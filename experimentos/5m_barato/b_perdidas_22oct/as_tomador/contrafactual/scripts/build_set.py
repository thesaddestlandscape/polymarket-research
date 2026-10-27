#!/usr/bin/env python3
"""build_set.py -- congela el SET de tomadores 'informados' con datos hasta 2026-10-23 23:59Z (corre UNA vez; no se vuelve a ejecutar tras el prereg).
SET_I (primario): ventana 09..23-Oct, n_fills>=30, coste_tomador>=50, ROI BRUTO (pnl_bruto/coste) >= +0,02.
SET_V (replica exacta del verificador): ventana 09..18-Oct, n>=100, coste>=200, ROI bruto >= +0,02 (verificacion/v3_B.py::inf_gro, 370 tomadores).
POOL_I: tomadores con n>=30 y coste>=50 en la ventana de SET_I (universo del placebo).
Salida: datos/set_I.txt, set_V.txt, pool_I.txt, SETS_META.json (hashes sha256). nice 19 / ionice idle / ulimit -v 3000000."""
import sys, json, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pandas as pd
import cf_lib as L

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
des = L.load_des()
days = ['2026-10-%02d' % d for d in range(9, 24)]
S = {}
for d in days:
    S[d] = L.cached_stats(d, des)
    print(d, 'takers', len(S[d]), 'fills', int(S[d].n.sum()), flush=True)


def agg(ds):
    A = pd.concat([S[d] for d in ds]).groupby('taker').agg(n=('n', 'sum'), coste=('coste', 'sum'), pnl=('pnl_bruto', 'sum')).reset_index()
    A['roi'] = A.pnl / A.coste
    return A


AI = agg(days)
SI = AI[(AI.n >= 30) & (AI.coste >= 50) & (AI.roi >= 0.02)]
PI = AI[(AI.n >= 30) & (AI.coste >= 50)]
AV = agg(days[:10])
SV = AV[(AV.n >= 100) & (AV.coste >= 200) & (AV.roi >= 0.02)]
meta = {'congelado_con_datos_hasta': '2026-10-23T23:59:59Z', 'ventana_I': [days[0], days[-1]], 'ventana_V': [days[0], days[9]],
        'criterio_I': 'n>=30, coste_tomador>=50, ROI bruto>=0.02', 'criterio_V': 'n>=100, coste>=200, ROI bruto>=0.02 (replica verificador)',
        'n_I': int(len(SI)), 'n_V': int(len(SV)), 'n_pool_I': int(len(PI)), 'interseccion_I_V': int(len(set(SI.taker) & set(SV.taker)))}
for nm, df in (('set_I', SI), ('set_V', SV), ('pool_I', PI)):
    items = list(df.taker)
    open(os.path.join(OUT, nm + '.txt'), 'w').write('\n'.join(sorted(items)) + '\n')
    meta['sha256_' + nm] = L.sha256_lines(items)
json.dump(meta, open(os.path.join(OUT, 'SETS_META.json'), 'w'), indent=1)
print(json.dumps(meta, indent=1))
