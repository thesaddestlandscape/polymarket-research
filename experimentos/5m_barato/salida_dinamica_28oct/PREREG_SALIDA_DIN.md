# PREREG SALIDA DINÁMICA CONDICIONADA (B, 28-Oct-2026, escrito ANTES de ejecutar eval_sal.py)
Visto antes (no ciego): eval_salida.txt del alpha miner (agregados X1..X5, PLAC, D, INV: X4 «vender ya» −0,1164 IS; X1 −0,2236;
R1 HOLD +0,0004 IS / −0,0318 OOS), F8_28oct.md, VALIDACION_ALPHA_B_27oct.md (R1 cota optimista; cola estricta IS −0,015 / OOS −0,046;
con regla C −0,025 / −0,067). NO visto: ninguna cifra de las reglas de abajo.

## Pregunta
¿Existe una regla de salida decidida con el estado en t (reloj de RECEPCIÓN, sin look-ahead) con EV total ponderado por € > 0,
IC90 por días > 0, etiqueta pesimista, que supere placebo e inversión? Informar también EV sin los 2 mejores días y fill-ability de salida.

## Mecanismos rivales
- H0 (martingala + costes): el bid es un estimador calibrado del valor; vender al bid cuesta semiespread + comisión y vender a maker
  cobra a informados (convexidad). Todo Δ(salida − mantener) ≤ 0 en cada celda de estado. (Optional stopping: una regla de parada
  sobre un precio martingala no cambia el EV bruto; solo quedan costes.)
- H1 (sesgo longshot del bid de fichas moribundas, comisión ≈ 0 en extremos): cerca del cierre, el bid de la ficha barata SIN rebote
  supera su frecuencia de acierto en más que la comisión ⇒ Δ_A30 > 0.
- H2 (el relleno informado sigue moviendo el precio): justo tras el relleno el bid aún sobrevalora ⇒ Δ_I1 > 0 en celdas de caída del bid.
Refutan H1/H2: Δ ≤ 0 (o IC90 por días no > 0) en la regla primaria y en toda celda tras max-statistic.

## Datos y población
units/u_2026-10-05..26.csv.gz de alpha_miner_b_27oct (sim.py ADENDA1: reloj RECEPCIÓN, ciego a desenlaces) + desenlace oficial
maker_ms_desenlaces_cache.json, 1 obs por (mercado, lado), unidades con relleno P (P_sh>0). IS = 05-22 Oct (18 d); OOS = 23-26 Oct
(4 d, mirado UNA vez para esta familia). Reproducción obligada: R1 HOLD IS n=25.427 EVw +0,0004; OOS n=5.711 EVw −0,0318 (si no cuadra, parar).
LÍMITE DE DATOS: las unidades guardan solo DOS sondas post-relleno: X4 (tx+250 ms) y X3 (T−30 s + 250 ms). Instantes intermedios y
Binance post-relleno NO están ⇒ NO PROBADOS (fase B = sim con sondas extra; solo si algún Δ_IS IC90d inferior > 0 en IS y OOS).

## Acción y pnl
Salida = venta TOMADORA al bid nivel 1, llegada +250 ms (precio de la sonda), q = min(restante, bs), comisión 0,07·p(1−p)/acción; el resto
se mantiene a resolución. Δ_i = q·(bb − fee(bb) − g_i); pnl_regla = pnl_HOLD + 1{disparo}·Δ_i. Las salidas maker (X1..X3, XI) ya están
REJECTED y no forman parte de las reglas.

## Reglas (cerradas)
- PRIMARIA A30: a T−30 s vender todo al bid si la posición está «sin rebote» (la orden maker X3 sin ninguna venta: NS = proc, fee y rem
  de X3 iguales a los de la pura descarga); si no, mantener. Condición = estado propio + entrada; ejecución = sonda X3.
- Referencia I1-ALL: vender todo en tx+250 ms (X4, ya medida −0,1164).
- Inversión de A30 (PS): descarga a T−30 s de lo que SÍ tuvo venta previa. Placebo de A30: 500 subconjuntos aleatorios (semilla 2711)
  del conjunto con sonda X3 (NS ∪ PS) del mismo tamaño que NS.
- Tablas DESCRIPTIVAS (sin derecho a veredicto) para I1 y A30: Δ por celda (moneda, causa A/B, nº parciales, Te, spread_e, v60, hora,
  espera te→tx) y por celdas de la sonda de ejecución (nivel de bid, Δbid vs avg, bs≥restante; ≤250 ms optimistas), n≥40 y ≥10 días en IS,
  corrección max-statistic por bootstrap de días (nulo centrado, 4.000). Calibración del bid (acierto real vs bid) por tramo.

## Métricas y criterios (fijados antes)
EVw = Σpnl/Σcoste (ponderado por €), IC90 bootstrap por días (B=2.000, semilla 2711) y por cierre, días>0, sin 2 mejores días, n.
Etiqueta pesimista = Δ pareado (no depende de la etiqueta de entrada) sumado al EV HOLD pesimista del validador (IS −0,015 / OOS −0,046).
- REJECTED: Δ_IS(A30) EVw ≤ 0, o IC90d superior ≤ 0.
- EXPLORATORY: Δ_IS EVw > 0, IC90d inferior > 0 y Δ_OOS > 0, pero EV total pesimista ≤ 0 o no supera placebo/inversión.
- CANDIDATE: además EV total pesimista (IS y OOS) > 0 con IC90d inferior > 0, sin 2 mejores días > 0, supera placebo e inversión,
  fill-ability de salida (bs ≥ restante) ≥ 90 % y confirmación con fase B. Nadie autocertifica: validador independiente.
