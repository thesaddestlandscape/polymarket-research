# PREREG PREDICTOR-AS-B (28-Oct-2026 ~18:10Z, ANTES de leer desenlaces; la extraccion pred_extract.py es ciega)
Datos: m5_registro 05..26-Oct (22 dias), IS 05-22 (18 d) / OOS 23-26 (4 d, una sola mirada), reloj RECEPCION, libros cruzados descartados.
Poblacion: primeros rellenos de P (alpha_miner_b_27oct/sim.py SIN cambios: puja 5 acc a bb+0,01, cancelacion TD Binance) = 'fills';
instantaneas cada >=4 s de unidades con puja P viva y T>=63 s = 'snaps'. Rasgos: 55 (nivel 1 propio y complementario, prints, Binance
ret 300/1000/3000 ms con signo del lado, v60, T, moneda, lado, hora, nivel de la puja conocido en tau = bb(tau-130)+0,01). bid15: el
registro no trae libros 15m (se comprueba al lanzar) -> NO cubierto. Q0 = 0 por construccion en P (cabeza de cola).
Q1 (lead): HGB fijo (depth 3, lr 0,05, 200 it, l2 1, min_leaf 300) entrenado en IS con offsets 100-1100 ms apilados; AUC OOS (gana) a
L=100,300,600,1000,2000 ms vs linea base M0 (solo T, moneda, lado, hora, nivel). Hay lead si dAUC(M1-M0) a L=100 ms >= +0,03 con IC90
(bootstrap por cierre) > 0. Si no: REJECTED y se para.
Q2 (politica no pujar/cancelar, Lc=100 ms primaria, 250 secundaria): score = p(gana)/nivel - 1; marcar el relleno si el MINIMO del score en
offsets [Lc, Lc+1000] <= theta_q; theta_q = cuantil q del score en IS (cross-fit 3 bloques de dias); q en {0,1;0,2;0,3;0,5}; q primario =
mayor EVw retenido IS con retenidos >= 40 % del coste. CANDIDATE solo si en OOS: EVw retenidos - 0,046 (etiqueta pesimista del validador,
IS -0,015) > 0 con IC90 por cierre > 0, >= percentil 95 del placebo (500 marcados aleatorios a la misma tasa), la inversion (EVw de los
marcados) peor y sin los 2 mejores dias > 0. EXPLORATORY si mejora el HOLD (IC90 de la diferencia > 0) sin cumplir lo anterior. Si no, REJECTED.
Techo oraculo: EVw de los rellenos sin barrido (print estrictamente a traves del nivel). EVw = sum pnl / sum coste (ponderado por EUR).
Q2b (palanca 1 con predictor): en snaps marcados (primera por unidad, top q en {1,3,10 %} del score de barrido adverso M2 entrenado en IS)
comprar 5 acc del complementario al ask a t+250 ms (fee 0,07 p(1-p), cas>=5), mantener a resolucion; EVw y IC90 por cierre vs primera snap
incondicional. Q3 (ambos lados / descargar perdedor): solo se mide si Q1 y Q2 superan el criterio; si no, 'no habilitadas'.
Limites: pujas virtuales sin cola real (optimista), nivel 1 solo, maker sin rebate (pesimista leve), etiqueta pesimista = ajuste aditivo.
