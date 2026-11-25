#!/usr/bin/env python3
"""sec7_calculos.py -- R1v2 sec.7 (b) estres NONE, (c) 13 sin L2, (d) error de tiempo de relleno de los TP. Funciones puras sobre DataFrames; sin I/O de datos de produccion.
Etiqueta obligatoria de toda salida con EV: ETIQUETA. No afirma 'SOLO = la AS' ni 'F5_t evita la NONE' (CONTRATO_R1v2_19nov_v2 sec.10e)."""
import numpy as np

ETIQUETA = 'RELLENOS VISIBLES + ESTRES NONE (no es EV de B real)'
TASAS_NONE = (0.017, 0.018, 0.019)      # por orden colocada (EXPEDIENTE RE-B-SOLO-OBSERVABLE: 1,7-1,9 %; TT excluidos: ya son rellenos visibles del motor)
EV_NONE = (-0.115, -0.176)              # EV/EUR por relleno NONE: central y pesimista
TERCILES = ('bajo', 'medio', 'alto')


def _ev(pnl, cost):
    return float(pnl / cost) if cost > 0 else float('nan')


def estres_none(R, tasa=0.018, ev_none=-0.115, coste_none=None, terc_col='tercil'):
    """(b) Estres NONE UNIFORME: la MISMA tasa y EV en los 3 terciles (no se condiciona a F5_t). R: ordenes simuladas (cols q, cost, pnl, tercil), una fila por orden colocada.
    n_none(tercil) = tasa * n_ordenes(tercil); coste de cada NONE = coste_none (por defecto el coste medio de TODOS los rellenos visibles, no por tercil, para no filtrar F5_t).
    pnl_none = n_none * coste_none * ev_none. Sin doble conteo con los TT: la tasa ya los excluye y los TT estan en R como rellenos visibles.
    Devuelve por tercil: n_ordenes, pct_ordenes, p_relleno, EV_visible (EUR ponderado: sum pnl/sum coste, NaN si sin rellenos), pnl_visible, pnl_none, EV_con_estres, pnl_total. 'inval' se reporta aparte."""
    fil = R[R.q > 0]; cm = float(fil.cost.mean()) if len(fil) else 0.0
    c_none = cm if coste_none is None else float(coste_none); N = len(R); out = {}
    for t in list(TERCILES) + ['inval']:
        g = R[R[terc_col] == t]; f = g[g.q > 0]
        if len(g) == 0 and t == 'inval': continue
        nn = tasa * len(g); pv = float(f.pnl.sum()); cv = float(f.cost.sum()); pn = nn * c_none * ev_none
        out[t] = dict(n_ordenes=int(len(g)), pct_ordenes=float(len(g) / N) if N else float('nan'), p_relleno=float(len(f) / len(g)) if len(g) else float('nan'),
                      n_none_esperadas=float(nn), coste_none=c_none, EV_visible=_ev(pv, cv), pnl_visible=pv, pnl_none=float(pn),
                      EV_con_estres=_ev(pv + pn, cv + nn * c_none), pnl_total=float(pv + pn))
    out['_params'] = dict(tasa=tasa, ev_none=ev_none, coste_none=c_none, etiqueta=ETIQUETA, uniforme=True)
    return out


def rejilla_estres(R, **kw):
    return {f't{t}_ev{e}': estres_none(R, tasa=t, ev_none=e, **kw) for t in TASAS_NONE for e in EV_NONE}


# ------------------------------------------------------------------ (c) 13 sin L2
def grupos_clase1(F):
    """F: filas de octubre (so1_filas.pkl: c1, mk, tt, hit (opcional, de so1b), dia, cost, pnl, tp). Grupos de la clase 1: TT / REST / NONE_L2 / SIN_L2 (la NONE NO incluye SIN_L2) y TP aparte."""
    F = F.copy()
    for c, v in (('tt', False), ('hit', 0.0)):
        if c not in F.columns: F[c] = v
    F['tt'] = F.tt.fillna(False).astype(bool); F['hit'] = F.hit.fillna(0).astype(float)
    g = np.where(~F.c1, np.where(F.tp, 'TP', 'otros'),
        np.where(~F.mk, 'SIN_L2', np.where(F.tt, 'TT', np.where(F.hit >= 1, 'REST', 'NONE_L2'))))
    F['grupo'] = g
    return F


def trata_sin_l2(F, dia_excluir='2026-10-23'):
    """(c) Dos versiones SIEMPRE: CON y SIN 23-Oct. Los SIN_L2 no se imputan al canal NONE ni al TP; su peso (n, coste, pnl, EV) se muestra aparte. 23-Oct no es confirmatorio.
    Es descriptivo de los rellenos REALES historicos de octubre (no es EV de R1v2)."""
    F = grupos_clase1(F); out = {}
    for nombre, G in (('CON_23oct', F), ('SIN_23oct', F[F.dia != dia_excluir])):
        d = {}
        for gr, g in G.groupby('grupo'):
            d[gr] = dict(n=int(len(g)), cost=float(g.cost.sum()), pnl=float(g.pnl.sum()), EV=_ev(g.pnl.sum(), g.cost.sum()), n_dias=int(g.dia.nunique()))
        c1 = G[G.c1]; d['clase1_total'] = dict(n=int(len(c1)), cost=float(c1.cost.sum()), pnl=float(c1.pnl.sum()), EV=_ev(c1.pnl.sum(), c1.cost.sum()), n_dias=int(c1.dia.nunique()))
        out[nombre] = d
    out['_nota'] = 'SIN_L2 aparte, no imputado a NONE ni a TP; 23-Oct no confirmatorio (INSUFFICIENT por dias)'
    return out


def verifica_unidades_tk(T):
    """(f) del contrato sec.10: tk_sz / tk_rem. T: tomador_202 (tk_tipo, tk_sz, tk_rem, tk_eq, real_q). tk_rem = FRACCION del tamano del tomador que quedo sin casar (debe estar en [0,1]);
    rem_sh = tk_rem*tk_sz. Prueba de consistencia: en compra_comp el tomador casa >= real_q de NUESTRO token, luego tk_sz*(1-tk_rem) >= real_q (hipotesis 'acciones') o
    tk_sz/tk_eq*(1-tk_rem) >= real_q (hipotesis 'USDC'). Se reportan las fracciones de filas que cumplen; 'acciones' solo puede quedar 'no refutada' (la prueba USDC es mas laxa): unidad_resuelta=True unicamente si se refuta 'acciones' y 'USDC' pasa; si no, hay que confirmar con la fuente de tk_sz (v1_decode_tomador.py)."""
    X = T[T.tk_tipo == 'compra_comp']; n = len(X)
    if n == 0: return dict(n=0, unidad_resuelta=False, motivo='sin compra_comp')
    tol = 1e-6
    frac_ok = bool(((X.tk_rem >= -tol) & (X.tk_rem <= 1 + tol)).all())
    acc = float(((X.tk_sz * (1 - X.tk_rem)) + 1e-6 >= X.real_q).mean())
    usd = float((((X.tk_sz / X.tk_eq.where(X.tk_eq > 0)) * (1 - X.tk_rem)) + 1e-6 >= X.real_q).mean())
    # prueba UNILATERAL: 'USDC' es mas permisiva (divide por tk_eq<1), asi que pasarla no discrimina; 'acciones' si puede ser refutada
    res = 'USDC' if (acc < 0.95 and usd >= 0.95) else ('acciones_no_refutada' if acc >= 0.95 else 'sin_resolver')
    return dict(n=int(n), tk_rem_es_fraccion_0_1=frac_ok, frac_consistente_acciones=acc, frac_consistente_usdc=usd, unidad=res, unidad_resuelta=(res == 'USDC'))


# ------------------------------------------------------------------ (d) error de tiempo de los TP
LCANCEL_CONTRATO = dict(fuente='CONTRATO/DISENO: paquete_l ensayo_real_B2/B3/B5 13-Nov n=313 (257 lo / 58 amb / 0 hi); p50 33, p90 74, estres 111 (pool; no separable por clase desde los informe_final)',
                        lo=dict(p50=33.0, p90=74.0, estres=111.0), indet=dict(p50=33.0, p90=74.0, estres=111.0), hi=None)


def _pct(x, q):
    return float(np.percentile(x, q)) if len(x) else float('nan')


def error_tiempo_tp(T, lcancel=None, clase_col='clase_suelo', sim_col='v3d_BASE_f_tf', real_col='real_tm3'):
    """(d) |t_sim - t_real| en los TP emparejados (sim con relleno Y real con relleno; relojes exchange: t_sim = sello tm3 de la cinta, t_real = real_tm3 = etiqueta, nunca decision).
    T: tomador_202 con 'sim' (bool TP), sim_col (ms; -1 = sin relleno sim), real_col y clase_col (lo/hi/indet por ventana, causal). lcancel: dict clase -> dict(p50,p90) o None (hi: no validado).
    Veredicto por clase: INSUFFICIENT si p90_err > L_cancel p90 (regla del contrato: 'si p90 > L_cancel'); flag_estricto si p90_err > L_cancel p50. hi = NO_VALIDADO (lo + sens 74/111/147)."""
    lc = lcancel or LCANCEL_CONTRATO
    P = T[(T.sim.astype(bool)) & (T[sim_col] > 0) & np.isfinite(T[real_col])].copy()
    P['err'] = (P[sim_col].astype(float) - P[real_col].astype(float)).abs(); P['err_signed'] = P[sim_col].astype(float) - P[real_col].astype(float)
    out = {}
    clases = ['TODAS'] + sorted(P[clase_col].dropna().unique().tolist()) if clase_col in P.columns else ['TODAS']
    for c in clases:
        g = P if c == 'TODAS' else P[P[clase_col] == c]
        e = g.err.values; d = dict(n=int(len(g)), p50=_pct(e, 50), p90=_pct(e, 90), max=float(e.max()) if len(e) else float('nan'), sesgo_p50=_pct(g.err_signed.values, 50))
        L = lc.get(c) if c != 'TODAS' else lc.get('lo')
        if c == 'hi' or L is None: d['veredicto'] = 'NO_VALIDADO (hi sin latencia medida; lo + sens 74/111/147)'; d['L_cancel'] = None
        elif d['n'] == 0: d['veredicto'] = 'INSUFFICIENT (n=0)'; d['L_cancel'] = L
        else:
            d['L_cancel'] = L; d['p90_gt_Lp90'] = bool(d['p90'] > L['p90']); d['flag_estricto_p90_gt_Lp50'] = bool(d['p90'] > L['p50'])
            d['veredicto'] = 'INSUFFICIENT: cancelar a tiempo no evaluable' if d['p90_gt_Lp90'] else 'evaluable (p90_err <= L_cancel p90)'
        for s in (74.0, 111.0, 147.0): d[f'p90_le_{int(s)}'] = bool(d['p90'] <= s) if d['n'] else None
        out[c] = d
    out['_nota'] = 'condicion previa a cualquier EV (CONTRATO_R1v2 sec.11.3); error exchange-vs-exchange; mezcla de relojes del canal bloqueo (rx) NO incluida aqui'
    return out


def clase_suelo_ventana(h1, h2):
    """Clase causal lo/hi/indet de una ventana usando suelo_causal.clase_de_ventanas (h1, h2: histogramas de d=rx-ex en bins de 1 ms [-50,400] de las dos mitades PREVIAS a t). mixta -> indet."""
    import sys, os
    d = os.path.abspath(__file__)
    for _ in range(4): d = os.path.dirname(d)
    sys.path.insert(0, d)      # f5_v4_17nov/ (suelo_causal.py)
    import suelo_causal as SC
    f, diag = SC.clase_de_ventanas(h1, h2)
    return ('indet' if f == 'mixta' else f), diag
