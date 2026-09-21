#!/usr/bin/env python3
"""shuffle_chunked.py -- test de permutacion por bloques (21-Sep, causa raiz
de OOM en los vigias de gates).

Las copias de shuffle_test() hacian `rng.random((iters, n)).argsort(axis=1)`
y `todos[idx]`: TRES matrices de iters x n vivas a la vez. Con iters=2000 y
n de decenas de miles son varios GB (medido: analisis_wallet_mirror_gate_
bucket_10ago.py llego a 4,7GB RSS y 22min antes de morir por OOM, 81
ejecuciones seguidas del vigia sin regenerar el JSON que lee el ejecutor real).

Aqui se procesa por bloques de filas. El generador se consume en el MISMO
orden (Generator.random rellena en orden C, un float64 por salida), asi que
el resultado es bit-identico al de una sola llamada de iters x n -- verificado
en verificar_shuffle_chunked() y por el test de equivalencia de la sesion."""
import numpy as np

# ~4M elementos por matriz temporal (32MB en float64/int64) => pico ~100MB
# independientemente de n, en vez de 3 x iters x n x 8 bytes.
CHUNK_ELEMS = 4_000_000


def diffs_permutacion(rng, todos, na: int, iters: int) -> np.ndarray:
    """Devuelve el array (iters,) de media_a - media_b para `iters`
    permutaciones de `todos`, con las primeras `na` posiciones como grupo a."""
    todos = np.asarray(todos, dtype=np.float64)
    n = len(todos)
    filas = max(1, CHUNK_ELEMS // max(n, 1))
    out = np.empty(iters, dtype=np.float64)
    hecho = 0
    while hecho < iters:
        c = min(filas, iters - hecho)
        idx = rng.random((c, n)).argsort(axis=1)
        permutado = todos[idx]
        out[hecho:hecho + c] = permutado[:, :na].mean(axis=1) - permutado[:, na:].mean(axis=1)
        hecho += c
    return out
