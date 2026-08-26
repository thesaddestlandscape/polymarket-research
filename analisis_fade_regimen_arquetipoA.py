#!/usr/bin/env python3
"""
analisis_fade_regimen_arquetipoA.py — 26-Ago, petición explícita Javi
tras resolver GBM_LATE vía ejecución reactiva: "vamos a solucionar todo
lo que tiene arquetipo A o está en el cementerio... si se ha solucionado
esto, no hay nada que no podamos solucionar".

Generaliza el hallazgo puntual de esta sesión (MOMENTUM_IBS_15M#BNB#15min
#BUY_NO [0.45,0.50): original -0.143€/tr, fade real +0.095€/tr no
significativo, fade condicionado a ballenas_dentro_banda=False +0.173€/tr
SÍ pasa rigor) a CUALQUIER tupla candidato_evaluacion con fade real
capturado por fade_depth_universal_fase0.py (universal desde 14-Ago,
cubre cualquier estrategia salvo WEEKLY_PRICE, que tiene su propio
mecanismo).

Procedimiento por cada (strategy, subtype, direction) con datos de fade:
  1. Fill-ability real del lado ORIGINAL (libro_snapshots.csv, colapsado
     por market_id con la prioridad canónica de analisis_fills.py,
     ratio_vs_stake>=5x) -- si pnl_medio>=0 o n<15, no es candidata a
     fade (se descarta, se registra igual para transparencia).
  2. FADE real: usa precio_contrario/ratio_contrario_min de
     fade_depth_universal_fase0.csv (profundidad REAL del lado
     contrario, no aproximada -- feedback_payout_fade_usa_posicion_
     propia_24ago). acierto_fade = 1-acierto_original (mercado binario).
     pnl con la fórmula estándar del proyecto (fee 7% sobre ganancia).
  3. Si el fade base (sin filtro) ya pasa rigor (n>=15, wilson90lo>
     breakeven, split-half ambas mitades positivas, binomial p<0.05):
     veredicto "fade_confirmado_sin_filtro".
  4. Si no, prueba 3 filtros de régimen INDIVIDUALES (nunca combinados
     entre sí -- combinar sobre la misma muestra es sobreajuste, ver
     nota de la sesión 26-Ago) sobre el subconjunto fade, en orden de
     prioridad económica (ballenas > smart money > hora): cada uno debe
     pasar el mismo rigor con n>=15 para marcar "fade_confirmado_con_
     filtro:<nombre>".
  5. Si nada pasa: "fade_no_confirma" (se deja el número igualmente,
     para que quede transparente qué se probó).

Salida: data/shadow/fade_regimen_arquetipoA.json, una entrada por
combo con todos los números (n, hit, pnl, wilson90lo, breakeven,
split_half, p_binomial, veredicto, filtro_usado).

Puramente análisis/observación -- no toca prob_yes, stake ni
pares_permitidos_live. El vigía (vigia_fade_regimen_arquetipoA.py)
re-corre esto a diario y avisa por Telegram solo veredictos NUEVOS.
"""
import csv
import json
import math
import sys
from collections import defaultdict
from math import comb
from pathlib import Path

csv.field_size_limit(sys.maxsize)

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from libro_snapshots_prioridad import prio  # noqa: E402

LIBRO_PATH = REPO / "data/live/libro_snapshots.csv"
RESULTS_PATH = REPO / "data/shadow/results.csv"
FADE_PATH = REPO / "data/shadow/fade_depth_universal_fase0.csv"
OUT_PATH = REPO / "data/shadow/fade_regimen_arquetipoA.json"

STAKE = 1.05
FEE = 0.07
N_MIN = 15
RATIO_MIN = 5.0
Z90 = 1.645


def wilson_lo(p: float, n: int, z: float = Z90) -> float:
    if n == 0:
        return 0.0
    denom = 1 + z * z / n
    center = p + z * z / (2 * n)
    adj = z * math.sqrt(max(p * (1 - p) / n, 0) + z * z / (4 * n * n))
    return (center - adj) / denom


def binom_sf(k: int, n: int, p: float) -> float:
    p = min(max(p, 1e-9), 1 - 1e-9)
    return sum(comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))


def payout_win(precio: float) -> float:
    """pnl si gana, precio = ask pagado, fee 7% sobre la ganancia bruta."""
    return STAKE * (1 - precio) / precio - STAKE * FEE * (1 - precio)


def split_half(items: list, ts_key) -> tuple:
    items_sorted = sorted(items, key=ts_key)
    n = len(items_sorted)
    half = n // 2
    if half == 0:
        return None, None
    m1 = sum(x[1] for x in items_sorted[:half]) / half
    m2 = sum(x[1] for x in items_sorted[half:]) / (n - half)
    return m1, m2


def cargar_fade_rows() -> dict:
    """(strategy,subtype,direction) -> lista de filas dict."""
    grupos = defaultdict(list)
    with open(FADE_PATH) as f:
        r = csv.DictReader(f)
        for row in r:
            key = (row["strategy"], row["subtype"], row["direction"])
            grupos[key].append(row)
    return grupos


def cargar_libro_collapsado(strategies_interes: set) -> dict:
    """(strategy,subtype,direction) -> {market_id: (ratio_vs_stake, motivo)}"""
    best = {}
    with open(LIBRO_PATH) as f:
        r = csv.DictReader(f)
        for row in r:
            if row["strategy"] not in strategies_interes:
                continue
            key = (row["strategy"], row["subtype"], row["direction"])
            mid = row["market_id"]
            p = prio(row["motivo"])
            cur = best.get((key, mid))
            if cur is None or p < cur[0]:
                best[(key, mid)] = (p, row)
    out = defaultdict(dict)
    for (key, mid), (p, row) in best.items():
        try:
            ratio = float(row["ratio_vs_stake"])
        except (TypeError, ValueError):
            ratio = 0.0
        out[key][mid] = ratio
    return out


def cargar_results(strategies_interes: set) -> dict:
    """(strategy,subtype,decision) -> {market_id: (acierto, pnl_neto, features_dict)}"""
    out = defaultdict(dict)
    with open(RESULTS_PATH) as f:
        r = csv.DictReader(f)
        for row in r:
            if row["strategy"] not in strategies_interes:
                continue
            acierto = row.get("acierto")
            pnl = row.get("pnl_neto")
            if acierto in ("", None) or pnl in ("", None):
                continue
            key = (row["strategy"], row["subtype"], row["decision"])
            try:
                feat = json.loads(row["features"]) if row["features"] else {}
            except Exception:
                feat = {}
            out[key][row["market_id"]] = (int(float(acierto)), float(pnl), feat)
    return out


FILTROS = [
    ("ballenas_dentro_banda=False",
     lambda f: f.get("ballenas_dentro_banda") in (False, "False", "false", 0, None)
     and "ballenas_dentro_banda" in f),
    ("smart_money_consensus>0",
     lambda f: (f.get("smart_money_consensus") or 0) > 0),
    ("hora_utc[8,16)",
     lambda f: 8 <= f.get("hora_utc", 99) < 16),
]


def evaluar_grupo(fade_rows: list, res_orig: dict) -> dict | None:
    """Evalúa fade real (sin filtro) sobre fade_rows ya filtrados a
    ratio_contrario_min>=RATIO_MIN. Devuelve stats o None si n<N_MIN."""
    items = []
    for row in fade_rows:
        mid = row["market_id"]
        if mid not in res_orig:
            continue
        acierto_orig, _pnl_orig, feat = res_orig[mid]
        try:
            p_fade = float(row["precio_contrario"])
        except (TypeError, ValueError):
            continue
        acierto_fade = 1 - acierto_orig
        pnl_fade = payout_win(p_fade) if acierto_fade == 1 else -STAKE
        items.append((acierto_fade, pnl_fade, p_fade, row["evento_timestamp_utc"], feat))
    n = len(items)
    if n < N_MIN:
        return {"n": n, "veredicto": "n_insuficiente"}
    hit = sum(x[0] for x in items) / n
    pnl_medio = sum(x[1] for x in items) / n
    ask_medio = sum(x[2] for x in items) / n
    breakeven = ask_medio
    wlo = wilson_lo(hit, n)
    k = sum(x[0] for x in items)
    p_binom = binom_sf(k, n, breakeven)
    m1, m2 = split_half([(x[3], x[1]) for x in items], lambda x: x[0])
    pasa = wlo > breakeven and p_binom < 0.05 and m1 is not None and m1 > 0 and m2 > 0
    return {
        "n": n, "hit": round(hit, 4), "pnl_medio": round(pnl_medio, 4),
        "ask_medio": round(ask_medio, 4), "breakeven": round(breakeven, 4),
        "wilson90lo": round(wlo, 4), "p_binomial": round(p_binom, 4),
        "split_half": [round(m1, 4), round(m2, 4)] if m1 is not None else None,
        "pasa_rigor": pasa,
        "_items": items,
    }


def main() -> int:
    print("Cargando fade_depth_universal_fase0.csv...")
    fade_grupos = cargar_fade_rows()
    strategies = {k[0] for k in fade_grupos}
    print(f"  {len(fade_grupos)} combos, {len(strategies)} estrategias distintas")

    print("Cargando libro_snapshots.csv (colapsado)...")
    libro = cargar_libro_collapsado(strategies)

    print("Cargando results.csv (puede tardar)...")
    resultados = cargar_results(strategies)

    salida = {}
    n_negativos = 0
    n_fade_confirmado = 0
    for (strategy, subtype, direction), fade_rows in fade_grupos.items():
        decision = direction
        key_orig = (strategy, subtype, decision)
        res_orig = resultados.get(key_orig, {})
        libro_key = (strategy, subtype, direction)
        ratios = libro.get(libro_key, {})

        # 1. fill-ability real del lado ORIGINAL
        orig_items = []
        for mid, ratio in ratios.items():
            if ratio < RATIO_MIN:
                continue
            if mid not in res_orig:
                continue
            acierto, pnl, _feat = res_orig[mid]
            orig_items.append((acierto, pnl))
        n_orig = len(orig_items)
        tupla_str = f"{strategy}#{subtype}#{decision}"

        if n_orig < N_MIN:
            salida[tupla_str] = {"original": {"n": n_orig, "veredicto": "n_insuficiente"}}
            continue
        hit_orig = sum(x[0] for x in orig_items) / n_orig
        pnl_orig = sum(x[1] for x in orig_items) / n_orig
        original_stats = {"n": n_orig, "hit": round(hit_orig, 4), "pnl_medio": round(pnl_orig, 4)}

        if pnl_orig >= 0:
            salida[tupla_str] = {"original": {**original_stats, "veredicto": "original_ya_positivo_no_aplica"}}
            continue

        n_negativos += 1

        # 2. fade real, filtrando ratio_contrario_min>=RATIO_MIN
        fade_rows_fillable = []
        for row in fade_rows:
            try:
                ratio_min_contrario = float(row["ratio_contrario_min"])
            except (TypeError, ValueError):
                continue
            if ratio_min_contrario < RATIO_MIN:
                continue
            fade_rows_fillable.append(row)

        base = evaluar_grupo(fade_rows_fillable, res_orig)
        entrada = {"original": {**original_stats, "veredicto": "negativo_candidata_fade"}}

        if base is None or base.get("veredicto") == "n_insuficiente":
            entrada["fade_sin_filtro"] = {"n": base["n"] if base else 0, "veredicto": "n_insuficiente"}
            salida[tupla_str] = entrada
            continue

        base_items = base.pop("_items")
        entrada["fade_sin_filtro"] = base

        if base["pasa_rigor"]:
            entrada["veredicto_final"] = "fade_confirmado_sin_filtro"
            n_fade_confirmado += 1
            salida[tupla_str] = entrada
            continue

        # 3. probar filtros individuales (nunca combinados)
        veredicto_final = "fade_no_confirma"
        filtros_probados = {}
        for nombre, fn in FILTROS:
            sub_items = [x for x in base_items if fn(x[4])]
            n_f = len(sub_items)
            if n_f < N_MIN:
                filtros_probados[nombre] = {"n": n_f, "veredicto": "n_insuficiente"}
                continue
            hit_f = sum(x[0] for x in sub_items) / n_f
            pnl_f = sum(x[1] for x in sub_items) / n_f
            ask_f = sum(x[2] for x in sub_items) / n_f
            wlo_f = wilson_lo(hit_f, n_f)
            k_f = sum(x[0] for x in sub_items)
            p_f = binom_sf(k_f, n_f, ask_f)
            m1_f, m2_f = split_half([(x[3], x[1]) for x in sub_items], lambda x: x[0])
            pasa_f = wlo_f > ask_f and p_f < 0.05 and m1_f is not None and m1_f > 0 and m2_f > 0
            filtros_probados[nombre] = {
                "n": n_f, "hit": round(hit_f, 4), "pnl_medio": round(pnl_f, 4),
                "wilson90lo": round(wlo_f, 4), "breakeven": round(ask_f, 4),
                "p_binomial": round(p_f, 4),
                "split_half": [round(m1_f, 4), round(m2_f, 4)] if m1_f is not None else None,
                "pasa_rigor": pasa_f,
            }
            if pasa_f and veredicto_final == "fade_no_confirma":
                veredicto_final = f"fade_confirmado_con_filtro:{nombre}"
                n_fade_confirmado += 1

        entrada["filtros_regimen"] = filtros_probados
        entrada["veredicto_final"] = veredicto_final
        salida[tupla_str] = entrada

    OUT_PATH.write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nCombos totales: {len(salida)}")
    print(f"Candidatas negativas con fade evaluado: {n_negativos}")
    print(f"Fade confirmado (con o sin filtro): {n_fade_confirmado}")
    print(f"Guardado en {OUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
