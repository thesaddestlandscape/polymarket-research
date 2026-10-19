# 5M BARATO — INSTRUCCIONES MAESTRAS Y ESTADO DE INVESTIGACIÓN

> **Ámbito EXCLUSIVO (Javi 16-Oct):** este fichero y los agentes `cheap5m-*` sirven SOLO para la misión 5m barato y no se
> extrapolan a nada más. Adaptado del paquete de Javi del 16-Oct (originales intactos en `original_drive_16oct.tar.gz`,
> SHA256 verificado; cambios y motivos en `docs/CAMBIOS_VS_ORIGINAL.md`).
> **Precedencia:** el `CLAUDE.md` raíz del proyecto (protocolo, trampas, reglas de dinero) MANDA sobre este si chocan.
> **Leer antes de nada:** `docs/MAPA_ARTEFACTOS.md` (rutas reales verificadas: no buscar lo que ya está ahí) y
> `docs/TRAMPAS_5M_BARATO.md` (errores ya cazados). Todas las rutas de este directorio son relativas a `misiones/5m_barato/`.

**Corte de estado:** 16-Oct-2026 07:40Z. Las cifras son comunicadas por el investigador; deben reproducirse desde los artefactos originales antes de considerarse validadas. Las instrucciones de prioridad se actualizan a partir del parte de 16-Oct.

## 1. Misión única

Investigar, diseñar, implementar en modo seguro y validar las subestrategias de la familia **Polymarket 5m barato** (definición exacta en `docs/MAPA_ARTEFACTOS.md` §0: pata 5m barata respecto a la cota bid15(s) del par anidado 5m/15m; diseño y decisiones en BTC, datos de las 6 monedas; v4/V2/V3/V5 multimoneda tal como se congelaron). La meta familiar es desarrollar una cartera de subestrategias complementarias que aspire a **200.000 € netos anuales en conjunto**, usando en primer lugar los datos, código, feeds, tiempo de cómputo e infraestructura que ya están disponibles.

El agente económico no debe limitarse a responder que la cifra no está validada: debe trabajar hacia ella, cuantificar el gap, encontrar contribuciones plausibles por subestrategia y proponer un plan de investigación que maximice la probabilidad de cerrar el gap con los medios existentes. A la vez, no debe inventar rentabilidad, relajar gates, sobreajustar, escalar stake a ciegas ni convertir estimaciones de descubrimiento en previsiones.

**Beneficio anual validado actual: 0 €.** La cifra objetivo es un objetivo de diseño y priorización, no una cuota que sesgue los experimentos.

**Restricción de capital real (verificado 17-Oct 08:45Z):** wallet PRINCIPAL live cripto 0xB6eD…028b = 39,66 $ libres + 4,51 $ en posiciones (`data/live/balance_real.json`; el 16-Oct eran 34,59 $); wallet DEDICADA de experimentos 0x659a…297F = 19,59 pUSD on-chain, 0 posiciones, tope de pruebas 5 € (Javi 09-Oct). `max_stake_eur` live 2,0, calendario sin recargas planificadas. Leer siempre el saldo fresco: estas cifras caducan. Todo escenario que necesite más stake o capital es CONDICIONAL a una decisión de Javi y se etiqueta así; la palanca de capital se modela explícitamente, no se supone.

La estrategia dedicada a BTC 15m permanece independiente. Puede aportar variables de referencia para 5m, pero no se mezclan universos ni resultados sin demostrar un mecanismo y una comparación correcta.

## 1b. Directiva de Javi (19-Oct) — aplica a TODA la misión
«Los agentes tienen que conseguir que esta estrategia funcione de forma objetiva, hacer todo lo posible y lo imposible, está demostrado que se puede; encontrar la forma, convencional o alternativa, cueste lo que cueste.» Primero la dijo para H43 y luego la extendió: «así tiene que ser con toda la misión de 5m barato».
- Todo encargo es de **encontrar y construir la vía de captura**, no de dictaminar si existe. Un resultado negativo se convierte en la siguiente variante a probar (otra colocación, momento, tamaño, moneda, cancelación, fuente de datos, mecanismo de las wallets que ganan, vía no convencional), no en un cierre de la línea.
- **Objetiva:** se mide igual de limpio que siempre (OOS, días independientes, EV ponderado por €, sin look-ahead, sin relajar gates) y se reporta tal cual. El cementerio (§3.6) sigue valiendo para la VERSIÓN probada; reabrir exige una variante con mecanismo distinto, que es justo lo que se pide buscar.
- **Cueste lo que cueste** no anula: gastos sin OK de Javi, límites de la wallet dedicada, /code-review en código que toca dinero, ni los topes de RAM/CPU de la máquina (§7).

## 2. Principios no negociables

1. **Solo shadow/dry-run para nuevas pruebas**, con UNA excepción aprobada por Javi (17-Oct): el peldaño «micro-real» de `docs/FLUJO_DE_TRABAJO.md` (wallet dedicada, ≤5 € de exposición, código en dev + `/code-review` medium + OK final de Javi, lo opera solo la sesión principal). F1 del 15-Oct incluyó pruebas reales históricas; no repetir F1. Los procesos F2 (`f2_5m_barato_dryrun.py`, DRY-RUN fijo sin opción de envío) los gestiona SOLO la sesión principal: ningún subagente los lanza, reinicia ni mata. No cambiar modo ni activar un sender live.
2. **Sin gastos sin autorización.** No contratar VPS, proveedores, datos ni servicios. Priorizar instrumentos, optimizaciones y cómputo ya disponible.
3. **No leer secretos.** Nunca abrir, imprimir, copiar o transmitir `.env`, claves, API secrets, tokens de autenticación, seed phrases o claves privadas. No usar endpoints privados de trading ni firmar transacciones.
4. **Baselines congelados.** No modificar V4 (`vigia_5m_barato_forward.py`, hash_config `77a75859ae5cf22e`), ni ningún vigía congelado (V2/V3/V5/V6/V7/FV v4/H5M: hashean el FICHERO ENTERO; una coma rompe el manifiesto), sus parámetros, resultados históricos ni datasets raw. Nuevos mecanismos van en `/root/polymarket-research-dev` o en `experimentos/5m_barato/`.
5. **Agente 5 = ingeniería inversa, no copia.** Debe diseccionar la estrategia completa de las wallets ganadoras, encontrar la fuente de su PnL, sus limitaciones y los mecanismos generalizables, y proponer cómo adaptar y mejorar el código propio para intentar superarlas. No generar señales copiando fills observados tarde.
6. **No alpha por narrativa.** PnL de una wallet, un hit rate alto, un EV in-sample, un resultado de dos días o un techo teórico no bastan.
7. **Trazabilidad.** Cada cifra necesita fuente, periodo, universo, denominador, fórmula, moneda, costes y artefacto. Los datos ausentes son `missing`, no cero. No reproducido = no verificado.
8. **No look-ahead.** Toda decisión debe usar solo información observable en el timestamp de decisión. Separar exchange event, feed receive, decision, send, arrival, fill/quote disappearance y chain settlement.
9. **Contabilidad completa.** Incluir señales descartadas, fills parciales, órdenes sin fill, posiciones residuales, pérdidas, ventanas sin oportunidad y exposición simultánea. No contar solo pares o trades ganadores.
10. **Validación cronológica.** Separar descubrimiento, calibración, OOS, forward shadow/dry-run y decisiones de despliegue. Cualquier cambio después de ver resultados crea nueva versión y requiere periodo confirmatorio.
11. **Análisis largos recuperables.** Todo trabajo largo necesita manifest, checkpoint durable, claves idempotentes, log, cobertura por fecha/mercado, resumen parcial e informe final. Una sesión que muere sin informe queda `PARTIAL/FAILED`, nunca «terminada».
12. **Un único trabajo intensivo a la vez.** Evitar competencia de I/O entre agentes. Heavy run `cosechar al abrir` solo fuera de 06:00–09:00Z. Dentro de esa franja se permiten diagnósticos ligeros, auditoría y preparación.
13. **El objetivo de 200k orienta el portafolio.** Diseñar la suma de subestrategias con exposición no duplicada y contribución marginal medible. No presentar €200k como logrado ni alcanzable sin evidencia; tampoco abandonar la búsqueda sin mapear el gap y las palancas plausibles.
14. **Cementerio respetado.** No reabrir una hipótesis refutada cambiándole el nombre. Hace falta mecanismo sustancialmente nuevo, evidencia nueva o error concreto en el test previo.

## 3. Estado actual — 16-Oct-2026 07:40Z

La fuente maestra ampliada es `docs/ESTADO_INVESTIGACION_2026-10-16.md`. Si el resumen contradice los datos/código fuente, registrar la discrepancia y conservar ambas referencias hasta resolverla.

### 3.1 Forward de subestrategias — todas solo observación, ninguna ha pasado gates

- **V4 (v1 corregida; baseline):** OOS desde 06-Oct hasta 15-Oct; 43 señales, 17 ejecutables, +€8,36, EV comunicado +€0,21/€. Nueve días; 4/10 gates (pasan G3 EV, G8 reconstrucción, G9 latencia, G10 OOS; G1 = n≥40 EJECUTABLES, a ~2/día → ~27-28 Oct). Un día aporta el 180 % del PnL. Los tres días más recientes están por debajo del 50 % del EV previo: alerta `DRIFT`. Frágil, aún no validada. Mantener forward congelado.
- **V2:** variante con todas las señales, hasta tres por mercado. Desde 12-Oct: cinco mercados, −€2,57, EV comunicado −€0,18; 0/7 gates. Peor que V4 en el periodo común: v1/v4 en el MISMO periodo da EV −0,002 (4 mercados, −0,02 €), ese es el «−0,002».
- **V3/V3a:** V4 con filtro Binance de cinco segundos. Desde 12-Oct: un mercado, −€2,12; 0/7 gates. Muestra insuficiente.
- **V5 `ORIGEN15M`:** desde 14-Oct, una señal y cero ejecuciones; 3/11 gates. Muestra insuficiente.
- **V6 `FOK_VUELO_BTC`:** desde 14-Oct, una ejecución y −€2,12; 0/7 gates. Discovery comunicado ~€30k/año, solo si se valida; descubrir por qué en discovery ganaban las señales “visibles”.
- **V7 `DISPARO15M_BTC`:** discovery comunicado de 8/8 días positivos, EV +1,99 y estimación exploratoria de ~€28–37k/año. Forward desde 14-Oct: cero ejecuciones; no hay eventos BTC registrados desde 13-Oct. Diagnosticar con una consulta ligera si hay sequía genuina, cambio de régimen o fallo en feed/filtros/registro/pipeline.

**Contribución anual validada de toda la familia: 0 €.** Estimación de discovery combinada V6+V7 ~€60k/año, sin validar y potencialmente no aditiva por solapamientos, capital o condiciones compartidas.

### 3.2 FV V4 — candidata nueva más prometedora, aún exploratoria

Dos días cronológicos comunicados: R² del movimiento de mid a 3 s de 0,28/0,29; ΔBrier frente al mid −0,003 en ambos días; como taker con margen 0,05, n=457 y EV +€0,095/€, resultados diarios +€0,049 y +€0,142. Auditar unidades, denominadores, costes, definición de ΔBrier, calendario exacto y separación discovery/OOS. Mantener el forward congelado. Si alcanza al menos cinco días cronológicos válidos y la auditoría es favorable, congelar una especificación separada para maker FV 4/4b y someterla a revisión independiente; cinco días no validan por sí solos el alpha.

### 3.3 Wallet intelligence: objetivo de mejorar y superar, no copiar

- Compras BTC por bucket: EV comunicado +€0,044/€ para precios <0,10 y +€0,082/€ para precios 0,10–0,20; reproducir fórmula y disponibilidad temporal.
- Wallets seleccionadas por rendimiento en 05–09-Oct tuvieron +€0,057/€ en 10–14-Oct, IC90 por días +€0,022..+€0,087, frente a un **placebo de −0,003** (`DL/m5barato_mision/baratas_informe.txt`). Ojo: en makers H5M la selección por resultado NO persistió (14-Oct); reproducir antes de usar.
- `mo-money` (0x32ed2e54…): +$10,4k en diez días; pares −$15,9k y dirección +$26,3k, maker DIRECCIONAL, no cosechador. Su primera pata maker barata (≤0,30) acierta **22,6 % frente a un precio de 17,1 % (+5,5 pp, igual en SEL y TEST)** (`analisis_mo_money_pares_5m.py`).
- Agent 5 debe reconstruir estrategia, inventario, decisión, selección, timing, costes y fuente de beneficio; identificar fortalezas y límites; traducir mecanismos a una política propia que intentemos mejorar y superar en replay emparejado OOS. Nunca copiar fills tardíos. La fase 2 «lo invisible» depende del informe de `cosechar al abrir` A/B, salvo que el chief documente cómo ejecutarla en paralelo sin contaminar resultados.

### 3.4 Trabajos interrumpidos

- `cosechar al abrir` A/B: análisis A (5m general) y B (5m barato con defensa 15m) murió con la sesión tras procesar solo 05–06-Oct y no dejó informe. No asumir terminación. Buscar script, stdout/stderr, artefactos, checkpoint y claves procesadas. Reanudar idempotentemente desde el último dato válido. Ejecutar el cómputo pesado fuera de 06:00–09:00Z. Comando citado parcialmente: `nice -n 19 ionice -c3 python3 ...`; recuperar ruta exacta, no adivinarla.
- Fase 2 «lo invisible» de wallets baratas: no arrancó y depende del anterior. Crear primero especificación de datos y consultas read-only; ejecutar fase completa después de A/B, salvo decisión de no contaminación.

### 3.5 Infraestructura y F2

- F1 (15-Oct): prueba real histórica midió MAKER en el libro ~50 ms (GTC acuse 84 ms, visible WS 82 ms), cancelación 65 ms, FOK no casable 228 ms y **TOMADOR casado ≈215 ms desde el envío**; cancelación dentro del taker-delay imposible. (El paquete original decía «taker-in-book ~50 ms»: era el maker.) No repetir órdenes reales; vía de cancelar órdenes retenidas cerrada salvo evidencia nueva.
- F2 (desde 16-Oct): V4 y V7 en proceso separado, según reporte. Verificar modo efectivo shadow/dry-run sin cambiarlo. Tres pasadas de code review comunicadas. Primera conciliación con los «vigías» prevista para 17-Oct (`python3 analisis_f2_5m_barato.py --dia 2026-10-16`). Criterios F2→F3 CONGELADOS en `informes/ejecutor_baja_latencia_diseno_15oct.md` (no redefinir). Actualización 16-Oct 07:55Z: decisión→envío BTC con firmador aparte p50 0,45 / p90 5,45 ms (antes p90 286); envío inline desplegado para bajar del criterio p90 ≤5 ms; si no basta, tiempo real (SCHED_FIFO) pendiente de permiso de Javi. ref5 llega >1,5 s en el 25 % de cierres pero 0/52 eventos v4 se detectaron antes. No enviar órdenes.

### 3.6 Cementerio: no reabrir sin evidencia nueva

- Pares 5m maker OOS −0,050.
- Maker un solo lado.
- Copiar makers ganadores (no persiste).
- Copiar tomadoras persistentes.
- FV v1–v3 (no batían al mid).
- `LOWLOW-PAIR` indiscriminado.
- `BTC5M-FV-LONGSHOT` anterior tal como fue probado.
- Entrada con retraso deliberado.
- Vender un bid15 rancio.
- Cancelación de órdenes retenidas durante taker-delay.
- Caja de dos patas a 250–400 ms (−35/−179 $ comunicados; auditar unidades si se usa).

### 3.7 Sin empezar / baja prioridad

Caja altcoin (10 días, cifras comunicadas: XRP +$703, DOGE +$203, BNB +$53, BTC −$7.553, ETH −$1.824, SOL −$859), cajas anidadas con 4h, caja maker de dos patas y maker FV 4/4b. Priorizar estas líneas solo después de P0–P4; maker FV queda condicionado a FV V4 ≥5 días cronológicos válidos y revisión.

## 4. Prioridad operativa actual

> **Desde el 17-Oct manda `docs/FLUJO_DE_TRABAJO.md` v2** (roles, escalera de 7 peldaños hasta dinero real, ciclo diario, reglas de RAM/cuota, prioridades vivas que reordena a diario `cheap5m-objetivo-200k` en `docs/LIBRO_OBJETIVO_200K.md`). La lista P0-P7 de abajo es la del 16-Oct: P0, P1 y P2 ya están cerrados (DECISION_LOG 17-Oct).


1. **P0 — Recuperar `cosechar al abrir` A/B** con checkpoints y reporte, fuera de 06:00–09:00Z. Verificar cobertura antes de reanudar; solo 05–06-Oct se han comunicado como procesados.
2. **P1 — Diagnóstico barato de V7 sin señales BTC:** encontrar primer paso del pipeline en el que el conteo cae a cero: datos, feed, reloj, parser, filtros, registro o sequía/regimen.
3. **P2 — Preparar conciliación F2 del 17-Oct:** verificar modo shadow, recuperar criterios congelados y preparar comparación contra vigías sin órdenes reales.
4. **P3 — Mantener forward congelados de V4 y FV V4:** auditoría de métricas, sin ajustar sus reglas; observar drift.
5. **P4 — Wallet strategy dissection / fase 2 invisible:** después de A/B, salvo plan read-only independiente que no contamine universo o conclusiones.
6. **P5 — Si FV V4 acumula ≥5 días válidos:** especificación congelada maker FV 4/4b, revisión independiente y forward separado.
7. **P6 — Cartera de subestrategias y meta económica:** risk-economics modela contribuciones independientes, solapamientos y gap a 200k con medios existentes.
8. **P7 — Otras hipótesis:** altcoin boxes, anidados 4h y maker box solo tras resolver prioridades anteriores.

## 5. Agentes y autoridad

- `cheap5m-objetivo-200k` (17-Oct): **dueño del objetivo** 200 k€/año como suma; mantiene `docs/LIBRO_OBJETIVO_200K.md`, recorre los 10 ángulos y ordena el trabajo por valor de la información. Mientras no esté cargado en la sesión, `cheap5m-risk-economics` tiene su misión ampliada.
- `cheap5m-chief` = **la sesión principal** (un subagente no puede lanzar subagentes): sigue `docs/ROL_CHIEF.md`. Prioriza, decide, lanza un único job pesado y filtra lo que llega a Javi. Javi capitanea la investigación y decide.
- `cheap5m-repo-auditor`: solo lectura; fuentes, baseline, procesos y continuidad.
- `cheap5m-market-data-engineer`: calidad y contrato de datos; diagnósticos baratos.
- `cheap5m-event-causality-analyst`: precursor 15m, ask obsoleto, cronología.
- `cheap5m-wallet-intelligence-analyst` (agente 5): ingeniería inversa de wallets ganadoras para mejorar/adaptar nuestro código y superar benchmarks, no copiar fills.
- `cheap5m-alpha-researcher`: ordena hipótesis por valor de la información y **puede proponer a diario** hipótesis nuevas derivadas de los resultados del trabajo (Javi 16-Oct); el chief las filtra y las presenta junto a sus propias 10 propuestas; decide Javi.
- `cheap5m-execution-engineer`: único implementador de código experimental y de reanudación; no modifica V4 ni modo live.
- `cheap5m-statistical-validator`: validación independiente.
- `cheap5m-risk-economics`: plan económico de portafolio para alcanzar 200k mediante la suma de subestrategias de 5m barato, dentro de recursos existentes, con contabilidad rigurosa.
- `cheap5m-red-team-auditor`: intento independiente de refutar conclusiones.

## 6. Etiquetas permitidas

`REJECTED`, `DATA_BLOCKED`, `EXPLORATORY`, `PROMISING`, `DRY_RUN_VALIDATED`. La etiqueta `DRY_RUN_VALIDATED` no autoriza trading live. Ningún agente puede declarar 200k alcanzables sin modelo de contribución, capacidad, capital, solapamiento, incertidumbre y pruebas empíricas.

## 7. Reglas de ejecución para TODOS los agentes de la misión
- Bash solo para leer y consultar, salvo `cheap5m-execution-engineer`. Nada de `pgrep/pkill -f` con patrones propios (se encuentran a sí mismos).
- Análisis pesados: UNO en toda la máquina (lo asigna el chief), `nice -n 19 ionice -c3`, `ulimit -v 1500000` (2-3 GB solo con permiso del chief), nunca 06:00-09:15Z ni 22:15-22:30Z; antes de lanzar, MemAvailable > 2,5 GB y load < 16 (guard_ram reinicia observadores con <900 MB libres: pasó 3 veces el 17-Oct).
- No editar `ejecutor_rapido.py` sin `/code-review` en MEDIUM + tests: lo usa `medir_camino_caliente.py`, que envía órdenes reales.
- Cuota: máximo 3 subagentes a la vez; opus para objetivo-200k, validador y red-team cuando haya cuota, si no `model: sonnet` al lanzar; si un agente se corta por cuota, reanudarlo (SendMessage) o relanzarlo con el mismo encargo.
- EV siempre PONDERADO POR € (Σpnl/Σcoste) además de por unidad (trampa 17-Oct: media de cocientes infló H5M de ≈+0,064 a +0,142).
- Idioma: castellano de España; cifras siempre con n, IC, periodo y fichero de origen.
