#!/usr/bin/env python3
"""Escribe/actualiza run_manifest.json (job id, hashes de codigo/entradas, parametros, fechas, estado) y cobertura por dia. Uso: manifest_v2.py inicio|fase1_ok|fin|BLOCKED [detalle]"""
import glob, hashlib, json, os, sys, time
Z = os.path.dirname(os.path.abspath(__file__)); OUT = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v2/'
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]
f = OUT + 'run_manifest.json'
m = json.load(open(f)) if os.path.exists(f) else {}
ev = sys.argv[1]
if ev == 'inicio' and 'job_id' not in m:
    m.update(job_id='h23_v2_20oct', inicio=time.strftime('%FT%TZ', time.gmtime()), fechas_previstas=[f'2026-10-{d:02d}' for d in range(6, 19)], monedas=['BTC', 'ETH', 'SOL', 'XRP'],
             parametros=dict(reps_ms=[0, 50, 150, 500, 1500], mults=[1, 2.5, 5, 12.5], regla='h23_regla.py (congelada)'),
             codigo={n: sha(os.path.join(Z, n)) for n in ('h23_sim_v2.py', 'extrae_alts.sh', 'run_v2.sh', 'manifest_v2.py', 'PREREGISTRO_v2.json')},
             regla_sha=sha(os.path.join(Z, '..', 'h23_regla.py')), entradas='extracto BTC v4_comprar_lo_bueno (rows/k/x_D) + controles_D.csv + maker_ms_desenlaces_cache.json; alts: m5_registro/m15_registro del volumen',
             comando='bash %s/run_v2.sh' % Z)
m['estado'] = {'inicio': 'RUNNING', 'fase1_ok': 'RUNNING(fase1 BTC completa)', 'fin': 'COMPLETE?', 'BLOCKED': 'BLOCKED'}.get(ev, ev)
if ev == 'BLOCKED': m['bloqueo'] = sys.argv[2]
cob = [json.load(open(c)) for c in sorted(glob.glob(OUT + 'v2_cobertura_*.json'))]
m['cobertura'] = {f"{c['coin']} {c['dia']}": {k: c[k] for k in ('cierres_grupo', 'con_lado', 'con_libro', 'errores', 'sin_desenlace')} for c in cob}
m['dias_hechos'] = sorted({f"{c['coin']} {c['dia']}" for c in cob})
if ev == 'fin': m['fin'] = time.strftime('%FT%TZ', time.gmtime())
m['actualizado'] = time.strftime('%FT%TZ', time.gmtime())
json.dump(m, open(f + '.tmp', 'w'), indent=1); os.replace(f + '.tmp', f)
print('manifest', m['estado'], len(m['dias_hechos']), 'coin-dia')
