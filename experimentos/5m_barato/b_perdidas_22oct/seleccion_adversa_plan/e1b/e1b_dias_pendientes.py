"""e1b_dias_pendientes.py -- 23-Nov: imprime los dias forward [fwd0, ayer] que e1b_diario.py debe (re)procesar.
Un dia COMPLETE se CONGELA (no se pasa) si sus salidas e1/e1x/aux/breal existen y el codigo de la sim coincide con el actual.
Motivo: (1) retencion() borra el npz de los COMPLETE >8 d y run sin --dias los re-extraia TODOS cada dia (20+ x 3,5 min,
1-3 GB cada uno -> OOM global 23-Nov 11:51); (2) si las fuentes del volumen rotan, correr_dia degradaba COMPLETE -> BLOCKED
y el evaluador perdia dias validos (10-27..10-31). Si cambia el codigo de la sim, el dia vuelve a la lista (comportamiento original).
No se edita e1b_diario.py porque su hash entra en la firma de la sim de cada dia. Uso: e1b_dias_pendientes.py --fwd0 D -> dias separados por espacio."""
import argparse, datetime, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import e1b_diario as E

ap = argparse.ArgumentParser(); ap.add_argument('--fwd0', default=E.FWD0); a = ap.parse_args()
ch = E.code_hashes(); cod = [ch['e1_sim.py'], ch['e1b_sim_ext.py'], ch['msdata.py'], ch['e1b_diario.py']]
ayer = datetime.datetime.now(datetime.timezone.utc).date() - datetime.timedelta(days=1)
d = datetime.date.fromisoformat(a.fwd0); out = []
while d <= ayer:
    s = d.isoformat(); M = E.load_json(E.E1B + f'dias/{s}.json', {})
    congelado = (M.get('estado') == 'COMPLETE' and M.get('etapas', {}).get('sim', {}).get('codigo') == cod
                 and all(os.path.exists(E.E1B + f'{p}_{s}.csv.gz') for p in ('e1', 'e1x', 'aux', 'breal')))
    if not congelado: out.append(s)
    d += datetime.timedelta(days=1)
print(' '.join(out))
