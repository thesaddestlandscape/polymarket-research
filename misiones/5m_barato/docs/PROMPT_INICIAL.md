# Prompt inicial para Claude Code

Actúa como `cheap5m-chief` (rol de la sesión principal, `misiones/5m_barato/docs/ROL_CHIEF.md`), lee en `misiones/5m_barato/`: `CLAUDE.md`, `docs/MAPA_ARTEFACTOS.md`, `docs/TRAMPAS_5M_BARATO.md`, `docs/ESTADO_INVESTIGACION_2026-10-16.md`, `docs/PLAN_EJECUCION_PRIORIDADES.md`, `docs/REGISTRO_HIPOTESIS.md`, `docs/DECISION_LOG.md` y `docs/FLUJO_DE_TRABAJO.md`. Respeta además el protocolo y las reglas del `CLAUDE.md` raíz del proyecto.

**Misión:** hacer funcionar la familia Polymarket BTC 5m barato y desarrollar una cartera de subestrategias complementarias que tenga una ruta verificable hacia el objetivo de 200.000 € netos anuales. La suma familiar es la unidad económica; no podemos duplicar alpha, ventanas, capital ni beneficio entre subestrategias. Debes trabajar activamente para cerrar el gap con recursos y medios existentes, sin falsear resultados ni gastos no autorizados.

**Primero, solo lectura; no modifiques archivos ni ejecutes trabajo pesado hasta inventariar el estado.** Delega a `cheap5m-repo-auditor` comprobar Git, baselines, los dos análisis interrumpidos `cosechar al abrir` A/B, checkpoints, outputs, informe ausente y estado exacto de V4/V7/F2. Requiere rutas y evidencia real, no resúmenes.

En paralelo, usa `cheap5m-market-data-engineer` y `cheap5m-event-causality-analyst` para un diagnóstico barato de por qué V7 no registra eventos BTC desde 13-Oct y encontrar el primer stage que tiene cero eventos. No hagas un replay masivo de V7 antes de localizar el punto de fallo o demostrar que no existe fallo.

P0 es recuperar `cosechar al abrir` A/B: A = BTC 5m general; B = 5m barato con defensa 15m. Solo se han comunicado los días 05–06-Oct procesados y no hay informe. Encuentra el script exacto; no adivines el comando truncado. Diseña reanudación idempotente con checkpoint/manifiesto y ejecuta el trabajo pesado solo fuera de 06:00–09:00Z.

Mantén V4 (`77a75859ae5cf22e`) congelada; mantén cerrada la vía de cancelar órdenes retenidas en taker-delay; sigue FV V4 sin cambiar parámetros; solo al cumplir ≥5 días cronológicos válidos y revisar métricas se puede congelar un maker-FV 4/4b separado.

El agente 5 (`cheap5m-wallet-intelligence-analyst`) no debe copiar trades/fills de las wallets. Su misión es reconstruir el mecanismo completo que produce el beneficio, separar selección direccional, pares, liquidez, inventario, costes y ejecución; encontrar qué hacen antes de los fills; diseñar cómo adaptar y mejorar esos mecanismos en nuestra implementación para intentar superarlos con el mismo universo y una evaluación OOS.

El agente `cheap5m-risk-economics` debe diseñar activamente un plan para que la suma de subestrategias 5m barato alcance, si la evidencia y capacidad lo permiten, 200.000 € netos/año. Debe calcular el gap, contribuciones marginales, overlap, capital, liquidez, fill rates y nuevas vías con recursos disponibles; no vale responder solo «no está validado». Tampoco puede anualizar discovery como ingreso o sumar estrategias solapadas como independientes.

Después de la auditoría, elige un solo job intensivo. Para cada tarea exige pregunta falsable, inputs, periodo, comando reproducible, owner, checkpoint, log, coverage y reporte final (`COMPLETE/PARTIAL/FAILED/BLOCKED`). Un proceso que muere sin informe no ha terminado; retoma desde el último checkpoint válido sin duplicar resultados.

Antes de cualquier cambio, entrega: (1) inventario verificado; (2) diagnóstico inicial de V7; (3) plan exacto de reanudación A/B; (4) agenda F2 17-Oct; (5) mapa preliminar de contribución a 200k, separando discovery y validado. No modifiques código en esta primera fase.

Prohibido: nuevas órdenes reales, firmar transacciones, mover fondos, leer secretos, modificar V4, cambiar F2 a live, contratar VPS/servicios, saltar gates o usar información futura. Toda subestrategia nueva queda en dry-run y en su propia rama/directorio.
