#!/usr/bin/env python3
"""e3_extrae.py -- E3 (ADDENDUM1): filas q (ex, tok, bid, ask, szb, sza, rx; SIN filtro de banda) de los tokens de las ordenes de B (ordenes_b.csv, 3.796) y de sus fills, dias 20-23 Oct, de m5_registro. Una pasada zcat|awk por dia.
Salida idempotente cache/bqall_D.csv.gz. Solo lectura. nice 19, ulimit lo pone el lanzador."""
import os, sys, subprocess; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib1 import *
O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}); M = pd.read_pickle(EXP + 'B_fills_v3.pkl')
for d in ('2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23'):
    out = CACHE + f'bqall_{d}.csv.gz'
    if os.path.exists(out) and os.path.getsize(out) > 1000: print(d, 'ya existe'); continue
    toks = sorted(set(O[O.dia == d].tok) | set(M[M.dia == d].tok_x)); tf = CACHE + f'bqall_tok_{d}.txt'; open(tf, 'w').write('\n'.join(toks) + '\n')
    cmd = (f"zcat {REG}m5_registro_{d}.csv.gz | awk -F, -v tf={tf} 'BEGIN{{while((getline l<tf)>0)t[l]}} $1==\"q\"&&($3 in t){{print $2\",\"$3\",\"$4\",\"$5\",\"$6\",\"$7\",\"$8}}' | gzip -c > {out}.tmp && mv {out}.tmp {out}")
    r = subprocess.run(['bash', '-o', 'pipefail', '-c', cmd], capture_output=True, text=True); assert r.returncode == 0, r.stderr[-300:]
    os.remove(tf); print(d, 'tokens', len(toks), 'bytes', os.path.getsize(out), flush=True)
estado_fase('E3x', 'COMPLETE')
