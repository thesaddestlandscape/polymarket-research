#!/usr/bin/env python3
# COPIA de precursores_barrido/prep_day.py (no se edita el original): rutas absolutas y fallback de on-chain a m5_onchain/ si no hay keep_onchain_re_as_b (dias <26-Oct).
"""Prep de cinta on-chain por dia (solo lectura de datalogs; DEV; 0 ordenes). Igual que escalera_B/run_day.prep_tape+prep_slim pero conserva 'maker'.
Uso: python3 -I prep_day.py DIA  -> out/tape_<D>.pkl (fills maker side 0 en horas sanas, 5m), out/bad_<D>.json"""
import sys, os, glob, json, numpy as np, pandas as pd
H = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/'; OUT = H + 'out/'
sys.path.insert(0, '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/captura_prints'); import reconstructor_relleno as RR
DL = '/root/polymarket-research-datalogs/'; TXD = '/mnt/HC_Volume_106538179/libro5_tx/'
d = sys.argv[1]
if os.path.exists(OUT + f'tape_{d}.pkl') and os.path.exists(OUT + f'bad_{d}.json'): print('ya hecho', d); sys.exit(0)
z = np.load(DL + f'sa_ms/ms_{d}.npz', allow_pickle=True); tok5 = set(t for t, r in zip(z['tokens'], z['tmap']) if r[1] == '5min'); del z
ch = []
for f in sorted((glob.glob(DL + f'keep_onchain_re_as_b/onchain_fills_{d}*.csv.gz') or glob.glob(f'/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_{d}.csv.gz'))):
    for c in pd.read_csv(f, usecols=['tipo', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'], dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str}, chunksize=400000):
        ch.append(c[c.token_id.isin(tok5)])
fills = RR.fills_makers(pd.concat(ch)); del ch
dd = pd.Timestamp(d); fr = []
for dday in [(dd + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in (-1, 0, 1)]:
    for f in sorted(glob.glob(TXD + f'libro5_tx_{dday}_*.csv.gz')):
        fr.append(pd.read_csv(f, header=None, names=['t_ev', 'token', 'tx', 'recv'], dtype={'token': str, 'tx': str}))
tws, _ = RR.tx_ws(fr, con_tokens=False); del fr
chain = RR.reconstruir(fills, tws); del fills
ok = RR.horas_sanas(chain, 0.95)
t = pd.to_datetime(chain.ts_est, unit='s', utc=True)
keep = np.array([(a, b) in ok for a, b in zip(t.dt.strftime('%Y-%m-%d'), t.dt.hour)])
bad = sorted([d, h] for h in range(24) if (d, h) not in ok)
sl = chain[keep & (chain.side.values == 0)][['token_id', 'price', 'sh', 'side', 't_ws_ms', 'src', 'tx', 'log_index', 'maker', 'ts_est']].copy()
sl.to_pickle(OUT + f'tape_{d}.pkl.tmp'); os.replace(OUT + f'tape_{d}.pkl.tmp', OUT + f'tape_{d}.pkl')
json.dump(dict(bad=bad, fills=int(len(chain)), cob_tx_ws=float((chain.src == 'tx_ws').mean()), side0_sanas=int(len(sl))), open(OUT + f'bad_{d}.json', 'w'))
print('ok', d, len(sl), 'horas malas', [h for _, h in bad])
