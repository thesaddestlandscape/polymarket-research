# PREREG R8-EMPAREJADO — 26-Oct-2026 ~07:55Z. Escrito ANTES de calcular nada sobre datos reales (solo test sintetico del estimador). Solo lectura, sin dinero real.
Hipotesis (R8): tras el primer BUY visible de una tomadora PERDEDORA persistente en un (mercado, lado s) barato (p<=0,35), VENDER s como maker (= pujar el lado contrario) a los tomadores no-roster que compran s en [t0+5, t0+60] s gana mas que en situaciones comparables SIN el evento. Previo (b_sin_flujo_minorista, PREREG_R8 cdb6bc83): EV absoluto +0,0017 IC90 cierre (-0,009,+0,012); vs control sin evento +0,039 pero control NO emparejado por banda.

## Datos y definiciones (identicas al R8 previo salvo lo marcado NUEVO)
- Fills on-chain de tomadores: /mnt/HC_Volume_106538179/agentes_datos/f6/T_2026-10-{05..23}.parquet + b_sin_flujo/T_2026-10-24.parquet. 6 monedas (columna act), 5m. Reloj = ts de BLOQUE on-chain (el UNICO disponible con identidad de wallet; ~1,69 s tras el casado segun b_sin_flujo/offset.txt). Es el reloj de recepcion: el evento solo es observable por nosotros en t0 (bloque) y nuestra puja no puede casar antes de t0+latencia; ver sensibilidades de inicio de ventana.
- Desenlace OFICIAL: cache maker_ms_desenlaces_cache.json + mapa_escala/des.json + b_vs_poblacion/datos/des_gamma.json (como R8 previo). Fills sin desenlace = missing (NO 0); se reporta cobertura por dia en tratados y controles por separado (supervivencia).
- Roster(D) = wallets con, en D-7..D-1, n>=30 ordenes, coste>=200 $ y z<=-2, z = sum(pnl)/sqrt(sum acc^2 p(1-p)); pnl a su precio, neto de fee. Dias evaluados D=12..24 Oct (13).
- Universo de fills (NUEVO, aplica a tratados y controles): BUY tomador, p<=0,35, desenlace conocido, elapsed = ts-(cierre-300) en [0,300). Evento = primer BUY de una wallet del roster en (mkt,lado) dentro del universo; t0 = su ts. Fills de wallets del roster se excluyen de la venta (y del control).
- Posicion vendedora: vender s a p_k, acc_k: pnl = acc_k*(p_k - win_s); capital = acc_k*(1-p_k); sin fee; rebate NO sumado (variante informativa +0,2*fee_tomador). Cota optimista (primero en la cola, sin AS de cola, todas las filas del nivel).
- Unidad estadistica = CIERRE (ventana 5m; agrupa monedas, mercados y lados), tambien dia. EV = sum(pnl)/sum(capital) ponderado por EUR.

## Control EMPAREJADO (NUEVO)
- Celda = (dia, moneda, lado, minuto-de-ciclo del PROPIO fill = floor(elapsed/60) in 0..4, banda de precio del fill 0,05 = floor(p/0,05) in 0..6).
- Controles = fills del universo (no-roster) en (mkt,lado) SIN evento en el dia. Celda elegible si tiene >=5 (mkt,lado) de control distintos y capital de control>0.
- mu_c = sum pnl_ctrl / sum cap_ctrl en la celda c. Exceso (ESTADISTICO PRIMARIO) = sum_{c elegibles}(pnl_trat_c - cap_trat_c*mu_c) / sum_{c elegibles} cap_trat_c, con tratados = fills en [t0+5,t0+60] de eventos. Cobertura = capital tratado en celdas elegibles / capital tratado total (si <70 %: DATA_BLOCKED parcial, se reporta).
- Inferencia: bootstrap por CIERRE (B=2000, semilla 20261026), recalculando mu_c en cada remuestra (tratados y controles de un cierre entran o salen juntos); IC90 percentiles 5-95. Bootstrap por DIA (13 dias) como segundo IC. Exceso sin 2 mejores dias, mitades cronologicas (12-17 / 18-24).
- Placebo A: roster sustituido por wallets elegibles (n>=30, coste>=200 en D-7..D-1) con z>-2, emparejadas una a una por log2 del nº de BUY baratos (p<=0,35) del dia D; placebo B: cualquier wallet no-roster con >=1 BUY barato ese dia, mismo emparejamiento. 500 sorteos cada uno, mismas definiciones (eventos, controles recomputados). p = (1+#{placebo>=real})/(501). Inversion (informativa): roster = ganadoras z>=+2 con la misma elegibilidad.
- Falsacion de mercado: ventana PRE [t0-60,t0-5] (fills previos al evento) con el mismo control; ventana POST [t0+65,t0+120].
- Sensibilidad de reloj: inicio de ventana t0+5 (primario), +10, +15, +20 (fin siempre t0+60).
- Variante de control estricto: controles solo en MERCADOS sin ningun BUY del roster (ningun lado, ningun precio).
- Variante tamano realista: solo las primeras 5 acciones por ventana de evento.
- Subgrupos (post-hoc, etiquetados, BH-FDR q sobre p bootstrap bilateral por cierre): moneda (5), banda de fill (7), minuto del ciclo (5), mitad (2) = 19 tests. Los subgrupos NO modifican el veredicto.

## Gate y veredicto (fijado ahora; no se cambia tras ver resultados)
G0 eventos>=40, dias>=10, cobertura de capital emparejado>=70 %.
G1 exceso>0 con IC90 cierre inferior>0 e IC90 dia inferior>0.
G2 exceso sin 2 mejores dias>0 y ambas mitades>0.
G3 placebo A p<0,05 y placebo B p<0,05.
G4 exceso PRE < 0,5*exceso primario (efecto especifico post-evento, no tipo de mercado).
G5 exceso con inicio +10 y +15 > 0 (punto).
G6 control estricto: exceso>0 (punto).
G7 (dinero) EV ABSOLUTO de la posicion con IC90 cierre inferior>0 y IC90 dia inferior>0 (el exceso no es dinero: la alternativa es no operar).
Veredicto: PROMISING = G0..G7 todos. DATA_BLOCKED = G0 falla. EXPLORATORY = G0 ok y (G1..G6 todos pero G7 falla [senal de informacion sin dinero]) o (exceso punto>0 con alguna G1-G6 fallando y IC90 cierre superior del exceso >=0,02). REJECTED = G0 ok y IC90 cierre superior del exceso <0,02, o exceso punto<=0. Nada de esto autoriza dinero real.
