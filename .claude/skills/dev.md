# Modo desarrollo (worktree aislado)

Instructs working in the dev worktree to avoid disrupting the production bot.

## When to use
When the user asks to experiment with a new strategy, adjust thresholds, test filters, or make changes that might break the running bot.

## Instructions

Explain to the user:

**El worktree de desarrollo está en `/root/polymarket-research-dev` (rama `dev`).**

Para trabajar sin tocar el bot en producción:
1. Los cambios experimentales van en `/root/polymarket-research-dev/`
2. El bot de producción sigue corriendo en `/root/polymarket-research/` (rama `main`)
3. Cuando el experimento valida → `git merge dev` en main

**Comandos útiles:**
```bash
# Ver el estado de ambos worktrees
git worktree list

# Trabajar en dev (editar archivos ahí)
# Los scripts se ejecutan desde /root/polymarket-research-dev/

# Cuando el experimento está listo, mergearlo a main (desde el worktree principal)
cd /root/polymarket-research
git merge dev --no-ff -m "feat: [descripción del experimento validado]"

# Si el experimento falla, descartar
git -C /root/polymarket-research-dev checkout -- .

# Ver diff entre dev y main
git diff main..dev -- shadow_predict.py
```

**Qué va en dev vs main:**
- Dev: nuevos filtros, ajustes de umbral, estrategias experimentales, cambios en features JSON
- Main: solo cambios validados con IC positivo en shadow, fixes de producción urgentes

Before making any changes to python scripts in this session, confirm with the user whether to work in `/root/polymarket-research` (production) or `/root/polymarket-research-dev` (development).
