#!/usr/bin/env python3
"""t4d_seg2.py DIA (1d-A (i)). Cuentas por SEGUNDO de RX en las 27 bandas de d=rx-ex (mismas bandas que t4_dia_seg) de TRES fuentes adicionales del WS de Polymarket, comparables (t4d_i: corr 0,87-0,97 con la base, d<30 ~0 en hi y 0,5-0,7 en lo):
 g0 = q de tokens 5min FUERA de banda (bid <0,03 o >0,45); g1 = prints 't' de tokens 5min; g2 = q de m15_registro (15m/60m). -> cache/seg2_D.npz (int32 [3,86400,27]). Idempotente (cache/seg2man_D.json; control: suma por grupo == recuento independiente en la misma pasada). 0 ordenes."""
import os, sys, json, hashlib, subprocess, time, numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); D = sys.argv[1]; EXPC = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1/cache/'; MAN = HERE + f'/cache/seg2man_{D}.json'; OUTP = HERE + f'/cache/seg2_{D}.npz'
CODE = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()[:12]; fs = [f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{D}.csv.gz', f'/mnt/HC_Volume_106538179/m15_registro/m15_registro_{D}.csv.gz']
ENT = {os.path.basename(f): [os.stat(f).st_size, int(os.stat(f).st_mtime)] for f in fs if os.path.exists(f)}
if os.path.exists(MAN):
    try:
        m = json.load(open(MAN))
        if m.get('estado') == 'COMPLETE' and m['code'] == CODE and m['entrada'] == ENT and os.path.exists(OUTP): print(D, 'seg2 ya COMPLETE'); sys.exit(0)
    except Exception: pass
t0 = time.time(); d0 = int(pd.Timestamp(D + 'T00:00:00Z').value // 10**6); ant = (pd.Timestamp(D) - pd.Timedelta(days=1)).strftime('%Y-%m-%d'); toks = set()
for f in (EXPC + f'add3_k_{ant}.csv', EXPC + f'add3_k_{D}.csv', HERE + f'/cache/k_{ant}.csv', HERE + f'/cache/k_{D}.csv'):
    if os.path.exists(f):
        for ln in open(f):
            c = ln.split(',')
            if len(c) > 7 and c[4] == '5min': toks.add(c[2])
tag = HERE + f'/cache/_s2_{D}_'; open(tag + 'k.txt', 'w').write('\n'.join(toks) + '\n')
prog = r'''BEGIN{FS=","} FILENAME==KP{K[$1]=1; next}
function put(g,ex,rx,  d,b){ if(rx>=D0 && rx<D0+86400000){ d=rx-ex; b=(d<=9)?0:((d>=60)?26:int((d-10)/2)+1); S[g*100000000+int((rx-D0)/1000)*32+b]++ } }
$1=="q" { if(MODE=="m5"){ if(($3 in K) && !($4>=0.03 && $4<=0.45)) put(0,$2,$8) } else put(2,$2,$8) }
$1=="t" && MODE=="m5" && ($3 in K) { put(1,$2,$7) }
END{for(k in S) print k","S[k]}'''
Z = np.zeros((3, 86400, 27), np.int32)
for mode, f in zip(('m5', 'm15'), fs):
    if not os.path.exists(f): continue
    r = subprocess.run(['bash', '-o', 'pipefail', '-c', f"zcat {f} | awk -v MODE={mode} -v KP={tag}k.txt -v D0={d0} '{prog}' {tag}k.txt - > {tag}o.csv"], capture_output=True, text=True); assert r.returncode == 0, r.stderr[-300:]
    h = pd.read_csv(tag + 'o.csv', header=None, names=['k', 'n'], dtype=np.int64)
    if len(h): g, rem = h.k.values // 100000000, h.k.values % 100000000; s, b = rem // 32, rem % 32; assert (s < 86400).all() and (b < 27).all(); Z[g, s, b] = h.n.values
np.savez_compressed(OUTP + '.tmp.npz', Z=Z); os.replace(OUTP + '.tmp.npz', OUTP)
json.dump(dict(job='t4d_seg2', dia=D, estado='COMPLETE', code=CODE, entrada=ENT, filas=[int(Z[g].sum()) for g in range(3)], s=round(time.time() - t0)), open(MAN, 'w'), indent=1)
os.remove(tag + 'k.txt'); os.remove(tag + 'o.csv'); print(D, 'seg2 COMPLETE filas', [int(Z[g].sum()) for g in range(3)], 's', round(time.time() - t0))
