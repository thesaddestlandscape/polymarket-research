import csv, glob, itertools, sys, math
import numpy as np
rng=np.random.default_rng(2811)
OOSD={'2026-10-23','2026-10-24','2026-10-25','2026-10-26'}
EDG=[0,.10,.15,.20,.25,.30,1.0]; BN=['<0.10','0.10-0.15','0.15-0.20','0.20-0.25','0.25-0.30','>=0.30']
D=(0.05,0.10,0.15,0.20,0.30,0.45); B=2000
def bk(p):
    for i in range(6):
        if p<EDG[i+1]: return i
    return 5
rows=[]; seen=set()
for f in sorted(glob.glob('out/e_*.csv')):
    for r in csv.DictReader(open(f)):
        k=(r['kind'],r['mercado'],r['lado'],r['p0'] if r['kind']=='pla' else '')
        if k in seen: continue
        seen.add(k); rows.append(r)
def fl(x): return float('nan') if x=='' else float(x)
# celdas
CELLS=[('base','H'),('base','D')]
for T in 'HDC':
    for i in range(6): CELLS.append(('S%d'%i,T))
    for i,j in itertools.combinations(range(6),2): CELLS.append(('L%d%d'%(i,j),T))
def mat(rs):
    n=len(rs); M=np.full((n,len(CELLS)),np.nan)
    for a,r in enumerate(rs):
        v={}
        v[('base','H')]=fl(r['pnl_base_H']); v[('base','D')]=fl(r['pnl_base_D'])
        for T in 'HDC':
            s=[fl(r['pnl_s%d_%s'%(i,T)]) for i in range(6)]
            for i in range(6): v[('S%d'%i,T)]=s[i]
            for i,j in itertools.combinations(range(6),2): v[('L%d%d'%(i,j),T)]=(s[i]+s[j])/2
        for c,k in enumerate(CELLS): M[a,c]=v[k]
    return M
def prep(rs):
    return dict(M=mat(rs),cost=np.array([float(r['cost']) for r in rs]),day=np.array([r['dia'] for r in rs]),
                coin=np.array([r['coin'] for r in rs]),bk=np.array([bk(float(r['p0'])) for r in rs]),
                p0=np.array([float(r['p0']) for r in rs]))
def daysum(M,cost,day,days):
    di={d:i for i,d in enumerate(days)}; ix=np.array([di[d] for d in day])
    valid=~np.isnan(M); P=np.zeros((len(days),M.shape[1])); C=np.zeros_like(P)
    for c in range(M.shape[1]):
        np.add.at(P[:,c],ix,np.where(valid[:,c],M[:,c],0)); np.add.at(C[:,c],ix,np.where(valid[:,c],cost,0))
    return P,C,valid.sum(0)
def ev(P,C): return P.sum(0)/np.maximum(C.sum(0),1e-12)
def boot(P,C,b=B):
    nd=P.shape[0]; cnt=rng.multinomial(nd,[1/nd]*nd,size=b)
    return (cnt@P)/np.maximum(cnt@C,1e-12), cnt
def ic90(P,C):
    if P.shape[0]<2: return (float('nan'),float('nan'))
    e,_=boot(P,C); return np.nanpercentile(e,5),np.nanpercentile(e,95)
def sin2(P,C):
    t=P.sum(1); o=np.argsort(-t)[2:]
    return P[o].sum()/max(C[o].sum(),1e-12) if len(o) else float('nan')
real=[r for r in rows if r['kind']=='real']
R=prep(real); out=[]
def pr(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
isd=np.array([d not in OOSD for d in R['day']])
pr('FILAS real',len(real),'IS',isd.sum(),'OOS',(~isd).sum(),'dias IS',len(set(R['day'][isd])),'OOS',len(set(R['day'][~isd])))
# Tabla base por moneda x bucket
pr('\n## HOLD (sin escalera) por moneda x bucket: n, EVw IS / OOS')
coins=sorted(set(R['coin']))
cH=CELLS.index(('base','H')); cD=CELLS.index(('base','D'))
sel=[]
pr('coin bucket n_IS n_OOS HOLD_IS HOLD_OOS | mejor_celda_IS EV_IS pmax | OOS: EVw IC90 sin2 n dias | toque estricto IS/p0/g')
for co in coins:
    for b in range(6):
        m=(R['coin']==co)&(R['bk']==b)
        mi=m&isd; mo=m&~isd
        if mi.sum()<15: 
            if m.sum()>0: pr(co,BN[b],'n_IS=%d n_OOS=%d'%(mi.sum(),mo.sum()),'-> n<15 IS, sin conclusion'); 
            continue
        days=sorted(set(R['day'][mi])); P,C,nv=daysum(R['M'][mi],R['cost'][mi],R['day'][mi],days)
        e=ev(P,C)
        el=[c for c in range(2,len(CELLS)) if nv[c]>=15]
        best=max(el,key=lambda c:e[c])
        # max-stat bootstrap centrado
        Pc=P-e*C
        bm,_=boot(Pc,C); mx=np.nanmax(bm[:,el],axis=1); p=float((mx>=e[best]-1e-12).mean())
        hold_is=e[cH]
        Po,Co,nvo=(daysum(R['M'][mo],R['cost'][mo],R['day'][mo],sorted(set(R['day'][mo]))) if mo.sum() else (None,None,None))
        if Po is not None:
            eo=ev(Po,Co); lo,hi=ic90(Po[:, [best]],Co[:, [best]]); s2=sin2(Po[:,[best]],Co[:,[best]])
            hold_o=eo[cH]; txt='%+.3f (%+.3f,%+.3f) sin2=%+.3f n=%d d=%d'%(eo[best],lo,hi,s2,nvo[best],Po.shape[0])
            sel.append((co,b,best,e[best],p,mi.sum(),mo.sum(),Po[:,best].sum(),Co[:,best].sum(),Po.shape[0],eo[best],lo,hi))
        else: hold_o=float('nan'); txt='sin OOS'
        pr(co,BN[b],mi.sum(),mo.sum(),'%+.3f'%hold_is,'%+.3f'%hold_o,'|',CELLS[best],'%+.3f'%e[best],'p=%.3f'%p,'| OOS',txt)
# Escalones agregados fijos (sin seleccion), todos las monedas, por terminal
pr('\n## EV por escalon (agregado, celdas fijas, SIN seleccion) EVw IS | OOS | P(toque estricto) IS vs p0/g')
for T in 'HDC':
  for i in range(6):
    c=CELLS.index(('S%d'%i,T)); out_=[]
    for nm,mk in (('IS',isd),('OOS',~isd)):
        days=sorted(set(R['day'][mk])); P,C,nv=daysum(R['M'][mk],R['cost'][mk],R['day'][mk],days)
        lo,hi=ic90(P[:,[c]],C[:,[c]]); out_.append('%s %+.3f (%+.3f,%+.3f) sin2 %+.3f n=%d'%(nm,ev(P,C)[c],lo,hi,sin2(P[:,[c]],C[:,[c]]),nv[c]))
    pr('d=%.2f %s'%(D[i],T),' | '.join(out_))
# toque vs martingala por moneda
pr('\n## P(toque) vs cota martingala p0/g, por moneda (todas las filas reales con g valido)')
for i in range(6):
    t=[];m_=[];tg=[];co_=[]
    for r in real:
        if r['g_s%d'%i]=='' : continue
        t.append(float(r['tf_s%d'%i])); tg.append(float(r['tfge_s%d'%i])); m_.append(float(r['p0'])/float(r['g_s%d'%i])); co_.append(r['coin'])
    t=np.array(t);m_=np.array(m_);tg=np.array(tg);co_=np.array(co_)
    s='d=%.2f n=%d estricto=%.3f (>=g %.3f) cota=%.3f |'%(D[i],len(t),t.mean(),tg.mean(),m_.mean())
    for co in coins:
        k=co_==co
        if k.sum()>=15: s+=' %s %.3f/%.3f(n=%d)'%(co,t[k].mean(),m_[k].mean(),k.sum())
    pr(s)
# controles
pr('\n## Controles (celdas fijas H/D/C de escalon d=0.10 y 0.20; agregado): real vs placebo(taker aleatorio) vs inversion(complemento)')
for kind in ('real','pla','inv'):
    rs=[r for r in rows if r['kind']==kind]
    if not rs: continue
    X=prep(rs); days=sorted(set(X['day'])); P,C,nv=daysum(X['M'],X['cost'],X['day'],days); e=ev(P,C)
    s=kind+' n=%d base_H=%+.3f base_D=%+.3f'%(len(rs),e[cH],e[cD])
    for i in (1,3):
        for T in 'HD': c=CELLS.index(('S%d'%i,T)); s+=' S%d%s=%+.3f(n=%d)'%(i,T,e[c],nv[c])
    pr(s)
# seleccion agregada OOS y capacidad
pr('\n## Seleccion IS por moneda x bucket aplicada a OOS (cartera de celdas seleccionadas)')
if sel:
    nOOS=len(set(R['day'][~isd])); pn=sum(s[7] for s in sel); cn=sum(s[8] for s in sel)
    pr('celdas seleccionadas',len(sel),'con p_max<0.05 en IS:',sum(1 for s in sel if s[4]<0.05),'| OOS agregado EVw=%+.4f  pnl=%.2f coste=%.2f (%d dias)'%(pn/cn,pn,cn,nOOS))
    for s in sel: pr(' ',s[0],BN[s[1]],CELLS[s[2]],'IS %+.3f p=%.3f nIS=%d | OOS EVw %+.3f (%+.3f,%+.3f) nOOS=%d d=%d'%(s[3],s[4],s[5],s[10],s[11],s[12],s[6],s[9]))
    ev_o=pn/cn; cost_day=cn/nOOS
    for nm,e_ in (('cons(0 si IC90lo<0)',0.0),('base (punto OOS)',ev_o)):
        pr('capacidad',nm,'EVw=%+.4f coste/dia=%.1f -> %.1f EUR/dia, %.0f EUR/año (5 acc, solo celdas seleccionadas)'%(e_,cost_day,e_*cost_day,e_*cost_day*365))
    if ev_o>0: pr('para 548 EUR/dia hace falta coste/dia=%.0f (x%.0f el actual)'%(548/ev_o,548/ev_o/cost_day))
else: pr('sin celdas seleccionadas')
open('out/analisis.txt','w').write('\n'.join(out))
pr('\n## EXTRA sanidad y capacidad')
for i,T in ((0,'H'),(1,'H'),(3,'H'),(5,'H')):
    t=np.array([float(r['tf_s%d'%i]) if r['g_s%d'%i]!='' else np.nan for r in real]); g=np.array([fl(r['g_s%d'%i]) for r in real]); w=np.array([float(r['win']) for r in real]); p0=np.array([float(r['p0']) for r in real])
    a=t==1; b=t==0
    pr('d=%.2f tocadas n=%d: win=%.3f  g=%.3f  p0=%.3f | no tocadas n=%d: win=%.3f p0=%.3f'%(D[i],a.sum(),w[a].mean(),g[a].mean(),p0[a].mean(),b.sum(),w[b].mean(),p0[b].mean()))
# cartera seleccionada: IC90 por dias OOS agregado y escenario opt
mo=~isd; days=sorted(set(R['day'][mo])); Pt=np.zeros(len(days)); Ct=np.zeros(len(days))
for s in sel:
    co,b,best=s[0],s[1],s[2]; m=mo&(R['coin']==co)&(R['bk']==b)
    P,C,_=daysum(R['M'][m],R['cost'][m],R['day'][m],days); Pt+=P[:,best]; Ct+=C[:,best]
e,_=boot(Pt[:,None],Ct[:,None]); lo,hi=np.percentile(e,[5,95]); pr('cartera OOS EVw %+.4f IC90 (%+.4f,%+.4f) por dia: %s'%(Pt.sum()/Ct.sum(),lo,hi,np.round(Pt/Ct,3)))
cd=Ct.sum()/len(days)
pr('capacidad anual (5 acc): cons=%.0f  base=%.0f  opt(IC90 sup)=%.0f EUR/año; coste desplegado/dia=%.0f'%(max(lo,0)*cd*365,(Pt.sum()/Ct.sum())*cd*365,hi*cd*365,cd))
for co in coins:
    m=(R['coin']==co); pr(co,'fills/dia OOS %.0f coste/dia %.0f | HOLD EVw IS %+.3f OOS %+.3f'%((m&mo).sum()/4,R['cost'][m&mo].sum()/4,R['M'][m&isd,cH].sum()/R['cost'][m&isd].sum(),R['M'][m&mo,cH].sum()/R['cost'][m&mo].sum()))
open('out/analisis.txt','w').write('\n'.join(out))
