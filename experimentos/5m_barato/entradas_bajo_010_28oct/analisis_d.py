import glob, numpy as np, pandas as pd
rng=np.random.default_rng(2811); B=2000
OOSD={'2026-10-23','2026-10-24','2026-10-25','2026-10-26'}
S5={('BTC',0),('ETH',0),('ETH',1)}   # celdas elegidas en el analisis original (S5D); el resto baseD, s=210
df=pd.concat([pd.read_csv(f,dtype={'mercado':np.int64}) for f in sorted(glob.glob('outD/d_*.csv'))],ignore_index=True)
df['lb']=np.select([df.L<=0.035,df.L<=0.065],[0,1],2); days=sorted(df.dia.unique()); di={d:i for i,d in enumerate(days)}
isd=np.array([d not in OOSD for d in days]); df['di']=df.dia.map(di)
out=[]
def pr(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
def ic90(P,C):
    nd=len(P); cnt=rng.multinomial(nd,[1/nd]*nd,size=B); e=(cnt@P)/np.maximum(cnt@C,1e-12); return np.percentile(e,5),np.percentile(e,95)
def agg(x,col):
    ok=~x[col].isna(); P=np.bincount(x.di[ok],weights=x[col][ok],minlength=len(days)); C=np.bincount(x.di[ok],weights=x.cost[ok],minlength=len(days)); return P,C
pr('dias',len(days),'filas rellenos',len(df))
pr('dstat (todas las unidades rellenas, s=210):',df[df.s==210].dstat.value_counts(normalize=True).round(3).to_dict())
for lb in range(3):
    x=df[(df.s==210)&(df.lb==lb)]; pr('  bucket',lb,'n',len(x),x.dstat.value_counts(normalize=True).round(3).to_dict(),'bs mediana (ok/partial)',x[x.dstat.isin(['ok','partial'])].bs.median())
pr('\n== baseD s=210 por bucket (todas monedas): viejo vs nuevo (IS | OOS)')
for lb in range(3):
    x=df[(df.s==210)&(df.lb==lb)]
    for col in ('pnl_oldD','pnl_newD'):
        P,C=agg(x,col); r=[]
        for lab,m in (('IS',isd),('OOS',~isd)):
            lo,hi=ic90(P[m],C[m]); r.append('%s EVw=%+.3f IC90[%+.3f,%+.3f]'%(lab,P[m].sum()/C[m].sum(),lo,hi))
        pr('bucket',lb,col,' | '.join(r))
pr('\n== CARTERA con las celdas elegidas ANTES (sin reseleccion)')
res={}
for col_old,col_new,nm in (('pnl_oldD','pnl_newD','baseD'),('pnl_oldS5D','pnl_newS5D','S5D')):
    pass
for ver in ('old','new'):
    Po=np.zeros(len(days)); Co=np.zeros(len(days)); nsel=0; stat=[]
    for coin in sorted(df.coin.unique()):
        for lb in range(3):
            x=df[(df.coin==coin)&(df.lb==lb)&(df.s==210)]
            col=('pnl_%sS5D' if (coin,lb) in S5 else 'pnl_%sD')%ver
            P,C=agg(x,col); Po+=P; Co+=C; nsel+=len(x); stat.append(x.dstat)
            if ver=='new':
                Pm,Cm=P[~isd],C[~isd]; pr('  %s b%d %s OOS EVw=%+.3f IS EVw=%+.3f coste OOS=%.0f'%(coin,lb,col,Pm.sum()/max(Cm.sum(),1e-12),P[isd].sum()/max(C[isd].sum(),1e-12),Cm.sum()))
    m=~isd; lo,hi=ic90(Po[m],Co[m]); t=Po[m]; o=np.argsort(-t)[2:]
    pr('CARTERA %s: IS EVw=%+.4f | OOS EVw=%+.4f IC90 dias[%+.4f,%+.4f] por dia %s sin2mejores=%+.4f coste OOS=%.0f n_unidades=%d'%(ver,Po[isd].sum()/Co[isd].sum(),Po[m].sum()/Co[m].sum(),lo,hi,np.round(Po[m]/Co[m],3),t[o].sum()/Co[m][o].sum(),Co[m].sum(),nsel))
    if ver=='new':
        s=pd.concat(stat); pr('  dstat en unidades de la cartera:',s.value_counts(normalize=True).round(3).to_dict())
        for nm,e in (('cons',lo),('base',Po[m].sum()/Co[m].sum()),('opt',hi)):
            pr('  capacidad %s: EVw %+.3f x coste/dia %.0f (1 nivel L por mercado-lado) = %+.0f EUR/dia (obj 548)'%(nm,e,Co[m].sum()/3/4,e*Co[m].sum()/3/4))
open('analisis_d.txt','w').write('\n'.join(out))
