#!/usr/bin/env python3
"""e1b_eval.py -- evaluador de PREREG_E1b_CONFIRMACION_S1.md (sha en PREREG_E1b_CONFIRMACION_S1.sha256). Regla S1_x2_w2000, variante D100.
Sin umbrales nuevos: todo lo del preregistro y nada mas. Metricas = las de e1_eval.py (paired / boot por cierre y por dia).

Gate (dias forward VALIDOS, >= 80 % de los 864 mercados 5m ETH/SOL/XRP esperados con desenlace oficial; manifest COMPLETE):
 CONFIRMADA si >= 5 dias validos y: G1 dPnL/EUR > 0 con IC90 por DIA > 0 y por CIERRE > 0 (limite inferior); G2 >= 60 % de dias con dPnL > 0;
 G3 dPnL/EUR > INV y > max de los 8 desplazamientos; G4 D250 > 0; G5 subconjunto R2-falso (bid15 mismo lado - obj > 0,03 en r-100 ms) dPnL > 0.
 REFUTADA si >= 5 dias y limite superior IC90 por dia <= 0, o si a >= 10 dias la estimacion puntual <= 0.  Si no: ACUMULANDO.
Uso:  e1b_eval.py [--dir E1B] [--fwd0 2026-10-23] [--json] [--telegram]      forward (lee dias/D.json COMPLETE)
      e1b_eval.py --repro                                                    17-22 Oct (DESC/TEST de E1) -> reproduce e1_eval.txt para S1_x2_w2000 (no es un gate)"""
import sys, os, json, glob, argparse, hashlib, datetime
import numpy as np, pandas as pd

AQUI = os.path.dirname(os.path.abspath(__file__)); PLAN = os.path.abspath(os.path.join(AQUI, '..'))
E1B_DEF = os.environ.get('E1B_DIR', '/root/polymarket-research-datalogs/e1b/').rstrip('/') + '/'
RULE = 'S1_x2_w2000'; SH = [f'SH{s:+d}' for s in (-240, -180, -120, -60, 60, 120, 180, 240)]
NBOOT = 10000; SEED = 20261022; R2_UMBRAL = 0.03
DESC = ['2026-10-17', '2026-10-18', '2026-10-19']; TEST = ['2026-10-20', '2026-10-21', '2026-10-22']


def boot(dp, coste, key, n=NBOOT, seed=SEED):
    """IC90 percentil (5,95) de sum(dp)/sum(coste_base) remuestreando grupos `key` (cierre o dia). Igual que e1_eval.boot."""
    g = pd.DataFrame({'dp': np.asarray(dp, float), 'c': np.asarray(coste, float), 'k': np.asarray(key)}).groupby('k').sum()
    a = g.dp.values; c = g.c.values; m = len(a)
    if m < 2: return [float('nan'), float('nan')]
    rng = np.random.default_rng(seed); i = rng.integers(0, m, (n, m)); s = a[i].sum(1) / np.maximum(c[i].sum(1), 1e-12)
    return [float(np.percentile(s, 5)), float(np.percentile(s, 95))]


def preparar(X):
    X = X.copy(); X['coste'] = np.where(X.fill == 1, 5 * X.obj, 0.0); X['pnl'] = np.where(X.fill == 1, 5 * (X.gana - X.obj), 0.0)
    B = X[X['var'] == 'BASE']
    if B.mid.duplicated().any(): raise ValueError(f'mercados BASE duplicados: {int(B.mid.duplicated().sum())} (un mercado en dos dias?)')
    if X.duplicated(['mid', 'var']).any(): raise ValueError('claves (mid,var) duplicadas')
    return X, B.set_index('mid')


def paired(X, B, var):
    V = X[X['var'] == var].set_index('mid'); b = B.loc[V.index]; dp = V.pnl - b.pnl
    rem = (b.fill == 1) & ((V.fill == 0) | (V.r != b.r)); sub = rem & (V.fill == 1)
    return dict(dpnl=float(dp.sum()), dpe=float(dp.sum() / b.coste.sum()), ev_base=float(b.pnl.sum() / b.coste.sum()), ev_var=float(V.pnl.sum() / max(V.coste.sum(), 1e-9)),
                ret=float(V.coste.sum() / b.coste.sum()), n_base=int(b.fill.sum()), n_var=int(V.fill.sum()), coste_base=float(b.coste.sum()),
                quitados=int(rem.sum()), ev_quitados=float(b.pnl[rem].sum() / b.coste[rem].sum()) if rem.any() else float('nan'),
                sustitutos=int(sub.sum()), ev_sust=float(V.pnl[sub].sum() / V.coste[sub].sum()) if sub.any() else float('nan')), dp, b


def evaluar(X, aux=None, nboot=NBOOT):
    """X = filas e1 (todas las variantes) de los dias a evaluar ; aux = DataFrame (mid, lvl15) con bid15-obj de cada relleno BASE."""
    X, B = preparar(X); dias = sorted(X.dia.unique()); res = {'dias': dias, 'n_dias': len(dias)}
    m, dp, b = paired(X, B, f'{RULE}|D100'); res['D100'] = m
    m['ic_cierre'] = boot(dp, b.coste, b.fin, nboot); m['ic_dia'] = boot(dp, b.coste, b.dia, nboot)
    m['por_dia'] = {d: float(dp[b.dia == d].sum()) for d in dias}; m['por_dia_eur'] = {d: float(b.coste[b.dia == d].sum()) for d in dias}
    m['por_moneda'] = {a: float(dp[b.act == a].sum()) for a in ('ETH', 'SOL', 'XRP')}
    pd_ = sorted(m['por_dia'].values()); m['dpnl_sin_2_mejores_dias'] = float(sum(pd_[:-2])) if len(pd_) > 2 else float('nan')
    res['D250'] = paired(X, B, f'{RULE}|D250')[0]; res['D0'] = paired(X, B, f'{RULE}|D0')[0]; res['INV'] = paired(X, B, f'{RULE}|INV')[0]
    res['SH'] = {s: paired(X, B, f'{RULE}|{s}')[0]['dpe'] for s in SH}
    # R2-falso / R2-verdadero / sin bid15, sobre los rellenos BASE
    if aux is not None:
        L = aux.drop_duplicates('mid').set_index('mid').lvl15.reindex(b.index); f = b.fill == 1
        sub = {}
        for nm, mk in (('R2_falso', f & (L > R2_UMBRAL + 1e-9)), ('R2_verdadero', f & (L <= R2_UMBRAL + 1e-9)), ('sin_bid15', f & L.isna())):
            c = b.coste[mk].sum(); sub[nm] = dict(rellenos=int(mk.sum()), dpnl=float(dp[mk].sum()), dpe=float(dp[mk].sum() / c) if c > 0 else float('nan'),
                                                   ev_base=float(b.pnl[mk].sum() / c) if c > 0 else float('nan'))
        res['R2'] = sub
    else: res['R2'] = None
    # gate
    sh = list(res['SH'].values()); n = len(dias); dias_pos = sum(v > 0 for v in m['por_dia'].values())
    G = {'G1': bool(m['dpnl'] > 0 and m['dpe'] > 0 and m['ic_dia'][0] > 0 and m['ic_cierre'][0] > 0),
         'G2': bool(n > 0 and dias_pos / n >= 0.60),
         'G3': bool(m['dpe'] > res['INV']['dpe'] and m['dpe'] > max(sh)),
         'G4': bool(res['D250']['dpnl'] > 0 and res['D250']['dpe'] > 0),
         'G5': bool(res['R2'] is not None and res['R2']['R2_falso']['rellenos'] > 0 and res['R2']['R2_falso']['dpnl'] > 0)}
    res['gate'] = G; res['dias_positivos'] = dias_pos
    conf = n >= 5 and all(G.values())
    ref = (n >= 5 and not np.isnan(m['ic_dia'][1]) and m['ic_dia'][1] <= 0) or (n >= 10 and m['dpe'] <= 0)
    res['veredicto'] = 'CONFIRMADA' if conf else ('REFUTADA' if ref else 'ACUMULANDO')
    if res['R2'] is not None and res['R2']['R2_verdadero']['rellenos'] > 0:
        res['expectativa_R2_verdadero'] = {'dpe': res['R2']['R2_verdadero']['dpe'], 'aviso_no_apilar_sobre_R3': bool(res['R2']['R2_verdadero']['dpe'] < 0)}
    return res



# ============================================================ ADDENDUM_E1b (A1-A8) -> veredicto V1
PRIM = f'{RULE}|D250'; NBOOT_NULL = 5000
SH250 = [f'{RULE}|SH{s:+d}_250' for s in (-240, -180, -120, -60, 60, 120, 180, 240)]
DELTA_E1_PP = 0.033; COSTE_DIA_DEF = 42.0; MIN_B_REAL = 100


def boot_ratio(num, den, key, n=NBOOT, seed=SEED):
    """IC90 (5,95) de sum(num)/sum(den) remuestreando grupos `key`"""
    g = pd.DataFrame({'a': np.asarray(num, float), 'c': np.asarray(den, float), 'k': np.asarray(key)}).groupby('k').sum(); a = g.a.values; c = g.c.values; m = len(a)
    if m < 2: return [float('nan'), float('nan')]
    i = np.random.default_rng(seed).integers(0, m, (n, m)); s = a[i].sum(1) / np.maximum(c[i].sum(1), 1e-12)
    return [float(np.percentile(s, 5)), float(np.percentile(s, 95))]


def boot_ev_diff(pv, cv, pb, cb, key, n=NBOOT, seed=SEED):
    """IC90 de EV_var - EV_base (ponderado por EUR) remuestreando dias"""
    g = pd.DataFrame({'pv': pv, 'cv': cv, 'pb': pb, 'cb': cb, 'k': key}).groupby('k').sum(); m = len(g)
    if m < 2: return [float('nan'), float('nan')]
    i = np.random.default_rng(seed).integers(0, m, (n, m)); A = {c: g[c].values[i].sum(1) for c in ('pv', 'cv', 'pb', 'cb')}
    s = A['pv'] / np.maximum(A['cv'], 1e-12) - A['pb'] / np.maximum(A['cb'], 1e-12)
    return [float(np.percentile(s, 5)), float(np.percentile(s, 95))]


def descomponer(X, B, var):
    """-> dict con eliminacion / sustitucion de `var` frente a BASE (mismas definiciones que el red team rt1/rt2)"""
    V = X[X['var'] == var].set_index('mid'); b = B.loc[V.index]; f = b.fill == 1
    rem = f & ((V.fill == 0) | (V.r != b.r)); gone = f & (V.fill == 0); sub = rem & (V.fill == 1)
    return V, b, f, gone, sub


def evaluar_add(X, Xe, aux=None, unidades_b=None, nboot=NBOOT, nnull=NBOOT_NULL, coste_dia_b=None):
    """V1 del ADDENDUM_E1b. X = filas e1 (todas las variantes originales) ; Xe = filas e1x (extras A4/A5). Variante primaria S1_x2_w2000|D250."""
    XA = pd.concat([X, Xe], ignore_index=True) if Xe is not None and len(Xe) else X
    XA, B = preparar(XA); dias = sorted(B.dia.unique()); n = len(dias); res = {'dias': dias, 'n_dias': n, 'variante_primaria': PRIM}
    if PRIM not in set(XA['var']): raise ValueError('falta la variante primaria')
    m, dp, b = paired(XA, B, PRIM); V, b, f, gone, sub = descomponer(XA, B, PRIM)
    m['ic_cierre'] = boot(dp, b.coste, b.fin, nboot); m['ic_dia'] = boot(dp, b.coste, b.dia, nboot)
    m['por_dia'] = {d: float(dp[b.dia == d].sum()) for d in dias}; res['P'] = m
    cb = b.coste.sum()
    # A1: EV ponderado por EUR
    a1_ic = boot_ev_diff(V.pnl.values, V.coste.values, b.pnl.values, b.coste.values, b.dia.values, nboot)
    res['A1'] = {'ev_var': m['ev_var'], 'ev_base': m['ev_base'], 'diff': m['ev_var'] - m['ev_base'], 'ic_dia': a1_ic, 'ok': bool(m['ev_var'] > m['ev_base'] and a1_ic[0] > 0)}
    # A2: sustitucion y eliminacion por separado
    sus_v = np.where(sub, V.pnl - b.pnl, 0.0); eli_v = np.where(gone, -b.pnl, 0.0)
    sus_ic = boot_ratio(sus_v, b.coste, b.dia, nboot); eli_ic = boot_ratio(eli_v, b.coste, b.dia, nboot)
    ev_gone = float(b.pnl[gone].sum() / b.coste[gone].sum()) if gone.any() else float('nan'); ev_f = float(b.pnl[f].sum() / b.coste[f].sum())
    obs = float(eli_v.sum()); rng = np.random.default_rng(SEED); pdias = []
    for d in dias:
        h = b[(b.dia == d) & f]; k = int(gone[h.index].sum()); pdias.append((h.pnl.values, k))
    sims = np.zeros(nnull)
    for pv_, k in pdias:
        if k == 0 or len(pv_) == 0: continue
        idx = np.argsort(rng.random((nnull, len(pv_))), axis=1)[:, :k]; sims += -pv_[idx].sum(1)
    p_null = float(np.mean(sims >= obs - 1e-12)) if gone.any() else float('nan')
    cond_b = bool((not gone.any()) or ev_gone <= ev_f or p_null < 0.10)      # sin eliminados la condicion es vacua (nada que perjudicar)
    res['A2'] = {'sust_pe': float(sus_v.sum() / cb), 'sust_ic_dia': sus_ic, 'sust_n': int(sub.sum()), 'elim_pe': obs / cb, 'elim_ic_dia': eli_ic, 'elim_n': int(gone.sum()),
                 'ev_eliminados': ev_gone, 'ev_rellenos_base': ev_f, 'eliminados_no_mejores': bool((not gone.any()) or ev_gone <= ev_f), 'p_azar_mismo_n_dia': p_null, 'azar_media_eur': float(sims.mean()),
                 'ok': bool(sus_v.sum() > 0 and sus_ic[0] > 0 and cond_b)}
    # A3 (informativo)
    nb = 0; delta = DELTA_E1_PP; fuente = 'delta E1 (+3,3 pp)'; coste_dia = coste_dia_b or COSTE_DIA_DEF
    if unidades_b is not None:
        U = unidades_b[unidades_b.dia.isin(dias)]; nb = len(U)
        if nb >= MIN_B_REAL:
            delta = float(U.gana.mean() - b.gana[f].mean()); fuente = f'B real n={nb}'; coste_dia = float(U.groupby('dia').coste.sum().mean())
    ne = int(gone.sum()); ce = float(b.coste[gone].sum()); ge = float(b.gana[gone].sum())
    elim_recal = -((ge + delta * ne) * 5 - ce) if ne else 0.0
    res['A3'] = {'delta_acierto': delta, 'fuente_delta': fuente, 'n_b_real': nb, 'coste_dia_b': coste_dia, 'sust_pe': res['A2']['sust_pe'], 'elim_recalibrada_pe': elim_recal / cb,
                 'eur_anual': 365 * coste_dia * (res['A2']['sust_pe'] + elim_recal / cb)}
    # A4: X50 y controles 250
    def dpe_of(var):
        if var not in set(XA['var']): return None
        return paired(XA, B, var)[0]
    x50 = dpe_of(f'{RULE}|X50'); cob = (XA[XA['var'] == f'{RULE}|X50'].mid.nunique() / max(len(B), 1)) if x50 else 0.0
    res['A4'] = {'X50': x50, 'X50_cobertura_mercados': cob, 'X50_ok': bool(x50 is not None and cob >= 0.9 and x50['dpnl'] > 0)}
    inv = dpe_of(f'{RULE}|INV250'); shs = [dpe_of(v) for v in SH250]
    res['controles'] = {'INV250': inv['dpe'] if inv else None, 'SH250': [s['dpe'] if s else None for s in shs]}
    # A5
    c1 = dpe_of('C1|D250'); c2 = dpe_of('C2|FILL')
    def domina(c): return bool(c is not None and c['dpe'] >= m['dpe'] and c['ret'] >= m['ret'])
    res['A5'] = {'S1': {'dpe': m['dpe'], 'ret': m['ret'], 'ev_var': m['ev_var']}, 'C1_D250': {k: c1[k] for k in ('dpe', 'ret', 'ev_var')} if c1 else None,
                 'C2': {k: c2[k] for k in ('dpe', 'ret', 'ev_var')} if c2 else None, 'ok': bool(c1 is not None and c2 is not None and not domina(c1) and not domina(c2))}
    # R2 (G5 y A6)
    if aux is not None:
        L = aux.drop_duplicates('mid').set_index('mid').lvl15.reindex(b.index); R = {}
        for nm, mk in (('R2_falso', f & (L > R2_UMBRAL + 1e-9)), ('R2_verdadero', f & (L <= R2_UMBRAL + 1e-9)), ('sin_bid15', f & L.isna())):
            c = b.coste[mk].sum(); R[nm] = {'rellenos': int(mk.sum()), 'dpnl': float(dp[mk].sum()), 'dpe': float(dp[mk].sum() / c) if c > 0 else float('nan')}
        res['R2'] = R
    else: res['R2'] = None
    res['A6_apilable_sobre_R3'] = bool(res['R2'] is not None and res['R2']['R2_verdadero']['rellenos'] > 0 and res['R2']['R2_verdadero']['dpnl'] >= 0)
    # puertas V1
    shv = [s for s in res['controles']['SH250'] if s is not None]
    G = {'G1': bool(m['dpnl'] > 0 and m['ic_dia'][0] > 0 and m['ic_cierre'][0] > 0),
         'G2': bool(sum(v > 0 for v in m['por_dia'].values()) / max(n, 1) >= 0.60),
         'G3': bool(inv is not None and len(shv) == 8 and m['dpe'] > inv['dpe'] and m['dpe'] > max(shv)),
         'G5': bool(res['R2'] is not None and res['R2']['R2_falso']['rellenos'] > 0 and res['R2']['R2_falso']['dpnl'] > 0),
         'A1': res['A1']['ok'], 'A2': res['A2']['ok'], 'A5': res['A5']['ok'], 'A4_X50': res['A4']['X50_ok']}
    res['gate'] = G; res['dias_positivos'] = sum(v > 0 for v in m['por_dia'].values())
    conf = n >= 5 and all(G.values()); ref = (n >= 5 and not np.isnan(m['ic_dia'][1]) and m['ic_dia'][1] <= 0) or (n >= 10 and m['dpe'] <= 0)
    res['veredicto_V1'] = 'CONFIRMADA_ADD' if conf else ('REFUTADA_ADD' if ref else 'ACUMULANDO')
    return res


def etiqueta_final(v0, v1):
    if v0 == 'CONFIRMADA' and v1 != 'CONFIRMADA_ADD': return 'CONFIRMADA SOLO POR VOLUMEN, mecanismo no demostrado (no proponer B_S1)'
    return f'V0={v0} V1={v1}'


def informe_add(r, titulo='E1b ADDENDUM'):
    m = r['P']; a2 = r['A2']; L = [f"=== {titulo}: primaria {PRIM} | dias validos {r['n_dias']} {r['dias']}"]
    L.append(f"D250: dPnL {m['dpnl']:+.1f} ({m['dpe']:+.4f}/EUR) IC90 cierre {m['ic_cierre'][0]:+.4f},{m['ic_cierre'][1]:+.4f} dia {m['ic_dia'][0]:+.4f},{m['ic_dia'][1]:+.4f} | por dia " + ' '.join(f'{d[5:]}:{v:+.1f}' for d, v in m['por_dia'].items()))
    L.append(f"A1 EV var {r['A1']['ev_var']:+.4f} base {r['A1']['ev_base']:+.4f} dif {r['A1']['diff']:+.4f} IC90 dia {r['A1']['ic_dia'][0]:+.4f},{r['A1']['ic_dia'][1]:+.4f} -> {r['A1']['ok']}")
    L.append(f"A2 sustitucion {a2['sust_pe']:+.4f}/EUR (n={a2['sust_n']}) IC90 dia {a2['sust_ic_dia'][0]:+.4f},{a2['sust_ic_dia'][1]:+.4f} | eliminacion {a2['elim_pe']:+.4f}/EUR (n={a2['elim_n']}) IC90 dia {a2['elim_ic_dia'][0]:+.4f},{a2['elim_ic_dia'][1]:+.4f} | "
             f"EV eliminados {a2['ev_eliminados']:+.3f} vs rellenos {a2['ev_rellenos_base']:+.3f} (no mejores {a2['eliminados_no_mejores']}) | p azar {a2['p_azar_mismo_n_dia']:.3f} -> {a2['ok']}")
    a3 = r['A3']; L.append(f"A3 (informativo) delta acierto {a3['delta_acierto']:+.3f} [{a3['fuente_delta']}] sust {a3['sust_pe']:+.4f} + elim recalibrada {a3['elim_recalibrada_pe']:+.4f} /EUR x coste/dia B {a3['coste_dia_b']:.1f} -> {a3['eur_anual']:+.0f} EUR/anyo")
    x = r['A4']['X50']; L.append('A4 X50 (exchange): ' + (f"dPnL {x['dpnl']:+.1f} ({x['dpe']:+.4f}/EUR) cobertura {r['A4']['X50_cobertura_mercados']:.2f}" if x else 'missing (sin td)') + f" -> {r['A4']['X50_ok']} | controles INV250 {r['controles']['INV250']} SH250 max {max([s for s in r['controles']['SH250'] if s is not None], default=None)}")
    L.append('A5 (dpe, retencion, EV_var) S1 ' + str(tuple(round(v, 4) for v in r['A5']['S1'].values())) + ' | C1 ' + (str(tuple(round(v, 4) for v in r['A5']['C1_D250'].values())) if r['A5']['C1_D250'] else 'missing') + ' | C2 ' + (str(tuple(round(v, 4) for v in r['A5']['C2'].values())) if r['A5']['C2'] else 'missing') + f" -> ningun control domina: {r['A5']['ok']}")
    if r['R2']: L.append('R2: ' + ' | '.join(f"{k} n={v['rellenos']} dPnL {v['dpnl']:+.1f} ({v['dpe']:+.4f})" for k, v in r['R2'].items()) + f" | A6 apilable sobre R3: {r['A6_apilable_sobre_R3']}")
    L.append('GATE V1 ' + str(r['gate']) + f" -> {r['veredicto_V1']}" + ('' if r['n_dias'] >= 5 else f" (necesita >=5 dias validos; hay {r['n_dias']})"))
    return '\n'.join(L)


def dias_validos(E1B, fwd0):
    """-> (lista de dias COMPLETE >= fwd0, dict de motivos de los que no entran)"""
    ok = []; no = {}
    for f in sorted(glob.glob(E1B + 'dias/*.json')):
        d = os.path.basename(f)[:-5]
        if d < fwd0: continue
        try: M = json.load(open(f))
        except Exception: no[d] = 'manifest ilegible'; continue
        if M.get('estado') == 'COMPLETE' and os.path.exists(E1B + f'e1_{d}.csv.gz') and os.path.exists(E1B + f'e1x_{d}.csv.gz'): ok.append(d)
        else: no[d] = f"{M.get('estado')}: {M.get('motivo', '')}"[:200]
    return ok, no


def cargar_forward(E1B, dias):
    X = pd.concat([pd.read_csv(E1B + f'e1_{d}.csv.gz') for d in dias], ignore_index=True)
    ax = [pd.read_csv(E1B + f'aux_{d}.csv.gz') for d in dias if os.path.exists(E1B + f'aux_{d}.csv.gz')]
    aux = pd.concat(ax, ignore_index=True) if len(ax) == len(dias) else None
    Xe = pd.concat([pd.read_csv(E1B + f'e1x_{d}.csv.gz') for d in dias if os.path.exists(E1B + f'e1x_{d}.csv.gz')], ignore_index=True)
    return X, aux, Xe


def descriptivo_breal(E1B, dias):
    fs = [E1B + f'breal_{d}.csv.gz' for d in dias if os.path.exists(E1B + f'breal_{d}.csv.gz')]
    if not fs: return None
    W = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True); out = {'rellenos_reales': len(W), 'con_print': int(W.flag.notna().sum()), 'sin_print_missing': int(W.flag.isna().sum())}
    for fl in (1, 0):
        s = W[W.flag == fl]
        out[f'senal={fl}'] = dict(n=len(s), acierto=float(s.gana.mean()) if len(s) else None, ev=float(s.pnl.sum() / s.coste.sum()) if len(s) and s.coste.sum() > 0 else None, pnl=float(s.pnl.sum()))
    return out


def informe(res, no_validos=None, breal=None, titulo='E1b forward'):
    m = res['D100']; L = [f'=== {titulo}: {RULE} D100 | dias validos {res["n_dias"]} {res["dias"]}']
    if no_validos: L.append('dias NO validos (no entran): ' + '; '.join(f'{d}: {v}' for d, v in no_validos.items()))
    L.append(f"BASE: rellenos {m['n_base']} coste {m['coste_base']:.1f} EUR EV {m['ev_base']:+.4f} | variante: rellenos {m['n_var']} EV {m['ev_var']:+.4f} retiene coste {m['ret']:.2f}")
    L.append(f"dPnL {m['dpnl']:+.1f} EUR ({m['dpe']:+.4f}/EUR) IC90 cierre {m['ic_cierre'][0]:+.4f},{m['ic_cierre'][1]:+.4f} IC90 dia {m['ic_dia'][0]:+.4f},{m['ic_dia'][1]:+.4f}")
    L.append('por dia: ' + ' '.join(f'{d[5:]}:{v:+.1f}' for d, v in m['por_dia'].items()) + f"  (positivos {res['dias_positivos']}/{res['n_dias']}; sin 2 mejores dias {m['dpnl_sin_2_mejores_dias']:+.1f})")
    L.append('por moneda: ' + ' '.join(f'{k}{v:+.1f}' for k, v in m['por_moneda'].items()))
    sh = res['SH']; L.append(f"controles: INV {res['INV']['dpe']:+.4f} | placebo max {max(sh.values()):+.4f} media {np.mean(list(sh.values())):+.4f} | D250 {res['D250']['dpnl']:+.1f} ({res['D250']['dpe']:+.4f}) | D0 {res['D0']['dpe']:+.4f}")
    L.append(f"quitados n={m['quitados']} EV {m['ev_quitados']:+.3f} | sustitutos n={m['sustitutos']} EV {m['ev_sust']:+.3f}")
    if res['R2']:
        L.append('R2: ' + ' | '.join(f"{k} n={v['rellenos']} EV base {v['ev_base']:+.3f} dPnL {v['dpnl']:+.1f} ({v['dpe']:+.4f}/EUR)" for k, v in res['R2'].items()))
        if 'expectativa_R2_verdadero' in res:
            e = res['expectativa_R2_verdadero']; L.append(f"expectativa declarada (no gate): R2-verdadero incremento ~0 (E1 +0,002); forward {e['dpe']:+.4f}" + ('  -> <0: S1 NO se apila sobre R3' if e['aviso_no_apilar_sobre_R3'] else ''))
    else: L.append('R2: sin aux -> G5 no evaluable (falso)')
    if breal: L.append('B real (descriptivo, no gate): ' + json.dumps(breal, default=float))
    L.append('GATE ' + str(res['gate']) + f"  -> {res['veredicto']}" + ('' if res['n_dias'] >= 5 else f"  (necesita >=5 dias validos; hay {res['n_dias']})"))
    return '\n'.join(L)


def repro():
    """Reproduce e1_eval.txt para S1_x2_w2000 sobre 17-22 Oct (DESC/TEST). aux R2 se calcula desde los npz de salida/datos (no hace falta E1B)."""
    sys.path.insert(0, os.path.join(PLAN, '..', 'salida', 'scripts')); sys.path.insert(0, AQUI)
    import msdata, e1b_diario
    DD = os.path.join(PLAN, 'datos'); out = {}
    for per, dias in (('DESC', DESC), ('TEST', TEST), ('TODO', DESC + TEST)):
        X = pd.concat([pd.read_csv(f'{DD}/e1_{d}.csv.gz') for d in dias], ignore_index=True)
        ax = []
        for d in dias:
            cf = os.environ.get('E1B_REPRO_CACHE', '/tmp') + f'/aux_repro_{d}.csv.gz'
            if os.path.exists(cf): ax.append(pd.read_csv(cf)); continue
            e1b_diario.E1B = DD + '/'                         # lvl15_aux lee e1_D de PLAN/datos y el npz de salida/datos via msdata.DD por defecto
            a = e1b_diario.lvl15_aux(msdata.Dia, d); a.to_csv(cf, index=False); ax.append(a)
        res = evaluar(X, pd.concat(ax, ignore_index=True)); out[per] = res
        print(informe(res, titulo=f'REPRO {per}'))
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--dir', default=E1B_DEF); ap.add_argument('--fwd0', default='2026-10-23'); ap.add_argument('--repro', action='store_true')
    ap.add_argument('--json', action='store_true'); ap.add_argument('--telegram', action='store_true')
    a = ap.parse_args(); E1B = a.dir.rstrip('/') + '/'
    pre = PLAN + '/PREREG_E1b_CONFIRMACION_S1.md'
    for f_, h_ in (('PREREG_E1b_CONFIRMACION_S1', 'PREREG_E1b_CONFIRMACION_S1'), ('ADDENDUM_E1b', 'ADDENDUM_E1b')):
        if hashlib.sha256(open(f'{PLAN}/{f_}.md', 'rb').read()).hexdigest() != open(f'{PLAN}/{h_}.sha256').read().split()[0]:
            print(f'{f_} CAMBIADO: abortar'); return 4
    if a.repro: repro(); return 0
    ok, no = dias_validos(E1B, a.fwd0)
    if not ok:
        print(f'E1b: 0 dias validos todavia (>= {a.fwd0}). No validos: {no}'); res = {'veredicto': 'ACUMULANDO', 'n_dias': 0, 'dias': [], 'no_validos': no}
        txt = 'E1b: 0 dias validos'
    else:
        X, aux, Xe = cargar_forward(E1B, ok); res = evaluar(X, aux); res['no_validos'] = no; br = descriptivo_breal(E1B, ok)
        ub = E1B + 'unidades_b.csv' if os.path.exists(E1B + 'unidades_b.csv') else os.path.join(PLAN, '..', 'salida', 'datos', 'unidades_b.csv'); U = pd.read_csv(ub) if os.path.exists(ub) else None
        r1 = evaluar_add(X, Xe, aux, U); res['V1'] = r1; res['veredicto_V0'] = res['veredicto']; res['etiqueta'] = etiqueta_final(res['veredicto'], r1['veredicto_V1'])
        txt = informe(res, no, br) + '\n' + informe_add(r1) + '\nFINAL: ' + res['etiqueta']; print(txt)
    res['calculado'] = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    sf = E1B + 'e1b_estado.json'; prev = json.load(open(sf)) if os.path.exists(sf) else {}
    if a.json or a.telegram:
        tmp = sf + '.tmp'; json.dump({'ultimo': res, 'previo_veredicto': prev.get('ultimo', {}).get('veredicto'), 'previo_n_dias': prev.get('ultimo', {}).get('n_dias')}, open(tmp, 'w'), indent=1, default=float); os.replace(tmp, sf)
        open(E1B + 'e1b_informe.txt', 'w').write(txt + '\n')
    # Telegram solo si cambia el veredicto o se cruzan los 5 dias validos por primera vez (latch por veredicto, no por cifras)
    if a.telegram:
        v1 = res.get('V1', {}).get('veredicto_V1'); pv = prev.get('ultimo', {}); pv1 = pv.get('V1', {}).get('veredicto_V1')
        cambio = (pv.get('veredicto') != res['veredicto'] and (pv or res['veredicto'] != 'ACUMULANDO')) or (pv1 != v1 and (pv1 or v1 not in (None, 'ACUMULANDO')))
        cruza5 = res['n_dias'] >= 5 and pv.get('n_dias', 0) < 5
        if cambio or cruza5:
            sys.path.insert(0, '/root/polymarket-research'); from shadow_digest import enviar_telegram
            enviar_telegram('📊 E1b (S1 retirar puja si Binance cae >=2 bps) forward: ' + res.get('etiqueta', res['veredicto']) + f" con {res['n_dias']} dias validos\n" + txt[-2400:])
    return 0


if __name__ == '__main__': sys.exit(main())
