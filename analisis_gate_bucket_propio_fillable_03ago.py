"""
analisis_gate_bucket_propio_fillable_03ago.py — v2 de
analisis_gate_bucket_propio_28jul.py: mismo gate por micro-bucket de
precio (n>=15, shuffle test, split-half cronológico, BH-FDR), pero
restringido al subconjunto REALMENTE accionable en vez de results.csv
completo.

Por qué (hallazgo 03-Ago, sesión de pausa de BALLENAS_TARDIAS#BTC#15min +
FAVORITO_15MIN_ALTACONVICCION#ETH#15min): un primer intento de cruzar
libro_snapshots.csv (ratio_vs_stake>=5x) contra results.csv mezclaba
"ejecutada" (trade real intentado) con "senal_caducada"/"fuera_ventana"
-- categorías que el proyecto YA demostró que son estructuralmente
adversas incluso con libro bueno (ver
idea_caducidad_senales_filtro_protector_28jul: las señales caducadas
que SÍ tenían profundidad pierden dinero en 11/12 tuplas si se
hubieran ejecutado -- es un filtro protector, no un bug). Incluirlas
como "fillable" sesgaba el resultado hacia negativo artificialmente.

Definición correcta de "accionable" aquí:
  - Tuplas LIVE: motivo en {ejecutada, abort_requote, fok_kill} -- intento
    real de ejecución (exitoso o abortado por fricción real de mercado,
    no por timeout). veto_profundidad queda fuera por definición (ratio<5x
    ya lo excluye el filtro fillable de más abajo).
  - Tuplas CANDIDATO (no viven en pares_permitidos_live todavía): no hay
    "ejecutada" posible (nunca se intenta con dinero real). Se usa
    candidato_evaluacion + ratio_vs_stake>=5x como la mejor proxy
    disponible de "tendría profundidad si se intentara" -- más débil que
    el caso live (nunca hubo intento real), documentado explícitamente en
    el output.

Solo lectura -- no cambia prob_yes/stake/pares_permitidos_live ni
sobreescribe gate_bucket_propio.json (el que SÍ vetea dinero real hoy).
Escribe en data/shadow/gate_bucket_propio_fillable.json para comparar
antes de decidir si sustituye a la fuente de verdad actual (requiere
/code-review, toca qué se ejecuta con dinero real).
"""
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
RESULTS = str(REPO / "data/shadow/results.csv")
LIBRO = str(REPO / "data/live/libro_snapshots.csv")
CONFIG_LIVE = str(REPO / "data/live/config_live.json")
OUT = str(REPO / "data/shadow/gate_bucket_propio_fillable.json")

STEP = 0.05
N_MIN = 15
P_MAX = 0.05
ITERS = 1000
RATIO_MIN = 5.0

PRIORIDAD_LIVE = ["ejecutada", "abort_requote", "fok_kill"]
PRIORIDAD_COLAPSO = ["ejecutada", "veto_profundidad", "abort_requote", "fok_kill",
                      "veto_sin_datos", "senal_caducada", "no_viable_stake",
                      "candidato_evaluacion", "fuera_ventana"]


def bucket(p):
    # 06-Ago fix: +1e-9 evita mal-clasificar precios EXACTOS en un múltiplo
    # de STEP al bucket inferior (coma flotante) -- ver idea_bug_bucketing_
    # float_precision_micro_buckets_06ago.
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def cargar_tuplas_live():
    with open(CONFIG_LIVE, encoding="utf-8") as f:
        c = json.load(f)
    vistos = {}
    for lista, es_live in ((c.get("pares_permitidos_live", []), True),
                            (c.get("candidatos_evaluacion_live", []), False)):
        for t in lista:
            partes = t.split("#")
            if len(partes) != 4:
                continue
            strategy, activo, marco, decision = partes
            if t in vistos and vistos[t][4]:
                continue
            vistos[t] = (strategy, f"{activo}#{marco}", decision, t, es_live)
    return list(vistos.values())


def colapsar_libro():
    """market_id -> mejor fila por (tupla), prioridad = PRIORIDAD_COLAPSO.
    Mismo criterio que analisis_fills.py -- NUNCA contar filas sueltas."""
    by_key = {}
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            tupla = (r["strategy"], r["subtype"], r["direction"])
            mid = r["market_id"]
            k = (tupla, mid)
            motivo = r.get("motivo", "")
            if k not in by_key:
                by_key[k] = r
            else:
                prev = by_key[k].get("motivo", "")
                if motivo in PRIORIDAD_COLAPSO and prev in PRIORIDAD_COLAPSO and \
                        PRIORIDAD_COLAPSO.index(motivo) < PRIORIDAD_COLAPSO.index(prev):
                    by_key[k] = r
    return by_key


def es_accionable(motivo, ratio, es_live):
    try:
        ratio_f = float(ratio) if ratio not in (None, "") else None
    except Exception:
        ratio_f = None
    if ratio_f is None or ratio_f < RATIO_MIN:
        return False
    if es_live:
        return motivo in PRIORIDAD_LIVE
    return motivo == "candidato_evaluacion"


def cargar_filas_accionables(tuplas):
    claves = {(s, sub, d): (t, es_live) for s, sub, d, t, es_live in tuplas}
    by_key = colapsar_libro()

    # market_ids accionables por tupla
    accionables_por_tupla = defaultdict(set)
    for (tupla_libro, mid), r in by_key.items():
        strat, sub, direc = tupla_libro
        info = claves.get((strat, sub, direc))
        if info is None:
            continue
        t, es_live = info
        if es_accionable(r.get("motivo"), r.get("ratio_vs_stake"), es_live):
            accionables_por_tupla[t].add(mid)

    out = defaultdict(list)
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            clave = (row["strategy"], row["subtype"], row["decision"])
            info = claves.get(clave)
            if info is None:
                continue
            t, es_live = info
            mid = row.get("market_id")
            if mid not in accionables_por_tupla.get(t, ()):
                continue
            try:
                py = float(row["precio_yes_mercado"])
                pnl = float(row["pnl_neto"])
            except Exception:
                continue
            out[t].append((row.get("prediction_timestamp", ""), py, pnl))
    return out, {t: len(accionables_por_tupla.get(t, ())) for _, _, _, t, _ in tuplas}


_rng = np.random.default_rng(42)


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


def main():
    tuplas = cargar_tuplas_live()
    filas_por_tupla, n_accionables = cargar_filas_accionables(tuplas)
    n_live = sum(1 for *_, es_live in tuplas if es_live)
    print(f"Tuplas a evaluar: {len(tuplas)} ({n_live} live, {len(tuplas) - n_live} candidatos)")
    print(f"Tuplas con >=1 mercado accionable: {sum(1 for v in n_accionables.values() if v > 0)}")

    pendientes = []
    resultado = {}
    for i, (strategy, subtype, decision, tupla_str, es_live) in enumerate(tuplas):
        filas = filas_por_tupla.get(tupla_str, [])
        if len(filas) < N_MIN:
            resultado[tupla_str] = {"_n_accionable_total": len(filas)}
            continue

        por_bucket = defaultdict(list)
        for ts, py, pnl in filas:
            por_bucket[bucket(py)].append((ts, pnl))

        tabla = {"_n_accionable_total": len(filas), "_es_live": es_live}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, pnl) for bb, fs in por_bucket.items() if bb != b for ts, pnl in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, pnl in dentro]
            pnl_f = [pnl for _, pnl in fuera]
            media_d = sum(pnl_d) / n_d

            entrada = {"n": n_d, "pnl_medio": round(media_d, 4),
                       "diff_vs_resto": round(media_d - (sum(pnl_f) / len(pnl_f)), 4) if pnl_f else None,
                       "shuffle_p": None, "split_half_diff": None, "veredicto": "sin_concluir"}
            tabla[f"{b:.2f}"] = entrada

            if n_d >= N_MIN and pnl_f:
                diff, p_valor = shuffle_test(pnl_d, pnl_f)
                entrada["shuffle_p"] = round(p_valor, 4)
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    d1 = sum(pnl for _, pnl in m1) / len(m1) - sum(pnl_f) / len(pnl_f)
                    d2 = sum(pnl for _, pnl in m2) / len(m2) - sum(pnl_f) / len(pnl_f)
                    entrada["split_half_diff"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"tupla_str": tupla_str, "bucket": f"{b:.2f}", "entrada": entrada,
                                            "p": p_valor, "diff": diff, "es_live": es_live})
        resultado[tupla_str] = tabla

    p_valores = [p["p"] for p in pendientes]
    sobreviven = bh_fdr_signif(p_valores, q=P_MAX)
    print(f"\nTests candidatos: {len(pendientes)} | sobreviven BH-FDR q={P_MAX}: {len(sobreviven)}")

    veredictos_nuevos = []
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        veredicto = "malo_confirmado" if p["diff"] < 0 else "bueno_confirmado"
        p["entrada"]["veredicto"] = veredicto
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        etiqueta = "LIVE" if p["es_live"] else "candidato(proxy)"
        b = p["bucket"]
        veredictos_nuevos.append(
            f"{marca} [{etiqueta}] {p['tupla_str']} [{b},{float(b)+STEP:.2f}) n={p['entrada']['n']} "
            f"pnl_medio={p['entrada']['pnl_medio']:+.3f} p={p['p']:.4f} {veredicto}"
        )

    print(f"\n{len(veredictos_nuevos)} bucket(s) con veredicto final tras BH-FDR:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
