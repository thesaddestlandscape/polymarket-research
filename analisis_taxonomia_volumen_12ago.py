#!/usr/bin/env python3
"""
analisis_taxonomia_volumen_12ago.py — prototipo retrospectivo (shadow puro,
no toca producción) del pendiente `project_pendiente_detectar_spikes_
volumen_12ago`: `volumen_regimen` hoy es un ratio simple (volumen reciente
20min / línea base 3h) que no mostró señal fuerte en agregado sobre
GBM_LATE_15M#BUY_YES (diff=+0.055, shuffle p=0.46). Hipótesis: un ratio
agregado mezcla 3 patrones cualitativamente distintos (creciente sostenido
= momentum, plano = reversión, spike puntual = agotamiento/reversión) que
un solo número no separa.

Método: para cada predicción histórica GBM_LATE_15M#BUY_YES post-TWAP,
reconstruye el volumen minuto a minuto de los 20min PREVIOS al momento de
la predicción (klines históricos de Binance, API pública, sin límite de
histórico) partido en 4 bloques de 5min, y calcula:
  - pendiente_norm: pendiente de regresión lineal de los 4 bloques,
    normalizada por su media (positiva = creciente, negativa = decreciente).
  - spike_ratio: bloque máximo / mediana de los otros 3 -- alto = un solo
    bloque domina (actividad climática puntual).
  - patron: 'spike' (spike_ratio>=2.5) > 'creciente' (pendiente_norm>=0.15)
    > 'decreciente' (pendiente_norm<=-0.15) > 'plano' (resto).

Cruza el patrón resultante con acierto/pnl_neto real (results.csv) para
ver si separa la señal mejor que el ratio agregado actual. NO modifica
shadow_predict.py/FEATURE_RULES -- puramente analítico.
"""
import csv
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import requests

csv.field_size_limit(sys.maxsize)
REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data" / "shadow" / "results.csv"

BINANCE_SYMBOLS = {"BTC": "BTCUSDT", "ETH": "ETHUSDT", "SOL": "SOLUSDT",
                   "XRP": "XRPUSDT", "DOGE": "DOGEUSDT", "BNB": "BNBUSDT"}
TWAP_FECHA = datetime(2026, 8, 7, tzinfo=timezone.utc)
VENTANA_MIN = 20
N_BLOQUES = 4
MIN_POR_BLOQUE = VENTANA_MIN // N_BLOQUES
SPIKE_UMBRAL = 2.5
PENDIENTE_UMBRAL = 0.15
TIMEOUT = 10


def cargar_predicciones() -> list:
    rows = []
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("strategy") != "GBM_LATE_15M" or row.get("decision") != "BUY_YES":
                continue
            ts = row.get("prediction_timestamp", "")
            try:
                dt = datetime.fromisoformat(ts)
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
            except Exception:
                continue
            if dt < TWAP_FECHA:
                continue
            activo = row["subtype"].split("#")[0]
            if activo not in BINANCE_SYMBOLS:
                continue
            acierto = row.get("acierto")
            try:
                pnl = float(row["pnl_neto"])
            except (TypeError, ValueError):
                continue
            rows.append((dt, activo, acierto, pnl))
    return rows


def clasificar_patron(dt: datetime, activo: str) -> str | None:
    symbol = BINANCE_SYMBOLS[activo]
    fin_ms = int(dt.timestamp() * 1000)
    inicio_ms = int((dt - timedelta(minutes=VENTANA_MIN)).timestamp() * 1000)
    try:
        r = requests.get(
            "https://api.binance.com/api/v3/klines",
            params={"symbol": symbol, "interval": "1m",
                    "startTime": inicio_ms, "endTime": fin_ms, "limit": VENTANA_MIN + 2},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        velas = r.json()
    except Exception:
        return None
    if len(velas) < VENTANA_MIN - 2:
        return None
    vols = [float(k[5]) for k in velas[-VENTANA_MIN:]]
    if len(vols) < VENTANA_MIN:
        return None

    bloques = [sum(vols[i:i + MIN_POR_BLOQUE]) for i in range(0, VENTANA_MIN, MIN_POR_BLOQUE)]
    if len(bloques) != N_BLOQUES or any(b <= 0 for b in bloques):
        return None

    x = np.arange(N_BLOQUES)
    y = np.array(bloques, dtype=np.float64)
    media = y.mean()
    pendiente = np.polyfit(x, y, 1)[0]
    pendiente_norm = pendiente / media if media > 0 else 0.0

    idx_max = int(np.argmax(y))
    otros = np.delete(y, idx_max)
    mediana_otros = float(np.median(otros)) if len(otros) else 0.0
    spike_ratio = (y[idx_max] / mediana_otros) if mediana_otros > 0 else 999.0

    if spike_ratio >= SPIKE_UMBRAL:
        return "spike"
    if pendiente_norm >= PENDIENTE_UMBRAL:
        return "creciente"
    if pendiente_norm <= -PENDIENTE_UMBRAL:
        return "decreciente"
    return "plano"


def main() -> int:
    predicciones = cargar_predicciones()
    print(f"Predicciones GBM_LATE_15M#BUY_YES post-TWAP: {len(predicciones)}")

    muestra = predicciones[-350:] if len(predicciones) > 350 else predicciones
    print(f"Muestra a consultar en Binance (histórico, klines 1m): {len(muestra)}")

    por_patron = defaultdict(list)  # patron -> [(acierto, pnl, activo)]
    por_patron_activo = defaultdict(lambda: defaultdict(list))
    fallos = 0
    for i, (dt, activo, acierto, pnl) in enumerate(muestra):
        if i % 50 == 0:
            print(f"  ... {i}/{len(muestra)}", flush=True)
        patron = clasificar_patron(dt, activo)
        if patron is None:
            fallos += 1
            continue
        hit = 1 if acierto in ("1", "True", "true") else 0
        por_patron[patron].append((hit, pnl))
        por_patron_activo[patron][activo].append((hit, pnl))
        time.sleep(0.05)

    print(f"\nFallos de consulta (klines insuficientes/error red): {fallos}")
    print("\n=== Resultado por patrón (agregado, todas las monedas) ===")
    for patron in ("creciente", "plano", "decreciente", "spike"):
        lst = por_patron.get(patron, [])
        n = len(lst)
        if n == 0:
            print(f"  {patron:12s} n=0")
            continue
        hits = sum(h for h, p in lst)
        pnls = [p for h, p in lst]
        print(f"  {patron:12s} n={n:4d}  hit={hits / n * 100:5.1f}%  pnl_medio={sum(pnls) / n:+.3f}")

    print("\n=== Desagregado por patrón x activo (CLAUDE.md pt.17) ===")
    for patron in ("creciente", "plano", "decreciente", "spike"):
        por_activo = por_patron_activo.get(patron, {})
        for activo in sorted(por_activo):
            lst = por_activo[activo]
            n = len(lst)
            if n < 5:
                continue
            hits = sum(h for h, p in lst)
            pnls = [p for h, p in lst]
            print(f"  {patron:12s} {activo:5s} n={n:3d}  hit={hits / n * 100:5.1f}%  pnl_medio={sum(pnls) / n:+.3f}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
