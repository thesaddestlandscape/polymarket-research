#!/usr/bin/env python3
"""qc2_delta_propio.py -- Q-C2 del ADDENDUM2_PREREG_REPLAY_BRECHA_B_16nov (BF5-REPLAY-COLOC-v1), sellado 2026-11-16T18:05:25Z (sha256 d3ea7183...45ec).
SOLO LECTURA, 0 ordenes, CPU ~segundos. delta por orden = ida y vuelta del PROPIO DELETE de B menos el acuse:
    delta_i = 1000*(t_fuera - t_cancel_int) - A,  A = 24 ms (mediana ack-ex del pool 13-Nov; regla aprobada por Javi 16-Nov)
Equivalencia (s.2): con el segmento simulado [t_ini, t_fuera] de verif_v3, anular tf > tcs + delta_i es cortar el segmento en t_fuera - A.
Variantes V0..V4 y pruebas T1-T5, veredictos s.6 y cautela c (s.7) exactamente como en el ADDENDUM2. Importa qc_brecha_nivel_mix.py (sha256
comprobado; sus copias literales de brecha_nivel_v3.py se reverifican por AST). No importa el motor ni lee ms2.
Adiciones DESCRIPTIVAS decididas tras sellar el ADDENDUM2 y ANTES de ejecutar (registradas en QC2_DECLARACION_PREVIA.json; no cambian ningun
veredicto sellado): D1 comprobar tf <= t_fuera en todos los rellenos simulados; D2 nulo CONDICIONADO de T1 (P(sobrevive | ida y vuelta >= x));
D3 placebo CONDICIONADO (delta de ordenes j con ida y vuelta_j >= x_i, el unico emparejamiento compatible con la ventana simulada);
D4 curva del corte A en {0, 12, 20, 21, 24, 28, 31, 44.5}.
Uso: cd etapa0 && (ulimit -v 3000000; nice -n 19 ionice -c3 /usr/bin/python3 -I qc2_delta_propio.py) -> QC2_delta_propio.json / .tsv"""
import os, sys, json, time, resource, collections, datetime as dt
import numpy as np, pandas as pd

E = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, E)
import qc_brecha_nivel_mix as Q

DL = '/root/polymarket-research-datalogs/'
H = Q.H
ADD2_F = E + 'ADDENDUM2_PREREG_REPLAY_BRECHA_B_16nov.md'; ADD2_SHA = 'd3ea71837424893b86cc76e78cc21e2a40fe494b946ca533e08915b7ff5145ec'
DECL_F = E + 'QC2_DECLARACION_PREVIA.json'
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
A_CURVA = (0, 12, 20, 21, 24, 28, 31, 44.5)
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
    out = dict(job='qc2_delta_propio', measurement_id='BF5-REPLAY-COLOC-v1', etapa='Q-C2 (ADDENDUM2 s.2-8)',
               etiqueta='EXPLORATORY (explicativo; 4 dias, una estrategia real; no decide ninguna palanca ni valida B)',
               addendum2_sha256=ADD2_SHA, codigo_sha256=Q.sha_full(os.path.abspath(__file__)),
               comando='cd ' + E + ' && (ulimit -v 3000000; nice -n 19 ionice -c3 /usr/bin/python3 -I qc2_delta_propio.py)',
               inicio_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    # ---------------- 0. sellos y entradas (Fail Loud)
    assert Q.sha_full(ADD2_F) == ADD2_SHA and open(E + 'ADDENDUM2_PREREG_REPLAY_BRECHA_B_16nov.sha256').read().split()[0] == ADD2_SHA, 'ADDENDUM2 alterado'
    for nm in ('PREREG_REPLAY_BRECHA_B_16nov', 'ADDENDUM1_PREREG_REPLAY_BRECHA_B_16nov'):
        s = open(Q.MIS + nm + '.sha256').read().split()[0]; assert Q.sha_full(Q.MIS + nm + '.md') == s, nm + ' alterado'; out[nm + '_sha256'] = s
    D = json.load(open(DECL_F)); assert D['codigo_sha256'] == out['codigo_sha256'], 'este script no es el declarado en QC2_DECLARACION_PREVIA.json'
    assert Q.sha_full(DECL_F) == open(E + 'QC2_DECLARACION_PREVIA.sha256').read().split()[0], 'declaracion previa alterada'
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
    R = Q.carga()
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
    ref = json.load(open(Q.REF_F)); TD = Q.tabla_delta(R).to_dict('records'); ES = Q.escalones(R)
    rep1 = all(a == b for a, b in zip(TD, ref['tabla_delta'])) and len(TD) == len(ref['tabla_delta']) and ES == ref['escalones']
    QM = json.load(open(QMIX_OUT))['total']['filas']; dm = Q.delta_mix(R.oid, v_all)
    m_sc = Q.metricas(R, Q.sim_con_delta(R, 1e9)[0]); m_mx = Q.metricas(R, Q.sim_con_delta(R, dm)[0])
    rep2 = all(m_sc[k] == QM['sin_correccion'][k] for k in m_sc) and all(m_mx[k] == QM['MIX'][k] for k in m_mx)
    out['reproduccion_previa'] = dict(brecha_nivel_v3_publicado=bool(rep1), QC_sin_correccion_y_MIX=bool(rep2))
    if not (rep1 and rep2):
        out['estado'] = 'PARADO: no reproduce lo publicado (stop rule s.9; Fail Loud)'
        json.dump(out, open(E + 'QC2_delta_propio.json', 'w'), indent=1, default=str); print(json.dumps(out['reproduccion_previa'])); sys.exit(2)
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
    def st(dv):
        an = tf_a > tc_a + dv
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
    # ---------------- 9. D4 curva del corte A (descriptiva, declarada antes de ejecutar)
    out['D4_curva_A'] = [dict(A_ms=a, **{k: Q.metricas(R, Q.sim_con_delta(R, (R.rtt - a).where(valid).fillna(1e9))[0])[k] for k in ('cierra_brecha', 'anulados_fp', 'anulados_tp', 'ev_sim')}) for a in A_CURVA]
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
    out['fallos'] = fallos
    out['estado'] = 'COMPLETE' if not fallos else 'COMPLETE_CON_FALLOS'
    out['recursos'] = dict(cpu_s=round(time.process_time(), 1), pared_s=round(time.time() - t0, 1), maxrss_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1))
    out['fin_utc'] = dt.datetime.now(dt.timezone.utc).isoformat()
    tmp = E + 'QC2_delta_propio.json.tmp'; json.dump(out, open(tmp, 'w'), indent=1, default=str); os.replace(tmp, E + 'QC2_delta_propio.json')
    cab = ['ambito', 'variante', 'n_ordenes', 'n_cierres', 'fills_real', 'fills_sim', 'tp', 'fp', 'fn', 'anulados', 'anulados_tp', 'anulados_fp', 'precision', 'recall',
           'ev_sim', 'ev_sim_sin_corr', 'ev_real', 'delta_ev', 'gap', 'cierra_brecha', 'ev_sim_ic90_cierre', 'delta_ev_ic90_cierre', 'cierra_ic90_cierre']
    lines = ['# Q-C2 (ADDENDUM2_PREREG_REPLAY_BRECHA_B_16nov, sha256 ' + ADD2_SHA[:16] + '...), BF5-REPLAY-COLOC-v1. EXPLORATORY, explicativo; no decide ninguna palanca.',
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
    open(E + 'QC2_delta_propio.tsv.tmp', 'w').write('\n'.join(lines) + '\n'); os.replace(E + 'QC2_delta_propio.tsv.tmp', E + 'QC2_delta_propio.tsv')
    print(json.dumps(dict(estado=out['estado'], reproduccion=out['reproduccion_previa'], veredicto=out['veredicto_s6'], recursos=out['recursos'], fallos=fallos), default=str))


if __name__ == '__main__':
    main()
