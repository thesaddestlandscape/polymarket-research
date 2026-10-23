# PREREG P3 — predecir/mitigar la continuación ex post (X2/C2) con señales L2 causales (22-Oct-2026 ~18:00Z). Orden de Javi vía chief.
Congelado ANTES de calcular ninguna señal. Visto antes (declarado): P1 (AVANCE), P2 completo en ELEGIR y MEDIR (incl. familia B_FIEL:
B_FIEL fiel a B real —tasa de relleno 0,58 vs 0,61 real, acuerdo puja a puja 0,74—; BF_RAPIDO = cancelar a 65 ms en vez de 280 ms:
ELEGIR +0,155 vs B_FIEL con retención 0,42; MEDIR +0,105), y que cola_posicion ve que en ~60 % de los rellenos no queda nadie a −100 ms.
Binance (S1) NO se re-prueba aquí: está en confirmación E1b (no duplicar).

## Instrumento
E1Q con la política B_FIEL (top−k recalculado cada 100 ms, cancelación efectiva +280 ms, reposición tras 1,5 s, 5 acc). Señales por tick de
100 ms con el libro L2 por RECEPCIÓN ≤ t, lado L de la puja, nivel o = objetivo B_FIEL en ese tick:
- SCANC: tamaño CANCELADO (bajadas no explicadas por operaciones) en niveles ≥ o en (t−1 s, t] / (tamaño en esos niveles en t−1 s + 1).
- SFINO: −log(1 + acc en niveles > o + acc en o) (colchón delante fino = alto).
- SCAIDA: caída del top bid en ticks en (t−2 s, t].
- SVEL: nº de cambios del top bid en (t−2 s, t].
- SIMB: (Σ asks 3 niveles − Σ bids 3 niveles)/(suma) del lado L (asks de L = bids del contrario espejados).
- SFLUJO: acc tomadoras que golpean bids de L en (t−2 s, t].
- SEDAD: −edad (ms) del último cambio del top.
- LOGIT: logística (estandarizada, sin regularizar) de las 7 señales para y = X1∪X2 en los rellenos B_FIEL de ELEGIR, rasgos en r_fill−300 ms.
## Regla de mitigación
Si la señal ≥ umbral en un tick: cancelar la orden viva (efectiva +280 ms) o no postear; bloqueo 2 s. Umbrales = cuantiles de ELEGIR sobre
ticks con objetivo válido: tasa de disparo 5 % y 15 % (16 reglas). Placebos: disparo ALEATORIO por tick con la misma tasa (5 %, 15 %; semilla fija).
## Métricas
(a) AUC de cada señal (rasgos en r_fill−300 ms) para X2 y para X1∪X2 en rellenos B_FIEL, ELEGIR y MEDIR por separado.
(b) Política: EV €/€, € PnL y retención frente a B_FIEL; diferencia pareada por mercado con IC90 por día y por cierre; control de igual
volumen (p2_eval) y frente al placebo de la misma tasa (diferencia regla − placebo).
## Selección y gate
ELEGIR 17-19: se elige UNA regla = mayor (EV_regla − EV_placebo_misma_tasa) con retención ≥ 0,70. MEDIR 20-22: gate = EV_regla − EV_B_FIEL
> 0 con IC90 por cierre > 0, ≥ 2/3 días, EV_regla > EV_placebo_misma_tasa, p igual volumen < 0,10, retención ≥ 0,70. Si falla: REJECTED.
