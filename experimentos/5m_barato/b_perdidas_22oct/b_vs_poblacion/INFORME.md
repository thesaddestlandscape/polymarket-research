# B vs población en el MISMO mercado-momento-nivel (25-Oct-2026). Estado: EXPLORATORY. Solo lectura, coste 0.
Prereg `PREREG.md` (sha256 af2902aa…, `sha256sum -c PREREG.sha256`) + `ADENDA1.md` (fuente de desenlace; la pasada 0 sin 22-Oct se descarta por supervivencia, guardada en `datos/x2_salida_pasada0_sin22.txt`). Salida: `datos/x2_salida.txt`.
Datos: on-chain `m5_onchain_2026-10-{20,21,22}` (rellenos maker con tx+log_index; extracción `scripts/x1_extrae.py` → `/mnt/HC_Volume_106538179/agentes_datos/b_vs_poblacion/F_D.pkl`), desenlace des.json ∪ tok_* ∪ gamma closed=true (cobertura 100 % en € de B y P). B = 0x659a40ff…297f, 198 rellenos (ETH 80, SOL 65, XRP 53), pc 0,11-0,29. P = 91.383 rellenos de 425 wallets, mismas monedas y días, pc 0,05-0,30.

## 0. Respuesta corta
1. **La brecha «−0,072 vs +0,027» compara cosas distintas.** −0,072 = 202 posiciones 20-Oct..23-Oct 08:56Z (`post_25_27/datos/pos_b.csv`); +0,027 = población 12-21 Oct, 6 monedas. En lo comparable (20-22 Oct, ETH/SOL/XRP, on-chain): **B −0,030 (n=198, 204 €) vs población −0,045 (n=91.383)**. B no es peor que la población en su periodo; el 23-Oct (sin mapa de tokens) queda fuera y es donde B empeora a −0,072.
2. Descomposición G = EV_B − 0,0265 = −0,057: (a) periodo+moneda **−0,071**; (b) composición (moneda×precio×T×tamaño) **+0,105** (IC90 cierre +0,022..+0,189; casi todo porque B no tiene rellenos >10 acc, que en P pierden −0,114); (c) mercado-momento (flujo de P en el mismo mercado-lado ±60 s) **−0,081** (IC90 cierre −0,35..+0,19); (d) residuo precio/cola **−0,009** (IC90 cierre −0,085..+0,060; día −0,053..+0,029).
3. **Emparejado**: en el mismo mercado-lado ±60 s B −0,029 vs resto −0,021 (196/198 con pareja); en el mismo nivel ±1c **−0,005 vs −0,002** (n=156). Dentro del mismo mercado-momento B gana lo mismo que los demás.
4. **Cola**: rellenos de B en barridos que agotan el nivel 19,9 % del € vs 20,6 % en P (Δ IC90 cierre −0,056..+0,042); contrafactual con la mezcla de barridos de P −0,031 (no cambia nada). B comparte nivel en el 14 % (P 37 %) y cuando lo comparte va primero en el 71 % (P 42 %, coherente con cola_posicion). **Regla «la cola explica»: NO CUMPLE. Regla «selección de mercado-momento»: NO CUMPLE (IC cruza 0).**
5. Placebo (1000 pseudo-B de P con los mismos estratos, n=198): EV medio +0,060, p5 −0,206, p95 +0,346; B en el percentil 32. 198 rellenos no distinguen a B de un maker cualquiera de su mismo estrato.

## 1. Detalle (EV ponderado por €; n = rellenos)
| corte | B | P |
|---|---|---|
| por día 20/21/22 | +0,07 (40) / +0,17 (77) / **−0,27 (81)** | −0,32 / +0,17 / +0,17 |
| por moneda ETH/SOL/XRP | +0,01 / −0,01 / −0,12 | −0,10 / +0,09 / +0,16 |
| tamaño ≤5 / 5-10 / >10 acc | −0,153 (143) / +0,287 (55) / — | +0,021 / +0,077 / −0,114 |
| T desde apertura 0-60/60-120/120-180/180-240 s | −0,14 (51) / −0,01 (63) / −0,02 (61) / +0,17 (23) | −0,00 / −0,10 / −0,01 / −0,16 |
| pc .10-.15/.15-.20/.20-.25/.25-.30 | +0,49 (34) / +0,07 (39) / +0,18 (63) / −0,45 (62) | +0,17 / −0,11 / −0,08 / −0,11 |
| barrido sí / no | −0,11 (36) / −0,01 (162) | −0,01 / −0,05 |
| nivel compartido: último / primero | +0,71 (6) / −0,32 (20) | −0,03 / −0,06 |
EV_B sin los 2 mejores días −0,267 (solo 22-Oct); P ese día +0,174: la divergencia del 22-Oct (y de XRP) es lo único llamativo, con n=81 en ~40 cierres.

## 2. Límite honesto
- 198 rellenos, ~100 cierres, 3 días: desviación del EV de un pseudo-B ≈0,17; para ver una diferencia de 0,09 con IC90 hacen falta ~1.800 rellenos (~28 días al ritmo de B). IC por día con 3 clústeres es informativo, no inferencial.
- On-chain no da la hora de armado/cancelación de B: «tiempo de puja» se aproxima por T del relleno. Tamaño del relleno ≠ tamaño de la orden (condicionar al tamaño final fabrica edge, trampa 19-Oct).
- 23-Oct fuera (tokens.json acaba el 22-Oct). vida_puja_virtual solo 24-Oct: no usado. Rebate no incluido (fee maker 0 en ambos).
- Descomposición secuencial: el reparto entre (b) y (c) depende del orden.

## 3. Qué política probar (diagnóstico, nada a real)
No hay palanca de cola: ni barridos, ni ir el último, ni cancelar (control_misma_edad ya lo rechazó a ≥300 ms). Lo que mueve el EV de B es CUÁNDO y EN QUÉ mercado está puesto (a y c), y eso no se puede separar mirando los datos con este n. Propuesta: **A/B aleatorizado dentro de B** (cada orden con un brazo sorteado y registrado: clip 5 vs 10 acc; armar en T 0-120 vs 120-240 s; nivel top vs top−1c), EV por € por brazo, IC por cierre, gate ≥1.800 rellenos. Mientras tanto, medir B contra P SIEMPRE en el mismo periodo y monedas (−0,030 vs −0,045), no contra el +0,027 de 12-21 Oct.

## 4. Reproducir
`nice -n 19 ionice -c3 python3 scripts/x1_extrae.py 2026-10-20 2026-10-21 2026-10-22` → `python3 scripts/x0_gamma_des.py` (necesita `datos/mids_sin_des.json`, generado inline: mids de P∪B sin des.json ni tok_*) → `python3 scripts/x2_analisis.py > datos/x2_salida.txt`. Hashes en `HASHES.txt`.
