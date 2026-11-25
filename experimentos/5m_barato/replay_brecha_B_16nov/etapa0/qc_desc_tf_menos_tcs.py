#!/usr/bin/env python3
"""qc_desc_tf_menos_tcs.py -- DESCRIPTIVO POST-HOC (no preregistrado, no decide nada) de Q-C (BF5-REPLAY-COLOC-v1), escrito DESPUES de ver
QC_brecha_nivel_mix.json para explicar por que la fraccion cerrada es una funcion escalon de delta (fijo_60 = estres_111 = todas las filas +20,5).
Mide, en los rellenos simulados afectables por la correccion (q_s > 0 y t_cancel_int conocido), la distancia x = tf_sim - t_cancel_int (ms) por
clase TP/FP: un relleno se anula con delta si x > delta. Misma muestra que Q-C: importa SOLO carga() de qc_brecha_nivel_mix.py (copia literal ya
verificada por AST; ese modulo no ejecuta nada al importarse). SOLO LECTURA.
Uso: ulimit -v 3000000; nice -n 19 ionice -c3 /usr/bin/python3 -I qc_desc_tf_menos_tcs.py  -> QC_desc_tf_menos_tcs.json"""
import os, sys, json, hashlib, datetime as dt
import numpy as np
E = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, E)
import qc_brecha_nivel_mix as Q


def main():
    R = Q.carga(); af = (R.q_s > 1e-9) & R.tcs.notna(); A = R[af].copy()
    A['x'] = A.v3d_BASE_f_tf.astype(float) - A.tcs * 1000.0; A['clase'] = np.where(A.q_r > 1e-9, 'TP', 'FP')
    out = dict(job='qc_desc_tf_menos_tcs', aviso='POST-HOC descriptivo, no preregistrado; no decide nada', codigo_sha256=hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest(),
               fuente_muestra='qc_brecha_nivel_mix.carga() (= brecha_nivel_v3.carga)', n_afectables=int(len(A)), n_sim_sin_tcs=int(((R.q_s > 1e-9) & R.tcs.isna()).sum()),
               generado_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    for c in ('TP', 'FP'):
        x = np.sort(A.x[A.clase == c].to_numpy())
        out[c] = dict(n=int(len(x)), x_ms_ordenado=[round(float(v), 1) for v in x],
                      en_tramos=dict(le_0=int((x <= 0).sum()), de_0_a_30=int(((x > 0) & (x <= 30)).sum()), de_30_a_36=int(((x > 30) & (x <= 36)).sum()),
                                     de_36_a_46=int(((x > 36) & (x <= 46)).sum()), de_46_a_60=int(((x > 46) & (x <= 60)).sum()), de_60_a_111=int(((x > 60) & (x <= 111)).sum()), gt_111=int((x > 111).sum())))
    json.dump(out, open(E + 'QC_desc_tf_menos_tcs.json', 'w'), indent=1)
    print(json.dumps({c: out[c]['en_tramos'] for c in ('TP', 'FP')}))


if __name__ == '__main__':
    main()
