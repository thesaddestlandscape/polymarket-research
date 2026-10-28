import glob, itertools, math
import numpy as np, pandas as pd
rng=np.random.default_rng(2811); B=2000
OOSD={'2026-10-23','2026-10-24','2026-10-25','2026-10-26'}
D=(0.02,0.05,0.10,0.20,0.30,0.45); LB=[(0.01,0.03),(0.04,0.06),(0.07,0.09)]
SV=(30,120,210)
# celdas
CELLS=[('base','H'),('base','D')]
for T in 'HDC':
    for i in range(6): CELLS.append(('S%d'%i,T))
    for i,j in itertools.combinations(range(6),2): CELLS.append(('L%d%d'%(i,j),T))
def cellmat(X):
    M=np.full((len(X),len(CELLS)),np.nan,dtype=np.float32)
    for k,(c,T) in enumerate(CELLS):
        if c=='base': M[:,k]=X['pnl_base_H' if T=='H' else 'pnl_base_D'].values
        elif c[0]=='S': M[:,k]=X['pnl_s%s_%s'%(c[1],T)].values
        else: M[:,k]=(X['pnl_s%s_%s'%(c[1],T)].values+X['pnl_s%s_%s'%(c[2],T)].values)/2
    return M
def cname(c): return c[0]+c[1]
allr=[];F=[];PL=[];IV=[];MFl=[]
files=sorted(glob.glob('out/n_*.csv'))
CAT_D=pd.CategoricalDtype([f[-14:-4] for f in files])
COINS=sorted(pd.read_csv(files[0],usecols=['coin']).coin.unique())
CAT_C=pd.CategoricalDtype(COINS); CAT_L=pd.CategoricalDtype(['YES','NO'])
for f in files:
    d=pd.read_csv(f,dtype={'mercado':np.int64,'dia':CAT_D,'coin':CAT_C,'lado':CAT_L,'kind':'category'})
    r=d[d.kind=='real']
    allr.append(r[['dia','coin','mercado','lado','L','s','sh','win','filled','touch','hold_hyp','cost','tfill']].copy())
    ff=r[r.filled==1].drop(columns=['bb0','bs0','ask0','kind'])
    MFl.append(cellmat(ff)); ff=ff.drop(columns=[c for c in ff.columns if c.startswith('pnl_s') or c.startswith('tfge') or c in ('pnl_base_H','pnl_base_D')])
    fc=[c for c in ff.columns if ff[c].dtype==np.float64 and c not in ('tfill','cost','pnl_hold','L')]
    ff[fc]=ff[fc].astype(np.float32); F.append(ff)
    PL.append(d[d.kind=='pla'].drop(columns=['bb0','bs0','ask0','kind'])); IV.append(d[d.kind=='inv'].drop(columns=['bb0','bs0','ask0','kind']))
R=pd.concat(allr,ignore_index=True); R['lado']=R.lado.astype(CAT_L); F=pd.concat(F,ignore_index=True); PL=pd.concat(PL,ignore_index=True); IV=pd.concat(IV,ignore_index=True)
for X in (R,F): X['lb']=np.select([X.L<=0.035,X.L<=0.065],[0,1],2)
for X in (PL,): X['lb']=np.select([X.L<0.035,X.L<0.065],[0,1],2)
IV['lb']=0
out=[]
def pr(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
days=sorted(R.dia.astype(str).unique()); di={d:i for i,d in enumerate(days)}
isd=np.array([d not in OOSD for d in days]); 
pr('DIAS',len(days),days[0],days[-1],'unidades',len(R),'rellenos estrictos',len(F),'placebo',len(PL),'inversion',len(IV))
def dayPC(dia,val,cost):
    ix=dia.astype(str).map(di).values; ok=~np.isnan(val)
    P=np.bincount(ix[ok],weights=val[ok],minlength=len(days)); C=np.bincount(ix[ok],weights=cost[ok],minlength=len(days)); return P,C
def ic90(P,C):
    nd=len(P)
    if nd<2: return (np.nan,np.nan)
    cnt=rng.multinomial(nd,[1/nd]*nd,size=B); e=(cnt@P)/np.maximum(cnt@C,1e-12); return np.percentile(e,5),np.percentile(e,95)
def s2(P,C):
    o=np.argsort(-P)[2:]; return P[o].sum()/max(C[o].sum(),1e-12) if len(o)>2 else np.nan
def summ(name,X,val):
    res=[name]; 
    for lab,mask in (('IS',isd),('OOS',~isd)):
        dd=[d for d,m in zip(days,mask) if m]; sub=X[X.dia.astype(str).isin(dd)]; v=val[X.dia.astype(str).isin(dd).values]
        ok=~np.isnan(v)
        if ok.sum()==0: res.append(lab+' n=0'); continue
        P,C=dayPC(sub.dia,v,sub.cost.values); P=P[mask];C=C[mask]
        lo,hi=ic90(P,C); res.append('%s n=%d EVw=%+.3f IC90[%+.3f,%+.3f] sin2=%+.3f'%(lab,ok.sum(),P.sum()/max(C.sum(),1e-12),lo,hi,s2(P,C)))
    pr(' | '.join(res))
pr('\n== A. Relleno estricto y seleccion adversa (hold) por L, todas monedas')
R['isf']=R.filled==1
for L in np.round(np.arange(1,10)*0.01,2):
    x=R[np.isclose(R.L,L)]; f=x[x.isf]; u=x[~x.isf]; t=x[x.touch==1]
    ef=F[np.isclose(F.L,L)]; ev_f=ef.pnl_hold.sum()/ef.cost.sum()
    tt=300*np.ceil(f.tfill/1000/300)-f.tfill/1000
    pr('L=%.2f n=%d fill=%.3f touch+cola=%.3f | acierto relleno %.3f (breakeven %.2f) no-relleno %.3f | EVw relleno %+.3f | EV no-relleno(hip) %+.3f | EV touch+cola %+.3f | s hasta cierre p10/p50/p90 %.0f/%.0f/%.0f'%(L,len(x),len(f)/len(x),len(t)/len(x),f.win.mean(),L,u.win.mean(),ev_f,u.hold_hyp.sum()/u.cost.sum(),t.hold_hyp.sum()/t.cost.sum(),*np.percentile(tt,[10,50,90])))
pr('\n== A2. moneda x bucket L: hold relleno estricto (IS|OOS) + fill + EV no-relleno')
for coin in COINS:
    for bi,(a,b) in enumerate(LB):
        x=R[(R.coin==coin)&(R.lb==bi)]; f=F[(F.coin==coin)&(F.lb==bi)]; u=x[~x.isf]
        summ('%s L[%.2f-%.2f] fill=%.3f noFillEV=%+.3f'%(coin,a,b,len(f)/len(x),u.hold_hyp.sum()/u.cost.sum()),f,f.pnl_hold.values)
pr('\n== A3. bucket L x s')
for bi,(a,b) in enumerate(LB):
    for s in SV:
        f=F[(F.lb==bi)&(F.s==s)]; summ('L[%.2f-%.2f] s=%d fill=%.3f'%(a,b,s,len(f)/len(R[(R.lb==bi)&(R.s==s)])),f,f.pnl_hold.values)
MF=np.concatenate(MFl); del MFl
import gc; gc.collect()
pr('\n== B. escalones fijos (sin seleccion) por bucket L, rellenos estrictos')
for bi,(a,b) in enumerate(LB):
    idx=(F.lb==bi).values; X=F[idx]
    for c in [('base','H'),('base','D'),('S0','H'),('S1','H'),('S2','H'),('S3','H'),('S5','H'),('L05','H'),('S1','D')]:
        summ('L[%.2f-%.2f] %s'%(a,b,cname(c)),X,MF[idx,CELLS.index(c)])
pr('\n-- P(toque estricto) vs cota L/g')
for bi,(a,b) in enumerate(LB):
    X=F[F.lb==bi]
    for i in range(6):
        g=X['g_s%d'%i].values; ok=~np.isnan(g)
        pr('L[%.2f-%.2f] +%.2f n=%d P(toque)=%.3f cota L/g=%.3f'%(a,b,D[i],ok.sum(),np.nanmean(X['tf_s%d'%i].values[ok]),np.mean(X.L.values[ok]/g[ok])))
pr('\n== B2. seleccion IS por moneda x bucket L (celdas s x escalon/escalera x terminal), max-statistic; OOS')
ii=np.where(isd)[0]; oi=np.where(~isd)[0]
CP_o=np.zeros(len(days)); CC_o=np.zeros(len(days)); CP_i=np.zeros(len(days)); CC_i=np.zeros(len(days)); sel_rows=[]
for coin in COINS:
    for bi,(a,b) in enumerate(LB):
        idx=((F.coin==coin)&(F.lb==bi)).values; X=F[idx]; M=MF[idx]; ix=X.dia.astype(str).map(di).values; cost=X.cost.values; sv=X.s.values
        nc=len(CELLS)*3; P=np.zeros((len(days),nc)); C=np.zeros_like(P); N=np.zeros(nc)
        for si,s in enumerate(SV):
            m=sv==s
            for k in range(len(CELLS)):
                v=M[m,k]; ok=~np.isnan(v); kk=si*len(CELLS)+k
                P[:,kk]=np.bincount(ix[m][ok],weights=v[ok],minlength=len(days)); C[:,kk]=np.bincount(ix[m][ok],weights=cost[m][ok],minlength=len(days))
                N[kk]=(ok&np.isin(ix[m],ii)).sum()
        eis=P[ii].sum(0)/np.maximum(C[ii].sum(0),1e-12); okc=N>=15
        if not okc.any(): pr(coin,bi,'sin celdas'); continue
        k=int(np.argmax(np.where(okc,eis,-9)))
        cnt=rng.multinomial(len(ii),[1/len(ii)]*len(ii),size=B); eb=(cnt@P[ii])/np.maximum(cnt@C[ii],1e-12)-eis
        p=float((np.where(okc,eb,-9).max(1)>=eis[k]-1e-12).mean()); eoo=P[oi,k].sum()/max(C[oi,k].sum(),1e-12)
        pr('%s L[%.2f-%.2f] elegida s=%d %s nIS=%d EVw_IS=%+.3f p_maxstat=%.3f | OOS EVw=%+.3f coste OOS=%.0f'%(coin,a,b,SV[k//len(CELLS)],cname(CELLS[k%len(CELLS)]),N[k],eis[k],p,eoo,C[oi,k].sum()))
        CP_o+=np.where(~isd,P[:,k],0); CC_o+=np.where(~isd,C[:,k],0); CP_i+=np.where(isd,P[:,k],0); CC_i+=np.where(isd,C[:,k],0)
Po=CP_o[~isd];Co=CC_o[~isd]; lo,hi=ic90(Po,Co)
pr('CARTERA IS EVw=%+.4f | OOS EVw=%+.4f IC90 dias[%+.4f,%+.4f] por dia %s sin2=%+.4f coste OOS(3 niveles L apilados)=%.0f EUR'%(CP_i[isd].sum()/CC_i[isd].sum(),Po.sum()/Co.sum(),lo,hi,np.round(Po/np.maximum(Co,1e-12),3),s2(Po,Co),Co.sum()))
# capacidad cartera: 1 nivel L por mercado-lado -> coste/3 ; dias OOS
nd=(~isd).sum()
for nm,e in (('cons(IC90 inf)',lo),('base(punto)',Po.sum()/Co.sum()),('opt(IC90 sup)',hi)):
    pr('capacidad %s: EVw %+.3f x coste/dia %.0f EUR (1 nivel L por mercado-lado) = %+.0f EUR/dia = %+.0f EUR/anio (objetivo 548 EUR/dia)'%(nm,e,Co.sum()/3/nd,e*Co.sum()/3/nd,e*Co.sum()/3/nd*365))
pr('\n== C. pares A+B (mismo L,s): probabilidad conjunta')
Y=R[R.lado=='YES'][['dia','mercado','L','s','filled','cost']].merge(R[R.lado=='NO'][['dia','mercado','L','s','filled','cost']],on=['dia','mercado','L','s'],suffixes=('_y','_n'))
fy=F[F.lado=='YES'][['dia','mercado','L','s','pnl_hold']]; fn=F[F.lado=='NO'][['dia','mercado','L','s','pnl_hold']]
Y=Y.merge(fy,on=['dia','mercado','L','s'],how='left').merge(fn,on=['dia','mercado','L','s'],how='left',suffixes=('_y','_n'))
for L in np.round(np.arange(1,10)*0.01,2):
    y=Y[np.isclose(Y.L,L)]; pa=(y.filled_y==1).mean(); pb=(y.filled_n==1).mean(); bo=y[(y.filled_y==1)&(y.filled_n==1)]
    ev_='NA' if len(bo)==0 else '%+.3f'%((bo.pnl_hold_y+bo.pnl_hold_n).sum()/(bo.cost_y+bo.cost_n).sum())
    pr('L=%.2f pares=%d P(YES)=%.3f P(NO)=%.3f P(conjunta)=%.4f producto=%.4f n_both=%d EVw_par_hold=%s'%(L,len(y),pa,pb,len(bo)/len(y),pa*pb,len(bo),ev_))
pr('\n== D. controles por bucket de precio de compra (hold, +0,05, +0,10 H)')
for bi,(a,b) in enumerate(LB):
    for nm,X in (('real',F[F.lb==bi]),('placebo',PL[PL.lb==bi]),('inversion',IV)):
        if nm=='inversion' and bi>0: continue
        Mx=MF[(F.lb==bi).values] if nm=='real' else cellmat(X)
        for c in [('base','H'),('S1','H'),('S2','H')]:
            summ('%s L[%.2f-%.2f] %s'%(nm,a,b,cname(c)),X,Mx[:,CELLS.index(c)])
open('analisis.txt','w').write('\n'.join(out))
