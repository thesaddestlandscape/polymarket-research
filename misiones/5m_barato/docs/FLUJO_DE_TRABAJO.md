# Flujo de trabajo del equipo — 5m barato (v2, 17-Oct)

Objetivo único: **200.000 € netos/año como SUMA de subestrategias de 5m barato** (Javi 17-Oct: suma, no por
subestrategia). Todo el equipo trabaja para cerrar el hueco del libro `docs/LIBRO_OBJETIVO_200K.md`. La v1 (16-Oct, P0-P5)
está en git; sus prioridades están cerradas o integradas abajo.

## 1. Roles (quién hace qué; nadie aprueba su propio trabajo)

| Rol | Agente | Hace | No hace |
|---|---|---|---|
| Capitán | Javi | decide dinero real, capital, stakes, prioridades | — |
| Chief | sesión principal (`docs/ROL_CHIEF.md`) | lanza agentes, asigna el turno pesado, escribe REGISTRO/DECISION_LOG, despliega, /code-review, pide OK a Javi | delegar la decisión |
| **Dueño del objetivo** | `cheap5m-objetivo-200k` | libro del hueco, 10 ángulos, ordena TODO por valor de la información (VOI), propone las 3 pruebas siguientes | medir su propia propuesta como validada |
| Ideas | `cheap5m-alpha-researcher` | ≤5 hipótesis/día con mecanismo y regla congelable; auditoría de planteamiento de lo rechazado | implementar |
| Quién gana | `cheap5m-wallet-intelligence-analyst` | on-chain maker/tomador: mecanismo de ganadores y vendedores, debilidades, migraciones (régimen) | copiar fills |
| Relojes y causalidad | `cheap5m-event-causality-analyst` | carreras en ms, orden de eventos, look-ahead, lead-lag de fuentes | — |
| Datos | `cheap5m-market-data-engineer` | contratos y cobertura de datos (libro5_ms, multivenue_ms, m5_registro, on-chain, desenlaces), salud de loggers | editar |
| Constructor | `cheap5m-execution-engineer` | ÚNICO que escribe código experimental: simuladores, datasets, ejecutores en dev con tests | tocar producción, V4, F2 |
| Validación | `cheap5m-statistical-validator` | reproduce de forma independiente cada cifra que vaya a contar (script propio, ponderado por €, IC por días/cierre, placebo) | — |
| Ataque | `cheap5m-red-team-auditor` | busca la razón más fuerte por la que una señal es falsa antes de forward y antes de dinero | — |
| Capital y riesgo | `cheap5m-risk-economics` | rampas de stake pre-registradas, kill-switches simulados, capital necesario por escenario | — |
| Procedencia | `cheap5m-repo-auditor` | hashes, reproducibilidad, artefactos congelados, que nada se edita en caliente | — |

## 2. La escalera de una subestrategia (solo se cuenta como ingreso desde el peldaño 5)

1. **Idea registrada** (REGISTRO, `PENDING`): mecanismo falsable, regla congelada, gate, datos, coste.
2. **Descubrimiento** (DESC): medida en días de elección; resultado `EXPLORATORY`/`PROMISING`/`REJECTED`.
3. **Fuera de muestra** (OOS cronológico, días distintos) + **validador independiente** + **red-team**.
4. **Forward congelado** (vigía con hash; criterio fijado antes): ≥ los días de su gate.
5. **Micro-real** en la wallet dedicada (≤5 € de exposición, modo dedicado, `/code-review`, OK de Javi): mide cola,
   rellenos y comisión reales. Primera cifra que entra en el libro (escenario conservador).
6. **Live mínimo** (stake 2 € en la principal; whitelist + checklist de 6 categorías + `/code-review` + OK Javi).
7. **Rampa** pre-registrada 2 → 5 → 10 € … (`risk-economics`), con criterio de subida y de bajada fijado antes
   (Javi: demostrar y luego subir poco a poco, como las wallets que ganan).

Bajar de peldaño es automático si se incumple el criterio del peldaño en que está.

## 3. Ciclo diario (UTC) y turnos de máquina

| Hora | Qué | Quién |
|---|---|---|
| 00:00-06:00 | **Turno pesado nocturno** (uno solo): corridas largas de simulador/dataset | constructor |
| 06:00-09:15 | **Nada pesado** (racimo de crons de producción) | — |
| 09:30 | Lectura de vigías/forwards/Telegram de la noche y actualización del libro; elige las 3 pruebas del día por VOI | dueño del objetivo |
| 09:45 | El chief asigna: 1 trabajo pesado + ≤2 ligeros; encarga ideas si el libro lo pide | chief |
| 10:00-14:00 | **Turno pesado de día** (uno solo) + ligeros en paralelo | constructor / analistas |
| 14:00-18:00 | Validación independiente y red-team de lo que el día quiera contar | validador / red-team |
| 18:00 | Cierre: libro actualizado, REGISTRO/DECISION_LOG, checkpoint en memoria | chief + dueño |
| 22:15-22:30 | Nada (reinicio de RAM programado) | — |

## 4. Reglas de recursos (la RAM es el cuello de botella)

- **Un solo trabajo pesado (>1 GB) en toda la máquina**, asignado por el chief. Antes de lanzarlo: MemAvailable > 2,5 GB
  y load < 16; si no, esperar 10 min.
- Cada proceso de agente: `ulimit -v 1500000` (2 GB solo con permiso), `nice -n 19 ionice -c3`, un día cada vez,
  streaming, cachés por día con hash e idempotentes.
- **Máximo 3 agentes a la vez.** Cuota: opus para objetivo, validador y red-team cuando haya; si no, sonnet en todos
  (`model: sonnet` al lanzar). Si un agente se corta por cuota, se reanuda (SendMessage) o se relanza con el mismo encargo.
- Nunca: producción, órdenes, firma, V4, F2, screens/cron, `pgrep/pkill -f` con su propio patrón.

## 5. Definición de "hecho" para cualquier cifra

Comando reproducible + fichero; n y días; **EV ponderado por €** (Σpnl/Σcoste) además de por unidad; IC90 por días y por
cierre; sin los 2 mejores días y sin los 5 mejores cierres; placebo/inversión; precio ejecutable y reloj de RECEPCIÓN;
desenlace oficial con cobertura; supervivencia revisada; veredicto del validador. Sin esto, la cifra no entra en el libro.
Estados: `PENDING`, `EXPLORATORY`, `PROMISING`, `DATA_BLOCKED`, `REJECTED`, `DRY_RUN_VALIDATED`, `MICRO_REAL`, `LIVE`;
trabajos: `COMPLETE`/`PARTIAL`/`FAILED`/`BLOCKED`.

## 6. Prioridades vivas (17-Oct; las reordena el dueño del objetivo cada día)

| P | Pieza | Peldaño | Siguiente paso | Quién |
|---|---|---|---|---|
| 1 | Micro-órdenes maker reales H35 (ETH/XRP, ≤5 €) | 4→5 | construir modo maker en dev + /code-review + OK Javi (cuando baje la carga) | chief + constructor |
| 2 | Modelo de colocación maker (batir primeras 5 acc + rebate en ≥+0,05) | 2 | dataset + modelo DESC/OOS | constructor (en curso) |
| 3 | Vendedores del volumen tardío barato; migración de las 6 wallets de V7 | 2 | on-chain | quién gana (en curso) |
| 4 | Lead-lag multi-bolsa (Bybit +5-70 ms) | 2 | repetir con 1-2 días incl. horario USA | causalidad |
| 5 | H35 completo (15-16 Oct) y recálculo ponderado por € de H35/H12 | 3 | corrida nocturna con memoria | constructor |
| 6 | H39 MM-REPOSO (pares rotando) | 1 | tras P2 (mismo motor) | constructor |
| — | PRECIERRE (fuera de 5m barato): rampa de stake en seguimiento diario | 6→7 | vigía 09:40Z | risk-economics |

## 7. Comunicación

- Cada agente devuelve un reporte con estado, cifras con fuente, incertidumbres y siguiente paso exacto.
- Solo el chief escribe REGISTRO/DECISION_LOG; solo el dueño del objetivo escribe el libro.
- Javi recibe: el libro (hueco y suma por escenario), decisiones que solo él puede tomar, y lo que entra o sale de dinero.
