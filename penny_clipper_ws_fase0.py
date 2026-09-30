#!/usr/bin/env python3
"""penny_clipper_ws_fase0.py -- Penny Clipper disparado por el WebSocket del CLOB (no por el feed RTDS de actividad).
FASE 0, SOLO OBSERVACIÓN, nunca envía órdenes (30-Sep noche, Javi: "Penny Clipper tiene que tener algo").

Por qué: en penny_clipper_fase0 (disparo por RTDS activity/trades) el EV al ask real depende del retraso del feed:
lectura del libro <500 ms tras el segundo del trade +8,6 % (n=395; +8 % el 29 y +9 % el 30-Sep), 500-1000 ms −4,7 %,
>1 s −9,8 %; la versión rápida gana en 15 de 17 estratos (marco, moneda, franja, edad de ronda, spread) con el mismo
precio medio, y la latencia no depende de la hora. El RTDS llega con ~0,9 s de retraso (p50); los trades del canal
market del CLOB (libro_estado_ws, evento last_trade_price con timestamp del exchange en ms) llegan antes.

Qué hace: cada 100 ms recorre los mercados up/down 5m/15m vigentes de las 6 monedas, toma los trades nuevos de ambos
tokens de libro_estado_ws (el del NO normalizado a precio del YES), aplica EXACTAMENTE la regla de Penny Clipper del
observador original (constantes importadas de mean_reversion_penny_clipper_fase0) y, al disparar, registra el libro
del token a comprar (libro en memoria: cero peticiones REST) en +0 / 0,25 / 0,5 / 1 / 2 s desde la DETECCIÓN, con la
latencia real de detección (ahora − timestamp del trade en el exchange).
Salida: /root/polymarket-research-datalogs/penny_clipper_ws_YYYY-MM-DD.csv.gz (gz diario, retención 30 días).
Desenlace: lo resuelve vigia_cripto10_diario.py por market_id.
"""
import csv
import gzip
import threading
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import mean_reversion_penny_clipper_fase0 as PC

DATALOGS = Path("/root/polymarket-research-datalogs")
RETENCION_DIAS = 30
OFFSETS_S = (0.0, 0.25, 0.5, 1.0, 2.0)
COLS = (["ts_deteccion_utc", "ts_trade_ms", "ts_deteccion_ms", "lat_deteccion_ms", "market_id", "activo", "marco",
         "ts_end", "decision", "price_yes", "round_age_s", "osc_range", "reversals", "discount"]
        + [f"{c}_{o}" for o in OFFSETS_S for c in ("ask", "ask_size", "bid", "edad_libro_ms")])
_lock = threading.Lock()
_pool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="pc_ws")
_estado = {"ult_limpieza": 0.0}


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


class _Mercado:
    __slots__ = ("activo", "marco", "ts_end", "yes", "no", "ult_ms", "buffer", "disparado")

    def __init__(self, activo, marco, ts_end, yes, no):
        self.activo, self.marco, self.ts_end, self.yes, self.no = activo, marco, ts_end, yes, no
        self.ult_ms, self.buffer, self.disparado = int(time.time() * 1000), deque(), False


def _regla(e: "_Mercado", t_s: float, price_yes: float):
    """Misma regla que mean_reversion_penny_clipper_fase0._procesar_trade_poly (bloque PENNY CLIPPER)."""
    e.buffer.append((t_s, price_yes))
    while e.buffer and e.buffer[0][0] < t_s - PC.PC_WINDOW_S - 5:
        e.buffer.popleft()
    if e.disparado:
        return None
    ventana = [p for (t, p) in e.buffer if t_s - t <= PC.PC_WINDOW_S]
    if len(ventana) < 3:
        return None
    osc = max(ventana) - min(ventana)
    if osc < PC.PC_MIN_OSC_RANGE:
        return None
    rev, last = 0, None
    for a, b in zip(ventana, ventana[1:]):
        diff = b - a
        if abs(diff) < PC.PC_REVERSAL_STEP:
            continue
        d = "up" if diff > 0 else "down"
        if last and d != last:
            rev += 1
        last = d
    if rev < PC.PC_MIN_REVERSALS:
        return None
    mean_v = sum(ventana) / len(ventana)
    if PC.PC_ZONA_MIN <= price_yes <= PC.PC_ZONA_MAX and mean_v - price_yes >= PC.PC_ENTRY_DISCOUNT:
        return "BUY_YES", mean_v - price_yes, osc, rev
    if PC.PC_ZONA_MIN <= 1 - price_yes <= PC.PC_ZONA_MAX and price_yes - mean_v >= PC.PC_ENTRY_DISCOUNT:
        return "BUY_NO", price_yes - mean_v, osc, rev
    return None


def _limpiar():
    if time.time() - _estado["ult_limpieza"] < 3600:
        return
    _estado["ult_limpieza"] = time.time()
    corte = time.time() - RETENCION_DIAS * 86400
    for f in DATALOGS.glob("penny_clipper_ws_*.csv.gz"):
        try:
            if f.stat().st_mtime < corte:
                f.unlink()
        except OSError:
            pass


def _registrar(base: dict, token: str, t_det: float):
    import libro_estado_ws as LE
    fila = dict(base)
    for off in OFFSETS_S:
        espera = t_det + off - time.time()
        if espera > 0:
            time.sleep(espera)
        top = LE.ultimo(token)
        ahora_ms = int(time.time() * 1000)
        fila.update({f"ask_{off}": top[3] if top else "", f"ask_size_{off}": top[4] if top else "",
                     f"bid_{off}": top[1] if top else "", f"edad_libro_ms_{off}": (ahora_ms - top[0]) if top else ""})
    _limpiar()
    out = DATALOGS / f"penny_clipper_ws_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.csv.gz"
    with _lock:
        nuevo = not out.exists()
        with gzip.open(out, "at", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=COLS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def main():
    import libro_estado_ws as LE
    import live_trade as lt
    from fetch_libro_ambos_lados import _universo_activo
    LE.iniciar(("5min", "15min"))
    _log("penny_clipper_ws_fase0 arrancado (disparo por trades del WebSocket del CLOB, libro en memoria, solo observación)")
    mercados, ult_universo = {}, 0.0
    while True:
        try:
            ahora = time.time()
            if ahora - ult_universo > 20:
                ult_universo = ahora
                for mid, (a, marco, _cid, edt) in _universo_activo().items():
                    if mid in mercados or marco not in PC.DUR_S or a not in PC.ACTIVOS:
                        continue
                    try:
                        yes, no, _ = lt._get_token_ids(mid)
                    except Exception:
                        continue
                    if yes and no:
                        mercados[mid] = _Mercado(a, marco, edt.timestamp(), yes, no)
                for mid in [m for m, e in mercados.items() if e.ts_end < ahora - 60]:
                    del mercados[mid]
            ahora_ms = int(ahora * 1000)
            for mid, e in mercados.items():
                if not (e.ts_end - PC.DUR_S[e.marco] <= ahora <= e.ts_end):
                    continue
                nuevos = [(t, p) for (t, p, _s, _z) in LE.trades(e.yes, e.ult_ms + 1, ahora_ms)]
                nuevos += [(t, round(1 - p, 4)) for (t, p, _s, _z) in LE.trades(e.no, e.ult_ms + 1, ahora_ms)]
                if not nuevos:
                    continue
                nuevos.sort()
                e.ult_ms = nuevos[-1][0]
                for t_ms, py in nuevos:
                    if not 0 < py < 1:
                        continue
                    r = _regla(e, t_ms / 1000, py)
                    if r and not e.disparado:
                        e.disparado = True
                        decision, disc, osc, rev = r
                        t_det = time.time()
                        base = {"ts_deteccion_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                                "ts_trade_ms": t_ms, "ts_deteccion_ms": int(t_det * 1000),
                                "lat_deteccion_ms": int(t_det * 1000) - t_ms, "market_id": mid, "activo": e.activo,
                                "marco": e.marco, "ts_end": int(e.ts_end), "decision": decision,
                                "price_yes": round(py, 4), "round_age_s": round(t_ms / 1000 - (e.ts_end - PC.DUR_S[e.marco]), 1),
                                "osc_range": round(osc, 4), "reversals": rev, "discount": round(disc, 4)}
                        _pool.submit(_registrar, base, e.yes if decision == "BUY_YES" else e.no, t_det)
        except Exception as ex:
            _log(f"error en bucle: {type(ex).__name__}: {ex}")
            time.sleep(1)
        time.sleep(0.1)


if __name__ == "__main__":
    main()
