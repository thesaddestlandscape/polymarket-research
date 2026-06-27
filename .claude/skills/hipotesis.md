# Estado de hipótesis activas

Muestra el estado actualizado de todas las hipótesis con datos reales del shadow.

## Instructions

Run this analysis:

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
params = json.load(open('data/shadow/strategy_params.json'))

def ic(wins, n):
    return ((wins+1)/(n+2)-0.5)*min(1.0, n/20)

by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto'])

print("=== H-REGIMEN (BUY_YES vs BUY_NO en #15min) ===")
for side in ['BUY_YES','BUY_NO']:
    sub = [r for r in rows if r.get('subtype','').endswith('15min') and r.get('decision')==side and r['strategy']=='UPDOWN_GBM']
    if sub:
        w=sum(int(r['acierto']) for r in sub); n=len(sub); pnl=sum(float(r['pnl_neto']) for r in sub)
        print(f"  {side}: {w}/{n} ({w/n*100:.0f}%) IC={ic(w,n):+.3f} PNL={pnl:+.2f}€")
print("  Veredicto: BUY_NO domina → H confirmada para #15min")

print()
print("=== H-60MIN (GBM en ventanas largas) ===")
for par in ['BTC','ETH','SOL']:
    k = f"UPDOWN_GBM#{par}#60min"
    d = by_sub.get(k, {'n':0,'win':0,'pnl':0.0})
    if d['n'] > 0:
        ic_v = ic(d['win'], d['n'])
        ops_falta = max(0, 40-d['n'])
        print(f"  {par}#60min: {d['win']}/{d['n']} IC={ic_v:+.3f} PNL={d['pnl']:+.2f}€  {'→ '+str(ops_falta)+' ops para n≥40' if ops_falta else '✅ n≥40'}")

print()
print("=== H-ORDER_FLOW-DECAY (DELTA_MAX=0.46, solo BUY_NO) ===")
k = "ORDER_FLOW_5M"
d = by_sub.get(k, {'n':0,'win':0,'pnl':0.0})
if d['n'] > 0:
    print(f"  Agregado: {d['win']}/{d['n']} IC={ic(d['win'],d['n']):+.3f} PNL={d['pnl']:+.2f}€")
of_rows = [r for r in rows if r['strategy']=='ORDER_FLOW_5M']
for par in ['BTC','SOL']:
    sub = [r for r in of_rows if r.get('subtype','').split('#')[0].upper() == par]
    if sub:
        w=sum(int(r['acierto']) for r in sub); n=len(sub)
        print(f"  {par}: {w}/{n} ({w/n*100:.0f}%) IC={ic(w,n):+.3f}")

print()
print("=== H-DRIFT60-BUY_YES_15MIN (filtro [0, +0.5%)) ===")
yes_rows = [r for r in rows if r.get('subtype','').endswith('15min') and r.get('decision')=='BUY_YES' and r['strategy']=='UPDOWN_GBM']
if yes_rows:
    w=sum(int(r['acierto']) for r in yes_rows); n=len(yes_rows); pnl=sum(float(r['pnl_neto']) for r in yes_rows)
    print(f"  BUY_YES forward (filtro activo): {w}/{n} ({w/n*100:.0f}%) IC={ic(w,n):+.3f} PNL={pnl:+.2f}€")
    if n >= 20:
        print(f"  → Con n={n}≥20, verificar si IC≥0.15 se sostiene")
    if n >= 40:
        print(f"  → Con n={n}≥40, revisar si umbral 0.5% es óptimo o puede subir a 0.7%")

print()
print("=== H-WEEKLY-PRICE (mercados semanales) ===")
for par in ['BTC','ETH','SOL']:
    k = f"UPDOWN_GBM#{par}#weekly"
    d = by_sub.get(k, {'n':0,'win':0,'pnl':0.0})
    if d['n'] > 0:
        print(f"  {par}: {d['win']}/{d['n']} IC={ic(d['win'],d['n']):+.3f} PNL={d['pnl']:+.2f}€")

print()
print("=== PENDIENTES: bloquear hora 18h GBM ===")
gbm_rows = [r for r in rows if r['strategy']=='UPDOWN_GBM']
by_hour_gbm = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in gbm_rows:
    h = r['prediction_timestamp'][11:13] if len(r.get('prediction_timestamp',''))>13 else '??'
    by_hour_gbm[h]['n']+=1; by_hour_gbm[h]['win']+=int(r['acierto']); by_hour_gbm[h]['pnl']+=float(r['pnl_neto'])
h18 = by_hour_gbm.get('18',{'n':0,'win':0,'pnl':0.0})
if h18['n'] > 0:
    accion = '→ BLOQUEAR ya (n≥15)' if h18['n']>=15 else f"→ esperar {15-h18['n']} ops más"
    print(f"  GBM 18h UTC: {h18['win']}/{h18['n']} IC={ic(h18['win'],h18['n']):+.3f} PNL={h18['pnl']:+.2f}€  {accion}")
EOF
```

After the analysis, comment on:
1. Which hypotheses are confirmed/refuted/still accumulating
2. What actions are needed (block hour, adjust threshold, etc.)
3. ETA para cada estrategia candidata a live
