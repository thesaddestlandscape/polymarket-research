#!/usr/bin/env python3
"""cosechar_sim.py -- simulador cronologico de COSECHAR PARES AL ABRIR (v3, 22-Oct): maker en ambos tokens de un 5m en los primeros 15 s,
bid b = round(PAR/2, 2), 5 acc/lado, pata suelta hasta T-10 s, desenlace OFICIAL, reembolso maker aparte. Todo por hora de RECEPCION.
Modelo de cola (calibrado con las ordenes reales de B, s4_calib_B): cola_adelante = F * (tamano del bid en ese nivel al entrar); trades que llenan = SELL del
token a p<=b o BUY del contrario a p'>=1-b (equivalente); p<b atraviesa, p==b llena lo que supere la cola; ventana de impresion + GRACE_MS tras la cancelacion
(las impresiones del WS de mercado llegan ~0-1 s despues del relleno real). Regimenes: OPT (F=0), BASE (F=1), CONS (solo atravesar: nunca llena en el nivel).
Defensas: A0, A_BN (Binance de la moneda >=2 bps en 1 s, solo mientras ninguna pata tenga relleno; recoloca 2 s despues si sigue en los primeros 15 s),
B_15 (bid del 15m del mismo lado cambia >=0,02 en 500 ms; solo 5m con 15m). Ventanas Binance reiniciadas en saltos >60 s (trampa m5_registro).
"""
import os, sys, bisect, numpy as np, pandas as pd
OUT = '/root/polymarket-research-datalogs/m5_cosechar_abrir'
DEC_MS, LPOST_MS, LCANCEL_MS, GRACE_MS = 50, 100, 60, 1000
ENTRADA_MS, T_FIN_MS, REARME_MS = 15000, 10000, 2000
APERTURA_MS = 13500   # corte 'rellenos de apertura' para comparar con T>285 on-chain (hora de bloque ~2,4 s despues del casado + retraso de impresion)
SH = 5.0; EPS = 1e-6; INF = float('inf')
COINS = ('BTC', 'ETH', 'SOL', 'XRP')
REGIMES = {'OPT': (0.0, GRACE_MS), 'BASE': (1.0, GRACE_MS), 'CONS': (None, 0)}   # (F, grace) ; F None = solo atravesar

class Dia5:
    def __init__(self, coin, d):
        z = np.load(f'{OUT}/ms5_{coin}_{d}.npz', allow_pickle=False)
        self.coin = coin; self.d = d; self.D0 = int(z['D0']); self.tokens = z['tokens']; self.tmap = z['tmap']
        self.qr = z['qr'].astype(np.int64) + self.D0; self.qk = z['qk']; self.qv = z['qv']
        self.tr = z['tr'].astype(np.int64) + self.D0; self.tk = z['tk']; self.tv = z['tv']
        self.xr = z['xr'].astype(np.int64) + self.D0; self.xv = z['xv']
        n = len(self.tokens)
        self.qs = np.searchsorted(self.qk, np.arange(n + 1)); self.ts = np.searchsorted(self.tk, np.arange(n + 1))
        self.tokix = {str(t): i for i, t in enumerate(self.tokens)}
        self.idx = {}
        for i, (act, marco, mid, fin, lado) in enumerate(self.tmap):
            if str(act) != coin: continue
            self.idx[(str(marco), int(pd.Timestamp(str(fin)).timestamp()), str(lado))] = i
        self._trig_bn = None
    def top(self, k, t):
        a, b = self.qs[k], self.qs[k + 1]
        j = np.searchsorted(self.qr[a:b], t, 'right') - 1
        if j < 0: return None
        v = self.qv[a + j]; return float(v[0]), float(v[1]), float(v[2]), float(v[3])
    def trig_bn(self, bps=2.0):
        if self._trig_bn is None:
            r, p = self.xr, self.xv
            if len(r) < 3: self._trig_bn = np.zeros(0, np.int64); return self._trig_bn
            j = np.searchsorted(r, r - 1000, 'right') - 1
            ok = (j >= 0) & (r - r[np.maximum(j, 0)] <= 3000) & (r[np.maximum(j, 0)] <= r - 1000)
            # saltos >60 s en la serie: la referencia no puede cruzar el salto
            gap = np.concatenate([[0], np.cumsum(np.diff(r) > 60000)])
            ok &= gap == gap[np.maximum(j, 0)]
            ret = np.abs(p - p[np.maximum(j, 0)]) / p[np.maximum(j, 0)] * 1e4
            self._trig_bn = r[ok & (ret >= bps)]
        return self._trig_bn
    def trig_15(self, k15, t_ini, t_fin, thr=0.02, win=500):
        a, b = self.qs[k15], self.qs[k15 + 1]
        r = self.qr[a:b]; bid = self.qv[a:b, 0]
        i0, i1 = np.searchsorted(r, t_ini, 'left'), np.searchsorted(r, t_fin, 'right')
        out = []
        for i in range(i0, i1):
            j = np.searchsorted(r, r[i] - win, 'right') - 1
            if j >= 0 and abs(bid[i] - bid[j]) >= thr - 1e-9: out.append(int(r[i]))
        return out

def eventos_llenado(D, k, ko, precio, t_a, t_b):
    """(t, p_equiv, sz) ordenados: SELL del token k a p<=precio y BUY del contrario a p' => SELL a 1-p'; solo los que pueden llenar (p_equiv<=precio)."""
    ev = []
    for kk, comp in ((k, False), (ko, True)):
        if kk is None: continue
        a, b = D.ts[kk], D.ts[kk + 1]
        r = D.tr[a:b]; i0, i1 = np.searchsorted(r, t_a, 'right'), np.searchsorted(r, t_b, 'right')
        if i1 <= i0: continue
        v = D.tv[a + i0:a + i1]
        if comp: m = v[:, 1] == 1; pe = np.round(1.0 - v[:, 0].astype(np.float64), 4)
        else: m = v[:, 1] == 0; pe = np.round(v[:, 0].astype(np.float64), 4)
        m &= pe <= precio + 1e-6
        if m.any():
            for t_, p_, s_ in zip(r[i0:i1][m], pe[m], v[:, 2][m]): ev.append((int(t_), float(p_), float(s_)))
    ev.sort()
    return ev

def simular_pata(D, k, ko, precio, size, t_post, t_cancel_eff, F, grace):
    """fills [(t, acc)] de una puja maker `precio` viva en [t_post, t_cancel_eff] (+grace de impresion). F None = solo atravesar."""
    top = D.top(k, t_post)
    if top is None: return []
    bid, ask, bsz, _ = top
    t_b = t_cancel_eff + grace
    q0 = INF; t_conv = None
    if F is None:
        q0 = INF
    elif precio > bid + EPS or bid != bid: q0 = 0.0
    elif abs(precio - bid) < EPS: q0 = F * bsz
    else:
        # nivel por debajo del mejor bid: cola desconocida hasta que el bid baje a nuestro nivel
        a, b = D.qs[k], D.qs[k + 1]
        r = D.qr[a:b]; bb = D.qv[a:b, 0]
        i0 = np.searchsorted(r, t_post, 'right')
        m = bb[i0:] <= precio + EPS
        if m.any():
            j = i0 + int(np.argmax(m)); t_conv = int(r[j])
            q0 = 0.0 if bb[j] < precio - EPS else F * float(D.qv[a + j, 2])
    ev = eventos_llenado(D, k, ko, precio, t_post, t_b)
    fills = []; thr = 0.0; vol = 0.0; lvl = 0.0; tot = 0.0
    for t, pe, sz in ev:
        falta = size - tot
        if falta <= 1e-9: break
        if pe < precio - 1e-6:
            n = min(falta, sz)
        else:
            if t_conv is not None and t < t_conv: continue
            if q0 == INF: continue
            vol += sz
            cand = max(0.0, vol - q0)
            new = min(cand, size - (tot - lvl))
            n = new - lvl
            if n <= 1e-12: continue
            lvl = new
        if n > 1e-12:
            fills.append((t, n)); tot += n
    return fills

def simular_mercado(D, kY, kN, fin_ms, mid, par, defensa, reg, k15Y=None, k15N=None, t_off_ms=0):
    """Una politica sobre un mercado: devuelve dict con rellenos por pata. t_off_ms>0 = CONTROL temporal (arranca en la ventana + t_off)."""
    F, grace = REGIMES[reg]
    b = None if par == 'JOIN' else round(par / 2.0, 2)
    t0 = fin_ms - 300000 + t_off_ms
    t_end = fin_ms - T_FIN_MS
    tokens = {'YES': (kY, kN), 'NO': (kN, kY)}
    trig = []
    if defensa == 'A_BN':
        tb = D.trig_bn(); trig = [int(x) for x in tb[np.searchsorted(tb, t0, 'left'):np.searchsorted(tb, t0 + ENTRADA_MS + 3000, 'right')]]
    elif defensa == 'B_15':
        if k15Y is None or k15N is None: return None
        trig = sorted(set(D.trig_15(k15Y, t0, t0 + ENTRADA_MS + 3000) + D.trig_15(k15N, t0, t0 + ENTRADA_MS + 3000)))
    seg_ini = t0 + DEC_MS
    res = None
    for _ in range(12):
        t_post = seg_ini + LPOST_MS
        legs = {}; px = {}
        for lado, (k, ko) in tokens.items():
            tp = D.top(k, seg_ini)
            bl = b if b is not None else (tp[0] if tp is not None and tp[0] == tp[0] else None)
            if tp is None or bl is None or not (0.01 <= bl < tp[1] - EPS): legs[lado] = None; continue
            legs[lado] = simular_pata(D, k, ko, bl, SH, t_post, t_end + LCANCEL_MS, F, grace)
            px[lado] = bl
        t_primer = min([f[0][0] for f in legs.values() if f] or [INF])
        nxt = next((x for x in trig if x > seg_ini and x + DEC_MS + LCANCEL_MS < t_primer), None) if defensa != 'A0' else None
        if nxt is None:
            res = legs; break
        seg_ini = nxt + REARME_MS
        if seg_ini > t0 + ENTRADA_MS:
            res = {'YES': None, 'NO': None, 'defendido': True}; break
    if res is None: res = legs
    return res, px

def unidad(res, px, des, t0=None):
    qY = sum(a for _, a in (res.get('YES') or [])); qN = sum(a for _, a in (res.get('NO') or []))
    bY, bN = px.get('YES', 0.0), px.get('NO', 0.0)
    cost = qY * bY + qN * bN
    win = qY if des == 'YES' else qN
    rb = 0.2 * 0.07 * (bY * (1 - bY) * qY + bN * (1 - bN) * qN)
    tY = res['YES'][0][0] if res.get('YES') else None; tN = res['NO'][0][0] if res.get('NO') else None
    q15 = {}
    for lado in ('YES', 'NO'):
        q15[lado] = sum(a for t, a in (res.get(lado) or []) if t0 is not None and t <= t0 + APERTURA_MS)
    c15 = q15['YES'] * bY + q15['NO'] * bN; w15 = q15['YES'] if des == 'YES' else q15['NO']
    return dict(q15Y=q15['YES'], q15N=q15['NO'], cost15=c15, pnl15=w15 - c15, qY=qY, qN=qN, cost=cost, pnl=win - cost, reemb=rb, bY=bY, bN=bN, tY=tY, tN=tN,
                opY=res.get('YES') is not None, opN=res.get('NO') is not None, defendido=bool(res.get('defendido')))
