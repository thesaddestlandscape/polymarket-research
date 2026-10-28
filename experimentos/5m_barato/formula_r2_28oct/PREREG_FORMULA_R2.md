# PREREG_FORMULA_R2 — ronda 2: curva AS(delta) de la puja pasiva por profundidad + compuerta dC/dQ (5m barato, B)
Escrito y hasheado ANTES de ejecutar sim2.py sobre los 22 dias reales. Solo se han ejecutado: (a) selftest sintetico; (b) un corte truncado de un dia con desenlaces SINTETICOS para comprobar que el codigo corre. Ningun resultado real visto. Agente polymarket-quantum-alpha-miner; mandato del chief: <=20 llamadas, guard load1<14 y MemAvailable>1,2 GB, nice 19.

## 0. Que decide
Si existe una profundidad delta de puja pasiva (5 acc) con EV por relleno >= +0,02/acc tras la seleccion adversa, robusta en 22 dias (05-26 Oct) y 6 monedas. Si no: cotizar pasivo en 5m barato no tiene EV con informacion L1 + 15m y B solo se reabre con subsidio (rewards) o con L2/identidad. R1 (FORMULA_R1_B.md) dejo REJECTED la salida/cancelacion y sin calibrar el precio de cotizacion x*.

## 1. Poblacion y politica (hereda de alpha_miner_b_27oct/sim.py, congelado y no modificado)
- Unidades: (mercado, token) 5m con la elegibilidad de sim.py: bb retrasado 130 ms en [0,10; 0,29], spread >= 0,02, T en [60; 290] s al cierre, sin TD Binance activo. Se simula TODA unidad elegible (rellena o no) para obtener lambda(delta)=P(relleno|elegible).
- Puja virtual de 5 acc a x = r2(bb_retrasado + delta), reposicionada con el estado retrasado (como la vida P de B), cancelada por TD de B, parada a T=60 s; reloj de recepcion; sin salida (se mantiene al desenlace oficial); EV por acc = gana - x + rho(x), rho = 0,2*0,07*x(1-x) (rebate maker 20 %; el maker no paga comision).
- delta en {+0,01; 0; -0,01; -0,02} (parrilla fija, cuatro puntos).
- Relleno ESTRICTO: impresion SELL (o BUY del complementario a 1-p) a precio equivalente pe: pe < x rellena (travesia); pe = x rellena solo con cola: delta=+0,01 cola 0 (nivel nuevo); delta=0 cola = tamano visible del bid retrasado en el ultimo reposicionamiento, se consume con el volumen en el nivel y solo el exceso rellena; delta<0 NUNCA en el nivel (cola no observable con L1): solo travesia. Sin credito por cancelaciones por delante.
- Cotas OPTIMISTAS (no candidatas): O_z0, O_m1, O_m2 = mismas pujas con cola 0 (el volumen en el nivel rellena). Sirven para la regla del logger L2 (sec. 8).

## 2. Variante nueva (UNA, un solo mecanismo): compuerta de informacion para NO cotizar cuando el barrido es inminente
eps_t = q^_t - m_t, con q^ = sigma( logit m + A2*dC + A3*dQ ), A2 = 0,026 y A3 = 0,085 FIJADOS (coeficientes de la clase E de R1, ajustados solo en IS; sin refit; zB omitido: R1 mostro que Binance no aporta). dC = logit(FV15) - logit(m) con FV15 = Phi(w), w = [sqrt(T15-t)*Phi^-1(mid15(t)) - 1{j>=2}*sqrt(T15-t0)*Phi^-1(mid15(t0))]/sqrt(T5-t) (mid del 15m del mismo lado, edad <= 15 s; t0 con edad <= 30 s; sin dato => dC=0); dQ = (bs-as)/(bs+as) en el nivel 1; todo con el estado retrasado 130 ms. La puja se retira (como si la TD) mientras eps < c: G10 c=-0,010; G5 c=-0,005; GP5 c=+0,005 (cotizar solo si la informacion dice que el token esta a su precio o infravalorado). Control de inversion I5: se retira mientras eps > +0,005 (informacion usada al reves). Misma parrilla de delta.

## 3. Cota analitica (calculada ANTES de medir)
Si eps ~ N(0, sigma^2) y la compuerta solo actua a traves de eps, el EV/acc de los rellenos retenidos sube, como maximo, E[eps | eps >= c] (pp/acc) frente a sin compuerta; sigma_eps medida en R1 sobre rellenos = 1,3 pp (rms de q^-mid), derivada de dLogLoss ~ 5e-4 nats por fila. Tabla (sigma en pp, c en pp, % bloqueado, ganancia maxima en pp/acc):
| sigma | c | bloquea | ganancia max |
|---|---|---|---|
| 0.8 | -1.0 | 11 % | +0.16 |
| 0.8 | -0.5 | 27 % | +0.36 |
| 0.8 | +0.5 | 73 % | +0.99 |
| 1.3 | -1.0 | 22 % | +0.50 |
| 1.3 | -0.5 | 35 % | +0.74 |
| 1.3 | +0.5 | 65 % | +1.38 |
| 2.0 | -1.0 | 31 % | +1.02 |
| 2.0 | -0.5 | 40 % | +1.29 |
| 2.0 | +0.5 | 60 % | +1.93 |
| 2.6 | -1.0 | 35 % | +1.48 |
| 2.6 | -0.5 | 42 % | +1.77 |
| 2.6 | +0.5 | 58 % | +2.40 |
Techo con signo perfecto (bloquear si eps<0): 0,798*sigma = sigma 0.8 pp: 0.64 pp ; sigma 1.3 pp: 1.04 pp ; sigma 2.0 pp: 1.60 pp. El umbral de exito es +2,0 pp/acc ABSOLUTOS, y el punto delta=+0,01 sin compuerta vale en R1 EV/acc ~ 0 (IS) y -0,8 pp (OOS) (EVw +0,0003/-0,0329 por EUR, p0~0,23). Prediccion: ninguna compuerta puede elevar una celda mas de ~+0,5-0,75 pp/acc (sigma=0,8-1,3) ni cruzar +2 pp salvo que la celda base ya este cerca de +1,3 pp. Un efecto de compuerta > +1,5 pp/acc se investiga como fuga/bug ANTES de tratarlo como hallazgo. Se mide sigma_eps real en las elegibles y se recalcula la tabla.

## 4. Estadistica
- EV/acc = sum pnl / sum acc de los rellenos (agregado de las 22 jornadas); EVw = sum pnl / sum coste; pnl = acc*gana - coste + 0,2*acc*0,07*p(1-p) con p = coste/acc. IC90 por dias: bootstrap de dias (B=2000, semilla 2811, dias con reemplazo, razon de sumas). Sin los 2 mejores dias: se quitan los 2 dias de mayor sum pnl.
- Familia candidata = 16 celdas (4 delta x {U sin compuerta, G10, G5, GP5}). MAX-STATISTIC: T_c = EV_c/se_c (se por bootstrap de dias), nula por bootstrap centrado de dias con los mismos remuestreos para todas las celdas; p_max = P(max T* >= max T_obs).
- PLACEBO de relleno (bajo la nula «el relleno es independiente del desenlace»): cada relleno recibe el desenlace de una elegible al azar del mismo estrato (moneda x dia x bucket de bb de 0,05), B=500; p_plac por celda = P(EV_placebo >= EV_obs); p_plac(max-statistic) sobre las 16 celdas con Z estudentizado. AS(delta) = E[tasa_estrato - gana | relleno] por acc = (EV_placebo_esperado - EV_obs) con IC90 por dias; es la brecha de seleccion adversa en terminos de acierto (una identidad de medicion: mide el sesgo de los rellenos, no un coste evitable por si solo).
- Particion: decision primaria sobre los 22 dias agrupados; secundario: IS (05-22) y OOS (23-26) por separado. Control de implementacion: U_p1 debe reproducir las unidades P de R1 (sh, coste, t1) en >= 99 % y EVw IS +0,0003 / OOS -0,0329 (tolerancia +-0,002); si no, es un bug y se corrige antes de leer el resto.
- Desagregado moneda x bucket (4 buckets de bb de 0,05) para U_p1 y la mejor celda con n>=750, tras el agregado. lambda(delta), k_eff (pendiente de ln lambda frente a la profundidad en centimos), EV|relleno lineal en la profundidad y x* = R - 1/k: d_R = profundidad con EV|relleno = 0, d* = d_R + 1/k_eff (optimo interior solo si la pendiente es > 0).

## 5. Criterios (por celda candidata)
CANDIDATE solo si TODOS: c1 EV/acc >= +0,02; c2 n rellenos >= 750; c3 >= 10 dias con >= 5 rellenos; c4 IC90 por dias del EV/acc > 0; c5 EV/acc sin los 2 mejores dias > 0; c6 p_max < 0,05; c7 p_plac(max-statistic) < 0,05; c8 EV/acc > 0 en IS y en OOS; c9 (compuertas) dEV frente a U del mismo delta con IC90 por dias > 0 y dEV de I5 < 0. EXPLORATORY: c4, c5 y c8 pero no todos. REJECTED: resto. Fracaso global: ninguna celda CANDIDATE (en tal caso AS(delta) >= (m-x)+rho para todo delta).

## 6. Regla del logger L2
Se necesita el logger (L2 top-5 + identidad) SOLO si alguna cota optimista O_* cumple c1 y c4 y su celda estricta no; si ninguna cota optimista supera +0,02, la profundidad <= 0 queda cerrada con L1 y el logger no se justifica para esta pregunta.

## 7. Limites declarados
Relleno sin credito por cancelaciones por delante (conservador en delta=0) y sin cola observable en delta<0 (conservador); posibles rellenos en el nivel perdidos. Solo L1; 4 dias OOS (ICs anchos); desenlaces del cache oficial; la elegibilidad hereda B (bb en [0,10;0,29]). Ejecucion 10:00-11:xx Z fuera de la ventana 06:00-09:30Z, nice 19, ionice idle, guard load1<14 y MemAvailable>1,2 GB, ulimit.
