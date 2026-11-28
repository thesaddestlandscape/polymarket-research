import json,re,glob,collections,bisect
d='p1b_real_B_20261128T033520Z'; 
S=[]  # (t, cpu_total_us, mem_total_us, pswpin, pgmajfault)
import datetime as dt
for l in open('p1b_sistema_20261128T033520Z_B.log'):
    m=re.match(r'(\d\d):(\d\d):(\d\d\.\d+) some avg10=([\d.]+).*?total=(\d+)\|some avg10=([\d.]+).*?total=(\d+)\|pswpin (\d+) pswpout (\d+) pgmajfault (\d+)',l)
    if not m: continue
    t=int(m[1])*3600+int(m[2])*60+float(m[3]); S.append((t,int(m[5]),int(m[7]),int(m[8]),int(m[10]),float(m[4])))
base=1795836800-(1795836800%86400)
I={}; P=[]
for l in open(d+'/ledger.jsonl'):
    try:r=json.loads(l)
    except: continue
    if r['k']=='intencion': I[r['oid_local']]=r
    if r['k']=='post' and r.get('t_send_ns'): P.append(r)
T=[s[0] for s in S]
def stall(ts):  # cpu stall us during the second containing ts, plus mem stall, swapin, majfault
    t=ts-base
    i=bisect.bisect_right(T,t)
    if i<2 or i>=len(S): return None
    a,b=S[i-1],S[i]; 
    return (b[1]-a[1],b[2]-a[2],b[3]-a[3],b[4]-a[4])
rows=[]
for p in P:
    ts=p['t_send_ns']/1e9; st=stall(ts)
    if st: rows.append((p['ack_ms'],st,I[p['oid_local']]['coin']))
import statistics as s
slow=[r for r in rows if r[0]>150]; fast=[r for r in rows if r[0]<=150]
for nm,g in (('slow>150',slow),('fast',fast)):
    print(nm,len(g),'cpu_stall_us med %.0f max %d | mem_stall_us med %.0f max %d | swapin pages med %.0f max %d | majfault med %.0f max %d'%(s.median(r[1][0] for r in g),max(r[1][0] for r in g),s.median(r[1][1] for r in g),max(r[1][1] for r in g),s.median(r[1][2] for r in g),max(r[1][2] for r in g),s.median(r[1][3] for r in g),max(r[1][3] for r in g)))
print('slow coins',collections.Counter(r[2] for r in slow))
# whole-run cpu/mem stall percent
a,b=S[0],S[-1]; print('run cpu stall %% of wall: %.2f  mem %.2f'%((b[1]-a[1])/((b[0]-a[0])*1e6)*100,(b[2]-a[2])/((b[0]-a[0])*1e6)*100), 'swapin pages total',b[3]-a[3])
# max single-second cpu stall
mx=max(S[i][1]-S[i-1][1] for i in range(1,len(S))); print('max 1s cpu stall us',mx)
