#!/usr/bin/env python3
"""analisis_wallet_mirror_microbucket_precio_10ago.py -- ¿sobrevive Wallet
Mirror SEGUIR a la misma cirugía de micro-bucket de precio que ya rescató
otras estrategias del proyecto (gate_bucket_propio.py) y a la corrección
Kelly exacta (kelly_precio_gate.py)?

Origen (10-Ago, petición explícita Javi tras el refutado agregado de esta
misma sesión: "conecta la solución a selección adversa/payout asimétrico
que ya tenemos, agota TODAS las opciones antes de cerrar"): el análisis
anterior (project_p24_wallet_mirror_refutado_ask_real_10ago) promedió el
ask real por (activo, jugada_grande) -- exactamente el error "agregado"
que CLAUDE.md pt.17 prohíbe. Puede haber micro-zonas de precio con edge
real mezcladas con zonas malas que cancelan el promedio, igual que pasó
con FAVORITO_CONFIRMADO/GBM_LATE/BALLENAS_TARDIAS antes de aplicarles
gate_bucket_propio.

Método: MISMO pipeline exacto que analisis_gate_bucket_propio_28jul.py
(bucket 0.05 del ASK REAL de ejecución, no precio_wallet; n>=15; shuffle
test pnl_dentro vs pnl_fuera del mismo activo; split-half cronológico;
BH-FDR por activo) pero con pnl_neto calculado con la fórmula exacta
(gross_win=(1-ask)/ask, fee 7%) en vez de leer resultados de results.csv
directamente (Wallet Mirror no pasa por shadow_predict.py).

Fuente: mismo cruce que el análisis agregado -- wallet_mirror_executor_
dryrun.csv (ask real en el momento de decisión, fillability real) x
wallet_mirror_sniper_dry_run.csv (outcome real), por wallet+market_slug+
trade_timestamp, restringido a sigue_fillable_en_decision=1.

Solo lectura -- no toca ningún gate real, no genera ninguna tupla
WALLET_MIRROR en pares_permitidos_live.
"""
import csv
import math
from collections import defaultdict
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
EXECUTOR = REPO / "data/shadow/wallet_mirror_executor_dryrun.csv"
SNIPER = REPO / "data/shadow/wallet_mirror_sniper_dry_run.csv"

STEP = 0.05
N_MIN = 15
P_MAX = 0.05
ITERS = 2000
FEE = 0.07

_rng = np.random.default_rng(42)


def bucket(p):
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def pnl_neto(ask, acierto):
    gross_win = (1 - ask) / ask
    return gross_win * (1 - FEE) if acierto else -1.0


def cargar_outcomes():
    out = {}
    with open(SNIPER, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("acierto") not in ("0", "1"):
                continue
            out[(r["wallet"], r["market_slug"], r["trade_timestamp"])] = int(r["acierto"])
    return out


def cargar_filas(tipo):
    outcomes = cargar_outcomes()
    filas = defaultdict(list)  # activo -> [(ts, ask, pnl, grande), ...]
    with open(EXECUTOR, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("tipo") != tipo or r.get("sigue_fillable_en_decision") != "1":
                continue
            clave = (r["wallet"], r["market_slug"], r["trade_timestamp"])
            ac = outcomes.get(clave)
            if ac is None:
                continue
            try:
                ask = float(r["ask_decision"])
            except (TypeError, ValueError):
                continue
            if not (0.0 < ask < 1.0):
                continue
            pnl = pnl_neto(ask, ac)
            grande = r.get("es_jugada_grande") == "1"
            filas[r["activo"]].append((r["timestamp_utc"], ask, pnl, grande))
    return filas


def shuffle_test(a, b, iters=ITERS):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    na, nb = len(a), len(b)
    diff_real = a.mean() - b.mean()
    todos = np.concatenate([a, b])
    n = na + nb
    idx = _rng.random((iters, n)).argsort(axis=1)
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


def evaluar(tipo):
    filas_por_activo = cargar_filas(tipo)
    print(f"\n{'='*90}\nTIPO={tipo}\n{'='*90}")

    pendientes = []
    for activo, filas in filas_por_activo.items():
        if len(filas) < N_MIN:
            continue
        por_bucket = defaultdict(list)
        for ts, ask, pnl, grande in filas:
            por_bucket[bucket(ask)].append((ts, pnl))

        for b, dentro in sorted(por_bucket.items()):
            n_d = len(dentro)
            if n_d < N_MIN:
                continue
            fuera = [(ts, pnl) for bb, fs in por_bucket.items() if bb != b for ts, pnl in fs]
            if not fuera:
                continue
            pnl_d = [pnl for _, pnl in dentro]
            pnl_f = [pnl for _, pnl in fuera]
            media_d = sum(pnl_d) / n_d
            diff, p_valor = shuffle_test(pnl_d, pnl_f)
            dentro_sorted = sorted(dentro, key=lambda x: x[0])
            mid = n_d // 2
            m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
            if len(m1) < 5 or len(m2) < 5:
                continue
            media_fuera = sum(pnl_f) / len(pnl_f)
            d1 = sum(pnl for _, pnl in m1) / len(m1) - media_fuera
            d2 = sum(pnl for _, pnl in m2) / len(m2) - media_fuera
            consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
            print(f"  {activo} [{b:.2f},{b+STEP:.2f}) n={n_d:>5} pnl_medio={media_d:+.4f} "
                  f"diff_vs_resto={diff:+.4f} p_shuffle={p_valor:.4f} split=[{d1:+.3f},{d2:+.3f}] "
                  f"{'consistente' if consistente else 'INCONSISTENTE'}")
            if consistente:
                pendientes.append({"activo": activo, "bucket": b, "n": n_d, "pnl_medio": media_d,
                                    "diff": diff, "p": p_valor})

    por_activo = defaultdict(list)
    for idx, p in enumerate(pendientes):
        por_activo[p["activo"]].append(idx)

    sobreviven = set()
    for activo, indices in por_activo.items():
        p_valores_grupo = [pendientes[i]["p"] for i in indices]
        sobreviven |= {indices[j] for j in bh_fdr_signif(p_valores_grupo, q=P_MAX)}

    print(f"\nTests candidatos (n>=15, split-half consistente): {len(pendientes)} | sobreviven BH-FDR por activo: {len(sobreviven)}")
    confirmados = []
    for idx in sobreviven:
        p = pendientes[idx]
        veredicto = "malo_confirmado" if p["diff"] < 0 else ("bueno_confirmado" if p["pnl_medio"] >= 0 else None)
        if veredicto:
            confirmados.append({**p, "veredicto": veredicto})
            marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
            print(f"  {marca} {p['activo']} [{p['bucket']:.2f},{p['bucket']+STEP:.2f}) n={p['n']} "
                  f"pnl_medio={p['pnl_medio']:+.4f} p={p['p']:.4f} {veredicto}")
    return confirmados


def main():
    for tipo in ("SEGUIR", "FADE"):
        evaluar(tipo)


if __name__ == "__main__":
    main()
