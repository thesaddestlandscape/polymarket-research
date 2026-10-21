# H59 — correcciones del /code-review (hallazgos 1-10) · 21-Oct-2026 · DRY-RUN, nada aplicado a F2, ningún proceso tocado
Congelación INTACTA: `vigia_5m_barato_h59_forward.py`, `h59_regla.py`, `h59_stats.py`, `h59_lectura.py` byte a byte (test), `hash_codigo()` = `ea3789bafdc70764`, V4 `77a75859ae5cf22e`. Ningún arreglo exigió tocar la regla: los del vigía van en un ENVOLTORIO nuevo (`vigia_5m_barato_h59_robusto.py`, que importa la regla del congelado), los de F2 en el parche. 37 tests pasan (`test_h59.py`, `test_f2_h59_parche.py` 10, `test_h59_robusto.py` 12).

| # | Hallazgo → cambio → test |
|---|---|
| 1 | Brazo consumía prefirmas de V4 y enviaba inline → `_h59` ya no usa `_decidir`/`Armero.tomar`/Enviador (solo lee `listas()`, que no consume); trabajo pesado en el hilo de la agenda → `test_h59_no_consume_prefirmas_ni_envia…` (V4 hace 1 `tomar` con 0,43; el enviador solo ve `v4`) |
| 2 | `llegada()` leía `lib.top` al ejecutarse → `_H59Estado` anota tops por RECEPCIÓN; estado = último con `t_recv <= t0+215` → `test_llegada_usa_el_ultimo_top…` (un top a +300 ms con el callback tarde no cuenta; se loguea `retraso_callback_ms`) |
| 3 | Iterar el dict vivo del WS; evento base → L2 sobre copia con reintentos y solo si el libro no se tocó tras el límite; evento base antes y `h59_relleno_error` si falla → `test_l2_copia_…`, `test_un_fallo_en_la_llegada…` |
| 4 | Dos copias de `h59_regla.py` → una sola ruta (carpeta, `importlib`), NO copiar a la raíz; sha256 completo en cada evento; sha ≠ `59c8302df7fe4f73` ⇒ brazo desactivado (fail-closed) → `test_la_regla_se_importa_de_una_sola_ruta…` |
| 5 | Reinicio duplica evento/pierde llegada → marcas durables `E`/`R` por cierre; duplicado omitido; `h59_relleno_perdido_reinicio` al arrancar → `test_reinicio_no_duplica…`, `test_reconciliar_ignora…` |
| 6 | COMPLETE con truncados/abiertos y «ya procesado» sin comprobar ficheros → COMPLETE solo con día terminado + 96/96 cierres + última fila q a ≤60 s de 24:00Z; truncados y abiertos quedan en el meta; «ya procesado» exige (tamaño, mtime_ns) iguales en los ficheros de D y ninguno nuevo (los de D+1 crecen y no cuentan) → `test_complete_exige…`, `test_fichero_truncado…`, `test_ya_procesado_se_revalida…` |
| 7 | `k,` en el fichero del día anterior → si faltan cierres se relee con D-1 (`usado_dia_previo`); si siguen faltando, PARTIAL con motivo → `test_mercado_con_la_linea_k…` |
| 8 | Gate con PARTIAL / sin pendientes → el gate solo usa días COMPLETE verificados por el envoltorio (un día del congelado a pelo no entra); llenas sin desenlace oficial ⇒ `PENDIENTE_DESENLACES` (nunca se evalúa el gate) → `test_el_gate_solo_cuenta…`, `test_dia_procesado_por_el_vigia_congelado…` |
| 9 | Env que sustituye datos sin constancia → `entorno_no_estandar` (con sha256 de `M5B_DES`) en meta, run, informe.json/txt y veredicto `NO_VALIDO_ENTORNO_SUSTITUIDO:*` → `test_entorno_sustituido…` |
| 10 | `manifiesto.json` sin flock → `flock` exclusivo `SAL/h59.lock` alrededor de procesar e informe → `test_bloqueo_exclusivo…`, `test_manifiesto_atomico…` |
Equivalencia: con datos completos el envoltorio escribe EXACTAMENTE el mismo `entradas_D.csv.gz` que el congelado (`test_misma_salida_que_el_vigia_congelado…`).

## Para el chief
- Cron: sustituir en PREREGISTRO §7 `vigia_5m_barato_h59_forward.py` por `vigia_5m_barato_h59_robusto.py` (mismos subcomandos). F2: `patch -p1 < f2_h59.patch` (dry-run limpio), sin copiar nada a la raíz; `/code-review` del diff nuevo antes de aplicar.
- Hashes nuevos (no cubiertos por la congelación): patch `5c3bf6691fd77978`, F2 parcheado `0b6d13372cddc432`, envoltorio `793ea6395dbe31aa`, tests `34a3b80cf160483e`/`6ab051177b712808` (el `preregistro.json` conserva los antiguos del patch/test_f2: sin editar a propósito).

## Abierto
- Hueco interior por reinicio de `observadores` (los `.gz` se truncan al matar el proceso: confirmado con `gzip -t` en 2 ficheros del 20-Oct): se registra pero NO se mide el hueco por cierre; un cierre con ms perdidos entra con `edad_llegada_ms` alta. Propuesta: medir huecos q por ventana antes del primer informe.
- COMPLETE estricto (96/96) puede dejar fuera días con un mercado faltante; decide el chief si se relaja (cambia solo el envoltorio, no la regla).
- No probado con un día real (necesita ≈1 GB y fuera de 06-09Z; load actual 20). Primer `procesar --dia 2026-10-20` por el chief tras 00:10Z, de noche.
- Fuera de alcance, observado: `relleno()` de F2 (usado por `v4_relleno`) itera `lib.lib[tk]['asks']` vivo; la `agenda` traga el RuntimeError y se pierde esa fila de V4. No se ha tocado (F2 en marcha).
- El brazo F2 ya no mide decisión→envío de H59 (no envía); lo mide V4.
