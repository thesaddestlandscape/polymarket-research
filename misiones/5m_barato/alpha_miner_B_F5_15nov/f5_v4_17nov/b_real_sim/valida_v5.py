#!/usr/bin/env python3
"""valida_v5.py TAG [VAR=BASE] -- metricas de validacion (contrato v2 sec.5) sobre out_verif_v5/V5_<TAG>_<dia>.pkl (4 dias 20-23 Oct). Solo calculo."""
import sys, json, glob, numpy as np, pandas as pd
FLOOR = 1e-3; H = '/root/polymarket-research/misiones/5m_barato/alpha_miner_B_F5_15nov/f5_v4_17nov/b_real_sim/'
def carga(tag):
    fs = sorted(glob.glob(H + f'out_verif_v5/V5_{tag}_2026-10-2?.pkl')); assert len(fs) == 4, (tag, len(fs))
    return pd.concat([pd.read_pickle(f) for f in fs], ignore_index=True)
def ev(q, gana, L):
    c = (q * L).sum(); return float((q * (gana - L)).sum() / c) if c > 0 else float('nan')
def evalua(R, var='BASE', v='v3d', verbose=True):
    q = R[f'{v}_{var}_f_q'].values; tf = R[f'{v}_{var}_f_tf'].values; sim = q >= FLOOR; rf = R.real_fill.values == 1
    aj = R.real_ajenoL.fillna(False).astype(bool).values
    tp, fp, fn = sim & rf, sim & ~rf, ~sim & rf
    out = dict(n_ord=len(R), real=int(rf.sum()), real_ajeno=int((rf & aj).sum()), real_propio=int((rf & ~aj).sum()), sim=int(sim.sum()), TP=int(tp.sum()), FP=int(fp.sum()), FN=int(fn.sum()),
               precision=float(tp.sum() / max(sim.sum(), 1)), recall=float(tp.sum() / max(rf.sum(), 1)), recall_ajeno=float((tp & aj).sum() / max((rf & aj).sum(), 1)), recall_propio=float((tp & ~aj).sum() / max((rf & ~aj).sum(), 1)),
               TP_ajeno=int((tp & aj).sum()), TP_propio=int((tp & ~aj).sum()), FN_ajeno=int((fn & aj).sum()), FN_propio=int((fn & ~aj).sum()))
    d = (tf - R.real_tm3.values)[tp & np.isfinite(R.real_tm3.values)]
    out['tp_con_tm3'] = int(len(d)); out['pct_50ms'] = float((np.abs(d) <= 50).mean()) if len(d) else float('nan'); out['mediana_dt_ms'] = float(np.median(d)) if len(d) else float('nan')
    out['p10_p90_dt'] = [float(np.percentile(d, 10)), float(np.percentile(d, 90))] if len(d) else None
    L = R.L.values; g = R.gana.values; qr = R.real_q.values
    dtall = tf - R.real_tm3.values; tpe = tp & np.isfinite(dtall) & (np.abs(np.where(np.isfinite(dtall), dtall, 1e12)) <= 50)
    out['evento_50ms'] = dict(TP=int(tpe.sum()), precision=float(tpe.sum() / max(sim.sum(), 1)), recall=float(tpe.sum() / max(rf.sum(), 1)), recall_ajeno=float((tpe & aj).sum() / max((rf & aj).sum(), 1)), recall_propio=float((tpe & ~aj).sum() / max((rf & ~aj).sum(), 1)), TP_ajeno=int((tpe & aj).sum()), TP_propio=int((tpe & ~aj).sum()))
    sc = R.sin_cancel.values == 1
    out['pct_50ms_por_sin_cancel'] = dict(sin_cancel=dict(n=int((tp & sc).sum()), pct=float((tpe & sc).sum() / max((tp & sc).sum(), 1))), con_cancel=dict(n=int((tp & ~sc).sum()), pct=float((tpe & ~sc).sum() / max((tp & ~sc).sum(), 1))))
    out['EV_TP_motor'] = ev(q[tp], g[tp], L[tp]); out['EV_TP_real'] = ev(qr[tp], g[tp], L[tp]); out['EV_FP_motor'] = ev(q[fp], g[fp], L[fp]); out['EV_FN_real'] = ev(qr[fn], g[fn], L[fn]); out['EV_real_total'] = ev(qr[rf], g[rf], L[rf])
    out['EV_motor_total'] = ev(q[sim], g[sim], L[sim]); out['pnl_FP_motor'] = float((q[fp] * (g[fp] - L[fp])).sum()); out['pnl_FN_real'] = float((qr[fn] * (g[fn] - L[fn])).sum()); out['pnl_TP_motor'] = float((q[tp] * (g[tp] - L[tp])).sum()); out['pnl_TP_real'] = float((qr[tp] * (g[tp] - L[tp])).sum())
    # unidad = (dia, k) = mercado-lado
    U = R.assign(sim=sim, rf=rf, aj=aj, q=q, qr=qr).groupby(['dia', 'k']).agg(sim=('sim', 'max'), rf=('rf', 'max')).reset_index()
    out['unidades'] = dict(n=len(U), real=int(U.rf.sum()), sim=int(U.sim.sum()), TP=int((U.sim & U.rf).sum()), precision=float((U.sim & U.rf).sum() / max(U.sim.sum(), 1)), recall=float((U.sim & U.rf).sum() / max(U.rf.sum(), 1)))
    # causas FN (jerarquia)
    F = R[fn].copy(); ta = F.t_arr.values; te = F.t_end.values; rt = F.real_tm3.values; mot = F[f'{v}_{var}_mot'].values
    c = np.full(len(F), '', object); aj_f = F.real_ajenoL.fillna(False).astype(bool).values
    def asg(m, name):
        mm = m & (c == ''); c[mm] = name
    asg(~aj_f, '1_propio_solo(sin print ajeno <=L en el tx)'); asg(~np.isfinite(rt), '2_sin_tm3_real')
    asg(rt < ta, '3_relleno_real_antes_de_llegada_sim'); asg(rt > te, '4_relleno_real_tras_cancel_sim')
    asg(mot != 'ok', '5_libro_a_llegada(' + 'taker/sin_libro)'); asg(F.n_pr.values == 0, '6_sin_prints_en_ventana')
    asg((F.sz_pr_eqL.values == 0) & (F.n_pr_bajo.values == 0), '7_prints_solo_por_encima(no<=L)')
    asg(F.n_pr.values > 0, '8_cola_no_agotada(prints<=L existen)'); asg(c == '', '9_otro')
    out['FN_causas'] = {k: int(v_) for k, v_ in pd.Series(c).value_counts().items()}
    out['FN_causas_EV'] = {k: dict(n=int((c == k).sum()), pnl=float((F.real_q.values * (F.gana.values - F.L.values))[c == k].sum()), coste=float((F.real_q.values * F.L.values)[c == k].sum())) for k in sorted(set(c))}
    if verbose: print(json.dumps(out, indent=1, default=float))
    return out, F.assign(causa=c)
if __name__ == '__main__':
    R = carga(sys.argv[1]); evalua(R, sys.argv[2] if len(sys.argv) > 2 else 'BASE')
