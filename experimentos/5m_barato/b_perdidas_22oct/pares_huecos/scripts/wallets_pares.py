#!/usr/bin/env python3
"""wallets_pares.py -- Parte B del PREREG: ledger wallet-mercado en ETH/SOL/XRP 5m (on-chain cola_vs_cruce/datos/oc_D, 17-22 Oct).
Salida ../datos/wm_ledger.csv.gz (una fila por wallet-mercado) y ../datos/wallets_pares.txt"""
import os, glob, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); SRC = os.path.join(AQ, '..', '..', 'cola_vs_cruce', 'datos'); OUT = os.path.join(AQ, '..', 'datos')
EXCH = '0xe111180000d2663c0091e4f400237545b87b996b'
rows = []
for d in ['2026-10-%02d' % i for i in range(17, 23)]:
    oc = pd.read_csv(os.path.join(SRC, f'oc_{d}.csv.gz')); tk = pd.read_csv(os.path.join(SRC, f'tok_{d}.csv'))
    oc = oc.merge(tk[['tok_i', 'act', 'mid', 'fin', 'lado', 'des']], on='tok_i', how='left')
    oc['rol'] = np.where(oc.taker == EXCH, 'T', 'M')
    buy = oc.side == 0
    oc['acc'] = np.where(buy, oc.ta, oc.ma); oc['usd'] = np.where(buy, oc.ma, oc.ta)
    oc['px'] = oc.usd / oc.acc
    # venta de X a s == compra del contrario a 1-s
    oc['lado_ef'] = np.where(buy, oc.lado, np.where(oc.lado == 'YES', 'NO', 'YES'))
    oc['cost_ef'] = np.where(buy, oc.usd, oc.acc - oc.usd)
    oc['fee_usd'] = np.where(oc.rol == 'T', oc.fee, 0.0)
    oc['dia'] = d
    rows.append(oc[['bloque', 'ts', 'tx', 'li', 'maker', 'rol', 'side', 'act', 'mid', 'fin', 'lado', 'des', 'acc', 'px', 'lado_ef', 'cost_ef', 'fee_usd', 'dia']])
F = pd.concat(rows, ignore_index=True); F = F.rename(columns={'maker': 'wallet'})
F = F[F.des.notna()]
if not os.path.exists(os.path.join(OUT, 'fills_alts.csv.gz')): F.to_csv(os.path.join(OUT, 'fills_alts.csv.gz'), index=False, compression='gzip')
F['mk_usd'] = np.where(F.rol == 'M', F.cost_ef, 0.0)
g = F.groupby(['wallet', 'mid', 'lado_ef'])
agg = g.agg(Q=('acc', 'sum'), C=('cost_ef', 'sum'), fee=('fee_usd', 'sum'), nfill=('acc', 'size'),
            maker_usd=('mk_usd', 'sum'), act=('act', 'first'), fin=('fin', 'first'), des=('des', 'first')).reset_index()
W = agg.pivot_table(index=['wallet', 'mid', 'act', 'fin', 'des'], columns='lado_ef', values=['Q', 'C', 'fee', 'nfill', 'maker_usd'], fill_value=0)
W.columns = [f'{a}_{b}' for a, b in W.columns]; W = W.reset_index()
for c in ('Q', 'C', 'fee', 'nfill', 'maker_usd'):
    for l in ('YES', 'NO'):
        if f'{c}_{l}' not in W: W[f'{c}_{l}'] = 0.0
W['vol'] = W.C_YES + W.C_NO; W['fee'] = W.fee_YES + W.fee_NO; W['maker_pct'] = (W.maker_usd_YES + W.maker_usd_NO) / W.vol
W['pago'] = np.where(W.des == 'YES', W.Q_YES, W.Q_NO)
W['pnl'] = W.pago - W.vol - W.fee
W['Qp'] = np.minimum(W.Q_YES, W.Q_NO)
py = np.where(W.Q_YES > 0, W.C_YES / W.Q_YES.where(W.Q_YES > 0, 1), 0); pn = np.where(W.Q_NO > 0, W.C_NO / W.Q_NO.where(W.Q_NO > 0, 1), 0)
W['par_coste'] = np.where(W.Qp > 0, py + pn, np.nan)
W['pnl_par'] = W.Qp * (1 - np.nan_to_num(W.par_coste))
W['pnl_res'] = W.pnl + W.fee - W.pnl_par            # residuo (sin comision); comision aparte
W['ambos'] = (W.Q_YES >= 5) & (W.Q_NO >= 5)
W['res_frac'] = np.abs(W.Q_YES - W.Q_NO) / (W.Q_YES + W.Q_NO)
W['dia'] = pd.to_datetime(W.fin.astype(int) - 1, unit='s').dt.strftime('%Y-%m-%d')
W.to_csv(os.path.join(OUT, 'wm_ledger.csv.gz'), index=False, compression='gzip')
print('wallet-mercado', len(W), 'wallets', W.wallet.nunique(), 'fills', len(F))
