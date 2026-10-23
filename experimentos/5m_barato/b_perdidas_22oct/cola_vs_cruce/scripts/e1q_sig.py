#!/usr/bin/env python3
"""e1q_sig.py A|B FASE -- PREREG_P3 (sha d004b159...). Paso A: por mercado, senales por tick (100 ms) sobre libro L2 libro5 por recepcion y
relleno B_FIEL con sus rasgos en r-300 ms -> DL/cola_vs_cruce/sig_<FASE>.npz + datos/sigfill_<FASE>.csv.
Paso B: reglas de mitigacion (cancelar/no postear si senal >= umbral, bloqueo 2 s) y placebos de igual tasa -> datos/e1q_sig_<FASE>.csv.gz."""
import sys, os, json, hashlib, bisect, collections
import numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_vs_cruce/'
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_P3_SENALES_C2.md'), 'rb').read()).hexdigest().startswith('d004b1599a7f6bcc')
PASO, FASE = sys.argv[1], sys.argv[2]; os.environ['E1Q_FASE'] = FASE
sys.path.insert(0, AQ); import e1q_sim as Q
STEP, T_HI, T_LO = Q.STEP, Q.T_HI, Q.T_LO
LATC, REPOST, BLOCK = 280, 1500, 2000
NOMS = ['SCANC', 'SFINO', 'SCAIDA', 'SVEL', 'SIMB', 'SFLUJO', 'SEDAD']
LV = np.arange(100, 410, 10)   # niveles 0,10..0,40

def mercados():
    TOK = json.load(open(Q.SRC + 'tokens.json')); mk = {}
    for t, v in TOK.items():
        if v[0] in ('ETH', 'SOL', 'XRP'): mk[(v[0], str(v[1]))] = int(float(v[3]))
    for (act, mid), fin in sorted(mk.items(), key=lambda x: x[1]):
        dia = pd.Timestamp(fin, unit='s').strftime('%Y-%m-%d')
        if dia not in Q.DIAS or not (Q.FIN_MIN <= fin <= Q.FIN_MAX): continue
        path = Q.SRC + f'mk/{act}_{mid}.gz'
        if not os.path.exists(path) or Q.DES.get(mid) is None: continue
        gi = bisect.bisect_left(Q.GALL, (fin - 305) * 1000)
        if gi < len(Q.GALL) and Q.GALL[gi] <= (fin - 60) * 1000: continue
        yield act, mid, fin, dia, path

def senales(ev, TT, TV, lvl, NT, L, g, k):
    """matriz (len(g), 7) de senales por tick con libro por recepcion <= t"""
    O = Q.OPP[L]; n = len(g)
    vec = np.zeros((n, len(LV))); b3 = np.zeros((n, 2))
    bids = {'Y': {}, 'N': {}}; i = 0
    for e in ev:
        r = e[0]
        while i < n and g[i] < r:
            bl = bids[L]; vec[i] = [bl.get(q, 0.0) for q in LV]
            for j, LL in enumerate((L, O)):
                ks = sorted(bids[LL], reverse=True)[:3]; b3[i, j] = sum(bids[LL][q] for q in ks)
            i += 1
        if i >= n: break
        if e[1] == 0: bids[e[2]] = dict(e[3])
        elif e[1] == 1:
            if e[4] > 0: bids[e[2]][e[3]] = e[4]
            else: bids[e[2]].pop(e[3], None)
    for j in range(i, n):
        vec[j] = vec[i - 1] if i > 0 else 0; b3[j] = b3[i - 1] if i > 0 else 0
    canc = sorted((x[0], q, max(0.0, -x[2] - x[3])) for (LL, q), h in lvl.items() if LL == L for x in h if x[2] < 0 and -x[2] - x[3] > 1e-9)
    cr = np.array([c[0] for c in canc], np.int64); cq = np.array([c[1] for c in canc]); cu = np.array([c[2] for c in canc])
    nt = NT[L]; ntr = np.array([x[0] for x in nt], np.int64); nts = np.cumsum([0.0] + [x[2] for x in nt])
    S = np.full((n, 7), np.nan); oo = np.full(n, -1)
    for i, t in enumerate(g):
        b = Q.top_at(TT, TV, L, t); bo = Q.top_at(TT, TV, O, t); a = 1000 - bo if bo > 0 else 9999
        o = Q.objetivo(b, a, k) if (110 < b <= 300 and b < a) else None
        if o is None: continue
        oo[i] = o; m = LV >= o
        S[i, 1] = -np.log1p(vec[i, m].sum())
        j0, j1 = np.searchsorted(cr, t - 1000, 'right'), np.searchsorted(cr, t, 'right')
        den = vec[max(i - 10, 0), m].sum() + 1.0
        S[i, 0] = cu[j0:j1][cq[j0:j1] >= o].sum() / den
        S[i, 2] = (Q.top_at(TT, TV, L, t - 2000) - b) / 10.0
        S[i, 3] = np.searchsorted(TT[L], t, 'right') - np.searchsorted(TT[L], t - 2000, 'right')
        tot = b3[i, 0] + b3[i, 1]; S[i, 4] = (b3[i, 1] - b3[i, 0]) / tot if tot > 0 else 0.0
        S[i, 5] = nts[np.searchsorted(ntr, t, 'right')] - nts[np.searchsorted(ntr, t - 2000, 'right')]
        lc = Q.lastchange(TT, TV, L, t); S[i, 6] = -(t - lc) if lc is not None else np.nan
    return S, oo

def politica_r(TT, TV, lvl, NT, fin, L, k, fire):
    """B_FIEL (settle 0, cancelacion +280 ms, reposicion 1,5 s) + regla: fire[i] -> cancelar/no postear, bloqueo 2 s"""
    g = (fin * 1000 - np.arange(T_HI * 1000, T_LO * 1000 - 1, -STEP)).astype(np.int64)
    live = None; t_next = 0; npost = 0
    for i, t in enumerate(g):
        b = Q.top_at(TT, TV, L, t); bo = Q.top_at(TT, TV, Q.OPP[L], t); a = 1000 - bo if bo > 0 else 9999
        cur = Q.objetivo(b, a, k) if (b > 0 and 110 < b <= 300 and b < a) else None
        f = fire is not None and fire[i]
        if live is not None:
            o, tl = live
            if cur is None or cur != o or f:
                res = Q.vida_orden(lvl, NT, L, o, tl, t + LATC, 5.0, 'prop')
                if res: return res + (o, npost)
                live = None; t_next = t + (BLOCK if f else REPOST)
            continue
        if f: t_next = max(t_next, t + BLOCK)
        if cur is None or t < t_next: continue
        live = (cur, int(t + Q.LAT_POST)); npost += 1
    if live is not None:
        res = Q.vida_orden(lvl, NT, L, live[0], live[1], int(g[-1]) + LATC, 5.0, 'prop')
        if res: return res + (live[0], npost)
    return (None, 0.0, None, None, npost)

def prepara_m(path, fin):
    ev = Q.load(path)
    if not ev: return None
    TT, TV, lvl, NT, roto = Q.prepara(ev, fin)
    if roto: return None
    g = (fin * 1000 - np.arange(T_HI * 1000, T_LO * 1000 - 1, -STEP)).astype(np.int64)
    L = None
    for t in g:
        for LL in ('Y', 'N'):
            if 110 < Q.top_at(TT, TV, LL, t) <= 300: L = LL; break
        if L: break
    if L is None: return None
    return ev, TT, TV, lvl, NT, L, g

def paso_a():
    rows = []; SS = {}; n = 0
    for act, mid, fin, dia, path in mercados():
        P = prepara_m(path, fin)
        if P is None: continue
        ev, TT, TV, lvl, NT, L, g = P; k = 2 if act == 'ETH' else 1
        S, oo = senales(ev, TT, TV, lvl, NT, L, g, k); SS[mid] = S.astype(np.float32)
        r, acc, tipo, o, npost = politica_r(TT, TV, lvl, NT, fin, L, k, None)
        gana = int((Q.DES[mid] == 'YES') == (L == 'Y'))
        row = dict(dia=dia, act=act, mid=mid, fin=fin, lado=L, gana=gana, fill=int(r is not None), acc=acc, p=(o / 1000 if o else np.nan), r=r)
        if r is not None:
            row['clase'] = Q.clase(NT, L, r, o, tipo); ii = int((r - 300 - g[0]) // STEP)
            if 0 <= ii < len(g): row.update({nm: float(S[ii, j]) for j, nm in enumerate(NOMS)})
        rows.append(row); n += 1
        if n % 200 == 0: print('A', FASE, n, flush=True)
    np.savez_compressed(DL + f'sig_{FASE}.npz', **SS)
    pd.DataFrame(rows).to_csv(os.path.join(D, f'sigfill_{FASE}.csv'), index=False); print('A FIN', FASE, n, flush=True)

def paso_b():
    Z = np.load(DL + f'sig_{FASE}.npz'); M = json.load(open(os.path.join(D, 'sig_modelo_ELEGIR.json')))
    rng = np.random.default_rng(20261022); rows = []; n = 0
    for act, mid, fin, dia, path in mercados():
        if mid not in Z.files: continue
        P = prepara_m(path, fin)
        if P is None: continue
        ev, TT, TV, lvl, NT, L, g = P; k = 2 if act == 'ETH' else 1; S = Z[mid].astype(float)
        gana = int((Q.DES[mid] == 'YES') == (L == 'Y'))
        Sz = (S - np.array(M['mu'])) / np.array(M['sd']); lg = np.nan_to_num(Sz) @ np.array(M['coef']) + M['b0']
        reglas = {'B_FIEL': None}
        for j, nm in enumerate(NOMS + ['LOGIT']):
            x = lg if nm == 'LOGIT' else S[:, j]
            for tasa in ('05', '15'): reglas[f'{nm}_{tasa}'] = np.nan_to_num(x, nan=-1e18) >= M['umbral'][nm][tasa]
        for tasa, pr in (('05', 0.05), ('15', 0.15)): reglas[f'PLACEBO_{tasa}'] = rng.random(len(g)) < pr
        for nm, fire in reglas.items():
            r, acc, tipo, o, npost = politica_r(TT, TV, lvl, NT, fin, L, k, fire)
            rows.append(dict(dia=dia, act=act, mid=mid, fin=fin, lado=L, gana=gana, var=nm, alloc='prop', fill=int(r is not None), acc=acc,
                             p=(o / 1000 if o else np.nan), r=r, clase=(Q.clase(NT, L, r, o, tipo) if r is not None else None), npost=npost))
        n += 1
        if n % 200 == 0: print('B', FASE, n, flush=True)
    pd.DataFrame(rows).to_csv(os.path.join(D, f'e1q_sig_{FASE}.csv.gz'), index=False); print('B FIN', FASE, n, flush=True)

if __name__ == '__main__':
    paso_a() if PASO == 'A' else paso_b()
