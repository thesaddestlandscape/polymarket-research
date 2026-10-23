#!/usr/bin/env python3
"""r3_precios.py - S_C (precios reales): regla rpre-skip (CON y |rpre|>=7,7) condicionada a clases del detector, medida en PnL TOTAL (EUR). PREREG_RTEND sec.4 H3.
pop 17-22 Oct (feats_pop, rpre W1) y baratas 5-14 Oct (rpre del detector). Clases del detector desde ventanas_bookticker. IC90 por cierre; placebo = misma cantidad de saltos al azar dentro de dia x moneda x cubo de precio 0,05 entre las unidades CON>=7,7."""
import os, sys, glob, numpy as np, pandas as pd, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); DAT = os.path.join(HERE, '..', 'datos')
assert hashlib.sha256(open(os.path.join(HERE, '..', 'PREREG_RTEND.md'), 'rb').read()).hexdigest().startswith('0cbe5e44')
RNG = np.random.default_rng(20261024); THR = 7.7
W = pd.read_csv(os.path.join(DAT, 'ventanas_bookticker.csv.gz'))[['coin', 'tmin', 'rpre', 'R', 'D', 'COH', 'ER60', 'VR240', 'VOLR', 'DAYT']].rename(columns={'rpre': 'rpre_bar'})
W['COHc'] = np.where(W.COH.isna(), 'NA', np.where(W.COH >= 4, 'COH4', 'NOCOH'))
def load_pop():
    P = pd.read_csv(os.path.join(HERE, '..', '..', 'tendencia_wallets', 'datos', 'feats_pop.csv.gz'))
    P = P[P.gana.notna() & P.pnl.notna()].copy(); P['coin'] = P.act; P['tmin'] = P.fin // 60 - 5; P['pnl_u'] = P.pnl; P['cost_u'] = P.coste; P['cierre'] = P.fin; P['pc_'] = P.pc
    return P.merge(W, on=['coin', 'tmin'], how='left')
def load_barat():
    fs = sorted(glob.glob('/root/polymarket-research-datalogs/m5barato_mision/baratas_unidades_2026-10-*.csv.gz')); P = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
    P = P[P.activo.isin(['ETH', 'SOL', 'XRP']) & (P.banda == '0.10-0.20') & (P.T_med >= 60) & (P.T_med <= 300) & (P.acc > 0)].copy()
    P['coin'] = P.activo; P['tmin'] = P.cierre // 60 - 5; sg = np.where(P.lado == 'YES', 1.0, -1.0)
    P['pnl_u'] = P.pnl * 5 / P.acc; P['cost_u'] = P.usdc * 5 / P.acc; P['cierre'] = P.cierre; P['pc_'] = P.precio_med; P['dia'] = P.dia
    P = P.merge(W, on=['coin', 'tmin'], how='left'); P['rpre'] = P.rpre_bar * sg; return P
def ic_cierre(D, mask_skip, nb=1000):
    """IC90 de dPnL = -Sum pnl(skipped) por cierre (bootstrap de cierres)."""
    g = D.assign(sk=np.where(mask_skip, D.pnl_u, 0.0)).groupby('cierre').agg(s=('sk', 'sum')); v = g.s.values; n = len(v)
    bs = np.array([-v[RNG.integers(0, n, n)].sum() for _ in range(nb)]); return np.percentile(bs, [5, 95])
def placebo(D, elig, nskip_mask, np_=1000):
    """dPnL de saltar al azar el mismo numero de unidades entre las elegibles (CON>=7.7), estratificado dia x moneda x cubo precio."""
    E = D[elig]; strat = (E.dia.astype(str) + E.coin + (E.pc_ * 20).astype(int).astype(str)).astype('category').cat.codes.values
    sk = nskip_mask[elig.values] if hasattr(elig, 'values') else nskip_mask[elig]; pnl = E.pnl_u.values; out = np.empty(np_)
    # cuantos saltar en cada estrato = los del conjunto real
    cnt = pd.Series(sk).groupby(strat).sum().to_dict(); idx_by = pd.Series(np.arange(len(E))).groupby(strat).apply(list).to_dict()
    for i in range(np_):
        tot = 0.0
        for s, k in cnt.items():
            if k: tot += pnl[RNG.choice(idx_by[s], int(k), replace=False)].sum()
        out[i] = -tot
    return out
def tabla(D, label, per_col=None):
    out = [f'\n=== {label}: n {len(D)}, coste {D.cost_u.sum():.0f}, PnL {D.pnl_u.sum():+.1f}, EV/EUR {D.pnl_u.sum()/D.cost_u.sum():+.4f}, cierres {D.cierre.nunique()}, dias {D.dia.nunique()} ===']
    D = D.copy(); D['con'] = (D.rpre >= THR); elig = D.con
    periods = [('TODO', D.dia.notna())] if per_col is None else [(k, D.dia.isin(v)) for k, v in per_col.items()] + [('TODO', D.dia.notna())]
    rules = [('INCOND  CON>=7,7', D.con)]
    for fam, cl in (('R', ['TREND', 'MIXTO', 'REVERT']), ('D', ['TENDENCIA', 'RANGO']), ('COHc', ['COH4', 'NOCOH'])):
        for c in cl: rules.append((f'CON>=7,7 & {fam}={c}', D.con & (D[fam] == c)))
    for pn, pm in periods:
        d = D[pm]
        out.append(f'-- periodo {pn}: n {len(d)}, PnL base {d.pnl_u.sum():+.1f}')
        for rn, rm in rules:
            m = rm[pm]; 
            if m.sum() < 20: out.append(f'   {rn:34s} n {int(m.sum())} (<20)'); continue
            dp = -d.pnl_u[m].sum(); ev_sk = d.pnl_u[m].sum() / d.cost_u[m].sum(); lo, hi = ic_cierre(d, m.values)
            pl = placebo(d, d.con, m.values & d.con.values, 300); pv = (pl >= dp).mean()
            out.append(f'   {rn:34s} n {int(m.sum()):5d} coste {d.cost_u[m].sum():7.0f} EV saltadas {ev_sk:+.3f}  dPnL(skip) {dp:+8.1f} IC90cierre ({lo:+.1f},{hi:+.1f}) placebo media {pl.mean():+.1f} p {pv:.3f}')
        by = d.groupby('dia').apply(lambda g: pd.Series({'base': g.pnl_u.sum(), 'dP_incond': -g.pnl_u[g.con].sum(), 'dP_TREND': -g.pnl_u[g.con & (g.R == 'TREND')].sum(), 'dP_REVERT': -g.pnl_u[g.con & (g.R == 'REVERT')].sum(), 'dP_TEND_D': -g.pnl_u[g.con & (g.D == 'TENDENCIA')].sum(), 'dP_RANGO_D': -g.pnl_u[g.con & (g.D == 'RANGO')].sum(), 'dP_COH4': -g.pnl_u[g.con & (g.COHc == 'COH4')].sum(), 'dP_NOCOH': -g.pnl_u[g.con & (g.COHc == 'NOCOH')].sum()}), include_groups=False)
        out.append(by.round(1).to_string()); 
    return out
if __name__ == '__main__':
    out = tabla(load_pop(), 'S_C pop on-chain 17-22 Oct (feats_pop)', {'DESC 17-19': ['2026-10-17', '2026-10-18', '2026-10-19'], 'TEST 20-22': ['2026-10-20', '2026-10-21', '2026-10-22']})
    out += tabla(load_barat(), 'S_C replica baratas 5-14 Oct (banda 0,10-0,20, normalizado a 5 acc)')
    open(os.path.join(DAT, 'r3.txt'), 'w').write('\n'.join(out)); print('\n'.join(out))
