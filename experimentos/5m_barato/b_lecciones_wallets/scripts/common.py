import csv,bisect,json,math
from datetime import datetime,timezone
DL='/root/polymarket-research-datalogs/'
def iso2e(s): return datetime.fromisoformat(s.replace('Z','+00:00')).timestamp()
def load_bt(days,assets=('ETH','SOL','XRP')):
    """bookTicker mid por recepción: {asset:(ts_list, mid_list)}"""
    T={a:[] for a in assets}; M={a:[] for a in assets}
    for d in days:
        with open(DL+f'binance_bookticker_{d}.csv') as fh:
            r=csv.reader(fh); next(r)
            for row in r:
                a=row[1]
                if a in T:
                    T[a].append(int(row[0])/1000.0); M[a].append(float(row[4]))
    out={}
    for a in assets:
        z=sorted(zip(T[a],M[a])); out[a]=([x for x,_ in z],[y for _,y in z])
    return out
def px_at(ser,t):
    ts,ms=ser; i=bisect.bisect_right(ts,t)-1
    if i<0: return None
    if t-ts[i]>130: return None   # bookTicker solo escribe si cambia: hueco = sin cambio (tope 130 s)
    return ms[i]
def ret_bps(ser,t0,t1):
    a=px_at(ser,t0); b=px_at(ser,t1)
    if a is None or b is None: return None
    return (b/a-1)*1e4
def load_cl(days,assets=('ETH','SOL','XRP'),root='/root/polymarket-research/data/prices/'):
    import gzip,os
    T={a:[] for a in assets}; P={a:[] for a in assets}
    for d in days:
        f=root+f'chainlink_{d}.csv'
        fh=open(f) if os.path.exists(f) else gzip.open(f+'.gz','rt')
        r=csv.reader(fh); next(r)
        for row in r:
            if row[1] in T and row[4]=='chainlink':
                T[row[1]].append(iso2e(row[0])); P[row[1]].append(float(row[2]))
        fh.close()
    out={}
    for a in assets:
        z=sorted(zip(T[a],P[a])); out[a]=([x for x,_ in z],[y for _,y in z])
    return out
def twap_ref(cl,a,e):
    """twap60 oficial aproximado del segundo e: media de ticks recibidos en [e-62,e-3] (por recepción)"""
    ts,ps=cl[a]; i=bisect.bisect_left(ts,e-62); j=bisect.bisect_right(ts,e-3)
    if j-i<20: return None
    return sum(ps[i:j])/(j-i)
