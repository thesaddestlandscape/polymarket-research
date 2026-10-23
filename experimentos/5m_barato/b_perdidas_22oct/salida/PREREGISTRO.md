# Preregistro b_perdidas_22oct (salida / cancelacion de B) -- fijado 2026-10-22 ~14:35Z ANTES de calcular ningun resultado
Conocido de antemano (no visto por mi, leido en informes previos): markout mid de B negativo, H40/H41 REJECTED con cache H35,
R1/Binance-en-contra no replica en poblacion, cancelar si bid15 baja (sim) REJECTED. No he mirado trayectorias post-relleno de B.

Unidad B: posicion (mercado, outcome) de contabilidad_wallet_dedicada/posiciones.csv con tanda_B != '' (175). t_det = min t_deteccion
de los rellenos del ledger (puja_fin.rellenos; reloj local = mismo reloj que la RECEPCION del registro ms). Sin cruce -> missing.
Hold = payout oficial (gamma) - coste. Salida a tau s tras t_det: SELL tomador enviado en t_dec=t_det+tau; precio = bid del token
propio en el ultimo q con recepcion <= t_dec+0,30 s, menos 0,005 (medio tick); si bsz < acciones, bid-0,01; comision 0,07*b*(1-b)
por accion; solo si t_dec <= fin-5 s, bid presente y acciones >= 5. Senales con datos de recepcion <= t_dec.
tau in {5,15,30,60}. Senales "en contra":
 A0 incondicional | A1 bid5(t_dec)-p_relleno <= -th, th in {0,01;0,02;0,04} | A2 Binance (ultimo aggTrade por recepcion) retorno
 firmado a favor de nuestro lado t_det->t_dec <= -X bps, X in {3;6} | A3 bid15 mismo outcome (15m de la misma moneda cuyo intervalo
 contiene t_dec) baja >= th15 t_det->t_dec, th15 in {0,01;0,02} | A4 flujo WS (t_det,t_dec]: (a favor - en contra)/total <= -0,5 con
 >=10 acc (a favor = BUY propio + SELL opuesto; en contra = SELL propio + BUY opuesto) | A5 imbalance top propio bsz/(bsz+asz) <= 0,25.
 => 40 reglas. Inversion: misma senal en sentido favorable. Placebo: disparo barajado dentro de dia (1000 perm). Multiplicidad:
 max-estadistico sobre las 40.
Seleccion/medida: elegir la mejor por EUR ganados en 20+21-Oct, medir en 22-Oct; ademas rotacion leave-one-day-out.
Metrica: ganancia = sum(salida - hold) en reglas disparadas / sum(coste de TODAS las posiciones); € evitados en perdedoras vs
€ sacrificados en ganadoras; IC90 bootstrap por dias y por cierre.
Poblacion (potencia): operaciones WS del CLOB tipo relleno de puja (lado verificado contra los rellenos propios de B) en tokens
ETH/SOL/XRP 5m, precio 0,10-0,30, T restante 65-295 s, primera por (mercado, token); 5 acc al precio; mismo modelo de salida
(t_det = recepcion + 0,5 s de deteccion). Descubrimiento 17-19 Oct, test 20-22 Oct.
Exito (para proponer algo): ganancia >0 en los 3 dias test de poblacion con IC90 por dias >0, max-estadistico p<0,05, y B real
22-Oct >=0. Si no -> REJECTED/EXPLORATORY, sin cortar nada.
Pre-relleno (cancelar/no entrar), secundario: A1-A4 medidos en [t_relleno-10 s, t_relleno-0,3 s]; disparo -> pnl 0 (solo
rellenos; no modela el contrafactico de no rellenadas).
