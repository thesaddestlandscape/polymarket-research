#!/usr/bin/env python3
"""unidades_b_e1b.py -- COPIA de salida/scripts/unidades_b.py (que revienta con posiciones abiertas: pnl_realizado vacio) que salta las abiertas y escribe en E1B/unidades_b.csv. ORIGINAL: unidades_b.py -- posiciones B (posiciones.csv, tanda_B != '') + hora de deteccion del relleno del ledger H47-B (puja_fin.rellenos).
Salida datos/unidades_b.csv. Solo lectura."""
import json, csv, collections, os
BASE = '/root/polymarket-research/experimentos/5m_barato/'
OUT = os.environ.get('E1B_DIR', '/root/polymarket-research-datalogs/e1b/').rstrip('/') + '/unidades_b.csv'
pos = [r for r in csv.DictReader(open(BASE + 'contabilidad_wallet_dedicada/posiciones.csv')) if r['tanda_B'] and r['pnl_realizado'] not in ('', None)]      # solo liquidadas
fills = collections.defaultdict(list); pujas = collections.defaultdict(list); tardios = collections.defaultdict(list)
oid2slug = {}
for l in open('/root/polymarket-research-datalogs/experimento_h47_B_ledger.jsonl'):
    d = json.loads(l); tp = d.get('tipo')
    if tp == 'puja_post': oid2slug[d['oid']] = (d['slug'], d['lado'], d.get('t_dec'), d.get('T'), d.get('precio'))
    if tp == 'puja_fin':
        out = 'Up' if d['lado'] == 'YES' else 'Down'
        pujas[(d['slug'], out)].append(d)
        for r in d.get('rellenos') or []: fills[(d['slug'], out)].append(r)
    if tp == 'relleno_tardio':
        s = oid2slug.get(d['oid']); 
        if s: tardios[(s[0], 'Up' if s[1] == 'YES' else 'Down')].append(d)
rows = []; miss = 0
for p in pos:
    k = (p['mercado'], p['outcome']); fs = fills.get(k, [])
    tdet = min((f['t_deteccion'] for f in fs), default=None)
    f0 = min(fs, key=lambda f: f['t_deteccion']) if fs else {}
    if tdet is None: miss += 1
    fin = p['fin_mercado_utc']
    import datetime
    fin_s = datetime.datetime.fromisoformat(fin.replace('Z', '+00:00')).timestamp()
    rows.append(dict(mercado=p['mercado'], outcome=p['outcome'], coin=p['mercado'].split('-')[0].upper(), dia=p['fecha_primer_fill_utc'][:10],
                     tanda=p['tanda_B'], acc=float(p['acciones']), coste=float(p['coste']), precio=float(p['precio_medio']),
                     payout=float(p['payout'] or 0), pnl=float(p['pnl_realizado']), gana=int(p['estado'] == 'liquidada_ganada'),
                     t_det=tdet, p_fill=f0.get('precio'), espera_s=f0.get('espera_s'), tras_cancel=f0.get('tras_cancel'), n_rellenos=len(fs),
                     n_tardios=len(tardios.get(k, [])), fin_s=fin_s, T_det=(fin_s - tdet) if tdet else None,
                     primer_fill_chain=p['fecha_primer_fill_utc'], mo5=f0.get('markout_5s'), mo30=f0.get('markout_30s')))
os.makedirs(os.path.dirname(OUT), exist_ok=True); TMP = OUT + '.tmp'
with open(TMP, 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
os.replace(TMP, OUT)
print('posiciones', len(rows), 'sin hora de deteccion', miss, 'tardios', sum(1 for r in rows if r['n_tardios']), '->', OUT)