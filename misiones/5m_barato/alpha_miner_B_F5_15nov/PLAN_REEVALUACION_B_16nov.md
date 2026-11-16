# Reevaluación de B y la subvariante — inventario y diseño de la descomposición de la brecha (16-Nov-2026)

Solo texto: 0 cómputo, 0 procesos tocados. Lo escribe la sesión principal a petición de Javi (16-Nov).
Fuentes leídas hoy: `docs/DECISION_LOG.md`, `exp1/RESUMEN_FINAL.txt` (15-Nov 19:02Z, ADD1, «NADA validado»), memorias de checkpoint 02-Nov..15-Nov, `paquete_l` 13-Nov.
**Limitación**: la clasificación de cada fila sale de la fecha y de lo que dicen el log y las memorias; NO he reabierto cada informe. Antes de recalcular, el auditor confirma cada dependencia.

## Reglas de esta reevaluación (Javi 15-16-Nov)
1. Reloj/época por SUELO rx−ex medido por ventana (lo/hi/indet), nunca por fecha. Resultados por clase de suelo primero.
2. Sello del print/relleno = `passT_v3` (tm3). Todo lo fechado con libro5_tx, `t−63` o `t−50` = sello viejo.
3. Latencia SOLO de los ensayos reales vigentes (`paquete_l` 13-Nov B2/B3/B5): alta ex−envío p50 34-38 ms, cancelación efectiva ex−envío p50 32-34 (p90 41-111), RTT cancel 56-59. Clase de suelo cubierta: LO. La Sonda 30-Oct..05-Nov NO se mezcla.
4. Un negativo con reloj/sello/latencia sin verificar = INSUFFICIENT («no validado»), nunca REJECTED. No cerrar puertas.
5. Métricas: EV ponderado por € Y por unidad; IC90 por días y por cierre; sin los 2 mejores días; placebo e inversión; BTC (subvariante) separado.

## Parte 1 — Inventario de veredictos heredados de B y la subvariante
Estado nuevo = «NO VALIDADO» salvo que se indique lo contrario. «Dep.» = de qué dependía: S sello de print/relleno pre-v3, R reloj/época por calendario, L latencia simulada (68/145/215 ms o Sonda), M métrica/simulador sesgado, F fuga detectada después.
Prioridad: A = recalcular primero (afecta directamente a la brecha), B = después, C = estructural/baja.

| Fecha | Veredicto heredado | Dep. | Prioridad | Qué recalcular |
|---|---|---|---|---|
| 16-17 Oct | Cosechar al abrir A/B (H10/H11), palancas 13a/13b, H32 → REJECTED | S, R, F (m5_registro no cronológico, A_BN activa 94-100 % en v1) | B | Tras el fix v2; rehacer con passT_v3 y suelo. Mecanismo nuevo reabre (regla 14) |
| 17 Oct | H26 «Binance en contra»: efecto 1ª pasada era look-ahead; versión causal | F, S | B | Confirmar con tm3 |
| 17 Oct | Simulador maker banda → NO_REPRODUCE (comparaba objetos distintos; criterio «primeras K acciones») | M, S | **A** | Es el origen de la brecha: población (todo el volumen) vs nuestras 5 acciones |
| 17 Oct | H26-MS: Binance no avisa a tiempo (EXPLORATORY); Λ 30-300 ms, te→rx 21/31/140 ms | R (suelo 38-41 ms) , L | **A** | Repetir con l real 35-60 ms y suelo por ventana |
| 17 Oct | Predicción del movimiento de Binance → REJECTED como defensa del maker (H=150/250/400 ms; AUC OOS 0,73) | L (H ≥150 ms era la latencia asumida), R, S | **A** | Horizontes ≤60 ms; ahora l es ~3-4× menor |
| 17 Oct | Salidas tras relleno H37/H40/H41 → REJECTED (venta al bid con comisión) | S (fecha del relleno) | A | Con tm3 y bid real a +5/30/120 s |
| 17-19 Oct | H5M/H26 «+0,142» inflado por métrica; ponderado ≈+0,064; H43 R5K validado +0,306 (n=238, 3 días); R5K ~ +0,057 + 1,61×EV población | M | B | Todo en ponderado por €; recalcular R5K con tm3 |
| 20 Oct-22 Oct | V4 «comprar lo bueno» NO capturable como tomador; B real: XRP −0,025 vs ETH +0,151, SOL +0,168 (251 pujas) | L (215 ms tomador medido 213 ms, sigue vigente), S | B | Solo el tramo maker de B |
| 27-28 Oct | Predictor AS, salida dinámica, F8, ESCALERA, ENTRADAS<0,10, FORMULA_R1 → REJECTED | S, R, L | **A** | Salida dinámica con l real y tm3 |
| 28 Oct | R9: E1 red profunda / **E3 colocación** → REJECTED; brecha = rellenos «solo toque» | S, R | **A** | Colocación es una palanca SIN MEDIR en EXP-1: rehacer con tm3 |
| 29 Oct | Hazard BTC → REJECTED (2 fugas corregidas; EV real −0,08..−0,12) | F (corregida), R | A (subvariante) | Rehacer por suelo; separar R1/R2 |
| 02-03 Nov | A3 INSUFFICIENT; escalera REJECTED (ventaja AR = qué fills y cuándo); C1/ETH INSUFFICIENT; M1 BTC (saturación C, no reloj) | S | B | Con tm3 y suelo |
| 05-09 Nov | Q11 SOL013 / THRU1 / PISTAS / GIRO (prereg + 7 addenda; Calma-T1 v1 con sello `t−63`) | S | A | Ya recalculado con v3 en EXP-1(c): T1 EV −0,124 (REFUTA literal), mitigación T1−G0 +489 € (IC90 días +248..+708) **sin validar** |
| 09 Nov | Q5 identidad tomador previa al casado: CERRADO NO VIABLE | estructural (sin fuente pre-casado) | C | No se cierra: «sin datos pre-casado»; reabrir si aparece fuente |
| 09 Nov | Disección bots de B: mecanismo = ráfagas tras movimiento de Binance; mitigar 100 % | S, L | A | Entra en la descomposición (paso P6) |
| 11 Nov | CXB60 TRAIN +0,135 (IC90 cruza 0; +0,040 sin 2 mejores) | v3 pero época/suelo sin separar | A | EXP-1 ADD2/ADD3 por clase de suelo |
| 15 Nov | EXP-1 (ADD1): B real −0,072; reglas CXB60/F5C/UNION INSUFFICIENT; gradiente F5 INSUFFICIENT; brecha −0,285 | primer pase v3; 3 días fallidos + 17 sin intentar | **A** | ADD3 pendiente (relanzar con RAM libre >5 GB) |

Marcado «no cerrar puertas»: ninguno de estos queda como REJECTED firme hasta recalcularse con las reglas de arriba. Lo que ya está recalculado con v3 es solo EXP-1.

## Parte 2 — Diseño de la descomposición de la brecha de B (EV población +0,213 vs real −0,072 → −0,285)
**Objetivo**: descomponer la brecha en pasos medibles y hallar, para cada uno, una regla que lo cierre (mandato Javi: eliminarla, «no vale un no»).
**Primera pregunta (discriminante)**: ¿es alcanzable el +0,213? La población son prints de bid q en (0,10;0,30] (CENSURADA: gradiente, no EV de regla; mediana 24 rellenos por unidad frente a nuestras 5 acciones; lección 17-Oct). Prueba: correr NUESTRO motor v3 (fills virtuales, ya existe en el dry-run) sobre las MISMAS celdas día×moneda×tipo B.
- Si el motor da ≈ +0,2 → la brecha es de EJECUCIÓN real (pasos P2-P6).
- Si el motor da ≈ −0,07 → la brecha es de DEFINICIÓN de la población (censura/ponderación) y el +0,213 no es un objetivo.
- Intermedio → repartir entre ambos.
(El 15-Nov se anotó EV real vs motor −0,222 vs −0,061 como «supuesto no medido»: es el mismo contraste y hay que cerrarlo primero.)

**Escalera contrafáctica** (cada peldaño cambia UNA cosa; misma población de fills, mismos días; orden fijo y además permutación de órdenes tipo Shapley porque los efectos no son aditivos):
| Paso | Qué cambia | Medida | Fuente |
|---|---|---|---|
| P0 | Población censurada, ponderada por prints | EV +0,213 (E6) | `exp1/` E6 |
| P1 | Definición de unidad: «primeras K=5 acciones», ponderado por € | EV de la población con nuestra definición | tm3, on-chain |
| P2 | Selección en el relleno (nuestros fills = solo toque/selección adversa; rellenas aciertan −18 pp) | Δ al pasar de población a fills nuestros virtuales | dry-run cxb60 (125 k rellenos virtuales) |
| P3 | Colocación (nivel, distancia al ask, T de la ventana) | Δ por regla de colocación; **sin medir hoy** | libro5_ms, registro ms |
| P4 | Tamaño (5 acc. mínimo vs volumen) | Δ por tamaño | on-chain |
| P5 | Posición en cola | P(relleno) y Δ por cola; log_index on-chain | on-chain (hecho 13-Oct: nadie va delante más que el azar) |
| P6 | Cancelación/salida con l REAL (35-60 ms) | Δ CXB60, F5C, salidas H37/H40/H41 recalculadas | paquete_l 13-Nov, tm3 |
| P7 | Sello/reloj: tm3 vs sello viejo | Δ al re-etiquetar (el tercil F5 cambia 21-37 %) | `own_2026-10-{20..23}.pkl` |
| P8 | Residuo no explicado | brecha − Σ pasos | — |

**Reglas estadísticas**: IC90 por cierre Y por día, sin los 2 mejores días, placebo e inversión (p≤0,0083 con K=6), BTC aparte (subvariante), por clase de suelo lo/hi, ponderado por € y por unidad.
**Potencia**: B real solo tiene 4 días (20-23 Oct, 100 % R1, 202 unidades); el gradiente F5 pedía 52 k-255 k unidades. La escalera sobre fills REALES no tiene potencia; la fuente principal son los fills virtuales del dry-run (125 k, 3 días válidos hoy) y la población on-chain, con los fills reales como comprobación.
**Qué NO se puede concluir con lo que hay**: ningún peldaño tiene aún cifra; esto es un diseño, no un resultado.

## Orden de ejecución (acordado con Javi, un agente cada vez)
1. Relanzar ADD3 con MemAvailable > 5 GB (fuera de 06-09:15Z); alpha-miner parado hasta entonces.
2. data-integrity-authority aprueba relojes/contratos/latencia vigente (solo lectura) ANTES de gastar CPU.
3. Discriminante (¿motor v3 en las celdas de población?), luego escalera P1→P8.
4. statistical-validator + red-team independientes.
5. Palancas sin medir (P3-P5) y F5 event-driven l=35-60 ms.
Relacionado: [[project_cola_reordenada_16nov]], [[feedback_latencia_solo_datos_reales_vigentes_16nov]], [[feedback_no_vale_un_no_explotar_carencias_11nov]].

## Hallazgos preliminares 16-Nov tarde (solo lectura de salidas ya calculadas + 1 corte ligero; EXPLORATORY, nada validado)
1. **La cifra de la brecha depende de la definición/ponderación** (`exp1/E6_brecha_add2.txt`, 09:33Z; p60/p35): población «tipo B» ponderada por coste de B +0,185/+0,203, agrupada −0,180/−0,193; «todas las filas» ponderada +0,073, agrupada −0,076. Brecha con B real −0,072: tipo B −0,258/−0,275 (pond.) pero +0,107/+0,121 (agrupada); todas −0,145 (pond.) / +0,004 (agrupada). Además el +0,213 del RESUMEN_FINAL (15-Nov 19:02Z) no coincide con +0,185/+0,203 de E6 posteriores (población PARTIAL, 531.217 prints): cifra no reconciliada. Celdas dominadas por pocos casos (p. ej. 10-20 ETH: población −0,68 con B +0,08; 10-23 SOL/XRP B −1,00 con ~5 € de coste).
2. **Colocación (palanca sin medir), corte ex-ante** sobre `exp1/B_fills_v3.pkl` (215 fills, tm3, 20-23 Oct, 4 días; criterio bid(t_dec,l=60) − precio ≥ 0,0099): 119 fills a ≥1c bajo el bid → EV +0,011, IC90 por cierre [−0,34, +0,38]; 96 a la altura del bid o por encima → EV −0,170, IC90 [−0,50, +0,19]. Ambos IC cruzan 0; el signo por día no es estable (tipo B: −0,24/+0,44/−0,15/−1,00); sin los 2 mejores días ambos < −0,3. Por moneda (tipo B): ETH +0,006, SOL +0,099, XRP −0,075. **No es palanca validada**: insinuación a testear con el dry-run (125 k rellenos virtuales) y con el ladder P3.
3. **Desajuste a vigilar**: los 215 fills reales son 100 % época R1 (suelo rx−ex 38-41 ms por fecha) y los datos de latencia vigentes (`paquete_l` 13-Nov) son de suelo ≈19 ms (clase LO). No se puede trasplantar la `l` de paquete_l a los fills R1 sin declarar la clase; resultados por clase primero (Javi 16-Nov).
