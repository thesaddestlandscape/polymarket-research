# PREREG ganadoras_persistentes (25-Oct-2026 ~12:15Z) — congelado ANTES de calcular ningún desenlace/EV
Agente: cheap5m-wallet-intelligence-analyst (read-only). Datos: m5_onchain (VOL) 06..21-Oct (16 días; 22-24 sin desenlace: des 57/1728),
filas F con maker/tomador explícitos; tokens/desenlace oficial `DL/mapa_escala/{tokens,des}.json` (5min, 6 monedas). Todo EXPLORATORY (≤21 días).
No se usan wallet_edge_score*/smart_money_consensus/ballenas_timing_state para SELECCIONAR (circulares). ballenas_timing_history solo con filas ts < inicio de la medida.

## Definiciones
- Fill M: taker≠exchange (wallet=maker, fee 0). Fill T: taker==exchange (wallet=tomadora; fee=comisión pagada). Venta → compra del complementario (pc=1−p) para PnL; el lado/side RAW se guarda para el rol.
- Banda = fills con pc∈[0,05,0,30]. Unidad = posición (wallet, mercado, lado comprado convertido) con sus fills en banda. pnl = acc·1{gana} − coste − fee. Rebate (0,014·(1−pc)·coste) aparte, no suma.
- EV€ = Σpnl/Σcoste (ponderado por €) + media por unidad. IC90 bootstrap por DÍA (2000). Siempre: sin 2 mejores días, top-1 wallet % coste.

## S1 roster walk-forward (primaria)
- Días de prueba d=13..21 (9 d). Ventana de selección = [d−7, d−1]. Elegible: ≥20 unidades banda, ≥3 días activos, coste banda ≥100 $.
- p de wallet: z por CIERRE (cluster = fin): z = Σpnl_c / sqrt(Σpnl_c²), unilateral. Roster = BH-FDR q<0,10 sobre elegibles Y EV€>0 Y pnl>0 en ≥60 % de días activos.
- Medida: unidades banda del roster en d. PASA (ganadoras persistentes existen) si: EV€ agregado >0, IC90 por días >0, sin 2 mejores días >0, top-1 wallet ≤30 % del coste, y EV€ > p95 del PLACEBO (200 rosters aleatorios del mismo tamaño entre elegibles, sin filtro de EV, por día). Inversión: wallets BH con EV<0 (control).
- Secundaria S1b: D1=06..13 selección, D2=14..21 medida (mismos criterios).

## S2 rol on-chain (en la ventana de selección, sobre TODA su actividad 5m)
fM = coste maker/total; fV = coste de ventas RAW/total; fP = coste en mercados con COMPRAS raw de ambos tokens/total; fL = coste con pc<0,30/total.
Orden: (1) gestor de salidas fV≥0,25; (2) tomador-sniper fM<0,5; (3) maker con fP≥0,5: acumulador de pares si en esos mercados min(acc)/max(acc) mediano ≥0,6, si no maker ambos lados direccional; (4) maker fP<0,5: holder de longshots si fL≥0,5, si no maker pasivo. Medida S1 desagregada por rol (descriptivo, cada rol con su IC; sin gate propio salvo n≥40 unidades y ≥5 días).

## S3 relaciones → regla ejecutable para B (medidas en los días de prueba, población = proxy de B; b_vs_poblacion: B≈población)
- R1 copia tomador con NUESTRA latencia: tras un fill banda de roster-tomador en (m,s) con bloque t, primer fill T de la POBLACIÓN en (m,s) con bloque ≥ t+2 s y ≤ t+30 s, a su precio y fee → EV€ (print siguiente ≥2 s, nunca el fill de la wallet). Informativa (cementerio: copiar tomadoras).
- R2 celdas maker: celdas (moneda × seg desde apertura 60 s × precio 0,05) que cubren el 50 % del coste banda de roster-makers en la ventana → EV€ de TODOS los fills maker banda de la población en esas celdas en d, frente a todos los fills maker banda (Δ). Replicable por B si Δ>0 con IC90 días>0 y sin 2 mejores días >0.
- R3 idem para tomadores (población T en celdas de roster-tomadores) frente a todos los T banda.
- R4 filtro «roster-maker ya compró s antes»: fills maker banda de la población en (m,s) con algún fill de roster-maker en (m,s) con bloque ≤ tf−5 s (identidad on-chain visible) frente al resto. R5: roster-maker compró el lado OPUESTO ≤ tf−5 s → ¿cancelar? Δ con IC90 días.
- Skill no replicable = EV€ roster − EV€ población en las MISMAS celdas (ponderado por coste del roster).
- K confirmatorio = S1 + R2 + R4 + R5 = 4 ⇒ α=0,0125 (IC90 sirve de cribado; todo EXPLORATORY por ≤21 días).

## S4 infraestructura de ballenas no circular
- Conjunto BH_pre: wallets de ballenas_timing_history (marco 5m, precio∈[0,05,0,30], ts < 2026-10-14) con ≥20 trades y acierto − precio medio ≥ +0,05 → EV€ on-chain banda en 14..21 frente a placebo de wallets del histórico con ≥20 trades. Solapamiento roster vs wallet_edge_score_por_marco (CIRCULAR, solo descriptivo).

## Refutaría
S1 no pasa ⇒ no hay roster persistente a precio bajo explotable por selección; R2/R4/R5 con Δ≤0 o IC cruzando 0 ⇒ ninguna relación replicable por B.
