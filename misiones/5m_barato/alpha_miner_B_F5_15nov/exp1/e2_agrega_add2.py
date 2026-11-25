#!/usr/bin/env python3
"""e2_agrega_add2.py [--smoke D1,D2] -- ADDENDUM2 §3-§5 (sha en ../ADDENDUM2_B_F5.sha256). Poblacion CENSURADA (solo prints = fills ajenos): gradiente, NO EV de regla.
(1) Regresion C10: reproduce la serie diaria pond. EUR y n_prints de las 4 celdas decisivas de E2_poblacion.json (ADD1, 35 dias) o aborta sin escribir.
(2) Unidad mercado-lado (mid, lado_m, tercil, segmento dia-epoca): EV pond. EUR y medio por unidad por tercil, inversion (alto), gradiente diario EUR y por unidad
    (IC90 por dias, dias+, sin 2 mejores), placebo por UNIDAD (permutacion dentro de dia x moneda x hora, B=1000, max-stat K=4) y regla de etiqueta §4 (solo endurece).
(3) Sensibilidad §2 (no decide): celdas por clase de suelo con 37 dias (hi = R1+R0hi+R2hi, lo = R2+R1lo) y gradiente propio de 16-Oct y 24-Oct. Solo lectura de caches; sin red."""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popdata_add2 import *
t0 = time.time(); SM = '--smoke' in sys.argv; DS = sys.argv[sys.argv.index('--smoke') + 1].split(',') if SM else None; B = 20 if SM else 1000
OUT = EXP + ('smoke_' if SM else '') + 'E2_poblacion_add2'
P, est = carga_pob(specs_keep=['p35', 'p60'], dias=DS); cobL, por = resumen_cobertura(est)
COMPLETO = (not SM) and len(por.get('COMPLETE', [])) == len(est)
REF = json.load(open(EXP + 'E2_poblacion.json'))['decisivas']
dia = P.dia.to_numpy(dtype=object); ep = P.epoca.to_numpy(dtype=object); coin = P.coin.to_numpy(dtype=object); hora = P.hora.values.astype(int)
pnl = P.pnl.values.astype(float); co = P.coste.values.astype(float); q = P.q.values.astype(float); cl = P.fin.values.astype(np.int64)
mid = P.mid.to_numpy(dtype=object); lado = P.lado_m.to_numpy(dtype=object); add2 = np.isin(dia, DIAS_ADD2)
sid_all = pd.factorize(pd.MultiIndex.from_arrays([dia, coin, hora]))[0]
etq2 = {str(k): int(v) for k, v in zip(*np.unique(ep[add2].astype(str), return_counts=True))} if add2.any() else {}
txt = [f'# E2 ADD2 (ADDENDUM1 {ADD_SHA[:8]} + ADDENDUM2 {ADD2_SHA[:8]}) -- poblacion CENSURADA: gradiente, NO EV de regla' + (f" [SMOKE {','.join(DS)}, B={B}]" if SM else '')] + cobL
txt.append(f"Estado: {'COMPLETO 37/37' if COMPLETO else 'PARTIAL'}; prints {len(P)} (dias ADD1 {int((~add2).sum())}, dias ADD2 {int(add2.sum())}; etiquetas ADD2 {etq2})")
def codes(f5): t = ter(f5); return np.select([t == 'bajo', t == 'medio', t == 'alto'], [0, 1, 2], 3).astype(np.int8)
def tipoB(nm): b = P['bid_' + nm].values.astype(float); return np.isfinite(b) & ((b - q) >= 0.0099 - 1e-12)
def g_eur(seg, c, p_, k_, ns):           # por segmento: Σpnl/Σcoste(bajo) - Σpnl/Σcoste(alto)
    mb, ma = c == 0, c == 2; cb = np.bincount(seg[mb], k_[mb], ns); ca = np.bincount(seg[ma], k_[ma], ns); sb = np.bincount(seg[mb], p_[mb], ns); sa = np.bincount(seg[ma], p_[ma], ns)
    g = np.full(ns, np.nan); ok = (cb > 0) & (ca > 0); g[ok] = sb[ok] / cb[ok] - sa[ok] / ca[ok]; return g
def g_uni(seg, c, r_, ns):               # por segmento: media de EV_u (bajo) - media de EV_u (alto)
    mb, ma = c == 0, c == 2; nb = np.bincount(seg[mb], None, ns); na = np.bincount(seg[ma], None, ns); sb = np.bincount(seg[mb], r_[mb], ns); sa = np.bincount(seg[ma], r_[ma], ns)
    g = np.full(ns, np.nan); ok = (nb > 0) & (na > 0); g[ok] = sb[ok] / nb[ok] - sa[ok] / na[ok]; return g
def serie(g):
    d = g[np.isfinite(g)]
    if len(d) < 3: return dict(n_seg=int(len(d)), media=float(np.mean(d)) if len(d) else np.nan, ic90_inf=np.nan, p_t=np.nan, dias_pos=int((d > 0).sum()), frac_pos=float((d > 0).mean()) if len(d) else np.nan, sin2=np.nan)
    lo, p, mu = t_ic(d); s = np.sort(d); return dict(n_seg=int(len(d)), media=float(mu), ic90_inf=float(lo), p_t=float(p), dias_pos=int((d > 0).sum()), frac_pos=float((d > 0).mean()), sin2=float(s[:-2].mean()))
def celda(nm, m):
    df = pd.DataFrame({'seg': (dia[m] + '|' + ep[m]).astype(object), 'mid': mid[m], 'lado': lado[m], 'code': codes(P['F5_' + nm].values[m]), 'pnl': pnl[m], 'co': co[m], 'sid': sid_all[m]})
    U = df.groupby(['seg', 'mid', 'lado', 'code'], sort=True).agg(pnl=('pnl', 'sum'), co=('co', 'sum'), sid=('sid', 'first'), nsid=('sid', 'nunique'), n=('pnl', 'size')).reset_index()
    assert (U.nsid == 1).all(), 'unidad mercado-lado-tercil con mas de un estrato dia x moneda x hora'
    seg, segn = pd.factorize(U.seg.values); ns = len(segn); code = U.code.values.astype(np.int8); pu = U.pnl.values.astype(float); cu = U.co.values.astype(float); assert (cu > 0).all(); ru = pu / cu
    ge, gu = g_eur(seg, code, pu, cu, ns), g_uni(seg, code, ru, ns); tt = {}
    for r, cs in (('todo', (0, 1, 2, 3)), ('bajo', (0,)), ('medio', (1,)), ('alto', (2,)), ('nan', (3,))):
        mu = np.isin(code, cs); tt[r] = dict(n_unid=int(mu.sum()), n_prints=int(U.n.values[mu].sum()), ev_eur=float(pu[mu].sum() / cu[mu].sum()) if mu.any() else np.nan, ev_unid=float(ru[mu].mean()) if mu.any() else np.nan)
    return dict(seg=seg.astype(np.int64), segn=[str(s) for s in segn], ns=ns, code=code, pu=pu, cu=cu, ru=ru, strata=pd.factorize(U.sid.values)[0], g_e=ge, g_u=gu, s_e=serie(ge), s_u=serie(gu), ter=tt,
                n_prints=int(m.sum()), n_unid=int(len(U)), n_ml=int(U.groupby(['mid', 'lado']).ngroups), n_dias=int(pd.Series(dia[m]).nunique()), n_cierres=int(pd.Series(cl[m]).nunique()))
def placebo(Cs, seed):
    rng = np.random.default_rng(seed); de = {k: np.empty(B) for k in Cs}; du = {k: np.empty(B) for k in Cs}; o0 = {k: np.argsort(C['strata'], kind='stable') for k, C in Cs.items()}
    for b in range(B):
        for k, C in Cs.items():
            o = np.lexsort((rng.random(len(C['code'])), C['strata'])); Lp = np.empty_like(C['code']); Lp[o0[k]] = C['code'][o]
            ge = g_eur(C['seg'], Lp, C['pu'], C['cu'], C['ns']); gu = g_uni(C['seg'], Lp, C['ru'], C['ns'])
            de[k][b] = np.nanmean(ge) if np.isfinite(ge).any() else np.nan; du[k][b] = np.nanmean(gu) if np.isfinite(gu).any() else np.nan
    mxe = np.nanmax(np.vstack(list(de.values())), 0); mxu = np.nanmax(np.vstack(list(du.values())), 0)
    for k, C in Cs.items():
        oe, ou = C['s_e']['media'], C['s_u']['media']
        C['pl'] = dict(e_celda=float(np.nanmean(de[k] >= oe - 1e-12)), e_max=float(np.nanmean(mxe >= oe - 1e-12)), e_media=float(np.nanmean(de[k])), u_celda=float(np.nanmean(du[k] >= ou - 1e-12)), u_max=float(np.nanmean(mxu >= ou - 1e-12)), u_media=float(np.nanmean(du[k])))
def lineas(k, C):
    t, se, su, pl = C['ter'], C['s_e'], C['s_u'], C['pl']; f = lambda x: f'{x:+.3f}' if x is not None and np.isfinite(x) else 'nan'
    return [f"{k}: prints {C['n_prints']} | unidades {C['n_unid']} ({C['n_ml']} mercado-lado) | {C['n_dias']} dias, {C['n_cierres']} cierres",
            f"   EV pond. EUR: todo {f(t['todo']['ev_eur'])} bajo {f(t['bajo']['ev_eur'])} medio {f(t['medio']['ev_eur'])} alto {f(t['alto']['ev_eur'])} | EV medio por unidad: todo {f(t['todo']['ev_unid'])} bajo {f(t['bajo']['ev_unid'])} medio {f(t['medio']['ev_unid'])} alto {f(t['alto']['ev_unid'])} | inversion (alto - todo): EUR {f(t['alto']['ev_eur'] - t['todo']['ev_eur'])}, unidad {f(t['alto']['ev_unid'] - t['todo']['ev_unid'])}",
            f"   gradiente EUR diario {f(se['media'])} IC90 dias inf {f(se['ic90_inf'])} (p_t {se['p_t']:.3f}) dias+ {se['dias_pos']}/{se['n_seg']} sin 2 mejores {f(se['sin2'])} | placebo por unidad: p celda {pl['e_celda']:.3f} maxstat {pl['e_max']:.3f} (media placebo {f(pl['e_media'])})",
            f"   gradiente por unidad diario {f(su['media'])} IC90 dias inf {f(su['ic90_inf'])} (p_t {su['p_t']:.3f}) dias+ {su['dias_pos']}/{su['n_seg']} sin 2 mejores {f(su['sin2'])} | placebo por unidad: p celda {pl['u_celda']:.3f} maxstat {pl['u_max']:.3f} (media placebo {f(pl['u_media'])})"]
def limpio(C): return {k: v for k, v in C.items() if k not in ('seg', 'code', 'pu', 'cu', 'ru', 'strata', 'g_e', 'g_u')} | dict(serie_eur=dict(zip(C['segn'], np.round(C['g_e'], 4).tolist())), serie_unid=dict(zip(C['segn'], np.round(C['g_u'], 4).tolist())))
RES = {'decisivas_unidad': {}, 'sensibilidad_suelo': {}, 'dias_add2': {}, 'regresion_C10': {}}
# ================= (1)+(2) celdas decisivas de ADD1 (35 dias; nunca los dias ADD2) =================
DEC = {}
for nm in ('p35', 'p60'):
    for e in ('R1', 'R2'):
        k = f'{nm}|{e}'; m = (ep == e) & tipoB(nm) & ~add2
        if m.sum() < 50: RES['decisivas_unidad'][k] = dict(etiqueta='DATA_BLOCKED (< 50 prints)'); continue
        C = celda(nm, m); sr = REF[k]['serie']; bad = []
        for s, v in zip(C['segn'], C['g_e']):
            r = sr.get(s, 'ausente')
            if r == 'ausente': bad.append((s, 'ausente en ADD1')); continue
            if not np.isfinite(r) and not np.isfinite(v): continue
            if not (np.isfinite(r) and np.isfinite(v) and abs(float(v) - r) <= 0.0006): bad.append((s, v, r))
        if not SM:
            if set(C['segn']) != set(sr): bad.append(('segmentos distintos', sorted(set(C['segn']) ^ set(sr))[:5]))
            if C['n_prints'] != REF[k]['n_prints']: bad.append(('n_prints', C['n_prints'], REF[k]['n_prints']))
        assert not bad, f'C10 regresion ADD1 {k}: {bad[:4]}'
        RES['regresion_C10'][k] = f"OK: {len(C['segn'])} segmentos reproducidos (|d| <= 0,0006), n_prints {C['n_prints']}" + ('' if SM else ' = ADD1'); DEC[k] = C
placebo(DEC, 20261116)
txt += ['', f"## (1) Regresion C10 frente a E2_poblacion.json (ADD1): " + '; '.join(f'{k} {v}' for k, v in RES['regresion_C10'].items()),
        '', f'## (2) DECISIVAS de ADD1 con unidad mercado-lado (35 dias, tipo B, todo el 5m). Placebo por UNIDAD B={B}, max-stat K=4; regla §4: VALIDADA se mantiene solo si placebo unidad maxstat <= 0,0125 y gradiente por unidad > 0']
nval = 0
for k, C in DEC.items():
    lab1 = REF[k]['etiqueta']; pl, su = C['pl'], C['s_u']; mot = []
    if lab1.startswith('VALIDADA'):
        if not pl['e_max'] <= 0.0125: mot.append(f"placebo por unidad maxstat {pl['e_max']:.3f} > 0,0125")
        if not (np.isfinite(su['media']) and su['media'] > 0): mot.append(f"gradiente por unidad {su['media']:+.3f} <= 0")
        lab2 = lab1 if not mot else 'EXPLORATORIA (sensible a la unidad mercado-lado: ' + '; '.join(mot) + ')'
        if not mot and not (np.isfinite(su['ic90_inf']) and su['ic90_inf'] > 0): lab2 += ' [nota: IC90 por dias del gradiente por unidad cruza 0]'
    else: lab2 = lab1
    nval += lab2.startswith('VALIDADA'); C['etiqueta_add1'], C['etiqueta_add2'] = lab1, lab2; C['placebo_print_add1'] = dict(celda=REF[k]['p_placebo_celda'], maxstat=REF[k]['p_placebo_maxstat'])
    txt += lineas(k, C) + [f"   placebo por PRINT (ADD1): p celda {REF[k]['p_placebo_celda']:.3f} maxstat {REF[k]['p_placebo_maxstat']:.3f} | etiqueta ADD1 -> ADD2: {lab1} -> {lab2}"]; RES['decisivas_unidad'][k] = limpio(C)
# ================= (3) sensibilidad §2: celdas por clase de suelo con los 37 dias (descriptivo) =================
SEN = {}
for nm in ('p35', 'p60'):
    for cls_, eps in (('hi', ('R1', 'R0hi', 'R2hi')), ('lo', ('R2', 'R1lo'))):
        m = np.isin(ep, eps) & tipoB(nm)
        if m.sum() >= 50: SEN[f'{nm}|suelo_{cls_}'] = celda(nm, m)
if SEN: placebo(SEN, 20261117)
txt += ['', f'## (3) SENSIBILIDAD §2 (no decide): celdas por clase de suelo medido, 37 dias (hi = R1 + R0hi + R2hi; lo = R2 + R1lo); placebo por unidad B={B}, max-stat sobre estas 4']
for k, C in SEN.items(): txt += lineas(k, C); RES['sensibilidad_suelo'][k] = limpio(C)
txt += ['', '## (3b) Gradiente propio de los dias ADD2 (tipo B, todo el 5m, por segmento dia-etiqueta; EUR / por unidad)']
for d in DIAS_ADD2:
    for nm in ('p35', 'p60'):
        m = (dia == d) & tipoB(nm) & (ep != 'indet')
        if m.sum() < 50: txt.append(f'{d} {nm}: {int(m.sum())} prints tipo B (< 50; sin dato)'); continue
        C = celda(nm, m); RES['dias_add2'][f'{d}|{nm}'] = limpio(C)
        txt.append(f"{d} {nm}: prints {C['n_prints']} unidades {C['n_unid']} | " + ', '.join(f"{s}: EUR {ge:+.3f} unidad {gu:+.3f}" for s, ge, gu in zip(C['segn'], C['g_e'], C['g_u'])) + f" | EV EUR bajo {C['ter']['bajo']['ev_eur']:+.3f} alto {C['ter']['alto']['ev_eur']:+.3f}")
txt += ['', f"RESUMEN: {nval}/4 celdas decisivas VALIDADAS tras ADD2; " + '; '.join(f"{k} -> {C['etiqueta_add2']}" for k, C in DEC.items()) + ('' if COMPLETO else ' | PARTIAL'),
        f"Tiempo {time.time() - t0:.0f} s. Limites: poblacion censurada (solo fills ajenos; gradiente, NO EV de regla), d_proc = 3 ms supuesto, sin ancla independiente del reloj de relleno propio; dias ADD2 solo en sensibilidad."]
write(OUT + '.txt', txt); json.dump(RES, open(OUT + '.json', 'w'), default=float, indent=1)
if not SM: estado_fase('E2agg_add2', 'COMPLETE' if COMPLETO else 'PARTIAL', celdas_validadas=nval, dias_complete=len(por.get('COMPLETE', [])), dias_add2=[d for d in DIAS_ADD2 if est[d] == ('COMPLETE', DET_ADD2)])
print('\n'.join(txt))
