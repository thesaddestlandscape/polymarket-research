#!/usr/bin/env python3
"""dproc_medicion.py -- solo lectura. Mide latencias internas reales: (A) ledger B real 20-23 Oct: t_call0 - t_dec (n=3796); (B) paquete_l B2/B3/B5 (13-Nov): t_send - t_decision (post) y t_send - t_trig_rx (cancel, rx del disparador -> envio). Clase de suelo (detector adoptado / verdad d<30) por segundo."""
import sys, json, glob, numpy as np, pandas as pd, datetime as dt
sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov'); import suelo_causal as SC, t4b_eval as T, t4d_c2 as C
DL = '/root/polymarket-research-datalogs/'; ts = lambda s: dt.datetime.fromisoformat(s).timestamp()
def q(x): x = np.asarray(x, float); return dict(n=len(x), p10=round(np.percentile(x, 10), 1), p50=round(np.percentile(x, 50), 1), p90=round(np.percentile(x, 90), 1)) if len(x) else dict(n=0)
cache = {}
def clase(d, t_s):
    if d not in cache:
        D = T.Dia(d); cache[d] = (SC.estado_lo(SC.lo_crudo(D.S, C.P), C.P), D.vs, int(pd.Timestamp(d + 'T00:00:00Z').timestamp()))
    st, vs, d0 = cache[d]; s = int(np.clip(t_s - d0, 0, 86399)); return ('lo' if st[s] else 'nolo'), ('lo' if vs[s] == 1 else 'hi' if vs[s] == 0 else 'amb')
out = {}
# (A) ledger B real
P = {}; Cl = {}
for ln in open(DL + 'experimento_h47_B_ledger.jsonl'):
    try: e = json.loads(ln)
    except Exception: continue
    if e.get('tipo') == 'puja_post': P[e['oid']] = e
    elif e.get('tipo') == 'post_lat': Cl[e['oid']] = e
rows = []
for o, p in P.items():
    if o in Cl:
        t = p['t_dec']; d = dt.datetime.fromtimestamp(t, dt.timezone.utc).strftime('%Y-%m-%d')
        if '2026-10-20' <= d <= '2026-10-23': rows.append((d, t, (Cl[o]['t_call0'] - t) * 1000, p.get('n_orden')))
A = pd.DataFrame(rows, columns=['d', 't', 'ms', 'n_orden']); cl = [clase(d, t) for d, t in zip(A.d, A.t)]; A['det'] = [c[0] for c in cl]; A['ver'] = [c[1] for c in cl]
out['A_B_real_t_call0_menos_t_dec'] = dict(todos=q(A.ms), por_det={k: q(g.ms) for k, g in A.groupby('det')}, por_verdad={k: q(g.ms) for k, g in A.groupby('ver')}, por_dia={k: q(g.ms) for k, g in A.groupby('d')}, primera_orden=q(A[A.n_orden == 1].ms))
# (B) paquete_l
B = {'post': [], 'cancel': []}
for tanda in ('B2', 'B3', 'B5'):
    for ln in open(DL + f'paquete_l/ensayo_real_{tanda}/ledger.jsonl'):
        e = json.loads(ln); k = e.get('k')
        if k == 'intencion': dec = dict(dec=e['t_decision_ns'], oid=e['oid_local'])
        if k == 'intencion': B.setdefault('_dec', {})[e['oid_local']] = e['t_decision_ns']
        elif k == 'post' and e.get('t_send_ns') and e.get('oid_local') in B['_dec']: B['post'].append((tanda, e['t_send_ns'], (e['t_send_ns'] - B['_dec'][e['oid_local']]) / 1e6))
        elif k == 'cancel' and e.get('t_trig_rx_ns') and e.get('t_send_ns') and e.get('intento') == 1: B['cancel'].append((tanda, e['t_send_ns'], (e['t_send_ns'] - e['t_trig_rx_ns']) / 1e6, (e['t_trig_rx_ns'] - e.get('t_trig_prog_ns', e['t_trig_rx_ns'])) / 1e6, e.get('trig')))
for nm in ('post', 'cancel'):
    D = pd.DataFrame(B[nm]); D['d'] = [dt.datetime.fromtimestamp(t / 1e9, dt.timezone.utc).strftime('%Y-%m-%d') for t in D[1]]
    cl = [clase(d, t / 1e9) for d, t in zip(D.d, D[1])]; D['det'] = [c[0] for c in cl]; D['ver'] = [c[1] for c in cl]; ms = D[2]
    out['B_paquete_l_' + nm] = dict(todos=q(ms), por_tanda={k: q(g[2]) for k, g in D.groupby(0)}, por_det={k: q(g[2]) for k, g in D.groupby('det')}, por_verdad={k: q(g[2]) for k, g in D.groupby('ver')}, **({'trig_rx_menos_prog': q(D[3]), 'triggers': D[4].value_counts().to_dict()} if nm == 'cancel' else {}))
json.dump(out, open(sys.argv[1], 'w'), indent=1); print(json.dumps(out)[:3500])
