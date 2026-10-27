# ANEXO AL PREREG - sets congelados (construidos 24-Oct-2026 ~09:50Z con `scripts/build_set.py`, datos 09..23-Oct)
PREREG.md sha256 (antes de construir): f48526f98f030901cd7086e2c7c74d706162336b9a9d4961ae46af71bdf1b3a7
Hash = sha256 de los tomadores ordenados, uno por linea con salto final (`cf_lib.sha256_lines`); ficheros en `datos/`.
- SET_I (primario): n=837 tomadores, sha256 `1466a608b4e4334d6a377bceebccc0e947c345124a69fc124973d522413a63fb`
- SET_V (replica verificador, 09..18): n=370 (coincide con los 370 de `verificacion/v3_stdout.txt`), sha256 `ac7d6a0b23706c5d5b1945a9aaf3eadb2b5fcc17add373279ea56182aec77d02`
- POOL_I (placebo): n=3.001, sha256 `16f019e9d658fc99b7e6b17d2903ade824fe7ff8f0b126d80b17efe64a7a815c`
- Interseccion I∩V = 302. `cf_diario.py` aborta si algun hash no coincide.
Nota 1: SET_I flags 837 de 3.001 tomadores (28 %): el umbral n>=30 deja entrar mucho ruido de muestra pequena (winner's curse); es la definicion pedida y se evalua tal cual.
Nota 2 (construccion en 2 pasadas, ANTES de cualquier evaluacion oficial): la 1.a pasada uso solo `maker_ms_desenlaces_cache.json`, que no cubria el 22-Oct (821 de 867 mercados sin desenlace) -> set_I n=837 con hash 323ebd32... y pool 2.919, DESCARTADA. La 2.a anade como relleno `precierre_desenlaces_cache.json` (slug->Up/Down, Up==YES; 0 discrepancias en 1.772 mercados comparables del 22-Oct) y rehace solo el 22 y 23-Oct. SET_V (09..18) no cambia. Mismos criterios; no se vio ningun resultado de B con ninguno de los dos sets antes de fijar el definitivo, salvo un dry-run del script (descartado).
