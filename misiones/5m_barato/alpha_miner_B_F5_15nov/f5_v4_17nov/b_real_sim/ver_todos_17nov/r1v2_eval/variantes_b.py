#!/usr/bin/env python3
"""variantes_b.py -- R1v2 FASE B (parcial): piezas PURAS de V5 (CXJ150 sobre B real, ADENDA_02/03/04) y V6 (E1b S1, ADENDA_05) + max-statistic, solape, % sin dato y test de fuga de ventanas.
Referencias (solo lectura, verificadas por test_variantes_b.py): passT_v4.py sha 85256bcc... (bnr l.75-80, JUMP 81-83, first_after 84-85, jadv 116, ja3 117, cxj 131-133) y e1_sim.py sha f826196d... (bn_trig l.46-56).
NO cambia el motor ni b_policy_sim: devuelve MARCAS por orden (no armar / disparo en vida / cancelacion efectiva) que el runner de FASE B aplicara. 0 ordenes, 0 red.
PENDIENTE (no implementado): V1-V4 (mu_ucb<-c, entrenamiento E1 + hazard v11), integracion de la cancelacion en el replay (re-armado), horquilla de bloqueo {0,Delta,nivel} (Delta sin definir en el prereg), cruce m5_registro vs x_*.csv.gz 17-18 Nov."""
import numpy as np, pandas as pd

V5 = dict(w_ms=1000, thr_bps=3.0, no_armar_ms=3000, nombre='V5_CXJ150')       # ADENDA_04: retorno 1 s por tick >=3 bps; (tq-3000, tq]
V6 = dict(w_ms=2000, thr_bps=2.0, no_armar_ms=2068, nombre='V6_E1bS1')        # ADENDA_05: retorno 2 s por tick >=2 bps; (tq-2068, tq]
DELAY_ARMAR_MS = 300                                                           # tq = t - 300 (convencion passT_v4 / ADENDA_03 C, ADENDA_04 3)
STALE_MS = 15000; MARGEN_CASADO_MS = 20; L_CANCEL = dict(primaria=74, sens=(111, 147))   # paquete_l 13-Nov B2/B3/B5 (ADENDA_03 B)

def ordena_rx(t, p):
    """ordena por RECEPCION (estable): recv no es monotono en el fichero (1-2,7 % de pasos negativos, CONTRATO ADENDA_05 (b))."""
    t = np.asarray(t, np.int64); o = np.argsort(t, kind='stable'); return t[o], np.asarray(p, float)[o]

def ret_bps(t, p, times, w):
    """= passT_v4.bnr: retorno en bps entre (times - w) y times con el ultimo tick <= cada instante; NaN si j0/j1<0 o el ultimo tick es rancio (> 15 s)."""
    times = np.asarray(times, np.int64)
    if len(t) == 0: return np.full(len(times), np.nan)
    j1 = np.searchsorted(t, times, side='right') - 1; j0 = np.searchsorted(t, times - w, side='right') - 1
    ok = (j1 >= 0) & (j0 >= 0) & (t[np.maximum(j1, 0)] > times - STALE_MS)
    return np.where(ok, (p[np.maximum(j1, 0)] / p[np.maximum(j0, 0)] - 1) * 1e4, np.nan)

def saltos(t, p, var):
    """instantes de TICK con retorno por tick >= +thr (up) / <= -thr (dn), inclusivo. = passT_v4 JUMP (V5) / e1_sim.bn_trig con W=2000, X=2 (V6, ver diferencias en el test)."""
    r = ret_bps(t, p, t, var['w_ms']); thr = var['thr_bps']
    with np.errstate(invalid='ignore'): return dict(up=t[r >= thr - 1e-12], dn=t[r <= -thr + 1e-12])

def adverso(J, lado):
    """adverso para el lado de la puja: YES(Up) -> bajada (dn); NO(Down) -> subida (up). VERIFICAR YES==Up en los tokens de B antes de usar (ADENDA_04 2): PENDIENTE de datos."""
    if lado not in ('YES', 'NO'): raise ValueError(lado)
    return J['dn'] if lado == 'YES' else J['up']

def no_armar(jadv, t, var):
    """True si hubo un tick adverso con tau en (tq - no_armar_ms, tq], tq = t - 300 (alta o repegado en t). = ja3 de passT (searchsorted right-right) con ventana V5=3000 / V6=2068."""
    tq = int(t) - DELAY_ARMAR_MS
    return bool(np.searchsorted(jadv, tq, 'right') - np.searchsorted(jadv, tq - var['no_armar_ms'], 'right') > 0)

def primer_disparo(jadv, t0, t1):
    """= passT first_after: primer tick adverso con t0 <= tau <= t1 (solo desde la llegada de la orden). None si no hay."""
    i = np.searchsorted(jadv, t0, side='left'); return int(jadv[i]) if i < len(jadv) and jadv[i] <= t1 else None

def cancela_a_tiempo(rx, casado, t_proc, l_cancel=L_CANCEL['primaria']):
    """efectividad (CONTRATO sec.5): rx + t_proc + L_cancel <= casado - 20 ms. t_proc = tiempo de computo MEDIDO y declarado: argumento OBLIGATORIO, sin default (code-review 3 #9). `casado` en reloj EXCHANGE."""
    return bool(rx is not None and casado is not None and rx + t_proc + l_cancel <= casado - MARGEN_CASADO_MS)

def marca_orden(jadv, t_dec, t_arr, t_end, tf, var, t_proc, l_cancel=L_CANCEL['primaria']):
    """marcas de UNA orden de B simulada: no_armar (en su alta/repegado t_dec), disparo (primer tick adverso en vida), cancela_fill (el relleno tf existe y la cancelacion llega a tiempo). tf=None/<0: sin relleno. tf debe estar en reloj EXCHANGE: para rellenos por bloqueo (tf=t_rx) pasar t_ex."""
    tb = primer_disparo(jadv, t_arr, t_end); fill = tf is not None and tf >= 0
    return dict(no_armar=no_armar(jadv, t_dec, var), disparo=tb is not None, t_disparo=tb, cancela_fill=bool(fill and tb is not None and cancela_a_tiempo(tb, tf, t_proc, l_cancel)))

def marca_ordenes(R, series, var, t_proc, l_cancel=L_CANCEL['primaria']):
    """R: ordenes de b_policy_sim (coin, lado, t_dec, t_arr, t_end, tf, q). series: {coin: (t_rx_ordenado, precio)}. Devuelve R con columnas pref_no_armar/disparo/cancela_fill y 'sin_dato' (sin tick fresco en tq)."""
    R = R.copy(); J = {c: saltos(t, p, var) for c, (t, p) in series.items()}; nm = var['nombre']; rows = []
    for r in R.itertuples():
        c = str(r.coin).lower(); t, p = series.get(c, (np.array([], np.int64), np.array([])))
        jad = adverso(J[c], r.lado) if c in J else np.array([], np.int64)
        tf = None
        if r.q > 0:
            tf = int(r.tf)
            if getattr(r, 'canal', '') == 'bloqueo':       # relleno por bloqueo: tf = t_rx; el casado se mide en reloj EXCHANGE (t_ex_fill de puerta0_core.t_ex_fills). Fail-closed si falta.
                tx = getattr(r, 't_ex_fill', float('nan'))
                if not np.isfinite(tx): raise ValueError('relleno bloqueo sin t_ex_fill: no se puede medir la efectividad en reloj exchange')
                tf = int(tx)
        m = marca_orden(jad, int(r.t_dec), int(r.t_arr), int(r.t_end), tf, var, t_proc, l_cancel)
        m['sin_dato'] = bool(np.isnan(ret_bps(t, p, [int(r.t_dec) - DELAY_ARMAR_MS], var['w_ms'])[0])) if len(t) else True
        rows.append(m)
    M = pd.DataFrame(rows, index=R.index)
    for c in ('no_armar', 'disparo', 'cancela_fill', 'sin_dato'): R[f'{nm}_{c}'] = M[c].values
    return R

def pct_sin_dato(R, nombre):
    """% de altas/repegados (una fila por orden) sin dato Binance fresco, por moneda (ADENDA_03 C.2 / 05 2f); XRP tiene huecos >15 s."""
    c = f'{nombre}_sin_dato'; return {k: dict(n=int(len(g)), pct=float(g[c].mean())) for k, g in list(R.groupby('coin')) + [('todas', R)]}

def frecuencia_disparo(R, nombre):
    """fraccion de VIDAS con >=1 disparo, de altas bloqueadas y de rellenos cancelados a tiempo; si disparo en >50 % de las vidas => 'solo no operar' (ADENDA_01 A1)."""
    f = float(R[f'{nombre}_disparo'].mean()) if len(R) else float('nan'); fi = R[R.q > 0]
    return dict(frac_vidas_con_disparo=f, frac_altas_bloqueadas=float(R[f'{nombre}_no_armar'].mean()) if len(R) else float('nan'), frac_rellenos_cancelados=float(fi[f'{nombre}_cancela_fill'].mean()) if len(fi) else float('nan'),
                solo_no_operar=bool(f > 0.5))

def solape(R, a='V5_CXJ150', b='V6_E1bS1', col='disparo'):
    """intersección V5 y V6 (ADENDA_05 4): ambas, V5 sin V6, V6 sin V5, ninguna. Descriptivo: apilar NO es variante nueva."""
    x, y = R[f'{a}_{col}'].astype(bool), R[f'{b}_{col}'].astype(bool)
    return dict(ambas=int((x & y).sum()), solo_v5=int((x & ~y).sum()), solo_v6=int((~x & y).sum()), ninguna=int((~x & ~y).sum()), n=int(len(R)))

def p_max_permutacion(obs, nulos):
    """max-statistic: obs (n_var,) estadisticos observados (mayor = mejor), nulos (K, n_var) bajo placebo. p_ajustado_k = (1 + #{max_j nulo_j >= obs_k}) / (K + 1); p_max = p del mejor observado. Una familia = una sola prueba."""
    obs = np.asarray(obs, float); nulos = np.asarray(nulos, float); mx = np.nanmax(nulos, axis=1); K = len(mx)
    adj = np.array([(1 + int((mx >= o).sum())) / (K + 1) for o in obs]); return dict(p_ajustado=adj.tolist(), p_max=float(adj[int(np.nanargmax(obs))]), K=int(K), n_var=int(len(obs)))

def mantiene_signo(evs):
    """horquilla de bloqueo {0, Delta, nivel}: un EV es valido solo si mantiene signo (no nulo) en los tres. evs: dict nombre->EV. Pura; la definicion de Delta es PENDIENTE."""
    v = [x for x in evs.values()]; return bool(len(v) >= 3 and all(np.isfinite(x) and x != 0 for x in v) and (all(x > 0 for x in v) or all(x < 0 for x in v)))

def fuga_flag(R, col, K=1000, seed=20261119, banda=(0.40, 0.60)):
    """test de fuga de ventana (2000 ms / cooldown 2068 / 1000 ms): el flag NO debe predecir el desenlace de NUESTRO token (gana, solo etiqueta). AUC por dia (banda provisional como en puerta0_core) y p por permutacion
    del flag DENTRO de dia x moneda (media de |AUC-0,5| por dia). Un flag con NaN-si-no-hay-dato = fuga: aqui sin_dato se trata como no-disparo, nunca como y=0."""
    from puerta0_core import auc
    rng = np.random.default_rng(seed); R = R.reset_index(drop=True); y = (R.gana > 0.5).astype(int).values; f = R[col].astype(int).values; dia = R.dia.values
    def est(fl): return np.nanmean([abs(auc(fl[dia == d], y[dia == d])[0] - 0.5) for d in np.unique(dia)])
    obs = est(f); grp = [np.where((R.dia == d) & (R.coin == c))[0] for d, c in R[['dia', 'coin']].drop_duplicates().itertuples(index=False)]; ge = 0
    for _ in range(K):
        g = f.copy()
        for ix in grp: g[ix] = rng.permutation(f[ix])
        ge += est(g) >= obs
    por_dia = {d: auc(f[dia == d], y[dia == d])[0] for d in np.unique(dia)}; fuera = [d for d, a in por_dia.items() if np.isfinite(a) and (a < banda[0] or a > banda[1])]
    return dict(col=col, auc_por_dia=por_dia, est_obs=float(obs), p_perm=float((1 + ge) / (K + 1)), dias_fuera_banda=fuera, estado='FUGA_SOSPECHOSA' if fuera else 'OK')
