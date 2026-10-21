import json,csv,collections,sys
S=sys.argv[1]
DL='/root/polymarket-research-datalogs/'
CUT='2026-10-21T10:08:41'   # snapshot contabilidad
pujas={}   # (slug,lado)->info
mk={}      # slug->id
orders={}  # oid->(slug,lado,t_dec,T,precio,n_orden,cola,libro)
lect={}
fins={}
for l in open(DL+'experimento_h47_B_ledger.jsonl'):
    try:e=json.loads(l)
    except: continue
    if not e.get('real'): continue
    if e.get('ts','')>CUT: continue
    t=e.get('tipo')
    if t=='mercado_inicio': mk[e['slug']]=e['id']
    elif t=='puja_post':
        k=(e['slug'],e['lado'])
        orders[e['oid']]=dict(slug=e['slug'],lado=e['lado'],coin=e['coin'],t_dec=e['t_dec'],T=e['T'],precio=e['precio'],n_orden=e['n_orden'],cola=e['cola'],libro=e['libro'],ts=e['ts'])
        p=pujas.setdefault(k,dict(slug=e['slug'],lado=e['lado'],coin=e['coin'],t0=e['t_dec'],T0=e['T'],p0=e['precio'],n_ord=0,precios=[],ts0=e['ts']))
        p['n_ord']+=1; p['precios'].append(e['precio'])
    elif t in ('lectura','relleno_tardio'):
        lect.setdefault(e['oid'],[]).append(e)
    elif t=='puja_fin':
        fins[(e['slug'],e['lado'])]=e
json.dump(dict(pujas={f'{a}|{b}':v for (a,b),v in pujas.items()},mk=mk,orders=orders,lect=lect,fins={f'{a}|{b}':v for (a,b),v in fins.items()}),open(S+'/ledger_extract.json','w'))
print(len(pujas),len(mk),len(orders),len(lect),len(fins))
# desenlace cache
c=json.load(open(DL+'maker_ms_desenlaces_cache.json'))
ids=set(mk.values()); print('ids',len(ids),'in cache',len(ids&set(c)))
