# PREREG — reglas de cartera/tanda para B (H47-B real), fijadas ANTES de ver resultados por posición
Fecha: 2026-10-22 ~14:35Z. Autor: agente risk-economics (ángulo cartera/tanda). Solo lectura sobre producción.

## Lo ya visto antes de fijar esto (declarado)
- Tabla por tanda de `contabilidad_wallet_dedicada/resumen_por_experimento.md` (PnL por tanda 1-23, total B −2,32 $).
- `B_MEJORA_DIARIA.md`: XRP peor (EV −0,025), hb=8 UTC −0,248, hb=4 +0,713 (b_postmortem). Por eso las reglas de moneda/hora
  NO usan esas celdas fijas: solo walk-forward causal.
- NO visto: secuencia por posición, rachas, concurrencia, correlación dentro de un mismo cierre.

## Datos y unidad
`contabilidad_wallet_dedicada/posiciones.csv`, experimento == H47-B, estado liquidada_* (desenlace oficial gamma 178/178).
Unidad = posición (mercado, outcome). t_fill = fecha_primer_fill_utc; t_conocido = fin_mercado_utc + 60 s (cuándo se sabe el resultado).
Orden por t_fill. Toda regla decide en t_fill usando solo posiciones con t_conocido <= t_fill.

## Reglas (familia de 11, parámetros fijos)
- R0 ACTUAL: todas.
- R1a/R1b RACHA_POS k=5 / k=8: si las últimas k posiciones TOMADAS ya conocidas son todas perdedoras -> pausa 60 min desde que se conoce la k-ésima; la racha se reinicia tras la pausa.
- R2a/R2b TOPE_CONCURRENTE C=2,0 / 3,0 $: se salta un relleno si coste abierto (tomadas con t_fill <= t < t_conocido) + coste propio > C.
- R3 UNA_POR_CIERRE: se salta un relleno si ya hay una posición tomada con el mismo fin_mercado.
- R4a/R4b STOP_DIARIO L=5 / 10 $: tras PnL conocido del día UTC (tomadas) <= −L, no se toma nada más ese día.
- R5 TANDAS_SEGUIDAS: tras 2 tandas seguidas con PnL<0 (tomadas; resultado conocido al t_conocido máximo de la tanda), se salta la tanda siguiente entera; la racha se reinicia.
- R6a WF_MONEDA / R6b WF_HORA4: se salta si la moneda (resp. bloque UTC de 4 h) tiene, entre TODAS las posiciones ya conocidas (shadow, para evitar estado absorbente), n>=15 y Σpnl/Σcoste < 0.
- R7 TAMAÑO_MINIMO: cada posición reescalada a 5 acciones (pnl y coste × 5/acciones). Regla de tamaño, no de selección.

## Métricas
PnL total ($), coste, EV ponderado Σpnl/Σcoste, ΔPnL vs R0, % de coste retenido, drawdown máximo de la curva de PnL realizada (orden t_conocido),
peor tramo de 24 h. IC90 de ΔPnL por bootstrap de TANDAS (contribuciones Δ por tanda, 10.000 réplicas). Split: tandas 1-12 vs 13-23.

## Placebos y falso disparo
- Placebo de secuencia: permutar los atributos de las posiciones (coste, pnl, moneda, acciones) entre los huecos temporales (t_fill, t_conocido, tanda, fin_mercado fijos), 2.000 permutaciones; p = P(Δ_placebo >= Δ_obs). Corrección de familia: Bonferroni ×10.
- Falso disparo / coste con edge real: resultados sintéticos Bernoulli q = precio·(1+e), i.i.d., misma secuencia de precios/tiempos, e ∈ {+0,10, 0, −0,10}, 2.000 sims: E[ΔPnL], P(dispara), % de coste eliminado.
- Criterio de palanca útil (fijado ahora): Δ_obs > 0, p_placebo < 0,05/10, IC90 bootstrap tandas de Δ excluye 0, Δ>0 en las dos mitades, y E[ΔPnL | e=+0,10] >= −10 % del PnL esperado con edge. Si ninguna lo cumple: "no hay palanca de cartera validada".

## Drawdown irreducible vs evitable
Simulación i.i.d. con los precios/costes reales de B: DD máx esperado con e=0 (varianza pura de pago) frente a e=observado; y DD con R3 (correlación por cierre).
Simulación del proceso de tandas (presupuesto 5 $, bloqueo por suelo con coste abierto, cierre por +6 $) con e=0 para ver qué reparto ganadoras/perdedoras produce la mecánica sola.
