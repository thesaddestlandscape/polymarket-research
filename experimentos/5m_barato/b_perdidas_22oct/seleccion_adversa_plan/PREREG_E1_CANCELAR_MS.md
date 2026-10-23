# PREREGISTRO E1 -- cancelar la puja de B ANTES del relleno por senal causal en milisegundos (22-Oct-2026 ~15:15Z)
Fijado ANTES de calcular ningun resultado de E1. Solo lectura; no toca B (experimento_maker_h47.py sha c82f5dc5f304b8a6), procesos, crons ni config.

## 0. Lo que ya se sabia al fijar (no visto por mi en estos datos; leido en informes)
- 05/06-Oct (memoria project_maker_cancelacion_binance_05oct): maker en el mejor bid de AMBOS lados, todas las bandas, cancelar 2 s si
  Binance >=1 bps en 1 s: -10,6 -> -4,5 $/mercado, IDENTICO a 100-250 ms ("la toxicidad que queda no es la carrera de ms").
- b_seleccion_adversa: Binance en contra con rasgos >=4 s antes del relleno REJECTED; simv2 (paso 5 s) "cancelar si bid15 baja 5/30 s" REJECTED.
- salida/pre.py: senales en [t_rel-10 s, t_rel-0,3 s] (Binance <=-3/-6 bps, dbid, d15, flujo) negativas en test 20-22. NUNCA se midio la
  ventana [t_rel-2 s, t_rel-0,06 s] ni con contrafactico (re-puja tras el enfriamiento).
- Mecanismo a probar: el tomador informado paga ~145 ms de taker delay + ida; nuestra cancelacion maker tarda ~60 ms ida y vuelta y no
  paga el delay. Si el barrido que nos rellena va precedido por un movimiento visible (Binance propio, flujo tomador contra nuestro lado,
  barrido en otra moneda del mismo cierre) >= D ms antes de casar, cancelar evita el relleno toxico.

## 1. Instrumentos
- I_SIM (gate): simulador nuevo a ms con `salida/datos/ms_D.npz` (top q, operaciones WS t y aggTrade Binance x, TODO por RECEPCION),
  dias 17,18,19 (DESCUBRIMIENTO) y 20,21,22 (TEST; 22 parcial hasta ~14:40Z). Desenlace oficial: maker_ms_desenlaces_cache.json +
  salida/datos/desenlaces_extra.json (por market id); sin desenlace = missing (excluido y contado).
  Puja tipo B por mercado 5m ETH/SOL/XRP: lado = primer token cuyo top bid entra en (0,11;0,30] (pegajoso, como simv2); rejilla de 100 ms
  en T restante 298..65 s; objetivo = top bid - k ticks (k ETH 2, SOL/XRP 1; regla de simv2: si bid multiplo de 0,01 -> bid-k*0,01),
  valido si 0,10<=obj<=0,30, obj<bid y obj<ask; repegado solo si el top lleva >=1,5 s estable (asentado de B), si no se mantiene el
  objetivo vigente; fuera de banda -> sin puja. Relleno CONS: primera operacion WS con recepcion r tal que la puja estaba viva en r-50 ms y
  (token propio, SELL, precio < obj) o (token opuesto, BUY, precio > 1-obj+1e-9). Un relleno de 5 acc a obj cierra el mercado.
  PnL = 5*(gana - obj); coste = 5*obj; sin comision maker; rebate aparte (no en el gate).
- I_B (descriptivo, NO gate): rellenos reales de B (`salida/datos/unidades_b.csv`, 166 con t_det). Print de relleno = primera operacion
  WS (propio SELL <= p_fill+1e-9 o opuesto BUY >= 1-p_fill-1e-9) en [t_det-5 s, t_det]; sin print = missing. Senales antes del print.

## 2. Senales (por recepcion; "contra" = en contra de nuestro lado; evaluadas en cada evento de su fuente)
- S1(X,W): retorno del aggTrade Binance de la MISMA moneda en (t-W, t], firmado a favor de nuestro lado, <= -X bps. X in {2,4}, W in {500, 2000} ms.
- S2(W): acciones tomadoras contra nuestro lado en el mismo mercado (BUY opuesto + SELL propio) en (t-W, t] >= 20 (excluida la operacion que rellena). W in {500, 2000}.
- S3: en (t-2000, t], >=20 acc tomadoras contra el MISMO sentido (Up/Down) en los 5m de las OTRAS dos monedas del mismo cierre.
Familia = 7 reglas.
## 3. Politica con regla
Al disparar en t_s la puja se retira en t_s + D y vuelve en t_s + 2000 + 68 ms (enfriamiento fijo 2 s desde el ULTIMO disparo + alta 68 ms).
Un relleno se evita si su recepcion cae en [t_s + D, t_s + 2068]. Despues la puja vuelve al objetivo vigente y puede rellenarse mas tarde
(contrafactico incluido). D primario = 100 ms (cancelacion ~35 ms efectiva + desfase casado->recepcion ~26 ms + margen);
estres D = 250 ms; techo D = 0 (no ejecutable, solo referencia).
## 4. Metrica y controles
- dPnL = PnL(regla) - PnL(base) en EUR (1 $ = 1 EUR) y por EUR de coste base; descompuesto en evitado (perdedoras quitadas), sacrificado
  (ganadoras quitadas) y sustituido (rellenos nuevos tras el enfriamiento). EV ponderado (sum pnl / sum coste) de base y regla.
- IC90 bootstrap por CIERRE (todos los mercados con el mismo fin = un bloque; 2.000 remuestreos, semilla 20261022) y por DIA.
- INVERSION: misma regla con el signo cambiado (Binance a favor, flujo a favor, otras monedas en el sentido contrario).
- PLACEBO TEMPORAL: la serie fuente desplazada +-60, +-120, +-180, +-240 s (8 desplazamientos); misma distribucion de tiempo fuera.
- Multiplicidad: max-estadistico en DESC sobre las 7 reglas contra los 8 placebos x 7 reglas.
## 5. Seleccion y gate (decidido ahora)
Elegir en DESC (17-19) la regla con mayor dPnL/EUR a D=100. Medirla UNA vez en TEST (20-22). PROMISING (merece variante + forward shadow) si en TEST:
 G1 dPnL > 0 con IC90 por cierre > 0; G2 >= 2/3 dias dPnL > 0; G3 dPnL > dPnL de la inversion Y > maximo de los 8 placebos temporales;
 G4 EV(regla) > EV(base) (no basta con reducir volumen); G5 a D=250 ms dPnL > 0; G6 retiene >= 50 % del coste base.
Si falla cualquiera: REJECTED (esta version). Se reportan las 7 reglas en ambos periodos sin reelegir.
Ademas (descriptivo): distribucion del adelanto senal->relleno; fidelidad del simulador (tasa de relleno, acierto relleno vs no relleno) frente a B real.
