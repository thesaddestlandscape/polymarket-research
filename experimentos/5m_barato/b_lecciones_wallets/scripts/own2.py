import json,sys,collections
sys.path.insert(0,sys.argv[1]); S=sys.argv[1]
from common import *
P=json.load(open(S+'/own_pos.json')); F=json.load(open(S+'/own_fills.json'))
L=json.load(open(S+'/ledger_extract.json')); des=json.load(open(S+'/des_pujas.json'))
def cell(rows):
    if not rows: return (0,)
    c=sum(r['coste'] for r in rows); pn=sum(r['pnl'] for r in rows); w=sum(r['gana'] for r in rows)
    return len(rows),w,round(c,2),round(pn,2),round(pn/c,3)
print('== split por día de reglas candidatas (posiciones propias) ==')
bt=load_bt(['2026-10-20','2026-10-21'])
for p in P:
    sg=1 if p['lado']=='YES' else -1; tb=p['ts_block']-2.4
    r=ret_bps(bt[p['coin']],tb-10,tb-1.5); p['bn_pre10x_blk']=None if r is None else sg*r
rules={'R1 bn_pre10x<=-2 (t propio)':lambda p:p['bn_pre10x'] is not None and p['bn_pre10x']<=-2,
       'R1b bn_pre10x<=-2 (t=bloque-2,4)':lambda p:p['bn_pre10x_blk'] is not None and p['bn_pre10x_blk']<=-2,
       'R2 T_fill>240':lambda p:p['T_fill']>240,
       'R2b T_post>240':lambda p:p['T_post']>240,
       'R3 relleno con cancel en vuelo':lambda p:p['tras_cancel'],
       'R4 XRP':lambda p:p['coin']=='XRP',
       'R5 precio>0,25':lambda p:p['pm']>0.25,
       'R6 n_orden>=9':lambda p:p['n_orden']>=9}
for nm,fn in rules.items():
    for d in ('10-20','10-21'):
        A=[p for p in P if p['dia']==d and fn(p)]; B=[p for p in P if p['dia']==d and not fn(p)]
        print(f'{nm:36s} {d} SI {cell(A)} | NO {cell(B)}')
# solapamientos
print('solape R2/R3', sum(1 for p in P if p['T_fill']>240 and p['tras_cancel']), 'R1/R3',sum(1 for p in P if rules['R1 bn_pre10x<=-2 (t propio)'](p) and p['tras_cancel']))
# no rellenadas vs rellenadas
filled=set((p['slug'],p['lado']) for p in P)
print('\n== selección adversa: pujas rellenadas vs NO rellenadas (desenlace oficial, cobertura 108/108) ==')
g=collections.defaultdict(lambda:[0,0,0.0])
for k,v in L['pujas'].items():
    slug,lado=k.split('|'); fl=(slug,lado) in filled
    win=(des[slug]==lado)
    # precio de referencia: último precio pujado
    pr=v['precios'][-1]; b=f"{(int(pr/0.05))*0.05:.2f}"
    for key in (('todas',fl),(b,fl)):
        g[key][0]+=1; g[key][1]+=win; g[key][2]+=pr
for k in sorted(g): n,w,s=g[k]; print(k,'n',n,'acierto',round(w/n,3),'precio medio puja',round(s/n,3))
