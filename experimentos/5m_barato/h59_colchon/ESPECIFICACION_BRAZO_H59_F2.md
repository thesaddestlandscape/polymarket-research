# Especificación (SIN aplicar) — brazo sombra H59 en F2 DRY-RUN. 20-Oct-2026. Etiqueta: DISEÑO / EXPLORATORY
Parche listo y probado en dev: `f2_h59.patch` (41 líneas, solo AÑADE; `patch -p1 --dry-run` limpio sobre el `f2_5m_barato_dryrun.py` de hoy) y la copia parcheada `f2_5m_barato_dryrun.h59.py` (compila). Tests con libro simulado: `test_f2_h59_parche.py` (3 pruebas, pasan). NO se ha tocado `f2_5m_barato_dryrun.py`, `scripts/f2_5m_barato_lanzar.sh` ni ningún proceso.

## Qué hace el parche
1. `import h59_regla as H59` junto a V7 (la regla vive solo en `h59_regla.py`; importa `vigia_5m_barato_forward` ya cargado por F2 como `V`). **Copiar `experimentos/5m_barato/h59_colchon/h59_regla.py` a la raíz del repo** (idéntico bit a bit: comparar sha256 con el de `preregistro.json`; el hash del vigía H59 cubre la copia de la carpeta). `h59_regla` localiza la raíz buscando `vigia_5m_barato_forward.py`, funciona en ambos sitios.
2. En `Par.al_cambiar`, justo tras programar los `v4_relleno`: `if self.mo == "BTC" and n == 1: self._h59(t, ask0, bid_o, qc)` → misma señal V4 (cero lógica de disparo nueva), solo BTC, solo la 1.ª señal del cierre.
3. `Par._h59`: calcula los límites FOK de los 5 colchones (`H59.limite_fok`); llama a `self._decidir("H59", t, límite_k0,02, {"n": 1})` (mismo camino que v4: orden prefirmada de la rejilla 0,01..0,99 + `Enviador` DRY-RUN → mide decisión→envío del brazo; el tamaño `H59.acciones_objetivo` = `tam_orden` de F2, comprobado en test); registra `h59_evento` (ask5, tamaño del nivel 1 en t0, bid15, margen, límites por k, tiempos de decisión).
4. A t0+215 ms por `agenda.en`: lee el nivel 1 vigente del WS propio y registra `h59_relleno` con, por cada k, `H59.evaluar_evento` (clase llena / repreciado / corte_tamano / sin_libro / UNKNOWN, acciones, precio) y, como diagnóstico, el relleno L2 completo (`relleno(...)`, que sí admite niveles 2-3 y parciales). El gate usa solo el nivel 1 todo-o-nada (idéntico al vigía).
5. Seguridad: el parche solo añade líneas (test), no añade ningún envío (`_decidir` ya es el Enviador DRY-RUN existente), no cambia constantes ni el flujo v4/V7.

## Cómo lo aplica el chief (reinicio de F2 = sesión principal)
```
cd /root/polymarket-research && cp experimentos/5m_barato/h59_colchon/h59_regla.py . && patch -p1 < experimentos/5m_barato/h59_colchon/f2_h59.patch
python3 -m py_compile f2_5m_barato_dryrun.py h59_regla.py && (cd experimentos/5m_barato/h59_colchon && python3 -m pytest -q test_h59.py test_f2_h59_parche.py)
```
y relanzar F2 con `scripts/f2_5m_barato_lanzar.sh` (no editado). F2 no está en `observadores` ni en el watchdog: el reinicio no afecta al histórico ms. `/code-review` MEDIUM del diff de F2 antes de aplicar (no toca `ejecutor_rapido.py`).

## Conciliación (a ampliar en `analisis_f2_5m_barato.py`, no hecho)
Por cierre: `h59_evento` de F2 vs `entradas_D.csv.gz` del vigía (`t0`, `ask0`, `plim`, límites, `ask_llegada`, `asz_llegada`, clase de k=0,02): aceptación ≥ 95 % de cierres con la misma decisión, |Δt0| mediana ≤ 5 ms, misma clase de relleno ≥ 90 %. Las diferencias se auditan una a una. F2 es gemelo para medir latencia decisión→envío; el EV del gate sale del vigía (registro ms).
