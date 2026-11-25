#!/usr/bin/env python3
"""prep_day2.py DIA -- como prep_day.py (dev) pero NO descarta horas: conserva TODOS los fills side0 5m (src tx_ws|bloque), t_ws_ms=recepcion libro5_tx o bloque-2,25 s;
ademas escribe huecos de libro5_tx (gaps de recepcion >60 s) y cobertura por hora. Solo lectura de datalogs; escribe en out/."""
import sys, os, glob, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'; sys.path.insert(0, H); import rr as RR
DL = '/root/polymarket-research-datalogs/'; TXD = '/mnt/HC_Volume_106538179/libro5_tx/'; d = sys.argv[1]
z = np.load(DL + f'sa_ms/ms_{d}.npz', allow_pickle=True); tok5 = set(t for t, r in zip(z['tokens'], z['tmap']) if r[1] == '5min'); del z
ch = []
for f in sorted(glob.glob(DL + f'keep_onchain_re_as_b/onchain_fills_{d}*.csv.gz')):
    for c in pd.read_csv(f, usecols=['tipo', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'], dtype={'token_id': str, 'maker': str, 'taker': str, 'tx': str}, chunksize=400000):
        ch.append(c[c.token_id.isin(tok5)])
fills = RR.fills_makers(pd.concat(ch)); del ch
dd = pd.Timestamp(d); fr = []
for dday in [(dd + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in (-1, 0, 1)]:
    for f in sorted(glob.glob(TXD + f'libro5_tx_{dday}_*.csv.gz')):
        try: fr.append(pd.read_csv(f, header=None, names=['t_ev', 'token', 'tx', 'recv'], dtype={'token': str, 'tx': str}, on_bad_lines='skip'))
        except Exception as e: print('err', f, e)
tws, _ = RR.tx_ws(fr, con_tokens=False)
d0 = int(dd.timestamp() * 1000); rx = np.unique(pd.concat(fr).recv.values); rx = rx[(rx >= d0 - 3600000) & (rx < d0 + 86400000 + 3600000)]; del fr
e = np.concatenate([[d0], rx[(rx >= d0) & (rx < d0 + 86400000)], [d0 + 86400000]]); g = np.diff(e); ix = np.where(g > 60000)[0]; holes = [(int(e[i]), int(e[i + 1])) for i in ix]
chain = RR.reconstruir(fills, tws); del fills
cob = RR.cobertura_hora(chain); ok = RR.horas_sanas(chain, 0.95)
bad = sorted([d, h] for h in range(24) if (d, h) not in ok)
sl = chain[chain.side.values == 0][['token_id', 'price', 'sh', 'side', 't_ws_ms', 'src', 'tx', 'log_index', 'maker', 'ts_est']].copy()
sl.to_pickle(OUT + f'tape2_{d}.pkl')
json.dump(dict(holes=holes, bad_hours=bad, fills=int(len(chain)), cob_tx_ws=float((chain.src == 'tx_ws').mean()), side0=int(len(sl)), side0_bloque=int((sl.src == 'bloque').sum())), open(OUT + f'meta2_{d}.json', 'w'))
print('ok', d, len(sl), 'bloque', int((sl.src == 'bloque').sum()), 'holes', len(holes), 'horas malas', [h for _, h in bad])
