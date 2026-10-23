#!/usr/bin/env python3
"""e2_run.py DIAS CELDAS SALIDA [var] -- PREREG_E2. DIAS: 2026-10-20 | 2026-10-21,2026-10-22 ; CELDAS: 'rej' (6 celdas) | 'cad:dobs' (celda unica)
var: base | lo | hi | inf. Salida datos/e2_<SALIDA>_<var>_{ordenes,pujas}.csv + manifiesto. Solo lectura de produccion."""
import os, sys, json, time, hashlib, collections, bisect
sys.dont_write_bytecode = True
import e2_engine as E
import numpy as np, pandas as pd
S = E.S
dias = sys.argv[1].split(','); celdas = sys.argv[2]; tag = sys.argv[3]; var = sys.argv[4] if len(sys.argv) > 4 else 'base'
LIM = int(os.environ.get('E2_LIM', '0'))
D = E.D; SEED = 20261023
R = pd.read_csv(os.path.join(D, 'cal_real_pujas.csv'), dtype={'mid': str}); R = R[R.dia.isin(dias)]
TOK = json.load(open(S.SRC + 'tokens.json')); bys = collections.defaultdict(dict)
for t, v in TOK.items():
    if v[0] in ('ETH', 'SOL', 'XRP'): bys[int(float(v[3]))][v[0]] = str(v[1])
slots = sorted(set(int(x) for x in R.fin if S.FIN_MIN <= int(x) <= S.FIN_MAX))
if LIM: slots = slots[:LIM]
if celdas == 'rej': CELLS = [(c, d) for c in (0.10, 0.25, 0.50) for d in (0, 100)]
else: CELLS = [(float(celdas.split(':')[0]), int(celdas.split(':')[1]))]
VARS = {'base': ('prop', 'obs'), 'lo': ('lo', 'obs'), 'hi': ('hi', 'obs'), 'inf': ('prop', 'inf')}
alloc, bmode = VARS[var]
bud, nobs = E.make_budget()
budget = bud if bmode == 'obs' else None
man = dict(job=f'e2_{tag}_{var}', codigo_h47_sha=E.H_SHA, prereg_sha=hashlib.sha256(open(os.path.join(D, '..', 'prereg', 'PREREG_E2_ORDEN_DECIDIR.md'), 'rb').read()).hexdigest(),
           dias=dias, celdas=CELLS, var=var, alloc=alloc, budget=bmode, n_obs_presupuesto=nobs, slots=len(slots), start=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), status='RUNNING')
json.dump(man, open(os.path.join(D, f'e2_{tag}_{var}_manifest.json'), 'w'), indent=1)
OO, PP = [], []; miss = collections.Counter(); t0 = time.time()
for si, fin in enumerate(slots):
    mkts = {}
    for act, mid in bys.get(fin, {}).items():
        path = S.SRC + f'mk/{act}_{mid}.gz'
        if not os.path.exists(path) or S.DES.get(mid) is None: miss['sin_fichero_o_desenlace'] += 1; continue
        gi = bisect.bisect_left(S.GALL, (fin - 305) * 1000)
        if gi < len(S.GALL) and S.GALL[gi] <= (fin - 60) * 1000: miss['hueco_global'] += 1; continue
        m = E.Mkt(act, mid, fin)
        if m.roto or m.TT is None: miss['hueco_token'] += 1; continue
        mkts[act] = m
    if not mkts: continue
    for (cad, dobs) in CELLS:
        o, p = E.run_slot(mkts, cad, dobs, budget, alloc, SEED)
        for x in o: x.update(cad=cad, dobs=dobs, var=var)
        for x in p: x.update(cad=cad, dobs=dobs, var=var)
        OO += o; PP += p
    if (si + 1) % 10 == 0: print(f'{time.strftime("%H:%M:%S")} slot {si+1}/{len(slots)} t={time.time()-t0:.0f}s orders={len(OO)} pujas={len(PP)} miss={dict(miss)}', flush=True)
pd.DataFrame(OO).to_csv(os.path.join(D, f'e2_{tag}_{var}_ordenes.csv'), index=False)
pd.DataFrame(PP).to_csv(os.path.join(D, f'e2_{tag}_{var}_pujas.csv'), index=False)
man.update(status='COMPLETE', end=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), n_ordenes=len(OO), n_pujas=len(PP), excluidos=dict(miss), seg=round(time.time() - t0))
json.dump(man, open(os.path.join(D, f'e2_{tag}_{var}_manifest.json'), 'w'), indent=1); print('FIN', man, flush=True)
