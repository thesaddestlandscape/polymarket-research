#!/usr/bin/env python3
"""r10c_build: version CAUSAL de r10_build (29-Oct). Todo rasgo en t usa solo datos <= t: L1 del complementario en t; sin prints del complementario = 0 explicito (no NaN por futuro); clusters grandes solo cuando YA estan cerrados (fin+300 ms <= t). Columnas extra del complementario al final (COLS_X). Original r10_build (copia corregida de formula_r8_28oct/r8h_build.py; unica diferencia: clave bid15 y ruta de salida). r8h_build: tabla de hazard (token x 2 s) con rasgos, etiquetas y relleno de pujas hipoteticas. Uso: r8h_build.py BTC|ETH. Manda PREREG_FORMULA_R8.md."""
import sys; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
from r8lib import *
import time
coin = sys.argv[1]; G = json.load(open(r4.I.CACHE)); days = days_incl(); t0 = time.time()
R10 = E4 + 'formula_r10_29oct/causal/'; assert coin == 'BTC'
MS = (1, 2, 3); DECL = 73.0; BIG = 800.0
COLS = ['acc1', 'acc5', 'acc30', 'acc60', 'np1', 'np5', 'np30', 'np60', 'tsl200', 'tsl800', 'n800_60', 'coin_n60', 'comp_acc5', 'bb', 'spr', 'bs', 'dbb1', 'dbb5', 'cbb', 'dcbb1', 'dcbb5', 'bid15', 'm15', 'dbid15', 'trem', 'hour', 'jadv', 'jopp', 'jn30', 'jn300']
COLS_X = ['cba', 'cspr', 'cbs', 'dcba1', 'dcba5', 'comp_tsl', 'comp_np5', 'sumb', 'suma', 'c_exist']
COLS_ALL = COLS + COLS_X
OUT = {k: [] for k in ('di', 'u', 't', 'y', 'Y5', 'Y10', 'Y4', 'dtn', 'a215')}; FE = []; FL = []; TG = []; TF = []; XB = []
def wsum(st, cs, t, w):
    i = np.searchsorted(st, t, 'right'); j = np.searchsorted(st, t - w, 'right'); return cs[i] - cs[j], (i - j).astype(float)
for di, d in enumerate(days):
    D = Day(d, coin); S = {}
    kz = None
    if coin == 'BTC':
        f15 = BASE.replace('formula_r8_28oct', 'formula_r7_28oct') + 'k15/k_%s.npz' % d
        if os.path.exists(f15):
            kz = np.load(f15); kmap = {(int(kz['kside'][i]), int(kz['kstart'][i])): i for i in range(len(kz['kstart']))}
            klo = np.searchsorted(kz['qk'], np.arange(len(kz['kstart'])), 'left'); khi = np.searchsorted(kz['qk'], np.arange(len(kz['kstart'])), 'right')
    allB = []
    for u in range(D.n):
        st, se, sp, ss = D.stream(u)
        if len(st) == 0: S[u] = None; continue
        cid, starts, ends = clusters(se); K = len(starts); tot = np.bincount(cid, weights=ss, minlength=K); cst = st[starts]; cen = st[ends - 1]
        ok = (sp[starts] >= 0.09) & (sp[starts] <= 0.35)
        S[u] = (st, se, sp, ss, np.r_[0.0, np.cumsum(ss)], cst, cen, tot, ok)
        allB.append((cen + 300.0)[(tot >= BIG) & ok])  # CAUSAL: instante en que el cluster grande ya esta cerrado
    allB = np.sort(np.concatenate(allB)) if allB else np.zeros(0)
    jall = np.sort(np.r_[D.jd, D.ju])
    EMPTY = (np.zeros(0), np.zeros(0), np.zeros(0), np.zeros(0), np.zeros(1), np.zeros(0), np.zeros(0), np.zeros(0), np.zeros(0, bool))
    for u in range(D.n):
        win = G.get(str(D.mks[u]))
        if win not in ('YES', 'NO') or D.qhi[u] <= D.qlo[u]: continue
        y = 1.0 if win == ('YES' if D.side[u] == 0 else 'NO') else 0.0
        c0 = float(D.cie[u]) * 1000.0; T = np.arange(c0 - 285000.0, c0 - 15000.0, 2000.0)
        bb, ba, bs = D.l1(u, T); keep = np.isfinite(bb) & np.isfinite(ba) & (ba > bb) & (bb >= 0.10) & (bb <= 0.35)
        if not keep.any(): continue
        T = T[keep]; bb = bb[keep]; ba = ba[keep]; bs = bs[keep]; n = len(T)
        s = S[u]; empty = s is None
        if empty:
            st = se = sp = ss = np.zeros(0); cs = np.zeros(1); cst = cen = tot = np.zeros(0); ok = np.zeros(0, bool)
        else: st, se, sp, ss, cs, cst, cen, tot, ok = s
        f = {}
        for w, nm in ((1000.0, '1'), (5000.0, '5'), (30000.0, '30'), (60000.0, '60')): f['acc' + nm], f['np' + nm] = wsum(st, cs, T, w)
        for thr, nm in ((200.0, 'tsl200'), (BIG, 'tsl800')):
            m = (tot >= thr) & ok; ce = cen[m]; j = np.searchsorted(ce + 300.0, T, 'right') - 1  # CAUSAL: cluster cerrado (fin+300 ms <= t)
            f[nm] = np.where(j >= 0, np.minimum(T - ce[np.clip(j, 0, None)], 300000.0), 300000.0) if len(ce) else np.full(n, 300000.0)
        B8 = cst[(tot >= BIG) & ok]; E8 = (cen + 300.0)[(tot >= BIG) & ok]; f['n800_60'] = (np.searchsorted(E8, T, 'right') - np.searchsorted(E8, T - 60000.0, 'right')).astype(float)  # CAUSAL: B8 (inicio) solo para etiquetas
        f['coin_n60'] = (np.searchsorted(allB, T, 'right') - np.searchsorted(allB, T - 60000.0, 'right')).astype(float)
        c = int(D.comp[u]); X = {}
        if c >= 0:
            sc = S.get(c); sc = EMPTY if sc is None else sc  # CAUSAL: sin prints del complementario = 0 explicito (R10 ponia NaN si no habia NINGUN print en toda la ventana)
            f['comp_acc5'], f['comp_np5'] = wsum(sc[0], sc[4], T, 5000.0)
            sT = sc[0]; jj = np.searchsorted(sT, T, 'right') - 1; X['comp_tsl'] = np.where(jj >= 0, np.minimum(T - sT[np.clip(jj, 0, None)], 300000.0), 300000.0) if len(sT) else np.full(n, 300000.0)
            cb, ca, cs_ = D.l1(c, T); cb1, ca1, _ = D.l1(c, T - 1000.0); cb5, ca5, _ = D.l1(c, T - 5000.0)
            X['cba'] = ca; X['cspr'] = ca - cb; X['cbs'] = cs_; X['dcba1'] = ca - ca1; X['dcba5'] = ca - ca5; X['sumb'] = bb + cb; X['suma'] = ba + ca; X['c_exist'] = np.ones(n)
        else:
            f['comp_acc5'] = np.full(n, np.nan); f['comp_np5'] = np.full(n, np.nan); cb = cb1 = cb5 = np.full(n, np.nan)
            for k in COLS_X: X[k] = np.full(n, np.nan)
            X['c_exist'] = np.zeros(n)
        b1 = D.l1(u, T - 1000.0)[0]; b5 = D.l1(u, T - 5000.0)[0]
        f['bb'] = bb; f['spr'] = ba - bb; f['bs'] = bs; f['dbb1'] = bb - b1; f['dbb5'] = bb - b5; f['cbb'] = cb; f['dcbb1'] = cb - cb1; f['dcbb5'] = cb - cb5
        bid15 = np.full(n, np.nan); dbid = np.full(n, np.nan)
        if kz is not None:
            i = kmap.get((int(D.side[u]), int((float(D.cie[u]) - 300.0) // 900 * 900 + 900)))  # R10: kstart de k15 = CIERRE del 15m; el 15m que contiene al 5m cierra en floor(s5/900)*900+900
            if i is not None and khi[i] > klo[i]:
                qq = kz['qt'][klo[i]:khi[i]]; bq = kz['qbb'][klo[i]:khi[i]]
                for tt, arr in ((T, 'a'), (T - 5000.0, 'b')):
                    j = np.searchsorted(qq, tt, 'right') - 1; v = np.where(j >= 0, bq[np.clip(j, 0, None)], np.nan)
                    if arr == 'a': bid15 = v
                    else: dbid = bid15 - v
        f['bid15'] = bid15; f['m15'] = bid15 - bb; f['dbid15'] = dbid; f['trem'] = (c0 - T) / 1000.0; f['hour'] = ((T / 1000.0) % 86400) // 3600
        adv = D.jd if D.side[u] == 0 else D.ju; opp = D.ju if D.side[u] == 0 else D.jd
        for arr, nm in ((adv, 'jadv'), (opp, 'jopp')):
            j = np.searchsorted(arr, T, 'right') - 1; f[nm] = np.where(j >= 0, np.minimum(T - arr[np.clip(j, 0, None)], 60000.0), 60000.0) if len(arr) else np.full(n, 60000.0)
        f['jn30'] = (np.searchsorted(jall, T, 'right') - np.searchsorted(jall, T - 30000.0, 'right')).astype(float); f['jn300'] = (np.searchsorted(jall, T, 'right') - np.searchsorted(jall, T - 300000.0, 'right')).astype(float)
        # etiquetas: primer print de un cluster >=800 en (t+0,1 s, t+H]
        idx = np.searchsorted(B8, T + 100.0, 'right'); nxt = np.where(idx < len(B8), B8[np.clip(idx, 0, max(len(B8) - 1, 0))] if len(B8) else np.inf, np.inf) if len(B8) else np.full(n, np.inf)
        B4 = cst[(tot >= 400.0) & ok]; i4 = np.searchsorted(B4, T + 100.0, 'right'); n4 = np.where(i4 < len(B4), B4[np.clip(i4, 0, max(len(B4) - 1, 0))] if len(B4) else np.inf, np.inf) if len(B4) else np.full(n, np.inf)
        dtn = nxt - T
        OUT['di'].append(np.full(n, di)); OUT['u'].append(np.full(n, u)); OUT['t'].append(T); OUT['y'].append(np.full(n, y))
        OUT['Y5'].append(dtn <= 5000.0); OUT['Y10'].append(dtn <= 10000.0); OUT['Y4'].append((n4 - T) <= 10000.0); OUT['dtn'].append(np.minimum(dtn, 600000.0)); OUT['a215'].append(D.l1(u, T + 215.0)[1])
        f.update(X); FE.append(np.vstack([f[k] for k in COLS_ALL]).T.astype(np.float32))
        fl = np.zeros((n, 3), bool); tg = np.full((n, 3), np.nan); tf = np.full((n, 3), np.nan); xb = np.full((n, 3, 3), np.nan)
        if not empty:
            for r in range(n):
                for mi, m in enumerate(MS):
                    tgt = round(float(bb[r]) - m * 0.01, 2)
                    if not (0.09 - 1e-9 <= tgt <= 0.29 + 1e-9): continue
                    tg[r, mi] = tgt; j = fillsrch(st, sp, T[r] + DECL, tgt)
                    if j >= 0: fl[r, mi] = True; tf[r, mi] = st[j]
        for mi in range(3):
            m = fl[:, mi]
            if m.any():
                for k, dl in enumerate((0.0, 1000.0, 3000.0)): xb[m, mi, k] = D.l1(u, tf[m, mi] + 215.0 + dl)[0]
        FL.append(fl); TG.append(tg); TF.append(tf); XB.append(xb)
    print(d, sum(len(x) for x in OUT['t']), '%.0f s' % (time.time() - t0), flush=True)
np.savez_compressed(R10 + 'hz_%s.npz' % coin, cols=np.array(COLS_ALL), ncore=len(COLS), **{k: np.concatenate(v) for k, v in OUT.items()}, F=np.concatenate(FE), fl=np.concatenate(FL), tg=np.concatenate(TG), tf=np.concatenate(TF), xb=np.concatenate(XB), days=np.array(days))
print('fin', flush=True)
