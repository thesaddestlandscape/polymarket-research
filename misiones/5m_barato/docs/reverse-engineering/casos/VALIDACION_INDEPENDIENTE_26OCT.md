# Validación independiente 26-Oct de RE-AS-B y RE-B-REFORMULACION (statistical-validator Opus; transcrito por el chief)
Fuentes crudas: experimento_h47_B_ledger.jsonl (3.796 órdenes), onchain_fills_2026-10-20..24 (maker 0x659a…297f, 215 filas / 202 órdenes), maker_ms_desenlaces_cache.json (100 %, única fuente de desenlace), contabilidad_wallet_dedicada/posiciones.csv (PnL −16,02 € cuadra). Scripts v1-v6.py en el scratchpad de sesión. Nota: la extracción zcat|grep (1,4 GB) corrió 09:17Z con load5 ~5,4, antes de 09:30Z. Ninguna etiqueta autoriza operar en real.

## 1. E-RE-BR-01/02L → CORREGIDO, EXPLORATORY
- Verdad on-chain: 202 rellenos, 1.072,3 acc, 221,30 €, PnL −16,02 €, EV ponderado −0,0724, IC90 por cierre (129) −0,31..+0,20. Por día +0,070/+0,166/−0,267/−0,584. Por moneda ETH +0,032, SOL −0,081, XRP −0,212.
- etiquetado_pasivo_B regenerado 26-Oct 09:01Z: 0 duplicados hoy (el «16/194» ya no verificable: missing); le faltan 7 rellenos (7,97 €, −2,97 €, 6/7 perdedores) → E01 daba 195/213,3 €/−0,061 (sesgo +0,011).
- Descomposición on-chain: SPREAD +0,106 (+0,101..+0,111); SEL +0,048 (−0,20..+0,33); COND −0,227 (−0,44..−0,01). COND por día +0,07/−0,21/−0,46/+0,00; sin el 22-Oct EV +0,045 y COND −0,079 (n=125): significación depende de UN día.
- COND es residuo y está acoplado mecánicamente a SPREAD (para rellenarse a pc el mid debe caer): no es una palanca independiente. Medida directa m_det − pc = −0,092 (n=193).
- «Sin barridos −0,007» = selección (exige mid_120s: excluye 50 de 202 con EV +0,104). Con los 202: tras_cancel 129 (64 % del €) −0,116 vs resto 73 +0,005; dif +0,12, IC90 −0,38..+0,60. Marca tras_cancel inestable (22/193 discrepan lectura vs puja_fin).
- Nivel 1c −0,130 (SOL/XRP) vs 2c +0,043 (todo ETH): confundido con moneda.
- Reparación mínima: recalcular desde on-chain por order_hash; no condicionar a mid_120s; una definición de tras_cancel con hora de exchange (E03); arreglar los 7 rellenos que faltan.

## 2. E01 RE-AS-B → cifras CONFIRMADAS, lectura CORREGIDA
- 39.593 VIDAS (no pujas), 5.068 mercado-lado, 576 cierres, desenlace 99,97 %. Brecha opt −0,280/pes −0,182 = (M_f − M_all)/(1−P): identidad, no demuestra nada sola. M_f −2,16 pp (IC90 −3,70..−0,61); g − mid0 −1,39 pp (−2,91..+0,13).
- Ponderado por € el margen NO es pequeño: opt −0,100 (−0,17..−0,03), pes −0,383; nicho de B (b 0,11-0,29, n=14.744) opt −0,134, pes −0,467. Solo 2 días.

## 3. P(fill) → cruce de unidades CONFIRMADO, cifras corregidas
- 5,32 % por orden (202/3.796) y 55,5 % por puja (202/364; por día 0,70/0,58/0,51/0,46); ~10,43 órdenes por puja. «Puja de B ≈ virtual 52,8 %» NO es calibración (una puja son ~10 órdenes repegadas 1-2c bajo el bid; la vida virtual 5 acc al mejor bid 60 s): coincidencia casual.

## 4. Techo de B → CORREGIDO, EXPLORATORY
- «40× la capacidad R3 a K20» = ~18× (40× es frente a K5). Palancas 1 y 2 se solapan (≈8,2 k€, no 10). Palanca 2 supone EV +0,06 vs medido R3 −0,041 (IC90 días −0,13..+0,05) y K20 −0,050. El 11 k€ es escenario optimista (EV +0,11 supuesto); valor central medido B ≈ −1,5 k€/año.
- «Nicho 15m ETH» NO es B ni 5m barato (mapa_escala: 15m ETH favoritos 0,70-0,99, flujo ~79 k€/día; 1 % cuota ≈6 k€, 5 % ≈29 k€ sin estrés, cuota sin medir). «≲40 k€ techo de B» no es defendible.
- Cuentas que cuadran: 0,10 × 5.479 €/día × 365 = 200 k€; 0,05 × 11 k€/día × 365 = 200 k€.

## 5. Conciliación AS≈0 (piloto) vs −0,216 (reformulación)
Misma identidad medida contra referencias distintas (precio de relleno vs mid al armar). B real on-chain: M_f = −1,49 pp/acc = −0,072 €/€ = el EV. Ninguna demuestra «AS≈0». Brecha por puja −16,5 pp (rellenas −2,1 vs no rellenas +14,4), coherente con 1/(1−0,555).
