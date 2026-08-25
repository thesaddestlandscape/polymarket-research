#!/usr/bin/env python3
"""analisis_bot_wallets_gate_bucket_25ago.py — gate riguroso por micro-
bucket de precio real para bot_wallets_gate_bucket_fase0.py (P-GALLINA
FASE0), mismo mecanismo que analisis_wallet_mirror_gate_bucket_10ago.py
(P24) pero para las bot wallets en vez de Wallet Mirror.

Origen (25-Ago, petición explícita Javi: "soluciona 2" -- el hueco de
instrumentación identificado en la revisión de pendientes): `bot_wallets_
gate_bucket_fase0.py` medía fill-ability real (profundidad de libro en
el instante de detección) pero nunca PnL real, porque no había ningún
join contra el resultado oficial del mercado. Cerrado el mismo día
añadiendo `resolver_pendientes()` (reusa `outcome_por_slug()` de
wallet_mirror_tracker.py) al propio observador -- este script consume
ese resultado ya resuelto.

A diferencia de Wallet Mirror (2 ficheros a joinear por clave compuesta),
aquí todo vive en un único CSV (`bot_wallets_gate_bucket_fase0.csv`):
`lado_wallet` (lo que compró la wallet), `outcome_real` (ganador oficial),
`mejor_ask_deteccion` (ask REAL en el instante de detección -- nunca
`precio_wallet`, ya refutado como aproximación optimista el 10-Ago,
project_p24_wallet_mirror_refutado_ask_real_10ago).

Rigor idéntico al resto del proyecto: n>=15, shuffle test (bucket vs
resto del mismo grupo), split-half cronológico, BH-FDR por (arquetipo,
activo,marco). pnl_neto con la fórmula exacta (gross_win=(1-ask)/ask,
fee 7%) -- mismo criterio que gate_bucket_propio.py/wallet_mirror_gate_
bucket.py, nunca duplicar con una fórmula distinta.

Solo lectura, solo ESCRIBE data/shadow/bot_wallets_gate_bucket.json --
no toca ningún gate real, estas tuplas no están en pares_permitidos_live
(FASE 0, solo observación).
"""
import csv
import json
import math
import sys
import zlib
from collections import defaultdict
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import shadow_postmortem as sp  # noqa: E402 -- reusa es_pre_twap

IN = REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv"
OUT = REPO / "data/shadow/bot_wallets_gate_bucket.json"

STEP = 0.05
N_MIN = 15
P_MAX = 0.05
ITERS = 2000
FEE = 0.07


def bucket(p):
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def pnl_neto(ask, acierto):
    gross_win = (1 - ask) / ask
    return gross_win * (1 - FEE) if acierto else -1.0


def cargar_filas():
    """clave de grupo: (arquetipo, activo, marco) -> [(ts, ask, pnl), ...].
    Solo filas resueltas (outcome_real presente) y con ask real capturado
    (mejor_ask_deteccion no vacío -- si _fillability_mirror falló, no hay
    ask real que usar, la fila no aporta a PnL, solo a fill-ability)."""
    grupos = defaultdict(list)
    with open(IN, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r.get("outcome_real"):
                continue
            ask_raw = r.get("mejor_ask_deteccion", "")
            if not ask_raw:
                continue
            try:
                ask = float(ask_raw)
            except (TypeError, ValueError):
                continue
            if not (0.0 < ask < 1.0):
                continue
            marco = r.get("marco", "?")
            if sp.es_pre_twap(marco, r.get("timestamp_utc", "")):
                continue
            acierto = 1 if r.get("outcome_real") == r.get("lado_wallet") else 0
            pnl = pnl_neto(ask, acierto)
            clave = (r.get("arquetipo", "?"), r.get("activo", "?"), marco)
            grupos[clave].append((r["timestamp_utc"], ask, pnl))
    return grupos


def shuffle_test(a, b, seed_key, iters=ITERS):
    """Mismo generador seedeado por hash estable de seed_key, mismo fix
    de no-determinismo del 20-Ago (analisis_wallet_mirror_gate_bucket_
    10ago.py) -- nunca un RNG module-level compartido entre llamadas."""
    rng = np.random.default_rng(zlib.crc32(seed_key.encode("utf-8")))
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    na, nb = len(a), len(b)
    diff_real = a.mean() - b.mean()
    todos = np.concatenate([a, b])
    n = na + nb
    idx = rng.random((iters, n)).argsort(axis=1)
    permutado = todos[idx]
    media_a = permutado[:, :na].mean(axis=1)
    media_b = permutado[:, na:].mean(axis=1)
    diffs = media_a - media_b
    p_valor = float(np.mean(np.abs(diffs) >= abs(diff_real)))
    return float(diff_real), p_valor


def bh_fdr_signif(p_valores, q=0.05):
    n = len(p_valores)
    if n == 0:
        return set()
    orden = sorted(range(n), key=lambda i: p_valores[i])
    corte = -1
    for rank, i in enumerate(orden, start=1):
        if p_valores[i] <= (rank / n) * q:
            corte = rank
    if corte == -1:
        return set()
    return set(orden[:corte])


def main():
    grupos = cargar_filas()
    print(f"Grupos (arquetipo,activo,marco): {len(grupos)}")

    resultado = {}
    pendientes = []
    for clave, filas in grupos.items():
        arquetipo, activo, marco = clave
        clave_str = f"{arquetipo}#{activo}#{marco}"
        if len(filas) < N_MIN:
            resultado[clave_str] = {}
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
            media_d = sum(pnl_d) / n_d
            entrada = {"n": n_d, "pnl_medio": round(media_d, 4),
                       "shuffle_p": None, "split_half": None, "veredicto": "sin_concluir"}
            tabla[f"{b:.2f}"] = entrada
            if n_d >= N_MIN and fuera:
                pnl_f = [pnl for _, pnl in fuera]
                diff, p_valor = shuffle_test(pnl_d, pnl_f, seed_key=f"{clave_str}#{b:.2f}")
                entrada["shuffle_p"] = round(p_valor, 4)
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    media_fuera = sum(pnl_f) / len(pnl_f)
                    d1 = sum(pnl for _, pnl in m1) / len(m1) - media_fuera
                    d2 = sum(pnl for _, pnl in m2) / len(m2) - media_fuera
                    entrada["split_half"] = [round(d1, 4), round(d2, 4)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"clave_str": clave_str, "bucket": f"{b:.2f}",
                                            "entrada": entrada, "p": p_valor, "diff": diff})
        resultado[clave_str] = tabla

    # BH-FDR por (activo,marco) -- mismo nivel de agrupación que
    # analisis_wallet_mirror_gate_bucket_10ago.py usa por (activo,marco,grande).
    por_grupo = defaultdict(list)
    for idx, p in enumerate(pendientes):
        _, activo, marco = p["clave_str"].split("#")
        por_grupo[(activo, marco)].append(idx)

    sobreviven = set()
    for grupo, indices in por_grupo.items():
        p_valores = [pendientes[i]["p"] for i in indices]
        sobreviven |= {indices[j] for j in bh_fdr_signif(p_valores, q=P_MAX)}

    veredictos_nuevos = []
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        if p["diff"] < 0:
            veredicto = "malo_confirmado"
        elif p["entrada"]["pnl_medio"] >= 0:
            veredicto = "bueno_confirmado"
        else:
            continue
        p["entrada"]["veredicto"] = veredicto
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        veredictos_nuevos.append(
            f"{marca} {p['clave_str']} [{p['bucket']},{float(p['bucket'])+STEP:.2f}) "
            f"n={p['entrada']['n']} pnl_medio={p['entrada']['pnl_medio']:+.3f} p={p['p']:.4f} {veredicto}"
        )

    print(f"\n{len(veredictos_nuevos)} bucket(s) con veredicto tras BH-FDR:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
