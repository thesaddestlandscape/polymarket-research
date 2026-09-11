#!/usr/bin/env python3
"""analisis_ultramicrobuckets_02_10ago.py -- ¿merece la pena bajar el step
de gate_bucket_propio de 0.05 a 0.02 ("bisturí", petición Javi 09-Ago)?

Alcance tal como lo pidió Javi (ver idea_ultramicrobuckets_bisturi_09ago):
SOLO para tuplas que HOY no tienen NINGÚN micro-bucket confirmado a
step=0.05 (gate_bucket_propio.json). Las que ya tienen bueno_confirmado/
malo_confirmado siguen mandando con el step actual -- no se tocan.

Antes de tocar analisis_gate_bucket_propio_28jul.py/gate_bucket_propio.py
(motor de decisión compartido, exige diseño cuidadoso + /code-review por
CLAUDE.md), este script mide con DATOS REALES si bajar el step realmente
rescata algo, o si la tensión estadística ya anticipada en el diseño
(menos n/bucket, más tests para BH-FDR) lo hace contraproducente hoy.

Mismo rigor que el generador real: n>=15, shuffle test, split-half
cronológico, BH-FDR por (familia,activo) -- reutiliza directamente
kelly_precio_gate._familia() y la misma metodología de
analisis_gate_bucket_propio_28jul.py, solo con STEP=0.02 y universo
restringido a las tuplas sin_concluir.

Solo lectura -- no toca gate_bucket_propio.json ni ningún gate real.
"""
import csv
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from kelly_precio_gate import _familia

REPO = Path(__file__).resolve().parent
RESULTS = str(REPO / "data/shadow/results.csv")
GATE_ACTUAL = str(REPO / "data/shadow/gate_bucket_propio.json")

STEP_FINO = 0.02
STEP_ACTUAL = 0.05
N_MIN = 15
P_MAX = 0.05
ITERS = 1000

# 10-Ago: MISMO fix de régimen TWAP que analisis_gate_bucket_propio_28jul.py
# -- sin esto, este script reintroduce la mezcla pre/post-TWAP que se acaba
# de arreglar en el generador canónico (bug real cazado al ver que este
# script "confirmaba" 21 buckets en tuplas que el JSON real, ya corregido,
# marca sin_concluir).
FECHA_CAMBIO_TWAP = datetime(2026, 8, 7, tzinfo=timezone.utc)
MARCOS_TWAP_AFECTADOS = {"5min", "15min", "240min"}


def _marco_de_tupla(tupla_str):
    partes = tupla_str.split("#")
    return partes[2] if len(partes) == 4 else ""

_rng = np.random.default_rng(42)


def bucket(p, step):
    return round(math.floor(p / step + 1e-9) * step, 4)


def tuplas_sin_confirmar():
    """Universo restringido: tuplas del gate actual (step=0.05) donde
    NINGÚN bucket llegó a malo_confirmado/bueno_confirmado."""
    d = json.loads(Path(GATE_ACTUAL).read_text(encoding="utf-8"))
    out = []
    for tupla, buckets in d.items():
        if not buckets:
            continue
        if all(info.get("veredicto") == "sin_concluir" for info in buckets.values()):
            out.append(tupla)
    return out


def cargar_filas(tuplas):
    claves = {}
    for t in tuplas:
        partes = t.split("#")
        if len(partes) == 4:
            claves[(partes[0], f"{partes[1]}#{partes[2]}", partes[3])] = t
        elif len(partes) == 3:
            claves[(partes[0], partes[1], partes[2])] = t
    marco_por_tupla = {t: _marco_de_tupla(t) for t in tuplas}
    out = defaultdict(list)
    n_excluidas = 0
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            clave = (row["strategy"], row["subtype"], row["decision"])
            t = claves.get(clave)
            if t is None:
                continue
            if marco_por_tupla.get(t) in MARCOS_TWAP_AFECTADOS:
                try:
                    ts_dt = datetime.fromisoformat(row.get("prediction_timestamp", ""))
                except Exception:
                    continue
                if ts_dt < FECHA_CAMBIO_TWAP:
                    n_excluidas += 1
                    continue
            try:
                py = float(row["precio_yes_mercado"])
                pnl = float(row["pnl_neto"])
            except Exception:
                continue
            out[t].append((row.get("prediction_timestamp", ""), py, pnl))
    if n_excluidas:
        print(f"[cargar_filas] {n_excluidas} filas pre-TWAP excluidas en marcos afectados")
    return out


def shuffle_test(a, b, iters=ITERS):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    na, nb = len(a), len(b)
    diff_real = a.mean() - b.mean()
    todos = np.concatenate([a, b])
    n = na + nb
    idx = _rng.random((iters, n)).argsort(axis=1)
    permutado = todos[idx]
    media_a = permutado[:, :na].mean(axis=1)
    media_b = permutado[:, na:].mean(axis=1)
    diffs = media_a - media_b
    p_valor = float(np.mean(np.abs(diffs) >= abs(diff_real)))
    return float(diff_real), p_valor


def bh_fdr_signif(p_valores, q=0.05):
    n = len(p_valores)
    if n == 0:
        return set()
    orden = sorted(range(n), key=lambda i: p_valores[i])
    corte = -1
    for rank, i in enumerate(orden, start=1):
        if p_valores[i] <= (rank / n) * q:
            corte = rank
    if corte == -1:
        return set()
    return set(orden[:corte])


def evaluar_step(tuplas, filas_por_tupla, step):
    pendientes = []
    n_buckets_totales = 0
    n_buckets_con_n_min = 0
    for tupla_str in tuplas:
        filas = filas_por_tupla.get(tupla_str, [])
        if not filas:
            continue
        por_bucket = defaultdict(list)
        for ts, py, pnl in filas:
            por_bucket[bucket(py, step)].append((ts, pnl))
        n_buckets_totales += len(por_bucket)
        for b, dentro in por_bucket.items():
            n_d = len(dentro)
            if n_d < N_MIN:
                continue
            n_buckets_con_n_min += 1
            fuera = [(ts, pnl) for bb, fs in por_bucket.items() if bb != b for ts, pnl in fs]
            if not fuera:
                continue
            pnl_d = [pnl for _, pnl in dentro]
            pnl_f = [pnl for _, pnl in fuera]
            media_d = sum(pnl_d) / n_d
            diff, p_valor = shuffle_test(pnl_d, pnl_f)
            dentro_sorted = sorted(dentro, key=lambda x: x[0])
            mid = n_d // 2
            m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
            if len(m1) < 5 or len(m2) < 5:
                continue
            d1 = sum(pnl for _, pnl in m1) / len(m1) - sum(pnl_f) / len(pnl_f)
            d2 = sum(pnl for _, pnl in m2) / len(m2) - sum(pnl_f) / len(pnl_f)
            consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
            if not consistente:
                continue
            pendientes.append({"tupla_str": tupla_str, "bucket": f"{b:.3f}", "n": n_d,
                                "pnl_medio": media_d, "diff": diff, "p": p_valor})

    por_familia_moneda = defaultdict(list)
    for idx, p in enumerate(pendientes):
        partes = p["tupla_str"].split("#")
        strategy, activo = partes[0], (partes[1] if len(partes) > 1 else "?")
        por_familia_moneda[(_familia(strategy), activo)].append(idx)

    sobreviven = set()
    for clave, indices in por_familia_moneda.items():
        p_valores_grupo = [pendientes[i]["p"] for i in indices]
        sobreviven |= {indices[j] for j in bh_fdr_signif(p_valores_grupo, q=P_MAX)}

    confirmados = []
    for idx in sobreviven:
        p = pendientes[idx]
        veredicto = "malo_confirmado" if p["diff"] < 0 else (
            "bueno_confirmado" if p["pnl_medio"] >= 0 else None)
        if veredicto:
            confirmados.append({**p, "veredicto": veredicto})

    return {
        "n_buckets_totales": n_buckets_totales,
        "n_buckets_con_n_min": n_buckets_con_n_min,
        "n_tests_bh": len(pendientes),
        "confirmados": confirmados,
    }


def main():
    tuplas = tuplas_sin_confirmar()
    print(f"Tuplas sin NINGÚN bucket confirmado a step={STEP_ACTUAL}: {len(tuplas)}")
    filas_por_tupla = cargar_filas(tuplas)
    n_con_datos = sum(1 for t in tuplas if filas_por_tupla.get(t))
    print(f"  de esas, con filas en results.csv: {n_con_datos}\n")

    print(f"=== STEP ACTUAL ({STEP_ACTUAL}) sobre el mismo universo (control) ===")
    r_actual = evaluar_step(tuplas, filas_por_tupla, STEP_ACTUAL)
    print(f"  buckets totales: {r_actual['n_buckets_totales']} | con n>={N_MIN}: {r_actual['n_buckets_con_n_min']} "
          f"| tests candidatos (n_min+split-half): {r_actual['n_tests_bh']} | confirmados tras BH-FDR: {len(r_actual['confirmados'])}")
    for c in r_actual["confirmados"]:
        print(f"    {c['veredicto']}: {c['tupla_str']} [{c['bucket']}) n={c['n']} pnl={c['pnl_medio']:+.3f} p={c['p']:.4f}")

    print(f"\n=== STEP FINO ({STEP_FINO}, ultra-micro-bucket) ===")
    r_fino = evaluar_step(tuplas, filas_por_tupla, STEP_FINO)
    print(f"  buckets totales: {r_fino['n_buckets_totales']} | con n>={N_MIN}: {r_fino['n_buckets_con_n_min']} "
          f"| tests candidatos (n_min+split-half): {r_fino['n_tests_bh']} | confirmados tras BH-FDR: {len(r_fino['confirmados'])}")
    for c in r_fino["confirmados"]:
        print(f"    {c['veredicto']}: {c['tupla_str']} [{c['bucket']}) n={c['n']} pnl={c['pnl_medio']:+.3f} p={c['p']:.4f}")

    print(f"\n=== Resumen ===")
    print(f"step={STEP_ACTUAL}: {r_actual['n_buckets_con_n_min']} buckets con n>={N_MIN} de {r_actual['n_buckets_totales']} totales "
          f"({r_actual['n_buckets_con_n_min']/max(1,r_actual['n_buckets_totales'])*100:.1f}%) -> {len(r_actual['confirmados'])} confirmados")
    print(f"step={STEP_FINO}: {r_fino['n_buckets_con_n_min']} buckets con n>={N_MIN} de {r_fino['n_buckets_totales']} totales "
          f"({r_fino['n_buckets_con_n_min']/max(1,r_fino['n_buckets_totales'])*100:.1f}%) -> {len(r_fino['confirmados'])} confirmados")


if __name__ == "__main__":
    main()
