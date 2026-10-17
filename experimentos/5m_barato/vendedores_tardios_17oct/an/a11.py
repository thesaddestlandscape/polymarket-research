exec(open("common_s.py").read())
import gzip, csv, os
from datetime import datetime
P=P[(P.act=="BTC")&(P.dia!="2026-10-05")&(P.dia!="2026-10-17")&(P.acc_l>0)][["ts","lado","mkt","fin","c_l","pnl_l","acc_l","per"]].copy()
import gc; gc.collect()
# serie BTC chainlink por recepcion
ts=[];px=[]
for d in range(5,18):
    f=f"/root/polymarket-research/data/prices/chainlink_2026-10-{d:02d}.csv"
    f=f if os.path.exists(f) else f+".gz"
    op=gzip.open if f.endswith(".gz") else open
    with op(f,"rt") as fh:
        rd=csv.reader(fh); next(rd)
        for c in rd:
            if c[1]=="BTC" and c[4]=="chainlink":
                ts.append(datetime.fromisoformat(c[0]).timestamp()); px.append(float(c[2]))
ts=np.array(ts); px=np.array(px); o=np.argsort(ts); ts=ts[o]; px=px[o]
print("ticks BTC",len(ts))
def ret(t,W):   # log-ret bps entre t-W y t (ultimo tick <= cada instante)
    i1=np.searchsorted(ts,t,side="right")-1; i0=np.searchsorted(ts,t-W,side="right")-1
    ok=(i0>=0)&(i1>=0)&(ts[i1]>=t-5)&(ts[i0]>=t-W-5)
    r=np.where(ok,np.log(px[np.clip(i1,0,None)]/px[np.clip(i0,0,None)])*1e4,np.nan); return r
sign=np.where(P.lado.values==1,-1.0,1.0)    # lado YES(Up): mover contra s = caida
tdec=P.ts.values-3.0
L=P[P.acc_l>0]
for W in (10,30):
    r=ret(tdec,W)*sign; P["m"+str(W)]=r
# baseline temporal: segundos de unidades con volumen tardio
U=L.groupby(["mkt","lado"]).agg(fin=("fin","first"),lado_=("lado","first"),per=("per","first")).reset_index()
rng=np.random.default_rng(1)
rows=[]
for (fin,lado,per) in zip(U.fin.values,U.lado_.values,U.per.values):
    tt=fin-np.arange(61,300,5.0)
    rows.append(pd.DataFrame({"t":tt,"lado":lado,"per":per}))
B=pd.concat(rows,ignore_index=True)
sB=np.where(B.lado.values==1,-1.0,1.0)
for W in (10,30): B["m"+str(W)]=ret(B.t.values-0.0,W)*sB
bins=[-1e9,-5,-2,2,5,10,1e9]
for W in (10,30):
    print(f"\n=== movimiento BTC EN CONTRA de s (bps; + = favorece ns) en los {W} s previos al casado ===")
    col="m"+str(W)
    Lw=P[(P.acc_l>0)&P[col].notna()]
    Lw=Lw.assign(b=pd.cut(Lw[col],bins)); Bw=B[B[col].notna()].assign(b=lambda x: pd.cut(x[col],bins))
    tc=Lw.c_l.sum(); 
    out=[]
    for b,x in Lw.groupby("b",observed=True):
        tb=(Bw.b==b).mean()
        s=x[x.per=="SEL"]; m=x[x.per=="MEAS"]
        out.append((str(b),len(x),x.c_l.sum()/tc,tb,(x.c_l.sum()/tc)/tb,ev(x.pnl_l,x.c_l),ev(s.pnl_l,s.c_l),ev(m.pnl_l,m.c_l)))
    print(pd.DataFrame(out,columns=["bucket","n","share_vol","share_tiempo","ratio","EV","EV_SEL","EV_MEAS"]).round(3).to_string(index=False))
