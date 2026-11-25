#!/usr/bin/env python3
"""t4d_b_f5.py DIA (paso 1d-B, 17-Nov). Rellenos VIRTUALES de B = G0 de passT_v4 (sello v3, motor dd; RT_v3dd_D.pkl de out_v4 o de cache/passT_out) + rasgos F5 al instante de decision de la regla: t = tf - 60 - 3 ms (p60, c=19, d_proc=3; igual que E1/ADD3),
F5 = log1p(tamano del ask) de la ultima fila q con rx <= t y antiguedad <= 30 s (lib1.Q.feat reutilizada). Tipo B = bid_p60 >= L + 0,0099. token = (coin, fin, lado) desde las filas k (add3_k_{D-1,D}). 0 ordenes. Salida cache/bfill_D.pkl + cache/bfill_man_D.json (atomico, idempotente).
POLITICA CONGELADA (antes de ver resultados): G0 tal cual passT_v4: ordenes en reposo (bid) por mercado-lado en los niveles L y tiempos t_dec del motor, q<=5 acciones, orden viva t_dec+68 ms (constante del motor), cola/relleno = engine_v4.relleno sobre la cinta on-chain, PnL = q*(gana-L)+rebate 0,2*0,07*L(1-L)*q; solo ETH/SOL/XRP (no hay cinta BTC)."""
import os, sys, json, subprocess, hashlib, time, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1'); import lib1
HERE = os.path.dirname(os.path.abspath(__file__)); CA = HERE + '/cache/'; EXPC = lib1.AQ + 'exp1/cache/'; REG = '/mnt/HC_Volume_106538179/m5_registro/'
D = sys.argv[1]; MAN = CA + f'bfill_man_{D}.json'; OUT = CA + f'bfill_{D}.pkl'; CODE = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()[:12]
RTP = [p for p in ('/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/out_v4/RT_v3dd_%s.pkl' % D, CA + 'passT_out/RT_v3dd_%s.pkl' % D) if os.path.exists(p)]
if not RTP: print(D, 'SIN RT (sin cinta/passT)'); sys.exit(2)
st = os.stat(RTP[0]); ENT = dict(rt=RTP[0], bytes=st.st_size, mtime=int(st.st_mtime))
if os.path.exists(MAN):
    try:
        m = json.load(open(MAN))
        if m.get('estado') == 'COMPLETE' and m['code'] == CODE and m['entrada'] == ENT and os.path.exists(OUT): print(D, 'ya COMPLETE'); sys.exit(0)
    except Exception: pass
t0 = time.time(); R = pd.read_pickle(RTP[0]); G = R[R['var'] == 'G0'].copy().reset_index(drop=True); assert len(G) > 0
ant = (pd.Timestamp(D) - pd.Timedelta(days=1)).strftime('%Y-%m-%d'); km = {}
for f in (EXPC + f'add3_k_{ant}.csv', EXPC + f'add3_k_{D}.csv'):
    if os.path.exists(f):
        for ln in open(f):
            c = ln.rstrip('\n').split(',')
            if len(c) > 7 and c[4] == '5min': km[(c[3], int(pd.Timestamp(c[6]).value // 10**9), c[7])] = c[2]
G['tok'] = [km.get((a, int(f), l)) for a, f, l in zip(G.act, G.fin, G.lado)]; miss = int(G.tok.isna().sum()); G = G[G.tok.notna()].reset_index(drop=True)
toks = sorted(set(G.tok)); ids = {t: i for i, t in enumerate(toks)}; tag = CA + f'_bf_{D}_'; open(tag + 'tok.txt', 'w').write('\n'.join(toks) + '\n')
prog = r'''BEGIN{FS=","} FILENAME==KP{K[$1]=1; next} $1=="q" && ($3 in K){ print $3","$8","$4","$5","$6","$7 }'''
r = subprocess.run(['bash', '-o', 'pipefail', '-c', f"zcat {REG}m5_registro_{D}.csv.gz | awk -v KP={tag}tok.txt '{prog}' {tag}tok.txt - > {tag}q.csv"], capture_output=True, text=True); assert r.returncode == 0, r.stderr[-300:]
Qd = pd.read_csv(tag + 'q.csv', header=None, names=['tok', 'r', 'b', 'a', 'tb', 'ta'], dtype={'tok': str, 'r': np.int64, 'b': np.float32, 'a': np.float32, 'tb': np.float32, 'ta': np.float32}, on_bad_lines='skip'); Qd['id'] = Qd.tok.map(ids)
Qo = lib1.Q(Qd.id.values, Qd.r.values, Qd.b.values, Qd.a.values, Qd.tb.values, Qd.ta.values); tid = G.tok.map(ids).values; td = lib1.t_dec(G.tf.values, 60, 3, 0)
f5, bid, cat, _ = Qo.feat(tid, td); G['F5_p60'] = f5; G['bid_p60'] = bid; G['cat_p60'] = cat; G['tipoB'] = np.isfinite(bid) & ((bid - G.L.values) >= 0.0099 - 1e-12); G['tercil'] = lib1.lab(f5)
G.drop(columns=['tok']).to_pickle(OUT + '.tmp'); os.replace(OUT + '.tmp', OUT)
json.dump(dict(job='t4d_b_f5', dia=D, estado='COMPLETE', code=CODE, entrada=ENT, g0_fills=int(len(R[R['var'] == 'G0'])), sin_token=miss, con_F5_ok=int((cat == 0).sum()), filas_q=int(len(Qd)), s=round(time.time() - t0)), open(MAN, 'w'), indent=1)
for s_ in ('tok.txt', 'q.csv'): os.remove(tag + s_)
print(D, 'bfill COMPLETE fills', len(G), 'sin_token', miss, 'cat ok', int((cat == 0).sum()), 'tipoB', int(G.tipoB.sum()), 's', round(time.time() - t0))
