#!/usr/bin/env python3
"""huerfana_exante: ejecuta las funciones de f6_sim.py (F7) con hooks minimos (parches de texto anotados) para las politicas
de momento de armado/cancelacion y extrae rasgos ex-ante. Uso: ps_run.py DIA [VARIANTES]  (PREREG.md manda).
Control de regresion: variante B parcheada == f6_sim_DIA.csv.gz (B)."""
import sys, hashlib, os, gzip, json, math, collections
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.dirname(HERE) + '/'
F7 = BASE + '../f7_precio_par/'
DAY = sys.argv[1]; VARS = (sys.argv[2] if len(sys.argv) > 2 else 'B,NB10,NB0,AC10,CB,SY,SN').split(',')
SRC = open(F7 + 'scripts/f6_sim.py').read()
assert hashlib.sha256(SRC.encode()).hexdigest() == 'ca2df7bd0c25b7fa7a6c0bf863c4ce11c4e82e3e9d7873109616d0c44df786ba', 'f6_sim.py cambiado'
head, tail = SRC.split("mk=collections.defaultdict(dict)")
PATCHES = [  # (original, nuevo) -- cada uno debe aparecer exactamente 1 vez
 ("st[l]=dict(tok=tk,", "st[l]=dict(l=l,tok=tk,"),                                                  # P1 lado en el estado
 ("    def post(S,t,top):\n", "    def post(S,t,top):\n        if not ARM(S,t,st): return\n"),     # P2 hook de armado
 ("live=t+LATP,cancel=1e18)", "live=t+LATP,cancel=1e18,arm=t)"),                                   # P3 instante de armado
 ("fills.append((t,l,o['price'],f))", "fills.append((t,l,o['price'],f,o['arm']))"),                # P4 fill con arm
 ("        if t>=t_post and not chk:", "        HOOK(S,t,st,cancel_live)\n        if t>=t_post and not chk:"),  # P5 historico touch + CB
 ("                    cancel_live(S2,t); post(S2,t+LATC,top); S2['capped']=capd",
  "                    if ARM(S2,t+LATC,st):\n                        cancel_live(S2,t); post(S2,t+LATC,top); S2['capped']=capd"),  # P6 NB: no cancelar lo vivo si no se rearma
]
for a, b in PATCHES:
    assert head.count(a) == 1, ('parche no unico', a)
    head = head.replace(a, b)

CUR = {'pol': None}
POLS = {'B': None, 'NB10': ('NB', 10000), 'NB0': ('NB', 0), 'AC10': ('AC', 10000), 'CB': ('CB', 0), 'SY': ('SIDE', 'YES'), 'SN': ('SIDE', 'NO')}
def barrido(S, t, L):
    th = S.get('th')
    if not th: return False
    tn = t - L; tw = tn - 5000
    i = len(th) - 1
    while i >= 0 and th[i][0] > tn: i -= 1
    if i < 0: return False
    cur = th[i][1]; mx = cur; j = i
    while j >= 0 and th[j][0] > tw: mx = max(mx, th[j][1]); j -= 1
    if j >= 0: mx = max(mx, th[j][1])
    return mx - cur >= 0.02 - 1e-9
def ARM(S, t, st):
    p = CUR['pol']
    if p is None: return True
    k = p[0]
    if k == 'NB': return not barrido(S, t, p[1])
    if k == 'AC': return S['posted'] or barrido(S, t, p[1])
    if k == 'CB': return not barrido(S, t, 0)
    if k == 'SIDE': return S['l'] == p[1] or st[p[1]]['inv'] > 0
    raise ValueError(k)
def HOOK(S, t, st, cancel_live):
    b = max(S['bids']) if S['bids'] else None
    th = S.setdefault('th', [])
    if b is not None and (not th or th[-1][1] != b): th.append((t, b))
    p = CUR['pol']
    if p and p[0] == 'CB' and S['posted'] and barrido(S, t, 0):
        if any(o['rem'] > 0 and o['cancel'] > t + 65 for o in S['orders']):
            cancel_live(S, t); S['anchor'] = None
ns = {'ARM': ARM, 'HOOK': HOOK, '__name__': 'f6_head'}
sys.argv = ['f6_sim.py', DAY, 'B']
exec(compile(head, 'f6_sim_head_patched', 'exec'), ns)
for v in POLS: ns['MARG'][v] = None
events, sim, TOK, DES, EV, parse_b, _C = ns['events'], ns['sim'], ns['TOK'], ns['DES'], ns['EV'], ns['parse_b'], ns['_C']
LATP = ns['LATP']

# ---- Binance BTC (recepcion c[7]) ----
prev = (pd.Timestamp(DAY) - pd.Timedelta(days=1)).strftime('%Y-%m-%d')
BN = None; parts = []
for dd in (prev, DAY):
    f_ = BASE + 'datos/bn_btc_%s.csv.gz' % dd
    if os.path.exists(f_): parts.append(pd.read_csv(f_, header=None, names=['t', 'p', 'q', 'r'], usecols=['p', 'r'], dtype={'p': np.float64, 'r': np.int64}))
if parts:
    a = pd.concat(parts).sort_values('r', kind='stable'); BN = (a.r.values, a.p.values)
def bn_feat(tc):
    out = {}
    if BN is None: return {k: np.nan for k in ('bn5', 'bn30', 'bn60', 'bnrng60', 'bn_edad')}
    r, p = BN; i = np.searchsorted(r, tc, side='right') - 1
    if i < 0 or tc - r[i] > 60000: return {k: np.nan for k in ('bn5', 'bn30', 'bn60', 'bnrng60', 'bn_edad')}
    p0 = p[i]; out['bn_edad'] = (tc - r[i]) / 1000.0
    for w, k in ((5, 'bn5'), (30, 'bn30'), (60, 'bn60')):
        j = np.searchsorted(r, tc - w * 1000, side='right') - 1
        out[k] = (p0 / p[j] - 1) * 1e4 if j >= 0 else np.nan
    j = np.searchsorted(r, tc - 60000, side='right'); seg = p[j:i + 1]
    out['bnrng60'] = (seg.max() - seg.min()) / p0 * 1e4 if len(seg) else np.nan
    return out

def book_feats(tok, tc):
    """estado del libro del token a tc (solo eventos con t<=tc)."""
    bids = {}; th = []; ev_t = []; tr = []
    for (t, k, p, q, sl, bs) in events(tok):
        if t > tc: break
        if k == 0:
            if bs: bids = parse_b(bs); ev_t.append(t)
        elif k == 1:
            if q <= 0: bids.pop(p, None)
            else: bids[p] = q
            ev_t.append(t)
        else: tr.append((t, p, q, sl))
        if bids:
            b = max(bids)
            if not th or th[-1][1] != b: th.append((t, b))
    if not bids: return None
    b = max(bids); lv = sorted(bids, reverse=True)
    f = {'touch': b, 'd1': bids[b], 'd3': sum(bids[x] for x in lv[:3])}
    for W in (5, 10, 30):
        tw = tc - W * 1000; mx = b
        for (tt, bb) in reversed(th):
            if tt > tw: mx = max(mx, bb)
            else: mx = max(mx, bb); break
        f['drop%d' % W] = mx - b
    for W in (30, 120):
        f['nev%d' % W] = sum(1 for x in ev_t if x > tc - W * 1000)
        f['ntr%d' % W] = sum(1 for x in tr if x[0] > tc - W * 1000)
        f['vtr%d' % W] = sum(x[2] for x in tr if x[0] > tc - W * 1000)
    return f
def feats_at(d, tc):
    fy = book_feats(d['YES'], tc); fn = book_feats(d['NO'], tc)
    if fy is None or fn is None: return None
    r = {}
    for pre, f in (('Y_', fy), ('N_', fn)):
        for k, v in f.items(): r[pre + k] = v
    r['spread'] = 1 - fy['touch'] - fn['touch']; r['mid'] = (fy['touch'] + 1 - fn['touch']) / 2
    r['absmid'] = abs(r['mid'] - 0.5); r['favY'] = int(fy['touch'] > fn['touch'])
    r['lr_d3'] = math.log((fy['d3'] + 1) / (fn['d3'] + 1))
    r.update(bn_feat(tc)); return r

mk = collections.defaultdict(dict)
for tok in EV: mk[TOK[tok][2]][TOK[tok][4]] = tok
frows = []; mrows = []; nvalid = 0
for mid, d in mk.items():
    _C.clear()
    if 'YES' not in d or 'NO' not in d or mid not in DES: continue
    if os.environ.get('PS_LIM') and nvalid >= int(os.environ['PS_LIM']): break
    fin = TOK[d['YES']][3]; t_post = (fin - 300) * 1000 + 2000 + LATP
    res = {}; ok0 = True
    for vn in VARS:
        CUR['pol'] = POLS[vn]
        fl, ok = sim(d, fin, vn)
        if vn == VARS[0] and not ok: ok0 = False; break
        res[vn] = fl
    if not ok0: continue
    nvalid += 1
    for vn, fl in res.items():
        for (t, l, p, a, arm) in fl:
            frows.append((DAY, mid, l, vn, t, p, a, p * a, a * (DES[mid] == l) - p * a, 0.014 * (1 - p) * p * a, arm))
    f0 = feats_at(d, t_post - 10000)
    row = {'dia': DAY, 'mkt': mid, 'fin': fin, 'tc': t_post - 10000}
    if f0: row.update(f0)
    # primera pata de B: primera orden rellena; rasgos en su instante de armado - 10 s
    fb = sorted(res.get('B', []))
    if fb:
        t1, l1, p1, a1, arm1 = fb[0]; row.update({'f1_l': l1, 'f1_p': p1, 'f1_t': t1, 'f1_arm': arm1, 'f1_T': (fin * 1000 - arm1) / 1000.0})
        f1 = feats_at(d, arm1 - 10000)
        if f1: row.update({'a_' + k: v for k, v in f1.items()})
    mrows.append(row)
    if nvalid % 20 == 0: print(DAY, 'mercados', nvalid, flush=True)
FR = pd.DataFrame(frows, columns=['dia', 'mid', 'lc', 'var', 't', 'pc', 'acc', 'coste', 'pnl', 'reb', 'arm'])
FR.to_csv(BASE + 'datos/ps_fills_%s.csv.gz' % DAY, index=False)
pd.DataFrame(mrows).to_csv(BASE + 'datos/ps_feat_%s.csv.gz' % DAY, index=False)
# regresion B vs f6_sim
ref = pd.read_csv(F7 + 'datos/f6_sim_%s.csv.gz' % DAY); ref = ref[(ref['var'] == 'B') & ref.mid.isin(set(FR.mid.astype(int)))]
mine = FR[FR['var'] == 'B']
key = lambda X: sorted(zip(X.mid.astype(str), X.lc, X.t.astype(np.int64), X.pc.round(2), X.acc.round(6)))
same = key(ref) == key(mine)
msg = f'{DAY} mercados validos {nvalid} (F7: ver f6_log) fills B ref {len(ref)} mio {len(mine)} IDENTICO={same}'
print(msg); open(BASE + 'datos/ps_regresion_%s.txt' % DAY, 'w').write(msg + '\n')
