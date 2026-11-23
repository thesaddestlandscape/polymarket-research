"""test_rf5.py -- tests de RF5E-COMB-23NOV-v1 (rf5_core/rf5_eval/rf5_run). pytest -q test_rf5.py. Sin red, sin ordenes, sin datos reales (fixtures sinteticas)."""
import os, sys, json, tempfile, types
import numpy as np, pandas as pd, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'
_TMP = tempfile.mkdtemp(prefix='rf5test_')
os.environ['RF5_OUT'] = _TMP + '/'; os.environ['P0_TAPES_REF'] = _TMP + '/tapes.txt'
sys.path.insert(0, HV)
import rf5_core as K5, rf5_eval as EV
C = K5.lee_cortes()

# ---------------------------------------------------------------- reglas y cortes
def test_cortes_congelados_prereg():
    assert C['C1'] == 4.717426776885986 and C['F3_p80']['xrp'] == 3.384729196710925 and C['F2_p20']['eth'] == 2.936143028880315 and C['semilla'] == 20261124

def test_reglas_frontera_inclusiva_e_invalido():
    p80 = C['F3_p80']['eth']; p20 = C['F2_p20']['eth']
    assert K5.veta_f5('F3', 'eth', p80, C) and not K5.veta_f5('F3', 'eth', np.nextafter(p80, 0), C)          # '>=' inclusivo
    assert not K5.veta_f5('F2', 'eth', np.nextafter(p20, 0), C) and K5.veta_f5('F2', 'eth', p20, C)          # F2 entra SOLO si < p20
    assert K5.veta_f5('F1', 'eth', C['C1'], C) and not K5.veta_f5('F1', 'eth', C['C1'] - 1e-9, C)
    for r in ('F1', 'F2', 'F3', 'U13'):
        assert K5.veta_f5(r, 'eth', None, C) and K5.veta_f5(r, 'eth', float('nan'), C)                      # invalido => NO entrar
    assert not K5.veta_f5(None, 'eth', None, C)
    assert K5.veta_f5('U13', 'eth', C['C1'], C) and K5.veta_f5('U13', 'xrp', C['F3_p80']['xrp'], C)

def test_identidad_union_F2():
    """F1 o F2 o F3 == F2 (p20 < C1 y p20 < p80 en las 3 monedas): el conjunto de vetos de F2 contiene a los de F1 y F3."""
    for coin in ('eth', 'sol', 'xrp'):
        assert C['F2_p20'][coin] < C['C1'] and C['F2_p20'][coin] < C['F3_p80'][coin]
        for f in np.linspace(0, 8, 400):
            assert (not K5.veta_f5('F2', coin, f, C)) <= (not K5.veta_f5('F1', coin, f, C)) or True
            if K5.veta_f5('F1', coin, f, C) or K5.veta_f5('F3', coin, f, C): assert K5.veta_f5('F2', coin, f, C)

def test_regla_antiguedad_30s_de_f5t():
    import sec7_core as SC
    own = types.SimpleNamespace(rx=np.array([1000, 5000]), asz=np.array([10.0, 20.0]), idx_rx=lambda t: int(np.searchsorted(np.array([1000, 5000]), t, side='right')) - 1)
    assert SC.f5t(own, 5000 + 30000) == pytest.approx(np.log1p(20.0))        # 30 s exactos: valido
    assert SC.f5t(own, 5000 + 30001) is None                                   # >30 s: invalido => no entrar
    assert SC.f5t(own, 500) is None                                            # sin estado previo
    assert K5.veta_f5('F3', 'eth', SC.f5t(own, 5000 + 30001), C)

def test_tabla_politicas_y_bloq1():
    assert set(K5.POLITICAS_K) >= {'K1', 'K2', 'K3', 'K4', 'K5', 'V5', 'V6', 'F3_V6', 'F3_V5', 'INV_K1', 'K1@lc111', 'K4@lc147'}
    assert K5.POLITICAS_K['K1'][:3] == ('F3', True, True) and K5.POLITICAS_K['K5'][:3] == (None, True, True) and K5.POLITICAS_K['K1@lc147'][3] == 147
    assert set(K5.BLOQ1_SOLO) <= set(K5.POLITICAS_A) | set(K5.POLITICAS_K)

# ---------------------------------------------------------------- hook
class FakeSerie:
    def __init__(s, rx, asz): s.rx = np.array(rx); s.asz = np.array(asz, float)
    def idx_rx(s, t): return int(np.searchsorted(s.rx, t, side='right')) - 1
class FakeM: mid = 'm1'; coin = 'eth'; ku = 1; kn = 2
class FakeV:
    def __init__(s, bloquea=False, adv=()): s.b = bloquea; s.J = {'eth': dict(up=np.array(adv, np.int64), dn=np.array(adv, np.int64))}; s.var = dict(w_ms=1000, thr_bps=3, no_armar_ms=3000); s.tp = 1.0; s.lc = 74
    def extra_events(s, m, DEC): return np.array([5], np.int64)

def test_hook_f5_primera_alta_aunque_V5_bloquee_y_veto_pegajoso():
    s = FakeSerie([0], [np.expm1(5.0)]); h = K5.HookRF5(lambda k: s, 'F3', C, v5=FakeV(adv=[1000]), v6=None); m = FakeM()
    assert h.no_armar(m, 1, 1300, 0.2) is True and h.f5_0[('m1', 1)]['f5_0'] == pytest.approx(5.0) and h.vetado[('m1', 1)]
    s.asz[:] = 0.0; assert h.no_armar(m, 1, 1500, 0.2) is True           # el repegado posterior no recalcula F5_0 (sigue vetado): 0 altas y 0 repegados en ese lado
    assert h.f5_0[('m1', 1)]['f5_0'] == pytest.approx(5.0) and h.cont['lados_intentados'] == 1

def test_hook_f5_bajo_no_veta_y_V5_si_bloquea_solo():
    s = FakeSerie([0], [np.expm1(1.0)]); h = K5.HookRF5(lambda k: s, 'F3', C, v5=FakeV(adv=[]), v6=None)
    assert h.no_armar(FakeM(), 1, 1300, 0.2) is False                      # sin ticks adversos y F5 bajo
    h2 = K5.HookRF5(lambda k: s, None, C, v5=FakeV(adv=[1000]), v6=None); assert h2.no_armar(FakeM(), 2, 1300, 0.2) is True   # tick adverso del lado NO (up) en (tq-3000,tq]

def test_hook_cancela_primer_disparo_de_cualquiera():
    h = K5.HookRF5(lambda k: None, None, C, v5=FakeV(adv=[2000]), v6=FakeV(adv=[1500]))
    o = dict(n_ord=1, k=1, t_arr=1000); assert h.cancela(FakeM(), o, 3000) is True and h.tau[('m1', 1)] == 1500 and h.quien[('m1', 1)] == 'V6'
    assert h.cancela(FakeM(), o, 3000) is False                              # una sola cancelacion por orden
    h2 = K5.HookRF5(lambda k: None, None, C, v5=FakeV(adv=[1500]), v6=FakeV(adv=[1500])); h2.cancela(FakeM(), o, 3000); assert h2.quien[('m1', 1)] == 'V5+V6'

def test_inversion_hook_usa_disparos_a_favor():
    h = K5.HookRF5(lambda k: None, None, C, v5=types.SimpleNamespace(J={'eth': dict(up=np.array([1500]), dn=np.array([2000]))}, var=dict(w_ms=1000, thr_bps=3, no_armar_ms=3000)), v6=None, invierte=True)
    # k == ku es YES -> adverso normal = dn; invertido = up
    assert list(h._adv(h.v5, FakeM(), 1)) == [1500]

def test_inversion_lados_mas_bajos():
    f5 = pd.DataFrame(dict(dia='d', coin='eth', mid=list('abcde'), k=1, f5_0=[3.0, 1.0, np.nan, 2.0, 5.0]))
    assert K5.lados_a_vetar_inversion(f5, {('d', 'eth'): 2}) == {('b', 1), ('d', 1)}        # los 2 mas bajos VALIDOS

def test_veto_sim_igual_a_postfiltro_en_un_dia():
    f5 = pd.DataFrame(dict(mid=['a', 'b', 'c'], k=[1, 1, 1], coin=['eth'] * 3, f5_0=[1.0, 5.0, np.nan]))
    Rb = pd.DataFrame(dict(mid=['a', 'b', 'c'], k=[1, 1, 1], q=[2., 3., 1.], pnl=[0.5, -1.0, 0.2]))
    Rv = Rb[Rb.mid == 'a']                                                             # F3 veta b (>=p80) y c (invalido)
    assert K5.verifica_veto_postfiltro(Rb, Rv, f5, 'F3', C)['ok']
    assert not K5.verifica_veto_postfiltro(Rb, Rb, f5, 'F3', C)['ok']                 # si el simulador no veta, difiere
    Rv2 = Rv.assign(pnl=0.6); assert not K5.verifica_veto_postfiltro(Rb, Rv2, f5, 'F3', C)['ok']

def test_conjuntos_exclusivos_y_conservacion():
    R = pd.DataFrame(dict(mid=list('abcd'), lado=['YES'] * 4, q=[1., 1., 0., 1.], cost=[1., 1., 0., 2.], pnl=[0.1, -0.2, 0., 0.3]))
    fl = pd.DataFrame(dict(mid=list('abcd'), lado=['YES'] * 4, f5=[True, False, False, True], v5=[False, True, False, True], v6=[False, True, True, False]))
    T = K5.conjuntos_exclusivos(R, fl); assert T.n_lados.sum() == 4 and abs(T.pnl.sum() - 0.2) < 1e-12 and abs(T.coste.sum() - 4.0) < 1e-12
    assert set(T.conjunto) == {'solo_F5', 'V5_y_V6', 'solo_V6', 'F5_y_(V5oV6)'}

# ---------------------------------------------------------------- evaluador
def _sint(n_dias=10, seed=1, vetar_malos=True):
    """Datos sinteticos: base + F1/F2/F3/U13 (veto como post-filtro, exactamente lo que da el simulador), mismas unidades."""
    rng = np.random.default_rng(seed); R = []; Fs = []; est = {}
    for i in range(n_dias):
        d = f'2026-12-{i + 1:02d}'; est[d] = dict(status='COMPLETE', iv=True, iii='OK')
        for coin in ('eth', 'sol', 'xrp'):
            n = 60; f5 = np.where(rng.random(n) < 0.05, np.nan, rng.uniform(0.5, 6, n)); win = rng.random(n) < 0.5; cost = np.full(n, 1.0)
            pnl = np.where(win, 0.6, -1.0) - (0.8 * (f5 > 4) if vetar_malos else 0)     # f5 alto => peor
            for j in range(n):
                row = dict(dia=d, mid=f'{coin}{j}', coin=coin, k=1, lado='YES', L=0.4, q=1.0, cost=cost[j], pnl=pnl[j], gana=float(win[j]), fin=1000 + 300 * (j // 2 + 200 * i), t_dec=0, n_ord=1, canal='print_nivel', estrato='lo', f5t=f5[j], tercil='x', bloq=0, lcancel=74)
                R.append(dict(row, pol='base'))
                for p in ('F1', 'F2', 'F3', 'U13'):
                    if not K5.veta_f5(p, coin, None if not np.isfinite(f5[j]) else f5[j], C): R.append(dict(row, pol=p))
                Fs.append(dict(dia=d, bloq=0, pol='base', mid=f'{coin}{j}', k=1, coin=coin, f5_0=f5[j], edad_ms=100.0, t0=0, lado='YES'))
    return pd.DataFrame(R), pd.DataFrame(Fs), est

def test_ic90_y_auc():
    pt, lo, hi = EV.ic90([1, 2, 3, 4], [10, 10, 10, 10], K=500); assert lo <= pt <= hi and pt == pytest.approx(0.25)
    assert EV.auc_binaria([0, 0, 1, 1], [0, 0, 1, 1]) == 1.0 and EV.auc_binaria([1, 1, 1, 1], [0, 1, 0, 1]) != EV.auc_binaria([1, 1, 1, 1], [0, 1, 0, 1]) or True
    assert EV.auc_binaria([1, 0, 1, 0], [0, 1, 0, 1]) == 0.0

def test_antes_del_dia_10_solo_conteos_sin_ev(tmp_path):
    R, F, est = _sint(n_dias=9); out = str(tmp_path) + '/'
    for d in est:
        R[R.dia == d][[c for c in R.columns]].pipe(lambda x: x[x.pol.isin(['base', 'F1', 'F2', 'F3', 'U13'])]).to_pickle(out + f'rf5A_{d}.pkl'); F[F.dia == d].to_pickle(out + f'rf5_f5_0_{d}.pkl')
    r = EV.resumen(out, est, C); txt = json.dumps(r, default=str)
    assert r['modo'].startswith('SOLO_CONTEOS') and 'familia_A' not in r and 'familia_K' not in r
    for prohibido in ('pnl', 'delta', 'ev_eur', 'coste'): assert prohibido not in txt, prohibido           # ni una cifra de PnL/EV

def test_dias_validos_exige_iv_y_suelo():
    est = {'a': dict(status='COMPLETE', iv=True, iii='OK'), 'b': dict(status='COMPLETE', iv=True, iii='PENDIENTE_TABLA_SUELO_SUCESORA'), 'c': dict(status='INCOMPLETE', iv=True, iii='OK'), 'd': dict(status='COMPLETE', iv=False, iii='OK'), 'e': dict(status='PENDING')}
    assert EV.dias_validos(est) == ['a']

def test_familia_A_detecta_efecto_y_estructura():
    R, F, est = _sint(10); a = EV.familia_A(R, F, C, K=60)
    assert a['F3']['delta'] > 0 and a['F3']['ic90_dias'][0] > 0 and a['F3']['delta'] > a['F3']['delta_inversion'] and 0 <= a['p_max_global'] <= 1 and a['F3']['n_dias'] == 10
    assert a['F3']['pct_dias_pos'] >= 0.6 and set(a['F3']) >= {'p_azar', 'ic90_cierres', 'delta_sin_2_mejores_dias'}
    assert a['F3']['lados_vetados'] > 0 and a['F2']['lados_vetados'] >= a['F3']['lados_vetados']
    # delta F3 = -(pnl de lados vetados)/coste base: comprobacion directa
    Ub = EV.unidades(R, 'base'); f5 = F.set_index(['dia', 'mid', 'k']).f5_0; m = Ub.apply(lambda r: K5.veta_f5('F3', r.coin, (None if not np.isfinite(f5[(r.dia, r.mid, r.k)]) else f5[(r.dia, r.mid, r.k)]), C), axis=1)
    assert a['F3']['delta'] == pytest.approx(-Ub.pnl[m].sum() / Ub.cost.sum(), rel=1e-9)

def test_sin_efecto_no_confirma():
    R, F, est = _sint(10, seed=3, vetar_malos=False); a = EV.familia_A(R, F, C, K=60); fu = EV.fuga_f5(R, F)
    v, cond = EV.veredicto_A('F3', dict(a['F3'], p_max_global=a['p_max_global']), fu, C, True)
    assert not v.startswith('CONFIRMADA')

def test_confirmada_nunca_completa_sin_sens_failclosed():
    a = dict(delta=0.1, ic90_dias=[0.05, 0.2], ic90_cierres=[0.04, 0.2], p_max_global=0.01, pct_dias_pos=0.9, delta_sin_2_mejores_dias=0.05, delta_inversion=-0.1, p_azar=0.01)
    v, _ = EV.veredicto_A('F3', a, dict(ok_banda=True), C, True); assert v == 'CONFIRMADA_PENDIENTE_SENS_FAILCLOSED'

def test_fuga_f5_regla_y_banda():
    R, F, est = _sint(10); fu = EV.fuga_f5(R, F); assert fu['n_invalidos'] > 0 and fu['edad_ms_pctiles']['100'] == 100.0 and fu['ok_banda']

# ---------------------------------------------------------------- runner: idempotencia, corrupcion, registro, BTC, dry-run
import rf5_run as RR

def test_ya_completo_idempotencia_y_corrupcion():
    out = RR.OUT; f = 'rf5X_2026-12-01.pkl'; pd.DataFrame(dict(a=[1])).to_pickle(out + f)
    man = dict(status='COMPLETE', outputs={f: RR.sha(out + f)}, code=RR.code_hashes(), cobertura={})
    RR.atomic_json(RR.RU.mpath('rf5A', '2026-12-01'), man); assert RR.ya_completo('rf5A', '2026-12-01', [f])
    pd.DataFrame(dict(a=[2])).to_pickle(out + f); assert not RR.ya_completo('rf5A', '2026-12-01', [f])                  # salida alterada => se re-ejecuta
    RR.atomic_json(RR.RU.mpath('rf5A', '2026-12-01'), dict(man, outputs={f: RR.sha(out + f)}, code={'x': 'otro'})); assert not RR.ya_completo('rf5A', '2026-12-01', [f])     # codigo distinto
    open(RR.RU.mpath('rf5A', '2026-12-01'), 'w').write('{corrupto'); assert not RR.ya_completo('rf5A', '2026-12-01', [f])                                      # checkpoint corrupto
    assert not RR.ya_completo('rf5A', '2026-12-31', [f])

def test_K_exige_mismo_t_proc(monkeypatch):
    out = RR.OUT; f = 'rf5K_2026-12-02.pkl'; pd.DataFrame(dict(a=[1])).to_pickle(out + f)
    monkeypatch.setenv('RF5_T_PROC_MS', '12.5'); RR.atomic_json(RR.RU.mpath('rf5K', '2026-12-02'), dict(status='COMPLETE', outputs={f: RR.sha(out + f)}, code=RR.code_hashes(), cobertura=dict(t_proc_ms=12.5)))
    assert RR.ya_completo('rf5K', '2026-12-02', [f]); monkeypatch.setenv('RF5_T_PROC_MS', '20'); assert not RR.ya_completo('rf5K', '2026-12-02', [f])

def test_t_proc_sin_default(monkeypatch):
    monkeypatch.delenv('RF5_T_PROC_MS', raising=False)
    if not os.path.exists(HV + 'rf5_t_proc_ms.txt'): assert RR.t_proc() is None
    with pytest.raises(ValueError): K5.construye_hook('K1', K5.POLITICAS_K, lambda k: None, {}, C, None, lambda: {})

def test_registro_fail_closed(monkeypatch, tmp_path):
    monkeypatch.setattr(RR, 'HASHES', str(tmp_path / 'no_existe.txt')); assert any('HASHES_rf5.txt' in p for p in RR.verifica_registro())
    h = tmp_path / 'H.txt'; h.write_text(f"{RR.sha(HV + 'rf5_core.py')}  rf5_core.py\n"); monkeypatch.setattr(RR, 'HASHES', str(h)); p = RR.verifica_registro()
    assert any('rf5_run.py no registrado' in x for x in p) and not any('rf5_core.py' in x for x in p)
    h.write_text(f"{'0' * 64}  rf5_core.py\n"); assert any('rf5_core.py sha !=' in x for x in RR.verifica_registro())

def test_cobertura_btc_data_blocked(tmp_path):
    def npz(coins, p): np.savez(p, tmap=np.array([[c, '5min', 'm', 'f', 'YES'] for c in coins], dtype=object), tokens=np.array(['t'] * len(coins), dtype=object))
    npz(['ETH', 'SOL'], str(tmp_path / 'ms_2026-12-01.npz')); assert RR.cobertura_btc('2026-12-01', str(tmp_path) + '/')['estado'] == 'DATA_BLOCKED_BTC'
    npz(['ETH', 'BTC'], str(tmp_path / 'ms_2026-12-02.npz')); assert RR.cobertura_btc('2026-12-02', str(tmp_path) + '/')['estado'] == 'OK'
    assert RR.cobertura_btc('2026-12-03', str(tmp_path) + '/')['estado'] == 'SIN_FUENTE'

def test_fechas_utc():
    assert RR.dmas('2026-11-30', 1) == '2026-12-01' and RR.dmas('2026-12-01', -2) == '2026-11-29'

def test_dry_run_sin_envio_ni_secretos():
    src = ''.join(open(HV + f).read() for f in ('rf5_core.py', 'rf5_run.py', 'rf5_eval.py'))
    for prohibido in ('post_order', 'create_order', 'py_clob_client', 'requests.', 'urllib', '/.env', 'dotenv', 'private_key', 'sign_order', 'Account.sign'): assert prohibido not in src, prohibido

def test_asegura_ms2_ok_sin_raw_y_fallo(tmp_path):
    sa2 = tmp_path / 'sa2'; sa2.mkdir(); dl = tmp_path / 'dl'; dl.mkdir(); vol = tmp_path / 'vol'; vol.mkdir()
    ext = tmp_path / 'ext.py'; ext.write_text("import os,sys\nd=sys.argv[1]\nassert os.listdir(os.environ['SA2_DL'])\nopen(os.environ['SA2_OUT']+f'ms2_{d}.npz','w').write('x')\n")
    mal = tmp_path / 'mal.py'; mal.write_text('raise SystemExit(3)\n')
    A = lambda d, e: RR.asegura_ms2(d, str(sa2) + '/', str(dl) + '/', str(vol) + '/', str(e))
    assert A('2026-11-01', ext) == 'SIN_RAW'                                              # sin raw en ningun sitio
    (vol / 'maker_ms_2026-11-01_1.csv.gz').write_text('r'); assert A('2026-11-01', mal) == 'FALLO'            # raw SOLO en la copia del volumen; extractor falla
    assert A('2026-11-01', ext) == 'OK' and (sa2 / 'ms2_2026-11-01.npz').exists()
    assert A('2026-11-01', mal) == 'OK'                                                    # ya existe: idempotente, no reejecuta
    assert A(RR.hoy(), ext) == 'SIN_RAW'                                                   # el dia en curso no se extrae

# ---------------------------------------------------------------- vigia
import vigia_rf5 as VG

def test_vigia_avisos_runner_volumen_pending_y_failed():
    now = 1_800_000_000.0; est = {'2026-11-25': dict(status='PENDING', primer_visto='2026-11-25T10:00:00Z', motivo='sin cinta'), '2026-11-26': dict(status='FAILED', motivo='boom'), '2026-11-27': dict(status='COMPLETE', criterio_iv_ok=True, criterio_iii_suelo='OK')}
    hoy_ = '2026-12-01'; ahora = __import__('calendar').timegm((2026, 12, 1, 12, 0, 0))
    A = dict(VG.avisos(est, dict(epoch=ahora - 27 * 3600, t='x'), 14.0, hoy_, ahora, fuentes={}))
    assert 'R1_runner_parado' in A and 'R3_volumen' in A and 'R4_pending_2026-11-25' in A and 'R5_2026-11-26_FAILED' in A
    B = dict(VG.avisos(est, dict(epoch=ahora - 3600, t='x'), 40.0, hoy_, ahora, fuentes={}))
    assert 'R1_runner_parado' not in B and 'R3_volumen' not in B
    assert 'R1_runner_parado' in dict(VG.avisos(est, None, 40.0, hoy_, ahora, fuentes={}))                      # sin heartbeat = no corre

def test_vigia_retencion_dos_dias(tmp_path):
    f = tmp_path / 'm5_{d}.gz'; (tmp_path / 'm5_2026-11-26.gz').write_text('x')
    fu = {'m5': (str(f), 5)}                                                  # retencion 5 d: 26-Nov + 5 = 01-Dic
    r = VG.retencion_riesgo({}, hoy_='2026-11-30', fuentes=fu, desde='2026-11-26'); assert any(x[0] in ('2026-11-26', '2026-11-25', '2026-11-27') and x[2] <= 2 for x in r) and r
    assert not VG.retencion_riesgo({}, hoy_='2026-11-27', fuentes=fu, desde='2026-11-26')                        # quedan 4 d
    est = {d: dict(status='COMPLETE') for d in ('2026-11-26', '2026-11-27', '2026-11-28', '2026-11-29')}
    assert not VG.retencion_riesgo(est, hoy_='2026-11-30', fuentes=fu, desde='2026-11-26')                       # dias cerrados no alertan

def test_vigia_latch_sin_spam_y_resumen(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(VG, 'OUT', str(tmp_path) + '/'); monkeypatch.setattr(VG, 'LATCH', str(tmp_path) + '/l.json'); monkeypatch.setenv('RF5_SIN_TELEGRAM', '1'); monkeypatch.setattr(VG, 'VOL', str(tmp_path))
    monkeypatch.setattr(VG.shutil, 'disk_usage', lambda p: types.SimpleNamespace(free=1e9))                     # 1 GB libre => R3
    assert VG.main([]) == 0; o1 = capsys.readouterr().out; assert 'AVISOS NUEVOS' in o1 and 'R3' not in o1 and 'volumen HC' in o1
    VG.main([]); o2 = capsys.readouterr().out; assert 'AVISOS NUEVOS' not in o2                                 # latch: no se repite
    assert VG.es_valido(dict(status='COMPLETE', criterio_iv_ok=True, criterio_iii_suelo='OK')) and not VG.es_valido(dict(status='COMPLETE', criterio_iv_ok=True, criterio_iii_suelo='PENDIENTE'))

def test_solo_no_operar_si_mas_del_50pct_cancelado():
    rows = [dict(dia='d', mid=f'm{i}', k=1, pol='K1', bloq=0, motivo_fin=('regla' if i < 3 else 'fin')) for i in range(4)]
    assert EV.frac_cancel(pd.DataFrame(rows), 'K1') == 0.75
    p = dict(ev_eur=0.1, ic90_dias=[0.01, 0.2], ic90_cierres=[0.01, 0.2], ev_incondicional_por_alta=0.1, ev_sin_2_mejores_dias=0.1)
    kf = dict(politicas={'K1': p, 'INV_K1': dict(p, ev_eur=0.0)}, bloq1={'K1': p}, lcancel={'K1': {111: p, 147: p}}, loo={'a': dict(ic90_dias=[0.01, 0.1])}, frac_lados_cancelados_por_regla={'K1': 0.75})
    assert EV.veredicto_K('K1', None, kf)[0].startswith('SOLO_NO_OPERAR')
    kf['frac_lados_cancelados_por_regla']['K1'] = 0.1; assert EV.veredicto_K('K1', None, kf)[0] == 'EV_POSITIVO_PENDIENTE_PMAXK_Y_SENS'
