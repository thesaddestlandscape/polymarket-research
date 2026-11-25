#!/usr/bin/env python3
"""Tests ADENDA_SO_A1c (definicion ORIGINAL rem_sh = tk_rem*tk_sz). Sin medir nada. Uso: cd solo_observable_19nov && python3 -I tests_so_a1/test_so_a1.py"""
import pathlib, re, subprocess, sys, tempfile, unittest, pickle
import numpy as np, pandas as pd
S = pathlib.Path(__file__).resolve().parent.parent; sys.path.insert(0, str(S))
import so_rem_a1 as A
class T(unittest.TestCase):
    def test_real_202_definicion_original(self):
        d = A.cargar_tomador(); self.assertEqual(len(d), 202); self.assertTrue((d.rem_estado == 'ok').all()); self.assertEqual(A.resumen_rem(d), {'ok': 202})
        self.assertTrue(np.allclose(d.rem_sh.values, d.tk_rem.values * d.tk_sz.astype(float).values)); self.assertTrue(np.allclose(d.tk_rem.values, d.tk_rem_old.values)); self.assertFalse((d.rem_estado == 'negativo').any())
    def test_mejora_de_precio_resto_cero(self):
        # compra a limite 0,72 (12 acc): mA=8,64 USDC, tA=12 acc. Fill COMPLETO con mejora de precio => takerFillAmount = mA => resto 0 (rem_new 'originales - recibidas' daria negativo)
        lim, ru, rs = A.rem_limite(8_640_000, 12_000_000, 8_640_000, 0); self.assertAlmostEqual(lim, 0.72); self.assertEqual(ru, 0.0); self.assertEqual(rs, 0.0)
        lim, ru, rs = A.rem_limite(8_640_000, 12_000_000, 4_320_000, 0); self.assertAlmostEqual(ru, 4.32); self.assertAlmostEqual(rs, 6.0); self.assertAlmostEqual(rs, 0.5 * 12.0)    # = tk_rem*tsz
        lim, ru, rs = A.rem_limite(10_000_000, 7_200_000, 4_000_000, 1); self.assertAlmostEqual(rs, 6.0); self.assertTrue(np.isnan(ru))                                    # venta: acciones
    def test_fail_closed_sin_dato(self):
        with tempfile.TemporaryDirectory() as td:
            d0 = pickle.load(open(A.V + '/tomador_202.pkl', 'rb')).head(4).copy(); d0['tk_rem'] = [0.5, 0.0, np.nan, 0.2]; d0['tk_sz'] = [12.0, 8.0, 5.0, 0.0]; pickle.dump(d0, open(td + '/tomador_202.pkl', 'wb'))
            d = A.cargar_tomador(td + '/', verificar_sha=False); self.assertEqual(list(d.rem_estado), ['ok', 'ok', 'sin_dato', 'sin_dato']); self.assertEqual(d.rem_sh.iloc[0], 6.0); self.assertEqual(d.rem_sh.iloc[1], 0.0)      # mejora de precio: rem 0, sigue 'ok'
            x = d.tk_rem; self.assertFalse(bool(((x > 0.01) | (x <= 0.01)).iloc[[2, 3]].any()))
    def test_sha_entrada(self):
        with tempfile.TemporaryDirectory() as td:
            pickle.dump(pd.DataFrame(dict(oid=['a'], tk_rem=[0.1], tk_sz=[1.0])), open(td + '/tomador_202.pkl', 'wb'))
            with self.assertRaises(AssertionError): A.cargar_tomador(td + '/')
    def test_scripts_v2(self):
        for n in ('so1_traza_v2', 'so1b_ancla_v2', 'so2_f5t_v2', 'so2b_dinamico_v2'):
            s = (S / f'{n}.py').read_text(); self.assertNotIn('rem_new', s); self.assertNotIn('import so1_traza as', s)
            for v1 in ('so1_filas.pkl', 'so1b_filas.pkl', 'so2_ordenes.pkl', 'so2b_rellenos.pkl', 'so1_status.json'): self.assertNotIn("'" + v1 + "'", s)
        s1 = (S / 'so1_traza_v2.py').read_text(); self.assertLess(s1.index("r.rem_estado != 'ok'"), s1.index('thr = 0.5')); self.assertIn('O = O[~O.oid.isin(EXC)]', (S / 'so2_f5t_v2.py').read_text())
        for n in ('so_rem_a1', 'so1_traza_v2', 'so1b_ancla_v2', 'so2_f5t_v2', 'so2b_dinamico_v2'): subprocess.run([sys.executable, '-m', 'py_compile', str(S / f'{n}.py')], check=True)
if __name__ == '__main__': unittest.main(verbosity=2)
