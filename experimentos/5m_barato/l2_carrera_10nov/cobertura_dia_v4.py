#!/usr/bin/env python3
"""cobertura_dia_v4.py check|fin DIA  (27-Nov, engineer 5m barato). Puerta de cobertura del backfill passT_v4 + manifiesto idempotente.
  check: lee bad_DIA.json (cob_tx_ws, horas malas) y maker_ms_DIA_* (existen y no vacios, enlaces rotos = falta). cob_tx_ws < 0,90 o sin maker_ms => BLOCKED (exit 3), si no exit 0.
  fin:   registra COMPLETE (RT_v3dd_DIA.pkl y ms2 con tamano+sha256) o FAILED. Manifiesto: out_v4/MANIFIESTO_backfill_27nov.json (escritura atomica, una entrada por dia; relanzar reescribe SU entrada, nunca duplica).
No fabrica dias: un dia BLOCKED no genera ms2 ni RT. Solo lectura de datos; escribe solo el manifiesto."""
import sys, os, json, glob, hashlib, time
H = '/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/'; DL = '/root/polymarket-research-datalogs/'
PB = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out/'; MAN = H + 'out_v4/MANIFIESTO_backfill_27nov.json'; UMBRAL = 0.90
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 22), b''): h.update(b)
    return h.hexdigest()
def put(d, rec):
    m = json.load(open(MAN)) if os.path.exists(MAN) else {'contrato': 'backfill passT_v4 v3dd, umbral cob_tx_ws>=%.2f' % UMBRAL, 'dias': {}}
    rec['actualizado'] = time.strftime('%FT%TZ', time.gmtime()); m['dias'][d] = rec
    tmp = MAN + '.tmp'; json.dump(m, open(tmp, 'w'), indent=1, sort_keys=True); os.replace(tmp, MAN)
cmd, d = sys.argv[1], sys.argv[2]
if cmd == 'check':
    try: b = json.load(open(PB + f'bad_{d}.json'))
    except Exception as e: put(d, {'estado': 'PENDING', 'motivo': f'sin bad_{d}.json ({e})'}); sys.exit(3)
    cob = b.get('cob_tx_ws'); hm = sorted({h for _, h in b.get('bad', [])})
    fs = [f for f in glob.glob(DL + f'maker_ms_{d}_*.csv.gz') if os.path.exists(f) and os.path.getsize(f) > 0]
    mot = []
    if cob is None or cob < UMBRAL: mot.append(f'cob_tx_ws={cob} < {UMBRAL} (libro5_tx en pausa/hueco)')
    if not fs: mot.append('sin maker_ms legible')
    rec = {'cob_tx_ws': cob, 'horas_malas': hm, 'n_horas_malas': len(hm), 'fills': b.get('fills'), 'side0_sanas': b.get('side0_sanas'), 'maker_ms_ficheros': len(fs)}
    if mot: rec.update(estado='BLOCKED', motivo='; '.join(mot)); put(d, rec); print('BLOQUEADO', d, rec['motivo']); sys.exit(3)
    rec.update(estado='EN_CURSO', nota=f'{len(hm)} horas malas excluidas por passT via bad_{d}.json'); put(d, rec); print('OK', d, cob, len(hm)); sys.exit(0)
if cmd == 'fin':
    m = json.load(open(MAN)); rec = m['dias'].get(d, {}); rt = H + f'out_v4/RT_v3dd_{d}.pkl'; ms = DL + f'sa_ms2/ms2_{d}.npz'
    if os.path.getsize(rt) > 0 if os.path.exists(rt) else False:
        rec.update(estado='COMPLETE', RT_bytes=os.path.getsize(rt), RT_sha256=sha(rt), ms2_bytes=os.path.getsize(ms) if os.path.exists(ms) else None)
    else: rec.update(estado='FAILED', motivo=rec.get('motivo', 'sin RT_v3dd tras el paso (ver out_v4_run.log)'))
    put(d, rec); print(rec['estado'], d)
