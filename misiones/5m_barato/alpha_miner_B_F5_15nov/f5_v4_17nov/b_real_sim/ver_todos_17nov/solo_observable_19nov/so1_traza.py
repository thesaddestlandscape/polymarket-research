#!/usr/bin/env python3
"""SO-1 (PREREG_SO1_19nov.md, sha 16543fc6...): traza publica contrafactual de la clase 1 (SOLO) de B, 20-22 Oct.
Solo lectura. Lee tomador_202.pkl + L2 de bids de ambos tokens (cola_vs_cruce/mk). <200 MB RAM."""
import gzip, json, os, pickle, sys
import numpy as np, pandas as pd

BASE = os.path.dirname(os.path.abspath(__file__)) + '/../'
MK = '/root/polymarket-research-datalogs/cola_vs_cruce/mk/'
TOKM = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json'))
W0, W1 = -50, 500
SHIFTS = [-30000, -20000, -10000, 10000, 20000, 30000]


def parse(fn):
    """{'Y'|'N': {precio_milesimas: (t[], s[])}} ; t = recepcion ms; s = nuevo total del nivel."""
    lv = {'Y': {}, 'N': {}}; book = {'Y': {}, 'N': {}}
    def rec(side, p, t, s):
        e = lv[side].setdefault(p, ([], [])); e[0].append(t); e[1].append(s)
    with gzip.open(fn, 'rt', errors='replace') as f:
        for ln in f:
            c = ln.rstrip('\n').split(',')
            if len(c) < 4 or c[0] not in lv: continue
            side, ty = c[0], c[1]
            try:
                if ty == 'B':
                    t = int(c[2]); new = {}
                    for it in c[3].split(';'):
                        if ':' in it:
                            p, s = it.split(':'); new[int(round(float(p) * 1000))] = float(s)
                    old = book[side]
                    for p in set(old) | set(new):
                        if abs(old.get(p, 0.0) - new.get(p, 0.0)) > 1e-9: rec(side, p, t, new.get(p, 0.0))
                    book[side] = new
                elif ty == 'd':
                    t = int(c[2]); p = int(round(float(c[3]) * 1000)); s = float(c[4]); o = book[side].get(p, 0.0)
                    if s > 0: book[side][p] = s
                    else: book[side].pop(p, None)
                    if abs(s - o) > 1e-9: rec(side, p, t, s)
            except (ValueError, IndexError):
                continue
    return {sd: {p: (np.array(a, np.int64), np.array(b, float)) for p, (a, b) in d.items()} for sd, d in lv.items()}


def subida(ser, t0, t1, thr):
    """True si algun cambio con recepcion en [t0,t1] sube el nivel >= thr respecto al valor previo."""
    if ser is None or len(ser[0]) == 0: return False
    t, s = ser; prev = np.concatenate([[0.0], s[:-1]]); m = (t >= t0) & (t <= t1)
    return bool(np.any((s[m] - prev[m]) >= thr - 1e-9))


def masa_en(sidebook, lo, hi, tcut):
    tot = 0.0
    for p in range(int(round(lo * 1000)), int(round(hi * 1000)) + 1, 10):
        ser = sidebook.get(p)
        if ser is None: continue
        i = np.searchsorted(ser[0], tcut, side='right') - 1
        if i >= 0: tot += ser[1][i]
    return tot


def main():
    d = pickle.load(open(BASE + 'tomador_202.pkl', 'rb'))
    d['cost'] = d.real_q * d.L; d['pnl'] = d.real_q * (d.gana - d.L)
    d['c1'] = d.causa.str.startswith('1_'); d['tp'] = d.causa == 'TP'
    cache = {}; rows = []
    for _, r in d.iterrows():
        m = TOKM.get(str(r.tok)); out = dict(oid=r.oid, dia=r.dia, coin=r.coin, causa=r.causa, estructura=r.estructura,
                                            tk_tipo=r.tk_tipo, en_L=bool(r.en_L), mas_alla=bool(r.mas_alla), tk_rem=float(r.tk_rem),
                                            cost=float(r.cost), pnl=float(r.pnl), c1=bool(r.c1), tp=bool(r.tp), mk=False)
        if m is not None:
            fn = MK + f'{m[0]}_{m[1]}.gz'
            if os.path.exists(fn):
                if fn not in cache:
                    if len(cache) > 8: cache.pop(next(iter(cache)))
                    cache[fn] = parse(fn)
                B = cache[fn]; own = 'Y' if m[2] == 'YES' else 'N'; comp = 'N' if own == 'Y' else 'Y'
                t3 = int(r.real_tm3); out['mk'] = True
                own_ser = B[own].get(int(round(r.L * 1000)))
                out['own_visible'] = bool(own_ser is not None and len(own_ser[0]) and own_ser[0][0] <= t3)
                rem_sh = float(r.tk_rem) * float(r.tk_sz)
                thr = 0.5 * rem_sh if r.tk_rem > 0.01 else 0.5 * float(r.real_q)
                P = int(round((1.0 - float(r.tk_eq)) * 100)) * 10  # 1-tk_eq al centimo, en milesimas
                ser = B[comp].get(P)
                out['rest'] = subida(ser, t3 + W0, t3 + W1, thr)
                for sh in SHIFTS: out[f'pl{sh // 1000:+d}'] = subida(ser, t3 + sh + W0, t3 + sh + W1, thr)
                out['tt_masa'] = masa_en(B[own], float(r.tk_eq), float(r.L) - 0.01, t3 - 20) if r.mas_alla else np.nan
                out['tt'] = bool(r.mas_alla and out['tt_masa'] >= 0.5 * float(r.real_q))
        rows.append(out)
    R = pd.DataFrame(rows); R.to_pickle(os.path.dirname(os.path.abspath(__file__)) + '/so1_filas.pkl')
    pl = [c for c in R.columns if c.startswith('pl')]
    def tasa(g, lab):
        g = g[g.mk]
        if len(g) == 0: print(lab, 'n=0'); return
        print(f"{lab:38s} n={len(g):3d} rest={g.rest.mean():.3f} placebo_max={g[pl].mean().max():.3f} placebo_medio={g[pl].values.mean():.3f}")
    print('cobertura mk:', R.groupby('causa').mk.agg(['sum', 'size']).to_dict())
    tasa(R[R.c1 & (R.tk_tipo == 'compra_comp') & (R.tk_rem > 0.01)], 'E1a clase1 comp rem>1%')
    tasa(R[R.c1 & (R.tk_tipo == 'compra_comp') & (R.tk_rem <= 0.01)], 'ctrl(i) clase1 comp rem<=1%')
    tasa(R[R.tp & (R.tk_tipo == 'compra_comp') & (R.tk_rem > 0.01)], 'ctrl(ii) TP comp rem>1%')
    tasa(R[R.c1 & (R.tk_tipo == 'compra_comp') & (R.tk_rem > 0.01) & R.en_L], '  E1a solo en_L')
    tasa(R[R.c1 & (R.tk_tipo == 'compra_comp') & (R.tk_rem > 0.01) & R.mas_alla], '  E1a solo mas_alla')
    g = R[R.c1 & R.mas_alla & (R.tk_rem <= 0.01) & R.mk]
    print(f"E1b TT clase1 mas_alla rem<=1% n={len(g)} tt={g.tt.mean() if len(g) else float('nan'):.3f} masa_med={g.tt_masa.median() if len(g) else float('nan')}")
    print('own_visible (alta propia en L2 antes del casado):', R[R.mk].own_visible.mean().round(3))
    json.dump({'n': int(len(R)), 'mk': int(R.mk.sum())}, open(os.path.dirname(os.path.abspath(__file__)) + '/so1_status.json', 'w'))


if __name__ == '__main__':
    main()
