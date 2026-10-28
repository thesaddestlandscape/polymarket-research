#!/usr/bin/env python3
"""E02-real paso C2 (PREREG_E02REAL.md + ADENDA1 + ADENDA2: regla de casado CORREGIDA): casa cada fill con su fila T y mide el barrido a 1 s. python3 -I fills.json ext_dir out.json"""
import json,sys,glob,os,collections
FJ,EXT,OUT=sys.argv[1:4]
F=json.load(open(FJ))
for i,f in enumerate(F): f['i']=i
VENT=(-4000,0)       # ventana primaria bloque (ms)
VENT2=(-8000,1000)   # sensibilidad
W=(250,500,1000,2000)
def parse_book(s):
    d={}
    if s:
        for z in s.split(';'):
            if ':' in z:
                p,q=z.split(':'); d[float(p)]=float(q)
    return d
def cand_T(ts,fl,tok,side,pr,acc,v):
    pass
byTokT=collections.defaultdict(list); byTokX=collections.defaultdict(list)
for f in F:
    byTokT[f['huella']['tok_t']].append(f); byTokX[f['tok_x']].append(f)
WIN={}
for f in F:
    for tk in (f['tok_x'],f['huella']['tok_t']):
        lo,hi=f['ts_est']*1000-420000,f['ts_est']*1000+4000
        a=WIN.get(tk); WIN[tk]=(lo,hi) if a is None else (min(a[0],lo),max(a[1],hi))
res={f['i']:{'i':f['i'],'L2':None,'TOB':None} for f in F}
def lado_ok(f,pr,side,sz):
    h=f['huella']; pe=(1-round(f['precio'],4)) if h['tok_t']!=f['tok_x'] else round(f['precio'],4)
    return side==h['side_t'] and abs(pr-pe)<=0.02 and abs(sz-h['acc_t'])<=0.01
# ---------- L2 ----------
for fn in sorted(glob.glob(EXT+'/libro5_ms_*.txt')):
    b=os.path.basename(fn)[:-4]
    G=[]
    for l in open(fn[:-4]+'.G',errors='replace'):
        p=l.rstrip('\n').split(',')
        if len(p)>=8:
            try: G.append((p[2],int(p[6]),int(p[7]),p[3]))
            except: pass
    ev=collections.defaultdict(list)   # token -> [(seq,rec,kind,a,b,c)]
    for l in open(fn,errors='replace'):
        p=l.rstrip('\n').split(',')
        if len(p)<8: continue
        try: tk=p[2];rec=int(p[6]);seq=int(p[7])
        except: continue
        w=WIN.get(tk)
        if w is None or not (w[0]<=rec<=w[1]): continue
        if p[0]=='B': ev[tk].append((seq,rec,'B',p[3],p[4],0))
        elif p[0]=='d' and p[3]=='B': ev[tk].append((seq,rec,'d',float(p[4]),float(p[5]),0))
        elif p[0]=='T': ev[tk].append((seq,rec,'T',float(p[3]),p[4],float(p[5])))
    for f in F:
        h=f['huella']; blk=f['ts_est']*1000
        for vname,(lo,hi) in (('p',VENT),('s',VENT2)):
            cs=[e for e in ev.get(h['tok_t'],[]) if e[2]=='T' and blk+lo<=e[1]<=blk+hi and lado_ok(f,e[3],e[4],e[5])]
            if not cs: continue
            cs.sort(key=lambda e:e[0]); T=cs[-1]
            r={'stream':b,'vent':vname,'ncand':len(cs),'off_ms':blk-T[1],'t_fill':T[1],'seq':T[0]}
            exs=ev.get(f['tok_x'],[]); bk=None;bi=-1
            for k,e in enumerate(exs):
                if e[2]=='B' and e[1]<=T[1]-2000: bi=k
            if bi<0:
                for k,e in enumerate(exs):
                    if e[0]<T[0] and e[2]=='B': bi=k
            if bi<0: r['estado']='sin_B_previo'
            else:
                bk=parse_book(exs[bi][3]); recB=exs[bi][1]
                gap=[g for g in G if g[0] in (f['tok_x'],'*') and recB<g[1]<=T[1]+1000]
                if gap: r['estado']='gap_G:'+gap[0][3]
                else:
                    b0=round(f['precio'],4); smax=bk.get(b0,0.0); bkp=dict(bk); bk_base=dict(bk)
                    for e in exs[bi+1:]:
                        if e[1]>T[1]: break
                        if e[2]=='B': bkp=parse_book(e[3])
                        elif e[2]=='d':
                            if e[4]<=0: bkp.pop(e[3],None)
                            else: bkp[e[3]]=e[4]
                        else: continue
                        if e[1]>=T[1]-2000: smax=max(smax,bkp.get(b0,0.0))
                    r['S_pre']=smax; r['bb_pre']=max(bkp) if bkp else None; bk=dict(bk_base)
                    sw={w:None for w in W}; bb=None; empty=False
                    for e in exs[bi+1:]:
                        if e[1]>T[1]+max(W): break
                        if e[2]=='B': bk=parse_book(e[3])
                        elif e[2]=='d':
                            if e[4]<=0: bk.pop(e[3],None)
                            else: bk[e[3]]=e[4]
                        else: continue
                        bb=max(bk) if bk else None
                        if bb is None or bb<b0-1e-9:
                            dt=e[1]-T[1]
                            if dt>-300:
                                for w in W:
                                    if sw[w] is None and dt<=w: sw[w]=max(dt,0)
                    # ADENDA2: confirmacion por libro y sensibilidad del tamano del nivel en [t-300, t]
                    bk2=parse_book(exs[bi][3]); ser=[(exs[bi][1],bk2.get(b0,0.0))]
                    for e in exs[bi+1:]:
                        if e[1]>T[1]+400: break
                        if e[2]=='B': bk2=parse_book(e[3])
                        elif e[2]=='d':
                            if e[4]<=0: bk2.pop(e[3],None)
                            else: bk2[e[3]]=e[4]
                        else: continue
                        ser.append((e[1],bk2.get(b0,0.0)))
                    ini=[v for t0,v in ser if t0<=T[1]-300]; ini=ini[-1] if ini else None
                    win=[v for t0,v in ser if T[1]-300<=t0<=T[1]+300]
                    lp=[(T[1]-t0,v) for t0,v in ser if t0<=T[1] and v>0]
                    r['last_pos_ms']=lp[-1][0] if lp else None; r['last_pos_sz']=lp[-1][1] if lp else None
                    r['pos_hist']=[(T[1]-t0,v) for t0,v in ser if T[1]-1500<=t0<=T[1]+150][-12:]
                    r['conf_libro']=bool(ini is not None and win and min(win)<ini-0.01)
                    r['S_max300']=max([v for t0,v in ser if T[1]-300<=t0<=T[1]]+([ini] if ini is not None else [0.0]))
                    r['estado']='ok'; r['dt_sweep']=sw[2000]; r['sw']={str(w):(sw[w] is not None) for w in W}
                    # cobertura posterior: hay eventos de X hasta t_fill+1s o G? (si no hay ningun evento tras T el barrido=0 es 'sin evidencia' pero B tras operacion lo cubre)
                    r['n_post']=sum(1 for e in exs if T[0]<e[0] and e[1]<=T[1]+1000 and e[2] in('B','d'))
            key='L2p' if vname=='p' else 'L2s'
            prev=res[f['i']].get(key)
            if prev is None or (r.get('estado')=='ok' and prev.get('estado')!='ok'): res[f['i']][key]=r
# ---------- TOB (m5_registro) ----------
for d in ('20','21','22','23'):
    fn=f'{EXT}/m5_{d}.txt'
    if not os.path.exists(fn): continue
    q=collections.defaultdict(list);t=collections.defaultdict(list)
    for n,l in enumerate(open(fn,errors='replace')):
        p=l.rstrip('\n').split(',')
        try:
            if p[0]=='q': q[p[2]].append((int(p[7]),n,float(p[3]) if p[3] else None,float(p[5]) if p[5] else 0.0))
            elif p[0]=='t': t[p[2]].append((int(p[6]),n,float(p[3]),p[4],float(p[5])))
        except: continue
    for k in q: q[k].sort()
    for k in t: t[k].sort()
    for f in F:
        h=f['huella']; blk=f['ts_est']*1000
        for vname,(lo,hi) in (('p',VENT),('s',VENT2)):
            cs=[e for e in t.get(h['tok_t'],[]) if blk+lo<=e[0]<=blk+hi and lado_ok(f,e[2],e[3],e[4])]
            if not cs: continue
            T=cs[-1]; qx=q.get(f['tok_x'],[]); b0=round(f['precio'],4)
            pre=[e for e in qx if e[0]<=T[0]]
            r={'vent':vname,'ncand':len(cs),'off_ms':blk-T[0],'t_fill':T[0],'dia':d}
            if not pre or T[0]-pre[-1][0]>120000: r['estado']='sin_q_previo'
            else:
                lp=pre[-1]; r['bb_pre']=lp[2]; r['S_pre']=lp[3] if lp[2] is not None and abs(lp[2]-b0)<1e-9 else None
                sw={w:None for w in W}
                for e in qx:
                    if e[0]<=T[0]: continue
                    if e[0]>T[0]+max(W): break
                    if e[2] is None or e[2]<b0-1e-9:
                        for w in W:
                            if sw[w] is None and e[0]-T[0]<=w: sw[w]=e[0]-T[0]
                r['estado']='ok'; r['sw']={str(w):(sw[w] is not None) for w in W}; r['dt_sweep']=sw[2000]
                r['n_post']=sum(1 for e in qx if T[0]<e[0]<=T[0]+1000)
            key='TOBp' if vname=='p' else 'TOBs'
            prev=res[f['i']].get(key)
            if prev is None or (r.get('estado')=='ok' and prev.get('estado')!='ok'): res[f['i']][key]=r
json.dump(list(res.values()),open(OUT,'w'))
c=collections.Counter()
for r in res.values():
    for k in ('L2p','L2s','TOBp','TOBs'):
        x=r.get(k); c[k+'_casado']+= x is not None; c[k+'_ok']+= bool(x and x.get('estado')=='ok')
print(len(F),dict(c))
