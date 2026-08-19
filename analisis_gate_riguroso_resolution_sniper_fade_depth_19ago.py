#!/usr/bin/env python3
"""analisis_gate_riguroso_resolution_sniper_fade_depth_19ago.py — gate
riguroso completo (Wilson90 + shuffle + split-half + BH-FDR) sobre
resolution_sniper_fade_depth_fase0.py, ahora que cruzó n>=40 (521 filas,
19-Ago, prioridad #1 del checklist de sesión).

Contexto (ver docstring de resolution_sniper_fade_depth_fase0.py /
memoria idea_wallet_sniper_099_confirmacion_externa_17ago): el hallazgo
14-Ago fue que FADEAR la dirección implícita de Chainlink en offset 0-3s
post-cierre nominal (BTC#5min sobre todo, origen wallet real 0x0bba) da
hit=80% en shadow SIN filtrar profundidad -- este observador mide si esa
oportunidad tiene profundidad real detrás (ratio_fade_vs_stake>=5x, mismo
umbral de fillability real que el resto del proyecto, ej. gbmlate_fade_
depth_fase0.py).

Join: resolution_sniper_fade_depth_fase0.csv (profundidad del lado fade)
contra resolution_sniper_obs_*.csv (outcome_real por market_id) -- el
propio market_id resuelve el resultado real del mercado sin ambigüedad.

Segmentado por (activo, marco) -- CLAUDE.md pt.17, nunca solo agregado.
Compara fillable (ratio>=5x) vs no fillable, igual que el patrón ya usado
en P23/gbmlate_fade_depth/wallet_mirror.

Solo lectura, no escribe ningún gate real ni toca dinero.
"""
import csv
import glob
import math
import random
from collections import defaultdict

FADE_CSV = "data/shadow/resolution_sniper_fade_depth_fase0.csv"
OBS_GLOB = "data/shadow/resolution_sniper_obs_*.csv"

Z_90 = 1.645
N_MIN = 15
N_SHUFFLE = 2000
FEE = 0.07
STAKE_REF = 1.05
RATIO_FILLABLE_MIN = 5.0


def wilson_lower(hits: int, n: int, z: float = Z_90) -> float:
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def pnl_trade(ask: float, acierto: bool) -> float:
    gross_win = (1 - ask) / ask
    return STAKE_REF * (gross_win * (1 - FEE) if acierto else -1.0)


def cargar_outcomes() -> dict:
    """market_id -> outcome_real ('Up'/'Down'), primera fila válida por mercado."""
    out = {}
    for fn in sorted(glob.glob(OBS_GLOB)):
        with open(fn, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                mid = r.get("market_id")
                oc = r.get("outcome_real")
                if mid and oc in ("Up", "Down") and mid not in out:
                    out[mid] = oc
    return out


def cargar_fade():
    outcomes = cargar_outcomes()
    filas = []
    con_outcome = 0
    with open(FADE_CSV, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            mid = r.get("market_id")
            oc = outcomes.get(mid)
            if oc is None:
                continue
            con_outcome += 1
            try:
                ask_fade = float(r["ask_fade"])
            except (TypeError, ValueError):
                continue
            if not (0.0 < ask_fade < 1.0):
                continue
            try:
                ratio = float(r["ratio_fade_vs_stake"])
            except (TypeError, ValueError):
                ratio = None
            dir_fade = r["direccion_fade"]
            acierto = (dir_fade == oc)
            filas.append({
                "activo": r["activo"], "marco": r["marco"],
                "offset": r["offset_s"], "ts": r["timestamp_utc"],
                "ask_fade": ask_fade, "ratio": ratio,
                "acierto": acierto,
                "pnl": pnl_trade(ask_fade, acierto),
            })
    print(f"Fade rows totales: {sum(1 for _ in open(FADE_CSV, encoding='utf-8')) - 1}")
    print(f"Con outcome_real resuelto (join market_id): {con_outcome}")
    print(f"Con ask_fade válido: {len(filas)}\n")
    return filas


def shuffle_pnl(grupo, n_shuffle=N_SHUFFLE):
    """Baraja las etiquetas de acierto dentro del grupo (mismo ask_fade fijo
    por fila), recalcula pnl medio -- ¿el pnl real supera lo que daría un
    acierto aleatorio p=0.5 con los mismos asks?"""
    n = len(grupo)
    hits_real = sum(1 for g in grupo if g["acierto"])
    pnl_real = sum(g["pnl"] for g in grupo) / n
    random.seed(42)
    mayor_igual = 0
    asks = [g["ask_fade"] for g in grupo]
    for _ in range(n_shuffle):
        pnl_shuf = sum(pnl_trade(a, random.random() < 0.5) for a in asks) / n
        if pnl_shuf >= pnl_real:
            mayor_igual += 1
    return mayor_igual / n_shuffle, pnl_real, hits_real / n


def analizar(filas, etiqueta):
    print(f"=== {etiqueta} (n={len(filas)}) ===")
    grupos = defaultdict(list)
    for f in filas:
        grupos[(f["activo"], f["marco"])].append(f)

    print(f"{'activo':<6}{'marco':<7}{'n':>5}{'hit%':>8}{'wilson90lo':>12}"
          f"{'ask_medio':>11}{'pnl/tr':>9}{'p_shuf':>8}{'split1':>8}{'split2':>8}")
    resultados = []
    for (activo, marco), grupo in sorted(grupos.items()):
        n = len(grupo)
        if n < N_MIN:
            continue
        hits = sum(1 for g in grupo if g["acierto"])
        hit_rate = hits / n
        wlo = wilson_lower(hits, n)
        ask_medio = sum(g["ask_fade"] for g in grupo) / n
        pnl_medio = sum(g["pnl"] for g in grupo) / n
        p_shuf, _, _ = shuffle_pnl(grupo)

        ordenado = sorted(grupo, key=lambda g: g["ts"])
        mitad = len(ordenado) // 2
        h1, h2 = ordenado[:mitad], ordenado[mitad:]
        pnl1 = sum(g["pnl"] for g in h1) / len(h1) if h1 else 0
        pnl2 = sum(g["pnl"] for g in h2) / len(h2) if h2 else 0

        print(f"{activo:<6}{marco:<7}{n:>5}{hit_rate*100:>7.1f}%{wlo:>12.3f}"
              f"{ask_medio:>11.3f}{pnl_medio:>+9.3f}{p_shuf:>8.4f}{pnl1:>+8.3f}{pnl2:>+8.3f}")
        resultados.append({
            "activo": activo, "marco": marco, "n": n, "hit_rate": hit_rate,
            "wilson90_lo": wlo, "ask_medio": ask_medio, "pnl_medio": pnl_medio,
            "p_shuffle": p_shuf, "split1": pnl1, "split2": pnl2,
        })

    if filas:
        p_shuf_agg, pnl_agg, hit_agg = shuffle_pnl(filas)
        print(f"\nAgregado {etiqueta}: n={len(filas)} hit={hit_agg*100:.1f}% "
              f"pnl/tr={pnl_agg:+.3f}€ p_shuffle={p_shuf_agg:.4f}")

    # BH-FDR sobre los p_shuffle de los grupos con n>=N_MIN
    if resultados:
        m = len(resultados)
        ordenados = sorted(resultados, key=lambda r: r["p_shuffle"])
        for i, r in enumerate(ordenados, start=1):
            r["bh_umbral"] = (i / m) * 0.05
            r["bh_pasa"] = r["p_shuffle"] <= r["bh_umbral"]

    print("\nGATE: n>=15, wilson90lo > ask_medio (edge real tras el precio), "
          "pnl/tr>0, p_shuffle<0.05, split-half incluso signo, BH-FDR pasa.")
    gate_ok = [r for r in resultados
               if r["wilson90_lo"] > r["ask_medio"] and r["pnl_medio"] > 0
               and r["p_shuffle"] < 0.05
               and (r["split1"] > 0) == (r["split2"] > 0)
               and r.get("bh_pasa")]
    print(f"Combos GATE OK: {len(gate_ok)} de {len(resultados)} evaluados (n>=15)")
    for r in gate_ok:
        print(f"  🟢 {r['activo']}#{r['marco']}: n={r['n']} hit={r['hit_rate']*100:.1f}% "
              f"wilson90lo={r['wilson90_lo']:.3f} pnl/tr={r['pnl_medio']:+.3f}€ "
              f"p_shuffle={r['p_shuffle']:.4f}")
    print()
    return resultados


def main():
    filas = cargar_fade()
    if not filas:
        print("Sin filas con outcome_real resuelto todavía -- nada que evaluar.")
        return

    fillable = [f for f in filas if f["ratio"] is not None and f["ratio"] >= RATIO_FILLABLE_MIN]
    no_fillable = [f for f in filas if f["ratio"] is not None and f["ratio"] < RATIO_FILLABLE_MIN]
    sin_dato = [f for f in filas if f["ratio"] is None]
    print(f"Split fillability: fillable(ratio>={RATIO_FILLABLE_MIN}x)={len(fillable)} "
          f"no_fillable={len(no_fillable)} sin_dato_profundidad={len(sin_dato)}\n")

    analizar(filas, "TODAS (sin filtrar profundidad)")
    if fillable:
        analizar(fillable, f"FILLABLE (ratio_fade_vs_stake>={RATIO_FILLABLE_MIN}x)")
    else:
        print(f"=== FILLABLE (ratio>={RATIO_FILLABLE_MIN}x): 0 filas -- profundidad real nunca alcanza el umbral todavía ===\n")
    if no_fillable:
        analizar(no_fillable, f"NO FILLABLE (ratio<{RATIO_FILLABLE_MIN}x)")


if __name__ == "__main__":
    main()
