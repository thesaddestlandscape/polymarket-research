#!/usr/bin/env python3
"""analisis_5m_barato_quien_gana.py -- MISIÓN 5m barato (Javi 14-Oct: "entender la estrategia de absolutamente todas las
wallets que ganan en este mercado, lo visible y lo invisible"). SOLO LECTURA, on-chain (m5_onchain / m15_onchain).

Universo = los PARES de 5m barato: mercados 5m que cierran a la vez que un 15m (cierre % 900 == 0) y su 15m.
Contabilidad por fila de relleno (OrderFilled), desde el punto de vista del dueño de la orden de esa fila:
  side 0 (compra): usdc = maker_amt, acciones = taker_amt;  side 1 (venta): acciones = maker_amt, usdc = taker_amt.
  Fila con taker == exchange = la orden TOMADORA (paga comisión `fee`); resto = orden MAKER (comisión 0).
  PnL a resolución OFICIAL: compra acc·1{gana} - usdc; venta usdc - acc·1{gana}; menos comisión. Reembolso de maker NO
  incluido (se estima aparte: 20 % de la comisión de los tomadores que cruzaron contra él).
Por wallet: PnL 5m (maker / tomador), PnL 15m entero y solo últimos 5 min (T<=300 s), volumen, mercados, días con PnL>0,
cierres en los que opera los DOS horizontes (cruce 5m-15m) y si en ellos compra el mismo lado ("dirección") o lados
opuestos ("cobertura/valor relativo").
Uso: nice -n 19 ionice -c3 python3 analisis_5m_barato_quien_gana.py --desde 2026-10-06 --hasta 2026-10-13
Salida: datalogs/m5barato_mision/quien_gana_wallets.csv, quien_gana_fills_D.csv.gz (caché), quien_gana_informe.txt
"""
import argparse
import gzip
import sys
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"


_CACHE_K = {}


def _k_fichero(f):
    from datetime import datetime
    if f in _CACHE_K:
        return _CACHE_K[f]
    m = {"5min": {}, "15min": {}}
    if f.exists():
        with gzip.open(f, "rt", errors="replace") as fh:
            try:
                for ln in fh:
                    if ln.startswith("k,"):
                        c = ln.rstrip("\n").split(",")
                        if len(c) >= 8 and c[4] in m:
                            m[c[4]][c[2]] = (c[3], c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
            except (EOFError, OSError):
                pass
    _CACHE_K[f] = m
    return m


def mapas(d):
    """token -> (activo, mercado, cierre, lado) de 5m y 15m (registros de d-1, d, d+1; caché por fichero)."""
    m = {"5min": {}, "15min": {}}
    for k in (-1, 0, 1):
        dd = (date.fromisoformat(d) + timedelta(days=k)).isoformat()
        for pref in ("m15", "m5"):
            mk = _k_fichero(VOL / f"{pref}_registro" / f"{pref}_registro_{dd}.csv.gz")
            for mar in m:
                m[mar].update(mk[mar])
    return m


def fills_dia(d):
    mp = mapas(d)
    t5 = {t: v for t, v in mp["5min"].items() if v[2] % 900 == 0}
    t15 = mp["15min"]
    partes = []
    for marco, tok, f in (("5m", t5, VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz"),
                          ("15m", t15, VOL / "m15_onchain" / f"m15_onchain_{d}.csv.gz")):
        if not f.exists():
            print(f"  {d}: falta {f.name}", file=sys.stderr)
            continue
        with gzip.open(f, "rt") as fh:
            for x in pd.read_csv(fh, chunksize=200_000, dtype={"token_id": str, "maker": str, "taker": str, "tx": str},
                                 usecols=["tipo", "ts_est", "tx", "maker", "taker", "side", "token_id", "maker_amt",
                                          "taker_amt", "fee"]):
                x = x[(x.tipo == "F") & x.token_id.isin(tok.keys())]
                if not len(x):
                    continue
                compra = x.side.values == 0
                tk = x.token_id
                partes.append(pd.DataFrame({
                    "marco": marco, "wallet": x.maker.str.lower().values,
                    "rol": np.where(x.taker.values == EXCH, "T", "M"), "act": tk.map(lambda t: tok[t][0]).values,
                    "mkt": tk.map(lambda t: tok[t][1]).values, "cierre": tk.map(lambda t: tok[t][2]).values,
                    "lado": tk.map(lambda t: tok[t][3]).values, "ts": x.ts_est.astype(float).values,
                    "compra": compra,
                    "acc": np.where(compra, x.taker_amt.values, x.maker_amt.values).astype(float),
                    "usdc": np.where(compra, x.maker_amt.values, x.taker_amt.values).astype(float),
                    "fee": x.fee.astype(float).values}))
    if not partes:
        return None
    X = pd.concat(partes, ignore_index=True)
    X["wallet"] = X.wallet.astype("category")
    X["T"] = X.cierre - X.ts
    des = desenlaces(set(X.mkt.astype(str)))
    X["des"] = X.mkt.astype(str).map(des)
    X["cob"] = X.des.notna()
    gana = (X.des == X.lado).astype(float)
    X["pnl"] = np.where(X.compra, X.acc * gana - X.usdc, X.usdc - X.acc * gana) - X.fee
    # comisión que pagaron los tomadores de cada tx -> reembolso estimado 20 % repartido entre makers por volumen
    X["dia"] = d
    return X


def agregar(X):
    """Agregados por wallet de un día (para no tener todos los días en memoria)."""
    X = X[X.cob]
    m5 = X.marco == "5m"
    A = pd.DataFrame({
        "pnl5_M": X[m5 & (X.rol == "M")].groupby("wallet").pnl.sum(), "pnl5_T": X[m5 & (X.rol == "T")].groupby("wallet").pnl.sum(),
        "fee5": X[m5].groupby("wallet").fee.sum(), "vol5": X[m5].groupby("wallet").usdc.sum(),
        "volT5": X[m5 & (X.rol == "T")].groupby("wallet").usdc.sum(), "n_mkt5": X[m5].groupby("wallet").mkt.nunique(),
        "pnl15": X[~m5].groupby("wallet").pnl.sum(), "pnl15_ult5": X[~m5 & (X["T"] <= 300)].groupby("wallet").pnl.sum(),
        "vol15": X[~m5].groupby("wallet").usdc.sum()}).fillna(0.0)
    k5 = X[m5][["wallet", "act", "cierre"]].drop_duplicates()
    k15 = X[~m5 & (X["T"] <= 300)][["wallet", "act", "cierre"]].drop_duplicates()
    A["cierres_cruce"] = k5.merge(k15, on=["wallet", "act", "cierre"]).groupby("wallet").size().reindex(A.index).fillna(0)
    A["cierres5"] = k5.groupby("wallet").size().reindex(A.index).fillna(0)
    A.index.name = "wallet"
    tot = {"vol5": float(X[m5].usdc.sum()), "pnl5_M": float(X[m5 & (X.rol == "M")].pnl.sum()),
           "pnl5_T": float(X[m5 & (X.rol == "T")].pnl.sum()), "fee5": float(X[m5].fee.sum())}
    return A, tot


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-06")
    ap.add_argument("--hasta", default="2026-10-13")
    a = ap.parse_args()
    import json
    partes, tots = [], {}
    d, d1 = date.fromisoformat(a.desde), date.fromisoformat(a.hasta)
    while d <= d1:
        ca = OUT / f"quien_gana_agg_{d}.csv"
        if not ca.exists():
            c = OUT / f"quien_gana_fills_{d}.csv.gz"
            if c.exists():
                X = pd.read_csv(c, dtype={"wallet": "category", "mkt": str, "tx": str})
            else:
                X = fills_dia(d.isoformat())
                if X is None:
                    d += timedelta(days=1)
                    continue
                print(f"{d}: {len(X)} rellenos ({(X.marco == '5m').sum()} 5m), cobertura desenlace {X.cob.mean():.1%}", flush=True)
                X.to_csv(c, index=False, compression="gzip")
            A, tot = agregar(X)
            del X
            A.to_csv(ca)
            (OUT / f"quien_gana_tot_{d}.json").write_text(json.dumps(tot))
        A = pd.read_csv(ca, index_col=0)
        A["dia"] = d.isoformat()
        partes.append(A)
        tots[d.isoformat()] = json.loads((OUT / f"quien_gana_tot_{d}.json").read_text())
        d += timedelta(days=1)
    D = pd.concat(partes)
    n_dias = D.dia.nunique()
    D["pnl5"] = D.pnl5_M + D.pnl5_T
    W = D.drop(columns=["dia"]).groupby(level=0).sum()
    W["dias5"] = D[D.vol5 > 0].groupby(level=0).size().reindex(W.index).fillna(0).astype(int)
    W["dias_pos5"] = D[D.pnl5 > 0].groupby(level=0).size().reindex(W.index).fillna(0).astype(int)
    W["pct_T5"] = W.volT5 / W.vol5.replace(0, np.nan)
    W["ev5"] = W.pnl5 / W.vol5.replace(0, np.nan)
    W = W.sort_values("pnl5", ascending=False)
    W.to_csv(OUT / "quien_gana_wallets.csv")
    L = [f"Quién gana en los PARES 5m/15m ({a.desde}..{a.hasta}, {n_dias} días): {len(W)} wallets"]
    tv = sum(t["vol5"] for t in tots.values())
    L.append(f"5m pares: volumen {tv:,.0f} $ | PnL makers {sum(t['pnl5_M'] for t in tots.values()):+,.0f} $ | PnL tomadores "
             f"{sum(t['pnl5_T'] for t in tots.values()):+,.0f} $ (comisión pagada {sum(t['fee5'] for t in tots.values()):,.0f} $)")
    mind = max(3, n_dias // 2)
    per = W[(W.dias5 >= mind) & (W.vol5 >= 500)]
    gan = per[(per.pnl5 > 0) & (per.dias_pos5 >= 0.75 * per.dias5)]
    L.append(f"wallets con >= {mind} días y >= 500 $ en 5m pares: {len(per)}; GANADORAS PERSISTENTES (PnL>0 y >=75 % días +): "
             f"{len(gan)}, PnL 5m {gan.pnl5.sum():+,.0f} $ = {gan.pnl5.sum() / max(1, W[W.pnl5 > 0].pnl5.sum()):.0%} del PnL positivo; "
             f"de ellas makers (>50 % vol maker) {int((gan.pct_T5 < 0.5).sum())}, tomadoras {int((gan.pct_T5 >= 0.5).sum())}, "
             f"con cruce 5m-15m en >=25 % de sus cierres {int((gan.cierres_cruce >= 0.25 * gan.cierres5).sum())}")
    L.append("\nTOP 30 GANADORAS PERSISTENTES por PnL 5m pares (M=maker, T=tomador; %T vol tomador; cruce = cierres con 5m y 15m-últ5 / cierres 5m):")
    for w, r in gan.sort_values("pnl5", ascending=False).head(30).iterrows():
        L.append(f"  {w[:10]} PnL5 {r.pnl5:+8.0f} (M {r.pnl5_M:+7.0f} T {r.pnl5_T:+7.0f}) vol {r.vol5:9.0f} EV {r.ev5:+.3f} %T {r.pct_T5:4.0%} "
                 f"días+ {r.dias_pos5}/{r.dias5} merc {int(r.n_mkt5):4d} | 15m {r.pnl15:+7.0f} (últ5 {r.pnl15_ult5:+6.0f}) cruce {int(r.cierres_cruce)}/{int(r.cierres5)}")
    L.append("\nTOP 10 por PnL bruto (sin filtro de persistencia):")
    for w, r in W.head(10).iterrows():
        L.append(f"  {w[:10]} PnL5 {r.pnl5:+8.0f} (M {r.pnl5_M:+7.0f} T {r.pnl5_T:+7.0f}) vol {r.vol5:9.0f} %T {r.pct_T5:4.0%} días+ {r.dias_pos5}/{r.dias5}")
    L.append("\nPEOR 10:")
    for w, r in W.tail(10).iterrows():
        L.append(f"  {w[:10]} PnL5 {r.pnl5:+8.0f} (M {r.pnl5_M:+7.0f} T {r.pnl5_T:+7.0f}) vol {r.vol5:9.0f} %T {r.pct_T5:4.0%} días+ {r.dias_pos5}/{r.dias5}")
    txt = "\n".join(L)
    print(txt)
    (OUT / "quien_gana_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
