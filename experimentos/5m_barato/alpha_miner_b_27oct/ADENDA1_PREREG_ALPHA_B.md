# ADENDA 1 al PREREG_ALPHA_B (27-Oct-2026 ~15:20Z) — ANTES de calcular ningún EV/desenlace
Motivo (diagnóstico CIEGO, sim.py no lee desenlaces; eval.py no se ha ejecutado): en el día de prueba 12-Oct la regla de
relleno (C) «ba del token ≤ b'» produce el 94 % de los primeros rellenos de P (2.127 de 2.264; A = 10, B = 127) y un
97 % de unidades rellenas. Es un artefacto: nuestra puja virtual es invisible para los demás; un maker que recotiza su
ask (o la puja del favorito, por espejo) a través de nuestro nivel lo haría post-only y NO casaría con nosotros. Lo mismo
vale para el cruce de la salida (bb ≥ a). FRENTE-TD (validado) usaba solo prints (A+B).
Cambios (versión v2; todo lo demás igual):
1. Entrada PRIMARIA P y L1/L5: relleno SOLO por prints (A: SELL del token a p ≤ b'; B: BUY del complementario a p ≥ 1−b').
2. Nueva secundaria PC = P + regla C (sensibilidad), con HOLD y X1 (PC_X1). Sin derecho a veredicto.
3. Salidas (todas): relleno SOLO por prints (BUY del token a ≥ a / SELL del complementario a ≤ 1−a, con las reglas de
   cola del prereg); se elimina el cruce bb ≥ a. Se mantiene la venta tomadora si al colocar bb ≥ a (acción nuestra).
Veredictos, métricas, muestras IS/OOS y umbrales: sin cambios. El fichero u_2026-10-12 de la prueba se borra y se rehace.
