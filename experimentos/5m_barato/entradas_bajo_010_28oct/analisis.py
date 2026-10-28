import csv, glob, itertools, math, collections
import numpy as np
rng=np.random.default_rng(2811); B=2000
OOSD={'2026-10-23','2026-10-24','2026-10-25','2026-10-26'}
D=(0.02,0.05,0.10,0.20,0.30,0.45)
LB=[(0.01,0.03),(0.04,0.06),(0.07,0.09)]
def lbk(L):
    for i,(a,b) in enumerate(LB):
        if a-1e-9<=L<=b+1e-9: return i
    return None
def fl(x): return float('nan') if x=='' else float(x)
real=[];pla=[];inv=[]
for f in sorted(glob.glob('out/n_*.csv')):
    for r in csv.DictReader(open(f)):
        if r['kind']=='real' and r['filled']!='1':
            r={k:r[k] for k in ('kind','dia','coin','mercado','lado','L','s','win','filled','touch','hold_hyp','cost')}
        {'real':real,'pla':pla,'inv':inv}[r['kind']].append(r)
out=[]
def pr(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
days_all=sorted({r['dia'] for r in real})
pr('DIAS',len(days_all),days_all[0],days_all[-1],'real',len(real),'pla',len(pla),'inv',len(inv))
def ev(P,C): return P.sum(0)/np.maximum(C.sum(0),1e-12)
def ic90(P,C):
    nd=P.shape[0]
    if nd<2: return (float('nan'),)*2
    cnt=rng.multinomial(nd,[1/nd]*nd,size=B); e=(cnt@P)/np.maximum(cnt@C,1e-12)
    return np.nanpercentile(e,5),np.nanpercentile(e,95)
def sin2(P,C):
    t=P.sum(1) if P.ndim>1 else P; o=np.argsort(-t)[2:]
    return (P[o].sum()/max(C[o].sum(),1e-12)) if len(o) else float('nan')
def daymat(rs,valf,days):
    di={d:i for i,d in enumerate(days)}
    P=np.zeros(len(days)); C=np.zeros(len(days))
    for r in rs:
        v=valf(r)
        if v is None or v!=v: continue
        P[di[r['dia']]]+=v; C[di[r['dia']]]+=float(r['cost'])
    return P,C
def summ(name,rs,valf,days):
    isd=[d for d in days if d not in OOSD]; oo=[d for d in days if d in OOSD]
    res=[name]
    for lab,dd in (('IS',isd),('OOS',oo)):
        sub=[r for r in rs if r['dia'] in set(dd)]
        P,C=daymat(sub,valf,dd); n=sum(1 for r in sub if valf(r) is not None and valf(r)==valf(r))
        if n==0: res.append('%s n=0'%lab); continue
        e=P.sum()/max(C.sum(),1e-12); lo,hi=ic90(P[:,None],C[:,None]) if len(dd)>1 else (float('nan'),)*2
        s2=sin2(np.stack([P,C],1)[:,0:1],np.stack([P,C],1)[:,1:2]) if len(dd)>2 else float('nan')
        res.append('%s n=%d EVw=%+.3f IC90[%+.3f,%+.3f] sin2=%+.3f'%(lab,n,e,float(lo),float(hi),s2))
    pr(' | '.join(res))
hold=lambda r: fl(r['pnl_hold']) if r['filled']=='1' else None
# --- A: relleno y seleccion adversa
pr('\n== A. Modelo de relleno y seleccion adversa (hold) por L (todas las monedas), estricto')
for L in [round(.01*i,2) for i in range(1,10)]:
    rs=[r for r in real if abs(float(r['L'])-L)<1e-9]
    n=len(rs); f=[r for r in rs if r['filled']=='1']; u=[r for r in rs if r['filled']!='1']; t=[r for r in rs if r['touch']=='1']
    ef=sum(fl(r['pnl_hold']) for r in f)/max(sum(float(r['cost']) for r in f),1e-9)
    en=sum(float(r['hold_hyp']) for r in u)/max(sum(float(r['cost']) for r in u),1e-9)
    et=sum(float(r['hold_hyp']) for r in t)/max(sum(float(r['cost']) for r in t),1e-9)
    wf=np.mean([float(r['win']) for r in f]); wu=np.mean([float(r['win']) for r in u])
    tt=[(math.ceil(float(r['tfill'])/1000/300)*300-float(r['tfill'])/1000) for r in f]
    pr('L=%.2f n=%d fill=%.3f touch+cola=%.3f | acierto relleno %.3f (breakeven %.2f) no-relleno %.3f | EVw relleno %+.3f  EV no-relleno(hip) %+.3f  EV touch+cola %+.3f | t hasta cierre p10/p50/p90 %.0f/%.0f/%.0f s'%(L,n,len(f)/n,len(t)/n,wf,L,wu,ef,en,et,*np.percentile(tt,[10,50,90])))
pr('\n== A2. Por moneda x bucket de L (IS|OOS), hold estricto')
for coin in sorted({r['coin'] for r in real}):
    for bi,(a,b) in enumerate(LB):
        rs=[r for r in real if r['coin']==coin and lbk(float(r['L']))==bi]
        f=[r for r in rs if r['filled']=='1']; u=[r for r in rs if r['filled']!='1']
        summ('%s L[%.2f-%.2f] fill=%.3f nofill_EV=%+.3f'%(coin,a,b,len(f)/max(len(rs),1),sum(float(r['hold_hyp']) for r in u)/max(sum(float(r['cost']) for r in u),1e-9)),rs,hold,days_all)
pr('\n== A3. Agregado por bucket de L y por s')
for bi,(a,b) in enumerate(LB):
    for s in (30,120,210):
        rs=[r for r in real if lbk(float(r['L']))==bi and int(r['s'])==s]
        summ('L[%.2f-%.2f] s=%d'%(a,b,s),rs,hold,days_all)
# --- B: escalones
CELLS=[('base','H'),('base','D')]
for T in 'HDC':
    for i in range(6): CELLS.append(('S%d'%i,T))
    for i,j in itertools.combinations(range(6),2): CELLS.append(('L%d%d'%(i,j),T))
def cellval(r,c):
    k,T=c
    if k=='base': return fl(r['pnl_base_H']) if T=='H' else fl(r['pnl_base_D'])
    if k[0]=='S': return fl(r['pnl_s%d_%s'%(int(k[1]),T)])
    i,j=int(k[1]),int(k[2]); return (fl(r['pnl_s%d_%s'%(i,T)])+fl(r['pnl_s%d_%s'%(j,T)]))/2
filled=[r for r in real if r['filled']=='1']
pr('\n== B. Escalones fijos (sin seleccion), rellenos estrictos, por bucket de L: hold vs escalon (terminal H)')
for bi,(a,b) in enumerate(LB):
    rs=[r for r in filled if lbk(float(r['L']))==bi]
    for c in [('base','H'),('base','D'),('S0','H'),('S1','H'),('S2','H'),('S3','H'),('S5','H'),('L05','H'),('S1','D')]:
        summ('L[%.2f-%.2f] %s%s'%(a,b,c[0],c[1]),rs,lambda r,c=c: cellval(r,c),days_all)
pr('\n-- P(toque) vs cota L/g (todas monedas, bucket, IS+OOS)')
for bi,(a,b) in enumerate(LB):
    rs=[r for r in filled if lbk(float(r['L']))==bi]
    for i in range(6):
        v=[(int(r['tf_s%d'%i]),float(r['L'])/float(r['g_s%d'%i])) for r in rs if r['g_s%d'%i]!='']
        pr('L[%.2f-%.2f] d=%.2f n=%d P(toque)=%.3f cota L/g=%.3f'%(a,b,D[i],len(v),np.mean([x[0] for x in v]),np.mean([x[1] for x in v])))
# --- selection
pr('\n== B2. Seleccion IS por moneda x bucket L (celdas: s x escalon/escalera x terminal), max-statistic, OOS')
SEL=[]  # (P_days_all, C_days_all) de la celda elegida
cartera_oos=[]; cartera_is=[]
isd=[d for d in days_all if d not in OOSD]; ood=[d for d in days_all if d in OOSD]
for coin in sorted({r['coin'] for r in real}):
    for bi,(a,b) in enumerate(LB):
        rs=[r for r in filled if r['coin']==coin and lbk(float(r['L']))==bi]
        keys=[(s,c) for s in (30,120,210) for c in CELLS]
        di={d:i for i,d in enumerate(days_all)}
        P=np.zeros((len(days_all),len(keys))); C=np.zeros_like(P); N=np.zeros(len(keys))
        for r in rs:
            ds=di[r['dia']]; s=int(r['s']); cost=float(r['cost'])
            for k,c in enumerate(CELLS):
                v=cellval(r,c)
                if v==v:
                    kk=keys.index((s,c)) if False else (( (30,120,210).index(s))*len(CELLS)+k)
                    P[ds,kk]+=v; C[ds,kk]+=cost
                    if r['dia'] not in OOSD: N[kk]+=1
        ii=[di[d] for d in isd]; oi=[di[d] for d in ood]
        eis=P[ii].sum(0)/np.maximum(C[ii].sum(0),1e-12)
        ok=N>=15
        if not ok.any(): pr('%s L[%.2f-%.2f]: sin celdas con n_IS>=15'%(coin,a,b)); continue
        k=np.argmax(np.where(ok,eis,-9)); Pi,Ci=P[ii],C[ii]
        cnt=rng.multinomial(len(ii),[1/len(ii)]*len(ii),size=B)
        eb=(cnt@Pi)/np.maximum(cnt@Ci,1e-12)-eis; mx=np.where(ok,eb,-9).max(1)
        p=float((mx>=eis[k]-1e-12).mean())
        eoo=P[oi,k].sum()/max(C[oi,k].sum(),1e-12)
        pr('%s L[%.2f-%.2f] elegida s=%d %s%s nIS=%d EVw_IS=%+.3f p_maxstat=%.3f | OOS EVw=%+.3f costeOOS=%.0f'%(coin,a,b,keys[k][0],keys[k][1][0],keys[k][1][1],N[k],eis[k],p,eoo,C[oi,k].sum()))
        cartera_oos.append((P[oi,k],C[oi,k])); cartera_is.append((P[ii,k],C[ii,k]))
if cartera_oos:
    Po=sum(p for p,c in cartera_oos); Co=sum(c for p,c in cartera_oos); Pi=sum(p for p,c in cartera_is); Ci=sum(c for p,c in cartera_is)
    lo,hi=ic90(Po[:,None],Co[:,None])
    pr('CARTERA IS EVw=%+.4f | OOS EVw=%+.4f IC90 dias[%+.4f,%+.4f] por dia %s sin2=%+.4f coste OOS %.0f'%(Pi.sum()/Ci.sum(),Po.sum()/max(Co.sum(),1e-12),lo,hi,np.round(Po/np.maximum(Co,1e-12),3),sin2(np.stack([Po],1),np.stack([Co],1)),Co.sum()))
# --- C: pares
pr('\n== C. Pares A+B (mismo L,s): relleno conjunto, hold')
idx=collections.defaultdict(dict)
for r in real: idx[(r['mercado'],r['L'],r['s'])][r['lado']]=r
for L in [round(.01*i,2) for i in range(1,10)]:
    ks=[v for k,v in idx.items() if abs(float(k[1])-L)<1e-9 and len(v)==2]
    pa=np.mean([v['YES']['filled']=='1' for v in ks]); pb=np.mean([v['NO']['filled']=='1' for v in ks])
    both=[v for v in ks if v['YES']['filled']=='1' and v['NO']['filled']=='1']
    pj=len(both)/len(ks)
    pnl=sum(fl(v['YES']['pnl_hold'])+fl(v['NO']['pnl_hold']) for v in both); cost=sum(float(v['YES']['cost'])+float(v['NO']['cost']) for v in both)
    pr('L=%.2f pares=%d P(YES)=%.3f P(NO)=%.3f P(conjunta)=%.4f producto=%.4f | n_both=%d EVw_par=%s'%(L,len(ks),pa,pb,pj,pa*pb,len(both),'%+.3f'%(pnl/cost) if cost else 'NA'))
# --- D: controles
pr('\n== D. Controles (hold y +0,05/+0,10 H) por bucket de precio de compra')
for bi,(a,b) in enumerate(LB):
    for nm,rs0 in (('real',filled),('placebo',pla),('inversion',inv)):
        rs=[r for r in rs0 if lbk(float(r['L']))==bi] if nm!='inversion' else [r for r in rs0 if a-1e-9<=float(r['L'])<=b+1e-9]
        if nm=='inversion': rs=[r for r in rs0 if True]
        if nm=='inversion' and bi>0: continue
        for c in [('base','H'),('S1','H'),('S2','H')]:
            summ('%s L[%.2f-%.2f] %s%s'%(nm,a,b,*c),rs,lambda r,c=c: cellval(r,c),days_all)
open('analisis.txt','w').write('\n'.join(out))
