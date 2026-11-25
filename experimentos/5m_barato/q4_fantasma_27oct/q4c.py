import pickle, bisect, random
from collections import defaultdict
d=pickle.load(open('/root/polymarket-research/experimentos/5m_barato/q4_fantasma_27oct/q4_unidades.pkl','rb')); UB=d['UB']; NZ=d['NZ']
OFFD={D:sorted(v)[len(v)//2] for D,v in NZ.items()}
NS={D:sorted(x-OFFD[D] for x in v) for D,v in NZ.items()}
def ecdf(D,x): return bisect.bisect_left(NS[D],x)/len(NS[D])
def ev(U):
    P=sum(u[2] for u in U); C=sum(u[3] for u in U); return P/C if C else float('nan')
def boot(U,B=2000,seed=2711):
    g=defaultdict(lambda:[0.0,0.0])
    for u in U: g[u[1]][0]+=u[2]; g[u[1]][1]+=u[3]
    L=list(g.values()); r=random.Random(seed); o=[]
    if not L: return float('nan'),float('nan')
    for _ in range(B):
        P=C=0.0
        for _ in range(len(L)):
            a=L[r.randrange(len(L))]; P+=a[0]; C+=a[1]
        o.append(P/C if C else 0)
    o.sort(); return o[int(.05*B)],o[int(.95*B)-1]
def rep(lab,U):
    if not U: print('%-46s n=0'%lab); return
    lo,hi=boot(U); print('%-46s n=%5d coste=%7.1f EVw=%+.4f IC90c=(%+.3f,%+.3f)'%(lab,len(U),sum(u[3] for u in U),ev(U),lo,hi),flush=True)
S=[x for x in UB if x['dt']<1000]
print('unidades <1 s',len(S),'| con t_exch',sum(x['e'] is not None for x in S))
# (e) delay recv - t_exch de los primeros prints
dl=sorted(x['recv']-x['e'] for x in S if x['e'] is not None); n=len(dl)
print('(e) recv-t_exch primeros prints <1 s: p10=%.0f p50=%.0f p90=%.0f p99=%.0f ms'%tuple(dl[int(f*(n-1))] for f in(.1,.5,.9,.99)))
al=sorted(x['recv']-x['e'] for x in UB if x['e'] is not None and x['dt']>=5000); m=len(al)
print('    idem primeros prints >=5 s (control): p10=%.0f p50=%.0f p90=%.0f p99=%.0f ms'%tuple(al[int(f*(m-1))] for f in(.1,.5,.9,.99)))
# (c) FX_d
print('\n(c) FX_d = t_exch + d < t0+85 (fraccion de unidades <1 s con t_exch conocido y por EUR)')
SE=[x for x in S if x['e'] is not None]
for dd in (0,100,200,300,500):
    F=[x for x in SE if x['e']+dd<x['t0']+85]; C=sum(x['u'][3] for x in SE)
    print(' d=%3d  fantasma %4d/%d = %.1f%%  por EUR %.1f%% | EVw fantasma %+.3f  EVw resto %+.3f'%(dd,len(F),len(SE),100*len(F)/len(SE),100*sum(x['u'][3] for x in F)/C,ev([x['u'] for x in F]),ev([x['u'] for x in SE if not x['e']+dd<x['t0']+85])))
# (d) subtramos
print('\n(d) subtramos de <1 s (dt desde t0): n, FX_0, FX_300, EVw total / sin FX_0 / sin FX_300')
for a,b in ((85,200),(200,400),(400,1000)):
    T=[x for x in SE if a<=x['dt']<b]
    if not T: continue
    f0=[x for x in T if x['e']<x['t0']+85]; f3=[x for x in T if x['e']+300<x['t0']+85]
    print(' [%3d,%4d) n=%4d FX0=%.0f%% FX300=%.0f%% | EVw %+.3f / sinFX0 %+.3f / sinFX300 %+.3f'%(a,b,len(T),100*len(f0)/len(T),100*len(f3)/len(T),ev([x['u'] for x in T]),ev([x['u'] for x in T if x not in f0]),ev([x['u'] for x in T if x not in f3])))
# (b) calibracion nula de FC
print('\n(b) FC observada vs esperada solo por ruido de reloj (unidades st=ok)')
for lab,cond in (('no-FX0 (t_exch>=t0+85)',lambda x:x['e']>=x['t0']+85),('FX0 (t_exch<t0+85)',lambda x:x['e']<x['t0']+85)):
    T=[x for x in S if x['st']=='ok' and x['e'] is not None and cond(x)]
    if not T: continue
    obs=sum(x['fc'] for x in T)/len(T); exp=sum(ecdf(x['key'][0],x['t0']+85-x['e']) for x in T)/len(T)
    print(' %-26s n=%4d FC obs=%.1f%%  esperada por ruido (si e fuera el evento)=%.1f%%'%(lab,len(T),100*obs,100*exp))
# (a) ambiguos: cotas
print('\n(a) FC con ambiguos (unidades <1 s con st ok|amb): cota inf (todos los candidatos), sup (alguno), resuelta=mas cercano a t_exch+OFF')
inf=sup=res=0; N=0
for x in S:
    if x['st']=='ok': c=[x['cas']+x['OFF']]
    elif x['st']=='amb' and x['cands']: c=x['cands']
    else: continue
    N+=1; th=x['t0']+85+x['OFF']; v=[ci<th for ci in c]
    inf+=all(v); sup+=any(v)
    best=min(c,key=lambda ci:abs(ci-(x['e']+x['OFF']))) if x['e'] is not None else c[0]; res+=best<th
print(' N=%d  FC_inf=%.1f%%  FC_sup=%.1f%%  FC_resuelta=%.1f%%'%(N,100*inf/N,100*sup/N,100*res/N))
# veredicto numerico
print('\nResumen <1 s: PRIM literal (FX0|FC ok) = %d/%d = %.1f%% ; 5-20 s: %d/%d'%(sum(x['prim'] for x in S),len(S),100*sum(x['prim'] for x in S)/len(S),sum(x['prim'] for x in UB if 5000<=x['dt']<20000),sum(1 for x in UB if 5000<=x['dt']<20000)))
