# PREREG_SIML_V2 — validación KS del modelo temporal de SIM-L (27-Nov-2026, redactado antes de las 22:00Z; firma = `.sha256` de este fichero + OK del chief/Javi)

Anclas: ANEXO2 `CONTRATO_5BIS_EXP5B_27nov.ANEXO2_27nov.md` §1 (sha256 `4d8c4551d30a2c5f2ddf5c5e57cb56ff98f69d133d6ac9e5c5c1eac6767e6c26`, verificado `sha256sum -c` OK); `PREREG_SIML_26nov.md` (sha256 `052d42a391a306171e8d688e7c3690be32baead7401c1f3c17b75bcf7419b404`, intacto; su §3 prohíbe repetir ESTA KS con otros días/umbrales: no se repite, se valida en una noche NUEVA bajo este prereg); `PREREG_SIML_26nov.ANEXO_DESVIACION_27nov.md` (libros cruzados no vetados en SIM-L: sigue vigente como limitación declarada). Dev-bk: `/root/polymarket-research-dev-bk/experimentos/5m_barato/b_k_ejecutor`.

## 1. Qué cambia y qué no
Causa del fallo del intento 3 (`ks_sim_vs_seco.json`, seco 25-26 Nov): modelo temporal (el sim satura en 100 ms exactos y p50 +1,5-3,6 ms; ANEXO2 §1c). Se parametriza el modelo temporal (periodo P, PROC, jitter gaussiano σ) en una **copia aislada** (`siml_v2.py`, `siml_valida_v2.py`): `siml.py` y `siml_valida_l4.py` NO se tocan (están en los pins del seco de esta noche; una primera edición in situ rompía `pins_ok` y se revirtió en minutos, sha16 originales `231ef58fe4c36422`/`6f929cd8fd016322` restablecidos y `manifest_codigo.py --pins` = ok). No cambia: criterio D<0,05, n_min 100, los 6 contrastes, la exclusión, la fase sembrada por día, el simulador firmado ni L1/L3a/L3b.

## 2. Test de identidad (hecho, 27-Nov ~18:10Z)
Con P=100 / PROC=3 / σ=0 el código V2 reproduce el anterior **bit a bit**: (a) `test_siml_v2_27nov.py` (11 pruebas: función de despertar vs copia literal congelada y vs `siml.py` original, con/sin anclas, cfg por defecto sin clave `modelo`, jitter determinista/agrupado, periodo fraccionario monótono); (b) `test_siml_v2_sobre_stubs_27nov.py` = las 28 pruebas de SIM-L sobre stubs apuntando a `siml_v2` + 1 prueba nueva de `run_day` con modelo (todas verdes; 74 con `test_siml.py` y `test_siml_valida_l4.py`); (c) end-to-end: la KS completa sobre 25-26 Nov con el código V2 y modelo por defecto (`out_siml_v2_27nov/ks_identidad_defecto.json`) es **byte-idéntica** a `out_seco_a_2026-11-25/ks_sim_vs_seco.json` salvo `sello` (`siml_v2_identidad.py`: `IDENTIDAD OK`). El ajuste reproduce además las D antiguas de la población completa (ETH/SOL/XRP lag 0,0984/0,0614/0,0694), lo que valida la maquinaria de training.

## 3. Ajuste en TRAINING (noche 25-26 Nov, ya vista; etiquetada «training», NO vuelve a validar)
Rejilla declarada antes (ANEXO2 §1): P ∈ {97,00…100,00} paso 0,25 ms (13) × PROC ∈ {0…3} paso 0,5 ms (7) × σ ∈ {0,1,2} ms gauss (3) = 273 puntos; estadístico = D_lag medio ETH/SOL/XRP, población completa con la exclusión declarada; un único juego global; desempate declarado antes (|ΔD|<1e-4 → menor σ, P más cercano a 100, PROC más cercano a 3; n_empatados = 1, no hizo falta). Código `siml_v2_ajuste.py`, salida `out_siml_v2_27nov/ajuste_training.json`.

**Parámetros CONGELADOS** (`siml_v2_params_27nov.json`, sha16 `c58fbbe494b46abd`): **periodo = 100.0 ms, PROC = 1.5 ms, σ = 0 ms**. D_lag medio de training = 0.0267. Defecto (100/3/0): ETH lag 0.0984 / cambios 0.0159; SOL lag 0.0614 / cambios 0.0268; XRP lag 0.0694 / cambios 0.0248;

D de training del juego elegido por contraste (población completa; n sim / n seco = lotes):
| moneda | D lag primero | D cambios/lote | n lotes sim / seco | p50 lag sim / seco (ms) | p90 lag sim / seco (ms) |
|---|---|---|---|---|---|
| ETH | 0.0294 | 0.0162 | 71867 / 9989 | 81.5 / 80.4 | 99.5 / 98.9 |
| SOL | 0.0279 | 0.0268 | 56382 / 6526 | 75.5 / 76.5 | 98.5 / 98.5 |
| XRP | 0.0229 | 0.0249 | 54311 / 6347 | 76.5 / 75.4 | 98.5 / 98.2 |

Seis contrastes < 0,05 en training. Mejores puntos (P, PROC, σ): D_lag medio: (100, 1.5, 0): 0.0267; (99.5, 1.5, 1): 0.0270; (98.25, 2.5, 1): 0.0270; (100, 1.5, 1): 0.0271; (98.25, 2.5, 0): 0.0273; (99.5, 1.5, 0): 0.0274: el valle es plano (varios puntos a <0,001 del mínimo), así que el óptimo es una elección dentro de ese valle, no una cima aguda; el hallazgo robusto es PROC ≈ 1,5-3 con P ≈ 98-100 y σ ≈ 0, no el decimal exacto. Limitaciones declaradas: (i) el reloj del simulador es entero: P/PROC sub-ms se redondean medio ms hacia arriba (`ms_reloj`; en el simulador dec_rx = 2 ms con PROC 1,5, la KS usa dec = 1,5 en el lag y el despertar tras un salto de Binance usa base + 2); (ii) PROC elegido (1,5 ms) es MENOR que los 3 ms del contrato L4: se mide aquí solo por la distribución de lag, no como latencia física del vivo; (iii) población y modelo se eligieron tras ver el training (decisión informada declarada; por eso la noche de validación debe ser nueva).
**Smoke de extremo a extremo en training (NO es validación)**: `siml_valida_v2.py --modelo --poblacion completa` sobre la noche 25-26 simulando de verdad con el modelo congelado (`out_siml_v2_27nov/ks_training_modelo_v2_smoke.json`, sha16 d52284a791d7540c): veredicto PASA; D lag/cambios ETH 0.0294/0.0162, SOL 0.0279/0.0268, XRP 0.0229/0.0249; sensibilidad población restringida a no_armar: FALLA (ETH 0.0293/0.0857, SOL 0.0306/0.0271, XRP 0.0550/0.0374).

## 4. Población del veredicto (declarada tras ver el training)
Ambos lados = TODOS los lotes con ≥1 cambio válido en banda: sim = todos los lotes simulados con cambios del token/mercado dentro de la ventana [fin−300 s, fin−T_STOP] con bid de top en BAND_Q (`--poblacion completa`, sin la restricción «evaluados por no_armar»); seco = decisiones de causa `cadencia`+`binance` de `dec_libro.csv.gz` deduplicadas por (t_dec, slug[, lado]) (todas con n_cambios ≥ 1). Consumo por mercado o por token según detecte el `dec_libro` (como antes). Sensibilidades informativas (NO deciden): población restringida a no_armar (en el smoke de training FALLA: ETH cambios/lote 0,0857, XRP lag 0,055; es el sesgo de selección de la restringida que ya diagnosticó ANEXO2 §1d, no un parámetro arreglable, y por eso no es el veredicto); KS restringida sin excluir el tramo (`sensibilidad_sin_excluir`, hereda la restricción).
Exclusión: la constante `EXCLUSIONES_KS` de `siml_valida_v2.py` (misma que la de `siml_valida_l4.py`: 2026-11-26T00:10-00:20Z; inerte en la noche 27→28 porque queda fuera de su ventana). No se declara ningún tramo nuevo a priori (el crontab de 27-Nov no tiene en 22:35-02:45Z nada pesado: `suelo_p5_directo` corre 03:10Z, el vigía de suelo es ligero a :07). Un tramo posterior solo valdría si estuviera escrito aquí antes; no lo está. Se exige además «sin P1b real vivo» (`exclusion_siml_p1b.exige_sin_p1b_real`, como antes).

## 5. Criterio (inmutable, copiado del PREREG_SIML_26nov §3 y ANEXO2 §1)
PASA = D < 0,05 en los 6 contrastes (ETH/SOL/XRP × lag al primer cambio del lote y cambios por lote) con ≥100 lotes por moneda en sim y seco, seco A COMPLETE con C0/C1 PASA, pins_ok, motor passT_v4, `--version-clase v3.4`. FALLA / INSUFFICIENT / BLOCKED = **A (U(3,103)+3) DEFINITIVA**, sin más rondas con esta familia de modelos. Un solo intento; el único reintento admitido es por fallo de memoria con el mismo entorno (abajo). Si PASA: dec='R' con el modelo congelado pasa a principal en E2 y se re-ejecuta con el sello nuevo; lo demás sigue en A.

## 6. Noche de validación y comando exacto
Noche = seco A de hoy (at 98, 22:35Z, `out_seco_a_2026-11-27`, ventana prevista 27-Nov 22:35Z → 28-Nov ~02:40Z): NO usada en el ajuste ni en la elección de población (el seco se lanza después de firmar este prereg). **Precondiciones de la KS (`siml_valida_v2.main`, BLOCKED si faltan)**: `out_seco_a_2026-11-27/run_manifest.json::estado = COMPLETE`; `manifest_suelo_DIA.json` COMPLETE y cintas `tape_DIA.pkl`/`bad_DIA.json` para los DOS días que cubre el seco (2026-11-27 y 2026-11-28); cobertura horaria ≥0,90. **El día 28 no está cerrado hasta las 00:00Z del 29-Nov** y el suelo de «ayer» lo genera el cron 03:10Z: la KS v2 solo puede lanzarse el **29-Nov tras `manifest_suelo_2026-11-28.json` COMPLETE (≈03:15Z) y las cintas de ambos días**, fuera de 06:00-09:15Z, vía cron_pesado (no «después de las 02:45Z del 28-Nov»: bloquearía por falta de suelo/cinta; un BLOCKED por precondición no consume el intento). Comando (cwd `/root/polymarket-research-dev-bk/experimentos/5m_barato/b_k_ejecutor`):
```
cd /root/polymarket-research-dev-bk/experimentos/5m_barato/b_k_ejecutor && ARROW_DEFAULT_MEMORY_POOL=system MALLOC_ARENA_MAX=2 nice -n 19 ionice -c3 /root/polymarket-research/scripts/cron_pesado.sh bash -c "ulimit -v 12000000; /usr/bin/time -v -o out_seco_a_2026-11-27/ks_v2_pico.txt python3 -I siml_valida_v2.py --seco out_seco_a_2026-11-27 --version-clase v3.4 --modelo siml_v2_params_27nov.json --poblacion completa --l3b-fecha 2026-11-27 --out out_seco_a_2026-11-27/ks_sim_vs_seco_v2.json > out_seco_a_2026-11-27/ks_v2.log 2>&1"
```
Entorno de memoria = el del intento 3 de la KS anterior (completó con pico 4,76 GB; RSS observado 4,76 GB en este training, cap del cgroup de `cron_pesado` ≥5,5 GB necesario: con 4,38 GB el job quedó estrangulado por `memory.high` y se mató, 27-Nov 18:05Z). Se verifica el JSON recién escrito (`veredicto`, `sello`, `modelo_temporal`), nunca el rc. `--l3b-fecha 2026-11-27` fija L3b (no entra en lag ni en cambios por lote; ANEXO2 §1a).

## 7. Ficheros y sha16 (código congelado; calculados al firmar)
| fichero (en `/root/polymarket-research-dev-bk/experimentos/5m_barato/b_k_ejecutor`) | sha16 | qué |
|---|---|---|
| `siml_v2.py` | `a52ce103e265c729` | SIM-L con modelo temporal parametrizable (copia aislada de siml.py) |
| `siml_valida_v2.py` | `9500940bed7b5286` | KS V2 (copia aislada de siml_valida_l4.py; --modelo, --poblacion) |
| `siml_v2_params_27nov.json` | `c58fbbe494b46abd` | parámetros congelados |
| `siml_v2_cache.py` | `7d17bc58a101eb6e` | cache de traza + anclas (training) |
| `siml_v2_ajuste.py` | `f5648eea7766ffdb` | ajuste en rejilla (training) |
| `siml_v2_identidad.py` | `3b335f37f6b02e80` | comparador de identidad end-to-end |
| `siml_v2_check_completa.py` | `aa13f50771d6752a` | comprobación de la rama completa |
| `out_siml_v2_27nov/ajuste_training.json` | `b8e74040c1bf08c3` | salida del ajuste (273 puntos) |
| `out_siml_v2_27nov/ks_identidad_defecto.json` | `da8514a2978ede60` | KS con modelo anterior, sello nuevo |

Tests (en `/root/polymarket-research-dev-bk`):
| fichero | sha16 |
|---|---|
| `test_siml_v2_27nov.py` | `e39f8a4db96bc5eb` |
| `test_siml_v2_sobre_stubs_27nov.py` | `b549db2d3efe2847` |

Sello de la KS v2: `codigo_sha16` = sha16 de `siml_valida_v2.py` y `siml_v2_sha16` = sha16 de `siml_v2.py` dentro de `sello`; si difieren de esta tabla, la KS no vale. Revisión previa pedida: `cheap5m-statistical-validator` (prereg y sha ANTES de las 22:00Z).

## 8. Limitaciones declaradas
Latencia, no EV. La KS no valida SIM-L como predictor de PnL, solo su modelo temporal. Persisten: L3b fallback_59 (no entra en esta KS), libros cruzados no vetados (ANEXO_DESVIACION), PROC físico no identificado (ver §3 ii). Un PASA en una noche es evidencia de una noche (n lotes sim/seco declarados), no de estabilidad: E2 debe seguir etiquetando R como «validado en una noche».

## 9. Enmiendas vinculantes del validador (27-Nov ~18:30Z, antes de las 22:00Z; prevalecen sobre §4-§6)
1. (§5, «Si PASA») E2 con dec='R' usa dec_rx = ms_reloj(1,5) = 2 ms (siml_v2.py:234), ≠ 3 ms de L4: 1 ms optimista para carrera/AS de B. E2 reporta OBLIGATORIAMENTE además la sensibilidad con dec_rx=3 ms. PROC es un parámetro de forma de la distribución de lag, NO latencia física de B; l/RTT/cancelación siguen saliendo SOLO de los ensayos reales vigentes (paquete_l).
2. (§6) Fallo por memoria = no hay JSON con `veredicto` Y `ks_v2.log` muestra OOM / rc 137 / MemoryError → no consume el intento. Cualquier `ks_sim_vs_seco_v2.json` escrito con PASA, FALLA o INSUFFICIENT (o BLOCKED emitido tras simular) CONSUME el intento; si ese JSON ya existe, no se relanza. Ventana: 29-Nov 03:15Z-06:00Z; si no es posible, la siguiente ventana fuera de 06:00-09:15Z y antes de que roten las entradas.
3. (§4) `sensibilidad_sin_excluir` usa la población RESTRINGIDA: no informa sobre la población que decide. La exclusión declarada (25-Nov 00:10-00:20Z) no actúa en la noche 27→28.
4. Acta: el chief registra el sha256 nuevo de este fichero en BRIEFS_COLA_25nov.md antes de las 22:00Z; si no, la validación pasa a la noche siguiente.
