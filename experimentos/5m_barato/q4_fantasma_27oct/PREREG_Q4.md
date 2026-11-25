# PREREG Q4 (RE-AS-B, 27-Oct-2026 ~14:55Z, ANTES de calcular nada) - fraccion FANTASMA en rellenos virtuales <1 s
Autor: agente Q4 (solo lectura; sin tocar produccion/crons). Pregunta: del tramo "relleno <1 s tras colocar" (EVw -0,085 en RESULTADO_FRENTE_27oct.md) que parte es fantasma.

## Poblacion (sin cambios respecto a lo ya medido)
FRENTE-TD primaria (PREREG_FRENTE.md sha 1528f06b...), reproducida con la MISMA logica que experimentos/5m_barato/validador_indep_27oct/ana.py (fr_D de re_as_b_frente, TD Binance k=2 bps/300 ms, Lc=100, Lp=85, regla A+B, unidad = primer print por (mercado,lado), EVw = sum(pnl)/sum(coste), IC90 bootstrap por CIERRE 2000 semilla 2711).
Dias: 24, 25, 26-Oct (m5_registro + archivo on-chain VOL/m5_onchain; 26 es el pedido, 24-25 se anaden porque el archivo on-chain los conserva). 27-Oct NO se cubre: no existe m5_registro_27 (se extrae a las 03:45Z del 28) ni fr_27; se declara, no se rellena.
Tramos por dt = tfirst - t0 (tfirst = recepcion del primer print aceptado, >= t0+85 ms): <1 s, 1-5 s, 5-20 s, >=20 s (informativo).

## Definiciones de fantasma (sobre CADA print; la unidad es fantasma si lo es su PRIMER print tfirst)
- Reloj de exchange (FX): t_exch del print (fila t de m5_registro, columna 2) < t0 + 85 ms. (Print cuyo sello de exchange es anterior a la llegada de nuestra orden; recibido despues.)
- Reloj on-chain (FC): el print se casa con un fill on-chain por (token_id, precio a 0,006 y tamano a 1e-4 acc) con ts_chain unico dentro de [t_exch/1000-2 s, recv/1000+15 s] (si hay >1 tx distinta en la ventana -> "ambiguo", excluido de FC y contado). casado_est = ts_chain_ms - OFF, con OFF = mediana del dia de (ts_chain_ms - t_exch) sobre los prints casados "frescos" (recv - t_exch <= 200 ms). FC = casado_est < t0 + 85 ms.
- No atribuible por nivel previo (FD): bb85 >= bp (el nivel bp ya existia al llegar nuestra orden: "disputada"; el relleno no es de nuestra orden en cola 0). Se informa APARTE.
- FANTASMA primaria = FX o FC. Variantes: FX solo, FC solo, FX y FC (conservadora), primaria o FD.
Ruido del reloj on-chain: se informa p25/p50/p75/IQR de (ts_chain_ms - t_exch) en frescos; FC solo es informativa si IQR <= 1500 ms. Control negativo: misma regla en los tramos 1-5 s y 5-20 s (un fantasma verdadero necesita retardo de feed; si el tramo <1 s no supera claramente a los otros, el exceso es ruido de la regla).

## Resultados a reportar
Fraccion fantasma por tramo (unidades y por € de coste), cobertura de cruce on-chain del primer print, ambiguos. EVw (ponderado por € , 1 obs por mercado-lado, IC90 por cierre y por dia) de <1 s: ANTES; DESPUES = quitar unidades fantasma (primaria); y re-simulacion quitando los PRINTS fantasma de cada vida (la unidad se re-asigna al siguiente print). Tambien sin los 2 mejores dias si hay >=3 dias.

## Veredicto (fijado ahora)
- CONFIRMADO: fantasma primaria en <1 s >= 25 % de las unidades Y >= 2x la fraccion del tramo 5-20 s, con cobertura on-chain del primer print >= 90 %.
- NO: fantasma primaria <1 s < 10 % o no mayor que la de 5-20 s.
- NO VALIDABLE: cobertura on-chain < 90 % o IQR del reloj on-chain > 1500 ms y FX no corroborado por FC (en ese caso solo se informa FX como cota).
- Intermedio (10-25 %): "PARCIAL"; no cambia la decision de RESULTADO_FRENTE (refutada con y sin <1 s).
Limites: pujas virtuales; t_exch es sello de lote (puede ser anterior al evento real: FX sobrestima); on-chain da hora de bloque (~2,4 s tras el casado), no hora de casado; no se observa identidad de nuestra orden ni reaccion de otros makers.
