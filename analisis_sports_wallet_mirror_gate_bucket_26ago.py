#!/usr/bin/env python3
"""
analisis_sports_wallet_mirror_gate_bucket_26ago.py — 26-Ago, petición
explícita Javi: "tenemos que instrumentar lo de sports con los
hallazgos de hoy de LoL". Wallet Mirror#LoL cruzó significancia en
agregado (n=946, pnl+0.166€/tr, p=0.0398, fill 73%) pero CLAUDE.md
pt.17 exige desagregar por micro-bucket de precio ANTES de dar nada por
bueno -- un agregado positivo puede (como ha pasado 5 veces hoy en
cripto) estar diluido o directamente ser negativo en la mayoría de
buckets y positivo solo en uno estrecho.

Mismo patrón que gate_bucket_propio.py (cripto): bucketiza por
(categoria, tipo, bucket_precio 0.05), exige fill-ability real
(ratio_vs_stake_mirror>=5x) desde el principio, rigor Wilson90 +
binomial + split-half. Generaliza a TODAS las categorías de sports, no
solo LoL -- mismo criterio "nunca hardcodear una tupla" ya aplicado
hoy en cripto.

Salida: data/sports/wallet_mirror_gate_bucket.json. Solo lectura --
NO conecta a ningún ejecutor todavía (sports no tiene infraestructura
de dinero real desplegada, es shadow puro).
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
DRY_RUN = REPO / "data/sports/wallet_mirror_sniper_dry_run.csv"
OUT_PATH = REPO / "data/sports/wallet_mirror_gate_bucket.json"

N_MIN = 15
F_KELLY = 0.10  # 29-Ago: mismo default que analisis_log_growth.py/gate_bucket_propio.py (P28/CLAUDE.md pt.14)
RATIO_MIN = 5.0
# FEE verificado 26-Ago con condition_ids reales del propio dataset contra gamma-api
# (feeType/feeSchedule): sports usa "sports_fees_v3" rate=0.05 en CS/LoL/Tennis/Dota/
# Valorant/Cricket/UFC/ATP/EPL (9/10 categorías muestreadas) -- NO el 0.07 de cripto,
# que es un supuesto copiado sin verificar (mismo aviso ya dejado en el fichero gemelo
# de weather). Único outlier visto: F1 usa "sports_fees_v2" rate=0.03 (volumen
# despreciable hoy, 1 señal). 0.05 es la mejor aproximación única disponible; no cambia
# qué buckets se confirman (breakeven/hit no dependen de FEE aquí) pero corrige el
# pnl_medio reportado, que con 0.07 estaba sistemáticamente infravalorado.
FEE = 0.05
STAKE = 1.0
Z90 = 1.645
STEP = 0.05


def bucket(p: float) -> str:
    b = round((p // STEP) * STEP, 2)
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


def payout_win(precio: float) -> float:
    return STAKE * (1 - precio) / precio - STAKE * FEE * (1 - precio)


def main() -> int:
    grupos = defaultdict(list)
    with open(DRY_RUN, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("acierto") not in ("0", "1"):
                continue
            try:
                ratio = float(row["ratio_vs_stake_mirror"])
                ask = float(row["mejor_ask_mirror"])
            except (TypeError, ValueError, KeyError):
                continue
            if ratio < RATIO_MIN:
                continue
            if not (0.01 < ask < 0.99):
                continue
            key = (row["categoria"], row["tipo"], bucket(ask))
            acierto = int(row["acierto"])
            pnl = payout_win(ask) if acierto == 1 else -STAKE
            grupos[key].append((acierto, pnl, ask, row.get("resolved_ts") or row.get("timestamp_utc", "")))

    salida = {}
    n_confirmados_buenos = 0
    n_confirmados_malos = 0
    pvals = []
    g_kelly_raw = {}  # (tupla_str, b) -> g_kelly SIN redondear, para el veto de abajo
    for (categoria, tipo, b), items in grupos.items():
        n = len(items)
        tupla_str = f"{categoria}#{tipo}"
        salida.setdefault(tupla_str, {})
        if n < N_MIN:
            salida[tupla_str][b] = {"n": n, "veredicto": "n_insuficiente"}
            continue
        hit = sum(x[0] for x in items) / n
        pnl_medio = sum(x[1] for x in items) / n
        # 29-Ago (paridad con el mismo hueco cerrado en WALLET_MIRROR cripto,
        # ver analisis_wallet_mirror_gate_bucket_10ago.py): payout asimétrico
        # (Kelly g(f)) -- pnl_medio lineal positivo puede convivir con
        # crecimiento compuesto negativo (hit-rate alto, pérdidas grandes
        # raras). Misma fórmula g(f)=mean(ln(1+f*x)), reusando x=pnl ya
        # calculado por trade (items[i][1], mismo concepto normalizado que
        # analisis_log_growth.py::_retorno()).
        g_kelly = sum(math.log(1 + F_KELLY * x[1]) for x in items) / n
        g_kelly_raw[(tupla_str, b)] = g_kelly
        ask_medio = sum(x[2] for x in items) / n
        breakeven = ask_medio
        wlo = wilson_lo(hit, n)
        k = sum(x[0] for x in items)
        p_binom = binom_sf(k, n, breakeven)
        items_sorted = sorted(items, key=lambda x: x[3])
        half = n // 2
        m1 = sum(x[1] for x in items_sorted[:half]) / half
        m2 = sum(x[1] for x in items_sorted[half:]) / (n - half)
        pvals.append(((tupla_str, b), p_binom, hit > breakeven))
        salida[tupla_str][b] = {
            "n": n, "hit": round(hit, 4), "pnl_medio": round(pnl_medio, 4),
            "g_kelly_f10": round(g_kelly, 5),
            "ask_medio": round(ask_medio, 4), "wilson90lo": round(wlo, 4),
            "p_binomial": round(p_binom, 4), "split_half": [round(m1, 4), round(m2, 4)],
        }

    # BH-FDR sobre la familia completa de buckets con n>=N_MIN
    m = len(pvals)
    if m:
        pvals_sorted = sorted(pvals, key=lambda x: x[1])
        prev_min = 1.0
        bh = {}
        for i in range(len(pvals_sorted) - 1, -1, -1):
            (key, p, mejor) = pvals_sorted[i]
            q = min(p * m / (i + 1), prev_min)
            prev_min = q
            bh[key] = q
        for tupla_str, buckets_dict in salida.items():
            for b, info in buckets_dict.items():
                if "p_binomial" not in info:
                    continue
                key = (tupla_str, b)
                q = bh.get(key, 1.0)
                info["p_bh"] = round(q, 4)
                m1, m2 = info["split_half"]
                mejor = info["hit"] > info["ask_medio"]
                if q < 0.05 and mejor and m1 > 0 and m2 > 0:
                    info["veredicto"] = "bueno_confirmado"
                    n_confirmados_buenos += 1
                elif q < 0.05 and not mejor and m1 < 0 and m2 < 0:
                    info["veredicto"] = "malo_confirmado"
                    n_confirmados_malos += 1
                else:
                    info["veredicto"] = "sin_concluir"
                # 29-Ago: veto de payout asimétrico -- degrada bueno_confirmado
                # si g_kelly(f=10%)<=0 pese a pnl_medio lineal positivo. Solo
                # puede degradar, nunca promover (mismo invariante que
                # gate_bucket_propio.py::_veto_fillable() señal #2 y su
                # gemelo en analisis_wallet_mirror_gate_bucket_10ago.py).
                # /code-review 29-Ago: comparar SIEMPRE contra g_kelly_raw
                # (sin redondear) -- info["g_kelly_f10"] redondeado a 5
                # decimales puede aplastar un valor positivo minúsculo a
                # 0.00000 y disparar el veto por error de redondeo, no por
                # payout asimétrico real.
                g_raw = g_kelly_raw.get(key)
                if info["veredicto"] == "bueno_confirmado" and g_raw is not None and g_raw <= 0:
                    info["veredicto"] = "malo_confirmado"
                    n_confirmados_buenos -= 1
                    n_confirmados_malos += 1

    OUT_PATH.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Categorías#tipo con datos: {len(salida)}")
    print(f"Tests con n>={N_MIN}: {m}")
    print(f"bueno_confirmado (BH-FDR): {n_confirmados_buenos} | malo_confirmado: {n_confirmados_malos}")
    print(f"Guardado en {OUT_PATH}")

    lol = {k: v for k, v in salida.items() if k.startswith("LoL#")}
    print("\n=== Detalle LoL ===")
    for tupla, buckets_dict in lol.items():
        for b, info in sorted(buckets_dict.items()):
            if info.get("n", 0) >= N_MIN:
                print(f"  {tupla} [{b},{float(b)+STEP:.2f}) n={info['n']} hit={info['hit']:.1%} "
                      f"pnl/tr={info['pnl_medio']:+.3f} p_bh={info.get('p_bh')} -> {info.get('veredicto')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
