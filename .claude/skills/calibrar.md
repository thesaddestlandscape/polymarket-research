---
name: calibrar
description: Revisión de parámetros actuales contra datos acumulados. Comprueba si ORDER_FLOW_BLACKLIST_HOURS, DELTA_MIN/MAX, drift thresholds y otros parámetros clave siguen siendo óptimos. Usar cuando el usuario quiere revisar si hay parámetros que ajustar, o después de acumular n≥50 nuevas ops. Triggers: "calibrar", "revisar parámetros", "son óptimos los umbrales", "ajustar thresholds", "revisar blacklist".
---

# Calibración de parámetros

Compara los parámetros actuales con los datos acumulados. Detecta si algún umbral ha quedado subóptimo.

## Paso 1 — Blacklist horaria ORDER_FLOW (¿siguen siendo las horas correctas?)

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)

# Parámetros actuales en shadow_predict.py
BLACKLIST_ACTUAL = {2, 7, 9, 10, 11, 22}
PAIR_BLACKLIST = {'ETH', 'BNB', 'XRP', 'DOGE'}

# ORDER_FLOW solo BTC+SOL (pares activos)
of_rows = [r for r in rows if r['strategy']=='ORDER_FLOW_5M']
of_activos = [r for r in of_rows if not any(p in r.get('subtype','').upper() for p in PAIR_BLACKLIST)]

by_hour = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in of_activos:
    h = r.get('prediction_timestamp','')[11:13]
    if h: by_hour[h]['n']+=1; by_hour[h]['win']+=int(r['acierto']); by_hour[h]['pnl']+=float(r['pnl_neto'])

print("=== ORDER_FLOW BLACKLIST_HOURS — calibración ===")
print(f"Blacklist actual: {sorted(BLACKLIST_ACTUAL)}")
print()
cambios_sugeridos = []
for h in sorted(by_hour.keys(), key=lambda x: int(x)):
    d = by_hour[h]
    if d['n'] < 3: continue
    ic_v = ic(d['win'], d['n'])
    h_int = int(h)
    en_bl = h_int in BLACKLIST_ACTUAL
    estado_actual = "🚫 BL" if en_bl else "✅ OK"
    accion = ""
    if d['n'] >= 15:
        if en_bl and ic_v > 0.05:
            accion = f"  ← REVISAR: IC={ic_v:+.3f} positivo → considerar DESBLOQUEAR"
            cambios_sugeridos.append(f"DESBLOQUEAR hora {h}h (IC={ic_v:+.3f} n={d['n']})")
        elif not en_bl and ic_v < -0.08:
            accion = f"  ← REVISAR: IC={ic_v:+.3f} negativo → considerar BLOQUEAR"
            cambios_sugeridos.append(f"BLOQUEAR hora {h}h (IC={ic_v:+.3f} n={d['n']})")
    conf = "*" if d['n'] >= 20 else "?" if d['n'] >= 10 else "~"
    print(f"  {h}h UTC {estado_actual}: {d['win']}/{d['n']} ({d['win']/d['n']*100:.0f}%) IC={ic_v:+.3f} PNL={d['pnl']:+.2f}€ [{conf}]{accion}")

print()
if cambios_sugeridos:
    print("CAMBIOS SUGERIDOS:")
    for c in cambios_sugeridos: print(f"  • {c}")
else:
    print("✅ Blacklist horaria sigue siendo óptima")
EOF
```

## Paso 2 — DELTA_MIN/MAX en ORDER_FLOW (¿sigue siendo 0.38-0.46 el sweet spot?)

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)

DELTA_MIN_ACTUAL = 0.38
DELTA_MAX_ACTUAL = 0.46

of_rows = [r for r in rows if r['strategy']=='ORDER_FLOW_5M']
n_con_feat = 0
buckets = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})

for r in of_rows:
    try:
        f = json.loads(r.get('features','{}') or '{}')
        delta = f.get('delta_ratio')
        if delta is None: continue
        n_con_feat += 1
        delta = abs(float(delta))
        bucket = round(delta * 20) / 20  # buckets de 0.05
        buckets[bucket]['n']+=1; buckets[bucket]['win']+=int(r['acierto']); buckets[bucket]['pnl']+=float(r['pnl_neto'])
    except: pass

print(f"=== DELTA_RATIO calibración (n con features: {n_con_feat}) ===")
print(f"Config actual: DELTA_MIN={DELTA_MIN_ACTUAL} DELTA_MAX={DELTA_MAX_ACTUAL}")
print()
for b in sorted(buckets.keys()):
    d = buckets[b]
    if d['n'] < 3: continue
    ic_v = ic(d['win'], d['n'])
    en_rango = DELTA_MIN_ACTUAL <= b < DELTA_MAX_ACTUAL
    estado = "✅ EN RANGO" if en_rango else "⬛ EXCLUIDO"
    bar = "█" * max(0, int(abs(ic_v)*20))
    sign = "+" if ic_v > 0 else "-"
    print(f"  [{b:.2f}-{b+0.05:.2f}) {estado}: n={d['n']:3d} IC={ic_v:+.3f} PNL={d['pnl']:+.2f}€ {sign}{bar}")

# Sugerir ajuste si hay buckets claramente mejores fuera del rango
all_ic = {b: ic(buckets[b]['win'], buckets[b]['n']) for b in buckets if buckets[b]['n'] >= 8}
if all_ic:
    mejor = max(all_ic, key=all_ic.get)
    if all_ic[mejor] > 0.10 and not (DELTA_MIN_ACTUAL <= mejor < DELTA_MAX_ACTUAL):
        print(f"\n  ⚠️ SUGERENCIA: bucket [{mejor:.2f}-{mejor+0.05:.2f}) IC={all_ic[mejor]:+.3f} está FUERA del rango actual")
    elif all_ic.get(DELTA_MIN_ACTUAL, 0) < -0.05:
        print(f"\n  ⚠️ SUGERENCIA: DELTA_MIN podría subir — el bucket [{DELTA_MIN_ACTUAL:.2f}-] está siendo negativo")
EOF
```

## Paso 3 — Drift thresholds GBM (BTC#15min drift≥0.3 y BUY_YES drift_60min [0, 0.5%))

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

rows = list(csv.DictReader(open('data/shadow/results.csv')))
def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)

# BTC#15min drift_15min threshold (actual: ≥0.3)
DRIFT15_THRESHOLD_BTC = 0.3
btc15 = [r for r in rows if 'BTC' in r.get('subtype','') and r.get('subtype','').endswith('15min') and r['strategy']=='UPDOWN_GBM']
buckets = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in btc15:
    try:
        f = json.loads(r.get('features','{}') or '{}')
        drift = f.get('drift_15min')
        if drift is None: continue
        drift_pct = float(drift)*100
        b = round(drift_pct * 2) / 2  # buckets de 0.5%
        buckets[b]['n']+=1; buckets[b]['win']+=int(r['acierto']); buckets[b]['pnl']+=float(r['pnl_neto'])
    except: pass

print(f"=== BTC#15min drift_15min calibración (threshold actual: ≥{DRIFT15_THRESHOLD_BTC}%/h) ===")
n_activo = sum(d['n'] for b, d in buckets.items() if b >= DRIFT15_THRESHOLD_BTC and d['n']>0)
n_filtrado = sum(d['n'] for b, d in buckets.items() if b < DRIFT15_THRESHOLD_BTC and d['n']>0)
print(f"  n activo (drift≥{DRIFT15_THRESHOLD_BTC}): {n_activo} | n filtrado: {n_filtrado}")
for b in sorted(buckets.keys()):
    d = buckets[b]
    if d['n'] < 3: continue
    ic_v = ic(d['win'], d['n'])
    en_rango = b >= DRIFT15_THRESHOLD_BTC
    estado = "✅" if en_rango else "⬛"
    print(f"  drift [{b:+.1f}%): {estado} n={d['n']:3d} IC={ic_v:+.3f} PNL={d['pnl']:+.2f}€")

# BUY_YES 15min drift_60min threshold (actual: [0, 0.5%))
print()
print(f"=== BUY_YES#15min drift_60min calibración (threshold actual: [0, 0.5%)) ===")
yes15 = [r for r in rows if r.get('subtype','').endswith('15min') and r.get('decision')=='BUY_YES' and r['strategy']=='UPDOWN_GBM']
buckets2 = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in yes15:
    try:
        f = json.loads(r.get('features','{}') or '{}')
        drift = f.get('drift_60min')
        if drift is None: continue
        drift_pct = float(drift)*100
        b = round(drift_pct * 4) / 4  # buckets de 0.25%
        buckets2[b]['n']+=1; buckets2[b]['win']+=int(r['acierto']); buckets2[b]['pnl']+=float(r['pnl_neto'])
    except: pass
for b in sorted(buckets2.keys()):
    d = buckets2[b]
    if d['n'] < 3: continue
    ic_v = ic(d['win'], d['n'])
    en_rango = 0.0 <= b < 0.5
    estado = "✅" if en_rango else "⬛"
    print(f"  drift60 [{b:+.2f}%): {estado} n={d['n']:3d} IC={ic_v:+.3f} PNL={d['pnl']:+.2f}€")
EOF
```

## Paso 4 — Resumen de parámetros actuales vs sugeridos

```bash
python3 << 'EOF'
import json
try:
    p = json.load(open('data/shadow/strategy_params.json'))
    print("=== strategy_params.json — estrategias activas ===")
    for k, v in sorted(p.items()):
        if isinstance(v, dict) and v.get('activa', True):
            ic_k = v.get('ic_efectivo', v.get('apuesta_kelly', '?'))
            n_k = v.get('n_total', '?')
            print(f"  {k}: activa=True n={n_k} IC={ic_k}")
except Exception as e:
    print(f"Error: {e}")
EOF
```

## Presentar al usuario

1. **Blacklist horaria**: ¿hay horas que desbloquear o bloquear?
2. **DELTA_MIN/MAX**: ¿el sweet spot 0.38-0.46 sigue siendo óptimo?
3. **Drift thresholds**: ¿los umbrales de BTC#15min y BUY_YES#15min siguen calibrados?
4. Para cada cambio sugerido: mostrar el código exacto a modificar en `shadow_predict.py`
5. Si los parámetros están bien: confirmar que no hay nada que tocar
