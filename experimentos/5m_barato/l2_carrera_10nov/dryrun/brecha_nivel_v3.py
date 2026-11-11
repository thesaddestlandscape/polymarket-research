#!/usr/bin/env python3
"""brecha_nivel_v3.py -- DIAGNOSTICO de la brecha de NIVEL de EV motor v3 (sim -0,222) vs B real (-0,061) en las 3.796 ordenes reales de B (20-23 Oct, ledger), y calibracion de composicion con validacion cruzada por dia.
SOLO LECTURA, 0 ordenes, no edita nada congelado. Entradas: verif_real/out_v3/V3_<D>.pkl (v3d_BASE_f_q = rellenos simulados con sello v3 + dedupe; real_q = acciones realmente casadas por order_hash; gana = desenlace oficial),
verif_real/out/T1_tx.pkl (estructura on-chain del primer tx de cada relleno real: n_mk = makers del tx, solo-nuestra = n_mk == 1). Convenciones del motor: coste = q*L; pnl = q*(gana-L) + q*0,2*0,07*L*(1-L).
Descomposicion ESCALONADA del nivel (cada paso cambia UNA cosa):
   S0 EV_sim(todos los rellenos simulados)  -> S1 quitar FP (rellenos simulados sin relleno real) -> S2 sustituir sim q por real q en las TP (efecto cantidad/parcial) -> S3 anadir FN (relleno real no simulado) = EV_real.
Clases: TP (sim>0 y real>0), FP (sim>0, real=0), FN (sim=0, real>0), por orden. FN se parte en 'solo-nuestra' (tx con un unico maker = nuestra orden: sin print ajeno en el feed) y 'con otros makers'.
CALIBRACION (calibra_composicion, funcion pura con test): EV_hat = w*EV_sim_TP + (1-w)*e_FN con w = coste_sim / (coste_sim + rho*coste_sim), rho = coste_FN_real / coste_TP_sim, e_FN = EV de los FN; parametros estimados en dias de calibracion y
aplicados a otro dia (LODO: leave-one-day-out sobre 4 dias = 4 observaciones). Es un diagnostico de la VALIDACION (la cinta de validacion excluye NUESTROS propios prints), no un factor para multiplicar el EV del dry-run (ver informe)."""
import os, sys, glob, json
import numpy as np, pandas as pd
H = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/verif_real/'; OUT = os.path.dirname(os.path.abspath(__file__)) + '/out_replay/'; os.makedirs(OUT, exist_ok=True)
REB = 0.2 * 0.07; rng = np.random.default_rng(20261111); B = 10000


def pnl_of(q, L, g): return q * (g - L) + q * REB * L * (1 - L)


def calibra_composicion(cost_sim, ev_sim, cost_fn, ev_fn, cost_tp_sim=None):
    """Mezcla de composicion: el relleno real = (rellenos que el motor ve) + (rellenos que no ve, FN). w = peso en coste de lo visto. cost_sim = coste de los rellenos simulados que son reales (TP) en la muestra de calibracion
    por unidad: se pasa rho = cost_fn/cost_tp_sim ya normalizado. Devuelve EV_hat = (ev_sim + rho*ev_fn)/(1+rho)."""
    rho = cost_fn / (cost_tp_sim if cost_tp_sim is not None else cost_sim)
    return (ev_sim + rho * ev_fn) / (1.0 + rho)


def carga():
    O = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}, usecols=['oid', 't_cancel_int'])
    R = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out_v3/V3_*.pkl'))], ignore_index=True); R = R[R['cov'] == 'ok'].copy(); R = R.merge(O.rename(columns={'t_cancel_int': 'tcs'}), on='oid', how='left')
    T = pd.read_pickle(H + 'out/T1_tx.pkl'); nm = T.groupby('order_hash').n_mk.min()
    R['q_s'] = R.v3d_BASE_f_q.astype(float); R['q_r'] = R.real_q.astype(float); R['n_mk'] = R.oid.map(nm)
    R['cls'] = np.where((R.q_s > 1e-9) & (R.q_r > 1e-9), 'TP', np.where(R.q_s > 1e-9, 'FP', np.where(R.q_r > 1e-9, 'FN', 'TN')))
    R['c_s'] = R.q_s * R.L; R['c_r'] = R.q_r * R.L; R['p_s'] = pnl_of(R.q_s, R.L, R.gana); R['p_r'] = pnl_of(R.q_r, R.L, R.gana); R['cl'] = R.dia + '_' + (R.t_ini // 300000).astype(str)
    return R


def ev(num, den): return float(num / den) if den > 0 else np.nan


def boot_ev(R, num_col, den_col, mask=None):
    d = R if mask is None else R[mask]; g = d.groupby('cl')[[num_col, den_col]].sum().values
    if len(g) == 0: return (np.nan, np.nan)
    ix = rng.integers(0, len(g), (B, len(g))); b = g[:, 0][ix].sum(1) / np.maximum(g[:, 1][ix].sum(1), 1e-9); return (round(float(np.quantile(b, .05)), 3), round(float(np.quantile(b, .95)), 3))


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


def main():
    R = carga(); print('ordenes validas', len(R), 'dias', sorted(R.dia.unique()))
    tab = []
    for c in ['TP', 'FP', 'FN']:
        d = R[R.cls == c]; tab.append(dict(clase=c, n=len(d), cost_sim=round(d.c_s.sum(), 1), cost_real=round(d.c_r.sum(), 1), ev_sim=round(ev(d.p_s.sum(), d.c_s.sum()), 4) if d.c_s.sum() > 0 else None, ev_real=round(ev(d.p_r.sum(), d.c_r.sum()), 4) if d.c_r.sum() > 0 else None,
                                           ic90_real_cl=boot_ev(R, 'p_r', 'c_r', R.cls == c) if c != 'FP' else None, acierto_real=round(float((d.gana[d.q_r > 0] > 0.5).mean()), 3) if (d.q_r > 0).any() else None))
    print(pd.DataFrame(tab).to_string(index=False))
    fn = R[R.cls == 'FN']; fns = fn[fn.n_mk == 1]; fno = fn[fn.n_mk > 1]
    print('FN partido: solo-nuestra n=%d (%.1f %%) ev_real %.4f cost %.1f | con otros makers n=%d ev_real %.4f cost %.1f' % (len(fns), 100 * len(fns) / max(len(fn), 1), ev(fns.p_r.sum(), fns.c_r.sum()), fns.c_r.sum(), len(fno), ev(fno.p_r.sum(), fno.c_r.sum()), fno.c_r.sum()))
    E = escalones(R); print('ESCALONES', json.dumps(E))
    TD = tabla_delta(R); print('--- fin de segmento = envio DELETE + delta (anula rellenos simulados posteriores)'); print(TD.to_string(index=False))
    ics = dict(sim=boot_ev(R, 'p_s', 'c_s'), real=boot_ev(R, 'p_r', 'c_r')); print('IC90 por cluster dia-ventana5min: sim', ics['sim'], 'real', ics['real'])
    # --- calibracion de composicion con LODO
    dias = sorted(R.dia.unique()); rows = []
    for d in dias:
        cal = R[R.dia != d]; val = R[R.dia == d]
        tp = cal[cal.cls == 'TP']; fnc = cal[cal.cls == 'FN']; rho = fnc.c_r.sum() / max(tp.c_s.sum(), 1e-9); e_fn = ev(fnc.p_r.sum(), fnc.c_r.sum())
        ev_sim_val = ev(val.p_s.sum(), val.c_s.sum()); ev_sim_tp_val = ev(val[val.cls == 'TP'].p_s.sum(), val[val.cls == 'TP'].c_s.sum())
        hat = calibra_composicion(None, ev_sim_val, fnc.c_r.sum(), e_fn, cost_tp_sim=tp.c_s.sum()); real = ev(val.p_r.sum(), val.c_r.sum())
        rows.append(dict(dia_valida=d, n_val=len(val), ev_sim=round(ev_sim_val, 4), ev_hat=round(hat, 4), ev_real=round(real, 4), err_sim=round(ev_sim_val - real, 4), err_hat=round(hat - real, 4), rho=round(rho, 3), e_fn=round(e_fn, 4)))
    L = pd.DataFrame(rows); print(L.to_string(index=False)); print('error absoluto medio: sim %.4f  calibrado %.4f   (LODO, 4 dias; la calibracion usa 3 dias para estimar rho y e_FN)' % (L.err_sim.abs().mean(), L.err_hat.abs().mean()))
    tp_all = R[R.cls == 'TP']; fn_all = R[R.cls == 'FN']; rho_all = fn_all.c_r.sum() / max(tp_all.c_s.sum(), 1e-9); e_all = ev(fn_all.p_r.sum(), fn_all.c_r.sum()); hat_all = calibra_composicion(None, ev(R.p_s.sum(), R.c_s.sum()), fn_all.c_r.sum(), e_all, cost_tp_sim=tp_all.c_s.sum())
    cierra = (hat_all - E['S0_sim_todos']) / (E['S3_real_total'] - E['S0_sim_todos']) if E['S3_real_total'] != E['S0_sim_todos'] else np.nan
    print('EN MUESTRA (circular, no es validacion): EV_hat %.4f vs real %.4f, cierra %.0f %% de la brecha; LODO cierra %.0f %%' % (hat_all, E['S3_real_total'], 100 * cierra, 100 * (1 - L.err_hat.abs().mean() / max(L.err_sim.abs().mean(), 1e-9))))
    json.dump(dict(tabla_delta=TD.to_dict('records'), tabla_clases=tab, escalones=E, ic90=ics, lodo=L.to_dict('records'), en_muestra=dict(ev_hat=hat_all, rho=rho_all, e_fn=e_all)), open(OUT + 'brecha_nivel_v3.json', 'w'), indent=1, default=str)


if __name__ == '__main__': main()
