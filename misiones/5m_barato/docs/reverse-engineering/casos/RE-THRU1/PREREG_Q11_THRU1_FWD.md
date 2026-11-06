# PREREG H-Q11-THRU1 forward (congelado 2026-11-06, antes de 2026-11-07 00:00Z). EXPLORATORIA. DEV, 0 ordenes; no autoriza nada live ni micro-real. Revisado por cheap5m-statistical-validator sobre PREREG_Q11_THRU1_FWD_BORRADOR.md (el borrador queda intacto como historia; manda este). No toca PREREG_Q11_{SOL013,PISTAS,GIRO}, sus addenda ni PREREG_Q11_PG_O50_FORWARD.md (sha 40d93fa63f70993b).
Origen (todo sobre dias QUEMADOS): Q11 barrido corregido, red-team PG_O50 (Q11_redteam_PG_O50_05nov.md), RE-THRU1 (DISENO_T.md sha 36e49c0c98c8fbfc, passT.py sha a8b9d7a0158fd0b0). Prior = regresion a la media.
Dias QUEMADOS, excluidos de TODA decision de este prereg: 26-Oct..04-Nov (los 10 de entrenamiento del modelo OWN y del red-team), 05-Nov y 06-Nov (dia de congelacion). Dias que cuentan: D >= 2026-11-07 (UTC).

## Objeto
Escalera G (engine.py escalera_B sin tocar, niveles 0,10/0,13/0,16/0,19, 5 acc, puerta G), ETH/SOL/XRP 5m, poblacion completa con reposicion. EV = SUMA pnl/SUMA coste con rebate 0,2*0,07*p(1-p); no relleno = 0 EUR. Cinta re-sincronizada (passC5d). Insumos: los de forward_calma (tape/bad/x, libro D). Rasgos a t_dec-300 ms, reloj de RECEPCION (Binance c[7]; Chainlink source=chainlink por recepcion).

## Dia que cuenta (un solo conjunto para todos los brazos)
D >= 2026-11-07 con: insumos completos; horas sanas (tx_ws >= 0,95, filtro del generador); Binance de las 3 monedas con cobertura >= 0,95 (fraccion de segundos de horas sanas con >=1 tick recibido; minimo de las 3); rasgo de PC_AS definido en >= 95 % de las unidades (cierre, moneda) NO. Si falla algo: NO VALIDO para todos los brazos. Dia valido en que ni el brazo ni G0 tienen relleno BASE: INSUFFICIENT para ese contraste (no cuenta ni a favor ni en contra; ADDENDUM3_Q11). Dia con relleno en solo uno de los dos: SI cuenta, porque la metrica es una diferencia de PnL de un filtro frente a su propia base (no relleno = 0 EUR), no un cociente de EV entre dos estrategias. nd_validos(brazo) = dias que cuentan para ese contraste. Checkpoints = los primeros 10 y los primeros 20 de esos dias en orden cronologico.

## Brazos primarios (familia de decision = 4 contrastes frente a G0)
1. PG_O50: identico a PREREG_Q11_PG_O50_FORWARD (passC5c VARS ('PG_O50','OWN','0.5','avo')): armar solo si p_OWN < 0,08880918519419896; modelo_own.pkl sha f80d7b573bd74084a8fb6b601af84f0eab7c7d8dd155f1f17d90070d28eb3839, modelo_own.json 35adc359660d8b99f3719d73989d1f9f9dc2ef20a974e159a0ec577cf69ab8dd, entrenar_own.py ea9f59056d0e3283bba5bc498a6242093eb20cbf2cbcb4d6e5acf94f49b30a68. No se reentrena. sha distinto al evaluar => ERROR_DATOS (INSUFFICIENT).
2. GEO6: armar solo si bid(t-300 ms) - L >= 0,06.
3. CXJ150: G0 que (i) no arma si hubo salto adverso de Binance >= 3 bps en 1 s en (t-3300, t-300] y (ii) da por cancelada la orden viva para todo relleno con t >= salto + 150 ms. Salto = definicion de passT.py (bnr(coin, t, 1000), hora = recepcion del tick; adverso = contra el lado de la puja); si texto y passT.py difieren, manda passT.py.
4. PC_AS: G0 sin armar en NO cuando r1 = ln(CL(a)/CL(a-3600)) > 0 y r4 = ln(CL(a-3600)/CL(a-18000)) < 0, a = fin-303 s; rasgo NaN => se arma (como G0) y se cuenta. Mismo mecanismo y fills que P-C (PREREG_Q11_GIRO): NO es evidencia independiente; CANDIDATO de PC_AS + CONFIRMA de P-C = un solo hallazgo.
Secundarios descriptivos (no deciden nada): NJ3A, CXJ1000 (curva CXJ150-CXJ1000), GEO6+CXJ150, GEO6_NJ3A, PG_O50-GEO6, CXB_l (l = 150/300/1000/3000 ms).

## Multiplicidad declarada
- Decision forward: 4 contrastes => PROMOCION a alfa/4 (IC 1,25/98,75 %, p <= 0,025), evaluada en UN solo vistazo (checkpoint 20).
- Ya mirado en quemados: 14 politicas C5 (red-team, max-t p 0,090), 12 variantes RE-THRU1 (CXJ150 elegida post hoc entre ellas, no primaria en DISENO_T, sin placebo), ~60 contrastes de momentum (origen de P-C) y la familia Q11 de 4 (SOL013, P-A, P-B, P-C).
- CXJ150 (seleccion efectiva entre 12): sin placebo calculado o con p > 0,10 queda EXPLORATORY sea cual sea su IC. Placebo: desplazamiento circular de la serie de saltos dentro del dia, tau' = D0 + ((tau - D0 + s) mod 86400 s), s ~ U[60, 86340] s, una s por (semilla, dia) comun a las 3 monedas (misma frecuencia y simultaneidad), 99 semillas (1..99). Estadistico = dPnL BASE (placebo - G0) sumado en los dias que cuentan; m = media placebo; p = (1 + #{|d_perm - m| >= |d_obs - m|}) / 100, exigiendo ademas d_obs > m. Se calcula en los checkpoints 10 y 20 (y una vez sobre quemados, solo informativo); nice 19, ionice 3, ulimit 3 GB, fuera de 06:00-09:15Z, un proceso a la vez.
- PC_AS placebo: permutar dentro de cada dia la etiqueta de condicion (signo de r1) entre unidades (cierre, moneda) NO, 1000 permutaciones, mismo estadistico y misma formula de p (con 1000 en vez de 99).
- GEO6 y PG_O50: sin placebo (puertas deterministas); su riesgo de seleccion es la familia de 14 y lo cubre la cota CROSS.

## Metrica
dPnL = SUMA por cierre (fin, agregando monedas y lados) de pnl(brazo) - pnl(G0). Bootstrap de cierres 4000 (semilla 20261107) e IC por dia (bootstrap de dias 4000, misma semilla). Cotas de relleno BASE, STRICT, OPT, THIN y CROSS cada dia (redteam/rt_sim.py); deciden BASE y CROSS, el resto se reporta. CXJ150 en CROSS: si el ask toca L antes de salto + 150 ms, el relleno cuenta. Se reportan por separado rellenos, cierres, dias, EV por EUR y por unidad, por moneda y por lado.

## CANDIDATO (pasa a dry-run de la escalera con el brazo; nunca a real), solo en checkpoints 10 y 20, todas:
C1 nd_validos >= 10; >= 300 rellenos BASE del brazo en esos dias; >= 40 cierres con dPnL != 0.
C2 dPnL BASE > 0 con IC90 por cierre inf > 0 Y IC90 por dia inf > 0.
C3 dPnL CROSS puntual > 0 (si no: "NO IDENTIFICADO POR EL RELLENO", no es CANDIDATO).
C4 dPnL BASE sin los 2 mejores dias > 0 y sin los 5 mejores cierres > 0.
C5 EV absoluto BASE del brazo > 0 con IC90 por cierre inf > 0; > 0 sin los 2 mejores dias y sin los 5 mejores cierres.
C6 dPnL_d > 0 en >= 60 % de nd_validos (5*k >= 3*n; dPnL_d = 0 no es victoria).
C7 dPnL_YES > 0 por separado, o >= 3 dias que cuentan con PnL G0-NO >= 0 y dPnL_NO > 0 en ellos; si no: "NO SEPARABLE DEL REGIMEN", no es CANDIDATO.
C8 CXJ150 y PC_AS: placebo p <= 0,10 y d_obs > m; placebo no calculado => no CANDIDATO.
C9 PG_O50: PG_O50-GEO6 > 0 con IC90 por cierre inf > 0; en el checkpoint 10 no es CANDIDATO si se encoge (media de dPnL_d de los dias 6-10 < 50 % de la de los dias 1-5). Etiqueta final de PG_O50 = la mas conservadora entre este prereg y PREREG_Q11_PG_O50_FORWARD (avanzar exige PASS alli Y CANDIDATO aqui; REFUTED/REJECTED en cualquiera cierra).
C10 Sin medir P(relleno | ask toca L con nuestra puja armada a >= 6c) fuera del simulador (L2, logger desde 05-Nov, ~16-17 Nov; o micro-real con OK Javi), la etiqueta maxima es "CANDIDATO (EXPLORATORY hasta medicion L2)".

## PROMOCION (alfa/4), solo en el checkpoint 20
Linea exacta por brazo:
PROMOCION (alfa/4): {SI|NO} | brazo={b} | seguimiento={veredicto} | dPnL BASE IC cierre inf 1,25%={x} req >0: {si|no} | dPnL BASE IC dia inf 1,25%={x} req >0: {si|no} | EV abs IC cierre inf 1,25%={x} req >0: {si|no} | placebo p={p} req <=0,025: {si|no|no aplica}
SI solo si CANDIDATO en el checkpoint 20 y todo definido y cumplido (NaN => NO). SI = propuesta de prereg de micro-real, que exige ademas C10 medida, /code-review y OK de Javi; nunca dinero real directo.

## REFUTA / REFUTED / parada
- REFUTA (terminal) en un checkpoint si dPnL BASE <= 0 puntual (definido). PG_O50 no se declara fallido antes del checkpoint 20. NaN, <3 cierres o nd_validos <= 2 => INSUFFICIENT, nunca REFUTA.
- Checkpoint 20 sin CANDIDATO => REFUTED (terminal; "no identificado" o "no separable" se anotan como motivo).
- Tope: si al cierre del 2026-12-31 UTC nd_validos < 20 => CERRADO_INSUFFICIENT (sin promocion; reabrir = prereg nuevo).
- Los informes diarios son descriptivos: ningun veredicto fuera de los checkpoints.
- Cambiar umbral, ventana, simbolo, modelo, cota o definicion de dia = prereg nuevo. Corregir un bug del evaluador se permite y se anota en DECISION_LOG sin cambiar reglas.
- Parada: sha de engine.py, passT.py, rt_sim.py o del modelo OWN distinto del registrado => INSUFFICIENT hasta corregir.
- Aceptacion del evaluador ANTES de mirar ningun dia forward: sobre quemados debe reproducir G0 2.938 rellenos, -166,9 EUR, EV -0,076; thru1 n 2.321, EV -0,125; dPnL GEO6 +140 y CXJ150 +128 (+-1 EUR). Si no, los dias se acumulan sin evaluarse.

## Calendario
Primera revision: 2026-11-17 o el dia del checkpoint 10, lo que sea mas tarde. Final: checkpoint 20 (no antes de 2026-11-26). Tope 2026-12-31. Coste ~1-3 min CPU/dia (placebos aparte, ~4-8 h por checkpoint), nice 19, fuera de 06:00-09:15Z. Evaluador: cheap5m-execution-engineer en dev reutilizando toxicidad_thru1/passT.py y barrido_corr/passC5c.py.
