import pandas as pd, numpy as np, glob
H = __file__.rsplit('/',1)[0] + '/'
V = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H+'out/V_*.pkl'))], ignore_index=True); V = V[V['cov']=='ok']
T = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H+'out/T2_*.pkl'))], ignore_index=True)
R = V.merge(T, on='oid'); R['vida'] = (R.t_fuera-R.t_ini)/1000
print('sanity WSI_BASE == WSBASE_f_q:', np.allclose(R.WSI_BASE_q, R.WSBASE_f_q), ' n', len(R), 'real', int(R.real_fill.sum()))
R['ev_any'] = (R.t_prn_any>0)   # existe print visible (<=L, token o complemento) en vida+250ms
def conf(df, col):
    s = df[col]>1e-9; r = df.real_fill==1; tp=int((s&r).sum()); fp=int((s&~r).sum()); fn=int((~s&r).sum())
    return f'real={int(r.sum())} sim={int(s.sum())} tp={tp} prec={tp/max(tp+fp,1):.3f} rec={tp/max(tp+fn,1):.3f}'
cols = [('chain BASE (motor previo)','BASE_f_q'),('chain OPT','OPT_f_q'),('WSI BASE','WSI_BASE_q'),('WSI OPT','WSI_OPT_q'),('WSXS BASE','WSXS_BASE_q'),('WSXS OPT','WSXS_OPT_q'),('WSXD BASE','WSXD_BASE_q'),('WSXD OPT','WSXD_OPT_q')]
for seg, df in (('TOTAL', R), ('vida>=1.5s', R[R.vida>=1.5])):
    print('==', seg, 'n', len(df))
    for nm, c in cols: print(f'  {nm:26s}', conf(df, c))
    r = df[df.real_fill==1]; print('  techo evento visible (print<=L tok/comp en vida): reales con evento', int(r.ev_any.sum()), 'de', len(r), f'= {r.ev_any.mean():.3f} | ordenes con evento', int(df.ev_any.sum()), 'P(fill|evento)', round(float(df[df.ev_any].real_fill.mean()),3))
for c in ('eth','sol','xrp'):
    df = R[R.coin==c]; print('== moneda', c, 'n', len(df))
    for nm, col in cols[:1]+cols[2:3]+cols[4:5]+cols[6:7]: print(f'  {nm:26s}', conf(df, col))
    print('  techo evento reales', int(df[df.real_fill==1].ev_any.sum()), 'de', int(df.real_fill.sum()))
# reales sin evento visible: FN no atribuibles a reloj/motor (no hay print en cinta WS)
r = R[R.real_fill==1]
print('reales n', len(r), 'sin evento visible', int((~r.ev_any).sum()), '| con evento y WSXS BASE no los da', int((r.ev_any & (r.WSXS_BASE_q<=1e-9)).sum()), '| con evento y WSXS OPT no los da', int((r.ev_any & (r.WSXS_OPT_q<=1e-9)).sum()))
print('de los 131 FN chain-BASE: WSXS BASE da', int(((r.BASE_f_q<=1e-9)&(r.WSXS_BASE_q>1e-9)).sum()), 'WSXD BASE da', int(((r.BASE_f_q<=1e-9)&(r.WSXD_BASE_q>1e-9)).sum()), 'WSI BASE da', int(((r.BASE_f_q<=1e-9)&(r.WSI_BASE_q>1e-9)).sum()), 'n FN', int((r.BASE_f_q<=1e-9).sum()))
# bootstrap por cluster del recall (dia-ventana 5 min): IC90
R['cl'] = R.dia+'_'+(R.t_ini//300000).astype(str)
def boot(df, col, n=2000):
    rng=np.random.default_rng(1); g=df.groupby('cl'); a=np.array([[((x[col]>1e-9)&(x.real_fill==1)).sum(), (x.real_fill==1).sum(), (x[col]>1e-9).sum()] for _,x in g])
    rec=[];pre=[]
    for _ in range(n):
        s=a[rng.integers(0,len(a),len(a))].sum(0); rec.append(s[0]/max(s[1],1)); pre.append(s[0]/max(s[2],1))
    return np.percentile(rec,[5,95]).round(3).tolist(), np.percentile(pre,[5,95]).round(3).tolist(), len(a)
for nm,c in cols[:1]+cols[2:3]+cols[4:5]+cols[6:7]: print('IC90 clusters (recall, precision) TOTAL', nm, boot(R,c))
