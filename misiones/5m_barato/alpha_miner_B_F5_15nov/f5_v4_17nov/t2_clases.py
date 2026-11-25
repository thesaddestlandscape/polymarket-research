#!/usr/bin/env python3
"""t2_clases.py -- tabla de clases causales por bin de 10 s y dia a partir de cache/hist_D.npz (SPEC_F5_V4_17nov.md). Idempotente (se regenera si cambia hist/codigo). Salida: cache/clases_D.npz
(cls = clase causal por bin B -> aplicar con t=B*10 s en adelante; cls_fut = clase de futuro para validacion; p5/tot de W y mitades) y clases_resumen.json (horas por clase y dia, bins con datos, fallos). Dia sin hist vecino: ceros (-> indet; missing != lo)."""
import os, sys, json, glob, hashlib, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as SC
C = HERE + '/cache/'; dias = sorted(os.path.basename(p)[5:15] for p in glob.glob(C + 'hist_2026-*.npz'))
def prev(d): import datetime as dt; return (dt.date.fromisoformat(d) - dt.timedelta(days=1)).isoformat()
def nxt(d): import datetime as dt; return (dt.date.fromisoformat(d) + dt.timedelta(days=1)).isoformat()
def ld(d):
    p = C + f'hist_{d}.npz'; return np.load(p)['H'] if os.path.exists(p) else None
code = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()[:10] + hashlib.sha256(open(HERE + '/suelo_causal.py', 'rb').read()).hexdigest()[:10]; res = {}
for d in dias:
    H = ld(d); P = ld(prev(d)); N = ld(nxt(d)); hs = hashlib.sha256(H.tobytes()).hexdigest()[:10] + ('P' if P is not None else 'p') + ('N' if N is not None else 'n') + (hashlib.sha256(P[-60:].tobytes()).hexdigest()[:6] if P is not None else '') + (hashlib.sha256(N[:30].tobytes()).hexdigest()[:6] if N is not None else '')
    out = C + f'clases_{d}.npz'
    if os.path.exists(out):
        z = np.load(out)
        if str(z['firma']) == code + hs: cls = z['cls']; res[d] = {k: int((cls == k).sum()) for k in ('lo', 'hi', 'mixta', 'indet')} | dict(bins_con_datos=int((H.sum(1) > 0).sum()), prev=P is not None, nxt=N is not None); continue
    t = SC.tabla_clases(H, prev=P, nxt=N); t['cls'] = t['cls'].astype('U5'); t['cls_fut'] = t['cls_fut'].astype('U5'); np.savez_compressed(out + '.tmp.npz', firma=code + hs, **t); os.replace(out + '.tmp.npz', out)
    res[d] = {k: int((t['cls'] == k).sum()) for k in ('lo', 'hi', 'mixta', 'indet')} | dict(bins_con_datos=int((H.sum(1) > 0).sum()), prev=P is not None, nxt=N is not None)
json.dump(res, open(HERE + '/clases_resumen.json', 'w'), indent=1)
for d, r in res.items(): print(d, r)
