# Validación independiente 19-Oct-2026 (~06:40Z) — V4 OOS, H5M población maker, H43 R5K

Solo lectura. Código propio en esta carpeta (v4_valida.py, v4_mecanismo.py, v4_fill.py, v4_extra.py, h5m_unidades.py,
h5m_fills.py, h5m_dias.py, h5m_regimen.py, r5k.py, r5k_stats.py). Intermedios en el scratchpad de la sesión
(`/tmp/claude-0/-root-polymarket-research/ce552a77-92f9-49c1-8c13-d01ef139d7f6/scratchpad/`: kmap_*.txt, fills_*.csv.gz,
F_all.pkl, U_all.pkl, R5K_U.pkl). Nada pesado: 1 proceso a la vez, nice 19, ionice idle, ulimit -v 1,5-3 GB.
Etiquetas: REJECTED / EXPLORATORY / PROMISING. Ninguna autoriza dinero.

## 1. V4 OOS (vigia_5m_barato_forward)

Fuente: `/root/polymarket-research-datalogs/vigia_5m_barato/eventos_2026-10-05..18.csv` (regla B1_5m, es_primero=1,
t_deteccion >= 06-Oct 12:00Z) + desenlaces oficiales `maker_ms_desenlaces_cache.json` (cobertura 58/58). Unidad = señal
(1 por mercado 5m y cierre); ejecutable = L215_acciones > 0; PnL = acc·(gana − p − fee(p)), fee = 0,07·p(1−p).
EV = Σpnl/Σcoste (ya ponderado por €).

REPRODUCIDO EXACTO: 58 señales, 25 ejecutables, PnL +15,756, coste 56,975, EV +0,2765, IC90 días (−0,358, +1,052)
(vigía −0,356/+1,046), sin mejor día +0,0129, 95,6 % del PnL en el 10-Oct, EV media de cocientes por señal +0,219.
13 días calendario 06-18 Oct; 12 con alguna ejecución (el 08-Oct tiene 2 señales y 0 ejecutables).

| Medida | Valor |
|---|---|
| EV sin la MEJOR operación (BTC Up a 0,12, +15,87 €) | **−0,002** (PnL −0,11 €) |
| EV sin las 2 mejores operaciones (+ BTC Up 0,14 del 17-Oct, +12,17 €) | **−0,234** |
| EV sin el mejor día (10-Oct) / sin 2 mejores días (10 y 17-Oct) / sin 3 (+07-Oct) | +0,013 / **−0,253** / −0,399 |
| IC90 bootstrap por días (n=12) / por cierre (n=24) | (−0,358, +1,052) / (−0,336, +1,025) |
| IC90 por cierre sin la mejor operación | (−0,467, +0,556) |
| ROI diario: media / sd / t | +0,398 / 1,713 / 0,81 |
| Aciertos ejecutables | 10/25 (40 %), precio medio de entrada 0,397 -> acierto = precio |
| Test nulo MC (P(gana)=precio): P(PnL >= +15,76) | 0,148 (p5-p95 del PnL nulo: −27 a +31 €) |

Por día (cierre UTC, n ejecutadas, PnL): 06 (1,+1,92) 07 (2,+4,83) 09 (3,−7,80) 10 (2,+15,06) 11 (2,−4,31) 12 (4,+0,95)
13 (1,−1,98) 14 (1,+1,82) 15 (1,−2,12) 16 (2,+2,26) 17 (3,+12,65) 18 (3,−7,51). 7/12 días positivos, pero sin los dos
días 10 y 17 el resto suma −11,95 € sobre 47,2 € arriesgados (EV −0,253).
Por moneda: BTC 12 ops +28,81 (EV +1,005, concentrado en 2 operaciones); BNB 4 −6,70; ETH 2 −5,02; SOL 1 −2,74; XRP 1 −2,84;
DOGE 5 +4,24. Sin BTC: −0,461. Por lado: Up 13 ops +21,5 (EV +0,70), Down 12 ops −5,8 (EV −0,22).
Por precio de entrada: <0,20 6 ops, 2 aciertos, +20,85 €; 0,20-0,60 17 ops, −8,8 €; >0,60 2 ops +3,7.
Los dos aciertos <0,20: P(>=2 de 6 | acierto = precio) = 0,137 (no significativo; bajo la cota bid15 sería 0,49).
Latencia: L150 +0,415 (n=31) -> L215 +0,277 (25) -> L250 +0,062 (22) -> L275 +0,021 (23) -> L300 +0,098 (24): la curva
cae hacia 0 con +35-60 ms de retraso (red team del propio vigía: lat_+35 ms = +0,06).

HALLAZGO NUEVO (la parte que NO es suerte de un día, y que explica por qué el ejecutable no cobra): el mecanismo existe en
las 58 señales pero NO en las 25 que llegamos a ejecutar.
- Las 58 señales (sin condicionar a relleno): acierto del lado s 36/58 = 62,1 % frente a ask_t0 medio 0,422 y cota bid15
  media 0,523 (z vs ask ≈ +3,0; vs bid15 ≈ +1,5). PnL "de papel" al ask_t0, 2 € por señal: +95,96 € (EV +0,83), +65,7 € sin
  las 2 mejores. Es coherente con "bid15(s) es cota inferior de P(s en 5m)".
- Pero las 33 señales NO ejecutables a 215 ms (17 "cancelado o repreciado", 16 "consumido") ganan 26/33 = **78,8 %**, y las
  25 ejecutables ganan 10/25 = **40,0 %** (Fisher dos colas p = 0,0033). El ask que sobrevive 215 ms es el que el mercado
  ya había descontado: selección adversa de relleno (misma historia que "rellenarse más barato es mala noticia": el
  precio de relleno L215 es de media −0,046 inferior al ask_t0). El EV ejecutable +0,28 es, por tanto, 1 operación.
- 18-Oct: 3 señales, 3 ejecutadas, 3 pérdidas (DOGE Up 0,50, BNB Down 0,42, SOL Down 0,53): −7,51 €; es el día que más baja
  el acumulado (+23,27 -> +15,76) y confirma el DRIFT que ya avisaba el vigía el 15-16-Oct.
- Gates: G1 (n>=40 ejecutables) 25/40, a ~1,9 ejecutables/día faltan ~8 días; G4, G6, G7 (sin BTC) en rojo.

Sesgos/flaws: (a) 25 ops ≈ 24 cierres independientes, el IC cubre 0 con holgura; (b) PnL = 1 operación; (c) descontando
una sola operación el EV es −0,002; (d) "fill" es una simulación sobre el libro (L215) y la selección adversa de fill ya
se ve en los datos; (e) 12 días calendario pero mucha concentración temporal (10 y 17-Oct).
Reparación mínima: no tocar el vigía; añadir al informe EV sin la mejor operación y acierto ejecutables vs no ejecutables
(Fisher) como diagnóstico por separado (fuera del fichero hasheado); decisión sobre V4 solo con n>=40 ejecutables.
**Etiqueta: EXPLORATORY.** Evidencia de una ventaja de señal (62 % vs 42 %) pero NINGUNA evidencia de ventaja capturable a
215 ms (ejecutables = precio; todo el PnL = 1 operación). Si las próximas ~15 ejecutables siguen en acierto <= precio,
pasar a REJECTED como estrategia tomadora a 215 ms.

## 2. H5M población maker (vigia_5m_barato_maker_forward)

Fuente: caches del vigía `/root/polymarket-research-datalogs/vigia_5m_barato_maker/unidades_2026-10-09..18.csv.gz`
(unidad = mercado-lado; 20.078 unidades, 10 días) y, a nivel de relleno (1.483.186 rellenos de la celda pc (0,10-0,30],
T (60-300]), `h5m_cola_sim/quien_gana_rellenos_v2_09..13` + mi extracción on-chain de 14..18 con la misma lógica de
`unidades_dia` (m5_onchain + filas k; cobertura de desenlace 100 %; reproduce PnL y coste del vigía al céntimo en los 5
días 14-18; 09-13 difiere en <=3 unidades/día por el borde pc = 0,10 redondeado). Unidades = (mercado, lado
comprado): no son órdenes ni fills nuestros; coste medio por unidad ~150 $ (es la caja de TODOS los makers).

REPRODUCIDO: vigía media-de-días de EV por unidad 0,1210 IC90 (0,0838, 0,1519) [el log da 0,1210 (0,0849, 0,1521)].

La trampa del 17-Oct se repite y es mayor con 10 días. Tabla por día (media de cocientes = lo que usa el vigía; ponderado por
€ = Σpnl/Σcoste; primeras 5 acciones del mercado-lado por orden de llegada, como `auditoria_17oct/metrica.py`):

| Día | unidades | EV media (vigía) | EV ponderado € | 1as 5 acc media | 1as 5 acc ponderado | acierto unid. |
|---|---|---|---|---|---|---|
| 09-Oct | 2117 | +0,132 | −0,019 | +0,023 | +0,006 | 25,7 % |
| 10 | 2027 | +0,166 | +0,066 | +0,071 | +0,042 | 26,3 % |
| 11 | 2013 | +0,151 | +0,063 | +0,059 | +0,031 | 26,0 % |
| 12 | 2040 | +0,156 | +0,065 | +0,042 | +0,009 | 25,7 % |
| 13 | 2023 | +0,047 | +0,063 | −0,043 | −0,054 | 23,8 % |
| 14 | 2063 | +0,151 | +0,135 | +0,038 | +0,040 | 26,5 % |
| 15 | 2021 | +0,153 | +0,197 | +0,034 | +0,014 | 26,0 % |
| 16 | 2017 | +0,184 | +0,018 | +0,077 | +0,059 | 27,3 % |
| 17 | 1879 | +0,113 | **−0,060** | +0,030 | −0,007 | 25,2 % |
| 18 | 1874 | **−0,042** | **−0,175** | **−0,126** | **−0,116** | 22,3 % |

Agregado 10 días (n = 20.078 unidades; fuente: caches del vigía y mis rellenos):
- Media de cocientes (vigía): +0,121, IC90 días (+0,084, +0,152).
- **Ponderado por € (Σpnl/Σcoste): +0,040**, IC90 por días (−0,012, +0,087); por cierre (n=2.880) (−0,012, +0,095). Media de
  días del EV ponderado +0,035 (−0,017, +0,085). El IC cruza 0.
- **Primeras 5 acciones: +0,003**, IC90 por días (−0,023, +0,026); por cierre (−0,021, +0,026). Media de cocientes de 1as 5
  acc: +0,021 (−0,012, +0,048). Es decir, el maker pequeño que llegase al principio de la cola no gana nada.
- Concentración: BTC es el 86-90 % del coste cada día (unidades enormes: hasta ~1.500 $ por unidad); EV ponderado por moneda
  (10 días): ETH +0,123, BNB +0,091, SOL +0,055, BTC +0,034, DOGE −0,025, XRP −0,069. La media de cocientes (BTC +0,189,
  ETH +0,177, SOL +0,142, DOGE +0,079, BNB +0,062, XRP +0,045) da un orden distinto: la "confirmación" depende de qué
  unidades pesen.
- Sin el 18-Oct: media-vigía +0,139 (0,116, 0,158); ponderado +0,059 (0,021, 0,099); 1as 5 acc ponderado +0,015.
La puerta G2 del vigía (EV >= 0,05) se cumple solo con la media de cocientes; ponderado por € el EV es +0,040 < 0,05 y
primeras 5 acc ≈ 0. «CONFIRMADA» describe a la población agregada de makers por unidad, no a un maker pequeño con cola.

**¿El 18-Oct es ruptura o ruido?** Es un valor atípico fuerte, pero un día no demuestra un cambio de régimen.
- Contra los otros 9 días (media-vigía +0,139, sd entre días 0,040): z = −4,5; ponderado z = −3,0. Bootstrap por cierre
  (clusters de 5 min), 18-Oct vs resto: diferencia de media −0,181, IC90 (−0,269, −0,096), P(dif>=0) = 0,0003;
  ponderado −0,235, IC90 (−0,399, −0,072), P = 0,007. El EV medio del propio día es −0,042 ± 0,049 (SE por cierre).
  Acierto de unidades 22,3 % (el rango 23,8-27,3 % los otros 9 días) con el mismo precio ponderado (0,204): menos aciertos
  a igual precio, no precios distintos.
- Es general, no de un rincón: en media de cocientes caen BNB −0,14, DOGE −0,23, XRP −0,20 (vs +0,07/+0,11/+0,09 el resto)
  y bajan BTC (+0,107 vs +0,197), ETH (+0,043 vs +0,191), SOL (+0,043 vs +0,152); ponderado solo ETH queda >0; por hora UTC (bloques de 4 h, media/pond): 00-04h
  −0,09/−0,32, 04-08h −0,22/−0,53, 20-24h −0,22/−0,29 negativos; 08-12h +0,14/+0,27 y 12-16h +0,04 positivos; lado NO −0,12,
  YES +0,035. No hay un régimen de tendencia evidente: % de mercados 5m Up 51,2 % (otros días 46-52 %), persistencia
  BTC P(igual al anterior) 45 %. Las horas 21-07 UTC y los activos baratos/de menor liquidez (BNB, DOGE, XRP) concentran la
  caída, pero con ~70-80 unidades por hora y moneda no se debe leer más (descriptivo, post hoc).
- Tendencia previa: 0,184 (16) -> 0,113 (17) -> −0,042 (18) en media; ponderado +0,018 -> −0,060 -> −0,175; primeras 5 acc
  cada vez más cerca de 0. Dos días consecutivos ponderados negativos más el 09-Oct (−0,019). Eso es lo que se llama "desgaste"
  o "ruido grande día a día": n=10 días no distingue. 13-Oct (+0,047) fue un precedente a −2,3 sd.
- Regla propuesta (falsable, sin tocar el vigía congelado): si 19-21-Oct juntos (3 días, ~6.000 unidades) dan media-vigía
  <= +0,05 o EV ponderado <= 0 con IC90 por cierre que no excluye 0, tratar el 18 como inicio de ruptura y pasar a EXPLORATORY
  declarado (hoy G3 sale ✅ pero "ningún día >40 %" mide PnL positivo concentrado, no signo).
**Etiqueta: EXPLORATORY** para la población (positiva en media-de-cocientes, ≈ +0,04 ponderado, no distinguible de 0
por IC) y **REJECTED como evidencia de ventaja capturable para un maker pequeño** (1as 5 acc +0,003, IC (−0,023, +0,026)).
Reparación mínima: que el vigía reporte además Σpnl/Σcoste por día con IC por cierre y 1as 5 acc (nuevo script fuera
del fichero hasheado); cualquier gate de pasar a dinero usa solo 1as 5 acc / cola real.

## 3. H43 R5K forward (vigia_5m_barato_r5k)

Fuente: log del vigía (1 día: 17-Oct, 61 unidades, 552 $, EV −0,275, IC90 cierre (−0,634, +0,119)); reproducción propia
con rellenos on-chain (mismo universo y K=50 acc tras 5.000 acc acumuladas, T (60-270], BTC, precio y desenlace reales):
17-Oct = 61 unidades, 549 $, **−0,272** (vigía 61, 552, −0,275: reproduce; diferencia = orden de empate en ts).
**El 18-Oct aún no está en el log del vigía (cron 09:30Z); mi reconstrucción da 69 unidades, 648 $, −0,306** (NO es
cifra del vigía, hay que confrontarla cuando salga).
- Por día (EV ponderado por €, unidades): 09 −0,117 (92), 10 +0,213 (89), 11 +0,168 (71), 12 +0,157 (80), 13 +0,236 (92),
  14 +0,688 (73), 15 +0,409 (107), 16 +0,042 (84), **17 −0,272 (61), 18 −0,306 (69)**. (No he podido asociar los +0,18/+0,15/+0,63 del encargo a ningún día o
  corte reproducible; el original es 06-16 Oct, n=1.010, +0,212 (+0,102, +0,326); mi 09-16: n=688, +0,2196, IC90 cierre
  (+0,080, +0,362), IC90 días (+0,097, +0,349).)
- In-sample (09-16) frágil: sin los 2 mejores días (14 y 15-Oct) +0,113; sin top-20 unidades +0,079; sin 14 y 15 n=508.
  Selección: la regla salió de mirar 24 combinaciones offset×K en 11 días. Nulo (acierto = precio, 688 unidades):
  sd 0,08, p95 +0,133; el +0,22 observado es z = 2,75 para UNA celda; "la mejor de 24" (correlacionadas, ≈5 independientes)
  espera un máximo de ~+0,10 por azar. Maldición del ganador: una parte del +0,22 es esperada por puro azar.
- Compatibilidad del forward con el in-sample (SE por cierre; unidades por cierre ≈1,0, deff 0,97):
  | | n | EV pond | IC90 cierre | P(EV_fw <= obs \| verdad +0,2) | verdad +0,1 | verdad 0 |
  |---|---|---|---|---|---|---|
  | solo 17-Oct (lo que ve el vigía) | 61 | −0,272 | (−0,633, +0,106) | **0,020** | 0,052 | 0,117 |
  | 17+18-Oct (mi reconstrucción) | 130 | −0,290 | (−0,539, −0,023) | **0,0008** | 0,006 | 0,031 |
  Forward − in-sample: −0,51, IC90 (−0,80, −0,21), P(dif>=0) = 0,003 (17+18) y 0,024 (solo 17).
  Con solo 1 día (61 unidades) el resultado es incómodo para +0,2 (z ≈ −2,1) pero NO distingue de 0 ni de +0,1: compatible
  con "mucha suerte negativa" + maldición del ganador. Con 2 días (130 unidades) ya es difícil de reconciliar con +0,2 (p ≈ 0,001)
  y con +0,1 (p ≈ 0,006); sigue sin ser inconsistente con 0 (p = 0,03 una cola).
- Dependencia: R5K es un subconjunto BTC de la población H5M; el 18-Oct también es el día malo de H5M (BTC ponderado −0,19):
  no son dos confirmaciones independientes sino un mismo mal día de compras baratas.
- **Potencia** (σ por unidad del EV ponderado = 2,19 sobre 818 unidades; ~82 unidades/día): para distinguir +0,20 de 0
  (una cola 5 %, potencia 80 %) hacen falta **~745 unidades ≈ 9 días**; potencia 50 %: ~330 unidades ≈ 4 días. Para +0,15:
  ~1.320 (16 días); para +0,10 (un valor más realista tras la maldición del ganador): ~2.980 (36 días). Con la dispersión
  ENTRE DÍAS (sd 0,30) el criterio por días necesita ~14 días para +0,2 y ~57 para +0,1. El criterio congelado (n>=40,
  >=10 días) llegaría con n≈800: suficiente solo si el efecto real fuese >=+0,2. Las 40 unidades de n_min no son una prueba
  de nada con σ = 2,2/unidad (SE ≈ 0,35).
**Etiqueta: EXPLORATORY** (formalmente EN CURSO: 1/10 días; no REJECTED aún porque el criterio exige >=10 días). Inclinación
honesta: sin apoyo; si el vigía confirma el 18-Oct ≈ −0,3, el EV conjunto cae a ~−0,29 y el criterio de refutación
(IC90 por cierre cruza 0, EV<+0,05) quedará cumplido en el instante que llegue a 40 unidades/10 días con ese ritmo. No
invertir esfuerzo de micro-órdenes en H43 antes de la lectura del 09:30Z.

## Verificación de los puntos pedidos
- ¿Algo que no sea suerte de un día en V4? Sí, la señal (62 % de acierto en las 58 vs 42 % de precio) pero no el
  ejecutable: 25 ejecutables = precio, el PnL entero es una operación y el relleno a 215 ms está sesgado contra nosotros
  (Fisher p = 0,003). Resolver eso (capturar la señal sin esperar 215 ms) es la pregunta real, no el EV agregado.
- H5M: la confirmación depende de la métrica; ponderado +0,040 (IC cruza 0), primeras 5 acc +0,003; 18-Oct atípico a ~3-4
  errores estándar, causa no identificada, sin régimen de mercado evidente.
- H43: día 1 compatible con 0 y con +0,1, poco con +0,2; con el 18-Oct (reconstrucción) incompatible con +0,2.
Salvedad transversal: todas las cifras de 18-Oct de R5K y las de H5M a nivel relleno son reconstrucción propia a partir de
on-chain (mismas reglas), no del vigía; las diferencias con el vigía están <=0,003 en EV (R5K 17-Oct) y exactas en PnL (H5M 14-18).
