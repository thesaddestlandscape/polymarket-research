#!/usr/bin/env python3
"""b1_tomadores_scan.py (ident_17nov, Tarea B) -- SOLO LECTURA, 0 ordenes. Perfil ON-CHAIN de las wallets tomadoras de los rellenos de B (fn_16nov/tomadores.pkl,
202 rellenos, 67 wallets) en TODO el 5m (m5_onchain_D.csv.gz del volumen, contrato 0xe1111800...; ts_est = BLOQUE, ~2,4 s tras el casado).
Lectura troceada (chunks 400k, columnas necesarias), filtro: tipo F y (taker en W | maker en W | order_hash en hashes tomadores).
Salidas: b1_rows.pkl (filas filtradas), b1_ordenes.pkl (una fila por ORDEN TOMADORA = fila resumen taker==exchange con maker=wallet:
patas del tx con taker=wallet; precio equivalente en el token de la orden; niveles, mejor/peor, profundidad del barrido; resto en reposo =
el mismo order_hash aparece despues como MAKER = limite revelado). Uso: python3 -I b1_tomadores_scan.py D1 D2 ..."""
import os, sys, glob, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
EX = '0xe111180000d2663c0091e4f400237545b87b996b'; OWN = '0x659a40ff9920febc5a66836213040924343d297f'
TK = pd.read_pickle(H + '../fn_16nov/tomadores.pkl')
W = set(TK.tk_addr.dropna().str.lower()); HS = set(TK.tk_hash.dropna().str.lower())
COLS = ['tipo', 'bloque', 'ts_est', 'tx', 'log_index', 'order_hash', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt']
dias = sys.argv[1:]
parts = []
for d in dias:
    f = f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz'
    if not os.path.exists(f): print('falta', f, flush=True); continue
    n = 0
    for c in pd.read_csv(f, usecols=COLS, dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str, 'order_hash': str, 'tipo': str}, chunksize=400000):
        c = c[c.tipo == 'F']; mk = c.maker.str.lower(); tk = c.taker.str.lower(); oh = c.order_hash.str.lower()
        sel = tk.isin(W) | mk.isin(W) | oh.isin(HS)
        x = c[sel].copy(); x['maker'] = mk[sel]; x['taker'] = tk[sel]; x['order_hash'] = oh[sel]; x['dia'] = d; parts.append(x.drop(columns=['tipo'])); n += len(x)
    print(d, 'filas', n, flush=True)
R = pd.concat(parts, ignore_index=True).drop_duplicates(['tx', 'log_index'])
R.to_pickle(H + 'b1_rows.pkl')
# ---- ordenes tomadoras de las wallets W
S = R[(R.taker == EX) & R.maker.isin(W)].rename(columns={'maker': 'wallet', 'order_hash': 'tk_hash', 'token_id': 'tokX', 'side': 'sX', 'maker_amt': 'amtA', 'taker_amt': 'amtB'})
L_ = R[R.taker.isin(W) & (R.taker != EX)].copy()
L_['p'] = np.where(L_.side == 0, L_.maker_amt / L_.taker_amt, L_.taker_amt / L_.maker_amt); L_['sh'] = np.where(L_.side == 0, L_.taker_amt, L_.maker_amt)
MK = R[R.maker.isin(W) & (R.taker != EX)]                       # actividad como MAKER (reposo)
mk_hash = MK.groupby('order_hash').agg(rest_n=('tx', 'nunique'), rest_ts=('ts_est', 'min'))
S2 = S[['tx', 'wallet', 'tk_hash', 'tokX', 'sX', 'amtA', 'amtB', 'ts_est', 'bloque', 'dia']].drop_duplicates(['tx', 'wallet'])
J = L_.merge(S2, left_on=['tx', 'taker'], right_on=['tx', 'wallet'], how='inner', suffixes=('', '_s'))
J['eq'] = np.where(J.token_id == J.tokX, J.p, 1 - J.p); J['eq3'] = J.eq.round(3); J['mint'] = J.token_id != J.tokX; J['conB'] = J.maker == OWN
J = J.sort_values(['tx', 'wallet', 'log_index'])
g = J.groupby(['tx', 'wallet'], sort=False)
OD = g.agg(dia=('dia_s', 'first'), tk_hash=('tk_hash', 'first'), tokX=('tokX', 'first'), sX=('sX', 'first'), amtA=('amtA', 'first'), amtB=('amtB', 'first'),
           ts=('ts_est_s', 'first'), bloque=('bloque_s', 'first'), n_patas=('eq', 'size'), n_niveles=('eq3', 'nunique'), eq_max=('eq', 'max'), eq_min=('eq', 'min'),
           mint=('mint', 'any'), con_B=('conB', 'any'), tok_m0=('token_id', 'first'), side_m0=('side', 'first'), p_m0=('p', 'first'), sh_m0=('sh', 'first')).reset_index()
OD['vende'] = OD.sX == 1
OD['mejor'] = np.where(OD.vende, OD.eq_max, OD.eq_min); OD['peor'] = np.where(OD.vende, OD.eq_min, OD.eq_max)
OD['prof_c'] = ((OD.eq_max - OD.eq_min) * 100).round(2); OD['sh'] = np.where(OD.vende, OD.amtA, OD.amtB)

OD = OD.merge(mk_hash, left_on='tk_hash', right_index=True, how='left'); OD['resto_reposo'] = OD.rest_n.fillna(0) > 0
OD.to_pickle(H + 'b1_ordenes.pkl')
print('ordenes tomadoras', len(OD), 'wallets', OD.wallet.nunique(), 'dias', OD.dia.nunique(), flush=True)
