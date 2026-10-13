#!/usr/bin/env python3
"""analisis_15m_v5_politica_planos.py -- MISIÓN 15M v5 (13-Oct): extraer de los rellenos on-chain la POLÍTICA de los
cosechadores que acaban PLANOS y ganan de forma persistente (0x2903c7dc, 0x98b84283, 0x86b9a88a) frente a los que
acaban con suelta y pierden (0xcfddfb6e, 0xb945945d). BTC 15m, 05-12 Oct, solo compras maker (ninguno toma ni vende).
  1) ¿dejan de comprar el lado que SOBRA? P(relleno que AUMENTA |inv|) según |inv| previo.
  2) Coste MARGINAL del par al completar: relleno del lado que falta a p + coste medio del lado que sobra.
  3) Momento: T de los rellenos (P10/50/90), y P(relleno en el 1er nivel de precio de su tx = mejor bid).
  4) Tamaño por relleno y por mercado; nº de rellenos por mercado.
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v5_politica_planos.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_15m_v5_pares_cola_onchain as B  # noqa: E402

W = ["0x2903c7dc", "0x98b84283", "0x86b9a88a", "0xcfddfb6e", "0xb945945d"]
INF = Path(__file__).resolve().parent / "informes" / "m15v5_politica_planos_13oct.txt"


def main():
    X = pd.concat([B.cargar(d) for d in B.DIAS], ignore_index=True)
    X = X[(X.act.astype(str) == "BTC") & ~X.es_tom & (X.side == 0)].copy()
    X["acc"], X["usdc"] = X.taker_amt.astype(float), X.maker_amt.astype(float)
    X = X[X.acc > 0]
    X["p"] = (X.usdc / X.acc).round(4)
    X["T"] = X.fin - X.ts_est
    # 1er nivel de precio de la tx (para el mismo token): ¿estaba en el mejor bid?
    pmax = X.groupby(["tx", "token_id"], observed=True).p.transform("max")
    X["nivel1"] = X.p >= pmax - 1e-9
    X["wallet"] = X.maker.astype(str)
    X = X[X.wallet.isin(W)].sort_values(["wallet", "mkt", "ts_est", "log_index"])
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)

    for w in W:
        s = X[X.wallet == w]
        out = []
        for mkt, g in s.groupby("mkt", observed=True):
            iy = inn = cy = cn = 0.0
            for lado, a, p, T_, n1 in zip(g.lado.astype(str), g.acc.values, g.p.values, g["T"].values, g.nivel1.values):
                inv = iy - inn
                aumenta = (lado == "YES" and inv >= 0) or (lado == "NO" and inv <= 0)
                comp = None
                if not aumenta:                          # completa: coste marginal del par
                    comp = p + ((cy / iy) if lado == "NO" else (cn / inn))
                out.append((abs(inv), aumenta, comp, a, T_, n1))
                if lado == "YES":
                    iy += a; cy += a * p
                else:
                    inn += a; cn += a * p
        O = pd.DataFrame(out, columns=["absinv", "aumenta", "comp", "acc", "T", "n1"])
        L(f"\n== {w}: rellenos {len(O)} en {s.mkt.nunique()} mercados | tamaño P50 {O.acc.median():.1f} | rell/merc P50 {s.groupby('mkt', observed=True).size().median():.0f}")
        for lo, hi in ((0, 1), (1, 50), (50, 150), (150, 300), (300, 1e9)):
            m = (O.absinv >= lo) & (O.absinv < hi)
            if m.sum() >= 20:
                L(f"   |inv| previo [{lo},{hi if hi < 1e9 else 'inf'}): n {m.sum():6d} P(aumenta) {O.aumenta[m].mean():.2f}")
        c = O.comp.dropna()
        L(f"   coste marginal del par al completar: n {len(c)} P10 {c.quantile(.1):.3f} P50 {c.median():.3f} P90 {c.quantile(.9):.3f} "
          f"| >1,00 {(c > 1.0).mean():.1%} | >0,99 {(c > 0.99).mean():.1%}")
        L(f"   T del relleno P10/50/90 {O['T'].quantile(.1):.0f}/{O['T'].median():.0f}/{O['T'].quantile(.9):.0f} | "
          f"en 1er nivel de su tx {O.n1.mean():.2f} | T>840: {(O['T'] > 840).mean():.1%} | T<120: {(O['T'] < 120).mean():.1%}")
    INF.write_text("\n".join(lin) + "\n")
    L(f"\n→ {INF}")


if __name__ == "__main__":
    main()
