#!/usr/bin/env python3
"""
candidatas_sin_fillability_depth_fase0.py -- FASE 0 (solo observación) de
profundidad real para candidatas que hoy carecen de CUALQUIER
infraestructura de fill-ability (0 observaciones de libro real,
verificado 25-Ago vía libro_snapshots.csv/ejecutores dedicados):

  FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION#BNB#5min#BUY_YES
  BALLENAS_CONFIRMADAS_15M#DOGE#15min#BUY_YES
  FAVORITO_CONFIRMADO#ETH#60min#BUY_NO

Ampliado 25-Ago tarde con 4 celdas más, encontradas con rigor PROPIO
(gate_bucket_propio.json, no solo externo) al cierre de la sesión --
mismo hueco (0% cobertura de libro real), ver checkpoint
project_checkpoint_cierre_sesion_25ago_tarde:

  WEEKLY_PRICE#ETH#BUY_NO       [0.45,0.50) n=35 pnl/tr=+1.069€ p=0.000
  WEEKLY_PRICE#BTC#BUY_NO       [0.30,0.35) n=28 pnl/tr=+0.457€ p=0.006
  GBM_LATE_5M#XRP#5min#BUY_YES  [0.45,0.50) n=32 pnl/tr=+1.061€ p=0.001
  STREAK_FADE_5M#SOL#5min#BUY_YES [0.45,0.50) n=26 pnl/tr=+0.346€ p=0.006

  OJO WEEKLY_PRICE: ya refutado 2 veces por fill-ability real (28-Jul
  0% vía trades API; 20-Ago 2.1% pese a hit=96.3%) -- probable que
  también falle aquí, pero se mide con datos frescos, no se asume.

Las 7 tienen zonas de precio confirmadas con rigor propio o externo
(`zonas_validadas_externas.json`, ballenas_timing_history.csv, n en
cientos/miles) pero ninguna tiene ejecutor de baja latencia propio ni
está cubierta por los depth-fase0 existentes (favorito_confirmado_
depth_fase0.py = solo BTC/SOL; ballenas_confirmadas_15m_buyno_depth_
fase0.py = solo BUY_NO; favorito_confirmado_60_240min_depth_fase0.py =
solo ETH#60min#BUY_YES, no BUY_NO) -- hueco real encontrado al intentar
promocionarlas.

Mismo mecanismo exacto que momentum_ibs_15m_depth_fase0.py (no
duplicar lógica compartida en un módulo común -- cada fase0 es
self-contained a propósito en este proyecto, mismo criterio que
favorito_confirmado_depth_fase0.py/ballenas_confirmadas_15m_buyno_
depth_fase0.py ya establecido): sigue (tail incremental, por posición
de fichero) `predictions_YYYY-MM-DD.csv` -- el mismo fichero que
shadow_predict.py YA escribe cada ciclo -- y en cuanto aparece una fila
nueva de alguna de las 3 tuplas, consulta el libro público real
(`lt._consultar_profundidad_libro`, solo lectura, nunca ordena) del
lado exacto que se compraría. NO escribe nada en predictions.csv/
results.csv -- CSV propio aparte, no contamina el aprendizaje causal.

Ninguna de las 3 necesita baja latencia (ninguna depende de "llegar
antes de que el libro reaccione a una ballena activa", a diferencia de
MOMENTUM_IBS_*_BALLENA/BALLENAS_TARDIAS) -- medir la profundidad justo
después del ciclo normal (~20-40s) es representativo de cómo operarían
si se promocionan vía el camino genérico.

NO coloca, cancela ni modifica ninguna orden real.

Se fusiona en observadores_fase0.py (screen "observadores") -- NUNCA
lanzar una screen suelta para este script.
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

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "candidatas_sin_fillability_depth_fase0.csv"
VISTOS_PATH = DIR_SHADOW / "candidatas_sin_fillability_depth_fase0_vistos.json"

# (strategy, activo, decision) -- ampliable si aparecen más candidatas
# confirmadas externamente sin infraestructura de fill-ability propia.
TUPLAS = [
    ("FAVORITO_CONFIRMADO_5MIN_ALTACONVICCION", "BNB", "BUY_YES"),
    ("BALLENAS_CONFIRMADAS_15M", "DOGE", "BUY_YES"),
    ("FAVORITO_CONFIRMADO", "ETH", "BUY_NO"),
    ("WEEKLY_PRICE", "ETH", "BUY_NO"),
    ("WEEKLY_PRICE", "BTC", "BUY_NO"),
    ("GBM_LATE_5M", "XRP", "BUY_YES"),
    ("STREAK_FADE_5M", "SOL", "BUY_YES"),
]
_CLAVES = {(s, a, d) for s, a, d in TUPLAS}

STAKE_REFERENCIA_EUR = 1.05
POLL_S = 15

COLUMNS = ["ts_deteccion_utc", "ts_prediccion_utc", "market_id", "strategy",
           "activo", "decision", "precio_yes_mercado", "mejor_ask_deteccion",
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


def _archivo_hoy() -> Path:
    return DIR_SHADOW / f"predictions_{datetime.now(timezone.utc).date().isoformat()}.csv"


def _procesar_fila(row: dict, vistos: set) -> dict | None:
    strategy = row.get("strategy", "")
    decision = row.get("decision", "")
    subtype = row.get("subtype", "")
    activo = subtype.split("#", 1)[0] if "#" in subtype else subtype
    clave = (strategy, activo, decision)
    if clave not in _CLAVES:
        return None
    market_id = row.get("market_id", "")
    dedup_key = f"{market_id}|{strategy}|{decision}"
    if dedup_key in vistos:
        return None
    vistos.add(dedup_key)

    try:
        yes_token, no_token, _ = lt._get_token_ids(market_id)
    except Exception as e:
        _log(f"WARN no se pudo resolver tokens para market_id={market_id}: {e}")
        return None
    token_id = no_token if decision == "BUY_NO" else yes_token

    try:
        py = float(row.get("precio_yes_mercado", ""))
    except (TypeError, ValueError):
        py = 0.5
    precio_entrada = py if decision == "BUY_YES" else (1.0 - py)

    fill = lt._consultar_profundidad_libro(None, token_id, precio_entrada, STAKE_REFERENCIA_EUR)
    return {
        "ts_deteccion_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "ts_prediccion_utc": row.get("timestamp_utc", ""),
        "market_id": market_id,
        "strategy": strategy,
        "activo": activo,
        "decision": decision,
        "precio_yes_mercado": py,
        "mejor_ask_deteccion": fill.get("mejor_ask") if fill.get("ok") else "",
        "profundidad_eur_deteccion": fill.get("profundidad_eur") if fill.get("ok") else "",
        "ratio_vs_stake_deteccion": fill.get("ratio_vs_stake") if fill.get("ok") else "",
    }


def main() -> None:
    _log(f"arrancado -- vigilando {TUPLAS}")
    vistos = _vistos_cargar()

    # Backlog del día ya escrito antes de arrancar: se marca como visto
    # SIN consultar libro (fill-ability es del instante de detección, no
    # reconstruible retroactivamente -- mismo criterio que el resto de
    # observadores fase0 del proyecto).
    archivo = _archivo_hoy()
    posicion = 0
    if archivo.exists():
        with open(archivo, encoding="utf-8") as f:
            header = f.readline()
            cabecera = next(csv.reader([header]))
            nuevos = 0
            for row in csv.DictReader(f, fieldnames=cabecera):
                strategy = row.get("strategy", "")
                decision = row.get("decision", "")
                subtype = row.get("subtype", "")
                activo = subtype.split("#", 1)[0] if "#" in subtype else subtype
                if (strategy, activo, decision) in _CLAVES:
                    vistos.add(f"{row.get('market_id','')}|{strategy}|{decision}")
                    nuevos += 1
            posicion = f.tell()
        _log(f"backlog de hoy marcado como visto sin consultar libro: {nuevos} señales")
    _vistos_guardar(vistos)

    archivo_actual = archivo
    cabecera = None
    while True:
        try:
            hoy = _archivo_hoy()
            if hoy != archivo_actual:
                archivo_actual = hoy
                posicion = 0
                cabecera = None

            if not archivo_actual.exists():
                time.sleep(POLL_S)
                continue

            filas_nuevas = []
            with open(archivo_actual, encoding="utf-8") as f:
                if cabecera is None:
                    f.seek(0)
                    header_line = f.readline()
                    cabecera = next(csv.reader([header_line]))
                    if posicion == 0:
                        posicion = f.tell()
                f.seek(posicion)
                nuevas_lineas = f.readlines()
                posicion = f.tell()

            for linea in nuevas_lineas:
                try:
                    row = next(csv.DictReader([linea], fieldnames=cabecera))
                except Exception:
                    continue
                resultado = _procesar_fila(row, vistos)
                if resultado:
                    filas_nuevas.append(resultado)
                    _log(f"NUEVA deteccion: {resultado['strategy']}#{resultado['activo']}#"
                         f"{resultado['decision']} py={resultado['precio_yes_mercado']} "
                         f"profundidad={resultado['profundidad_eur_deteccion']}")

            if filas_nuevas:
                _guardar(filas_nuevas)
                _vistos_guardar(vistos)

        except Exception as e:
            _log(f"WARN ciclo fallido: {type(e).__name__}: {e}")

        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
