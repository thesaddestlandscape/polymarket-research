"""
shadow_postmortem.py — Diagnóstico automático de pérdidas + análisis de rendimiento.

Por cada pérdida nueva en results.csv:
1. Clasifica la causa
2. Calcula IC Bayesiano por estrategia desde la primera observación
3. Genera strategy_params.json → shadow_predict.py lo aplica en el siguiente ciclo
4. Genera performance.csv con métricas completas de trader por estrategia

Causas de pérdida:
  SPREAD_TRAP       — slippage implícito > 4%, el spread se comió el edge
  EDGE_INSUFICIENTE — edge neto < 3%, demasiado fino para ser real
  TIMING_CORTO      — mercado < 24h, perdimos por timing
  DIRECTION_ERROR   — dirección incorrecta del activo (el fallo principal)
"""
import csv
import json
import re
from datetime import datetime, timezone
from pathlib import Path

DIR_SHADOW      = Path("data/shadow")
RESULTS_PATH    = DIR_SHADOW / "results.csv"
POSTMORTEM_PATH = DIR_SHADOW / "postmortem.csv"
PARAMS_PATH     = DIR_SHADOW / "strategy_params.json"
PERFORMANCE_PATH = DIR_SHADOW / "performance.csv"

APUESTA_SHADOW = 0.90

UMBRAL_SUBIR_EDGE = (-0.10, 3)
UMBRAL_SUBIR_MAS  = (-0.20, 5)
UMBRAL_DESACTIVAR = (-0.20, 8)  # bajado de -0.30: desactiva antes estrategias con IC negativo claro


def cargar_results() -> list:
    if not RESULTS_PATH.exists():
        return []
    with open(RESULTS_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _verificar_integridad() -> list[str]:
    """Grader independiente: valida results.csv antes de que el postmortem lo procese."""
    alertas = []
    if not RESULTS_PATH.exists():
        return ["results.csv no existe"]
    content = RESULTS_PATH.read_text(encoding="utf-8")
    if any(m in content for m in ["<<<<<<<", ">>>>>>>", "======="]):
        alertas.append("CONFLICT MARKERS en results.csv — git rebase incompleto")
    rows = list(csv.DictReader(content.splitlines()))
    if rows:
        if "features" not in rows[0]:
            alertas.append("Falta columna 'features' en results.csv — fix urgente")
        bad = sum(1 for r in rows if r.get("pnl_neto") in (None, ""))
        if bad:
            alertas.append(f"{bad} filas con pnl_neto inválido")
    return alertas


def _monitor_5min(resultados: list) -> dict:
    """
    Monitor específico del mercado de 5 minutos.
    Tres señales bajo vigilancia:
      1. OU_5M: CLV y tendencia (¿THETA_OU=30 sigue siendo válido?)
      2. ORDER_FLOW BUY_YES: CLV rolling — umbral de desactivación en -0.030 con n≥400
      3. Alpha decay ORDER_FLOW: IC rolling últimas 30 vs histórico
    """
    alertas = []

    # 1. UPDOWN_OU_5M
    ou = [r for r in resultados if r.get("strategy") == "UPDOWN_OU_5M"]
    ou_clv = [float(r["clv"]) for r in ou if r.get("clv")]
    ou_state = {
        "n": len(ou),
        "clv": round(sum(ou_clv)/len(ou_clv), 4) if ou_clv else None,
        "clv_ult30": None,
    }
    if len(ou) >= 10:
        ult30 = sorted(ou, key=lambda r: r["resolution_timestamp"])[-30:]
        clv30 = [float(r["clv"]) for r in ult30 if r.get("clv")]
        ou_state["clv_ult30"] = round(sum(clv30)/len(clv30), 4) if clv30 else None

    # 2. ORDER_FLOW BUY_YES: umbral de desactivación
    of_yes = [r for r in resultados
              if r.get("strategy") == "ORDER_FLOW_5M" and r.get("decision") == "BUY_YES"
              and r.get("subtype","")]
    of_yes_clv = [float(r["clv"]) for r in of_yes if r.get("clv")]
    of_yes_state = {
        "n": len(of_yes),
        "clv": round(sum(of_yes_clv)/len(of_yes_clv), 4) if of_yes_clv else None,
        "umbral_accion": -0.030,
        "n_umbral": 400,
    }
    if of_yes_clv:
        clv_m = sum(of_yes_clv)/len(of_yes_clv)
        if len(of_yes) >= 400 and clv_m < -0.030:
            alertas.append(f"🚨 ORDER_FLOW BUY_YES: CLV={clv_m:+.3f} con n={len(of_yes)} → DESACTIVAR BUY_YES")
        elif len(of_yes) >= 300:
            # Alerta temprana cuando se acerca al umbral
            of_yes_state["alerta_proxima"] = f"n={len(of_yes)}/400, CLV={clv_m:+.3f}/−0.030"

    # 3. Alpha decay ORDER_FLOW global (rolling 30 vs histórico)
    of_all = [r for r in resultados if r.get("strategy") == "ORDER_FLOW_5M" and r.get("subtype","")]
    of_clv_all = [float(r["clv"]) for r in of_all if r.get("clv")]
    of_clv_hist = sum(of_clv_all)/len(of_clv_all) if of_clv_all else 0
    ult30_of = sorted(of_all, key=lambda r: r["resolution_timestamp"])[-30:]
    of_clv_30 = [float(r["clv"]) for r in ult30_of if r.get("clv")]
    of_clv_30m = sum(of_clv_30)/len(of_clv_30) if of_clv_30 else 0
    decay_ratio = of_clv_30m / of_clv_hist if of_clv_hist > 0.005 else None

    of_state = {
        "clv_historico": round(of_clv_hist, 4),
        "clv_ult30":     round(of_clv_30m, 4),
        "decay_ratio":   round(decay_ratio, 2) if decay_ratio else None,
    }
    # Decay real = varias sesiones consecutivas negativas, no un único día malo.
    # Solo alertar si hay ops de al menos 2 días distintos en las últimas 30
    dias_distintos = len({r["resolution_timestamp"][:10] for r in ult30_of})
    if decay_ratio is not None and decay_ratio < 0.5 and dias_distintos >= 2:
        alertas.append(f"⚠️ ORDER_FLOW alpha decay: CLV histórico={of_clv_hist:+.3f} → últimas30={of_clv_30m:+.3f} (ratio={decay_ratio:.1f}x, {dias_distintos} días)")

    # Enviar alertas por Telegram si las hay
    if alertas:
        try:
            import os, requests
            tok = os.environ.get("TELEGRAM_TOKEN", "")
            cid = os.environ.get("TELEGRAM_CHAT_ID", "")
            if tok and cid:
                msg = "📊 *Monitor 5min — alerta*\n" + "\n".join(alertas)
                requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
                              json={"chat_id": cid, "text": msg, "parse_mode": "Markdown"},
                              timeout=10)
        except Exception:
            pass
    for a in alertas:
        print(f"  [5MIN ALERTA] {a}")

    return {"ou_5m": ou_state, "of_buy_yes": of_yes_state, "of_decay": of_state, "alertas": alertas}


def _escribir_state(params: dict, resultados: list):
    """Gap 2: state file machine-generated con snapshot del sistema."""
    estrategias = params.get("estrategias", {})
    activas      = {k: v for k, v in estrategias.items() if v.get("activa", True)}
    desactivadas = {k: v for k, v in estrategias.items() if not v.get("activa", True)}
    pnl_total    = sum(float(r.get("pnl_neto", 0)) for r in resultados)
    brier_vals   = [float(r["brier_score"]) for r in resultados if r.get("brier_score")]
    clv_vals     = [float(r["clv"])         for r in resultados if r.get("clv")]
    brier_mean   = round(sum(brier_vals)/len(brier_vals), 4) if brier_vals else None
    clv_mean     = round(sum(clv_vals)/len(clv_vals), 4)     if clv_vals  else None
    n_total      = len(resultados)
    wins         = sum(int(r.get("acierto", 0)) for r in resultados)
    top3         = sorted(activas.items(), key=lambda x: x[1].get("ic_bayes", 0), reverse=True)[:3]
    monitor_5m   = _monitor_5min(resultados)
    state = {
        "timestamp_utc":   datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "bankroll_sim":    round(20.0 + pnl_total, 2),
        "pnl_total":       round(pnl_total, 2),
        "n_ops":           n_total,
        "win_rate":        round(wins / n_total, 4) if n_total else 0,
        "estrategias_activas": len(activas),
        "desactivadas":    list(desactivadas.keys()),
        "top3_ic":         [{"k": k, "ic": round(v.get("ic_bayes", 0), 4), "n": v.get("n", 0)} for k, v in top3],
        "brier_medio":     brier_mean,
        "clv_medio":       clv_mean,
        "monitor_5min":    monitor_5m,
    }
    path = PARAMS_PATH.parent / "system_state.json"
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    return state


def _normalizar_pred(row: dict) -> dict:
    """Extrae subtype, apuesta y features del key None cuando el header es antiguo (13 cols)."""
    extra = row.pop(None, None)
    if isinstance(extra, list):
        for i, campo in enumerate(["subtype", "apuesta", "features"]):
            if i < len(extra) and extra[i] and not row.get(campo):
                row[campo] = extra[i]
    return row


def cargar_predicciones_index() -> dict:
    index = {}
    for arch in sorted(DIR_SHADOW.glob("predictions_*.csv")):
        with open(arch, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("decision") in ("BUY_YES", "BUY_NO"):
                    row = _normalizar_pred(row)
                    clave = (row["strategy"], row["market_id"], row["decision"])
                    if clave not in index:
                        index[clave] = row
    return index


def cargar_ya_postmortem() -> set:
    if not POSTMORTEM_PATH.exists():
        return set()
    with open(POSTMORTEM_PATH, encoding="utf-8") as f:
        return {(r["strategy"], r["market_id"], r["prediction_timestamp"])
                for r in csv.DictReader(f)}


def clasificar_causa(resultado: dict, pred: dict | None) -> str:
    strategy = resultado.get("strategy", "")
    subtype  = resultado.get("subtype", "") or (pred.get("subtype", "") if pred else "")

    if pred:
        try:
            eb = abs(float(pred.get("edge_bruto", 0)))
            en = abs(float(pred.get("edge_neto", 0)))
            if eb - en > 0.04:
                return "SPREAD_TRAP"
        except (ValueError, TypeError):
            pass
        try:
            if abs(float(pred.get("edge_neto", 0))) < 0.03:
                return "EDGE_INSUFICIENTE"
        except (ValueError, TypeError):
            pass

    # SLOT_OVERCONFIDENCE: modelo GBM da prob extrema en slots cortos
    # El mercado valora esos slots en ~0.50 → el edge aparente es ilusorio
    if strategy == "UPDOWN_GBM" and subtype and "min" in subtype:
        try:
            mins = int(subtype.replace("min", ""))
            prob = float(resultado.get("prob_yes_modelo", 0.5) or 0.5)
            if mins <= 10 and (prob > 0.75 or prob < 0.25):
                return "SLOT_OVERCONFIDENCE"
        except (ValueError, TypeError):
            pass

    # TIMING_CORTO: solo para estrategias que no están diseñadas para slots cortos
    if strategy not in ("UPDOWN_GBM", "PRICE_TARGET_GBM") and pred:
        try:
            if float(pred.get("horas_a_vencimiento", 999)) < 24:
                return "TIMING_CORTO"
        except (ValueError, TypeError):
            pass

    # DRIFT_ERROR: PRICE_TARGET_GBM asume drift=0; si el mercado hizo un movimiento
    # direccional sostenido grande (>5%) la hipótesis es incorrecta
    if strategy == "PRICE_TARGET_GBM":
        try:
            prob = float(resultado.get("prob_yes_modelo", 0.5) or 0.5)
            edge = abs(float(resultado.get("edge_direccional", 0) or 0))
            # edge alto + fallo = modelo muy seguro pero mercado tenía razón
            if edge > 0.15 and prob < 0.20:
                return "DRIFT_ERROR"  # modelo dijo ~0 pero ocurrió: drift alcista
            if edge > 0.15 and prob > 0.80:
                return "DRIFT_ERROR"  # modelo dijo ~1 pero no ocurrió: drift bajista
        except (ValueError, TypeError):
            pass

    return "DIRECTION_ERROR"


def calcular_params(resultados: list) -> dict:
    por_estrategia = {}
    for r in resultados:
        s = r["strategy"]
        subtype = r.get("subtype", "")
        # Generar todas las claves de agregación relevantes
        claves = [s]
        if "#" in subtype:
            a_part, d_part = subtype.split("#", 1)
            claves += [
                f"{s}#{subtype}",   # UPDOWN_GBM#BTC#15min  (más específico)
                f"{s}#{a_part}",    # UPDOWN_GBM#BTC         (nivel asset)
                f"{s}#{d_part}",    # UPDOWN_GBM#15min       (nivel duración)
            ]
        elif subtype:
            claves.append(f"{s}#{subtype}")   # WEEKLY_PRICE#BTC
        decision = r.get("decision", "")
        for clave in claves:
            if clave not in por_estrategia:
                por_estrategia[clave] = {"n": 0, "aciertos": 0, "pnl": 0.0, "causas": {}, "por_decision": {}}
            por_estrategia[clave]["n"] += 1
            por_estrategia[clave]["aciertos"] += int(r.get("acierto", 0))
            try:
                por_estrategia[clave]["pnl"] += float(r.get("pnl_neto", 0))
            except (ValueError, TypeError):
                pass
            causa = r.get("causa_perdida", "")
            if causa:
                por_estrategia[clave]["causas"][causa] = por_estrategia[clave]["causas"].get(causa, 0) + 1
            if decision in ("BUY_YES", "BUY_NO"):
                pd = por_estrategia[clave]["por_decision"]
                if decision not in pd:
                    pd[decision] = {"n": 0, "aciertos": 0, "pnl": 0.0}
                pd[decision]["n"] += 1
                pd[decision]["aciertos"] += int(r.get("acierto", 0))
                try:
                    pd[decision]["pnl"] += float(r.get("pnl_neto", 0))
                except (ValueError, TypeError):
                    pass

    params = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "estrategias": {},
    }

    for s, d in por_estrategia.items():
        n = d["n"]
        ic_bayes   = (d["aciertos"] + 1) / (n + 2) - 0.5
        confianza  = min(1.0, n / 20)
        ic_efectivo = round(ic_bayes * confianza, 4)

        activa      = True
        edge_minimo = 0.02
        motivo      = f"IC_bayes={ic_bayes:+.3f} n={n} conf={confianza:.2f}"
        causa_principal = max(d["causas"], key=d["causas"].get) if d["causas"] else ""

        if n >= UMBRAL_DESACTIVAR[1] and ic_bayes < UMBRAL_DESACTIVAR[0]:
            activa  = False
            motivo += " → DESACTIVADA"
        elif n >= UMBRAL_SUBIR_MAS[1] and ic_bayes < UMBRAL_SUBIR_MAS[0]:
            edge_minimo = 0.06
            motivo += " → edge_minimo=0.06"
        elif n >= UMBRAL_SUBIR_EDGE[1] and ic_bayes < UMBRAL_SUBIR_EDGE[0]:
            edge_minimo = 0.04
            motivo += " → edge_minimo=0.04"

        # Kelly simplificado: apuesta = 20€ * |ic_efectivo| * 0.5 (half-Kelly)
        # Mínimo 0.50€ (sin datos / IC negativo), máximo 2.00€ (10% del capital)
        # Sólo escala hacia arriba con IC positivo confirmado (n >= 5)
        if activa and n >= 5 and ic_efectivo > 0:
            apuesta_kelly = round(min(2.00, max(0.50, 20.0 * ic_efectivo * 0.5)), 2)
        else:
            apuesta_kelly = 0.50 if activa else 0.0

        entry = {
            "activa":          activa,
            "edge_minimo":     edge_minimo,
            "ic_bayes":        ic_efectivo,
            "n":               n,
            "pnl_total":       round(d["pnl"], 4),
            "causa_principal": causa_principal,
            "motivo":          motivo,
            "apuesta_kelly":   apuesta_kelly,
        }

        # Kelly por dirección (BUY_YES / BUY_NO separados)
        for dec_name, dec_d in d.get("por_decision", {}).items():
            dn = dec_d["n"]
            d_ic_b = (dec_d["aciertos"] + 1) / (dn + 2) - 0.5
            d_ic_e = round(d_ic_b * min(1.0, dn / 20), 4)
            if dn >= 5 and d_ic_e > 0:
                d_ap = round(min(2.00, max(0.50, 20.0 * d_ic_e * 0.5)), 2)
            else:
                d_ap = 0.50
            entry[f"n_{dec_name}"]               = dn
            entry[f"ic_{dec_name}"]              = d_ic_e
            entry[f"apuesta_kelly_{dec_name}"]   = d_ap

        params["estrategias"][s] = entry

    return params


def generar_performance(resultados: list, pred_index: dict) -> list:
    """
    Métricas completas de trader por estrategia:
    hit rate, expectancy, profit factor, Kelly, rachas, edge predicho vs real.
    """
    por_estrategia = {}

    for r in resultados:
        s = r["strategy"]
        if s not in por_estrategia:
            por_estrategia[s] = []

        acierto = int(r.get("acierto", 0))
        try:
            pnl = float(r.get("pnl_neto", 0))
        except (ValueError, TypeError):
            pnl = 0.0

        clave_pred = (r["strategy"], r["market_id"], r.get("decision", ""))
        pred = pred_index.get(clave_pred, {})
        try:
            edge_pred = float(pred.get("edge_neto", 0))
        except (ValueError, TypeError):
            edge_pred = 0.0
        try:
            horas = float(pred.get("horas_a_vencimiento", 0))
        except (ValueError, TypeError):
            horas = 0.0

        por_estrategia[s].append({
            "acierto":  acierto,
            "pnl":      pnl,
            "edge_pred": edge_pred,
            "horas":    horas,
            "causa":    r.get("causa_perdida", ""),
        })

    performance = []

    for s, ops in sorted(por_estrategia.items()):
        n        = len(ops)
        aciertos = sum(o["acierto"] for o in ops)
        fallos   = n - aciertos
        hit_rate = aciertos / n if n else 0.0

        pnls      = [o["pnl"] for o in ops]
        pnl_total = sum(pnls)
        pnl_medio = pnl_total / n if n else 0.0

        ganancias = [p for p in pnls if p > 0]
        perdidas  = [p for p in pnls if p < 0]
        avg_win   = sum(ganancias) / len(ganancias) if ganancias else 0.0
        avg_loss  = sum(perdidas)  / len(perdidas)  if perdidas  else 0.0

        expectancy    = hit_rate * avg_win + (1 - hit_rate) * avg_loss
        total_wins    = sum(ganancias)
        total_losses  = abs(sum(perdidas))
        profit_factor = (total_wins / total_losses) if total_losses > 0 else (99.0 if total_wins > 0 else 0.0)

        # Rachas
        mejor_racha = peor_racha = racha_pos = racha_neg = 0
        for o in ops:
            if o["acierto"]:
                racha_pos += 1
                racha_neg  = 0
                mejor_racha = max(mejor_racha, racha_pos)
            else:
                racha_neg += 1
                racha_pos  = 0
                peor_racha = max(peor_racha, racha_neg)

        # Horas promedio en ganadora vs perdedora
        hw = [o["horas"] for o in ops if o["acierto"] and o["horas"] > 0]
        hl = [o["horas"] for o in ops if not o["acierto"] and o["horas"] > 0]
        avg_horas_win  = sum(hw) / len(hw) if hw else 0.0
        avg_horas_loss = sum(hl) / len(hl) if hl else 0.0

        edges = [o["edge_pred"] for o in ops if o["edge_pred"] != 0]
        edge_medio_pred = sum(edges) / len(edges) if edges else 0.0
        edge_real       = pnl_medio / APUESTA_SHADOW if APUESTA_SHADOW else 0.0

        # IC Bayesiano
        ic_bayes    = (aciertos + 1) / (n + 2) - 0.5
        confianza   = min(1.0, n / 20)
        ic_efectivo = round(ic_bayes * confianza, 4)

        # Kelly fracción óptima
        if hit_rate > 0 and avg_loss < 0:
            b     = avg_win / abs(avg_loss)
            kelly = (hit_rate * b - (1 - hit_rate)) / b if b > 0 else 0.0
            kelly = max(0.0, min(0.40, kelly))
        else:
            kelly = 0.0

        # Causa de pérdida principal
        causas = {}
        for o in ops:
            c = o["causa"]
            if c:
                causas[c] = causas.get(c, 0) + 1
        causa_principal = max(causas, key=causas.get) if causas else ""

        performance.append({
            "strategy":            s,
            "n_total":             n,
            "n_aciertos":          aciertos,
            "n_fallos":            fallos,
            "hit_rate":            round(hit_rate, 4),
            "ic_bayes":            round(ic_bayes, 4),
            "confianza":           round(confianza, 4),
            "ic_efectivo":         ic_efectivo,
            "pnl_total":           round(pnl_total, 4),
            "pnl_medio":           round(pnl_medio, 4),
            "max_ganancia":        round(max(pnls), 4) if pnls else 0.0,
            "max_perdida":         round(min(pnls), 4) if pnls else 0.0,
            "avg_win":             round(avg_win,  4),
            "avg_loss":            round(avg_loss, 4),
            "expectancy":          round(expectancy, 4),
            "profit_factor":       round(min(profit_factor, 99.0), 4),
            "mejor_racha":         mejor_racha,
            "peor_racha":          peor_racha,
            "edge_medio_pred":     round(edge_medio_pred, 4),
            "edge_real":           round(edge_real, 4),
            "avg_horas_ganadora":  round(avg_horas_win,  1),
            "avg_horas_perdedora": round(avg_horas_loss, 1),
            "kelly_optimo":        round(kelly, 4),
            "causa_perdida_principal": causa_principal,
        })

    performance.sort(key=lambda x: x["pnl_total"], reverse=True)
    return performance


def _extraer_features(resultado: dict, pred: dict) -> dict:
    """
    Extrae features del momento de la predicción para análisis causal.
    Lee primero la columna 'features' (JSON estructurado, predicciones nuevas),
    luego parsea la cadena 'razon' como fallback para datos históricos.
    """
    features = {}

    # 1. Columna features (nueva, a partir de 2026-06-24)
    raw = resultado.get("features") or (pred or {}).get("features", "")
    if raw and raw != "{}":
        try:
            parsed = json.loads(raw) if isinstance(raw, str) else raw
            features.update({k: float(v) for k, v in parsed.items()
                             if v not in (None, "")})
        except (ValueError, TypeError, json.JSONDecodeError):
            pass

    # 2. Fallback: parsear razon string (datos históricos sin columna features)
    razon = (pred or {}).get("razon", "") if pred else ""
    if "pct_spot_vs_ref" not in features:
        m = re.search(r'\(([+-]\d+\.?\d*)%\)', razon)
        if m:
            try: features["pct_spot_vs_ref"] = float(m.group(1))
            except ValueError: pass
    if "sigma_h" not in features:
        m = re.search(r'sigma_h=(\d+\.?\d+)', razon)
        if m:
            try: features["sigma_h"] = float(m.group(1))
            except ValueError: pass
    if "delta_ratio" not in features:
        m = re.search(r'delta=([+-]\d+\.?\d+)', razon)
        if m:
            try: features["delta_ratio"] = float(m.group(1))
            except ValueError: pass

    return features


# Features a analizar y en qué dirección buscar el patrón
# (feature, condicion_mala, condicion_buena)
# condicion_mala: "abs_gt" = malo cuando |feature| > umbral (ej: pct_spot alto)
# condicion_buena: "abs_lt" = bueno cuando |feature| < umbral (ej: delta alto es bueno)
_BASE_GBM = [
    # ── Features de precio y volatilidad ──────────────────────────────────────
    # pct alto = precio ya movió mucho desde ref → el modelo sobreestima la señal
    ("pct_spot_vs_ref",  "abs_gt", "abs_lt"),
    # sigma alta = alta volatilidad → señales más ruidosas (varía por activo/ventana)
    ("sigma_h",          "gt",     "lt"),
    ("sigma_h",          "lt",     "gt"),    # algunas estrategias prefieren alta vol
    # ── Features de régimen / drift ────────────────────────────────────────────
    # drift fuerte en cualquier dirección → precio ya priceado en Polymarket
    ("drift_60min",      "abs_gt", "abs_lt"),
    ("drift_15min",      "abs_gt", "abs_lt"),
    # ── Order flow macro ───────────────────────────────────────────────────────
    ("delta_ratio_macro","abs_lt", "abs_gt"),
    # ── Temporal — hora UTC (0-23) ─────────────────────────────────────────────
    # El sistema aprende automáticamente qué horas son buenas/malas por estrategia
    ("hora_utc",         "lt",     "gt"),    # malo cuando hora < umbral (madrugada/mañana)
    ("hora_utc",         "gt",     "lt"),    # malo cuando hora > umbral (noche)
    # ── IBS-15 (Internal Bar Strength, últimas 15 velas 1min) ──────────────────
    # IBS>0.7: precio cerca del máximo → sobrecompra → refuerza BUY_NO
    # IBS<0.3: precio cerca del mínimo → sobreventa → refuerza BUY_YES
    # El postmortem descubrirá automáticamente qué umbral separa ganadores de perdedores
    ("ibs_15",           "gt",     "lt"),
    ("ibs_15",           "lt",     "gt"),
]

FEATURE_RULES = {
    # 5min: desactivadas manualmente, pero seguimos aprendiendo por si acaso se reactivan
    "UPDOWN_GBM#5min":     _BASE_GBM,
    "UPDOWN_GBM#BTC#5min": _BASE_GBM,
    "UPDOWN_GBM#ETH#5min": _BASE_GBM,
    "UPDOWN_GBM#SOL#5min": _BASE_GBM,
    # 15min: nuestras estrategias más activas
    "UPDOWN_GBM#15min":    _BASE_GBM,
    "UPDOWN_GBM#BTC#15min": _BASE_GBM,
    "UPDOWN_GBM#ETH#15min": _BASE_GBM,
    "UPDOWN_GBM#SOL#15min": _BASE_GBM,
    "UPDOWN_GBM#XRP#15min": _BASE_GBM,
    # 60min: candidatas a live con mejor IC — CRÍTICO tener aprendizaje aquí
    # En 60min sigma_h baja correlaciona con IC alto (H-60MIN confirmada en shadow)
    "UPDOWN_GBM#60min":    _BASE_GBM,
    "UPDOWN_GBM#BTC#60min": _BASE_GBM,
    "UPDOWN_GBM#ETH#60min": _BASE_GBM,
    "UPDOWN_GBM#SOL#60min": _BASE_GBM,
    # ORDER_FLOW: delta_ratio es la señal principal + hora
    "ORDER_FLOW_5M":       [("delta_ratio",        "abs_lt", "abs_gt"),
                            ("hora_utc",            "lt",     "gt"),
                            ("hora_utc",            "gt",     "lt")],
}

IC_FILTRO_MIN   = -0.12   # IC para activar filtro (evitar)
IC_PATRON_MIN   = +0.12   # IC para activar patrón ganador (amplificar)
N_BUCKET_MIN    = 15      # mínimo de observaciones en cualquier bucket (subido de 8: n<15 → demasiado ruidoso para kelly_boost)


def _evaluar_bucket(vals, umbral, condicion_mala):
    """Separa vals en [malo, bueno] según condicion_mala y umbral."""
    if condicion_mala == "abs_gt":
        malo  = [(r, v) for r, v in vals if abs(v) > umbral]
        bueno = [(r, v) for r, v in vals if abs(v) <= umbral]
        cond_buena = "abs_lt"
    elif condicion_mala == "gt":
        malo  = [(r, v) for r, v in vals if v > umbral]
        bueno = [(r, v) for r, v in vals if v <= umbral]
        cond_buena = "lt"
    elif condicion_mala == "lt":
        malo  = [(r, v) for r, v in vals if v < umbral]
        bueno = [(r, v) for r, v in vals if v >= umbral]
        cond_buena = "gt"
    else:
        malo, bueno, cond_buena = [], [], ""
    return malo, bueno, cond_buena


def aprender_patrones_causales(resultados: list, pred_index: dict) -> dict:
    """
    Aprende TANTO por qué el modelo pierde COMO por qué gana.

    Para cada estrategia/subtipo y feature relevante, busca el umbral que
    mejor separa ganadores de perdedores y genera:
      - filtros_causales: rangos de features donde siempre pierde → skip
      - patrones_ganadores: rangos de features donde gana consistentemente → boost kelly

    El aprendizaje es completamente automático y se actualiza cada ciclo.
    """
    ts_ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")
    resultado_final = {}

    for strat_key, feature_specs in FEATURE_RULES.items():
        datos = []
        for r in resultados:
            s   = r.get("strategy", "")
            sub = r.get("subtype", "")
            key = s + ("#" + sub if sub else "")
            if key != strat_key:
                continue
            clave_pred = (s, r.get("market_id", ""), r.get("decision", ""))
            pred  = pred_index.get(clave_pred)
            feats = _extraer_features(r, pred)
            if feats:
                datos.append((r, feats))

        if len(datos) < N_BUCKET_MIN:
            continue

        ic_base = ((sum(int(r.get("acierto", 0)) for r, _ in datos) + 1)
                   / (len(datos) + 2) - 0.5)

        filtros_strat  = []
        patrones_strat = []

        for feature, cond_mala, cond_buena in feature_specs:
            vals = [(r, f[feature]) for r, f in datos if feature in f]
            if len(vals) < N_BUCKET_MIN:
                continue

            # Probar percentiles como posibles umbrales de corte
            abs_vals = sorted(abs(v) for _, v in vals)
            percentiles = [0.25, 0.33, 0.50, 0.66, 0.75]

            mejor_filtro  = None
            mejor_patron  = None
            mejor_dif_filtro = 0.0
            mejor_dif_patron = 0.0

            for p in percentiles:
                idx = int(len(abs_vals) * p)
                umbral = abs_vals[idx] if idx < len(abs_vals) else None
                if umbral is None or umbral == 0:
                    continue

                malo, bueno, _ = _evaluar_bucket(vals, umbral, cond_mala)
                if len(malo) < N_BUCKET_MIN or len(bueno) < 3:
                    continue

                wins_malo  = sum(int(r.get("acierto", 0)) for r, _ in malo)
                wins_bueno = sum(int(r.get("acierto", 0)) for r, _ in bueno)
                ic_malo    = (wins_malo  + 1) / (len(malo)  + 2) - 0.5
                ic_bueno   = (wins_bueno + 1) / (len(bueno) + 2) - 0.5
                dif        = ic_bueno - ic_malo

                # ── Filtro: el bucket malo es suficientemente malo ──
                if ic_malo < IC_FILTRO_MIN and dif > mejor_dif_filtro:
                    mejor_dif_filtro = dif
                    mejor_filtro = {
                        "feature":    feature,
                        "condicion":  cond_mala,
                        "umbral":     round(umbral, 4),
                        "ic_malo":    round(ic_malo,  4),
                        "ic_bueno":   round(ic_bueno, 4),
                        "n_malo":     len(malo),
                        "n_bueno":    len(bueno),
                        "descubierto": ts_ahora,
                    }

                # ── Patrón ganador: el bucket bueno es suficientemente bueno ──
                if ic_bueno > IC_PATRON_MIN and len(bueno) >= N_BUCKET_MIN and dif > mejor_dif_patron:
                    # Kelly boost: cuánto apostar extra cuando esta condición se cumple
                    kelly_boost = round(min(1.00, max(0.10, 20.0 * ic_bueno * 0.25)), 2)
                    mejor_dif_patron = dif
                    mejor_patron = {
                        "feature":     feature,
                        "condicion":   cond_buena,
                        "umbral":      round(umbral, 4),
                        "ic_patron":   round(ic_bueno, 4),
                        "ic_base":     round(ic_base,  4),
                        "n_patron":    len(bueno),
                        "kelly_boost": kelly_boost,
                        "descubierto": ts_ahora,
                    }

            if mejor_filtro:
                filtros_strat.append(mejor_filtro)
            if mejor_patron:
                patrones_strat.append(mejor_patron)

        if filtros_strat or patrones_strat:
            resultado_final[strat_key] = {
                "filtros_causales":  filtros_strat,
                "patrones_ganadores": patrones_strat,
            }

    return resultado_final


def _generar_hipotesis_auto(params: dict, patrones: dict, resultados: list) -> None:
    """
    Traduce los patrones causales aprendidos a hipótesis accionables en markdown.
    Escribe data/shadow/hipotesis_auto.md — leída por el LLM nocturno y por el humano.

    Cada patrón descubierto se expresa como:
      - QUÉ condición predice éxito/fracaso
      - POR QUÉ (interpretación microestructural)
      - ACCIÓN sugerida (filtro, boost, nueva estrategia)
    """
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    n_total = len(resultados)
    pnl_total = sum(float(r.get("pnl_neto", 0)) for r in resultados)

    lineas = [
        f"# Hipótesis automáticas — {ts}",
        f"_Generado por shadow_postmortem.py sobre {n_total} resoluciones (PNL={pnl_total:+.2f}€)_",
        "",
        "## Patrones causales activos",
        "",
    ]

    # Interpretaciones microestructurales por feature
    INTERPRETACIONES = {
        "sigma_h": {
            "gt":    "alta volatilidad → el modelo GBM sobreestima la señal; el mercado es más aleatorio",
            "lt":    "baja volatilidad → señal GBM más fiable; el spread de Polymarket cubre mejor el edge",
            "abs_gt":"alta volatilidad en cualquier dirección → señal contaminada por ruido",
        },
        "drift_60min": {
            "abs_gt":"drift fuerte en 1h → el movimiento ya está priceado en Polymarket; edge agotado",
            "abs_lt":"drift moderado → precio aún no ha reaccionado del todo; lag explotable",
        },
        "drift_15min": {
            "abs_gt":"drift fuerte en 15min → momentum reciente ya en el precio Polymarket",
        },
        "pct_spot_vs_ref": {
            "abs_gt":"precio spot lejos de la referencia → señal GBM sobreextiende; riesgo de reversión",
            "abs_lt":"precio spot cerca de la referencia → señal GBM más calibrada",
        },
        "hora_utc": {
            "lt":    "hora temprana → mercados cripto menos líquidos, spreads más amplios; edge real menor",
            "gt":    "hora tardía/noche → sesión US cerrada, menos participantes informados; señales más ruidosas",
        },
        "ibs_15": {
            "gt":    "IBS alto (precio cerca del máximo) → sobrecompra de corto plazo; BUY_YES menos fiable",
            "lt":    "IBS bajo (precio cerca del mínimo) → sobreventa de corto plazo; BUY_NO menos fiable",
        },
        "delta_ratio": {
            "abs_lt":"delta_ratio bajo → order flow débil; señal insuficiente para batir el spread",
            "abs_gt":"delta_ratio alto → flow informado visible; edge real en el desequilibrio",
        },
        "delta_ratio_macro": {
            "abs_gt":"flow macro dominante → el lado comprador/vendedor ya fijó el precio en Polymarket",
            "abs_lt":"flow macro débil → el mercado no ha procesado aún la presión; lag explotable",
        },
    }

    tiene_patrones = False
    for strat_key, p in sorted(patrones.items()):
        filtros   = p.get("filtros_causales", [])
        ganadores = p.get("patrones_ganadores", [])
        if not filtros and not ganadores:
            continue
        tiene_patrones = True
        lineas.append(f"### {strat_key}")

        for f in filtros:
            feat = f["feature"]; cond = f["condicion"]
            interp = INTERPRETACIONES.get(feat, {}).get(cond, "")
            accion = f"SKIP cuando `{feat}` {_cond_legible(cond)} {f['umbral']}"
            lineas += [
                f"- **FILTRO** `{feat}` {_cond_legible(cond)} `{f['umbral']}` → IC={f['ic_malo']:+.3f} (n={f['n_malo']})",
                f"  - _Por qué funciona_: {interp}" if interp else "",
                f"  - _Acción_: {accion}",
                f"  - _Potencial_: sin este filtro IC_bueno={f['ic_bueno']:+.3f} (n={f['n_bueno']})",
                "",
            ]

        for g in ganadores:
            feat = g["feature"]; cond = g["condicion"]
            interp = INTERPRETACIONES.get(feat, {}).get(cond, "")
            accion = f"Kelly boost +{g['kelly_boost']:.2f}€ cuando `{feat}` {_cond_legible(cond)} {g['umbral']}"
            lineas += [
                f"- **PATRÓN** `{feat}` {_cond_legible(cond)} `{g['umbral']}` → IC={g['ic_patron']:+.3f} (n={g['n_patron']})",
                f"  - _Por qué funciona_: {interp}" if interp else "",
                f"  - _Acción_: {accion} (IC base={g['ic_base']:+.3f})",
                "",
            ]

    if not tiene_patrones:
        lineas.append("_Sin patrones causales con n≥15 aún. El sistema necesita más datos._\n")

    lineas += [
        "## Estrategias nuevas sugeridas",
        "_Derivadas de los patrones aprendidos:_",
        "",
    ]

    # Generar sugerencias basadas en patrones encontrados
    sugerencias = _sugerir_estrategias(patrones, params, resultados)
    if sugerencias:
        for s in sugerencias:
            lineas.append(f"- {s}")
    else:
        lineas.append("_Sin sugerencias automáticas con datos actuales. Ampliar n por estrategia._")

    lineas += [
        "",
        "## Estado de aprendizaje por estrategia",
        "",
        "| Estrategia | n | IC | PNL | Filtros | Patrones |",
        "|---|---|---|---|---|---|",
    ]
    for k, v in sorted(params.get("estrategias", {}).items()):
        if not isinstance(v, dict): continue
        n = v.get("n", 0)
        if n < 5: continue
        ic = v.get("ic_bayes", 0)
        pnl = v.get("pnl_total", 0)
        nf = len(v.get("filtros_causales", []))
        np_ = len(v.get("patrones_ganadores", []))
        act = "✅" if v.get("activa", True) else "🚫"
        lineas.append(f"| {act} {k} | {n} | {ic:+.3f} | {pnl:+.2f}€ | {nf} | {np_} |")

    out = "\n".join(l for l in lineas if l is not None)
    hip_path = DIR_SHADOW / "hipotesis_auto.md"
    hip_path.write_text(out, encoding="utf-8")
    print(f"  → hipotesis_auto.md actualizado ({len(patrones)} estrategias con patrones)")


def _cond_legible(cond: str) -> str:
    return {"gt": ">", "lt": "<", "abs_gt": "|x|>", "abs_lt": "|x|≤"}.get(cond, cond)


def _sugerir_estrategias(patrones: dict, params: dict, resultados: list) -> list[str]:
    """
    A partir de los patrones aprendidos, propone estrategias nuevas o ajustes.
    Devuelve lista de strings (markdown) con sugerencias accionables.
    """
    sugs = []
    estrats = params.get("estrategias", {})

    # 1. Si BTC#60min o ETH#60min tienen patrón en sigma_h → proponer filtro sigma
    for activo in ["BTC", "ETH", "SOL"]:
        key = f"UPDOWN_GBM#{activo}#60min"
        sp = estrats.get(key, {})
        pats_key = patrones.get(key, {})
        for p in pats_key.get("patrones_ganadores", []):
            if p["feature"] == "sigma_h" and p["ic_patron"] > 0.15:
                sugs.append(
                    f"**H-SIGMA-{activo}-60MIN**: `{key}` gana cuando sigma_h {_cond_legible(p['condicion'])} "
                    f"{p['umbral']} (IC={p['ic_patron']:+.3f} n={p['n_patron']}). "
                    f"Implementar como filtro pre-predicción en shadow_predict.py."
                )

    # 2. Si hora_utc aparece como patrón en ORDER_FLOW → refinar blacklist horaria
    of_pats = patrones.get("ORDER_FLOW_5M", {})
    for f in of_pats.get("filtros_causales", []):
        if f["feature"] == "hora_utc":
            cond = f["condicion"]
            umb = f["umbral"]
            hora_int = int(umb)
            sugs.append(
                f"**H-HORA-OF**: ORDER_FLOW_5M tiene IC={f['ic_malo']:+.3f} cuando hora_utc {_cond_legible(cond)} {umb}. "
                f"Añadir hora {hora_int} a ORDER_FLOW_BLACKLIST_HOURS si n≥20."
            )

    # 3. Si IBS aparece como patrón ganador → proponer IBS-boost en shadow_predict
    for key, pdata in patrones.items():
        for g in pdata.get("patrones_ganadores", []):
            if g["feature"] == "ibs_15" and g["ic_patron"] > 0.15 and g["n_patron"] >= 15:
                dir_text = "BUY_NO" if g["condicion"] == "gt" else "BUY_YES"
                sugs.append(
                    f"**H-IBS-{key}**: IBS {_cond_legible(g['condicion'])} {g['umbral']} "
                    f"correlaciona con éxito en {key} (IC={g['ic_patron']:+.3f} n={g['n_patron']}). "
                    f"Confirma señal de reversión media → alinear con {dir_text}."
                )

    # 4. Si hay estrategia activa con IC creciente y n acercándose a 40 → alertar
    for key, v in estrats.items():
        if not isinstance(v, dict): continue
        if not v.get("activa", True): continue
        n = v.get("n", 0)
        ic = v.get("ic_bayes", 0)
        if 30 <= n < 40 and ic > 0.08:
            ops_rest = 40 - n
            sugs.append(
                f"**LIVE-CANDIDATA**: `{key}` — IC={ic:+.3f} n={n}. "
                f"Faltan ~{ops_rest} resoluciones para umbral n≥40. ETA: ~{ops_rest * 0.7:.0f}h."
            )

    return sugs


def guardar_performance(performance: list):
    if not performance:
        return
    columnas = list(performance[0].keys())
    with open(PERFORMANCE_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        w.writeheader()
        for p in performance:
            w.writerow(p)
    print(f"  Performance guardado: {PERFORMANCE_PATH}")


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Postmortem ===")

    # Gap 1: grader independiente
    alertas = _verificar_integridad()
    if alertas:
        for a in alertas:
            print(f"  [ALERTA INTEGRIDAD] {a}")
        try:
            import os, requests
            tok = os.environ.get("TELEGRAM_TOKEN", "")
            cid = os.environ.get("TELEGRAM_CHAT_ID", "")
            if tok and cid:
                msg = "⚠️ *Alerta integridad pipeline*\n" + "\n".join(f"• {a}" for a in alertas)
                requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
                              json={"chat_id": cid, "text": msg, "parse_mode": "Markdown"},
                              timeout=10)
        except Exception:
            pass

    resultados = cargar_results()
    if not resultados:
        print("  Sin resultados aún — nada que analizar.")
        print(f"[{ts}] === Fin postmortem ===")
        return

    pred_index    = cargar_predicciones_index()
    ya_procesadas = cargar_ya_postmortem()

    perdidas_nuevas = []
    for r in resultados:
        if int(r.get("acierto", 1)) == 1:
            continue
        clave_pm = (r["strategy"], r["market_id"], r.get("prediction_timestamp", ""))
        if clave_pm in ya_procesadas:
            continue
        clave_pred = (r["strategy"], r["market_id"], r.get("decision", ""))
        pred  = pred_index.get(clave_pred)
        causa = clasificar_causa(r, pred)
        perdidas_nuevas.append({**r, "causa_perdida": causa})

    perdidas_total = [r for r in resultados if int(r.get("acierto", 1)) == 0]
    aciertos_total = len(resultados) - len(perdidas_total)
    print(f"  Resultados totales: {len(resultados)}")
    print(f"  Aciertos: {aciertos_total} | Pérdidas: {len(perdidas_total)}")
    print(f"  Pérdidas nuevas a diagnosticar: {len(perdidas_nuevas)}")

    if perdidas_nuevas:
        nuevo    = not POSTMORTEM_PATH.exists()
        columnas = list(perdidas_nuevas[0].keys())
        with open(POSTMORTEM_PATH, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=columnas, extrasaction="ignore")
            if nuevo:
                w.writeheader()
            for p in perdidas_nuevas:
                w.writerow(p)

        causas = {}
        for p in perdidas_nuevas:
            c = p["causa_perdida"]
            causas[c] = causas.get(c, 0) + 1
        print("  Causas de pérdidas nuevas:")
        for c, n in sorted(causas.items(), key=lambda x: -x[1]):
            print(f"    {c:25s}: {n}")

    # Params con todos los resultados
    todos_con_causa = []
    for r in resultados:
        if int(r.get("acierto", 1)) == 0:
            clave_pred = (r["strategy"], r["market_id"], r.get("decision", ""))
            pred  = pred_index.get(clave_pred)
            todos_con_causa.append({**r, "causa_perdida": clasificar_causa(r, pred)})
        else:
            todos_con_causa.append({**r, "causa_perdida": ""})

    params = calcular_params(todos_con_causa)

    # Aprendizaje causal completo: aprende POR QUÉ pierde Y POR QUÉ gana
    patrones = aprender_patrones_causales(resultados, pred_index)

    n_filtros  = sum(len(v["filtros_causales"])  for v in patrones.values())
    n_patrones = sum(len(v["patrones_ganadores"]) for v in patrones.values())

    if patrones:
        print(f"\n  Aprendizaje causal: {n_filtros} filtros (evitar) + {n_patrones} patrones (amplificar)")
        for strat_key, p in patrones.items():
            for f in p["filtros_causales"]:
                print(f"    ✗ EVITAR  {strat_key}: |{f['feature']}|>{f['umbral']}"
                      f"  IC={f['ic_malo']:+.3f} (n={f['n_malo']})"
                      f"  vs bueno={f['ic_bueno']:+.3f}")
            for g in p["patrones_ganadores"]:
                print(f"    ✓ AMPLIF  {strat_key}: {g['condicion']} {g['feature']} {g['umbral']}"
                      f"  IC={g['ic_patron']:+.3f} (n={g['n_patron']})"
                      f"  kelly_boost=+{g['kelly_boost']:.2f}€")
            # Inyectar en params de esa estrategia
            if strat_key in params["estrategias"]:
                params["estrategias"][strat_key]["filtros_causales"]   = p["filtros_causales"]
                params["estrategias"][strat_key]["patrones_ganadores"] = p["patrones_ganadores"]
            else:
                params["estrategias"][strat_key] = p
    else:
        print(f"\n  Sin patrones causales nuevos (datos insuficientes o sin señal clara)")

    # Preservar desactivaciones manuales y sección meta (ambas sobreviven al ciclo de reescritura)
    if PARAMS_PATH.exists():
        try:
            old_data = json.load(open(PARAMS_PATH, encoding="utf-8"))
            old = old_data.get("estrategias", {})
            for k, v in old.items():
                if not v.get("activa", True) and k in params["estrategias"]:
                    motivo_old = v.get("motivo", "")
                    if "MANUALMENTE" in motivo_old or ("DESACTIVADA 202" in motivo_old and "DESACTIVADA" in motivo_old):
                        params["estrategias"][k]["activa"] = False
                        if "DESACTIVADA" not in params["estrategias"][k]["motivo"]:
                            params["estrategias"][k]["motivo"] += f" | {motivo_old.split('|')[-1].strip()}"
            # Preservar meta (hypothesis_tracker y cambios manuales lo usan)
            if "meta" in old_data and old_data["meta"]:
                existing_meta = old_data["meta"]
                new_meta = params.get("meta", {})
                # Merge: hypothesis_tracker puede añadir a gbm_blacklist_hours_auto; preservar entradas manuales
                if "gbm_blacklist_hours_auto" in existing_meta:
                    merged_bl = set(existing_meta.get("gbm_blacklist_hours_auto", []))
                    merged_bl.update(new_meta.get("gbm_blacklist_hours_auto", []))
                    existing_meta["gbm_blacklist_hours_auto"] = sorted(merged_bl)
                existing_meta.update({k: v for k, v in new_meta.items() if k != "gbm_blacklist_hours_auto"})
                params["meta"] = existing_meta
        except Exception:
            pass

    with open(PARAMS_PATH, "w", encoding="utf-8") as f:
        json.dump(params, f, indent=2, ensure_ascii=False)

    print(f"\n  Ajustes automáticos por estrategia/subtipo:")
    for s, p in sorted(params["estrategias"].items()):
        estado = "✓" if p["activa"] else "✗ DESACT"
        print(f"    [{estado}] {s:35s}  n={p['n']:>3}  edge≥{p['edge_minimo']:.2f}  {p['motivo']}")

    # Performance completo
    performance = generar_performance(todos_con_causa, pred_index)
    guardar_performance(performance)

    print(f"\n  Ranking de estrategias por P&L:")
    for p in performance:
        pf_str = f"{p['profit_factor']:.2f}" if p["profit_factor"] < 99 else "∞"
        print(f"    {p['strategy']:30s}  {p['n_total']:>3}ops  "
              f"hit={p['hit_rate']*100:.0f}%  "
              f"pnl={p['pnl_total']:+.2f}€  "
              f"exp={p['expectancy']:+.4f}  "
              f"IC={p['ic_bayes']:+.3f}  PF={pf_str}")

    print(f"\n  Params guardados: {PARAMS_PATH}")
    _escribir_state(params, resultados)  # Gap 2: state file

    # Generador de hipótesis automáticas — aprende POR QUÉ y propone QUÉ hacer
    try:
        _generar_hipotesis_auto(params, patrones, resultados)
    except Exception as e:
        print(f"  [WARN] hipotesis_auto.md: {e}")

    try:
        import hypothesis_tracker as ht
        h_resultados = ht.run(resultados)
        h_md = ht.generate_markdown_section(h_resultados)
        hip_path = DIR_SHADOW / "hipotesis_auto.md"
        hip_path.write_text(hip_path.read_text(encoding="utf-8") + h_md, encoding="utf-8")
        listas = [hid for hid, d in h_resultados.items()
                  if d.get("status") in ("LISTA_IMPLEMENTAR", "LISTA_LIVE", "LISTA_EVALUAR")]
        print(f"  → hypothesis_tracker: {len(h_resultados)} hipótesis | "
              f"{len(listas)} listas para evaluar: {listas}")
    except Exception as e:
        print(f"  [WARN] hypothesis_tracker: {e}")

    print(f"[{ts}] === Fin postmortem ===")


if __name__ == "__main__":
    main()
