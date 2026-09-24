#!/usr/bin/env python3
"""saltos_chainlink_fase0.py -- A3 "ganarles al entrar", FASE 0 (24-Sep, Javi). SOLO OBSERVACIÓN:
nunca envía órdenes.

Base (analisis_leadlag_chainlink_libro_24sep.py, 4 días 21-24 Sep, ~8.300 eventos): cuando el
precio JUSTO de un Up/Down 5/15min (Chainlink + regla TWAP) salta >=0,08, el mercado tarda ~5 s
(mediana) en cerrar la mitad del hueco; entrando 1 s después al ÚLTIMO TRADE el EV es
+0,15/+0,27 EUR/tr agregado, y +0,37/+0,68 en DOGE#5min, +0,21/+0,37 en BNB#5min, +0,09/+0,23 en
XRP#5min, ~0 en BTC. Falta lo decisivo: ¿el ASK REAL, con profundidad, en ese instante?

Qué hace: cada 0,25 s, por cada mercado vigente (6 monedas × 5/15min) calcula p_justo con la
misma fórmula del análisis (Chainlink hora de recepción, cola compartida _TAIL). Si
|p(t) - p(t-2 s)| >= SALTO y no hubo evento en ese mercado en 20 s, lee el libro PÚBLICO del lado
del salto (_profundidad_correcta del precierre, stake 1,05) y registra ask, profundidad, VWAP de
relleno, latencias y el estado TWAP para calcular después el EV real al ask con el resultado
por regla TWAP. -> data/shadow/saltos_chainlink_fase0.csv
Dentro de observadores_fase0.py la cola _TAIL ya la arranca resolution_sniper_observer (no se
arranca otra: duplicaría ticks); suelto (__main__) sí se arranca.
"""
import csv
import math
import statistics
import threading
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
from resolution_sniper_observer import _TAIL, mercado_slot, token_ids

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "saltos_chainlink_fase0.csv"
ACTIVOS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
MARCOS = {"5m": 300, "15m": 900}
SALTO = 0.08
CADA_S = 0.25
STAKE = 1.05
CAMPOS = ["ts_utc", "activo", "marco", "slug", "market_id", "ini", "fin", "resto_s", "p_justo", "p_justo_prev",
          "direccion", "ref_twap", "spot", "edad_tick_s", "ask", "profundidad_eur", "ratio_vs_stake",
          "vwap_fill", "fill_completo", "lat_libro_ms", "error"]
_lock = threading.Lock()
_pool = ThreadPoolExecutor(max_workers=4)


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _escribir(fila):
    with _lock:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _ticks(activo, ventana_s=1200):
    """Solo los últimos `ventana_s` segundos de la cola (la cola guarda ~4 h: copiarla entera
    4 veces/s por moneda sería CPU tirada)."""
    lim = time.time() - ventana_s
    out = []
    with _TAIL._lock:
        for x in reversed(_TAIL._buf.get(activo, ())):
            if x[0] < lim:
                break
            out.append(x)
    out.reverse()
    return out


def _profundidad(token_id, stake):
    """Misma lógica que resolution_sniper_precierre_executor._profundidad_correcta (techo anclado
    al mejor ask real, 1,05x), replicada para no importar el ejecutor live en este proceso."""
    book = lt._fetch_book_publico(token_id)
    if book is None:
        return {"ok": False, "error": "sin respuesta del libro"}
    asks = book.get("asks") or []
    precios = []
    for lvl in asks:
        try:
            precios.append((float(lvl["price"]), float(lvl["size"])))
        except (TypeError, ValueError, KeyError):
            continue
    if not precios:
        return {"ok": True, "mejor_ask": None, "profundidad_eur": 0.0, "ratio_vs_stake": 0.0}
    mejor = min(p for p, _ in precios)
    prof = sum(p * sz for p, sz in precios if p <= mejor * 1.05)
    vwap, completo = lt.vwap_fill_desde_niveles(asks, stake, mejor)
    return {"ok": True, "mejor_ask": mejor, "profundidad_eur": round(prof, 2),
            "ratio_vs_stake": round(prof / stake, 1), "vwap_fill_estimado": vwap,
            "fill_completo_en_niveles": completo}


def _media(dq, t0, t1):
    v = [p for t, p in dq if t0 <= t <= t1]
    return (sum(v) / len(v), len(v)) if v else (None, 0)


def _sigma(dq, t):
    r = [math.log(b[1] / a[1]) / math.sqrt(max(b[0] - a[0], 1e-3))
         for a, b in zip(dq, dq[1:]) if t - 300 <= a[0] and b[0] <= t and a[1] > 0 and b[1] > 0 and b[0] > a[0]]
    return statistics.pstdev(r) if len(r) >= 30 else None


def _p_justo(dq, t, ini, fin, sig):
    ref, nr = _media(dq, ini - 60, ini)
    if ref is None or nr < 10 or not sig or not dq or t - dq[-1][0] > 5:
        return None
    spot, resto = dq[-1][1], max(0.0, fin - t)
    if resto > 60:
        proy = spot
    else:
        m, n = _media(dq, fin - 60, t)
        if m is None or n < 5:
            return None
        proy = (m * (t - (fin - 60)) + spot * resto) / 60.0
    teff = max(resto - 40 if resto > 60 else resto ** 3 / (3 * 3600), 15.0)
    x = math.log(proy / ref) / (sig * math.sqrt(teff))
    return 0.5 * (1 + math.erf(x / math.sqrt(2))), ref, spot


def _leer_y_registrar(fila, activo, marco_tag, ini, direccion):
    t0 = time.perf_counter()
    try:
        slug, mkt = mercado_slot(activo, marco_tag, ini)
        fila["slug"] = slug
        if not mkt:
            fila["error"] = "sin_mercado"
        else:
            fila["market_id"] = mkt.get("id", "")
            ty, tn = token_ids(mkt)
            tok = ty if direccion == "Up" else tn
            if not tok:
                fila["error"] = "sin_token"
            else:
                d = _profundidad(tok, STAKE)
                if not d.get("ok"):
                    fila["error"] = d.get("error", "libro")
                else:
                    fila.update({"ask": d.get("mejor_ask"), "profundidad_eur": d.get("profundidad_eur"),
                                 "ratio_vs_stake": d.get("ratio_vs_stake"), "vwap_fill": d.get("vwap_fill_estimado"),
                                 "fill_completo": d.get("fill_completo_en_niveles")})
    except Exception as e:
        fila["error"] = f"{type(e).__name__}: {e}"[:120]
    fila["lat_libro_ms"] = round((time.perf_counter() - t0) * 1000)
    _escribir(fila)


def main():
    _log(f"saltos_chainlink_fase0 arrancado (SALTO={SALTO}, solo observación)")
    hist = {}      # (activo, marco, ini) -> deque[(t, p)]
    sig = {}       # activo -> (t_calc, sigma)
    ult_ev = {}    # (activo, marco, ini) -> t
    while True:
        ahora = time.time()
        for activo in ACTIVOS:
            dq = _ticks(activo)
            if len(dq) < 30:
                continue
            if ahora - sig.get(activo, (-1e9, None))[0] >= 60:
                sig[activo] = (ahora, _sigma(dq, ahora))
            for tag, dur in MARCOS.items():
                ini = int(ahora // dur) * dur
                fin = ini + dur
                if ahora - ini < 5 or fin - ahora < 3:
                    continue
                r = _p_justo(dq, ahora, ini, fin, sig[activo][1])
                if r is None:
                    continue
                p, ref, spot = r
                k = (activo, tag, ini)
                h = hist.setdefault(k, deque())
                h.append((ahora, p))
                while h and h[0][0] < ahora - 2.5:
                    h.popleft()
                p_prev = next((pp for tt, pp in h if ahora - tt >= 1.75), None)
                if p_prev is None or abs(p - p_prev) < SALTO or ahora - ult_ev.get(k, -1e9) < 20:
                    continue
                ult_ev[k] = ahora
                direccion = "Up" if p > p_prev else "Down"
                fila = {c: "" for c in CAMPOS}
                fila.update({"ts_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                             "activo": activo, "marco": tag, "ini": ini, "fin": fin,
                             "resto_s": round(fin - ahora, 1), "p_justo": round(p, 4),
                             "p_justo_prev": round(p_prev, 4), "direccion": direccion,
                             "ref_twap": ref, "spot": spot, "edad_tick_s": round(ahora - dq[-1][0], 2)})
                _pool.submit(_leer_y_registrar, fila, activo, tag, ini, direccion)
        # poda de ventanas viejas
        for k in [k for k in hist if k[2] + MARCOS[k[1]] < ahora - 60]:
            hist.pop(k, None)
            ult_ev.pop(k, None)
        time.sleep(max(0.0, CADA_S - (time.time() - ahora)))


if __name__ == "__main__":
    _TAIL.arrancar()
    time.sleep(5)
    main()
