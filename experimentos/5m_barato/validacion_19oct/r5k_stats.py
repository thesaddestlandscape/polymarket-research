import pandas as pd,numpy as np
from math import erf,sqrt
SP='/tmp/claude-0/-root-polymarket-research/ce552a77-92f9-49c1-8c13-d01ef139d7f6/scratchpad/'
U=pd.read_pickle(SP+'R5K_U.pkl')
ins=U[U.dia<='2026-10-16'];fw=U[U.dia>='2026-10-17']
rng=np.random.default_rng(2)
def ev(x): return x.p.sum()/x.c.sum()
def boot_cierre(x,n=10000):
    g=x.groupby('fin')[['p','c']].sum();out=[]
    for _ in range(n):
        i=rng.integers(0,len(g),len(g));out.append(g.p.values[i].sum()/g.c.values[i].sum())
    return np.quantile(out,[.05,.5,.95]),np.std(out),len(g)
def boot_dia(x,n=10000):
    g=x.groupby('dia')[['p','c']].sum();out=[]
    for _ in range(n):
        i=rng.integers(0,len(g),len(g));out.append(g.p.values[i].sum()/g.c.values[i].sum())
    return np.quantile(out,[.05,.5,.95])
for nm,x in (('in-sample 09-16',ins),('forward 17-18',fw),('forward 17 sólo',U[U.dia=='2026-10-17']),('todo 09-18',U)):
    q,sd,k=boot_cierre(x);print(nm,'n',len(x),'EV pond',round(ev(x),4),'IC90 cierre',q.round(3),'SE',round(sd,3),'cierres',k,'IC90 días',boot_dia(x).round(3))
# sin 2 mejores días in-sample, sin top-20 unidades
d=ins.groupby('dia')[['p','c']].sum();d['ev']=d.p/d.c
r=d.sort_values('ev',ascending=False).iloc[2:];print('in-sample sin 2 mejores días',round(r.p.sum()/r.c.sum(),4),'días:',d.ev.round(3).to_dict())
t=ins.sort_values('p',ascending=False).iloc[20:];print('in-sample sin top-20 unidades',round(t.p.sum()/t.c.sum(),4))
# sin 14 y 15 (los dos días 0.69 y 0.41)
x=ins[~ins.dia.isin(['2026-10-14','2026-10-15'])];print('in-sample sin 14 y 15-Oct',round(ev(x),4),len(x))
# compatibilidad forward vs in-sample: dif con bootstrap por cierre independiente
def bootdif(a,b,n=10000):
    ga=a.groupby('fin')[['p','c']].sum();gb=b.groupby('fin')[['p','c']].sum();out=[]
    for _ in range(n):
        ia=rng.integers(0,len(ga),len(ga));ib=rng.integers(0,len(gb),len(gb))
        out.append(ga.p.values[ia].sum()/ga.c.values[ia].sum()-gb.p.values[ib].sum()/gb.c.values[ib].sum())
    return np.quantile(out,[.05,.5,.95]).round(3),np.mean(np.array(out)>=0)
print('forward-in_sample: IC90 y P(dif>=0)',bootdif(fw,ins))
print('forward 17 vs in-sample:',bootdif(U[U.dia=='2026-10-17'],ins))
# p-valor forward bajo H: verdad=+0.2 / +0.1 / 0 (SE cluster del forward)
q,sd,k=boot_cierre(fw)
for th in (0.2,0.1,0.0):
    z=(ev(fw)-th)/sd;p=0.5*(1+erf(z/sqrt(2)));print(f'P(EV_fw<=obs | verdad {th:+.1f}) aprox normal: z={z:.2f} p={p:.4f}')
q1,sd1,_=boot_cierre(U[U.dia=='2026-10-17'])
for th in (0.2,0.1,0.0):
    z=(ev(U[U.dia=='2026-10-17'])-th)/sd1;print(f'  solo 17: verdad {th:+.1f}: z={z:.2f} p={0.5*(1+erf(z/sqrt(2))):.4f}')
# potencia: sigma por unidad
allu=U
th=ev(allu)
res=(allu.p-th*allu.c); cbar=allu.c.mean()
sig_u=np.sqrt((res**2).mean())/cbar     # sd de EV por unidad (ponderado)
print('sigma por unidad (EV ponderado, delta) =',round(sig_u,3),' coste medio',round(cbar,2))
# por cierre (cluster): unidades por cierre
print('unidades por cierre medias',round(len(allu)/allu.fin.nunique(),3))
# clustering por cierre: deff
g=allu.groupby('fin');tot=((g.apply(lambda x:(x.p-th*x.c).sum())**2).sum()); ind=((allu.p-th*allu.c)**2).sum();print('deff cierre',round(tot/ind,3))
# unidades/día
upd=allu.groupby('dia').size().mean();print('unidades/día',round(upd,1))
for delta in (0.2,0.1,0.15):
    for pw,zb in ((0.8,0.8416),(0.5,0.0)):
        n=((1.645+zb)*sig_u/delta)**2; print(f'distinguir +{delta} de 0: potencia {pw}: n={n:.0f} unidades ≈ {n/upd:.1f} días (iid)')
# potencia por días: sd entre días de EV diario in-sample
dd=U.groupby('dia').apply(lambda x:x.p.sum()/x.c.sum());print('EV diario 09-18',dd.round(3).tolist(),'sd',round(dd.std(),3))
sd_d=dd.std()
for delta in (0.2,0.1):
    n=((1.645+0.8416)*sd_d/delta)**2;print(f'por días: distinguir +{delta} de 0 (t≈normal, sd entre días {sd_d:.2f}): {n:.1f} días')
# null: EV esperado bajo hipótesis nula por simulación (win~Bernoulli(precio unitario c/acc)), para ver la sd y max
sim=[]
pr=(allu.c/allu.acc).values; acc=allu.acc.values; c=allu.c.values
ii=np.where(allu.dia<='2026-10-16')[0]
for _ in range(5000):
    w=rng.random(len(ii))<pr[ii];p=acc[ii]*w-c[ii];sim.append(p.sum()/c[ii].sum())
sim=np.array(sim);print('NULL (precio justo, sin fee) in-sample 688 unidades: EV media',sim.mean().round(3),'sd',sim.std().round(3),'P95',np.quantile(sim,.95).round(3),' obs',round(ev(ins),3),' z',round((ev(ins)-sim.mean())/sim.std(),2))
