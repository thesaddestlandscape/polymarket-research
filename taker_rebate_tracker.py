#!/usr/bin/env python3
"""
taker_rebate_tracker.py — KPI de volumen ponderado (wV) del Taker Rebate
Program de Polymarket, ventana móvil de 30 días, mismo criterio para
cripto y sports (misma wallet/cuenta, mismo contador de tier -- ver
idea_taker_rebate_program_descubierto_27ago).

Origen (27-Ago, descubierto; 02-Sep, propuesta C10 del barrido "cerrar
el gap PnL fiel"): `rebateRate:0.2` llevaba en el fee schedule desde
22-Jul sin que nadie lo investigara. Programa REAL (docs.polymarket.com/
trading/taker-rebates), pago automático diario en pUSD, 7 tiers por
volumen ponderado de 30 días. Fórmula:

    wV = stake_eur * (1 - precio_entrada) * peso_categoria

Pesos: Sports=1.0, Crypto=2.3 (el más alto), Weather=1.7 (categoría
Culture/Economics, no confirmado 1:1 pero es el peso citado en la
fuente oficial para esa familia de categorías).

Puramente informativo -- no toca ninguna decisión ni dinero, solo
reporta el tier actual y cuánto falta para el siguiente. Genera
data/shadow/taker_rebate_wv.json.
"""
import csv
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "taker_rebate_wv.json"
PESO_CRYPTO = 2.3
PESO_SPORTS = 1.0
TIERS = [
    ("Bronze", 2_000, 0.03),
    ("Silver", 20_000, 0.08),
    ("Gold", 200_000, 0.18),
    ("Platinum", 1_000_000, 0.32),
    ("Diamond", 4_000_000, 0.44),
    ("Obsidian", 10_000_000, 0.50),
]


def _wv_desde_trades(path: Path, peso: float, campo_stake="stake_eur", campo_precio="entry_price") -> float:
    if not path.exists():
        return 0.0
    cutoff = (datetime.now(timezone.utc) - timedelta(days=30)).isoformat()
    total = 0.0
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue
            ts = row.get("timestamp_utc", "")
            if ts < cutoff:
                continue
            try:
                stake = float(row.get(campo_stake) or 0)
                precio = float(row.get(campo_precio) or 0)
            except ValueError:
                continue
            if stake <= 0 or not (0 < precio < 1):
                continue
            total += stake * (1 - precio) * peso
    return total


def _tier_actual(wv: float) -> tuple[str, float, str | None, float]:
    """(tier_actual, rebate_actual, siguiente_tier, falta_para_siguiente)."""
    tier_actual, rebate_actual = "Ninguno", 0.0
    for nombre, umbral, rebate in TIERS:
        if wv >= umbral:
            tier_actual, rebate_actual = nombre, rebate
    for nombre, umbral, _ in TIERS:
        if wv < umbral:
            return tier_actual, rebate_actual, nombre, round(umbral - wv, 2)
    return tier_actual, rebate_actual, None, 0.0


def main() -> None:
    wv_cripto = _wv_desde_trades(REPO / "data/live/trades.csv", PESO_CRYPTO)
    wv_sports = _wv_desde_trades(REPO / "data/sports/trades.csv", PESO_SPORTS)
    wv_total = wv_cripto + wv_sports  # misma wallet/cuenta, mismo contador de tier

    tier, rebate, siguiente, falta = _tier_actual(wv_total)
    resultado = {
        "wv_cripto_30d": round(wv_cripto, 2),
        "wv_sports_30d": round(wv_sports, 2),
        "wv_total_30d": round(wv_total, 2),
        "tier_actual": tier,
        "rebate_actual_pct": rebate,
        "siguiente_tier": siguiente,
        "falta_para_siguiente": falta,
    }
    OUT.write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"[taker_rebate_tracker] wV_total_30d=${wv_total:.2f} tier={tier} "
          f"rebate={rebate*100:.0f}% siguiente={siguiente} falta=${falta:.2f}")


if __name__ == "__main__":
    main()
