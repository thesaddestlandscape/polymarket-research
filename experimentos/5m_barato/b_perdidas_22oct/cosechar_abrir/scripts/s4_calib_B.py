#!/usr/bin/env python3
"""s4: CALIBRACION del modelo de cola con las ordenes REALES de B (wallet dedicada, ETH/SOL/XRP 5m, 20-22 Oct).
Ancla: para cada oid del ledger experimento_h47_B_ledger.jsonl (intencion_post, post_lat, post_ok.cola REST, intencion_cancel, lectura/verificada f)
se simula la misma orden (precio, hora de entrada en libro, hora de cancelacion) sobre el flujo WS por RECEPCION (msdata, ms_D.npz de b_perdidas_22oct/salida)
con cola_adelante = F * cola_REST y se compara P(relleno) simulada vs real. Variantes de conteo de operaciones: own (solo SELL del token y BUY del contrario,
equivalente), solo_own (solo operaciones del propio token), solo_opp. Solo lectura. Salida: ../datos/s4_calib_B.txt/.csv"""
import sys, json, collections, os, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/salida/scripts')
import msdata as M
LED = '/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
orders = {}
for ln in open(LED):
    try: r = json.loads(ln)
    except Exception: continue
    o = r.get('oid'); t = r.get('tipo')
    if not o: continue
    d = orders.setdefault(o, {})
    if t == 'intencion_post': d.update(slug=r['slug'], tok=r['tok'], lado=r['lado'], precio=r['precio'], size=r['size'], ts_int=r['ts'])
    elif t == 'post_lat': d.update(t_call0=r['t_call0'], t_ret=r['t_ret'], ms=r['ms'])
    elif t == 'post_ok': d.update(cola=r.get('cola'), metodo=r.get('metodo_cola'))
    elif t == 'intencion_cancel': d.setdefault('ts_cancel', r['ts'])
    elif t in ('lectura', 'verificada') and r.get('f') is not None: d['f'] = max(d.get('f', 0.0), float(r['f']))
    elif t == 'puja_post': d.update(T=r.get('T'), coin=r.get('coin'))
df = pd.DataFrame.from_dict(orders, orient='index')
df = df[df.t_ret.notna() & df.ts_cancel.notna() & df.tok.notna()].copy()
df['t_cancel'] = pd.to_datetime(df.ts_cancel, utc=True).astype('int64') // 10**6 if False else pd.to_datetime(df.ts_cancel, utc=True).map(lambda x: x.timestamp())
df['f'] = df.f.fillna(np.nan)
print('ordenes con post+cancel', len(df), ' con lectura f', df.f.notna().sum(), ' real relleno>0', (df.f > 0).sum())
df['dia'] = pd.to_datetime(df.t_ret, unit='s', utc=True).dt.strftime('%Y-%m-%d')
cache = {}
def dia(d):
    if d not in cache:
        p = os.path.join(M.DD, f'ms_{d}.npz')
        cache[d] = M.Dia(d) if os.path.exists(p) else None
    return cache[d]
def sim(D, k, precio, size, t0, t1, Q0, modo):
    """devuelve (acc_llena, t_primer_relleno) con operaciones por recepcion en (t0, t1]. Equivalencia: SELL del token a p, o BUY del contrario a p' => SELL a 1-p'."""
    lleno = 0.0; vol = 0.0; tf = None; lvl = 0.0
    ev = []
    if modo in ('ambas', 'solo_own'):
        t, v = D.trades(k, t0, t1)
        for a, b in zip(t, v):
            if b[1] == 0: ev.append((a, round(float(b[0]), 4), float(b[2])))
    if modo in ('ambas', 'solo_opp'):
        ko = D.idx.get((str(D.tmap[k][0]), str(D.tmap[k][1]), int(pd.Timestamp(str(D.tmap[k][3])).timestamp()), 'NO' if str(D.tmap[k][4]) == 'YES' else 'YES'))
        if ko is not None:
            t, v = D.trades(ko, t0, t1)
            for a, b in zip(t, v):
                if b[1] == 1: ev.append((a, round(1.0 - float(b[0]), 4), float(b[2])))
    ev.sort()
    for a, pe, sz in ev:
        falta = size - lleno
        if falta <= 1e-9: break
        if pe < precio - 1e-6: n = min(falta, sz)
        elif abs(pe - precio) < 1e-6:
            vol += sz; cand = max(0.0, vol - Q0); new = min(cand, size - (lleno - lvl)); n = new - lvl; lvl = max(lvl, new)
        else: continue
        if n > 1e-12:
            if tf is None: tf = a
            lleno += n
    return lleno, tf
rows = []
FS = [0.0, 0.25, 0.5, 0.75, 1.0]
EXT = [30, 500, 1000, 1500]
for r in df.itertuples():
    D = dia(r.dia)
    if D is None: continue
    if not hasattr(D, 'tokix'): D.tokix = {str(t): i for i, t in enumerate(D.tokens)}
    k = D.tokix.get(str(r.tok))
    if k is None: continue
    cola = r.cola if (r.cola is not None and r.cola == r.cola) else 0.0
    t0 = int(r.t_ret * 1000)
    for ext in EXT:
        t1 = int(r.t_cancel * 1000) + ext
        for modo in ('ambas', 'solo_opp'):
            for F in FS:
                a, tf = sim(D, k, float(r.precio), float(r.size), t0, t1, F * cola, modo)
                rows.append((r.Index, r.dia, r.precio, r.size, cola, r.f, ext, modo, F, a, (tf - t0) / 1000 if tf else np.nan, (t1 - t0) / 1000))
R = pd.DataFrame(rows, columns=['oid', 'dia', 'precio', 'size', 'cola', 'f_real', 'ext', 'modo', 'F', 'acc_sim', 't_fill_sim', 'vida'])
R.to_csv(os.path.join(OUT, 's4_calib_B.csv.gz'), index=False)
R = R[R.f_real.notna()].copy()
R['real'] = (R.f_real > 0).astype(float); R['sim'] = (R.acc_sim > 0).astype(float)
def met(d):
    tp = ((d.sim == 1) & (d.real == 1)).sum()
    return pd.Series({'n': len(d), 'P_real': d.real.mean(), 'P_sim': d.sim.mean(), 'recall': tp / max(1, d.real.sum()), 'prec': tp / max(1, d.sim.sum()),
                      'acc_real': d.f_real.sum(), 'acc_sim': d.acc_sim.sum(), 'brier': ((d.sim - d.real) ** 2).mean()})
g = R.groupby(['modo', 'ext', 'F']).apply(met)
pd.set_option('display.width', 220); pd.set_option('display.max_rows', 200)
print(g.round(3))
open(os.path.join(OUT, 's4_calib_B.txt'), 'w').write(g.round(3).to_string())
