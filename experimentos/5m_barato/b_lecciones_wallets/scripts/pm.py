import json,collections,sys,random,math
S=sys.argv[1]
F=json.load(open(S+'/own_fills.json'))
P=collections.OrderedDict()
for f in sorted(F,key=lambda x:x['t_fill']):
    k=(f['slug'],f['outcome'])
    if k not in P: P[k]=dict(f,n_fills=0,coste=0,sh=0,pnl=0)
    p=P[k]; p['n_fills']+=1; p['coste']+=f['coste']; p['sh']+=f['sh']; p['pnl']+=f['pnl']
P=list(P.values())
for p in P: p['pm']=p['coste']/p['sh']
json.dump(P,open(S+'/own_pos.json','w'))
def cell(rows):
    c=sum(r['coste'] for r in rows); pn=sum(r['pnl'] for r in rows); w=sum(r['gana'] for r in rows)
    pm=sum(r['coste'] for r in rows)/sum(r['sh'] for r in rows)
    return len(rows),w,round(c,2),round(pn,2),round(pn/c,3) if c else None,round(pm,3)
def boot(rows,key,n=4000):
    g=collections.defaultdict(lambda:[0,0])
    for r in rows: g[key(r)][0]+=r['pnl']; g[key(r)][1]+=r['coste']
    v=list(g.values()); rr=random.Random(1); e=[]
    for _ in range(n):
        s=[v[rr.randrange(len(v))] for _ in v]; e.append(sum(a for a,b in s)/sum(b for a,b in s))
    e.sort(); return round(e[int(.05*n)],3),round(e[int(.95*n)],3),len(v)
print('TOTAL n,gan,coste,pnl,EVpond,pmedio',cell(P),'IC90 boot por posición',boot(P,lambda r:(r['slug'])),'por cierre',boot(P,lambda r:r['fin']))
s=sorted(P,key=lambda r:-r['pnl']); print('sin 2 mejores pos',cell(s[2:]),'top3 pnl',[round(r['pnl'],2) for r in s[:3]])
print('hit esperado (precio medio)', round(sum(r['pm'] for r in P)/len(P),3),'hit real',round(sum(r['gana'] for r in P)/len(P),3))
def tab(name,key):
    g=collections.defaultdict(list)
    for r in P: g[key(r)].append(r)
    print('\n##',name)
    for k in sorted(g): print(k,cell(g[k]))
tab('dia',lambda r:r['dia'])
tab('moneda',lambda r:r['coin'])
tab('banda 0,05 precio medio',lambda r:f"{math.floor(r['pm']/0.05)*0.05:.2f}")
tab('moneda x banda',lambda r:(r['coin'],f"{math.floor(r['pm']/0.05)*0.05:.2f}"))
tab('tanda',lambda r:int(r['tanda']))
tab('hora UTC (bloques 3h)',lambda r:r['hora']//3*3)
tab('T restante al relleno (60s)',lambda r:int(r['T_fill']//60)*60)
tab('T restante al post',lambda r:int(r['T_post']//60)*60)
tab('lado',lambda r:r['lado'])
tab('n_orden (repegados antes del relleno)',lambda r:min(r['n_orden'],10)//3)
tab('relleno tras cancel / tardio',lambda r:(r['tras_cancel'],r['tardio']))
tab('nº makers en la tx tomadora',lambda r:min(r['n_makers_tx'],5))
tab('niveles barridos en la tx',lambda r:min(r['niveles_tx'],4))
tab('tamaño tomador (acc)',lambda r:'<50' if r['tk_sh']<50 else ('50-200' if r['tk_sh']<200 else '>=200'))
def q(v,cuts):
    if v is None: return 'missing'
    for c in cuts:
        if v<c: return f'<{c}'
    return f'>={cuts[-1]}'
for nm in ['bn_pre30','bn_pre10','bn_pre3','bn_pre10x','bn_pre5x','bn_pre20x','bn_post3','bn_post10','bn_toend','cl_pre10','cl_pre10x','cl_pre20x','cl_post10','marg_fill','marg_dec']:
    tab(nm+' (bps a favor de NUESTRO lado)',lambda r,nm=nm:q(r[nm],[-5,-2,0,2,5]))
