exec(open("common.py").read())
L=P[P.acc_l>0].copy()
L["inv_s"]=L.inv_s.round(2); L["inv_ns"]=L.inv_ns.round(2)
def estado(r_cl,inv_s,inv_ns):
    pass
vend=(L.cl=="VENDE_s").values; a=(L.inv_s>0.5).values; b=(L.inv_ns>0.5).values
names=["VENDE_s|dueno_s+ns(deshace par)","VENDE_s|dueno_s(liquida)","VENDE_s|solo_ns(corto s?)","VENDE_s|sin_inv(mint/ext)","COMPRA_ns|dueno_s+ns(amplia par)","COMPRA_ns|dueno_ns(refuerza fav)","COMPRA_ns|dueno_s(cubre/par)","COMPRA_ns|sin_inv(nuevo)"]
code=np.where(vend,np.where(a,np.where(b,0,1),np.where(b,2,3)),np.where(b,np.where(a,4,5),np.where(a,6,7))).astype(np.int8)
st=pd.Categorical.from_codes(code,names)
L["st"]=st
print("ESTADO del tomador antes de la tx (inventario por fills logueados), volumen tardio, EV del MAKER (=comprador de s) ponderado por EUR")
tot=L.c_l.sum()
rows=[]
for s,x in L.groupby("st"):
    r={"estado":s,"n":len(x),"mkts":x.groupby(["mkt","lado"]).ngroups,"takers":x.tk.nunique(),"share_c":x.c_l.sum()/tot,"px":x.c_l.sum()/x.acc_l.sum(),"ev_SEL":ev(x[x.per=="SEL"].pnl_l,x[x.per=="SEL"].c_l),"ev_MEAS":ev(x[x.per=="MEAS"].pnl_l,x[x.per=="MEAS"].c_l),
       "nSEL":(x.per=="SEL").sum(),"nMEAS":(x.per=="MEAS").sum()}
    rows.append(r)
print(pd.DataFrame(rows).sort_values("share_c",ascending=False).round(4).to_string())
# T distribution
print("\nT (s restantes) del volumen tardio: cuantiles ponderados por coste")
for lo,hi in [(60,90),(90,120),(120,150),(150,180),(180,210),(210,240),(240,270),(270,300)]:
    x=L[(L["T"]>lo)&(L["T"]<=hi)]
    print(lo,hi,"share_c %.3f"%(x.c_l.sum()/tot),"ev_SEL %.4f ev_MEAS %.4f"%(ev(x[x.per=='SEL'].pnl_l,x[x.per=='SEL'].c_l),ev(x[x.per=='MEAS'].pnl_l,x[x.per=='MEAS'].c_l)),"px %.3f"%(x.c_l.sum()/x.acc_l.sum()))
