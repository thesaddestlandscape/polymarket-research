import pandas as pd, numpy as np, warnings; warnings.filterwarnings("ignore")
C='/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
D=['2026-10-%02d'%i for i in range(14,19)]
E=pd.concat([pd.read_parquet(C+f'estado_{d}.parquet') for d in D])
E['win']=(E.pnl_m>0).astype(float)
def ev(g): return pd.Series({'coste':g.coste_m.sum(),'pnl':g.pnl_m.sum(),'EV':g.pnl_m.sum()/g.coste_m.sum(),'acierto_w':(g.win*g.sh).sum()/g.sh.sum(),'precio_w':(g.pc*g.sh).sum()/g.sh.sum(),'pfair_w':(g.p_fair*g.sh).sum()/g.sh[g.p_fair.notna()].sum() if g.p_fair.notna().any() else np.nan})
print("== por dia x moneda (EV maker ponderado)"); 
t=E.groupby(['dia','act']).apply(ev); print(t.EV.unstack().round(3).to_string()); print(t.coste.unstack().round(0).to_string())
print("\n== por dia: acierto ponderado acciones vs precio pagado vs p_fair (todas monedas)")
print(E.groupby('dia').apply(ev).round(4).to_string())
print("\n== BTC por dia")
print(E[E.act=='BTC'].groupby('dia').apply(ev).round(4).to_string())
# edge vs fair: buckets de p_fair - pc
E['gap']=E.p_fair-E.pc
E['gb']=pd.cut(E.gap,[-1,-0.15,-0.05,0,0.05,0.15,1])
print("\n== EV maker por bucket (p_fair - pc) y dia [p_fair con sigma del dia: descriptivo]")
t=E.groupby(['gb','dia'],observed=True).apply(ev); print(t.EV.unstack().round(3).to_string()); print((t.coste.unstack()/t.coste.unstack().sum()).round(3).to_string())
# z_rem buckets: estado del mercado (cuanto va por detras el lado barato)
E['zb']=pd.cut(E.z_rem,[-99,-2,-1.5,-1,-0.5,0,99])
print("\n== EV maker por z_rem (lado comprado por el maker; negativo = va por detras) y dia")
t=E.groupby(['zb','dia'],observed=True).apply(ev); print(t.EV.unstack().round(3).to_string()); print((t.coste.unstack()/t.coste.unstack().sum()).round(3).to_string())
print("\n   acierto - precio (pp) por zb x dia"); print(((t.acierto_w-t.precio_w)*100).unstack().round(2).to_string())
E['Tb']=pd.cut(E['T'],[60,120,180,240,300])
t=E.groupby(['Tb','dia'],observed=True).apply(ev); print("\n== EV por T restante"); print(t.EV.unstack().round(3).to_string())
E['pb']=pd.cut(E.pc,[0.1,0.15,0.2,0.25,0.3])
t=E.groupby(['pb','dia'],observed=True).apply(ev); print("\n== EV por precio"); print(t.EV.unstack().round(3).to_string())
E['hora']=pd.to_datetime(E.ts,unit='s').dt.hour
t=E[E.dia>='2026-10-17'].groupby(['dia','hora']).apply(ev)
print("\n== 17-18 por hora: EV y coste"); print(t[['EV','coste','pnl']].unstack(0).round(3).to_string())
