#!/usr/bin/env python3
"""agg.py OUT - agrega OUT/dia_*.json y OUT/tb_*.txt.
(1) tb.py por dia (BTC 5m, T y K, >=0,80) y agrupado por dias.  (2) Rejilla H3 franja x bucket 0,05 x rol x moneda: EV/EUR ponderado,
IC90 POR DIAS (bootstrap 2000), EV sin los 2 mejores dias (por pnl EUR), dias +/-, sign-flip por dias (10.000, una cola), BH-FDR y
max-statistic (z por celda, flips conjuntos) por familia declarada.  LIMPIO = 08-Oct..03-Nov (dias no usados para elegir la franja);
DESCUBRIMIENTO = 04-05 Nov (contaminados: ahi se eligio la franja).  (3) CF1 segun prereg d74fae89: DESC 05..25-Oct descriptivo;
FRESCO (>=27-Oct con m5_onchain del dia siguiente) -> solo n y cobertura hasta 10 dias; gate completo solo con >=10 dias frescos."""
import json, glob, os, sys, re, ast, math, datetime as dt
import numpy as np
O = sys.argv[1]; VD = '/mnt/HC_Volume_106538179/m5_onchain'
fs = sorted(glob.glob(O + '/dia_*.json')); days = [os.path.basename(f)[4:14] for f in fs]
J = {d: json.load(open(f)) for d, f in zip(days, fs)}
avail = {os.path.basename(f)[11:21] for f in glob.glob(VD + '/m5_onchain_*.csv.gz')}
nxt = lambda d: (dt.date.fromisoformat(d) + dt.timedelta(days=1)).isoformat()
CLEAN = [d for d in days if '2026-10-08' <= d <= '2026-11-03']; DISC = [d for d in days if d in ('2026-11-04', '2026-11-05')]
DESC = [d for d in days if '2026-10-05' <= d <= '2026-10-25']; FRESH = [d for d in days if d >= '2026-10-27' and nxt(d) in avail]
COINS = sorted({k.split('|')[2] for d in days for k in J[d]['grid']})
LINES = []; RES = {}
def pr(*a):
    s = ' '.join(str(x) for x in a); LINES.append(s); print(s, flush=True)
exp = [(dt.date(2026, 10, 8) + dt.timedelta(i)).isoformat() for i in range(29)]
pr('dias', len(days), 'faltan', [d for d in exp if d not in days], 'maxfilas>0 (prueba):', [d for d in days if J[d].get('maxfilas')])
pr('monedas', COINS, '| LIMPIO', len(CLEAN), '| DESC', len(DESC), '| FRESCO', FRESH)
for d in days:
    s = J[d]['st']; pr('st', d, {k: (round(v) if isinstance(v, float) else v) for k, v in s.items()})

def okg(d, co):
    v = J[d]['covg'].get(co); return bool(v) and v[1] > 0 and v[0] / v[1] >= 0.99
pr('rejilla: moneda x dia con cobertura de desenlace <99 % del $ (excluidos):',
   [(d, co, round(J[d]['covg'][co][0] / J[d]['covg'][co][1], 4)) for d in days for co in COINS if co in J[d]['covg'] and not okg(d, co)])
BANDS = {'pre': ['pre'], '0-30': ['0-30'], '30-120': ['30-120'], '120-240': ['120-240'], '240-300': ['240-300'],
         '30-240': ['30-120', '120-240'], 'ALL': ['ALL']}
def bk(s): return {'ge80': [16, 17, 18, 19], 'le20': [0, 1, 2, 3], 'ge90': [18, 19]}.get(s) or [int(s)]
def cell(d, role, mode, coin, band, b):
    g = J[d]['grid']; p = c = n = 0.
    for co in (COINS if coin == 'ALLC' else [coin]):
        if not okg(d, co): continue
        for bd in BANDS[band]:
            for x in bk(b):
                v = g.get(f'{role}|{mode}|{co}|{bd}|{x}')
                if v: p += v[0]; c += v[1]; n += v[2]
    return p, c, n
def mats(cells, ds):
    A = np.array([[cell(d, *k) for k in cells] for d in ds], dtype=float).reshape(len(ds), len(cells), 3)
    return A[:, :, 0], A[:, :, 1], A[:, :, 2]
def bh(p):
    p = np.nan_to_num(np.asarray(p, float), nan=1.0); n = len(p); o = np.argsort(p)
    q = p[o] * n / np.arange(1, n + 1); q = np.minimum.accumulate(q[::-1])[::-1]; out = np.empty(n); out[o] = np.minimum(q, 1); return out
def mstats(cells, ds, seed=20261106, B=2000, NF=10000):
    P, C, N = mats(cells, ds); nd = len(ds); rng = np.random.default_rng(seed); Ct = C.sum(0)
    with np.errstate(all='ignore'):
        ev = np.where(Ct > 0, P.sum(0) / np.where(Ct > 0, Ct, 1), np.nan)
        W = rng.multinomial(nd, np.full(nd, 1 / nd), size=B); evb = (W @ P) / (W @ C)
        lo = np.nanpercentile(evb, 5, axis=0); hi = np.nanpercentile(evb, 95, axis=0)
        idx = np.argsort(-P, axis=0)[:2]; M = np.ones_like(P)
        for j in range(P.shape[1]): M[idx[:, j], j] = 0
        ev2 = (P * M).sum(0) / (C * M).sum(0)
        S = rng.choice([-1., 1.], size=(NF, nd)); evf = (S @ P) / np.where(Ct > 0, Ct, np.nan)
        p1 = ((evf >= ev[None, :]).sum(0) + 1) / (NF + 1); p1[~np.isfinite(ev)] = 1.0
        sd = np.nanstd(evf, axis=0); z = np.where(sd > 0, ev / sd, np.nan); zf = evf / np.where(sd > 0, sd, np.nan)
        mx = np.nanmax(np.where(np.isfinite(zf), zf, -np.inf), axis=1)
        pm = ((mx[:, None] >= z[None, :]).sum(0) + 1) / (NF + 1); pm[~np.isfinite(z)] = 1.0
    q = bh(p1)
    return [dict(cell='|'.join(k), ev=ev[j], lo=lo[j], hi=hi[j], ev_sin2=ev2[j], dpos=int((P[:, j] > 0).sum()), dneg=int((P[:, j] < 0).sum()),
                 usd=Ct[j], nu=int(N[:, j].sum()), p=p1[j], q=q[j], pmax=pm[j]) for j, k in enumerate(cells)]
def fmt(r): return (f"{r['cell']:34s} EV {r['ev']:+.4f} IC90d [{r['lo']:+.4f},{r['hi']:+.4f}] sin2 {r['ev_sin2']:+.4f} d+/- {r['dpos']}/{r['dneg']} "
                    f"$ {r['usd']:>11,.0f} u {r['nu']:>6} p {r['p']:.4f} qBH {r['q']:.3f} pmax {r['pmax']:.3f}")
def dstats(ka, kb, ds, seed=20261106, B=2000):
    P, C, _ = mats([ka, kb], ds); nd = len(ds); rng = np.random.default_rng(seed); W = rng.multinomial(nd, np.full(nd, 1 / nd), size=B)
    with np.errstate(all='ignore'):
        e = P.sum(0) / C.sum(0); eb = (W @ P) / (W @ C); dd = eb[:, 0] - eb[:, 1]
    return e[0] - e[1], np.nanpercentile(dd, 5), np.nanpercentile(dd, 95)
def evday(k, d):
    p, c, _ = cell(d, *k); return p / c if c > 0 else float('nan')

# ---------------- (1) tb.py por dia ----------------
TB = {}
for f in sorted(glob.glob(O + '/tb_*.txt')):
    for l in open(f):
        m = re.match(r"^(\S+) (\(.*?\)) (\(.*\))\s*$", l)
        if m: TB[(m.group(1),) + ast.literal_eval(m.group(2))] = ast.literal_eval(m.group(3))
if TB:
    pr('\n=== (1) tb.py tal cual (BTC 5m, compras literales, unidad wallet-token-franja, IC90 por mercados del propio tb.py) ===')
    ks = [('K', '30-120', '>=0.80'), ('K', '120-240', '>=0.80'), ('T', '30-120', '>=0.80'), ('T', '120-240', '>=0.80'), ('K', '240-300', '>=0.80'), ('K', '0-30', '>=0.80')]
    pr('dia        ' + ' | '.join(f'{k[0]}{k[1]}' for k in ks))
    for d in days:
        pr(d, ' | '.join((f"{TB[(d,)+k][3]:+.4f}" if (d,) + k in TB else '   NA  ') for k in ks))
    for nm, ds in (('LIMPIO', CLEAN), ('DESCUB', DISC)):
        for k in ks:
            v = [(TB[(d,) + k][3] * TB[(d,) + k][2], TB[(d,) + k][2]) for d in ds if (d,) + k in TB and TB[(d,) + k][2] > 0]
            if len(v) < 2: continue
            a = np.array(v); rng = np.random.default_rng(20261106); W = rng.multinomial(len(a), np.full(len(a), 1 / len(a)), size=2000)
            eb = (W @ a[:, 0]) / (W @ a[:, 1])
            pr(f'tb {nm} {k}: dias {len(a)} EV {a[:,0].sum()/a[:,1].sum():+.4f} IC90d [{np.percentile(eb,5):+.4f},{np.percentile(eb,95):+.4f}] d+/- {(a[:,0]>0).sum()}/{(a[:,0]<0).sum()} $ {a[:,1].sum():,.0f}')
    for d in DISC:
        pr('tb crudo', d, {k: TB.get((d,) + k) for k in ks[:4]})

# ---------------- (2) rejilla H3 ----------------
if len(CLEAN) >= 2:
    pr('\n=== (2) Rejilla H3 sobre LIMPIO (%d dias %s..%s); unidad mercado-lado; EV ponderado por $ ===' % (len(CLEAN), CLEAN[0], CLEAN[-1]))
    QB = ['0-30', '30-120', '120-240', '240-300']
    F32 = [(r, 'lit', 'BTC', b, str(x)) for r in 'KT' for b in QB for x in (16, 17, 18, 19)]
    R32 = mstats(F32, CLEAN); pr('-- Familia F32 (BTC lit, K/T x 4 franjas x 4 buckets >=0,80): 32 celdas; BH y max-stat dentro de F32')
    for r in R32: pr(fmt(r))
    F160 = [(r, 'lit', 'BTC', b, str(x)) for r in 'KT' for b in QB for x in range(20)]
    R160 = mstats(F160, CLEAN); sig = [r for r in R160 if r['q'] < 0.10 or r['pmax'] < 0.10]
    pr('-- Familia F160 (BTC lit, K/T x 4 franjas x 20 buckets): celdas con qBH<0,10 o pmax<0,10:', len(sig))
    for r in sig: pr(fmt(r))
    F192 = [(r, 'lit', co, b, str(x)) for co in COINS for r in 'KT' for b in QB for x in (16, 17, 18, 19)]
    R192 = mstats(F192, CLEAN); sig = [r for r in R192 if r['q'] < 0.10 or r['pmax'] < 0.10]
    pr('-- Familia F%d (%d monedas x K/T x 4 franjas x 4 buckets >=0,80): qBH<0,10 o pmax<0,10:' % (len(F192), len(COINS)), len(sig))
    for r in sig: pr(fmt(r))
    pr('-- Titulares (agregados, sin corregir; placebo = otras franjas y ALL; inversion = <=0,20 misma franja; eq = compras U ventas)')
    HB = ['pre', '0-30', '30-120', '120-240', '30-240', '240-300', 'ALL']
    H = [(r, m, 'BTC', b, bb) for m in ('lit', 'eq') for bb in ('ge80', 'le20', 'ge90') for r in 'KT' for b in HB]
    RH = mstats(H, CLEAN)
    for r in RH: pr(fmt(r))
    RES['titulares_limpio'] = RH
    pr('-- Por moneda, >=0,80 lit (LIMPIO); BH dentro de esta tabla')
    PC = [(r, 'lit', co, b, 'ge80') for co in COINS + ['ALLC'] for r in 'KT' for b in ('30-120', '120-240', '30-240', 'ALL')]
    for r in mstats(PC, CLEAN): pr(fmt(r))
    pr('-- Diferencias con remuestreo conjunto de dias (LIMPIO): EV_a - EV_b [IC90d]')
    for ka, kb in [(('K', 'lit', 'BTC', '30-240', 'ge80'), ('K', 'lit', 'BTC', 'ALL', 'ge80')),
                   (('K', 'lit', 'BTC', '30-240', 'ge80'), ('T', 'lit', 'BTC', '30-240', 'ge80')),
                   (('K', 'lit', 'BTC', '30-120', 'ge80'), ('K', 'lit', 'BTC', '240-300', 'ge80')),
                   (('K', 'lit', 'BTC', '120-240', 'ge80'), ('K', 'lit', 'BTC', '240-300', 'ge80')),
                   (('T', 'lit', 'BTC', '30-240', 'ge80'), ('T', 'lit', 'BTC', 'ALL', 'ge80'))]:
        e, lo, hi = dstats(ka, kb, CLEAN); pr(f"{'|'.join(ka)} - {'|'.join(kb)}: {e:+.4f} [{lo:+.4f},{hi:+.4f}]")
    pr('-- EV diario (LIMPIO + DESCUB) BTC lit >=0,80: K30-120 K120-240 T30-120 T120-240 K_ALL T_ALL | $K30-240')
    DK = [('K', 'lit', 'BTC', '30-120', 'ge80'), ('K', 'lit', 'BTC', '120-240', 'ge80'), ('T', 'lit', 'BTC', '30-120', 'ge80'),
          ('T', 'lit', 'BTC', '120-240', 'ge80'), ('K', 'lit', 'BTC', 'ALL', 'ge80'), ('T', 'lit', 'BTC', 'ALL', 'ge80')]
    for d in CLEAN + DISC:
        pr(d, ' '.join(f'{evday(k, d):+.4f}' for k in DK), f"| {cell(d, 'K', 'lit', 'BTC', '30-240', 'ge80')[1]:,.0f}")
    if DISC:
        pr('-- DESCUBRIMIENTO (04-05 Nov; contaminado, solo 2 dias, sin IC por dias): EV agrupado')
        for k in DK + [('K', 'lit', 'BTC', '30-240', 'ge80'), ('T', 'lit', 'BTC', '30-240', 'ge80')]:
            P = sum(cell(d, *k)[0] for d in DISC); C = sum(cell(d, *k)[1] for d in DISC)
            pr('|'.join(k), f'EV {P / C:+.4f}' if C > 0 else 'NA', f'$ {C:,.0f}')
        cand = [r for r in R32 if r['cell'].startswith('K|lit|BTC|30-120') or r['cell'].startswith('K|lit|BTC|120-240')]
        best = max(cand, key=lambda r: r['ev']); k = tuple(best['cell'].split('|'))
        P = sum(cell(d, *k)[0] for d in DISC); C = sum(cell(d, *k)[1] for d in DISC)
        pr('-- Mejor celda K 30-240 elegida en LIMPIO:', fmt(best), '| en DESCUB:', f'{P / C:+.4f}' if C > 0 else 'NA')

# ---------------- (3) CF1 ----------------
def okc(d, co):
    v = J[d]['covc'].get(co); return (not v) or v[1] <= 0 or v[0] / v[1] >= 0.99
def agsum(d, f):
    p = c = r = n = 0.
    for k, v in J[d]['ag'].items():
        t = k.split('|')
        if okc(d, t[1]) and f(*t): p += v[0]; c += v[1]; r += v[2]; n += v[3]
    return p, c, r, n
CELLS = {'A_DEEP': lambda bc, co, sb, cl, *r: bc == 'FAV' and cl == 'DEEP', 'A_MID': lambda bc, co, sb, cl, *r: bc == 'FAV' and cl == 'MID',
         'A_TOP': lambda bc, co, sb, cl, *r: bc == 'FAV' and cl == 'TOP',
         'B_DEEP': lambda bc, co, sb, cl, *r: bc == 'FAV' and co == 'BTC' and sb in ('0.90-0.95', '0.95-0.99') and cl == 'DEEP',
         'B_MID': lambda bc, co, sb, cl, *r: bc == 'FAV' and co == 'BTC' and sb in ('0.90-0.95', '0.95-0.99') and cl == 'MID',
         'B_TOP': lambda bc, co, sb, cl, *r: bc == 'FAV' and co == 'BTC' and sb in ('0.90-0.95', '0.95-0.99') and cl == 'TOP'}
def dser(ds, f): return np.array([agsum(d, f) for d in ds]).reshape(len(ds), 4)
def ic_dias(a, b=None, B=2000, seed=20261026):
    rng = np.random.default_rng(seed); n = len(a); W = rng.multinomial(n, np.full(n, 1 / n), size=B)
    with np.errstate(all='ignore'):
        e = (W @ a[:, 0]) / (W @ a[:, 1])
        if b is not None: e = e - (W @ b[:, 0]) / (W @ b[:, 1])
    return np.nanpercentile(e, 5), np.nanpercentile(e, 95)
def closes(ds, nm):
    acc = {}
    for d in ds:
        for k, v in J[d]['cl'].items():
            c, cl, co = k.split('|')
            if c == nm and okc(d, co): a = acc.setdefault(cl, [0., 0.]); a[0] += v[0]; a[1] += v[1]
    return np.array(list(acc.values())).reshape(-1, 2)
def ic_cierres(a, B=1000, seed=20261026):
    rng = np.random.default_rng(seed); n = len(a); W = rng.multinomial(n, np.full(n, 1 / n), size=B)
    with np.errstate(all='ignore'): e = (W @ a[:, 0]) / (W @ a[:, 1])
    return np.nanpercentile(e, 5), np.nanpercentile(e, 95)
def signo(a, NF=10000, seed=20261026):
    e = a[a[:, 1] > 0, 0] / a[a[:, 1] > 0, 1]; rng = np.random.default_rng(seed); S = rng.choice([-1., 1.], size=(NF, len(e)))
    return ((S @ e) / len(e) >= e.mean()).mean()
def sin2(a):
    o = np.argsort(-a[:, 0])[2:]; return a[o, 0].sum() / a[o, 1].sum()
def cf1(ds, nombre, modo):
    pr(f'\n=== (3) CF1 {nombre}: {len(ds)} dias {ds[0] if ds else ""}..{ds[-1] if ds else ""} (modo {modo}) ===')
    pr('cobertura CF1 <99 % del $ por moneda x dia (excluidos):',
       [(d, co, round(v[0] / v[1], 4)) for d in ds for co, v in J[d]['covc'].items() if v[1] > 0 and v[0] / v[1] < 0.99])
    S = {nm: dser(ds, f) for nm, f in CELLS.items()}
    for nm, a in S.items(): pr(f'{nm}: rellenos {int(a[:,3].sum())} $ {a[:,1].sum():,.0f}')
    shA = S['A_DEEP'][:, 1].sum() / sum(S[x][:, 1].sum() for x in ('A_DEEP', 'A_MID', 'A_TOP'))
    shB = S['B_DEEP'][:, 1].sum() / max(1e-9, sum(S[x][:, 1].sum() for x in ('B_DEEP', 'B_MID', 'B_TOP')))
    pr(f'cuota DEEP del $ maker: A {shA:.3f} B {shB:.3f}')
    if modo == 'n': return
    R = {}
    for nm in ('A_DEEP', 'A_TOP', 'B_DEEP', 'B_TOP'):
        a = S[nm]; ev = a[:, 0].sum() / a[:, 1].sum(); lo, hi = ic_dias(a); clo, chi = ic_cierres(closes(ds, nm))
        R[nm] = dict(ev=ev, lo=lo, hi=hi, clo=clo, chi=chi, p=signo(a), sin2=sin2(a), dpos=int((a[:, 0] > 0).sum()), dneg=int((a[:, 0] < 0).sum()), reb=a[:, 2].sum() / a[:, 1].sum())
        pr(f"{nm}: EV {ev:+.4f} IC90dia [{lo:+.4f},{hi:+.4f}] IC90cierre [{clo:+.4f},{chi:+.4f}] signo p {R[nm]['p']:.4f} sin2 {R[nm]['sin2']:+.4f} d+/- {R[nm]['dpos']}/{R[nm]['dneg']} rebate/$ {R[nm]['reb']:+.4f}")
    dlo, dhi = ic_dias(S['A_DEEP'], S['A_TOP']); pr(f"A DEEP-TOP: {R['A_DEEP']['ev']-R['A_TOP']['ev']:+.4f} IC90dia [{dlo:+.4f},{dhi:+.4f}]")
    pcm = {}
    for co in COINS:
        u = [x for d in ds for x in J[d]['un'] if okc(d, x[1]) and x[0] == 'FAV' and x[3] == 'DEEP' and x[1] == co]
        if u: pcm[co] = (len(u), sum(x[4] for x in u) / sum(x[5] for x in u))
    pr('por moneda DEEP (unidades mercado-lado-clase-subbanda, EV):', {k: (v[0], round(v[1], 4)) for k, v in pcm.items()})
    rd = []
    for nm, fa, fb in [('MINT-CRUCE', lambda bc, co, sb, cl, ct, *r: bc == 'FAV' and cl == 'DEEP' and ct == 'MINT', lambda bc, co, sb, cl, ct, *r: bc == 'FAV' and cl == 'DEEP' and ct == 'CRUCE'),
                       ('FAV-CTRL', CELLS['A_DEEP'], lambda bc, co, sb, cl, *r: bc == 'CTRL' and cl == 'DEEP')] + \
                      [(f'sub {s}', (lambda s: lambda bc, co, sb, cl, *r: bc == 'FAV' and cl == 'DEEP' and sb == s)(s), None) for s in ('0.70-0.80', '0.80-0.90', '0.90-0.95', '0.95-0.99')] + \
                      [(f'T {t}', (lambda t: lambda bc, co, sb, cl, ct, tb, *r: bc == 'FAV' and cl == 'DEEP' and tb == t)(t), None) for t in ('(5,60]', '(60,150]', '(150,300]')] + \
                      [('sin W/MM', lambda bc, co, sb, cl, ct, tb, sz, wm: bc == 'FAV' and cl == 'DEEP' and wm == 'O', None)]:
        a = dser(ds, fa); b = dser(ds, fb) if fb else None
        if a[:, 1].sum() <= 0 or (b is not None and b[:, 1].sum() <= 0): continue
        ev = a[:, 0].sum() / a[:, 1].sum() - (b[:, 0].sum() / b[:, 1].sum() if b is not None else 0); lo, hi = ic_dias(a, b)
        dd = (a[:, 0] / np.where(a[:, 1] > 0, a[:, 1], np.nan)) - ((b[:, 0] / np.where(b[:, 1] > 0, b[:, 1], np.nan)) if b is not None else 0)
        dd = dd[np.isfinite(dd)]; rng = np.random.default_rng(20261026); Sg = rng.choice([-1., 1.], size=(10000, len(dd)))
        p = ((Sg @ dd) / len(dd) >= dd.mean()).mean() if len(dd) else 1.0; rd.append((nm, ev, lo, hi, p, a[:, 1].sum()))
    for (nm, ev, lo, hi, p, usd), q in zip(rd, bh([x[4] for x in rd])):
        pr(f'lectura {nm}: {ev:+.4f} IC90dia [{lo:+.4f},{hi:+.4f}] p {p:.4f} qBH {q:.3f} $ {usd:,.0f}')
    c = closes(ds, 'A_DEEP'); u = np.array([[x[4], x[5]] for d in ds for x in J[d]['un'] if okc(d, x[1]) and x[0] == 'FAV' and x[3] == 'DEEP']).reshape(-1, 2)
    o = np.argsort(-u[:, 0]); k1 = int(math.ceil(0.01 * len(u))); wc = c[np.argmin(c[:, 0])] if len(c) else np.array([0., 0.])
    pr(f"salvaguardas A_DEEP: peor cierre {c[:,0].min():,.1f} $, peor dia {S['A_DEEP'][:,0].min():,.1f} $, EV sin 1 % mejores unidades {u[o[k1:],0].sum()/u[o[k1:],1].sum():+.4f}, "
       f"EV con peor cierre duplicado {(c[:,0].sum()+wc[0])/(c[:,1].sum()+wc[1]):+.4f}")
    rac = {}
    for d in ds:
        for k, v in J[d]['cl'].items():
            cn, cl, co = k.split('|')
            if cn == 'A_DEEP' and okc(d, co) and v[0] < 0: rac[cl] = rac.get(cl, 0) + 1
    pr(f'racimo: cierres con >=2 monedas DEEP perdedoras {sum(1 for v in rac.values() if v >= 2)} de {len(c)} cierres con DEEP')
    if modo == 'gate':
        A, Bc = R['A_DEEP'], R['B_DEEP']
        okAB = all(x['ev'] >= 0.02 and x['lo'] > 0 and x['clo'] > 0 and x['p'] < 0.01 and x['sin2'] > 0 for x in (A, Bc))
        okmon = sum(1 for co, v in pcm.items() if v[0] >= 200 and v[1] > 0) >= 4
        pasa = len(ds) >= 10 and okAB and dlo > 0 and okmon
        refut = len(ds) >= 10 and A['hi'] < 0.01 and Bc['hi'] < 0.01
        ver = ('PASA' if shA >= 0.02 else 'PASA_SIN_CAPACIDAD') if pasa else ('REFUTADA' if refut else 'INSUFICIENTE')
        pr(f'VEREDICTO CF1 ({len(ds)} dias frescos): {ver} | okAB {okAB} DEEP-TOP>0 {dlo > 0} monedas>=4 {okmon}')
        RES['cf1_veredicto'] = ver
cf1(DESC, 'DESC (descriptivo, no decide)', 'desc')
cf1(FRESH, 'FRESCO', 'gate' if len(FRESH) >= 10 else 'n')
if len(FRESH) < 10: pr(f'CF1 FRESCO: {len(FRESH)} dias (<10): segun §4 solo n y cobertura; la 1a mirada exige el m5_onchain del dia siguiente al 10o dia fresco.')
open(O + '/resultado.txt', 'w').write('\n'.join(LINES) + '\n')
json.dump(RES, open(O + '/resultado.json', 'w'), default=float, indent=0)
