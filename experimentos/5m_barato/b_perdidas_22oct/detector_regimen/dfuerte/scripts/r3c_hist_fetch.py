#!/usr/bin/env python3
"""r3c - reconstruccion de mid de mercados 5m cerrados con CLOB prices-history (GET publico) para las ventanas-unidad. Uso: r3c <src:backfill|reciente> <dia_ini> <dia_fin> <n_max|0> -> /mnt/.../dfuerte/hist_<src>.jsonl (reanudable). PROXY declarado: puntos ~cada 60 s."""
import sys, json, time, os, datetime as dt, requests, pandas as pd
from concurrent.futures import ThreadPoolExecutor
src, d0, d1, nmax = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]); D = '/mnt/HC_Volume_106538179/agentes_datos/dfuerte'
U = pd.read_pickle(f'/root/polymarket-research-datalogs/regimen_5m/dfuerte/units_{src}.pkl'); U = U[(U['T'] == 180) & U.coin.isin(['BTC','ETH','SOL','XRP'])]
e = lambda s: (dt.date.fromisoformat(s) - dt.date(1970, 1, 1)).days
U = U[(U.dia >= e(d0)) & (U.dia <= e(d1))][['coin', 'tmin']].drop_duplicates()
if nmax: U = U.sample(nmax, random_state=1)
out = f'{D}/hist_{src}.jsonl'; done = set()
if os.path.exists(out): done = {(j['coin'], j['tmin']) for j in map(json.loads, open(out))}
todo = [(c, t) for c, t in zip(U.coin, U.tmin) if (c, t) not in done]; print('pendientes', len(todo), flush=True)
ses = requests.Session()
def one(ct):
    c, t = ct; ep = t * 60; time.sleep(0.12)
    for k in range(3):
        try:
            g = ses.get('https://gamma-api.polymarket.com/markets', params=dict(slug=f'{c.lower()}-updown-5m-{ep}', closed='true'), timeout=15).json()
            if not g: return dict(coin=c, tmin=int(t), err='nogamma')
            tk = json.loads(g[0]['clobTokenIds']); oc = json.loads(g[0]['outcomes'])
            h = ses.get('https://clob.polymarket.com/prices-history', params=dict(market=tk[oc.index('Up')], startTs=ep - 180, endTs=ep + 330, fidelity=1), timeout=15).json()
            return dict(coin=c, tmin=int(t), pts=[(x['t'], x['p']) for x in h.get('history', [])])
        except Exception as ex: time.sleep(1.5)
    return dict(coin=c, tmin=int(t), err='fallo')
with ThreadPoolExecutor(4) as ex, open(out, 'a') as f:
    for i, r in enumerate(ex.map(one, todo)):
        f.write(json.dumps(r) + '\n')
        if i % 500 == 0: f.flush(); print(i, flush=True)
print('FIN', flush=True)
