"""test_rf5_nulo.py -- ESPEC E4 (DICTAMEN tests 3 y 4): nulo exacto dentro del simulador (replicas) y familia K (desplazamiento circular + re-simulacion, checkpoint, Besag-Clifford). Fixtures sinteticas; 0 EV real."""
import os, sys, json, tempfile
import numpy as np, pandas as pd, pytest
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
os.environ.setdefault('RF5_OUT', tempfile.mkdtemp(prefix='rf5nulo_') + '/')
import rf5_core as K5, rf5_nulo as NU, rf5_eval as EV
C = K5.lee_cortes()

def _mundo(n_dias=6, n=40, seed=0, efecto=True, acople=False):
    """sintetico con replicas: cada mercado tiene lado Up (k=1) y Down (k=2). base intenta Up o Down segun un sorteo; VETO_UP intenta solo Down; VETO_DN solo Up. PnL del lado = f(F5 propio): alto => pierde (efecto)."""
    rng = np.random.default_rng(seed); R = []; F = []
    for i in range(n_dias):
        d = f'2026-12-{i + 1:02d}'
        for j in range(n):
            coin = ('eth', 'sol', 'xrp')[j % 3]; mid = f'{d}_{j}'; fu, fd = rng.uniform(0.5, 6, 2); win = rng.random(2) < 0.5
            pnl = {k: (0.6 if win[k] else -1.0) - (0.8 * (f > 4) if efecto else 0.0) for k, f in enumerate((fu, fd))}; elige = int(rng.random() < 0.5)       # lado que la base intenta (0=Up, 1=Down)
            fila = lambda pol, k, lado: dict(dia=d, mid=mid, coin=coin, k=k, lado=lado, q=1.0, cost=1.0, pnl=pnl[0 if k == 1 else 1], pol=pol, bloq=0, fin=1000 + 300 * (j // 2 + 100 * i), gana=1.0)
            R.append(fila('base', 1 + elige, 'YES' if elige == 0 else 'NO'))
            R.append(fila('VETO_UP', 2, 'NO')); R.append(fila('VETO_DN', 1, 'YES'))
            F.append(dict(dia=d, bloq=0, pol='base', mid=mid, k=1 + elige, coin=coin, f5_0=(fu, fd)[elige], lado='YES' if elige == 0 else 'NO'))
            F.append(dict(dia=d, bloq=0, pol='VETO_UP', mid=mid, k=1, coin=coin, f5_0=fu, lado='YES')); F.append(dict(dia=d, bloq=0, pol='VETO_UP', mid=mid, k=2, coin=coin, f5_0=fd, lado='NO'))
            F.append(dict(dia=d, bloq=0, pol='VETO_DN', mid=mid, k=1, coin=coin, f5_0=fu, lado='YES')); F.append(dict(dia=d, bloq=0, pol='VETO_DN', mid=mid, k=2, coin=coin, f5_0=fd, lado='NO'))
            for r in ('F1', 'F2', 'F3', 'U13'):                                           # replica DIRECTA de cada regla = lo que daria un simulador desacoplado
                vu = K5.veta_f5(r, coin, fu, C); vd = K5.veta_f5(r, coin, fd, C); kk = 1 + elige; vet = vu if elige == 0 else vd
                if not vet: R.append(fila(r, kk, 'YES' if elige == 0 else 'NO'))
                else:
                    otro = vd if elige == 0 else vu                                       # veto del lado elegido: la replica intenta el otro lado si no esta vetado
                    if not otro: R.append(fila(r, 2 if elige == 0 else 1, 'NO' if elige == 0 else 'YES'))
    R = pd.DataFrame(R)
    if acople: R.loc[(R.pol == 'F3') & (R.mid == R.mid.iloc[0]), 'pnl'] += 5.0           # rompe la igualdad compuesta == directa en un mercado
    return R, pd.DataFrame(F)

def test_composicion_reproduce_la_replica_directa_bit_a_bit():
    R, F = _mundo(); v = NU.verifica_composicion(R, F, C)
    assert v['exacto'] and all(x['distintos'] == 0 for x in v['por_regla'].values()) and v['por_regla']['F3']['n_mercados'] == 240

def test_acople_detectado_marca_no_exacto():
    R, F = _mundo(acople=True); nu = NU.nulo_replicas(R, F, C, K=30); assert not nu['exacto'] and nu['estado'].startswith('NO_EXACTO')

def test_f5_0_del_lado_no_intentado_sale_de_la_replica_con_el_otro_lado_vetado():
    R, F = _mundo(n_dias=1, n=3); M = NU.tabla_mercados(R, F)
    for r in M.itertuples():
        assert np.isfinite(r.f_up) and np.isfinite(r.f_dn)                           # ambos lados tienen F5_0 aunque la base solo intentara uno
        b = F[(F.pol == 'base') & (F.mid == r.mid)].iloc[0]; lado_no = 'NO' if b.lado == 'YES' else 'YES'
        src = F[(F.pol == ('VETO_UP' if lado_no == 'NO' else 'VETO_DN')) & (F.mid == r.mid) & (F.lado == lado_no)].f5_0.iloc[0]; assert (r.f_dn if lado_no == 'NO' else r.f_up) == src

def test_p_de_caso_conocido_efecto_fuerte_y_sin_efecto():
    R, F = _mundo(n_dias=10, n=60, seed=1, efecto=True); K = 500; nu = NU.nulo_replicas(R, F, C, K=K)
    assert nu['exacto'] and nu['p_max'] == (1 + nu['exceden']) / (K + 1) and nu['p_max'] <= 0.05                       # formula (1+#)/(K+1), no .mean()
    assert nu['p_max'] != nu['exceden'] / K or nu['exceden'] == 0
    R0, F0 = _mundo(n_dias=10, n=60, seed=1, efecto=False); nu0 = NU.nulo_replicas(R0, F0, C, K=200); assert nu0['p_max'] > 0.05
    F1 = F.assign(f5_0=3.0); Rr, _ = R, None; nu1 = NU.nulo_replicas(R, F1, C, K=50); assert nu1['p_max'] == 1.0 or nu1['exceden'] == 50               # F5_0 constante: toda permutacion da el mismo T => p = (1+K)/(K+1) = 1

def test_p_exacto_con_todas_las_permutaciones_iguales():
    R, F = _mundo(n_dias=4, n=9, seed=2); F2 = F.assign(f5_0=3.5); nu = NU.nulo_replicas(R, F2, C, K=100, h=0); assert nu['p_max'] == (1 + nu['exceden']) / 101 and nu['exceden'] == 100 and nu['p_max'] == 1.0
    nb = NU.nulo_replicas(R, F2, C, K=100, h=20); assert nb['n_perm'] == 20 and nb['exceden'] == 20 and nb['p_max'] == 1.0          # Besag-Clifford: para a las 20 exceedances, p = h/L

def test_familia_A_usa_el_nulo_de_replicas_y_etiqueta_el_postfiltro():
    R, F = _mundo(n_dias=10, n=60, seed=1); a = EV.familia_A(R.assign(coin=R.coin), F, C, K=100)
    assert a['nulo_exacto'] is True and 'p_max_postfiltro' in a and a['p_max_global'] == a['nulo']['p_max']
    cond = EV.veredicto_A('F3', dict(a['F3'], p_max_global=a['p_max_global'], nulo_exacto=False), dict(ok_banda=True), C, True)[1]; assert cond['nulo_exacto'] is False

# ---------------------------------------------------------------- familia K
def test_desplazamiento_circular_conserva_series_y_minimo_60s():
    t = np.arange(0, 86400000, 1000, dtype=np.int64); p = np.arange(len(t), dtype=float); t2, p2 = NU.desplaza_circular(t, p, 0, 123000)
    assert len(t2) == len(t) and np.all(np.diff(t2) >= 0) and set(p2) == set(p) and t2[0] == 0
    assert all(60000 <= NU.delta_perm('2026-12-01', j) <= 86400000 - 60000 for j in range(200)) and NU.delta_perm('d', 3) == NU.delta_perm('d', 3) and NU.delta_perm('d', 3) != NU.delta_perm('e', 3)

def test_besag_clifford_formula():
    assert NU.besag_clifford(20, 200, 1000, 20) == 0.1 and NU.besag_clifford(5, 1000, 1000, 20) == 6 / 1001 and NU.besag_clifford(0, 1000, 1000, 20) == 1 / 1001

def test_nulo_K_run_reanuda_sin_duplicar_y_descarta_linea_corrupta(tmp_path):
    llamadas = []
    def sim(d, delta, j=None): llamadas.append((d, delta)); return {'K1': (delta % 7) / 10.0 - 0.3, 'K2': (delta % 5) / 10.0 - 0.2}
    ck = str(tmp_path / 'ck.jsonl'); r1 = NU.nulo_K_run(['a', 'b', 'c'], 1e300, sim, ck, K=10, h=0); n1 = len(llamadas); assert n1 == 30 and r1['n_perm'] == 10 and r1['p_max'] == 1 / 11 and r1['parada'] == 'K_completo'
    open(ck, 'a').write('{corrupta\n'); llamadas.clear(); r2 = NU.nulo_K_run(['a', 'b', 'c'], 1e300, sim, ck, K=10, h=0); assert llamadas == [] and r2 == r1          # reanudado: 0 re-simulaciones y mismo resultado
    assert sum(1 for l in open(ck) if l.startswith('{"dia"')) == 30                                                                  # sin filas duplicadas (una por dia x permutacion)
    r3 = NU.nulo_K_run(['a', 'b', 'c'], -99.0, sim, str(tmp_path / 'ck2.jsonl'), K=1000, h=20); assert r3['parada'] == 'besag_clifford' and r3['n_perm'] == 20 and r3['p_max'] == 1.0

def test_nulo_K_run_sim_bloque_mismo_resultado_que_por_llamada_y_construye_una_vez_por_bloque(tmp_path):
    def val(d, delta): return {'K1': (delta % 7) / 10.0 - 0.3, 'K2': (delta % 5) / 10.0 - 0.2}
    r_a = NU.nulo_K_run(['a', 'b'], 0.5, lambda d, dl, j: val(d, dl), str(tmp_path / 'a.jsonl'), K=12, h=0); builds = []
    def blq(d, lista): builds.append((d, len(lista))); return {j: val(d, dl) for j, dl in lista}
    r_b = NU.nulo_K_run(['a', 'b'], 0.5, None, str(tmp_path / 'b.jsonl'), K=12, h=0, sim_bloque=blq, bloque=6); assert r_a == r_b and builds == [('a', 6), ('b', 6), ('a', 6), ('b', 6)]
    n = len(builds); NU.nulo_K_run(['a', 'b'], 0.5, None, str(tmp_path / 'b.jsonl'), K=12, h=0, sim_bloque=blq, bloque=6); assert len(builds) == n          # reanudado: nada que simular

def test_permutacion_de_pares_deterministica_conserva_el_par_y_la_moneda():
    M = pd.DataFrame(dict(coin=['eth'] * 5 + ['sol'] * 4, mid=[f'm{i}' for i in range(9)], f_up=np.arange(9) * 1.0, f_dn=np.arange(9) * 10.0))
    a = NU.permuta_pares(M, NU.rng_perm('2026-11-20', 3)); b = NU.permuta_pares(M, NU.rng_perm('2026-11-20', 3)); c = NU.permuta_pares(M, NU.rng_perm('2026-11-20', 4)); assert a == b and a != c
    assert all(abs(fd - 10 * fu) < 1e-9 for fu, fd in a.values())                                             # el par (Up, Down) viaja junto
    assert {a[f'm{i}'][0] for i in range(5)} == set(range(5)) and {a[f'm{i}'][0] for i in range(5, 9)} == set(range(5, 9))   # permuta DENTRO de la moneda

def test_veto_set_de_pares_usa_las_mismas_reglas_que_veta_f5_e_invalido_veta():
    cortes = C; c0 = 'eth'; p80 = cortes['F3_p80'][c0]; pares = {'m1': (p80 + 1.0, 0.0), 'm2': (float('nan'), p80 - 1.0)}
    v = NU.veto_set_de_pares('F3', pares, {'m1': (10, 11), 'm2': (20, 21)}, {'m1': c0, 'm2': c0}, cortes)
    assert v == {('m1', 10), ('m2', 20)}                                                                       # alto => veta; NaN => veta; bajo => no
