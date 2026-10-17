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
PING_S = 10.0             # PING de texto que exige el canal de mercado del CLOB
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
LIBRO5_DIR = Path(os.environ.get("LIBRO5_DIR", "/mnt/HC_Volume_106538179/libro5_ms"))   # 17-Oct: en el volumen
# 05-Oct noche (misión "monetizar la ventana Binance -> Polymarket"): además del bookTicker (sin hora de evento),
# aggTrade trae T (hora de la operación) y E (hora del evento) del exchange -> t0 real y latencia de red por evento.
# x = aggTrade (T, símbolo, precio, cantidad, comprador_es_maker, E, recepción); q = top de Polymarket SIN muestrear
# (cada cambio de precio o tamaño del mejor bid/ask, hora del exchange + recepción; t también lleva recepción): t1/t2 al ms. El top muestreado (h) se mantiene.
_SIMB_BN = ("btcusdt", "ethusdt", "solusdt", "xrpusdt", "dogeusdt", "bnbusdt")
BINANCE_WS = "wss://stream.binance.com:9443/stream?streams=" + "/".join(
    [f"{s}@bookTicker" for s in _SIMB_BN] + [f"{s}@aggTrade" for s in _SIMB_BN])

_LIB = {}                  # (hijo) token -> {"bids": {p: s}, "asks": {p: s}}
_ULT = {}                  # (hijo) token -> t_ms del último registro (muestreo mínimo entre registros)
_TOPQ = {}                 # (hijo) token -> último top registrado sin muestrear (registro q)
_L2Q = {}                  # (hijo) token -> últimos 3 niveles ask registrados (registro l)
_LFULL = {}                # (hijo) token -> último libro ask completo registrado (registro L, solo pares BTC)
_LFULL_T = {}              # (hijo) token -> hora del exchange de la última fila L (muestreo <= 1 cada MUESTREO_MS)
_T_RECV = [0]              # (hijo) hora local (ms) de recepción del mensaje WS en curso (registro q/t, auditoría de reloj)
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


def _aplicar(msg, salida, k=None):          # k: grupo/conexión de origen (libro5 graba solo la del dueño)
    t_ev = int(msg.get("timestamp") or time.time() * 1000)
    if msg.get("event_type") == "last_trade_price":
        tk = msg.get("asset_id")
        if tk in _LIB:
            try:
                salida.append(("t", tk, (t_ev, float(msg["price"]), msg.get("side"), float(msg.get("size") or 0))))
                if _REGISTRO is not None:
                    _REGISTRO.put(f"t,{t_ev},{tk},{msg.get('price')},{msg.get('side')},{msg.get('size')},{_T_RECV[0]},\n")
                if _LIBRO5 is not None and _LIBRO5.activo:
                    try:
                        _LIBRO5.operacion(t_ev, tk, msg, k)
                    except Exception as e:
                        _LIBRO5.desactivar(f"{type(e).__name__}: {e}")
            except (KeyError, TypeError, ValueError):
                pass
        return
    if "price_changes" in msg:
        tocados = set()
        filas5 = [] if (_LIBRO5 is not None and _LIBRO5.activo) else None   # libro5: filas d de este mensaje
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
            if filas5 is not None and _LIBRO5.grabable(tk, k):
                filas5.append(("d", t_ev, tk, "B" if lado == "bids" else "A", p, s))   # tupla: el texto, en el escritor
        if _REGISTRO is not None:
            for tk in tocados:
                L = _LIB[tk]
                bb = max((p for p, s in L["bids"].items() if s > 0), default=None)
                ba = min((p for p, s in L["asks"].items() if s > 0), default=None)
                top = (bb, ba, L["bids"].get(bb) if bb is not None else None, L["asks"].get(ba) if ba is not None else None)
                if _TOPQ.get(tk) != top:                # precio O tamaño del top (cancelación vs relleno; ~1 GB/día)
                    _TOPQ[tk] = top
                    _REGISTRO.put(f"q,{t_ev},{tk},{top[0]},{top[1]},{top[2]},{top[3]},{_T_RECV[0]}\n")
                cie = _REGISTRO.l2.get(tk)
                if cie is not None and (cie - 305) * 1000 <= t_ev <= cie * 1000:
                    niv = tuple(sorted((p, s) for p, s in L["asks"].items() if s > 0)[:3])
                    if _L2Q.get(tk) != niv:              # l = ask nivel 1..3 (precio, tamaño) + recepción
                        _L2Q[tk] = niv
                        cols = [str(x) for ps in niv for x in ps] + [""] * (6 - 2 * len(niv))
                        _REGISTRO.put(f"l,{t_ev},{tk},{','.join(cols)},{_T_RECV[0]}\n")
                    if tk in _REGISTRO.l2full and t_ev - _LFULL_T.get(tk, 0) >= MUESTREO_MS:   # L: libro ask COMPLETO,
                        full = tuple(sorted((p, s) for p, s in L["asks"].items() if s > 0))  # solo pares BTC, <= 1 cada 100 ms
                        if _LFULL.get(tk) != full:           # L = todos los niveles ask "p:s;p:s;..." + recepción
                            _LFULL[tk] = full
                            _LFULL_T[tk] = t_ev
                            _REGISTRO.put(f"L,{t_ev},{tk},{';'.join(f'{p}:{s}' for p, s in full)},{_T_RECV[0]}\n")
        if filas5:
            try:
                _LIBRO5.put(filas5)
            except Exception as e:                      # libro5 nunca tumba la sesión WS
                _LIBRO5.desactivar(f"{type(e).__name__}: {e}")
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
        if _LIBRO5 is not None and _LIBRO5.activo:
            try:
                _LIBRO5.libro(t_ev, tk, msg, k)
            except Exception as e:
                _LIBRO5.desactivar(f"{type(e).__name__}: {e}")


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
                    _cerrar_libro5()
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
        # 06-Oct (OK Javi): niveles ask 1-3 (fila l) SOLO de los 5m que cierran con un 15m y SOLO en su último tramo,
        # para que vigia_5m_barato_forward.py reconstruya el VWAP multinivel. token -> cierre (epoch s)
        self.l2 = {}
        # 14-Oct (Javi: "necesitamos llegar a todos los niveles"): tokens 5m BTC que cierran con un 15m -> fila L con el
        # libro ask COMPLETO en su último tramo (capacidad real de 5m barato / V7). Tipo nuevo: la fila l (3 niveles) no
        # cambia porque la lee el vigía congelado v4.
        self.l2full = set()
        threading.Thread(target=self._loop, daemon=True, name="registro_ms").start()

    def put(self, linea):
        try:
            self.q.put_nowait(linea)
        except queue.Full:
            self.descartes += 1

    def meta(self, meta):
        for t, (a, m, mid, fin, lado) in meta.items():
            if m == "5min" and t not in self.l2:
                try:
                    cie = int(datetime.fromisoformat(str(fin)).timestamp())
                    if cie % 900 == 0:
                        self.l2[t] = cie
                        if a == "BTC":
                            self.l2full.add(t)
                except (TypeError, ValueError):
                    pass
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
                    f = gzip.open(ruta, "wt", encoding="utf-8", compresslevel=9)   # 14-Oct (Javi): máxima compresión
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


class _Libro5:
    """17-Oct (OK Javi, misión 5m barato H35: "la cola tiene que ser conocida"). Graba el feed CRUDO del libro y de las
    operaciones de TODOS los tokens 5m de todas las monedas durante toda su vida, directamente en el VOLUMEN
    (LIBRO5_DIR/libro5_ms_YYYY-MM-DD_<pid>.csv.gz; no en el disco raíz ni en maker_ms_*, que el vigía congelado v4 y el
    resto de lectores leen entero). Aquí NO se reconstruye nada: la cola se reconstruye después, en el análisis.
    El hilo del socket NO formatea: valida (lo mismo que _aplicar), encola TUPLAS (una escritura en cola por mensaje) y
    sigue; el texto, seq, ficheros, errores y marcas los hace el hilo escritor.
    Filas (8 columnas):
      B,t_ms,token,bids "p:s;..." (orden del servidor),asks,,recepción,seq   libro completo enviado por el servidor
      d,t_ms,token,B|A,precio,tamaño,recepción,seq                         price_change (tamaño absoluto; 0 = vacío)
      T,t_ms,token,precio,BUY|SELL,tamaño,recepción,seq                    last_trade_price (relleno vs cancelación)
      G,t_ms,token|*,motivo[+motivo],,,recepción,seq                       hueco: arranque/caida/cancelada/fin_sesion/
                                     baja/traspaso/json_ilegible/cola_llena/pausa/error_escritura/reanudado/
                                     interruptor/fin_proceso/libro5_desactivado
    Lectura: un proceso (pid) = un flujo; sus ficheros (diarios y _e<n> tras un error) se encadenan por seq. seq NUNCA se
    repite; solo salta justo antes de una G,* con error_escritura (gzip guarda en búfer: lo no volcado se pierde). La
    última línea de un fichero puede estar incompleta (corte): se descarta. Por token: estado = último B + d posteriores
    en orden de seq (NUNCA por t_ms, sello de lote del WS). Tras una G del token o una G,* no hay continuidad hasta su
    siguiente B (el servidor manda B al suscribir y tras cada operación; un token sin operaciones puede tardar).
    Espacio: libro5 se mantiene por debajo de PRESUPUESTO_GB borrando sus propios ficheros más antiguos (nunca el que
    escribe); no depende de lo que ocupen otros. Seguridad: cualquier excepción aquí desactiva libro5 sin tocar la
    sesión WS. Se PAUSA (el socket deja de encolar) y se reanuda solo: con el volumen por debajo de MIN_LIBRE_GB,
    durante el reintento de un error de escritura, o mientras exista el fichero INTERRUPTOR (persistente a reinicios).
    Con ESCRITURA_FALLOS_MAX errores sin un periodo sano (con datos escritos) entre medias, se desactiva. Cada minuto
    deja su estado en ESTADO (activo/pausa/apagado/muerto) para que el vigía de loggers no avise en falso."""

    MAXQ = 20000                   # lotes (uno por mensaje del WS)
    PRESUPUESTO_GB = 20.0          # tope de libro5 en el volumen: por encima se borran sus ficheros más antiguos
    MIN_LIBRE_GB = 10.0            # seguridad: con el volumen por debajo, pausa (los archivos de 60 d recortan a 8)
    ESCRITURA_FALLOS_MAX = 8
    SANO_FLUSHES = 12              # ~1 min de volcados correctos seguidos para dar por sano el disco
    INTERRUPTOR = Path("/root/polymarket-research-datalogs/LIBRO5_OFF")   # fuera de git: el bucle no lo toca
    ESTADO = Path("/root/polymarket-research-datalogs/libro5_estado.json")   # lo lee vigia_loggers_silenciosos

    def __init__(self):
        vol = "/mnt/HC_Volume_106538179"
        if str(LIBRO5_DIR).startswith(vol) and not os.path.ismount(vol):
            raise RuntimeError(f"{vol} no está montado: libro5 no escribe en el disco raíz")
        LIBRO5_DIR.mkdir(parents=True, exist_ok=True)
        self.q = queue.Queue(maxsize=self.MAXQ)
        self.lk = threading.Lock()     # transiciones activo/muerto
        self.activo = True
        self.muerto = False
        self.descartes = 0
        self.perdida = False           # solo la toca el hilo del socket (marca G,*,cola_llena en banda)
        self.cie = {}                  # token 5m -> cierre (epoch s); solo hilo de stdin
        self.rechazados = set()        # tokens 5m cerrados o con cierre ilegible; solo hilo de stdin
        self.toks = frozenset()        # tokens 5m vivos: se SUSTITUYE entera (lectura atómica desde el socket)
        self.dueno = {}                # token 5m vivo -> grupo cuya conexión se graba (la última alta manda; solo socket)
        self.fin = threading.Event()
        self.cerrado = threading.Event()
        threading.Thread(target=self._loop, daemon=True, name="registro_libro5").start()

    # ---------- estado (cualquier hilo) ----------
    def desactivar(self, motivo, definitivo=True):
        with self.lk:
            if definitivo:
                self.muerto = True
            era = self.activo
            self.activo = False
        if era or definitivo:
            _log(f"registro_libro5 {'DESACTIVADO' if definitivo else 'EN PAUSA'}: {motivo}")

    def _reanudar(self):
        with self.lk:
            if self.muerto:
                return False
            self.activo = True
            return True

    # ---------- hilo del socket: solo tuplas ----------
    def put(self, items, recv=None):
        """Una sola escritura en cola por mensaje del WS. Único dueño de self.perdida: la pérdida se marca EN BANDA (la
        G,*,cola_llena va al frente del primer lote que sí entra, en su punto real del flujo)."""
        if not self.activo or not items:
            return
        r = _T_RECV[0] if recv is None else recv
        if self.perdida:
            items = [("G", int(time.time() * 1000), "*", "cola_llena")] + items
        try:
            self.q.put_nowait((r, items))
            self.perdida = False
        except queue.Full:
            self.descartes += len(items)
            self.perdida = True

    def grabable(self, tk, k):
        """Solo los 5m vivos y solo desde la conexión de su grupo dueño (un token no se graba dos veces)."""
        return tk in self.toks and self.dueno.get(tk) == k

    def libro(self, t_ev, tk, msg, k):
        if self.grabable(tk, k):
            # texto compacto con los valores tal cual (sin float): ~1-2 KB en cola, no las listas de dicts del JSON
            b = ";".join(f"{x.get('price')}:{x.get('size')}" for x in (msg.get("bids") or []) if isinstance(x, dict))
            a = ";".join(f"{x.get('price')}:{x.get('size')}" for x in (msg.get("asks") or []) if isinstance(x, dict))
            self.put([("B", t_ev, tk, b, a)])

    def operacion(self, t_ev, tk, msg, k):
        if not self.grabable(tk, k):
            return
        try:
            p, s = float(msg["price"]), float(msg.get("size") or 0)
        except (KeyError, TypeError, ValueError):
            return
        self.put([("T", t_ev, tk, p, msg.get("side") if msg.get("side") in ("BUY", "SELL") else "", s)])

    def alta(self, k, toks):
        """Grupo k suscribe toks: pasa a ser su dueño (si venía de otro grupo: G traspaso, la reconstrucción espera al B
        que el servidor manda al suscribir)."""
        vivos, t, items = self.toks, int(time.time() * 1000), []
        for tk in toks:
            if tk in vivos:
                if self.dueno.get(tk) not in (None, k):
                    items.append(("G", t, tk, "traspaso"))
                self.dueno[tk] = k
        self.put(items, recv=t)
        if len(self.dueno) > 4 * len(vivos) + 1000:
            for tk in [x for x in self.dueno if x not in vivos]:
                del self.dueno[tk]

    def hueco(self, k, toks, motivo):
        """Hueco en la conexión del grupo k: G para los tokens de los que k es dueño. Con baja/fin_sesion k deja de
        ser su dueño; con caida/cancelada/json_ilegible sigue siéndolo (al reconectar: alta y el B del servidor)."""
        t, items = int(time.time() * 1000), []
        for tk in toks:
            if self.dueno.get(tk) != k:
                continue
            items.append(("G", t, tk, motivo))
            if motivo in ("baja", "fin_sesion"):
                del self.dueno[tk]
        self.put(items, recv=t)

    # ---------- hilo de stdin ----------
    def meta(self, meta):
        """Alta de tokens 5m nuevos y poda de los cerrados; publica un frozenset nuevo solo si algo cambió."""
        ahora, cambio = time.time(), False
        for t, (a, m, mid, fin, lado) in meta.items():
            if m != "5min" or t in self.cie or t in self.rechazados:
                continue
            try:
                c = int(datetime.fromisoformat(str(fin)).timestamp())
            except (TypeError, ValueError):
                self.rechazados.add(t)
                continue
            if c >= ahora - 600:
                self.cie[t] = c
                cambio = True
            else:
                self.rechazados.add(t)
        for t in [t for t, c in self.cie.items() if c < ahora - 600]:
            self.cie.pop(t, None)
            self.rechazados.add(t)
            cambio = True
        if len(self.rechazados) > 50000:
            self.rechazados = set(list(self.rechazados)[-20000:])
        if cambio:
            self.toks = frozenset(self.cie)

    def cerrar(self, timeout=3.5):
        """Al salir el proceso: el escritor vuelca (acotado) lo pendiente, G,*,fin_proceso y cierra el gzip."""
        self.fin.set()
        self.cerrado.wait(timeout)

    # ---------- hilo escritor ----------
    def _texto(self, it):
        if it[0] == "d":
            return f"d,{it[1]},{it[2]},{it[3]},{it[4]},{it[5]}"
        if it[0] == "B":
            return f"B,{it[1]},{it[2]},{it[3]},{it[4]},"
        if it[0] == "T":
            return f"T,{it[1]},{it[2]},{it[3]},{it[4]},{it[5]}"
        return f"G,{it[1]},{it[2]},{it[3]},,"

    def _libre(self):
        st = os.statvfs(LIBRO5_DIR)
        return st.f_bavail * st.f_frsize / 1e9

    def _ajustar_presupuesto(self, actual):
        """Borra los libro5_ms más antiguos (nunca `actual`, el fichero abierto) mientras la familia pase de
        PRESUPUESTO_GB. Devuelve el espacio libre del volumen."""
        fs = []
        for p in LIBRO5_DIR.glob("libro5_ms_*.csv.gz"):
            try:
                stp = p.stat()
            except OSError:
                continue
            fs.append((stp.st_mtime, stp.st_size, p))
        total = sum(x[1] for x in fs) / 1e9
        reciente = time.time() - 3 * 86400            # los 3 últimos días de captura nunca se borran por presupuesto
        for mt, tam, p in sorted(fs):
            if total <= self.PRESUPUESTO_GB:
                break
            if (actual is not None and p.name == actual) or mt >= reciente:
                continue
            try:
                p.unlink()
                total -= tam / 1e9
                _log(f"registro_libro5: presupuesto {self.PRESUPUESTO_GB} GB superado, borrado {p.name}")
            except OSError:
                continue
        return self._libre()

    def _estado(self, txt, motivo=""):
        try:
            if txt != getattr(self, "_estado_txt", None):
                self._estado_txt, self._estado_desde = txt, int(time.time())
            tmp = self.ESTADO.with_suffix(".json.tmp")
            tmp.write_text(json.dumps({"ts": int(time.time()), "estado": txt, "desde": self._estado_desde,
                                       "motivo": motivo}))
            tmp.replace(self.ESTADO)
        except OSError:
            pass

    def _vaciar(self):
        try:
            while True:
                self.q.get_nowait()
        except queue.Empty:
            pass

    def _abrir(self, dia_txt, n):
        """Nunca sobrescribe: modo 'x' y, si el nombre existe (mismo PID tras reiniciar, error previo), contador _e<n>."""
        while True:
            suf = f"{os.getpid()}" if n == 0 else f"{os.getpid()}_e{n}"
            try:
                return gzip.open(LIBRO5_DIR / f"libro5_ms_{dia_txt}_{suf}.csv.gz", "xt", encoding="utf-8",
                                 compresslevel=3), n   # CPU baja: comparte proceso con el lector WS
            except FileExistsError:
                n += 1

    def _loop(self):
        st = {"f": None, "dia": None, "n": 0, "seq": 0, "intento": 0, "escrito": False}
        pendiente = {"arranque"}       # motivos de la próxima G,* (se escriben juntos: ninguno pisa a otro)
        fallos, sanos, escrito = 0, 0, False
        t_flush = t_chk = 0.0
        desc_log = 0

        def escribir(recv, items):
            hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
            if st["f"] is None or hoy != st["dia"]:
                if st["f"] is not None:
                    st["f"].close()
                    st["f"] = None
                st["f"], st["n"] = self._abrir(hoy, 0 if hoy != st["dia"] else st["n"])
                st["f"].write("tipo,t_ms,token,c1,c2,c3,recepcion,seq\n")
                st["dia"] = hoy
            s, lineas = st["seq"], []
            if pendiente:
                s += 1
                t_g = int(time.time() * 1000)
                lineas.append(f"G,{t_g},*,{'+'.join(sorted(pendiente))},,,{t_g},{s}\n")
            for it in items:
                s += 1
                lineas.append(f"{self._texto(it)},{recv},{s}\n")
            st["intento"] = s                  # si la escritura falla a medias, estos seq ya no se reutilizan
            st["f"].write("".join(lineas))
            st["seq"] = s
            st["escrito"] = True
            pendiente.clear()

        def cerrar_fichero():
            try:
                if st["f"] is not None:
                    st["f"].close()
            except Exception:
                pass
            st["f"] = None

        def volcar_y_marcar(motivo):
            """Vuelca (máx. 1 s) lo encolado, marca el final y cierra pase lo que pase."""
            try:
                limite = time.time() + 1.0
                try:
                    while time.time() < limite:
                        escribir(*self.q.get_nowait())
                except queue.Empty:
                    pass
                pendiente.add(motivo)
                t_g = int(time.time() * 1000)
                escribir(t_g, [])
            except Exception:
                pass
            finally:
                cerrar_fichero()
                self._vaciar()

        while True:
            try:
                if self.fin.is_set():
                    if self.activo:            # en pausa no se abre ningún fichero nuevo
                        volcar_y_marcar("fin_proceso")
                    else:
                        cerrar_fichero()
                    self.cerrado.set()
                    return
                if self.muerto:
                    volcar_y_marcar("libro5_desactivado")
                    self._estado("muerto")
                    self.cerrado.set()
                    return
                if time.time() - t_chk > 60:
                    t_chk = time.time()
                    apagado = self.INTERRUPTOR.exists()
                    actual = None
                    if st["f"] is not None and st["dia"]:
                        actual = Path(getattr(st["f"], "name", "") or "").name or None
                    libre = self._ajustar_presupuesto(actual)
                    if self.activo and (apagado or libre < self.MIN_LIBRE_GB):
                        self.desactivar("interruptor LIBRO5_OFF" if apagado else
                                        f"volumen con {libre:.1f} GB libres (< {self.MIN_LIBRE_GB})", definitivo=False)
                        pendiente.add("interruptor" if apagado else "pausa")
                    elif not self.activo and not apagado and libre >= self.MIN_LIBRE_GB + 0.5:   # sin estado absorbente
                        self._vaciar()         # lo encolado durante la pausa es de antes del hueco
                        if self._reanudar():
                            pendiente.add("reanudado")
                            _log(f"registro_libro5 REANUDADO: volumen con {libre:.1f} GB libres")
                    self._estado("activo" if self.activo else ("apagado" if apagado else "pausa"),
                                 "" if self.activo else f"libre={libre:.1f}GB fallos={fallos}")
                if not self.activo:
                    self._vaciar()
                    cerrar_fichero()
                    time.sleep(1.0)
                    continue
                try:
                    item = self.q.get(timeout=1.0)
                except queue.Empty:
                    item = None
                if item is not None:
                    escribir(*item)
                if st["f"] is not None and time.time() - t_flush > 5:
                    st["f"].flush()
                    t_flush = time.time()
                    if st["escrito"]:                  # solo cuenta un volcado CON datos nuevos
                        sanos += 1
                        st["escrito"] = False
                    if sanos >= self.SANO_FLUSHES:     # disco sano un rato: el contador de fallos vuelve a 0
                        fallos = 0
                    if self.descartes != desc_log:
                        _log(f"registro_libro5: {self.descartes} filas descartadas (cola llena)")
                        desc_log = self.descartes
            except Exception as e:
                fallos += 1
                sanos = 0
                _log(f"registro_libro5: {type(e).__name__}: {e} (fallo {fallos}/{self.ESCRITURA_FALLOS_MAX})")
                cerrar_fichero()
                st["seq"] = max(st["seq"], st["intento"])   # seq nunca se repite entre ficheros
                st["n"] += 1
                pendiente.add("error_escritura")
                if fallos >= self.ESCRITURA_FALLOS_MAX:
                    self.desactivar(f"{fallos} errores de escritura")
                    volcar_y_marcar("libro5_desactivado")   # protegido: si el disco sigue fallando, solo cierra
                    self._estado("muerto", f"{fallos} errores de escritura")
                    self.cerrado.set()
                    return
                self.desactivar("reintento tras error de escritura", definitivo=False)   # el socket deja de encolar
                self._vaciar()
                self.fin.wait(min(300, 5 * 2 ** (fallos - 1)))   # se despierta si el proceso termina
                if self.fin.is_set():
                    continue
                self._vaciar()                 # lo que entrase en la carrera de la pausa es de antes del hueco
                try:
                    ok = self._ajustar_presupuesto(None) >= self.MIN_LIBRE_GB and not self.INTERRUPTOR.exists()
                except OSError:
                    ok = False
                if ok and self._reanudar():
                    _log("registro_libro5: se reanuda tras el error de escritura")


_REGISTRO = None
_LIBRO5 = None
_SUSC = {}                 # grupo -> tokens suscritos por su sesión viva (libro5: huecos al caer)
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
            _cerrar_libro5()
            os._exit(0)                             # EOF: el padre murió o cerró -> el hijo sale
        if m[0] == "tokens":
            if len(m) > 4 and _LIBRO5 is not None:      # ANTES de publicar la versión: el token ya está en libro5
                try:                                    # cuando el gestor lo suscriba (no se pierde su primer B)
                    _LIBRO5.meta(m[4])
                except Exception as e:
                    _LIBRO5.desactivar(f"{type(e).__name__}: {e}")
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
        except asyncio.CancelledError:
            _hueco_libro5(k, _SUSC.pop(k, ()), "cancelada")
            raise
        except Exception as e:
            _log(f"sesión caída [{k}]: {type(e).__name__}: {e}; reconecta en 2 s")
            _hueco_libro5(k, _SUSC.pop(k, ()), "caida")
            await asyncio.sleep(2)
        else:
            _hueco_libro5(k, _SUSC.pop(k, ()), "fin_sesion")


def _cerrar_libro5():
    if _LIBRO5 is not None:
        try:
            _LIBRO5.cerrar()
        except Exception:
            pass


def _alta_libro5(k, toks):
    if _LIBRO5 is not None and not _LIBRO5.muerto:
        try:
            _LIBRO5.alta(k, list(toks))
        except Exception as e:
            _LIBRO5.desactivar(f"{type(e).__name__}: {e}")


def _hueco_libro5(k, toks, motivo):
    if _LIBRO5 is not None and not _LIBRO5.muerto:     # también en pausa: actualiza dueños (las G no se escriben)
        try:
            _LIBRO5.hueco(k, list(toks), motivo)
        except Exception as e:
            _LIBRO5.desactivar(f"{type(e).__name__}: {e}")


async def _una_sesion(k, emisor):
    async with websockets.connect(WS_URL, ping_interval=20, ping_timeout=20, open_timeout=10, max_queue=None) as ws:
        toks, ver_aplicada = list(_GRUPOS.get(k, [])), _GRUPOS_VER.get(k)
        if not toks:
            return
        # 30-Sep: suscribir 150+ tokens de golpe hace que el servidor mande todas las fotos del libro en una ráfaga,
        # llene SU buffer de envío y corte con 1013. Se suscribe en trozos de SUB_TROZO, uno cada SUB_PAUSA_S,
        # leyendo el socket entre medias; lo mismo para las altas posteriores.
        cola_sub, t_sub = collections.deque(toks[SUB_TROZO:]), time.time()
        t_ping = time.time()
        await ws.send(json.dumps({"type": "market", "assets_ids": toks[:SUB_TROZO]}))
        suscritos = set(toks)
        _alta_libro5(k, toks)
        _SUSC[k] = suscritos                            # libro5: mismos tokens que esta sesión (se marcan si cae)
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
                _alta_libro5(k, nuevos)
                cola_sub.extend(nuevos)
                for t in nuevos:
                    _LIB.setdefault(t, {"bids": {}, "asks": {}})
                suscritos.update(nuevos)
                viejos = [t for t in suscritos if t not in set(deseados)]
                if viejos:
                    await ws.send(json.dumps({"assets_ids": viejos, "operation": "unsubscribe"}))
                    _hueco_libro5(k, viejos, "baja")
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
            # 05-Oct 16:40Z: con una conexión por moneda#marco, las tranquilas (60 min) caían con 1008 "no ping
            # received" (~30/h): el canal de mercado exige un PING de texto cada 10 s; el ping de protocolo no basta.
            if time.time() - t_ping >= PING_S:
                await ws.send("PING")
                t_ping = time.time()
            if not raw or raw == "PONG":
                continue
            _T_RECV[0] = int(time.time() * 1000)
            try:
                j = json.loads(raw)
            except Exception:
                if isinstance(raw, (bytes, bytearray)) or (isinstance(raw, str) and raw[:1] in "[{"):   # mensaje perdido
                    _hueco_libro5(k, suscritos, "json_ilegible")
                continue
            salida = []
            for e in (j if isinstance(j, list) else [j]):
                if isinstance(e, dict):
                    _aplicar(e, salida, k)
            emisor.extend(salida)


def _main_hijo():
    global _ES_HIJO
    _ES_HIJO = True
    try:
        # 17-Oct (Javi: "hazlo con las otras vías", VPS descartado): el lector a nice -10. Medido con renice a mano
        # (12:18Z): sello->recepción p90 ~280 -> ~115 ms y p99 a la mitad con la máquina a load 12-23; la mediana ya
        # está en el suelo de red (~44 ms). Es ligero (~20 % de un núcleo): apenas resta CPU al resto.
        if os.getpriority(os.PRIO_PROCESS, 0) > -10:
            os.setpriority(os.PRIO_PROCESS, 0, -10)  # el padre corre a nice 10; el lector, por delante
    except OSError as e:
        _log(f"no se pudo subir la prioridad del hijo: {e}")
    global _REGISTRO, _LIBRO5
    try:
        _REGISTRO = _Registro()
    except Exception as e:
        _log(f"registro_ms desactivado: {type(e).__name__}: {e}")
    if _REGISTRO is not None:                       # libro5 se apaga con el fichero _Libro5.INTERRUPTOR (persistente)
        try:
            _LIBRO5 = _Libro5()
        except Exception as e:
            _log(f"registro_libro5 desactivado: {type(e).__name__}: {e}")
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
