#!/usr/bin/env python3
"""E3 (ADDENDUM1 §3 E3): reglas de cancelacion sobre los FILLS REALES de B (sello tm3) con el timing de cancelacion SIMULADO.
CXB60: disparo = bid == L con otros <= 0,011 con la orden propia dentro (replica vectorizada de l_real_11nov/bid_sin_nosotros.bid_otros: ventana de inclusion cierta ex > t_ack+5 y ex < fin+30; estado invalido = szb < restante - eps = no dispara);
F5C (por eventos): no postear si F5 (estado q con rx <= t_dec de la orden) es alto en la colocacion y cancelar en la 1a fila q con F5 > C1 tras el ack; F5A-rejilla = F5C + 250 ms; UNION = CXB60 u F5C.
Un fill se EVITA si t_trig_rx <= tm3 + delta - l_ef - d_proc (o no-post). l_ef en {35,60,100,150} ms y mixtura kappa*RTT (CDF empirica del ledger).  Multiplicidad: K_B = 6 (CXB60/F5C/UNION x l_ef 35,60; alfa 0,0083); el resto es descriptivo.
Entradas: ordenes_b.csv (3.796), exp1/B_fills_v3.pkl (215 fills con tm3), cache/bqall_D.csv.gz (e3_extrae.py). Salida E3_reglas.{txt,json} (smoke: --smoke -> un dia, salida smoke_). Solo lectura; nice 19."""
import os, sys; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib1 import *
SMOKE = '--smoke' in sys.argv; PRE = 'smoke_' if SMOKE else ''
TOL = 1e-6; EPS = 0.011; T_CLK = 5; T_EFF_MIN = 30; GRID_EXTRA = 250; DPROC = 3; FLOOR_R1 = 39.5
O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}); M = pd.read_pickle(EXP + 'B_fills_v3.pkl').reset_index(drop=True)
DIAS = ['2026-10-20'] if SMOKE else ['2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23']
O = O[O.dia.isin(DIAS)].reset_index(drop=True); M = M[M.dia.isin(DIAS)].reset_index(drop=True)
assert M.oid.isin(O.oid).all() and M.tm3.notna().all() and (SMOKE or len(M) == 215), 'C1/C7: fills sin orden o sin tm3'
assert (M.epoca == 'R1').all(), 'B real debe ser 100 % R1'
rtt = ((O.t_fuera - O.t_cancel_int) * 1000.0).dropna().values; rtt = rtt[(rtt > 0) & (rtt < 20000)]; LS_ = {k: np.sort(k * rtt) for k in (0.5, 0.6, 1.0)}
def carga_bq(d):
    df = pd.read_csv(CACHE + f'bqall_{d}.csv.gz', header=None, names=['ex', 'tok', 'bid', 'ask', 'szb', 'sza', 'rx'], na_values=['None'], on_bad_lines='skip',
                     dtype={'ex': np.int64, 'tok': str, 'bid': np.float32, 'ask': np.float32, 'szb': np.float32, 'sza': np.float32, 'rx': np.int64})
    cod, cats = pd.factorize(df.tok); o = np.lexsort((df.ex.values, df.rx.values, cod)); cod = cod[o]; cut = np.flatnonzero(np.r_[True, cod[1:] != cod[:-1], True]); A = {c: df[c].values[o] for c in ('ex', 'rx', 'bid', 'ask', 'szb', 'sza')}; out = {}
    for a, b in zip(cut[:-1], cut[1:]): out[cats[cod[a]]] = {c: v[a:b] for c, v in A.items()}
    return out, len(df)
rows = []; DIAG = dict(ordenes=0, sin_q=0, sin_ventana=0, filas_vivas_bid_menor_L=0, ordenes_con_cxb=0, ordenes_con_f5=0, ordenes_nopost_f5=0, cxb_dentro_200ms_del_ack=0, filas_q=0)
for d in DIAS:
    BQ, nq = carga_bq(d); DIAG['filas_q'] += nq
    for o in O[O.dia == d].itertuples():
        DIAG['ordenes'] += 1; q = BQ.get(o.tok); fl = M[M.oid == o.oid].sort_values('tm3')
        L = float(o.precio); size = float(o.size); t_ack = int((o.t_call0 + o.post_ms / 1000.0) * 1000); t_dec_ms = int(o.t_dec * 1000)
        tcs = int(o.t_cancel_int * 1000) if o.t_cancel_int == o.t_cancel_int else None
        hi = (tcs + T_EFF_MIN) if tcs is not None else ((int(fl.tm3.max()) + 50) if len(fl) else (int(o.t_fin * 1000) + 50))
        r = dict(oid=o.oid, dia=d, L=L, size=size, t_cxb=np.nan, t_f5=np.nan, nopost=False, fin_ms=(tcs if tcs is not None else hi))
        if q is None: DIAG['sin_q'] += 1; rows.append(r); continue
        ex, rx, bid, ask, szb, sza = (q[c] for c in ('ex', 'rx', 'bid', 'ask', 'szb', 'sza')); bid = bid.astype(float)
        i = np.searchsorted(rx, t_dec_ms, 'right') - 1                           # no-post: estado q con rx <= t_dec de la orden (antiguedad <= 30 s; banda del extractor)
        if i >= 0 and t_dec_ms - rx[i] <= 30000 and 0.03 <= bid[i] <= 0.45 and np.isfinite(ask[i]) and np.isfinite(sza[i]) and bid[i] < ask[i]: r['nopost'] = bool(np.log1p(float(sza[i])) > C1)
        DIAG['ordenes_nopost_f5'] += int(r['nopost'])
        w = np.flatnonzero((ex > t_ack + T_CLK) & (ex < hi))
        if len(w) == 0: DIAG['sin_ventana'] += 1; rows.append(r); continue
        ex_w, rx_w, b_w, a_w, sb_w, sa_w = ex[w], rx[w], bid[w], ask[w].astype(float), szb[w].astype(float), sza[w].astype(float)
        matched = np.r_[0.0, np.cumsum(fl['size'].values)][np.searchsorted(fl.tm3.values, ex_w, 'left')] if len(fl) else np.zeros(len(w))      # tamano propio ya rellenado (fills con tm3 < ex de la fila)
        rem = size - matched; viva = rem > 1e-9
        DIAG['filas_vivas_bid_menor_L'] += int((viva & (b_w < L - TOL)).sum())
        fire = viva & (np.abs(b_w - L) < TOL) & ((sb_w - rem) <= EPS) & (sb_w >= rem - EPS)
        if fire.any(): j = np.flatnonzero(fire); j = j[np.argmin(rx_w[j])]; r['t_cxb'] = float(rx_w[j]); DIAG['ordenes_con_cxb'] += 1; DIAG['cxb_dentro_200ms_del_ack'] += int(rx_w[j] - t_ack <= 200)
        alto = viva & np.isfinite(a_w) & np.isfinite(sa_w) & (b_w >= 0.03) & (b_w <= 0.45) & (b_w < a_w) & (np.log1p(np.where(np.isfinite(sa_w), sa_w, 0.0)) > C1)
        if alto.any(): r['t_f5'] = float(rx_w[alto].min()); DIAG['ordenes_con_f5'] += 1
        rows.append(r)
R = pd.DataFrame(rows); Rs = R.set_index('oid'); F = M.merge(R[['oid', 't_cxb', 't_f5', 'nopost', 'fin_ms']], on='oid', how='left', validate='many_to_one'); assert len(F) == len(M)
txt = [f'# E3 reglas de cancelacion sobre fills reales de B (sello tm3; timing de cancelacion SIMULADO; ADDENDUM1 sha {ADD_SHA[:8]})' + (' [SMOKE: solo 20-Oct]' if SMOKE else ''), f'Diagnostico de disparos (ordenes): {DIAG}',
       f'RTT de cancelacion del ledger: n={len(rtt)} p50/p90/p95/p99 = {np.percentile(rtt, [50, 90, 95, 99]).round(1).tolist()} ms | l_ef (kappa=0,6) p50/p90/p99 = {np.percentile(LS_[0.6], [50, 90, 99]).round(1).tolist()} ms',
       f'Fills: {len(F)} | con disparo CXB previo a su fill (cualquier latencia): {int((F.t_cxb < F.tm3).sum())} | con F5-alto previo a su fill: {int((F.t_f5 < F.tm3).sum())} | de ordenes no-post por F5: {int(F.nopost.sum())}']
J = L2 + 'l_real_11nov/out/bid_sin_nosotros.json'                          # validacion cruzada de mi replica vectorizada de bid_otros contra la funcion validada (ordenes SIN relleno con cancelacion propia)
if os.path.exists(J) and not SMOKE:
    ref = int(json.load(open(J))['ordenes_con_disparo']); mir = O[(O.acc_llena == 0) & O.t_cancel_int.notna() & O.t_fuera.notna()].oid; mine = int(R[R.oid.isin(mir)].t_cxb.notna().sum()); dif = abs(mine - ref) / max(ref, 1)
    txt.append(f"VALIDACION de la replica vectorizada de bid_otros: ordenes sin relleno con disparo CXB: {mine} (mia) vs {ref} (l_real_11nov/out/bid_sin_nosotros.json, funcion validada) -> diferencia {100 * dif:.1f} % " + ('OK (<= 3 %)' if dif <= 0.03 else '*** REPLICA NO COINCIDE (> 3 %): los resultados CXB60 de E3 quedan EXPLORATORIOS/NO VALIDADOS ***')); DIAG['replica_cxb_dif'] = float(dif)
cl = F.cierre.values; ucl, icl = np.unique(cl, return_inverse=True); pn, co = F.pnl.values.astype(float), F.coste.values.astype(float)
def evalua(wv, boot=True, B=1000, seed=20261115, placebo=False):
    pa, ca = pn * wv, co * wv; evall = pn.sum() / co.sum(); evk = (pn.sum() - pa.sum()) / max(co.sum() - ca.sum(), 1e-9)
    o = dict(n_evit=float(wv.sum()), pnl_evit=float(pa.sum()), coste_evit=float(ca.sum()), ev_evit=float(pa.sum() / ca.sum()) if ca.sum() > 0 else np.nan, ev_kept=float(evk), dPnL=float(-pa.sum()), dEV=float(evk - evall))
    day = pd.Series(-pa).groupby(F.dia.values).sum(); o['dias_pos'] = int((day > 0).sum()); o['n_dias'] = int(len(day)); o['dPnL_sin_mejor_dia'] = float(day.sum() - day.max()); o['dPnL_dia'] = day.round(2).to_dict()
    if boot:
        rng = np.random.default_rng(seed); S = np.c_[np.bincount(icl, pn), np.bincount(icl, co), np.bincount(icl, pa), np.bincount(icl, ca)]; n = len(S); dE = np.empty(B); dP = np.empty(B)
        for b in range(B): s = S[rng.integers(0, n, n)].sum(0); dE[b] = (s[0] - s[2]) / max(s[1] - s[3], 1e-9) - s[0] / s[1]; dP[b] = -s[2]
        o['dEV_ic90'] = np.percentile(dE, [5, 95]).round(4).tolist(); o['dPnL_ic90'] = np.percentile(dP, [5, 95]).round(2).tolist()
    if placebo and wv.sum() > 0:
        rng = np.random.default_rng(seed + 1); st = pd.factorize(F.dia.astype(str) + F.coin.astype(str))[0]; idx = {s: np.flatnonzero(st == s) for s in np.unique(st)}; kk = {s: int(round(wv[idx[s]].sum())) for s in idx}; e = np.empty(B)
        for b in range(B):
            w2 = np.zeros(len(wv))
            for s, k in kk.items():
                if k > 0: w2[rng.choice(idx[s], min(k, len(idx[s])), replace=False)] = 1
            e[b] = (pn.sum() - (pn * w2).sum()) / max(co.sum() - (co * w2).sum(), 1e-9)
        o['placebo_p_EVkept'] = float((e >= evk - 1e-12).mean()); o['placebo_media_EVkept'] = float(e.mean())
    return o
def pesos(regla, l, dm=0, dp=DPROC, mix=None):
    """Peso de evitacion por fill. mix=kappa -> fraccional con la CDF empirica de kappa*RTT; si no, binario con l_ef fijo. dm: 0, 'm' (-suelo), 'p' (+suelo) o numero de ms (proyeccion R2-equivalente)."""
    dsh = 0.0 if dm == 0 else (-FLOOR_R1 if dm == 'm' else (FLOOR_R1 if dm == 'p' else float(dm)))
    t = {'CXB60': F.t_cxb.values, 'F5C': F.t_f5.values, 'F5A': F.t_f5.values + GRID_EXTRA, 'UNION': np.fmin(F.t_cxb.values, F.t_f5.values)}[regla]; npst = F.nopost.values & (regla != 'CXB60')
    slack = F.tm3.values + dsh - dp - t
    if mix is None: w = (np.isfinite(t) & (slack >= l)).astype(float)
    else: w = np.where(np.isfinite(t) & (slack >= 0), np.searchsorted(LS_[mix], np.nan_to_num(slack, nan=-1.0), 'right') / len(LS_[mix]), 0.0)
    return np.where(npst, 1.0, w)
RES = {}; REGLAS = ('CXB60', 'F5C', 'F5A', 'UNION'); evall = pn.sum() / co.sum()
txt += ['', f'Base (todos los fills): EV pond. {evall:+.4f}; PnL {pn.sum():+.2f} EUR sobre {co.sum():.2f} EUR; {len(F)} fills; {F.oid.nunique()} ordenes con fill; {len(DIAS)} dias; 100 % R1',
        '', '# TABLA principal (delta=0, d_proc=3): regla x l_ef -> evitados, EV de lo evitado, EV retenido, dPnL (= -pnl evitado) con IC90 por cierre, dEV (retenido - todo) con IC90 por cierre, dias+, sin mejor dia, placebo (p = P(EV retenido al azar >= observado))',
        'DECISIVAS (K_B=6, alfa 0,0083): CXB60, F5C, UNION x l_ef {35,60}; el resto es descriptivo']
for rg in REGLAS:
    for l in LS:
        o = evalua(pesos(rg, l), placebo=True); RES[f'{rg}_l{l}'] = o; dec = ' [DECISIVA]' if rg in ('CXB60', 'F5C', 'UNION') and l in (35, 60) else ''
        txt.append(f"{rg} l_ef={l}{dec}: evitados {o['n_evit']:.0f} (pnl {o['pnl_evit']:+.2f}, EV evitado {o['ev_evit']:+.3f}) | retenido EV {o['ev_kept']:+.4f} | dPnL {o['dPnL']:+.2f} EUR IC90 {o['dPnL_ic90']} | dEV {o['dEV']:+.4f} IC90 {o['dEV_ic90']} | dias+ {o['dias_pos']}/{o['n_dias']} | sin mejor dia {o['dPnL_sin_mejor_dia']:+.2f} | placebo p {o.get('placebo_p_EVkept', np.nan):.3f}")
txt += ['', '# Mixtura empirica l_ef = kappa*RTT_ledger (CDF; evitado fraccional; sin placebo)']
for rg in REGLAS:
    for kap in (0.5, 0.6, 1.0):
        o = evalua(pesos(rg, 0, mix=kap)); RES[f'{rg}_mix{kap}'] = o
        txt.append(f"{rg} kappa={kap}: evitados {o['n_evit']:.1f} | retenido EV {o['ev_kept']:+.4f} | dPnL {o['dPnL']:+.2f} EUR IC90 {o['dPnL_ic90']} | dEV {o['dEV']:+.4f} IC90 {o['dEV_ic90']} | dias+ {o['dias_pos']}/{o['n_dias']}")
txt += ['', '# Sensibilidades DESCRIPTIVAS (no deciden): d_proc 10/30, delta -suelo/+suelo (39,5 ms; +suelo NO decide), proyeccion R2-equivalente (+20,5 ms de holgura de deteccion: SIMULADA)']
for rg in ('CXB60', 'F5C', 'UNION'):
    for l in (35, 60):
        for et, kw in (('d_proc=10', dict(dp=10)), ('d_proc=30', dict(dp=30)), ('delta=-suelo', dict(dm='m')), ('delta=+suelo (no decide)', dict(dm='p')), ('R2-equivalente (+20,5 ms; SIMULADA)', dict(dm=20.5))):
            o = evalua(pesos(rg, l, **kw), boot=False); RES[f'{rg}_l{l}_{et}'] = o; txt.append(f"{rg} l_ef={l} {et}: evitados {o['n_evit']:.0f} | EV retenido {o['ev_kept']:+.4f} | dPnL {o['dPnL']:+.2f} | dEV {o['dEV']:+.4f}")
g35, g100 = RES['F5C_l35']['dPnL'], RES['F5C_l100']['dPnL']; txt += ['', f'H-F5-LAT: dPnL F5C l_ef=35 {g35:+.2f} EUR -> l_ef=100 {g100:+.2f} EUR (perdida {g35 - g100:+.2f} EUR; el motor da -0,086/EUR por +40 ms para CXB)']
for rg in ('CXB60', 'F5C', 'UNION'):
    w = pesos(rg, 60); tab = pd.DataFrame({'rama': F.rama.values, 'evit': w, 'pnl': pn, 'pnl_evit': pn * w}).groupby('rama').agg(fills=('pnl', 'size'), evitados=('evit', 'sum'), pnl=('pnl', 'sum'), pnl_evitado=('pnl_evit', 'sum'))
    txt += ['', f'{rg} l_ef=60 por rama del sello (sig/amb/nosig/sinev/guard):', tab.round(2).to_string()]
sg = (F.rama.values == 'sig'); txt += ['', f'# Sensibilidad SOLO rama sig ({int(sg.sum())} fills; el sello sig es el mas preciso): dEV = EV retenido - EV de todos los sig; l_ef 35/60']
for rg in ('CXB60', 'F5C', 'UNION'):
    for l in (35, 60):
        w = pesos(rg, l)[sg]; p_, c_ = pn[sg], co[sg]; ea = p_.sum() / c_.sum(); ek = (p_.sum() - (p_ * w).sum()) / max(c_.sum() - (c_ * w).sum(), 1e-9); RES[f'sig_{rg}_l{l}'] = dict(n_evit=float(w.sum()), ev_todos=float(ea), ev_kept=float(ek), dEV=float(ek - ea), dPnL=float(-(p_ * w).sum()))
        txt.append(f"{rg} l_ef={l} solo sig: evitados {w.sum():.0f} | EV de todos los sig {ea:+.4f} | EV retenido {ek:+.4f} | dEV {ek - ea:+.4f} | dPnL {-(p_ * w).sum():+.2f} EUR")
# ---------------- C8: incondicional por orden (4 dias): denominador = size*precio de las ordenes COLOCADAS (todas menos no-post); P(fill) y pnl por EUR potencial
O['exp'] = O['size'] * O.precio; O['pnl'] = O.pnl.fillna(0.0).astype(float); O['coste'] = O.coste.fillna(0.0).astype(float); O['filled'] = O['fill'].astype(bool); assert O.exp.sum() >= O.coste.sum() - 1e-9, 'C8: coste potencial < coste relleno'
txt += ['', f'# C8 incondicional por orden ({len(O)} ordenes; coste potencial {O.exp.sum():.1f} EUR >= coste relleno {O.coste.sum():.1f} EUR). Base: P(fill) {O.filled.mean():.4f}; EV|fill {O.pnl.sum() / max(O.coste.sum(), 1e-9):+.4f}; pnl / exposicion potencial {O.pnl.sum() / O.exp.sum():+.5f}']
npost = O.oid.map(Rs.nopost).fillna(False).astype(bool).values
for rg in ('CXB60', 'F5C', 'UNION'):
    for l in (35, 60):
        w = pesos(rg, l); k = 1 - w; pk = pd.Series(pn * k).groupby(F.oid.values).sum(); ck = pd.Series(co * k).groupby(F.oid.values).sum(); pk_o = O.oid.map(pk).fillna(0.0).values; ck_o = O.oid.map(ck).fillna(0.0).values
        placed = ~npost if rg != 'CXB60' else np.ones(len(O), bool); fk = (ck_o > 1e-9) & placed
        RES[f'incond_{rg}_l{l}'] = dict(placed=int(placed.sum()), pnl_retenido=float(pk_o[placed].sum()), exp_colocadas=float(O.exp.values[placed].sum()), p_fill=float(fk.sum() / max(placed.sum(), 1)), ev_fill=float(pk_o[placed].sum() / max(ck_o[placed].sum(), 1e-9)))
        r_ = RES[f'incond_{rg}_l{l}']; txt.append(f"{rg} l_ef={l}: colocadas {r_['placed']}/{len(O)} | P(fill) {r_['p_fill']:.4f} | EV|fill {r_['ev_fill']:+.4f} | pnl retenido {r_['pnl_retenido']:+.2f} EUR | pnl / exposicion potencial colocada {r_['pnl_retenido'] / r_['exp_colocadas']:+.5f} (base {O.pnl.sum() / O.exp.sum():+.5f})")
txt += ['', 'LECTURA: CXB60/F5C evitan fills por reglas con timing de cancelacion simulado (MEDIDO sobre fills reales tm3, SIMULADO en la latencia); no hay ancla independiente del reloj de relleno propio; 202 unidades / 4 dias / R1: potencia baja (IC90 por cierre arriba).']
write(EXP + PRE + 'E3_reglas.txt', txt); json.dump(dict(RES=RES, DIAG=DIAG, base=dict(ev=float(evall), pnl=float(pn.sum()), coste=float(co.sum()))), open(EXP + PRE + 'E3_reglas.json', 'w'), default=float, indent=1)
if not SMOKE: estado_fase('E3', 'COMPLETE', fills=len(F), ordenes=len(O))
print('\n'.join(txt))
