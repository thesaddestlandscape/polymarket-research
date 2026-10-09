#!/usr/bin/env python3
"""analisis_5m_v1_banda_barata_maker.py -- MISIÓN 5M v1, punto 3 (09-Oct, Javi: "ve con el punto 2 y 3"): validar la
pista de la sección 4 de analisis_5m_v1_quien_gana (makers que COMPRAN barato 0,10-0,30 a T 60-300 s: +9/+19 %/vol;
favoritos 0,50-0,90 negativos), que estaba calculada POR RELLENO, sin IC ni días.

Correcciones (CLAUDE.md, trampas "micro-buckets que cuentan FILLS", "gate por filas", "PnL de una pata de par"):
  - la VENTA maker de un token a p es la compra del token contrario a 1-p -> todo se expresa como LADO COMPRADO y
    precio pagado (pc);
  - UNIDAD = (mercado, lado comprado) dentro de la celda (fase T x banda pc): PnL/€ de la unidad = suma pnl / suma usdc
    de todos los rellenos maker de esa unidad; EV de la celda = media de unidades (cada mercado-lado pesa 1);
  - IC90 por bootstrap de MERCADOS; signo por DÍA (3 días); por activo (BTC vs resto);
  - separar quién compra: wallets "pares" (>= 80 % de sus mercados con ambos lados en el día) vs "direccionales";
  - control: misma celda sin filtrar y las bandas de favoritos.
El PnL es a RESOLUCIÓN con desenlace oficial (cobertura 100 % en la caché), SIN reembolso (aparte: ~0,4 %/vol).
Uso: nice -n 19 python3 analisis_5m_v1_banda_barata_maker.py
"""
from pathlib import Path

import numpy as np
import pandas as pd

CACHE = Path("/root/polymarket-research-datalogs/m5_cache/v1_quien_gana_makers.parquet")
SALIDA = Path(__file__).resolve().parent / "informes" / "m5v1_banda_barata_maker_09oct.txt"
FASES = [0, 60, 120, 200, 300]
BANDAS = [0.0, 0.10, 0.20, 0.30, 0.50, 0.70, 0.90, 1.0]
RNG = np.random.default_rng(7)


def ic90(v, grupos, n=1000):
    """IC90 de la media de unidades remuestreando GRUPOS (mercados)."""
    df = pd.DataFrame({"v": v, "g": grupos})
    s = df.groupby("g").v.agg(["sum", "size"])
    S, N = s["sum"].values, s["size"].values
    if len(S) < 5:
        return (np.nan, np.nan)
    idx = RNG.integers(0, len(S), size=(n, len(S)))
    m = S[idx].sum(1) / N[idx].sum(1)
    return tuple(np.quantile(m, [0.05, 0.95]))


def main():
    X = pd.read_parquet(CACHE, columns=["dia", "wallet", "mkt", "lado", "side", "acc", "usdc", "pnl", "p", "T", "act"])
    X = X[(X["T"] > 0) & (X["T"] <= 300)]
    venta = X.side == 1
    X["lado_c"] = np.where(venta, np.where(X.lado == "YES", "NO", "YES"), X.lado)
    X["pc"] = np.where(venta, 1 - X.p, X.p)
    X["coste"] = np.where(venta, X.acc - X.usdc, X.usdc)       # USDC realmente arriesgado en la compra equivalente
    X = X[X.coste > 0]
    # wallets "pares" por día: >= 80 % de sus mercados con ambos lados comprados
    wm = X.groupby(["dia", "wallet", "mkt"]).lado_c.nunique()
    frac = (wm == 2).groupby(level=[0, 1]).mean()
    pares = set(frac[frac >= 0.8].index)
    X["tipo"] = [("pares" if (d, w) in pares else "direccional") for d, w in zip(X.dia.values, X.wallet.values)]
    X["fase"] = pd.cut(X["T"], FASES)
    X["banda"] = pd.cut(X.pc, BANDAS)
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    L(f"Makers 5m que COMPRAN (venta = compra del contrario), 06-08 Oct, T 0-300 s, {len(X):,} rellenos, "
      f"{X.mkt.nunique()} mercados. Unidad = (mercado, lado comprado); PnL/€ a resolución SIN reembolso.")

    def celda(D, etiqueta):
        U = D.groupby(["dia", "mkt", "lado_c"], observed=True).agg(pnl=("pnl", "sum"), coste=("coste", "sum"),
                                                                    act=("act", "first")).reset_index()
        if len(U) < 15:
            return
        U["ev"] = U.pnl / U.coste
        lo, hi = ic90(U.ev.values, U.mkt.values)
        dias = U.groupby("dia").ev.mean()
        btc = U[U.act == "BTC"].ev.mean()
        resto = U[U.act != "BTC"].ev
        L(f"  {etiqueta:<34s} unidades {len(U):6d} | EV/€ {U.ev.mean():+.4f} IC90 ({lo:+.4f},{hi:+.4f}) | por € agregado "
          f"{U.pnl.sum() / U.coste.sum():+.4f} | días " + " ".join(f"{d[5:]}:{v:+.3f}" for d, v in dias.items()) +
          f" | BTC {btc:+.3f} resto {resto.mean() if len(resto) else float('nan'):+.3f} (n={len(resto)})")

    L("\n1) Rejilla fase x banda (todos los makers)")
    for f in X.fase.cat.categories:
        for b in X.banda.cat.categories:
            celda(X[(X.fase == f) & (X.banda == b)], f"T{f} p{b}")
    L("\n2) La pista: banda 0,10-0,30, T 60-300, por tipo de wallet")
    pista = X[(X.pc > 0.10) & (X.pc <= 0.30) & (X["T"] > 60)]
    celda(pista, "TODOS")
    for t in ("pares", "direccional"):
        celda(pista[pista.tipo == t], t)
    L("\n3) Control: favoritos 0,50-0,90, T 60-300, por tipo de wallet")
    fav = X[(X.pc > 0.50) & (X.pc <= 0.90) & (X["T"] > 60)]
    celda(fav, "TODOS")
    for t in ("pares", "direccional"):
        celda(fav[fav.tipo == t], t)
    SALIDA.write_text("\n".join(lin) + "\n")
    print(f"informe: {SALIDA}")


if __name__ == "__main__":
    main()
