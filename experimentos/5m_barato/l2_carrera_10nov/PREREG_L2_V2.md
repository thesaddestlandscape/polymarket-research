# PREREG_L2_V2 — B maker 5m barato tras la carrera L2: reglas, placebo y gate CONGELADOS (10-Nov-2026 ~19:20Z)
Autor: revisión estadística independiente (QA). 0 órdenes, solo lectura, sin commit. Sustituye a los §2-§3 de DISENO_V2.md (sha 71297c9b…) y al §3/§7.3 de
PROGRAMA_MEDICION.md (sha 20a84156…) en todo lo que choque; lo que no se redefine aquí se hereda literal de esos dos ficheros y de
PREREG_Q11_THRU1_FWD.md (sha 68ca25a0…: GEO6, salud de horas). El sha de ESTE fichero va en PREREG_L2_V2.sha256 (fichero entero).
Cualquier cambio = V2.1 con sha nuevo; V2.1 solo puede reclamar como HOLD días ≥10-Nov sobre los que NINGUNA regla V2 se haya evaluado
(el evaluador escribe un log append-only `eval_log.jsonl` con ts, regla, días leídos; sin log = día quemado).

## 0. Días
- QUEMADOS (todo ≤ 2026-11-09 UTC). 03-07 Nov: TRAIN de la carrera L2 (clases M, orden en ventana, valor de salida 03/04/07 vistos).
  08-09 Nov: calculados como HOLD del estudio v1 (trg_*.pkl, analiza.py) y agregados de G0 03-09 vistos en INTEGRIDAD_V2 Q4 → NO son
  limpios: solo sirven de etapa 0 / VAL de muerte, nunca de confirmación. 26-31 Oct: TRAIN de frente 2 (salidas, otra regla).
  07-09 Nov son además forward de thru1 (otro prereg; no se tocan sus veredictos).
- HOLD: D ≥ 2026-11-10 00:00Z. Comprobado a 19:15Z del 10-Nov: no existe ningún RT_ ≥10-Nov; ninguna regla de este fichero ha leído
  datos ≥10-Nov. Ningún parámetro se elige con HOLD.
- El Paso 0 (sobre quemados, incluidos 03-07 Nov) NO puede cambiar ninguna regla congelada: solo produce el ADDENDUM A1, generado por
  código determinista (pasa/muere de cada etapa 0 y celdas ajustadas de N1/B1/E2), escrito y hasheado ANTES del primer look HOLD.

## 1. Universos, unidad y métricas (comunes)
- U1 = colocaciones G0 de passT (sha a8b9d7a0…) ETH/SOL/XRP 5m, escalera 0,10/0,13/0,16/0,19 (out/g0_segs.pkl y sus equivalentes diarios).
  U2 = colocaciones VIRTUALES (generador nuevo, mismo motor passT): niveles/horas/BTC fuera de G0. Base de U1 = G0∧GEO6
  (armar solo si bid(t−300 ms) − L ≥ 0,06).
- Unidad = COLOCACIÓN. pnl maker por acción rellenada = 1{gana} − L + rb·0,07·L(1−L), rb ∈ {0; 0,2} (ambos deben pasar; rebate por
  relleno = supuesto). Sin relleno = 0. EV_€ = Σpnl/Σcoste (coste = Σ q·L rellenado), ponderado por €; nunca media de cocientes.
- Desenlace oficial; día con cobertura de desenlace < 99 % = NO VÁLIDO.
- Día válido (decidido por código, sin PnL): horas sanas tx_ws ≥ 0,95 (thru1); hueco > 60 s excluye la HORA; ≥ 12 h sanas; L2 b40 del
  día extraído y sin fichero corrupto (stats.json); sa_ms presente. Si falta b40 de un día por rotación, el día es NO VÁLIDO (no se imputa).
- Reloj: todo rasgo ≤ t en RECEPCIÓN (sa_ms / libro5). tf = tiempo de relleno de passT (print_rx − 63 ms o caída L1 de sa_ms): NO es un
  evento observado; M = tf − t_top solo se usa en cubos ≥ 150 ms. Rasgo NaN-si-no-hay-datos = indicador explícito y se descarta si
  |P(y|NaN) − P(y)| > 2 pp en su TRAIN.
- Latencias fijadas (no medidas con anclas propias; ver §6): d_det (aviso de NUESTRO relleno) = 250 ms primaria (sens. 150/500);
  cancelación efectiva = +60 ms; retraso tomador = 175 ms (30 ida + 145).
- Estadístico primario por hipótesis h: Δ_d = PnL_d(cartera con h) − PnL_d(cartera sin h) en € por día válido, PAREADO sobre las mismas
  colocaciones, incremental en ORDEN FIJO: base → N1 → E1 → X1 → E2 → (adiciones) B1 → N3 → N2. H-VIDA en su propio universo U2-peg.
  Se reporta también Δ/Σcoste_base (€/€) y EV_€ del conjunto conservado.

## 2. Hipótesis congeladas (familia confirmatoria k = 8: N1, E1, X1, E2, B1, N3, N2, H-VIDA)
N1 (no armar fuera de oportunidad, U1). Celda = (moneda, L ∈ {0,10;0,13;0,16;0,19}, bloque UTC {00-06,06-12,12-18,18-24}, T_rem al armar
  {<120, 120-210, ≥210 s}). TRAIN = 26-Oct..09-Nov. P̂ = (aciertos+0,5)/(rellenos+1) de los rellenos G0∧GEO6 de la celda. Se arma la
  celda solo si rellenos_TRAIN ≥ 30, rellenos en ≥ 5 días distintos y P̂ ≥ L + 0,02 (comisión maker 0, rebate 0). El resto no se arma.
  Muerte en TRAIN: 0 celdas armadas, o lo no armado ≥ 85 % del coste base (veto, no filtro).
E1 (una ficha por token-ventana, U1). Al primer relleno t1 de (día, token, fin) se cancelan los demás niveles vivos de ese token y no se
  re-arma hasta el cierre. Se conservan rellenos con tf ≤ t1 + Λ, Λ = d_det + 60 = 310 ms (sens. 150 optimista, 560).
  Etapa 0 (26-Oct..09-Nov, muerte): KILL si Δ ≤ placebo de grupo aleatorio o < 10/15 días con Δ_d > 0.
X1 (salida por el complementario, U1). Relleno del barato en tf con t_top = primera cotización sa_ms en [t_arm+68 ms, tf] con mejor bid ≤ L
  y 150 ≤ M ≤ 1.500 ms → FAK de compra de q acc del complementario, límite a_lim = 1 − (b_tf − 0,01) redondeado HACIA ABAJO al tick vigente
  del complementario. Casado en t_x = tf + d_det + 175 ms; precio = libro de asks del complementario en sa_ms en t_x, recorriendo niveles ≤ a_lim;
  sin libro → espejo 1 − bid del barato en t_x; sin ninguno → no se cubre (se mantiene, cuenta como no ejecutable). Parcial permitido; el
  residuo se mantiene. Pata FAK: comisión 0,07·a·(1−a) por acción (5 decimales), rebate 0. Par a resolución.
  Δ por acción cubierta = (1 − a − fee) − 1{gana}. Sens.: d_det 150/500, −2 ticks en a, M_cut 1.000/2.000.
  Etapa 0 (26-Oct..02-Nov + 08-09 Nov; días sin sa_ms se excluyen y se declaran; < 8 días = INSUFFICIENT): Δ > 0; IC90 por cierre > 0;
  ≥ 7/10 días > 0; p placebo < 0,05/3; sin 2 mejores días > 0; ≥ 2/3 monedas > 0; tamaño ≥ q en ≥ 90 %; n ≥ 150 coberturas.
  Superarla NO autoriza nada real: FAK real solo con /code-review + OK de Javi (decisión 10-Nov).
E2 (cancelar al pasar a mejor bid, U1). Población = TODAS las transiciones a mejor bid de colocaciones G0 vivas (g0_segs). y = relleno en
  ≤ 1.500 ms tras t_top. Rasgos en t_top: f1/f2 caída del mejor bid 1 s/3 s (sa_ms), f4 nº y tamaño de prints del token 2 s (filas T b40),
  f5 tamaño en L y en [L−0,03, L) (b40), f6 T_rem, f7 L y moneda. f3 (Binance) EXCLUIDO: bnreg no existe para 03-07 Nov.
  Logística L2 C=1 (rasgos estandarizados en DESC), ajuste DESC 03-07 Nov; θ = menor umbral tal que lo cancelado contiene ≤ 30 % de los
  rellenos GEO6-OK de DESC. Acción: score ≥ θ → cancelar en t_top + 150 ms (sens. 300), no re-armar en la token-ventana; solo cuentan como
  evitados los rellenos con tf ≥ t_top + 150 ms. VAL de muerte 08-09 Nov: AUC ≥ 0,60 y Δ > placebo (p < 0,05); si no, KILL.
B1 (armar MÁS donde es bueno, adición U2). En celdas armadas por N1, con GEO6 OK, sin relleno «rápido» (150 ≤ M ≤ 1.500) previo (≤ t) en la
  token-ventana y T_rem ≥ 60 s: añadir colocaciones virtuales en los ticks intermedios de la celda (L+0,01, L+0,02), mismo tamaño G0, vida
  hasta el cierre o disparo E1. Δ = PnL de lo añadido. Si N1 muere, B1 = INSUFFICIENT.
N3 (capacidad: niveles profundos y horas, adición U2). Colocaciones a bid − d, d ∈ {1,2,4,6} ticks, con L ∈ [0,05;0,09] ∪ [0,20;0,29] a
  cualquier hora, o L ∈ [0,10;0,19] solo en 00-05Z y 20-23Z; instantes en rejilla de 30 s desde inicio+15 s mientras T_rem ≥ 60 s; vida fija
  30 s sin repeg; ≤ 1 viva por (token, d). Estadístico = PnL total de N3 (celdas solo descriptivas, no deciden).
N2 (BTC, adición). Precondición: passT + L2 BTC utilizables (comprobar en Paso 0); si no, DATA_BLOCKED (k no baja). TRAIN_N2 = los 7 primeros
  días válidos ≥ 10-Nov con BTC; algoritmo N1 idéntico ajustado solo ahí (A2 automático y hasheado); HOLD_N2 = días válidos posteriores.
H-VIDA (vida exógena fija, U2-peg, soporte del ledger: bid−1/−2, L 0,10-0,29, 06-19Z, ETH/SOL/XRP). Rejilla de instantes cada 30 s.
  F = colocación fija 30 s sin repeg; R = re-anclar a bid−d en cada cambio del mejor bid (alta 68 ms, cancelación 60 ms).
  Primario: EV_€(F) incondicional > 0 con el gate; requisito adicional: EV_€(F) − EV_€(R) > 0 (IC por días). Control: F con vida 1 s.
NO CONGELABLES SIN DINERO (DATA_BLOCKED, fuera de la familia): N4 y B2 (efecto del tamaño q=10 sobre P(relleno) y selección adversa no es
  identificable en simulación sin órdenes reales de ese tamaño). Añadirlas = V2.1 con k = 10 para todo test aún no decidido.

## 3. Placebo, inversión y controles
- Reglas de quita/salida (N1, E1, X1, E2): placebo a IGUAL cobertura (nº de unidades afectadas) estratificado día × L × moneda, 20.000 perm.
  E1 además placebo de grupo aleatorio por token-ventana. B1: añadir el mismo nº de colocaciones en celdas aleatorias (mismo estrato).
- Inversión obligatoria (si su Δ > 0, la hipótesis no es PROMISING): N1 armar solo lo vetado; E1 conservar el ÚLTIMO grupo; X1 cubrir solo
  lentas (M > 1.500); B1 añadir solo en el complemento. N3/N2/H-VIDA: sin placebo (adiciones); controles = R y F 1 s.
- Toda regla de quita con cobertura ≥ 85 % del coste base = VETO → no PROMISING aunque pase.

## 4. Gate (por hipótesis, en HOLD; looks en los 10 y 20 primeros días válidos de esa hipótesis, sin mirar PnL para validar días)
α_look = 0,05/(8·2) = 0,003125 (una cola). PROMISING exige TODO, con rb = 0 y con rb = 0,2:
G1 ΣΔ_d > 0. G2 cota inferior 1−α_look de la media de Δ_d > 0 por bootstrap de DÍAS (20.000) Y por t de Student sobre Δ_d; además IC90 por
días > 0 (reportado siempre). G3 p placebo < α_look (si aplica). G4 sin los 2 mejores días ΣΔ_d > 0. G5 ≥ 60 % de días con Δ_d > 0.
G6 ≥ 2/3 monedas con Δ > 0 (N2: no aplica). G7 n afectadas ≥ 150 (quita) / ≥ 40 rellenos (X1, B1, N3, N2, H-VIDA). G8 inversión/control
como en §3. G9 ≥ 10 días válidos. G10 en el look 10: media de Δ_d de los días 6-10 ≥ 50 % de la de los días 1-5.
REJECTED en cualquier look si ΣΔ_d ≤ 0 o Δ ≤ media del placebo. Parada anticipada solo por REJECTED; en el look 20 manda lo más conservador.
B_VIABLE (único criterio que podría justificar dinero, decisión de Javi): la cartera FIJADA en A1 (todas las piezas que pasan etapa 0/TRAIN,
fijada antes del HOLD; quitar piezas que fallen en HOLD es post-hoc y solo descriptivo) con EV_€ incondicional > 0, cota 1−α_look por días
> 0, IC90 por días > 0, sin 2 mejores días > 0, rb 0 y 0,2.
Techos de etiqueta: U1 máx. PROMISING; U2 máx. EXPLORATORY (motor sin el 59 % «solo nuestra orden», recall 0,36); DRY_RUN_VALIDATED
exige simulador calibrado (PROGRAMA §2, 5 criterios) = hoy DATA_BLOCKED. Ninguna etiqueta autoriza dinero.
Aceptación del evaluador ANTES de cualquier look (sobre quemados, ±1 €): G0 03-07 Nov n 1.350, EV −0,245; números de thru1 de su §52.

## 5. Ambigüedades corregidas respecto a DISENO_V2 / PROGRAMA
1 k = 6/8 con 11 IDs → familia exacta de 8; N4/B2 fuera. 2 «IC90» vs α/k → ambos, más reparto por 2 looks. 3 d_det no fijado y precio de
X1 en tf+250 vs tf+d_det+175 → t_x único. 4 Λ_E1 = 150 no cubría aviso+cancelación → 310 primaria. 5 X1 M > 0 → 150-1.500 (reloj).
6 E2 usaba Binance inexistente en DESC → f3 fuera. 7 N1 sin celdas ni estimador → fijados. 8 cartera elegida mirando HOLD → fijada en A1.
9 B1 era nulo tras E1 → adición. 10 H-VIDA sin regla → escrita. 11 08-09 Nov declarados semi-vistos. 12 veto ≥ 85 %.
Sin resolver (no bloquea la congelación): ledger B fin_ejecucion «ordenes 4765» vs 3.833 intencion_post (+137 abortados = 3.970) — FALTA_INFO.

## 6. Limitaciones reclasificadas
(i) Sin dinero, ahora (orden más limpio): a) preservar HOLD: comprobar que b40/RT_/ms_D ≥ 10-Nov se extraen a diario antes de la rotación
  de libro5_ms (~6 d) y que on-chain se archiva (keep_onchain cubre 26-Oct..10-Nov) — coste minutos, riesgo 0, URGENTE (pérdida irreversible);
  b) aceptación del evaluador en quemados; c) EV incondicional de G0 sobre g0_segs por (moneda, L, hora, T), con/sin respaldo L2 aparte, y sd
  de Δ_d pareado (potencia real); d) etapas 0 de E1, X1, E2 (DESC/VAL), TRAIN de N1/B1 → A1; e) tamaño del tomador y makers por tx 08-10 Nov
  on-chain (descriptivo, no independiente de passT); f) generador U2 (pasivo virtual: BTC, niveles, 00-05Z/20-23Z, bid−d vida fija) con
  aceptación «reproduce G0 si se le dan las colocaciones G0»; todos con CPU ≤ 20 min, nice 19, ulimit 3 GB, fuera de 06-09:30Z, riesgo 0.
  g) bloqueos por saldo con slug/L/oid: edición de código de B/sonda en dev; valor 0 mientras no haya órdenes → preparar al final y con review.
  h) medidor FOK a 0,01: el retraso del tomador ya está medido (07/14-Oct, 213-217 ms) y son órdenes reales → NO procede ahora.
(ii) Solo con anclas reales; vía sin dinero nuevo: d_det y latencia de cancelación propia desde sonda1/cancel_evid 03-05 Nov (user-WS ya
  registrado); modelo de precio tomador y cruce por mint de X1 con las FOK reales de PRECIERRE ≥ 03-Nov (on-chain: ¿la contraparte es puja del
  token opuesto?) contra replay sa_ms; ~79 órdenes reales de Sonda1 30-Oct..05-Nov (n mínimo, mayoría sin L2) solo para mecánica de cola.
  Calibración del simulador maker (≥ 5 días de órdenes maker reales con L2) y rellenos «solo nuestra orden»: NO hay vía sin órdenes maker
  nuevas → con la decisión de Javi (1) el programa llega como mucho a PROMISING/EXPLORATORY + B_VIABLE en simulación; demostrar EV real
  exige que Javi decida si ese nivel basta para una sonda de medición. Se declara, no se relaja.
(iii) No resolubles hoy: posición real en cola y efecto del tamaño (N4/B2); L2 de 20-23 Oct (no existe).

## 7. Entrega (≤ 20 líneas)
Congelado: este fichero (sha en PREREG_L2_V2.sha256), familia k=8 (N1, E1, X1, E2, B1, N3, N2, H-VIDA), HOLD ≥ 10-Nov, todo ≤ 09-Nov quemado.
Cambios: 12 correcciones del §5; N4/B2 DATA_BLOCKED; techos de etiqueta; cartera fija en A1; α_look 0,003125.
Orden Paso 0 (gratis): (a) preservar HOLD → (b) aceptación evaluador → (c) EV incondicional G0 + sd pareada → (d) etapas 0 E1/X1/E2 y TRAIN
N1/B1 → A1 hasheado → (e) anclas sin dinero: d_det (cancel_evid) y mint/precio tomador (PRECIERRE) → (f) tomador on-chain 08-10 →
(g) generador U2 → (h) logging de bloqueos (al final). Paso 1: acumular HOLD; looks a 10 y 20 días válidos (~20-Nov y ~30-Nov si todos válidos).
Primer especialista: cheap5m-execution-engineer (a, b, c, d, en ese orden, un agente a la vez); después data-integrity revisa A1 antes del 1.er look.
