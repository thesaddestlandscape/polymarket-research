#!/usr/bin/env python3
"""c1_build_b.py: tabla de ordenes reales de B (ledger H47-B 20-23 Oct) + verdad (etiquetado_pasivo_B) + rho_off. Solo lectura."""
import json, glob, datetime as dt, collections, statistics as st
import numpy as np, pandas as pd
DL = '/root/polymarket-research-datalogs/'; OUT = DL + 'calibracion_etiqueta/'
def ep(s): return dt.datetime.fromisoformat(s).timestamp()
O = {}; tok = {}; vis = {}; cint = {}; fuera = {}
for l in open(DL + 'experimento_h47_B_ledger.jsonl'):
    try: d = json.loads(l)
    except Exception: continue
    t = d.get('tipo'); oid = d.get('oid')
    if t == 'intencion_post': tok[oid] = d['tok']
    elif t == 'puja_post': O[oid] = d
    elif t == 'post_lat': O.setdefault(oid, {})['_lat'] = d
    elif t == 'visto': vis[oid] = d['t']
    elif t == 'intencion_cancel': cint[oid] = ep(d['ts'])
    elif t == 'fuera_libro': fuera[oid] = ep(d['ts'])
rows = []; rho = collections.defaultdict(list)
for oid, d in O.items():
    if 'slug' not in d or oid not in tok: continue
    lat = O[oid].get('_lat') if False else None
rows = []
lat = {}
for l in open(DL + 'experimento_h47_B_ledger.jsonl'):
    try: d = json.loads(l)
    except Exception: continue
    if d.get('tipo') == 'post_lat': lat[d['oid']] = d
for oid, d in O.items():
    if 'slug' not in d or oid not in tok: continue
    L = lat.get(oid)
    t_call0 = L['t_call0'] if L else d['t_dec']; post_ms = L['ms'] if L else 300.0
    cie = int(d['slug'].rsplit('-', 1)[1]) + 300
    bids = d['libro']['bids']; p = d['precio']
    bb = bids[0][0] if bids else None; bs = bids[0][1] if bids else None
    if bids:
        off = int(round((bb - p) * 100)); lev = {round(x[0], 2): x[1] for x in bids}
        if off in (1, 2) and bs and bs > 0 and round(bb - off / 100, 2) in lev: rho[off].append(lev[round(bb - off / 100, 2)] / bs)
    rows.append(dict(oid=oid, slug=d['slug'], tok=tok[oid], coin=d['coin'], lado=d['lado'], precio=p, size=d['size'], cola=d.get('cola'), bb=bb, bs=bs, off_c=(int(round((bb - p) * 100)) if bb is not None else None),
                     t_dec=d['t_dec'], t_call0=t_call0, post_ms=post_ms, t_ini=t_call0 + 0.5 * post_ms / 1000.0, t_cancel_int=cint.get(oid), t_fuera=fuera.get(oid), cie=cie, n_orden=d['n_orden'], T=d['T']))
B = pd.DataFrame(rows)
B['t_fin'] = np.where(B.t_cancel_int.notna(), B.t_cancel_int + 0.030, np.where(B.t_fuera.notna(), B.t_fuera, B.cie - 2.0))
B['t_fin'] = np.minimum(B.t_fin, B.cie - 2.0)
B['dia'] = pd.to_datetime(B.t_ini, unit='s', utc=True).dt.strftime('%Y-%m-%d')
E_ = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(DL + 'etiquetado_pasivo_B/etiquetado_B_2026-10-2*.csv.gz'))], ignore_index=True)
E_ = E_[E_.unidad == 'orden'][['id', 'gana_lado', 'resuelto', 'acc_llena']].rename(columns={'id': 'oid', 'acc_llena': 'acc_llena_etiq'})
B = B.merge(E_, on='oid', how='left')
# VERDAD = on-chain por order_hash (c0_verdad_onchain.py); etiquetado_pasivo_B solo aporta el desenlace oficial y se contrasta
OC = pd.read_csv(OUT + 'b_fills_onchain.csv'); OC['oid'] = OC.order_hash.str.lower()
g = OC.groupby('oid').agg(acc_llena=('taker_amt', 'sum'), coste=('maker_amt', 'sum'), n_fills_oc=('tx', 'size'))
B['oid_l'] = B.oid.str.lower(); B = B.merge(g, left_on='oid_l', right_index=True, how='left').drop(columns='oid_l')
B[['acc_llena', 'coste', 'n_fills_oc']] = B[['acc_llena', 'coste', 'n_fills_oc']].fillna(0.0)
B['fill'] = (B.acc_llena > 0).astype(int)
B['pnl'] = B.acc_llena * B.gana_lado - B.coste
nohash = set(OC.oid) - set(B.oid.str.lower())
print('ON-CHAIN: fills', len(OC), 'ordenes con fill', int(B.fill.sum()), 'coste', round(OC.maker_amt.sum(), 2), 'fills de hashes fuera del ledger de B:', int(OC.oid.isin(nohash).sum()))
print('contraste etiquetado: ordenes rellenas segun etiquetado', int((B.acc_llena_etiq > 0).sum()), 'discrepan en fill (oc vs etiq):', int(((B.acc_llena_etiq.fillna(0) > 0) != (B.fill == 1)).sum()), '| PnL on-chain', round(B.pnl.sum(), 2))
B['puja'] = B.slug + '|' + B.lado
# CORRECCION 26-Oct: acc_llena de etiquetado_pasivo_B estaba duplicada (relleno_tardio contado 2 veces) -> corregido en etiquetar_pasivo.py; aqui se reconcilia con las posiciones.
PS = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(DL + 'etiquetado_pasivo_B/etiquetado_B_2026-10-2*.csv.gz'))], ignore_index=True)
PS = PS[PS.unidad == 'posicion']
pk = set((m + '|' + ('YES' if o == 'Up' else 'NO')) for m, o in zip(PS.mercado, PS.outcome))
B['fill_puja'] = ((B.groupby('puja').fill.transform('max') == 1) | B.puja.isin(pk)).astype(int)
fo = B[B.fill == 1]
print('RECONCILIACION: ordenes rellenas', len(fo), 'acc', round(fo.acc_llena.sum(), 2), 'pnl ordenes', round(fo.pnl.sum(), 2), '| posiciones', len(PS), 'acc', round(PS.acc_llena.sum(), 2), 'pnl', round(PS.pnl.sum(), 2),
      '| pujas con relleno solo por posicion (relleno no atribuido a una orden):', int(((B.groupby('puja').fill.max() == 0) & (B.groupby('puja').fill_puja.max() == 1)).sum()))
R = {str(k): {'mediana': float(np.median(v)), 'n': len(v), 'p25': float(np.percentile(v, 25)), 'p75': float(np.percentile(v, 75))} for k, v in rho.items()}
R['0'] = {'mediana': 1.0, 'n': 0}
json.dump(R, open(OUT + 'rho.json', 'w'), indent=1)
B.to_parquet(OUT + 'ordenes_b.parquet'); B.to_csv(OUT + 'ordenes_b.csv', index=False)
print(len(B), 'ordenes', B.fill.sum(), 'rellenas', B.resuelto.isna().sum(), 'sin etiqueta'); print(B.groupby('dia').agg(n=('oid', 'size'), f=('fill', 'mean'))); print(R)
print('vida real (t_fin-t_ini) p10/50/90', np.percentile(B.t_fin - B.t_ini, [10, 50, 90]).round(3), 'off_c', B.off_c.value_counts().to_dict())
pj = B.groupby('puja').agg(n=('oid', 'size'), f=('fill', 'max'), dur=('t_fin', 'max'), ini=('t_ini', 'min')); pj['dur'] = pj.dur - pj.ini
print('pujas', len(pj), 'fill puja', pj.f.mean().round(3), 'dur p10/50/90', np.percentile(pj.dur, [10, 50, 90]).round(1), 'ordenes/puja med', pj.n.median())
