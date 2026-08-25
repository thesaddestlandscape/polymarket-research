#!/usr/bin/env python3
"""analisis_candidata10b_crossactivo_baseline_propio_25ago.py -- rediseño
de la Candidata 10 tras el sesgo de selección encontrado en la 1ª pasada
(analisis_candidata10_crossactivo_bots_25ago.py, 25-Ago): comparar
"con_confirm" vs "sin_confirm" como grupos independientes es incorrecto
porque "sin_confirm" es un control raro y no representativo (con
ventana +-30min, la mayoría de bots casi siempre tienen otro trade
cerca -- el grupo pequeño resultante está sesgado, no es un control
limpio).

Petición explícita Javi 25-Ago ("hazlo con lo que tienes para ver si es
por ahí el camino"): en vez de comparar dos grupos de BOTS distintos,
compara cada trade "confirmado cruzado" contra el BASELINE PROPIO de esa
misma wallet (su hit-rate en TODOS sus trades resueltos) -- así cada bot
actúa como su propio control, y la heterogeneidad de habilidad entre
bots (la causa real del artefacto anterior) queda neutralizada.

Significancia: permutación EN BLOQUE por wallet -- para cada bot, se
reasignan aleatoriamente las etiquetas "confirmado"/"no confirmado" entre
SUS PROPIOS trades (manteniendo fijo cuántos son confirmados por bot),
nunca se mezclan aciertos entre bots distintos. Esto es lo que corrige
el sesgo: la estadística nula ya incorpora la habilidad de cada bot.

Solo lectura.
"""
import csv
import zlib
from collections import defaultdict
from datetime import datetime

import numpy as np

IN = "data/shadow/bot_wallets_gate_bucket_fase0.csv"
VENTANA_MIN = 30
N_MIN_BOT = 5      # mínimo de trades resueltos por bot para incluirlo
N_MIN_TOTAL = 15   # mínimo de trades "confirmados" agregados para concluir
ITERS = 5000


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def main():
    filas = []
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real") or r.get("acierto") not in ("0", "1"):
                continue
            filas.append(r)

    por_wallet = defaultdict(list)
    for r in filas:
        por_wallet[r["wallet"]].append(r)

    # Marca confirmado/no por trade (misma lógica que la 1a pasada)
    confirmado_por_wallet = {}  # wallet -> [(acierto, confirm_bool, activo, marco)]
    for w, trs in por_wallet.items():
        if len(trs) < N_MIN_BOT or len({t["activo"] for t in trs}) < 2:
            continue
        trs_ts = [(parse_ts(t["trade_timestamp"]), t) for t in trs]
        marcados = []
        for ts_i, ti in trs_ts:
            confirm = False
            for ts_j, tj in trs_ts:
                if tj is ti or tj["activo"] == ti["activo"]:
                    continue
                if abs((ts_j - ts_i).total_seconds()) <= VENTANA_MIN * 60 and tj["lado_wallet"] == ti["lado_wallet"]:
                    confirm = True
                    break
            marcados.append((int(ti["acierto"]), confirm, ti["activo"], ti["marco"]))
        # solo bots con AMBOS grupos no vacíos aportan información
        if any(c for _, c, _, _ in marcados) and any(not c for _, c, _, _ in marcados):
            confirmado_por_wallet[w] = marcados

    n_bots_uso = len(confirmado_por_wallet)
    print(f"Bots con >=2 activos, >={N_MIN_BOT} trades, y AMBOS grupos (con/sin confirm) no vacíos: {n_bots_uso}")

    if n_bots_uso == 0:
        print("Sin bots utilizables -- no se puede evaluar con el diseño de baseline propio todavía.")
        return

    # Estadístico observado: hit-rate agregado del grupo "confirmado"
    # MENOS hit-rate agregado del grupo "no confirmado", ambos sumados
    # across bots (cada bot pesa por su propio n).
    def estadistico(datos_por_wallet):
        hits_c = n_c = hits_s = n_s = 0
        for marcados in datos_por_wallet.values():
            for acierto, confirm, _, _ in marcados:
                if confirm:
                    hits_c += acierto
                    n_c += 1
                else:
                    hits_s += acierto
                    n_s += 1
        return hits_c, n_c, hits_s, n_s

    hits_c, n_c, hits_s, n_s = estadistico(confirmado_por_wallet)
    if n_c < N_MIN_TOTAL or n_s < N_MIN_TOTAL:
        print(f"n_confirm={n_c} n_sin_confirm={n_s} -- insuficiente para concluir (umbral {N_MIN_TOTAL})")
        return
    hit_c = hits_c / n_c
    hit_s = hits_s / n_s
    diff_obs = hit_c - hit_s
    print(f"\nAgregado (baseline propio, {n_bots_uso} bots): "
          f"con_confirm n={n_c} hit={hit_c*100:.1f}% | sin_confirm n={n_s} hit={hit_s*100:.1f}% "
          f"| diff={diff_obs*100:+.1f}pp")

    # Permutación EN BLOQUE por wallet: para cada bot, baraja qué trades
    # SUYOS son "confirmado" manteniendo fijo cuántos lo son -- nunca
    # mezcla aciertos entre bots distintos (eso es lo que neutraliza la
    # heterogeneidad de habilidad entre bots).
    rng = np.random.default_rng(zlib.crc32(b"candidata10b"))
    diffs_nulas = []
    wallets = list(confirmado_por_wallet.keys())
    for _ in range(ITERS):
        hits_c_p = n_c_p = hits_s_p = n_s_p = 0
        for w in wallets:
            marcados = confirmado_por_wallet[w]
            aciertos = np.array([a for a, _, _, _ in marcados])
            n_confirm_bot = sum(1 for _, c, _, _ in marcados if c)
            idx = rng.permutation(len(aciertos))
            idx_confirm = idx[:n_confirm_bot]
            idx_sin = idx[n_confirm_bot:]
            hits_c_p += aciertos[idx_confirm].sum()
            n_c_p += len(idx_confirm)
            hits_s_p += aciertos[idx_sin].sum()
            n_s_p += len(idx_sin)
        diffs_nulas.append(hits_c_p / n_c_p - hits_s_p / n_s_p)
    diffs_nulas = np.array(diffs_nulas)
    p_valor = float(np.mean(np.abs(diffs_nulas) >= abs(diff_obs)))
    print(f"p_valor (permutación en bloque por wallet, {ITERS} iters): {p_valor:.4f}")

    if p_valor < 0.05:
        print(f"\n🟢 SEÑAL SOBREVIVE al control de baseline propio -- diff={diff_obs*100:+.1f}pp, p={p_valor:.4f}")
    else:
        print(f"\n🔴 Señal NO sobrevive al control de baseline propio (p={p_valor:.4f}) -- "
              f"confirma que el hallazgo original era artefacto de heterogeneidad entre bots.")

    # Desagregado por activo, mismo estadístico y mismo tipo de permutación
    # pero restringido a las filas de ese activo (dentro de cada bot).
    print("\n--- Desagregado por activo (mismo diseño, exploratorio, ojo con n bajo) ---")
    activos = sorted({act for marcados in confirmado_por_wallet.values() for _, _, act, _ in marcados})
    for activo in activos:
        datos_activo = {}
        for w, marcados in confirmado_por_wallet.items():
            sub = [(a, c) for a, c, act, _ in marcados if act == activo]
            if any(c for _, c in sub) and any(not c for _, c in sub):
                datos_activo[w] = [(a, c, activo, "") for a, c in sub]
        hits_c, n_c, hits_s, n_s = estadistico(datos_activo)
        if n_c < N_MIN_TOTAL or n_s < N_MIN_TOTAL:
            print(f"  {activo:6} n_con={n_c} n_sin={n_s} -- insuficiente")
            continue
        diff = hits_c / n_c - hits_s / n_s
        print(f"  {activo:6} n_con={n_c} hit_con={hits_c/n_c*100:.1f}% "
              f"n_sin={n_s} hit_sin={hits_s/n_s*100:.1f}% diff={diff*100:+.1f}pp "
              f"(bots usados: {len(datos_activo)})")


if __name__ == "__main__":
    main()
