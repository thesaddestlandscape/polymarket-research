"""popdata_add2.py -- ADDENDUM2 §2/§6: poblacion de 37 dias = 35 caches de ADD1 (epoca por timestamp, C3 OK; via popdata.carga_pob sin cambios)
+ 2 caches de ADD2 (2026-10-16 y 2026-10-24; epoca por suelo medido por ventana de 10 min: R0hi / R1lo / ... / indet). Solo lectura. Lo usan e2_agrega_add2, e5_regimen_add2 y e6_brecha_add2."""
import os, sys, json, hashlib; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import popdata as _p
from popdata import *
ADD2_SHA = open(AQ + 'ADDENDUM2_B_F5.sha256').read().split()[0]
assert hashlib.sha256(open(AQ + 'ADDENDUM2_B_F5.md', 'rb').read()).hexdigest() == ADD2_SHA, 'ADDENDUM2 modificado tras el sellado'
DIAS_ADD2 = ('2026-10-16', '2026-10-24')
DET_ADD2 = 'ADD2 epoca por suelo medido'
def estado_dias():
    """Estados de ADD1; los 2 dias FAILED-C3 pasan a COMPLETE solo si su cache ADD2 es COMPLETE con el sha de ADDENDUM2 y el pickle existe."""
    out = _p.estado_dias()
    for d in DIAS_ADD2:
        if out.get(d, ('',))[0] == 'COMPLETE': continue
        p = CACHE + f'pob_add2_{d}.json'
        if not os.path.exists(p): out[d] = ('FALTA_ADD2', 'ADD1: ' + out.get(d, ('', ''))[1][:60]); continue
        m = json.load(open(p)); e = m.get('estado')
        if e == 'COMPLETE' and (m.get('addendum') != ADD2_SHA[:8] or not os.path.exists(CACHE + f'{d}_pob_add2.pkl.gz')): e = 'INVALIDO_ADD2'
        out[d] = ('COMPLETE', DET_ADD2) if e == 'COMPLETE' else (f'{e}_ADD2', m.get('error', '') or '')
    return out
def carga_pob(specs_keep=None, dias=None):
    """ADD1 (popdata.carga_pob, 35 dias) + dias ADD2 COMPLETE. Columna extra epoca_ts (epoca por timestamp; = epoca en los dias ADD1) y p5w (suelo de la ventana; NaN en ADD1)."""
    P, _ = _p.carga_pob(specs_keep, dias); est = estado_dias(); keep = SPEC_NAMES if specs_keep is None else list(specs_keep)
    cols = BASE + ['epoca_ts', 'p5w'] + [f'{a}_{s}' for s in keep for a in ('F5', 'bid', 'cat')]; parts = [P]
    for d in DIAS_ADD2:
        if est[d] != ('COMPLETE', DET_ADD2) or (dias is not None and d not in dias): continue
        X = pd.read_pickle(CACHE + f'{d}_pob_add2.pkl.gz', compression='gzip'); X = X[[c for c in cols if c in X.columns]].copy()
        for c in ('dia', 'coin', 'epoca', 'mid', 'lado_m', 'epoca_ts'): X[c] = X[c].astype(str)
        parts.append(X)
    P = pd.concat(parts, ignore_index=True) if len(parts) > 1 else P.copy()
    if 'epoca_ts' not in P.columns: P['epoca_ts'] = P.epoca
    P['epoca_ts'] = P.epoca_ts.where(P.epoca_ts.notna(), P.epoca).astype(str)
    if 'p5w' not in P.columns: P['p5w'] = np.nan
    for c in P.columns:
        if str(P[c].dtype) == 'float64' and c not in ('pnl', 'coste', 'q', 'acc', 'gana'): P[c] = P[c].astype(np.float32)
    return P, est
def resumen_cobertura(est):
    L, por = _p.resumen_cobertura(est); a2 = [d for d, v in est.items() if v == ('COMPLETE', DET_ADD2)]
    if a2: L.append(f"  de ellos por ADDENDUM2 {ADD2_SHA[:8]} (epoca por suelo medido; FAILED-C3 en ADD1, fuera de las celdas decisivas): " + ', '.join(a2))
    return L, por
