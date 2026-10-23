# PREREG L1 - etiquetado pasivo rpre/r900 en B (23-Oct-2026). Congelado ANTES de calcular ningun EV con las etiquetas.
Origen: W1 (`../tendencia_wallets/INFORME.md`, sha PREREG W1 303c2090...). Solo lectura de B; no se toca ningun ejecutor.

## Definiciones (identicas a `tendencia_wallets/scripts/feats.py`, salvo la fuente Binance)
- sgn = +1 si el lado comprado es YES/Up, -1 si NO/Down. Binance = mid del bookTicker (`binance_bookticker_D.csv`, hora de RECEPCION), ultimo tick con recepcion <= instante pedido. NOTA: W1 uso aggTrade del registro ms; la fuente cambia por no existir ese registro en vivo para B (el registro ms rota a ~5 d). Contraste obligatorio en el INFORME (misma posicion, ambas fuentes, 20-22 Oct).
- open = fin - 300 s (fin = epoch del slug + 300). rpre = (P(open)/P(open-900 s) - 1) * 1e4 * sgn [bps]. r900 = (P(t0)/P(t0-900 s) - 1) * 1e4 * sgn.
- t0: orden = t_dec del `puja_post`; posicion = t_det del primer relleno - 4 s (como W1), o primer_fill_chain - 5 s si falta t_det (marcado).
- clase a_favor: rpre*sgn > 0 ; en_contra: < 0 ; retorno exactamente 0 = neutra (mid sin cambio en la ventana; excluida de ambos grupos); NaN/dato Binance con edad > 300 s = missing (ni neutra ni en_contra). Enmienda hecha antes de calcular ningun EV (el primer borrador agrupaba 0 con missing).
- h_w1 = 1 si clase a_favor Y |rpre| >= 7.7 bps (mediana de |rpre| de la poblacion en W1). El umbral NO se reajusta.

## Hipotesis a refutar (H-L1)
«B no deberia pujar el lado A FAVOR de la tendencia de los 15 min previos a la ventana cuando |rpre| >= 7.7 bps»: se predice EV_ponderado(h_w1=1) < EV_ponderado(h_w1=0 con rpre no missing) en posiciones de B.

## Gate (todo debe cumplirse para ELEGIBILIDAD de una variante B; ni siquiera entonces se cambia B sin /code-review + OK Javi)
Unidad = posicion (mercado, outcome) de B con desenlace oficial y rpre no missing. Solo cuentan dias FORWARD, es decir con fecha >= 23-Oct (los dias 20-22 ya fueron vistos en W1: el backfill es descriptivo y NO suma al reloj). Un dia cuenta si tiene >= 1 posicion resuelta.
1. >= 10 dias forward con posiciones y >= 40 posiciones en h_w1=1 (n por clase siempre reportado; con n<40 por clase = solo descriptivo).
2. Delta = EV(h_w1=1) - EV(h_w1=0), EV = sum(pnl)/sum(coste) (ponderado por EUR), <0 y IC90 de Delta por CIERRE (bootstrap del `fin`) con extremo superior < 0.
3. PnL total: quitar h_w1=1 no baja el PnL total: PnL(h_w1=0) > PnL(todas) (es decir PnL(h_w1=1) < 0), y mejor que el placebo (quitar al azar la misma fraccion de coste dentro de dia x moneda x lado x cubo de precio 0,05, 2.000 permutaciones, p<0,05 una cola).
4. EV sin los 2 mejores dias reportado; mismo signo. Signo de Delta igual en >= 60 % de los dias forward con ambas clases.
5. Refutada si, con >= 10 dias, Delta >= 0 o el IC90 por cierre incluye 0, o el skip no supera al placebo, o PnL(h_w1=1) >= 0.
Sensibilidad (no decide): r900 con la misma regla; umbrales 5/10 bps; clase a_favor sin umbral.
Dependencia: si B sigue parado no hay dias forward; el reloj corre solo con B operando (reportarlo en cada lectura).
Fecha: 23-Oct-2026, antes de calcular cualquier EV con las etiquetas L1.
