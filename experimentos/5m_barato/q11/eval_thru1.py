#!/usr/bin/env python3
"""Evaluador forward H-Q11-THRU1 (PREREG_Q11_THRU1_FWD.md sha 68ca25a0, ADDENDUM3 sha c991602c, ADDENDUM4 sha 3dac1bf4: REFUTA solo con evidencia contraria significativa, tabla thru1 A-H, tope). Solo lectura de pickles + escritura de salida; 0 ordenes. EXPLORATORIA.
Entradas por dia D (producidas por scripts SIN tocar, ver --producir): toxicidad_thru1/out/RT_D.pkl (passT.py: G0, GEO6, CXJ150, NJ3A, CXJ1000, CXB_l, GEO6NJ3) y
redteam/out/RT_D.pkl (rt_sim.py: G0/GEO6/PG_O50 x BASE/STRICT/OPT/CROSS/THIN). PC_AS = G0 menos los rellenos NO de las unidades (cierre, moneda) marcadas (exacto: un token por orden).
Modos:  --aceptacion            prueba sobre QUEMADOS (G0 2938, -166,9, EV -0,076; thru1 n 2321 EV -0,125; dPnL GEO6 +140, CXJ150 +128 +-1): escribe thru1_fwd/aceptacion.json
        --evaluar [--hoy D]      informe diario DESCRIPTIVO + checkpoints 10/20 + estado terminal (thru1_fwd/estado_thru1.json); exige aceptacion PASS y sha de codigo
        --producir D             genera Po_D (modelo OWN), passT D y rt_sim D con nice/ionice/ulimit (pesado: fuera de 06:00-09:15Z, uno a la vez)
        --desde/--salida         ensayo (p.ej. --desde 2026-10-26 --salida /tmp/x --sin-validez)"""
import sys, os, json, hashlib, argparse, subprocess, glob, ast, datetime as dt
sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/forward_sol013/')
import numpy as np, pandas as pd
import q11_decision as Q
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/'; PB = P2 + 'precursores_barrido/out/'
TX, RTD, BCO, RXD = HERE + 'toxicidad_thru1/out/', HERE + 'redteam/out/', HERE + 'barrido_corr/out/', HERE + 'redteam/out_cxj150/'
PRICES = '/root/polymarket-research/data/prices/'
FWD_DESDE = '2026-11-09'; DESCRIPTIVOS_DESDE = '2026-11-07';   # ADDENDUM6 3.1: 07 y 08-Nov DESCRIPTIVOS-QUEMADOS (no cuentan)
SEED = 20261107; B = 4000
PREREG = '/root/polymarket-research/misiones/5m_barato/docs/reverse-engineering/casos/RE-THRU1/PREREG_Q11_THRU1_FWD.md'
SHAS = {  # codigo/modelo registrados (prereg: engine.py, passT.py, rt_sim.py, modelo OWN; engine fijado aqui el 06-Nov con el valor vigente)
    P2 + 'escalera_B/engine.py': 'a7b8431a73952524917ffd90e65b2dcf2779fabd3c452bc0407d36e34b1e8feb',
    HERE + 'toxicidad_thru1/passT.py': 'a8b9d7a0158fd0b0cf47582c499d6c1cc870269310c8ef4481482733d1c64038',
    HERE + 'redteam/rt_sim.py': '86b14afbf91b308ab6185e0060427047fc644a6a0ac33813127627ef507f652b',
    HERE + 'redteam/rt_cxj150_cross.py': 'ef9fde82e977cb87b266e57b0b0e1477a3bb5e87b261a78b16fd090561ca37fe',   # CXJ150 bajo BASE/CROSS (nuevo 09-Nov, ADDENDUM4; lee rt_sim.py/passT.py con sha comprobado)
    HERE + 'forward_pg/modelo_own.pkl': 'f80d7b573bd74084a8fb6b601af84f0eab7c7d8dd155f1f17d90070d28eb3839',
    HERE + 'forward_pg/modelo_own.json': '35adc359660d8b99f3719d73989d1f9f9dc2ef20a974e159a0ec577cf69ab8dd',
    HERE + 'forward_pg/entrenar_own.py': 'ea9f59056d0e3283bba5bc498a6242093eb20cbf2cbcb4d6e5acf94f49b30a68',
    PREREG: '68ca25a04bb4fb7cb8f9f5161b57155baaf6e9ead89170ad03ad284100bfe33e'}
ARMS = ['PG_O50', 'GEO6', 'CXJ150', 'PC_AS']; FV = ('BASE', 'STRICT', 'OPT', 'THIN', 'CROSS')
QUEMADOS = [f'2026-10-{d}' for d in range(26, 32)] + [f'2026-11-0{d}' for d in range(1, 5)]
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def eval_sha():
    """sha de la aceptacion = sha256(sha(eval_thru1.py) + sha(q11_decision.py)): editar cualquiera de los dos invalida aceptacion.json (la guardia por sha se mantiene)."""
    return hashlib.sha256((sha(__file__) + sha(Q.__file__)).encode()).hexdigest()
def check_shas():
    return [f'{os.path.basename(p)}: {sha(p)[:12]} != {h[:12]}' for p, h in SHAS.items() if not os.path.exists(p) or sha(p) != h]
def atomic(path, text):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True); tmp = path + '.tmp'
    with open(tmp, 'w') as f: f.write(text); f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)
# ---------------- carga ----------------
def cargar(dias):
    """-> (T, R, S, RX, err). err = lista de ERROR_DATOS (filas con dia != D): el llamador NO escribe estado y muestra los terminales (ADDENDUM4 5b)."""
    T, R, S, X, err = [], [], [], [], []
    for d in dias:
        try:   # un pickle ilegible es ERROR_DATOS (no una excepcion que deje el evaluador sin informe ni B2)
            T.append(pd.read_pickle(f'{TX}RT_{d}.pkl')); R.append(pd.read_pickle(f'{RTD}RT_{d}.pkl')); S.append(pd.read_pickle(f'{TX}SEGT_{d}.pkl'))
            if os.path.exists(f'{RXD}RX_{d}.pkl'): X.append(pd.read_pickle(f'{RXD}RX_{d}.pkl'))   # CXJ150 bajo BASE/CROSS (rt_cxj150_cross.py); su falta solo invalida el dia para CXJ150
        except Exception as e_:
            err.append(f'RT_{d}.pkl (o SEGT/RX del dia {d}) ilegible: {type(e_).__name__}: {e_}'); return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), err
        for nm, x in (('passT', T[-1]), ('rt_sim', R[-1])) + ((('rt_cxj150_cross', X[-1]),) if os.path.exists(f'{RXD}RX_{d}.pkl') else ()):
            if len(x) and (x['dia'].astype(str) != d).any(): err.append(f'{nm} RT_{d}.pkl: filas con dia != {d}')
    cat = lambda L: pd.concat(L, ignore_index=True) if L else pd.DataFrame()
    return cat(T), cat(R), cat(S), cat(X), err
def feat_chainlink(dias, units, hoy=None, cache=None):
    """r1, r4 por unidad (fin, act): a = fin-303 s; r1 = ln(CL(a)/CL(a-3600)), r4 = ln(CL(a-3600)/CL(a-18000)); source=='chainlink', recepcion, tolerancia 20 s.
    Serie por dia desde la cache propia (q11_decision.cl_dia: el CSV de data/prices rota a ~20 d) con UNA lectura por dia. Fail-closed: CSV ausente/vacio => ERROR_DATOS
    del brazo PC_AS (se devuelve en `err`; r1/r4 quedan NaN y el llamador NO los usa). -> (units con r1, r4, err)"""
    need = sorted({(pd.Timestamp(d) - pd.Timedelta(days=k)).strftime('%Y-%m-%d') for d in dias for k in (0, 1)})
    out = units.copy(); out['r1'] = np.nan; out['r4'] = np.nan
    S, err = Q.cl_series(need, Q.COINS, hoy, cache)
    if err: return out, err
    for coin in Q.COINS:
        m = (units.act == coin).values
        if not m.any(): continue
        ms, pp = S[coin]
        def px(t):
            i = np.searchsorted(ms, t, side='right') - 1; ok = (i >= 0) & (t - ms[np.clip(i, 0, None)] < 20000); return np.where(ok, pp[np.clip(i, 0, None)], np.nan)
        a = (units.fin.values[m] * 1000 - 303000).astype('int64')
        with np.errstate(all='ignore'): out.loc[m, 'r1'] = np.log(px(a) / px(a - 3600000)); out.loc[m, 'r4'] = np.log(px(a - 3600000) / px(a - 18000000))
    return out, []
def armar_base(T, R, S, X, dias, hoy=None, cache=None):
    """-> dict nombre -> DataFrame de rellenos (cols fin,dia,act,lado,pnl,cost) y dict (arm,fv)-> idem para cotas; unit table de PC_AS."""
    g0 = T[T['var'] == 'G0']; A = {'G0': g0, 'GEO6': T[T['var'] == 'GEO6'], 'CXJ150': T[T['var'] == 'CXJ150']}
    for v in ('NJ3A', 'CXJ1000', 'GEO6NJ3', 'CXB150', 'CXB300', 'CXB1000', 'CXB3000'): A[v] = T[T['var'] == v]
    for p in ('G0', 'GEO6', 'PG_O50'):
        for f in FV: A[f'rt_{p}_{f}'] = R[(R.pol == p) & (R.fv == f)]
    for f in ('BASE', 'CROSS'): A[f'rt_CXJ150_{f}'] = X[X.fv == f] if len(X) else R.iloc[:0]   # script rt_cxj150_cross.py (ADDENDUM4: C3 de CXJ150)
    # PC_AS: unidades NO de los segmentos G0 (cobertura del rasgo) y marca por (fin, act)
    U = S[S.lado == 'NO'][['dia', 'fin', 'act']].drop_duplicates().reset_index(drop=True); U, cl_err = feat_chainlink(dias, U, hoy, cache)
    U['flag'] = (U.r1 > 0) & (U.r4 < 0); cov = float((U.r1.notna() & U.r4.notna()).mean()) if len(U) else float('nan')   # ADDENDUM7 A2: r1 Y r4 finitos
    fl = set(map(tuple, U[U.flag][['fin', 'act']].values))
    def pcas(x): return x[~((x.lado == 'NO') & pd.Series([(a, b) in fl for a, b in zip(x.fin, x.act)], index=x.index))] if len(x) else x
    A['PC_AS'] = pcas(g0)
    for f in FV: A[f'rt_PC_AS_{f}'] = pcas(A[f'rt_G0_{f}'])
    return A, U, cov, cl_err
# ---------------- metricas ----------------
def pc(x): return x.groupby('fin').pnl.sum() if len(x) else pd.Series(dtype=float)
def dser(a, b): return pc(a).sub(pc(b), fill_value=0.0)
def dia_of(x): return x.groupby('fin').dia.first()
def boot_sum(v, seed, Bn=B):
    v = np.asarray(v, float)
    if len(v) < 3: return None
    return v[np.random.default_rng(seed).integers(0, len(v), (Bn, len(v)))].sum(axis=1)
def stats_dpnl(a, b, days):
    s = dser(a, b); n = len(s); d = pd.concat([dia_of(a), dia_of(b)]).groupby(level=0).first().reindex(s.index)
    sd = s.groupby(d.values).sum().reindex(days).fillna(0.0)
    vc, vd = boot_sum(s.values, SEED), boot_sum(sd.values, SEED)
    r = dict(tot=float(s.sum()) if n else float('nan'), ncierres=n, nnz=int((s.abs() > 1e-12).sum()), dias=sd.to_dict(),
             ic_c=(Q.q(vc, .05), Q.q(vc, .95), Q.q(vc, .0125), Q.q(vc, .9875)), ic_d=(Q.q(vd, .05), Q.q(vd, .95), Q.q(vd, .0125), Q.q(vd, .9875)))
    r['sin2dias'] = float(sd.sort_values(ascending=False).iloc[2:].sum()) if len(sd) > 2 else float('nan')
    r['sin5cierres'] = float(s.sort_values(ascending=False).iloc[5:].sum()) if n > 5 else float('nan')
    return r
def ev_stats(x):
    e = Q.ev(x); v = Q.vec_cierre(x, B, SEED); s2 = Q.sin2(x)
    c = x.groupby('fin').pnl.sum().sort_values(ascending=False); k5 = c.iloc[5:].sum() if len(c) > 5 else float('nan')
    return dict(ev=e, ic_inf=Q.q(v, .05), ic_inf_p=Q.q(v, .0125), sin2dias=s2, sin5=float(k5))
def placebo_pcas(U, pnl_no, days_cnt):
    """PC_AS placebo (1000 perm.): permuta dentro de cada dia el signo de r1 entre unidades (cierre, moneda) NO; estadistico dPnL BASE = -sum pnl G0-NO de las unidades marcadas."""
    u = U[U.r1.notna() & U.r4.notna() & U.dia.isin(days_cnt)].reset_index(drop=True)
    if not len(u): return Q.NAN, Q.NAN, Q.NAN
    p = np.array([pnl_no.get((f, a), 0.0) for f, a in zip(u.fin, u.act)]); sg = np.sign(u.r1.values); r4 = u.r4.values
    grp = [np.where(u.dia.values == d)[0] for d in pd.unique(u.dia)]; stat = lambda s: -p[(s > 0) & (r4 < 0)].sum()
    obs = stat(sg); rng = np.random.default_rng(SEED); perm = []
    for _ in range(1000):
        sp = sg.copy()
        for ix in grp: sp[ix] = rng.permutation(sg[ix])
        perm.append(stat(sp))
    m = float(np.mean(perm)); pv = (1 + sum(abs(x - m) >= abs(obs - m) for x in perm)) / 1001
    return float(obs), m, pv
# ---------------- validez de dia ----------------
# ---------------- salud del feed Binance (ADDENDUM6 sec. 2, 2b, 5) ----------------
CRITERIO = 'ADDENDUM7'                      # clave de validez_D.json: una cache sin ella (regla vieja de cobertura por moneda) se rechaza y se recalcula
SIMB_FLUJO = ('BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB')   # ADDENDUM7 B3: flujo CONJUNTO de TODOS los simbolos del logger (= libro_estado_ws._SIMB_BN, una sola conexion; un test lo cruza con el codigo); BTC/DOGE/BNB centinelas, no entran en ningun brazo
SIMB_H3 = ('BTC', 'ETH', 'SOL', 'XRP')      # H3: los unicos con kline REST y los que entran o centinelean los brazos
SIMB_4 = SIMB_H3                           # sensibilidad H2 con 4 simbolos (ADDENDUM7 B4)
H1_S, H2_MIN, H3_MIN = 60, 0.95, 0.95       # decisorios (por diseno, ADDENDUM6 3.3); sensibilidad solo se REPORTA
H1_VAR, H3_VAR = (50, 60, 73), (0.93, 0.95, 0.97)
KCACHE = '/root/polymarket-research-datalogs/q11_binance_salud/'   # klines REST 1m del dia por simbolo (no se repiten las llamadas)
DAY_MS = 86400000
class ErrorDatos(Exception): pass
BIGMS = np.iinfo(np.int64).max
REST_TRIES, ESPERA_REST = 3, 2              # reintentos con espera creciente (2, 4 s) antes de declarar ERROR_DATOS por REST
def acc_nuevo():
    """Acumulador en STREAMING del x_D (memoria O(86400): ni se guardan las filas ni se reescanea): por simbolo de SIMB_FLUJO y segundo de RECEPCION, min y max del tick (ms; un tick por segundo basta para
    todos los huecos >= 1 s, exactos); n por simbolo; por segundo de hora de TRADE T, min y max conjuntos de los 6 simbolos (H1b); suma de q por minuto de T de los simbolos de SIMB_H3 (H3)."""
    return dict(rmin=np.full((len(SIMB_FLUJO), 86400), BIGMS, np.int64), rmax=np.full((len(SIMB_FLUJO), 86400), -1, np.int64), n=np.zeros(len(SIMB_FLUJO), np.int64),
                tmin=np.full(86400, BIGMS, np.int64), tmax=np.full(86400, -1, np.int64), qsum=np.zeros((len(SIMB_H3), 1440)))
def _minmax(mn, mx, sec, ms):
    df = pd.DataFrame({'s': sec, 'v': ms}).groupby('s').v.agg(['min', 'max']); i = df.index.values; mn[i] = np.minimum(mn[i], df['min'].values); mx[i] = np.maximum(mx[i], df['max'].values)
def acc_add(acc, k, recv, T, q, day0):
    """Suma al acumulador las filas de UN simbolo k: recv/T/q (arrays). Solo cuentan recepciones dentro del dia (H1/H2) y T dentro del dia (H3, H1b)."""
    if k not in SIMB_FLUJO: return
    ik = SIMB_FLUJO.index(k); recv = np.asarray(recv, np.int64); T = np.asarray(T, np.int64); q = np.asarray(q, float)
    m = (recv >= day0) & (recv < day0 + DAY_MS)
    if m.any(): _minmax(acc['rmin'][ik], acc['rmax'][ik], (recv[m] - day0) // 1000, recv[m]); acc['n'][ik] += int(m.sum())
    mt = (T >= day0) & (T < day0 + DAY_MS)
    if mt.any():
        _minmax(acc['tmin'], acc['tmax'], (T[mt] - day0) // 1000, T[mt])
        if k in SIMB_H3: acc['qsum'][SIMB_H3.index(k)] += np.bincount(((T[mt] - day0) // 60000).astype(int), weights=q[mt], minlength=1440)[:1440]
def acc_from(rec=None, tr=None, day0=0):
    """Acumulador desde arrays ya en memoria (pruebas y compatibilidad): rec {simbolo: recv ms}, tr {simbolo: (T ms, q)}."""
    acc = acc_nuevo(); e = np.array([], np.int64)
    for k, v in (rec or {}).items(): acc_add(acc, k, v, e, np.array([], float), day0)
    for k, (T, q) in (tr or {}).items(): acc_add(acc, k, e, T, q, day0)
    return acc
def _huecos(mn, mx, day0):
    """Intervalos entre ticks consecutivos (ini, fin en ms) con bordes virtuales 00:00 y 24:00; exactos para huecos >= 1 s (dentro de un segundo no se calculan: < 1 s)."""
    s = np.nonzero(mx >= 0)[0]; return np.concatenate([[day0], mx[s]]), np.concatenate([mn[s], [day0 + DAY_MS]])
def salud_h1h2(acc, day0, sanas):
    """H1/H2 sobre el flujo conjunto de SIMB_FLUJO (ms de RECEPCION; ADDENDUM7 B3, C1) a partir del acumulador en streaming (o de un dict {simbolo: recv} que se convierte). sanas: horas sanas (0..23).
    Bordes (C1): 00:00 y 24:00 UTC actuan como ticks virtuales (el primer intervalo empieza en 00:00 y el ultimo en el ultimo tick); un intervalo cuenta si su INICIO cae en hora sana
    (aunque termine en hora mala) y se ignora si empieza en hora mala; H1 valido si todo intervalo contado <= H1_S (> H1_S invalida); ticks con recepcion fuera del dia no entran. Sin horas
    sanas: NO VALIDO. Simbolo de SIMB_FLUJO sin ninguna fila en el dia => h1=h2=False (nunca se mide con menos simbolos en silencio).
    H2: fraccion de segundos de horas sanas con >=1 tick conjunto >= H2_MIN; h2_cobertura_4 (BTC/ETH/SOL/XRP) es sensibilidad (B4). Diagnosticos por moneda y n de intervalos >=30 s sobre los 6."""
    if 'rmin' not in acc: acc = acc_from(rec=acc, day0=day0)
    sanas = sorted(sanas); ausentes = [k for i, k in enumerate(SIMB_FLUJO) if acc['n'][i] == 0]; ns = 3600 * len(sanas)
    pres = acc['rmax'] >= 0; hora = lambda pr: pr.reshape(24, 3600).sum(1)   # segundos con tick por hora
    cov_ = lambda pr: (float(hora(pr)[sanas].sum() / ns) if sanas else 0.0)
    i4 = [SIMB_FLUJO.index(k) for k in SIMB_4]; cov = cov_(pres.any(0)); cov4 = cov_(pres[i4].any(0))
    def gaps(mn, mx):
        ini, fin = _huecos(mn, mx, day0); en = np.isin((ini - day0) // 3600000, sanas); return ini, fin, en
    ini, fin, en = gaps(acc['rmin'].min(0), acc['rmax'].max(0)); gap = fin - ini; gmax = int(gap[en].max()) if en.any() else 0; g30 = en & (gap >= 30000)
    pm = {}   # diagnosticos por moneda (NO decisorios)
    for ik, k in enumerate(SIMB_FLUJO):
        a, b, ek = gaps(acc['rmin'][ik], acc['rmax'][ik]); hr = hora(pres[ik]) / 3600
        pm[k] = dict(cobertura=cov_(pres[ik]), hueco_max_s=float((b - a)[ek].max() / 1000) if ek.any() else 0.0, min_horario=float(hr[sanas].min()) if sanas else 0.0, n=int(acc['n'][ik]))
    h1 = bool(gmax <= H1_S * 1000 and len(sanas) > 0 and not ausentes); h2 = bool(len(sanas) > 0 and cov >= H2_MIN and not ausentes)
    return dict(h1_hueco_max_s=gmax / 1000, h1_var={str(v): bool(gmax <= v * 1000 and not ausentes) for v in H1_VAR}, h1=h1, h2_cobertura=cov, h2=h2, h2_cobertura_4=cov4, simbolos_ausentes=ausentes,
                n_intervalos_ge30s=int(g30.sum()), intervalos_ge30s=[[int(x), int(y)] for x, y in zip(ini[g30], fin[g30])], por_moneda=pm)
def salud_h3(acc, kvol, day0):
    """H3: ratio por simbolo de SIMB_H3 (BTC/ETH/SOL/XRP; BNB/DOGE no entran) = suma de q logueada en x_D (por MINUTO de hora de trade T) / volumen del kline 1m REST del dia completo; valido si el MINIMO de los 4 >= H3_MIN.
    acc: acumulador (o dict {simbolo: (T_ms, q)}); kvol: {simbolo: ndarray de 1440 volumenes}. Diagnosticos: n minutos con ratio<0,5 y kline>10x mediana; H1b (hueco conjunto en T, 6 simbolos)."""
    if 'qsum' not in acc: acc = acc_from(tr=acc, day0=day0)
    rat, diag = {}, {}
    for i, k in enumerate(SIMB_H3):
        kv = np.asarray(kvol[k], float); lm = acc['qsum'][i]; tot = float(kv.sum()); rat[k] = float(lm.sum() / tot) if tot > 0 else float('nan')
        med = float(np.median(kv)); bad = (kv > 10 * med) & (lm < 0.5 * kv) if med > 0 else np.zeros(1440, bool); diag[k] = dict(n_min_ratio_lt05_vol_gt10x=int(bad.sum()), vol_kline=tot, vol_log=float(lm.sum()))
    a, b = _huecos(acc['tmin'], acc['tmax'], day0)
    mn = min(rat.values()) if rat and all(v == v for v in rat.values()) else float('nan')   # cualquier simbolo sin ratio (kline 0) => NaN => no valido
    ok = lambda thr: bool(mn == mn and mn >= thr)
    return dict(h3_ratio=rat, h3_min=mn, h3=ok(H3_MIN), h3_var={str(v): ok(v) for v in H3_VAR}, h3_diag=diag, h1b_hueco_trade_max_s=float((b - a).max() / 1000))
def kl_rest(sym, day0):
    """Klines 1m REST de Binance (publico) del dia completo: 2 llamadas de hasta 1000, UN intento por llamada (los reintentos con espera los hace klines_dia). -> [(openTime, volumen_base)]."""
    import urllib.request
    out = []; t = day0
    for _ in range(2):
        u = f'https://api.binance.com/api/v3/klines?symbol={sym}USDT&interval=1m&startTime={t}&endTime={day0 + DAY_MS - 1}&limit=1000'; ch = json.load(urllib.request.urlopen(u, timeout=20))
        out += [(int(r[0]), float(r[5])) for r in ch]
        if len(ch) < 1000: break
        t = int(ch[-1][0]) + 60000
    return out
def _kl_ok(vol):
    v = np.asarray(vol, float); return v.shape == (1440,) and bool(np.isfinite(v).all()) and float(v.sum()) > 0
def klines_dia(sym, d, kcache=None, fetch=None):
    """Volumen por minuto (1440) del dia d para el simbolo; cache por dia en datalogs (sin repetir llamadas). La cache se valida AL LEER y AL ESCRIBIR (1440 valores, finitos, suma > 0): si no, se descarta y se
    vuelve a descargar. REST con REST_TRIES intentos con espera (ESPERA_REST*k s); fallo, kline incompleto/no contiguo, no finito o volumen 0 => ErrorDatos (ERROR_DATOS, no se cachea)."""
    import time
    kcache = KCACHE if kcache is None else kcache; fetch = kl_rest if fetch is None else fetch; f = f'{kcache}klines_{sym}_{d}.json'; day0 = int(pd.Timestamp(d, tz='UTC').timestamp()) * 1000
    if os.path.exists(f):
        try:
            c = json.load(open(f))
            if c['dia'] == d and c['sym'] == sym and _kl_ok(c['vol']): return np.array(c['vol'], float)
        except Exception: pass   # cache ilegible o invalida: se descarta y se vuelve a pedir
    ex = None
    for k in range(REST_TRIES):
        try: ks = fetch(sym, day0); break
        except Exception as e:
            ex = e
            if k < REST_TRIES - 1: time.sleep(ESPERA_REST * (k + 1))
    else: raise ErrorDatos(f'REST klines {sym} {d}: {type(ex).__name__}: {ex} (tras {REST_TRIES} intentos)')
    if len(ks) != 1440 or any(int(ks[i][0]) != day0 + 60000 * i for i in range(len(ks))): raise ErrorDatos(f'kline {sym} {d} incompleto o no contiguo ({len(ks)} de 1440)')
    vol = [float(x[1]) for x in ks]
    if not _kl_ok(vol): raise ErrorDatos(f'kline {sym} {d}: volumen no finito o total 0')   # ADDENDUM7 C3: ERROR_DATOS global, no se cachea ni se declara dia NO VALIDO
    atomic(f, json.dumps(dict(dia=d, sym=sym, creado=dt.datetime.now(dt.timezone.utc).strftime('%FT%TZ'), vol=vol))); return np.array(vol, float)
def leer_x(xfile, day0):
    """x_D (aggTrade) en STREAMING por chunks -> acumulador (memoria O(86400)). UN solo recorrido para H1, H2, H3, los 4 y los 6 simbolos y los diagnosticos por moneda."""
    acc = acc_nuevo()
    for ch in pd.read_csv(xfile, header=None, usecols=[1, 2, 4, 7], names=['T', 'sym', 'q', 'recv'], dtype={'T': 'int64', 'sym': 'category', 'q': 'float64', 'recv': 'int64'}, chunksize=1000000):
        for sym, g in ch.groupby('sym', observed=True): acc_add(acc, str(sym)[:-4], g.recv.values, g['T'].values, g.q.values, day0)
    return acc
def evaluar_salud(d, xfile, sanas, kcache=None, fetch=None):
    """Salud del feed del dia d (H1, H2, H3 de ADDENDUM6) con diagnosticos y sensibilidad (H1 50/60/73 y H3 0,93/0,95/0,97). Lanza ErrorDatos si falla la consulta REST."""
    day0 = int(pd.Timestamp(d, tz='UTC').timestamp()) * 1000; acc = leer_x(xfile, day0)
    h12 = salud_h1h2(acc, day0, sanas); kv = {k: klines_dia(k, d, kcache, fetch) for k in SIMB_H3}; h3 = salud_h3(acc, kv, day0)
    r = dict(dia=d, criterio=CRITERIO, horas_sanas=len(sanas)); r.update(h12); r.update(h3)
    r['valido'] = bool(r['h1'] and r['h2'] and r['h3']); fal = [n for n, v in (('H1 hueco conjunto <= %ds' % H1_S, r['h1']), ('H2 cobertura conjunta >= %.2f' % H2_MIN, r['h2']), ('H3 ratio volumen >= %.2f' % H3_MIN, r['h3'])) if not v]
    if r['simbolos_ausentes']: fal.append('simbolo del flujo ausente: ' + ','.join(r['simbolos_ausentes']))
    r['motivo'] = '' if r['valido'] else 'Binance NO sano: ' + '; '.join(fal)
    r['fragil_criterio_salud'] = bool(r['valido'] and r['h2_cobertura_4'] < H2_MIN)   # ADDENDUM7 B4: valido con 6 simbolos pero H2(4) < 0,95
    r['sensibilidad'] = {**{f'H1={v}s': bool(r['h1_var'][str(v)] and r['h2'] and r['h3']) for v in H1_VAR}, **{f'H3={v}': bool(r['h1'] and r['h2'] and r['h3_var'][str(v)]) for v in H3_VAR}, 'H2=4simb': bool(r['h1'] and r['h3'] and r['h2_cobertura_4'] >= H2_MIN and not r['simbolos_ausentes'])}
    return r
ASENTAR_MIN, ESTABLE_MIN = 30, 10   # dia asentado: >= 30 min tras la medianoche de d+1 y x_D/bad_D.json ESCRITOS despues de esa hora y sin tocar en los ultimos 10 min
def asentado(d, xpath, bpath, ahora):
    """-> (ok, motivo). Dia d asentado: ahora >= medianoche de d+1 + ASENTAR_MIN min, y x_D y bad_D.json con mtime >= esa hora (producidos DESPUES del cierre del dia: un fichero con mtime anterior pudo copiarse
    incompleto) y <= ahora - ESTABLE_MIN min (no se estan escribiendo). INTERPRETACION ANOTADA: el encargo decia "mtime anterior a esa hora"; en este pipeline x_D/bad_D se extraen a las ~11-12Z de d+1, asi que
    la lectura literal dejaria TODO dia PENDIENTE para siempre; se aplica la lectura "producidos despues del asentamiento y ya estables"."""
    t = pd.Timestamp(d, tz='UTC') + pd.Timedelta(days=1, minutes=ASENTAR_MIN)
    if ahora < t: return False, f'sin asentar: antes de las {t:%FT%TZ} (ahora {ahora:%FT%TZ})'
    for pth in (xpath, bpath):
        mt = os.path.getmtime(pth)
        if mt < t.timestamp(): return False, f'sin asentar: {os.path.basename(pth)} producido antes de {t:%FT%TZ} (pudo copiarse incompleto)'
        if mt > (ahora - pd.Timedelta(minutes=ESTABLE_MIN)).timestamp(): return False, f'sin asentar: {os.path.basename(pth)} modificado hace menos de {ESTABLE_MIN} min'
    return True, ''
def dia_valido(d, hoy=None, vdir=None, kcache=None, fetch=None, ahora=None):
    """Dia que cuenta (ADDENDUM6 2 + ADDENDUM7): insumos completos, horas sanas (bad_D.json) y Binance sano H1+H2+H3. Estados:
    - EN CURSO (C2: d >= fecha UTC de la ejecucion): en_curso=True, ni valido ni NO VALIDO, sin cache y sin llamada REST.
    - PENDIENTE (C5: d < hoy con insumos incompletos, o dia SIN ASENTAR [< 30 min tras la medianoche de d+1 o x_D/bad_D.json modificados despues]): pendiente=True, valido=False, sin cache ni REST.
    - NO VALIDO por H1/H2/H3 (dia cerrado y asentado): se cachea en validez_D.json y es DEFINITIVO (no se recalcula por reintento; solo por correccion de bug anotada en DECISION_LOG).
    - REST fallido (3 intentos con espera) / kline != 1440 min contiguos / no finito / volumen 0 (C3): dict error=True (ERROR_DATOS GLOBAL del evaluador), sin cache de validez.
    Cache validez_D.json con clave `criterio`: una cache sin ella o con otra (p.ej. ADDENDUM6) se RECHAZA y se recalcula. `ahora` (Timestamp UTC): por defecto el reloj real; si se simula `hoy`, la 01:00Z de ese dia.
    (El rasgo de PC_AS >=95 % se comprueba en evaluar, solo para PC_AS.)"""
    vdir = HERE + 'thru1_fwd/' if vdir is None else vdir; ahora = pd.Timestamp.now(tz='UTC') if (ahora is None and hoy is None) else (ahora if ahora is not None else pd.Timestamp(hoy, tz='UTC') + pd.Timedelta(hours=1))
    hoy = hoy or Q.hoy_utc(); cache = vdir + f'validez_{d}.json'
    if d >= hoy: return dict(dia=d, valido=False, en_curso=True, motivo='EN CURSO (el dia no esta completo: sin cache, sin REST)')
    if os.path.exists(cache):
        try:
            c = json.load(open(cache))
            if c.get('criterio') == CRITERIO: return c
        except Exception: pass
    sys.path.insert(0, HERE + 'barrido_multi'); import bfeat
    falta = [n for n, ok in (('tape', os.path.exists(PB + f'tape_{d}.pkl')), ('bad', os.path.exists(PB + f'bad_{d}.json')), ('x_binance', bool(bfeat.xfile(d))),
                             ('RT_passT', os.path.exists(f'{TX}RT_{d}.pkl')), ('RT_rt_sim', os.path.exists(f'{RTD}RT_{d}.pkl'))) if not ok]
    if falta: return dict(dia=d, valido=False, pendiente=True, motivo='PENDIENTE: faltan ' + ','.join(falta))   # sin cache: puede completarse mas tarde
    okas, why = asentado(d, bfeat.xfile(d), PB + f'bad_{d}.json', ahora)
    if not okas: return dict(dia=d, valido=False, pendiente=True, motivo='PENDIENTE: dia ' + why)
    bad = {int(h) for dd, h in json.load(open(PB + f'bad_{d}.json'))['bad'] if dd == d}; sanas = [h for h in range(24) if h not in bad]
    if not sanas: r = dict(dia=d, criterio=CRITERIO, valido=False, motivo='0 horas sanas')
    else:
        try: r = evaluar_salud(d, bfeat.xfile(d), sanas, kcache, fetch)
        except ErrorDatos as e: return dict(dia=d, valido=False, error=True, motivo=f'ERROR_DATOS: {e}')
    atomic(cache, json.dumps(r, indent=1)); return r
# ---------------- checkpoint de un brazo ----------------
def checkpoint(arm, A, days, cp, U, plc):
    """Evalua C1-C10 sobre los primeros `cp` dias que cuentan. A: dict de brazos; days: lista cronologica (ya cortada)."""
    if arm == 'PG_O50': a, b = A['rt_PG_O50_BASE'], A['rt_G0_BASE']
    else: a, b = A[arm], (A['G0'])
    a, b = a[a.dia.isin(days)], b[b.dia.isin(days)]
    st = stats_dpnl(a, b, days); eva = ev_stats(a); nd = len(days); c = {}
    c['C1 nd>=10, >=300 rellenos BASE, >=40 cierres con dPnL!=0'] = nd >= 10 and len(a) >= 300 and st['nnz'] >= 40
    c['C2 dPnL BASE>0, IC90 cierre inf>0 e IC90 dia inf>0'] = Q.gt(st['tot']) and Q.gt(st['ic_c'][0]) and Q.gt(st['ic_d'][0])
    ak, bk = A[f'rt_{arm}_CROSS'], A['rt_G0_CROSS']; cross = float(dser(ak[ak.dia.isin(days)], bk[bk.dia.isin(days)]).sum())   # CXJ150: de rt_cxj150_cross.py (dias sin RX_D no cuentan para CXJ150)
    c['C3 dPnL CROSS>0 (si no: NO IDENTIFICADO POR EL RELLENO)'] = Q.gt(cross)
    c['C4 dPnL sin 2 mejores dias>0 y sin 5 mejores cierres>0'] = Q.gt(st['sin2dias']) and Q.gt(st['sin5cierres'])
    c['C5 EV abs BASE>0, IC90 cierre inf>0, sin 2 mejores dias>0, sin 5 mejores cierres>0'] = Q.gt(eva['ev']) and Q.gt(eva['ic_inf']) and Q.gt(eva['sin2dias']) and Q.gt(eva['sin5'])
    dd = pd.Series(st['dias']); k = int((dd > 1e-12).sum()); c[f'C6 dPnL_d>0 en >=60 % de dias ({k}/{nd})'] = nd >= 1 and 5 * k >= 3 * nd
    ys = stats_dpnl(a[a.lado == 'YES'], b[b.lado == 'YES'], days)['tot']
    gno = b[b.lado == 'NO'].groupby('dia').pnl.sum().reindex(days).fillna(0.0); dno = pd.Series(stats_dpnl(a[a.lado == 'NO'], b[b.lado == 'NO'], days)['dias'])
    cnt = int(((gno >= 0) & (dno.reindex(days).fillna(0.0) > 0)).sum())
    c['C7 dPnL_YES>0, o >=3 dias con G0-NO>=0 y dPnL_NO>0 (si no: NO SEPARABLE DEL REGIMEN)'] = Q.gt(ys) or cnt >= 3
    placebo = None
    if arm == 'PC_AS':
        pno = b[b.lado == 'NO'].groupby(['fin', 'act']).pnl.sum().to_dict(); o, m, p = placebo_pcas(U, pno, set(days)); placebo = dict(d_obs=o, m=m, p=p)
        c['C8 placebo p<=0,10 y d_obs>m'] = p == p and p <= 0.10 and o > m
    elif arm == 'CXJ150':
        placebo = plc if plc and sorted(plc.get('dias', [])) == sorted(days) else None
        c['C8 placebo p<=0,10 y d_obs>m'] = bool(placebo and placebo['p'] <= 0.10 and placebo['d_obs'] > placebo['m'])
    shrink = None; pgg = None
    if arm == 'PG_O50':
        g6 = A['rt_GEO6_BASE']; sp = stats_dpnl(a, g6[g6.dia.isin(days)], days); pgg = sp['tot']
        ok9 = Q.gt(sp['tot']) and Q.gt(sp['ic_c'][0])
        if cp == 10 and nd >= 10:
            m1, m2 = dd.iloc[:5].mean(), dd.iloc[5:10].mean(); shrink = (float(m1), float(m2)); ok9 = ok9 and not (m2 < 0.5 * m1)
        c['C9 PG_O50-GEO6>0 con IC90 cierre inf>0; sin encogerse (cp10)'] = ok9
    cand = all(c.values())
    return dict(cp=cp, dias=list(days), nd=nd, candidato=bool(cand), conds={k_: bool(v) for k_, v in c.items()}, dpnl=st, ev=eva, n_arm=len(a), cross=cross, placebo=placebo, pg_menos_geo6=pgg, shrink=shrink,
                label=('CANDIDATO (EXPLORATORY hasta medicion L2)' if cand else 'NO CANDIDATO'))
def promocion(arm, res, tok):
    st, ev_, pl = res['dpnl'], res['ev'], res.get('placebo'); f = Q.f3
    a1 = Q.gt(st['ic_c'][2]); a2 = Q.gt(st['ic_d'][2]); a3 = Q.gt(ev_['ic_inf_p'])
    if arm in ('CXJ150', 'PC_AS'): a4 = bool(pl) and pl['p'] == pl['p'] and pl['p'] <= 0.025 and pl['d_obs'] > pl['m']; ptxt = f'{pl["p"]:.4f}' if pl else 'nan'
    else: a4 = True; ptxt = 'no aplica'
    ok = tok == 'CANDIDATO' and res['candidato'] and a1 and a2 and a3 and a4
    return (f'PROMOCION (alfa/4): {"SI" if ok else "NO"} | brazo={arm} | seguimiento={tok} | dPnL BASE IC cierre inf 1,25%={f(st["ic_c"][2])} req >0: {Q.si(a1)} | dPnL BASE IC dia inf 1,25%={f(st["ic_d"][2])} req >0: {Q.si(a2)}'
            f' | EV abs IC cierre inf 1,25%={f(ev_["ic_inf_p"])} req >0: {Q.si(a3)} | placebo p={ptxt} req <=0,025: {"no aplica" if ptxt == "no aplica" else Q.si(a4)}')
# ---------------- REFUTA thru1 (ADDENDUM4 sec. 3) ----------------
def refuta_fuerte(res):
    """REFUTA fuerte (ADDENDUM4 sec. 3), TODAS: dPnL BASE < 0 definido con >=3 cierres; limite SUPERIOR del IC90 por cierre < 0 y por dia < 0; >=300 rellenos BASE del brazo en esos dias."""
    st = res['dpnl']; c = {'dPnL BASE<0': Q.lt(st['tot']), '>=3 cierres': st['ncierres'] >= 3, 'IC90 cierre sup<0': Q.lt(st['ic_c'][1]), 'IC90 dia sup<0': Q.lt(st['ic_d'][1]), '>=300 rellenos BASE': res['n_arm'] >= 300}
    return all(c.values()), ', '.join(f'{k}={Q.si(v)}' for k, v in c.items()) + f' (dPnL {Q.f3(st["tot"])}, IC90c sup {Q.f3(st["ic_c"][1])}, IC90d sup {Q.f3(st["ic_d"][1])}, n={res["n_arm"]})'
def motivo_refuted(res):
    """Motivo anotado del REFUTED del checkpoint 20 (no es regla de decision): C3 -> 'no identificado por el relleno', C7 -> 'no separable del regimen', resto = condiciones fallidas."""
    fallan = [k for k, v in res['conds'].items() if not v]; m = []
    if any(k.startswith('C3') for k in fallan): m.append('no identificado por el relleno')
    if any(k.startswith('C7') for k in fallan): m.append('no separable del regimen')
    return '; '.join(m + ['condiciones no cumplidas: ' + ','.join(k.split(' ')[0] for k in fallan)])
# ---------------- evaluacion ----------------
def aceptacion(salida):
    T = pd.concat([pd.read_pickle(f'{TX}RT_{d}.pkl') for d in QUEMADOS], ignore_index=True)
    g0 = T[T['var'] == 'G0']; th = g0[g0.ftype == 'thru1']
    r = dict(g0_n=len(g0), g0_pnl=float(g0.pnl.sum()), g0_ev=float(Q.ev(g0)), thru1_n=len(th), thru1_ev=float(Q.ev(th)),
             d_geo6=float(dser(T[T['var'] == 'GEO6'], g0).sum()), d_cxj150=float(dser(T[T['var'] == 'CXJ150'], g0).sum()))
    ok = {'G0 n=2938': r['g0_n'] == 2938, 'G0 pnl -166,9+-1': abs(r['g0_pnl'] + 166.9) <= 1, 'G0 EV -0,076': abs(r['g0_ev'] + 0.076) <= 0.0006, 'thru1 n=2321': r['thru1_n'] == 2321,
          'thru1 EV -0,125': abs(r['thru1_ev'] + 0.125) <= 0.0006, 'dPnL GEO6 +140+-1': abs(r['d_geo6'] - 140) <= 1, 'dPnL CXJ150 +128+-1': abs(r['d_cxj150'] - 128) <= 1}
    out = dict(pass_=all(ok.values()), checks=ok, valores=r, eval_sha=eval_sha(), fecha=Q.hoy_utc(), dias=QUEMADOS)
    atomic(salida + '/aceptacion.json', json.dumps(out, indent=1, default=float)); return out
def evaluar(a):
    sal = a.salida; os.makedirs(sal, exist_ok=True); hoy = a.hoy or Q.hoy_utc(); L = [f'# INFORME DIARIO H-Q11-THRU1 forward (DESCRIPTIVO; ningun veredicto fuera de checkpoints) generado {dt.datetime.now(dt.timezone.utc):%FT%TZ} | hoy={hoy}']
    spath = sal + '/estado_thru1.json'
    def terminales(err=()):
        """ADDENDUM4 A/5b: ante sha distinto, ERROR_DATOS o aceptacion pendiente, un terminal ya emitido se muestra igualmente (con ' [EN REVISION]' si el error afecta a dias <= su fecha). NO escribe estado."""
        ST0 = json.load(open(spath)) if os.path.exists(spath) else {'arms': {}}
        for arm_, s_ in ST0['arms'].items():
            if s_.get('terminal'): tok_, why_, _ = Q.veredicto({'terminal': s_['terminal']}, list(err), 0, 0, False, False, hoy); L.append(f'VEREDICTO {arm_}: {tok_} ({why_})')
    def fin_(msg):
        L.append(msg); atomic(f'{sal}/informe_thru1_{hoy}.txt', '\n'.join(L) + '\n'); print('\n'.join(L)); sys.exit(0)
    rt_tx = {os.path.basename(f)[3:13] for f in glob.glob(TX + 'RT_2026-*.pkl')}; rt_rd = {os.path.basename(f)[3:13] for f in glob.glob(RTD + 'RT_2026-*.pkl')}
    cand0 = sorted(rt_tx | rt_rd)   # ADDENDUM7 C5: un dia con solo uno de los RT es candidato incompleto => PENDIENTE (no se descarta en silencio)
    cand_all = [d for d in cand0 if a.desde <= d <= Q.TOPE]; vz = {}   # ADDENDUM4: un dia posterior al tope nunca entra
    en_curso = [d for d in cand_all if d >= hoy]; cand = [d for d in cand_all if d < hoy]   # ADDENDUM7 C2: el dia EN CURSO no es valido ni NO VALIDO, sin cache/REST, fuera de nd_validos y de nd_ficheros
    nd_fich = len([d for d in cand if d in rt_tx and d in rt_rd])   # ADDENDUM5 sec. 2: nd_ficheros = dias candidatos con RT_D en toxicidad_thru1 y redteam, SOLO por nombre
    ST = json.load(open(spath)) if os.path.exists(spath) else {'arms': {}}
    if a.reevaluar_b2:   # ADDENDUM5 sec. 3 (sin automatismo): reabre solo los terminales B2 (con `causa`) por brazo; la reevaluacion no puede emitir CANDIDATO/PROMOCION
        for arm_, s_ in ST['arms'].items():
            t_ = s_.get('terminal')
            if t_ and t_.get('causa'): s_['reabierto'] = list(s_.get('reabierto', [])) + [dict(terminal=t_, ref=a.reevaluar_b2, fecha=hoy)]; s_['terminal'] = None; s_['racha'] = 0; s_['last_nd'] = max([int(k_) for k_ in s_.get('cp', {})] or [0]); L.append(f'B2 reabierto ({arm_}) con ref: {a.reevaluar_b2} (cp ya emitidos se conservan: ADDENDUM7 A5; last_nd coherente con ellos)')
        if any(s_.get('reabierto') for s_ in ST['arms'].values()): atomic(spath, json.dumps(ST, indent=1, default=float))   # la reapertura se persiste YA (tambien si luego hay salida temprana)
    def terminales(err=()):
        """ADDENDUM4 A/5b: ante sha distinto, ERROR_DATOS o aceptacion pendiente, un terminal ya emitido se muestra igualmente (con ' [EN REVISION]' si el error afecta a dias <= su fecha o si el B2 lo trae). NO escribe estado."""
        for arm_, s_ in ST['arms'].items():
            if s_.get('terminal'): tok_, why_, _ = Q.veredicto({'terminal': s_['terminal']}, list(err), 0, 0, False, False, hoy); L.append(f'VEREDICTO {arm_}: {tok_} ({why_})')
    def salida_temprana(msg, causa, err=(), arms=None):
        """ADDENDUM5 sec. 2: funcion UNICA de salida temprana (sha, aceptacion, 0 dias, ERROR_DATOS de insumos/Chainlink, 0 tras PC_AS). Fecha < 2027-01-01: fila B (INSUFFICIENT, parada, SIN escribir estado).
        Fecha >= 2027-01-01: fila B2 = CERRADO_INSUFFICIENT administrativo por cada brazo de `arms` (None = todos) SIN terminal, con nd = last_nd del brazo, causa, motivo, nd_ficheros, en_revision=true; escribe el estado."""
        terminales(err)
        if hoy >= Q.EJEC_CIERRE:
            for arm_ in (arms or ARMS):
                s_ = ST['arms'].setdefault(arm_, {'terminal': None, 'cp': {}})
                if s_.get('terminal'): continue
                s_['terminal'] = dict(veredicto='CERRADO_INSUFFICIENT', fecha=hoy, nd=s_.get('last_nd', 0), cp=None, causa=causa, motivo=msg[:300], nd_ficheros=nd_fich, en_revision=Q.en_revision(causa, nd_fich, err, thru1=True))
                L.append(f'VEREDICTO {arm_}: CERRADO_INSUFFICIENT [EN REVISION] (B2 ADDENDUM5: ejecucion {hoy}>={Q.EJEC_CIERRE}, causa={causa}; cierre ADMINISTRATIVO nd=last_nd={s_["terminal"]["nd"]}, nd_ficheros={nd_fich}: no es evidencia)')
            atomic(spath, json.dumps(ST, indent=1, default=float)); fin_(f'B2: {msg}')
        fin_(msg + ' (fila B: no se escribe estado)')
    bad = check_shas()
    if bad: salida_temprana('INSUFFICIENT (ERROR_DATOS: sha distinto del registrado => parada hasta corregir): ' + '; '.join(bad), 'SHA_DISTINTO', bad)
    if not a.ensayo:
        ac = json.load(open(sal + '/aceptacion.json')) if os.path.exists(sal + '/aceptacion.json') else None
        if not ac or not ac['pass_'] or ac['eval_sha'] != eval_sha(): salida_temprana('INSUFFICIENT: aceptacion sobre quemados no pasada/obsoleta (correr --aceptacion); los dias se acumulan sin evaluarse', 'ACEPTACION')
    desc = [d for d in cand0 if DESCRIPTIVOS_DESDE <= d < a.desde]
    if desc: L.append(f'Dias DESCRIPTIVOS-QUEMADOS (ADDENDUM6: no cuentan, no deciden): {", ".join(desc)}')
    if en_curso: L.append(f'Dia EN CURSO (ADDENDUM7 C2: ni valido ni NO VALIDO, no cuenta): {", ".join(en_curso)}')
    for d in cand: vz[d] = {'valido': True, 'motivo': 'ensayo'} if a.ensayo else dia_valido(d, hoy, ahora=(None if a.hoy else pd.Timestamp.now(tz='UTC')))   # ejecucion real: reloj real; --hoy simulado: 01:00Z de ese dia
    errs = [f'{d}: {vz[d]["motivo"]}' for d in cand if vz[d].get('error')]   # ADDENDUM6 2b: REST fallido/kline incompleto => ERROR_DATOS (INSUFFICIENT), nunca dia valido
    if errs: salida_temprana('INSUFFICIENT (ERROR_DATOS salud Binance H3: ' + '; '.join(errs[:3]) + ')', 'ERROR_DATOS', errs)
    dias = [d for d in cand if vz[d]['valido']]; L.append(f'Dias candidatos {len(cand)} | validos {len(dias)}: ' + ', '.join(f'{d}{"" if vz[d]["valido"] else (" " + vz[d]["motivo"] if vz[d].get("pendiente") else " NO VALIDO(" + vz[d]["motivo"] + ")")}' for d in cand))
    pend = [d for d in cand if vz[d].get('pendiente')]; bloquea = bool(any(d < max(cand) for d in pend) if cand else False) and hoy < Q.EJEC_CIERRE   # ADDENDUM7 C5: un PENDIENTE anterior al ultimo candidato impide congelar checkpoints
    if pend: L.append(f'PENDIENTES (ADDENDUM7 C5, no se cachean): {pend}' + (f' | BLOQUEAN checkpoints/terminales por checkpoint hasta completarse (orden cronologico)' if bloquea else '') + ''.join(f' | ESCALAR A LA SESION PRINCIPAL: {d} lleva {(pd.Timestamp(hoy) - pd.Timestamp(d)).days} dias pendiente (>7)' for d in pend if (pd.Timestamp(hoy) - pd.Timestamp(d)).days > 7))
    if pend and hoy >= Q.EJEC_CIERRE: L.append(f'PENDIENTES a >= 2027-01-01 ({pend}): tratados como NO VALIDOS/PERDIDOS, no cuentan y NO bloquean; cada brazo cierra por las reglas normales (F/G con su nd). Requiere entrada DECISION_LOG manual, redactada sin mirar signos (ADDENDUM7 C5)')
    for d in cand:   # diagnostico NO decisorio y sensibilidad (ADDENDUM6 2, 3.4)
        v = vz[d]
        if v.get('fragil_criterio_salud'): L.append(f'  [salud {d}] FRAGIL AL CRITERIO DE SALUD (H2 con 4 simbolos {v["h2_cobertura_4"]:.4f} < 0,95): un contraste que cambie de signo o de CANDIDATO por incluirlo/excluirlo = no confirmado (ADDENDUM7 B4)')
        if 'h1_hueco_max_s' in v: L.append(f'  [salud {d}] H1 hueco conjunto max {v["h1_hueco_max_s"]:.1f}s ({"ok" if v["h1"] else "NO"}) | H2 cob conjunta {v["h2_cobertura"]:.4f} ({"ok" if v["h2"] else "NO"}) | H3 min ratio {v["h3_min"]:.4f} ({"ok" if v["h3"] else "NO"}) | n intervalos>=30s {v["n_intervalos_ge30s"]} | sensibilidad {v["sensibilidad"]} | por moneda ' + ' '.join(f'{k}:cob{m["cobertura"]:.2f},hueco{m["hueco_max_s"]:.0f}s,minh{m["min_horario"]:.2f}' for k, m in v['por_moneda'].items()))
    if not dias: salida_temprana('INSUFFICIENT: 0 dias validos', 'SIN_DIAS_VALIDOS')
    T, R, S, X, err = cargar(dias)
    if err: salida_temprana('INSUFFICIENT (ERROR_DATOS: ' + '; '.join(err[:3]) + '; no cuenta ningun dia nuevo)', 'ERROR_DATOS', err)
    A, U, cov, cl_err = armar_base(T, R, S, X, dias, hoy, a.cl_cache)
    # ADDENDUM7 A: la condicion de rasgo PC_AS NO recorta `dias` (dia comun de todos los brazos): define arm_dias de PC_AS. Cobertura = (r1 Y r4 finitos) sobre las unidades (cierre, moneda) NO del dia; sin unidades = no cumple.
    covd = U.assign(ok_=U.r1.notna() & U.r4.notna()).groupby('dia').ok_.mean().to_dict() if len(U) else {}
    dias_pcas = [] if cl_err else [d for d in dias if covd.get(d, 0.0) >= 0.95]   # con ERROR_DATOS de Chainlink el rasgo es NaN por falta de datos: no se declaran no validos los dias (ruta A5)
    if not cl_err and len(dias_pcas) < len(dias): L.append(f'PC_AS: dias no validos por rasgo (cobertura r1&r4 < 0,95; solo afecta a PC_AS): {[d for d in dias if d not in dias_pcas]}')
    _upc = U[U.dia.isin(dias_pcas)]; _gpc = A['G0'][A['G0'].dia.isin(dias_pcas)]   # ADDENDUM7 A3/A4: el descriptivo de PC_AS solo usa arm_dias(PC_AS), no los dias G0 excluidos por rasgo
    L.append(f'Cobertura rasgo PC_AS (unidades cierre-moneda NO, SOLO en arm_dias(PC_AS)={len(dias_pcas)} dias): ' + (f'{float((_upc.r1.notna() & _upc.r4.notna()).mean()):.3f} | G0 rellenos {len(_gpc)} pnl {_gpc.pnl.sum():+.2f} EV {Q.f3(Q.ev(_gpc))}' if len(dias_pcas) else 'n/d (ningun dia con rasgo >= 95 %)') + f' | G0 todos los dias comunes: {len(A["G0"])} rellenos, EV {Q.f3(Q.ev(A["G0"]))}')
    if cl_err: L.append('ERROR_DATOS (Chainlink; solo afecta al brazo PC_AS): ' + '; '.join(cl_err[:3]))
    for arm in ARMS:
        if arm == 'PC_AS' and (cl_err or not dias_pcas):   # ADDENDUM7 A5, ruta unica: ERROR_DATOS de Chainlink o arm_dias vacio => fila B (INSUFFICIENT sin estado) / B2 (>= 2027-01-01) SOLO para PC_AS; los demas brazos siguen
            t_ = (ST['arms'].get('PC_AS') or {}).get('terminal'); causa_ = 'ERROR_DATOS' if cl_err else 'SIN_DIAS_VALIDOS'; mot_ = '; '.join(cl_err[:3])[:300] if cl_err else 'rasgo PC_AS < 95 %'
            tok_, why_, _ = Q.veredicto({'terminal': t_}, cl_err, 0, 0, False, False, hoy) if t_ else ('INSUFFICIENT', (('ERROR_DATOS: ' + '; '.join(cl_err[:3])) if cl_err else 'ningun dia con rasgo PC_AS >= 95 % (r1&r4)') + ' (no cuenta ningun dia nuevo; sin estado)', None)
            L.append(f'\n## PC_AS: {"ERROR_DATOS Chainlink" if cl_err else "0 dias con rasgo >= 95 %"}\nVEREDICTO PC_AS: {tok_} ({why_})')
            if hoy >= Q.EJEC_CIERRE and not t_:   # B2 solo para PC_AS (ADDENDUM5 sec. 2 / ADDENDUM7 A5)
                s_ = ST['arms'].setdefault('PC_AS', {'terminal': None, 'cp': {}}); s_['terminal'] = dict(veredicto='CERRADO_INSUFFICIENT', fecha=hoy, nd=s_.get('last_nd', 0), cp=None, causa=causa_, motivo=mot_, nd_ficheros=nd_fich, en_revision=Q.en_revision(causa_, nd_fich, cl_err))
                L.append(f'VEREDICTO PC_AS: CERRADO_INSUFFICIENT{" [EN REVISION]" if s_["terminal"]["en_revision"] else ""} (B2 ADDENDUM5: ejecucion {hoy}>={Q.EJEC_CIERRE}, causa={causa_}; cierre ADMINISTRATIVO nd=last_nd={s_["terminal"]["nd"]}: no es evidencia)')
            continue
        s = ST['arms'].setdefault(arm, {'terminal': None, 'cp': {}})
        if arm == 'PG_O50':   # dia valido para PG_O50 solo si hay Po_D Y filas PG_O50 de rt_sim (si rt_sim corrio antes que Po_D, el brazo faltaria y dPnL = -G0: falso)
            arm_dias = [d for d in dias if os.path.exists(BCO + f'Po_{d}.pkl') and (A['rt_PG_O50_BASE'].dia == d).any()]
            if len(arm_dias) < len(dias): L.append(f'PG_O50: dias sin Po_D o sin filas del brazo (no cuentan para PG_O50): {[d for d in dias if d not in arm_dias]}')
        elif arm == 'CXJ150':   # C3 exige rt_cxj150_cross.py: dia sin RX_D no cuenta para este brazo (no hay cota CROSS)
            arm_dias = [d for d in dias if os.path.exists(f'{RXD}RX_{d}.pkl')]
            if len(arm_dias) < len(dias): L.append(f'CXJ150: dias sin RX_D (rt_cxj150_cross.py; no cuentan para CXJ150): {[d for d in dias if d not in arm_dias]}')
        elif arm == 'PC_AS': arm_dias = list(dias_pcas)   # ADDENDUM7 A1: PC_AS = dias comunes con cobertura de rasgo >= 95 % (r1&r4) y sin ERROR_DATOS de Chainlink
        else: arm_dias = list(dias)
        ab, gb = (A['rt_PG_O50_BASE'], A['rt_G0_BASE']) if arm == 'PG_O50' else (A[arm], A['G0'])
        con = sorted(d for d in arm_dias if (ab.dia == d).any() or (gb.dia == d).any()); nd = len(con)   # cuenta: relleno BASE del brazo o de G0
        s['last_nd'] = nd   # ADDENDUM5 sec. 5.4: last_nd por brazo en cada evaluacion valida (lo usa B2)
        L.append(f'\n## {arm}: dias que cuentan nd_validos={nd} (validos {len(arm_dias)}); G0 {len(gb[gb.dia.isin(con)])} rellenos, brazo {len(ab[ab.dia.isin(con)])}')
        if not s['terminal'] and bloquea: L.append('  checkpoints NO evaluados: dia PENDIENTE anterior al ultimo candidato (ADDENDUM7 C5); ejecucion descriptiva')
        if not s['terminal'] and not bloquea:
            for cp in (10, 20):
                if nd >= cp and str(cp) not in s['cp']:
                    plc = None
                    if arm == 'CXJ150':   # el placebo se calcula EN el checkpoint (prereg): sin el no se congela ni se evalua
                        pf = f'{sal}/placebo_cxj150_cp{cp}.json'; plc = json.load(open(pf)) if os.path.exists(pf) else None
                        if not plc or sorted(plc.get('dias', [])) != con[:cp]:
                            L.append(f'  PENDIENTE checkpoint {cp} de CXJ150: falta placebo (99 semillas) para los dias {",".join(con[:cp])}. Ejecutar: nice -n 19 ionice -c3 python3 -I placebo_cxj150.py cp {cp} {",".join(con[:cp])}'); break
                    res = checkpoint(arm, A, con[:cp], cp, U, plc)
                    if s.get('reabierto') and res['candidato']: res['label'] = 'CANDIDATO NO EMITIBLE (reevaluacion B2)'   # ADDENDUM7 C4: sin efecto en cp10; en cp20 cierra CERRADO_INSUFFICIENT
                    s['cp'][str(cp)] = res; r5 = res['dpnl']; fuerte, fdet = refuta_fuerte(res)
                    if cp == 10 and arm != 'PG_O50' and fuerte: s['terminal'] = dict(veredicto='REFUTA', fecha=hoy, nd=nd, cp=cp, motivo=fdet)   # fila C (PG_O50 no se declara fallido antes del checkpoint 20)
                    elif cp == 20:
                        if res['candidato'] and s.get('reabierto'): s['terminal'] = dict(veredicto='CERRADO_INSUFFICIENT', fecha=hoy, nd=nd, cp=cp, motivo='reevaluacion tras B2 (ADDENDUM5 sec. 3): CANDIDATO/PROMOCION no emitibles')
                        elif res['candidato']: s['terminal'] = dict(veredicto='CANDIDATO', fecha=hoy, nd=nd, cp=cp)   # fila D
                        elif not (r5['tot'] == r5['tot']) or r5['ncierres'] < 3: s['terminal'] = dict(veredicto='CERRADO_INSUFFICIENT', fecha=hoy, nd=nd, cp=cp, motivo='dPnL BASE NaN o <3 cierres en el checkpoint 20')   # fila E
                        else: s['terminal'] = dict(veredicto='REFUTED', fecha=hoy, nd=nd, cp=cp, motivo=('REFUTA fuerte: ' + fdet) if fuerte else motivo_refuted(res))   # fila F
                    if s['terminal']: break
            if not s['terminal'] and hoy >= Q.EJEC_CIERRE and nd < 20: s['terminal'] = dict(veredicto='CERRADO_INSUFFICIENT', fecha=hoy, nd=nd, cp=None, motivo='fila G: ejecucion >= 2027-01-01 con nd<20')   # ADDENDUM4 fila G
        tok = s['terminal']['veredicto'] if s['terminal'] else ('INSUFFICIENT' if nd <= 2 else ('EN_CURSO (checkpoint 10 evaluado)' if s['cp'] else 'EN_CURSO' if nd < 10 else 'EN_CURSO (checkpoint pendiente)'))
        L.append(f'VEREDICTO {arm}: {tok}' + (f' (terminal desde {s["terminal"]["fecha"]}, cp={s["terminal"]["cp"]}{"; causa=" + s["terminal"]["causa"] if s["terminal"].get("causa") else ""}{"; " + s["terminal"]["motivo"] if s["terminal"].get("motivo") else ""}{" [EN REVISION]" if s["terminal"].get("en_revision") else ""})' if s['terminal'] else f' (nd={nd}; checkpoints evaluados: {sorted(s["cp"])})'))
        for k_, res in sorted(s['cp'].items()):
            L.append(f'  [checkpoint {k_}] {res["label"]} | dPnL BASE {res["dpnl"]["tot"]:+.2f} EUR IC90c ({Q.f3(res["dpnl"]["ic_c"][0])},{Q.f3(res["dpnl"]["ic_c"][1])}) IC90d inf {Q.f3(res["dpnl"]["ic_d"][0])} | CROSS {Q.f3(res["cross"])} | EV abs {Q.f3(res["ev"]["ev"])} n={res["n_arm"]}')
            L += [f'     - [{"x" if v else " "}] {c_}' for c_, v in res['conds'].items()]
            if k_ == '20' and not s.get('reabierto'): L.append('  ' + promocion(arm, res, tok))
        # descriptivo diario (no decide)
        d_ = stats_dpnl(ab[ab.dia.isin(con)], gb[gb.dia.isin(con)], con) if nd else None
        if d_: L.append(f'  [descriptivo acumulado] dPnL BASE {d_["tot"]:+.2f} cierres {d_["ncierres"]} IC90c ({Q.f3(d_["ic_c"][0])},{Q.f3(d_["ic_c"][1])}) sin2dias {Q.f3(d_["sin2dias"])} | por dia: ' + ' '.join(f'{k}:{v:+.1f}' for k, v in d_['dias'].items()))
        if nd:
            L.append('  [cotas dPnL] ' + ' '.join(f'{f}={float(dser(A[f"rt_{arm}_{f}"][A[f"rt_{arm}_{f}"].dia.isin(con)], A[f"rt_G0_{f}"][A[f"rt_G0_{f}"].dia.isin(con)]).sum()):+.1f}' for f in (('BASE', 'CROSS') if arm == 'CXJ150' else FV)))
    sec = []
    for v in ('NJ3A', 'CXJ1000', 'GEO6NJ3', 'CXB150', 'CXB300', 'CXB1000', 'CXB3000'): sec.append(f'{v}={float(dser(A[v], A["G0"]).sum()):+.1f}')
    pg, g6 = A['rt_PG_O50_BASE'], A['rt_GEO6_BASE']; sec.append(f'PG_O50-GEO6={float(dser(pg, g6).sum()):+.1f}' if len(pg) else 'PG_O50-GEO6=n/d')
    L.append('\n[secundarios descriptivos dPnL BASE vs G0: DIAS COMUNES (todos los validos), NO son arm_dias(PC_AS) ni de ningun brazo; los descriptivos por brazo van arriba con sus propios dias; no deciden] ' + ' '.join(sec) + ' | GEO6+CXJ150: no disponible (requiere simulacion nueva)')
    L.append('NOTA: CXJ150 bajo BASE/CROSS = redteam/rt_cxj150_cross.py (script nuevo, sha propio, rt_sim.py/passT.py sin tocar); dia sin RX_D no cuenta para CXJ150.')
    atomic(spath, json.dumps(ST, indent=1, default=float)); fin_('FIN')
# ---------------- produccion por dia ----------------
def puntuar(d):
    """Po_D (p_OWN del modelo congelado) + entrada C2o_thr.json[d] con el umbral FIJO del modelo. Reutiliza c1own de entrenar_own.py por extraccion AST (sin copiar logica)."""
    import pickle; bad = check_shas()
    if bad: raise SystemExit('ERROR_DATOS sha: ' + '; '.join(bad))
    src = open(HERE + 'forward_pg/entrenar_own.py').read(); tree = ast.parse(src); idx = next(i for i, n in enumerate(tree.body) if isinstance(n, ast.FunctionDef) and n.name == 'c1own')
    ns = {'__file__': HERE + 'forward_pg/entrenar_own.py', '__name__': 'entrenar_own_import'}; exec(compile(ast.Module(tree.body[:idx + 1], []), 'entrenar_own_AST', 'exec'), ns)
    M = pickle.load(open(HERE + 'forward_pg/modelo_own.pkl', 'rb')); meta = json.load(open(HERE + 'forward_pg/modelo_own.json')); C = ns['c1own'](d)
    p = M.predict_proba(C[['T', 'L', 'bidL', 'act_i', 'lado_i']])[:, 1].astype(np.float32)
    Po = pd.DataFrame({'k': C.k.values, 'L': C.L.values, 't': C.t.values, 'p_OWN': p}); Po.to_pickle(BCO + f'Po_{d}.pkl.tmp'); os.replace(BCO + f'Po_{d}.pkl.tmp', BCO + f'Po_{d}.pkl')
    tj = BCO + 'C2o_thr.json'; J = json.load(open(tj))
    if d not in J: J[d] = {'OWN': {'0.5': float(meta['umbral_c05'])}}; atomic(tj, json.dumps(J))
    print('Po', d, len(Po), 'umbral', J[d]['OWN']['0.5'])
def producir(d):
    h = dt.datetime.now(dt.timezone.utc); m = h.hour * 60 + h.minute
    if 360 <= m < 555: raise SystemExit('BLOQUEADO: no se lanza trabajo pesado entre 06:00 y 09:15Z')
    cmds = [f'python3 -I {HERE}eval_thru1.py --puntuar {d}', f'cd {HERE}toxicidad_thru1 && python3 -I passT.py {d}', f'cd {HERE}redteam && python3 -I rt_sim.py {d}', f'cd {HERE}redteam && python3 -I rt_cxj150_cross.py {d}']
    for c in cmds:
        r = subprocess.run(['nice', '-n', '19', 'ionice', '-c3', 'bash', '-c', f'ulimit -v 3000000; export OMP_NUM_THREADS=1; {c}'])
        if r.returncode: raise SystemExit(f'FALLO ({r.returncode}): {c}')
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('--aceptacion', action='store_true'); ap.add_argument('--evaluar', action='store_true'); ap.add_argument('--producir'); ap.add_argument('--puntuar')
    ap.add_argument('--reevaluar-b2', default=None, metavar='REF', help='ADDENDUM5 sec. 3: reabre los terminales B2 con la referencia escrita (DECISION_LOG); la reevaluacion no puede emitir CANDIDATO/PROMOCION'); ap.add_argument('--cl-cache', default=Q.CL_CACHE); ap.add_argument('--desde', default=FWD_DESDE); ap.add_argument('--salida', default=HERE + 'thru1_fwd'); ap.add_argument('--hoy'); ap.add_argument('--ensayo', action='store_true', help='sin validez de dia ni aceptacion (solo ensayo sobre quemados)')
    a = ap.parse_args()
    if a.aceptacion:
        r = aceptacion(a.salida); print(json.dumps(r, indent=1, default=float)); sys.exit(0 if r['pass_'] else 2)
    elif a.evaluar: evaluar(a)
    elif a.producir: producir(a.producir)
    elif a.puntuar: puntuar(a.puntuar)
    else: ap.print_help()
