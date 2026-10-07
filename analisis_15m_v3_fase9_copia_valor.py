#!/usr/bin/env python3
"""analisis_15m_v3_fase9_copia_valor.py -- MISIÓN 15M V3 FASE 9, M17: copiar con RETRASO a las tomadoras que ganan por
VALOR a resolución (no por velocidad). Sin look-ahead de selección: wallets elegidas SOLO con el 05-Oct (n>=40 órdenes,
>=15 mercados, PnL/$ a resolución neto de su comisión > +0,05, mk30 <= 0: el precio les va en contra a corto), copia
evaluada SOLO el 06-Oct. Copia: misma dirección (en términos YES) comprando el token correspondiente al ASK REAL del registro
ms a tr + L (L = 1, 5, 10, 30 s; tr = recepción de su operación), una copia por (wallet, mercado, dirección) = la primera;
PnL/acción = gana − ask − 0,07·ask(1−ask). Entrada: datalogs/m15_ms_cache/v3_quien_barre.parquet + caché ms.
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_fase9_copia_valor.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

INF = Path(__file__).resolve().parent / "informes" / "m15v3_fase9_copia_valor_07oct.txt"
LS = (1000, 5000, 10_000, 30_000)


def main():
    R = pd.read_parquet("/root/polymarket-research-datalogs/m15_ms_cache/v3_quien_barre.parquet")
    R = R[np.isfinite(R.tr_ms) & (R.t_cierre > 0) & (R.t_cierre <= 900)].copy()
    R["dia"] = np.where(R.t < 1791244800000, "05", "06")
    R["res_usdc"] = R.res * R.acc
    sel = R[R.dia == "05"].groupby("wallet").agg(n=("tx", "size"), merc=("mkt", "nunique"), pnl=("res_usdc", "sum"),
                                                  usdc=("usdc", "sum"), mk30=("mk30", "mean"))
    sel["ev"] = sel.pnl / sel.usdc
    W = sel[(sel.n >= 40) & (sel.merc >= 15) & (sel.ev > 0.05) & (sel.mk30 <= 0)]
    C = cargar()
    q, toks = C["q"], C["tokens"]
    des = desenlaces({str(t[2]) for t in toks})
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    libro = {}
    for i, (tk, act, mid_, fin, lado) in enumerate(toks):
        a, b = bq[i], bq[i + 1]
        if b - a >= 50:
            o = np.argsort(q["tr"][a:b], kind="stable")
            libro[(str(mid_), lado)] = (q["tr"][a:b][o], q["ba"][a:b][o].astype(float))
    T = R[(R.dia == "06") & R.wallet.isin(W.index)].sort_values("tr_ms").drop_duplicates(["wallet", "mkt", "d"])
    filas = []
    for r in T.itertuples(index=False):
        lado = "YES" if r.d > 0 else "NO"
        lb = libro.get((str(r.mkt), lado))
        if lb is None or str(r.mkt) not in des:
            continue
        gana = 1.0 if des[str(r.mkt)] == lado else 0.0
        f = {"wallet": r.wallet, "mkt": r.mkt, "fin": r.fin, "act": r.act, "gana": gana,
             "su_pnl": r.res}
        for L in LS:
            k = np.searchsorted(lb[0], int(r.tr_ms) + L, side="right") - 1
            a2 = lb[1][k] if k >= 0 else np.nan
            f[f"pnl{L}"] = gana - a2 - 0.07 * a2 * (1 - a2) if np.isfinite(a2) and 0.02 < a2 < 0.98 else np.nan
        filas.append(f)
    D = pd.DataFrame(filas)
    rng = np.random.default_rng(6)
    L_ = [f"MISIÓN 15M V3 FASE 9 M17 — copiar con retraso a tomadoras de VALOR. Selección 05-Oct: {len(W)} wallets "
          f"(n>=40, >=15 mercados, PnL/$ >+0,05, mk30<=0). Prueba 06-Oct: {len(D)} copias (1 por wallet-mercado-dirección), "
          f"{D.wallet.nunique() if len(D) else 0} wallets activas, {D.fin.nunique() if len(D) else 0} cierres"]
    if len(D):
        L_.append(f"  su propio PnL/acción el 06 (a su precio): {D.su_pnl.mean():+.4f}; acierto {D.gana.mean():.1%}")
        for L in LS:
            g = D[D[f"pnl{L}"].notna()]
            c, n = g.groupby("fin")[f"pnl{L}"].sum(), g.groupby("fin").size()
            bs = [c.iloc[ix].sum() / n.iloc[ix].sum() for ix in (rng.integers(0, len(c), len(c)) for _ in range(2000))]
            top = g.groupby("wallet").size().max() / len(g)
            L_.append(f"  copia a +{L / 1000:>4.0f} s: n={len(g)} EV/acción {g[f'pnl{L}'].mean():+.4f} IC90 cierres "
                      f"({np.percentile(bs, 5):+.4f},{np.percentile(bs, 95):+.4f}) | wallet top {top:.0%}")
        L_.append("  por wallet (copia +5 s): " + "  ".join(f"{w[:8]} n={len(x)} {x.pnl5000.mean():+.3f}"
                                                          for w, x in D.groupby("wallet") if len(x) >= 10))
    INF.write_text("\n".join(L_) + "\n")
    print("\n".join(L_))


if __name__ == "__main__":
    main()
