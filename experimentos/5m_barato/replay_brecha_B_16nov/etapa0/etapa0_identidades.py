#!/usr/bin/env python3
"""etapa0_identidades.py -- Etapa 0 del PREREG_REPLAY_BRECHA_B_16nov (+ ADDENDUM1 s.2): identidades SEGT<->CX (s.6.1-6, CONTROL DESCRIPTIVO
desde ADDENDUM1), verificacion SEGT subconjunto de N_ok (s.6.1-2, PUERTA) y paridad de lectura (s.6.1-7, PUERTA). SOLO LECTURA.
- No importa el motor, no lee ms2, no abre nada del HOLD (10-14 Nov) ni >= 15-Nov.
- Publica SOLO booleanos y diferencias por dia; la unica cifra en claro es el agregado de G0 de los 15 dias, YA PUBLICADO
  (PASS_T_V3_RESULTADOS_11nov.md s.4: 47.470 segmentos, 4.601 rellenos, coste 3.422 EUR, pnl -527,8 EUR, EV -0,154).
- pnl recalculado con s.5.1: pnl = q*(gana - L) + q*0,2*0,07*L*(1-L); coste = q*L (passT_cxb_v3.py:143, passT_v3.py:155).
- SEGT es anterior al arreglo de tf (11-Nov): su tf/T no entra en ninguna cifra; las diferencias de tf frente a R(G0) se cuentan (descriptivo).
Uso: ulimit -v 3000000; nice -n 19 ionice -c3 /usr/bin/python3 -I etapa0_identidades.py
Escribe en este directorio: identidades_SEGT_CX_E0.json (el .sha256 se escribe fuera con sha256sum)."""
import os, json, hashlib, time, resource, datetime as dt
import numpy as np, pandas as pd

H = os.path.dirname(os.path.abspath(__file__)) + '/'
R_ = '/root/polymarket-research/'
L2 = R_ + 'experimentos/5m_barato/l2_carrera_10nov/'
MIS = R_ + 'misiones/5m_barato/alpha_miner_B_F5_15nov/'
P2 = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out/'
DIAS = [d.strftime('%Y-%m-%d') for d in pd.date_range('2026-10-26', '2026-11-09')]
COINS = ('ETH', 'SOL', 'XRP')
TOL = 1e-6; QMIN = 1e-9; REB = 0.2 * 0.07
APA = {  # Apendice A del prereg: sha256 (16 hex) de CX_v3dd y SEGT_v3dd
    '2026-10-26': ('7a85cdb5c689a5c9', 'bcb2928495edc0cc'), '2026-10-27': ('774ca0666ecf997d', 'b96caee382a3de27'),
    '2026-10-28': ('a66d1ecc375352ef', 'a3fff3eef8dab3df'), '2026-10-29': ('0e14cb1b04b5df48', '1968741ddce2dfc8'),
    '2026-10-30': ('4e500ec40d4c6a90', 'cfde4f68146b1b9c'), '2026-10-31': ('007af78af73b1cfc', 'b652829447d938d1'),
    '2026-11-01': ('0d6a2a447ae854e6', 'a70a05c5ddee6af2'), '2026-11-02': ('74c9e95e028127ff', '90a12182d397cfcd'),
    '2026-11-03': ('4e1cb1d338f4ae1d', 'c6b9b4e0a0298312'), '2026-11-04': ('b1b57697e5d0c2d7', 'b7afc381c2c17572'),
    '2026-11-05': ('5cc7b4af954aac9a', '4a791df788fa5942'), '2026-11-06': ('9657382cea87ec34', '4b7e4301bf919bc7'),
    '2026-11-07': ('0b396e0de768257a', '78dace8a127e7937'), '2026-11-08': ('aa8ae756db1686d6', 'f2a64e67a1a429cb'),
    '2026-11-09': ('67b436c7c478946e', 'a66323ad6287cccb')}
# Cifra agregada YA PUBLICADA (PASS_T_V3_RESULTADOS_11nov.md s.4; prereg s.1.2 y s.6.1-7). Tolerancias: enteros exactos; coste y pnl a la
# precision publicada (media unidad del ultimo digito); EV +-0,0005 (s.6.1-7).
PUB = dict(n_seg=(47470, 0), n_fill=(4601, 0), cost=(3422.0, 0.5), pnl=(-527.8, 0.05), ev=(-0.154, 0.0005))


def sha_full(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for ch in iter(lambda: f.read(1 << 20), b''): h.update(ch)
    return h.hexdigest()


def pnl_of(q, L, g): return q * (g - L) + q * REB * L * (1 - L)


def fins(d):
    e0 = int(pd.Timestamp(d, tz='UTC').timestamp()); return [e0 + 4 * 3600 + 300 * (i + 1) for i in range(240)]   # cierres 04:05..24:00Z


def n_ok_set(d):
    """Reimplementacion INDEPENDIENTE (pandas, otra ruta de codigo que etapa0_dias_validos.py) de engine.sane para la regla de horas malas:
    fuera todo mercado cuya hora UTC de inicio (fin-300) o de cierre (fin) este en bad_<D>.json."""
    bad = pd.DataFrame(json.load(open(P2 + f'bad_{d}.json'))['bad'], columns=['d', 'h'])
    badk = set(zip(bad['d'].astype(str), bad['h'].astype(int)))
    f = pd.Series(fins(d), dtype='int64'); t0 = pd.to_datetime(f - 300, unit='s', utc=True); t1 = pd.to_datetime(f, unit='s', utc=True)
    m0 = [(a.strftime('%Y-%m-%d'), a.hour) in badk for a in t0]; m1 = [(b.strftime('%Y-%m-%d'), b.hour) in badk for b in t1]
    okf = f[~(np.array(m0) | np.array(m1))].tolist()
    return {(c, int(x)) for c in COINS for x in okf}


def main():
    t_ini = time.time()
    out = dict(job='etapa0_identidades', measurement_id='BF5-REPLAY-COLOC-v1',
               prereg_sha256=open(MIS + 'PREREG_REPLAY_BRECHA_B_16nov.sha256').read().split()[0],
               addendum1_sha256=open(MIS + 'ADDENDUM1_PREREG_REPLAY_BRECHA_B_16nov.sha256').read().split()[0],
               codigo_sha256=sha_full(os.path.abspath(__file__)), inicio_utc=dt.datetime.now(dt.timezone.utc).isoformat(),
               nota='Solo booleanos y diferencias por dia; la unica cifra en claro es el agregado G0 de 15 dias ya publicado (PASS_T_V3 s.4).')
    assert sha_full(MIS + 'PREREG_REPLAY_BRECHA_B_16nov.md') == out['prereg_sha256'], 'prereg alterado'
    assert sha_full(MIS + 'ADDENDUM1_PREREG_REPLAY_BRECHA_B_16nov.md') == out['addendum1_sha256'], 'addendum1 alterado'
    # dias validos fijados (hasheados) -> se leen, no se tocan
    shl = {l.split()[1]: l.split()[0] for l in open(H + 'dias_validos_E0.sha256') if l.strip()}
    dv_ok = sha_full(H + 'dias_validos_E0.json') == shl['dias_validos_E0.json']; assert dv_ok, 'dias_validos_E0.json no coincide con su sha256'
    DV = json.load(open(H + 'dias_validos_E0.json'))
    dias = {}; agg = dict(n_seg=0, n_fill=0, cost=0.0, pnl=0.0); agg_coin = {}
    for d in DIAS:
        pc, ps = L2 + f'out_v3/CX_v3dd_{d}.pkl', L2 + f'out_v3/SEGT_v3dd_{d}.pkl'
        shc, shs = sha_full(pc)[:16], sha_full(ps)[:16]
        S = pd.read_pickle(ps); X = pd.read_pickle(pc); A = X['A']; RR = X['R']
        A0 = A[A['var'] == 'G0'].copy(); R0 = RR[RR['var'] == 'G0'].copy(); del X, A, RR
        # ---------------- s.6.1-2: SEGT subconjunto de N_ok (puerta); recalculo independiente + lectura del JSON hasheado
        okset = n_ok_set(d); mk = set(zip(S['act'].astype(str), S['fin'].astype(np.int64)))
        fuera = sorted((a, int(f)) for a, f in mk if (a, int(f)) not in okset)
        js = DV['dias'][d]['segt']
        sub = dict(recalc_fuera=len(fuera), json_fuera=int(js['fuera_de_N_ok']), json_dia_ok=bool(js['dia_ok']),
                   dia_col_ok=bool((S['dia'] == d).all()), monedas_ok=bool(S['act'].astype(str).isin(COINS).all()),
                   pasa=bool(len(fuera) == 0 and int(js['fuera_de_N_ok']) == 0 and bool(js['dia_ok']) and bool((S['dia'] == d).all())))
        # ---------------- s.6.1-6: identidades SEGT <-> A(G0) <-> R(G0) (control descriptivo)
        S['cost'] = S.q * S.L; S['pnl'] = pnl_of(S.q, S.L, S.gana)
        sf = S[S.q > QMIN]
        n_seg_S, n_seg_A = len(S), int(A0.n_seg.sum())
        n_fill_S, n_fill_A, n_fill_R = int(len(sf)), int(A0.n_fill.sum()), int(len(R0))
        n_qpos_S = int((S.q > 0).sum())
        c_S, c_A, c_R = float(sf.cost.sum()), float(A0.cost.sum()), float(R0.cost.sum())
        p_S, p_A, p_R = float(sf.pnl.sum()), float(A0.pnl.sum()), float(R0.pnl.sum())
        p_R_recalc = float(pnl_of(R0.q, R0.L, R0.gana).sum()); c_R_recalc = float((R0.q * R0.L).sum())
        ide = dict(
            n_seg=dict(ok=n_seg_S == n_seg_A, d_SEGT_menos_A=n_seg_S - n_seg_A),
            n_fill=dict(ok=(n_fill_S == n_fill_A == n_fill_R), d_SEGT_menos_A=n_fill_S - n_fill_A, d_R_menos_A=n_fill_R - n_fill_A,
                        q_pos_igual_q_gt_1e9=n_qpos_S == n_fill_S),
            cost=dict(ok=bool(abs(c_S - c_A) <= TOL and abs(c_R - c_A) <= TOL), d_SEGT_menos_A=c_S - c_A, d_R_menos_A=c_R - c_A, d_Rrecalc_menos_R=c_R_recalc - c_R),
            pnl=dict(ok=bool(abs(p_S - p_A) <= TOL and abs(p_R - p_A) <= TOL), d_SEGT_menos_A=p_S - p_A, d_R_menos_A=p_R - p_A, d_Rrecalc_menos_R=p_R_recalc - p_R))
        ide['todas_ok'] = bool(all(ide[k]['ok'] for k in ('n_seg', 'n_fill', 'cost', 'pnl')) and ide['n_fill']['q_pos_igual_q_gt_1e9'])
        # por celda moneda x L (solo booleanos: n de celdas que fallan)
        S['Lk'] = S.L.round(2); A0['Lk'] = A0.L.round(2); R0['Lk'] = R0.L.round(2)
        gS = S.groupby(['act', 'Lk']).agg(n_seg=('q', 'size')); gS = gS.join(sf.assign(Lk=sf.L.round(2)).groupby(['act', 'Lk']).agg(n_fill=('q', 'size'), cost=('cost', 'sum'), pnl=('pnl', 'sum')), how='outer')
        gA = A0.groupby(['act', 'Lk'])[['n_seg', 'n_fill', 'cost', 'pnl']].sum()
        gR = R0.groupby(['act', 'Lk']).agg(n_fill=('q', 'size'), cost=('cost', 'sum'), pnl=('pnl', 'sum'))
        J = gA.join(gS, rsuffix='_S', how='outer').join(gR, rsuffix='_R', how='outer').fillna(0)
        bad_cells = int((~((J.n_seg == J.n_seg_S) & (J.n_fill == J.n_fill_S) & (J.n_fill == J.n_fill_R) & ((J.cost - J.cost_S).abs() <= TOL)
                           & ((J.cost - J.cost_R).abs() <= TOL) & ((J.pnl - J.pnl_S).abs() <= TOL) & ((J.pnl - J.pnl_R).abs() <= TOL))).sum())
        ide['celdas_moneda_L'] = dict(n=int(len(J)), fallan=bad_cells)
        # emparejado fila a fila de los rellenos SEGT <-> R(G0) por (act, lado, fin, L, t_dec)
        key = ['act', 'lado', 'fin', 'Lk', 't_dec']
        a = sf.assign(Lk=sf.L.round(2))[key + ['k', 'seg', 'q', 'gana', 'tf']]; b = R0[key + ['k', 'seg', 'q', 'gana', 'tf']]
        dupa, dupb = int(a.duplicated(key).sum()), int(b.duplicated(key).sum())
        m = a.merge(b, on=key, how='outer', suffixes=('_S', '_R'), indicator=True)
        both = m[m['_merge'] == 'both']
        ide['emparejado_rellenos'] = dict(
            clave='act,lado,fin,L,t_dec', duplicados_SEGT=dupa, duplicados_R=dupb, solo_SEGT=int((m['_merge'] == 'left_only').sum()),
            solo_R=int((m['_merge'] == 'right_only').sum()), emparejados_1a1=bool(dupa == 0 and dupb == 0 and len(both) == len(a) == len(b)),
            k_distinto=int((both.k_S != both.k_R).sum()), seg_distinto=int((both.seg_S != both.seg_R).sum()),
            q_distinto=int(((both.q_S - both.q_R).abs() > QMIN).sum()), gana_distinto=int((both.gana_S != both.gana_R).sum()),
            tf_distinto_descriptivo=int((both.tf_S != both.tf_R).sum()))
        e = ide['emparejado_rellenos']; ide['emparejado_rellenos']['ok'] = bool(e['emparejados_1a1'] and e['k_distinto'] == 0 and e['seg_distinto'] == 0 and e['q_distinto'] == 0 and e['gana_distinto'] == 0)
        dias[d] = dict(sha16=dict(CX=shc == APA[d][0], SEGT=shs == APA[d][1]), segt_en_N_ok=sub, identidades=ide,
                       valido_primaria=d in DV['dias_validos_primaria'], valido_hole60=d in DV['dias_validos_hole60'])
        agg['n_seg'] += n_seg_A; agg['n_fill'] += n_fill_A; agg['cost'] += c_A; agg['pnl'] += p_A
        for c, x in A0.groupby('act'):
            v = agg_coin.setdefault(c, [0, 0.0, 0.0]); v[0] += int(x.n_fill.sum()); v[1] += float(x.cost.sum()); v[2] += float(x.pnl.sum())
    # ---------------- s.6.1-7: paridad de lectura (puerta) contra la cifra YA publicada
    agg['ev'] = agg['pnl'] / agg['cost']
    par = {k: dict(publicado=PUB[k][0], leido=(round(agg[k], 6) if isinstance(agg[k], float) else agg[k]), tol=PUB[k][1],
                   ok=bool(abs(agg[k] - PUB[k][0]) <= PUB[k][1] + 1e-12)) for k in PUB}
    # control EXTRA (no es la puerta): contra el artefacto ORIGINAL de esas cifras publicadas, out_v3/paso0_v3dd/ev.json (generado desde RT/G0 de
    # passT_v3, otro fichero que CX), con tolerancia = media unidad del decimal publicado. (run1 comparaba con el md de PASS_T_V3 s.4, donde ETH
    # figura como -0,056 = -0,0555 redondeado dos veces: falso negativo por doble redondeo; ver etapa0_identidades_run1.log.)
    EVJ = L2 + 'out_v3/paso0_v3dd/ev.json'; J0 = json.load(open(EVJ))
    g = J0['G0']; fina = dict(fills=g['fills'] == agg['n_fill'], colocaciones=g['colocaciones'] == agg['n_seg'], cost=bool(abs(g['cost'] - agg['cost']) <= 0.005),
                              pnl2=bool(abs(g['pnl2']['pnl'] - agg['pnl']) <= 0.005), ev2=bool(abs(g['pnl2']['ev_eur'] - agg['ev']) <= 0.00005))
    par_coin = {c: dict(fills=J0['por_moneda'][c]['fills'] == agg_coin[c][0], cost=bool(abs(J0['por_moneda'][c]['cost'] - agg_coin[c][1]) <= 0.005),
                        pnl2=bool(abs(J0['por_moneda'][c]['pnl2']['pnl'] - agg_coin[c][2]) <= 0.005),
                        ev2=bool(abs(J0['por_moneda'][c]['pnl2']['ev_eur'] - agg_coin[c][2] / agg_coin[c][1]) <= 0.00005)) for c in COINS}
    par_coin = dict(fuente='out_v3/paso0_v3dd/ev.json', sha16=sha_full(EVJ)[:16], G0=fina, por_moneda=par_coin,
                    todo_ok=bool(all(fina.values()) and all(all(v.values()) for v in par_coin.values())))
    paridad_ok = all(v['ok'] for v in par.values())
    seg_ok = all(dias[d]['segt_en_N_ok']['pasa'] for d in DIAS); sha_ok = all(dias[d]['sha16']['CX'] and dias[d]['sha16']['SEGT'] for d in DIAS)
    ide_ok = [d for d in DIAS if dias[d]['identidades']['todas_ok']]; emp_ok = [d for d in DIAS if dias[d]['identidades']['emparejado_rellenos']['ok']]
    out.update(dias_validos_E0_sha256_ok=dv_ok, dias=dias, paridad_lectura=dict(agregado_G0_15_dias=par, por_moneda_booleanos=par_coin, pasa=paridad_ok),
               resumen=dict(sha_entradas_ok=sha_ok, segt_en_N_ok_15_de_15=seg_ok, identidades_ok_dias=len(ide_ok), identidades_fallan=[d for d in DIAS if d not in ide_ok],
                            emparejado_1a1_ok_dias=len(emp_ok), emparejado_fallan=[d for d in DIAS if d not in emp_ok],
                            tf_distinto_total_descriptivo=int(sum(dias[d]['identidades']['emparejado_rellenos']['tf_distinto_descriptivo'] for d in DIAS)),
                            paridad_lectura=('PASA' if paridad_ok else 'NO_PASA'),
                            puerta_parcial_etapa0=('PASA (SEGT en N_ok 15/15 y paridad de lectura); clase PENDIENTE_ADD3' if (seg_ok and paridad_ok and sha_ok) else 'NO_PASA')),
               recursos=dict(cpu_s=round(time.process_time(), 1), pared_s=round(time.time() - t_ini, 1), maxrss_mb=round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024, 1)),
               fin_utc=dt.datetime.now(dt.timezone.utc).isoformat())
    tmp = H + 'identidades_SEGT_CX_E0.json.tmp'; json.dump(out, open(tmp, 'w'), indent=1, default=str); os.replace(tmp, H + 'identidades_SEGT_CX_E0.json')
    print(json.dumps(dict(resumen=out['resumen'], paridad=out['paridad_lectura'], recursos=out['recursos']), default=str))


if __name__ == '__main__':
    main()
