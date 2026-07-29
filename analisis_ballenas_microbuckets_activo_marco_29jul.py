"""
analisis_ballenas_microbuckets_activo_marco_29jul.py — petición explícita
Javi 29-Jul, tras el hallazgo de payout inverso en BALLENAS_TARDIAS en
live: "hay que ver ballenas familia desagregado por moneda, marca
temporal y sacar los 6 mejores micro-buckets... hay que ir donde está el
dinero y eliminar pérdidas". Aclarado: los 6 mejores micro-buckets vistos
POR (moneda, marco) -- no un agregado de familia (eso ya lo hace
analisis_kelly_precio_gate_29jul.py, y ahí BALLENAS_FAMILIA no confirmó
ningún bucket por falta de n al agregar TODAS las monedas/marcos juntos).

Metodología: mismo rigor que el resto del proyecto (Wilson + shuffle +
split-half + BH-FDR), pero la unidad de agregación es (strategy, activo,
marco) -- NO la familia entera -- y el bucket es más fino (paso 0.05, no
0.10) porque cada celda ya es más estrecha (un solo activo/marco en vez
de las 4-5 monedas mezcladas).

Ranking: "los 6 mejores" = los 6 con mayor |pnl_total| entre los que
sobreviven el gate de rigor (n>=15, shuffle+split-half, BH-FDR) -- eso es
literalmente "dónde está el dinero" (más euros en juego, no solo el
ratio/€ por trade más bonito con n bajo).

Solo lectura. No toca prob_yes/stake/pares_permitidos_live. Salida:
data/shadow/ballenas_microbuckets_activo_marco.json
"""
import csv
import json
import math
from collections import defaultdict
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
RESULTS = str(REPO / "data/shadow/results.csv")
OUT = str(REPO / "data/shadow/ballenas_microbuckets_activo_marco.json")

STEP = 0.05
N_MIN = 15
P_MAX = 0.05
ITERS = 2000
TOP_N = 6

_rng = np.random.default_rng(2907)


def bucket(p):
    return round(math.floor(p / STEP) * STEP, 4)


def precio_decision(row):
    p = float(row["precio_yes_mercado"])
    if row["decision"] == "BUY_NO":
        p = 1 - p
    return min(0.999, max(0.001, p))


def wilson_ci(k, n, z=1.645):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((centro - margen) / denom, (centro + margen) / denom)


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
    return float(np.mean(np.abs(diffs) >= abs(diff_real)))


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


def cargar():
    """(strategy, activo#marco) -> [(ts, py_decision, pnl, acierto), ...]
    -- solo estrategias BALLENAS_*, cualquier subtype/decision."""
    out = defaultdict(list)
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if not row["strategy"].startswith("BALLENAS"):
                continue
            if row.get("acierto") not in ("0", "1"):
                continue
            try:
                pnl = float(row["pnl_neto"])
                py = precio_decision(row)
            except Exception:
                continue
            clave = (row["strategy"], row["subtype"])
            out[clave].append((row.get("prediction_timestamp", ""), py, pnl, int(row["acierto"])))
    return out


def main():
    datos = cargar()
    print(f"Combos (strategy, activo#marco): {list(datos.keys())}")

    resultado = {}
    pendientes = []
    for (strategy, subtype), filas in datos.items():
        clave = f"{strategy}#{subtype}"
        por_bucket = defaultdict(list)
        for ts, py, pnl, ac in filas:
            por_bucket[bucket(py)].append((ts, py, pnl, ac))

        tabla = {}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, py, pnl, ac) for bb, fs in por_bucket.items() if bb != b for ts, py, pnl, ac in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, _, pnl, _ in dentro]
            wins = sum(ac for _, _, _, ac in dentro)
            entrada = {
                "n": n_d, "hit": round(wins / n_d, 4) if n_d else None,
                "pnl_medio": round(sum(pnl_d) / n_d, 4) if n_d else None,
                "pnl_total": round(sum(pnl_d), 4) if n_d else None,
                "shuffle_p": None, "split_half_diff": None, "veredicto": "sin_concluir",
            }
            tabla[f"{b:.2f}"] = entrada

            if n_d >= N_MIN and fuera:
                pnl_f = [pnl for _, _, pnl, _ in fuera]
                p_valor = shuffle_test(pnl_d, pnl_f)
                entrada["shuffle_p"] = round(p_valor, 4)
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    media_fuera = sum(pnl_f) / len(pnl_f)
                    d1 = sum(pnl for _, _, pnl, _ in m1) / len(m1) - media_fuera
                    d2 = sum(pnl for _, _, pnl, _ in m2) / len(m2) - media_fuera
                    entrada["split_half_diff"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"clave": clave, "bucket": f"{b:.2f}", "entrada": entrada,
                                            "p": p_valor})
        resultado[clave] = tabla

    p_valores = [p["p"] for p in pendientes]
    sobreviven = bh_fdr_signif(p_valores, q=P_MAX)
    print(f"\nTests candidatos: {len(pendientes)} | sobreviven BH-FDR q={P_MAX}: {len(sobreviven)}")

    confirmados = []
    for idx, p in enumerate(pendientes):
        if idx in sobreviven:
            p["entrada"]["veredicto"] = "confirmado"
            confirmados.append(p)

    confirmados.sort(key=lambda p: -abs(p["entrada"]["pnl_total"]))
    top = confirmados[:TOP_N]

    print(f"\n{'='*95}\nTOP {TOP_N} micro-buckets por |pnl_total| (los {TOP_N} 'donde está el dinero'):\n{'='*95}")
    print(f"{'clave (activo#marco)':40s} {'bucket':>7s} {'n':>5s} {'hit':>6s} {'pnl/tr':>8s} {'pnl_total':>10s} {'shuf_p':>7s}")
    for p in top:
        e = p["entrada"]
        print(f"{p['clave']:40s} {p['bucket']:>7s} {e['n']:>5d} {e['hit']*100:>5.1f}% "
              f"{e['pnl_medio']:>+8.3f} {e['pnl_total']:>+10.2f} {e['shuffle_p']:>7}")

    print(f"\n{'='*95}\nTodos los buckets confirmados (no solo top {TOP_N}):\n{'='*95}")
    for p in sorted(confirmados, key=lambda p: p["clave"]):
        e = p["entrada"]
        print(f"{p['clave']:40s} {p['bucket']:>7s} {e['n']:>5d} {e['hit']*100:>5.1f}% "
              f"{e['pnl_medio']:>+8.3f} {e['pnl_total']:>+10.2f} {e['shuffle_p']:>7}")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({
            "generado_utc": __import__("datetime").datetime.now(__import__("datetime").timezone.utc).isoformat(),
            "step": STEP, "n_min": N_MIN, "p_max": P_MAX,
            "top_6_por_pnl_total": [{"clave": p["clave"], "bucket": p["bucket"], **p["entrada"]} for p in top],
            "combos": resultado,
        }, f, indent=2, ensure_ascii=False)
    print(f"\nEscrito {OUT}")


if __name__ == "__main__":
    main()
