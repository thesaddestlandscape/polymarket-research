#!/usr/bin/env python3
"""rf5_eval.py -- evaluador de RF5E-COMB-23NOV-v1 (prereg 16be06b6). LEE rf5_cortes.json (nunca recalcula cortes) y SOLO dias VALIDOS (manifest COMPLETE, criterio (iv) ok, (iii) suelo OK).
REGLA DE MIRADA (ADENDA_RF5_INTERINA_24nov sec.2/6, SUSTITUYE prereg sec.7; rf5_fronteras.decide_mirada): con < 6 dias validos (o un dia anterior pendiente) escribe SOLO conteos y cobertura; NUNCA calcula ni escribe EV/PnL. Mirada 1 = los 6 PRIMEROS validos; final = los 10 primeros; umbrales Pocock-LD e IC t de Student por dias en rf5_fronteras. Con mirada calcula Delta_k (familia A) y EV (familia K) con IC90 por dias y por cierre.
Implementado: Delta_k = (PnL regla - PnL base)/coste base agregado por dias; T_k y p_max por permutacion de F5_0 dentro de dia x moneda (K<=1000 con parada secuencial Besag-Clifford h=20 [firma chief 23-Nov; el prereg decia 2000], semilla 20261124, mismas permutaciones para las 4 reglas); inversion; veto al azar;
% dias>0; sin 2 mejores dias; bloq1; test de fuga F5 (AUC invalido/antiguo vs desenlace); EV/incondicional/L_cancel/inversion y ablacion+LOO de la familia K.
NO implementado (declarado, impide CONFIRMADA/COMBINADA_EV_POSITIVO): sensibilidad fail-closed por huecos de stream (ESPEC_GRABADOR_CONEXION_23nov) y el p_max_K (lo calcula rf5_nulo_run.py en la mirada 1, no esta en este evaluador). 0 ordenes, 0 red.
NOTAS DE ALCANCE (adenda interina 24-Nov sec.5; no cambian ningun parametro): (1) el 23-Nov es INCOMPLETE (libro5/libro5_tx en pausa de 00 a 13:22Z => con_tx/units del dia < 0,90) y el 24-Nov lo es previsiblemente por d-1: el primer dia valido posible es el 25-Nov; (2) la tabla de suelo sucesora NO sustituye a bad_D (horas malas del dia);
(3) clase de suelo hi SIN datos ciegos (1728/1728 ventanas lo por dia): todo veredicto vale SOLO para la clase lo (hi = DATA_BLOCKED); (4) K6 se juzga aparte (rf5_k6.gate_k6 sobre rf5K6_*.pkl); (5) BTC sigue DATA_BLOCKED_BTC (solo ETH/SOL/XRP).
Uso: python3 rf5_eval.py [--dir out_rf5_ciego/] -> escribe rf5_resumen.json (+ imprime)."""
import os, sys, json, glob
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, HV)
import rf5_core as K5, rf5_nulo as NU, rf5_huecos as HU, rf5_fronteras as FR
MIN_DIAS = FR.MIRADA1_DIAS; SEMILLA = FR.SEMILLA; K_PERM = FR.K_MAX['A']      # adenda interina 24-Nov sec.6: mirada 1 = 6.o dia valido, final = 10.o; Pocock-LD; Besag-Clifford h=20 con K_max 2000 (A) / 1500 (K); semilla 20261124

def dias_validos(estado):
    """estado = {dia: manifest-resumen}. VALIDO <=> COMPLETE y criterio_iv_ok True y criterio_iii == 'OK' (tabla de suelo sucesora firmada)."""
    return sorted(d for d, m in estado.items() if m.get('status') == 'COMPLETE' and m.get('iv') is True and m.get('iii') == 'OK')

PRECINTO = HV + 'PRECINTO_CIEGOS_18nov.txt'

def precintados(path=None):
    """nombres de fichero precintados (PRECINTO_CIEGOS_18nov.txt: prohibido abrirlos). Se leen del propio registro del precinto."""
    p = path or PRECINTO
    if not os.path.exists(p): return set()
    return {os.path.basename(l.split(None, 1)[1].strip()) for l in open(p) if l.strip() and not l.startswith('#') and len(l.split()) >= 2}

def carga(out, dias, precint=None, registro=None):
    """Abre SOLO los pkl de los dias dados (ya VALIDOS). Un fichero precintado o ilegible (PermissionError) NO provoca excepcion: se registra 'precintado' en `registro` y el dia se omite entero (nunca datos parciales de un dia)."""
    precint = precintados() if precint is None else precint; registro = registro if registro is not None else []; A = []; K = []; F = []
    for d in dias:
        fa, fk, ff = f'rf5A_{d}.pkl', f'rf5K_{d}.pkl', f'rf5_f5_0_{d}.pkl'
        if fa in precint or ff in precint or fk in precint: registro.append(dict(dia=d, estado='precintado', motivo='listado en PRECINTO_CIEGOS')); continue
        try:
            a = pd.read_pickle(out + fa); f = pd.read_pickle(out + ff); k = pd.read_pickle(out + fk) if os.path.exists(out + fk) else None
        except PermissionError: registro.append(dict(dia=d, estado='precintado', motivo='sin permiso de lectura (chmod)')); continue
        A.append(a); F.append(f); (K.append(k) if k is not None else None)
    if not A: return None, None
    return pd.concat(A + K, ignore_index=True), pd.concat(F, ignore_index=True)

def sin_resolver_fuera(R):
    """(R_primaria sin mercados sin desenlace oficial, R_peor_caso con todo: los sin resolver valen pnl = -coste). Sin columna sin_res => identicas."""
    if 'sin_res' not in R.columns: return R, R
    return R[~R.sin_res.fillna(False).astype(bool)], R

def conteos(R, F):
    """Solo conteos/cobertura (SIN pnl, SIN coste, SIN EV)."""
    por = R.groupby(['dia', 'bloq', 'pol']).agg(ordenes=('mid', 'size'), rellenos=('q', lambda s: int((s > 0).sum())), lados=('mid', lambda s: 0)).reset_index().drop(columns='lados')
    f5 = F[(F.bloq == 0) & (F.pol == 'base')].groupby(['dia', 'coin']).agg(lados=('mid', 'size'), f5_invalidos=('f5_0', lambda s: int((~np.isfinite(s.astype(float))).sum()))).reset_index()
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

def ic90(num, den, K=10000, seed=SEMILLA, unil=0.05):
    """bootstrap de BLOQUES (dias o cierres) del cociente sum(num)/sum(den): (punto, lo, hi) con cola unilateral `unil` (0,05 = IC90). Por DIAS con n<10 NO se usa para decidir (rf5_fronteras.ic_t_dias); por CIERRES (bloques de 5 min) con B>=5000 y el nivel de la mirada."""
    num = np.asarray(num, float); den = np.asarray(den, float); n = len(num)
    if n < 2 or den.sum() <= 0: return (float('nan'),) * 3
    rng = np.random.default_rng(seed); idx = rng.integers(0, n, (K, n)); r = num[idx].sum(1) / np.maximum(den[idx].sum(1), 1e-12)
    return float(num.sum() / den.sum()), float(np.percentile(r, 100 * unil)), float(np.percentile(r, 100 * (1 - unil)))

def sin_mejores(num, den, n_out=2):
    num = np.asarray(num, float); den = np.asarray(den, float); o = np.argsort(-num)[n_out:]
    return float(num[o].sum() / den[o].sum()) if den[o].sum() > 0 else float('nan')

# ------------------------------------------------------------------ familia A
def _masks(f5, coin_idx, c, coins):
    p20 = np.array([c['F2_p20'][k] for k in coins])[coin_idx]; p80 = np.array([c['F3_p80'][k] for k in coins])[coin_idx]; inv = ~np.isfinite(f5); f = np.where(inv, np.inf, f5)
    m1 = inv | (f >= c['C1']); m2 = inv | ~(f < p20); m3 = inv | (f >= p80)
    return {'F1': m1, 'F2': m2, 'F3': m3, 'U13': m1 | m3}

def familia_A(R, F, c, K=K_PERM, seed=SEMILLA, mirada=1, nulo_resim=None):
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
    Tmax = np.array(Tmax); out = {}; Tmx_obs = np.nanmax(list(Tobs.values())); out['T_max_obs'] = float(Tmx_obs); out['p_max_global'] = float((1 + (Tmax >= Tmx_obs).sum()) / (len(Tmax) + 1)) if K else float('nan')
    out['p_max_postfiltro'] = out['p_max_global']            # DESCRIPTIVO: permutar F5_0 y filtrar la base despues NO es confirmatorio (DICTAMEN 5; test 3)
    if nulo_resim is not None:                               # p de la SIMULACION COMPLETA (rf5_nulo_run corre A; acople real busy/MAXV => sin tabla exacta): unico confirmatorio
        out['p_max_global'] = float(nulo_resim['p_max']); out['nulo'] = nulo_resim; out['nulo_exacto'] = (nulo_resim.get('estado') == 'NULO_RESIMULADO_EXACTO')
    elif K and {'VETO_UP', 'VETO_DN'} <= set(R.pol.unique()):  # nulo EXACTO (por tablas; con acople real sale NO_EXACTO y NO es confirmatorio) dentro del simulador (replicas por dia); si la composicion no reproduce la replica directa => NO_EXACTO
        nu = NU.nulo_replicas(R, F, c, K=K, seed=seed); out['p_max_global'] = nu['p_max']; out['nulo'] = nu; out['nulo_exacto'] = bool(nu['exacto'])
    else: out['nulo_exacto'] = None
    for k, m in obs.items():
        dd = delta_dias(m); dpnl_d = dd * cost_d; pt, lo, hi = ic90(dpnl_d, cost_d, seed=seed); ict = FR.ic_t_dias(dd, mirada)
        Dc = deltas(R, k, 'fin'); cierre = ic90(Dc.dpnl.values, Dc.cost.values, K=5000, seed=seed); cn = ic90(Dc.dpnl.values, Dc.cost.values, K=5000, seed=seed, unil=FR.UMBRAL[mirada]['ic_unil'])
        ninv = []; dinv_p = 0.0
        for g in G:                                              # inversion: vetar los F5_0 MAS BAJOS validos, mismo n por dia x moneda
            n = int(m[g].sum()); fg = f[g]; v = np.where(np.isfinite(fg))[0]; o = v[np.argsort(fg[v], kind='stable')][:n]; dinv_p += pnl[g][o].sum()
        D_inv = -dinv_p / cost_d.sum()
        out[k] = dict(delta=pt, ic90_dias=[lo, hi], ic90_cierres=[cierre[1], cierre[2]], ic_dias_t=[ict[1], ict[2]], ic_cierres=[cn[1], cn[2]], mirada=mirada, pct_dias_pos=float((dd > 0).mean()), delta_sin_2_mejores_dias=sin_mejores(dpnl_d, cost_d), delta_inversion=D_inv,
                      T=float(Tobs[k]), n_dias=len(dias), lados_vetados=int(m.sum()), lados=int(len(m)), por_dia=dict(zip(dias, map(float, dd))))
        out[k]['p_azar'] = p_azar(G, m, pnl, cost_d.sum(), -pnl[m].sum() / cost_d.sum(), K, rng) if K else float('nan')
    return out

def p_azar(G, m, pnl, cost, delta_obs, K, rng):
    """P(Delta aleatorio >= Delta observado) vetando AL AZAR el mismo n de lados por dia x moneda (prereg sec.2 d)."""
    ns = [int(m[g].sum()) for g in G]; hit = 0
    for _ in range(K):
        s = 0.0
        for g, n in zip(G, ns):
            if n: s += pnl[g][rng.permutation(len(g))[:n]].sum()
        hit += (-s / cost) >= delta_obs
    return float((1 + hit) / (K + 1))

def auc_binaria(score, y):
    """AUC de Mann-Whitney de la bandera 'F5_0 invalido' frente al desenlace y (0/1); NaN si falta una clase."""
    s = np.asarray(score, float); y = np.asarray(y, int)
    if y.min() == y.max() or s.min() == s.max(): return float('nan')
    r = pd.Series(s).rank().values; n1 = int(y.sum()); n0 = len(y) - n1
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))

def fuga_f5(R, F):
    """AUC por dia (n>=20) de 'F5_0 invalido' vs desenlace del lado; distribucion de antiguedad. 0 invalidos en todo => se exige el test unitario de la regla de 30 s (test_rf5.py)."""
    gana = R[(R.pol == 'base') & (R.bloq == 0)].groupby(['dia', 'mid', 'k']).gana.first().reset_index(); X = F[(F.bloq == 0) & (F.pol == 'base')].merge(gana, on=['dia', 'mid', 'k'], how='left'); X['inv'] = (~np.isfinite(X.f5_0.astype(float))).astype(int); out = {}
    for d, g in X.groupby('dia'):
        g = g.dropna(subset=['gana']); out[d] = dict(n=int(len(g)), auc=(auc_binaria(g.inv, g.gana) if len(g) >= 20 else None))
    ed = X.edad_ms.astype(float).dropna()
    return dict(por_dia=out, n_invalidos=int(X.inv.sum()), n=int(len(X)), edad_ms_pctiles=({str(p): float(np.percentile(ed, p)) for p in (50, 90, 99, 100)} if len(ed) else {}),
                ok_banda=all(v['auc'] is None or (np.isnan(v['auc']) or 0.40 <= v['auc'] <= 0.60) for v in out.values()))

def _lo(d, k_nuevo, k_viejo):
    """limite inferior del IC de la mirada (clave nueva); si el dict solo trae la clave vieja (IC90 bootstrap, pruebas antiguas) cae a ella."""
    return (d[k_nuevo] if k_nuevo in d else d[k_viejo])[0]

def _sin_rechazo(mirada, ic90_sup_no_pos, refutada):
    """sin rechazo: en la MIRADA 1 nunca se emite REFUTADA (adenda sec.3) => ACUMULANDO; en la FINAL, REFUTADA <=> limite superior IC90 por dias <= 0 (literal del prereg), si no NO_CONFIRMADA_A_10 (no es 'cerrada')."""
    if mirada == 1: return 'ACUMULANDO'
    return refutada if ic90_sup_no_pos else 'NO_CONFIRMADA_A_10'

def veredicto_A(k, a, fuga, c, bloq1_delta_pos, peor=None, frag=None, mirada=1):
    """CONFIRMADA_k (prereg sec.3). Devuelve (veredicto, condiciones). Sensibilidad fail-closed NO implementada => nunca CONFIRMADA completa: 'CONFIRMADA_PENDIENTE_SENS'."""
    cond = dict(delta_pos=a['delta'] > 0, ic_t_dias_lo_pos=_lo(a, 'ic_dias_t', 'ic90_dias') > 0, ic_cierres_lo_pos=_lo(a, 'ic_cierres', 'ic90_cierres') > 0, p_max_le_umbral=a['p_max_global'] <= FR.umbral_p('A', mirada), nulo_exacto=(a.get('nulo_exacto') is True), dias_pos=a['pct_dias_pos'] >= FR.DIAS_POS_MIN[mirada] - 1e-9,
                sin2mejores_pos=a['delta_sin_2_mejores_dias'] > 0, mayor_que_inversion=a['delta'] > a['delta_inversion'], p_azar_le_umbral=a['p_azar'] <= FR.UMBRAL[mirada]['vs_azar'], bloq1_pos=bool(bloq1_delta_pos), fuga_ok=bool(fuga['ok_banda']))
    if peor is not None: cond['peor_caso_desenlace_ic_pos'] = bool(_lo(peor, 'ic_dias_t', 'ic90_dias') > 0)       # C3: lados con relleno sin resolver = -coste
    cond = {x: bool(v) for x, v in cond.items()}
    if all(cond.values()):
        if frag is None: return 'CONFIRMADA_PENDIENTE_SENS_FAILCLOSED', cond            # sensibilidad por huecos no evaluada
        return ('CONFIRMADA' if frag['estado'] == 'OK_HUECOS' else 'FRAGIL_HUECOS'), dict(cond, huecos=frag['estado'])
    return _sin_rechazo(mirada, a['ic90_dias'][1] <= 0, 'REFUTADA'), cond

# ------------------------------------------------------------------ familia K
def ev_pol(R, pol, bloq=0, mirada=1):
    U = unidades(R, pol, bloq)
    if not len(U): return None
    d = U.groupby('dia').agg(pnl=('pnl', 'sum'), cost=('cost', 'sum')).reset_index(); pt, lo, hi = ic90(d.pnl.values, d.cost.values); cc = U.groupby('fin').agg(pnl=('pnl', 'sum'), cost=('cost', 'sum')); pc = ic90(cc.pnl.values, cc.cost.values, K=5000); pn = ic90(cc.pnl.values, cc.cost.values, K=5000, unil=FR.UMBRAL[mirada]['ic_unil']); ict = FR.ic_t_dias(d.pnl.values / np.maximum(d.cost.values, 1e-12), mirada)
    return dict(ev_eur=pt, ic90_dias=[lo, hi], ic90_cierres=[pc[1], pc[2]], ic_dias_t=[ict[1], ict[2]], ic_cierres=[pn[1], pn[2]], ev_sin_2_mejores_dias=sin_mejores(d.pnl.values, d.cost.values), pnl_total=float(U.pnl.sum()), coste_total=float(U.cost.sum()), lados=int(len(U)),
                rellenos=int((U.cost > 0).sum()), ev_por_unidad=float(U.pnl[U.cost > 0].mean()) if (U.cost > 0).any() else float('nan'), ev_incondicional_por_alta=float(U.pnl.sum() / len(U)), p_relleno=float((U.cost > 0).mean()), eur_dia=float(U.cost.sum() / d.shape[0]), pnl_dia=float(U.pnl.sum() / d.shape[0]))

def incremento(R, a, b, mirada=1):
    """Delta PnL/EUR de la politica a frente a la b (b = referencia), agregado por dias con IC90 por dias."""
    D = deltas(R.assign(pol=R.pol), a, 'dia', 0, base=b); pt, lo, hi = ic90(D.dpnl.values, D.cost.values); ict = FR.ic_t_dias(D.dpnl.values / np.maximum(D.cost.values, 1e-12), mirada); return dict(delta=pt, ic90_dias=[lo, hi], ic_dias_t=[ict[1], ict[2]])

def frac_cancel(R, pol, bloq=0):
    """fraccion de lados con orden colocada cuya orden se cancela por la regla (motivo_fin == 'regla'). > 0,5 => 'solo no operar' (prereg sec.4: no cuenta). None si no hay columna/datos."""
    X = R[(R.pol == pol) & (R.bloq == bloq)]
    if 'motivo_fin' not in X.columns or not len(X): return None
    g = X.groupby(['dia', 'mid', 'k']).motivo_fin.apply(lambda s: bool((s == 'regla').any())); return float(g.mean())

def familia_K(R, mirada=1):
    out = dict(politicas={}, bloq1={}, lcancel={}, ablacion={}, loo={}, aislados={}, interaccion=None, nulo_K='PENDIENTE: rf5_nulo_run.py corre K (re-simulacion con series Binance desplazadas, Besag-Clifford h=20, K_max 1500) solo en la mirada con autorizacion del chief => sin p_max_K', p_max_K=None)
    for p in ['base', 'F3', 'F3_V6', 'F3_V5', 'V5', 'V6', 'K1', 'K2', 'K3', 'K4', 'K5', 'INV_F3', 'INV_K1']: out['politicas'][p] = ev_pol(R, p, 0, mirada)
    for p in ('K1', 'K2', 'K3', 'K4'):
        out['bloq1'][p] = ev_pol(R, p, 1, mirada); out['lcancel'][p] = {lc: ev_pol(R, f'{p}@lc{lc}', 0, mirada) for lc in (111, 147)}
    out['ablacion'] = dict(F3_vs_base=incremento(R, 'F3', 'base', mirada), F3V6_vs_F3=incremento(R, 'F3_V6', 'F3', mirada), K1_vs_F3V6=incremento(R, 'K1', 'F3_V6', mirada))
    out['loo'] = dict(capa_F3=incremento(R, 'K1', 'K5', mirada), capa_V5=incremento(R, 'K1', 'F3_V6', mirada), capa_V6=incremento(R, 'K1', 'F3_V5', mirada))
    out['aislados'] = dict(F3=incremento(R, 'F3', 'base', mirada), V5=incremento(R, 'V5', 'base', mirada), V6=incremento(R, 'V6', 'base', mirada), K1_comb=incremento(R, 'K1', 'base', mirada))
    out['frac_lados_cancelados_por_regla'] = {p: frac_cancel(R, p) for p in ('K1', 'K2', 'K3', 'K4', 'K5', 'V5', 'V6')}
    out['interaccion'] = float(sum(out['aislados'][x]['delta'] for x in ('F3', 'V5', 'V6')) - out['aislados']['K1_comb']['delta'])
    return out

def veredicto_K(k, ev, kf, peor=None, frag=None, mirada=1):
    """COMBINADA_EV_POSITIVO (prereg sec.4) incompleta: faltan p_max_K y sensibilidad fail-closed => 'EV_POSITIVO_PENDIENTE_*' como mucho."""
    p = kf['politicas'].get(k);
    if p is None: return 'SIN_DATOS', {}
    cond = dict(ev_pos=p['ev_eur'] > 0, ic_t_dias_lo_pos=_lo(p, 'ic_dias_t', 'ic90_dias') > 0, ic_cierres_lo_pos=_lo(p, 'ic_cierres', 'ic90_cierres') > 0, incond_pos=p['ev_incondicional_por_alta'] > 0, sin2_pos=p['ev_sin_2_mejores_dias'] > 0,
                bloq1_pos=bool(kf['bloq1'].get(k) and kf['bloq1'][k]['ev_eur'] > 0), lc_pos=all(bool(v and v['ev_eur'] > 0) for v in kf['lcancel'].get(k, {}).values()),
                capas_loo_pos=all(_lo(v, 'ic_dias_t', 'ic90_dias') > 0 for v in kf['loo'].values()), inv_menor=(k != 'K1') or bool(kf['politicas']['INV_K1'] and kf['politicas']['INV_K1']['ev_eur'] < p['ev_eur']))
    if peor is not None: cond['peor_caso_desenlace_ic_pos'] = bool(peor is not None and peor.get(k) is not None and _lo(peor[k], 'ic_dias_t', 'ic90_dias') > 0)
    cond = {x: bool(v) for x, v in cond.items()}
    fr = (kf.get('frac_lados_cancelados_por_regla') or {}).get(k)
    if fr is not None and fr > 0.5: return 'SOLO_NO_OPERAR (>50 % de vidas disparadas; no cuenta)', dict(cond, frac_disparadas=fr)
    pm = kf.get('p_max_K')
    if pm is not None: cond['p_max_K_le_umbral'] = bool(pm <= FR.umbral_p('K1_K4', mirada))
    if all(cond.values()):
        if pm is None: return (('EV_POSITIVO_PENDIENTE_PMAXK_Y_SENS' if frag is None else ('EV_POSITIVO_PENDIENTE_PMAXK' if frag['estado'] == 'OK_HUECOS' else 'FRAGIL_HUECOS')), cond)
        return (('EV_POSITIVO_PENDIENTE_SENS' if frag is None else ('COMBINADA_EV_POSITIVO' if frag['estado'] == 'OK_HUECOS' else 'FRAGIL_HUECOS')), cond)
    return _sin_rechazo(mirada, p['ic90_dias'][1] <= 0, 'REFUTADA_COMB'), cond

def sensibilidad_huecos(R, F, c):
    """E5: Delta (A) y EV (K) con y sin los mercados cuya vida solapa un hueco >=5 s, por moneda; FRAGIL_HUECOS si el signo cambia en >=2 de 3 monedas. Sin columna hueco => None (fail-closed: no hay CONFIRMADA)."""
    excl = HU.mercados_excluidos(R)
    if excl is None: return None
    Rs = HU.excluye(R, excl); out = dict(n_mercados_excluidos=len(excl), n_mercados=int(R[(R.pol == 'base') & (R.bloq == 0)].groupby(['dia', 'mid']).ngroups), A={}, K={}); coins = ('eth', 'sol', 'xrp')
    def delta_coin(RR_, k, c_):
        X = RR_[RR_.coin.astype(str).str.lower() == c_]
        if not len(X): return None
        D = deltas(X, k, 'dia'); return float(D.dpnl.sum() / D.cost.sum()) if D.cost.sum() > 0 else None
    def ev_coin(RR_, k, c_):
        X = RR_[RR_.coin.astype(str).str.lower() == c_]; v = ev_pol(X, k) if len(X) else None; return None if v is None else v['ev_eur']
    for k in ('F1', 'F2', 'F3', 'U13'): out['A'][k] = HU.veredicto_fragil({c_: delta_coin(R, k, c_) for c_ in coins}, {c_: delta_coin(Rs, k, c_) for c_ in coins})
    for k in ('K1', 'K2', 'K3', 'K4'): out['K'][k] = HU.veredicto_fragil({c_: ev_coin(R, k, c_) for c_ in coins}, {c_: ev_coin(Rs, k, c_) for c_ in coins})
    return out

def por_bloque_4h(R):
    """resultado por bloque de 4 h UTC del dia (C1, sesgo hora-del-dia): PnL, coste y EV por bloque para base, F3 y K1 (solo con >=10 dias validos; t_dec ms epoch)."""
    out = {}
    for pol in ('base', 'F3', 'K1'):
        X = R[(R.pol == pol) & (R.bloq == 0) & (R.q > 0)]
        if not len(X): continue
        b = ((X.t_dec.astype('int64') // 3600000) % 24 // 4 * 4).astype(int); g = X.assign(b=b).groupby('b').agg(pnl=('pnl', 'sum'), cost=('cost', 'sum'), n=('pnl', 'size'))
        out[pol] = {int(i): dict(n=int(r.n), pnl=float(r.pnl), coste=float(r.cost), ev=float(r.pnl / r.cost) if r.cost > 0 else None) for i, r in g.iterrows()}
    return out

def lee_nulo(out, fam, dias, mirada):
    """resultado del nulo por re-simulacion (rf5_nulo_run corre FAM). Solo vale si fue calculado con EXACTAMENTE los dias y la mirada de esta evaluacion; si no => None (p pendiente)."""
    p = out + f'nulo_{fam}_resultado.json'
    if not os.path.exists(p): return None
    try: r = json.load(open(p))
    except Exception: return None
    return r if (r.get('dias') == list(dias) and r.get('mirada') == mirada and r.get('estado') == 'NULO_RESIMULADO_EXACTO') else None

def resumen(out, estado, c=None, min_dias=None):
    """min_dias se ignora (compatibilidad): la regla de mirada la fija rf5_fronteras.decide_mirada (adenda interina sec.2)."""
    c = c or K5.lee_cortes(); dec = FR.decide_mirada(estado); vals = FR.es_valido; dv_all = sorted(d for d, m in estado.items() if vals(m))
    res = dict(measurement_id='RF5E-COMB-23NOV-v1', codigo='v3', dias_validos=dv_all, n_dias_validos=len(dv_all), mirada_decision=dec, min_dias_mirada1=FR.MIRADA1_DIAS, estado_por_dia={d: m.get('status') for d, m in estado.items()})
    if not dv_all: res['modo'] = 'SOLO_CONTEOS (0 dias validos)'; return res
    dv = dec['dias'] or dv_all[:FR.MIRADA1_DIAS]
    reg = []; R, F = carga(out, dv, registro=reg); res['precintados_u_omitidos'] = reg
    if R is None: res['modo'] = 'SOLO_CONTEOS (ningun dia legible/no precintado)'; return res
    dv = sorted(set(R.dia)); res['dias_en_conteo'] = dv; res['conteos'] = conteos(R, F)
    if dec['mirada'] == 0 or dv != dec['dias']:
        res['modo'] = f"SOLO_CONTEOS ({dec['nombre']}: {dec['motivo'] or 'algun dia de la mirada precintado/ilegible'}; sin EV, sin PnL)"; return res
    m = dec['mirada']; res['modo'] = dec['nombre']; res['dias_validos'] = dv; res['n_dias_validos'] = len(dv); R_all = R; R, _ = sin_resolver_fuera(R_all)
    nuA = lee_nulo(out, 'A', dv, m); nuK = lee_nulo(out, 'K', dv, m); res['nulo_resimulado'] = dict(A=(None if nuA is None else dict(p_max=nuA['p_max'], n_perm=nuA['n_perm'], K_max=nuA.get('K_max'))), K=(None if nuK is None else dict(p_max=nuK['p_max'], n_perm=nuK['n_perm'], K_max=nuK.get('K_max'))))
    A = familia_A(R, F, c, mirada=m, nulo_resim=nuA); fu = fuga_f5(R, F)
    Aw = familia_A(R_all, F, c, K=0, mirada=m); Kw = {k: ev_pol(R_all, k, 0, m) for k in ('K1', 'K2', 'K3', 'K4')}
    res['peor_caso_desenlace'] = dict(familia_A={k: dict(delta=Aw[k]['delta'], ic90_dias=Aw[k]['ic90_dias'], ic_dias_t=Aw[k]['ic_dias_t']) for k in ('F1', 'F2', 'F3', 'U13')}, familia_K={k: (None if v is None else dict(ev_eur=v['ev_eur'], ic90_dias=v['ic90_dias'], ic_dias_t=v['ic_dias_t'])) for k, v in Kw.items()})
    res['por_bloque_4h'] = por_bloque_4h(R); sh = sensibilidad_huecos(R, F, c); res['sensibilidad_huecos'] = sh
    b1 = {k: deltas(R, k, 'dia', 1) for k in ('F1', 'F2', 'F3', 'U13')}; res['familia_A'] = {k: dict(A[k], veredicto=veredicto_A(k, dict(A[k], p_max_global=A['p_max_global'], nulo_exacto=A.get('nulo_exacto')), fu, c, float(b1[k].dpnl.sum()) > 0, Aw[k], (sh['A'][k] if sh else None), m)[0]) for k in ('F1', 'F2', 'F3', 'U13')}
    res['familia_A_global'] = dict(T_max_obs=A['T_max_obs'], p_max=A['p_max_global'], umbral_p=FR.umbral_p('A', m), primario='F3'); res['fuga_f5'] = fu; res['familia_K'] = kf = familia_K(R, m)
    if nuK is not None: kf['p_max_K'] = float(nuK['p_max']); kf['nulo_K'] = 'RESIMULADO (Besag-Clifford h=20)'; kf['umbral_p_K1_K4'] = FR.umbral_p('K1_K4', m)
    res['veredictos_K'] = {k: veredicto_K(k, None, kf, Kw, (sh['K'][k] if sh else None), m)[0] for k in ('K1', 'K2', 'K3', 'K4')}
    res['K6'] = 'NO evaluado en este evaluador: lo juzga rf5_k6 sobre rf5K6_*.pkl en la final de K6 (umbral rf5_fronteras.umbral_p("K6", m, alfa)); la mirada 1 SI contrasta K6 (adenda sec.6 D1)'
    return res

if __name__ == '__main__':
    import rf5_run as RR
    out = RR.OUT; est = RR.estado(); r = resumen(out, est); open(out + 'rf5_resumen.json', 'w').write(json.dumps(r, indent=1, default=str)); print(json.dumps({k: r[k] for k in ('modo', 'n_dias_validos', 'dias_validos')}, default=str))
