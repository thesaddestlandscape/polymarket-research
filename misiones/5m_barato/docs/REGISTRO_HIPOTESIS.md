# Registro de hipótesis — BTC 5m barato

Este registro es un estado de control, no una certificación. Todo número debe rastrearse al artefacto y fórmula originales. Cada cambio necesita fecha UTC, owner, versión y motivo.

| ID | Familia | Estado a 16-Oct | Pregunta falsable | Siguiente paso / condición |
|---|---|---|---|---|
| H01 | V4, valor relativo 5m/15m | `EXPLORATORY`, baseline congelado; 4/10 gates comunicado | ¿Mantiene EV neto ejecutable pese a concentración y drift? | Reconciliar +€8,36/EV, mantener forward idéntico y gates congelados. |
| H02 | Ask 5m obsoleto tras cambio de bid 15m | Mecanismo provisional | ¿Qué precio/cantidad sigue disponible a llegada? | Replay temporal evento a evento; no inferir desde medianas marginales. |
| H03 | Cancelar órdenes retenidas en taker-delay | `REJECTED/CLOSED` | ¿Existe una vía técnica nueva para cancelar de forma útil? | No reabrir sin evidencia del exchange que contradiga el rechazo observado. |
| H04 | Anticipar cambio del bid 15m | `OPEN/PRIORITY` | ¿Hay precursor causal/predictivo disponible antes del cambio con margen ejecutable? | Prueba sin look-ahead, OOS y replay de llegada. |
| H05 | V7 DISPARO15M_BTC | `DATA_BLOCKED/UNKNOWN` hasta diagnóstico | ¿Cero eventos desde 13-Oct es sequía real, cambio de régimen o bug de pipeline? | Consulta ligera: primer stage count=0; no replay masivo primero. |
| H06 | V6 FOK_VUELO_BTC | `EXPLORATORY` | ¿Por qué ganaban las señales “visibles” en discovery y cambia su resultado a forward? | Verificar definición “visible”, selección y fill; 1 fill forward no basta. |
| H07 | FV V4, valor justo/calibración | `PROMISING` provisional, solo 2 días | ¿Mejora calibración y EV neto fuera de muestra sobre mid/price ejecutable? | Auditoría completa y forward congelado; evaluar al llegar a ≥5 días válidos. |
| H08 | Maker con FV 4/4b | `BLOCKED_BY_GATE` | ¿La señal FV mejora la selección maker y supera adverse selection/cola? | No implementar candidato confirmatorio hasta el gate de ≥5 días válidos y revisión. |
| H09 | Wallet strategy dissection / “lo invisible” | `PENDING_DEPENDENCY` | ¿Qué mecanismos rentables anteceden a la operación y cómo crear una variante propia mejor? | Después de A/B o plan no contaminante; holdout; no copiar fills. |
| H10 | Cosechar al abrir A: BTC 5m general | `PARTIAL/FAILED` | ¿Cómo rinde la cosecha al abrir en 5m normal con fills y costes realistas? | Recuperar artefactos; solo Oct 5–6 comunicados; reanudar idempotente. |
| H11 | Cosechar al abrir B: BTC 5m barato + defensa 15m | `PARTIAL/FAILED` | ¿La defensa 15m mejora la política A sobre el mismo universo? | Mismos eventos y contabilidad; recuperar y reanudar. |
| H12 | EV wallet por bucket de precios | `EXPLORATORY` | ¿EV +0,044 €/€ (<0,10) y +0,082 €/€ (0,10–0,20) generalizan por wallet/fecha? | Placebo recuperado (−0,003); auditar denominador y selección; holdout distinto del de selección. |
| H13 | Copiar fills de wallets | `REJECTED` | ¿Una compra pública ya ejecutada permite capturar su alpha? | Cerrada; el objetivo de H09 es ingeniería inversa, no copia. |
| H14 | LOWLOW-PAIR indiscriminado | `REJECTED` | ¿Comprar automáticamente lados ≤0,10 crea alpha? | No reabrir sin predictor nuevo; evidencia previa negativa. |
| H15 | BTC5M-FV-LONGSHOT anterior | `REJECTED` como se probó | ¿Hay nuevo modelo/feature/muestreo realmente distinto? | Solo una hipótesis nueva, no renombrado. |
| H16 | Maker one-sided / pair maker | `REJECTED` en los tests previos | ¿Hay un mecanismo nuevo que resuelva queue/adverse selection? | No reabrir sin dato nuevo y prueba diferenciada. |
| H17 | V2 | `REJECTED/PROMISING?` (comunicado 0/7 gates) | ¿Aporta algo aceptar todas las señales vs V4? | No expandir; reconciliar periodo común. |
| H18 | V3a filtro Binance 5s | `EXPLORATORY` insuficiente | ¿Filtra adverse moves sin eliminar alpha? | Un mercado no permite conclusión; preservar regla. |
| H19 | V5 ORIGEN15M | `EXPLORATORY` insuficiente | ¿La señal nace en 15m y conserva EV a llegada? | Una señal/0 fills; mantener separada. |
| H20 | Cartera agregada a €200k netos/año | `STRATEGIC_GOAL/UNVALIDATED` | ¿Puede la suma de subestrategias sin doble conteo cubrir €200k usando recursos existentes? | Risk-economics: mapa de contribución, gap, capacidad, overlap, plan por hitos. |
| H21 | Caja altcoin | `NOT_STARTED/LOW_PRIORITY` | ¿Existe edge no solapado y capacidad más allá de BTC? | Solo tras prioridades principales; verificar cifras originales. |
| H22 | Anidados 4h / maker caja dos patas | `NOT_STARTED/LOW_PRIORITY` | ¿Mecanismos no refutados y económicamente ejecutables? | Tras P0–P5; una hipótesis por vez. |

## Reglas

- «REJECTED» se refiere a la versión/mecanismo ensayado, no prohíbe una hipótesis genuinamente nueva; el cambio debe justificarse.
- Datos no verificados mantienen la etiqueta `reported`; no presentarlos como hechos finales.
- Nunca escoger wallets o ventanas en función de resultados futuros del holdout.
- Cuando varios mecanismos operen en el mismo mercado/ventana, no sumar su PnL como si fuesen independientes.
- Cada candidata tiene owner, commit/hash, config, universo, discovery/OOS, gates, artefactos y criterio de cierre.
