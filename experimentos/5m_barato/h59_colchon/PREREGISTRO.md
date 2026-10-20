# PREREGISTRO H59 — V4 como TOMADOR con colchón de 2c (forward DRY-RUN). Congelado 2026-10-20T19:05Z. Estado: EXPLORATORY
Origen: `experimentos/5m_barato/v4_captura_maker/informe.md` §1 (alpha-researcher, 20-Oct; descubrimiento BTC 06-18 Oct) y REGISTRO_HIPOTESIS «propuestas del alpha-researcher» (H59). Autorización: Javi, 20-Oct (solo dry-run/forward, sin dinero, sin órdenes).
Hash de congelación (código + config + hash de V4): `ea3789bafdc70764`; hashes por fichero en `preregistro.json`. Cambiar cualquiera = versión nueva + OOS nuevo.

## 1. Regla congelada (una sola hipótesis: k = +0,02)
- **Universo:** BTC, par anidado 5m/15m de cada cierre (múltiplo de 900 s), lado s por TWAP60 oficiales, |gap| ≥ 1 bp. Primera señal de cada cierre.
- **Disparo:** exactamente el de V4 (`vigia_5m_barato_forward.py`, hash_config 77a75859ae5cf22e, importado, no editado): margen_neto = bid15(s) − ask5(s) − 0,07·p(1−p), **redondeado a 4 decimales**, ≥ 0,05; libro no cruzado en ninguna pata; ventana [C−300 s + 1,5 s, C − 10 s); hora de RECEPCIÓN de la fila q.
- **Orden virtual (FOK):** llega a t0 + 215 ms. Límite = `p_limite(bid15(t0)) + 0,02` (rejilla 1 c, tope 0,99). Acciones = `max(5, ceil(2/límite·100)/100)` (= `tam_orden` de F2, la orden prefirmada real; stake nominal 2 €/5 acc).
- **Relleno:** estado = última fila q con recepción ≤ t0+215 ms (nunca posterior). Llena si `ask_llegada ≤ límite` **y** `tamaño del nivel 1 ≥ acciones` (FOK todo-o-nada, solo nivel 1: conservador). Si el precio cabe pero el nivel tiene menos acciones → `corte_tamano`, sin relleno. Precio = ask a la llegada (no el límite). Libro de llegada con >60 s → `UNKNOWN` (no cuenta).
- **PnL:** acc·(pago − precio − fee(precio)); coste = acc·(precio + fee). Desenlace OFICIAL (gamma closed) por mercado; desenlace ausente = pendiente, nunca 0.
- **Colchones registrados pero DESCRIPTIVOS:** 0, 0,01, 0,03, 0,05 (no cuentan para el gate). k=0 es además el brazo emparejado «V4 nivel 1 todo-o-nada».
- **OOS:** disparos con `t0 ≥ 2026-10-20T19:05Z`. Nada anterior entra en el gate (el descubrimiento 06-18 Oct no cuenta).

## 2. Multiplicidad y estimaciones
- En el descubrimiento se probaron **5 colchones: 0; 0,01; 0,02; 0,03; 0,05**. **k = 0,02 se eligió a posteriori** (el mejor), así que n=20 / EV +1,17 / IC90 (+0,37;+2,30) / +0,575 sin 2 mejores días están afectados por maldición del ganador y NO son la expectativa del forward. Las 8 operaciones añadidas por el colchón ganan 7 (8 observaciones).
- Diferencias deliberadas de este preregistro frente al descubrimiento (m3_profundidad.py): (a) FOK todo-o-nada, sin rellenos parciales; (b) acciones por el límite, no por el ask de llegada; (c) estado del libro por recepción ≤ t0+215. **No se ha re-ejecutado el descubrimiento con estas reglas**; el validador debe hacerlo antes de leer nada del forward.
- El forward evalúa UNA hipótesis (k=0,02): no necesita corrección adicional dentro del forward; los otros k son descriptivos y cualquier afirmación sobre otro k exige versión nueva.

## 3. Gate (todos a la vez, sobre OOS, k = 0,02) — no se retoca
n ≥ 40 ejecutables · ≥ 10 días UTC con operación · EV ponderado por € ≥ +0,10 · IC90 por días (bootstrap, 4000, semilla fija) inferior > 0 · EV sin los 2 mejores días > 0 · EV sin el 5 % mejor de operaciones (⌈5 %·n⌉, mín. 1) > 0. Se informa además IC90 por cierre, g log a f=10 % (payout inverso), % PnL del mejor día y la comparación emparejada con k=0.
**Calendario de miradas (propuesto, el chief puede cambiarlo antes de ejecutar):** veredicto formal en el primer informe con n ≥ 40 y ≥ 10 días; si PENDIENTE y sin kill, una única relectura a n = 60 y otra a n = 80; después, cierre como «no concluyente». Sin más miradas con consecuencias (los informes diarios son descriptivos).
Potencia (aviso): con payoffs binarios (σ por € ≈ 1), n = 40 solo supera «IC90 por días > 0» si el EV verdadero es ≳ +0,3; con un EV verdadero de +0,10 el gate casi nunca pasa en n=40 y no pasar NO equivale a refutar.
**Kill de hipótesis (no es interruptor de dinero):** EV pond < −0,15 con n ≥ 25 · IC90 por cierre superior < 0 con n ≥ 20 · incrementales (llenan con k=0,02 y no con k=0) con EV pond < −0,15 y n ≥ 10.
Estado superado = `GATE_SUPERADO_pasa_a_revision` (validador independiente + red-team); no autoriza dinero.

## 4. Ritmo esperado (fuente: `DL/vigia_5m_barato/eventos_2026-10-12..19.csv`, V4 BTC 1.ª señal)
13 señales en 8 días (1,6/día; 2 de 8 días sin señal), 7 llenaban con k=0. Descubrimiento: 20 ejecutables en 13 días con colchón (~1,5/día, con parciales). Con la regla estricta se espera **1,2–2 ejecutables/día**. n = 40 ≈ **9-Nov (2/día) · 16-Nov (1,5/día) · 22-Nov (1,2/día)**; 10 días con operación se alcanza antes. Primera lectura formal esperada ≈ 16-Nov (±1 semana). Los días de sequía (BTC sin señal) son normales; V4/V7 mostraron regímenes de varios días sin eventos.

## 5. Solapamientos y limitaciones
- Misma señal que V4: NO es PnL aditivo con V4 (H59 reemplaza a V4 en ese cierre). Canibaliza a H53/H56 (dispara antes con límite = ask(t)); no sumar en el libro.
- Nivel 1 solo (las filas `l` de 3 niveles no se usan): subestima rellenos que necesitan niveles 2-3. El brazo sombra F2 registra además el L2 completo (diagnóstico, no gate).
- Selección adversa: el colchón compra más caro donde el ask se movió; el control es la comparación emparejada con k=0 y el EV de las incrementales.
- Capital: 5 acciones a ~0,45 = ~2,3-2,7 €/operación (>2 € nominal, ≈ stake máx. live); dinero real requeriría decisión de Javi y rampa.

## 6. Artefactos y reproducción
Código (dev, sin commits): `experimentos/5m_barato/h59_colchon/{h59_regla,h59_stats,h59_lectura,vigia_5m_barato_h59_forward}.py`, tests `test_h59.py`, `test_f2_h59_parche.py`. Salidas: `/root/polymarket-research-datalogs/vigia_5m_barato_h59/` (entradas_D.csv.gz con clave única `cierre`, entradas_D.meta.json, calidad_D.csv, manifiesto.json, runs/run_*.json, informe.json/txt).
```
cd /root/polymarket-research/experimentos/5m_barato/h59_colchon
(ulimit -v 3000000; nice -n 19 ionice -c3 python3 -I vigia_5m_barato_h59_forward.py procesar --dia 2026-10-20)   # reintentable; --forzar recalcula
nice -n 19 python3 -I vigia_5m_barato_h59_forward.py informe              # --telegram solo con orden
nice -n 19 python3 -m pytest -q test_h59.py test_f2_h59_parche.py
```
Registro ms: retención 4 días (`maker_ms_*`); un día que no se procese antes de rotar queda BLOCKED (no se rellena con ceros).

## 7. Propuesta de cron (NO instalada; fuera de 06-09Z y 22:15-22:30Z)
```
50 2 * * * flock -n /tmp/vigia_5m_barato_h59.lock bash -c "ulimit -v 3000000; cd /root/polymarket-research/experimentos/5m_barato/h59_colchon && nice -n 19 ionice -c3 /usr/bin/python3 -I vigia_5m_barato_h59_forward.py procesar && nice -n 19 /usr/bin/python3 -I vigia_5m_barato_h59_forward.py informe || /usr/bin/python3 -c 'import sys; sys.path.insert(0,\"/root/polymarket-research\"); from shadow_digest import enviar_telegram as e; e(\"🚨 Vigía H59 FALLÓ: ver logs/vigia_5m_barato_h59.log\")'" >> /root/polymarket-research/logs/vigia_5m_barato_h59.log 2>&1
```
02:50Z: tras el cron 02:30 de V5/V6 (`run_m5barato_forward_diario.sh`) y antes del restart de RAM 03:20 y de la extracción 03:50; procesa el día anterior (necesita los ficheros ms de D y D+1). Informe sin Telegram (se lee a mano o se añade `--telegram` cuando el chief lo ordene). Antes de instalar: comprobar MemAvailable (el proceso lee un día de BTC con numpy: ≲1 GB) y que el `ulimit -v` del cron no rompa numpy (probado con 3 GB en tests, no con un día real).
