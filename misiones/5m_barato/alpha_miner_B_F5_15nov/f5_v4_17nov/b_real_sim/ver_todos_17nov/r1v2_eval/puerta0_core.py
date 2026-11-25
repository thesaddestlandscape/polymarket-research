#!/usr/bin/env python3
"""puerta0_core.py -- R1v2 FASE A (Puerta 0 = veredicto de F5_t como gatillo; PREREG_R1v2_19nov sec.4, CONTRATO v2 sec.2). Funciones PURAS sobre DataFrames de ordenes B simuladas.
NO duplica el motor ni la politica: las ordenes salen de b_policy_sim.run_day (politica REAL de B, DEEP_PEG top-k + repegado) sobre eng_v5.build (= bloque STAMP v3 / ENG dd de passT_v4, sha 85256bcc...),
con EngineBloqueo/f5t/tercil de r1v2_sec7/sec7_core.py (sha en HASHES_sec7.txt). Aqui solo: unidad, EV por tercil, IC90 por DIAS, estratos de suelo (tabla firmada), estres NONE, test de fuga.
Etiqueta de todo resultado: RELLENOS VISIBLES + ESTRES NONE (no es EV de B real). 0 ordenes, 0 red, 0 escritura en data/."""
import os, sys, hashlib
import numpy as np, pandas as pd

ETIQUETA = 'RELLENOS VISIBLES + ESTRES NONE (no es EV de B real)'
FEE = 0.07                      # cripto, takerOnly; el maker no paga (comision_cripto.FEE_CRIPTO)
REBATES = (0.0, 0.2)            # 0 PRIMARIO (ADENDA_01 A3); 0,2 del fee del tomador = sensibilidad
SEED = 20261119; K_BOOT = int(os.environ.get('P0_K', 10000))
DIAS_QUEMADOS_MAX = '2026-11-04'   # ADENDA_03 D: 26-Oct..04-Nov excluidos de Puerta 0 confirmatoria (solo POST HOC)
N_VENT_MIN = 24; FRAC_LO_MIN = 0.5; W_MS = 300_000   # dia valido (contrato sec.4); ventanas de 5 min de la tabla firmada
TABLA_SHA = '8012c16af99b73fb16a727aeeb5e2696408f6bcbf393bcbb6fe38682f141a1d4'
BCOINS = ('eth', 'sol', 'xrp')
TERC = ('bajo', 'medio', 'alto')
# estres NONE uniforme (CONTRATO sec.10b; mismos numeros que sec7_calculos): tasa por orden colocada y EV por relleno NONE
ESTRES = {'sin': None, 'central': (0.018, -0.115), 'pesimista': (0.018, -0.176)}

# ------------------------------------------------------------------ unidad y pnl
def unidad_primer_relleno(R):
    """Unidad = 1.er relleno por (dia, mercado, lado). b_policy_sim ya cierra la puja tras el primer relleno; aqui se COMPRUEBA y, si hubiera mas, se anulan (q=0) y se cuentan en R.attrs['extra_rellenos']."""
    R = R.copy().reset_index(drop=True)
    if not len(R): R.attrs['extra_rellenos'] = 0; return R
    f = R[R.q > 0].sort_values(['dia', 'mid', 'lado', 'tf', 't_arr'], kind='stable')
    dup = f.duplicated(['dia', 'mid', 'lado'], keep='first'); idx = f.index[dup.values]
    R.loc[idx, ['q', 'cost', 'pnl']] = 0.0; R.attrs['extra_rellenos'] = int(len(idx)); return R

def con_rebate(R, reb):
    """pnl + reb * FEE * L(1-L) * q  (rebate = fraccion del fee del tomador, por accion; 0 = primario)."""
    return R.pnl.astype(float) + reb * FEE * R.L.astype(float) * (1.0 - R.L.astype(float)) * R.q.astype(float)

# ------------------------------------------------------------------ tabla de suelo firmada
def lee_tabla_suelo(path, verifica=True):
    h = hashlib.sha256(open(path, 'rb').read()).hexdigest()
    if verifica and h != TABLA_SHA: raise ValueError(f'tabla de suelo con sha {h} != firmado {TABLA_SHA}')
    t = pd.read_csv(path, usecols=['dia', 'coin', 'w0_ms', 'clase_estrato']); t['coin'] = t.coin.str.lower(); return t

def celdas_validas(tab, n_min=N_VENT_MIN, frac_lo=FRAC_LO_MIN):
    """Una fila por (dia, coin): n_lo, n_hi, n_indet, n_sin_datos, n_clasificadas = lo+hi+indet; valida = n_clas >= n_min Y n_lo/n_clas >= frac_lo. sin_datos NO se clasifica ni se imputa."""
    g = tab.pivot_table(index=['dia', 'coin'], columns='clase_estrato', values='w0_ms', aggfunc='count', fill_value=0).reset_index()
    for c in ('lo', 'hi', 'indet', 'sin_datos'):
        if c not in g.columns: g[c] = 0
    g['n_clas'] = g.lo + g.hi + g.indet
    g['frac_lo'] = np.where(g.n_clas > 0, g.lo / g.n_clas.where(g.n_clas > 0, 1), np.nan)
    g['valida'] = (g.n_clas >= n_min) & (g.frac_lo >= frac_lo)
    return g[['dia', 'coin', 'lo', 'hi', 'indet', 'sin_datos', 'n_clas', 'frac_lo', 'valida']]

def dias_lo_validos(cel, coins=BCOINS):
    """INTERPRETACION (no fijada en el contrato; el chief la confirma): dia valido = TODAS las monedas de B presentes (ETH/SOL/XRP) validas. Se publican tambien las alternativas."""
    c = cel[cel.coin.isin(coins)]
    todas = sorted(d for d, g in c.groupby('dia') if len(g) == len(coins) and g.valida.all())
    alguna = sorted(d for d, g in c.groupby('dia') if g.valida.any())
    return dict(todas_las_monedas=todas, alguna_moneda=alguna)

def anota_suelo(R, tab, cel):
    """clase_estrato de la ventana de 5 min que contiene t_dec (floor a W_MS), de la tabla firmada (ESTRATO, nunca rasgo) y validez de la celda (dia, coin). Ventana sin fila -> 'sin_tabla'."""
    R = R.copy(); w0 = (R.t_dec.astype('int64') // W_MS) * W_MS
    k = pd.DataFrame(dict(dia=R.dia.values, coin=R.coin.str.lower().values, w0_ms=w0.values))
    m = k.merge(tab, on=['dia', 'coin', 'w0_ms'], how='left'); R['estrato'] = m.clase_estrato.fillna('sin_tabla').values
    v = k.merge(cel[['dia', 'coin', 'valida']], on=['dia', 'coin'], how='left'); R['celda_valida'] = v.valida.fillna(False).astype(bool).values
    return R

# ------------------------------------------------------------------ agregados por dia y bootstrap por DIAS
def agrega_dia(R, pnl_col='pnl_x'):
    """por (dia, grupo): n ordenes, n rellenos, coste, pnl. grupo = 'bm' (bajo U medio) | 'alto' | 'inval'."""
    R = R.copy(); R['grupo'] = np.where(R.tercil.isin(('bajo', 'medio')), 'bm', np.where(R.tercil == 'alto', 'alto', 'inval'))
    R['_f'] = (R.q > 0).astype(int)
    g = R.groupby(['dia', 'grupo']).agg(n=('q', 'size'), nf=('_f', 'sum'), cost=('cost', 'sum'), pnl=(pnl_col, 'sum')).reset_index()
    return g

def aplica_estres(g, tasa, ev_none, c_none):
    """suma n_none = tasa*n ordenes del grupo-dia, cada una de coste c_none (coste medio de TODOS los rellenos, no por tercil: uniforme) y EV ev_none. Idem sec7_calculos.estres_none."""
    g = g.copy(); nn = tasa * g.n; g['cost'] = g.cost + nn * c_none; g['pnl'] = g.pnl + nn * c_none * ev_none; return g

def _ev(p, c): return float(p / c) if c > 0 else float('nan')

def resumen_grupo(g, grupo):
    x = g[g.grupo == grupo]; n = int(x.n.sum()); nf = int(x.nf.sum()); c = float(x.cost.sum()); p = float(x.pnl.sum())
    return dict(n_ordenes=n, n_rellenos=nf, p_relleno=(nf / n if n else float('nan')), coste=c, pnl=p, EV_eur=_ev(p, c), pnl_por_orden=(p / n if n else float('nan')), n_dias=int(x.dia.nunique()))

def boot_diff(g, rng, K=None):
    """diferencia EV_eur(bm) - EV_eur(alto) con IC90 por DIAS (percentiles 5-95 del bootstrap por dia con reemplazo; EV = Sigma pnl/Sigma coste dentro de cada remuestreo). Sorteos con EV indefinido se descartan y se cuentan."""
    K = K or K_BOOT; dias = sorted(g.dia.unique()); nd = len(dias)
    if nd < 2: return dict(n_dias=nd, diff=float('nan'), lo=float('nan'), hi=float('nan'), n_descartados=0, nota='INSUFFICIENT: <2 dias')
    P = np.zeros((nd, 2)); C = np.zeros((nd, 2))
    for i, d in enumerate(dias):
        for j, gr in enumerate(('bm', 'alto')):
            x = g[(g.dia == d) & (g.grupo == gr)]; P[i, j] = x.pnl.sum(); C[i, j] = x.cost.sum()
    def diff(idx):
        p = P[idx].sum(0); c = C[idx].sum(0)
        return (p[0] / c[0] - p[1] / c[1]) if c[0] > 0 and c[1] > 0 else np.nan
    pt = diff(np.arange(nd)); ds = np.array([diff(rng.integers(0, nd, nd)) for _ in range(K)]); ok = ds[np.isfinite(ds)]
    return dict(n_dias=nd, diff=float(pt), lo=float(np.percentile(ok, 5)) if len(ok) else float('nan'), hi=float(np.percentile(ok, 95)) if len(ok) else float('nan'), n_descartados=int(K - len(ok)))

def sin_mejores_dias(g, k=2):
    """diff (bm - alto) quitando los k dias con mayor pnl total (bm+alto): informativo (EV sin los 2 mejores dias)."""
    tot = g[g.grupo.isin(('bm', 'alto'))].groupby('dia').pnl.sum().sort_values(ascending=False)
    q = g[~g.dia.isin(list(tot.index[:k]))]; a, b = resumen_grupo(q, 'bm'), resumen_grupo(q, 'alto')
    return dict(dias_quitados=list(tot.index[:k]), diff=a['EV_eur'] - b['EV_eur'] if np.isfinite(a['EV_eur']) and np.isfinite(b['EV_eur']) else float('nan'), n_dias=int(q.dia.nunique()))

def veredicto_puerta0(ev_alto, d):
    """PREREG sec.4: EV_eur(bm)-EV_eur(alto) > 0 con IC90 por DIAS (limite inferior > 0) Y EV_eur(alto) <= 0. Fallo => F5_t AMBER-exploratorio. IC no calculable => INSUFFICIENT (no se cierra la puerta)."""
    if not np.isfinite(d['diff']) or not np.isfinite(d['lo']) or not np.isfinite(ev_alto): return 'INSUFFICIENT'
    return 'PASA' if (d['diff'] > 0 and d['lo'] > 0 and ev_alto <= 0) else 'NO_PASA'

def evalua(R, dias, estrato=None, reb=0.0, estres='sin', c_none=None, seed=SEED, K=None, dias_todas=None):
    """Una celda de la rejilla: ordenes de `dias` (+ filtro de estrato), pnl con rebate `reb`, estres NONE opcional. Devuelve EV por tercil/agrupado, diff, IC90 por dias, sin 2 mejores dias, veredicto."""
    Q = R[R.dia.isin(dias)].copy()
    if estrato == 'lo': Q = Q[Q.estrato == 'lo']
    elif estrato == 'lo_valido': Q = Q[(Q.estrato == 'lo') & Q.celda_valida]
    elif estrato == 'todas_las_monedas': Q = Q[(Q.estrato == 'lo') & Q.celda_valida & Q.dia.isin(list(dias_todas or []))]       # sensibilidad ADENDA_06 2: dia valido solo si ETH, SOL y XRP validas a la vez
    elif estrato == 'hi': Q = Q[Q.estrato == 'hi']
    elif estrato == 'indet': Q = Q[Q.estrato.isin(('indet', 'sin_tabla', 'sin_datos'))]
    Q['pnl_x'] = con_rebate(Q, reb)
    if estres != 'sin' and c_none is None: c_none = float(Q[Q.q > 0].cost.mean()) if (Q.q > 0).any() else 0.0
    g = agrega_dia(Q)
    if estres != 'sin': tasa, evn = ESTRES[estres]; g = aplica_estres(g, tasa, evn, c_none)
    por_terc = {}
    for t in TERC + ('inval',):
        x = Q[Q.tercil == t]
        if not len(x): por_terc[t] = dict(n_ordenes=0); continue
        gg = agrega_dia(x); gg = aplica_estres(gg, *ESTRES[estres], c_none) if estres != 'sin' else gg
        por_terc[t] = resumen_grupo(gg, gg.grupo.iloc[0])
    rng = np.random.default_rng(seed); d = boot_diff(g, rng, K); bm = resumen_grupo(g, 'bm'); al = resumen_grupo(g, 'alto')
    return dict(dias=sorted(Q.dia.unique()), bm=bm, alto=al, inval=resumen_grupo(g, 'inval'), por_tercil=por_terc, diff_ic90_dias=d, sin_2_mejores_dias=sin_mejores_dias(g),
                veredicto_bruto=veredicto_puerta0(al['EV_eur'], d), n_dias=d['n_dias'], etiqueta=ETIQUETA + ' | veredicto_bruto NO es el oficial: leer veredicto_combinado')

# ------------------------------------------------------------------ validez de F5_t: % invalido, cambio de tercil, fuga NaN
def pct_invalido(R):
    """% de ordenes con F5_t invalido (= no operar) por tercil-grupo y moneda, y EV de B-sin-filtro (pnl con rebate 0) en las invalidas (por si el invalido censura)."""
    out = {}
    for c, g in list(R.groupby('coin')) + [('todas', R)]:
        n = len(g); inv = g[g.tercil == 'inval']; f = inv[inv.q > 0]
        out[c] = dict(n_ordenes=int(n), n_inval=int(len(inv)), pct_inval=float(len(inv) / n) if n else float('nan'), EV_eur_inval=_ev(float(f.pnl.sum()), float(f.cost.sum())), n_rellenos_inval=int(len(f)),
                      pct_por_tercil={t: float((g.tercil == t).mean()) if n else float('nan') for t in TERC + ('inval',)})
    return out

def cambio_tercil(R):
    """Fraccion de ordenes (ambas validas) con tercil de F5_t (rx<=t) distinto del tercil con reloj EXCHANGE (ex<=t). Limite contractual <=35 %. 'F5' del contrato se aproxima por el mismo tamano con reloj exchange: SUPUESTO declarado."""
    a = R[(R.tercil != 'inval') & (R.tercil_ex != 'inval')]
    return dict(n_validas_ambas=int(len(a)), frac_cambia=float((a.tercil != a.tercil_ex).mean()) if len(a) else float('nan'), limite=0.35, ok=bool(len(a) and (a.tercil != a.tercil_ex).mean() <= 0.35))

def auc(score, y):
    """AUC de Mann-Whitney (rangos medios): P(score|y=1 > score|y=0) + 0,5 P(=). NaN si falta una clase. Devuelve (auc, n1, n0, z) con z normal aprox. bajo H0 (AUC=0,5)."""
    s = np.asarray(score, float); y = np.asarray(y, int); n1 = int((y == 1).sum()); n0 = int((y == 0).sum())
    if n1 == 0 or n0 == 0: return float('nan'), n1, n0, float('nan')
    r = pd.Series(s).rank(method='average').values; u = r[y == 1].sum() - n1 * (n1 + 1) / 2.0; a = u / (n1 * n0)
    se = np.sqrt(n1 * n0 * (n1 + n0 + 1) / 12.0) / (n1 * n0); return float(a), n1, n0, float((a - 0.5) / se)

def test_fuga_nan(R, banda=(0.40, 0.60), n_min_inval=20):
    """CONTRATO sec.11-5: el indicador 'F5_t invalido' NO debe predecir el desenlace (AUC ~ 0,5 por DIA). y = gana de NUESTRO token (R.gana, etiqueta posterior: solo etiqueta, nunca rasgo).
    banda [0,40;0,60] y n_inval>=20 CONGELADAS en ADENDA_06 sec.3; dias con n_inval<20 se reportan sin decidir. Se aplica SOLO a dias confirmatorios (05-09 Nov); 03-04 aparte POST HOC. Por dia y pooled-por-dia; fuga_sospechosa si algun dia con n_inval>=n_min cae fuera de la banda."""
    if not len(R): return dict(por_dia=[], banda_provisional=banda, n_min_inval=n_min_inval, dias_evaluables=0, fuga_sospechosa=None, estado='INSUFFICIENT')
    filas = []
    for d, g in R.groupby('dia'):
        ind = (g.tercil == 'inval').astype(int).values; y = (g.gana > 0.5).astype(int).values
        a, n1, n0, z = auc(ind, y); filas.append(dict(dia=d, n=int(len(g)), n_inval=int(ind.sum()), auc_inval_vs_gana=a, z=z, n_gana=int(y.sum())))
    F = pd.DataFrame(filas); ev = F[(F.n_inval >= n_min_inval) & F.auc_inval_vs_gana.notna()]
    fuga = bool(((ev.auc_inval_vs_gana < banda[0]) | (ev.auc_inval_vs_gana > banda[1])).any()) if len(ev) else None
    return dict(por_dia=F.to_dict('records'), banda_provisional=banda, n_min_inval=n_min_inval, dias_evaluables=int(len(ev)), fuga_sospechosa=fuga, estado=('INSUFFICIENT' if fuga is None else ('FUGA_SOSPECHOSA' if fuga else 'OK')))

# ------------------------------------------------------------------ F5 con reloj exchange (solo para la metrica de cambio de tercil)
def f5_ex(own, t, max_age=30000):
    """mismo tamano que sec7_core.f5t pero con la fila de mayor sello EXCHANGE <= t (SerieL1.idx_ex). Solo para cambio_tercil; NUNCA como decision."""
    i = own.idx_ex(t) if own is not None else -1
    if i < 0 or t - int(own.ex[i]) > max_age: return None
    a = own.asz[i]
    return float(np.log1p(a)) if np.isfinite(a) and a >= 0 else None

def anota_ex(R, series_por_k, tercil):
    R = R.copy(); v = [f5_ex(series_por_k(int(k)), int(t)) for k, t in zip(R.k, R.t_dec)]
    R['f5ex'] = [np.nan if x is None else x for x in v]; R['tercil_ex'] = [tercil(x) for x in v]; return R

# ------------------------------------------------------------------ veredicto OFICIAL combinado (ADENDA_06 + code-review 3)
UMBRAL_DIAS_LO = 10
def _fin(x): return x is not None and np.isfinite(x)

def veredicto_combinado(c0, c1, n_dias_lo_validos, fuga_estado, faltantes=None):
    """Veredicto oficial de una celda (misma combinacion conj|rebate|estres|estrato en bloq0 y bloq1). Orden de precedencia:
      1 fuga NaN confirmatoria FUGA_SOSPECHOSA -> BLOCKED_FUGA (todas las celdas);  2 faltan dias confirmatorios COMPLETE -> INSUFFICIENT (lista en la celda);
      3 bloq0 INSUFFICIENT o bloq1 sin diff/EV_alto -> INSUFFICIENT;  4 'cumpliria' = bloq0 PASA (diff>0, IC90 por dias lo>0, EV_alto<=0) Y bloq1 con diff>0 y EV_alto<=0 (mismo signo);
      5 <10 dias lo validos -> nunca PASA: PARTIAL si cumpliria, INSUFFICIENT si no;  si no, PASA / NO_PASA. n_dias en cada veredicto."""
    d0 = c0['diff_ic90_dias']; d1 = c1['diff_ic90_dias'] if c1 else dict(diff=float('nan'))
    base = dict(n_dias=d0['n_dias'], n_dias_bloq1=d1.get('n_dias'), n_dias_lo_validos=int(n_dias_lo_validos), dias_faltantes=list(faltantes or []), bruto_bloq0=c0['veredicto_bruto'], bruto_bloq1=c1['veredicto_bruto'] if c1 else None,
                diff_bloq0=d0['diff'], diff_bloq1=d1['diff'], ev_alto_bloq0=c0['alto']['EV_eur'], ev_alto_bloq1=c1['alto']['EV_eur'] if c1 else float('nan'), etiqueta=ETIQUETA)
    if fuga_estado == 'FUGA_SOSPECHOSA': return dict(base, veredicto='BLOCKED_FUGA')
    if faltantes: return dict(base, veredicto='INSUFFICIENT', motivo='faltan dias confirmatorios COMPLETE')
    if c1 is None or c0['veredicto_bruto'] == 'INSUFFICIENT' or not _fin(d1['diff']) or not _fin(base['ev_alto_bloq1']): return dict(base, veredicto='INSUFFICIENT', motivo='celda no evaluable en bloq0/bloq1')
    cumple = c0['veredicto_bruto'] == 'PASA' and d1['diff'] > 0 and base['ev_alto_bloq1'] <= 0
    if n_dias_lo_validos < UMBRAL_DIAS_LO: return dict(base, veredicto='PARTIAL' if cumple else 'INSUFFICIENT', motivo=f'<{UMBRAL_DIAS_LO} dias lo validos: nunca PASA')
    return dict(base, veredicto='PASA' if cumple else 'NO_PASA')

def t_ex_fills(R, fills):
    """columna t_ex_fill = sello EXCHANGE del relleno (fills[(k,L4,t_arr,tf)]['t_ex'] de EngineBloqueo); NaN si no consta (bloqueo apagado: tf de print ya es exchange). Para bloqueo, tf = t_rx: la efectividad de cancelar se mide contra t_ex."""
    R = R.copy(); R['t_ex_fill'] = [fills.get((int(r.k), round(float(r.L), 4), int(r.t_arr), int(r.tf)), {}).get('t_ex', np.nan) if r.q > 0 else np.nan for r in R.itertuples()]; return R
