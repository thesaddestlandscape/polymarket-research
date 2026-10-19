#!/usr/bin/env python3
"""(3) Perfil on-chain 5m de las wallets que se llevan el ask V4 (09-18 Oct). Lee la caché de fills del agente de wallets
(fills_D.parquet, derivada de m5_onchain; solo lectura) y desenlaces oficiales (maker_ms_desenlaces_cache.json).
Unidad: (wallet, mercado, lado) para EV; también fills. PnL de compra tomadora = acc*(1{gana}) - coste - fee."""
import pandas as pd, json, numpy as np, sys, collections
C = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
des = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
W = ['0x9783f45ce35f794be38ca47dd0816a5c241383b9', '0xe38cc08b122dc5fdf21ebd936059cb47f30def5b',
     '0xdec35f1d2eece908432f505094f12d34b69e9a52', '0x27e99389f6fd80cbc414f39a33e58425b3fac5b7']
rows = []
for d in [f'2026-10-{x:02d}' for x in range(9, 19)]:
    f = pd.read_parquet(C + f'fills_{d}.parquet', columns=['tx', 'is_tk', 'maker', 'taker', 'side', 'act', 'mkt', 'lado', 'fin', 'ts', 'maker_amt', 'taker_amt', 'fee'])
    tk = f[(f.is_tk == 1) & f.maker.isin(W)].copy(); tk['rol'] = 'TOMADOR'; tk['w'] = tk.maker
    mk = f[(f.is_tk == 0) & f.maker.isin(W)].copy(); mk['rol'] = 'MAKER'; mk['w'] = mk.maker
    for x in (tk, mk):
        x['dia'] = d; rows.append(x)
    del f
R = pd.concat(rows)
R['buy'] = R.side == 0
R['acc'] = np.where(R.buy, R.taker_amt, R.maker_amt); R['usd'] = np.where(R.buy, R.maker_amt, R.taker_amt)
R['p'] = R.usd / R.acc
R['T'] = R.fin - (R.ts - 2.4)
R['out'] = R.mkt.astype(str).map(des)
R['gana'] = np.where(R.out.isna(), np.nan, (R.out == R.lado).astype(float))
print('filas', len(R), '| cobertura desenlace', round(R.out.notna().mean(), 4))
for w in W:
    x = R[R.w == w]
    print(f'\n##### {w}  filas {len(x)}  días {x.dia.nunique()}')
    print(' rol x side:', dict(collections.Counter(zip(x.rol, x.buy))))
    print(' monedas:', dict(x.act.value_counts()))
    t = x[(x.rol == 'TOMADOR') & x.buy & x.out.notna()]
    if len(t):
        t = t.assign(pnl=t.acc * t.gana - t.usd - t.fee)
        u = t.groupby(['mkt', 'lado']).agg(pnl=('pnl', 'sum'), coste=('usd', 'sum'), gana=('gana', 'first'), p=('p', 'mean'), dia=('dia', 'first'), T=('T', 'median'), n=('p', 'size'))
        print(f' COMPRAS TOMADORAS: fills {len(t)} unidades {len(u)} coste {u.coste.sum():.0f} $ PnL {u.pnl.sum():+.1f} $ EV/€ ponderado {u.pnl.sum()/u.coste.sum():+.3f} | acierto unidades {u.gana.mean():.3f} precio medio {u.p.mean():.3f}')
        dd = u.groupby('dia').apply(lambda g: g.pnl.sum() / g.coste.sum())
        print('   EV ponderado por día:', dd.round(3).to_dict())
        print('   T restante (s) en el fill P10/50/90:', np.percentile(t['T'], [10, 50, 90]).round(1), '| precio P10/50/90:', np.percentile(t.p, [10, 50, 90]).round(3))
        print('   fills/unidad P50/P90:', np.percentile(u.n, [50, 90]), '| coste por unidad P50/P90 $:', np.percentile(u.coste, [50, 90]).round(1))
        print('   por banda de precio (unidades, EV pond.):', {b: (len(g), round(g.pnl.sum() / g.coste.sum(), 3)) for b, g in u.groupby(pd.cut(u.p, [0, .2, .4, .6, .8, 1.0]), observed=True)})
        print('   por moneda:', {a: (len(g), round(g.pnl.sum() / g.coste.sum(), 3)) for a, g in t.assign(coste=t.usd).groupby('act')})
    s = x[(x.rol == 'TOMADOR') & ~x.buy]
    print(' ventas tomadoras:', len(s), '| fills maker:', int((x.rol == 'MAKER').sum()))
R.to_pickle('/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/competidores_fills.pkl')
