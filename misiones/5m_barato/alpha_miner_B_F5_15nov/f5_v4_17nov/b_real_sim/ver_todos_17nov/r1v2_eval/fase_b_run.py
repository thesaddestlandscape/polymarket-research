#!/usr/bin/env python3
"""fase_b_run.py MODO [DIA] -- runner idempotente de la FASE B de R1v2 (V1-V6 DENTRO del replay de la politica real de B). NO se lanza sin OK del chief (run_fase_b.sh). 0 ordenes, 0 red.
 l2 DIA        : PASO PREVIO (una pasada en streaming por dia sobre TODOS los ficheros libro5_ms PID, orden (rx,pid,seq)): eventos L2 de los tokens 5m de interes + m15 + MAPA DE HUECOS por (dia, token) -> fb_l2ev_DIA.pkl, fb_huecos_DIA.json. Fichero truncado = FAILED (dia vetado).
 base DIA      : replay base (HK=None) + tabla de PUNTOS (orden,t) con rasgos (E1-L1) y flags V5/V6 -> fb_base_DIA.pkl, fb_puntos_DIA.pkl.   (dias TRAIN y dias de evaluacion)
 entrena       : (exige l2 y base COMPLETE de todos los dias TRAIN) test de fuga NaN por rasgo/dia (banda 0,40-0,60 -> BLOCKED_FUGA), E1 completo (E + A5,F,A3,A4,D1,D2; logistica L2, bootstrap por dias) SOLO con puntos de dias TRAIN y ordenes rellenadas -> fb_e1.pkl + ABLACION por grupo y baseline 'solo E' (leave-one-day-out, mismas filas) fb_ablacion.json (+ manifest con hash). IPW solo si existe fb_hazard_train.pkl; si no, SIN IPW (declarado).
 variantes DIA : (exige entrena COMPLETE con el codigo vigente; el sha de fb_e1.pkl queda en el manifest) dia de EVALUACION, horquilla de bloqueo H0 (motor vigente, primaria) / HD (Delta=9,07 acciones, ADENDA_07 firmada) / HN (nivel entero): V1..V6 + controles V5/V6 con hooks sobre el replay real (+ puntuaciones de puntos para el placebo) -> fb_var_DIA.pkl, fb_pts_eval_DIA.pkl.
 final         : EV incondicional/condicional/ponderado por EUR por variante, DeltaPnL vs base POR DIA con IC90 por dias, frecuencia de disparo, familia de 6 (placebo/inversion/max-statistic) -> fb_resultado.json + run_manifest.json.
t_proc (tiempo de computo medido) es OBLIGATORIO: variable FB_T_PROC_MS sin default (exit 3 si falta). Unidad: 1.er relleno mercado-lado. Dias de evaluacion por defecto: 08-09 Nov (SELECCION, diagnostico); 10-17 Nov exigen FB_DIAS_EVAL explicito (una lectura por version hasheada, R-CXB-5). Etiqueta: DIAGNOSTICO, no confirmatorio."""
import sys, os, json, time, hashlib, subprocess, pickle
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; V = os.path.dirname(HV.rstrip('/')) + '/'; BSIM = os.path.dirname(V.rstrip('/')) + '/'
OUT = os.environ.get('FB_OUT', HV + 'out_fb/'); os.makedirs(OUT, exist_ok=True); os.environ['SEC7_OUT'] = OUT
sys.path.insert(0, HV); sys.path.insert(0, V + 'r1v2_sec7/'); sys.path.insert(0, BSIM)
import numpy as np, pandas as pd
import sec7_run as RU, l2_rasgos as L2
RU.OUT = OUT
TRAIN = list(__import__('e1_modelo').TRAIN_DIAS); EVAL = os.environ.get('FB_DIAS_EVAL', '2026-11-08,2026-11-09').split(',')
TABLA = V + 'cierre_limites_19nov/tabla_suelo_ventanas_19nov.csv'; DELTA_CENTRAL = 9.07      # ADENDA_07 FIRMADA (sha db4484e5...): mediana rem_sh_limite compra_comp ok, n=89
HORQ = ('H0', 'HD', 'HN'); CTRL = {'V5': 'ctl_V5', 'V6': 'ctl_V6'}
M5 = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz'; BCOINS = ('ETH', 'SOL', 'XRP'); VARS = ('V1', 'V2', 'V3', 'V4', 'V5', 'V6')
ts, log, sha, atomic_json, atomic_pkl = RU.ts, RU.log, RU.sha, RU.atomic_json, RU.atomic_pkl
def t_proc():
    v = os.environ.get('FB_T_PROC_MS')
    if v is None: raise SystemExit('FB_T_PROC_MS obligatorio (tiempo de computo medido, ms); sin default')
    return float(v)
def code_hashes():
    H = {f: sha(HV + f) for f in ('fase_b_run.py', 'replay_variantes.py', 'l2_rasgos.py', 'e1_modelo.py', 'familia6.py', 'variantes_b.py', 'puerta0_core.py')}
    for f in ('b_policy_sim.py', 'eng_v5.py', 'ejecutor_puro.py'): H['motor/' + f] = sha(BSIM + f)
    for f in ('sec7_core.py', 'sec7_calculos.py', 'sec7_run.py'): H['sec7/' + f] = sha(V + 'r1v2_sec7/' + f)
    return H
RU.code_hashes = code_hashes
_ya = RU.ya_completo
def ya_completo(modo, d, outs):
    if not _ya(modo, d, outs): return False
    try:
        m = json.load(open(RU.mpath(modo, d)))
        if m.get('code') != code_hashes(): return False
        if modo == 'variantes': return (m.get('cobertura') or {}).get('e1_sha') == sha(OUT + 'fb_e1.pkl')      # las variantes valen SOLO para el e1 con que se corrieron
        return True
    except Exception: return False
RU.ya_completo = ya_completo

def carga_binance(d):
    """{coin_minuscula: (recv_ordenado, px)} (arrays numpy) de las filas x del m5_registro del dia (y las 3 h previas del dia anterior), por RECEPCION (columna 8). STREAMING: awk -> pandas por trozos -> arrays (sin listas de tuplas)."""
    import calendar, variantes_b as VB
    d0 = calendar.timegm(time.strptime(d, '%Y-%m-%d')) * 1000; prev = time.strftime('%Y-%m-%d', time.gmtime(d0 / 1000 - 86400)); acc = {}
    for dia in (prev, d):
        p = M5 % dia
        if not os.path.exists(p): continue
        cmd = f"set -o pipefail; zcat '{p}' | awk -F, -v a={d0 - 3 * 3600_000} -v b={d0 + 86400_000} '$1==\"x\" && $8>=a && $8<b && ($3==\"ETHUSDT\"||$3==\"SOLUSDT\"||$3==\"XRPUSDT\") {{print $3\",\"$4\",\"$8}}'"
        pr = subprocess.Popen(['bash', '-c', cmd], stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
        try:
            for ch in pd.read_csv(pr.stdout, header=None, names=['s', 'px', 'r'], dtype={'s': str, 'px': float, 'r': 'int64'}, chunksize=500_000):
                for s_, g in ch.groupby('s'): acc.setdefault(s_[:3].lower(), []).append((g.r.values, g.px.values))
        except pd.errors.EmptyDataError: pass
        if pr.wait() != 0: raise RuntimeError(f'm5_registro ilegible/truncado: {p}')
    return {c: VB.ordena_rx(np.concatenate([a for a, _ in v]), np.concatenate([b for _, b in v])) for c, v in acc.items()}

_TS = {}
def suelo_tab():
    """tabla de suelo FIRMADA (sha comprobado en lee_tabla_suelo) + celdas validas; cache."""
    import puerta0_core as P0
    if 'x' not in _TS: tab = P0.lee_tabla_suelo(TABLA); _TS['x'] = (tab, P0.celdas_validas(tab))
    return _TS['x']

def contexto_dia(d, horq='H0', base=None):
    """base = ctx de otra horquilla: reutiliza todo y solo cambia el motor de bloqueo."""
    import b_policy_sim as BS, eng_v5 as EV, sec7_core as C, replay_variantes as RV
    if base is not None:
        E = base['E']; W = C.EngineBloqueo(E, activo=False) if horq == 'H0' else (RV.EngineBloqueoDelta(E, DELTA_CENTRAL) if horq == 'HD' else C.EngineBloqueo(E, activo=True)); return dict(base, W=W, horq=horq)
    E, info = EV.build(d); W = C.EngineBloqueo(E, activo=False); bsrc = carga_binance(d)
    l2 = pickle.load(open(OUT + f'fb_l2ev_{d}.pkl', 'rb')); cl = L2.carga_chainlink(d)             # fail-closed: sin chainlink del dia no hay D2 (FileNotFoundError)
    k2tok = {k: tok for tok, k in E.D.tokidx.items()}
    return dict(W=W, E=E, serie=W._serie, bsrc=bsrc, P=BS.params(), info=info, dia=d, horq='H0', k2tok=k2tok, l2=L2.L2Dia(l2['ev'], l2['m15'], cl, bsrc))

def anota(R, ctx, d):
    import sec7_core as C, puerta0_core as P0
    R = R.copy(); R['dia'] = d
    if not len(R): return R
    tab, cel = suelo_tab(); R = P0.anota_suelo(R, tab, cel)                                          # estrato lo/hi/indet/sin_tabla de la VENTANA (tabla firmada), nunca rasgo
    R = C.anota_ordenes(R, ctx['W'], ctx['serie']); R = P0.t_ex_fills(R, ctx['W'].fills); R['canal'] = R.canal.where(R.q <= 0, 'visible'); return R

def hook_de(nombre, ctx, modelo, tp):
    import replay_variantes as RV, variantes_b as VB, e1_modelo as E1
    fills = lambda: ctx['W'].fills
    if nombre.startswith('ctl_'): return RV.HookControl(hook_de(nombre[4:], ctx, modelo, tp))
    if nombre in ('V5', 'V6'): return RV.HookBinance(ctx['bsrc'], VB.V5 if nombre == 'V5' else VB.V6, tp, fills=fills)
    c, regla = {'V1': (0.02, 'ucb'), 'V2': (0.0, 'ucb'), 'V3': (0.05, 'ucb'), 'V4': (0.02, 'mu')}[nombre]
    return RV.HookE1(E1.PuntuaE1(modelo, ctx['serie'], ctx['bsrc'], l2=ctx['l2'], k2tok=ctx['k2tok']), regla, c, tp, fills=fills)

def corre_variante(ctx, d, nombre, modelo, tp):
    """replay de la politica real de B con el hook de la variante (None = base). Devuelve ordenes anotadas + contadores del hook."""
    import replay_variantes as RV, puerta0_core as P0
    HK = None if nombre == 'base' else hook_de(nombre, ctx, modelo, tp); ctx['W'].fills.clear()
    R, cov = RV.run_day(d, ctx['P'], E=ctx['W'], HK=HK); R = P0.unidad_primer_relleno(anota(R, ctx, d).assign(variante=nombre, horq=ctx['horq'])) if len(R) else R.assign(variante=nombre, dia=d, horq=ctx['horq'])
    return R, dict(contadores=dict(HK.cont) if HK else {}, ordenes=int(len(R)), rellenos=int((R.q > 0).sum()) if len(R) else 0, saltados=cov.get('skip'))

def puntos_dia(ctx, R, modelo, tp):
    """tabla de puntos (orden,t) de las ordenes base: rasgos E1 completos (E + L2/15m/D2), puntuaciones (si hay modelo), flags V5/V6 en (t-250, t], es_alta (primer punto = alta/repegado), gate_f5 (F5_t invalido/alto en el alta), suelo (estrato de la tabla firmada), fin."""
    import e1_modelo as E1, variantes_b as VB, sec7_core as C
    J = {c: {n: VB.saltos(*ctx['bsrc'][c], v) for n, v in (('V5', VB.V5), ('V6', VB.V6))} for c in ctx['bsrc']}; filas = []
    for o in R.itertuples():
        k = int(o.k); kc = ctx['W'].D.comp(k) if hasattr(ctx['W'], 'D') and hasattr(ctx['W'].D, 'comp') else None; own = ctx['serie'](k); comp = ctx['serie'](kc) if kc is not None else None
        d_ = dict(o._asdict()); d_.update(tf=o.tf if o.q > 0 else float('nan'), fin=o.fin); tok = ctx['k2tok'].get(k)
        P = E1.puntos_orden(d_, own, comp, ctx['bsrc'].get(o.coin), tp, l2=ctx['l2'], ctx=dict(tok=tok, fin=o.fin) if tok else None)
        if not len(P): continue
        P['ord_id'] = f'{o.dia}|{o.mid}|{o.n_ord}'; P['coin'] = o.coin; P['nivel'] = o.L; P['pnl_orden'] = o.pnl if o.q > 0 else 0.0; P['suelo'] = getattr(o, 'estrato', 'sin_tabla')
        f5 = C.f5t(own, int(P.t.iloc[0])); P['gate_f5'] = False; P.loc[P.es_alta, 'gate_f5'] = C.tercil(None if f5 is None or not np.isfinite(f5) else f5) in ('inval', 'alto')
        X = P[E1.FEATS_ALL].values; ok = ~np.isnan(X).any(axis=1); P['score_mu'] = np.nan; P['score_ucb'] = np.nan
        if modelo is not None and ok.any(): mh, mu = modelo.mu(P[modelo.feats].values[ok], P.L.values[ok]); P.loc[ok, 'score_mu'] = mh; P.loc[ok, 'score_ucb'] = mu
        for n, var in (('V5', VB.V5), ('V6', VB.V6)):       # MISMAS funciones que HookBinance: no armar en el alta (VB.no_armar) y cancelacion en vida = primer tick adverso desde la llegada (VB.primer_disparo)
            adv = VB.adverso(J[o.coin][n], o.lado) if o.coin in J else np.array([], np.int64); t = P.t.values; f = np.zeros(len(t), bool); al = P.es_alta.values.astype(bool)
            f[al] = [VB.no_armar(adv, int(x), var) for x in t[al]]
            tb = VB.primer_disparo(adv, int(o.t_arr), int(t.max()))
            if tb is not None:
                ix = int(np.searchsorted(t, tb, 'left'))                  # primer punto de rejilla >= tb (retraso <= 250 ms, conservador)
                if ix < len(t) and not al[ix]: f[ix] = True
            P['fire_' + n] = f
        filas.append(P)
    return pd.concat(filas, ignore_index=True) if filas else pd.DataFrame()

# ------------------------------------------------------------------ jobs
def run_l2(d):
    ven = L2.ventanas_m5(M5 % d); rutas = L2.rutas_dia(d)
    if not ven: raise RuntimeError(f'sin mercados 5m ETH/SOL/XRP en m5_registro {d}')
    if not rutas: raise RuntimeError(f'sin ficheros libro5_ms para {d} (DATA_BLOCKED)')
    L2.carga_chainlink(d)                                                                             # fail-closed: el dia debe existir
    ev, hu = L2.materializa(d, ven, rutas, tmpdir=OUT)
    if hu['truncado']: raise RuntimeError('fichero libro5_ms TRUNCADO: dia vetado para TRAIN/SELECCION/HOLD: ' + str([i['ruta'] for i in hu['ficheros'].values() if i['truncado']]))
    m15 = L2.carga_m15(L2.M15 % d); L2.guarda(OUT + f'fb_l2ev_{d}.pkl', dict(ev=ev, m15=m15)); atomic_json(OUT + f'fb_huecos_{d}.json', hu)
    sin = sum(1 for h in hu['tokens'].values() if h['n_B'] + h['n_d'] == 0); cob = dict(tokens=len(ven), tokens_sin_B_ni_d=int(sin), eventos=hu['n_eventos'], duplicadas=hu['duplicadas'], seq_perdidos=sum(i['seq_perdidos'] for i in hu['ficheros'].values()), ficheros=len(rutas), tokens_m15=len(m15['q']))
    return dict(cob, etiqueta='CONTEOS; sin EV'), cob

def run_base(d):
    ctx = contexto_dia(d); tp = t_proc(); R, cov = corre_variante(ctx, d, 'base', None, tp); Pt = puntos_dia(ctx, R, None, tp) if len(R) else pd.DataFrame()
    atomic_pkl(OUT + f'fb_base_{d}.pkl', R); atomic_pkl(OUT + f'fb_puntos_{d}.pkl', Pt); atomic_json(OUT + f'fb_cov_base_{d}.json', dict(cov, puntos=int(len(Pt)), t_proc_ms=tp, l2_rewinds=ctx['l2'].n_rewind))
    return dict(ordenes=cov['ordenes'], rellenos=cov['rellenos'], puntos=int(len(Pt)), etiqueta='CONTEOS; sin EV'), dict(cov, puntos=int(len(Pt)))

def run_variantes(d):
    import e1_modelo as E1
    if not RU.ya_completo('entrena', 'x', ['fb_e1.pkl', 'fb_e1_info.json', 'fb_ablacion.json', 'fb_fuga_nan.json']): raise RuntimeError('variantes exige entrena COMPLETE con el codigo vigente (manifest + sha de salidas)')
    e1_sha = sha(OUT + 'fb_e1.pkl'); modelo = pickle.load(open(OUT + 'fb_e1.pkl', 'rb')); ctx0 = contexto_dia(d); tp = t_proc(); Rs = []; cov = {}
    for h in HORQ:
        ctx = contexto_dia(d, h, base=ctx0)
        for v in ('base',) + VARS + tuple(CTRL.values()):
            R, c = corre_variante(ctx, d, v, modelo, tp); Rs.append(R); cov[f'{h}/{v}'] = c
    Rb = [r for r in Rs if len(r) and r.variante.iloc[0] == 'base' and r.horq.iloc[0] == 'H0']; Pt = puntos_dia(contexto_dia(d, 'H0', base=ctx0), Rb[0], modelo, tp) if Rb else pd.DataFrame()
    atomic_pkl(OUT + f'fb_var_{d}.pkl', pd.concat(Rs, ignore_index=True)); atomic_pkl(OUT + f'fb_pts_eval_{d}.pkl', Pt); atomic_json(OUT + f'fb_cov_var_{d}.json', cov)
    return {v: dict(ordenes=c['ordenes'], rellenos=c['rellenos'], contadores=c['contadores']) for v, c in cov.items() if v.startswith('H0/')}, dict(cov, e1_sha=e1_sha)

def run_entrena(_):
    import e1_modelo as E1
    Ps = []; faltan = []
    for d in TRAIN:
        if os.path.exists(RU.mpath('base', d)) and RU.ya_completo('base', d, [f'fb_base_{d}.pkl', f'fb_puntos_{d}.pkl', f'fb_cov_base_{d}.json']): Ps.append(pd.read_pickle(OUT + f'fb_puntos_{d}.pkl'))
        else: faltan.append(d)
    if faltan: raise RuntimeError(f'faltan dias TRAIN base COMPLETE (con el codigo vigente): {faltan}')
    P = pd.concat([p for p in Ps if len(p)], ignore_index=True); n0 = len(P); F = E1.FEATS_ALL
    fuga = E1.fuga_nan_por_rasgo(P[P.relleno], feats=F); atomic_json(OUT + 'fb_fuga_nan.json', fuga); mal = [k for k, v in fuga.items() if v['estado'] == 'FUGA_SOSPECHOSA']
    if mal: raise RuntimeError(f'BLOCKED_FUGA (ADENDA_06): el indicador NaN de {mal} predice el desenlace en algun dia (AUC fuera de 0,40-0,60)')
    nan_por_grupo = {g: {d: float(x[fs].isna().any(axis=1).mean()) for d, x in P.groupby('dia')} for g, fs in E1.GRUPOS_E1.items()}
    P = P[P.relleno]; ok = ~P[F].isna().any(axis=1); excl = int((~ok).sum()); P = P[ok].copy(); P['w_orden'] = E1.pesos_orden(P)      # cada orden suma 1 DESPUES de quitar NaN
    ipw = 'SIN (fb_hazard_train.pkl ausente: hazard TRAIN pendiente)'
    if os.path.exists(OUT + 'fb_hazard_train.pkl'): pass          # PENDIENTE: pesos 1/S del hazard v11 entrenado en TRAIN (entrena_hazard); no se inventa aqui
    M = E1.E1(feats=F).ajusta(P[F].values, P.y.values, P.dia.values, P.w_orden.values); M.feats = list(F)
    abl = E1.ablacion(P, dict(completo=F, solo_E=E1.FEATS, **{f'sin_{g}': [f for f in F if f not in L2.GRUPOS[g]] for g in ('A5', 'F', 'A3', 'A4', 'D1', 'D2')})); atomic_json(OUT + 'fb_ablacion.json', dict(abl, etiqueta='LODO sobre TRAIN, mismas filas; baseline solo_E; no es EV'))
    pickle.dump(M, open(OUT + 'fb_e1.pkl.tmp', 'wb')); os.replace(OUT + 'fb_e1.pkl.tmp', OUT + 'fb_e1.pkl')
    atomic_json(OUT + 'fb_e1_info.json', dict(dias=M.dias, n=M.n, n_puntos_total=int(n0), excluidos_nan=excl, feats=F, grupos=E1.GRUPOS_E1, nan_por_grupo_y_dia=nan_por_grupo, ipw=ipw, B=M.B, seed=M.seed, C=M.C)); return dict(n=M.n, dias=M.dias, ipw=ipw), dict(n=M.n)

def ic90_dias(porDia, K=10000, seed=20261119):
    v = np.asarray(list(porDia.values()), float); rng = np.random.default_rng(seed)
    if len(v) < 2: return dict(total=float(v.sum()), media_dia=float(v.mean()) if len(v) else float('nan'), lo=float('nan'), hi=float('nan'), n_dias=int(len(v)), nota='INSUFFICIENT')
    m = np.array([v[rng.integers(0, len(v), len(v))].mean() for _ in range(K)]); return dict(total=float(v.sum()), media_dia=float(v.mean()), lo=float(np.percentile(m, 5)), hi=float(np.percentile(m, 95)), n_dias=int(len(v)))

def tabla_variantes(R):
    """por variante (incl. base y controles): ordenes, rellenos, P(relleno), EV INCONDICIONAL por mercado-lado ELEGIBLE con el MISMO denominador para todas (mercado-lados del replay base; las que la variante no arma cuentan 0) y EV ponderado por EUR (Sigma pnl / Sigma coste),
    EV|relleno por unidad, y DeltaPnL por dia con IC90 por dias frente al control (V5/V6: replay con los mismos instantes extra sin regla; V1-V4: base)."""
    out = {}; ms = lambda g: set(zip(g.dia, g.mid, g.k)); base = R[R.variante == 'base']; den = ms(base); nden = len(den); dias = sorted(R.dia.unique())
    pdia = lambda g: g.groupby('dia').pnl.sum().reindex(dias, fill_value=0.0)
    for v, g in R.groupby('variante'):
        f = g[g.q > 0]; ref = R[R.variante == CTRL.get(v, 'base')]; dl = (pdia(g) - pdia(ref)).to_dict()
        out[v] = dict(ordenes=int(len(g)), rellenos=int(len(f)), p_relleno=float(len(f) / len(g)) if len(g) else float('nan'), pnl=float(g.pnl.sum()), coste=float(g.cost.sum()), n_mercado_lado_base=nden,
                      EV_incond_por_mercado_lado=float(g.pnl.sum() / nden) if nden else float('nan'), ms_fuera_de_base=int(len(ms(g) - den)), ms_sin_orden=int(len(den - ms(g))),
                      EV_eur=float(g.pnl.sum() / g.cost.sum()) if g.cost.sum() > 0 else float('nan'), EV_cond_por_unidad=float((f.pnl / f.cost).mean()) if len(f) else float('nan'),
                      referencia=None if v == 'base' else CTRL.get(v, 'base'), delta_pnl_vs_referencia=ic90_dias(dl) if v != 'base' else None)
    return out

def horquilla(R):
    """ADENDA_07: DeltaPnL total de cada variante frente a su referencia en H0 / HD (Delta=9,07) / HN; se exige el MISMO signo (no nulo) en las tres; si no -> 'NO ROBUSTO AL BLOQUEO'."""
    import variantes_b as VB
    out = {}
    for v in VARS:
        dl = {}
        for h in HORQ:
            g = R[R.horq == h]; ref = CTRL.get(v, 'base'); dl[h] = float(g[g.variante == v].pnl.sum() - g[g.variante == ref].pnl.sum())
        ms = VB.mantiene_signo(dl); out[v] = dict(delta_pnl=dl, mantiene_signo=ms, etiqueta=None if ms else 'NO ROBUSTO AL BLOQUEO')
    return out

def por_estrato(R):
    """EV y DeltaPnL por estrato de suelo de la tabla firmada (lo / hi / indet / sin_tabla), cada uno con su IC90 por dias; el que decide es 'lo' (Puerta 0)."""
    return {e: tabla_variantes(R[R.estrato == e]) for e in sorted(R.estrato.dropna().unique())}

def final():
    import familia6 as F6, e1_modelo as E1
    est = {}; Rs = []; Ps = []; e1sha = sha(OUT + 'fb_e1.pkl') if os.path.exists(OUT + 'fb_e1.pkl') else None
    for d in EVAL:
        p = RU.mpath('variantes', d); st = json.load(open(p)).get('status') if os.path.exists(p) else 'MISSING'; est[d] = st
        if st == 'COMPLETE' and RU.ya_completo('variantes', d, [f'fb_var_{d}.pkl', f'fb_pts_eval_{d}.pkl', f'fb_cov_var_{d}.json']): Rs.append(pd.read_pickle(OUT + f'fb_var_{d}.pkl')); Ps.append(pd.read_pickle(OUT + f'fb_pts_eval_{d}.pkl'))
        elif st == 'COMPLETE': est[d] = 'FAILED(checkpoint invalido, codigo distinto o e1 distinto)'
    vals = set(est.values()); st_g = 'COMPLETE' if vals == {'COMPLETE'} else ('BLOCKED' if vals <= {'BLOCKED', 'MISSING'} else ('FAILED' if any(v.startswith('FAILED') for v in vals) else 'PARTIAL'))
    rep = dict(job='fase_b R1v2', status=st_g, dias_eval=EVAL, estado_por_dia=est, code=code_hashes(), e1_sha=e1sha, t_fin=ts(), repro='cd %s && bash run_fase_b.sh' % HV, etiqueta='DIAGNOSTICO (SELECCION/no ciego): no confirmatorio; RELLENOS VISIBLES + ESTRES NONE no aplicado aqui; no es EV de B real')
    if not Rs: atomic_json(OUT + 'run_manifest.json', rep); log('FINAL', st_g, est); return 'BLOCKED' if st_g == 'BLOCKED' else 'PARTIAL'
    R = pd.concat(Rs, ignore_index=True); R0 = R[R.horq == 'H0']; res = dict(variantes=tabla_variantes(R0), por_estrato=por_estrato(R0), horquilla_bloqueo=horquilla(R), dias=sorted(R.dia.unique()), delta_central_acciones=DELTA_CENTRAL)
    for nom in ('fb_ablacion.json', 'fb_e1_info.json', 'fb_fuga_nan.json'):
        if os.path.exists(OUT + nom): res[nom[3:-5]] = json.load(open(OUT + nom))
    P = pd.concat([p for p in Ps if len(p)], ignore_index=True) if any(len(p) for p in Ps) else pd.DataFrame()
    if len(P):
        res['fuga_nan_eval'] = E1.fuga_nan_por_rasgo(P[P.relleno], feats=E1.FEATS_ALL)             # misma regla de NaN en SELECCION/HOLD: AUC del indicador por dia
        P = P.copy(); P['tramoT'] = ((P.fin - P.t / 1000.0) // 60).astype(int).clip(0, 4); codes, uniq = pd.factorize(P.ord_id); P['ord'] = codes
        O = P.groupby('ord').pnl_orden.first().reindex(range(len(uniq)), fill_value=0.0).to_frame('pnl'); res['familia6'] = F6.evalua_familia(P, O, t_proc())
    else: res['familia6'] = 'INSUFFICIENT: sin puntos'
    atomic_json(OUT + 'fb_resultado.json', res); rep['outputs'] = {'fb_resultado.json': sha(OUT + 'fb_resultado.json')}; atomic_json(OUT + 'run_manifest.json', rep); log('FINAL', st_g, est); return 'COMPLETE' if st_g == 'COMPLETE' else 'PARTIAL'

if __name__ == '__main__':
    modo = sys.argv[1]
    t_proc()
    if modo == 'base': d = sys.argv[2]; r = RU.job('base', d, [f'fb_base_{d}.pkl', f'fb_puntos_{d}.pkl', f'fb_cov_base_{d}.json'], run_base, dict(RU.inputs_dia(d), l2ev=OUT + f'fb_l2ev_{d}.pkl'))
    elif modo == 'l2': d = sys.argv[2]; r = RU.job('l2', d, [f'fb_l2ev_{d}.pkl', f'fb_huecos_{d}.json'], run_l2, {'m5': M5 % d})
    elif modo == 'entrena': r = RU.job('entrena', 'x', ['fb_e1.pkl', 'fb_e1_info.json', 'fb_ablacion.json', 'fb_fuga_nan.json'], run_entrena, {})
    elif modo == 'variantes': d = sys.argv[2]; r = RU.job('variantes', d, [f'fb_var_{d}.pkl', f'fb_pts_eval_{d}.pkl', f'fb_cov_var_{d}.json'], run_variantes, dict(RU.inputs_dia(d), l2ev=OUT + f'fb_l2ev_{d}.pkl', e1=OUT + 'fb_e1.pkl'))
    elif modo == 'final': r = final()
    else: raise SystemExit(__doc__)
    sys.exit(0 if r == 'COMPLETE' else (4 if r == 'BLOCKED' else 1))      # 0 COMPLETE | 4 BLOCKED | 1 PARTIAL/FAILED: el .sh aborta ante cualquier distinto de 0
