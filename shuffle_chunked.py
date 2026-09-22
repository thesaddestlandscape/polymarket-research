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


def t_permutacion_chunked(rng, dentro, fuera, b: int) -> np.ndarray:
    """Version por bloques de `permutar_t_vectorizado`
    (analisis_romano_wolf_gate_bucket_12ago.py): mismo t-estadistico de dos
    muestras (Welch) bajo H0, bit-identico a la version de una sola matriz
    (b, n) porque el generador se consume en el mismo orden por bloques."""
    dentro = np.asarray(dentro, dtype=np.float64)
    fuera = np.asarray(fuera, dtype=np.float64)
    n_d, n_f = len(dentro), len(fuera)
    pool = np.concatenate([dentro, fuera])
    n = n_d + n_f
    filas = max(1, CHUNK_ELEMS // max(n, 1))
    out = np.empty(b, dtype=np.float64)
    hecho = 0
    while hecho < b:
        c = min(filas, b - hecho)
        idx = rng.random((c, n)).argsort(axis=1)
        permutado = pool[idx]
        grupo_d = permutado[:, :n_d]
        grupo_f = permutado[:, n_d:]
        media_d = grupo_d.mean(axis=1)
        media_f = grupo_f.mean(axis=1)
        var_d = grupo_d.var(axis=1, ddof=1) if n_d > 1 else np.zeros(c)
        var_f = grupo_f.var(axis=1, ddof=1) if n_f > 1 else np.zeros(c)
        se = np.sqrt(var_d / n_d + var_f / n_f)
        se[se == 0] = np.nan
        out[hecho:hecho + c] = (media_d - media_f) / se
        hecho += c
    return out


def corr_permutacion_chunked(rng, stakes, aciertos, iters: int) -> np.ndarray:
    """Version por bloques de `correlacion_shuffle`
    (analisis_gate_despineo_stake_28jul.py): correlacion de Pearson entre
    `stakes` (fijo) y `aciertos` permutado, bajo H0. Bit-identica a la
    version de una sola matriz (iters, n)."""
    stakes = np.asarray(stakes, dtype=np.float64)
    aciertos = np.asarray(aciertos, dtype=np.float64)
    n = len(stakes)
    stakes_c = stakes - stakes.mean()
    std_stake = stakes_c.std()
    filas = max(1, CHUNK_ELEMS // max(n, 1))
    out = np.empty(iters, dtype=np.float64)
    hecho = 0
    while hecho < iters:
        c = min(filas, iters - hecho)
        idx = rng.random((c, n)).argsort(axis=1)
        aciertos_perm = aciertos[idx]
        aciertos_perm_c = aciertos_perm - aciertos_perm.mean(axis=1, keepdims=True)
        cov = (stakes_c[None, :] * aciertos_perm_c).sum(axis=1)
        std_prod = std_stake * aciertos_perm_c.std(axis=1) * n
        with np.errstate(divide="ignore", invalid="ignore"):
            out[hecho:hecho + c] = np.where(std_prod > 0, cov / std_prod, 0.0)
        hecho += c
    return out
