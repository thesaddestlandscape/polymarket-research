---
name: decision
description: Capa de decisión del sistema de aprendizaje continuo. Analiza el estado actual y genera un plan de acción priorizado con los cambios exactos a hacer. Usar cuando el usuario quiere saber "qué toca hacer", "qué implementar ahora", "qué hipótesis está lista", "próximos pasos concretos", o después de ver el resumen de inicio. Triggers: "decisión", "decision", "qué hago", "próximos pasos", "qué implementar", "qué cambiar".
---

# Sistema de decisión — aprendizaje continuo

Analiza toda la evidencia acumulada y genera un plan de acción priorizado con cambios específicos.

## Paso 1 — Análisis de decisión automático

```bash
python3 << 'EOF'
import csv, json, os
from collections import defaultdict
from datetime import datetime

rows = list(csv.DictReader(open('data/shadow/results.csv')))
_raw = json.load(open('data/shadow/strategy_params.json'))
params = _raw.get('estrategias', _raw)  # soporta estructura plana y anidada

def ic(w, n): return ((w+1)/(n+2)-0.5)*min(1.0, n/20)
def ic_trend(rows_list, last_n=20):
    if len(rows_list) < last_n: return None
    r = rows_list[-last_n:]; w = sum(int(x['acierto']) for x in r)
    return ic(w, last_n)

by_sub = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0,'rows':[]})
for r in rows:
    k = r['strategy']+('#'+r['subtype'] if r.get('subtype') else '')
    by_sub[k]['n']+=1; by_sub[k]['win']+=int(r['acierto']); by_sub[k]['pnl']+=float(r['pnl_neto']); by_sub[k]['rows'].append(r)

acciones_ahora = []
acciones_pronto = []
monitorear = []

# ── REGLA 1: Live ready (IC≥0.10 n≥40) ──────────────────────────────
for k, d in by_sub.items():
    ic_v = ic(d['win'], d['n'])
    if ic_v >= 0.10 and d['n'] >= 40:
        p = params.get(k, {})
        if p.get('activa', True):
            ic_rec = ic_trend(d['rows']) or ic_v
            acciones_ahora.append({
                'titulo': f"🔥 LIVE READY: {k}",
                'evidencia': f"IC={ic_v:+.3f} n={d['n']} | tendencia ult20: IC={ic_rec:+.3f}",
                'accion': "Esperar credenciales Polymarket. Estrategia lista en config_live.json.",
                'impacto': d['pnl']
            })

# ── REGLA 2: Candidata 60min (IC≥0.08 n≥40) ─────────────────────────
for k, d in by_sub.items():
    if '60min' not in k: continue
    ic_v = ic(d['win'], d['n'])
    if ic_v >= 0.08 and d['n'] >= 40:
        p = params.get(k, {})
        if p.get('activa', True):
            acciones_ahora.append({
                'titulo': f"✅ 60MIN CANDIDATA: {k}",
                'evidencia': f"IC={ic_v:+.3f} n={d['n']}",
                'accion': "Primera candidata para live con GBM. Preparar cuando lleguen credenciales.",
                'impacto': d['pnl']
            })

# ── REGLA 3: Desactivar estrategia activa con IC muy negativo ─────────
for k, d in by_sub.items():
    if d['n'] < 15: continue
    ic_v = ic(d['win'], d['n'])
    p = params.get(k, {})
    if p.get('activa', True) and ic_v < -0.10:
        ic_rec = ic_trend(d['rows']) or ic_v
        # Solo bloquear si la tendencia reciente también es negativa
        if ic_rec < -0.05:
            acciones_ahora.append({
                'titulo': f"🚫 DESACTIVAR: {k}",
                'evidencia': f"IC={ic_v:+.3f} n={d['n']} | ult20: IC={ic_rec:+.3f}",
                'accion': f"En strategy_params.json → {json.dumps({k: {'activa': False}})}",
                'impacto': d['pnl']
            })

# ── REGLA 4: Horas con IC negativo en GBM (bloquear) ─────────────────
gbm_rows = [r for r in rows if r['strategy']=='UPDOWN_GBM']
by_h = defaultdict(lambda: {'n':0,'win':0,'pnl':0.0})
for r in gbm_rows:
    h = r.get('prediction_timestamp','')[11:13]
    if h: by_h[h]['n']+=1; by_h[h]['win']+=int(r['acierto']); by_h[h]['pnl']+=float(r['pnl_neto'])
BLOQUEADAS_GBM = set()  # Añadir horas ya bloqueadas aquí si existe config
for h, d in sorted(by_h.items()):
    if d['n'] < 5: continue
    ic_v = ic(d['win'], d['n'])
    h_int = int(h)
    if d['n'] >= 15 and ic_v < -0.08 and h_int not in BLOQUEADAS_GBM:
        acciones_ahora.append({
            'titulo': f"🚫 BLOQUEAR GBM hora {h}h UTC",
            'evidencia': f"IC={ic_v:+.3f} n={d['n']} PNL={d['pnl']:+.2f}€",
            'accion': f"En shadow_predict.py: añadir {h} a GBM_BLACKLIST_HOURS (o usar meta_params)",
            'impacto': d['pnl']
        })
    elif d['n'] < 15 and ic_v < -0.05:
        monitorear.append(f"GBM {h}h UTC: IC={ic_v:+.3f} n={d['n']} (esperar n≥15)")

# ── REGLA 5: Hipótesis custom que han cruzado umbral ──────────────────
try:
    custom = json.load(open('data/shadow/hipotesis_custom.json'))
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
        n_h = len(sub)
        if n_h == 0: continue
        wins_h = sum(int(r['acierto']) for r in sub)
        ic_v = ic(wins_h, n_h)
        umbral_n = h.get('umbral_n', 20)
        ic_min = h.get('umbral_ic_min')
        ic_max = h.get('umbral_ic_max')
        pnl_h = sum(float(r['pnl_neto']) for r in sub)
        if n_h >= umbral_n:
            if ic_min and ic_v >= ic_min:
                acciones_ahora.append({
                    'titulo': f"✅ HIPÓTESIS POSITIVA: {h['id']}",
                    'evidencia': f"{h['nombre']} — IC={ic_v:+.3f} n={n_h} (umbral IC≥{ic_min})",
                    'accion': h.get('accion', 'Ver hipotesis_custom.json'),
                    'impacto': pnl_h
                })
            elif ic_max and ic_v <= ic_max:
                acciones_ahora.append({
                    'titulo': f"🚫 HIPÓTESIS NEGATIVA: {h['id']}",
                    'evidencia': f"{h['nombre']} — IC={ic_v:+.3f} n={n_h} (umbral IC<{ic_max})",
                    'accion': h.get('accion', 'Ver hipotesis_custom.json'),
                    'impacto': pnl_h
                })
        else:
            ops_falta = umbral_n - n_h
            if ic_v > 0.03 and ops_falta <= 25:
                accionable = ic_min and ic_v >= ic_min*0.7
                nivel = '⏳ PRONTO' if accionable else '👁 WATCH'
                (acciones_pronto if accionable else monitorear).append(
                    f"{h['id']}: IC={ic_v:+.3f} n={n_h} — {ops_falta} ops para umbral n≥{umbral_n}")
except Exception as e:
    print(f"  [hipotesis_custom.json: {e}]")

# ── REGLA 6: Estrategias cerca del umbral live ────────────────────────
for k, d in by_sub.items():
    if d['n'] < 15: continue
    ic_v = ic(d['win'], d['n'])
    if ic_v >= 0.06 and d['n'] < 40:
        ops_falta = 40 - d['n']
        # Días estimados (ciclo 60min → ~6 ops/día en ventanas activas)
        eta_dias = ops_falta // 6 + 1
        acciones_pronto.append(f"{k}: IC={ic_v:+.3f} n={d['n']} — {ops_falta} ops (ETA ~{eta_dias}d)")

# ── OUTPUT ────────────────────────────────────────────────────────────
print(f"\n=== 🔥 ACCIONES AHORA ({len(acciones_ahora)}) ===")
for a in sorted(acciones_ahora, key=lambda x: abs(x.get('impacto',0)), reverse=True):
    print(f"\n  [{a['titulo']}]")
    print(f"    Evidencia : {a['evidencia']}")
    print(f"    Acción    : {a['accion']}")

if not acciones_ahora:
    print("  (ninguna — todo en orden)")

print(f"\n=== ⏳ PRONTO ({len(acciones_pronto)}) ===")
for a in sorted(set(acciones_pronto))[:8]:
    print(f"  {a}")

print(f"\n=== 👁 MONITOREAR ===")
for a in sorted(set(monitorear))[:6]:
    print(f"  {a}")

# Resumen PNL acciones identificadas
print(f"\n=== 💡 RESUMEN ===")
pnl_total = sum(float(r['pnl_neto']) for r in rows)
print(f"  Bankroll: {20+pnl_total:.2f}€ | PNL total: {pnl_total:+.2f}€")
print(f"  Acciones identificadas: {len(acciones_ahora)} ahora, {len(acciones_pronto)} pronto")
EOF
```

## Paso 2 — Verificar hipotesis_auto.md para señales adicionales del tracker

```bash
head -40 data/shadow/hipotesis_auto.md 2>/dev/null || echo "hipotesis_auto.md no disponible"
```

## Presentar al usuario

1. **Ejecuta ambos pasos** y sintetiza las acciones en un plan claro
2. Para cada acción AHORA: muestra el cambio concreto (código o config) y pregunta si implementar
3. Para acciones PRONTO: muestra ETA y qué observar
4. Termina con la pregunta: "¿Implementamos algo de esto ahora?"

## Implementación directa

Si el usuario confirma una acción:
- **Desactivar estrategia**: edita `data/shadow/strategy_params.json` directamente
- **Bloquear hora GBM**: edita `shadow_predict.py` para añadir la hora al set de blacklist
- **Activar hipótesis**: edita `shadow_predict.py` con el filtro o boost correspondiente
- Después de cualquier cambio en `shadow_predict.py`: verificar que el bot lo leerá en el próximo ciclo (es stateless, no hace falta reiniciar)
