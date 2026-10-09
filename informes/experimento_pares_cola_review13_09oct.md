# experimento_pares_cola_15m.py — 13ª pasada de /code-review (09-Oct ~07:30Z), hallazgos SIN APLICAR

Fichero: `/root/polymarket-research-dev/experimento_pares_cola_15m.py`, commit de dev `89cd168af5` (aplica los 10 de la 12ª).

| # | Línea | Dinero | Hallazgo | Corrección propuesta |
|---|---|---|---|---|
| 3 | 964 | SÍ | verif_trades_maker puede ver en /trades MÁS relleno que el registrado y solo lo anota: el presupuesto se queda con el menor | en mercado_fin, si /trades > ledger -> escribir `relleno` corrector (máximo) |
| 4 | 765 | SÍ | cancelada propia / del exchange se cierra con UNA lectura de size_matched a +1,5 s; si va retrasada, el coste queda corto para siempre | misma reconciliación final con /trades (#3) + reconciliación en el arranque de las liquidadas de los últimos N min |
| 1 | 645 | SÍ (orden ajena) | resolver_pendientes_ledger no mira `no_tocar`: si el proceso muere entre intencion_post(oid) y cerrada_incierta(oid), el reinicio cancela un oid no verificado | respetar `no_tocar` también ahí (y escribir ambas líneas con fsync) |
| 6 | 528 | SÍ (orden ajena) | la verificación de propiedad (token, lado, precio, tamaño, hora) no distingue una orden igual de otro proceso de la wallet compartida | no hay forma fiable con esos campos: ver decisión de diseño abajo |
| 2 | 520 | SÍ | `_oid_es_nuestra` lee las abiertas una vez sin reintento: una orden nuestra aún sin indexar queda no_tocar, viva y sin control hasta el cierre del mercado | reintentos (p. ej. 3 × 0,5 s) |
| 7 | 488 | presupuesto | rama verificada: h y oid cuentan las dos (doble presupuesto) y pueden duplicar la medición | contar una sola vez el par (h, oid) |
| 8 | 481 | SÍ | `oid.lower()` revienta si orderID no es str: la orden real queda sin registrar | `oid = str(oid)` si no es None; tipo raro -> incierta + kill |
| 9 | 410 | SÍ | `relleno` con acc_total=None cuenta como 0 conocido (el `or 0` evita el fallback); post_rechazada trata la incertidumbre distinto en los dos sitios | acc_total ausente -> llena entera; misma regla en ambos |
| 5 | 937 | robustez | la 2ª pasada del finally puede dejar otra cancelada sin cerrar (el #7 de la 12ª, un nivel más abajo) | bucle hasta vaciar las canceladas del mercado (con tope de tiempo) |
| 10 | 520 | reutilización | `_oid_es_nuestra` duplica la consulta de abiertas de `_ausente_de_abiertas` | helper común |

**Decisión de diseño para Javi:** la rama "orderID ≠ hash calculado" ha generado hallazgos en 4 pasadas seguidas y no
tiene solución limpia en una wallet compartida (o se toca una orden que podría ser ajena, o se deja viva una que podría
ser nuestra). Hasta hoy el hash coincidió siempre. Propuesta: comprobar ANTES de operar, con una única orden de prueba
lejos del precio (coste 0) si el hash coincide; y si en operación aparece un descuadre, NO tocar el oid, kill, y contarlo
como llena (peor caso acotado: 5 × precio ≤ 4 $, dentro de los 5 USDC).
