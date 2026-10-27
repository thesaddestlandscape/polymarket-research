import sys, json, numpy as np, pandas as pd
sys.path.insert(0,'.'); from lib import *
import warnings; warnings.filterwarnings('ignore')
OUT=[]
def P(*a):
    s=' '.join(str(x) for x in a); OUT.append(s); print(s,flush=True)
des=json.load(open('desenl_all.json')); X=load_raw(); W=load_W()
dias=sorted(X.dia.unique()); P('dias cargados',dias[0],dias[-1],len(dias),'tokens',len(X))
P('cobertura desenlace por dia (T180 lag250 todos tokens):'); 
Y=prep(view(X),W,des)
cob=Y.groupby('dia').agg(tok=('mid','size'),des=('gana',lambda s:s.notna().mean()),rpre=('rpre',lambda s:s.notna().mean()),vivo=('vivo','mean'),ask_ok=('ask',lambda s:s.notna().mean()))
P(cob.round(3).T.to_string())
ALT=['ETH','SOL','XRP']; BTC=['BTC']
RNG=np.random.default_rng(20261024)
def fmt_ic(ic): return f'({ic[0]:+.3f},{ic[1]:+.3f})'
def h1(Uall,label,perm=True,nperm=1000,full=True):
    """H1: Delta=EV(CON)-EV(CONTRA). Uall incluye NEU. Todo ponderado por EUR (sum pnl / sum coste)."""
    U=Uall[Uall.cls.isin(['CON','CONTRA'])]; nC=(U.cls=='CON').sum(); nK=(U.cls=='CONTRA').sum()
    if nC<20 or nK<20: P(f'  {label}: n CON {nC} CONTRA {nK} (<20, no concluye)'); return None
    d0,icc,ncl=boot_delta(U,'cierre'); _,icd,nd=boot_delta(U,'dia',seed=2)
    a=U[U.cls=='CON']; b=U[U.cls=='CONTRA']
    r=dict(delta=d0,icc=icc,icd=icd,nC=nC,nK=nK,evC=ev(a.pnl,a.cst),evK=ev(b.pnl,b.cst))
    s=f'  {label}: n CON {nC} CONTRA {nK} (cierres {ncl}, dias {nd}) EV(CON) {r["evC"]:+.3f} EV(CONTRA) {r["evK"]:+.3f} Delta {d0:+.3f} IC90cierre {fmt_ic(icc)} IC90dia {fmt_ic(icd)}'
    if full:
        dd=U.groupby('dia').apply(lambda g: delta(g) if (g.cls=='CON').sum()>=3 and (g.cls=='CONTRA').sum()>=3 else np.nan).dropna()
        r['dias_neg']=(dd<0).sum(); r['dias_pos']=(dd>0).sum(); r['ndias']=len(dd)
        srt=dd.sort_values(); w2n=srt.index[:2]; w2p=srt.index[-2:]
        r['sin2neg']=delta(U[~U.dia.isin(w2n)]); r['sin2pos']=delta(U[~U.dia.isin(w2p)])
        s+=f'\n      dias Delta<0 {r["dias_neg"]}/{len(dd)}, >0 {r["dias_pos"]}/{len(dd)}; sin 2 dias mas negativos {r["sin2neg"]:+.3f}; sin 2 dias mas positivos {r["sin2pos"]:+.3f}'
    P(s); return r
def placebo(Uall,Yall,coins,nperm=1000,seed=11):
    """Placebo de VENTANA: permuta rpre entre ventanas del mismo dia x moneda (todas las ventanas, no solo las de banda), recalcula CON/CONTRA y repite Delta/R0/R1/R2."""
    rng=np.random.default_rng(seed)
    win=Yall[Yall.coin.isin(coins)].drop_duplicates(['coin','tmin'])[['coin','tmin','dia','rpre']].dropna(subset=['rpre']).reset_index(drop=True)
    grp=pd.factorize(win.dia+win.coin)[0]; win['wid']=np.arange(len(win))
    U=Uall.merge(win[['coin','tmin','wid']],on=['coin','tmin'],how='inner'); sg=np.where(U.lado=='YES',1.0,-1.0)
    R=U.R.values; pnl=U.pnl.values; cst=U.cst.values; rp=win.rpre.values
    def stats(rpre_w):
        rs=sg*rpre_w[U.wid.values]; con=rs>=7.7; ctr=rs<=-7.7
        d=pnl[con].sum()/cst[con].sum()-pnl[ctr].sum()/cst[ctr].sum()
        r0=-pnl[con].sum(); r1=-pnl[con&(R=='TREND')].sum(); r2=-pnl[con&np.isin(R,['TREND','MIXTO'])].sum()
        return d,r0,r1,r2
    obs=stats(rp); res=np.empty((nperm,4))
    for i in range(nperm):
        key=rng.random(len(win))+grp; order=np.argsort(key); # dentro de cada grupo, permutacion
        perm=np.empty(len(win),dtype=int); 
        # indices ordenados por (grupo, azar) y por (grupo, posicion): asignar rpre del 'order' a posiciones ordenadas por grupo
        pos=np.lexsort((np.arange(len(win)),grp)); perm[pos]=rp[order]
        res[i]=stats(perm)
    return obs,res
def h3(Uall,label,Yall,coins,nperm=1000):
    Uc=Uall[Uall.cls=='CON']; Uk=Uall[Uall.cls=='CONTRA']; tot=Uall
    obs,res=placebo(Uall,Yall,coins,nperm)
    # p Delta: una cola en la direccion observada y dos colas
    pdl=(res[:,0]<=obs[0]).mean(); pdh=(res[:,0]>=obs[0]).mean()
    P(f'  [{label}] placebo de ventana (rpre permutado dentro de dia x moneda, {nperm} perm): Delta obs {obs[0]:+.3f}; media perm {res[:,0].mean():+.3f}; p(Delta_perm<=obs) {pdl:.3f}; p(Delta_perm>=obs) {pdh:.3f}')
    out={}
    for k,(nm,mask) in enumerate((('R0 CON',Uc.index==Uc.index),('R1 CON&TREND',(Uc.R=='TREND').values),('R2 CON&(TREND|MIXTO)',Uc.R.isin(['TREND','MIXTO']).values)),start=1):
        S=Uc[mask]
        if len(S)<20: P(f'  [{label}] {nm}: n {len(S)} (<20)'); continue
        dP=-S.pnl.sum(); g=S.groupby('cierre').pnl.sum().values; bs=np.array([-g[RNG.integers(0,len(g),len(g))].sum() for _ in range(3000)])
        dd=-S.groupby('dia').pnl.sum(); b2=dd.sort_values(ascending=False).index[:2]; sin2=dd.drop(b2).sum()
        # EV por EUR: retenido (no saltado) vs todo
        keep=Uall.drop(S.index); evall=ev(Uall.pnl,Uall.cst); evkeep=ev(keep.pnl,keep.cst); ret=keep.cst.sum()/Uall.cst.sum()
        # inversion: saltar CONTRA con la misma tasa de skip por (dia,moneda)
        Si=Uk; dPi=-Si.pnl.sum()
        p_up=(res[:,k]>=dP).mean(); p_dn=(res[:,k]<=dP).mean()
        out[nm]=dict(n=len(S),dP=dP,p=p_up)
        P(f'  [{label}] {nm}: n saltadas {len(S)} (coste {S.cst.sum():.0f}) EV saltadas {ev(S.pnl,S.cst):+.3f}; dP=-PnL saltadas {dP:+.1f} (x5 acc {5*dP:+.0f}) IC90cierre ({np.percentile(bs,5):+.1f},{np.percentile(bs,95):+.1f}); placebo media {res[:,k].mean():+.1f}, p(dP_perm>=obs) {p_up:.3f} p(<=obs) {p_dn:.3f}; dias dP>0 {int((dd>0).sum())}/{len(dd)}; sin 2 mejores dias {sin2:+.1f}')
        P(f'        EV/EUR todo {evall:+.3f} -> retenido {evkeep:+.3f} (dEV {evkeep-evall:+.3f}, retiene {100*ret:.0f} % del EUR)')
    P(f'  [{label}] inversion R0 (saltar CONTRA, n {len(Uk)}): dP {-Uk.pnl.sum():+.1f}; EV retenido {ev(Uall.drop(Uk.index).pnl,Uall.drop(Uk.index).cst):+.3f}')
    return out
def full(coins,label,desde,hasta,nperm=1000,thr=7.7,kind='ask',lo=.10,hi=.30,minsz=0,YY=None,perm=True):
    YY=Y if YY is None else YY; U=units(YY[YY.dia.between(desde,hasta)],coins,kind,lo,hi,minsz)
    nuni=len(U); P(f'\n## {label} [{desde}..{hasta}] unidades U1 {nuni}, dias {U.dia.nunique()}, cierres {U.cierre.nunique()}, coste {U.cst.sum():.0f}, EV/EUR todas {ev(U.pnl,U.cst):+.4f}; ask medio {U.ask.mean():.3f}; CON {(U.cls=="CON").sum()} CONTRA {(U.cls=="CONTRA").sum()} NEU {(U.cls=="NEU").sum()}')
    r=h1(U,'H1 Delta',full=True)
    if perm and r: h3(U,label,YY[YY.dia.between(desde,hasta)],coins,nperm)
    return U,r
if __name__=='__main__':
    which=sys.argv[1]
    if which=='A':   # reproduccion de P-REAL y extension
        U,r=full(ALT,'ALTS ETH/SOL/XRP (reproduccion P-REAL)','2026-10-05','2026-10-21',nperm=500)
        U,r=full(ALT,'ALTS 22-23 Oct (OOS nuevo)','2026-10-22','2026-10-23')
        U,r=full(ALT,'ALTS 05-23','2026-10-05','2026-10-23')
        U,r=full(BTC,'BTC 05-21 (P-REAL)','2026-10-05','2026-10-21')
        U,r=full(BTC,'BTC 22-23 Oct (OOS nuevo)','2026-10-22','2026-10-23')
        U,r=full(BTC,'BTC 05-23','2026-10-05','2026-10-23')
    open(f'out_{which}.txt','w').write('\n'.join(OUT))
