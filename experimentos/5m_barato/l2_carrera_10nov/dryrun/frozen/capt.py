#!/usr/bin/env python3
"""Capturabilidad propia de A_R1ws. Solo lectura de datalogs; escribe en out/. Uso: python3 -I capt.py policy|real DIA [DIA...]
Contrato: CONTRATO_MEDICION.json (congelado ANTES de ver resultados). Libro top-of-book del registro ms (sa_ms/ms_D.npz), recepcion."""
import sys, json, glob, numpy as np, pandas as pd, datetime as dt
DL = '/root/polymarket-research-datalogs/'; OUT = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/capturabilidad_A_R1ws/out/'
LAT_POST = 68; LAT_CANC = 60; GRID = 500; EPS = 1e-6
BAND = (0.10, 0.30); TMIN = 61; SIZE = 5.0; GATE = dict(lvl=0.03, vol=26.0, hora=4)
REB = 0.2 * 0.07   # rebate maker = 20 % de la comision 0,07*p*(1-p) del tomador
GM = {}
for f in glob.glob(DL + 'sa_r1/gmap_*.json'):
    for s, v in json.load(open(f)).items():
        if v.get('des') in ('YES', 'NO'): GM[str(v['id'])] = v['des']

class Day:
    def __init__(s, d):
        z = np.load(DL + f'sa_ms/ms_{d}.npz', allow_pickle=True)
        s.toks = list(z['tokens']); t0 = int(z['t0'])
        m = pd.DataFrame(z['tmap'], columns=['act', 'marco', 'mid', 'fin', 'lado'])
        s.fin = m.fin.map(lambda x: int(pd.Timestamp(x).timestamp())).values; s.act = m.act.values; s.marco = m.marco.values; s.mid = m.mid.values; s.lado = m.lado.values
        s.tokidx = {t: i for i, t in enumerate(s.toks)}
        s.t5 = {(s.mid[i], s.lado[i]): i for i in range(len(s.toks)) if s.marco[i] == '5min'}
        s.t15 = {(s.act[i], s.fin[i], s.lado[i]): i for i in range(len(s.toks)) if s.marco[i] == '15min'}
        n = len(s.toks); qk = z['q_k']; s.qb = np.searchsorted(qk, np.arange(n + 1)); s.qt = z['q_t'] + t0
        s.v0 = z['q_v0']; s.v1 = z['q_v1']; s.v2 = z['q_v2']; s.v3 = z['q_v3']
        tk = z['t_k']; tt = z['t_t'] + t0; o = np.lexsort((tt, tk)); s.tk = tk[o]; s.tt = tt[o]; s.tp = z['t_pr'][o]; s.tsd = z['t_sd'][o]; s.tsz = z['t_sz'][o]
        s.tb = np.searchsorted(s.tk, np.arange(n + 1)); s.cs = np.cumsum(s.tsz.astype(np.float64))
    def comp(s, k):
        return s.t5.get((s.mid[k], 'NO' if s.lado[k] == 'YES' else 'YES'))
    def book(s, k, t):   # ultimo quote <= t -> (bid, ask, bidsz, asksz) o None
        a, b = s.qb[k], s.qb[k + 1]
        if b <= a: return None
        j = np.searchsorted(s.qt[a:b], t, side='right') - 1
        return None if j < 0 else (float(s.v0[a + j]), float(s.v1[a + j]), float(s.v2[a + j]), float(s.v3[a + j]))
    def vol30(s, k5, t):  # acciones de ambos tokens del mercado 5m en (t-30s, t]
        v = 0.0
        for k in (k5, s.comp(k5)):
            if k is None: continue
            a, b = s.tb[k], s.tb[k + 1]; tt = s.tt[a:b]
            i1 = np.searchsorted(tt, t, side='right'); i0 = np.searchsorted(tt, t - 30000, side='right')
            if i1 > i0: v += float(s.cs[a + i1 - 1] - (s.cs[a + i0 - 1] if a + i0 - 1 >= a else 0.0))
        return v
    def b15(s, k5, t):
        f15 = int(np.ceil(s.fin[k5] / 900.0) * 900); k = s.t15.get((s.act[k5], f15, s.lado[k5]))
        if k is None: return np.nan
        bk = s.book(k, t); return np.nan if bk is None else bk[0]
    def gate_ok(s, k5, p, t):
        b = s.b15(k5, t)
        if not np.isfinite(b): return False, np.nan, np.nan
        v = s.vol30(k5, t); h = dt.datetime.fromtimestamp(t / 1000, dt.timezone.utc).hour
        return ((b - p) <= GATE['lvl'] + EPS) and v >= GATE['vol'] and h >= GATE['hora'], b - p, v
    def prints(s, kY, p, t0_, t1_):
        """prints que ATRAVIESAN/tocan el nivel p del bid de kY en (t0_, t1_] -> lista (t, q, sz) ordenada; dedupe espejo 100 ms"""
        out = []
        a, b = s.tb[kY], s.tb[kY + 1]; tt = s.tt[a:b]; i0 = np.searchsorted(tt, t0_, side='right'); i1 = np.searchsorted(tt, t1_, side='right')
        for j in range(a + i0, a + i1):
            if s.tsd[j] == 0 and s.tp[j] <= p + 0.0049: out.append((int(s.tt[j]), round(float(s.tp[j]), 2), float(s.tsz[j]), 0))
        kX = s.comp(kY)
        if kX is not None:
            a, b = s.tb[kX], s.tb[kX + 1]; tt = s.tt[a:b]; i0 = np.searchsorted(tt, t0_, side='right'); i1 = np.searchsorted(tt, t1_, side='right')
            for j in range(a + i0, a + i1):
                q = round(1 - float(s.tp[j]), 2)
                if s.tsd[j] == 1 and q <= p + 0.0049: out.append((int(s.tt[j]), q, float(s.tsz[j]), 1))
        out.sort(); res = []
        for r in out:
            if res and r[3] != res[-1][3] and abs(r[0] - res[-1][0]) <= 100 and abs(r[1] - res[-1][1]) < 1e-9 and abs(r[2] - res[-1][2]) < 1e-3: continue
            if res and r[3] == res[-1][3] and r[0] == res[-1][0] and r[1] == res[-1][1] and r[2] == res[-1][2] and False: continue
            res.append(r)
        return res
    def fill(s, kY, p, t_arr, t_end, q0s, rem=SIZE):
        """q0s dict variante->cola por delante. Devuelve dict variante->(qty, t_primer)"""
        pr = s.prints(kY, p, t_arr, t_end); res = {}
        for v, q0 in q0s.items():
            cum = 0.0; qty = 0.0; tf = None
            for (t, q, sz, _) in pr:
                if q < p - EPS: qty = rem; tf = t if tf is None else tf; break
                cum += sz
                if cum > q0 + 1e-9:
                    qty = min(rem, cum - q0); tf = t if tf is None else tf
                    if qty >= rem - 1e-9: break
            res[v] = (qty, tf)
        return res
    def q0_variants(s, kY, p, t_arr, cola=None):
        bk = s.book(kY, t_arr); kX = s.comp(kY)
        if cola is None:
            if bk is None: return None
            if bk[0] > p + EPS: return None        # cola desconocida (nivel por debajo del top)
            base = bk[2] if abs(bk[0] - p) < EPS else 0.0
        else: base = cola
        xa = 0.0
        if kX is not None:
            bx = s.book(kX, t_arr)
            if bx is not None and abs(bx[1] - (1 - p)) < 0.0049: xa = bx[3]
        return {'C': base + xa, 'M': base, 'O': 0.0}

def outcome(D, k):
    des = GM.get(str(D.mid[k]))
    return None if des is None else float(des == D.lado[k])

def policy(d):
    D = Day(d); rows = []
    ks = [k for k in range(len(D.toks)) if D.marco[k] == '5min' and D.act[k] in ('ETH', 'SOL', 'XRP')]
    miss = {}
    for k in ks:
        fin = int(D.fin[k]); g = outcome(D, k)
        if g is None: miss['sin_desenlace'] = miss.get('sin_desenlace', 0) + 1; continue
        if D.comp(k) is None: miss['sin_comp'] = miss.get('sin_comp', 0) + 1; continue
        a, b = D.qb[k], D.qb[k + 1]
        if b - a < 2: miss['sin_libro'] = miss.get('sin_libro', 0) + 1; continue
        grid = np.arange((fin - 300) * 1000, (fin - TMIN) * 1000 + 1, GRID)
        j = np.searchsorted(D.qt[a:b], grid, side='right') - 1
        okj = j >= 0; jj = np.where(okj, j, 0)
        bid = np.where(okj, D.v0[a + jj], np.nan); ask = np.where(okj, D.v1[a + jj], np.nan)
        for pol in ('G', 'U'):                   # G = con gate A_R1ws, U = sin gate
            live = False; filled = {v: 0.0 for v in 'CMO'}; nseg = 0; seg = None
            def close(t_end_eff):
                nonlocal live, seg
                p, t_arr, q0s = seg; live = False
                for v in 'CMO':
                    rem = SIZE - filled[v]
                    if rem <= 1e-9: continue
                    r = D.fill(k, p, t_arr, t_end_eff, {v: q0s[v]}, rem)[v]
                    if r[0] > 0:
                        tf = r[1]; gk, lv, vo = D.gate_ok(k, p, tf)
                        rows.append(dict(dia=d, pol=pol, var=v, mkt=int(D.mid[k]), act=D.act[k], lado=D.lado[k], fin=fin, p=p, q=r[0], t_fill=tf, T=fin - tf / 1000, t_arr=t_arr, q0=q0s[v],
                                         gana=g, hora=dt.datetime.fromtimestamp(tf / 1000, dt.timezone.utc).hour, gate_fill=gk, lvl15=lv, vol30=vo, seg=nseg))
                        filled[v] += r[0]
            for i in range(len(grid)):
                t = int(grid[i]); done = all(filled[v] >= SIZE - 1e-9 for v in 'CMO')
                if live:
                    pp = seg[0]
                    if pol == 'G':
                        okg, _, _ = D.gate_ok(k, pp, t)
                        if not okg: close(t + LAT_CANC)
                elif not done and np.isfinite(bid[i]) and np.isfinite(ask[i]) and bid[i] < ask[i] and BAND[0] - EPS <= bid[i] <= BAND[1] + EPS:
                    p = round(float(bid[i]), 2)
                    if pol == 'G' and not D.gate_ok(k, p, t)[0]: continue
                    t_arr = t + LAT_POST; q0s = D.q0_variants(k, p, t_arr)
                    if q0s is None: miss['cola_desconocida'] = miss.get('cola_desconocida', 0) + 1; continue
                    bk = D.book(k, t_arr)
                    if bk is not None and bk[1] <= p + EPS: miss['seria_taker'] = miss.get('seria_taker', 0) + 1; continue
                    live = True; nseg += 1; seg = (p, t_arr, q0s)
                    rows.append(dict(dia=d, pol=pol, var='post', mkt=int(D.mid[k]), act=D.act[k], lado=D.lado[k], fin=fin, p=p, q=0.0, t_fill=t, T=fin - t / 1000, t_arr=t_arr, q0=q0s['C'], gana=g, hora=-1, gate_fill=False, lvl15=np.nan, vol30=np.nan, seg=nseg))
            if live: close((fin - TMIN) * 1000 + LAT_CANC)
    df = pd.DataFrame(rows); df.to_csv(OUT + f'policy_{d}.csv.gz', index=False)
    json.dump(dict(dia=d, tokens=len(ks), miss=miss, posts=int((df['var'] == 'post').sum()) if len(df) else 0), open(OUT + f'policy_{d}.cov.json', 'w'))
    print(d, 'tokens', len(ks), miss, 'filas', len(df), flush=True)

def real(d):
    """B real (ordenes_b.csv, 20-23 Oct): calibracion del relleno virtual con cola real + clasificacion A_R1ws en t_ini"""
    D = Day(d); O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv'); O = O[O.dia == d]; rows = []
    for r in O.itertuples():
        k = D.tokidx.get(str(r.tok))
        if k is None or D.marco[k] != '5min': continue
        ti = int(r.t_ini * 1000); te = int(r.t_fin * 1000); cola = None if not np.isfinite(r.cola) else float(r.cola)
        if cola is None or D.comp(k) is None: continue
        q0s = D.q0_variants(k, round(float(r.precio), 2), ti, cola=cola)
        f = D.fill(k, round(float(r.precio), 2), ti, te, q0s, rem=float(r.size))
        gk, lv, vo = D.gate_ok(k, float(r.precio), ti)
        rows.append(dict(dia=d, oid=r.oid, act=D.act[k], precio=r.precio, size=r.size, cola=cola, real_q=r.acc_llena, coste=r.coste, pnl=r.pnl, resuelto=r.resuelto, T=r.T, gana=r.gana_lado,
                         gateAR=gk, lvl15=lv, vol30=vo, hora=dt.datetime.fromtimestamp(ti / 1000, dt.timezone.utc).hour, **{('f' + v): f[v][0] for v in 'CMO'}))
    pd.DataFrame(rows).to_csv(OUT + f'real_{d}.csv.gz', index=False); print(d, 'real orders', len(rows), flush=True)

if __name__ == '__main__':
    mode = sys.argv[1]
    for d in sys.argv[2:]: (policy if mode == 'policy' else real)(d)
