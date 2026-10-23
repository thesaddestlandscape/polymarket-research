#!/usr/bin/env python3
"""trayectorias.py b|pop DIA... -- para cada unidad (posicion B o relleno tipo-B de la poblacion) calcula en tau = 5/15/30/60 s tras t_det
las senales (por RECEPCION <= t_dec) y el valor de salida (bid del top con recepcion <= t_dec+300 ms, -medio tick, comision 0,07 b(1-b)).
Tambien senales PRE-relleno en [t_rel-10 s, t_rel-0,3 s]. Salida datos/largo_{b|pop}_DIA.csv"""
import sys, os, json, math, csv
import numpy as np, pandas as pd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from msdata import Dia, SYM, DD
TAUS = (5, 15, 30, 60); FEE = 0.07
FILLSIDE = float(os.environ.get('FILLSIDE', '0'))   # valor de 'side' (1=BUY,0=SELL) de la operacion WS que rellena una puja (verificado con B)
def flujo(D, own, opp, t0, t1):
    fav = con = 0.0
    if own is not None:
        r, v = D.trades(own, t0, t1)
        for pr, sd, sz in v: (fav := fav + sz) if sd == 1 else (con := con + sz)
    if opp is not None:
        r, v = D.trades(opp, t0, t1)
        for pr, sd, sz in v: (con := con + sz) if sd == 1 else (fav := fav + sz)
    return fav, con
def unidad(D, coin, fin5, out, t_det, p_fill, acc, t_rel=None):
    lado = 'YES' if out == 'Up' else 'NO'; olado = 'NO' if lado == 'YES' else 'YES'
    own = D.tok(coin, '5min', fin5, lado); opp = D.tok(coin, '5min', fin5, olado)
    fin15 = int(math.ceil(fin5 / 900.0) * 900); t15 = D.tok(coin, '15min', fin15, lado)
    if own is None: return None
    sg = 1 if out == 'Up' else -1; sym = SYM[coin]
    b0 = D.top(own, t_det); bn0, _ = D.bn(sym, t_det); q15 = D.top(t15, t_det) if t15 is not None else None
    base = dict(own_ok=b0 is not None, bid_det=b0[0] if b0 else None, ask_det=b0[1] if b0 else None, bid15_det=q15[0] if q15 else None)
    # pre-relleno
    tr_ = t_rel if t_rel is not None else t_det
    pa, pb = tr_ - 10000, tr_ - 300
    qa = D.top(own, pa); qb = D.top(own, pb); ba, _ = D.bn(sym, pa); bb, _ = D.bn(sym, pb)
    fa = D.top(t15, pa) if t15 is not None else None; fb = D.top(t15, pb) if t15 is not None else None
    fav, con = flujo(D, own, opp, pa, pb)
    base.update(pre_dbid=(qb[0] - qa[0]) if (qa and qb and qa[0] and qb[0]) else None,
                pre_bn=((bb / ba - 1) * 1e4 * sg) if (ba and bb) else None,
                pre_d15=(fb[0] - fa[0]) if (fa and fb and fa[0] == fa[0] and fb[0] == fb[0]) else None,
                pre_fav=fav, pre_con=con)
    rows = []
    for tau in TAUS:
        td = t_det + tau * 1000
        r = dict(tau=tau, aplic=0)
        if td > fin5 * 1000 - 5000: rows.append({**base, **r}); continue
        q = D.top(own, td); bn, _ = D.bn(sym, td); f = D.top(t15, td) if t15 is not None else None
        e = D.top(own, td + 300)
        fav, con = flujo(D, own, opp, t_det, td)
        r.update(bid=q[0] if q else None, ask=q[1] if q else None, bsz=q[2] if q else None, asz=q[3] if q else None,
                 dbid=(q[0] - p_fill) if (q and q[0] == q[0]) else None,
                 bnret=((bn / bn0 - 1) * 1e4 * sg) if (bn and bn0) else None,
                 d15=(f[0] - q15[0]) if (f and q15 and f[0] == f[0] and q15[0] == q15[0]) else None,
                 fav=fav, con=con)
        if e and e[0] == e[0] and e[0] > 0 and acc >= 5 and not (e[1] == e[1] and e[0] >= e[1]):
            be = e[0]; px = be - (0.005 if (e[2] == e[2] and e[2] >= acc) else 0.01)
            r.update(aplic=1, salida=acc * max(px - FEE * be * (1 - be), 0.0), bid_exec=be)
        rows.append({**base, **r})
    return rows
def main(modo, dias):
    for d in dias:
        D = Dia(d); out_rows = []
        if modo == 'b':
            U = pd.read_csv(os.path.join(DD, 'unidades_b.csv')); U = U[(U.dia == d) & U.t_det.notna()]
            for u in U.itertuples():
                fin5 = int(u.mercado.split('-')[-1]) + 300
                rr = unidad(D, u.coin, fin5, u.outcome, int(u.t_det * 1000), u.p_fill, u.acc, t_rel=int(u.t_det * 1000) - 1500)
                if rr is None: print('sin token', u.mercado, u.outcome); continue
                for r in rr: out_rows.append(dict(mercado=u.mercado, outcome=u.outcome, coin=u.coin, dia=d, acc=u.acc, coste=u.coste,
                                                  payout=u.payout, gana=u.gana, p_fill=u.p_fill, T_det=u.T_det, **r))
        else:
            des = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
            ex = json.load(open(os.path.join(DD, 'desenlaces_extra.json'))) if os.path.exists(os.path.join(DD, 'desenlaces_extra.json')) else {}
            des.update(ex)
            Ub = pd.read_csv(os.path.join(DD, 'unidades_b.csv')); propios = set(zip(Ub.mercado, Ub.outcome))
            nm = nd = 0
            for k, (act, marco, mid, fin, lado) in enumerate(D.tmap):
                if marco != '5min': continue
                fin5 = int(pd.Timestamp(str(fin)).timestamp()); out = 'Up' if lado == 'YES' else 'Down'
                slug = f'{act.lower()}-updown-5m-{fin5 - 300}'
                if (slug, out) in propios: continue
                # relleno de una puja en X a p = SELL tomador en X a p, o BUY tomador en el opuesto a 1-p (cruce por acunado; asi
                # aparecen 128/166 rellenos reales de B, verificado 22-Oct)
                o = D.tok(act, '5min', fin5, 'NO' if lado == 'YES' else 'YES')
                r1, v1 = D.trades(k, 0, 10**15); c1 = [(int(a), float(b[0])) for a, b in zip(r1, v1) if b[1] == 0]
                c2 = []
                if o is not None:
                    r2, v2 = D.trades(o, 0, 10**15); c2 = [(int(a), 1.0 - float(b[0])) for a, b in zip(r2, v2) if b[1] == 1]
                cand = sorted(x for x in c1 + c2 if 0.10 - 1e-9 <= x[1] <= 0.30 + 1e-9 and 65000 <= fin5 * 1000 - x[0] <= 295000)
                if not cand: continue
                nm += 1
                w = des.get(str(mid))
                if w is None: nd += 1; continue
                trel, p = cand[0]; p = round(p, 4)
                rr = unidad(D, act, fin5, out, trel + 500, p, 5.0, t_rel=trel)
                if rr is None: continue
                for r in rr: out_rows.append(dict(mercado=slug, outcome=out, coin=act, dia=d, acc=5.0, coste=5 * p, payout=5.0 if w == lado else 0.0,
                                                  gana=int(w == lado), p_fill=p, T_det=fin5 - (trel + 500) / 1000, **r))
            print(d, 'pob: mercados-lado con relleno', nm, 'sin desenlace', nd)
        pd.DataFrame(out_rows).to_csv(os.path.join(DD, f'largo_{modo}_{d}.csv'), index=False)
        print(d, modo, 'filas', len(out_rows), flush=True)
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
