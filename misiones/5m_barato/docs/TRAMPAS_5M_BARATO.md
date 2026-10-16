# Trampas ya cazadas que afectan a 5m barato — lectura OBLIGATORIA antes de concluir, refutar o construir

Extracto del CLAUDE.md del proyecto (sección "🪤 Trampas ya cazadas", que manda si hay duda) + lecciones de la misión.
Cada línea es un error real que ya costó días o dinero.

## Latencia y ejecución (medido, no supuesto)
- **F1 15-Oct (órdenes reales, NO repetir)**: GTC post-only acuse 84 ms, visible en el WS 82 ms → en el libro ~50 ms del envío
  (MAKER); cancelación 65 ms; FOK no casable 228 ms; **TOMADOR casado ≈215 ms desde el envío** (237/247/252 ms hasta el print).
  "~50 ms" es del maker, NUNCA del tomador. Firmas prefirmadas válidas ≥120 s.
- Una orden tomadora retenida en el taker delay NO se puede cancelar ("pending/delayed"): vía cerrada.
- FOK/FAK pagan ~145 ms de retraso del tomador aunque no crucen. El maker tiene ~145 ms de ventaja estructural.
- Una FOK "que no puede llenarse" SÍ se llena si el precio cae hacia ella: ninguna orden marketable es coste 0.
- Rellenarse más barato que el ask de la decisión es mala noticia (selección adversa medida con dinero real).
- El `timestamp` del WS del CLOB NO es la hora del evento (sello de lote, hasta 468 ms antes de nuestro envío): ordenar por RECEPCIÓN.
- Feed RTDS de actividad llega ~0,9 s tarde: disparar por el WS del CLOB, nunca por RTDS.
- EV/€ que SUBE con la latencia no significa que esperar sea mejor: comparar PnL TOTAL y emparejar eventos (subestrategia 9 descartada).
- F2 16-Oct: firmar dentro del proceso del libro llevaba decisión→envío a p90 286 ms; un hilo en núcleo compartido, p90 ~5 ms.

## Datos
- **Libro CRUZADO** (bid > ask, ~2.700 filas/día) fabrica señales de valor relativo: el +17,75 €/€ del 05-Oct salía de un 15m
  cruzado. Toda regla que use el bid de otro mercado descarta libros cruzados (v3+ lo hace).
- El firehose (`polymarket_activity_*`) trae DOS filas por casación (tomador + cada maker): sin on-chain, "flujo tomador" contaminado.
- Registro ms fila x: usar c[7] (recepción), no c[6] (E de Binance, ~138 ms de look-ahead).
- TWAP60 oficial del segundo e = media RTDS [e−62, e−3], no [e−60, e]. ref5 llega +1,31 s p50 / +1,78 p90 (>1,5 s en 25 %).
- PolyBolt `spot` es Pyth, no Chainlink; desde el 02-Oct hay dos filas spot por segundo: filtrar `source` SIEMPRE.
- Φ(z) con σ de 300 s está SOBRECONFIADO y peor calibrado que el mid: calibrar contra el mid antes de usarlo como precio justo.
- El bookTicker grabado de Binance no es tick a tick (muestreo 100 ms si cambia).
- gamma-api no devuelve mercados CERRADOS por slug sin `closed=true`.
- Placebo de valor relativo sin restringir al lado s de las referencias: 236 k "señales" falsas/día.

## Estadística
- Sesgo de supervivencia al resolver: exigir desenlace OFICIAL con cobertura ≈100 % y decir la cobertura.
- Unidad = mercado-lado (no fill, no copia): micro-buckets por fills inflan n y EV.
- Makers "ganadoras" con grupos y medida del MISMO periodo = selección por resultado (14-Oct): grupos y medida en días distintos.
- Fallos en racimo: varias monedas en el mismo cierre son UNA apuesta; IC por cierre o por día, nunca por mercado.
- PnL concentrado en 1-2 días: reportar siempre EV sin los 2 mejores días y sin top 3.
- Buscar entre muchas celdas y testear la mejor con shuffle simple infla falsos positivos: max-statistic / BH-FDR.
- Un resultado espectacular es, primero, un bug.
- Ranking cuyo placebo e inversión salen igual de positivos no ordena nada.

## Operación (VPS de 4 núcleos, load habitual 12-16)
- Un solo análisis pesado a la vez; `nice -n 19 ionice -c3` y `ulimit -v 3000000` (o 3500000) y NUNCA en 06:00-09:00Z.
- `guard_ram_fase0.py` reinicia `observadores` si MemAvailable < 900 MB → se pierde el histórico ms en memoria.
- Los vigías congelados hashean el FICHERO ENTERO: editar uno (aunque sea un comentario) rompe el manifiesto y obliga a versión nueva + OOS nuevo.
- `pgrep -f` / `pkill -f` dentro de un comando que contiene el patrón se encuentra/mata a sí mismo: PIDs explícitos o script en fichero.
- El watchdog redespliega solo un ejecutor live si cambia su .py: preparar en dev y copiar de una vez.
- Editar un módulo de la cadena de imports de `observadores_fase0` lo reinicia (ojo con módulos compartidos).
- Todo cron con Telegram lleva `|| aviso de fallo`; todo logger nuevo: gz diario + retención + fuera de git.

## Cementerio de 5m barato (no reabrir por renombrado)
Pares 5m maker (OOS −0,050, CABEZA −0,032, 0/4 días) · maker de un solo lado (~0) · copiar makers ganadoras (no persisten) ·
copiar tomadoras persistentes (OOS −0,004) · FV v1-v3 (no batían al mid) · LOWLOW-PAIR (todas negativas en cota optimista) ·
BTC5M-FV-LONGSHOT (FV v4 no discrimina longshots) · entrada con retraso deliberado · vender bid15 rancio (−0,64) ·
órdenes armadas para cancelar en el delay · caja 2 patas a 250-400 ms (dry-run arbitraje anidado −35/−179 $).
- **El `m5_registro`/`m15_registro` diario NO es cronológico** (16-Oct): es la unión de tramos, cada uno ordenado (10-Oct: 22:25–24:00, 08:10–22:25, 00:00–08:10). Una ventana deslizante sin reiniciar en saltos atrás conserva ticks de horas antes: la defensa A_BN de cosechar v1 se activaba en el 94-100 % de los ticks (vs 2-7 % real). Todo lector debe reiniciar ventanas en saltos >60 s u ordenar por hora.
