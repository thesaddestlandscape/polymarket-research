#!/usr/bin/env python3
"""t2_agrega_v4.py [--smoke D1,D2] -- SPEC_F5_V4_17nov.md T2/T3: celdas F5 (p35/p60 x lo/hi, tipo B) por CLASE CAUSAL v4 (suelo_causal, ventana movil de 10 min, excluye indet/mixta) frente a la clase causal de ADD3 (ventana alineada previa, control).
Grupos: ALL3 (ETH/SOL/XRP, caches ADD3 de exp1) y BTC (cache/btc_pob_D). Mismas formulas que e2_agrega_add3.py (celda/placebo/serie copiadas). Solo lectura de caches; sin red; 0 ordenes. Salida: T2_clase_suelo_v4.{txt,json}."""
import os, sys, time, json, hashlib, glob
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/exp1')
from popdata import *                                   # lib1: C0/C1, ter, t_ic, ms, epoca ...
import suelo_causal as SC
assert hashlib.sha256(open(HERE + '/SPEC_F5_V4_17nov.md', 'rb').read()).hexdigest() == open(HERE + '/SPEC_F5_V4_17nov.sha256').read().split()[0], 'SPEC modificada tras el sellado'
t0 = time.time(); SM = '--smoke' in sys.argv; B = 20 if SM else 1000; C4 = HERE + '/cache/'
D35 = [d for d in dias_esperados() if d not in ('2026-10-16', '2026-10-24')]; DIAS = sys.argv[sys.argv.index('--smoke') + 1].split(',') if SM else D35
OUT = HERE + ('/smoke_' if SM else '/') + 'T2_clase_suelo_v4'; REF = json.load(open(EXP + 'E2_clase_suelo_add3.json'))
def clase_p5(p5): p5 = np.asarray(p5, float); return np.where(~np.isfinite(p5), 'indet', np.where(np.abs(p5 - 19.25) <= 5, 'lo', np.where(np.abs(p5 - 39.5) <= 5, 'hi', 'indet'))).astype(object)
DIAS_ALL = [d for d in dias_esperados()]; CN = ['lo', 'hi', 'mixta', 'indet']; CODN = {0: 'ETH', 1: 'SOL', 2: 'XRP', 3: 'BTC'}
KEEP = BASE + [f'{a}_{s}' for s in ('p35', 'p60') for a in ('F5', 'bid', 'cat')]
def carga_dia(grupo, d):
    """-> DataFrame de prints del grupo con clases: cl_v4 (causal movil), cl_c (ADD3, ventana alineada previa), cl_fut (validacion, mira hacia delante); None + motivo si no utilizable."""
    day0 = ms(d + 'T00:00:00Z'); z = np.load(C4 + f'clases_{d}.npz'); cls, fut = z['cls'].astype(object), z['cls_fut'].astype(object)
    if grupo == 'ALL3':
        mp, pk = CACHE + f'pob_add3_{d}.json', CACHE + f'{d}_pob_add3.pkl.gz'; m = json.load(open(mp))
        if m.get('estado') != 'COMPLETE' or not os.path.exists(pk): return None, f"{m.get('estado')}"
        X = pd.read_pickle(pk, compression='gzip'); X = X[[c for c in KEEP if c in X.columns]].copy(); cw = clase_p5([np.nan if v is None else v for v in m['C3_suelo_rx_menos_ex']['perfil_p5_10min']])
    else:
        mp, pk = C4 + f'manifest_{d}.json', C4 + f'btc_pob_{d}.pkl.gz'
        if not os.path.exists(mp): return None, 'FALTA'
        m = json.load(open(mp))
        if m.get('estado') != 'COMPLETE' or not os.path.exists(pk): return None, f"{m.get('estado')} cob {m.get('cobertura_desenlace_coste')}"
        X = pd.read_pickle(pk, compression='gzip'); X = X[[c for c in KEEP if c in X.columns]].copy(); pm = json.load(open(CACHE + f'pob_add3_{d}.json'))['C3_suelo_rx_menos_ex']['perfil_p5_10min']; cw = clase_p5([np.nan if v is None else v for v in pm])
        assert m['paridad_p5'] == 'NA' or (isinstance(m['paridad_p5'], dict) and m['paridad_p5']['difieren'] == 0), f'{d}: paridad p5 de histograma != ADD3'
    X = X.drop(columns=[c for c in ('r_rx', 'acc', 'gana', 'epoca', 'epoca_ts', 'p5w') if c in X.columns]); X['dia_c'] = np.int16(DIAS_ALL.index(d)); X['coin_c'] = X.coin.astype(str).map({'ETH': 0, 'SOL': 1, 'XRP': 2, 'BTC': 3}).astype(np.int8)
    X['mid'] = X.mid.astype(str).astype(np.int64); X['lado_c'] = (X.lado_m.astype(str) == 'YES').astype(np.int8); X = X.drop(columns=['dia', 'coin', 'lado_m'])
    r = X.r_ex.values.astype(np.int64); Bq = (r - 83 - day0) // 10_000; ok = (Bq >= 0) & (Bq < len(cls)); Bc = np.clip(Bq, 0, len(cls) - 1)
    CM = {'lo': 0, 'hi': 1, 'mixta': 2, 'indet': 3}; cd = lambda a: np.array([CM[x] for x in a], np.int8)
    X['cl_v4'] = cd(np.where(ok, cls[Bc], 'indet')); X['cl_fut'] = cd(np.where(ok, fut[Bc], 'indet'))
    wc = (r - 200 - day0) // 600000 - 1; X['cl_c'] = cd(np.where((wc >= 0) & (wc < 144), cw[np.clip(wc, 0, 143)], 'indet'))
    for c in X.columns:
        if str(X[c].dtype) == 'float64' and c not in ('pnl', 'coste', 'q'): X[c] = X[c].astype(np.float32)
    X['hora'] = X.hora.astype(np.int8); X['pnl'] = X.pnl.astype(np.float32)
    return X, 'COMPLETE'
f3 = lambda x: f'{x:+.3f}' if x is not None and np.isfinite(x) else 'nan'
class Grupo:
    def __init__(s, nombre, P):
        s.n = nombre; s.P = P; s.dia = P.dia_c.values.astype(np.int64); s.coin = P.coin_c.values.astype(np.int64); s.hora = P.hora.values.astype(int); s.pnl = P.pnl.values.astype(float); s.co = P.coste.values.astype(float); s.q = P.q.values.astype(float)
        s.cl = P.fin.values.astype(np.int64); s.mid = P.mid.values.astype(np.int64); s.lado = P.lado_c.values.astype(np.int64); s.sid_all = pd.factorize(s.dia * 1000 + s.coin * 100 + s.hora)[0]
    def codes(s, f5): t = ter(f5); return np.select([t == 'bajo', t == 'medio', t == 'alto'], [0, 1, 2], 3).astype(np.int8)
    def tipoB(s, nm): b = s.P['bid_' + nm].values.astype(float); return np.isfinite(b) & ((b - s.q) >= 0.0099 - 1e-12)
    @staticmethod
    def g_eur(seg, c, p_, k_, ns):
        mb, ma = c == 0, c == 2; cb = np.bincount(seg[mb], k_[mb], ns); ca = np.bincount(seg[ma], k_[ma], ns); sb = np.bincount(seg[mb], p_[mb], ns); sa = np.bincount(seg[ma], p_[ma], ns)
        g = np.full(ns, np.nan); ok = (cb > 0) & (ca > 0); g[ok] = sb[ok] / cb[ok] - sa[ok] / ca[ok]; return g
    @staticmethod
    def g_uni(seg, c, r_, ns):
        mb, ma = c == 0, c == 2; nb = np.bincount(seg[mb], None, ns); na = np.bincount(seg[ma], None, ns); sb = np.bincount(seg[mb], r_[mb], ns); sa = np.bincount(seg[ma], r_[ma], ns)
        g = np.full(ns, np.nan); ok = (nb > 0) & (na > 0); g[ok] = sb[ok] / nb[ok] - sa[ok] / na[ok]; return g
    @staticmethod
    def serie(g):
        d = g[np.isfinite(g)]; o = dict(n_seg=int(len(d)), media=float(np.mean(d)) if len(d) else np.nan, ic90_inf=np.nan, p_t=np.nan, dias_pos=int((d > 0).sum()), frac_pos=float((d > 0).mean()) if len(d) else np.nan, sin2=np.nan, n_req=np.nan)
        if len(d) >= 3:
            lo, p, mu = t_ic(d); s_ = np.sort(d); sd = float(np.std(d, ddof=1)); o.update(media=float(mu), ic90_inf=float(lo), p_t=float(p), sin2=float(s_[:-2].mean()), n_req=float((1.645 * sd / mu) ** 2) if mu > 0 else np.nan)
        return o
    def celda(s, nm, m, segl):
        df = pd.DataFrame({'seg': segl[m], 'mid': s.mid[m], 'lado': s.lado[m], 'code': s.codes(s.P['F5_' + nm].values[m]), 'pnl': s.pnl[m], 'co': s.co[m], 'sid': s.sid_all[m], 'dia': s.dia[m]})
        U = df.groupby(['seg', 'mid', 'lado', 'code'], sort=True).agg(pnl=('pnl', 'sum'), co=('co', 'sum'), sid=('sid', 'first'), nsid=('sid', 'nunique'), n=('pnl', 'size'), dia=('dia', 'first')).reset_index()
        assert (U.nsid == 1).all(), 'unidad con mas de un estrato dia x moneda x hora'
        seg, segn = pd.factorize(U.seg.values); ns = len(segn); code = U.code.values.astype(np.int8); pu = U.pnl.values.astype(float); cu = U.co.values.astype(float); assert (cu > 0).all(); ru = pu / cu
        ge, gu = s.g_eur(seg, code, pu, cu, ns), s.g_uni(seg, code, ru, ns); tt = {}
        for r, cs in (('todo', (0, 1, 2, 3)), ('bajo', (0,)), ('medio', (1,)), ('alto', (2,)), ('nan', (3,)), ('G1', (0, 1))):
            mu = np.isin(code, cs); tt[r] = dict(n_unid=int(mu.sum()), n_prints=int(U.n.values[mu].sum()), coste=float(cu[mu].sum()), ev_eur=float(pu[mu].sum() / cu[mu].sum()) if mu.any() else np.nan, ev_unid=float(ru[mu].mean()) if mu.any() else np.nan)
        # EV por dia de la regla G1 (bajo+medio) y exceso alto diario (como el juez V2: f*sum(pnl) - sum(pnl alto), por segmento)
        ex = np.full(ns, np.nan); evg1 = np.full(ns, np.nan)
        for i in range(ns):
            mi = seg == i; c_all = cu[mi].sum(); c_hi = cu[mi & (code == 2)].sum(); ex[i] = (c_hi / c_all) * pu[mi].sum() - pu[mi & (code == 2)].sum() if c_all > 0 else np.nan
            mg = mi & np.isin(code, (0, 1)); evg1[i] = pu[mg].sum() / cu[mg].sum() if cu[mg].sum() > 0 else np.nan
        return dict(seg=seg.astype(np.int64), segn=[f'{DIAS_ALL[int(x) // 4]}|{CN[int(x) % 4]}' for x in segn], ns=ns, code=code, pu=pu, cu=cu, ru=ru, strata=pd.factorize(U.sid.values)[0], g_e=ge, g_u=gu, s_e=s.serie(ge), s_u=s.serie(gu), ter=tt, s_exc=s.serie(ex), s_evg1=s.serie(evg1),
                    exc_alto_total=float(np.nansum(ex)), n_prints=int(m.sum()), n_unid=int(len(U)), n_ml=int(U.groupby(['mid', 'lado']).ngroups), n_dias=int(pd.Series(s.dia[m]).nunique()), n_cierres=int(pd.Series(s.cl[m]).nunique()))
    def placebo(s, Cs, seed):
        rng = np.random.default_rng(seed); de = {k: np.empty(B) for k in Cs}; du = {k: np.empty(B) for k in Cs}; o0 = {k: np.argsort(C['strata'], kind='stable') for k, C in Cs.items()}
        for b in range(B):
            for k, C in Cs.items():
                o = np.lexsort((rng.random(len(C['code'])), C['strata'])); Lp = np.empty_like(C['code']); Lp[o0[k]] = C['code'][o]
                ge = s.g_eur(C['seg'], Lp, C['pu'], C['cu'], C['ns']); gu = s.g_uni(C['seg'], Lp, C['ru'], C['ns'])
                de[k][b] = np.nanmean(ge) if np.isfinite(ge).any() else np.nan; du[k][b] = np.nanmean(gu) if np.isfinite(gu).any() else np.nan
        mxe = np.nanmax(np.vstack(list(de.values())), 0); mxu = np.nanmax(np.vstack(list(du.values())), 0)
        for k, C in Cs.items():
            oe, ou = C['s_e']['media'], C['s_u']['media']
            C['pl'] = dict(e_celda=float(np.nanmean(de[k] >= oe - 1e-12)), e_max=float(np.nanmean(mxe >= oe - 1e-12)), e_media=float(np.nanmean(de[k])), u_celda=float(np.nanmean(du[k] >= ou - 1e-12)), u_max=float(np.nanmean(mxu >= ou - 1e-12)), u_media=float(np.nanmean(du[k])))
    def celdas(s, clasecol, seed):
        cl = s.P[clasecol].values.astype(np.int64); segc = s.dia * 4 + cl; CB = {}
        for nm in ('p35', 'p60'):
            for k in ('hi', 'lo'):
                m = (cl == {'lo': 0, 'hi': 1}[k]) & s.tipoB(nm)
                if m.sum() >= 50: CB[f'{nm}|{k}'] = s.celda(nm, m, segc)
        if CB: s.placebo(CB, seed)
        return CB
def lineas(k, C):
    t, se, su, pl = C['ter'], C['s_e'], C['s_u'], C.get('pl'); sx, sg = C['s_exc'], C['s_evg1']
    L = [f"{k}: prints {C['n_prints']} | unidades {C['n_unid']} ({C['n_ml']} mercado-lado) | {C['n_dias']} dias, {C['n_cierres']} cierres",
         f"   EV pond. EUR: todo {f3(t['todo']['ev_eur'])} bajo {f3(t['bajo']['ev_eur'])} medio {f3(t['medio']['ev_eur'])} alto {f3(t['alto']['ev_eur'])} G1(bajo+medio) {f3(t['G1']['ev_eur'])} | EV por unidad: todo {f3(t['todo']['ev_unid'])} bajo {f3(t['bajo']['ev_unid'])} medio {f3(t['medio']['ev_unid'])} alto {f3(t['alto']['ev_unid'])} G1 {f3(t['G1']['ev_unid'])} | inversion (alto-todo) EUR {f3(t['alto']['ev_eur'] - t['todo']['ev_eur'])}"]
    for nmb, s_, pk in (('EUR', se, 'e'), ('unidad', su, 'u')):
        L.append(f"   gradiente {nmb} diario {f3(s_['media'])} IC90 dias inf {f3(s_['ic90_inf'])} dias+ {s_['dias_pos']}/{s_['n_seg']} sin 2 mejores {f3(s_['sin2'])}" + (f" | placebo unidad p celda {pl[pk + '_celda']:.3f} maxstat {pl[pk + '_max']:.3f} (media {f3(pl[pk + '_media'])})" if pl else ''))
    L.append(f"   exceso alto (EUR) total {C['exc_alto_total']:+.0f} diario {f3(sx['media'])} IC90 dias inf {f3(sx['ic90_inf'])} dias+ {sx['dias_pos']}/{sx['n_seg']} sin 2 mejores {f3(sx['sin2'])} | EV diario G1 {f3(sg['media'])} IC90 inf {f3(sg['ic90_inf'])} dias+ {sg['dias_pos']}/{sg['n_seg']} sin 2 mejores {f3(sg['sin2'])}")
    return L
def limpio(C): return {k: v for k, v in C.items() if k not in ('seg', 'code', 'pu', 'cu', 'ru', 'strata', 'g_e', 'g_u')} | dict(serie_eur=dict(zip(C['segn'], np.round(C['g_e'], 4).tolist())), serie_unid=dict(zip(C['segn'], np.round(C['g_u'], 4).tolist())))
def criterio(CB, nm):
    h, l = CB.get(f'{nm}|hi'), CB.get(f'{nm}|lo')
    if h is None or l is None: return 'INSUFFICIENT (falta una clase)'
    sh, sl = h['s_e'], l['s_e']
    if min(sh['n_seg'], sl['n_seg']) < 5: return f"INSUFFICIENT (dias hi {sh['n_seg']}, lo {sl['n_seg']}; < 5)"
    if all(np.isfinite(s['ic90_inf']) and s['media'] > 0 and s['ic90_inf'] > 0 and s['sin2'] > 0 for s in (sh, sl)): return 'EXPLORATORY (signo robusto; ' + ('placebo superado' if max(h['pl']['e_max'], l['pl']['e_max']) <= 0.0125 else f"placebo no superado: maxstat hi {h['pl']['e_max']:.3f}, lo {l['pl']['e_max']:.3f}") + ')'
    return f"EXPLORATORY (media > 0 en ambas; n dias requerido hi {sh['n_req']:.0f}, lo {sl['n_req']:.0f})" if sh['media'] > 0 and sl['media'] > 0 else f"INSUFFICIENT (media hi {f3(sh['media'])}, lo {f3(sl['media'])})"
txt = [f"# T2/T3 F5-V4: F5 por CLASE CAUSAL v4 (suelo_causal, ventana movil 10 min; excluye indet/mixta) -- SPEC sha {open(HERE + '/SPEC_F5_V4_17nov.sha256').read()[:8]} -- CENSURADA, gradiente poblacional (NO EV de regla), TODO «no validado»" + (f" [SMOKE {','.join(DIAS)}]" if SM else '')]
RES = dict(spec=open(HERE + '/SPEC_F5_V4_17nov.sha256').read().split()[0]); GR = {}
for grupo in ('ALL3', 'BTC'):
    parts, est = [], {}
    for d in DIAS:
        try: X, e = carga_dia(grupo, d)
        except FileNotFoundError as ex: X, e = None, f'FALTA {os.path.basename(str(ex.filename))}'
        est[d] = e
        if X is not None: parts.append(X)
    ok_d = [d for d in DIAS if est[d] == 'COMPLETE']; RES[grupo] = dict(estado_dias=est, dias_ok=ok_d)
    txt += ['', f"## GRUPO {grupo}: dias {len(ok_d)}/{len(DIAS)} COMPLETE" + ('' if len(ok_d) == len(DIAS) else ' | no utilizables: ' + '; '.join(f'{d}[{e}]' for d, e in est.items() if e != 'COMPLETE'))]
    if not parts: txt.append('DATA_BLOCKED: sin dias utilizables'); continue
    P = pd.concat(parts, ignore_index=True); del parts; G = Grupo(grupo, P); GR[grupo] = G
    # ---- exclusion por clase (tipo B), por print/EUR/mercado-lado
    txt.append(f"### {grupo} exclusion por clase causal v4 (tipo B; prints = rellenos poblacionales)"); RES[grupo]['exclusion'] = {}
    for nm in ('p35', 'p60'):
        m = G.tipoB(nm); c_ = P.cl_v4.values[m]; w_ = G.co[m]; g = pd.DataFrame({'mid': G.mid[m], 'lado': G.lado[m], 'c': c_}).groupby(['mid', 'lado']).c.first()
        sh = {k: (float(np.mean(c_ == i)), float(w_[c_ == i].sum() / w_.sum()), float((g == i).mean())) for i, k in enumerate(CN)}; RES[grupo]['exclusion'][nm] = dict(prints=int(m.sum()), **{k: dict(prints=v[0], eur=v[1], mercado_lado=v[2]) for k, v in sh.items()})
        txt.append(f"  {nm}: prints {int(m.sum())} | lo {100*sh['lo'][0]:.1f} % hi {100*sh['hi'][0]:.1f} % mixta {100*sh['mixta'][0]:.1f} % indet {100*sh['indet'][0]:.1f} % (prints) | EUR: lo {100*sh['lo'][1]:.1f} hi {100*sh['hi'][1]:.1f} mixta {100*sh['mixta'][1]:.1f} indet {100*sh['indet'][1]:.1f} | EXCLUIDO (mixta+indet) {100*(sh['mixta'][0]+sh['indet'][0]):.2f} % prints, {100*(sh['mixta'][1]+sh['indet'][1]):.2f} % EUR")
    # ---- validacion contra la clase de futuro (5 min siguientes; NO se usa para elegir nada)
    txt.append(f"### {grupo} validacion vs clase de FUTURO (5 min siguientes, tot>=100): de los prints declarados lo/hi, % con clase futura determinada y DISTINTA (contaminacion) y % futura indet"); RES[grupo]['validacion'] = {}
    for nm in ('p35', 'p60'):
        m = G.tipoB(nm)
        for col, et in (('cl_c', 'ADD3 ventana alineada previa'), ('cl_v4', 'v4 causal movil pura')):
            c_ = P[col].values[m]; f_ = P.cl_fut.values[m]; w_ = G.co[m]; r = {}
            for ki, k in ((0, 'lo'), (1, 'hi')):
                mk = c_ == ki
                if mk.sum() == 0: continue
                det = mk & (f_ <= 1); mal = det & (f_ != ki)
                r[k] = dict(prints=int(mk.sum()), contam_prints=float(mal.sum() / max(det.sum(), 1)), contam_eur=float(w_[mal].sum() / max(w_[det].sum(), 1e-9)), fut_indet=float(np.mean(f_[mk] == 3)), fut_mixta_o_otra=float(np.mean(f_[mk] != ki)))
            RES[grupo]['validacion'][f'{nm}|{col}'] = r
            txt.append(f"  {nm} {et}: " + ' | '.join(f"{k}: n {v['prints']}, contaminada {100*v['contam_prints']:.2f} % prints / {100*v['contam_eur']:.2f} % EUR, futura indet {100*v['fut_indet']:.1f} %" for k, v in r.items()))
    # ---- celdas: control (cl_c) y v4
    for col, et, seed in (('cl_c', 'CONTROL ADD3: clase causal de ADD3 (ventana alineada previa)', 20261118), ('cl_v4', 'v4: clase causal movil PURA (excluye indet y mixta)', 20261118)):
        CB = G.celdas(col, seed); GR[(grupo, col)] = CB
        txt += ['', f"### {grupo} CELDAS por {et} (segmento = dia x clase; placebo por unidad B={B}, max-stat sobre estas celdas)"]
        for k, C in CB.items(): txt += lineas(k, C)
        RES[grupo][f'celdas_{col}'] = {k: limpio(C) for k, C in CB.items()}
        crit = {nm: criterio(CB, nm) + ' -- sensibilidad, NO VALIDADO' for nm in ('p35', 'p60')}; RES[grupo][f'criterio_{col}'] = crit; txt += [f'  criterio §4 l_ef {nm[1:]} ms: {v}' for nm, v in crit.items()]
    if grupo == 'ALL3' and not SM:       # control de reproduccion: celdas con cl_c deben coincidir con E2_clase_suelo_add3.json
        bad = []
        for k, C in GR[(grupo, 'cl_c')].items():
            r = REF['clase_causal'].get(k)
            if r is None or C['n_prints'] != r['n_prints'] or abs(C['s_e']['media'] - r['s_e']['media']) > 1e-9 or abs(C['ter']['todo']['ev_eur'] - r['ter']['todo']['ev_eur']) > 1e-9: bad.append(k)
        txt.append(f"CONTROL de reproduccion de E2_clase_suelo_add3.json (cl_c, ALL3): {'OK, 4/4 celdas identicas (n prints, gradiente EUR diario, EV todo)' if not bad and len(GR[(grupo, 'cl_c')]) == 4 else 'FALLA: ' + str(bad)}"); RES[grupo]['control_add3'] = 'OK' if not bad and len(GR[(grupo, 'cl_c')]) == 4 else f'FALLA {bad}'
txt += ['', f"Tiempo {time.time() - t0:.0f} s. Limites: poblacion censurada (gradiente, no EV de regla); d_proc = 3 ms supuesto; causa de la alternancia del suelo INSUFICIENTE; el clasificador p5 detecta tarde el paso lo->hi (lag ~4,75 min); EV por EUR domina el gran tamano (comparar con EV por unidad)."]
open(OUT + '.txt', 'w').write('\n'.join(txt) + '\n'); json.dump(RES, open(OUT + '.json', 'w'), default=float, indent=1); print('\n'.join(txt))
