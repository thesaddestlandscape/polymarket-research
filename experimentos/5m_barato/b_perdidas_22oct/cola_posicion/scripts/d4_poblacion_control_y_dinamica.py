#!/usr/bin/env python3
"""d4_poblacion_control_y_dinamica.py -- PREREG_CONTROL partes 1 (poblacion) y 3 (dinamica). Poblacion: M_exit evento (print) vs 3 controles emparejados por (mercado,token,nivel,+-60 s), ponderado por EUR del
print, IC90 por dia y por cierre, placebo (intercambio de etiqueta dentro de cada par) por banda y moneda. Dinamica: cancelaciones brutas por accion tradeada por banda x moneda x rango de nivel x T.
Salida datos/poblacion_control.txt"""
import os, glob, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_posicion/'
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_CONTROL.md'), 'rb').read()).hexdigest().startswith('37f710e298664193')
rng = np.random.default_rng(20261022); out = []
def P(*a): out.append(' '.join(str(x) for x in a))
E = pd.concat([pd.read_csv(f, low_memory=False, usecols=lambda c: c in ('grp', 's1ok', 'mid', 'act', 'L', 'fin', 'dia', 'r', 'q', 'banda', 'T', 'size', 'S1000', 'S150', 'cons', 'pair', 'bestL')) for f in sorted(glob.glob(DL + 'l2_eventos_*.csv.gz'))], ignore_index=True)
E['s1ok'] = E.s1ok.fillna(1)
E = E[E.s1ok == 1].copy(); E['exit'] = ((E.S1000 >= 5) & ((E.S1000 - E.cons - E.S150) >= 0.8 * E.S1000)).astype(int)
E['alone'] = (E.S150 <= 0.5).astype(int); E['mid'] = E.mid.astype(str)
Ev = E[E.grp == 'E'].copy(); Ct = E[E.grp == 'C'].copy(); Ev['key'] = Ev.mid + '|' + Ev.L + '|' + Ev.q.astype(str) + '|' + Ev.r.astype(str)
Ct['key'] = Ct.mid + '|' + Ct.L + '|' + Ct.q.astype(str) + '|' + Ct.pair.astype(int).astype(str)
Ev['w'] = Ev['size'] * Ev.q / 1000
g = Ct.groupby('key').agg(c_exit=('exit', 'mean'), c_alone=('alone', 'mean'), nc=('exit', 'size')).reset_index()
Pm = Ev.merge(g, on='key', how='inner')
P(f'Eventos (prints con S(q,t-1000)>=5) {len(Ev)}; con >=1 control emparejado {len(Pm)}; controles {len(Ct)}')
def stat(df, col, lab=None):
    a = df[col].values; b = df['c_' + col].values; w = df.w.values
    if lab is not None: a2 = np.where(lab, b, a); b2 = np.where(lab, a, b); a, b = a2, b2
    return np.average(a, weights=w) - np.average(b, weights=w)
def boot(df, col, key):
    gi = {c: x.index.values for c, x in df.groupby(key)}; cl = list(gi); v = []
    for _ in range(1000):
        s = df.loc[np.concatenate([gi[c] for c in rng.choice(cl, len(cl))])]; v.append(stat(s, col))
    return np.percentile(v, [5, 95])
for bd in ('A', 'B'):
    for act in (None, 'ETH', 'SOL', 'XRP'):
        s = Pm[Pm.banda == bd] if act is None else Pm[(Pm.banda == bd) & (Pm.act == act)]
        if len(s) < 100: continue
        s = s.reset_index(drop=True)
        for col in ('exit', 'alone'):
            obs = stat(s, col); icc = boot(s, col, 'fin'); icd = boot(s, col, 'dia')
            plc = np.array([stat(s, col, rng.random(len(s)) < 0.5) for _ in range(1000)]); p = float((plc >= obs).mean())
            mE = np.average(s[col], weights=s.w); mC = np.average(s['c_' + col], weights=s.w)
            P(f'banda {bd} {"TODAS" if act is None else act} {col.upper():5s}: evento {mE:.3f} vs control {mC:.3f} Delta {obs:+.3f} (n={len(s)}) IC90 cierre ({icc[0]:+.3f},{icc[1]:+.3f}) dia ({icd[0]:+.3f},{icd[1]:+.3f}) placebo p={p:.3f}')
# dinamica
A = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(DL + 'l2_agregado_*.csv.gz'))], ignore_index=True); A['prints'] = A.prints.fillna(0)
P('\nDINAMICA: acciones quitadas del nivel (bajadas brutas) por accion tradeada, T 50-290 s; ratio-1 = cancelaciones/retiradas netas por cada accion consumida por trades')
g = A.groupby(['banda', 'act', 'rk', 'half']).agg(dec=('dec', 'sum'), inc=('inc', 'sum'), prints=('prints', 'sum'), upd=('n', 'sum')).reset_index()
g['bajadas_por_trade'] = g.dec / g.prints.clip(lower=1e-9); g['altas_por_trade'] = g.inc / g.prints.clip(lower=1e-9); g['cancel_share'] = 1 - g.prints / g.dec.clip(lower=1e-9)
P(g.round(2).to_string(index=False))
t = A.groupby(['banda']).agg(dec=('dec', 'sum'), inc=('inc', 'sum'), prints=('prints', 'sum'), upd=('n', 'sum')); t['cancel_share'] = 1 - t.prints / t.dec; t['bajadas_por_trade'] = t.dec / t.prints
P('\nTOTAL por banda:'); P(t.round(2).to_string())
d = A.groupby(['banda', 'dia']).agg(dec=('dec', 'sum'), prints=('prints', 'sum')); d['cancel_share'] = 1 - d.prints / d.dec; P('\nPor dia:'); P(d.round(3).to_string())
open(os.path.join(D, 'poblacion_control.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
