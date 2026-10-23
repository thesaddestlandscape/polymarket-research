#!/usr/bin/env python3
"""an_hedge.py -- analiza datos/hedge_{b,pop}_D.csv segun PREREG (Parte A). EV = Sum pnl / Sum coste1; Delta vs h0 emparejado;
IC90 bootstrap por dia y por cierre (2000, semilla 20261022); sin 2 mejores dias; sd por unidad; grupo adverso."""
import os, glob, sys
import numpy as np, pandas as pd
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
POL = ['h0', 'ht0', 'htc02', 'htc05', 'htc10', 'hts03', 'hts06', 'hts10', 'hm00', 'hm02', 'hm04', 'hm00_opt', 'hm02_opt', 'hm04_opt']
rng = np.random.default_rng(20261022)
def boot(df, col, g, n=2000, base=None):
    gs = df.groupby(g); num = gs[col].sum().values; den = gs['coste'].sum().values
    if base is not None: num = num - gs[base].sum().values
    k = len(num)
    if k < 2: return (np.nan, np.nan)
    ix = rng.integers(0, k, (n, k)); v = num[ix].sum(1) / den[ix].sum(1)
    return tuple(np.percentile(v, [5, 95]))
def fila(df, col, base=None):
    x = df[list(dict.fromkeys([col, 'h0', 'coste', 'dia', 'cierre']))].dropna()
    num = x[col].sum() - (x[base].sum() if base else 0); ev = num / x.coste.sum()
    gd = x.groupby('dia'); nn = gd[col].sum() - (gd[base].sum() if base else 0); byd = (nn / gd['coste'].sum()).astype(float)
    top2 = byd.sort_values().index[:-2] if len(byd) > 2 else byd.index
    xs = x[x.dia.isin(top2)]
    s2 = (xs[col].sum() - (xs[base].sum() if base else 0)) / xs.coste.sum() if len(xs) else np.nan
    return dict(n=len(x), ev=ev, ic_dia=boot(x, col, 'dia', base=base), ic_cierre=boot(x, col, 'cierre', base=base),
                dias_pos=f"{(byd > 0).sum()}/{len(byd)}", sin2=s2, por_dia=' '.join(f'{v:+.3f}' for v in byd.values),
                sd_u=float((x[col] / x.coste).std()), p_perd50=float(((x[col] / x.coste) < -0.5).mean()))
def bloque(df, titulo, out):
    out.append(f'\n=== {titulo}  (unidades {len(df)}, coste {df.coste.sum():.1f}, dias {sorted(df.dia.unique())})')
    out.append(f"{'pol':10s} {'n':>5s} {'EV':>7s} {'IC90dia':>17s} {'IC90cierre':>17s} {'d+':>4s} {'sin2':>7s} | {'Delta':>7s} {'IC90dia':>17s} {'IC90cierre':>17s} {'d+':>4s} | sd_u  p(<-50%)  hit/fill  por_dia(Delta)")
    for c in POL:
        if c not in df: continue
        a = fila(df, c); b = fila(df, c, base='h0') if c != 'h0' else None
        hit = ''
        for suf in ('_hit', '_f'):
            if c + suf in df: hit = f'{df[c + suf].mean():.2f}'
        if b:
            out.append(f"{c:10s} {a['n']:5d} {a['ev']:+7.3f} ({a['ic_dia'][0]:+.3f},{a['ic_dia'][1]:+.3f}) ({a['ic_cierre'][0]:+.3f},{a['ic_cierre'][1]:+.3f}) {a['dias_pos']:>4s} {a['sin2']:+7.3f} | {b['ev']:+7.3f} ({b['ic_dia'][0]:+.3f},{b['ic_dia'][1]:+.3f}) ({b['ic_cierre'][0]:+.3f},{b['ic_cierre'][1]:+.3f}) {b['dias_pos']:>4s} | {a['sd_u']:.2f} {a['p_perd50']:.2f} {hit:>6s} {b['por_dia']}")
        else:
            out.append(f"{c:10s} {a['n']:5d} {a['ev']:+7.3f} ({a['ic_dia'][0]:+.3f},{a['ic_dia'][1]:+.3f}) ({a['ic_cierre'][0]:+.3f},{a['ic_cierre'][1]:+.3f}) {a['dias_pos']:>4s} {a['sin2']:+7.3f} |  sd_u {a['sd_u']:.2f} p(<-50%) {a['p_perd50']:.2f}  por_dia {a['por_dia']}")
def main():
    out = []
    for modo in ('b', 'pop'):
        fs = sorted(glob.glob(os.path.join(D, f'hedge_{modo}_2026-*.csv')))
        if not fs: continue
        df = pd.concat([pd.read_csv(f) for f in fs])
        if modo == 'b':
            bloque(df, 'B REAL 20-22 Oct (t_ref = deteccion real de B)', out)
            for g, nom in ((1, 'adverso (bid +5 s <= p-0,03)'), (0, 'resto')):
                bloque(df[df.adverso == g], f'B REAL grupo {nom} [descriptivo ex post]', out)
        else:
            bloque(df[df.dia <= '2026-10-19'], 'POBLACION DESC 17-19', out)
            bloque(df[df.dia >= '2026-10-20'], 'POBLACION TEST 20-22', out)
            for g, nom in ((1, 'adverso'), (0, 'resto')):
                bloque(df[(df.adverso == g)], f'POBLACION 17-22 grupo {nom} [descriptivo ex post]', out)
            for c in ('ETH', 'SOL', 'XRP'):
                bloque(df[df.coin == c], f'POBLACION 17-22 {c} [exploratorio]', out)
    txt = '\n'.join(out); print(txt); open(os.path.join(D, 'an_hedge.txt'), 'w').write(txt + '\n')
main()
