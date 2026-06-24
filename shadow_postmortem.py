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
    if strategy != "UPDOWN_GBM" and pred:
        try:
            if float(pred.get("horas_a_vencimiento", 999)) < 24:
                return "TIMING_CORTO"
        except (ValueError, TypeError):
            pass

    return "DIRECTION_ERROR"


def calcular_params(resultados: list) -> dict:
    por_estrategia = {}
    for r in resultados:
        s = r["strategy"]
        subtype = r.get("subtype", "")
        # Acumular en clave global y, si hay subtype, también en clave granular
        claves = [s]
        if subtype:
            claves.append(f"{s}#{subtype}")
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

        params["estrategias"][s] = {
            "activa":          activa,
            "edge_minimo":     edge_minimo,
            "ic_bayes":        ic_efectivo,
            "n":               n,
            "pnl_total":       round(d["pnl"], 4),
            "causa_principal": causa_principal,
            "motivo":          motivo,
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
