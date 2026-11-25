#!/usr/bin/env python3
"""E2 agregado (ADDENDUM1 §3 E2): gradiente de la POBLACION (prints bid en banda, ETH/SOL/XRP, desenlace oficial, CENSURADA: solo prints = fills ajenos) por tercil de F5 con r_v3 = r_ex - 19 - 1 y t_dec = r_v3 - l_ef - d_proc.
Decisivo (K_pop = 4): spec p35/p60 x epoca R1/R2, tipo B (bid(t_dec)-q >= 0,0099), TODO el 5m: gradiente bajo-alto por segmento dia-epoca (pond. por EUR), media > 0, IC90 por dias (t, inf) > 0, >= 2/3 de dias +,
placebo max-statistic (permutacion de etiquetas dentro de dia x moneda x hora, B=1000, claves independientes por celda = conservador) p <= 0,0125. Todo lo demas es DESCRIPTIVO. La poblacion es censurada: gradiente, NO EV de regla.
Un dia FAILED/PENDING/FALTA se lista y el resultado se rotula PARTIAL. Solo lectura de caches; sin red."""
import os, sys, time; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from popdata import *
t0 = time.time(); P, est = carga_pob(); cobL, por = resumen_cobertura(est); COMPLETO = len(por.get('COMPLETE', [])) == len(est)
txt = [f'# E2 poblacion con r_v3 (ADDENDUM1 sha {ADD_SHA[:8]}) -- CENSURADA: solo gradiente, NO EV de regla'] + cobL + [f'Estado: {"COMPLETO" if COMPLETO else "PARTIAL (dias no COMPLETE listados arriba)"}; prints {len(P)} (ETH/SOL/XRP, q en (0,10;0,30], desenlace oficial cobertura >= 0,995 por dia)']
if len(P) == 0: txt.append('DATA_BLOCKED: ninguna cache COMPLETE'); write(EXP + 'E2_poblacion.txt', txt); estado_fase('E2agg', 'DATA_BLOCKED'); print('\n'.join(txt)); sys.exit(2)
dia = P.dia.to_numpy(dtype=object); dias_u, dia_i = np.unique(dia, return_inverse=True); ep = P.epoca.to_numpy(dtype=object); coin = P.coin.to_numpy(dtype=object); hora = P.hora.values.astype(int)
pnl = P.pnl.values.astype(float); co = P.coste.values.astype(float); q = P.q.values.astype(float); cl = P.fin.values.astype(np.int64); trem = cl - P.r_ex.values / 1000.0
sid_all = pd.factorize(pd.MultiIndex.from_arrays([dia, coin, hora]))[0]
txt.append('Prints por epoca: ' + str({e: int((ep == e).sum()) for e in ('R0', 'R1', 'R2')}) + ' | por moneda: ' + str({c: int((coin == c).sum()) for c in ('ETH', 'SOL', 'XRP')}))
for nm in ('p35', 'p60', 'p100', 'p150'):                       # composicion de categorias NaN (C5: se cuentan, no se descartan)
    c = P['cat_' + nm].values; txt.append(f'Categorias de estado q en t_dec ({nm}): ' + ', '.join(f"{CATN[k]} {100*np.mean(c == k):.1f} %" for k in range(4)) + ' | por epoca "ok": ' + ', '.join(f"{e} {100*np.mean(c[ep == e] == 0):.1f} %" for e in ('R0', 'R1', 'R2') if (ep == e).any()))
def codes(f5):
    t = ter(f5); return np.select([t == 'bajo', t == 'medio', t == 'alto'], [0, 1, 2], 3).astype(np.int8)
def mask(nm, e, tipoB, trem_min=None, d0=None, d1=None):
    m = np.ones(len(P), bool) if e in (None, 'all') else (ep == e)
    if tipoB: b = P['bid_' + nm].values.astype(float); m &= np.isfinite(b) & ((b - q) >= 0.0099 - 1e-12)
    if trem_min is not None: m &= trem > trem_min
    if d0: m &= dia >= d0
    if d1: m &= dia <= d1
    return m
def frame(nm, m): return pd.DataFrame({'ter': ter(P['F5_' + nm].values[m]), 'pnl': pnl[m], 'coste': co[m], 'cl': cl[m], 'dia': dia[m]})
def seg_grad(L, a):
    mb, ma = L == 0, L == 2; ns = a['ns']; cb = np.bincount(a['seg'][mb], a['co'][mb], ns); ca = np.bincount(a['seg'][ma], a['co'][ma], ns)
    sb = np.bincount(a['seg'][mb], a['pnl'][mb], ns); sa = np.bincount(a['seg'][ma], a['pnl'][ma], ns); g = np.full(ns, np.nan); ok = (cb > 0) & (ca > 0); g[ok] = sb[ok] / cb[ok] - sa[ok] / ca[ok]; return g
def cell_arrays(nm, m):
    seg, segn = pd.factorize(dia[m] + '|' + ep[m]); return dict(code=codes(P['F5_' + nm].values[m]), pnl=pnl[m], co=co[m], seg=seg.astype(np.int64), ns=len(segn), segn=list(segn), sid=pd.factorize(sid_all[m])[0], cl=cl[m])
def stats_cell(a, nm, label):
    g = seg_grad(a['code'], a); d = g[np.isfinite(g)]; lo, p, mu = t_ic(d) if len(d) >= 3 else (np.nan, np.nan, np.nan); srt = np.sort(d)
    df = pd.DataFrame({'ter': np.select([a['code'] == 0, a['code'] == 1, a['code'] == 2], ['bajo', 'medio', 'alto'], 'nan'), 'pnl': a['pnl'], 'coste': a['co'], 'cl': a['cl']}); gp, glo, ghi, sdb = boot_grad(df)
    ncl = int(pd.Series(a['cl']).nunique()); return dict(celda=label, n_prints=int(len(a['code'])), n_cierres=ncl, n_segmentos=int(len(d)), grad_media_dia=float(mu), ic90_dias_inf=float(lo), p_t=float(p), dias_pos=int((d > 0).sum()), frac_dias_pos=float((d > 0).mean()) if len(d) else np.nan,
                                                       sin2mejores=float(srt[:-2].mean()) if len(srt) > 2 else np.nan, grad_pooled=float(gp), ic90_cierre=(glo, ghi), sd_boot=sdb, n_req_cierres=n_req(ncl, gp, sdb), serie=dict(zip(a['segn'], np.round(g, 3).tolist())))
RES = {'decisivas': {}, 'descriptivas': {}}
# ================= DECISIVAS (K_pop = 4) =================
CEL = [(nm, e) for nm in ('p35', 'p60') for e in ('R1', 'R2')]; arrs = {}
for nm, e in CEL:
    m_ = mask(nm, e, True)
    if m_.sum() >= 50: arrs[f'{nm}|{e}'] = cell_arrays(nm, m_)
    else: RES['decisivas'][f'{nm}|{e}'] = dict(etiqueta='DATA_BLOCKED (< 50 prints tipo B en la celda)', n_prints=int(m_.sum()), cumple_gate=False)
B = 1000; rng = np.random.default_rng(20261115); dist = {k: np.empty(B) for k in arrs}; ord0 = {k: np.argsort(a['sid'], kind='stable') for k, a in arrs.items()}
for b in range(B):
    for k, a in arrs.items():
        ordr = np.lexsort((rng.random(len(a['code'])), a['sid'])); Lp = np.empty_like(a['code']); Lp[ord0[k]] = a['code'][ordr]; g = seg_grad(Lp, a); dist[k][b] = np.nanmean(g) if np.isfinite(g).any() else np.nan
mx = np.nanmax(np.vstack(list(dist.values())), axis=0) if dist else np.array([np.nan]); txt += ['', f'## DECISIVAS (K_pop=4; TODO el 5m; tipo B; gradiente = EV(bajo) - EV(alto) pond. EUR por segmento dia-epoca; placebo B={B}, claves independientes por celda (conservador); umbral p <= 0,0125)']
for nm, e in CEL:
    k = f'{nm}|{e}'
    if k not in arrs: txt.append(f"{k}: {RES['decisivas'][k]['etiqueta']}"); continue
    s = stats_cell(arrs[k], nm, k); obs = s['grad_media_dia']; s['p_placebo_celda'] = float(np.nanmean(dist[k] >= obs - 1e-12)); s['p_placebo_maxstat'] = float(np.nanmean(mx >= obs - 1e-12)); s['placebo_media'] = float(np.nanmean(dist[k]))
    ok = (obs > 0) and (s['ic90_dias_inf'] > 0) and (s['frac_dias_pos'] >= 2 / 3) and (s['p_placebo_maxstat'] <= 0.0125); s['cumple_gate'] = bool(ok)
    s['etiqueta'] = 'VALIDADA (gradiente poblacional censurado; NO EV de regla)' if ok else ('EXPLORATORIA' if (obs > 0 and s['frac_dias_pos'] >= 0.5) else ('INSUFFICIENT (gradiente <= 0 o < 50 % de dias +; no refuta: poblacion censurada)')); RES['decisivas'][k] = s
    txt.append(f"{k}: n={s['n_prints']} prints, {s['n_cierres']} cierres, {s['n_segmentos']} segmentos | grad media diaria {obs:+.3f} IC90 dias inf {s['ic90_dias_inf']:+.3f} p_t {s['p_t']:.3f} | dias+ {s['dias_pos']}/{s['n_segmentos']} ({100*s['frac_dias_pos']:.0f} %) | sin 2 mejores {s['sin2mejores']:+.3f} | pooled {s['grad_pooled']:+.3f} IC90 cierre ({s['ic90_cierre'][0]:+.3f},{s['ic90_cierre'][1]:+.3f}) | placebo celda p {s['p_placebo_celda']:.3f} (media {s['placebo_media']:+.3f}) maxstat p {s['p_placebo_maxstat']:.3f} -> {s['etiqueta']}" + (f" | n requerido {s['n_req_cierres']:.0f} cierres" if np.isfinite(s['n_req_cierres']) else ''))
    txt.append('    serie diaria bajo-alto: ' + ', '.join(f'{kk}:{v:+.2f}' for kk, v in s['serie'].items() if np.isfinite(v)))
# ================= DESCRIPTIVAS =================
txt += ['', '## DESCRIPTIVO 1: terciles de F5 por spec (l_ef) x epoca x poblacion (EV pond. EUR; IC90 por cierre por bootstrap; G1/G2/inv)']
for nm in ('p35', 'p60', 'p100', 'p150'):
    for e in ('R0', 'R1', 'R2', 'all'):
        for tb in (True, False):
            for tm in (None, 60):
                m = mask(nm, e, tb, tm)
                if m.sum() < 200: continue
                L, o = resumen(frame(nm, m), f"{nm} | epoca {e} | {'tipo B' if tb else 'todas'} | {'todo T' if tm is None else 'T_rem>60 s'}"); txt += L; RES['descriptivas'][f"{nm}|{e}|{'B' if tb else 'todas'}|{'T' if tm is None else 'T60'}"] = o
txt += ['', '## DESCRIPTIVO 2: sensibilidades (c=16/22, d_proc=10/30, delta=-/+suelo) a l_ef=35 y 60, tipo B, por epoca: terciles y gradiente agrupado (sin bootstrap; no deciden)']
for l in (35, 60):
    for pre_ in (f'p{l}', f'c16_{l}', f'c22_{l}', f'd10_{l}', f'd30_{l}', f'dm_{l}', f'dp_{l}'):
        for e in ('R1', 'R2'):
            m = mask(pre_, e, True); a = cell_arrays(pre_, m); g = seg_grad(a['code'], a); d = g[np.isfinite(g)]; f = frame(pre_, m); tt = {r: ev(f.pnl[f.ter == r], f.coste[f.ter == r]) for r in ('bajo', 'medio', 'alto')}
            txt.append(f"{pre_} {e}: n={int(m.sum())} | EV bajo {tt['bajo']:+.3f} medio {tt['medio']:+.3f} alto {tt['alto']:+.3f} | gradiente pooled {tt['bajo'] - tt['alto']:+.3f} | media diaria {np.nanmean(d) if len(d) else np.nan:+.3f} dias+ {(d > 0).sum()}/{len(d)}")
txt += ['', '## DESCRIPTIVO 3: periodos antiguos (INS 09-19 Oct, DER 24-Oct..03-Nov, OOS 04-14 Nov) y reproduccion de las columnas VIEJAS (tau = r_rx - lag, sin filas de ask vacio) frente a poblacion_por_tercil.txt (NO VALIDADO; solo para ver si cambia el signo)']
OLD = {('OOS', 100, 'todas'): (0.059, 0.007, -0.135), ('OOS', 100, 'B'): (0.129, 0.057, -0.132), ('OOS', 250, 'todas'): (0.056, -0.018, -0.122), ('OOS', 250, 'B'): (0.081, 0.020, -0.097),
       ('DER', 100, 'todas'): (0.132, 0.048, -0.033), ('DER', 100, 'B'): (0.389, 0.140, 0.113), ('DER', 250, 'todas'): (0.105, 0.060, -0.016), ('DER', 250, 'B'): (0.248, 0.137, 0.037)}
PER = {'INS': ('2026-10-09', '2026-10-19'), 'DER': ('2026-10-24', '2026-11-03'), 'OOS': ('2026-11-04', '2026-11-14')}
for per, (d0, d1) in PER.items():
    for nm, etq in (('o100', 'viejo tau=r_rx-100'), ('o250', 'viejo tau=r_rx-250'), ('p35', 'v3 l_ef=35'), ('p60', 'v3 l_ef=60'), ('p100', 'v3 l_ef=100'), ('p150', 'v3 l_ef=150')):
        for tb in (False, True):
            m = mask(nm, None, tb, None, d0, d1)
            if m.sum() < 200: continue
            f = frame(nm, m); t3 = {r: ev(f.pnl[f.ter == r], f.coste[f.ter == r]) for r in ('bajo', 'medio', 'alto')}; ref = OLD.get((per, int(nm[1:]), 'B' if tb else 'todas')) if nm in ('o100', 'o250') else None
            txt.append(f"{per} {d0}..{d1} | {etq} | {'tipo B' if tb else 'todas'}: n={int(m.sum())} cierres={f.cl.nunique()} | EV bajo {t3['bajo']:+.3f} medio {t3['medio']:+.3f} alto {t3['alto']:+.3f} | gradiente {t3['bajo'] - t3['alto']:+.3f}" + (f" | viejo archivo: {ref[0]:+.3f}/{ref[1]:+.3f}/{ref[2]:+.3f}" if ref else ''))
txt += ['', '## DESCRIPTIVO 4: gradiente por moneda (p60, tipo B, R1 y R2; pooled)']
for e in ('R1', 'R2'):
    for c in ('ETH', 'SOL', 'XRP'):
        m = mask('p60', e, True) & (coin == c); f = frame('p60', m); tt = {r: ev(f.pnl[f.ter == r], f.coste[f.ter == r]) for r in ('bajo', 'medio', 'alto')}; txt.append(f"{e} {c}: n={int(m.sum())} | bajo {tt['bajo']:+.3f} medio {tt['medio']:+.3f} alto {tt['alto']:+.3f} | gradiente {tt['bajo'] - tt['alto']:+.3f}")
dec = RES['decisivas']; ncum = sum(v['cumple_gate'] for v in dec.values())
txt += ['', f"RESUMEN: {ncum}/4 celdas decisivas cumplen el gate; etiquetas: " + '; '.join(f"{k} -> {v['etiqueta']}" for k, v in dec.items()) + ('' if COMPLETO else ' | PARTIAL: faltan dias'),
        f"Tiempo {time.time() - t0:.0f} s. Limites: poblacion censurada (solo fills ajenos), d_proc=3 ms supuesto, sin ancla independiente del reloj de relleno propio; segmentos dia-epoca (17-Oct y 27-Oct parciales)."]
write(EXP + 'E2_poblacion.txt', txt); json.dump(RES, open(EXP + 'E2_poblacion.json', 'w'), default=float, indent=1); estado_fase('E2agg', 'COMPLETE' if COMPLETO else 'PARTIAL', celdas_ok=ncum, dias_complete=len(por.get('COMPLETE', []))); print('\n'.join(txt))
