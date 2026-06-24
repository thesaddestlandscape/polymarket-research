"""
shadow_resumen.py — genera data/shadow/estado_actual.md tras cada ciclo fast.

Visible en GitHub en tiempo real. Muestra:
  - Bankroll actual vs inicial (20€ operativo / 30€ depósito)
  - P&L del día y acumulado por estrategia con IC, Kelly, apuesta actual
  - Últimas 5 resoluciones
  - Señales abiertas pendientes
"""
import csv
import json
import glob
from datetime import datetime, timezone, timedelta
from pathlib import Path

DIR_SHADOW   = Path("data/shadow")
RESULTS_PATH = DIR_SHADOW / "results.csv"
PARAMS_PATH  = DIR_SHADOW / "strategy_params.json"
OUTPUT_MD    = DIR_SHADOW / "estado_actual.md"

CAPITAL_OPERATIVO = 20.0
DEPOSITO_TOTAL    = 30.0
RESERVA           = 10.0


def cargar_csv(path):
    if not Path(path).exists():
        return []
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cargar_params():
    if not PARAMS_PATH.exists():
        return {}
    with open(PARAMS_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return data.get("estrategias", {})


def main():
    ahora = datetime.now(timezone.utc)
    hoy   = ahora.strftime("%Y-%m-%d")

    resultados = cargar_csv(RESULTS_PATH)
    params     = cargar_params()

    # ── Bankroll ──────────────────────────────────────────────────────────────
    pnl_total = sum(float(r.get("pnl_neto", 0)) for r in resultados)
    bankroll  = CAPITAL_OPERATIVO + pnl_total
    roi_op    = pnl_total / CAPITAL_OPERATIVO * 100
    roi_dep   = pnl_total / DEPOSITO_TOTAL    * 100

    # P&L del día de hoy
    pnl_hoy = sum(
        float(r.get("pnl_neto", 0)) for r in resultados
        if (r.get("resolution_timestamp", "") or "")[:10] == hoy
    )

    # ── Stats por estrategia (subtipo más específico disponible) ──────────────
    from collections import defaultdict
    por_strat = defaultdict(lambda: {"n": 0, "win": 0, "pnl": 0.0})
    for r in resultados:
        key = r.get("strategy", "?")
        sub = r.get("subtype", "")
        if sub:
            key = f"{key}#{sub}"
        por_strat[key]["n"]   += 1
        por_strat[key]["win"] += int(r.get("acierto", 0))
        por_strat[key]["pnl"] += float(r.get("pnl_neto", 0))

    # Agrupar también a nivel estrategia base
    por_base = defaultdict(lambda: {"n": 0, "win": 0, "pnl": 0.0})
    for r in resultados:
        key = r.get("strategy", "?")
        por_base[key]["n"]   += 1
        por_base[key]["win"] += int(r.get("acierto", 0))
        por_base[key]["pnl"] += float(r.get("pnl_neto", 0))

    # ── Últimas 5 resoluciones ────────────────────────────────────────────────
    ultimas = resultados[-5:] if resultados else []

    # ── Señales abiertas (predicciones no resueltas) ──────────────────────────
    resueltos_ids = set(
        (r.get("prediction_timestamp",""), r.get("strategy",""), r.get("market_id",""))
        for r in resultados
    )
    archivos_pred = sorted(glob.glob(str(DIR_SHADOW / "predictions_*.csv")))[-2:]
    abiertas = 0
    for arch in archivos_pred:
        with open(arch, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("decision","") not in ("BUY_YES","BUY_NO"):
                    continue
                clave = (row.get("timestamp_utc",""), row.get("strategy",""), row.get("market_id",""))
                if clave not in resueltos_ids:
                    abiertas += 1

    # ── Construir Markdown ────────────────────────────────────────────────────
    ts = ahora.strftime("%Y-%m-%d %H:%M UTC")
    n_total = len(resultados)
    n_win   = sum(int(r.get("acierto", 0)) for r in resultados)
    wr_g    = n_win / n_total * 100 if n_total else 0

    signo_pnl    = "+" if pnl_total >= 0 else ""
    signo_hoy    = "+" if pnl_hoy   >= 0 else ""
    emoji_roi    = "🟢" if pnl_total >= 0 else "🔴"
    emoji_hoy    = "🟢" if pnl_hoy   >= 0 else "🔴"

    lines = [
        f"# Estado del bot — {ts}",
        "",
        "## Capital",
        f"| | |",
        f"|---|---|",
        f"| Depósito total | **{DEPOSITO_TOTAL:.0f} €** |",
        f"| Capital operativo | **{CAPITAL_OPERATIVO:.0f} €** |",
        f"| Reserva intocable | **{RESERVA:.0f} €** |",
        "",
        "## Bankroll simulado",
        f"| | |",
        f"|---|---|",
        f"| Inicio | {CAPITAL_OPERATIVO:.2f} € |",
        f"| Actual | **{bankroll:.2f} €** |",
        f"| P&L acumulado | {emoji_roi} **{signo_pnl}{pnl_total:.2f} €** |",
        f"| ROI s/ operativo | {signo_pnl}{roi_op:.2f}% |",
        f"| ROI s/ depósito | {signo_pnl}{roi_dep:.2f}% |",
        f"| P&L hoy ({hoy}) | {emoji_hoy} {signo_hoy}{pnl_hoy:.2f} € |",
        f"| Operaciones resueltas | {n_total} ({n_win} WIN / {n_total-n_win} LOSS) — {wr_g:.1f}% |",
        f"| Señales abiertas | {abiertas} |",
        "",
        "## Estrategias (visión global)",
        "",
        "| Estrategia | n | Win% | IC_efectivo | PNL | Apuesta | Estado |",
        "|---|---|---|---|---|---|---|",
    ]

    # Estrategias base ordenadas por PNL
    for s, d in sorted(por_base.items(), key=lambda x: x[1]["pnl"], reverse=True):
        n   = d["n"]
        wr  = d["win"] / n * 100 if n else 0
        pnl = d["pnl"]
        ic  = (d["win"] + 1) / (n + 2) - 0.5
        confianza = min(1.0, n / 20)
        ic_ef = ic * confianza

        sp = params.get(s, {})
        activa = sp.get("activa", True)
        apuesta = sp.get("apuesta_kelly", 0.90)

        est_str = "✅ activa" if activa else "🚫 desactivada"
        if activa and n < 8:
            est_str = "⏳ acumulando"
        elif activa and ic_ef < 0:
            est_str = "⚠️ IC negativo"

        signo = "+" if pnl >= 0 else ""
        lines.append(
            f"| {s} | {n} | {wr:.1f}% | {ic_ef:+.3f} | {signo}{pnl:.2f}€ | {apuesta:.2f}€ | {est_str} |"
        )

    lines += [
        "",
        "## Últimas 5 resoluciones",
        "",
        "| Timestamp | Estrategia | Mercado | Resultado | PNL |",
        "|---|---|---|---|---|",
    ]

    for r in reversed(ultimas):
        ts_r   = (r.get("resolution_timestamp","") or "")[:16]
        strat  = r.get("strategy","")
        sub    = r.get("subtype","")
        label  = f"{strat}#{sub}" if sub else strat
        q      = (r.get("question","") or "")[:50]
        acierto = r.get("acierto","0")
        emoji  = "✅ WIN" if acierto == "1" else "❌ LOSS"
        pnl_r  = float(r.get("pnl_neto", 0))
        signo_r = "+" if pnl_r >= 0 else ""
        lines.append(f"| {ts_r} | {label} | {q}… | {emoji} | {signo_r}{pnl_r:.2f}€ |")

    lines += [
        "",
        "---",
        f"*Actualizado automáticamente cada ~60s por el fast loop*",
    ]

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"  [resumen] Bankroll={bankroll:.2f}€ PNL={signo_pnl}{pnl_total:.2f}€ "
          f"({signo_pnl}{roi_op:.1f}% op) | Hoy={signo_hoy}{pnl_hoy:.2f}€ | "
          f"n={n_total} wr={wr_g:.1f}% | abiertas={abiertas}")


if __name__ == "__main__":
    main()
