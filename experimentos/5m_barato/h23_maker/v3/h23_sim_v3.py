#!/usr/bin/env python3
"""h23_sim_v3.py -- replay H23 v3 (solo lectura, OFFLINE, BTC). Port de ../v2/h23_sim_v2.py (que queda intacto) con tres cambios y NADA mas:
  (1) TAMANO: sizing '2eur' (= v1/v2, R.acciones: max(5, 2 EUR/p)) y 'real' (= arnes H47/H23: 5 acc o ceil(1 USD/p), tope 10, R.acciones_real). En 'real' tambien se aplica el
      UNIVERSO EJECUTABLE del paquete: no se cotiza (ni se mantiene como objetivo) a precio fuera de [0,10; 0,60] y no se abre una puja NUEVA con T <= 12 s.
  (2) CIERRE: modo 'acum' (v1/v2: el relleno puede acumularse sobre varias operaciones y segmentos hasta `need`) y 'primer' (arnes real: UN relleno, aunque parcial, CIERRA la
      puja; el replay corta tras la PRIMERA operacion que toca nuestra orden = cota inferior de rellenos adicionales antes de que el arnes cancele).
  (3) retardos de re-puja 0/50/150/300/500/1500 ms tras la DECISION de cancelar (misma logica exacta de v2; 'r300' = latencia plausible del arnes real, ver PREREGISTRO).
Sin Binance (x_D) ni rasgos H61: no hacen falta. Validacion: sizing 2eur + acum debe reproducir v2 fila a fila (h23_valida_v3.py).
Uso: nice -n 19 ionice -c3 python3 -I h23_sim_v3.py D   (ulimit -v 3000000). Env: H23V3_IN (extracto), H23V3_OUT. Idempotente: si existe la salida, no recalcula.
La regla (querer/p_limite/umbral/mq) es la de v1: h23_regla_v3.py solo anade `repuja_ms` y `acciones_real` (diff en el informe)."""
import csv, json, os, sys
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r3')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from datetime import datetime
import numpy as np
import simlib
from simlib import DES, grupos, DL
import h23_regla_v3 as R

REPS = (0, 50, 150, 300, 500, 1500)
SIZINGS = ('2eur', 'real')
CIERRES = ('acum', 'primer')
IN = os.environ.get('H23V3_IN', '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/')
OUT = os.environ.get('H23V3_OUT', '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/')
simlib.O = IN
CFG = R.CONFIG


def kmap(key, coin='BTC'):
    km = {}
    for ln in open(IN + f'k_{key}.csv'):
        c = ln.rstrip('\n').split(',')
        if len(c) >= 8 and c[3] == coin and c[4] in ('5min', '15min'):
            C = int(datetime.fromisoformat(c[6]).timestamp())
            km[(c[4], C, c[7])] = (c[2], c[5])
    return km


def lados(D, coin='BTC'):
    out = {}
    for r in csv.DictReader(open(DL + f'vigia_5m_barato/controles_{D}.csv')):
        if r['moneda'] == coin: out[int(r['cierre'])] = (r['lado'], r['market_compra'])
    return out


def querible(w, real):
    """Precio objetivo efectivo: en sizing 'real' un precio fuera del universo ejecutable equivale a no querer pujar (el arnes no envia; si habia orden a otro precio, la cancela)."""
    if w is None: return None
    if real and not (CFG['precio_min_ejec'] - 1e-9 <= w <= CFG['precio_max_ejec'] + 1e-9): return None
    return w


def segmentos(inst, want, bsz, rep, t_post_max):
    """Segmentos de puja [precio, profundidad_al_unirse, t_decision, t_decision_cancel]. Misma logica que v2 (exact=True) + t_post_max: no se abre un segmento NUEVO con t >= t_post_max
    (el arnes no postea con T <= t_stop+2 = 12 s; una orden viva sigue vigilandose hasta t_fin). t_post_max=inf reproduce v2."""
    segs, cur, bloq = [], None, None
    pw, pb, pt = None, 0.0, None
    for t, w, b in zip(inst, want, bsz):
        t = int(t)
        if cur is None and bloq is not None and pt is not None and pt < bloq < t and pw is not None:
            if bloq < t_post_max:
                segs.append([pw, pb, bloq, None]); cur = pw
            bloq = None                                                    # re-puja exacta en el instante de desbloqueo
        pw, pb, pt = w, float(b), t
        if (w is None and cur is None) or (w is not None and cur is not None and abs(w - cur) < 1e-9): continue
        if cur is not None: segs[-1][3] = t; bloq = t + rep
        if w is not None and bloq is not None and t < bloq: cur = None; continue
        if w is not None and t >= t_post_max: cur = None; continue          # no se abre puja nueva en los ultimos 12 s
        if w is not None: segs.append([w, float(b), t, None]); bloq = None
        cur = w
    return segs


def llenar(segs, need, frac, lp, lc, FIL, FE, t_fin, primer):
    lleno = coste = 0.0; t_rel = p_rel = None; nfill = 0
    for sg in segs:
        if lleno >= need - 1e-9 or (primer and nfill): break
        tc = (sg[3] + lc) if sg[3] is not None else t_fin + lc
        a, b = np.searchsorted(FE, sg[2] + lp, 'left'), np.searchsorted(FE, tc, 'right')
        ahead = frac * sg[1]
        for rx_, pe, sz in FIL[a:b]:
            falta = need - lleno
            if falta <= 1e-9: break
            if pe < sg[0] - 1e-9: x = falta
            elif abs(pe - sg[0]) < 1e-9:
                tomo = min(ahead, sz); ahead -= tomo; x = min(falta, sz - tomo)
            else: x = 0.0
            if x > 0:
                lleno += x; coste += x * sg[0]; nfill += 1
                if t_rel is None: t_rel, p_rel = rx_, sg[0]
                if primer: break
    return lleno, coste, t_rel, p_rel, nfill


def main(D, coin='BTC'):
    key = D
    os.makedirs(OUT, exist_ok=True)
    fo = OUT + f'v3_{coin}_{D}.csv'
    if os.path.exists(fo):
        print(coin, D, 'ya hecho'); return
    km, LS = kmap(key, coin), lados(D, coin)
    ROWS = []
    COB = dict(coin=coin, dia=D, cierres_grupo=0, con_lado=0, con_libro=0, errores=0, cotizados_A=0, cotizados_B=0, sin_desenlace=0, rows_fuente=f'{IN}rows_{key}.csv.gz')
    for C, QS, TS in grupos(key):
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
            if gana is None: COB['sin_desenlace'] += 1
            t_ini, t_fin = (C - 300) * 1000 + CFG['ref_conocible_ms'], (C - CFG['fin_margen_s']) * 1000
            t_post_max_real = (C - CFG['t_min_ejec_s']) * 1000
            inst = np.unique(np.concatenate([q5.rx, q15.rx])); inst = inst[(inst >= t_ini) & (inst < t_fin)]
            if not len(inst): continue
            i5, i15 = q5.i(inst), q15.i(inst); ok = (i5 >= 0) & (i15 >= 0)
            inst, i5, i15 = inst[ok], i5[ok], i15[ok]
            if not len(inst): continue
            ask5, bid5, bsz5 = q5.ask[i5], q5.bid[i5], q5.bsz[i5]
            bid15, ask15 = q15.bid[i15], q15.ask[i15]
            FIL = []
            t5, t5o = TS.get(k5[0]), (TS.get(k5o[0]) if k5o else None)
            for tk, side_s in ((t5, True), (t5o, False)):
                if tk is None or not len(tk.rx): continue
                sel = (~tk.buy) if side_s else tk.buy
                pr = tk.p[sel] if side_s else np.round(1 - tk.p[sel], 4)
                for rx_, p_, sz_ in zip(tk.rx[sel], pr, tk.sz[sel]): FIL.append((int(rx_), float(p_), float(sz_)))
            FIL.sort(); FE = np.array([f[0] for f in FIL], dtype=np.int64)
            for brazo, umbral in CFG['brazos'].items():
                want0 = [R.querer(b5, a5, b15, a15, umbral) for b5, a5, b15, a15 in zip(bid5, ask5, bid15, ask15)]
                for sizing in SIZINGS:
                    real = sizing == 'real'
                    want = [querible(w, real) for w in want0]
                    tpm = t_post_max_real if real else float('inf')
                    for rep in REPS:
                        segs = segmentos(inst, want, bsz5, rep, tpm)
                        if not segs: continue
                        if rep == 0 and sizing == '2eur': COB['cotizados_' + brazo] += 1
                        need = R.acciones_real(segs[0][0]) if real else R.acciones(segs[0][0])
                        for cierre in CIERRES:
                            for cola, frac in CFG['colas'].items():
                                for lp in (CFG['lat_post_ms'], CFG['lat_post_cons_ms']):
                                    for lc in (CFG['lat_cancel_ms'], CFG['lat_cancel_cons_ms']):
                                        lleno, coste, t_rel, p_rel, nfill = llenar(segs, need, frac, lp, lc, FIL, FE, t_fin, cierre == 'primer')
                                        ROWS.append(dict(coin=coin, dia=D, cierre=C, lado=lado, m5=m5id, brazo=brazo, sizing=sizing, modo=cierre, rep=rep, cola=cola,
                                                         lat_post=lp, lat_cancel=lc, n_cotiz=len(segs), need=round(need, 2), lleno=round(lleno, 4), coste=round(coste, 6),
                                                         n_fill=nfill, t_rel=t_rel, p_rel=p_rel, gana=gana,
                                                         rebate=round(CFG['rebate'] * R.fee(coste / lleno) * lleno, 6) if lleno > 0 else 0.0))
        except Exception as e:
            COB['errores'] += 1
            print(coin, D, C, type(e).__name__, str(e)[:100], flush=True)
    cols = ['coin', 'dia', 'cierre', 'lado', 'm5', 'brazo', 'sizing', 'modo', 'rep', 'cola', 'lat_post', 'lat_cancel', 'n_cotiz', 'need', 'lleno', 'coste', 'n_fill',
            't_rel', 'p_rel', 'gana', 'rebate']
    with open(fo + '.tmp', 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(ROWS)
    os.replace(fo + '.tmp', fo)
    json.dump(COB, open(OUT + f'v3_cobertura_{coin}_{D}.json', 'w'))
    print(coin, D, 'filas', len(ROWS), COB, flush=True)


if __name__ == '__main__':
    main(sys.argv[1])
