#!/usr/bin/env python3
"""pl_sender_real.py -- ADAPTADOR REAL (NO se importa en dry-run ni en los tests de seguridad; solo `paquete_l.py --real` + fichero de confirmacion). Capa FINA sobre codigo ya revisado de la Sonda1 que va VENDORIZADO en vendor/ (sha256 en
vendor/VENDOR_HASHES.json; `pl_core.cargar_vendor` ejecuta EXACTAMENTE los bytes verificados, SIN tocar sys.path; el paquete NO importa nada de dev ni de main, ni `live_trade`, ni lee data/live/.env):
  * vendor/envio_real.py (extracto verbatim de sonda1.EnvioReal): firma local (create_order + hash EIP-712 antes del POST), get_order, cancel_order, saldo on-chain, abiertas. v3: `clase_envio` lo subclasifica (aqui, revisable) para el GTD de
    cota dura y para exigir el neg_risk de gamma.
  * vendor/vendor_main.py (GENERADO): cliente de la wallet DEDICADA (ruta fija, wallet exacta), redondeo CLOB (verbatim de live_trade, como texto), saldo on-chain por RPC publico.
  * vendor/cancel_evidencia.py (copia verbatim): canal de USUARIO del CLOB, alta/cancel_try y gate_envio. Sus avisos por Telegram (subproceso que importaria shadow_digest de main) se SUSTITUYEN por un aviso a fichero/log.
Mercados: gamma PUBLICO (solo GET), cada evento VALIDADO contra lo que el paquete supone (pl_core.verificar_mercado_gamma). NUNCA se ejecuta sin /code-review + OK final de Javi."""
import os, sys, json, time, types, collections, threading
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import pl_core as C
import re

HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
VENDOR = HERE + 'vendor/'
GAMMA = 'https://gamma-api.polymarket.com'
CLOB = 'https://clob.polymarket.com'


class MercadosReal:
    """Mercados 5m de las 4 monedas (slug {coin}-updown-5m-{ini}) por gamma publico, con cache de TTL corto. Solo lectura. `get` inyectable (tests)."""
    def __init__(self, coins=('BTC', 'ETH', 'SOL', 'XRP'), get=None, ttl_s=15.0, reloj=time.time):
        self.coins = coins; self.get = get; self.ttl = ttl_s; self.reloj = reloj; self.cache = {}; self.libros = {}; self.rechazados = {}

    def _get(self, url, params, timeout=2.5):                      # v4 (hallazgo 9): timeout acotado (la seleccion de mercado ocurre con 0 vivas, pero no debe colgarse)
        if self.get: return self.get(url, params)
        import requests
        return requests.get(url, params=params, timeout=timeout).json()

    def _slug(self, coin, ini):
        slug = f'{coin.lower()}-updown-5m-{ini}'; t = self.reloj(); c = self.cache.get(slug)
        if c and t - c[0] < self.ttl: return c[1]
        r = None
        try:
            ev = self._get(f'{GAMMA}/events', {'slug': slug}); ok, why, toks, neg = C.verificar_mercado_gamma(coin, ini, ev[0] if ev else None)
            if ok: r = (toks, neg)
            else: self.rechazados[slug] = why
        except Exception as e: self.rechazados[slug] = f'gamma:{type(e).__name__}'
        self.cache[slug] = (t, r); return r

    def mercados(self, coin=None):
        """v4 (hallazgo 9): con `coin` solo se consultan los 2 slots de ESA moneda (el orquestador pide la del slot); sin `coin`, las 4 (solo `--verificar-mercados`)."""
        ahora = self.reloj(); base = int(ahora // 300) * 300; out = []
        for c in (self.coins if coin is None else [x for x in self.coins if x == coin]):
            for k in (0, 1):
                ini = base + 300 * k; slug = f'{c.lower()}-updown-5m-{ini}'; r = self._slug(c, ini)
                if r: out.append((slug, c, ini + 300, r[0], r[1]))                 # toks = [Up, Down] VERIFICADO por etiqueta
        return out

    def libro(self, tok):
        r = self._get(f'{CLOB}/book', {'token_id': tok}, timeout=1.5)                         # v3: el libro justo antes del POST no puede tardar (hallazgo 2)
        bids = sorted(((float(x['price']), float(x['size'])) for x in r.get('bids', [])), reverse=True); asks = sorted((float(x['price']), float(x['size'])) for x in r.get('asks', []))
        return bids, asks


def leer_chrony():
    """Offset del reloj del sistema segun chrony (solo lectura de `chronyc tracking`); None si no esta disponible. Se registra en el manifiesto de un run con reloj real."""
    import subprocess
    try: out = subprocess.run(['chronyc', 'tracking'], capture_output=True, text=True, timeout=3).stdout
    except Exception: return None
    m = re.search(r'System time\s*:\s*([0-9.eE+-]+) seconds (fast|slow) of NTP time', out); n = re.search(r'Last offset\s*:\s*([+-]?[0-9.eE+-]+) seconds', out)
    if not m: return None
    g = lambda pat: (re.search(pat, out) or [None, None])[1]; f = lambda v: float(v) if v is not None else None
    # v5 (hallazgo 3): ademas del offset, el estado de sincronizacion (un chrony SIN sincronizar tambien imprime 'System time : 0.0 seconds'): se juzga en pl_core.reloj_sincronizado
    return dict(system_time_s=float(m.group(1)) * (1 if m.group(2) == 'fast' else -1), last_offset_s=float(n.group(1)) if n else None, stratum=f(g(r'Stratum\s*:\s*(\d+)')), ref_id=g(r'Reference ID\s*:\s*([0-9A-Fa-f]+)'),
                leap=(g(r'Leap status\s*:\s*(.+)') or '').strip() or None, root_dispersion_s=f(g(r'Root dispersion\s*:\s*([0-9.eE+-]+) seconds')), root_delay_s=f(g(r'Root delay\s*:\s*([0-9.eE+-]+) seconds')))


class SenderReal:
    """Interfaz de pl_sender.SenderSim sobre sonda1.EnvioReal + cancel_evidencia."""
    real = True

    def __init__(self, env, reg, res, ce, evid_dir, espera_gate_s=6.0):
        self.env, self.reg, self.res, self.ce, self.evid_dir = env, reg, res, ce, evid_dir; self.espera_gate_s = espera_gate_s; self._t_envio = {}
        self._tail = C.EvidTail(os.path.join(evid_dir, 'cancel_evid_*.jsonl*'))

    def tick(self, tok): return self.env.tick(tok)

    def preparar(self, tok):
        """Resuelve el conditionId del token y espera (hasta espera_gate_s) a que el canal de usuario este suscrito al mercado ANTES de firmar/enviar. False => no se envia (fail-closed)."""
        try: self.res.pedir(tok)
        except Exception: pass
        ok, motivo = self.reg.gate_envio(tok, self.env, espera_s=self.espera_gate_s, fase='paquete_l')
        return ok

    def colocar(self, tok, precio, size, clave, neg_risk=None, expira_s=None):
        """Firma local (NO envia). v3: el neg_risk de gamma es OBLIGATORIO (el cliente lo contrasta y se niega a firmar si difiere) y `expira_s` fija la expiracion dura GTD."""
        if neg_risk is None: raise RuntimeError('neg_risk de gamma ausente: no firmo')
        oid, signed = self.env.poner(tok, precio, size, clave, neg_risk=neg_risk, expira_s=expira_s)
        return oid, dict(oid=oid, signed=signed, tok=tok, precio=precio, gtd=bool(expira_s))

    def enviar(self, handle):
        """POST. v3 (hallazgo 8): el POST pasa por el camino `Puja.lanzar` de cancel_evidencia (hilo marcado en `CE._TL`), cuyo re-chequeo del gate es INSTANTANEO (espera_s=0.0, sin dormir): el camino 'suelto' esperaba hasta 2 s DENTRO del
        POST, lo que retrasaba cualquier cancelacion vencida y contaminaba t_send/d_red. La ESPERA real del gate ocurre en `preparar` (con 0 ordenes vivas). t0 se toma justo antes de la llamada."""
        TL = self.ce._TL; TL.env, TL.tok, TL.gate, TL.bloqueado = self.env, handle['tok'], True, False
        t0 = time.time_ns() // 1_000_000; resp = None
        try: resp = self.env.enviar(handle['signed'], gtd=bool(handle.get('gtd')))
        finally:
            t1 = time.time_ns() // 1_000_000; bloqueado = bool(getattr(TL, 'bloqueado', False)); TL.env = TL.tok = None; TL.gate = False; TL.bloqueado = False
            # v4 (hallazgo 7): el alta de cancel_evidencia se registra con el oid que DEVUELVE el servidor (el que usaran PLACEMENT/CANCELLATION del canal de usuario); sin respuesta (excepcion), con el local.
            oid_srv = C.id_servidor(resp, handle['oid']); oid_alta = oid_srv or handle['oid']
            if oid_srv and getattr(self.reg, 'avisar', None):
                try: self.reg.avisar(f'ALARMA oid del servidor {oid_srv} != oid local {handle["oid"]}: alta registrada con el del servidor')
                except Exception: pass
            if not bloqueado: self.reg.alta(types.SimpleNamespace(oid=oid_alta, slug=None, tok=handle['tok'], precio=handle['precio'], t_envio=t0, t_ack=t1))        # un envio bloqueado por el gate NO es un alta: nada salio
        return resp

    def estado(self, oid): return self.env.estado(oid)
    def cancelar(self, oid): return self.env.cancelar(oid)
    def saldo(self): return self.env.saldo()
    def abiertas_todas(self): return self.env.abiertas_todas()

    def chrony(self): return leer_chrony()

    def fills_push(self):
        """Rellenos de nuestras ordenes que el canal de usuario ya escribio (lectura LOCAL de los JSONL del escritor; sin red). El escritor tiene un retraso de volcado de fracciones de segundo."""
        return self._tail.sondear()

    def anclas_directas(self):
        """Espera a que el hilo escritor vuelque y cuenta anclas validas (alta+PLACEMENT+CANCELLATION+cancel_try) del JSONL del canal de usuario."""
        time.sleep(1.5)
        try: self.reg.w.vaciar(timeout=5.0)
        except Exception: pass
        return C.contar_anclas(os.path.join(self.evid_dir, 'cancel_evid_*.jsonl*'))[0]

    def cerrar(self):
        try: self.reg.w.cerrar()
        except Exception: pass


def clase_envio(ER):
    """Subclase REVISABLE de vendor/envio_real.EnvioReal (el extracto verbatim no se edita). v3: (a) `poner` exige el neg_risk de gamma y lo contrasta con el del cliente (hallazgo 10); (b) `expira_s` -> expiracion GTD (hallazgo 3: cota dura de vida
    en el exchange; en el struct EIP-712 V2 la expiracion NO entra, asi que el orderID local no cambia); (c) `enviar` manda SIEMPRE GTD post-only: v6, sin modo GTC (sin expiracion `poner` y `enviar` lanzan). NO verificado contra el CLOB real: si rechazara GTD+post-only
    saldria 'rechazo' => BLOCKED tras 2 rechazos y SIN gasto (fail-safe)."""
    class EnvioPaquete(ER.EnvioReal):
        def poner(self, tok, precio, size, clave, neg_risk=None, expira_s=None):
            from py_clob_client_v2 import OrderArgsV2, PartialCreateOrderOptions
            if neg_risk is None: raise RuntimeError('neg_risk de gamma ausente: no firmo')
            nr = self._neg_risk(tok)
            if bool(neg_risk) != bool(nr): raise RuntimeError(f'neg_risk del mercado (gamma {bool(neg_risk)}) != cliente ({bool(nr)}): no firmo')
            if not expira_s: raise RuntimeError('sin expiracion GTD: no firmo (v6: no existe modo GTC)')
            exp = int(time.time()) + int(expira_s)                                                        # el orquestador exige chrony legible y |offset| <= 1 s ANTES de cada lote (v4, hallazgo 4)
            signed = self.cli.create_order(OrderArgsV2(token_id=tok, price=precio, size=size, side='BUY', expiration=exp), PartialCreateOrderOptions(neg_risk=bool(nr)))
            return self.M.hash_orden(signed, bool(nr)), signed

        def enviar(self, signed, gtd=False):
            from py_clob_client_v2 import OrderType
            if not gtd: raise RuntimeError('orden sin GTD: no envio (v6: no existe modo GTC)')
            return self.cli.post_order(signed, OrderType.GTD, post_only=True)

        def abiertas_todas(self):
            """v5 (hallazgo 4): get_open_orders SIN filtro de asset (toda la wallet), todas las paginas; None si ilegible/paginacion no garantizada. (El `abiertas(tok)` verbatim filtra por token y no se usa.)"""
            from py_clob_client_v2 import OpenOrderParams
            try:
                res = self.cli.get_open_orders(OpenOrderParams(), only_first_page=False)
                if not isinstance(res, list) or not all(isinstance(o, dict) for o in res): return None
                return [str(o.get('id') or '') for o in res]
            except Exception: return None
    return EnvioPaquete


def aviso_a_fichero(evid_dir):
    """Sustituye `Registro.avisar` (que lanzaba un subproceso con `shadow_digest` de main = codigo fuera de codigo_sha): el aviso queda en run.log (via stderr) y en ALERTA_paquete_l.txt."""
    def avisar(msg):
        try:
            print(f'ALERTA registro: {msg}', file=sys.stderr, flush=True)
            with open(os.path.join(evid_dir, 'ALERTA_paquete_l.txt'), 'a') as f: f.write(f'{time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())} {msg}\n')
        except Exception: pass
    return avisar


def cargar_env(cfg):
    """v5 (hallazgo 9): UNICO camino que usan `construir` (envio real) y `preflight`: vendor verificado por hash, wallet del vendor == cfg.wallet, cliente dedicado (fail-closed: sys.exit si la wallet de deposito no es exactamente la autorizada
    o si comparte credenciales con produccion) y wallet del cliente == cfg.wallet. Devuelve (env, CE). TODO se carga de vendor/ con `C.cargar_vendor` (sys.path intacto); jamas de dev ni de main."""
    ok, mal = C.verificar_vendor(HERE)
    if not ok: sys.exit(f'vendor/ alterado o incompleto ({mal}): NO envio (regenerar con vendor/regenerar_vendor.py y re-revisar)')
    V = C.cargar_vendor('vendor_main', HERE); ER = C.cargar_vendor('envio_real', HERE); CE = C.cargar_vendor('cancel_evidencia', HERE); C.cargar_vendor('plan_paquete_l', HERE)
    if V.WALLET_DEDICADA.lower() != cfg.wallet.lower(): sys.exit('vendor_main.WALLET_DEDICADA != cfg.wallet: NO envio')
    env = clase_envio(ER)()
    wallet = str(getattr(env, 'wallet', '') or '')
    if wallet.lower() != cfg.wallet.lower(): sys.exit(f'wallet del cliente ({wallet}) != wallet dedicada autorizada ({cfg.wallet}): NO envio')
    return env, CE


def construir(cfg, evid_dir):
    """Devuelve (sender, mercados, anclas_fn, por_moneda_fn, libro_fn). Fail-closed."""
    env, CE = cargar_env(cfg); os.makedirs(evid_dir, exist_ok=True)
    reg = CE.Registro(CE.Escritor(evid_dir)); res = CE.Resolutor(reg); reg.resolutor = res; reg.avisar = aviso_a_fichero(evid_dir)
    CE.adjuntar_env(env, reg, markets=(), canal=True, resolutor=res, modo_markets='lista')           # modo explicito: no se lee SONDA1_CANCEL_EVIDENCIA_MARKETS del entorno
    if not getattr(env, '_cancel_evid', False) or reg.canal is None: sys.exit('canal de usuario NO adjuntado: NO envio')
    sender = SenderReal(env, reg, res, CE, evid_dir); mercados = MercadosReal()
    por_fn = lambda filas: C.contar_anclas(os.path.join(evid_dir, 'cancel_evid_*.jsonl*'), filas)[1]
    return sender, mercados, sender.anclas_directas, por_fn, mercados.libro


# ------------------------------------------------------------------------------------------------ PREFLIGHT (R1, 12-Nov): SOLO LECTURA, jamas un POST
def _prohibido(*a, **k): raise AssertionError('PREFLIGHT: envio PROHIBIDO (modo solo lectura)')


def _esperado_orden(precio, size, tok, wallet, exp_aprox, ahora):
    """Forma esperada de una orden V2 BUY a `precio` de `size` acciones, firmada por la wallet dedicada (POLY_1271 = 3): importes en micro-unidades (6 decimales)."""
    return dict(makerAmount=str(int(round(precio * size * 1e6))), takerAmount=str(int(round(size * 1e6))), tokenId=str(tok), maker=wallet.lower(), signatureType=3, exp_min=int(ahora) + exp_aprox - 5, exp_max=int(ahora) + exp_aprox + 5)


def comprobar_orden_firmada(signed, oid, esperado):
    """Compara la orden firmada LOCALMENTE (sin enviar) con la forma esperada; devuelve {comprobacion: bool}. No imprime ni devuelve ninguna clave/firma (solo booleanos)."""
    g = lambda n: getattr(signed, n, None)
    side = g('side'); side_ok = str(getattr(side, 'name', side)).upper().endswith('BUY') or side in (0, '0')
    try: exp = int(g('expiration'))
    except (TypeError, ValueError): exp = -1
    try: st = int(getattr(g('signatureType'), 'value', g('signatureType')))
    except (TypeError, ValueError): st = -1
    oid_s = str(oid or '')
    return dict(importe_maker=str(g('makerAmount')) == esperado['makerAmount'], importe_taker=str(g('takerAmount')) == esperado['takerAmount'], token=str(g('tokenId')) == esperado['tokenId'],
                lado_buy=side_ok, maker_es_wallet_dedicada=str(g('maker') or '').lower() == esperado['maker'], signature_type_1271=(st == esperado['signatureType']),
                expiracion_en_rango=(esperado['exp_min'] <= exp <= esperado['exp_max']), firma_presente=bool(g('signature')),
                hash_formato_32_bytes=bool(re.fullmatch(r'0x[0-9a-fA-F]{64}', oid_s)))


def preflight(cfg, autenticado=True, get=None, env_factory=None, chrony=None, ahora=time.time):
    """Comprobacion SOLO LECTURA (R1). NUNCA envia: antes de tocar nada `enviar`/`post_order` del cliente se sustituyen por una funcion que lanza.
    A) PUBLICO (sin credenciales): por moneda (BTC/ETH/SOL/XRP) el mercado 5m (el de mas vida) por gamma + las mismas validaciones del envio real, y GET /book de sus 2 tokens: tick_size 0,01, min_order_size <= 5, neg_risk == gamma, el libro (asks/bids) se
       informa como `operable_ahora` sin ser requisito.
    B) AUTENTICADO (`autenticado=True`; lee el fichero de credenciales de la wallet DEDICADA en `cliente_dedicado`; wallet exacta, credenciales != produccion): API creds derivadas == las del fichero (GET /auth/derive-api-key, firma L1 de autenticacion),
       saldo on-chain (GET RPC), open orders de TODA la wallet sin filtro de asset (GET autenticado: [] esperado), reloj (chrony SINCRONIZADO: leap Normal, stratum 1-9, ref id externo (!= 0, offset y root dispersion acotados) y UNA orden de prueba firmada EN LOCAL (no se envia) cuya forma se compara con lo esperado.
       NOTA (v5, hallazgo 8): el hash EIP-712 local NO se valida aqui contra nada independiente (recalcularlo con la misma funcion seria tautologico): solo se comprueba su FORMATO (32 bytes). Se valida de verdad en el 1.er POST real: el orderID que devuelve el servidor debe ser el hash local (si no, alarma + BLOCKED, hallazgo 7 v4).
    Devuelve dict `ok` + secciones; solo booleanos/cifras/ids publicos (ninguna clave, secreto ni firma)."""
    R = dict(ok=False, version=C.VERSION, ts_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(ahora())), monedas={}, autenticado=None, errores=[])
    mk = MercadosReal(get=get, reloj=ahora); fallos = R['errores']; tokens = []; neg_de = {}
    for c in C.COINS:
        info = dict(mercado=None, tokens=[], ok=False)
        try: ms = mk.mercados(c)
        except Exception as e: ms = []; fallos.append(f'{c}: gamma {type(e).__name__}')
        if not ms: fallos.append(f'{c}: sin mercado 5m verificado ({list(mk.rechazados.values())[-2:]})'); R['monedas'][c] = info; continue
        slug, coin, fin, toks, neg = max(ms, key=lambda m: m[2]); info['mercado'] = slug; info['neg_risk_gamma'] = neg; ok_c = True                  # el de MAS vida (el 5m actual puede estar ya decidido: ask 0,01 sin bids)
        for lado, tok in zip(('Up', 'Down'), toks):
            t = dict(lado=lado, token_fin=str(tok)[-8:])
            try:
                r = mk._get(f'{CLOB}/book', {'token_id': tok}, timeout=2.5)
                bids = [float(x['price']) for x in r.get('bids', [])]; asks = [float(x['price']) for x in r.get('asks', [])]
                t.update(tick_size=str(r.get('tick_size')), min_order_size=str(r.get('min_order_size')), neg_risk_book=r.get('neg_risk'), version=r.get('version'), n_bids=len(bids), n_asks=len(asks), mejor_ask=(min(asks) if asks else None), mejor_bid=(max(bids) if bids else None))
                t['ok'] = (abs(float(r.get('tick_size')) - 0.01) < 1e-9 and float(r.get('min_order_size')) <= cfg.size + 1e-9 and isinstance(r.get('neg_risk'), bool) and r.get('neg_risk') == neg)                      # DURO: tick/minsize/neg_risk. El estado del libro es INFORMATIVO (operable_ahora): cambia cada segundo
                t['operable_ahora'] = bool(asks) and min(asks) >= cfg.ask_min - 1e-9 and bool(bids) and max(bids) >= cfg.bid_min_lejos - 1e-9
            except Exception as e: t['ok'] = False; t['error'] = f'{type(e).__name__}: {str(e)[:80]}'
            if not t['ok']: fallos.append(f'{c} {lado}: libro/tick/minsize/neg_risk no valido {t}'); ok_c = False
            info['tokens'].append(t); tokens.append((c, lado, tok)); neg_de[tok] = neg
        info['ok'] = ok_c; R['monedas'][c] = info
    pub_ok = all(v.get('ok') for v in R['monedas'].values()) and len(R['monedas']) == len(C.COINS)
    if not autenticado: R['ok'] = bool(pub_ok); return R
    A = R['autenticado'] = dict(ok=False); ch = (chrony or leer_chrony)(); A['reloj_chrony'] = ch if isinstance(ch, dict) else None; A['reloj_ok'] = C.reloj_sincronizado(ch, cfg)       # v5 (R3): sincronizado de verdad, no solo offset 0
    try:
        env = (env_factory or (lambda c: cargar_env(c)[0]))(cfg)
    except SystemExit as e: A['error'] = f'cliente_dedicado se nego a arrancar: {str(e)[:160]}'; fallos.append(A['error']); return R
    except Exception as e: A['error'] = f'cliente: {type(e).__name__}: {str(e)[:120]}'; fallos.append(A['error']); return R
    env.enviar = _prohibido                                                                       # ANTES de cualquier otra cosa: imposible hacer un POST desde aqui
    if getattr(env, 'cli', None) is not None:
        for n in ('post_order', 'post_orders', 'create_and_post_order', 'create_and_post_market_order'): setattr(env.cli, n, _prohibido)
    A['wallet_es_la_dedicada'] = str(getattr(env, 'wallet', '') or '').lower() == cfg.wallet.lower()
    try:                                                                                          # credenciales API: las derivadas de la clave == las del fichero
        d = env.cli.derive_api_key(); c0 = env.cli.creds; A['api_creds_derivadas_coinciden'] = bool(d.api_key == c0.api_key and d.api_secret == c0.api_secret and d.api_passphrase == c0.api_passphrase)
    except Exception as e: A['api_creds_derivadas_coinciden'] = False; A['error_derive'] = f'{type(e).__name__}: {str(e)[:100]}'
    try: sal = env.saldo(); A['saldo_onchain_usd'] = sal; A['saldo_dentro_de_lo_autorizado'] = isinstance(sal, (int, float)) and cfg.max_simultaneas * cfg.coste_orden - 1e-9 <= sal <= cfg.saldo_autorizado + 0.05           # v6 (hallazgo 8): ademas del tope, el minimo para sostener las 12 vivas a la vez (12 x 0,05 = 0,60 $)
    except Exception as e: A['saldo_dentro_de_lo_autorizado'] = False; A['error_saldo'] = f'{type(e).__name__}: {str(e)[:100]}'
    try: ab = env.abiertas_todas()                                                                # v5 (hallazgo 4): TODA la wallet, sin filtro de asset
    except Exception: ab = None
    A['open_orders_total'] = len(ab) if isinstance(ab, list) else None; A['open_orders_legibles_y_vacias'] = isinstance(ab, list) and not ab
    if tokens:                                                                                    # orden de prueba EN LOCAL (no se envia): token BTC Up
        tok = tokens[0][2]; nr = neg_de[tok]; t0 = ahora()
        try:
            oid, signed = env.poner(tok, cfg.precio, cfg.size, 'preflight', neg_risk=nr, expira_s=cfg.gtd_expira_s)
            A['orden_firmada_local'] = comprobar_orden_firmada(signed, oid, _esperado_orden(cfg.precio, cfg.size, tok, cfg.wallet, cfg.gtd_expira_s, t0))
        except Exception as e: A['orden_firmada_local'] = dict(error=f'{type(e).__name__}: {str(e)[:120]}')
    f = A.get('orden_firmada_local') or {}
    A['ok'] = bool(A['wallet_es_la_dedicada'] and A.get('api_creds_derivadas_coinciden') and A.get('saldo_dentro_de_lo_autorizado') and A['open_orders_legibles_y_vacias'] and A['reloj_ok'] and f and all(v is True for v in f.values()))
    for k, v in list(A.items()):
        if v is False: fallos.append(f'autenticado.{k} = False')
    R['ok'] = bool(pub_ok and A['ok']); return R
