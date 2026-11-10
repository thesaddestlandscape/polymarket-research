# ADDENDUM A1 a PREREG_L2_V2 -- generado por gen_a1.py (determinista; sin marcas de tiempo)
Generado ANTES de cualquier look sobre dias >=10-Nov (ningun dato >=10-Nov leido: eval_log.jsonl solo contiene dias <=2026-11-09). NO cambia ninguna regla de PREREG_L2_V2: solo fija cartera, dias y parametros de TRAIN.
- PREREG_L2_V2.md sha256 573dae3893c47adf2b0fbf95c8c4610a894eb3e9b6a975b229025df8d7b4491d
- l2eval.py sha256 4db49b11fd36441fa9f9d21c9cd3cd84afcc7d6be033b9e7122b2ed2ae8ad3a5
- paso0_lib.py sha256 0f15bcf22abf342efbd05012122e915dee07f46cb267b92b7bb4af294d1c73e6
- paso0_run.py sha256 4f49bf167cae2400f0198a6adb161dbef5ac6bad7fef9347018470023d87bf8d
- test_l2eval.py sha256 9ded9635627c201789d7b452af45fb8e8c41af0b228b68543a1b3d7937fa6f08
- gen_a1.py sha256 19496cfef96c12486ccc0dbba2c7843cb1bbed60da4770d13d4704cc91dabe50
- entrada out/g0_fills.pkl sha256 92761f009e6df823860bf5499c738fe5a2eebf4cfa2eb6f9cc471081f52df073
- entrada out/g0_segs.pkl sha256 d0b84e531cc2b02a66411b17794e6109d4f7bf5e286b3720ff0d09cdfe868a29
- semilla 20261110; permutaciones/bootstrap B=20000; alpha_look=0.003125

## 1. Dias (por codigo, sin PnL)
Regla de dia valido (l2eval.valida_dia): >=12 horas sanas (bad_D.json), b40 del dia extraido sin fichero corrupto (stats.json), sa_ms presente. Dia HOLD = >=2026-11-10.
Quemados <=09-Nov (valido L2 = cumple la regla; 26-Oct..02-Nov no tienen b40 -> solo etapa 0/TRAIN de reglas que no usan L2): 2026-10-26:NO(24h; b40 no extraido); 2026-10-27:NO(24h; b40 no extraido); 2026-10-28:NO(24h; b40 no extraido); 2026-10-29:NO(23h; b40 no extraido); 2026-10-30:NO(15h; b40 no extraido); 2026-10-31:NO(20h; b40 no extraido); 2026-11-01:NO(12h; b40 no extraido); 2026-11-02:NO(6h; horas sanas 6 < 12,b40 no extraido); 2026-11-03:OK(16h); 2026-11-04:NO(10h; horas sanas 10 < 12); 2026-11-05:OK(19h); 2026-11-06:OK(18h); 2026-11-07:OK(18h); 2026-11-08:OK(21h); 2026-11-09:OK(18h)

## 2. EV incondicional G0 (rb 0 / 0,2), 15 dias 26-Oct..09-Nov, desenlace de RT passT, ponderado por EUR
- G0: colocaciones 47368, rellenos 4633, coste 3448.27 EUR; rb0 EV -0.1722 IC90 dias [-0.2778, -0.0643]; rb0,2 EV -0.1604 IC90 dias [-0.2639, -0.0505]; sin 2 mejores dias -0.2322; dias + 0.2; pnl/colocacion -0.01168
- G0^GEO6: rellenos 3219, coste 2407.02; rb0 EV -0.1112 IC90 [-0.2422, 0.016]; rb0,2 EV -0.0994 IC90 [-0.2291, 0.028]; dias + 0.333
- Aceptacion §4 (G0 03-07 Nov con L2 valido): n 1350 (esperado 1350), EV -0.2447 (esperado -0.245), pnl -245.76 EUR -> OK

## 3. Etapa 0 y TRAIN (reglas congeladas, sin tocar)
- E1 Lambda=310 base G0 rb0.0: quita 2007/4633 rellenos (0.368 del coste); Delta 242.772 EUR; placebo estratificado media 225.014 p 0.3233; placebo grupo-token media 426.467 p 1.0; dias + 0.8; inversion (ultimo grupo) Delta 590.628; KILL=True
- E1 Lambda=310 base G0 rb0.2: quita 2007/4633 rellenos (0.368 del coste); Delta 227.344 EUR; placebo estratificado media 209.582 p 0.3232; placebo grupo-token media 409.153 p 1.0; dias + 0.8; inversion (ultimo grupo) Delta 570.173; KILL=True
  Sensibilidad Lambda 150/500/560 (G0 y G0^GEO6): KILL en todas (placebo de grupo aleatorio por token-ventana supera a E1 en todas: p=1,0).
  => E1: KILL en etapa 0. FUERA de la cartera A1.
- X1 (dias 10: 2026-10-26..2026-11-09, d_det 250, M 150-1500): coberturas 427, Delta -40.198 EUR, IC90 por cierre inf -0.4196, dias+ 0.5, placebo p 0.48065 (media -42.222), sin 2 mejores -68.007, monedas+ 1, tamano>=q 0.972, espejo 0.0, inversion (lentas) -178.343; pasa_etapa0=False
  Sensibilidad (d_det 150/500, -2 ticks, M_cut 1000/2000): ninguna de las 12 variantes con Delta>0 y pasa_etapa0=True (todas Delta<0). Limite: sa_ms solo da el nivel 1 del libro del complementario (no recorre niveles); esperada subestimacion de profundidad, no de precio.
  => X1: KILL en etapa 0. FUERA de la cartera A1.
- N1 TRAIN (26-Oct..09-Nov, base G0^GEO6): 11 celdas armadas de 144 (37 con n>=30); coste NO armado 0.849783 (muerte si >=0,85: NO, por 0,000217 de margen).
  rb0.0: in-sample Delta 390.976 (placebo media 246.151, p 0.0: SELECCION in-sample, no evidencia); VALIDACION CRONOLOGICA descriptiva (celdas de 26-Oct..02-Nov evaluadas en 03-09 Nov; 7 celdas): Delta 211.533 vs placebo media 220.878 p 0.66605 dias+ 0.571 cobertura 0.805
  rb0.2: in-sample Delta 366.868 (placebo media 222.028, p 0.0: SELECCION in-sample, no evidencia); VALIDACION CRONOLOGICA descriptiva (celdas de 26-Oct..02-Nov evaluadas en 03-09 Nov; 7 celdas): Delta 200.27 vs placebo media 209.613 p 0.66605 dias+ 0.571 cobertura 0.805
  Lectura: N1 reduce perdidas porque opera menos; fuera de muestra NO supera al placebo (p~0,67). Pasa el criterio literal de muerte del prerreg por margen minimo; entra en A1 con esa fragilidad declarada (el veto >=85 % del gate HOLD sera casi seguro: coste no armado 0,8498).
  Celdas armadas (act, L, bloque UTC 0-3, T_rem 0:<120/1:120-210/2:>=210 s; n, dias, P^): (ETH,0.1,2,2,62,13,0.1667); (ETH,0.13,2,1,39,12,0.1625); (ETH,0.13,2,2,84,13,0.1588); (ETH,0.13,3,1,41,14,0.1786); (ETH,0.16,2,1,42,13,0.2674); (ETH,0.16,3,1,40,15,0.2317); (ETH,0.19,0,2,30,11,0.2419); (ETH,0.19,2,1,40,13,0.2561); (ETH,0.19,3,1,38,15,0.2436); (SOL,0.13,2,2,42,12,0.1512); (SOL,0.19,1,2,31,12,0.2969)
- E2: NO ejecutada en el Paso 0 (requiere logistica L2 sobre b40 DESC 03-07 Nov: lectura de ~2,6 GB comprimidos de b40 por token-ventana; programada para la ronda siguiente, ANTES del primer look). Estado A1: PENDIENTE.
- B1: BLOCKED: requiere generador U2 (colocaciones virtuales L+0,01/+0,02) no construido (§6 f). No se puede hacer TRAIN. N3, H-VIDA: BLOCKED por U2.
- N2 (BTC): DATA_BLOCKED en hoy: passT G0 es ETH/SOL/XRP, sa_ms se extrae con SA_COINS=ETH,SOL,XRP (sin BTC) y no existe RT/SEGT de BTC. k no baja.

## 4. Cartera fija A1 (sin tocar tras el primer look)
Cartera A1 = N1 con las celdas listadas (base G0^GEO6, sin ninguna otra pieza). E1 y X1 (KILL) no entran. E2, B1, N3, N2, H-VIDA: no entran salvo que su etapa 0/TRAIN se ejecute y se anexe en A2 ANTES del primer look. B_VIABLE se evalua sobre esta cartera.

## 5. Potencia (sd diaria; Delta pareado)
- Delta_d E1 L310 (rb0,2): n_dias 15, media 15.16, sd 36.83 EUR/dia, dias necesarios (alpha 0.003125, potencia 0,8) 75, media minima detectable a 10 dias 47.9, a 20 dias 31.7 EUR/dia
- Delta_d N1 in-sample (rb0,2): n_dias 15, media 24.46, sd 39.52 EUR/dia, dias necesarios (alpha 0.003125, potencia 0,8) 33, media minima detectable a 10 dias 51.4, a 20 dias 34.0 EUR/dia
- Delta_d N1 validacion 03-09 (rb0,2): n_dias 7, media 28.61, sd 52.54 EUR/dia, dias necesarios (alpha 0.003125, potencia 0,8) 43, media minima detectable a 10 dias 68.3, a 20 dias 45.2 EUR/dia
- Delta_d X1 base (rb0): n_dias 10, media -4.02, sd 15.43 EUR/dia, dias necesarios (alpha 0.003125, potencia 0,8) inf, media minima detectable a 10 dias 20.1, a 20 dias 13.3 EUR/dia
- PnL_d G0 base (rb0,2): media -36.88, sd 60.52 EUR/dia; G0^GEO6 sd 49.94; coste base medio 229.9 EUR/dia.
- Lectura: sd diaria del Delta pareado 29-40 EUR/dia contra un coste base ~230 EUR/dia (12-17 %); con 10 dias solo se detectan Delta medios >~40 EUR/dia (~17 % del coste base/dia): detectar un efecto de 0,03 EUR/EUR requiere >>20 dias.

## 6. Revisar antes del primer look
1) E2 (ronda aparte); 2) generador U2 y aceptacion (§6f); 3) confirmar que el log de HOLD solo se abre con hold=True y escribe eval_log.jsonl; 4) que el reloj de sa_ms (columna t de maker_ms) es RECEPCION (no verificado en este Paso 0); 5) en X1 t_arm = t_dec (ambiguedad del prerreg: no se define t_arm); 6) pnl de RT trae rb 0,2 y se reproduce con la formula (verificado, 1e-15); 7) cuota diaria: b40/RT/x_/tape/bad de cada dia deben existir (valida_dia).
