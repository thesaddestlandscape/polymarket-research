# L2 carrera cancelacion-vs-tomador, maker B (sueltos G0 de passT) - DISENO fijado el 10-Nov ~17:25Z ANTES de calcular ningun PnL de una politica
Exploratorio, DEV, 0 ordenes, solo lectura. Dias 05..09-Nov (y 03/04 parciales) quedan QUEMADOS para otros estudios tras este.
Universo: rellenos G0 de passT.py (sha a8b9d7a0..., copia sin cambios en passT_copia/, RT_/SEGT_ del repo para 03,04,07,08,09; 05 y 06 corridos aqui) ETH/SOL/XRP; token via ms_<D>.npz.
Fuente L2: libro5_b40_<D>.csv.gz (d=diff bids<=0,40, B=snapshot, G=huecos), orden por RECEPCION (rx, seq). Reloj del relleno: tf de passT (rx de la cotizacion que ya refleja el consumo).
TRAIN (cronologico): 03-Nov desde 11:00Z, 04-Nov 00:00-02:41Z y 10:46-24:00Z, 05, 06, 07. HOLD: 08, 09-Nov. Politica y L se eligen SOLO en TRAIN.
Validez: se excluye un relleno si hay G (caida/traspaso/arranque) del token entre t_dec-3 s y tf+1 s, o el libro del token esta 'sucio' (sin B posterior a un hueco) o sin niveles visibles; se cuenta el excluido.
Politica = CANCELAR-SOLO (sin reposicion; cota prudente: no recupera rellenos buenos posteriores). Disparador evaluado por RECEPCION en eventos L2 con rx > t_dec (info disponible), orden viva desde t_dec+68.
 Familia D (distancia): mejor bid visible <= L+delta, delta en {-0,01; 0; 0,01; 0,02; 0,03; 0,05}.
 Familia V (caida rapida): el mejor bid cae >= d en <=500 ms y queda <= L+0,10; d en {0,02; 0,03; 0,05}.
 Familia S (profundidad): suma de tamanos de bids visibles en (L, L+0,05] <= theta; theta en {0; 50; 200} acciones.
 (12 configs incl. nulas excluidas: 6+3+3 = 12.) Si el disparador ya se cumple con info <= t_dec: caso ESTATICO (no se arma; sin carrera), se informa aparte.
Carrera: relleno EVITADO si tf - t_trig > LAMBDA ms (cancelacion llega al motor ~30 ms tras el envio; el relleno se sella ~15 ms tras el casado). LAMBDA base 30, conservador 60 (RTT completo), optimista 15; sensibilidad {0,15,30,60,100,150}. Titular de eficacia: LAMBDA=60 (prudente) y 30 (base).
 El FOK tomador paga ~213 ms (68+145): solo condiciona que la orden tomadora ya estaba en vuelo; se mide empiricamente como M = tf - t_trig, no se supone.
PnL: RT.pnl por relleno (fee+rebate del motor). Delta politica = -sum(pnl de evitados) [>0 = mejora]; TOTAL en EUR y ponderado por EUR (sum pnl / sum cost) del conjunto resultante; emparejado: evitados (toxicos y buenos) vs perdidos (buenos evitados), mismos eventos.
Seleccion (solo TRAIN, LAMBDA=30): elegible = DeltaPnL>0, positivo en >=70 % de los dias TRAIN con relleno, y p<0,05/12 contra PLACEBO (evitar el mismo numero de rellenos al azar dentro de cada dia, 5000 permutaciones, estadistico = Delta). Elegida = mayor DeltaPnL entre elegibles. Si ninguna elegible: NO_EDGE y NO se evalua HOLD.
HOLD: se evalua UNA vez la elegida (y su sensibilidad en LAMBDA); IC90 por cierre de mercado (bootstrap de clusters 'fin') y por dia (solo 2 dias: se dan los dos valores, sin IC por dia).
Validacion base: G0 sin cancelar reproduce el AS conocido (sueltos R0==0, 12 dias quemados: n=2290, acierto 0,1410, precio medio 0,1523); y concordancia de reloj L2 vs tf.
Limites declarados: identidad del tomador on-chain NO usada (08-10-Nov solo; la carrera se mide por tiempos de libro); sin reposicion; relleno 'evitado' no cuenta cola/efectos sobre otros rellenos.
