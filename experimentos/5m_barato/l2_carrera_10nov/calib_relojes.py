#!/usr/bin/env python3
"""calib_relojes.py DIA [DIA...] -- calibracion del desfase RECEPCION - SELLO EXCHANGE por dia / hora / tipo de mensaje (q = cambio de top del libro, t = trade WS), desde sa_ms2/ms2_DIA.npz.
Salida: out_v2/calib_relojes_<DIA>.json (p5/p50/p90/p99, % negativos, % exceso>100 ms sobre el suelo de la hora, duplicados) y una linea resumen. Un dia cada vez; nice -n 19; solo lectura.
Definiciones (CONTRATO_RELOJES.md):
  lag = rx - ex (ms). SUELO DE RED de (hora, tipo) = p5 del lag; exceso = lag - suelo.  %rafaga>100 = % de mensajes con exceso > 100 ms.
  TRAMA = mensajes que comparten rx exacto (un frame del WS: _T_RECV se fija por frame). Si el desfase fuera RED ESTABLE, lag seria independiente del tamano/dispersion de la trama;
  si hay SELLO DE LOTE, el exceso crece con la dispersion de sellos exchange DENTRO de la trama (los mas viejos del lote llevan lag mayor). Se informa lag p50/p90 por clase de trama
  (unica / multiple con dispersion<=20 ms / >20 ms) y la correlacion de Spearman exceso vs edad dentro de la trama (ex_max_trama - ex)."""
import sys, os, json
import numpy as np
H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = os.environ.get('CALIB_OUT', H + 'out_v2/'); os.makedirs(OUT, exist_ok=True)
SA2 = os.environ.get('SA2_OUT', '/root/polymarket-research-datalogs/sa_ms2/')
Q = [5, 50, 90, 99]


def pct(x):
    if len(x) == 0: return None
    p = np.percentile(x, Q); return dict(n=int(len(x)), p5=float(p[0]), p50=float(p[1]), p90=float(p[2]), p99=float(p[3]), neg_pct=round(float((x < 0).mean() * 100), 3), min=float(x.min()))


def por_hora(ex, lag, t0):
    h = ((ex + t0) // 3600000 % 24).astype(int); out = {}
    for hh in range(24):
        m = h == hh
        if m.sum() < 100: continue
        l = lag[m]; suelo = np.percentile(l, 5); e = l - suelo
        out[str(hh)] = dict(n=int(m.sum()), p5=float(suelo), p50=float(np.percentile(l, 50)), p90=float(np.percentile(l, 90)), p99=float(np.percentile(l, 99)), neg_pct=round(float((l < 0).mean() * 100), 3), rafaga100_pct=round(float((e > 100).mean() * 100), 3))
    return out


def spearman(a, b):
    ra = np.argsort(np.argsort(a, kind='stable'), kind='stable').astype(float); rb = np.argsort(np.argsort(b, kind='stable'), kind='stable').astype(float)
    ra -= ra.mean(); rb -= rb.mean(); den = np.sqrt((ra ** 2).sum() * (rb ** 2).sum()); return float((ra * rb).sum() / den) if den > 0 else float('nan')


def tramas(ex, rx):
    """Agrupa por rx exacto. Devuelve (edad = ex_max_trama - ex, n_trama, disp_trama) por mensaje."""
    o = np.argsort(rx, kind='stable'); r = rx[o]; e = ex[o]
    ini = np.r_[0, np.where(np.diff(r) != 0)[0] + 1]; n = np.diff(np.r_[ini, len(r)])
    mx = np.maximum.reduceat(e, ini); mn = np.minimum.reduceat(e, ini)
    edad = np.empty(len(r), np.int64); nt = np.empty(len(r), np.int64); dp = np.empty(len(r), np.int64)
    edad[o] = np.repeat(mx, n) - e; nt[o] = np.repeat(n, n); dp[o] = np.repeat(mx - mn, n)
    return edad, nt, dp


def dia(d):
    f = SA2 + f'ms2_{d}.npz'; z = np.load(f, allow_pickle=True); t0 = int(z['t0'])
    qk = z['q_k']; qex = z['q_t_ex'].astype(np.int64); qrx = z['q_t_rx'].astype(np.int64); tex = z['t_t_ex'].astype(np.int64); trx = z['t_t_rx'].astype(np.int64)
    V = np.stack([z[f'q_v{j}'] for j in range(4)], 1)
    R = dict(dia=d, t0=t0, n_q=int(len(qex)), n_t=int(len(tex)), q_sin_rx=int((qrx < 0).sum()), t_sin_rx=int((trx < 0).sum()))
    # duplicados exactos adyacentes (mismo k, ex, bid, ask, tamanos): procesos simultaneos o reenvios
    same = (qk[1:] == qk[:-1]) & (qex[1:] == qex[:-1]) & np.all((V[1:] == V[:-1]) | (np.isnan(V[1:]) & np.isnan(V[:-1])), 1)
    R['q_duplicados_exactos_adyacentes'] = int(same.sum()); del V
    mq = qrx >= 0; mt = trx >= 0
    lq = (qrx[mq] - qex[mq]); lt = (trx[mt] - tex[mt])
    R['q'] = pct(lq); R['t'] = pct(lt)
    R['q_por_hora'] = por_hora(qex[mq], lq, t0); R['t_por_hora'] = por_hora(tex[mt], lt, t0)
    # tramas sobre q+t juntos
    ex = np.concatenate([qex[mq], tex[mt]]); rx = np.concatenate([qrx[mq], trx[mt]]); lag = rx - ex; tipo = np.r_[np.zeros(mq.sum(), np.int8), np.ones(mt.sum(), np.int8)]
    edad, nt, dp = tramas(ex, rx)
    suelo = np.percentile(lag, 5); exceso = lag - suelo
    cl = np.where(nt == 1, 0, np.where(dp <= 20, 1, 2))
    R['suelo_global_p5_ms'] = float(suelo)
    R['tramas'] = {nm: dict(n=int((cl == c).sum()), lag_p50=float(np.percentile(lag[cl == c], 50)), lag_p90=float(np.percentile(lag[cl == c], 90)), lag_p99=float(np.percentile(lag[cl == c], 99)),
                            rafaga100_pct=round(float((exceso[cl == c] > 100).mean() * 100), 3)) for c, nm in ((0, 'unica'), (1, 'multiple_disp_le20ms'), (2, 'multiple_disp_gt20ms')) if (cl == c).any()}
    m2 = nt >= 2; sub = np.where(m2)[0]
    if len(sub) > 2_000_000: sub = np.random.default_rng(1).choice(sub, 2_000_000, replace=False)
    R['spearman_exceso_vs_edad_en_trama'] = spearman(exceso[sub], edad[sub]) if len(sub) > 100 else None
    R['spearman_exceso_vs_tamano_trama'] = spearman(exceso[sub], nt[sub]) if len(sub) > 100 else None
    R['rafaga100_pct_global'] = round(float((exceso > 100).mean() * 100), 3); R['neg_pct_global'] = round(float((lag < 0).mean() * 100), 3)
    json.dump(R, open(OUT + f'calib_relojes_{d}.json', 'w'), indent=1)
    print(d, 'q', R['q'], 't', R['t'], 'tramas', R['tramas'], 'sp_edad', R['spearman_exceso_vs_edad_en_trama'], 'rafaga100%', R['rafaga100_pct_global'], 'dup', R['q_duplicados_exactos_adyacentes'], flush=True)
    return R


if __name__ == '__main__':
    for d in sys.argv[1:]: dia(d)
