#!/usr/bin/env python3
"""M1 (v4_captura_maker, 20-Oct, solo lectura): auditoria de RELOJ del replay H23 + rasgos V3 del relleno.
(a) delta = rx(trade tomador-venta en 5m lado s) - rx(transicion del bid5 por debajo de p) para trades que VACIAN el nivel.
(b) re-simulacion H23 (misma logica que h23_sim_dia.py) adelantando el reloj de los rellenos S ms (S=0 reproduce).
(c) para cada relleno: retorno Binance orientado a s en 5 s / 1 s previos (reloj rx) -> filtro V3 aplicado al MAKER."""
import csv, json, os, sys
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r3')
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/h23_maker')
import numpy as np
from simlib import DES, kmap, lados, grupos, binance, bin_ret
import h23_regla as R
D = sys.argv[1]
OUT = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_captura_maker/'
fo = OUT + f'm1_{D}.csv'
if os.path.exists(fo): print(D, 'ya hecho'); sys.exit()
C_ = R.CONFIG; km, LS = kmap(D), lados(D); B = binance(D)
SHIFTS = (0, 50, 100, 150, 250)
ROWS, DEL = [], []
for C, QS, TS in grupos(D):
    try:
        if C not in LS: continue
        lado, m5id = LS[C]
        sl = 'YES' if lado == 'Up' else 'NO'; ol = 'NO' if sl == 'YES' else 'YES'
        k5, k15, k5o = km.get(('5min', C, sl)), km.get(('15min', C, sl)), km.get(('5min', C, ol))
        if not k5 or not k15 or k5[1] != m5id: continue
        q5, q15 = QS.get(k5[0]), QS.get(k15[0])
        if q5 is None or q15 is None or not len(q5.rx) or not len(q15.rx): continue
        out = DES.get(m5id); gana = None if out is None else (out == sl)
        t_ini, t_fin = (C - 300) * 1000 + C_['ref_conocible_ms'], (C - C_['fin_margen_s']) * 1000
        # (a) delta reloj: trades venta-tomador del token s que vacian el nivel p
        t5 = TS.get(k5[0])
        if t5 is not None and len(t5.rx):
            b = q5.bid
            for rx_, p_, buy_ in zip(t5.rx, t5.p, t5.buy):
                if buy_ or rx_ < t_ini or rx_ >= t_fin: continue
                lo, hi = np.searchsorted(q5.rx, rx_ - 1500, 'left'), np.searchsorted(q5.rx, rx_ + 1500, 'right')
                cand = None
                for j in range(max(lo, 1), hi):
                    if b[j - 1] >= p_ - 1e-9 and b[j] < p_ - 1e-9:
                        if cand is None or abs(q5.rx[j] - rx_) < abs(cand - rx_): cand = int(q5.rx[j])
                if cand is not None: DEL.append(int(rx_) - cand)
        inst = np.unique(np.concatenate([q5.rx, q15.rx])); inst = inst[(inst >= t_ini) & (inst < t_fin)]
        if not len(inst): continue
        i5, i15 = q5.i(inst), q15.i(inst); ok = (i5 >= 0) & (i15 >= 0)
        inst, i5, i15 = inst[ok], i5[ok], i15[ok]
        if not len(inst): continue
        ask5, bid5, bsz5 = q5.ask[i5], q5.bid[i5], q5.bsz[i5]
        bid15, ask15 = q15.bid[i15], q15.ask[i15]
        FIL = []
        t5o = TS.get(k5o[0]) if k5o else None
        for tk, side_s in ((t5, True), (t5o, False)):
            if tk is None or not len(tk.rx): continue
            sel = (~tk.buy) if side_s else tk.buy
            pr = tk.p[sel] if side_s else np.round(1 - tk.p[sel], 4)
            for rx_, p_, sz_ in zip(tk.rx[sel], pr, tk.sz[sel]): FIL.append((int(rx_), float(p_), float(sz_)))
        FIL.sort(); FE0 = np.array([f[0] for f in FIL], dtype=np.int64)
        for brazo, umbral in C_['brazos'].items():
            want = [R.querer(b5, a5, b15, a15, umbral) for b5, a5, b15, a15 in zip(bid5, ask5, bid15, ask15)]
            for var in ('join', 'join_r', 'nc'):
                segs, cur, bloq = [], None, 0
                rep = C_['repost_min_ms'][var]
                for t, w, bsz in zip(inst, want, bsz5):
                    if var == 'nc':
                        if segs: break
                        if w is not None: segs.append([w, float(bsz), int(t), None])
                        continue
                    if (w is None and cur is None) or (w is not None and cur is not None and abs(w - cur) < 1e-9): continue
                    if cur is not None: segs[-1][3] = int(t); bloq = int(t) + rep
                    if w is not None and int(t) < bloq: cur = None; continue
                    if w is not None: segs.append([w, float(bsz), int(t), None])
                    cur = w
                if not segs: continue
                need = R.acciones(segs[0][0])
                for S in SHIFTS:
                    FE = FE0 - S
                    for cola in ('base', 'cons', 'opt'):
                        frac = C_['colas'][cola]; lp = C_['lat_post_ms']; lc = C_['lat_cancel_ms']
                        lleno = coste = 0.0; t_rel = None; nfill = 0
                        for sg in segs:
                            if lleno >= need - 1e-9: break
                            tc = (sg[3] + lc) if sg[3] is not None else t_fin + lc
                            a, b_ = np.searchsorted(FE, sg[2] + lp, 'left'), np.searchsorted(FE, tc, 'right')
                            ahead = frac * sg[1]
                            for k in range(a, b_):
                                rx_, pe, sz = int(FE[k]), FIL[k][1], FIL[k][2]
                                falta = need - lleno
                                if falta <= 1e-9: break
                                if pe < sg[0] - 1e-9: x = falta
                                elif abs(pe - sg[0]) < 1e-9:
                                    tomo = min(ahead, sz); ahead -= tomo; x = min(falta, sz - tomo)
                                else: x = 0.0
                                if x > 0:
                                    lleno += x; coste += x * sg[0]; nfill += 1
                                    if t_rel is None: t_rel = rx_
                        if lleno <= 0: continue
                        pm = coste / lleno
                        r5 = float(bin_ret(B, np.array([t_rel]), 5000)[0]); r1 = float(bin_ret(B, np.array([t_rel]), 1000)[0])
                        sg_ = 1 if lado == 'Up' else -1
                        ROWS.append(dict(dia=D, cierre=C, lado=lado, brazo=brazo, var=var, S=S, cola=cola, need=round(need, 2), lleno=round(lleno, 4),
                                         coste=round(coste, 6), pm=round(pm, 4), gana=gana, T_rel=round(C - t_rel / 1000, 1), n_seg=len(segs),
                                         pnl=(None if gana is None else round(R.pnl_relleno(lleno, pm, gana), 6)),
                                         bret5=(None if np.isnan(r5) else round(sg_ * r5, 3)), bret1=(None if np.isnan(r1) else round(sg_ * r1, 3))))
    except Exception as e:
        print(D, C, type(e).__name__, str(e)[:100], flush=True)
cols = ['dia', 'cierre', 'lado', 'brazo', 'var', 'S', 'cola', 'need', 'lleno', 'coste', 'pm', 'gana', 'T_rel', 'n_seg', 'pnl', 'bret5', 'bret1']
with open(fo + '.tmp', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(ROWS)
os.replace(fo + '.tmp', fo)
d = np.array(DEL)
json.dump(dict(dia=D, n=int(len(d)), p10=float(np.percentile(d, 10)) if len(d) else None, p50=float(np.median(d)) if len(d) else None,
               p90=float(np.percentile(d, 90)) if len(d) else None, frac_libro_antes=float((d > 0).mean()) if len(d) else None,
               frac_gt60=float((d > 60).mean()) if len(d) else None, frac_gt150=float((d > 150).mean()) if len(d) else None),
          open(OUT + f'm1_delta_{D}.json', 'w'))
print(D, 'filas', len(ROWS), 'delta n', len(d), flush=True)
