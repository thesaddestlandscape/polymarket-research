# Plan de ejecución — BTC 5m barato

Corte: 16-Oct-2026 07:40Z. Este plan solo se modifica mediante una decisión documentada en `docs/DECISION_LOG.md`.

## P0. Recuperar `cosechar al abrir` A/B

**Meta:** completar el análisis interrumpido sin duplicar registros ni resultados.

1. Inventariar procesos, scripts, stdout/stderr, outputs, checkpoint y manifest.
2. Confirmar que solo 05–06-Oct están completos o hallar más cobertura válida.
3. Recuperar comando exacto, rutas e inputs. No adivinar `python3 ...`.
4. Verificar en una copia pequeña la reanudación idempotente y el ledger.
5. Ejecutar el trabajo pesado fuera de 06:00–09:00Z con prioridad baja si soportada (`nice -n 19`, `ionice -c3`).
6. Cada run deja manifest, checkpoint atómico, log, contadores y reporte `COMPLETE/PARTIAL/FAILED/BLOCKED`.
7. Comparar A (BTC 5m general) contra B (BTC 5m barato con defensa 15m) con el mismo universo cuando sea posible y detallar las diferencias.

No lanzar dos trabajos intensivos a la vez.

## P1. Diagnóstico barato de V7 sin señales

No lanzar reejecución masiva hasta que una consulta ligera identifique el primer punto del pipeline en el que los eventos BTC pasan a cero. Chequear feed/heartbeat, reloj, parser, filtros, registry, error de señales, régimen y fuente de trigger. Clasificar `DATA_PIPELINE`, `FILTER/REGIME`, `STALE/CLOCK`, `REGISTRY`, `UNKNOWN`.

## P2. F2 y conciliación del 17-Oct

1. Verificar desde logs/config que V4/V7 corren en shadow/dry-run.
2. Recuperar criterios F2→F3 congelados del diseño original.
3. Preparar conciliación con los «vigías», sin activar sender ni enviar órdenes.
4. Aclarar la medición decision→send y los checkpoints 07:30/07:45.
5. No rediseñar gates para que el resultado sea favorable.

## P3. Mantener V4 y FV V4

- V4 congelada; medir el forward con mismos gates y anotar drift.
- Auditar FV V4: fórmula, calibración, Brier, R², EV, denominador, fees, fill model, OOS.
- FV V4 solo puede avanzar a especificación maker 4/4b después de ≥5 días cronológicos válidos y revisión de chief/validator/red-team.

## P4. Agent 5: disección estratégica de wallets

Secuencia preferida: completar A/B; luego correr «lo invisible» con selección congelada de wallets y periodo holdout. Si se diseña trabajo de preparación en paralelo, debe ser read-only y no mirar el holdout ni condicionar criterios según sus resultados.

Entrega: mecanismo de PnL, proceso de decisión, edge reproducible, debilidades, diseño mejorado propio, comparación emparejada y protocolo OOS. No copiar fills.

## P5. Construir el mapa de portafolio hacia €200k

Risk-economics trabaja con medios existentes. No paraliza los forwards ni depende de que todas las subestrategias estén validadas para hacer escenarios. Debe:

- Calcular contribución anual conservadora/base/optimista por candidata y estado de evidencia.
- Mostrar contribución validada separada de discovery y forecast.
- Calcular el gap desde €0 validado hasta €200k.
- Descomponer el gap en palancas: EV por fill, más señales válidas, fill rate, capital y profundidad disponibles, nuevas subestrategias no solapadas, robustez/uptime.
- Cuantificar overlap de mercados/ventanas, correlación, costes compartidos y límites de capital para no sumar dos veces el mismo alpha.
- Priorizar pruebas con mayor información esperada por unidad de tiempo/cómputo, sin comprar datos/infraestructura ni aumentar stakes a ciegas.
- Entregar una ruta operativa por hitos, cada uno condicionado a evidencia verificable.

## P6. Otras hipótesis

Solo después de P0–P5, o mediante datos exploratorios baratos que no distraigan el trabajo prioritario: altcoin boxes, anidados 4h, caja maker de dos patas.

## Reglas de proceso

- Un solo heavy job; consultas de diagnóstico y auditorías read-only sí pueden paralelizarse si no compiten por I/O.
- Cada experimento tiene ID, owner, pregunta falsable, input hashes, periodo, universe, checkpoint, salida y criterio de aceptación/rechazo.
- No se acepta «terminado» sin reporte y comprobación de cobertura.
- El estado anual validado solo aumenta cuando una estrategia pasa sus gates congelados; las cifras discovery aparecen separadas.
