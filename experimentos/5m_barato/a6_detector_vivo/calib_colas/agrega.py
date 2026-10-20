#!/usr/bin/env python3
import sys,json,math,collections,statistics,random,datetime
C='/mnt/HC_Volume_106538179/datalogs_analisis_caches/colas_20oct/'
coins=sys.argv[1].split(',')
TQ={1:12.706,2:4.303,3:3.182,4:2.776}   # t bilateral 95% ... pero IC90 -> usar t 0.95 unilateral
T90={1:6.314,2:2.920,3:2.353,4:2.132}
random.seed(7)
def bucket(q):
    return '0.10-0.15' if q<=150 else '0.15-0.20' if q<=200 else '0.20-0.25' if q<=250 else '0.25-0.30'
TR=['T60-140','T140-220','T220-270']
rows=[]
for c in coins:
    for l in open(C+f'muestras_{c}.ndjson'):
        d=json.loads(l)
        if d.get('vacio'): continue
        d['day']=datetime.datetime.fromtimestamp(d['t0']/1000,datetime.timezone.utc).strftime('%m-%d')
        d['hour']=d['t0']//3600000
        d['b']=bucket(d['q0']); d['tr']=TR[d['k']]
        rows.append(d)
print('muestras',len(rows),'rotas',sum(r['roto'] for r in rows))
rows=[r for r in rows if not r['roto']]
H=[2,5,10,30,60]
def fillinfo(r,nm):
    if nm.startswith('sh_'):
        t1,f,tf=r[nm]; return t1,f
    v=r[nm]; return v['t1'],v['fill']
def tfull(r,nm):
    return r[nm][2] if nm.startswith('sh_') else r[nm]['tf']
VAR=['sh_f000','sh_f050','sh_f100','rp_lo','rp_prop','rp_hi']
NAME={'sh_f000':'opt','sh_f050':'base','sh_f100':'cons','rp_lo':'lo','rp_prop':'prop','rp_hi':'hi'}
GRID=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.25,1.5,2.0]
HZ=[1,2,5,10,30,60]
def stats(rs):
    out={}
    n=len(rs)
    for nm in VAR:
        a=[fillinfo(r,nm) for r in rs]
        out[nm+'_any']=sum(1 for t,f in a if f>0)/n
        out[nm+'_full']=sum(1 for t,f in a if f>=49.99)/n
        for h in H:
            out[nm+f'_h{h}']=sum(1 for (t,f),r in zip(a,rs) if t is not None and (t-r['t0'])<=h*1000)/n
        ts=[t-r['t0'] for (t,f),r in zip(a,rs) if t is not None]
        out[nm+'_t1med']=statistics.median(ts) if ts else None
    return out
def cfill(r,al):
    v=r['rp_'+al]; f1=v['f1']
    if f1: return f1[1],r['D0']+f1[4],True
    return v['ca'],r['D0']+v['apre'],False
def feff(r,al):
    v=r['rp_'+al]; f1=v['f1']
    if f1: return f1[3],r['D0'],True
    return v['ctp'],r['D0'],False
def cW(r,al,W):
    v=r['rp_'+al]; s=v['snaps'][str(W)]
    return s[0],r['D0']+s[3]
def dayci(vals):
    # vals: lista de (num,den) por dia -> razon por dia -> media y IC90 t
    byd=collections.defaultdict(lambda:[0.0,0.0])
    for d,n,m in vals: byd[d][0]+=n; byd[d][1]+=m
    rs=[a/b for a,b in byd.values() if b>0]
    if not rs: return None
    mean=statistics.mean(rs)
    if len(rs)<2: return mean,None,None,len(rs)
    se=statistics.stdev(rs)/math.sqrt(len(rs)); t=T90[len(rs)-1] if len(rs)-1 in T90 else 1.7
    return mean,mean-t*se,mean+t*se,len(rs)
def pooled(vals):
    n=sum(v[1] for v in vals); m=sum(v[2] for v in vals); return n/m if m>0 else None
def blockci(rs,fn,B=400):
    # bootstrap por bloques de 1 hora del estadistico fn(lista_de_muestras)
    byh=collections.defaultdict(list)
    for r in rs: byh[r['hour']].append(r)
    keys=list(byh)
    if len(keys)<5: return None
    vs=[]
    for _ in range(B):
        samp=[]
        for _k in range(len(keys)): samp+=byh[random.choice(keys)]
        v=fn(samp)
        if v is not None: vs.append(v)
    vs.sort()
    return vs[int(0.05*len(vs))],vs[int(0.95*len(vs))]
def fc(al): 
    def g(rs):
        n=m=0
        for r in rs:
            a,b,_=cfill(r,al); n+=a; m+=b
        return n/m if m>0 else None
    return g
def ff(al):
    def g(rs):
        n=m=0
        for r in rs:
            a,b,_=feff(r,al); n+=a; m+=b
        return n/m if m>0 else None
    return g
def pcurve(rs,nm):
    n=len(rs); out=[]
    for h in HZ:
        a=sum(1 for r in rs if fillinfo(r,nm)[0] is not None and fillinfo(r,nm)[0]-r['t0']<=h*1000)/n
        b=sum(1 for r in rs if tfull(r,nm) is not None and tfull(r,nm)-r['t0']<=h*1000)/n
        out+= [a,b]
    return out
def fstar(rs,al):
    tgt=pcurve(rs,'rp_'+al); best=None
    for g in GRID:
        nm='sh_f%03d'%int(round(g*100))
        c=pcurve(rs,nm); d=sum(abs(x-y) for x,y in zip(tgt,c))/len(tgt)
        if best is None or d<best[1]: best=(g,d)
    return best
def fstar_dias(rs,al):
    byd=collections.defaultdict(list)
    for r in rs: byd[r['day']].append(r)
    v=[fstar(x,al)[0] for x in byd.values() if len(x)>=8]
    if len(v)<2: return None
    m=statistics.mean(v); se=statistics.stdev(v)/math.sqrt(len(v)); t=T90[len(v)-1] if len(v)-1 in T90 else 1.7
    return round(m,2),round(m-t*se,2),round(m+t*se,2),len(v)
def report(rs,tit):
    n=len(rs)
    days=sorted(set(r['day'] for r in rs))
    print(f'== {tit}  n={n} dias={len(days)}')
    if n==0: return
    st=stats(rs)
    print('  fill any   : '+'  '.join(f"{NAME[nm]}={st[nm+'_any']:.2f}" for nm in VAR))
    print('  fill full  : '+'  '.join(f"{NAME[nm]}={st[nm+'_full']:.2f}" for nm in VAR))
    for h in (2,10,30):
        print(f'  fill<={h}s   : '+'  '.join(f"{NAME[nm]}={st[nm+f'_h{h}']:.2f}" for nm in VAR))
    print('  t1 med (ms): '+'  '.join(f"{NAME[nm]}={st[nm+'_t1med']}" for nm in VAR))
    for al in('lo','prop','hi'):
        vc=[(r['day'],)+cfill(r,al)[:2] for r in rs]
        vf=[(r['day'],)+feff(r,al)[:2] for r in rs]
        cens=sum(1 for r in rs if not cfill(r,al)[2])
        ci=dayci(vc); fi=dayci(vf)
        bc=blockci(rs,fc(al)); bf=blockci(rs,ff(al))
        def fmt(x): return 'NA' if x is None else f'{x:.3f}'
        print(f"  [{al}] c_fill pooled={fmt(pooled(vc))} dias={fmt(ci[0]) if ci else 'NA'} IC90dias=({fmt(ci[1])},{fmt(ci[2])}) IC90bloque1h={None if not bc else (round(bc[0],3),round(bc[1],3))} | f_eff pooled={fmt(pooled(vf))} dias={fmt(fi[0]) if fi else 'NA'} IC90dias=({fmt(fi[1])},{fmt(fi[2])}) IC90bloque={None if not bf else (round(bf[0],2),round(bf[1],2))} cens={cens}")
    for al in('lo','prop','hi'):
        fs=fstar(rs,al); print(f"  f* ({al}) mejor factor de cola = {fs[0]} (dist media {fs[1]:.3f}); por dias: {fstar_dias(rs,al)}; dist de opt/base/cons: "+', '.join(f"{NAME['sh_f%03d'%k]}={sum(abs(x-y) for x,y in zip(pcurve(rs,'rp_'+al),pcurve(rs,'sh_f%03d'%k)))/12:.3f}" for k in (0,50,100)))
    # acuerdo puja a puja de 'lleno <=10 s' y 'lleno completo al final' entre cada cola y cada replay
    for al in('lo','prop','hi'):
        o=[]
        for nm in ('sh_f000','sh_f050','sh_f100'):
            a10=sum(1 for r in rs if ((fillinfo(r,nm)[0] is not None and fillinfo(r,nm)[0]-r['t0']<=10000)==(fillinfo(r,'rp_'+al)[0] is not None and fillinfo(r,'rp_'+al)[0]-r['t0']<=10000)))/len(rs)
            a2=sum(1 for r in rs if ((fillinfo(r,nm)[0] is not None and fillinfo(r,nm)[0]-r['t0']<=2000)==(fillinfo(r,'rp_'+al)[0] is not None and fillinfo(r,'rp_'+al)[0]-r['t0']<=2000)))/len(rs)
            o.append(f"{NAME[nm]}: acuerdo<=2s {a2:.2f} <=10s {a10:.2f}")
        print(f'  acuerdo muestra a muestra vs replay-{al}: '+' | '.join(o))
    cm=[cfill(r,'prop')[0]/cfill(r,'prop')[1] for r in rs if cfill(r,'prop')[1]>0]
    print('  c_fill prop: mediana por muestra',round(statistics.median(cm),3),' (sin ponderar por profundidad); D0 mediana',round(statistics.median([r['D0'] for r in rs]),1))
    sm=[statistics.median([feff(r,'prop')[0]/r['D0'] for r in rs if r['D0']>0])]
    print('  f_eff prop mediana por muestra:',round(sm[0],3))
    for W in (2,5,30):
        ci=dayci([(r['day'],)+cW(r,'prop',W) for r in rs]); print(f'  c(W={W}s) prop dias={ci[0]:.3f} IC90=({ci[1]},{ci[2]})' if ci and ci[1] is not None else f'  c(W={W}s) prop {ci}')
if __name__=='__main__':
    mode=sys.argv[2] if len(sys.argv)>2 else 'celdas'
    if mode=='todo':
        for c in coins: report([r for r in rows if r['coin']==c],f'{c} TODO (agregado, solo resumen posterior)')
    else:
        for c in coins:
            for b in ['0.10-0.15','0.15-0.20','0.20-0.25','0.25-0.30']:
                for t in TR:
                    report([r for r in rows if r['coin']==c and r['b']==b and r['tr']==t],f'{c} {b} {t}')
