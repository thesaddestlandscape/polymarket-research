#!/usr/bin/env python3
"""t4d_c.py (paso 1d-C, 17-Nov). Con los rellenos VIRTUALES de B (G0 passT_v4; cache/bfill_D.pkl) como metrica: separa el EV por estado del detector adoptado (W12 C30 rho0,07 nmin5 H1, salida inmediata; y con memoria N=60 como sensibilidad), por p5 10 min y por la verdad d<30 ms?
Regla F5 = tercil bajo p60 (F5<=C0) con cat ok, TODOS los rellenos G0 (convencion E1; tipo B como sensibilidad). Variantes de gating del relleno (a): OPTIMISTA = estado lo en tf-L (conserva prioridad de cola aunque se cancele y reponga); (b) CONSERVADORA = lo en TODO [t_dec+68, tf] (sin cancelaciones).
Unidad: EV pond. por EUR = sum(pnl)/sum(cost). Diferencia lo-nolo PAREADA por dia, IC90 t por dias y bootstrap por BLOQUES DE DIA (B=5000, semilla 20261118). n de dias necesarios = (1,645*sd/media)^2 con sd de la diferencia diaria. 0 ordenes."""
import os, sys, json, glob, numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); import suelo_causal as SC, t4b_eval as T, t4d_a as A
from scipy import stats
C0 = 3.526360511779785; P = A.P; LMS = 35
def estados(D, N=0):
    n, c = A.ventana(D.S, P); return A.estado_mem(n, c, P, N) if N else SC.estado_lo(SC.lo_crudo(D.S, P), P)
def gate(F, D, st, L, modo):
    day0 = int(pd.Timestamp(D.d + 'T00:00:00Z').value // 10**6); tf = F.tf.values.astype(np.int64)
    if modo == 'opt': return st[np.clip((tf - L - day0) // 1000, 0, 86399)]
    c = np.concatenate([[0], np.cumsum(~st)]); a = np.clip((F.t_dec.values.astype(np.int64) + 68 - day0) // 1000, 0, 86399); b = np.clip((tf - L - day0) // 1000, 0, 86399); return (c[b + 1] - c[a]) == 0       # ningun segundo nolo entre alta y relleno
def ev(p, c): return float(p / c) if c > 0 else float('nan')
def boot(rows, B=5000, seed=20261118):
    """rows: lista (p_lo,c_lo,p_no,c_no) por dia -> (dif EV lo-nolo agregada, IC90 percentil bloques-dia)."""
    a = np.array(rows, float); rng = np.random.default_rng(seed); n = len(a); d = []
    for _ in range(B):
        s = a[rng.integers(0, n, n)].sum(0); d.append(ev(s[0], s[1]) - ev(s[2], s[3]))
    d = np.array(d); d = d[np.isfinite(d)]; s0 = a.sum(0); return ev(s0[0], s0[1]) - ev(s0[2], s0[3]), float(np.percentile(d, 5)), float(np.percentile(d, 95))
def resumen(nm, rows, per_dia):
    s = np.array(rows, float).sum(0); pdif = np.array([ev(r[0], r[1]) - ev(r[2], r[3]) for r in rows]); pdif = pdif[np.isfinite(pdif)]; b = boot(rows)
    t = ''
    if len(pdif) >= 3:
        se = pdif.std(ddof=1) / np.sqrt(len(pdif)); lo = pdif.mean() - stats.t.ppf(.95, len(pdif) - 1) * se; hi = pdif.mean() + stats.t.ppf(.95, len(pdif) - 1) * se; sd = pdif.std(ddof=1)
        nreq = (1.645 * sd / abs(pdif.mean())) ** 2 if pdif.mean() != 0 else float('inf'); t = f"dif pareada media {pdif.mean():+.3f} IC90 dias ({lo:+.3f},{hi:+.3f}) n_dias {len(pdif)} dias+ {(pdif > 0).sum()}; dias necesarios para IC90>0 con este efecto ~{nreq:.0f}"
    return f"{nm:<34} lo: EV {ev(s[0], s[1]):+.3f} (n={int(per_dia['n_lo'])}, {s[1]:.0f} EUR) | nolo: EV {ev(s[2], s[3]):+.3f} (n={int(per_dia['n_no'])}, {s[3]:.0f} EUR) | dif agregada {b[0]:+.3f} bootstrap-bloques-dia IC90 ({b[1]:+.3f},{b[2]:+.3f}) | {t}"
if __name__ == '__main__':
    fs = sorted(glob.glob(HERE + '/cache/bfill_2026-*.pkl')); days = [os.path.basename(f)[6:16] for f in fs if json.load(open(HERE + '/cache/bfill_man_' + os.path.basename(f)[6:16] + '.json')).get('estado') == 'COMPLETE']
    days = [d for d in days if os.path.exists(HERE + f'/cache/seg_{d}.npz') and os.path.exists(HERE + f'/cache/clases_{d}.npz')]; L = [f'# T4d-C rellenos virtuales de B (G0 passT_v4), dias con fills+seg: {len(days)} ({days[0]}..{days[-1]}); regla F5 bajo p60 con cat ok; L={LMS} ms']
    Fs = {d: pd.read_pickle(HERE + f'/cache/bfill_{d}.pkl') for d in days}; tot = pd.concat(Fs.values()); L.append(f"G0 fills n={len(tot)}, cost {tot.cost.sum():.0f} EUR, pnl {tot.pnl.sum():+.0f}, EV {ev(tot.pnl.sum(), tot.cost.sum()):+.3f}; con F5 ok {int((tot.cat_p60 == 0).sum())}; regla (bajo) n={int(((tot.cat_p60 == 0) & (tot.F5_p60 <= C0)).sum())}; tipoB n={int(tot.tipoB.sum())}")
    Ds = {d: T.Dia(d) for d in days}
    for variante, filtro in (('REGLA bajo (primaria)', lambda F: (F.cat_p60 == 0) & (F.F5_p60 <= C0)), ('regla bajo & tipoB', lambda F: (F.cat_p60 == 0) & (F.F5_p60 <= C0) & F.tipoB), ('TODOS los fills G0', lambda F: np.ones(len(F), bool)), ('tercil ALTO (cat ok)', lambda F: (F.cat_p60 == 0) & (F.F5_p60 > 4.717426776885986))):
        L.append(f'## {variante}')
        for dn, fn in (('detector adoptado N=0', lambda D: estados(D)), ('detector + memoria N=60', lambda D: estados(D, 60)), ('p5 10 min (v4)', lambda D: D.st_p5), ('verdad d<30 ms (lo)', lambda D: D.vs == 1)):
            for modo in ('opt', 'cons'):
                rows = []; cnt = dict(n_lo=0, n_no=0)
                for d in days:
                    F = Fs[d][filtro(Fs[d])]
                    if len(F) == 0: continue
                    g = gate(F, Ds[d], fn(Ds[d]), LMS, modo); rows.append((float(F.pnl[g].sum()), float(F.cost[g].sum()), float(F.pnl[~g].sum()), float(F.cost[~g].sum()))); cnt['n_lo'] += int(g.sum()); cnt['n_no'] += int((~g).sum())
                L.append(resumen(f'{dn} [{modo}]', rows, cnt))
    # oportunidad perdida (regla bajo): rellenos en nolo con verdad lo (detector adoptado)
    rl = dict(n=0, c=0., p=0.); rh = dict(n=0, c=0., p=0.)
    for d in days:
        F = Fs[d][(Fs[d].cat_p60 == 0) & (Fs[d].F5_p60 <= C0)]; D = Ds[d]; st = estados(D); g = gate(F, D, st, LMS, 'opt'); s = np.clip((F.tf.values.astype(np.int64) - int(pd.Timestamp(d + 'T00:00:00Z').value // 10**6)) // 1000, 0, 86399); tv = D.vs[s]
        for tgt, m in ((rl, ~g & (tv == 1)), (rh, g & (tv == 0))): tgt['n'] += int(m.sum()); tgt['c'] += float(F.cost.values[m].sum()); tgt['p'] += float(F.pnl.values[m].sum())
    L.append(f"B virtual, regla bajo: en nolo con verdad lo (oportunidad perdida) n={rl['n']} {rl['c']:.1f} EUR pnl {rl['p']:+.1f}; en lo con verdad hi n={rh['n']} {rh['c']:.1f} EUR pnl {rh['p']:+.1f}")
    open(HERE + '/T4d_C.txt', 'w').write('\n'.join(L) + '\n'); print('\n'.join(x[:900] for x in L))
