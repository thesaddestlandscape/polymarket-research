#!/usr/bin/env python3
"""E-RE-CG-02: favorito tardio tomador al ask real (precierre_multioffset). Solo lectura."""
import json, numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs'
DES = {}
for f in (DL + '/maker_ms_desenlaces_cache.json', DL + '/mapa_escala/des.json', DL + '/desenlaces_por_market_id_cache.json'):
    for k, v in json.load(open(f)).items():
        if v in ('YES', 'NO'): DES.setdefault(str(k), v)
d = pd.read_csv(DL + '/precierre_multioffset_fase0.csv', usecols=['ts_utc', 'activo', 'marco', 'slug', 'market_id', 'offset_s', 'direccion', 'ask', 'profundidad_eur', 'lat_libro_ms'])
d = d[(d.marco == '5m') & d.ask.notna() & (d.ask >= 0.95) & (d.ask < 0.99)].copy()
d = d.drop_duplicates(['slug', 'offset_s'])
d['des'] = pd.to_numeric(d.market_id, errors='coerce').astype('Int64').astype(str).map(DES); print('filas', len(d), 'cobertura desenlace', round(d.des.notna().mean(), 4))
d = d[d.des.notna()]
d['gana'] = (((d.direccion == 'Up') & (d.des == 'YES')) | ((d.direccion == 'Down') & (d.des == 'NO'))).astype(float)
d['pnl'] = d.gana - d.ask - 0.07 * d.ask * (1 - d.ask); d['c'] = d.ask
d['dia'] = d.ts_utc.str[:10]; d['cierre'] = d.slug.str.rsplit('-', n=1).str[1]
d['banda'] = np.where(d.ask < 0.97, '.95-.97', '.97-.99')
rng = np.random.default_rng(20261026)
def boot(x, key):
    g = x.groupby(key)[['pnl', 'c']].sum().values
    if len(g) < 5: return np.nan, np.nan
    idx = rng.integers(0, len(g), (2000, len(g))); s = g[idx].sum(axis=1); r = s[:, 0] / s[:, 1]
    return np.percentile(r, 5), np.percentile(r, 95)
def fila(x, lab):
    ev = x.pnl.sum() / x.c.sum(); lc, hc = boot(x, 'cierre'); ld, hd = boot(x, 'dia')
    pd_ = x.groupby('dia').pnl.sum(); top = pd_.sort_values(ascending=False).index[:2]; y = x[~x.dia.isin(top)]
    fall = x[x.gana == 0].groupby('cierre').size()
    print('%-34s n %5d cierres %5d dias %2d | acierto %.4f ask %.4f | EV %+.4f IC90 cierre (%+.4f,%+.4f) dia (%+.4f,%+.4f) | dias+ %2d/%2d peor dia %+.1f sin2 %+.4f | fallos %d (en racimo %d) | prof p50 %.0f €' % (
        lab, len(x), x.cierre.nunique(), x.dia.nunique(), x.gana.mean(), x.ask.mean(), ev, lc, hc, ld, hd, (pd_ > 0).sum(), len(pd_), pd_.min(),
        y.pnl.sum() / y.c.sum(), int((x.gana == 0).sum()), int(fall[fall >= 2].sum()), x.profundidad_eur.median()))
print('== PRINCIPAL ==')
fila(d[d.offset_s == -60], 'off-60 ask[.95,.99) todas')
print('== descriptivo ==')
for off in (-120, -90, -60, -45, -30, -20, -10):
    for b in ('.95-.97', '.97-.99'):
        x = d[(d.offset_s == off) & (d.banda == b)]
        if len(x) >= 50: fila(x, 'off%d %s' % (off, b))
for a in sorted(d.activo.unique()):
    x = d[(d.offset_s == -60) & (d.activo == a)]
    if len(x) >= 50: fila(x, 'off-60 %s' % a)
x = d[d.offset_s == -60]; print('cierres/dia con entrada off-60: %.1f; lat_libro_ms p50 %.0f p90 %.0f' % (x.groupby('dia').cierre.nunique().mean(), x.lat_libro_ms.median(), x.lat_libro_ms.quantile(.9)))
