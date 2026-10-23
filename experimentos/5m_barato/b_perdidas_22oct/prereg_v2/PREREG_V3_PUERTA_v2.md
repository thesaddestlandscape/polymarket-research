# PREREGISTRO v2 -- V3 «puerta de MERCADO» para B (H47-B maker) -- fijado 2026-10-22 ~15:05Z ANTES de calcular ningun resultado nuevo
Autor: cheap5m-statistical-validator (encargo del chief, linea B). Solo lectura sobre produccion. Fichero en solo lectura; sha256 en
`PREREG_V3_PUERTA_v2.sha256`. Cualquier cambio posterior = v3 nueva; los resultados de esta version se conservan.

## 0. Lo ya visto antes de fijar (declarado; NADA de esto cuenta como confirmacion)
- `V9_V3_INFORME.md` §3-§4 y `contraste/diagnosticos_secundarios.txt`: en I3 (simv2, libro real, 17-21 Oct, ETH/SOL/XRP) la puerta de
  MERCADO (spread de la 1.a cotizacion valida > 0,02) dio Delta +0,129, IC90 dia (+0,009,+0,241), cierre (+0,014,+0,249), 4/5 dias,
  neto +184,8 EUR, placebo particion p=0,033, re-simulado p=0,057 (1.058/4.311 mercados vetados). La puerta POR PASO (primaria del
  prereg v1) dio lo contrario (cambio -26,3 EUR, p=0,98). I4b (spread en el instante de CADA relleno de otros makers) Delta -0,055.
  Tramos de spread en el relleno sin gradiente. B real (origen, 20-22 Oct): `spread_post` Delta +0,710 (175 pos.), pujas >0,02
  aciertan 13,5 % vs 25,4 %. `b_seleccion_adversa/INFORME.md`: celda spread0<=0,02 de b_postmortem (n=89 +0,394 vs n=39 -0,3/-0,4).
- Por tanto los dias 17-21 Oct son DESCUBRIMIENTO para esta hipotesis y no confirman nada. NO he mirado ningun resultado de spread,
  puerta ni PnL en 06-16 Oct, ni las pujas/posiciones de B real posteriores a 2026-10-22 14:45Z (39 pujas nuevas aprox.).
- No he abierto `scan_v2_reglas.csv` ni `scan_pop_libro_reglas.csv`.
- Por que la poblacion no la replico: `ms_units.pkl` guarda el spread en t_obs = ts-4 s del token de CADA unidad (instante del relleno),
  no el de la 1.a cotizacion del mercado. La puerta es una propiedad del MERCADO medible con el libro (filas q) en T 295..65 s, que
  existe en `datalogs/sa_ms/ms_D.npz` (17-21) y en el archivo `VOL/m5_registro/m5_registro_D.csv.gz` (05-21 Oct, q/t de TODOS los
  tokens 5m, mismas filas crudas que `maker_ms_*`). No es un dato que falte: no se habia adjuntado.

## 1. Definicion EXACTA de la puerta (umbral unico, sin barrido)
Politica B-like identica a `b_seleccion_adversa/scripts/sim_v2.py` (sin los rasgos Binance, que no intervienen): rejilla
TK = 295,290,...,65 s antes del cierre (47 pasos); top del libro de cada token 5m = ultima fila q con t <= instante, solo filas con
t en [cierre-330 s, cierre+10 s] (mismo filtro que `ms_extract.py`); lado s = primera cara (YES o NO) cuyo bid top entra en
(0,11; 0,30] (pegajoso); precio de puja o = bid - k ticks (ETH 2, SOL/XRP 1, regla de redondeo de sim_v2), valido si bid en banda,
0,10 <= o <= 0,30, o < bid, o < ask. **1.a cotizacion valida** = primer paso con o valido. **spread_puerta** = round(ask - bid, 2) del
token del lado s en ese paso. **Mercado VETADO** si spread_puerta > 0,025 (es decir >= 0,03). Mercado sin cotizacion valida: no entra.
spread NaN en la 1.a cotizacion: no vetado y contado (como en v1). **t_puerta** = cierre - TK[paso de la 1.a cotizacion].
Hipotesis inversa («al reves», mercados que favorecen la puja): **subconjunto FAVORABLE** = spread_puerta <= 0,015 (= 0,01, tick
minimo). Umbral unico, fijado ahora.

## 2. Instrumentos (rangos de dias fijados ahora)
- **I5 simv2-OOS (primario):** simulador de sim_v2 reconstruido con el libro de `m5_registro` para **09-16 Oct (8 dias)**, cinta de
  rellenos on-chain `fills_loader.all_fills` (parquet `wallets_18oct`), desenlace oficial (`maker_ms_desenlaces_cache.json`),
  relleno 'cons' (operacion del lado con pc < p en (t+0,1; t+5,1], casado = ts-2,4), 5 acc. Mismos dias que NO intervinieron en el
  descubrimiento y anteriores al origen (B real 20-22).
  **Gate de reproduccion R0 (antes de usar I5):** el mismo codigo sobre 17-21 Oct con `m5_registro` debe reproducir los `simv2_D.npz`
  originales: >= 99 % de mercados comunes; en ellos >= 99 % de celdas con p identico (o ambos NaN), >= 99 % de mercados con el mismo
  spread_puerta y el mismo paso de 1.a cotizacion, >= 99 % de celdas minpc identicas; y Delta de la puerta en 17-21 dentro de +-0,01 de
  +0,129. Si R0 falla: I5 e I6 = DATA_BLOCKED (se reporta por que), no se interpreta nada.
- **I6 poblacion-puerta (primario):** unidades de OTROS makers `b_seleccion_adversa/datos/units/units_D.pkl` (primeras 5 acc por
  maker-mercado-lado, pc (0,10;0,30], T (60;300]), con la etiqueta de MERCADO calculada como en §1 a partir del mismo libro.
  **Poblacion valida:** unidad del lado s de la puerta (lado_c == s), casada despues de la decision (ts - 2,4 >= t_puerta), desenlace
  oficial presente, mercado con puerta calculable. Dias primarios **09-16 Oct**; 17-21 se reportan aparte (solapados con el
  descubrimiento: secundarios). Sensibilidad (no decide): sin la restriccion de hora; ambos lados.
- **I1 B real (descriptivo):** pujas reales del ledger posteriores a 2026-10-22 14:45Z, spread de la 1.a `puja_post` (la definicion de
  `spread_post`). n minusculo: solo descriptivo; alimenta el forward (§6).
- Cobertura: dia valido si el instrumento tiene >= 90 % de los 864 mercados ETH/SOL/XRP 5m del dia (288 cierres x 3) con libro en
  algun paso; si no, dia DATA_BLOCKED excluido y contado. Missing nunca es 0.

## 3. Metrica y estadistica
- EV PONDERADO por EUR (Sum pnl / Sum coste). I5: pnl = 5(win - p), coste = 5p por mercado rellenado. I6: columnas p (pnl) y c (coste).
  Sin comision (maker), rebate ignorado (+0,011 por EUR, no cambia signo).
- Delta = EV(rellenos en mercados NO vetados) - EV(rellenos en mercados vetados). **neto EUR = -pnl de los rellenos vetados**
  (perdidas evitadas - ganancias sacrificadas). En I5 la puerta es de mercado, asi que el re-simulado = particion (cambio de PnL total
  puerta - base = neto). EV de lo retenido frente a EV base.
- IC90 bootstrap percentil, 2.000 remuestreos, semilla 20261023, por DIA y por CIERRE (los 3 mercados de un cierre = una apuesta).
- **Placebo estricto (unico esquema):** se barajan las etiquetas de MERCADO (vetado/no) entre los mercados con puerta calculable del
  mismo estrato (dia, moneda, bloque de 6 h UTC del cierre), conservando el numero de vetados por estrato; 2.000 permutaciones,
  semilla 20261023+1. Estadisticos: Delta y neto. p = (#{placebo >= real} + 1)/(2.000 + 1). En I6 las unidades heredan la etiqueta.
- **Multiplicidad:** familia m = 4 hipotesis contadas: V3 por paso (ya mirada, v1), V3 puerta de mercado (H-V), puerta favorable
  (H-F), y la lectura de spread de B real/b_postmortem. Bonferroni: **alfa = 0,05/4 = 0,0125** para cada p de placebo. Ademas cada
  hipotesis tiene que pasar en LOS DOS instrumentos primarios (interseccion: no se elige el mejor instrumento).
- EV sin los 2 mejores dias (de Delta y de neto). Por moneda y por dia como sensibilidad (no deciden).

## 4. Gate de decision -- H-V (vetar puerta > 0,02), dias 09-16
**CONFIRMADA** si en I5 Y en I6, todas:
 G1 Delta > 0 y limite inferior IC90 por dia > 0.
 G2 limite inferior IC90 por cierre de Delta > 0.
 G3 placebo estricto: p(Delta) <= 0,0125 y p(neto) <= 0,0125, con neto - media placebo > 0 (EUR).
 G4 Delta > 0 en >= 6 de 8 dias; Delta sin los 2 dias de mayor Delta > 0; neto - placebo sin los 2 mejores dias > 0.
 G5 no degenerada: veta <= 50 % de los rellenos y retiene >= 40 % del EUR rellenado.
 G6 n minimo: I5 >= 2.000 rellenos y >= 300 vetados; I6 >= 5.000 unidades y >= 500 vetadas en >= 300 mercados vetados distintos.
 G7 criterio en EUR (I5): cambio de PnL puerta - base > 0 y EV ponderado de lo retenido > EV base.
**REFUTADA** si en I5 o en I6: Delta <= 0 en el agregado, o limite superior IC90 por dia de Delta < 0, o (I5) neto <= media del placebo.
**NO CONCLUYENTE** en cualquier otro caso (incluido G6 sin n). R0 fallido -> DATA_BLOCKED.

## 5. Gate -- H-F (al reves: pujar SOLO / preferentemente donde spread_puerta = 0,01), dias 09-16
**CONFIRMADA** si: I5 EV(rellenos FAVORABLES) > 0 con IC90 por dia y por cierre > 0, y DeltaF = EV(favorables) - EV(resto) > 0 con
p placebo (etiqueta favorable barajada en el mismo estrato) <= 0,0125; e I6 DeltaF > 0 con IC90 por dia > 0; n >= 300 rellenos favorables
en I5 y >= 1.000 unidades en I6. **REFUTADA** si DeltaF <= 0 en I5 o en I6, o EV(favorables) en I5 con IC90 por dia superior < 0.
**NO CONCLUYENTE** en otro caso. Aunque se confirme, I5/I6 no son B: maximo PROMISING.

## 6. Consecuencias y forward (fijado ahora)
- H-V REFUTADA -> no se construye shadow ni variante; la linea V3 se cierra en el cementerio para ESTA version.
- H-V NO CONCLUYENTE -> se disena (no se ejecuta) el forward solo lectura `shadow_v3m/` sobre `puja_post.libro` de B real + I5/I6
  diarios (dias >= 23-Oct del extractor `r1_fwd_cron`); NO se redacta uso en B.
- H-V CONFIRMADA -> lo anterior + MD de uso en B (variante en fichero nuevo, sin tocar `experimento_maker_h47.py` sha c82f5dc5f304b8a6)
  y en R2/R3. Nada se aplica a B real sin el gate forward, N>=500, /code-review y OK de Javi.
- Gate forward (B real, pujas tras 2026-10-22 14:45Z): >= 10 dias, >= 60 rellenos vetados, Delta > 0 con IC90 por dia y por cierre
  > 0, p placebo <= 0,0125, sin 2 mejores dias > 0, mismo signo en ambas mitades cronologicas. Falsador: Delta <= 0 en las 2 ultimas
  semanas moviles tras >= 10 dias.

## 7. Que NO se hace
No se barre el umbral (0,02/0,01 son los unicos), ni la rejilla, ni el retardo, ni la definicion de 1.a cotizacion. No se toca B, el
supervisor, procesos, crons, config live ni se envian ordenes. Datos pesados en `/root/polymarket-research-datalogs/v3m_puerta/`.
nice -n 19 ionice -c3, ulimit -v 2000000, fuera de 06:00-09:15Z.
