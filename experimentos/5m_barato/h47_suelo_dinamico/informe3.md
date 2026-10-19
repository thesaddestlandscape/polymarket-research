# H47 — 3ª /code-review medium: 10 hallazgos aplicados (19-Oct)
Repo dev `/root/polymarket-research-dev`, commit `75a60b7d52` sobre `ea1fa2aa1c` (solo `experimento_maker_h47.py` y su test). Sin órdenes, sin cliente CLOB, sin .env. Diff: `git diff ea1fa2aa1c HEAD`.
Tests: `/root/polymarket-research/.venv/bin/python -m pytest -q test_experimento_maker_h47.py` -> 103 passed (90 + 13 nuevos). Mutaciones (copia en scratchpad): 18, 17 matadas, 1 equivalente (`--rearmar-kill` con truthiness: ya lo cubre la validación de motivo vacío).
1 [alto] `--reiniciar-suelo`, `--aceptar-linea-ilegible` y `--rearmar-kill` se comprueban con `is not None`; motivo vacío o en blanco -> error, nunca arranca un real. Las tres son excluyentes.
2 [alto] El reseteo verifica el saldo (si no se puede, no reinicia) y guarda `saldo_base`: `_saldo_inicial()` toma esa base del último `suelo_reiniciado` y `cuadre()` solo explica las órdenes con `t_int` posterior al evento (la hecha antes ya está en el saldo base). Harness sin tocar.
3 [alto] El CLI de reseteo/aceptación toma `X.LOCK` y `LOCK_PARES` (como el camino real); con pares activo sale.
4 [alto] Nuevo `--aceptar-linea-ilegible "motivo"`: evento `linea_ilegible_aceptada` (sha + fichero, wallet exacta, fsync, confirmación escrita) que NO descarta suelos válidos; el reseteo completo queda aparte.
5 [alto] `saldo()` (usado por puede_enviar, cuadre y vigilar) usa `saldo_con_bloque` con edad <= 60 s y bloque >= último visto; si no, `lectura_saldo_rechazada` y saldo ilegible (fail-closed).
6 [medio] La 2ª lectura del arranque exige bloque ESTRICTAMENTE mayor; espera de 2,5 s entre lecturas (> 1 bloque).
7 [alto] Si `suelo_subido` no llega a disco: kill, False y nada cambia en memoria (saldo_min/hwm intactos). El disponible usa min(saldo, pico confirmado).
8 [medio] El alza pendiente caduca a los 10 s, exige una 2ª lectura de bloque más nuevo (>= 2 s) y una lectura ilegible la anula.
9 [bajo] Un solo escaneo en streaming por arranque, reutilizado para tope de órdenes, base del cuadre y suelos.
10 [medio] Ledger ilegible: `n_ordenes_total` = tope (no se envía) y `suelo_no_fijado` registrado con el motivo.
Límites: (a) reseteo y aceptación se han de hacer con nada abierto en el exchange (una orden anterior que rellene después se tomaría como pérdida sin explicar y haría kill). (b) Aceptar una línea pierde lo que decía; un suelo_* cortado no llegó a usarse porque se escribe ANTES de la orden. (c) Con RPC con bloques desordenados entre nodos, las lecturas se rechazan hasta que avancen (fail-closed, para a los 2 min). (d) `import subprocess` sin usar, preexistente.
