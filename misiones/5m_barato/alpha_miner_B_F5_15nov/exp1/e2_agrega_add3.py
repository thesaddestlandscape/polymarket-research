#!/usr/bin/env python3
"""e2_agrega_add3.py [--smoke D1,D2] -- ADDENDUM3 (sha en ../ADDENDUM3_B_F5.sha256): F5 por CLASE DE SUELO MEDIDA (no por calendario) en los 35 dias decisivos.
Poblacion CENSURADA (solo prints = fills ajenos): gradiente, NO EV de regla. Solo sensibilidad: no sube etiquetas; todo «no validado»; ningun negativo es REJECTED.
Reloj: sello r_v3 = t_ev(EX) - 19 - 1 (passT_v3, rama constante); decision con estado q de RX <= t_dec; clase causal = ventana RX de 10 min cerrada antes de r_ex - 200 ms.
Tablas §3: (f) reproduccion desde crudo frente a las caches ADD1, (a) contaminacion, (b) celdas por clase causal con placebo por unidad, (c) calendario x clase,
(d) celdas ADD1 en ventanas puras, (e) clase concurrente (ADD2); criterio §4 «F5 robusta a la epoca». Solo lectura de caches; sin red."""
import os, sys, time, json, hashlib; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popdata import *
ADD3_SHA = open(AQ + 'ADDENDUM3_B_F5.sha256').read().split()[0]; assert hashlib.sha256(open(AQ + 'ADDENDUM3_B_F5.md', 'rb').read()).hexdigest() == ADD3_SHA, 'ADDENDUM3 modificado tras el sellado'
t0 = time.time(); SM = '--smoke' in sys.argv; B = 20 if SM else 1000
D35 = [d for d in dias_esperados() if d not in ('2026-10-16', '2026-10-24')]; assert len(D35) == 35
DIAS = sys.argv[sys.argv.index('--smoke') + 1].split(',') if SM else D35
OUT = EXP + ('smoke_' if SM else '') + 'E2_clase_suelo_add3'; REF = json.load(open(EXP + 'E2_poblacion.json'))['decisivas']
KEEP = BASE + ['epoca_ts', 'p5w'] + [f'{a}_{s}' for s in ('p35', 'p60') for a in ('F5', 'bid', 'cat')]
CLS_DE = {'R0': 'lo', 'R2': 'lo', 'R1lo': 'lo', 'R1': 'hi', 'R0hi': 'hi', 'R2hi': 'hi', 'indet': 'indet'}
def clase(p5): p5 = np.asarray(p5, float); return np.where(~np.isfinite(p5), 'indet', np.where(np.abs(p5 - 19.25) <= 5, 'lo', np.where(np.abs(p5 - 39.5) <= 5, 'hi', 'indet'))).astype(object)
parts, est, rep, VW = [], {}, {}, {}
for d in DIAS:
    mp, pk = CACHE + f'pob_add3_{d}.json', CACHE + f'{d}_pob_add3.pkl.gz'
    if not os.path.exists(mp): est[d] = 'FALTA'; continue
    m = json.load(open(mp))
    if m.get('estado') != 'COMPLETE' or m.get('addendum') != ADD3_SHA[:8] or not os.path.exists(pk): est[d] = f"{m.get('estado')} {(m.get('error') or '')[:80]}"; continue
    X = pd.read_pickle(pk, compression='gzip'); X = X[[c for c in KEEP if c in X.columns]].copy()
    for c in ('dia', 'coin', 'epoca', 'mid', 'lado_m', 'epoca_ts'): X[c] = X[c].astype(str)
    A = pd.read_pickle(CACHE + f'{d}_pob.pkl.gz', compression='gzip'); K = ['r_ex', 'r_rx', 'mid', 'lado_m', 'q', 'acc']; bad = []     # (f) reproduccion desde crudo
    if len(A) != len(X): bad.append(f'n ADD1 {len(A)} vs ADD3 {len(X)}')
    else:
        for c in ('mid', 'lado_m', 'coin', 'epoca'): A[c] = A[c].astype(str)
        a = A.sort_values(K, kind='mergesort').reset_index(drop=True); x = X.sort_values(K, kind='mergesort').reset_index(drop=True)
        bad += [c for c in ('r_ex', 'r_rx', 'q', 'acc', 'gana', 'pnl', 'coste', 'fin') if not np.array_equal(a[c].values, x[c].values)] + [c for c in ('mid', 'lado_m', 'coin') if not (a[c].values == x[c].values).all()]
        for c in ('F5_p35', 'F5_p60', 'bid_p35', 'bid_p60'):
            u, v = a[c].values.astype(float), x[c].values.astype(float); ok = (np.isnan(u) & np.isnan(v)) | (np.abs(u - v) <= 1e-6)
            if not ok.all(): bad.append(f'{c}({int((~ok).sum())})')
        if not (a.epoca.values == x.epoca_ts.values).all(): bad.append('epoca')
    rep[d] = 'OK' if not bad else 'DIFIERE: ' + ', '.join(bad); del A
    if bad: est[d] = 'NO_REPRODUCE'; continue
    cw = clase([np.nan if v is None else v for v in m['C3_suelo_rx_menos_ex']['perfil_p5_10min']]); day0 = ms(d + 'T00:00:00Z')
    wc = (X.r_ex.values.astype(np.int64) - 200 - day0) // 600000 - 1; X['cl_c'] = np.where((wc >= 0) & (wc < 144), cw[np.clip(wc, 0, 143)], 'indet').astype(str); X['cl_w'] = clase(X.p5w.values).astype(str)
    assert (X.epoca.map(CLS_DE).values == X.cl_w.values).all(), f'{d}: etiqueta ADD3 incoherente con la clase concurrente'
    VW[d] = cw; parts.append(X); est[d] = 'COMPLETE'
ok_d = [d for d in DIAS if est.get(d) == 'COMPLETE']; COMPLETO = (not SM) and len(ok_d) == 35
txt = [f"# E2 ADD3: F5 por clase de suelo medida (ADDENDUM1 {ADD_SHA[:8]} + ADDENDUM3 {ADD3_SHA[:8]}) -- CENSURADA, solo sensibilidad, TODO «no validado»" + (f" [SMOKE {','.join(DIAS)}, B={B}]" if SM else ''),
       f"Dias: {len(ok_d)}/{len(DIAS)} COMPLETE" + ('' if len(ok_d) == len(DIAS) else ' | no COMPLETE: ' + '; '.join(f'{d}[{e}]' for d, e in est.items() if e != 'COMPLETE')) + f" | estado {'COMPLETO 35/35' if COMPLETO else 'PARTIAL'}",
       f"(f) Reproduccion desde crudo (m5_registro re-extraido) frente a las caches ADD1: {sum(v == 'OK' for v in rep.values())}/{len(rep)} dias identicos print a print" + ''.join(f' | {d}: {v}' for d, v in rep.items() if v != 'OK')]
RES = dict(dias_ok=ok_d, estado_dias=est, reproduccion=rep)
if not parts:
    txt.append('DATA_BLOCKED: ninguna cache ADD3 utilizable'); write(OUT + '.txt', txt)
    if not SM: estado_fase('E2agg_add3', 'DATA_BLOCKED')
    print('\n'.join(txt)); sys.exit(2)
P = pd.concat(parts, ignore_index=True); del parts
dia = P.dia.to_numpy(dtype=object); cal = P.epoca_ts.to_numpy(dtype=object); clc = P.cl_c.to_numpy(dtype=object); clw = P.cl_w.to_numpy(dtype=object); coin = P.coin.to_numpy(dtype=object); hora = P.hora.values.astype(int)
pnl = P.pnl.values.astype(float); co = P.coste.values.astype(float); q = P.q.values.astype(float); cl = P.fin.values.astype(np.int64); mid = P.mid.to_numpy(dtype=object); lado = P.lado_m.to_numpy(dtype=object)
sid_all = pd.factorize(pd.MultiIndex.from_arrays([dia, coin, hora]))[0]
def codes(f5): t = ter(f5); return np.select([t == 'bajo', t == 'medio', t == 'alto'], [0, 1, 2], 3).astype(np.int8)
def tipoB(nm): b = P['bid_' + nm].values.astype(float); return np.isfinite(b) & ((b - q) >= 0.0099 - 1e-12)
def g_eur(seg, c, p_, k_, ns):
    mb, ma = c == 0, c == 2; cb = np.bincount(seg[mb], k_[mb], ns); ca = np.bincount(seg[ma], k_[ma], ns); sb = np.bincount(seg[mb], p_[mb], ns); sa = np.bincount(seg[ma], p_[ma], ns)
    g = np.full(ns, np.nan); ok = (cb > 0) & (ca > 0); g[ok] = sb[ok] / cb[ok] - sa[ok] / ca[ok]; return g
def g_uni(seg, c, r_, ns):
    mb, ma = c == 0, c == 2; nb = np.bincount(seg[mb], None, ns); na = np.bincount(seg[ma], None, ns); sb = np.bincount(seg[mb], r_[mb], ns); sa = np.bincount(seg[ma], r_[ma], ns)
    g = np.full(ns, np.nan); ok = (nb > 0) & (na > 0); g[ok] = sb[ok] / nb[ok] - sa[ok] / na[ok]; return g
def serie(g):
    d = g[np.isfinite(g)]; o = dict(n_seg=int(len(d)), media=float(np.mean(d)) if len(d) else np.nan, ic90_inf=np.nan, p_t=np.nan, dias_pos=int((d > 0).sum()), frac_pos=float((d > 0).mean()) if len(d) else np.nan, sin2=np.nan, n_req=np.nan)
    if len(d) >= 3:
        lo, p, mu = t_ic(d); s = np.sort(d); sd = float(np.std(d, ddof=1)); o.update(media=float(mu), ic90_inf=float(lo), p_t=float(p), sin2=float(s[:-2].mean()), n_req=float((1.645 * sd / mu) ** 2) if mu > 0 else np.nan)
    return o
def celda(nm, m, segl):
    df = pd.DataFrame({'seg': segl[m], 'mid': mid[m], 'lado': lado[m], 'code': codes(P['F5_' + nm].values[m]), 'pnl': pnl[m], 'co': co[m], 'sid': sid_all[m]})
    U = df.groupby(['seg', 'mid', 'lado', 'code'], sort=True).agg(pnl=('pnl', 'sum'), co=('co', 'sum'), sid=('sid', 'first'), nsid=('sid', 'nunique'), n=('pnl', 'size')).reset_index()
    assert (U.nsid == 1).all(), 'unidad con mas de un estrato dia x moneda x hora'
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
f3 = lambda x: f'{x:+.3f}' if x is not None and np.isfinite(x) else 'nan'
def lineas(k, C):
    t, se, su, pl = C['ter'], C['s_e'], C['s_u'], C.get('pl'); L = [f"{k}: prints {C['n_prints']} | unidades {C['n_unid']} ({C['n_ml']} mercado-lado) | {C['n_dias']} dias, {C['n_cierres']} cierres",
        f"   EV pond. EUR: todo {f3(t['todo']['ev_eur'])} bajo {f3(t['bajo']['ev_eur'])} medio {f3(t['medio']['ev_eur'])} alto {f3(t['alto']['ev_eur'])} | EV por unidad: todo {f3(t['todo']['ev_unid'])} bajo {f3(t['bajo']['ev_unid'])} alto {f3(t['alto']['ev_unid'])} | inversion (alto-todo) EUR {f3(t['alto']['ev_eur'] - t['todo']['ev_eur'])}"]
    for nmb, s, pk in (('EUR', se, 'e'), ('unidad', su, 'u')):
        L.append(f"   gradiente {nmb} diario {f3(s['media'])} IC90 dias inf {f3(s['ic90_inf'])} dias+ {s['dias_pos']}/{s['n_seg']} sin 2 mejores {f3(s['sin2'])}" + (f" | placebo unidad p celda {pl[pk + '_celda']:.3f} maxstat {pl[pk + '_max']:.3f} (media {f3(pl[pk + '_media'])})" if pl else ''))
    return L
def limpio(C): return {k: v for k, v in C.items() if k not in ('seg', 'code', 'pu', 'cu', 'ru', 'strata', 'g_e', 'g_u')} | dict(serie_eur=dict(zip(C['segn'], np.round(C['g_e'], 4).tolist())), serie_unid=dict(zip(C['segn'], np.round(C['g_u'], 4).tolist())))
def rangos(hs):
    o = []
    for h in sorted(set(int(x) for x in hs)):
        if o and h == o[-1][1] + 1: o[-1][1] = h
        else: o.append([h, h])
    return ','.join(f'{a:02d}' if a == b else f'{a:02d}-{b:02d}' for a, b in o) or '-'
# ---------------- (a) contaminacion
txt += ['', '## (a) CONTAMINACION de las celdas decisivas de ADD1 (epoca por calendario) segun la clase CAUSAL medida (esperado R1 -> hi, R2 -> lo); tipo B, todo el 5m']; RES['contaminacion'] = {}
for nm in ('p35', 'p60'):
    for e, esp in (('R1', 'hi'), ('R2', 'lo')):
        m = (cal == e) & tipoB(nm); c_, w_ = clc[m], co[m]; sh = {k: (float(np.mean(c_ == k)), float(w_[c_ == k].sum() / w_.sum())) for k in ('hi', 'lo', 'indet')}
        g = pd.DataFrame({'mid': mid[m], 'lado': lado[m], 'c': c_}).groupby(['mid', 'lado']).c.first(); shm = {k: float((g == k).mean()) for k in ('hi', 'lo', 'indet')}; otra = 'lo' if esp == 'hi' else 'hi'
        RES['contaminacion'][f'{nm}|{e}'] = dict(prints=int(m.sum()), cuota_prints=sh, cuota_mercado_lado=shm)
        txt.append(f"{nm}|{e}: prints {int(m.sum())} | clase esperada {esp}: {100*sh[esp][0]:.1f} % prints, {100*sh[esp][1]:.1f} % EUR, {100*shm[esp]:.1f} % mercado-lado | CONTAMINACION ({otra}): {100*sh[otra][0]:.1f} % prints, {100*sh[otra][1]:.1f} % EUR | indet {100*sh['indet'][0]:.1f} %")
txt.append('Ventanas de 10 min por dia (clase medida) y horas UTC con clase inesperada para su epoca de calendario:')
for d in ok_d:
    cw = VW[d]; ecal = epoca(ms(d + 'T00:00:00Z') + np.arange(144) * 600000 + 300000); esp = np.where(ecal == 'R1', 'hi', 'lo'); ine = (cw != esp) & (cw != 'indet')
    txt.append(f"  {d}: lo {int((cw == 'lo').sum())} hi {int((cw == 'hi').sum())} indet {int((cw == 'indet').sum())} | inesperada {int(ine.sum())} ventanas, horas {rangos(np.where(ine)[0] // 6) if ine.any() else '-'}")
# ---------------- (b) celdas por clase causal (decide el criterio §4) y (c) calendario x clase
segc = (dia + '|' + clc).astype(object); CB = {}
for nm in ('p35', 'p60'):
    for k in ('hi', 'lo'):
        m = (clc == k) & tipoB(nm)
        if m.sum() >= 50: CB[f'{nm}|{k}'] = celda(nm, m, segc)
if CB: placebo(CB, 20261118)
txt += ['', f'## (b) CELDAS POR CLASE DE SUELO CAUSAL (35 dias decisivos; segmento = dia x clase; placebo por unidad B={B}, max-stat sobre estas celdas)']
for k, C in CB.items(): txt += lineas(k, C)
RES['clase_causal'] = {k: limpio(C) for k, C in CB.items()}
txt += ['', '## (c) CALENDARIO x CLASE CAUSAL (descriptivo; gradiente diario pond. EUR)']
for nm in ('p35', 'p60'):
    for e in ('R0', 'R1', 'R2'):
        for k in ('lo', 'hi'):
            m = (cal == e) & (clc == k) & tipoB(nm)
            if m.sum() < 50: txt.append(f'  {nm} {e}-{k}: {int(m.sum())} prints (< 50)'); continue
            sg, sn = pd.factorize(dia[m]); s = serie(g_eur(sg, codes(P['F5_' + nm].values[m]), pnl[m], co[m], len(sn))); txt.append(f"  {nm} {e}-{k}: prints {int(m.sum())} dias {s['n_seg']} | gradiente EUR diario {f3(s['media'])} IC90 inf {f3(s['ic90_inf'])} dias+ {s['dias_pos']}/{s['n_seg']}")
# ---------------- (d) celdas decisivas de ADD1 en ventanas puras
segl = (dia + '|' + cal).astype(object); CP = {}
for nm in ('p35', 'p60'):
    for e, k in (('R1', 'hi'), ('R2', 'lo')):
        m = (cal == e) & (clc == k) & tipoB(nm)
        if m.sum() >= 50: CP[f'{nm}|{e}_puro'] = celda(nm, m, segl)
if CP: placebo(CP, 20261119)
txt += ['', f'## (d) CELDAS DECISIVAS DE ADD1 EN VENTANAS PURAS (R1 con clase causal hi; R2 con lo); placebo por unidad B={B}, max-stat sobre estas 4; entre corchetes ADD1 (calendario, contaminada)']
for k, C in CP.items():
    r = REF.get(k.replace('_puro', ''), {}); txt += lineas(k, C) + [f"   [ADD1: gradiente EUR diario {f3(r.get('grad_media_dia'))} IC90 inf {f3(r.get('ic90_dias_inf'))} dias+ {r.get('dias_pos')}/{r.get('n_segmentos')} sin 2 mejores {f3(r.get('sin2mejores'))} placebo print maxstat {r.get('p_placebo_maxstat')} -> {r.get('etiqueta')}]"]
RES['puras'] = {k: limpio(C) for k, C in CP.items()}
# ---------------- (e) clase concurrente (ADD2; mira hasta 10 min hacia delante)
segw = (dia + '|' + clw).astype(object); CW = {}
for nm in ('p35', 'p60'):
    for k in ('hi', 'lo'):
        m = (clw == k) & tipoB(nm)
        if m.sum() >= 50: CW[f'{nm}|{k}_concurrente'] = celda(nm, m, segw)
txt += ['', '## (e) CLASE CONCURRENTE (definicion ADD2; descriptivo, sin placebo)']
for k, C in CW.items(): txt += lineas(k, C)
RES['clase_concurrente'] = {k: limpio(C) for k, C in CW.items()}
# ---------------- criterio §4 y regla §5
def criterio(nm):
    h, l = CB.get(f'{nm}|hi'), CB.get(f'{nm}|lo')
    if h is None or l is None: return 'INSUFFICIENT (falta una clase)'
    sh, sl = h['s_e'], l['s_e']
    if min(sh['n_seg'], sl['n_seg']) < 5: return f"INSUFFICIENT (dias hi {sh['n_seg']}, lo {sl['n_seg']}; < 5)"
    if all(np.isfinite(s['ic90_inf']) and s['media'] > 0 and s['ic90_inf'] > 0 and s['sin2'] > 0 for s in (sh, sl)):
        return 'ROBUSTA A LA EPOCA' if max(h['pl']['e_max'], l['pl']['e_max']) <= 0.0125 else f"EXPLORATORY (signo robusto, placebo no superado: maxstat hi {h['pl']['e_max']:.3f}, lo {l['pl']['e_max']:.3f})"
    nr = f"n dias requerido hi {sh['n_req']:.0f}, lo {sl['n_req']:.0f}"
    return f"EXPLORATORY (media > 0 en ambas clases; {nr})" if sh['media'] > 0 and sl['media'] > 0 else f"INSUFFICIENT (media hi {f3(sh['media'])}, lo {f3(sl['media'])}; {nr})"
CRIT = {nm: criterio(nm) + ' -- sensibilidad ADD3, NO VALIDADO' for nm in ('p35', 'p60')}; RES['criterio_robustez'] = CRIT
d60 = CP.get('p60|R2_puro'); reb = d60 is not None and not (d60['s_e']['media'] > 0 and np.isfinite(d60['s_e']['ic90_inf']) and d60['s_e']['ic90_inf'] > 0)
RES['rebaja_p60R2'] = bool(reb)
txt += ['', '## CRITERIO §4 «F5 robusta a la epoca» (hi y lo por separado: media diaria > 0, IC90 por dias inf > 0, sin 2 mejores > 0; placebo por unidad max-stat <= 0,0125)'] + [f'l_ef {nm[1:]} ms: {v}' for nm, v in CRIT.items()]
txt += [f"Regla §5 (p60|R2 en ventanas puras): {'REBAJA la etiqueta VALIDADA de ADD1/ADD2 a EXPLORATORY' if reb else 'no obliga a rebajar (sigue «no validado» hasta la revision independiente)'}",
        '', f"RESUMEN: dias {len(ok_d)}/35, reproduccion desde crudo {sum(v == 'OK' for v in rep.values())}/{len(rep)}; robustez p35 -> {CRIT['p35']}; p60 -> {CRIT['p60']}." + ('' if COMPLETO else ' PARTIAL.'),
        f"Tiempo {time.time() - t0:.0f} s. Limites: poblacion censurada (gradiente, no EV de regla); d_proc = 3 ms supuesto; causa de la alternancia del suelo INSUFICIENTE; clase causal con margen de 200 ms."]
write(OUT + '.txt', txt); json.dump(RES, open(OUT + '.json', 'w'), default=float, indent=1)
if not SM: estado_fase('E2agg_add3', 'COMPLETE' if COMPLETO else 'PARTIAL', dias_ok=len(ok_d), no_reproduce=[d for d, v in rep.items() if v != 'OK'], robustez=CRIT, rebaja_p60R2=bool(reb))
print('\n'.join(txt))
