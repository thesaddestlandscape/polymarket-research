#!/usr/bin/env python3
"""c4_equiv_lowmem.py DIA -- C4 (8): ms_extract_lowmem.py == ms_extract.py bit a bit sobre un dia comun (monedas ETH/SOL/XRP por defecto, SA_TAG=eqv): extrae con lowmem a sa_ms/eqv_ms_DIA.npz, compara TODOS los arrays con sa_ms/ms_DIA.npz (np.array_equal) y borra el temporal.
Escribe rf5_btc/equiv_lowmem_DIA.json {igual, arrays, sha_lowmem, sha_orig}. Pesado (una extraccion de un dia): se lanza por cron_pesado (btc_backfill.sh). 0 ordenes, 0 red."""
import os, sys, json, hashlib, subprocess
import numpy as np
HV = os.path.dirname(os.path.abspath(__file__)) + '/'; DL = os.environ.get('RF5_DL', '/root/polymarket-research-datalogs/'); BTCD = os.environ.get('RF5_BTC_OUT', DL + 'rf5_btc/')
SC = '/root/polymarket-research/experimentos/5m_barato/b_seleccion_adversa/scripts/'
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def iguales_bit(x, y):
    """igualdad BIT A BIT: dtype, forma y bytes (los float32 de q_v* llevan NaN: np.array_equal da False con NaN aunque el patron sea identico -- causa del DIFIERE del 24-Nov 10:01Z con q_k/q_t/t* iguales). Objetos/strings: array_equal."""
    if x.dtype != y.dtype or x.shape != y.shape: return False
    if x.dtype.kind in 'fiub': return bool(np.ascontiguousarray(x).tobytes() == np.ascontiguousarray(y).tobytes())
    return bool(np.array_equal(x, y))

def compara(a, b):
    za = np.load(a, allow_pickle=True); zb = np.load(b, allow_pickle=True); ka, kb = set(za.files), set(zb.files); arr = {k: iguales_bit(za[k], zb[k]) for k in sorted(ka & kb)}
    return dict(igual=bool(ka == kb and all(arr.values())), arrays=arr, solo_en_a=sorted(ka - kb), solo_en_b=sorted(kb - ka))
def main(d):
    orig = DL + f'sa_ms/ms_{d}.npz'; tmp = DL + f'sa_ms/eqv_ms_{d}.npz'
    if not os.path.exists(orig): raise SystemExit(f'sin {orig}')
    if os.path.exists(tmp): os.remove(tmp)
    env = dict(os.environ, SA_TAG='eqv', OMP_NUM_THREADS='1'); r = subprocess.run(['python3', '-I', SC + 'ms_extract_lowmem.py', d], env=env, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(tmp): raise SystemExit('lowmem fallo: ' + r.stderr[-400:])
    res = compara(orig, tmp); os.remove(tmp); res.update(dia=d, sha_lowmem=sha(SC + 'ms_extract_lowmem.py'), sha_orig=sha(SC + 'ms_extract.py')); os.makedirs(BTCD, exist_ok=True); json.dump(res, open(BTCD + f'equiv_lowmem_{d}.json', 'w'), indent=1); print(d, 'igual' if res['igual'] else 'DIFIERE')
if __name__ == '__main__': main(sys.argv[1])
