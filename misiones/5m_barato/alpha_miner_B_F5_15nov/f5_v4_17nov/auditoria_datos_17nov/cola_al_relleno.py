#!/usr/bin/env python3
"""Solo lectura. Estado del libro del token propio justo antes del relleno real (fila q con ex<=tm3-1) para los 202 rellenos reales de B 20-23 Oct: bid vs L y tamano en el top. Clasifica FN|SOLO frente a TP."""
import sys, subprocess, numpy as np, pandas as pd
X = pd.read_pickle('/root/polymarket-research/experimentos/5m_barato/replay_brecha_B_16nov/fn_16nov/tomadores.pkl')
X = X[X.tm3.notna()].copy(); X['tm3'] = X.tm3.astype('int64'); out = []
for d, g in X.groupby('dia'):
    tk = f'/tmp/claude-0/cola_tok_{d}.txt'; open(tk, 'w').write('\n'.join(sorted(set(g.tok.astype(str)))) + '\n')
    prog = r'''BEGIN{FS=","} FILENAME==KP{K[$1]=1; next} $1=="q" && ($3 in K){ print $2","$3","$4","$5","$6","$7","$8 }'''
    r = subprocess.run(['bash', '-o', 'pipefail', '-c', f"zcat /mnt/HC_Volume_106538179/m5_registro/m5_registro_{d}.csv.gz | awk -v KP={tk} '{prog}' {tk} - > /tmp/claude-0/cola_q_{d}.csv"], capture_output=True, text=True); assert r.returncode == 0, r.stderr[-300:]
    Q = pd.read_csv(f'/tmp/claude-0/cola_q_{d}.csv', header=None, names=['ex', 'tok', 'b', 'a', 'tb', 'ta', 'rx'], dtype={'tok': str}, on_bad_lines='skip').sort_values('ex')
    by = {k: v for k, v in Q.groupby('tok')}
    for r_ in g.itertuples():
        q = by.get(str(r_.tok)); 
        if q is None: out.append((r_.oid, None, None, None)); continue
        i = np.searchsorted(q.ex.values, r_.tm3 - 1, side='right') - 1
        if i < 0: out.append((r_.oid, None, None, None)); continue
        row = q.iloc[i]; out.append((r_.oid, row.b, row.tb, (r_.tm3 - row.ex)))
Y = pd.DataFrame(out, columns=['oid', 'b_pre', 'tb_pre', 'edad_ms']); X = X.merge(Y, on='oid', how='left'); X['tp'] = X.v3d_BASE_f_q >= 1e-3
X['pos'] = np.where(X.b_pre.isna(), 'sin_fila', np.where(X.b_pre > X.L + 0.0049, 'bid_arriba', np.where(X.b_pre >= X.L - 0.0049, 'en_top', 'bid_abajo')))
X['cola_pre'] = np.where(X.pos == 'en_top', X.tb_pre - X.size, np.nan)
def r(x): return round(float(x), 1)
for nm, g in (('TP', X[X.tp]), ('FN|SOLO', X[~X.tp & (X.estructura == 'SOLO')]), ('FN|otros', X[~X.tp & (X.estructura != 'SOLO')])):
    print(nm, len(g), g.pos.value_counts().to_dict(), '| edad fila q (ms) mediana', r(g.edad_ms.median()), '| en_top: tamano del top - propio (acc) p10/p50/p90', g.cola_pre.quantile([.1, .5, .9]).round(1).tolist(), '| cola visible al colocar mediana', r(g.cola_x.median()))
X[['oid', 'dia', 'coin', 'L', 'estructura', 'tp', 'pos', 'b_pre', 'tb_pre', 'cola_pre', 'cola_x', 'edad_ms']].to_csv('cola_al_relleno.csv', index=False)
