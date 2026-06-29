---
name: ic
description: Análisis IC detallado por subtipo con matriz de decisión integrada. Muestra tendencias recientes vs histórico, split BUY_YES/BUY_NO, análisis horario ORDER_FLOW, y progreso hacia umbral live. Triggers: "ic", "información coefficient", "análisis ic", "cómo van las estrategias", "ver ICs", "estadísticas".
---

# Análisis IC completo con matriz de decisión

## Paso 1 — IC global por subtipo con tendencia

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
_raw = json.load(open('data/shadow/strategy_params.json'))
params = _raw.get('estrategias', _raw)

def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)

pnl_t = sum(float(r['pnl_neto']) for r in rows)
wins_t = sum(int(r['acierto']) for r in rows)
n_t = len(rows)
print(f"GLOBAL: {n_t} ops | {wins_t}W/{n_t-wins_t}L ({wins_t/n_t*100:.1f}%) | PNL={pnl_t:+.2f}€ | Bankroll={20+pnl_t:.2f}€")

by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0,'rows':[]})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto']); by_sub[k]['rows'].append(r)

print("\n=== IC POR SUBTIPO — ordenado por PNL ===")
print(f"  {'Estrategia':38s} {'W/N':>12} {'%':>5} {'PNL':>7} {'IC':>7} {'ult20':>7}  Estado")
print("  " + "─"*85)
for k, d in sorted(by_sub.items(), key=lambda x: x[1]['pnl'], reverse=True):
    if d['n'] < 5: continue
    ic_v = ic(d['win'], d['n'])
    r20 = d['rows'][-20:]; w20 = sum(int(r['acierto']) for r in r20)
    ic20 = ic(w20, len(r20))
    trend = "📈" if ic20 - ic_v > 0.05 else "📉" if ic_v - ic20 > 0.05 else "─"
    flag = ""
    if ic_v >= 0.10 and d['n'] >= 40: flag = "🔥 LIVE"
    elif ic_v >= 0.08 and d['n'] >= 40: flag = "✅ CAND"
    elif ic_v < -0.10 and d['n'] >= 15: flag = "🚫 MALA"
    p = params.get(k, {}); activa = "✅" if p.get('activa', True) else "🚫"
    print(f"  {activa} {k:36s} {d['win']:4d}/{d['n']:3d}  {d['win']/d['n']*100:4.0f}%  {d['pnl']:+6.2f}  {ic_v:+.3f}  {ic20:+.3f} {trend}  {flag}")
EOF
```

## Paso 2 — Análisis horario ORDER_FLOW (¿cambiar blacklist?)

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)

BLACKLIST = {2, 7, 9, 10, 11, 22}
PAIR_BL = {'ETH','BNB','XRP','DOGE'}
of_rows = [r for r in rows if r['strategy']=='ORDER_FLOW_5M' and not any(p in r.get('subtype','').upper() for p in PAIR_BL)]

by_h = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in of_rows:
    h = r.get('prediction_timestamp','')[11:13]
    if h: by_h[h]['n']+=1; by_h[h]['win']+=int(r['acierto']); by_h[h]['pnl']+=float(r['pnl_neto'])

print("=== ORDER_FLOW por hora UTC (BTC+SOL) ===")
alertas_bl = []
for h in sorted(by_h.keys(), key=int):
    d = by_h[h]
    if d['n'] < 3: continue
    ic_v = ic(d['win'], d['n'])
    bl = "🚫" if int(h) in BLACKLIST else "✅"
    conf = "**" if d['n'] >= 20 else " ?" if d['n'] < 10 else "  "
    alerta = ""
    if int(h) in BLACKLIST and ic_v > 0.05 and d['n'] >= 15: alerta = " ← considerar DESBLOQUEAR"
    if int(h) not in BLACKLIST and ic_v < -0.08 and d['n'] >= 15: alerta = " ← considerar BLOQUEAR"
    if alerta: alertas_bl.append(f"  {h}h: IC={ic_v:+.3f} n={d['n']}{alerta}")
    print(f"  {h}h {bl}{conf}: {d['win']:3d}/{d['n']:3d} ({d['win']/d['n']*100:.0f}%) IC={ic_v:+.3f} PNL={d['pnl']:+.2f}€")
if alertas_bl:
    print("\nALERTAS BLACKLIST:")
    for a in alertas_bl: print(a)
EOF
```

## Paso 3 — Split BUY_YES vs BUY_NO + progreso hacia live

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)

by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto'])

print("=== BUY_YES vs BUY_NO por ventana (GBM) ===")
for ventana in ['5min','15min','60min']:
    for side in ['BUY_YES','BUY_NO']:
        sub = [r for r in rows if r.get('subtype','').endswith(ventana) and r.get('decision')==side and r['strategy']=='UPDOWN_GBM']
        if sub and len(sub) >= 5:
            w=sum(int(r['acierto']) for r in sub); n=len(sub); pnl=sum(float(r['pnl_neto']) for r in sub)
            print(f"  {side:8s} #{ventana:5s}: {w:3d}/{n:3d} ({w/n*100:.0f}%) PNL={pnl:+.2f}€ IC={ic(w,n):+.3f}")

print()
print("=== PROGRESO HACIA LIVE (umbral: IC≥0.08 n≥40) ===")
candidatas = []
for k, d in sorted(by_sub.items(), key=lambda x: -x[1]['n']):
    ic_v = ic(d['win'], d['n'])
    if ic_v > 0.04 and d['n'] >= 10:
        ops_falta = max(0, 40-d['n'])
        ic_falta = max(0, 0.08-ic_v)
        if ops_falta > 0 or ic_falta > 0:
            eta = f"{ops_falta//6+1}d" if ops_falta > 0 else "IC insuficiente"
            candidatas.append((ic_v, d['n'], f"  {k:38s} n={d['n']:3d} IC={ic_v:+.3f} {'→ '+str(ops_falta)+' ops (ETA '+eta+')' if ops_falta else '→ IC bajo umbral'}"))
for _, _, line in sorted(candidatas, reverse=True)[:8]:
    print(line)
EOF
```

## Presentar al usuario

1. Tabla IC con tendencia (ult20 vs histórico) — destacar cambios >0.05
2. Alertas de blacklist horaria ORDER_FLOW si las hay
3. Split BUY_YES/BUY_NO — confirmar que BUY_NO domina en #15min
4. Progreso hacia live — cuántas ops faltan por estrategia
5. Sugerir `/decision` si hay algo que requiere acción inmediata, o `/analizar <estrategia>` si hay una que merece análisis profundo de features
