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
UMBRAL_EMPEORA = 1.0  # 02-Sep: reverso -- ratio_max/ratio_inicial<1 (nunca mejora) es VETO
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
    """(key, market_id) -> 'mejora' (ratio_max/inicial>=2x) | 'empeora'
    (ratio_max/inicial<1x, nunca mejora -- 02-Sep, reverso del hallazgo
    original, veto potencial más fuerte todavía) | 'neutral' (entre medias)."""
    fade_by_key = {}
    with open(FADE, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            key = f"{row.get('strategy')}#{row.get('subtype')}"
            try:
                ini = float(row["ratio_contrario_inicial"])
                mx = float(row["ratio_contrario_max"])
            except (TypeError, ValueError, KeyError):
                continue
            if ini > 0:
                ratio = mx / ini
                cat = "mejora" if ratio >= UMBRAL_MEJORA else ("empeora" if ratio < UMBRAL_EMPEORA else "neutral")
            else:
                cat = "mejora" if mx > 0 else "empeora"
            fade_by_key[(key, row.get("market_id"))] = cat
    return fade_by_key


def cargar_matched(fade_by_key: dict) -> dict:
    matched = defaultdict(lambda: {"con_mejora": [], "sin_mejora": [], "con_empeora": [], "sin_empeora": []})
    with open(RESULTS, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            strat = row.get("strategy")
            subtype = row.get("subtype")
            key = f"{strat}#{subtype}"
            fk = (key, row.get("market_id"))
            if fk not in fade_by_key:
                continue
            cat = fade_by_key[fk]
            acierto = row.get("acierto")
            if acierto not in ("0", "1"):
                continue
            try:
                pnl = float(row.get("pnl_neto"))
            except (TypeError, ValueError):
                pnl = None
            ts = row.get("prediction_timestamp") or row.get("timestamp_utc", "")
            tupla = (int(acierto), pnl, ts)
            matched[key]["con_mejora" if cat == "mejora" else "sin_mejora"].append(tupla)
            matched[key]["con_empeora" if cat == "empeora" else "sin_empeora"].append(tupla)
    return matched


def shuffle_test(con: list, sin: list) -> float:
    """Test de permutación DOS COLAS (|d|>=|diff_obs|) -- deliberado: este
    gate evalúa tanto grupos MEJORES que el resto (mejora_contraria) como
    PEORES (empeora_contraria/veto). Un test de una cola (d>=diff_obs)
    daba p~1.0 para todo el lado "peor" -- bug real cazado 02-Sep antes
    de que ningún veto llegara a confirmarse con el número equivocado."""
    n1 = len(con)
    diff_obs = sum(x[0] for x in con) / n1 - sum(x[0] for x in sin) / len(sin)
    pool = [x[0] for x in con] + [x[0] for x in sin]
    cnt = 0
    for _ in range(N_SHUFFLE):
        random.shuffle(pool)
        sub = pool[:n1]
        resto = pool[n1:]
        d = sum(sub) / n1 - sum(resto) / len(resto)
        if abs(d) >= abs(diff_obs):
            cnt += 1
    return cnt / N_SHUFFLE


def split_half(vals: list) -> tuple:
    items = sorted(vals, key=lambda x: x[2])
    n = len(items)
    half = n // 2
    m1 = sum(x[0] for x in items[:half]) / max(half, 1)
    m2 = sum(x[0] for x in items[half:]) / max(n - half, 1)
    return round(m1, 4), round(m2, 4)


def evaluar_gate(matched: dict, clave_con: str, clave_sin: str) -> list:
    resultados = []
    for key, d in matched.items():
        con, sin = d[clave_con], d[clave_sin]
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
            "key": key, "n_grupo": n1, "hit_grupo": round(hit1, 4),
            "pnl_medio_grupo": pnl_m1, "n_resto": n2,
            "hit_resto": round(hit2, 4), "pnl_medio_resto": pnl_m2,
            "diff_hit_pp": round((hit1 - hit2) * 100, 2),
            "p_shuffle": round(p_shuffle, 5),
            "split_half_grupo": sh1,
        })
    m = len(resultados)
    resultados.sort(key=lambda r: r["p_shuffle"])
    prev = 1.0
    for i in range(m - 1, -1, -1):
        r = resultados[i]
        q = min(r["p_shuffle"] * m / (i + 1), prev)
        prev = q
        r["p_bh"] = round(q, 5)
        r["significativo"] = q < 0.05
    return resultados


def main():
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] cargando fuentes...")
    fade_by_key = cargar_fade_by_key()
    matched = cargar_matched(fade_by_key)
    print(f"fade_by_key: {len(fade_by_key)} | familias con datos: {len(matched)}")

    res_mejora = evaluar_gate(matched, "con_mejora", "sin_mejora")
    for r in res_mejora:
        r["veredicto"] = "confirmado" if (r["significativo"] and r["diff_hit_pp"] > 0) else "no_significativo"
    n_conf_mejora = sum(1 for r in res_mejora if r["veredicto"] == "confirmado")

    res_empeora = evaluar_gate(matched, "con_empeora", "sin_empeora")
    for r in res_empeora:
        r["veredicto"] = "veto_confirmado" if (r["significativo"] and r["diff_hit_pp"] < 0) else "no_significativo"
    n_conf_empeora = sum(1 for r in res_empeora if r["veredicto"] == "veto_confirmado")

    print(f"MEJORA -- familias evaluadas: {len(res_mejora)} | confirmadas BH-FDR: {n_conf_mejora}")
    print(f"EMPEORA (veto) -- familias evaluadas: {len(res_empeora)} | veto confirmado BH-FDR: {n_conf_empeora}")

    OUT.write_text(json.dumps({
        "actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "umbral_mejora": UMBRAL_MEJORA, "umbral_empeora": UMBRAL_EMPEORA, "n_min": N_MIN,
        "mejora": {
            "n_familias_evaluadas": len(res_mejora), "n_confirmadas": n_conf_mejora,
            "resultados": sorted(res_mejora, key=lambda r: -r["diff_hit_pp"]),
        },
        "empeora_veto": {
            "n_familias_evaluadas": len(res_empeora), "n_veto_confirmado": n_conf_empeora,
            "resultados": sorted(res_empeora, key=lambda r: r["diff_hit_pp"]),
        },
    }, indent=1, ensure_ascii=False), encoding="utf-8")

    print(f"\nTOP 15 MEJORA (con_mejora gana vs resto):")
    print(f"{'familia':45s} {'n_con':>6s} {'hit_con':>8s} {'n_resto':>7s} {'hit_resto':>9s} {'diff':>7s} {'p_bh':>8s}")
    for r in sorted(res_mejora, key=lambda r: -r["diff_hit_pp"])[:15]:
        print(f"{r['key']:45s} {r['n_grupo']:6d} {r['hit_grupo']*100:7.1f}% "
              f"{r['n_resto']:7d} {r['hit_resto']*100:8.1f}% {r['diff_hit_pp']:+6.1f}pp {r['p_bh']:8.4f}")

    print(f"\nTOP 15 EMPEORA/VETO (con_empeora pierde vs resto):")
    print(f"{'familia':45s} {'n_emp':>6s} {'hit_emp':>8s} {'n_resto':>7s} {'hit_resto':>9s} {'diff':>7s} {'p_bh':>8s}")
    for r in sorted(res_empeora, key=lambda r: r["diff_hit_pp"])[:15]:
        print(f"{r['key']:45s} {r['n_grupo']:6d} {r['hit_grupo']*100:7.1f}% "
              f"{r['n_resto']:7d} {r['hit_resto']*100:8.1f}% {r['diff_hit_pp']:+6.1f}pp {r['p_bh']:8.4f}")


if __name__ == "__main__":
    main()
