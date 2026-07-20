#!/usr/bin/env python3
"""
wallet_edge_tracker.py — puntúa cada wallet vista en ballenas_timing_history.csv
por su edge REAL (hit-rate propio menos el precio al que compra), no por su
PnL de leaderboard.

Origen (20-Jul): cruzando las 66 wallets "smart" (smart_money_wallets.json,
verificadas por PnL oficial del leaderboard) contra ballenas_timing_history.csv
(330k trades reales con resultado) se encontró que la mayoría de ellas
(30/38 con n>=15 en ese momento) NO tienen ningún edge demostrable en los
mercados Up/Down 5-15min específicamente -- su rentabilidad de leaderboard
viene de otro sitio (otros tipos de mercado, timing de redención, tamaño).
Peor: al menos una wallet con n=10023 (la muestra más grande de toda la
cohorte) tiene edge NEGATIVO significativo y estable en el tiempo,
concentrado en SOL/ETH#15min -- justo el hueco donde vive
BALLENAS_CONFIRMADAS_15M. "Smart" (PnL leaderboard) != "informativo para
nuestra señal direccional". Ver memoria de esta sesión (20-Jul) para el
detalle completo del hallazgo.

Este script generaliza ese cruce a TODAS las wallets del histórico (no solo
las 66 "smart"), con n>=15 (suelo de rigor del proyecto) y significancia
vía shuffle test (Binomial(n, p=precio_medio), no z-approx -- mismo estándar
que el resto del proyecto, feedback_shuffle_antes_de_bloquear) + BH-FDR
sobre TODO el lote testeado cada ciclo (reutiliza _benjamini_hochberg de
shadow_postmortem.py, no reinventa el método).

Puramente shadow/observacional: no ejecuta nada, no toca dinero. Pensado
para alimentar shadow_predict.py como feature adicional en
s_ballenas_confirmadas_15m (peso por wallet en vez de conteo plano),
SIN tocar prob_yes -- ese cableado es un paso aparte, deliberadamente
separado de este script.

Output: data/shadow/wallet_edge_score.json
  {wallet_lower: {n, hit, precio_medio, edge_pp, p_shuffle, sig_bhfdr,
                   actualizado}}
"""
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from shadow_postmortem import _benjamini_hochberg  # reutiliza el método ya

DIR_SHADOW = Path("data/shadow")
HIST = DIR_SHADOW / "ballenas_timing_history.csv"
OUT = DIR_SHADOW / "wallet_edge_score.json"

N_MIN = 15          # mismo suelo de rigor que el resto del proyecto
N_SHUFFLE = 2000
FDR = 0.10           # mismo FDR que shadow_postmortem/analisis_shuffle_patrones_causales


def _cargar_por_wallet():
    por_wallet = {}
    with open(HIST, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            w = r["wallet"].lower()
            try:
                precio = float(r["precio"])
                acierto = int(r["acierto"])
            except (ValueError, TypeError, KeyError):
                continue
            if not (0.0 < precio < 1.0):
                continue  # precio_medio=0 o 1 rompe el shuffle (p fijo degenerado)
            d = por_wallet.setdefault(w, {"n": 0, "aciertos": 0, "suma_precio": 0.0})
            d["n"] += 1
            d["aciertos"] += acierto
            d["suma_precio"] += precio
    return por_wallet


def _shuffle_pvalue_edge(n: int, precio_medio: float, hit_real: float, seed: int,
                          n_shuffle: int = N_SHUFFLE) -> float:
    """Shuffle test de dos colas: ¿el hit-rate observado es sorprendente
    comparado con Binomial(n, p=precio_medio) -- el nulo de 'compra al
    precio de mercado, sin edge propio'? Semilla determinista (misma wallet
    -> mismo resultado siempre, mismo criterio que _simular_null_binomial
    en shadow_postmortem.py) en vez de random sin semilla."""
    rng = np.random.default_rng(seed=seed)
    aciertos_sim = rng.binomial(n, precio_medio, size=n_shuffle)
    hit_sim = aciertos_sim / n
    dist_real = abs(hit_real - precio_medio)
    dist_sim = np.abs(hit_sim - precio_medio)
    return float(np.mean(dist_sim >= dist_real))


def main():
    ahora = datetime.now(timezone.utc)
    print(f"[wallet_edge_tracker] {ahora.isoformat(timespec='seconds')}")
    por_wallet = _cargar_por_wallet()
    print(f"  wallets distintas en histórico: {len(por_wallet)}")

    candidatas = {w: d for w, d in por_wallet.items() if d["n"] >= N_MIN}
    print(f"  con n>={N_MIN}: {len(candidatas)}")

    filas = []
    for w, d in candidatas.items():
        n = d["n"]
        hit = d["aciertos"] / n
        precio_medio = d["suma_precio"] / n
        seed = (hash(w) ^ n) & 0xFFFFFFFF
        p = _shuffle_pvalue_edge(n, precio_medio, hit, seed)
        filas.append({"wallet": w, "n": n, "hit": round(hit, 4),
                       "precio_medio": round(precio_medio, 4),
                       "edge_pp": round((hit - precio_medio) * 100, 3),
                       "p_shuffle": p})

    pvals = [f["p_shuffle"] for f in filas]
    keep = _benjamini_hochberg(pvals, fdr=FDR)
    n_sig = 0
    for f, sig in zip(filas, keep):
        f["sig_bhfdr"] = bool(sig)
        f["actualizado"] = ahora.isoformat(timespec="seconds")
        n_sig += int(sig)
    print(f"  significativas tras BH-FDR({FDR}) sobre {len(filas)} tests: {n_sig}")

    salida = {f["wallet"]: {k: v for k, v in f.items() if k != "wallet"} for f in filas}
    OUT.write_text(json.dumps(salida, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  escrito {OUT} ({len(salida)} wallets)")


if __name__ == "__main__":
    main()
