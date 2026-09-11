---
name: hipotesis
description: Estado actualizado de todas las hipótesis activas con datos reales, veredicto y próxima acción para cada una. Triggers: "hipótesis", "hipotesis", "estado hipótesis", "qué hipótesis están validadas", "ver hipótesis", "H-REGIMEN", "H-60MIN".
---

# Estado de hipótesis activas

## Paso 1 — Hipótesis builtin principales

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
_raw = json.load(open('data/shadow/strategy_params.json'))
params = _raw.get('estrategias', _raw)
def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)

by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto'])

def sub_ic(filtro_strategy=None, filtro_subtype=None, filtro_decision=None):
    sub = rows
    if filtro_strategy: sub = [r for r in sub if r['strategy']==filtro_strategy]
    if filtro_subtype: sub = [r for r in sub if filtro_subtype in r.get('subtype','')]
    if filtro_decision: sub = [r for r in sub if r.get('decision')==filtro_decision]
    if not sub: return 0, 0, 0.0
    w=sum(int(r['acierto']) for r in sub); n=len(sub); pnl=sum(float(r['pnl_neto']) for r in sub)
    return w, n, pnl

# H-REGIMEN
print("=== H-REGIMEN (BUY_YES vs BUY_NO en #15min) ===")
print("  Veredicto: ❌ REFUTADA en 15min | ✅ APLICADA en 60min+ (REGIME_BUY_NO_THRESHOLD=0.7%/h)")
for side in ['BUY_YES','BUY_NO']:
    w,n,pnl = sub_ic('UPDOWN_GBM','15min',side)
    if n: print(f"  {side}: {w}/{n} ({w/n*100:.0f}%) IC={ic(w,n):+.3f} PNL={pnl:+.2f}€")
print("  → Acción: ninguna pendiente. Monitorear que BUY_NO#15min mantiene IC>BUY_YES.")

# H-60MIN
print()
print("=== H-60MIN (GBM ventanas largas) — umbral live IC≥0.08 n≥40 ===")
print("  Veredicto: ✅ CONFIRMADA por backfill 90d — acumulando shadow")
for par in ['BTC','ETH','SOL']:
    k = f"UPDOWN_GBM#{par}#60min"
    d = by_sub.get(k,{'n':0,'win':0,'pnl':0.0})
    if d['n'] > 0:
        ic_v = ic(d['win'], d['n']); ops_f = max(0,40-d['n'])
        eta = f"ETA {ops_f//6+1}d" if ops_f>0 else "✅ n≥40"
        umbral = "✅ IC OK" if ic_v>=0.08 else f"⚠️ IC bajo (falta {0.08-ic_v:.3f})"
        print(f"  {par}#60min: {d['win']}/{d['n']} IC={ic_v:+.3f} PNL={d['pnl']:+.2f}€  {eta}  {umbral}")

# H-ORDER_FLOW-DECAY
print()
print("=== H-ORDER_FLOW-DECAY (DELTA_MAX=0.46, solo BUY_NO) ===")
print("  Veredicto: ✅ RESUELTA — zona muerta [0.46-0.65] eliminada")
for par in ['BTC','SOL']:
    w,n,pnl = sub_ic('ORDER_FLOW_5M', par, 'BUY_NO')
    if n: print(f"  OF {par} BUY_NO: {w}/{n} ({w/n*100:.0f}%) IC={ic(w,n):+.3f} PNL={pnl:+.2f}€")
print("  → Acción: ninguna. Monitorear DELTA_MIN si IC cae — usar /calibrar")

# H-VENTANAS-HORARIAS
print()
print("=== H-VENTANAS-HORARIAS (ORDER_FLOW blacklist {2,7,9,10,11,22} UTC) ===")
print("  Veredicto: ✅ APLICADA — mejora retroactiva +31.30€")
print("  → Acción: usar /calibrar para verificar si alguna hora debe ajustarse")

# H-DRIFT60-BUY_YES_15MIN
print()
print("=== H-DRIFT60-BUY_YES_15MIN (filtro drift_60 ∈ [0, 0.5%)) ===")
print("  Veredicto: ✅ IMPLEMENTADA 2026-06-26 — forward validando")
w,n,pnl = sub_ic('UPDOWN_GBM','15min','BUY_YES')
if n:
    ic_v=ic(w,n)
    estado = "✅ IC bueno" if ic_v>0.08 else "⚠️ IC bajo" if ic_v<0 else "⏳ acumulando"
    print(f"  BUY_YES#15min forward: {w}/{n} ({w/n*100:.0f}%) IC={ic_v:+.3f} PNL={pnl:+.2f}€  {estado}")
    if n >= 40: print("  → Con n≥40: usar /analizar BUY_YES#15min para revisar si umbral 0.5% sigue óptimo")
    else: print(f"  → Esperar n≥40 ({40-n} ops más) para revisar umbral")

# H-DRIFT15-MOMENTUM
print()
print("=== H-DRIFT15-MOMENTUM (BTC#15min filtro drift_15≥0.3%/h) ===")
print("  Veredicto: ✅ IMPLEMENTADA 2026-06-27 — zona muerta [-1,+0.3] eliminada")
w,n,pnl = sub_ic('UPDOWN_GBM','BTC#15min',None)
if n: print(f"  BTC#15min global: {w}/{n} IC={ic(w,n):+.3f} PNL={pnl:+.2f}€")
print("  → Revisable con n≥60 en BTC#15min con feature registrada")

# H-WEEKLY-PRICE
print()
print("=== H-WEEKLY-PRICE (mercados semanales) — acumulando (n=21+) ===")
print("  Veredicto: ⏳ SIN ACCIÓN — SOL 4/4 (100%) pero n muy pequeño, BTC negativo")
for par in ['BTC','ETH','SOL']:
    for k_suf in ['#weekly','#7day','#weekly_close']:
        k = f"UPDOWN_GBM#{par}{k_suf}"
        d = by_sub.get(k, {'n':0,'win':0,'pnl':0.0})
        if d['n'] > 0:
            print(f"  {par}: {d['win']}/{d['n']} IC={ic(d['win'],d['n']):+.3f} PNL={d['pnl']:+.2f}€")
print("  → Esperar n≥15 por par antes de tomar decisiones")
EOF
```

## Paso 2 — Hipótesis custom activas (desde hipotesis_custom.json)

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)

try:
    custom = json.load(open('data/shadow/hipotesis_custom.json'))
except:
    print("hipotesis_custom.json no encontrado"); exit()

print("=== HIPÓTESIS CUSTOM ===")
for h in custom.get('hipotesis', []):
    filtro = h.get('filtro', {})
    sub = rows
    if filtro.get('strategy_prefix'):
        sub = [r for r in sub if r['strategy'].startswith(filtro['strategy_prefix'])]
    if filtro.get('subtype_contains'):
        sub = [r for r in sub if filtro['subtype_contains'] in r.get('subtype','')]
    if filtro.get('decision'):
        sub = [r for r in sub if r.get('decision')==filtro['decision']]
    if filtro.get('par'):
        par = filtro['par']
        sub = [r for r in sub if par in r.get('subtype','').upper().split('#')]
    if filtro.get('hora_utc') is not None:
        h_val = str(filtro['hora_utc']).zfill(2)
        sub = [r for r in sub if r.get('prediction_timestamp','')[11:13]==h_val]

    n = len(sub)
    w = sum(int(r['acierto']) for r in sub) if sub else 0
    pnl = sum(float(r['pnl_neto']) for r in sub) if sub else 0.0
    ic_v = ic(w, n) if n > 0 else 0.0
    umbral_n = h.get('umbral_n', 20)
    ops_falta = max(0, umbral_n - n)
    ic_min = h.get('umbral_ic_min')
    ic_max = h.get('umbral_ic_max')

    if n == 0:
        estado = "⏸ Sin datos"
    elif ops_falta > 0:
        estado = f"⏳ {ops_falta} ops para n≥{umbral_n}"
    elif ic_min and ic_v >= ic_min:
        estado = f"✅ CONFIRMADA (IC≥{ic_min})"
    elif ic_max and ic_v <= ic_max:
        estado = f"✅ CONFIRMADA (IC<{ic_max})"
    elif ic_min and ic_v < ic_min:
        estado = f"⏳ IC aún bajo (necesita ≥{ic_min})"
    else:
        estado = "⏳ acumulando"

    accion = h.get('accion', '')
    print(f"\n  [{h['id']}] {estado}")
    print(f"    n={n} IC={ic_v:+.3f} PNL={pnl:+.2f}€  |  {h['nombre']}")
    if ops_falta == 0 and 'CONFIRMADA' in estado:
        print(f"    → ACCIÓN: {accion}")
EOF
```

## Presentar al usuario

1. Para cada hipótesis: veredicto claro (confirmada/refutada/acumulando) + próxima acción concreta
2. Hipótesis custom que han cruzado umbral: proponer implementación
3. ETA para las que están cerca del umbral
4. Sugerir `/decision` para plan de acción completo, o `/analizar` para hipótesis con n≥30 que merecen análisis de features
