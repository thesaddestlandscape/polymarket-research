#!/usr/bin/env python3
"""
analisis_wallet_quirurgico_precio_timing_22jul.py -- desagregación
quirúrgica por wallet: precio fino (bucket 0.05) x timing relativo
(TEMPRANO/MEDIO/TARDIO dentro del marco), comparado contra la POBLACIÓN
TOTAL en esa misma celda (activo, marco, precio_bucket, timing_bucket),
excluyendo a la propia wallet.

Motivo (22-Jul, petición explícita Javi tras investigar las 15 wallets
CONFIRMADO de vigia_wallet_edge_forward.py): el edge_pp agregado de ese
vigía mezcla todo el rango de precio de una wallet en un solo número --
con una wallet de distribución bimodal (favoritos + longshots) eso
produce un "edge negativo confirmado, p<0.01" que en realidad es el
sesgo longshot DE TODO EL MERCADO, no algo específico de la wallet (ver
idea_vigia_wallet_edge_forward_simpson_22jul). Este script corrige eso:
en vez de comparar contra un coinflip 50/50, compara cada celda de la
wallet contra la población real en esa celda -- lo que sobrevive es
EXCESO sobre el sesgo ya conocido, la única parte nueva y potencialmente
explotable (fade/follow específico de esa wallet en ese nicho preciso).

Test: two-proportion z-test (wallet_hit vs poblacion_hit_excluyendo_wallet
en la misma celda) + corrección Benjamini-Hochberg (FDR=0.10, misma
función y mismo umbral que shadow_postmortem._benjamini_hochberg -- no se
inventa un criterio nuevo) sobre TODAS las celdas probadas de TODAS las
wallets, porque se testean cientos de hipótesis a la vez.

Universo: las wallets ya en el roster de vigia_wallet_edge_forward.py
(data/shadow/wallet_edge_forward_state.json) -- ya filtradas por volumen o
significancia, no hace falta re-filtrar aquí.

Puramente análisis/shadow, solo lectura -- no toca live_trade.py,
config_live.json ni ninguna decisión.

Uso: python3 analisis_wallet_quirurgico_precio_timing_22jul.py [--min-n-wallet 15] [--min-n-poblacion 30]
"""
import argparse
import json
import math
from collections import defaultdict
from pathlib import Path

DIR = Path(__file__).parent
HIST = DIR / "data/shadow/ballenas_timing_history.csv"
ROSTER = DIR / "data/shadow/wallet_edge_forward_state.json"
OUT = DIR / "data/shadow/wallet_quirurgico_precio_timing.json"

MARCO_DUR_MIN = {"5m": 5, "15m": 15, "60m": 60, "240m": 240}
FDR = 0.10


def _precio_bucket(p: float) -> float:
    b = math.floor(p * 20) / 20
    return max(0.0, min(0.95, b))


def _timing_bucket(restante_min: float, marco: str) -> str | None:
    dur = MARCO_DUR_MIN.get(marco)
    if dur is None or dur <= 0:
        return None
    frac = restante_min / dur
    if frac < 1 / 3:
        return "TARDIO"
    if frac < 2 / 3:
        return "MEDIO"
    return "TEMPRANO"


def _z_two_prop(h1: int, n1: int, h2: int, n2: int) -> float:
    """Two-proportion z-test, dos colas. p-valor via erf (stdlib, sin scipy)."""
    if n1 == 0 or n2 == 0:
        return 1.0
    p1, p2 = h1 / n1, h2 / n2
    p_pool = (h1 + h2) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1 / n1 + 1 / n2))
    if se == 0:
        return 1.0
    z = (p1 - p2) / se
    # p-valor de dos colas de una normal estándar
    p_val = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    return p_val


def _benjamini_hochberg(pvals: list, fdr: float = FDR) -> list:
    n = len(pvals)
    if n == 0:
        return []
    indexed = sorted(range(n), key=lambda i: pvals[i])
    keep = [False] * n
    cutoff = -1
    for rank, i in enumerate(indexed, start=1):
        if pvals[i] <= fdr * rank / n:
            cutoff = rank
    if cutoff >= 0:
        for rank, i in enumerate(indexed, start=1):
            if rank <= cutoff:
                keep[i] = True
    return keep


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--min-n-wallet", type=int, default=15)
    ap.add_argument("--min-n-poblacion", type=int, default=30)
    args = ap.parse_args()

    with open(ROSTER, encoding="utf-8") as f:
        roster = json.load(f)
    wallets_universo = {v["wallet"].lower() for v in roster.values()}
    print(f"[wallet_quirurgico] universo: {len(wallets_universo)} wallets (roster de vigia_wallet_edge_forward)")

    # PASO 1: colapsar a una fila por (wallet, condition_id) -- si no, fills
    # múltiples en el MISMO mercado se cuentan como observaciones independientes
    # y n queda inflado de forma ilusoria (ej. 15 fills en 1 solo mercado ->
    # "n=15" cuando el evento real resuelto es 1 solo). Verificado 22-Jul: los
    # candidatos más "espectaculares" de la primera pasada (sin colapsar)
    # resultaron ser justo esto -- 1 wallet, 1 día, 1 condition_id.
    por_mercado = {}  # (wallet, condition_id) -> dict(activo, marco, n_fills, suma_precio, restante_primera, acierto, ts_primera)
    n_leidas = 0
    with open(HIST, encoding="utf-8") as f:
        import csv
        reader = csv.DictReader(f)
        for row in reader:
            n_leidas += 1
            marco = row["marco"]
            if marco not in MARCO_DUR_MIN:
                continue
            try:
                precio = float(row["precio"])
                restante = float(row["restante_min"])
            except (ValueError, TypeError):
                continue
            wallet = row["wallet"].lower()
            key = (wallet, row["condition_id"])
            hit = 1 if row["acierto"] in ("1", "1.0", "True") else 0
            ts = row.get("ts_trade", "")
            e = por_mercado.get(key)
            if e is None:
                por_mercado[key] = {
                    "activo": row["activo"], "marco": marco,
                    "n_fills": 1, "suma_precio": precio,
                    "restante_primera": restante, "acierto": hit, "ts_primera": ts,
                }
            else:
                e["n_fills"] += 1
                e["suma_precio"] += precio
                # "primera" fill = ts_trade más temprano (restante_min más alto,
                # el mercado cuenta hacia atrás hasta el cierre)
                if ts and (not e["ts_primera"] or ts < e["ts_primera"]):
                    e["ts_primera"] = ts
                    e["restante_primera"] = restante

    print(f"[wallet_quirurgico] filas leídas={n_leidas} -> {len(por_mercado)} posiciones (wallet,mercado) tras colapsar fills")

    # celda global (activo, marco, precio_bucket, timing_bucket) -> [n, hits, suma_precio]
    baseline = defaultdict(lambda: [0, 0, 0.0])
    # (wallet, celda) -> [n, hits, suma_precio]
    por_wallet = defaultdict(lambda: [0, 0, 0.0])
    # (wallet, celda) -> set de días distintos (para detectar concentración temporal)
    dias_por_wallet_celda = defaultdict(set)

    n_usadas = 0
    for (wallet, condition_id), e in por_mercado.items():
        marco = e["marco"]
        precio_medio_pos = e["suma_precio"] / e["n_fills"]
        tb = _timing_bucket(e["restante_primera"], marco)
        if tb is None:
            continue
        pb = _precio_bucket(precio_medio_pos)
        hit = e["acierto"]
        activo = e["activo"]
        celda = (activo, marco, pb, tb)

        bl = baseline[celda]
        bl[0] += 1
        bl[1] += hit
        bl[2] += precio_medio_pos
        n_usadas += 1

        if wallet in wallets_universo:
            we = por_wallet[(wallet, celda)]
            we[0] += 1
            we[1] += hit
            we[2] += precio_medio_pos
            if e["ts_primera"]:
                dias_por_wallet_celda[(wallet, celda)].add(e["ts_primera"][:10])

    print(f"[wallet_quirurgico] posiciones usadas={n_usadas} celdas_poblacion={len(baseline)} celdas_wallet={len(por_wallet)}")

    candidatos = []  # dict con todo, antes de BH-FDR
    for (wallet, celda), (wn, wh, wsp) in por_wallet.items():
        if wn < args.min_n_wallet:
            continue
        bn, bh, bsp = baseline[celda]
        pop_n = bn - wn
        pop_h = bh - wh
        pop_sp = bsp - wsp
        if pop_n < args.min_n_poblacion:
            continue
        wallet_hit = wh / wn
        wallet_precio = wsp / wn
        wallet_edge_pp = 100 * (wallet_hit - wallet_precio)
        pop_hit = pop_h / pop_n
        pop_precio = pop_sp / pop_n
        pop_edge_pp = 100 * (pop_hit - pop_precio)
        excess_edge_pp = wallet_edge_pp - pop_edge_pp
        pval = _z_two_prop(wh, wn, pop_h, pop_n)
        activo, marco, pb, tb = celda
        dias_distintos = len(dias_por_wallet_celda.get((wallet, celda), set()))
        candidatos.append({
            "wallet": wallet, "activo": activo, "marco": marco,
            "precio_bucket": round(pb, 2), "timing": tb,
            "dias_distintos": dias_distintos,
            "wallet_n": wn, "wallet_hit": round(wallet_hit, 4),
            "wallet_precio_medio": round(wallet_precio, 4),
            "wallet_edge_pp": round(wallet_edge_pp, 2),
            "poblacion_n": pop_n, "poblacion_hit": round(pop_hit, 4),
            "poblacion_edge_pp": round(pop_edge_pp, 2),
            "excess_edge_pp": round(excess_edge_pp, 2),
            "p_value": pval,
        })

    print(f"[wallet_quirurgico] candidatos con n_wallet>={args.min_n_wallet} y n_poblacion>={args.min_n_poblacion}: {len(candidatos)}")

    pvals = [c["p_value"] for c in candidatos]
    keep = _benjamini_hochberg(pvals, FDR)
    sobrevive = [c for c, k in zip(candidatos, keep) if k]
    sobrevive.sort(key=lambda c: -abs(c["excess_edge_pp"]))

    print(f"[wallet_quirurgico] sobreviven BH-FDR({FDR}): {len(sobrevive)}\n")

    positivos = [c for c in sobrevive if c["excess_edge_pp"] > 0]
    negativos = [c for c in sobrevive if c["excess_edge_pp"] < 0]

    print(f"=== EXCESO POSITIVO (wallet mejor que la población en su propio nicho) — top 15 de {len(positivos)} ===")
    for c in positivos[:15]:
        print(f"  {c['wallet'][:12]}.. {c['activo']}#{c['marco']} precio[{c['precio_bucket']:.2f},{c['precio_bucket']+0.05:.2f}) {c['timing']}: "
              f"wallet n={c['wallet_n']} ({c['dias_distintos']} dias) hit={c['wallet_hit']:.1%} edge_pp={c['wallet_edge_pp']:+.2f} | "
              f"poblacion n={c['poblacion_n']} hit={c['poblacion_hit']:.1%} edge_pp={c['poblacion_edge_pp']:+.2f} | "
              f"EXCESO={c['excess_edge_pp']:+.2f}pp p={c['p_value']:.4f}")

    print(f"\n=== EXCESO NEGATIVO (wallet peor que la población en su propio nicho -- debilidad quirúrgica) — top 15 de {len(negativos)} ===")
    for c in negativos[:15]:
        print(f"  {c['wallet'][:12]}.. {c['activo']}#{c['marco']} precio[{c['precio_bucket']:.2f},{c['precio_bucket']+0.05:.2f}) {c['timing']}: "
              f"wallet n={c['wallet_n']} ({c['dias_distintos']} dias) hit={c['wallet_hit']:.1%} edge_pp={c['wallet_edge_pp']:+.2f} | "
              f"poblacion n={c['poblacion_n']} hit={c['poblacion_hit']:.1%} edge_pp={c['poblacion_edge_pp']:+.2f} | "
              f"EXCESO={c['excess_edge_pp']:+.2f}pp p={c['p_value']:.4f}")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"candidatos_totales": len(candidatos), "sobreviven_bhfdr": sobrevive}, f, indent=2)
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
