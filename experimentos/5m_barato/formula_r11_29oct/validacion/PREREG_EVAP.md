# PREREG EVAP (validador independiente, 29-Oct-2026 ~13:40Z, ANTES de calcular nada en L2)
Visto antes: salida_r11.txt, EXPEDIENTE R11 (categorías A/B/C/D y sus EV), formato de libro5_ms (cabecera y primeras filas). NO he mirado
ningún nivel L2 alrededor de órdenes de B ni ningún EVAP.
## Datos
Órdenes y verdad: `datalogs/calibracion_etiqueta/ordenes_b.csv` (dia 2026-10-23: 524 órdenes, 16 rellenas, 06:30-08:56Z) + `b_fills_onchain.csv`.
L2: `/mnt/HC_Volume_106538179/libro5_ms/libro5_ms_2026-10-23_331840.csv.gz` (filas B=snapshot, d=nivel absoluto, T=print), reloj = RECEPCIÓN
(col `recepcion`). Solo tokens de B y sus complementarios. B no operó del 24 al 28-Oct: «23-28 Oct» para rellenos de B = solo 23-Oct.
## Definiciones (fijas)
- L(t) = tamaño del nivel BID a precio p (el de la orden) en el token tk, último valor recibido ≤ t. Prints en nivel = T en tk a p (cualquier lado)
  o T en el complementario a 1−p.
- t_fill = recepción del print propio en libro5 (T en tk a p o comp a 1−p, |tamaño − relleno on-chain| ≤ 0,011, en [t_ini−2 s, t_fin+5 s], el
  más cercano a t_fin); si no hay, t_fill = t_fin. Para no rellenas, t_end = t_fin.
- Base: Q0 = L(t_ini − 100 ms) (cola delante, sin nosotros). Delante estimado a(t) = max(0, L(t) − s) para t ≥ t_ini + 150 ms.
- **EVAP** (primaria, única): primer t en [t_ini+150 ms, min(t_fill, t_end)) con Q0 ≥ 1 y a(t) ≤ 0,5·Q0, sin NINGÚN print en el nivel en
  [t_ini, t]. Q0 < 1 → clase «sin cola» (no puede haber EVAP). Sin look-ahead: el evento es estrictamente anterior al relleno.
## Pruebas
P1 (discriminación, una obs por orden rellena): tasa de EVAP previa al relleno en C (solo-propio, mi recategorización independiente) vs A∪B.
   Fisher exacto unilateral (C > A∪B). Decisión «discrimina» si p<0,05 y diferencia ≥20 pp. Adicional descriptivo: a(t_fill−) en C.
P2 (política): cancelar a t_EVAP + 60 ms. Relleno evitado si t_EVAP + 60 < t_fill. Δpnl = −Σpnl de los evitados (rebate 0; no se modela
   la repuja perdida). Placebo: cancelar con la misma probabilidad por orden que la tasa EVAP y retraso desde t_ini muestreado de la
   distribución empírica de retrasos EVAP, 2.000 réplicas → percentil del Δpnl real. «Evitaría pérdidas» si Δpnl>0 y percentil ≥95.
P3 (markout, una obs por orden con Q0≥1): mid del token a t_e+10 s menos mid a t_e (céntimos; mid=(bb+ba)/2 de L2), t_e = t_EVAP o, sin
   EVAP, t_ini + retraso placebo (misma distribución); y desenlace (gana_lado − p)/p. Diferencia EVAP − no-EVAP, IC90 bootstrap por puja.
Cortes: por moneda (sol/eth/xrp). sin2 no aplicable (1 día). Multiplicidad: una sola definición/ventana primaria → sin corrección.
Etiqueta máxima posible: EXPLORATORY (1 día, n rellenas=16). Gate futuro (sin relajar): n≥40 rellenos C con L2, ≥10 días, IC90 por días.
## Parte 1 (revisión R11) — recálculo propio desde mk_D (no desde r11.py)
Categorías A/B/C/D con prints ajenos en [t_ini, t_fin+250 ms], dedup token/complementario (mismo tamaño, precios suman 1, ≤300 ms, se
descarta el segundo), casado propio por tamaño (exacto ±0,011, si no resta del print ≥), EV Σpnl/Σcoste, IC90 bootstrap por puja y por día.
