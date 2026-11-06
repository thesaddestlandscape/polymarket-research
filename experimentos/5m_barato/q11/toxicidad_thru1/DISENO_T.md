# DISENO_T toxicidad thru1 (06-Nov, reverse-engineer). Escrito ANTES de calcular. EXPLORATORIO: los 10 dias 26-Oct..04-Nov estan QUEMADOS (Q11/C5/redteam). Nada de esto es prerregistro forward.
Base: escalera G (engine.py SIN tocar), cinta re-sincronizada = passC5d.py, relleno BASE, poblacion completa con reposicion (segs de passC5), no relleno = 0, EV = sum pnl / sum coste con rebate 0,2.
Rasgos SOLO a t_dec-300 ms (t_dec = punto de rejilla 500 ms en que se arma): bidL = bid(t-300)-L; T; moneda; lado; r3 = retorno Binance spot (reloj recepcion c[7]) en (t-3300, t-300] en bps, firmado a favor del lado (YES +, NO -), frescura <=15 s, NaN si no; dbid3 = bid(t-300)-bid(t-3300).
Tipo de relleno (etiqueta, futuro, solo descriptiva): thru1 = print del evento con pmin<L y 1 precio; nivel = >=2 precios y pmin<L; cola = print en L.
Variantes (todas fijadas aqui):
 G0; GEO6: armar si bidL>=0,06 (post hoc de C5d, control); NJ3: no armar si |r3|>=3 bps; NJ3A: no armar si r3<=-3 (salto adverso); CALM3: armar solo si dbid3==0 y |r3|<3; GEO6NJ3 = GEO6 y NJ3;
 CXB_l (l = 150, 300, 1000, 3000 ms): armar solo si bidL>=+0,01 y cancelar cuando el bid real cae por debajo de L (primera cotizacion con v0<L-TOLP en la vida) + l ms (PROTEGER/latencia);
 CXJ_l (l = 150, 1000): cancelar cuando Binance hace un salto adverso >=3 bps en 1 s (deteccion = recepcion) + l ms;
 placebos: PNJ3A_s (s=1..19): mascara NJ3A desplazada circularmente por un offset aleatorio >=60 s dentro de la rejilla del token (misma fraccion y persistencia); PCXB300_s (s=1..5): cancelacion a hora uniforme dentro de la vida en los segmentos en que CXB300 cancelaria.
Hipotesis primarias (familia 4, alfa/4: IC al 1,25/98,75 % y p placebo bilateral <=0,025):
 H-GEO (GEO6-G0), H-JUMP (NJ3A-G0, placebo PNJ3A), H-CALM (CALM3-G0), H-LAT (CXB300-G0, placebo PCXB300; curva CXB_l descriptiva).
CANDIDATE (para prereg forward, no validacion): dPnL>0 con IC90 por cierre >0 en los 10 d Y en OOS 01-04 Nov (dPnL>0 puntual y >=3/4 dias), sin 2 mejores dias >0, EV absoluto de la variante >0, placebo p bilateral <=0,10 (seguimiento) y alfa/4 para promocion.
REJECTED: dPnL<=0 o IC90 por cierre con limite superior <0. Resto INSUFFICIENT. NaN: comprobar que r3 NaN no predice EV|relleno (diferencia IC90 incluye 0) o la hipotesis queda INSUFFICIENT.
Decision que cambia: si H-LAT CANDIDATE y la curva CXB_l cae con l -> reducir latencia de cancelacion es la palanca (ingenieria); si H-JUMP/H-CALM CANDIDATE -> filtro de colocacion en prereg forward; si nada -> limite de datos L1+Binance declarado, esperar L2 (16-17 Nov).
Descomposicion G0 por segmento: P(relleno), EV|relleno, EUR/segmento por cubos bidL (<0,02, 0,02-0,04, 0,04-0,06, 0,06-0,08, >=0,08), r3 adverso si/no, T (<120, 120-200, >=200 s), moneda, lado.
