#!/usr/bin/env python3
"""qc_brecha_nivel_mix.py -- Q-C del PREREG_REPLAY_BRECHA_B_16nov (s.7.3) + ADDENDUM1 (s.2.2, B-2). SOLO LECTURA, 0 ordenes, CPU~0.
Pregunta (Q-C): cuanto de la brecha de NIVEL motor-vs-real de B (sim -0,222 vs real -0,061 con rebate; 3.796 ordenes reales 20-23 Oct) explica la
carrera de cancelacion con delta VIGENTE (no circular). Explicativo, EXPLORATORY (4 dias, 100 % R1 por calendario); no decide ninguna palanca.
Entradas (E16 + s.7.3): L2/verif_real/out_v3/V3_2026-10-2{0..3}.pkl, DL/calibracion_etiqueta/ordenes_b.csv (oid, t_cancel_int; t_dec solo para la
clase), L2/verif_real/out/T1_tx.pkl; pool etapa0/l_pool_vigente_13nov.json (assert sha256); ADD3 exp1/cache/pob_add3_<D>.json (clase, solo COMPLETE).
Funciones copiadas LITERALMENTE de L2/dryrun/brecha_nivel_v3.py (sha16 55880cf512c1228d; NO se importa: crea out_replay/ al importarse):
pnl_of y sim_con_delta (exigidas por s.7.3) y, para la reproduccion previa y la misma muestra, carga, ev, tabla_delta y escalones.
La igualdad textual de las copias se comprueba por AST (sin ejecutar el original) antes de calcular nada.
Concreciones (el prereg dice "sorteo determinista por oid, s.3.3" sin fijar la codificacion de la clave; fijadas ANTES de ver ninguna cifra de Q-C;
ver QC_DECLARACION_PREVIA.json, que guarda el sha256 de este fichero y la hora):
 (1) delta_MIX(oid) = 3 + v[j], j = numpy.random.default_rng([int(oid, 16), 20261116]).integers(313), v = cancel_ex_menos_envio del pool en su orden
     (B2 -> B3 -> B5). MIX_sinBTC (sensibilidad obligatoria B-2.6): mismo sorteo sobre las 187 anclas ETH/SOL/XRP (integers(187)).
 (2) Clase de la ventana de cada orden = clase CAUSAL de s.3.4 con el t_dec de la orden (ledger, reloj LOC = RX): w = floor((t_dec_ms - 200 - dia0_ms)
     / 600000) - 1 sobre perfil_p5_10min de ADD3 (lo |p5-19,25|<=5, hi |p5-39,5|<=5, si no indet); w < 0 o fuera del dia -> indet. La clase
     concurrente (ventana de t_cancel_int) es solo descriptiva (concordancia). Ordenes hi: solo sensibilidad delta + 20,5 (DATA_BLOCKED).
 (3) IC90 por cierre (cl = dia + t_ini//300000, el cluster de brecha_nivel_v3.boot_ev): bootstrap percentil, B = 10.000, semilla 20261116 (s.5.2 M7),
     los MISMOS remuestreos para todas las delta (emparejado). Por dia: 4 observaciones, solo valores puntuales (+ IC por cierre dentro del dia en MIX).
 (4) LODO = la misma tabla sobre los 3 dias restantes al quitar cada dia (delta viene de fuera: no hay parametros que estimar).
 (5) Descriptivos NO preregistrados (no deciden nada): dispersion del sorteo MIX en 1.000 semillas alternativas (20261116 + s, s = 1..1000) y MIX
     "esperado" por la CDF del pool (sin sorteo: q esperada = q_s * P(3 + v >= tf - tcs)).
Etiqueta obligatoria (ADDENDUM1 B-2.7): latencia de 1 dia (13-Nov) y ~2,2 h, solo clase LO; d_proc = 3 ms SUPUESTO, no medido.
Uso: ulimit -v 3000000; nice -n 19 ionice -c3 /usr/bin/python3 -I qc_brecha_nivel_mix.py
Escribe en este directorio: QC_brecha_nivel_mix.json y QC_brecha_nivel_mix.tsv (los .sha256 se escriben fuera con sha256sum)."""
import os, sys, glob, json, ast, hashlib, time, resource, collections, datetime as dt
import numpy as np, pandas as pd

E = os.path.dirname(os.path.abspath(__file__)) + '/'
MIS = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/'
L2 = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'
POOL_F = E + 'l_pool_vigente_13nov.json'; POOL_SHA = '7d92a57c74f7541d77d17dcafa2ed9ec1288ddba3407072ed5264f38a5e69ddf'
ORIG_F = L2 + 'dryrun/brecha_nivel_v3.py'; ORIG_SHA16 = '55880cf512c1228d'
REF_F = L2 + 'dryrun/out_replay/brecha_nivel_v3.json'      # cifras publicadas (L_REAL_Y_DRYRUN_CXB60_11nov.md s.5): reproduccion previa obligatoria
D_PROC = 3; SEED = 20261116; HI_EXTRA = 20.5; BOOT = 10000; N_SEM_DESC = 1000
DIAS = ['2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23']
ETQ = 'latencia de 1 dia (13-Nov) y ~2,2 h, solo clase LO; d_proc = 3 ms SUPUESTO, no medido'
COPIAS = ('pnl_of', 'carga', 'ev', 'sim_con_delta', 'tabla_delta', 'escalones')

# ============================== COPIA LITERAL de brecha_nivel_v3.py (constantes que usan las funciones: H, REB) ==============================
H = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/verif_real/'
REB = 0.2 * 0.07


def pnl_of(q, L, g): return q * (g - L) + q * REB * L * (1 - L)


def carga():
    O = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}, usecols=['oid', 't_cancel_int'])
    R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out_v3/V3_*.pkl'))], ignore_index=True); R = R[R['cov'] == 'ok'].copy(); R = R.merge(O.rename(columns={'t_cancel_int': 'tcs'}), on='oid', how='left')
    T = pd.read_pickle(H + 'out/T1_tx.pkl'); nm = T.groupby('order_hash').n_mk.min()
    R['q_s'] = R.v3d_BASE_f_q.astype(float); R['q_r'] = R.real_q.astype(float); R['n_mk'] = R.oid.map(nm)
    R['cls'] = np.where((R.q_s > 1e-9) & (R.q_r > 1e-9), 'TP', np.where(R.q_s > 1e-9, 'FP', np.where(R.q_r > 1e-9, 'FN', 'TN')))
    R['c_s'] = R.q_s * R.L; R['c_r'] = R.q_r * R.L; R['p_s'] = pnl_of(R.q_s, R.L, R.gana); R['p_r'] = pnl_of(R.q_r, R.L, R.gana); R['cl'] = R.dia + '_' + (R.t_ini // 300000).astype(str)
    return R


def ev(num, den): return float(num / den) if den > 0 else np.nan


def sim_con_delta(R, delta):
    """Correccion del FIN DE SEGMENTO (NUEVO codigo, sin tocar el motor): verif_v3 simula cada orden real hasta `t_fuera` (retorno del DELETE), pero la orden deja de existir en el exchange en t_envio_DELETE + delta (delta = retraso efectivo
    de cancelacion, ~40 ms medido en la carrera cancelacion-vs-print, n=39). Un relleno simulado cuyo primer print tf cae despues de t_envio + delta es un fantasma (la cancelacion ya habia ganado): se anula. R necesita `tcs` (envio del DELETE, s) y `v3d_BASE_f_tf`."""
    q = R.q_s.copy(); tf = R.v3d_BASE_f_tf.astype(float); tcs = R.tcs * 1000.0
    anula = (q > 1e-9) & tcs.notna() & (tf > tcs + delta); q = q.where(~anula, 0.0)
    return q, anula


def tabla_delta(R, deltas=(30, 40, 47, 60, 1e9)):
    rows = []; real = R.q_r > 1e-9; S3 = ev(R.p_r.sum(), R.c_r.sum())
    for d in deltas:
        q, anula = sim_con_delta(R, d); c = q * R.L; p = pnl_of(q, R.L, R.gana); sim = q > 1e-9; tp = int((sim & real).sum()); fp = int((sim & ~real).sum())
        rows.append(dict(delta_ms=('sin correccion (t_fuera)' if d > 1e8 else d), fills_sim=int(sim.sum()), tp=tp, fp=fp, anulados=int(anula.sum()), precision=round(tp / max(int(sim.sum()), 1), 3), recall=round(tp / max(int(real.sum()), 1), 3), ev_sim=round(ev(p.sum(), c.sum()), 4),
                         cierra_brecha=round((ev(p.sum(), c.sum()) - ev(R.p_s.sum(), R.c_s.sum())) / (S3 - ev(R.p_s.sum(), R.c_s.sum())), 3)))
    return pd.DataFrame(rows)


def escalones(R):
    S0 = ev(R.p_s.sum(), R.c_s.sum()); keep = R.cls.isin(['TP']); S1 = ev(R[keep].p_s.sum(), R[keep].c_s.sum()); S2 = ev(R[keep].p_r.sum(), R[keep].c_r.sum()); S3 = ev(R.p_r.sum(), R.c_r.sum())
    return dict(n_ordenes=len(R), S0_sim_todos=round(S0, 4), S1_solo_TP_sim=round(S1, 4), S2_TP_con_cantidad_real=round(S2, 4), S3_real_total=round(S3, 4),
                gap_total=round(S3 - S0, 4), paso_quitar_FP=round(S1 - S0, 4), paso_cantidad_real=round(S2 - S1, 4), paso_anadir_FN=round(S3 - S2, 4))
# ============================== FIN DE LA COPIA LITERAL ==============================


def sha_full(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for ch in iter(lambda: f.read(1 << 20), b''): h.update(ch)
    return h.hexdigest()


def fuentes(path):
    src = open(path).read(); tree = ast.parse(src)
    return {n.name: ast.get_source_segment(src, n) for n in tree.body if isinstance(n, ast.FunctionDef)}


def verifica_copia():
    """Igualdad textual (AST, sin ejecutar el original) de las funciones copiadas y de las constantes H y REB."""
    o, m = fuentes(ORIG_F), fuentes(os.path.abspath(__file__))
    res = {f: bool(f in o and f in m and o[f] == m[f]) for f in COPIAS}
    so = open(ORIG_F).read()
    res['H_igual'] = ("H = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/verif_real/'" in so)
    res['REB_igual'] = ('REB = 0.2 * 0.07' in so)
    return res


def clase_p5(v):                                   # = etapa0_dias_validos.py (ADD2 s.2 / ADD3 s.1)
    if v is None or not np.isfinite(v): return 'indet'
    if abs(v - 19.25) <= 5: return 'lo'
    if abs(v - 39.5) <= 5: return 'hi'
    return 'indet'


def delta_mix(oids, pool, seed=SEED):
    return pd.Series([D_PROC + float(pool[np.random.default_rng([int(o, 16), seed]).integers(len(pool))]) for o in oids.values], index=oids.index)


def rn(x, k=4): return round(float(x), k) if (x is not None and np.isfinite(x)) else None


def metricas(R, q):
    """Metricas de s.7.3 para una cantidad simulada corregida q (alineada con R). EV = sum pnl / sum coste (con rebate, s.5.1)."""
    real = R.q_r > 1e-9; sim = q > 1e-9; sim0 = R.q_s > 1e-9; an = sim0 & ~sim
    c = q * R.L; p = pnl_of(q, R.L, R.gana); nreal = int(real.sum()); nsim = int(sim.sum()); tp = int((sim & real).sum())
    e_sim = ev(p.sum(), c.sum()); e_inf = ev(R.p_s.sum(), R.c_s.sum()); e_real = ev(R.p_r.sum(), R.c_r.sum()); gap = e_real - e_inf
    return dict(n_ordenes=int(len(R)), n_cierres=int(R.cl.nunique()), fills_real=nreal, fills_sim=nsim, tp=tp, fp=nsim - tp, fn=nreal - tp,
                anulados=int(an.sum()), anulados_tp=int((an & real).sum()), anulados_fp=int((an & ~real).sum()),
                precision=(round(tp / nsim, 4) if nsim else None), recall=(round(tp / nreal, 4) if nreal else None),
                coste_sim=round(float(c.sum()), 3), coste_real=round(float(R.c_r.sum()), 3),
                ev_sim=rn(e_sim), ev_sim_sin_corr=rn(e_inf), ev_real=rn(e_real), delta_ev=rn(e_sim - e_inf), gap=rn(gap),
                cierra_brecha=(rn((e_sim - e_inf) / gap, 3) if (np.isfinite(gap) and abs(gap) > 1e-12 and np.isfinite(e_sim)) else None))


def boot(R, qs, B=BOOT, seed=SEED, chunk=1000):
    """IC90 percentil por cierre (cl), remuestreo emparejado (mismos pesos multinomiales para todas las delta)."""
    cols = {'ps': R.p_s, 'cs': R.c_s, 'pr': R.p_r, 'cr': R.c_r}
    for k, q in qs.items(): cols['p|' + k] = pnl_of(q, R.L, R.gana); cols['c|' + k] = q * R.L
    M = pd.DataFrame(cols).groupby(R.cl.values).sum(); A = M.to_numpy(float); n = len(M); ix = {c: i for i, c in enumerate(M.columns)}
    rng = np.random.default_rng(seed); S = np.vstack([rng.multinomial(n, np.full(n, 1.0 / n), size=min(chunk, B - i)) @ A for i in range(0, B, chunk)])
    with np.errstate(divide='ignore', invalid='ignore'):
        e_inf = S[:, ix['ps']] / S[:, ix['cs']]; e_real = S[:, ix['pr']] / S[:, ix['cr']]; gap = e_real - e_inf
        out = dict(n_cierres=n, B=B, semilla=seed, gap_ic90=[round(float(np.nanquantile(gap, .05)), 4), round(float(np.nanquantile(gap, .95)), 4)],
                   ev_real_ic90=[round(float(np.nanquantile(e_real, .05)), 4), round(float(np.nanquantile(e_real, .95)), 4)],
                   ev_sim_sin_corr_ic90=[round(float(np.nanquantile(e_inf, .05)), 4), round(float(np.nanquantile(e_inf, .95)), 4)])
        for k in qs:
            es = S[:, ix['p|' + k]] / S[:, ix['c|' + k]]; de = es - e_inf; fr = de / gap
            out[k] = dict(ev_sim_ic90=[round(float(np.nanquantile(es, .05)), 4), round(float(np.nanquantile(es, .95)), 4)],
                          delta_ev_ic90=[round(float(np.nanquantile(de, .05)), 4), round(float(np.nanquantile(de, .95)), 4)],
                          cierra_ic90=[round(float(np.nanquantile(fr, .05)), 3), round(float(np.nanquantile(fr, .95)), 3)],
                          p_delta_ev_le_0=round(float(np.nanmean(de <= 0)), 4), replicas_nan=int(np.isnan(fr).sum()))
    return out


def main():
    t0 = time.time(); fallos = []
    out = dict(job='qc_brecha_nivel_mix', measurement_id='BF5-REPLAY-COLOC-v1', etapa='Q-C (prereg s.7.3; ADDENDUM1 s.2.2)', etiqueta='EXPLORATORY (explicativo; 4 dias, 100 % R1 por calendario; no decide ninguna palanca)',
               etiqueta_latencia=ETQ, prereg_sha256=open(MIS + 'PREREG_REPLAY_BRECHA_B_16nov.sha256').read().split()[0],
               addendum1_sha256=open(MIS + 'ADDENDUM1_PREREG_REPLAY_BRECHA_B_16nov.sha256').read().split()[0], codigo_sha256=sha_full(os.path.abspath(__file__)),
               comando='cd ' + E + ' && (ulimit -v 3000000; nice -n 19 ionice -c3 /usr/bin/python3 -I qc_brecha_nivel_mix.py)', inicio_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    assert sha_full(MIS + 'PREREG_REPLAY_BRECHA_B_16nov.md') == out['prereg_sha256'], 'prereg alterado'
    assert sha_full(MIS + 'ADDENDUM1_PREREG_REPLAY_BRECHA_B_16nov.md') == out['addendum1_sha256'], 'addendum1 alterado'
    assert sha_full(POOL_F) == POOL_SHA, 'l_pool_vigente_13nov.json no coincide con su sha256 (ADDENDUM1 B-2.5)'
    assert sha_full(ORIG_F)[:16] == ORIG_SHA16, 'brecha_nivel_v3.py cambio respecto al prereg (E6)'
    cp = verifica_copia(); out['copia_literal'] = cp; assert all(cp.values()), ('copia literal NO identica', cp)
    P = json.load(open(POOL_F)); assert P['resumen']['puerta_B2_cancel'].startswith('PASA'), 'puerta B-2 no pasa: la primaria seria l=46 (ADDENDUM1 B-2.3)'
    v_all = [p['cancel_ex_menos_envio'] for p in P['pool']]; v_sb = [p['cancel_ex_menos_envio'] for p in P['pool'] if p['coin'] != 'BTC']
    assert len(v_all) == 313 and len(v_sb) == 187 and all(float(x).is_integer() for x in v_all), 'pool inesperado'
    out['pool'] = dict(fichero=os.path.basename(POOL_F), sha256=POOL_SHA, n=len(v_all), n_sinBTC=len(v_sb), d_proc_ms=D_PROC,
                       delta_ms_pct=dict(zip(('p10', 'p50', 'p90'), [float(x) for x in np.percentile(np.array(v_all) + D_PROC, [10, 50, 90])])),
                       delta_sinBTC_ms_pct=dict(zip(('p10', 'p50', 'p90'), [float(x) for x in np.percentile(np.array(v_sb) + D_PROC, [10, 50, 90])])))
    ent = {os.path.basename(f): sha_full(f)[:16] for f in sorted(glob.glob(H + 'out_v3/V3_*.pkl'))}
    for f in ('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', H + 'out/T1_tx.pkl', REF_F): ent[os.path.basename(f)] = sha_full(f)[:16]
    out['entradas_sha16'] = ent
    # ---------------- muestra (carga literal) + t_dec para la clase
    R = carga()
    O = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', usecols=['oid', 't_dec'])
    assert O.oid.is_unique; R['t_dec_s'] = R.oid.map(O.set_index('oid').t_dec)
    out['muestra'] = dict(n_ordenes=int(len(R)), por_dia={d: int((R.dia == d).sum()) for d in DIAS}, sin_tcs=int(R.tcs.isna().sum()), sin_t_dec=int(R.t_dec_s.isna().sum()),
                          monedas=sorted(R.coin.astype(str).unique().tolist()), oid_unico=bool(R.oid.is_unique))
    # ---------------- Fase 1: reproducir lo publicado (delta 30/40/47/60 y sin correccion; escalones) ANTES de cualquier delta vigente
    ref = json.load(open(REF_F)); TD = tabla_delta(R).to_dict('records'); ES = escalones(R)
    rep_rows = [bool(a == b) for a, b in zip(TD, ref['tabla_delta'])]; rep_esc = bool(ES == ref['escalones'])
    out['reproduccion_publicado'] = dict(fuente=os.path.relpath(REF_F, '/root/polymarket-research/'), filas_tabla_delta_identicas=rep_rows, escalones_identicos=rep_esc,
                                         tabla_delta_recalculada=TD, escalones_recalculados=ES)
    if not (all(rep_rows) and len(TD) == len(ref['tabla_delta']) and rep_esc):
        out['estado'] = 'PARADO: no reproduce lo publicado (stop rule; Fail Loud)'
        json.dump(out, open(E + 'QC_brecha_nivel_mix.json', 'w'), indent=1, default=str); print(json.dumps(out['reproduccion_publicado'], default=str)); sys.exit(2)
    # ---------------- delta vigentes (primaria MIX; rejilla; estres; HI +20,5)
    dm = delta_mix(R.oid, v_all); ds = delta_mix(R.oid, v_sb)
    VAR = collections.OrderedDict()
    VAR['sin_correccion'] = 1e9
    VAR['MIX'] = dm; VAR['MIX_sinBTC'] = ds
    for x in (36, 46, 60): VAR[f'fijo_{x}'] = x
    VAR['estres_111'] = 111
    VAR['MIX+20.5_HI'] = dm + HI_EXTRA; VAR['MIX_sinBTC+20.5_HI'] = ds + HI_EXTRA
    for x in (36, 46, 60): VAR[f'fijo_{x}+20.5_HI'] = x + HI_EXTRA
    VAR['obsoleto_40_circular'] = 40
    Q = {k: sim_con_delta(R, d)[0] for k, d in VAR.items()}
    out['delta_mix_por_orden'] = dict(n=int(len(dm)), p10=float(dm.quantile(.1)), p50=float(dm.median()), p90=float(dm.quantile(.9)),
                                      en_rellenos_sim=dict(n=int((R.q_s > 1e-9).sum()), p50=float(dm[R.q_s > 1e-9].median()), max=float(dm[R.q_s > 1e-9].max())))
    # total
    tot = {k: metricas(R, q) for k, q in Q.items()}
    bt = boot(R, {k: q for k, q in Q.items()})
    for k in tot:
        if k in bt: tot[k]['ic90_cierre'] = bt[k]
    out['total'] = dict(nota='MIX aplicado a TODAS las ordenes (ADDENDUM1 s.2.2: sin ADD3 de 20-21 Oct el corte por clase queda pendiente y la cifra total no se bloquea). '
                             'Las filas +20,5_HI son sensibilidad HI aplicada a todas (B fue R1/HI por calendario); fijo_40 = delta circular obsoleto, solo regresion.',
                        ic90_comun=dict((k, bt[k]) for k in ('n_cierres', 'B', 'semilla', 'gap_ic90', 'ev_real_ic90', 'ev_sim_sin_corr_ic90')), filas=tot)
    # por dia (4) y LODO
    pdia, lodo = {}, {}
    for d in DIAS:
        m = (R.dia == d).values; Rd = R[m]
        pdia[d] = {k: metricas(Rd, Q[k][m]) for k in Q}
        pdia[d]['MIX']['ic90_cierre_dentro_del_dia'] = boot(Rd, {'MIX': Q['MIX'][m]})['MIX']
        Rl = R[~m]; lodo['sin_' + d] = {k: metricas(Rl, Q[k][~m]) for k in Q}
    out['por_dia'] = pdia; out['lodo'] = lodo
    # ---------------- clase de la ventana de cada orden (ADD3; solo COMPLETE)
    lab, est = {}, {}
    for d in DIAS:
        p = MIS + f'exp1/cache/pob_add3_{d}.json'
        if not os.path.exists(p): est[d] = dict(estado='PENDIENTE_ADD3'); continue
        j = json.load(open(p))
        if j.get('estado') != 'COMPLETE': est[d] = dict(estado='ADD3_' + str(j.get('estado'))); continue
        pf = j['C3_suelo_rx_menos_ex']['perfil_p5_10min']; lb = [clase_p5(None if v is None else float(v)) for v in pf]; tt = collections.Counter(lb)
        vpc = j['C3_suelo_rx_menos_ex'].get('ventanas_por_clase', {})
        est[d] = dict(estado='COMPLETE', sha16=sha_full(p)[:16], n_ventanas=len(pf), ventanas=dict(tt), reproduce_ventanas_por_clase=bool(all(tt[k] == vpc.get(k, 0) for k in ('lo', 'hi', 'indet'))))
        if len(pf) == 144 and est[d]['reproduce_ventanas_por_clase']: lab[d] = lb
        else: fallos.append(f'ADD3 {d}: perfil no reproduce ventanas_por_clase o no tiene 144 ventanas')
    d0 = R.dia.map(lambda s: int(pd.Timestamp(s, tz='UTC').timestamp()) * 1000).astype('int64')
    w = np.floor((R.t_dec_s * 1000.0 - 200 - d0) / 600000.0) - 1; wc = np.floor((R.tcs * 1000.0 - d0) / 600000.0)
    def lab_of(dd, ww):
        if dd not in lab: return 'pendiente_ADD3'
        if not np.isfinite(ww) or ww < 0 or ww >= len(lab[dd]): return 'indet'
        return lab[dd][int(ww)]
    R['clase'] = [lab_of(dd, ww) for dd, ww in zip(R.dia.values, w.values)]
    R['clase_conc'] = [lab_of(dd, ww) if np.isfinite(ww) else 'sin_tcs' for dd, ww in zip(R.dia.values, wc.values)]
    con = R[R.clase != 'pendiente_ADD3']
    comp = {}
    for d in DIAS:
        x = R[R.dia == d]
        comp[d] = dict(estado_ADD3=est[d]['estado'], ordenes=dict(collections.Counter(x.clase)), fills_real=dict(collections.Counter(x.clase[x.q_r > 1e-9])),
                       fills_sim=dict(collections.Counter(x.clase[x.q_s > 1e-9])), fp_sin_corr=dict(collections.Counter(x.clase[(x.q_s > 1e-9) & ~(x.q_r > 1e-9)])))
    porc = {}
    if len(con):
        for c in ('lo', 'hi', 'indet'):
            m = (R.clase == c).values
            if not m.any(): porc[c] = dict(n_ordenes=0); continue
            Rc = R[m]
            if c == 'lo': ks = ('sin_correccion', 'MIX', 'MIX_sinBTC', 'fijo_36', 'fijo_46', 'fijo_60', 'estres_111')
            elif c == 'hi': ks = ('sin_correccion', 'MIX+20.5_HI', 'MIX_sinBTC+20.5_HI', 'fijo_36+20.5_HI', 'fijo_46+20.5_HI', 'fijo_60+20.5_HI', 'MIX')
            else: ks = ('sin_correccion', 'MIX')
            porc[c] = {k: metricas(Rc, Q[k][m]) for k in ks}
            if c in ('lo', 'hi'):
                kk = 'MIX' if c == 'lo' else 'MIX+20.5_HI'; porc[c][kk]['ic90_cierre'] = boot(Rc, {kk: Q[kk][m]})[kk]
    out['por_clase'] = dict(regla='clase CAUSAL por t_dec de la orden (w = floor((t_dec_ms-200-dia0)/600000)-1), ADD3 perfil_p5_10min; hi = solo sensibilidad delta+20,5 (DATA_BLOCKED)',
                            estado_ADD3=est, dias_con_clase=sorted(lab), dias_pendientes=[d for d in DIAS if d not in lab],
                            concordancia_causal_vs_concurrente=dict(n=int(len(con)), discordantes=int(((con.clase != con.clase_conc) & (con.clase_conc != 'sin_tcs')).sum())),
                            composicion_por_dia=comp, tablas=porc,
                            aviso='corte por clase PARCIAL: solo dias con ADD3 COMPLETE; 20 y 21-Oct pendientes (ADDENDUM1 s.2.2)')
    # ---------------- descriptivos NO preregistrados: dispersion del sorteo MIX y MIX esperado por CDF
    af = (R.q_s > 1e-9) & R.tcs.notna(); Ra = R[af]; tfa = Ra.v3d_BASE_f_tf.astype(float).values; tca = Ra.tcs.values * 1000.0; oa = Ra.oid.values
    real = R.q_r > 1e-9; e_inf = ev(R.p_s.sum(), R.c_s.sum()); e_real = ev(R.p_r.sum(), R.c_r.sum()); gap = e_real - e_inf
    base_q = R.q_s.copy(); fr, es_ = [], []
    va = np.array(v_all, float)
    for s in range(1, N_SEM_DESC + 1):
        dd = np.array([D_PROC + va[np.random.default_rng([int(o, 16), SEED + s]).integers(len(va))] for o in oa])
        qq = base_q.copy(); qq.loc[Ra.index] = np.where(tfa > tca + dd, 0.0, Ra.q_s.values)
        e = ev(pnl_of(qq, R.L, R.gana).sum(), (qq * R.L).sum()); es_.append(e); fr.append((e - e_inf) / gap)
    fr = np.array(fr); es_ = np.array(es_)
    pan = np.array([np.mean(D_PROC + va < tf - tc) for tf, tc in zip(tfa, tca)])        # P(anula) = P(tf > tcs + 3 + v)
    qe = base_q.copy(); qe.loc[Ra.index] = Ra.q_s.values * (1.0 - pan); ee = ev(pnl_of(qe, R.L, R.gana).sum(), (qe * R.L).sum())
    out['descriptivo_no_preregistrado'] = dict(
        aviso='NO preregistrado; no decide nada. Mide cuanto depende la cifra MIX del sorteo concreto por oid.',
        sorteo_mix_1000_semillas=dict(semillas='20261116+s, s=1..1000', n_ordenes_afectables=int(af.sum()),
                                      cierra_p5_p50_p95=[round(float(np.quantile(fr, q)), 3) for q in (.05, .5, .95)], cierra_min_max=[round(float(fr.min()), 3), round(float(fr.max()), 3)],
                                      ev_sim_p5_p50_p95=[round(float(np.quantile(es_, q)), 4) for q in (.05, .5, .95)],
                                      rango_percentil_de_la_primaria=round(float(np.mean(fr <= (tot['MIX']['cierra_brecha'] or np.nan))), 3)),
        mix_esperado_cdf=dict(ev_sim=round(ee, 4), cierra_brecha=round((ee - e_inf) / gap, 3), fp_anulados_esperados=round(float(pan[~real[af].values].sum()), 2),
                              tp_anulados_esperados=round(float(pan[real[af].values].sum()), 2), n_fp_sin_corr=int((~real[af]).sum()), n_tp_sin_corr=int(real[af].sum())))
    # ---------------- salida
    out['fallos'] = fallos
    out['estado'] = 'COMPLETE (total, por dia, LODO) + PARTIAL (corte por clase: solo ' + ','.join(sorted(lab)) + '; pendientes ' + ','.join(d for d in DIAS if d not in lab) + ')'
    out['recursos'] = dict(cpu_s=round(time.process_time(), 1), pared_s=round(time.time() - t0, 1), maxrss_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1))
    out['fin_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    tmp = E + 'QC_brecha_nivel_mix.json.tmp'; json.dump(out, open(tmp, 'w'), indent=1, default=str); os.replace(tmp, E + 'QC_brecha_nivel_mix.json')
    cab = ['ambito', 'variante', 'n_ordenes', 'n_cierres', 'fills_real', 'fills_sim', 'tp', 'fp', 'fn', 'anulados', 'anulados_tp', 'anulados_fp', 'precision', 'recall',
           'ev_sim', 'ev_sim_sin_corr', 'ev_real', 'delta_ev', 'gap', 'cierra_brecha', 'ev_sim_ic90_cierre', 'delta_ev_ic90_cierre', 'cierra_ic90_cierre']
    lines = ['# Q-C (PREREG_REPLAY_BRECHA_B_16nov s.7.3 + ADDENDUM1 s.2.2), BF5-REPLAY-COLOC-v1. EXPLORATORY, explicativo; no decide ninguna palanca.',
             '# Muestra: 3.796 ordenes reales de B, 20-23 Oct 2026 (ETH/SOL/XRP 5m), V3_<D>.pkl (verif_v3, sello v3 + dedupe, cola BASE) + ordenes_b.csv + T1_tx.pkl.',
             '# EV = sum pnl / sum coste con rebate 0,2*0,07*L*(1-L); cierra_brecha = (EV_sim(delta) - EV_sim(sin corr)) / (EV_real - EV_sim(sin corr)). IC90 percentil por cierre (cl), B=10.000, semilla 20261116.',
             '# delta = d_proc + cancel_ex_menos_envio; MIX = 3 + v_j, sorteo por oid (pool 313, sha 7d92a57c...); ' + ETQ + '. Filas *_HI = sensibilidad HI (DATA_BLOCKED).',
             '# Comando: ' + out['comando'] + '  | codigo sha256 ' + out['codigo_sha256'],
             '\t'.join(cab)]
    def fila(amb, k, mt):
        ic = mt.get('ic90_cierre') or mt.get('ic90_cierre_dentro_del_dia') or {}
        return '\t'.join(str(x) for x in [amb, k] + [mt.get(c) for c in cab[2:20]] + [ic.get('ev_sim_ic90', ''), ic.get('delta_ev_ic90', ''), ic.get('cierra_ic90', '')])
    for k, mt in tot.items(): lines.append(fila('total', k, mt))
    for d in DIAS:
        for k in ('sin_correccion', 'MIX', 'MIX_sinBTC', 'fijo_36', 'fijo_46', 'fijo_60', 'estres_111', 'MIX+20.5_HI'): lines.append(fila('dia_' + d, k, pdia[d][k]))
    for dl in lodo:
        for k in ('MIX', 'MIX_sinBTC', 'fijo_36', 'fijo_46', 'fijo_60', 'MIX+20.5_HI'): lines.append(fila('lodo_' + dl, k, lodo[dl][k]))
    for c, t in porc.items():
        for k, mt in t.items():
            if isinstance(mt, dict) and 'n_ordenes' in mt and k != 'n_ordenes': lines.append(fila('clase_' + c + '_(' + '+'.join(sorted(lab)) + ')', k, mt))
    open(E + 'QC_brecha_nivel_mix.tsv.tmp', 'w').write('\n'.join(lines) + '\n'); os.replace(E + 'QC_brecha_nivel_mix.tsv.tmp', E + 'QC_brecha_nivel_mix.tsv')
    print(json.dumps(dict(estado=out['estado'], copia_literal=all(cp.values()), reproduce=all(rep_rows) and rep_esc, recursos=out['recursos'], fallos=fallos), default=str))


if __name__ == '__main__':
    main()
