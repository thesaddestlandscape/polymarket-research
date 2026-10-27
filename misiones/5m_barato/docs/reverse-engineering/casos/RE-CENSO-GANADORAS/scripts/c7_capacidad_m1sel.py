#!/usr/bin/env python3
"""c7 (descriptivo, POST-HOC de la regla congelada off-120 z>=8 ask[.95,.99]): capacidad, perdidas, monedas, racimos. Solo lectura."""
import json, numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs'
DES = {}
for f in (DL + '/maker_ms_desenlaces_cache.json', DL + '/mapa_escala/des.json', DL + '/desenlaces_por_market_id_cache.json'):
    for k, v in json.load(open(f)).items():
        if v in ('YES', 'NO'): DES.setdefault(str(k), v)
d = pd.read_csv(DL + '/precierre_multioffset_fase0.csv', usecols=['ts_utc', 'activo', 'marco', 'slug', 'market_id', 'offset_s', 'direccion', 'ask', 'z', 'z_v2', 'profundidad_eur', 'lat_libro_ms'])
d = d[(d.marco == '5m') & (d.offset_s == -120) & d.ask.between(0.95, 0.99)].drop_duplicates('slug').copy()
d['zz'] = d.z_v2.fillna(d.z).abs(); d = d[d.zz >= 8]
d['des'] = pd.to_numeric(d.market_id, errors='coerce').astype('Int64').astype(str).map(DES)
print('n', len(d), 'sin desenlace', int(d.des.isna().sum()), '(missing; por dia):', d[d.des.isna()].ts_utc.str[:10].value_counts().sort_index().to_dict())
d = d[d.des.notna()]
d['gana'] = (((d.direccion == 'Up') & (d.des == 'YES')) | ((d.direccion == 'Down') & (d.des == 'NO'))).astype(float)
d['dia'] = d.ts_utc.str[:10]; d['epoch'] = d.slug.str.rsplit('-', n=1).str[1]
print('perdidas:'); print(d[d.gana == 0][['ts_utc', 'activo', 'ask', 'zz', 'profundidad_eur']].to_string())
print('por moneda', d.groupby('activo').agg(n=('gana', 'size'), acierto=('gana', 'mean'), ask=('ask', 'mean'), prof_p50=('profundidad_eur', 'median')).round(4).to_string())
print('profundidad_eur al ask: p10 %.0f p50 %.0f p90 %.0f; entradas/dia %.1f; epochs/dia %.1f; lat p50 %.0f ms' % (d.profundidad_eur.quantile(.1), d.profundidad_eur.median(), d.profundidad_eur.quantile(.9), d.groupby('dia').size().mean(), d.groupby('dia').epoch.nunique().mean(), d.lat_libro_ms.median()))
for cap in (10, 50, 200, 1000):
    st = np.minimum(d.profundidad_eur.fillna(0), cap); pnl = (st / d.ask) * (d.gana - d.ask - 0.07 * d.ask * (1 - d.ask))
    print('stake <= %4d €/entrada: coste/dia %.0f € pnl/dia %+.1f € -> %.1f k€/año (contrafactual, profundidad nivel 1, sin competencia)' % (cap, st.sum() / d.dia.nunique(), pnl.sum() / d.dia.nunique(), pnl.sum() / d.dia.nunique() * 365 / 1000))
