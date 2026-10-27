#!/usr/bin/env python3
"""e1d_pob.py -- PREREG_E1D (sha en prereg/PREREG_E1D.sha256). Paso 1: construye rellenos de bid poblacionales (banda 0,10-0,30, 5m ETH/SOL/XRP) de
DL/e1_cancelacion_ms/reg/D.gz con bandera BN_W300_X2 (latencia real) y lead, y la tabla de ventanas (mercados) con rasgos R1-R5 conocidos en t0.
Salida DL/e1_cancelacion_ms/e1d_rellenos.csv.gz, e1d_ventanas.csv.gz; log con hora; reanudable por dia (e1d_dia_D.pkl)."""
import os, sys, glob, json, gzip, hashlib, time, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__))
H = open(os.path.join(AQ, '..', 'prereg', 'PREREG_E1D.sha256')).read().split()[0]
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_E1D.md'), 'rb').read()).hexdigest() == H
OUT = '/root/polymarket-research-datalogs/e1_cancelacion_ms/'; REG = OUT + 'reg/'; LOG = OUT + 'e1d.log'
DES = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
DES.update(json.load(open(os.path.join(AQ, '../../salida/datos/desenlaces_extra.json'))))   # mismo origen gamma closed=true (como e1q_sim)
DES.update(json.load(open('/root/polymarket-research-datalogs/e1_cancelacion_ms/desenlaces_e1d.json')))   # faltantes, gamma closed=true (e1d_desenlaces.py)
def log(*a):
    with open(LOG, 'a') as f: f.write(time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()) + ' ' + ' '.join(map(str, a)) + '\n')
def lv(ta, va, t):
    i = np.searchsorted(ta, t, 'right') - 1; return np.where(i >= 0, va[np.maximum(i, 0)], np.nan)
dias = sorted(os.path.basename(f)[:-3] for f in glob.glob(REG + '2026-10-??.gz'))
# mapa global de tokens (k puede venir en otro dia)
K = {}
for d in dias:
    with gzip.open(REG + d + '.gz', 'rt') as fh:
        for ln in fh:
            if ln.startswith('k,'):
                c = ln.rstrip('\n').split(',')
                K[c[2]] = (c[3], c[5], pd.Timestamp(c[6]).timestamp(), c[7])
OPP = {}
for tok, (coin, mid, fin, lado) in K.items(): OPP[(mid, lado)] = tok
log('dias', dias, 'tokens', len(K))
prev_x = {}
for d in dias:
    pk = OUT + f'e1d_dia_{d}.pkl'
    T = []; X = []; nbad = 0
    with gzip.open(REG + d + '.gz', 'rt') as fh:
        for ln in fh:
            if ln[0] == 't':
                c = ln.rstrip('\n').split(',')
                try:
                    if c[2] in K: T.append((int(c[1]), c[2], float(c[3]), c[4], float(c[5])))
                except (ValueError, IndexError): nbad += 1
            elif ln[0] == 'x':
                c = ln.rstrip('\n').split(',')
                try: X.append((int(c[1]), c[2], float(c[3])))
                except (ValueError, IndexError): nbad += 1
    Xd = pd.DataFrame(X, columns=['r', 'c', 'p']).sort_values('r', kind='stable')
    BN = {}
    for c in ('ETH', 'SOL', 'XRP'):
        a = Xd[Xd.c == c][['r', 'p']].values
        if c in prev_x: a = np.concatenate([prev_x[c], a])
        a = a[np.argsort(a[:, 0], kind='stable')]; BN[c] = (a[:, 0].astype(np.int64), a[:, 1])
        if len(a): prev_x[c] = a[a[:, 0] >= a[-1, 0] - 3700 * 1000]
    del X, Xd
    if os.path.exists(pk): log(d, 'ya hecho'); continue
    Td = pd.DataFrame(T, columns=['r', 'tok', 'p', 'side', 'acc']).drop_duplicates()
    ndup = len(T) - len(Td); del T
    Td['coin'] = Td.tok.map(lambda t: K[t][0]); Td['mid'] = Td.tok.map(lambda t: K[t][1]); Td['fin'] = Td.tok.map(lambda t: K[t][2]); Td['lado'] = Td.tok.map(lambda t: K[t][3])
    sell = Td.side == 'SELL'
    Td['lado_m'] = np.where(sell, Td.lado, np.where(Td.lado == 'YES', 'NO', 'YES')); Td['q'] = np.where(sell, Td.p, 1 - Td.p).round(3)
    F = Td[(Td.q > 0.10 + 1e-9) & (Td.q <= 0.30 + 1e-9) & (Td.r / 1000 < Td.fin) & (Td.r / 1000 >= Td.fin - 300)].copy()
    F['w'] = F.mid.map(DES); nsin = int(F.w.isna().sum()); F = F[F.w.notna()]
    F['gana'] = (F.lado_m == F.w).astype(float); F['pnl'] = (F.gana - F.q) * F.acc; F['coste'] = F.q * F.acc
    F['flag'] = 0; F['lead'] = np.nan
    for c, g in F.groupby('coin'):
        ta, pa = BN[c]
        if not len(ta): F.loc[g.index, 'flag'] = -1; continue
        t = g.r.values.astype(np.int64); off = np.arange(-1000, 1, 10)
        G = t[:, None] + off[None, :]; p1 = lv(ta, pa, G); p0 = lv(ta, pa, G - 300); ret = (p1 / p0 - 1) * 1e4
        up = (g.lado_m.values == 'YES')[:, None]; fire = np.where(up, ret <= -2, ret >= 2)
        ok = fire[:, :-9].any(1)                                     # g <= t-90
        first = np.where(fire.any(1), fire.argmax(1), -1); lead = np.where(first >= 0, -off[np.maximum(first, 0)], np.nan)
        age = t - ta[np.maximum(np.searchsorted(ta, t, 'right') - 1, 0)]
        F.loc[g.index, 'flag'] = ok.astype(int); F.loc[g.index, 'lead'] = lead; F.loc[g.index, 'bn_age'] = age
    F['dia'] = d
    # ventanas: mercados con algun token del dia (cierre dentro del dia)
    W = []
    for (coin, mid), fin in {(v[0], v[1]): v[2] for v in K.values()}.items():
        if pd.Timestamp(fin, unit='s').strftime('%Y-%m-%d') != d: continue
        t0 = int((fin - 300) * 1000); ta, pa = BN[coin]
        def vol(sec):
            g = np.arange(t0 - sec * 1000, t0 + 1, 10000); p = lv(ta, pa, g); r = np.diff(np.log(p)); return float(np.nanstd(r) * 1e4) if np.isfinite(r).sum() > 5 else np.nan
        p_now = lv(ta, pa, np.array([t0]))[0]; p15 = lv(ta, pa, np.array([t0 - 900000]))[0]
        W.append(dict(coin=coin, mid=mid, fin=fin, dia=d, R1=vol(900), R2=vol(3600), R3=abs(np.log(p_now / p15)) * 1e4 if p15 > 0 else np.nan, R4=int(pd.Timestamp(fin - 300, unit='s').hour // 4), R5=coin))
    pd.to_pickle((F[['dia', 'coin', 'mid', 'fin', 'lado_m', 'r', 'q', 'acc', 'gana', 'pnl', 'coste', 'flag', 'lead', 'bn_age']], pd.DataFrame(W)), pk)
    log(d, 'rellenos', len(F), 'filas malas', nbad, 'dup', ndup, 'sin desenlace', nsin, 'ventanas', len(W))
Fs = []; Ws = []
for d in dias:
    pk = OUT + f'e1d_dia_{d}.pkl'
    if os.path.exists(pk): f, w = pd.read_pickle(pk); Fs.append(f); Ws.append(w)
pd.concat(Fs).to_csv(OUT + 'e1d_rellenos.csv.gz', index=False); pd.concat(Ws).to_csv(OUT + 'e1d_ventanas.csv.gz', index=False); log('escrito')
