#!/usr/bin/env python3
"""binance_registro_ms.py -- registro Binance (aggTrade + bookTicker, 6 monedas) en PROCESO PROPIO (screen `bnreg`).

DISENO_CAPTURA_INDEPENDIENTE_L2_09nov.md, FASE 1. Motivo: el registro vivia dentro del hijo `libro_estado_ws.py --hijo` de `observadores`; cada
reinicio de observadores (restart_ram 03:20/10:20/22:20Z, OOM-killer 14:00:29Z del 09-Nov = 148 s, watchdog) dejaba un hueco de 46-148 s en `x`.

SOLO LECTURA de un feed publico: sin claves, sin ordenes, sin dinero. Imports: SOLO stdlib + `websockets` (ningun modulo local): el watchdog solo lo marca
STALE si se edita ESTE fichero.

Salida (mismo formato y misma ruta que el hijo -> ningun lector cambia):
  /root/polymarket-research-datalogs/maker_ms_<dia>_<pid>.csv.gz   cabecera `tipo,t_ms,id,c1,c2,c3,c4,c5`, gzip nivel 9, volcado cada 5 s
    x,T,sym,p,q,m,E,recv_ms          (aggTrade; EXACTAMENTE 8 campos)
    b,recv_ms,sym,bid,ask,B,A,       (bookTicker, solo si cambia (bid,ask); EXACTAMENTE 8 campos)
  Ficheros hermanos (pequenos, fuera de git, retencion 60 d):
    binance_integridad_<dia>.csv     1 fila/min/simbolo: n_x, aggTradeId min/max/distintos/duplicados/fuera de orden/faltantes, n_b, updateId min/max, recv-E p50/p90/p99, conn_id
    binance_huecos_<dia>.csv         eventos `evento,t_ms,conn_id,pid,motivo`: arranque/lock_tomado/conexion/caida/caida_proceso(t_ms = ultimo latido del proceso anterior)/parada/parada_centinela/
                                     salida_sin_datos/cola_llena/escritor_fallo/escritor_recuperado (el hijo de reserva añade hijo_asume/hijo_conexion/hijo_cede)
    binance_registro_estado.json     latido cada 2 s (lo lee el vigia de silencio y el hijo de reserva): estado, lock, cola, escritor_fallando, descartes, ignorados, oom_adj...
Cierre limpio con SIGTERM/SIGINT/SIGHUP (el restart de screen manda SIGHUP): vacia la cola, cierra el gzip, marca `parada`, vuelca la integridad del minuto y el estado.
Un fichero NUEVO por escritura (`maker_ms_<dia>_<pid>.csv.gz`; si el nombre ya existe -- p.ej. un fragmento truncado por SIGKILL -- se usa `<pid><n>`, solo digitos, que casan con los glob de
los lectores): NUNCA se añade un miembro gzip detras de un fragmento posiblemente truncado.
Un solo escritor de Binance: flock en `.binance_registro.lock` y fichero centinela `BNREG_HABILITADO` (kill-switch): sin centinela este proceso queda OCIOSO (sin lock, sin conexion); con
centinela toma el lock (si lo tiene el hijo de observadores, espera 1 s y reintenta); si se borra el centinela, cierra y suelta el lock (el hijo, en reserva, asume en <=5 s).
Hueco = silencio de la UNION de los 6 simbolos > 3 s, o faltantes de aggTradeId, o fila en binance_huecos (nunca silencio de un solo simbolo: BTC calla >2,5 s decenas de veces/h).
Directorio por LIBRO_WS_REGISTRO_DIR (el mismo que el hijo; pruebas en dev lo apuntan a un scratch); BINANCE_WS_URL solo para pruebas con un servidor falso.
"""
import asyncio
import fcntl
import gzip
import json
import os
import queue
import signal
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import websockets

DIR = Path(os.environ.get("LIBRO_WS_REGISTRO_DIR", "/root/polymarket-research-datalogs"))
LOCK_PATH = DIR / ".binance_registro.lock"
CENTINELA = DIR / "BNREG_HABILITADO"
ESTADO_PATH = DIR / "binance_registro_estado.json"
# Copiadas de libro_estado_ws.py (un test las compara; no se importa para no heredar su cierre de imports)
_SIMB_BN = ("btcusdt", "ethusdt", "solusdt", "xrpusdt", "dogeusdt", "bnbusdt")
BINANCE_WS_DEFECTO = "wss://stream.binance.com:9443/stream?streams=" + "/".join(
    [f"{s}@bookTicker" for s in _SIMB_BN] + [f"{s}@aggTrade" for s in _SIMB_BN])
BINANCE_WS = os.environ.get("BINANCE_WS_URL") or BINANCE_WS_DEFECTO
SILENCIO_S = 10.0        # ningun mensaje de la UNION de los 12 streams en 10 s -> cerrar y reconectar
SIN_DATOS_SALIR_S = max(5.0, float(os.environ.get("BNREG_SIN_DATOS_S", "120")))  # (BNREG_SIN_DATOS_S solo en pruebas) 120 s CONECTADO (acumulados) sin recibir NINGUN mensaje -> sys.exit(2) (la screen desaparece y el watchdog la relanza); la espera de backoff NO cuenta
BACKOFF_MAX_S = 30.0
COLA_MAX = 200000
RETENCION_HERMANOS_D = 60
PID = os.getpid()


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] [binance_registro_ms] {msg}", flush=True)


def _ahora_ms():
    return int(time.time() * 1000)


def _dia(t=None):
    return time.strftime("%Y-%m-%d", time.gmtime(t if t is not None else time.time()))


def _atomic(path, text):
    tmp = Path(str(path) + f".tmp{PID}")
    tmp.write_text(text)
    os.replace(tmp, path)


def _pct(v, p):
    if not v:
        return ""
    s = sorted(v)
    return s[min(len(s) - 1, int(p * len(s)))]


def _oom_adj():
    try:
        return int(Path("/proc/self/oom_score_adj").read_text())
    except Exception:
        return None


class Escritor:
    """Hilo propio con cola acotada: si la cola se llena se DESCARTA (y se cuenta: latido + marca `cola_llena`), nunca se frena el socket. Un fichero NUEVO por apertura
    (`maker_ms_<dia>_<pid>.csv.gz`, o `<pid><n>` si el nombre existe: nunca se añade tras un fragmento posiblemente truncado). Si abrir/escribir/volcar FALLA, la linea NO se pierde: se
    retiene y se reintenta cada 1 s con un fichero nuevo (mientras tanto la cola crece; `fallando` y `cola` salen en el latido, marca `escritor_fallo`/`escritor_recuperado`)."""

    def __init__(self):
        self.q = queue.Queue(maxsize=COLA_MAX)
        self.descartes = 0
        self.filas = 0
        self.fallando = False
        self.errores = 0
        self.sin_volcar = 0          # lineas escritas al gzip desde el ultimo flush OK (posible perdida si el fallo llega ahi)
        self.ruta = None
        self._parar = threading.Event()
        self.th = threading.Thread(target=self._loop, daemon=True, name="registro_bn")
        self.th.start()

    def put(self, linea):
        try:
            self.q.put_nowait(linea)
        except queue.Full:
            self.descartes += 1

    def parar(self, esperar=15.0):
        self._parar.set()
        self.th.join(esperar)

    def _abrir(self, hoy):
        DIR.mkdir(parents=True, exist_ok=True)
        n = 0
        while True:
            ruta = DIR / (f"maker_ms_{hoy}_{PID}.csv.gz" if n == 0 else f"maker_ms_{hoy}_{PID}{n}.csv.gz")
            if not ruta.exists():
                break
            n += 1
        f = gzip.open(ruta, "xt", encoding="utf-8", compresslevel=9)     # "x": jamas abre uno existente
        f.write("tipo,t_ms,id,c1,c2,c3,c4,c5\n")
        self.ruta = ruta
        return f

    def _cerrar(self, f):
        try:
            if f:
                f.close()
        except Exception:
            pass

    def _loop(self):
        dia, f, t_flush, desc_log, pendiente, t_err_log, t_parar_fallo = None, None, time.time(), 0, None, 0.0, None
        while True:
            if pendiente is None:
                try:
                    pendiente = self.q.get(timeout=1.0)
                except queue.Empty:
                    if self._parar.is_set():
                        break
            try:
                hoy = _dia()
                if hoy != dia or f is None:
                    self._cerrar(f)
                    f = None
                    f = self._abrir(hoy)
                    dia = hoy
                if pendiente is not None:
                    f.write(pendiente)
                    pendiente = None
                    self.filas += 1
                    self.sin_volcar += 1
                if time.time() - t_flush > 5 or (self._parar.is_set() and self.q.empty()):
                    f.flush()
                    self.sin_volcar = 0
                    t_flush = time.time()
                    if self.fallando:
                        self.fallando = False
                        _log("escritor recuperado")
                        Huecos.marca("escritor_recuperado", _ahora_ms(), motivo=f"errores={self.errores}; fichero={self.ruta.name if self.ruta else ''}")
                    if self.descartes != desc_log:
                        _log(f"{self.descartes} lineas descartadas (cola llena)")
                        Huecos.marca("cola_llena", _ahora_ms(), motivo=f"descartes_acumulados={self.descartes}")
                        desc_log = self.descartes
            except Exception as e:
                self.errores += 1
                if not self.fallando:
                    self.fallando = True
                    Huecos.marca("escritor_fallo", _ahora_ms(), motivo=f"{type(e).__name__}: {e}; lineas_sin_volcar_posible_perdida={self.sin_volcar}")
                if time.time() - t_err_log > 30:
                    _log(f"escritor: {type(e).__name__}: {e} (linea retenida; cola={self.q.qsize()}); reintenta cada 1 s con fichero nuevo")
                    t_err_log = time.time()
                self._cerrar(f)                  # fichero en estado dudoso: no se reutiliza
                f = None
                self.sin_volcar = 0
                if self._parar.is_set():                 # al parar, hasta 10 s de reintentos y se abandona (se dice cuanto se pierde)
                    t_parar_fallo = t_parar_fallo or time.time()
                    if time.time() - t_parar_fallo > 10:
                        _log(f"escritor: abandono al parar tras reintentos fallidos; sin escribir: {self.q.qsize() + (1 if pendiente else 0)} lineas")
                        Huecos.marca("escritor_abandono", _ahora_ms(), motivo=f"lineas_sin_escribir={self.q.qsize() + (1 if pendiente else 0)}")
                        break
                time.sleep(1.0)
        self._cerrar(f)


class Huecos:
    """binance_huecos_<dia>.csv: marcas de eventos (UNA fila por evento). Tambien las escribe el hijo de reserva de libro_estado_ws (mismo formato, O_APPEND)."""
    _lk = threading.Lock()

    @classmethod
    def marca(cls, evento, t_ms, conn_id="", motivo=""):
        try:
            with cls._lk:
                DIR.mkdir(parents=True, exist_ok=True)
                ruta = DIR / f"binance_huecos_{_dia(t_ms / 1000)}.csv"
                nuevo = not ruta.exists()
                with open(ruta, "a", encoding="utf-8") as fh:
                    if nuevo:
                        fh.write("evento,t_ms,conn_id,pid,motivo\n")
                    fh.write(f"{evento},{t_ms},{conn_id},{PID},{str(motivo).replace(',', ';').replace(chr(10), ' ')}\n")
        except Exception as e:
            _log(f"huecos: {type(e).__name__}: {e}")



class Integridad:
    """binance_integridad_<dia>.csv: 1 fila por minuto y simbolo. aggTradeId (campo `a` de aggTrade) es contiguo por simbolo: faltantes = saltos del id respecto del anterior."""
    COLS = "min_utc,sym,conn_id,n_x,a_min,a_max,distintos,dup,fuera_orden,faltantes,n_b,u_min,u_max,recvE_p50,recvE_p90,recvE_p99"

    def __init__(self):
        self.min_actual = None
        self.m = {}
        self.ult_a = {}      # simbolo -> ultimo aggTradeId (global: salto entre minutos y conexiones cuenta)
        self.ult_u = {}

    def _nuevo(self):
        return dict(n_x=0, ids=set(), a_min=None, a_max=None, dup=0, fo=0, falt=0, n_b=0, u_min=None, u_max=None, lat=[])

    def x(self, minuto, sym, a, lat_ms, conn_id):
        self._rot(minuto)
        s = self.m.setdefault(sym, self._nuevo())
        s["n_x"] += 1
        s["conn"] = conn_id
        if lat_ms is not None:
            s["lat"].append(lat_ms)
        if a is None:
            return
        if a in s["ids"]:
            s["dup"] += 1
        s["ids"].add(a)
        s["a_min"] = a if s["a_min"] is None else min(s["a_min"], a)
        s["a_max"] = a if s["a_max"] is None else max(s["a_max"], a)
        ult = self.ult_a.get(sym)
        if ult is not None:
            if a < ult:
                s["fo"] += 1
            elif a > ult + 1:
                s["falt"] += a - ult - 1
        self.ult_a[sym] = a if ult is None else max(ult, a)

    def b(self, minuto, sym, u, conn_id):
        self._rot(minuto)
        s = self.m.setdefault(sym, self._nuevo())
        s["n_b"] += 1
        s["conn"] = conn_id
        if u is not None:
            s["u_min"] = u if s["u_min"] is None else min(s["u_min"], u)
            s["u_max"] = u if s["u_max"] is None else max(s["u_max"], u)

    def _rot(self, minuto):
        if self.min_actual is None:
            self.min_actual = minuto
        elif minuto > self.min_actual:
            self.volcar()
            self.min_actual = minuto

    def volcar(self):
        if self.min_actual is None or not self.m:
            self.m = {}
            return
        try:
            DIR.mkdir(parents=True, exist_ok=True)
            ruta = DIR / f"binance_integridad_{_dia(self.min_actual * 60)}.csv"
            nuevo = not ruta.exists()
            mm = time.strftime("%Y-%m-%dT%H:%MZ", time.gmtime(self.min_actual * 60))
            with open(ruta, "a", encoding="utf-8") as fh:
                if nuevo:
                    fh.write(self.COLS + "\n")
                for sym, s in sorted(self.m.items()):
                    fh.write(f"{mm},{sym},{s.get('conn', '')},{s['n_x']},{s['a_min'] if s['a_min'] is not None else ''},{s['a_max'] if s['a_max'] is not None else ''},"
                             f"{len(s['ids'])},{s['dup']},{s['fo']},{s['falt']},{s['n_b']},{s['u_min'] if s['u_min'] is not None else ''},{s['u_max'] if s['u_max'] is not None else ''},"
                             f"{_pct(s['lat'], .5)},{_pct(s['lat'], .9)},{_pct(s['lat'], .99)}\n")
        except Exception as e:
            _log(f"integridad: {type(e).__name__}: {e}")
        self.m = {}


def limpiar_hermanos():
    """Retencion propia de los ficheros hermanos (60 d)."""
    try:
        corte = time.time() - RETENCION_HERMANOS_D * 86400
        for pat in ("binance_integridad_*.csv", "binance_huecos_*.csv"):
            for p in DIR.glob(pat):
                try:
                    d = datetime.strptime(p.stem.rsplit("_", 1)[1], "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp()
                except ValueError:
                    continue
                if d < corte:
                    p.unlink()
    except Exception as e:
        _log(f"limpieza hermanos: {type(e).__name__}: {e}")


class Estado:
    def __init__(self):
        self.estado = "arrancando"
        self.conn_id = 0
        self.ult_recv = 0
        self.ult_T = 0
        self.msgs_min = 0
        self.t_min = time.time()
        self.filas_min = 0
        self.tiene_lock = False
        self.desde = _ahora_ms()
        self.escritor = None
        self.ignorados = 0
        self.oom_adj = _oom_adj()

    def escribir(self):
        esc = self.escritor
        try:
            _atomic(ESTADO_PATH, json.dumps(dict(ts=_ahora_ms(), pid=PID, estado=self.estado, centinela=CENTINELA.exists(), lock=self.tiene_lock, conn_id=self.conn_id,
                                                  ultimo_recv_ms=self.ult_recv, ultimo_T_ms=self.ult_T, filas_min=self.filas_min, descartes=(esc.descartes if esc else 0),
                                                  filas_total=(esc.filas if esc else 0), cola=(esc.q.qsize() if esc else 0), escritor_fallando=(esc.fallando if esc else False),
                                                  escritor_errores=(esc.errores if esc else 0), ignorados=self.ignorados, oom_adj=self.oom_adj, desde_ms=self.desde)))
        except Exception as e:
            _log(f"estado: {type(e).__name__}: {e}")


ST = Estado()
_PARAR = False
_EV = None          # asyncio.Event de parada (se crea en principal)


def tomar_lock():
    """flock exclusivo no bloqueante. -> fd o None. El kernel lo libera al morir el proceso."""
    DIR.mkdir(parents=True, exist_ok=True)
    fd = os.open(str(LOCK_PATH), os.O_CREAT | os.O_RDWR, 0o644)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        os.ftruncate(fd, 0)
        os.write(fd, f"bnreg pid={PID}\n".encode())
        return fd
    except OSError:
        os.close(fd)
        return None


async def espera(segundos):
    """Sueño interrumpible por la señal de parada."""
    if _EV is None:
        await asyncio.sleep(segundos)
        return
    try:
        await asyncio.wait_for(_EV.wait(), segundos)
    except asyncio.TimeoutError:
        pass


def procesar_mensaje(raw):
    """-> dict `data` o None (no JSON / sin dict): se IGNORA y se cuenta, nunca cierra la conexion."""
    try:
        d = json.loads(raw).get("data")
    except Exception:
        d = None
    if not isinstance(d, dict):
        ST.ignorados += 1
        return None
    return d


async def sesion(esc, integ, ult_bt):
    """Una conexion al WS de Binance. -> (motivo, duracion_s, mensajes_recibidos). Cierra si: silencio de la union > SILENCIO_S (de CUALQUIER mensaje), centinela borrado, parada."""
    ST.conn_id += 1
    cid = ST.conn_id
    t_con = time.time()
    motivo = "cierre_normal"
    nmsg = 0
    async with websockets.connect(BINANCE_WS, ping_interval=20, ping_timeout=20, max_queue=None) as ws:
        t_con = time.time()
        _log(f"conectado a Binance spot (conn {cid}): bookTicker + aggTrade")
        Huecos.marca("conexion", _ahora_ms(), cid)
        ST.estado = "activo"
        ult = [time.time()]
        razon = [None]

        async def vigilar():
            while True:
                await asyncio.sleep(0.5)
                if _PARAR:
                    razon[0] = "parada"
                elif not CENTINELA.exists():
                    razon[0] = "centinela_borrado"
                elif time.time() - ult[0] > SILENCIO_S:
                    razon[0] = "silencio_union_%ds" % int(SILENCIO_S)
                if razon[0]:
                    await ws.close()
                    return

        vig = asyncio.create_task(vigilar())
        try:
            async for raw in ws:
                t_ms = _ahora_ms()
                ult[0] = time.time()
                nmsg += 1
                d = procesar_mensaje(raw)
                if d is None:
                    continue
                minuto = t_ms // 60000
                ST.ult_recv = t_ms
                if d.get("e") == "aggTrade":
                    a = d.get("a")
                    E = d.get("E")
                    esc.put(f"x,{d.get('T')},{d.get('s')},{d.get('p')},{d.get('q')},{int(bool(d.get('m')))},{E},{t_ms}\n")
                    ST.ult_T = d.get("T") or ST.ult_T
                    integ.x(minuto, d.get("s"), a, (t_ms - E) if isinstance(E, int) else None, cid)
                    ST.msgs_min += 1
                    continue
                s, b, a_ = d.get("s"), d.get("b"), d.get("a")
                if s and b and a_:
                    integ.b(minuto, s, d.get("u"), cid)
                    if ult_bt.get(s) != (b, a_):
                        ult_bt[s] = (b, a_)
                        esc.put(f"b,{t_ms},{s},{b},{a_},{d.get('B')},{d.get('A')},\n")
                    ST.msgs_min += 1
        except websockets.ConnectionClosed as e:
            motivo = f"ConnectionClosed {getattr(e, 'code', '')}"
        finally:
            vig.cancel()
    if razon[0]:
        motivo = razon[0]
    return motivo, time.time() - t_con, nmsg


async def tarea_latido(integ):
    """Cada 2 s: estado.json (latido; el traspaso, el vigia y el hijo de reserva lo leen). Cada >=10 s recalcula filas_min; al cambiar de minuto vuelca la integridad (aunque no lleguen mensajes)."""
    while True:
        t = time.time()
        if t - ST.t_min >= 10:
            ST.filas_min = int(ST.msgs_min * 60 / max(1.0, t - ST.t_min))
            ST.msgs_min, ST.t_min = 0, t
        if integ.min_actual is not None and int(t // 60) > integ.min_actual:
            integ.volcar()
            integ.min_actual = None
        ST.escribir()
        await asyncio.sleep(2)


def _marca_caida_previa():
    """Si el latido del proceso anterior no termino en parado/ocioso (SIGKILL, OOM, fallo), marca `caida_proceso` con t_ms = ULTIMO latido: es el inicio real del hueco."""
    try:
        e = json.loads(ESTADO_PATH.read_text())
        if e.get("pid") != PID and e.get("estado") not in ("parado", "ocioso", "salida") and e.get("lock"):
            Huecos.marca("caida_proceso", int(e["ts"]), e.get("conn_id", ""), f"pid_previo={e.get('pid')}; detectada_en={_ahora_ms()}")
    except Exception:
        pass


async def principal():
    global _PARAR, _EV
    loop = asyncio.get_running_loop()
    _EV = asyncio.Event()

    def _senal():
        globals().__setitem__("_PARAR", True)
        _EV.set()
    for sg in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP):
        loop.add_signal_handler(sg, _senal)
    try:
        if os.getpriority(os.PRIO_PROCESS, 0) > -10:
            os.setpriority(os.PRIO_PROCESS, 0, -10)   # como el hijo de libro_estado_ws: mejora el sello->recepcion
    except OSError as e:
        _log(f"no se pudo subir la prioridad: {e}")
    limpiar_hermanos()
    _marca_caida_previa()
    Huecos.marca("arranque", _ahora_ms(), motivo=f"proceso bnreg; oom_adj={ST.oom_adj}")
    integ = Integridad()
    ult_bt = {}
    lat = asyncio.create_task(tarea_latido(integ))
    fd = None
    esc = None
    backoff, sin_msgs_acum = 1.0, 0.0
    salida2 = False
    dia_hermanos = _dia()
    try:
        while not _PARAR:
            if _dia() != dia_hermanos:
                dia_hermanos = _dia()
                limpiar_hermanos()
            if not CENTINELA.exists():              # OCIOSO: ni lock ni conexion ni fichero
                if fd is not None or esc is not None:
                    _log("centinela borrado: suelto el lock y paro el escritor")
                    Huecos.marca("parada_centinela", _ahora_ms())
                    if esc:
                        esc.parar()
                        esc = None
                        ST.escritor = None
                    if fd is not None:
                        os.close(fd)
                        fd = None
                    ST.tiene_lock = False
                ST.estado = "ocioso"
                await espera(1.0)
                continue
            if fd is None:
                fd = tomar_lock()
                if fd is None:
                    ST.estado = "espera_lock"
                    ST.tiene_lock = False
                    await espera(1.0)
                    continue
                ST.tiene_lock = True
                _log("lock tomado: este proceso es el escritor de Binance")
                Huecos.marca("lock_tomado", _ahora_ms())
                esc = Escritor()
                ST.escritor = esc
                backoff, sin_msgs_acum = 1.0, 0.0
            try:
                motivo, dur, nmsg = await sesion(esc, integ, ult_bt)
            except Exception as e:
                motivo, dur, nmsg = f"{type(e).__name__}: {e}", 0.0, 0
            t_ms = _ahora_ms()
            if nmsg > 0:                                    # llegaron mensajes: el reloj de "sin datos" y el backoff se reinician
                backoff, sin_msgs_acum = 1.0, 0.0
            else:
                sin_msgs_acum += dur                        # solo tiempo CONECTADO sin mensajes (un fallo de conexion tiene dur=0)
            if motivo not in ("centinela_borrado", "parada"):
                Huecos.marca("caida", t_ms, ST.conn_id, motivo)
            if sin_msgs_acum >= SIN_DATOS_SALIR_S:
                _log(f"{SIN_DATOS_SALIR_S:.0f} s conectado sin recibir mensajes: salgo (el watchdog relanza la screen)")
                Huecos.marca("salida_sin_datos", _ahora_ms(), ST.conn_id)
                ST.estado = "salida"
                salida2 = True
                break
            if motivo in ("centinela_borrado", "parada"):
                _log(f"conexion cerrada ({motivo}) tras {dur:.1f} s")
                continue
            espera_s = backoff
            _log(f"conexion cerrada ({motivo}) tras {dur:.1f} s, {nmsg} mensajes; reconecta en {espera_s:.0f} s")
            ST.estado = "reconectando"
            await espera(espera_s)
            if nmsg == 0:
                backoff = min(BACKOFF_MAX_S, backoff * 2)
    finally:
        lat.cancel()
        integ.volcar()
        Huecos.marca("parada", _ahora_ms(), ST.conn_id, "sin_datos" if salida2 else ("senal" if _PARAR else "fin"))
        if esc:
            esc.parar()
        if not salida2:
            ST.estado = "parado"
        ST.tiene_lock = False
        ST.escribir()
        if fd is not None:
            os.close(fd)
    if salida2:
        sys.exit(2)


if __name__ == "__main__":
    _log(f"arrancado (pid {PID}); dir={DIR}; oom_score_adj={ST.oom_adj}; centinela={'presente' if CENTINELA.exists() else 'AUSENTE (ocioso)'}")
    asyncio.run(principal())
