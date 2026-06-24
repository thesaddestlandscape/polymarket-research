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
UMBRAL_DESACTIVAR = (-0.30, 8)


def cargar_results() -> list:
    if not RESULTS_PATH.exists():
        return []
    with open(RESULTS_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cargar_predicciones_index() -> dict:
    index = {}
    for arch in sorted(DIR_SHADOW.glob("predictions_*.csv")):
        with open(arch, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("decision") in ("BUY_YES", "BUY_NO"):
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
        for clave in claves:
            if clave not in por_estrategia:
                por_estrategia[clave] = {"n": 0, "aciertos": 0, "pnl": 0.0, "causas": {}}
            por_estrategia[clave]["n"] += 1
            por_estrategia[clave]["aciertos"] += int(r.get("acierto", 0))
            try:
                por_estrategia[clave]["pnl"] += float(r.get("pnl_neto", 0))
            except (ValueError, TypeError):
                pass
            causa = r.get("causa_perdida", "")
            if causa:
                por_estrategia[clave]["causas"][causa] = por_estrategia[clave]["causas"].get(causa, 0) + 1

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

        params["estrategias"][s] = {
            "activa":          activa,
            "edge_minimo":     edge_minimo,
            "ic_bayes":        ic_efectivo,
            "n":               n,
            "pnl_total":       round(d["pnl"], 4),
            "causa_principal": causa_principal,
            "motivo":          motivo,
            "apuesta_kelly":   apuesta_kelly,
        }

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


# Qué features analizar por estrategia/subtipo y con qué condición
FEATURE_RULES = {
    "UPDOWN_GBM#5min":     [("pct_spot_vs_ref", "abs_gt")],
    "UPDOWN_GBM#BTC#5min": [("pct_spot_vs_ref", "abs_gt")],
    "UPDOWN_GBM#ETH#5min": [("pct_spot_vs_ref", "abs_gt")],
    "UPDOWN_GBM#SOL#5min": [("pct_spot_vs_ref", "abs_gt")],
    "ORDER_FLOW_5M":        [("delta_ratio",     "abs_gt")],
}

# Umbrales mínimos para generar un filtro aprendido
IC_BUCKET_MIN  = -0.12   # IC del bucket problemático para activar el filtro
N_BUCKET_MIN   = 8       # mínimo de observaciones en el bucket


def aprender_filtros_causales(resultados: list, pred_index: dict) -> dict:
    """
    Analiza la correlación entre features en el momento de la predicción
    y el outcome real. Descubre automáticamente en qué rangos de features
    el modelo pierde sistemáticamente y genera filtros para evitarlos.

    Retorna dict de filtros aprendidos por clave de estrategia.
    """
    filtros = {}

    for strat_key, feature_specs in FEATURE_RULES.items():
        # Recopilar (resultado, features) para esta clave
        datos = []
        for r in resultados:
            s   = r.get("strategy", "")
            sub = r.get("subtype", "")
            key = s + ("#" + sub if sub else "")
            if key != strat_key:
                continue
            clave_pred = (s, r.get("market_id", ""), r.get("decision", ""))
            pred = pred_index.get(clave_pred)
            feats = _extraer_features(r, pred)
            if feats:
                datos.append((r, feats))

        if len(datos) < N_BUCKET_MIN:
            continue

        filtros_strat = []

        for feature, condicion in feature_specs:
            vals = [(r, f[feature]) for r, f in datos if feature in f]
            if len(vals) < N_BUCKET_MIN:
                continue

            # Probar percentiles como posibles umbrales de corte
            abs_vals = sorted(abs(v) for _, v in vals)
            percentiles = [0.33, 0.50, 0.66]

            mejor = None
            mejor_dif_ic = 0.0

            for p in percentiles:
                idx = int(len(abs_vals) * p)
                umbral = abs_vals[idx] if idx < len(abs_vals) else None
                if umbral is None or umbral == 0:
                    continue

                encima = [(r, v) for r, v in vals if abs(v) > umbral]
                debajo = [(r, v) for r, v in vals if abs(v) <= umbral]

                if len(encima) < N_BUCKET_MIN or len(debajo) < 3:
                    continue

                wins_enc = sum(int(r.get("acierto", 0)) for r, _ in encima)
                wins_deb = sum(int(r.get("acierto", 0)) for r, _ in debajo)
                ic_enc   = (wins_enc + 1) / (len(encima) + 2) - 0.5
                ic_deb   = (wins_deb + 1) / (len(debajo) + 2) - 0.5
                dif_ic   = ic_deb - ic_enc

                if ic_enc < IC_BUCKET_MIN and dif_ic > mejor_dif_ic:
                    mejor_dif_ic = dif_ic
                    mejor = {
                        "feature":    feature,
                        "condicion":  condicion,
                        "umbral":     round(umbral, 4),
                        "ic_malo":    round(ic_enc, 4),
                        "ic_bueno":   round(ic_deb, 4),
                        "n_malo":     len(encima),
                        "n_bueno":    len(debajo),
                        "descubierto": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                    }

            if mejor:
                filtros_strat.append(mejor)

        if filtros_strat:
            filtros[strat_key] = filtros_strat

    return filtros


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

    # Aprendizaje causal: descubrir filtros de features automáticamente
    filtros_causales = aprender_filtros_causales(resultados, pred_index)
    if filtros_causales:
        print(f"\n  Filtros causales aprendidos:")
        for strat_key, filtros in filtros_causales.items():
            for f in filtros:
                print(f"    {strat_key}: {f['feature']} {f['condicion']} {f['umbral']}"
                      f"  → IC_malo={f['ic_malo']:+.3f} (n={f['n_malo']})"
                      f"  IC_bueno={f['ic_bueno']:+.3f} (n={f['n_bueno']})")
            # Inyectar en params de esa estrategia
            if strat_key in params["estrategias"]:
                params["estrategias"][strat_key]["filtros_causales"] = filtros
            else:
                params["estrategias"][strat_key] = {"filtros_causales": filtros}
    else:
        print(f"\n  Sin filtros causales nuevos (datos insuficientes o sin patrones claros)")

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
    print(f"[{ts}] === Fin postmortem ===")


if __name__ == "__main__":
    main()
