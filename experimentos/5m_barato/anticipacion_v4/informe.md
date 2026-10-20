# Anticipación V4 — informe 20-Oct-2026 (pasos 1-4). EXPLORATORY
BTC, 06-18 Oct (13 d; rivales 09-18), desenlace oficial 100 %, recepción, ask real nivel 1, EV ponderado por €. Códigos y salidas `p1`-`p7` en esta carpeta.

## Mecanismo de R1/R2/R3 (paso 1)
Solo 5m anidado (0 fills en :05/:10); lado s 97-98 %; disparan por un evento (libro estático 2-3 % vs 29-32 % placebo; margen sube ≥1c en 1 s 73-82 %) con umbral laxo (margen P50 −0,046/−0,036). **H-B (p3, 3 días, n=113+82 1ªs ráfagas)**: el envío acotado cae P10/50/90 = 35/113/188 ms (R1) y 24/100/227 ms (R2) tras la última subida de margen (placebo P50 1.004/705 ms; ≤250 ms 84-94 % vs 27-33 %); el evento es bid15 en 51-58 % y ask5 en 42-49 %. Su reacción (~100 ms, cota) no es más rápida que nuestro feed (+42 ms) + decisión (0,8 ms): **no hay déficit de velocidad pura**; el retraso tomador de 145 ms les afecta igual.

## H-A como tomador (paso 2): NO SOBREVIVE
Cuatro variantes fijadas antes: A (m≥−0,05, subida ≥1c) 1ª/cierre EV −0,086 (n=262; TEST −0,363; Bonferroni inf −0,42); re-armes −0,336; B (m≥−0,02) −0,430; C (cruce) −0,042; D (m≥0) +0,292 (n=38, sin 2 mejores −0,128). Las no ejecutadas ganan 54-58 % vs 24 % de las ejecutadas (selección adversa). Pérdida concentrada en ask≤0,15 (164/257, acierto 4 %, −0,28). Filtro de calidad (4 variantes, elegida en DESC, un solo TEST): ask≥0,30 y T≥120 → TEST +0,045 (n=23, IC90 cierre −0,22;+0,31).

## Ventajas competitivas: ranking
1. **Maker H23 con cancelación 60 ms** (los rivales son tomadores; ventaja estructural medida 68/60 vs 213 ms): +0,795 (n=17, IC90 cierre +0,14;+1,35, sin 2 mejores +0,25, P=0,021); TEST n=2. Falta H47.
2. **Umbral 0,02 tomador (H53)**: +0,507 (n=24, IC90 cierre +0,06;+1,01, sin 2 mejores +0,11; DESC +0,52/TEST +0,47 n=6). Frecuencia cayendo (2,6→1,0/día).
3. **Combinación una vía** (H54): +0,457 (n=25): NO aditiva.
4. **Selección de cierres**: dentro de cierres operados por rivales nuestra entrada A rinde +0,002 (n=65) y fuera −0,183 (n=192); ellos eligen ask/bid15 más altos (AUC 0,71/0,72), T mayor (0,67). No convertible en regla (filtro ≈0). **Su ventaja no está probada**: EV de unidades rivales BTC +0,239 (IC90 cierre +0,03;+0,44) pero sin 2 mejores días −0,004, 5/10 días positivos; 1ª ráfaga +0,107/+0,081; las siguientes +0,315/+0,155 (nuestras re-armes A −0,34).
5. **Monedas**: R1/R2 no operan altcoins (R3 13-25 unidades/moneda, mixto). Campo (todas las tomadoras, 10 d) lado s vs opuesto: SOL +0,002/−0,059, XRP +0,019/−0,062, BNB −0,007/−0,048, ETH −0,034/+0,003, DOGE −0,015/−0,029, BTC −0,027/−0,015: sin sesgo explotable por el campo. V4 vigía 05-19 Oct: 38 eventos en alts vs 33 BTC, 14 ejecutables, EV L215 negativo (n≤5/moneda): **hueco sin medir** a umbral 0,02 (exige extraer alts del archivo m5/m15, pesado).
6. Sin evidencia (solo experimento): 15m/60m, ballenas, L2 profundo, TWAP [e−62,e−3]; los rivales no usan Binance (AUC 0,44-0,52) ni z.

## Preregistro (paso 4)
H53 y H54 en `misiones/5m_barato/docs/REGISTRO_HIPOTESIS.md` (regla congelada, gate, kill, OOS ≥19-Oct). Falsador: no batir a V4 emparejada en cierres >18-Oct (IC90 por cierre).

## Huecos / siguiente
Extraer 19-20 Oct BTC (OOS); alts (ETH/SOL/XRP) a umbral 0,02 desde `m5_registro`; modelar selección de los rivales con orden de log_index on-chain; envío rival = cota.
