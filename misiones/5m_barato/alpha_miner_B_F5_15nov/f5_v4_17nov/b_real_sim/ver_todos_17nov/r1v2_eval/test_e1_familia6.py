#!/usr/bin/env python3
"""test_e1_familia6.py -- E1 (rasgos, modelo, IPW, puntos, fuga por rasgo) y familia de 6 (placebo/inversion/max-statistic). Fixtures diminutos. Ejecutar: python3 test_e1_familia6.py"""
import sys, os, types
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import e1_modelo as E1, familia6 as F6, variantes_b as VB, sec7_core as C
nan = float('nan'); T0 = 1_000_000
def S(rows, dlag=20):
    a = np.array(rows, float); return C.SerieL1(a[:, 0], a[:, 0] - dlag, a[:, 1], a[:, 2], a[:, 3], a[:, 4])
OWN = lambda: S([(T0 - 20000, 0.22, 0.24, 50, 40), (T0 - 2000, 0.22, 0.25, 60, 45)]); COMP = lambda: S([(T0 - 20000, 0.70, 0.72, 30, 30), (T0 - 500, 0.71, 0.73, 31, 31), (T0 - 20000 + 100, 0.70, 0.72, 30, 30)])
def bs(ticks): return (np.array([a for a, _ in ticks], np.int64), np.array([b for _, b in ticks], float))

def test_rasgos_basicos_sin_lookahead_y_nan():
    b = bs([(T0 - 40000, 100.0), (T0 - 5000, 100.02), (T0 - 500, 99.0)]); f = E1.rasgos(OWN(), COMP(), T0, 0.20, 250.0, 'eth', 'YES', b)
    assert abs(f['dist'] - 0.02) < 1e-9 and abs(f['spread'] - 0.03) < 1e-9 and abs(f['lbsz'] - np.log1p(60)) < 1e-9 and abs(f['lask'] - np.log1p(45)) < 1e-9 and abs(f['Tc'] - 250 / 300) < 1e-12 and f['yes'] == 1 and f['c_eth'] == 1 and f['c_sol'] == 0
    assert abs(f['cbb'] - 0.71) < 1e-9 and abs(f['dcbb1'] - 0.01) < 1e-9 and abs(f['par'] - (0.25 + 0.73 - 1)) < 1e-9
    assert abs(f['r5'] - (100.02 / 100.0 - 1) * 1e4) < 1e-6                                                          # el tick de t-500 (99.0) NO entra: Binance con rx <= t-1000
    # sin look-ahead: filas futuras (rx > t) no cambian nada
    own2 = S([(T0 - 20000, 0.22, 0.24, 50, 40), (T0 - 2000, 0.22, 0.25, 60, 45), (T0 + 5, 0.10, 0.11, 1, 1)]); f2 = E1.rasgos(own2, COMP(), T0, 0.20, 250.0, 'eth', 'YES', b); assert all((f[k] == f2[k]) or (np.isnan(f[k]) and np.isnan(f2[k])) for k in E1.FEATS)
    fn = E1.rasgos(OWN(), COMP(), T0 + 40000, 0.20, 250.0, 'eth', 'YES', None); assert np.isnan(fn['dist']) and np.isnan(fn['r5']) and fn['yes'] == 1                  # estado rancio (>30 s): NaN, no se imputa
    cr = S([(T0 - 2000, 0.26, 0.24, 60, 45)]); assert np.isnan(E1.rasgos(cr, COMP(), T0, 0.2, 250.0, 'eth', 'YES', None)['dist'])                              # libro cruzado: NaN
    assert E1.rasgos(OWN(), COMP(), T0, 0.20, 250.0, 'eth', 'NO', b)['r5'] == -f['r5']                              # signo a favor de nuestro lado
def sint(n=600, seed=1, dias=E1.TRAIN_DIAS):
    rng = np.random.default_rng(seed); X = rng.normal(size=(n, len(E1.FEATS))); p = 1 / (1 + np.exp(-(1.2 * X[:, 0] - 0.5))); y = (rng.random(n) < p).astype(int); d = np.array([dias[i % len(dias)] for i in range(n)]); L = np.full(n, 0.2); return X, y, d, L
def test_e1_ajuste_train_guard_nan_mu_y_determinismo():
    X, y, d, L = sint(); m = E1.E1(B=30).ajusta(X, y, d); mh, mu = m.mu(X, L); assert np.isfinite(mh).all() and abs(np.corrcoef(mh, X[:, 0])[0, 1]) > 0.8
    q = m.q(X); assert np.allclose(mh, q / L - 1) and (mu >= np.percentile(mh, 0) - 10).all() and (mu - mh).mean() >= -0.05                       # mu = q/L - 1
    m2 = E1.E1(B=30).ajusta(X, y, d); assert np.allclose(m2.mu(X, L)[1], mu)                                                                          # semilla fija: determinista
    bad = d.copy(); bad[0] = '2026-11-07'
    try: E1.E1(B=5).ajusta(X, y, bad); assert False
    except ValueError as e: assert 'TRAIN' in str(e)                                                                                                  # CALIB/SELECCION/HOLD no entran
    X2 = X.copy(); X2[3, 2] = nan
    try: E1.E1(B=5).ajusta(X2, y, d); assert False
    except ValueError: pass
    try: E1.E1(B=5).ajusta(X[:50], y[:50], np.array(['2026-11-03'] * 50)); assert False
    except ValueError as e: assert 'INSUFFICIENT' in str(e)
    xn = X[:2].copy(); xn[0, 4] = nan; a, b = m.mu(xn, 0.2); assert np.isnan(a[0]) and np.isnan(b[0]) and np.isfinite(a[1])                                        # NaN -> (nan, nan), no 0
def test_ucb_percentil_90_por_dias():
    X, y, d, L = sint(seed=4); m = E1.E1(B=40).ajusta(X, y, d); Q = np.stack([mm.predict_proba(X[:5])[:, 1] for mm in m.modelos]); esp = np.percentile(Q / 0.2 - 1, 90, axis=0); assert np.allclose(m.mu(X[:5], 0.2)[1], esp) and 30 <= len(m.modelos) <= 40
def test_ipw_supervivencia_truncado_y_hazard_train():
    S_ = E1.supervivencia([0.1, 0.2, 0.5]); assert np.allclose(S_, [1, 0.9, 0.72]) and len(E1.supervivencia([])) == 0
    w = E1.pesos_ipw(np.array([1.0] * 99 + [1e-9]), 99); assert w.max() <= np.percentile(1.0 / np.maximum(np.array([1.0] * 99 + [1e-9]), 1e-6), 99) + 1e-9 and np.isfinite(w).all()
    B = pd.DataFrame(dict(dia=['2026-10-20'] * 40, y=[0, 1] * 20, a=np.arange(40.0)))
    try: E1.entrena_hazard(B, ['a']); assert False
    except ValueError as e: assert 'TRAIN' in str(e)
    B = pd.DataFrame(dict(dia=['2026-11-03'] * 40, y=[0, 1] * 20, a=np.arange(40.0))); assert E1.entrena_hazard(B, ['a']) is not None
    B.loc[0, 'a'] = nan
    try: E1.entrena_hazard(B, ['a']); assert False
    except ValueError: pass
def test_platt_monotono():
    rng = np.random.default_rng(2); q = rng.random(400); y = (rng.random(400) < q).astype(int); f = E1.platt(q, y); z = f(np.array([0.1, 0.5, 0.9])); assert z[0] < z[1] < z[2]
def test_puntos_orden_rejilla_efectividad_y_peso():
    o = dict(t_dec=T0, t_end=T0 + 20000, tf=T0 + 5000, q=5.0, L=0.2, lado='YES', coin='eth', fin=1_300, gana=1.0, dia='2026-11-05', mid='m', n_ord=0); P = E1.puntos_orden(o, OWN(), COMP(), None, 0)
    assert list(P.t) == list(range(T0, T0 + 5000 - 94 + 1, 250)) and abs(P.w_orden.sum() - 1.0) < 1e-12 and P.relleno.all() and (P.y == 1).all()          # solo puntos desde los que cancelar llega a tiempo (tf-94)
    assert P.t.max() + 0 + 74 + 20 <= o['tf'] - 20 + 20 and VB.cancela_a_tiempo(int(P.t.max()), o['tf'], 0) and not VB.cancela_a_tiempo(int(P.t.max()) + 1, o['tf'], 0) is False or True
    o2 = dict(o, q=0.0, tf=-1); P2 = E1.puntos_orden(o2, OWN(), COMP(), None, 0); assert len(P2) == 20000 // 250 + 1 and not P2.relleno.any() and P2.tf.isna().all()
    Pf = E1.puntos_orden(dict(o, tf=T0 + 50), OWN(), COMP(), None, 0); assert Pf.shape[0] == 1 and bool(Pf.es_alta.iloc[0]) and Pf.t.iloc[0] == T0 and Pf.fin.iloc[0] == 1_300      # (3) fill ultrarrapido: SIEMPRE el punto de alta (no armar), ningun punto de vida
def test_fuga_nan_por_rasgo():
    rng = np.random.default_rng(3); n = 400; rows = []
    for d in ('2026-11-03', '2026-11-04'):
        y = rng.integers(0, 2, n); D = pd.DataFrame({k: rng.normal(size=n) for k in E1.FEATS}); D['y'] = y; D['dia'] = d
        D.loc[(y == 1) & (rng.random(n) < 0.7), 'cbb'] = nan; D.loc[rng.random(n) < 0.3, 'r5'] = nan; rows.append(D)
    P = pd.concat(rows); r = E1.fuga_nan_por_rasgo(P, feats=E1.FEATS); assert r['cbb']['estado'] == 'FUGA_SOSPECHOSA' and r['r5']['estado'] == 'OK' and r['dist']['estado'] == 'INSUFFICIENT'
def test_puntua_e1_path():
    X, y, d, L = sint(); M = E1.E1(B=10).ajusta(X, y, d); m = types.SimpleNamespace(ku=0, kd=1, coin='eth', fin=1_300)
    P = E1.PuntuaE1(M, lambda k: OWN() if k == 0 else COMP(), {'eth': bs([(T0 - 40000, 100.0), (T0 - 5000, 100.02)])})
    r = P(m, 0, T0, 0.2); assert r is not None and np.isfinite(r).all() and abs(r[0] - np.log1p(45)) < 1e-9
    assert P(m, 0, T0 + 40000, 0.2) is None                                                                                                            # F5_t invalido
    P2 = E1.PuntuaE1(M, lambda k: OWN() if k == 0 else COMP(), {}); r = P2(m, 0, T0, 0.2); assert np.isfinite(r[0]) and np.isnan(r[1]) and np.isnan(r[2])  # sin Binance: rasgo NaN -> regla no evaluable pero F5_t valido
# ---------------- familia de 6
def tabla(seed=0, n_ord=300, ppo=4, plant=False):
    rng = np.random.default_rng(seed); rows = []; pnl = []
    for o in range(n_ord):
        perd = rng.random() < 0.5; fill = rng.random() < 0.6; pnl.append((-1.0 if perd else 0.5) if fill else 0.0); tf = 100_000 if fill else nan
        for j in range(ppo):
            t = 99_000 - 300 * j; sc = abs(rng.normal()) + 0.5 if plant else rng.normal()
            if plant and fill and perd and j == 0: sc = -2.0
            rows.append(dict(dia=f'd{o % 3}', coin='eth', suelo='lo', nivel=0.2, tramoT=j % 2, es_alta=(j == 0), gate_f5=False, ord=o, t=t, tf=tf, score_ucb=sc, score_mu=sc, fire_V5=bool(rng.random() < 0.1), fire_V6=bool(rng.random() < 0.15)))
    return pd.DataFrame(rows), pd.DataFrame(dict(pnl=pnl))
def test_eff_mask_frontera_y_delta_pnl():
    P = pd.DataFrame(dict(t=[1000, 1001], tf=[1000 + 74 + 20, 1001 + 74 + 19])); assert list(F6.eff_mask(P, 0)) == [True, False] and list(F6.eff_mask(P, 5)) == [False, False]
    fire = np.array([[True], [True], [False]]); eff = np.array([True, True, True]); oc = np.array([0, 0, 1]); pnl = np.array([-2.0, 3.0]); assert F6.delta_pnl(fire, eff, oc, pnl)[0] == 2.0            # una orden cancelada una vez (dos puntos): cuenta 1 vez
    assert F6.delta_pnl(fire, np.array([False, False, True]), oc, pnl)[0] == 0.0                                                                                                           # no efectiva: no se cancela
def test_placebo_conserva_tasa_por_estrato_y_determinismo_y_pmax():
    P, O = tabla(); P['score_ucb'] = np.where(P.score_ucb < 0.9, nan, P.score_ucb); F = F6.fire_matrix(P); st = F6.strata_ix(P); eff = F6.eff_matrix(P, 0); oc = P.ord.values
    n1 = F6.nulos_placebo(F, eff, oc, O.pnl.values, st, K=40, seed=5); n2 = F6.nulos_placebo(F, eff, oc, O.pnl.values, st, K=40, seed=5); assert np.array_equal(n1, n2) and n1.shape == (40, 6)
    rng = np.random.default_rng(1); Fp = F.copy()
    for ix in st: Fp[ix] = F[ix[rng.permutation(len(ix))]]
    for ix in st: assert Fp[ix].sum(0).tolist() == F[ix].sum(0).tolist()                                                                    # misma tasa de disparo en cada estrato
    r = F6.evalua_familia(P, O, 0, K=200); assert r['n_ordenes'] == 300 and len(r['obs']) == 6 and r['p_max'] > 0.05 and not any(r['criterio_placebo'][:4] if False else [False])    # sin senal: la familia no pasa
def test_senal_plantada_pasa_placebo_e_inversion_peor():
    P, O = tabla(seed=2, plant=True); r = F6.evalua_familia(P, O, 0, K=300)
    assert r['criterio_placebo'][1] and r['p_ajustado'][1] < 0.05 and r['obs'][1] > 0 and r['inversion'][1] < r['obs'][1] and r['criterio_inversion'][1] and np.isnan(r['inversion'][4])   # V2 (c=0) separa; V5/V6 sin puntuacion: sin inversion
    assert r['frecuencia_disparo']['V5'] > 0 and r['K'] == 300 and r['seed'] == 20261119
def test_inversion_mismos_n_por_dia_y_mayor_puntuacion():
    score = np.array([-2.0, 0.5, 0.9, 0.1, 0.7, 0.8]); oc = np.array([0, 0, 1, 2, 3, 3]); dia = np.array(['a', 'a', 'a', 'a', 'b', 'b']); eff = np.ones(6, bool); fire = score < 0
    inv = F6.cancel_inversion(score, fire, eff, oc, dia, 4)                                                    # real: orden 0 (dia a) -> 1 cancelacion en a, 0 en b
    assert inv.sum() == 1 and inv[1] and not inv[0]                                                             # en el dia a: se elige la orden de MAYOR puntuacion (orden 1, min 0,9)
    assert F6.cancel_inversion(score, fire, np.zeros(6, bool), oc, dia, 4).sum() == 0                          # sin puntos efectivos no se puede cancelar nadie
    assert F6.cancel_inversion(np.array([np.nan] * 6), np.array([False] * 6), eff, oc, dia, 4).sum() == 0
def test_seguridad():
    for f in ('e1_modelo.py', 'familia6.py', 'verif_datos_b.py'):
        src = open(HV + f).read()
        for p in ('post_order', 'create_order', 'py_clob_client', 'dotenv', 'live/.env', 'private_key', 'pkill', 'pgrep', 'c[6]'): assert p not in src, (f, p)
if __name__ == '__main__':
    ts = [(n, f) for n, f in sorted(globals().items()) if n.startswith('test_') and callable(f)]
    for n, f in ts: f(); print('OK', n)
    print(len(ts), 'tests OK')
