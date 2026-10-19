#!/usr/bin/env python3
"""a3_ledger.py w1,w2,.. [dias..] -- ledger por wallet en mercados 5m (on-chain, m5_onchain via fills_D.parquet): TODAS las bandas de precio y T,
como TOMADOR (filas resumen is_tk=1: maker==wallet) y como MAKER (filas is_tk=0: maker==wallet). PnL a resolucion con desenlace oficial:
compra de token: sh*(v-p)-fee ; venta: sh*(p-v) (v=1 si el token gana). Limite: solo mercados 5m de las 6 monedas; cualquier cobertura en 15m/4h/otra
wallet NO se ve (PnL visible != PnL total). Maker sin rebate (20 % del fee del tomador, no incluido). Salida: ledger_<wallet8>.csv.gz + resumen impreso."""
import sys
import numpy as np, pandas as pd
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from lib import *
ws = [w.lower() for w in sys.argv[1].split(",")]
dias = sys.argv[2:] or ["2026-10-%02d" % i for i in range(9, 19)]
rows = []
for d in dias:
    F = pd.read_parquet(CACHE + f"fills_{d}.parquet")
    F = F[(F.maker.isin(ws))]                         # maker==wallet: (is_tk=0) rellenos como maker; (is_tk=1) ordenes como tomador
    if not len(F): continue
    buy = F.side.values == 0
    sh = np.where(buy, F.taker_amt.values, F.maker_amt.values); usd = np.where(buy, F.maker_amt.values, F.taker_amt.values)
    des = F.mkt.astype(str).map(DES)
    v = np.where(F.lado.values == des.values, 1.0, 0.0); v[des.isna().values] = np.nan
    p = usd / sh
    pnl = np.where(buy, sh * (v - p), sh * (p - v)) - np.where(F.is_tk.values == 1, F.fee.values, 0.0)
    expo_p = np.where(buy, p, 1 - p)                   # precio de la exposicion que adquiere (comprar token a p / vender token a p = comprar complemento a 1-p)
    expo_lado = np.where(buy, F.lado.values, np.where(F.lado.values == "YES", "NO", "YES"))
    rows.append(pd.DataFrame({"dia": d, "wallet": F.maker.values, "rol": np.where(F.is_tk.values == 1, "TOMADOR", "MAKER"), "act": F.act.values, "mkt": F.mkt.values,
                              "fin": F.fin.values, "ts": F.ts.values, "T": F.fin.values - F.ts.values, "tx": F.tx.values, "tok_lado": F.lado.values, "compra": buy,
                              "sh": sh, "usd": usd, "p": p, "expo_p": expo_p, "expo_lado": expo_lado, "fee": np.where(F.is_tk.values == 1, F.fee.values, 0.0),
                              "des": des.values, "pnl": pnl}))
L = pd.concat(rows, ignore_index=True)
for w in ws:
    Lw = L[L.wallet == w]
    Lw.to_csv(f"/root/polymarket-research/experimentos/5m_barato/wallets_18oct/ledger_{w[:10]}.csv.gz", index=False, compression="gzip")
    print(f"\n=== {w}  filas {len(Lw)} | cobertura desenlace {Lw.des.notna().mean():.3f}")
    Lw = Lw[Lw.des.notna()]
    g = Lw.groupby(["rol"]).agg(n=("sh", "size"), vol=("usd", "sum"), pnl=("pnl", "sum"), fee=("fee", "sum"), mkts=("mkt", "nunique"))
    print(g.round(1).to_string())
    print(Lw.groupby(["dia", "rol"]).agg(n=("sh", "size"), vol=("usd", "sum"), pnl=("pnl", "sum")).round(1).unstack().to_string())
    print(Lw.groupby(["act", "rol"]).agg(vol=("usd", "sum"), pnl=("pnl", "sum")).round(1).unstack().to_string())
    Lw = Lw.assign(banda=pd.cut(Lw.expo_p, [0, .1, .3, .5, .7, .9, .97, 1.0]), tb=pd.cut(Lw["T"], [-1e9, 0, 20, 45, 60, 120, 300, 1e9]))
    print(Lw.groupby(["rol", "banda"], observed=True).agg(n=("sh", "size"), vol=("usd", "sum"), pnl=("pnl", "sum")).round(1).to_string())
    print(Lw.groupby(["rol", "tb"], observed=True).agg(n=("sh", "size"), vol=("usd", "sum"), pnl=("pnl", "sum")).round(1).to_string())
