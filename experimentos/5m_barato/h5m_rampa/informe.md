# Rampa gradual de H5M con dinero real mínimo — diseño pre-registrable (risk-economics, 19-Oct-2026 ~14:30Z)

Solo diseño. No se ha enviado nada ni se ha tocado ningún proceso, vigía ni ejecutor. Cómputo: 4 scripts ligeros (nice 19, ionice idle,
ulimit 1,5 GB) sobre el dataset de colocación ya existente. Unidades: pUSD ($), tal como salen de los ficheros. Etiqueta: **DISEÑO / EXPLORATORY**;
nada de esto autoriza dinero: cada peldaño exige `/code-review` medium + OK final de Javi.

## 0. Resumen (lo que cambia el plan)

1. **H5M no se puede escalar «copiándola»: hay que escalar el vehículo con el que la capturamos.** Unirse al bid como la población
   (JOIN/SEGUIR) da −0,050 en la cola simulada (`h5m_cola_sim/informe.txt`, 09-13 Oct, IC90 días (−0,082,−0,020)); las primeras 5 acciones
   de la población dan +0,003 (IC90 días (−0,023,+0,026)). El único vehículo con signo positivo fuera de muestra es **H35 DEEP_PEG en
   ETH k2 / SOL k1 / XRP k1**: reproducido aquí, OOS 14-16 Oct **+0,064 por €** (879 rellenos simulados, 3 días: +0,027 / +0,185 / −0,009),
   DESC 05-10 +0,084 (1.547 rellenos, 4/6 días +), más reembolso ≈ +0,011 por €. Es exactamente la política de H47. **La rampa de H5M = la
   rampa de H35-alts, y su peldaño 0 y 1 son H47-A y H47-B.** No se crea un brazo real aparte (no se duplica capital).
2. **Con la wallet dedicada tal como está, H47-B NO se completa en la mayoría de los casos.** Simulado con los rellenos reales del dataset
   (bootstrap por día y por cierre): con el suelo de 12 pUSD sobre 19,59 el presupuesto efectivo es 4,5-7,6 $ y la probabilidad de llegar a
   los ~70 rellenos es **24-44 %** aunque el EV real sea +0,077 (mediana de parada: relleno nº 14). **Y si los rellenos ganadores no se
   redimen solos, el suelo para tras ~7 rellenos con certeza** (el harness no redime; la memoria del 15-Oct dice que Polymarket «redime solo»
   tras un FOK, la del 09-Oct que hay que redimir: **sin verificar para 5m**). Para completar B con ≥90 % hacen falta ≈30 $ de presupuesto
   efectivo (≈45 pUSD de saldo con el suelo de 12) o bajar el suelo: **decisión de capital de Javi antes de B**, no después.
3. **El EV no se mide con dinero real a 5 acciones en ningún plazo razonable**: σ = 2,05 por € y relleno; con 1.000 rellenos reales
   (≈7 días, 1.020 $ rotados, σ del PnL ≈ 80 $) la cota inferior del IC90 por días supera 0 solo en el 24 % de los casos con EV real +0,077.
   Confirmar +0,064 con 80 % de potencia exige ≈9.700 rellenos (≈1 mes, σ ≈ 256 $). **Por diseño, el EV para subir de peldaño sale del
   simulador calibrado por H47 corriendo en forward sobre TODAS las decisiones (gratis, ~300 rellenos/día), y el dinero real solo tiene que
   demostrar que la ejecución real no es peor que el simulador.**
4. **Kill-switch**: el secuencial naïf (n≥20 y media acumulada <0 tras cada relleno) se dispara en falso el **74-84 %** de las veces con el
   EV bueno (prohibido). Topes catastróficos dimensionados para ≤5 % de disparo en falso con EV +0,05: 32 $ (B, 70 rellenos), 73 $
   (300 rellenos a 5 acc), 143 $ (10 acc), 354 $ (25 acc), 710 $ (50 acc). Su potencia contra un EV de −0,10 es solo 15-31 %: **acotan dinero,
   no validan nada.** La validación va por miradas pre-planificadas al final del peldaño y por el acuerdo real↔gemelo.
5. Corrección de un dato del encargo: «las 54 ganadoras on-chain +0,142 por ejecución invisible» es una **clasificación por resultado en los
   mismos 5 días** (`quien_gana_informe.txt`); fuera de muestra las «ganadoras» dan +0,076 y las «perdedoras» +0,071 (`ganadoras_persistencia_informe.txt`,
   Spearman 0,13-0,19). No es evidencia de una ejecución que podamos dimensionar; no entra en la rampa.

## 1. Qué es exactamente lo que se escala

| Pieza | Papel en la rampa | Evidencia (ponderada por €) | Fuente |
|---|---|---|---|
| H5M población (vigía congelado) | **Monitor de régimen** (condición para subir, no vehículo) | +0,040 IC90 días (−0,012,+0,087), 10 d, 20.078 u.; 18-Oct −0,175 | `validacion_19oct/informe.md`; `DL/vigia_5m_barato_maker/` |
| H44 H5M-ALT (ETH/SOL/XRP) | Monitor de régimen de las monedas de la rampa | +0,085 (+0,011,+0,145) post hoc; forward desde 19-Oct | `LIBRO_OBJETIVO_200K.md` |
| JOIN / SEGUIR (copiar H5M) | Control en el gemelo, nunca brazo real | SEGUIR −0,050 (−0,082,−0,020); CABEZA +0,005 | `DL/h5m_cola_sim/informe.txt` |
| **H35 DEEP alts** | **Vehículo** | OOS 14-16 +0,064 (879 rell.), DESC +0,084 (1.547), tasa de relleno por puja 23 % (32 % por mercado) | reproducido: `rep.py`, `chk.py` |
| H47 | Peldaños 0 y 1 (maquinaria + calibración) | 0 órdenes reales; review #1 en aplicación (dev 48e0fbd980) | `dev/experimento_maker_h47.py` |
| H45 | Decide si existen los peldaños de 25 y 50 acc | PENDING, corrida nocturna | REGISTRO H45 |

Datos del vehículo (dataset `m5_maker_colocacion/base_*.csv.gz`, 9 días, motor CONS 5 acc): coste medio por relleno 1,02 $, precio medio
0,217, acierto 23,2 %, σ del PnL 2,02 $ por relleno (2,05 por €); 293 rellenos/día y 293 $/día de coste en OOS para las 3 monedas; rellenos
por cierre: 1 (939 cierres), 2 (481), 3 (144), ≥4 (23) → **varias monedas en el mismo cierre son una apuesta correlada: IC por día/cierre**.
El `pnl` del dataset NO incluye reembolso (verificado: pnl = acciones·acierto − coste, dif 0); reembolso medio 0,0119 $ por relleno.

## 2. Peldaños

Una puja por mercado (una cara), una sola wallet (la dedicada), un único lock y un único `.KILL` (ya en H47): **todo brazo maker comparte
el mismo presupuesto de exposición y de pérdida**. Tamaño: nunca <5 acciones (mínimo del mercado) y ≥1 $ de nocional (lo dirá P0).

| Peldaño | Acc/orden | € máx/mercado | N fijo | Días mín. | Rotación esperada | PnL (EV +0,077 / 0 / −0,10) media; σ | P5 del PnL (EV 0) | Tope catastrófico (≤5 % falso con EV +0,05) | Capital que exige |
|---|---|---|---|---|---|---|---|---|---|
| **P0 = H47-A** | 5 a 0,01-0,03 | 0,15 | 40 pujas | 1 | ≈0 $ (no deben rellenarse) | ≈0 | > −1 $ | 1 $ | lo actual |
| **P1 = H47-B** | 5 (hasta 10 si 1 $ de nocional) | 1,5-3 | 230 pujas ≈ 70 rell. | 1-2 | 72 $ | +3,9 / −1,4 / −8,3; σ 19 | −32 $ | 32 $ (> saldo útil: manda el suelo) | **≈30 $ efectivos para completar con ≥90 %** (hoy 4,5-7,6) |
| **P2** | 5 | 1,5 | ≥1.000 rell. | ≥5 | 1.020 $ | +54 / −19 / −122; σ 80 | −145 $ | ≈127 $ | ≈130 $ de presupuesto de pérdida + ~10 $ de exposición |
| **P3** | 10 | 3 | ≥300 rell. | ≥3 | 614 $ | +34 / −13 / −76; σ 88 | −156 $ | 143 $ | ≈150 $ |
| **P4** (solo si H45 pasa a 25) | 25 | 7,5 | ≥300 rell. | ≥3 | 1.536 $ | +97 / −30 / −166; σ 218 | −387 $ | 354 $ | ≈380 $ |
| **P5** (solo si H45 pasa a 50) | 50 | 15 | ≥300 rell. | ≥3 | 3.073 $ | +164 / −60 / −363; σ 433 | −788 $ | 710 $ | ≈750 $ |

P3-P5 escalan PnL y coste LINEALMENTE desde 5 acc (SUPUESTO: con más tamaño cambian cola, relleno parcial y selección adversa; eso es lo que
miden H45 offline y el gemelo en cada peldaño). Escenario anual (SCENARIO, no previsión; 293 $/día × (EV + reembolso 0,011) × 365):
5 acc ≈ 8,0 k$/año con el EV OOS del simulador (≈1,5 k$ con el de «primeras 5 acc» de la población); 10 acc ≈ 16 k; 25 ≈ 40 k; 50 ≈ 80 k,
**todo condicionado a H45 y a capacidad lineal no medida**. Ninguno cuenta en el libro hasta pasar su peldaño.

## 3. Criterios pre-registrados

**Para subir de Pk a Pk+1 (TODOS):**
- S1 Maquinaria: 0 incidentes de cuadre, de identidad por hash o de doble envío; 4xx/429 < 1 % de las órdenes; cancelación p90 ≤ 150 ms.
- S2 Calibración a ESE tamaño (gate de H47, sin retocar): |tasa real − simulada| ≤ 8 pp; P(real|sim) ≥ 0,70 y P(sim|real) ≥ 0,70;
  |markout real − simulado| ≤ 0,03 (σ del markout SUPUESTA ~0,2 por €: el dataset no tiene `mo*` calculado). Desde P2 se añade: diferencia
  emparejada de PnL real − gemelo en las MISMAS pujas con cota inferior del IC90 por días ≥ −0,05.
- S3 EV del vehículo en forward del SIMULADOR (todas las decisiones, gratis): el gate de H35 tal cual (≥6 días OOS nuevos, por moneda ≥40
  rellenos, EV ponderado ≥ +0,05, IC90 por días y por cierre > 0, sin mejor día > 0, sin 5 mejores mercados > 0, ≥4/6 días +). Para P4/P5,
  además H45: EV(25) ≥ EV(5) − 0,03 y rellenos×coste ≥ 4× (y su análogo a 50).
- S4 Dinero real del peldaño: N y días mínimos de la tabla cumplidos, y EV real ponderado acumulado ≥ 0 (punto). No se pide IC>0 al real
  (sería imposible con este n: ver §0.3); se pide que no contradiga al simulador.
- S5 Régimen: la regla de ruptura de H5M (19-21 Oct: media-vigía ≤ +0,05 o ponderado ≤ 0 con IC por cierre que no excluye 0) NO disparada
  y H44 no refutada. Si se dispara, **pausa** (no se sube; se puede seguir en el peldaño actual solo si es P0/P1, que no son de EV).
- S6 Capital: OK explícito de Javi al presupuesto de pérdida del peldaño siguiente (columna «capital que exige»). Sin recargas planificadas
  en el calendario: hoy solo P0 cabe, y P1 solo a medias.

**Para bajar (automático, sin juicio):**
- B1 Un peldaño abajo si en la mirada de fin de peldaño (≥5 días) la cota superior del IC90 por días del EV real es < 0, o si S2 falla a ese
  tamaño. Re-subir exige repetir el peldaño entero.
- B2 A P0 (fuera de dinero) si el forward del simulador (S3) pierde el gate, o si se dispara K1/K2.

**Kill-switch (dimensionado con simulación, `mc.py`/`mc2.py`):**
- K1 Maquinaria, inmediato y fail-closed (ya en H47): dinero que no cuadra, saldo ilegible > 2 min, excepción repetida, tope de órdenes.
- K2 Tope catastrófico por peldaño sobre el PnL real acumulado del peldaño (tabla): P(disparo en falso | EV +0,05) ≤ 5 %; potencia contra
  EV −0,10: 15 % (P1), 26 % (P2-300), 31 % (P3). Es un techo de pérdida, no un test.
- Prohibidos: kill secuencial por media acumulada (falso 74-84 % con EV +0,077) y cualquier kill diario por PnL (añade disparos en falso sin
  potencia). Las miradas intermedias por IC con pocos días también fallan: tres miradas a 250/500/1.000 rellenos con «cota superior IC90 < 0»
  pararían en falso el 25 % de las veces con EV +0,05 (`mc2.py`); por eso solo hay UNA mirada estadística, al final, con ≥5 días.

## 4. Encaje con H47, H45 y el resto (sin duplicar capital)

- H47-A = P0 y H47-B = P1: mismo código, ledger y lock. Lo que añade la rampa a H47 **antes de lanzar B**: (1) verificar la redención
  automática de posiciones 5m ganadoras o añadir la redención al ciclo (si no, el suelo corta a los ~7 rellenos); (2) fijar el presupuesto
  de pérdida explícito (no «≤5 € de exposición») y decidir saldo/suelo; (3) registrar el reembolso cobrado por relleno.
- P2+ deben ser escalones nuevos del MISMO programa (`--escalon C…` con tamaño y N del peldaño), no un ejecutor aparte: cambio de código →
  `/code-review` medium + OK Javi. Repegado 35-65 órdenes por puja (aviso del implementador): a 300 rellenos/día son ~40-60 k órdenes/día;
  el riesgo de 429 crece con el peldaño, no con el tamaño → S1 vigila 4xx/429 por peldaño.
- H45 (offline, 0 $) no consume capital y es la puerta de P4/P5; recomendado incluir 10 acc en la misma corrida (es solo otra columna; no
  cambia su gate). Si EV(25) ≤ 0, la rampa termina en P3 (techo de escenario ≈16 k$/año).
- R5K brazo 2 queda fuera mientras H48 no lo reabra; si vuelve, comparte la misma wallet y el mismo tope K2 (no se suman presupuestos).
- PRECIERRE vive en la wallet principal: no se mezcla con la dedicada.

## 5. Siguiente paso concreto

Antes del OK de Javi a H47-B: medir en el escalón A (o con una lectura pública de la actividad de la dedicada tras su primer relleno) si
una posición 5m ganadora vuelve a pUSD sola y en cuánto tiempo; y presentar a Javi la tabla del §2 fila P1 para que elija entre (a) recargar
la dedicada a ≈45 pUSD, (b) bajar el suelo (con 12 $ efectivos P(completar) 52-62 %) o (c) aceptar B truncado (mediana ~14 rellenos ⇒ tasa
de relleno con IC de ±12 pp: gate de H47 casi seguro inconcluso). Sin esa decisión, B consume dinero sin poder pasar su propio gate.

## 6. Fuentes y reproducción

- Vehículo: `/root/polymarket-research-datalogs/m5_maker_colocacion/base_2026-10-{05..10,14..16}.csv.gz` (sha256[:16] 9251b8a31ef51063,
  e308ed886d9a086c, e5c7314898faad9a, db39e50a252766fd, c852ab36dffa8f01, 47aaebcea9e9d360, da3a47440f66c606, aadd972c959f991f,
  c226282653c40e15); motores `DEEP_k2|C0|CONS|5` (ETH), `DEEP_k1|C0|CONS|5` (SOL, XRP).
- Scripts en esta carpeta: `rep.py` (53a376910d6bb733, reproduce H35 alts), `chk.py` (d4974625e8f92360, contabilidad y rellenos por cierre),
  `mc.py` (58a96fb67e3a2953, semilla 20261019, peldaños, topes, naïf, suelo) → `mc_salida.txt`, `mc2.py` (05b0a88faf8fab33, semilla 1910,
  presupuesto vs completar B, P2 con miradas) → `mc2_salida.txt`. Método: bootstrap de días fuente y de cierres dentro del día (conserva la
  correlación entre monedas del mismo cierre); EV objetivo por desplazamiento pnl − δ·coste (conserva la varianza; SUPUESTO).
- H5M: `DL/vigia_5m_barato_maker/informe.txt` (vigía d1fa040e7bd9c08d, sin tocar), `DL/h5m_cola_sim/{informe,quien_gana_informe,ganadoras_persistencia_informe}.txt`
  (`analisis_h5m_cola_simulada.py` a361df3108004dc1, `analisis_h5m_quien_gana_banda.py` 3f7a8e2ed4d77712); ponderado y primeras 5 acc:
  `experimentos/5m_barato/validacion_19oct/informe.md`.
- H47: `/root/polymarket-research-dev/experimento_maker_h47.py` (sha 212f722088698d2a, dev 48e0fbd980; suelo 12, N A=40/B=230, 5 vivas,
  sin redención en el código), `dev/informes/h47_code_review1_19oct.md`.
- Saldo de la dedicada: 19,59 pUSD es la cifra del 17-Oct, **NO re-verificada** (la dirección completa solo está en la credencial, que no se lee).

Limitaciones: simulador CONS sin calibrar (NO_REPRODUCE → criterio v2 post hoc); 9 días de datos; escala lineal supuesta; markout sin datos;
redención no verificada; fills/día de la rampa supuestos (100 en P1, 150 en P2+).
