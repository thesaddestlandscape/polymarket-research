# Plan de recarga de B en noviembre (Javi 26-Oct: «en noviembre haremos una recarga de capital para que B testee todos nuestros hallazgos»)
Estado: BORRADOR del chief. Nada se envía sin diseño + /code-review + OK final de Javi. Los números marcados (*) son propuestas a simular antes de fijarlos, no resultados.

## Principio (corregido por Javi 26-Oct)
NO se recarga B para descubrir: se recarga cuando el equipo YA tiene la solución de la selección adversa y un EV positivo, validado y encaminado a los 200 k€. El primer tramo real es la CONFIRMACIÓN de lo validado en forward/shadow con la etiqueta virtual calibrada, no su descubrimiento.
GATE DE RECARGA (todos, o no hay recarga y se informa a Javi): (1) mecanismo de mitigación de AS con forward ≥10 días, EV ponderado por € > 0, IC90 por días > 0, sin los 2 mejores días, placebo e inversión correctos; (2) simulador calibrado contra rellenos reales de B reproduce el P(fill) real y mantiene EV > 0; (3) red-team independiente con datos crudos; (4) cuentas del libro: contribución a 200 k€ con capacidad, capital y solapamiento. Hoy: validado 0 €/año, ninguna pieza cumple (1); el equipo trabaja hasta cumplirlo, y si a fin de mes no se cumple, se lo digo a Javi en vez de recargar.
Nota de potencia: n≈215 solo distingue ~0,28 €/€; el EV positivo hay que demostrarlo en forward/shadow (más n) antes del dinero.

## Candidatas a testear (orden de entrada, solo si pasan su gate previo)
| Brazo | Qué | Gate previo | Fecha prevista |
|---|---|---|---|
| R0 | saltar lado CON (|rpre|≥7,7 bps), ETH/SOL/XRP | forward pasivo L1/L1b/P-REAL ≥10 días | ~02-03 Nov |
| R1 (E1D) | regla cancelación ms con prereg reparado | forward ≥10 días con gate sin peor día ni 2 mejores | ≥04-Nov |
| A1/F5 | cancelar con tamaño grande en ask (≤100 ms), nivel real de B | forward pasivo ≥10 días, base F2×moneda×hora | ~04-Nov |
| skip025 | saltar pujas ≥0,25 | forward cron 10:50 | ver cron |
| nivel/vida de puja | top vs top−1c, clip 5/10, T0-120/120-240, mantener 3-12 s | solo mide con A/B real | dentro de la recarga |
| Control | B actual sin cambios | — | siempre |
Asignación aleatoria por mercado (semilla registrada), un brazo por mercado, mismo flujo para todos.

## Protección de capital (lo que sí «evita pérdidas»)
- Recarga por TRAMOS de ~35 $ (*), no de golpe; el siguiente tramo solo si el anterior cierra con datos suficientes para el gate del brazo.
- Tope de pérdida del tramo y suelo de equity que PARA B (*), calculados con el simulador de x_salida (14 reglas) y la tasa de falso disparo con acierto ≈21 % y pago +4,1/−1,1 $ (el drawdown viene del pago, no de la regla).
- Retirada/reinversión por tramos: si hay beneficio realizado, se retira el capital inicial del tramo y solo se reinvierte lo ganado (plan escalonado). Sin ganancia no hay escalado.
- Wallet dedicada 0x659a…297F; máx. exposición según decisión de Javi; DRY_RUN→micro-real solo con el flujo de FLUJO_DE_TRABAJO.md.
- Mientras tanto: ninguna recarga, y el forward pasivo sigue acumulando (cron L1/L1b, A1, R1, skip025).

## Antes de recargar (checklist)
1. Gates de forward cumplidos o decisión explícita de Javi de probarlos igualmente como exploratorios.
2. Calibración de la etiqueta virtual vs real entregada (en curso 26-Oct).
3. Código de variante de B en dev + /code-review adversarial + tests + brazo aleatorio registrado.
4. OK final de Javi con importe exacto del tramo 1.
5. Libro de cuentas (objetivo-200k) con coste máximo de información aceptado.

## Qué NO es
No es una promesa de rentabilidad: validado 0 €/año; hueco ≈193,7 k€. Si ningún brazo supera al control con gate, B no escala y se redirige el capital a otras subestrategias de 5m barato.
