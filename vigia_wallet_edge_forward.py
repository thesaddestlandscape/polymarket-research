#!/usr/bin/env python3
"""
vigia_wallet_edge_forward.py -- valida FUERA DE MUESTRA el edge de las
wallets que wallet_edge_tracker.py marca como significativas.

Motivo (20-Jul): wallet_edge_tracker.py recalcula sobre TODO el histórico
cada hora -- una wallet "significativa" hoy lo es sobre datos que ya
existían cuando se detectó, no es una confirmación forward real (mismo
principio que el resto del proyecto: H-CUSTOM-BUYYES15-SOLO-TARDIO no se
dio por buena hasta confirmar forward, feedback_shuffle_antes_de_bloquear).
Este vigía congela cada wallet#marco significativa la primera vez que la
ve, y a partir de ahí mide su hit-rate SOLO sobre trades posteriores al
congelado -- la única prueba honesta de que el edge no es sobreajuste a
un puñado de mercados ya vistos.

No ejecuta nada, no toca dinero, no cablea ninguna decisión -- puramente
observacional. Pensado para correr por cron cada hora, 10min después de
wallet_edge_tracker.py (que corre a :25), para leer su snapshot ya fresco.

Estado: data/shadow/wallet_edge_forward_state.json
  {"wallet#marco": {wallet, marco, freeze_ts, n_frozen, hit_frozen,
                     precio_medio_frozen, edge_pp_frozen, pnl_proxy_frozen,
                     forward_n, forward_hit, forward_precio_medio,
                     forward_edge_pp, forward_pnl_proxy, forward_p_shuffle,
                     forward_sig_bhfdr, estado, ultimo_chequeo}}
estado en {ACUMULANDO, CONFIRMADO, NO_CONFIRMADO, INVERTIDO}
"""
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from shadow_postmortem import _benjamini_hochberg

DIR_SHADOW = Path("data/shadow")
HIST = DIR_SHADOW / "ballenas_timing_history.csv"
SCORE_POR_MARCO = DIR_SHADOW / "wallet_edge_score_por_marco.json"
STATE = DIR_SHADOW / "wallet_edge_forward_state.json"

N_MIN_FORWARD = 15   # mismo suelo de rigor que el resto del proyecto
N_SHUFFLE = 2000
FDR = 0.10


def _cargar_estado():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return {}


def _congelar_nuevas(estado, ahora):
    if not SCORE_POR_MARCO.exists():
        print("  [vigia_wallet_edge_forward] falta wallet_edge_score_por_marco.json -- nada que congelar")
        return 0
    score = json.loads(SCORE_POR_MARCO.read_text(encoding="utf-8"))
    nuevas = 0
    for clave, v in score.items():
        if not v.get("sig_bhfdr") or v.get("n", 0) < 15:
            continue
        if clave in estado:
            continue
        estado[clave] = {
            "wallet": v["wallet"], "marco": v["marco"],
            "freeze_ts": ahora.isoformat(timespec="seconds"),
            "n_frozen": v["n"], "hit_frozen": v["hit"],
            "precio_medio_frozen": v["precio_medio"],
            "edge_pp_frozen": v["edge_pp"], "pnl_proxy_frozen": v["pnl_proxy"],
            "forward_n": 0, "forward_aciertos": 0, "forward_suma_precio": 0.0,
            "forward_pnl_proxy": 0.0, "forward_hit": None,
            "forward_precio_medio": None, "forward_edge_pp": None,
            "forward_p_shuffle": None, "forward_sig_bhfdr": None,
            "estado": "ACUMULANDO", "ultimo_chequeo": ahora.isoformat(timespec="seconds"),
        }
        nuevas += 1
    return nuevas


def _acumular_forward(estado):
    """Un paso por el CSV: para cada fila cuyo (wallet, marco) esté en el
    roster congelado Y ts_trade > freeze_ts de esa wallet, acumula."""
    freeze_lookup = {}
    for clave, v in estado.items():
        freeze_lookup[(v["wallet"], v["marco"])] = v["freeze_ts"]

    acumulado = defaultdict(lambda: {"n": 0, "aciertos": 0, "suma_precio": 0.0, "pnl_proxy": 0.0})
    with open(HIST, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            try:
                w = r["wallet"].lower()
                marco = r["marco"]
                key = (w, marco)
                if key not in freeze_lookup:
                    continue
                if r["ts_trade"] <= freeze_lookup[key]:
                    continue
                precio = float(r["precio"])
                acierto = int(r["acierto"])
            except (ValueError, TypeError, KeyError, AttributeError):
                continue
            if not (0.0 < precio < 1.0):
                continue
            a = acumulado[key]
            a["n"] += 1
            a["aciertos"] += acierto
            a["suma_precio"] += precio
            a["pnl_proxy"] += (1.0 - precio) if acierto else -precio

    for clave, v in estado.items():
        key = (v["wallet"], v["marco"])
        a = acumulado.get(key)
        if a is None:
            continue
        v["forward_n"] = a["n"]
        v["forward_aciertos"] = a["aciertos"]
        v["forward_suma_precio"] = round(a["suma_precio"], 4)
        v["forward_pnl_proxy"] = round(a["pnl_proxy"], 3)
        if a["n"] > 0:
            v["forward_hit"] = round(a["aciertos"] / a["n"], 4)
            v["forward_precio_medio"] = round(a["suma_precio"] / a["n"], 4)
            v["forward_edge_pp"] = round((v["forward_hit"] - v["forward_precio_medio"]) * 100, 3)


def _shuffle_pvalue(n, precio_medio, hit_real, seed):
    rng = np.random.default_rng(seed=seed)
    aciertos_sim = rng.binomial(n, precio_medio, size=N_SHUFFLE)
    hit_sim = aciertos_sim / n
    dist_real = abs(hit_real - precio_medio)
    dist_sim = np.abs(hit_sim - precio_medio)
    return float(np.mean(dist_sim >= dist_real))


def _evaluar_significancia_forward(estado, ahora):
    elegibles = [k for k, v in estado.items() if v["forward_n"] >= N_MIN_FORWARD]
    pvals = []
    for k in elegibles:
        v = estado[k]
        seed = (hash(k) ^ v["forward_n"]) & 0xFFFFFFFF
        p = _shuffle_pvalue(v["forward_n"], v["forward_precio_medio"], v["forward_hit"], seed)
        v["forward_p_shuffle"] = p
        pvals.append(p)
    keep = _benjamini_hochberg(pvals, fdr=FDR) if pvals else []
    for k, sig in zip(elegibles, keep):
        estado[k]["forward_sig_bhfdr"] = bool(sig)

    for k, v in estado.items():
        v["ultimo_chequeo"] = ahora.isoformat(timespec="seconds")
        if v["forward_n"] < N_MIN_FORWARD:
            v["estado"] = "ACUMULANDO"
            continue
        mismo_signo = (v["forward_edge_pp"] >= 0) == (v["edge_pp_frozen"] >= 0)
        if v["forward_sig_bhfdr"] and mismo_signo:
            v["estado"] = "CONFIRMADO"
        elif v["forward_sig_bhfdr"] and not mismo_signo:
            v["estado"] = "INVERTIDO"
        else:
            v["estado"] = "NO_CONFIRMADO"


def main():
    ahora = datetime.now(timezone.utc)
    print(f"[vigia_wallet_edge_forward] {ahora.isoformat(timespec='seconds')}")
    estado = _cargar_estado()
    nuevas = _congelar_nuevas(estado, ahora)
    print(f"  roster: {len(estado)} wallet#marco ({nuevas} nuevas congeladas este ciclo)")
    _acumular_forward(estado)
    _evaluar_significancia_forward(estado, ahora)

    por_estado = defaultdict(int)
    for v in estado.values():
        por_estado[v["estado"]] += 1
    print(f"  estados: {dict(por_estado)}")

    for k, v in sorted(estado.items(), key=lambda kv: kv[1]["ultimo_chequeo"]):
        if v["estado"] in ("CONFIRMADO", "INVERTIDO"):
            print(f"  *** {k}: {v['estado']} -- forward n={v['forward_n']} hit={v['forward_hit']} "
                  f"edge_pp={v['forward_edge_pp']:+.2f} (congelado en {v['edge_pp_frozen']:+.2f}) "
                  f"p_shuffle={v['forward_p_shuffle']:.4f} ***")

    STATE.write_text(json.dumps(estado, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"  escrito {STATE}")


if __name__ == "__main__":
    main()
