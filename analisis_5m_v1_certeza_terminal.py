#!/usr/bin/env python3
"""analisis_5m_v1_certeza_terminal.py -- MISIÓN 5M v1, paso 3b (12-Oct, Javi: "haz el paso 3b de certeza terminal"):
qué hacen en 5m quienes compran el lado LÍDER a precio alto (p >= 0,80) en los últimos 300 s, frente a nuestro
PRECIERRE/NAIVE (que ya operan en real). Réplica en 5m de analisis_15m_v4_certeza_terminal.py (misma contabilidad y
mismo estado del contrato), con datos on-chain de m5_onchain (volumen) y mapa de tokens de m15_registro.

  - Compras = filas F on-chain con side 0 (el dueño de la orden COMPRA), rol tomador si taker == contrato del exchange,
    maker si no. Precio = USDC/acciones; T = cierre - ts_est (s). Filtro p ∈ [0,80; 0,995), T ∈ (3, 300].
  - Estado en t = ts_est - 2,06 s (desfase bloque-exchange de V3) con ticks Chainlink RECIBIDOS <= t
    (analisis_15m_v4_twap_terminal_mes.estado_twap: z_TWAP con ventana [e-62, e-3], z_spot, σ 300 s); referencia de
    apertura = TWAP60 oficial PolyBolt en cierre-300 (o media RTDS [e-62, e-3]).
  - PnL por acción = gana - p - fee (fee 0,07·p·(1-p) solo al tomador); desenlace OFICIAL (gamma closed=true).
  - EXTRACCIÓN 06-08 Oct: superficie z × precio y definición de "persistentes" (wallets con PnL > 0 en cada uno de los
    3 días en este tramo y >= 30 compras). CONTRASTE 09-11 Oct: mismas celdas y mismas wallets, sin re-elegir nada.
Uso: (ulimit -v 4000000; nice -n 19 ionice -c3 python3 analisis_5m_v1_certeza_terminal.py) — fuera de 06-09Z.
"""
import collections
import gzip
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_5m_v1_quien_gana import EXCH, VOL, mapa_tokens  # noqa: E402
from analisis_b1_compradores_mes import refs_dia, twap_rtds  # noqa: E402
from analisis_15m_v4_twap_terminal_mes import estado_twap, ticks_dia, fee  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

EXTR = ["2026-10-06", "2026-10-07", "2026-10-08"]
CONT = ["2026-10-09", "2026-10-10", "2026-10-11"]
P_MIN, P_MAX, T_MAX, DESFASE_S = 0.80, 0.995, 300, 2.06
INF = Path(__file__).resolve().parent / "informes" / "m5v1_certeza_terminal_12oct.txt"


def compras_dia(d, tok):
    partes = []
    with gzip.open(VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz", "rt") as fh:
        for x in pd.read_csv(fh, chunksize=200_000, dtype={"token_id": str, "maker": str, "taker": str},
                             usecols=["tipo", "ts_est", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt"]):
            x = x[(x.tipo == "F") & (x.side == 0) & x.token_id.isin(tok.keys())]
            if not len(x):
                continue
            usdc, acc = x.maker_amt.astype(float).values, x.taker_amt.astype(float).values
            p = np.divide(usdc, acc, out=np.zeros_like(usdc), where=acc > 0)
            fin = x.token_id.map(lambda t: tok[t][2]).astype(float).values
            T = fin - x.ts_est.astype(float).values
            k = (p >= P_MIN) & (p < P_MAX) & (T > 3) & (T <= T_MAX)
            if not k.any():
                continue
            x = x[k]
            partes.append(pd.DataFrame({
                "dia": d, "wallet": x.maker.str[:10].values, "rol": np.where(x.taker.values == EXCH, "tomador", "maker"),
                "act": x.token_id.map(lambda t: tok[t][0]).values, "mkt": x.token_id.map(lambda t: tok[t][1]).values,
                "lado": x.token_id.map(lambda t: tok[t][3]).values, "fin": fin[k], "ts_est": x.ts_est.astype(float).values,
                "acc": acc[k], "p": p[k], "T": T[k]}))
    return pd.concat(partes, ignore_index=True) if partes else pd.DataFrame()


def main():
    dias = EXTR + CONT
    tok = mapa_tokens(dias, "5min")
    X = pd.concat([compras_dia(d, tok) for d in dias], ignore_index=True)
    print(f"compras p∈[{P_MIN},{P_MAX}) T∈(3,{T_MAX}]: {len(X):,}", file=sys.stderr, flush=True)
    des = desenlaces(set(X.mkt.unique()))
    X = X[X.mkt.isin(des.keys())].copy()
    X["win"] = (X.lado == X.mkt.map(des)).astype(int)
    PB, RT = {}, collections.defaultdict(lambda: [0.0, 0])
    for d in ["2026-10-05"] + dias:
        refs_dia(d, PB, RT)
    zt, zs = np.full(len(X), np.nan), np.full(len(X), np.nan)
    for d in dias:
        tk = ticks_dia(d)
        for i in np.flatnonzero((X.dia == d).values):
            r = X.iloc[i]
            if r.act not in tk:
                continue
            fin = int(r.fin)
            ref = PB.get((r.act, fin - 300)) or twap_rtds(RT, r.act, fin - 300)
            if ref is None:
                continue
            rv, ws, px = tk[r.act]
            e = estado_twap(rv, ws, px, fin, int((r.ts_est - DESFASE_S) * 1000), ref)
            if e is None:
                continue
            s = 1 if r.lado == "YES" else -1
            zt[i], zs[i] = s * e[1], s * e[2]
        del tk
    X["z_tw"], X["z_sp"] = zt, zs
    X["pnl_acc"] = X.win - X.p - np.where(X.rol == "tomador", fee(X.p), 0.0)
    X["pnl"] = X.pnl_acc * X.acc
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    cob = np.isfinite(X.z_tw).mean()
    L(f"Certeza terminal 5m — compras p∈[{P_MIN},{P_MAX}) T∈(3,{T_MAX}] s: {len(X):,} rellenos, {X.mkt.nunique():,} mercados, "
      f"desenlace oficial 100 % de los incluidos; estado TWAP disponible {cob:.1%}")
    E = X[X.dia.isin(EXTR)]
    pw = E.groupby(["wallet", "dia"]).pnl.sum().unstack(fill_value=0.0)
    nw = E.groupby("wallet").size()
    pers = set(pw[(pw > 0).all(axis=1)].index) & set(nw[nw >= 30].index)
    X["pers"] = X.wallet.isin(pers)
    L(f"Persistentes (PnL>0 en 06, 07 y 08 en este tramo, >=30 compras): {len(pers)} wallets")
    for tramo, ds in (("EXTRACCIÓN 06-08", EXTR), ("CONTRASTE 09-11 (sin re-elegir)", CONT)):
        G = X[X.dia.isin(ds)]
        L(f"\n===== {tramo}: {len(G):,} rellenos, {G.mkt.nunique():,} mercados =====")
        for nom, q in (("persistentes", G[G.pers]), ("resto", G[~G.pers])):
            for rol in ("tomador", "maker"):
                r = q[q.rol == rol]
                if len(r) < 20:
                    continue
                zz = r.z_tw.dropna()
                L(f"  {nom:12} {rol:7}: n={len(r):6,} merc={r.mkt.nunique():5,} acierto={np.average(r.win, weights=r.acc):.4f} "
                  f"p_med={np.average(r.p, weights=r.acc):.3f} PnL/acc={np.average(r.pnl_acc, weights=r.acc):+.4f} PnL={r.pnl.sum():+9.0f}$ "
                  f"| z_TWAP P10/P50/P90 {zz.quantile(.1):.2f}/{zz.median():.2f}/{zz.quantile(.9):.2f} | T P50 {r['T'].median():.0f} s")
        L("  SUPERFICIE (todos, con estado): z_TWAP del lado comprado × precio -> acierto, precio y PnL/acc (celdas con >=15 mercados)")
        H = G[np.isfinite(G.z_tw)].assign(zb=lambda d_: pd.cut(d_.z_tw, [-1e9, 0, 1, 2, 3, 4, 6, 1e9]),
                                           pb=lambda d_: pd.cut(d_.p, [0.80, 0.90, 0.95, 0.97, 0.99, 0.995]),
                                           tb=lambda d_: pd.cut(d_["T"], [3, 30, 60, 120, 300]))
        for (zb, pb), q in H.groupby(["zb", "pb"], observed=True):
            if q.mkt.nunique() < 15:
                continue
            tom = q[q.rol == "tomador"]
            L(f"    z {str(zb):>12s} p {str(pb):>13s}: merc={q.mkt.nunique():5,} acierto={np.average(q.win, weights=q.acc):.4f} "
              f"precio={np.average(q.p, weights=q.acc):.4f} PnL/acc todos={np.average(q.pnl_acc, weights=q.acc):+.4f} "
              f"tomador={np.average(tom.pnl_acc, weights=tom.acc) if len(tom) else float('nan'):+.4f} (n tom {len(tom)})")
        L("  POR FASE (todos): T × rol -> PnL/acc")
        for (tb, rol), q in H.groupby(["tb", "rol"], observed=True):
            if q.mkt.nunique() >= 15:
                L(f"    T {str(tb):>10s} {rol:7}: merc={q.mkt.nunique():5,} acierto={np.average(q.win, weights=q.acc):.4f} "
                  f"precio={np.average(q.p, weights=q.acc):.4f} PnL/acc={np.average(q.pnl_acc, weights=q.acc):+.4f}")
    INF.write_text("\n".join(lin) + "\n")
    print(f"\ninforme: {INF}", file=sys.stderr)


if __name__ == "__main__":
    main()
