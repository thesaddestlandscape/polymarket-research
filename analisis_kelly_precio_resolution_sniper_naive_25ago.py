#!/usr/bin/env python3
"""analisis_kelly_precio_resolution_sniper_naive_25ago.py — gate de
corrección de Kelly por precio de entrada para RESOLUTION_SNIPER_NAIVE
(25-Ago, petición explícita Javi: "constrúyelo pero solo para los
micro-buckets y micro-buckets finos que tienen edge y pnl positivo
confirmado").

Origen: `kelly_precio_gate.py`/`analisis_kelly_precio_gate_29jul.py`
(mismo mecanismo, mismas fórmulas f_actual/f_exacto/ratio_correccion) NO
cubre RESOLUTION_SNIPER_NAIVE porque esa tupla no pasa por results.csv
(pipeline propio vía resolution_sniper_observer.py, no shadow_predict.py)
-- mismo motivo por el que WALLET_MIRROR necesita su propio join en otros
sitios del proyecto. Este script es el generador análogo, sobre la fuente
correcta (`resolution_sniper_obs_YYYY-MM-DD.csv`, ask real vía ask_yes/
ask_no + outcome_real ya resuelto).

Evaluación previa (25-Ago, misma sesión) que motivó construirlo: cruzando
11.673 observaciones post-TWAP (marco 5min, offset 0-3s, las mismas
condiciones del gate riguroso de 19-Ago) apareció un patrón MONOTÓNICO
claro -- pnl/trade cae de +0.68€ en ask~0.50 a -0.065€ en ask~0.90, pese
a que `resolution_sniper_naive_gate_bucket.py` hoy sella TODO [0.05,0.95)
como "bueno_confirmado" en bloque para las 6 monedas. Exactamente el tipo
de hueco que kelly_precio_gate.py ya corrige en las otras 4 familias.

Dos granularidades, igual que pidió Javi:
1. Bucket fijo (paso 0.10, misma fórmula EXACTA que analisis_kelly_
   precio_gate_29jul.py, reimportada de ahí para no duplicar) --
   desagregado por ACTIVO (nunca las 6 monedas juntas, CLAUDE.md pt.17).
2. Ventana deslizante fina (paso 0.01, ancho 0.05, max-statistic,
   reimportada de analisis_gate_bucket_fino.py) -- por si el edge real es
   más estrecho que el grid de 0.10 y el bucket fijo lo diluye.

**Filtro explícito de Javi**: SOLO se escriben en el JSON de salida las
entradas con veredicto="confirmado" Y pnl_medio>0 -- un bucket/ventana
negativo o sin_concluir no se guarda (esa parte ya la cubre el veto
binario de resolution_sniper_naive_gate_bucket.py, este mecanismo es
puramente de SIZING sobre lo que YA se va a operar, nunca de veto).

Solo lectura de resolution_sniper_obs_*.csv. Escribe
data/shadow/kelly_precio_resolution_sniper_naive.json -- NO toca
kelly_precio_gate.json (ese lo regenera un cron distinto que lo
sobreescribiría por completo cada día, perdiendo esta familia). Consumido
por kelly_precio_gate.py::evaluar() como fuente ADICIONAL (mismo patrón
aditivo que zonas_validadas_externas.json en gate_bucket_propio.py).
"""
import csv
import glob
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

from analisis_kelly_precio_gate_29jul import bucket, shuffle_test, bh_fdr_signif, wilson_ci
from analisis_gate_bucket_fino import evaluar_tupla

REPO = Path(__file__).resolve().parent
OUT = REPO / "data/shadow/kelly_precio_resolution_sniper_naive.json"

FEE = 0.07
STEP = 0.10
N_MIN = 15
P_MAX = 0.05
MARCO = "5min"
OFFSETS_VALIDOS = {0, 1, 2, 3}
TWAP_FECHA_CAMBIO = "2026-08-07"  # mismo corte que shadow_postmortem.TWAP_FECHA_CAMBIO


def cargar_filas() -> dict:
    """activo -> [(ts, ask, pnl), ...], filtrado a marco=5min, offset 0-3s,
    post-TWAP, ask real de la dirección implícita, outcome ya resuelto."""
    por_activo = defaultdict(list)
    for path in sorted(glob.glob(str(REPO / "data/shadow/resolution_sniper_obs_*.csv"))):
        fecha = Path(path).stem.rsplit("_", 1)[-1]
        if fecha < TWAP_FECHA_CAMBIO:
            continue
        with open(path, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if r.get("marco") != MARCO:
                    continue
                try:
                    offset = int(r.get("offset_s", ""))
                except (TypeError, ValueError):
                    continue
                if offset not in OFFSETS_VALIDOS:
                    continue
                dir_impl = r.get("chainlink_direccion_implicita", "")
                if dir_impl not in ("Up", "Down"):
                    continue
                ask_raw = r.get("ask_yes") if dir_impl == "Up" else r.get("ask_no")
                try:
                    ask = float(ask_raw)
                except (TypeError, ValueError):
                    continue
                if not (0.0 < ask < 1.0):
                    continue
                outcome = r.get("outcome_real", "")
                if outcome not in ("Up", "Down"):
                    continue
                acierto = 1 if outcome == dir_impl else 0
                gross_win = (1 - ask) / ask
                pnl = gross_win * (1 - FEE) if acierto else -1.0
                ts = r.get("timestamp_utc", "")
                por_activo[r["activo"]].append((ts, ask, pnl, acierto))
    return por_activo


def gate_fijo(por_activo: dict) -> dict:
    """Mismas fórmulas EXACTAS que analisis_kelly_precio_gate_29jul.py."""
    resultado = {}
    pendientes = []
    for activo, filas4 in por_activo.items():
        subtype = f"{activo}#{MARCO}"
        por_bucket = defaultdict(list)
        for ts, ask, pnl, ac in filas4:
            por_bucket[bucket(ask)].append((ts, ask, pnl, ac))

        tabla = {}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, ask, pnl, ac) for bb, fs in por_bucket.items() if bb != b for ts, ask, pnl, ac in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, _, pnl, _ in dentro]
            pnl_f = [pnl for _, _, pnl, _ in fuera]
            wins = sum(ac for _, _, _, ac in dentro)
            p_hat = wins / n_d if n_d else 0.0
            pi_medio = sum(ask for _, ask, _, _ in dentro) / n_d if n_d else 0.0
            ic_bayes = (wins + 1) / (n_d + 2) - 0.5
            f_actual = abs(ic_bayes) * 0.5
            f_exacto = max(0.0, (p_hat - pi_medio) / (1 - pi_medio)) * 0.5
            ratio = (f_exacto / f_actual) if f_actual > 1e-9 else None
            wilson_lo, wilson_hi = wilson_ci(wins, n_d) if n_d else (0.0, 0.0)

            entrada = {
                "n": n_d, "hit": round(p_hat, 4), "pi_medio": round(pi_medio, 4),
                "pnl_medio": round(sum(pnl_d) / n_d, 4) if n_d else None,
                "f_actual": round(f_actual, 5), "f_exacto": round(f_exacto, 5),
                "ratio_correccion": round(ratio, 3) if ratio is not None else None,
                "wilson90": [round(wilson_lo, 3), round(wilson_hi, 3)],
                "shuffle_p": None, "split_half_diff": None, "veredicto": "sin_concluir",
            }
            if n_d >= N_MIN and pnl_f:
                diff, p_valor = shuffle_test(pnl_d, pnl_f)
                entrada["shuffle_p"] = round(p_valor, 4)
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    media_fuera = sum(pnl_f) / len(pnl_f)
                    d1 = sum(pnl for _, _, pnl, _ in m1) / len(m1) - media_fuera
                    d2 = sum(pnl for _, _, pnl, _ in m2) / len(m2) - media_fuera
                    entrada["split_half_diff"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"activo": activo, "subtype": subtype, "bucket": f"{b:.2f}",
                                            "entrada": entrada, "p": p_valor})
            # filtro explícito de Javi: solo confirmado Y pnl positivo se guarda
            tabla[f"{b:.2f}"] = entrada
        resultado[subtype] = tabla

    p_valores = [p["p"] for p in pendientes]
    sobreviven = bh_fdr_signif(p_valores, q=P_MAX)
    for idx, p in enumerate(pendientes):
        if idx in sobreviven:
            p["entrada"]["veredicto"] = "confirmado"

    # filtro final: solo confirmado Y pnl_medio>0 sobrevive en la salida
    salida = {}
    for subtype, tabla in resultado.items():
        tabla_filtrada = {b: e for b, e in tabla.items()
                           if e["veredicto"] == "confirmado" and (e["pnl_medio"] or 0) > 0}
        if tabla_filtrada:
            salida[subtype] = tabla_filtrada
    return salida


def gate_fino(por_activo: dict) -> dict:
    """Ventana deslizante fina (paso 0.01, ancho 0.05) vía evaluar_tupla()
    de analisis_gate_bucket_fino.py -- solo se guardan ventanas con
    p_valor<0.05, split_half_ok, robusto_loo, robusto_bootstrap Y
    pnl_medio>0 (mismo filtro explícito de Javi). evaluar_tupla() no
    calcula ratio_correccion (no es su trabajo, gate_bucket_fino.py solo
    detecta la ventana ganadora) -- se recalcula aquí con la MISMA fórmula
    f_actual/f_exacto que el resto del gate, restringida a las filas
    DENTRO de la ventana devuelta."""
    salida = {}
    for activo, filas4 in por_activo.items():
        subtype = f"{activo}#{MARCO}"
        filas3 = [(ts, ask, pnl) for ts, ask, pnl, _ in filas4]
        r = evaluar_tupla(filas3)
        if not r:
            continue
        if not (r["p_valor"] < 0.05 and r["split_half_ok"] and r["robusto_loo"]
                and r["robusto_bootstrap"] and r["pnl_medio"] > 0):
            continue
        dentro = [(ask, ac) for _, ask, _, ac in filas4 if r["lo"] <= ask < r["hi"]]
        n_d = len(dentro)
        if n_d == 0:
            continue
        wins = sum(ac for _, ac in dentro)
        p_hat = wins / n_d
        pi_medio = sum(ask for ask, _ in dentro) / n_d
        ic_bayes = (wins + 1) / (n_d + 2) - 0.5
        f_actual = abs(ic_bayes) * 0.5
        f_exacto = max(0.0, (p_hat - pi_medio) / (1 - pi_medio)) * 0.5
        ratio = round(f_exacto / f_actual, 3) if f_actual > 1e-9 else None
        r["hit"] = round(p_hat, 4)
        r["pi_medio"] = round(pi_medio, 4)
        r["ratio_correccion"] = ratio
        salida[subtype] = [r]
    return salida


def main() -> int:
    por_activo = cargar_filas()
    print(f"Activos con datos: {list(por_activo.keys())}")
    for a, filas in por_activo.items():
        print(f"  {a}: n={len(filas)}")

    fijo = gate_fijo(por_activo)
    fino = gate_fino(por_activo)

    print("\n--- Bucket fijo, confirmado Y positivo ---")
    for subtype, tabla in fijo.items():
        for b, e in tabla.items():
            print(f"  {subtype} [{b},{float(b)+STEP:.2f}) n={e['n']} pnl={e['pnl_medio']:+.3f} "
                  f"ratio_correccion={e['ratio_correccion']}")

    print("\n--- Ventana fina, confirmada Y positiva ---")
    for subtype, ventanas in fino.items():
        for v in ventanas:
            print(f"  {subtype} [{v['lo']:.2f},{v['hi']:.2f}) n={v['n']} pnl={v['pnl_medio']:+.3f} "
                  f"p={v['p_valor']:.4f}")

    payload = {
        "generado_utc": datetime.now(timezone.utc).isoformat(),
        "step": STEP,
        "n_min": N_MIN,
        "p_max": P_MAX,
        "nota": "Solo entradas confirmado+pnl_medio>0 (filtro explicito Javi 25-Ago)",
        "familias": {"RESOLUTION_SNIPER_NAIVE": fijo},
        "ventanas_finas": {"RESOLUTION_SNIPER_NAIVE": fino},
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"\nEscrito {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
