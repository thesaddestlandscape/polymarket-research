#!/usr/bin/env python3
"""h23_sim_dia.py -- replay H23-MAKER-V1 por dia (solo lectura) sobre el extracto BTC de v4_comprar_lo_bueno (rows_D, k_D, x_D).
Port de r3/sim_dia3.py (el simulador del +0,80) con: regla y latencias de h23_regla.py (fuente unica), brazos A/B (umbral 0,05/0,02),
colas opt/base/cons (calibracion_colas.md), alta 79/254 ms, cancelacion 60/150 ms, control SIN cancelar, y rasgos del relleno
(bid del 5m a +5/+30/+120 s por RECEPCION, caida del bid en el 1 s previo) para el estudio del desplome. Reloj de relleno = RECEPCION.
Salida idempotente por dia: $OUT/h23_D.csv (si existe, no se recalcula). Uso: nice -n 19 ionice -c3 python3 -I h23_sim_dia.py D   (ulimit -v 3000000)
Fallo en un cierre = se registra y se sigue (cobertura en h23_cobertura_D.json)."""
import csv, json, os, sys
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r3')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from simlib import O, DES, kmap, lados, grupos
import h23_regla as R

D = sys.argv[1]
OUT = os.environ.get('H23_OUT', '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_maker/'); os.makedirs(OUT, exist_ok=True)
fo = OUT + f'h23_{D}.csv'
if os.path.exists(fo):
    print(D, 'ya hecho'); sys.exit()
C_ = R.CONFIG
km, LS = kmap(D), lados(D)
ROWS, COB = [], dict(dia=D, cierres_grupo=0, con_lado=0, con_libro=0, errores=0, cotizados=0)

def val(a, i):
    return float(a[i]) if i >= 0 and not np.isnan(a[i]) else None

for C, QS, TS in grupos(D):
    COB['cierres_grupo'] += 1
    try:
        if C not in LS: continue
        COB['con_lado'] += 1
        lado, m5id = LS[C]
        sl = 'YES' if lado == 'Up' else 'NO'; ol = 'NO' if sl == 'YES' else 'YES'
        k5, k15, k5o = km.get(('5min', C, sl)), km.get(('15min', C, sl)), km.get(('5min', C, ol))
        if not k5 or not k15 or k5[1] != m5id: continue
        q5, q15 = QS.get(k5[0]), QS.get(k15[0])
        if q5 is None or q15 is None or not len(q5.rx) or not len(q15.rx): continue
        COB['con_libro'] += 1
        out = DES.get(m5id); gana = None if out is None else (out == sl)
        t_ini, t_fin = (C - 300) * 1000 + C_['ref_conocible_ms'], (C - C_['fin_margen_s']) * 1000
        inst = np.unique(np.concatenate([q5.rx, q15.rx])); inst = inst[(inst >= t_ini) & (inst < t_fin)]
        if not len(inst): continue
        i5, i15 = q5.i(inst), q15.i(inst); ok = (i5 >= 0) & (i15 >= 0)
        inst, i5, i15 = inst[ok], i5[ok], i15[ok]
        if not len(inst): continue
        ask5, bid5, bsz5 = q5.ask[i5], q5.bid[i5], q5.bsz[i5]
        bid15, ask15 = q15.bid[i15], q15.ask[i15]
        # rellenos: prints TOMADORES del WS (misma regla que r3): venta del token s a p, o compra del token contrario a 1-p, por recepcion
        FIL = []
        t5, t5o = TS.get(k5[0]), (TS.get(k5o[0]) if k5o else None)
        for tk, side_s in ((t5, True), (t5o, False)):
            if tk is None or not len(tk.rx): continue
            sel = (~tk.buy) if side_s else tk.buy
            pr = tk.p[sel] if side_s else np.round(1 - tk.p[sel], 4)
            for rx_, p_, sz_ in zip(tk.rx[sel], pr, tk.sz[sel]): FIL.append((int(rx_), float(p_), float(sz_)))
        FIL.sort(); FE = np.array([f[0] for f in FIL], dtype=np.int64)
        for brazo, umbral in C_['brazos'].items():
            want = [R.querer(b5, a5, b15, a15, umbral) for b5, a5, b15, a15 in zip(bid5, ask5, bid15, ask15)]
            for var in ('join', 'join_r', 'nc'):
                segs, cur, bloq = [], None, 0   # seg = [precio, bsz_al_unirse, t_decision, t_decision_cancel]
                rep = C_['repost_min_ms'][var]
                for t, w, bsz in zip(inst, want, bsz5):
                    if var == 'nc':
                        if segs: break
                        if w is not None: segs.append([w, float(bsz), int(t), None])
                        continue
                    if (w is None and cur is None) or (w is not None and cur is not None and abs(w - cur) < 1e-9): continue
                    if cur is not None: segs[-1][3] = int(t); bloq = int(t) + rep
                    if w is not None and int(t) < bloq: cur = None; continue          # esperando a asentar la cancelacion
                    if w is not None: segs.append([w, float(bsz), int(t), None])
                    cur = w
                if not segs: continue
                COB['cotizados'] += 1 if (brazo == 'A' and var == 'join') else 0
                need = R.acciones(segs[0][0])
                for cola, frac in C_['colas'].items():
                    for lp in (C_['lat_post_ms'], C_['lat_post_cons_ms']):
                        for lc in ((C_['lat_cancel_ms'], C_['lat_cancel_cons_ms']) if var != 'nc' else (C_['lat_cancel_ms'],)):
                            lleno = coste = 0.0; t_rel = p_rel = None; nfill = 0
                            for sg in segs:
                                if lleno >= need - 1e-9: break
                                tc = (sg[3] + lc) if sg[3] is not None else t_fin + lc
                                a, b = np.searchsorted(FE, sg[2] + lp, 'left'), np.searchsorted(FE, tc, 'right')
                                ahead = frac * sg[1]
                                for rx_, pe, sz in FIL[a:b]:
                                    falta = need - lleno
                                    if falta <= 1e-9: break
                                    if pe < sg[0] - 1e-9: x = falta                       # atraviesa nuestro nivel: barrido completo
                                    elif abs(pe - sg[0]) < 1e-9:
                                        tomo = min(ahead, sz); ahead -= tomo; x = min(falta, sz - tomo)
                                    else: x = 0.0
                                    if x > 0:
                                        lleno += x; coste += x * sg[0]; nfill += 1
                                        if t_rel is None: t_rel, p_rel = rx_, sg[0]
                            row = dict(dia=D, cierre=C, lado=lado, m5=m5id, brazo=brazo, var=var, cola=cola, lat_post=lp, lat_cancel=lc,
                                       n_cotiz=len(segs), need=round(need, 2), lleno=round(lleno, 4), coste=round(coste, 6), n_fill=nfill,
                                       t_rel=t_rel, p_rel=p_rel, gana=gana, T_rel=(round(C - t_rel / 1000, 1) if t_rel else None),
                                       rebate=round(R.CONFIG['rebate'] * R.fee(coste / lleno) * lleno, 6) if lleno > 0 else 0.0)
                            if t_rel:                                    # rasgos del relleno (desplome del bid del 5m, bid de la cota)
                                j0 = q5.i(t_rel)
                                row['bid5_rel'] = val(q5.bid, j0)
                                for h in (5, 30, 120):
                                    th = t_rel + h * 1000
                                    row[f'bid5_p{h}'] = val(q5.bid, q5.i(th)) if th < C * 1000 else None
                                jm = q5.i(t_rel - 1000)
                                seg = q5.bid[max(jm, 0):j0 + 1] if j0 >= 0 else np.array([])
                                seg = seg[~np.isnan(seg)]
                                row['bid5_max_1s_pre'] = float(seg.max()) if len(seg) else None
                                row['bid15_rel'] = val(q15.bid, q15.i(t_rel)); row['bid15_m1s'] = val(q15.bid, q15.i(t_rel - 1000))
                            ROWS.append(row)
    except Exception as e:                                   # un cierre roto no tumba el dia: queda contado
        COB['errores'] += 1
        print(D, C, type(e).__name__, str(e)[:100], flush=True)

cols = ['dia', 'cierre', 'lado', 'm5', 'brazo', 'var', 'cola', 'lat_post', 'lat_cancel', 'n_cotiz', 'need', 'lleno', 'coste', 'n_fill', 't_rel', 'p_rel',
        'gana', 'T_rel', 'rebate', 'bid5_rel', 'bid5_p5', 'bid5_p30', 'bid5_p120', 'bid5_max_1s_pre', 'bid15_rel', 'bid15_m1s']
with open(fo + '.tmp', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(ROWS)
os.replace(fo + '.tmp', fo)
json.dump(COB, open(OUT + f'h23_cobertura_{D}.json', 'w'))
print(D, 'filas', len(ROWS), COB, flush=True)
