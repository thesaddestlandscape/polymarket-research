"""popdata.py -- carga de las caches de poblacion por dia del EXP-1 (salida de e2_dia.py). Solo lectura. Usado por e2_agrega, e5_regimen y e6_brecha."""
import os, sys, glob; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib1 import *
D_INI, D_FIN = '2026-10-09', '2026-11-14'                 # poblacion 09-Oct..14-Nov (08-Oct solo para el mapa k)
BASE = ['dia', 'coin', 'hora', 'fin', 'r_ex', 'r_rx', 'q', 'acc', 'gana', 'pnl', 'coste', 'epoca', 'mid', 'lado_m']
SPEC_NAMES = [s[0] for s in specs()] + ['o100', 'o250']
def dias_esperados(): return [d.strftime('%Y-%m-%d') for d in pd.date_range(D_INI, D_FIN)]
def estado_dias():
    """-> dict dia: (estado, detalle) leyendo los manifiestos pob_D.json; FALTA si no hay manifiesto."""
    out = {}
    for d in dias_esperados():
        p = CACHE + f'pob_{d}.json'
        if not os.path.exists(p): out[d] = ('FALTA', ''); continue
        m = json.load(open(p)); e = m.get('estado')
        if e == 'COMPLETE' and (m.get('addendum') != ADD_SHA[:8] or not os.path.exists(CACHE + f'{d}_pob.pkl.gz')): e = 'INVALIDO'
        out[d] = (e, m.get('error', '') or f"cob {m.get('cobertura_desenlace_coste')}")
    return out
def carga_pob(specs_keep=None, dias=None):
    """Concatena los pkl.gz COMPLETE. specs_keep: lista de nombres de spec (F5_/bid_/cat_) a conservar (None = todas). Devuelve (P, estado_dias)."""
    est = estado_dias(); keep = SPEC_NAMES if specs_keep is None else list(specs_keep); cols = BASE + [f'{a}_{s}' for s in keep for a in ('F5', 'bid', 'cat')]; parts = []
    for d, (e, _) in est.items():
        if e != 'COMPLETE' or (dias is not None and d not in dias): continue
        X = pd.read_pickle(CACHE + f'{d}_pob.pkl.gz', compression='gzip'); X = X[[c for c in cols if c in X.columns]].copy()
        for c in ('dia', 'coin', 'epoca', 'mid', 'lado_m'): X[c] = X[c].astype(str)
        parts.append(X)
    P = pd.concat(parts, ignore_index=True) if parts else pd.DataFrame(columns=cols)
    for c in P.columns:
        if str(P[c].dtype) == 'float64' and c not in ('pnl', 'coste', 'q', 'acc', 'gana'): P[c] = P[c].astype(np.float32)
    return P, est
def resumen_cobertura(est):
    por = {}
    for d, (e, det) in est.items(): por.setdefault(e, []).append(d)
    L = [f"Dias esperados {len(est)} ({D_INI}..{D_FIN}): " + ', '.join(f"{e} {len(v)}" for e, v in sorted(por.items()))]
    for e, v in sorted(por.items()):
        if e != 'COMPLETE': L.append(f"  {e}: " + ', '.join(f"{d}[{est[d][1][:80]}]" for d in v))
    return L, por
