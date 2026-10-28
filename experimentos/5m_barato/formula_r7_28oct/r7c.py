import sys, os, pickle, zlib, io, contextlib, numpy as np
E4 = '/root/polymarket-research/experimentos/5m_barato/'
for d in ('formula_r6_28oct', 'formula_r5_28oct', 'formula_r4_28oct', 'formula_r3_28oct'): sys.path.insert(0, E4 + d)
import r4, r5f, r6a
from r6a import summ, F, P, load as load6
crc = lambda s: zlib.crc32(s.encode()) & 0xffffffff
days0 = sorted(f[2:12] for f in os.listdir(E4 + 'formula_r6_28oct/fills') if f.startswith('f_'))
with contextlib.redirect_stdout(io.StringIO()): days = r5f.inclusion(days0)
nd = len(days); dd = lambda lo, hi: [i for i, d in enumerate(days) if lo <= int(d[-2:]) <= hi]
IS, OOS, DEV = dd(6, 15), dd(16, 25), dd(26, 27)
R = load6(days, 0); S = np.isfinite(R['dA']); off = np.round((R['p'] - R['bb']) / 0.01); trs = R['trem']
niche = S & (R['sA'] >= 800) & (trs >= 120) & (trs < 240) & (R['p'] <= 0.29) & np.isfinite(off) & (off >= 0)
# sim v258
SM = {'di': [], 'mk': [], 'bpx': [], 'y': [], 'tf': [], 't2': [], 't0': [], 'trem': []}
for i, d in enumerate(days):
    f = E4 + 'formula_r7_28oct/simc/s_%s.pkl' % d
    if not os.path.exists(f): continue
    Rv, rows = pickle.load(open(f, 'rb'))
    for r in rows:
        SM['di'].append(i); SM['mk'].append(crc(r[2])); SM['bpx'].append(r[4]); SM['y'].append(r[3]); SM['tf'].append(r[10]); SM['t2'].append(r[8]); SM['t0'].append(r[6]); SM['trem'].append(r[11])
SM = {k: np.array(v) for k, v in SM.items()}
Rs = dict(di=SM['di'], num=SM['t2'] * (SM['y'] - SM['bpx']), den=SM['t2'] * SM['bpx']); ms = SM['t2'] > 0
P('== R7 C: brecha de ejecucion v258 (theta800, W5-60, Trem120-240, TD1, bb+0,01, banda>=0,10; N=20 acc)')
for pn, ds in (('IS 06-15', IS), ('OOS 16-25', OOS), ('DEV 26-27', DEV), ('06-25', dd(6, 25))):
    P('  SIM  %-9s %s | ejec/d %.0f' % (pn, F(summ(Rs, ms, ds, nd)), ms[np.isin(SM['di'], ds)].sum() / len(ds)))
    P('  REAL %-9s %s' % (pn, F(summ(R, niche, ds, nd))))
reb = float((Rs['den'][ms] * 0.014 * (1 - SM['bpx'][ms])).sum() / Rs['den'][ms].sum()); P('  rebate maker 0,014*(1-p) por EUR sobre fills sim: +%.4f' % reb)
# emparejamiento fill sim <-> relleno real (mismo mercado, mismo precio, |dt|<=2 s)
key = {}
for i in np.flatnonzero(niche | (S & (trs >= 120) & (trs < 240))): key.setdefault((int(R['mk'][i]), round(float(R['p'][i]), 2)), []).append((float(R['rhat'][i]), i))
matched_real = np.zeros(len(R['p']), bool); hit = np.zeros(len(SM['tf']), bool)
for j in np.flatnonzero(ms):
    for (t, i) in key.get((int(SM['mk'][j]), round(float(SM['bpx'][j]), 2)), ()):
        if abs(t - SM['tf'][j]) <= 2000.0: matched_real[i] = True; hit[j] = True
P('  fills sim con relleno real emparejado (mismo mercado y precio, |dt|<=2 s): %.1f %% de %d' % (100 * hit[ms].mean(), ms.sum()))
sets = {'real nicho', 'x'}
A = niche & matched_real; B = niche & ~matched_real & (off == 1); C = niche & ~matched_real & (off != 1)
for pn, ds in (('IS', IS), ('OOS 16-25', OOS), ('DEV', DEV)):
    P('  [%s] nicho real ∩ sim: %s' % (pn, F(summ(R, A, ds, nd))))
    P('  [%s] nicho real SIN sim, p=bb+0,01: %s' % (pn, F(summ(R, B, ds, nd))))
    P('  [%s] nicho real SIN sim, otros niveles: %s' % (pn, F(summ(R, C, ds, nd))))
    P('  [%s] sim SIN relleno real emparejado: %s' % (pn, F(summ(Rs, ms & ~hit, ds, nd))))
for pn, ds in (('OOS', OOS),):
    for k, (lb, mm) in enumerate((('niv bb+1', niche & (off == 1)), ('niv bb', niche & (off == 0)), ('niv >bb+1', niche & (off > 1)))): P('  nicho real %s por nivel: %s' % (lb, F(summ(R, mm, ds, nd))))
    for lb, mm in (('fill <5 acc', niche & (R['sz'] < 5)), ('5-20', niche & (R['sz'] >= 5) & (R['sz'] < 20)), ('>=20', niche & (R['sz'] >= 20))): P('  nicho real tamano %s: %s' % (lb, F(summ(R, mm, ds, nd))))
    for lb, mm in (('retardo 5-20 s', niche & (R['dA'] < 20000)), ('20-60 s', niche & (R['dA'] >= 20000))): P('  nicho real %s: %s' % (lb, F(summ(R, mm, ds, nd))))
open(E4 + 'formula_r7_28oct/salida_r7c.txt', 'w').write('\n'.join(r6a.LINES))
