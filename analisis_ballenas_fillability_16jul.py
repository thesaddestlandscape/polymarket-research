#!/usr/bin/env python3
"""Read-only, one-off (16-Jul, petición Javi): ¿cuando la concentración de
ballenas en un mercado es alta, el LIBRO REAL que vimos nosotros (nuestros
propios intentos de ejecución, libro_snapshots.csv) tiene profundidad, o ya
está consumido? Mismo patrón que ya reveló selección adversa 3 veces este
mes (BTC#15min#BUY_NO 14-Jul, FAVORITO_CONFIRMADO#*#15min#BUY_NO 16-Jul,
maker_pilot 12-Jul) — antes de añadir un combo a `combos_validados` del
veto_ballenas de live_trade.py, hay que comprobar si el libro aguanta en
el momento en que las ballenas confirman, para ESE combo concreto.

Cruza libro_snapshots.csv (nuestros propios intentos reales de ejecución,
con ratio_vs_stake ya medido) contra la concentración de ballenas del mismo
mercado dentro de la banda de precio calibrada (re-fetch /trades, mismo
método que analisis_ballenas_dosis_respuesta_16jul.py).

Uso: python3 analisis_ballenas_fillability_16jul.py SOL#15min FAVORITO_CONFIRMADO,GBM_LATE_15M_ESPACIO_ATR BUY_YES 0.7 0.9
     (subtype_prefix, strategies_csv, direction, banda_lo, banda_hi)

Solo lectura. No toca dinero ni config.
"""
import csv
import sys
from collections import defaultdict
from pathlib import Path

from smart_money_tracker import trades_de_mercado

DIR = Path(__file__).parent
SNAPSHOTS = DIR / "data/live/libro_snapshots.csv"
DIR_MARKETS = DIR / "data/markets"
ARCHIVOS_MARKETS_RECIENTES = 5


def mapear_condition_a_market():
    mapa = {}
    archivos = sorted(DIR_MARKETS.glob("*.csv"))[-ARCHIVOS_MARKETS_RECIENTES:]
    for archivo in archivos:
        with open(archivo, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                cid = row.get("condition_id", "")
                mid = row.get("market_id", "")
                if cid and mid:
                    mapa[mid] = cid
    return mapa


def concentracion_ballena(condition_id: str, banda_lo: float, banda_hi: float) -> tuple[int, int]:
    """(n_yes, n_no) de trades BUY de ballena en `condition_id` dentro de banda."""
    trades = trades_de_mercado(condition_id)
    n_yes = n_no = 0
    for t in trades:
        if (t.get("side") or "").strip().upper() != "BUY":
            continue
        precio_t = t.get("price")
        outcome_t = (t.get("outcome") or "").strip().lower()
        if precio_t is None or outcome_t not in ("up", "down", "yes", "no"):
            continue
        try:
            precio_t = float(precio_t)
        except (ValueError, TypeError):
            continue
        if not (banda_lo <= precio_t < banda_hi):
            continue
        if outcome_t in ("up", "yes"):
            n_yes += 1
        else:
            n_no += 1
    return n_yes, n_no


def main():
    if len(sys.argv) != 6:
        print(__doc__)
        sys.exit(1)
    subtype_prefix, strategies_csv, direction, banda_lo, banda_hi = sys.argv[1:6]
    strategies = set(strategies_csv.split(","))
    banda_lo, banda_hi = float(banda_lo), float(banda_hi)

    filas = defaultdict(list)  # market_id -> [rows de libro_snapshots]
    with open(SNAPSHOTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["subtype"] != subtype_prefix:
                continue
            if row["strategy"] not in strategies:
                continue
            if row["direction"] != direction:
                continue
            if row.get("ratio_vs_stake") in (None, ""):
                continue
            filas[row["market_id"]].append(row)

    print(f"{subtype_prefix}#{direction} ({strategies_csv}): mercados con intento de ejecución real: {len(filas)}")

    print("Construyendo mapa market_id -> condition_id...")
    mapa_mid_cid = mapear_condition_a_market()

    lado_nuestro = "yes" if direction == "BUY_YES" else "no"
    resultados = []  # (market_id, ratio_vs_stake_min, motivo_peor, pct_nuestro_lado, n_ballena)
    for i, (mid, rows) in enumerate(filas.items()):
        cid = mapa_mid_cid.get(mid)
        if not cid:
            continue
        try:
            ratios = [float(r["ratio_vs_stake"]) for r in rows]
        except (ValueError, TypeError):
            continue
        ratio_repr = min(ratios)
        motivo_repr = next((r["motivo"] for r in rows if float(r["ratio_vs_stake"]) == ratio_repr), rows[0]["motivo"])

        try:
            n_yes, n_no = concentracion_ballena(cid, banda_lo, banda_hi)
        except Exception:
            continue
        n_tot = n_yes + n_no
        if n_tot < 3:
            continue
        n_nuestro = n_yes if lado_nuestro == "yes" else n_no
        pct_nuestro = n_nuestro / n_tot
        resultados.append((mid, ratio_repr, motivo_repr, pct_nuestro, n_tot))
        if (i + 1) % 20 == 0:
            print(f"  {i+1}/{len(filas)} procesados...")

    print(f"\nMercados con dato completo (libro real + ballenas): {len(resultados)}")
    if not resultados:
        return

    buckets = [(0.0, 0.6), (0.6, 0.9), (0.9, 1.01)]
    print(f"\n{'bucket pct_nuestro_lado':<26} {'n':>4} {'ratio_vs_stake medio':>22} {'% con veto_profundidad':>24}")
    print("-" * 80)
    for lo, hi in buckets:
        sub = [r for r in resultados if lo <= r[3] < hi]
        if not sub:
            print(f"[{lo:.1f},{hi:.1f})".ljust(26) + f"{0:>4}")
            continue
        ratio_medio = sum(r[1] for r in sub) / len(sub)
        pct_veto = sum(1 for r in sub if r[2] == "veto_profundidad") / len(sub)
        print(f"[{lo:.1f},{hi:.1f})".ljust(26) + f"{len(sub):>4}" + f"{ratio_medio:>22.2f}" + f"{pct_veto*100:>23.1f}%")


if __name__ == "__main__":
    sys.exit(main() or 0)
