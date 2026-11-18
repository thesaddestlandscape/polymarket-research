#!/usr/bin/env python3
"""s4 (18-Nov, MECANISMO, NO EV): piloto descriptivo de 'evaporacion de nivel antes del casado' con libro5_ms (reloj = RECEPCION de d y T, mismo canal).
Evento = cluster de T (gap<300 ms) sobre un nivel de BID p en [0,10,0,30) de un token 5m BTC, via SELL del token a p (directo) o BUY del complementario a 1-p (mint).
Metricas por ventana W en {50,150,300,1000} ms antes del 1er T del cluster: tamano del nivel (replay B+d), masa cancelada neta = max(0, bajada del nivel - volumen impreso en ese nivel).
Placebo: instantes aleatorios (d-eventos) en el mismo token/nivel con nivel>0 y sin T en los siguientes 1000 ms. Uso: s4 FICHERO NLINEAS DIA_SONDA"""
import sys, gzip, json, bisect, random, collections, numpy as np, pandas as pd
f, N, D = sys.argv[1], int(sys.argv[2]), sys.argv[3]; random.seed(1)
comp = {}; rows = collections.defaultdict(dict)
for ch in pd.read_csv(f'/root/polymarket-research-datalogs/sonda1/pasivo/sonda1_fotos_l2_{D}.csv.gz', usecols=['slug', 'token', 'rol'], dtype=str, chunksize=200000):
    ch = ch[ch.slug.str.startswith('btc-updown-5m')].drop_duplicates(['slug', 'rol'])
    for r in ch.itertuples(): rows[r.slug][r.rol] = r.token
for s_, t in rows.items():
    if 'tok' in t and 'comp' in t: comp[t['tok']] = t['comp']; comp[t['comp']] = t['tok']
TK = set(comp)
def parse(s): return {round(float(a), 4): float(b) for a, b in (x.split(':') for x in s.split(';') if x)} if s else {}
lv = collections.defaultdict(dict)       # token -> {px: size}
H = collections.defaultdict(list)        # (token,px) -> [(rx, new_size)]
PV = collections.defaultdict(list)       # (token,px) -> [(rx, size impreso)]  (impresos en ese nivel de bid)
ev = []; plc_cand = []
def size_at(k, t):
    h = H.get(k)
    if not h: return None
    i = bisect.bisect_right(h, (t, 1e18)) - 1
    return h[i][1] if i >= 0 else None
def printed(k, a, b):
    pv = PV.get(k, []); return sum(s for (t, s) in pv if a < t <= b)
last = {}; raw = []
with gzip.open(f, 'rt') as fh:
    next(fh)
    for i, l in enumerate(fh):
        if i >= N: break
        p = l.rstrip('\n').split(',')
        t = p[0]
        if t == 'B' and p[2] in TK:
            b = parse(p[3]); tk = p[2]; r = int(p[6])
            for px, s in b.items():
                if px < 0.5: H[(tk, px)].append((r, s))
            for px in list(lv[tk]):
                if px not in b and px < 0.5: H[(tk, px)].append((r, 0.0))
            lv[tk] = b
        elif t == 'd' and p[2] in TK and p[3] == 'B':
            px = round(float(p[4]), 4); s = float(p[5]); r = int(p[6])
            if px < 0.5: H[(p[2], px)].append((r, s)); 
            if s > 0: lv[p[2]][px] = s
            else: lv[p[2]].pop(px, None)
        elif t == 'T' and p[2] in TK:
            px = round(float(p[3]), 4); r = int(p[6]); sz = float(p[5]); tk = p[2]
            if p[4] == 'SELL': kx = (tk, px)
            else: kx = (comp[tk], round(1 - px, 4))
            if 0.10 <= kx[1] < 0.30 - 1e-9:
                PV[kx].append((r, sz)); raw.append((kx, r, sz, 'dir' if p[4] == 'SELL' else 'mint'))
W = (50, 150, 300, 1000)
def feats(k, t):
    o = {}
    for w in W:
        a = size_at(k, t - w); b = size_at(k, t - 50 if w > 50 else t - 1)
        if a is None or b is None: o[w] = None; continue
        o[w] = (a, max(0.0, a - b - printed(k, t - w, t - 50 if w > 50 else t - 1)))
    return o
raw.sort(key=lambda x: x[1]); cl = []; 
for kx, r, sz, ty in raw:
    if cl and cl[-1]['k'] == kx and r - cl[-1]['t1'] < 300: cl[-1]['t1'] = r; cl[-1]['sz'] += sz; cl[-1]['n'] += 1
    else: cl.append(dict(k=kx, t0=r, t1=r, sz=sz, n=1, ty=ty))
res = collections.defaultdict(list)
for c in cl:
    pre = size_at(c['k'], c['t0'] - 150)
    if pre is None: res['sin_estado'].append(1); continue
    F = feats(c['k'], c['t0'])
    res['n'].append(1); res['pre_gt0'].append(pre > 0); res['pre_gt_sz'].append(pre > c['sz'] * 1.001); res['n_prints'].append(c['n'])
    for w in W:
        if F[w] is not None: res[f'canc_gt0_{w}'].append(F[w][1] > 0); res[f'canc_frac_{w}'].append(F[w][1] / F[w][0] if F[w][0] > 0 else np.nan)
# placebo: instantes (rx de d) en niveles de bid 0,10-0,30 con nivel>0, sin T en el nivel en +1000 ms
pl = collections.defaultdict(list); n_pl = 0
for k, h in H.items():
    if not (0.10 <= k[1] < 0.30 - 1e-9) or len(h) < 3: continue
    for (r, s) in random.sample(h, min(len(h), 20)):
        if s <= 0 or printed(k, r, r + 1000) > 0 or printed(k, r - 1000, r) > 0: continue
        F = feats(k, r); n_pl += 1
        for w in W:
            if F[w] is not None: pl[f'canc_gt0_{w}'].append(F[w][1] > 0); pl[f'canc_frac_{w}'].append(F[w][1] / F[w][0] if F[w][0] > 0 else np.nan)
out = {'clusters': len(cl), 'sin_estado': len(res['sin_estado']), 'tipos': dict(collections.Counter(c['ty'] for c in cl)),
       'pre150_gt0': float(np.mean(res['pre_gt0'])), 'pre_mayor_que_impreso': float(np.mean(res['pre_gt_sz'])), 'n_placebo': n_pl}
for w in W:
    out[f'W{w}'] = dict(evento_frac_con_cancel=float(np.mean(res[f'canc_gt0_{w}'])), evento_mediana_frac_cancel=float(np.nanmedian(res[f'canc_frac_{w}'])), n_ev=len(res[f'canc_gt0_{w}']),
                        placebo_frac_con_cancel=float(np.mean(pl[f'canc_gt0_{w}'])) if pl[f'canc_gt0_{w}'] else None, placebo_mediana_frac_cancel=float(np.nanmedian(pl[f'canc_frac_{w}'])) if pl[f'canc_frac_{w}'] else None)
offs = []
for c in cl:
    h = H.get(c['k'], []); 
    for j in range(1, len(h)):
        if abs(h[j][0] - c['t0']) <= 400 and h[j][1] < h[j - 1][1] - 1e-9: offs.append(h[j][0] - c['t0'])
out['offset_d_decrece_vs_primer_T_ms_pcts_1_10_25_50_75_90_99'] = [float(np.percentile(offs, q)) for q in (1, 10, 25, 50, 75, 90, 99)] if offs else None
out['n_decrementos_d_pm400ms'] = len(offs)
print(json.dumps(out, indent=1))
