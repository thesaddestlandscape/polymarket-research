import json,sys,collections,csv
import pandas as pd, numpy as np
S=sys.argv[1]; EX='0xe111180000d2663c0091e4f400237545b87b996b'
F=json.load(open(S+'/own_fills.json'))
for f in F:
    f['tk_fee_part']=(f['tk_fee'] or 0)*f['sh']/(f['tk_sh'] or f['sh'])
    f['their_gain']=-f['pnl']-f['tk_fee_part']
D=pd.DataFrame(F)
print('fills',len(D),'tomadores distintos',D.taker.nunique())
print('modo de casado: tomador compra el token CONTRARIO (mint) ',int((D.tk_tok_same==False).sum()),' / vende nuestro token',int((D.tk_tok_same==True).sum()))
D['tk_px']=D.tk_usd/D.tk_sh
print('precio que paga el tomador (lado contrario) mediana',round(D.tk_px.median(),3),'p10/p90',D.tk_px.quantile([.1,.9]).round(3).tolist(),' tamaño orden tomadora mediana acc',D.tk_sh.median(),'p90',D.tk_sh.quantile(.9))
g=D.groupby('taker').agg(n=('sh','size'),sh=('sh','sum'),nuestro_coste=('coste','sum'),nuestro_pnl=('pnl','sum'),su_gan=('their_gain','sum'),
   monedas=('coin',lambda s:','.join(sorted(set(s)))),px=('tk_px','mean'),orden_acc=('tk_sh','median'),T=('T_fill','mean'),dias=('dia',lambda s:','.join(sorted(set(s))))).sort_values('su_gan',ascending=False)
pd.set_option('display.width',250)
print(g.head(15).round(3)); print('...'); print(g.tail(5).round(3))
print('concentración: top1 su_gan',round(g.su_gan.iloc[0],2),'de total',round(g.su_gan.sum(),2),'; wallets con >=2 fills contra nosotros',int((g.n>=2).sum()),' fills que suponen',int(g[g.n>=2].n.sum()))
g.to_csv(S+'/contrapartes_rank.csv')
json.dump(list(g.index),open(S+'/cp_wallets.json','w'))
