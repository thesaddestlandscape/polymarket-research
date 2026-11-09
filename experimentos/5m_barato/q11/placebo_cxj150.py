#!/usr/bin/env python3
"""Placebo de CXJ150 (PREREG_Q11_THRU1_FWD, multiplicidad): desplazamiento circular de la serie de saltos de Binance dentro del dia, tau' = D0 + ((tau - D0 + s) mod 86400 s),
s ~ U[60, 86340] s, UNA s por (semilla, dia) comun a las 3 monedas (misma frecuencia y simultaneidad), 99 semillas. Estadistico: dPnL BASE (placebo - G0) sumado en los dias que cuentan.
m = media placebo; p = (1 + #{|d_perm - m| >= |d_obs - m|}) / 100 exigiendo d_obs > m. IMPLEMENTADO, NO EJECUTADO en produccion (4-8 h por checkpoint; nice 19, ionice 3, ulimit 3 GB, fuera de 06:00-09:15Z, un proceso a la vez).
Reutiliza passT.py SIN tocarlo: lee su codigo (sha comprobado), sustituye SOLO la construccion de JUMP y la lista VN, y lo ejecuta con __file__ en el directorio del placebo.
Uso:  placebo_cxj150.py dia D SEMILLA     -> thru1_fwd/placebo/s<SEMILLA>/out/RT_<D>.pkl (variables G0 y CXJ150 con saltos desplazados)
      placebo_cxj150.py cp CP D1,D2,...   -> para cada semilla 1..99 sin RT del dia, lo genera; agrega y escribe thru1_fwd/placebo_cxj150_cp<CP>.json
      placebo_cxj150.py agregar CP D1,...  -> solo agrega (si ya estan todos los RT)
      placebo_cxj150.py test              -> comprueba que el parche aplica sobre passT.py (sin ejecutar nada pesado)"""
import sys, os, re, json, hashlib, subprocess
import numpy as np, pandas as pd
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; PT = HERE + 'toxicidad_thru1/passT.py'; PSHA = 'a8b9d7a0158fd0b0cf47582c499d6c1cc870269310c8ef4481482733d1c64038'
TX = HERE + 'toxicidad_thru1/out/'; SAL = HERE + 'thru1_fwd/'
OLD_J = "r1 = bnr(coin, t, 1000); JUMP[coin] = {'up': t[r1 >= 3], 'dn': t[r1 <= -3]}"
NEW_J = ("r1 = bnr(coin, t, 1000); JUMP[coin] = {'up': _SH(t[r1 >= 3]), 'dn': _SH(t[r1 <= -3])}")
def parchear():
    src = open(PT).read(); assert hashlib.sha256(src.encode()).hexdigest() == PSHA, 'passT.py distinto del registrado'
    assert src.count(OLD_J) == 1, 'no encuentro la construccion de JUMP'; src = src.replace(OLD_J, NEW_J)
    src, n = re.subn(r"^VN = .*$", "VN = ['G0', 'CXJ150']", src, flags=re.M); assert n == 1, 'no encuentro VN'
    pre = ("def _SH(a):\n    a = np.asarray(a, np.int64); return np.sort(day0 + ((a - day0 + _S) % 86400000))\n")
    return src, pre
def shift_ms(seed, d): return int(np.random.default_rng(seed * 100003 + int(d.replace('-', ''))).integers(60, 86341)) * 1000
def correr(d, seed):
    src, pre = parchear(); od = SAL + f'placebo/s{seed}/'; os.makedirs(od + 'out', exist_ok=True)
    if os.path.exists(od + f'out/RT_{d}.pkl'): return
    src = src.replace("JUMP = {}", pre + "_S = " + str(shift_ms(seed, d)) + "\nJUMP = {}", 1); assert '_S = ' in src
    sys.argv = ['passT.py', d]; ns = {'__file__': od + 'passT_placebo.py', '__name__': '__main__'}; exec(compile(src, 'passT_placebo', 'exec'), ns)
def agregar(cp, dias):
    from importlib import import_module
    sys.path.insert(0, HERE); E = import_module('eval_thru1')
    T = pd.concat([pd.read_pickle(f'{TX}RT_{d}.pkl') for d in dias], ignore_index=True); g0 = T[T['var'] == 'G0']; c0 = T[T['var'] == 'CXJ150']
    d_obs = float(E.dser(c0, g0).sum()); perm = []
    for s in range(1, 100):
        P = pd.concat([pd.read_pickle(SAL + f'placebo/s{s}/out/RT_{d}.pkl') for d in dias], ignore_index=True)
        perm.append(float(E.dser(P[P['var'] == 'CXJ150'], P[P['var'] == 'G0']).sum()))
    m = float(np.mean(perm)); p = (1 + sum(abs(x - m) >= abs(d_obs - m) for x in perm)) / 100
    E.atomic(SAL + f'placebo_cxj150_cp{cp}.json', json.dumps(dict(dias=list(dias), d_obs=d_obs, m=m, p=p, n_semillas=len(perm), perm=perm), indent=1)); print('cp', cp, 'd_obs', d_obs, 'm', m, 'p', p)
if __name__ == '__main__':
    a = sys.argv[1:]
    if a[0] == 'test': src, pre = parchear(); print('parche OK; shift ejemplo (semilla 1, 2026-11-07):', shift_ms(1, '2026-11-07') // 1000, 's'); compile(src, 'x', 'exec')
    elif a[0] == 'dia': correr(a[1], int(a[2]))
    elif a[0] in ('cp', 'agregar'):
        dias = a[2].split(',')
        if a[0] == 'cp':
            for s in range(1, 100):
                for d in dias: correr(d, s)   # exec de passT: un dia por proceso en la practica (usar un wrapper por semilla/dia si hace falta aislar memoria)
        agregar(int(a[1]), dias)
