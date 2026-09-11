# Recap sesión — 2026-06-24 tarde (~15:30 UTC)

## Estado al inicio

- Bankroll real: **16.06€** (PNL total -3.94€ sobre 232 ops)
- `estado_actual.md` reportaba 13.12€ — discrepancia porque `shadow_resumen.py` no contabiliza ORDER_FLOW_5M. Bug conocido, pendiente de fix.
- BTC había bajado **-3.12%** en el día (62,669 → 60,713)

---

## Análisis realizado

### 1. Hallazgo principal: BUY_NO gana sistemáticamente, BUY_YES pierde

| Estrategia | BUY_YES | BUY_NO |
|---|---|---|
| UPDOWN_GBM #15min | 10/22 — 45% — **-2.16€** | **11/11 — 100% — +10.18€** |
| ORDER_FLOW_5M | 11/33 — 33% — **-10.69€** | **59/92 — 64% — +22.53€** |

Mismo patrón en todos los assets #15min (BTC, ETH, SOL, XRP, BNB).

### 2. ¿Es una señal real o racha?

Investigamos si el 11/11 BUY_NO era fiable o simple racha. Resultado: **todo en un solo día**, concentrado hoy.

Outcomes reales del día:
- #15min: YES=30%, NO=**70%**
- #5min: YES=40%, NO=**60%**
- ORDER_FLOW: YES=35%, NO=**65%**

Conclusión: **no es edge del modelo, es sesgo bajista del día**. BTC -3.12% hoy. El modelo no era mejor — simplemente el mercado bajó casi siempre.

### 3. Por qué el GBM se equivocaba en BUY_YES

El GBM usaba `drift=0`. Lógica interna:

```
Spot subió 0.1% dentro del slot → GBM ve momentum → BUY_YES (prob=0.70)
Realidad: ese rebote ocurre dentro de una tendencia bajista de horas
→ Outcome = NO → LOSS
```

El modelo miraba el micro-movimiento dentro de 15min pero era **ciego al contexto macro**:
- `drift_60min = -0.82%/h` (BTC bajando sostenidamente)
- `delta_ratio_macro = -0.19` (vendedores dominan en Binance)
- Estas variables estaban disponibles pero no se alimentaban al modelo.

### 4. ORDER_FLOW_5M: evolución temporal

| Bloque | Win% | PNL | IC |
|---|---|---|---|
| #1-31 | 39% | -6.80€ | -0.106 |
| #32-62 | 58% | +4.02€ | +0.076 |
| #63-93 | **71%** | **+11.38€** | **+0.197** ← pico |
| #94-124 | 58% | +4.16€ | +0.076 |

El bloque #63-93 fue el mejor hasta ahora (71%). Los dos últimos bloques están en 58%, que sigue siendo positivo pero debemos vigilar si se mantiene.

### 5. UPDOWN_GBM #15min: estado real

n=33 (vs 23 del CLAUDE.md, han llegado ~10 más hoy). Faltan ~17 ops para n=50 (umbral live).
IC=+0.220 global, pero está dominado por BUY_NO (11/11). Con más días mixtos el IC se estabilizará — lo que importa es si el modelo CON drift se calibra mejor.

### 6. SMART_FLOW_1H: candidata a desactivar

2/13 (15%) — IC=-0.195 — PNL=-7.66€. Supera el umbral de desactivación (-0.30, n=8) del postmortem, pero no se ha desactivado automáticamente. Revisar en próxima sesión.

### 7. H3 BTC#5min: sin datos

La columna `features` estaba vacía en resultados de BTC#5min. No se pudo verificar la hipótesis del momentum opuesto. Ahora con el fix del CSV (ver implementación) se empezará a acumular.

### 8. Arb scan: solo OVERROUNDs

Todos los mercados detectados tienen suma YES > 1.0 (desfavorable). No hay bracket arb con suma < 0.97 hoy.

---

## Qué implementamos

### Commit: `feat: incorporar drift de mercado al modelo GBM`

**shadow_predict.py:**

1. **`_calcular_drift_h(sym, precios_data, n_min)`** — retorno acumulado de las últimas N min desde precios_intraday (datos cada ~60s). Devuelve fracción/hora.

2. **`_calcular_delta_ratio_macro(sym, klines_raw)`** — delta ratio acumulado sobre TODAS las klines Binance disponibles (~25 velas). Señal macro de presión compradora/vendedora.

3. **`DRIFT_DAMPING = 0.25`** — amortiguación para no sobrereaccionar al drift.

4. **`_gbm_p_up(..., mu_h=0.0)`** — fórmula actualizada:
   ```
   d2 = (log(spot/ref) + mu_h × T_h) / (sigma_h × sqrt(T_h))
   ```
   Con drift bajista de hoy (-0.82%/h), `mu_h = -0.82% × 0.25 = -0.205%/h`:
   - Señal marginal BUY_YES (p≈0.55-0.60) → se flipea a BUY_NO o SKIP
   - Señal fuerte BUY_YES (p≈0.87) → baja a p≈0.75 (sigue siendo BUY_YES pero menos confiado)

5. **`s_updown_gbm()`** — calcula `drift_15min`, `drift_60min`, `delta_ratio_macro` y los añade al dict `features` de cada predicción.

**shadow_postmortem.py:**

6. **FEATURE_RULES ampliadas** — para todos los subtipos UPDOWN_GBM (5min y 15min):
   - `drift_60min` (abs_gt/abs_lt) — malo cuando tendencia extrema en cualquier dirección
   - `delta_ratio_macro` (abs_lt/abs_gt) — malo cuando el exchange está muy equilibrado (sin señal)

**shadow_resolve.py + shadow_postmortem.py:**

7. **`_normalizar_pred(row)`** — fix de bug preexistente: el CSV de predicciones tenía header antiguo de 13 columnas. `subtype`, `apuesta` y `features` caían en el key `None` como lista. Ahora se extraen correctamente en ambos scripts.

---

## Estado post-cambios

**features que ahora se guardan en cada predicción UPDOWN_GBM:**
```json
{
  "pct_spot_vs_ref": -0.48,
  "sigma_h": 0.01464,
  "T_h": 0.059,
  "drift_15min": -2.28,
  "drift_60min": -1.46,
  "delta_ratio_macro": -0.29
}
```

**Efecto inmediato:** en mercados con drift fuerte, el modelo ajustará p_up automáticamente. No depende del postmortem para aprender — la corrección entra en la fórmula desde el primer ciclo.

**Efecto a largo plazo:** el postmortem acumulará datos con las nuevas features y aprenderá filtros adicionales (e.g., "cuando |drift_60min| > X% → el modelo sigue fallando, skip").

---

## Números clave al cierre de sesión

| Estrategia | n | Win% | IC | PNL |
|---|---|---|---|---|
| ORDER_FLOW_5M | 124 | 56% | +0.063 | **+12.75€** |
| UPDOWN_GBM#15min global | 33 | 63% | +0.220 | **+9.92€** |
| UPDOWN_GBM#5min (BTC+ETH+SOL) | ~45 | ~33% | ~-0.11 | **-14.81€** |
| SMART_FLOW_1H | 13 | 15% | -0.195 | **-7.66€** |

Bankroll real: **~16€** (el fast loop sigue corriendo, el número cambia cada minuto).

---

## Hipótesis abiertas tras esta sesión

### H-REGIMEN: El mercado tiene regímenes bajistas/alcistas persistentes en el día
**Evidencia hoy**: 70% de slots #15min fueron NO. BTC -3.12% en el día.
**Estado**: confirmado para hoy. ¿Se repite en otros días? Necesita verificación con datos de más días.
**Acción**: el drift en el GBM ya lo captura parcialmente. Si el HMM se implementa, lo haría de forma más sofisticada.

### H-BUYNO: BUY_NO tiene edge estructural sobre BUY_YES en #15min
**Evidencia**: 11/11 BUY_NO vs 10/22 BUY_YES — pero todo en un día bajista.
**Estado**: **no confirmado como edge estructural**. Es artefacto del día. Revisar cuando tengamos datos de 5+ días distintos.
**Acción**: vigilar el split BUY_YES/BUY_NO en días alcistas. Si BUY_YES gana el 70% en días alcistas, el patrón es simétrico y no hay bias.

### H3: BTC#5min momentum opuesto a ETH/SOL
**Estado**: sin datos por bug del CSV (features vacías). Ahora el fix está activo.
**Acción**: verificar en 5-7 días cuando tengamos features en BTC#5min.

---

## Prioridades para la próxima sesión

1. **Verificar que el drift funciona** — comprobar en las primeras predicciones que `drift_15min`/`drift_60min` están en las features y que el modelo está ajustando `p_up` correctamente.

2. **H-REGIMEN con más días** — ¿el split BUY_YES/BUY_NO se invierte en días alcistas? Analizar con todos los días disponibles, no solo hoy.

3. **SMART_FLOW_1H** — IC=-0.195 con n=13. ¿Desactivar o esperar más datos limpios?

4. **Dataset Jon-Becker** — sigue siendo la prioridad de mayor impacto. Con 36GB de histórico podemos backtestear todo.

5. **WEEKLY_PRICE** — resolvió a las 16:00 UTC. Ver resultados y calcular IC inicial.

---

## Constante nueva añadida esta sesión

```python
# shadow_predict.py
DRIFT_DAMPING = 0.25  # fracción del drift observado que entra en el GBM
```
