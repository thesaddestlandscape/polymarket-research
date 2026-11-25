"""u1b_prereg_bloqueo_A2.py (R4 exploratoria) -- mide PREREG_BLOQUEO_19nov.md + ADENDA_A1 (ancla al precio del maker). Solo lectura, 0 ordenes, no EV."""
import sys, os, gzip, numpy as np, pandas as pd
sys.path.insert(0, '../solo_observable_19nov'); import so1_traza as S
d = pd.read_pickle(S.BASE + 'tomador_202.pkl'); d = d[d.tk_tipo == 'compra_comp'].copy()
d['rem_sh'] = d.tk_rem.fillna(0) * d.tk_sz; d['pos'] = d.tk_rem.fillna(0) > 0.01
def trades(fn):
    T = {'Y': [], 'N': []}
    with gzip.open(fn, 'rt', errors='replace') as f:
        for ln in f:
            c = ln.rstrip('\n').split(',')
            if len(c) >= 6 and c[1] == 'T' and c[0] in T:
                try: T[c[0]].append((int(c[2]), c[3], int(round(float(c[4]) * 1000)), float(c[5])))
                except ValueError: pass
    return T
def first_inc(ser, t0, t1, need_empty=False):
    if ser is None: return None
    t, s = ser; prev = np.concatenate([[0.0], s[:-1]]); m = np.where((t >= t0) & (t <= t1) & (s - prev > 1e-9))[0]
    for i in m:
        if need_empty and prev[i] > 1e-9: continue
        return float(s[i] - prev[i])
    return None
RULES = {'R4': (2, False)}
cache = {}; rows = []
for r in d.itertuples():
    m = S.TOKM.get(str(r.tok))
    if m is None: continue
    fn = S.MK + f'{m[0]}_{m[1]}.gz'
    if not os.path.exists(fn): continue
    if fn not in cache:
        if len(cache) > 6: cache.pop(next(iter(cache)))
        cache[fn] = (S.parse(fn), trades(fn))
    B, TR = cache[fn]; own = 'Y' if m[2] == 'YES' else 'N'; comp = 'N' if own == 'Y' else 'Y'
    t3 = int(r.real_tm3); P = int(round((1.0 - float(r.tk_eq)) * 100)) * 10; Pown = int(round(float(r.tk_eq) * 100)) * 10
    rx_pr = None; src = 'sin_print'
    PL = int(round((1.0 - float(r.L)) * 100)) * 10; PLo = int(round(float(r.L) * 100)) * 10
    for sd, pps, lab in ((comp, (P, PL), "comp"), (own, (Pown, PLo), "own")):
        c = [x[0] for x in TR[sd] if x[1] == 'BUY' and min(abs(x[2] - q) for q in pps) <= 5 and t3 - 100 <= x[0] <= t3 + 1500]
        if c: rx_pr = min(c); src = lab; break
    tol = max(0.02 * r.rem_sh, 0.05); tol2 = max(0.02 * r.rem_sh, 0.5)
    out = dict(oid=r.oid, dia=r.dia, pos=bool(r.pos), rem_sh=r.rem_sh, src=src, dt_pr_tm3=(rx_pr - t3) if rx_pr else np.nan)
    for k, (X, emp) in RULES.items():
        def ev(p, sh):
            if rx_pr is None: return (False, False, False)
            dl = first_inc(B[comp].get(p), rx_pr + sh - (2 if k == "R4" else 30), rx_pr + sh + X, emp)
            if dl is None: return (False, False, False)
            return (True, bool(r.pos and abs(dl - r.rem_sh) <= tol), bool(r.pos and abs(dl - r.rem_sh) <= tol2))
        f, h, h2 = ev(P, 0); out.update({k+'_f': f, k+'_h': h, k+'_h2': h2})
        pt = [ev(P + o, 0) for o in (-10, 10)]; out[k+'_plv_h'] = np.mean([x[1] for x in pt]); out[k+'_plv_f'] = np.mean([x[0] for x in pt])
        ps = [ev(P, s) for s in S.SHIFTS]; out[k+'_pt_h'] = np.mean([x[1] for x in ps]); out[k+'_pt_hmax'] = float(any(x[1] for x in ps)); out[k+'_pt_f'] = np.mean([x[0] for x in ps])
    rows.append(out)
X = pd.DataFrame(rows); X.to_csv('out/u1b_prereg_bloqueo_A2.csv', index=False)
def wil(k, n, z=1.645):
    if n == 0: return (np.nan, np.nan)
    p = k / n; den = 1 + z*z/n; c = (p + z*z/(2*n)) / den; h = z*np.sqrt(p*(1-p)/n + z*z/(4*n*n)) / den; return (round(c-h, 3), round(c+h, 3))
Pz = X[X.pos]; N = X[~X.pos]
print('n compra_comp con mk =', len(X), '| positivos', len(Pz), '| negativos', len(N), '| ancla:', X.src.value_counts().to_dict())
print('dt rx_print - tm3 (ms) p5/p50/p95:', np.nanpercentile(X.dt_pr_tm3, [5, 50, 95]).round(0).tolist())
for k in RULES:
    hp = int(Pz[k+'_h'].sum()); fl = int(X[k+'_f'].sum()); fp_neg = int(N[k+'_f'].sum())
    rec = hp / len(Pz); prec = hp / fl if fl else np.nan
    plv = Pz[k+'_plv_h'].mean(); pt = Pz[k+'_pt_h'].mean(); ptm = Pz[k+'_pt_hmax'].mean()
    ok = rec >= 0.15 and rec >= 3*plv and rec >= 5*ptm and (prec >= 0.5)
    print(f"{k}: recall {rec:.3f} {wil(hp,len(Pz))} | precision {prec:.3f} ({hp}/{fl}) {wil(hp,fl)} | disparos en negativos {fp_neg}/{len(N)} | tol0,5acc recall {Pz[k+'_h2'].mean():.3f}"
          f" | placebo tick acierto {plv:.3f} disparo {X[k+'_plv_f'].mean():.3f} | placebo t acierto media {pt:.3f} max {ptm:.3f} disparo {X[k+'_pt_f'].mean():.3f} | disparo real {X[k+'_f'].mean():.3f} | PASA={ok}")
G = Pz[Pz.rem_sh >= 1]; print('INFORMATIVO positivos rem_sh>=1 acc: n', len(G), '| sin ancla', int((G.src == 'sin_print').sum()))
for k in RULES:
    print(f"  {k}: recall {G[k+'_h'].mean():.3f} ({int(G[k+'_h'].sum())}/{len(G)}) | placebo tick {G[k+'_plv_h'].mean():.3f} | placebo t max {G[k+'_pt_hmax'].mean():.3f}")
