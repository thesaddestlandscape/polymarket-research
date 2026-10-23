#!/usr/bin/env python3
"""r3_esc_an.py -- analisis de capacidad y escalado de R3 sobre datos/esc_D.csv.gz (salida de r3_esc_sim.py) y datos/b_real_r3.csv.
EV SIEMPRE ponderado por EUR (sum pnl / sum coste). Maker sin comision, rebate NO sumado. IC90 por remuestreo de DIAS y de CIERRES (fin, las 3 monedas
del mismo cierre = una apuesta). Salida: texto a stdout (se guarda en datos/r3_esc_an.txt) + datos/r3_esc_resumen.json."""
import os, sys, json, glob
import numpy as np, pandas as pd
AQUI = os.path.dirname(os.path.abspath(__file__)); DD = os.path.join(AQUI, 'datos')
PREF = os.environ.get('R3_PREF', 'esc')
X = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(os.path.join(DD, f'{PREF}_2026-10-*.csv.gz')))], ignore_index=True)
X['per'] = np.where(X.dia <= '2026-10-19', 'DESC17-19', 'TEST20-22')
DIAS = sorted(X.dia.unique()); RES = {}
rng = np.random.default_rng(7)

def boot(df, p, c, key, n=4000):
    g = df.groupby(key)[[p, c]].sum(); a, b = g[p].values, g[c].values
    if len(g) < 2 or b.sum() <= 0: return (np.nan, np.nan)
    i = rng.integers(0, len(g), (n, len(g))); e = a[i].sum(1) / np.maximum(b[i].sum(1), 1e-9)
    return (float(np.quantile(e, .05)), float(np.quantile(e, .95)))

def stat(df, p='pnl', c='coste'):
    if len(df) == 0 or df[c].sum() <= 0: return dict(n=len(df), ev=np.nan)
    g = df.groupby('dia')[[p, c]].sum(); o = np.argsort(-g[p].values)[2:]
    sin2 = g[p].values[o].sum() / g[c].values[o].sum() if len(o) and g[c].values[o].sum() > 0 else np.nan
    return dict(n=int(len(df)), coste=float(df[c].sum()), pnl=float(df[p].sum()), ev=float(df[p].sum() / df[c].sum()),
                icd=boot(df, p, c, 'dia'), icc=boot(df, p, c, 'fin'), sin2=float(sin2), dpos=f"{int((g[p] > 0).sum())}/{len(g)}",
                acierto=float(df.gana.mean()), precio=float((df[c].sum() / df['q'].sum()) if 'q' in df else np.nan))

def fmt(s):
    if s.get('ev') is None or s['ev'] != s['ev']: return f"n={s['n']} EV n/a"
    return (f"n={s['n']:5d} coste {s['coste']:8.1f} PnL {s['pnl']:+8.1f} EV {s['ev']:+.3f} IC90d({s['icd'][0]:+.3f},{s['icd'][1]:+.3f}) "
            f"IC90c({s['icc'][0]:+.3f},{s['icc'][1]:+.3f}) sin2 {s['sin2']:+.3f} dias+ {s['dpos']} acierto {s['acierto']:.3f} precio {s['precio']:.3f}")

def fills(pol, K=None, V='V1'):
    """filas rellenas de la politica; q = 5 acc fijo (K=None, como e1/B) o min(K, V) (relleno consistente con el barrido)"""
    s = X[X[f'{pol}_fill'] == 1].copy(); s['obj'] = s[f'{pol}_obj']
    s['q'] = 5.0 if K is None else np.minimum(float(K), s[f'{pol}_{V}'])
    s = s[s.q > 0]
    s['coste'] = s.q * s.obj; s['pnl'] = s.q * (s.gana - s.obj); s['hora'] = (s[f'{pol}_r'] // 1000 % 86400 // 3600).astype(int)
    return s

out = []
def P(*a):
    t = ' '.join(str(x) for x in a); print(t); out.append(t)

P('# R3 capacidad y escalado -- simulador CONS de E1 a ms (ETH/SOL/XRP 5m, 17-22 Oct; 22 hasta ~14:40Z)')
P(f'mercados con banda y desenlace: {len(X)} ; por dia', X.groupby('dia').size().to_dict())
# ---------- 1. capacidad
P('\n## 1. Capacidad (1 puja por mercado-lado, sin tope de 5 vivas)')
cap = X.groupby('dia').agg(mercados=('mid', 'size'), con_r2=('g_r2', lambda v: int((v > 0).sum())), con_r3=('g_r3', lambda v: int((v > 0).sum())),
                           rell_base=('BASE_fill', 'sum'), rell_r2=('R2_fill', 'sum'), rell_r3=('R3_fill', 'sum'))
cap['frac_t_r3'] = X.groupby('dia').apply(lambda d: d.g_r3.sum() / d.g_valid.sum(), include_groups=False)
cap['frac_t_has15'] = X.groupby('dia').apply(lambda d: d.g_has15.sum() / d.g_valid.sum(), include_groups=False)
P(cap.to_string())
full = [d for d in DIAS if d != '2026-10-22']
P('media 17-21 (dias completos): mercados %.0f, con R3 alguna vez %.0f, rellenos BASE %.0f, R2 %.0f, R3 %.0f' % tuple(cap.loc[full, c].mean() for c in ['mercados', 'con_r3', 'rell_base', 'rell_r2', 'rell_r3']))
RES['capacidad_dia'] = {c: float(cap.loc[full, c].mean()) for c in cap.columns}
s3 = fills('R3')
P('rellenos R3/dia por moneda (17-21):', (s3[s3.dia.isin(full)].groupby('act').size() / len(full)).round(1).to_dict())
P('rellenos R3/dia por hora UTC (17-21):', (s3[s3.dia.isin(full)].groupby('hora').size() / len(full)).round(1).to_dict())
P('EUR de puja rellenada R3/dia a 5 acc: %.1f (precio medio %.3f)' % (s3[s3.dia.isin(full)].coste.sum() / len(full), s3.obj.mean()))
# ---------- 2. EV
P('\n## 2. EV (5 acc fijas, como B y e1)')
b = fills('BASE')
for nm, m in (('BASE todos', np.ones(len(b), bool)), ('BASE flag R3 al rellenar', b.b_r3 == 1), ('BASE flag R3 falso', b.b_r3 == 0),
              ('BASE flag R2', b.b_r2 == 1), ('BASE R2 falso', b.b_r2 == 0), ('BASE sin bid15', b.b_has15 == 0)):
    P(f'{nm:28s}', fmt(stat(b[m.values if hasattr(m, "values") else m])))
for pol in ('R2', 'R3'):
    s = fills(pol)
    for per in ('DESC17-19', 'TEST20-22', None):
        ss = s if per is None else s[s.per == per]
        st = stat(ss); P(f'POLITICA {pol} {per or "todo":10s}', fmt(st)); RES[f'pol_{pol}_{per or "todo"}'] = st
P('POLITICA R3 solo 22-Oct (virgen para R2/R3; parcial)', fmt(stat(s3[s3.dia == '2026-10-22'])))
# DIF y placebo (permutacion del flag R3 dentro de dia x moneda entre los rellenos BASE)
def dif(df, f):
    a, c = df[f == 1], df[f == 0]; return a.pnl.sum() / a.coste.sum() - c.pnl.sum() / c.coste.sum()
f = b.b_r3.values.copy(); d0 = dif(b, f); grp = (b.dia + b.act).values; perm = []
for _ in range(2000):
    ff = f.copy()
    for gk in np.unique(grp):
        ii = np.flatnonzero(grp == gk); ff[ii] = rng.permutation(ff[ii])
    perm.append(dif(b, ff))
perm = np.array(perm); P(f'DIF (BASE flag R3 - no R3) = {d0:+.3f}; placebo permutado dia x moneda: media {perm.mean():+.3f}, p95 {np.quantile(perm, .95):+.3f}, p(>=obs) {(perm >= d0).mean():.4f}')
dd = {d: dif(b[b.dia == d], b[b.dia == d].b_r3.values) for d in DIAS}; P('DIF por dia:', {k: round(v, 3) for k, v in dd.items()})
RES['dif_r3'] = dict(obs=d0, placebo_media=float(perm.mean()), p=float((perm >= d0).mean()), por_dia=dd)
# ---------- 3. celdas (EXPLORATORIO, multiplicidad declarada)
P('\n## 3. Celdas de la politica R3 (EXPLORATORIO: 3 monedas + 4 bandas + 4 bloques horarios = 11 celdas, sin correccion)')
for col, bins in (('act', None), ('obj', [0.099, 0.15, 0.20, 0.25, 0.301]), ('hora', [3.5, 8, 12, 16, 20, 24])):
    key = s3[col] if bins is None else pd.cut(s3[col], bins)
    for k, g in s3.groupby(key, observed=True): P(f'  {col} {str(k):14s}', fmt(stat(g)))
# ---------- 4. escalado de tamano
P('\n## 4. Escalado de tamano: relleno(K) = min(K, acciones que atraviesan la puja en 1 s / 5 s desde el primer print)')
for pol in ('BASE', 'R3'):
    s = X[X[f'{pol}_fill'] == 1]
    for V in ('V1', 'V5'):
        v = s[f'{pol}_{V}']
        P(f'{pol} {V}: P(V>=5) {(v >= 5).mean():.3f} P(V>=10) {(v >= 10).mean():.3f} P(V>=20) {(v >= 20).mean():.3f} P(V>=50) {(v >= 50).mean():.3f} mediana {v.median():.1f}')
    for V in ('V1', 'V5'):
        for K in (5, 10, 20, 50):
            st = stat(fills(pol, K, V)); P(f'  {pol} K={K:2d} {V}', fmt(st), f'| acc/dia {fills(pol, K, V).q.sum() / X.dia.nunique():.0f}'); RES[f'K_{pol}_{K}_{V}'] = st
P('corr(tamano del barrido, acierto) y EV por tamano del barrido (R3, V1):')
s = fills('R3', 5, 'V1'); s['V'] = X.loc[s.index, 'R3_V1']
P(f'  Spearman(V1, gana) = {s.V.rank().corr(s.gana.rank()):+.3f}  (BASE: {X[X.BASE_fill == 1].BASE_V1.rank().corr(X[X.BASE_fill == 1].gana.rank()):+.3f})')
for k, g in s.groupby(pd.cut(s.V, [0, 5, 10, 20, 50, 1e9], right=False), observed=True): P(f'  V1 {str(k):14s}', fmt(stat(g)))
# ---------- 5. B real
P('\n## 5. B real (unidades_b.csv, rellenos 20-22 Oct) con los mismos flags en su print (DESCRIPTIVO, n pequeno)')
W = pd.read_csv(os.path.join(DD, 'b_real_r3.csv')); W['fin'] = W.mercado.str.split('-').str[-1].astype(int); W['q'] = W.acc
P('todos', fmt(stat(W)))
P('sin print WS (missing)', fmt(stat(W[W['print'] == 0])))
for nm, m in (('R3 verdadero', W.r3 == 1), ('R3 falso', (W['print'] == 1) & (W.r3 == 0)), ('R2 verdadero', W.r2 == 1), ('R2 falso', (W['print'] == 1) & (W.r2 == 0)),
              ('sin bid15', (W['print'] == 1) & W.lvl15.isna())):
    st = stat(W[m]); P(f'  {nm:14s}', fmt(st)); RES[f'breal_{nm}'] = st
w1 = W[W['print'] == 1]
P(f'B real barrido (acciones al precio de B o mejor, 1 s): P(>=10) {(w1.V1_le >= 10).mean():.2f} P(>=20) {(w1.V1_le >= 20).mean():.2f} mediana {w1.V1_le.median():.0f}; '
  f'estrictamente por debajo: mediana {w1.V1_lt.median():.0f}, P(>=5) {(w1.V1_lt >= 5).mean():.2f}')
for col in ('r3',):
    for k, g in w1.groupby(col): P(f'  B real {col}={k}: por moneda', {a: (len(h), round(h.pnl.sum() / h.coste.sum(), 3)) for a, h in g.groupby('coin')})
json.dump(RES, open(os.path.join(DD, f'r3_{PREF}_resumen.json'), 'w'), indent=1, default=float)
open(os.path.join(DD, f'r3_{PREF}_an.txt'), 'w').write('\n'.join(out) + '\n')
