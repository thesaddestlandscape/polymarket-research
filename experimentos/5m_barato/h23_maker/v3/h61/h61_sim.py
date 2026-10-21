#!/usr/bin/env python3
"""H61 retencion: replay H23 (regla congelada, solo lectura) con la defensa Binance en contra, variantes X (bps) x W (ms) x modo x rep.
Salidas: fills_D.csv (por cierre/brazo/variante) y prints_D.csv (poblacion de prints que habrian rellenado nuestra puja, con ret Binance)."""
import csv, os, sys
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/h23_maker/v2')
import numpy as np
import h23_sim_v2 as V
from h23_sim_v2 import R, simlib, kmap, lados, llenar, cargar_binance
OUT = sys.argv[2] if len(sys.argv) > 2 else '/tmp/'
XS = (0.0, 0.5, 1.0, 2.0, 3.0); WS = (500, 1000, 3000); REPS = (150, 1500); MODOS = ('cancel', 'repuja')

def segs_mode(inst, want, bsz, allow, rep):
    segs, cur, bloq = [], None, None
    pw, pb, pt = None, 0.0, None
    for t, w, b, al in zip(inst, want, bsz, allow):
        t = int(t)
        if cur is None and bloq is not None and pt is not None and pt < bloq < t and pw is not None:
            segs.append([pw, pb, bloq, None]); cur = pw; bloq = None
        pw, pb, pt = (w if al else None), float(b), t
        if (w is None and cur is None) or (w is not None and cur is not None and abs(w - cur) < 1e-9): continue
        if cur is not None: segs[-1][3] = t; bloq = t + rep
        if w is not None and bloq is not None and t < bloq: cur = None; continue
        if w is not None and al: segs.append([w, float(b), t, None]); bloq = None; cur = w
        else: cur = None
    return segs

def retW(BN, t, W, lado):
    rx, p = BN
    i1 = np.searchsorted(rx, t, 'right') - 1; i0 = np.searchsorted(rx, t - W, 'right') - 1
    out = np.full(len(t), np.nan)
    ok = (i0 >= 0) & (i1 >= 0) & (rx[np.maximum(i1, 0)] >= t - 5000)
    out[ok] = (p[i1[ok]] / p[i0[ok]] - 1) * 1e4
    return out if lado == 'Up' else -out

def main(D):
    C_ = R.CONFIG; lp, lc, frac = C_['lat_post_ms'], C_['lat_cancel_ms'], C_['colas']['base']
    km, LS, BN = kmap(D, 'BTC'), lados(D, 'BTC'), cargar_binance(D, 'BTC')
    FO, PO = [], []
    for C, QS, TS in simlib.grupos(D):
        if C not in LS: continue
        lado, m5id = LS[C]; sl = 'YES' if lado == 'Up' else 'NO'; ol = 'NO' if sl == 'YES' else 'YES'
        k5, k15, k5o = km.get(('5min', C, sl)), km.get(('15min', C, sl)), km.get(('5min', C, ol))
        if not k5 or not k15 or k5[1] != m5id: continue
        q5, q15 = QS.get(k5[0]), QS.get(k15[0])
        if q5 is None or q15 is None or not len(q5.rx) or not len(q15.rx): continue
        out = simlib.DES.get(m5id); gana = None if out is None else (out == sl)
        if gana is None: continue
        t_ini, t_fin = (C - 300) * 1000 + C_['ref_conocible_ms'], (C - C_['fin_margen_s']) * 1000
        ib = np.unique(np.concatenate([q5.rx, q15.rx])); ib = ib[(ib >= t_ini) & (ib < t_fin)]
        if not len(ib): continue
        bx = BN[0][(BN[0] >= t_ini) & (BN[0] < t_fin)] if BN is not None else np.zeros(0, np.int64)
        inst = np.unique(np.concatenate([ib, bx]))
        i5, i15 = q5.i(inst), q15.i(inst); ok = (i5 >= 0) & (i15 >= 0)
        inst, i5, i15 = inst[ok], i5[ok], i15[ok]
        if not len(inst): continue
        ask5, bid5, bsz5, bid15, ask15 = q5.ask[i5], q5.bid[i5], q5.bsz[i5], q15.bid[i15], q15.ask[i15]
        FIL = []
        for tk, side_s in ((TS.get(k5[0]), True), (TS.get(k5o[0]) if k5o else None, False)):
            if tk is None or not len(tk.rx): continue
            sel = (~tk.buy) if side_s else tk.buy
            pr = tk.p[sel] if side_s else np.round(1 - tk.p[sel], 4)
            for rx_, p_, sz_ in zip(tk.rx[sel], pr, tk.sz[sel]): FIL.append((int(rx_), float(p_), float(sz_)))
        FIL.sort(); FE = np.array([f[0] for f in FIL], dtype=np.int64)
        RET = {W: retW(BN, inst, W, lado) for W in WS} if BN is not None else None
        for brazo, umbral in C_['brazos'].items():
            want = [R.querer(b5, a5, b15, a15, umbral) for b5, a5, b15, a15 in zip(bid5, ask5, bid15, ask15)]
            if not any(w is not None for w in want): continue
            # poblacion de prints: want activo en el instante <= t_print - lp y print a <= want
            if FIL and RET is not None:
                wa = np.array([np.nan if w is None else w for w in want])
                for rx_, pe, sz in FIL:
                    if rx_ < t_ini or rx_ >= t_fin: continue
                    j = np.searchsorted(inst, rx_ - lp, 'right') - 1
                    if j < 0 or wa[j] != wa[j] or pe > wa[j] + 1e-9: continue
                    tt = np.array([rx_ - lc]); r = [retW(BN, tt, W, lado)[0] for W in WS]
                    PO.append((D, C, brazo, wa[j], int(gana), round(sz, 2), *[('' if x != x else round(x, 3)) for x in r]))
            variants = [('v1', 0, 0.0, 'none')] + [(m, W, X, m) for m in MODOS for W in WS for X in XS]
            for rep in REPS + (0,):
                for nom, W, X, m in variants:
                    if rep == 0 and nom != 'v1': continue
                    allow = np.ones(len(inst), bool) if m == 'none' else ~(RET[W] < -X)  # NaN -> no dispara
                    if m == 'cancel':
                        w2 = [w if a else None for w, a in zip(want, allow)]; segs = segs_mode(inst, w2, bsz5, np.ones(len(inst), bool), rep)
                    else:
                        segs = segs_mode(inst, want, bsz5, allow, rep)
                    if not segs: continue
                    need = R.acciones(segs[0][0])
                    lleno, coste, t_rel, p_rel, nfill = llenar(segs, need, frac, lp, lc, FIL, FE, t_fin)
                    reb = R.CONFIG['rebate'] * R.fee(coste / lleno) * lleno if lleno > 0 else 0.0
                    FO.append((D, C, brazo, m, W, X, rep, len(segs), round(need, 2), round(lleno, 4), round(coste, 6), int(gana), round(reb, 6),
                               round(lleno * gana - coste + reb, 6), t_rel or ''))
    with open(OUT + f'fills_{D}.csv', 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['dia', 'cierre', 'brazo', 'modo', 'W', 'X', 'rep', 'n_seg', 'need', 'lleno', 'coste', 'gana', 'rebate', 'pnl', 't_rel']); w.writerows(FO)
    with open(OUT + f'prints_{D}.csv', 'w', newline='') as fh:
        w = csv.writer(fh); w.writerow(['dia', 'cierre', 'brazo', 'p', 'gana', 'sz', 'r500', 'r1000', 'r3000']); w.writerows(PO)
    print(D, 'fills', len(FO), 'prints', len(PO), flush=True)

if __name__ == '__main__':
    main(sys.argv[1])
