#!/usr/bin/env python3
"""analisis_5m_barato_v7_capacidad.py -- CAPACIDAD de V7_DISPARO15M_BTC (DESCUBRIMIENTO 05-13 Oct, solo lectura): para cada
ejecución simulada (caché disparo15m_D, BTC, DELTA 0, L355) relee el libro del 5m en t+L y toma el TAMAÑO del nivel 1 al ask
de llegada (lo único que registra el registro ms: los niveles 2-3 no están -> cota INFERIOR de capacidad). PnL por stake
objetivo S: acciones = min(S/ask, tamaño nivel 1) (mínimo 5 acciones o no se opera), mismo desenlace y comisión.
Uso: nice -n 19 python3 analisis_5m_barato_v7_capacidad.py
"""
import csv
import gzip
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_5m_barato_disparo15m as D7  # noqa: E402
import vigia_5m_barato_forward as V  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
STAKES = (2, 5, 10, 25, 50, 100, 250)


def main():
    ej = defaultdict(list)
    for f in sorted(OUT.glob("disparo15m_2026-10-*.csv.gz")):
        for r in csv.DictReader(gzip.open(f, "rt")):
            if r["moneda"] == "BTC" and r.get("pnl") and float(r["delta"]) == 0.0 and r["L"] == "355":
                ej[r["dia"]].append(r)
    filas = []
    for dia, rs in sorted(ej.items()):
        meta, libros, _ = D7.cargar(dia)
        tok = {(m[2], m[4]): k for k, m in meta.items() if m[1] == "5min"}
        for r in rs:
            k = tok.get((r["mercado"], "YES" if r["lado"] == "Up" else "NO"))
            L5 = libros.get(k)
            _, qa = L5.en(int(r["t"]) + 355) if L5 else (None, None)
            sz = qa[3] if qa else 0.0
            filas.append({**r, "tam_n1": sz})
        print(f"{dia}: {len(rs)} ejecuciones", flush=True)
    print(f"\nV7 BTC DELTA 0 L355 — {len(filas)} ejecuciones; tamaño nivel 1 al llegar (acciones): "
          f"P25/P50/P75 {sorted(f['tam_n1'] for f in filas)[len(filas) // 4]:.0f}/"
          f"{sorted(f['tam_n1'] for f in filas)[len(filas) // 2]:.0f}/{sorted(f['tam_n1'] for f in filas)[3 * len(filas) // 4]:.0f}")
    dias = len({f["dia"] for f in filas}) or 1
    for S in STAKES:
        pnl = cost = 0.0
        n = 0
        top = []
        for f in filas:
            p = float(f["ask"])
            acc = min(S / p, f["tam_n1"])
            if acc < 5:
                continue
            g = f["gana"] == "True"
            x = acc * ((1.0 if g else 0.0) - p - V.fee(p))
            pnl += x
            cost += acc * (p + V.fee(p))
            n += 1
            top.append(x)
        top.sort(reverse=True)
        print(f"  stake {S:4d} €: ops {n:2d} | invertido {cost:8.1f} € | PnL {pnl:+8.2f} € | EV/€ {pnl / cost if cost else 0:+.3f} | "
              f"sin top3 {pnl - sum(top[:3]):+8.2f} € | {pnl / dias:+.2f} €/día ({dias} días) -> x365 {pnl / dias * 365:+,.0f} €/año")


if __name__ == "__main__":
    main()
