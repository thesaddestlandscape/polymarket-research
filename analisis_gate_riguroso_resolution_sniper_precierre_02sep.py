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
# 03-Sep: el fino de este script hacía shuffle SIMPLE sobre la mejor de ~95
# ventanas -- p-valor inflado por multiplicidad, el error exacto que
# CLAUDE.md ya documenta como cazado en analisis_gate_bucket_fino.py
# (allí: p=0,0073 con shuffle simple -> p=0,262 con max-statistic). Se reusa
# su `evaluar_tupla` (permutación MAX-STATISTIC + split-half + LOO +
# bootstrap CI90) en vez de reimplementar el test.
from analisis_gate_bucket_fino import evaluar_tupla as _evaluar_tupla_fino

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
    # 03-Sep: NO se colapsa entre offsets. Antes se guardaba una sola fila por
    # market_id (la del offset más cercano a 0) -- con la rejilla ampliada
    # [-30..-1] eso mezclaría distribuciones distintas bajo la misma etiqueta:
    # un mercado sin fila a -1s (filtrado por ask fuera de rango ahí) pero con
    # fila a -8s entraría en el mismo grupo que los -1s. El offset es un EJE
    # de análisis, no ruido a colapsar: mover el offset cambia la
    # distribución (a -8s el mercado es más incierto y el ask es otro), así
    # que el gate se re-corre por offset y NUNCA se hereda entre ellos.
    # El colapso canónico de CLAUDE.md 3b (no contar filas repetidas de la
    # misma señal) se mantiene: dedup por (market_id, offset_s).
    por_mercado: dict[tuple[str, str], dict] = {}
    with open(depth_path, encoding="utf-8") as fh:
        for d in csv.DictReader(fh):
            por_mercado[(d["market_id"], d["offset_s"])] = d

    filas = []
    for (mid, off_s), d in por_mercado.items():
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
            "offset_s": off_s,
            # ts para el split-half CRONOLÓGICO de evaluar_tupla (antes el
            # split-half partía por orden de inserción del dict, que no es
            # tiempo -- otra fuente silenciosa de falso positivo).
            "ts": d.get("timestamp_utc", ""),
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


def grid_por_offset_activo(filas: list[dict]) -> dict:
    """Grid segmentado por (offset, activo). La corrección BH-FDR se acumula
    sobre TODOS los tests de TODOS los offsets a la vez (03-Sep): con 8
    offsets × 6 activos × buckets, corregir dentro de cada offset por
    separado dejaría sin corregir la multiplicidad de haber probado 8
    offsets -- falsos positivos garantizados (mismo mecanismo que ya
    convirtió el techo de pnl_fiel_v2 en ruido de multiple-testing).
    El `resto` de cada shuffle es del MISMO offset: comparar contra otro
    offset mezclaría distribuciones distintas."""
    resultado: dict[str, dict] = {}
    p_valores: list[float] = []
    claves: list[tuple[str, str, float]] = []
    evals: dict[tuple[str, str, float], dict] = {}
    for off in sorted({f["offset_s"] for f in filas}, key=lambda o: -abs(int(o))):
        del_offset = [f for f in filas if f["offset_s"] == off]
        for activo in sorted({f["activo"] for f in del_offset}):
            del_activo = [f for f in del_offset if f["activo"] == activo]
            buckets: dict[float, list] = {}
            for f in del_activo:
                buckets.setdefault(_bucket(f["ask"]), []).append(f)
            for b, grupo in buckets.items():
                if len(grupo) < N_MIN_GRID:
                    continue
                ids_grupo = {id(f) for f in grupo}
                resto = [f for f in del_offset if id(f) not in ids_grupo]
                ev = _evaluar_grupo(grupo, resto)
                claves.append((off, activo, b))
                evals[(off, activo, b)] = ev
                p_valores.append(ev["p_shuffle"] if ev["p_shuffle"] is not None else 1.0)
    sobreviven = bh_fdr_signif(p_valores, q=0.05)
    for i, k in enumerate(claves):
        ev = evals[k]
        ev["p_bh_signif"] = i in sobreviven
        ev["offset_s"] = k[0]
        if ev["n_min_live_ok"] and ev["p_bh_signif"] and ev["wilson90lo"] > ev["breakeven_aprox"] and ev["split_half_positivo_ambas"]:
            ev["veredicto"] = "bueno_confirmado"
        elif ev["n"] >= N_MIN_GRID:
            ev["veredicto"] = "sin_concluir"
        resultado.setdefault(k[0], {})[f"{k[1]}#{k[2]:.2f}"] = ev
    return resultado


def fino_por_offset_activo(filas: list[dict]) -> dict:
    """Ventana deslizante con permutación MAX-STATISTIC real, por (offset,
    activo).

    03-Sep, hallazgo de /code-review: la versión anterior de esta función
    prometía max-statistic en el docstring pero NO lo implementaba --
    elegía la mejor de ~95 ventanas y le aplicaba un shuffle SIMPLE
    (`_evaluar_grupo`), que no corrige por haber buscado entre todas esas
    posiciones. Encima su veredicto ni siquiera miraba `p_shuffle`: bastaba
    n≥40 + Wilson>breakeven + split-half. Es el mismo error ya cazado y
    documentado en `analisis_gate_bucket_fino.py` (p=0,0073 con shuffle
    simple -> p=0,262 con la corrección). Importa porque este gate es el
    que autoriza dinero real vía `resolution_sniper_precierre_gate.py`.

    Ahora se delega en `analisis_gate_bucket_fino.evaluar_tupla` (permutación
    max-statistic + split-half cronológico + LOO + bootstrap CI90) y el
    veredicto EXIGE significancia tras BH-FDR global sobre todos los
    (offset, activo) probados.
    """
    candidatos: dict[tuple[str, str], dict] = {}
    p_valores: list[float] = []
    claves: list[tuple[str, str]] = []
    for off in sorted({f["offset_s"] for f in filas}, key=lambda o: -abs(int(o))):
        del_offset = [f for f in filas if f["offset_s"] == off]
        for activo in sorted({f["activo"] for f in del_offset}):
            del_activo = [f for f in del_offset if f["activo"] == activo]
            ev = _evaluar_tupla_fino([(f["ts"], f["ask"], f["pnl"]) for f in del_activo])
            if not ev:
                candidatos[(off, activo)] = {
                    "veredicto": "n_insuficiente_para_ventana", "n_disponible": len(del_activo)}
                continue
            # hit/Wilson sobre la ventana ganadora (evaluar_tupla devuelve
            # PnL, no hit): se recalculan con sus propios límites lo/hi.
            grupo = [f for f in del_activo if ev["lo"] <= f["ask"] < ev["hi"]]
            n_g = len(grupo)
            hit = (sum(1 for f in grupo if f["acierto"]) / n_g) if n_g else 0.0
            ask_medio = (sum(f["ask"] for f in grupo) / n_g) if n_g else 0.0
            ev.update({
                "offset_s": off, "hit": round(hit, 4),
                "ask_medio": round(ask_medio, 4),
                "breakeven_aprox": round(ask_medio, 4),
                "wilson90lo": round(_wilson90_lo(hit, n_g), 4) if n_g else None,
                "n_min_live_ok": n_g >= N_MIN_LIVE,
            })
            candidatos[(off, activo)] = ev
            claves.append((off, activo))
            p_valores.append(ev.get("p_valor", 1.0))
    sobreviven = bh_fdr_signif(p_valores, q=0.05)
    for i, k in enumerate(claves):
        ev = candidatos[k]
        ev["p_bh_signif"] = i in sobreviven
        ev["veredicto"] = (
            "bueno_confirmado"
            if (ev["n_min_live_ok"] and ev["p_bh_signif"] and ev["split_half_ok"]
                and ev["wilson90lo"] is not None and ev["wilson90lo"] > ev["breakeven_aprox"])
            else "sin_concluir"
        )
    resultado: dict[str, dict] = {}
    for (off, activo), ev in candidatos.items():
        resultado.setdefault(off, {})[activo] = ev
    return resultado


def _fino_por_activo_OBSOLETO(filas: list[dict]) -> dict:
    """OBSOLETO (03-Sep) -- conservado solo como referencia del test débil
    que se sustituyó. No llamar: no corrige multiplicidad de ventana."""
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
    grid = grid_por_offset_activo(filas)
    fino = fino_por_offset_activo(filas)
    # Formato con EJE DE OFFSET (03-Sep). El gate vivo
    # (resolution_sniper_precierre_gate.py) exige el offset y falla cerrado
    # si no hay evidencia de ESE offset -- un edge medido a -1s no autoriza
    # nada a -8s.
    por_offset: dict[str, dict] = {}
    for off in sorted(set(grid) | set(fino), key=lambda o: -abs(int(o))):
        por_offset[off] = {"grid": grid.get(off, {}), "fino": fino.get(off, {})}
    n_por_offset = {}
    for f in filas:
        n_por_offset[f["offset_s"]] = n_por_offset.get(f["offset_s"], 0) + 1
    resultado = {
        "formato": "por_offset_v2",
        "n_filas_fillable": len(filas),
        "n_por_offset": n_por_offset,
        "por_offset": por_offset,
    }
    OUT.write_text(json.dumps(resultado, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"[gate_riguroso_resolution_sniper_precierre] n={len(filas)} "
          f"offsets={sorted(n_por_offset, key=lambda o: -abs(int(o)))}")
    for off, blq in por_offset.items():
        g_ok = [k for k, v in blq["grid"].items() if v.get("veredicto") == "bueno_confirmado"]
        f_ok = [k for k, v in blq["fino"].items() if v.get("veredicto") == "bueno_confirmado"]
        conv = sorted({k.split("#")[0] for k in g_ok} & set(f_ok))
        print(f"  offset={off:>4}s n={n_por_offset.get(off,0):>4} "
              f"grid_ok={len(g_ok)} fino_ok={len(f_ok)} CONVERGEN={conv or '-'}")


if __name__ == "__main__":
    main()
