#!/usr/bin/env python3
"""E02-real paso D (PREREG_E02REAL.md + ADENDA1): clases, EVw, IC90 por cierre. python3 -I fills.json cruce.json"""
import json,sys,collections
import numpy as np
F=json.load(open(sys.argv[1])); C={r['i']:r for r in json.load(open(sys.argv[2]))}
rng=np.random.default_rng(2711)
for i,f in enumerate(F):
    f['pnl']=f['size']*(f['gana']-f['precio']); f['cost']=f['size']*f['precio']
    f['cierre']=int(f['mercado'].split('-')[-1])+300; f['dia']=f['fecha'][:10]; f['coin']=f['mercado'].split('-')[0]
    f['c']=C[i]
print('n fills',len(F),'unidades',len({(f['mercado'],f['outcome']) for f in F}),'Sum pnl fills %.4f coste %.2f EVw %.4f'%(sum(f['pnl'] for f in F),sum(f['cost'] for f in F),sum(f['pnl'] for f in F)/sum(f['cost'] for f in F)))
def clase(x,w='1000'):
    if not x or x.get('estado')!='ok': return None
    s=x.get('S_pre'); acc=None
    return x,s
def cls(f,key,w):
    x=f['c'].get(key)
    if not x or x.get('estado')!='ok': return None
    s=x.get('S_pre')
    if s is not None and s<=f['size']+0.5: return 'solo'
    return 'sweep' if x['sw'][w] else 'nosweep'
def asign(f,w='1000',mode='prim',vent='p'):
    a=cls(f,'L2'+vent,w); b=cls(f,'TOB'+vent,w)
    if mode=='L2': return (a,'L2') if a else (None,None)
    if mode=='TOB': return (b,'TOB') if b else (None,None)
    return (a,'L2') if a else ((b,'TOB') if b else (None,None))
# cobertura
st=collections.Counter()
for f in F:
    c=f['c']; st['F_casado']+=1
    st['T_L2p']+= c.get('L2p') is not None; st['T_TOBp']+= c.get('TOBp') is not None
    st['T_any_p']+= (c.get('L2p') is not None) or (c.get('TOBp') is not None)
    st['L2_eval']+= bool(c.get('L2p') and c['L2p'].get('estado')=='ok'); st['TOB_eval']+= bool(c.get('TOBp') and c['TOBp'].get('estado')=='ok')
    st['clase_prim']+= asign(f)[0] is not None
    st['T_any_s(ampliada)']+= any(c.get(k) is not None for k in ('L2p','L2s','TOBp','TOBs'))
    st['clase_ampliada']+= asign(f,vent='s')[0] is not None or asign(f)[0] is not None
print('COBERTURA (de 215):',dict(st),'-> clase asignada %.1f%%'%(100*st['clase_prim']/len(F)))
est=collections.Counter((f['c'].get('L2p') or {}).get('estado','NOCASADO') for f in F); print('estado L2p:',dict(est))
est=collections.Counter((f['c'].get('TOBp') or {}).get('estado','NOCASADO') for f in F); print('estado TOBp:',dict(est))
print('por dia, clase asignada:',{d:(sum(1 for f in F if f['dia']==d and asign(f)[0]),sum(1 for f in F if f['dia']==d)) for d in sorted({f['dia'] for f in F})})
off=[(f['c'][k]['off_ms']) for f in F for k in ('L2p','TOBp') if f['c'].get(k)]
if off: print('offset bloque-recepcionT ms (n=%d): p10 %d p50 %d p90 %d min %d max %d'%(len(off),*np.percentile(off,[10,50,90]),min(off),max(off)))
print('ambiguedad ncand>1 (L2p/TOBp):',sum(1 for f in F if f['c'].get('L2p') and f['c']['L2p']['ncand']>1),sum(1 for f in F if f['c'].get('TOBp') and f['c']['TOBp']['ncand']>1))
# unidades primarias
first={}
for f in sorted(F,key=lambda f:(f['bloque'],f['logidx_fill'])): first.setdefault((f['mercado'],f['outcome']),f)
U=list(first.values())
def ev(S): c=sum(x['cost'] for x in S); return sum(x['pnl'] for x in S)/c if c>0 else float('nan')
def boot(S,R=2000):
    if len(S)<2: return None
    cl=sorted({x['cierre'] for x in S}); ix=collections.defaultdict(list)
    for x in S: ix[x['cierre']].append(x)
    v=[]
    for _ in range(R):
        q=[y for c in rng.choice(len(cl),len(cl)) for y in ix[cl[c]]]
        e=ev(q)
        if e==e: v.append(e)
    return np.percentile(v,[5,95])
def rep(nm,S):
    if not S: print('  %-10s n=0'%nm); return
    ic=boot(S); pd={d:(len([x for x in S if x['dia']==d]),round(ev([x for x in S if x['dia']==d]),3)) for d in sorted({x['dia'] for x in S})}
    print('  %-10s n=%3d cierres=%3d coste=%7.2f pnl=%+7.3f EVw=%+.4f IC90cierre=%s  porDia=%s'%(nm,len(S),len({x['cierre'] for x in S}),sum(x['cost'] for x in S),sum(x['pnl'] for x in S),ev(S),None if ic is None else '(%+.3f,%+.3f)'%tuple(ic),pd))
def bloque(titulo,pop,w='1000',mode='prim',vent='p'):
    print('==',titulo,'(ventana barrido %s ms, fuente %s, vent %s)'%(w,mode,vent))
    g=collections.defaultdict(list)
    for f in pop:
        c,src=asign(f,w,mode,vent)
        if c: g[c].append(f)
    for k in ('sweep','nosweep','solo'): rep(k,g[k])
    rep('TODOS-clase',[x for k in g for x in g[k]]); return g
g=bloque('UNIDAD primera por mercado-lado',U)
bloque('TODOS los fills',F)
for w in ('250','500','2000'): bloque('sensibilidad unidad',U,w)
bloque('unidad, solo L2',U,mode='L2'); bloque('unidad, solo TOB',U,mode='TOB'); bloque('unidad, ventana ampliada',U,vent='s')
# concordancia L2 vs TOB
cc=collections.Counter()
for f in F:
    a=cls(f,'L2p','1000'); b=cls(f,'TOBp','1000')
    if a and b: cc[(a,b)]+=1
print('concordancia L2 (filas) vs TOB (cols), fills con ambos:',dict(cc))
# fuente por clase
print('fuente de la clase (unidades):',collections.Counter(asign(f)[1] for f in U))
# monedas
for coin in sorted({f['coin'] for f in U}):
    print('moneda',coin); rep('sweep',[f for f in g['sweep'] if f['coin']==coin]); rep('nosweep',[f for f in g['nosweep'] if f['coin']==coin])
sw=[f['c'][k]['dt_sweep'] for f in U for k in ['L2p'] if f['c'].get(k) and f['c'][k].get('estado')=='ok' and f['c'][k].get('dt_sweep') is not None]
if sw: print('tiempo hasta barrido (L2, <=2 s) ms: n=%d p10 %d p50 %d p90 %d'%(len(sw),*np.percentile(sw,[10,50,90])))
