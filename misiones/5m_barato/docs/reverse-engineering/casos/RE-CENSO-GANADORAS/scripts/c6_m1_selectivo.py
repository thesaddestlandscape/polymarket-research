#!/usr/bin/env python3
"""E-RE-CG-03: M1 selectivo por z, DESC->OOS. Solo lectura."""
import json, numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs'
DES = {}
for f in (DL + '/maker_ms_desenlaces_cache.json', DL + '/mapa_escala/des.json', DL + '/desenlaces_por_market_id_cache.json'):
    for k, v in json.load(open(f)).items():
        if v in ('YES', 'NO'): DES.setdefault(str(k), v)
d = pd.read_csv(DL + '/precierre_multioffset_fase0.csv', usecols=['ts_utc', 'activo', 'marco', 'slug', 'market_id', 'offset_s', 'direccion', 'ask', 'z', 'z_v2', 'profundidad_eur'])
d = d[(d.marco == '5m') & d.offset_s.isin([-120, -90, -60]) & d.ask.between(0.95, 0.99)].drop_duplicates(['slug', 'offset_s']).copy()
d['des'] = pd.to_numeric(d.market_id, errors='coerce').astype('Int64').astype(str).map(DES)
print('filas', len(d), 'cobertura', round(d.des.notna().mean(), 4)); d = d[d.des.notna()]
d['zz'] = d.z_v2.fillna(d.z).abs()
d['gana'] = (((d.direccion == 'Up') & (d.des == 'YES')) | ((d.direccion == 'Down') & (d.des == 'NO'))).astype(float)
d['pnl'] = d.gana - d.ask - 0.07 * d.ask * (1 - d.ask); d['c'] = d.ask; d['dia'] = d.ts_utc.str[:10]
DESC = d.dia <= '2026-10-10'; rng = np.random.default_rng(20261026)
def stats(x):
    g = x.groupby('dia')[['pnl', 'c']].sum(); v = g.values; idx = rng.integers(0, len(v), (4000, len(v))); s = v[idx].sum(axis=1); r = s[:, 0] / s[:, 1]
    top = g.pnl.sort_values(ascending=False).index[:2]; y = g.drop(top)
    return dict(n=len(x), cierres=x.slug.nunique(), dias=len(g), ev=v[:, 0].sum() / v[:, 1].sum(), lo=np.percentile(r, 5), hi=np.percentile(r, 95), pboot=(r <= 0).mean(),
                dpos=(g.pnl > 0).mean(), sin2=y.pnl.sum() / y.c.sum(), acierto=x.gana.mean(), ask=x.ask.mean())
for off in (-120, -90, -60):
    best = None
    for u in (2, 3, 4, 5, 6, 8):
        x = d[DESC & (d.offset_s == off) & (d.zz >= u)]
        if len(x) < 300: continue
        s = stats(x); print('DESC off %d z>=%d' % (off, u), {k: round(v, 4) for k, v in s.items()})
        if best is None or s['ev'] > best[1]: best = (u, s['ev'])
    if best is None: print('off', off, 'sin umbral con n>=300'); continue
    for lab, x in (('OOS elegido z>=%d' % best[0], d[~DESC & (d.offset_s == off) & (d.zz >= best[0])]), ('OOS control sin z', d[~DESC & (d.offset_s == off)])):
        s = stats(x); ok = s['ev'] >= .005 and s['lo'] > 0 and s['pboot'] < .033 and s['dpos'] >= .65 and s['sin2'] > 0 and s['cierres'] >= 300
        print('>>> off %d %s' % (off, lab), {k: round(v, 4) for k, v in s.items()}, 'CANDIDATA' if ok and 'elegido' in lab else '')
