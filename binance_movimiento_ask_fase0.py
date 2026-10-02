#!/usr/bin/env python3
"""binance_movimiento_ask_fase0.py -- FASE 0, SOLO OBSERVACIÓN (02-Oct, Javi: "ok, guarda y dale a todo").

Motivo (project_bote_latencia_binance_200k_02oct): en el firehose de 30-Sep y 01-Oct, las compras up/down 5m+15m
hechas con Binance movido >1 bps A FAVOR en [t-3, t] ganan ~+92-99 k$/día y las hechas en contra pierden lo mismo;
el 77 % está en BTC 5m. Ese bote está medido al precio de PRINT (optimista tras un movimiento: trampa conocida).
binance_jump_leadlag_fase0 solo mira saltos grandes (>=2,5 bps BTC en 1 s); aquí se miden los movimientos PEQUEÑOS
(1-3 bps), que son casi todo el bote, al ASK REAL del libro.

Qué hace: se engancha al bookTicker que ya mantiene binance_jump_leadlag_fase0 (cero WebSockets nuevos, cero REST).
Cuando el retorno de Binance en 1 s supera UMBRAL[moneda] (dedup DEDUP_S por moneda), para cada mercado 5m/15m
vigente con resto >= RESTO_MIN programa UNA lectura diferida (t0 + 2,2 s) del histórico ms de libro_estado_ws:
ask/tamaño/bid del token del lado del movimiento en OFFSETS_S (0 = antes de poder reaccionar), ask del lado
contrario en 0, y el mid de Binance en t0, +0,6 s y +2 s. Desenlace oficial: después (analisis), por market_id.
-> /root/polymarket-research-datalogs/binance_movimiento_ask_YYYY-MM-DD.csv (gz al día siguiente, RETENCION_DIAS).
NUNCA envía órdenes.
"""
import csv
import gzip
import heapq
import math
import shutil
import threading
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path

import libro_estado_ws as LE
from resolution_sniper_observer import _CACHE_MKT, token_ids

DATALOGS = Path("/root/polymarket-research-datalogs")
PREFIJO = "binance_movimiento_ask"
RETENCION_DIAS = 14
# 1 bps BTC (escalado como binance_jump_leadlag_fase0.UMBRAL / 2,5): movimiento en 1 s
UMBRAL = {"BTC": 1.0e-4, "ETH": 1.2e-4, "SOL": 1.6e-4, "XRP": 1.6e-4, "DOGE": 2.0e-4, "BNB": 1.2e-4}
DEDUP_S = 3.0
MARCOS = {"5m": 300, "15m": 900}
RESTO_MIN = 10
OFFSETS_S = [0.0, 0.15, 0.3, 0.6, 1.0, 2.0]
LECTURA_S = 2.2
CAMPOS = (["ts_ms", "activo", "marco", "slug", "market_id", "resto_s", "direccion", "ret_1s", "ret_3s", "mid0",
           "mid_06", "mid_2", "ask_contrario_0"]
          + [f"{c}_{str(o).replace('.', '')}" for o in OFFSETS_S for c in ("ask", "ask_size", "bid", "edad_ms")])
_lock = threading.Lock()
_ticks = {}            # activo -> deque[(t, mid)] de ~4 s
_ult = {}              # activo -> t del último evento
_cola = []             # heap (t_lectura, seq, base, tok, tok_contrario, activo)
_cond = threading.Condition()
_seq = [0]
_arrancado = [False]


def _log(msg):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _mid_en(activo, t):
    """Último mid de Binance con tiempo <= t (None si no hay)."""
    m = None
    for tt, mm in list(_ticks.get(activo, ())):
        if tt <= t:
            m = mm
        else:
            break
    return m


def tick(activo, mid, t):
    """Llamado por binance_jump_leadlag_fase0._procesar en cada tick del bookTicker. Debe ser barato y no lanzar."""
    if not _arrancado[0]:
        return
    dq = _ticks.setdefault(activo, deque())
    dq.append((t, mid))
    while dq and dq[0][0] < t - 4.0:
        dq.popleft()
    ref = None
    for tt, mm in dq:
        if t - tt >= 1.0:
            ref = mm
        else:
            break
    if not ref or mid <= 0 or abs(math.log(mid / ref)) < UMBRAL.get(activo, 1.0) or t - _ult.get(activo, -1e9) < DEDUP_S:
        return
    _ult[activo] = t
    ret = math.log(mid / ref)
    r3 = dq[0][1] if t - dq[0][0] >= 2.9 else None
    direccion = "Up" if ret > 0 else "Down"
    for tag, dur in MARCOS.items():
        ini = int(t // dur) * dur
        resto = ini + dur - t
        if resto < RESTO_MIN:
            continue
        slug = f"{activo.lower()}-updown-{tag}-{ini}"
        mkt = _CACHE_MKT.get(slug)              # solo caché (la calienta binance_jump_leadlag_fase0._calentar)
        if not mkt:
            continue
        ty, tn = token_ids(mkt)
        tok, contra = (ty, tn) if direccion == "Up" else (tn, ty)
        if not tok:
            continue
        base = {"ts_ms": int(t * 1000), "activo": activo, "marco": tag, "slug": slug, "market_id": mkt.get("id", ""),
                "resto_s": round(resto, 2), "direccion": direccion, "ret_1s": round(ret, 6),
                "ret_3s": round(math.log(mid / r3), 6) if r3 else "", "mid0": mid}
        with _cond:
            _seq[0] += 1
            heapq.heappush(_cola, (t + LECTURA_S, _seq[0], base, tok, contra, activo))
            _cond.notify()


def _escribir(fila):
    ruta = DATALOGS / f"{PREFIJO}_{datetime.now(timezone.utc):%Y-%m-%d}.csv"
    with _lock:
        nuevo = not ruta.exists()
        with open(ruta, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            if nuevo:
                w.writeheader()
            w.writerow(fila)


def _mantenimiento():
    hoy = f"{datetime.now(timezone.utc):%Y-%m-%d}"
    for f in DATALOGS.glob(f"{PREFIJO}_*.csv"):
        if hoy not in f.name:
            with open(f, "rb") as a, gzip.open(str(f) + ".gz", "wb") as b:
                shutil.copyfileobj(a, b)
            f.unlink()
    for f in DATALOGS.glob(f"{PREFIJO}_*.csv.gz"):
        if time.time() - f.stat().st_mtime > RETENCION_DIAS * 86400:
            f.unlink()


def _leer(base, tok, contra, activo):
    t0_ms = base["ts_ms"]
    fila = dict(base)
    t0 = t0_ms / 1000
    fila["mid_06"] = _mid_en(activo, t0 + 0.6) or ""
    fila["mid_2"] = _mid_en(activo, t0 + 2.0) or ""
    c = LE.en(contra, t0_ms) if contra else None
    fila["ask_contrario_0"] = c["best_ask"] if c else ""
    for o in OFFSETS_S:
        e = LE.en(tok, t0_ms + int(o * 1000))
        s = str(o).replace(".", "")
        fila[f"ask_{s}"] = e["best_ask"] if e else ""
        fila[f"ask_size_{s}"] = e["ask_size"] if e else ""
        fila[f"bid_{s}"] = e["best_bid"] if e else ""
        fila[f"edad_ms_{s}"] = e["edad_ms"] if e else ""
    _escribir(fila)


def main():
    LE.iniciar(("5min", "15min"))
    _arrancado[0] = True
    _log(f"binance_movimiento_ask_fase0 arrancado (umbrales {UMBRAL}, dedup {DEDUP_S} s, offsets {OFFSETS_S}, solo observación)")
    t_mant, n = 0.0, 0
    while True:
        try:
            if time.time() - t_mant > 3600:
                t_mant = time.time()
                _mantenimiento()
                if n:
                    _log(f"{n} filas escritas en la última hora")
                n = 0
            with _cond:
                while not _cola or _cola[0][0] > time.time():
                    _cond.wait(timeout=0.5 if not _cola else max(0.01, _cola[0][0] - time.time()))
                    if time.time() - t_mant > 3600:
                        break
                if not _cola or _cola[0][0] > time.time():
                    continue
                _, _, base, tok, contra, activo = heapq.heappop(_cola)
            _leer(base, tok, contra, activo)
            n += 1
        except Exception as e:
            _log(f"🚨 error: {type(e).__name__}: {e}")
            time.sleep(1)


if __name__ == "__main__":
    main()
