"""Ledger 5m de flippingsharks (0xc387c2a4...) desde fills_D.parquet (m5_onchain, 6 monedas, 09-18 Oct). Solo lectura."""
import sys, pandas as pd, numpy as np, warnings; warnings.filterwarnings("ignore")
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/wallets_18oct')
from lib import CACHE, DES
W="0xc387c2a40d389f17b723b6bba9b18b7dbd2de4f4"
SP='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/'
L=[]; Q=[]
for i in range(9,19):
    d='2026-10-%02d'%i
    F=pd.read_parquet(CACHE+f'fills_{d}.parquet',columns=['tx','li','is_tk','maker','taker','side','tok','act','mkt','lado','fin','ts','maker_amt','taker_amt','fee'])
    txw=set(F.tx[(F.maker==W)|(F.taker==W)].values)
    F=F[F.tx.isin(txw)]
    # cola: en cada (tx, tok, precio) de rellenos MAKER, rango de W entre los makers por log_index
    Mk=F[F.is_tk==0].copy()
    venta=Mk.side.values==1
    Mk['sh']=np.where(venta,Mk.maker_amt,Mk.taker_amt); Mk['usd']=np.where(venta,Mk.taker_amt,Mk.maker_amt); Mk['p3']=(Mk.usd/Mk.sh*1000).round()
    lv=Mk.groupby(['tx','tok','p3'])
    Mk['rk']=lv.li.rank(method='first'); Mk['nlv']=lv.li.transform('size')
    q=Mk[(Mk.maker==W)&(Mk.nlv>=2)]
    Q.append(pd.DataFrame({'dia':d,'rk':q.rk.values,'nlv':q.nlv.values,'act':q.act.values}))
    X=F[F.maker==W].copy()
    if not len(X): continue
    buy=X.side.values==0
    X['sh']=np.where(buy,X.taker_amt,X.maker_amt); X['usd']=np.where(buy,X.maker_amt,X.taker_amt); X['p']=X.usd/X.sh
    X['rol']=np.where(X.is_tk==1,'TOMADOR','MAKER'); X['buy']=buy; X['dia']=d
    X['des']=X.mkt.astype(str).map(DES)
    L.append(X[['dia','rol','act','mkt','fin','ts','tx','li','lado','buy','sh','usd','p','fee','des','taker']])
L=pd.concat(L,ignore_index=True); Q=pd.concat(Q,ignore_index=True)
L.to_csv(SP+'fs_ledger5m.csv.gz',index=False)
print('filas',len(L),'cobertura desenlace',round(L.des.notna().mean(),4),'dias',L.dia.nunique())
L=L[L.des.notna()]
L['v']=(L.lado==L.des).astype(float)
L['T']=L.fin-L.ts
L['pnl']=np.where(L.buy,L.sh*(L.v-L.p),L.sh*(L.p-L.v))-np.where(L.rol=='TOMADOR',L.fee,0)
L['reb_est']=np.where(L.rol=='MAKER',0.2*0.07*L.sh*L.p*(1-L.p),0)
print('\n== por rol (todas monedas, 5m)'); g=L.groupby('rol').agg(n=('sh','size'),acc=('sh','sum'),vol=('usd','sum'),pnl=('pnl','sum'),fee=('fee','sum'),reb_est=('reb_est','sum'),mkts=('mkt','nunique'))
g['vol_%']=g.vol/g.vol.sum(); print(g.round(2).to_string())
print('\n   compras vs ventas por rol:'); print(L.groupby(['rol','buy']).agg(n=('sh','size'),vol=('usd','sum')).round(0).to_string())
print('\n== por dia'); print(L.groupby(['dia','rol']).agg(vol=('usd','sum'),pnl=('pnl','sum')).unstack().round(0).to_string())
print('\n== por moneda'); print(L.groupby(['act','rol']).agg(vol=('usd','sum'),pnl=('pnl','sum')).unstack().round(0).to_string())
# posicion por mercado: acciones netas por lado y coste neto
L['dsh']=np.where(L.buy,L.sh,-L.sh); L['dc']=np.where(L.buy,L.usd,-L.usd)+np.where(L.rol=='TOMADOR',L.fee,0)
P=L.groupby(['dia','act','mkt','lado']).agg(q=('dsh','sum'),c=('dc','sum'),v=('v','first')).reset_index()
P=P.pivot_table(index=['dia','act','mkt'],columns='lado',values=['q','c','v'],fill_value=0)
P.columns=[a+'_'+b for a,b in P.columns]; P=P.reset_index()
for k in ('q_YES','q_NO','c_YES','c_NO','v_YES','v_NO'):
    if k not in P: P[k]=0.0
P['vY']=(P.mkt.astype(str).map(DES)=='YES').astype(float)  # YES gana? (desenlace oficial)
P['pnl']=P.q_YES*P.vY+P.q_NO*(1-P.vY)-P.c_YES-P.c_NO
P['par']=np.minimum(P.q_YES.clip(lower=0),P.q_NO.clip(lower=0))
cY=np.where(P.q_YES>0,P.c_YES/P.q_YES.replace(0,np.nan),np.nan); cN=np.where(P.q_NO>0,P.c_NO/P.q_NO.replace(0,np.nan),np.nan)
P['coste_par_medio']=cY+cN
P['pnl_pares']=np.where(P.par>0,P.par*(1-np.nan_to_num(cY)-np.nan_to_num(cN)),0)
P['pnl_resid']=P.pnl-P.pnl_pares
P['resid_acc']=(P.q_YES-P.q_NO).abs()
P['bruto']=P[['c_YES','c_NO']].clip(lower=0).sum(1)
print('\n== Descomposicion pares vs residuo (posicion NETA por mercado a resolucion; incluye ventas y fees)')
print('mercados',len(P),'| pnl total',round(P.pnl.sum(),1),'| pnl pares',round(P.pnl_pares.sum(),1),'| pnl residuo (direccion)',round(P.pnl_resid.sum(),1))
print('acciones de par',round(P.par.sum(),0),'| acciones residuales',round(P.resid_acc.sum(),0),'| ratio resid/par',round(P.resid_acc.sum()/P.par.sum(),3))
print('coste medio del par (ponderado por acciones de par)',round(np.nansum(P.coste_par_medio*P.par)/P.par[P.coste_par_medio.notna()].sum(),4))
d=P.groupby('dia').agg(m=('pnl','size'),pnl=('pnl','sum'),pares=('pnl_pares','sum'),resid=('pnl_resid','sum'),par_acc=('par','sum'),resid_acc=('resid_acc','sum'),bruto=('bruto','sum'))
print(d.round(1).to_string())
print('por moneda'); print(P.groupby('act').agg(m=('pnl','size'),pnl=('pnl','sum'),pares=('pnl_pares','sum'),resid=('pnl_resid','sum')).round(1).to_string())
# residuo: ¿la pata grande es la ganadora? (direccional informado vs pata suelta perdedora)
R=P[P.resid_acc>1].copy(); R['grande']=np.where(R.q_YES>R.q_NO,'YES','NO'); R['gana_grande']=np.where(R.grande=='YES',R.vY,1-R.vY)
print('\n   mercados con residuo>1 acc:',len(R),'| la pata grande gana en',round((R.gana_grande*R.resid_acc).sum()/R.resid_acc.sum(),3),'(ponderado por acc residuales); por mercado',round(R.gana_grande.mean(),3))
# precio medio de la pata residual
R['p_res']=np.where(R.grande=='YES',R.c_YES/R.q_YES.replace(0,np.nan),R.c_NO/R.q_NO.replace(0,np.nan))
print('   precio medio pagado de la pata grande (ponderado acc resid):',round(np.nansum(R.p_res*R.resid_acc)/R.resid_acc[R.p_res.notna()].sum(),4))
for lo,hi in [(0,.3),(.3,.5),(.5,.7),(.7,1.01)]:
    s=R[(R.p_res>=lo)&(R.p_res<hi)]
    if len(s): print(f'     p_res [{lo},{hi}): mercados {len(s)}, gana grande {s.gana_grande.mean():.3f}, p medio {np.average(s.p_res,weights=s.resid_acc):.3f}, pnl_resid {s.pnl_resid.sum():+.0f}')
print('\n== MAKER: bandas de precio y T de sus rellenos maker (compras de token)')
M=L[L.rol=='MAKER']
M['banda']=pd.cut(M.p,[0,.1,.3,.5,.7,.9,.97,1]); M['tb']=pd.cut(M['T'],[-1e9,0,20,60,120,180,240,300,1e9])
print(M.groupby('banda',observed=True).agg(n=('sh','size'),vol=('usd','sum'),pnl=('pnl','sum')).round(0).to_string())
print(M.groupby('tb',observed=True).agg(n=('sh','size'),vol=('usd','sum'),pnl=('pnl','sum')).round(0).to_string())
print('   tamaño de relleno maker: mediana acc',M.sh.median(),' p90',M.sh.quantile(.9))
print('\n== TOMADOR: bandas y T'); Tk=L[L.rol=='TOMADOR']; Tk['banda']=pd.cut(Tk.p,[0,.1,.3,.5,.7,.9,.97,1]); Tk['tb']=pd.cut(Tk['T'],[-1e9,0,20,60,120,300,1e9])
print(Tk.groupby(['banda'],observed=True).agg(n=('sh','size'),vol=('usd','sum'),pnl=('pnl','sum'),fee=('fee','sum')).round(0).to_string())
print(Tk.groupby(['tb'],observed=True).agg(n=('sh','size'),vol=('usd','sum'),pnl=('pnl','sum')).round(0).to_string())
print('\n== COLA: rango de W entre makers rellenados en el mismo nivel (tx,token,precio) con >=2 makers; azar => rango relativo medio 0,5')
Q['rel']=(Q.rk-1)/(Q.nlv-1)
print('niveles',len(Q),'rango relativo medio',round(Q.rel.mean(),3),'| primero',round((Q.rk==1).mean(),3),'vs azar',round((1/Q.nlv).mean(),3),'| ultimo',round((Q.rk==Q.nlv).mean(),3))
print(Q.groupby('dia').rel.mean().round(3).to_dict())
P.to_csv(SP+'fs_mercados5m.csv.gz',index=False)
