"""R8 emparejado: libreria (estimador). Ver ../PREREG.md (sha256 en ../PREREG.sha256). Solo lectura."""
import json, numpy as np, pandas as pd
NC=8; NCELL=NC*2*5*7
COINS=["BTC","ETH","SOL","XRP","DOGE","BNB","HYPE","OTRA"]
def band(p): return np.clip(np.floor(p/0.05+1e-9),0,6).astype(np.int64)

class Day:
    """Universo de fills del dia ordenado por (grupo mkt-lado, ts). Todo vectorizado."""
    def __init__(s, df, pw_codes, roster_info=None):
        # df: columnas ts,cierre,mkt,lado,buy,acc,usd,fee,p,w,act,win (win NaN = missing)
        el=df.ts.values-(df.cierre.values-300)
        uni=df.buy.values&(df.p.values<=0.35)&(el>=0)&(el<300)
        s.cov_rows=uni.sum(); known=~np.isnan(df.win.values); s.known=known
        wal,uw=pd.factorize(df.w.values); mk,_=pd.factorize(df.mkt.values); s.nw=wal.max()+1; s.uw=uw
        s.wal_full=wal; s.mkt_full=mk; s.buy_full=df.buy.values
        gcode,_=pd.factorize(df.mkt.astype(str).values+"|"+df.lado.astype(str).values)
        # diagnostico de cobertura: grupos con evento bruto (ignorando win) vs sin; se rellena en cov_diag()
        s.raw=dict(uni=uni,known=known,wal=wal,g=gcode,ts=df.ts.values,cap=(df.acc.values*(1-df.p.values)))
        U=np.flatnonzero(uni&known)
        o=np.lexsort((df.ts.values[U],gcode[U])); U=U[o]
        s.U=U; g=gcode[U]; s.g=g; s.ng=gcode.max()+1
        s.ts=df.ts.values[U]; s.wal=wal[U]; s.mkt=mk[U]; s.cierre=df.cierre.values[U]; s.el=el[U]
        s.acc=df.acc.values[U]; s.p=df.p.values[U]; w=df.win.values[U]
        lado=(df.lado.values[U]=="YES").astype(np.int64)
        s.pnl=s.acc*(s.p-w); s.cap=s.acc*(1-s.p); s.reb=0.2*df.fee.values[U]
        coin=np.array([COINS.index(a) if a in COINS else NC-1 for a in df.act.values[U]],dtype=np.int64)
        s.coin=coin; s.lado=lado; s.minute=np.clip((s.el//60).astype(np.int64),0,4); s.band=band(s.p)
        s.cell=((coin*2+lado)*5+s.minute)*7+s.band; s.n=len(U)
        key=s.cell*(s.ng+1)+g; s.perm=np.argsort(key,kind="stable"); s.key_sorted=key[s.perm]
        # primer indice de cada grupo (filas ordenadas por grupo)
        s.gstart=np.r_[0,np.flatnonzero(g[1:]!=g[:-1])+1] if s.n else np.array([],dtype=np.int64)
        s.mkt_has=None
    def events(s,inS):
        """t0 por grupo (nan si sin evento) para el set de wallets inS (bool por codigo)."""
        m=inS[s.wal]; idx=np.flatnonzero(m); t0g=np.full(s.ng,np.nan)
        if len(idx):
            gg=s.g[idx]; first=idx[np.r_[True,gg[1:]!=gg[:-1]]]; t0g[s.g[first]]=s.ts[first]
        return t0g,m
    def masks(s,inS,a,b,strict=False,cap5=False):
        t0g,m=s.events(inS); t0=t0g[s.g]; has=~np.isnan(t0)
        wt=(has&~m&(s.ts>=t0+a)&(s.ts<=t0+b)).astype(float)
        if cap5:
            ca=np.cumsum(s.acc*wt); base=np.zeros(s.n)
            gs=s.gstart; 
            prev=np.r_[0.0,ca][gs]            # cumsum antes de cada grupo
            gidx=np.repeat(np.arange(len(gs)),np.diff(np.r_[gs,s.n]))
            before=ca-s.acc*wt-prev[gidx]
            wt=wt*np.clip(5-before,0,s.acc)/np.maximum(s.acc,1e-12)
        ctrl=~has&~m
        if strict:
            sm=np.zeros(s.mkt_full.max()+1,bool); sm[s.mkt_full[inS[s.wal_full]&s.buy_full]]=True; ctrl&=~sm[s.mkt]
        return wt,ctrl,has
    def inS_from(s,addrs):
        return np.asarray(pd.Index(s.uw).isin(addrs))

def cellsums(d,wt,ctrl,minctl=5,use_reb=False):
    c=d.cell; pn=d.pnl+(d.reb if use_reb else 0)
    Tp=np.bincount(c,wt*pn,NCELL); Tc=np.bincount(c,wt*d.cap,NCELL)
    Cp=np.bincount(c,ctrl*pn,NCELL); Cc=np.bincount(c,ctrl*d.cap,NCELL)
    cm=ctrl[d.perm]; ks=d.key_sorted[cm]
    nd=np.zeros(NCELL)
    if len(ks):
        new=np.r_[True,ks[1:]!=ks[:-1]]; cells=(ks[new]//(d.ng+1)); nd=np.bincount(cells,minlength=NCELL)
    elig=(nd>=minctl)&(Cc>0)
    return Tp,Tc,Cp,Cc,elig
def excess(Tp,Tc,Cp,Cc,elig):
    mu=np.where(Cc>0,Cp/np.maximum(Cc,1e-12),0.0)
    num=(Tp-Tc*mu)[elig].sum(); den=Tc[elig].sum()
    return (num/den if den>0 else np.nan), den, Tc.sum()
