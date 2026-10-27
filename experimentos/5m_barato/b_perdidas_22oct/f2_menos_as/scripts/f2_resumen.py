# f2_resumen.py: tablas derivadas de celdas.csv + unidades (por moneda x banda gruesa, grupos post-hoc, capacidad/€ anual, diario de finalistas). Solo lectura.
import pandas as pd, numpy as np, glob, json
exec(open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/f2_menos_as/scripts/f2_analisis.py').read().split("rows=[]")[0].replace("print(cob); cob.to_csv(OUT+'cobertura.csv')",""))
pd.set_option('display.width',250); pd.set_option('display.max_columns',50)
def pool(df,label):
    if len(df)==0: return None
    D=df.groupby('dia').agg(coste=('coste','sum'),pnl=('pnl','sum'),reb=('reb','sum')); lo,hi,p=boot_days(D)
    dd=df[df.desc]; hh=df[~df.desc]
    f=lambda s: s.pnl.sum()/s.coste.sum() if len(s) and s.coste.sum()>0 else np.nan
    d2=D.sort_values('pnl',ascending=False).iloc[2:]
    return dict(grupo=label,ev=D.pnl.sum()/D.coste.sum(),ic_lo=lo,ic_hi=hi,p=p,sin2d=d2.pnl.sum()/d2.coste.sum(),desc=f(dd),hold=f(hh),dias_pos=int((D.pnl>0).sum()),dias=len(D),cierres=df.fin.nunique(),flujo_dia=D.coste.mean(),ev_reb=D.pnl.sum()/D.coste.sum()+D.reb.sum()/D.coste.sum())
out=[]
bands=[(0.0,0.10),(0.10,0.30),(0.30,0.50),(0.50,0.70),(0.70,0.90),(0.90,1.0)]
for marco in ['5min','15min']:
    for coin in ['BTC','ETH','SOL','XRP','DOGE','BNB']:
        for lo_,hi_ in bands:
            g=U[(U.marco==marco)&(U.coin==coin)&(U.pc>=lo_)&(U.pc<hi_)]
            r=pool(g,f'{marco} {coin} [{lo_:.2f},{hi_:.2f})')
            if r: out.append(r)
T=pd.DataFrame(out); T.round(3).to_csv(OUT+'coin_banda.csv',index=False)
print(T[['grupo','ev','ic_lo','ic_hi','sin2d','desc','hold','dias_pos','cierres','flujo_dia','ev_reb']].round(3).to_string())
# post-hoc: alts finas
ph=[]
for lab,coins,marcos,(a,b) in [('PH1 BNB+DOGE 5m+15m [0.10,0.40)',['BNB','DOGE'],['5min','15min'],(0.10,0.40)),('PH2 BNB 5m [0.20,0.40)',['BNB'],['5min'],(0.20,0.40)),('PH3 BNB+DOGE 5m+15m [0.10,0.50)',['BNB','DOGE'],['5min','15min'],(0.10,0.50)),
   ('PH4 ETH 15m [0.80,0.99)',['ETH'],['15min'],(0.80,0.99)),('PH5 ETH 15m [0.70,0.99)',['ETH'],['15min'],(0.70,0.99)),('PH6 BTC 5m [0.05,0.30)',['BTC'],['5min'],(0.05,0.30)),('PH7 BTC 5m [0.95,0.99)',['BTC'],['5min'],(0.95,0.99)),
   ('PH8 60m ALL [0.70,0.90)',['BTC','ETH','SOL'],['60min'],(0.70,0.90)),('PH9 4h ALL [0.65,0.99)',['BTC','ETH','SOL','XRP','DOGE','BNB'],['240min'],(0.65,0.99)),('PH10 ALT3 5m [0.10,0.30)',['ETH','SOL','XRP'],['5min'],(0.10,0.30)),('PH11 XRP 5m [0.10,0.30)',['XRP'],['5min'],(0.10,0.30)),('PH12 DOGE 5m [0.10,0.30)',['DOGE'],['5min'],(0.10,0.30))]:
    g=U[U.marco.isin(marcos)&U.coin.isin(coins)&(U.pc>=a)&(U.pc<b)]; r=pool(g,lab)
    if r: ph.append(r)
P=pd.DataFrame(ph); P.round(3).to_csv(OUT+'posthoc.csv',index=False); print(P[['grupo','ev','ic_lo','ic_hi','p','sin2d','desc','hold','dias_pos','dias','cierres','flujo_dia','ev_reb']].round(3).to_string())
