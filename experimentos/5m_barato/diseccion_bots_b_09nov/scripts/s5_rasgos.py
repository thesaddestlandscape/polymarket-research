#!/usr/bin/env python3
"""s5: banco de rasgos por ORDEN TOMADORA que rellena bids en la banda de B (makers compran L a pc 0,05-0,35), 5m ETH/SOL/XRP.
Reloj: tau = hora EXCHANGE del print WS emparejado (token del tomador, precio +-0,006, tamano +-2 %, ventana [bloque-15 s, bloque+1 s]).
Corte de informacion c = tau - 100 ms por hora de RECEPCION (lo visible con margen para cancelar ~61 ms). On-chain previo: bloque <= tau-3 s.
Rasgos NaN si no hay dato <= c (se audita aparte que NaN no prediga). Muestra: hasta 25.000 ordenes/dia (semilla = fecha) + todas las de B.
Uso: s5_rasgos.py D [D...] -> datos/feat_D.parquet"""
import sys, json, numpy as np, pandas as pd
pd.set_option('future.infer_string', False)
DD='/root/polymarket-research/experimentos/5m_barato/diseccion_bots_b_09nov/datos/'
W='0x659a40ff9920febc5a66836213040924343d297f'
DES=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
SYM={'BTC':0,'ETH':1,'SOL':2,'XRP':3}
def pq(st, tt, qs, qt):
    """ultimo indice con serie==qs y t<=qt; series ordenadas por (s,t); -1 si no hay. Tiempos relativos (<1e9)."""
    key=st.astype(np.float64)*1e10+tt; qk=qs.astype(np.float64)*1e10+qt
    i=np.searchsorted(key,qk,'right')-1; ok=(i>=0)&(qs>=0); ok[ok]=st[i[ok]]==qs[ok]; i[~ok]=-1; return i
def take(a,i): out=np.full(len(i),np.nan); m=i>=0; out[m]=a[i[m]]; return out
opp=lambda s: np.where(s=='YES','NO','YES')
for D in sys.argv[1:]:
    tok=json.load(open(DD+f'tok_{D}.json')); R=np.load(DD+f'reg_{D}_tx.npz'); BASE=float(R['BASE'][0])
    tl=list(R['tok']); ti={k:i for i,k in enumerate(tl)}
    by=pd.DataFrame([(k,)+tuple(v) for k,v in tok.items()],columns=['tid','coin','marco','mkt','cierre','out'])
    m5=by[by.marco=='5min'].set_index(['mkt','out']).tid.to_dict()
    m15=by[by.marco=='15min'].set_index(['coin','cierre','out']).tid.to_dict()
    MK=pd.read_parquet(DD+f'mk_{D}.parquet'); TK=pd.read_parquet(DD+f'tk_{D}.parquet')
    for X_ in (MK,TK):
        for c_ in ('coin','L','mkt'): X_[c_]=X_[c_].astype(str)
    MK=MK[(MK.pc>=0.05)&(MK.pc<=0.35)&MK.coin.isin(['ETH','SOL','XRP'])].copy(); MK['c']=MK.acc*MK.pc; MK['esB']=MK.maker==W
    g=MK.groupby('tx',sort=False).agg(taker=('taker','first'),coin=('coin','first'),mkt=('mkt','first'),cierre=('cierre','first'),L=('L','first'),
        acc=('acc','sum'),c=('c','sum'),nmk=('maker','nunique'),ts=('ts_est','first'),bloque=('bloque','first'),esB=('esB','max')).reset_index()
    g['pc']=g.c/g.acc
    rng=np.random.default_rng(int(D.replace('-','')))
    U=g[g.esB.values | (rng.random(len(g))<min(1.0,25000/len(g)))].copy()
    tk=TK.drop_duplicates('tx').set_index('tx')[['wallet','L','pc','acc','venta','fee']].rename(columns={'wallet':'tw','L':'tL','pc':'tpc','acc':'tacc','venta':'tventa','fee':'tfee'})
    U=U.join(tk,on='tx'); U=U[U.tw.notna()].reset_index(drop=True)
    U['res']=U.mkt.map(DES); U['y_loss']=np.where(U.res.isna(),np.nan,(U.L!=U.res).astype(float))
    U['pnl_mk']=np.where(U.res.isna(),np.nan,np.where(U.L==U.res,U.acc,0)-U.c)
    # ---- emparejar el print WS de la orden tomadora
    Tt=R['t_tok'].astype(np.int32); Tex=R['t_ex'].astype(np.float64); Tr=R['t_rx'].astype(np.float64); Tp=R['t_p']; Tb=R['t_buy']; Tsz=R['t_sz']
    tout=np.where(U.tventa.values.astype(bool),opp(U.tL.values),U.tL.values); tp=np.where(U.tventa.values.astype(bool),1-U.tpc.values,U.tpc.values)
    tix=np.array([ti.get(m5.get((mk,o)),-1) for mk,o in zip(U.mkt,tout)],dtype=np.int32)
    tsr=U.ts.values*1000-BASE
    # T esta ordenado por (tok, rx): buscar por rx en ventana amplia y filtrar por ex
    a=np.searchsorted(Tt.astype(np.float64)*1e10+Tr,tix*1e10+tsr-17000); b=np.searchsorted(Tt.astype(np.float64)*1e10+Tr,tix*1e10+tsr+3000)
    tau=np.full(len(U),np.nan); tacc=U.tacc.values
    for j in range(len(U)):
        if tix[j]<0 or b[j]<=a[j]: continue
        ex=Tex[a[j]:b[j]]; okw=(ex>=tsr[j]-15000)&(ex<=tsr[j]+1000)&(np.abs(Tp[a[j]:b[j]]-tp[j])<0.006)
        if not okw.any(): continue
        oks=okw&(np.abs(Tsz[a[j]:b[j]]-tacc[j])<=0.02*tacc[j]+0.01)
        cand=np.where(oks if oks.any() else okw)[0]; k=cand[np.argmin(np.abs(ex[cand]-(tsr[j]-2400)))]; tau[j]=ex[k]
    U['tau_rel']=tau; nall=len(U); U=U[~np.isnan(tau)].reset_index(drop=True); n=len(U)
    c=U.tau_rel.values-100.0; sgn=np.where(U.L.values=='YES',1.0,-1.0)
    F={k:np.full(n,np.nan) for k in []}; FL=[]
    tidL=np.array([ti.get(m5.get((mk,l)),-1) for mk,l in zip(U.mkt,U.L)],dtype=np.int32)
    tidC=np.array([ti.get(m5.get((mk,o)),-1) for mk,o in zip(U.mkt,opp(U.L.values))],dtype=np.int32)
    c15=((U.cierre.values+899)//900)*900
    tid15=np.array([ti.get(m15.get((co,int(ci),l)),-1) for co,ci,l in zip(U.coin,c15,U.L)],dtype=np.int32)
    # ---- libro por moneda (cada npz de moneda contiene sus tokens 5m y 15m)
    for co in ('ETH','SOL','XRP'):
        mco=U.coin.values==co
        if not mco.any(): continue
        Q=np.load(DD+f'reg_{D}_{co}.npz'); Qt=Q['q_tok'].astype(np.int32); Qr=Q['q_rx'].astype(np.float64)
        bidA=Q['q_bid']; askA=Q['q_ask']; bszA=Q['q_bsz']; aszA=Q['q_asz']
        cc=c[mco]; part={}
        for nm,tt in (('L',tidL[mco]),('C',tidC[mco]),('15',tid15[mco])):
            i0=pq(Qt,Qr,tt,cc); bid=take(bidA,i0); ask=take(askA,i0)
            part[f'{nm}_bid']=bid; part[f'{nm}_ask']=ask; part[f'{nm}_spr']=ask-bid; part[f'{nm}_edad']=(cc-take(Qr,i0))/1000
            if nm!='15':
                bs=take(bszA,i0); as_=take(aszA,i0); part[f'{nm}_bsz']=bs; part[f'{nm}_asz']=as_; part[f'{nm}_imb']=(bs-as_)/(bs+as_)
            for w in (0.5,1,2,5,10,30,60):
                iw=pq(Qt,Qr,tt,cc-w*1000)
                part[f'{nm}_dmid{w}']=(bid+ask)/2-(take(bidA,iw)+take(askA,iw))/2; part[f'{nm}_dbid{w}']=bid-take(bidA,iw); part[f'{nm}_dask{w}']=ask-take(askA,iw)
                if nm!='15': part[f'{nm}_nupd{w}']=np.where((i0>=0)&(iw>=0),(i0-iw).astype(float),np.nan)
        FL.append((np.where(mco)[0],part)); del Q,Qt,Qr,bidA,askA,bszA,aszA
    keys=sorted(set(k for _,p in FL for k in p)); F={k:np.full(n,np.nan) for k in keys}
    for idx,p in FL:
        for k,v in p.items(): F[k][idx]=v
    pc=U.pc.values
    F['bid15_menos_pc']=F['15_bid']-pc; F['bidL_menos_pc']=F['L_bid']-pc; F['askL_menos_pc']=F['L_ask']-pc
    F['suma_bids']=F['L_bid']+F['C_bid']; F['suma_asks']=F['L_ask']+F['C_ask']; F['ask15_menos_askL']=F['15_ask']-F['L_ask']
    # ---- prints WS del mercado firmados hacia L (por recepcion)
    cum=np.cumsum(Tsz*np.where(Tb==1,1.0,-1.0)); cumv=np.cumsum(Tsz.astype(np.float64))
    def cv(arr,i): o=np.zeros(len(i)); m=i>=0; o[m]=arr[i[m]]; return o
    for nm,tt,sg in (('L',tidL,1.0),('C',tidC,-1.0)):
        s0=np.searchsorted(Tt,tt,'left')-1; i0=pq(Tt,Tr,tt,c); ok=i0>=0
        for w in (1,5,30,60):
            iw=pq(Tt,Tr,tt,c-w*1000); iw=np.where(iw>=0,iw,s0)
            F[f'pr{nm}_vol{w}']=np.where(ok,cv(cumv,i0)-cv(cumv,iw),0.0); F[f'pr{nm}_sgn{w}']=np.where(ok,cv(cum,i0)-cv(cum,iw),0.0)*sg; F[f'pr{nm}_n{w}']=np.where(ok,i0-iw,0).astype(float)
    # ---- Binance aggTrade (RECEPCION c[7]) de la moneda y de BTC
    Xs=R['x_sym'].astype(np.int32); Xr=R['x_rx'].astype(np.float64); lp=np.log(R['x_p']); sv=np.cumsum(np.where(R['x_m']==0,1.0,-1.0)*R['x_qty']*R['x_p'])
    for nm,sy in (('bn',np.array([SYM[x] for x in U.coin],dtype=np.int32)),('btc',np.zeros(n,dtype=np.int32))):
        i0=pq(Xs,Xr,sy,c); p0=take(lp,i0); F[f'{nm}_edad']=(c-take(Xr,i0))/1000
        for w in (0.2,0.5,1,2,5,10,30,60,120,300):
            iw=pq(Xs,Xr,sy,c-w*1000); F[f'{nm}_r{w}']=(p0-take(lp,iw))*1e4*sgn
            if w in (1,5,30,60,300): F[f'{nm}_cvd{w}']=(take(sv,i0)-take(sv,iw))*sgn; F[f'{nm}_n{w}']=np.where((i0>=0)&(iw>=0),(i0-iw).astype(float),np.nan)
        io=pq(Xs,Xr,sy,(U.cierre.values-300)*1000.0-BASE); F[f'{nm}_r_apertura']=(p0-take(lp,io))*1e4*sgn
        for w in (60,300):
            acc=np.zeros(n)
            for k in range(10):
                acc+=np.abs(take(lp,pq(Xs,Xr,sy,c-w*100*k))-take(lp,pq(Xs,Xr,sy,c-w*100*(k+1))))
            F[f'{nm}_rv{w}']=acc*1e4
    F['bn_z_apertura']=F['bn_r_apertura']/(F['bn_rv300']+1e-6)
    # ---- tiempo y orden
    tabs=(U.tau_rel.values+BASE)/1000
    F['seg_a_cierre']=U.cierre.values-tabs; F['hora']=(tabs%86400)//3600; F['min_hora']=(tabs%3600)//60; F['ms_del_segundo']=(U.tau_rel.values+BASE)%1000
    F['dow']=pd.to_datetime(tabs,unit='s').dayofweek.values.astype(float)
    F['pc']=pc; F['acc_banda']=U.acc.values; F['nmk']=U.nmk.values.astype(float); F['tacc']=U.tacc.values; F['tventa']=U.tventa.values.astype(float)
    F['t_nocional']=U.tacc.values*U.tpc.values; F['tfee_pos']=(U.tfee.values>0).astype(float); F['es_lado_yes']=(U.L.values=='YES').astype(float)
    for co in ('ETH','SOL','XRP'): F[f'coin_{co}']=(U.coin.values==co).astype(float)
    # ---- on-chain previo (bloque <= tau-3 s)
    t3=tabs-3
    TKs=TK[['ts_est','wallet','mkt','L','acc','pc']].sort_values(['mkt','ts_est']); mk_g={k:(v.ts_est.values,v.wallet.values,v.L.values,(v.acc*v.pc).values) for k,v in TKs.groupby('mkt')}
    for w in (30,120,300):
        nn=np.zeros(n); fl=np.zeros(n); dw=np.zeros(n); own=np.zeros(n)
        for j,(mk,L,tt3,tw) in enumerate(zip(U.mkt.values,U.L.values,t3,U.tw.values)):
            G=mk_g.get(mk)
            if G is None: continue
            a_=np.searchsorted(G[0],tt3-w); b_=np.searchsorted(G[0],tt3,'right')
            if b_>a_:
                nn[j]=b_-a_; fl[j]=float((G[3][a_:b_]*np.where(G[2][a_:b_]==L,1,-1)).sum()); dw[j]=len(set(G[1][a_:b_])); own[j]=float((G[1][a_:b_]==tw).sum())
        F[f'oc_n{w}']=nn; F[f'oc_flujoL{w}']=fl; F[f'oc_wallets{w}']=dw; F[f'oc_propio{w}']=own
    TKw=TK[['ts_est','wallet']].sort_values(['wallet','ts_est']); tw_g={k:v.ts_est.values for k,v in TKw.groupby('wallet')}
    for w in (60,600,3600):
        F[f'tw_prev{w}']=np.array([float(np.searchsorted(tw_g.get(tw,np.zeros(0)),x,'right')-np.searchsorted(tw_g.get(tw,np.zeros(0)),x-w)) for tw,x in zip(U.tw.values,t3)])
    # ---- perp Binance 5 min (ultimo cerrado <= tau)
    try:
        P=pd.read_csv(f'/root/polymarket-research/data/shadow/binance_perp_cvd_oi_{D}.csv'); P['t']=pd.to_datetime(P.timestamp_utc,utc=True).astype('int64')/1e9; P=P.sort_values('t')
        pdr=np.full(n,np.nan); doi=np.full(n,np.nan)
        for co in ('ETH','SOL','XRP'):
            S=P[P.activo==co]; m=U.coin.values==co
            if not len(S) or not m.any(): continue
            i=np.searchsorted(S.t.values,tabs[m]-1,'right')-1; ok=i>=1
            v=np.full(m.sum(),np.nan); v[ok]=S.perp_delta_ratio.values[i[ok]]; pdr[m]=v*sgn[m]
            v2=np.full(m.sum(),np.nan); v2[ok]=(S.open_interest.values[i[ok]]/S.open_interest.values[i[ok]-1]-1)*1e4; doi[m]=v2
        F['perp_delta_ratio']=pdr; F['perp_doi_bps']=doi
    except FileNotFoundError: pass
    Fd=pd.DataFrame(F)
    keepc=['tx','taker','tw','coin','mkt','cierre','L','pc','acc','c','nmk','esB','y_loss','pnl_mk','tau_rel','bloque','ts','tL','tpc','tacc','tventa']
    out=pd.concat([U[keepc].rename(columns={'pc':'pc_u','acc':'acc_u','nmk':'nmk_u','tacc':'tacc_u','tventa':'tventa_u'}),Fd],axis=1); out['dia']=D; out['tau_abs']=U.tau_rel.values+BASE
    out.to_parquet(DD+f'feat_{D}.parquet')
    print(D,'unidades_banda',len(g),'muestra',nall,'emparejadas',n,'(%.3f)'%(n/max(nall,1)),'B',int(U.esB.sum()),'/',int(g.esB.sum()),'desenlace',round(float(U.res.notna().mean()),4),'rasgos',Fd.shape[1],flush=True)
