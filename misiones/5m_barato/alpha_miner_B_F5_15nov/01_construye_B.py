#!/usr/bin/env python3
"""Paso 1: F5 (y rezagos) de cada fill real de B (e02real_fills, 20-23 Oct) con la MISMA definicion que forward_a1.estado()/rasgos(), calculado desde q_D.gz (poblacion derivacion);
y dataset de ordenes de B (ledger real, puja_post.libro = F5 en la decision). Escribe B_fills.pkl y B_ordenes.pkl en esta carpeta. Solo lectura de insumos.
Uso: nice -n 19 ionice -c3 python3 -I 01_construye_B.py"""
import json, os, sys, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__))
RE = '/root/polymarket-research/misiones/5m_barato/docs/reverse-engineering/casos/RE-AS-B/'
DL = '/root/polymarket-research-datalogs/mitigar_as_25oct/'
LED = '/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'
SH = np.int64(1) << np.int64(41)
C0, C1 = json.load(open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mitigar_as_25oct/forward/regla_congelada.json'))['cortes_F5_terciles_train']
LAGS = (100, 250, 1000, 2000, 5000)
fills = pd.DataFrame(json.load(open(RE + 'e02real_fills.json')))
cruce = json.load(open(RE + 'e02real_cruce.json'))
fills['t_fill'] = [(c.get('TOBp') or {}).get('t_fill') for c in cruce]
fills['t_fill_src'] = np.where(fills.t_fill.notna(), 'libro5_T', 'ts_est-2400')
fills['t_fill'] = fills.t_fill.fillna(fills.ts_est * 1000 - 2400).astype('int64')
fills['dia'] = fills.fecha.str[:10]
fills['coin'] = fills.mercado.str.split('-').str[0].str.upper()
fills['cierre'] = fills.mercado.str.rsplit('-', n=1).str[1].astype('int64') + 300
fills['mkt_lado'] = fills.mercado + '|' + fills.outcome
tk = pd.read_csv(DL + 'tokens.csv', header=None, names=['token', 'tid', 'coin', 'mid', 'cierre', 'lado'], dtype={'token': str})
fills = fills.merge(tk[['token', 'tid', 'mid', 'lado']], left_on='tok_x', right_on='token', how='left').drop(columns='token')
assert fills.tid.notna().all(); fills['tid'] = fills.tid.astype('int64')

def leeq(path, keep):
    out = []
    for ch in pd.read_csv(path, header=None, names=['id', 'r', 'b', 'a', 'tb', 'ta'], chunksize=2_000_000, compression='gzip',
                          dtype={'id': np.int64, 'r': np.int64, 'b': np.float32, 'a': np.float32, 'tb': np.float32, 'ta': np.float32}, on_bad_lines='skip'):
        out.append(ch[ch.id.isin(keep)].dropna())
    return pd.concat(out, ignore_index=True)
def estado(K, R, ids, t):                      # copia literal de forward_a1.estado
    k = ids * SH + t; i = np.searchsorted(K, k, 'right') - 1; ok = (i >= 0); i = np.maximum(i, 0)
    ok &= ((K[i] // SH) == ids) & ((t - R[i]) <= 30000)
    return i, ok
res = []
for d, g in fills.groupby('dia'):
    Q = leeq(DL + f'q_{d}.gz', set(g.tid.unique()))
    K = Q.id.values.astype(np.int64) * SH + Q.r.values; o = np.lexsort((Q.ta.values, Q.tb.values, Q.a.values, Q.b.values, K))
    K = K[o]; R = Q.r.values[o]; B = Q.b.values[o]; A = Q.a.values[o]; TB = Q.tb.values[o]; TA = Q.ta.values[o]
    ids = g.tid.values.astype(np.int64); out = pd.DataFrame(index=g.index)
    for L in LAGS:
        tau = g.t_fill.values - L
        i1, ok1 = estado(K, R, ids, tau); ok1 &= (B[i1] < A[i1])
        out[f'F5_{L}'] = np.where(ok1, np.log1p(TA[i1]), np.nan); out[f'F2_{L}'] = np.where(ok1, TB[i1] / np.maximum(TB[i1] + TA[i1], 1e-9), np.nan)
        out[f'bid_{L}'] = np.where(ok1, B[i1], np.nan); out[f'ask_{L}'] = np.where(ok1, A[i1], np.nan); out[f'edad_{L}'] = np.where(ok1, tau - R[i1], np.nan)
    res.append(out); print(d, 'q filas tokens', len(Q), 'fills', len(g), 'F5_100 valido', float(np.isfinite(out.F5_100).mean()))
fills = fills.join(pd.concat(res))
def ter(f): return np.where(~np.isfinite(f), 'nan', np.where(f <= C0, 'bajo', np.where(f <= C1, 'medio', 'alto')))
for L in LAGS: fills[f'ter_{L}'] = ter(fills[f'F5_{L}'].values)
# --- validacion cruzada con la poblacion (r_D): reloj y F5
rows = []
for d, g in fills.groupby('dia'):
    r = pd.read_pickle(DL + f'r_{d}.pkl')
    for i, x in g.iterrows():
        c = r[(r.tid == x.tid) & (np.abs(r.q - x.precio) < 1e-6) & (np.abs(r.r - x.t_fill) <= 2000)]
        if len(c) >= 1:
            j = (c.r - x.t_fill).abs().idxmin(); rows.append((i, int(c.loc[j, 'r'] - x.t_fill), float(c.loc[j, 'F5']), len(c)))
V = pd.DataFrame(rows, columns=['i', 'dr', 'F5_pob', 'n']).set_index('i'); fills = fills.join(V)
print('join poblacion:', len(V), 'de', len(fills), '| offset r-t_fill ms p5/p50/p95', np.percentile(V.dr, [5, 50, 95]).tolist())
m = V.join(fills.F5_100).dropna(); print('F5 propio vs poblacion (misma fila): iguales (|d|<1e-4):', int((np.abs(m.F5_pob - m.F5_100) < 1e-4).sum()), 'de', len(m))
print('F5_100 valido', float(np.isfinite(fills.F5_100).mean()), '| terciles@100:', fills.ter_100.value_counts().to_dict(), '| @250:', fills.ter_250.value_counts().to_dict())
fills.to_pickle(AQ + '/B_fills.pkl')
# --- ordenes (ledger)
P = {}; post_ts = {}; can_ts = {}
with open(LED) as f:
    for line in f:
        try: o = json.loads(line)
        except Exception: continue
        t = o.get('tipo')
        if t == 'puja_post' and o.get('real'): P[o['oid']] = o
        elif t == 'intencion_cancel' and o.get('real'): can_ts[o['oid']] = o['ts']
O = pd.DataFrame([{k: v for k, v in o.items() if k in ('oid', 'slug', 'coin', 'lado', 'k', 'precio', 'size', 'T', 't_dec', 'cola', 'variante')} |
                  {'TA': (o['libro']['asks'][0][1] if o['libro'].get('asks') else np.nan), 'TB': (o['libro']['bids'][0][1] if o['libro'].get('bids') else np.nan),
                   'bid_top': (o['libro']['bids'][0][0] if o['libro'].get('bids') else np.nan), 'ask_top': (o['libro']['asks'][0][0] if o['libro'].get('asks') else np.nan), 'ts_post': o['ts']} for o in P.values()])
O['F5_post'] = np.log1p(O.TA.astype(float)); O['ter_post'] = ter(O.F5_post.values)
O['dia'] = O.ts_post.str[:10]; O['cierre'] = O.slug.str.rsplit('-', n=1).str[1].astype('int64') + 300
fo = fills.groupby('oid').agg(acc=('size', 'sum'), pnl=('size', lambda s: 0.0)).reset_index()
fills['pnl'] = fills['size'] * (fills.gana - fills.precio); fills['coste'] = fills['size'] * fills.precio
fo = fills.groupby('oid').agg(acc_fill=('size', 'sum'), pnl=('pnl', 'sum'), coste=('coste', 'sum'), gana=('gana', 'first')).reset_index()
O = O.merge(fo, on='oid', how='left'); O['relleno'] = O.acc_fill.notna()
print('ordenes', len(O), 'rellenadas', int(O.relleno.sum()), '| fills con oid en ledger', int(fills.oid.isin(O.oid).sum()), 'de', len(fills), '| dias', O.dia.value_counts().sort_index().to_dict())
print('F5_post valido', float(np.isfinite(O.F5_post).mean()), O.ter_post.value_counts().to_dict())
fills.to_pickle(AQ + '/B_fills.pkl'); O.to_pickle(AQ + '/B_ordenes.pkl')
