#!/usr/bin/env python3
"""Evaluador forward H-Q11-THRU1 (PREREG_Q11_THRU1_FWD.md sha 68ca25a0, ADDENDUM3 sha c991602c, ADDENDUM4 sha 3dac1bf4: REFUTA solo con evidencia contraria significativa, tabla thru1 A-H, tope). Solo lectura de pickles + escritura de salida; 0 ordenes. EXPLORATORIA.
Entradas por dia D (producidas por scripts SIN tocar, ver --producir): toxicidad_thru1/out/RT_D.pkl (passT.py: G0, GEO6, CXJ150, NJ3A, CXJ1000, CXB_l, GEO6NJ3) y
redteam/out/RT_D.pkl (rt_sim.py: G0/GEO6/PG_O50 x BASE/STRICT/OPT/CROSS/THIN). PC_AS = G0 menos los rellenos NO de las unidades (cierre, moneda) marcadas (exacto: un token por orden).
Modos:  --aceptacion            prueba sobre QUEMADOS (G0 2938, -166,9, EV -0,076; thru1 n 2321 EV -0,125; dPnL GEO6 +140, CXJ150 +128 +-1): escribe thru1_fwd/aceptacion.json
        --evaluar [--hoy D]      informe diario DESCRIPTIVO + checkpoints 10/20 + estado terminal (thru1_fwd/estado_thru1.json); exige aceptacion PASS y sha de codigo
        --producir D             genera Po_D (modelo OWN), passT D y rt_sim D con nice/ionice/ulimit (pesado: fuera de 06:00-09:15Z, uno a la vez)
        --desde/--salida         ensayo (p.ej. --desde 2026-10-26 --salida /tmp/x --sin-validez)"""
import sys, os, json, hashlib, argparse, subprocess, glob, ast, datetime as dt
sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/forward_sol013/')
import numpy as np, pandas as pd
import q11_decision as Q
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'; PB = P2 + 'precursores_barrido/out/'
TX, RTD, BCO, RXD = HERE + 'toxicidad_thru1/out/', HERE + 'redteam/out/', HERE + 'barrido_corr/out/', HERE + 'redteam/out_cxj150/'
PRICES = '/root/polymarket-research/data/prices/'
FWD_DESDE = '2026-11-07'; SEED = 20261107; B = 4000
PREREG = '/root/polymarket-research/misiones/5m_barato/docs/reverse-engineering/casos/RE-THRU1/PREREG_Q11_THRU1_FWD.md'
SHAS = {  # codigo/modelo registrados (prereg: engine.py, passT.py, rt_sim.py, modelo OWN; engine fijado aqui el 06-Nov con el valor vigente)
    P2 + 'escalera_B/engine.py': 'a7b8431a73952524917ffd90e65b2dcf2779fabd3c452bc0407d36e34b1e8feb',
    HERE + 'toxicidad_thru1/passT.py': 'a8b9d7a0158fd0b0cf47582c499d6c1cc870269310c8ef4481482733d1c64038',
    HERE + 'redteam/rt_sim.py': '86b14afbf91b308ab6185e0060427047fc644a6a0ac33813127627ef507f652b',
    HERE + 'redteam/rt_cxj150_cross.py': 'ef9fde82e977cb87b266e57b0b0e1477a3bb5e87b261a78b16fd090561ca37fe',   # CXJ150 bajo BASE/CROSS (nuevo 09-Nov, ADDENDUM4; lee rt_sim.py/passT.py con sha comprobado)
    HERE + 'forward_pg/modelo_own.pkl': 'f80d7b573bd74084a8fb6b601af84f0eab7c7d8dd155f1f17d90070d28eb3839',
    HERE + 'forward_pg/modelo_own.json': '35adc359660d8b99f3719d73989d1f9f9dc2ef20a974e159a0ec577cf69ab8dd',
    HERE + 'forward_pg/entrenar_own.py': 'ea9f59056d0e3283bba5bc498a6242093eb20cbf2cbcb4d6e5acf94f49b30a68',
    PREREG: '68ca25a04bb4fb7cb8f9f5161b57155baaf6e9ead89170ad03ad284100bfe33e'}
ARMS = ['PG_O50', 'GEO6', 'CXJ150', 'PC_AS']; FV = ('BASE', 'STRICT', 'OPT', 'THIN', 'CROSS')
QUEMADOS = [f'2026-10-{d}' for d in range(26, 32)] + [f'2026-11-0{d}' for d in range(1, 5)]
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def eval_sha():
    """sha de la aceptacion = sha256(sha(eval_thru1.py) + sha(q11_decision.py)): editar cualquiera de los dos invalida aceptacion.json (la guardia por sha se mantiene)."""
    return hashlib.sha256((sha(__file__) + sha(Q.__file__)).encode()).hexdigest()
def check_shas():
    return [f'{os.path.basename(p)}: {sha(p)[:12]} != {h[:12]}' for p, h in SHAS.items() if not os.path.exists(p) or sha(p) != h]
def atomic(path, text):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True); tmp = path + '.tmp'
    with open(tmp, 'w') as f: f.write(text); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)
# ---------------- carga ----------------
def cargar(dias):
    """-> (T, R, S, RX, err). err = lista de ERROR_DATOS (filas con dia != D): el llamador NO escribe estado y muestra los terminales (ADDENDUM4 5b)."""
    T, R, S, X, err = [], [], [], [], []
    for d in dias:
        T.append(pd.read_pickle(f'{TX}RT_{d}.pkl')); R.append(pd.read_pickle(f'{RTD}RT_{d}.pkl')); S.append(pd.read_pickle(f'{TX}SEGT_{d}.pkl'))
        if os.path.exists(f'{RXD}RX_{d}.pkl'): X.append(pd.read_pickle(f'{RXD}RX_{d}.pkl'))   # CXJ150 bajo BASE/CROSS (rt_cxj150_cross.py); su falta solo invalida el dia para CXJ150
        for nm, x in (('passT', T[-1]), ('rt_sim', R[-1])) + ((('rt_cxj150_cross', X[-1]),) if os.path.exists(f'{RXD}RX_{d}.pkl') else ()):
            if len(x) and (x['dia'].astype(str) != d).any(): err.append(f'{nm} RT_{d}.pkl: filas con dia != {d}')
    cat = lambda L: pd.concat(L, ignore_index=True) if L else pd.DataFrame()
    return cat(T), cat(R), cat(S), cat(X), err
def feat_chainlink(dias, units, hoy=None, cache=None):
    """r1, r4 por unidad (fin, act): a = fin-303 s; r1 = ln(CL(a)/CL(a-3600)), r4 = ln(CL(a-3600)/CL(a-18000)); source=='chainlink', recepcion, tolerancia 20 s.
    Serie por dia desde la cache propia (q11_decision.cl_dia: el CSV de data/prices rota a ~20 d) con UNA lectura por dia. Fail-closed: CSV ausente/vacio => ERROR_DATOS
    del brazo PC_AS (se devuelve en `err`; r1/r4 quedan NaN y el llamador NO los usa). -> (units con r1, r4, err)"""
    need = sorted({(pd.Timestamp(d) - pd.Timedelta(days=k)).strftime('%Y-%m-%d') for d in dias for k in (0, 1)})
    out = units.copy(); out['r1'] = np.nan; out['r4'] = np.nan
    S, err = Q.cl_series(need, Q.COINS, hoy, cache)
    if err: return out, err
    for coin in Q.COINS:
        m = (units.act == coin).values
        if not m.any(): continue
        ms, pp = S[coin]
        def px(t):
            i = np.searchsorted(ms, t, side='right') - 1; ok = (i >= 0) & (t - ms[np.clip(i, 0, None)] < 20000); return np.where(ok, pp[np.clip(i, 0, None)], np.nan)
        a = (units.fin.values[m] * 1000 - 303000).astype('int64')
        with np.errstate(all='ignore'): out.loc[m, 'r1'] = np.log(px(a) / px(a - 3600000)); out.loc[m, 'r4'] = np.log(px(a - 3600000) / px(a - 18000000))
    return out, []
def armar_base(T, R, S, X, dias, hoy=None, cache=None):
    """-> dict nombre -> DataFrame de rellenos (cols fin,dia,act,lado,pnl,cost) y dict (arm,fv)-> idem para cotas; unit table de PC_AS."""
    g0 = T[T['var'] == 'G0']; A = {'G0': g0, 'GEO6': T[T['var'] == 'GEO6'], 'CXJ150': T[T['var'] == 'CXJ150']}
    for v in ('NJ3A', 'CXJ1000', 'GEO6NJ3', 'CXB150', 'CXB300', 'CXB1000', 'CXB3000'): A[v] = T[T['var'] == v]
    for p in ('G0', 'GEO6', 'PG_O50'):
        for f in FV: A[f'rt_{p}_{f}'] = R[(R.pol == p) & (R.fv == f)]
    for f in ('BASE', 'CROSS'): A[f'rt_CXJ150_{f}'] = X[X.fv == f] if len(X) else R.iloc[:0]   # script rt_cxj150_cross.py (ADDENDUM4: C3 de CXJ150)
    # PC_AS: unidades NO de los segmentos G0 (cobertura del rasgo) y marca por (fin, act)
    U = S[S.lado == 'NO'][['dia', 'fin', 'act']].drop_duplicates().reset_index(drop=True); U, cl_err = feat_chainlink(dias, U, hoy, cache)
    U['flag'] = (U.r1 > 0) & (U.r4 < 0); cov = float(U.r1.notna().mean()) if len(U) else float('nan')
    fl = set(map(tuple, U[U.flag][['fin', 'act']].values))
    def pcas(x): return x[~((x.lado == 'NO') & pd.Series([(a, b) in fl for a, b in zip(x.fin, x.act)], index=x.index))] if len(x) else x
    A['PC_AS'] = pcas(g0)
    for f in FV: A[f'rt_PC_AS_{f}'] = pcas(A[f'rt_G0_{f}'])
    return A, U, cov, cl_err
# ---------------- metricas ----------------
def pc(x): return x.groupby('fin').pnl.sum() if len(x) else pd.Series(dtype=float)
def dser(a, b): return pc(a).sub(pc(b), fill_value=0.0)
def dia_of(x): return x.groupby('fin').dia.first()
def boot_sum(v, seed, Bn=B):
    v = np.asarray(v, float)
    if len(v) < 3: return None
    return v[np.random.default_rng(seed).integers(0, len(v), (Bn, len(v)))].sum(axis=1)
def stats_dpnl(a, b, days):
    s = dser(a, b); n = len(s); d = pd.concat([dia_of(a), dia_of(b)]).groupby(level=0).first().reindex(s.index)
    sd = s.groupby(d.values).sum().reindex(days).fillna(0.0)
    vc, vd = boot_sum(s.values, SEED), boot_sum(sd.values, SEED)
    r = dict(tot=float(s.sum()) if n else float('nan'), ncierres=n, nnz=int((s.abs() > 1e-12).sum()), dias=sd.to_dict(),
             ic_c=(Q.q(vc, .05), Q.q(vc, .95), Q.q(vc, .0125), Q.q(vc, .9875)), ic_d=(Q.q(vd, .05), Q.q(vd, .95), Q.q(vd, .0125), Q.q(vd, .9875)))
    r['sin2dias'] = float(sd.sort_values(ascending=False).iloc[2:].sum()) if len(sd) > 2 else float('nan')
    r['sin5cierres'] = float(s.sort_values(ascending=False).iloc[5:].sum()) if n > 5 else float('nan')
    return r
def ev_stats(x):
    e = Q.ev(x); v = Q.vec_cierre(x, B, SEED); s2 = Q.sin2(x)
    c = x.groupby('fin').pnl.sum().sort_values(ascending=False); k5 = c.iloc[5:].sum() if len(c) > 5 else float('nan')
    return dict(ev=e, ic_inf=Q.q(v, .05), ic_inf_p=Q.q(v, .0125), sin2dias=s2, sin5=float(k5))
def placebo_pcas(U, pnl_no, days_cnt):
    """PC_AS placebo (1000 perm.): permuta dentro de cada dia el signo de r1 entre unidades (cierre, moneda) NO; estadistico dPnL BASE = -sum pnl G0-NO de las unidades marcadas."""
    u = U[U.r1.notna() & U.r4.notna() & U.dia.isin(days_cnt)].reset_index(drop=True)
    if not len(u): return Q.NAN, Q.NAN, Q.NAN
    p = np.array([pnl_no.get((f, a), 0.0) for f, a in zip(u.fin, u.act)]); sg = np.sign(u.r1.values); r4 = u.r4.values
    grp = [np.where(u.dia.values == d)[0] for d in pd.unique(u.dia)]; stat = lambda s: -p[(s > 0) & (r4 < 0)].sum()
    obs = stat(sg); rng = np.random.default_rng(SEED); perm = []
    for _ in range(1000):
        sp = sg.copy()
        for ix in grp: sp[ix] = rng.permutation(sg[ix])
        perm.append(stat(sp))
    m = float(np.mean(perm)); pv = (1 + sum(abs(x - m) >= abs(obs - m) for x in perm)) / 1001
    return float(obs), m, pv
# ---------------- validez de dia ----------------
def dia_valido(d):
    """Insumos completos, horas sanas (bad_D.json), Binance 3 monedas con cobertura >=0,95 de segundos en horas sanas. (El rasgo de PC_AS >=95 % se comprueba en evaluar.)"""
    cache = HERE + f'thru1_fwd/validez_{d}.json'
    if os.path.exists(cache): return json.load(open(cache))
    sys.path.insert(0, HERE + 'barrido_multi'); import bfeat
    falta = [n for n, ok in (('tape', os.path.exists(PB + f'tape_{d}.pkl')), ('bad', os.path.exists(PB + f'bad_{d}.json')), ('x_binance', bool(bfeat.xfile(d))),
                             ('RT_passT', os.path.exists(f'{TX}RT_{d}.pkl')), ('RT_rt_sim', os.path.exists(f'{RTD}RT_{d}.pkl'))) if not ok]
    if falta: return dict(dia=d, valido=False, motivo='faltan: ' + ','.join(falta))   # sin cache: puede completarse mas tarde
    bad = {int(h) for dd, h in json.load(open(PB + f'bad_{d}.json'))['bad'] if dd == d}; sanas = [h for h in range(24) if h not in bad]
    if not sanas: r = dict(dia=d, valido=False, motivo='0 horas sanas')
    else:
        t0 = int(pd.Timestamp(d, tz='UTC').timestamp()); segs = {}
        for ch in pd.read_csv(bfeat.xfile(d), header=None, usecols=[2, 7], names=['sym', 'recv'], dtype={'sym': 'category', 'recv': 'int64'}, chunksize=1500000):
            for sym, g in ch.groupby('sym', observed=True):
                s = np.unique(g.recv.values // 1000 - t0); segs.setdefault(str(sym)[:-4], []).append(s[(s >= 0) & (s < 86400)])
        cov = {}
        for c in ('ETH', 'SOL', 'XRP'):
            s = np.unique(np.concatenate(segs[c])) if c in segs else np.array([], int); ok = np.isin(s // 3600, sanas)
            cov[c] = float(ok.sum() / (3600 * len(sanas)))
        r = dict(dia=d, valido=min(cov.values()) >= 0.95, motivo='' if min(cov.values()) >= 0.95 else 'Binance cobertura < 0,95', cobertura_binance=cov, horas_sanas=len(sanas))
    atomic(cache, json.dumps(r, indent=1)); return r
# ---------------- checkpoint de un brazo ----------------
def checkpoint(arm, A, days, cp, U, plc):
    """Evalua C1-C10 sobre los primeros `cp` dias que cuentan. A: dict de brazos; days: lista cronologica (ya cortada)."""
    if arm == 'PG_O50': a, b = A['rt_PG_O50_BASE'], A['rt_G0_BASE']
    else: a, b = A[arm], (A['G0'])
    a, b = a[a.dia.isin(days)], b[b.dia.isin(days)]
    st = stats_dpnl(a, b, days); eva = ev_stats(a); nd = len(days); c = {}
    c['C1 nd>=10, >=300 rellenos BASE, >=40 cierres con dPnL!=0'] = nd >= 10 and len(a) >= 300 and st['nnz'] >= 40
    c['C2 dPnL BASE>0, IC90 cierre inf>0 e IC90 dia inf>0'] = Q.gt(st['tot']) and Q.gt(st['ic_c'][0]) and Q.gt(st['ic_d'][0])
    ak, bk = A[f'rt_{arm}_CROSS'], A['rt_G0_CROSS']; cross = float(dser(ak[ak.dia.isin(days)], bk[bk.dia.isin(days)]).sum())   # CXJ150: de rt_cxj150_cross.py (dias sin RX_D no cuentan para CXJ150)
    c['C3 dPnL CROSS>0 (si no: NO IDENTIFICADO POR EL RELLENO)'] = Q.gt(cross)
    c['C4 dPnL sin 2 mejores dias>0 y sin 5 mejores cierres>0'] = Q.gt(st['sin2dias']) and Q.gt(st['sin5cierres'])
    c['C5 EV abs BASE>0, IC90 cierre inf>0, sin 2 mejores dias>0, sin 5 mejores cierres>0'] = Q.gt(eva['ev']) and Q.gt(eva['ic_inf']) and Q.gt(eva['sin2dias']) and Q.gt(eva['sin5'])
    dd = pd.Series(st['dias']); k = int((dd > 1e-12).sum()); c[f'C6 dPnL_d>0 en >=60 % de dias ({k}/{nd})'] = nd >= 1 and 5 * k >= 3 * nd
    ys = stats_dpnl(a[a.lado == 'YES'], b[b.lado == 'YES'], days)['tot']
    gno = b[b.lado == 'NO'].groupby('dia').pnl.sum().reindex(days).fillna(0.0); dno = pd.Series(stats_dpnl(a[a.lado == 'NO'], b[b.lado == 'NO'], days)['dias'])
    cnt = int(((gno >= 0) & (dno.reindex(days).fillna(0.0) > 0)).sum())
    c['C7 dPnL_YES>0, o >=3 dias con G0-NO>=0 y dPnL_NO>0 (si no: NO SEPARABLE DEL REGIMEN)'] = Q.gt(ys) or cnt >= 3
    placebo = None
    if arm == 'PC_AS':
        pno = b[b.lado == 'NO'].groupby(['fin', 'act']).pnl.sum().to_dict(); o, m, p = placebo_pcas(U, pno, set(days)); placebo = dict(d_obs=o, m=m, p=p)
        c['C8 placebo p<=0,10 y d_obs>m'] = p == p and p <= 0.10 and o > m
    elif arm == 'CXJ150':
        placebo = plc if plc and sorted(plc.get('dias', [])) == sorted(days) else None
        c['C8 placebo p<=0,10 y d_obs>m'] = bool(placebo and placebo['p'] <= 0.10 and placebo['d_obs'] > placebo['m'])
    shrink = None; pgg = None
    if arm == 'PG_O50':
        g6 = A['rt_GEO6_BASE']; sp = stats_dpnl(a, g6[g6.dia.isin(days)], days); pgg = sp['tot']
        ok9 = Q.gt(sp['tot']) and Q.gt(sp['ic_c'][0])
        if cp == 10 and nd >= 10:
            m1, m2 = dd.iloc[:5].mean(), dd.iloc[5:10].mean(); shrink = (float(m1), float(m2)); ok9 = ok9 and not (m2 < 0.5 * m1)
        c['C9 PG_O50-GEO6>0 con IC90 cierre inf>0; sin encogerse (cp10)'] = ok9
    cand = all(c.values())
    return dict(cp=cp, dias=list(days), nd=nd, candidato=bool(cand), conds={k_: bool(v) for k_, v in c.items()}, dpnl=st, ev=eva, n_arm=len(a), cross=cross, placebo=placebo, pg_menos_geo6=pgg, shrink=shrink,
                label=('CANDIDATO (EXPLORATORY hasta medicion L2)' if cand else 'NO CANDIDATO'))
def promocion(arm, res, tok):
    st, ev_, pl = res['dpnl'], res['ev'], res.get('placebo'); f = Q.f3
    a1 = Q.gt(st['ic_c'][2]); a2 = Q.gt(st['ic_d'][2]); a3 = Q.gt(ev_['ic_inf_p'])
    if arm in ('CXJ150', 'PC_AS'): a4 = bool(pl) and pl['p'] == pl['p'] and pl['p'] <= 0.025 and pl['d_obs'] > pl['m']; ptxt = f'{pl["p"]:.4f}' if pl else 'nan'
    else: a4 = True; ptxt = 'no aplica'
    ok = tok == 'CANDIDATO' and res['candidato'] and a1 and a2 and a3 and a4
    return (f'PROMOCION (alfa/4): {"SI" if ok else "NO"} | brazo={arm} | seguimiento={tok} | dPnL BASE IC cierre inf 1,25%={f(st["ic_c"][2])} req >0: {Q.si(a1)} | dPnL BASE IC dia inf 1,25%={f(st["ic_d"][2])} req >0: {Q.si(a2)}'
            f' | EV abs IC cierre inf 1,25%={f(ev_["ic_inf_p"])} req >0: {Q.si(a3)} | placebo p={ptxt} req <=0,025: {"no aplica" if ptxt == "no aplica" else Q.si(a4)}')
# ---------------- REFUTA thru1 (ADDENDUM4 sec. 3) ----------------
def refuta_fuerte(res):
    """REFUTA fuerte (ADDENDUM4 sec. 3), TODAS: dPnL BASE < 0 definido con >=3 cierres; limite SUPERIOR del IC90 por cierre < 0 y por dia < 0; >=300 rellenos BASE del brazo en esos dias."""
    st = res['dpnl']; c = {'dPnL BASE<0': Q.lt(st['tot']), '>=3 cierres': st['ncierres'] >= 3, 'IC90 cierre sup<0': Q.lt(st['ic_c'][1]), 'IC90 dia sup<0': Q.lt(st['ic_d'][1]), '>=300 rellenos BASE': res['n_arm'] >= 300}
    return all(c.values()), ', '.join(f'{k}={Q.si(v)}' for k, v in c.items()) + f' (dPnL {Q.f3(st["tot"])}, IC90c sup {Q.f3(st["ic_c"][1])}, IC90d sup {Q.f3(st["ic_d"][1])}, n={res["n_arm"]})'
def motivo_refuted(res):
    """Motivo anotado del REFUTED del checkpoint 20 (no es regla de decision): C3 -> 'no identificado por el relleno', C7 -> 'no separable del regimen', resto = condiciones fallidas."""
    fallan = [k for k, v in res['conds'].items() if not v]; m = []
    if any(k.startswith('C3') for k in fallan): m.append('no identificado por el relleno')
    if any(k.startswith('C7') for k in fallan): m.append('no separable del regimen')
    return '; '.join(m + ['condiciones no cumplidas: ' + ','.join(k.split(' ')[0] for k in fallan)])
# ---------------- evaluacion ----------------
def aceptacion(salida):
    T = pd.concat([pd.read_pickle(f'{TX}RT_{d}.pkl') for d in QUEMADOS], ignore_index=True)
    g0 = T[T['var'] == 'G0']; th = g0[g0.ftype == 'thru1']
    r = dict(g0_n=len(g0), g0_pnl=float(g0.pnl.sum()), g0_ev=float(Q.ev(g0)), thru1_n=len(th), thru1_ev=float(Q.ev(th)),
             d_geo6=float(dser(T[T['var'] == 'GEO6'], g0).sum()), d_cxj150=float(dser(T[T['var'] == 'CXJ150'], g0).sum()))
    ok = {'G0 n=2938': r['g0_n'] == 2938, 'G0 pnl -166,9+-1': abs(r['g0_pnl'] + 166.9) <= 1, 'G0 EV -0,076': abs(r['g0_ev'] + 0.076) <= 0.0006, 'thru1 n=2321': r['thru1_n'] == 2321,
          'thru1 EV -0,125': abs(r['thru1_ev'] + 0.125) <= 0.0006, 'dPnL GEO6 +140+-1': abs(r['d_geo6'] - 140) <= 1, 'dPnL CXJ150 +128+-1': abs(r['d_cxj150'] - 128) <= 1}
    out = dict(pass_=all(ok.values()), checks=ok, valores=r, eval_sha=eval_sha(), fecha=Q.hoy_utc(), dias=QUEMADOS)
    atomic(salida + '/aceptacion.json', json.dumps(out, indent=1, default=float)); return out
def evaluar(a):
    sal = a.salida; os.makedirs(sal, exist_ok=True); hoy = a.hoy or Q.hoy_utc(); L = [f'# INFORME DIARIO H-Q11-THRU1 forward (DESCRIPTIVO; ningun veredicto fuera de checkpoints) generado {dt.datetime.now(dt.timezone.utc):%FT%TZ} | hoy={hoy}']
    spath = sal + '/estado_thru1.json'
    def terminales(err=()):
        """ADDENDUM4 A/5b: ante sha distinto, ERROR_DATOS o aceptacion pendiente, un terminal ya emitido se muestra igualmente (con ' [EN REVISION]' si el error afecta a dias <= su fecha). NO escribe estado."""
        ST0 = json.load(open(spath)) if os.path.exists(spath) else {'arms': {}}
        for arm_, s_ in ST0['arms'].items():
            if s_.get('terminal'): tok_, why_, _ = Q.veredicto({'terminal': s_['terminal']}, list(err), 0, 0, False, False, hoy); L.append(f'VEREDICTO {arm_}: {tok_} ({why_})')
    def fin_(msg):
        L.append(msg); atomic(f'{sal}/informe_thru1_{hoy}.txt', '\n'.join(L) + '\n'); print('\n'.join(L)); sys.exit(0)
    bad = check_shas()
    if bad: terminales(); fin_('INSUFFICIENT (ERROR_DATOS: sha distinto del registrado => parada hasta corregir; no se escribe estado): ' + '; '.join(bad))
    if not a.ensayo:
        ac = json.load(open(sal + '/aceptacion.json')) if os.path.exists(sal + '/aceptacion.json') else None
        if not ac or not ac['pass_'] or ac['eval_sha'] != eval_sha(): terminales(); fin_('INSUFFICIENT: aceptacion sobre quemados no pasada/obsoleta (correr --aceptacion); los dias se acumulan sin evaluarse')
    cand = sorted(os.path.basename(f)[3:13] for f in glob.glob(TX + 'RT_2026-*.pkl') if os.path.exists(RTD + os.path.basename(f)))
    cand = [d for d in cand if a.desde <= d <= Q.TOPE]; vz = {}   # ADDENDUM4: un dia posterior al tope nunca entra
    for d in cand: vz[d] = {'valido': True, 'motivo': 'ensayo'} if a.ensayo else dia_valido(d)
    dias = [d for d in cand if vz[d]['valido']]; L.append(f'Dias candidatos {len(cand)} | validos {len(dias)}: ' + ', '.join(f'{d}{"" if vz[d]["valido"] else " NO VALIDO(" + vz[d]["motivo"] + ")"}' for d in cand))
    if not dias: terminales(); fin_('INSUFFICIENT: 0 dias validos')
    T, R, S, X, err = cargar(dias)
    if err: terminales(err); fin_('INSUFFICIENT (ERROR_DATOS: ' + '; '.join(err[:3]) + '; no cuenta ningun dia nuevo; no se escribe estado)')
    A, U, cov, cl_err = armar_base(T, R, S, X, dias, hoy, a.cl_cache)
    covd = U.groupby('dia').r1.apply(lambda x: float(x.notna().mean())); malos = [] if cl_err else [d for d in dias if covd.get(d, 0) < 0.95]   # con ERROR_DATOS de Chainlink el rasgo es NaN por falta de datos: no se declaran NO VALIDOS los dias (afecta solo al brazo PC_AS)
    if malos: L.append(f'NO VALIDOS por rasgo PC_AS <95 %: {malos}'); dias = [d for d in dias if d not in malos]; T, R, S, X, err = cargar(dias); A, U, cov, cl_err = armar_base(T, R, S, X, dias, hoy, a.cl_cache)
    if not dias: terminales(); fin_('INSUFFICIENT: 0 dias validos tras cobertura PC_AS')
    L.append(f'Cobertura rasgo PC_AS (unidades cierre-moneda NO): {cov:.3f} | G0 rellenos {len(A["G0"])} pnl {A["G0"].pnl.sum():+.2f} EV {Q.f3(Q.ev(A["G0"]))}')
    ST = json.load(open(spath)) if os.path.exists(spath) else {'arms': {}}
    if cl_err: L.append('ERROR_DATOS (Chainlink; solo afecta al brazo PC_AS): ' + '; '.join(cl_err[:3]))
    for arm in ARMS:
        if arm == 'PC_AS' and cl_err:   # fail-closed: sin rasgo no hay brazo; un terminal ya emitido se muestra (A, con EN REVISION si afecta a dias <= su fecha); no se escribe nada del brazo
            t_ = (ST['arms'].get('PC_AS') or {}).get('terminal')
            tok_, why_, _ = Q.veredicto({'terminal': t_}, cl_err, 0, 0, False, False, hoy) if t_ else ('INSUFFICIENT', 'ERROR_DATOS: ' + '; '.join(cl_err[:3]) + ' (no cuenta ningun dia nuevo; sin estado)', None)
            L.append(f'\n## PC_AS: ERROR_DATOS Chainlink\nVEREDICTO PC_AS: {tok_} ({why_})'); continue
        s = ST['arms'].setdefault(arm, {'terminal': None, 'cp': {}})
        if arm == 'PG_O50':   # dia valido para PG_O50 solo si hay Po_D Y filas PG_O50 de rt_sim (si rt_sim corrio antes que Po_D, el brazo faltaria y dPnL = -G0: falso)
            arm_dias = [d for d in dias if os.path.exists(BCO + f'Po_{d}.pkl') and (A['rt_PG_O50_BASE'].dia == d).any()]
            if len(arm_dias) < len(dias): L.append(f'PG_O50: dias sin Po_D o sin filas del brazo (no cuentan para PG_O50): {[d for d in dias if d not in arm_dias]}')
        elif arm == 'CXJ150':   # C3 exige rt_cxj150_cross.py: dia sin RX_D no cuenta para este brazo (no hay cota CROSS)
            arm_dias = [d for d in dias if os.path.exists(f'{RXD}RX_{d}.pkl')]
            if len(arm_dias) < len(dias): L.append(f'CXJ150: dias sin RX_D (rt_cxj150_cross.py; no cuentan para CXJ150): {[d for d in dias if d not in arm_dias]}')
        else: arm_dias = list(dias)
        ab, gb = (A['rt_PG_O50_BASE'], A['rt_G0_BASE']) if arm == 'PG_O50' else (A[arm], A['G0'])
        con = sorted(d for d in arm_dias if (ab.dia == d).any() or (gb.dia == d).any()); nd = len(con)   # cuenta: relleno BASE del brazo o de G0
        L.append(f'\n## {arm}: dias que cuentan nd_validos={nd} (validos {len(arm_dias)}); G0 {len(gb[gb.dia.isin(con)])} rellenos, brazo {len(ab[ab.dia.isin(con)])}')
        if not s['terminal']:
            for cp in (10, 20):
                if nd >= cp and str(cp) not in s['cp']:
                    plc = None
                    if arm == 'CXJ150':   # el placebo se calcula EN el checkpoint (prereg): sin el no se congela ni se evalua
                        pf = f'{sal}/placebo_cxj150_cp{cp}.json'; plc = json.load(open(pf)) if os.path.exists(pf) else None
                        if not plc or sorted(plc.get('dias', [])) != con[:cp]:
                            L.append(f'  PENDIENTE checkpoint {cp} de CXJ150: falta placebo (99 semillas) para los dias {",".join(con[:cp])}. Ejecutar: nice -n 19 ionice -c3 python3 -I placebo_cxj150.py cp {cp} {",".join(con[:cp])}'); break
                    res = checkpoint(arm, A, con[:cp], cp, U, plc); s['cp'][str(cp)] = res; r5 = res['dpnl']; fuerte, fdet = refuta_fuerte(res)
                    if cp == 10 and arm != 'PG_O50' and fuerte: s['terminal'] = dict(veredicto='REFUTA', fecha=hoy, nd=nd, cp=cp, motivo=fdet)   # fila C (PG_O50 no se declara fallido antes del checkpoint 20)
                    elif cp == 20:
                        if res['candidato']: s['terminal'] = dict(veredicto='CANDIDATO', fecha=hoy, nd=nd, cp=cp)   # fila D
                        elif not (r5['tot'] == r5['tot']) or r5['ncierres'] < 3: s['terminal'] = dict(veredicto='CERRADO_INSUFFICIENT', fecha=hoy, nd=nd, cp=cp, motivo='dPnL BASE NaN o <3 cierres en el checkpoint 20')   # fila E
                        else: s['terminal'] = dict(veredicto='REFUTED', fecha=hoy, nd=nd, cp=cp, motivo=('REFUTA fuerte: ' + fdet) if fuerte else motivo_refuted(res))   # fila F
                    if s['terminal']: break
            if not s['terminal'] and hoy >= Q.EJEC_CIERRE and nd < 20: s['terminal'] = dict(veredicto='CERRADO_INSUFFICIENT', fecha=hoy, nd=nd, cp=None, motivo='fila G: ejecucion >= 2027-01-01 con nd<20')   # ADDENDUM4 fila G
        tok = s['terminal']['veredicto'] if s['terminal'] else ('INSUFFICIENT' if nd <= 2 else ('EN_CURSO (checkpoint 10 evaluado)' if s['cp'] else 'EN_CURSO' if nd < 10 else 'EN_CURSO (checkpoint pendiente)'))
        L.append(f'VEREDICTO {arm}: {tok}' + (f' (terminal desde {s["terminal"]["fecha"]}, cp={s["terminal"]["cp"]}{"; " + s["terminal"]["motivo"] if s["terminal"].get("motivo") else ""})' if s['terminal'] else f' (nd={nd}; checkpoints evaluados: {sorted(s["cp"])})'))
        for k_, res in sorted(s['cp'].items()):
            L.append(f'  [checkpoint {k_}] {res["label"]} | dPnL BASE {res["dpnl"]["tot"]:+.2f} EUR IC90c ({Q.f3(res["dpnl"]["ic_c"][0])},{Q.f3(res["dpnl"]["ic_c"][1])}) IC90d inf {Q.f3(res["dpnl"]["ic_d"][0])} | CROSS {Q.f3(res["cross"])} | EV abs {Q.f3(res["ev"]["ev"])} n={res["n_arm"]}')
            L += [f'     - [{"x" if v else " "}] {c_}' for c_, v in res['conds'].items()]
            if k_ == '20': L.append('  ' + promocion(arm, res, tok))
        # descriptivo diario (no decide)
        d_ = stats_dpnl(ab[ab.dia.isin(con)], gb[gb.dia.isin(con)], con) if nd else None
        if d_: L.append(f'  [descriptivo acumulado] dPnL BASE {d_["tot"]:+.2f} cierres {d_["ncierres"]} IC90c ({Q.f3(d_["ic_c"][0])},{Q.f3(d_["ic_c"][1])}) sin2dias {Q.f3(d_["sin2dias"])} | por dia: ' + ' '.join(f'{k}:{v:+.1f}' for k, v in d_['dias'].items()))
        if nd:
            L.append('  [cotas dPnL] ' + ' '.join(f'{f}={float(dser(A[f"rt_{arm}_{f}"][A[f"rt_{arm}_{f}"].dia.isin(con)], A[f"rt_G0_{f}"][A[f"rt_G0_{f}"].dia.isin(con)]).sum()):+.1f}' for f in (('BASE', 'CROSS') if arm == 'CXJ150' else FV)))
    sec = []
    for v in ('NJ3A', 'CXJ1000', 'GEO6NJ3', 'CXB150', 'CXB300', 'CXB1000', 'CXB3000'): sec.append(f'{v}={float(dser(A[v], A["G0"]).sum()):+.1f}')
    pg, g6 = A['rt_PG_O50_BASE'], A['rt_GEO6_BASE']; sec.append(f'PG_O50-GEO6={float(dser(pg, g6).sum()):+.1f}' if len(pg) else 'PG_O50-GEO6=n/d')
    L.append('\n[secundarios descriptivos dPnL BASE vs G0, todos los dias validos; no deciden] ' + ' '.join(sec) + ' | GEO6+CXJ150: no disponible (requiere simulacion nueva)')
    L.append('NOTA: CXJ150 bajo BASE/CROSS = redteam/rt_cxj150_cross.py (script nuevo, sha propio, rt_sim.py/passT.py sin tocar); dia sin RX_D no cuenta para CXJ150.')
    atomic(spath, json.dumps(ST, indent=1, default=float)); fin_('FIN')
# ---------------- produccion por dia ----------------
def puntuar(d):
    """Po_D (p_OWN del modelo congelado) + entrada C2o_thr.json[d] con el umbral FIJO del modelo. Reutiliza c1own de entrenar_own.py por extraccion AST (sin copiar logica)."""
    import pickle; bad = check_shas()
    if bad: raise SystemExit('ERROR_DATOS sha: ' + '; '.join(bad))
    src = open(HERE + 'forward_pg/entrenar_own.py').read(); tree = ast.parse(src); idx = next(i for i, n in enumerate(tree.body) if isinstance(n, ast.FunctionDef) and n.name == 'c1own')
    ns = {'__file__': HERE + 'forward_pg/entrenar_own.py', '__name__': 'entrenar_own_import'}; exec(compile(ast.Module(tree.body[:idx + 1], []), 'entrenar_own_AST', 'exec'), ns)
    M = pickle.load(open(HERE + 'forward_pg/modelo_own.pkl', 'rb')); meta = json.load(open(HERE + 'forward_pg/modelo_own.json')); C = ns['c1own'](d)
    p = M.predict_proba(C[['T', 'L', 'bidL', 'act_i', 'lado_i']])[:, 1].astype(np.float32)
    Po = pd.DataFrame({'k': C.k.values, 'L': C.L.values, 't': C.t.values, 'p_OWN': p}); Po.to_pickle(BCO + f'Po_{d}.pkl.tmp'); os.replace(BCO + f'Po_{d}.pkl.tmp', BCO + f'Po_{d}.pkl')
    tj = BCO + 'C2o_thr.json'; J = json.load(open(tj))
    if d not in J: J[d] = {'OWN': {'0.5': float(meta['umbral_c05'])}}; atomic(tj, json.dumps(J))
    print('Po', d, len(Po), 'umbral', J[d]['OWN']['0.5'])
def producir(d):
    h = dt.datetime.now(dt.timezone.utc); m = h.hour * 60 + h.minute
    if 360 <= m < 555: raise SystemExit('BLOQUEADO: no se lanza trabajo pesado entre 06:00 y 09:15Z')
    cmds = [f'python3 -I {HERE}eval_thru1.py --puntuar {d}', f'cd {HERE}toxicidad_thru1 && python3 -I passT.py {d}', f'cd {HERE}redteam && python3 -I rt_sim.py {d}', f'cd {HERE}redteam && python3 -I rt_cxj150_cross.py {d}']
    for c in cmds:
        r = subprocess.run(['nice', '-n', '19', 'ionice', '-c3', 'bash', '-c', f'ulimit -v 3000000; export OMP_NUM_THREADS=1; {c}'])
        if r.returncode: raise SystemExit(f'FALLO ({r.returncode}): {c}')
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--aceptacion', action='store_true'); ap.add_argument('--evaluar', action='store_true'); ap.add_argument('--producir'); ap.add_argument('--puntuar')
    ap.add_argument('--cl-cache', default=Q.CL_CACHE); ap.add_argument('--desde', default=FWD_DESDE); ap.add_argument('--salida', default=HERE + 'thru1_fwd'); ap.add_argument('--hoy'); ap.add_argument('--ensayo', action='store_true', help='sin validez de dia ni aceptacion (solo ensayo sobre quemados)')
    a = ap.parse_args()
    if a.aceptacion:
        r = aceptacion(a.salida); print(json.dumps(r, indent=1, default=float)); sys.exit(0 if r['pass_'] else 2)
    elif a.evaluar: evaluar(a)
    elif a.producir: producir(a.producir)
    elif a.puntuar: puntuar(a.puntuar)
    else: ap.print_help()
