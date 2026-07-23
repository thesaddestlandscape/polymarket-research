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

20-Jul (extensión, petición Javi): añadido desglose por MARCO por separado
(data/shadow/wallet_edge_score_por_marco.json) -- "smart en general" puede
ser plana o mala en un marco concreto y buena en otro (ya visto: una wallet
va muy bien en BTC#15min y muy mal en SOL#5min a la vez). Cada marco lleva
su propia corrección BH-FDR (multiplicidad separada, no mezclada -- mismo
criterio que feedback_desagregar_por_activo_siempre) en vez de una sola
corrección global que diluiría marcos con pocos candidatos. Incluye
pnl_proxy (EUR de payoff por cada 1 EUR apostado, sumado sobre los n
trades -- normalizado a stake unitario porque el CSV no registra tamaño
real; sirve para rankear "cuánta pasta genera" sin necesitar tamaño real)
usando la misma fórmula que _stats_banda() en ballenas_observer.py.

23-Jul (extensión, petición Javi -- hueco encontrado en la sesión de
franja milimétrica de ballenas_executor_5min): el desglose por marco de
arriba MEZCLA las 5 monedas dentro de, p.ej., "5m" -- una wallet activa en
BTC+ETH+XRP#5min sale con un edge_pp que es una mezcla de las 3, no
atribuible a ninguna en concreto. Se añade un TERCER desglose
(wallet, activo, marco), con su propia corrección BH-FDR por (activo,marco)
-- mismo principio de multiplicidad separada que ya se aplicaba por marco,
ahora también por activo. Motivado por un hallazgo concreto: la wallet
0x32d5d0c7... aparece con n=73 hit=82.2% edge_pp=+34.96 SOLO en XRP#5min
(precio medio 0.46, zona temprana) -- validado con shuffle test propio,
p=0.0000 -- que el desglose por-marco solo (sin activo) no podía aislar.

Output: data/shadow/wallet_edge_score.json (agregado, todos los marcos)
  {wallet_lower: {n, hit, precio_medio, edge_pp, pnl_proxy, p_shuffle,
                   sig_bhfdr, actualizado}}
Output: data/shadow/wallet_edge_score_por_marco.json (desagregado por marco)
  {"wallet_lower#marco": {..mismas columnas.., marco, wallet}}
Output: data/shadow/wallet_edge_score_por_activo_marco.json (desagregado
  por activo+marco, 23-Jul)
  {"wallet_lower#activo#marco": {..mismas columnas.., activo, marco, wallet}}
"""
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from shadow_postmortem import _benjamini_hochberg  # reutiliza el método ya

DIR_SHADOW = Path(__file__).parent / "data/shadow"
HIST = DIR_SHADOW / "ballenas_timing_history.csv"
OUT = DIR_SHADOW / "wallet_edge_score.json"
OUT_POR_MARCO = DIR_SHADOW / "wallet_edge_score_por_marco.json"
OUT_POR_ACTIVO_MARCO = DIR_SHADOW / "wallet_edge_score_por_activo_marco.json"

N_MIN = 15          # mismo suelo de rigor que el resto del proyecto
N_SHUFFLE = 2000
FDR = 0.10           # mismo FDR que shadow_postmortem/analisis_shuffle_patrones_causales


def _stat_vacia():
    return {"n": 0, "aciertos": 0, "suma_precio": 0.0, "pnl_proxy": 0.0}


def _acumular(d, precio, acierto):
    d["n"] += 1
    d["aciertos"] += acierto
    d["suma_precio"] += precio
    d["pnl_proxy"] += (1.0 - precio) if acierto else -precio


def _cargar_por_wallet_y_marco():
    """Un solo paso por el CSV: acumula agregado (todos los marcos), por
    (wallet, marco) y por (wallet, activo, marco) a la vez -- no relee el
    fichero tres veces."""
    por_wallet = defaultdict(_stat_vacia)
    por_wallet_marco = defaultdict(_stat_vacia)
    por_wallet_activo_marco = defaultdict(_stat_vacia)
    with open(HIST, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                w = r["wallet"].lower()
                marco = r["marco"]
                activo = r["activo"]
                precio = float(r["precio"])
                acierto = int(r["acierto"])
            except (ValueError, TypeError, KeyError, AttributeError):
                continue
            if not (0.0 < precio < 1.0):
                continue  # precio_medio=0 o 1 rompe el shuffle (p fijo degenerado)
            _acumular(por_wallet[w], precio, acierto)
            _acumular(por_wallet_marco[(w, marco)], precio, acierto)
            _acumular(por_wallet_activo_marco[(w, activo, marco)], precio, acierto)
    return por_wallet, por_wallet_marco, por_wallet_activo_marco


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


def _filas_con_significancia(grupos, ahora, etiqueta):
    """grupos: {clave: stat_dict} -- calcula edge/p_shuffle y aplica BH-FDR
    SOLO dentro de este grupo de tests (el llamador decide el alcance de la
    multiplicidad: todo el lote para el agregado, por-marco para el
    desglose)."""
    candidatas = {k: d for k, d in grupos.items() if d["n"] >= N_MIN}
    filas = []
    for k, d in candidatas.items():
        n = d["n"]
        hit = d["aciertos"] / n
        precio_medio = d["suma_precio"] / n
        seed = (hash(k) ^ n) & 0xFFFFFFFF
        p = _shuffle_pvalue_edge(n, precio_medio, hit, seed)
        filas.append({"clave": k, "n": n, "hit": round(hit, 4),
                       "precio_medio": round(precio_medio, 4),
                       "edge_pp": round((hit - precio_medio) * 100, 3),
                       "pnl_proxy": round(d["pnl_proxy"], 3),
                       "p_shuffle": p})
    pvals = [f["p_shuffle"] for f in filas]
    keep = _benjamini_hochberg(pvals, fdr=FDR)
    n_sig = 0
    for f, sig in zip(filas, keep):
        f["sig_bhfdr"] = bool(sig)
        f["actualizado"] = ahora.isoformat(timespec="seconds")
        n_sig += int(sig)
    print(f"  [{etiqueta}] n>={N_MIN}: {len(candidatas)} candidatas, "
          f"significativas tras BH-FDR({FDR}): {n_sig}")
    return filas


def main():
    ahora = datetime.now(timezone.utc)
    print(f"[wallet_edge_tracker] {ahora.isoformat(timespec='seconds')}")
    por_wallet, por_wallet_marco, por_wallet_activo_marco = _cargar_por_wallet_y_marco()
    print(f"  wallets distintas en histórico: {len(por_wallet)}")

    filas_agg = _filas_con_significancia(por_wallet, ahora, "agregado")
    salida_agg = {f["clave"]: {k: v for k, v in f.items() if k != "clave"} for f in filas_agg}
    OUT.write_text(json.dumps(salida_agg, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  escrito {OUT} ({len(salida_agg)} wallets)")

    # por marco: multiplicidad separada por marco (no mezclar 5m con 60m)
    por_marco_agrupado = defaultdict(dict)
    for (w, marco), d in por_wallet_marco.items():
        por_marco_agrupado[marco][(w, marco)] = d
    salida_marco = {}
    for marco, grupo in por_marco_agrupado.items():
        filas_m = _filas_con_significancia(grupo, ahora, f"marco={marco}")
        for f in filas_m:
            w, marco_k = f["clave"]
            clave_out = f"{w}#{marco_k}"
            salida_marco[clave_out] = {"wallet": w, "marco": marco_k,
                                        **{k: v for k, v in f.items() if k != "clave"}}
    OUT_POR_MARCO.write_text(json.dumps(salida_marco, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  escrito {OUT_POR_MARCO} ({len(salida_marco)} filas wallet#marco)")

    # por activo+marco (23-Jul): multiplicidad separada por (activo,marco) --
    # no mezclar XRP#5m con ETH#5m, mismo principio que separar marcos entre sí.
    por_activo_marco_agrupado = defaultdict(dict)
    for (w, activo, marco), d in por_wallet_activo_marco.items():
        por_activo_marco_agrupado[(activo, marco)][(w, activo, marco)] = d
    salida_activo_marco = {}
    for (activo, marco), grupo in por_activo_marco_agrupado.items():
        filas_am = _filas_con_significancia(grupo, ahora, f"activo={activo} marco={marco}")
        for f in filas_am:
            w, activo_k, marco_k = f["clave"]
            clave_out = f"{w}#{activo_k}#{marco_k}"
            salida_activo_marco[clave_out] = {"wallet": w, "activo": activo_k, "marco": marco_k,
                                               **{k: v for k, v in f.items() if k != "clave"}}
    OUT_POR_ACTIVO_MARCO.write_text(json.dumps(salida_activo_marco, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  escrito {OUT_POR_ACTIVO_MARCO} ({len(salida_activo_marco)} filas wallet#activo#marco)")


if __name__ == "__main__":
    main()
