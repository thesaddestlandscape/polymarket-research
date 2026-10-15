# Ejecutor dedicado de baja latencia — diseño (15-Oct, objetivo Javi: < 200 ms)

## KPI (definición única, medida con relojes del exchange donde existan)
**L = hora de casado de NUESTRA orden (timestamp del trade en el WS del CLOB / on-chain) − hora de RECEPCIÓN del evento disparador.**
Objetivo: **p50 < 200 ms, p90 < 250 ms**. Hoy (camino actual, medido 12-Oct): ~489 ms.

## Presupuesto medido hoy (15-Oct, VPS Helsinki)
| Tramo | Medida | Fuente |
|---|---|---|
| Evento Polymarket → nuestra recepción | p50 31 ms, p90 78, p99 345 | registro ms, 838 k filas q |
| Evento Binance (E) → nuestra recepción | p50 135 ms, p90 229 | registro ms, 129 k filas x (incluye desfase de relojes) |
| TCP a clob.polymarket.com | 2-8 ms (borde Cloudflare local) | curl ×5 |
| TLS nuevo | 20-180 ms | curl ×5 → **conexión SIEMPRE caliente** |
| Borde → origen → respuesta (conexión hecha) | ~50-100 ms ida y vuelta | curl ×5 |
| GTC post-only en reposo (alta) | P50 68-81 ms | órdenes reales 07-Oct |
| FOK (retraso del tomador incluido) | P50 213-216 ms; ~+135-145 ms sobre GTC | órdenes reales 07-Oct |

**Suelo físico del TOMADOR** desde nuestra recepción: decisión+firma ~3 ms + ida al origen ~30 ms + retraso del tomador ~145 ms ≈ **~180 ms** → < 200 ms ES ALCANZABLE solo si el camino caliente no gasta nada más (hoy gasta ~300 ms extra). Medido desde el evento en Polymarket: +31 ms → ~210 ms p50. Disparado por Binance: +135 ms → imposible < 200 desde Helsinki.
**MAKER** (alta 68 ms, cancelación 60 ms, sin retraso del tomador): ~35 ms desde recepción → holgura enorme; es la vía natural para todo lo que pueda ser maker.

## Dónde se pierden hoy los ~300 ms (a verificar en F0 con perfilado)
1. Lectura REST del libro antes de enviar (~1-1,5 s en live_trade; trampa "relleno más barato = malo").
2. py-clob-client en el camino caliente: consultas por orden (tick size, neg_risk, fee) y firma al vuelo.
3. Conexiones HTTP nuevas (TLS 20-180 ms).
4. Hilos de `observadores` compartidos / GIL, CSV intermedios, polling.

## Arquitectura
1. **Proceso propio** (no hilo de observadores): asyncio + uvloop; afinidad a un núcleo; `choom -n -500`; sin escritura a disco en el camino caliente (cola a un hilo escritor).
2. **Feed push**: WS de mercado del CLOB con conexión propia por par (5m+15m de la moneda), libro L2 en memoria; disparo por timestamp de RECEPCIÓN (el timestamp del WS es de lote, trampa 07-Oct).
3. **Precarga por mercado al abrir la ventana**: token ids, tick size, neg_risk, comisión, mínimo de acciones → cero REST en el camino caliente.
4. **Órdenes PREFIRMADAS**: rejilla de precios ±k ticks alrededor del precio esperado × tamaño fijo, firmadas EIP-712 al abrir el mercado (salt único por orden, expiración corta). Camino caliente = elegir la orden ya firmada y enviarla. Re-firma en segundo plano si el precio se sale de la rejilla.
5. **HTTP caliente**: un cliente persistente (keep-alive, HTTP/2 si el borde lo acepta), latido cada pocos segundos para no perder la sesión TLS; cabeceras L2 (HMAC con timestamp) calculadas en µs justo antes del POST; POST /order directo, sin envoltorio.
6. **Estado de riesgo en memoria**: circuit breakers, freno diario, whitelist y kill-switch leídos en segundo plano cada ≤1 s; si el dato tiene >2 s → NO opera (fail-closed).
7. **Ledger de intención antes del envío** + idempotencia por (mercado, lado) + reconciliación por WS de usuario y on-chain; estado incierto → kill.
8. **Medición integrada**: cada orden guarda t_recepción_evento, t_decisión, t_envío, t_respuesta, t_casado (exchange) → KPI L en el ledger.

## Casos límite (orden CLAUDE.md)
Dinero no cuadra → parar · API a medias → estado recuperable por ledger + consulta de orden · doble ejecución → idempotencia · datos viejos → fail-closed (>2 s) · límites del exchange (min 5 acc / $1, tick, decimales) precalculados · reinicio → ledger persistente.

## Fases
- **F0 (sin dinero)**: perfilar el camino actual paso a paso (dónde van los 489 ms) + prototipo del camino caliente en dev contra endpoints sin efecto (GET /time, /book) para medir HTTP caliente vs frío.
- **F1 (órdenes reales a coste ~0, requiere OK Javi)**: GTC post-only lejos del precio + cancelación, y FOK a precio que no puede cruzar con tamaño mínimo (ojo trampa 07-Oct: una FOK "imposible" puede llenarse si el precio cae: usar precios que no puedan casar) → KPI L real de alta/cancelación/FOK con el camino caliente.
- **F2 (dry-run)**: conectar V7 (disparo 15m) y la pata de V6 al ejecutor en DRY_RUN, registrando el KPI simulado contra el registro ms.
- **F3 (dinero, requiere gates de la subestrategia + /code-review medium + OK Javi)**.
- **Palanca externa (decisión Javi, pendiente #4)**: VPS junto al origen del CLOB (quita ~25-50 ms de ida y vuelta); para Binance, el feed ya llega con 135 ms → los disparadores que valen < 200 ms son los de POLYMARKET (V7, 15m), no los de Binance.
