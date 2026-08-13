#!/usr/bin/env python3
"""
analisis_cluster_wallets_evento_12ago.py — análisis retrospectivo (shadow
puro, no toca dinero ni config) del detector de clúster de wallets por
mercado concreto (idea_cluster_wallets_y_cross_market_evento_12ago,
pendiente 12-Ago). Pregunta: cuando 3+ wallets con edge YA VALIDADO
(wallet_edge_score_por_activo_marco.json, sig_bhfdr=True) convergen en el
MISMO mercado (condition_id) dentro de su ventana de vida, ¿el voto
mayoritario de ese clúster predice el resultado mejor que el ruido?
Distinto de smart_money_consensus.json (agregado por moneda, no por
mercado/evento concreto).

Rigor aplicado (petición explícita Javi, "no la cagues"):
  - TWAP: filtra `_es_pre_twap_hist` (reusa wallet_edge_tracker.py) en
    5m/15m/240m antes de contar cualquier trade.
  - Desagregado por (activo, marco) SIEMPRE antes de mirar el agregado
    (CLAUDE.md pt.17) — nunca mezclar monedas/marcos.
  - Desagregado por micro-bucket de precio (0.05) del precio MEDIO del
    clúster en el momento de formarse.
  - Timing/baja latencia: para cada clúster, calcula restante_min en el
    momento en que se completa (la wallet Nº3, el trade que activa la
    señal) — si ese margen es demasiado corto (mediana <1min, mismo
    patrón que wallets snipe de último segundo ya descartadas en P31),
    la señal no es accionable aunque prediga bien.
  - shuffle test (permutación) sobre el voto mayoritario vs outcome real,
    por (activo,marco) con n>=15.

Salida: imprime tabla por (activo,marco) y guarda
data/shadow/cluster_wallets_evento_12ago.json para que sesiones futuras
no repitan el análisis desde cero.
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np

csv.field_size_limit(sys.maxsize)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from wallet_edge_tracker import _es_pre_twap_hist  # noqa: E402

REPO = Path(__file__).resolve().parent
HIST = REPO / "data" / "shadow" / "ballenas_timing_history.csv"
EDGE_SCORE = REPO / "data" / "shadow" / "wallet_edge_score_por_activo_marco.json"
OUT = REPO / "data" / "shadow" / "cluster_wallets_evento_12ago.json"

MIN_WALLETS_CLUSTER = 3
N_MIN_GATE = 15


def truthy(v) -> bool:
    return str(v).strip().lower() in ("1", "true", "yes")


def cargar_wallets_validadas() -> dict:
    g = json.loads(EDGE_SCORE.read_text())
    out = {}
    for v in g.values():
        if v.get("sig_bhfdr"):
            out[(v["wallet"], v["activo"], v["marco"])] = v["edge_pp"]
    return out


def cargar_clusters(edge_validado: dict) -> dict:
    """market_id -> lista de filas (solo wallets validadas, post-TWAP)."""
    por_mercado = defaultdict(list)
    with open(HIST, encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            key = (row["wallet"], row["activo"], row["marco"])
            if key not in edge_validado:
                continue
            if _es_pre_twap_hist(row["marco"], row.get("ts_trade", "")):
                continue
            por_mercado[row["condition_id"]].append(row)
    return {mid: rows for mid, rows in por_mercado.items()
            if len({r["wallet"] for r in rows}) >= MIN_WALLETS_CLUSTER}


def analizar(clusters: dict) -> dict:
    por_activo_marco = defaultdict(list)  # (activo,marco) -> [(precio_medio, restante_min_formacion, mayoria_yes, outcome_yes, n_wallets)]

    for mid, rows in clusters.items():
        activo = rows[0]["activo"]
        marco = rows[0]["marco"]
        # una fila por wallet: si una wallet aparece varias veces, quedarse
        # con la de menor restante_min (la más tardía/informada) para el
        # voto, pero usar la PRIMERA vez que se completa el clúster para el timing
        por_wallet = {}
        for r in rows:
            por_wallet[r["wallet"]] = r
        n_wallets = len(por_wallet)

        votos_yes = sum(1 for r in por_wallet.values() if truthy(r["compro_yes"]))
        votos_no = n_wallets - votos_yes
        if votos_yes == votos_no:
            continue  # empate, sin voto mayoritario

        mayoria_yes = votos_yes > votos_no
        r0 = next(iter(por_wallet.values()))
        outcome_yes = truthy(r0["compro_yes"]) == truthy(r0["acierto"])

        precios = [float(r["precio"]) for r in por_wallet.values()
                   if r.get("precio") not in ("", None)]
        precio_medio = sum(precios) / len(precios) if precios else None

        # timing de formación: ordenar trades por ts_trade, el instante en
        # que se alcanza la 3ª wallet DISTINTA es cuando la señal se activa
        vistos = set()
        restante_formacion = None
        for r in sorted(rows, key=lambda x: x["ts_trade"]):
            vistos.add(r["wallet"])
            if len(vistos) >= MIN_WALLETS_CLUSTER:
                try:
                    restante_formacion = float(r["restante_min"])
                except (TypeError, ValueError):
                    restante_formacion = None
                break

        por_activo_marco[(activo, marco)].append(
            (precio_medio, restante_formacion, mayoria_yes, outcome_yes, n_wallets))

    resultado = {}
    for (activo, marco), obs in sorted(por_activo_marco.items()):
        n = len(obs)
        hits = sum(1 for _, _, mv, ov, _ in obs if mv == ov)
        hit_rate = hits / n if n else None

        rng = np.random.default_rng(hash((activo, marco)) & 0xFFFFFFFF)
        p_shuffle = None
        if n >= N_MIN_GATE:
            outcomes = np.array([1 if ov else 0 for _, _, _, ov, _ in obs])
            votos = np.array([1 if mv else 0 for _, _, mv, _, _ in obs])
            obs_hit = np.mean(votos == outcomes)
            sims = []
            for _ in range(10000):
                perm = rng.permutation(outcomes)
                sims.append(np.mean(votos == perm))
            sims = np.array(sims)
            p_shuffle = float(np.mean(sims >= obs_hit))

        restantes = [rf for _, rf, _, _, _ in obs if rf is not None]
        restante_mediana = float(np.median(restantes)) if restantes else None

        # desagregado por micro-bucket de precio (0.05)
        buckets = defaultdict(list)
        for precio_medio, _, mv, ov, _ in obs:
            if precio_medio is None:
                continue
            import math
            b = round(math.floor(precio_medio / 0.05) * 0.05, 2)
            buckets[b].append(mv == ov)
        buckets_resumen = {
            str(b): {"n": len(lst), "hit": round(sum(lst) / len(lst), 4)}
            for b, lst in sorted(buckets.items())
        }

        resultado[f"{activo}#{marco}"] = {
            "n": n, "hit_rate": round(hit_rate, 4) if hit_rate is not None else None,
            "p_shuffle": p_shuffle,
            "restante_min_mediana_formacion": round(restante_mediana, 2) if restante_mediana is not None else None,
            "buckets_precio": buckets_resumen,
        }
    return resultado


def main() -> int:
    edge_validado = cargar_wallets_validadas()
    print(f"wallets con edge validado (wallet,activo,marco): {len(edge_validado)}")
    clusters = cargar_clusters(edge_validado)
    print(f"mercados con clúster (>= {MIN_WALLETS_CLUSTER} wallets validadas distintas, post-TWAP): {len(clusters)}")

    resultado = analizar(clusters)
    OUT.write_text(json.dumps(resultado, indent=1, ensure_ascii=False))

    print()
    print(f"{'activo#marco':16s} {'n':>5s} {'hit':>7s} {'p_shuf':>7s} {'restante_min~':>14s}")
    for k, v in sorted(resultado.items(), key=lambda kv: -kv[1]["n"]):
        hit = v["hit_rate"]
        ps = v["p_shuffle"]
        rm = v["restante_min_mediana_formacion"]
        flag = ""
        if v["n"] < N_MIN_GATE:
            flag = "  (n<15, exploratorio)"
        print(f"{k:16s} {v['n']:5d} {hit*100 if hit else 0:6.1f}% "
              f"{ps if ps is not None else '  --':>7} {rm if rm is not None else '?':>14}{flag}")
        for b, bv in v["buckets_precio"].items():
            if bv["n"] >= 5:
                print(f"    precio[{b},{float(b)+0.05:.2f}) n={bv['n']:3d} hit={bv['hit']*100:.1f}%")

    return 0


if __name__ == "__main__":
    sys.exit(main())
