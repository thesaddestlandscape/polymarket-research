#!/usr/bin/env python3
"""analisis_mo_money_pares_5m.py — Misión pares 5m (Javi 14-Oct, @mo-money). SOLO LECTURA, on-chain (m5_onchain).

@mo-money = 0x32ed2e546b187ca15e2841edc82b22c713cf8ec3 (gamma public-search, perfil "mo-money"; cifras de su perfil
externas y SIN verificar: +496 k$ desde junio). Pregunta de arranque (Javi): ¿cómo EVITA la pata suelta?

Reconstruye CADA relleno suyo en mercados 5m (todas las monedas, todos los cierres) desde OrderFilled:
  fila con maker == wallet; side 0 compra (usdc = maker_amt, acc = taker_amt), side 1 venta (acc = maker_amt,
  usdc = taker_amt); taker == exchange -> su orden era TOMADORA (paga fee), si no MAKER.
Ledger por mercado en orden cronológico (hora de bloque): acciones y coste por lado tras cada relleno, primera pata,
segunda pata, tiempo hasta la primera unidad emparejada, máximo desequilibrio, residuo al final, ventas; PnL a
desenlace OFICIAL (gamma closed=true) descompuesto en PARES (min(QU,QD)·(1 − coste medio del par)) y RESIDUO.
Salida: datalogs/mo_money/mercados_D.csv.gz (caché por día), rellenos_D.csv.gz, informe.txt
Uso: nice -n 19 ionice -c3 python3 analisis_mo_money_pares_5m.py [--dias 2026-10-05,...]
"""
import argparse
import gzip
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_5m_barato_quien_gana import mapas, EXCH  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

W = "0x32ed2e546b187ca15e2841edc82b22c713cf8ec3"
OUT = Path("/root/polymarket-research-datalogs/mo_money")
DIAS = [f"2026-10-{d:02d}" for d in range(5, 14)]


def rellenos_dia(d):
    c = OUT / f"rellenos_{d}.csv.gz"
    if c.exists():
        return pd.read_csv(c, dtype={"mkt": str})
    tok = mapas(d)["5min"]
    f = VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz"
    if not f.exists():
        return None
    partes = []
    with gzip.open(f, "rt") as fh:
        for x in pd.read_csv(fh, chunksize=300_000, dtype={"token_id": str, "maker": str, "taker": str, "tx": str},
                             usecols=["tipo", "ts_est", "tx", "log_index", "maker", "taker", "side", "token_id",
                                      "maker_amt", "taker_amt", "fee"]):
            x = x[(x.tipo == "F") & (x.maker.str.lower() == W)]
            if not len(x):
                continue
            x = x[x.token_id.isin(tok.keys())]
            compra = x.side.values == 0
            partes.append(pd.DataFrame({
                "ts": x.ts_est.astype(float).values, "tx": x.tx.values, "li": x.log_index.values,
                "rol": np.where(x.taker.str.lower().values == EXCH, "T", "M"),
                "act": x.token_id.map(lambda t: tok[t][0]).values, "mkt": x.token_id.map(lambda t: tok[t][1]).values,
                "cierre": x.token_id.map(lambda t: tok[t][2]).values, "lado": x.token_id.map(lambda t: tok[t][3]).values,
                "compra": compra, "acc": np.where(compra, x.taker_amt.values, x.maker_amt.values).astype(float),
                "usdc": np.where(compra, x.maker_amt.values, x.taker_amt.values).astype(float),
                "fee": x.fee.astype(float).values}))
    if not partes:
        return None
    R = pd.concat(partes, ignore_index=True).sort_values(["ts", "li"])
    R["T"] = R.cierre - R.ts
    R["p"] = R.usdc / R.acc
    OUT.mkdir(parents=True, exist_ok=True)
    R.to_csv(c, index=False, compression="gzip")
    return R


def ledger(R, d):
    des = desenlaces(set(R.mkt.astype(str)))
    filas = []
    for mkt, g in R.groupby("mkt", sort=False):
        g = g.sort_values(["ts", "li"])
        q = {"YES": 0.0, "NO": 0.0}
        cst = {"YES": 0.0, "NO": 0.0}
        primera = g.iloc[0]
        t_par = None
        max_desq = 0.0
        ventas = int((~g.compra).sum())
        for r in g.itertuples():
            s = 1.0 if r.compra else -1.0
            q[r.lado] += s * r.acc
            cst[r.lado] += s * r.usdc + r.fee
            max_desq = max(max_desq, abs(q["YES"] - q["NO"]))
            if t_par is None and min(q["YES"], q["NO"]) > 0:
                t_par = primera["T"] - r.T          # s desde la 1ª pata hasta tener algo del otro lado
        r_ = des.get(str(mkt))
        pares = max(0.0, min(q["YES"], q["NO"]))
        pmY = cst["YES"] / q["YES"] if q["YES"] > 1e-9 else np.nan
        pmN = cst["NO"] / q["NO"] if q["NO"] > 1e-9 else np.nan
        coste = cst["YES"] + cst["NO"]
        pnl = (q[r_] - coste) if r_ else np.nan
        pnl_par = pares * (1.0 - pmY - pmN) if pares > 0 else 0.0
        segunda = g[g.lado != primera.lado]
        filas.append({
            "dia": d, "mkt": mkt, "act": primera.act, "des": r_ or "", "n_fills": len(g), "ventas": ventas,
            "lado1": primera.lado, "p1": round(primera.p, 4), "T1": round(primera["T"], 1), "rol1": primera.rol,
            "p2_primera": round(segunda.iloc[0].p, 4) if len(segunda) else np.nan,
            "T2_primera": round(segunda.iloc[0]["T"], 1) if len(segunda) else np.nan,
            "rol2": segunda.iloc[0].rol if len(segunda) else "", "seg_hasta_par": t_par,
            "qY": round(q["YES"], 3), "qN": round(q["NO"], 3), "pmY": pmY, "pmN": pmN, "coste_par": pmY + pmN,
            "max_desq": round(max_desq, 3), "resid": round(abs(q["YES"] - q["NO"]), 3),
            "frac_resid": abs(q["YES"] - q["NO"]) / max(q["YES"], q["NO"], 1e-9),
            "coste": round(coste, 4), "pnl": pnl, "pnl_pares": pnl_par,
            "pnl_resid": (pnl - pnl_par) if r_ else np.nan,
            "pct_M": round((g.rol == "M").mean(), 3), "vol": round(g.usdc.sum(), 2)})
    return pd.DataFrame(filas)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default=",".join(DIAS))
    a = ap.parse_args()
    M = []
    for d in a.dias.split(","):
        c = OUT / f"mercados_{d}.csv.gz"
        if c.exists():
            M.append(pd.read_csv(c, dtype={"mkt": str}))
            continue
        R = rellenos_dia(d)
        if R is None:
            continue
        L = ledger(R, d)
        L.to_csv(c, index=False, compression="gzip")
        M.append(L)
        print(f"{d}: {len(R)} rellenos, {len(L)} mercados", flush=True)
    M = pd.concat(M, ignore_index=True)
    ok = M[M.des != ""]
    lin = [f"@mo-money ({W[:10]}) 5m on-chain — {M.dia.min()}..{M.dia.max()}",
           f"mercados {len(M)} (desenlace oficial {len(ok)} = {len(ok) / len(M):.1%}) | volumen {M.vol.sum():,.0f} $ | "
           f"rellenos {int(M.n_fills.sum())} | % maker {np.average(M.pct_M, weights=M.n_fills):.1%} | ventas {int(M.ventas.sum())}",
           f"PnL total {ok.pnl.sum():+,.0f} $ = pares {ok.pnl_pares.sum():+,.0f} + residuo {ok.pnl_resid.sum():+,.0f} | "
           f"PnL/vol {ok.pnl.sum() / ok.vol.sum():+.2%}"]
    for nom, s in (("BTC", ok[ok.act == "BTC"]), ("resto", ok[ok.act != "BTC"])):
        if len(s):
            lin.append(f"  {nom:5s}: merc {len(s)} PnL {s.pnl.sum():+,.0f} (pares {s.pnl_pares.sum():+,.0f} resid {s.pnl_resid.sum():+,.0f})"
                       f" PnL/vol {s.pnl.sum() / s.vol.sum():+.2%}")
    pd_ = ok.groupby("dia").pnl.sum()
    lin.append("PnL por día: " + " ".join(f"{k[5:]} {v:+.0f}" for k, v in pd_.items()))
    lin.append("\n¿CÓMO EVITA LA PATA SUELTA?")
    lin.append(f"  mercados con los dos lados: {(ok.qY.gt(0) & ok.qN.gt(0)).mean():.1%} | residuo/mayor lado mediana "
               f"{ok.frac_resid.median():.2f} p75 {ok.frac_resid.quantile(.75):.2f}")
    lin.append(f"  coste del par (medio por mercado con ambos) mediana {ok.coste_par.median():.3f} p25 {ok.coste_par.quantile(.25):.3f} p75 {ok.coste_par.quantile(.75):.3f}")
    lin.append(f"  1ª pata: precio mediano {ok.p1.median():.2f}, T mediana {ok.T1.median():.0f} s, rol maker {(ok.rol1 == 'M').mean():.0%}; "
               f"2ª pata: precio mediano {ok.p2_primera.median():.2f}, T {ok.T2_primera.median():.0f} s, rol maker {(ok.rol2 == 'M').mean():.0%}; "
               f"s hasta el 1er par mediana {ok.seg_hasta_par.median():.0f}")
    for lo, hi in ((0, 0.05), (0.05, 0.2), (0.2, 0.5), (0.5, 1.01)):
        s = ok[(ok.frac_resid >= lo) & (ok.frac_resid < hi)]
        if len(s):
            lin.append(f"  residuo/mayor en [{lo:.2f},{hi:.2f}): {len(s)} merc ({len(s) / len(ok):.0%}) PnL {s.pnl.sum():+,.0f} "
                       f"(pares {s.pnl_pares.sum():+,.0f} resid {s.pnl_resid.sum():+,.0f})")
    for lo, hi in ((0, 0.3), (0.3, 0.5), (0.5, 0.7), (0.7, 1.01)):
        s = ok[(ok.p1 >= lo) & (ok.p1 < hi)]
        if len(s):
            lin.append(f"  1ª pata a precio [{lo:.1f},{hi:.1f}): {len(s)} merc, con ambos lados {(s.qY.gt(0) & s.qN.gt(0)).mean():.0%}, "
                       f"PnL {s.pnl.sum():+,.0f} (resid {s.pnl_resid.sum():+,.0f})")
    txt = "\n".join(lin)
    print(txt)
    (OUT / "informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
