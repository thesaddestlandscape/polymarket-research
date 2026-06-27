#!/usr/bin/env python3
"""
hypothesis_tracker.py — Evaluador automático de hipótesis pendientes

Evalúa todas las hipótesis con datos reales de results.csv.
Escribe data/shadow/hipotesis_pendientes.json y genera sección para hipotesis_auto.md.
Llamado por shadow_postmortem.py en cada ciclo.

Hipótesis pendientes conectadas al sistema:
  H-GBM-18H      Bloquear hora 18h UTC en GBM (n≥15)
  H-IBS-15       IBS-15 mean-reversion feature (n≥40 forward)
  H-HORA-GBM     hora_utc causal automático en GBM (n≥20 forward)
  H-CROSS-ASSET  GBM+OF BUY_NO mismo activo → boost (n_overlaps≥20)
  H-OF-PAR       ORDER_FLOW per-pair delta ranges (n≥200 BTC+SOL)
  H-KELLY-HORA   Boost ×1.2 en horas top 15/17/19h (n≥40 por hora)
  H-60MIN-LIVE   BTC/ETH#60min → live cuando IC≥0.08 n≥40
  H-WEEKLY       Predicciones semanales por par (n≥15 por par)
  H-SOL-15MIN    SOL#15min → live cuando IC≥0.08 n≥40
  H-OBI          Orderbook Imbalance [BLOQUEADA Jon-Becker]
  H-OU-THETA     Calibrar theta OU [BLOQUEADA Jon-Becker]
  H-HMM-REGIME   Régimen de mercado con HMM [BLOQUEADA Jon-Becker]
  H-KALMAN       Kalman filter drift [BLOQUEADA n<200 por subtipo]
  H-CROSS-ARB    Arb Polymarket vs Kalshi [BLOQUEADA API Kalshi]
"""
import csv
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO             = Path(__file__).parent
RESULTS_CSV      = REPO / "data/shadow/results.csv"
STRATEGY_PARAMS  = REPO / "data/shadow/strategy_params.json"
HIPOTESIS_JSON   = REPO / "data/shadow/hipotesis_pendientes.json"
JON_BECKER_DIR   = REPO / "data/jon_becker"

# ── Utilidades ────────────────────────────────────────────────────────────────

def _ic(wins, n):
    if n == 0:
        return 0.0
    return ((wins + 1) / (n + 2) - 0.5) * min(1.0, n / 20)


def _feat(row, key):
    try:
        return json.loads(row.get("features", "{}") or "{}").get(key)
    except Exception:
        return None


def _pnl(r):
    try:
        return float(r.get("pnl_neto", 0) or 0)
    except Exception:
        return 0.0


def _win(r):
    try:
        return int(r.get("acierto", 0) or 0)
    except Exception:
        return 0


def _stats(rows):
    n = len(rows)
    wins = sum(_win(r) for r in rows)
    pnl = sum(_pnl(r) for r in rows)
    return {"n": n, "wins": wins, "ic": round(_ic(wins, n), 4), "pnl": round(pnl, 2)}


def _hour_from_ts(r):
    ts = r.get("resolution_timestamp", "")
    try:
        return int(ts[11:13]) if len(ts) >= 13 else None
    except Exception:
        return None


def _load_results():
    if not RESULTS_CSV.exists():
        return []
    return list(csv.DictReader(open(RESULTS_CSV, encoding="utf-8")))


def _jon_becker_disponible():
    return JON_BECKER_DIR.exists() and any(JON_BECKER_DIR.iterdir())


# ── Evaluadores ───────────────────────────────────────────────────────────────

def _eval_gbm_18h(rows):
    """Bloquear hora 18h UTC en GBM. Trigger: n≥15 con IC<-0.05."""
    gbm_18h = []
    for r in rows:
        if not r.get("strategy", "").startswith("UPDOWN_GBM"):
            continue
        h = _feat(r, "hora_utc")
        if h is None:
            h = _hour_from_ts(r)
        if h == 18:
            gbm_18h.append(r)

    s = _stats(gbm_18h)
    if s["n"] < 15:
        return {**s, "status": "ACUMULANDO", "umbral": 15,
                "rec": f"Falta {15 - s['n']} ops más en GBM@18h (IC actual={s['ic']:+.3f})"}
    if s["ic"] < -0.05:
        return {**s, "status": "LISTA_IMPLEMENTAR",
                "rec": f"Confirma: IC={s['ic']:+.3f} n={s['n']} PNL={s['pnl']:+.2f}€ → añadir 18 a GBM_BLACKLIST_HOURS"}
    return {**s, "status": "NO_JUSTIFICADA",
            "rec": f"IC={s['ic']:+.3f} n={s['n']} — no justifica filtro, seguir monitorizando"}


def _eval_ibs15(rows):
    """IBS-15 mean-reversion feature. Solo forward data (feature añadida 2026-06-27)."""
    ibs_rows = [r for r in rows if _feat(r, "ibs_15") is not None]
    s = _stats(ibs_rows)

    if s["n"] < 15:
        return {**s, "status": "ACUMULANDO", "umbral": 40,
                "rec": f"Solo {s['n']} ops con ibs_15 (feature añadida 2026-06-27). Esperar n≥40."}

    def bucket(lo, hi):
        sub = [r for r in ibs_rows if lo <= (_feat(r, "ibs_15") or -1) < hi]
        return _stats(sub)

    b = {
        "oversold":   bucket(0.0,  0.30),
        "neutral":    bucket(0.30, 0.70),
        "overbought": bucket(0.70, 1.01),
    }
    ics = [v["ic"] for v in b.values()]
    spread = max(ics) - min(ics)

    best  = max(b, key=lambda k: b[k]["ic"])
    worst = min(b, key=lambda k: b[k]["ic"])

    summary = (f"oversold(IBS<0.3): IC={b['oversold']['ic']:+.3f} n={b['oversold']['n']} | "
               f"neutral: IC={b['neutral']['ic']:+.3f} n={b['neutral']['n']} | "
               f"overbought(IBS>0.7): IC={b['overbought']['ic']:+.3f} n={b['overbought']['n']}")

    if s["n"] >= 40 and spread > 0.15:
        status = "LISTA_EVALUAR"
        rec = f"Spread={spread:.3f}: {best}→boost, {worst}→filtro | {summary}"
    elif s["n"] >= 40:
        status = "SEÑAL_DEBIL"
        rec = f"Spread bajo ({spread:.3f}) — sin ventaja clara. {summary}"
    else:
        status = "ACUMULANDO"
        rec = f"{s['n']}/40 ops con ibs_15. {summary}"

    return {**s, "status": status, "rec": rec, "buckets": b}


def _eval_hora_gbm(rows):
    """hora_utc como feature causal en GBM forward data."""
    gbm_rows = [r for r in rows
                if r.get("strategy", "").startswith("UPDOWN_GBM")
                and _feat(r, "hora_utc") is not None]

    if len(gbm_rows) < 20:
        return {"n": len(gbm_rows), "status": "ACUMULANDO", "umbral": 20,
                "rec": f"Solo {len(gbm_rows)} ops GBM con hora_utc en features. Esperar n≥20 para patrones."}

    by_hour = defaultdict(list)
    for r in gbm_rows:
        h = _feat(r, "hora_utc")
        if h is not None:
            by_hour[int(h)].append(r)

    actionable = []
    for h in sorted(by_hour):
        s = _stats(by_hour[h])
        if s["n"] >= 15:
            if s["ic"] < -0.10:
                actionable.append(f"H={h:02d}h: IC={s['ic']:+.3f} n={s['n']} PNL={s['pnl']:+.2f}€ → FILTRAR")
            elif s["ic"] > +0.10:
                actionable.append(f"H={h:02d}h: IC={s['ic']:+.3f} n={s['n']} PNL={s['pnl']:+.2f}€ → BOOST")

    by_hour_summary = {str(h): _stats(v) for h, v in by_hour.items() if len(v) >= 5}

    if actionable:
        return {"n": len(gbm_rows), "status": "LISTA_EVALUAR",
                "by_hour": by_hour_summary,
                "rec": " | ".join(actionable)}

    return {"n": len(gbm_rows), "status": "ACUMULANDO",
            "by_hour": by_hour_summary,
            "rec": f"{len(gbm_rows)} ops, {len(by_hour)} horas distintas. Sin hora con n≥15 y IC extremo aún."}


def _eval_cross_asset(rows):
    """GBM BUY_NO + OF BUY_NO mismo activo en misma ventana horaria → boost ×1.5."""
    ASSETS = ["BTC", "ETH", "SOL"]

    by_key = defaultdict(lambda: {"gbm": [], "of": []})
    for r in rows:
        strat = r.get("strategy", "")
        sub   = r.get("subtype", "")
        dec   = r.get("decision", "")
        if dec != "BUY_NO":
            continue

        asset = next((a for a in ASSETS if a in sub), None)
        if not asset:
            continue

        ts = r.get("resolution_timestamp", "")
        hour_key = ts[:13]  # "YYYY-MM-DDTHH"
        if not hour_key:
            continue

        key = (asset, hour_key)
        if strat.startswith("UPDOWN_GBM"):
            by_key[key]["gbm"].append(r)
        elif strat == "ORDER_FLOW_5M":
            by_key[key]["of"].append(r)

    overlaps = [(k, v) for k, v in by_key.items() if v["gbm"] and v["of"]]
    n_overlaps = len(overlaps)

    if n_overlaps < 10:
        return {"n_overlaps": n_overlaps, "status": "ACUMULANDO", "umbral": 20,
                "rec": f"Solo {n_overlaps} ventanas con GBM+OF BUY_NO mismo activo. Necesita n≥20."}

    overlap_rows = []
    for _, v in overlaps:
        overlap_rows.extend(v["gbm"])
        overlap_rows.extend(v["of"])

    s_overlap = _stats(overlap_rows)
    all_buyno  = [r for r in rows if r.get("decision") == "BUY_NO"]
    s_base     = _stats(all_buyno)
    boost      = round(s_overlap["ic"] - s_base["ic"], 4)

    if boost > 0.05 and n_overlaps >= 20:
        status = "LISTA_EVALUAR"
        rec = (f"Cross-asset boost={boost:+.3f}: IC_overlap={s_overlap['ic']:+.3f} vs "
               f"IC_base={s_base['ic']:+.3f} (n_overlaps={n_overlaps})")
    else:
        status = "ACUMULANDO"
        rec = (f"n_overlaps={n_overlaps}, boost estimado={boost:+.3f}. "
               f"Necesita {max(0, 20-n_overlaps)} más y boost>0.05")

    return {"n_overlaps": n_overlaps, "ic_overlap": s_overlap["ic"],
            "ic_base": s_base["ic"], "boost_estimado": boost,
            "status": status, "rec": rec}


def _eval_of_rangos_par(rows):
    """ORDER_FLOW per-pair delta ranges. Backfill: BTC 0.42-0.44, SOL 0.36-0.40."""
    PAIRS = ["BTC", "SOL"]
    by_pair = {}

    for pair in PAIRS:
        pair_rows = [r for r in rows
                     if r.get("strategy") == "ORDER_FLOW_5M"
                     and pair in r.get("subtype", "")
                     and r.get("decision") == "BUY_NO"]
        with_delta = [r for r in pair_rows if _feat(r, "delta_ratio") is not None]
        s_all = _stats(pair_rows)

        if len(with_delta) >= 50:
            def range_ic(lo, hi, rows_d):
                sub = [r for r in rows_d if lo <= abs(_feat(r, "delta_ratio") or 0) < hi]
                return {**_stats(sub), "rango": f"[{lo:.2f},{hi:.2f})"}

            ranges = [
                range_ic(0.38, 0.41, with_delta),
                range_ic(0.41, 0.44, with_delta),
                range_ic(0.44, 0.46, with_delta),
            ]
            by_pair[pair] = {
                **s_all,
                "n_with_delta": len(with_delta),
                "ranges": ranges,
                "status": "LISTA_EVALUAR" if len(with_delta) >= 100 else "ACUMULANDO",
                "rec": f"{pair}: {len(with_delta)} ops con delta_ratio",
            }
        else:
            by_pair[pair] = {
                **s_all,
                "n_with_delta": len(with_delta),
                "status": "ACUMULANDO",
                "rec": f"{pair}: {len(with_delta)}/50 ops con delta_ratio feature",
            }

    min_nd = min(v.get("n_with_delta", 0) for v in by_pair.values()) if by_pair else 0
    overall = "LISTA_EVALUAR" if min_nd >= 100 else "ACUMULANDO"
    recs = " | ".join(v["rec"] for v in by_pair.values())

    return {"by_pair": by_pair, "status": overall, "rec": recs}


def _eval_kelly_hora(rows):
    """Boost ×1.2 en horas top (UTC 13/15/17/19). Trigger: n≥40 por hora con IC≥+0.10."""
    TARGET_HOURS = [13, 15, 17, 19]  # UTC → Madrid CEST +2 = 15/17/19/21h

    hourly = defaultdict(list)
    for r in rows:
        h = _hour_from_ts(r)
        if h is not None:
            hourly[h].append(r)

    by_hour = {}
    for h in TARGET_HOURS:
        s = _stats(hourly[h])
        ready = s["n"] >= 40 and s["ic"] >= 0.10
        by_hour[str(h)] = {
            **s,
            "status": "LISTA_EVALUAR" if ready else "ACUMULANDO",
            "rec": f"H={h:02d}h UTC: IC={s['ic']:+.3f} n={s['n']}/40 PNL={s['pnl']:+.2f}€",
        }

    all_ready = all(v["status"] == "LISTA_EVALUAR" for v in by_hour.values())

    return {"by_hour": by_hour,
            "status": "LISTA_EVALUAR" if all_ready else "ACUMULANDO",
            "rec": " | ".join(v["rec"] for v in by_hour.values())}


def _eval_60min_live(rows):
    """BTC/ETH/SOL 60min → live cuando IC≥0.08 n≥40."""
    by_sub = defaultdict(list)
    for r in rows:
        if not r.get("strategy", "").startswith("UPDOWN_GBM"):
            continue
        sub = r.get("subtype", "")
        if "60min" not in sub:
            continue
        by_sub[sub].append(r)

    by_subtype = {}
    for key, krows in by_sub.items():
        s = _stats(krows)
        if s["n"] >= 40 and s["ic"] >= 0.08:
            status = "LISTA_LIVE"
        elif s["n"] >= 40:
            status = "N_ALCANZADO_IC_BAJO"
        else:
            status = "ACUMULANDO"
        by_subtype[key] = {
            **s,
            "eta_n": max(0, 40 - s["n"]),
            "status": status,
            "rec": f"{key}: n={s['n']}/40 IC={s['ic']:+.3f} PNL={s['pnl']:+.2f}€",
        }

    listas = [k for k, v in by_subtype.items() if v["status"] == "LISTA_LIVE"]
    overall = "LISTA_LIVE" if listas else "ACUMULANDO"

    return {"by_subtype": by_subtype, "listas_live": listas,
            "status": overall,
            "rec": " | ".join(v["rec"] for v in by_subtype.values()) or "Sin datos 60min"}


def _eval_sol_15min_live(rows):
    """SOL#15min → live cuando IC≥0.08 n≥40."""
    sol_rows = [r for r in rows
                if r.get("strategy", "").startswith("UPDOWN_GBM")
                and "SOL" in r.get("subtype", "")
                and "15min" in r.get("subtype", "")]
    s = _stats(sol_rows)

    if s["n"] >= 40 and s["ic"] >= 0.08:
        status = "LISTA_LIVE"
        rec = f"SOL#15min LISTA: IC={s['ic']:+.3f} n={s['n']} PNL={s['pnl']:+.2f}€"
    elif s["n"] >= 40:
        status = "N_ALCANZADO_IC_BAJO"
        rec = f"SOL#15min: n≥40 pero IC={s['ic']:+.3f} < 0.08 — monitorear"
    else:
        status = "ACUMULANDO"
        rec = f"SOL#15min: n={s['n']}/40 IC={s['ic']:+.3f} PNL={s['pnl']:+.2f}€ (ETA: {max(0,40-s['n'])} ops)"

    return {**s, "status": status, "rec": rec}


def _eval_weekly_price(rows):
    """WEEKLY_PRICE por par. Trigger: n≥15 por par con IC≥+0.05."""
    by_pair = defaultdict(list)
    for r in rows:
        if r.get("strategy") != "WEEKLY_PRICE":
            continue
        sub = r.get("subtype", "")
        for p in ["BTC", "ETH", "SOL", "XRP"]:
            if p in sub:
                by_pair[p].append(r)
                break

    results = {}
    for pair, prows in by_pair.items():
        s = _stats(prows)
        if s["n"] >= 15 and s["ic"] >= 0.05:
            status = "LISTA_EVALUAR"
        elif s["n"] >= 15:
            status = "NO_JUSTIFICADA"
        else:
            status = "ACUMULANDO"
        results[pair] = {**s, "status": status,
                         "rec": f"{pair}: n={s['n']}/15 IC={s['ic']:+.3f} PNL={s['pnl']:+.2f}€"}

    any_ready = any(v["status"] == "LISTA_EVALUAR" for v in results.values())
    n_total = sum(v["n"] for v in results.values())

    return {"by_pair": results, "n_total": n_total,
            "status": "LISTA_EVALUAR" if any_ready else "ACUMULANDO",
            "rec": " | ".join(v["rec"] for v in results.values()) or "Sin datos WEEKLY_PRICE"}


# ── Evaluadores hipótesis bloqueadas ─────────────────────────────────────────

def _eval_blocked_jon_becker(desc):
    if _jon_becker_disponible():
        return {"status": "DATASET_DISPONIBLE",
                "rec": f"Dataset Jon-Becker detectado en {JON_BECKER_DIR}. Implementar evaluación: {desc}"}
    return {"status": "BLOQUEADA_DATASET",
            "rec": f"Descargar github.com/Jon-Becker/prediction-market-analysis (36GB). {desc}"}


def _eval_kalman(rows):
    """Kalman filter para drift. Requiere n≥200 por subtipo para calibrar Q/R."""
    try:
        sp = json.loads(STRATEGY_PARAMS.read_text())
    except Exception:
        sp = {}
    estrats = sp.get("estrategias", {})

    # Ver cuántos subtypes han alcanzado n≥200
    n200 = {k: v.get("n", 0) for k, v in estrats.items()
            if v.get("n", 0) >= 200 and "UPDOWN_GBM" in k}

    if len(n200) >= 3:
        return {"status": "LISTA_EVALUAR", "subtypes_listos": list(n200.keys()),
                "rec": f"{len(n200)} subtypes con n≥200: {', '.join(list(n200)[:5])}"}

    n_actuales = {k: v.get("n", 0) for k, v in estrats.items() if "UPDOWN_GBM" in k}
    max_n = max(n_actuales.values(), default=0)
    return {"status": "ACUMULANDO", "max_n": max_n,
            "rec": f"Máximo n actual en GBM: {max_n}/200. Esperar 3+ subtypes con n≥200."}


# ── Definición de hipótesis ───────────────────────────────────────────────────

HIPOTESIS = [
    # ── Activas con datos ────────────────────────────────────────────────────
    {
        "id":          "H-GBM-18H",
        "nombre":      "Bloquear hora 18h UTC en GBM",
        "descripcion": "GBM@18h UTC: IC=-0.148 n=11. Con n≥15 confirmar o descartar.",
        "tipo":        "filtro",
        "umbral":      "n≥15 y IC<-0.05",
        "accion":      "Añadir 18 a GBM_BLACKLIST_HOURS en shadow_predict.py",
        "eval_fn":     _eval_gbm_18h,
    },
    {
        "id":          "H-IBS-15",
        "nombre":      "IBS-15 como señal de mean-reversion",
        "descripcion": "IBS<0.3→BUY_YES, IBS>0.7→BUY_NO: señal reversión en GBM. Feature añadida 2026-06-27.",
        "tipo":        "feature_causal",
        "umbral":      "n≥40 ops con ibs_15 en features y spread_IC>0.15 entre buckets",
        "accion":      "Añadir ibs_15 como boost/filtro en FEATURE_RULES de shadow_postmortem.py",
        "eval_fn":     _eval_ibs15,
    },
    {
        "id":          "H-HORA-GBM",
        "nombre":      "hora_utc causal automático en GBM (forward)",
        "descripcion": "El postmortem ya aprende hora_utc. Monitorear cuándo aparecen horas con IC extremo en forward data.",
        "tipo":        "feature_causal",
        "umbral":      "n≥20 forward con hora_utc + alguna hora con n≥15 IC<-0.10 o >+0.10",
        "accion":      "El sistema lo aplica automáticamente vía FEATURE_RULES. Verificar en strategy_params.json.",
        "eval_fn":     _eval_hora_gbm,
    },
    {
        "id":          "H-CROSS-ASSET",
        "nombre":      "Cross-asset confirmation GBM+OF BUY_NO",
        "descripcion": "GBM BUY_NO + OF BUY_NO mismo activo/ventana → boost ×1.5. 5 solapamientos actuales.",
        "tipo":        "kelly_compuesto",
        "umbral":      "n_overlaps≥20 y IC_overlap > IC_base + 0.05",
        "accion":      "Cambiar _aplicar_kelly_compuesto: match por activo, no market_id",
        "eval_fn":     _eval_cross_asset,
    },
    {
        "id":          "H-OF-PAR",
        "nombre":      "ORDER_FLOW per-pair delta_ratio ranges",
        "descripcion": "Backfill sugiere BTC 0.42-0.44, SOL 0.36-0.40 óptimos. Validar en shadow forward.",
        "tipo":        "filtro",
        "umbral":      "n≥200 por par con delta_ratio feature en shadow",
        "accion":      "Añadir DELTA_MIN/MAX por par dict en shadow_predict.py",
        "eval_fn":     _eval_of_rangos_par,
    },
    {
        "id":          "H-KELLY-HORA",
        "nombre":      "Kelly boost ×1.2 en horas top (15/17/19h UTC)",
        "descripcion": "Horas 15/17/19h UTC históricamente IC>+0.10. Boost en esas horas.",
        "tipo":        "kelly_boost",
        "umbral":      "n≥40 por hora con IC estable ≥+0.10 confirmado en forward",
        "accion":      "Añadir HORA_BOOST = {13: 1.2, 15: 1.2, 17: 1.2, 19: 1.2} en shadow_predict.py",
        "eval_fn":     _eval_kelly_hora,
    },
    {
        "id":          "H-60MIN-LIVE",
        "nombre":      "Estrategias 60min → umbral live (IC≥0.08 n≥40)",
        "descripcion": "BTC#60min IC=+0.135 n=20, ETH#60min n=22. Acumulando.",
        "tipo":        "live_threshold",
        "umbral":      "IC≥0.08 y n≥40 en cualquier subtipo 60min",
        "accion":      "Activar live cuando haya credenciales Polymarket API",
        "eval_fn":     _eval_60min_live,
    },
    {
        "id":          "H-SOL-15MIN",
        "nombre":      "SOL#15min → umbral live (IC≥0.08 n≥40)",
        "descripcion": "SOL#15min n=34 IC=+0.028. ETA hoy 27 Jun con 6 ops más.",
        "tipo":        "live_threshold",
        "umbral":      "IC≥0.08 y n≥40",
        "accion":      "Activar live cuando haya credenciales Polymarket API",
        "eval_fn":     _eval_sol_15min_live,
    },
    {
        "id":          "H-WEEKLY",
        "nombre":      "Predicciones semanales de precio por par",
        "descripcion": "SOL 4/4 (100%) pero n pequeño. BTC negativo. Esperar n≥15 por par.",
        "tipo":        "nueva_estrategia",
        "umbral":      "n≥15 por par con IC≥+0.05",
        "accion":      "Si confirma IC≥+0.10 n≥15 en SOL → considerar live semanal",
        "eval_fn":     _eval_weekly_price,
    },
    # ── Bloqueadas por dataset/API ────────────────────────────────────────────
    {
        "id":          "H-OBI",
        "nombre":      "Orderbook Imbalance como señal",
        "descripcion": "Bid/ask imbalance en CLOB de Polymarket como predictor de resolución.",
        "tipo":        "nueva_estrategia",
        "umbral":      "Dataset Jon-Becker + API CLOB con orderbook histórico",
        "accion":      "Implementar s_obi en shadow_predict.py usando L2 orderbook",
        "bloqueante":  "JON_BECKER_DATASET",
        "eval_fn":     lambda rows: _eval_blocked_jon_becker(
            "Analizar spread bid/ask e imbalance por mercado en 60min previos a resolución."),
    },
    {
        "id":          "H-OU-THETA",
        "nombre":      "Calibrar theta OU con datos históricos",
        "descripcion": "THETA_OU=30 actual es estimado. Jon-Becker permite calibrar mean-reversion real por par.",
        "tipo":        "calibracion",
        "umbral":      "Dataset Jon-Becker con series de precios históricos suficientes",
        "accion":      "Ajustar THETA_OU por par en strategy_params.json (BTC/ETH/SOL independientes)",
        "bloqueante":  "JON_BECKER_DATASET",
        "eval_fn":     lambda rows: _eval_blocked_jon_becker(
            "Fit OU sobre series históricas por par y estimar theta por MLE."),
    },
    {
        "id":          "H-HMM-REGIME",
        "nombre":      "HMM para régimen de mercado",
        "descripcion": "Detectar régimen (tendencial/lateral/volátil) con HMM sobre (drift_60min, sigma_h).",
        "tipo":        "nueva_estrategia",
        "umbral":      "n≥200 ops GBM forward con hora_utc/ibs_15, o dataset Jon-Becker",
        "accion":      "Implementar hmmlearn sobre features GBM; condicionar estrategia al régimen detectado",
        "bloqueante":  "JON_BECKER_DATASET",
        "eval_fn":     lambda rows: _eval_blocked_jon_becker(
            "Entrenar HMM 3-estado sobre (drift_60min, sigma_h) histórico. Validar en forward."),
    },
    {
        "id":          "H-KALMAN",
        "nombre":      "Kalman filter para drift adaptativo",
        "descripcion": "KF actualiza estimación de drift en tiempo real, reemplazando DRIFT_DAMPING estático.",
        "tipo":        "mejora_modelo",
        "umbral":      "n≥200 por subtipo para calibrar parámetros Q/R del KF",
        "accion":      "Sustituir DRIFT_DAMPING por KalmanDrift en fetch_binance_klines.py",
        "bloqueante":  "N_INSUFICIENTE",
        "eval_fn":     _eval_kalman,
    },
    {
        "id":          "H-CROSS-ARB",
        "nombre":      "Arbitraje Polymarket vs Kalshi",
        "descripcion": "Mismos eventos en ambas plataformas con spreads 2-5%. Requiere API Kalshi.",
        "tipo":        "nueva_estrategia",
        "umbral":      "API Kalshi activa + credenciales Polymarket live",
        "accion":      "Extender arb_scanner.py con endpoints Kalshi; comparar mismo evento cross-plataforma",
        "bloqueante":  "API_KALSHI",
        "eval_fn":     lambda rows: {"status": "BLOQUEADA_API",
                                     "rec": "Requiere acceso API Kalshi + credenciales Polymarket live"},
    },
]

# ── Iconos por estado ─────────────────────────────────────────────────────────

STATUS_ICON = {
    "LISTA_IMPLEMENTAR":    "🔴",
    "LISTA_EVALUAR":        "🟡",
    "LISTA_LIVE":           "🟢",
    "DATASET_DISPONIBLE":   "🟡",
    "N_ALCANZADO_IC_BAJO":  "⚠️",
    "SEÑAL_DEBIL":          "〰️",
    "NO_JUSTIFICADA":       "✅",
    "ACUMULANDO":           "⏳",
    "BLOQUEADA_DATASET":    "🔒",
    "BLOQUEADA_API":        "🔒",
    "ERROR":                "❌",
}


# ── Runner ────────────────────────────────────────────────────────────────────

def _auto_apply(resultados):
    """
    Para hipótesis con status LISTA_IMPLEMENTAR, aplica el cambio directamente
    en strategy_params.json bajo la clave 'meta', sin tocar código Python.
    shadow_predict.py lee 'meta' al inicio de cada ciclo.
    """
    if not STRATEGY_PARAMS.exists():
        return []

    try:
        sp = json.loads(STRATEGY_PARAMS.read_text())
    except Exception:
        return []

    meta = sp.setdefault("meta", {})
    aplicados = []

    # H-GBM-18H: bloquear hora 18 UTC en GBM
    h = resultados.get("H-GBM-18H", {})
    if h.get("status") == "LISTA_IMPLEMENTAR":
        blacklist = set(meta.get("gbm_blacklist_hours_auto", []))
        if 18 not in blacklist:
            blacklist.add(18)
            meta["gbm_blacklist_hours_auto"] = sorted(blacklist)
            meta["gbm_blacklist_hours_auto_motivo"] = (
                f"H-GBM-18H auto-aplicada: IC={h.get('ic',0):+.3f} n={h.get('n',0)}")
            aplicados.append("H-GBM-18H → hora 18 añadida a gbm_blacklist_hours_auto")

    # H-KELLY-HORA: boost por hora cuando IC≥0.15 y n≥40 confirmado
    h = resultados.get("H-KELLY-HORA", {})
    if h.get("status") == "LISTA_EVALUAR":
        hora_boost = {}
        for hora_str, d in h.get("by_hour", {}).items():
            if d.get("n", 0) >= 40 and d.get("ic", 0) >= 0.15:
                hora_boost[hora_str] = 1.2
        if hora_boost:
            meta["hora_boost_factor"] = hora_boost
            aplicados.append(f"H-KELLY-HORA → boost ×1.2 en horas {list(hora_boost.keys())}")

    if aplicados:
        sp["meta"] = meta
        STRATEGY_PARAMS.write_text(json.dumps(sp, indent=2, ensure_ascii=False))

    return aplicados


def run(rows=None):
    """Evalúa todas las hipótesis. Devuelve dict id→resultado y escribe JSON."""
    if rows is None:
        rows = _load_results()

    now = datetime.now(timezone.utc).isoformat(timespec="minutes")
    resultados = {}

    for h in HIPOTESIS:
        try:
            result = h["eval_fn"](rows)
        except Exception as e:
            result = {"status": "ERROR", "rec": str(e)}

        resultados[h["id"]] = {
            "nombre":    h["nombre"],
            "tipo":      h["tipo"],
            "umbral":    h["umbral"],
            "accion":    h["accion"],
            "bloqueante": h.get("bloqueante"),
            "actualizado": now,
            **result,
        }

    HIPOTESIS_JSON.write_text(json.dumps(resultados, indent=2, ensure_ascii=False))

    # Auto-apply cambios que ya superaron el umbral
    aplicados = _auto_apply(resultados)
    if aplicados:
        for msg in aplicados:
            print(f"  [AUTO-APPLY] {msg}")

    return resultados


def generate_markdown_section(resultados=None):
    """Genera la sección '## Hipótesis pendientes' para añadir a hipotesis_auto.md."""
    if resultados is None:
        if HIPOTESIS_JSON.exists():
            try:
                resultados = json.loads(HIPOTESIS_JSON.read_text())
            except Exception:
                return ""
        else:
            return ""

    # Agrupar por urgencia
    grupos = {
        "🔴 Listas para implementar YA": [],
        "🟢 Listas para live":           [],
        "🟡 Listas para evaluar":        [],
        "⏳ Acumulando datos":            [],
        "🔒 Bloqueadas (requieren dataset/API)": [],
    }

    for hid, d in resultados.items():
        s = d.get("status", "")
        if s == "LISTA_IMPLEMENTAR":
            grupos["🔴 Listas para implementar YA"].append((hid, d))
        elif s in ("LISTA_LIVE",):
            grupos["🟢 Listas para live"].append((hid, d))
        elif s in ("LISTA_EVALUAR", "N_ALCANZADO_IC_BAJO", "SEÑAL_DEBIL",
                   "NO_JUSTIFICADA", "DATASET_DISPONIBLE"):
            grupos["🟡 Listas para evaluar"].append((hid, d))
        elif s in ("BLOQUEADA_DATASET", "BLOQUEADA_API"):
            grupos["🔒 Bloqueadas (requieren dataset/API)"].append((hid, d))
        else:
            grupos["⏳ Acumulando datos"].append((hid, d))

    lines = ["\n## Hipótesis pendientes — tracking automático\n"]

    for grupo, items in grupos.items():
        if not items:
            continue
        lines.append(f"\n### {grupo}\n")
        for hid, d in items:
            icon = STATUS_ICON.get(d.get("status", ""), "❓")
            lines.append(f"**{icon} {hid}** — {d['nombre']}")
            lines.append(f"  - _Umbral_: {d.get('umbral', '')}")
            if d.get("accion"):
                lines.append(f"  - _Acción_: {d['accion']}")
            rec = d.get("rec", "")
            if rec:
                lines.append(f"  - _Estado_: {rec}")
            n   = d.get("n") or d.get("n_overlaps") or d.get("n_total")
            ic  = d.get("ic")
            pnl = d.get("pnl")
            if n is not None and ic is not None:
                extra = f" PNL={pnl:+.2f}€" if pnl is not None else ""
                lines.append(f"  - _Datos_: n={n} IC={ic:+.3f}{extra}")
            bl = d.get("bloqueante")
            if bl:
                lines.append(f"  - _Bloqueante_: {bl}")
            lines.append("")

    return "\n".join(lines)


if __name__ == "__main__":
    rows = _load_results()
    resultados = run(rows)
    print(generate_markdown_section(resultados))
    print(f"\n{len(resultados)} hipótesis evaluadas.")
    for hid, d in resultados.items():
        icon = STATUS_ICON.get(d.get("status", ""), "❓")
        print(f"  {icon} {hid}: {d['status']}")
