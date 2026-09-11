---
name: dev
description: Instrucciones para trabajar en el worktree de desarrollo sin tocar el bot en producción. Usar cuando el usuario quiere experimentar con nuevas estrategias, ajustar thresholds, o hacer cambios que podrían romper el bot corriendo. Triggers: "dev", "worktree", "experimento", "probar cambio", "sin tocar producción", "rama dev".
---

# Modo desarrollo — worktree aislado

El bot corre en producción en `/root/polymarket-research` (rama `main`). Los experimentos van en `/root/polymarket-research-dev` (rama `dev`).

## Regla de oro

- Cambios en `shadow_predict.py`, `shadow_postmortem.py`, `hypothesis_tracker.py`, o cualquier script del loop → **trabajar en dev primero**
- Fixes urgentes de producción (bug crítico, crash) → pueden ir directamente en main si el riesgo de no hacerlo supera el riesgo del cambio
- Cambios en `data/shadow/hipotesis_custom.json` o `data/live/config_live.json` → pueden ir en main directamente (son configs, no código del loop)

## Estado de los worktrees

```bash
git worktree list
git -C /root/polymarket-research-dev status
git diff main..dev -- shadow_predict.py | head -50
```

## Flujo de trabajo

```bash
# 1. Editar en dev
nano /root/polymarket-research-dev/shadow_predict.py

# 2. Probar manualmente (sin afectar el bot)
cd /root/polymarket-research-dev && python3 shadow_predict.py --dry-run 2>&1 | head -20

# 3. Ver diff vs producción
git diff main..dev -- shadow_predict.py

# 4. Cuando el experimento valida (IC positivo en shadow)
# Desde main:
git merge dev --no-ff -m "feat: [descripción del experimento validado]"

# 5. Si el experimento falla → descartar
git -C /root/polymarket-research-dev checkout -- .
```

## Qué validar antes de mergear a main

- [ ] El script no tiene errores de sintaxis: `python3 -m py_compile shadow_predict.py`
- [ ] El IC del subtipo afectado mejoró en shadow (al menos 20 ops forward con el cambio)
- [ ] No hay regresión en otras estrategias (IC global no cae >0.02)
- [ ] El cambio está documentado en CLAUDE.md (sección de hipótesis o constantes clave)

## Qué NO hacer en main

- No cambiar `DELTA_MIN`, `DELTA_MAX`, `ORDER_FLOW_BLACKLIST_HOURS`, `DRIFT_DAMPING` sin validación en dev
- No añadir nuevas estrategias sin al menos 20 ops en shadow
- No subir EDGE_MINIMO sin análisis de impacto en señales generadas

## Comandos útiles

```bash
# Loops corriendo en producción
screen -ls                          # ver sesiones
screen -r fast                      # attach al loop fast
screen -r slow                      # attach al loop slow

# Diff entre dev y main
git diff main..dev                  # todos los cambios
git diff main..dev -- shadow_predict.py

# Sincronizar dev con main sin mergear
git -C /root/polymarket-research-dev rebase main
```
