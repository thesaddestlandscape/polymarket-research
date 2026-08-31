#!/usr/bin/env python3
"""
huecos_extremos_fase0.py -- FASE 0 (solo observación) de fill-ability real
en los 4 huecos de cobertura encontrados 31-Ago vía
analisis_franja_milimetrica_ballenas.py: zona de precio [0.95,1.00) en
(activo,marco) donde las ballenas muestran edge brutal y limpio
(hit>=97%, miles de mercados, sin concentración) pero nuestras propias
estrategias casi nunca predicen ahí (shadow_n=1-8):

  BTC#15min  [0.95,1.00)  ballenas hit=98.5% n=28734 (462 mercados, top1=1%)
  XRP#15min  [0.95,1.00)  ballenas hit=97.7% n=4011  (459 mercados, top1=1%)
  BTC#60min  [0.95,1.00)  ballenas hit=98.5% n=12959 (232 mercados, top1=2%)
  ETH#60min  [0.95,1.00)  ballenas hit=98.4% n=7342  (233 mercados, top1=2%)

A diferencia de los fase0 "candidatas_sin_fillability_depth" (que
disparan sobre una FILA de predictions.csv de una estrategia concreta),
aquí no hay estrategia que dispare -- es la zona de precio del propio
MERCADO la que importa, independientemente de si alguna estrategia
predijo ahí. Por eso este observador ESCANEA el universo activo
(reusa fetch_libro_ambos_lados._universo_activo(), ya cacheado 15s) en
vez de seguir predictions.csv.

Mecanismo: cada POLL_S segundos, para cada mercado del universo en los 4
(activo,marco) de arriba, consulta el mejor ask YES/NO (barato, público).
Si algún lado cruza a >=UMBRAL_EXTREMO (0.95), consulta profundidad real
del libro en ESE lado (lt._consultar_profundidad_libro, solo lectura,
nunca ordena) y registra. Dedup por (market_id, lado) con vistos.json,
mismo patrón que el resto de fase0 -- una vez capturado un mercado en un
lado, no se vuelve a consultar profundidad para él (el mercado ya "vive"
en la zona extrema, capturar una vez basta para medir fill-ability).

NO coloca, cancela ni modifica ninguna orden real. NO conectado a ningún
ejecutor -- puramente exploratorio, alimenta una decisión futura de
promoción solo cuando haya n suficiente con rigor (n>=15, luego n>=40).

Se fusiona en observadores_fase0.py (screen "observadores") -- NUNCA
lanzar una screen suelta para este script (mismo criterio que el resto
de fase0 del proyecto, ver CLAUDE.md pt.13 -- costoso reservar CPU/screen
para algo tan barato).
"""
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import live_trade as lt  # noqa: E402
import fetch_libro_ambos_lados as fla  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "huecos_extremos_fase0.csv"
VISTOS_PATH = DIR_SHADOW / "huecos_extremos_fase0_vistos.json"

OBJETIVOS = {("BTC", "15min"), ("XRP", "15min"), ("BTC", "60min"), ("ETH", "60min")}
UMBRAL_EXTREMO = 0.95
STAKE_REFERENCIA_EUR = 1.05
POLL_S = 30  # mercados ya casi decididos, sin urgencia de baja latencia (ver docstring)

COLUMNS = ["ts_deteccion_utc", "market_id", "condition_id", "activo", "marco",
           "restante_s", "lado", "ask_lado", "mejor_ask_deteccion",
           "profundidad_eur_deteccion", "ratio_vs_stake_deteccion"]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-20000:]), encoding="utf-8")


def _guardar(filas: list) -> None:
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        for fila in filas:
            w.writerow([fila.get(c, "") for c in COLUMNS])


def _procesar_mercado(mid: str, activo: str, marco: str, condition_id: str, edt, vistos: set) -> list:
    filas = []
    try:
        yes_token, no_token, cid_real = lt._get_token_ids(mid)
    except Exception:
        return filas
    book_yes = lt._fetch_book_publico(yes_token)
    book_no = lt._fetch_book_publico(no_token)
    ask_yes = fla._mejor_ask(book_yes)
    ask_no = fla._mejor_ask(book_no)
    ahora = datetime.now(timezone.utc)
    restante_s = round((edt - ahora).total_seconds(), 1)

    for lado, ask, token in (("YES", ask_yes, yes_token), ("NO", ask_no, no_token)):
        if ask is None or ask < UMBRAL_EXTREMO:
            continue
        dedup_key = f"{mid}|{lado}"
        if dedup_key in vistos:
            continue
        vistos.add(dedup_key)
        fill = lt._consultar_profundidad_libro(None, token, ask, STAKE_REFERENCIA_EUR)
        filas.append({
            "ts_deteccion_utc": ahora.isoformat(timespec="seconds"),
            "market_id": mid,
            "condition_id": cid_real or condition_id,
            "activo": activo,
            "marco": marco,
            "restante_s": restante_s,
            "lado": lado,
            "ask_lado": ask,
            "mejor_ask_deteccion": fill.get("mejor_ask") if fill.get("ok") else "",
            "profundidad_eur_deteccion": fill.get("profundidad_eur") if fill.get("ok") else "",
            "ratio_vs_stake_deteccion": fill.get("ratio_vs_stake") if fill.get("ok") else "",
        })
        _log(f"🎯 {activo}#{marco} {lado}@{ask:.3f} restante={restante_s}s "
             f"ratio_vs_stake={fill.get('ratio_vs_stake') if fill.get('ok') else 'ERR'}")
    return filas


def main() -> None:
    _log(f"arrancado -- vigilando {sorted(OBJETIVOS)} zona [{UMBRAL_EXTREMO},1.00)")
    vistos = _vistos_cargar()
    while True:
        try:
            universo = fla._universo_activo()
            filas_nuevas = []
            for mid, (activo, marco, condition_id, edt) in universo.items():
                if (activo, marco) not in OBJETIVOS:
                    continue
                filas_nuevas.extend(_procesar_mercado(mid, activo, marco, condition_id, edt, vistos))
            if filas_nuevas:
                _guardar(filas_nuevas)
                _vistos_guardar(vistos)
        except Exception as e:
            _log(f"ERROR ciclo: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
