#!/usr/bin/env python3
"""ADDENDUM2: agrega out/d_<D>.npz y aplica el criterio congelado (CRITERIO_PREVIO.txt sha 18310f5f61f380a0...). Solo lectura.
Uso: python3 -I add2_eval.py [--sin-guardas] -> imprime tablas + traza de decision; escribe out/resumen_add2[_sg].json."""
import sys, glob, json, numpy as np
HERE = __file__.rsplit('/', 1)[0] + '/'
SG = '--sin-guardas' in sys.argv
TK = [int(x) for x in sys.argv[sys.argv.index('--ticks') + 1:sys.argv.index('--ticks') + 3]] if '--ticks' in sys.argv else None   # POST HOC (descriptivo): filtra tick de precio
BR = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R10', 'R11']; MR = ['R0f', 'R8', 'R9']
rng = np.random.default_rng(20261110)
Z = {f[-14:-4]: np.load(f) for f in sorted(glob.glob(HERE + 'out/d_2026-*.npz'))}
DAYS = sorted(Z); assert all(d < '2026-11-10' for d in DAYS)
per = lambda d: 'DISC' if d <= '2026-10-29' else 'HOLD'

def strata(z, p, n):
    coin = z[p + '_coin'].astype(np.int64); tick = z[p + '_tick'].astype(np.int64)
    mn = (z[p + '_min'].astype(np.int64) + 1) if (p + '_min') in z.files else np.zeros(n, np.int64)
    return (coin * 1000 + tick) * 10 + mn

def day_sums(p, rules, nperm, ms=False):
    """por dia y regla: sumas reales, P-temp y P-comp (nperm). Devuelve dict de arrays [dia, regla(, perm)]."""
    out = {k: [] for k in ('d', 'n_all', 'c_all', 'p_all', 'n_b', 'c_b', 'p_b', 'c_t', 'p_t', 'n_t', 'c_bp', 'p_bp', 'loss_all', 'loss_b',
                           'n_s30', 'n_b30', 'c_f1', 'p_f1', 'c_f0', 'p_f0')}
    for d in DAYS:
        z = Z[d]
        if (p + '_pnl') not in z.files: continue
        pnl = z[p + '_pnl'].astype(np.float64); cost = z[p + '_cost'].astype(np.float64)
        ok = np.isfinite(pnl) & (cost > 0)
        if not SG: ok &= z[p + '_guard'].astype(bool)
        if ms: ok &= np.all([z[f'{p}_{r}'] >= 0 for r in MR], axis=0)
        if TK: ok &= (z[p + '_tick'] >= TK[0]) & (z[p + '_tick'] <= TK[1])
        if ok.sum() == 0: continue
        pnl = pnl[ok]; cost = cost[ok]; n = len(pnl); st = strata(z, p, len(ok))[ok]
        o0 = np.lexsort((np.arange(n), st)); perms = [np.lexsort((rng.random(n), st)) for _ in range(nperm)]
        lab = np.array([z[f'{p}_{r}'][ok] == 1 for r in rules]); labt = np.array([z[f'{p}_{r}_t'][ok] == 1 for r in rules])
        fr = z[p + '_first'][ok] == 1
        cbp = np.empty((len(rules), nperm)); pbp = np.empty((len(rules), nperm))
        for j, pi in enumerate(perms):
            lp = np.empty_like(lab); lp[:, o0] = lab[:, pi]
            cbp[:, j] = lp @ cost; pbp[:, j] = lp @ pnl
        loss = np.maximum(-pnl, 0)
        out['d'].append(d); out['n_all'].append(n); out['c_all'].append(cost.sum()); out['p_all'].append(pnl.sum()); out['loss_all'].append(loss.sum())
        out['n_b'].append(lab.sum(1)); out['c_b'].append(lab @ cost); out['p_b'].append(lab @ pnl); out['loss_b'].append(lab @ loss)
        out['n_t'].append(labt.sum(1)); out['c_t'].append(labt @ cost); out['p_t'].append(labt @ pnl)
        out['c_bp'].append(cbp); out['p_bp'].append(pbp)
        out['n_b30'].append(lab.sum(1)); out['n_s30'].append(n - lab.sum(1))
        out['c_f1'].append((lab & fr) @ cost); out['p_f1'].append((lab & fr) @ pnl); out['c_f0'].append((lab & ~fr) @ cost); out['p_f0'].append((lab & ~fr) @ pnl)
    return {k: np.array(v) for k, v in out.items()}

def metr(S, w):
    """metricas agregadas con pesos por dia w (vector de recuentos de bootstrap o mascara 0/1). Devuelve dict por regla (arrays)."""
    W = np.asarray(w, np.float64)
    ca, pa = W @ S['c_all'], W @ S['p_all']
    cb, pb = W @ S['c_b'], W @ S['p_b']
    cbp = np.tensordot(W, S['c_bp'], 1); pbp = np.tensordot(W, S['p_bp'], 1)
    ev_b = pb / cb; ev_s = (pa - pb) / (ca - cb); dl = ev_s - ev_b; V = -pb / ca
    evbp = pbp / cbp; evsp = (pa - pbp) / (ca - cbp); dlp = evsp - evbp; Vp = -pbp / ca
    ct, pt = W @ S['c_t'], W @ S['p_t']; dlt = (pa - pt) / (ca - ct) - pt / ct
    return dict(cov_n=(W @ S['n_b']) / (W @ S['n_all']), cov_e=cb / ca, ev_b=ev_b, ev_s=ev_s, d=dl, V=V, d_adj=dl - dlp.mean(-1), V_adj=V - Vp.mean(-1),
                p_perm=(dlp >= dl[..., None]).mean(-1), d_t=dlt, cov_t=ct / ca, ev_all=pa / ca, loss_cap=(W @ S['loss_b']) / (W @ S['loss_all']),
                ev_f1=(W @ S['p_f1']) / (W @ S['c_f1']), ev_f0=(W @ S['p_f0']) / (W @ S['c_f0']), n=W @ S['n_all'], nb=W @ S['n_b'])

def boot(S, mask, B=2000, ref=0):
    idx = np.flatnonzero(mask); k = len(idx); out = {'d_adj': [], 'V_adj': [], 'dV': [], 'd': []}
    for _ in range(B):
        w = np.zeros(len(mask)); np.add.at(w, idx[rng.integers(0, k, k)], 1)
        m = metr(S, w); out['d_adj'].append(m['d_adj']); out['V_adj'].append(m['V_adj']); out['dV'].append(m['V_adj'] - m['V_adj'][ref]); out['d'].append(m['d'])
    return {kk: np.nanquantile(np.array(v), [0.05, 0.95], axis=0) for kk, v in out.items()}

def daily(S, mask, minn):
    r = []
    for i in np.flatnonzero(mask):
        w = np.zeros(len(mask)); w[i] = 1; m = metr(S, w)
        okd = (S['n_b30'][i] >= minn) & (S['n_s30'][i] >= minn); r.append(np.where(okd, m['d'], np.nan))
    r = np.array(r); v = ~np.isnan(r); return np.where(v, r > 0, False).sum(0) / np.maximum(v.sum(0), 1), v.sum(0), r

R = {'criterio_sha': '18310f5f61f380a04f33bc2ee4eebf99d6ddd44d1c47530d4bca9177cdd1ed48', 'sin_guardas': SG, 'dias': DAYS}
def tabla(nm, S, rules, minn, ref=0):
    res = {}
    for P in ('DISC', 'HOLD', 'TODO'):
        mask = np.array([(per(d) == P) or P == 'TODO' for d in S['d']])
        if mask.sum() < 2: continue
        m = metr(S, mask.astype(float)); b = boot(S, mask, ref=ref); fpos, nd, rd = daily(S, mask, minn)
        res[P] = {r: dict(n=int(m['n']), nb=int(m['nb'][i]), cov_n=m['cov_n'][i], cov_e=m['cov_e'][i], ev_all=m['ev_all'], ev_b=m['ev_b'][i], ev_s=m['ev_s'][i],
                          d=m['d'][i], d_ic=b['d'][:, i].tolist(), d_adj=m['d_adj'][i], d_adj_ic=b['d_adj'][:, i].tolist(), V=m['V'][i], V_adj=m['V_adj'][i],
                          V_adj_ic=b['V_adj'][:, i].tolist(), dV_ref=m['V_adj'][i] - m['V_adj'][ref], dV_ref_ic=b['dV'][:, i].tolist(), p_perm=m['p_perm'][i],
                          d_t=m['d_t'][i], cov_t=m['cov_t'][i], loss_cap=m['loss_cap'][i], ev_f1=m['ev_f1'][i], ev_f0=m['ev_f0'][i],
                          dias_pos=fpos[i], dias_n=int(nd[i]), d_dia=[None if np.isnan(x) else round(float(x), 4) for x in rd[:, i]],
                          dias=[d for d, mm in zip(S['d'], mask) if mm]) for i, r in enumerate(rules)}
        print(f'\n== {nm} {P} dias={int(mask.sum())} n={int(m["n"])} EV_todos={m["ev_all"]:+.4f}')
        print(f'{"regla":5s} {"cob_n":>6s} {"cob_e":>6s} {"EV_raf":>7s} {"EV_sue":>7s} {"Delta":>7s} {"D_adj":>7s} {"IC90dia D_adj":>17s} {"V_adj":>7s} {"IC90 V_adj":>17s} {"dV_ref":>7s} {"IC90 dV_ref":>17s} {"p":>5s} {"D_temp":>7s} {"cobT":>5s} {"dias+":>6s} {"perd%":>6s}')
        for i, r in enumerate(rules):
            x = res[P][r]
            print(f'{r:5s} {x["cov_n"]:6.3f} {x["cov_e"]:6.3f} {x["ev_b"]:+7.3f} {x["ev_s"]:+7.3f} {x["d"]:+7.3f} {x["d_adj"]:+7.3f} ({x["d_adj_ic"][0]:+.3f},{x["d_adj_ic"][1]:+.3f}) {x["V_adj"]:+7.4f} ({x["V_adj_ic"][0]:+.4f},{x["V_adj_ic"][1]:+.4f}) {x["dV_ref"]:+7.4f} ({x["dV_ref_ic"][0]:+.4f},{x["dV_ref_ic"][1]:+.4f}) {x["p_perm"]:5.3f} {x["d_t"]:+7.3f} {x["cov_t"]:5.3f} {x["dias_pos"]:4.2f}/{x["dias_n"]:<2d} {x["loss_cap"]:6.3f}')
    return res

S = day_sums('pop', BR, 200); R['pop'] = tabla('S_pop ETH/SOL/XRP (reglas de bloque)', S, BR, 30)
Sm = day_sums('pop', MR, 200, ms=True); R['pop_ms'] = tabla('S_pop subconjunto con tau (bloque feat vs ms)', Sm, MR, 30)
Ss = day_sums('sim', BR, 1000); R['sim'] = tabla('S_sim G0 (reglas de bloque)', Ss, BR, 5)
Ssm = day_sums('sim', MR, 1000, ms=True); R['sim_ms'] = tabla('S_sim subconjunto con tau', Ssm, MR, 5)
Sr = day_sums('real', BR, 1000); R['real'] = tabla('S_real B ETH/SOL/XRP+BTC>=0,03 (reglas de bloque)', Sr, BR, 5)
Srm = day_sums('real', MR, 1000, ms=True); R['real_ms'] = tabla('S_real subconjunto con tau', Srm, MR, 5)
Sb = day_sums('btc', BR, 50); R['btc'] = tabla('S_pop BTC (descriptivo, subvariante)', Sb, BR, 30)
R['ticks_posthoc'] = TK
json.dump(R, open(HERE + 'out/resumen_add2' + ('_sg' if SG else '') + (f'_t{TK[0]}_{TK[1]}' if TK else '') + '.json', 'w'), default=float, indent=0)
