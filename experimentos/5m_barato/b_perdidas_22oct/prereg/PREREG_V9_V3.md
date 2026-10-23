# PREREGISTRO V9 y V3 para B (H47-B maker) -- fijado 2026-10-22 ~14:45Z ANTES de calcular ningun resultado de V9/V3 sobre simv2, cinta, poblacion ni pujas
Autor: execution-engineer (linea B, encargo de Javi 22-Oct). Solo lectura sobre produccion. NO se modifica tras congelar (sha256 en PREREG_V9_V3.sha256).
Cualquier cambio posterior = version nueva (PREREG_V9_V3_v2.md) y los resultados de la v1 se conservan.

## 0. Lo ya visto antes de fijar (declarado)
- `anatomia/INFORME.md` (B real 175 posiciones, 20-22 Oct, IN-SAMPLE): V9 neto +11,0 EUR (3/3 dias +), V3 neto +31,1 EUR (-2,9/+21,8/+12,2). De ahi salen las reglas: son el ORIGEN, no confirmacion.
- `b_seleccion_adversa/INFORME.md`: el spread del libro ya se barrio como rasgo en simv2 y poblacion («sin efecto robusto», `Spread<=0,01: -0,168 n=2.599`), pero NO el corte >0,02 de V3 ni nada de V9 sobre cinta/poblacion/simulador. NO he abierto `scan_v2_reglas.csv`, `scan_pop_libro_reglas.csv` ni ningun PnL de simv2/cinta/poblacion por estas reglas.
- Otro agente (risk-economics, `tandas/PREREG.md`) tiene R3 «una posicion por cierre» sobre B real y poblacion: es afin a V9 (V9 es por cierre Y LADO y cancela, no solo salta). No he leido sus resultados.

## 1. Reglas (parametros FIJOS, sin ajuste)
**V9 (primer relleno por cierre y lado).** Para cada (cierre = fin del mercado 5m, lado Up/Down) y MISMO decisor, solo cuenta el 1.er relleno (en el tiempo) entre las monedas ETH/SOL/XRP; en cuanto se detecta, se cancelan las pujas vivas del MISMO lado en las demas monedas del cierre. Un relleno posterior se considera VETADO solo si la cancelacion habria llegado antes que el: gap (tiempo del relleno posterior menos el del 1.o) >= L. Los rellenos con gap < L NO se vetan (pasan igual: latencia). No se cancela el lado contrario.
- Cinta (I2) y simv2 (I3): pasos de 5 s; L estructural primario = relleno en paso k >= k1+2 (gap garantizado >= 5,0 s); secundario k >= k1+1 (gap medio 5 s, minimo >0). Rellenos en el MISMO paso k1 no se vetan (conservador).
- Poblacion (I4, unidades on-chain, decisor = maker): grupo (maker, fin, lado_c); hora = `ts` (bloque - 2,4 s, error +-1,5 s); L primario = 3,0 s; sensibilidad L = 1,0 y 5,0 s.
- B real (I1): L primario = 1,0 s sobre `t_fill` (deteccion de B por get_order cada 0,5 s + cancelacion ~65 ms); sensibilidad 0,5 y 3,0 s.
**V3 (no pujar con spread > 0,02).** No se puja (y se cancela la puja viva) en un instante en que spread = ask - bid del token propio en el top > 0,02 (es decir >= 0,03; ticks de 0,01; tolerancia numerica: spread redondeado a 2 decimales > 0,025).
- simv2 (I3), primario: puerta POR PASO (en cada paso de 5 s solo se cotiza si spread <= 0,02; un mercado puede rellenar mas tarde si el spread se cierra). Secundario: puerta de MERCADO (si el spread en la 1.a cotizacion valida es > 0,02 el mercado no se puja, replica la definicion de B real).
- Poblacion con libro (I4b, `ms_units.pkl`, 17-21 Oct): unidad vetada si `spread` en el relleno > 0,02 (spread NaN = excluida y contada, nunca 0).
- B real (I1): `spread_post` de la 1.a `puja_post` (spread NaN = excluida y contada; tres limites: excluidas / tratadas como no vetadas / tratadas como vetadas).

## 2. Instrumentos y particion por dias (rangos de dias fijados ahora)
- I1 B real on-chain: `contabilidad_wallet_dedicada/posiciones.csv` (tanda_B no vacia; PnL on-chain; 175 posiciones, 20-22 Oct 11:40Z a 12:11Z; incluye las 9 SIN `puja_fin`) y las 275 pujas del ledger (166 rellenas, 109 no). ORIGEN de las reglas: DESCRIPTIVO / IN-SAMPLE, nunca cuenta para el gate. Se reproduce (anatomia/pos_anotado2.csv) y se anade IC por cierre, placebo y latencia.
- I2 cinta (simulador de cinta on-chain, sin libro): `b_seleccion_adversa/datos/sim/sim_*.npz`, 9-21 Oct (13 dias), ETH/SOL/XRP, politica B-like (delta ETH 2 / SOL,XRP 1 sobre la ultima operacion, repeg 5 s, T 295..65, relleno 'cons', 5 acc), via `scripts/sa_sim.py::run` sin cambios. SOLO V9 (no tiene libro).
- I3 simv2 (libro real): `datos/simv2/simv2_*.npz`, 17-21 Oct (5 dias), misma politica B-like con libro real (relleno 'cons' `minpc < p`). V3 y V9.
- I4 poblacion (rellenos on-chain de OTROS makers, unidad = primeras 5 acc por (maker, mercado, lado), pc 0,10-0,30, T 60-300): `datos/units/units_*.pkl` 9-21 Oct (13 dias) para V9; `datos/ms_units.pkl` 17-21 Oct para V3 (columna `spread`).
- Particion cronologica FIJA: **dias <= 19-Oct = CONFIRMATORIO PRIMARIO** (anteriores a la ventana 20-22 Oct de B real que origino las reglas); **20-21 Oct = solapado** (mismo periodo del origen, instrumento independiente de B real). Dias 9-16 solo en I2/I4-V9 (V9 tiene 8 dias previos a la ventana de B). Las reglas no tienen parametros que elegir, asi que no hay «descubrimiento» propio: nada se afina en un dia y se mide en otro; el reparto sirve para exigir que el signo exista ANTES del origen.

## 3. Metrica y estadistica
- EV siempre PONDERADO POR EUR: Sum pnl / Sum coste (pnl = 5*(win - p), coste = 5*p en I2/I3; columnas c/p reales en I4; $ on-chain en I1). Sin comision (maker); rebate maker ignorado (+0,011, no cambia nada, `b_seleccion_adversa/INFORME.md` §2).
- Por regla e instrumento: n fills, n vetados, coste vetado, pnl vetado/retenido, EV_vetado, EV_retenido, **Delta = EV_retenido - EV_vetado** (informatividad del veto), **neto = -pnl_vetado** (perdidas evitadas - ganancias sacrificadas, EUR), neto por dia, mejor/peor dia.
- Alerta de aritmetica: si el EV global es negativo, vetar CUALQUIER cosa «ahorra» (neto>0). Por eso la decision usa **neto sobre placebo** y **Delta**, no el neto bruto.
- IC90: bootstrap percentil 5-95 %, 2.000 remuestreos, semilla 20261022, (a) por DIA (remuestrear dias) y (b) por CIERRE (remuestrear cierres `fin`; las posiciones del mismo cierre son una sola apuesta, correlacion intra-cierre medida 0,20). EV sin los 2 mejores dias de Delta/neto.
- Placebo (2.000 permutaciones, semilla 20261022+1): **P-estricto** conserva la estructura de grupos: en V9 cada grupo (cierre, lado[, maker]) veta el MISMO numero de rellenos que la regla real, elegidos al azar entre sus miembros; en V3 se barajan las etiquetas vetado/no vetado entre los rellenos del mismo (dia, moneda) (misma cuenta). **P-simple**: veta el mismo numero de rellenos al azar dentro de cada dia. Se reporta p = P(neto_placebo >= neto_real); la decision usa el P-estricto. Para V3 re-simulado: se barajan las filas de spread entre los mercados del mismo (dia, moneda) y se vuelve a simular.
- Latencia (V9): fraccion del coste vetado cuyo gap es >= L en I1 (B real, t_fill) y en I4; distribucion de gaps (p10/p25/p50/p75/p90); neto con latencia aplicada (el de arriba ya la aplica: lo vetado exige gap >= L).
- Cobertura: n de rellenos/mercados esperados vs usados por dia; missing por columna; ninguna fila con dato ausente se trata como 0.
- Integridad de los inputs: sha256 de cada npz/pkl/csv en el manifest de salida.

## 4. Gate de decision (todas las condiciones, fijadas ahora)
**V9 = POSITIVO** si se cumplen TODAS, evaluadas por separado en I2 (13 dias) e I4 (13 dias), con el L primario:
 G1  Delta > 0 y limite inferior IC90 por dia > 0.
 G2  limite inferior IC90 por cierre de Delta > 0.
 G3  neto sobre placebo > 0 con p(P-estricto) <= 0,05.
 G4  Delta > 0 en >= 9 de los 13 dias, y neto sin los 2 mejores dias > 0.
 G5  Delta > 0 restringido a dias <= 19-Oct (primario).
 G6  Latencia: >= 75 % del coste vetado con gap >= 1,0 s en I1 y >= 75 % con gap >= 3,0 s en I4 (la regla es ejecutable con el camino de B).
 Ademas I3 (5 dias, libro real) debe tener Delta > 0 (consistencia de signo; no exige IC).
**V3 = POSITIVO** si se cumplen TODAS, en I3 (5 dias, puerta por paso) e I4b (5 dias):
 G1  Delta = EV(spread<=0,02) - EV(spread>0,02) > 0 y limite inferior IC90 por dia > 0.
 G2  limite inferior IC90 por cierre de Delta > 0.
 G3  neto sobre placebo > 0 con p(P-estricto) <= 0,05; y en I3 el re-simulado (PnL total puerta - base) > 0 con p(placebo de filas) <= 0,05.
 G4  Delta > 0 en >= 4 de los 5 dias, neto sin los 2 mejores dias > 0, y Delta > 0 en dias <= 19-Oct.
 G5  No degenerada: veta <= 50 % de los rellenos y retiene >= 40 % del EUR de relleno (un gate que veta casi todo no filtra).
 G6  Mismo signo de Delta en I3 e I4b (dos instrumentos independientes).
**NEGATIVO** si, para la regla: en cualquiera de los instrumentos primarios Delta <= 0 en el agregado, O el limite superior del IC90 por dia de Delta < 0.
**NO CONCLUYE** en cualquier otro caso. Dos instrumentos (I2/I3 son simulaciones, I4 es observacional de otros makers) NO son B: ni siquiera un POSITIVO es validacion; solo autoriza el brazo FORWARD SHADOW.
Consecuencia: POSITIVO en alguna regla -> se construye el brazo shadow solo-lectura para ESA regla y se redacta el diseno de la variante de B en un MD (nada se aplica a B real antes de N=500, `/code-review` y OK de Javi). NEGATIVO o NO CONCLUYE -> NO se construye el brazo shadow.

## 5. Gate del brazo FORWARD SHADOW (si se construye; fijado ahora)
Se evalua con datos posteriores a 2026-10-22 14:45Z (B real y simulado emparejado, mismas pujas): >= 10 dias forward y >= 60 rellenos vetados por la regla (n efectivo), Delta > 0 con IC90 por dia > 0 y por cierre > 0, neto sobre placebo p <= 0,05, neto sin 2 mejores dias > 0, y el mismo signo en las dos mitades cronologicas. Falsador: Delta <= 0 en las 2 ultimas semanas moviles tras >= 10 dias. Hasta alli: ACUMULANDO. Ningun cambio a B antes de N=500.

## 6. Que NO se hace
No se afinan umbrales ni se anaden reglas (V1, V2, V4...). Variantes extra (L alternativos, puerta de mercado, k+1) se reportan como sensibilidad y NO cambian el veredicto. Sin ordenes, sin config live, sin tocar `experimento_maker_h47.py` (sha c82f5dc5f304b8a6), `h47_tandas_supervisor.py` ni procesos.
