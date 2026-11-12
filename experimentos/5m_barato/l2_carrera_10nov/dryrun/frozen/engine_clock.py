#!/usr/bin/env python3
"""engine_clock.py -- DayEng (dev, sin editar) con RELOJ EXPLICITO. Modos (ver CONTRATO_RELOJES.md):
  'legacy' : todo en EXCHANGE (reproduce passT original: conocimiento = q_t_ex).  Solo para regresion.
  'causal' : CONOCIMIENTO (features de decision: bid/ask/b15/vol30 en la rejilla) en RECEPCION; MECANICA DE RELLENO (libro en llegada, cola por delante, prints, cancelacion) en EXCHANGE.
             Supuesto etiquetado: reloj local = UTC (chrony 0,2 ms) y t_arr = t_dec + 68 ms (RTT del POST, conservador) se compara con sellos EXCHANGE.
  'rx'     : todo en RECEPCION (cota 'solo lo verificable'; los rellenos se ven tarde: pesimista en cancelacion, optimista en llegada).
Solo se sobreescriben quotes()/feats()/__init__; el resto (run_segment, qupd, xa, sane, grid) es el de engine.py con la vista de relleno D."""
import sys, numpy as np, pandas as pd
import relojes as R
P2 = R.P2
sys.path.insert(0, P2 + 'escalera_B'); import engine as G

MODOS = {'legacy': ('ex', 'ex'), 'causal': ('ex', 'rx'), 'rx': ('rx', 'rx')}     # modo -> (reloj de relleno, reloj de conocimiento)


class DayEngClock(G.DayEng):
    def __init__(self, d, tape_mode, chain=None, bad_hours=None, universe=('ETH', 'SOL', 'XRP'), modo='legacy'):
        assert modo in MODOS, modo
        self.modo = modo; fc, kc = MODOS[modo]; self.clock_fill, self.clock_know = fc, kc
        self.capt = R.capt; self.d = d
        D = self.D = R.Day2(d, fc)                                           # vista de RELLENO (book/qupd/prints de run_segment)
        self.K = D if kc == fc else R.Day2(d, kc, light=True, with_otro=(kc == 'rx' and fc == 'ex'))                # vista de CONOCIMIENTO (solo bid/ask + trades para vol30)
        self.tape = G.Tape(tape_mode, D, chain); self.bad = bad_hours or set()
        self.day0 = int(pd.Timestamp(d, tz='UTC').timestamp()) * 1000; self.day1 = self.day0 + 86400000
        self.ks = [k for k in range(len(D.toks)) if D.marco[k] == '5min' and D.act[k] in universe]
        self.S = {}

    def _SK(self, k):
        if k not in self.S:
            K = self.K; a, b = K.tb[k], K.tb[k + 1]
            self.S[k] = np.concatenate([[0.0], np.cumsum(K.tsz[a:b].astype(np.float64))])
        return self.S[k]

    def quotes(self, k, times):
        K = self.K; a, b = K.qb[k], K.qb[k + 1]
        if b <= a: return np.full(len(times), np.nan), np.full(len(times), np.nan)
        j = np.searchsorted(K.qt[a:b], times, side='right') - 1; ok = j >= 0; jj = np.where(ok, j, 0)
        return np.where(ok, K.v0[a + jj], np.nan).astype(float), np.where(ok, K.v1[a + jj], np.nan).astype(float)

    def feats(self, k):
        """Igual que engine.DayEng.feats pero TODO con la vista de conocimiento K (mismo reloj para bid/ask, b15 y vol30)."""
        D = self.D; K = self.K; g = self.grid(k); fin = int(D.fin[k])
        bid, ask = self.quotes(k, g)
        f15 = int(np.ceil(fin / 900.0) * 900); k15 = D.t15.get((D.act[k], f15, D.lado[k]))
        b15 = self.quotes(k15, g)[0] if k15 is not None else np.full(len(g), np.nan)
        vol = np.zeros(len(g))
        for kk in (k, D.comp(k)):
            if kk is None: continue
            a, b = K.tb[kk], K.tb[kk + 1]
            if b > a: vol += G.vol30_vec(K.tt[a:b], self._SK(kk), g)
        hora = (g // 3600000) % 24
        return g, bid, ask, b15, vol, hora
