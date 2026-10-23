#!/usr/bin/env python3
"""hedge.py b|pop DIA... -- Parte A del PREREG (sha fc6db829...): valor de la pata contraria (tomador inmediata, condicional, stop, maker)
sobre rellenos tipo B. Solo lectura de salida/datos (npz, unidades_b, desenlaces). Salida ../datos/hedge_{modo}_D.csv"""
import sys, os, json, math
import numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__))
SAL = os.path.join(AQ, '..', '..', 'salida', 'scripts'); sys.path.insert(0, SAL)
from msdata import Dia, DD   # DD = salida/datos (solo lectura)
OUT = os.path.join(AQ, '..', 'datos')
FEE = 0.07; LAT = 215
def fee(a): return FEE * a * (1 - a)
class Ctx:
    def __init__(s, D, own, opp): s.D, s.own, s.opp = D, own, opp
    def ask(s, t):
        """(ask, asz) del contrario con recepcion <= t; si falta o cruzado -> 1-bid propio"""
        D = s.D
        if s.opp is not None:
            q = D.top(s.opp, t)
            if q and q[1] == q[1] and 0 < q[1] < 1 and not (q[0] == q[0] and q[0] >= q[1]): return q[1], q[3]
        q = D.top(s.own, t)
        if q and q[0] == q[0] and 0 < q[0] < 1 and not (q[1] == q[1] and q[0] >= q[1]): return 1 - q[0], q[2]
        return None, None
def unidad(D, coin, fin5, out, t_ref, p, acc, gana, coste):
    lado = 'YES' if out == 'Up' else 'NO'; olado = 'NO' if lado == 'YES' else 'YES'
    own = D.tok(coin, '5min', fin5, lado); opp = D.tok(coin, '5min', fin5, olado)
    if own is None: return None
    C = Ctx(D, own, opp); fin_ms = fin5 * 1000
    pay1 = acc * gana
    r = dict(h0=pay1 - coste)
    # grupo adverso ex post (descriptivo)
    q5 = D.top(own, t_ref + 5000); r['bid5'] = q5[0] if q5 else np.nan
    r['adverso'] = int(bool(q5 and q5[0] == q5[0] and q5[0] <= p - 0.03))
    # HT0
    te = t_ref + 50
    a, sz = C.ask(te + LAT) if te <= fin_ms - 5000 else (None, None)
    if a is None: r['ht0'] = np.nan; r['ht0_a'] = np.nan
    else:
        a2 = a + (0.01 if (sz is None or not (sz >= acc)) else 0)
        r['ht0'] = acc - coste - acc * a2 - acc * fee(a2); r['ht0_a'] = a2
    # linea temporal del contrario (o del propio si no hay contrario)
    if opp is not None:
        s0, s1 = D.qs[opp], D.qs[opp + 1]; tt = D.qr[s0:s1]; vv = D.qv[s0:s1]
        av = vv[:, 1].astype(float); bv = vv[:, 0].astype(float)
        ok = (av > 0) & (av < 1) & ~(bv >= av)
    else:
        s0, s1 = D.qs[own], D.qs[own + 1]; tt = D.qr[s0:s1]; vv = D.qv[s0:s1]
        av = 1 - vv[:, 0].astype(float); ok = (av > 0) & (av < 1)
    w = (tt > t_ref) & (tt <= fin_ms - 5000 - LAT) & ok
    idx = np.nonzero(w)[0]; tw = tt[idx]; aw = av[idx]
    lock = 1 - p - aw - FEE * aw * (1 - aw)   # beneficio por accion si se cierra al ask del instante
    for m in (0.02, 0.05, 0.10):
        val = h0 = r['h0']; hit = 0
        for j in np.nonzero(lock >= m)[0]:
            ae, sze = C.ask(int(tw[j]) + LAT)
            if ae is not None and ae <= aw[j] + 1e-9 and sze is not None and sze >= acc:
                val = acc - coste - acc * ae - acc * fee(ae); hit = 1; break
        r[f'htc{int(m*100):02d}'] = val; r[f'htc{int(m*100):02d}_hit'] = hit
    for d in (0.03, 0.06, 0.10):
        val = r['h0']; hit = 0
        js = np.nonzero(-lock >= d)[0]
        if len(js):
            ae, sze = C.ask(int(tw[js[0]]) + LAT)
            if ae is not None:
                ae += 0.01 if not (sze is not None and sze >= acc) else 0
                val = acc - coste - acc * ae - acc * fee(ae); hit = 1
        r[f'hts{int(d*100):02d}'] = val; r[f'hts{int(d*100):02d}_hit'] = hit
    # HM: puja maker en el contrario
    t0, t1 = t_ref + 50, fin_ms - 10000
    ro, vo = D.trades(opp, t0, t1) if opp is not None else (np.array([]), np.zeros((0, 3)))
    rw, vw = D.trades(own, t0, t1)
    for m in (0.00, 0.02, 0.04):
        q = math.floor((1 - p - m) * 100 + 1e-6) / 100
        for nom, strict in (('', True), ('_opt', False)):
            if strict:
                so = vo[(vo[:, 1] == 0) & (vo[:, 0] < q - 1e-9)] if len(vo) else vo
                sw = vw[(vw[:, 1] == 1) & (vw[:, 0] > 1 - q + 1e-9)] if len(vw) else vw
            else:
                so = vo[(vo[:, 1] == 0) & (vo[:, 0] <= q + 1e-9)] if len(vo) else vo
                sw = vw[(vw[:, 1] == 1) & (vw[:, 0] >= 1 - q - 1e-9)] if len(vw) else vw
            f = min(acc, float(so[:, 2].sum() if len(so) else 0) + float(sw[:, 2].sum() if len(sw) else 0))
            r[f'hm{int(m*100):02d}{nom}'] = pay1 + f * (1 - gana) - coste - f * q
            r[f'hm{int(m*100):02d}{nom}_f'] = f / acc
    return r
def main(modo, dias):
    for d in dias:
        D = Dia(d); rows = []
        if modo == 'b':
            U = pd.read_csv(os.path.join(DD, 'unidades_b.csv')); U = U[(U.dia == d) & U.t_det.notna()]
            for u in U.itertuples():
                fin5 = int(u.mercado.split('-')[-1]) + 300
                r = unidad(D, u.coin, fin5, u.outcome, int(u.t_det * 1000), float(u.p_fill), float(u.acc), int(u.gana), float(u.coste))
                if r is None: print('sin token', u.mercado); continue
                rows.append(dict(mercado=u.mercado, outcome=u.outcome, coin=u.coin, dia=d, cierre=fin5, acc=u.acc, coste=u.coste, p=u.p_fill, gana=u.gana, **r))
        else:
            des = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
            des.update(json.load(open(os.path.join(DD, 'desenlaces_extra.json'))))
            Ub = pd.read_csv(os.path.join(DD, 'unidades_b.csv')); propios = set(zip(Ub.mercado, Ub.outcome))
            nm = nd = 0
            for k, (act, marco, mid, fin, lado) in enumerate(D.tmap):
                if marco != '5min' or act not in ('ETH', 'SOL', 'XRP'): continue
                fin5 = int(pd.Timestamp(str(fin)).timestamp()); out = 'Up' if lado == 'YES' else 'Down'
                slug = f'{act.lower()}-updown-5m-{fin5 - 300}'
                if (slug, out) in propios: continue
                o = D.tok(act, '5min', fin5, 'NO' if lado == 'YES' else 'YES')
                r1, v1 = D.trades(k, 0, 10**15); c1 = [(int(a), float(b[0])) for a, b in zip(r1, v1) if b[1] == 0]
                c2 = []
                if o is not None:
                    r2, v2 = D.trades(o, 0, 10**15); c2 = [(int(a), 1.0 - float(b[0])) for a, b in zip(r2, v2) if b[1] == 1]
                cand = sorted(x for x in c1 + c2 if 0.10 - 1e-9 <= x[1] <= 0.30 + 1e-9 and 65000 <= fin5 * 1000 - x[0] <= 295000)
                if not cand: continue
                nm += 1; w = des.get(str(mid))
                if w is None: nd += 1; continue
                trel, p = cand[0]; p = round(p, 2); g = int(w == lado)
                r = unidad(D, act, fin5, out, trel + 500, p, 5.0, g, 5 * p)
                if r is None: continue
                rows.append(dict(mercado=slug, outcome=out, coin=act, dia=d, cierre=fin5, acc=5.0, coste=5 * p, p=p, gana=g, **r))
            print(d, 'pob mercados-lado', nm, 'sin desenlace', nd)
        pd.DataFrame(rows).to_csv(os.path.join(OUT, f'hedge_{modo}_{d}.csv'), index=False)
        print(d, modo, 'unidades', len(rows), flush=True)
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
