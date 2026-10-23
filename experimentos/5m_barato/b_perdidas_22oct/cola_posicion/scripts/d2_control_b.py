#!/usr/bin/env python3
"""d2_control_b.py -- PREREG_CONTROL parte 1 (B). F (instante de la rafaga de cada relleno) vs R (instante aleatorio de ordenes NO rellenadas, vida>=1,25 s) vs P (prints a nivel
estrictamente mejor mientras viva la orden y sin relleno nuestro en 3 s). M_exit: otros(t-1000)>=5 y retirada neta >=80 % tras descontar prints en 850 ms. Estratos moneda x edad x A0.
IC90 por dia y por cierre, placebo por permutacion de etiqueta dentro de estrato, ponderado por EUR de la orden. Salida datos/control_b.txt, datos/control_b_eventos.csv"""
import os, sys, json, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_posicion/'
sys.path.insert(0, AQ)
import d1_l2_motor as M
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_CONTROL.md'), 'rb').read()).hexdigest().startswith('37f710e298664193')
rng = np.random.default_rng(20261022)
O = json.load(open(DL + 'ordenes_b.json')); TOK = {}
for l in open(DL + 'snap/ledger_B.jsonl'):
    d = json.loads(l)
    if d.get('tipo') == 'intencion_post': TOK[d['oid']] = d['tok']
Lb = pd.read_csv(os.path.join(D, 'b_l2.csv')).set_index('oid')
iso = lambda s: int(pd.Timestamp(s).timestamp() * 1000)
filled = set(Lb.index)
por_mercado = {}
for o in O:
    t = TOK.get(o['oid'])
    if t is None or t not in M.TM: continue
    act, mid, lado, fin = M.TM[t]; por_mercado.setdefault((act, mid), []).append((o, 'Y' if lado == 'YES' else 'N', fin))
rows = []
for (act, mid), lst in por_mercado.items():
    path = M.MK + f'{act}_{mid}.gz'
    if not os.path.exists(path): continue
    lvn, prn, tp, ap = M.carga(path)
    for o, L, fin in lst:
        q = M.mills(o['precio']); size = o['size']; oid = o['oid']
        tc = int(o.get('t_call0', 0) * 1000)
        if not tc: continue
        isf = oid in filled and not pd.isna(Lb.loc[oid].get('t_print', np.nan))
        arr = int(Lb.loc[oid].t_arr) if (oid in filled and not pd.isna(Lb.loc[oid].get('t_arr', np.nan))) else tc + 122
        if isf: end = int(Lb.loc[oid].t_print)
        elif o.get('t_fuera'): end = iso(o['t_fuera'])
        elif o.get('t_cancel_int'): end = iso(o['t_cancel_int']) + 65
        else: continue
        if oid in filled and not isf: continue          # relleno sin print localizado: missing, no entra como control
        def otros(L_, q_, t): return M.S(lvn, L_, q_, t) - (size if arr <= t <= end else 0.0)
        def met(t):
            s1 = otros(L, q, t - 1000); s2 = otros(L, q, t - 150); c, n = M.cons_between(prn, L, q, t - 1000, t - 150)
            return s1, s2, c, int(s1 >= 5 and (s1 - c - s2) >= 0.8 * s1), int(s2 <= 0.5)
        base = dict(oid=oid, coin=o['coin'], L=L, fin=fin, dia=o['ts_post'][:10], A0=o['cola'], eur=size * o['precio'])
        def add(grp, t):
            if t - arr < 1200 or not (arr <= t - 0 <= end + 1): return
            s1, s2, c, ex, al = met(t)
            if s1 < 5: return
            rows.append(dict(base, grp=grp, t=t, edad=(t - arr) / 1000, S1=s1, S2=s2, cons=c, exit=ex, alone=al))
        if isf: add('F', end)
        else:
            if end - arr >= 1260: add('R', int(rng.integers(arr + 1200, end - 50)))
        # P: prints a nivel mejor mientras viva (>=1,2 s tras llegada) y sin relleno nuestro en 3 s
        for (L_, q2), (rt, rs) in prn.items():
            if L_ != L or q2 <= q: continue
            for r in rt[(rt >= arr + 1200) & (rt <= end - 50)]:
                if isf and end - r < 3000: continue
                add('P', int(r))
E1 = pd.DataFrame(rows); E1.to_csv(os.path.join(D, 'control_b_eventos.csv'), index=False)
out = []
def P(*a): out.append(' '.join(str(x) for x in a))
E1['edad_b'] = pd.cut(E1.edad, [0, 2, 5, 1e9], labels=['<2', '2-5', '>=5']); E1['a0b'] = pd.cut(E1.A0, [-1, 0.5, 30, 1e9], labels=['0', '1-30', '>30'])
E1['est'] = E1.coin + '|' + E1.edad_b.astype(str) + '|' + E1.a0b.astype(str)
P(f'Eventos con otros(t-1000)>=5 y edad>=1,2 s: F {int((E1.grp=="F").sum())}, R {int((E1.grp=="R").sum())}, P {int((E1.grp=="P").sum())} (P de {E1[E1.grp=="P"].oid.nunique()} ordenes)')
# peso: en controles se reparte el EUR de la orden entre sus eventos del mismo grupo
E1['w'] = E1.eur / E1.groupby(['oid', 'grp']).oid.transform('size')
def delta(df, ctrl, col, nperm=0, seed=0):
    F = df[df.grp == 'F']; C = df[df.grp == ctrl]
    ests = sorted(set(F.est) & set(C.est))
    if not ests: return np.nan, np.nan, 0
    num = 0.0; den = 0.0
    for e in ests:
        f = F[F.est == e]; c = C[C.est == e]
        mf = np.average(f[col], weights=f.w); mc = np.average(c[col], weights=c.w); wf = f.w.sum(); num += wf * (mf - mc); den += wf
    return num / den, den, len(ests)
def run(ctrl, col):
    df = E1[E1.grp.isin(['F', ctrl])].copy(); obs, wsum, ne = delta(df, ctrl, col)
    # IC por cierre y por dia: bootstrap de clusters
    res = {}
    for key in ('fin', 'dia'):
        cl = df[key].unique(); v = []
        for _ in range(1000):
            pick = rng.choice(cl, len(cl)); s = pd.concat([df[df[key] == c] for c in pick]); d_, _, _ = delta(s, ctrl, col); v.append(d_)
        res[key] = np.nanpercentile(v, [5, 95])
    # placebo: permutar etiqueta F/ctrl dentro de estrato
    cnt = 0; v = []
    for _ in range(1000):
        s = df.copy(); lab = s.grp.values.copy()
        for e, ix in s.groupby('est').indices.items(): lab[ix] = rng.permutation(lab[ix])
        s['grp'] = lab; d_, _, _ = delta(s, ctrl, col); v.append(d_)
    v = np.array(v); p = float((v[~np.isnan(v)] >= obs).mean())
    return obs, res, p, ne
P('')
veredicto = {}
for ctrl in ('R', 'P'):
    for col in ('exit', 'alone'):
        sub = E1[E1.grp.isin(['F', ctrl])]
        mF = np.average(sub[sub.grp == 'F'][col], weights=sub[sub.grp == 'F'].w); mC = np.average(sub[sub.grp == ctrl][col], weights=sub[sub.grp == ctrl].w)
        obs, res, p, ne = run(ctrl, col)
        P(f'{col.upper():5s} F vs {ctrl}: tasa F {mF:.3f} (n={int((sub.grp=="F").sum())}) vs control {mC:.3f} (n={int((sub.grp==ctrl).sum())}); Delta estratificada {obs:+.3f} ({ne} estratos); IC90 por cierre ({res["fin"][0]:+.3f},{res["fin"][1]:+.3f}) por dia ({res["dia"][0]:+.3f},{res["dia"][1]:+.3f}); placebo p(>=obs)={p:.3f}')
        veredicto[(ctrl, col)] = (obs, res['fin'], p)
nF = int(((E1.grp == 'F')).sum())
fr = veredicto[('R', 'exit')]; fp = veredicto[('P', 'exit')]
okR = fr[0] > 0 and fr[1][0] > 0 and fr[2] < 0.10; okP = fp[0] > 0 and fp[1][0] > 0 and fp[2] < 0.10
v = 'NO CONCLUYENTE (n(F)<30)' if nF < 30 else ('A: especifica del relleno (firma de seleccion adversa)' if (okR and okP) else ('B: retirada general ante cualquier taker' if (okR and not okP) else 'C: artefacto / sin asociacion con F-R'))
P(f'\nVEREDICTO PREREGISTRADO (M_exit): {v} | F-R cumple {okR}, F-P cumple {okP}')
P('\nTasas por grupo (sin estratificar, ponderadas por EUR):'); P(E1.groupby('grp').apply(lambda d: pd.Series(dict(n=len(d), exit=np.average(d.exit, weights=d.w), alone=np.average(d.alone, weights=d.w), S1_med=d.S1.median(), edad_med=d.edad.median()))).round(3).to_string())
open(os.path.join(D, 'control_b.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
