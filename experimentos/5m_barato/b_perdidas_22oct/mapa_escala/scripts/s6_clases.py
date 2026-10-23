# s6: clases, escenarios anuales y ranking (PREREG_MAPA). Salida datos/niches.csv + datos/s6_resumen.txt
import pandas as pd, numpy as np
D='/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/mapa_escala/datos'
N=pd.read_csv(D+'/niches_raw.csv'); S=pd.read_csv(D+'/maker_sel.csv')
N['tipo']=np.where(N.coin.isin(['ALL','ALT3']),'agregado','moneda')
mid=N.banda.map(lambda b:(float(b.split('-')[0])+float(b.split('-')[1]))/2); N['pc_mid']=mid
N['reb_pc']=0.014*(1-mid)
cnd=(N.ev>0)&(N.ev_desc>0)&(N.ev_oos>0)&(N.ic_lo_dias>0)&(N.ev_sin2dias>0)&(N.top1<=0.30)&(N.dias20>=10)
frag=(N.ev>0)&(N.ev_oos>0)&~cnd
N['clase']=np.where(cnd,'PERSISTENTE',np.where(frag,'FRAGIL','NEGATIVO/CERO')); N.loc[N.ndias<10,'clase']='SOLO_DESCRIPTIVO(<10d)'
# BH sobre moneda 5m/15m
def bh(p):
    p=np.asarray(p); o=np.argsort(p); n=len(p); q=np.empty(n); r=p[o]*n/(np.arange(n)+1); r=np.minimum.accumulate(r[::-1])[::-1]; q[o]=np.minimum(r,1); return q
m=(N.tipo=='moneda')&N.marco.isin(['5min','15min']); N.loc[m,'q_bh']=bh(N.loc[m,'p_dias'].values)
conserv=np.maximum(0,np.minimum(N.ic_lo_dias,N.ev_sin2dias))
cap=N.cap_oos.fillna(N.vol_dia)
N['cons']=np.where(N.clase=='PERSISTENTE',0.01*cap*conserv*365,0.0)
evo=N.ev_oos.fillna(N.ev)
N['base']=np.where(N.clase.isin(['PERSISTENTE','FRAGIL']),0.03*cap*np.maximum(0,evo)*0.28*365,0.0)
N['opt']=np.where(N.clase.isin(['PERSISTENTE','FRAGIL']),0.05*cap*np.maximum(0,evo)*365,0.0)
N['opt_reb']=np.where(N.clase.isin(['PERSISTENTE','FRAGIL']),0.05*cap*np.maximum(0,evo+N.reb_pc)*365,0.0)
N['cap_1pct_capital']=0.01*N.expo_p95; N['cap_5pct_capital']=0.05*N.expo_p95
N['score']=cap*np.maximum(0,np.where(N.ev_oos.notna(),np.minimum(N.ev_oos_lo,N.ic_lo_dias).clip(lower=0),0))
N['facil']=np.select([(N.marco=='5min')&N.banda.isin(['0.05-0.10','0.10-0.20','0.20-0.30']),(N.marco=='5min'),(N.marco=='15min')],[3,2,2],1)
N.to_csv(D+'/niches.csv',index=False)
pd.set_option('display.width',250); pd.set_option('display.max_columns',40)
print('CLASES (moneda 5m/15m):'); print(N[m].clase.value_counts().to_string())
print('BH q<0.10 entre 96 moneda 5m/15m:',int((N.loc[m,'q_bh']<0.10).sum()),' esperados ~',round(96*0.05*0.25,1),'(5% x P(DESC y OOS>0)~25%)')
print('\nPERSISTENTE/FRAGIL (todas):')
c=['marco','coin','banda','tipo','clase','vol_dia','ev','ev_reb','ic_lo_dias','ic_hi_dias','ic_lo_cierre','ev_sin2dias','ev_desc','ev_oos','top1','makers','expo_p95','cons','base','opt','facil']
print(N[N.clase.isin(['PERSISTENTE','FRAGIL'])].sort_values('opt',ascending=False)[c].round(4).to_string())
print('\nSUMAS (moneda, sin solapar):'); 
for k in ['cons','base','opt','opt_reb']: print(k, 'moneda:',round(N[N.tipo=="moneda"][k].sum()), ' agregado ALL (marco x banda):',round(N[N.coin=="ALL"][k].sum()))
print('\nMAKERS seleccionados DESC->OOS (moneda/ALL):'); print(S.round(4).to_string())
