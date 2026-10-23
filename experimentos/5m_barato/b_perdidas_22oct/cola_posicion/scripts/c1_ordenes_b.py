#!/usr/bin/env python3
"""c1_ordenes_b.py -- tabla de ORDENES de B (una fila por oid = order hash on-chain) desde el snapshot del ledger H47-B.
Campos: slug, coin, lado, tok, precio, size, cola (nivel_precio al postear), libro bids/asks al decidir, T, t_dec, t_ret, t_post_gemelo, t_visto,
espera_s, t_cancel_int, t_fuera, lectura (acc, f, espera_s, cola, tras_cancel), rellenos de puja_fin (t_deteccion). Solo lectura.
Salida datos: /root/polymarket-research-datalogs/cola_posicion/ordenes_b.json"""
import json, collections
DL = '/root/polymarket-research-datalogs/cola_posicion/'
O = collections.OrderedDict(); ev = collections.defaultdict(list)
for l in open(DL + 'snap/ledger_B.jsonl'):
    d = json.loads(l); oid = d.get('oid')
    if oid: ev[oid].append(d)
    if d.get('tipo') == 'puja_fin':
        for r in d.get('rellenos') or []: ev[r['oid']].append(dict(r, tipo='relleno_pf'))
for oid, es in ev.items():
    pp = [e for e in es if e['tipo'] == 'puja_post']
    if not pp: continue
    p = pp[0]; o = dict(oid=oid, slug=p['slug'], coin=p['coin'], lado=p['lado'], k=p.get('k'), precio=p['precio'], size=p['size'], cola=p['cola'],
                        libro=p.get('libro'), T=p['T'], t_dec=p['t_dec'], n_orden=p.get('n_orden'), ts_post=p['ts'])
    for e in es:
        t = e['tipo']
        if t == 'post_lat': o['t_call0'] = e['t_call0']; o['t_ret'] = e['t_ret']; o['t_post_gemelo'] = e.get('t_post_gemelo'); o['post_ms'] = e['ms']
        elif t == 'visto': o['t_visto'] = e['t']; o['espera_visto'] = e['espera_s']
        elif t == 'intencion_cancel': o.setdefault('t_cancel_int', e['ts'])
        elif t == 'fuera_libro': o['t_fuera'] = e['ts']; o['fuera_origen'] = e.get('origen')
        elif t == 'cancel_lat': o['cancel_ms'] = e['ms']
        elif t == 'lectura': o.setdefault('lect', []).append(dict(f=e.get('f'), acc=e.get('acc'), precio=e.get('precio'), espera_s=e.get('espera_s'), cola=e.get('cola'), T=e.get('T'), tras_cancel=e.get('tras_cancel'), ts=e['ts']))
        elif t == 'relleno_pf': o.setdefault('pf', []).append(dict(acc=e['acc'], precio=e['precio'], t_det=e['t_deteccion'], espera_s=e.get('espera_s'), cola=e.get('cola'), tras_cancel=e.get('tras_cancel')))
        elif t == 'relleno_tardio': o['tardio'] = dict(acc=e['acc'], precio=e['precio'], ts=e['ts'])
        elif t == 'gemelo_relleno': o['gemelo_acc'] = e['acc_total']
        elif t == 'verificada': o['verificada_f'] = e['f']
    O[oid] = o
json.dump(list(O.values()), open(DL + 'ordenes_b.json', 'w'))
print('ordenes', len(O), 'con lectura', sum(1 for o in O.values() if 'lect' in o), 'con pf', sum(1 for o in O.values() if 'pf' in o),
      'tardio', sum(1 for o in O.values() if 'tardio' in o), 'gemelo', sum(1 for o in O.values() if 'gemelo_acc' in o), 'sin t_visto', sum(1 for o in O.values() if 't_visto' not in o))
