#!/usr/bin/env python3
"""h23_sim_v2.py -- replay H23 v2 (solo lectura, OFFLINE). NO toca el paquete_real congelado ni h23_regla.py (importa la regla tal cual).
Cambios respecto a ../h23_sim_dia.py (que queda intacto):
  (1) retardo de RE-PUJA tras cancelar parametrizado: REPS = 0/50/150/500/1500 ms. La re-puja se hace en t_cancel_decision + rep EXACTO (el estado del libro
      es constante entre instantes de actualizacion, asi que se evalua `want` del instante previo al hueco); el replay antiguo solo re-pujaba en el SIGUIENTE
      instante de libro >= bloqueo. Validacion: rep=0 exacto == `join` antiguo; rep=1500 'discreto' (var 1500d) == `join_r` antiguo.
  (2) multiplos de stake (2/5/10/25 EUR) para el estudio de capacidad (solo cola base, 79/60 ms, rep 0 y 150).
  (3) moneda parametrizable (alts extraidas aparte: ficheros rows_<COIN>_<D>.csv.gz / k_<COIN>_<D>.csv).
  (4) rasgo ciego al desenlace: retorno Binance 1 s (RECEPCION) orientado al lado s en el relleno y fraccion de instantes de cotizacion con Binance en contra
      (solo BTC; descriptivo de H61; NO se calcula ningun EV con ese corte).
Uso: nice -n 19 ionice -c3 python3 -I h23_sim_v2.py COIN D   (ulimit -v 3000000). Env: H23V2_IN (dir extracto), H23V2_OUT. Idempotente: si existe la salida, no recalcula."""
import csv, gzip, json, os, sys
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/v4_comprar_lo_bueno/r3')
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/h23_maker')
from datetime import datetime
import numpy as np
import simlib
from simlib import DES, grupos, DL
import h23_regla as R

REPS = (0, 50, 150, 500, 1500)
VARS = [(f'r{r}', r, True) for r in REPS] + [('r1500d', 1500, False)]   # r1500d: bloqueo DISCRETO (replica el join_r antiguo; solo validacion)
MULTS = (1.0, 2.5, 5.0, 12.5)                                            # stake 2 / 5 / 10 / 25 EUR
IN = os.environ.get('H23V2_IN', '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/')
OUT = os.environ.get('H23V2_OUT', '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/')
simlib.O = IN


def kmap(key, coin):
    km = {}
    for ln in open(IN + f'k_{key}.csv'):
        c = ln.rstrip('\n').split(',')
        if len(c) >= 8 and c[3] == coin and c[4] in ('5min', '15min'):
            C = int(datetime.fromisoformat(c[6]).timestamp())
            km[(c[4], C, c[7])] = (c[2], c[5])
    return km


def lados(D, coin):
    out = {}
    for r in csv.DictReader(open(DL + f'vigia_5m_barato/controles_{D}.csv')):
        if r['moneda'] == coin: out[int(r['cierre'])] = (r['lado'], r['market_compra'])
    return out


def segmentos(inst, want, bsz, rep, exact):
    """Segmentos de puja [precio, profundidad_al_unirse, t_decision, t_decision_cancel]. Misma logica que h23_sim_dia (var join/join_r) + re-puja exacta."""
    segs, cur, bloq = [], None, None
    pw, pb = None, 0.0
    pt = None
    for t, w, b in zip(inst, want, bsz):
        t = int(t)
        if exact and cur is None and bloq is not None and pt is not None and pt < bloq < t and pw is not None:
            segs.append([pw, pb, bloq, None]); cur = pw; bloq = None        # re-puja exacta en el instante de desbloqueo
        pw, pb, pt = w, float(b), t
        if (w is None and cur is None) or (w is not None and cur is not None and abs(w - cur) < 1e-9): continue
        if cur is not None: segs[-1][3] = t; bloq = t + rep
        if w is not None and bloq is not None and t < bloq: cur = None; continue
        if w is not None: segs.append([w, float(b), t, None]); bloq = None
        cur = w
    return segs


def llenar(segs, need, frac, lp, lc, FIL, FE, t_fin):
    lleno = coste = 0.0; t_rel = p_rel = None; nfill = 0
    for sg in segs:
        if lleno >= need - 1e-9: break
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
    return lleno, coste, t_rel, p_rel, nfill


def cargar_binance(D, coin):
    f = IN + f'x_{D}.csv.gz'
    if coin != 'BTC' or not os.path.exists(f): return None
    rows = []
    with gzip.open(f, 'rt') as fh:
        for ln in fh:
            c = ln.split(',')
            try: rows.append((int(c[7]), float(c[3])))
            except (ValueError, IndexError): pass
    if not rows: return None
    rows.sort(); a = np.array(rows, dtype=np.float64)
    return a[:, 0].astype(np.int64), a[:, 1]


def ret1s_bps(bn, t, lado):
    """Retorno Binance 1 s hasta t (RECEPCION), orientado al lado s (positivo = a favor). NaN si falta."""
    if bn is None: return float('nan')
    rx, p = bn
    i1, i0 = np.searchsorted(rx, t, 'right') - 1, np.searchsorted(rx, t - 1000, 'right') - 1
    if i0 < 0 or i1 < 0 or rx[i1] < t - 5000: return float('nan')
    r = (p[i1] / p[i0] - 1.0) * 1e4
    return r if lado == 'Up' else -r


def main(coin, D):
    key = D if coin == 'BTC' else f'{coin}_{D}'
    os.makedirs(OUT, exist_ok=True)
    fo = OUT + f'v2_{coin}_{D}.csv'
    if os.path.exists(fo):
        print(coin, D, 'ya hecho'); return
    C_ = R.CONFIG
    km, LS, BN = kmap(key, coin), lados(D, coin), cargar_binance(D, coin)
    ROWS = []
    COB = dict(coin=coin, dia=D, cierres_grupo=0, con_lado=0, con_libro=0, errores=0, cotizados_A=0, cotizados_B=0, sin_desenlace=0,
               q_inst=0, q_contra=0, q_cero=0, q_sinbin=0)
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
            t_ini, t_fin = (C - 300) * 1000 + C_['ref_conocible_ms'], (C - C_['fin_margen_s']) * 1000
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
            for brazo, umbral in C_['brazos'].items():
                want = [R.querer(b5, a5, b15, a15, umbral) for b5, a5, b15, a15 in zip(bid5, ask5, bid15, ask15)]
                if brazo == 'A' and BN is not None:                           # H61 descriptivo: frecuencia del disparo (ciego al desenlace)
                    for t, w in zip(inst, want):
                        if w is None: continue
                        r = ret1s_bps(BN, int(t), lado); COB['q_inst'] += 1
                        if r != r: COB['q_sinbin'] += 1
                        elif r < 0: COB['q_contra'] += 1
                        elif r == 0: COB['q_cero'] += 1
                for nom, rep, exact in VARS:
                    segs = segmentos(inst, want, bsz5, rep, exact)
                    if not segs: continue
                    if nom == 'r0': COB['cotizados_' + brazo] += 1
                    need0 = R.acciones(segs[0][0])
                    for mult in MULTS:
                        if mult != 1.0 and nom not in ('r0', 'r150'): continue
                        for cola, frac in C_['colas'].items():
                            if mult != 1.0 and cola != 'base': continue
                            for lp in (C_['lat_post_ms'], C_['lat_post_cons_ms']):
                                for lc in (C_['lat_cancel_ms'], C_['lat_cancel_cons_ms']):
                                    if mult != 1.0 and (lp, lc) != (C_['lat_post_ms'], C_['lat_cancel_ms']): continue
                                    need = need0 * mult
                                    lleno, coste, t_rel, p_rel, nfill = llenar(segs, need, frac, lp, lc, FIL, FE, t_fin)
                                    row = dict(coin=coin, dia=D, cierre=C, lado=lado, m5=m5id, brazo=brazo, var=nom, rep=rep, exact=int(exact), mult=mult,
                                               cola=cola, lat_post=lp, lat_cancel=lc, n_cotiz=len(segs), need=round(need, 2), lleno=round(lleno, 4),
                                               coste=round(coste, 6), n_fill=nfill, t_rel=t_rel, p_rel=p_rel, gana=gana,
                                               rebate=round(R.CONFIG['rebate'] * R.fee(coste / lleno) * lleno, 6) if lleno > 0 else 0.0,
                                               bsz_rel=None, ret1s_or_bps=None)
                                    if t_rel:
                                        j0 = q5.i(t_rel); row['bsz_rel'] = float(q5.bsz[j0]) if j0 >= 0 else None
                                        r = ret1s_bps(BN, t_rel, lado); row['ret1s_or_bps'] = None if r != r else round(r, 4)
                                    ROWS.append(row)
        except Exception as e:
            COB['errores'] += 1
            print(coin, D, C, type(e).__name__, str(e)[:100], flush=True)
    cols = ['coin', 'dia', 'cierre', 'lado', 'm5', 'brazo', 'var', 'rep', 'exact', 'mult', 'cola', 'lat_post', 'lat_cancel', 'n_cotiz', 'need', 'lleno',
            'coste', 'n_fill', 't_rel', 'p_rel', 'gana', 'rebate', 'bsz_rel', 'ret1s_or_bps']
    with open(fo + '.tmp', 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(ROWS)
    os.replace(fo + '.tmp', fo)
    json.dump(COB, open(OUT + f'v2_cobertura_{coin}_{D}.json', 'w'))
    print(coin, D, 'filas', len(ROWS), COB, flush=True)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
