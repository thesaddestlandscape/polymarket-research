# PREREG H-ESC-V2-SIN19 — escalera v2 (congelado 2026-11-04 ~09:40Z, ANTES de ver ningun dia >= 2026-11-03). DEV, 0 ordenes, no autoriza nada live.
Hipotesis unica (decide): la politica H-CALMA-ESC-T1 (PREREG_CALMA_T1.md sha c28e1749...) SIN el nivel 0,19 tiene EV>0 por EUR robusto.
Politica V2: pujas maker 5 acc a 0,10 / 0,13 / 0,16 (tamano igual por nivel; NO hay evidencia para tamanos distintos) en el lado barato 5m ETH/SOL/XRP, T 61-300 s;
 ARMAR solo con gate A_R1ws (lvl15<=0,03, vol30ws>=26, hora>=4) Y calma de Binance (calma_exec/calma_gate.py, umbral 1 bps, equivalente bit a bit a esc_dec2 'T1');
 DESARMAR (cancelar todos los niveles del token, efectivo +60 ms) al caer el gate o ante movimiento ADVERSO >=1 bps; REARMAR tras >=1000 ms sin movimiento adverso. A3v11 (2 bps) queda subsumido (1 bps lo incluye).
Implementacion del juez: ana_v2.py (filtro L in {0,10;0,13;0,16} de la variante T1 de dec2_D.pkl / dec3s100_D.pkl; los niveles se simulan independientes => filtrar = quitar el nivel). Reloj: cinta re-sincronizada sa_ms (no libro5_tx).
Dias GASTADOS (no cuentan, declarado): 26-Oct..01-Nov (derivacion: se eligio quitar 0,19 mirando estos datos) y 02-Nov (dia 0 de T1, visto en agregado). Forward = dias >= 2026-11-03, horas sanas tx_ws>=0,95.
Reproduccion en gastados (out_ana_v2_repro_gastados.txt): EV +0,149 (1.194 rellenos, 588 tokens), -100 ms +0,093, sin 2 mejores -0,067, IC90 cierre [-0,064;+0,38], PLA +0,012, INV -0,329 [IC sup -0,118].
 => YA EN MUESTRA FALLA sin2 e IC cierre: el prior es que el forward la REFUTE o quede INSUFFICIENT; se prueba porque es el unico cambio estructural (no ex post por relleno).
CONFIRMA (PROMISING -> micro-real solo con OK Javi; SOLVED exige validador independiente) con >=10 dias forward si TODOS: EV>0; EV(-100 ms)>0; EV sin 2 mejores dias>0; IC90 por cierre inf>0;
 EV(V2)>EV(PLA_T1 sin 0,19) agregado y en >=2/3 de los dias; INV (rellenos que la calma elimina) IC90 cierre sup<0; dEUR(V2-G0 sin 0,19) IC90 por dias y por cierre >0.
REFUTA con >=10 dias si EV<=0 o EV sin 2 mejores<=0 o EV<=EV(PLA). Resto INSUFFICIENT; a los 20 dias sin cumplir => REFUTED. Diagnostico (no decide): AS eliminada <=> EV de rellenos no-barrido IC90 dias inf>-0,05 e INV<0.
Unidad = relleno agregado por token y cierre (bootstrap por cierre y por dia); EV ponderado por EUR (Σpnl/Σcoste) con rebate 0,2*0,07*p(1-p). T1_c300 se reporta: si <=0, latencia <=100 ms obligatoria.
