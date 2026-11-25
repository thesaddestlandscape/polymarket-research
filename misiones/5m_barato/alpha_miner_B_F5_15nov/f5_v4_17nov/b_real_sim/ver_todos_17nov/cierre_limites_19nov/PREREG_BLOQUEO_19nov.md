# PREREG_BLOQUEO_19nov — regla ex ante de identificacion del resto en reposo del tomador (canal bloqueo de B). Fijado ANTES de medir (19-Nov ~09:30Z). No mide EV. Solo lectura.
Datos: tomador_202.pkl (verdad on-chain: tk_eq, tk_sz, tk_rem; rem_sh=tk_rem*tk_sz acciones) + L2 bids y trades T de cola_vs_cruce/mk (rx = recepcion ms). Mismo universo que u1: 20-22 Oct.
Poblacion: tk_tipo=='compra_comp' con fichero mk. POSITIVOS = tk_rem>0,01 (los 94 de u1). NEGATIVOS = tk_rem<=0,01 (no hay resto: cualquier bloqueo atribuido es falso positivo).
Ancla (reloj de recepcion): rx_pr = rx de la PRIMERA fila T del token complementario, BUY, precio = 1-tk_eq (+-0,005), con rx en [real_tm3-100, real_tm3+1500]. Si no hay, fila T del token propio a tk_eq (+-0,005) en la misma ventana. Si no hay ninguna: caso 'sin_print' = miss en reglas R1-R3 (cuenta en el denominador). real_tm3 solo sirve para localizar el print del relleno (en el simulador el print ES el evento); on-chain nunca es rasgo.
Nivel P = 1-tk_eq del complementario (bids). Delta = s[i]-s[i-1] del nivel (s previo 0 si nivel ausente).
Reglas (ninguna usa rem_sh para elegir el Delta):
- R1: Delta* = PRIMER incremento positivo del nivel P con rx en [rx_pr-30, rx_pr+50] ms. Dispara si existe.
- R2: R1 + primera aparicion (nivel P vacio, s previo == 0, justo antes del incremento).
- R3: como R1 con ventana [rx_pr-30, rx_pr+150] ms.
- R0 (referencia, NO ex ante): u1 (cualquier Delta==rem en [tm3-50,tm3+500]).
Acierto: |Delta*-rem_sh| <= max(0,02*rem_sh, 0,05 acc) (tol de u1). Secundario (informativo): tol max(2 %, 0,5 acc) por redondeo de acciones.
Metricas: recall = aciertos/POSITIVOS; precision = aciertos/disparos (disparos en NEGATIVOS = FP). Wilson 90 %.
Placebos (misma regla, mismo Delta*): nivel P+-1 tick (acierto contra rem_sh y tasa de disparo); ancla desplazada +-10/20/30 s (media y max por desplazamiento).
Criterio de aceptacion (fijo): recall >= 0,15 Y recall >= 3x placebo_tick Y recall >= 5x placebo_t_max Y precision >= 0,50. Regla final = la de mayor precision entre las que pasan (empate: mayor recall). Si ninguna pasa: INSUFFICIENT, se mantiene L1 actual con su limite.
