# Pendientes 5m barato — repaso 16-20 Oct (generado 20-Oct ~09:10Z; fuente: DECISION_LOG, REGISTRO_HIPOTESIS, checkpoints 16/17/19/20-Oct)
Estado: HECHO · EN CURSO (agente/proceso vivo) · PENDIENTE (sin lanzar) · JAVI (decisión tuya). Actualizar al cerrar cada línea.

## EN CURSO hoy
| # | Pieza | Quién / dónde | Siguiente paso |
|---|---|---|---|
| 1 | H47 (SIM-REAL, micro-órdenes maker reales, wallet dedicada 0x659a…297F, presupuesto 5 $) | A real HECHO 20-Oct (40/40, 0 rellenos por diseño, kill arreglado: dev 027162df21+9aee8beff8+a6d42b178d). B: ensayo en seco programado ≥09:20Z | Revisar el seco; OK final de Javi para enviar B; luego rampa 2→5→10 € con n/IC/días |
| 2 | V4 "comprar lo bueno" (P2) | HECHO 20-Oct: NO CAPTURABLE como tomador (rival compra a 49-57 ms del trigger, 188 ms antes que nuestro casado; 77 % de las ganadoras perdidas se pierden con cualquier latencia ≥145 ms); maker H23 n insuficiente y simulador sin calibrar. Informe experimentos/5m_barato/v4_comprar_lo_bueno/informe.md | Siguiente: congelar umbral 0,02 como V4b en SOMBRA (exploratorio, sin corrección de multiplicidad); micro-orden maker solo tras H47-B |
| 3 | H43 R5K: A1 HECHO (h43_unidades.py, 13 tests), A5 HECHO (18-Oct cuadra 1:1 con on-chain), A6 ver sí / operar no (20-Oct) | agente execution-engineer | A2 sidecar vigía = /code-review + OK Javi; A6: shadow standalone (OK Javi), filtro de régimen H50, micro-orden solo tras H47-B + /code-review + OK |

## PENDIENTE (sin lanzar) — por orden de prioridad (Javi 19-Oct: 1 H45+H47, 2 V4, 3 H43 A6, resto espera)
| # | Pieza | Detalle / condición |
|---|---|---|
| 4 | **Modelo de colocación** (datalogs/m5_maker_colocacion) | Manifest `BLOCKED` a las 22:00Z del 19-Oct (se pasó del límite). Relanzar con lanzador idempotente (`experimentos/5m_barato/colocacion_17oct/lanzar_modelo.py`): hueco ≥09:15Z, Mem>2,5 GB, load<16, nice |
| 5 | H45 H35-ESCALA (5/25/50 acc, OOS 14-18 Oct) | `PENDING`: decide si la capacidad alt es ~9 k o ~90 k €/año; sin esto no hay camino a 200 k |
| 6 | H44 (H5M-ALT ETH/SOL/XRP ponderado por €), H46 (R5K normalizado por moneda), H50 (operar solo si población del día positiva) | `PENDING`, lectura/cómputo ligero |
| 7 | wallet-intelligence AMPLIADO (todas las wallets cripto ganadoras + bonereader, 0x502b, @flippingsharks como referencia H39) | Fases: universo → arquetipos → réplica. Directiva latencia "lo imposible" (VPS cerca del CLOB DESCARTADO, 17-Oct) |
| 8 | A1-A6 de H43 restantes y R5K "que funcione cueste lo que cueste" (§1b) | Tras el informe del agente 3 |
| 9 | Informes R5K (`r5k_camino`) y rampa H5M (`h5m_rampa`) "SIN verificar por el chief" (19-Oct 13:50Z) | statistical-validator independiente |
| 10 | H25b (filtro tomador V4 por nocional, preregistrada) y H23 (maker pre-posicionado V4/V7) | `OPEN`; la capacidad de H23 es ~2-3 $/evento: prioridad baja salvo informe V4 |
| 11 | H09 "lo invisible" (wallets: mecanismos que anteceden a la operación) | `PENDING_DEPENDENCY` de A/B (A/B ya REJECTED: desbloqueada) |
| 12 | FV v5 (H34) + BTC5M-FV-LONGSHOT | v5 construida (75 tests); falta validación independiente; FV Φ(z) sobreconfiado: calibrar contra el mid |
| 13 | Desfase sello WS→recepción (te→rx 21/38/161 ms) | Parcial: lector hijo a nice -10 (17-Oct, p90 280→115). Falta medir red vs proceso y lector dedicado solo 5m en ventana |
| 14 | Rampa de stake 5m barato 2→5→10 € todas las monedas (Javi 16-Oct) y rampa PRECIERRE 2→5→10 pre-registrada (≥40 órdenes post-arreglo, ≥10 días) | Solo con gates + /code-review + OK Javi por peldaño |
| 15 | H39 MM-REPOSO-5M-V1, H38 markout como parada | `PENDING`; dependen de H47 (calibración) |
| 16 | Equipo "solo ganar"/bot arbitraje cripto 200 k€ | Misión NUEVA aparte, alcance sin definir (Javi) |
| 17 | Rotación de los 10 CSV `*_fase0` fuera de git + bajar carga de los vigías | `project_push_bloqueado_ya_decidido_100mb_19oct`; OK Javi para vigías |
| 18 | PRECIERRE: vigilar FOK muertas nuevas (SOL 5m, tope 0,65 = banda) | Subir tope 5m solo con n≥15 y EV>0 |

## JAVI (decisiones tuyas abiertas)
- VPS: más RAM/CPU (8 GB+) o parar `multivenue` (carga ~8 de base, picos 42 en 06-09Z). Dejado "hasta que lo veas".
- OK final antes de enviar el escalón B; escalado con beneficios con OK por peldaño.
- CSV WM reconstruido, alcance del equipo "solo ganar".

## CERRADO (no reabrir sin mecanismo nuevo)
Cosechar al abrir A/B/v2 (REJECTED), pares maker/LOWLOW-PAIR, salidas tras relleno H37/H40/H41, predicción Binance como defensa del maker, "Binance en contra" (era look-ahead), cancelación durante taker-delay (cerrada), V7 sin eventos = régimen, lead-lag multibolsa (Binance manda), H26 como estrategia propia: DATA_BLOCKED (solo vehículo H35-alts positivo fuera de muestra: +0,064/€).

## A6 shadow (lanzado 20-Oct 09:59Z, screen `a6shadow`, nice 5, `datalogs/a6_shadow/`) — dos cautelas, cómo se cierran
- **Colas de relleno sin calibrar** (opt / base 0,5 de profundidad / cons 1,0): NO se cierra con datos de hoy, solo H47-B (rellenos reales) puede calibrarlas. Criterio fijado ahora: tras H47-B, por cola, |tasa de relleno shadow − tasa real| ≤ 8 pp y acuerdo puja a puja ≥ 0,70 (mismo gate que H47); se adopta la cola que lo cumpla, si ninguna → el shadow se reporta solo como rango [cons, opt]. Hasta entonces ninguna cifra de EV del shadow se cita con una sola cola.
- **Reconexiones del WS con load ~30**: causa probable (no confirmada) = `nice 19` dejaba al proceso sin CPU y el servidor lo desconectaba; subido a nice 5 (renice en caliente + `pipeline_watchdog.py::SCREEN_RESTART`, commit 935ad302cb). Verificación: contar filas `gap` por hora a load alto durante ≥24 h; si siguen, leer el `motivo` y actuar sobre él (reconexión con resuscripción + backfill de trades).

## Flujo escalonado de agentes (20-Oct ~11:30Z, Javi: "no consuman todos los tokens de la sesión")
Fase 1 (vivos, con tope de llamadas): anticipación V4 (event-causality-analyst, paso 1 y informe parcial) + calibración de colas del shadow (statistical-validator). 
Fase 2 (esperan, se relanzan con su prompt al terminar la fase 1; el chief decide):
- **H23 maker en dry-run** (execution-engineer): espera la calibración de colas (necesita el factor de cancelación para su simulador y la cancelación rápida). Entregables: spec H23 v1 congelada con cancelación rápida, proceso sombra persistente, paquete REAL listo (OK final de Javi + H47-B + /code-review).
- **Capacidad y camino de escala H23** (risk-economics): espera los hallazgos de anticipación (paso 1) para no duplicar palancas. Entregable: experimentos/5m_barato/h23_capacidad/informe.md.
Fase 3: escalón B real de H47 (tras calibración; OK de Javi dado) y rampa de stake por peldaños.
Regla de tokens: un agente pesado a la vez salvo lecturas; cada agente con tope de ~35-45 llamadas, resultados a fichero y solo agregados al contexto, informe parcial por fase.

## Rampa por subestrategia + revisión semanal (Javi 20-Oct)
- Rampa 2→5→10 € y siguientes peldaños (con ganancias) para CADA subestrategia: H55 favorito (plantilla en experimentos/5m_barato/rampa_plantilla/, agente a6e98dc39399e2811), H35/H47 alts, H23 maker, R5K, V4/V4b; y PRECIERRE 5m y 15m (rampa pre-registrada 17-Oct). Objetivo ≥200 k€/año limpios DE CADA UNA.
- **Revisión semanal ~27-Oct:** por subestrategia, ¿cumple n, IC90 por días, EV ponderado, sin 2 mejores días y kill? ¿sube de peldaño? Con datos reales del día, no de memoria.
- Pendiente en cola: risk-economics (capacidad y camino de escala H23 y del resto) una vez salgan H55/H23; calibración de colas por moneda (agente a0df08cc219a82d3c); vigía H53/H54/H55 (agente a6e98dc39399e2811); /code-review del paquete H23 real tras H47-B.

## Dashboard / escritorio 5m barato (Javi 20-Oct, PARA MÁS ADELANTE — registrado, no empezar sin orden)
- Javi quiere un escritorio (dashboard) **exactamente igual que el de cripto** (`dashboard_server.py`, http://37.27.249.72:8888, screen `dash`) pero **adaptado a la misión 5m barato**, para ver cómo vamos: B real (H47: tanda, suelo, saldo de la wallet 0x659a…297F, rellenos, PnL realizado/abierto, KILL), supervisor `h47sup`, vigías (H5M, V3/V4, H55/H53, R5K, H15), H23 (replay/sombra/kill V3), PRECIERRE 5m/15m, rampa y gates por subestrategia.
- Reglas al hacerlo: copiar el diseño del dashboard de cripto, **no mezclar datos con el repo weather ni con el dinero de sports** (trampa registrada), solo lectura, puerto propio, screen registrada en `pipeline_watchdog.py` y `verify_deploy.py::SCREENS`, `choom` no hace falta (sin dinero). Antes de construir: decisión ladder (reusar `dashboards_consolidado.py`).

## Maker de liquidez con rewards (Javi 21-Oct, PARA MÁS ADELANTE — registrado, no empezar sin orden)
- Idea: cotizar como maker de LIQUIDEZ para cobrar el programa de rewards de los 5m: gamma de los 5m (ETH/XRP, 21-Oct) da `rewardsMinSize 50`, `rewardsMaxSpread 4,5` (c) y `feeSchedule.rebateRate 0,2` (20 % de la comisión del tomador al maker).
- Hecho verificado 21-Oct: B (size 5, pujas 0,05-0,40, cancela rápido) NO puntúa; `get_total_earnings_for_user_for_day` del CLOB devuelve [] los 13 días 09..21-Oct y la contabilidad no ve ninguna entrada distinta de depósito/redención. El rebate por relleno a 5 acc y p=0,2 ≈ 0,011 pUSD (≈0,7 pUSD en 67 fills): despreciable.
- No verificado: que ese endpoint cubra también el rebate de maker. Tamaño de la recompensa por mercado (`get_current_rewards`/`get_raw_rewards_for_market`) sin medir.
- Siguiente paso cuando Javi lo ordene: medir en SIMULACIÓN con libros ms existentes cuánto pagaría puntuar (≥50 acc a ≤4,5c del medio) frente a la selección adversa y al capital inmovilizado; preregistrar antes. Nada de dinero real sin gate + /code-review + OK de Javi. B real no se toca.

## H39 / H39b — MM en reposo (cotizar ambos lados en continuo) — PENDIENTE (Javi 22-Oct, empezar SOLO cuando B esté masterizada)
- Registro: H39 MM-REPOSO-5M-V1 en `REGISTRO_HIPOTESIS.md` (PENDING desde 17-Oct). Variante **H39b** propuesta 22-Oct por los agentes de B: ETH 5m (luego ETH/SOL/XRP), ambos lados en banda 0,30-0,70, clip 5 acc, inventario tope 15 acc, T 290→50 s, reequilibrado como regla; referencia 0xf074dc84 y 0x0ab01745 (ETH, 100 % maker, +0,85..+1,5 %/vol, exploratorio, elegidas viendo el test).
- Orden de Javi (22-Oct): primero MASTERIZAR B (confirmar o descartar todas sus vías); H39/H39b es subestrategia pendiente de 5m barato, no se prepara ahora (si resultara ser sub-estrategia de B, se replantea). NO preregistrar ni simular antes.
- Lo ya sabido que condiciona: B va DELANTE en la cola (`b_perdidas_22oct/cola_posicion/INFORME.md`), así que la cola no la bloquea; pero la competencia se retira antes del print (firma de selección adversa, hipótesis); falta medir cancelación en 0,30-0,70; el simulador maker aún no reproduce la cola (bloqueo de H39). Pares/cobertura posteriores al relleno REJECTED para B (`pares_huecos/INFORME.md`). Probar con micro-órdenes reales: /code-review + capital + OK Javi.

## FAV-15M-ETH — REUBICADA 26-Oct a la misión 15m v5 (Javi: «quizá sea el mejor sitio»; ver informes/m15v5_libro_investigacion_13oct.md, sección 26-Oct). Se vigila desde el LIBRO DE SUMA, fila propia, sin sumar con B — maker en favoritos 15m ETH banda 0,70-0,99
- Origen: separada de B por la validación independiente (casos/VALIDACION_INDEPENDIENTE_26OCT.md §4): es OTRA mecánica (maker en favoritos 15m, no 5m barato) y NO se suma al techo de B. Sale de mapa_escala/INFORME.md (15m ETH favoritos 0,70-0,99: flujo ~79 k€/día, pool de beneficio 750-850 €/día por banda; 1 % de cuota ≈6 k€/año, 5 % ≈29 k€/año, sin estrés, brecha de ejecución 0, cuota SIN medir) y de F2/F3 (15m ETH [0,90-0,95) +0,031-0,032 población; con puja virtual 5 acc al final de cola −0,003, IC90 cierres −0,023..+0,022; capacidad F3 ≤1/3/11 k pUSD/año).
- Estado: EXPLORATORY, 0 € validado. Contradicción abierta a resolver ANTES de nada: población +0,03 vs puja propia ≈0/negativa (fav 60m puja propia −0,0575); fallos agrupados (19,6 % cierres con fallo ≥0,90).
- Siguiente (cuando Javi lo ordene): medir cuota maker alcanzable (TP2) y EV de puja propia por € con on-chain (verdad) en 15m ETH 0,70-0,99 por banda de 0,05, ≥10 días, IC por cierre/día; después extender a otras monedas. Incluir en el LIBRO DE SUMA de RE-CEMENTERIO como fila propia, sin sumar con B.
- Dónde encaja: la sesión principal decide si cuelga de 5m barato (decisión Javi: sí, como subestrategia nueva) o de la misión 15m v5 (`project_mision_15m_v5_13oct`); no mezclar universos sin demostrar el mecanismo.

## NUEVA SUBESTRATEGIA CANDIDATA (26-Oct, hallazgo de wallet_mecanismos_26oct/INFORME.md): CARRY-FAV-5M «maker paciente en el favorito ≥0,70»
- Hallazgo (EXPLORATORY, desenlace oficial 100 %, EV ponderado por €): las dos ganadoras reales ganan comprando COMO MAKER el FAVORITO, no en la banda barata. mo-money: +10.264 $ en selección (06-14 Oct) y +1.634 $ OOS (EV +0,006, IC −0,045..+0,041, se seca: últimos 4 días negativos); todo su beneficio sale de 0,70-0,99 (0,70-0,90 +0,036 OOS IC>0; ≥0,90 +0,064 en 7/7 días); pierde en lo barato, en tomas y pares. pspspsps5 (W): +5.438 $ OOS (EV +0,027, IC +0,016..+0,039, 6/7 días), maker en ≥0,90 (+0,034, 7/7) y 0,10-0,30 (+0,13, IC cruza 0).
- Lectura (inferencia SIN probar): ventaja de CALIDAD DE RELLENO, no de predicción. Población maker en el mismo carry ≈+0,003 y nuestra puja virtual de final de cola −0,035/−0,071 (f3_carry; ojo: etiqueta 'pes' pesimista, RT 26-Oct: opt +0,009). Requisito para replicar: órdenes viejas (~5 s) y 2-4 ticks bajo el mejor bid (replica_ganadora adenda 2). A escala de W exige ~17 k$/día de capital rotando.
- Refutado hoy: información del 15m, velocidad/precio rancio como tomador, rebate (0,3 % del coste de W), rewards, barrido compartido (era look-ahead). Pendiente: H2 vendedor-vs-comprador complementario, H3 BTC <0,10 con MM presente, H4 MM favorito 22-25 Oct (preregistradas).
- Implicación: la banda 0-0,30 no es donde ganan los que ganan. Ampliar el programa a favoritos 5m (≥0,70) y calibrar con on-chain; relaciona con FAV-15M-ETH (misión 15m v5). Sin dinero real: la medición de la cola real exige micro-órdenes F5 (OK Javi + /code-review + wallet dedicada); antes, simulación con la calibración de la etiqueta virtual.

## Frente 4 — micro-órdenes F5 reales en favoritos ≥0,70 (PENDIENTE, anotado 27-Oct, OK Javi)
- NO es B. Medición de fill-ability/selección adversa en favoritos, no prueba de rentabilidad: hoy 0 rellenos reales, solo transfiere el método.
- Evidencia previa: regla F5 de A1 EXPLORATORY (sin 3 mejores días +6.260 $, bajo el mejor bid IC cruza 0, 99 % ETH); frente 3 (moneda vs hora) en curso 27-Oct.
- Requisitos antes de pedir OK: frente 3 resuelto, ventanas reales (no etiqueta generativa), diseño con presupuesto máx. de pérdida fijado de antemano, /code-review, wallet dedicada, OK Javi con importe.
- MANDATO Javi 27-Oct: el equipo debe RESOLVER la selección adversa de B y hacer click con la(s) estrategia(s) que den dinero; no resignarse.
