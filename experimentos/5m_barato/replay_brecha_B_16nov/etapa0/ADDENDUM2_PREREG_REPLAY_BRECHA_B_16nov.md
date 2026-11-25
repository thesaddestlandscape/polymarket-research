# ADDENDUM 2 — PREREG_REPLAY_BRECHA_B_16nov (BF5-REPLAY-COLOC-v1): Q-C2, δ por orden con la ida y vuelta del propio DELETE de B

- **Redacción y sellado**: 2026-11-16 (~18:10Z), ANTES de calcular ninguna cifra de Q-C2. Sello: `ADDENDUM2_PREREG_REPLAY_BRECHA_B_16nov.sha256` (sha256 de este fichero).
- **Autor**: polymarket-quantum-alpha-miner (encargo de la sesión principal). **Aprobación**: Javi (usuario), 16-Nov, vía coordinador: OK explícito a la regla de latencia δ_i = (t_fuera − t_cancel_int) − 24 ms de acuse, solo con datos reales vigentes (paquete_l 13-Nov, ensayos B2/B3/B5; nada de la Sonda antigua).
- **No edita** el PREREG (sha256 `f1a7d76664ff4ede03a98b948fe78e43d6e95bf3f4381390df9bb206a82fa562`) ni el ADDENDUM1 (sha256 `7dca…4718`), que siguen vigentes. Q-C (ADDENDUM1 §2.2, l = MIX) sigue siendo la cifra de ADDENDUM1; Q-C2 la complementa y no la sustituye. Nombre distinto de `ADDENDUM2_B_F5.md` (programa BF5-EXP1, ajeno).
- **Ubicación**: `experimentos/5m_barato/replay_brecha_B_16nov/etapa0/` (ámbito de escritura del agente; PREREG y ADDENDUM1 viven en `misiones/5m_barato/alpha_miner_B_F5_15nov/`). Si la sesión principal lo copia junto al PREREG, manda el sha256.
- **Alcance**: solo lectura, 0 órdenes. No toca producción, `data/live`, ADD3 (no se lanza; se leen sus ficheros COMPLETE), las Etapas 2-3 (bloqueadas), los días HOLD (10-14 Nov) ni los días ≥15-Nov.
- **Etiqueta**: EXPLORATORY/explicativo (4 días, una sola estrategia real). No decide ninguna palanca ni valida B.

## 0. Motivo (cifras ya publicadas en `QC_brecha_nivel_mix.json`, sha256 `1c83e558…3166`)
- Q-C con MIX cierra el 79,9 % (ΔEV +0,128, IC90 por cierre [+0,013, +0,255]). Tiene tres problemas:
  - (i) MIX transfiere latencia de otro día (13-Nov, ~2,2 h, solo LO), con d_proc = 3 ms supuesto.
  - (ii) Depende del sorteo: con 1.000 semillas cierra entre 0,565 y 1,077.
  - (iii) El 79,9 % supera el techo de quitar los 12 FP (72,5 %: escalón publicado +0,1161 sobre una brecha de 0,1602). Parte de ese cierre sale de anular 10 TP, que son rellenos REALES: eso es un error, no una corrección.
- **Hecho nuevo** (ADD3, ficheros COMPLETE leídos el 16-Nov hacia las 18:02Z; no los lancé yo):

  | Día | Ventanas hi | Ventanas lo | Indet | sha256 |
  |---|---|---|---|---|
  | 20-Oct | 144 | 0 | 0 | `806f6152…aa84` |
  | 21-Oct | 138 | 6 | 0 | `61e5c166…25a1` |
  | 22-Oct | 143 | 1 | 0 | `84e17302…5071` |
  | 23-Oct | 76 | 67 | 1 | `705f1a5a…e277` |

  B operó casi siempre en HI, y las anclas del 13-Nov son LO. Aplicar MIX a B es, por tanto, transferir latencia entre clases.

## 1. Semántica verificada antes de sellar (solo estructura; sin EV ni etiquetas por orden)
- **Ledger** `experimento_h47_B_ledger.jsonl` (sha256 `32653e4f…c2c9`).
  - Eventos `intencion_cancel` (ts) y `fuera_libro` (ts, origen).
  - origen = 'cancel' en 3.737 órdenes, todas con t_cancel_int. origen = 'status' en 59: 1 con t_cancel_int y 58 sin él.
  - `cancel_lat.ms` es la ida y vuelta del DELETE medida por el cliente. Ejemplo, oid 0x93c7…: 61,4 ms, frente a t_fuera − t_cancel_int = 62 ms.
- **`ordenes_b.csv`** (sha256 `7ebd392b…d3a5`, generado por `c1_build_b.py`).
  - t_cancel_int y t_fuera son esos mismos ts, en segundos con resolución de 1 ms.
  - Hay 3 oid con dos `intencion_cancel`: se conserva el último, igual que en Q-C.
- **t_fuera − t_cancel_int** (origen cancel): n = 3.737, mínimo 51, p50 65, máximo 3.464 ms, 0 negativos.
- **Monedas**: B no tiene órdenes BTC (eth 1.357, sol 1.296, xrp 1.143).
- **Pool del 13-Nov** (`l_pool_vigente_13nov.json`, sha256 `7d92a57c…`; solo latencia).
  - A = ack − ex: p5/p50/p95 = 21/24/28 ms con las 313 anclas, y 20/24/28 ms con las 187 sin BTC.
  - En el cuartil alto de v + A, el exceso está en v (envío → sello EX) en un 103 % (todas) y un 121 % (sin BTC).
  - Esto respalda δ = ida y vuelta − A (una resta), no un reparto proporcional.
- **Lo único visto por orden** es un ejemplo del ledger (oid 0x93c7…). No he calculado δ_i de ninguna orden con relleno, ni simulado ni real.
- **Otras entradas** (sha256):
  - V3_2026-10-20..23.pkl: `f96b1382…`, `cd7e4dcb…`, `2918ce32…`, `c904c16a…`.
  - own_2026-10-20..23.pkl: `b4b2d686…`, `47599123…`, `ee7142c4…`, `80214e77…`.
  - T1_tx.pkl: `fbf7e5ca…`.
  - brecha_nivel_v3.json: `d995a069…`.
  - qc_brecha_nivel_mix.py: `e20db942…a0a7818`.
  - QC_desc_tf_menos_tcs.json: `18e87406…8176`.
  - El script comprueba los hashes completos.

## 2. Definición primaria (fijada por la aprobación de Javi)
**δ_i = 1000·(t_fuera_i − t_cancel_int_i) − A**, con **A = 24 ms** (mediana de ack − ex en el pool del 13-Nov).
- **Cuándo está definida**: solo si origen(fuera_libro) = 'cancel' y t_cancel_int no es nulo (3.737 órdenes).
  - La orden con origen 'status' y t_cancel_int no se corrige (δ = ∞).
  - Las 58 órdenes sin t_cancel_int tampoco se corrigen, igual que en Q-C y en brecha_nivel_v3.
- **Sin d_proc adicional**: t_fuera − t_cancel_int ya lo contiene.
- **Cómo se aplica**: con `sim_con_delta` (copia literal importada de `qc_brecha_nivel_mix.py`), pasando δ como serie por orden. Se anula el relleno simulado si tf_sim (reloj EX, sello v3) > 1000·tcs (LOC) + δ_i. Es la misma convención mixta de relojes que en brecha_nivel_v3 y Q-C.
- **Derivación**. Sea LOC = EX + θ.
  - Ida y vuelta = d_proc + ow_envío + proc + ow_retorno; θ se cancela.
  - El instante EX efectivo de la cancelación menos tcs (convención mixta del simulador) vale (t_fuera − tcs) − (ack − ex)_vigente.
  - Por tanto, δ_i es exacta si A es el ack − ex vigente en esa ventana.

## 3. Variantes preregistradas (primaria = V0)
- **V0 (primaria)**: A = 24.
- **V1, «sin BTC»**: A = mediana de las 187 anclas ETH/SOL/XRP = 24 ms. Es idéntica a V0 por construcción (B no tiene órdenes BTC y BTC no entra en la ida y vuelta). Se reporta como idéntica.
- **V1d, sensibilidad al acuse**: A_j sorteado por orden del pool (todas las anclas, y solo sin BTC), con j = `default_rng([int(oid,16), 20261116, 2]).integers(n_pool)`.
- **V2, sensibilidad**: δ'_i = cancel_lat.ms_i − 24 (ida y vuelta HTTP pura, sin el registro local). Se usa el último `cancel_lat` de cada oid.
- **V3, sensibilidad**: reparto proporcional δ''_i = (t_fuera − t_cancel_int)·33/57 (medianas de v y de v + A en el pool). El §1 la desfavorece.
- **V4, cota HI** (preregistrada como cota, no como primaria): para las órdenes en ventana hi (clase causal), δ_i − 20,5.
  - En HI, el suelo WS rx − ex sube unos 20 ms.
  - Si ack − ex sube con él, δ_true = δ_i − 20,5. Esto ocurre si cambia θ, el camino de retorno compartido o la red de forma simétrica.
  - Si el salto es exclusivo del feed WS (pasarela), δ_true = δ_i.
  - En ningún caso es +20,5: **la corrección HI de la regla por orden está en [−20,5, 0]**. En MIX el signo era ambiguo (±20).
  - El cierre se reporta como el intervalo entre V4 y V0.
- **Clase**: la causal de Q-C, a partir de t_dec: w = floor((t_dec_ms − 200 − día0)/600000) − 1, sobre el perfil ADD3 COMPLETE. Los días sin ADD3 COMPLETE quedan como «pendiente_ADD3», y V4 no se les aplica.

## 4. Métricas
- **Las de Q-C**, con `metricas()` copiada:
  - EV con rebate.
  - Cierre f = (EV_sim(δ) − EV_sim(∞)) / (EV_real − EV_sim(∞)).
  - ΔEV, precisión, recall y anulados TP/FP.
- **Cierre descompuesto**: f_soloFP aplica solo las anulaciones de FP de la regla; f_soloTP aplica solo las de TP (que son errores).
- **Techos deterministas** (oráculo, sin ajuste):
  - C1 = quitar los 12 FP.
  - C2 = quitar solo los FP con tcs y x > 0, los alcanzables por cualquier δ ≥ 0, sin tocar ningún TP.
- **Brecha residual**: EV_real − EV_sim(δ).
- **IC90 percentil por cierre**: cl = día + t_ini//300000, B = 10.000, semilla 20261116, los mismos pesos para todas las variantes (= Q-C).
- **Cortes**:
  - Por día (los 4, con IC dentro del día para V0).
  - LODO.
  - Por clase (lo/hi/indet; V0 y V4).
  - Por moneda (descriptivo).

## 5. Pruebas preregistradas
**T1 — predicción de los 7.** Son los TP con x_i = tf_sim − 1000·tcs > 111 ms; sus valores ya están publicados post hoc: 127, 364, 442, 465, 712, 723 y 866. Predicción: «deben tener ida y vuelta larga», es decir, δ_i ≥ x_i (sobreviven).
- Confirmada: ≥ 6/7. Refutada: ≤ 3/7. Con 4-5: no concluyente.
- Probabilidad nula: p_i = fracción de las 3.737 δ con δ ≥ x_i; se da la cola Poisson-binomial P(X ≥ k_obs).

**T1b — lectura si T1 falla (descriptivo).** Se define x_real_i = tm3 del último relleno real propio − 1000·tcs; el tm3 sale de own_<D>.pkl, enlazado por T1_tx.order_hash → tx. Clasificación por orden:
- «ida y vuelta larga»: δ_i ≥ x_i.
- «simulador tardío»: δ_i < x_i y x_real_i < δ_i.
- «contradicción»: δ_i < x_i y x_real_i ≥ δ_i.
- «sin sello».

**T2 — consistencia con la verdad (todos los rellenos reales).** Una regla de carrera correcta exige que ningún relleno real ocurra después de que la cancelación surta efecto: x_real_último < δ_i.
- Elegibles: órdenes con relleno real, δ definida, sello propio distinto de 'sinev' y x_real_último > 0.
- Violación: x_real_último ≥ δ_i.
- Umbrales: PASS si las violaciones son ≤ 10 % de los elegibles; FAIL si son > 25 %; AMBER entre medias; INSUFFICIENT si hay menos de 5 elegibles.
- Se evalúa con V0 (primaria) y con V4 (en HI), y también por clase.
- Sensibilidades: incluyendo 'sinev', y con una banda de ±20 ms (descriptivo).

**T3 — placebo de permutación (sobreajuste a 12 fantasmas).**
- Diseño: δ se permuta entre las 3.737 órdenes que la tienen definida, 2.000 veces, con rng = `default_rng([20261116, 3])`. Como sensibilidad, permutación estratificada por día×moneda con `default_rng([20261116, 4])`.
- Estadísticos: f (cierre) y S = anulados_FP − anulados_TP.
- p unilateral = (1 + #{perm ≥ obs}) / (1 + 2.000). S es el estadístico que decide; f se reporta.
- Lectura:
  - p_S < 0,05: la ida y vuelta de CADA orden informa de la carrera, porque separa fantasmas de rellenos reales mejor que su distribución marginal.
  - p_S ≥ 0,05: no hay identificación por orden. El cierre lo explica el NIVEL de δ (equivale a un sorteo tipo MIX): no refutado, pero «no validado» a nivel de orden.
- δ_i no tiene parámetros ajustados al desenlace (A viene del 13-Nov y la ida y vuelta está medida). El sobreajuste solo puede venir de la elección de la regla, y el placebo mide si el emparejamiento importa.

**T4 — escalón 35-49 ms (cautela a).** Ventana 0 < x ≤ 111: 7 FP en [35, 49] y 12 TP en [12, 51] (valores ya publicados). El escalón «lo explica el δ propio» si se cumplen las tres condiciones:
- (i) Al menos 5 de los 7 FP del escalón quedan anulados (δ_i < x_i).
- (ii) Como mucho 3 de los 12 TP de la ventana quedan anulados.
- (iii) p_S restringido a la ventana, con las mismas permutaciones globales, es < 0,10.

Si no se cumplen, el escalón sigue siendo post hoc.

**T5 — HI con lo medido (cautela b).**
- Medida: ida y vuelta (t_fuera − t_cancel_int) por clase de la ventana que contiene t_cancel_int (clase concurrente: la ida y vuelta se mide en ese momento), en los días con ADD3 COMPLETE. Se reporta la discordancia con la clase causal.
- Contraste principal: dentro del 23-Oct (hi frente a lo, mismo día). Diferencia de medianas con IC90 bootstrap por ventana de 10 min (B = 2.000, `default_rng([20261116, 5])`).
- Descriptivo: post_lat.ms (alta) por clase.
- Lectura:
  - |Δ| ≤ 5 ms: el salto del suelo no está en nuestro camino de ida y vuelta (es θ o un retorno exclusivo del WS). La corrección HI queda en {−20,5, 0} sin decidir y se usa la cota V4.
  - Δ ≥ 15 ms: cambio de red. ack − ex sube con el suelo, así que la corrección vigente es −20,5 (V4).
  - Entre 5 y 15 ms: no concluyente.
- T2 por clase con V4 discrimina además: los rellenos reales en HI con x_real ∈ [δ_i − 20,5, δ_i) contradicen V4.

## 6. Veredictos preregistrados de Q-C2
- **MECANISMO_SOPORTADO_POR_ORDEN**: p_S global < 0,05, T2(V0) PASS y T1 no refutada.
- **NIVEL_SIN_IDENTIFICACION_POR_ORDEN**: p_S ≥ 0,05 y T2(V0) PASS.
- **CONTRADICHO**: T2(V0) FAIL.
- **INSUFFICIENT**: menos de 5 elegibles en T2, o menos de 10 rellenos simulados afectables.
- Cualquier otra combinación se reporta literalmente, sin etiqueta nueva.

**Cómo se reporta el cierre**:
- f(V0) y el intervalo HI [f(V4), f(V0)], con IC90, junto a C1 y C2.
- El «100 %» solo es alcanzable por δ si C2 ≥ 1. Si C2 < 1, la parte 1 − C2 no la cierra ninguna corrección de la cancelación. Se atribuye con los escalones publicados:
  - FN: 132 rellenos reales que el simulador no ve. En 94 nuestra orden es el único maker, y la cinta de validación excluye nuestros prints.
  - FP con x ≤ 0.
  - Cantidad.
- Un f por encima de C2 implica anular rellenos reales: es un error, no un cierre mejor.

## 7. Cautela c — IC de la brecha
- **Verificado antes de sellar**:
  - El ledger de B solo tiene órdenes del 20 al 23-Oct (puja_post 405 / 1.121 / 1.746 / 524). Del 24 al 27-Oct solo hay eventos sin órdenes, y no existe otro ledger de B.
  - H47-A (932 órdenes reales a 0,02, 19-20 Oct) es otra población (pujas profundas) y no sirve para la brecha de B. Además, el on-chain de `keep_onchain_re_as_b` empieza el 20-Oct.
- **Se calcula (descriptivo)**:
  - Error típico bootstrap de EV_real, EV_sim(∞), la brecha y la brecha residual.
  - Componentes con IC: paso FP, cantidad y FN.
  - Proyección de n_cierres (y de días de B al ritmo del 20-23 Oct) para que la semiamplitud del IC90 de la brecha baje a 0,10 y a 0,05 €/€ (escala 1/√n), y para que la brecha excluya el 0.
- **Propuesta, no se ejecuta aquí** (exige cargar el libro de cada día, y ADD3 es el trabajo pesado en curso): un estimador de varianza reducida por markout. Usaría el mid EX a +60 s del relleno, con el mismo reloj EX para rellenos reales y simulados (sin mezclar relojes), y su sesgo se mediría contra el desenlace oficial en la misma muestra.

## 8. Qué falta para HI y medición mínima (sin dinero real)
- **Falta**: ack − ex en ventanas HI (A_HI), o lo que es lo mismo, θ + ow_retorno REST por ventana. Las anclas del 13-Nov son solo LO, y las anclas HI con dinero real están vetadas sin el OK de Javi.
- **Medición mínima propuesta** (pasiva, sin claves, coste 0):
  - GET públicos al CLOB (p. ej. /book) cada ~1 s, registrando envío y recepción LOC en ms y el `timestamp` EX de la respuesta.
  - Calcular el suelo p5 por ventana de 10 min de (recepción − timestamp) y de la ida y vuelta, y cruzarlo con la clase del suelo WS del mismo día. Hacen falta al menos 2 días con ventanas de ambas clases.
  - Lectura: si (recepción − timestamp) sube ~20 ms en HI, manda V4 (−20,5); si no sube, manda V0.
  - Antes conviene comprobar si algún fetcher existente ya guarda esos campos: sería una medición retrospectiva gratis.
  - La instalación corresponde a la sesión principal.

## 9. Salidas, recursos y reglas
- **Script**: nuevo, `etapa0/qc2_delta_propio.py`.
  - Es de solo lectura. Importa `qc_brecha_nivel_mix.py` (y comprueba su sha256), no importa el motor y no lee ms2.
  - Su sha256 queda en `QC2_DECLARACION_PREVIA.json` (+ `.sha256`) antes de ejecutarlo.
- **Salidas**: `QC2_delta_propio.json`, `.tsv` y `.log`, más `QC2_delta_propio.sha256`.
- **Reproducción previa obligatoria**: antes de aplicar ninguna δ_i, la muestra y las cifras de Q-C (sin corrección y MIX) se recalculan y deben igualar a `QC_brecha_nivel_mix.json`. Si no cuadran, el script queda PARADO (Fail Loud).
- **Recursos**: nice 19, ionice 3, `ulimit -v 3000000`, < 5 min de CPU, MemAvailable ≥ 2,5 GB, load5/nproc ≤ 3, fuera de 06:00-09:30Z.
- **Cambios tras ver resultados**: crean una versión nueva y son solo descriptivos.
