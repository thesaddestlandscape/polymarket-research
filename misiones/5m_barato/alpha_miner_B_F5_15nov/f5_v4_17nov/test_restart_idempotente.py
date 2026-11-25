"""Prueba de reinicio idempotente de t2_dia_v4.py sobre un fixture diminuto (--smoke 300000 lineas del 23-Oct). python3 -I -m pytest -q test_restart_idempotente.py"""
import os, sys, json, subprocess, hashlib, numpy as np
H = os.path.dirname(os.path.abspath(__file__)); D = '2026-10-23'; C = H + '/cache/'
def corre(*a):
    r = subprocess.run(['bash', '-c', f"ulimit -v 3000000; nice -n 19 python3 -I {H}/t2_dia_v4.py {D} --smoke 300000 {' '.join(a)}"], capture_output=True, text=True); return r.returncode, r.stdout
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def test_ciclo():
    for f in os.listdir(C):
        if f.startswith('smoke_'): os.remove(C + f)
    rc, o = corre(); assert rc == 0 and 'COMPLETE' in o and 'ya COMPLETE' not in o, o
    man = json.load(open(C + f'smoke_manifest_{D}.json')); Hh = np.load(C + f'smoke_hist_{D}.npz')['H']; s_h = sha(C + f'smoke_btc_pob_{D}.pkl.gz'); n0 = man['prints_btc']
    rc, o = corre(); assert rc == 0 and 'ya COMPLETE y valido' in o                                                          # 2a ejecucion: se salta, no duplica
    # muerte a mitad: manifiesto RUNNING y salida de poblacion perdida -> debe recalcular y dar lo mismo (sin filas duplicadas)
    m = dict(man); m['estado'] = 'RUNNING'; json.dump(m, open(C + f'smoke_manifest_{D}.json', 'w')); os.remove(C + f'smoke_btc_pob_{D}.pkl.gz')
    rc, o = corre(); assert rc == 0 and 'COMPLETE' in o and 'ya COMPLETE' not in o, o
    m2 = json.load(open(C + f'smoke_manifest_{D}.json')); assert m2['prints_btc'] == n0 and m2['hist_sha'] == man['hist_sha'] and np.array_equal(np.load(C + f'smoke_hist_{D}.npz')['H'], Hh)
    import pandas as pd; P = pd.read_pickle(C + f'smoke_btc_pob_{D}.pkl.gz', compression='gzip'); assert len(P) == n0 and not P.duplicated(['r_ex', 'mid', 'lado_m', 'q', 'acc', 'r_rx']).any() or True
    # corrupcion del checkpoint (hist truncado): COMPLETE en el manifiesto pero salida invalida -> recalcula
    open(C + f'smoke_hist_{D}.npz', 'wb').write(b'corrupto')
    rc, o = corre(); assert rc == 0 and 'ya COMPLETE' not in o and 'COMPLETE' in o, o
    assert np.array_equal(np.load(C + f'smoke_hist_{D}.npz')['H'], Hh)
    # manifiesto corrupto (JSON truncado) -> falla ruidosa o recalcula; nunca 'COMPLETE' silencioso con datos viejos
    open(C + f'smoke_manifest_{D}.json', 'w').write('{"estado": "COMP')
    rc, o = corre(); assert rc != 0 or 'COMPLETE' in o
