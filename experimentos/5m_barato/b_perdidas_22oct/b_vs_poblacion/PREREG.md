# PREREG b_vs_poblacion (25-Oct-2026 ~11:40Z) — congelado ANTES de calcular EV/cola de B vs población
Pregunta: B (wallet dedicada 0x659a40ff…297f) gana −0,072 €/€ (b_regimen/b4, n=202 posiciones) y la población de rellenos maker 5m pc 0,05-0,30 gana +0,0265 (wallets_ballenas_b/a1, 12-21 Oct, 6 monedas). ¿Dónde está la brecha?
Ya visto (declarado): cola_posicion (B delante en ráfaga 96 %, A0 mediana 25, 97 % de la cola cancela; posición↔EV no demostrada), control_misma_edad (retirada ≤300 ms, no accionable), b_regimen (EV población por nivel P1/P2), as_tomador (tomadores informados: REJECTED).
## Datos
- `/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_D.csv.gz`, tipo F, tokens 5min de `mapa_escala/tokens.json`; desenlace `mapa_escala/des.json` (sin desenlace = missing, se reporta cobertura). D = días 12..22-Oct (límite de tokens.json/des.json). vida_puja_virtual solo tiene 24-Oct (fuera de cobertura): NO se usa.
- Relleno maker = fila F con taker != exchange (misma conversión que e1_extrae: lc lado comprado, pc, coste, acc). Se guardan tx y log_index.
- B = maker == 0x659a40ff9920febc5a66836213040924343d297f. Población P = resto de makers, MISMAS monedas que B y MISMOS días en que B tiene rellenos, pc∈[0,05;0,30], sec∈[0,300]. REF = a1 (+0,0265, no se recalcula).
- EV = Σ(acc·gana − coste)/Σcoste (ponderado por €), fee maker 0; rebate aparte (0,014·(1−pc)·coste) solo informativo.
## Métricas
1. Nivel = (mercado, lc, pc redondeado a 0,01) dentro de la tx. SWEEP(f) = en la misma tx hay relleno maker del mismo (mercado, lc) a pc ≤ pc_f − 0,005 (el tomador agotó el nivel y siguió). ULTIMO(f) = f es el último log_index entre makers de su nivel en la tx. MULTI = ≥2 makers en el nivel. Comparar P(SWEEP), P(ULTIMO|MULTI) B vs P (por € y por fila).
2. Emparejado: para cada relleno de B, rellenos de P en el mismo (mercado, lc), |Δts| ≤ 60 s (M60) y además mismo nivel ±0,01 (M60L). Por construcción el desenlace es idéntico: la diferencia B−M60L solo puede venir de precio/tamaño; EV(M60) mide si TODO el flujo de ese mercado-momento perdía.
3. Descomposición secuencial de G = EV_B − REF: (a) periodo+moneda = EV_P − REF; (b) composición = EV_P reponderado a la distribución en € de B por estrato moneda × pc 0,05 × sec (0-60,60-120,120-180,180-240,240-300) × tamaño de relleno (≤5, 5-10, >10 acc) − EV_P; además cada dimensión sola; (c) selección de mercado-momento = EV(M60) − EV_P reponderado; (d) residuo = EV_B − EV(M60) (precio dentro del mercado-momento + cola).
4. Cola: en P, EV por SWEEP sí/no y por ULTIMO/PRIMERO en MULTI; contrafactual EV_B reponderando B a la mezcla SWEEP de P.
## Inferencia
IC90 bootstrap (2000) por CIERRE (fin del 5m; todas las monedas del mismo cierre = 1 unidad) y por DÍA. Placebo: 1000 pseudo-B muestreados de P con la misma distribución de estratos (3) y el mismo nº de rellenos ⇒ percentil de EV_B y de P(SWEEP)_B.
## Reglas (fijadas antes)
- «La cola explica» si P(SWEEP)_B − P(SWEEP)_P tiene IC90 por cierre > 0 Y el contrafactual (4) cierra ≥50 % de (c)+(d). Si no: «no es cola».
- «Selección de mercado-momento» si (c) < 0 con IC90 por cierre < 0.
- n de B ~200 rellenos y 3 días: todo es EXPLORATORY; nada decide política, solo dice qué probar.
