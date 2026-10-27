import pandas as pd, numpy as np
T=pd.read_pickle('/mnt/HC_Volume_106538179/agentes_datos/q_techo/tab.pkl')
print(T.dia.value_counts().sort_index().to_string())
print(T.lado_c.value_counts().to_string(), T.act.value_counts().to_string())
print('tk_score cov', np.isfinite(T.tk_score).mean(), 'inf120 cov', np.isfinite(T.inf120).mean())
print(T[['pc','c','pnl','gana_f','T','tk_score','inf120','b10','nf']].describe().T.to_string())
print('EV/€ por dia'); g=T.groupby('dia'); print((g.pnl.sum()/g.c.sum()).round(4).to_string())
print('hit-pc', (T.gana_f-T.pc).mean())
print('NaN frac', T.isna().mean().round(3)[T.isna().mean()>0].to_string())
