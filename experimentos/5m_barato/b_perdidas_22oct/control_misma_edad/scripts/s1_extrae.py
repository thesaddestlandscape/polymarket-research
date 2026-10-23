#!/usr/bin/env python3
"""s1_extrae.py -- PREREG_S1 (sha 5f1aab59...). E (prints de la cinta en nivel top) y C (instantes control emparejados) con EXIT(u) a leads 150/300/500/1000 ms.
Reutiliza SOLO el parser del libro de cola_posicion/scripts/d1_l2_motor.carga (validado aparte en s0_sanidad.py). Salida: DL/control_misma_edad/s1_eventos.csv.gz"""
import sys, os, glob, hashlib, zlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(AQ, '..', 'prereg', 'PREREG_S1.md')
assert hashlib.sha256(open(P, 'rb').read()).hexdigest().startswith('5f1aab59408ec5e7')
sys.path.insert(0, os.path.join(AQ, '..', '..', 'cola_posicion', 'scripts'))
import d1_l2_motor as M
DL = '/root/polymarket-research-datalogs/control_misma_edad/'; os.makedirs(DL, exist_ok=True)
TAUS = (150, 300, 500, 1000)
def top_is(tp, L, q, t): return M.best(tp, L, t) == q
def exit_u(lvn, prn, L, q, u):
    s0 = M.S(lvn, L, q, u - 850)
    if s0 < 5: return 0, s0, 0
    c, _ = M.cons_between(prn, L, q, u - 850, u); s1 = M.S(lvn, L, q, u)
    return int((s0 - c - s1) >= 0.8 * s0), s0, 1
def fila(grp, lvn, prn, tp, act, mid, L, fin, dia, r, q, bd, a, pair):
    row = dict(grp=grp, act=act, mid=mid, L=L, fin=fin, dia=dia, r=int(r), q=q, banda=bd, T=fin - r / 1000, a=a, pair=pair)
    any_ok = False
    for tau in TAUS:
        u = r - tau; ok = 0; ex = 0; s0 = 0.0
        if top_is(tp, L, q, u):
            ex, s0, ok = exit_u(lvn, prn, L, q, u)
        row[f'ok{tau}'] = ok; row[f'ex{tau}'] = ex; row[f's{tau}'] = s0; any_ok |= bool(ok)
    return row, any_ok
def procesa(path):
    act, mid = os.path.basename(path)[:-3].split('_'); fin = M.FIN[(act, mid)]
    rng = np.random.default_rng(zlib.crc32(os.path.basename(path).encode()) ^ 20261023)
    lvn, prn, tp, ap = M.carga(path); dia = pd.Timestamp(fin - 1, unit='s').strftime('%Y-%m-%d'); out = []
    for (L, q), (rt, rs) in prn.items():
        bd = M.banda(q)
        if bd is None: continue
        for k, (r, a) in enumerate(zip(rt, rs)):
            T = fin - r / 1000
            if not (50 <= T <= 300): continue
            row, ok = fila('E', lvn, prn, tp, act, mid, L, fin, dia, r, q, bd, float(a), -1)
            if not row['ok300']: 
                if ok: out.append(row)   # elegible solo en otros taus
                continue
            out.append(row); kk = 0
            for _ in range(40):
                if kk >= 3: break
                t = int(r + rng.integers(-60000, 60001)); Tt = fin - t / 1000
                if abs(t - r) < 4000 or not (50 <= Tt <= 300): continue
                c, n = M.cons_between(prn, L, q, t - 2000, t + 3000)
                if n > 0: continue
                if not top_is(tp, L, q, t - 300): continue
                if M.S(lvn, L, q, t - 300 - 850) < 5: continue
                rc, _ = fila('C', lvn, prn, tp, act, mid, L, fin, dia, t, q, bd, float(a), int(r)); out.append(rc); kk += 1
    return out
if __name__ == '__main__':
    import multiprocessing as mp
    files = sorted(glob.glob(M.MK + '*.gz')); print('ficheros', len(files), flush=True)
    R = []
    with mp.Pool(3) as pool:
        for i, o in enumerate(pool.imap_unordered(procesa, files, chunksize=8)):
            R += o
            if i % 200 == 0: print(i, len(R), flush=True)
    pd.DataFrame(R).to_csv(DL + 's1_eventos.csv.gz', index=False); print('FIN', len(R))
