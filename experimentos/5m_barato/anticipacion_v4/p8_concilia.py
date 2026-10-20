"""Concilia vigia V4 (BTC, B1_5m es_primero, L215 niveles 1-3) con mi simulacion nivel 1 (v4_D.csv de r3_out). Mismos cierres."""
import csv, glob, json, numpy as np, pandas as pd
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
fee = lambda p: 0.07 * p * (1 - p)
E = []
for f in sorted(glob.glob('/root/polymarket-research-datalogs/vigia_5m_barato/eventos_*.csv')):
    for r in csv.DictReader(open(f)):
        if r['regla'] == 'B1_5m' and r['es_primero'] == '1' and r['moneda'] == 'BTC': E.append(r)
V = pd.DataFrame(E); V['cierre'] = V.cierre.astype(int)
M = pd.concat([pd.read_csv(f) for f in sorted(glob.glob('/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/v4_*.csv')) if __import__('os').path.getsize(f) > 0])
print('vigia BTC primeros', len(V), 'mi sim', len(M), 'cierres comunes', len(set(V.cierre) & set(M.cierre)))
J = V.merge(M, on='cierre', how='inner', suffixes=('_v', '_m'))
J['dt0'] = J.t_deteccion.astype(float) - J.t0
print('t_deteccion vigia - t0 mio (ms) P10/50/90', np.nanpercentile(J.dt0, [10, 50, 90]).round(0), '| ask0 igual:', (J.ask_compra_t0.astype(float).round(2) == J.ask0.round(2)).mean().round(2))
J['pv'] = pd.to_numeric(J.L215_precio, errors='coerce'); J['av'] = pd.to_numeric(J.L215_acciones, errors='coerce')
J['ev_v'] = J.L215_clase.isin(['A_sigue_barato', 'D_otro_nivel_barato']) & (J.av > 0)
J['ev_m'] = J.acc215 > 0
print(pd.crosstab(J.ev_v, J.ev_m, rownames=['vigia ejec'], colnames=['mia ejec']))
print('clases vigia L215:', J.L215_clase.value_counts().to_dict())
print('fuente libro vigia:', J.L215_fuente_libro.value_counts().to_dict())
def pnl(d, p, a, g):
    c = (d[a] * (d[p] + fee(d[p]))); y = d[a] * (d[g].astype(float) - d[p] - fee(d[p])); return y.sum(), c.sum(), len(d)
for nom, mask, p, a in (('vigia (solo comunes ejec vigia)', J.ev_v, 'pv', 'av'), ('mia nivel 1 (comunes ejec mia)', J.ev_m, 'p215', 'acc215')):
    d = J[mask].copy()
    y, c, n = pnl(d, p, a, 'gana'); print(f'{nom}: n={n} coste={c:.1f} PnL={y:+.2f} EV={y/c:+.3f}')
d = J[J.ev_v & J.ev_m].copy(); print('ejecutables en ambas:', len(d))
for nom, p, a in (('vigia', 'pv', 'av'), ('mia', 'p215', 'acc215')):
    y, c, n = pnl(d, p, a, 'gana'); print(f'  {nom}: n={n} coste={c:.1f} PnL={y:+.2f} EV={y/c:+.3f}')
d = J[J.ev_v & J.ev_m]; 
print('vigia sin comunes: eventos vigia BTC ejec totales (todos dias):'); Vv=V[V.L215_clase.isin(['A_sigue_barato','D_otro_nivel_barato'])].copy(); Vv['pv']=pd.to_numeric(Vv.L215_precio); Vv['av']=pd.to_numeric(Vv.L215_acciones); Vv['g']=[DES.get(m)==('YES' if l=='Up' else 'NO') for m,l in zip(Vv.market_compra,Vv.lado)]; y=(Vv.av*(Vv.g.astype(float)-Vv.pv-fee(Vv.pv))).sum(); c=(Vv.av*(Vv.pv+fee(Vv.pv))).sum(); print(len(Vv),c,y,y/c); print(Vv[~Vv.cierre.isin(M.cierre)][['cierre','pv','av','g','ask_compra_t0','margen_neto','resto_s']])
print('dias vigia 05-19 vs comunes: dias comunes', sorted(set(J.dia)))
