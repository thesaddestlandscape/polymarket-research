#!/usr/bin/env python3
"""
analisis_bot_consenso_gate_momentum_ballena.py — 26-Ago, propuesta #2
aprobada por Javi ("tiene sentido hacerlo para toda la familia"), tras
el hallazgo del día: dentro de MOMENTUM_IBS_5M_BALLENA, el bucket de
precio [0.40,0.50) muestra una diferencia grande entre señales donde
`bot_consenso_lado` COINCIDE con la dirección de la decisión (n=81,
hit=64,2%, wilson90lo=55,1%>breakeven=45,3%, p=0,0005) vs DISCREPA
(n=71, hit=28,2%, muy por debajo). 6/6 monedas van en la misma
dirección, aunque cada una sola tiene n insuficiente (6-23) para
confirmar por separado.

GENERALIZADO a toda la familia (no solo SOL#5min#BUY_YES, la única hoy
en pares_permitidos_live) -- mismo criterio que gate_bucket_propio.py:
"NO crear tablas de zonas hardcodeadas por ejecutor", el mecanismo se
autoextiende a cualquier tupla de la familia que llegue a vivo en el
futuro sin tocar código de nuevo.

Bucketiza por (activo, marco, decisión, bucket_precio 0.05,
bot_consenso_coincide) -- DOS dimensiones (precio Y consenso), rigor
Wilson90+binomial+split-half, mismo patrón que gate_bucket_propio.py.

Puramente observacional -- NO toca prob_yes/stake/pares_permitidos_
live. Conectar cualquier veredicto "bueno_confirmado" a la ejecución
real de MOMENTUM_IBS_5M_BALLENA#SOL#5min#BUY_YES (la única tupla live
hoy) requiere aprobación explícita de Javi + /code-review, igual que
cualquier cambio de prob_yes/stake de una tupla live (manual del
proyecto, CLAUDE.md).
"""
import csv
import json
import math
import sys
from collections import defaultdict
from math import comb
from pathlib import Path

csv.field_size_limit(sys.maxsize)

REPO = Path(__file__).resolve().parent
RESULTS_PATH = REPO / "data/shadow/results.csv"
OUT_PATH = REPO / "data/shadow/bot_consenso_gate_momentum_ballena.json"

STRATEGY = "MOMENTUM_IBS_5M_BALLENA"
N_MIN = 15
Z90 = 1.645
BUCKET_STEP = 0.05


def bucket(p: float) -> str:
    b = round((p // BUCKET_STEP) * BUCKET_STEP, 2)
    return f"{b:.2f}"


def wilson_lo(p: float, n: int, z: float = Z90) -> float:
    if n == 0:
        return 0.0
    denom = 1 + z * z / n
    center = p + z * z / (2 * n)
    adj = z * math.sqrt(max(p * (1 - p) / n, 0) + z * z / (4 * n * n))
    return (center - adj) / denom


def binom_sf(k: int, n: int, p: float) -> float:
    p = min(max(p, 1e-9), 1 - 1e-9)
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def main() -> int:
    grupos = defaultdict(list)  # (subtype, decision, bucket, coincide) -> [(acierto,pnl,ts)]
    with open(RESULTS_PATH) as f:
        r = csv.DictReader(f)
        for row in r:
            if row["strategy"] != STRATEGY:
                continue
            acierto = row.get("acierto")
            pnl = row.get("pnl_neto")
            if acierto in ("", None) or pnl in ("", None):
                continue
            try:
                feat = json.loads(row["features"]) if row["features"] else {}
            except Exception:
                continue
            lado = feat.get("bot_consenso_lado")
            if lado not in ("Up", "Down"):
                continue
            decision = row["decision"]
            try:
                py = float(row["precio_yes_mercado"])
            except (TypeError, ValueError):
                continue
            coincide = (decision == "BUY_YES" and lado == "Up") or (decision == "BUY_NO" and lado == "Down")
            key = (row["subtype"], decision, bucket(py), coincide)
            grupos[key].append((int(float(acierto)), float(pnl), row.get("prediction_timestamp", "")))

    salida = {}
    n_confirmados = 0
    for (subtype, decision, b, coincide), items in grupos.items():
        n = len(items)
        tupla_str = f"{STRATEGY}#{subtype}#{decision}"
        salida.setdefault(tupla_str, {}).setdefault(b, {})
        etiqueta = "coincide" if coincide else "discrepa"
        if n < N_MIN:
            salida[tupla_str][b][etiqueta] = {"n": n, "veredicto": "n_insuficiente"}
            continue
        hit = sum(x[0] for x in items) / n
        pnl_medio = sum(x[1] for x in items) / n
        breakeven = float(b) + BUCKET_STEP / 2  # aproximación: centro del bucket de precio
        wlo = wilson_lo(hit, n)
        k = sum(x[0] for x in items)
        p_binom = binom_sf(k, n, breakeven)
        items_sorted = sorted(items, key=lambda x: x[2])
        half = n // 2
        m1 = sum(x[1] for x in items_sorted[:half]) / half if half else None
        m2 = sum(x[1] for x in items_sorted[half:]) / (n - half) if (n - half) else None
        veredicto = "sin_concluir"
        if coincide and wlo > breakeven and p_binom < 0.05 and m1 is not None and m1 > 0 and m2 > 0:
            veredicto = "bueno_confirmado"
            n_confirmados += 1
        elif (not coincide) and hit < breakeven and p_binom > 0.95:
            veredicto = "malo_confirmado"
        salida[tupla_str][b][etiqueta] = {
            "n": n, "hit": round(hit, 4), "pnl_medio": round(pnl_medio, 4),
            "breakeven_aprox": round(breakeven, 4), "wilson90lo": round(wlo, 4),
            "p_binomial": round(p_binom, 4),
            "split_half": [round(m1, 4), round(m2, 4)] if m1 is not None else None,
            "veredicto": veredicto,
        }

    OUT_PATH.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Tuplas de la familia con datos: {len(salida)}")
    print(f"Celdas (coincide/discrepa) 'bueno_confirmado': {n_confirmados}")
    print(f"Guardado en {OUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
