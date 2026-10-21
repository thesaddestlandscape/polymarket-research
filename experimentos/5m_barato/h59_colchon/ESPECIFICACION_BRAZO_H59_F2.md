# Especificación (SIN aplicar) — brazo sombra H59 en F2 DRY-RUN. v2 corregida 21-Oct-2026 (tras code-review 19:20Z). Etiqueta: DISEÑO / EXPLORATORY
Parche: `f2_h59.patch` (solo AÑADE líneas; `patch -p1 --dry-run` limpio sobre el `f2_5m_barato_dryrun.py` actual) y copia parcheada `f2_5m_barato_dryrun.h59.py`. Tests: `test_f2_h59_parche.py` (10). NO se ha tocado `f2_5m_barato_dryrun.py`, `scripts/f2_5m_barato_lanzar.sh` ni ningún proceso.

## Qué hace el parche (v2)
1. Carga `h59_regla.py` desde UNA sola ruta (`experimentos/5m_barato/h59_colchon/`, `importlib` por ruta; NO se copia a la raíz). Calcula su sha256; si falta o `sha256[:16] != 59c8302df7fe4f73` el brazo H59 queda desactivado (F2 sigue) y lo avisa por stderr. El sha256 completo va en cada `h59_evento`/`h59_relleno`.
2. Tras programar los `v4_relleno`: `if self.mo == "BTC" and n == 1: self._h59(...)` (misma señal V4, solo BTC, 1.ª del cierre).
3. `_h59` NO llama a `_decidir`, NO toma prefirmas (`Armero.tomar`), NO usa el Enviador y no envía: en el hilo del WS solo crea un `_H59Estado` (anota los tops del 5m s con hora de RECEPCIÓN). Todo lo demás corre en el hilo de la agenda: marca durable + `h59_evento` (con `prefirmas_listas_k0.02` leído con `ArmeroProceso.listas`, que no consume).
4. A t0+215 ms (agenda) `h59_relleno`: estado = último top con `t_recv <= t0+215` (nunca posterior, aunque el callback corra tarde; se registran `retraso_callback_ms`, `t_recv_estado`, `edad_llegada_ms`, `hay_top_posterior`). Gate = `H59.evaluar_evento` (nivel 1 todo-o-nada, igual que el vigía). L2 completo solo como diagnóstico y solo si el libro no se tocó tras el límite (`ult_tk`), sobre COPIA del dict (reintentos); si no, `clase=no_exacto_*`.
5. El evento base se loguea siempre antes; cualquier fallo en la llegada queda como `h59_relleno_error` (no se pierde).
6. Idempotencia por cierre: `OUT/h59_marcas_<dia>.txt` (`E|BTC|cierre` al emitir el evento, `R|…` al registrar la llegada). Un F2 reiniciado a mitad de cierre emite `h59_evento_duplicado_omitido` y no repite; al arrancar `_h59_reconciliar` declara (`h59_relleno_perdido_reinicio`) los cierres con E sin R. Lo perdido NO se rellena con ceros: la fuente del gate es el vigía, no F2.

## Cómo lo aplica el chief (reinicio de F2 = sesión principal)
```
cd /root/polymarket-research && patch -p1 < experimentos/5m_barato/h59_colchon/f2_h59.patch      # NO copiar h59_regla.py a la raíz
python3 -m py_compile f2_5m_barato_dryrun.py && (cd experimentos/5m_barato/h59_colchon && nice -n 19 python3 -m pytest -q test_h59.py test_f2_h59_parche.py test_h59_robusto.py)
```
y relanzar F2 con `scripts/f2_5m_barato_lanzar.sh` (no editado). F2 no está en `observadores` ni en el watchdog. `/code-review` MEDIUM del diff de F2 antes de aplicar (no toca `ejecutor_rapido.py`).

## Vigía (cron): llamar al ENVOLTORIO, no al congelado
`vigia_5m_barato_h59_robusto.py procesar|informe` (mismo uso; el congelado `vigia_5m_barato_h59_forward.py` queda intacto y hashea igual). Ver INFORME_CORRECCIONES.md.

## Conciliación (a ampliar en `analisis_f2_5m_barato.py`, no hecho)
Por cierre: `h59_evento` de F2 vs `entradas_D.csv.gz` del vigía (`t0`, `ask0`, `plim`, límites, `ask_llegada`, `asz_llegada`, clase de k=0,02): aceptación ≥ 95 % de cierres con la misma decisión, |Δt0| mediana ≤ 5 ms, misma clase de relleno ≥ 90 %. Las diferencias se auditan una a una. Como el brazo ya no envía, F2 NO mide el decisión→envío de H59 (lo mide V4, mismo camino caliente); el EV del gate sale del vigía (registro ms).
