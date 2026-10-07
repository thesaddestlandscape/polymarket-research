#!/usr/bin/env python3
"""analisis_15m_v3_quien_barre.py -- MISIÓN 15M V3 §15-17 (07-Oct): ¿QUIÉN barre a los makers de 15m y con qué MECANISMO?
Fase 1 dejó: la selección adversa del maker es un SALTO DISCRETO simultáneo al relleno (mid ya −5/−6 c en el instante).
Aquí, con la única fuente con identidad (on-chain, datalogs/m15_onchain/m15_onchain_D.csv.gz, formato verificado:
  fila del TOMADOR = la que lleva taker == contrato del exchange; su campo maker es la wallet tomadora; side 0 BUY / 1 SELL;
  BUY: maker_amt = USDC, taker_amt = acciones; SELL al revés; fee en USDC = 0,07·p·(1−p)·acciones),
cada ORDEN TOMADORA (una por tx) se pasa a términos YES del mercado (comprar NO = vender YES a 1−p) y se mide:
  - mid YES del registro ms (caché m15_ms_cache, top del libro, hora del exchange) en bloque−3 s (antes) y bloque+5/+30 s;
  - salto = mid(+5 s) − mid(−3 s) en la dirección del tomador; BARRIDO = salto >= 4 c (la hora del bloque es ±2 s);
  - markout a +30 s y PnL a resolución neto de su comisión, por acción y por USDC.
Por wallet tomadora: n órdenes, mercados, días, volumen, % barridos, EV a resolución por USDC, markout, fase del ciclo,
tamaño. Concentración de los barridos (top 1/10 wallets) y PLACEBO: tomadoras sin barrido.
Uso: (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v3_quien_barre.py)
"""
import gzip
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from m15_ms_cache import cargar  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
DIAS = ["2026-10-05", "2026-10-06"]
OUT = DL / "m15_ms_cache" / "v3_quien_barre.parquet"
INF = Path(__file__).resolve().parent / "informes" / "m15v3_quien_barre_07oct.txt"


def leer_onchain():
    dfs = []
    for d in DIAS:
        f = DL / "m15_onchain" / f"m15_onchain_{d}.csv.gz"
        with gzip.open(f, "rt") as fh:
            x = pd.read_csv(fh, dtype={"token_id": str, "maker": str, "taker": str, "tx": str})
        dfs.append(x[x.tipo == "F"])
    return pd.concat(dfs, ignore_index=True)


def main():
    C = cargar()
    q, T, X = C["q"], C["t"], C["x"]
    bt = np.searchsorted(T["tok"], np.arange(len(C["tokens"]) + 1))
    MON = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
    xs = {}
    for k, m in enumerate(MON):
        sel = X["s"] == k
        o = np.argsort(X["tr"][sel], kind="stable")
        xs[m] = (X["tr"][sel][o], X["p"][sel][o])

    def bin_ret(act, t, h):
        tr, pp = xs[act]
        k1, k0 = np.searchsorted(tr, t, side="right") - 1, np.searchsorted(tr, t - h, side="right") - 1
        if k0 < 0 or k1 < 0:
            return np.nan
        return (pp[k1] / pp[k0] - 1) * 1e4
    toks = C["tokens"]                       # (token, act, mid, fin, lado)
    tokinfo = {str(t[0]): (i, t[1], str(t[2]), int(t[3]), t[4]) for i, t in enumerate(toks)}
    bq = np.searchsorted(q["tok"], np.arange(len(toks) + 1))
    des = desenlaces({str(t[2]) for t in toks})

    oc = leer_onchain()
    print("filas on-chain", len(oc), file=sys.stderr)
    # niveles de maker por tx (precios distintos en términos del token del tomador no son triviales con mint/merge:
    # contamos makers y tokens distintos como medida de "barrido" estructural)
    mk = oc[oc.taker != EXCH]
    nmk = mk.groupby("tx").size().rename("n_makers")
    tk = oc[oc.taker == EXCH].copy()
    tk = tk[tk.token_id.isin(tokinfo.keys())]
    tk = tk.join(nmk, on="tx")
    buy = tk.side == 0
    tk["acc"] = np.where(buy, tk.taker_amt, tk.maker_amt).astype(float)
    tk["usdc"] = np.where(buy, tk.maker_amt, tk.taker_amt).astype(float)
    tk = tk[tk.acc > 0]
    tk["p"] = tk.usdc / tk.acc
    filas = []
    for r in tk.itertuples(index=False):
        i, act, mid_, fin, lado = tokinfo[r.token_id]
        if mid_ not in des:
            continue
        # dirección y precio en términos YES
        larga_tok = 1 if r.side == 0 else -1
        d = larga_tok if lado == "YES" else -larga_tok
        p_yes = r.p if lado == "YES" else 1 - r.p
        a, b = bq[i], bq[i + 1]
        te = q["te"][a:b]
        if len(te) < 20:
            continue
        bb, ba = q["bb"][a:b].astype(np.float64), q["ba"][a:b].astype(np.float64)
        t0 = int(r.ts_est * 1000)

        def mid(t):
            k = np.searchsorted(te, t, side="right") - 1
            if k < 0 or not (np.isfinite(bb[k]) and np.isfinite(ba[k])):
                return np.nan
            m = (bb[k] + ba[k]) / 2
            return m if lado == "YES" else 1 - m
        m_pre, m5, m30 = mid(t0 - 3000), mid(t0 + 5000), mid(t0 + 30_000)
        # emparejar con la fila t del registro ms (mismo token, lado tomador, tamaño) en [bloque−8 s, bloque+3 s]
        ta, tb_ = bt[i], bt[i + 1]
        j0 = ta + np.searchsorted(T["te"][ta:tb_], t0 - 8000)
        j1 = ta + np.searchsorted(T["te"][ta:tb_], t0 + 3000)
        te_ms = tr_ms = np.nan
        lado_t = 1 if r.side == 0 else 0
        best = 1e9
        for j in range(j0, j1):
            if T["side"][j] == lado_t and abs(float(T["sz"][j]) - r.acc) < 0.02 and abs(T["te"][j] - t0) < best:
                best, te_ms, tr_ms = abs(T["te"][j] - t0), T["te"][j], T["tr"][j]
        b500 = b2000 = bpost = np.nan
        if np.isfinite(tr_ms):
            b500, b2000, bpost = d * bin_ret(act, tr_ms, 500), d * bin_ret(act, tr_ms, 2000), d * bin_ret(act, tr_ms + 2000, 2000)
        win = 1.0 if des[mid_] == "YES" else 0.0
        fee_acc = float(r.fee) / r.acc
        filas.append(dict(wallet=r.maker, tx=r.tx, act=act, mkt=mid_, fin=fin, t=t0, dia=DIAS[0] if t0 < 1791244800000 else DIAS[1],
                          d=d, p=p_yes, acc=r.acc, usdc=r.usdc, fee=float(r.fee), n_makers=r.n_makers,
                          t_cierre=fin - t0 / 1000, salto=d * (m5 - m_pre), mk30=d * (m30 - p_yes),
                          res=d * (win - p_yes) - fee_acc, te_ms=te_ms, tr_ms=tr_ms, b500=b500, b2000=b2000, bpost=bpost))
    R = pd.DataFrame(filas)
    R.to_parquet(OUT)
    R = R[(R.t_cierre > 0) & (R.t_cierre <= 900)]
    R["barrido"] = R.salto >= 0.04
    R["res_usdc"] = R.res * R.acc
    L = []
    P = lambda *a: L.append(" ".join(str(x) for x in a))
    P(f"MISIÓN 15M V3 §15-17 — quién barre (on-chain {DIAS}, tomadoras en tokens 15m de la caché ms). Órdenes: {len(R)}")
    P(f"barridos (salto mid −3s→+5s >= 4c a favor del tomador): {R.barrido.sum()} ({R.barrido.mean():.1%}); "
      f"volumen barridos {R[R.barrido].usdc.sum():,.0f} $ de {R.usdc.sum():,.0f} $")
    for nom, g in (("BARRIDOS", R[R.barrido]), ("NO barridos", R[~R.barrido])):
        P(f"  {nom}: n={len(g)} EV res/acción {g.res.mean():+.4f}  PnL res {g.res_usdc.sum():+,.0f} $ "
          f"({g.res_usdc.sum() / g.usdc.sum():+.3%}/$)  mk30 {g.mk30.mean():+.4f}  tamaño mediano {g.usdc.median():.1f} $  "
          f"makers/tx mediana {g.n_makers.median():.0f}  t_cierre mediana {g.t_cierre.median():.0f} s")
    # wallets
    W = R.groupby("wallet").agg(n=("tx", "size"), mercados=("mkt", "nunique"), dias=("dia", "nunique"), usdc=("usdc", "sum"),
                                n_barr=("barrido", "sum"), pnl=("res_usdc", "sum"), mk30=("mk30", "mean"),
                                t_cierre=("t_cierre", "median"), tam=("usdc", "median"), acts=("act", "nunique"))
    W["ev_usdc"] = W.pnl / W.usdc
    W["pct_barr"] = W.n_barr / W.n
    tb = R[R.barrido].groupby("wallet").usdc.sum().sort_values(ascending=False)
    P(f"\nwallets tomadoras: {len(W)}; con algún barrido: {(W.n_barr > 0).sum()}; "
      f"top1 = {tb.iloc[0] / tb.sum():.1%} del volumen barrido, top10 = {tb.iloc[:10].sum() / tb.sum():.1%}, "
      f"top50 = {tb.iloc[:50].sum() / tb.sum():.1%}")
    P("\nTOP 25 por volumen BARRIDO (n órdenes, mercados, días, monedas, % barrido, EV res por $ de TODAS sus órdenes, mk30, t_cierre mediano, tamaño mediano):")
    for w in tb.index[:25]:
        x = W.loc[w]
        P(f"  {w[:10]} barr {tb[w]:>9,.0f} $  n={int(x.n):>5} merc={int(x.mercados):>4} d={int(x.dias)} mon={int(x.acts)} "
          f"%barr {x.pct_barr:5.1%}  EV/$ {x.ev_usdc:+.3f}  mk30 {x.mk30:+.4f}  tc {x.t_cierre:4.0f}s  tam {x.tam:7.1f} $")
    grandes = W[(W.n >= 100) & (W.mercados >= 40)]
    P(f"\nwallets con n>=100 y >=40 mercados: {len(grandes)}; EV/$ >0 en ambos días? (abajo, top 15 por PnL)")
    porDia = R.groupby(["wallet", "dia"]).apply(lambda g: g.res_usdc.sum() / g.usdc.sum(), include_groups=False).unstack()
    for w in grandes.sort_values("pnl", ascending=False).index[:15]:
        x = W.loc[w]
        dd = " ".join(f"{v:+.3f}" if np.isfinite(v) else "  nan " for v in porDia.loc[w].values)
        P(f"  {w[:10]} PnL {x.pnl:+8,.0f} $ vol {x.usdc:9,.0f} EV/$ {x.ev_usdc:+.3f} por día [{dd}] %barr {x.pct_barr:5.1%} "
          f"mk30 {x.mk30:+.4f} tc {x.t_cierre:4.0f}s tam {x.tam:6.1f}")
    # fase del ciclo de los barridos vs placebo
    P("\nfase del ciclo (t_cierre) — % de barridos y EV res/acción de los barridos:")
    for lo, hi in ((720, 900), (540, 720), (360, 540), (180, 360), (60, 180), (0, 60)):
        g = R[(R.t_cierre > lo) & (R.t_cierre <= hi)]
        gb = g[g.barrido]
        P(f"  T-{hi:>3}..T-{lo:<3}: n={len(g):>6} %barr {g.barrido.mean():5.1%}  EV barr {gb.res.mean():+.4f}  EV no-barr {g[~g.barrido].res.mean():+.4f}")
    P("\npor moneda: % barridos, EV barr / no-barr")
    for a_, g in R.groupby("act"):
        P(f"  {a_:5} n={len(g):>6} %barr {g.barrido.mean():5.1%} EV barr {g[g.barrido].res.mean():+.4f} no {g[~g.barrido].res.mean():+.4f}")
    M = R[np.isfinite(R.tr_ms)]
    P(f"\nemparejadas con fila t del registro ms: {len(M)} de {len(R)} ({len(M) / len(R):.1%}); bloque − hora exchange mediana "
      f"{np.nanmedian(M.t - M.te_ms):.0f} ms")
    P("MECANISMO sin look-ahead: retorno de Binance (nuestro reloj de recepción) en los 500 ms / 2 s PREVIOS a la operación, "
      "en la dirección del tomador → EV res/acción, mk30, % barrido")
    for nom, col in (("500ms", "b500"), ("2s", "b2000")):
        for lo, hi in ((-1e9, -3), (-3, -1), (-1, 1), (1, 3), (3, 6), (6, 1e9)):
            g = M[(M[col] > lo) & (M[col] <= hi)]
            if len(g) < 30:
                continue
            P(f"  {nom} Binance ({lo:>5},{hi:>5}] bps: n={len(g):>6} EV res {g.res.mean():+.4f} mk30 {g.mk30.mean():+.4f} %barr {g.barrido.mean():5.1%} "
              f"PnL/$ {g.res_usdc.sum() / g.usdc.sum():+.3f}")
    P("  (control: Binance en los 2 s POSTERIORES, en dirección del tomador, mediana) barridos "
      f"{M[M.barrido].bpost.median():+.2f} bps / no barridos {M[~M.barrido].bpost.median():+.2f} bps")
    P("\nwallets top (n>=200 emparejadas): % de órdenes con Binance 2 s previos >= +3 bps a favor, EV/$ por día")
    Mw = M.groupby("wallet").agg(n=("tx", "size"), pre3=("b2000", lambda v: (v >= 3).mean()), mk30=("mk30", "mean"),
                                 usdc=("usdc", "sum"), pnl=("res_usdc", "sum"))
    Mw = Mw[Mw.n >= 200]
    Mw["ev"] = Mw.pnl / Mw.usdc
    P(f"  base de todas las tomadoras: pre>=3bps {(M.b2000 >= 3).mean():.1%}")
    for w, x in Mw.sort_values("pre3", ascending=False).head(20).iterrows():
        dd = " ".join(f"{v:+.3f}" if np.isfinite(v) else "  nan " for v in porDia.loc[w].values)
        P(f"  {w[:10]} n={int(x.n):>5} pre>=3bps {x.pre3:5.1%} mk30 {x.mk30:+.4f} EV/$ {x.ev:+.3f} [{dd}] vol {x.usdc:9,.0f}")
    INF.write_text("\n".join(L) + "\n")
    print("\n".join(L))


if __name__ == "__main__":
    main()
