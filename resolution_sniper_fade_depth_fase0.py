#!/usr/bin/env python3
"""
resolution_sniper_fade_depth_fase0.py — FASE 0 (SOLO OBSERVACIÓN), 14-Ago.

Hallazgo del día (análisis ad-hoc sobre resolution_sniper_obs_*.csv,
10-14-Ago, sin filtrar profundidad): en el subconjunto "accionable" de
resolution_sniper_observer.py (ask del lado que la `chainlink_direccion_
implicita` señala, todavía NO obvio, en [0.05,0.95]) esa dirección
implícita acierta solo 17.1% (n=123) -- mucho peor que el azar. FADEANDO
esa dirección (comprando el lado contrario): n=90 (excluidos 2 outliers
ask<0.05), hit=80.0%, EV/trade=+0.058€, shuffle p=0.0000, mejor cuanto
más cerca del cierre real (offset>=0: 87-88% hit). Ver memoria
idea_resolution_sniper_fade_hallazgo_14ago.

PERO resolution_sniper_obs_*.csv NO tiene columna de profundidad --
ask_yes/ask_no son solo el mejor precio, no si hay tamaño real detrás.
Mismo cuello de botella que TODO lo demás este mes (P32/P33/GBM_LATE
fade): un precio barato no implica que se pueda comprar de verdad. Este
observador mide profundidad real del lado FADE en el instante exacto
donde el análisis de arriba encontró el edge (offset 0-3s post-cierre),
antes de proponer ningún ejecutor.

Mecanismo (mismo patrón que gbmlate_fade_depth_fase0.py / p33_maker_
fillability_fase0.py -- reusa `lt._consultar_profundidad_libro`, solo
lectura, nunca ordena; y reusa el tail de Chainlink + descubrimiento de
mercado de resolution_sniper_observer.py, decisión ladder CLAUDE.md: no
duplicar código ya existente):
  1. Un hilo por (activo,marco) de los 6x2 ya cubiertos por
     resolution_sniper_observer.py, mismo reloj de ventanas.
  2. En offsets [0,1,2,3] tras el cierre nominal, calcula
     chainlink_direccion_implicita igual que el observador original
     (precio Chainlink actual vs precio de apertura de la ventana).
  3. Si el ask del lado implícito está en [0.05,0.95] (la señal
     "accionable", no obvia todavía) -- consulta profundidad real del
     lado FADE (el contrario) vía `lt._consultar_profundidad_libro`,
     con stake de referencia 1.05€ (suelo real del proyecto).
  4. Persiste en data/shadow/resolution_sniper_fade_depth_fase0.csv:
     identidad de la señal, dirección implícita/fade, ask de ambos
     lados, profundidad/ratio del lado fade. Cruce posterior con
     outcome_real (join market_id contra resolution_sniper_obs_*.csv,
     que sí lo resuelve) responde si el fade es ejecutable de verdad.

NO coloca, cancela ni modifica ninguna orden real -- puramente
observacional, mismo criterio de riesgo que el resto de *_fase0.py.

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
    ASSETS, TIMEFRAMES, DESPERTAR_ANTICIPO_S, _TAIL,
    mercado_slot, token_ids, libro,
)
# 19-Ago: fusionado con resolution_sniper_naive_depth_fase0.py -- ambos
# observadores consultaban la MISMA ventana/mercado en el MISMO instante
# (mismos offsets 0-3s, mismo ts_end), cada uno con su propio hilo/pool de
# 12 workers -- CPU sobresuscrita real (py-spy: 85 hilos vivos en
# observadores_fase0.py, load5/nproc>2.9x, swap activo en vivo). Se fusiona
# en un único paso: 1 descubrimiento de mercado + 1 libro() por offset
# (antes 2 de cada), consultando profundidad de AMBOS lados (fade e
# implícito) en la misma iteración -- ahorra ~12 hilos y ~40-50% de
# llamadas API de esta familia. Los 2 CSV de salida y sus columnas NO
# cambian (compatibilidad con los gates ya escritos hoy).
import resolution_sniper_naive_depth_fase0 as _naive
import resolution_sniper_naive_executor_dryrun as _naive_exec

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "resolution_sniper_fade_depth_fase0.csv"

OFFSETS_FADE_S = [0, 1, 2, 3]  # donde el hit-rate del fade fue más fuerte (87-88%)
STAKE_REF_EUR = 1.05  # suelo real del proyecto (CLOB min size)
ASK_MIN, ASK_MAX = 0.05, 0.95  # subconjunto "accionable" (no obvio)

COLUMNS = [
    "timestamp_utc", "activo", "marco", "slug", "market_id", "condition_id",
    "ts_end", "offset_s", "direccion_implicita", "ask_implicita",
    "direccion_fade", "ask_fade", "profundidad_fade_eur", "ratio_fade_vs_stake",
    "mejor_ask_fade", "n_niveles_fade",
]


def _log(msg: str):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _csv_path() -> Path:
    return DIR_SHADOW / f"resolution_sniper_fade_depth_fase0.csv"


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


def observar_ventana(asset: str, marco: str, dur_s: int, marco_tag: str, ts_end: int):
    ts_start = ts_end - dur_s
    slug, mkt = mercado_slot(asset, marco_tag, ts_start)
    if not mkt:
        return [], []
    market_id = mkt.get("id", "")
    condition_id = mkt.get("conditionId", "")
    token_yes, token_no = token_ids(mkt)
    if not token_yes or not token_no:
        return [], []
    ref_open = _TAIL.precio_en(asset, ts_start) or _TAIL.precio_en(asset, ts_start + 2)

    filas = []
    filas_naive = []
    for offset in OFFSETS_FADE_S:
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

        dir_fade = "Down" if dir_impl == "Up" else "Up"
        token_fade = token_no if dir_fade == "Down" else token_yes
        ask_fade = ask_no if dir_fade == "Down" else ask_yes
        token_impl = token_yes if dir_impl == "Up" else token_no

        depth = lt._consultar_profundidad_libro(None, token_fade, ask_fade or 0.5, STAKE_REF_EUR)
        depth_impl = lt._consultar_profundidad_libro(None, token_impl, ask_impl or 0.5, STAKE_REF_EUR)

        filas_naive.append({
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "activo": asset, "marco": marco, "slug": slug,
            "market_id": market_id, "condition_id": condition_id,
            "ts_end": ts_end, "offset_s": offset,
            "direccion_implicita": dir_impl, "ask_implicita": ask_impl,
            "profundidad_implicita_eur": depth_impl.get("profundidad_eur", ""),
            "ratio_implicita_vs_stake": depth_impl.get("ratio_vs_stake", ""),
            "mejor_ask_implicita": depth_impl.get("mejor_ask", ""),
            "n_niveles_implicita": depth_impl.get("n_niveles", ""),
        })

        filas.append({
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "activo": asset, "marco": marco, "slug": slug,
            "market_id": market_id, "condition_id": condition_id,
            "ts_end": ts_end, "offset_s": offset,
            "direccion_implicita": dir_impl, "ask_implicita": ask_impl,
            "direccion_fade": dir_fade, "ask_fade": ask_fade if ask_fade is not None else "",
            "profundidad_fade_eur": depth.get("profundidad_eur", ""),
            "ratio_fade_vs_stake": depth.get("ratio_vs_stake", ""),
            "mejor_ask_fade": depth.get("mejor_ask", ""),
            "n_niveles_fade": depth.get("n_niveles", ""),
        })
        _log(f"[{asset}#{marco}] ts_end={ts_end} offset={offset} "
             f"implicita={dir_impl}@{ask_impl} (ratio={depth_impl.get('ratio_vs_stake')}) "
             f"fade={dir_fade}@{ask_fade} (ratio={depth.get('ratio_vs_stake')})")

        try:
            _naive_exec.evaluar(
                asset, marco, slug, market_id, condition_id, ts_end, offset,
                dir_impl, ask_impl, token_impl, depth_impl.get("ratio_vs_stake"),
                libro, token_yes, token_no,
            )
        except Exception as e:
            _log(f"[{asset}#{marco}] error en executor_dryrun offset={offset}: {e}")
    return filas, filas_naive


def worker(asset: str, marco: str, dur_s: int, marco_tag: str):
    while True:
        now = time.time()
        ts_end = (int(now) // dur_s + 1) * dur_s
        despertar = ts_end - DESPERTAR_ANTICIPO_S
        resto = despertar - time.time()
        if resto > 0:
            time.sleep(resto)
        try:
            filas, filas_naive = observar_ventana(asset, marco, dur_s, marco_tag, ts_end)
            _guardar(filas)
            _naive._guardar(filas_naive)
        except Exception as e:
            _log(f"[{asset}#{marco}] error en ventana ts_end={ts_end}: {e}")
        resto2 = ts_end + max(OFFSETS_FADE_S) + 1 - time.time()
        if resto2 > 0:
            time.sleep(resto2)


def main():
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    _log(f"resolution_sniper_fade_depth_fase0 arrancado — activos={ASSETS} "
         f"marcos={list(TIMEFRAMES)} offsets={OFFSETS_FADE_S}")
    with ThreadPoolExecutor(max_workers=len(ASSETS) * len(TIMEFRAMES)) as ex:
        for asset in ASSETS:
            for marco, (dur_s, tag) in TIMEFRAMES.items():
                ex.submit(worker, asset, marco, dur_s, tag)
        while True:
            time.sleep(3600)


if __name__ == "__main__":
    main()
