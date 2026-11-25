#!/usr/bin/env python3
"""Tests minimos ADENDA_12 (p7/p3 v12). Sin datos reales, sin tasas: extrae por AST las funciones del script (el script corre a nivel de modulo) y las prueba con datos sinteticos.
Uso: python3 -I tests_v12/test_v12.py"""
import ast, gzip, hashlib, pathlib, os, re, sys, tempfile, unittest
import numpy as np, pandas as pd
H = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
def carga(fn, nombres, extra=None):
    tree = ast.parse(pathlib.Path(f'{H}/{fn}').read_text()); body = [n for n in tree.body if (isinstance(n, ast.FunctionDef) and n.name in nombres) or (isinstance(n, ast.Assign) and any(getattr(t, 'id', None) in nombres for t in n.targets))]
    ns = dict(np=np, pd=pd, os=os); exec(compile(ast.Module(body=body, type_ignores=[]), fn, 'exec'), ns); return ns
NOM = ['wm', 'wv', 'smd', 'COV', 'DT', 'rk', 'pxl', 'e3_calc', 'e3_informativo', 'completitud', 'cierre_max_universo', 'sonda1_fns']
N12 = carga('p7_ipw_balance_v12.py', NOM); N11 = carga('p7_ipw_balance.py', NOM)
def sint(seed=1, nw=300, nn=400, outlier=False):
    r = np.random.default_rng(seed)
    def fr(n, nb, off):
        df = pd.DataFrame(dict(act2=r.lognormal(1, 1, n) + off, WA_q=r.gamma(2, 30, n), ttc=r.uniform(0, 3e5, n), absr5=r.exponential(1e-4, n), dist_ticks=r.integers(0, 6, n).astype(float), edad_nivel=r.exponential(5e3, n),
                             om=r.uniform(0.5, 1.5, n), nb=nb, end=r.integers(0, 30, n) * 300000 + 1_000_000))
        return df
    wo = fr(nw, False, 0.0 if outlier else 0.3); wn = fr(nn, True, 0.0)
    if outlier: wo.loc[wo.index[:2], 'act2'] = 1e4
    return pd.concat([wo, wn], ignore_index=True)
class T(unittest.TestCase):
    def test_e3_igual_a_v11_y_determinista(self):
        W = sint(); a = N11['e3_calc'](W); b = N12['e3_calc'](W); c = N12['e3_calc'](W, informativo=True); d = N12['e3_calc'](W, informativo=True)
        self.assertEqual(a, b, 'informativo=False debe ser identico a v11')
        for k in a: self.assertEqual(a[k], c[k], f'campo v11 {k} cambia en v12')
        self.assertTrue(set(c) - set(a) == {'act2_wins_corte_p99', 'SMD_act2_wins_p99', 'E3_IC90_cluster_mercado', 'cov_usadas', 'n_finitos_por_cov', 'n_filas_sin_end'})
        self.assertEqual(c, d, 'bootstrap no determinista')
        ic = c['E3_IC90_cluster_mercado']; self.assertEqual(ic['reps'], 400); self.assertEqual(ic['semilla'], 20261119); self.assertLessEqual(ic['lo'], ic['hi']); self.assertEqual(ic['n_validas'] + ic['descartadas'], 400); self.assertEqual(ic['n_clusters'], int(W.end.nunique()))
    def test_winsor_reduce_outlier(self):
        W = sint(outlier=True); c = N12['e3_calc'](W, informativo=True); raw = c['SMD_pond_om']['a2']      # distribuciones iguales salvo 2 outliers en propios: el SMD crudo sale espurio, el winsorizado ~0
        self.assertLess(abs(c['SMD_act2_wins_p99']), abs(raw)); self.assertLess(abs(c["SMD_act2_wins_p99"]), 0.25); self.assertLess(c['act2_wins_corte_p99'], 1e4)
    def test_no_evaluable_no_agrega(self):
        W = sint(nw=10, nn=400); c = N12['e3_calc'](W, informativo=True); self.assertEqual(c, N11['e3_calc'](W)); self.assertFalse(c['evaluable'])
    def test_estado_global_rng_intacto(self):
        W = sint(); np.random.seed(5); x = np.random.rand(); np.random.seed(5); N12['e3_calc'](W, informativo=True); self.assertEqual(x, np.random.rand())
    def test_cola_contra_cierre_universo(self):
        t0, t1 = 0, 86_400_000; cm = 86_100_000   # cierre 23:55 (ejemplo)
        f = lambda mx, mn=0, n=5: [dict(fichero='a', min=mn, max=mx, n=n)]; C = N12['completitud']
        self.assertTrue(C(f(cm + 120000), t0, t1, cm)['cola_ok']); self.assertFalse(C(f(cm + 119999), t0, t1, cm)['cola_ok'])
        r = C(f(cm + 120000), t0, t1, cm); self.assertFalse(r['cola_v11_ok']); self.assertTrue(r['cobertura_ok']); self.assertEqual(r['cola_requerida'], cm + 120000)
        self.assertFalse(C(f(t1), t0, t1, None)['cobertura_ok'], 'sin universo: fail-closed')
        self.assertFalse(C(f(cm + 120000, mn=121000), t0, t1, cm)['cabecera_ok']); self.assertTrue(C(f(cm + 120000, mn=120000), t0, t1, cm)['cabecera_ok'])
        g = [dict(fichero='a', min=0, max=1000, n=1), dict(fichero='b', min=1000 + 300001, max=cm + 120000, n=1)]; self.assertFalse(C(g, t0, t1, cm)['cobertura_ok']); g[1]['min'] = 1000 + 300000; self.assertTrue(C(g, t0, t1, cm)['cobertura_ok'])
        self.assertFalse(C(f(cm + 120000, n=0), t0, t1, cm)['cobertura_ok']); self.assertFalse(C([], t0, t1, cm)['cobertura_ok'])
        self.assertFalse(C(f(cm + 120000) + [dict(fichero='x', min=None, max=None, n=0)], t0, t1, cm)['cobertura_ok'], 'fichero con n=0 invalida el dia (fail-closed)')
    def test_cierre_max_universo(self):
        D = '2026-11-12'; t0 = int(pd.Timestamp(D, tz='UTC').timestamp() * 1000); t1 = t0 + 86_400_000
        base_ts = t0 // 1000 + 23 * 3600 + 40 * 60   # start 23:40 -> END 23:45; start 23:45 -> END 23:50 ; start 23:55 solo 'tok' (excluido)
        rows = []
        for st, roles in ((base_ts, ('tok', 'comp')), (base_ts + 300, ('tok', 'comp')), (base_ts + 600, ('tok',))): rows += [(f'btc-updown-5m-{st}', r) for r in roles]
        rows += [(f'eth-updown-5m-{base_ts + 600}', 'tok'), (f'eth-updown-5m-{base_ts + 600}', 'comp'), (f'btc-updown-5m-{t0 // 1000 - 600}', 'tok'), (f'btc-updown-5m-{t0 // 1000 - 600}', 'comp')]
        with tempfile.TemporaryDirectory() as td:
            pd.DataFrame(rows, columns=['slug', 'rol']).to_csv(f'{td}/sonda1_fotos_l2_{D}.csv.gz', index=False, compression='gzip')
            self.assertEqual(N12['cierre_max_universo'](D, 'btc', t0, t1, base=td), (base_ts + 300 + 300) * 1000)    # 23:50
            self.assertEqual(N12['cierre_max_universo'](D, 'eth', t0, t1, base=td), (base_ts + 600 + 300) * 1000)
            self.assertIsNone(N12['cierre_max_universo'](D, 'xrp', t0, t1, base=td)); self.assertIsNone(N12['cierre_max_universo']('2026-01-01', 'btc', t0, t1, base=td))
    def test_p3_v12_patrones_y_v11_intacto(self):
        s = pathlib.Path(f'{H}/p3_agrega_v12.py').read_text()
        for k in ('p7v12_', 'p7wv12_', "'p7w_v12'", "'p3_v7_ADENDA12'", "'ADENDA_12_19nov.md'", "'p3_agrega_v12.py'", "'p7_ipw_balance_v12.py'", 'p3v12_'): self.assertIn(k, s, k)
        for k in ('out/p7_{COIN}', 'out/p7w_{COIN}', 'p7w_v11', "'p3_v6_ADENDA11'", "'p3_agrega.py'"): self.assertNotIn(k, s, k)
        p7 = pathlib.Path(f'{H}/p7_ipw_balance_v12.py').read_text(); self.assertIn("'p7_v12_ADENDA12'", p7); self.assertIn("'p7w_v12'", p7); self.assertNotIn('p7w_v11', p7); self.assertIn("p1_v11_ADENDA11", p7)
        last = {}
        for ln in pathlib.Path(f'{H}/HASHES_CODIGO.txt').read_text().splitlines():
            p_ = ln.split()
            if len(p_) == 2 and re.fullmatch(r'[0-9a-f]{64}', p_[0]): last[p_[1]] = p_[0]
        for nm in ('p1_dia.py', 'p3_agrega.py', 'p7_ipw_balance.py', 'p5_control_sin_relleno.py', 'run_p1.sh'): self.assertEqual(hashlib.sha256(pathlib.Path(f'{H}/{nm}').read_bytes()).hexdigest(), last[nm], f'{nm} v11 modificado')

import json, shutil, subprocess, pickle
class T2(unittest.TestCase):
    """Hallazgos del /code-review (ADENDA_13): 1 nota fixture, 2 cola min t1, 3 tres ficheros Sonda1, 4 p3 comprueba p7 JSON y pkl, 7 covariables del bootstrap, 8 estados de run_v12_post."""
    def test_run_v12_post_revision2(self):
        s = pathlib.Path(f'{H}/run_v12_post.sh').read_text()
        for k in ('rm -f $okj $bj', 'stat -c %Y $okj', "== 'p3_v7_ADENDA12'", "w.get('version') == 'p7w_v12'", "w.get('SHA256_codigo') == c and w.get('SHA256_pkl_p1') == p", 'ya_hecho $j $pk $w', 'WAITING_ROTACION', 'sonda1_ok()', 'kill -0 $cpid', '21600', 'blocked cadena_v11', 'blocked espera_6h', 'chain.pid', "'ADENDA_13b_19nov.md'"): self.assertIn(k, s, k)
        self.assertNotIn('pgrep', s.replace('sin pgrep/pkill', '')); self.assertLess(s.index('esperar_rot\n#'), s.index('p3run()'))
        self.assertIn("'ADENDA_13b_19nov.md']", pathlib.Path(f'{H}/p3_agrega_v12.py').read_text()); subprocess.run(['bash', '-n', f'{H}/run_v12_post.sh'], check=True)
    def test_so_docstrings_y_so2_quita_oid(self):
        S2 = pathlib.Path(H).parent / 'solo_observable_19nov'
        for n in ('so1_traza_v2', 'so1b_ancla_v2', 'so2_f5t_v2', 'so2b_dinamico_v2'):
            t = (S2 / f'{n}.py').read_text(); self.assertIsNone(re.search(r'ADENDA_SO_A1(?!c)', t), n); self.assertNotIn('l3_reverif.csv', t); self.assertNotIn('en ACCIONES de', t)
        t = (S2 / 'so2_f5t_v2.py').read_text(); self.assertLess(t.index('O = O[~O.oid.isin(EXC)]'), t.index("O.merge(k[['oid'")); self.assertIn("how='inner'", (S2 / 'so2b_dinamico_v2.py').read_text())
    def test1_nota_fixture_y_estado_p3(self):
        s = pathlib.Path(f'{H}/run_v12_post.sh').read_text()
        self.assertIn('p7 2026-11-12 _fxP1 fixture_fxP1 ||', s); self.assertNotIn('fixture_fxP1_v12', s)
        self.assertIn('[ $rc = 2 ] && blocked P3', s); self.assertIn('[ $rc = 0 ] || fail $nm', s); self.assertLess(s.index('p3run()'), s.index('COMPLETE_V12 $(date'))
        subprocess.run(['bash', '-n', f'{H}/run_v12_post.sh'], check=True)
        self.assertNotIn('rc=$?; say "p3', s)
    def test2_cola_min_t1_menos_1s(self):
        C = N12['completitud']; t0, t1 = 0, 86_400_000; f = lambda mx: [dict(fichero='a', min=0, max=mx, n=5)]
        r = C(f(t1 - 1000), t0, t1, t1 - 1000); self.assertEqual(r['cola_requerida'], t1 - 1000); self.assertTrue(r['cola_ok'])      # cierre+120 s > t1-1 s -> tope t1-1000
        self.assertFalse(C(f(t1 - 1001), t0, t1, t1 - 1000)['cola_ok']); self.assertTrue(C(f(t1 - 9), t0, t1, t1)['cola_ok'], 'libro5 acaban ~9 ms antes de t1'); self.assertEqual(C(f(t1), t0, t1, 86_100_000)['cola_requerida'], 86_220_000)
    def test2b_cover_fich_real_16nov(self):
        mj = pathlib.Path(f'{H}/out/p1_btc_2026-11-16_DISENO.manifest.json')
        if not mj.exists(): self.skipTest('sin manifest 16-Nov'); 
        os.nice(19); cf = json.loads(mj.read_text())['cover_fich']; D = '2026-11-16'; t0 = int(pd.Timestamp(D, tz='UTC').timestamp() * 1000); t1 = t0 + 86_400_000
        cm = N12['cierre_max_universo'](D, 'btc', t0, t1); self.assertIsNotNone(cm); r = N12['completitud'](cf, t0, t1, cm)
        self.assertTrue(r['cola_ok'], (r['reach'], r['cola_requerida'])); self.assertTrue(r['cobertura_ok']); self.assertLessEqual(cm, t1)
        print('\n[info 16-Nov real] cierre_max', cm, 'reach', r['reach'], 't1-reach ms', t1 - r['reach'], 'hueco s', r['gap'] / 1000)
    def test3_tres_ficheros_sonda1(self):
        D = '2026-11-12'; t0 = int(pd.Timestamp(D, tz='UTC').timestamp() * 1000); t1 = t0 + 86_400_000; st = t0 // 1000 + 23 * 3600 + 40 * 60
        mk = lambda ss, roles: [(f'btc-updown-5m-{x}', r) for x in ss for r in roles]
        with tempfile.TemporaryDirectory() as td:
            wr = lambda dd, rows: pd.DataFrame(rows, columns=['slug', 'rol']).to_csv(f'{td}/sonda1_fotos_l2_{dd}.csv.gz', index=False, compression='gzip')
            wr('2026-11-11', mk([t0 // 1000 - 300], ('tok', 'comp')))                 # END = t0 -> excluido (t0 < END)
            wr(D, mk([st], ('tok', 'comp')))                                           # END 23:45
            wr('2026-11-13', mk([st + 600], ('tok', 'comp')) + mk([st + 900], ('tok',)))   # D+1: END 23:55 cuenta; el de solo 'tok' no
            self.assertEqual(N12['cierre_max_universo'](D, 'btc', t0, t1, base=td), (st + 600 + 300) * 1000)
            wr('2026-11-13', mk([st + 600], ('tok',)) + mk([st + 600], ('comp',)))       # roles repartidos entre filas del mismo fichero SI cuentan (mismo fichero)
            self.assertEqual(N12['cierre_max_universo'](D, 'btc', t0, t1, base=td), (st + 600 + 300) * 1000)
            os.remove(f'{td}/sonda1_fotos_l2_{D}.csv.gz'); self.assertIsNone(N12['cierre_max_universo'](D, 'btc', t0, t1, base=td), 'sin fichero de D: fail-closed')
            self.assertEqual(len(N12['sonda1_fns'](D, base=td)), 3)
    def _p3_tmp(self, td, json_sha, pkl_version):
        for n in ('p3_agrega_v12.py', 'p7_ipw_balance_v12.py'): shutil.copy(f'{H}/{n}', f'{td}/{n}')
        os.makedirs(td + '/out'); f1 = td + '/out/p1_btc_2026-11-12_x.pkl'; open(f1, 'wb').write(b'x'); sp1 = hashlib.sha256(b'x').hexdigest(); p7sha = hashlib.sha256(pathlib.Path(f'{td}/p7_ipw_balance_v12.py').read_bytes()).hexdigest()
        json.dump(dict(version='p7_v12_ADENDA12', SHA256_codigo=p7sha if json_sha else 'mal', SHA256_pkl_p1=sp1, dia_completo=dict(ok=True), dia_valido_E=True, E4_fallos=[]), open(td + '/out/p7v12_btc_2026-11-12_x.json', 'w'))
        pickle.dump(dict(dia='2026-11-12', version=pkl_version, SHA256_codigo=p7sha, SHA256_pkl_p1=sp1, pesos={}), open(td + '/out/p7wv12_btc_2026-11-12_x.pkl', 'wb'))
    def _run_p3(self, td):
        r = subprocess.run([sys.executable, 'p3_agrega_v12.py', 'btc', 'act'], cwd=td, env=dict(os.environ, P3_DISENO='1', PISTA_SUF='_x'), capture_output=True, text=True)
        import glob; bj = glob.glob(td + '/out/*BLOCKED.json'); return r, (json.load(open(bj[0])) if bj else None)
    def test4_p3_comprueba_json_y_pkl_de_este_p7(self):
        with tempfile.TemporaryDirectory() as td:
            self._p3_tmp(td, False, 'p7w_v12'); r, b = self._run_p3(td); self.assertEqual(r.returncode, 2, r.stderr[-400:]); self.assertIn('informe p7', b['motivo'])
        with tempfile.TemporaryDirectory() as td:
            self._p3_tmp(td, True, 'p7w_v11'); r, b = self._run_p3(td); self.assertEqual(r.returncode, 2, r.stderr[-400:]); self.assertIn('pesos p7w', b['motivo'])
    def test7_bootstrap_mismo_filtro_y_filas_sin_end(self):
        W = sint(); W['dist_ticks'] = 3.0; W.loc[W.index[:7], 'end'] = np.nan
        c = N12['e3_calc'](W, informativo=True); self.assertNotIn('dist_ticks', c['SMD_pond_om']); self.assertNotIn('dist_ticks', c['cov_usadas'])
        self.assertEqual(sorted(c['cov_usadas']), sorted(c['SMD_pond_om'])); self.assertEqual(c['n_filas_sin_end'][0], int(W[~W.nb].end.isna().sum())); self.assertGreater(sum(c['n_filas_sin_end']), 0)
        for k, (a, b) in c['n_finitos_por_cov'].items(): self.assertGreater(a, 0)
        self.assertEqual(c['max_abs_pond'], N11['e3_calc'](W)['max_abs_pond'])
if __name__ == '__main__': unittest.main(verbosity=2)
