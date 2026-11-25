# EJECUTOR_B_K_CASOS_LIMITE — pase de casos límite (CLAUDE.md raíz, 6 categorías) del ejecutor B con política K (RF5)
Autor: cheap5m-execution-engineer, 24-Nov-2026. Código: rama de dev `b-k-ejecutor` (worktree /root/polymarket-research-dev-bk): `experimento_maker_bk.py` (+ 5 enganches `[HOOK-K]` no-op en `experimento_maker_h47.py`), `test_experimento_maker_bk.py`, `experimentos/5m_barato/b_k_ejecutor/`.
Estado: SIN /code-review (va en la revisión única con RF5), SIN OK de Javi, SIN pins escritos (`--escribir-pins` tras la firma de HASHES v3), NO ha enviado ninguna orden real. Todo lo siguiente es fail-closed salvo lo marcado «DECLARADO».

## 1. ¿El dinero no cuadra? -> qué hace el sistema
- Cuadre/kill de H47 intactos (cuadre on-chain, `suelo_fijado` con fsync antes del 1.er POST real, kill persistente, `.KILL` y lock ÚNICOS de toda la wallet; el ledger propio es `experimento_h47_BK_ledger.jsonl`, el lock/KILL son los de H47).
- Wallet 25 €: `presupuesto_util` ≤ 24 (el arranque exige saldo ≥ presupuesto + 1) y ≤ `presupuesto_eur` de `b_k_kill_dimensionado.json` (kill por € dimensionado por simulación, ver §7). La pérdida acumulada máxima = ese presupuesto (suelo dinámico: parada si saldo < pico − presupuesto). Sin ese JSON válido: no hay real (SystemExit).
- Stake: `--stake-usd` ≤ 5,0 (tope duro en código; subirlo = cambiar `STAKE_TOPE_DURO` con OK de Javi + review). Sin stake = tamaño H47 (5 acc, el SIMULADO). Con stake: size = floor(stake/precio) acc enteras, coste ≤ stake, nocional ≥ 1 $, ≥ 5 acc; si no cabe, no se envía.
- Real exige DOS confirmaciones (`--confirmo-dinero-real` y `--confirmo-micro-real-k`); una sola = SystemExit.

## 2. ¿La API falla a medias? -> estado recuperable
- Heredado de H47/X.Exp: identidad por hash EIP-712 antes de enviar, intención con fsync, cancelación por hash, `post_abortado_tras_firma`, orden sin ack -> verificación a los 30 s, reinicio que cancela lo propio.
- Cancelación por regla K: si `cancelar()` falla, `cerrar_ctx` pasa el mercado a la fase 'asentando' que reintenta cada 2 s y, si no se confirma en 60 s, kill (comportamiento H47). El hook solo dispara UNA vez por orden (`tau`), por eso el reintento es de la fase, no de la regla.
- Binance: WS propio con reconexión; sin mensajes de la moneda > 5 s (bookTicker/aggTrade, liveness del stream, no edad del último trade) o < 10 s tras (re)conectar = «Binance no vivo»: NO se arma y la orden viva se CANCELA (DECLARADO: el simulador marca hueco y no bloquea; aquí es más conservador).
- Clase de suelo desconocida (arranque en frío ~10 min, sin filas) = `indet` = no se opera.

## 3. ¿Se puede ejecutar dos veces? -> idempotencia
- Ledger de H47 (`slugs_usados`, N persistente, tope por puja 400 / total 20.000, una orden viva por puja, «mercado_ya_operado_no_reentra»). Test: `test_reinicio_a_mitad_no_reentra...`.
- El estado de la política K (F5_0, `tau`, arrays de saltos) es EFÍMERO por diseño: tras un reinicio no se reentra en ningún mercado ya operado, y el calentamiento de Binance (10 s) y de la clase de suelo (~10 min) hace que un reinicio solo retrase, nunca arme sobre un J vacío.
- El mercado cerrado por regla K no se rearma (como el simulador: `m.done = True`).

## 4. ¿Datos viejos o faltantes? -> fail-closed
- F5 inválido/NaN/ausente/estado > 30 s => veto (prereg §1; misma función `sec7_core.f5t`). F5_0 se mide en la PRIMERA alta intentada aunque otra guarda bloquee, y se loguea (`k_f5`: f5_0, edad, vetado) para auditar contra el simulador.
- Libro WS: se re-lee JUSTO antes de enviar (`_post_real`): sigue en banda y el objetivo H35 == precio, si no `k_pre_envio_abortado: libro_movido`; además la comprobación tras firmar del harness (bid ajeno, ask, T_STOP). Libro no fresco (> 5 s sin mensajes) = no se opera (H47).
- Circuit breaker (kill/parada/señal) y clase `lo` y Binance vivo se re-chequean también en `_post_real` (test `test_real_pre_envio_aborta...`).
- Solo ventanas de clase `lo`: se usa la clase CAUSAL de la ventana (`suelo_causal.SueloCausalLive`, solo filas rx < w0), no la tabla `clase_estrato` (que mira al futuro a propósito). DECLARADO: una ventana causal `lo` puede ser `indet`/`hi` por estrato; el filtro del vivo es la mejor aproximación sin mirar al futuro. Las filas q del vivo se reconstruyen del WS del propio ejecutor (rx tomado tras parsear el mensaje en proceso, ligeramente posterior al registro ms): si sesga el p5 hacia arriba, el efecto es `indet` => no operar (nunca operar de más). Medido en ensayo en seco: ver informe.
- Código de la política pineado por sha (`b_k_pins.json`, 10 ficheros); real sin pins que cuadren = SystemExit.

## 5. ¿Límites del exchange? -> min $1, 5 acc, decimales, tick
- Tick 0,01 verificado por mercado (`get_tick_size`), precio en rejilla (`en_rejilla`), tamaño entero de acciones, ≥ 5 acc, nocional ≥ 1 $ (`tamano_orden`/`tamano`), `min_size` del mercado, `post_only` GTC, máx. 5 vivas, tope 5 $ por orden (solo con stake), tick_size_change -> mercado cerrado (H47).

## 6. ¿Reinicio a mitad? -> estado persistente
- Ledger/suelo/N/kill persisten (H47). `--reiniciar-suelo`, `--aceptar-linea-ilegible`, `--rotar-tanda` NO están expuestos en este entrypoint (la reinversión del beneficio y la subida de stake son decisiones de Javi con cambio de configuración explícito).
- El supervisor `h47_tandas_supervisor.py` NO se ha tocado y no lanza este ejecutor (otro comando, otro ledger).

## 7. Kill-switch por € dimensionado por simulación
`experimentos/5m_barato/b_k_ejecutor/kill_dimensionado.py` (bootstrap por bloques de cierre de 5 min sobre las órdenes RF5 de 17-Nov no ciego, retorno por € escalado al stake, 10 días): presupuesto = menor X con P(falso disparo | edge medido) ≤ 5 %; se reporta también con mitad de edge y con edge nulo. Es calibración de umbral, no validación del edge. Resultado y n: ver informe de entrega (y `b_k_kill_dimensionado.json`).

## 8. Diferencias DECLARADAS frente al simulador (no bit a bit)
1. Reloj de decisión = instante actual (sim: rx + 50 ms). 2. `t_arr` de la orden = instante previo al envío (sim: +88 ms): un salto adverso en esa ventana cuenta como disparo (lado seguro). 3. `no_armar` conserva el retraso de armado de 300 ms de la política (tq = t − 300), como el simulador. 4. Binance muerto => no armar y cancelar (sim: no bloquea). 5. El simulador acopla mercados por `MAXV/busy` y modela latencias medidas; en vivo son reales. 6. Con `--stake-usd` el tamaño es ≠ 5 acc: el simulador NO lo ha modelado (profundidad/cola a ese tamaño); el EV/€ simulado solo es extrapolable si el relleno escala.
