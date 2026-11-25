# INFORME 1b (17-Nov) - detector rapido lo<->hi del suelo rx-ex. Sin ordenes, nada en data/. Todo EXPLORATORY.
Datos: seg_D.npz 37 dias (09-Oct..14-Nov), cuentas por segundo de RX de las filas q (tokens 5min, bid [0,03;0,45]), control Σ == hist_filas en los 37. Verdad (solo validacion): por bin de 10 s fraccion d<30 ms (lo >=0,30; hi <=0,01; tramos >=3 bins). Cota conservadora del retraso (incluye zona ambigua).
Detector: suelo_causal.lo_crudo/estado_lo (segundo t usa solo [t-W,t-1], RX; sin datos suficientes = nolo = no operar). Grid 576 en 17 dias <=25-Oct; hold-out 20 dias. Salida: T4b_sel.txt, T4b_grid_dev.json.
Seleccion W5 C30 rho0,05 nmin10 H1 (en el BORDE del grid: W max, nmin/H min; no se ha explorado fuera).
## Resultados (37 dias; hold-out 20 dias entre parentesis)
- Retraso lo->hi: rapido p50/p90 7/84 s (hold-out 4/8 s), 124/124 detectadas; p5 10 min: solo 23/124 detectadas (19 %; los regimenes hi cortos no los ve), p50 270 s.
- Retraso hi->lo: rapido p50/p90 12/54 s (10,5/44,5), 123/123; p5: la cifra "0 s" es artefacto (nunca salio de lo en episodios cortos).
- Lo-en-hi (estado lo con verdad hi): rapido 208 s de 748.490 (0,03 %), 73 episodios (1,97/dia); p5 10.580 s (1,41 %), 206 (5,57/dia).
- Oportunidad lo perdida (nolo con verdad lo): rapido 9.712 s de 1.900.570 (0,51 %), 3.390 episodios (91,6/dia: oscila, cortos); p5 45.820 s (2,41 %), 335 episodios.
- EUR regla F5 (poblacion ajena censurada, tipo B + tercil bajo p60, 35 dias con poblacion, n 112.414): prints en lo-en-hi p5 n=207, 898 EUR, pnl +109 (EV +0,12); rapido n=7, 90 EUR, pnl -85. Es el 0,16 % del coste: la exposicion por retraso del p5 es PEQUENA y no perdedora en esta poblacion. Lo perdido por fail-closed (nolo, verdad lo): p5 1.580 prints / 11.014 EUR (pnl +5.045); rapido 62 / 317 EUR (pnl +955).
- Compuerta "operar solo en lo": pnl rapido-p5 +71 EUR/dia (IC90 por dias -181..+323; dias+ 14/35; sin 2 mejores -93). Dev -194/dia (IC90 -362..-25, 3/15 dias+); hold-out +270/dia (-153..+693). NO distingue: sin ventaja demostrada en EUR.
## Veredicto
- Detector: COMPLETE y mucho mas rapido y fino que p5 10 min (cobertura de deteccion y exposicion). Su valor en EUR: INSUFFICIENT/EXPLORATORY (efecto en EUR no distinguible de 0).
- E1 con sellos v4: tm3 y rama de own_D v4 identicos a v3 en los 215 rellenos; E1_B_real_v4.txt identico a exp1/E1_B_real_v3.txt (diff 0). Ninguna celda ni conclusion cambia (EV pond. -0,0724).
## No verificado / dudas
- Verdad y detector comparten la misma magnitud (fraccion d<30 ms): la verdad no es independiente; el p5 mide otra cosa (cuantil). No es un oraculo de la clase operativa.
- Poblacion F5 = prints ajenos (censurada), no capacidad de B ni EV de regla; regla F5 tomada como tercil bajo p60 tipo B (definicion de t2_agrega_v4); hi EV ~0.
- Optimo en el borde del grid; seleccion con 17 dias; 91 episodios nolo/dia (trafico bajo en horas valle) implican que un operador real veria parpadeo: no probado con el ejecutor.
- Poblacion F5 disponible en 35 de 37 dias (2 sin ningun pickle; no identificados aqui).
