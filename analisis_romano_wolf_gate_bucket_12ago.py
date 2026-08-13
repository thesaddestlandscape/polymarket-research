#!/usr/bin/env python3
"""
analisis_romano_wolf_gate_bucket_12ago.py — prototipo Romano-Wolf stepdown
(pendiente 12-Ago, idea_romano_wolf_ras_bounds_multiples_tests_12ago).
Puramente analítico, NO toca producción ni gate_bucket_propio.json.

Compara la corrección BH-FDR (por familia+moneda) que ya usa
`analisis_gate_bucket_propio_28jul.py` contra Romano-Wolf stepdown
(FWER, controla la probabilidad de tener SIQUIERA UN falso positivo,
más estricta que BH-FDR que controla la PROPORCIÓN esperada) aplicado
GLOBALMENTE sobre TODOS los tests a la vez (el corte más duro posible,
sin trocear por familia).

Método (mismo test base que gate_bucket_propio: diff de pnl_neto entre
el bucket y el "resto" de la misma tupla, permutación):
  1. Reconstruye los mismos ~397 tests (n>=15 en ambos grupos) desde
     results.csv, con el mismo filtro TWAP.
  2. Para cada test, calcula el t-estadístico observado (diferencia de
     medias estandarizada por el error estándar combinado -- pone todos
     los tests en una escala comparable, necesario para el paso 3).
  3. Para B réplicas: permuta CADA bucket por separado (pool
     dentro+fuera, split aleatorio del mismo tamaño) y calcula su
     t-estadístico permutado -- construye una matriz (B, K).
  4. Stepdown Romano-Wolf: ordena los tests por |t_obs| descendente;
     para el más extremo, compara contra el cuantil (1-alpha) del máximo
     |t| ACTIVO (todos los tests aún no rechazados) en cada réplica; si
     lo supera, se rechaza (Romano-Wolf-significativo) y se quita del
     conjunto activo; se repite con el siguiente. Para en el primer test
     que NO supere el umbral (monótono: los siguientes tampoco lo harían).

Salida: tabla comparando BH-FDR (ya en gate_bucket_propio.json) vs
Romano-Wolf, y cuántos de los 16 veredictos actuales sobreviven.
"""
import csv
import json
import math
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kelly_precio_gate import _familia  # noqa: E402
from analisis_gate_bucket_propio_28jul import (  # noqa: E402
    cargar_tuplas_live, cargar_filas, bucket, N_MIN,
)

REPO = Path(__file__).resolve().parent
GATE_ACTUAL = REPO / "data" / "shadow" / "gate_bucket_propio.json"

B = 2000  # réplicas de permutación conjunta
ALPHA = 0.05
_rng = np.random.default_rng(123)


def t_estadistico(dentro: np.ndarray, fuera: np.ndarray) -> float:
    n_d, n_f = len(dentro), len(fuera)
    media_d, media_f = dentro.mean(), fuera.mean()
    var_d = dentro.var(ddof=1) if n_d > 1 else 0.0
    var_f = fuera.var(ddof=1) if n_f > 1 else 0.0
    se = math.sqrt(var_d / n_d + var_f / n_f) if n_d > 0 and n_f > 0 else 0.0
    if se == 0:
        return 0.0
    return (media_d - media_f) / se


def permutar_t_vectorizado(dentro: np.ndarray, fuera: np.ndarray, b: int) -> np.ndarray:
    """B réplicas del t-estadístico bajo H0 (etiqueta dentro/fuera no
    importa), vectorizado (mismo patrón que shuffle_test en
    analisis_gate_bucket_propio_28jul.py)."""
    n_d, n_f = len(dentro), len(fuera)
    pool = np.concatenate([dentro, fuera])
    n = n_d + n_f
    idx = _rng.random((b, n)).argsort(axis=1)
    permutado = pool[idx]
    grupo_d = permutado[:, :n_d]
    grupo_f = permutado[:, n_d:]
    media_d = grupo_d.mean(axis=1)
    media_f = grupo_f.mean(axis=1)
    var_d = grupo_d.var(axis=1, ddof=1) if n_d > 1 else np.zeros(b)
    var_f = grupo_f.var(axis=1, ddof=1) if n_f > 1 else np.zeros(b)
    se = np.sqrt(var_d / n_d + var_f / n_f)
    se[se == 0] = np.nan
    return (media_d - media_f) / se


def main() -> int:
    tuplas = cargar_tuplas_live()
    filas_por_tupla = cargar_filas(tuplas)

    tests = []  # (clave, t_obs, familia_moneda) -- clave = "tupla|bucket"
    T_perm_cols = []

    for strategy, subtype, decision, tupla_str, es_live in tuplas:
        filas = filas_por_tupla.get(tupla_str, [])
        if len(filas) < N_MIN:
            continue
        por_bucket = defaultdict(list)
        for ts, py, pnl in filas:
            por_bucket[bucket(py)].append(pnl)

        for b_key, dentro_list in por_bucket.items():
            fuera_list = [pnl for bb, fs in por_bucket.items() if bb != b_key for pnl in fs]
            n_d, n_f = len(dentro_list), len(fuera_list)
            if n_d < N_MIN or n_f == 0:
                continue
            dentro = np.array(dentro_list, dtype=np.float64)
            fuera = np.array(fuera_list, dtype=np.float64)
            t_obs = t_estadistico(dentro, fuera)
            activo = subtype.split("#")[0] if "#" in subtype else ""
            familia = _familia(strategy)
            clave = f"{tupla_str}|{b_key:.2f}"
            tests.append((clave, t_obs, f"{familia}#{activo}"))
            T_perm_cols.append(permutar_t_vectorizado(dentro, fuera, B))

    K = len(tests)
    print(f"Tests con n>=15 en ambos grupos: {K}")
    if K == 0:
        return 0

    T_obs = np.array([t for _, t, _ in tests])
    T_perm = np.column_stack(T_perm_cols)  # (B, K)
    T_perm = np.nan_to_num(T_perm, nan=0.0)

    # --- Romano-Wolf stepdown global ---
    orden = np.argsort(-np.abs(T_obs))  # de mayor a menor |t|
    activos = set(range(K))
    romano_wolf_sig = set()
    for idx in orden:
        if idx not in activos:
            continue
        cols_activas = list(activos)
        max_null = np.abs(T_perm[:, cols_activas]).max(axis=1)
        umbral = np.quantile(max_null, 1 - ALPHA)
        if np.abs(T_obs[idx]) > umbral:
            romano_wolf_sig.add(idx)
            activos.discard(idx)
        else:
            break  # monótono: el resto tampoco pasaría

    print(f"Romano-Wolf (FWER global, alpha={ALPHA}): {len(romano_wolf_sig)}/{K} tests sobreviven")

    # --- comparar contra p simple (sin corregir) y contra BH-FDR ya calculado en gate_bucket_propio.json ---
    p_simple = np.array([float(np.mean(np.abs(T_perm[:, i]) >= abs(T_obs[i]))) for i in range(K)])
    n_p_simple_sig = int(np.sum(p_simple < ALPHA))
    print(f"p simple sin corregir (< {ALPHA}): {n_p_simple_sig}/{K} tests 'significativos' (referencia, infla falsos positivos)")

    gate_actual = json.loads(GATE_ACTUAL.read_text()) if GATE_ACTUAL.exists() else {}
    confirmados_actuales = []
    for tupla_str, buckets_dict in gate_actual.items():
        for b_str, v in buckets_dict.items():
            if v.get("veredicto") in ("bueno_confirmado", "malo_confirmado"):
                confirmados_actuales.append((f"{tupla_str}|{b_str}", v["veredicto"]))

    print(f"\nVeredictos actuales (BH-FDR por familia+moneda) en gate_bucket_propio.json: {len(confirmados_actuales)}")
    clave_a_idx = {clave: i for i, (clave, _, _) in enumerate(tests)}
    sobreviven_rw = 0
    for clave, veredicto in confirmados_actuales:
        idx = clave_a_idx.get(clave)
        sobrevive = idx is not None and idx in romano_wolf_sig
        sobreviven_rw += int(sobrevive)
        print(f"  {clave:55s} {veredicto:18s} Romano-Wolf: {'SÍ' if sobrevive else 'no'}"
              f"{'' if idx is not None else '  (no recalculado -- posible desalineo bucket/tupla)'}")

    print(f"\n{sobreviven_rw}/{len(confirmados_actuales)} veredictos BH-FDR actuales sobreviven Romano-Wolf global")

    # --- Romano-Wolf estratificado por (familia,moneda) -- mismo universo que BH-FDR usa hoy ---
    print("\n=== Romano-Wolf estratificado por (familia,moneda) -- comparación justa con BH-FDR ===")
    grupos = defaultdict(list)
    for i, (clave, t_obs, grupo) in enumerate(tests):
        grupos[grupo].append(i)

    romano_wolf_estrat_sig = set()
    for grupo, idxs in grupos.items():
        if len(idxs) == 1:
            # un solo test en el grupo: Romano-Wolf estratificado = shuffle simple sin corregir
            i = idxs[0]
            if p_simple[i] < ALPHA:
                romano_wolf_estrat_sig.add(i)
            continue
        activos_g = set(idxs)
        orden_g = sorted(idxs, key=lambda i: -abs(T_obs[i]))
        for idx in orden_g:
            if idx not in activos_g:
                continue
            cols = list(activos_g)
            max_null_g = np.abs(T_perm[:, cols]).max(axis=1)
            umbral_g = np.quantile(max_null_g, 1 - ALPHA)
            if np.abs(T_obs[idx]) > umbral_g:
                romano_wolf_estrat_sig.add(idx)
                activos_g.discard(idx)
            else:
                break

    print(f"Romano-Wolf estratificado: {len(romano_wolf_estrat_sig)}/{K} tests sobreviven "
          f"(vs {len(romano_wolf_sig)}/{K} global, vs {n_p_simple_sig}/{K} sin corregir)")

    sobreviven_rw_estrat = 0
    for clave, veredicto in confirmados_actuales:
        idx = clave_a_idx.get(clave)
        sobrevive = idx is not None and idx in romano_wolf_estrat_sig
        sobreviven_rw_estrat += int(sobrevive)
        print(f"  {clave:55s} {veredicto:18s} RW-estratificado: {'SÍ' if sobrevive else 'no'}")

    print(f"\n{sobreviven_rw_estrat}/{len(confirmados_actuales)} veredictos BH-FDR actuales sobreviven "
          f"Romano-Wolf estratificado por (familia,moneda)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
