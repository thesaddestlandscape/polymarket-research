#!/usr/bin/env python3
"""a1: evalúa H1, H1-WF, H2, H3 de PREREG.md (sha en PREREG.sha256). Lee datos/M_*.pkl, T_*.pkl."""
import pandas as pd,numpy as np,json,os,sys
D=os.path.dirname(os.path.abspath(__file__))+'/../datos/'
rng=np.random.default_rng(20261025)
DAYS=[f'2026-10-{i:02d}' for i in range(6,22)]; DESC=DAYS[:6]; HOLD=DAYS[6:]
if os.environ.get('PRUEBA'): DAYS=DAYS[:4]; DESC=DAYS[:2]; HOLD=DAYS[2:]  # solo depuración, días DESC
des=json.load(open('/root/polymarket-research-datalogs/mapa_escala/des.json'))
def win(mid,lc):
    o=pd.Series(mid).map(lambda m: des.get(str(m))).values
    return np.where(o==None,np.nan,np.where(((o=='YES')&(lc==0))|((o=='NO')&(lc==1)),1.0,0.0))
M=[];T=[];WDL=[];G={}; WU=[]; cov=[0,0,0,0]
import datetime as _dt
LAB={int(_dt.datetime(2026,10,int(x[-2:]),tzinfo=_dt.timezone.utc).timestamp()//86400):x for x in DAYS}
for d in DAYS:
    m=pd.read_pickle(D+f'M_{d}.pkl').drop(columns=['w','tk','oh'])
    m['win']=win(m.mid.values,m.lc.values); cov[0]+=m.coste[~np.isnan(m.win)].sum(); cov[1]+=m.coste.sum(); m=m[~np.isnan(m.win)]
    m['pnl']=(m.acc*m.win-m.coste).astype(np.float32); m['reb']=(0.014*(1-m.pc)*m.coste).astype(np.float32)
    m=m[['mid','lc','coin','fin','ts','sec','pc','coste','pnl','reb']]; M.append(m)
    t=pd.read_pickle(D+f'T_{d}.pkl'); cats=t.w.cat.categories
    for c in cats:
        if c not in G: G[c]=len(WU); WU.append(c)
    mp=np.array([G[c] for c in cats],dtype=np.int32); t['w']=mp[t.w.cat.codes.values]
    t['win']=win(t.mid.values,t.lc.values); cov[2]+=t.coste[~np.isnan(t.win)].sum(); cov[3]+=t.coste.sum(); t=t[~np.isnan(t.win)]
    t['pnl']=(t.acc*t.win-t.coste-t.fee).astype(np.float32)
    t=t[['w','mid','lc','ts','fin','coste','pnl']]; t['coste']=t.coste.astype(np.float32)
    di_=((t.fin.values-300)//86400); tt=t[np.array([LAB.get(int(x))==d for x in np.unique(di_)])[np.searchsorted(np.unique(di_),di_)]]
    tu=tt.groupby(['w','mid','lc'],sort=False).agg(c=('coste','sum'),p=('pnl','sum')).reset_index()
    wd=tu.groupby('w').agg(n=('c','size'),c=('c','sum'),p=('p','sum')).reset_index(); wd['dia']=d; WDL.append(wd)
    T.append(t); del t,m,tt,tu
M=pd.concat(M,ignore_index=True); T=pd.concat(T,ignore_index=True)
for X in (M,):
    X['di']=((X.fin.values-300)//86400).astype(np.int64); X['dia']=X.di.map(LAB)
M=M[M.dia.notna()].reset_index(drop=True)
cov_M=cov[0]/cov[1]; cov_T=cov[2]/cov[3]
print(f'cobertura desenlace (coste) M {cov_M:.4f} T {cov_T:.4f}; M fills {len(M)} coste {M.coste.sum():.0f}; T {len(T)} coste {T.coste.sum():.0f}',flush=True)
# ---------- skill tomadoras ----------
WD=pd.concat(WDL,ignore_index=True)
def sel(days,ev_min=0.03,ev_max=None):
    x=WD[WD.dia.isin(days)]
    g=x.groupby('w').agg(n=('n','sum'),c=('c','sum'),p=('p','sum'),da=('dia','nunique'),dp=('p',lambda s:(s>0).sum()))
    base=g[(g.n>=30)&(g.c>=200)&(g.da>=3)]
    ev=base.p/base.c
    if ev_max is not None: return set(base[ev<=ev_max].index), set(base.index)
    return set(base[(ev>=ev_min)&(base.dp>=np.ceil(2*base.da/3))].index), set(base.index)
S,A=sel(DESC); BAD,_=sel(DESC,ev_max=-0.03)
print(f'S={len(S)} pool A={len(A)} BAD={len(BAD)}',flush=True)
# ---------- índices de ventana (una vez) ----------
import gc
_mid=T.mid.values; _ts=T.ts.values; _fin=T.fin.values; _lc=T.lc.values; _c=T.coste.values; _w=T.w.values
del T; gc.collect()
o=np.lexsort((_ts,_mid))
kT=(_mid[o]*1e4+np.clip(_ts[o]-_fin[o]+5000,0,9999)); del _ts,_fin
assert (np.diff(kT)>=0).all()
sY=np.where(_lc[o]==0,_c[o],-_c[o]).astype(np.float64); Tw=_w[o]; del _mid,_lc,_c,_w,o; gc.collect()
kF=M.mid.values*1e4+(M.ts.values-M.fin.values+5000)
lo=np.searchsorted(kT,kF-33,side='left'); hi=np.searchsorted(kT,kF-3,side='right')
sgn=np.where(M.lc.values==0,-1.0,1.0)   # flujo CONTRA el lado comprado por el maker
codes=lambda ws: np.fromiter(ws,dtype=np.int64)
def F(mask):
    cs=np.concatenate([[0.0],np.cumsum(sY*mask)])
    return sgn*(cs[hi]-cs[lo])
isH=M.dia.isin(HOLD).values; isD=~isH
def ev(sel_):
    return M.pnl.values[sel_].sum()/M.coste.values[sel_].sum()
def daysum(mask):
    g=pd.DataFrame(dict(d=M.dia.values[mask],p=M.pnl.values[mask],c=M.coste.values[mask])).groupby('d').sum()
    return g
def boot_exceso(flag,base,key='dia',B=2000):
    # EXCESO = EV(no bandera) - EV(todo) dentro de base
    k=M[key].values[base]; f=flag[base]; p=M.pnl.values[base]; c=M.coste.values[base]
    g=pd.DataFrame(dict(k=k,pa=p,ca=c,pu=np.where(f,0,p),cu=np.where(f,0,c),pf=np.where(f,p,0),cf=np.where(f,c,0))).groupby('k').sum()
    ex=g.pu.sum()/g.cu.sum()-g.pa.sum()/g.ca.sum(); dl=g.pf.sum()/max(g.cf.sum(),1e-9)-g.pu.sum()/g.cu.sum()
    a=g.values; n=len(a); bs=[]
    for _ in range(B):
        s=a[rng.integers(0,n,n)].sum(0); bs.append(s[2]/s[3]-s[0]/s[1])
    lo_,hi_=np.percentile(bs,[5,95])
    # sin 2 mejores días (por EXCESO diario)
    exd=g.pu/g.cu-g.pa/g.ca; keep=exd.sort_values().index[:-2]; gg=g.loc[keep]
    ex2=gg.pu.sum()/gg.cu.sum()-gg.pa.sum()/gg.ca.sum()
    return dict(EXCESO=ex,ic90=(lo_,hi_),sin2=ex2,DELTA=dl,EV_all=g.pa.sum()/g.ca.sum(),EV_flag=g.pf.sum()/max(g.cf.sum(),1e-9),EV_unflag=g.pu.sum()/g.cu.sum(),frac_coste_flag=g.cf.sum()/g.ca.sum(),dias_pos=int((exd>0).sum()),n_dias=len(g))
def nunits(flag,base):
    x=M[base&flag]; return x.groupby(['mid','lc']).ngroups, x.dia.nunique()
def report(name,flag,base):
    r=boot_exceso(flag,base); rc=boot_exceso(flag,base,key='fin',B=1000)
    nu,nd=nunits(flag,base)
    print(f'{name}: n_unid_bandera={nu} dias={nd} frac€={r["frac_coste_flag"]:.3f} EV_all={r["EV_all"]:+.4f} EV_flag={r["EV_flag"]:+.4f} EV_noflag={r["EV_unflag"]:+.4f} DELTA={r["DELTA"]:+.4f} EXCESO={r["EXCESO"]:+.4f} IC90dia=({r["ic90"][0]:+.4f},{r["ic90"][1]:+.4f}) IC90cierre=({rc["ic90"][0]:+.4f},{rc["ic90"][1]:+.4f}) sin2={r["sin2"]:+.4f} diasEXC>0={r["dias_pos"]}/{r["n_dias"]}',flush=True)
    return r
inS=np.isin(Tw,codes(S)); FS=F(inS); flagS=FS>0
print('\n== H1 (S fijo DESC, medido HOLD) ==')
rH=report('H1 S HOLD',flagS,isH)
btc=M.coin.values==0
report('H1 S HOLD BTC',flagS,isH&btc); report('H1 S HOLD ALT',flagS,isH&~btc)
report('H1 S DESC (in-sample, descriptivo)',flagS,isD)
FA=F(np.ones(len(Tw))); report('CTRL todas tomadoras F_all>0 HOLD',FA>0,isH)
inB=np.isin(Tw,codes(BAD)); report('INV malas F_BAD>0 HOLD',F(inB)>0,isH)
# placebo
Al=np.array(sorted(A)); k=len(S); ds=[]
Ph=M.pnl.values[isH]; Ch=M.coste.values[isH]
for b in range(500):
    pick=rng.choice(Al,size=min(k,len(Al)),replace=False); fl=(F(np.isin(Tw,codes(pick)))>0)[isH]
    if fl.sum()==0: ds.append(0); continue
    ds.append(Ph[fl].sum()/Ch[fl].sum()-Ph[~fl].sum()/Ch[~fl].sum())
ds=np.array(ds); p=(ds<=rH['DELTA']).mean()
print(f'placebo DELTA: media {ds.mean():+.4f} sd {ds.std():.4f} p5 {np.percentile(ds,5):+.4f}; obs {rH["DELTA"]:+.4f}; p={p:.3f}',flush=True)
# concentración top wallet de S
sh=[]
for w in S:
    fl=(F(Tw==w)>0)&isH&flagS; sh.append((M.coste.values[fl].sum(),w))
sh.sort(reverse=True); tot=M.coste.values[flagS&isH].sum()
print('top S wallets por coste bandera:',[(WU[w][:10],round(c/tot,3)) for c,w in sh[:3]],flush=True)
# ---------- H1-WF ----------
print('\n== H1-WF ==')
flagW=np.zeros(len(M),bool); base=np.zeros(len(M),bool)
for i,d in enumerate(DAYS):
    if i<3: continue
    Sd,_=sel(DAYS[:i]); md=(M.dia.values==d)
    if not Sd: continue
    f=F(np.isin(Tw,codes(Sd)))>0; flagW|=(f&md); base|=md
report('H1-WF 09-21',flagW,base); report('H1-WF HOLD 12-21',flagW,base&isH)
# ---------- H2 ----------
print('\n== H2 nichos ==')
hb=(pd.to_datetime(M.ts,unit='s').dt.hour.values//6); bb=(M.pc.values>=0.15).astype(int)
cell=M.coin.values.astype(int)*8+hb*2+bb
from scipy import stats
def cell_stats(mask):
    g=pd.DataFrame(dict(c=cell[mask],d=M.dia.values[mask],p=M.pnl.values[mask],k=M.coste.values[mask])).groupby(['c','d']).sum().reset_index()
    out={}
    for c,x in g.groupby('c'):
        evd=x.p/x.k; ev_=x.p.sum()/x.k.sum()
        t=stats.ttest_1samp(evd,0) if len(x)>2 else None
        pv=t.pvalue/2 if (t is not None and t.statistic>0) else 1.0
        out[c]=(ev_,pv,len(x),x.k.sum())
    return out
cd_=cell_stats(isD); cs=sorted(cd_); pv=np.array([cd_[c][1] for c in cs])
o=np.argsort(pv); m=len(pv); q=np.empty(m); q[o]=np.minimum.accumulate((pv[o]*m/np.arange(1,m+1))[::-1])[::-1]
selc=[c for c,qq in zip(cs,q) if qq<0.10 and cd_[c][0]>0]
CO=['BTC','ETH','SOL','XRP','DOGE','BNB']
lab=lambda c:f'{CO[c//8]}/h{(c%8)//2*6:02d}/{"0.15-0.30" if c%2 else "0.05-0.15"}'
print('celdas seleccionadas DESC (q<0,10):',[lab(c) for c in selc])
print('top 8 celdas DESC por p:',[(lab(cs[i]),round(cd_[cs[i]][0],3),round(pv[i],4)) for i in o[:8]])
if selc:
    fl=np.isin(cell,selc); r=boot_exceso(~fl,isH)  # EV_unflag = EV de la unión seleccionada
    nu=M[isH&fl].groupby(['mid','lc']).ngroups
    evu=r['EV_unflag']
    rb=[]; allc=np.array(cs)
    for b in range(1000):
        pk=rng.choice(allc,len(selc),replace=False); ff=np.isin(cell,pk)&isH; rb.append(M.pnl.values[ff].sum()/M.coste.values[ff].sum())
    worst=[cs[i] for i in np.argsort([cd_[c][0] for c in cs])[:len(selc)]]; fw=np.isin(cell,worst)&isH
    g=daysum(isH&fl); evd=(g.p/g.c); bs=[g.iloc[rng.integers(0,len(g),len(g))].sum() for _ in range(2000)]; bs=[x.p/x.c for x in bs]
    keep=evd.sort_values().index[:-2]; gg=g.loc[keep]
    print(f'H2 HOLD unión: EV={evu:+.4f} n_unid={nu} dias={len(g)} IC90dia=({np.percentile(bs,5):+.4f},{np.percentile(bs,95):+.4f}) sin2={gg.p.sum()/gg.c.sum():+.4f} p_placebo={(np.array(rb)>=evu).mean():.3f} inversion EV={M.pnl.values[fw].sum()/M.coste.values[fw].sum():+.4f} reb={M.reb.values[isH&fl].sum()/M.coste.values[isH&fl].sum():+.4f}')
# ---------- H3 ----------
print('\n== H3 descriptivo moneda x lado x banda x T ==')
rem=300-M.sec.values; tb=np.digitize(rem,[60,120,240]); 
c3=M.coin.values.astype(int)*16+M.lc.values.astype(int)*8+bb*4+tb
def evc(mask):
    g=pd.DataFrame(dict(c=c3[mask],p=M.pnl.values[mask],k=M.coste.values[mask])).groupby('c').sum(); return g.p/g.k, g.k
eD,kD=evc(isD); eH,kH=evc(isH); j=eD.index.intersection(eH.index)
rho=stats.spearmanr(eD[j],eH[j]).correlation
print(f'Spearman DESC↔HOLD 96 celdas: {rho:+.3f} (n={len(j)})')
both=[(c,eD[c],eH[c],kH[c]) for c in j if eD[c]>0.02 and eH[c]>0.02 and kH[c]>20000]
TB=['0-60','60-120','120-240','240-300']
print('celdas >+0,02 en DESC y HOLD (coste HOLD>20k):',[(f'{CO[c//16]}/{"Up" if (c%16)//8==0 else "Down"}/{"0.15-0.30" if (c%8)//4 else "0.05-0.15"}/T{TB[c%4]}',round(a,3),round(b,3),int(k)) for c,a,b,k in both])
for nm,mk in [('BTC',btc),('ALT',~btc)]:
    for lc in (0,1):
        for t_ in range(4):
            mm=mk&(M.lc.values==lc)&(tb==t_)
            print(f'  {nm} {"Up" if lc==0 else "Down"} T{TB[t_]}: DESC {ev(mm&isD):+.4f} HOLD {ev(mm&isH):+.4f} costeHOLD {M.coste.values[mm&isH].sum():.0f}')
# ---------- H4 (ADENDA1) ----------
print('\n== H4 flujo de todas las tomadoras ==')
keep=FA>0
for nm,mk in [('ALL',np.ones(len(M),bool)),('BTC',btc),('ALT',~btc)]:
    r=boot_exceso(~keep,isH&mk); rc=boot_exceso(~keep,isH&mk,key='fin',B=1000)
    # EXCESO aquí = EV(keep) - EV(todo) porque bandera=~keep
    print(f'H4 {nm} HOLD: EV_keep={r["EV_unflag"]:+.4f} EV_cancel={r["EV_flag"]:+.4f} EV_all={r["EV_all"]:+.4f} EXCESO={r["EXCESO"]:+.4f} IC90dia=({r["ic90"][0]:+.4f},{r["ic90"][1]:+.4f}) IC90cierre=({rc["ic90"][0]:+.4f},{rc["ic90"][1]:+.4f}) sin2={r["sin2"]:+.4f} dias>0={r["dias_pos"]}/{r["n_dias"]} frac€keep={1-r["frac_coste_flag"]:.3f}')
for nm,mk in [('F<0',FA<0),('F=0',FA==0),('F>0',FA>0)]:
    for per,pm in [('DESC',isD),('HOLD',isH)]:
        print(f'  {nm} {per}: EV={ev(mk&pm):+.4f} coste={M.coste.values[mk&pm].sum():.0f} reb={M.reb.values[mk&pm].sum()/M.coste.values[mk&pm].sum():+.4f}')
nu=M[isH&keep].groupby(['mid','lc']).ngroups; print('n unidades keep HOLD',nu)
# placebo: permutar signo dentro de dia x moneda
gid=M.di.values*10+M.coin.values.astype(np.int64); obs=ev(isH&keep)-ev(isH); pl=[]
IX=[np.where((gid==g)&isH)[0] for g in np.unique(gid[isH])]
for b in range(200):
    kk=keep.copy()
    for ix in IX: kk[ix]=rng.permutation(keep[ix])
    pl.append(ev(isH&kk)-ev(isH))
print(f'H4 placebo: media {np.mean(pl):+.4f} p95 {np.percentile(pl,95):+.4f} obs {obs:+.4f} p={(np.array(pl)>=obs).mean():.3f}')
# EV diario keep vs all
g1=daysum(isH&keep); g0=daysum(isH); print('diario EXCESO:',' '.join(f'{d[5:]}:{(g1.p[d]/g1.c[d]-g0.p[d]/g0.c[d]):+.3f}' for d in g0.index))
