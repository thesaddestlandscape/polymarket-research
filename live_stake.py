"""
live_stake.py — Calculadora de stake para operaciones live.

Lógica:
  1. Bankroll operativo = 20€ inicial + PNL acumulado en live
  2. Budget diario = bankroll * pct_bankroll_diario (default 30%)
  3. Budget por ventana = budget_diario / n_ventanas_hoy
  4. Stake Kelly = IC * bankroll * 0.5 (half-Kelly)
  5. Stake final = min(stake_kelly, max_pct * bankroll, budget_ventana_restante)
  6. Nunca < min_stake ni > max_stake del config

El presupuesto se repone cada día a las 00:00 Madrid.
Las ventanas no bloquean el presupuesto entre sí — si una ventana no usa
su cuota, la cuota pasa a las siguientes (pool diario compartido).
"""

import csv
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path

DIR_LIVE    = Path("data/live")
CONFIG_PATH = DIR_LIVE / "config_live.json"
TRADES_CSV  = DIR_LIVE / "trades.csv"
BANKROLL_CSV= DIR_LIVE / "bankroll.csv"

CAPITAL_OPERATIVO_INICIAL = 20.0


def _cargar_config() -> dict:
    if not CONFIG_PATH.exists():
        return {}
    with open(CONFIG_PATH, encoding="utf-8") as f:
        return json.load(f)


def bankroll_actual() -> float:
    """Bankroll live = capital inicial + PNL de trades cerrados."""
    if not TRADES_CSV.exists():
        return CAPITAL_OPERATIVO_INICIAL
    total_pnl = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") == "CLOSED":
                try:
                    total_pnl += float(row.get("pnl_neto_eur", 0) or 0)
                except ValueError:
                    pass
    return CAPITAL_OPERATIVO_INICIAL + total_pnl


def gastado_hoy() -> float:
    """Suma de stakes reales ejecutados hoy (trades OPEN o CLOSED de hoy)."""
    if not TRADES_CSV.exists():
        return 0.0
    config = _cargar_config()
    offset = config.get("utc_offset_verano", 2)
    hoy_madrid = (datetime.now(timezone.utc) + timedelta(hours=offset)).strftime("%Y-%m-%d")
    gastado = 0.0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            fecha_trade = (row.get("timestamp_utc") or "")[:10]
            if fecha_trade == hoy_madrid:
                try:
                    gastado += float(row.get("stake_eur", 0) or 0)
                except ValueError:
                    pass
    return gastado


def calcular_stake(ic: float, strategy: str = "", subtype: str = "") -> dict:
    """
    Devuelve el stake recomendado para una señal con el IC dado.

    Retorna dict con:
      stake_eur       — stake final recomendado
      motivo          — explicación del cálculo
      budget_restante — cuánto queda del budget diario hoy
      bankroll        — bankroll actual
    """
    config   = _cargar_config()
    riesgo   = config.get("riesgo", {})
    bkr      = bankroll_actual()
    n_ventanas = len(config.get("ventanas_lunes_viernes", [])) or 6

    max_pct     = riesgo.get("max_pct_bankroll_por_trade", 0.10)
    pct_diario  = riesgo.get("pct_bankroll_diario", 0.30)
    half_kelly  = riesgo.get("half_kelly", True)
    min_stake   = riesgo.get("min_stake_eur", 0.25)
    max_stake   = riesgo.get("max_stake_eur", 2.00)

    budget_diario    = bkr * pct_diario
    gastado          = gastado_hoy()
    budget_restante  = max(0.0, budget_diario - gastado)

    # Techos en cascada
    techo_kelly      = bkr * abs(ic) * (0.5 if half_kelly else 1.0)
    techo_pct        = bkr * max_pct
    techo_budget     = budget_restante
    techo_config     = max_stake

    stake = min(techo_kelly, techo_pct, techo_budget, techo_config)
    stake = max(stake, min_stake) if budget_restante >= min_stake else 0.0

    motivo = (
        f"Kelly={techo_kelly:.2f}€ | "
        f"max10%={techo_pct:.2f}€ | "
        f"budget_restante={budget_restante:.2f}€ | "
        f"→ stake={stake:.2f}€"
    )

    return {
        "stake_eur":       round(stake, 2),
        "bankroll":        round(bkr, 2),
        "budget_diario":   round(budget_diario, 2),
        "budget_restante": round(budget_restante, 2),
        "gastado_hoy":     round(gastado, 2),
        "motivo":          motivo,
        "viable":          stake >= min_stake,
    }


if __name__ == "__main__":
    bkr  = bankroll_actual()
    hoy  = gastado_hoy()
    print(f"Bankroll live:   {bkr:.2f}€")
    print(f"Gastado hoy:     {hoy:.2f}€")
    print()
    for ic in [0.08, 0.10, 0.15, 0.22]:
        r = calcular_stake(ic)
        print(f"  IC={ic:+.2f}  →  stake={r['stake_eur']:.2f}€  |  {r['motivo']}")
