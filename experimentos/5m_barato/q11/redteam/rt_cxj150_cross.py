#!/usr/bin/env python3
"""CXJ150 bajo BASE y CROSS (ADDENDUM4/PREREG_Q11_THRU1_FWD: C3 de CXJ150; rt_sim.py no modela cancelacion por salto). DEV, solo lectura, 0 ordenes.
NO modifica rt_sim.py ni passT.py: lee su codigo (sha registrado comprobado) y ejecuta (a) el prefijo de rt_sim.py hasta la definicion de FV (cinta
re-sincronizada, DayEng, fill_v con BASE/CROSS, cross_events) y (b) el bloque de passT.py que construye XS/bnr/JUMP/first_after. Politica CXJ150 = copia literal de
passT.py: base & ~ja3 (sin salto adverso >=3 bps en 1 s en (t-3300, t-300]) y cancelacion de la orden viva en el primer salto adverso >= t_arr + 150 ms
(t_end = salto + 150). CROSS = fill_v('CROSS') sobre ese [t_arr, t_end]: si el ask propio toca L (o el bid complementario >= 1-L) antes del relleno BASE
y antes de salto + 150, el relleno cuenta. Dos rellenos independientes (BASE, CROSS) con su propio `rem` de 5 acc, mismos segmentos.
Uso (argumentos validados, YYYY-MM-DD): nice -n 19 ionice -c3 python3 -I rt_cxj150_cross.py DIA -> out_cxj150/RX_<D>.pkl (cols de rt_sim: pol='CXJ150', fv, dia, act, lado, fin, k, L, q, tf, gana, seg, t_dec, cost, pnl)
Chequeo de equivalencia: el BASE de este script debe igualar el CXJ150 de toxicidad_thru1/out/RT_<D>.pkl (python3 -I rt_cxj150_cross.py verificar DIA)."""
import sys, os, hashlib, json, time
import numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUTX = H + 'out_cxj150/'
RT = H + 'rt_sim.py'; PT = H + '../toxicidad_thru1/passT.py'
SHA_RT = '86b14afbf91b308ab6185e0060427047fc644a6a0ac33813127627ef507f652b'; SHA_PT = 'a8b9d7a0158fd0b0cf47582c499d6c1cc870269310c8ef4481482733d1c64038'
EXIT_RT = "if os.path.exists(OUT + f'RT_{d}.pkl'): print('ya', d); sys.exit(0)\n"
MARK_RT = "FV = ('BASE', 'STRICT', 'OPT', 'CROSS', 'THIN')\n"
INI_PT = "sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/q11/barrido_multi'); import bfeat\n"
FIN_PT = "def run_var("
COLS = ['pol', 'fv', 'dia', 'act', 'lado', 'fin', 'k', 'L', 'q', 'tf', 'gana', 'seg', 't_dec', 'cost', 'pnl']
def fuentes():
    a = open(RT).read(); b = open(PT).read()
    assert hashlib.sha256(a.encode()).hexdigest() == SHA_RT, 'rt_sim.py distinto del registrado'
    assert hashlib.sha256(b.encode()).hexdigest() == SHA_PT, 'passT.py distinto del registrado'
    assert a.count(EXIT_RT) == 1 and a.count(MARK_RT) == 1 and b.count(INI_PT) == 1 and b.count(FIN_PT) == 1, 'marcas no encontradas'
    pre = a[:a.index(MARK_RT)].replace(EXIT_RT, ''); blq = b[b.index(INI_PT):b.index(FIN_PT)]
    return pre, blq
def correr(d):
    T0 = time.time(); os.makedirs(OUTX, exist_ok=True)
    if os.path.exists(OUTX + f'RX_{d}.pkl'): print('ya', d); return
    pre, blq = fuentes(); sys.argv = ['rt_sim.py', d]
    ns = {'__file__': RT, '__name__': '__main__'}; exec(compile(pre, 'rt_sim_prefijo', 'exec'), ns)
    exec(compile(blq, 'passT_bloque_binance', 'exec'), ns)
    G, E, D, ks, FE, fill_v, first_after, JUMP = (ns[x] for x in ('G', 'E', 'D', 'ks', 'FE', 'fill_v', 'first_after', 'JUMP'))
    FVS = ('BASE', 'CROSS'); FILLS = []; NSEG = 0
    for k in ks:
        g, bid, ask, b15, vol, hora = FE[k]; fin = int(D.fin[k]); gana = G.capt_outcome(E, k); coin = D.act[k]; lado = D.lado[k]
        tq = g - 300
        J = JUMP.get(coin, {'up': np.array([], np.int64), 'dn': np.array([], np.int64)}); jadv = J['dn'] if lado == 'YES' else J['up']
        ja3 = (np.searchsorted(jadv, tq, side='right') - np.searchsorted(jadv, tq - 3000, side='right')) > 0   # = passT.py
        for L in G.LEVELS:
            Gm = G.gate_vec('G', L, b15, vol, hora); base = Gm & np.isfinite(ask) & (ask > L + G.EPS); can = base & ~ja3   # = passT.py CXJ{l}: base & ~ja3
            n = len(g); hard = (fin - G.TMIN) * 1000 + 60; falsos = np.where(~Gm)[0]; i = 0; rem = {f: 5.0 for f in FVS}; si = 0
            while i < n and any(rem[f] > 1e-9 for f in FVS):   # = passT.run_var (segmentacion y cancelacion por salto + 150 ms)
                if not can[i]: i += 1; continue
                t = int(g[i]); t_arr = t + G.LAT_POST; pos = np.searchsorted(falsos, i + 1); j = falsos[pos] if pos < len(falsos) else n
                t_end = min(int(g[j]) + 60 if j < n else hard, hard)
                if t_end > t_arr:
                    tb = first_after(jadv, t_arr, t_end)
                    if tb is not None and tb + 150 < t_end: t_end = max(tb + 150, t_arr)
                if t_end > t_arr:
                    NSEG += 1
                    for f in FVS:
                        if rem[f] <= 1e-9: continue
                        q, tf = fill_v(k, L, t_arr, t_end, rem[f], f)
                        if q > 1e-9: rem[f] -= q; FILLS.append(('CXJ150', f, d, coin, lado, fin, k, L, float(q), int(tf), gana, si, t))
                    si += 1
                i = max(i + 1, int(np.searchsorted(g, t_end)))
    R = pd.DataFrame(FILLS, columns=COLS[:13]); R['cost'] = R.q * R.L; R['pnl'] = R.q * (R.gana - R.L) + R.q * 0.2 * 0.07 * R.L * (1 - R.L)
    tmp = OUTX + f'RX_{d}.pkl.tmp'; R.to_pickle(tmp); os.replace(tmp, OUTX + f'RX_{d}.pkl')
    print('ok', d, 'segmentos', NSEG, {f: (len(x), round(float(x.pnl.sum()), 2)) for f, x in R.groupby('fv', sort=False)}, round(time.time() - T0, 1), 's', flush=True)
def verificar(d):
    """BASE de RX_D == CXJ150 de passT (mismo numero de rellenos, mismos (k, L, tf, q) y pnl)."""
    X = pd.read_pickle(OUTX + f'RX_{d}.pkl'); P = pd.read_pickle(H + f'../toxicidad_thru1/out/RT_{d}.pkl'); P = P[P['var'] == 'CXJ150']; B = X[X.fv == 'BASE']
    kk = lambda x: sorted(zip(x.k.astype(int), x.L.round(2), x.tf.astype(int), x.q.round(6)))
    ok = kk(B) == kk(P); print('verificar', d, 'n_BASE', len(B), 'n_passT', len(P), 'pnl', round(float(B.pnl.sum()), 4), round(float(P.pnl.sum()), 4), 'IGUALES' if ok else 'DISTINTOS'); return ok
def fecha_ok(x):
    """YYYY-MM-DD real (el dia entra en rutas de fichero: nada de patrones ni '..')."""
    import re, datetime
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', x or ''): return False
    try: datetime.date.fromisoformat(x); return True
    except ValueError: return False
USO = 'uso: rt_cxj150_cross.py YYYY-MM-DD | verificar YYYY-MM-DD | test'
if __name__ == '__main__':
    a = sys.argv[1:]
    if len(a) == 1 and a[0] == 'test': pre, blq = fuentes(); compile(pre, 'x', 'exec'); compile(blq, 'y', 'exec'); print('fuentes OK (sha y marcas)')
    elif len(a) == 2 and a[0] == 'verificar' and fecha_ok(a[1]): sys.exit(0 if verificar(a[1]) else 3)
    elif len(a) == 1 and fecha_ok(a[0]): correr(a[0])
    else: print(USO, file=sys.stderr); sys.exit(2)
