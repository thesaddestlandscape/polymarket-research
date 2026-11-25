# ADENDA 12 al PREREG PISTA COLA (RE-B-COLA-CANCELA) — 19-Nov-2026 ~10:57Z. Etiqueta: MECANISMO (no EV, 0 órdenes). Escrita por cheap5m-execution-engineer ANTES de crear los scripts v12 y sin haber leído NINGUNA tasa evento−placebo (f_*, C*, F*, V1..V7) de ningún día. NO se procesa ningún día de veredicto (13-19-Nov).
Hereda ADENDA_06, 07, 09, 10 y 11 (a49c31ca…) y CONTRATO_VEREDICTO_19nov. ADENDA_01-11 NO se editan. Los ficheros v11 (p1_dia.py, p3_agrega.py, p7_ipw_balance.py, run_p1.sh, HASHES_CODIGO bloque v11) NO se tocan: la cadena `out/verif_adenda11/run_adenda11_chain.sh` los está usando; v12 son COPIAS con otro nombre.

## 1. Decisiones de Javi (19-Nov ~11:00Z) y dictamen del validador que se implementan
A (Javi). La cola de completitud se mide contra el ÚLTIMO CIERRE DEL UNIVERSO del día + 120 s, no contra t1. D (Javi). E3 queda como criterio de balance (umbral 0,10) pero se añaden dos magnitudes SOLO INFORMATIVAS. Dictamen del statistical-validator (19-Nov): PASS de ADENDA_11; E3 z0 propio-vecino 0,162 = propiedad del criterio/fixture, no un bug de código.
LIMITACIÓN DECLARADA: el validador vio solo la cola del 12-Nov (día de DISEÑO), no la de ningún día de veredicto; el criterio A se fija antes de abrir 13-19-Nov y no se reajusta tras verlos.

## 2. A. Cola contra el último cierre del universo (p7 v12; sustituye ADENDA_11 §2.2 (ii))
2.1 `cierre_max_universo(D)`: máximo END (ms) de los mercados 5m de la moneda del universo Sonda1 del día D con END en (t0, t1], leído de `/root/polymarket-research-datalogs/sonda1/pasivo/sonda1_fotos_l2_<D>.csv.gz` (columnas slug, rol; un mercado cuenta solo si tiene roles `tok` y `comp`, igual que p1_dia.py líneas 19-30; END = (sufijo numérico del slug + 300)·1000). Sin fichero, sin mercados o END fuera de (t0, t1] → `None` ⇒ cola NO OK (fail-closed).
2.2 Cola OK ⇔ máximo de los `max` de `cover_fich` ≥ `cierre_max_universo` + 120.000 ms. Cabecera (mínimo de `min` ≤ t0 + 120 s) y hueco máximo entre ficheros ≤ 300 s (ADENDA_11 §2.2 (i) y (iii)) y `inputs_ok` NO cambian. `cobertura_ok` = cabecera Y cola(v12) Y hueco.
2.3 `dia_completo` publica además `cierre_max_universo_ms`, `cola_requerida_ms`, `cola_ok` y, solo informativo, `cola_v11_ok` (máximo ≥ t1 − 120 s, criterio tachado). Efecto esperado y declarado: un día cuyo universo acaba en el cierre 23:50 exige cobertura hasta 23:52:00Z en vez de 23:58:00Z; es una RELAJACIÓN frente a v11 aceptada por Javi y fijada ANTES de ver 13-19-Nov. La limitación de universo de ADENDA_11 §2.3 (Sonda1 omite 9-13 mercados BTC 5m/día) sigue vigente.

## 3. D. E3 informativo (p7 v12, `e3_calc`; solo cuando lo llama `e_block`, no en el pase 1 de small)
3.1 `E3_IC90_cluster_mercado`: bootstrap por CLÚSTER = valor de `end` (cierre del mercado) sobre las filas de propios ∪ vecinos del estrato; 400 réplicas; generador local `numpy.random.default_rng(20261119)` (no toca ningún estado global); en cada réplica se remuestrean clústeres con reposición y se recalcula max|SMD ponderado (om)| de las MISMAS 9 covariables de `cov7`; IC90 = percentiles 5 y 95; réplicas con algún grupo < 2 filas finitas se descartan y se cuentan. Campos: lo, hi, reps, descartadas, n_clusters.
3.2 `SMD_act2_wins_p99`: act2 de propios y vecinos winsorizado al percentil 99 de su unión (sin ponderar); SMD ponderado (om) como en `SMD_pond_om`.
3.3 NO cambian: umbral 0,10, la condición de fallo E3 z0, `E4_fallos`, `dia_valido_E`, la regla ADENDA_09 §2.2 (small solo-propio) ni ninguna E1/E2. Los campos nuevos no entran en ninguna condición; `max_abs_pond` y `SMD_pond_om` salen idénticos a v11 (se comprueba en `cmp_p7_v11_v12.py` y en los tests).

## 4. Cadena de equivalencia declarada (p1 no cambia)
p1_dia.py v11 = hash eed3a41d… (HASHES_CODIGO bloque v11). El fixture fxN1 (`out/verif_adenda07/fx_artefactos/p1_btc_2026-11-12_fxN1.pkl`) lleva el sello de versión `p1_v7_ADENDA07` y `code_sha256` 4d84b124… (= hash del p1 v10; v10 no cambió la etiqueta de versión). Se declara fxN1 ≡ p1_v7 (f6ab6a46…, `out/obsoletos_preD1/p1_dia_v7_adenda07.py`) por la equivalencia v7 ≡ v10 valor a valor ya comprobada (fixture fxM2, HASHES_CODIGO bloque v10) y heredada sin repetir; v11 vs fxN1 = ADENDA_11 §8 (2) (`cmp_fx_p1.json`). Cadena: p1_v7 ≡ p1_v10 (fxM2) → fxN1 → p1_v11 (solo absr5/r5/absr5_rx + cover_fich).

## 5. Versiones y ficheros v12 (copias, mínimo cambio)
`p7_ipw_balance_v12.py` (versión `p7_v12_ADENDA12`, pesos `p7w_v12`, entrada: p1 `p1_v11_ADENDA11`; salida `out/p7v12_<coin>_<D><SUF>.json`, `out/p7wv12_<coin>_<D><SUF>.pkl`); `p3_agrega_v12.py` (versión `p3_v7_ADENDA12`; lee solo p7v12/p7wv12; salida `out/p3v12_…`; REQ de hashes = p1_dia.py, p3_agrega_v12.py, p7_ipw_balance_v12.py, p5_control_sin_relleno.py, run_p1.sh, ADENDA_07/09/10/11/12); `cmp_p7_v11_v12.py`; `run_v12_post.sh` (no se lanza aquí: espera `chain.status = COMPLETE`); `tests_v12/test_v12.py`; `DIFF_v11_v12.txt`. Bloque v12 en HASHES_CODIGO.txt (solo añade; no re-lista ficheros v11).
Los pkl/JSON v11 de la cadena (out/p7_*, out/p7w_*, out/p3_*) NO se sobrescriben.

## 6. Verificaciones (con salida de comando)
(1) py_compile de p3/p7 v12. (2) tests_v12: E3 informativo determinista, mismos `max_abs_pond`/`SMD_pond_om` que v11, winsor reduce un outlier, cola con casos límite (justo en el borde, falta Sonda1, None), `cierre_max_universo` con fichero sintético, REQ/patrones de nombre. (3) cmp v11/v12 sobre el fixture fxP1 dentro de run_v12_post.sh (p7 v12 no cambia E1/E2/E3/E4 ni `dia_valido_E`). (4) Primer p7/p3 v12 sobre datos reales = run_v12_post.sh tras la cadena v11.

## 7. Tachados
ADENDA_11 §2.2 (ii) (cola ≥ t1 − 120 s) pasa a informativo (`cola_v11_ok`). ADENDA_11 §9 sigue en lo demás. Un cambio de código posterior a esta adenda exige ADENDA_13 por escrito antes de procesar ningún día de veredicto.

## 8. Límites
0 tasas leídas; 0 días de veredicto procesados; los E3 informativos no sustituyen el criterio. Esta adenda no cambia prereg, contrato ni universo.
