# Plan del equipo — directiva de Javi 22-Oct 11:10Z (estructurado en olas)

Mandato (CLAUDE.md §1b): cada línea responde **capturar / explotar / dinero limpio**. Un negativo = siguiente variante, no cierre. Gates intactos, nada con dinero real sin `/code-review` + OK Javi + peldaño micro-real. Máx. 3 agentes a la vez, UN análisis pesado (nice 19, fuera de 06-09Z, RAM>2,5 GB).

Entradas nuevas de hoy: la selección adversa de B (`b_seleccion_adversa/INFORME.md` §A-F) da una palanca ETH/SOL/XRP (R2: cotizar solo con bid15 del mismo lado ≤3c sobre mi puja; R3 = R2 + ≥26 acc casadas en 30 s + hora ≥4 UTC; población +0,114 IC90 días (+0,079,+0,155), 5/5 días; BTC la rechaza −0,030) con forward en cron `40 10`.
F2 (V4+V7 dry-run con ejecutor rápido) estaba CAÍDO desde el 21-Oct 23:39Z (Rescale): relanzado 22-Oct 11:09Z (pids 26647 BTC, 26650 alts).

## ⭐ PRIORIDAD 1 (Javi 22-Oct 11:25Z): R2/R3 de la selección adversa → shadow en tiempo real + variante de B lista para `/code-review` + OK. Agente execution-engineer en curso; entrega `b_seleccion_adversa/R3_PRODUCCION.md`. La ola 1 (capturar V4/V7) se relanza cuando se libere un hueco (se paró para respetar el máx. de 3 agentes).

## OLA 1 — capturar (por qué V4/V7/V2/V3/V5 no se capturan) [en curso]
| Línea | Encargo | Agente |
|---|---|---|
| H01 V4 + ejecutor baja latencia (`informes/ejecutor_baja_latencia_diseno_15oct.md`, criterios F2→F3 fijados 16-Oct) | Reconciliar F2 vs vigías desde el relanzamiento; medir L (casado − recepción) con relojes del exchange; qué parte del 62 %→40 % es latencia (rival 150-300 ms) y cuál se gana con maker H23/H54 | event-causality |
| H05 V7 / H17-H19 V2,V3a,V5 | Causa última de «cero eventos»: el escalón del margen del 13-Oct (P90 −3/−5c en 6 monedas) ¿competidor que reprecia el 5m con el bid15? Buscar el margen en otro sitio (otras monedas, 15m→60m, umbral por moneda, ventana ms) | event-causality |
| H59/H53 colchón +0,02 | Aplicar parche a F2 solo tras `/code-review` del diff nuevo (RAM>2,5 GB, load<16) | execution-engineer (ola 2) |

## OLA 2 — maker/taker combinado y colas
| Línea | Encargo |
|---|---|
| H23 / H54 una-vía-por-evento | EN CURSO: demostración re-puja 150 ms (DEMOSTRACION_REPUJA.md). Después: brazo combinado maker→tomador a +60 ms sobre eventos emparejados (DISC no aditivo: +0,795 y +0,507) |
| H43 R5K + H46 | Garantizar la posición en cola: el registro solo guarda el top; falta L2 bajo el top y bid15 al pujar (cambio en B = `/code-review` + OK). H46: coger datos ya |
| H60 H23 altcoins | Extraer datos alts (`run_v2_dogebnb.sh`) |
| H39 MM-REPOSO-5M, H30 pares @mo-money | Simulación emparejada primero (cementerio: pares maker OOS −0,050); mecanismo distinto: direccional, no cosecha de pares |
| H37 salida maker tras barrida | Postproceso sobre rellenos H35/JOIN; REJECTED si EV con salida ≤ EV mantener − 0,02 |

## OLA 3 — poner en marcha lo ya medido
| Línea | Acción |
|---|---|
| H26 H5M (replicar) | R2/R3 de la selección adversa ES la réplica con cola y selección adversa acotadas; llevar R3 al brazo forward de B tras el gate de 10 días |
| H07/H34 FV como guarda defensiva del maker | Especificación congelada (semilla fija), forward separado |
| H45 H35-ESCALA | Corrida nocturna 00-06Z mientras existan los maker_ms de 17-18 Oct (extraer ya: rotan) |
| H55 FAV-ANIDADO / H56-58 | Más margen = ampliar universo y forward (corte ask 0,90-0,95 fijado desde 21-Oct), sin relajar el gate |
| H44 H5M-ALT, H35 DEEP_PEG | Esperar n: forward activo |

## Reglas de lanzamiento
1. Máx. 3 agentes simultáneos; el siguiente arranca al entregar el MD.
2. Cada agente deja manifest/checkpoint y entrega MD; el chief lee solo el MD final.
3. Cualquier cambio a B o a ejecutores reales: propuesta + `/code-review` + OK Javi.

## ⭐⭐ MISIÓN BTC-200K (Javi 22-Oct 11:40Z): «entrar a operar en BTC con alguna subestrategia que dé 200.000 €/año; el equipo no puede resignarse a decir que no se puede; tienen una misión y la tienen que cumplir a toda costa»
Hechos de partida (no son excusas, son el terreno): (a) el ejecutor de baja latencia YA existe en dry-run (F2: `f2_5m_barato_dryrun.py` + `ejecutor_rapido.py`, decisión→envío p90 0,41 ms); lo pendiente es F3 (real), que exige criterios F2→F3 + gates de la subestrategia + `/code-review` + OK. (b) El suelo del TOMADOR es físico y común: ~145 ms de taker delay + ida ~30 ms ≈ 180-215 ms; ser «igual de rápidos» es posible, más rápidos que ese suelo no. (c) El MAKER no paga ese retraso (alta 68 ms, cancelación 60 ms): la ventaja estructural de velocidad está en el lado maker con cancelación.
Palancas a perseguir en BTC (cada una: capturar / explotar / dinero limpio, gate intacto):
1. Filtro de selección adversa propio de BTC para el maker (rasgos Binance, flujo de tomadores, saltos Chainlink, bid15 en ms, libro L2) con simulador de libro real, split por días, placebo e inversión.
2. Maker→tomador una-vía-por-evento (H54) y H23 con re-puja a 150 ms: el modo en que los rivales «combinan» ambos.
3. V4/V7 con F2 en F3-ready: medir L real, cerrar la brecha 62 %→40 %, colchón H59, umbral H53.
4. Dimensionar la capacidad: bote BTC 12,1 k$/día; ≈4,5 % del bote = 200 k€/año; qué tamaño, cola y capital exige y qué parte de ese flujo es alcanzable.
5. Mecanismos de las wallets que ganan en BTC (H09/H24/H30): ingeniería inversa, no copia.
Cola: lanzar un agente por palanca en cuanto se libere un hueco (máx. 3 a la vez), empezando por 1 y 3.

Registro: H63-H68 en `REGISTRO_HIPOTESIS.md` («SUBESTRATEGIA BTC-200K»). Las cinco palancas = H63-H67; H68 = tomador en las demás monedas. Aclaración de velocidad (Javi 22-Oct): objetivo superar a los bots más rápidos en TOMADOR (BTC y resto) — se persigue llegando al suelo físico (~180-215 ms) y descubriendo cómo llegan ellos (H65/H24); VPS cerca del CLOB sigue DESCARTADO por Javi (17-Oct) salvo nueva decisión suya.
