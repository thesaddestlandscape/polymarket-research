#!/usr/bin/env python3
"""s2 (18-Nov, MECANISMO): cobertura de libro5_ms (B=snapshot, d=price_change, T=trade, G=control): tokens, saltos de seq, suelo rx-ex, precios T, niveles d.
Uso: s2 FICHERO NLINEAS"""
import sys, gzip, numpy as np, collections, json
f, N = sys.argv[1], int(sys.argv[2]); c = collections.Counter(); tok = collections.defaultdict(collections.Counter)
seq_prev = None; gaps = 0; gapsz = []; seqs = []; dT = []; dd = []; pT = collections.Counter(); sz0 = 0; t0 = None; t1 = None; sides = collections.Counter()
with gzip.open(f, 'rt') as fh:
    next(fh)
    for i, l in enumerate(fh):
        if i >= N: break
        p = l.rstrip('\n').split(',')
        t = p[0]; c[t] += 1
        if t == 'G': continue
        try: seq = int(p[-1])
        except: continue
        if seq_prev is not None and seq != seq_prev + 1: gaps += 1; gapsz.append(seq - seq_prev)
        seq_prev = seq
        tk = p[1] if t == 'B' and False else p[2]
        tok[t][tk] += 1
        if t == 'T':
            dT.append(int(p[6]) - int(p[1])); pT[round(float(p[3]) * 10) / 10] += 1
        if t == 'd':
            dd.append(int(p[6]) - int(p[1])); sides[p[3]] += 1
        ts = int(p[1]) 
        t0 = ts if t0 is None else t0; t1 = ts
r = dict(f=f, lineas=c.total(), tipos=dict(c), tokens_B=len(tok['B']), tokens_d=len(tok['d']), tokens_T=len(tok['T']), seq_saltos=gaps, seq_salto_tam_med=float(np.median(gapsz)) if gapsz else None,
 seq_perdidos=int(sum(g - 1 for g in gapsz)), T_rx_menos_ex_p1_p50_p99=[float(np.percentile(dT, q)) for q in (1, 50, 99)] if dT else None,
 d_rx_menos_ex_p1_p50_p99=[float(np.percentile(dd, q)) for q in (1, 50, 99)] if dd else None, T_precio_hist=dict(sorted(pT.items())), d_lados=dict(sides), t_ini=t0, t_fin=t1)
print(json.dumps(r, indent=1))
