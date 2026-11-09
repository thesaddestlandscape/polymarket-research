"""ACEPTACION sobre dias QUEMADOS (ADDENDUM3 sec. 7, PREREG_Q11_THRU1_FWD): usa los pickles de dev y de q11. Uso: python3 -I test_q11_aceptacion.py
(a) thru1: G0 n=2938, pnl -166,9 +-1, EV -0,076; thru1 n=2321, EV -0,125; dPnL GEO6 +140 y CXJ150 +128 (+-1). (b) SOL013 --desde 2026-10-26 --hasta 2026-11-03: T1 n=117, EV +0,468, sin2 +0,145.
No escribe en thru1_fwd/ (usa un directorio temporal); `eval_thru1.py --aceptacion` es lo que regenera thru1_fwd/aceptacion.json (ver reaceptar.sh)."""
import sys, os, json, tempfile, subprocess
sys.path.insert(0, '/root/polymarket-research/misiones/5m_barato/forward_sol013/'); sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/q11/')
import eval_thru1 as E
tmp = tempfile.mkdtemp(); ac = E.aceptacion(tmp); v = ac['valores']
assert (ac['pass_'] and v['g0_n'] == 2938 and abs(v['g0_pnl'] + 166.9) <= 1 and v['thru1_n'] == 2321 and abs(v['thru1_ev'] + 0.125) <= 0.0006 and abs(v['d_geo6'] - 140) <= 1 and abs(v['d_cxj150'] - 128) <= 1), f'ACEPTACION quemados: {v}'
import subprocess   # aceptacion SOL013 (ADDENDUM3 sec. 7): sobre quemados T1 n=117, EV +0,468, sin2 +0,145 (ventana 26-Oct..03-Nov), con --salida temporal (no toca el estado real)
sd = tempfile.mkdtemp(); subprocess.run(['python3', '-I', '/root/polymarket-research/misiones/5m_barato/forward_sol013/filtro_sol013.py', '--desde', '2026-10-26', '--hasta', '2026-11-03', '--salida', sd, '--hoy', '2026-11-20'], check=True, capture_output=True)
rj = json.load(open(sd + '/resumen.json')); assert (rj['n'] == 117 and abs(rj['ev'] - 0.468) < 0.0006 and abs(rj['sin2'] - 0.145) < 0.0006 and 'r123' in rj), f'ACEPTACION SOL013 quemados: n={rj["n"]} EV={rj["ev"]:.4f} sin2={rj["sin2"]:.4f} veredicto={rj["veredicto"]}'
print('OK test_q11_aceptacion  ' + json.dumps({k: round(x, 3) for k, x in v.items()}) + f'  SOL013 n={rj["n"]} ev={rj["ev"]:.3f} sin2={rj["sin2"]:.3f}')
