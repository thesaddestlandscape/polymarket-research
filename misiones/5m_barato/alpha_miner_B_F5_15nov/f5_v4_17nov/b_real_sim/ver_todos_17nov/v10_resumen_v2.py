#!/usr/bin/env python3
"""v10_resumen_v2.py (18-Nov) -- metricas del PREREG_VER_TODOS_v2_18nov (sha b3374be3...) sobre out_v2/V2_*.pkl. Solo calculo. -> v10_resumen_v2.json"""
import glob, json, os, sys, hashlib, numpy as np, pandas as pd
H = os.path.dirname(os.path.abspath(__file__)) + '/'; FLOOR = 1e-3
assert hashlib.sha256(open(H + 'PREREG_VER_TODOS_v2_18nov.md', 'rb').read()).hexdigest().startswith('b3374be38c2f12ce')
TOK = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', usecols=['oid', 'tok'], dtype={'tok': str}).set_index('oid').tok
CL = pd.read_pickle(H + 'tomador_202.pkl')[['oid', 'causa']].set_index('oid').causa.fillna('').str.split('(').str[0]
DIAS = ['2026-10-20', '2026-10-21', '2026-10-22', '2026-10-23']


def load(tag):
    fs = sorted(glob.glob(H + f'out_v2/{tag}_2026-10-2?.pkl'))
    if len(fs) != 4: return None
    R = pd.concat([pd.read_pickle(f) for f in fs], ignore_index=True); R['tok'] = R.oid.map(TOK); R['cl'] = R.oid.map(CL); return R


def ev(R, q, m, first=True):
    """EV por EUR y por unidad; first=1.er relleno por token-lado (orden mas temprana del conjunto)"""
    S = R[m].assign(_q=q[m])
    if first: S = S.sort_values('t_arr').drop_duplicates('tok')
    S = S[S._q > 0]
    if len(S) == 0: return dict(n=0)
    g = S.gana.astype(float); c = S._q * S.L; p = S._q * (g - S.L)
    return dict(n=int(len(S)), ev_eur=round(float(p.sum() / c.sum()), 4), ev_unit=round(float(((g - S.L) / S.L).mean()), 4), pnl=round(float(p.sum()), 2), coste=round(float(c.sum()), 2))


def clasif(R, v):
    q = R[f'{v}_f_q'].fillna(0).values; s = q >= FLOOR; rf = R.real_fill.values == 1; qr = R.real_q.values
    tp = s & rf & (q >= 0.5 * qr); tpp = s & rf & ~tp; fp = s & ~rf; fn = rf & ~tp
    return q, s, rf, tp, tpp, fp, fn


def metr(R, v, ref='COLAv'):
    q, s, rf, tp, tpp, fp, fn = clasif(R, v); qr = R.real_q.values
    _, _, _, tp0, _, fp0, _ = clasif(R, ref)
    tf = R[f'{v}_f_tf'].fillna(-1).values; rt = R.real_tm3.values
    near = tp & np.isfinite(rt) & (np.abs(tf - rt) <= 50); dt0_new = tp & ~tp0 & np.isfinite(rt) & (tf == rt)
    o = dict(sim=int(s.sum()), TP=int(tp.sum()), TP_parcial=int(tpp.sum()), FP=int(fp.sum()), FN=int(fn.sum()), prec=round(tp.sum() / max(s.sum(), 1), 3), rec=round(tp.sum() / rf.sum(), 3),
             rec_q=round(float(np.minimum(np.where(s, q, 0), qr)[rf].sum() / qr[rf].sum()), 3), TP_50ms=int(near.sum()), nuevos_dt0=int(dt0_new.sum()),
             dTP=int(tp.sum() - tp0.sum()), dFP=int(fp.sum() - fp0.sum()))
    o['neto'] = o['dTP'] - o['dFP']; o['TP_ganados'] = int((tp & ~tp0).sum()); o['TP_perdidos'] = int((tp0 & ~tp).sum())
    dd = {}
    for d in DIAS:
        m = R.dia.values == d; dd[d] = dict(TP=int(tp[m].sum()), FP=int(fp[m].sum()), dTP=int(tp[m].sum() - tp0[m].sum()), dFP=int(fp[m].sum() - fp0[m].sum()))
        dd[d]['neto'] = dd[d]['dTP'] - dd[d]['dFP']
    o['por_dia'] = dd; o['lodo_neto'] = {d: o['neto'] - dd[d]['neto'] for d in DIAS}
    o['EV_TP_motor'] = ev(R, q, tp); o['EV_TP_real'] = ev(R, qr, tp); o['EV_FP_motor'] = ev(R, q, fp); o['EV_FN_real'] = ev(R, qr, fn)
    o['nuevos_por_clase'] = pd.Series(R.cl.values[tp & ~tp0]).value_counts().to_dict()
    return o


def resumen(tag):
    R = load(tag)
    if R is None: return None
    out = dict(n_ordenes=len(R), n_real=int(R.real_fill.sum()), EV_real_todos=ev(R, R.real_q.values, R.real_fill.values == 1, first=False), EV_real_1er=ev(R, R.real_q.values, R.real_fill.values == 1))
    VS = ['BASE', 'COLA', 'COLAv', 'DEMe_COLAv', 'DEMt_COLAv', 'DEMt_COLAv_p30', 'DEMt_COLAv_m30', 'L2Q', 'L2Q20', 'L2Q_opt', 'L2Q_p30', 'L2Q_m30'] + [f'{b}_cap{c}' for b in ('BASE', 'COLAv') for c in (605, 2675)]
    out['var'] = {v: metr(R, v) for v in VS}
    rn = [metr(R, f'DEMt_COLAv_rnd{s}') for s in range(20)]
    out['DEMt_rnd'] = dict(dTP_max=max(x['dTP'] for x in rn), dTP_p95=float(np.percentile([x['dTP'] for x in rn], 95)), neto_max=max(x['neto'] for x in rn), neto_p95=float(np.percentile([x['neto'] for x in rn], 95)))
    out['nsint'] = {v: int(R[f'{v}_nsint'].fillna(0).sum()) for v in ('DEMe_COLAv', 'DEMt_COLAv', 'DEMt_COLAv_p30', 'DEMt_COLAv_m30')}
    # COLA (constante) vs COLAv: rescates con dt=0 (defecto 2c)
    _, _, _, tpc, _, _, _ = clasif(R, 'COLA'); _, _, _, tpv, _, _, _ = clasif(R, 'COLAv'); _, _, _, tpb, _, _, _ = clasif(R, 'BASE')
    tfc = R.COLA_f_tf.fillna(-1).values; rt = R.real_tm3.values
    out['COLA_vs_COLAv'] = dict(COLA_no_COLAv=int((tpc & ~tpv).sum()), COLA_no_COLAv_dt0=int((tpc & ~tpv & (tfc == rt)).sum()), COLAv_no_BASE=int((tpv & ~tpb).sum()), BASE_no_COLAv=int((tpb & ~tpv).sum()))
    # L2: cobertura y metricas solo en ordenes con L2
    m2 = R.l2.fillna(0).values == 1; R2 = R[m2].reset_index(drop=True)
    out['L2_cob'] = dict(ordenes=int(m2.sum()), reales=int(R.real_fill.values[m2].sum()), alta_hallada=float(R2.l2_found_add.mean()), ahead0_p50=float(R2.l2_ahead0.median()), filas_p50=float(R2.l2_nrows.median()))
    out['L2_sub'] = {v: {k_: metr(R2, v)[k_] for k_ in ('TP', 'FP', 'dTP', 'dFP', 'neto', 'por_dia', 'nuevos_por_clase', 'TP_perdidos', 'TP_ganados')} for v in ('L2Q', 'L2Q20', 'L2Q_opt', 'L2Q_p30', 'L2Q_m30')}
    # FN por clase (C8: no identificable ex ante), EV real 1.er relleno
    fnc = {}
    for v in ('BASE', 'COLAv'):
        _, _, _, tp, _, _, fn = clasif(R, v); qr = R.real_q.values
        fnc[v] = {c: dict(ev(R, qr, fn & (R.cl.values == c))) for c in sorted(set(R.cl.values[fn]) - {np.nan}) if isinstance(c, str)}
        fnc[v]['TODOS'] = ev(R, qr, fn); fnc[v]['TODOS_por_orden'] = ev(R, qr, fn, first=False)
    out['FN_por_clase'] = fnc
    # C7: subconjunto sin sinev/amb
    m7 = (R.n_amb_sinev.fillna(0).values == 0) & ~R.real_rama.isin(['amb', 'sinev']).values; R7 = R[m7].reset_index(drop=True)
    out['C7'] = dict(n=int(m7.sum()), reales=int(R7.real_fill.sum()), var={v: {k_: metr(R7, v)[k_] for k_ in ('TP', 'FP', 'rec', 'prec', 'dTP', 'dFP', 'neto')} for v in ('BASE', 'COLAv', 'L2Q', 'DEMt_COLAv')})
    return out


def veredicto(o, prim, plac, rnd=None, dias=DIAS):
    v = o['var'][prim]; pm_tp = max(o['var'][p]['dTP'] for p in plac); pm_n = max(o['var'][p]['neto'] for p in plac)
    if rnd: pm_tp = max(pm_tp, rnd['dTP_max']); pm_n = max(pm_n, rnd['neto_max'])
    dpos = sum(v['por_dia'][d]['neto'] > 0 for d in dias); lodo = all(x > 0 for x in v['lodo_neto'].values())
    c = dict(dTP_ge5=v['dTP'] >= 5, dFP_le_tercio=v['dFP'] <= v['dTP'] / 3, neto_pos=v['neto'] > 0, plac_tp=pm_tp <= v['dTP'] / 3, plac_neto=pm_n <= max(v['neto'], 0) / 3, dt0=v['nuevos_dt0'] == 0,
             dias=dpos >= (3 if len(dias) == 4 else 2), lodo=lodo)
    st = 'ACEPTA' if all(c.values()) else ('REFUTA' if (v['dTP'] <= pm_tp or v['neto'] <= 0) else 'INCONCLUSO')
    return dict(estado=st, criterios=c, placebo_max_dTP=pm_tp, placebo_max_neto=pm_n, dias_neto_pos=dpos)


if __name__ == '__main__':
    OUT = {}
    for tag in sorted({os.path.basename(f).rsplit('_', 1)[0] for f in glob.glob(H + 'out_v2/V2_*_2026-10-2?.pkl')}):
        o = resumen(tag)
        if o is None: continue
        o['VEREDICTO_DEMt'] = veredicto(o, 'DEMt_COLAv', ['DEMt_COLAv_p30', 'DEMt_COLAv_m30'], o['DEMt_rnd'])
        o['VEREDICTO_L2Q'] = veredicto(o, 'L2Q', ['L2Q_p30', 'L2Q_m30'], dias=DIAS[:3])
        OUT[tag] = o
        print('==', tag, 'reales', o['n_real'], 'EV real 1er', o['EV_real_1er'])
        for v, m in o['var'].items():
            print(f"  {v:16s} sim {m['sim']:3d} TP {m['TP']:3d} (+parc {m['TP_parcial']}) FP {m['FP']:3d} rec {m['rec']:.3f} recq {m['rec_q']:.3f} dTP {m['dTP']:+d} dFP {m['dFP']:+d} neto {m['neto']:+d} dt0 {m['nuevos_dt0']} dia {[m['por_dia'][d]['neto'] for d in DIAS]} EVtp {m['EV_TP_real'].get('ev_eur')} EVfn {m['EV_FN_real'].get('ev_eur')}")
        print('  rnd', o['DEMt_rnd'], 'nsint', o['nsint'], 'COLA_vs_COLAv', o['COLA_vs_COLAv'])
        print('  L2', o['L2_cob'], {v: (x['dTP'], x['dFP'], x['neto']) for v, x in o['L2_sub'].items()})
        print('  VER DEMt', o['VEREDICTO_DEMt']['estado'], 'VER L2Q', o['VEREDICTO_L2Q']['estado'], o['VEREDICTO_L2Q']['criterios'])
    json.dump(OUT, open(H + 'v10_resumen_v2.json', 'w'), indent=1, default=str)
