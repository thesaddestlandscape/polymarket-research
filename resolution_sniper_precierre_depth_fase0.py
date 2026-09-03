#!/usr/bin/env python3
"""
resolution_sniper_precierre_depth_fase0.py — FASE 0 (SOLO OBSERVACIÓN), 01-Sep.

Origen: RESOLUTION_SNIPER_NAIVE (P34) llevaba 59/59 intentos de orden real
fallidos desde el 31-Ago 23:15 UTC, TODOS con PolyApiException[503,
'trading is disabled'] -- incluido el intento MÁS RÁPIDO medido (2.0s tras
el cierre nominal del mercado). Retirada de `pares_permitidos_live` el
mismo día (ver `_pares_resolutionsnipernaive_pausa_nota_2026-09-01` en
config_live.json). Diagnóstico: Polymarket deshabilita el envío de
órdenes esencialmente en el instante de `endDate`, sin margen post-cierre
-- ningún ajuste de latencia en nuestro pipeline habría bastado, porque ni
el intento más rápido lo consiguió. El borde temporal que sostenía el
edge (offset 0-3s DESPUÉS del cierre) ya no existe.

Este observador prueba el ángulo simétrico, sin chocar contra esa pared:
apostar la dirección implícita 1-2s ANTES del cierre nominal, mientras el
libro sigue confirmadamente abierto (verificado: `resolution_sniper_
observer.py` lleva semanas capturando ask_yes/ask_no reales en offset=-2/
-1 sin ningún fallo de "trading is disabled" -- solo consulta, nunca
envía orden).

Análisis retrospectivo sobre datos YA EXISTENTES (resolution_sniper_obs_
*.csv, sin construir nada, 01-Sep) confirma que el edge sobrevive ahí:
restringido al subconjunto accionable (ask del lado implícito en
[0.05,0.95], igual criterio que resolution_sniper_naive_depth_fase0.py),
5min, los 6 activos confirmados el 19-Ago (BTC/ETH/SOL/XRP/DOGE/BNB):

  offset  n por activo   hit agregado   pnl/trade agregado (stake 1.05€, sin fee)
  -2      247-413         72.4%          +0.276€
  -1      247-413         72.4%          +0.276€

(n=3973 combinado ambos offsets, 6 activos -- cada celda individual ya
por encima de n≥40). Positivo en LAS 6 monedas, en AMBOS offsets, sin
ningún outlier negativo -- ver memoria `idea_resolution_sniper_precierre_
hallazgo_01sep` para el detalle completo del análisis retrospectivo y el
gate riguroso (Wilson+shuffle+split-half) todavía pendiente antes de
proponer nada con dinero.

PERO ese análisis usa el ask observado, no profundidad real -- mismo
cuello de botella que motivó `resolution_sniper_fade_depth_fase0.py` en
su día (14-Ago) y que el propio RESOLUTION_SNIPER_NAIVE post-cierre SÍ
tenía resuelto (99.2% seguía fillable) hasta que chocó con el muro de
"trading is disabled". Este script mide EXACTAMENTE eso para el lado
pre-cierre, antes de proponer ningún ejecutor: profundidad real
(`lt._consultar_profundidad_libro`, misma función que el resto de la
familia) en offset=-2 y offset=-1, para los 6 activos confirmados en
5min.

Mecanismo (mismo patrón que resolution_sniper_fade_depth_fase0.py --
reusa descubrimiento de mercado + tail de Chainlink de
resolution_sniper_observer.py, decisión ladder CLAUDE.md: no duplicar
código ya existente):
  1. Un hilo por activo (los 6 ya cubiertos por resolution_sniper_
     observer.py en 5min), mismo reloj de ventana (dur_s=300).
  2. En offsets [-2,-1] ANTES del cierre nominal, calcula
     chainlink_direccion_implicita igual que el observador original.
  3. Si el ask del lado implícito está en [0.05,0.95] -- consulta
     profundidad real de ESE lado (no fade, dirección naive) vía
     `lt._consultar_profundidad_libro`, stake de referencia 1.05€.
  4. Persiste en data/shadow/resolution_sniper_precierre_depth_fase0.csv.
     Cruce posterior con outcome_real (join market_id contra
     resolution_sniper_obs_*.csv) responde con rigor completo si el
     pre-cierre es ejecutable de verdad.

NO coloca, cancela ni modifica ninguna orden real -- puramente
lectura (GET), mismo criterio de riesgo que el resto de *_fase0.py. No
toca `pares_permitidos_live` ni ninguna decisión de dinero real.

Se fusiona en observadores_fase0.py (screen "observadores") -- NUNCA
lanzar una screen suelta para este script.
"""
import csv
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt
from resolution_sniper_observer import (
    ASSETS, DESPERTAR_ANTICIPO_S, _TAIL,
    mercado_slot, token_ids, libro,
)

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "resolution_sniper_precierre_depth_fase0.csv"

DUR_S = 300      # 5min -- único marco confirmado el 19-Ago para esta familia
MARCO = "5min"
MARCO_TAG = "5m"
# 03-Sep noche: ampliado de [-2,-1] a la rejilla completa. Motivo (hallazgo
# real de esta sesión, prueba controlada 13:14:58Z): el edge de esta familia
# está medido SOLO a -1/-2s, y a -2s NO llegamos a tiempo -- el pipeline
# genérico de dinero real consume los 2s enteros en validaciones y la orden
# aterriza en ts_end exacto ("trading is disabled", mismo muro que tumbó
# RESOLUTION_SNIPER_NAIVE 59/59). Entre 60s (último punto que mide
# punto_confirmacion_*.csv) y 2s NADIE medía precio+profundidad+outcome:
# zona ciega real. Sin esa curva no se puede decidir a qué offset disparar
# -- mover el offset cambia la distribución medida, así que el hit=95,6%
# de [0,47-0,52) NO se puede asumir válido a -5s ni a -10s, hay que medirlo.
# Coste: 8 offsets × 6 activos × 2 GET (~74ms cada uno) por ventana de 5min,
# un hilo por activo (sin contención entre ellos), offsets separados ≥1s.
OFFSETS_PRE_S = [-30, -20, -12, -8, -5, -3, -2, -1]  # segundos ANTES del cierre nominal
# Anticipo propio, NO se toca DESPERTAR_ANTICIPO_S (=6) importado de
# resolution_sniper_observer.py: esa constante la comparte el observador
# post-cierre, que lleva meses acumulando con ella. Aquí hace falta más
# margen porque el primer offset ya no es -2s sino -30s, y observar_ventana()
# resuelve el mercado en gamma (~35ms) antes del primer offset.
ANTICIPO_PRE_S = abs(min(OFFSETS_PRE_S)) + 6
STAKE_REF_EUR = 1.05
ASK_MIN, ASK_MAX = 0.05, 0.95

COLUMNS = [
    "timestamp_utc", "activo", "marco", "slug", "market_id", "condition_id",
    "ts_end", "offset_s", "direccion_implicita", "ask_implicita",
    "profundidad_eur", "ratio_vs_stake", "mejor_ask", "n_niveles",
]


def _log(msg: str):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _guardar(filas: list):
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        for fila in filas:
            w.writerow([fila.get(c, "") for c in COLUMNS])


def observar_ventana(asset: str, ts_end: int):
    ts_start = ts_end - DUR_S
    slug, mkt = mercado_slot(asset, MARCO_TAG, ts_start)
    if not mkt:
        return []
    market_id = mkt.get("id", "")
    condition_id = mkt.get("conditionId", "")
    token_yes, token_no = token_ids(mkt)
    if not token_yes or not token_no:
        return []
    ref_open = _TAIL.precio_en(asset, ts_start) or _TAIL.precio_en(asset, ts_start + 2)

    filas = []
    for offset in OFFSETS_PRE_S:
        objetivo = ts_end + offset
        espera = objetivo - time.time()
        if espera > 0:
            time.sleep(espera)

        precio = _TAIL.precio_ultimo(asset)
        if precio is None or ref_open is None or ref_open <= 0:
            continue
        if precio > ref_open:
            dir_impl = "Up"
        elif precio < ref_open:
            dir_impl = "Down"
        else:
            continue

        ask_yes, ask_no, _, _ = libro(token_yes, token_no)
        ask_impl = ask_yes if dir_impl == "Up" else ask_no
        if ask_impl is None or not (ASK_MIN <= ask_impl <= ASK_MAX):
            continue  # no accionable -- ya obvio o sin dato, no gastar la consulta de profundidad

        token_impl = token_yes if dir_impl == "Up" else token_no
        depth = lt._consultar_profundidad_libro(None, token_impl, ask_impl, STAKE_REF_EUR)

        filas.append({
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "activo": asset, "marco": MARCO, "slug": slug,
            "market_id": market_id, "condition_id": condition_id,
            "ts_end": ts_end, "offset_s": offset,
            "direccion_implicita": dir_impl, "ask_implicita": ask_impl,
            "profundidad_eur": depth.get("profundidad_eur", ""),
            "ratio_vs_stake": depth.get("ratio_vs_stake", ""),
            "mejor_ask": depth.get("mejor_ask", ""),
            "n_niveles": depth.get("n_niveles", ""),
        })
        _log(f"[{asset}] ts_end={ts_end} offset={offset} dir={dir_impl}@{ask_impl} "
             f"profundidad={depth.get('profundidad_eur')} ratio={depth.get('ratio_vs_stake')}")
    return filas


def worker(asset: str):
    while True:
        now = time.time()
        ts_end = (int(now) // DUR_S + 1) * DUR_S
        despertar = ts_end - ANTICIPO_PRE_S
        resto = despertar - time.time()
        if resto > 0:
            time.sleep(resto)
        try:
            filas = observar_ventana(asset, ts_end)
            _guardar(filas)
        except Exception as e:
            _log(f"[{asset}] error en ventana ts_end={ts_end}: {e}")
        resto2 = ts_end + max(OFFSETS_PRE_S) + 2 - time.time()
        if resto2 > 0:
            time.sleep(resto2)


def main():
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    _log(f"resolution_sniper_precierre_depth_fase0 arrancado — activos={ASSETS} "
         f"marco={MARCO} offsets={OFFSETS_PRE_S}")
    with ThreadPoolExecutor(max_workers=len(ASSETS)) as ex:
        for asset in ASSETS:
            ex.submit(worker, asset)
        while True:
            time.sleep(3600)


if __name__ == "__main__":
    main()
