---
name: inicio
description: Protocolo completo de inicio de sesión del bot Polymarket. Usar cuando el usuario quiere revisar el estado del bot, ver el bankroll actual, analizar IC por estrategia, o retomar una sesión. Triggers: "inicio", "estado", "cómo va", "dame el resumen", "qué ha pasado", "resumen sesión".
---

# Protocolo de inicio de sesión

Ejecuta todos los pasos en secuencia y presenta un resumen accionable al usuario.

## CRÍTICO: Detectar anomalías primero

Antes de mostrar el resumen completo, ejecuta este análisis de anomalías:

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
_raw = json.load(open('data/shadow/strategy_params.json'))
params = _raw.get('estrategias', _raw)

def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)

by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0,'rows':[]})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto']); by_sub[k]['rows'].append(r)

alertas = []

for k, d in by_sub.items():
    if d['n'] < 10: continue
    ic_total = ic(d['win'], d['n'])
    # Trend: últimas 20 vs histórico
    if d['n'] >= 25:
        r20 = d['rows'][-20:]
        w20 = sum(int(r['acierto']) for r in r20)
        ic_rec = ic(w20, 20)
        degradacion = ic_total - ic_rec
        if degradacion > 0.10 and ic_total > 0.05:
            alertas.append(f"⚠️ DEGRADACIÓN: {k} histórico IC={ic_total:+.3f} → reciente IC={ic_rec:+.3f} (delta={-degradacion:+.3f})")
        elif ic_rec >= 0.10 and ic_total < 0.05:
            alertas.append(f"🚀 MEJORA RECIENTE: {k} ult20 IC={ic_rec:+.3f} (total IC={ic_total:+.3f})")
    # Nueva estrategia cruzando umbral
    if ic_total >= 0.10 and d['n'] >= 40:
        alertas.append(f"🔥 LIVE READY: {k} — IC={ic_total:+.3f} n={d['n']}")
    # IC muy negativo activa
    if ic_total < -0.10 and d['n'] >= 15:
        p = params.get(k, {})
        if p.get('activa', True):
            alertas.append(f"🚫 DESACTIVAR: {k} — IC={ic_total:+.3f} n={d['n']} (sigue activa)")

# Bankroll
pnl = sum(float(r['pnl_neto']) for r in rows)
if 20 + pnl < 8:
    alertas.append(f"💀 BANKROLL CRÍTICO: {20+pnl:.2f}€ — revisar circuit breakers")

if alertas:
    print("=== ⚡ ALERTAS ===")
    for a in alertas: print(f"  {a}")
else:
    print("  ✅ Sin anomalías detectadas")
EOF
```

## Step 1 — Estado del sistema

```bash
cat data/shadow/estado_actual.md
```

## Step 2 — IC por subtipo (solo estrategias relevantes, ordenado por PNL)

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict
rows = list(csv.DictReader(open('data/shadow/results.csv')))
pnl = sum(float(r['pnl_neto']) for r in rows)
wins = sum(int(r['acierto']) for r in rows)
n = len(rows)
print(f"TOTAL: {n} ops | {wins}W/{n-wins}L ({wins/n*100:.1f}%) | PNL={pnl:+.2f}€ | Bankroll={20+pnl:.2f}€")
print()
by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0,'rows':[]})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto']); by_sub[k]['rows'].append(r)
for k,d in sorted(by_sub.items(), key=lambda x: x[1]['pnl'], reverse=True):
    if d['n'] < 5: continue
    ic=((d['win']+1)/(d['n']+2)-0.5)*min(1.0,d['n']/20)
    r20 = d['rows'][-20:]; w20=sum(int(r['acierto']) for r in r20)
    ic20=((w20+1)/(len(r20)+2)-0.5)*min(1.0,len(r20)/20)
    flag = ""
    if ic >= 0.10 and d['n'] >= 40: flag = " 🔥LIVE"
    elif ic >= 0.08 and d['n'] >= 40: flag = " ✅CAND"
    elif ic < -0.10 and d['n'] >= 15: flag = " 🚫MALA"
    elif abs(ic20 - ic) > 0.08: flag = f" {'📈' if ic20>ic else '📉'}TREND"
    print(f"  {k:38s} {d['win']}/{d['n']:3d} ({d['win']/d['n']*100:.0f}%)  PNL={d['pnl']:+6.2f}  IC={ic:+.3f}  ult20={ic20:+.3f}{flag}")
EOF
```

## Step 3 — Split BUY_YES vs BUY_NO por ventana

```bash
python3 << 'EOF'
import csv
from collections import defaultdict
rows = list(csv.DictReader(open('data/shadow/results.csv')))
def ic(w,n): return ((w+1)/(n+2)-0.5)*min(1.0,n/20)
print("=== BUY_YES vs BUY_NO (GBM) ===")
for ventana in ['5min','15min','60min']:
    for side in ['BUY_YES','BUY_NO']:
        sub = [r for r in rows if r.get('subtype','').endswith(ventana) and r.get('decision')==side and r['strategy']=='UPDOWN_GBM']
        if sub:
            w=sum(int(r['acierto']) for r in sub); n=len(sub); pnl=sum(float(r['pnl_neto']) for r in sub)
            print(f"  {side:8s} #{ventana:5s}: {w:3d}/{n:3d} ({w/n*100:.0f}%) PNL={pnl:+.2f}€ IC={ic(w,n):+.3f}")
EOF
```

## Step 4 — Estado live trading

```bash
python3 live_guard.py
python3 live_stake.py
```

## Step 5 — Arb y calidad de datos

```bash
cat data/shadow/arb_scan_$(date +%Y-%m-%d).csv 2>/dev/null | head -5 || echo "Sin oportunidades arb hoy"
cat data/shadow/data_quality.json 2>/dev/null | python3 -c "import json,sys; d=json.load(sys.stdin); print(f'Data quality: {d.get(\"overall_score\",\"?\")}')" 2>/dev/null || true
```

## Presentar al usuario

Después de ejecutar todos los pasos, presenta:
1. **Alertas activas** (si las hay) primero — son lo más urgente
2. Bankroll actual y PNL desde última sesión
3. Estrategias que han cruzado umbral live → candidatas
4. Split BUY_YES/BUY_NO y si H-REGIMEN se mantiene
5. Estado switch live (ON/OFF) y ventana horaria
6. Oportunidades arb si las hay
7. Sugiere `/decision` si hay alertas pendientes de acción
