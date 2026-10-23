# PREREG pares_huecos (cobertura / pata contraria de B + ingenieria inversa de cosechadores alts) -- fijado 22-Oct-2026 ~16:20Z ANTES de calcular
Ya visto antes de fijar (declarado): salida/INFORME (40 reglas de salida al bid, todas <0 en test), an_v2 de b_seleccion_adversa
(scalp/cobertura maker 1-p-m: -0,336..-0,341 sim), cosechar al abrir v1/v2 BTC (REJECTED; completado_tomador == salida al bid en PnL),
pares 15m (completar como tomador estructuralmente imposible), cola_vs_cruce AVANCE (C2 malo, ex post). NO he mirado ninguna trayectoria
de la pata contraria ni ningun ledger de wallet alt antes de fijar esto.

## Parte A -- pata contraria sobre rellenos tipo B
Unidades: (i) B real = datos/unidades_b.csv de salida (166 con t_det; 9 sin t_det = missing); t_ref = t_det (deteccion real de B).
(ii) Poblacion = primer relleno por (mercado,lado) ETH/SOL/XRP 5m a 0,10-0,30, T 65-295 s, por cinta WS (SELL propio a p o BUY opuesto a 1-p),
5 acc, t_ref = recepcion del print + 0,5 s (igual que salida). DESC 17-19 Oct, TEST 20-22 Oct (22 hasta ~14:40Z). Desenlace oficial gamma.
Libro: filas q (top) por RECEPCION del npz salida/datos/ms_D.npz. ask_opp(t) = ask del token contrario con recepcion <= t (si falta o cruzado -> 1-bid propio; si tampoco, missing).
Politicas (todas solo si el envio es <= fin-5 s):
 H0 mantener (base).
 HT0 tomador inmediato: envio t_ref+0,05 s; casa en t_env+0,215 s al ask_opp de ese instante; si asz<acc, +0,01; comision 0,07*a*(1-a)*acc.
 HTc(m) tomador condicional "cerrar el hueco con beneficio": primer q del token contrario en (t_ref, fin-5 s] con p + a + 0,07a(1-a) <= 1-m;
   FOK limite a enviada en ese instante; casa si ask_opp(t+0,215) <= a (al ask de ese instante), si no sigue buscando. m in {0,02;0,05;0,10}.
 HTs(d) tomador "stop": primer instante con p + a + fee >= 1+d; casa al ask_opp(t+0,215) (sin limite). d in {0,03;0,06;0,10}.
 HM(m) maker en el contrario: puja en q = floor100(1-p-m)/100 desde t_ref+0,05 s hasta fin-10 s; se rellena con volumen que ATRAVIESA
   (SELL contrario a precio < q o BUY propio a precio > 1-q), acumulado hasta acc (parcial posible). m in {0,00;0,02;0,04}. Variante OPT
   (al precio o mejor, cota optimista no elegible).
PnL unidad = pago pata1 + pago pata2 - coste1 - coste2 - comisiones. Rebate maker no sumado (0 $ cobrados).
Metricas: EV = Sum pnl / Sum coste1 (y / coste total), Delta vs H0 emparejado, IC90 bootstrap por dia y por cierre, sin 2 mejores dias,
desviacion tipica por unidad, % unidades con perdida >50 % del coste. Efecto AS: desglose por grupo ex post "adverso" (bid propio a +5 s <= p-0,03)
vs resto (descriptivo).
Gate (familia de 10 politicas): elegir la mejor Delta en DESC; en TEST exige Delta>0 con IC90 por dias Y por cierre >0, 3/3 dias, y B real Delta>=0.
Si no -> REJECTED (cobertura no aporta EV). Reducir varianza sin EV se reporta como palanca de capital, no de EV.

## Parte B -- cosechadores/pares en alts 5m (on-chain cola_vs_cruce/datos/oc_D, 17-22 Oct)
Filas con taker=exchange 0xe111... = orden TOMADORA de la wallet "maker"; resto = relleno MAKER de la wallet maker. side 0 = compra
(ma=USDC, ta=acc), side 1 = venta (ma=acc, ta=USDC). Venta de X a s == compra del contrario a 1-s. Unidad = wallet-mercado.
Por unidad: Q_up, Q_down, coste, pares = min, coste par medio, residuo, PnL par / residuo con desenlace oficial, comision pagada.
Seleccion "pareadoras": wallets con >=30 mercados y >=60 % de mercados con ambos lados en 17-19 (sin mirar PnL). Medida 20-22: PnL/vol,
par vs residuo, IC90 por dia. Placebo: wallets con >=30 mercados y <20 % ambos lados. Casos: 0x41e2e1cc, 0x21f4c1a1, 0xaa1a4f31, @mo-money.
Disección descriptiva de la mejor pareadora persistente: T de cada relleno, tamano, precio, maker%, inventario, retraso entre patas,
coste del par, rango en cola (log_index entre makers del mismo nivel en la tx) vs azar.
