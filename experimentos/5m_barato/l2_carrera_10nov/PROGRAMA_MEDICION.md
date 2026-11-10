# PROGRAMA DE MEDICION B maker 5m barato (10-Nov-2026). DISENO, 0 ordenes, sin commit. No calibra nada sobre datos que no valen.
Lee: DISENO_V2, INTEGRIDAD_V2, AUDITORIA_CRUZADA_V2, verif_real/TESTS_BARATOS + memorias sonda 03/05-Nov. Estado sonda real: ultimo output real 05-Nov, sin screen viva hoy, presupuesto restante NO comprobado (era ~0,66 $ con tope 3,40 $; asumo ~0). Sonda PASIVA (datalogs/sonda1/pasivo) sigue escribiendo hasta 10-Nov.

## 0. Principio
Unidad de decision = COLOCACION (token, ventana, nivel, instante t). Cada politica se mide por EV incondicional = Σpnl/Σcoste sobre TODAS las colocaciones (sin relleno = 0 pnl, coste solo de lo rellenado), ponderado por €, IC90 por DIAS, sin 2 mejores dias, placebo a igual cobertura estratificado dia×L, rebate 0 y 0,2. Nada que dependa solo de rellenos (censurado).

## 1. Variables que faltan -> instrumento
| Variable | Hoy | Como obtenerla | Instrumento / coste |
|---|---|---|---|
| Rellenos «solo nuestra orden» (59 % de reales; tx de 1 maker, sin print ajeno) | inobservable sin nuestra presencia | NO se puede simular sin ancla: modelarlos como P(consumo del nivel | nivel en el bid, tamano tomador) y calibrar SOLO con ordenes reales; reportar siempre por separado «con evento / sin evento» | sonda real (unico). Sin ella el simulador tiene techo de recall ~0,4-0,5 |
| Posicion real en cola | ordenes_b.cola = profundidad al armar, no posicion | user-WS (registro cancelacion ya existe) + tamano consumido en el nivel antes de nuestro relleno (L2 b40 + on-chain order_hash) | sonda real + L2 |
| Latencia cancelacion propia vs llegada | RTT cancel ~50-65 ms medido; carrera vs llegada del tomador NO medida con anclas (C2 del registro fallo 04-Nov, fix Q3b sin relanzar) | registro de cancelacion (sonda ampliada) + medidor FOK 0,01 a coste ~0 (no construido) | real: coste ≈0 $ (FOK a 0,01) pero requiere code-review + OK Javi |
| P(relleno) por token-ventana y nivel | solo por orden-instancia (5,3 %, endogena al repeg) y solo bid-1/-2, 06-19Z, sin BTC | colocaciones pasivas ESCALONADAS Y DE VIDA FIJA (no repeg) en niveles variados: da positividad que el ledger no tiene | sonda real y/o simulador sobre g0_segs (todas las colocaciones) tras validar |
| Tamano del tomador | no esta en el ledger | on-chain por tx: suma acc del token en el tx (T1 lo hizo para 202); extender a 08-10-Nov (on-chain NO independiente de passT: usa cinta chain) | datos existentes, barato |
| Bloqueos por saldo (804) y 37 post_rechazada | sin moneda/nivel/oid | anadir slug/L/oid al evento bloqueo_suelo_saldo (cambio de logging en sonda, no toca ordenes) | trivial, pero es edicion de codigo de sonda: revisar |
| Complementario FAK (H-EXIT) | cruce mint/merge no confirmado por doc; nunca ejecutado | (a) replay del ask complementario en sa_ms (existe); (b) prueba real minima: FAK 5 acc en complementario caro (≈0,88) en un caso real | (a) gratis; (b) ≈4-5 $ de nocional, perdida esperada ≲0,1 $, requiere OK Javi + code-review |
| Dia / regimen | 4 dias reales (20-23 Oct), HOLD limpio desde 10-Nov | acumular dias con logging pasivo L2+ms+on-chain | tiempo |

## 2. Simulador virtual sobre L2 (para volumen)
Reproduce: (i) P(relleno) por colocacion, (ii) EV incondicional por colocacion, (iii) distribucion de vida/instante de relleno (para H-EXIT/H-TOP: reloj).
Entradas: libro5_b40 (L2 completo solo 05-09 Nov; 10-Nov en adelante crece), ms_D sa_ms (reloj recepcion), cinta WS LIMPIA (restando nuestro share, WSXS), on-chain solo para tamano del tomador.
Modelo de relleno en 3 clases explicitas: A) consumo observable (print ajeno a precio<=L), B) consumo «solo nuestra orden» (no observable: P estimada del hazard de L1-drop + tamano de nivel; incierto, etiquetado), C) cola (motor).
Criterio de CALIBRADO (todos necesarios, sobre ordenes reales de DIAS NO usados para ajustar):
1. Mismos dias: motor y ledger real con L2 completo. HOY HAY CERO DIAS COMUNES (real 20-23 Oct; L2 b40 desde 03-Nov). Bloqueante: solo se cierra con ordenes reales >= 03-Nov (>=5 dias) o con L2 de 20-23 Oct (no existe, no reconstruible).
2. Recall >= 0,70 y precision >= 0,80 por (token,L,ventana) con la cinta limpia (hoy 0,36/0,89 y 0,48 OPT).
3. EV incondicional sim vs real, diferencia por dia con IC90 por dias que contenga 0 y |dif media| <= 0,03 €/€.
4. P(relleno) calibrada: pendiente de calibracion en [0,7;1,3] por tercil de L, y por clase A/B.
5. Placebo: invertir el orden de las ventanas (token-ventana mezclada) debe dar P(relleno) ≈ 0.
Hasta cumplirlo: el simulador solo sirve para DESCARTAR (cotas optimistas), nunca para confirmar. Es honesto decir que con el 59 % no observable puede NO llegar a calibrarse; en ese caso la unica via es sonda real con n suficiente.

## 3. Hipotesis prerregistrables (politica completa). Plantilla comun
Rasgos solo <=t (recepcion; NaN-si-vacio prohibido: indicador explicito y chequear |P(y|NaN)-P(y)|<2 pp). Placebo: misma cobertura por dia×L (5.000 perm.). TRAIN: dias quemados 26-Oct..09-Nov SOLO para fijar parametros (declarado); HOLD >=10-Nov, dias DISTINTOS, no tocar tras verlos. Gate comun: EV incondicional ponderado por € > 0, IC90 por dias > 0, sin 2 mejores dias > 0, >= 10 dias validos, >= 40 rellenos afectados (>=150 si es una regla de quita), α=0,05/k con k = nº de hipotesis primarias declaradas (aqui 6 -> 0,0083).
| ID | Regla exacta (colocacion) | Datos | Cobertura objetivo | Coste prueba |
|---|---|---|---|---|
| N1 H-NIVEL oportunidad | Armar solo celdas (moneda, L en rejilla 0,03, hora-bloque 6 h, T restante) cuya P̂(gana|relleno) calibrada en TRAIN >= L + comision efectiva(0,07·L(1−L)·0, maker=0; rebate 0) + 0,02, con n_TRAIN>=30 por celda; todo lo demas no se arma | descriptivo en g0 (+ledger para soporte bid-1/2) | 20-40 % de colocaciones | datos existentes (sim), pero el EV real exige sonda: P(relleno) fuera de soporte no existe |
| N2 Moneda BTC | Misma N1 en BTC (DATA_BLOCKED en passT: sin L2 BTC util). Primero medir en pasivo cuantas colocaciones/ventana hay y P(relleno)>0 | L2 10-Nov+ | n/d | datos nuevos (dias) |
| N3 Niveles profundos (0,05-0,09 y 0,20-0,29 pegados) y horas 00-05Z/20-23Z | Ofertas pasivas de vida fija (>=30 s, sin repeg) en nivel d ticks bajo bid, d∈{1,2,4,6}; sin relleno hoy en ledger (0 ordenes en esas horas/niveles) => solo medible con pasivo+sim o sonda | pasivo, g0_segs | por celda | sim: gratis; real: 1 orden/celda |
| N4 Tamano | q ∈ {5, 10} acc (min 5; la rejilla de ledger usa 6-10 si L<0,20): efecto de tamano en P(relleno) y AS | sonda real | n/d | real: ×2 coste por orden |
| E1 H-ONE (ficha por token-ventana) | primer relleno cancela el resto y no re-arma; Λ=150 ms (30-60 irresoluble: tf=print−63 ms constante) | RT_ 15 dias + HOLD | 45 % de rellenos G0∧GEO6 afectados | segundos; INTEGRIDAD: solo etapa 0 |
| E2 H-TOP | cancelar en t_top+Λ si score>=θ; solo M>=150 ms (BLOQUEADA a ms); precondicion AUC>=0,60 en VAL 08-09 Nov | b40 03-09 Nov | <=30 % | rasgos 2 min/dia; expectativa baja |
| X1 H-EXIT | tras relleno con 150 ms <= M <= 1.500 ms: FAK compra del complementario con limite 1−(b_tf−0,01); resolucion par; margen ~1 c, sensibilidad a tick/redondeo | F_*.pkl 03/04/07 (+0,054/acc, n=147: quemados, no confirmatorio) + etapa 0 en 26-Oct..02-Nov + 08/09 Nov; forward; FAK real minima antes de nada | rapidas ≈22-30 % de rellenos | sim gratis; real 4-5 $ nocional (OK Javi) |
Orden de evaluacion (cada Δ incremental): N1 -> E1 -> X1 -> E2; N2-N4 solo definen el soporte para medir (colocaciones, no veto).
Kill-switch de prerregistro: si TRAIN da Δ <= placebo o <10/15 dias positivos, se cierra antes del HOLD.

## 4. Secuencia y presupuesto
Paso 0 (gratis, datos existentes, hoy): (a) logging: slug/L/oid en bloqueos; (b) contar makers/tx y tamano de tomador para 08-10 Nov; (c) construir EV INCONDICIONAL de G0 sobre g0_segs por (moneda,L,hora,T) con sin-respaldo-L2 aparte; (d) etapa 0 de E1 y X1 (replay); fuera de 06-09:30Z, nice 19, ulimit 3 GB.
Paso 1 (gratis, tiempo): dejar el pasivo (L2+ms+on-chain) acumular HOLD >= 10-Nov incluyendo BTC y 00-05Z/20-23Z; 10 dias para primer checkpoint = 20-Nov, 20 dias = 30-Nov.
Paso 2 (sonda real, decision Javi): anclas para calibrar simulador y medir P(relleno) por celda fuera de soporte. Diseno: ordenes pasivas de vida fija, 5 acc, celdas N3 con ≤1 orden activa por (token,celda). Presupuesto: capital de trabajo ≈6-8 $ (5 vivas × ≈1 $, recicla en ≤5 min) + perdida esperada al EV de B (−0,06 €/€): 100 rellenos × ≈1 $ ≈ −6 $ (rango −27/+23 $ por la varianza observada). Con P(relleno) 5 % por orden: ≈2.000 ordenes por 100 rellenos; ritmo ledger 20-23 Oct = ~50 rellenos/dia con 5 vivas/3 monedas. Necesidad: ≈200 rellenos reales en ≥5 dias nuevos = capital 8 $ + perdida esperada ≈ 12 $ (techo 40 $). El presupuesto previo de sonda (≈0,66 $ + tope 3,40 $) NO alcanza: es insuficiente por un orden de magnitud; requiere recarga (regla vigente: recarga de B solo con AS resuelta y EV>0; esto es medicion, no operacion de B: decision de Javi).
Paso 3 (decision Javi): FAK real del complementario (4-5 $, 1-3 ordenes) solo si X1 pasa etapa 0.
n necesaria para detectar EV +0,05 €/€ (IC90 por dias >0, una cola):
- Escala B real (ledger: coste ≈55 €/dia, pnl diario −21..+14 €, sd diaria ≈15,6 € -> sd/€ ≈0,28): N = (1,645·0,28/0,05)² ≈ 85 dias para que el IC excluya 0 SI el EV verdadero es +0,05; con potencia 80 %: ≈270 dias. Por el IC por clusters (±0,26 con 4 dias): ≈110 dias. => NO alcanzable con dinero real a esta escala en tiempo razonable.
- Escala virtual (G0 ~200 €/dia coste en 3 monedas): sd diaria/€ desconocida; si fuera 0,15 (SUPUESTO a medir en Paso 0c): ≈24 dias (potencia 50 %) o ≈75 con potencia 80 % (z 2,93 → (2,93·0,15/0,05)² ≈ 77). Es el unico camino a n util, y depende de que el simulador se califique (§2).
Conclusion: sin simulador calibrado el gate de 10 dias solo sirve para RECHAZAR (rechazar EV≤−0,05 es barato; confirmar +0,05 no lo es).

## 5. Contribucion al hueco 200 k€ (hueco medido ≥164 k€)
Solo hay una base medida de capacidad: B real ≈55 € coste/dia (≈20 k€ turnover/ano) y G0 virtual ≈200 €/dia en 3 monedas (≈73 k€ turnover/ano, sin cola/rebate). EV neto = EV × turnover (maker sin fee, rebate no por relleno).
- Conservador: 0 € (EV ≤ 0; hoy medido −0,06 a −0,25).
- Base (si N1+E1+X1 llevaran EV a +0,03 €/€ en escala G0): ≈2 k€/ano con ≈10-30 $ de capital de trabajo.
- Optimista (EV +0,05, volumen ×5 con BTC, niveles profundos, 24 h; turnover ≈365 k€): ≈18 k€/ano, capital ≈100-300 €. Supuesto sin base medida: ×5 volumen.
Ninguna pieza cierra el hueco; B es subestrategia de ≤ ~10 % del objetivo incluso en el caso optimista. No hay base para cifras mayores.

## 6. Lo que NO se puede disenar con lo existente
1. Calibrar el simulador (cero dias comunes real-L2). Cierra: >=5 dias de ordenes reales ≥03-Nov con L2 completo.
2. Rellenos «solo nuestra orden» sin ancla propia. Cierra: sonda real con posicion en cola.
3. Soporte fuera del bid-1/-2 (niveles, BTC, 00-05Z/20-23Z, tamano, vida larga): solo sonda/pasivo.
4. Mecanica FAK/mint del complementario: prueba real minima.

## 7. ADENDA (mandato Javi 10-Nov): optimizar para explotar B sin relajar gates ni inventar cifras
Escala de referencia (unica con base medida): G0 virtual ≈270 rellenos/dia, ≈200 €/dia coste, EV TRAIN −0,245 €/€ (≈ −49 €/dia). Todo «mejor caso» es TECHO sobre dias quemados (03-07 Nov), NO confirmatorio; se reescribe con el HOLD.

### 7.1 Palancas: mejor caso defendible, desbloqueo y orden por valor/coste
| # | Palanca | Mejor caso defendible (base medida, TRAIN quemado) | Lo desbloquea | Coste prueba | Orden |
|---|---|---|---|---|---|
| 1 | Evitacion E1 H-ONE (+GEO6) | quita 45 % de rellenos GEO6-OK con −0,290 y deja −0,109 (§1 DISENO_V2): ≈ +15-30 €/dia a escala G0 junto a E2/X1 (estimacion del propio diseno) ≈ 5-11 k€/ano de perdida evitada, NO llega a EV>0 | etapa 0 en 15 dias quemados + HOLD; Λ=150 | segundos CPU, 0 € | 1 |
| 2 | Salida X1 H-EXIT | +0,054 €/acc en rapidas (n=147, 3 dias quemados) ≈ 147×5×0,054 ≈ 40 € en 3 dias ≈ 13 €/dia ≈ 5 k€/ano techo, margen ~1 c, puede ser 0 | etapa 0 en 10 dias NO vistos + FAK real minima | CPU ~15 min; real 4-5 $ | 2 |
| 3 | Colocacion N1 H-NIVEL (oportunidad) | sin cifra defendible: lentas a L 0,10/0,13 aciertan 5-6 % vs 13-19 % a 0,16/0,19 (3 dias): solo dice DONDE NO armar; como oportunidad exige P̂>L+0,02 y ninguna celda TRAIN lo cumple hoy | >=10 dias DESC + P̂ calibrada | 0 € en g0; real para P(relleno) | 3 |
| 4 | Vida/tamano (N4) y «orden >30 s» | pista Q2 sin prerregistrar: ordenes >30 s +0,23 €/€ y rellenos <1 s tras rearmar −0,35 (ledger 4 dias; vida endogena al repeg: puede ser selección) | prerregistrar YA como H-VIDA con vida FIJA exogena (no repeg) | pasivo + sonda | 4 |
| 5 | BTC, niveles profundos (N2/N3), horas 00-05Z/20-23Z | NO HAY base: 0 ordenes reales, BTC DATA_BLOCKED en passT. Valor desconocido; solo cabe medir P(relleno) y AS | L2 BTC pasivo + sonda de celdas | tiempo; real 1 orden/celda | 5 (mayor opcionalidad: es el unico que añade CAPACIDAD) |
| 6 | Evitacion E2 H-TOP | proxy 24 %→31-36 %, expectativa baja; BLOQUEADA a ms | AUC>=0,60 en VAL 08-09 Nov | 2 min/dia | 6 |
Regla de orden: valor esperado €/coste = (techo €/ano × P(pasar etapa 0) ) / coste en € y dias; E1 y X1 etapa 0 son gratis y se hacen primero; real solo si pasan. P(pasar) no se cifra (sin base): se reporta como «alta/media/baja» y se actualiza con cada etapa.

### 7.2 Acumulabilidad y camino mas corto a n
- UN solo arnés: (a) tabla de COLOCACIONES por dia (todas las g0_segs + sonda pasiva), con rasgos ≤t y version congelada; (b) cada hipotesis es una columna de decision (cancelar/mantener/salir/no armar) evaluada por el MISMO simulador y el MISMO gate; Δ incremental en orden fijo N1→E1→X1→E2. Un dia nuevo suma a TODAS a la vez (no hay pruebas separadas).
- Un solo conjunto de anclas reales sirve para calibrar P(relleno) (§2) y para validar cada regla: no se compra una sonda por hipotesis.
- Acortar dias: (i) evaluar en escala virtual (≈24-77 dias, §4) y NO real (≈85-270); (ii) puntuar por token-ventana y moneda para elevar n sin inflar dias, pero IC SIEMPRE por dias (clusters de dia, 3 monedas correladas); (iii) bajar la varianza con control: reportar Δ pareado sobre la MISMA colocacion (con/sin regla) en vez de EV absoluto: la sd de la diferencia pareada es menor que la del EV y es lo que determina los dias (medirla en Paso 0c; hoy no esta medida); (iv) dias quemados valen para fijar parametros y etapa 0, nunca para el gate.
- Checkpoint fijo 10/20 dias HOLD; decision de parada anticipada solo por REJECTED (Δ ≤ placebo), nunca por exito temprano.

### 7.3 Explotar los rellenos BUENOS (no solo vetar los toxicos)
Evidencia de separacion ex ante (todo exploratorio): primer relleno de token-ventana −0,120 (acierto 14,7 %) vs tras rapida −0,501; lentas >5 s −0,113 vs rapidas 60-1500 ms −0,415; vida >30 s +0,23 (pista); GEO6-OK lentas −0,068. NINGUN subconjunto es >0 en TRAIN: «bueno» hoy = «menos malo». Hipotesis a prerregistrar:
- B1 (selector de colocacion): condiciones ex ante ≤t para armar = nivel sin rapida previa en la ventana, gap GEO ≥0,06, vida fija ≥30 s, L con P̂>L+0,02 (N1). La accion es ARMAR (mas tamano/mas niveles) solo en esa celda; el resto no.
- B2 (tamano): subir q de 5 a 10 acc SOLO en celdas B1 con EV TRAIN>0 en ≥2/3 monedas; en caso contrario no se sube (hoy ninguna celda lo cumple).
- Comprobacion: placebo a igual cobertura estratificado dia×L×moneda (5.000 perm.), inversion (armar solo el complemento de B1 debe dar Δ<0), y prueba de que B1 no es solo «horas buenas/dia bueno»: Δ debe sostenerse sin los 2 mejores dias y en ≥7/10 dias HOLD. Gate: EV incondicional ponderado por € > 0 e IC90 por dias > 0; rebate 0 y 0,2 siempre.
- Riesgo declarado: seleccionar «buenos» por rasgos que correlacionan con resultado = multiplicidad; B1/B2 cuentan en k (k pasa de 6 a 8, α=0,05/8) y se congelan antes de HOLD.

### 7.4 Cuanto del hueco ≥164 k€ puede cerrar cada pieza (base: turnover G0 ≈73 k€/ano; ningun otro dato de capacidad)
Perdida de partida G0 ≈ −49 €/dia ≈ −18 k€/ano. Pasar a EV>0 exige primero recuperar eso.
| Pieza | Conservador | Base | Optimista |
|---|---|---|---|
| E1+E2 (evitacion) | 0 | recupera ≈ +5 k€/ano de perdida (no es beneficio) | +11 k€/ano de perdida evitada |
| X1 salida | 0 (ley del ~1 c) | ≈ +2 k€ | ≈ +5 k€ (techo del +0,054) |
| N1/B1/B2 colocacion y tamano | 0 | sin base: 0 hasta HOLD | sin base: no se cifra |
| N2/N3/horas/BTC (capacidad) | 0 | 0 | multiplica turnover (×5 es SUPUESTO sin base) si EV>0 |
| Total B | 0 € | ≈ +2 k€/ano (alineado con §5) | ≈ 18 k€/ano (§5; con ×5 y EV +0,05) |
Capital: base ≈10-30 $ de trabajo; optimista ≈100-300 €. Cierra como mucho ≈11 % del hueco en el escenario optimista; ≈1 % en base. Lo que B SOLA NO puede cerrar: ≥146 k€ de los ≥164 k€ aun en el optimista; el resto debe venir de otras subestrategias (A/precierre, 15m, wallets) o de otro regimen de capacidad que hoy no esta medido. Se disena el camino medible, no se promete el objetivo.

### 7.5 Reglas que se mantienen
0 ordenes reales en este programa; HOLD limpio ≥10-Nov (03-09 Nov solo TRAIN/etapa 0); EV incondicional ponderado por € con IC90 por dias, sin 2 mejores dias, rebate 0 y 0,2; todo envio real (sonda, FAK) = /code-review + OK final de Javi; parametros congelados con sha antes de leer HOLD.
