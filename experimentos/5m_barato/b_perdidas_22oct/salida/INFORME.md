# B perdidas: causalidad tras el relleno y reglas de SALIDA / NO-ENTRADA (22-Oct-2026, ~15:00Z)
Etiqueta: **REJECTED** para todas las reglas de salida y de veto previas al relleno que se probaron. No hay ninguna regla que cortar.
Preregistro congelado ANTES de calcular: `PREREGISTRO.md` (sha256 ad46304660a491ca…, `sha256sum -c PREREGISTRO.sha256` = OK).
Solo lectura sobre producción. Scripts en `scripts/`, datos intermedios en `datos/` (fuera de git).

## 1. Datos, unidades y relojes
- **B real**: 175 posiciones H47-B (`contabilidad_wallet_dedicada/posiciones.csv` con tanda_B, sha 26b8b95c…; 37 ganadas / 138 perdidas; coste 193,6 $, PnL −2,32 $, EV −0,012/€). La hora de detección del relleno (`puja_fin.rellenos.t_deteccion` del ledger `experimento_h47_B_ledger.jsonl`, mismo reloj que la recepción del registro ms) existe para 166; **9 son missing** (excluidas). Desenlace oficial gamma 175/175, y coincide 175/175 con la contabilidad.
- **Población** (para tener potencia): rellenos tipo-B de OTROS en ETH/SOL/XRP 5m (primera operación por mercado-lado a 0,10-0,30 con T restante 65-295 s, 5 acciones), sacados de los trades del WS del CLOB. **Descubrimiento** 17-19 Oct, 3.094 unidades, 3.689 €. **Test** 20-22 Oct (el 22 llega hasta ~14:40Z), 2.583 unidades, 3.096 €. Desenlace gamma 100 % salvo 6 mercados del 22-Oct aún sin resolver (excluidos).
- Libro: filas q (top) y t (operaciones) ordenadas por **RECEPCIÓN**. Fuente: `VOL/m5_registro` + `m15_registro` para 17-21 Oct y el registro ms crudo para el 22. Binance: aggTrade con recepción en c[7].
- **Cronología de un relleno de B** (medida): en 128 de 166 casos el relleno aparece en el WS como un **BUY tomador del token contrario a 1−p** (cruce por acuñado). Solo 21 casan con un print del propio token. Nuestra detección llega una mediana de **1,16 s** después de ese print (n=21) y **1,5 s antes** del bloque on-chain (mediana, n=166; rango −3,5..+3,6 s).

## 2. Qué pasa tras el relleno (señales causales). Pérdidas vs ganancias
B real (166 unidades; mediana en perdedoras | ganadoras):

| τ tras detección | Δbid propio vs precio de relleno | Binance a nuestro favor (bps, media) | Δbid15 mismo lado | AUC del bid del momento | AUC de la mejor señal |
|---|---|---|---|---|---|
| +5 s | −0,03 \| 0,00 | −0,25 \| +1,08 | 0,00 \| +0,01 | 0,64 | 0,69 (flujo) |
| +15 s | −0,05 \| +0,035 | −0,71 \| +2,49 | 0,00 \| +0,035 | 0,74 | 0,76 (Δbid) |
| +30 s | −0,08 \| +0,12 | −0,88 \| +3,60 | 0,00 \| +0,09 | 0,78 | 0,81 (Δbid) |
| +60 s | −0,11 \| +0,20 | −0,98 \| +6,22 | −0,02 \| +0,135 | 0,86 | 0,87 (Δbid) |

La población muestra el mismo patrón (AUC 0,59-0,82, estable en los 3 días). **Mecanismo**: el relleno llega dentro de un barrido. En las perdedoras el movimiento sigue (el bid propio ya cae 3c a los 5 s y 11c a los 60 s; Binance se mueve en contra) y en las ganadoras se da la vuelta. Es la selección adversa ya medida, ahora vista desde la SALIDA.
**Lo que mata cualquier salida**: el precio ya lo descuenta. En el logit `gana ~ logit(bid_salida) + señal` ninguna señal añade información sobre el bid del momento (|z| < 2,1 en los 3 periodos; el único z=−2,1, Δbid15 a 30 s en 17-19, tiene el signo opuesto en el test). Por cuartiles de Δbid, el acierto real ≈ el bid de salida (p. ej., pob. 17-19 a 60 s, peor cuartil: 5,2 % de acierto frente a un bid de 5,6 %). Vender al bid paga medio spread + medio tick + comisión (≈0,01-0,02 $/acción, un 5-10 % del precio a 0,10-0,25) sin vender nada sobrevalorado. (`scripts/describe.py`, `scripts/incremental.py`)

## 3. Reglas de SALIDA (40 preregistradas: τ 5/15/30/60 s × incondicional, Δbid, Binance, Δbid15, flujo WS, desequilibrio del top)
Ganancia = Σ(salida − mantener) en las disparadas / coste de TODAS las unidades (ponderado por €). Ficheros `reglas_*.csv`, `scripts/reglas.py`, `scripts/ic.py`.
- **Población, elegir en 17-19 → medir en 20-22** (contraste principal). La mejor del descubrimiento, A5 (desequilibrio del top ≤0,25 a 60 s), daba +0,0089/€ (p placebo 0,073, p max-estadístico 0,53). En el test: **−0,034/€** (−106,5 €; salva 371 € en 482 perdedoras y sacrifica 478 € en 145 ganadoras; IC90 por cierre −0,062..−0,008; 0/3 días). La segunda, A4 (flujo en contra a 15 s): +0,0086 → **−0,043** (IC90 −0,067..−0,018). **Las 40 reglas son negativas en el test** (de −0,0003 a −0,18/€). Ninguna pasa el max-estadístico en el descubrimiento (p ≥ 0,53). La incondicional (como H41): −0,07/−0,08 €/€ en 17-19 y −0,15/−0,18 en 20-22.
- **B real, elegir en 20+21 → medir en 22**. Mejor regla: A2 = vender a +30 s si Binance se movió ≥3 bps en contra (+0,082/€ en 20-21, p placebo 0,056, p max-estadístico 0,78). En el 22-Oct: +0,043/€ (+2,99 €) frente a un placebo de +0,015, p 0,38. En los 3 días dispara 33 veces, todas perdedoras: salva +12,31 €, sacrifica 0 € y deja una ganancia de +0,067/€. Ese 0/33 es azar de una muestra pequeña elegida entre 40 reglas. En la población, la MISMA regla dispara 625 y 532 veces, las disparadas aciertan el 8,8 % y el 12,0 % (al nivel de su bid de salida, 8,7 % y 9,1 %, o por encima), y da **−0,010 y −0,034/€** (IC90 por cierre en test −0,058..−0,011). Las inversiones (vender cuando la señal va a favor) también salen ≤0: la salida pierde se haga como se haga.
- Ojo de régimen: el 22-Oct la propia incondicional "gana" en B (+0,10/+0,22/€) solo porque fue un día de pocas ganadoras (EV mantener −0,22). Por eso el placebo es el contraste que vale, no el signo del día.

## 4. Reglas de CANCELACIÓN / NO-ENTRADA (señal en [relleno −10 s, −0,3 s] → no pujar)
`scripts/pre.py`. B real: ninguna se distingue del placebo (p 0,14-0,57). Población: la mejor del descubrimiento, Δbid15 ≤ −2c (+0,035/€, p 0,11), da **−0,075/€** en el test (p 0,93, peor que el placebo; 0/3 días). Las demás también son negativas en el test. Coincide con el REJECTED previo de «cancelar si el bid15/Binance cae» (b_seleccion_adversa, H26-MS). Limitación: aquí solo se cuentan las rellenadas (no el contrafactual de la re-puja).

## 5. Viabilidad de ejecución (aunque el EV fuera positivo)
- La salida tomadora tarda ≈215 ms del envío al casado (F1). Con τ ≥5 s la latencia no es el problema: el problema es el precio.
- **17 de 166 posiciones de B (10 %) no se pueden vender**: tienen menos de 5 acciones (rellenos parciales: 0,10-4,995 acc; min_order_size 5). Además, vender exige que el relleno esté liquidado on-chain (bloque ≈1,5 s después de nuestra detección).
- En la población el bid existe casi siempre (τ=5: salida posible en 3.093/3.094) y con profundidad ≥5 acc en el top la mayoría de las veces.

## 6. Conclusión
Las pérdidas de B se anticipan tras el relleno (Δbid, Binance y bid15 en contra; AUC hasta 0,87 a 60 s), pero el mercado ya las precia en el bid. Vender o cancelar no recupera nada: en la población, fuera de muestra, todas las variantes pierden 0,03-0,18 €/€ y sacrifican más € en ganadoras de los que salvan en perdedoras. Esto cierra con datos de libro por recepción lo que H40/H41 apuntaban con la caché H35. **No cortar nada por salida.** La palanca contra las pérdidas está ANTES de pujar (dónde y cuánto: nivel del bid15 R2/R3 en b_seleccion_adversa, en forward). La pista «Binance ≥3 bps en contra a +30 s» de B (0/33 ganadoras) no replica en la población: anotarla solo como observación para el forward de B (con ≥300 posiciones), sin regla.

## 7. Desviaciones y huecos (declarados)
- Definición de relleno de la población ampliada a «BUY del token contrario a 1−p», tras verificarla con los rellenos de B (128/166) y antes de ver los resultados de la población. t_det de la población = recepción del print + 0,5 s (preregistrado). El retraso medido de B es de 1,16 s (n=21): sin análisis de sensibilidad. Con τ ≥5 s el efecto esperado es menor.
- Las filas q del 15m se adelgazaron (solo cambios de bid o huecos de más de 60 s) para caber en RAM. El ms_2026-10-22.npz pudo salir de una ejecución sin adelgazar: mismo contenido útil.
- Solo hay salida tomadora al bid. No se ha probado una salida maker (vender en el ask); la selección adversa del lado vendedor la haría peor. Solo ETH/SOL/XRP 5m. El 22-Oct es parcial. Hay 9 posiciones de B sin hora de detección (missing).
- Reproducir (nice 19, `ulimit -v 3000000`, pico de RSS 1,6 GB): `scripts/run_extraer.sh DIA…` → `desenlaces.py DIA…` → `unidades_b.py` → `trayectorias.py b|pop DIA…` → `describe.py`, `reglas.py`, `pre.py`, `ic.py`, `incremental.py`.
