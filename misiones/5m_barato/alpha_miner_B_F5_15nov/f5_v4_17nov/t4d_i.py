#!/usr/bin/env python3
"""t4d_i.py DIA (1d-A (i), 17-Nov): COMPARABILIDAD del suelo rx-ex entre FUENTES del WS de Polymarket, por bin de 10 s (n y n con d<30 ms): s0 base (q, tokens 5min, bid [0,03;0,45]); s1 q tokens 5min FUERA de banda; s2 prints 't' de tokens 5min (ex=col2, rx=col7); s3 q de m15_registro (15m/60m, otras conexiones).
Salida cache/fuentes_D.npz. Una pasada zcat|awk por fichero; lectura; 0 ordenes."""
import os, sys, subprocess, numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); D = sys.argv[1]; EXPC = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1/cache/'
d0 = int(pd.Timestamp(D + 'T00:00:00Z').value // 10**6); ant = (pd.Timestamp(D) - pd.Timedelta(days=1)).strftime('%Y-%m-%d'); toks = set()
for f in (EXPC + f'add3_k_{ant}.csv', EXPC + f'add3_k_{D}.csv', HERE + f'/cache/k_{ant}.csv', HERE + f'/cache/k_{D}.csv'):
    if os.path.exists(f):
        for ln in open(f):
            c = ln.split(',')
            if len(c) > 7 and c[4] == '5min': toks.add(c[2])
tag = HERE + f'/cache/_fu_{D}_'; open(tag + 'k.txt', 'w').write('\n'.join(toks) + '\n')
prog = r'''BEGIN{FS=","} FILENAME==KP{K[$1]=1; next}
function put(s,ex,rx){ if(rx>=D0 && rx<D0+86400000){ b=int((rx-D0)/10000); N[s","b]++; if(rx-ex<30) Lw[s","b]++ } }
$1=="q" { if(MODE=="m5"){ if($3 in K){ if($4>=0.03 && $4<=0.45) put(0,$2,$8); else put(1,$2,$8) } } else put(3,$2,$8) }
$1=="t" && MODE=="m5" && ($3 in K) { put(2,$2,$7) }
END{for(k in N) print k","N[k]","Lw[k]+0}'''
H = np.zeros((4, 8640, 2), np.int64)
for mode, f in (('m5', f'/mnt/HC_Volume_106538179/m5_registro/m5_registro_{D}.csv.gz'), ('m15', f'/mnt/HC_Volume_106538179/m15_registro/m15_registro_{D}.csv.gz')):
    if not os.path.exists(f): print('sin', f); continue
    r = subprocess.run(['bash', '-o', 'pipefail', '-c', f"zcat {f} | awk -v MODE={mode} -v KP={tag}k.txt -v D0={d0} '{prog}' {tag}k.txt - > {tag}o.csv"], capture_output=True, text=True); assert r.returncode == 0, r.stderr[-300:]
    for ln in open(tag + 'o.csv'):
        s, b, n, l = ln.strip().split(','); H[int(s), int(b)] = (int(n), int(l))
np.savez_compressed(HERE + f'/cache/fuentes_{D}.npz', H=H); os.remove(tag + 'k.txt'); os.remove(tag + 'o.csv'); print(D, 'fuentes filas por fuente', H[:, :, 0].sum(1).tolist())
