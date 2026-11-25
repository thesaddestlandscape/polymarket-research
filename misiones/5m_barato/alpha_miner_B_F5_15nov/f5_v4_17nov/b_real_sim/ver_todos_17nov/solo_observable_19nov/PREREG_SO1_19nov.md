# PREREG SO-1 — ¿Deja la clase 1 (SOLO) una TRAZA pública en un mundo SIN nuestra orden? (reverse-engineer, 19-Nov-2026 ~08:50Z)
Escrito ANTES de calcular nada de SO-1. Solo lectura, 0 órdenes. Datos: `../tomador_202.pkl` (202 rellenos reales B 20-23 Oct; columnas causa, estructura, tk_tipo, en_L, mas_alla, tk_eq, tk_sz, tk_rem, real_q, real_tm3, tok, gana, L) + L2 de bids de AMBOS tokens `datalogs/cola_vs_cruce/mk/<ACT>_<mid>.gz` (filas B snapshot / d delta = nuevo total del nivel; t = recepción ms; ETH/SOL/XRP, 20-Oct..22-Oct 16:15Z; 23-Oct sin datos) + `tokens.json` (token → act, mid, YES/NO).

## Mecanismo (física del CLOB, hecho estructural)
Un tomador que nos casa como ÚNICO maker (clase 1), en un mundo sin nuestra orden hace UNA de tres cosas:
- TT (trade-through): si su límite va más allá de L (tk_eq < L) y le quedaba tamaño, casa con bids del token en [tk_eq, L) → print público < L → el motor passT ya rellena la orden virtual (engine.fill_segment: `q < L − TOLP` ⇒ relleno completo). VISIBLE en noviembre.
- REST: si es límite en reposo (GTC), su orden queda en el libro: BUY del complementario a 1−tk_eq (o SELL de nuestro token a tk_eq). Cruza con nuestra puja virtual en L (L + 1 − tk_eq ≥ 1). VISIBLE en el L2 de noviembre (no lo usa hoy el motor: «relleno por bloqueo»).
- NONE: FAK/FOK o tomador reactivo a NUESTRA cotización → no existe sin nosotros → NO observable.
Con nuestra orden presente (octubre) solo se ve el remanente: en los tx con remanente > 1 % (tk_rem > 0,01) el remanente REST debe aparecer en el L2 del complementario justo después del casado.

## E-SO-1a (REST). Población: clase 1 (causa empieza por «1_»), tk_tipo = compra_comp, tk_rem > 0,01, con fichero mk. Controles: (i) clase 1 con tk_rem ≤ 0,01 (sin remanente: debe dar tasa base); (ii) TP con tk_rem > 0,01 (réplica); (iii) placebo temporal: misma regla en ventanas desplazadas −30, −20, −10, +10, +20, +30 s.
Regla de detección: nivel N_bid a precio P = round(1 − tk_eq, 2) (complementario) sube en ≥ 0,5·rem_sh (rem_sh = tk_rem·tk_sz; en el control (i) umbral = 0,5·real_q) en algún delta con recepción en [real_tm3 − 50, real_tm3 + 500] ms. (real_tm3 = reloj exchange del print; la recepción va ~20-40 ms detrás: ventana holgada.)
Aceptación REST observable: tasa(1a) ≥ 0,50 Y tasa(1a) − máx(placebo) ≥ 0,30 Y control (i) ≤ máx(placebo) + 0,10. Refutación: tasa(1a) − máx(placebo) < 0,15.

## E-SO-1b (TT). Población: clase 1, mas_alla = True, tk_rem ≤ 0,01. Regla: en el último estado L2 de bids de NUESTRO token con recepción ≤ real_tm3 − 20 ms, masa total en precios [tk_eq, L − 0,01] ≥ 0,5·real_q. (Proxy del barrido contrafactual; no ve vendedores reales del complementario.) Se reporta la tasa; no hay criterio de aceptación (descriptivo, define el tamaño de la parte TT).

## Salida
Partición de los 98 clase 1 en TT / REST-observable / REST-inferible (sin remanente, si 1a acepta: se supone GTC con la tasa de 1a) / NONE, con n y EV ponderado por € (Σpnl/Σcoste, desenlace oficial `gana`) por parte. 4 días, sin IC por días posible: EXPLORATORY. Ningún EV de esto es EV de B.
Multiplicidad: 1 regla, 1 ventana, sin rejilla. Cualquier cambio tras ver resultados = variante nueva declarada.
