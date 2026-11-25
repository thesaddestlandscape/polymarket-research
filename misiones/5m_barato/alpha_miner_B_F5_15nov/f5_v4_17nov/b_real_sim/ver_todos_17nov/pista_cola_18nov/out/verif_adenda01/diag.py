import gzip, pickle, collections, pandas as pd, numpy as np
FX='/tmp/claude-0/-root-polymarket-research/5055698c-f1c6-493f-8e00-51095bf98a56/scratchpad/fx/fx30m.csv.gz'
E=pd.read_pickle('/tmp/claude-0/-root-polymarket-research/5055698c-f1c6-493f-8e00-51095bf98a56/scratchpad/E_fxB.pkl')
E['C1']=E.q150-E.S>1e-9
sub=E[(E.n_mk==1)&E.C1&E.dec_eq_S&(E.WA_c>0)].sort_values('t')
sub=sub.iloc[::max(1,len(sub)//6)].head(6)
print('n dec_eq_S & WA_c>0 en prim:', len(E[(E.n_mk==1)&E.C1&E.dec_eq_S&(E.WA_c>0)]), 'de', len(E[(E.n_mk==1)&E.C1&E.dec_eq_S]))
keys={(r.X,r.p):r for r in sub.itertuples()}; toks={k[0] for k in keys}|{None}
comp={}
# comp tokens: need T prints of comp BUY at 1-p; just show same-token d and T lines + all T of ANY token within window by price
ev=collections.defaultdict(list)
with gzip.open(FX,'rt') as f:
    for l in f:
        c=l.rstrip('\n').split(',')
        if len(c)<8: continue
        if c[0] in ('d','T') and c[2] in toks:
            ev[c[2]].append(c)
for (X,p),r in keys.items():
    print('\n== evento t=%d X=...%s p=%.2f S=%.2f nT=%d ty=%s q150=%.1f WA_c=%.2f WA_c0=%.2f'%(r.t,X[-6:],p,r.S,r.nT,r.ty,r.q150,r.WA_c,r.WA_c0))
    for c in ev[X]:
        t=int(c[6])
        if r.t-1000<=t<=r.t+400:
            if c[0]=='d' and c[3]=='B' and abs(float(c[4])-p)<1e-6: print('  d  %+5d size=%s'%(t-r.t,c[5]))
            if c[0]=='T' and abs(float(c[3])-p)<1e-6: print('  T  %+5d %s sz=%s'%(t-r.t,c[4],c[5]))
