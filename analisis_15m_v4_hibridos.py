#!/usr/bin/env python3
"""analisis_15m_v4_hibridos.py -- MISIÓN 15M v4, vía HÍBRIDA (08-Oct, Javi: orden 3 -> 2 -> 1). Disecciona las
híbridas direccionales persistentes (PnL > 0 los 3 días 05-07, analisis_15m_v4_tres_vias.py) que usan maker Y tomador
en el mismo mercado: 0xb970fb5c, 0x2ed94d1a, 0x9d57c42e, 0xb0c078c8, 0x14cbd313.
Por mercado (orden = hora del bloque): secuencia de rellenos por rol; la pata TOMADORA ¿REFUERZA (mismo lado que su
posición maker previa), CUBRE (lado contrario) o ABRE (sin posición previa)?; precio y T por rol; posición neta al
cierre (acciones del lado ganador menos perdedor), acierto direccional, PnL por rol; estado del contrato en cada
entrada (z_TWAP, z_spot, lead) con ticks Chainlink RECIBIDOS <= bloque - 2,06 s (estado_twap, sin mirar el futuro).
Solo EXTRACCIÓN 05-06; 07 como contraste.
Uso: nice -n 19 python3 analisis_15m_v4_hibridos.py
"""
import collections
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_b1_compradores_mes import refs_dia, twap_rtds  # noqa: E402
from analisis_15m_v4_twap_terminal_mes import estado_twap, ticks_dia  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
HIB = ["0xb970fb5c", "0x2ed94d1a", "0x9d57c42e", "0xb0c078c8", "0x14cbd313"]
INF = Path(__file__).resolve().parent / "informes" / "m15v4_hibridos_08oct.txt"


def main():
    X = pd.read_parquet(DL / "m15_ms_cache" / "v4_quien_gana.parquet",
                        columns=["wallet", "rol", "side", "dia", "act", "mkt", "fin", "lado", "ts_est", "acc", "usdc", "p", "T", "pnl", "des"])
    X["w"] = X.wallet.str[:10]
    X = X[X.w.isin(HIB)].sort_values(["w", "mkt", "ts_est"], kind="stable").copy()
    dias = sorted(X.dia.unique())
    PB, RT = {}, collections.defaultdict(lambda: [0.0, 0])
    for d in [(date.fromisoformat(dias[0]) - timedelta(days=1)).isoformat()] + dias:
        refs_dia(d, PB, RT)
    zt, zs, ld = [], [], []
    for d in dias:
        tk = ticks_dia(d)
        for r in X[X.dia == d].itertuples(index=False):
            e = None
            if r.act in tk:
                ref = PB.get((r.act, int(r.fin) - 900)) or twap_rtds(RT, r.act, int(r.fin) - 900)
                if ref is not None:
                    rv, ws, px = tk[r.act]
                    e = estado_twap(rv, ws, px, int(r.fin), int((r.ts_est - 2.06) * 1000), ref)
            s = (1 if r.lado == "YES" else -1) * (1 if r.side == 0 else -1)   # signo de la exposición que toma
            zt.append(s * e[1] if e else np.nan)
            zs.append(s * e[2] if e else np.nan)
            ld.append(s * e[0] * 1e4 if e else np.nan)
        del tk
    X = X[X.dia.isin(dias)]
    X["z_tw"], X["z_sp"], X["lead"] = zt, zs, ld
    # exposición YES firmada de cada relleno (+ acciones largas en YES)
    X["exp"] = np.where(X.side == 0, 1, -1) * np.where(X.lado == "YES", 1, -1) * X.acc
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    L(f"Híbridas direccionales — {len(X)} rellenos, días {dias} (EXTRACCIÓN 05-06, CONTRASTE 07)")
    for w in HIB:
        q = X[X.w == w]
        if q.empty:
            continue
        clases, merc = [], []
        for mkt, g in q.groupby("mkt", sort=False):
            pos = 0.0
            for r in g.itertuples(index=False):
                if r.rol == "tomador":
                    clases.append("ABRE" if abs(pos) < 1e-9 else ("REFUERZA" if np.sign(pos) == np.sign(r.exp) else "CUBRE"))
                pos += r.exp
            gana_yes = g.des.iloc[0] == "YES"
            merc.append({"mkt": mkt, "dia": g.dia.iloc[0], "neto": pos, "acierta": (pos > 0) == gana_yes if abs(pos) > 1e-9 else np.nan,
                         "pnl": g.pnl.sum(), "pnl_mk": g.pnl[g.rol == "maker"].sum(), "pnl_tk": g.pnl[g.rol == "tomador"].sum(),
                         "vol": g.usdc.sum(), "ambos": g.rol.nunique() == 2})
        M = pd.DataFrame(merc)
        c = pd.Series(clases).value_counts(normalize=True)
        L(f"\n== {w}: mercados {len(M)} (con ambos roles {int(M.ambos.sum())}), PnL {M.pnl.sum():+.0f} (maker {M.pnl_mk.sum():+.0f}, tomador {M.pnl_tk.sum():+.0f}), "
          f"vol {M.vol.sum():.0f}")
        L(f"   pata TOMADORA: " + ", ".join(f"{k} {v:.0%}" for k, v in c.items())
          + f" | posición neta al cierre: acierto direccional {M.acierta.mean():.1%} (n={int(M.acierta.notna().sum())}), "
          f"|neto| P50 {M.neto.abs().median():.0f} acc")
        for tramo, sel in (("05-06", q.dia <= "2026-10-06"), ("07", q.dia == "2026-10-07")):
            for rol in ("maker", "tomador"):
                r_ = q[sel & (q.rol == rol)]
                if len(r_) < 10:
                    continue
                L(f"   [{tramo} {rol:7s}] n={len(r_):5d} PnL {r_.pnl.sum():+7.0f} PnL/vol {r_.pnl.sum() / r_.usdc.sum():+.3f} | precio P25/50/75 "
                  f"{r_.p.quantile(.25):.2f}/{r_.p.median():.2f}/{r_.p.quantile(.75):.2f} | T P50 {r_['T'].median():.0f} | "
                  f"z_TWAP de la exposición P25/50/75 {r_.z_tw.quantile(.25):.2f}/{r_.z_tw.median():.2f}/{r_.z_tw.quantile(.75):.2f} | "
                  f"z_spot P50 {r_.z_sp.median():.2f} | lead P50 {r_.lead.median():.1f} bps | %BUY {(r_.side == 0).mean():.0%}")
        Md = M.groupby("dia").pnl.sum()
        L("   PnL por día: " + ", ".join(f"{k} {v:+.0f}" for k, v in Md.items()))
    INF.write_text("\n".join(lin) + "\n")


if __name__ == "__main__":
    main()
