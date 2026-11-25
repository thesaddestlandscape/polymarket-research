#!/usr/bin/env python3
"""test_fase_b_run.py -- runner FASE B: Delta de la horquilla, dry de 1 mercado (base/V5/V1 dentro del replay), tabla de variantes, final PARCIAL, checkpoint/codigo, carga Binance, t_proc obligatorio."""
import sys, os, json, gzip, types, tempfile, shutil, subprocess
import numpy as np, pandas as pd
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; TMP = tempfile.mkdtemp(prefix='fb_test_'); os.environ['FB_OUT'] = TMP + '/out/'; os.environ['FB_T_PROC_MS'] = '0'; os.environ['P0_K'] = '50'
sys.path.insert(0, HV)
import fase_b_run as FB, replay_variantes as RV, variantes_b as VB, sec7_core as C, e1_modelo as E1
import test_b_real_sim as TB, b_policy_sim as BS
t0 = TB.T0; nan = float('nan'); BS.G.capt_outcome = lambda E, k: E.capt.outcome(E.D, k)
def S(rows, dlag=20):
    a = np.array(rows, float); return C.SerieL1(a[:, 0], a[:, 0] - dlag, a[:, 1], a[:, 2], a[:, 3], a[:, 4])
def ctx_stub(prints=None, bsrc=None, comp_rows=None):
    st = TB.Stub([('eth', [(t0 - 400000, 0.22, 0.24)], [(t0 - 400000, 0.70, 0.72)])], prints=prints if prints is not None else {0: [(t0 + 20000, 0.19)]}); st.D.comp = lambda k: 1 - k
    own = S([(t0 - 20000, 0.22, 0.24, 50, 20)]); comp = S(comp_rows or [(t0 - 20000, 0.70, 0.72, 30, 30)]); W = C.EngineBloqueo(st, activo=False)
    return dict(W=W, serie=lambda k: own if k == 0 else comp, bsrc=bsrc or {}, P=TB.P0, dia='2026-11-08', horq='H0', k2tok={}, l2=None)

def test_t_proc_obligatorio_sin_default():
    env = {k: v for k, v in os.environ.items() if k != 'FB_T_PROC_MS'}; r = subprocess.run([sys.executable, HV + 'fase_b_run.py', 'final'], env=env, capture_output=True, text=True); assert r.returncode != 0 and 'FB_T_PROC_MS' in r.stderr + r.stdout
    assert FB.t_proc() == 0.0
def test_engine_bloqueo_delta_recorta_solo_bloqueo():
    own = S([(t0 - 5000, 0.22, 0.24, 50, 40)]); comp = S([(t0 - 5000, 0.70, 0.72, 30, 30), (t0 + 1000, 0.81, 0.83, 7.0, 9)])
    class St:
        D = types.SimpleNamespace(x=1)
        def __init__(s, res): s.res = res
        def run_segment(s, k, L, t_arr, t_end, rem, v): return s.res
    mk = lambda res, d: RV.EngineBloqueoDelta(St(res), d, fuente=lambda k: (own, comp))
    assert mk((0.0, None, 'ok'), 2.0).run_segment(0, 0.19, t0, t0 + 5000, 5.0, 'BASE') == (2.0, t0 + 1000, 'ok')                  # bloqueo: min(rem=5, nivel=7, delta=2)
    assert mk((0.0, None, 'ok'), 10.0).run_segment(0, 0.19, t0, t0 + 5000, 5.0, 'BASE')[0] == 5.0                                  # delta mayor que el restante: sin cambio
    W = mk((5.0, t0 + 500, 'ok'), 2.0); assert W.run_segment(0, 0.19, t0, t0 + 5000, 5.0, 'BASE')[0] == 5.0                        # relleno por print previo: NO se recorta
    for bad in (None, nan, 0.0, 1e-4):
        try: RV.EngineBloqueoDelta(St((0.0, None, 'ok')), bad); assert False
        except ValueError: pass
def test_dry_un_mercado_base_v5_v1_dentro_del_replay():
    ctx = ctx_stub(); Rb, cb = FB.corre_variante(ctx, ctx['dia'], 'base', None, 0); assert cb['rellenos'] == 1 and len(Rb) == 1 and Rb.f5t.notna().all() and Rb.tercil.iloc[0] == 'bajo' and Rb.variante.iloc[0] == 'base'
    tf = int(Rb.tf.iloc[0]); tau = tf - 94; bsrc = {'eth': (np.array([tau - 1500, tau], np.int64), np.array([100.0, 99.9]))}
    ctx = ctx_stub(bsrc=bsrc); R5, c5 = FB.corre_variante(ctx, ctx['dia'], 'V5', None, 0); assert c5['rellenos'] == 0 and c5['contadores']['vidas_con_disparo'] == 1 and (R5.pnl.sum() == 0)
    base_pnl = float(Rb.pnl.sum()); assert base_pnl != 0 and abs(R5.pnl.sum() - base_pnl) == abs(base_pnl)                                  # el DeltaPnL de V5 = -pnl del relleno evitado
    class M:  # modelo con mu fijo
        def __init__(s, mh, mu): s.v = (np.array([mh]), np.array([mu]))
        def mu(s, X, L): return s.v
    import e1_modelo as E
    def con(mh, mu):
        ctx = ctx_stub(bsrc={'eth': (np.array([t0 - 45000, t0 - 12000], np.int64), np.array([100.0, 100.0]))}); return FB.corre_variante(ctx, ctx['dia'], 'V1', M(mh, mu), 0)
    assert con(0.1, 0.1)[1]['rellenos'] == 1 and con(-0.5, -0.5)[1]['rellenos'] == 0 and con(-0.5, -0.5)[1]['contadores']['bloq_regla'] >= 1                     # V1: mu_ucb < -0,02 no arma
    assert FB.corre_variante(ctx_stub(bsrc={'eth': (np.array([t0 - 45000, t0 - 12000], np.int64), np.array([100.0, 100.0]))}), '2026-11-08', 'V4', M(-0.5, 0.1), 0)[1]['rellenos'] == 0       # V4 usa mu_hat
def test_puntos_dia_flags_y_pesos():
    ctx = ctx_stub(); Rb, _ = FB.corre_variante(ctx, ctx['dia'], 'base', None, 0); tf = int(Rb.tf.iloc[0]); tau = tf - 300
    ctx = ctx_stub(bsrc={'eth': (np.array([tau - 1500, tau], np.int64), np.array([100.0, 99.9]))}); P = FB.puntos_dia(ctx, Rb, None, 0)
    assert len(P) > 5 and abs(P.w_orden.sum() - 1.0) < 1e-9 and P.fire_V5.sum() == 1 and P.t[P.fire_V5].iloc[0] >= tau and P.t[P.fire_V5].iloc[0] - tau < 250 and not P.fire_V5.iloc[0] and P.relleno.all() and P.score_ucb.isna().all() and (P.pnl_orden == Rb.pnl.iloc[0]).all()
    assert P.t.max() + 74 + 20 <= tf                                                                                                       # solo puntos desde los que cancelar es efectivo
def test_tabla_variantes_ev_incondicional_ponderado_y_delta():
    R = pd.DataFrame(dict(variante=['base'] * 4 + ['V1'] * 4, dia=['d1', 'd1', 'd2', 'd2'] * 2, q=[5, 0, 5, 5, 5, 0, 0, 5], cost=[1.0, 0, 1.0, 3.0, 1.0, 0, 0, 3.0], pnl=[-1.0, 0, 0.5, -1.0, -1.0, 0, 0, -1.0], mid=list('abcd') * 2, k=[0] * 8))
    T = FB.tabla_variantes(R); b, v = T['base'], T['V1']; assert abs(b['EV_eur'] - (-1.5 / 5)) < 1e-12 and b['p_relleno'] == 0.75 and abs(b['EV_incond_por_mercado_lado'] + 0.375) < 1e-12 and b['n_mercado_lado_base'] == 4 and abs(b['EV_cond_por_unidad'] - np.mean([-1, 0.5, -1 / 3])) < 1e-12
    assert v['delta_pnl_vs_referencia']['total'] == -0.5 and v['delta_pnl_vs_referencia']['n_dias'] == 2 and b['delta_pnl_vs_referencia'] is None and v['rellenos'] == 2 and abs(v['EV_incond_por_mercado_lado'] + 0.5) < 1e-12                              # d2: -1 frente a -0,5 de la base (se cancelo un relleno bueno); d1 igual
    one = FB.ic90_dias({'d1': 1.0}); assert one['nota'] == 'INSUFFICIENT' and np.isnan(one['lo'])
def fake_pts(d, n_ord=30, seed=0):
    rng = np.random.default_rng(seed); rows = []
    for o in range(n_ord):
        fill = rng.random() < 0.6; pnl = (-1.0 if rng.random() < 0.5 else 0.5) if fill else 0.0
        for j in range(4): rows.append(dict(dia=d, ord_id=f'{d}|m{o}|0', es_alta=(j == 0), gate_f5=False, suelo='lo', relleno=fill, y=int(rng.random() < .5), **{f: 0.5 for f in E1.FEATS_ALL}, t=t0 - 5000 - 300 * j, tf=t0 if fill else nan, fin=FIN, coin='eth', nivel=0.2, pnl_orden=pnl, score_ucb=rng.normal(), score_mu=rng.normal(), fire_V5=bool(rng.random() < .1), fire_V6=bool(rng.random() < .1), L=0.2))
    return pd.DataFrame(rows)
FIN = TB.FIN
def test_final_parcial_con_dia_faltante_y_checkpoint_por_codigo():
    def fn_for(d):
        def fn(dd):
            R = pd.DataFrame(dict(variante=['base', 'V1'] * 3, dia=d, q=[5.0, 0, 5.0, 5.0, 0, 0], cost=[1.0, 0, 1.0, 1.0, 0, 0], pnl=[-1.0, 0, .5, -1., 0, 0], mid=list('aabbcc'), k=0, horq='H0', estrato='lo')); FB.atomic_pkl(FB.OUT + f'fb_var_{d}.pkl', R); FB.atomic_pkl(FB.OUT + f'fb_pts_eval_{d}.pkl', fake_pts(d)); FB.atomic_json(FB.OUT + f'fb_cov_var_{d}.json', dict(ok=1)); return dict(ok=1), dict(ok=1, e1_sha=FB.sha(FB.OUT + 'fb_e1.pkl'))
        return fn
    open(FB.OUT + 'fb_e1.pkl', 'wb').write(b'e1-v1'); FB.EVAL = ['2026-11-08', '2026-11-09']; d = FB.EVAL[0]; outs = [f'fb_var_{d}.pkl', f'fb_pts_eval_{d}.pkl', f'fb_cov_var_{d}.json']
    assert FB.RU.job('variantes', d, outs, fn_for(d), {'x': HV + 'fase_b_run.py'}) == 'COMPLETE'; assert FB.final() == 'PARTIAL'                          # falta el 09-Nov: nunca COMPLETE
    m = json.load(open(FB.OUT + 'run_manifest.json')); r = json.load(open(FB.OUT + 'fb_resultado.json')); assert m['status'] == 'PARTIAL' and m['estado_por_dia']['2026-11-09'] == 'MISSING' and 'DIAGNOSTICO' in m['etiqueta']
    assert set(r['variantes']) == {'base', 'V1'} and r['familia6']['K'] == 1000 and len(r['familia6']['obs']) == 6 and r['horquilla_bloqueo']['V1']['etiqueta'] == 'NO ROBUSTO AL BLOQUEO' and set(r['por_estrato']) == {'lo'}
    open(FB.OUT + 'fb_e1.pkl', 'wb').write(b'e1-v2'); assert not FB.RU.ya_completo('variantes', d, outs); assert FB.final() == 'PARTIAL' and json.load(open(FB.OUT + 'run_manifest.json'))['estado_por_dia'][d].startswith('FAILED')      # (5) otro e1 -> las variantes no valen
    open(FB.OUT + 'fb_e1.pkl', 'wb').write(b'e1-v1'); assert FB.RU.ya_completo('variantes', d, outs)
    orig = FB.code_hashes; FB.code_hashes = lambda: dict(orig(), **{'fase_b_run.py': 'x' * 64}); FB.RU.code_hashes = FB.code_hashes
    try: assert not FB.RU.ya_completo('variantes', d, outs)                                                                                         # codigo distinto: checkpoint invalido
    finally: FB.code_hashes = orig; FB.RU.code_hashes = orig
def test_carga_binance_orden_recv_ventana_y_monedas():
    d = '2026-11-08'; import calendar, time; d0 = calendar.timegm(time.strptime(d, '%Y-%m-%d')) * 1000; os.makedirs(TMP + '/m5', exist_ok=True)
    rows = [f'x,{d0},ETHUSDT,100.0,1,0,{d0},{d0 + 500}', f'x,{d0},ETHUSDT,101.0,1,0,{d0},{d0 + 300}', f'x,{d0},BTCUSDT,5.0,1,0,{d0},{d0 + 100}', f'x,{d0},XRPUSDT,1.0,1,0,{d0},{d0 - 20_000_000}', f'k,{d0},id,ETH,5min,1,2026,YES', f'x,{d0},SOLUSDT,2.0,1,0,{d0},{d0 + 900}']
    with gzip.open(TMP + f'/m5/m5_registro_{d}.csv.gz', 'wt') as f: f.write('\n'.join(rows) + '\n')
    FB.M5 = TMP + '/m5/m5_registro_%s.csv.gz'; B = FB.carga_binance(d); assert set(B) == {'eth', 'sol'} and list(B['eth'][0]) == [d0 + 300, d0 + 500] and list(B['eth'][1]) == [101.0, 100.0]       # ordenado por recepcion; BTC y fuera de ventana fuera
def test_script_guardas_t_proc_condiciones_prereg_y_pid():
    d = tempfile.mkdtemp(dir=TMP); o = d + '/o/'; ch = d + '/c'; base = dict(os.environ, FB_OUT=o, P0_CHAIN=ch, P0_HM='1300', P0_RAM_MIN='1', P0_ESPERA='0', FB_T_PROC_MS='0')
    def run(env): return subprocess.run(['bash', HV + 'run_fase_b.sh'], env=env, capture_output=True, text=True, timeout=60)
    def log(): return ''.join(open(o + f).read() for f in os.listdir(o) if f.endswith('.log'))
    open(ch, 'w').write('COMPLETE'); e = {k: v for k, v in base.items() if k != 'FB_T_PROC_MS'}; p = run(e); assert p.returncode == 3 and 'FB_T_PROC_MS' in p.stdout                    # t_proc obligatorio
    for kw in (dict(P0_HM='0700'), dict(P0_HM='1100'), dict(P0_RAM_MIN='999999999')):
        os.makedirs(o, exist_ok=True); p = run(dict(base, **kw)); assert p.returncode == 3 and 'BLOQUEADO' in log(), kw
    open(ch, 'w').write('RUNNING'); p = run(base); assert p.returncode == 3
    h = subprocess.Popen(['flock', o + '.lock', 'sleep', '3']); import time; time.sleep(0.4); os.remove(o + 'run.pid') if os.path.exists(o + 'run.pid') else None
    p = run(base); h.wait(); assert p.returncode == 2 and not os.path.exists(o + 'run.pid')                                                                                          # PID solo tras el flock
    pd_ = d + '/pre/'; os.makedirs(pd_); V_ = os.path.dirname(HV.rstrip('/')) + '/'
    for f in os.listdir(V_):
        if f.startswith(('PREREG_R1v2_19nov', 'CONTRATO_R1v2_19nov_v2')) and f.endswith(('.md', '.sha256')): shutil.copy(V_ + f, pd_ + f)
    open(pd_ + 'PREREG_R1v2_19nov.md', 'a').write('x'); open(ch, 'w').write('COMPLETE'); p = run(dict(base, P0_PREREG_DIR=pd_)); assert p.returncode == 3 and 'PREREG' in p.stdout + log()
    src = open(HV + 'run_fase_b.sh').read(); assert 'run base $d' in src and 'run entrena' in src and 'run variantes $d' in src and src.count('cond_ok') >= 3 and 'ulimit -v 3000000' in src and 'ADENDA_07' in src and 'run l2 $d' in src and src.count('|| aborta') >= 4 and src.index('ventana_ok') < src.index('>>> $*')                 # (5) aborta si falla base/entrena; (8) ventana 06-09:15Z re-chequeada en cada paso; ADENDA_07 en prereg_ok
def test_fix1_fin_esalta_gate_en_puntos_y_suelo_en_ordenes():
    ctx = ctx_stub(); Rb, _ = FB.corre_variante(ctx, ctx['dia'], 'base', None, 0); P = FB.puntos_dia(ctx, Rb, None, 0)
    assert (P.fin == FIN).all() and P.es_alta.sum() == 1 and bool(P.es_alta.iloc[0]) and 'gate_f5' in P and not P.gate_f5.any() and (P.suelo == 'sin_tabla').all() and Rb.estrato.iloc[0] == 'sin_tabla'       # (1) fin real, (3) estrato por ventana
    import puerta0_core as P0; W = P0.W_MS; w0 = int(Rb.t_dec.iloc[0]) // W * W
    tab = pd.DataFrame(dict(dia=['2026-11-08'], coin=['eth'], w0_ms=[w0], clase_estrato=['lo'])); FB._TS['x'] = (tab, P0.celdas_validas(tab, n_min=1, frac_lo=0.5))
    try: R2, _ = FB.corre_variante(ctx_stub(), '2026-11-08', 'base', None, 0); assert R2.estrato.iloc[0] == 'lo'
    finally: FB._TS.clear()
def test_fix2_familia_v1_v4_solo_alta_con_gate_f5():
    import familia6 as F6
    P = pd.DataFrame(dict(es_alta=[True, False, True, False], gate_f5=[False, False, True, False], score_ucb=[-1, -1, np.nan, -1.0], score_mu=[0.5, -1, np.nan, -1.0], fire_V5=False, fire_V6=False)); F = F6.fire_matrix(P)
    assert F[:, 0].tolist() == [True, False, True, False] and F[:, 3].tolist() == [False, False, True, False]            # en vida NO dispara V1-V4; gate F5 dispara aunque el score sea NaN
    assert F6.eff_matrix(pd.DataFrame(dict(t=[0, 0], tf=[nan, nan], es_alta=[True, False])), 0)[:, 0].tolist() == [True, False]
def test_fix4_horquilla_signo_en_tres_motores():
    mk = lambda h, pv, pb: [dict(variante='V1', horq=h, pnl=pv), dict(variante='base', horq=h, pnl=pb)]
    R = pd.DataFrame(sum([mk('H0', 1.0, -1.0), mk('HD', 0.5, -1.0), mk('HN', 2.0, -1.0)], [])); assert FB.horquilla(R)['V1']['mantiene_signo'] and FB.horquilla(R)['V1']['etiqueta'] is None
    R = pd.DataFrame(sum([mk('H0', 1.0, -1.0), mk('HD', -1.5, -1.0), mk('HN', 2.0, -1.0)], [])); assert FB.horquilla(R)['V1']['etiqueta'] == 'NO ROBUSTO AL BLOQUEO'
    assert FB.DELTA_CENTRAL == 9.07 and FB.HORQ == ('H0', 'HD', 'HN')
def test_fix5_variantes_exige_entrena_y_exit_codes():
    try: FB.run_variantes('2026-11-08'); assert False
    except RuntimeError as e: assert 'entrena COMPLETE' in str(e)
    env = dict(os.environ, FB_OUT=TMP + '/ec/', FB_T_PROC_MS='0'); p = subprocess.run(['python3', HV + 'fase_b_run.py', 'base', '2026-11-08'], env=env, capture_output=True, text=True, timeout=300); assert p.returncode == 4, p.stdout + p.stderr   # BLOCKED (falta l2ev) = 4 -> el .sh aborta
def test_fix6_control_mismos_eventos_sin_regla():
    ctx = ctx_stub(); Rb, _ = FB.corre_variante(ctx, ctx['dia'], 'base', None, 0); tf = int(Rb.tf.iloc[0]); tau = tf - 94
    ctx = ctx_stub(bsrc={'eth': (np.array([tau - 1500, tau], np.int64), np.array([100.0, 99.9]))}); h5 = FB.hook_de('V5', ctx, None, 0); hc = FB.hook_de('ctl_V5', ctx, None, 0); m = types.SimpleNamespace(coin='eth', fin=int(FIN))
    assert np.array_equal(h5.extra_events(m, 20), hc.extra_events(m, 20)) and not hc.no_armar(m, 0, 0, 0.2) and not hc.cancela(m, {}, 0)
    Rc, cc = FB.corre_variante(ctx, ctx['dia'], 'ctl_V5', None, 0); assert cc['rellenos'] == 1 and cc['contadores'] == {} and Rc.variante.iloc[0] == 'ctl_V5'                  # el control NO cancela
def test_fix7_t_end_ancla_max_tau_trx_y_clave_por_orden():
    h = RV.HookBase(); o = dict(k=0, L=0.19, t_arr=1000, tf1=None); assert h._t_end(o, 1000, 4000, 0, 74) == 4000 + 74 + 19 and h._t_end(o, 4000, 1000, 0, 74) == 4000 + 74 + 19
    m = types.SimpleNamespace(mid='m1'); assert h.key(m, dict(n_ord=0)) != h.key(m, dict(n_ord=1)) and h.key(m, dict(n_ord=0)) == h.key(types.SimpleNamespace(mid='m1'), dict(n_ord=0))
def test_fix8_binance_arrays_y_pesos_tras_nan():
    P = pd.DataFrame(dict(ord_id=['a', 'a', 'a', 'b'], y=[1, 1, 1, 0])); w = E1.pesos_orden(P); assert abs(w[:3].sum() - 1) < 1e-12 and w[3] == 1.0                                  # minor: cada orden suma 1 tras excluir NaN
def test_fix6b_fire_v5_usa_funciones_del_hook_no_armar_en_alta_y_primer_disparo_desde_llegada():
    ctx = ctx_stub(); Rb, _ = FB.corre_variante(ctx, ctx['dia'], 'base', None, 0); o = Rb.iloc[0]; td = int(o.t_dec); ta = int(o.t_arr)
    ctx = ctx_stub(bsrc={'eth': (np.array([td - 2500, td - 1000], np.int64), np.array([100.0, 99.9]))}); P = FB.puntos_dia(ctx, Rb, None, 0)        # tick adverso en la ventana de no armar del alta
    assert bool(P.fire_V5.iloc[0]) and P.es_alta.iloc[0] and P.fire_V5.sum() == 1                                                                   # no-armar representado en el alta; el tick previo a t_arr NO cuenta como cancelacion en vida
    ctx = ctx_stub(bsrc={'eth': (np.array([ta - 1500, ta - 100], np.int64), np.array([100.0, 99.9]))}); P = FB.puntos_dia(ctx, Rb, None, 0); assert not P.fire_V5.iloc[1:].any() or P.t[P.fire_V5].min() >= ta
def test_seguridad():
    src = open(HV + 'fase_b_run.py').read() + open(HV + 'replay_variantes.py').read()
    for p in ('post_order', 'create_order', 'py_clob_client', 'dotenv', 'live/.env', 'private_key', 'requests.', 'urlopen', 'pkill', 'pgrep', 'c[6]'): assert p not in src, p
if __name__ == '__main__':
    ts = [(n, f) for n, f in sorted(globals().items()) if n.startswith('test_') and callable(f)]
    try:
        for n, f in ts: f(); print('OK', n)
        print(len(ts), 'tests OK')
    finally: shutil.rmtree(TMP, ignore_errors=True)
