#!/usr/bin/env python3
"""analisis_15m_v4_quien_gana.py -- MISIÓN 15M v4 §17/§43 (08-Oct): ¿QUIÉN gana dinero en el 15m y con qué ESTRUCTURA?
V3 solo miró a los TOMADORES. Aquí: TODOS los rellenos on-chain de 15m (datalogs/m15_onchain, formato verificado en
analisis_15m_v3_quien_barre.py: fila con taker == contrato del exchange = orden TOMADORA (su campo maker es la wallet
tomadora); resto = relleno de un MAKER (orden en reposo); side 0 BUY (maker_amt USDC, taker_amt acciones) / 1 SELL (al
revés); fee en USDC solo al tomador).
PnL a RESOLUCIÓN (desenlace oficial gamma) por fila: BUY acciones·gana − USDC; SELL USDC − acciones·gana; tomador además
− fee. Reembolso del maker ESTIMADO = 20 % de la comisión del tomador (rebateRate 0,2 verificado 07-Oct en gamma; el
programa real puede repartirlo distinto: se reporta aparte, nunca sumado al PnL de mercado).
Por wallet y rol: rellenos, mercados, volumen, PnL, PnL/volumen, por día; persistencia 06→07 (wallets con volumen ambos
días); concentración; PERFIL de las ganadoras: precio medio, % de rellenos en los últimos 120 s, mercados con relleno en
AMBOS lados (YES y NO), posición neta al cierre / volumen (plano = vive del spread; direccional = información).
Mapa token: tokens.json de la caché ms (05-06) + filas k del registro ms (07). Uso:
  (ulimit -v 5000000; nice -n 19 ionice -c3 python3 analisis_15m_v4_quien_gana.py)
"""
import gzip
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

DL = Path("/root/polymarket-research-datalogs")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
DIAS = ["2026-10-05", "2026-10-06", "2026-10-07"]
INF = Path(__file__).resolve().parent / "informes" / "m15v4_quien_gana_08oct.txt"


def mapa_tokens():
    m = {}
    for tok, act, mid, fin, lado in json.load(open(DL / "m15_ms_cache" / "tokens.json")):
        m[str(tok)] = (act, str(mid), int(fin), lado)
    for f in sorted(DL.glob("maker_ms_2026-10-0[5-8]_*.csv.gz")):
        out = subprocess.run(f"zcat {f} 2>/dev/null | grep -a '^k,'", shell=True, capture_output=True).stdout.decode()
        for ln in out.splitlines():
            c = ln.split(",")
            if len(c) >= 8 and c[4] == "15min":
                m[c[2]] = (c[3], c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
    return m


def main():
    tok = mapa_tokens()
    print(f"tokens 15m: {len(tok)}", file=sys.stderr)
    dfs = []
    for d in DIAS:
        with gzip.open(DL / "m15_onchain" / f"m15_onchain_{d}.csv.gz", "rt") as fh:
            x = pd.read_csv(fh, dtype={"token_id": str, "maker": str, "taker": str, "tx": str},
                            usecols=["tipo", "ts_est", "tx", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt", "fee"])
        x = x[(x.tipo == "F") & x.token_id.isin(tok.keys())]
        x["dia"] = d
        dfs.append(x)
    X = pd.concat(dfs, ignore_index=True)
    info = X.token_id.map(tok)
    X["act"] = info.str[0]
    X["mkt"] = info.str[1]
    X["fin"] = info.str[2]
    X["lado"] = info.str[3]
    des = desenlaces(set(X.mkt))
    X["des"] = X.mkt.map(des)
    cob = X.drop_duplicates("mkt").des.notna().mean()
    X = X[X.des.notna()].copy()
    buy = X.side == 0
    X["acc"] = np.where(buy, X.taker_amt, X.maker_amt).astype(float)
    X["usdc"] = np.where(buy, X.maker_amt, X.taker_amt).astype(float)
    X = X[X.acc > 0]
    X["p"] = X.usdc / X.acc
    win = (X.lado == X.des).astype(float)
    X["rol"] = np.where(X.taker == EXCH, "tomador", "maker")
    X["wallet"] = X.maker
    X["pnl"] = np.where(buy, X.acc * win - X.usdc, X.usdc - X.acc * win) - np.where(X.rol == "tomador", X.fee.astype(float), 0.0)
    X["T"] = X.fin - X.ts_est
    X["firm"] = np.where(buy, 1, -1) * np.where(X.lado == "YES", 1, -1)   # +1 = largo YES
    # comisión de tomadores por tx -> reembolso estimado repartido entre makers de esa tx por acciones
    fee_tx = X[X.rol == "tomador"].groupby("tx").fee.sum()
    mk = X.rol == "maker"
    acc_tx = X[mk].groupby("tx").acc.sum()
    X["rebate_est"] = 0.0
    X.loc[mk, "rebate_est"] = 0.2 * X.loc[mk, "tx"].map(fee_tx).fillna(0).values * X.loc[mk, "acc"].values / X.loc[mk, "tx"].map(acc_tx).values
    lin = []

    def L(s=""):
        print(s, flush=True)
        lin.append(s)
    L(f"Rellenos 15m on-chain {DIAS[0]}..{DIAS[-1]}: {len(X)} filas, {X.mkt.nunique()} mercados, cobertura desenlace {cob:.1%}")
    L("\n1) PnL AGREGADO A RESOLUCIÓN por rol y día (USDC)")
    g = X.groupby(["dia", "rol"]).agg(filas=("pnl", "size"), vol=("usdc", "sum"), pnl=("pnl", "sum"), fee=("fee", "sum"),
                                      rebate=("rebate_est", "sum"), wallets=("wallet", "nunique"))
    g["pnl_por_vol"] = g.pnl / g.vol
    L(g.round(3).to_string())
    W = X.groupby(["rol", "wallet", "dia"]).agg(n=("pnl", "size"), merc=("mkt", "nunique"), vol=("usdc", "sum"),
                                                 pnl=("pnl", "sum"), rebate=("rebate_est", "sum")).reset_index()
    for rol in ("maker", "tomador"):
        w = W[W.rol == rol].groupby("wallet").agg(dias=("dia", "nunique"), n=("n", "sum"), merc=("merc", "sum"),
                                                   vol=("vol", "sum"), pnl=("pnl", "sum"), rebate=("rebate", "sum"))
        w["pnl_vol"] = w.pnl / w.vol
        tot_pos = w.pnl[w.pnl > 0].sum()
        L(f"\n2) {rol.upper()}: {len(w)} wallets; PnL total {w.pnl.sum():+.0f}; ganancias brutas de las ganadoras {tot_pos:+.0f}; "
          f"top10 ganadoras = {w.pnl.nlargest(10).sum() / tot_pos:.0%} de ellas; top10 por volumen = {w.vol.nlargest(10).sum() / w.vol.sum():.0%} del volumen")
        L("   top 15 por PnL:")
        for wa, r in w.sort_values("pnl", ascending=False).head(15).iterrows():
            L(f"   {wa[:10]} días={r.dias} n={int(r.n):6d} vol={r.vol:9.0f} PnL={r.pnl:+8.0f} PnL/vol={r.pnl_vol:+.3f} rebate_est={r.rebate:6.0f}")
        L("   top 10 por VOLUMEN:")
        for wa, r in w.sort_values("vol", ascending=False).head(10).iterrows():
            L(f"   {wa[:10]} días={r.dias} n={int(r.n):6d} vol={r.vol:9.0f} PnL={r.pnl:+8.0f} PnL/vol={r.pnl_vol:+.3f} rebate_est={r.rebate:6.0f}")
        # persistencia 06 -> 07
        p = W[(W.rol == rol) & W.dia.isin(["2026-10-06", "2026-10-07"])].pivot_table(index="wallet", columns="dia", values=["pnl", "vol"])
        p = p.dropna()
        p = p[(p[("vol", "2026-10-06")] >= 2000) & (p[("vol", "2026-10-07")] >= 2000)]
        if len(p) >= 10:
            a = p[("pnl", "2026-10-06")] / p[("vol", "2026-10-06")]
            b = p[("pnl", "2026-10-07")] / p[("vol", "2026-10-07")]
            L(f"   PERSISTENCIA 06→07 ({len(p)} wallets con ≥2.000 USDC ambos días): Spearman PnL/vol {a.corr(b, method='spearman'):+.3f}; "
              f"positivas ambos días {int(((a > 0) & (b > 0)).sum())}, negativas ambos {int(((a < 0) & (b < 0)).sum())}, cambian {int(((a > 0) != (b > 0)).sum())}")
            gan = p[(a > 0) & (b > 0)]
            L(f"   ganadoras ambos días: PnL 06 {gan[('pnl', '2026-10-06')].sum():+.0f}, PnL 07 {gan[('pnl', '2026-10-07')].sum():+.0f}")
    # PERFIL de makers ganadores persistentes vs perdedores (volumen ≥2.000 en 06 y 07)
    L("\n3) PERFIL MAKERS (vol ≥2.000 USDC 06 y 07): ganadoras ambos días vs resto")
    M = X[(X.rol == "maker") & X.dia.isin(["2026-10-06", "2026-10-07"])]
    wd = M.groupby(["wallet", "dia"]).agg(vol=("usdc", "sum"), pnl=("pnl", "sum")).unstack()
    ok = wd.dropna()
    ok = ok[(ok[("vol", "2026-10-06")] >= 2000) & (ok[("vol", "2026-10-07")] >= 2000)]
    ganw = set(ok[(ok[("pnl", "2026-10-06")] > 0) & (ok[("pnl", "2026-10-07")] > 0)].index)
    perw = set(ok.index) - ganw

    def perfil(ws, nom):
        q = M[M.wallet.isin(ws)]
        if len(q) == 0:
            return
        pm = q.groupby(["wallet", "mkt"]).agg(ny=("lado", lambda s: (s == "YES").sum()), nn=("lado", lambda s: (s == "NO").sum()),
                                               neto=("firm", lambda s: 0), vol=("usdc", "sum"))
        ambos = ((pm.ny > 0) & (pm.nn > 0)).mean()
        q2 = q.assign(pos=q.firm * q.acc)
        neto = q2.groupby(["wallet", "mkt"]).pos.sum().abs().sum() / q2.acc.sum()
        L(f"  {nom}: wallets={len(ws)} rellenos={len(q)} vol={q.usdc.sum():.0f} PnL={q.pnl.sum():+.0f} PnL/vol={q.pnl.sum() / q.usdc.sum():+.4f} "
          f"rebate_est={q.rebate_est.sum():.0f} | precio medio {q.p.mean():.3f}, P(p<0,2 o >0,8) {((q.p < 0.2) | (q.p > 0.8)).mean():.0%}, "
          f"rellenos T<120s {(q['T'] < 120).mean():.0%}, T<300s {(q['T'] < 300).mean():.0%}, mercados con ambos lados {ambos:.0%}, "
          f"|posición neta| / acciones {neto:.2f}, tamaño mediano {q.acc.median():.0f} acc")
    perfil(ganw, "GANADORAS ambos días")
    perfil(perw, "RESTO (≥2.000 ambos días)")
    L("\n4) PnL MAKER por fase del ciclo y banda de precio (todos los makers, 3 días)")
    MM = X[X.rol == "maker"]
    t = MM.groupby([pd.cut(MM["T"], [-60, 0, 30, 120, 300, 600, 900, 2000]), pd.cut(MM.p, [0, 0.1, 0.3, 0.5, 0.7, 0.9, 1])], observed=True).agg(
        vol=("usdc", "sum"), pnl=("pnl", "sum"))
    t["pnl_vol"] = t.pnl / t.vol
    L(t.round(4).to_string())
    INF.write_text("\n".join(lin) + "\n")
    X.to_parquet(DL / "m15_ms_cache" / "v4_quien_gana.parquet")


if __name__ == "__main__":
    main()
