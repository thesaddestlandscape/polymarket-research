#!/usr/bin/env python3
import sys,glob,json,os,collections,time
sys.path.insert(0,'/root/polymarket-research/experimentos/5m_barato/a6_detector_vivo/calib_colas')
import analiza as A
coin=sys.argv[1]
C=A.C
TAG=os.environ.get('OUTTAG','')
outp=C+f'muestras_{coin}{TAG}.ndjson'
done=set()
if os.path.exists(outp):
    for l in open(outp):
        try: done.add(json.loads(l)['mkt'])
        except: pass
diag=collections.defaultdict(float)
for k in('lag_own','lag_mint'): diag[k]=[]
fo=open(outp,'a')
files=sorted(glob.glob(C+f'mk/{coin}_*.gz'))
STR=int(open(C+f'stride_{coin}').read()) if os.path.exists(C+f'stride_{coin}') else 1
files=files[::STR]
if os.environ.get('DIA'):
    files=[f for f in files if os.environ['DIA'] in f or True]
    import json as _j
    _tk=_j.load(open(C+'tokens.json')); _dm={}
    for _t,_v in _tk.items(): _dm[_v[1]]=_v[3]
    import datetime as _dt
    lo=float(os.environ['DIA_LO']); hi=float(os.environ['DIA_HI'])
    files=[f for f in files if lo<=_dm.get(f.split(coin+'_')[1][:-3],0)<hi]
STRIDE2=int(os.environ.get('STRIDE2','1'))
files=files[::STRIDE2]
t0=time.time(); n=0
def first(fl): return fl[0][0] if fl else None
for i,f in enumerate(files):
    m=f.split(f'{coin}_')[1][:-3]
    if m in done: continue
    S=A.procesa(coin,m,f,diag)
    for s in S:
        r=s['res']; rec={k:s[k] for k in('L','k','kind','cum','t0','T0','q0','D0','cierre','roto','n_niv')}
        rec['mkt']=m; rec['coin']=coin
        for nm in [k for k in r if k.startswith('sh_f')]:
            fl=r[nm]; acc=0.0; tf=None
            for (tt,x) in fl:
                acc+=x
                if tf is None and acc>=49.99: tf=tt
            rec[nm]=[first(fl),round(acc,3),tf]
        for nm in('rp_lo','rp_prop','rp_hi'):
            v=r[nm]; fl=v['fills']
            tf=None; acc=0.0
            for (tt,x) in fl:
                acc+=x
                if tf is None and acc>=49.99: tf=tt
            rec[nm]={'t1':first(fl),'tf':tf,'fill':round(sum(x for _,x in fl),3),'ca':round(v['ca_end'],3),'ct':round(v['ct_end'],3),'ctp':round(v['ctp_end'],3),
                     'apre':round(v['apre'],3),'ah_ready':v['ah_ready'],'f1':v['f1'],'snaps':{str(k):[round(a,3) for a in x] for k,x in v['snaps'].items()}}
        fo.write(json.dumps(rec)+'\n'); n+=1
    if not S:
        fo.write(json.dumps({'mkt':m,'vacio':True})+'\n')
    fo.flush()
    if i%50==0: print(coin,i,len(files),n,round(time.time()-t0),flush=True)
json.dump({k:(v if not isinstance(v,list) else v[:2000]) for k,v in diag.items()},open(C+f'diag_{coin}{TAG}.json','w'))
print('FIN',coin,n,round(time.time()-t0),flush=True)
