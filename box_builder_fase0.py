#!/usr/bin/env python3
"""
box_builder_fase0.py — FASE 0, solo observación. Detector de arbitraje
estructural YES+NO (comprar ambos lados cuando la suma, tras comisión,
garantiza beneficio vía MERGE) -- P29 backlog, Stage 4 del plan
escalonado (motor no correlacionado con nuestras estrategias direccionales
actuales, ver project_plan_escalonado_200k_23jul en memoria).

Origen (30-Jul, petición explícita Javi -- "busca lo evidente y lo no
evidente... ahí está la clave"): investigación con wallets reales
(idea_arbitraje_yes_no_wallets_expertas_30jul) confirmó el mecanismo
(wallet 0x643b696d: 19/22 mercados compra ambos lados, 20/22 con MERGE)
y dos correcciones NO evidentes:

1. El umbral de rentabilidad real NO es "ask_yes+ask_no < 1.00" (heurística
   ingenua) -- la comisión taker (7%, cobrada SIEMPRE al comprar, incluso
   si pierdes -- confirmado con dinero real en un trade recuperado hoy)
   se paga en CADA pata. Umbral real ~0.95-0.96, no 1.00. Este script usa
   la fórmula exacta: ganancia_neta = 1 - (ask_yes+ask_no) -
   0.07*(ask_yes*(1-ask_yes) + ask_no*(1-ask_no)).

2. La ventana de oportunidad es CORTA (wallets reales: mediana 49s entre
   comprar un lado y el otro) -- verificado retrospectivamente contra nuestra
   propia captura de libro cada 45s (fetch_libro_ambos_lados.py, screen
   `libroambos`, en producción desde 28-Jul): de 250.960 snapshots en 2
   días, solo 8 (0.003%) muestran una oportunidad rentable tras fee -- la
   captura de 45s es DEMASIADO LENTA para verlas, no porque no existan
   (los datos de wallets reales confirman que sí ocurren) sino porque el
   hueco se abre y cierra en segundos.

Este script NO sustituye a fetch_libro_ambos_lados.py (que sigue cubriendo
TODO el universo cada 45s, barato). En vez de vigilar rápido TODO el
universo (185-191 mercados, ~380 peticiones/ciclo -- caro e ineficiente,
la mayoría lejos de cerrar no importa), vigila cada
POLL_INTERVAL_S=3s SOLO los mercados dentro de la ventana caliente
(restante_s < VENTANA_CALIENTE_S) -- normalmente 10-20 mercados a la vez,
carga acotada. Los tokens de cada mercado se cachean (no hay razón para
repetir la llamada a gamma-api cada 3s, no cambian en la vida del mercado).

NO coloca ni cancela ninguna orden real -- solo lee libros públicos y
registra. ⚠️ 05-Ago: fusionado dentro de observadores_fase0.py (screen
"observadores"), NO tiene screen propia -- corre como hilo. NUNCA lanzar
`screen -dmS boxbuilder ...` suelto: duplica el proceso. Ver
observadores_fase0.py y pipeline_watchdog.py::SCREENS_RETIRADAS.
"""

import csv
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt  # solo lectura: _get_token_ids, _fetch_book_publico, _consultar_profundidad_libro
from fetch_libro_ambos_lados import _universo_activo  # reusa el descubrimiento de universo ya en producción

DIR = Path(__file__).resolve().parent
DIR_SHADOW = DIR / "data" / "shadow"
OUT_CSV = DIR_SHADOW / "box_builder_fase0.csv"

POLL_INTERVAL_S = 3.0
VENTANA_CALIENTE_S = 180.0  # solo mercados a <3min del cierre -- ver docstring
MARGEN_SEGURIDAD = 0.005  # 30-Jul: exigir ganancia_neta > 0.5% del nocional
# (no solo >0), para absorber slippage/latencia entre detectar y ejecutar --
# la ganancia teórica se calcula con el best-ask del instante de la lectura,
# que puede haberse movido para cuando (si algún día) se llegara a ejecutar.

STAKE_REF_EUR = 1.05  # mismo suelo/referencia que el resto de ejecutores del proyecto

COLUMNS = [
    "timestamp_utc", "market_id", "condition_id", "activo", "marco",
    "restante_s", "ask_yes", "ask_no", "ask_sum",
    "ganancia_neta_por_share", "profundidad_yes_eur", "profundidad_no_eur",
    "ratio_yes_vs_stake", "ratio_no_vs_stake",
]

_tokens_cache: dict[str, tuple[str, str]] = {}  # market_id -> (yes_token, no_token)


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _tokens_de(mid: str) -> tuple[str, str] | None:
    if mid in _tokens_cache:
        return _tokens_cache[mid]
    try:
        yes_token, no_token, _cid = lt._get_token_ids(mid)
    except Exception:
        return None
    _tokens_cache[mid] = (yes_token, no_token)
    return (yes_token, no_token)


def _fee(p: float) -> float:
    return 0.07 * (1.0 - p)


def _ganancia_neta_por_share(ask_yes: float, ask_no: float) -> float:
    return 1.0 - (ask_yes + ask_no) - (_fee(ask_yes) * ask_yes + _fee(ask_no) * ask_no)


def _revisar_mercado(mid: str, activo: str, marco: str, cid: str, restante_s: float) -> dict | None:
    tokens = _tokens_de(mid)
    if tokens is None:
        return None
    yes_token, no_token = tokens
    with ThreadPoolExecutor(max_workers=2) as ex:
        f_yes = ex.submit(lt._fetch_book_publico, yes_token)
        f_no = ex.submit(lt._fetch_book_publico, no_token)
        book_yes = f_yes.result()
        book_no = f_no.result()
    ask_yes = _mejor_ask(book_yes)
    ask_no = _mejor_ask(book_no)
    if ask_yes is None or ask_no is None:
        return None
    ganancia = _ganancia_neta_por_share(ask_yes, ask_no)
    if ganancia <= MARGEN_SEGURIDAD:
        return None

    # Solo se consulta profundidad real (llamadas extra) cuando YA hay
    # oportunidad -- barato el caso común (sin oportunidad), completo el raro.
    with ThreadPoolExecutor(max_workers=2) as ex:
        f_prof_yes = ex.submit(lt._consultar_profundidad_libro, None, yes_token, ask_yes, STAKE_REF_EUR)
        f_prof_no = ex.submit(lt._consultar_profundidad_libro, None, no_token, ask_no, STAKE_REF_EUR)
        prof_yes = f_prof_yes.result()
        prof_no = f_prof_no.result()

    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "market_id": mid, "condition_id": cid, "activo": activo, "marco": marco,
        "restante_s": round(restante_s, 1),
        "ask_yes": ask_yes, "ask_no": ask_no, "ask_sum": round(ask_yes + ask_no, 4),
        "ganancia_neta_por_share": round(ganancia, 4),
        "profundidad_yes_eur": prof_yes.get("profundidad_eur", "") if prof_yes.get("ok") else "",
        "profundidad_no_eur": prof_no.get("profundidad_eur", "") if prof_no.get("ok") else "",
        "ratio_yes_vs_stake": prof_yes.get("ratio_vs_stake", "") if prof_yes.get("ok") else "",
        "ratio_no_vs_stake": prof_no.get("ratio_vs_stake", "") if prof_no.get("ok") else "",
    }


def _mejor_ask(book: dict | None) -> float | None:
    if not book:
        return None
    asks = book.get("asks") or []
    mejor = None
    for lvl in asks:
        try:
            p = float(lvl.get("price"))
        except (TypeError, ValueError, AttributeError):
            continue
        if mejor is None or p < mejor:
            mejor = p
    return mejor


def _guardar(filas: list) -> None:
    if not filas:
        return
    nuevo = not OUT_CSV.exists()
    with open(OUT_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)


def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    log(f"box_builder_fase0 arrancado -- poll {POLL_INTERVAL_S}s, ventana caliente {VENTANA_CALIENTE_S}s, "
        f"margen seguridad {MARGEN_SEGURIDAD}")
    ultimo_log_resumen = 0.0
    while True:
        t0 = time.time()
        try:
            universo = _universo_activo()
            ahora = datetime.now(timezone.utc)
            calientes = []
            for mid, (activo, marco, cid, edt) in universo.items():
                restante_s = (edt - ahora).total_seconds()
                if 0 < restante_s < VENTANA_CALIENTE_S:
                    calientes.append((mid, activo, marco, cid, restante_s))

            hallazgos = []
            with ThreadPoolExecutor(max_workers=6) as ex:
                futuros = [ex.submit(_revisar_mercado, mid, activo, marco, cid, restante_s)
                           for mid, activo, marco, cid, restante_s in calientes]
                for fut in futuros:
                    r = fut.result()
                    if r:
                        hallazgos.append(r)

            if hallazgos:
                _guardar(hallazgos)
                for h in hallazgos:
                    log(f"🎯 OPORTUNIDAD {h['activo']}#{h['marco']} market={h['market_id']} "
                        f"ask_yes={h['ask_yes']:.3f} ask_no={h['ask_no']:.3f} "
                        f"ganancia_neta={h['ganancia_neta_por_share']:+.4f}/share "
                        f"ratio_yes={h['ratio_yes_vs_stake']} ratio_no={h['ratio_no_vs_stake']} "
                        f"restante={h['restante_s']:.0f}s")

            if t0 - ultimo_log_resumen > 300:  # resumen cada 5min, no cada 3s
                log(f"vigilando {len(calientes)} mercados en ventana caliente "
                    f"(de {len(universo)} en el universo total)")
                ultimo_log_resumen = t0
        except Exception as e:
            log(f"Error en ciclo: {type(e).__name__}: {e}")
        dormir = POLL_INTERVAL_S - (time.time() - t0)
        if dormir > 0:
            time.sleep(dormir)


if __name__ == "__main__":
    main()
