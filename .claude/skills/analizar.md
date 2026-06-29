---
name: analizar
description: Análisis profundo de features para una estrategia específica. Encuentra patrones ocultos en los datos, sugiere umbrales óptimos, y compara con los filtros actuales. Usar cuando el usuario quiere entender por qué una estrategia funciona/falla, qué filtros añadir, o qué umbrales ajustar. Argumentos: nombre de estrategia (ej: "BTC#15min", "ORDER_FLOW", "ETH#60min", "BUY_NO"). Triggers: "analizar X", "por qué falla X", "features de X", "qué filtro añadir a X", "buckets de X".
---

# Análisis profundo de features

Extrae patrones de features → IC por bucket → sugiere umbrales concretos.

El usuario ha especificado una estrategia o subtipo. Si no lo especificó, pregunta cuál analizar.

## Paso 1 — Análisis de features por bucket

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

ESTRATEGIA = "REEMPLAZAR_CON_ARGUMENTO"  # Claude: reemplaza con el argumento del usuario

rows = list(csv.DictReader(open('data/shadow/results.csv')))
params = json.load(open('data/shadow/strategy_params.json'))

def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)

# Filtrar por estrategia/subtipo
def match(r, query):
    key = (r['strategy'] + '#' + r.get('subtype','')).upper()
    return all(q.upper() in key for q in query.replace('#',' ').split())

sub = [r for r in rows if match(r, ESTRATEGIA)]
if not sub:
    print(f"Sin datos para: {ESTRATEGIA}")
    print("Estrategias disponibles:")
    keys = set(r['strategy']+'#'+r.get('subtype','') for r in rows)
    for k in sorted(keys)[:20]: print(f"  {k}")
    exit()

n_total = len(sub)
wins_total = sum(int(r['acierto']) for r in sub)
pnl_total = sum(float(r['pnl_neto']) for r in sub)
print(f"=== ANÁLISIS: {ESTRATEGIA} ===")
print(f"Total: n={n_total} wins={wins_total} ({wins_total/n_total*100:.0f}%) PNL={pnl_total:+.2f}€ IC={ic(wins_total,n_total):+.3f}")

# Extraer features numéricas
feats = defaultdict(list)
n_con_features = 0
for r in sub:
    try:
        f = json.loads(r.get('features','{}') or '{}')
        if f: n_con_features += 1
        for k, v in f.items():
            if isinstance(v, (int, float)) and v is not None:
                feats[k].append((float(v), int(r['acierto']), float(r['pnl_neto'])))
    except: pass

print(f"Ops con features: {n_con_features}/{n_total}")

if not feats:
    print("\nSin features disponibles. Las features se registran desde la predicción — revisar predictions CSV.")
    exit()

# Análisis por feature
print()
for feat_name in sorted(feats.keys()):
    data = feats[feat_name]
    if len(data) < 8: continue
    vals = [v for v, _, _ in data]
    lo, hi = min(vals), max(vals)
    if lo == hi: continue

    # 4 buckets por cuartil
    vals_sorted = sorted(vals)
    q4 = [vals_sorted[i*len(vals_sorted)//4] for i in range(5)]
    q4[-1] = hi + 1e-9

    print(f"\n  ── {feat_name} (range: [{lo:.5f}, {hi:.5f}]) ──")
    best_ic = -99
    best_bucket = None
    bucket_results = []
    for i in range(4):
        bucket = [(v, a, p) for v, a, p in data if q4[i] <= v < q4[i+1]]
        if not bucket: continue
        n_b = len(bucket); w_b = sum(a for _, a, _ in bucket); pnl_b = sum(p for _, _, p in bucket)
        ic_v = ic(w_b, n_b)
        bucket_results.append((q4[i], q4[i+1], n_b, w_b, pnl_b, ic_v))
        if ic_v > best_ic: best_ic = ic_v; best_bucket = i

    for i, (lo_b, hi_b, n_b, w_b, pnl_b, ic_v) in enumerate(bucket_results):
        bar = "█" * max(0, int(abs(ic_v) * 20))
        sign = "+" if ic_v > 0 else "-"
        marker = " ← MEJOR" if i == best_bucket and best_ic > 0.05 else ""
        marker += " ← PEOR" if ic_v == min(r[5] for r in bucket_results) and ic_v < -0.05 and i != best_bucket else ""
        print(f"    [{lo_b:+8.4f}, {hi_b:+8.4f}): n={n_b:3d} {w_b}/{n_b} ({w_b/n_b*100:.0f}%) PNL={pnl_b:+5.2f} IC={ic_v:+.3f} {sign}{bar}{marker}")

    # Sugerencia de filtro
    if best_ic > 0.08 and best_bucket is not None:
        lo_b, hi_b = bucket_results[best_bucket][0], bucket_results[best_bucket][1]
        print(f"    → Sugerencia: filtrar a {feat_name} ∈ [{lo_b:.4f}, {hi_b:.4f}) — IC esperado ≥ {best_ic:+.3f}")

# Comparar con filtros actuales en strategy_params
print("\n=== FILTROS ACTUALES EN strategy_params.json ===")
for k, p in params.items():
    if ESTRATEGIA.upper() in k.upper():
        filtros = p.get('filtros_causales', [])
        patrones = p.get('patrones_ganadores', [])
        activa = p.get('activa', True)
        print(f"  {k}: activa={activa}, filtros={len(filtros)}, patrones={len(patrones)}")
        for f in filtros:
            print(f"    FILTRO: {f}")
        for pa in patrones:
            print(f"    PATRÓN: {pa}")
EOF
```

## Paso 2 — Análisis temporal (tendencia por semana)

```bash
python3 << 'EOF'
import csv, json
from collections import defaultdict

ESTRATEGIA = "REEMPLAZAR_CON_ARGUMENTO"

rows = list(csv.DictReader(open('data/shadow/results.csv')))
def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)
def match(r, q):
    key = (r['strategy']+'#'+r.get('subtype','')).upper()
    return all(x.upper() in key for x in q.replace('#',' ').split())

sub = [r for r in rows if match(r, ESTRATEGIA)]
if not sub: exit()

# Agrupar por día
by_day = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in sub:
    d = r.get('prediction_timestamp','')[:10] or r.get('resolution_timestamp','')[:10]
    if d:
        by_day[d]['n']+=1; by_day[d]['win']+=int(r['acierto']); by_day[d]['pnl']+=float(r['pnl_neto'])

print(f"\n=== TENDENCIA DIARIA: {ESTRATEGIA} ===")
running_w, running_n = 0, 0
for d in sorted(by_day.keys())[-14:]:  # últimas 2 semanas
    dd = by_day[d]
    running_w += dd['win']; running_n += dd['n']
    ic_day = ic(dd['win'], dd['n'])
    ic_cum = ic(running_w, running_n)
    print(f"  {d}: {dd['win']}/{dd['n']} ({dd['win']/dd['n']*100:.0f}%) PNL={dd['pnl']:+.2f} IC_día={ic_day:+.3f} IC_acum={ic_cum:+.3f}")
EOF
```

## Presentar al usuario

1. **Tabla de buckets** para cada feature — qué rangos son rentables vs destructivos
2. **Sugerencias de filtro** concretas con el threshold exacto
3. **Comparar** con filtros ya activos en strategy_params.json — ¿están bien calibrados?
4. **Tendencia temporal** — ¿está mejorando o empeorando?
5. Si hay una sugerencia clara: proponer implementarla directamente
