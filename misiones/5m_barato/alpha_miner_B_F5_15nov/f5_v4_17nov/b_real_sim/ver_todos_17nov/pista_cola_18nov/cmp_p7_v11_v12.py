#!/usr/bin/env python3
"""cmp_p7_v11_v12.py (ADENDA_12 §6.3): compara el informe p7 v11 con el p7 v12 del MISMO pkl de p1 (fixture): solo pueden diferir version/SHA256_codigo, los campos nuevos
(E3 informativo, cierre_max/cola de dia_completo) y las decisiones de completitud ligadas a la cola. Todo lo demas (E1/E2/E3/E4, dia_valido_E, soporte, SMD) debe ser IDENTICO.
Uso: cmp_p7_v11_v12.py p7_v11.json p7_v12.json   (exit 0 si equivalentes)"""
import json, sys
a, b = json.load(open(sys.argv[1])), json.load(open(sys.argv[2])); dif = []; nuevos = []
PERMITIDO = ('version', 'SHA256_codigo', 'dia_completo')
def cmp(x, y, p):
    if isinstance(x, dict) and isinstance(y, dict):
        for k in x:
            if k not in y: dif.append(f'{p}/{k}: falta en v12')
            else: cmp(x[k], y[k], f'{p}/{k}')
        for k in y:
            if k not in x: nuevos.append(f'{p}/{k}')
    elif isinstance(x, list) and isinstance(y, list):
        if len(x) != len(y): dif.append(f'{p}: len {len(x)} != {len(y)}')
        else:
            for i, (u, v) in enumerate(zip(x, y)): cmp(u, v, f'{p}[{i}]')
    elif x != y and not (isinstance(x, float) and isinstance(y, float) and abs(x - y) <= 1e-12 * max(1.0, abs(x))): dif.append(f'{p}: {str(x)[:60]} != {str(y)[:60]}')
cmp({k: v for k, v in a.items() if k not in PERMITIDO}, {k: v for k, v in b.items() if k not in PERMITIDO}, '')
dc = {k: (a['dia_completo'].get(k), b['dia_completo'].get(k)) for k in ('cobertura_ok', 'ok', 'mayor_hueco_ficheros_s', 'inputs_ok', 'inputs_faltantes')}
bad_dc = [k for k in ('mayor_hueco_ficheros_s', 'inputs_ok', 'inputs_faltantes') if dc[k][0] != dc[k][1]]
nuevos_e3 = [n for n in nuevos if 'E3' in n or 'wins' in n]; otros = [n for n in nuevos if n not in nuevos_e3]
print('dia_completo v11->v12 (cobertura_ok/ok pueden cambiar por la cola):', dc); print('campos nuevos E3 informativo:', len(nuevos_e3), '| otros campos nuevos:', otros); print('DIFERENCIAS inesperadas:', len(dif)); [print(' ', x) for x in dif[:30]]
sys.exit(0 if not dif and not bad_dc and not otros else 1)
