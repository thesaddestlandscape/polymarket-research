import json, glob, pandas as pd, numpy as np, warnings; warnings.filterwarnings("ignore")
SP='/tmp/claude-0/-root-polymarket-research/cbc315b0-0ee3-4fbb-b193-997ca0900993/scratchpad/act/'
out=[]
for f in sorted(glob.glob(SP+'act_*.json')):
    d=f[-15:-5]; A=pd.DataFrame(json.load(open(f)))
    A['mt']=A.slug.str.extract(r'^[a-z]+-updown-(\w+?)-')[0]
    T=A[(A.type=='TRADE')&(A.side=='BUY')]
    g=T.groupby(['conditionId','outcomeIndex']).agg(q=('size','sum'),c=('usdcSize','sum')).unstack(fill_value=0)
    g.columns=[f'{a}{b}' for a,b in g.columns]
    for k in ['q0','q1','c0','c1']:
        if k not in g: g[k]=0.0
    RES=json.load(open(SP+'../act/resol.json')) if False else json.load(open(SP+'resol.json'))
    slug=A.drop_duplicates('conditionId').set_index('conditionId').slug
    g['w']=slug.reindex(g.index).map(lambda s: 0 if RES.get(s)==['1','0'] else (1 if RES.get(s)==['0','1'] else None)).astype(float)
    print(d,'cobertura desenlace oficial',round(g.w.notna().mean(),4)); g=g[g.w.notna()]
    g['mt']=A.drop_duplicates('conditionId').set_index('conditionId').mt.reindex(g.index)
    g['pnl']=np.where(g.w==0,g.q0,g.q1)-g.c0-g.c1
    g['par']=np.minimum(g.q0,g.q1)
    a0=g.c0/g.q0.replace(0,np.nan); a1=g.c1/g.q1.replace(0,np.nan)
    g['pnl_par']=np.where(g.par>0,g.par*(1-a0.fillna(0)-a1.fillna(0)),0); g['pnl_res']=g.pnl-g.pnl_par
    g['big']=np.where(g.q0>g.q1,0,1); g['pbig']=np.where(g.big==0,a0,a1); g['res']=(g.q0-g.q1).abs(); g['gana_big']=(g.big==g.w).astype(float)
    g['dia']=d; out.append(g)
G=pd.concat(out)
pd.set_option('display.width',250)
print('mercados con desenlace OFICIAL (gamma closed=true):'); print(G.groupby('dia').size().to_dict())
t=G.groupby(['dia','mt']).agg(m=('pnl','size'),coste=('c0','sum'),pnl=('pnl','sum'),pnl_pares=('pnl_par','sum'),pnl_resid=('pnl_res','sum'),acc_par=('par','sum'),acc_res=('res','sum'))
t['coste']=G.groupby(['dia','mt']).apply(lambda x:(x.c0+x.c1).sum()); t['EV']=t.pnl/t.coste
print(t.round(3).to_string())
G['pb']=pd.cut(G.pbig,[0,.3,.5,.7,.9,1.01])
G['per']=np.where(G.dia<'2026-10','SEP','OCT')
r=G[G.res>1].groupby(['per','pb'],observed=True).apply(lambda x:pd.Series({'m':len(x),'acc_res':x.res.sum(),'gana_pata_grande':np.average(x.gana_big,weights=x.res),'p_medio':np.average(x.pbig,weights=x.res),'pnl_resid':x.pnl_res.sum()}))
print('\n residuo (pata grande) por precio medio pagado, SEP (14,21,27*) vs OCT (15,17,18):'); print(r.round(3).to_string())
