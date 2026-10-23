#!/usr/bin/env python3
"""s1_attach.py DIA -- une a las unidades de poblacion del dia (b_seleccion_adversa/datos/units/units_DIA.pkl) los rasgos de libro 5m/15m en t_obs = ts-4 s
leidos de m5_registro_DIA / m15_registro_DIA (asof por RECEPCION, sin look-ahead). Salida datalogs/q_techo/att_DIA.csv.gz (clave dia,maker,mkt,lado_c).
Reglas: missing = NaN (nunca 0). Solo lectura de las fuentes. Mismo formato de fila k/q/t que preal_extrae."""
import sys, os, gzip, io, subprocess, bisect, datetime as dt
from array import array
import numpy as np, pandas as pd
DIA = sys.argv[1]
UN = '/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/datos/units/units_%s.pkl' % DIA
OUT = '/root/polymarket-research-datalogs/q_techo/att_%s.csv.gz' % DIA
M5 = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz' % DIA
M15 = '/mnt/HC_Volume_106538179/m15_registro/m15_registro_%s.csv.gz' % DIA
LAG = 4.0
U = pd.read_pickle(UN).reset_index(drop=True)
U = U[['dia', 'maker', 'mkt', 'lado_c', 'act', 'fin', 'ts']].copy()
U['tobs'] = ((U.ts.values - LAG) * 1000).astype(np.int64)
U['fin15'] = (np.ceil(U.fin.values / 900.0) * 900).astype(np.int64)
def lee_k(src, marco):
    tm = {}
    p = subprocess.Popen("gzip -dc '%s' 2>/dev/null | grep -a '^k,'" % src, shell=True, stdout=subprocess.PIPE)
    for ln in p.stdout:
        f = ln.decode().rstrip('\n').split(',')
        if len(f) < 8 or f[4] != marco or f[3] not in ('ETH', 'SOL', 'XRP'): continue
        try: fin = int(dt.datetime.fromisoformat(f[6]).timestamp())
        except Exception: continue
        tm[f[2].encode()] = (f[3], f[5], fin, f[7])
    p.wait(); return tm
k5 = lee_k(M5, '5min'); k15 = lee_k(M15, '15min')
# indices de objetivo
key5 = {}; key15 = {}
for t, (c, mid, fin, lado) in k5.items(): key5[(int(mid), lado)] = t
for t, (c, mid, fin, lado) in k15.items(): key15[(c, fin, lado)] = t
sib = {}   # token 5m -> token hermano (mismo mid) para vol30ws
bym = {}
for t, (c, mid, fin, lado) in k5.items(): bym.setdefault(int(mid), []).append(t)
U['t5'] = [key5.get((int(m), l)) for m, l in zip(U.mkt, U.lado_c)]
U['t15'] = [key15.get((a, int(f), l)) for a, f, l in zip(U.act, U.fin15, U.lado_c)]
print(DIA, 'unidades', len(U), 'con token5', U.t5.notna().mean().round(4), 'con token15', U.t15.notna().mean().round(4), flush=True)
# cotas por token: [min(tobs)-41 s, max(tobs)]
LO = {}; HI = {}
def upd(t, lo, hi):
    if t is None: return
    LO[t] = min(LO.get(t, 1 << 62), lo); HI[t] = max(HI.get(t, 0), hi)
for t5, t15, to in zip(U.t5, U.t15, U.tobs.values):
    upd(t5, to - 41000, to); upd(t15, to - 41000, to)
# trades: por mercado (ambos tokens)
MK = {}
for t5, to, m in zip(U.t5, U.tobs.values, U.mkt.values):
    if t5 is None: continue
    for t in bym[int(m)]:
        upd(t, to - 41000, to)
PRE = {}; ROWS = {}; TR = {}
def lee_q(src, nombre):
    nq = nt = 0
    with gzip.open(src, 'rb') as f:
        for ln in io.BufferedReader(f, 1 << 22):
            c = ln[0]
            if c != 113 and c != 116: continue
            j = ln.find(b',', 16); tk = ln[16:j]
            lo = LO.get(tk)
            if lo is None: continue
            p = ln[j + 1:].rstrip(b'\n').split(b',')
            try:
                if c == 113: rv = int(p[4])
                else: rv = int(p[3])
            except Exception: continue
            if rv > HI[tk]: continue
            if c == 113:
                try: v = (rv, float(p[0]) if p[0] else np.nan, float(p[1]) if p[1] else np.nan, float(p[2]) if p[2] else np.nan, float(p[3]) if p[3] else np.nan)
                except Exception: continue
                if rv < lo:
                    o = PRE.get(tk)
                    if o is None or rv > o[0]: PRE[tk] = v
                else:
                    r = ROWS.get(tk)
                    if r is None: r = ROWS[tk] = [array('d') for _ in range(5)]
                    for q_, x_ in zip(r, v): q_.append(x_)
                    nq += 1
            else:
                if rv < lo: continue
                try: TR.setdefault(tk, []).append((rv, float(p[2])))
                except Exception: continue
                nt += 1
    print(nombre, 'q', nq, 't', nt, flush=True)
lee_q(M5, 'm5'); lee_q(M15, 'm15')
def arr(tk):
    r = ROWS.get(tk); pre = PRE.get(tk)
    a = np.stack([np.frombuffer(x, dtype=float) for x in r], 1) if r else np.zeros((0, 5))
    if pre is not None: a = np.vstack([np.array(pre, dtype=float)[None, :], a])
    if not len(a): return None
    return a[np.argsort(a[:, 0], kind='stable')]
CACHE = {}
def asof(tk, t_ms):
    if tk is None: return None
    if tk not in CACHE: CACHE[tk] = arr(tk)
    a = CACHE[tk]
    if a is None: return None
    j = np.searchsorted(a[:, 0], t_ms, side='right') - 1
    return a[j] if j >= 0 else None
TRA = {}
def trsum(tk, lo, hi):
    if tk not in TRA:
        r = TR.get(tk, []); TRA[tk] = np.array(sorted(r)) if r else np.zeros((0, 2))
    a = TRA[tk]
    if not len(a): return 0.0
    i0 = np.searchsorted(a[:, 0], lo, side='right'); i1 = np.searchsorted(a[:, 0], hi, side='right'); return float(a[i0:i1, 1].sum())
cols = ['bb', 'ba', 'bs', 'as_', 'qage', 'bb30', 'b15', 'a15', 'b15_30', 'vol30ws', 'q15age']
R = {c: np.full(len(U), np.nan) for c in cols}
for i, (t5, t15, to, m) in enumerate(zip(U.t5, U.t15, U.tobs.values, U.mkt.values)):
    s = asof(t5, to)
    if s is not None:
        R['bb'][i], R['ba'][i], R['bs'][i], R['as_'][i], R['qage'][i] = s[1], s[2], s[3], s[4], (to - s[0]) / 1000
        s2 = asof(t5, to - 30000)
        if s2 is not None: R['bb30'][i] = s2[1]
        R['vol30ws'][i] = sum(trsum(t, to - 30000, to) for t in bym[int(m)])
    s = asof(t15, to)
    if s is not None:
        R['b15'][i], R['a15'][i], R['q15age'][i] = s[1], s[2], (to - s[0]) / 1000
        s2 = asof(t15, to - 30000)
        if s2 is not None: R['b15_30'][i] = s2[1]
O = U[['dia', 'maker', 'mkt', 'lado_c']].copy()
for c in cols: O[c] = R[c]
tmp = OUT + '.tmp'; O.to_csv(tmp, index=False, compression='gzip'); os.replace(tmp, OUT)
print(DIA, 'guardado', len(O), 'cobertura bb', np.isfinite(O.bb).mean().round(4), 'b15', np.isfinite(O.b15).mean().round(4), 'vol30ws', np.isfinite(O.vol30ws).mean().round(4), flush=True)
