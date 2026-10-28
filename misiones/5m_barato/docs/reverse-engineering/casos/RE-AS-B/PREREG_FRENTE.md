# PREREG E-RE-AS-B-FRENTE — «FRENTE-TD»: puja en el FRENTE de un nivel nuevo (+1 tick) + cancelación por Binance (27-Oct-2026 ~13:05Z, ANTES de calcular nada)
Autor: polymarket-quantum-alpha-miner (intervención previa). Solo lectura de datos; pujas VIRTUALES; no toca B/producción/crons/git.

## Por qué esta política y no otra (decisión previa, con lo ya medido)
- La AS de B es, sobre todo, de POSICIÓN EN COLA: una puja al FINAL de la cola de bb solo se rellena cuando un flujo grande consume todo el nivel (86 % de rellenos pes los completa el espejo, 89 % con print por debajo de b: barridos; VALIDACION_E02). El dinero del maker (comprar a b sin condicionar +0,135 €/€) se lo queda el PRIMERO de la cola, que cobra al vendedor pequeño/no informado; el último solo recibe barridos (−0,33 pes).
- Mecanismo (H-ASB-7, distinto de cola-por-moneda, palanca 1, TD sola, filtrar rellenos): mejorando un tick (b' = bb+0,01, dentro del spread) se crea un nivel NUEVO con cola delante 0 → nos rellena el PRIMER vendedor que cruce, sea cual sea su tamaño. Encima, TD (E-RE-AS-B-TD, ya medida y congelada: salto adverso Binance ≥2 bps/300 ms, Lc=100 ms) aparta a los tomadores informados por Binance aprovechando la ventaja maker (cancelación ~60 ms vs taker delay ~145-217 ms).
- Ventaja de medición: en el frente el relleno lo fija el primer print que cruza (no hay cola que modelar) → pes≈opt; la sensibilidad residual es (i) A+B vs max(A,B) (doble conteo espejo), (ii) Lp (llegada de la orden), (iii) reacción de otros (penny-jumping, vendedores nuevos atraídos por el mejor bid) NO observable en histórico.
- Descartadas para esta prueba (valor/coste): (3) pujar solo con Binance quieto = TD k=1 ya medida (opt +0,014, IC cruza 0); (4) rebate/rewards: rebate ≈ +1 % del coste, no cambia el signo de pes; rewards exigen ≥50 acc; (5) pares con cancelación: complejo y en el cementerio la versión sin cancelación (−0,050); queda como siguiente si FRENTE no da.

## Datos
m5_registro_D (24, 25, 26-Oct; filas k/q/t; reloj = RECEPCIÓN: q c7, t c6); Binance = filas x extraídas (scratch td/x_D.csv, precio c3, RECEPCIÓN c7, las mismas de td_eval.py); desenlace maker_ms_desenlaces_cache.json (missing = fuera). Baseline cola-final: vpv_D.csv.gz (relleno_pes/opt) unido por (mercado, lado, t0).

## Política primaria (congelada)
1. Calendario idéntico a vida_puja_virtual_5m.py: cada 10 s por token 5min, si bb∈[0,10;0,30] y T∈[60;300] s, en la recepción de la fila q. La política coloca SOLO si ba−bb ≥ 0,02: BUY 5 acc a b' = bb+0,01 (post-only).
2. Llegada: activa desde t0+Lp, Lp = 85 ms (F1: acuse GTC 84 ms). Rechazada si la primera q del token con recv ≥ t0+Lp tiene ba ≤ b'. «Disputada» si en esa q bb ≥ b' (se trata igual, cola 0: optimista; se reporta).
3. Relleno (regla A+B): prints con recv ≥ t0+Lp y ≤ fin de vida: SELL del token a p ≤ b' (A) y BUY del complementario a p ≥ 1−b' (B); acciones acumuladas hasta 5 (parciales cuentan con sus acciones).
4. Vida: hasta 5 acc, t0+60 s o cierre−2 s.
5. TD: primer instante tr ∈ [t0, fin] (recepción Binance) con retorno adverso 300 ms ≥ 2 bps (YES=Up: bajada; NO: subida), calculado como td_eval.saltos; cancelación efectiva en tr+Lc, Lc = 100 ms: prints con recv ≥ tr+Lc no rellenan.
6. Unidad: por (mercado, lado) la vida con el PRIMER print que rellena (empate: menor t0); acciones = las de esa vida (≤5). pnl = acc·(g−b'), coste = acc·b', comisión maker 0, SIN rebate.
7. Métrica: EVw = Σpnl/Σcoste (€/€); IC90 bootstrap por CIERRE (2000, semilla 2711); también EV por unidad y por día.
8. Muestras: DESC = 24+25; OOS = 26 (el 26 ya se vio en otros experimentos con OTRAS políticas; los parámetros de esta — +1 tick, k=2, 300 ms, Lc=100, Lp=85 — vienen de E-TD/F1 y no se ajustan aquí).

## Criterios (sobre la primaria)
- REFUTADA: IC90 por cierre de TODO (24-26) con cota superior < 0, o EVw ≤ 0 en DESC y en OOS.
- PROMETEDORA (pendiente de forward): EVw > 0 en DESC y en OOS; IC90 TODO cota inferior > 0; EVw > 0 con regla conservadora max(A,B); EVw > 0 sin el mejor día. (Nunca «validada»: el gate exige ≥10 días, n≥40 por celda moneda×bucket, IC90 por día >0, forward.)
- EXPLORATORIA: EVw TODO > 0 sin cumplir lo anterior. NEGATIVA no concluyente: el resto.

## Controles y robustez (descriptivas, Bonferroni ×12; no cambian la decisión)
Frente SIN TD (aísla el efecto cola); TD placebo = serie Binance desplazada −60 s (misma frecuencia, información rancia); inversión = unidades cuyo primer print cae tras la cancelación TD (lo que la regla aparta) frente al resto; regla max(A,B); excluyendo disputadas; solo rellenos completos de 5; Lp 0 y 250; +rebate 0,2·0,07·b'(1−b') por acción (supuesto no verificado); sin el mejor día; peor día (= sin los 2 mejores); sin los 2 mejores cierres. Baseline cola-final (vpv pes/opt con TD) sobre las MISMAS vidas (spread ≥ 0,02). Desagregado moneda × bucket b' (0,05), n≥40, descriptivo.

## Límites declarados (Fail Loud)
Pujas virtuales; la reacción de otros makers a nuestro nivel (penny-jumping) y los vendedores que solo venderían a b' no están en el histórico (sesgo de signo desconocido); se supone que B no operó 24-26 (sin auto-print; por fechas del ledger, no verificado on-chain); recepción ≠ hora de exchange; libro espejo YES/NO supuesto (lo usa vpv).
