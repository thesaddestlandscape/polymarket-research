#!/usr/bin/env python3
"""x2: evalúa PREREG.md (sha256 af2902aa…). Lee agentes_datos/b_vs_poblacion/F_D.pkl."""
import pandas as pd,numpy as np,json,glob,os,datetime as dt
O='/mnt/HC_Volume_106538179/agentes_datos/b_vs_poblacion/'; REF=0.0265
rng=np.random.default_rng(20261025)
des=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json'))
for _D in ['20','21','22']:
    _T=pd.read_csv(os.path.dirname(os.path.abspath(__file__))+f'/../../cola_vs_cruce/datos/tok_2026-10-{_D}.csv',dtype={'mid':str})
    for _m,_v in _T.drop_duplicates('mid')[['mid','des']].dropna().values: des.setdefault(_m,_v)
for _m,_v in json.load(open(os.path.dirname(os.path.abspath(__file__))+'/../datos/des_gamma.json')).items(): des.setdefault(_m,_v)  # ADENDA1
F=pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(O+'F_2026-10-*.pkl'))],ignore_index=True)
F['dia']=pd.to_datetime((F.fin-300)//86400*86400,unit='s').dt.strftime('%m-%d')
o=F.mid.astype(str).map(des.get)
F['win']=np.where(o.isna(),np.nan,np.where(((o=='YES')&(F.lc==0))|((o=='NO')&(F.lc==1)),1.0,0.0))
# --- estructura de tx (sobre TODOS los rellenos maker, cualquier pc) ---
F['lvl']=(F.pc*100).round().astype(int)
g=F.groupby(['tx','mid','lc'],observed=True)
F['minpc']=g.pc.transform('min'); F['SWEEP']=F.minpc<=F.pc-0.005
gl=F.groupby(['tx','mid','lc','lvl'],observed=True)
F['ULT']=F.li==gl.li.transform('max'); F['PRI']=F.li==gl.li.transform('min'); F['nmk']=gl.w.transform('nunique')
F['MULTI']=F.nmk>=2
Bd=F[F.isB]; print('B rellenos totales',len(Bd),'por dia',Bd.dia.value_counts().sort_index().to_dict(),'monedas',Bd.coin.value_counts().to_dict())
print('B pc',Bd.pc.describe().round(3).to_dict())
dB=set(Bd.dia); cB=set(Bd.coin)
base=F[F.dia.isin(dB)&F.coin.isin(cB)&(F.pc>=0.05)&(F.pc<=0.30)&(F.sec>=0)&(F.sec<=300)].copy()
cov=base.coste[base.win.notna()].sum()/base.coste.sum(); covB=base.coste[base.isB&base.win.notna()].sum()/base.coste[base.isB].sum()
print(f'cobertura desenlace (coste) P+B {cov:.4f}  B {covB:.4f}; B fuera de banda/sec: {len(Bd)-base.isB.sum()}')
base=base[base.win.notna()].reset_index(drop=True)
base['pnl']=base.acc*base.win-base.coste
base['sb']=base.coin.astype(int)*1000+np.clip((base.pc/0.05).astype(int),1,6)*100+np.clip((base.sec//60).astype(int),0,4)*10+np.where(base.acc<=5,0,np.where(base.acc<=10,1,2))
B=base[base.isB].reset_index(drop=True); P=base[~base.isB].reset_index(drop=True)
ev=lambda d: d.pnl.sum()/d.coste.sum()
print(f'\nB: n={len(B)} coste={B.coste.sum():.1f} pnl={B.pnl.sum():.2f} EV={ev(B):+.4f} | P: n={len(P)} coste={P.coste.sum():.0f} EV={ev(P):+.4f} wallets={P.w.nunique()}')
print('EV P por dia',P.groupby('dia').apply(ev).round(4).to_dict(),' B por dia',B.groupby('dia').apply(ev).round(3).to_dict(),B.groupby('dia').size().to_dict())
print('EV P por moneda',P.groupby('coin').apply(ev).round(4).to_dict(),' B',B.groupby('coin').apply(ev).round(3).to_dict(),B.groupby('coin').size().to_dict())
# --- 1. cola ---
def frac(d,col): return d.coste[d[col]].sum()/d.coste.sum(), d[col].mean()
for col in ['SWEEP','MULTI']: print(f'{col}: B €{frac(B,col)[0]:.3f} filas{frac(B,col)[1]:.3f} | P €{frac(P,col)[0]:.3f} filas{frac(P,col)[1]:.3f}')
for nm,d in (('B',B),('P',P)):
    m=d[d.MULTI]; print(f'{nm} MULTI n={len(m)} P(ULT)={m.ULT.mean():.3f} P(PRI)={m.PRI.mean():.3f} nmk medio {m.nmk.mean():.2f}')
for nm,d in (('B',B),('P',P)):
    for col in ['SWEEP','MULTI']:
        print(f'  {nm} EV {col}=1 {ev(d[d[col]]):+.4f} (n={d[col].sum()}) {col}=0 {ev(d[~d[col]]):+.4f} (n={(~d[col]).sum()})')
    m=d[d.MULTI]; print(f'  {nm} MULTI: ULT {ev(m[m.ULT&~m.PRI]):+.4f} (n={(m.ULT&~m.PRI).sum()}) PRI {ev(m[m.PRI&~m.ULT]):+.4f} (n={(m.PRI&~m.ULT).sum()})')
# --- 2. emparejado mercado-momento ---
P=P.sort_values(['mid','lc','ts']).reset_index(drop=True); key=P.mid.values*2+P.lc.values; kts=P.ts.values
evm=np.full(len(B),np.nan); evml=np.full(len(B),np.nan); nm60=np.zeros(len(B),int); sel=np.zeros(len(P),bool)
for i,r in B.iterrows():
    k=r.mid*2+r.lc; a=np.searchsorted(key,k,'left'); b=np.searchsorted(key,k,'right')
    if a==b: continue
    s=a+np.searchsorted(kts[a:b],r.ts-60,'left'); e=a+np.searchsorted(kts[a:b],r.ts+60,'right')
    if e>s:
        q=P.iloc[s:e]; evm[i]=q.pnl.sum()/q.coste.sum(); nm60[i]=e-s; sel[s:e]=True
        ql=q[(q.lvl-r.lvl).abs()<=1]
        if len(ql): evml[i]=ql.pnl.sum()/ql.coste.sum()
B['evm']=evm; B['evml']=evml
ok=B.evm.notna(); okl=B.evml.notna()
print(f'\nEmparejado M60: B con pareja {ok.sum()}/{len(B)}; EV_B (con pareja) {ev(B[ok]):+.4f}; EV M60 por € de B {np.sum(B.coste[ok]*B.evm[ok])/B.coste[ok].sum():+.4f}; unión {ev(P[sel]):+.4f} (n={sel.sum()})')
print(f'M60L (nivel ±1c): con pareja {okl.sum()}; EV_B {ev(B[okl]):+.4f} vs M60L {np.sum(B.coste[okl]*B.evml[okl])/B.coste[okl].sum():+.4f}')
# --- 3. descomposición ---
sP=P.groupby('sb').agg(c=('coste','sum'),p=('pnl','sum')); sB=B.groupby('sb').agg(c=('coste','sum'),p=('pnl','sum'))
j=sB.join(sP,rsuffix='P',how='left'); cubre=j.cP.notna(); 
evrw=(j.c[cubre]*(j.pP[cubre]/j.cP[cubre])).sum()/j.c[cubre].sum()
print(f'\nestratos B {len(sB)}, cubiertos en P {cubre.sum()} (€ {j.c[cubre].sum()/j.c.sum():.3f})')
def rw(cols):
    kP=P.groupby(cols).agg(c=('coste','sum'),p=('pnl','sum')); kB=B.groupby(cols).coste.sum().rename('cb')
    jj=kB.to_frame().join(kP,how='left').dropna(); return (jj.cb*jj.p/jj.c).sum()/jj.cb.sum()
for nm,cols in (('moneda',[B.coin.name]),('precio',['pcb']),('T',['tb']),('tamaño',['zb'])):
    pass
for d in (B,P):
    d['pcb']=np.clip((d.pc/0.05).astype(int),1,6); d['tb']=np.clip((d.sec//60).astype(int),0,4); d['zb']=np.where(d.acc<=5,0,np.where(d.acc<=10,1,2))
for nm,cols in (('moneda',['coin']),('precio',['pcb']),('T',['tb']),('tamaño',['zb'])): print(f'  solo {nm}: EV_P reponderado {rw(cols):+.4f} (Δ vs EV_P {rw(cols)-ev(P):+.4f})')
evM=np.sum(B.coste[ok]*B.evm[ok])/B.coste[ok].sum()
a=ev(P)-REF; b=evrw-ev(P); c=evM-evrw; dd=ev(B)-evM
print(f'G=EV_B-REF={ev(B)-REF:+.4f} = (a) periodo+moneda {a:+.4f} + (b) composición {b:+.4f} + (c) mercado-momento {c:+.4f} + (d) residuo precio/cola {dd:+.4f}')
print('B y P por tamaño/T/precio (EV, n):')
for col in ['zb','tb','pcb']:
    print(' ',col,'B',{k:(round(ev(v),3),len(v)) for k,v in B.groupby(col)},'P',{k:round(ev(v),4) for k,v in P.groupby(col)})
# --- bootstrap por cierre y día ---
def boot(unit,R=2000):
    U=np.unique(np.concatenate([B[unit].values,P[unit].values])); ix={u:i for i,u in enumerate(U)}; n=len(U)
    bi=B[unit].map(ix).values; pi_=P[unit].map(ix).values
    S=sorted(set(B.sb)); sx={s:i for i,s in enumerate(S)}; K=len(S)
    def agg(idx,vals,n,K=None,sidx=None):
        if K is None: return np.bincount(idx,vals,minlength=n)
        return np.bincount(idx*K+sidx,vals,minlength=n*K).reshape(n,K)
    Bp=agg(bi,B.pnl.values,n); Bc=agg(bi,B.coste.values,n)
    Bm=agg(bi,np.where(ok,B.coste*B.evm,0),n); Bmc=agg(bi,np.where(ok,B.coste,0),n)
    Bsc=agg(bi,B.coste.values,n,K,B.sb.map(sx).values)
    pm=P.sb.isin(sx).values; Pp_s=agg(pi_[pm],P.pnl.values[pm],n,K,P.sb[pm].map(sx).values); Pc_s=agg(pi_[pm],P.coste.values[pm],n,K,P.sb[pm].map(sx).values)
    Pp=agg(pi_,P.pnl.values,n); Pc=agg(pi_,P.coste.values,n)
    Bsw=agg(bi,B.coste.values*B.SWEEP.values,n); Psw=agg(pi_,P.coste.values*P.SWEEP.values,n)
    out=[]
    for r in range(R):
        wv=rng.multinomial(n,np.ones(n)/n).astype(float)
        evB=wv@Bp/(wv@Bc); evP=wv@Pp/(wv@Pc)
        ps=wv@Pp_s; cs=wv@Pc_s; bs=wv@Bsc; m=cs>0; evrw_=(bs[m]*ps[m]/cs[m]).sum()/bs[m].sum()
        evM_=wv@Bm/(wv@Bmc)
        out.append((evB,evP,evrw_-evP,evM_-evrw_,evB-evM_,evB-evP,wv@Bsw/(wv@Bc)-wv@Psw/(wv@Pc)))
    out=np.array(out); q=np.nanpercentile(out,[5,95],axis=0)
    names=['EV_B','EV_P','(b)comp','(c)merc-mom','(d)residuo','EV_B-EV_P','ΔP(SWEEP)€']
    print(f'IC90 por {unit} (n={n}): '+'; '.join(f'{nm} ({q[0,i]:+.4f},{q[1,i]:+.4f})' for i,nm in enumerate(names)))
boot('fin'); boot('dia')
# --- 4. contrafactual cola ---
sh=P.groupby('SWEEP').coste.sum()/P.coste.sum(); eb=B.groupby('SWEEP').apply(ev)
cf=sum(sh[k]*eb.get(k,np.nan) for k in sh.index)
print(f'\nContrafactual EV_B con mezcla SWEEP de P: {cf:+.4f} (EV_B {ev(B):+.4f}; cierra {(cf-ev(B))/(-(c+dd)) if (c+dd)!=0 else np.nan:.2f} de (c)+(d))')
# --- placebo pseudo-B ---
grp=P.groupby('sb').indices; cnt=B.sb.value_counts()
pe=[];ps=[]
for r in range(1000):
    idx=np.concatenate([rng.choice(grp[s],k,replace=True) for s,k in cnt.items() if s in grp])
    q=P.iloc[idx]; pe.append(ev(q)); ps.append(q.coste[q.SWEEP].sum()/q.coste.sum())
pe=np.array(pe); ps=np.array(ps)
print(f'placebo pseudo-B (estratos iguales, n={len(B)}): EV media {pe.mean():+.4f} p5 {np.percentile(pe,5):+.4f} p95 {np.percentile(pe,95):+.4f}; P(EV<=EV_B)={np.mean(pe<=ev(B)):.3f} | SWEEP€ media {ps.mean():.3f} p95 {np.percentile(ps,95):.3f} P(>=B)={np.mean(ps>=frac(B,"SWEEP")[0]):.3f}')
# sin los 2 mejores días de B
bd=B.groupby('dia').pnl.sum().sort_values(); keep=bd.index[:-2] if len(bd)>2 else bd.index
print('EV_B sin 2 mejores días',round(ev(B[B.dia.isin(keep)]),4),'| EV_P mismos días',round(ev(P[P.dia.isin(keep)]),4))
B.to_csv(O+'B_rellenos_anotados.csv',index=False)
