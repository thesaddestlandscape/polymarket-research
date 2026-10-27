#!/usr/bin/env python3
"""Reconstructor DIARIO de puja_fin de B (27-Oct): encadena reconstruir_puja_fin + markouts_desde_registro en UNA pasada.
Paso 1: puja_fin reconstruido de los mercados B cerrados sin puja_fin (idempotente por slug) -> puja_fin_reconstruido.jsonl.
Paso 2: markouts +5/+30/+120 s de TODOS los rellenos pendientes en una sola carga por fichero-dia de m5_registro
        (grep -F -f con todos los tokens), con fallback a libro5_ms donde la serie q falte/este stale -> puja_fin_markouts_m5registro.jsonl
        (idempotente por (slug,oid), flock, fsync). Mercados cuyo m5_registro del dia aun no esta archivado (04:03) se aplazan solos.
Solo LEE ledger/posiciones/m5_registro/libro5; solo ESCRIBE ficheros nuevos de datalogs. No toca B ni procesos vivos.
Seguridad: se niega a correr en 06:00-09:00Z (salvo --forzar-hora); flock -n (una instancia); deja una linea de manifiesto por pasada en
puja_fin_markouts_m5registro.runs.jsonl (inicio/fin, cobertura, estado). Lanzar con: ulimit -v 3000000; nice -n 19 ionice -c3.
Uso: reconstructor_diario_puja_fin.py [--dry] [--forzar-hora]"""
import os, sys, json, time, fcntl, hashlib, datetime as dt, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reconstruir_puja_fin as R
import markouts_desde_registro as M


def _sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:12]


def correr(dry=False):
    filas, bad = R.leer_jsonl(R.LEDGER)
    regs = R.reconstruir(filas, R.cargar_posic(), time.time())
    nuevos, ya = (0, len(regs)) if dry else R.escribir(regs)
    recs = [r for r in R.leer_jsonl(R.OUT)[0] if r.get('tipo') == 'puja_fin']
    if dry:                                   # --dry: ver el efecto sin escribir nada (incluye los que escribiria el paso 1)
        vistos = {r['slug'] for r in recs}; recs += [r for r in regs if r['slug'] not in vistos]
    nuevas, res = M.procesar(recs, dry=dry)
    return dict(ledger_filas=len(filas), ledger_malas=bad, candidatos_puja_fin=len(regs), reconstruidos_nuevos=nuevos, reconstruidos_ya_estaban=ya,
                con_relleno=sum(1 for r in recs if r['rellenos']), markouts=res)


def main():
    dry = '--dry' in sys.argv
    h = dt.datetime.now(dt.timezone.utc).hour
    if 6 <= h < 9 and '--forzar-hora' not in sys.argv:
        print('NO CORRE: 06:00-09:00Z (racimo de crons); usar --forzar-hora solo con permiso', file=sys.stderr); return 3
    lk = open(os.path.join(M.DL, 'reconstructor_diario_puja_fin.lock'), 'w')
    try: fcntl.flock(lk, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError: print('otra instancia en curso', file=sys.stderr); return 4
    man = dict(job='reconstructor_diario_puja_fin', inicio_utc=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), dry=dry,
               codigo={os.path.basename(p): _sha(p) for p in (__file__, R.__file__, M.__file__)}, estado='FAILED')
    try:
        man.update(correr(dry)); man['estado'] = 'COMPLETE' if not man['markouts']['esperan_archivo_dia'] and not man['markouts']['sin_token'] else 'PARTIAL'
    except Exception:
        man['error'] = traceback.format_exc()[-1500:]
    man['fin_utc'] = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    print(json.dumps(man))
    if not dry:
        with open(M.OUT.replace('.jsonl', '.runs.jsonl'), 'a') as f: f.write(json.dumps(man) + '\n')
    return 0 if man['estado'] != 'FAILED' else 1


if __name__ == '__main__':
    sys.exit(main())
