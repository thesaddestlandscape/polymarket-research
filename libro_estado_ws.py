#!/usr/bin/env python3
"""libro_estado_ws.py -- estado del libro L2 en memoria por token, mantenido
por WebSocket del CLOB (canal market) con histórico corto de imbalance/mejor
bid-ask con TIMESTAMP EN MS, para poder preguntar "¿cómo estaba el libro en
el instante T?" (29-Sep, principio Javi: micro-latencia/detección rápida).

Motivo: gbm_late_imbalance_fase0 medía el libro por REST ~0,5-22 s DESPUÉS
de la señal (ciclo de predictions ~100 s + poll); aquí el libro se conoce en
todo momento y se consulta en el ms exacto de la señal.

Uso (desde otro módulo, mismo proceso):
    import libro_estado_ws as LE
    LE.iniciar(filtro_marcos=("15min",))          # idempotente
    LE.en(token_id, t_ms)  -> dict|None           # último estado con t<=t_ms
Solo lectura, sin órdenes. Universo = mercados abiertos de los marcos pedidos
(fetch_libro_ambos_lados._universo_activo), refrescado cada 30 s con
suscripciones incrementales (sin reconectar, sin huecos).

02-Oct, LECTOR EN PROCESO SEPARADO (OK Javi): dentro de la screen `observadores` (~60 hilos, nice 10, máquina a
load 8-11) el hilo que leía el socket se quedaba sin turno y el servidor cortaba (1013 "slow consumer" / ping
vencido): ~85 caídas/h, ~10 s de hueco cada una. Subir el hilo a nice 0 lo dejó en ~27/h; un lector aislado no cae
nunca. Ahora:
  - HIJO (`python libro_estado_ws.py --hijo`, nice 0, solo stdlib + websockets): lee el socket, parsea, mantiene el
    libro L2, muestrea cada MUESTREO_MS y manda lotes de registros compactos por stdout (tramas longitud+pickle).
    Un hilo emisor desacopla el envío: el socket se lee siempre aunque el padre vaya lento. Logs por stderr.
  - PADRE (este módulo importado): calcula el universo (REST) y los tokens on-demand (pedir) y se los manda al hijo
    por stdin; un hilo lector aplica los lotes a _HIST/_TOP/_TRADES. La API pública no cambia.
  - Si el padre muere, el hijo ve EOF en stdin y sale. Si el hijo muere, el padre lo relanza en 2 s.
  Se usa subprocess y no multiprocessing: spawn/forkserver reimportarían el __main__ del padre (observadores_fase0
  con ~100 módulos).
"""
import asyncio
import gzip
import queue
import collections
import json
import os
import pickle
import struct
import subprocess
import sys
import threading
import time
from bisect import bisect_right
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

WS_URL = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
REFRESCO_S = 30
HIST_MAX = 3000            # eventos por token (>= varios minutos a ritmo alto)
RECV_TIMEOUT_S = 0.25      # corto: las altas on-demand (pedir) se atienden en <=0,25 s
MUESTREO_MS = 100
SUB_TROZO, SUB_PAUSA_S = 20, 0.25   # alta de tokens en trozos (ver _una_sesion)
LOTE_S = 0.02              # el hijo agrupa registros y los manda cada 20 ms
# 05-Oct (Javi: hacer explotable el hueco Binance -> Polymarket como MAKER que cancela antes que el tomador retrasado
# 150 ms): registro de día completo en ms para simularlo. Lo escribe el HIJO (CPU propia, cero conexiones nuevas al
# CLOB): h = top del libro (hora del exchange, muestreo MUESTREO_MS), t = TODAS las operaciones, b = mid de Binance
# por hora de RECEPCIÓN (bookTicker spot no trae hora de evento; es el reloj con el que cancelaríamos), k = mapa
# token -> moneda/marco/mercado/cierre/lado. gz diario fuera de git, retención en comprimir_data_historica.sh.
REGISTRO_MS_DIR = Path(os.environ.get("LIBRO_WS_REGISTRO_DIR", "/root/polymarket-research-datalogs"))
# 05-Oct noche (misión "monetizar la ventana Binance -> Polymarket"): además del bookTicker (sin hora de evento),
# aggTrade trae T (hora de la operación) y E (hora del evento) del exchange -> t0 real y latencia de red por evento.
# x = aggTrade (T, símbolo, precio, cantidad, comprador_es_maker, E, recepción); q = top de Polymarket SIN muestrear
# (cada cambio de PRECIO del mejor bid/ask, con sus tamaños, hora del exchange): t1/t2 al ms. El top muestreado (h) se mantiene.
_SIMB_BN = ("btcusdt", "ethusdt", "solusdt", "xrpusdt", "dogeusdt", "bnbusdt")
BINANCE_WS = "wss://stream.binance.com:9443/stream?streams=" + "/".join(
    [f"{s}@bookTicker" for s in _SIMB_BN] + [f"{s}@aggTrade" for s in _SIMB_BN])

_LIB = {}                  # (hijo) token -> {"bids": {p: s}, "asks": {p: s}}
_ULT = {}                  # (hijo) token -> t_ms del último registro (muestreo mínimo entre registros)
_TOPQ = {}                 # (hijo) token -> último top registrado sin muestrear (registro q)
_HIST = {}                 # token -> deque[(t_ms, bb, ba, i1, i5, i10, dask5, bid_size, ask_size)]
_LOCK = threading.Lock()
_EXTRA = {}                # token -> expiración (epoch s): tokens pedidos on-demand por otros módulos (suscripción inmediata)
_TRADES = {}               # token -> deque[(t_ms, price, side, size)] de last_trade_price (29-Sep, requote/maker sim)
_MARCOS = {}               # marco -> conjunto de activos permitidos (None = todos); unión de todos los llamantes
_TOP = {}                  # token -> (t_ms, best_bid, bid_size, best_ask, ask_size): último estado O(1) (detectores de alta frecuencia)
_ESTADO = {"iniciado": False, "n_tokens": 0, "n_eventos": 0, "ultimo_evento_ms": 0, "reinicios_hijo": 0}
_ES_HIJO = False


def _log(msg):
    # en el hijo stdout es el canal de datos: los logs van SIEMPRE a stderr (mismo fichero de log de la screen)
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] [libro_estado_ws] {msg}",
          file=sys.stderr if _ES_HIJO else sys.stdout, flush=True)


def _trama(obj):
    b = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
    return struct.pack("<I", len(b)) + b


def _leer_trama(f):
    cab = f.read(4)
    if len(cab) < 4:
        return None
    n = struct.unpack("<I", cab)[0]
    b = f.read(n)
    if len(b) < n:
        return None
    return pickle.loads(b)


def subir_prioridad_hilo():
    """02-Oct: los procesos de observación corren con nice 10 y, con la máquina a load 8-11 en 4 cores, un hilo que
    lee un socket se queda sin turno. Solo SUBE la prioridad del hilo que llama a 0 (nunca la baja si ya está a 0 o
    negativa); sin permisos, no hace nada. Lo usa binance_jump_leadlag (y el hijo de este módulo)."""
    try:
        tid = threading.get_native_id()
        if os.getpriority(os.PRIO_PROCESS, tid) > 0:
            os.setpriority(os.PRIO_PROCESS, tid, 0)
    except (OSError, AttributeError) as e:
        _log(f"no se pudo subir la prioridad del hilo: {e}")


# ----------------------------------------------------------------------------------------------- API (padre)

def en(token, t_ms):
    """Último estado del libro con timestamp <= t_ms: dict con edad_ms respecto a t_ms, o None."""
    with _LOCK:
        h = _HIST.get(token)
        if not h:
            return None
        arr = list(h)
    i = bisect_right([x[0] for x in arr], t_ms) - 1
    if i < 0:
        return None
    t, bb, ba, i1, i5, i10, d5, bbs, bas = arr[i]
    return {"t_ms": t, "edad_ms": t_ms - t, "best_bid": bb, "best_ask": ba, "imb1": i1, "imb5": i5, "imb10": i10,
            "depth_ask5_usd": d5, "bid_size": bbs, "ask_size": bas}


def pedir(tokens, ttl_s=900):
    """Pide seguimiento ms de tokens arbitrarios (p.ej. mercado de un evento recién detectado). Se suscribe en
    <=~0,3 s y se da de baja solo al expirar. Idempotente."""
    exp = time.time() + ttl_s
    nuevos = False
    for t in tokens:
        if t:
            nuevos |= t not in _EXTRA or _EXTRA[t] <= time.time()
            _EXTRA[t] = max(_EXTRA.get(t, 0), exp)
    if nuevos:
        _enviar_deseados()


def trades(token, t0_ms, t1_ms):
    with _LOCK:
        d = list(_TRADES.get(token, ()))
    return [x for x in d if t0_ms <= x[0] <= t1_ms]


def hist_rango(token, t0_ms, t1_ms):
    with _LOCK:
        h = list(_HIST.get(token, ()))
    return [x for x in h if t0_ms <= x[0] <= t1_ms]


def ultimo(token):
    """(t_ms, best_bid, bid_size, best_ask, ask_size) más reciente del token, O(1). None si sin datos."""
    return _TOP.get(token)


def estado():
    return dict(_ESTADO)


# ----------------------------------------------------------------------------------------------- padre

_HIJO = {"proc": None, "lock": threading.Lock()}
_UNIVERSO = {"toks": None, "claves": {}, "meta": {}}


def _tokens_universo(filtro_marcos=None):
    import live_trade as lt
    from fetch_libro_ambos_lados import _universo_activo
    out, claves, meta = [], {}, {}
    for mid, (activo, marco, _cid, _edt) in _universo_activo().items():
        permitidos = _MARCOS.get(marco, "no")
        if permitidos == "no" or (permitidos is not None and activo not in permitidos):
            continue
        try:
            yes, no, _ = lt._get_token_ids(mid)
        except Exception:
            continue
        out += [t for t in (yes, no) if t]
        for t, lado in ((yes, "YES"), (no, "NO")):
            if t:
                claves[t] = f"{activo}#{marco}"
                meta[t] = (activo, marco, str(mid), str(_edt), lado)
    _UNIVERSO["claves"], _UNIVERSO["meta"] = claves, meta
    return out


def _enviar_deseados():
    """Manda al hijo el conjunto completo deseado (universo + on-demand vigentes; los on-demand primero)."""
    ahora = time.time()
    extra = [t for t, e in list(_EXTRA.items()) if e > ahora]
    univ = _UNIVERSO["toks"]
    if univ is None:
        return                                   # sin universo aún: se mandará en cuanto exista
    with _HIJO["lock"]:
        p = _HIJO["proc"]
        if p is None or p.poll() is not None:
            return
        try:
            p.stdin.write(_trama(("tokens", list(univ), extra, dict(_UNIVERSO["claves"]), dict(_UNIVERSO["meta"]))))
            p.stdin.flush()
        except (BrokenPipeError, OSError, ValueError):
            pass


def _podar(vivos):
    """Fuga del 30-Sep: tokens que ya no están en el universo ni pedidos se tiran del histórico (3.000 muestras/token)."""
    with _LOCK:
        for d in (_HIST, _TRADES, _TOP):
            for t in [t for t in d if t not in vivos]:
                d.pop(t, None)


def _hilo_universo():
    while True:
        try:
            toks = _tokens_universo()
            ahora = time.time()
            for t in [t for t, e in list(_EXTRA.items()) if e <= ahora]:
                _EXTRA.pop(t, None)
            _UNIVERSO["toks"] = toks
            _ESTADO["n_tokens"] = len(set(toks) | set(_EXTRA))
            _podar(set(toks) | set(_EXTRA))
            _enviar_deseados()
        except Exception as e:
            _log(f"refresco de universo falló: {type(e).__name__}: {e}")
        time.sleep(REFRESCO_S)


def _hilo_lector(proc):
    """Aplica los lotes del hijo. Si el padre va lento, los lotes esperan en la tubería / el emisor del hijo, nunca
    en el socket: el servidor no ve un consumidor lento."""
    f = proc.stdout
    while True:
        try:
            lote = _leer_trama(f)
        except Exception as e:
            _log(f"lector del hijo: {type(e).__name__}: {e}")
            lote = None
        if lote is None:
            return                                   # EOF: el hijo murió (el supervisor lo relanza)
        ult = None
        with _LOCK:
            for tipo, tk, rec in lote:
                if tipo == "h":
                    _HIST.setdefault(tk, deque(maxlen=HIST_MAX)).append(rec)
                    _TOP[tk] = (rec[0], rec[1], rec[7], rec[2], rec[8])
                    ult = rec[0]
                    _ESTADO["n_eventos"] += 1
                elif tipo == "t":
                    _TRADES.setdefault(tk, deque(maxlen=500)).append(rec)
        if ult is not None:
            _ESTADO["ultimo_evento_ms"] = ult


def _supervisor():
    while True:
        try:
            proc = subprocess.Popen([sys.executable, "-u", str(Path(__file__).resolve()), "--hijo"],
                                    stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=None, cwd=str(REPO))
        except Exception as e:
            _log(f"no se pudo lanzar el lector hijo: {type(e).__name__}: {e}; reintento en 5 s")
            time.sleep(5)
            continue
        with _HIJO["lock"]:
            _HIJO["proc"] = proc
        _log(f"lector hijo lanzado (pid {proc.pid})")
        _enviar_deseados()
        lector = threading.Thread(target=_hilo_lector, args=(proc,), daemon=True, name="libro_ws_lector")
        lector.start()
        proc.wait()
        lector.join(timeout=5)
        _ESTADO["reinicios_hijo"] += 1
        _log(f"lector hijo terminó (rc {proc.returncode}); relanzo en 2 s")
        time.sleep(2)


def iniciar(filtro_marcos=("15min",), activos=None):
    """Idempotente y ACUMULATIVO: cada llamante añade sus marcos (activos=None -> todos)."""
    for m in filtro_marcos:
        if m in _MARCOS and _MARCOS[m] is None:
            continue
        if activos is None:
            _MARCOS[m] = None
        else:
            _MARCOS[m] = set(_MARCOS.get(m) or ()) | set(activos)
    if _ESTADO["iniciado"]:
        return
    _ESTADO["iniciado"] = True
    threading.Thread(target=_supervisor, daemon=True, name="libro_estado_ws").start()
    threading.Thread(target=_hilo_universo, daemon=True, name="libro_ws_universo").start()


# ----------------------------------------------------------------------------------------------- hijo

def _imb(bids, asks, n):
    sb = sum(s for _, s in bids[:n])
    sa = sum(s for _, s in asks[:n])
    t = sb + sa
    return round((sb - sa) / t, 4) if t > 0 else None


def _registrar(token, t_ms, salida):
    L = _LIB.get(token)
    if L is None:
        return
    bids = sorted(((p, s) for p, s in L["bids"].items() if s > 0), reverse=True)
    asks = sorted((p, s) for p, s in L["asks"].items() if s > 0)
    bb = bids[0][0] if bids else None
    ba = asks[0][0] if asks else None
    dask5 = round(sum(p * s for p, s in asks[:5]), 2)
    salida.append(("h", token, (t_ms, bb, ba, _imb(bids, asks, 1), _imb(bids, asks, 5), _imb(bids, asks, 10), dask5,
                                bids[0][1] if bids else None, asks[0][1] if asks else None)))


def _aplicar(msg, salida):
    t_ev = int(msg.get("timestamp") or time.time() * 1000)
    if msg.get("event_type") == "last_trade_price":
        tk = msg.get("asset_id")
        if tk in _LIB:
            try:
                salida.append(("t", tk, (t_ev, float(msg["price"]), msg.get("side"), float(msg.get("size") or 0))))
            except (KeyError, TypeError, ValueError):
                pass
        return
    if "price_changes" in msg:
        tocados = set()
        for pc in msg["price_changes"]:
            tk = pc.get("asset_id")
            L = _LIB.get(tk)
            if L is None:
                continue
            try:
                p, s = float(pc["price"]), float(pc.get("size") or 0)
            except (KeyError, TypeError, ValueError):
                continue
            lado = "bids" if pc.get("side") == "BUY" else "asks"
            if s <= 0:
                L[lado].pop(p, None)
            else:
                L[lado][p] = s
            tocados.add(tk)
        if _REGISTRO is not None:
            for tk in tocados:
                L = _LIB[tk]
                bb = max((p for p, s in L["bids"].items() if s > 0), default=None)
                ba = min((p for p, s in L["asks"].items() if s > 0), default=None)
                top = (bb, ba, L["bids"].get(bb) if bb is not None else None, L["asks"].get(ba) if ba is not None else None)
                if _TOPQ.get(tk) != top[:2]:            # solo cambios de PRECIO del top (con tamaños: ~1 GB/día)
                    _TOPQ[tk] = top[:2]
                    _REGISTRO.put(f"q,{t_ev},{tk},{top[0]},{top[1]},{top[2]},{top[3]},\n")
        for tk in tocados:
            if t_ev - _ULT.get(tk, 0) >= MUESTREO_MS:   # el libro se actualiza siempre; se muestrea el histórico
                _ULT[tk] = t_ev
                _registrar(tk, t_ev, salida)
    elif "asset_id" in msg and ("bids" in msg or "asks" in msg):
        tk = msg["asset_id"]
        _LIB[tk] = {"bids": {float(b["price"]): float(b["size"]) for b in (msg.get("bids") or [])},
                    "asks": {float(a["price"]): float(a["size"]) for a in (msg.get("asks") or [])}}
        _ULT[tk] = t_ev
        _registrar(tk, t_ev, salida)


class _Emisor:
    """Cola de salida del hijo + hilo que la vuelca a stdout por lotes. El bucle del socket solo hace append."""

    def __init__(self):
        self.buf = []
        self.cv = threading.Condition()
        threading.Thread(target=self._loop, daemon=True, name="emisor").start()

    def extend(self, recs):
        if recs:
            with self.cv:
                self.buf.extend(recs)
            if _REGISTRO is not None:
                for tipo, tk, r in recs:
                    if tipo == "h":
                        _REGISTRO.put(f"h,{r[0]},{tk},{r[1]},{r[2]},{r[7]},{r[8]},\n")
                    else:
                        _REGISTRO.put(f"t,{r[0]},{tk},{r[1]},{r[2]},{r[3]},,\n")

    def _loop(self):
        out = sys.stdout.buffer
        while True:
            time.sleep(LOTE_S)
            with self.cv:
                lote, self.buf = self.buf, []
            if lote:
                try:
                    out.write(_trama(lote))
                    out.flush()
                except (BrokenPipeError, OSError):
                    os._exit(0)                     # el padre murió


class _Registro:
    """Hijo: escribe h/t/b/k a REGISTRO_MS_DIR/maker_ms_YYYY-MM-DD_<pid>.csv.gz: un fichero por arranque y día (un
    corte brusco deja truncado el final del gzip; si se siguiera añadiendo al mismo fichero, lo posterior sería
    ilegible). Los lectores leen todos los del día y toleran el final truncado (vuelco cada 5 s).
    Hilo propio con cola acotada: si el disco va lento se DESCARTA (y se cuenta), nunca se frena la lectura del socket."""

    def __init__(self):
        self.q = queue.Queue(maxsize=200000)
        self.descartes = 0
        self.vistos = set()
        threading.Thread(target=self._loop, daemon=True, name="registro_ms").start()

    def put(self, linea):
        try:
            self.q.put_nowait(linea)
        except queue.Full:
            self.descartes += 1

    def meta(self, meta):
        for t, (a, m, mid, fin, lado) in meta.items():
            if t not in self.vistos:
                self.vistos.add(t)
                self.put(f"k,{int(time.time() * 1000)},{t},{a},{m},{mid},{fin},{lado}\n")

    def _loop(self):
        dia, f, t_flush, desc_log = None, None, time.time(), 0
        while True:
            try:
                linea = self.q.get(timeout=1.0)
            except queue.Empty:
                linea = None
            hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            try:
                if hoy != dia:
                    if f:
                        f.close()
                    dia = hoy
                    ruta = REGISTRO_MS_DIR / f"maker_ms_{hoy}_{os.getpid()}.csv.gz"
                    f = gzip.open(ruta, "wt", encoding="utf-8", compresslevel=5)
                    f.write("tipo,t_ms,id,c1,c2,c3,c4,c5\n")
                    self.vistos = set()        # el mapa k se repite en el fichero de cada día
                if linea:
                    f.write(linea)
                if time.time() - t_flush > 5:
                    f.flush()
                    t_flush = time.time()
                    if self.descartes != desc_log:
                        _log(f"registro_ms: {self.descartes} líneas descartadas (cola llena)")
                        desc_log = self.descartes
            except Exception as e:
                _log(f"registro_ms: {type(e).__name__}: {e}")
                time.sleep(5)


_REGISTRO = None
_DESEADOS = {"univ": [], "extra": [], "claves": {}, "ver": 0}
_DES_LOCK = threading.Lock()


def _hilo_stdin():
    f = sys.stdin.buffer
    while True:
        try:
            m = _leer_trama(f)
        except Exception:
            m = None
        if m is None:
            os._exit(0)                             # EOF: el padre murió o cerró -> el hijo sale
        if m[0] == "tokens":
            with _DES_LOCK:
                _DESEADOS["univ"], _DESEADOS["extra"] = m[1], m[2]
                _DESEADOS["claves"] = m[3] if len(m) > 3 else {}
                if len(m) > 4:
                    _REGISTRO.meta(m[4])
                _DESEADOS["ver"] += 1


# 05-Oct: UNA conexión por moneda#marco (+ "extra" para on-demand fuera del universo). Medido aislado (10 min, mismos
# tokens, a la vez): 1 conexión ~13 caídas 1013 y ~40 % menos mensajes recibidos; 3/6 conexiones por hash de token
# 10-12 caídas (los mercados en ventana viva -- ~10 mercados = 90 % de los price_changes -- caen juntos en un mismo
# trozo); 4 grupos por peso 4 caídas; 15 conexiones por moneda#marco 0 caídas y flujo completo. El límite es el buffer
# de envío del servidor POR CONEXIÓN, no nuestra lectura (Recv-Q ~0, RTT ~1,5 ms).
_GRUPOS = {}               # (hijo) grupo -> lista ordenada de tokens deseados (on-demand primero)
_GRUPOS_VER = {}           # (hijo) grupo -> versión (cambia cuando cambia su conjunto)


def _calcular_grupos():
    with _DES_LOCK:
        ver, univ, extra, claves = (_DESEADOS["ver"], list(_DESEADOS["univ"]), list(_DESEADOS["extra"]),
                                    dict(_DESEADOS["claves"]))
    grupos = {}
    for t in dict.fromkeys(extra + univ):            # on-demand por delante dentro de su grupo
        grupos.setdefault(claves.get(t, "extra"), []).append(t)
    return ver, grupos


def _huerfano(t):
    return not any(t in g for g in _GRUPOS.values())


async def _gestor(emisor):
    # esperar al primer conjunto deseado ANTES de conectar: el servidor cierra con 1008 "no subscribe received" si
    # el socket queda abierto sin suscripción (el padre tarda ~35 s en su primer universo al arrancar observadores)
    ver_vista, tareas = -1, {}
    if _REGISTRO is not None:
        tareas["__binance__"] = asyncio.create_task(_binance_registro())
    while True:
        ver, grupos = _calcular_grupos()
        if ver and ver != ver_vista:
            ver_vista = ver
            for k in list(_GRUPOS):
                if k not in grupos:
                    _GRUPOS.pop(k)
                    _GRUPOS_VER[k] = _GRUPOS_VER.get(k, 0) + 1
            for k, toks in grupos.items():
                if _GRUPOS.get(k) != toks:
                    _GRUPOS[k] = toks
                    _GRUPOS_VER[k] = _GRUPOS_VER.get(k, 0) + 1
            for t in [t for t in _LIB if _huerfano(t)]:
                _LIB.pop(t, None)
                _ULT.pop(t, None)
                _TOPQ.pop(t, None)
        if _REGISTRO is not None and tareas["__binance__"].done():
            tareas["__binance__"] = asyncio.create_task(_binance_registro())
        for k in list(_GRUPOS):
            if k not in tareas or tareas[k].done():
                tareas[k] = asyncio.create_task(_sesion_grupo(k, emisor))
        await asyncio.sleep(0.2)


async def _binance_registro():
    """Mid de Binance (6 monedas) al registro cuando cambia, con hora de RECEPCIÓN en ms."""
    ult = {}
    while True:
        try:
            async with websockets.connect(BINANCE_WS, ping_interval=20, ping_timeout=20, max_queue=None) as ws:
                _log("registro_ms: conectado a Binance bookTicker + aggTrade")
                async for raw in ws:
                    t_ms = int(time.time() * 1000)
                    d = json.loads(raw).get("data") or {}
                    if d.get("e") == "aggTrade":
                        _REGISTRO.put(f"x,{d.get('T')},{d.get('s')},{d.get('p')},{d.get('q')},{int(bool(d.get('m')))},"
                                      f"{d.get('E')},{t_ms}\n")
                        continue
                    s, b, a = d.get("s"), d.get("b"), d.get("a")
                    if s and b and a and ult.get(s) != (b, a):
                        ult[s] = (b, a)
                        _REGISTRO.put(f"b,{t_ms},{s},{b},{a},{d.get('B')},{d.get('A')},\n")
        except Exception as e:
            _log(f"registro_ms: Binance caído: {type(e).__name__}: {e}; reconecta en 2 s")
            await asyncio.sleep(2)


async def _sesion_grupo(k, emisor):
    while k in _GRUPOS:
        try:
            await _una_sesion(k, emisor)
        except Exception as e:
            _log(f"sesión caída [{k}]: {type(e).__name__}: {e}; reconecta en 2 s")
            await asyncio.sleep(2)


async def _una_sesion(k, emisor):
    async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20, open_timeout=10, max_queue=None) as ws:
        toks, ver_aplicada = list(_GRUPOS.get(k, [])), _GRUPOS_VER.get(k)
        if not toks:
            return
        # 30-Sep: suscribir 150+ tokens de golpe hace que el servidor mande todas las fotos del libro en una ráfaga,
        # llene SU buffer de envío y corte con 1013. Se suscribe en trozos de SUB_TROZO, uno cada SUB_PAUSA_S,
        # leyendo el socket entre medias; lo mismo para las altas posteriores.
        cola_sub, t_sub = collections.deque(toks[SUB_TROZO:]), time.time()
        await ws.send(json.dumps({"type": "market", "assets_ids": toks[:SUB_TROZO]}))
        suscritos = set(toks)
        for t in toks:
            _LIB.setdefault(t, {"bids": {}, "asks": {}})
        _log(f"conectado [{k}], {len(toks)} tokens (lector en proceso separado, pid {os.getpid()})")
        while True:
            try:
                raw = await asyncio.wait_for(ws.recv(), RECV_TIMEOUT_S)
            except asyncio.TimeoutError:
                raw = None
            if _GRUPOS_VER.get(k) != ver_aplicada:
                ver_aplicada = _GRUPOS_VER.get(k)
                if k not in _GRUPOS:
                    return                                  # grupo retirado: cerrar la conexión
                deseados = _GRUPOS[k]
                nuevos = [t for t in deseados if t not in suscritos]
                cola_sub.extend(nuevos)
                for t in nuevos:
                    _LIB.setdefault(t, {"bids": {}, "asks": {}})
                suscritos.update(nuevos)
                viejos = [t for t in suscritos if t not in set(deseados)]
                if viejos:
                    await ws.send(json.dumps({"assets_ids": viejos, "operation": "unsubscribe"}))
                    for t in viejos:
                        suscritos.discard(t)
                        if _huerfano(t):
                            _LIB.pop(t, None)
                            _ULT.pop(t, None)
            if cola_sub and time.time() - t_sub >= SUB_PAUSA_S:
                trozo = [cola_sub.popleft() for _ in range(min(SUB_TROZO, len(cola_sub)))]
                trozo = [t for t in trozo if t in suscritos]          # por si se dio de baja mientras esperaba
                if trozo:
                    await ws.send(json.dumps({"assets_ids": trozo, "operation": "subscribe"}))
                t_sub = time.time()
            if not raw:
                continue
            try:
                j = json.loads(raw)
            except Exception:
                continue
            salida = []
            for e in (j if isinstance(j, list) else [j]):
                if isinstance(e, dict):
                    _aplicar(e, salida)
            emisor.extend(salida)


def _main_hijo():
    global _ES_HIJO
    _ES_HIJO = True
    try:
        if os.getpriority(os.PRIO_PROCESS, 0) > 0:
            os.setpriority(os.PRIO_PROCESS, 0, 0)    # el padre corre a nice 10; el lector no
    except OSError as e:
        _log(f"no se pudo subir la prioridad del hijo: {e}")
    global _REGISTRO
    try:
        _REGISTRO = _Registro()
    except Exception as e:
        _log(f"registro_ms desactivado: {type(e).__name__}: {e}")
    emisor = _Emisor()
    threading.Thread(target=_hilo_stdin, daemon=True, name="stdin").start()
    while True:
        try:
            asyncio.run(_gestor(emisor))
        except Exception as e:
            _log(f"sesión caída: {type(e).__name__}: {e}; reconecta en 2 s")
        time.sleep(2)


if __name__ == "__main__":
    if "--hijo" in sys.argv:
        _main_hijo()
    else:
        iniciar(("5min", "15min"))
        while True:
            time.sleep(10)
            print(estado(), flush=True)
