# Estado de investigación — BTC 5m barato

> **Correcciones verificadas por la sesión principal (16-Oct 08:10Z):** F1 corregido (tomador ≈215 ms; 50 ms es el maker); placebo de wallets −0,003; @mo-money 1ª pata 22,6 % vs 17,1 %; «−0,002» = EV de v1/v4 en el mismo periodo que V2; «n=40» = G1 ejecutables; rutas exactas en `MAPA_ARTEFACTOS.md`; restricción de capital real (34,59 $, stake 2 €, sin recargas) en `CLAUDE.md` de la misión. Lo demás, tal cual lo escribió Javi.

**Corte:** 2026-10-16 07:40Z. **Fuente:** parte del investigador. Los números son comunicados y requieren reproducción desde los artefactos originales salvo que exista referencia explícita a una conciliación verificable.

## Resumen ejecutivo

- Objetivo familiar: **200.000 € netos/año como suma de subestrategias de BTC 5m barato**.
- Beneficio anual validado: **0 €**. Ninguna candidata ha pasado sus gates de validación.
- Estimación de discovery sin validar: ~60 k€/año, compuesta por V7 (~28–37 k€) y V6 (~30 k€). No es forecast; no asumir aditividad ni capacidad conjunta.
- Prioridad inmediata: recuperar `cosechar al abrir` A/B; diagnosticar los eventos ausentes de V7; mantener forwards congelados; preparar conciliación F2 del 17-Oct.

## 1. Subestrategias vivas / forward congelado

| Candidata | Función | Estado comunicado hasta 15-Oct | Gates / conclusión |
|---|---|---|---|
| V4 (v1 corregida) | Compra pata 5m cuando existe señal de valor relativo `bid15(s) - ask5(s) - commission` (confirmar código) | OOS desde 06-Oct: 43 señales, 17 ejecutables, +€8,36, EV +€0,21/€. Nueve días | 4/10. Un día aporta ~180% del PnL; los últimos tres días por debajo del 50% del EV previo (`DRIFT`). Hacia n=40/gate próxima el 27–28-Oct según informe; comprobar conteo real y gate exacto. Mantener congelada. |
| V2 | Todas las señales, hasta 3 por mercado | Desde 12-Oct: 5 mercados, −€2,57, EV −€0,18 | 0/7. Comunicada como peor que V4 en periodo común; el «−0,002» es el EV de v1/v4 en el MISMO periodo (4 mercados, −0,02 €). |
| V3/V3a | V4 + filtro Binance 5 s | Desde 12-Oct: 1 mercado, −€2,12 | 0/7. Sin n. |
| V5 ORIGEN15M | Señal cuando el desajuste nace del timeframe de 15m | Desde 14-Oct: 1 señal, 0 ejecuciones | 3/11. Sin n. |
| V6 FOK_VUELO_BTC | FOK en vuelo cuando cae el ask | Desde 14-Oct: 1 ejecución, −€2,12 | 0/7. Discovery estima ~30 k€/año, no validado; investigar por qué en discovery ganaban las oportunidades “visibles”. |
| V7 DISPARO15M_BTC | Disparo con operaciones/cambio del 15m (exacta regla: verificar) | Discovery: 8/8 días positivos, EV +1,99; cota exploratoria ~€28–37k/año. Forward desde 14-Oct: 0 ejecuciones; no hay evento BTC en registro desde 13-Oct | Sin gate favorable acreditado. Prioridad: diagnóstico barato del pipeline vs señal seca/cambio de régimen. |

**Nota sobre V4:** «n=40» es el gate G1 = 40 EJECUTABLES (hay 17; salen ~2/día → ~27-28 Oct). Las 43 son señales; ejecutables = las que rellenan a +215 ms.

## 2. FV V4

Datos comunicados en solo dos días cronológicos (el rango exacto empieza en un registro indicado como 05:50; verificar fecha/huso):

- R² del movimiento del mid a 3 s: 0,28 y 0,29.
- ΔBrier frente al mid: −0,003 en ambos días.
- Como taker con margen de 0,05: n=457, EV +€0,095/€.
- Resultado diario comunicado: +€0,049 y +€0,142.

Auditar qué cuenta `n`, definición y signo de ΔBrier, muestra, horizonte, umbral, benchmark, calibración, fees, fill model, latencia y si hubo selección sobre la misma muestra. Es la candidata nueva más prometedora, pero solo exploratoria tras dos días. Mantener forward congelado. Si aguanta ≥5 días cronológicos válidos, revisar una especificación maker FV 4/4b aparte; no implica validación automática.

## 3. Wallets ganadoras: indicios a auditar

- EV comunicado para compras BTC según precio: +€0,044/€ por debajo de 0,10; +€0,082/€ en 0,10–0,20. Revisar periodo, universo, costes, selección de wallet y si el dato estaba disponible antes de entrar.
- Carteras seleccionadas por rendimiento del 05–09-Oct mantuvieron +€0,057/€ en 10–14-Oct, IC90 por días +€0,022 a +€0,087, frente a un **placebo de −0,003** (`DL/m5barato_mision/baratas_informe.txt`). Reproducir antes de usar: en makers H5M la selección por resultado NO persistió (14-Oct).
- `mo-money` (0x32ed2e54…): +$10,4k en diez días; pares −$15,9k, dirección +$26,3k → maker DIRECCIONAL, no cosechador. Su primera pata maker barata (≤0,30) acierta **22,6 % frente a un precio de 17,1 % (+5,5 pp, igual en SEL y TEST)** (`analisis_mo_money_pares_5m.py`).
- Prioridad del agente 5: diseccionar estrategias completas y fuente del PnL, saber qué hacen antes y cuándo deciden, detectar debilidades y diseñar una política propia mejor, adaptada al código existente, que pueda superarles en comparación OOS. No copiar fills públicos una vez ejecutados.

## 4. Trabajos incompletos

### Cosechar al abrir — A/B

- A: BTC 5m general.
- B: BTC 5m barato con defensa de 15m.
- Los dos análisis del 15-Oct murieron con la sesión tras procesar solamente el 05 y 06-Oct; no hay informe final.
- Script y rutas exactas en `docs/MAPA_ARTEFACTOS.md` §2: `analisis_5m_cosechar_apertura.py` (fix 340755d55f), comando documentado `cd /root/polymarket-research && nice -n 19 ionice -c3 python3 analisis_5m_cosechar_apertura.py`; cachés borradas el 15-Oct al corregir (la carpeta `DL/m5_cosechar_apertura/` no tiene `mercados_D.csv.gz`), así que reanudar = recalcular desde 05-Oct. Leer su argparse/cabecera y añadir manifest/checkpoint ANTES de la corrida larga; prueba ligera de 1 día primero. Trabajo pesado fuera de 06:00–09:00Z.

### Fase 2 «lo invisible» de wallets baratas

No ha arrancado. Su dependencia es `cosechar al abrir` A/B. Primero preparar contrato de datos, queries y especificación read-only; ejecutar el análisis completo después de A/B. Solo ejecutar en paralelo si el chief deja por escrito cómo se evita contaminación de universo, I/O y conclusiones.

## 5. Infraestructura F1/F2

- F1 del 15-Oct (órdenes reales, NO repetir): MAKER en el libro ~50 ms (GTC acuse 84 ms, visible WS 82 ms), cancelación 65 ms, FOK no casable 228 ms, **TOMADOR casado ≈215 ms desde el envío**; cancelación dentro del taker-delay imposible ("pending/delayed"). [Corregido 16-Oct: el original decía «taker-in-book ~50 ms», que es el maker.]
- F2 arrancó el 16-Oct en proceso separado con V4/V7 según el parte. Confirmar shadow/dry-run mediante configuración y logs; no cambiar el modo. Tres code reviews comunicados. Primera conciliación con vigías prevista el 17-Oct. Recuperar gates F2→F3 originales y congelados.
- Medición decision→send con firmador separado pendiente, con referencias temporales 07:30 y 07:45; resolver qué significan a partir de logs. Cualquier instrumentación debe ser mock/shadow y no enviar órdenes.

## 6. Cementerio — no reabrir por renombrado

- Pares 5m maker: OOS comunicado −0,050.
- Maker de un solo lado.
- Copia de makers ganadores: persistencia no demostrada.
- Copia de tomadoras persistentes.
- FV v1–v3: no batían al mid.
- LOWLOW-PAIR indiscriminado.
- BTC5M-FV-LONGSHOT anterior.
- Entrada con retraso deliberado.
- Venta de bid15 rancio.
- Cancelaciones armadas dentro del taker-delay.
- Caja de dos patas a 250–400 ms (−35/−179 $ comunicado; validar antes de reutilizar la cifra).

Reabrir solo por mecanismo distinto, dato nuevo o defecto concreto de validación.

## 7. Hipótesis sin comenzar / prioridad baja

- Caja de altcoins: pastel de diez días comunicado: XRP +$703; DOGE +$203; BNB +$53; BTC −$7.553; ETH −$1.824; SOL −$859. Auditar, no desplazar prioridad principal BTC.
- Cajas anidadas con 4h.
- Caja maker en dos patas.
- Maker con valor justo (4/4b), depende de FV V4 sostener al menos cinco días cronológicos válidos y pasar revisión.

## 8. Próximas decisiones

1. Recuperar A/B `cosechar al abrir`, con checkpoints, informe final y reanudación idempotente, fuera de 06:00–09:00Z.
2. Diagnóstico ligero del cero de V7: último evento por fuente; conteos antes/después de filtros; heartbeat, reloj, parser, registry y logs. Identificar primer punto donde el conteo BTC cae a cero.
3. Preparar reconciliación de F2 para 17-Oct sin cambiar su modo ni ejecutar órdenes.
4. Mantener forwards V4/FV V4 congelados y verificar la deriva.
5. Completar fase 2 wallet «lo invisible» tras A/B; disección y mejora, nunca copia.
6. Si FV V4 alcanza ≥5 días válidos, congelar propuesta de maker FV 4/4b para revisión independiente.
7. Risk-economics construye una hoja de ruta hacia 200k como suma de subestrategias BTC 5m barato, con contribución incremental, overlap, capital, capacidad y medios existentes.

## 9. Definiciones contables que no se pueden mezclar

- `EV/€ risked`: PnL esperado relativo al capital perdido o comprometido en el denominador, según definición explícita.
- `ROI on committed capital`: PnL / pico o capital comprometido medio (definir cuál).
- `PnL/trade`, `PnL/market`, `PnL/day`: unidades distintas.
- `Signal`, `market`, `order`, `fill`, `leg`, `pair`, `day`: muestras distintas.
- Beneficio histórico de wallet ≠ PnL atribuible al mecanismo estudiado.
- Señal o fill teórico ≠ oportunidad ejecutable ni fill real.
- PnL validado actual de familia: cero hasta que al menos una subestrategia pase gates congelados.
