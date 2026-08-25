#!/usr/bin/env python3
"""
momentum_ibs_15m_depth_fase0.py -- FASE 0 (solo observación) de
profundidad real para MOMENTUM_IBS_15M#BNB#15min#BUY_NO.

Origen (25-Ago, petición explícita Javi): `gate_bucket_propio.py`
confirmó con rigor propio el bucket [0.45,0.50) (n=21, pnl/tr=+0.574€,
shuffle p=0.022), pero la tupla es candidato (no está en
`pares_permitidos_live`) -- nunca pasa por la consulta real al libro que
sí hace `live_trade.py` para tuplas live, así que la fill-ability es
desconocida (0% de las señales tienen dato de libro real, verificado
25-Ago). A diferencia de MOMENTUM_IBS_5M_BALLENA/MOMENTUM_IBS_15M_BALLENA
(que SÍ tienen ejecutor de baja latencia dedicado, momentum_ibs_ballena_
executor.py, 17-Ago -- consultado directamente para SOL#5min#BUY_YES, ya
tenía 61/62 señales con profundidad real verificada), MOMENTUM_IBS_15M
(variante SIN gate de ballena) no lo tiene.

Por qué NO se replica el patrón de polling agresivo de momentum_ibs_
ballena_executor.py: esa variante necesita baja latencia porque su edge
depende de "llegar antes de que el libro reaccione a una ballena ya
activa" (ver idea_momentum_gateado_por_ballenas_hallazgo_central_17ago).
MOMENTUM_IBS_15M plano no tiene ese mecanismo -- su edge (si lo tiene)
sería el mismo si se ejecutara vía el ciclo normal de shadow_predict.py
(~20-40s) que si se ejecutara con latencia perfecta, así que medir la
profundidad justo después del ciclo normal (mismo cadencia con la que
operaría en producción si se promociona) es representativo, no un sesgo
de medición -- no hace falta duplicar el cálculo de la señal.

Mecanismo: sigue (tail incremental, por posición de fichero, mismo
patrón que bot_wallets_gate_bucket_fase0.py) `predictions_YYYY-MM-DD.csv`
-- el mismo fichero que shadow_predict.py YA escribe cada ciclo -- y en
cuanto aparece una fila nueva de MOMENTUM_IBS_15M#BNB#15min#BUY_NO,
consulta el libro público real (`lt._consultar_profundidad_libro`, solo
lectura, nunca ordena) del token "No" de ese market_id
(`lt._get_token_ids`, ya validado contra `outcomes` en vez de asumir
orden). NO escribe nada en predictions.csv/results.csv -- CSV propio
aparte, no contamina el aprendizaje causal de la estrategia real.

Generalizable a otros activos/buckets de MOMENTUM_IBS_15M si hiciera
falta más adelante -- hoy limitado a BNB#15min#BUY_NO (única celda
confirmada con rigor hasta ahora), ver TUPLAS abajo.

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
OUT = DIR_SHADOW / "momentum_ibs_15m_depth_fase0.csv"
VISTOS_PATH = DIR_SHADOW / "momentum_ibs_15m_depth_fase0_vistos.json"

# (strategy, activo, decision) -- ampliable, hoy solo la celda confirmada.
TUPLAS = [
    ("MOMENTUM_IBS_15M", "BNB", "BUY_NO"),
]

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
    if clave not in {(s, a, d) for s, a, d in TUPLAS}:
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
    activos = sorted({a for _, a, _ in TUPLAS})
    _log(f"arrancado -- vigilando {TUPLAS} ({len(activos)} activo(s))")
    vistos = _vistos_cargar()

    # Backlog del día ya escrito antes de arrancar: se marca como visto
    # SIN consultar libro (mismo motivo que bot_wallets_gate_bucket_fase0.py
    # -- fill-ability es del instante de detección, no reconstruible).
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
                if (strategy, activo, decision) in {(s, a, d) for s, a, d in TUPLAS}:
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
