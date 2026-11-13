#!/usr/bin/env python3
"""pl_sender.py -- interfaz de envio del paquete y su DOBLE de simulacion (SenderSim). SIN red, SIN firma, SIN py-clob-client. La interfaz replica la de sonda1.EnvioReal/EnvioSeco:
    tick(tok)->str | colocar(tok, precio, size, clave)->(oid_local, handle) [firma local, NO envia] | enviar(handle)->resp [POST] | estado(oid)->(size_matched|None, status|None) | cancelar(oid)->bool |
    saldo()->float|None | abiertas(tok)->[oid]|None | anclas_directas()->int|None (solo real: cuenta del canal de usuario).
Relojes inyectables (Reloj real / RelojVirtual) para que los tests corran en tiempo virtual y deterministas."""
import time, hashlib, random, threading, collections


class Reloj:
    """Reloj LOCAL unico del paquete: hora de pared (UTC, time.time_ns) leida UNA vez al arrancar y avanzada con time.monotonic_ns => inmune a saltos/steps del reloj del sistema durante el run (los plazos de hold y los d_proc usan este reloj).
    Todo `*_ns` del ledger esta en este reloj; las horas del EXCHANGE solo vienen del canal de usuario (pl_core.reloj_stats mide la diferencia, no se supone)."""
    def __init__(self): self.w0 = time.time_ns(); self.m0 = time.monotonic_ns()
    def now_ns(self): return self.w0 + (time.monotonic_ns() - self.m0)
    def wall_ns(self): return time.time_ns()
    def sleep(self, s, abortar=None):
        """Sueno en rodajas de <= 50 ms. `abortar` (callable sin argumentos que solo LEE una bandera; sin locks ni Event, hallazgos 2 y 3) permite que el cuerpo del run despierte a una senal; SIN `abortar` el sueno es completo:
        asi el barrido final (cancelaciones, backoffs, esperas de asentamiento) duerme de verdad aunque haya senales pendientes."""
        if s <= 0: return
        if abortar is None: time.sleep(s); return
        fin = time.monotonic() + s
        while not abortar():
            rest = fin - time.monotonic()
            if rest <= 0: return
            time.sleep(min(0.05, rest))


class RelojVirtual:
    def __init__(self, t0_ns=1_790_000_000_000_000_000): self.t = int(t0_ns)
    def now_ns(self): return self.t
    def sleep(self, s, abortar=None):
        if s > 0 and not (abortar is not None and abortar()): self.t += int(s * 1e9)             # igual que Reloj: con `abortar` y bandera levantada el sueno es no-op; sin `abortar`, completo
    def avanzar_ns(self, ns): self.t += int(ns)


class ErrHTTP(Exception):
    def __init__(self, status, msg=''): super().__init__(f'{status} {msg}'); self.status_code = status; self.error_msg = msg


class Limitador:
    """Ventana deslizante de 1 s: maximo `por_s` peticiones/s en TODO el proceso (POST+DELETE+lecturas). Espera con el reloj inyectado."""
    def __init__(self, reloj, por_s):
        self.r = reloj; self.por_s = por_s; self.t = collections.deque(); self.n = 0

    def registrar(self):
        """Cuenta una peticion SIN esperar (las cancelaciones no se retrasan nunca por el limitador)."""
        self.t.append(self.r.now_ns()); self.n += 1

    def esperar(self):
        while True:
            ahora = self.r.now_ns(); lim = ahora - 1_000_000_000
            while self.t and self.t[0] <= lim: self.t.popleft()
            if len(self.t) < self.por_s: self.t.append(ahora); self.n += 1; return
            self.r.sleep(max(0.005, (self.t[0] + 1_000_000_000 - ahora) / 1e9))


class SenderSim:
    """Doble determinista. Escenarios inyectables (todos por NUMERO de llamada o por clave, sin azar oculto):
       lat_post_ms / lat_cancel_ms / lat_get_ms (latencias de red simuladas, avanzan el reloj virtual), err_429_en_post {n_llamada}, err_ambiguo_post {n} (la orden SI queda viva pero la respuesta se pierde con excepcion de red),
       rechazo_post {n} (400 crosses book), fill_a {oid_idx: (size_rellena, t_s_tras_alta)} (relleno total/parcial simulado), cancel_falla {n} (cancelar devuelve False), cancel_pendiente {n} (ErrHTTP 'pending'),
       saldo_inicial, saldo_ilegible_en {n}, fuga: cualquier alta con tok no-valido. Lleva el LIBRO de ordenes y el saldo (colateral reservado no resta del saldo, como on-chain)."""
    real = False

    def __init__(self, reloj, saldo_inicial=0.612681, lat_post_ms=85.0, lat_cancel_ms=62.0, lat_get_ms=40.0, err_429_en_post=(), err_ambiguo_post=(), rechazo_post=(), fill_a=None, cancel_falla=(),
                 cancel_pendiente=(), saldo_ilegible_en=(), anclas_por_orden=True, tick='0.01', cancel_429=(), push_delay_s=0.15, index_delay_s=0.0, preparar_dur_s=0.0, preparar_falla=(), sin_push=False, chrony_s=0.0, oid_servidor_distinto=(), gtd_rechazado=False, chrony_extra=None, abiertas_ajenas=(), cancel_falla_por_oid=0):
        self.r = reloj; self.saldo_v = float(saldo_inicial); self.lat_post = lat_post_ms; self.lat_cancel = lat_cancel_ms; self.lat_get = lat_get_ms
        self.err_429 = set(err_429_en_post); self.err_amb = set(err_ambiguo_post); self.rech = set(rechazo_post); self.fill_a = dict(fill_a or {}); self.cancel_falla = set(cancel_falla); self.cancel_pend = set(cancel_pendiente)
        self.saldo_ileg = set(saldo_ilegible_en); self.tick_v = tick; self.cancel_429 = set(cancel_429)
        self.push_delay = push_delay_s; self.index_delay = index_delay_s; self.prep_dur = preparar_dur_s; self.prep_falla = set(preparar_falla); self.sin_push = sin_push; self.n_prep = 0; self.prep_log = []
        self.gtd_rechazado = gtd_rechazado; self.chrony_extra = dict(chrony_extra or {}); self.cfo_k = cancel_falla_por_oid; self.cfo = {}; self.ajenas = list(abiertas_ajenas); self.chrony_s = chrony_s; self.oid_srv_dist = set(oid_servidor_distinto); self.n_post = self.n_cancel = self.n_saldo = self.n_colocar = 0; self.colocados = []; self.ordenes = {}; self.posts_enviados = []; self.cancelaciones = []; self.anclas = 0; self.anclas_por_orden = anclas_por_orden

    def tick(self, tok): return self.tick_v

    def chrony(self):
        """Doble de leer_chrony(): None = no disponible; si no, dict(system_time_s=offset del reloj local respecto a NTP)."""
        if self.chrony_s is None: return None
        return dict(dict(system_time_s=float(self.chrony_s), last_offset_s=0.0, stratum=2, ref_id='65D8456C', leap='Normal', root_dispersion_s=0.001, root_delay_s=0.04), **self.chrony_extra)

    def _vivas_ahora(self):
        t = self.r.now_ns(); return sum(1 for o in self.ordenes.values() if self._estado_en(o, t)[1] == 'LIVE')

    def preparar(self, tok):
        """Doble del gate del canal de usuario: consume tiempo de reloj y registra CUANTAS ordenes habia vivas cuando se llamo (el paquete debe llamarlo con 0 vivas: no retrasa cancelaciones)."""
        self.n_prep += 1; self.prep_log.append((self.r.now_ns(), self._vivas_ahora())); self.r.sleep(self.prep_dur); return self.n_prep not in self.prep_falla

    def fills_push(self):
        """Doble del canal de usuario: {oid: matched} de las ordenes cuyo relleno ya llego POR PUSH (relleno + push_delay_s). Nunca consulta get_order."""
        if self.sin_push: return {}
        t = self.r.now_ns() - int(self.push_delay * 1e9); out = {}
        for oid, o in self.ordenes.items():
            m, _ = self._estado_en(o, t)
            if m > 1e-9: out[oid.lower()] = m
        return out

    def colocar(self, tok, precio, size, clave, neg_risk=None, expira_s=None):
        """Firma local (doble: solo calcula un id). v3: recibe el neg_risk verificado en gamma y la expiracion dura (GTD); el doble los REGISTRA para que los tests comprueben que el orquestador los pasa."""
        if not isinstance(expira_s, (int, float)) or expira_s < 185: raise RuntimeError('orden sin GTD (expira_s >= 185): el doble tampoco firma GTC (v6)')
        self.colocados.append(dict(tok=tok, neg_risk=neg_risk, expira_s=expira_s)); self.n_colocar += 1; oid = '0x' + hashlib.sha256(f'{tok}|{precio}|{size}|{clave}|{self.n_colocar}'.encode()).hexdigest()[:40]
        return oid, dict(oid=oid, tok=tok, precio=precio, size=size, neg_risk=neg_risk, expira_s=expira_s)

    def _estado_en(self, o, t_ns):
        """(matched, status) de la orden `o` en el instante t_ns segun el escenario (relleno programado o cancelacion)."""
        m = 0.0
        if o.get('fill'):
            s_rell, t_rel_ns = o['fill']
            if t_ns >= t_rel_ns and not (o.get('cancel_ns') is not None and o['cancel_ns'] < t_rel_ns): m = s_rell
        if m >= o['size'] - 1e-9: return m, 'MATCHED'
        if o.get('cancel_ns') is not None and t_ns >= o['cancel_ns']: return m, 'CANCELED'
        if o.get('expira_ns') is not None and t_ns >= o['expira_ns']: return m, 'EXPIRED'                 # GTD: el exchange la retira solo (cota dura de vida)
        return m, 'LIVE'

    def enviar(self, handle):
        self.n_post += 1; n = self.n_post; self.r.sleep(self.lat_post / 2000.0)           # ida
        oid = handle['oid']
        if not handle.get('expira_s'): raise RuntimeError('orden sin GTD: el doble tampoco admite GTC (v6)')
        if n in self.err_429: self.r.sleep(self.lat_post / 2000.0); raise ErrHTTP(429, 'Too Many Requests')
        if n in self.rech: self.r.sleep(self.lat_post / 2000.0); return {'success': False, 'errorMsg': 'invalid post-only order: order crosses book'}
        if handle.get('expira_s') and (handle['expira_s'] < 180 or self.gtd_rechazado):                # regla de los docs (12-Nov): GTD exige expiracion >= now + 3 min; `gtd_rechazado` simula que el CLOB no admite GTD+post-only
            self.r.sleep(self.lat_post / 2000.0); return {'success': False, 'errorMsg': 'invalid expiration value: GTD order expiration must be at least 3 minutes in the future'}
        t_alta = self.r.now_ns(); idx = len(self.posts_enviados); self.posts_enviados.append(dict(oid=oid, tok=handle['tok'], precio=handle['precio'], size=handle['size'], t_alta_ns=t_alta, n=n))
        o = dict(handle, t_alta_ns=t_alta, cancel_ns=None, fill=None, expira_ns=(t_alta + int((handle['expira_s'] - 60) * 1e9)) if handle.get('expira_s') else None)         # el exchange la retira 60 s ANTES de la expiracion declarada
        if idx in self.fill_a: s_rell, dt_s = self.fill_a[idx]; o['fill'] = (float(s_rell), t_alta + int(dt_s * 1e9))
        if n in self.oid_srv_dist: oid = '0x' + hashlib.sha256(('srv|' + oid).encode()).hexdigest()[:40]            # el servidor devuelve (y conoce la orden por) un id DISTINTO del hash local
        self.ordenes[oid] = o; self.r.sleep(self.lat_post / 2000.0)
        if n in self.err_amb: raise ErrHTTP(None, 'timeout leyendo la respuesta')              # status None => ambiguo; la orden SI esta viva
        return {'success': True, 'orderID': oid, 'status': 'live', 'errorMsg': ''}

    def estado(self, oid):
        self.r.sleep(self.lat_get / 2000.0); o = self.ordenes.get(oid)
        if o is not None and self.r.now_ns() - o['t_alta_ns'] < int(self.index_delay * 1e9): o = None                 # aun sin indexar: get_order devuelve null (NO_EXISTE)
        if o is None: self.r.sleep(self.lat_get / 2000.0); return None, 'NO_EXISTE'
        r = self._estado_en(o, self.r.now_ns()); self.r.sleep(self.lat_get / 2000.0); return r

    def cancelar(self, oid):
        self.n_cancel += 1; n = self.n_cancel; self.r.sleep(self.lat_cancel / 2000.0)
        if n in self.cancel_429: self.r.sleep(self.lat_cancel / 2000.0); raise ErrHTTP(429, 'Too Many Requests')
        if n in self.cancel_pend: self.r.sleep(self.lat_cancel / 2000.0); raise ErrHTTP(400, "order can't be canceled because it is pending/delayed")
        o = self.ordenes.get(oid); self.r.sleep(self.lat_cancel / 2000.0)
        if o is not None and self.r.now_ns() - o['t_alta_ns'] < int(self.index_delay * 1e9): return False                  # 'not found' mientras no esta indexada
        self.cfo[oid] = self.cfo.get(oid, 0) + 1                                          # v5: las primeras `cancel_falla_por_oid` cancelaciones de CADA orden devuelven False (como `cancel_falla` pero por orden y no global)
        if o is None or n in self.cancel_falla or self.cfo[oid] <= self.cfo_k: return False
        m, est = self._estado_en(o, self.r.now_ns())
        if est != 'LIVE': self.cancelaciones.append((oid, False)); return False                  # ya casada/cancelada: no es una cancelacion exitosa
        o['cancel_ns'] = self.r.now_ns(); self.cancelaciones.append((oid, True)); self.anclas += 1 if self.anclas_por_orden else 0; return True

    def saldo(self):
        self.n_saldo += 1
        if self.n_saldo in self.saldo_ileg: return None
        gasto = sum(self._estado_en(o, self.r.now_ns())[0] * o['precio'] for o in self.ordenes.values())
        return round(self.saldo_v - gasto, 6)

    def abiertas_todas(self):
        """v5 (hallazgo 4): TODAS las ordenes abiertas de la wallet (sin filtro de asset), incluidas las ajenas al run (`abiertas_ajenas`, solo en el doble)."""
        t = self.r.now_ns()
        return [oid for oid, o in self.ordenes.items() if t - o['t_alta_ns'] >= int(self.index_delay * 1e9) and self._estado_en(o, t)[1] == 'LIVE'] + list(self.ajenas)

    def abiertas(self, tok):
        t = self.r.now_ns()
        return [oid for oid, o in self.ordenes.items() if o['tok'] == tok and t - o['t_alta_ns'] >= int(self.index_delay * 1e9) and self._estado_en(o, t)[1] == 'LIVE']          # sin indexar tampoco aparece en abiertas

    def anclas_directas(self): return self.anclas

    def cerrar(self): pass


class MercadosSim:
    """Fuente de mercados 5m simulada: (slug, coin, fin_s, [tok_up, tok_down], neg_risk) y libro REST (bids, asks) por token. Mercados rotan cada 300 s con el reloj."""
    def __init__(self, reloj, coins=('BTC', 'ETH', 'SOL', 'XRP'), bid=0.40, ask=0.45, down_barato=False):
        self.r = reloj; self.coins = coins; self.bid = bid; self.ask = ask; self.libros = {}; self.down_barato = down_barato      # down_barato: el token '...D' tiene bid 0,01 / ask 0,02 con cola (para la fase B)

    def mercados(self, coin=None):
        t = self.r.now_ns() // 1_000_000_000; ini = (t // 300) * 300; out = []
        for c in (self.coins if coin is None else [x for x in self.coins if x == coin]):
            for k in (0, 1):
                f = ini + 300 * (1 + k); out.append((f'{c.lower()}-updown-5m-{f - 300}', c, f, [f'{c}{f}U', f'{c}{f}D'], False))
        return [m for m in out if m[2] - t >= 1]

    def libro(self, tok):
        b, a = self.libros.get(tok, (0.01, 0.02) if (self.down_barato and tok.endswith('D')) else (self.bid, self.ask)); return [(b, 100.0)], [(a, 100.0)]
