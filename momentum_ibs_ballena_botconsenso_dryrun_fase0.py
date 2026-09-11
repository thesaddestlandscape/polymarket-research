#!/usr/bin/env python3
"""
momentum_ibs_ballena_botconsenso_dryrun_fase0.py — 09-Sep, DRY_RUN puro,
petición explícita Javi: "analiza si mejora todas las tuplas y monedas de
esta familia conectarlo a bot consenso, si es así, lo dejamos unos días
en dry-run corriendo para ver en un par de días los resultados".

Hallazgo (rigor completo: n≥3 votos, split-half, bootstrap CI90%, las 6
monedas × 2 marcos): NO mejora de forma uniforme -- solo 3 de 12
combinaciones sobreviven (CI90% no cruza cero, split-half consistente):
  MOMENTUM_IBS_5M_BALLENA#SOL   (n=526, pnl/tr=+0.206€, CI90=[0.054,0.380])
  MOMENTUM_IBS_15M_BALLENA#SOL  (n=176, pnl/tr=+0.314€, CI90=[0.069,0.618])
  MOMENTUM_IBS_15M_BALLENA#BNB  (n=119, pnl/tr=+0.279€, CI90=[0.097,0.482])
BTC#5min y XRP#15min incluso EMPEORAN (pnl negativo); el resto no
confirma (CI90% cruza cero o split-half invierte signo). Conectar la
familia entera habría repetido el error de la pausa del 29-Ago
(MOMENTUM_IBS_5M_BALLENA#SOL/ETH real, -3.84€ n=3 -- las 3 pérdidas
reales de esa racha: 2 sin dato de bot_consenso, 1 con bot_consenso
DISCREPANDO -- exactamente lo que este filtro habría evitado).

Mecanismo: NO toca momentum_ibs_ballena_executor.py (código de dinero
real, screen ejeclive) -- observador nuevo, autocontenido, que sigue
(tail incremental por posición de fichero, mismo patrón que
candidatas_sin_fillability_depth_fase0.py) predictions_YYYY-MM-DD.csv
(el mismo fichero que shadow_predict.py YA escribe cada ciclo) y para
las 3 combinaciones confirmadas arriba, exige que features::
bot_consenso_lado coincida con la decisión Y bot_consenso_n≥3 -- si
coincide, consulta profundidad real del libro (lt._consultar_
profundidad_libro, solo lectura, nunca ordena) y marca DISPARARIA/
NO_dispara. Deliberadamente separado del gate de precio ya existente
(gate_bucket_propio) -- este script mide el filtro NUEVO por sí solo,
sin mezclar ambos criterios, para poder juzgar su aporte marginal.

⚠️ Solo observación -- NO coloca ninguna orden, no firma nada, no toca
dinero real ni pares_permitidos_live. Salida: data/shadow/momentum_ibs_ballena_botconsenso_dryrun_fase0.csv

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
OUT = DIR_SHADOW / "momentum_ibs_ballena_botconsenso_dryrun_fase0.csv"
VISTOS_PATH = DIR_SHADOW / "momentum_ibs_ballena_botconsenso_dryrun_fase0_vistos.json"

# (strategy, activo, marco) -- las 3 únicas combinaciones confirmadas con
# rigor completo (09-Sep). marco=None coincide con cualquier subtype que
# empiece por ese activo (MOMENTUM_IBS_*_BALLENA no desagrega más).
TUPLAS_CONFIRMADAS = {
    ("MOMENTUM_IBS_5M_BALLENA", "SOL"),
    ("MOMENTUM_IBS_15M_BALLENA", "SOL"),
    ("MOMENTUM_IBS_15M_BALLENA", "BNB"),
}

N_VOTOS_MIN = 3
STAKE_REFERENCIA_EUR = 1.05
POLL_S = 15
RATIO_MIN = 5.0

COLUMNS = [
    "ts_deteccion_utc", "ts_prediccion_utc", "market_id", "strategy",
    "activo", "marco", "decision", "precio_yes_mercado",
    "bot_consenso_lado", "bot_consenso_n", "bot_consenso_pct",
    "mejor_ask_deteccion", "profundidad_eur_deteccion", "ratio_vs_stake_deteccion",
    "sigue_fillable", "decision_dry_run",
]


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


def _bot_coincide(features: dict, decision: str) -> bool:
    lado = features.get("bot_consenso_lado")
    n_votos = features.get("bot_consenso_n", 0) or 0
    if lado is None or n_votos < N_VOTOS_MIN:
        return False
    d_mayoria = "BUY_YES" if lado in (1, "1", "Yes", "YES", "Up") else "BUY_NO"
    return decision == d_mayoria


def _procesar_fila(row: dict, vistos: set) -> dict | None:
    strategy = row.get("strategy", "")
    subtype = row.get("subtype", "")
    activo = subtype.split("#", 1)[0] if "#" in subtype else subtype
    marco = subtype.split("#", 1)[1] if "#" in subtype else ""
    if (strategy, activo) not in TUPLAS_CONFIRMADAS:
        return None
    decision = row.get("decision", "")
    if decision not in ("BUY_YES", "BUY_NO"):
        return None

    market_id = row.get("market_id", "")
    dedup_key = f"{market_id}|{strategy}|{decision}"
    if dedup_key in vistos:
        return None
    vistos.add(dedup_key)

    raw = row.get("features", "")
    try:
        features = json.loads(raw) if raw else {}
    except (TypeError, json.JSONDecodeError):
        features = {}

    if not _bot_coincide(features, decision):
        return None  # fuera del filtro nuevo -- no se audita (ya cubierto por results.csv/predictions.csv normal)

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
    ratio = fill.get("ratio_vs_stake") if fill.get("ok") else None
    sigue_fillable = bool(ratio is not None and ratio >= RATIO_MIN)

    fila = {
        "ts_deteccion_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "ts_prediccion_utc": row.get("timestamp_utc", ""),
        "market_id": market_id, "strategy": strategy, "activo": activo, "marco": marco,
        "decision": decision, "precio_yes_mercado": py,
        "bot_consenso_lado": features.get("bot_consenso_lado", ""),
        "bot_consenso_n": features.get("bot_consenso_n", ""),
        "bot_consenso_pct": features.get("bot_consenso_pct", ""),
        "mejor_ask_deteccion": fill.get("mejor_ask") if fill.get("ok") else "",
        "profundidad_eur_deteccion": fill.get("profundidad_eur") if fill.get("ok") else "",
        "ratio_vs_stake_deteccion": ratio if ratio is not None else "",
        "sigue_fillable": int(sigue_fillable),
        "decision_dry_run": "DISPARARIA" if sigue_fillable else "NO_dispara_sin_libro",
    }
    _log(f"[{strategy}#{activo}] {decision} bot_lado={fila['bot_consenso_lado']} "
         f"bot_n={fila['bot_consenso_n']} ratio={ratio} -> {fila['decision_dry_run']}")
    return fila


def main() -> None:
    _log(f"arrancado -- vigilando {sorted(TUPLAS_CONFIRMADAS)} (bot_consenso n>={N_VOTOS_MIN})")
    vistos = _vistos_cargar()

    archivo = _archivo_hoy()
    posicion = 0
    if archivo.exists():
        with open(archivo, encoding="utf-8") as f:
            header = f.readline()
            cabecera = next(csv.reader([header]))
            for row in csv.DictReader(f, fieldnames=cabecera):
                strategy = row.get("strategy", "")
                subtype = row.get("subtype", "")
                activo = subtype.split("#", 1)[0] if "#" in subtype else subtype
                decision = row.get("decision", "")
                if (strategy, activo) in TUPLAS_CONFIRMADAS and decision in ("BUY_YES", "BUY_NO"):
                    vistos.add(f"{row.get('market_id','')}|{strategy}|{decision}")
            posicion = f.tell()
        _log("backlog de hoy marcado como visto sin consultar libro")
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
                for row in csv.DictReader(f, fieldnames=cabecera):
                    fila = _procesar_fila(row, vistos)
                    if fila is not None:
                        filas_nuevas.append(fila)
                posicion = f.tell()

            if filas_nuevas:
                _guardar(filas_nuevas)
                _vistos_guardar(vistos)
        except Exception as e:
            _log(f"error en ciclo principal ({type(e).__name__}: {e}) -- se reintenta en el siguiente ciclo")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
