#!/usr/bin/env python3
"""p4_m3_b.py (RE-B-COLA-CANCELA): M3 sobre rellenos de B 20-23 Oct como MECANISMO (contrato §8). L2 por nivel = cola_vs_cruce/mk (ETH/SOL/XRP
hasta 22-Oct 16:15Z; reloj t del fichero, rx ~ t+38 segun H-VT-6). Casado = 1.er T en nuestro nivel (SELL nuestro token a L o BUY comp a 1-L)
en [bloque-4,5 s, bloque-0,8 s]. R1: masa cancelada sin imprimir en (te-300,te] >= 50 % de Q(te-300), te en [t_c-1000, t_c-20-L_total]."""
import json, gzip, bisect, os, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)); MK = '/root/polymarket-research-datalogs/cola_vs_cruce/mk/'
TOKM = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json')); OWN = '0x659a40ff9920febc5a66836213040924343d297f'
T = pd.read_pickle(H + '/../tomador_202.pkl'); T['cl'] = T.causa.str.split('(').str[0]
M = pd.read_csv(H + '/out/b202_onchain.csv.gz', dtype={'tx': str, 'maker': str}); BT = M[M.maker.str.lower() == OWN].groupby('tx').ts_est.first()
def parse(fn):
    lv = {'Y': {}, 'N': {}}; bk = {'Y': {}, 'N': {}}; TR = {'Y': [], 'N': []}
    def rec(s_, p, t, z):
        e = lv[s_].setdefault(p, ([], [])); e[0].append(t); e[1].append(z)
    try:
        with gzip.open(fn, 'rt', errors='replace') as f:
            for ln in f:
                c = ln.rstrip('\n').split(',')
                if len(c) < 4 or c[0] not in lv: continue
                s_, ty = c[0], c[1]
                try:
                    if ty == 'B':
                        t = int(c[2]); new = {}
                        for it in c[3].split(';'):
                            if ':' in it: p, z = it.split(':'); new[round(float(p), 2)] = float(z)
                        for p in set(bk[s_]) | set(new):
                            if abs(bk[s_].get(p, 0) - new.get(p, 0)) > 1e-9: rec(s_, p, t, new.get(p, 0.0))
                        bk[s_] = new
                    elif ty == 'd':
                        t = int(c[2]); p = round(float(c[3]), 2); z = float(c[4]); o = bk[s_].get(p, 0.0)
                        if z > 0: bk[s_][p] = z
                        else: bk[s_].pop(p, None)
                        if abs(z - o) > 1e-9: rec(s_, p, t, z)
                    elif ty == 'T': TR[s_].append((int(c[2]), c[3], round(float(c[4]), 2), float(c[5])))
                except (ValueError, IndexError): continue
    except (EOFError, OSError): pass
    return lv, TR
rows = []
for r in T.itertuples():
    m = TOKM.get(str(r.tok)); bt = BT.get(r.tx)
    if m is None or bt is None: rows.append(dict(oid=r.oid, cov='sin_l2')); continue
    act, mid, lado, _ = m; fn = f'{MK}{act}_{mid}.gz'
    if not os.path.exists(fn): rows.append(dict(oid=r.oid, cov='sin_fichero')); continue
    lv, TR = parse(fn); me = 'Y' if lado == 'YES' else 'N'; ot = 'N' if me == 'Y' else 'Y'; L = round(r.L, 2)
    pr = sorted([(t, z) for (t, sd, p, z) in TR[me] if sd == 'SELL' and p == L] + [(t, z) for (t, sd, p, z) in TR[ot] if sd == 'BUY' and abs(p - (1 - L)) < 1e-6])
    cand = [t for t, z in pr if -4500 <= t - bt * 1000 <= -800]
    ser = lv[me].get(L)
    if not cand or ser is None: rows.append(dict(oid=r.oid, cov='sin_casado_o_nivel')); continue
    tc = min(cand, key=lambda t: abs(t - (bt * 1000 - 2300))); hr, hs = ser
    prt = [t for t, z in pr]; pcs = np.concatenate([[0], np.cumsum([z for t, z in pr])])
    def q(t):
        i = bisect.bisect_right(hr, t) - 1; return hs[i] if i >= 0 else None
    def printed(a, b): return pcs[bisect.bisect_right(prt, b)] - pcs[bisect.bisect_right(prt, a)]
    def fire(dl, tau=300, th=.5):
        cs = {tc - 1000, dl} | {t for t in hr if tc - 1000 - tau <= t <= dl} | {t + tau for t in hr if tc - 1000 - tau <= t <= dl}
        for te in sorted(x for x in cs if tc - 1000 <= x <= dl):
            qa, qb = q(te - tau), q(te)
            if qa and qb is not None and qa > 0 and max(0, qa - qb - printed(te - tau, te)) >= th * qa - 1e-9: return te
        return None
    f50, f90 = fire(tc - 20 - 53), fire(tc - 20 - (60 + 147))
    pnl = r.real_q * ((1.0 if r.gana == 1 else 0.0) - L); cost = r.real_q * L
    rows.append(dict(oid=r.oid, cov='ok', coin=r.coin, dia=r.dia, cl=r.cl, n_mk=r.n_mk, cola=r.cola, q150=q(tc - 150), F50=f50 is not None, F90=f90 is not None, pnl=pnl, cost=cost))
O = pd.DataFrame(rows); O.to_pickle(H + '/out/p4_m3_b.pkl'); res = {'cobertura': O['cov'].value_counts().to_dict()}
K = O[O['cov'] == 'ok'].copy(); K['F50'] = K.F50.astype(bool); K['F90'] = K.F90.astype(bool)
for nm, s in (('todos', K.index == K.index), ('clase1', K.cl == '1_propio_solo'), ('resto', K.cl != '1_propio_solo')):
    x = K[s]; o = dict(n=len(x), dias=x.dia.value_counts().to_dict())
    for f in ('F50', 'F90'):
        e = x[x[f]]; ne = x[~x[f]]
        o[f] = dict(n_disp=int(len(e)), frac=round(float(x[f].mean()), 3) if len(x) else None, pnl_evitados=round(float(e.pnl.sum()), 2), coste_evitados=round(float(e.cost.sum()), 2),
                    dPnL_total=round(float(-e.pnl.sum()), 2), buenos_perdidos=round(float(e[e.pnl > 0].pnl.sum()), 2), malos_evitados=round(float(-e[e.pnl < 0].pnl.sum()), 2),
                    n_buenos_perdidos=int((e.pnl > 0).sum()), por_dia={k: round(float(g.pnl.sum()), 2) for k, g in e.groupby('dia')})
    res[nm] = o
print(json.dumps(res, indent=1, default=str))
