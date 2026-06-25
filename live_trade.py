"""
live_trade.py — Motor de ejecución live. Se añade al fast loop tras shadow_predict.

Flujo por ciclo:
  1. live_guard: ¿puede operar ahora? (switch + ventana)
  2. Leer predicciones del ciclo actual (predictions_HOY.csv)
  3. Filtrar señales que pasan el umbral IC mínimo y son de estrategias permitidas
  4. Evitar duplicados: no operar en el mismo mercado dos veces
  5. Calcular stake con live_stake.py
  6. [STUB] Ejecutar orden en Polymarket via CLOB API  ← pendiente de credenciales
  7. Registrar en data/live/trades.csv
  8. Log completo en logs/live.log
"""

import csv
import json
import os
from datetime import datetime, timezone, timedelta
from pathlib import Path

from live_guard import puede_operar_live, estado_live
from live_stake import calcular_stake, bankroll_actual

DIR_LIVE    = Path("data/live")
DIR_SHADOW  = Path("data/shadow")
TRADES_CSV  = DIR_LIVE  / "trades.csv"
PARAMS_PATH = DIR_SHADOW / "strategy_params.json"
LOG_PATH    = Path("logs/live.log")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

TRADES_COLS = [
    "timestamp_utc", "market_id", "question", "end_date",
    "strategy", "subtype", "direction", "stake_eur",
    "entry_price", "ic_modelo", "edge_neto",
    "conviction_score", "kelly_recomendado",
    "status", "close_timestamp", "exit_price",
    "outcome_real", "fee_eur", "pnl_bruto_eur", "pnl_neto_eur", "notas",
]


def log(msg: str):
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def _cargar_params() -> dict:
    if not PARAMS_PATH.exists():
        return {}
    with open(PARAMS_PATH, encoding="utf-8") as f:
        return json.load(f).get("estrategias", {})


def _cargar_config() -> dict:
    p = DIR_LIVE / "config_live.json"
    if not p.exists():
        return {}
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def _ya_operados_hoy() -> set:
    """Set de market_id que ya tienen trade OPEN o CLOSED hoy."""
    if not TRADES_CSV.exists():
        return set()
    config = _cargar_config()
    offset = config.get("utc_offset_verano", 2)
    hoy    = (datetime.now(timezone.utc) + timedelta(hours=offset)).strftime("%Y-%m-%d")
    vistos = set()
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row.get("timestamp_utc") or "")[:10] == hoy:
                vistos.add(row.get("market_id", ""))
    return vistos


def _cargar_predicciones_hoy() -> list:
    """Carga las predicciones de hoy con decision BUY_YES o BUY_NO."""
    hoy  = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = DIR_SHADOW / f"predictions_{hoy}.csv"
    if not path.exists():
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("decision") in ("BUY_YES", "BUY_NO"):
                rows.append(row)
    return rows


def _ic_para_subtype(strategy: str, subtype: str, params: dict) -> float:
    """IC Bayesiano efectivo del subtype desde strategy_params.json."""
    claves = []
    if "#" in subtype:
        a, d = subtype.split("#", 1)
        claves = [f"{strategy}#{subtype}", f"{strategy}#{a}", f"{strategy}#{d}", strategy]
    elif subtype:
        claves = [f"{strategy}#{subtype}", strategy]
    else:
        claves = [strategy]
    for k in claves:
        if k in params:
            return float(params[k].get("ic_bayes", 0))
    return 0.0


def _ejecutar_orden_polymarket(market_id: str, direction: str,
                               stake_eur: float, entry_price: float) -> dict:
    """
    STUB: aquí irá la integración con la CLOB API de Polymarket.

    Necesita:
      - Clave privada de la wallet (POLYMARKET_PRIVATE_KEY en .env)
      - py-clob-client o llamadas directas a https://clob.polymarket.com
      - USDC en Polygon en la wallet

    Cuando esté listo, sustituir este stub por la llamada real.
    Devuelve dict con: ok, order_id, entry_price_real, fee_eur, error
    """
    log(f"  [STUB] Orden NO ejecutada — credenciales pendientes")
    log(f"         market_id={market_id} direction={direction} "
        f"stake={stake_eur:.2f}€ precio={entry_price:.4f}")
    return {
        "ok":           False,
        "stub":         True,
        "order_id":     None,
        "entry_price":  entry_price,
        "fee_eur":      0.0,
        "error":        "CREDENCIALES_PENDIENTES",
    }


def _registrar_trade(row: dict):
    nuevo = not TRADES_CSV.exists()
    with open(TRADES_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=TRADES_COLS)
        if nuevo:
            w.writeheader()
        w.writerow({col: row.get(col, "") for col in TRADES_COLS})


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    log(f"=== live_trade ciclo {ts} ===")

    # 1. Guardián: ¿podemos operar ahora?
    puede, motivo = puede_operar_live()
    est = estado_live()
    log(f"  Switch: {'ON' if est['switch'] else 'OFF'} | "
        f"Ventana: {'SÍ' if est['en_ventana'] else 'NO'} ({motivo}) | "
        f"Hora Madrid: {est['hora_madrid']} ({est['dia']})")

    if not puede:
        log(f"  → Fuera de operación. Motivo: {motivo}")
        return

    # 2. Cargar predicciones y parámetros
    predicciones = _cargar_predicciones_hoy()
    params       = _cargar_params()
    config       = _cargar_config()
    riesgo       = config.get("riesgo", {})
    min_ic       = riesgo.get("min_ic_para_live", 0.08)
    min_n        = riesgo.get("min_n_para_live", 40)
    estrategias_ok = config.get("estrategias_permitidas_live", [])
    subtypes_ok    = config.get("subtypes_permitidos_live", [])
    ya_operados  = _ya_operados_hoy()
    bkr          = bankroll_actual()

    log(f"  Predicciones hoy: {len(predicciones)} | Bankroll: {bkr:.2f}€ | Ya operados hoy: {len(ya_operados)}")

    ejecutados = 0
    for pred in predicciones:
        strategy = pred.get("strategy", "")
        subtype  = pred.get("subtype", "")
        mid      = pred.get("market_id", "")
        dec      = pred.get("decision", "")

        # Filtros de elegibilidad
        if strategy not in estrategias_ok:
            continue
        if subtypes_ok and subtype not in subtypes_ok:
            continue
        if mid in ya_operados:
            continue

        # IC mínimo confirmado en histórico
        ic_hist = _ic_para_subtype(strategy, subtype, params)
        n_hist  = params.get(f"{strategy}#{subtype}", params.get(strategy, {})).get("n", 0)
        if ic_hist < min_ic or n_hist < min_n:
            continue

        # IC del modelo para esta señal concreta
        try:
            prob_y = float(pred.get("prob_yes_modelo", 0.5))
            precio = float(pred.get("precio_yes_mercado", 0.5))
            edge   = float(pred.get("edge_neto", 0))
        except ValueError:
            continue

        # Stake
        stake_info = calcular_stake(ic_hist, strategy, subtype)
        if not stake_info["viable"]:
            log(f"  SKIP {strategy}#{subtype}: budget insuficiente ({stake_info['budget_restante']:.2f}€ restante)")
            continue

        stake    = stake_info["stake_eur"]
        entry_p  = precio

        log(f"  SEÑAL → {strategy}#{subtype} {dec} "
            f"precio={entry_p:.4f} IC_hist={ic_hist:+.3f} n={n_hist} "
            f"stake={stake:.2f}€")
        log(f"         {stake_info['motivo']}")

        # 3. Ejecutar (STUB hasta tener credenciales)
        resultado = _ejecutar_orden_polymarket(mid, dec, stake, entry_p)

        # 4. Registrar
        ts_now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        trade = {
            "timestamp_utc":   ts_now,
            "market_id":       mid,
            "question":        pred.get("question", ""),
            "end_date":        pred.get("end_date", ""),
            "strategy":        strategy,
            "subtype":         subtype,
            "direction":       dec,
            "stake_eur":       stake if resultado["ok"] else 0.0,
            "entry_price":     resultado["entry_price"],
            "ic_modelo":       round(prob_y, 4),
            "edge_neto":       round(edge, 4),
            "conviction_score": round(ic_hist, 4),
            "kelly_recomendado": stake,
            "status":          "OPEN" if resultado["ok"] else "STUB",
            "close_timestamp": "",
            "exit_price":      "",
            "outcome_real":    "",
            "fee_eur":         resultado.get("fee_eur", 0),
            "pnl_bruto_eur":   "",
            "pnl_neto_eur":    "",
            "notas":           resultado.get("error", ""),
        }
        _registrar_trade(trade)
        ya_operados.add(mid)
        ejecutados += 1

        # No más de 3 operaciones por ciclo (espacio entre señales)
        if ejecutados >= 3:
            log(f"  Límite de 3 operaciones por ciclo alcanzado.")
            break

    log(f"  Operaciones ejecutadas este ciclo: {ejecutados}")
    log(f"=== Fin live_trade ===")


if __name__ == "__main__":
    main()
