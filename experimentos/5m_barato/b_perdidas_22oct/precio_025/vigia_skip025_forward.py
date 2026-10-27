#!/usr/bin/env python3
"""Vigia FORWARD SHADOW de «saltar pujas > 0,243» (B, ETH/SOL/XRP 5m). SOLO LECTURA, sin dinero, sin tocar B/live.
Fuente: r3_shadow BASE (= pujas H35 de B simuladas en vivo sobre el WS del CLOB) escenario cons_x (primario) + opt_x/cons_r (cotas), desenlace oficial r3_desenlaces.
Unidad: (mercado, lado, precio); inferencia por CIERRE (bootstrap 2000, semilla 7); placebo = misma fraccion al azar dentro de dia (3000).
Gates PREREG (todos): >=10 dias desde --desde, >=40 cierres saltados, IC90 por cierre del EXCESO >0, EXCESO>0 sin los 2 mejores dias, placebo p<0,05.
Uso: nice -n 19 ionice -c3 python3 -I vigia_skip025_forward.py --desde 2026-10-24 [--salida fichero.json]"""
import argparse, glob, gzip, json
import numpy as np, pandas as pd
D = '/root/polymarket-research-datalogs/r3_shadow/'; CORTE = 0.243
ap = argparse.ArgumentParser(); ap.add_argument('--desde', required=True); ap.add_argument('--salida', default='skip025_forward.json'); a = ap.parse_args()
des = {}
for f in glob.glob(D + 'r3_desenlaces_*.jsonl.gz'):
    for l in gzip.open(f, 'rt'):
        try: d = json.loads(l)
        except Exception: continue
        if d.get('ganador'): des[d['slug']] = d['ganador']
rows = []
for f in sorted(glob.glob(D + 'r3_shadow_20*.jsonl.gz')):
    dia = f[-19:-9]
    if dia < a.desde: continue
    with gzip.open(f, 'rt') as fh:
        try:
            for l in fh:
                if '"tipo":"fill"' in l:
                    d = json.loads(l)
                    if d['pol'] == 'BASE': rows.append(dict(dia=dia, slug=d['slug'], esc=d['esc'], lado=d['lado'], precio=d['precio'], acc=d['acc']))
        except Exception: pass
F = pd.DataFrame(rows)
out = {'desde': a.desde, 'corte': CORTE}
if len(F):
    F['gan'] = F.slug.map(des); out['sin_desenlace'] = int(F.gan.isna().sum()); F = F[F.gan.notna()].copy()
    F['g'] = (F.gan == F.lado).astype(int); F['coste'] = F.precio * F.acc; F['pnl'] = np.where(F.g == 1, F.acc - F.coste, -F.coste)
    F['fin'] = F.slug.str.split('-').str[-1].astype(float) + 300
    ev = lambda x: x.pnl.sum() / x.coste.sum()
    for esc in ['cons_x', 'cons_r', 'opt_x']:
        U = F[F.esc == esc].groupby(['slug', 'lado', 'precio']).agg(dia=('dia', 'first'), fin=('fin', 'first'), coste=('coste', 'sum'), pnl=('pnl', 'sum')).reset_index()
        U['hi'] = U.precio > CORTE
        if U.hi.sum() < 5 or (~U.hi).sum() < 5: out[esc] = 'datos insuficientes'; continue
        rng = np.random.default_rng(7)
        exc = lambda x, f: ev(x[~f]) - ev(x)
        obs = exc(U, U.hi); gi = U.groupby('fin').indices; cl = U.fin.unique(); bs = []
        for _ in range(2000):
            x = U.iloc[np.concatenate([gi[c] for c in rng.choice(cl, len(cl))])].reset_index(drop=True); bs.append(exc(x, x.hi))
        di = U.groupby('dia').indices; pl = []
        for _ in range(3000):
            g = U.hi.values.copy()
            for ix in di.values(): g[ix] = rng.permutation(g[ix])
            pl.append(exc(U, pd.Series(g)))
        dp = U[U.hi].groupby('dia').pnl.sum().sort_values(); mejores = list(dp.index[:2])  # dias donde saltar mas ahorra (pnl de lo saltado mas negativo)
        k = ~U.dia.isin(mejores); sin2 = exc(U[k].reset_index(drop=True), U[k].hi.reset_index(drop=True)) if U[k].hi.sum() > 0 else None
        ic = np.quantile(bs, [.05, .95]).tolist(); dias = int(U.dia.nunique()); cs = int(U[U.hi].fin.nunique()); pp = float((np.array(pl) >= obs).mean())
        out[esc] = dict(dias=dias, cierres_saltados=cs, unidades=len(U), EXC=round(obs, 4), IC90_cierre=[round(v, 4) for v in ic], sin2_mejores=None if sin2 is None else round(sin2, 4), p_placebo=pp,
                        ret_EUR=round(1 - U[U.hi].coste.sum() / U.coste.sum(), 3), dPnL_EUR=round(-U[U.hi].pnl.sum(), 2),
                        GATE=bool(dias >= 10 and cs >= 40 and ic[0] > 0 and sin2 is not None and sin2 > 0 and pp < 0.05))
json.dump(out, open(a.salida, 'w'), indent=1, default=str); print(json.dumps(out, indent=1, default=str))
