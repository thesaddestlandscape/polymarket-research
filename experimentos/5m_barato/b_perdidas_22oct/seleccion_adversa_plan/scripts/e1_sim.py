#!/usr/bin/env python3
"""e1_sim.py DIA... -- PREREG_E1_CANCELAR_MS.md (sha 31d09a9f...). Simulador a ms de una puja tipo B (ETH/SOL/XRP 5m) con libro, operaciones
y Binance por RECEPCION (salida/datos/ms_D.npz) y reglas de cancelacion previa al relleno S1/S2/S3 con contrafactico.
Salida datos/e1_D.csv.gz: una fila por (mercado, variante) con relleno/obj/gana. Solo lectura de produccion."""
import sys, os, json, hashlib
import numpy as np, pandas as pd
AQUI = os.path.dirname(os.path.abspath(__file__))
SAL = os.path.join(AQUI, '..', '..', 'salida', 'scripts'); sys.path.insert(0, SAL)
from msdata import Dia, SYM, DD
OUT = os.path.join(AQUI, '..', 'datos')
PRE = os.path.join(AQUI, '..', 'PREREG_E1_CANCELAR_MS.md')
assert hashlib.sha256(open(PRE, 'rb').read()).hexdigest().startswith('31d09a9f53c1da69'), 'prereg cambiado'
STEP = 100; T_HI, T_LO = 298.0, 65.0; SETTLE = 1500; LAG_VIVA = 50; COOL = 2068
RULES = [('S1_x2_w500', 'S1', 2, 500), ('S1_x2_w2000', 'S1', 2, 2000), ('S1_x4_w500', 'S1', 4, 500), ('S1_x4_w2000', 'S1', 4, 2000),
         ('S2_w500', 'S2', 20, 500), ('S2_w2000', 'S2', 20, 2000), ('S3_w2000', 'S3', 20, 2000)]
SHIFTS = [-240000, -180000, -120000, -60000, 60000, 120000, 180000, 240000]
des = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
des.update(json.load(open(os.path.join(DD, 'desenlaces_extra.json'))))

def tops(D, k, t):
    a, b = D.qs[k], D.qs[k + 1]; r = D.qr[a:b]; v = D.qv[a:b]
    if b <= a: return np.full(len(t), np.nan), np.full(len(t), np.nan), np.full(len(t), np.nan)
    j = np.searchsorted(r, t, 'right') - 1; ok = j >= 0; jj = np.where(ok, j, 0)
    bid = np.where(ok, v[jj, 0], np.nan); ask = np.where(ok, v[jj, 1], np.nan)
    # hora del ultimo cambio de bid
    if len(r):
        ch = np.r_[True, v[1:, 0] != v[:-1, 0]]; ci = np.flatnonzero(ch)
        lc_idx = np.searchsorted(ci, jj, 'right') - 1; lc = np.where(ok, r[ci[np.clip(lc_idx, 0, None)]], np.nan)
    else: lc = np.full(len(t), np.nan)
    return bid.astype(float), ask.astype(float), lc

def obj_raw(bid, ask, k):
    b = np.round(np.nan_to_num(bid, nan=0) * 1000).astype(int); a = np.round(np.nan_to_num(ask, nan=9) * 1000).astype(int)
    o = np.where(b % 10 == 0, b - k * 10, (b // 10 - (k - 1)) * 10)
    band = np.isfinite(bid) & (bid > 0.11 + 1e-9) & (bid <= 0.30 + 1e-9)
    ok = band & (o >= 100) & (o <= 300) & (o < b) & (o < a)
    return np.where(ok, o / 1000.0, np.nan)

def triggers(times, vals, W, thr):
    """dispara en cada evento con suma de vals en (t-W, t] >= thr"""
    if len(times) == 0: return np.zeros(0, np.int64)
    cs = np.r_[0, np.cumsum(vals)]; i0 = np.searchsorted(times, times - W, 'right')
    s = cs[np.arange(1, len(times) + 1)] - cs[i0]
    return times[s >= thr - 1e-9]

def bn_trig(D, sym, sg, t0, t1, W, X):
    a, b = D.xs[sym], D.xs[sym + 1]; r = D.xr[a:b]; v = D.xv[a:b].astype(float)
    i0, i1 = np.searchsorted(r, t0 - W - 1000), np.searchsorted(r, t1, 'right')
    rr, vv = r[i0:i1], v[i0:i1]
    if len(rr) < 2: return np.zeros(0, np.int64), np.zeros(0, np.int64)
    j = np.searchsorted(rr, rr - W, 'right') - 1; ok = j >= 0
    ret = np.where(ok, (vv / vv[np.clip(j, 0, None)] - 1) * 1e4 * sg, 0.0)
    m = (rr >= t0)
    return rr[m & (ret <= -X)], rr[m & (ret >= X)]

def flows(D, kown, kopp, t0, t1):
    """(times, contra, favor) de operaciones del mercado en [t0,t1]: contra = BUY opuesto + SELL propio"""
    T = []; C = []; F = []
    for k, own in ((kown, True), (kopp, False)):
        if k is None: continue
        r, v = D.trades(k, t0, t1)
        buy = v[:, 1] == 1; sz = v[:, 2].astype(float)
        con = np.where(buy, 0, sz) if own else np.where(buy, sz, 0)
        fav = np.where(buy, sz, 0) if own else np.where(buy, 0, sz)
        T.append(r); C.append(con); F.append(fav)
    if not T: return np.zeros(0, np.int64), np.zeros(0), np.zeros(0)
    t = np.concatenate(T); o = np.argsort(t, kind='stable')
    return t[o], np.concatenate(C)[o], np.concatenate(F)[o]

def first_fill(cand_r, trig, D_ms):
    """primer candidato no cubierto por [ts+D, ts+COOL]"""
    if len(trig) == 0: return 0 if len(cand_r) else -1
    trig = np.sort(trig)
    for i, r in enumerate(cand_r):
        j = np.searchsorted(trig, r - D_ms, 'right') - 1
        if j >= 0 and r - trig[j] <= COOL: continue
        return i
    return -1

def day(d):
    D = Dia(d); rows = []; nmiss = 0
    mk = {}
    for i, (act, marco, mid, fin, lado) in enumerate(D.tmap):
        if str(marco) != '5min' or str(act) not in SYM: continue
        fe = int(pd.Timestamp(str(fin)).timestamp()); mk.setdefault((str(act), fe, str(mid)), {})[str(lado)] = i
    porfin = {}
    for (act, fe, mid), dd in mk.items(): porfin.setdefault(fe, {})[act] = dd
    for (act, fe, mid), dd in sorted(mk.items(), key=lambda x: x[0][1]):
        if 'YES' not in dd or 'NO' not in dd: continue
        w = des.get(mid)
        g = (fe * 1000 - np.arange(T_HI * 1000, T_LO * 1000 - 1, -STEP)).astype(np.int64)
        by, ay, lcy = tops(D, dd['YES'], g); bn, an, lcn = tops(D, dd['NO'], g)
        def band(b): return np.isfinite(b) & (b > 0.11 + 1e-9) & (b <= 0.30 + 1e-9)
        cy, cn = band(by), band(bn)
        if not (cy | cn).any(): continue
        if w is None: nmiss += 1; continue
        f0 = int(np.argmax(cy | cn)); yes = bool(cy[f0]); sg = 1 if yes else -1
        bid, ask, lc = (by, ay, lcy) if yes else (bn, an, lcn)
        kk = 2 if act == 'ETH' else 1; raw = obj_raw(bid, ask, kk)
        O = np.full(len(g), np.nan); cur = np.nan
        for i in range(f0, len(g)):
            if np.isfinite(lc[i]) and g[i] - lc[i] >= SETTLE: cur = raw[i]
            O[i] = cur
        if not np.isfinite(O).any(): continue
        kown = dd['YES'] if yes else dd['NO']; kopp = dd['NO'] if yes else dd['YES']
        t0, t1 = int(g[0]), int(g[-1] + STEP)
        tf, con, fav = flows(D, kown, kopp, t0 - 3000, t1 + 1000)
        # candidatos de relleno
        cr = []; cp = []
        for k, own in ((kown, True), (kopp, False)):
            r, v = D.trades(k, t0, t1 + LAG_VIVA)
            for rr, (pr, sd, sz) in zip(r, v):
                gi = int((rr - LAG_VIVA - t0) // STEP)
                if gi < 0 or gi >= len(g): continue
                o = O[gi]
                if not np.isfinite(o): continue
                if (own and sd == 0 and pr < o - 1e-6) or ((not own) and sd == 1 and pr > 1 - o + 1e-6): cr.append(int(rr)); cp.append(o)
        o_ = np.argsort(cr, kind='stable'); cr = np.array(cr, np.int64)[o_]; cp = np.array(cp)[o_]
        gana = int((w == 'YES') == yes)
        # senales
        trig = {}
        for name, typ, X, W in RULES:
            if typ == 'S1': c, f = bn_trig(D, SYM[act], sg, t0, t1, W, X)
            elif typ == 'S2':
                c = triggers(tf[con > 0], con[con > 0], W, X); f = triggers(tf[fav > 0], fav[fav > 0], W, X)
            else:
                TT = []; CC = []; FF = []
                for a2, d2 in porfin.get(fe, {}).items():
                    if a2 == act or 'YES' not in d2 or 'NO' not in d2: continue
                    # mismo sentido que nuestro lado: contra = flujo hacia el lado opuesto al nuestro en esa moneda
                    k_s = d2['YES'] if yes else d2['NO']; k_o = d2['NO'] if yes else d2['YES']
                    t2, c2, f2 = flows(D, k_s, k_o, t0 - 3000, t1 + 1000); TT.append(t2); CC.append(c2); FF.append(f2)
                if TT:
                    t2 = np.concatenate(TT); o2 = np.argsort(t2, kind='stable'); t2 = t2[o2]; c2 = np.concatenate(CC)[o2]; f2 = np.concatenate(FF)[o2]
                    c = triggers(t2[c2 > 0], c2[c2 > 0], W, X); f = triggers(t2[f2 > 0], f2[f2 > 0], W, X)
                else: c = f = np.zeros(0, np.int64)
            trig[name] = (np.asarray(c, np.int64), np.asarray(f, np.int64))
        base = {'dia': d, 'act': act, 'mid': mid, 'fin': fe, 'yes': int(yes), 'gana': gana, 'n_cand': len(cr)}
        def emit(var, i):
            if i < 0: rows.append({**base, 'var': var, 'fill': 0, 'obj': np.nan, 'r': -1})
            else: rows.append({**base, 'var': var, 'fill': 1, 'obj': float(cp[i]), 'r': int(cr[i])})
        ib = 0 if len(cr) else -1
        for name, _, _, _ in RULES:   # descriptivo: adelanto (ms) de la ultima senal contra antes del relleno base
            c = np.sort(trig[name][0]); j = np.searchsorted(c, cr[0], 'right') - 1 if ib >= 0 else -1
            base['lead_' + name] = float(cr[0] - c[j]) if j >= 0 else np.nan
        emit('BASE', ib)
        for name, _, _, _ in RULES:
            c, f = trig[name]
            emit(f'{name}|D100', first_fill(cr, c, 100)); emit(f'{name}|D250', first_fill(cr, c, 250)); emit(f'{name}|D0', first_fill(cr, c, 0))
            emit(f'{name}|INV', first_fill(cr, f, 100))
            for s in SHIFTS: emit(f'{name}|SH{s//1000:+d}', first_fill(cr, c + s, 100))
    df = pd.DataFrame(rows); of = os.path.join(OUT, f'e1_{d}.csv.gz'); df.to_csv(of, index=False)
    print(d, 'mercados', df[df['var'] == 'BASE'].shape[0], 'sin desenlace (missing)', nmiss, '->', of, flush=True)

if __name__ == '__main__':
    for d in sys.argv[1:]: day(d)
