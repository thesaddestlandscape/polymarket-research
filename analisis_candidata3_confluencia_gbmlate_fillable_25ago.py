#!/usr/bin/env python3
"""analisis_candidata3_confluencia_gbmlate_fillable_25ago.py -- Candidata 3
"gallina de los huevos de oro": ¿la confluencia de ballenas (direccion de
ballenas coincidiendo con la senal) rescata un sub-segmento con edge real
DENTRO del subconjunto ya fillable de las 4 tuplas GBM_LATE refutadas por
seleccion adversa (idea_gbm_late_bnb_doge_fillable_50_55_25ago)?

kelly_precio_gate.json YA se comprobo (25-Ago) que NO tiene estos buckets
como "confirmado" (shuffle_p=0.06/0.181, sin_concluir) -- la correccion de
sizing sola no aporta nada aqui, no se repite ese analisis.

Metodologia:
1. Colapsa libro_snapshots.csv por (market_id,strategy,direction) --
   PRIORIDAD canonica (libro_snapshots_prioridad.py), nunca contar filas.
2. Fillable real = motivo=="ejecutada" O ratio_vs_stake>=5x (mismo
   criterio que idea_gbm_late_bnb_doge_fillable_50_55_25ago).
3. Filtra a precio_plan en bucket [0.50,0.55).
4. Join market_id->condition_id via market_id_resolver (indice ya
   construido, sin llamadas de red).
5. Confluencia de ballenas = mayoria de trades en ballenas_timing_
   history.csv para ese condition_id compran el mismo lado que la senal
   (BUY_YES -> compro_yes mayoritario).
6. Outcome real de results.csv (acierto/pnl_neto) por (market_id,
   strategy,decision).
7. Compara pnl/hit CON confluencia vs SIN confluencia, desagregado por
   tupla y agregado, n>=15, shuffle test.

Solo lectura.
"""
import csv
import json
import sys
import zlib
from collections import defaultdict
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from libro_snapshots_prioridad import prio as _prio  # noqa: E402
from market_id_resolver import resolver_lote  # noqa: E402

SNAPSHOTS = REPO / "data/live/libro_snapshots.csv"
RESULTS = REPO / "data/shadow/results.csv"
BALLENAS = REPO / "data/shadow/ballenas_timing_history.csv"

TARGETS = [
    ("GBM_LATE_15M", "BNB#15min", "BUY_YES"),
    ("GBM_LATE_15M_TARDIO", "BNB#15min", "BUY_YES"),
    ("GBM_LATE_15M_ESPACIO_ATR", "DOGE#15min", "BUY_YES"),
    ("GBM_LATE_15M_MULTIHORIZONTE", "DOGE#15min", "BUY_YES"),
]
TARGET_SET = set(TARGETS)
BUCKET_LO, BUCKET_HI = 0.50, 0.55
N_MIN = 15


def shuffle_test(a, b, seed_key, iters=5000):
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    na, nb = len(a), len(b)
    diff_real = a.mean() - b.mean()
    todos = np.concatenate([a, b])
    idx = rng.random((iters, na + nb)).argsort(axis=1)
    perm = todos[idx]
    diffs = perm[:, :na].mean(axis=1) - perm[:, na:].mean(axis=1)
    p = float(np.mean(np.abs(diffs) >= abs(diff_real)))
    return float(diff_real), p


def main():
    # 1-2-3: colapsar señales por (market_id, strategy, subtype, direction)
    senales = {}
    with open(SNAPSHOTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            key4 = (r["strategy"], r["subtype"], r["direction"])
            if key4 not in TARGET_SET:
                continue
            try:
                precio = float(r.get("precio_plan") or "")
            except (TypeError, ValueError):
                continue
            if not (BUCKET_LO <= precio < BUCKET_HI):
                continue
            mkey = (r["market_id"], r["strategy"], r["subtype"], r["direction"])
            prev = senales.get(mkey)
            if prev is None or _prio(r["motivo"]) < _prio(prev["motivo"]):
                try:
                    ratio = float(r.get("ratio_vs_stake") or 0)
                except (TypeError, ValueError):
                    ratio = 0.0
                senales[mkey] = {"motivo": r["motivo"], "ratio": ratio}

    fillable = {}
    for mkey, s in senales.items():
        if s["motivo"] == "ejecutada" or s["ratio"] >= 5.0:
            fillable[mkey] = s
    print(f"Señales en bucket [0.50,0.55) colapsadas: {len(senales)} | fillable real: {len(fillable)}")

    if not fillable:
        print("Sin señales fillable -- nada que evaluar.")
        return

    # 4: resolver condition_id -- índice persistido está desactualizado
    # (max market_id=3.128.776, nuestros market_id son de agosto, más
    # nuevos) -- resolver_lote() usa el índice PRIMERO y solo pide a la
    # API los que falten (aquí, prácticamente todos), persistiendo el
    # resultado para que la próxima vez sea gratis.
    market_ids_necesarios = sorted({mkey[0] for mkey in fillable})
    print(f"Resolviendo {len(market_ids_necesarios)} market_id -> condition_id (API fallback, ~{len(market_ids_necesarios)*0.15:.0f}s)...")
    mapa = resolver_lote(market_ids_necesarios, usar_api_fallback=True)
    n_resueltos = sum(1 for mid in market_ids_necesarios if mapa.get(mid))
    print(f"market_id -> condition_id resueltos: {n_resueltos}/{len(market_ids_necesarios)}")

    # 5: cargar ballenas por condition_id (solo los que necesitamos)
    cids_necesarios = {mapa.get(mid) for mid in market_ids_necesarios if mapa.get(mid)}
    ballenas_por_cid = defaultdict(list)  # cid -> [(compro_yes)]
    with open(BALLENAS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            cid = r.get("condition_id")
            if cid in cids_necesarios:
                ballenas_por_cid[cid].append(r.get("compro_yes") == "1")

    n_con_ballenas = sum(1 for mid in market_ids_necesarios if mapa.get(mid) in ballenas_por_cid)
    print(f"señales fillable con ≥1 trade de ballenas en ese mercado: {n_con_ballenas}/{len(market_ids_necesarios)}")

    # 6: outcomes
    outcomes = {}
    with open(RESULTS, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            outcomes[(r["market_id"], r["strategy"], r["decision"])] = (
                int(r["acierto"]), float(r["pnl_neto"]))

    # 7: comparar con/sin confluencia
    por_tupla = defaultdict(lambda: {"con": [], "sin": [], "sin_ballenas": 0, "sin_outcome": 0})
    for mkey, s in fillable.items():
        market_id, strategy, subtype, direction = mkey
        out = outcomes.get((market_id, strategy, direction))
        if out is None:
            por_tupla[(strategy, subtype)]["sin_outcome"] += 1
            continue
        acierto, pnl = out
        cid = mapa.get(market_id)
        trades = ballenas_por_cid.get(cid, [])
        if not trades:
            por_tupla[(strategy, subtype)]["sin_ballenas"] += 1
            continue
        n_yes = sum(trades)
        n_no = len(trades) - n_yes
        # BUY_YES: confluencia si mayoría de ballenas compró YES (Up)
        confluye = n_yes > n_no
        d = por_tupla[(strategy, subtype)]
        (d["con"] if confluye else d["sin"]).append(pnl)

    print("\n--- Desagregado por tupla (CLAUDE.md pt.17) ---")
    todos_con, todos_sin = [], []
    for (strategy, subtype), d in por_tupla.items():
        n_c, n_s = len(d["con"]), len(d["sin"])
        print(f"\n{strategy}#{subtype}: n_con_ballenas={n_c} n_sin_confluencia={n_s} "
              f"(sin_dato_ballenas={d['sin_ballenas']} sin_outcome={d['sin_outcome']})")
        if n_c >= N_MIN:
            print(f"  CON confluencia: pnl_medio={np.mean(d['con']):+.3f}€ (n={n_c})")
        if n_s >= N_MIN:
            print(f"  SIN confluencia: pnl_medio={np.mean(d['sin']):+.3f}€ (n={n_s})")
        if n_c >= N_MIN and n_s >= N_MIN:
            diff, p = shuffle_test(d["con"], d["sin"], seed_key=f"{strategy}#{subtype}")
            print(f"  diff={diff:+.3f}€ p_shuffle={p:.4f}")
        todos_con.extend(d["con"])
        todos_sin.extend(d["sin"])

    print(f"\n--- Agregado (4 tuplas juntas, exploratorio -- ver desagregado arriba para el veredicto real) ---")
    n_c, n_s = len(todos_con), len(todos_sin)
    print(f"n_con={n_c} n_sin={n_s}")
    if n_c >= N_MIN and n_s >= N_MIN:
        diff, p = shuffle_test(todos_con, todos_sin, seed_key="agregado_candidata3")
        print(f"CON confluencia: pnl_medio={np.mean(todos_con):+.3f}€")
        print(f"SIN confluencia: pnl_medio={np.mean(todos_sin):+.3f}€")
        print(f"diff={diff:+.3f}€ p_shuffle={p:.4f}")
    else:
        print("n insuficiente para el agregado.")


if __name__ == "__main__":
    main()
