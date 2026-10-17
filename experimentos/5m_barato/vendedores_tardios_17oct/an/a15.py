exec(open("common_s.py").read())
import csv
from datetime import datetime
f2m={}
for c in csv.reader(open("../kall.csv")):
    if c[2]=="15min" and c[1]=="BTC": f2m[int(datetime.fromisoformat(c[4]).timestamp())]=int(c[3])
Q=P[(P.act=="BTC")&(P.acc_l>0)&(P.dia!="2026-10-05")&(P.dia!="2026-10-17")][["ts","tk","lado","fin","c_l","pnl_l","acc_l","dia","per","cl"]].copy()
Q["fin15"]=(np.ceil(Q.fin/900)*900).astype("int64")
Q["m15"]=Q.fin15.map(f2m)
print("fills sin mercado 15m:",Q.m15.isna().mean())
Q=Q[Q.m15.notna()].copy(); Q["m15"]=Q.m15.astype("int32"); Q["t"]=Q.ts-3.0
E15=pd.read_pickle("../E15.pkl")
E15=E15.sort_values("ts"); 
E15["cum"]=E15.groupby(["w","m15"]).dup.cumsum()
Qs=Q.sort_values("t").rename(columns={"tk":"w"})
M=pd.merge_asof(Qs,E15[["ts","w","m15","cum"]].rename(columns={"ts":"tE"}),left_on="t",right_on="tE",by=["w","m15"],direction="backward")
M["cum"]=M.cum.fillna(0.0)    # sin posicion 15m previa visible (=0 en nuestra ventana de datos; ver nota)
# direccion 5m del tomador: compra ns. ns=Up si lado s=NO(0). exposicion up = +1 si ns=Up
M["e5"]=np.where(M.lado==0,1.0,-1.0)
M["rel"]=np.where(M.cum.abs()<5,"sin_15m",np.where(np.sign(M.cum)==M.e5,"15m_alineada_con_ns","15m_opuesta_a_ns"))
print("Posicion previa del tomador en el 15m que cubre el 5m (BTC, volumen tardio, 06-16 Oct), EV del maker (=pierde el tomador) pooled")
tot=M.c_l.sum(); rows=[]
for r,x in M.groupby("rel"):
    dd=x.groupby("dia",observed=True)[["pnl_l","c_l"]].sum()
    rows.append((r,x.w.nunique(),len(x),x.c_l.sum()/tot,x.pnl_l.sum()/x.c_l.sum(),(dd.pnl_l>0).sum(),len(dd),
        x[x.per=="SEL"].pnl_l.sum()/x[x.per=="SEL"].c_l.sum(),x[x.per=="MEAS"].pnl_l.sum()/x[x.per=="MEAS"].c_l.sum()))
print(pd.DataFrame(rows,columns=["rel","wallets","fills","share_coste","EV","dias+","nd","EV_SEL","EV_MEAS"]).round(3).to_string(index=False))
# tamano de la posicion 15m
x=M[M.rel!="sin_15m"]; print("posicion 15m abs mediana %.0f p90 %.0f acc"%(x.cum.abs().median(),x.cum.abs().quantile(.9)))
