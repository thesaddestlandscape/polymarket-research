#!/usr/bin/env python3
"""e1c_pob.py -- EXTRA de potencia (NO preregistrado en PREREG_E1C; regla fijada ANTES de mirar: la elegida en TRAIN de F1, BN_W300_X2).
Proxy poblacional: TODOS los rellenos de bids (prints que golpean bids) en banda 0,10-0,30 de ETH/SOL/XRP 5m del libro5 L2 (cola_vs_cruce/mk, 20-22 Oct).
Bandera = Binance se movio >=2 bps en contra en 300 ms en algun instante de [t_print-LOOK, t_print-90] (rejilla 10 ms, recepcion).
Mide (gana - p) y pnl por accion de los rellenos con bandera vs sin bandera, IC90 por cierre, placebo desplazando la serie Binance +-30..120 s.
NO sustituye la orden propia (no se conoce la vida de la orden ni la cola). Salida datos/e1c_pob.txt"""
import os, sys, json, gzip, glob, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); OUT = '/root/polymarket-research-datalogs/e1_cancelacion_ms/'
sys.path.insert(0, AQ); import e1c_senales as S
MK = '/root/polymarket-research-datalogs/cola_vs_cruce/mk/'; TM = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json'))
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
MF = {}
for tok, (act, mid, lado, fin) in TM.items(): MF[(act, mid)] = fin
BN = S.carga_bn(); rng = np.random.default_rng(7)
def flag(s, t, Lside, look, shift=0):
    g = (t[:, None] + np.arange(-look, -89, 10)[None, :]).ravel() + shift
    p1 = S.last_val(s[0], s[1], g); p0 = S.last_val(s[0], s[1], g - 300); ret = ((p1 / p0 - 1) * 1e4).reshape(len(t), -1)
    return (ret <= -2).any(1) if Lside == 'Y' else (ret >= 2).any(1)
rows = []
for f in sorted(glob.glob(MK + '*.gz')):
    act, mid = os.path.basename(f)[:-3].split('_'); fin = MF.get((act, mid)); w = DES.get(mid)
    if fin is None or w is None or act not in BN: continue
    pr = {'Y': [], 'N': []}
    with gzip.open(f, 'rt', errors='replace') as fh:
        try:
            for ln in fh:
                if ',T,' not in ln: continue
                c = ln.rstrip('\n').split(',')
                if len(c) < 6 or c[1] != 'T': continue
                try: L, r, side, q, a = c[0], int(c[2]), c[3], int(round(float(c[4]) * 1000)), float(c[5])
                except ValueError: continue
                if side == 'SELL': pr[L].append((r, q, a))
                elif side == 'BUY': pr['N' if L == 'Y' else 'Y'].append((r, 1000 - q, a))
        except (EOFError, OSError): pass
    for L in 'YN':
        x = np.array(sorted(pr[L]), float).reshape(-1, 3)
        x = x[(x[:, 1] > 100) & (x[:, 1] <= 300) & (x[:, 0] / 1000 < fin)]
        if not len(x): continue
        gana = 1.0 if ((L == 'Y') == (w == 'YES')) else 0.0
        t = x[:, 0].astype(np.int64); s = BN[act]
        f1 = flag(s, t, L, 1000); f3 = flag(s, t, L, 3000)
        sh = rng.integers(30000, 120001, len(t)) * rng.choice([-1, 1], len(t))
        fp = flag(s, t, L, 1000, sh[0])                     # un desplazamiento por mercado-lado (placebo)
        for i in range(len(t)):
            rows.append((act, mid, fin, L, t[i], x[i, 1] / 1000, x[i, 2], gana, int(f1[i]), int(f3[i]), int(fp[i])))
X = pd.DataFrame(rows, columns=['act', 'mid', 'fin', 'L', 't', 'p', 'acc', 'gana', 'f1', 'f3', 'fp'])
X['dia'] = pd.to_datetime(X.fin, unit='s').dt.strftime('%Y-%m-%d'); X['pnl'] = (X.gana - X.p) * X.acc; X['coste'] = X.p * X.acc
X.to_csv(OUT + 'pob_rellenos.csv.gz', index=False)
out = []
def P(*a): out.append(' '.join(map(str, a))); print(*a)
P(f'rellenos de bid 0,10-0,30 con desenlace: {len(X)} prints, {X.groupby(["mid","L"]).ngroups} mercado-lado, {X.fin.nunique()} cierres, dias {sorted(X.dia.unique())}')
def ev(d): return d.pnl.sum() / d.coste.sum() if len(d) else np.nan
def boot(d, col, nb=1000):
    gi = {c: g for c, g in d.groupby('fin')}; cl = list(gi); v = []
    for _ in range(nb):
        s = pd.concat([gi[c] for c in rng.choice(cl, len(cl))]); v.append(ev(s[s[col] == 1]) - ev(s[s[col] == 0]))
    return np.quantile(v, [0.05, 0.95])
for col, lab in (('f1', 'look 1 s'), ('f3', 'look 3 s'), ('fp', 'PLACEBO desplazado look 1 s')):
    a = X[X[col] == 1]; b = X[X[col] == 0]; lo, hi = boot(X, col)
    P(f'{lab}: con bandera {len(a)} ({len(a)/len(X):.3f}) EV€ {ev(a):+.3f} hit-p {(a.gana-a.p).mean():+.3f} | sin {len(b)} EV€ {ev(b):+.3f} hit-p {(b.gana-b.p).mean():+.3f} | dif EV IC90 cierre ({lo:+.3f},{hi:+.3f})')
    for (ac, dia), g in X.groupby(['act', 'dia']):
        a = g[g[col] == 1]; b = g[g[col] == 0]
        if col != 'fp': P(f'   {ac} {dia}: con {len(a)} EV {ev(a):+.3f} | sin {len(b)} EV {ev(b):+.3f}')
open(os.path.join(D, 'e1c_pob.txt'), 'w').write('\n'.join(out) + '\n')
