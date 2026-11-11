#!/usr/bin/env python3
"""paso0_run_v2.py <fase> <modo>: COPIA de paso0_run.py (no se edita el original) sobre paso0_lib_v2 (assert real + conteo) y fills de out_v2 (modo causal/rx/legacy: concat_v2.py) o `orig` (out/g0_fills.pkl = regresion del original).
X1 lee sa_ms2 con reloj EXCHANGE (fuente v2) salvo modo orig (sa_ms v1). Salida out_v2/paso0_<modo>/<fase>.json. Fases ev NO soportada aqui (necesita trg de 03-07). Original: paso0_run.py <fase> : fases 'ev' (EV incondicional G0 + potencia), 'e1n1' (etapa 0 E1 + TRAIN N1), 'x1' (etapa 0 X1). Solo dias quemados. Salida out/paso0/<fase>.json. Determinista."""
import sys, os, json, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, H)
import l2eval as E, paso0_lib_v2 as P
fase, MODO = sys.argv[1], sys.argv[2]
OUT = H + f'out_v2/paso0_{MODO}/'; os.makedirs(OUT, exist_ok=True)
if MODO == 'orig': U, S = P.cargar()
else: U, S = P.cargar(H + f'out_v2/g0_fills_{MODO}_ALL.pkl', H + f'out_v2/g0_segs_{MODO}_ALL.pkl')
B = 20000
print('integridad', MODO, 'rellenos', U.attrs['n_rellenos'], 'sin_segmento', U.attrs['n_rellenos_sin_segmento'], 'dias', sorted(U.dia.unique())[:1], sorted(U.dia.unique())[-1:], flush=True)
def dump(nm, o): json.dump(o, open(OUT + nm + '.json', 'w'), indent=1, default=lambda x: x.item() if hasattr(x, 'item') else str(x))

if fase == 'ev':
    raise SystemExit('fase ev no soportada en v2')
if False:
    R = dict(G0=P.resumen_ev(U, S), G0_geo6=P.resumen_ev(U[U.geo6], S[S.dia.isin(U.dia.unique())]))
    R['G0_dias_0307'] = P.resumen_ev(U[U.dia.isin(P.DIAS[8:13])], S, P.DIAS[8:13])
    R['por_moneda'] = {c: P.resumen_ev(U[U.act == c], None) for c in ('ETH', 'SOL', 'XRP')}
    R['por_L'] = {str(L): P.resumen_ev(U[U.L == L], None) for L in sorted(U.L.unique())}
    R['por_bloque_UTC'] = {str(b): P.resumen_ev(U[U.bloque == b], None) for b in range(4)}
    R['por_Trem_arm'] = {str(t): P.resumen_ev(U[U.trb == t], None) for t in range(3)}
    # validez de dias por codigo
    R['validez'] = [E.valida_dia(d, P.BAD_DIR, P.B40_DIR, P.SA_DIR) for d in P.DIAS]
    # aceptacion §4: G0 03-07 con L2 valido (n 1.350, EV -0,245 +-1 eur)
    T = pd.concat([pd.read_pickle(H + f'out/trg_{d}.pkl') for d in P.DIAS[8:13]])
    m = U[U.dia.isin(P.DIAS[8:13])].merge(T[['dia', 'k', 'L', 'tf', 'bad']], on=['dia', 'k', 'L', 'tf'], how='left', validate='1:1'); v = m[m.bad.isna()]
    R['aceptacion_G0_0307_L2valido'] = dict(n=len(v), pnl=round(float(v.pnl2.sum()), 2), ev=round(float(v.pnl2.sum() / v.cost.sum()), 4), esperado_n=1350, esperado_ev=-0.245, ok=bool(len(v) == 1350 and abs(v.pnl2.sum() / v.cost.sum() + 0.245) < 0.005))
    # sd diaria del PnL base y sd/potencia (de la serie base, pareada = misma serie con/sin regla; ver e1n1/x1 para Delta)
    xd = U.groupby('dia').pnl2.sum().reindex(P.DIAS).values
    R['potencia_base_pnl_dia_rb0.2'] = E.stats_potencia(xd)
    dump('ev', R)
if fase == 'e1n1':
    R = {}
    # ---- E1 etapa 0 (26-Oct..09-Nov, 15 dias): Lambda 310 primaria; sens 150/500/560. Base = G0 (U1 incluye G0; GEO6 se reporta aparte)
    dias = P.DIAS; res = {}
    for lam in (150, 310, 500, 560):
        for base in ('G0', 'G0_GEO6'):
            V = U if base == 'G0' else U[U.geo6].reset_index(drop=True)
            aff, inv = P.e1_aff(V, lam); V = V.assign(aff=aff, aff_inv=inv, pot0=-V.pnl0, pot2=-V.pnl2)
            g = E.gate(V, dias, f'E1_lam{lam}_{base}', B=B, look=None, tipo='quita', aplica_G6=True)
            for k, nm in (('0.0', 'pot0'), ('0.2', 'pot2')):
                o, p, pm = P.placebo_tokwin(V, aff, V[nm].values, B=B); g['rb'][k]['placebo_grupo_token_p'] = round(p, 5); g['rb'][k]['placebo_grupo_token_media'] = round(pm, 3)
            for k in ('0.0', '0.2'):
                r = g['rb'][k]; r['kill_E1'] = bool(r['sum_delta'] <= r['placebo_grupo_token_media'] or (np.array(r['daily']) > 0).sum() < np.ceil(10 / 15 * len(dias)))
            g['n_unidades'] = int(len(V)); g['frac_coste_quitado'] = round(float(V.cost[aff].sum() / V.cost.sum()), 3); g['n_quitadas'] = int(aff.sum())
            res[f'lam{lam}_{base}'] = g
    R['E1'] = res
    # ---- N1 TRAIN: 26-Oct..09-Nov
    C = P.n1_celdas(U); quit_, arm_ = P.n1_aplica(U, C)
    V = U[U.geo6].reset_index(drop=True); a2, _ = P.n1_aplica(V, C)
    V = V.assign(aff=a2, aff_inv=~a2, pot0=-V.pnl0, pot2=-V.pnl2)
    g = E.gate(V, dias, 'N1_TRAIN_insample', B=B, look=None, tipo='quita')
    n1 = dict(celdas_totales=int(len(C)), celdas_armadas=int(C.arma.sum()), celdas_n30=int((C.n >= 30).sum()), cobertura_coste_no_armado=g['rb']['0.0']['cobertura_coste'], gate=g,
              cobertura_exacta=float(V.cost.values[a2].sum() / V.cost.sum()), muerte=bool(C.arma.sum() == 0 or V.cost.values[a2].sum() / V.cost.sum() >= 0.85), celdas_armadas_lista=C[C.arma].to_dict('records'))
    # validacion cronologica descriptiva: elegir con 26-Oct..02-Nov, evaluar 03-09 Nov
    Ua = U[U.dia.isin(P.DIAS[:8])]; Ub = U[U.dia.isin(P.DIAS[8:])]; Ca = P.n1_celdas(Ua); Vb = Ub[Ub.geo6].reset_index(drop=True); ab, _ = P.n1_aplica(Vb, Ca)
    Vb = Vb.assign(aff=ab, aff_inv=~ab, pot0=-Vb.pnl0, pot2=-Vb.pnl2); gb = E.gate(Vb, P.DIAS[8:], 'N1_VAL_0309_celdas_de_2610_0211', B=B, look=None, tipo='quita')
    n1['val_cronologica'] = dict(celdas_armadas_train=int(Ca.arma.sum()), gate=gb)
    R['N1'] = n1; R['celdas_N1'] = C.to_dict('records')
    dump('e1n1', R)
if fase == 'x1':
    dias_x = P.DIAS[:8] + P.DIAS[13:]; frames = []
    var = dict(base=dict(d_det=250, ticks_adj=0), d_det150=dict(d_det=150, ticks_adj=0), d_det500=dict(d_det=500, ticks_adj=0), menos2ticks=dict(d_det=250, ticks_adj=2))
    cache = {}
    for d in dias_x:
        if not os.path.exists((P.SA_DIR + f'ms_{d}.npz') if MODO == 'orig' else (P.SA2_DIR + f'ms2_{d}.npz')): print('sin sa_ms', d); continue
        for vn, kw in var.items(): cache[(vn, d)] = P.x1_dia(U, d, clock='ex', fuente='v1' if MODO == 'orig' else 'v2', **kw)
        print('x1 dia', d, flush=True)
    R = dict(dias_usados=sorted({d for (_, d) in cache}), variantes={})
    for vn in var:
        X = pd.concat([cache[(vn, d)] for d in sorted({d for (v, d) in cache if v == vn})]); V = U.loc[X.index].copy().join(X)
        for mcut in (1500, 1000, 2000):
            elig = (V.M >= 150) & (V.M <= mcut) & V.cov_ok; inv = (V.M > mcut) & V.cov_ok
            W = V.reset_index(drop=True).assign(aff=elig.values, aff_inv=inv.values, pot0=V.pot_x.values, pot2=V.pot_x.values)
            g = E.gate(W, sorted(W.dia.unique()), f'X1_{vn}_M{mcut}', B=B, look=None, tipo='adicion', nmin=150, pool=W.cov_ok.values)
            # placebo estratificado dia x L x moneda a igual cobertura entre unidades con cobertura posible
            o, p, pm, _ = E.placebo(W, W.aff.values, W.pot0.values, B=B, pool=W.cov_ok.values)
            # IC90 por CIERRE (cluster dia, fin)
            cl = W[W.aff].groupby(['dia', 'fin']).pot0.sum().values; rng = np.random.default_rng(E.SEED)
            lb = float(np.quantile(rng.choice(cl, (B, len(cl))).mean(1), 0.05)) if len(cl) else float('nan')
            r = g['rb']['0.0']; dd = np.array(r['daily'])
            st0 = dict(delta=round(o, 3), n_coberturas=int(W.aff.sum()), n_cierres=int(len(cl)), ic90_lb_por_cierre=round(lb, 4), pct_dias_pos=r['pct_dias_pos'], placebo_p=round(p, 5), placebo_media=round(pm, 3), umbral_p=round(0.05 / 3, 5),
                       sin_2_mejores=r['sin_2_mejores'], monedas_pos=r['monedas_pos'], delta_inversion_lentas=r['delta_inv'], tam_ge_q=round(float(W[W.aff].size_ok.mean()), 3) if W.aff.any() else None,
                       frac_espejo=round(float(W[W.aff].mirror.mean()), 3) if W.aff.any() else None, n_dias=len(dd), daily=r['daily'], sd_dia=r['sd_dia'], media_dia=r['media_dia'])
            st0['pasa_etapa0'] = bool(len(dd) >= 8 and o > 0 and lb > 0 and st0['pct_dias_pos'] >= 0.7 and p < 0.05 / 3 and st0['sin_2_mejores'] > 0 and st0['monedas_pos'] >= 2 and (st0['tam_ge_q'] or 0) >= 0.9 and st0['n_coberturas'] >= 150 and (st0['delta_inversion_lentas'] or 0) <= 0)
            R['variantes'][f'{vn}_M{mcut}'] = st0
    dump('x1', R)
