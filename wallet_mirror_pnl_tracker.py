#!/usr/bin/env python3
"""
wallet_mirror_pnl_tracker.py — PnL REAL que nos ha generado seguir/fadear
cada wallet fuente de WALLET_MIRROR (cripto, data/live/trades.csv) y de
Wallet Mirror sports (data/sports/trades.csv), agregado por wallet.

Origen (02-Sep, propuesta B2 del barrido de sesión "edge sin capturar"):
ya existe `wallet_edge_tracker.py` (edge de la wallet en ballenas_timing_
history.csv, un dataset RETROSPECTIVO ajeno) pero nada mide cuánto nos ha
hecho ganar o perder A NOSOTROS seguir/fadear cada wallet concreta con
DINERO REAL. Encontrado el mismo día: wallet 0xf1ee4842...519c generó las
2 únicas pérdidas reales de sports (-2.10€, ver sesión); en cripto, 2
wallets (0x44832d0d..., 0x20d2309c...) concentran el 62% de los -8.63€
reales de WALLET_MIRROR.

Puramente informativo/shadow -- NO ejecuta nada, NO toca dinero, NO vetа
automáticamente ninguna wallet (n todavía bajo para cualquier decisión con
rigor, ver CLAUDE.md "ninguna conclusión con n<15"). Solo agrega y expone
el ranking para revisión manual cada sesión, mismo espíritu que
gate_bucket_propio.py pero sobre la fuente de la señal (wallet), no sobre
el precio de entrada.

Se fusiona en observadores_fase0.py (screen "observadores") -- NUNCA
lanzar una screen suelta para este script.
"""
import csv
import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "wallet_mirror_pnl_por_wallet.json"

_RE_WALLET = re.compile(r"wallet=(0x[0-9a-fA-F]+)")


def _extraer_wallet(notas: str) -> str | None:
    m = _RE_WALLET.search(notas or "")
    return m.group(1) if m else None


def _agregar(path: Path, strategy_filtro: str | None, fuente: str, acc: dict) -> None:
    if not path.exists():
        return
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("status") != "CLOSED":
                continue  # excluye OPEN y ERROR (incluye fantasmas, ver docstring)
            if strategy_filtro and row.get("strategy") != strategy_filtro:
                continue
            wallet = _extraer_wallet(row.get("notas", ""))
            if wallet is None:
                continue
            try:
                pnl = float(row.get("pnl_neto_eur") or 0)
            except ValueError:
                continue
            key = wallet
            e = acc.setdefault(key, {"n": 0, "pnl_total_eur": 0.0, "n_win": 0, "fuentes": set()})
            e["n"] += 1
            e["pnl_total_eur"] += pnl
            e["n_win"] += 1 if pnl > 0 else 0
            e["fuentes"].add(fuente)


def calcular() -> dict:
    acc: dict = {}
    _agregar(REPO / "data" / "live" / "trades.csv", "WALLET_MIRROR", "cripto", acc)
    _agregar(REPO / "data" / "sports" / "trades.csv", None, "sports", acc)

    resultado = {}
    for wallet, e in acc.items():
        n = e["n"]
        resultado[wallet] = {
            "n": n,
            "pnl_total_eur": round(e["pnl_total_eur"], 4),
            "pnl_medio_eur": round(e["pnl_total_eur"] / n, 4) if n else 0.0,
            "hit_rate": round(e["n_win"] / n, 4) if n else 0.0,
            "fuentes": sorted(e["fuentes"]),
            "n_suficiente_para_concluir": n >= 15,
        }
    return dict(sorted(resultado.items(), key=lambda kv: kv[1]["pnl_total_eur"]))


def main() -> None:
    resultado = calcular()
    OUT.write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")
    n_total = sum(v["n"] for v in resultado.values())
    pnl_total = sum(v["pnl_total_eur"] for v in resultado.values())
    print(f"[wallet_mirror_pnl_tracker] {len(resultado)} wallets, "
          f"n_total={n_total} pnl_total={pnl_total:.2f}EUR -> {OUT}")


if __name__ == "__main__":
    main()
