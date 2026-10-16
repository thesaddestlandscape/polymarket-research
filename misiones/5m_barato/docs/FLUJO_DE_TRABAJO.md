# Flujo de trabajo multiagente — 5m barato

## 0. Director y regla de carga

`cheap5m-chief` (= la sesión principal, que sigue `docs/ROL_CHIEF.md`; un subagente no puede lanzar subagentes) es responsable de la prioridad, dependencias y decisión; Javi capitanea y decide. Hay **un único trabajo pesado a la vez**. Se pueden paralelizar auditorías y consultas read-only si no compiten por I/O ni miran indebidamente el holdout de otro agente; máximo 2-3 subagentes simultáneos (cuota).

## 1. Fase de lectura y preservación

Invocar `cheap5m-repo-auditor` antes de cualquier cambio. Verificar git, V4 y hashes, jobs, artefactos, checkpoint, logs, datos originales, F2 mode y outputs. No editar baselines.

## 2. P0: continuidad `cosechar al abrir` A/B

- Agent repo auditor reconstruye qué hay y cobertura.
- Market data engineer revisa esquema, claves idempotentes y huecos.
- Execution engineer es el único que crea/corrige soporte de resume en un área aislada después de especificación.
- Trabajo heavy fuera de 06:00–09:00Z.
- Cada mercado/día se escribe de forma idempotente con manifest/checkpoint. Al reanudar, verificar rows procesadas antes de añadir más.
- Informe obligatorio: A/B, cobertura por día, parciales, pérdidas, fills, costes, incertidumbre y paths.

## 3. P1: V7 cero señales

Consulta barata primero: último evento en cada fuente y paso; conteos de BTC antes/después de filtros; heartbeats, gaps, parser, reloj, registry, exceptions. Identificar primer punto en el que el conteo pasa a cero y clasificar causa. No lanzar replay masivo hasta documentar la razón.

## 4. P2: F2 conciliación

Verificar el proceso en shadow/dry-run, recuperar gates F2→F3 congelados, preparar conciliación con vigías el 17-Oct. Instrumentación decision→send solo en mock/shadow. Nunca repetir F1 real.

## 5. P3: forwards congelados

- V4 no se modifica.
- FV V4 se audita y sigue en forward con configuración fija.
- Al alcanzar ≥5 días cronológicos válidos, preparar propuesta maker FV 4/4b separada, pero pasar revisión independiente antes de comenzar un nuevo forward.

## 6. P4: ingeniería inversa de wallets

Agent 5 tiene misión explícita de reconstruir y mejorar su mecanismo, no copiar fills. La fase «lo invisible» viene después de A/B salvo plan read-only y no contaminante documentado por chief. Selección de wallets en discovery, holdout cronológico separado y placebo.

## 7. P5: construcción de portafolio para €200k

Risk-economics debe hacer un plan hacia el objetivo utilizando la suma de las subestrategias de 5m barato y los medios existentes: contribución por candidata, gap a 200k, solapamiento de ventanas, límites de capital/liq, presupuesto de cómputo, coste de ejecución, nuevas subestrategias candidatas y orden de investigación. No basta con señalar que €200k no están validados. El plan tampoco puede sumar como independientes estrategias que disputan las mismas oportunidades.

## 8. Congelar experimento antes de confirmar

Cada experimento tiene ID, mecanismo, hipótesis falsable, owner, commit/hash, universo, periodo, señal, timestamp de decisión, coste/fill, controles, métrica primaria, gates y regla de parada. Registrar antes de evaluar el holdout.

## 9. Implementación

Solo `cheap5m-execution-engineer` modifica código experimental bajo una especificación congelada. Rama/directorio separado; sin V4, datos raw ni producción. Añadir tests de timestamp, checkpoint, idempotencia, ejecución parcial, coste, posición residual y conciliación PnL.

## 10. Validación y ataque

- `cheap5m-statistical-validator`: reimplementa/recalcula independiente.
- `cheap5m-red-team-auditor`: busca la explicación más fuerte por la que la señal sería falsa.
- `cheap5m-risk-economics`: construye la cartera agregada y prueba el gap económico.

El implementador no aprueba su propio experimento.

## Estados válidos

- `REJECTED`
- `DATA_BLOCKED`
- `EXPLORATORY`
- `PROMISING`
- `DRY_RUN_VALIDATED`
- `PARTIAL` / `FAILED` para trabajos incompletos

No usar «terminado» si no existe informe, manifest, coverage y comprobación de completitud.
