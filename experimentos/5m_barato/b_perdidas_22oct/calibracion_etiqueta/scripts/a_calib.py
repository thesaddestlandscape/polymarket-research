#!/usr/bin/env python3
"""a_calib.py: Parte A (PREREG_CALIB). Calibra la etiqueta virtual contra los rellenos reales de B. Entrada: datalogs/calibracion_etiqueta/{ordenes_b.parquet, cal_B_D.csv.gz}. Salida: datos/a_calib.json + stdout."""
import json, glob, sys
import numpy as np, pandas as pd
import os
DL = os.environ.get('CALIB_DL', '/root/polymarket-research-datalogs/calibracion_etiqueta/'); OUTD = os.environ.get('CALIB_OUT', __file__.rsplit('/', 2)[0] + '/datos/')
VARS = [(f, sw) for f in (0.0, 0.25, 0.5, 1.0) for sw in (0, 1)]; NV = len(VARS)
rng = np.random.default_rng(20261026)
B = pd.read_parquet(DL + 'ordenes_b.parquet')
C = pd.concat([pd.read_csv(f, dtype={'oid': str}) for f in sorted(glob.glob(DL + 'cal_B_2026-10-2*.csv.gz'))], ignore_index=True)
print('cal filas', len(C), C.tag.value_counts().to_dict())
def wilson(k, n, z=1.96):
    if n == 0: return (np.nan, np.nan)
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)); return ((c - h) / d, (c + h) / d)
def auc(score, y):
    y = np.asarray(y); s = np.asarray(score, float)
    if y.sum() == 0 or y.sum() == len(y): return np.nan
    r = pd.Series(s).rank().values; n1 = y.sum(); n0 = len(y) - n1; return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))
def boot_ev(df, pnl, cost, key='cie', nb=2000):
    g = df.assign(_p=pnl, _c=cost).groupby(key)[['_p', '_c']].sum().values
    if len(g) < 2 or g[:, 1].sum() <= 0: return None
    est = [ (lambda ix: g[ix, 0].sum() / max(g[ix, 1].sum(), 1e-9))(rng.integers(0, len(g), len(g))) for _ in range(nb)]
    return [float(np.percentile(est, 5)), float(np.percentile(est, 95))]
Bq = B.set_index('oid')
R = C[C.tag == 'R'].drop_duplicates('oid').set_index('oid').join(Bq[['fill', 'fill_puja', 'puja', 'dia', 'cie', 'precio', 'size', 'acc_llena', 'gana_lado', 'pnl', 'coste', 'coin']], rsuffix='_b', how='inner')
print('ordenes R unidas', len(R), 'de', len(B), 'reales; dias', R.dia_b.value_counts().to_dict() if 'dia_b' in R else '')
TUNE = ['2026-10-20', '2026-10-21']; TEST = ['2026-10-22', '2026-10-23']
def metricas(sub, tag_df, i, nivel='orden'):
    """sub: ordenes reales (indice oid) del tramo; tag_df: filas del tag; i: variante."""
    ft = tag_df['v%d_ft' % i].notna()
    if nivel == 'orden':
        x = tag_df.join(Bq[['fill']], how='inner'); x = x[x.index.isin(sub.index)]
        v = x['v%d_ft' % i].notna().values.astype(int); y = x.fill.values.astype(int)
    else:
        g1 = tag_df[tag_df.index.isin(sub.index)] if tag_df.index.name == 'oid' else tag_df
        x = g1
        v = None
    return None
out = {'tramos': {}}
def tabla_orden(sub, tag='R'):
    x = sub; res = {}
    y = x.fill.values.astype(int); n = len(x); k = int(y.sum()); res['n_ordenes'] = n; res['n_real'] = k; res['P_real'] = k / n; res['P_real_W95'] = wilson(k, n)
    pr = x.groupby('puja').fill_puja.max(); res['n_pujas'] = int(len(pr)); res['P_puja_real'] = float(pr.mean())
    res['EV_real'] = float(x.pnl[y == 1].sum() / x.coste[y == 1].sum()) if k else None; res['EV_real_IC90_cierre'] = boot_ev(x[y == 1], x.pnl[y == 1], x.coste[y == 1]) if k > 3 else None
    res['v'] = {}
    for i, (f, sw) in enumerate(VARS):
        v = x['v%d_ft' % i].notna().values.astype(int); tp = int(((v == 1) & (y == 1)).sum()); fp = int(((v == 1) & (y == 0)).sum()); fn = int(((v == 0) & (y == 1)).sum()); tn = int(((v == 0) & (y == 0)).sum())
        pv = v.mean(); po = (tp + tn) / n; pe = (pv * y.mean() + (1 - pv) * (1 - y.mean())); kap = (po - pe) / (1 - pe) if pe < 1 else np.nan
        pvp = x.assign(_v=v).groupby('puja')._v.max().mean()
        evm = x[v == 1]; cost = evm['size'] * evm.precio; pnl = evm['size'] * (evm.gana_lado - evm.precio)
        res['v'][i] = dict(f=f, barrido=sw, P_v=float(pv), P_v_puja=float(pvp), recall=tp / max(tp + fn, 1), precision=tp / max(tp + fp, 1), kappa=float(kap), tp=tp, fp=fp, fn=fn,
                           AUC=auc((x.cons / (x.Q + x['size'])).values if False else x.cons.values / (x.Q.values + x['size'].values) if 'size' in x else x.cons.values, y),
                           EV_v=float(pnl.sum() / cost.sum()) if len(evm) and cost.sum() > 0 else None, n_v=int(v.sum()), EV_v_IC90_cierre=boot_ev(evm, pnl, cost) if len(evm) > 3 else None)
    return res
R = R.rename(columns={'dia': 'dia_cal'}); R['dia'] = R.dia_b if 'dia_b' in R else R.dia_cal
R['size'] = R['s'] if 's' in R else R['size']
for nm, ds in (('TUNE', TUNE), ('TEST', TEST), ('TODO', TUNE + TEST)):
    x = R[R.dia.isin(ds)]; out['tramos'][nm] = tabla_orden(x)
# seleccion en TUNE
T = out['tramos']['TUNE']; best = None
for i, m in T['v'].items():
    if m['P_v'] <= 0 or m['P_v_puja'] <= 0: loss = np.inf
    else: loss = abs(np.log(m['P_v'] / T['P_real'])) + abs(np.log(m['P_v_puja'] / T['P_puja_real']))
    m['loss_TUNE'] = float(loss); cand = (loss, -(m['recall'] * m['precision']))
    if best is None or cand < best[0]: best = (cand, i)
isel = best[1]; out['seleccion'] = {'indice': isel, 'f': VARS[isel][0], 'barrido': VARS[isel][1], 'loss_TUNE': best[0][0]}
# criterios en TEST
S = out['tramos']['TEST']; m = S['v'][isel]; lo, hi = S['P_real_W95']
c1 = (abs(m['P_v'] / S['P_real'] - 1) <= 0.30) or (lo <= m['P_v'] <= hi); c2 = abs(m['P_v_puja'] - S['P_puja_real']) <= 0.10
c3 = m['recall'] >= 0.5 and m['precision'] >= 0.5; c4 = (m['AUC'] or 0) >= 0.75; c5 = (m['EV_v'] is not None and S['EV_real'] is not None and abs(m['EV_v'] - S['EV_real']) <= 0.15)
out['criterios_TEST'] = dict(C1_P_orden=bool(c1), C2_P_puja=bool(c2), C3_recall_precision=bool(c3), C4_AUC=bool(c4), C5_EV_informativo=bool(c5))
out['CALIBRADA'] = bool(c1 and c2 and c3 and c4)
# descomposicion 51 % vs 5,1 % (todas las ordenes 20-23, variante f=1 sin barrido = F8, y la seleccionada)
dec = {}
for tag in ('R', 'L60', 'BB60'):
    t = C[C.tag == tag].drop_duplicates('oid').set_index('oid'); t = t[t.index.isin(Bq.index)].join(Bq[['fill']])
    dec[tag] = {}
    for i in (7 - 1 if False else 6, isel):  # (f=1, sin barrido) = indice 6 ; seleccionada
        v = t['v%d_ft' % i].notna(); dec[tag][i] = dict(n=int(len(t)), P_orden=float(v.mean()), P_puja=float(t.assign(_v=v).groupby('puja')._v.max().mean()))
for tag in ('PE', 'P60'):
    t = C[C.tag == tag].drop_duplicates('puja').set_index('puja'); real = B.groupby('puja').fill_puja.max(); t = t[t.index.isin(real.index)].join(real.rename('fill_real'))
    dec[tag] = {}
    for i in (6, isel):
        v = t['v%d_ft' % i].notna(); y = t.fill_real.values
        dec[tag][i] = dict(n=int(len(t)), P_puja=float(v.mean()), P_puja_real=float(y.mean()), recall=float(((v.values) & (y == 1)).sum() / max(y.sum(), 1)), precision=float(((v.values) & (y == 1)).sum() / max(v.sum(), 1)),
                           P_puja_TEST=float(v[t.index.map(lambda k: B[B.puja == k].dia.iloc[0] in TEST)].mean()) if False else None)
out['descomposicion'] = dec
# puente en TEST: PE/P60 con variante seleccionada, pujas de TEST
puja_dia = B.groupby('puja').dia.first()
for tag in ('PE', 'P60'):
    t = C[C.tag == tag].drop_duplicates('puja').set_index('puja'); real = B.groupby('puja').fill_puja.max(); t = t[t.index.isin(real.index)].join(real.rename('fill_real')).join(puja_dia.rename('dia_b'))
    t = t[t.dia_b.isin(TEST)]; v = t['v%d_ft' % isel].notna()
    out.setdefault('puente_TEST', {})[tag] = dict(n_pujas=int(len(t)), P_virtual=float(v.mean()), P_real=float(t.fill_real.mean()), dif=float(v.mean() - t.fill_real.mean()), ok=bool(abs(v.mean() - t.fill_real.mean()) <= 0.10))
# sensibilidad: todas las variantes en TEST (P_v, P_v_puja, recall, precision, AUC, EV_v)
out['tabla_TEST'] = {i: {k: m_[k] for k in ('f', 'barrido', 'P_v', 'P_v_puja', 'recall', 'precision', 'kappa', 'AUC', 'EV_v', 'n_v')} for i, m_ in S['v'].items()}
out['tabla_TUNE'] = {i: {k: m_[k] for k in ('f', 'barrido', 'P_v', 'P_v_puja', 'recall', 'precision', 'AUC', 'loss_TUNE')} for i, m_ in T['v'].items()}
json.dump(out, open(OUTD + 'a_calib.json', 'w'), indent=1, default=lambda o: None if o != o else float(o) if isinstance(o, (np.floating, np.integer)) else str(o))
print(json.dumps({k: out[k] for k in ('seleccion', 'criterios_TEST', 'CALIBRADA', 'puente_TEST')}, indent=1, default=float))
for nm in ('TUNE', 'TEST'):
    t = out['tramos'][nm]; print(nm, 'n', t['n_ordenes'], 'real', t['n_real'], 'P_real %.4f' % t['P_real'], 'P_puja_real %.3f' % t['P_puja_real'], 'EV_real', t['EV_real'])
    for i, m_ in t['v'].items(): print('  v%s f=%.2f sw=%d  P=%.4f Ppuja=%.3f rec=%.2f prec=%.2f AUC=%s EV=%s' % (i, m_['f'], m_['barrido'], m_['P_v'], m_['P_v_puja'], m_['recall'], m_['precision'], m_['AUC'], m_['EV_v']))
print(json.dumps(dec, indent=1, default=float))
