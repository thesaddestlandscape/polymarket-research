#!/usr/bin/env python3
"""relojes.py -- capa de datos con RELOJ EXPLICITO sobre sa_ms2/ms2_DIA.npz (ms_extract_v2.py). Solo lectura. Contrato: CONTRATO_RELOJES.md.
Day2(d, clock) = misma interfaz que capt.Day (dev, solo importado, no editado) pero con la linea de tiempo elegida:
    clock='ex' -> q_t/t_t = sello del EXCHANGE (== sa_ms v1, para regresion);  clock='rx' -> RECEPCION local (filas sin rx se descartan y se cuentan en s.n_sin_rx).
    s.otro(i) / s.tt_otro = el OTRO reloj alineado fila a fila con s.qt / s.tt (para convertir de forma explicita y etiquetada, nunca implicita).
light=True: solo bid/ask (v0, v1) -- suficiente para las vistas de CONOCIMIENTO (features de decision)."""
import sys, os, numpy as np, pandas as pd
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'
sys.path.insert(0, P2 + 'capturabilidad_A_R1ws')
import capt                                              # solo importado (dev no se edita)
DL = os.environ.get('SA2_DL', '/root/polymarket-research-datalogs/')
SA2 = os.environ.get('SA2_OUT', DL + 'sa_ms2/')


class Day2(capt.Day):
    def __init__(s, d, clock='ex', light=False, with_otro=False):
        assert clock in ('ex', 'rx'), clock
        z = np.load(SA2 + f'ms2_{d}.npz', allow_pickle=True)
        s.clock = clock; s.toks = list(z['tokens']); t0 = int(z['t0']); s.t0 = t0
        m = pd.DataFrame(z['tmap'], columns=['act', 'marco', 'mid', 'fin', 'lado'])
        s.fin = m.fin.map(lambda x: int(pd.Timestamp(x).timestamp())).values; s.act = m.act.values; s.marco = m.marco.values; s.mid = m.mid.values; s.lado = m.lado.values
        s.tokidx = {t: i for i, t in enumerate(s.toks)}
        s.t5 = {(s.mid[i], s.lado[i]): i for i in range(len(s.toks)) if s.marco[i] == '5min'}
        s.t15 = {(s.act[i], s.fin[i], s.lado[i]): i for i in range(len(s.toks)) if s.marco[i] == '15min'}
        n = len(s.toks)
        qk = z['q_k']; ex = z['q_t_ex']; rx = z['q_t_rx']                                   # int32 relativos a t0 (poca memoria)
        vs = ['q_v0', 'q_v1'] if light else ['q_v0', 'q_v1', 'q_v2', 'q_v3']
        V = {j: z[j] for j in vs}; s._otro = None
        if clock == 'ex':
            s.n_sin_rx = int((rx < 0).sum()); s.qt = ex.astype(np.int64) + t0
            if with_otro: s._otro = rx.copy()                                                # rx relativo (-1 = sin rx)
        else:
            ok = rx >= 0; s.n_sin_rx = int((~ok).sum())
            if s.n_sin_rx: qk = qk[ok]; ex = ex[ok]; rx = rx[ok]; V = {j: v[ok] for j, v in V.items()}
            o = np.lexsort((rx, qk)).astype(np.int32)                                         # (k, rx); lexsort es estable: empate = orden de fichero
            qk = qk[o]; s.qt = rx[o].astype(np.int64) + t0; del rx
            if with_otro: s._otro = ex[o]
            del ex
            for j in list(V): V[j] = V[j][o]
            del o
        ex = rx = None
        s.qk = qk; s.qb = np.searchsorted(qk, np.arange(n + 1))
        for j in range(4): setattr(s, f'v{j}', V.get(f'q_v{j}'))
        tk = z['t_k']; tex = z['t_t_ex'].astype(np.int64); trx = z['t_t_rx'].astype(np.int64); pr = z['t_pr']; sd = z['t_sd']; sz = z['t_sz']
        if clock == 'rx':
            ok = trx >= 0; tk, tex, trx, pr, sd, sz = tk[ok], tex[ok], trx[ok], pr[ok], sd[ok], sz[ok]; main, oth = trx, tex
        else:
            main, oth = tex, np.where(trx >= 0, trx + t0, -1) - t0
        o = np.lexsort((np.arange(len(main)), main, tk.astype(np.int64)))
        s.tk = tk[o]; s.tt = main[o] + t0; s.tt_otro = oth[o] + t0; s.tp = pr[o]; s.tsd = sd[o]; s.tsz = sz[o]
        s.tb = np.searchsorted(s.tk, np.arange(n + 1)); s.cs = np.cumsum(s.tsz.astype(np.float64))
        del z

    def otro(s, i):
        """Sello del OTRO reloj (absoluto, ms) de la fila q i de esta vista (-1 si falta). Requiere with_otro=True."""
        v = int(s._otro[i]); return v + s.t0 if v >= 0 else -1


def desfase_q(d):
    """Utilidad de calibracion: (k, t_ex, t_rx) de las filas q con rx valido, en ms absolutos. Lee el npz v2 sin construir Day2."""
    z = np.load(SA2 + f'ms2_{d}.npz', allow_pickle=True); t0 = int(z['t0'])
    rx = z['q_t_rx'].astype(np.int64); ok = rx >= 0
    return z['q_k'][ok], z['q_t_ex'].astype(np.int64)[ok] + t0, rx.astype(np.int64)[ok] + t0
