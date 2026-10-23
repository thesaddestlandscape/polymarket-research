# Para el agente cosechar_abrir: qué hacen los que SÍ ganan con pares (on-chain 17-22 Oct). EXPLORATORY, descriptivo
Fuente: `datos/btc_cosech.txt` (BTC 5m 17-21, VOL/m5_onchain), `datos/an_wallets.txt`, `datos/res_pareadoras.txt`, `datos/diseccion_alts.txt`
(ETH/SOL/XRP 5m 17-22, cola_vs_cruce/datos/oc_D). Desenlace oficial 100 %. PnL sin rebate. Unidad wallet-mercado; venta de X a s = compra del contrario a 1-s.

## 1. Los tres cosechadores de BTC del 09-Oct, hoy
| wallet | universo | merc (5 d) | vol | PnL/vol | par | residuo | comisión | maker | coste par med | max|I| med | P(siguiente relleno reduce |I|) | acc/relleno | días + |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0x21f4c1a1 | solo BTC (0 filas en alts) | 1.391 | 931 k$ | **+1,21 %** | +6,1 % | −4,7 % | −0,2 % | 0,87 | 0,934 | 399 acc | 0,447 (no reequilibra) | 13 | 4/5 |
| 0xaa1a4f31 | solo BTC | 1.411 | 734 k$ | −0,20 % | +8,1 % | −8,3 % | 0 | 1,00 | 0,923 | 274 | 0,464 | 13,5 | 3/5 |
| 0x41e2e1cc | BTC + ETH/SOL (no XRP) | 1.314 BTC / 2.482 alts | 1,33 M$ BTC / 103 k$ alts | −0,48 % BTC / ≈0 alts (−0,32 % y +0,15 %) | +0,4 % / +3,3..5,2 % | +0,7 % / −0,6..−1,9 % | −1,6 % / −3,0 % | 0,39 BTC / **0,00 alts (tomador puro)** | 0,999 / 0,944 | 191 / 40 | 0,586 / 0,545 | 17 / 14 | 0/5 BTC |
Lectura: de los tres solo 0x21f4 sigue ganando, ~+1,2 %/vol (+11 k$ en 5 días por volumen enorme). **Ninguno evita la pata suelta**: el residuo
pierde −4,7/−8,3 % del volumen; ganan si el margen del par (comprar ambos lados ~6-8c por debajo de 1 a lo largo de la ventana) supera al residuo.
0x41e2 en alts es TOMADOR y la comisión (−3 %) se come el margen del par.

## 2. Alts 5m: «pareadoras» elegidas por CONDUCTA en 17-19 (≥30 merc, ≥60 % con ambos lados ≥5 acc; sin mirar PnL), medidas 20-22
- Grupo (51 wallets, 875 k$ TEST): PnL/vol **+0,03 %** IC90 días (−0,49 %, +0,79 %); par +5,6 %, residuo −4,7 %, comisión −0,85 %; maker 65 %.
  Placebo direccionales (626 wallets): −1,20 % (IC90 −1,76 %, −0,88 %). Mixtas −0,95 %. Todas las wallets: −1,01 %.
- La pata suelta pierde siempre: residuo gana 28,7 % frente a un precio pagado de 34,9 % (27.973 unidades, ponderado por acciones).
- Dosis-respuesta del residuo (ex post, NO accionable por sí solo): res_frac <0,1 +4,0 %/vol; 0,1-0,3 +2,4 %; 0,3-0,6 −1,1 %; >0,6 −11,6 %.
- Mitad mejor en DESC → TEST +0,31 % (IC90 −0,19 %, +1,05 %) vs mitad peor −2,8 %: persistencia débil, no significativa.
- Casos (elegidos VIENDO el TEST: exploratorio): 0xf074dc84 (ETH, 100 % maker, vende ambos lados = asks) +0,85 %/+1,1 %; 0x0ab01745 (ETH, 100 % maker,
  asks) +1,3 %/+1,5 % 5/6 días; 0x43e7e4b6 (ETH/SOL, 87 % maker) +3,7 %/+1,5 %; 0xae68447c (ETH, maker) +1,6 %/+0,4 %; 0x31393e2f (ETH) +4,0 %/+3,3 %.

## 3. Cómo LIMITAN la pata suelta las dos que mejor lo hacen (0xf074, 0x0ab0; `diseccion_alts.txt`)
- Lotes de **5 acc** (p90 10-15), **15 y 10 rellenos/mercado**, toda la ventana (T p10 49-57 s .. p90 277 s), precios 0,3-0,5 la mayor parte.
- **Tope de inventario minúsculo**: max|I| mediana 14 / 17,5 acc (p90 23 / 32); final |I|/acc 0,08 / 0,13.
- **Reequilibran**: P(siguiente relleno reduce |I|) 0,64 / 0,55 (las que no reequilibran: 0x43e7 0,43, 0xae68 0,48, 0x21f4 0,45).
- **Cola**: 0xf074 va DELANTE (rango medio 0,29, primero en el 70 % de niveles compartidos); 0x0ab0 detrás (0,64). 0xae68 detrás (0,76).
- Cotizan con ASKS (venden; implica acuñar pares) en vez de pujas. Solo ETH. Retraso entre la 1.ª pata de cada lado: mediana 16 s / 27 s.
- Margen: coste par mediano 0,975 / 0,964 (≈2,5-3,5c), muy por debajo del de 0x21f4 (0,934): menos margen, mucho menos residuo.
**Implicación para cosechar al abrir:** el patrón que gana NO es «poner un par al abrir y esperar» (eso es lo refutado en BTC: 81 % pares completos y aun así −5,7 %),
sino cotizar ambos lados en continuo con clips de 5 acc, inventario ≤~15-30 acc y sesgo de cotización hacia el lado que falta.
Ganan ~+1 %/vol + rebate. Su cola (delante en 0xf074) no la podemos medir sin órdenes reales (registro ms solo top: DATA_BLOCKED), y la
capacidad a nuestra escala es pequeña (ver INFORME.md §4).
