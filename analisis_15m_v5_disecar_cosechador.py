#!/usr/bin/env python3
"""analisis_15m_v5_disecar_cosechador.py -- MISIÓN 15M v5 (13-Oct) PASO 5: ¿POR QUÉ 0x2903c7dc gana de forma persistente
(8/8 días, coste/par 0,967, residual pequeño) y 0xcfddfb6e no? Iteración 1 (m15v5_pares_cola_onchain_13oct.txt) descartó
la PRIORIDAD de cola. Aquí, solo on-chain (mismo cargador y unidades que analisis_15m_v5_pares_cola_onchain.py):
  a) SELECCIÓN de mercados: qué mercados BTC 15m toca cada wallet y cómo le fue al RESTO de cosechadores en los que salta.
  b) CUÁNDO: rellenos y PnL/acción por fase (T restante) y banda de precio.
  c) INVENTARIO: desequilibrio máximo por mercado, tiempo hasta completar cada acción emparejada, residual por mercado.
  d) PATA TOMADORA: ¿usa órdenes tomadoras? cuántas, cuándo (respecto a sus rellenos maker), con qué resultado.
  e) TAMAÑO y precio relativo: acciones por relleno, ¿compra el lado barato o el caro?
Todo por periodo DESC 05-07 / FORWARD 08-12. Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v5_disecar_cosechador.py)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_15m_v5_pares_cola_onchain as B  # noqa: E402

INF = Path(__file__).resolve().parent / "informes" / "m15v5_disecar_cosechador_13oct.txt"
W = ["0x2903c7dc", "0xcfddfb6e", "0xb945945d", "0x758dac51", "0x86b9a88a", "0x98b84283"]


def main():
    X = pd.concat([B.cargar(d) for d in B.DIAS], ignore_index=True)
    for c in ("tx", "token_id", "act", "mkt", "lado", "dia", "maker"):
        X[c] = X[c].astype(str).astype("category")
    des = B.desenlaces(set(X.mkt.astype(str)))
    X["des"] = X.mkt.astype(str).map(des)
    X = X[X.des.notna() & (X.act == "BTC")].copy()
    buy = X.side == 0
    X["acc"] = np.where(buy, X.taker_amt, X.maker_amt).astype(float)
    X["usdc"] = np.where(buy, X.maker_amt, X.taker_amt).astype(float)
    X = X[X.acc > 0].copy()
    X["p"] = X.usdc / X.acc
    X["buy"] = buy[X.index]
    win = (X.lado.astype(str) == X.des).astype(float)
    X["fee"] = X.fee.astype(float).fillna(0)
    X["rol"] = np.where(X.es_tom, "tomador", "maker")
    X["wallet"] = X.maker.astype(str)
    X["pnl"] = np.where(X.buy, X.acc * win - X.usdc, X.usdc - X.acc * win) - np.where(X.rol == "tomador", X.fee, 0.0)
    X["T"] = X.fin - X.ts_est
    X["per"] = np.where(X.dia.astype(str).isin(B.DESC), "DESC", "FWD")
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)

    mk = X[X.rol == "maker"]
    todos = mk.groupby("per").mkt.nunique()
    L(f"BTC 15m, mercados con algún relleno maker: DESC {todos.get('DESC', 0)}, FWD {todos.get('FWD', 0)}")

    # pnl por (wallet, mercado) maker
    def por_merc(s):
        s = s.assign(by=np.where(s.buy & (s.lado == "YES"), s.acc, 0.0), cy=np.where(s.buy & (s.lado == "YES"), s.usdc, 0.0),
                     bn=np.where(s.buy & (s.lado == "NO"), s.acc, 0.0), cn=np.where(s.buy & (s.lado == "NO"), s.usdc, 0.0))
        g = s.groupby(["per", "mkt"], observed=True).agg(by=("by", "sum"), cy=("cy", "sum"), bn=("bn", "sum"), cn=("cn", "sum"),
                                                         pnl=("pnl", "sum"), n=("pnl", "size"), t1=("T", "max"), tz=("T", "min"))
        g["emp"] = np.minimum(g.by, g.bn)
        g["cp"] = g.cy / g.by.replace(0, np.nan) + g.cn / g.bn.replace(0, np.nan)
        g["margen"] = g.emp * (1 - g.cp.fillna(1))
        g["resid"] = g.pnl - g.margen
        g["desbal"] = (g.by - g.bn).abs()
        return g

    grupos = {w: por_merc(mk[mk.wallet == w]) for w in W}
    L("\n(a) SELECCIÓN: ¿qué mercados salta cada wallet? PnL de los OTROS cosechadores (W sin ella) en sus mercados vs en los que salta")
    for w in W:
        g = grupos[w]
        for per in ("DESC", "FWD"):
            si = set(g.loc[per].index) if per in g.index.get_level_values(0) else set()
            tot = set(mk[mk.per == per].mkt.unique())
            otros = pd.concat([grupos[o].loc[per] for o in W if o != w and per in grupos[o].index.get_level_values(0)])
            o_si = otros[otros.index.isin(si)]
            o_no = otros[~otros.index.isin(si)]
            L(f"   {w} {per}: toca {len(si)}/{len(tot)} merc ({len(si) / max(len(tot), 1):.0%}) | otros en SUS merc PnL/merc-wallet "
              f"{o_si.pnl.mean():+.2f} (n {len(o_si)}) vs en los que SALTA {o_no.pnl.mean():+.2f} (n {len(o_no)})")

    L("\n(b) CUÁNDO y DÓNDE: rellenos maker por fase y banda, PnL/acción (FWD)")
    bins_T = [0, 60, 120, 300, 600, 840, 900, 2000]
    bins_p = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
    for w in W[:2]:
        s = mk[(mk.wallet == w) & (mk.per == "FWD")]
        t = s.groupby([pd.cut(s["T"], bins_T), pd.cut(s.p, bins_p)], observed=True).agg(acc=("acc", "sum"), pnl=("pnl", "sum"))
        t["pnl_acc"] = t.pnl / t.acc
        t["%acc"] = t.acc / t.acc.sum()
        L(f"  {w}:\n" + t[t["%acc"] > 0.01].round(4).to_string())

    L("\n(c) INVENTARIO por mercado (medianas; FWD y DESC)")
    for w in W:
        g = grupos[w]
        for per in ("DESC", "FWD"):
            if per not in g.index.get_level_values(0):
                continue
            q = g.loc[per]
            L(f"   {w} {per}: merc {len(q)} | acc compradas P50 {(q.by + q.bn).median():.0f} | desbal final P50 {q.desbal.median():.1f} "
              f"P90 {q.desbal.quantile(.9):.1f} | desbal/compras {(q.desbal / (q.by + q.bn)).median():.3f} | coste/par P50 {q.cp.median():.3f} "
              f"| merc con residual <0 {(q.resid < 0).mean():.0%} | 1er relleno T P50 {q.t1.median():.0f} | último T P50 {q.tz.median():.0f}"
              f" | PnL/merc {q.pnl.mean():+.2f} (margen {q.margen.mean():+.2f}, resid {q.resid.mean():+.2f})")

    L("\n(c2) desequilibrio DURANTE el mercado: P90 de |YES−NO| acumulado tras cada relleno (FWD) y espera hasta emparejar")
    for w in W[:2]:
        s = mk[(mk.wallet == w) & (mk.per == "FWD") & mk.buy].sort_values("ts_est")
        s = s.assign(sg=np.where(s.lado == "YES", s.acc, -s.acc))
        s["inv"] = s.groupby("mkt", observed=True).sg.cumsum()
        mx = s.groupby("mkt", observed=True).inv.apply(lambda v: v.abs().max())
        L(f"   {w}: max|inv| por mercado P50 {mx.median():.0f} P90 {mx.quantile(.9):.0f}; |inv| medio tras relleno {s.inv.abs().mean():.1f}; "
          f"tamaño relleno P50 {s.acc.median():.1f} P90 {s.acc.quantile(.9):.1f}")

    L("\n(d) PATA TOMADORA de cada wallet (todas las monedas no: solo BTC 15m)")
    tk = X[X.rol == "tomador"]
    for w in W:
        for per in ("DESC", "FWD"):
            s = tk[(tk.wallet == w) & (tk.per == per)]
            m = mk[(mk.wallet == w) & (mk.per == per)]
            if len(m) == 0:
                continue
            L(f"   {w} {per}: tomador n {len(s)} vol {s.usdc.sum():.0f} ({s.usdc.sum() / max(m.usdc.sum(), 1):.1%} del maker) PnL {s.pnl.sum():+.0f} "
              f"(PnL/$ {s.pnl.sum() / max(s.usdc.sum(), 1e-9):+.3f}) | comisión {s.fee.sum():.0f} | ventas maker {(~m.buy).mean():.1%}")

    L("\n(e) ¿qué lado compra? precio del lado comprado vs 0,5 y resultado por lado caro/barato (maker, FWD)")
    for w in W[:2]:
        s = mk[(mk.wallet == w) & (mk.per == "FWD") & mk.buy]
        bar = s.p < 0.5
        L(f"   {w}: barato (<0,5) {s[bar].acc.sum() / s.acc.sum():.0%} de acciones PnL/acc {s[bar].pnl.sum() / s[bar].acc.sum():+.4f} | "
          f"caro {s[~bar].pnl.sum() / s[~bar].acc.sum():+.4f}")
    L("\n(f) PnL por día (FWD+DESC) de cada wallet")
    for w in W:
        s = mk[mk.wallet == w].groupby("dia", observed=True).pnl.sum()
        L(f"   {w}: " + " ".join(f"{d[5:]}:{v:+.0f}" for d, v in s.items()))
    INF.write_text("\n".join(lin) + "\n")
    L(f"\n→ {INF}")


if __name__ == "__main__":
    main()
