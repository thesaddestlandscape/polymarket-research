# s4a: mids presentes en las celdas (+cellsx) -> desenlace oficial (cache + gamma closed=true para lo que falte). Salida datalogs/mapa_escala/des.json + cobertura.
import pandas as pd, json, glob, sys, collections
sys.path.insert(0,'/root/polymarket-research')
OUT='/root/polymarket-research-datalogs/mapa_escala'
mids=collections.defaultdict(set)
for f in sorted(glob.glob(OUT+'/cells_*.csv.gz')):
    x=pd.read_csv(f,usecols=['marco','mid','dia'],dtype={'mid':str}).drop_duplicates()
    for m,g in x.groupby('marco'): mids[m]|=set(g.mid)
cache=json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
extra=json.load(open(OUT+'/mercados_extra_vol.json'))
des=dict(cache)
for mid,v in extra.items():
    if v[4]: des[mid]=v[4]
for m,s in mids.items(): print(m,'mids',len(s),'en cache',sum(1 for k in s if k in des))
falt=sorted(k for s in mids.values() for k in s if k not in des)
print('faltan',len(falt))
if falt:
    from analisis_maker_cancelacion_binance import desenlaces
    got=desenlaces(set(falt))
    for k,v in got.items():
        if v in ('YES','NO'): des[k]=v
for m,s in mids.items(): print(m,'mids',len(s),'con desenlace',sum(1 for k in s if k in des))
json.dump(des,open(OUT+'/des.json','w'))
