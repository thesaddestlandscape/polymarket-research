#!/usr/bin/env python3
"""Paso 3. Modo 'train': lee SOLO dias TRAIN, aplica la regla de seleccion del DISENO.md y escribe out/chosen.json. Modo 'hold': exige chosen.json y evalua UNA vez la elegida en HOLD.
Modo 'base': validacion de la base (sin cancelar) y de concordancia de reloj; no toca ninguna politica."""
import sys, os, json, hashlib, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
mode = sys.argv[1]
DIS_SHA = hashlib.sha256(open(H + 'DISENO.md', 'rb').read()).hexdigest()
assert DIS_SHA.startswith('1e2d13cc'), 'DISENO.md cambio'
TRAIN = ['2026-11-03', '2026-11-04', '2026-11-05', '2026-11-06', '2026-11-07']; HOLD = ['2026-11-08', '2026-11-09']
CFG = [('D', x) for x in (-1, 0, 1, 2, 3, 5)] + [('V', x) for x in (2, 3, 5)] + [('S', x) for x in (0, 50, 200)]; NAM = [f'{a}{x}' for a, x in CFG]
def ms(s): return int(pd.Timestamp(s, tz='UTC').timestamp() * 1000)
CLEAN = {'2026-11-03': [(ms('2026-11-03 11:00'), ms('2026-11-04 00:00'))], '2026-11-04': [(ms('2026-11-04 00:00'), ms('2026-11-04 02:41')), (ms('2026-11-04 10:46'), ms('2026-11-05 00:00'))]}
def cargar(dias):
    F = pd.read_pickle(H + 'out/g0_fills.pkl'); out = []
    for d in dias:
        T = pd.read_pickle(H + f'out/trg_{d}.pkl'); f = F[F.dia == d]
        m = f.merge(T.drop(columns=['token']), on=['dia', 'k', 'L', 'tf'], how='left', validate='1:1'); assert len(m) == len(f)
        if d in CLEAN: m = m[np.any([(m.t_dec >= a) & (m.t_dec < b) for a, b in CLEAN[d]], axis=0)]
        out.append(m)
    return pd.concat(out, ignore_index=True)
def avoided(D, name, lam):
    t = D['tr_' + name].values; M = D.tf.values - t; st = D['st_' + name].values if 'st_' + name in D else np.zeros(len(D), bool)
    return st | ((t >= 0) & (M > lam))
def delta(D, av): return -D.pnl.values[av].sum()
def placebo_p(D, av, B=5000, seed=20261110):
    rng = np.random.default_rng(seed); obs = delta(D, av); idx = {d: np.where(D.dia.values == d)[0] for d in D.dia.unique()}; n_by = {d: int(av[i].sum()) for d, i in idx.items()}
    pnl = D.pnl.values; sim = np.zeros(B)
    for d, i in idx.items():
        n = n_by[d]
        if n == 0: continue
        for b in range(B): pass
        # permutaciones vectorizadas: elegir n de len(i) sin reposicion
        P = np.argsort(rng.random((B, len(i))), axis=1)[:, :n]; sim -= pnl[i][P].sum(1)
    return obs, float((sim >= obs - 1e-12).mean()), float(sim.mean())
if mode == 'train':
    D = cargar(TRAIN); D = D[D.bad.isna()].reset_index(drop=True)
    print('TRAIN fills validos', len(D), 'por dia', D.groupby('dia').size().to_dict(), 'pnl base', round(D.pnl.sum(), 1), 'cost', round(D.cost.sum(), 1))
    rows = []
    for c, nm in enumerate(NAM):
        av = avoided(D, nm, 30); obs, p, mpl = placebo_p(D, av)
        pd_ = {d: -g.pnl[av[g.index]].sum() for d, g in D.groupby('dia')}; pos = np.mean([v > 0 for v in pd_.values()])
        el = (obs > 0) and pos >= 0.7 and p < 0.05 / 12
        rows.append(dict(cfg=nm, n_evit=int(av.sum()), frac=round(av.mean(), 3), delta=round(obs, 2), placebo_mean=round(mpl, 2), p=round(p, 4), dias_pos=round(pos, 2), elegible=bool(el)))
    R = pd.DataFrame(rows); print(R.to_string(index=False))
    E = R[R.elegible]; ch = None if E.empty else E.sort_values('delta', ascending=False).iloc[0].cfg
    json.dump(dict(chosen=ch, diseno_sha=DIS_SHA, tabla=rows), open(H + 'out/chosen.json', 'w'), indent=1); print('ELEGIDA:', ch)
if mode == 'base':
    import glob
    G = pd.read_pickle(H + 'out/g0_fills.pkl'); Fx = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + '../frente2_sueltos_10nov/out/F_*.pkl'))], ignore_index=True)
    m = G.merge(Fx[['dia', 'k', 'L', 'tf', 'R0']], on=['dia', 'k', 'L', 'tf'], how='inner'); S = m[m.R0 == 0]
    print('BASE sin cancelar, 12 dias quemados: fills', len(m), 'sueltos n', len(S), 'acierto', round(S.gana.mean(), 4), 'precio medio', round((S.cost / S.q).mean(), 4), '(conocido: n=2290, 0,1410, 0,1523)')
    print('  todos los G0 de esos dias: pnl', round(m.pnl.sum(), 1), 'coste', round(m.cost.sum(), 1), 'EV/eur', round(m.pnl.sum() / m.cost.sum(), 4))
    D = cargar(TRAIN + HOLD); v = D[D.bad.isna()]
    print('validez L2: fills', len(D), 'validos', len(v), 'bad', D.bad.value_counts(dropna=False).to_dict())
    d = (v.tf - v.tl2)[v.tl2 > 0]; print('reloj: cobertura de reduccion en nivel L +-1,5 s', round((v.tl2 > 0).mean(), 3), 'tf-tl2 ms pct 5/25/50/75/95', d.quantile([.05, .25, .5, .75, .95]).round(0).tolist())
    print('  |tf-tl2|<=50 ms:', round((d.abs() <= 50).mean(), 3), '<=150 ms:', round((d.abs() <= 150).mean(), 3))
