# DISEÑO V2 — B maker 5m barato: filtrar, salir y explotar tras la carrera L2 (10-Nov-2026 ~17:50Z)
Estado: DISEÑO + PRERREGISTRO EXPLORATORIO. 0 órdenes, solo lectura, sin commit. Autor: polymarket-quantum-alpha-miner.
Hereda: DISENO.md (sha 1e2d13cc…, NO_EDGE en TRAIN), passT.py (sha a8b9d7a0…), PREREG_Q11_THRU1_FWD (sha 68ca25a0…) para GEO6 y salud de horas.
Todo cambio posterior al sha de este fichero = versión V2.1, congelada ANTES de leer cualquier dato >=10-Nov de estas reglas.

## Visto antes de congelar (declarado)
Solo días QUEMADOS: 03-07-Nov (rellenos G0 válidos del estudio de carrera, n=1.350, out/trg_*.pkl + out/g0_fills.pkl) y, para el valor
de salida, 03/04/07-Nov (frente2_sueltos_10nov/out/F_*.pkl). Nada de 08/09-Nov para estas reglas; nada >=10-Nov en absoluto.
Descriptivos en scratchpad de la sesión (desc_train.py … desc7.py), no forman parte del arnés. Cifras en §1 (no confirmatorias).

## 0. Inventario anti-duplicación
| Línea | Estado | No repetir | Hueco que queda |
|---|---|---|---|
| L2 carrera D/V/S (este dir.) y H-LAT/CXB_l (thru1) | NO_EDGE / INSUFFICIENT: veto 79-99 %, Δ ≈ placebo; V5 anti-selectivo (p 0,99) | disparar por distancia/caída/profundidad sin condicionar; contar estáticos como carrera | la carrera NO es el cuello (rápidas 60-1500 ms ≫ Λ 30-60 ms): falta discriminar en el instante de exposición |
| GEO6 / PG_O50 / CXJ150 / PC_AS (thru1 fwd desde 07-Nov) | forward en curso, 0 días válidos | filtros de colocación por distancia (el «estático» de L2 ⊂ GEO6) | dentro de GEO6-OK las rápidas son 22 % de rellenos y 62 % de la pérdida |
| Frente 2 sueltos: SALIDA, IW5, GEO, SPR2 | salida REFUTADA (−0,286 TRAIN; markout/stop/Binance/A30 <0); IW5 FALTA_INFO (motor 12 d: G0 −430 €, GEO6∧IW5 −132 €) | salida incondicional o condicionada a markout/stop; venta directa (5 acc × 0,12 < 1 $) | salida condicionada a la dinámica PREVIA al relleno, vía complementario |
| DB1 / DB2 / H-DB3 (db1/, docs/PREREG_*) | DB1 +152,6 vs nulo +78,3 (~2 sd), fwd desde 10-Nov; DB2 ≈ nulo; H-DB3 congelado sin implementar | Binance 1 s, primer print contrario, pausa por ráfaga R0 on-chain | pausa disparada por NUESTRO relleno (ms, sin identidad) y prohibición de re-armar |
| Precursores e identidad: H-SURF, H-SURF-L2, R1-R3, R9-R10, Q5 | REJECTED / NO VIABLE (AUC sin EV; cola AUC 0,49; σ_L2 máx 1,64 pp; fugas NaN) | predecir y−mid o barridos con actividad/cola/Binance sobre el libro medio; rasgos NaN-si-vacío | predicción condicionada al EVENTO «paso a mejor bid» (población de exposiciones) |
| Salidas 27-28 Oct (repeg+TD, ask avg+0,01, A30, cubrir con favorito) | REJECTED (≈0; −0,22; Δ solo suelo 1 c; −2,6 %) | salidas maker a precio fijo; cobertura incondicional | cobertura tomadora solo donde P(gana|estado) < bid − comisión |
| Frente 3 / S1 (P(gana|relleno) ex ante, predictive-alpha-engine) | PENDIENTE, sin artefacto | — | añadir clase de llegada y orden en la ventana como estado |

## 1. Qué dijo de verdad la carrera L2 (TRAIN 03-07-Nov, descriptivo)
- Base: n=1.350, EV −0,245 €/€, acierto 0,114, precio medio 0,150, edad mediana de la orden al relleno 23 s.
- Clases por M = tf − t_top (t_top = primer evento L2 con mejor bid <= L): estático 144 (−0,565; acierto 6,2 %), sin toque 122 (−0,249),
  <=60 ms 28 (−0,031), 60-500 ms 117 (−0,415), 0,5-1,5 s 142 (−0,548), 1,5-5 s 255 (−0,120), >5 s 542 (−0,113).
- Dentro de GEO6-OK (bid−L >= 0,06 al armar; aproximado con L2): rápidas 60-1500 ms n=208, −0,502, acierto 7,7 %, −79,5 € (5/5 días <0);
  lentas n=617, −0,068; total GEO6-OK n=951, −127,5 €.
- Por qué «veto, no filtro»: todo subconjunto de G0 es <0 en estos días ⇒ cualquier cancelación mejora y el placebo iguala; D/S cuentan como
  evitados los estáticos (eso es colocación = GEO6); V5 cancela sobre todo rellenos >5 s tras la caída (−0,097) y barridos inmediatos (+0,27).
- Proxy ex ante (primera caída V en <=1 s antes del paso a mejor bid): fracción de rápidas 24 % → 31-36 % (n=87-124). Señal débil.
- Valor de salida (bid +250 ms − 1 tick − comisión tomadora, frente a mantener, por acción; 03/04/07): rápidas n=147 +0,054,
  IC90 por cierre (+0,020; +0,084), 87 cierres, 3/3 días >=0, tamaño >=5 acc en el bid 97 %; GEO6-OK rápidas n=116 +0,053 (+0,010; +0,091);
  lentas n=384 −0,019 (−0,061; +0,021). Mecanismo de la salida refutada: bid post-relleno 2-3 pp BAJO el acierto + ~0,7 pp de comisión;
  la latencia no cuenta (bid +250 ≈ bid +1000). Solo en rápidas el bid queda POR ENCIMA del acierto (0,121 vs 0,052).
- Orden en la token-ventana (2,9 rellenos por token-ventana, todos en niveles distintos 0,10/0,13/0,16/0,19): primero n=464 −0,120
  (acierto 14,7 %); tras rápida <=15 s n=175 −0,501; tras otro <=15 s n=536 −0,191; >15 s después n=175 −0,579; mediana del hueco <=15 s = 0
  (barrido simultáneo, no evitable). En GEO6-OK, quedarse con el primer grupo (<=60 ms) quita 429 (45 %) con −0,290 y deja 522 con −0,109.
- Ninguna combinación deja EV>0 en TRAIN: manda el día (07-Nov −43 € incluso en lo conservado).

## 2. Hipótesis (rankeadas por valor de información / coste)
### H0 (nula)
La toxicidad de rápidas y segundas es ruido de 3-5 días o régimen: ninguna regla supera al placebo a igual cobertura en días nuevos y B G0
es <=0 en todo subconjunto ex ante. Predicción: la etapa 0 falla (Δ ≈ placebo, días mixtos).

### H-EXIT (1.º) — cobertura inmediata de la llegada rápida
Mecanismo: el relleno rápido ocurre en mitad de un repreciado; las demás pujas del libro (makers rancios) quedan ~0,25-1 s por encima de la
probabilidad realizada. Salir = vender a esos rancios, como el tomador informado. En lentas el mercado está calibrado al mid y salir paga.
Regla exacta: para cada relleno de la cartera base en tf: t_top = primera cotización L1 de sa_ms (ms_D.npz, reloj de RECEPCIÓN, el mismo de
tf) en [t_dec+68 ms, tf] con mejor bid <= L (si ya lo es en t_dec+68, t_top = t_dec+68). M = tf − t_top. Si 0 < M <= 1.500 ms: FAK de compra
de q acc del token COMPLEMENTARIO con límite a_lim = 1 − (b_tf − 0,01) (b_tf = mejor bid del barato en tf); el par se mantiene a resolución
(o merge). Sin t_top, o M > 1.500 ms: mantener.
Ejecución simulada: casado en tf + d_det + 175 ms (30 ms ida + 145 ms retraso tomador); precio = mejor ask del complementario en tf+250 ms
(sa_ms; si falta, espejo 1 − bid del barato), tamaño >= q y <= a_lim recorriendo niveles; lo no cubierto se mantiene.
Δ por acción = (1 − a − 0,07·a·(1−a)) − 1{gana}. Sensibilidades: +500/+1.000 ms, −2 ticks, d_det 150 ms, M_cut 1.000/2.000, excluir M<=60,
M con reloj L2 (b40, 03-09-Nov) con concordancia de clase >=90 % o se declara.
Diferencia con lo refutado: frente 2 y las salidas de octubre condicionaban a markout, stop, Binance, A30 o nada; aquí la condición es la
dinámica PREVIA (conocida en tf, sin mirar el futuro) y la salida va por el complementario (nocional ≈4,4 $ >= 1 $).
Placebo: salir de un subconjunto aleatorio del mismo tamaño por día×L (5.000 perm.). Inversión: salir solo de las lentas (debe dar Δ<0).
Etapa 0 (réplica en días quemados NO vistos para esta pregunta: 26-Oct..02-Nov + 08 + 09-Nov = 10 días; mata o deja seguir, no confirma):
Δ total >0; IC90 por cierre >0; >=7/10 días >0; p placebo < 0,05/3; sin los 2 mejores días >0; >=2/3 monedas >0; tamaño >= q en >=90 %;
n >= 150 coberturas (si no, INSUFFICIENT). Riesgo declarado: si 26-31 Oct (TRAIN de frente 2, salidas <0) sale <0, la señal de 3 días era ruido.
Coste: datos existentes (RT_, ms_D.npz, F_*.pkl; ext.py de frente 2 solo para 09-Nov); ~15 min CPU; forward <=5 min/día tras el RT_ del cron
thru1 (13:20Z).

### H-ONE (2.º) — una ficha por token-ventana
Mecanismo: el primer relleno revela que una ola vendedora llegó a nuestra escalera; los niveles siguientes solo se rellenan si el precio sigue
cayendo (cascada) o el token reprecia dentro de la ventana. Política de inventario: máximo q acc por (token, ventana).
Regla exacta: en cada token-ventana (dia, token, fin), al primer relleno t1 de la cartera base se cancelan los demás niveles vivos de ese
token y no se re-arma hasta el cierre. Se conservan los rellenos con tf <= t1 + Λ (Λ = 60 ms; sensibilidad 30/150) y se quitan los posteriores.
Es un subconjunto exacto de G0 (cancelar sin reposición ES la política, no una cota).
Diferencia: H-DB3 pausa tras una ráfaga R0 on-chain (identidad, >=2,2 s tarde, solo ráfagas); H-ONE se dispara con nuestro relleno en ms,
también en sueltos, y prohíbe re-armar. Predicción diferencial: bajo H-DB3 la pausa tras sueltos <= placebo; bajo H-ONE también mejora.
Placebo: conservar un grupo ALEATORIO por token-ventana (mismo Λ); segundo placebo: quitar el mismo nº de rellenos al azar por día×L.
Inversión: conservar el ÚLTIMO grupo.
Etapa 0 (15 días quemados, solo cordura: la premisa ya se vio en RE-Q11 H-TOX-2 «primera vs re-armado» y en §1): KILL si Δ sobre GEO6
<= placebo de grupo aleatorio o <10/15 días positivos. La confirmación es solo el forward. Reportar solapamiento con H-DB3/DB1.
Coste: segundos sobre RT_ existentes; forward igual que H-EXIT.

### H-TOP (3.º) — cancelar al pasar a mejor bid si hay ola
Mecanismo: la llegada rápida es la cola de una ola (Binance, ráfaga de prints, caída del bid); si se anticipa en t_top la carrera se gana.
Población de decisión: TODAS las transiciones a mejor bid de órdenes G0 vivas (out/g0_segs.pkl, rellenas o no), nunca solo rellenos.
Rasgos en t_top (recepción, <= t): f1/f2 caída del mejor bid en 1 s / 3 s (L1); f3 retorno Binance 1 s contra el lado (registro bnreg,
columna de RECEPCIÓN); f4 nº y tamaño de prints del token en 2 s (filas T de libro5); f5 tamaño en L y en [L−0,03, L) (b40); f6 T restante;
f7 L y moneda. NaN = indicador explícito; se descarta el rasgo si |P(y|NaN) − P(y)| > 2 pp en DESC (trampa R10).
Modelo: logística C=1 para y = 1{relleno en <=1.500 ms tras t_top}, ajuste en DESC 03-07-Nov; θ fijado en DESC para que lo cancelado contenga
<=30 % de los rellenos GEO6-OK. Acción: score >= θ → cancelar en t_top + Λ y no re-armar en la token-ventana.
Precondición VAL (08-09-Nov): AUC(y) >= 0,60 y Δ > placebo de igual cobertura; si no, KILL antes del forward.
Diferencia: V/D/S disparaban en cualquier momento de la vida (veto); R3/H-SURF predecían y−mid o barridos sobre el libro medio.
Expectativa baja-media (proxy 24 %→31-36 %). Coste: rasgos L2 03-09-Nov (~2 min/día) + ajuste; depende de la dependencia (ii).

### H-NIVEL (4.º, dueño Frente 3 / predictive-alpha-engine) — no armar donde P(gana|relleno) < precio + costes
P̂(gana | relleno, moneda, L, gap GEO, T, orden en la ventana, clase de llegada esperada) calibrada en DESC; armar solo niveles con
P̂ >= L + comisión efectiva + 0,02. En §1 las lentas a L 0,10/0,13 aciertan 5-6 % frente a 13-19 % a 0,16/0,19 (3 días): riesgo de micro-bucket;
exige >=10 días DESC y forward. «Reducir tamaño» no existe: B ya va al mínimo de 5 acc; solo cabe no armar.

## 3. Protocolo común
- Universo: G0 de passT ETH/SOL/XRP 5m (BTC DATA_BLOCKED). Base: G0∧GEO6 (brazo thru1); toda Δ es INCREMENTAL sobre la base y también se da
  sobre G0; descriptivo sobre G0∧GEO6∧DB1. Orden fijo de la cartera: base → H-ONE → H-EXIT → H-TOP, cada Δ sobre lo que deja la anterior.
- Métricas: Δ € y EV ponderado por € (Σpnl/Σcoste) del conjunto conservado; IC90 por cierre (bootstrap de clusters 'fin' entre monedas, 5.000);
  días positivos; sin los 2 mejores días; desagregado moneda × L (ninguna celda decide); desenlace oficial con cobertura declarada (~100 %).
- HOLD: forward desde 10-Nov, >=10 días válidos (horas sanas tx_ws >= 0,95 de thru1; huecos >60 s excluyen la HORA, no el día; día válido con
  >=12 h sanas), decidido sin mirar PnL. Checkpoints a 10 y 20 días. n >= 150 rellenos afectados por regla.
- Multiplicidad: 3 primarias (H-EXIT, H-ONE, H-TOP) → α = 0,05/3. H-NIVEL exploratoria.
- Veredictos: CANDIDATE (todo pasa) → statistical-validator + red-team; INSUFFICIENT (n o días); REJECTED (Δ <= 0 o <= placebo).
  B_VIABLE solo si el conjunto conservado da EV/€ > 0 con IC90 por días > 0 (criterio aparte; NO esperado con estas piezas solas).

## 4. Qué mide distinto el simulador (puede sesgar la conclusión L2 y estas pruebas)
a) D/S cuentan los estáticos (ya cumplidos en t_dec) como evitados: mezcla filtro de colocación (GEO6) con carrera e infla la cobertura.
b) Placebo uniforme por día, no estratificado por L: el EV cambia mucho con L (acierto 5-19 %); aquí se estratifica por día×L.
c) Cancelar sin reponer: si la política real re-arma, los añadidos de GEO6 fueron <0 (H-TOX-3): la Δ por quita sería optimista; por eso
   H-ONE/H-TOP fijan «no re-armar» como política y no como cota.
d) Validez L2 de 03/04-Nov (146 «sin eventos» el 03): si los huecos coinciden con volatilidad, la muestra válida es más tranquila.
e) Dos relojes: tf es recepción de sa_ms; t_trig de L2 es recepción de libro5 (desfase conocido ~40-60 ms): a Λ 30-60 ms decide la carrera.
   H-EXIT/H-ONE primarias usan solo sa_ms (mismo reloj que tf).
f) 31 % de rellenos de passT sin reducción del nivel L en ±1,5 s en L2: posibles rellenos sin respaldo (optimismo del modelo de relleno)
   o barridos; las clases «sin toque» se informan aparte.
g) Bids >0,40 invisibles en b40 (irrelevante para L <= 0,19); en libro5_bajos (PMAX 0,20) el mejor bid es ciego para L >= 0,16: no usarlo
   para t_top.

## 5. Dependencias (las resuelve otro especialista DESPUÉS)
(i) Circularidad: la base reutiliza los rellenos de passT; L2 solo prueba trazabilidad. Contraste obligatorio antes de proponer nada real:
    ledger real de B 20-26-Oct (on-chain por order_hash): signo de Δ_exit en rápidas reales y primero-vs-resto real (n pequeño: solo signo);
    on-chain 08-10-Nov para ver si las «rápidas» de passT son consumo real del nivel.
(ii) Reloj L2: 69 % de rellenos con reducción en ±1,5 s, 47 % de esos a <=50 ms, resolución Λ 15-30 ms. Afecta a H-TOP; no a las primarias.
(iii) Mecánica del exchange sin verificar (solo documentación, nunca órdenes): casado cruzado complementario (comprar el complementario casa
    contra pujas del barato por mint), mínimo 1 $ en ventas marketable, feeSchedule del día, retraso del tomador ~145 ms.

## 6. Plan y coste
1) statistical-validator revisa y congela (o se acepta el sha de este fichero) antes de cualquier dato >=10-Nov.
2) execution-engineer: arnés etapa 0 de H-EXIT + H-ONE (<=20 min CPU; fuera de 06:00-09:30Z, load5 < 4, nice 19, ulimit 3 GB).
3) Si H-EXIT pasa la etapa 0: evaluación diaria tras el RT_ del cron thru1. 4) H-TOP con rasgos L2. 5) H-NIVEL al Frente 3.
Economía honesta: en TRAIN las tres piezas reducen la pérdida simulada (orden de +15-30 €/día a escala G0) pero no llevan B a EV>0;
el hueco a 200 k€ sigue >= 164 k€.
