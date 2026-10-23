#!/usr/bin/env python3
"""r3_esc_sim.py DIA... -- R3 capacidad/escalado (22-Oct, risk-economics). SOLO LECTURA de salida/datos/ms_D.npz.
Reutiliza el simulador CONS de E1 (seleccion_adversa_plan/scripts/e1_sim.py: puja tipo B, ETH k2 / SOL,XRP k1, banda 0,11-0,30,
T 298-65, asentado 1,5 s, relleno = print que ATRAVIESA la puja con la puja viva 50 ms antes) y anade, por mercado:
 - flags R2/R3 (reglas_congeladas.json v2, parametros de r3_regla.py) en la rejilla de 100 ms: bid15 mismo lado - puja <= 0,03 (15m no cruzado),
   vol30 = acciones casadas en los dos tokens del 5m en (max(t-30 s, apertura), t] por RECEPCION, hora UTC >= 4;
 - relleno de 3 politicas: BASE (1er print que atraviesa), R2 y R3 (1er print que atraviesa con la regla verdadera en ese tick = la politica cancela
   cuando la regla es falsa y vuelve a cotizar cuando es verdadera; sin asentado extra al volver: leve optimismo);
 - volumen que atraviesa la puja en [r, r+1 s] y [r, r+5 s] (V1, V5) = acciones que habrian llenado una puja MAYOR (relleno(K) = min(K, V)).
Salida r3_escalado/datos/esc_D.csv.gz (una fila por mercado) y b_real_r3.csv (rellenos de B real con los mismos rasgos en su print)."""
import sys, os, math
import numpy as np, pandas as pd
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'salida', 'scripts')); sys.path.insert(0, os.path.join(AQUI, '..', 'seleccion_adversa_plan', 'scripts'))
from msdata import Dia, SYM, DD
import e1_sim as E   # (comprueba el hash del preregistro E1 al importar; solo usamos funciones)
OUT = os.path.join(AQUI, 'datos'); os.makedirs(OUT, exist_ok=True)
R2_MAX = 0.030; VOL30_MIN = 26.0; HORA_MIN = 4
BLO, BHI = float(os.environ.get('R3_BAND_LO', '0.11')), float(os.environ.get('R3_BAND_HI', '0.30'))   # banda del bid (B: (0,11, 0,30])
PREF = os.environ.get('R3_PREF', 'esc')

def obj_raw(bid, ask, k):
    """= e1_sim.obj_raw con banda parametrizable (exploratorio fuera de 0,11-0,30)"""
    b = np.round(np.nan_to_num(bid, nan=0) * 1000).astype(int); a = np.round(np.nan_to_num(ask, nan=9) * 1000).astype(int)
    o = np.where(b % 10 == 0, b - k * 10, (b // 10 - (k - 1)) * 10)
    band = np.isfinite(bid) & (bid > BLO + 1e-9) & (bid <= BHI + 1e-9)
    ok = band & (o >= int(round((BLO - 0.01) * 1000))) & (o <= int(round(BHI * 1000))) & (o < b) & (o < a)
    return np.where(ok, o / 1000.0, np.nan)

def vol30_at(tt, cs, ini_ms, t):
    """suma de tamanos en (max(t-30000, ini), t]"""
    lo = np.maximum(t - 30000, ini_ms)
    return cs[np.searchsorted(tt, t, 'right')] - cs[np.searchsorted(tt, lo, 'right')]

def trades_mkt(D, ks, t0, t1):
    T = []; S = []
    for k in ks:
        if k is None: continue
        r, v = D.trades(k, t0, t1); T.append(r); S.append(v[:, 2].astype(float))
    if not T: return np.zeros(0, np.int64), np.zeros(1)
    t = np.concatenate(T); o = np.argsort(t, kind='stable'); t = t[o]; s = np.concatenate(S)[o]
    return t, np.r_[0.0, np.cumsum(s)]

def crossing(D, kown, kopp, t0, t1, o):
    """(tiempos, tamanos) de prints que atraviesan una puja a precio o: SELL propio < o o BUY opuesto > 1-o"""
    R = []; Z = []
    for k, own in ((kown, True), (kopp, False)):
        r, v = D.trades(k, t0, t1)
        if len(r) == 0: continue
        m = ((v[:, 1] == 0) & (v[:, 0] < o - 1e-6)) if own else ((v[:, 1] == 1) & (v[:, 0] > 1 - o + 1e-6))
        R.append(r[m]); Z.append(v[m, 2].astype(float))
    if not R: return np.zeros(0, np.int64), np.zeros(0)
    t = np.concatenate(R); oo = np.argsort(t, kind='stable'); return t[oo], np.concatenate(Z)[oo]

def day(d):
    D = Dia(d); rows = []; nmiss = 0; mk = {}
    for i, (act, marco, mid, fin, lado) in enumerate(D.tmap):
        if str(marco) != '5min' or str(act) not in SYM: continue
        fe = int(pd.Timestamp(str(fin)).timestamp()); mk.setdefault((str(act), fe, str(mid)), {})[str(lado)] = i
    for (act, fe, mid), dd in sorted(mk.items(), key=lambda x: x[0][1]):
        if 'YES' not in dd or 'NO' not in dd: continue
        w = E.des.get(mid)
        g = (fe * 1000 - np.arange(E.T_HI * 1000, E.T_LO * 1000 - 1, -E.STEP)).astype(np.int64)
        by, ay, lcy = E.tops(D, dd['YES'], g); bn, an, lcn = E.tops(D, dd['NO'], g)
        def band(b): return np.isfinite(b) & (b > BLO + 1e-9) & (b <= BHI + 1e-9)
        cy, cn = band(by), band(bn)
        if not (cy | cn).any(): continue
        if w is None: nmiss += 1; continue
        f0 = int(np.argmax(cy | cn)); yes = bool(cy[f0])
        bid, ask, lc = (by, ay, lcy) if yes else (bn, an, lcn)
        kk = 2 if act == 'ETH' else 1; raw = obj_raw(bid, ask, kk)
        O = np.full(len(g), np.nan); cur = np.nan
        for i in range(f0, len(g)):
            if np.isfinite(lc[i]) and g[i] - lc[i] >= E.SETTLE: cur = raw[i]
            O[i] = cur
        if not np.isfinite(O).any(): continue
        kown = dd['YES'] if yes else dd['NO']; kopp = dd['NO'] if yes else dd['YES']
        f15 = int(math.ceil(fe / 900.0) * 900); k15 = D.tok(act, '15min', f15, 'YES' if yes else 'NO')
        if k15 is not None:
            b15, a15, _ = E.tops(D, k15, g)
        else:
            b15 = a15 = np.full(len(g), np.nan)
        ini_ms = (fe - 300) * 1000
        tt, cs = trades_mkt(D, (kown, kopp), ini_ms - 1000, int(g[-1]) + 1)
        v30 = vol30_at(tt, cs, ini_ms, g)
        hora = ((g // 1000) % 86400) // 3600
        okq = np.isfinite(O) & np.isfinite(b15) & ~(np.isfinite(a15) & (b15 >= a15 - 1e-9))
        lvl = np.where(okq, b15 - O, np.nan)
        r2 = okq & (np.round(np.nan_to_num(lvl, nan=9) * 1000) <= 30)
        r3 = r2 & (v30 >= VOL30_MIN) & (hora >= HORA_MIN)
        t0, t1 = int(g[0]), int(g[-1] + E.STEP)
        # candidatos de relleno (mismo criterio que e1_sim)
        cr = []; cp = []; cg = []
        for k, own in ((kown, True), (kopp, False)):
            r, v = D.trades(k, t0, t1 + E.LAG_VIVA)
            for rr, (pr, sd, sz) in zip(r, v):
                gi = int((rr - E.LAG_VIVA - t0) // E.STEP)
                if gi < 0 or gi >= len(g): continue
                o = O[gi]
                if not np.isfinite(o): continue
                if (own and sd == 0 and pr < o - 1e-6) or ((not own) and sd == 1 and pr > 1 - o + 1e-6): cr.append(int(rr)); cp.append(o); cg.append(gi)
        oo = np.argsort(cr, kind='stable'); cr = np.array(cr, np.int64)[oo]; cp = np.array(cp)[oo]; cg = np.array(cg, np.int64)[oo]
        gana = int((w == 'YES') == yes)
        valid = np.isfinite(O)
        row = dict(dia=d, act=act, mid=mid, fin=fe, yes=int(yes), gana=gana, n_cand=len(cr), hora0=int(hora[f0]),
                   g_valid=int(valid.sum()), g_r2=int((r2 & valid).sum()), g_r3=int((r3 & valid).sum()), g_has15=int((okq & valid).sum()),
                   obj_med=float(np.nanmedian(O)))
        for pol, fl in (('BASE', None), ('R2', r2), ('R3', r3)):
            idx = -1
            for j in range(len(cr)):
                if fl is None or fl[cg[j]]: idx = j; break
            if idx < 0:
                row.update({f'{pol}_fill': 0, f'{pol}_obj': np.nan, f'{pol}_r': -1, f'{pol}_V1': np.nan, f'{pol}_V5': np.nan}); continue
            o, r = float(cp[idx]), int(cr[idx]); xt, xz = crossing(D, kown, kopp, r - 1, r + 5000, o)  # r-1: D.trades excluye t0 (searchsorted right)
            row.update({f'{pol}_fill': 1, f'{pol}_obj': o, f'{pol}_r': r, f'{pol}_V1': float(xz[xt <= r + 1000].sum()), f'{pol}_V5': float(xz.sum())})
            if pol == 'BASE':
                gi = cg[idx]; row.update(dict(b_lvl15=float(lvl[gi]), b_vol30=float(v30[gi]), b_hora=int(hora[gi]), b_r2=int(r2[gi]), b_r3=int(r3[gi]),
                                              b_has15=int(okq[gi]), b_T=float((fe * 1000 - r) / 1000)))
        rows.append(row)
    df = pd.DataFrame(rows); of = os.path.join(OUT, f'{PREF}_{d}.csv.gz'); df.to_csv(of, index=False)
    print(d, 'mercados', len(df), 'sin desenlace (missing)', nmiss, '->', of, flush=True)

def b_real():
    """rellenos de B real (salida/datos/unidades_b.csv) con print de relleno en el WS: flags R2/R3 a print-100 ms y V1/V5 del barrido"""
    U = pd.read_csv(os.path.join(DD, 'unidades_b.csv')); U = U[U.t_det.notna()]; rows = []
    for d in sorted(U.dia.unique()):
        D = Dia(d)
        for u in U[U.dia == d].itertuples():
            fin5 = int(u.mercado.split('-')[-1]) + 300; lado = 'YES' if u.outcome == 'Up' else 'NO'
            own = D.tok(u.coin, '5min', fin5, lado); opp = D.tok(u.coin, '5min', fin5, 'NO' if lado == 'YES' else 'YES')
            td = int(u.t_det * 1000); pr = None
            for k, isown in ((own, True), (opp, False)):
                if k is None: continue
                r, v = D.trades(k, td - 5000, td)
                for rr, (p, sd, sz) in zip(r, v):
                    if (isown and sd == 0 and p <= u.p_fill + 1e-6) or ((not isown) and sd == 1 and p >= 1 - u.p_fill - 1e-6):
                        pr = int(rr) if pr is None else min(pr, int(rr))
            base = dict(mercado=u.mercado, dia=d, coin=u.coin, acc=u.acc, coste=u.coste, pnl=u.payout - u.coste, gana=u.gana, p_fill=u.p_fill, T_det=u.T_det)
            if pr is None or own is None: rows.append({**base, 'print': 0}); continue
            t = pr - 100; f15 = int(math.ceil(fin5 / 900.0) * 900); k15 = D.tok(u.coin, '15min', f15, lado)
            q = D.top(k15, t) if k15 is not None else None
            ok15 = q is not None and q[0] == q[0] and q[0] > 0 and not (q[1] == q[1] and q[0] >= q[1] - 1e-9)
            lvl = (q[0] - u.p_fill) if ok15 else np.nan
            ini = (fin5 - 300) * 1000; tt, cs = trades_mkt(D, (own, opp), ini - 1000, t + 1)
            v30 = float(vol30_at(tt, cs, ini, np.array([t]))[0]); hora = int((t // 1000) % 86400 // 3600)
            r2 = int(ok15 and round(lvl * 1000) <= 30); r3 = int(r2 and v30 >= VOL30_MIN and hora >= HORA_MIN)
            xt, xz = crossing(D, own, opp, pr - 1, pr + 5000, u.p_fill + 0.002)   # +0,002: incluye prints AL precio de B (B real se llena en cola)
            xt2, xz2 = crossing(D, own, opp, pr - 1, pr + 5000, u.p_fill)
            rows.append({**base, 'print': 1, 'lvl15': lvl, 'vol30': v30, 'hora': hora, 'r2': r2, 'r3': r3,
                         'V1_le': float(xz[xt <= pr + 1000].sum()), 'V1_lt': float(xz2[xt2 <= pr + 1000].sum()), 'V5_lt': float(xz2.sum())})
    W = pd.DataFrame(rows); W.to_csv(os.path.join(OUT, 'b_real_r3.csv'), index=False); print('B real', len(W), 'con print', int(W['print'].sum()))

if __name__ == '__main__':
    if sys.argv[1] == 'breal': b_real()
    else:
        for d in sys.argv[1:]: day(d)
