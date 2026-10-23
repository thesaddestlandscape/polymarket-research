# PREREG R-TEND (23-Oct-2026 ~07:05Z) - detector de regimen causal + regla rpre-skip condicionada
Congelado ANTES de calcular ningun resultado ligado a desenlaces con el detector. Lo anadido despues va marcado POST-HOC. `sha256sum -c PREREG_RTEND.sha256`.
Solo lectura. Sin ordenes, sin claves, B/ejecutores/modulos compartidos intactos. Dato externo: UNICA descarga publica de klines 1m Binance (GET sin clave) para 18-Dic-2025..28-Ene-2026, solo para S_B.

## 0. Pregunta
La regla de W1 (no pujar el longshot CON la tendencia de los 15 min previos, |rpre|>=7,7 bps) sube EV/EUR pero en W1 TEST el PnL total baja 140 EUR (el efecto vive en dias malos). Aqui: (H1) el efecto "CON rinde peor" es estructural?; (H2) un detector causal de regimen predice cuando ayuda/daña?; (H3) la regla condicionada mejora el PnL TOTAL?

## 1. Muestras (n dias independientes)
- S_A DESCUBRIMIENTO, proxy sin precios: klines 1m Binance de `data/backfill/klines/*.json` (Mar-26..Jun-25 y Jul-13..Aug-17 de 2026; dias con 1440 barras completas; hueco 25-Jun..13-Jul). Desenlace = proxy Binance (Up si cierre barra fin >= cierre barra apertura; 88-95 % de acuerdo con la regla oficial TWAP60, igual para CON y CONTRA). Monedas primarias ETH,SOL,XRP; replica BTC,BNB,DOGE.
- S_B CONFIRMACION, proxy sin precios, desenlace OFICIAL: Jon-Becker `markets_*.parquet` (outcome_prices de `*-updown-5m-<epoch>`, closed=true; ~18-Dic-2025..27-Ene-2026) + klines 1m Binance descargadas. Mismo procedimiento.
- S_C PRECIOS REALES (poblacion on-chain): `tendencia_wallets/datos/feats_pop.csv.gz` (17-22 Oct, ETH/SOL/XRP, pc 0,10-0,30, 28.871 unidades con desenlace; DESC 17-19, TEST 20-22) con el detector recalculado desde bookTicker; replica `m5barato_mision/baratas_unidades_D.csv.gz` (5-14 Oct, bandas 0-0,10 y 0,10-0,20, maker+tomador, normalizado a 5 acc).
La proxy NO sustituye al ask real: contesta si el mecanismo es estructural y si el detector discrimina; el dinero lo decide S_C y el forward con ask real.

## 2. Unidad proxy y estadistico (S_A, S_B)
Ventana 5m con apertura t_o (multiplo de 300 s), decision a T=180 s (primaria) o 120 s (sensibilidad). C[t] = cierre de la barra 1m que termina en t.
ret=ln(C[t_o+T]/C[t_o]); s1 = desv. tipica de retornos 1m en los 60 min previos a t_o+T; m=(300-T)/60; z=|ret|/(s1*sqrt(m)); q=Phi(-z) (prob. modelo de que el lado que VA PERDIENDO gane).
Unidad = lado perdedor con 0,10<=q<0,30 ("longshot"). win=1 si ese lado gana. e=win-q (PnL por accion comprada al precio modelo; Sum e = PnL total en acciones iguales); coste=q; EV/EUR = Sum e / Sum q.
rpre = ln(C[t_o]/C[t_o-15min]) en bps. CON si el lado longshot coincide con el signo de rpre y |rpre|>=7,7; CONTRA si opuesto y |rpre|>=7,7; el resto NEUTRO (excluido de Delta).
Delta = EV(CON) - EV(CONTRA). Placebo: permutar la etiqueta CON/CONTRA dentro de dia x moneda x cubo q (0,05), 1.000 perm. IC90 por bootstrap de DIAS (clusters).

## 3. Detector (todo causal con barras cerradas <= t_o; mismas funciones para analisis y etiquetador forward)
Por moneda c y apertura t_o:
- ER60 = |C[t_o]-C[t_o-60]| / Sum|dC| (60 barras). VR240 = var(r5)/(5 var(r1)) sobre 240 min (r5 no solapados alineados a t_o). VOLR = RV60 / RV(24 h previas). DAYT = ln(C[t_o]/C[00:00 UTC]) / (s1 sqrt(min desde 00:00)), NaN si <120 min. COH = |Sum_c sign(r60_c)| sobre BTC,ETH,SOL,XRP (coherente si =4).
- Clase de ventana R (variable familia i): med_ER = mediana de ER60 muestreada en aperturas de los 14 dias previos de esa moneda. TREND si ER60>=med_ER y VR240>=1; REVERT si ER60<med_ER y VR240<1; MIXTO resto.
- Clase de dia D (familia ii): ER_dia_prev = |C[fin dia-1]-C[ini dia-1]| / Sum|dC_15m| del dia UTC anterior; D=TENDENCIA si >= mediana de los 14 dias anteriores, si no RANGO.
- Coherencia (familia iii): COH==4 vs no.
K=3 familias; ninguna otra variable se evalua para decidir. VOLR y DAYT se reportan DESCRIPTIVOS (no deciden). Monedas primarias: ETH,SOL,XRP.

## 4. Hipotesis y criterios
H1 estructural: Delta<0 en S_A y en S_B, cada una con IC90-dias (superior) <0 y placebo p<0,05 (una cola). Si no: el efecto no es estructural y la regla de W1 es del periodo.
H2 el detector discrimina: para cada familia k, interaccion I_k = Delta(clase A) - Delta(clase B) (R: TREND vs REVERT; D: TENDENCIA vs RANGO; COH: coherente vs no). Descubrimiento en S_A: se elige la familia con menor p (bootstrap de dias, dos colas) con Bonferroni x3 (p_adj<0,05) y su signo. Confirmacion S_B: solo esa familia, mismo signo, p<0,05 una cola. Si ninguna pasa en S_A: "el detector no discrimina con estas variables" (resultado valido).
H3 regla condicionada: regla R_cond = saltar unidades CON con |rpre|>=7,7 SOLO en las clases donde Delta estimado en S_A es <0 (por clase, de la familia ganadora de H2; si H2 falla, R_cond no se define). Metrica = PnL TOTAL: Dp = -(Sum e de unidades saltadas), por dia. Exito: Dp>0 con IC90-dias inferior >0 en S_B, MEJOR que R_incond y que el placebo (mismo numero de saltos al azar en dia x moneda x cubo q), y en S_C TEST PnL total de R_cond >= 0 (R_incond: -140 EUR) con IC90 por cierre; replica baratas sin cambiar signo. Se reporta tambien Dp sin los 2 mejores dias.
Dia-nivel: Spearman(D de hoy, Dp del dia) en S_A, S_B y S_C (descriptivo).
Sensibilidades (no deciden): T=120; BTC/BNB/DOGE; umbral rpre relativo (mediana |rpre| 14 d); desenlace oficial vs proxy en las 40 d solapadas S_B.
Potencia: se reporta el MDE (1,64*SE de Delta, dias como clusters) de cada muestra; el verdicto "sin potencia" solo es admisible si el MDE > efecto de W1 (~0,10-0,25) en S_A+S_B conjuntas.
## 5. Gate de promocion forward (ver INFORME)
Se fija en el INFORME con el calculo de dias. Nada se cambia en B sin variante + /code-review + OK Javi.
