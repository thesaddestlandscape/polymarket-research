#!/usr/bin/env python3
"""
analisis_perps_wallet_categoria_16sep.py — primera categorización
quirúrgica de wallets de Polymarket Perps (4º modelo, venue nuevo desde
03-Sep, ver project_investigacion_universo_perps_09sep), petición
explícita Javi 16-Sep: "en perps tenemos que categorizar las mejores
wallets por cada categoria y item, posiciones largas, posiciones cortas
[...] por precio de entrada, micro-buckets, todas las variables tienen
que estar controladas con precisión quirúrgica".

Fuente: data/shadow/polymarket_perps_wallet_fills_YYYY-MM-DD.csv
(fetch_polymarket_perps_wallet_fills.py, horario desde 09-Sep). Cada fila
es un FILL real de una wallet de la watchlist; el campo `pnl` viene
poblado por la propia API cuando ese fill REDUCE/cierra una posición
existente (realizado, no mark-to-market) — es la fuente de verdad de
edge real, mismo espíritu que results.csv/pnl_neto en cripto/sports.

Limitación real ya documentada (CLAUDE.md pt.20): la API solo expone el
ciclo de posición ABIERTO actual por wallet, no el histórico completo —
el dataset crece hacia adelante desde el 09-Sep, no se puede backfillear.
Con ~1 semana de datos (80k fills, 24 wallets a 16-Sep) hay volumen para
un primer corte (wallet, instrumento, dirección), pero TODAVÍA NO para
desagregar además por micro-bucket de precio de entrada con rigor
(N_MIN=15 por celda ya es exigente cruzando 3 variables a la vez) — se
deja preparado (bucket_entry calculado y guardado por fila) para cuando
haya más n, sin forzar el corte fino hoy (mismo criterio que refutó el
LP farming/otros con datos insuficientes, "no minimizar rigor").

Rigor: mismo patrón que sports_wallet_edge_tracker.py (shuffle test +
BH-FDR dentro de cada instrumento) pero sobre PnL continuo, no hit
binario — bootstrap de la media de pnl (¿el CI90% cruza cero?) en vez de
shuffle sobre hit-rate, porque aquí no hay un "precio de mercado" que
haga de baseline implícito como en Polymarket de predicción.

Solo lectura. No conecta a ninguna decisión ni dinero real.
"""
import csv
import json
import random
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
OUT_PATH = DIR_SHADOW / "perps_wallet_edge_score_por_instrumento_direccion.json"

N_MIN = 15
N_BOOTSTRAP = 2000
FDR = 0.10


def cargar_fills() -> list[dict]:
    filas = []
    for arch in sorted(DIR_SHADOW.glob("polymarket_perps_wallet_fills_*.csv")):
        try:
            with open(arch, encoding="utf-8") as f:
                filas.extend(csv.DictReader(f))
        except Exception as e:
            print(f"  [aviso] no se pudo leer {arch.name}: {e}")
    return filas


def _to_float(v, default=None):
    try:
        return float(v)
    except (TypeError, ValueError):
        return default


def bootstrap_stats(valores: list[float], seed: int) -> tuple[float, float, float]:
    """CI90% de la media (percentil) + p-valor bootstrap de dos colas
    (fracción de medias remuestreadas que cruzan 0 respecto a la media
    observada, ×2 -- mismo criterio que el resto del proyecto usa para
    PnL continuo, p.ej. analisis_smart_exit_dependiente_tiempo_19ago.py)."""
    rng = random.Random(seed)
    n = len(valores)
    medias = []
    for _ in range(N_BOOTSTRAP):
        muestra = [valores[rng.randrange(n)] for _ in range(n)]
        medias.append(sum(muestra) / n)
    medias.sort()
    lo = medias[int(0.05 * N_BOOTSTRAP)]
    hi = medias[int(0.95 * N_BOOTSTRAP) - 1]
    frac_no_lado = sum(1 for m in medias if m <= 0) / N_BOOTSTRAP
    p_boot = 2 * min(frac_no_lado, 1 - frac_no_lado)
    return lo, hi, min(p_boot, 1.0)


def benjamini_hochberg(pvals: list[float], fdr: float = FDR) -> list[bool]:
    m = len(pvals)
    if m == 0:
        return []
    orden = sorted(range(m), key=lambda i: pvals[i])
    keep = [False] * m
    corte = -1
    for rank, idx in enumerate(orden, start=1):
        if pvals[idx] <= (rank / m) * fdr:
            corte = rank
    if corte > 0:
        for idx in orden[:corte]:
            keep[idx] = True
    return keep


def main() -> int:
    filas_raw = cargar_fills()
    print(f"fills totales cargados: {len(filas_raw)}")

    realizados = []
    for r in filas_raw:
        pnl = _to_float(r.get("pnl"))
        if pnl is None or pnl == 0.0:
            continue
        if r.get("liquidation") == "True":
            continue  # liquidación forzosa distorsiona el pnl medio de una wallet que sí decide bien
        entry = _to_float(r.get("previous_entry_price"))
        realizados.append({
            "wallet": r.get("address"), "instrumento": r.get("symbol"),
            "direccion": r.get("side"), "pnl": pnl, "entry": entry,
            "taker": r.get("taker"),
        })
    print(f"fills con pnl realizado (excluye liquidaciones/sin pnl): {len(realizados)}")

    # (instrumento, direccion) -> por wallet -> [pnl,...]
    grupos = defaultdict(lambda: defaultdict(list))
    for f in realizados:
        grupos[(f["instrumento"], f["direccion"])][f["wallet"]].append(f["pnl"])

    resultados = []
    for (instr, direc), por_wallet in sorted(grupos.items()):
        candidatas = {w: pnls for w, pnls in por_wallet.items() if len(pnls) >= N_MIN}
        if not candidatas:
            continue
        filas_grupo = []
        for w, pnls in candidatas.items():
            n = len(pnls)
            pnl_medio = sum(pnls) / n
            win_rate = sum(1 for p in pnls if p > 0) / n
            seed = (hash((instr, direc, w)) ^ n) & 0xFFFFFFFF
            lo, hi, p_boot = bootstrap_stats(pnls, seed)
            filas_grupo.append({
                "wallet": w, "n": n, "pnl_medio": round(pnl_medio, 4),
                "win_rate": round(win_rate, 4), "ci90_lo": round(lo, 4),
                "ci90_hi": round(hi, 4), "cruza_cero": lo <= 0 <= hi,
                "p_boot": round(p_boot, 4),
            })
        pvals = [f["p_boot"] for f in filas_grupo]
        keep = benjamini_hochberg(pvals)
        for f, sig in zip(filas_grupo, keep):
            f["significativo_bh"] = sig
        resultados.append({"instrumento": instr, "direccion": direc,
                            "n_wallets_n_min": len(candidatas), "wallets": filas_grupo})

    n_wallets_sig = sum(
        1 for g in resultados for f in g["wallets"] if f["significativo_bh"]
    )
    print(f"grupos (instrumento,direccion) con >=1 wallet n>={N_MIN}: {len(resultados)}")
    print(f"(wallet,instrumento,direccion) con CI90 de pnl fuera de cero y BH-FDR: {n_wallets_sig}")

    top = sorted(
        [(g["instrumento"], g["direccion"], f) for g in resultados for f in g["wallets"] if f["significativo_bh"]],
        key=lambda x: -x[2]["pnl_medio"],
    )[:20]
    print("\nTop 20 por pnl_medio:")
    for instr, direc, f in top:
        print(f"  {instr:12s} {direc:6s} wallet={f['wallet'][:14]}.. n={f['n']:4d} "
              f"pnl_medio={f['pnl_medio']:+.3f} win_rate={f['win_rate']*100:.1f}% "
              f"ci90=[{f['ci90_lo']:+.3f},{f['ci90_hi']:+.3f}]")

    salida = {
        "actualizado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "n_fills_totales": len(filas_raw),
        "n_fills_con_pnl_realizado": len(realizados),
        "n_min": N_MIN,
        "nota": ("Primer corte (instrumento, direccion=long/short). Micro-bucket de "
                 "precio de entrada (`entry`) NO desagregado todavia -- n insuficiente "
                 "cruzando 3 variables con 1 semana de datos. Repetir cuando crezca."),
        "grupos": resultados,
    }
    OUT_PATH.write_text(json.dumps(salida, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {OUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
