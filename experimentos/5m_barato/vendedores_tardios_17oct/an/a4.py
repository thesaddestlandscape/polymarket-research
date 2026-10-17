exec(open("common.py").read())
L=P[(P.acc_l>0)&(P.dia!="2026-10-05")&(P.dia!="2026-10-17")].copy()   # 05 parcial, 17 parcial
L["pos15"]=((L.fin%900)/300).round().astype(int)
L["hora"]=pd.to_datetime(L.fin,unit="s").dt.hour
L["hb"]=(L.hora//4)*4
L["dow"]=pd.to_datetime(L.fin,unit="s").dt.dayofweek
L["trend60"]=np.where(L.p60.notna(),L.p60-L.pc,np.nan)     # >0: el precio de s era MAYOR hace 60 s (cae)
L["trend10"]=np.where(L.p10.notna(),L.p10-L.pc,np.nan)
L["pcb"]=pd.cut(L.pc,[0.10,0.15,0.20,0.25,0.30])
L["tkacc_b"]=pd.cut(L.tk_acc,[0,10,50,200,1e9])
L["nfb"]=pd.cut(L.nf_prev,[-1,0,3,10,1e9])
L["nmkb"]=pd.cut(L.nmk,[0,1,3,6,1e9])
L["tr60b"]=pd.cut(L.trend60,[-1,-0.02,0.02,0.06,1])
L["tr10b"]=pd.cut(L.trend10,[-1,-0.02,0.02,0.06,1])
L["cum_b"]=pd.cut(L.cum0,[499,1000,2000,5000,1e9])
dias=sorted(L.dia.unique())
def tabla(col):
    rows=[]
    for k,x in L.groupby(col,observed=True):
        s=x[x.per=="SEL"]; m=x[x.per=="MEAS"]
        pd_=[ev(y.pnl_l,y.c_l) for _,y in x.groupby("dia",observed=True)]
        pos=sum(1 for v in pd_ if v>0)
        rows.append((str(k),len(x),round(x.c_l.sum()),ev(x.pnl_l,x.c_l),ev(s.pnl_l,s.c_l),ev(m.pnl_l,m.c_l),f"{pos}/{len(pd_)}"))
    print(f"-- {col}"); print(pd.DataFrame(rows,columns=["bucket","n","coste","ev_all","ev_SEL","ev_MEAS","dias+"]).round(4).to_string(index=False))
print("EV tardio total",ev(L.pnl_l,L.c_l),"n",len(L))
for c in ["pos15","hb","dow","pcb","tkacc_b","nfb","nmkb","tr60b","tr10b","cum_b","act"]: tabla(c)
