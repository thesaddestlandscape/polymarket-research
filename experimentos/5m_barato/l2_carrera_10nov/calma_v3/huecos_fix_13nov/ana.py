import json,sys,os,numpy as np,pandas as pd
H='/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/huecos_fix_13nov/out/'; OLD='/root/polymarket-research/experimentos/5m_barato/l2_carrera_10nov/calma_v3/recalc_13nov/out/'
days=[f'2026-11-{d:02d}' for d in range(2,13)]; V=('G0','T1','PLA_T1'); rows=[]; allh=[]
def st(x,v):
    y=x[x['var']==v]; return len(y),y.pnl.sum(),y.cost.sum()
for d in days:
    f=H+f'hole60_dec2v3_{d}.pkl'
    if not os.path.exists(f): continue
    n=pd.read_pickle(f); o=pd.read_pickle(OLD+f'dec2v3_{d}.pkl'); M=json.load(open(H+f'meta2_{d}.json'))
    bh={h for _,h in M['bad_hours']}; n=n[n['var'].isin(V)].copy(); o=o[o['var'].isin(V)]
    n['hr']=((n.fin-300)//3600)%24; n['bad']=n.hr.isin(bh)|(((n.fin)//3600)%24).isin(bh)|n.hr.isin({(h-1)%24 for h in bh}) & False
    n['bad']=(((n.fin-300)//3600)%24).isin(bh)|((n.fin//3600)%24).isin(bh); n['d']=d; allh.append(n)
    r=dict(d=d,mk_old=o[o['var']=='G0'].k.nunique(),mk_new=n[n['var']=='G0'].k.nunique(),mk_rec=n[(n['var']=='G0')&n.bad].k.nunique())
    for v in V:
        a=st(o,v); b=st(n,v); r.update({f'{v}_old':a[1],f'{v}_new':b[1]})
    r['dT1G0_old']=r['T1_old']-r['G0_old']; r['dT1G0_new']=r['T1_new']-r['G0_new']
    rows.append(r)
R=pd.DataFrame(rows).set_index('d'); pd.set_option('display.width',250); print(R.round(1).to_string()); print(R.sum().round(1).to_dict())
def ic(x):
    x=np.asarray(x,float); m=x.mean(); se=x.std(ddof=1)/np.sqrt(len(x)); t={9:1.833,10:1.812,8:1.860,7:1.895}.get(len(x)-1,1.8); return round(m,1),round(m-t*se,1),round(m+t*se,1),int((x>0).sum()),len(x)
print('delta T1-G0 por dia OLD mean,lo,hi,dias+,n',ic(R.dT1G0_old),' NEW',ic(R.dT1G0_new))
A=pd.concat(allh); 
for lab,sub in (('RECUPERADAS(horas antes bad)',A[A.bad]),('YA INCLUIDAS',A[~A.bad]),('TODO hole60',A)):
    out={}
    for v in V:
        y=sub[sub['var']==v]; out[v]=(len(y),round(y.pnl.sum(),1),round(y.pnl.sum()/y.cost.sum(),3) if len(y) else None)
    dd=sub.groupby(['d','var']).pnl.sum().unstack().fillna(0); dl=(dd['T1']-dd['G0']) if 'T1' in dd else None
    print(lab,out,'delta T1-G0 €',round(out['T1'][1]-out['G0'][1],1),'por dia',ic(dl.values) if dl is not None and len(dl)>2 else None)
A.to_pickle(H+'A_hole60.pkl')
