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
