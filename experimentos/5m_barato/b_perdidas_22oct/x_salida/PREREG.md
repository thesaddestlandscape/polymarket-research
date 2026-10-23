# PREREG X-SALIDA (OLA 5) - salida a nivel de CURVA DE SALDO/TANDA de B (H47-B real), 23-Oct-2026 ~08:58Z
Autor: agente risk-economics. Solo lectura. B, supervisor, ejecutores, crons, config: intactos. Sin ordenes, sin claves, sin commits.
Congelado ANTES de calcular ningun estadistico de este informe (se verifica con `sha256sum -c PREREG.sha256`). Todo lo posterior va marcado POST-HOC.

## 0. Ya visto antes de fijar esto (declarado)
- `tandas/INFORME.md` (22-Oct): PnL por tanda 1-23, 15 perdedoras -58,08 / 8 ganadoras +55,76; 11 reglas de tanda/cartera NO pasan; DD observado = varianza de pago; autocorr lag-1 del EV por cierre +0,006; concordancia intra-cierre 0,774.
- `salida/INFORME.md`: 40 reglas de salida/cancelacion por posicion, todas negativas en test.
- `r3_escalado`, `ADENDA_22OCT_B_R3.md`: n_eff, techos R3, Kelly corregido g=n*EV^2/(2*sigma^2).
- Tabla por tanda de `resumen_por_experimento.md` hasta la tanda 27 (PnL/tanda). NO visto: la curva por cierre, ninguna regla de curva, ningun test de estructura de los incrementos.
- Contexto B a las 08:55Z: saldo on-chain 5,65 pUSD < suelo duro 12: B esta PARADO por capital (supervisor "no relanzo").

## 1. Datos (snapshot con sha en HASHES.txt; copia en datalogs/x_salida/)
- DB (B real): `contabilidad_wallet_dedicada/posiciones.csv`, experimento H47-B, estado liquidada_* (desenlace oficial gamma), unidad posicion; **cierre** = `fin_mercado_utc`; orden por `fecha_primer_fill_utc` dentro de cierre; `tanda_B` tal cual. X_c = suma de pnl_realizado de las posiciones del cierre.
- DP (poblacion real de otros makers, ETH/SOL/XRP 5m, 17-22 Oct): `cola_posicion/datos/pop_units_2026-10-{17..22}.csv.gz` (unidad = maker x mercado x lado, 5 acc, pc 0,10-0,30, T 60-300 s; columnas fin, ts, coste, pnl, act, dia). Solo filas con `des` conocido (n esperado ~28.871).
- DL (proxy largo, precio de MODELO, NO ask real): `detector_regimen/datos/panel_{y2025,backfill,dic_ene,bookticker}.csv.gz`, T=180, filas con q en [0,10; 0,30], monedas ETH/SOL/XRP; pnl por accion = win_proxy - q; cierre = (tmin*60+300); dedupe (coin,tmin) y por dia; dias solapados entre paneles: se conserva el de mayor prioridad bookticker > backfill > dic_ene > y2025. Que NO sustituye: precio ejecutable, relleno, selection adversa.
- Capital/ledger B de contexto: `movimientos.csv`.

## 2. PARTE A - estructura de los incrementos (unidad = CIERRE; serie ordenada por tiempo; pares solo dentro del mismo dia UTC)
Series: DB: X_c ($). DP: X_c = suma pnl de unidades del cierre, y se reporta tambien la serie estandarizada. DL: X_c = suma pnl_proxy por cierre.
Estadisticos (6, familia Bonferroni x6 por dataset; permutaciones 5.000, semilla 20261023):
- S1 autocorrelacion lag-1 (Pearson, media ponderada por pares intra-dia) y lags 2-3 descriptivos. Nulo: permutar el orden de los cierres DENTRO de cada dia (preserva distribucion y nivel del dia).
- S2 EV condicionado al nivel acumulado: pendiente b de X_c sobre P_c (P_c = suma de X de los cierres previos del MISMO dia), nulo: permutar dentro de dia (recalcula P). Reporta tambien diferencia de medias X_c | P_c >= +1 sigma_c vs <= -1 sigma_c.
- S3 reversion tras pico: media de X_c cuando la curva intra-dia esta a >= 2 sigma_c por debajo de su maximo del dia (y el maximo >= 2 sigma_c) menos la media del resto. Nulo: permutacion intra-dia.
- S4 ratio de varianza Lo-MacKinlay VR(8) de la curva intra-dia (sumas de 8 cierres), nulo: permutacion intra-dia. (VR(2,4,16) descriptivos.)
- S5 hora: max sobre los 6 bloques UTC de 4 h de |EV_bloque - EV_global| (EV = suma pnl / suma coste), nulo: permutar etiquetas de bloque dentro de dia. Con IC90 por dia por bloque. B real: solo descriptivo (3 dias).
- S6 nivel diario: autocorr lag-1 del EV diario (solo DL, >= 400 dias) y razon var(medias diarias)/var esperada por permutacion de cierres entre dias.
Potencia: para cada dataset se reporta n de cierres, n_eff (ICC), y diferencia minima detectable (MDE) del lag-1: ~2,8/sqrt(n) (alfa 5 %, potencia 80 %).
**Criterio "hay estructura explotable"** (todo a la vez): mismo signo y p_Bonf(x6) < 0,05 en DL y en DP, p crudo < 0,05 en DB o DB no contradice (signo igual), y que la magnitud, convertida a regla (parte B), mejore el PnL frente al placebo. Si no: "martingala / sin estructura detectable" con su MDE (no es "demostrado que no hay": es que no se ve al nivel MDE).

## 3. PARTE B - reglas de salida sobre la curva (simulador de tanda; ver scripts/xsal_sim.py, fijado aqui)
Estado: E = equidad realizada (capital + PnL de posiciones resueltas); suelo F; base E0 de la tanda; ancho Bd (presupuesto). Por cierre (en orden), posiciones del cierre por hora de fill: se TOMA la posicion si E - F - pendiente - coste_i >= 0 (si no, bloqueada, como `bloqueo_suelo_saldo`); al resolverse el cierre E += suma pnl de las tomadas. Tanda agotada si E - F < 1,05: se rota (E0=E, F=E-Bd) solo si E >= H + Bd (H = suelo duro 12) y la politica de rotacion lo permite; si no, B se PARA el resto de la trayectoria. Ratchet R0 (supervisor): si E - F >= Bd + 1 entonces F = E - Bd.
Reglas (familia de 14 alternativas + R0; parametros fijos aqui):
- R0 ACTUAL: Bd=5, ratchet +1, rotacion ilimitada (mientras E>=H+Bd).
- W2.5, W3.5, W8 (tamano de tanda Bd=2,5 / 3,5 / 8; W8 solo diagnostico).
- NR (sin ratchet: la base no sube con las ganancias; F fijo hasta agotar la tanda).
- TPd3, TPd6 (objetivo diario: cuando E - E_inicio_del_dia_UTC >= 3 / 6, parar hasta el dia siguiente).
- TPT3, TPT6 (objetivo de tanda: cuando E - E0 >= 3 / 6, cerrar la tanda y pausar 12 cierres, luego nueva base).
- LOCK3_50, LOCK6_50, LOCK3_75 (bloqueo parcial: cuando el pico de beneficio de la tanda P >= L, F = max(F, E0 + f*P), f=0,50 / 0,50 / 0,75; L=3 / 6 / 3).
- MAXROT1, MAXROT2 (maximo de rotaciones por dia UTC: tras agotar la 1.a / 2.a tanda del dia, parar hasta el dia siguiente).
- TIME40 (parar hasta el dia siguiente tras 40 cierres con al menos una posicion tomada en el dia).
Metricas (pareadas con R0 sobre el MISMO flujo): PnL total ($), posiciones tomadas, coste desplegado, EV pond = sum pnl/sum coste de lo tomado, drawdown maximo de E, peor tramo, g = ln(E_fin/E_ini)/dias (por dia), ruina (E < H+Bd antes del fin).
Entornos:
- E-B (replay real): las posiciones reales de DB en orden, con E_ini = 19,59 y H=12 (S_real) y con E_ini = 40 (S_free). Control de fidelidad: R0 vs el PnL real de B (se reporta la discrepancia; NO se ajusta).
- E-P (pseudo-B de poblacion): flujo = bootstrap de bloques de 12 cierres consecutivos (1 h) del dia de DP; cada cierre elegido con probabilidad igual al perfil horario de B (fills/hora de B / cierres con unidades de DP por hora) y, si se elige, se toman 1 + Poisson(0,8) unidades al azar del cierre (calibrado a 72-76 fills / ~40 cierres de B); 30 dias por trayectoria, 3.000 trayectorias, S_free (E_ini=60) y S_real (E_ini=19,59, 10 dias).
- E-S (sintetico): mismas posiciones (coste, acciones, hora) con acierto Bernoulli q = p(1+e) y cluster intra-cierre rho=0,333 (copula gaussiana), e en {-0,10, -0,05, 0, +0,05, +0,10}, 2.000 trayectorias; sirve para ver Delta(regla) como funcion de EV.
Placebo: el MISMO flujo con los cierres permutados dentro de cada dia (conserva distribucion, destruye el orden); Delta_estructura = Delta(real) - Delta(permutado). IC90: (a) por trayectoria (ruido de Monte Carlo, NO incertidumbre del dato), (b) por DIA de la poblacion (replicas por cada uno de los 6 dias con IC t de 5 gl) y (c) en E-B bootstrap de dias/cierres de DB.
**Criterio de palanca util** (todo a la vez, fijado ahora): en E-P S_real, DeltaPnL medio > 0 con IC90 por dia > 0; Delta_estructura > 0 con IC90 por dia > 0; p placebo < 0,05/14; Delta EV pond. del retenido >= 0 (no solo quitar volumen); Delta > 0 en E-B (S_real) y en >= 5 de 6 dias de DP; Delta en E-S con e=+0,05 no peor que -10 % del PnL esperado sin regla. REGLA DURA: si los incrementos son martingala (S1-S4 no pasan), Delta = mu * Delta N (Wald): se mostrara en E-S que Delta(regla)/Delta(posiciones tomadas) = EV, y la conclusion es "ninguna regla crea EV; solo cambia varianza/camino".

## 4. PARTE C - tamano y 200 k
- EV, sigma^2 por EUR, n_eff y DEFF de DB (cierre; IC90 por cierre y por dia) y de DP (IC90 por dia y cierre). g = n_eff*EV^2/(2*sigma^2) por dia; f* = EV/(sigma^2*DEFF); Kelly y 1/2 Kelly; capital minimo para stake 1,05 $.
- Tabla EV/EUR -> nocional/dia para 200.000 EUR/ano (365 y 260 dias) = 548/EV (365 d); comparado con capacidad medida (B real $/dia; pool DP $/dia; techo R3 K=20 de `r3_escalado`); fraccion del pool necesaria.
- Reinversion por tramos: Monte Carlo (2.000 trayectorias) con stake por tramos = clamp(f_frac*W, 1,05, tope de profundidad 2,44 $ por relleno [K=20 de `r3_escalado`]) para EV real en {+0,03, +0,07, +0,11, +0,20} y W0 en {19,59, 75}: dias hasta el tope, ingreso anual en el tope, P(ruina). Hueco honesto = 200.000 - suma de palancas conocidas, cada una con su etiqueta (VALIDATED/EXPLORATORY/SCENARIO).
- Modo pasivo: `scripts/pasivo.py` recalcula cada regla sobre cada tanda real con el ledger en curso y escribe una linea por dia en datalogs/x_salida/pasivo.csv (sin tocar B).

## 5. Multiplicidad y limites (declarados ahora)
Familia primaria de la parte B: 14 reglas (Bonferroni 0,05/14 = 0,00357); de la parte A: 6 estadisticos por dataset. Todo lo no listado aqui es POST-HOC. Los $ no se convierten a EUR. B esta parado por capital, de modo que "forward de la regla" solo existe en modo pasivo/shadow del flujo de la poblacion hasta que Javi decida capital. Un unico instrumento de ejecucion (B) con 3 dias de reloj: ninguna conclusion sobre B real es de gate.
