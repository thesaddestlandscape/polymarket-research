#!/usr/bin/env python3
"""
analisis_gate_mejora_contraria_02sep.py — gate riguroso permanente para
el hallazgo "mejora_contraria>=2x" (02-Sep): cuando la profundidad del
lado NO operado se duplica o más tras la señal (misma fuente que
fade_depth_universal_fase0.py, campos ratio_contrario_inicial/max),
el hit-rate/pnl real sube de forma sistemática y muy significativa en
decenas de familias -- no es un caso aislado de 4 tuplas.

Origen: petición explícita Javi 02-Sep ("revisa que familias pueden
verse afectadas también"). Cruce manual de sesión sobre 90.890 filas de
fade_depth_universal_fase0.csv × 356.771 filas de results.csv: 100
combos (strategy,subtype) con n>=15 en ambos grupos, 60 sobreviven
p<0.05 corregido BH-FDR (diffs +8.7pp a +51.5pp de hit-rate). Confounds
obvios descartados sobre el grupo más grande (FAVORITO_CONFIRMADO#BTC#
5min): tiempo restante a la señal (4.88 vs 4.83min) y precio de entrada
(0.509 vs 0.509) -- prácticamente idénticos entre grupos, no es proxy de
ninguno de los dos. Ver memoria nativa idea_mejora_contraria_2x_
filtro_sistemico_02sep para el detalle completo del hallazgo.

Diseño deliberado: SOLO OBSERVACIÓN, no toca shadow_predict.py ni
prob_yes de ninguna tupla -- convierte el análisis retrospectivo de la
sesión en mecanismo recurrente (cron diario) para que el gate riguroso
se recalcule solo con datos frescos, mismo patrón que gate_bucket_
propio.py/wallet_mirror_gate_bucket_10ago.py. Solo cuando una familia
sobreviva con rigor sostenido en varias corridas (no solo el snapshot
retrospectivo de hoy) tendría sentido plantear instrumentarlo como
filtro real en shadow_predict.py -- eso requeriría /code-review por
tocar el motor de decisión compartido, decisión explícita de Javi.

Rigor: n>=15 en ambos grupos (con/sin mejora_contraria) por familia,
shuffle test (permutación de acierto entre los dos grupos), split-half
cronológico, BH-FDR sobre TODAS las familias evaluadas en la corrida
(no solo las llamativas -- evita el error de "significancia" post-hoc
que ya se cazó una vez en gate_bucket_fino.py, 20-Ago).

Cron sugerido (diario, franja tranquila):
  20 7 * * * flock -n /tmp/gate_mejora_contraria.lock /root/polymarket-research/.venv/bin/python /root/polymarket-research/analisis_gate_mejora_contraria_02sep.py >> /root/polymarket-research/logs/gate_mejora_contraria.log 2>&1
"""
import csv
import json
import math
import random
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

csv.field_size_limit(sys.maxsize)
random.seed(42)

REPO = Path(__file__).resolve().parent
FADE = REPO / "data/shadow/fade_depth_universal_fase0.csv"
RESULTS = REPO / "data/shadow/results.csv"
OUT = REPO / "data/shadow/gate_mejora_contraria.json"

N_MIN = 15
UMBRAL_MEJORA = 2.0
N_SHUFFLE = 2000
Z90 = 1.645


def wilson_lo(p: float, n: int, z: float = Z90) -> float:
    if n == 0:
        return 0.0
    denom = 1 + z * z / n
    center = p + z * z / (2 * n)
    adj = z * math.sqrt(max(p * (1 - p) / n, 0) + z * z / (4 * n * n))
    return (center - adj) / denom


def cargar_fade_by_key() -> dict:
    fade_by_key = {}
    with open(FADE, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = f"{row.get('strategy')}#{row.get('subtype')}"
            try:
                ini = float(row["ratio_contrario_inicial"])
                mx = float(row["ratio_contrario_max"])
            except (TypeError, ValueError, KeyError):
                continue
            mejora = (mx / ini >= UMBRAL_MEJORA) if ini > 0 else (mx > 0)
            fade_by_key[(key, row.get("market_id"))] = mejora
    return fade_by_key


def cargar_matched(fade_by_key: dict) -> dict:
    matched = defaultdict(lambda: {"con_mejora": [], "sin_mejora": []})
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            strat = row.get("strategy")
            subtype = row.get("subtype")
            key = f"{strat}#{subtype}"
            fk = (key, row.get("market_id"))
            if fk not in fade_by_key:
                continue
            acierto = row.get("acierto")
            if acierto not in ("0", "1"):
                continue
            try:
                pnl = float(row.get("pnl_neto"))
            except (TypeError, ValueError):
                pnl = None
            ts = row.get("prediction_timestamp") or row.get("timestamp_utc", "")
            bucket = "con_mejora" if fade_by_key[fk] else "sin_mejora"
            matched[key][bucket].append((int(acierto), pnl, ts))
    return matched


def shuffle_test(con: list, sin: list) -> float:
    n1 = len(con)
    diff_obs = sum(x[0] for x in con) / n1 - sum(x[0] for x in sin) / len(sin)
    pool = [x[0] for x in con] + [x[0] for x in sin]
    n_total = len(pool)
    cnt = 0
    for _ in range(N_SHUFFLE):
        random.shuffle(pool)
        sub = pool[:n1]
        resto = pool[n1:]
        d = sum(sub) / n1 - sum(resto) / len(resto)
        if d >= diff_obs:
            cnt += 1
    return cnt / N_SHUFFLE


def split_half(vals: list) -> tuple:
    items = sorted(vals, key=lambda x: x[2])
    n = len(items)
    half = n // 2
    m1 = sum(x[0] for x in items[:half]) / max(half, 1)
    m2 = sum(x[0] for x in items[half:]) / max(n - half, 1)
    return round(m1, 4), round(m2, 4)


def main():
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] cargando fuentes...")
    fade_by_key = cargar_fade_by_key()
    matched = cargar_matched(fade_by_key)
    print(f"fade_by_key: {len(fade_by_key)} | familias con datos: {len(matched)}")

    resultados = []
    for key, d in matched.items():
        con, sin = d["con_mejora"], d["sin_mejora"]
        n1, n2 = len(con), len(sin)
        if n1 < N_MIN or n2 < N_MIN:
            continue
        hit1 = sum(x[0] for x in con) / n1
        hit2 = sum(x[0] for x in sin) / n2
        pnl1 = [x[1] for x in con if x[1] is not None]
        pnl2 = [x[1] for x in sin if x[1] is not None]
        pnl_m1 = round(sum(pnl1) / len(pnl1), 4) if pnl1 else None
        pnl_m2 = round(sum(pnl2) / len(pnl2), 4) if pnl2 else None
        p_shuffle = shuffle_test(con, sin)
        sh1 = split_half(con)
        resultados.append({
            "key": key, "n_con_mejora": n1, "hit_con_mejora": round(hit1, 4),
            "pnl_medio_con_mejora": pnl_m1, "n_sin_mejora": n2,
            "hit_sin_mejora": round(hit2, 4), "pnl_medio_sin_mejora": pnl_m2,
            "diff_hit_pp": round((hit1 - hit2) * 100, 2),
            "p_shuffle": round(p_shuffle, 5),
            "split_half_con_mejora": sh1,
        })

    m = len(resultados)
    resultados.sort(key=lambda r: r["p_shuffle"])
    prev = 1.0
    for i in range(m - 1, -1, -1):
        r = resultados[i]
        q = min(r["p_shuffle"] * m / (i + 1), prev)
        prev = q
        r["p_bh"] = round(q, 5)
        r["veredicto"] = "confirmado" if (q < 0.05 and r["diff_hit_pp"] > 0) else "no_significativo"

    n_confirmados = sum(1 for r in resultados if r["veredicto"] == "confirmado")
    print(f"familias evaluadas (n>=15 ambos grupos): {m} | confirmadas BH-FDR: {n_confirmados}")

    OUT.write_text(json.dumps({
        "actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "umbral_mejora": UMBRAL_MEJORA, "n_min": N_MIN,
        "n_familias_evaluadas": m, "n_confirmadas": n_confirmados,
        "resultados": sorted(resultados, key=lambda r: -r["diff_hit_pp"]),
    }, indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"{'familia':45s} {'n_con':>6s} {'hit_con':>8s} {'n_sin':>6s} {'hit_sin':>8s} {'diff':>7s} {'p_bh':>8s}")
    for r in sorted(resultados, key=lambda r: -r["diff_hit_pp"])[:20]:
        print(f"{r['key']:45s} {r['n_con_mejora']:6d} {r['hit_con_mejora']*100:7.1f}% "
              f"{r['n_sin_mejora']:6d} {r['hit_sin_mejora']*100:7.1f}% {r['diff_hit_pp']:+6.1f}pp {r['p_bh']:8.4f}")


if __name__ == "__main__":
    main()
