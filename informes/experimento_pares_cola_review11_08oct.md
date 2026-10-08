# experimento_pares_cola_15m.py — 11ª pasada de /code-review (08-Oct ~11:55Z), hallazgos SIN APLICAR

Fichero: `/root/polymarket-research-dev/experimento_pares_cola_15m.py` (rama dev). Reanudar aplicando estos 10, después 12ª pasada.
Copias de cada versión previa: `experimento_v{3..10}_backup.py` (scratchpad de la sesión del 08-Oct; pueden no existir ya: la verdad es el commit de dev).

| # | Línea aprox. | Dinero | Hallazgo | Corrección propuesta |
|---|---|---|---|---|
| 1 | 580 | SÍ | `cancelar()` escribe `cancel_ok` SIN campo `real` y `resolver_inciertas` ignora eventos sin `real` → `t_fuera` nunca se fija → la regla "margen desde la última cancel_ok" no actúa; una incierta queda cobrada para siempre (puede agotar los 5 USDC). | Añadir `"real": self.real` a TODOS los eventos del ledger (cancel_ok, intencion_cancel, cancel_no_confirmada, fuera_libro_fill_desconocido...). |
| 2 | 664 | SÍ | `liquidar()` tiene un 2º camino de cierre para órdenes NO canceladas con estado TERMINAL (cancelada por el exchange) que escribe relleno/liquidada sin `_registrar_cierre` ni asentar 1,5 s. | Tratar TERMINAL no-MATCHED igual que una cancelada propia: mover a `canceladas` con `t_cancel` y cerrar tras ASENTAR_S vía `_registrar_cierre`. |
| 3 | 617 | SÍ | `get_trades(after,before)` sin `maker_address`: no verificado que devuelva rellenos MAKER de la wallet de depósito (signature_type=3, funder). Si no, una incierta llena como maker se cierra con 0. | Verificar con una consulta de solo lectura de un relleno maker real conocido; si no aparece, pasar `maker_address=funder` o no resolver por trades (fail-closed). |
| 4 | 430 | SÍ | 200 con `success:false` y `orderID` != hash: se cancela `h` (inexistente) y la orden real X queda sin control. | Si `orderID` presente y != h → mismo tratamiento que `hash_distinto` (kill + cancelar X). |
| 5 | 462 | SÍ | `consultar()` acepta cualquier dict no vacío: un `{'error': ...}` sin `size_matched`/`status` se lee como relleno 0 conocido. | Exigir `size_matched` presente y numérico (y `status` no vacío); si no → (None, None). |
| 6 | 625 | robustez | `float(size)`/`float(matched_amount)` sin try en `resolver_inciertas`: un trade mal formado tumba el arranque para siempre. | try por trade; si falla alguno de NUESTRO hash → no resolver (sigue incierta). |
| 7 | 339 | CPU | La caché del presupuesto tiene 1 entrada y el bucle alterna YES/NO → nunca acierta. | Cachear fijas/pend del ledger por versión y sumar la candidata después. |
| 8 | 375 | SÍ (bloqueo) | `sin_coste` se sobrescribe en el presupuesto pero es pegajoso en `resolver_inciertas`: presupuesto bloqueado para siempre por una orden que nunca se resuelve. | Misma semántica en ambos (pegajoso con `or`). |
| 9 | 840 | mantenimiento | Emparejado de nuestros hashes contra trades duplicado (resolver_inciertas suma, mercado_fin toma el primero). | Helper `_rellenos_propios(trades, hashes)`. |
| 10 | 712 | limpieza | `self.perdida_otros` calculado y solo registrado (resto del modelo doble). | Quitar o registrar el valor que de verdad usa la compuerta. |
