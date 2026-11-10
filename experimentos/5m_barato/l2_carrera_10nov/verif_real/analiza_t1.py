import pandas as pd, numpy as np, glob
H = __file__.rsplit('/',1)[0] + '/'
V = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H+'out/V_*.pkl'))], ignore_index=True); V = V[V['cov']=='ok']
T2 = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H+'out/T2_*.pkl'))], ignore_index=True)
X = pd.read_pickle(H+'out/T1_tx.pkl').drop_duplicates('order_hash', keep='first')   # primer tx de cada orden
R = V.merge(T2, on='oid'); R = R[R.real_fill==1].merge(X, left_on='oid', right_on='order_hash', how='left')
print('reales', len(R), 'con tx on-chain', int(R.tx.notna().sum()))
R['cl'] = R.dia+'_'+(R.t_ini//300000).astype(str); R['grp'] = np.where(R.BASE_f_q>1e-9, 'TP', 'FN'); R['grp2'] = np.where(R.WSXS_BASE_q>1e-9, 'TPx', 'FNx')
R['otros'] = R.S_tok - R.own_sh; R['solo'] = R.n_mk==1; R['multi'] = R.n_mk>=2; R['share'] = R.own_sh/R.S_tok
def pnl(q, L, g, rb): return q*(g-L) + rb*q*0.07*L*(1-L)*(1)
for rb in (0, 0.2): R[f'p{rb}'] = pnl(R.real_q, R.L, R.gana, rb)
R['c'] = R.real_q*R.L
def boot(df, rb, n=3000, seed=1):
    cl = df.groupby('cl')[[f'p{rb}','c']].sum().values; rng = np.random.default_rng(seed); ev=[]
    for _ in range(n):
        s = cl[rng.integers(0,len(cl),len(cl))].sum(0); ev.append(s[0]/s[1] if s[1]>0 else np.nan)
    return np.nanpercentile(ev,[5,95]).round(3).tolist()
def ln(nm, df):
    if len(df)==0: return f'{nm}: n=0'
    c = df.c.sum(); o = [f'{df[f"p{rb}"].sum()/c:+.3f} IC{boot(df,rb)}' for rb in (0,0.2)]
    return f'{nm}: n={len(df)} cl={df.cl.nunique()} acierto={df.gana.mean():.3f} L={df.L.mean():.3f} EV/E rb0 {o[0]} | rb0.2 {o[1]}'
print('--- estructura on-chain del primer tx (n makers, tamano tomador S_tok, share nuestro)')
for g, df in R.groupby('grp'):
    print(g, 'n', len(df), 'n_mk dist', df.n_mk.value_counts().sort_index().to_dict(), '| solo-nosotros(n_mk=1)', round(df.solo.mean(),3), '| S_tok med/p25/p75', df.S_tok.median(), df.S_tok.quantile(.25), df.S_tok.quantile(.75), '| otros_sh med', df.otros.median(), '| share nuestro med', round(df.share.median(),3), '| S_tok==nuestro', round(float((df.otros<1e-6).mean()),3), '| n_tokens_tx>1', round(float((df.n_tokens_tx>1).mean()),3))
from scipy.stats import mannwhitneyu, fisher_exact
a, b = R[R.grp=='TP'], R[R.grp=='FN']
print('MWU S_tok p=', round(mannwhitneyu(a.S_tok,b.S_tok).pvalue,4), 'MWU n_mk p=', round(mannwhitneyu(a.n_mk,b.n_mk).pvalue,4), 'Fisher solo p=', round(fisher_exact([[a.solo.sum(),(~a.solo).sum()],[b.solo.sum(),(~b.solo).sum()]])[1],4))
a, b = R[R.grp2=='TPx'], R[R.grp2=='FNx']
print('(motor sin fuga WSXS BASE) TPx n', len(a), 'solo', round(a.solo.mean(),3), 'S_tok med', a.S_tok.median(), '| FNx n', len(b), 'solo', round(b.solo.mean(),3), 'S_tok med', b.S_tok.median())
print('--- EV por grupo'); 
for g in ('TP','FN'): print(ln(g, R[R.grp==g]))
print(ln('TODOS reales', R))
print('--- EV por n_makers (todos los reales, sin FN/TP)')
for nm, m in (('solo-nuestro n_mk=1', R.solo), ('multi n_mk>=2', R.multi)): print(ln(nm, R[m]))
R['Sb'] = pd.cut(R.S_tok, [0,5.01,7,10.01,1000], labels=['<=5','5-7','7-10','>10'])
R['Ob'] = pd.cut(R.otros, [-1,1e-6,5,1000], labels=['0 (solo nosotros)','0-5','>5'])
print('--- EV por tamano del tomador (S_tok) x grupo')
for s, df in R.groupby('Sb', observed=True):
    for g in ('TP','FN'): print(ln(f'S_tok {s} {g}', df[df.grp==g]))
print('--- EV por tamano de OTROS makers x grupo')
for s, df in R.groupby('Ob', observed=True):
    for g in ('TP','FN'): print(ln(f'otros {s} {g}', df[df.grp==g]))
print('--- estrato n_mk x grupo')
for nm, m in (('solo', R.solo), ('multi', R.multi)):
    for g in ('TP','FN'): print(ln(f'{nm} {g}', R[m & (R.grp==g)]))
# diferencia FN-TP estandarizada por estrato (n_mk x Sb): pesos = coste total de cada estrato; IC bootstrap por cluster
R['st'] = R.solo.astype(str)+'_'+R.Sb.astype(str)
def dstd(df, rb):
    out=0; w=0
    for s, g in df.groupby('st'):
        a=g[g.grp=='FN']; b=g[g.grp=='TP']
        if a.c.sum()>0 and b.c.sum()>0: wt=g.c.sum(); out+=wt*(a[f'p{rb}'].sum()/a.c.sum()-b[f'p{rb}'].sum()/b.c.sum()); w+=wt
    return out/w if w else np.nan
rng=np.random.default_rng(3); cls=R.cl.unique(); gb={k:v for k,v in R.groupby('cl')}
for rb in (0,0.2):
    pt=dstd(R,rb); bs=[]
    for _ in range(2000):
        sm=pd.concat([gb[k] for k in rng.choice(cls,len(cls))]); bs.append(dstd(sm,rb))
    print(f'dif EV FN-TP estandarizada por (n_mk x S_tok) rb{rb}: {pt:+.3f} IC90 clusters {np.nanpercentile(bs,[5,95]).round(3).tolist()}  (bruta FN-TP: {R[R.grp=="FN"][f"p{rb}"].sum()/R[R.grp=="FN"].c.sum()-R[R.grp=="TP"][f"p{rb}"].sum()/R[R.grp=="TP"].c.sum():+.3f})')
print('--- por moneda'); 
for c in ('eth','sol','xrp'):
    for g in ('TP','FN'): print(ln(f'{c} {g}', R[(R.coin==c)&(R.grp==g)]))
print('--- por dia')
for d in sorted(R.dia.unique()):
    for g in ('TP','FN'): print(ln(f'{d} {g}', R[(R.dia==d)&(R.grp==g)]))
print('--- composicion FN/TP por moneda (n_mk, solo)'); print(R.groupby(['coin','grp']).agg(n=('oid','size'), solo=('solo','mean'), Smed=('S_tok','median')).round(3))
