#!/usr/bin/env python3
"""(3) Ingeniería inversa del rival que se lleva el ask V4: cada orden TOMADORA on-chain (resumen is_tk=1) de las wallets rivales en BTC 5m
se casa con su operación del WS del CLOB (misma token, BUY, precio ±0,011, hora del exchange en [bloque-6 s, bloque]) para obtener
su hora de casado en ms (ex) y de recepción (rx). Rasgos en el instante de ENVÍO acotado (ex - 150 ms, retraso tomador mínimo, SUPUESTO):
Binance en reloj E (lo que él puede ver colocado) y en reloj rx (lo que vemos nosotros), libro 5m (s y contrario) y 15m (mismo lado).
Placebo: 20 instantes uniformes por fill dentro de la vida del mismo 5m (T 10-295 s). Salida: rival_D.csv en el volumen."""
import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
from simlib import *
D = sys.argv[1]
O3 = os.environ.get('SIM_OUT', O + 'r3_out/'); os.makedirs(O3, exist_ok=True)
W = {'0x9783f45ce35f794be38ca47dd0816a5c241383b9': 'R1_9783', '0xe38cc08b122dc5fdf21ebd936059cb47f30def5b': 'R2_e38c',
     '0x27e99389f6fd80cbc414f39a33e58425b3fac5b7': 'R3_27e9'}
fo = O3 + f'rival_{D}.csv'
if os.path.exists(fo): print('ya hecho'); sys.exit()
f = pd.read_parquet('/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/' + f'fills_{D}.parquet',
                    columns=['is_tk', 'maker', 'side', 'tok', 'act', 'mkt', 'lado', 'fin', 'ts', 'maker_amt', 'taker_amt', 'fee'])
f = f[(f.is_tk == 1) & f.maker.isin(W) & (f.side == 0) & (f.act == 'BTC')].copy()
f['p'] = f.maker_amt / f.taker_amt
byg = {}
for r in f.itertuples():
    g = -(-int(r.fin) // 900) * 900
    byg.setdefault(g, []).append(r)
km = kmap(D); B = binance(D)
k15 = {(C, l): v[0] for (mar, C, l), v in km.items() if mar == '15min'}
k5 = {(C, l): v[0] for (mar, C, l), v in km.items() if mar == '5min'}
rng = np.random.default_rng(int(D.replace('-', '')))
OUT = []
def estado(q, t, clock):
    ts = q.ex if clock == 'ex' else q.rx
    j = np.searchsorted(ts, t, side='right') - 1
    return (np.nan,) * 4 if j < 0 else (q.bid[j], q.ask[j], q.bsz[j], q.asz[j])
def feats(t_send, tok5, toko, tok15, sgn, QS):
    out = {}
    for w in (250, 500, 1000, 3000):
        out[f'E{w}'] = float(sgn * bin_ret(B, np.array([t_send]), w, 'E')[0])
        out[f'R{w}'] = float(sgn * bin_ret(B, np.array([t_send]), w, 'rx')[0])
    out['E_fwd150'] = float(sgn * bin_ret(B, np.array([t_send + 150]), 150, 'E')[0])
    for nom, tk in (('s5', tok5), ('o5', toko), ('s15', tok15)):
        q = QS.get(tk)
        b, a, bs, as_ = estado(q, t_send, 'ex') if q is not None and len(q.ex) else (np.nan,) * 4
        b1, a1, _, _ = estado(q, t_send - 1000, 'ex') if q is not None and len(q.ex) else (np.nan,) * 4
        out[f'{nom}_bid'], out[f'{nom}_ask'], out[f'{nom}_asz'], out[f'{nom}_da1s'], out[f'{nom}_db1s'] = b, a, as_, a - a1, b - b1
    return out
for g, QS, TS in grupos(D):
    if g not in byg: continue
    for r in byg[g]:
        C = int(r.fin); sl = r.lado; tok5 = r.tok; toko = k5.get((C, 'NO' if sl == 'YES' else 'YES')); tok15 = k15.get((g, sl))
        t = TS.get(tok5)
        if t is None or not len(t.ex): continue
        blk = int(r.ts * 1000)
        c = np.where(t.buy & (t.ex >= blk - 6000) & (t.ex <= blk) & (np.abs(t.p - r.p) <= 0.011))[0]
        if not len(c): OUT.append(dict(dia=D, w=W[r.maker], cierre=C, lado=sl, p=r.p, acc=r.taker_amt, match=0)); continue
        sc = np.abs(t.sz[c] - r.taker_amt) / max(r.taker_amt, 1) + np.abs((blk - 2400) - t.ex[c]) / 3000
        j = c[np.argmin(sc)]
        ex, rx = int(t.ex[j]), int(t.rx[j]); sgn = 1 if sl == 'YES' else -1
        gana = None if str(r.mkt) not in DES else DES[str(r.mkt)] == sl
        base = dict(dia=D, w=W[r.maker], cierre=C, lado=sl, p=round(r.p, 4), acc=r.taker_amt, usd=r.maker_amt, fee=r.fee, gana=gana, match=1,
                    ex=ex, rx=rx, T=round(C - ex / 1000, 2), nested=int(C % 900 == 0), placebo=0)
        base.update(feats(ex - 150, tok5, toko, tok15, sgn, QS)); OUT.append(base)
        for tp in rng.uniform((C - 295) * 1000, (C - 10) * 1000, 5):
            pb = dict(dia=D, w=W[r.maker], cierre=C, lado=sl, match=1, placebo=1, ex=int(tp), T=round(C - tp / 1000, 2), nested=int(C % 900 == 0))
            pb.update(feats(int(tp) - 150, tok5, toko, tok15, sgn, QS)); OUT.append(pb)
cols = list(dict.fromkeys(k for o in OUT for k in o))
with open(fo + '.tmp', 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(OUT)
os.replace(fo + '.tmp', fo)
print(D, 'filas', len(OUT), 'rival fills', len(f), 'casados', sum(1 for o in OUT if o.get('match') and not o.get('placebo')))
