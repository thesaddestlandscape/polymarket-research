#!/usr/bin/env python3
"""n5: PnL diario y por componente de MM y W, 06-21 Oct, desde R_D (agregados on-chain por wallet×mercado×token×venta×rol de
ganadoras_persistentes/e1_roles, validado al céntimo contra la caché de mo-money 10-Oct). Desenlace oficial. Comisión del
tomador estimada 0,07·p(1−p)·acc (R_D no la guarda); rebate maker estimado 20 % de la comisión del tomador contrario (no observado).
Componentes por mercado: pares = min(qY,qN)·(1 − pY − pN) con precios medios; dirección = resto. Periodos: SEL 06-14 / OOS 15-21."""
import sys, glob
sys.path.insert(0, "/root/polymarket-research")
import numpy as np, pandas as pd
from analisis_maker_cancelacion_binance import desenlaces
G = "/mnt/HC_Volume_106538179/agentes_datos/ganadoras_persistentes"
WAL = {"MM": "0x32ed2e546b187ca15e2841edc82b22c713cf8ec3", "W": "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5"}
P = []
for f in sorted(glob.glob(f"{G}/R_2026-10-*.pkl")):
    r = pd.read_pickle(f); r = r[r.w.astype(str).isin(WAL.values())].copy(); r["w"] = r.w.astype(str); r["dia"] = f[-14:-4]; P.append(r)
R = pd.concat(P, ignore_index=True); R["wal"] = R.w.map({v: k for k, v in WAL.items()})
print("ventas (v=1) filas:", int((R.v == 1).sum()))
des = desenlaces(set(R.mid.astype(str))); R["des"] = R.mid.astype(str).map(des)
print("cobertura desenlace", round(R.des.notna().mean(), 4)); R = R[R.des.notna()]
R["lado"] = np.where(R.tok == 0, "YES", "NO"); R["win"] = (R.lado == R.des).astype(float)
R["p"] = R.coste / R.acc; R["fee"] = np.where(R.rol == 1, 0.07 * R.p * (1 - R.p) * R.acc, 0.0)
R["reb"] = np.where(R.rol == 0, 0.2 * 0.07 * R.p * (1 - R.p) * R.acc, 0.0)
R["pnl"] = R.win * R.acc - R.coste - R.fee
R["per"] = np.where(R.dia <= "2026-10-14", "SEL", "OOS")
rng = np.random.default_rng(9)
def ic(g):
    dd = g.groupby("dia")[["pnl", "coste"]].sum().values; bs = []
    for _ in range(1000):
        s = dd[rng.integers(0, len(dd), len(dd))].sum(0); bs.append(s[0] / s[1])
    return f"EV {g.pnl.sum()/g.coste.sum():+.4f} IC90d ({np.percentile(bs,5):+.4f},{np.percentile(bs,95):+.4f}) PnL {g.pnl.sum():+,.0f}$ coste {g.coste.sum():,.0f}$ días+ {(g.groupby('dia').pnl.sum()>0).sum()}/{g.dia.nunique()}"
for wal in ("MM", "W"):
    X = R[R.wal == wal]
    print(f"\n===== {wal}")
    print("por día:", " ".join(f"{d[5:]}:{v:+.0f}" for d, v in X.groupby("dia").pnl.sum().items()))
    for per in ("SEL", "OOS"):
        S = X[X.per == per]
        print(f"[{per}] total {ic(S)} | rebate est {S.reb.sum():+.0f}$ | fee tomador est {S.fee.sum():.0f}$")
        for rol in (0, 1):
            for lo, hi in ((0, .1), (.1, .3), (.3, .7), (.7, .9), (.9, 1.01)):
                g = S[(S.rol == rol) & (S.p >= lo) & (S.p < hi)]
                if len(g) >= 30: print(f"   {'M' if rol==0 else 'T'} p[{lo},{hi}) unidades {len(g)} hit {g.win.mean():.3f} vs p {np.average(g.p, weights=g.coste):.3f} (media {g.p.mean():.3f}) {ic(g)}")
        # pares vs dirección por mercado (todas las filas compra)
        m = S.groupby(["mid", "lado"]).agg(q=("acc", "sum"), c=("coste", "sum"), f=("fee", "sum"), win=("win", "first")).reset_index()
        pv = m.pivot(index="mid", columns="lado", values=["q", "c", "win"]).fillna(0)
        qY, qN = pv[("q", "YES")], pv[("q", "NO")]; cY, cN = pv[("c", "YES")], pv[("c", "NO")]
        pY = cY / qY.replace(0, np.nan); pN = cN / qN.replace(0, np.nan); mn = np.minimum(qY, qN)
        pares = (mn * (1 - pY.fillna(0) - pN.fillna(0))).where(mn > 0, 0)
        tot = S.groupby("mid").pnl.sum() + S.groupby("mid").fee.sum()
        print(f"   mercados {len(pv)} con ambos lados {(mn>0).mean():.2f} | pares {pares.sum():+,.0f}$ | dirección {(tot.reindex(pv.index)-pares).sum():+,.0f}$ | fee tomador {-S.fee.sum():+,.0f}$")
        print(f"   por moneda: n/a en R_D (sin activo); hora: n/a")
