#!/usr/bin/env python3
"""paquete_l.py -- ORQUESTADOR del paquete de medicion de `l` (12-Nov-2026). POR DEFECTO ES UN DRY-RUN TOTAL: usa SenderSim + MercadosSim con reloj virtual; NO hay red de envio, no firma, no importa py-clob-client ni sonda1.
Envio REAL solo con `--real` Y `--confirmacion FICHERO` (que NO crea este codigo: lo escribe Javi tras /code-review) cuyo contenido fija config_sha, codigo_sha, wallet, perdida_dura y fase B; si algo no coincide, sale sin enviar.
Uso dry:   python3 -I paquete_l.py --out /ruta/out [--run-id ID] [--escenario base|fill|429|...]
Uso real:  python3 -I paquete_l.py --real --confirmacion /ruta/PAQUETE_L_OK.txt --out /ruta/out   (NO ejecutar sin /code-review + OK final de Javi)
INSTANCIA UNICA (v7): flock exclusivo no bloqueante por wallet y por --out (ficheros en C.LOCK_DIR, fuera de --out), tomado antes de leer/enviar nada; si esta tomado el proceso sale sin tocar nada (run/resume/liquidar-informe).
Contrato de largo plazo (mandato 12-Nov): run_manifest.json, ledger.jsonl (JSONL fsync, eid unico), checkpoint.json atomico, run.log con marca de tiempo, parcial_resumen.json tras CADA lote, informe_final.json con COMPLETE/PARTIAL/FAILED/BLOCKED
y cobertura exacta. Reanudacion idempotente: el LEDGER es la verdad; un slot con intencion nunca se reenvia; las vivas se reconcilian (estado/cancelar/abiertas/saldo) antes de seguir."""
import os, sys, json, time, math, argparse, datetime as dt, collections, signal, threading, shlex
sys.path.append(os.path.dirname(os.path.abspath(__file__)))            # v3: AL FINAL (no puede sombrear la libreria estandar); `exigir_aislamiento` vigila que el directorio no tenga .py ajenos
import pl_core as C
from pl_sender import Reloj, RelojVirtual, Limitador, SenderSim, MercadosSim

STATUS = ('COMPLETE', 'PARTIAL', 'FAILED', 'BLOCKED')
BENIGNOS = ('max_minutos', 'max_ordenes', 'slots_agotados')           # kills que NO impiden reanudar (limites de tiempo/cantidad del run); el resto exige decision humana
BENIGNOS_PREFIJO = ('fase_b_tope', 'senal_')                          # fin de fase B en su tope / parada ordenada por SIGTERM-SIGINT (el barrido ya cancelo todo): tampoco exigen decision humana


def exigir_confirmacion(ruta, cfg, codigo_sha):
    """Fail-closed: el fichero de confirmacion (escrito por Javi, NO por este codigo) debe contener paquete, config_sha, codigo_sha, wallet, perdida_dura y fase_b_max_rellenos IGUALES a los del proceso."""
    if not ruta or not os.path.exists(ruta): sys.exit(f'envio real exige --confirmacion con fichero existente ({ruta}): NO envio')
    kv = {}
    for l in open(ruta).read().splitlines():
        l = l.split('#')[0].strip()
        if '=' in l: k, v = l.split('=', 1); kv[k.strip()] = v.strip()
    esperado = dict(paquete=C.VERSION, config_sha=cfg.sha(), codigo_sha=codigo_sha, wallet=cfg.wallet.lower(), perdida_dura=f'{cfg.perdida_dura:g}', fase_b_max_rellenos=str(cfg.fase_b_max_rellenos))
    for k, v in esperado.items():
        if str(kv.get(k, '')).lower() != str(v).lower(): sys.exit(f'confirmacion no coincide en {k}: esperado {v}, fichero {kv.get(k)!r}: NO envio')
    return kv


def cfg_b(cfg): return cfg.fase_b_max_rellenos > 0


KILL_ORDEN = ('cancel_no_confirmada', 'estado_ilegible_tras_cancel', 'orden_indeterminada')        # v8 (hallazgos 4 y 8): UNICA fuente de los motivos de kill por orden (emision y resolucion)
PREF_RECHAZO = 'resume_rechazado_kill_previo:'
KILLS_TRANSITORIOS = ('saldo_ilegible_en_arranque', 'abiertas_previas_o_ilegibles')          # v10: lecturas de arranque que fallan SIN dejar ordenes vivas sin verificar: no cuentan como cambio de estado real (rechazo transitorio, no toca informe/manifiesto/checkpoint)


def motivo_kill_orden(tipo, clave):
    C.exigir(tipo in KILL_ORDEN, f'tipo de kill por orden desconocido: {tipo}'); return f'{tipo}:{clave}'


def base_kill(motivo):
    """Quita TODOS los prefijos de rechazo de resume (los rechazos repetidos no se anidan)."""
    m = str(motivo)
    while m.startswith(PREF_RECHAZO): m = m[len(PREF_RECHAZO):]
    return m


def motivo_rechazo_resume(motivo): return PREF_RECHAZO + base_kill(motivo)


class Paquete:
    def __init__(self, cfg, sender, mercados, dir_out, reloj, run_id, real=False, libro=None, anclas_fn=None, evid_patron=None, params=None, stdout=True, locks=None):
        self.cfg, self.s, self.m, self.dir, self.r, self.run_id, self.real = cfg, sender, mercados, dir_out, reloj, run_id, real
        self.libro = libro or (mercados.libro if hasattr(mercados, 'libro') else None); self.anclas_fn = anclas_fn; self.evid = evid_patron; self.params = params or {}; self.stdout = stdout
        os.makedirs(dir_out, exist_ok=True); self.P = lambda n: os.path.join(dir_out, n)
        self.lim = Limitador(reloj, cfg.req_por_s); self.kill = None; self.kill_status = None; self.kill_sev = -1; self.exc = []; self.cnt = collections.Counter(); self.seguidos_429 = 0; self.seguidos_rech = 0; self.saldo_ileg = 0
        self.t_inicio_ns = reloj.now_ns(); self.logf = None; self.vivas = {}                      # vivas: clave -> dict(oid, tok, deadline_ns, slot, modo, hold_s)
        self.slots = C.plan_slots(cfg, n=cfg.max_ordenes + 100); self.fase = 'A'; self.sin_mercado = 0
        self.pres = None; self.led = None; self.ordenes = {}; self.senal = None; self.post_no_antes_ns = 0; self.ilegibles = []; self.abiertas_res = False; self.fills_b = 0; self.gasto_b = 0.0; self.t_ini_iso = dt.datetime.now(dt.timezone.utc).isoformat()
        self.ultimo_rechazo = None; self.alertas = []; self.n_senales = 0; self.lote_n0 = 0; self.ilegible_n0 = 0; self.io_fallos = 0
        self._locks = locks; self.n_filas0 = 0; self.corr_pend = 0; self.corr_total = 0; self.corr_json = {}; self.n_pend0 = 0; self.resume = False; self.operado = False; self.kills = {}; self.kills_resueltos = []; self.t_lim_ns = None; self.fase_b_fin = None; self.fase_b_parar = None; self.anclas_ult = (None, {}); self.anclas_ev = None; self.evid_ilegibles = []

    # ---------------------------------------------------------------- utilidades
    def log(self, msg, err=False):
        ts = dt.datetime.fromtimestamp(self.r.now_ns() / 1e9, dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'; linea = f'{ts} {"ERR " if err else ""}{msg}'
        try:
            if self.logf is None: self.logf = open(self.P('run.log'), 'a')                 # v7 (hallazgo 3): run.log se abre al primer mensaje (una instancia rechazada por el lock no toca nada)
            self.logf.write(linea + '\n'); self.logf.flush()
        except (OSError, ValueError):                                                 # v4 (hallazgo 10): un log que no se puede escribir NUNCA detiene el barrido
            try: print('LOG NO ESCRIBIBLE: ' + linea, file=sys.stderr, flush=True)
            except Exception: pass
        if self.stdout:
            try: print(linea, file=sys.stderr if err else sys.stdout, flush=True)
            except Exception: pass

    def _req(self, n=1):
        for _ in range(n): self.lim.esperar()

    @staticmethod
    def _severidad(motivo, status):
        """FAILED 3 > BLOCKED 2 > PARTIAL con motivo duro 1 > kill benigno (limites de tiempo/cantidad, senales, fin de fase B) 0."""
        if status == 'FAILED': return 3
        if status == 'BLOCKED': return 2
        return 0 if (motivo in BENIGNOS or str(motivo).startswith(BENIGNOS_PREFIJO)) else 1

    def _matar(self, motivo, status):
        """v6 (hallazgo 1): SIEMPRE queda una fila `kill` en el ledger (el resume decide por ellas: un kill benigno previo no puede ocultar uno grave posterior) y `self.kill/kill_status` conservan el MAS SEVERO (a igual severidad, el primero)."""
        sev = self._severidad(motivo, status); prev = self.kills.get(motivo)
        if prev is None or sev > self._severidad(motivo, prev): self.kills[motivo] = status                                  # v7 (hallazgo 2): kills vivos EN MEMORIA (los resueltos por verificacion salen de aqui)
        if self.led is not None and not any(r.get('k') == 'kill' and r.get('motivo') == motivo and r.get('status') == status for r in self.led.filas):
            self.led.add('kill', 'run', sum(1 for r in self.led.filas if r.get('k') == 'kill'), t_ns=self.r.now_ns(), motivo=motivo, status=status)
        if self.kill is None or sev > self.kill_sev:
            self.kill, self.kill_status, self.kill_sev = motivo, status, sev
            self.log(f'KILL {motivo} -> {status}', err=True)

    def _recalcular_kill(self):
        if self.kills: self.kill, self.kill_status = max(self.kills.items(), key=lambda kv: self._severidad(kv[0], kv[1])); self.kill_sev = self._severidad(self.kill, self.kill_status)
        else: self.kill = self.kill_status = None; self.kill_sev = -1

    @staticmethod
    def _kills_de_orden(clave): return tuple(motivo_kill_orden(t, clave) for t in KILL_ORDEN)

    def _resolver_kills_orden(self, clave, razon='inexistente_verificada'):
        """v7 (hallazgo 2b) y v8 (hallazgo 4): SOLO cuando `reconciliar_orden` PRUEBA que la orden no existio (inexistente_verificada: exchange sin ella + abiertas sin ella + saldo cuadrado contra el ledger tras el asentamiento) o la lee en estado TERMINAL LEGIBLE (reconciliada:<estado>; un relleno lo registra `_fill_detectado` aparte) el kill duro por esa orden (cancelacion no confirmada / estado ilegible / indeterminada)
        deja de serlo: fila `kill_resuelto` en el ledger (la fila `kill` original NO se borra: append-only) y el kill vivo en memoria se recalcula. Una orden NO verificada sigue BLOQUEANDO (fail-closed)."""
        for m in self._kills_de_orden(clave):
            if any(r.get('k') == 'kill' and r.get('motivo') == m for r in self.led.filas) and not any(r.get('k') == 'kill_resuelto' and r.get('motivo') == m for r in self.led.filas):
                self.led.add('kill_resuelto', 'run', sum(1 for r in self.led.filas if r.get('k') == 'kill_resuelto'), t_ns=self.r.now_ns(), motivo=m, razon=razon)
            if m in self.kills: del self.kills[m]; self.kills_resueltos.append(m); self.log(f'KILL RESUELTO {m}: {razon}')
        self._recalcular_kill()

    def _saldo_cae_mas_que_ledger(self, sal, gasto_ledger=None):
        """v7 (hallazgo 7): UNICO criterio de 'el saldo cayo mas de lo que explica el ledger' (tras lote, barrido final y verificacion de inexistente): s0 - saldo > gasto de rellenos del ledger + tol (< 1 share)."""
        if gasto_ledger is None: gasto_ledger = C.replay_estado(self.led.filas)[1]['gasto_fills_usd']
        return round(self.pres.s0 - sal, 6) > round(gasto_ledger + self.cfg.tol_saldo_usd, 6)

    # ---------------------------------------------------------------- senales (hallazgos 1-3 y 2a ronda)
    def _instalar_senales(self):
        """SIGTERM/SIGINT/SIGHUP: el manejador SOLO escribe en atributos (bandera + contador): sin E/S, sin locks, sin Event, sin excepciones (por tanto ninguna senal puede lanzar KeyboardInterrupt ni cortar `cancelar_viva`).
        Se restauran los manejadores originales SOLO al final de `correr`, despues del barrido y del informe final; las senales sucesivas solo incrementan el contador."""
        prev = {}
        if threading.current_thread() is not threading.main_thread(): return prev
        for sg in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
            try: prev[sg] = signal.signal(sg, self._on_senal)
            except (ValueError, OSError): pass
        return prev

    def _restaurar_senales(self, prev):
        for sg, h in prev.items():
            try: signal.signal(sg, h)
            except (ValueError, OSError, TypeError): pass

    def _on_senal(self, signum, frame):
        if self.senal is None: self.senal = signal.Signals(signum).name
        self.n_senales += 1

    def _hay_senal(self): return self.senal is not None

    def _dormir(self, s):
        """Sueno del CUERPO: en rodajas cortas que miran la bandera y despiertan con una senal. El barrido, las cancelaciones y las esperas de asentamiento usan `self.r.sleep(s)` a secas (duermen de verdad)."""
        self.r.sleep(s, abortar=self._hay_senal)

    def _chequear_senal(self):
        """Punto de control del cuerpo: si llego una senal se mata el run (PARTIAL, senal_X). True si hay senal."""
        if self.senal is None: return False
        if self.kill is None: self._matar(f'senal_{self.senal}', 'PARTIAL')
        return True

    # ---------------------------------------------------------------- manifiesto / checkpoint
    def _escribir(self, nombre, obj):
        """Escritura atomica que NO propaga OSError (hallazgo 10): cuenta el fallo y sigue; el barrido y el informe final no dependen de que el disco responda."""
        try: C.escribir_atomico(self.P(nombre), obj); return True
        except BaseException as e:
            self.io_fallos += 1; self.log(f'NO SE PUDO ESCRIBIR {nombre}: {type(e).__name__}: {str(e)[:80]}', err=True); return False

    def _manifest(self, estado, extra=None):
        m = dict(job=f'paquete_l:{self.run_id}', version=C.VERSION, run_id=self.run_id, codigo_sha=C.sha_codigo(), config=C.dataclasses.asdict(self.cfg), config_sha=self.cfg.sha(), parametros=self.params, real=self.real,
                 wallet=self.cfg.wallet, saldo_inicial=(self.pres.s0 if self.pres else None), suelo=(self.pres.suelo if self.pres else None), inicio_utc=self.t_ini_iso, estado=estado, fechas_previstas=[self.t_ini_iso[:10]], plan_sha=C.hashlib.sha256(json.dumps([C.dataclasses.asdict(x) for x in self.slots[:self.cfg.plan_ordenes]], sort_keys=True).encode()).hexdigest()[:16],
                 entradas_hash={'plan_slots': True, 'vendor': C.verificar_vendor()[0]}, reloj=dict(local='time.time_ns alineado a monotonic', chrony=getattr(self, 'chrony', None)), ultima_actualizacion_utc=dt.datetime.now(dt.timezone.utc).isoformat())
        if extra: m.update(extra)
        self._escribir('run_manifest.json', m)

    def _checkpoint(self, extra=None):
        O, res = C.replay_estado(self.led.filas); sl = max([o.slot for o in O.values()] + [-1])
        ck = dict(run_id=self.run_id, config_sha=self.cfg.sha(), slot_ultimo_intentado=sl, ledger_filas=len(self.led.filas), ledger_eids_sha=C.hashlib.sha256('|'.join(sorted(self.led.eids)).encode()).hexdigest()[:16],
                  kill=self.kill, fase=self.fase, **res)
        if extra: ck.update(extra)
        self._escribir('checkpoint.json', ck); return ck

    def _validar_checkpoint(self):
        """Ledger = verdad. Checkpoint ilegible -> se reconstruye; checkpoint con MAS filas que el ledger -> ledger truncado/perdido -> BLOQUEA (no se reenvia nada)."""
        p = self.P('checkpoint.json')
        if not os.path.exists(p): return 'sin_checkpoint'
        try: ck = json.load(open(p))
        except ValueError: self.log('checkpoint corrupto: se reconstruye desde el ledger', err=True); self.cnt['checkpoint_corrupto'] += 1; return 'corrupto_reconstruido'
        if ck.get('config_sha') != self.cfg.sha(): self._matar('config_distinta_al_checkpoint', 'FAILED'); return 'config_distinta'
        if ck.get('ledger_filas', 0) > len(self.led.filas): self._matar(f'ledger_truncado: checkpoint {ck["ledger_filas"]} filas > ledger {len(self.led.filas)}', 'FAILED'); return 'ledger_menor_que_checkpoint'
        return 'ok' if ck.get('ledger_filas') == len(self.led.filas) else 'ledger_por_delante_ok'

    # ---------------------------------------------------------------- reconciliacion (arranque / POST ambiguo)
    def _estado(self, oid, prioritario=False):
        """`prioritario` (lecturas de la maquina de cancelacion, v7 hallazgo 2a): se CUENTAN en el limitador pero nunca esperan su cupo (las cancelaciones tienen prioridad; son los POST/lecturas de preparacion los que ceden)."""
        if prioritario: self.lim.registrar()
        else: self._req()
        return self._leer_estado(oid)

    def _leer_estado(self, oid):
        try: return self.s.estado(oid)
        except Exception as e:
            if getattr(e, 'status_code', None) == 404: return None, 'NO_EXISTE'
            return None, None

    def _estado_poll(self, oid):
        """v10 (hallazgo 5): lectura del seguimiento 1 Hz de fase B. Comprueba el cupo JUSTO antes de leer; sin cupo devuelve (None, None, espera_s) y NO lee, NO espera y NO consume cupo (jamas duerme el bucle de cancelacion); con cupo se cuenta en el limitador y lee."""
        esp = self.lim.espera_s()
        if esp > 0: return None, None, esp
        self.lim.registrar(); m, est = self._leer_estado(oid); return m, est, 0.0

    def _confirmar_cancelada(self, oid, intentos):
        """v5 (hallazgo 1): hasta `intentos` veces: DELETE + lectura de estado, con backoff y el reloj del barrido (no interrumpible). Devuelve (matched, estado, cancelada) en cuanto el estado sea terminal y LEGIBLE."""
        back = (0.5, 1.0, 1.0, 2.0, 2.0); canc = False; m = est = None
        for i in range(max(1, intentos)):
            try: self._req(); canc = bool(self.s.cancelar(oid)) or canc
            except Exception as e: self.log(f'  cancelar fallo {type(e).__name__}: {str(e)[:80]}', err=True)
            m, est = self._estado(oid)
            if m is not None and C.es_terminal(est): return m, est, canc
            if i < intentos - 1: self.r.sleep(back[min(i, len(back) - 1)])
        return m, est, canc

    def _cierre(self, o, **kw):
        """Fila `cerrada` con indice unico: una orden puede cerrarse varias veces (INDETERMINADA y luego resuelta en un barrido/resume); la ULTIMA fila manda en replay_estado."""
        n = sum(1 for r in self.led.filas if r.get('k') == 'cerrada' and r.get('clave') == o.clave)
        self.led.add('cerrada', o.clave, n, t_ns=self.r.now_ns(), **kw)

    def reconciliar_orden(self, o, motivo):
        """Orden de la que no se sabe si esta viva (arranque tras caida, POST ambiguo, barrido final) o que quedo INDETERMINADA. Reintenta cancelar (con backoff) hasta leer un estado terminal LEGIBLE; el asentamiento (index_gracia + 3 s tras el POST) se
        espera SOLO si el primer intento no dio estado terminal, es decir, solo antes de poder declarar 'inexistente_verificada' o comparar saldo (hallazgo 10 v5). Si no se puede probar nada -> INDETERMINADA (bloquea). NUNCA reenvia."""
        oid = o.oid; self.log(f'reconciliar {o.clave} oid={oid} ({motivo})'); ref = self._ref_post_ns(o); terminal = lambda m_, e_: m_ is not None and C.es_terminal(e_)
        m, est, _ = self._confirmar_cancelada(oid, 1)
        if not terminal(m, est):
            self._asentar(ref, interrumpible=False)
            m, est, _ = self._confirmar_cancelada(oid, self.cfg.cancel_intentos_barrido)
        if terminal(m, est):
            mm = float(m); self.led.add('estado', o.clave, 1 + sum(1 for r in self.led.filas if r.get('k') == 'estado' and r.get('fuente') == 'reconciliacion' and r.get('clave') == o.clave), matched=mm, status=est, t_ns=self.r.now_ns(), fuente='reconciliacion')
            if mm > 1e-9 and o.matched < mm - 1e-9: self.cnt['fills'] += 1; o.matched = mm; self._fill_detectado(o, mm)
            o.indeterminada = False; self._cierre(o, motivo=f'reconciliada:{est}', size_matched=mm)
            if motivo == 'arranque' and o.matched >= mm - 1e-9: self._resolver_kills_orden(o.clave, f'reconciliada:{est}')                  # v8 (hallazgo 4): SOLO al reanudar, con la orden en estado terminal LEGIBLE y su relleno YA REGISTRADO en el ledger (v10 hallazgo 1: conocido, o detectado/registrado justo arriba por `_fill_detectado`; el relleno en si sigue bloqueando por n_fills>0 / ledger_con_rellenos, no por el kill de la orden) (el run anterior ya acabo BLOCKED por esa orden; leerla ahora en estado terminal LEGIBLE prueba que esta cerrada). En el barrido del MISMO run el incidente de cancelacion se mantiene (T10)
            return True
        ab = None
        try: self._req(); ab = self.s.abiertas_todas()
        except Exception: ab = None
        sal = self._saldo()
        pasado = ref is not None and self.r.now_ns() - ref >= self._asentamiento_ns()                      # 'inexistente_verificada' EXIGE que haya pasado el asentamiento desde el POST (sin referencia temporal => INDETERMINADA)
        if pasado and isinstance(ab, (list, tuple, set)) and str(oid).lower() not in {str(x).lower() for x in ab} and est == 'NO_EXISTE' and sal is not None and self.pres is not None and not self._saldo_cae_mas_que_ledger(sal):
            o.indeterminada = False; self._cierre(o, motivo='inexistente_verificada', size_matched=0.0); self._resolver_kills_orden(o.clave); return True
        o.indeterminada = True; self._cierre(o, motivo='INDETERMINADA', size_matched=(float(m) if m is not None else None), indeterminada=True); self.cnt['indeterminadas'] += 1
        self._matar(motivo_kill_orden('orden_indeterminada', o.clave), 'BLOCKED'); return False

    # ---------------------------------------------------------------- asentamiento tras el POST (hallazgo 5)
    def _asentamiento_ns(self): return int((self.cfg.index_gracia_s + self.cfg.asentamiento_extra_s) * 1e9)

    def _ref_post_ns(self, o):
        """Instante (reloj del run) desde el que se cuenta el asentamiento de una orden: el ack de su POST (o el envio); sin POST registrado, su intencion + 5 s (el POST pudo salir despues). None si no hay ninguna marca."""
        if o.t_ack_ns: return o.t_ack_ns
        if o.t_envio_ns: return o.t_envio_ns
        if o.t_intencion_ns: return o.t_intencion_ns + int(5e9)
        return None

    def _ult_post_ns(self):
        ts = [self._ref_post_ns(o) for o in self.ordenes.values() if o.clase_post != 'rechazo']
        ts = [t for t in ts if t]
        return max(ts) if ts else None

    def _asentar(self, ref_ns, interrumpible):
        """Espera hasta ref + index_gracia_s + 3 s. interrumpible=True (cuerpo): una senal corta la espera y devuelve False (el barrido repetira la comprobacion); False => NO se puede comparar saldo/estado todavia."""
        if not ref_ns: return True
        rest = ref_ns + self._asentamiento_ns() - self.r.now_ns()
        if rest <= 0: return True
        if interrumpible: self._dormir(rest / 1e9); return self.r.now_ns() >= ref_ns + self._asentamiento_ns()
        self.r.sleep(rest / 1e9); return True

    def _fill_detectado(self, o, mm):
        coste = round(mm * o.precio, 6); self.log(f'FILL {o.clave} matched={mm} coste={coste} modo={o.modo}', err=True)
        self.led.add('fill', o.clave, 0, size_matched=mm, coste=coste, modo=o.modo, t_ns=self.r.now_ns())
        if o.modo == 'top':
            self.fills_b += 1; self.gasto_b = round(self.gasto_b + coste, 6)
            if self.fills_b >= self.cfg.fase_b_max_rellenos or self.gasto_b >= self.cfg.fase_b_tope_usd - 1e-9: self._matar('fase_b_tope_rellenos', 'PARTIAL')
        else: self._matar('relleno_en_fase_A (corte inmediato)', 'PARTIAL')

    # ---------------------------------------------------------------- POST de un slot
    def _libro_ok(self, slot, tok):
        try: bids, asks = self.libro(tok)
        except Exception as e: return None, f'libro_ilegible:{type(e).__name__}'
        if not asks: return None, 'sin_asks'
        mb = max((float(p) for p, _ in bids), default=None); ma = min(float(p) for p, _ in asks); q_bid = sum(float(s) for p, s in bids if mb is not None and abs(float(p) - mb) < 1e-9) if mb else 0.0
        if ma < self.cfg.ask_min - 1e-9: return None, 'ask_cruzaria'
        if slot.modo == 'lejos':
            if mb is None or mb < self.cfg.bid_min_lejos - 1e-9: return None, 'bid_bajo_para_lejos'
        else:
            if mb is None or abs(mb - self.cfg.precio) > 1e-9 or q_bid < 1.0: return None, 'sin_cola_en_0.01_para_top'
            if ma > self.cfg.top_ask_max + 1e-9: return None, 'top_no_casi_resuelto'                       # la posicion residual de un relleno debe valer ~0 (ask <= 0,05)
        return dict(mejor_bid=mb, mejor_ask=ma, q_bid=q_bid), None

    def _vida_req(self, slot):
        """v7 (hallazgos 1 y 6): vida restante minima del mercado para ENVIAR este slot = base + hold + 2 s. Fase A: min_vida_mercado_s (90: el precio no puede colapsar a 0,01 por cierre inminente). Fase B (modo 'top'): fase_b_min_vida_s (15), porque
        BUSCA tokens casi resueltos (recta final del 5m); solo exige poder cancelar y leer el estado antes del cierre. Se aplica al elegir (+ prep_presupuesto_s) y OTRA VEZ justo antes del POST (sin prep)."""
        return (self.cfg.fase_b_min_vida_s if slot.modo == 'top' else self.cfg.min_vida_mercado_s) + slot.hold_s + 2.0

    def _elegir_mercado(self, slot):
        t = self.r.now_ns() / 1e9; minv = self._vida_req(slot) + self.cfg.prep_presupuesto_s; cand = []
        for (slug, coin, fin, toks, neg) in self.m.mercados(slot.coin):                # hallazgo 9: SOLO la moneda del slot (1 consulta de mercado, no 8)
            if coin != slot.coin or len(toks) != 2: continue
            if fin - t >= minv: cand.append((fin, slug, toks, neg))
        cand.sort()
        for fin, slug, toks, neg in cand:                       # el que acaba antes pero con vida suficiente (diversifica mercados)
            for lado in (slot.lado, 1 - slot.lado):
                info, why = self._libro_ok(slot, toks[lado])
                if info: return slug, fin, toks[lado], neg, info
        return None

    def preparar_lote(self, slots):
        """FASE 1 del lote, SIN ordenes vivas: elige mercado/token de cada slot, espera el gate del canal de usuario (preparar), comprueba tick. Asi el gate (hasta 6 s por mercado nuevo) NUNCA retrasa la cancelacion de otra orden viva.
        Devuelve [(slot, sel)] de los slots listos; los fallidos quedan en el ledger como `saltado` (con motivo). Sin mercado valido: espera y reintenta (sin quemar slots) y, pasado max_espera_mercado_s, BLOCKED."""
        listos = []; cfg = self.cfg
        C.exigir(not self.vivas, 'preparar_lote con ordenes vivas (retrasaria sus cancelaciones)')
        for slot in slots:
            clave = f'{self.run_id}|s{slot.i}'
            if self.kill or self._chequear_senal(): break
            if clave in self.ordenes: self.cnt['slot_ya_en_ledger'] += 1; continue
            while True:
                if self._chequear_senal(): sel = None; break
                sel = self._elegir_mercado(slot)
                if sel is not None: self.sin_mercado = 0; break
                self.cnt['reintentos_sin_mercado'] += 1; self.sin_mercado += 1
                if self.fase == 'B':                              # v7 (hallazgo 6): en fase B no encontrar un token barato NO es un fallo del run: termina la fase B (benigna), sin kill y sin tocar el status de la fase A
                    if self.sin_mercado * cfg.espera_mercado_s >= cfg.fase_b_espera_s: self.fase_b_parar = 'sin_token_barato'; break
                    if self.t_lim_ns is not None and self.r.now_ns() > self.t_lim_ns: self.fase_b_parar = 'max_minutos'; break
                elif self.sin_mercado * cfg.espera_mercado_s >= cfg.max_espera_mercado_s: self._matar('sin_mercado_valido_prolongado', 'BLOCKED'); break
                self._dormir(cfg.espera_mercado_s)
            if sel is None: break
            slug, fin, tok, neg, info = sel
            try:
                if hasattr(self.s, 'preparar') and not self.s.preparar(tok): self.cnt['saltados_canal_no_listo'] += 1; self.led.add('saltado', clave, 0, slot=slot.i, coin=slot.coin, motivo='canal_usuario_no_listo', t_ns=self.r.now_ns()); continue
                if str(self.s.tick(tok)) != '0.01': self.cnt['saltados_tick'] += 1; self.led.add('saltado', clave, 0, slot=slot.i, coin=slot.coin, motivo='tick_distinto', t_ns=self.r.now_ns()); continue
            except Exception as e:
                self.cnt['saltados_firma'] += 1; self.led.add('saltado', clave, 0, slot=slot.i, coin=slot.coin, motivo=f'prepare:{type(e).__name__}:{str(e)[:80]}', t_ns=self.r.now_ns()); continue
            listos.append((slot, sel))
        return listos

    def _vida_ok(self, slot, fin): return fin - self.r.now_ns() / 1e9 >= self._vida_req(slot)

    def _saltar_vida(self, slot, clave, fin):
        rest = fin - self.r.now_ns() / 1e9; self.cnt['saltados_mercado_caducado'] += 1
        self.led.add('saltado', clave, 0, slot=slot.i, coin=slot.coin, motivo=f'vida_minima_al_post:{rest:.0f}s<{self._vida_req(slot):.0f}s', t_ns=self.r.now_ns()); return 'saltado'

    def post_slot(self, slot, sel):
        o_prev = self.ordenes.get(f'{self.run_id}|s{slot.i}')
        if o_prev is not None: self.cnt['slot_ya_en_ledger'] += 1; return None
        if self.kill: return None
        if self.r.now_ns() < self.post_no_antes_ns: return 'diferido'                    # backoff 429: SOLO se difiere el siguiente POST; el bucle sigue cancelando (hallazgo 7)
        if not self.pres.puede_enviar(len(self.vivas)): self.cnt['espera_presupuesto'] += 1; return 'espera'
        if self.lim.espera_s() > 0: self.cnt['post_diferido_por_limitador'] += 1; return 'diferido'                      # v7 (hallazgo 2a): un POST NUNCA espera el cupo dentro del bucle (bloquearia las cancelaciones vencidas): se difiere y el bucle sigue cancelando
        slug, fin, tok, neg, info = sel; clave = f'{self.run_id}|s{slot.i}'; cfg = self.cfg
        if not self._vida_ok(slot, fin): return self._saltar_vida(slot, clave, fin)                          # v7 (hallazgo 1): la vida minima se revalida AQUI (antes de firmar) y otra vez justo antes del POST: una preparacion/espera larga NO deja salir un slot con poca vida
        try: t_dec = self.r.now_ns(); oid_local, handle = self.s.colocar(tok, cfg.precio, cfg.size, clave, neg_risk=neg, expira_s=cfg.gtd_expira_s)      # neg_risk de gamma (verificado) + expiracion dura GTD (hallazgos 10 y 3)
        except Exception as e:
            self.cnt['saltados_firma'] += 1; self.led.add('saltado', clave, 0, slot=slot.i, coin=slot.coin, motivo=f'prepost:{type(e).__name__}:{str(e)[:80]}', t_ns=self.r.now_ns()); return 'saltado'
        # hallazgo 2: el libro se REVALIDA justo antes del POST (el de la fase de preparacion tiene hasta ~40 s). Orden ya firmada pero sin ledger ni envio: descartarla no deja rastro.
        t_l0 = self.r.now_ns(); info2, why = self._libro_ok(slot, tok); dt_libro = (self.r.now_ns() - t_l0) / 1e9
        if info2 is None or dt_libro > cfg.libro_max_s:
            motivo = f'libro_revalidacion:{why}' if info2 is None else f'libro_rancio:{dt_libro:.2f}s'; self.cnt['saltados_libro_revalidacion'] += 1
            self.led.add('saltado', clave, 0, slot=slot.i, coin=slot.coin, motivo=motivo, t_ns=self.r.now_ns()); return 'saltado'
        if self.vivas and min(v['deadline_ns'] for v in self.vivas.values()) <= self.r.now_ns(): self.cnt['post_diferido_por_cancelacion_vencida'] += 1; return 'diferido'     # la lectura del libro se comio el hold de otra: primero cancelar
        if not self._vida_ok(slot, fin): return self._saltar_vida(slot, clave, fin)                          # tras firmar y leer el libro: la ultima comprobacion antes de dejar rastro (intencion)
        info = info2
        self.led.add('intencion', clave, 0, slot=slot.i, coin=slot.coin, slug=slug, tok=tok, modo=slot.modo, precio=cfg.precio, size=cfg.size, hold_s=slot.hold_s, oid_local=oid_local, t_decision_ns=t_dec, libro=info, fin_s=fin, neg_risk=neg, expira_s=(cfg.gtd_expira_s or None))
        o = C.Orden(clave=clave, slot=slot.i, coin=slot.coin, tok=tok, modo=slot.modo, precio=cfg.precio, size=cfg.size, oid=oid_local); o.t_intencion_ns = t_dec; self.ordenes[clave] = o; self.cnt['intenciones'] += 1
        self._req(); t_send = self.r.now_ns(); resp = None; clase = None; err = None
        try: resp = self.s.enviar(handle); t_ack = self.r.now_ns(); clase = C.clasificar_post(resp)
        except Exception as e:
            t_ack = self.r.now_ns(); err = f'{type(e).__name__}: {str(e)[:150]}'; clase = C.clasificar_excepcion_post(e)
            if C.es_429(e): clase = '429'
        oid_srv = C.id_servidor(resp, oid_local); oid = oid_srv or oid_local; o.oid = oid; o.t_envio_ns = t_send; o.t_ack_ns = t_ack; o.clase_post = clase
        self.led.add('post', clave, 0, oid=oid, oid_local=oid_local, t_send_ns=t_send, t_ack_ns=t_ack, clase=clase, error=err, resp=(str(resp)[:200] if resp is not None else None), ack_ms=(t_ack - t_send) / 1e6)
        self.cnt['posts'] += 1
        if oid_srv:                                                                       # hallazgo 7: el orderID del servidor NO es el hash local (se esperaba identico): las anclas (alta con oid local) no casarian con el canal de usuario => alarma y BLOCKED
            self.cnt['oid_servidor_distinto'] += 1; self.log(f'ALARMA oid del servidor {oid_srv} != oid local {oid_local} en {clave}: la orden se sigue con el oid del servidor; run BLOCKED', err=True)
            self._matar('oid_servidor_distinto_del_local', 'BLOCKED')
        if clase == '429':
            self.cnt['http429'] += 1; self.seguidos_429 += 1; self.led.add('cerrada', clave, 0, motivo='http429', size_matched=0.0, t_ns=self.r.now_ns()); o.cerrada = True
            back = cfg.backoff_429_s[min(self.seguidos_429 - 1, len(cfg.backoff_429_s) - 1)]; self.log(f'429 en POST ({self.seguidos_429} seguidos): el siguiente POST no antes de {back}s (el bucle sigue cancelando)', err=True)
            if self.seguidos_429 >= cfg.kill_429_seguidos: self._matar('rate_limit_429_seguidos', 'BLOCKED')
            else: self.post_no_antes_ns = self.r.now_ns() + int(back * 1e9)
            return 'rechazo'
        self.seguidos_429 = 0
        if clase == 'rechazo':
            self.cnt['rechazos'] += 1; self.seguidos_rech += 1; self.ultimo_rechazo = (str(resp) if resp is not None else str(err))[:240]; self.led.add('cerrada', clave, 0, motivo='rechazo', size_matched=0.0, t_ns=self.r.now_ns(), rechazo_literal=self.ultimo_rechazo); o.cerrada = True
            if self.seguidos_rech >= cfg.kill_rechazos_seguidos: self._matar(f'rechazos_seguidos; ultimo rechazo literal del CLOB: {self.ultimo_rechazo}', 'BLOCKED')           # v5 (hallazgo 2): sin caida de modo: BLOCKED (sin gasto: una orden rechazada no esta en el libro) con el literal
            return 'rechazo'
        self.seguidos_rech = 0
        if (t_ack - t_send) / 1e6 > cfg.ack_max_ms: self._matar(f'ack_lento_{(t_ack - t_send) / 1e6:.0f}ms', 'BLOCKED')
        if clase == 'ambiguo':
            self.cnt['ambiguos'] += 1; self.vivas[clave] = dict(oid=oid, tok=tok, deadline_ns=self.r.now_ns(), slot=slot.i, modo=slot.modo, hold_s=0.0, t_ack_ns=t_ack, trig='ambiguo'); return 'ambiguo'
        hold_ns = int(slot.hold_s * 1e9); self.vivas[clave] = dict(oid=oid, tok=tok, deadline_ns=t_ack + hold_ns, slot=slot.i, modo=slot.modo, hold_s=slot.hold_s, t_ack_ns=t_ack, trig='hold', next_poll_ns=(t_ack + int(1e9)) if slot.modo == 'top' else None)
        st = C.post_status(resp)
        if st in C.STATUS_POST_ANOMALO:                                                  # hallazgo 4: una post-only a 0,01 que vuelve 'matched'/'delayed' = relleno (o casado en curso): CORTE INMEDIATO, sin esperar al hold
            self.cnt['post_status_anomalo'] += 1; self.led.add('anomalia_post', clave, 0, status=st, resp=str(resp)[:200], t_ns=self.r.now_ns())
            self.vivas[clave]['deadline_ns'] = self.r.now_ns(); self.vivas[clave]['trig'] = f'post_status_{st}'; self._matar(f'relleno_o_casado_en_post:{st}', 'PARTIAL')
        return 'ok'

    # ---------------------------------------------------------------- cancelacion con medicion d_proc
    def _reprogramar(self, v, s): v['deadline_ns'] = self.r.now_ns() + int(s * 1e9); return None

    def _due(self, v):
        """Hora a la que una viva exige atencion: su deadline, o AHORA si hay kill y aun no se ha empezado a cancelarla (una que esta esperando un reintento conserva su hora)."""
        return self.r.now_ns() if (self.kill and v.get('cx') is None) else v['deadline_ns']

    def cancelar_viva(self, clave, forzada=False):
        """v7 (hallazgo 2a): UN PASO de la maquina de cancelacion (DELETE + lectura de estado, o una lectura de confirmacion). Las esperas (gracia de indexacion de get_order, backoffs, relecturas del estado) NO bloquean: se programan en `v['deadline_ns']` y la funcion devuelve None; el bucle del lote
        atiende primero cualquier deadline vencido de las DEMAS vivas (una orden ambigua cuyo POST nunca llego ya no retrasa las cancelaciones ajenas mas que un paso). Devuelve True/False al TERMINAR (cancelada o terminal / INDETERMINADA). `_cancelar_completa` la repite hasta el final (barrido)."""
        v = self.vivas[clave]; o = self.ordenes[clave]; oid = v['oid']; ahora = self.r.now_ns(); backoffs = (0.25, 0.5, 1.0); gracia_ns = int(self.cfg.index_gracia_s * 1e9)
        cx = v.get('cx')
        if cx is None: cx = v['cx'] = dict(fase='cancelar', n=0, fallos=0, ok=False, t_prog=v['deadline_ns'], t_trig=ahora, t_ack0=v.get('t_ack_ns') or ahora, leidas=0, m=None, est=None)       # t_trig_rx_ns: el evento (vencimiento de hold / kill) YA recibido por el hilo; compartido por los reintentos
        if cx['fase'] == 'cancelar':
            cx['n'] += 1; n = cx['n']; self.lim.registrar(); t_send = self.r.now_ns(); err = None; r_ok = False
            try: r_ok = bool(self.s.cancelar(oid))
            except Exception as e: err = f'{type(e).__name__}: {str(e)[:150]}'; self.cnt['cancel_excepciones'] += 1; self.cnt['cancel_429'] += 1 if C.es_429(e) else 0
            t_ack = self.r.now_ns()
            self.led.add('cancel', clave, n, oid=oid, ok=r_ok, intento=n, t_trig_prog_ns=cx['t_prog'], t_trig_rx_ns=cx['t_trig'], t_send_ns=t_send, t_ack_ns=t_ack, error=err, forzada=bool(forzada), trig=v['trig'])
            if r_ok: cx['ok'] = True; cx['fase'] = 'leer'
            else:
                m, est = self._estado(oid, prioritario=True)                     # ya casada/cancelada (= terminal) o seguimos
                if C.es_terminal(est): self.led.add('estado', clave, 10 + n, matched=float(m or 0.0), status=est, t_ns=self.r.now_ns(), fuente='post_cancel_fallido'); cx['fase'] = 'leer'
                elif est == 'NO_EXISTE' and self.r.now_ns() - cx['t_ack0'] < gracia_ns: self.cnt['cancel_pre_indice'] += 1; return self._reprogramar(v, 0.25)      # get_order devuelve null hasta ~1,4 s tras el POST: aun sin indexar, NO es un fallo de cancelacion
                else:
                    cx['fallos'] += 1
                    if cx['fallos'] > len(backoffs): cx['fase'] = 'leer'
                    else: return self._reprogramar(v, backoffs[cx['fallos'] - 1])
            if cx['fase'] == 'leer': v['deadline_ns'] = self.r.now_ns(); return None          # la lectura de confirmacion es el SIGUIENTE paso (las demas vivas vencidas pasan antes)
        cx['leidas'] += 1; m, est = self._estado(oid, prioritario=True); cx['m'], cx['est'] = m, est         # hallazgo 4 (v4): tras cancelar el estado tiene que ser LEGIBLE y terminal (size_matched conocido); hasta 4 lecturas espaciadas 0,25 s (indexacion/red) antes de rendirse
        legible = m is not None and C.es_terminal(est)
        if not legible and cx['leidas'] < 4: return self._reprogramar(v, 0.25)
        ok = cx['ok']; self.led.add('estado', clave, 0, matched=(float(m) if m is not None else None), status=est, t_ns=self.r.now_ns(), fuente='post_cancel', legible=legible)
        if not legible:                                                       # cancel_ok pero estado ilegible NO es 'matched=0': pudo casarse antes del DELETE => INDETERMINADO, corte (BLOCKED); el saldo on-chain lo cruza en el barrido final
            motivo = 'CANCEL_NO_CONFIRMADA' if not ok else 'ESTADO_ILEGIBLE_TRAS_CANCEL'
            self.led.add('cerrada', clave, 0, motivo=motivo, size_matched=(float(m) if m is not None else None), indeterminada=True, t_ns=self.r.now_ns()); o.cerrada = True; o.indeterminada = True
            self.cnt['cancel_no_confirmada' if not ok else 'estado_ilegible_tras_cancel'] += 1; self._matar(motivo_kill_orden('cancel_no_confirmada' if not ok else 'estado_ilegible_tras_cancel', clave), 'BLOCKED'); del self.vivas[clave]; return False
        mm = max(float(m), o.matched); o.matched = mm; o.cerrada = True
        del self.vivas[clave]
        if mm > 1e-9: self.cnt['fills'] += 1; self._fill_detectado(o, mm)                    # orden de escritura (hallazgo 5): fill + kill DURABLES antes de la fila `cerrada`: un SIGKILL entre medias no deja un hueco
        self.led.add('cerrada', clave, 0, motivo=('cancelada' if ok else f'terminal:{est}'), size_matched=mm, t_ns=self.r.now_ns())
        self.cnt['canceladas_ok'] += 1 if ok else 0
        return True

    def _cancelar_completa(self, clave):
        """Barrido final: repite `cancelar_viva` (duerme DE VERDAD entre pasos, sin abortar con senales) hasta que la orden queda cerrada o INDETERMINADA."""
        while True:
            r = self.cancelar_viva(clave, forzada=True)
            if r is not None: return r
            esp = self.vivas[clave]['deadline_ns'] - self.r.now_ns()
            if esp > 0: self.r.sleep(esp / 1e9)

    # ---------------------------------------------------------------- relleno por PUSH (canal de usuario) ademas de estado/saldo
    def _chequear_push(self):
        """Lee del canal de usuario (local, sin red) los rellenos de nuestras vivas. Un relleno en fase A = corte inmediato (se cancelan TODAS ya, sin esperar al vencimiento del hold ni al saldo del fin de lote). Complementa, no sustituye,
        a get_order al cancelar y al saldo on-chain tras el lote (si el push se pierde, esos dos lo detectan)."""
        if not hasattr(self.s, 'fills_push') or not self.vivas: return
        try: f = self.s.fills_push() or {}
        except Exception: self.cnt['push_errores'] += 1; return
        for clave, v in list(self.vivas.items()):
            mm = float(f.get(str(v['oid']).lower(), 0.0) or 0.0)
            if mm <= 1e-9 or v.get('push_visto'): continue
            v['push_visto'] = True; o = self.ordenes[clave]; o.matched = max(o.matched, mm); self.cnt['push_fills'] += 1
            self.led.add('push_fill', clave, 0, matched=mm, t_ns=self.r.now_ns(), fuente='canal_usuario', modo=o.modo); self.led.add('estado', clave, 200, matched=mm, status='PUSH', t_ns=self.r.now_ns(), fuente='canal_usuario')
            self.log(f'PUSH relleno {clave} matched={mm}', err=True)
            if o.modo != 'top': self._matar('relleno_en_fase_A (push canal usuario)', 'PARTIAL')
            else: v['deadline_ns'] = min(v['deadline_ns'], self.r.now_ns())

    # ---------------------------------------------------------------- lote
    def lote(self, slots):
        listos = self.preparar_lote(slots)                                   # FASE 1 (sin vivas)
        pend = list(listos); next_post = self.r.now_ns(); t_push = 0
        if pend and not self._reloj_ok(): self.log(f'reloj no verificado: se descartan {len(pend)} slots (sin gasto)', err=True); pend = []
        while pend or self.vivas:
            self._chequear_senal()
            if self.kill and pend: self.log(f'kill activo: se descartan {len(pend)} slots pendientes del lote'); pend = []
            now = self.r.now_ns()
            if self.vivas and now >= t_push: self._chequear_push(); t_push = self.r.now_ns() + int(self.cfg.push_poll_s * 1e9); now = self.r.now_ns()
            t_dl = min((self._due(v) for v in self.vivas.values()), default=None)
            t_po = next_post if pend else None
            t_pl = min((v['next_poll_ns'] for v in self.vivas.values() if v.get('next_poll_ns') and v.get('cx') is None), default=None) if not self.kill else None
            t_ps = t_push if (self.vivas and not self.kill and hasattr(self.s, 'fills_push')) else None
            cands = [t for t in (t_dl, t_po, t_pl, t_ps) if t is not None]
            if not cands: break
            t_next = min(cands)
            if t_next > now: (self.r.sleep if self.kill else self._dormir)((t_next - now) / 1e9)               # el cuerpo del lote despierta con una senal; con kill (cancelaciones/reintentos pendientes) y en el barrido se duerme DE VERDAD (sin abortar: no hay bucle caliente)
            now = self.r.now_ns()
            if self.vivas and min(self._due(v) for v in self.vivas.values()) <= now:                 # las cancelaciones tienen PRIORIDAD sobre cualquier otra tarea del bucle; v7: UN paso por iteracion, siempre la mas vencida
                clave = min(self.vivas, key=lambda c: (self._due(self.vivas[c]), self.vivas[c]['deadline_ns'])); self.cancelar_viva(clave, forzada=bool(self.kill)); continue
            if self.vivas and now >= t_push: continue                       # toca leer el push antes que nada
            pol = [c for c, v in self.vivas.items() if v.get('next_poll_ns') and v['next_poll_ns'] <= now and v.get('cx') is None]
            if pol and not self.kill:                                       # fase B: seguimiento 1 Hz de size_matched (parciales) mientras la orden esta viva
                for c in pol:
                    v = self.vivas[c]; m, est, esp = self._estado_poll(v['oid'])                                  # v10 (hallazgo 5): cupo comprobado antes de CADA lectura; sin cupo se DIFIERE esa orden (nunca espera ni consume el cupo de las cancelaciones)
                    if esp > 0: v['next_poll_ns'] = self.r.now_ns() + int(esp * 1e9); continue
                    v['next_poll_ns'] = self.r.now_ns() + int(1e9)
                    self.led.add('estado', c, 100 + int(self.r.now_ns() // 1_000_000) % 10_000_000, matched=float(m or 0.0), status=est, t_ns=self.r.now_ns(), fuente='poll_top')
                    if m and float(m) > 1e-9: v['deadline_ns'] = min(v['deadline_ns'], self.r.now_ns())      # algo casado: se cierra la orden ya (se cancela el resto)
                continue
            if pend and next_post <= now:
                slot, sel = pend[0]; res = self.post_slot(slot, sel)
                if res == 'espera':
                    if not self.vivas: self._matar('presupuesto_no_permite_enviar', 'BLOCKED')
                    else: next_post = now + int(0.2e9)
                    continue
                if res == 'diferido': next_post = max(self.post_no_antes_ns, self.r.now_ns() + int(0.05e9)); continue                  # backoff 429 / cancelacion vencida: el slot sigue pendiente; el bucle cancela primero
                pend.pop(0); next_post = max(self.r.now_ns() + int(self.cfg.espaciado_post_s * 1e9), self.post_no_antes_ns)
            if self.kill and not pend and not self.vivas: break
        return True

    def _reloj_ok(self):
        """Fail-closed (hallazgos 4 v4 y 3 v5): la expiracion GTD es hora de pared del sistema (`now + gtd_expira_s`) y el exchange la compara con la suya. ANTES DE CADA LOTE se exige un chrony SINCRONIZADO (leap Normal, stratum 1-15, ref id != 0)
        con |System time| y Root dispersion acotados (`C.reloj_sincronizado`); si no => BLOCKED sin enviar."""
        try: ch = self.s.chrony() if hasattr(self.s, 'chrony') else None
        except Exception: ch = None
        self.chrony = ch; ok = C.reloj_sincronizado(ch, self.cfg)
        if not ok: self.cnt['reloj_no_verificado'] += 1; self._matar(f'reloj_no_verificado:{ch}', 'BLOCKED')
        return ok

    def _saldo(self):
        """Saldo on-chain con reintentos (RPC Polygon) y validacion; None solo si TODAS las lecturas fallan (el llamador lo trata como fail-closed)."""
        mx = self.cfg.saldo_autorizado + 0.05
        v = C.leer_saldo_robusto(self.s.saldo, self.cfg.saldo_reintentos, self.cfg.saldo_backoff_s, self.r.sleep, maximo=(mx if getattr(self, 'pres', None) is not None else None))
        if v is None: self.cnt['saldo_lecturas_agotadas'] += 1
        return v

    anclas_unico = None                                                      # v7 (hallazgo 10): real = sender.anclas(filas) -> (total, por_moneda, eventos, ilegibles); una sola lectura de los cancel_evid por lote

    def _leer_anclas(self):
        """(total|None, por_moneda) con UNA lectura por llamada; guarda en `anclas_ult` y los eventos leidos (real) en `anclas_ev` para el informe final."""
        if self.anclas_unico is not None: tot, por, ev, ileg = self.anclas_unico(self.led.filas); self.anclas_ev = (ev, ileg)
        else: tot = self.anclas_fn() if self.anclas_fn else None; por = self.anclas_por_moneda_fn() if self.anclas_por_moneda_fn else {}
        self.anclas_ult = (tot, por); return tot, por

    def _tras_lote(self, n_lote):
        ancl = self._leer_anclas()[0]                                       # hallazgo 5: PRIMERO la espera del canal de usuario (anclas); el saldo se lee DESPUES
        sal = None; lote_id = self.lote_n0 + self.cnt['lotes']
        if self._asentar(self._ult_post_ns(), interrumpible=True):           # y solo tras >= index_gracia_s + 3 s desde el ultimo POST (bloque on-chain / indexacion)
            sal = self._saldo()
            if sal is None:
                self.saldo_ileg += 1; self.log(f'saldo ilegible tras lote ({self.saldo_ileg})', err=True)
                if self.saldo_ileg >= 2: self._matar('saldo_ilegible_seguido', 'BLOCKED')
            else: self.saldo_ileg = 0; self.pres.actualizar(saldo=sal)
        else: self.log('saldo del lote NO comparado: senal durante el asentamiento (lo comprueba el barrido final)', err=True)
        O, res = C.replay_estado(self.led.filas); self.pres.actualizar(gasto_ledger=res['gasto_fills_usd'])
        if self.pres.toca_suelo(): self._matar(f'TOCA_SUELO gasto={self.pres.gasto} saldo={self.pres.saldo}', 'FAILED')
        # discrepancia saldo vs ledger: si el saldo cayo mas de lo que explica el ledger => relleno no visto: se corta
        if sal is not None and self._saldo_cae_mas_que_ledger(sal, res['gasto_fills_usd']): self._matar(f'saldo_cae_mas_que_ledger {self.pres.s0 - sal:.4f} > {res["gasto_fills_usd"]:.4f}', 'PARTIAL')       # tol < 1 share (hallazgo 4)
        resumen = dict(lote=lote_id, n_ordenes_lote=n_lote, ts_utc=dt.datetime.now(dt.timezone.utc).isoformat(), cnt=dict(self.cnt), saldo=sal, gasto=self.pres.gasto, suelo=self.pres.suelo, anclas_directas=ancl, kill=self.kill, **res)
        self._escribir('parcial_resumen.json', resumen)
        self.led.add('lote', f'{self.run_id}|l{lote_id}', 0, **{k: v for k, v in resumen.items() if k != 'cnt'})                # hallazgo 6: numeracion global (filas ya presentes + lotes de este proceso): un resume no choca con las filas previas
        self._checkpoint(); return ancl

    def anclas_ledger_por_moneda(self):
        """Cancelaciones CONFIRMADAS (ok) por moneda segun el ledger (cota superior de las anclas directas; en real las validas las cuenta el canal de usuario)."""
        coin = {r['clave']: r['coin'] for r in self.led.filas if r.get('k') == 'intencion'}; c = collections.Counter()
        for r in self.led.filas:
            if r.get('k') == 'cancel' and r.get('ok'): c[coin.get(r['clave'], '?')] += 1
        return dict(c)

    # ---------------------------------------------------------------- ejecucion
    def correr(self):
        """UNICO punto de entrada. v4 (hallazgo 1): los manejadores de senal se instalan ANTES de todo y se restauran SOLO al final (tras barrido e informe): una 2a senal durante el barrido solo incrementa un contador."""
        propios = self._locks is None
        if propios: self._locks = C.locks_de_run(self.cfg, self.dir, self.real)                  # v7 (hallazgo 3): ANTES de cualquier lectura de estado, apertura de ledger o envio
        if not self._locks:
            print(f'INSTANCIA UNICA: ya hay otro proceso con la wallet {self.cfg.wallet} o el --out {self.dir} (o no se pudo tomar el lock): no se toca nada (ni ledger, ni checkpoint, ni informe)', file=sys.stderr, flush=True)
            self._locks = None; return 'LOCKED'
        prev = self._instalar_senales()
        try: return self._correr()
        finally:
            self._restaurar_senales(prev)
            if propios: C.liberar_locks(self._locks); self._locks = None

    def _excepcion(self, donde, e):
        """Hallazgo 10: registrar una excepcion NUNCA puede impedir el barrido: cada paso va en su propio try (disco lleno, log roto...)."""
        try: import traceback; self.exc.append(f'[{donde}] ' + traceback.format_exc()[-1500:])
        except BaseException: pass
        try: self.log(f'EXCEPCION en {donde} {type(e).__name__}: {e}', err=True)
        except BaseException: pass
        try: self._matar(f'excepcion:{type(e).__name__}', 'FAILED')
        except BaseException:
            m = f'excepcion:{type(e).__name__}'; self.kills[m] = 'FAILED'; self.kill, self.kill_status, self.kill_sev = m, 'FAILED', 3                       # v8 (hallazgo 3): tambien en self.kills (un `_recalcular_kill` posterior no puede borrarlo)
            try:
                if not any(r.get('k') == 'kill' and r.get('motivo') == m and r.get('status') == 'FAILED' for r in self.led.filas):                      # v9 (hallazgo 6): si `_matar` ya la escribio antes de fallar, no se duplica
                    self.led.add('kill', 'run', sum(1 for r in self.led.filas if r.get('k') == 'kill'), t_ns=self.r.now_ns(), motivo=m, status='FAILED')
            except BaseException: pass

    def _correr(self):
        """v3 (hallazgo 3): cuerpo dentro de try/except BaseException; SIEMPRE, salga como salga, se ejecuta el barrido final (cancelar vivas + reconciliar toda orden sin cierre + verificar abiertas/saldo) y se escribe el informe final.
        v4 (hallazgo 10): ni el log, ni el ledger, ni el manifiesto pueden impedir el barrido ni el informe (fallback a stderr y a FALLBACK_DIR)."""
        self.led = C.Ledger(self.P('ledger.jsonl')); self.t_ini_iso = dt.datetime.now(dt.timezone.utc).isoformat(); self.fills_b = 0; self.gasto_b = 0.0
        self._persistir_corruptas()                                                        # v9 (hallazgo 3): el contador de corruptas se persiste FUERA del ledger (fichero lateral atomico) al abrir; la fila `ledger_reparado` solo se escribe si el run va a operar (`_cuerpo`)
        self.n_filas0 = len(self.led.filas)
        self.ordenes, _ = C.replay_estado(self.led.filas)                                  # el barrido conoce TODAS las ordenes del ledger aunque el cuerpo salga al principio
        self.n_pend0 = sum(1 for o in self.ordenes.values() if (not o.cerrada or o.indeterminada) and o.clase_post != 'rechazo')      # ordenes sin cierre (o INDETERMINADAS) al abrir
        self.lote_n0 = sum(1 for r in self.led.filas if r.get('k') == 'lote'); self.ilegible_n0 = sum(1 for r in self.led.filas if r.get('k') == 'ilegible'); accion = ('normal',)      # hallazgo 6
        try: accion = self._cuerpo()
        except BaseException as e: self._excepcion('cuerpo', e)
        if accion[0] == 'ya_complete': self.led.cerrar(); return 'COMPLETE'
        try: self._barrido_final()
        except BaseException as e:
            self._excepcion('barrido_final', e)
            try: self._ilegible('barrido_final', f'excepcion:{type(e).__name__}')
            except BaseException: self.ilegibles.append(dict(lectura='barrido_final', detalle=f'excepcion:{type(e).__name__}'))
        try:
            if accion[0] == 'rechazo': return self._final(accion[1], accion[2], sin_pres=True)
            return self._final(None, None, sin_pres=(self.resume and not self.operado and not self._cambio_real_del_run()))                          # v7 (hallazgo 5): un resume que NO llego a operar (rechazado) no pisa informe/manifiesto/checkpoint del run original
        except BaseException as e:
            self._excepcion('final', e); return self._final_emergencia(e)

    def _persistir_corruptas(self):
        """v9/v10 (hallazgo 3): `Ledger()` ya reescribio el fichero sin las lineas corruptas. UNA fuente de verdad: `ledger_reparado.json` (dentro del --out, atomico) con el TOTAL acumulado de eventos de reparacion (`corruptas`) y cuanto de ese total ya esta en filas del ledger (`en_ledger`); la fila lleva solo el DELTA y el informe lee el total del json (no suma filas)."""
        ruta = self.P('ledger_reparado.json'); self.corr_pend = 0; self.corr_total = 0
        try: prev = json.load(open(ruta))
        except (OSError, ValueError): prev = {}
        prev = dict(corruptas=int(prev.get('corruptas') or 0), duplicadas=int(prev.get('duplicadas') or 0), en_ledger=int(prev.get('en_ledger') or 0))
        if self.led.corruptas:
            prev['corruptas'] += self.led.corruptas; prev['duplicadas'] += self.led.duplicadas
            try: C.escribir_atomico(ruta, prev)
            except BaseException as e: self._excepcion('persistir_corruptas', e)
        self.corr_total = prev['corruptas']; self.corr_pend = prev['corruptas'] - prev['en_ledger']; self.corr_json = prev

    def _escribir_ledger_reparado(self):
        """v9/v10 (hallazgo 3): la fila de evidencia (con el DELTA pendiente) entra en el ledger SOLO cuando el run va a operar (tras config distinta / preflight / ya_complete). En un rechazo temprano la evidencia queda en el json y en el informe de rechazo."""
        if self.corr_pend <= 0: return
        self.led.add('ledger_reparado', 'run', sum(1 for r in self.led.filas if r.get('k') == 'ledger_reparado'), corruptas=self.corr_pend, total_acumulado=self.corr_total, t_ns=self.r.now_ns())
        self._alerta(f'LEDGER con {self.corr_total} fila(s) corrupta(s) descartada(s) en total (reparado; las ordenes sin cierre se reconcilian): el informe final nunca sera COMPLETE a secas')
        try: C.escribir_atomico(self.P('ledger_reparado.json'), dict(self.corr_json, en_ledger=self.corr_total))
        except BaseException as e: self._excepcion('ledger_reparado_json', e)
        self.corr_pend = 0

    def _cambio_real_del_run(self):
        """v10 (hallazgos 2): UNICO criterio de 'el estado REAL del run cambio respecto al previo' (decide si un resume que no llego a operar reescribe informe_final/manifiesto/checkpoint). Mira SOLO lo posterior a `n_filas0`.
        CAMBIA: fila nueva estado/cerrada/fill/push_fill/cancel/kill_resuelto (una INDETERMINADA es una `cerrada`), o un kill duro nuevo (severidad>=1) que NO sea el derivado del rechazo ni una lectura transitoria de arranque, o abiertas residuales, o lecturas ilegibles del barrido con ordenes sin cierre en el ledger al abrir.
        NO CAMBIA: el rechazo puro (`resume_rechazado_kill_previo:*`), ledger_reparado, ni un fallo transitorio (saldo/abiertas ilegibles en el arranque) que no deja ordenes vivas sin verificar."""
        for r in self.led.filas[self.n_filas0:]:
            k = r.get('k')
            if k in ('estado', 'cerrada', 'fill', 'push_fill', 'cancel', 'kill_resuelto'): return True
            if k == 'kill':
                m = str(r.get('motivo'))
                if not m.startswith(PREF_RECHAZO) and m not in KILLS_TRANSITORIOS and self._severidad(m, r.get('status')) >= 1: return True
        return bool(self.abiertas_res or (self.ilegibles and self.n_pend0 > 0))

    def _final_emergencia(self, e):
        """Ultimo recurso si `_final` fallo: informe minimo FAILED a disco (o fallback/stderr)."""
        inf = dict(status='FAILED', motivo=f'excepcion en el informe final: {type(e).__name__}: {str(e)[:100]}', run_id=self.run_id, lecturas_ilegibles=self.ilegibles, excepciones=self.exc, kill=self.kill, repro=self._repro())
        C.escribir_con_fallback(self.P('informe_final.json'), inf, f'informe_final_{self.run_id}.json'); return 'FAILED'

    def _cuerpo(self):
        """Devuelve ('normal',) | ('ya_complete',) | ('rechazo', status, motivo). NO hace `return self._final(...)` (lo hace `correr`, tras el barrido)."""
        man = None
        if os.path.exists(self.P('run_manifest.json')):
            try: man = json.load(open(self.P('run_manifest.json')))
            except ValueError: man = None
        resume = man is not None and man.get('run_id') == self.run_id; self.resume = resume
        if resume and man.get('config_sha') != self.cfg.sha(): self.log('RESUME con config distinta: BLOQUEADO', err=True); return ('rechazo', 'FAILED', 'config_distinta_en_resume')
        if resume and man.get('estado') == 'FINALIZADO' and man.get('status_final') == 'COMPLETE': self.log('run ya COMPLETE: nada que hacer'); return ('ya_complete',)
        s0 = man['saldo_inicial'] if resume else self._saldo()
        try: self.pres = C.Presupuesto(self.cfg, s0)
        except C.Invariante as e: self.pres = None; self.log(f'preflight: {e}', err=True); return ('rechazo', 'BLOCKED', f'preflight:{e}')
        if resume: self.t_ini_iso = man.get('inicio_utc', self.t_ini_iso)
        self.chrony = (self.s.chrony() if self.real and hasattr(self.s, 'chrony') else None)
        if not resume: self._manifest('EN_CURSO')                                                           # v7 (hallazgo 5): un RESUME no pisa el manifiesto del run original hasta que de verdad va a operar (si se rechaza, el manifiesto/informe/checkpoint originales quedan intactos)
        self.log(f'INICIO run={self.run_id} real={self.real} resume={resume} saldo_inicial={self.pres.s0} suelo={self.pres.suelo} config_sha={self.cfg.sha()[:12]} codigo_sha={C.sha_codigo()[:12]}')
        ck = self._validar_checkpoint(); self.log(f'checkpoint: {ck}'); self.ordenes, res = C.replay_estado(self.led.filas)
        self._escribir_ledger_reparado()
        if self.led.corruptas or self.led.duplicadas: self.log(f'ledger: corruptas={self.led.corruptas} duplicadas={self.led.duplicadas} (reparado)', err=True)
        if self.kill: return ('normal',)
        for o in [o for o in self.ordenes.values() if (not o.cerrada or o.indeterminada) and o.clase_post != 'rechazo']:            # reconciliacion de vivas/ambiguas/INDETERMINADAS de una ejecucion anterior
            if o.t_envio_ns is None and o.clase_post is None: self.cnt['intencion_sin_post'] += 1                  # intencion sin POST registrado: pudo salir: se reconcilia igual
            self.reconciliar_orden(o, 'arranque'); o.cerrada = True
            if self.kill: return ('normal',)
        resueltos = {r.get('motivo') for r in self.led.filas if r.get('k') == 'kill_resuelto'}                          # v7 (hallazgo 2b): un kill por una orden luego VERIFICADA como inexistente no impide reanudar
        duros = [r for r in self.led.filas if r.get('k') == 'kill' and r.get('motivo') not in BENIGNOS and not str(r.get('motivo')).startswith(BENIGNOS_PREFIJO) and base_kill(r.get('motivo')) not in resueltos]
        try: self._req(); ab = self.s.abiertas_todas()                                                          # v5 (hallazgo 4): la wallet dedicada debe tener 0 abiertas ANTES de enviar (propias ya reconciliadas, ajenas = nunca se tocan)
        except Exception: ab = None
        if not isinstance(ab, (list, tuple, set)) or ab:
            self._alerta(f'ANTES DE EMPEZAR la wallet dedicada no tiene 0 ordenes abiertas legibles: {ab!r}: no se envia nada'); self._matar('abiertas_previas_o_ilegibles', 'BLOCKED'); return ('normal',)
        _, res = C.replay_estado(self.led.filas); self.pres.actualizar(gasto_ledger=res['gasto_fills_usd'])
        self._asentar(self._ult_post_ns(), interrumpible=False)                                                  # v6 (hallazgo 2): saldo on-chain ANTES del primer lote, ya asentado el ultimo POST de un run previo, y recomputado contra el ledger
        sal0 = self._saldo()
        if sal0 is None: self._alerta('saldo on-chain ilegible en el arranque: no se envia nada'); self._matar('saldo_ilegible_en_arranque', 'BLOCKED'); return ('normal',)
        self.pres.actualizar(saldo=sal0)
        if abs((self.pres.s0 - sal0) - res['gasto_fills_usd']) > self.cfg.tol_saldo_usd + 1e-9:
            self._alerta(f'saldo on-chain {sal0} != saldo_inicial {self.pres.s0} - gasto del ledger {res["gasto_fills_usd"]}: descuadre antes de enviar'); self._matar(f'saldo_descuadrado_en_arranque {self.pres.s0 - sal0:.4f} vs ledger {res["gasto_fills_usd"]:.4f}', 'BLOCKED'); return ('normal',)
        # hallazgo 5: el bloqueo por kill duro previo NO depende solo de que exista la fila `kill` (un SIGKILL entre el relleno y esa fila la habria perdido): tambien se deduce del propio ledger (rellenos o indeterminadas)
        n_ileg = sum(1 for r in self.led.filas if r.get('k') == 'ilegible')                 # v5 (hallazgo 5): una lectura final ilegible de un run previo (BLOCKED sin fila kill) tambien bloquea el relanzamiento: se deduce del LEDGER
        if duros or res['n_fills'] > 0 or res['n_indeterminadas'] > 0 or n_ileg:
            motivo = duros[-1]['motivo'] if duros else (f'ledger_con_rellenos={res["n_fills"]}' if res['n_fills'] > 0 else (f'ledger_con_indeterminadas={res["n_indeterminadas"]}' if res['n_indeterminadas'] > 0 else f'ledger_con_lecturas_ilegibles={n_ileg} (cuenta del ledger de ESTE --out: verificar a mano y relanzar con OTRO --out; cambiar solo el run-id NO lo desbloquea)'))
            self._matar(motivo_rechazo_resume(motivo), (duros[-1].get('status') if duros else None) or ('PARTIAL' if res['n_fills'] > 0 else 'BLOCKED')); self.log(f'RESUME RECHAZADO: {motivo}; no se envia nada', err=True)
            return ('normal',)
        if resume: self._manifest('EN_CURSO')                                                               # v7 (hallazgo 5): ya no hay rechazo posible: el resume pasa a ser el run en curso
        self.operado = True; self.t_lim_ns = t_lim = self.t_inicio_ns + int(self.cfg.max_minutos * 60e9); idx = 0; enviadas0 = sum(1 for r in self.led.filas if r.get('k') == 'intencion'); self.cnt['enviadas_previas'] = enviadas0
        while not self.kill:
            if self._chequear_senal(): break
            if self.r.now_ns() > t_lim: self._matar('max_minutos', 'PARTIAL'); break
            n_int = sum(1 for r in self.led.filas if r.get('k') == 'intencion')
            if n_int >= self.cfg.max_ordenes: self._matar('max_ordenes', 'PARTIAL'); break
            lote = []
            while idx < len(self.slots) and len(lote) < min(self.cfg.lote, self.cfg.max_ordenes - n_int):
                s = self.slots[idx]; idx += 1
                if f'{self.run_id}|s{s.i}' in self.ordenes or any(r.get('k') == 'saltado' and r.get('slot') == s.i for r in self.led.filas): continue
                if s.modo == 'lejos' or self.fase == 'B': lote.append(s)
            if not lote: self._matar('slots_agotados', 'PARTIAL'); break
            self.cnt['lotes'] += 1; self.lote(lote); ancl = self._tras_lote(len(lote))
            self.log(f'lote {self.lote_n0 + self.cnt["lotes"]}: anclas_directas={ancl} intenciones={self.cnt["intenciones"]} fills={self.cnt["fills"]} saldo={self.pres.saldo} gasto={self.pres.gasto}')
            if ancl is not None and not self.kill:
                tot, por = ancl, self.anclas_ult[1]
                if not C.faltan_anclas(self.cfg, tot, por): self.log('objetivo de anclas alcanzado'); break
        if not self.kill and cfg_b(self.cfg): self._fase_b()
        return ('normal',)

    def _fase_b_terminar(self, motivo):
        """v7 (hallazgo 6): FIN BENIGNO de la fase B (sin kill: el status del run es el de la fase A). Queda en el ledger y en el informe (`fase_b.fin`)."""
        if self.fase_b_fin is None:
            self.fase_b_fin = motivo; self.log(f'FASE B terminada ({motivo}); el run conserva el status de la fase A')
            if self.led is not None: self.led.add('fase_b_fin', 'run', 0, motivo=motivo, t_ns=self.r.now_ns(), rellenos=self.fills_b, gasto=self.gasto_b)

    def _fase_b(self):
        """Fase B (opcional, solo con fase_b_max_rellenos>0 Y confirmada): ordenes 'top' a 0,01 sobre el nivel con cola de un token barato (casi resuelto: bid==0,01, ask<=0,05), para provocar rellenos PARCIALES y orden propia VISIBLE en el libro publico.
        v7 (hallazgo 6): vida propia (`fase_b_min_vida_s`, no los 90 s de A); respeta max_ordenes, max_minutos y los topes fase_b_*; sin token barato (tras `fase_b_espera_s`) / limites de tiempo o cantidad = fin BENIGNO (el run conserva COMPLETE/PARTIAL de la fase A, nunca BLOCKED por eso). Tope propio de rellenos y de coste; seguimiento 1 Hz de size_matched. Cualquier relleno cuenta contra el mismo presupuesto duro."""
        import random
        cfg = self.cfg; rg = random.Random(cfg.seed + 1); self.fase = 'B'; self.sin_mercado = 0; self.log(f'FASE B: hasta {cfg.fase_b_ordenes} ordenes top, max {cfg.fase_b_max_rellenos} rellenos / {cfg.fase_b_tope_usd} $')
        sl = [C.Slot(1000 + j, C.COINS[j % 4], j % 2, round(rg.uniform(cfg.hold_b_min_s, cfg.hold_b_max_s), 3), 'top') for j in range(cfg.fase_b_ordenes)]
        i = 0
        while i < len(sl) and not self.kill:
            if self._chequear_senal(): break
            if self.t_lim_ns is not None and self.r.now_ns() > self.t_lim_ns: self._fase_b_terminar('max_minutos'); break
            resto = cfg.max_ordenes - sum(1 for r in self.led.filas if r.get('k') == 'intencion')
            if resto < 1: self._fase_b_terminar('max_ordenes'); break
            n_ok = min(4, resto, cfg.fase_b_max_rellenos - self.fills_b, int((cfg.fase_b_tope_usd - self.gasto_b) / cfg.coste_orden + 1e-9))   # nunca mas ordenes vivas que rellenos que aun caben en el tope (ni mas ordenes que max_ordenes)
            if n_ok < 1: self._matar('fase_b_tope_rellenos', 'PARTIAL'); break
            lote = [s for s in sl[i:i + n_ok] if f'{self.run_id}|s{s.i}' not in self.ordenes]; i += n_ok
            if not lote: continue
            self.cnt['lotes'] += 1; self.lote(lote); self._tras_lote(len(lote))
            if self.fase_b_parar and not self.kill: self._fase_b_terminar(self.fase_b_parar); break

    anclas_por_moneda_fn = None

    def _ilegible(self, lectura, detalle=''):
        """Una lectura del barrido final que NO se pudo hacer/validar (hallazgo 9): se lista en el informe y el status nunca puede ser COMPLETE."""
        self.ilegibles.append(dict(lectura=lectura, detalle=detalle)); self.cnt['lecturas_ilegibles'] += 1; self.log(f'LECTURA ILEGIBLE en el barrido final: {lectura} {detalle}', err=True)
        if self.led is not None: self.led.add('ilegible', f'{self.run_id}|{lectura}', self.ilegible_n0 + len(self.ilegibles), detalle=detalle, t_ns=self.r.now_ns())

    def _alerta(self, msg):
        """Alerta EXPLICITA (nunca silencio): stderr + ALERTA_paquete_l.txt en el directorio del run + lista en el informe final (`alertas`)."""
        self.alertas.append(msg)
        try: self.log('ALERTA ' + msg, err=True)
        except Exception: pass
        try:
            with open(self.P('ALERTA_paquete_l.txt'), 'a') as f: f.write(f'{dt.datetime.now(dt.timezone.utc).isoformat()} {msg}\n')
        except OSError: pass

    def _barrido_final(self):
        """Barrido (hallazgos 3 y 9 v3; 1, 4 y 6 v5), SIEMPRE: (1) cancela cada viva; (2) reconcilia (con reintentos y backoff) toda orden sin cierre o INDETERMINADA; (3) espera el asentamiento desde el ultimo POST y lee get_open_orders SIN filtro de
        asset: cada id propio se cancela con reintentos, y lo que siga abierto (o sea ajeno) => BLOCKED con la lista y ALERTA; ilegible = INDETERMINADA; (4) saldo final contra el ledger."""
        for c in list(self.vivas):
            try: self._cancelar_completa(c)
            except BaseException as e: self.cnt['barrido_excepciones'] += 1; self.log(f'cancelar_viva en barrido: {type(e).__name__}: {str(e)[:100]}', err=True)
            self.vivas.pop(c, None)                                    # si cancelar_viva fallo a medias la orden NO esta cerrada: la recoge el paso (2)
        for o in [o for o in self.ordenes.values() if (not o.cerrada or o.indeterminada) and o.clase_post != 'rechazo']:
            try: self.reconciliar_orden(o, 'barrido_final'); o.cerrada = True
            except BaseException as e: self._ilegible(f'reconciliar:{o.clave}', f'excepcion:{type(e).__name__}')
        if self.ordenes:
            self._asentar(self._ult_post_ns(), interrumpible=False)           # v5 (hallazgo 6): ni abiertas ni saldo se leen antes de index_gracia + 3 s desde el ultimo POST (un 'vacio' antes no prueba nada)
        self._abiertas_final()
        if self.pres is not None and self.ordenes:
            sal = self._saldo()
            if sal is None: self._ilegible('saldo_final', 'RPC sin lectura valida')
            else:
                self.pres.actualizar(saldo=sal); gl = C.replay_estado(self.led.filas)[1]['gasto_fills_usd']; self.pres.actualizar(gasto_ledger=gl)
                if self._saldo_cae_mas_que_ledger(sal, gl): self._matar(f'saldo_cae_mas_que_ledger_final {self.pres.s0 - sal:.4f} > {gl:.4f}', 'BLOCKED')

    def _abiertas_final(self):
        propios = {str(o.oid).lower(): o for o in self.ordenes.values() if o.oid}
        def leer():
            try: self._req(); r = self.s.abiertas_todas()
            except Exception as e: self.log(f'abiertas_todas fallo {type(e).__name__}', err=True); r = None
            return r
        ab = leer()
        if not isinstance(ab, (list, tuple, set)): self._ilegible('abiertas_todas', 'None/ilegible/paginacion no garantizada'); return
        mias = [x for x in ab if str(x).lower() in propios]
        for x in mias:                                                                                        # cada id abierto propio se cancela con reintentos y backoff ANTES de declarar nada (y su cierre queda en el ledger)
            try: self.reconciliar_orden(propios[str(x).lower()], 'abierta_en_el_barrido_final')
            except BaseException as e: self._ilegible(f'reconciliar:{x}', f'excepcion:{type(e).__name__}')
        for espera in ((1.0, 2.0) if mias else ()):                                                           # v6 (hallazgo 9): tras cancelar, la lista de abiertas puede tardar en reflejarlo: se relee hasta 2 veces con backoff (reloj del barrido) antes de declarar viva
            self.r.sleep(espera); nuevo = leer()
            if not isinstance(nuevo, (list, tuple, set)): self._ilegible('abiertas_todas', 'relectura None/ilegible'); return
            ab = nuevo
            if not any(str(x).lower() in propios for x in ab): break
        if ab:
            ajenas = [x for x in ab if str(x).lower() not in propios]; self.cnt['abiertas_residuales'] += len(ab); self.abiertas_res = True
            self._alerta(f'ORDENES ABIERTAS AL FINAL en la wallet dedicada: propias vivas={[x for x in ab if str(x).lower() in propios]} ajenas al run={ajenas}')
            self._matar('abiertas_residuales', 'BLOCKED')

    def _evid_filas(self):
        """Eventos del canal de usuario para el informe: los de la ultima lectura del lote/final (`anclas_ev`) o, sin ella, UNA lectura tolerante (`C.leer_evid`: .gz truncado / linea rota no lanzan; los ficheros ilegibles quedan en `evid_ilegibles`)."""
        if self.anclas_ev is not None: ev, ileg = self.anclas_ev
        elif self.evid: ev, ileg = C.leer_evid(self.evid)
        else: ev, ileg = [], []
        self.evid_ilegibles = list(ileg); return ev

    # ---------------------------------------------------------------- informe final
    def _final(self, status, motivo, sin_pres=False):
        if sin_pres or self.pres is None:                             # rechazo antes de operar (config distinta / preflight / resume rechazado): NO pisa el informe_final, el manifiesto ni el checkpoint de una ejecucion previa
            if status is None: status, motivo = (self.kill_status or 'FAILED'), (self.kill or 'sin_presupuesto')
            if self.ilegibles and status in ('COMPLETE', 'PARTIAL'): status = 'BLOCKED'
            nombre = 'informe_final.json' if not os.path.exists(self.P('informe_final.json')) else 'informe_rechazo_%s_%d.json' % (dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%f'), os.getpid())
            C.escribir_con_fallback(self.P(nombre), dict(status=status, motivo=motivo, run_id=self.run_id, rechazo_de_resume=bool(self.resume and not self.operado), filas_corruptas_ledger=(self.corr_total or (self.led.corruptas if self.led is not None else 0)), kill=self.kill, alertas=self.alertas, ledger_filas=(len(self.led.filas) if self.led is not None else None), lecturas_ilegibles=self.ilegibles, excepciones=self.exc, repro=self._repro()), f'{nombre[:-5]}_{self.run_id}.json'); self.log(f'FIN {status} {motivo}', err=True); self.led.cerrar(); return status
        O, res = C.replay_estado(self.led.filas); ancl, por = self._leer_anclas(); cfg = self.cfg; ev = self._evid_filas()                  # v7 (hallazgo 10): una lectura de anclas; sus eventos sirven para los relojes
        if status is None:
            if self.kill == 'fase_b_tope_rellenos' and ancl is not None and not C.faltan_anclas(cfg, ancl, por): status, motivo = 'COMPLETE', 'objetivo de anclas alcanzado; fase B terminada en su tope de rellenos'
            elif self.kill_status: status, motivo = self.kill_status, self.kill
            elif ancl is not None and not C.faltan_anclas(cfg, ancl, por): status, motivo = 'COMPLETE', 'objetivo de anclas alcanzado'
            else: status, motivo = 'PARTIAL', 'objetivo de anclas no alcanzado'
        pf = self.led.fallos_escritura + self.io_fallos                              # hallazgo 10: si hubo escrituras fallidas el registro en disco NO es completo => nunca COMPLETE/PARTIAL a secas
        if pf and status in ('COMPLETE', 'PARTIAL'): status, motivo = 'BLOCKED', f'{motivo}; escrituras fallidas: ledger={self.led.fallos_escritura} otros={self.io_fallos} (filas en memoria/ledger.jsonl.fallback/stderr)'
        # hallazgo 9: COMPLETE exige TODO verificado: sin lecturas finales ilegibles, sin abiertas residuales, sin ordenes indeterminadas, sin vivas
        if status == 'COMPLETE' and (self.ilegibles or self.abiertas_res or res['n_indeterminadas'] or self.vivas): status, motivo = 'BLOCKED', f'{motivo}; NO verificado: lecturas_ilegibles={len(self.ilegibles)} abiertas_residuales={self.abiertas_res} indeterminadas={res["n_indeterminadas"]}'
        elif status == 'PARTIAL' and (self.ilegibles or self.abiertas_res or res['n_indeterminadas']): status, motivo = 'BLOCKED', f'{motivo}; ademas NO verificado: lecturas_ilegibles={len(self.ilegibles)} abiertas_residuales={self.abiertas_res} indeterminadas={res["n_indeterminadas"]}'
        corr = self.corr_total or self.led.corruptas        # v7 (pendiente ronda 4): filas corruptas del ledger descartadas (en ESTE proceso o en uno anterior de este --out) = el registro pudo perder un evento
        if corr:                                                                     # nunca COMPLETE silencioso: PARTIAL + alerta (las ordenes sin cierre ya se reconciliaron; para un COMPLETE limpio, otro --out)
            if status == 'COMPLETE': status, motivo = 'PARTIAL', f'{motivo}; ledger con {corr} fila(s) corrupta(s) descartada(s): verificar a mano'
            if not any('LEDGER con' in a for a in self.alertas): self._alerta(f'LEDGER con {corr} fila(s) corrupta(s) descartada(s) (en este o en un proceso anterior del --out)')
        if self.evid_ilegibles: self._alerta(f'cancel_evid ilegibles/truncados (se cuenta lo legible; las anclas pueden estar subestimadas): {self.evid_ilegibles}')
        C.exigir(status in STATUS, f'status invalido: {status}')
        # cobertura
        k = lambda n: sum(1 for r in self.led.filas if r.get('k') == n)
        cob = dict(esperado_slots=cfg.plan_ordenes, intenciones=k('intencion'), posts=k('post'), saltados=k('saltado'), ack_ok=sum(1 for r in self.led.filas if r.get('k') == 'post' and r.get('clase') == 'ok'), rechazos=sum(1 for r in self.led.filas if r.get('k') == 'post' and r.get('clase') == 'rechazo'),
                   http429=sum(1 for r in self.led.filas if r.get('k') == 'post' and r.get('clase') == '429'), ambiguos=sum(1 for r in self.led.filas if r.get('k') == 'post' and r.get('clase') == 'ambiguo'), canceladas_ok=sum(1 for r in self.led.filas if r.get('k') == 'cancel' and r.get('ok')),
                   fills=res['n_fills'], indeterminadas=res['n_indeterminadas'], duplicados_ledger=self.led.duplicadas, filas_corruptas_ledger=corr, anclas_directas=ancl, anclas_por_moneda=por,
                   intenciones_por_moneda=dict(collections.Counter(o.coin for o in O.values())), por_dia={self.t_ini_iso[:10]: k('intencion')})
        fase_b = dict(activada=cfg_b(cfg), ordenes=sum(1 for o in O.values() if o.modo == 'top'), rellenos=self.fills_b, gasto_usd=self.gasto_b, fin=(self.fase_b_fin or (self.kill if self.fase == 'B' else None)))
        inf = dict(status=status, motivo=motivo, run_id=self.run_id, cobertura=cob, fase_b=fase_b, presupuesto=dict(saldo_inicial=self.pres.s0, saldo_final=self.pres.saldo, suelo=self.pres.suelo, gasto=self.pres.gasto, perdida_dura=cfg.perdida_dura, toco_suelo=self.pres.toca_suelo()),
                   latencias=C.d_proc_stats(self.led.filas), relojes=dict(local='time.time_ns alineado a time.monotonic_ns desde el arranque (inmune a steps)', chrony=getattr(self, 'chrony', None), vs_exchange=C.reloj_stats(ev)), anclas_detalle=self._anclas_detalle(),
                   residuales=dict(posiciones=C.residuales(self.led.filas), nota='una posicion no se elimina sin vender; acotada por cfg.fase_b_* y top_ask_max; valor final con `--liquidar-informe RUN_DIR` (desenlace oficial por gamma publico; la redencion de ganadoras es MANUAL, este codigo no firma redenciones)'), excepciones=self.exc, lecturas_ilegibles=self.ilegibles, alertas=self.alertas, kills_resueltos=self.kills_resueltos, evid_ilegibles=self.evid_ilegibles, signal=self.senal, senales_recibidas=self.n_senales, gtd_expira_s=cfg.gtd_expira_s, ultimo_rechazo=self.ultimo_rechazo, escrituras_fallidas=dict(ledger=self.led.fallos_escritura, otros=self.io_fallos), viva_al_final=len(self.vivas), fin_utc=dt.datetime.now(dt.timezone.utc).isoformat(), repro=self._repro())
        ruta = self.P('informe_final.json')
        if os.path.exists(ruta):                                                     # v7 (hallazgo 5): el informe de un proceso anterior NO se pierde (traceback/alertas): se conserva con marca de tiempo
            try: os.replace(ruta, self.P('informe_final.previo_%s_%d.json' % (dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S%f'), os.getpid())))
            except OSError: pass
        C.escribir_con_fallback(ruta, inf, f'informe_final_{self.run_id}.json'); self._manifest('FINALIZADO', dict(status_final=status, fin_utc=inf['fin_utc'], cobertura=cob)); self._checkpoint(dict(status_final=status))
        self.log(f'FIN status={status} motivo={motivo} cobertura={json.dumps(cob, default=str)}'); self.led.cerrar(); return status

    def _anclas_detalle(self):
        """Percentiles de alta/cancelacion vs envio (plan_paquete_l.analiza): SOLO en el informe final, una vez por run (el vendor relee los ficheros; un .gz truncado no lanza: queda anotado)."""
        if not self.evid: return None
        try: return C.cargar_vendor('plan_paquete_l').analiza(self.evid)
        except Exception as e: return dict(error=f'{type(e).__name__}: {str(e)[:80]}')

    def _repro(self): return ' '.join(['python3', '-I', shlex.quote(os.path.abspath(__file__))] + repro_args(self.params))


def construir_parser():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--out', default=None); ap.add_argument('--run-id', default=None); ap.add_argument('--real', action='store_true'); ap.add_argument('--confirmacion', default=None)
    ap.add_argument('--escenario', default='base', choices=sorted(ESCENARIOS)); ap.add_argument('--objetivo', type=int, default=None); ap.add_argument('--max-ordenes', type=int, default=None)
    ap.add_argument('--fase-b', type=int, default=0, help='N rellenos maximos de la fase B (0 = desactivada)'); ap.add_argument('--tiempo-real', action='store_true', help='dry con reloj real (no virtual)')
    ap.add_argument('--evid-dir', default=None, help='real: directorio de cancel_evid del canal de usuario'); ap.add_argument('--liquidar-informe', default=None, metavar='RUN_DIR', help='valor final de las posiciones residuales de un run (gamma publico, solo GET; no modifica el ledger pero ESCRIBE RUN_DIR/liquidacion_residuales.json)')
    ap.add_argument('--verificar-mercados', action='store_true', help='solo lectura (GET gamma publico): valida los mercados 5m vigentes; no envia nada')
    ap.add_argument('--preflight-publico', action='store_true', help='SOLO LECTURA, sin credenciales: por moneda gamma + /book (tick, min size, neg_risk); no firma ni envia')
    ap.add_argument('--preflight-real', action='store_true', help='SOLO LECTURA: ademas lee las credenciales DEDICADAS, deriva/valida API creds, saldo, open orders, reloj y firma EN LOCAL una orden de prueba (sin enviarla). Sin POST posible; no pide fichero de confirmacion')
    return ap


PARAM_A_OPCION = dict(run_id='--run-id', out='--out', escenario='--escenario', objetivo='--objetivo', max_ordenes='--max-ordenes', fase_b='--fase-b')       # v7 (hallazgo 8): nombres REALES de argparse
_REPRO_SUF = {}                                                                          # v10 (hallazgo 4): sufijo del dry-run de reproduccion UNA vez por run (clave = run_id/out): `_repro()` se llama desde varios sitios y debe dar el MISMO comando
PARAM_BANDERA = dict(tiempo_real='--tiempo-real')                       # v8 (hallazgo 1): NINGUNA bandera que habilite envio (--real/--confirmacion/--evid-dir) entra en el comando de reproduccion


def repro_args(params):
    """Argumentos de linea de comandos (nombres reales de argparse, valores entrecomillados) que reproducen `params` como DRY-RUN (sin --real ni --confirmacion). Test de ida y vuelta: `construir_parser().parse_args(...)`."""
    out = []; params = dict(params)
    if params.get('real'):                                                                                  # v8 (hallazgo 1): la reproduccion de un run REAL es un DRY-RUN (SenderSim) en un --out APARTE: nunca toca el ledger del real
        # v9 (hallazgo 5): ruta ABSOLUTA derivada del out real (o de OUT_BASE/run_id si falta) + sufijo unico (hora, pid, contador): jamas relativa al cwd ni un directorio reutilizado
        base = params.get('out') or os.path.join(C.OUT_BASE, str(params.get('run_id') or 'run'))
        clave = str(params.get('run_id') or base); suf = _REPRO_SUF.setdefault(clave, '%s_%d_%d' % (dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%S'), os.getpid(), len(_REPRO_SUF) + 1))
        params['out'] = os.path.abspath(str(base)).rstrip('/') + '_repro_dry_' + suf
    for k, v in params.items():
        if v is None or v is False: continue
        if k in PARAM_BANDERA: out.append(PARAM_BANDERA[k])
        elif k in PARAM_A_OPCION: out.append(f'{PARAM_A_OPCION[k]}={shlex.quote(str(v))}')
    return out


ESCENARIOS = {
    'base': {},
    'fill_total': dict(fill_a={4: (5.0, 1.2)}),                           # la 5a orden se rellena entera a 1,2 s: corte inmediato
    'fill_parcial': dict(fill_a={2: (2.0, 1.0)}),
    '429': dict(err_429_en_post={5, 6, 7}),
    'ambiguo': dict(err_ambiguo_post={3}),
    'rechazo2': dict(rechazo_post={2, 3}),
    'cancel_pendiente': dict(cancel_pendiente={2}),
}


def liquidar_informe(run_dir, get=None):
    """Valor FINAL de las posiciones residuales de un run con el desenlace OFICIAL (gamma publico, solo GET). Lee el ledger sin tocarlo, pero ESCRIBE `liquidacion_residuales.json` (atomico) en el directorio del run. Sin desenlace (mercado aun no cerrado) => valor None (missing != 0). No firma ni redime nada (las ganadoras se redimen a mano)."""
    locks = C.tomar_locks(None, run_dir, wallet_lock=False)                                                                                     # v7 (hallazgo 3): escribe en run_dir: no mientras otro proceso lo use
    if not locks: raise C.Invariante(f'{run_dir} en uso por otra instancia (o lock no disponible): no escribo nada')
    try: return _liquidar(run_dir, get)
    finally: C.liberar_locks(locks)


def _liquidar(run_dir, get):
    filas = C.leer_ledger_solo_lectura(os.path.join(run_dir, 'ledger.jsonl')); res = C.residuales(filas); slug_de = {r['tok']: r.get('slug') for r in filas if r.get('k') == 'intencion'}; ganador = {}                   # v6 (hallazgo 7): SOLO lectura, el ledger no se abre en append ni se repara
    if get is None:
        import requests; get = lambda url, params: requests.get(url, params=params, timeout=8).json()
    for r in res:
        slug = slug_de.get(r['tok']); ganador[r['tok']] = None
        try: ev = get('https://gamma-api.polymarket.com/events', {'slug': slug}); m = ev[0]['markets'][0]
        except Exception: continue
        if not m.get('closed'): continue
        toks = json.loads(m['clobTokenIds']) if isinstance(m['clobTokenIds'], str) else m['clobTokenIds']; pr = json.loads(m['outcomePrices']) if isinstance(m['outcomePrices'], str) else m['outcomePrices']
        if r['tok'] in toks and len(pr) == len(toks) and sorted(float(x) for x in pr) == [0.0, 1.0]: ganador[r['tok']] = float(pr[toks.index(r['tok'])]) == 1.0
    out = dict(run_dir=run_dir, residuales=C.valor_residual(res, ganador), cobertura_desenlace=(sum(1 for g in ganador.values() if g is not None), len(ganador)), nota='redencion de ganadoras MANUAL; perdedoras valen 0 y no requieren accion')
    C.escribir_atomico(os.path.join(run_dir, 'liquidacion_residuales.json'), out); return out


def verificar_mercados():
    """Solo GET a gamma publico: valida los mercados 5m vigentes de las 4 monedas con las MISMAS comprobaciones que el envio real (slug, outcomes<->tokens por etiqueta, endDate, tick, minsize). No envia nada."""
    import pl_sender_real as R
    m = R.MercadosReal(); vistos = m.mercados(); por = collections.Counter(x[1] for x in vistos)
    for x in vistos: print('OK', x[0], 'fin', x[2], 'tokens[Up,Down]=[..%s, ..%s]' % (x[3][0][-6:], x[3][1][-6:]), 'neg_risk', x[4])
    for sl, why in m.rechazados.items():
        if m.cache.get(sl, (0, None))[1] is None: print('RECHAZADO', sl, why)
    print('monedas con mercado verificado:', dict(por)); return 0 if set(por) == set(C.COINS) else 2


def preflight_cli(autenticado, out=None):
    """R1: `python3 -I paquete_l.py --preflight-publico|--preflight-real [--out DIR]`. Escribe preflight_<modo>_<ts>.json (solo booleanos/cifras publicas) y lo imprime. Exit 0 = ok, 2 = algo no valido. Jamas envia."""
    import pl_sender_real as R
    if autenticado: C.exigir_aislamiento()
    cfg = C.Config(); res = R.preflight(cfg, autenticado=autenticado); d = out or os.path.join(C.OUT_BASE, 'preflight'); os.makedirs(d, exist_ok=True)
    ruta = os.path.join(d, 'preflight_%s_%s.json' % ('real' if autenticado else 'publico', time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())))
    C.escribir_con_fallback(ruta, res, os.path.basename(ruta)); print(json.dumps(res, indent=1, default=str, sort_keys=True)); print('PREFLIGHT', 'OK' if res['ok'] else 'NO OK', ruta); return 0 if res['ok'] else 2


def main():
    ap = construir_parser(); a = ap.parse_args()
    if a.verificar_mercados: return verificar_mercados()
    if a.preflight_publico or a.preflight_real: return preflight_cli(a.preflight_real, a.out)
    if a.liquidar_informe:
        try: print(json.dumps(liquidar_informe(a.liquidar_informe), indent=1, default=str)); return 0
        except C.Invariante as e: print(f'liquidar-informe: {e}', file=sys.stderr); return 2
    kw = {}
    if a.objetivo: kw['objetivo_anclas'] = a.objetivo
    if a.max_ordenes: kw['max_ordenes'] = a.max_ordenes
    if a.fase_b: kw['fase_b_max_rellenos'] = a.fase_b
    cfg = C.Config(**kw); run_id = a.run_id or ('dry-' if not a.real else 'real-') + dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ'); out = a.out or os.path.join(C.OUT_BASE, run_id)
    params = dict(run_id=run_id, out=out, escenario=a.escenario, objetivo=a.objetivo, max_ordenes=a.max_ordenes, fase_b=a.fase_b or None, real=a.real, tiempo_real=a.tiempo_real, evid_dir=a.evid_dir, confirmacion=a.confirmacion)
    if a.real:
        C.exigir_aislamiento()                                                              # v3 (hallazgo 1): `python3 -I` y directorio sin .py ajenos
        exigir_confirmacion(a.confirmacion, cfg, C.sha_codigo())
    locks = C.locks_de_run(cfg, out, a.real)                                                  # v7 (hallazgo 3): instancia unica por wallet y por --out, ANTES de construir nada (el sender real crea el directorio de evidencias y el canal de usuario)
    if not locks: print(f'INSTANCIA UNICA: ya hay otro proceso con la wallet {cfg.wallet} o el --out {out} (o no se pudo tomar el lock): salgo sin tocar nada', file=sys.stderr); return 2
    try:
        if a.real:
            import pl_sender_real as R
            reloj = Reloj(); sender, mercados, libro = R.construir(cfg, evid_dir=a.evid_dir or os.path.join(out, 'cancel_evid'))
            P = Paquete(cfg, sender, mercados, out, reloj, run_id, real=True, libro=libro, evid_patron=os.path.join(a.evid_dir or os.path.join(out, 'cancel_evid'), 'cancel_evid_*.jsonl*'), params=params, locks=locks)
            P.anclas_unico = sender.anclas
        else:
            reloj = Reloj() if a.tiempo_real else RelojVirtual(); sender = SenderSim(reloj, **ESCENARIOS[a.escenario]); mercados = MercadosSim(reloj)
            P = Paquete(cfg, sender, mercados, out, reloj, run_id, real=False, anclas_fn=lambda: sum(P.anclas_ledger_por_moneda().values()), params=params, locks=locks)
            P.anclas_por_moneda_fn = P.anclas_ledger_por_moneda
        st = P.correr(); print(f'STATUS {st}  out={out}'); return 0 if st in ('COMPLETE', 'PARTIAL') else 2
    finally: C.liberar_locks(locks)


if __name__ == '__main__': sys.exit(main())
