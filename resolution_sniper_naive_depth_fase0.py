#!/usr/bin/env python3
"""
resolution_sniper_naive_depth_fase0.py — FASE 0 (SOLO OBSERVACIÓN), 19-Ago.

Reacción inmediata al gate riguroso de hoy (analisis_gate_riguroso_
resolution_sniper_fade_depth_19ago.py, ver idea_resolution_sniper_fade_
refutado_19ago): el hallazgo de fade del 14-Ago (fadear la dirección
implícita de Chainlink, hit=80%) se REFUTÓ con datos frescos -- el régimen
se invirtió. Restringiendo a >=13-Ago (offset<=2s, ask accionable en
[0.05,0.95]): la dirección NAIVE (NO fade, apostar CON chainlink_
direccion_implicita) acierta 70-100% en las 12 combinaciones (activo,
marco), 9/12 pasan gate riguroso completo (Wilson90+shuffle+split-half+
BH-FDR, p_shuffle<0.05 en las 9, split-half consistente en TODAS las 12).
pnl/tr (sin fee ni profundidad) hasta +0.71€ por cada 1€ de stake.

Nadie sabe todavía si ese precio es EJECUTABLE -- resolution_sniper_fade_
depth_fase0.py solo mide profundidad del lado FADE (contrario), nunca del
lado implícito/naive. Este observador cierra ese hueco: mismo mecanismo
exacto que resolution_sniper_fade_depth_fase0.py (offsets 0-3s, activo/
marco de resolution_sniper_observer.py, `lt._consultar_profundidad_libro`
con stake de referencia 1.05€), pero consulta profundidad del lado
IMPLÍCITO (el que gana), no del contrario.

Decisión ladder (CLAUDE.md): reusa TODO lo de resolution_sniper_fade_
depth_fase0.py salvo qué lado se consulta -- no se duplica lógica de
descubrimiento de mercado / reloj de ventanas / Chainlink tail.

NO coloca, cancela ni modifica ninguna orden real -- puramente
observacional, mismo criterio de riesgo que el resto de *_fase0.py.
Objetivo: acumular n>=40 CON profundidad antes de plantear ningún
ejecutor -- ninguna promoción a pares_permitidos_live sin esto.

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

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "resolution_sniper_naive_depth_fase0.csv"

OFFSETS_S = [0, 1, 2, 3]  # mismo rango accionable que resolution_sniper_fade_depth_fase0
STAKE_REF_EUR = 1.05  # suelo real del proyecto (CLOB min size)
ASK_MIN, ASK_MAX = 0.05, 0.95  # subconjunto "accionable" (no obvio todavía)

COLUMNS = [
    "timestamp_utc", "activo", "marco", "slug", "market_id", "condition_id",
    "ts_end", "offset_s", "direccion_implicita", "ask_implicita",
    "profundidad_implicita_eur", "ratio_implicita_vs_stake",
    "mejor_ask_implicita", "n_niveles_implicita",
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


def observar_ventana(asset: str, marco: str, dur_s: int, marco_tag: str, ts_end: int):
    ts_start = ts_end - dur_s
    slug, mkt = mercado_slot(asset, marco_tag, ts_start)
    if not mkt:
        return []
    market_id = mkt.get("id", "")
    condition_id = mkt.get("conditionId", "")
    token_yes, token_no = token_ids(mkt)
    if not token_yes or not token_no:
        return []
    ref_open = _TAIL.precio_en(asset, ts_start) or _TAIL.precio_en(asset, ts_start + 2)

    filas = []
    for offset in OFFSETS_S:
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
        depth = lt._consultar_profundidad_libro(None, token_impl, ask_impl or 0.5, STAKE_REF_EUR)

        filas.append({
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "activo": asset, "marco": marco, "slug": slug,
            "market_id": market_id, "condition_id": condition_id,
            "ts_end": ts_end, "offset_s": offset,
            "direccion_implicita": dir_impl, "ask_implicita": ask_impl,
            "profundidad_implicita_eur": depth.get("profundidad_eur", ""),
            "ratio_implicita_vs_stake": depth.get("ratio_vs_stake", ""),
            "mejor_ask_implicita": depth.get("mejor_ask", ""),
            "n_niveles_implicita": depth.get("n_niveles", ""),
        })
        _log(f"[{asset}#{marco}] ts_end={ts_end} offset={offset} "
             f"implicita={dir_impl}@{ask_impl} ratio_profundidad={depth.get('ratio_vs_stake')}")
    return filas


def worker(asset: str, marco: str, dur_s: int, marco_tag: str):
    while True:
        now = time.time()
        ts_end = (int(now) // dur_s + 1) * dur_s
        despertar = ts_end - DESPERTAR_ANTICIPO_S
        resto = despertar - time.time()
        if resto > 0:
            time.sleep(resto)
        try:
            filas = observar_ventana(asset, marco, dur_s, marco_tag, ts_end)
            _guardar(filas)
        except Exception as e:
            _log(f"[{asset}#{marco}] error en ventana ts_end={ts_end}: {e}")
        resto2 = ts_end + max(OFFSETS_S) + 1 - time.time()
        if resto2 > 0:
            time.sleep(resto2)


def main():
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    _log(f"resolution_sniper_naive_depth_fase0 arrancado — activos={ASSETS} "
         f"marcos={list(TIMEFRAMES)} offsets={OFFSETS_S}")
    with ThreadPoolExecutor(max_workers=len(ASSETS) * len(TIMEFRAMES)) as ex:
        for asset in ASSETS:
            for marco, (dur_s, tag) in TIMEFRAMES.items():
                ex.submit(worker, asset, marco, dur_s, tag)
        while True:
            time.sleep(3600)


if __name__ == "__main__":
    main()
