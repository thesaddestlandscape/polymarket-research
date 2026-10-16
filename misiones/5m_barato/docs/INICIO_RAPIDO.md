# Inicio rápido — Claude Code 5m barato

Abre Claude Code desde la raíz del repositorio. Comprueba que los agentes `.claude/agents/*.md` están detectados; si acabas de instalarlos y no aparecen, reinicia la sesión.

## Orden inicial recomendado

1. **Read-only:** invoca `cheap5m-repo-auditor` para inventariar repo, git, V4, jobs incompletos, checkpoint, informe de estado, F2 y procesos existentes.
2. **Read-only ligero en paralelo:** `cheap5m-market-data-engineer` diagnostica dónde desaparecen las señales V7; `cheap5m-event-causality-analyst` prepara la cronología solo con artefactos disponibles.
3. **Plan recuperación:** `cheap5m-chief` debe emitir el comando exacto para reanudar `cosechar al abrir` A/B, sin adivinar paths, con checkpoints e idempotencia. No iniciar trabajo pesado entre 06:00 y 09:00Z.
4. **Mantener forward:** V4 y FV V4 no se optimizan. FV se audita y acumula cronología con configuración congelada.
5. **Después de A/B:** invocar `cheap5m-wallet-intelligence-analyst` para la fase «lo invisible». Debe analizar mecanismos, inventario y fuentes de PnL, y diseñar cómo mejorar y superar benchmarks, no copiar fills.
6. **Cartera objetivo:** `cheap5m-risk-economics` debe producir un plan activo hacia 200.000 € netos/año por suma de subestrategias 5m barato, con medios existentes y sin doble conteo.

## Prompt recomendado para primera sesión

Usa `misiones/5m_barato/docs/PROMPT_INICIAL.md`. Los subagentes `cheap5m-*` viven en `.claude/agents/` (raíz del repo); el chief es la sesión principal. Subagentes sin cuota hasta el 19-Oct 13:00 UTC (límite semanal).

## Seguridad

No habilites credenciales de trading, no leas `.env`, no cambies procesos a live, no envíes órdenes reales y no compres infraestructura. F1 fue una prueba histórica y no debe repetirse.
