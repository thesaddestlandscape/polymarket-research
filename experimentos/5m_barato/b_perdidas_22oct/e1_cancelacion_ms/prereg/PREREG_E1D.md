# PREREG E1D (24-Oct-2026 ~11:10Z) — validación poblacional de BN_W300_X2 + «cuándo operar / cuándo no». Escrito ANTES de calcular.
Ya visto (no ciego): E1C (BN_W300_X2 elegida con B 20-21 Oct, test 22-Oct; proxy poblacional 20-22 Oct con mk: sin diferencia). Por eso 20-22 Oct
NO cuentan para H1. Fuente única nueva: VOL/m5_registro_D (05-23 Oct): filas t (operaciones por token, recepción c[6]), x (aggTrade Binance, recepción c[7]), k (mapa).
Desenlace oficial: DL/maker_ms_desenlaces_cache.json (por mid). Universo: 5m ETH/SOL/XRP. Relleno de bid = print SELL del token s a q (bid de s), o BUY de s a p
(= bid del opuesto a 1−p), convención de cola_vs_cruce (W2 volumen vs on-chain 0,995). Banda: 0,10 < q ≤ 0,30. Maker sin comisión, sin rebate.
pnl por acción = gana − q; EV ponderado por € = Σpnl/Σcoste. Unidad = mercado+lado (sumas por unidad); inferencia por CIERRE (bootstrap 2000, semilla 11).

## H1 — BN_W300_X2 en la población (regla congelada, sin tocar parámetros)
Bandera de un relleno en t (recepción del print): existe g en rejilla 10 ms de [t−1000, t−90] con retorno Binance 300 ms ≥2 bps en contra del lado
(−90 = 30 ms lag print + 60 ms cancelación). Política = quitar los rellenos con bandera. Días H1 = 05-19 Oct y 23 Oct (todos los disponibles salvo 20-22).
Gate H1 (alfa 0,05 una cola, hipótesis única), TODO: (a) EV€(bandera) − EV€(sin) < 0 con IC90 por cierre por debajo de 0; (b) EXCESO = ΔPnL − media placebo > 0 con
p_placebo < 0,05 (placebo = quitar la misma fracción de rellenos al azar dentro de cada día, 2000); (c) (a) con el mismo signo sin los 2 mejores días y en ≥60 % de días con n≥30 rellenos marcados.
Latencia real: distribución de lead = t − primer disparo (recepción) para rellenos con disparo en [t−1000, t]; fracción con lead ≥90 / ≥150 ms (capturable con 60 / 120 ms).

## H2 — «cuándo operar»: regla ANTERIOR a la ventana, walk-forward estricto por día
Ventana = mercado 5m (moneda × cierre). Rasgos conocidos en la apertura t0 = fin−300 (solo datos con recepción < t0):
R1 vol Binance 15 min previos (desv. típica de retornos de 10 s); R2 vol 60 min; R3 |deriva| Binance 15 min; R4 hora UTC (bloques de 4 h); R5 moneda;
R6 EV maker poblacional de la misma moneda en los 6 mercados con fin ≤ t0−300 (excluye el inmediatamente anterior); R7 nº de prints en banda de esos 6 mercados (flujo).
K = 7, alfa familiar 0,10 → Bonferroni 0,0143 por rasgo.
Para cada día de test d (desde el 4º día con datos): cortes de terciles (R1-R3, R6, R7) o niveles (R4, R5) con días < d; se SALTA el tercil/nivel de menor EV€ en
entrenamiento. Métricas acumuladas en test: ΔPnL = −Σpnl saltado; EXCESO vs placebo (saltar al azar la misma fracción de ventanas dentro de día, 2000); INVERSIÓN (saltar el
mejor tercil de entrenamiento) debe dar ΔPnL < placebo; IC90 por cierre de EXCESO; sin los 2 mejores días; comparación con «operar siempre» (0) y «azar».
Gate H2 por rasgo: EXCESO > 0, p_placebo < 0,0143, IC90 por cierre > 0, EXCESO > 0 sin los 2 mejores días, inversión < placebo, retención ≥ 40 % del €.
Transferencia (descriptiva): aplicar las reglas a los rellenos reales de B 20-22 Oct (b_cola.csv). €/año: escala B (coste/día real de B) y escala población (Σcoste/día de la banda).
