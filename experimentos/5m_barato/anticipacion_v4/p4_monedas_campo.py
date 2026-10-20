#!/usr/bin/env python3
"""Paso 4 (ventajas competitivas): ¿existe el sesgo del 5m anidado en otras monedas y lo explota alguien? Nivel CAMPO (todas las tomadoras), on-chain.
Unidad = (wallet, mercado, lado) de compras TOMADORAS en 5m que cierran en multiplo de 900 (anidados), 09-18 Oct, 6 monedas, desenlace oficial (cache DES).
s = lado implicado por TWAP60 oficial (ref15=twap60@C-900, ref5=twap60@C-300; ref15>ref5 => Up/YES). EV = sum(pnl)/sum(coste) ponderado por EUR (pnl = shares*win - usd - fee).
Compara lado s vs lado opuesto, por moneda y banda de precio medio de la unidad; rivales R1-R3 aparte del resto; IC90 bootstrap por cierre; sin 2 mejores dias."""
import glob, json, numpy as np, pandas as pd
W = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
RIV = {'0x9783f45ce35f794be38ca47dd0816a5c241383b9', '0xe38cc08b122dc5fdf21ebd936059cb47f30def5b', '0x27e99389f6fd80cbc414f39a33e58425b3fac5b7'}
def refs(D):
    d = pd.concat([pd.read_csv(f, usecols=['asset', 'canal', 'value', 'event_ts_ms', 'source']) for f in glob.glob(f'/root/polymarket-research/data/prices/polybolt_{D}.csv*')])
    d = d[(d.canal == 'twap60') & (d.source == 'chainlink')].drop_duplicates(['asset', 'event_ts_ms'])
    return {(a, t // 1000): v for a, t, v in zip(d.asset, d.event_ts_ms, d.value)}
days = [f[-18:-8] for f in sorted(glob.glob(W + 'fills_2026-10-*.parquet'))]; days = [d for d in days if '2026-10-09' <= d <= '2026-10-18']
U = []
for D in days:
    ref = {}
    for dd in (pd.Timestamp(D) - pd.Timedelta(days=1), pd.Timestamp(D), pd.Timestamp(D) + pd.Timedelta(days=1)):
        try: ref.update(refs(dd.strftime('%Y-%m-%d')))
        except Exception: pass
    f = pd.read_parquet(W + f'fills_{D}.parquet', columns=['is_tk', 'maker', 'side', 'act', 'mkt', 'lado', 'fin', 'maker_amt', 'taker_amt', 'fee'])
    f = f[(f.is_tk == 1) & (f.side == 0) & (f.fin % 900 == 0)].copy()
    f['k5'] = [ref.get((a, c - 300), np.nan) for a, c in zip(f.act, f.fin)]; f['k15'] = [ref.get((a, c - 900), np.nan) for a, c in zip(f.act, f.fin)]
    f = f.dropna(subset=['k5', 'k15']); f['sUp'] = f.k15 > f.k5
    f['es_s'] = (f.lado == 'YES') == f.sUp
    f['gap_bp'] = (f.k5 / f.k15 - 1).abs() * 1e4
    u = f.groupby(['maker', 'mkt', 'lado', 'act', 'fin', 'es_s']).agg(usd=('maker_amt', 'sum'), sh=('taker_amt', 'sum'), fee=('fee', 'sum'), gap=('gap_bp', 'first')).reset_index()
    u['dia'] = D; U.append(u)
    print(D, len(f), len(u), flush=True)
U = pd.concat(U); U['gana'] = [None if str(m) not in DES else DES[str(m)] == l for m, l in zip(U.mkt, U.lado)]
print('cobertura desenlace por moneda:', U.groupby('act').gana.apply(lambda s: round(s.notna().mean(), 3)).to_dict())
U = U.dropna(subset=['gana']); U['gana'] = U.gana.astype(float)
U['pnl'] = U.sh * U.gana - U.usd - U.fee; U['coste'] = U.usd + U.fee; U['p'] = U.usd / U.sh
U['riv'] = U.maker.isin(RIV); U['banda'] = pd.cut(U.p, [0, .15, .3, .5, .7, 1.01])
rng = np.random.default_rng(5)
def ev(x): return x.pnl.sum() / x.coste.sum() if x.coste.sum() > 0 else np.nan
def ic(x):
    g = x.groupby('fin')[['pnl', 'coste']].sum().values
    if len(g) < 5: return (np.nan, np.nan)
    ix = rng.integers(0, len(g), (1500, len(g))); r = g[ix, 0].sum(1) / np.maximum(g[ix, 1].sum(1), 1e-9)
    return tuple(np.percentile(r, [5, 95]).round(2))
def s2(x):
    by = x.groupby('dia')[['pnl', 'coste']].sum(); top = by.pnl.sort_values(ascending=False).index[:2]; y = x[~x.dia.isin(top)]
    return ev(y), int((by.pnl > 0).sum()), len(by)
out = open('p4_out.txt', 'w')
def P(*a): print(*a); print(*a, file=out)
U.to_pickle(W.replace('wallets_18oct/', 'v4_comprar_lo_bueno/') + 'p4_unidades.pkl')
P('unidades', len(U), 'rivales', int(U.riv.sum()))
P('\nCAMPO sin rivales, compras tomadoras, 5m anidado: EV por moneda x (s / opuesto), unidades con coste; (n, coste $, EV, IC90 cierre, EV sin 2 mejores dias, dias+)')
for a in ['BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB']:
    for nm, riv in (('campo', False), ('RIVALES', True)):
        for es in (True, False):
            x = U[(U.act == a) & (U.riv == riv) & (U.es_s == es)]
            if len(x) < 5: continue
            e2, dp, nd = s2(x)
            P(f'{a:5s} {nm:8s} {"lado s " if es else "opuesto"} n={len(x):6d} coste={x.coste.sum():10.0f} EV={ev(x):+.3f} IC90={ic(x)} sin2mejores={e2:+.3f} dias+={dp}/{nd}')
P('\nCAMPO sin rivales, lado s, por banda de precio de la unidad (todas las monedas / BTC / altcoins)')
for nm, sel in (('BTC', U.act == 'BTC'), ('ALTS', U.act != 'BTC')):
    for b, x in U[sel & ~U.riv & U.es_s].groupby('banda', observed=True):
        xo = U[sel & ~U.riv & ~U.es_s & (U.banda == b)]
        P(f'{nm:5s} {str(b):14s} lado s n={len(x):5d} coste={x.coste.sum():9.0f} EV={ev(x):+.3f} {ic(x)} | opuesto n={len(xo):5d} EV={ev(xo):+.3f}')
P('\nPersistencia por gap |ref5/ref15-1| (lado s, campo, ALTS+BTC, p<0.5):')
for a in ['BTC', 'ALTS']:
    sel = (U.act == 'BTC') if a == 'BTC' else (U.act != 'BTC')
    x = U[sel & ~U.riv & U.es_s & (U.p < .5)].copy(); x['gb'] = pd.cut(x.gap, [0, 1, 2, 4, 8, 1e9])
    for b, y in x.groupby('gb', observed=True): P(f'  {a:5s} gap {str(b):12s} n={len(y):5d} coste={y.coste.sum():8.0f} EV={ev(y):+.3f}')
out.close()
