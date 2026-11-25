# PREREG ALPHA-B «ENTRADA + SALIDA» (alpha miner, 27-Oct-2026 ~15:05Z)
Escrito ANTES de ejecutar sim.py / eval.py sobre datos reales. Ninguna cifra de estas reglas vista.
Visto antes (no ciego): FRENTE-TD −0,217 / FRENTE-FAV −0,056 / E-TD / SEGFAV / palanca 1 / Q4 (todos 24-26 Oct, reglas distintas).
Contrato de datos comprobado (no resultados; 6 M líneas del 26-Oct): libros q espejo exacto YES/NO (88,5 % de pares de
estados; el resto, desfase de actualización); filas t NO duplicadas en el complementario (104/77.214 coincidencias).

## Datos
m5_registro 05..26-Oct (22 ficheros, /mnt/HC_Volume_106538179/m5_registro/), filas k/q/t/x. Reloj = RECEPCIÓN
(q c7, t c6, x c7; si falta, c1 y se cuenta). Desenlace = maker_ms_desenlaces_cache.json (missing = fuera, contado).
sim.py NO lee desenlaces (ciego). Unidad = mercado-lado (token) 5min de BTC/ETH/SOL/XRP/DOGE/BNB con cierre en el día
del fichero. 1 observación por unidad. YES = Up (como FRENTE/E-TD).

## Mecanismo y predicción
H-SAL: la pérdida de B es selección por relleno (relleno informado: 94 % lo provoca quien compra el favorito).
Si tras el relleno el barato rebota con flujo no informado, vender el relleno en maker a avg+0,01 convierte parte de
los rellenos en +1 c/acc y deja la residual. Predicción diferenciadora: Δ(X1−HOLD) > 0 en rellenos reales y mayor que
en el placebo (entradas sin selección). Nula: precio martingala + contrapartes de salida informadas (FRENTE-FAV) ⇒ Δ ≤ 0.

## Entrada maker E (común a R1/R2)
- Elegible en t si el estado del token con recepción ≤ t−130 ms (LR = cancelar 60 + colocar 68) tiene edad ≤ 30 s,
  bb ∈ [0,10; 0,29], ba−bb ≥ 0,02, T = cierre−t ∈ [60; 290] s y NO hay salto Binance adverso (|ret| ≥ 2 bps en 300 ms,
  recepción; YES adverso = bajada, NO = subida) en (t−1000, t−100] ms (TD: cancelamos a +100 ms, reponemos a +1 s).
- P (PRIMARIA, recotización continua = Q1 límite): puja virtual 5 acc a b'(t) = bb(t−130)+0,01 (cabeza de cola).
  L1 / L5 (secundarias, vida 1 s / 5 s): b' se fija cada 1 / 5 s desde te.
- Relleno por acción, parcial acumulado hasta 5, cada parcial al b' vigente: (A) print t SELL del token a p ≤ b';
  (B) print t BUY del complementario a p ≥ 1−b' (espejo); (C) ba del token ≤ b' (min(resto, as_), una vez por nivel).
  Fin de entrada: 5 acc o T = 60 s (un parcial se gestiona igual).
- te = primer instante elegible (referencia del placebo y del tomador).

## Salidas (alternativas sobre las MISMAS entradas)
- X0 HOLD → R1 (candidata b, Q1).
- X1 → R2 (candidata c, PRIMARIA del mandato): a t_fin+150 ms ask maker por la posición a a = ceil(avg+0,01).
  Cola: a < ba → cabeza; a = ba → detrás de as_ (prints a == a consumen la cola antes); a > ba → solo prints que
  atraviesan (p > a). Relleno: print BUY del token a ≥ a, o SELL del complementario a ≤ 1−a (merge), o bb del token
  > a (≥ a en cabeza; una vez por nivel). Vive hasta T = 2 s; lo no vendido se mantiene a resolución. Si al colocar
  bb ≥ a: venta tomadora al bid (fee) de min(resto, bs) y el resto a bb+0,01.
- Secundarias: X2 (a = ceil(avg+0,02)); X3 (X1 y a T = 30 s, llegada +250 ms, vender el resto tomador al bid nivel 1);
  XI = INVERSIÓN (a = max(avg−0,01, bb+0,01): descarga rápida con pérdida); X4 (vender tomador al bid a t_fin+250);
  X5 (comprar el complementario tomador al ask a t_fin+250: par bloqueado, descriptor de la palanca 1/pares).
- PLACEBO PL: comprar 5 a be = bb(te−130)+0,01 en te SIN condicionar a relleno; HOLD y X1 (a = ceil(be+0,01), te+150).
- R3 (candidata d, frente 4 «lado no informado como tomador»): en te comprar 5 acc del barato al ask nivel 1 a te+250 ms
  (as_ ≥ 5; si no, no ejecutable y contado), HOLD. Secundarias: D_X1 (salida maker a ceil(ask+0,01));
  INVERSIÓN INV_D = comprar el complementario (favorito) al ask a te+250.
- No elegidas: (a) complementario tras barrido = palanca 1, REFUTADA 24-26 (−0,057, red team SÓLIDO); aquí solo X5 como
  descriptor. Pares con cancelación Binance mantenidos a resolución = SUMA lineal de las dos caras (FRENTE-TD + FAV-TD,
  ambas < 0): no se recalcula.

## Contabilidad y estadística
Maker sin fee ni rebate (rebate 20 % ignorado: pesimista leve); tomador fee 0,07·p(1−p)/acc. pnl = cobros de salida −
fees + acciones no vendidas·gana − coste de entrada. EVw = Σpnl/Σcoste (coste de entrada; X5 suma la cobertura);
EVu = media pnl/coste. Solo unidades con coste > 0.
IS = 05..22-Oct (18 días); OOS = 23..26-Oct (4 días), mirados UNA vez en la misma ejecución de eval.py congelado.
IC90 bootstrap por CIERRE (2000, semilla 2711) y por DÍA. Signo por día; sin los 2 mejores días; regímenes (moneda; T de
te 60-120/120-180/180-240/240-290; hora UTC 0-7/8-15/16-23; vol Binance |ret 60 s| < 3 / 3-10 / ≥ 10 bps).
Multiplicidad: 3 primarias (R1, R2, R3); el resto es exploratorio sin derecho a veredicto.

## Veredictos (por primaria, calculados por eval.py)
- PROMISING: n IS ≥ 400; EVw IS > 0 con IC90 por días inf > 0; ≥ 60 % de días IS > 0; IS sin 2 mejores días > 0;
  EVw OOS > 0 con IC90 por cierre inf > 0. R2 además: Δ(R2−R1) IS con IC90 cierre inf > 0 y Δ real > Δ placebo.
- REJECTED: IC90 por días IS sup < 0, o (EVw IS < 0 y EVw OOS < 0).
- INSUFFICIENT_EVIDENCE en otro caso. Nada de esto autoriza dinero real: PROMISING exige validador + red team + forward.

## Límites declarados
Órdenes virtuales (sin reacción de otros makers ni auto-print); solo nivel 1 del libro; cola de entrada en cabeza
(optimista) y de salida «detrás» conservadora; mínimo de 1 $ no modelado; orden de fichero ≈ orden de llegada
(retrocesos >60 s: se cortan las unidades en curso y se cuentan); Binance y Polymarket en el reloj de recepción del
mismo proceso; YES = Up.
