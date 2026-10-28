#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""formula_r4_28oct/r4.py - confirmacion prerregistrada del estado 'tras barrido grande reciente' (B pasivo, zona 0,09-0,31).
Modos:  build DIA...  |  calib  |  confirm --days D1,D2 --tag T [--K n]  |  capacity --days D1,D2 --sdays D3 --tag T
Reutiliza SIN modificar identity3.py de R3 (load_registry, load_onchain, match). Solo lectura de datos; sin ordenes, sin .env, sin crons."""
import sys, os, gzip, json, math, time, zlib, datetime, traceback
import numpy as np
from scipy import stats
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct')
import identity3 as I

BASE = '/root/polymarket-research/experimentos/5m_barato/formula_r4_28oct/'
OUT = BASE + 'out/'
os.makedirs(OUT, exist_ok=True)
COINS = ['BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB', 'HYPE', 'AVAX', 'LINK', 'OTHER']
NC = len(COINS)
PLO, PHI = I.PLO, I.PHI
DIRS = ['/mnt/HC_Volume_106538179/keep_onchain_re_as_b/', '/root/polymarket-research-datalogs/keep_onchain_re_as_b/', '/root/polymarket-research-datalogs/']
CALIB_DAYS = ['2026-10-26', '2026-10-27']
LAG_DEF = 2200.0     # ms, mediana bloque-recepcion medida en R3 (2,19-2,20 s)
GAP = 300.0          # ms, hueco maximo entre impresiones (hora de exchange) del mismo (token, lado) para formar un barrido
SW_THR = 200.0       # acc, umbral del barrido on-chain del descubrimiento
LINES = []


def P(*a):
    s = ' '.join(str(x) for x in a); print(s, flush=True); LINES.append(s)


def crc(s): return zlib.crc32(s.encode()) & 0xffffffff
def cx(s): return COINS.index(s) if s in COINS else NC - 1


# ---------------------------------------------------------------- build
def onc_fmt(day):
    for d in DIRS:
        if os.path.exists(d + 'onchain_fills_%s.csv.gz' % day): return d + 'onchain_fills_%s.csv.gz'
    q = '/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_%s.csv.gz'
    if os.path.exists(q % day): return q
    raise FileNotFoundError('onchain ' + day)


def load_prints(day, tok):
    rec = []; ex = []; tkn = []; sd = []; px = []; sz = []; cn = []; seen = set(); dups = 0
    with gzip.open(I.REG % day, 'rt') as f:
        next(f)
        for ln in f:
            if ln[0] != 't': continue
            c = ln.rstrip('\n').split(',')
            t = I.ntok(c[2]); m = tok.get(t)
            if m is None: continue
            p = float(c[3]); s = c[4]
            if s == 'SELL':
                if not (PLO - 0.005 <= p <= PHI + 0.005): continue
            elif s == 'BUY':
                if not (1.0 - PHI - 0.005 <= p <= 1.0 - PLO + 0.005): continue
            else: continue
            k = (t, c[1], c[3], c[5])
            if k in seen: dups += 1
            else: seen.add(k)
            rv = c[6].strip() if len(c) > 6 else ''
            rec.append(float(rv) if rv else float(c[1])); ex.append(float(c[1])); tkn.append(crc(t)); sd.append(0 if s == 'SELL' else 1)
            px.append(p); sz.append(float(c[5])); cn.append(cx(m[1]))
    return {'pr_rec': np.array(rec), 'pr_ex': np.array(ex), 'pr_tk': np.array(tkn, np.int64), 'pr_sd': np.array(sd, np.int8),
            'pr_px': np.array(px), 'pr_sz': np.array(sz), 'pr_coin': np.array(cn, np.int8)}, dups, len(rec)


def build(day, G):
    out = OUT + 'd_%s.npz' % day
    if os.path.exists(out) and 'trem' in np.load(out).files:
        P('[%s] ya construido (idempotente)' % day); return
    t0 = time.time()
    I.ONC = onc_fmt(day)
    tok, prints = I.load_registry(day)
    rows, n_on, nF = I.load_onchain(day, tok)
    lag = I.match(rows, tok, prints)
    del prints
    pr, dups, npr = load_prints(day, tok)
    n = len(rows)
    T = np.fromiter((r[0] for r in rows), float, n); p = np.fromiter((r[5] for r in rows), float, n); sz = np.fromiter((r[6] for r in rows), float, n)
    sw = {}
    swid = np.fromiter((sw.setdefault((r[1], r[3], r[4]), len(sw)) for r in rows), np.int64, n)
    coin = np.empty(n, np.int8); mk = np.empty(n, np.int64); tk = np.empty(n, np.int64); tkr = np.empty(n, np.int64); y = np.full(n, np.nan)
    for i, r in enumerate(rows):
        m = tok[r[4]]; coin[i] = cx(m[1]); mk[i] = crc(m[0]); tk[i] = crc(r[4]); tkr[i] = crc(r[3])
        o = G.get(m[0])
        if o in ('YES', 'NO'): y[i] = 1.0 if o == m[2] else 0.0
    lg = np.array([np.nan if x is None else x for x in lag], float)
    rhat = T * 1000.0 - np.where(np.isnan(lg), LAG_DEF, lg)
    swsz = np.bincount(swid, weights=sz)[swid]
    swT = np.full(len(sw), np.inf); np.minimum.at(swT, swid, T); swT = swT[swid]
    trem = np.array([tok[r[4]][3] for r in rows], float) - rhat / 1000.0
    mm = {}
    for v in tok.values(): mm[v[0]] = v[1]
    ks = [k for k in mm if k.isdigit()]
    mk_num = np.array([int(k) for k in ks], np.int64); mk_coin = np.array([cx(mm[k]) for k in ks], np.int8)
    np.savez_compressed(out, trem=trem, T=T, rhat=rhat, matched=~np.isnan(lg), coin=coin, mk=mk, tk=tk, tkr=tkr, swid=swid, p=p, sz=sz, y=y, swsz=swsz, swT=swT,
                        mk_num=mk_num, mk_coin=mk_coin, **pr)
    P('[%s] BUILD ok: lineas_onchain=%d filas_F_tokens5m=%d pujas_zona=%d (con desenlace %.2f %%) casadas con impresion %.1f %% | impresiones zona=%d duplicadas(token,ex,px,sz)=%.2f %% | %.0f s'
      % (day, n_on, nF, n, 100.0 * np.isfinite(y).mean(), 100.0 * np.isfinite(lg).mean(), npr, 100.0 * dups / max(1, npr), time.time() - t0))


# ---------------------------------------------------------------- estado
def load_day(day):
    z = np.load(OUT + 'd_%s.npz' % day)
    return {k: z[k] for k in z.files}


def build_clusters(D, sidemode, gap=GAP):
    m = np.ones(len(D['pr_sz']), bool) if sidemode == 'ALL' else (D['pr_sd'] == 0)
    ex = D['pr_ex'][m]; rec = D['pr_rec'][m]; tk = D['pr_tk'][m]; sd = D['pr_sd'][m]; sz = D['pr_sz'][m]; cn = D['pr_coin'][m]
    if len(ex) == 0: return np.zeros(0), np.zeros(0), np.zeros(0, np.int8)
    order = np.lexsort((ex, sd, tk))
    ex, rec, tk, sd, sz, cn = ex[order], rec[order], tk[order], sd[order], sz[order], cn[order]
    new = np.ones(len(ex), bool)
    new[1:] = (tk[1:] != tk[:-1]) | (sd[1:] != sd[:-1]) | ((ex[1:] - ex[:-1]) > gap)
    cid = np.cumsum(new) - 1; K = int(cid[-1]) + 1
    size = np.bincount(cid, weights=sz, minlength=K)
    crec = np.full(K, -np.inf); np.maximum.at(crec, cid, rec)
    ccoin = np.zeros(K, np.int8); ccoin[cid] = cn
    return size, crec, ccoin


def events_reg(D, spec, cache):
    kind, sm, th = spec
    if kind == 'cl':
        if ('cl', sm) not in cache: cache[('cl', sm)] = build_clusters(D, sm)
        size, crec, ccoin = cache[('cl', sm)]
        k = size >= th
        return crec[k], ccoin[k], None
    m = np.ones(len(D['pr_sz']), bool) if sm == 'ALL' else (D['pr_sd'] == 0)
    return D['pr_rec'][m], D['pr_coin'][m], D['pr_sz'][m]


def events_chain(D, thr=SW_THR):
    _, first = np.unique(D['swid'], return_index=True)
    k = D['swsz'][first] >= thr
    return D['swT'][first][k] * 1000.0, D['coin'][first][k], None


def prep_state(ev_t, ev_coin, ev_w):
    Pp = {}
    for c in range(NC):
        m = ev_coin == c
        if not m.any(): continue
        t = ev_t[m]
        if ev_w is None: Pp[c] = (np.sort(t), None)
        else:
            o = np.argsort(t, kind='stable'); Pp[c] = (t[o], np.concatenate([[0.0], np.cumsum(ev_w[m][o])]))
    return Pp


def eval_state(Pp, tq, coin_q, theta=None):
    """S(tq) = existe evento (barrido) de la misma moneda con hora en (tq-60 s, tq-5 s]; en modo flujo, suma de tamanos >= theta."""
    S = np.zeros(len(tq), bool)
    for c, (t, cs) in Pp.items():
        mq = np.nonzero(coin_q == c)[0]
        if len(mq) == 0 or len(t) == 0: continue
        a = np.searchsorted(t, tq[mq] - 5000.0, side='right'); b = np.searchsorted(t, tq[mq] - 60000.0, side='right')
        S[mq] = ((a - b) > 0) if cs is None else ((cs[a] - cs[b]) >= theta)
    return S


def kappa(a, b):
    po = float((a == b).mean()); pa = float(a.mean()); pb = float(b.mean()); pe = pa * pb + (1 - pa) * (1 - pb)
    return (po - pe) / (1 - pe) if pe < 1 else float('nan')


def calib():
    Ds = [load_day(d) for d in CALIB_DAYS]
    Sc = np.concatenate([eval_state(prep_state(*events_chain(D)), D['T'] * 1000.0, D['coin']) for D in Ds])
    P('CALIBRACION sobre dias de DESCUBRIMIENTO %s (sin usar desenlaces): fidelidad de un estado OBSERVABLE (impresiones del registro, reloj de recepcion) frente al estado on-chain S_chain (barrido>=%d acc, misma moneda, (t-60 s, t-5 s], reloj de bloque)'
      % (','.join(CALIB_DAYS), SW_THR))
    P('S_chain: cobertura de rellenos %.3f (n=%d)' % (Sc.mean(), len(Sc)))
    VARS = [('cl', sm, th) for sm in ('SELL', 'ALL') for th in (50, 100, 150, 200, 300)] + [('flow', sm, th) for sm in ('SELL', 'ALL') for th in (300, 600, 1200, 2400)]
    caches = [dict() for _ in Ds]; res = []
    for spec in VARS:
        S = np.concatenate([eval_state(prep_state(*events_reg(D, spec, caches[i])), D['rhat'], D['coin'], theta=spec[2] if spec[0] == 'flow' else None) for i, D in enumerate(Ds)])
        kp = kappa(S, Sc); pc = float((S & Sc).sum() / max(1, Sc.sum())); pp = float((S & Sc).sum() / max(1, S.sum()))
        res.append((spec, float(S.mean()), kp, pc, pp))
        P('   %-22s cobertura=%.3f kappa=%+.3f P(S_reg|S_chain)=%.3f P(S_chain|S_reg)=%.3f' % (str(spec), S.mean(), kp, pc, pp))
    okc = [r for r in res if 0.10 <= r[1] <= 0.60]
    best = max(okc, key=lambda r: r[2])
    fz = {'spec': list(best[0]), 'gap_ms': GAP, 'ventana_s': [5, 60], 'lag_defecto_ms': LAG_DEF, 'sw_thr_chain': SW_THR, 'cobertura_calib': best[1], 'kappa_calib': best[2],
          'tabla': [[list(r[0])] + [float(x) for x in r[1:]] for r in res], 'dias_calib': CALIB_DAYS}
    json.dump(fz, open(BASE + 'frozen_r4.json', 'w'), indent=1)
    P('ELEGIDO (max kappa con cobertura en [0,10; 0,60]): %s cobertura=%.3f kappa=%+.3f -> frozen_r4.json' % (best[0], best[1], best[2]))


# ---------------------------------------------------------------- estadistica
def tci(v, conf=0.90):
    v = np.asarray(v, float); v = v[np.isfinite(v)]; n = len(v)
    if n == 0: return (np.nan, np.nan, np.nan)
    if n < 2: return (float(v.mean()), np.nan, np.nan)
    m = float(v.mean()); se = float(v.std(ddof=1)) / math.sqrt(n); t = float(stats.t.ppf(0.5 + conf / 2, n - 1))
    return (m, m - t * se, m + t * se)


def dday(S, num, den, d, nd, mask=None):
    S1 = S if mask is None else (S & mask); S0 = (~S) if mask is None else ((~S) & mask)
    n1 = np.bincount(d, weights=num * S1, minlength=nd); d1 = np.bincount(d, weights=den * S1, minlength=nd)
    n0 = np.bincount(d, weights=num * S0, minlength=nd); d0 = np.bincount(d, weights=den * S0, minlength=nd)
    with np.errstate(all='ignore'): e1 = n1 / d1; e0 = n0 / d0
    return e1, e0, e1 - e0, d1, d0


def conc(mask, key, den):
    if mask.sum() == 0: return (0, float('nan'), float('nan'))
    u, inv = np.unique(key[mask], return_inverse=True)
    w = np.sort(np.bincount(inv, weights=den[mask]))[::-1]; tot = w.sum()
    return (len(u), float(w[:1].sum() / tot), float(w[:5].sum() / tot))


def confirm(days, tag, K):
    fz = json.load(open(BASE + 'frozen_r4.json')); spec = tuple(fz['spec']); th = spec[2]; flow = spec[0] == 'flow'
    nd = len(days); rng = np.random.default_rng(2812)
    names = ('d', 'coin', 'mk', 'tkr', 'p', 'sz', 'y', 'S', 'Sc', 'S14', 'S29', 'Sa', 'Sb', 'swsz', 'q0', 'trem')
    A = {k: [] for k in names}; PREP = []; T0 = []
    for i, day in enumerate(days):
        D = load_day(day); cache = {}
        prep = prep_state(*events_reg(D, spec, cache)); PREP.append(prep)
        T0.append(datetime.datetime.fromisoformat(day + 'T00:00:00+00:00').timestamp() * 1000.0)
        th_ = th if flow else None
        spa = (spec[0], spec[1], th * 0.5); spb = (spec[0], spec[1], th * 2.0)
        V = {'S': eval_state(prep, D['rhat'], D['coin'], th_),
             'S14': eval_state(prep, D['T'] * 1000.0 - 1400.0, D['coin'], th_), 'S29': eval_state(prep, D['T'] * 1000.0 - 2900.0, D['coin'], th_),
             'Sa': eval_state(prep_state(*events_reg(D, spa, cache)), D['rhat'], D['coin'], spa[2] if flow else None),
             'Sb': eval_state(prep_state(*events_reg(D, spb, cache)), D['rhat'], D['coin'], spb[2] if flow else None),
             'Sc': eval_state(prep_state(*events_chain(D)), D['T'] * 1000.0, D['coin'])}
        ok = np.isfinite(D['y']); n = len(ok)
        base = {'d': np.full(n, i), 'coin': D['coin'], 'mk': D['mk'], 'tkr': D['tkr'], 'p': D['p'], 'sz': D['sz'], 'y': D['y'], 'swsz': D['swsz'], 'q0': D['rhat'], 'trem': D['trem']}
        base.update(V)
        for k in names: A[k].append(base[k][ok])
        P('[%s] fills con desenlace=%d (de %d) cobertura S=%.3f' % (day, int(ok.sum()), n, float(V['S'][ok].mean())))
    X = {k: np.concatenate(A[k]) for k in names}
    d = X['d'].astype(np.int64); coin = X['coin'].astype(np.int64); p = X['p']; sz = X['sz']; y = X['y']; S = X['S']
    num = sz * (y - p); den = sz * p; n = len(d)
    P('')
    P('== CONFIRMACION %s: dias=%s | estado congelado %s (hueco %d ms, ventana (t-60 s, t-5 s], misma moneda, reloj de RECEPCION; fill en r_hat = bloque - lag casado o 2,2 s) | n fills=%d' % (tag, ','.join(days), spec, GAP, n))
    e1, e0, dv, d1, d0 = dday(S, num, den, d, nd)
    cov_n = np.bincount(d, weights=S.astype(float), minlength=nd) / np.bincount(d, minlength=nd)
    P('día        fills   n_S     cov_n  cov_EUR  EV/E(S)  EV/E(noS)  dEV/E   dEV/E(acc-igual) mercados_S  EUR_S/dia')
    dq = dday(S, y - p, p, d, nd)[2]
    for i, day in enumerate(days):
        mi = d == i
        P('%s %7d %7d  %.3f  %.3f   %+.3f   %+.3f    %+.3f   %+.3f           %5d      %9.0f' % (day, mi.sum(), (S & mi).sum(), cov_n[i], d1[i] / (d1[i] + d0[i]), e1[i], e0[i], dv[i], dq[i], len(np.unique(X['mk'][S & mi])), d1[i]))
    mu, lo, hi = tci(dv); pos = int(np.sum(dv > 0))
    b = rng.integers(0, nd, (4000, nd)); bs = np.nanmean(dv[b], axis=1)
    P('PRIMARIO dEV/E medio por dia = %+.4f IC90 t(dias)[%+.4f,%+.4f] | bootstrap dias [%+.4f,%+.4f] | dias positivos %d/%d | cobertura media (n) %.3f (€) %.3f | acc-igual %+.4f'
      % (mu, lo, hi, np.percentile(bs, 5), np.percentile(bs, 95), pos, nd, cov_n.mean(), float(np.mean(d1 / (d1 + d0))), float(np.nanmean(dq))))
    o = np.argsort(dv)[::-1]; rest = np.delete(dv, o[:2]); m2 = tci(rest)
    P('   sin los 2 mejores dias (%s): dEV/E %+.4f IC90[%+.4f,%+.4f] (n=%d dias) | dejando fuera cada dia: min %+.4f max %+.4f'
      % (','.join(days[j] for j in o[:2]), m2[0], m2[1], m2[2], len(rest), min(np.nanmean(np.delete(dv, j)) for j in range(nd)), max(np.nanmean(np.delete(dv, j)) for j in range(nd))))
    P('   EUR en S por dia (volumen de la zona en estado S, todos los makers): %.0f ; acc: %.0f' % (float(d1.mean()), float(np.bincount(d, weights=sz * S, minlength=nd).mean())))
    # placebo A: etiquetas permutadas dentro de estratos dia x moneda x centimo de precio de relleno
    cents = np.rint(p * 100).astype(np.int64); sid0 = (d * 16 + coin) * 100 + cents
    us, sid = np.unique(sid0, return_inverse=True); cnt = np.bincount(sid); starts = np.cumsum(cnt) - cnt; kk = np.bincount(sid, weights=S.astype(float)).astype(np.int64)
    pa = []
    for _ in range(K):
        order = np.argsort(sid + rng.random(n)); rank = np.arange(n) - starts[sid[order]]
        ps = np.zeros(n, bool); ps[order] = rank < kk[sid[order]]
        pa.append(float(np.nanmean(dday(ps, num, den, d, nd)[2])))
    pa = np.array(pa); p_A = (1 + float((pa >= mu).sum())) / (K + 1)
    # placebo B: desplazamiento circular del estado por moneda y dia, resultados residualizados por (moneda, centimo)
    cell = coin * 100 + cents; ucell, ci = np.unique(cell, return_inverse=True)
    mu_c = np.bincount(ci, weights=num) / np.maximum(np.bincount(ci, weights=sz), 1e-12)
    numr = sz * (y - p - mu_c[ci])
    idx = [np.nonzero(d == i)[0] for i in range(nd)]

    def stat_res(Slist):
        v = []
        for i in range(nd):
            ix = idx[i]; Sp = Slist[i]
            a1 = den[ix][Sp].sum(); a0 = den[ix][~Sp].sum()
            v.append(numr[ix][Sp].sum() / a1 - numr[ix][~Sp].sum() / a0 if a1 > 0 and a0 > 0 else np.nan)
        return float(np.nanmean(v)), v
    obs_res, v_res = stat_res([S[idx[i]] for i in range(nd)])
    pb = []
    for _ in range(K):
        Sl = []
        for i in range(nd):
            ix = idx[i]; sh = rng.uniform(600.0, 86400.0 - 600.0, NC) * 1000.0
            tq = ((X['q0'][ix] - T0[i] + sh[coin[ix]]) % 86.4e6) + T0[i]
            Sl.append(eval_state(PREP[i], tq, coin[ix], th if flow else None))
        pb.append(stat_res(Sl)[0])
    pb = np.array(pb); p_B = (1 + float((pb >= obs_res).sum())) / (K + 1)
    P('PLACEBO A (etiquetas permutadas en estratos dia x moneda x centimo de relleno, K=%d): media placebo %+.4f sd %.4f -> p=%.4f | efecto ajustado por composicion (obs - media placebo) = %+.4f' % (K, pa.mean(), pa.std(), p_A, mu - pa.mean()))
    P('PLACEBO B (estado desplazado en el tiempo por moneda-dia 10 min..23 h, resultados residualizados por moneda x centimo; observado %+.4f, K=%d): media placebo %+.4f sd %.4f -> p=%.4f' % (obs_res, K, pb.mean(), pb.std(), p_B))
    tb = np.digitize(X['trem'], [30.0, 60.0, 120.0, 180.0, 240.0])
    us2, sid2 = np.unique(sid0 * 8 + tb, return_inverse=True); cnt2 = np.bincount(sid2); starts2 = np.cumsum(cnt2) - cnt2; kk2 = np.bincount(sid2, weights=S.astype(float)).astype(np.int64)
    pa2 = []
    for _ in range(K):
        order = np.argsort(sid2 + rng.random(n)); rank = np.arange(n) - starts2[sid2[order]]
        ps = np.zeros(n, bool); ps[order] = rank < kk2[sid2[order]]
        pa2.append(float(np.nanmean(dday(ps, num, den, d, nd)[2])))
    pa2 = np.array(pa2); p_A2 = (1 + float((pa2 >= mu).sum())) / (K + 1)
    P('PLACEBO A2 (como A + tramo de T_rem hasta el cierre del mercado {<30,30-60,60-120,120-180,180-240,>=240 s}, K=%d): media placebo %+.4f sd %.4f -> p=%.4f | efecto ajustado (obs - media) = %+.4f' % (K, pa2.mean(), pa2.std(), p_A2, mu - pa2.mean()))
    tlab = ['<30 s', '30-60 s', '60-120 s', '120-180 s', '180-240 s', '>=240 s']
    P('== T_rem (segundos hasta el cierre del mercado en el relleno): cobertura de S y contraste DENTRO de cada tramo (estado primario)')
    adjT = 0.0; wsum = 0.0
    for b_ in range(6):
        m = tb == b_
        if (m & S).sum() < 20 or (m & ~S).sum() < 20:
            P('   T_rem %-9s fills=%d n_S=%d insuficiente' % (tlab[b_], m.sum(), (m & S).sum())); continue
        v = dday(S, num, den, d, nd, m)[2]; m_, l_, h_ = tci(v); w_ = den[m].sum(); adjT += w_ * m_; wsum += w_
        P('   T_rem %-9s fills=%d cov_n=%.3f dEV/E %+.3f IC90[%+.3f,%+.3f] dias+ %d/%d' % (tlab[b_], m.sum(), S[m].mean(), m_, l_, h_, int(np.sum(v > 0)), int(np.isfinite(v).sum())))
    P('   efecto post-estratificado por T_rem (media ponderada por EUR de los contrastes por tramo): %+.4f' % (adjT / max(wsum, 1e-12)))
    um, mi_ = np.unique(X['mk'], return_inverse=True); M_ = len(um)
    n1m = np.bincount(mi_, weights=num * S, minlength=M_); d1m = np.bincount(mi_, weights=den * S, minlength=M_)
    n0m = np.bincount(mi_, weights=num * (~S), minlength=M_); d0m = np.bincount(mi_, weights=den * (~S), minlength=M_)
    pool = n1m.sum() / d1m.sum() - n0m.sum() / d0m.sum(); bsm = []
    for _ in range(2000):
        jx = rng.integers(0, M_, M_); a1 = d1m[jx].sum(); a0 = d0m[jx].sum()
        bsm.append(n1m[jx].sum() / a1 - n0m[jx].sum() / a0 if a1 > 0 and a0 > 0 else np.nan)
    bsm = np.array(bsm)
    P('BOOTSTRAP por MERCADO (agrupa dias; %d mercados distintos, %d con fills en S): dEV/E agrupado %+.4f IC90[%+.4f,%+.4f]' % (M_, int((d1m > 0).sum()), pool, np.nanpercentile(bsm, 5), np.nanpercentile(bsm, 95)))
    pmax = max(p_A, p_A2, p_B)
    # sensibilidades (no deciden)
    P('== SECUNDARIOS (no deciden)')
    for lab, Sx, msk, w in (('S_chain (tamano on-chain, reloj bloque, oraculo)', X['Sc'], None, 0), ('lag 1,4 s uniforme', X['S14'], None, 0), ('lag 2,9 s uniforme', X['S29'], None, 0),
                            ('umbral/2', X['Sa'], None, 0), ('umbral*2', X['Sb'], None, 0), ('solo fills de barridos propios <50 acc', S, X['swsz'] < 50, 0), ('fills con barrido propio >=200 acc excluidos', S, X['swsz'] < 200, 0),
                            ('pesos iguales por fill (acc-igual)', S, None, 1)):
        v = dday(Sx, (y - p) if w else num, p if w else den, d, nd, msk)[2]
        m_, l_, h_ = tci(v)
        P('   %-52s dEV/E %+.4f IC90[%+.4f,%+.4f] dias+ %d/%d cobertura %.3f' % (lab, m_, l_, h_, int(np.sum(v > 0)), nd, float(Sx.mean())))
    P('== DESAGREGADO por moneda (todos los precios; estado primario)')
    for c in range(NC):
        m = coin == c
        if m.sum() == 0: continue
        if (m & S).sum() < 20 or (m & ~S).sum() < 20:
            P('   %-5s fills=%d n_S=%d: insuficiente para contraste' % (COINS[c], m.sum(), (m & S).sum())); continue
        v = dday(S, num, den, d, nd, m)[2]; m_, l_, h_ = tci(v)
        P('   %-5s dEV/E %+.3f IC90[%+.3f,%+.3f] dias+ %d/%d fills=%d n_S=%d cov_n=%.3f EUR_zona/dia=%.0f' % (COINS[c], m_, l_, h_, int(np.sum(v > 0)), int(np.isfinite(v).sum()), m.sum(), (m & S).sum(), (m & S).sum() / m.sum(), den[m].sum() / nd))
    # moneda x bucket
    P('== DESAGREGADO moneda x bucket de precio de relleno (estado primario; dEV/E medio por dia, IC90 t; n_S fills; mercados distintos en S)')
    bk = np.digitize(p, [0.15, 0.20, 0.25]); blab = ['[0,09-0,15)', '[0,15-0,20)', '[0,20-0,25)', '[0,25-0,31]']
    for c in range(NC):
        for bq in range(4):
            m = (coin == c) & (bk == bq)
            if (m & S).sum() < 30 or (m & ~S).sum() < 30: continue
            v = dday(S, num, den, d, nd, m)[2]; m_, l_, h_ = tci(v)
            P('   %-5s %s dEV/E %+.3f IC90[%+.3f,%+.3f] dias+ %d/%d n_S=%6d n_noS=%6d mercados_S=%4d' % (COINS[c], blab[bq], m_, l_, h_, int(np.sum(v > 0)), int(np.isfinite(v).sum()), (m & S).sum(), (m & ~S).sum(), len(np.unique(X['mk'][m & S]))))
    P('== CONCENTRACION (fills en S): mercados distintos / top-1 / top-5 del volumen por mercado | barrenderos distintos / top-1 / top-5')
    mc = conc(S, X['mk'], den); tc = conc(S, X['tkr'], den)
    P('   S: mercados %d top1 %.1f %% top5 %.1f %% | barrenderos %d top1 %.1f %% top5 %.1f %%' % (mc[0], 100 * mc[1], 100 * mc[2], tc[0], 100 * tc[1], 100 * tc[2]))
    mc = conc(~S, X['mk'], den); tc = conc(~S, X['tkr'], den)
    P('   noS: mercados %d top1 %.1f %% top5 %.1f %% | barrenderos %d top1 %.1f %% top5 %.1f %%' % (mc[0], 100 * mc[1], 100 * mc[2], tc[0], 100 * tc[1], 100 * tc[2]))
    P('   aporte de los 2 mejores dias a la suma de dEV/E positivos: %.1f %%' % (100.0 * np.sort(dv)[::-1][:2].clip(0).sum() / max(1e-12, dv.clip(0).sum())))
    # veredicto mecanico
    c_mean = mu >= 0.10; c_ci = (lo > 0) if np.isfinite(lo) else False; c_cov = 0.10 <= cov_n.mean() <= 0.60; c_pl = pmax < 0.05
    need = int(math.ceil(0.8 * nd)); c_pos = pos >= need
    P('== VEREDICTO MECANICO (criterios del prereg; nd=%d dias de confirmacion)' % nd)
    P('   dEV/E>=+0,10: %s (%+.4f) | IC90 dias>0: %s (lo %+.4f) | dias positivos >=80 %% (%d de %d): %s (%d) | cobertura 10-60 %%: %s (%.3f) | placebo p<0,05 (max(A,A2,B)=%.4f): %s'
      % (c_mean, mu, c_ci, lo, need, nd, c_pos, pos, c_cov, cov_n.mean(), pmax, c_pl))
    if nd >= 10:
        v = 'ACCEPTED_FOR_NEXT_STAGE' if (c_mean and c_ci and c_pos and c_cov and c_pl) else ('REJECTED' if (mu < 0.05 or not c_ci) else 'INSUFFICIENT_EVIDENCE')
    else:
        v = 'PARCIAL (%d<10 dias): ' % nd + ('FALLO_PROVISIONAL (dEV/E<+0,05)' if mu < 0.05 else ('CONSISTENTE_CON_EXITO_pendiente_de_dias' if (c_mean and c_ci and c_pos and c_cov and c_pl) else 'NO_CONCLUYENTE'))
    P('   VEREDICTO: %s' % v)


# ---------------------------------------------------------------- capacidad
def capacity(days, sdays, tag):
    fz = json.load(open(BASE + 'frozen_r4.json')); spec = tuple(fz['spec']); th = spec[2]; flow = spec[0] == 'flow'
    F3 = '/root/polymarket-research/experimentos/5m_barato/formula_r3_28oct/out/f_%s.npz'
    tot = {k: 0.0 for k in ('nff', 'e5', 'e10', 'e20', 'a5', 'a10', 'a20', 'nS', 'e5S', 'e10S', 'e20S', 'nffS', 'dS', 'dall', 'e5_sd')}
    P('== CAPACIDAD B-sim (R3 features: primer relleno por mercado-token, puja bb+0,01, cola 0, LR 130 ms) x estado S congelado en el TICK de decision (sin desenlaces)')
    for day in days:
        zf = np.load(F3 % day); nm = [str(x) for x in zf['names']]; ix = {n_: i for i, n_ in enumerate(nm)}
        Xf = zf['X']; d0 = float(zf['d0'])
        ts = Xf[:, ix['ts']].astype(np.float64)
        if np.nanmax(ts) < 1e8: ts = ts + d0
        mkt = np.rint(Xf[:, ix['mkt']].astype(np.float64)).astype(np.int64); yes = (Xf[:, ix['yes']] > 0.5).astype(np.int64)
        fsz = np.nan_to_num(Xf[:, ix['fsz']].astype(np.float64)); fpx = np.nan_to_num(Xf[:, ix['fpx']].astype(np.float64))
        ixf = np.nonzero(fsz > 0)[0]; ixf = ixf[np.argsort(ts[ixf], kind='stable')]
        _, first = np.unique(mkt[ixf] * 2 + yes[ixf], return_index=True); ff = ixf[first]
        P('   [diag %s] ts-d0 min %.1f max %.1f ; d0=%.0f ; mkt unicos=%d ; col coin unicos=%s' % (day, ts.min() - d0, ts.max() - d0, d0, len(np.unique(mkt)), np.unique(Xf[:, ix['coin']])[:12]))
        m5 = np.minimum(fsz[ff], 5.0); m10 = np.minimum(fsz[ff], 10.0); m20 = np.minimum(fsz[ff], 20.0); px = fpx[ff]
        line = '[%s] filas=%d con_relleno=%d primeros_rellenos=%d precio_medio=%.3f acc_llenas(5/10/20)=%.2f/%.2f/%.2f EUR(5/10/20 acc)=%.0f/%.0f/%.0f' % (
            day, len(ts), len(ixf), len(ff), px.mean(), m5.mean(), m10.mean(), m20.mean(), (m5 * px).sum(), (m10 * px).sum(), (m20 * px).sum())
        tot['nff'] += len(ff); tot['e5'] += (m5 * px).sum(); tot['e10'] += (m10 * px).sum(); tot['e20'] += (m20 * px).sum(); tot['a5'] += m5.sum(); tot['a10'] += m10.sum(); tot['a20'] += m20.sum(); tot['dall'] += 1
        if day in sdays and os.path.exists(OUT + 'd_%s.npz' % day):
            D = load_day(day); o = np.argsort(D['mk_num']); kn = D['mk_num'][o]; kc = D['mk_coin'][o]
            pos_ = np.searchsorted(kn, mkt[ff]); pos_ = np.clip(pos_, 0, len(kn) - 1); okm = kn[pos_] == mkt[ff]; cq = np.where(okm, kc[pos_], -1)
            prep = prep_state(*events_reg(D, spec, {})); S = eval_state(prep, ts[ff] * 1000.0, cq.astype(np.int64), th if flow else None) & okm
            line += ' | mapeo mercado->moneda %.1f %% | cobertura S en el tick: n %.3f EUR %.3f' % (100 * okm.mean(), S[okm].mean(), (m5 * px)[S].sum() / (m5 * px).sum())
            tot['nS'] += S.sum(); tot['nffS'] += len(ff); tot['e5S'] += (m5 * px)[S].sum(); tot['e10S'] += (m10 * px)[S].sum(); tot['e20S'] += (m20 * px)[S].sum(); tot['dS'] += 1; tot['e5_sd'] += (m5 * px).sum()
        P(line)
    nd = len(days)
    P('TOTAL %d dias: primeros rellenos/dia %.0f; EUR desplegados/dia a 5/10/20 acc: %.0f/%.0f/%.0f ; factor de profundidad medido vs lineal (10 acc, 20 acc): %.2f (de 2) / %.2f (de 4)'
      % (nd, tot['nff'] / nd, tot['e5'] / nd, tot['e10'] / nd, tot['e20'] / nd, tot['e10'] / tot['e5'], tot['e20'] / tot['e5']))
    if tot['dS'] > 0:
        covE = tot['e5S'] / tot['e5_sd']; covN = tot['nS'] / tot['nffS']
        P('cobertura de S sobre los primeros rellenos B-sim (%d dia(s) con estado): n %.3f, EUR %.3f' % (tot['dS'], covN, covE))
    else:
        covE = 0.45; P('sin dias con estado construido: cobertura supuesta 0,45 (S_chain on-chain 26-27 Oct)')
    P('ESCENARIOS: EV(S) = EV_todo + (1-cov)*dEV ; EUR/anio = 365 x (EUR desplegados/dia en S) x EV(S) ; EV_todo = +0,5 %% (R2 U_p1 EVw) | -4,2 %% (proxy R3: -0,0085/acc a ~0,2) | -7,2 %% (B real on-chain, n=202); cov=%.3f' % covE)
    for X_, e in ((5, tot['e5']), (10, tot['e10']), (20, tot['e20'])):
        eS = e / nd * covE
        for dEV in (0.10, 0.15):
            cells = []
            for ev_all in (0.005, -0.042, -0.072):
                evS = ev_all + (1 - covE) * dEV
                cells.append('EV_todo %+.1f%% -> EV(S) %+.1f%% -> %+7.0f EUR/anio' % (100 * ev_all, 100 * evS, 365 * eS * evS))
            P('   %2d acc: EUR/dia desplegados en S %.0f | dEV=%+.2f | %s' % (X_, eS, dEV, ' | '.join(cells)))
    P('   (UNA unidad por mercado-token, cola 0, sin reposiciones; EUR del simulador B-sim, no validados; referencia 200.000 EUR/anio)')
    return tot


if __name__ == '__main__':
    t0 = time.time(); mode = sys.argv[1] if len(sys.argv) > 1 else ''
    tag = mode
    try:
        if mode == 'build':
            G = json.load(open(I.CACHE))
            for day in sys.argv[2:]:
                try: build(day, G)
                except Exception: P('ERROR build', day, traceback.format_exc()[-1500:])
        elif mode == 'calib': calib()
        elif mode == 'confirm':
            a = sys.argv; days = a[a.index('--days') + 1].split(','); tag = 'confirm_' + a[a.index('--tag') + 1]
            confirm(days, a[a.index('--tag') + 1], int(a[a.index('--K') + 1]) if '--K' in a else 500)
        elif mode == 'capacity':
            a = sys.argv; days = a[a.index('--days') + 1].split(','); sd = a[a.index('--sdays') + 1].split(',') if '--sdays' in a else []; tag = 'capacity_' + a[a.index('--tag') + 1]
            capacity(days, sd, a[a.index('--tag') + 1])
        else: P('modo desconocido')
    except Exception:
        P('ERROR', mode, traceback.format_exc()[-2500:])
    P('fin %s %.0f s' % (mode, time.time() - t0))
    open(BASE + 'salida_%s.txt' % tag, 'w').write('\n'.join(LINES) + '\n')
