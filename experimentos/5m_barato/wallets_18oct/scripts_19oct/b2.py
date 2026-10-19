import pandas as pd, numpy as np, warnings; warnings.filterwarnings("ignore")
C='/mnt/HC_Volume_106538179/datalogs_analisis_caches/wallets_18oct/'
D=['2026-10-%02d'%i for i in range(14,19)]
R=pd.concat([pd.read_parquet(C+f'reloj_{d}.parquet').assign(dia=d) for d in D])
print("cobertura emparejada por dia y EV de los emparejados vs total (sesgo de seleccion del emparejado)")
for d,g in R.groupby('dia'): print(d, len(g), 'EV_m emparejados', round(g.pnl_m.sum()/g.coste_m.sum(),4), 'BTC share', round((g.act=='BTC').mean(),3))
cols=['rex_-30','rex_-10','rex_-5','rex_-2','rex_-1','rex_-0.5','rex_-0.1','rex_+0.1','rex_+0.5','rex_+1','rex_+2','rex_+5','rex_+10','rex_+30']
for co in ['BTC','ALT']:
    g0=R[R.act=='BTC'] if co=='BTC' else R[R.act!='BTC']
    print(f"\n== {co}: retorno Binance (bps, + = a favor del TOMADOR) por lag relativo al casado (hora exchange), ponderado por acciones; pre: de t+L a t, post: de t a t+L")
    t=g0.groupby('dia').apply(lambda g: pd.Series({c:np.average(g[c].fillna(0),weights=g.sh) for c in cols}))
    print(t.round(2).to_string())
    # fraccion de fills con move pre >=1bp a favor del tomador en 2 s previos
    print("  frac rex_-2 >= +1bp (Binance ya movio a favor del tomador en 2 s previos):", g0.groupby('dia').apply(lambda g: np.average(g['rex_-2']>=1,weights=g.sh)).round(3).to_dict())
    print("  frac rex_-2 >= +1bp, EV maker en esos:", g0.groupby('dia').apply(lambda g: g[g['rex_-2']>=1].pnl_m.sum()/g[g['rex_-2']>=1].coste_m.sum()).round(3).to_dict())
    print("  resto (rex_-2 < 1bp), EV maker:", g0.groupby('dia').apply(lambda g: g[g['rex_-2']<1].pnl_m.sum()/g[g['rex_-2']<1].coste_m.sum()).round(3).to_dict())
# volatilidad realizada y reversiones BTC a nivel mercado (de estado: todos los fills)
E=pd.concat([pd.read_parquet(C+f'estado_{d}.parquet') for d in ['2026-10-%02d'%i for i in range(14,19)]])
U=E.groupby(['dia','act','mkt','lado_c']).agg(c=('coste_m','sum'),p=('pnl_m','sum'),sh=('sh','sum'),win=('pnl_m',lambda s:(s>0).any())).reset_index()
print("\n== unidades mercado-lado (cheap side comprado por makers) BTC: n, % que gana, EV pond")
b=U[U.act=='BTC'].groupby('dia').agg(n=('c','size'),gana=('win','mean'),c=('c','sum'),p=('p','sum')); b['EV']=b.p/b.c; print(b.round(3).to_string())
M=E[E.act=='BTC'].groupby(['dia','mkt']).agg(lados=('lado_c','nunique')).reset_index()
print("  mercados BTC con ambos lados baratos en algun momento (giro):", M.groupby('dia').lados.apply(lambda s:(s==2).mean()).round(3).to_dict(), "mercados:", M.groupby('dia').size().to_dict())
