"""c4_equiv_lowmem.compara: igualdad bit a bit con NaN (fallo real del 24-Nov: np.array_equal da False si hay NaN)."""
import os, sys, tempfile
import numpy as np
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HV)
import c4_equiv_lowmem as C

def _npz(d, nombre, **kw):
    p = os.path.join(d, nombre); np.savez(p, **kw); return p

def test_nan_identico_es_igual_y_distinto_no():
    v = np.array([1.0, np.nan, 3.0], dtype=np.float32)
    with tempfile.TemporaryDirectory() as d:
        a = _npz(d, 'a.npz', q_v0=v, q_k=np.arange(3)); b = _npz(d, 'b.npz', q_v0=v.copy(), q_k=np.arange(3))
        assert C.compara(a, b)['igual'] is True                       # fallaba antes: array_equal(NaN, NaN) = False
        w = v.copy(); w[0] = 1.5; c = _npz(d, 'c.npz', q_v0=w, q_k=np.arange(3))
        r = C.compara(a, c); assert r['igual'] is False and r['arrays']['q_v0'] is False and r['arrays']['q_k'] is True
        w2 = v.copy(); w2[1] = 0.0; assert C.compara(a, _npz(d, 'd.npz', q_v0=w2, q_k=np.arange(3)))['igual'] is False   # un NaN que pasa a 0 se detecta

def test_dtype_o_claves_distintas_no_son_iguales():
    with tempfile.TemporaryDirectory() as d:
        a = _npz(d, 'a.npz', x=np.arange(3, dtype=np.int64)); b = _npz(d, 'b.npz', x=np.arange(3, dtype=np.int32)); c = _npz(d, 'c.npz', x=np.arange(3, dtype=np.int64), y=np.zeros(1))
        assert C.compara(a, b)['igual'] is False and C.compara(a, c)['igual'] is False and C.compara(a, c)['solo_en_b'] == ['y']
