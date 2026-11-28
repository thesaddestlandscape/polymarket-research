#!/usr/bin/env python3
"""fn5bis_etapa1.py DIA  (27-Nov, engineer 5m barato; CONTRATO_5BIS_EXP5B_27nov.md §1a/§1c). PESADO: por scripts/cron_pesado.sh. 0 ordenes, 0 red. Escribe SOLO en datalogs/exp5bis_27nov/.
Reutiliza SIN modificar capacidad_b_27nov/piloto_m1_m4.py::etapa1 (politica REAL de B-K = K6: DEEP_PEG/H35 con repegado + hooks RF5, motor passT_v4, latencia paquete_l 13-Nov, clase causal v3.4) con OUT redirigido, un solo brazo (base) y sin q_s
contrafactuales, y reutiliza el MISMO motor E (construido una vez) para el replay passT_v4 de las colocaciones del dry-run CXB60 (§1c): MISMAS ordenes (t_dec_rx, t_arr, t_end, L, rem_antes grabados), motor passT_v4;
sensibilidad l1_34 (t_arr = t_dec_rx+34, paquete_l L1). SOLO CONTEOS (EV/pnl precintado hasta la mirada 1: NO se lee res_*.csv.gz ni se calcula pnl). Variantes: CXB35/45/60/100/150/EMP, G0, GEO1 (placebos PLC60_* fuera: declarado)."""
import sys, os, gzip, json, time, pickle, csv, hashlib
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.dirname(HERE) + '/capacidad_b_27nov')
import numpy as np, pandas as pd
import piloto_m1_m4 as P
OUT5 = '/root/polymarket-research-datalogs/exp5bis_27nov/'
DEC = '/root/polymarket-research-datalogs/cxb60_dryrun/'
VARIANTES = ('CXB35', 'CXB45', 'CXB60', 'CXB100', 'CXB150', 'CXBEMP', 'G0', 'GEO1')
_E = {}


def escribe_json(p, d): P.escribe_json(p, d)


def replay_dryrun(dia, E, info):
    """Colocaciones 'seg' del dry-run (dec_DIA) re-ejecutadas con el motor passT_v4 (E.run_segment, mismo que SIM-L). Cuenta por (variante, moneda): colocaciones, rellenos v3 (q>0 del dec), rellenos passT_v4, cambios emparejados."""
    tokidx = E.D.tokidx; filas = []
    with gzip.open(DEC + f'dec_{dia}.csv.gz', 'rt', newline='') as f:
        rd = csv.reader(f); h = next(rd); ix = {c: i for i, c in enumerate(h)}
        for r in rd:
            if r[ix['tipo']] != 'seg' or r[ix['var']] not in VARIANTES: continue
            try:
                filas.append((r[ix['var']], r[ix['coin']], r[ix['tok']], r[ix['mid']], r[ix['lado']], float(r[ix['L']]), int(r[ix['t_dec_rx']]), int(r[ix['t_arr']]), int(r[ix['t_end']]),
                              float(r[ix['rem_antes']]), float(r[ix['q']] or 0.0), int(r[ix['fin']])))
            except (ValueError, IndexError): continue
    cnt = {}; det = []
    for (var, coin, tok, mid, lado, L, t_dec, t_arr, t_end, rem, q3, fin) in filas:
        k = tokidx.get(tok)
        c = cnt.setdefault((var, coin), dict(colocaciones=0, en_motor=0, rellenos_v3=0, rellenos_passT_v4=0, rellenos_passT_v4_l1_34=0, v3_si_v4_no=0, v3_no_v4_si=0, ambos=0))
        c['colocaciones'] += 1; c['rellenos_v3'] += int(q3 > 1e-9)
        if k is None: continue
        c['en_motor'] += 1
        q4 = float(E.run_segment(int(k), float(L), int(t_arr), int(t_end), float(rem), 'BASE')[0])
        q34 = float(E.run_segment(int(k), float(L), int(t_dec + 34), int(t_end), float(rem), 'BASE')[0]) if t_dec + 34 < t_end else 0.0
        c['rellenos_passT_v4'] += int(q4 > 1e-3); c['rellenos_passT_v4_l1_34'] += int(q34 > 1e-3)
        a, b = q3 > 1e-9, q4 > 1e-3
        c['v3_si_v4_no'] += int(a and not b); c['v3_no_v4_si'] += int(b and not a); c['ambos'] += int(a and b)
        if var == 'CXB60': det.append((mid, lado, coin, L, t_arr, t_end, q3, q4, q34, fin, tok))
    return cnt, det, len(filas)


def main(dia):
    os.makedirs(OUT5, exist_ok=True)
    fin_ = OUT5 + f'etapa1_{dia}.json'
    if os.path.exists(fin_) and os.path.exists(OUT5 + f'ordenes_K6_base_{dia}.pkl') and os.path.exists(OUT5 + f'f2_replay_{dia}.json') and os.path.exists(OUT5 + f'status_motor_{dia}.pkl'):
        print('ya hecho', dia); return
    P.OUT = OUT5; P.BRAZOS = {'base': dict()}; P.TAMANOS = ()
    P.puerta(P.RAM_MIN_RUN)
    sys.path.insert(0, P.BK); sys.path.insert(0, P.BKE)
    import siml as SL
    ver = 'v3.4'
    tabla = SL.tabla_clases_dia(dia, ver, '/root/polymarket-research-dev-bk/experimentos/5m_barato/b_k_ejecutor/suelo_p5')
    pickle.dump(tabla, open(OUT5 + f'clases_causales_v34_{dia}.pkl', 'wb'))
    import experimento_maker_bk as BKm
    sys.path.insert(0, str(BKm.D_RF5)); sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim')
    import eng_v5 as EV
    orig = EV.build
    def build_cache(d):
        r = orig(d); _E['E'], _E['info'] = r; return r
    EV.build = build_cache
    t0 = time.time(); P.etapa1(dia)                                      # K6 base -> ordenes_K6_base_DIA.pkl, etapa1_DIA.json
    E, info = _E['E'], _E['info']; P.guarda_ram('f2 replay')
    R = pd.read_pickle(OUT5 + f'ordenes_K6_base_{dia}.pkl'); st = []
    for r in R.itertuples():                                              # estado del motor por orden (para clasificar FN): libro a t_arr y status de run_segment (seria_taker = ask<=L al llegar: no armable como maker)
        b = E.D.book(int(r.k), int(r.t_arr)); res_ = E.run_segment(int(r.k), float(r.L), int(r.t_arr), int(r.t_end), float(r.size), 'BASE')
        st.append((float(b[0]) if b is not None else np.nan, float(b[1]) if b is not None else np.nan, float(res_[0]), res_[2]))
    pd.DataFrame(st, columns=['bid_arr', 'ask_arr', 'q_motor', 'status_motor']).to_pickle(OUT5 + f'status_motor_{dia}.pkl')
    cnt, det, n = replay_dryrun(dia, E, info)
    pd.DataFrame(det, columns=['mid', 'lado', 'coin', 'L', 't_arr', 't_end', 'q_v3', 'q_v4', 'q_v4_l1_34', 'fin', 'token']).to_pickle(OUT5 + f'f2_cxb60_seg_{dia}.pkl')
    d = dict(dia=dia, job='exp5bis f2_replay (CONTRATO_5BIS §1c)', filas_seg_replay=n, variantes=list(VARIANTES), motor_info=info, politica='MISMAS ordenes del dry-run (t_dec_rx,t_arr,t_end,L,rem_antes grabados) re-ejecutadas con passT_v4; NO re-decide ni aplica L_cancel paquete_l; sensibilidad l1_34',
             solo_conteos='sin pnl/EV (precintado hasta la mirada 1)', por_variante_moneda={f'{v}|{c}': x for (v, c), x in sorted(cnt.items())}, segundos=round(time.time() - t0, 1), generado=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    escribe_json(OUT5 + f'f2_replay_{dia}.json', d); print('fn5bis_etapa1 OK', dia, round(time.time() - t0))


if __name__ == '__main__':
    main(sys.argv[1])
