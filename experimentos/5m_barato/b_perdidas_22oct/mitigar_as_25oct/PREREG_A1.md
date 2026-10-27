# PREREG A1 — ¿Distingue el libro L1 en los 2 s previos (por RECEPCIÓN) los rellenos maker adversos? (25-Oct-2026 ~11:55Z)
Escrito ANTES de extraer ni mirar ningún resultado de estos rasgos. Solo lectura. Nada a real.

## Población (fija)
Rellenos maker de bid poblacionales de E1D (`DL/e1_cancelacion_ms/e1d_dia_D.pkl`, construidos por `e1d_pob.py` desde VOL/m5_registro):
banda q en (0,10, 0,30], 5m ETH/SOL/XRP, último 300 s de la ventana, desenlace OFICIAL (cobertura declarada en E1D 100 %).
Unidad = print (fila t) ponderado por € (coste = q·acc). Días 06..23-Oct (05-Oct parcial EXCLUIDO). Convención E1D: SELL → bid del token s;
BUY → bid del opuesto a 1−p. Token del maker = token (mid, lado_m) del mapa k.
Diferencia con lo cerrado: E1C (KNIFE/DEPTH/L15) se probó sobre 55 rellenos de B; E1D H1 = Binance; F8 = rasgos ESTÁTICOS al armar sobre
vidas VIRTUALES. Aquí: rasgos DINÁMICOS del libro propio en ≤2 s antes del relleno, sobre prints REALES de toda la población (no etiqueta virtual).

## Rasgos (q del token del maker, VOL/m5_registro filas q: bid, ask, tam_bid, tam_ask, recepción c[7]); τ = r − 100 ms (r = recepción del print)
F1 spread(τ)=ask−bid · F2 imb(τ)=tb/(tb+ta) · F3 dQ=log1p(tb(τ))−log1p(tb(τ−2000)) · F4 vmid=mid(τ)−mid(τ−2000) ·
F5 log1p(ta(τ)) · F6 nº de filas q en (τ−2000, τ] · F7 edad del top = τ − última recepción en que cambió bid o ask · F8 T restante = fin − r.
Estado = última fila q con recepción ≤ instante (ordenado por recepción; si la recepción retrocede >60 s se reinicia, trampa m5_registro).
Sin fila q previa ≤30 s → rasgo `missing` (no se marca nunca; se cuenta). Libros cruzados (bid≥ask) en τ → missing.

## Regla (walk-forward por día; selección y medida en días DISTINTOS)
Para cada rasgo y día de test d ∈ 09..23-Oct (15 días): entrenamiento = todos los días 06..d−1. Terciles por cuantiles del entrenamiento;
se marca el tercil con menor EV€ (Σpnl/Σcoste) en el entrenamiento ("cancelar si el rasgo cae en ese tercil"). INVERSIÓN = marcar el de mayor EV.
Métrica del día: EXCESO_d = f_d·Σpnl_d − Σpnl_marcados_d, con f_d = Σcoste_marcados/Σcoste (placebo = quitar la misma fracción de € al azar).

## Gate (K=8, todos a la vez)
(1) ΣEXCESO>0 e IC90 por días (t, n=15) inferior >0; (2) p unilateral por días < 0,05/8 (Bonferroni) y BH-FDR q<0,10;
(3) sin los 2 mejores días >0; (4) INVERSIÓN ΣEXCESO<0; (5) ≥10/15 días con EXCESO>0; (6) IC90 bootstrap por CIERRE (cluster fin, 1000) inferior >0;
(7) EV€ retenido > EV€ total con IC90 días de la diferencia >0. Descriptivos obligatorios: tasa de disparo en instantes de CONTROL
(r − U[5,30] s, mismo token, bid en banda) frente a la tasa antes del relleno; sensibilidad τ = r − 250 ms; por moneda; EV€ retenido absoluto.
Pasa → PROMISING (población, prints; NO es la cola de B ni su nivel 1,5c bajo el mejor bid). No pasa ninguno → REJECTED para rasgos L1 ≤2 s.
€/año: ΔEV€ × coste diario de B (y techo poblacional aparte, no capacidad propia).
