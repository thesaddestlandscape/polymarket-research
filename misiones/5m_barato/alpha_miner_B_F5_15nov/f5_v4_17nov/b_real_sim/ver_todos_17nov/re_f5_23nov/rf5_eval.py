#!/usr/bin/env python3
"""rf5_eval.py -- evaluador de RF5E-COMB-23NOV-v1 (prereg 16be06b6). LEE rf5_cortes.json (nunca recalcula cortes) y SOLO dias VALIDOS (manifest COMPLETE, criterio (iv) ok, (iii) suelo OK).
REGLA DE MIRADA (prereg sec.7): con < MIN_DIAS_MIRADA1 dias validos escribe SOLO conteos y cobertura; NUNCA calcula ni escribe EV/PnL. Con >=10 calcula Delta_k (familia A) y EV (familia K) con IC90 por dias y por cierre.
Implementado: Delta_k = (PnL regla - PnL base)/coste base agregado por dias; T_k y p_max por permutacion de F5_0 dentro de dia x moneda (K=2000, semilla 20261124, mismas permutaciones para las 4 reglas); inversion; veto al azar;
% dias>0; sin 2 mejores dias; bloq1; test de fuga F5 (AUC invalido/antiguo vs desenlace); EV/incondicional/L_cancel/inversion y ablacion+LOO de la familia K.
NO implementado (declarado, impide CONFIRMADA/COMBINADA_EV_POSITIVO): sensibilidad fail-closed por huecos de stream (ESPEC_GRABADOR_CONEXION_23nov) y nulo de K con desplazamiento circular de series V5/V6 (p_max_K). 0 ordenes, 0 red.
Uso: python3 rf5_eval.py [--dir out_rf5_ciego/] -> escribe rf5_resumen.json (+ imprime)."""
import os, sys, json, glob
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, HV)
import rf5_core as K5
MIN_DIAS = 10; SEMILLA = 20261124; K_PERM = 2000

def dias_validos(estado):
    """estado = {dia: manifest-resumen}. VALIDO <=> COMPLETE y criterio_iv_ok True y criterio_iii == 'OK' (tabla de suelo sucesora firmada)."""
    return sorted(d for d, m in estado.items() if m.get('status') == 'COMPLETE' and m.get('iv') is True and m.get('iii') == 'OK')

def carga(out, dias):
    A = [pd.read_pickle(out + f'rf5A_{d}.pkl') for d in dias]; K = [pd.read_pickle(out + f'rf5K_{d}.pkl') for d in dias if os.path.exists(out + f'rf5K_{d}.pkl')]
    F = [pd.read_pickle(out + f'rf5_f5_0_{d}.pkl') for d in dias]
    return pd.concat(A + K, ignore_index=True), pd.concat(F, ignore_index=True)

def conteos(R, F):
    """Solo conteos/cobertura (SIN pnl, SIN coste, SIN EV)."""
    por = R.groupby(['dia', 'bloq', 'pol']).agg(ordenes=('mid', 'size'), rellenos=('q', lambda s: int((s > 0).sum())), lados=('mid', lambda s: 0)).reset_index().drop(columns='lados')
    f5 = F[(F.bloq == 0)].groupby(['dia', 'coin']).agg(lados=('mid', 'size'), f5_invalidos=('f5_0', lambda s: int((~np.isfinite(s.astype(float))).sum()))).reset_index()
    return dict(politicas_por_dia=por.to_dict('records'), f5_0_por_dia_moneda=f5.to_dict('records'))

# ------------------------------------------------------------------ unidades y deltas
def unidades(R, pol, bloq=0):
    X = R[(R.pol == pol) & (R.bloq == bloq)]
    if not len(X): return pd.DataFrame(columns=['dia', 'mid', 'k', 'fin', 'coin', 'pnl', 'cost', 'altas', 'lado'])
    f = X.assign(pnl=X.pnl.where(X.q > 0, 0.0).fillna(0.0), cost=X.cost.where(X.q > 0, 0.0).fillna(0.0))
    return f.groupby(['dia', 'mid', 'k'], as_index=False).agg(fin=('fin', 'first'), coin=('coin', 'first'), pnl=('pnl', 'sum'), cost=('cost', 'sum'), lado=('lado', 'first')).assign(altas=1)

def deltas(R, pol, por='dia', bloq=0, base='base'):
    """filas por bloque (dia | fin): dpnl = PnL(pol) - PnL(base); cost_base."""
    U = unidades(R, pol, bloq); B = unidades(R, base, bloq)
    M = B.merge(U, on=['dia', 'mid', 'k'], how='outer', suffixes=('_b', '_p')); M[['pnl_b', 'pnl_p', 'cost_b']] = M[['pnl_b', 'pnl_p', 'cost_b']].fillna(0.0)
    M['fin'] = M.fin_b.fillna(M.fin_p); M['dpnl'] = M.pnl_p - M.pnl_b
    return M.groupby(por, as_index=False).agg(dpnl=('dpnl', 'sum'), cost=('cost_b', 'sum'))

def ic90(num, den, K=10000, seed=SEMILLA):
    """bootstrap de BLOQUES (dias o cierres) del cociente sum(num)/sum(den): (punto, lo, hi)."""
    num = np.asarray(num, float); den = np.asarray(den, float); n = len(num)
    if n < 2 or den.sum() <= 0: return (float('nan'),) * 3
    rng = np.random.default_rng(seed); idx = rng.integers(0, n, (K, n)); r = num[idx].sum(1) / np.maximum(den[idx].sum(1), 1e-12)
    return float(num.sum() / den.sum()), float(np.percentile(r, 5)), float(np.percentile(r, 95))

def sin_mejores(num, den, n_out=2):
    num = np.asarray(num, float); den = np.asarray(den, float); o = np.argsort(-num)[n_out:]
    return float(num[o].sum() / den[o].sum()) if den[o].sum() > 0 else float('nan')

# ------------------------------------------------------------------ familia A
def _masks(f5, coin_idx, c, coins):
    p20 = np.array([c['F2_p20'][k] for k in coins])[coin_idx]; p80 = np.array([c['F3_p80'][k] for k in coins])[coin_idx]; inv = ~np.isfinite(f5); f = np.where(inv, np.inf, f5)
    m1 = inv | (f >= c['C1']); m2 = inv | ~(f < p20); m3 = inv | (f >= p80)
    return {'F1': m1, 'F2': m2, 'F3': m3, 'U13': m1 | m3}

def familia_A(R, F, c, K=K_PERM, seed=SEMILLA):
    """Delta_k por regla con IC90 dias/cierre, % dias>0, sin 2 mejores, inversion, azar y p_max (permutacion de F5_0 dentro de dia x moneda)."""
    Ub = unidades(R, 'base', 0); f5 = F[(F.bloq == 0) & (F.pol == 'base')][['dia', 'mid', 'k', 'coin', 'f5_0']]
    L = f5.merge(Ub[['dia', 'mid', 'k', 'pnl', 'cost']], on=['dia', 'mid', 'k'], how='left').fillna({'pnl': 0.0, 'cost': 0.0}); L = L.sort_values(['dia', 'coin', 'mid', 'k']).reset_index(drop=True)
    coins = sorted(L.coin.unique()); ci = L.coin.map({k: i for i, k in enumerate(coins)}).values; dias = sorted(L.dia.unique()); di = L.dia.map({d: i for i, d in enumerate(dias)}).values
    f = L.f5_0.values.astype(float); pnl = L.pnl.values; cost_d = np.bincount(di, L.cost.values, minlength=len(dias))
    grp = {}; [grp.setdefault((di[i], ci[i]), []).append(i) for i in range(len(L))]; G = [np.array(v) for v in grp.values()]
    def delta_dias(mask): return -np.bincount(di, np.where(mask, pnl, 0.0), minlength=len(dias)) / np.maximum(cost_d, 1e-12)
    def T(dd): return np.nan if len(dd) < 2 or np.std(dd, ddof=1) == 0 else np.mean(dd) / (np.std(dd, ddof=1) / np.sqrt(len(dd)))
    obs = _masks(f, ci, c, coins); rng = np.random.default_rng(seed); Tobs = {k: T(delta_dias(m)) for k, m in obs.items()}
    Tmax = [];
    for _ in range(K):
        fp = f.copy()
        for g in G: fp[g] = f[rng.permutation(g)]
        mm = _masks(fp, ci, c, coins); Tmax.append(np.nanmax([T(delta_dias(m)) for m in mm.values()]))
    Tmax = np.array(Tmax); out = {}; Tmx_obs = np.nanmax(list(Tobs.values())); out['T_max_obs'] = float(Tmx_obs); out['p_max_global'] = float((Tmax >= Tmx_obs).mean())
    for k, m in obs.items():
        dd = delta_dias(m); dpnl_d = dd * cost_d; pt, lo, hi = ic90(dpnl_d, cost_d, seed=seed)
        Dc = deltas(R, k, 'fin'); cierre = ic90(Dc.dpnl.values, Dc.cost.values, K=2000, seed=seed)
        ninv = []; dinv_p = 0.0
        for g in G:                                              # inversion: vetar los F5_0 MAS BAJOS validos, mismo n por dia x moneda
            n = int(m[g].sum()); fg = f[g]; v = np.where(np.isfinite(fg))[0]; o = v[np.argsort(fg[v], kind='stable')][:n]; dinv_p += pnl[g][o].sum()
        D_inv = -dinv_p / cost_d.sum()
        out[k] = dict(delta=pt, ic90_dias=[lo, hi], ic90_cierres=[cierre[1], cierre[2]], pct_dias_pos=float((dd > 0).mean()), delta_sin_2_mejores_dias=sin_mejores(dpnl_d, cost_d), delta_inversion=D_inv,
                      T=float(Tobs[k]), n_dias=len(dias), lados_vetados=int(m.sum()), lados=int(len(m)), por_dia=dict(zip(dias, map(float, dd))))
        out[k]['p_azar'] = p_azar(G, m, pnl, cost_d.sum(), -pnl[m].sum() / cost_d.sum(), K, rng)
    return out

def p_azar(G, m, pnl, cost, delta_obs, K, rng):
    """P(Delta aleatorio >= Delta observado) vetando AL AZAR el mismo n de lados por dia x moneda (prereg sec.2 d)."""
    ns = [int(m[g].sum()) for g in G]; hit = 0
    for _ in range(K):
        s = 0.0
        for g, n in zip(G, ns):
            if n: s += pnl[g][rng.permutation(len(g))[:n]].sum()
        hit += (-s / cost) >= delta_obs
    return float(hit / K)

def auc_binaria(score, y):
    """AUC de Mann-Whitney de la bandera 'F5_0 invalido' frente al desenlace y (0/1); NaN si falta una clase."""
    s = np.asarray(score, float); y = np.asarray(y, int)
    if y.min() == y.max() or s.min() == s.max(): return float('nan')
    r = pd.Series(s).rank().values; n1 = int(y.sum()); n0 = len(y) - n1
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))

def fuga_f5(R, F):
    """AUC por dia (n>=20) de 'F5_0 invalido' vs desenlace del lado; distribucion de antiguedad. 0 invalidos en todo => se exige el test unitario de la regla de 30 s (test_rf5.py)."""
    gana = R[(R.pol == 'base') & (R.bloq == 0)].groupby(['dia', 'mid', 'k']).gana.first().reset_index(); X = F[(F.bloq == 0)].merge(gana, on=['dia', 'mid', 'k'], how='left'); X['inv'] = (~np.isfinite(X.f5_0.astype(float))).astype(int); out = {}
    for d, g in X.groupby('dia'):
        g = g.dropna(subset=['gana']); out[d] = dict(n=int(len(g)), auc=(auc_binaria(g.inv, g.gana) if len(g) >= 20 else None))
    ed = X.edad_ms.astype(float).dropna()
    return dict(por_dia=out, n_invalidos=int(X.inv.sum()), n=int(len(X)), edad_ms_pctiles=({str(p): float(np.percentile(ed, p)) for p in (50, 90, 99, 100)} if len(ed) else {}),
                ok_banda=all(v['auc'] is None or (np.isnan(v['auc']) or 0.40 <= v['auc'] <= 0.60) for v in out.values()))

def veredicto_A(k, a, fuga, c, bloq1_delta_pos):
    """CONFIRMADA_k (prereg sec.3). Devuelve (veredicto, condiciones). Sensibilidad fail-closed NO implementada => nunca CONFIRMADA completa: 'CONFIRMADA_PENDIENTE_SENS'."""
    cond = dict(delta_pos=a['delta'] > 0, ic90_dias_lo_pos=a['ic90_dias'][0] > 0, ic90_cierres_lo_pos=a['ic90_cierres'][0] > 0, p_max_lt_005=a['p_max_global'] < 0.05, dias_pos_60=a['pct_dias_pos'] >= 0.60,
                sin2mejores_pos=a['delta_sin_2_mejores_dias'] > 0, mayor_que_inversion=a['delta'] > a['delta_inversion'], p_azar_le_010=a['p_azar'] <= 0.10, bloq1_pos=bool(bloq1_delta_pos), fuga_ok=bool(fuga['ok_banda']))
    cond = {x: bool(v) for x, v in cond.items()}
    if all(cond.values()): return 'CONFIRMADA_PENDIENTE_SENS_FAILCLOSED', cond
    return ('REFUTADA' if a['ic90_dias'][1] <= 0 else 'ACUMULANDO'), cond

# ------------------------------------------------------------------ familia K
def ev_pol(R, pol, bloq=0):
    U = unidades(R, pol, bloq)
    if not len(U): return None
    d = U.groupby('dia').agg(pnl=('pnl', 'sum'), cost=('cost', 'sum')).reset_index(); pt, lo, hi = ic90(d.pnl.values, d.cost.values); cc = U.groupby('fin').agg(pnl=('pnl', 'sum'), cost=('cost', 'sum')); pc = ic90(cc.pnl.values, cc.cost.values, K=2000)
    return dict(ev_eur=pt, ic90_dias=[lo, hi], ic90_cierres=[pc[1], pc[2]], ev_sin_2_mejores_dias=sin_mejores(d.pnl.values, d.cost.values), pnl_total=float(U.pnl.sum()), coste_total=float(U.cost.sum()), lados=int(len(U)),
                rellenos=int((U.cost > 0).sum()), ev_por_unidad=float(U.pnl[U.cost > 0].mean()) if (U.cost > 0).any() else float('nan'), ev_incondicional_por_alta=float(U.pnl.sum() / len(U)), p_relleno=float((U.cost > 0).mean()), eur_dia=float(U.cost.sum() / d.shape[0]), pnl_dia=float(U.pnl.sum() / d.shape[0]))

def incremento(R, a, b):
    """Delta PnL/EUR de la politica a frente a la b (b = referencia), agregado por dias con IC90 por dias."""
    D = deltas(R.assign(pol=R.pol), a, 'dia', 0, base=b); pt, lo, hi = ic90(D.dpnl.values, D.cost.values); return dict(delta=pt, ic90_dias=[lo, hi])

def frac_cancel(R, pol, bloq=0):
    """fraccion de lados con orden colocada cuya orden se cancela por la regla (motivo_fin == 'regla'). > 0,5 => 'solo no operar' (prereg sec.4: no cuenta). None si no hay columna/datos."""
    X = R[(R.pol == pol) & (R.bloq == bloq)]
    if 'motivo_fin' not in X.columns or not len(X): return None
    g = X.groupby(['dia', 'mid', 'k']).motivo_fin.apply(lambda s: bool((s == 'regla').any())); return float(g.mean())

def familia_K(R):
    out = dict(politicas={}, bloq1={}, lcancel={}, ablacion={}, loo={}, aislados={}, interaccion=None, nulo_K='PENDIENTE (desplazamiento circular V5/V6 no implementado) => sin p_max_K')
    for p in ['base', 'F3', 'F3_V6', 'F3_V5', 'V5', 'V6', 'K1', 'K2', 'K3', 'K4', 'K5', 'INV_F3', 'INV_K1']: out['politicas'][p] = ev_pol(R, p)
    for p in ('K1', 'K2', 'K3', 'K4'):
        out['bloq1'][p] = ev_pol(R, p, 1); out['lcancel'][p] = {lc: ev_pol(R, f'{p}@lc{lc}') for lc in (111, 147)}
    out['ablacion'] = dict(F3_vs_base=incremento(R, 'F3', 'base'), F3V6_vs_F3=incremento(R, 'F3_V6', 'F3'), K1_vs_F3V6=incremento(R, 'K1', 'F3_V6'))
    out['loo'] = dict(capa_F3=incremento(R, 'K1', 'K5'), capa_V5=incremento(R, 'K1', 'F3_V6'), capa_V6=incremento(R, 'K1', 'F3_V5'))
    out['aislados'] = dict(F3=incremento(R, 'F3', 'base'), V5=incremento(R, 'V5', 'base'), V6=incremento(R, 'V6', 'base'), K1_comb=incremento(R, 'K1', 'base'))
    out['frac_lados_cancelados_por_regla'] = {p: frac_cancel(R, p) for p in ('K1', 'K2', 'K3', 'K4', 'K5', 'V5', 'V6')}
    out['interaccion'] = float(sum(out['aislados'][x]['delta'] for x in ('F3', 'V5', 'V6')) - out['aislados']['K1_comb']['delta'])
    return out

def veredicto_K(k, ev, kf):
    """COMBINADA_EV_POSITIVO (prereg sec.4) incompleta: faltan p_max_K y sensibilidad fail-closed => 'EV_POSITIVO_PENDIENTE_*' como mucho."""
    p = kf['politicas'].get(k);
    if p is None: return 'SIN_DATOS', {}
    cond = dict(ev_pos=p['ev_eur'] > 0, ic90_dias_lo_pos=p['ic90_dias'][0] > 0, ic90_cierres_lo_pos=p['ic90_cierres'][0] > 0, incond_pos=p['ev_incondicional_por_alta'] > 0, sin2_pos=p['ev_sin_2_mejores_dias'] > 0,
                bloq1_pos=bool(kf['bloq1'].get(k) and kf['bloq1'][k]['ev_eur'] > 0), lc_pos=all(bool(v and v['ev_eur'] > 0) for v in kf['lcancel'].get(k, {}).values()),
                capas_loo_pos=all(v['ic90_dias'][0] > 0 for v in kf['loo'].values()), inv_menor=(k != 'K1') or bool(kf['politicas']['INV_K1'] and kf['politicas']['INV_K1']['ev_eur'] < p['ev_eur']))
    cond = {x: bool(v) for x, v in cond.items()}
    fr = (kf.get('frac_lados_cancelados_por_regla') or {}).get(k)
    if fr is not None and fr > 0.5: return 'SOLO_NO_OPERAR (>50 % de vidas disparadas; no cuenta)', dict(cond, frac_disparadas=fr)
    if all(cond.values()): return 'EV_POSITIVO_PENDIENTE_PMAXK_Y_SENS', cond
    return ('REFUTADA_COMB' if p['ic90_dias'][1] <= 0 else 'ACUMULANDO'), cond

def resumen(out, estado, c=None, min_dias=MIN_DIAS):
    c = c or K5.lee_cortes(); dv = dias_validos(estado); res = dict(measurement_id='RF5E-COMB-23NOV-v1', dias_validos=dv, n_dias_validos=len(dv), min_dias_mirada1=min_dias, estado_por_dia={d: m.get('status') for d, m in estado.items()})
    if not dv: res['modo'] = 'SOLO_CONTEOS (0 dias validos)'; return res
    R, F = carga(out, dv); res['conteos'] = conteos(R, F)
    if len(dv) < min_dias: res['modo'] = f'SOLO_CONTEOS ({len(dv)} < {min_dias} dias validos: sin EV, sin PnL, prereg sec.7)'; return res
    res['modo'] = 'MIRADA_1' if len(dv) < 20 else 'MIRADA_2'; A = familia_A(R, F, c); fu = fuga_f5(R, F)
    b1 = {k: deltas(R, k, 'dia', 1) for k in ('F1', 'F2', 'F3', 'U13')}; res['familia_A'] = {k: dict(A[k], veredicto=veredicto_A(k, dict(A[k], p_max_global=A['p_max_global']), fu, c, float(b1[k].dpnl.sum()) > 0)[0]) for k in ('F1', 'F2', 'F3', 'U13')}
    res['familia_A_global'] = dict(T_max_obs=A['T_max_obs'], p_max=A['p_max_global'], primario='F3'); res['fuga_f5'] = fu; res['familia_K'] = kf = familia_K(R)
    res['veredictos_K'] = {k: veredicto_K(k, None, kf)[0] for k in ('K1', 'K2', 'K3', 'K4')}
    return res

if __name__ == '__main__':
    import rf5_run as RR
    out = RR.OUT; est = RR.estado(); r = resumen(out, est); open(out + 'rf5_resumen.json', 'w').write(json.dumps(r, indent=1, default=str)); print(json.dumps({k: r[k] for k in ('modo', 'n_dias_validos', 'dias_validos')}, default=str))
