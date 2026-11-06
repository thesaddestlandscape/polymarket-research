# PREREG H-Q11-PISTAS (P-A y P-B) - congelado 2026-11-05 (UTC ~08:50). EXPLORATORIA, FORWARD. DEV, 0 ordenes, no autoriza nada live.
Origen: validacion independiente Q11 (informes/Q11_validacion_05nov.md), 9 dias GASTADOS (26-Oct..03-Nov, dec2). Pistas elegidas post hoc entre ~16 y ~5 contrastes: prior = regresion a la media. Nada de lo mirado cuenta como evidencia.
Datos del juez: pickles dec2_D.pkl (y dec3s100_D.pkl como control) que genera forward_calma_diario.sh en /root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/out/ (columnas var,dia,act,lado,mkt,fin,k,L,q,tf,T,gana,nmk,edad,lagj,act10,cost,pnl; lagj en MS). Chainlink data/prices/chainlink_D(.csv|.csv.gz), source=='chainlink', reloj de RECEPCION. Dias que cuentan: >= 2026-11-06 00:00Z (GASTADOS 26-Oct..05-Nov). Solo dias con horas sanas ya filtradas por el generador.
Evaluador: experimentos/5m_barato/q11/eval_pistas.py (implementa EXACTAMENTE esto; corregir un bug de codigo se permite y se anota en DECISION_LOG sin cambiar reglas; su sha se registra en el .sha256 solo como referencia).
Metrica comun: EV ponderado por EUR = SUMA(pnl)/SUMA(cost) (pnl ya con rebate maker 0,2*0,07*p(1-p)); tambien por unidad. Unidad estadistica = cierre (fin); bootstrap de cierres (2000) para IC90; ademas bootstrap por dia. Reportar siempre EV sin los 2 mejores dias del subconjunto y n de fills, cierres y dias. Variante primaria = 'T1'; G0 y PLA_T1 se reportan como controles.

## P-A: evitar el lado NO barato en ETH cuando la 1 h previa a la APERTURA del 5m es positiva
Rasgo: rpre1h = ln(CL(a)/CL(a-3600 s)), a = fin - 300 s - 3 s (apertura del 5m menos 3 s, ultimo tick de recepcion <= a, tolerancia 20 s; si falta -> fila excluida y contada). Es la 1 h ENTERA previa a la apertura (no incluye el tramo dentro del 5m).
Conjunto EVITADO H = {var=='T1', act=='ETH', lado=='NO', rpre1h>0}. Conjunto CONSERVADO C = {var=='T1', act=='ETH', lado=='NO', rpre1h<=0}.
CONFIRMA (PROMISING; solo vigilancia, nada live) con >=10 dias forward y n(H)>=40 fills (>=25 cierres) si TODOS:
 1) EV_w(H) < 0 y IC90 por cierre de EV_w(H) con limite superior < 0 (sin esto no hay dano que evitar);
 2) EV_w(C) - EV_w(H) > 0 con IC90 por cierre inferior > 0;
 3) EV_w(H) sigue < 0 tras quitar sus 2 PEORES dias, y EV_w(C) > EV_w(H) sin los 2 MEJORES dias de C;
 4) placebo: permutando el signo de rpre1h dentro de dia (1000 perm.), p<=0,10 para el spread C-H; control negativo: mismo spread en lado YES-ETH no debe ser >= al de NO-ETH (esperado ~0);
 5) EV_w(T1 ETH-NO con la regla aplicada) > EV_w(T1 ETH-NO sin regla) en >=60 % de los dias con datos.
REFUTA con >=10 dias si EV_w(H)>=0 o spread C-H <= 0. Resto INSUFFICIENT; a 20 dias sin cumplir => REFUTED. Sin retoques (activo, lado, ventana de 1 h, signo, T1) tras esta fecha; cualquier cambio = prereg nuevo.
Registro en gastados (no cuenta): T1 NO hi +0,187 vs lo -0,421 (todas las monedas); ETH hi +0,55 vs -0,16 en la version r1h (ventana distinta, incluye tramo interno); rpre1h spread T1 +0,31, IC90 cierre (-0,02,+0,69), hi sin 2 mejores dias -0,011.

## P-B: rellenos con lag <= 3 s al ultimo salto adverso de Binance son toxicos (latencia de cancelacion)
Conjunto TOXICO Z = {var=='T1', lagj<=3000 ms, lagj no NaN}; resto R = {var=='T1', lagj>3000}. Las 3 monedas juntas (primaria); desagregado por moneda solo informativo.
CONFIRMA (PROMISING: indica que hay que medir/bajar la latencia real de cancelacion, NO un filtro) con >=10 dias forward y n(Z)>=40 fills (>=25 cierres) si TODOS:
 1) EV_w(Z) < 0 con IC90 por cierre limite superior < 0;
 2) EV_w(R) - EV_w(Z) > 0 con IC90 por cierre inferior > 0;
 3) EV_w(Z) < 0 sin sus 2 PEORES dias y en >=60 % de los dias con datos de Z;
 4) control PLA_T1 (saltos desplazados): su conjunto Z' tiene EV_w<0 tambien => es propiedad del relleno justo tras salto (mecanismo de cancelacion), se reporta asi; si PLA_T1 NO lo reproduce, el efecto es dependiente de la estrategia y se reporta tal cual;
 5) dec3s100 (-100 ms): EV_w(Z) del mismo signo (<0).
REFUTA con >=10 dias si EV_w(Z)>=0 o EV_w(R)<=EV_w(Z). Resto INSUFFICIENT; 20 dias sin cumplir => REFUTED. Umbral 3000 ms fijo (no se prueban otros).
Registro en gastados (no cuenta): Z n=101 (5 % fills, 77 EUR), EV -0,470, pnl -36,3, IC90 cierre (-66,-4) EUR, 7/9 dias <0; G0 n=513 -0,328; PLA_T1 -0,34. Quitar Z: T1 0,051 -> 0,082.

## Limitaciones declaradas
Coincidencia parcial de fills entre T1/G0/PLA_T1 (no independientes). P-A y P-B se solapan en fills; se reportan marginales, no sumados. Racimos por cierre (monedas simultaneas) => IC por cierre, no por fill. No se mira ningun dato forward para ajustar reglas antes de n>=40 y 10 dias.
