# Análisis IC completo

Análisis detallado de Information Coefficient por subtipo con contexto de hipótesis activas.

## Instructions

Run this analysis and present results clearly:

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
params = json.load(open('data/shadow/strategy_params.json'))

# Global
pnl = sum(float(r['pnl_neto']) for r in rows)
wins = sum(int(r['acierto']) for r in rows)
n = len(rows)
print(f"=== GLOBAL: {n} ops | {wins}W/{n-wins}L ({wins/n*100:.1f}%) | PNL={pnl:+.2f}€ | Bankroll={20+pnl:.2f}€")
print()

# Por subtipo con IC bayesiano
by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0,'rows':[]})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1
    by_sub[k]['win']+=int(r['acierto'])
    by_sub[k]['pnl']+=float(r['pnl_neto'])
    by_sub[k]['rows'].append(r)

print("=== IC POR SUBTIPO (ordenado por PNL) ===")
for k,d in sorted(by_sub.items(), key=lambda x: x[1]['pnl'], reverse=True):
    ic=((d['win']+1)/(d['n']+2)-0.5)*min(1.0,d['n']/20)
    estado = ""
    if ic >= 0.10 and d['n'] >= 40: estado = " 🔥 LIVE READY"
    elif ic >= 0.08 and d['n'] >= 40: estado = " ✅ CANDIDATA"
    elif d['n'] >= 40 and ic < 0.05: estado = " ⚠️ IC BAJO"
    elif ic < -0.10 and d['n'] >= 15: estado = " 🚫 MALA"
    # Últimas 10 ops
    ultimas = d['rows'][-10:]
    wr_rec = sum(int(r['acierto']) for r in ultimas)/len(ultimas)*100 if ultimas else 0
    print(f"  {k:35s} {d['win']}/{d['n']:3d} ({d['win']/d['n']*100:.0f}%)  PNL={d['pnl']:+6.2f}  IC={ic:+.3f}  [ult10: {wr_rec:.0f}%]{estado}")

# Análisis por hora para ORDER_FLOW
print()
print("=== ORDER_FLOW por hora UTC (BTC+SOL activos) ===")
of_rows = [r for r in rows if r['strategy']=='ORDER_FLOW_5M' and r.get('subtype','').split('#')[0] in ('BTC','SOL','')]
by_hour = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in of_rows:
    h = r['prediction_timestamp'][11:13] if len(r.get('prediction_timestamp',''))>13 else '??'
    by_hour[h]['n']+=1; by_hour[h]['win']+=int(r['acierto']); by_hour[h]['pnl']+=float(r['pnl_neto'])
blacklist = {2,7,9,10,11,22}
for h in sorted(by_hour.keys()):
    d = by_hour[h]
    if d['n'] < 3: continue
    ic = ((d['win']+1)/(d['n']+2)-0.5)*min(1.0,d['n']/20)
    bl = " 🚫" if int(h) in blacklist else ""
    print(f"  {h}h UTC: {d['win']}/{d['n']} ({d['win']/d['n']*100:.0f}%) IC={ic:+.3f} PNL={d['pnl']:+.2f}€{bl}")

# Split BUY_YES vs BUY_NO en 15min
print()
print("=== BUY_YES vs BUY_NO #15min ===")
for side in ['BUY_YES','BUY_NO']:
    sub = [r for r in rows if r.get('subtype','').endswith('15min') and r.get('decision')==side and r['strategy']=='UPDOWN_GBM']
    if sub:
        w=sum(int(r['acierto']) for r in sub); n2=len(sub); pnl2=sum(float(r['pnl_neto']) for r in sub)
        ic=((w+1)/(n2+2)-0.5)*min(1.0,n2/20)
        print(f"  {side:8s} #15min: {w}/{n2} ({w/n2*100:.0f}%) PNL={pnl2:+.2f}€ IC={ic:+.3f}")

# Progreso hacia umbral live
print()
print("=== PROGRESO HACIA LIVE (umbral IC≥0.08 n≥40) ===")
for k,d in sorted(by_sub.items(), key=lambda x: -x[1]['n']):
    ic=((d['win']+1)/(d['n']+2)-0.5)*min(1.0,d['n']/20)
    if ic > 0 and d['n'] >= 10:
        ops_falta = max(0, 40-d['n'])
        ic_falta = max(0, 0.08-ic)
        if ops_falta > 0 or (ic_falta > 0 and d['n'] >= 40):
            print(f"  {k:35s} n={d['n']:3d} IC={ic:+.3f}  {'→ '+str(ops_falta)+' ops para n≥40' if ops_falta else '→ IC insuficiente'}")
EOF
```

After the analysis, highlight:
1. Any strategy that newly crossed IC≥0.10 n≥40 (live ready)
2. Trends in recent 10 ops vs historical (improving/deteriorating)  
3. Hours that should be added/removed from ORDER_FLOW blacklist based on current data
4. Next hypothesis to validate based on n progress
