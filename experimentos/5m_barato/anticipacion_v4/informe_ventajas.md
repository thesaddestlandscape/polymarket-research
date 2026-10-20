# Ventajas de los rivales R1/R2/R3 — informe 20-Oct-2026. EXPLORATORY
BTC, 06-18 Oct (rivales 09-18), desenlace oficial 100 %, recepción, ask real nivel 1, EV ponderado por €. Códigos/salidas `p8`-`p13`.

## (6) Discrepancia conciliada (`p8_concilia.py`)
En los 13 ejecutables comunes (30 cierres) el vigía (niveles 1-3) y mi simulación (nivel 1) son IDÉNTICOS: t0 igual (Δ 0 ms), mismo ask, precio, acciones y PnL +32,55 sobre 30,6 € (EV +1,063). El +1,988 (n=15, 34,5 €) = esos 13 + 2 eventos fuera de mi ventana: 05-Oct (pre-OOS, ask 0,05, 40 acciones, ganó, ≈+37,8 €) y 19-Oct (−1,8 €). Sin la cola de 0,05: ≈+0,95. Mi +0,507 es OTRA regla (V4b, umbral 0,02): comparación mal hecha antes, no hay error de nivel.

## Ventajas que SÍ tienen (ranking, EV medido en sus fills)
1. **Capital/tamaño**: mediana 147 $/unidad (R1), 526 acciones; ~60-100× nuestro stake. No barren profundidad: 1 orden por ráfaga (P90 3), 33 acciones (R1)/9 (R2), vwap−ask mediana 0 c, 85 %/70 % a ≤ ask, solo 15 %/7 % superan el nivel 1. No es límite de profundidad: es capital. Recurso que falta: stake (≥ decenas de $; hoy 2 €).
2. **Bolsillo robusto = favorito (precio 0,7-1,0)**: R1 +0,131, IC90 cierre (+0,04;+0,20), 10/10 días, sin 2 mejores +0,110 (45 cierres); R2 +0,142 (6/8 días). T>200 s precio 0,7-1: R1 +0,214 (9/10 días). Réplica nuestra (`p11`, F1 ask 0,70-0,95, m≥−0,05): +0,083 (n=22, 9/11 días +, sin 2 mejores +0,031); F3 (0,50-0,95): +0,179 (n=36, IC90 cierre +0,005;+0,34, Bonf×4 inf −0,058, TEST +0,235 n=14) → **H55**.
3. **El resto de su PnL no es robusto**: unidades BTC +0,239 pero sin 2 mejores días −0,004; todas las celdas por índice de ráfaga, dirección de precio o dt dan sin 2 mejores ≈0 (`p12`): +18,99 k$ de R1 en 10 días dependen de 2 días (EV diario de −0,93 a +1,81).
4. **Selección**: logística entrenada 09-12 → AUC holdout 0,751 (T alto +0,58, tamaño bid15 +0,37, subida de margen +0,38, margen −0,40). Pero nuestra entrada A en el top 30 % predicho: −0,257 (n=26); en cierres que sí operaron: −0,099 (n=28) vs −0,453 fuera. La selección explica diferencias relativas, no EV positivo absoluto.

## Dimensiones sin ventaja
- **Salida/cobertura**: sin ventas (R2: 39 ventas, 210 acciones); 0 % de mercados con ambos lados; mantienen a resolución. Unidad R1: 47 % positivas, mediana −3,74 $.
- **Costes**: fee observado/teórico (0,07·p(1−p)) = 1,000 en R1, R2 y R3; ni rebate ni descuento. Idénticos a los nuestros (solo el maker propio cobraría 20 % de rebate).
- **Información**: Binance AUC 0,44-0,52, z 0,47, FV GBM 0,49-0,52; mi FV anidado (bid15 + excedente P(ref5≤P_C<ref15) con gap TWAP, spot y σ causal, `p13`): E0-E2 EV +0,002/−0,052/−0,094 (TEST −0,34/−0,39/−0,33), E3 +0,039 (n=36). Sin información extra demostrada. Orden de log_index y TWAP [e−62,e−3]: no probados como señal.
- **Velocidad**: reaccionan ~100 ms (cota) tras la subida de margen; no más rápido que nuestro feed.
- **Monedas**: R1/R2 solo BTC; campo en altcoins sin sesgo (informe previo).

## Siguiente
Forward H55 en sombra desde 19-Oct (extraer 19-20 Oct); si pasa gate, escalar solo por decisión de Javi (capital); medir el bolsillo favorito en alts con `m5_registro`.
