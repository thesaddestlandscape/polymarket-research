# ADDENDUM3 Q11 - dias sin comparador, contadores minimos, tabla de decision y linea PROMOCION (2026-11-06, vigente desde 2026-11-06 00:00Z; a las 09:24Z del 06-Nov no existia ningun dec2/dec3s100 de un dia que cuente: ningun dia forward evaluado antes).
Origen: criterios 1-2 y tabla decididos por Javi (mandato transmitido por la sesion principal el 06-Nov); resto = resolucion fail-closed de ambiguedades por cheap5m-statistical-validator por encargo de la sesion principal (Javi puede vetarla antes de la primera evaluacion forward, prevista 07-Nov ~12:00Z sobre el dia 06-Nov). NO cambia reglas, umbrales de EV/IC/p, activos, niveles, ventanas ni conjuntos. PREREG_Q11_{SOL013,PISTAS,GIRO}.md, ADDENDUM_Q11_SOL013.md, ADDENDUM_Q11_PISTAS_GIRO.md y ADDENDUM2_Q11_DECISIONES_JAVI.md intactos (sha 38ebc6f8, 5001c9e6, bc9b3d79, 996dfff2, 66a939fc, e96289b1); donde este texto los concreta o sustituye, manda ADDENDUM3.

## 0. Definiciones (SOL013, P-A, P-B, P-C)
- Dia valido: D >= 2026-11-06 con dec2_D.pkl y dec3s100_D.pkl. Toda fila debe tener dia == D del fichero que la contiene; si no, la ejecucion entera es INSUFFICIENT (ERROR_DATOS) y no cuenta ningun dia nuevo.
- Relleno de un conjunto X en el dia d: >=1 fila de X con cost>0. EV_d(X) = SUMA pnl/SUMA cost de X en d, definido solo si hay relleno (coste 0 = sin relleno).
- Comparacion A vs B (A juzgado, B comparador). Dia comparable: dia valido con relleno de A Y de B. D_AB = dias comparables; nd_validos(A,B) = |D_AB|.
- Dia INSUFFICIENT para A vs B: dia valido no comparable. No cuenta ni a favor ni en contra: fuera del numerador y del denominador de todo criterio diario de esa comparacion y fuera de los contadores de 10 y 20 dias de REFUTA/REFUTED.
- Victoria de A en d de D_AB: EV_d(A) > EV_d(B) estricto. Empate o menor = no victoria (si cuenta en el denominador).
- ">= 60 %": con k victorias, 5*k >= 3*nd_validos en enteros, y nd_validos >= 10.
- Metrica no definida (NaN): IC por bootstrap con <3 cierres (lo que ya hace filtro_sol013; sustituye al "<2" de ADDENDUM_Q11_PISTAS_GIRO 1), coste 0, "sin 2 mejores/peores dias" con <=2 dias, comparador vacio. En CONFIRMA una condicion NaN = NO cumplida; en REFUTA una condicion NaN impide REFUTA (=> INSUFFICIENT).

## 1. Contadores minimos (mandato 1; reconcilia ADDENDUM_Q11_SOL013 2)
- Comparacion principal (fija nd_validos de REFUTA/REFUTED): SOL013 T1 vs PLA_T1; P-A H vs C (ETH-NO); P-B Z vs R; P-C H vs C.
- REFUTA solo con nd_validos >= 10 y metricas de REFUTA calculadas SOLO con las filas de los dias de D_AB, definidas y cumpliendo la regla del prereg (P-A/P-C ademas n(H)>=40 fills en D_AB; P-B n(Z)>=40). Con nd_validos <= 9 nunca REFUTA.
- REFUTED solo con nd_validos >= 20 sin CONFIRMA_FINAL. El contador de 20 es nd_validos, no dias de calendario ni dias validos.
- ADDENDUM_Q11_SOL013 2 queda como caso particular: PLA_T1 NaN o con <=2 dias con relleno => nd_validos <= 2 => INSUFFICIENT.
- ADDENDUM_Q11_SOL013 1 y ADDENDUM2 2 (denominador = todos los dias validos) quedan sustituidos: denominador = nd_validos de la comparacion, minimo 10. El dia sin relleno sigue sin contar a favor y ahora tampoco en contra. (ADDENDUM2 1c no se toca: el 60 % no se endurece con Bonferroni.)
- Tope de calendario: si al cierre del 2026-12-31 UTC nd_validos < 20 y no hay CONFIRMA_FINAL => CERRADO_INSUFFICIENT (sin promocion, sin REFUTED; reabrir = prereg nuevo).

## 2. Dia con relleno de un solo brazo (mandato 2)
T1 con relleno y PLA_T1 sin relleno: NO es victoria de T1 (sin comparador no hay comparacion) => dia INSUFFICIENT para T1 vs PLA_T1. Inverso (PLA_T1 si, T1 no): INSUFFICIENT, no derrota. Igual para T1 vs G0 (su propio D_T1G0), H vs C, Z vs R. filtro_sol013.frac (`d not in dB.index` => victoria) contradice esto y se corrige (sec. 7).

## 3. CONFIRMA (seguimiento) en dos muestras
SOL013 CONFIRMA (provisional) si a la vez:
 a) condiciones del prereg sobre TODOS los dias validos: EV>0, EV(-100 ms)>0, sin 2 mejores dias>0, IC90 cierre inf>0, EV(T1)>EV(PLA_T1) y EV(T1)>EV(G0) agregados, n>=40 rellenos T1;
 b) las mismas (salvo EV(-100 ms)) recalculadas SOLO con los dias de D_T1PLA, con n>=40 rellenos T1 en esos dias;
 c) nd_validos(T1,PLA_T1) >= 10 y nd_validos(T1,G0) >= 10, con >= 60 % de victorias en cada una.
P-A/P-B/P-C: sus condiciones sobre todos los dias validos Y sobre D_AB (n(H o Z)>=40 fills y >=25 cierres en ambas). Criterios diarios: P-A 5 dia comparable = relleno de C (con regla) y de H+C (sin regla); P-B 3 y P-C 3 ("dias con datos de Z/H"): denominador = dias validos con relleno de Z/H, minimo 10. Exigir (a) y (b) impide que excluir dias sin comparador fabrique un CONFIRMA.

## 4. Caracter terminal y vistazos
- El veredicto se calcula a diario, pero solo es TERMINAL asi:
  CONFIRMA_FINAL: CONFIRMA en 3 evaluaciones consecutivas en que nd_validos aumento (evaluaciones sin dia comparable nuevo no rompen ni alargan la racha), alcanzado con nd_validos <= 20.
  REFUTA: terminal la primera vez que se cumple (nd_validos >= 10). No se endurece con Bonferroni (ADDENDUM2 1d).
  REFUTED: nd_validos >= 20 sin CONFIRMA_FINAL (una racha en curso no lo evita).
- El estado (racha, terminal emitido, fecha) se persiste; un terminal no se recalcula.

## 5. Tabla de decision (SOL013; P-A/P-B/P-C igual con su par A/B)
Por dia, comparacion T1 vs PLA_T1:
| caso | T1 | PLA_T1 | estado del dia | entra en "todos los dias validos" (3a) | cuenta en nd_validos |
|---|---|---|---|---|---|
| falta dec2 o dec3s100 | - | - | NO VALIDO | no | no |
| filas con dia != D | - | - | ERROR_DATOS: ejecucion INSUFFICIENT | no | no |
| valido | relleno | relleno | comparable: victoria si EV_d(T1)>EV_d(PLA_T1); empate o menor = no victoria | si | si |
| valido | relleno | sin relleno | INSUFFICIENT (no es victoria) | si (sus filas suman a 3a) | no |
| valido | sin relleno | relleno | INSUFFICIENT (no es derrota) | si (suma a EV(PLA_T1) agregado) | no |
| valido | sin relleno | sin relleno | INSUFFICIENT | si (sin filas) | no |
| valido | coste 0 o EV_d NaN | cualquiera | ese brazo = sin relleno; aplicar la fila que toque | segun fila | segun fila |
T1 vs G0: misma tabla con D_T1G0 (solo alimenta 3c).
Veredicto (primera fila que se cumpla):
| # | condicion | veredicto |
|---|---|---|
| 0 | ERROR_DATOS o 0 dias validos | INSUFFICIENT |
| 1 | ya emitido CONFIRMA_FINAL, REFUTA o REFUTED | se mantiene (terminal) |
| 2 | sec. 3 cumplida | CONFIRMA (provisional k/3; k=3 => CONFIRMA_FINAL) |
| 3 | nd_validos <= 2, o PLA_T1 NaN, o alguna metrica de REFUTA sobre D_T1PLA NaN | INSUFFICIENT (no avanza contadores) |
| 4 | nd_validos >= 10 y, sobre D_T1PLA, EV(T1)<=0 o sin2(T1)<=0 o EV(T1)<=EV(PLA_T1) | REFUTA (terminal) |
| 5 | nd_validos >= 20 | REFUTED (terminal) |
| 6 | despues del 2026-12-31 y nd_validos < 20 | CERRADO_INSUFFICIENT (terminal) |
| 7 | resto | INSUFFICIENT |
P-A/P-C fila 4: sobre D_HC, EV_w(H)>=0 o EV_w(C)-EV_w(H)<=0, con n(H)>=40; P-B: sobre D_ZR, EV_w(Z)>=0 o EV_w(R)<=EV_w(Z), con n(Z)>=40.

## 6. Linea PROMOCION (alfa/4) (ADDENDUM2 1d), texto exacto
IC de promocion = cuantiles 1,25 % y 98,75 % del bootstrap de cierres con 4000 remuestreos (SOL013: el MISMO vector que da el IC90, semilla 13; P-A/P-B/P-C: corrida aparte de 4000 con semilla fija anotada; su IC90 de seguimiento sigue con 2000). Cada IC se exige en las dos muestras de la sec. 3. p de placebo = (1 + #{|s_perm| >= |s_obs|}) / (1 + 1000) (sustituye la fraccion simple de ADDENDUM2 3).
SOL013:
PROMOCION (alfa/4): {SI|NO} | seguimiento={veredicto} | IC cierre T1 [1,25%;98,75%] B=4000 todos los dias=({lo},{hi}) req inf>0: {si|no} | dias comparables T1-PLA_T1=({lo},{hi}) req inf>0: {si|no} | placebo: no aplica
P-A y P-C:
PROMOCION (alfa/4): {SI|NO} | seguimiento={veredicto} | c1 EV_w(H) IC cierre sup 98,75% todos/comparables=({x},{y}) req <0: {si|no} | c2 C-H IC cierre inf 1,25% todos/comparables=({x},{y}) req >0: {si|no} | placebo p_bil={p} (1000 perm) req <=0,025: {si|no}
P-B: como P-A con Z y R-Z, terminando en "| placebo: no aplica".
SI solo si seguimiento == CONFIRMA_FINAL y todos los requisitos de la linea estan definidos y se cumplen; cualquier NaN => NO. Formato numerico {:+.3f}; NaN se imprime "nan".

## 7. Implementacion (solo codigo de evaluacion, en dev, cheap5m-execution-engineer + /code-review)
filtro_sol013.py, eval_pistas.py, eval_giro.py: (i) criterios diarios sobre D_AB con victoria estricta, minimo 10 y test entero; (ii) nd_validos de la comparacion principal en REFUTA/REFUTED; (iii) CONFIRMA en dos muestras; (iv) estado terminal persistido (escritura atomica); (v) linea PROMOCION; (vi) assert dia == D; (vii) tope 2026-12-31. Ensayo obligatorio sobre gastados (--desde 2026-10-26) antes de la primera evaluacion forward: SOL013 debe reproducir T1 n=117, EV +0,468, sin2 +0,145 (dias comparables y veredicto pueden cambiar). sha nuevos al DECISION_LOG. Si los evaluadores no estan corregidos antes de una evaluacion, su veredicto se marca PROVISIONAL y se recalcula con el codigo corregido; ningun veredicto calculado con el codigo viejo es terminal.
