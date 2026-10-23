#!/usr/bin/env python3
"""s3_b.py -- PREREG_S1 H4 (ordenes de B). Salida datos/s3_b.txt, datos/s3_b_eventos.csv"""
import os, sys, json, glob, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); CP = os.path.join(AQ, '..', '..', 'cola_posicion')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_S1.md'), 'rb').read()).hexdigest().startswith('5f1aab59408ec5e7')
sys.path.insert(0, os.path.join(CP, 'scripts')); import d1_l2_motor as M
DL = '/root/polymarket-research-datalogs/cola_posicion/'; rng = np.random.default_rng(20261023); out = []
def P(*a): out.append(' '.join(str(x) for x in a)); print(out[-1], flush=True)
O = json.load(open(DL + 'ordenes_b.json')); TOK = {}
for l in open(DL + 'snap/ledger_B.jsonl'):
    d = json.loads(l)
    if d.get('tipo') == 'intencion_post': TOK[d['oid']] = d['tok']
Lb = pd.read_csv(os.path.join(CP, 'datos', 'b_l2.csv')).set_index('oid')
U = pd.concat([pd.read_csv(f, usecols=['act', 'mid', 'lado', 'gana']) for f in glob.glob(os.path.join(CP, 'datos', 'pop_units_*.csv.gz'))]); U['mid'] = U.mid.astype(str)
U['win'] = np.where(((U.lado == 'YES') & (U.gana == 1)) | ((U.lado == 'NO') & (U.gana == 0)), 'Y', 'N'); WIN = {(r.act, r.mid): r.win for r in U.drop_duplicates(['act', 'mid']).itertuples()}
iso = lambda s: int(pd.Timestamp(s).timestamp() * 1000)
TAUS = (150, 300, 500, 1000)
def others_fn(lvn, L, q, size, arr, end):
    e = lvn.get((L, q))
    def oth(t):
        s = M.S(lvn, L, q, t)
        return max(0.0, s - (size if arr <= t <= end else 0.0))
    def ahead_ub(t):  # min de others en [arr,t] (puntos de cambio + arr)
        v = [oth(arr)]
        if e is not None:
            i0 = np.searchsorted(e[0], arr, 'right'); i1 = np.searchsorted(e[0], t, 'right')
            v += [max(0.0, s - size) for s in e[1][i0:i1]]
        return min(v) if t >= arr else np.nan
    def t_clear():
        if oth(arr) <= 0.5: return arr
        if e is None: return np.nan
        i0 = np.searchsorted(e[0], arr, 'right'); 
        for tt, s in zip(e[0][i0:], e[1][i0:]):
            if tt > end: break
            if s - size <= 0.5: return int(tt)
        return np.nan
    return oth, ahead_ub, t_clear
def exit_(oth, prn, L, q, u):
    s0 = oth(u - 850)
    if s0 < 5: return np.nan, s0
    c, _ = M.cons_between(prn, L, q, u - 850, u); return float((s0 - c - oth(u)) >= 0.8 * s0), s0
por = {}
for o in O:
    t = TOK.get(o['oid'])
    if t is None or t not in M.TM: continue
    act, mid, lado, fin = M.TM[t]; por.setdefault((act, mid), []).append((o, 'Y' if lado == 'YES' else 'N', fin, act, mid))
rows = []; haz = []
for (act, mid), lst in por.items():
    path = M.MK + f'{act}_{mid}.gz'
    if not os.path.exists(path): continue
    lvn, prn, tp, ap = M.carga(path)
    for o, L, fin, act_, mid_ in lst:
        q = M.mills(o['precio']); size = o['size']; oid = o['oid']; tc = int(o.get('t_call0', 0) * 1000)
        if not tc: continue
        isf = oid in Lb.index; arr = int(Lb.loc[oid].t_arr) if (isf and not pd.isna(Lb.loc[oid].t_arr)) else tc + 122
        if isf:
            if pd.isna(Lb.loc[oid].t_print): continue
            end = int(Lb.loc[oid].t_print)
        elif o.get('t_fuera'): end = iso(o['t_fuera'])
        elif o.get('t_cancel_int'): end = iso(o['t_cancel_int']) + 65
        else: continue
        if end <= arr: continue
        oth, aub, tcl = others_fn(lvn, L, q, size, arr, end)
        base = dict(oid=oid, coin=o['coin'], L=L, fin=fin, dia=o['ts_post'][:10], A0=o['cola'], size=size, q=q, act=act_, mid=mid_, arr=arr, end=end, filled=int(isf))
        tcv = tcl(); ex_ = (end - tcv) / 1000 if not np.isnan(tcv) else np.nan
        haz.append(dict(base, t_clear=tcv, exp_s=ex_, vida=(end - arr) / 1000))
        def add(grp, t):
            r = dict(base, grp=grp, t=int(t), edad=(t - arr) / 1000, ahead100=aub(t - 100), oth100=oth(t - 100))
            for tau in TAUS:
                ex, s0 = exit_(oth, prn, L, q, t - tau); r[f'ex{tau}'] = ex; r[f's{tau}'] = s0
            if isf and grp == 'F':
                r['acc'] = float(Lb.loc[oid].print_acc if False else Lb.loc[oid].acc)
            rows.append(r)
        if isf:
            if end - arr >= 1200: add('F', end)
        else:
            if end - arr >= 1260:
                add('R', int(rng.integers(arr + 1200, end - 50)))
                lo = max(arr + 1200, tcv) if not np.isnan(tcv) else None
                if lo is not None and lo < end - 50: add('RC', int(rng.integers(int(lo), end - 50)))
E1 = pd.DataFrame(rows); H = pd.DataFrame(haz); E1.to_csv(os.path.join(D, 's3_b_eventos.csv'), index=False); H.to_csv(os.path.join(D, 's3_b_haz.csv'), index=False)
P('B: ordenes', len(H), 'rellenas', int(H.filled.sum()), 'con edad>=1,2 s: F', int((E1.grp == 'F').sum()), 'R', int((E1.grp == 'R').sum()), 'RC', int((E1.grp == 'RC').sum()))
F = E1[E1.grp == 'F']
P('\n(a) F con print localizado y edad>=1,2 s (n=%d): ahead_ub(t*-100)<=0,5: %.3f ; otros(t*-100)<=0,5: %.3f ; otros<=0,5 entre los de ahead_ub<=0,5: %.3f' % (len(F), (F.ahead100 <= 0.5).mean(), (F.oth100 <= 0.5).mean(), (F[F.ahead100 <= 0.5].oth100 <= 0.5).mean()))
Fall = H[H.filled == 1]; P('    todas las F (sin filtro edad): despeje medido (otros<=0,5 en algun momento de la vida) %.3f (n=%d); tiempo despeje->relleno mediana %.2f s' % (Fall.t_clear.notna().mean(), len(Fall), Fall.exp_s.median()))
P('\n(b) hazard por tiempo desde el despeje de la cola (exposicion en s; rellenos por 100 s de exposicion; IC90 Poisson aprox.)')
bins = [(0, .3), (.3, .85), (.85, 2), (2, 1e9)]; Hc = H[H.t_clear.notna()]
for lo, hi in bins:
    ex = 0.0; ev = 0
    for r in Hc.itertuples():
        a = max(0.0, lo); b = min(r.exp_s, hi)
        if b > a: ex += b - a
        if r.filled and lo <= r.exp_s < hi: ev += 1
    se = np.sqrt(max(ev, 1)) / ex * 100 if ex else np.nan
    P(f'    [{lo:g},{hi:g}) s: exposicion {ex:8.1f} s, rellenos {ev:3d}, tasa {ev/ex*100 if ex else np.nan:6.2f} /100 s (+-{1.645*se:.2f})')
# tasa antes del despeje (cola presente)
pre = 0.0; evp = 0
for r in H.itertuples():
    end_pre = (r.t_clear - r.arr) / 1000 if not np.isnan(r.t_clear) else r.vida
    pre += max(end_pre, 0)
P(f'    antes del despeje (cola delante >0,5): exposicion {pre:.1f} s, rellenos con ese estado: {int(H[(H.filled==1)&H.t_clear.isna()].shape[0])} (rellenos sin despeje medido)')
def ic(df, col, key='fin', nb=1000):
    cl = df[key].unique(); g = {c: x for c, x in df.groupby(key)}; v = []
    return None
P('\n(c) EXIT(t*-tau) en F vs R vs RC (R restringido a cola despejada) ; edad>=1,2 s ; elegible = otros(u-850)>=5')
def rate(df, col): d = df[col].dropna(); return d.mean() if len(d) else np.nan, len(d)
def diff_ic(a, b, col, nb=1000):
    A = a[['fin', col]].dropna(); B = b[['fin', col]].dropna()
    if len(A) < 5 or len(B) < 5: return np.nan, (np.nan, np.nan)
    ga = A.groupby('fin')[col].agg(['sum', 'count']); gb = B.groupby('fin')[col].agg(['sum', 'count']); cl = np.array(sorted(set(ga.index) | set(gb.index))); ga = ga.reindex(cl).fillna(0); gb = gb.reindex(cl).fillna(0); v = []
    for _ in range(nb):
        m = rng.multinomial(len(cl), np.ones(len(cl)) / len(cl)); sa = (m * ga['sum'].values).sum(); ca = (m * ga['count'].values).sum(); sb = (m * gb['sum'].values).sum(); cb = (m * gb['count'].values).sum()
        v.append(sa / ca - sb / cb if ca > 0 and cb > 0 else np.nan)
    return A[col].mean() - B[col].mean(), tuple(np.nanpercentile(v, [5, 95]))
for tau in TAUS:
    col = f'ex{tau}'; fr, fn = rate(E1[E1.grp == 'F'], col); rr, rn = rate(E1[E1.grp == 'R'], col); cr, cn = rate(E1[E1.grp == 'RC'], col)
    d1, i1 = diff_ic(E1[E1.grp == 'F'], E1[E1.grp == 'R'], col); d2, i2 = diff_ic(E1[E1.grp == 'F'], E1[E1.grp == 'RC'], col)
    P(f'    tau {tau:4d}: F {fr:.3f} (n={fn})  R {rr:.3f} (n={rn})  RC {cr:.3f} (n={cn}) ; F-R {d1:+.3f} IC90 cierre ({i1[0]:+.3f},{i1[1]:+.3f}) ; F-RC {d2:+.3f} IC90 cierre ({i2[0]:+.3f},{i2[1]:+.3f})')
P('\n(d) EV de los rellenos de B (acc*(win-q), win por resolucion; sin fee/rebate) segun EXIT(t*-tau) (descriptivo)')
F = F.copy(); F['win'] = [WIN.get((a, str(m))) for a, m in zip(F.act, F.mid)]; F = F[F.win.isin(['Y', 'N'])]
F['cost'] = F.acc * F.q / 1000; F['pnl'] = F.acc * ((F.L == F.win).astype(float) - F.q / 1000)
P(f'    n con desenlace {len(F)}, EV total {F.pnl.sum()/F.cost.sum():+.3f}')
for tau in TAUS:
    d = F.dropna(subset=[f'ex{tau}'])
    for v in (1, 0):
        g = d[d[f'ex{tau}'] == v]; P(f'    tau {tau:4d} exit={v}: n={len(g)} EV {g.pnl.sum()/g.cost.sum() if len(g) else np.nan:+.3f} PnL {g.pnl.sum():+.2f} $ (hit {(g.pnl>0).mean() if len(g) else np.nan:.2f})')
open(os.path.join(D, 's3_b.txt'), 'w').write('\n'.join(out) + '\n')
