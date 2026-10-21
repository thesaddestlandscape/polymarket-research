#!/usr/bin/env python3
"""Escribe/actualiza run_manifest.json del job H23 v3 (job id, hashes de codigo/entradas, parametros, fechas previstas, estado, cobertura por dia, duplicados).
Uso: manifest_v3.py inicio|paso|fin|BLOCKED|FAILED [detalle]. Escritura atomica (tmp + replace)."""
import glob, hashlib, json, os, sys, time
Z = os.path.dirname(os.path.abspath(__file__)); OUT = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/h23_v3/'
IN = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/'
DISC = [f'2026-10-{d:02d}' for d in range(6, 19)]; OOS = ['2026-10-19', '2026-10-20']
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]
sys.path.insert(0, Z)
os.makedirs(OUT, exist_ok=True)
f = OUT + 'run_manifest.json'
m = json.load(open(f)) if os.path.exists(f) else {}
ev = sys.argv[1]
if 'job_id' not in m:
    m.update(job_id='h23_v3_21oct', inicio=time.strftime('%FT%TZ', time.gmtime()), fechas_previstas=OOS + DISC, periodos=dict(OOS=OOS, DISC=DISC), moneda='BTC',
             parametros=dict(reps_ms=[0, 50, 150, 300, 500, 1500], sizings=['2eur', 'real'], modos_cierre=['acum', 'primer'], celda_central='cola base, alta 79, cancel 60'),
             codigo={n: sha(os.path.join(Z, n)) for n in ('h23_sim_v3.py', 'h23_regla_v3.py', 'h23_analisis_v3.py', 'h23_valida_v3.py', 'run_v3.sh', 'manifest_v3.py', 'PREREGISTRO.md') if os.path.exists(os.path.join(Z, n))},
             regla_hash_config=__import__('importlib').import_module('h23_regla_v3').hash_config(), entradas='extracto BTC v4_comprar_lo_bueno (rows/k/x_D; 19-20 Oct extraidos por r2/extrae_btc.sh) + controles_D.csv + maker_ms_desenlaces_cache.json',
             comando='bash %s/run_v3.sh' % Z)
m['estado'] = {'inicio': 'RUNNING', 'paso': 'RUNNING', 'fin': 'COMPLETE?', 'BLOCKED': 'BLOCKED', 'FAILED': 'FAILED'}.get(ev, ev)
if len(sys.argv) > 2: m.setdefault('pasos', []).append({'t': time.strftime('%FT%TZ', time.gmtime()), 'ev': ev, 'detalle': sys.argv[2]})
cob = [json.load(open(c)) for c in sorted(glob.glob(OUT + 'v3_cobertura_BTC_*.json'))]
m['cobertura'] = {c['dia']: {k: c[k] for k in ('cierres_grupo', 'con_lado', 'con_libro', 'errores', 'sin_desenlace')} for c in cob}
m['dias_hechos'] = sorted(c['dia'] for c in cob)
m['dias_pendientes'] = [d for d in m['fechas_previstas'] if d not in m['dias_hechos']]
m['extracto_presente'] = {d: all(os.path.exists(IN + n.format(d)) for n in ('rows_{}.csv.gz', 'k_{}.csv', 'x_{}.csv.gz')) for d in OOS}
dup = {}
for fcsv in sorted(glob.glob(OUT + 'v3_BTC_20*.csv')):
    import csv
    seen, d = set(), 0
    for r in csv.DictReader(open(fcsv)):
        k = (r['cierre'], r['brazo'], r['sizing'], r['modo'], r['rep'], r['cola'], r['lat_post'], r['lat_cancel'])
        d += k in seen; seen.add(k)
    dup[os.path.basename(fcsv)[7:17]] = d
m['filas_duplicadas_por_clave'] = dup
if ev in ('fin', 'FAILED', 'BLOCKED'): m['fin'] = time.strftime('%FT%TZ', time.gmtime())
m['actualizado'] = time.strftime('%FT%TZ', time.gmtime())
json.dump(m, open(f + '.tmp', 'w'), indent=1); os.replace(f + '.tmp', f)
print('manifest', m['estado'], len(m['dias_hechos']), 'dias hechos;', len(m['dias_pendientes']), 'pendientes')
