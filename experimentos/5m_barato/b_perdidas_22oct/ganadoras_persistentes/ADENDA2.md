# ADENDA 2 (25-Oct ~12:35Z) — tras ver a2_salida.txt (S1-R, roles, R1-R5). Todo lo de aquí es POST-HOC ⇒ EXPLORATORY, α=0,0125 Bonferroni sobre 4 nuevas.
Visto: ganadoras z≥2 por DEBAJO del azar (9-42 vs 43-48 esperadas); perdedoras z≤−2 2,5-5× el azar; INV medido −0,196 (0/9 días +). R2 celdas maker Δ +0,035 IC90 (+0,004,+0,062).
- R6 (primaria nueva): filtro «perdedoras persistentes (INV, ventana d−7..d−1) ya compraron el MISMO lado s en (m,s) con bloque ≤ tf−5 s» sobre fills maker banda de la población (excluidas INV y roster) en d. Regla B: cancelar/no pujar si flag. Métrica: EV€(sin flag) − EV€(todo). Desagregado INV-maker / INV-tomador (la parte tomador solapa con contrapunto_informado: solo descriptiva). Además R6o: INV compró el lado OPUESTO (¿bueno para nosotros?).
- R2-control: Δ de celdas elegidas por (a) 50 % del coste de TODOS los makers (popularidad), (b) celdas con EV€ población maker >0 en la ventana (mismo nº que R2), (c) celdas de INV-makers. Si (a) o (b) dan ≥ R2, el roster no aporta información.
- Rol de las INV (perfil) y de B: ¿se parece B a las perdedoras? (descriptivo).
- R2 a α=0,0125: intervalo bootstrap por días 98,75 %.
Criterio replicable igual que PREREG (Δ>0, IC90 días >0, sin 2 mejores >0) + a α ajustado para afirmar.

## ADENDA 2b (25-Oct ~12:50Z, tras ver a3: INV = 75 % coste TOMADOR, R6 nulo, R2 = efecto de celda BTC que reproducen celdas de popularidad/INV)
- R7 (EXPLORATORY, solapa en parte con contrapunto_informado → solo descriptivo + regla de celdas): lado contrario de las tomadoras baratas.
  (a) EV del maker que les VENDE el lado barato (= compra el complementario a 1−pc), por € de capital acc·(1−pc), por clase de tomadora (INV / R / resto), sin rebate y con rebate 0,2·fee.
  (b) regla ejecutable: celdas (moneda×min×5c) con 50 % del coste tomador de INV en la ventana → EV maker-complementario de TODA la población tomadora banda en esas celdas en d vs todas. Mismo criterio de replicable.
