#!/usr/bin/env python3
"""diag_fn_motor.py DIA  (27-Nov): para cada FN nominal de fn5bis_dia_DIA.json reconstruye con el MISMO motor passT_v4 (eng_v5.build + E.run_segment) que ve en la orden: libro a t_arr, prints del tape en [t_arr,t_end], q. Solo lectura, 0 ordenes."""
import sys, json, os
sys.dont_write_bytecode = True
dia = sys.argv[1]; O = '/root/polymarket-research-datalogs/exp5bis_27nov/'
BK = '/root/polymarket-research-dev-bk'; sys.path.insert(0, BK); sys.path.insert(0, BK + '/experimentos/5m_barato/b_k_ejecutor')
import experimento_maker_bk as BKm
sys.path.insert(0, str(BKm.D_RF5)); sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim')
import pandas as pd, numpy as np, eng_v5 as EV
E, info = EV.build(dia)
R = pd.read_pickle(O + f'ordenes_K6_base_{dia}.pkl'); d = json.load(open(O + f'fn5bis_dia_{dia}.json')); out = []
for f in d['fn_lista']:
    for _, r in R[(R.mid == f['mid']) & (R.lado == f['lado'])].iterrows():
        if not (r.t_arr - 300 <= f['rx'] <= r.t_end + 300): continue
        k = int(r.k); L = float(r.L); b = E.D.book(k, int(r.t_arr)); pr = E.tape.get(k, L, int(r.t_arr), int(r.t_end))
        q = E.run_segment(k, L, int(r.t_arr), int(r.t_end), float(r['size']), 'BASE')
        out.append(dict(clase=f['clase_fn'], mid=f['mid'], coin=f['coin'], L=L, t_arr=int(r.t_arr), t_end=int(r.t_end), ev_rx=f['rx'], book_en_t_arr=[float(x) for x in b[:3]] if b is not None else None,
                        prints_tape_en_ventana=[(int(t), float(p), float(s)) for t, p, s in zip(*[np.asarray(x)[:12] for x in pr])] if pr is not None else None, run_segment=[float(q[0]), q[1], q[2]]))
json.dump(out, open(O + f'diag_fn_motor_{dia}.json', 'w'), indent=1, default=str); print('diag OK', len(out))
