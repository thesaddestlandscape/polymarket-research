# ADENDA 2 — 25-Oct 12:22Z, ANTES de calcular ningún EV (solo vistos descriptivos sin desenlace de 24-Oct, que es OOS)
Descriptivo 24-Oct (sin EV): las órdenes rellenas de W son MÁS viejas (edad mediana ~5 s vs 0,5 s población) y MÁS
profundas (2-4 ticks bajo el mejor bid vs 0) y su nivel lleva más tiempo vivo (70-478 s vs 5-44 s). H1 tal como se
escribió (W más joven) queda refutada en su parte (a) en ese día; se mantiene el test completo.
Política candidata R1 «PUJA PROFUNDA EN REPOSO» (dirección opuesta a H1): rellenos de órdenes con edad > A (A = mediana
de W en DESC) Y profundidad en el alta ≥2 ticks. Éxito si EV población R1 en OOS ≥ +0,05 con IC90 por cierre >0 y brecha
vs complemento >0; y especificidad: brecha W−población dentro de R1 ≤ 50 % de la brecha total. K=7, alfa 0,0071.
Si R1 pasa, se simula ejecutable (cola FIFO pesimista, 5 acc, alta a T−200 s, sin cancelar) antes de proponer nada.
Nota: el rasgo «tT≤3 s» (H2) vale 0,99 en todos: la operación del mercado es casi continua → H2 no discrimina tal cual.
