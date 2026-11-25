import sys,glob,collections,datetime
# uso: permin.py HH:MM HH:MM fichero.seg.csv...  -> filas/min por tipo
a,b=sys.argv[1],sys.argv[2]; c=collections.defaultdict(lambda: collections.Counter())
for f in sys.argv[3:]:
    for l in open(f):
        p=l.strip().split(","); 
        if len(p)!=3 or not p[0].isdigit(): continue
        s,t,n=p; m=datetime.datetime.fromtimestamp(int(s),datetime.timezone.utc).strftime('%H:%M')
        if a<=m<=b: c[m][t]+=int(n)
for m in sorted(c): print(m,*(f'{t}={c[m][t]}' for t in 'BdTG'))
