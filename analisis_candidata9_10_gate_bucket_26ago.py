#!/usr/bin/env python3
"""analisis_candidata9_10_gate_bucket_26ago.py -- gate por micro-bucket
de precio (mismo rigor EXACTO que analisis_gate_bucket_propio_28jul.py:
shuffle vs resto de la misma tupla + bootstrap CI90% absoluto + split-half
cronológico + BH-FDR por (familia,activo), piso absoluto pnl_medio>=0
para "bueno_confirmado") aplicado a los dos hallazgos confirmados 26-Ago:

  - Candidata 9 "CANDIDATA9_BOT_CONSENSO": consenso mayoritario de las 84
    bot wallets por mercado, evento = trade EXACTO que hace cruzar a
    mayoría estricta (sin look-ahead, ver analisis_candidata9_v2_
    sinlookahead_26ago.py). Todas las (activo,marco) con datos.
  - Candidata 10 "CANDIDATA10_CROSSACTIVO": confirmación cruzada BTC
    (misma wallet, 2 activos, ventana 30min, solo confirmaciones PREVIAS
    -- ver analisis_candidata10_v2_sinlookahead_26ago.py). Solo BTC (único
    activo con n suficiente en el grupo "sin confirmar" para el contraste
    original).

pnl_neto con la fórmula exacta del proyecto: gross_win=(1-ask)/ask,
fee 7% -- import directo de kelly_precio_gate._familia() para agrupar
BH-FDR, e import directo de shuffle_test/bh_fdr_signif de
analisis_gate_bucket_propio_28jul.py (nunca duplicar la fórmula).

FASE 0 -- solo lectura. Escribe data/shadow/candidata9_10_gate_bucket.json.
NO conectado a ningún ejecutor real, estas tuplas no existen en
pares_permitidos_live ni candidatos_evaluacion_live -- exploratorio.
"""
import csv
import json
import math
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_bucket_propio_28jul import shuffle_test, bh_fdr_signif  # noqa: E402

IN_BOTS = REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv"
OUT = REPO / "data/shadow/candidata9_10_gate_bucket.json"

STEP = 0.05
N_MIN = 15
P_MAX = 0.05
FEE = 0.07
VENTANA_MIN_C10 = 30
N_MIN_BOTS_C9 = 3
# 31-Ago (/code-review sesión, pendiente #3 checkpoint 31-Ago): igual que
# analisis_bot_wallets_gate_bucket_25ago.py (mismo IN_BOTS) -- un ask
# capturado no implica profundidad real, mismo hueco ya corregido para
# Wallet Mirror el 10-Ago. Verificado con datos reales: Candidata9
# sobrevive limpio en sus 4 buckets confirmados (n_fillable>=15 en todos);
# Candidata10#BTC#60min[0.15,0.20) se queda sin evidencia suficiente
# (n_fillable=4<15, no concluyente -- no confirma ni refuta).
RATIO_MIN = 5.0


def bucket(p):
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def pnl_neto(ask, acierto):
    gross_win = (1 - ask) / ask
    return gross_win * (1 - FEE) if acierto else -1.0


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def to_float(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def eventos_candidata9():
    """tupla_str -> [(ts, ask, pnl), ...] para TODAS las (activo,marco)."""
    por_mercado = defaultdict(list)
    with open(IN_BOTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real"):
                continue
            por_mercado[r["condition_id"]].append(r)

    eventos = defaultdict(list)
    for cond, filas in por_mercado.items():
        if len(filas) < N_MIN_BOTS_C9:
            continue
        votos_final = defaultdict(int)
        for r in filas:
            votos_final[r["lado_wallet"]] += 1
        if len(votos_final) == 1:
            continue
        lado_mayoria = max(votos_final, key=votos_final.get)
        n_mayoria = votos_final[lado_mayoria]
        n_total = sum(votos_final.values())
        if n_mayoria == n_total - n_mayoria:
            continue
        activo = filas[0]["activo"]
        marco = filas[0]["marco"]
        outcome = filas[0]["outcome_real"]

        filas_ordenadas = sorted(filas, key=lambda r: parse_ts(r["trade_timestamp"]))
        cuenta = defaultdict(int)
        trigger = None
        for r in filas_ordenadas:
            cuenta[r["lado_wallet"]] += 1
            resto = sum(v for k, v in cuenta.items() if k != lado_mayoria)
            if cuenta[lado_mayoria] > resto and r["lado_wallet"] == lado_mayoria:
                trigger = r
                break
        if trigger is None:
            continue

        ask = to_float(trigger["mejor_ask_deteccion"])
        if ask is None or not (0.0 < ask < 1.0):
            continue
        ratio = to_float(trigger.get("ratio_vs_stake_deteccion", ""))
        if ratio is None or ratio < RATIO_MIN:
            continue
        acierto = 1 if lado_mayoria == outcome else 0
        pnl = pnl_neto(ask, acierto)
        ts = parse_ts(trigger["trade_timestamp"])
        tupla_str = f"CANDIDATA9_BOT_CONSENSO#{activo}#{marco}"
        eventos[tupla_str].append((ts, ask, pnl))
    return eventos


def eventos_candidata10():
    """tupla_str -> [(ts, ask, pnl), ...] solo BTC, grupo con_confirm."""
    filas = []
    with open(IN_BOTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real") or not r.get("acierto"):
                continue
            filas.append(r)

    por_wallet = defaultdict(list)
    for r in filas:
        por_wallet[r["wallet"]].append(r)

    eventos = defaultdict(list)
    for w, trs in por_wallet.items():
        if len({t["activo"] for t in trs}) < 2:
            continue
        trs_ts = sorted([(parse_ts(t["trade_timestamp"]), t) for t in trs], key=lambda x: x[0])
        for idx, (ts_i, ti) in enumerate(trs_ts):
            if ti["activo"] != "BTC":
                continue
            confirm = False
            for ts_j, tj in trs_ts[:idx]:
                if tj["activo"] == ti["activo"]:
                    continue
                if (ts_i - ts_j).total_seconds() <= VENTANA_MIN_C10 * 60 and tj["lado_wallet"] == ti["lado_wallet"]:
                    confirm = True
                    break
            if not confirm:
                continue
            ask = to_float(ti["mejor_ask_deteccion"])
            if ask is None or not (0.0 < ask < 1.0):
                continue
            ratio = to_float(ti.get("ratio_vs_stake_deteccion", ""))
            if ratio is None or ratio < RATIO_MIN:
                continue
            acierto = int(ti["acierto"])
            pnl = pnl_neto(ask, acierto)
            marco = ti["marco"]
            tupla_str = f"CANDIDATA10_CROSSACTIVO#BTC#{marco}"
            eventos[tupla_str].append((ts_i, ask, pnl))
    return eventos


def _familia(tupla_str):
    return tupla_str.split("#")[0]


def main():
    eventos = defaultdict(list)
    for tupla_str, evs in eventos_candidata9().items():
        eventos[tupla_str].extend(evs)
    for tupla_str, evs in eventos_candidata10().items():
        eventos[tupla_str].extend(evs)

    print(f"Tuplas (candidata9+10): {len(eventos)}")

    pendientes = []
    resultado = {}
    for tupla_str, filas in eventos.items():
        if len(filas) < N_MIN:
            resultado[tupla_str] = {}
            continue

        por_bucket = defaultdict(list)
        for ts, ask, pnl in filas:
            por_bucket[bucket(ask)].append((ts, pnl))

        tabla = {}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, pnl) for bb, fs in por_bucket.items() if bb != b for ts, pnl in fs]
            n_d = len(dentro)
            pnl_d = [pnl for _, pnl in dentro]
            pnl_f = [pnl for _, pnl in fuera]
            media_d = sum(pnl_d) / n_d

            entrada = {"n": n_d, "pnl_medio": round(media_d, 4),
                       "diff_vs_resto": round(media_d - (sum(pnl_f) / len(pnl_f)), 4) if pnl_f else None,
                       "shuffle_p": None, "split_half_diff": None,
                       "ci90_bootstrap_absoluto": None, "veredicto": "sin_concluir"}
            tabla[f"{b:.2f}"] = entrada

            if n_d >= N_MIN and pnl_f:
                diff, p_valor = shuffle_test(pnl_d, pnl_f)
                entrada["shuffle_p"] = round(p_valor, 4)
                pnl_d_arr = np.asarray(pnl_d, dtype=np.float64)
                rng = np.random.default_rng(abs(hash((tupla_str, b))) % (2**32))
                boots = pnl_d_arr[rng.integers(0, n_d, size=(2000, n_d))].mean(axis=1)
                boots.sort()
                ci_lo90 = float(boots[int(0.05 * len(boots))])
                ci_hi90 = float(boots[int(0.95 * len(boots))])
                entrada["ci90_bootstrap_absoluto"] = [round(ci_lo90, 4), round(ci_hi90, 4)]
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    d1 = sum(pnl for _, pnl in m1) / len(m1) - sum(pnl_f) / len(pnl_f)
                    d2 = sum(pnl for _, pnl in m2) / len(m2) - sum(pnl_f) / len(pnl_f)
                    entrada["split_half_diff"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"tupla_str": tupla_str, "bucket": f"{b:.2f}", "entrada": entrada,
                                            "p": p_valor, "diff": diff})
        resultado[tupla_str] = tabla

    por_familia_activo = defaultdict(list)
    for idx, p in enumerate(pendientes):
        partes = p["tupla_str"].split("#")
        activo = partes[1] if len(partes) > 1 else "?"
        clave = (_familia(p["tupla_str"]), activo)
        por_familia_activo[clave].append(idx)

    sobreviven = set()
    for (familia, activo), indices in por_familia_activo.items():
        p_valores_grupo = [pendientes[i]["p"] for i in indices]
        sobreviven_grupo = bh_fdr_signif(p_valores_grupo, q=P_MAX)
        sobreviven |= {indices[j] for j in sobreviven_grupo}
        print(f"  familia={familia} activo={activo}: {len(indices)} tests candidatos, "
              f"{len(sobreviven_grupo)} sobreviven BH-FDR q={P_MAX}")

    print(f"\nTests candidatos: {len(pendientes)} | sobreviven BH-FDR: {len(sobreviven)}")

    veredictos_nuevos = []
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        ci = p["entrada"]["ci90_bootstrap_absoluto"]
        if p["diff"] < 0:
            veredicto = "malo_confirmado"
        elif p["entrada"]["pnl_medio"] >= 0 and ci is not None and ci[0] > 0:
            veredicto = "bueno_confirmado"
        else:
            continue
        resultado[p["tupla_str"]][p["bucket"]]["veredicto"] = veredicto
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        b = p["bucket"]
        veredictos_nuevos.append(
            f"{marca} {p['tupla_str']} [{b},{float(b)+STEP:.2f}) n={p['entrada']['n']} "
            f"pnl_medio={p['entrada']['pnl_medio']:+.3f} p={p['p']:.4f} {veredicto}"
        )

    print(f"\n{len(veredictos_nuevos)} bucket(s) con veredicto tras BH-FDR:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")

    OUT.write_text(json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nEscrito {OUT}")


if __name__ == "__main__":
    main()
