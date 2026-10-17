exec(open("common.py").read())
print("filas",len(P),"mercados",P.mkt.nunique())
print("dias:",P.groupby("dia",observed=True).agg(n=("acc","size"),mk=("mkt","nunique"),acc=("acc","sum"),coste=("coste","sum")).round(0).to_string())
print("\nEV ponderado por EUR (Sum pnl/Sum coste)  total / temprano(<500) / tardio(>=500)  por dia")
rows=[]
for d,x in P.groupby("dia",observed=True):
    rows.append((d,len(x),ev(x.pnl,x.coste),ev(x.pnl_e,x.c_e),ev(x.pnl_l,x.c_l),x.acc_l.sum()/x.acc.sum(),x.c_l.sum()/x.acc_l.sum()))
print(pd.DataFrame(rows,columns=["dia","n","ev_tot","ev_temp","ev_tard","frac_vol_tard","px_tard"]).round(4).to_string())
for per,x in P.groupby("per"):
    print(per,"ev_tot %.4f ev_temp %.4f ev_tard %.4f frac_tard %.3f px_tard %.3f  coste_tard %.0f"%(ev(x.pnl,x.coste),ev(x.pnl_e,x.c_e),ev(x.pnl_l,x.c_l),x.acc_l.sum()/x.acc.sum(),x.c_l.sum()/x.acc_l.sum(),x.c_l.sum()))
# unidades
U=P.groupby(["dia","mkt","lado"],observed=True).agg(acc=("acc","sum"),pnl=("pnl","sum"),c=("coste","sum"),pnl_l=("pnl_l","sum"),c_l=("c_l","sum"),act=("act","first")).reset_index()
print("unidades",len(U),"con tardio",(U.c_l>0).sum())
print("por moneda tardio:")
for a,x in P.groupby("act",observed=True): print(a,len(x),"ev_tard %.4f"%ev(x.pnl_l,x.c_l),"ev_temp %.4f"%ev(x.pnl_e,x.c_e), "cost_l %.0f"%x.c_l.sum())
print("por cl (clase de tomador) tardio:")
for a,x in P.groupby("cl",observed=True): print(a,len(x),"share_acc_l %.3f"%(x.acc_l.sum()/P.acc_l.sum()),"ev_tard %.4f"%ev(x.pnl_l,x.c_l))
