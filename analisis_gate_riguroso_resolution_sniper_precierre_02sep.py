#!/usr/bin/env python3
"""
analisis_gate_riguroso_resolution_sniper_precierre_02sep.py — gate
riguroso completo (grid fijo + ventana deslizante fina) para
RESOLUTION_SNIPER_PRECIERRE (offset -1/-2s antes del cierre nominal,
`resolution_sniper_precierre_depth_fase0.py`, ver [[idea_resolution_
sniper_precierre_confirmado_02sep]] en memoria nativa).

Origen (02-Sep, propuesta B3 del barrido "edge sin capturar", petición
explícita Javi: "vamos a ver si está para live en micro-buckets propio
y micro-buckets fino"): el agregado por moneda ya confirmó edge fuerte
(n=184 fillable, hit=89,1%, Wilson90%[84,8%,92,3%], EV neto+fee=
+0,417€/trade) pero ninguna promoción se hace sin el mismo rigor de
micro-bucket que el resto del proyecto (gate_bucket_propio.py + gate_
bucket_fino.py) y la regla del 01-Sep de exigir convergencia grid+fino.

Mecánica idéntica a gate_bucket_propio.py/analisis_gate_bucket_fino.py
pero sobre datos propios (no results.csv, esquema distinto -- este
family todavía no tiene entrada formal en strategy_params.json): reusa
shuffle_test/bh_fdr_signif de analisis_gate_bucket_propio_28jul.py, no
reinventa el test estadístico.

Colapsa por market_id (offset más cercano a 0, regla canónica CLAUDE.md
3b) y restringe SIEMPRE al subconjunto fillable (ratio_vs_stake>=5x) --
es la población que de verdad se podría ejecutar.

FEE=0.07 (crypto). Cada fila = comprar `direccion_implicita` al precio
`mejor_ask`, resultado = acierto si direccion_implicita==outcome_real.

Solo lectura -- no conecta a ninguna decisión real. Genera
data/shadow/resolution_sniper_precierre_gate_riguroso.json.
"""
import glob
import json
from pathlib import Path

import numpy as np

from analisis_gate_bucket_propio_28jul import shuffle_test, bh_fdr_signif

REPO = Path(__file__).resolve().parent
FEE = 0.07
N_MIN_GRID = 15       # piso informativo (CLAUDE.md: nunca concluir con n<15)
N_MIN_LIVE = 40        # umbral real de confirmación para dinero real (mismo que el resto del proyecto)
MIN_RATIO_LIBRO = 5.0
STEP_GRID = 0.05
STEP_SCAN = 0.01
WIDTH_FINO = 0.05
N_MIN_FINO = 40
ITERS = 2000
OUT = REPO / "data" / "shadow" / "resolution_sniper_precierre_gate_riguroso.json"


def _bucket(ask: float) -> float:
    return round(int(ask / STEP_GRID) * STEP_GRID, 2)


def _pnl(ask: float, acierto: bool) -> float:
    fee = FEE * ask * (1 - ask)
    return (1.0 / ask - 1.0) - fee if acierto else -1.0


def _cargar_filas() -> list[dict]:
    outcome: dict[str, str] = {}
    for f in sorted(glob.glob(str(REPO / "data/shadow/resolution_sniper_obs_2026-*.csv"))):
        import csv
        with open(f, encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                if row.get("outcome_real") not in (None, ""):
                    outcome[row["market_id"]] = row["outcome_real"]

    import csv
    depth_path = REPO / "data/shadow/resolution_sniper_precierre_depth_fase0.csv"
    por_mercado: dict[str, dict] = {}
    with open(depth_path, encoding="utf-8") as fh:
        for d in csv.DictReader(fh):
            mid = d["market_id"]
            off = abs(int(d["offset_s"]))
            actual = por_mercado.get(mid)
            if actual is None or off < abs(int(actual["offset_s"])):
                por_mercado[mid] = d

    filas = []
    for mid, d in por_mercado.items():
        if mid not in outcome:
            continue
        try:
            ratio = float(d["ratio_vs_stake"])
            ask = float(d["mejor_ask"])
        except (TypeError, ValueError):
            continue
        if ratio < MIN_RATIO_LIBRO:
            continue
        if not (0.01 < ask < 0.99):
            continue
        acierto = d["direccion_implicita"] == outcome[mid]
        filas.append({
            "activo": d["activo"], "ask": ask, "acierto": acierto,
            "pnl": _pnl(ask, acierto),
        })
    return filas


def _wilson90_lo(hit: float, n: int) -> float:
    z = 1.645
    denom = 1 + z ** 2 / n
    centro = (hit + z ** 2 / (2 * n)) / denom
    margen = z * np.sqrt(hit * (1 - hit) / n + z ** 2 / (4 * n ** 2)) / denom
    return float(centro - margen)


def _evaluar_grupo(filas: list[dict], resto: list[dict]) -> dict:
    n = len(filas)
    hit = sum(1 for f in filas if f["acierto"]) / n
    pnl_medio = sum(f["pnl"] for f in filas) / n
    ask_medio = sum(f["ask"] for f in filas) / n
    wilson90lo = _wilson90_lo(hit, n)
    pnls_a = [f["pnl"] for f in filas]
    pnls_b = [f["pnl"] for f in resto] if resto else [0.0]
    diff, p_shuffle = shuffle_test(pnls_a, pnls_b, iters=ITERS) if resto else (pnl_medio, None)
    mitad = n // 2
    sh1 = filas[:mitad]
    sh2 = filas[mitad:]
    split_ok = None
    if mitad >= 5:
        pm1 = sum(f["pnl"] for f in sh1) / len(sh1)
        pm2 = sum(f["pnl"] for f in sh2) / len(sh2)
        split_ok = (pm1 > 0) == (pm2 > 0) and pm1 > 0
    return {
        "n": n, "hit": round(hit, 4), "pnl_medio": round(pnl_medio, 4),
        "ask_medio": round(ask_medio, 4), "wilson90lo": round(wilson90lo, 4),
        "breakeven_aprox": round(ask_medio, 4), "diff_pnl_vs_resto": round(diff, 4),
        "p_shuffle": round(p_shuffle, 4) if p_shuffle is not None else None,
        "split_half_positivo_ambas": split_ok,
        "n_min_live_ok": n >= N_MIN_LIVE,
    }


def grid_por_activo(filas: list[dict]) -> dict:
    resultado = {}
    activos = sorted({f["activo"] for f in filas})
    p_valores = []
    claves = []
    evals = {}
    for activo in activos:
        del_activo = [f for f in filas if f["activo"] == activo]
        buckets: dict[float, list] = {}
        for f in del_activo:
            buckets.setdefault(_bucket(f["ask"]), []).append(f)
        for b, grupo in buckets.items():
            if len(grupo) < N_MIN_GRID:
                continue
            resto = [f for f in filas if f not in grupo]
            ev = _evaluar_grupo(grupo, resto)
            claves.append((activo, b))
            evals[(activo, b)] = ev
            p_valores.append(ev["p_shuffle"] if ev["p_shuffle"] is not None else 1.0)
    sobreviven = bh_fdr_signif(p_valores, q=0.05)
    for i, k in enumerate(claves):
        ev = evals[k]
        ev["p_bh_signif"] = i in sobreviven
        if ev["n_min_live_ok"] and ev["p_bh_signif"] and ev["wilson90lo"] > ev["breakeven_aprox"] and ev["split_half_positivo_ambas"]:
            ev["veredicto"] = "bueno_confirmado"
        elif ev["n"] >= N_MIN_GRID:
            ev["veredicto"] = "sin_concluir"
        resultado[f"{k[0]}#{k[1]:.2f}"] = ev
    return resultado


def fino_por_activo(filas: list[dict]) -> dict:
    """Ventana deslizante paso 0.01 ancho 0.05, max-statistic sobre el
    mismo activo (mismo criterio que analisis_gate_bucket_fino.py:
    corrige por buscar entre ~19 posiciones dentro de [0,1))."""
    resultado = {}
    for activo in sorted({f["activo"] for f in filas}):
        del_activo = sorted([f for f in filas if f["activo"] == activo], key=lambda f: f["ask"])
        asks = np.array([f["ask"] for f in del_activo])
        pnls = np.array([f["pnl"] for f in del_activo])
        mejor = None
        for lo in np.arange(0.0, 1.0 - WIDTH_FINO + 1e-9, STEP_SCAN):
            mask = (asks >= lo) & (asks < lo + WIDTH_FINO)
            n = int(mask.sum())
            if n < N_MIN_FINO:
                continue
            pm = float(pnls[mask].mean())
            if mejor is None or pm > mejor[2]:
                mejor = (lo, n, pm, mask)
        if mejor is None:
            resultado[activo] = {"veredicto": "n_insuficiente_para_ventana", "n_max_bucket": int(mask.sum()) if 'mask' in dir() else None}
            continue
        lo, n, pm, mask = mejor
        grupo = [del_activo[i] for i in range(len(del_activo)) if mask[i]]
        resto = [del_activo[i] for i in range(len(del_activo)) if not mask[i]]
        ev = _evaluar_grupo(grupo, resto)
        ev["lo"] = round(float(lo), 3)
        ev["hi"] = round(float(lo) + WIDTH_FINO, 3)
        ev["veredicto"] = (
            "bueno_confirmado"
            if ev["n_min_live_ok"] and ev["wilson90lo"] > ev["breakeven_aprox"] and ev["split_half_positivo_ambas"]
            else "sin_concluir"
        )
        resultado[activo] = ev
    return resultado


def main() -> None:
    filas = _cargar_filas()
    grid = grid_por_activo(filas)
    fino = fino_por_activo(filas)
    resultado = {"n_filas_fillable": len(filas), "grid": grid, "fino": fino}
    OUT.write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")
    n_grid_ok = sum(1 for v in grid.values() if v.get("veredicto") == "bueno_confirmado")
    n_fino_ok = sum(1 for v in fino.values() if v.get("veredicto") == "bueno_confirmado")
    print(f"[gate_riguroso_resolution_sniper_precierre] n={len(filas)} "
          f"grid_confirmados={n_grid_ok} fino_confirmados={n_fino_ok} -> {OUT}")


if __name__ == "__main__":
    main()
