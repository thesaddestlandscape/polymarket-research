#!/usr/bin/env python3
"""qc2_posthoc_rtt_relleno.py -- POST-HOC descriptivo (escrito DESPUES de ver QC2_delta_propio.json; no preregistrado, no cambia ningun veredicto).
Pregunta: la ida y vuelta del DELETE (rtt = t_fuera - t_cancel_int) es exogena o la ALARGA el propio relleno (causalidad inversa)? Motivo: los 7 TP con
x > 111 ms tienen rtt de 1.600-1.672 ms, muy por encima del p95 (175 ms). Mide la distribucion de rtt por grupo (sin relleno real / relleno real antes
de la intencion de cancelar / despues) y, para rtt >= 1.000 ms, los eventos del ledger de esa orden. SOLO LECTURA. Misma muestra que Q-C/Q-C2.
Uso: cd etapa0 && (ulimit -v 3000000; nice -n 19 ionice -c3 /usr/bin/python3 -I qc2_posthoc_rtt_relleno.py) -> QC2_posthoc_rtt_relleno.json"""
import os, sys, json, collections, datetime as dt
import numpy as np, pandas as pd
E = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, E)
import qc_brecha_nivel_mix as Q
DL = '/root/polymarket-research-datalogs/'; H = Q.H
EV = ('cancel_ya_terminal', 'cancel_ya_terminal_ack', 'relleno_tardio', 'gemelo_relleno', 'cancel_no_confirmada', 'get_order_error', 'get_order_pendiente_indexacion', 'lectura')


def main():
    R = Q.carga(); O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', usecols=['oid', 't_fuera']).set_index('oid'); R['t_fuera_s'] = R.oid.map(O.t_fuera)
    org, clat, evs = {}, {}, collections.defaultdict(collections.Counter)
    for l in open(DL + 'experimento_h47_B_ledger.jsonl'):
        try: d = json.loads(l)
        except Exception: continue
        t = d.get('tipo'); o = d.get('oid')
        if t == 'fuera_libro': org[o] = d.get('origen')
        elif t == 'cancel_lat': clat[o] = (d.get('ms'), d.get('ok'))
        if t in EV and o: evs[o][t] += 1
    R['origen'] = R.oid.map(org); R['rtt'] = np.round(1000.0 * (R.t_fuera_s - R.tcs), 3); valid = (R.origen == 'cancel') & R.tcs.notna()
    R['clat'] = R.oid.map(lambda o: clat.get(o, (np.nan, None))[0]).astype(float); R['clat_ok'] = R.oid.map(lambda o: clat.get(o, (None, None))[1])
    T1t = pd.read_pickle(H + 'out/T1_tx.pkl')[['order_hash', 'tx', 'token']].astype(str)
    OW = pd.concat([pd.read_pickle(H + f'out_v3/own_{d}.pkl') for d in Q.DIAS], ignore_index=True); OW['token_id'] = OW.token_id.astype(str); OW['tx'] = OW.tx.astype(str)
    MM = T1t.merge(OW[['tx', 'token_id', 'tm3']], left_on=['tx', 'token'], right_on=['tx', 'token_id'], how='left'); MM['tm3'] = MM.tm3.astype(float)
    R['xr_first'] = R.oid.map(MM.groupby('order_hash').tm3.min()) - R.tcs * 1000.0; R['xr_last'] = R.oid.map(MM.groupby('order_hash').tm3.max()) - R.tcs * 1000.0
    real = R.q_r > 1e-9; sim = R.q_s > 1e-9
    grp = np.where(~real, 'sin_relleno_real', np.where(R.xr_first.isna(), 'relleno_sin_sello', np.where(R.xr_last <= 0, 'relleno_antes_de_cancelar', 'relleno_despues_de_intencion')))
    R['grupo'] = grp
    def q(s): s = s.dropna(); return dict(n=int(len(s)), p50=round(float(s.median()), 1), p90=round(float(s.quantile(.9)), 1), ge_1000=int((s >= 1000).sum()), frac_ge_1000=round(float((s >= 1000).mean()), 4)) if len(s) else dict(n=0)
    out = dict(job='qc2_posthoc_rtt_relleno', aviso='POST-HOC descriptivo tras ver QC2_delta_propio.json; no preregistrado; no cambia veredictos',
               codigo_sha256=Q.sha_full(os.path.abspath(__file__)), generado_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    out['rtt_por_grupo'] = {g: q(R.rtt[valid & (R.grupo == g)]) for g in ('sin_relleno_real', 'relleno_antes_de_cancelar', 'relleno_despues_de_intencion', 'relleno_sin_sello')}
    L = R[valid & (R.rtt >= 1000)]
    out['rtt_ge_1000'] = dict(n=int(len(L)), con_relleno_real=int((L.q_r > 1e-9).sum()), con_relleno_sim=int((L.q_s > 1e-9).sum()),
                              rtt_p10_p50_p90=[round(float(L.rtt.quantile(x)), 1) for x in (.1, .5, .9)],
                              cancel_lat_ms_p10_p50_p90=[round(float(L.clat.quantile(x)), 1) for x in (.1, .5, .9)], cancel_lat_ok=dict(collections.Counter(map(str, L.clat_ok))),
                              grupos=dict(collections.Counter(L.grupo)), eventos_ledger=dict(sum((evs[o] for o in L.oid), collections.Counter())),
                              ordenes_con_algun_evento=int(sum(1 for o in L.oid if evs[o])))
    S = R[valid & (R.rtt < 1000)]
    out['rtt_lt_1000_eventos_ledger'] = dict(n=int(len(S)), eventos=dict(sum((evs[o] for o in S.oid), collections.Counter())), ordenes_con_algun_evento=int(sum(1 for o in S.oid if evs[o])))
    out['relleno_real_por_rtt'] = {b: dict(n=int(m.sum()), con_relleno_real=int((m & real).sum()), frac=round(float((m & real).sum() / max(int(m.sum()), 1)), 4))
                                   for b, m in (('rtt_lt_100', valid & (R.rtt < 100)), ('rtt_100_1000', valid & (R.rtt >= 100) & (R.rtt < 1000)), ('rtt_ge_1000', valid & (R.rtt >= 1000)))}
    aff = sim & valid
    out['sim_afectables_por_rtt'] = {c: dict(n=int((aff & (R.cls == c)).sum()), rtt_ge_1000=int((aff & (R.cls == c) & (R.rtt >= 1000)).sum()),
                                             rtt_p50_si_lt_1000=round(float(R.rtt[aff & (R.cls == c) & (R.rtt < 1000)].median()), 1) if (aff & (R.cls == c) & (R.rtt < 1000)).any() else None)
                                     for c in ('TP', 'FP')}
    json.dump(out, open(E + 'QC2_posthoc_rtt_relleno.json', 'w'), indent=1, default=str)
    print(json.dumps(out, default=str))


if __name__ == '__main__':
    main()
