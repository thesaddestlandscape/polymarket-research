#!/usr/bin/env python3
"""V4 «comprar lo bueno» ronda 2 — simulación por día sobre el extracto BTC (solo lectura). Reloj de decisión = RECEPCIÓN.
Salidas por día en el volumen (checkpoint: si existen, no se recalcula):
  v4_D.csv      réplica V4 (primer evento B1_5m por cierre BTC anidado) con tomador a L=150/215/250 (solo nivel 1; vigía usa l3)
  feat_D.csv.gz instantes con margen >= -0,10 (rasgos causales + desenlace de un tomador a +215 ms con límite = ask del instante
                + etiqueta: ¿se cumple la condición V4 en (t, t+500 ms]?)
  mk_D.csv      maker H23 (bid en reposo en el 5m lado s con precio <= p_limite(bid15) y cancelación) por cierre y variante
Uso: nice -n 19 ionice -c3 python3 -I sim_dia.py D  (ulimit -v 3000000)"""
import sys, os, gzip, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from simlib import *
D = sys.argv[1]
LAT_POST, LAT_CANCEL = 68, 60          # GTC post-only y cancelación medidas (07-Oct; F1 15-Oct 50-84 / 65 ms)
fo_v4, fo_f, fo_m = O + f'v4_{D}.csv', O + f'feat_{D}.csv.gz', O + f'mk_{D}.csv'
if all(os.path.exists(f) for f in (fo_v4, fo_f, fo_m)):
    print(D, 'ya hecho'); sys.exit()
km, LS, B = kmap(D), lados(D), binance(D)
print(D, 'cierres con lado', len(LS), 'binance', len(B['rx']), 'lat E->rx P50/P90', np.percentile(B['lat'], [50, 90]), flush=True)
V4R, FEAT, MK = [], [], []
MKVAR = [('join', -9.0), ('join', -0.05), ('join', 0.0), ('mejora', -9.0), ('mejora', -0.05), ('mejora', 0.0)]

def taker(q5, t, L, lim, acc_obj):
    j = q5.i(t + L)
    if j < 0 or np.isnan(q5.ask[j]): return None, 0.0
    a = q5.ask[j]
    if a <= lim + 1e-9: return a, min(acc_obj, q5.asz[j])
    return a, 0.0

for g, QS, TS in grupos(D):
    C = g
    if C not in LS: continue
    lado, m5id = LS[C]
    sl = 'YES' if lado == 'Up' else 'NO'; ol = 'NO' if sl == 'YES' else 'YES'
    k5, k15, k5o = km.get(('5min', C, sl)), km.get(('15min', C, sl)), km.get(('5min', C, ol))
    if not k5 or not k15 or k5[1] != m5id: continue
    q5, q15 = QS.get(k5[0]), QS.get(k15[0])
    if q5 is None or q15 is None or not len(q5.rx) or not len(q15.rx): continue
    out = DES.get(m5id)
    gana = None if out is None else (out == sl)
    t_ini, t_fin = (C - 300) * 1000 + 1500, (C - 10) * 1000
    inst = np.unique(np.concatenate([q5.rx, q15.rx]))
    inst = inst[(inst >= t_ini) & (inst < t_fin)]
    if not len(inst): continue
    i5, i15 = q5.i(inst), q15.i(inst)
    ok = (i5 >= 0) & (i15 >= 0)
    inst, i5, i15 = inst[ok], i5[ok], i15[ok]
    ask5, bid5, asz5, bsz5 = q5.ask[i5], q5.bid[i5], q5.asz[i5], q5.bsz[i5]
    bid15, ask15, bsz15 = q15.bid[i15], q15.ask[i15], q15.bsz[i15]
    cruz = (bid15 > ask15) | (bid5 > ask5)
    with np.errstate(invalid='ignore'):
        m = bid15 - ask5 - fee(ask5)
    sen = (m >= 0.05 - 1e-12) & ~cruz & ~np.isnan(m)
    # ---------------- réplica V4 (primer evento)
    if sen.any():
        k = int(np.argmax(sen)); t0 = int(inst[k]); a0 = ask5[k]; b0 = bid15[k]; pl = p_limite(b0)
        acc_obj = max(5.0, 2.0 / a0); row = dict(dia=D, cierre=C, lado=lado, m5=m5id, t0=t0, ask0=a0, bid15=b0, plim=pl, gana=gana,
                                                    resto=round(C - t0 / 1000, 2))
        for L in (150, 215, 250):
            p, acc = taker(q5, t0, L, pl, acc_obj)
            row[f'p{L}'], row[f'acc{L}'] = p, acc
        V4R.append(row)
    # ---------------- rasgos por instante (solo margen >= -0,10, sin libro cruzado)
    sgn = 1 if lado == 'Up' else -1
    near = (m >= -0.10) & ~cruz & ~np.isnan(m)
    if near.any():
        tn = inst[near]
        r250, r500, r1000 = (sgn * bin_ret(B, tn, w) for w in (250, 500, 1000))
        j1 = q15.i(tn - 1000); jj = q5.i(tn - 1000)
        db15 = np.where(j1 >= 0, bid15[near] - q15.bid[np.maximum(j1, 0)], np.nan)
        da5 = np.where(jj >= 0, ask5[near] - q5.ask[np.maximum(jj, 0)], np.nan)
        # ¿condición V4 en (t, t+500]?
        ts_sen = inst[sen]
        nxt = np.searchsorted(ts_sen, tn, side='right')
        ev500 = (nxt < len(ts_sen)) & (ts_sen[np.minimum(nxt, len(ts_sen) - 1)] <= tn + 500) if len(ts_sen) else np.zeros(len(tn), bool)
        # tomador a +215 con límite = ask del instante
        je = q5.i(tn + 215); ae = q5.ask[je]; aze = q5.asz[je]
        lim = ask5[near]; accobj = np.maximum(5.0, 2.0 / lim)
        llena = ae <= lim + 1e-9
        for z in zip(tn, m[near], ask5[near], bid15[near], asz5[near], bsz15[near], bid5[near], r250, r500, r1000, db15, da5, ev500, sen[near], ae, np.where(llena, np.minimum(accobj, aze), 0.0)):
            FEAT.append((D, C, lado, m5id, gana) + tuple(z))
    # ---------------- maker H23: bid en reposo en s con precio <= p_limite(bid15); cancelación al romper la condición
    t5 = TS.get(k5[0]); t5o = TS.get(k5o[0]) if k5o else None
    fills_ev = []   # (ex, precio equivalente, tamaño)
    if t5 is not None and len(t5.ex):
        s_ = ~t5.buy; fills_ev += list(zip(t5.ex[s_], t5.p[s_], t5.sz[s_]))
    if t5o is not None and len(t5o.ex):
        b_ = t5o.buy; fills_ev += list(zip(t5o.ex[b_], np.round(1 - t5o.p[b_], 4), t5o.sz[b_]))
    fills_ev.sort()
    fe = np.array([f[0] for f in fills_ev], dtype=np.int64) if fills_ev else np.zeros(0, np.int64)
    valid = ~cruz & ~np.isnan(ask5) & ~np.isnan(bid15) & ~np.isnan(bid5)
    pl_arr = np.array([p_limite(b) if v else np.nan for b, v in zip(bid15, valid)], dtype=float)
    for var, mq in MKVAR:
        want = np.full(len(inst), np.nan)
        if var == 'join': cand = bid5.copy()
        else: cand = np.round(np.minimum(ask5 - 0.01, np.where(np.isnan(pl_arr), -1, pl_arr)), 2)
        okq = valid & ~np.isnan(pl_arr) & (cand <= pl_arr + 1e-9) & (cand < ask5 - 1e-9) & (cand >= bid5 - 1e-9) & (cand >= 0.01) & (m >= mq)
        want[okq] = cand[okq]
        segs = []  # [precio, cola, t_post_ex, t_cancel_ex]
        cur = np.nan
        for t, w, bsz, b5 in zip(inst, want, bsz5, bid5):
            if (np.isnan(w) and np.isnan(cur)) or (not np.isnan(w) and not np.isnan(cur) and abs(w - cur) < 1e-9): continue
            if not np.isnan(cur): segs[-1][3] = t + LAT_CANCEL
            if not np.isnan(w):
                segs.append([w, (bsz if abs(w - b5) < 1e-9 else 0.0), t + LAT_POST, t_fin + LAT_CANCEL])
            cur = w
        need = max(5.0, 2.0 / segs[0][0]) if segs else 5.0
        lleno, coste, t_rel, p_rel = 0.0, 0.0, None, None
        for sg in segs:
            if lleno >= need - 1e-9: break
            a, b = np.searchsorted(fe, sg[2], 'left'), np.searchsorted(fe, sg[3], 'right')
            cola = sg[1]
            for ex_, pe, sz in fills_ev[a:b]:
                falta = need - lleno
                if falta <= 1e-9: break
                if pe < sg[0] - 1e-9: x = falta                      # atraviesa nuestro nivel: llena entera
                elif abs(pe - sg[0]) < 1e-9:                          # en nuestro nivel: primero la cola de delante
                    tomo = min(cola, sz); cola -= tomo; x = min(falta, sz - tomo)
                else: x = 0.0
                if x > 0:
                    lleno += x; coste += x * sg[0]
                    if t_rel is None: t_rel, p_rel = ex_, sg[0]
        MK.append(dict(dia=D, cierre=C, lado=lado, m5=m5id, var=var, mq=mq, n_cotiz=len(segs), lleno=round(lleno, 4), coste=round(coste, 6),
                       t_relleno=t_rel, p_relleno=p_rel, gana=gana, v4_t0=(V4R[-1]['t0'] if V4R and V4R[-1]['cierre'] == C else None),
                       rebate=round(0.2 * fee(coste / lleno) * lleno, 6) if lleno > 0 else 0.0))

def wcsv(f, rows):
    if not rows: open(f, 'w').close(); return
    with open(f + '.tmp', 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    os.replace(f + '.tmp', f)
wcsv(fo_v4, V4R); wcsv(fo_m, MK)
cols = ['dia', 'cierre', 'lado', 'm5', 'gana', 't', 'm', 'ask5', 'bid15', 'asz5', 'bsz15', 'bid5', 'r250', 'r500', 'r1000', 'db15_1s', 'da5_1s', 'ev500', 'sen', 'ask_e215', 'acc_e215']
with gzip.open(fo_f + '.tmp', 'wt') as fh:
    w = csv.writer(fh); w.writerow(cols); w.writerows(FEAT)
os.replace(fo_f + '.tmp', fo_f)
print(D, 'v4', len(V4R), 'feat', len(FEAT), 'mk', len(MK), flush=True)
