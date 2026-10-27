# Expediente RE-CENSO-GANADORAS — 26-Oct-2026 (cheap5m-reverse-engineer)
Estado de cierre: PARTIALLY_SOLVED · Bloqueo dominante (A-K): A/H (la ventaja persistente que existe es de SELECCIÓN de favoritos tardíos y pequeña por €; el grueso del dinero lo pagan los tomadores en comisiones a Polymarket) · Secundarios: K (el censo maker+tomador completo `c1` ha estado bloqueado por carga; ver §9), G (19 días), E (cola y latencia reales de la candidata sin medir)
Sin validación independiente. Fuentes: on-chain (m5_onchain → f6 T_D.parquet; quien_gana_agg). Desenlace: unión de cachés oficiales, sin red. Fuera de mi alcance: pspspsps5 y mo-money (los lleva el agente wallet-intelligence en `b_perdidas_22oct/wallet_mecanismos_26oct/`).

## 1. Fenómeno y premisa
Javi: «hay miles de wallets minando pasta de verdad con estrategias claras; es imposible que nosotros no podamos». Contra eso, el roster previo de 5m barato salió vacío (ganadoras_persistentes, banda 0,05-0,30). Aquí no se acepta ninguna de las dos posturas: se mide.

## 2. Datos y reproducción
| cifra | artefacto → crudo | estado |
|---|---|---|
| Censo de tomadores 5m (todas las monedas y bandas, 05-23 Oct) | f6 `T_D.parquet` (de m5_onchain, taker==exchange) → `scripts/c5_censo_tomadores.py`, `c5_salida.txt` | REPRODUCIDA (cálculo propio; cobertura del desenlace 99,97 % del USD como mínimo diario) |
| Censo proxy maker+tomador, solo 5m de PARES (1/3 de los mercados), 06-25 Oct sin el 19 | `DL/m5barato_mision/quien_gana_agg_D.csv` → `scripts/c0_proxy.py`, `c0_salida.txt` | REPRODUCIDA (agregados del cron; sin rebate) |
| Favorito tardío al ask real | `DL/precierre_multioffset_fase0.csv` (25-Sep..26-Oct) → `c4`/`c6`/`c7` | REPRODUCIDA (cobertura del desenlace 86,5 %; faltan días enteros 30-Sep..05-Oct y el 26-Oct = missing) |
| «roster de 5m barato vacío» (ganadoras_persistentes) | `ganadoras_persistentes/INFORME.md` | no recomputado; coherente (otra banda y otra unidad) |

Relojes: el on-chain va con hora de BLOQUE (~2,4 s después del casado; T = cierre − bloque). El ask de multioffset es el libro leído al offset (lat_libro p50 64 ms). Nuestro tomador casa ~215 ms + taker delay más tarde: el EV medido es una COTA OPTIMISTA.

## 3. Hechos (con fuente)
1. **Quién paga** (c5, 19 días, todos los 5m).
   - Los 35.261 tomadores pierden en neto −2,72 M$ (≈ −143 k$/día). De eso, 2,63 M$ son comisiones (≈138 k$/día) y solo −88 k$ es pérdida direccional antes de comisión.
   - El rebate del 20 % devuelve ≈27 k$/día a los makers; Polymarket se queda ≈110 k$/día.
   - En el proxy de PARES, la suma de todas las wallets es exactamente −comisiones cada día (−861 k$ en 19 días). El juego es de suma negativa por la comisión, no por la dirección.
2. **¿Miles ganando?**
   - Sí ganan muchas: 9.009 tomadores (25,5 %) y 10.660 wallets en PARES (33 %) acaban el periodo en positivo. Ganadoras con más de 1 k$: 213 tomadores. Con más de 10 k$: 18.
   - Pero casi todo es varianza. Persistencia walk-forward (SEL 05-14 → TEST 15-23):
     - Tomadores: 328 en el roster; positivas en TEST el 37,8 % frente al 15,8 % del placebo emparejado por volumen (p<0,001). El neto del roster en TEST (−13,6 k$) NO supera al placebo (−28,7 k$; p95 −3,9 k$; p=0,19).
     - PARES (maker+tomador): 414 en el roster; 48,6 % positivas frente al 24,5 % del placebo (p<0,001); neto TEST +11,9 k$ frente a −12,5 k$ (p=0,044).
   - Con BH-FDR q=0,10 sobreviven 59 tomadoras (+34 k$ en los 9 días de TEST; +63 k$ en el periodo ≈ 3,3 k$/día entre todas) y 90 wallets en PARES (+38 k$ en 19 días).
   - Por la regla del prereg (≥1.000 persistentes por encima del azar), **la premisa «miles» se RECHAZA: son ~60-90, no miles**. Hay persistencia real, pero en un subconjunto pequeño y con poco dinero.
3. **Concentración**: el top-100 se lleva el 56 % del beneficio de las tomadoras ganadoras y el 48 % en PARES. El top-1 solo un 3-4 %.
4. **Mecanismo de las persistentes tomadoras** (c5, descriptivo):
   - **M1 (≈70 % de su volumen).** Comprar el FAVORITO ≥0,95 (sobre todo 0,95-0,99 y >0,99) con 10-150 s restantes. Rinde +0,7..+1,2 %/€ frente a −0,2..−0,5 % de la población en las MISMAS celdas. Órdenes grandes (55-1.130 $), 15-19/19 días positivos, BTC 0,9-1,0 (0x5e4aa0f1, 0x48ac40fc, 0x87e3bbac, 0x8e777ef6, 0xab36e680, 0x0567e29d).
   - **M2.** Tomador direccional en BTC, banda 0,3-0,7, T 60-300 s, muchas órdenes pequeñas (6-23 $). EV +2..+7,5 %, que sube cuanto más cerca del cierre (T 30-60 s: +7..+19 %) (0x129246be, 0x5e2b9261, 0x75cc3b63, 0x20d2309c). Es compatible con un modelo propio o con llegar antes que el libro (Binance). Con la hora de bloque no se puede identificar; hacen falta ms.
   - Los makers persistentes (0x2dad1d7d 19/19 días, 0x4233…, 0x0ab0, 0xf074, 0x0997) solo están en el proxy de PARES. Su perfil por banda queda pendiente del censo c1.

## 4. Experimentos (prereg con sha antes de calcular)
- E-RE-CG-00 proxy PARES (`ADENDA_E00.md`) y E-RE-CG-01b tomadores (`ADENDA_E01b.md`): §3.
- **E-RE-CG-02, M1 ingenuo** (`PREREG_E02.md` sha256 f7a6ce28…b556). Comprar el favorito con ask 0,95-0,99 a T−60: EV −0,0132 (IC90 por días −0,018..−0,008), 11/32 días positivos, n=5.757 → **REFUTADO para nosotros**. BTC ≈0 (−0,0002; profundidad p50 4 k€). Las persistentes ganan por SELECCIÓN, no por estar en la celda.
- **E-RE-CG-03, M1 selectivo por z** (`PREREG_E03.md` sha256 78d05842…f3eb). El umbral se elige en DESC (25-Sep..10-Oct) y se juzga una vez en OOS (11-26 Oct):
  - **T−120 s, |z_v2| ≥ 8, ask 0,95-0,99**: OOS EV **+0,0116 €/€** (IC90 por días +0,008..+0,014; p_boot <0,001), 14/15 días positivos, sin los 2 mejores +0,0105, acierto 99,79 % frente a un ask medio 0,9855, n=476. **CANDIDATA**: pasa el prereg con Bonferroni ×3. Control sin z en OOS: −0,0049.
  - T−90 (z≥4): OOS +0,0015 (IC cruza 0). T−60 (z≥4): −0,0007. Ninguna de las dos pasa.
- c7 (POST-HOC, descriptivo de la regla congelada):
  - 3 pérdidas en 985 entradas con desenlace (0,30 %; Wilson95 superior ≈0,9 % frente a un umbral de rentabilidad ≈1,35 %). Las 3 fueron con z 10-11,5: el filtro no evita la cola.
  - 31,8 entradas/día en 23,7 cierres/día. Profundidad al ask: p10 20 €, p50 470 €, p90 5.551 €. BTC p50 3,4 k€, el resto 25-576 €.
  - Contrafactual a nivel 1 sin competencia: 1,3 k€/año a ≤10 €/entrada, 6,3 k€ a ≤50 €, 22,7 k€ a ≤200 €, 82,6 k€ a ≤1.000 €.

## 5. Qué se puede sostener / qué NO
SÍ:
- El dinero que «minan» las ganadoras sale sobre todo de otros tomadores y de rebates, dentro de un juego que pierde ~138 k$/día en comisiones.
- Persistentes de verdad hay ~60-90, con poco dinero agregado (≈2-4 k$/día).
- Su mecanismo dominante (M1) es comprar favoritos tardíos SELECCIONADOS.
- Un filtro propio de z sobre datos propios reproduce la selección fuera de muestra a T−120 (+1,16 %/€, 15 días OOS).
NO:
- Que M1-selectivo sea capturable a la latencia real: falta el ask a +215 ms + taker delay y la competencia por el mismo ask.
- Que escale linealmente con la profundidad: la profundidad p50 en alts es 25-576 €, y los tomadores persistentes compiten por ese mismo libro.
- Que la cola esté acotada: con 3 pérdidas, el EV depende de 1-2 sucesos. Una pérdida extra en OOS lo baja a ≈ +0,009.
- Nada sobre M2 (velocidad o modelo) sin datos en ms.

## 6. Requisitos frente a lo que tenemos
| mecanismo | qué exige | nuestro estado | replicable |
|---|---|---|---|
| M1 favorito tardío selectivo (T−120, z≥8) | decidir con ~120 s de margen (sin carrera de ms); capital por entrada 50-1.000 € con resolución en ≤120 s ⇒ capital simultáneo = entradas del mismo cierre × stake (media 1,3; pico ≤6 monedas ⇒ ≤6 k€ a 1.000 €/entrada); aguantar una pérdida −100 % cada ~300 entradas | latencia de 215 ms irrelevante a 120 s salvo que el ask se lo lleven; capital actual 40 $ libres + dedicada 19,6 pUSD | SÍ en mecanismo; capital = decisión de Javi (≥0,5-3 k€ para ≥6-23 k€/año contrafactual) |
| M2 direccional BTC 0,3-0,7 tardío | edge de modelo o de velocidad en ms frente a Binance/libro | FV v1-v5 no baten al mid; tomador a 215 ms va por detrás del rival 150-300 ms (V4) | NO hoy (lo decide un estudio en ms; ver §8) |
| Makers persistentes (rebate + cola) | volumen ≥89 €/día para el rebate y cola delantera | B: −0,072 €/€, cola sin calibrar | NO demostrado |

## 7. Economía (sin sumar solapados)
Validada: 0 €. Exploratoria: M1-selectivo +0,0116 €/€ OOS, n=476, 15 días. Contrafactual por capacidad a nivel 1 sin competencia: 1,3 / 6,3 / 22,7 / 82,6 k€/año con 10 / 50 / 200 / 1.000 € por entrada, que en capital equivale a ~0,03 / 0,15 / 0,6 / 3 k€ simultáneos.
Solape: con PRECIERRE live ninguno en operaciones (banda 0,25-0,65 frente a ≥0,95), pero comparte el mecanismo TWAP/z y los mismos cierres (riesgo de racimo conjunto). Con B, ninguno.
Hueco a 200 k€: incluso el contrafactual de 1.000 €/entrada (82,6 k€) deja ≥117 k€, y supone llevarse el 100 % del nivel 1 sin competencia, lo que no es creíble con ~60 tomadores persistentes compitiendo.

## 8. Subestrategia candidata y siguiente experimento
**FAV-TARDÍO-Z (5m, T−120 s, |z_v2| ≥8, ask 0,95-0,99, 6 monedas).** Regla congelada en PREREG_E03, sin retoques.
1. Forward pasivo ≥10 días nuevos (desde el 27-Oct) sobre el mismo logger. Gate: EV ≥ +0,005, IC90 por días >0, sin los 2 mejores >0, ≥300 entradas. Coste 0, script `c6` sin cambios.
2. Capturabilidad (barato, libro5_ms / maker_ms): ask y tamaño a +215/+400 ms del offset en las entradas de la regla. ¿Sigue el ask ≤ el de la decisión y hay profundidad? ¿Hay prints de tomadores persistentes en esa ventana?
3. Racimo: correlación de pérdidas entre monedas en el mismo cierre (el kill y el sizing por cierre, no por mercado).
4. M2: con libro5 T (hora del exchange) cruzar las órdenes de 0x1292/0x5e2b/0x75cc con los saltos de Binance (bookTicker c[7]). Si compran <300 ms tras el salto, es velocidad y no es replicable.
Que pasar a dry-run o a real es decisión de Javi, con code-review y su OK.

## 9. Pendiente del censo completo (c1)
`scripts/c1_extrae.py` (maker+tomador, todas las bandas, rebate estimado, ambos lados), 21 días 05-25 Oct, con checkpoint por día y manifest en `VOL/agentes_datos/re_censo/manifest.json`. Estuvo bloqueado por load5 >4 de 10:21 a 13:03Z. Relanzado a las 13:05Z con la guarda nueva de Javi (load5 <8, MemAvailable >2,5 GB, fuera de 06:00-09:30Z) y en espera porque la carga estaba en 9,2. Al acabar: `python3 scripts/c2_analiza.py c2_perfil.csv` da Q1-Q3 con makers. Hasta entonces, la parte maker solo es el proxy de PARES.

## 10. Refutación intentada
1. Placebo emparejado por volumen: la persistencia por FRACCIÓN de wallets supera al azar; el NETO del roster tomador no. No hay que confundir «más wallets positivas» con «más dinero».
2. M1-selectivo: umbral elegido en DESC; OOS de una pasada con Bonferroni; control sin z negativo; 14/15 días. Pero n de pérdidas = 1 en OOS: frágil ante la cola. Desenlace con 86,5 % de cobertura en días enteros (no asociado a resultado: faltan días completos del caché).
3. Riesgo de look-ahead: z_v2 usa la ventana TWAP alineada ya disponible al offset (logger en vivo). La desviación de 3 s de la ventana está corregida en _v2.
4. «Persistentes» en PARES con PnL de céntimos y 100 % de días positivos: es microcarry (≥0,99). Su dinero es irrelevante.
5. Validación independiente: PENDIENTE (statistical-validator sobre c5/c6/c7 y red-team sobre la capturabilidad de FAV-TARDÍO-Z).
