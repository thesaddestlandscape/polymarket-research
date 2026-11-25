#!/usr/bin/env python3
"""qc2_v2_sinpolvo.py -- Q-C2 v2 DESCRIPTIVA (16-Nov), tras REVISION_ESTADISTICA_QC2_16nov.md. SOLO LECTURA, 0 ordenes, CPU ~segundos.
Version NUEVA de qc2_delta_propio.py (sellado; NO se edita): misma logica (copiada; delta_i = 1000*(t_fuera - t_cancel_int) - A, A=24) con UN cambio de
definicion y adiciones descriptivas.
 (a) UMBRAL DE RELLENO SIMULADO q >= 1e-3 (antes q > 1e-9). 2 de los 82 rellenos simulados (23-Oct eth x=40 q=1,9e-7; sol x=35 q=2,7e-7) son POLVO de coma
     flotante (cola 'ahead' en float32, print en float64: 6,19999981 vs 6,2 -> 'relleno' de 1,9e-7 con la cola agotada EXACTAMENTE = no hay relleno). Se ponen a
     q_s = 0 (cls, c_s, p_s recalculados) antes de todo. Antes se reproduce con el umbral viejo (brecha_nivel_v3 publicado, Q-C sin correccion y MIX, y V0 de QC2 v1)
     para demostrar que la unica diferencia son esas 2 filas.
 (b) nulo FORWARD: delta = rtt_j - A con rtt_j de ordenes SIN relleno real, condicionado a rtt_j >= x_i (las con relleno real tienen causalidad inversa).
 (c) sin TP con rtt >= 1 s; (d) solo lado FP (estadistico = FP anulados); (e) C1/C2 recalculados.
 (f) cierre como CURVA f(A), A = 0..40 ms paso 1 (+44,5), cota SUPERIOR A <= A_max (mayor A sin TP anulado) y SIN cota inferior (A no medido en 20-23 Oct).
Etiquetas v2: T1 'no informativa'; identificacion por orden 'NO VALIDADA' (el veredicto literal del s.6 se imprime aparte); se retira 'la carrera no necesita
correccion HI' (A_HI y A_LO no medidos el mismo dia; unica inferencia: A_HI(20-23 Oct) <= ~32 ms). Ninguna etiqueta autoriza operar en real.
EXPLORATORY/descriptivo: no sustituye ni reescribe nada sellado (ADDENDUM2, QC2_delta_propio.*).
Uso: cd etapa0 && (ulimit -v 3000000; nice -n 19 ionice -c3 /usr/bin/python3 -I qc2_v2_sinpolvo.py) -> QC2_v2_sinpolvo.json / .tsv"""
import os, sys, json, time, resource, collections, datetime as dt
import numpy as np, pandas as pd

E = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, E)
import qc_brecha_nivel_mix as Q

DL = '/root/polymarket-research-datalogs/'
H = Q.H
ADD2_F = E + 'ADDENDUM2_PREREG_REPLAY_BRECHA_B_16nov.md'; ADD2_SHA = 'd3ea71837424893b86cc76e78cc21e2a40fe494b946ca533e08915b7ff5145ec'
QC2V1_F = E + 'QC2_delta_propio.json'; QC2V1_SHA = '200031e441da001c917bbbab5be7f32c3776b8ac285de9cf1698977c78901c8c'
Q_UMBRAL = 1e-3
QMIX_F = E + 'qc_brecha_nivel_mix.py'; QMIX_SHA = 'e20db94244f404f367615bea44970eaac7fec420a8170c9e4dc7e44eba0a7818'
QMIX_OUT = E + 'QC_brecha_nivel_mix.json'
SHA_IN = {
    DL + 'calibracion_etiqueta/ordenes_b.csv': '7ebd392b44e7337c25b8ee9786030371dfdb714ff32313765746b36d7c49d3a5',
    DL + 'experimento_h47_B_ledger.jsonl': '32653e4f16a2e00586154ac0406888de44d4ded60ad2ecef0020aa314b26c2c9',
    H + 'out_v3/V3_2026-10-20.pkl': 'f96b13822ada0a2b5e96c0e553402fb3111b444615cb1c66dc323303c84b9e8d',
    H + 'out_v3/V3_2026-10-21.pkl': 'cd7e4dcbc962a4fb260eb7b3b2fadc78f1da662e1c82124859ee3644b3b26e2a',
    H + 'out_v3/V3_2026-10-22.pkl': '2918ce32b257278e5983523cf9810efd7582572d138fba10d165820e491dfa9b',
    H + 'out_v3/V3_2026-10-23.pkl': 'c904c16aa08f7aa31c76aa79ab005fee608cce81417a86493cf7de68aa1c3c55',
    H + 'out_v3/own_2026-10-20.pkl': 'b4b2d686a70a7f42e6733fc6e4a949d9576167b286d460f3cb778eaf56136ba7',
    H + 'out_v3/own_2026-10-21.pkl': '4759912356fae4a14cf2d1933ecc9aa14ef1460525aee031af26df0503c59f4e',
    H + 'out_v3/own_2026-10-22.pkl': 'ee7142c43b0526a1400146be74af642208bc0cdcc89f4fb58c60fa9bfc84bee5',
    H + 'out_v3/own_2026-10-23.pkl': '80214e77600e5e336a1089f083e12382b5377e7ce8bf3f39b5559e143ea2999b',
    H + 'out/T1_tx.pkl': 'fbf7e5caf5e6f6d803e9cb400858be33d104049a96b17a5e3192a0d26667a634',
    E + 'l_pool_vigente_13nov.json': '7d92a57c74f7541d77d17dcafa2ed9ec1288ddba3407072ed5264f38a5e69ddf',
    Q.REF_F: 'd995a069aea1a402b1e61a476c4f49ba375c2fa2788ebb9aa7079e5289dd75d0',
    E + 'QC_desc_tf_menos_tcs.json': '18e874068f7ff5c20db6ec1c0fd6a516a1e7da73a1fe77a3daa871af3c0d8176',
    QMIX_OUT: '1c83e558be5b9de4c0b1f70392da6724cb30eb0cad3a4431de57e681889e3166',
}
ADD3_SHA = {'2026-10-20': '806f6152e75ca80c75ae3bd386fa546c30dc4168ec6f5be3c2166aa9c5aaaa84', '2026-10-21': '61e5c166ab72461b4dd11746bbb6f628931d0eec7034f05c372de75b1f3725a1',
            '2026-10-22': '84e173029794ff21024af3ee13e2f166d0f053aac0bc51591d448cc51c9f5071', '2026-10-23': '705f1a5ab85d83b69a49ffb2c3faa437b173a7255dfd466fe7fc1c2348d4e277'}
A_ACK = 24.0; HI = 20.5; SEED = 20261116; BOOT = 10000; NPERM = 2000; NBT5 = 2000
X7 = [127, 364, 442, 465, 712, 723, 866]
A_CURVA = tuple(range(0, 41)) + (44.5,)
DIAS = Q.DIAS
rn = Q.rn


def ledger():
    org, clat, plat = {}, {}, {}
    for l in open(DL + 'experimento_h47_B_ledger.jsonl'):
        try: d = json.loads(l)
        except Exception: continue
        t = d.get('tipo')
        if t == 'fuera_libro': org[d['oid']] = d.get('origen')
        elif t == 'cancel_lat': clat[d['oid']] = float(d['ms']) if d.get('ms') is not None else np.nan
        elif t == 'post_lat': plat[d['oid']] = float(d['ms']) if d.get('ms') is not None else np.nan
    return org, clat, plat


def ic(a, k=4):
    a = np.asarray(a, float); a = a[np.isfinite(a)]
    return [round(float(np.quantile(a, .05)), k), round(float(np.quantile(a, .95)), k)] if len(a) else None


def pesos(R, B=BOOT, seed=SEED, chunk=1000):
    """Mismos pesos multinomiales que Q.boot (misma semilla, mismos tamanos de bloque, clusters en el orden de groupby)."""
    n = R.cl.nunique(); rng = np.random.default_rng(seed)
    return np.vstack([rng.multinomial(n, np.full(n, 1.0 / n), size=min(chunk, B - i)) for i in range(0, B, chunk)])


def sumas(R, cols):
    M = pd.DataFrame(cols).groupby(R.cl.values).sum()
    return M.to_numpy(float), {c: i for i, c in enumerate(M.columns)}


def pb_cola(ps, k):
    dist = np.array([1.0])
    for p in ps: dist = np.convolve(dist, [1.0 - p, p])
    return float(dist[k:].sum())


def main():
    t0 = time.time(); fallos = []
    out = dict(job='qc2_v2_sinpolvo', measurement_id='BF5-REPLAY-COLOC-v1', etapa='Q-C2 v2 descriptiva (umbral q>=1e-3) sobre ADDENDUM2 s.2-8',
               etiqueta='EXPLORATORY (explicativo; 4 dias, una estrategia real; no decide ninguna palanca ni valida B)',
               addendum2_sha256=ADD2_SHA, codigo_sha256=Q.sha_full(os.path.abspath(__file__)),
               comando='cd ' + E + ' && (ulimit -v 3000000; nice -n 19 ionice -c3 /usr/bin/python3 -I qc2_v2_sinpolvo.py)',
               inicio_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    # ---------------- 0. sellos y entradas (Fail Loud)
    assert Q.sha_full(ADD2_F) == ADD2_SHA and open(E + 'ADDENDUM2_PREREG_REPLAY_BRECHA_B_16nov.sha256').read().split()[0] == ADD2_SHA, 'ADDENDUM2 alterado'
    for nm in ('PREREG_REPLAY_BRECHA_B_16nov', 'ADDENDUM1_PREREG_REPLAY_BRECHA_B_16nov'):
        s = open(Q.MIS + nm + '.sha256').read().split()[0]; assert Q.sha_full(Q.MIS + nm + '.md') == s, nm + ' alterado'; out[nm + '_sha256'] = s
    assert Q.sha_full(QC2V1_F) == QC2V1_SHA, 'QC2_delta_propio.json (v1) alterado'
    assert Q.sha_full(E + 'qc2_delta_propio.py') == open(E + 'QC2_delta_propio.sha256').read().split()[0], 'qc2_delta_propio.py (v1) alterado'
    V1 = json.load(open(QC2V1_F))
    assert Q.sha_full(QMIX_F) == QMIX_SHA, 'qc_brecha_nivel_mix.py cambio'
    assert Q.sha_full(Q.ORIG_F)[:16] == Q.ORIG_SHA16, 'brecha_nivel_v3.py cambio'
    cp = Q.verifica_copia(); assert all(cp.values()), ('copia literal NO identica', cp)
    for f, s in SHA_IN.items(): assert Q.sha_full(f) == s, 'entrada cambiada: ' + f
    out['entradas_sha256_ok'] = sorted(os.path.basename(f) for f in SHA_IN)
    P = json.load(open(E + 'l_pool_vigente_13nov.json'))['pool']
    v_all = [p['cancel_ex_menos_envio'] for p in P]; v_sb = [p['cancel_ex_menos_envio'] for p in P if p['coin'] != 'BTC']
    a_all = np.array([p['cancel_ack_menos_ex'] for p in P], float); a_sb = np.array([p['cancel_ack_menos_ex'] for p in P if p['coin'] != 'BTC'], float)
    A_sb = float(np.median(a_sb)); med_v = float(np.median(v_all)); med_va = float(np.median(np.array(v_all, float) + a_all))
    assert float(np.median(a_all)) == A_ACK and len(P) == 313 and len(a_sb) == 187, 'pool: A != 24 o tamano inesperado'
    assert (med_v, med_va) == (33.0, 57.0), ('V3: medianas del pool distintas de las declaradas', med_v, med_va)
    out['pool'] = dict(A_todas=A_ACK, A_sinBTC=A_sb, mediana_v=med_v, mediana_v_mas_A=med_va, A_p5_p95_todas=[float(np.percentile(a_all, 5)), float(np.percentile(a_all, 95))])
    # ---------------- 1. muestra (carga literal de Q-C) + campos del ledger
    R = Q.carga(); R0 = R.copy()     # R0 = muestra con el umbral viejo (q > 1e-9), solo para la reproduccion previa
    polvo = (R.q_s > 0) & (R.q_s < Q_UMBRAL)
    out['polvo'] = dict(umbral_nuevo=Q_UMBRAL, n_sim_umbral_viejo=int((R.q_s > 1e-9).sum()), n_polvo=int(polvo.sum()), n_q_real_menor_umbral=int(((R.q_r > 0) & (R.q_r < Q_UMBRAL)).sum()),
                        filas=[dict(oid=o[:14], dia=d_, coin=str(c_), L=float(l_), cola=float(co_), q_s=float(q_), tf=int(t_), tcs_ms=rn(tc_ * 1000.0, 1), x_ms=rn(t_ - tc_ * 1000.0, 1), q_real=float(qr_))
                               for o, d_, c_, l_, co_, q_, t_, tc_, qr_ in zip(R.oid[polvo], R.dia[polvo], R.coin[polvo], R.L[polvo], R.cola[polvo], R.q_s[polvo], R.v3d_BASE_f_tf[polvo], R.tcs[polvo], R.q_r[polvo])],
                        q_s_valores_distintos_menores_de_1=sorted(set(R.q_s[(R.q_s > 0) & (R.q_s < 1)].round(6).tolist())))
    R['q_s'] = R.q_s.where(~polvo, 0.0)
    R['cls'] = np.where((R.q_s > 1e-9) & (R.q_r > 1e-9), 'TP', np.where(R.q_s > 1e-9, 'FP', np.where(R.q_r > 1e-9, 'FN', 'TN')))
    R['c_s'] = R.q_s * R.L; R['p_s'] = Q.pnl_of(R.q_s, R.L, R.gana)
    O = pd.read_csv(DL + 'calibracion_etiqueta/ordenes_b.csv', usecols=['oid', 't_dec', 't_fuera', 't_cancel_int']); assert O.oid.is_unique
    O = O.set_index('oid'); R['t_dec_s'] = R.oid.map(O.t_dec); R['t_fuera_s'] = R.oid.map(O.t_fuera)
    assert bool(((R.tcs - R.oid.map(O.t_cancel_int)).abs().fillna(0) < 1e-9).all()), 'tcs de carga() distinto de ordenes_b'
    org, clat, plat = ledger(); R['origen'] = R.oid.map(org); R['cancel_lat_ms'] = R.oid.map(clat); R['post_lat_ms'] = R.oid.map(plat)
    R['rtt'] = np.round(1000.0 * (R.t_fuera_s - R.tcs), 3)
    valid = (R.origen == 'cancel') & R.tcs.notna() & R.t_fuera_s.notna()
    real = R.q_r > 1e-9; sim0 = R.q_s > 1e-9
    R['x'] = np.where(sim0 & R.tcs.notna(), R.v3d_BASE_f_tf.astype(float) - R.tcs * 1000.0, np.nan)
    out['muestra'] = dict(n_ordenes=int(len(R)), por_dia={d: int((R.dia == d).sum()) for d in DIAS}, monedas=sorted(R.coin.astype(str).unique().tolist()),
                          origen=dict(collections.Counter(R.origen.fillna('NA'))), delta_definida=int(valid.sum()), con_tcs_sin_delta=int((R.tcs.notna() & ~valid).sum()),
                          sin_tcs=int(R.tcs.isna().sum()), rellenos_sim=int(sim0.sum()), rellenos_real=int(real.sum()),
                          sim_afectables_con_delta=int((sim0 & valid).sum()), sim_con_tcs_sin_delta=int((sim0 & R.tcs.notna() & ~valid).sum()), sim_sin_tcs=int((sim0 & R.tcs.isna()).sum()),
                          rtt_ms=dict(n=int(valid.sum()), p5=rn(R.rtt[valid].quantile(.05), 1), p25=rn(R.rtt[valid].quantile(.25), 1), p50=rn(R.rtt[valid].median(), 1),
                                      p75=rn(R.rtt[valid].quantile(.75), 1), p95=rn(R.rtt[valid].quantile(.95), 1), min=rn(R.rtt[valid].min(), 1), max=rn(R.rtt[valid].max(), 1)))
    # ---------------- 2. reproduccion previa obligatoria (s.9): publicado brecha_nivel_v3 + Q-C (sin correccion, MIX)
    ref = json.load(open(Q.REF_F)); TD = Q.tabla_delta(R0).to_dict('records'); ES = Q.escalones(R0)
    rep1 = all(a == b for a, b in zip(TD, ref['tabla_delta'])) and len(TD) == len(ref['tabla_delta']) and ES == ref['escalones']
    QM = json.load(open(QMIX_OUT))['total']['filas']; dm = Q.delta_mix(R.oid, v_all)
    m_sc = Q.metricas(R0, Q.sim_con_delta(R0, 1e9)[0]); m_mx = Q.metricas(R0, Q.sim_con_delta(R0, dm)[0])
    rep2 = all(m_sc[k] == QM['sin_correccion'][k] for k in m_sc) and all(m_mx[k] == QM['MIX'][k] for k in m_mx)
    # V0 de QC2 v1 con el umbral viejo (misma muestra R0, delta = rtt - 24): debe igualar QC2_delta_propio.json
    dv0_old = (R.rtt - A_ACK).where(valid).fillna(1e9); m_v0_old = Q.metricas(R0, Q.sim_con_delta(R0, dv0_old)[0]); mv1 = V1['total']['filas']['V0_primaria']
    rep3 = all(m_v0_old[k] == mv1[k] for k in m_v0_old); rep4 = bool(V1['veredicto_s6']['cierre_V0'] == m_v0_old['cierra_brecha'])
    out['reproduccion_previa'] = dict(brecha_nivel_v3_publicado=bool(rep1), QC_sin_correccion_y_MIX=bool(rep2), QC2_v1_V0_umbral_viejo=bool(rep3 and rep4))
    out['V0_umbral_viejo_(QC2_v1)'] = m_v0_old
    rep1 = rep1 and rep3 and rep4
    if not (rep1 and rep2):
        out['estado'] = 'PARADO: no reproduce lo publicado (stop rule s.9; Fail Loud)'
        json.dump(out, open(E + 'QC2_v2_sinpolvo.json', 'w'), indent=1, default=str); print(json.dumps(out['reproduccion_previa'])); sys.exit(2)
    # D1: el segmento simulado termina en t_fuera
    tfv = R.v3d_BASE_f_tf.astype(float)[sim0]; tfu = R.t_fuera[sim0].astype(float)
    out['D1_tf_menor_o_igual_t_fuera'] = dict(n_sim=int(sim0.sum()), n_tf_mayor_que_t_fuera=int((tfv > tfu).sum()), max_tf_menos_t_fuera_ms=rn((tfv - tfu).max(), 1),
                                              nota='si 0: anular tf > tcs + (rtt - A) == cortar el segmento en t_fuera - A; x_i <= rtt_i por construccion')
    # ---------------- 3. clase (causal por t_dec; concurrente por tcs) con ADD3 COMPLETE (sha declarados)
    lab, est = {}, {}
    for d in DIAS:
        p = Q.MIS + f'exp1/cache/pob_add3_{d}.json'
        if not os.path.exists(p): est[d] = dict(estado='PENDIENTE_ADD3'); continue
        if Q.sha_full(p) != ADD3_SHA[d]: est[d] = dict(estado='ADD3_CAMBIO_TRAS_SELLAR'); fallos.append('ADD3 ' + d + ' cambio respecto al sha del ADDENDUM2'); continue
        j = json.load(open(p))
        if j.get('estado') != 'COMPLETE': est[d] = dict(estado='ADD3_' + str(j.get('estado'))); continue
        pf = j['C3_suelo_rx_menos_ex']['perfil_p5_10min']; lb = [Q.clase_p5(None if v is None else float(v)) for v in pf]; tt = collections.Counter(lb)
        vpc = j['C3_suelo_rx_menos_ex'].get('ventanas_por_clase', {}); okv = all(tt[k] == vpc.get(k, 0) for k in ('lo', 'hi', 'indet'))
        est[d] = dict(estado='COMPLETE', n_ventanas=len(pf), ventanas=dict(tt), reproduce_ventanas_por_clase=bool(okv))
        if len(pf) == 144 and okv: lab[d] = lb
        else: fallos.append(f'ADD3 {d}: perfil no reproduce ventanas_por_clase o no tiene 144 ventanas')
    d0 = R.dia.map(lambda s: int(pd.Timestamp(s, tz='UTC').timestamp()) * 1000).astype('int64')
    w = np.floor((R.t_dec_s * 1000.0 - 200 - d0) / 600000.0) - 1; wc = np.floor((R.tcs * 1000.0 - d0) / 600000.0)
    def lab_of(dd, ww):
        if dd not in lab: return 'pendiente_ADD3'
        if not np.isfinite(ww) or ww < 0 or ww >= len(lab[dd]): return 'indet'
        return lab[dd][int(ww)]
    R['clase'] = [lab_of(dd, ww) for dd, ww in zip(R.dia.values, w.values)]
    R['clase_conc'] = [lab_of(dd, ww) if np.isfinite(ww) else 'sin_tcs' for dd, ww in zip(R.dia.values, wc.values)]
    R['w_conc'] = wc
    hi = (R.clase == 'hi')
    con = R[(R.clase != 'pendiente_ADD3') & (R.clase_conc != 'sin_tcs')]
    out['clase'] = dict(estado_ADD3=est, dias_con_clase=sorted(lab), ordenes_por_clase=dict(collections.Counter(R.clase)),
                        discordancia_causal_vs_concurrente=dict(n=int(len(con)), discordantes=int((con.clase != con.clase_conc).sum())))
    # ---------------- 4. variantes (s.3)
    d_v0 = (R.rtt - A_ACK).where(valid)
    d_v1 = (R.rtt - A_sb).where(valid)
    rng1 = lambda o, n: np.random.default_rng([int(o, 16), SEED, 2]).integers(n)
    d_v1d = pd.Series([r - a_all[rng1(o, len(a_all))] if ok else np.nan for o, r, ok in zip(R.oid.values, R.rtt.values, valid.values)], index=R.index)
    d_v1ds = pd.Series([r - a_sb[rng1(o, len(a_sb))] if ok else np.nan for o, r, ok in zip(R.oid.values, R.rtt.values, valid.values)], index=R.index)
    d_v2 = (R.cancel_lat_ms - A_ACK).where(valid & R.cancel_lat_ms.notna())
    d_v3 = (R.rtt * med_v / med_va).where(valid)
    d_v4 = d_v0 - HI * hi.astype(float)
    VAR = collections.OrderedDict()
    VAR['sin_correccion'] = pd.Series(1e9, index=R.index); VAR['V0_primaria'] = d_v0; VAR['V1_sinBTC'] = d_v1
    VAR['V1d_acuse_sorteado_todas'] = d_v1d; VAR['V1d_acuse_sorteado_sinBTC'] = d_v1ds; VAR['V2_cancel_lat'] = d_v2; VAR['V3_proporcional'] = d_v3
    VAR['V4_cota_HI'] = d_v4; VAR['ref_MIX_QC'] = dm
    ANU = {}; QS = {}
    for k, dv in VAR.items():
        q, an = Q.sim_con_delta(R, dv.fillna(1e9)); QS[k] = q; ANU[k] = an
    # techos oraculo (s.4) y descomposicion solo-FP / solo-TP
    fp0 = sim0 & ~real
    QS['C1_quitar_12_FP'] = R.q_s.where(~fp0, 0.0)
    QS['C2_quitar_FP_alcanzables'] = R.q_s.where(~(fp0 & R.tcs.notna() & (R.x > 0)), 0.0)
    for k in ('V0_primaria', 'V4_cota_HI'):
        QS[k + '|soloFP'] = R.q_s.where(~(ANU[k] & ~real), 0.0); QS[k + '|soloTP'] = R.q_s.where(~(ANU[k] & real), 0.0)
    out['delta_por_orden'] = {k: dict(n=int(VAR[k].notna().sum()), p10=rn(VAR[k].quantile(.1), 1), p50=rn(VAR[k].median(), 1), p90=rn(VAR[k].quantile(.9), 1))
                              for k in VAR if k != 'sin_correccion'}
    out['V1_identica_a_V0'] = bool(A_sb == A_ACK)
    # ---------------- 5. total + IC90 por cierre (mismos pesos que Q-C)
    tot = {k: Q.metricas(R, q) for k, q in QS.items()}
    bt = Q.boot(R, QS)
    for k in tot:
        if k in bt: tot[k]['ic90_cierre'] = bt[k]
    Wt = pesos(R)
    cols = {'ps': R.p_s, 'cs': R.c_s, 'pr': R.p_r, 'cr': R.c_r, 'psTP': R.p_s.where(R.cls == 'TP', 0.0), 'csTP': R.c_s.where(R.cls == 'TP', 0.0),
            'prTP': R.p_r.where(R.cls == 'TP', 0.0), 'crTP': R.c_r.where(R.cls == 'TP', 0.0)}
    for k in ('V0_primaria', 'V4_cota_HI'): cols['p|' + k] = Q.pnl_of(QS[k], R.L, R.gana); cols['c|' + k] = QS[k] * R.L
    A_, ix = sumas(R, cols); S = Wt @ A_
    with np.errstate(divide='ignore', invalid='ignore'):
        s0 = S[:, ix['ps']] / S[:, ix['cs']]; s1 = S[:, ix['psTP']] / S[:, ix['csTP']]; s2 = S[:, ix['prTP']] / S[:, ix['crTP']]; s3 = S[:, ix['pr']] / S[:, ix['cr']]
        gap = s3 - s0; e0 = S[:, ix['p|V0_primaria']] / S[:, ix['c|V0_primaria']]; e4 = S[:, ix['p|V4_cota_HI']] / S[:, ix['c|V4_cota_HI']]
    assert ic(gap) == bt['gap_ic90'], ('pesos distintos de Q.boot', ic(gap), bt['gap_ic90'])
    out['total'] = dict(ic90_comun={k: bt[k] for k in ('n_cierres', 'B', 'semilla', 'gap_ic90', 'ev_real_ic90', 'ev_sim_sin_corr_ic90')},
                        residual_V0_ic90=ic(s3 - e0), residual_V4_ic90=ic(s3 - e4), filas=tot)
    # ---------------- 6. por dia, LODO, por clase, por moneda
    KD = ('sin_correccion', 'V0_primaria', 'V4_cota_HI', 'V2_cancel_lat', 'V3_proporcional', 'ref_MIX_QC', 'C1_quitar_12_FP', 'C2_quitar_FP_alcanzables', 'V0_primaria|soloFP', 'V0_primaria|soloTP')
    pdia, lodo = {}, {}
    for d in DIAS:
        m = (R.dia == d).values; Rd = R[m]
        pdia[d] = {k: Q.metricas(Rd, QS[k][m]) for k in KD}
        b2 = Q.boot(Rd, {'V0_primaria': QS['V0_primaria'][m], 'V4_cota_HI': QS['V4_cota_HI'][m]})
        pdia[d]['V0_primaria']['ic90_cierre_dentro_del_dia'] = b2['V0_primaria']; pdia[d]['V4_cota_HI']['ic90_cierre_dentro_del_dia'] = b2['V4_cota_HI']
        Rl = R[~m]; lodo['sin_' + d] = {k: Q.metricas(Rl, QS[k][~m]) for k in KD}
    porc = {}
    for c in ('lo', 'hi', 'indet', 'pendiente_ADD3'):
        m = (R.clase == c).values
        if not m.any(): continue
        Rc = R[m]; porc[c] = {k: Q.metricas(Rc, QS[k][m]) for k in KD}
        if int((Rc.q_s > 1e-9).sum()) >= 2:
            b3 = Q.boot(Rc, {'V0_primaria': QS['V0_primaria'][m], 'V4_cota_HI': QS['V4_cota_HI'][m]})
            porc[c]['V0_primaria']['ic90_cierre'] = b3['V0_primaria']; porc[c]['V4_cota_HI']['ic90_cierre'] = b3['V4_cota_HI']
    pmon = {}
    for c in sorted(R.coin.astype(str).unique()):
        m = (R.coin.astype(str) == c).values; pmon[c] = {k: Q.metricas(R[m], QS[k][m]) for k in ('sin_correccion', 'V0_primaria', 'V4_cota_HI')}
    out['por_dia'] = pdia; out['lodo'] = lodo; out['por_clase'] = porc; out['por_moneda_descriptivo'] = pmon
    # ---------------- 7. pruebas T1-T5
    aff = sim0 & valid; tf_a = R.v3d_BASE_f_tf[aff].astype(float).values; tc_a = R.tcs[aff].values * 1000.0; x_a = tf_a - tc_a
    real_a = real[aff].values; ps_a = R.p_s[aff].values; cs_a = R.c_s[aff].values; win_a = (x_a > 0) & (x_a <= 111)
    Ps, Cs = float(R.p_s.sum()), float(R.c_s.sum()); e_inf = Ps / Cs; e_real = float(R.p_r.sum() / R.c_r.sum()); g0 = e_real - e_inf
    vidx = np.where(valid.values)[0]; pool = d_v0.values[vidx]; rtt_pool = R.rtt.values[vidx]; posv = {i: k for k, i in enumerate(vidx)}
    pa = np.array([posv[i] for i in np.where(aff.values)[0]])
    def st(dv, keep=None):
        an = tf_a > tc_a + dv
        if keep is not None: an = an & keep
        es = (Ps - ps_a[an].sum()) / (Cs - cs_a[an].sum())
        return dict(f=(es - e_inf) / g0, S=int((an & ~real_a).sum() - (an & real_a).sum()), Sw=int((an & ~real_a & win_a).sum() - (an & real_a & win_a).sum()),
                    afp=int((an & ~real_a).sum()), atp=int((an & real_a).sum()))
    obs = st(pool[pa])
    assert abs(obs['f'] - tot['V0_primaria']['cierra_brecha']) < 6e-4, ('cierre del placebo != metricas', obs['f'], tot['V0_primaria']['cierra_brecha'])
    # T1 (+ D2 nulo condicionado) y T1b
    T1t = pd.read_pickle(H + 'out/T1_tx.pkl')[['order_hash', 'tx', 'token']].copy(); T1t['token'] = T1t.token.astype(str); T1t['tx'] = T1t.tx.astype(str)
    OW = pd.concat([pd.read_pickle(H + f'out_v3/own_{d}.pkl') for d in DIAS], ignore_index=True); OW['token_id'] = OW.token_id.astype(str); OW['tx'] = OW.tx.astype(str)
    MM = T1t.merge(OW[['tx', 'token_id', 'tm3', 'rama']], left_on=['tx', 'token'], right_on=['tx', 'token_id'], how='left')
    MM['tm3'] = MM.tm3.astype(float); ok = MM.rama.notna() & (MM.rama.astype(str) != 'sinev') & MM.tm3.notna()
    last_ok = MM[ok].groupby('order_hash').tm3.max(); last_all = MM[MM.tm3.notna()].groupby('order_hash').tm3.max()
    R['tm3_last_ok'] = R.oid.map(last_ok); R['tm3_last_all'] = R.oid.map(last_all)
    R['xr_ok'] = R.tm3_last_ok - R.tcs * 1000.0; R['xr_all'] = R.tm3_last_all - R.tcs * 1000.0
    qd = json.load(open(E + 'QC_desc_tf_menos_tcs.json')); x7pub = [v for v in qd['TP']['x_ms_ordenado'] if v > 111]
    t7 = sim0 & real & R.tcs.notna() & (R.x > 111)
    x7 = sorted(R.x[t7].round(1).tolist()); assert len(x7) == 7 and all(abs(a - b) <= 0.051 for a, b in zip(x7, x7pub)), ('los 7 no coinciden con QC_desc', x7, x7pub)
    rows7 = []; p_marg, p_cond = [], []
    for i in R.index[t7]:
        xi = float(R.x[i]); di = float(d_v0[i]) if valid[i] else np.inf; d4 = float(d_v4[i]) if valid[i] else np.inf
        pm = float(np.mean(pool >= xi)); el = rtt_pool >= xi; pc = float(np.mean(rtt_pool[el] >= xi + A_ACK)) if el.any() else np.nan
        p_marg.append(pm); p_cond.append(pc)
        xr = R.xr_ok[i] if np.isfinite(R.xr_ok[i]) else (R.xr_all[i] if np.isfinite(R.xr_all[i]) else np.nan)
        if di >= xi: lec = 'ida_y_vuelta_larga'
        elif not np.isfinite(xr): lec = 'sin_sello'
        elif xr < di: lec = 'simulador_tardio'
        else: lec = 'contradiccion'
        rows7.append(dict(oid=R.oid[i][:12], dia=R.dia[i], coin=R.coin[i], clase=R.clase[i], x_ms=rn(xi, 1), rtt_ms=rn(R.rtt[i], 1), delta_V0=rn(di, 1), sobrevive_V0=bool(di >= xi),
                          delta_V4=rn(d4, 1), sobrevive_V4=bool(d4 >= xi), x_real_ultimo_ms=rn(xr, 1), sello_real=('ok' if np.isfinite(R.xr_ok[i]) else ('sinev' if np.isfinite(R.xr_all[i]) else 'no')),
                          lectura_T1b=lec, p_nulo_marginal=rn(pm, 4), p_nulo_condicionado_D2=rn(pc, 4)))
    k7 = sum(r['sobrevive_V0'] for r in rows7); k7v4 = sum(r['sobrevive_V4'] for r in rows7)
    out['T1'] = dict(regla='delta_i >= x_i (sobrevive); confirmada >=6/7, refutada <=3/7, 4-5 no concluyente', k_V0=k7, k_V4=k7v4,
                     veredicto=('CONFIRMADA' if k7 >= 6 else ('REFUTADA' if k7 <= 3 else 'NO_CONCLUYENTE')),
                     veredicto_V4=('CONFIRMADA' if k7v4 >= 6 else ('REFUTADA' if k7v4 <= 3 else 'NO_CONCLUYENTE')),
                     p_cola_nulo_marginal_preregistrado=rn(pb_cola(p_marg, k7), 6), p_cola_nulo_condicionado_D2=rn(pb_cola(p_cond, k7), 6),
                     aviso_D2='x_i <= rtt_i por construccion (D1): el nulo marginal preregistrado sobrestima la evidencia; el condicionado (P(rtt >= x+24 | rtt >= x)) es el justo',
                     filas=rows7)
    # T2 consistencia con los rellenos reales
    def t2(dv, col):
        el = real & valid & R[col].notna() & (R[col] > 0); xr = R[col][el]; dd = dv[el]; vi = xr >= dd; n = int(el.sum()); nv = int(vi.sum())
        ver = 'INSUFFICIENT' if n < 5 else ('PASS' if nv <= 0.10 * n else ('FAIL' if nv > 0.25 * n else 'AMBER'))
        res = dict(elegibles=n, violaciones=nv, fraccion=(rn(nv / n, 3) if n else None), veredicto=ver,
                   por_clase={c: dict(n=int((el & (R.clase == c)).sum()), violaciones=int((vi & (R.clase[el] == c)).sum())) for c in ('lo', 'hi', 'indet', 'pendiente_ADD3')},
                   margen_delta_menos_xreal_ms=dict(p5=rn((dd - xr).quantile(.05), 1), p50=rn((dd - xr).median(), 1), min=rn((dd - xr).min(), 1)) if n else None,
                   banda_20ms=dict(viol_si_delta_menos_20=int((xr >= dd - 20).sum()), viol_si_delta_mas_20=int((xr >= dd + 20).sum())) if n else None,
                   filas=[dict(oid=o[:12], dia=d_, clase=c_, x_real=rn(a, 1), delta=rn(b, 1), viola=bool(a >= b)) for o, d_, c_, a, b in zip(R.oid[el], R.dia[el], R.clase[el], xr, dd)])
        return res
    cob = dict(rellenos_reales=int(real.sum()), en_T1_tx=int(real.sum() and R.oid[real].isin(set(T1t.order_hash)).sum()), con_sello_ok=int((real & R.tm3_last_ok.notna()).sum()),
               con_sello_cualquiera=int((real & R.tm3_last_all.notna()).sum()), reales_con_delta=int((real & valid).sum()),
               reales_x_real_gt0=int((real & valid & (R.xr_ok > 0)).sum()), reales_x_real_le0=int((real & valid & (R.xr_ok <= 0)).sum()),
               reales_sello_despues_de_t_fuera=int((real & valid & (R.tm3_last_ok > R.t_fuera_s * 1000.0)).sum()))
    out['T2'] = dict(regla='elegibles: relleno real, delta definida, sello propio no sinev, x_real_ultimo > 0; viola si x_real_ultimo >= delta; PASS <=10 %, FAIL >25 %, INSUFFICIENT n<5',
                     cobertura=cob, V0=t2(d_v0, 'xr_ok'), V4=t2(d_v4, 'xr_ok'), V0_con_sinev=t2(d_v0, 'xr_all'))
    # T3 placebo (global preregistrado + estratificado) y D3 placebo condicionado
    rng = np.random.default_rng([SEED, 3]); PG = []
    for b in range(NPERM): p = rng.permutation(len(pool)); PG.append(st(pool[p[pa]]))
    strata = collections.defaultdict(list)
    for k, i in enumerate(vidx): strata[(R.dia.values[i], str(R.coin.values[i]))].append(k)
    strata = [np.array(v) for v in strata.values()]
    rng = np.random.default_rng([SEED, 4]); PE = []
    for b in range(NPERM):
        p = np.arange(len(pool))
        for s_ in strata: p[s_] = s_[rng.permutation(len(s_))]
        PE.append(st(pool[p[pa]]))
    srt = np.sort(rtt_pool); lo_i = np.searchsorted(srt, x_a, side='left'); rng = np.random.default_rng([SEED, 6]); PC = []
    for b in range(NPERM):
        u = rng.random(len(x_a)); j = lo_i + np.floor(u * (len(srt) - lo_i)).astype(int); j = np.minimum(j, len(srt) - 1); PC.append(st(srt[j] - A_ACK))
    def resumen(L_, nombre):
        f = np.array([r['f'] for r in L_]); s_ = np.array([r['S'] for r in L_]); sw = np.array([r['Sw'] for r in L_])
        return dict(placebo=nombre, n=len(L_), p_f=rn((1 + np.sum(f >= obs['f'])) / (1 + len(L_)), 4), p_S=rn((1 + np.sum(s_ >= obs['S'])) / (1 + len(L_)), 4),
                    p_S_ventana=rn((1 + np.sum(sw >= obs['Sw'])) / (1 + len(L_)), 4), f_p5_p50_p95=[rn(np.quantile(f, q), 3) for q in (.05, .5, .95)],
                    S_p5_p50_p95=[float(np.quantile(s_, q)) for q in (.05, .5, .95)], Sw_p5_p50_p95=[float(np.quantile(sw, q)) for q in (.05, .5, .95)],
                    anulados_fp_medio=rn(np.mean([r['afp'] for r in L_]), 2), anulados_tp_medio=rn(np.mean([r['atp'] for r in L_]), 2))
    out['T3'] = dict(observado=dict(f=rn(obs['f'], 3), S=obs['S'], S_ventana=obs['Sw'], anulados_fp=obs['afp'], anulados_tp=obs['atp']),
                     global_preregistrado=resumen(PG, 'permutacion global entre las 3.737 (rng [20261116,3])'),
                     estratificado_dia_moneda=resumen(PE, 'permutacion dentro de dia x moneda (rng [20261116,4])'),
                     D3_condicionado=resumen(PC, 'delta de ordenes j con rtt_j >= x_i (rng [20261116,6]); DESCRIPTIVO declarado antes de ejecutar'),
                     aviso='x_i <= rtt_i por construccion: para x > 51 ms (rtt minimo) el placebo global favorece al emparejamiento real; la prueba justa es la ventana (x <= 51 en la practica) y D3')
    # ---- v2 (b)(c)(d): nulo forward con rtt de ordenes SIN relleno real, sin TP con rtt >= 1 s, solo lado FP. Todo DESCRIPTIVO, declarado tras la revision independiente.
    def resumen_g(L_, ob, nombre):
        f = np.array([r['f'] for r in L_]); s_ = np.array([r['S'] for r in L_]); sw = np.array([r['Sw'] for r in L_]); afp_ = np.array([r['afp'] for r in L_]); n_ = len(L_)
        return dict(placebo=nombre, n=n_, observado=dict(S=ob['S'], afp=ob['afp'], atp=ob['atp'], Sw=ob['Sw'], f=rn(ob['f'], 3)),
                    p_S=rn((1 + np.sum(s_ >= ob['S'])) / (1 + n_), 4), p_FP_solo=rn((1 + np.sum(afp_ >= ob['afp'])) / (1 + n_), 4), p_S_ventana=rn((1 + np.sum(sw >= ob['Sw'])) / (1 + n_), 4),
                    p_f=rn((1 + np.sum(f >= ob['f'])) / (1 + n_), 4), anulados_fp_medio=rn(np.mean(afp_), 2), anulados_tp_medio=rn(np.mean([r['atp'] for r in L_]), 2),
                    S_p5_p50_p95=[float(np.quantile(s_, q)) for q in (.05, .5, .95)])
    def plac_cond(srt_, x_, keep, seed):
        lo_ = np.searchsorted(srt_, x_, side='left'); rg = np.random.default_rng(seed); L_ = []
        for b_ in range(NPERM):
            u = rg.random(len(x_)); j = np.minimum(lo_ + np.floor(u * (len(srt_) - lo_)).astype(int), len(srt_) - 1); L_.append(st(srt_[j] - A_ACK, keep))
        return L_
    def plac_glob(pool_, keep, seed):
        rg = np.random.default_rng(seed); L_ = []
        for b_ in range(NPERM): p_ = rg.permutation(len(pool_)); L_.append(st(pool_[p_[pa]], keep))
        return L_
    rtt_a = R.rtt.values[aff.values]; sin_rel = valid & ~real
    srt_nf = np.sort(R.rtt.values[sin_rel.values]); srt_nf_lt1s = srt_nf[srt_nf < 1000]; srt_lt1s = np.sort(rtt_pool[rtt_pool < 1000])
    keep_all = np.ones(len(x_a), bool); keep_sin = ~(real_a & (rtt_a >= 1000)); ob_sin = st(pool[pa], keep_sin)
    tp_g1s = int((real_a & (rtt_a >= 1000)).sum())
    mw = None
    try:
        from scipy.stats import mannwhitneyu
        mw = float(mannwhitneyu(rtt_a[real_a], rtt_a[~real_a], alternative='greater').pvalue)
    except Exception as e: mw = 'scipy: ' + str(e)[:60]
    out['T3_v2'] = dict(
        aviso='DESCRIPTIVO, no preregistrado: declarado tras la revision estadistica independiente (REVISION_ESTADISTICA_QC2_16nov.md). Con el umbral q>=1e-3.',
        n_afectables=int(aff.sum()), n_afectables_TP=int(real_a.sum()), n_afectables_FP=int((~real_a).sum()), TP_afectables_con_rtt_ge_1000=tp_g1s,
        rtt_afectables_ms=dict(TP_p50=rn(np.median(rtt_a[real_a]), 1), FP_p50=rn(np.median(rtt_a[~real_a]), 1), sin_relleno_real_p50=rn(np.median(srt_nf), 1), mannwhitney_p_TP_mayor_que_FP=mw),
        pool_sin_relleno=dict(n=int(len(srt_nf)), p50=rn(np.median(srt_nf), 1), p90=rn(np.quantile(srt_nf, .9), 1), ge_1000=int((srt_nf >= 1000).sum())),
        observado_global=dict(S=obs['S'], afp=obs['afp'], atp=obs['atp'], Sw=obs['Sw']),
        nulo_forward_rtt_sin_relleno=resumen_g(plac_cond(srt_nf, x_a, None, [SEED, 7]), obs, 'delta = rtt_j - 24, j entre ordenes SIN relleno real con rtt_j >= x_i (rng [20261116,7])'),
        nulo_forward_rtt_sin_relleno_lt1s=resumen_g(plac_cond(srt_nf_lt1s, x_a, None, [SEED, 8]), obs, 'idem con rtt_j < 1 s (rng [20261116,8])'),
        D3_todas_las_ordenes=resumen_g(PC, obs, 'D3 de QC2 v1 (rng [20261116,6]) recalculado con umbral nuevo'),
        sin_TP_rtt_ge_1s=dict(observado=dict(S=ob_sin['S'], afp=ob_sin['afp'], atp=ob_sin['atp'], Sw=ob_sin['Sw']), n_afectables_restantes=int(keep_sin.sum()),
                              global_pool_todo=resumen_g(plac_glob(pool, keep_sin, [SEED, 9]), ob_sin, 'permutacion global, sin los TP afectables con rtt >= 1 s (rng [20261116,9])'),
                              D3_pool_todo=resumen_g(plac_cond(srt, x_a, keep_sin, [SEED, 10]), ob_sin, 'D3 (rtt_j >= x_i, pool todas las ordenes) sin esos TP (rng [20261116,10])'),
                              D3_pool_lt1s=resumen_g(plac_cond(srt_lt1s, x_a, keep_sin, [SEED, 11]), ob_sin, 'D3 con pool rtt_j < 1 s y sin esos TP (rng [20261116,11])')),
        solo_lado_FP=dict(nota='estadistico = FP anulados (ignora los TP anulados); p = P(FP anulados placebo >= observados)',
                          observado_afp=obs['afp'], global_perm=out['T3']['global_preregistrado']['placebo'], p_global=resumen_g(PG, obs, 'global')['p_FP_solo'],
                          p_estratificado=resumen_g(PE, obs, 'estrat')['p_FP_solo'], p_D3=resumen_g(PC, obs, 'D3')['p_FP_solo'],
                          p_nulo_forward=None))
    out['T3_v2']['solo_lado_FP']['p_nulo_forward'] = out['T3_v2']['nulo_forward_rtt_sin_relleno']['p_FP_solo']
    # T4 escalon
    stp = win_a & ~real_a & (x_a >= 35) & (x_a <= 49); twin = win_a & real_a; an0 = tf_a > tc_a + pool[pa]
    c1 = int((an0 & stp).sum()); c2 = int((an0 & twin).sum()); pw = out['T3']['global_preregistrado']['p_S_ventana']
    out['T4'] = dict(fp_escalon=int(stp.sum()), fp_escalon_anulados=c1, tp_ventana=int(twin.sum()), tp_ventana_anulados=c2, p_S_ventana_global=pw,
                     criterios=dict(i_ge5de7=bool(c1 >= 5), ii_le3de12=bool(c2 <= 3), iii_p_lt_0_10=bool(pw < 0.10)),
                     veredicto=('LO_EXPLICA_EL_DELTA_PROPIO' if (c1 >= 5 and c2 <= 3 and pw < 0.10) else 'SIGUE_POST_HOC'),
                     filas=sorted([dict(cls=('TP' if r_ else 'FP'), x=rn(x_, 1), delta_V0=rn(d_, 1), anulado=bool(a_)) for r_, x_, d_, a_ in zip(real_a[win_a], x_a[win_a], pool[pa][win_a], an0[win_a])], key=lambda z: z['x']))
    # T5 ida y vuelta por clase concurrente
    t5 = {}
    for d in DIAS:
        m = valid & (R.dia == d) & R.clase_conc.isin(['hi', 'lo'])
        t5[d] = {c: dict(n=int((m & (R.clase_conc == c)).sum()), rtt_p50=rn(R.rtt[m & (R.clase_conc == c)].median(), 1), post_lat_p50=rn(R.post_lat_ms[m & (R.clase_conc == c)].median(), 1))
                 for c in ('hi', 'lo')}
    m23 = valid & (R.dia == '2026-10-23'); H23 = R[m23 & (R.clase_conc == 'hi')]; L23 = R[m23 & (R.clase_conc == 'lo')]
    dmed = float(H23.rtt.median() - L23.rtt.median()) if len(H23) and len(L23) else np.nan
    gH = [g.rtt.values for _, g in H23.groupby('w_conc')]; gL = [g.rtt.values for _, g in L23.groupby('w_conc')]; rng = np.random.default_rng([SEED, 5]); bd = []
    for b in range(NBT5 if (gH and gL) else 0):
        hh = np.concatenate([gH[i] for i in rng.integers(len(gH), size=len(gH))]); ll = np.concatenate([gL[i] for i in rng.integers(len(gL), size=len(gL))]); bd.append(np.median(hh) - np.median(ll))
    dpl = float(H23.post_lat_ms.median() - L23.post_lat_ms.median()) if len(H23) and len(L23) else np.nan
    lect = ('NO_CONCLUYENTE' if not np.isfinite(dmed) else ('SIN_CAMBIO_IDA_Y_VUELTA' if abs(dmed) <= 5 else ('CAMBIO_DE_RED' if dmed >= 15 else 'NO_CONCLUYENTE')))
    out['T5'] = dict(regla='diferencia de medianas de rtt hi - lo dentro del 23-Oct; |d|<=5 sin cambio; d>=15 cambio de red; resto no concluyente', por_dia=t5,
                     d23=dict(n_hi=int(len(H23)), n_lo=int(len(L23)), ventanas_hi=len(gH), ventanas_lo=len(gL), dif_mediana_rtt_ms=rn(dmed, 1), ic90_bootstrap_ventanas=ic(bd, 1),
                              dif_mediana_post_lat_ms=rn(dpl, 1)), lectura=lect)
    # ---------------- 8. cautela c: componentes de la brecha, residual y proyeccion de precision
    hw = (np.quantile(gap, .95) - np.quantile(gap, .05)) / 2.0; nc = int(R.cl.nunique()); cd = nc / 4.0
    def proy(h): n_ = nc * (hw / h) ** 2; return dict(semiamplitud_objetivo=h, n_cierres=int(np.ceil(n_)), dias_B_al_ritmo_20_23oct=rn(n_ / cd, 1))
    out['cautela_c'] = dict(
        dias_con_ordenes_B='solo 2026-10-20..23 (ledger: puja_post 405/1.121/1.746/524; 24-27 Oct sin ordenes; sin otro ledger de B)',
        sd_bootstrap=dict(ev_real=rn(np.nanstd(s3), 4), ev_sim_sin_corr=rn(np.nanstd(s0), 4), brecha=rn(np.nanstd(gap), 4), residual_V0=rn(np.nanstd(s3 - e0), 4),
                          corr_real_sim=rn(np.corrcoef(s3[np.isfinite(s3) & np.isfinite(s0)], s0[np.isfinite(s3) & np.isfinite(s0)])[0, 1], 3)),
        componentes_ic90=dict(paso_FP=dict(punto=rn(float(Q.escalones(R)['paso_quitar_FP']), 4), ic90=ic(s1 - s0), sd=rn(np.nanstd(s1 - s0), 4)),
                              paso_cantidad=dict(punto=rn(float(Q.escalones(R)['paso_cantidad_real']), 4), ic90=ic(s2 - s1), sd=rn(np.nanstd(s2 - s1), 4)),
                              paso_FN=dict(punto=rn(float(Q.escalones(R)['paso_anadir_FN']), 4), ic90=ic(s3 - s2), sd=rn(np.nanstd(s3 - s2), 4))),
        semiamplitud_ic90_brecha_actual=rn(hw, 4), n_cierres_actual=nc, cierres_por_dia=rn(cd, 2),
        proyeccion=[proy(0.10), proy(0.05), dict(objetivo='excluir 0 en la brecha puntual', **proy(abs(g0)))],
        nota='escala 1/sqrt(n) con la varianza por cierre de 20-23 Oct; supone mismo ritmo y mezcla; mas ordenes reales = dinero = decision de Javi')
    # ---------------- 9. curva del cierre f(A), A = 0..40 ms (+44,5): cota superior sin cota inferior (v2 (f))
    CV = []
    for a in A_CURVA:
        qa = Q.sim_con_delta(R, (R.rtt - a).where(valid).fillna(1e9))[0]; mt = Q.metricas(R, qa)
        CV.append(dict(A_ms=a, cierra_brecha=mt['cierra_brecha'], delta_ev=mt['delta_ev'], ev_sim=mt['ev_sim'], anulados_fp=mt['anulados_fp'], anulados_tp=mt['anulados_tp'], fills_sim=mt['fills_sim'], fp=mt['fp'], tp=mt['tp']))
    out['D4_curva_A'] = CV
    ok_sin_tp = [c for c in CV if c['A_ms'] <= 40 and c['anulados_tp'] == 0]; primer_tp = next((c['A_ms'] for c in CV if c['anulados_tp'] > 0), None)
    A_max = max(c['A_ms'] for c in ok_sin_tp if primer_tp is None or c['A_ms'] < primer_tp)
    cA = {c['A_ms']: c for c in CV}; fmax = cA[A_max]['cierra_brecha']
    QA = {f'A{a}': Q.sim_con_delta(R, (R.rtt - a).where(valid).fillna(1e9))[0] for a in sorted({0, 12, 20, 24, 28, A_max, 33, 40})}
    bA = Q.boot(R, QA)
    out['cierre_curva_f_A'] = dict(
        regla='f(A) = cierre con delta_i = rtt_i - A. A = ack - ex NO medido en 20-23 Oct (ancla 13-Nov LO: 24 ms, p5-p99 20-28); la unica inferencia de datos es una COTA SUPERIOR '
              '(A mayor anula rellenos REALES): A <= A_max. NO hay cota inferior; f(A=0) = 0 por construccion (tf <= t_fuera). No hay valor puntual del cierre.',
        A_max_sin_TP_anulado_ms=A_max, primer_A_que_anula_TP_ms=primer_tp, f_en_A_max=fmax, f_A0=cA[0]['cierra_brecha'], intervalo_f=[0.0, fmax],
        f_en_A_24_ancla_13nov=cA[24]['cierra_brecha'], f_A20=cA[20]['cierra_brecha'], f_A28=cA[28]['cierra_brecha'],
        ic90_cierre_por_A={k: dict(cierra_ic90=v['cierra_ic90'], delta_ev_ic90=v['delta_ev_ic90'], p_delta_ev_le_0=v['p_delta_ev_le_0']) for k, v in bA.items() if k.startswith('A')},
        nota_n='n efectivo = FP con dinero anulables (4 dias/cierres); sin un FP, f cambia mucho (ver leave-one-out)')
    # cotas CONTINUAS de A (tf > tcs + rtt - A anula un TP si A > rtt - x): (1) TP simulados afectables; (2) T2: rellenos reales con sello propio, violacion si x_real >= rtt - A
    m_tp = (aff & real).values; b_tp = (R.rtt - R.x)[m_tp]; el2 = real & valid & R.xr_ok.notna() & (R.xr_ok > 0); b_t2 = (R.rtt - R.xr_ok)[el2]
    out['cierre_curva_f_A']['cotas_continuas_A_ms'] = dict(TP_simulados_afectables=dict(n=int(m_tp.sum()), A_max=rn(b_tp.min(), 2), tres_menores=sorted(b_tp.round(1).tolist())[:3]),
                                                          T2_rellenos_reales_con_sello=dict(n=int(el2.sum()), A_max=rn(b_t2.min(), 2), tres_menores=sorted(b_t2.round(1).tolist())[:3]),
                                                          lectura='cota de T2: 2 de 36 rellenos reales ya violan con A=24 (margen negativo; no dependen de A) y el 3.o menor es la cota; ambas cotas = 33,0 ms (la revision independiente daba ~32: misma cosa dentro de 1 ms de convencion). Sin cota inferior. Dominada por 1-3 observaciones: fragil')
    # leave-one-out de FP anulados con A_max (sensibilidad al n pequeno)
    loo = []
    qm = Q.sim_con_delta(R, (R.rtt - A_max).where(valid).fillna(1e9))[1] & ~real
    for i in R.index[qm]:
        q1 = Q.sim_con_delta(R, (R.rtt - A_max).where(valid).fillna(1e9))[0].copy(); q1[i] = R.q_s[i]; loo.append(dict(oid=R.oid[i][:12], dia=R.dia[i], coin=str(R.coin[i]), x=rn(R.x[i], 1), f_sin_esa_anulacion=Q.metricas(R, q1)['cierra_brecha']))
    out['cierre_curva_f_A']['leave_one_out_FP_en_A_max'] = loo
    # ---------------- 10. veredicto s.6
    pS = out['T3']['global_preregistrado']['p_S']; v2 = out['T2']['V0']['veredicto']; t1 = out['T1']['veredicto']
    if v2 == 'INSUFFICIENT' or int(aff.sum()) < 10: ver = 'INSUFFICIENT'
    elif v2 == 'FAIL': ver = 'CONTRADICHO'
    elif pS < 0.05 and v2 == 'PASS' and t1 != 'REFUTADA': ver = 'MECANISMO_SOPORTADO_POR_ORDEN'
    elif pS >= 0.05 and v2 == 'PASS': ver = 'NIVEL_SIN_IDENTIFICACION_POR_ORDEN'
    else: ver = f'OTRA (literal): p_S={pS}, T2={v2}, T1={t1}'
    f0 = tot['V0_primaria']['cierra_brecha']; f4 = tot['V4_cota_HI']['cierra_brecha']
    out['veredicto_s6'] = dict(veredicto=ver, p_S_global=pS, T2_V0=v2, T1=t1, cierre_V0=f0, cierre_V4=f4, intervalo_HI=[min(f0, f4), max(f0, f4)],
                               C1=tot['C1_quitar_12_FP']['cierra_brecha'], C2=tot['C2_quitar_FP_alcanzables']['cierra_brecha'],
                               soloFP_V0=tot['V0_primaria|soloFP']['cierra_brecha'], soloTP_V0=tot['V0_primaria|soloTP']['cierra_brecha'],
                               cien_por_cien_alcanzable_por_delta=bool((tot['C2_quitar_FP_alcanzables']['cierra_brecha'] or 0) >= 1))
    out['veredicto_s6']['nota'] = 'veredicto LITERAL de la regla sellada del s.6 con umbral q>=1e-3; no es la etiqueta de sustancia (ver etiquetas_v2)'
    sT3 = out['T3_v2']
    out['etiquetas_v2'] = dict(
        T1='no informativa (los 7 TP de T1 tienen cancel_ya_terminal_ack; el nulo condicionado da p=%s: x<=rtt por construccion)' % out['T1']['p_cola_nulo_condicionado_D2'],
        identificacion_por_orden='NO VALIDADA (p_S global %s es estructural: x<=rtt; D3 condicionado %s; nulo forward %s; sin TP rtt>=1s D3 %s; solo lado FP global %s)' % (
            out['T3']['global_preregistrado']['p_S'], out['T3']['D3_condicionado']['p_S'], sT3['nulo_forward_rtt_sin_relleno']['p_S'], sT3['sin_TP_rtt_ge_1s']['D3_pool_todo']['p_S'], sT3['solo_lado_FP']['p_global']),
        T4='NO VALIDADO: %d FP en el escalon 35-49 ms (7 con polvo), %d anulados; depende de la misma identificacion por orden' % (out['T4']['fp_escalon'], out['T4']['fp_escalon_anulados']),
        cierre='curva f(A) con cota superior A<=%s ms y sin cota inferior (f en [0, %s]); NO hay cifra puntual' % (out['cierre_curva_f_A']['A_max_sin_TP_anulado_ms'], out['cierre_curva_f_A']['f_en_A_max']),
        HI='retirada la frase \'la carrera no necesita correccion HI\'. Solo: A_HI(20-23 Oct) <= ~32 ms (T2 V4 FAIL, 11/36 frente a 2/36 de V0, fragil); no hay A_LO del mismo periodo; A_HI y A_LO no medidos el mismo dia (ADDENDUM2 s.8)',
        nota_C1='la clave C1_quitar_12_FP de las tablas es ahora C1 = quitar los 10 FP reales (nombre heredado de v1)',
        niveles_que_quedan='nivel de delta compatible con fantasmas al final del segmento (Fisher p=0,0005 en la revision); la correccion respecto a MIX (MIX anulaba 10 TP) y C1/C2 en EV se mantienen',
        aviso='EXPLORATORY/descriptivo; ninguna etiqueta autoriza operar en real; delta usa t_fuera (depende del desenlace): admisible en replay, NO trasladable a un simulador forward')
    out['T1']['etiqueta_v2'] = 'no informativa'
    # ---- comparacion con QC2 v1 (umbral q>1e-9) y con QC/brecha_nivel_v3
    v1t = V1['total']['filas']; nt = tot
    out['cambios_vs_v1'] = {
        f'{k}.{c}': dict(v1=v1t[k][c], v2=nt[k][c]) for k, c in (('sin_correccion', 'fills_sim'), ('sin_correccion', 'fp'), ('sin_correccion', 'tp'), ('sin_correccion', 'ev_sim'), ('sin_correccion', 'gap'),
                                                              ('V0_primaria', 'fills_sim'), ('V0_primaria', 'fp'), ('V0_primaria', 'anulados_fp'), ('V0_primaria', 'anulados_tp'), ('V0_primaria', 'ev_sim'),
                                                              ('V0_primaria', 'delta_ev'), ('V0_primaria', 'cierra_brecha'), ('C1_quitar_12_FP', 'cierra_brecha'), ('C2_quitar_FP_alcanzables', 'cierra_brecha'),
                                                              ('V4_cota_HI', 'cierra_brecha'), ('V4_cota_HI', 'anulados_tp'))}
    out['cambios_vs_v1']['escalones_paso_quitar_FP'] = dict(v1=ES['paso_quitar_FP'], v2=Q.escalones(R)['paso_quitar_FP'])
    out['cambios_vs_v1']['T4'] = dict(v1=dict(fp_escalon=V1['T4']['fp_escalon'], anulados=V1['T4']['fp_escalon_anulados'], tp_ventana=V1['T4']['tp_ventana'], tp_anulados=V1['T4']['tp_ventana_anulados'], veredicto=V1['T4']['veredicto']),
                                      v2=dict(fp_escalon=out['T4']['fp_escalon'], anulados=out['T4']['fp_escalon_anulados'], tp_ventana=out['T4']['tp_ventana'], tp_anulados=out['T4']['tp_ventana_anulados'], veredicto=out['T4']['veredicto']))
    out['cambios_vs_v1']['T3'] = dict(v1=dict(p_S_global=V1['T3']['global_preregistrado']['p_S'], p_S_D3=V1['T3']['D3_condicionado']['p_S'], S_obs=V1['T3']['observado']['S']),
                                      v2=dict(p_S_global=out['T3']['global_preregistrado']['p_S'], p_S_D3=out['T3']['D3_condicionado']['p_S'], S_obs=out['T3']['observado']['S']))
    out['fallos'] = fallos
    out['estado'] = 'COMPLETE' if not fallos else 'COMPLETE_CON_FALLOS'
    out['recursos'] = dict(cpu_s=round(time.process_time(), 1), pared_s=round(time.time() - t0, 1), maxrss_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1))
    out['fin_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    tmp = E + 'QC2_v2_sinpolvo.json.tmp'; json.dump(out, open(tmp, 'w'), indent=1, default=str); os.replace(tmp, E + 'QC2_v2_sinpolvo.json')
    cab = ['ambito', 'variante', 'n_ordenes', 'n_cierres', 'fills_real', 'fills_sim', 'tp', 'fp', 'fn', 'anulados', 'anulados_tp', 'anulados_fp', 'precision', 'recall',
           'ev_sim', 'ev_sim_sin_corr', 'ev_real', 'delta_ev', 'gap', 'cierra_brecha', 'ev_sim_ic90_cierre', 'delta_ev_ic90_cierre', 'cierra_ic90_cierre']
    lines = ['# Q-C2 v2 DESCRIPTIVA, umbral q>=1e-3 (sin polvo). Base: Q-C2 (ADDENDUM2_PREREG_REPLAY_BRECHA_B_16nov, sha256 ' + ADD2_SHA[:16] + '...), BF5-REPLAY-COLOC-v1. EXPLORATORY, explicativo; no decide ninguna palanca.',
             '# Muestra: 3.796 ordenes reales de B, 20-23 Oct 2026 (ETH/SOL/XRP 5m), V3_<D>.pkl (verif_v3, sello v3 + dedupe, cola BASE) + ordenes_b.csv + ledger H47-B.',
             '# delta_i = 1000*(t_fuera - t_cancel_int) - 24 ms (equivale a cortar el segmento simulado en t_fuera - 24). V4 = cota HI (-20,5 en ventanas hi). C1/C2 = techos oraculo.',
             '# EV = sum pnl / sum coste con rebate; cierra = (EV_sim(delta) - EV_sim(sin corr)) / (EV_real - EV_sim(sin corr)); IC90 percentil por cierre, B=10.000, semilla 20261116.',
             '# Comando: ' + out['comando'] + '  | codigo sha256 ' + out['codigo_sha256'], '\t'.join(cab)]
    def fila(amb, k, mt):
        icx = mt.get('ic90_cierre') or mt.get('ic90_cierre_dentro_del_dia') or {}
        return '\t'.join(str(x) for x in [amb, k] + [mt.get(c) for c in cab[2:20]] + [icx.get('ev_sim_ic90', ''), icx.get('delta_ev_ic90', ''), icx.get('cierra_ic90', '')])
    for k, mt in tot.items(): lines.append(fila('total', k, mt))
    for d in DIAS:
        for k in KD: lines.append(fila('dia_' + d, k, pdia[d][k]))
    for dl in lodo:
        for k in KD: lines.append(fila('lodo_' + dl, k, lodo[dl][k]))
    for c, t in porc.items():
        for k in KD: lines.append(fila('clase_' + c, k, t[k]))
    open(E + 'QC2_v2_sinpolvo.tsv.tmp', 'w').write('\n'.join(lines) + '\n'); os.replace(E + 'QC2_v2_sinpolvo.tsv.tmp', E + 'QC2_v2_sinpolvo.tsv')
    print(json.dumps(dict(estado=out['estado'], reproduccion=out['reproduccion_previa'], veredicto=out['veredicto_s6'], recursos=out['recursos'], fallos=fallos), default=str))


if __name__ == '__main__':
    main()
