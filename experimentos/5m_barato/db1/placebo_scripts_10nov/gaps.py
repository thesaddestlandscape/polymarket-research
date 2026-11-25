import gzip,sys,datetime as d
files=sys.argv[1:]
ts=[];sym={}
for f in files:
    with gzip.open(f,'rt',errors='replace') as fh:
        try:
            for ln in fh:
                p=ln.rstrip('\n').split(',')
                if p[0]=='x' and len(p)==8 and p[7].isdigit():
                    r=int(p[7]); ts.append(r); sym.setdefault(p[2],[]).append(r)
                elif p[0]=='b' and len(p)==8 and p[1].isdigit():
                    ts.append(int(p[1]))
        except EOFError as e: print('EOF truncado',f)
ts.sort()
iso=lambda t:d.datetime.fromtimestamp(t/1000,d.UTC).strftime('%m-%dT%H:%M:%S.%f')[:-3]
print('n',len(ts),'primero',iso(ts[0]),'ultimo',iso(ts[-1]))
g=[(b-a,a,b) for a,b in zip(ts,ts[1:]) if b-a>3000]
print('huecos conjuntos >3s (x+b):',len(g)); 
for x in sorted(g,reverse=True)[:12]: print(' %.1fs  %s -> %s'%(x[0]/1000,iso(x[1]),iso(x[2])))
print('>=30s:',sum(1 for x in g if x[0]>=30000),' >60s:',sum(1 for x in g if x[0]>60000))
for s,v in sym.items():
    v.sort(); gg=[(b-a,a) for a,b in zip(v,v[1:]) if b-a>60000]
    print(s,'n_x',len(v),'huecos x>60s:',[(round(x/1000,1),iso(a)) for x,a in gg][:5])
