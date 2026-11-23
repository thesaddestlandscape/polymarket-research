#!/usr/bin/env python3
"""H6 (chief 23-Nov): ¿los huecos de stream contaminan F5? Marca ordenes (t_dec), rellenos (tf) y lados (t0) dentro de un hueco >15 s de su conexion coin#5min o hasta 15 s despues.
Modo 'proxy' = causas conocidas deterministas (restart_ram 03:20/10:20/22:20Z +50 s todas; XRP 08/12/16Z primeros 115 s); modo 'real' = out/gaps/gaps_D.txt (hbgap.py)."""
import sys, glob, json, numpy as np, pandas as pd
modo = sys.argv[1] if len(sys.argv) > 1 else 'proxy'; rng = np.random.default_rng(20261123); POST = 15000
R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob('../r1v2_eval/out_p0/p0_ordenes_2026-11-*.pkl'))], ignore_index=True); R = R[R.dia >= '2026-11-05'].copy()
G = []  # (dia, coin, ini, fin)
for d in sorted(R.dia.unique()):
    d0 = int(pd.Timestamp(d, tz='UTC').value // 10**6)
    if modo == 'proxy':
        for hh in (3, 10, 22):
            for c in ('eth', 'sol', 'xrp'): G.append((d, c, d0 + (hh*3600 + 20*60)*1000, d0 + (hh*3600 + 20*60 + 50)*1000))
        for hh in (8, 12, 16): G.append((d, 'xrp', d0 + hh*3600*1000, d0 + (hh*3600 + 115)*1000))
    else:
        for l in open(f'out/gaps/gaps_{d}.txt'):
            a = l.split()
            if len(a) == 5 and a[2].isdigit() and a[4] != '-1': G.append((d, a[1].split('#')[0].lower(), int(a[2]), int(a[3])))
G = pd.DataFrame(G, columns=['dia', 'coin', 'ini', 'fin'])
def marca(t, dia, coin):
    out = np.zeros(len(t), bool); t = np.asarray(t, float)
    for (d, c), g in G.groupby(['dia', 'coin']):
        m = (dia == d) & (coin == c)
        if not m.any(): continue
        x = t[m]; hit = np.zeros(len(x), bool)
        for a, b in zip(g.ini, g.fin): hit |= (x >= a) & (x <= b + POST)
        out[m] = hit
    return out
R['m_dec'] = marca(R.t_dec.values, R.dia.values, R.coin.values)
R['m_fill'] = (R.q > 0) & marca(R.tf.values, R.dia.values, R.coin.values)
R['grupo'] = np.where(R.tercil == 'alto', 'alto', 'bm')
def diff(F, col):
    A = F[F[col] == 'bm']; B = F[F[col] == 'alto']
    return A.pnl.sum()/A.cost.sum() - B.pnl.sum()/B.cost.sum() if A.cost.sum() > 0 and B.cost.sum() > 0 else np.nan
def boot(F, col='grupo', K=2000):
    D = sorted(F.dia.unique()); idx = {d: F.index[F.dia == d] for d in D}
    v = np.array([diff(F.loc[np.concatenate([idx[D[j]] for j in rng.integers(0, len(D), len(D))])], col) for _ in range(K)]); v = v[np.isfinite(v)]
    return dict(diff=round(diff(F, col), 4), lo=round(np.percentile(v, 5), 4) if len(v) else None, hi=round(np.percentile(v, 95), 4) if len(v) else None, n=int(len(F)), n_alto=int((F[col] == 'alto').sum()), dias=len(D))
res = dict(modo=modo, n_huecos=int(len(G)), huecos_por_moneda=G.groupby('coin').size().to_dict())
for b, Rv in R.groupby('bloq'):
    F = Rv[Rv.q > 0]; F = F.assign(contam=F.m_dec | F.m_fill)
    r = dict(frac_ordenes_marcadas=Rv.groupby('coin').m_dec.mean().round(4).to_dict(), n_rellenos_contam=F.groupby('coin').contam.sum().astype(int).to_dict(), n_rellenos=F.groupby('coin').size().to_dict())
    r['ev_contam_vs_limpio'] = {k: round(x.pnl.sum()/x.cost.sum(), 4) for k, x in F.groupby('contam') if x.cost.sum() > 0}
    r['orden_todos'] = boot(F); r['orden_sin_contam'] = boot(F[~F.contam])
    r['orden_por_moneda_sin_contam'] = {c: boot(F[(~F.contam) & (F.coin == c)]) for c in sorted(F.coin.unique()) if (F[(~F.contam) & (F.coin == c)].grupo == 'alto').sum() >= 5}
    r['orden_por_moneda_todos'] = {c: boot(F[F.coin == c]) for c in sorted(F.coin.unique()) if (F[F.coin == c].grupo == 'alto').sum() >= 5}
    Rs = Rv.sort_values('t_dec'); S = Rs.groupby(['dia', 'mid', 'lado']).agg(cost=('cost', 'sum'), pnl=('pnl', 'sum'), coin=('coin', 'first'), t0=('tercil', 'first'), m0=('m_dec', 'first'), mf=('m_fill', 'any')).reset_index()
    S['g'] = np.where(S.t0 == 'alto', 'alto', 'bm'); S['contam'] = S.m0 | S.mf
    r['t0_todos'] = boot(S, 'g'); r['t0_sin_contam'] = boot(S[~S.contam], 'g'); r['t0_lados_contam'] = int(S.contam.sum())
    r['t0_xrp_sin_contam'] = boot(S[(~S.contam) & (S.coin == 'xrp')], 'g')
    res[f'bloq{b}'] = r
json.dump(res, open(f'out/gap_mark_{modo}.json', 'w'), indent=1, default=str)
print(json.dumps(res, default=str, indent=0)[:3500])
