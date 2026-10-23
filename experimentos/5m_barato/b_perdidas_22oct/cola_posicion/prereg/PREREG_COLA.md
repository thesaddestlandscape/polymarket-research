# PREREG COLA — posición de B en la cola y su relación con el EV (22-Oct-2026 ~17:15Z). Solo lectura; B/supervisor/procesos sin tocar.
Congelado ANTES de calcular ninguna métrica de posición de B ni EV por posición. Declarado lo YA visto: (a) pares_huecos: rango en cola de otras
wallets (diseccion_alts.txt: 0xf074 primero 70 %, 0xae68 18 %...) y su hipótesis H39b; (b) cola_vs_cruce AVANCE.md (EV por clase C1/C2/C3, B y población) y
r3 (cola/cruce WS B +0,190 n=85 / −0,091 n=59); (c) estructura del ledger de B y de la tx on-chain en 6 ejemplos mirados a mano (para entender los campos).
NO visto: rango/n_same/A0 de B en agregado, EV por posición, timestamps de calldata.

## Datos y unidades
- B: snapshot del ledger H47-B (sha256 en snap/, 22-Oct 16:34Z) + movimientos.csv (idem). Unidad B = ORDEN con relleno (hash on-chain = oid del ledger), fila de relleno = primera por (bloque, log_index).
  Missing (no se imputan): 3 rellenos 22-Oct >14:40Z sin mapa de tokens/L2 (entran en la parte on-chain, no en L2).
- Población: oc_D + tok_D de cola_vs_cruce/datos (17–22 Oct, ETH/SOL/XRP 5m); unidades como en P1: primeras 5 acc por (maker, mercado, token c), pc∈(0,10;0,30],
  T∈(60;300] s, sin la wallet de B; pnl = acc·gana − coste (sin fee ni rebate, como P1); desenlace oficial (cache + desenlaces_extra), sin desenlace = excluida y contada.
- Precio equivalente: BUY c a x → (c,x); SELL del complemento c' a x → (c,1−x). El libro es UNIFICADO (verificado: ask_Y = 1−bid_N y tamaños iguales en el npz del 21-Oct):
  la cola de un nivel mezcla ambas; las filas de una tx se ordenan por precio y luego por log_index (li).
- Nivel «mismo» = |px_eq − pc| < 0,0005. Orden = (bloque, li); NUNCA hora de bloque (≈ +2,4 s, ±1,5 s).
## Métricas de posición (de la fila del relleno, entre makers de la MISMA tx)
n_same, rank_same (0-based por li), q = rank/(n_same−1) (n_same≥2), sh_ahead_same (acciones de los makers del mismo nivel con li menor), sh_better (acc. de makers
con mejor precio antes), sh_beyond (acc. después de nosotros, mismo nivel o peor). Clase POS1: SOLO (n_same=1) · FRENTE (n_same≥2, rank 0) · CENTRO (n_same≥3, ni primero ni último)
· ATRAS (n_same≥2, último). Pre-relleno (solo B, accionable): A0 = cola del ledger (nivel al postear) y A0_book (L2 antes de verse la orden), espera hasta el relleno.
## Pregunta 3 (veredicto delante/medio/detrás), unidad: relleno de B con n_same≥2
S1 = media de q (nula 0,5); S2 = P(primero) frente a E0 = media de 1/n_same (nula exacta bajo orden aleatorio). IC90 bootstrap por tx y por día (2.000, semilla 20261022).
DELANTE: IC90 de S1 con techo <0,5 Y IC90 de S2−E0 con suelo >0. DETRÁS: IC90 de S1 con suelo >0,5 Y IC90 de S2−E0 con techo <0. Si no: EN MEDIO / NO DISTINGUIBLE DEL AZAR
(se reporta la diferencia mínima detectable con ese n). También percentil de S1 de B entre wallets de población con ≥30 observaciones multi-maker (17–22 Oct).
Además se reportan: P(A0=0), mediana y cuantiles de A0, quién va delante (wallets), acciones delante, y — con timestamps de la calldata de matchOrders si se obtienen (RPC público de
solo lectura) — fracción de co-makers «por delante» en li cuya orden se FIRMÓ después de la ráfaga de postear de B (timestamp > t_ret de B = llegaron después con certeza).
## Pregunta 4 (posición ↔ EV), población 17–22 Oct (muestra principal) y B (descriptivo)
EV = Σpnl/Σcoste (ponderado por €). IC90 bootstrap por DÍA y por CIERRE (fin del mercado). Contraste PRIMARIO: EV(ATRAS) − EV(FRENTE), población. Secundarios (no
cambian el veredicto): ATRAS vs resto; SOLO vs multi; terciles de sh_ahead_same+sh_better (profundidad de la ráfaga hasta nosotros); B con terciles de A0.
Placebo: 2.000 permutaciones de la clase POS1 entre unidades del MISMO mercado (mismo mid) → p = P(diferencia placebo ≤ observada); además dentro de (mid, c).
Sin los 2 mejores días y mitades 17–19 / 20–22. Reglas: «posición ATRAS es adversa» solo si diferencia<0 con IC90 por día Y por cierre <0, p placebo<0,10, ambas mitades<0 y
sin 2 mejores días <0. «No concluyente» en otro caso. Con B (n≈180) no hay potencia para IC: se reporta con su n y sin conclusión salvo que cumpla lo mismo.
Probabilidad de relleno: sobre las ~3.270 órdenes de B (con su A0 del ledger y censura por vida de la orden), tasa de relleno por segundo en riesgo por tercil de A0, estratificada por moneda y k; descriptivo.
Anclas de validación: oid del ledger = order_hash on-chain; li vs reconstrucción L2 (tamaño de nivel antes de la ráfaga ≥ acciones del nivel en la tx); orden de timestamps firmados vs li.
