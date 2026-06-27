# Protocolo de inicio de sesión

Ejecuta el protocolo completo de inicio y presenta el resumen al usuario.

## Instructions

Run these steps in sequence and present the results clearly:

**Step 1 — Estado del sistema:**
```bash
cat data/shadow/estado_actual.md
```

**Step 2 — Resultados con IC por subtipo:**
```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict
rows = list(csv.DictReader(open('data/shadow/results.csv')))
pnl = sum(float(r['pnl_neto']) for r in rows)
wins = sum(int(r['acierto']) for r in rows)
n = len(rows)
print(f"{n} ops | {wins}W/{n-wins}L ({wins/n*100:.1f}%) | PNL={pnl:+.2f}€ | Bankroll={20+pnl:.2f}€")
by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto'])
for k,d in sorted(by_sub.items(), key=lambda x: x[1]['pnl'], reverse=True):
    ic=((d['win']+1)/(d['n']+2)-0.5)*min(1.0,d['n']/20)
    print(f"  {k:32s} {d['win']}/{d['n']} ({d['win']/d['n']*100:.0f}%)  PNL={d['pnl']:+.2f}  IC={ic:+.3f}")
EOF
```

**Step 3 — Split BUY_YES vs BUY_NO en #15min (H-REGIMEN):**
```bash
python3 << 'EOF'
import csv
rows = list(csv.DictReader(open('data/shadow/results.csv')))
for side in ['BUY_YES','BUY_NO']:
    sub = [r for r in rows if r.get('subtype','').endswith('15min') and r.get('decision')==side and r['strategy']=='UPDOWN_GBM']
    if sub:
        w=sum(int(r['acierto']) for r in sub); n=len(sub); pnl=sum(float(r['pnl_neto']) for r in sub)
        ic=((w+1)/(n+2)-0.5)*min(1.0,n/20)
        print(f"  {side:8s} #15min: {w}/{n} ({w/n*100:.0f}%) PNL={pnl:+.2f}€ IC={ic:+.3f}")
EOF
```

**Step 4 — Estado live trading:**
```bash
python3 live_guard.py
python3 live_stake.py
```

**Step 5 — Arb scan del día:**
```bash
cat data/shadow/arb_scan_$(date +%Y-%m-%d).csv 2>/dev/null | head -5 || echo "Sin oportunidades hoy"
```

After running all steps, present to the user:
- Bankroll actual (shadow + live si hay) y PNL desde última sesión
- Estrategias que han cruzado IC≥0.10 n≥40 → candidatas a live (umbral activo: IC≥0.08 para 60min)
- Split BUY_YES/BUY_NO en #15min y si H-REGIMEN se mantiene
- Estado del switch live (ON/OFF) y ventana horaria actual
- Oportunidades de arb si las hay
- Cualquier anomalía detectada (bankroll bajo, IC cayendo, etc.)
