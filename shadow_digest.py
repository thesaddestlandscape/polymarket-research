"""
shadow_digest.py — resumen diario único del experimento, enviado por Telegram.

Filosofía: una sola notificación al día, conciso, informativo, sin
recomendaciones operativas. El objetivo es tener visibilidad del
experimento sin caer en el sesgo de saliencia que provocan las
notificaciones constantes.

Contiene:
  - Estado de actividad de las últimas 24 horas (predicciones emitidas,
    resueltas).
  - Horserace global de las seis estrategias: P&L acumulado, win rate,
    número de operaciones.
  - Resoluciones nuevas del último día desglosadas por estrategia.
  - Número de predicciones operables pendientes de resolver, agrupadas
    por horizonte temporal.

Ejecutado una vez al día por .github/workflows/digest.yml a las 20:00 UTC
(21:00 hora España invierno / 22:00 verano).

Secretos requeridos en GitHub (Settings → Secrets and variables → Actions):
  - TELEGRAM_TOKEN
  - TELEGRAM_CHAT_ID

Si no están configurados, el script genera el digest e imprime por
stdout pero no envía nada (no falla).
"""

import csv
import glob
import os
from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests

TIMEOUT = 15
DIR_SHADOW = Path("data/shadow")
RESULTS_PATH = DIR_SHADOW / "results.csv"

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "")

EMOJI = {
    1: "🥇", 2: "🥈", 3: "🥉",
}


def cargar_predicciones_de_ultimo_dia() -> list:
    """Carga predicciones (todas, no solo operables) del último día."""
    desde = datetime.now(timezone.utc) - timedelta(hours=24)
    todas = []
    archivos = sorted(glob.glob(str(DIR_SHADOW / "predictions_*.csv")))[-3:]
    for arch in archivos:
        with open(arch, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    ts = datetime.fromisoformat(
                        row["timestamp_utc"].replace("Z", "+00:00"))
                except Exception:
                    continue
                if ts < desde:
                    continue
                todas.append(row)
    return todas


def cargar_resultados_acumulados() -> list:
    """Carga TODOS los resultados acumulados desde el inicio."""
    if not RESULTS_PATH.exists():
        return []
    with open(RESULTS_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def horserace_global(resultados: list) -> dict:
    """Agrega P&L y win rate por estrategia desde el inicio del experimento."""
    agg = defaultdict(lambda: {"n": 0, "aciertos": 0, "pnl": 0.0})
    for r in resultados:
        s = r.get("strategy", "")
        if not s:
            continue
        agg[s]["n"] += 1
        try:
            agg[s]["aciertos"] += int(r.get("acierto", 0))
        except (ValueError, TypeError):
            pass
        try:
            agg[s]["pnl"] += float(r.get("pnl_neto", 0))
        except (ValueError, TypeError):
            pass
    return dict(agg)


def horserace_ultimo_dia(resultados: list) -> dict:
    """Resoluciones registradas en las últimas 24 horas (no creadas)."""
    desde = datetime.now(timezone.utc) - timedelta(hours=24)
    sub = []
    for r in resultados:
        try:
            ts = datetime.fromisoformat(
                r.get("resolution_timestamp", "").replace("Z", "+00:00"))
        except Exception:
            continue
        if ts >= desde:
            sub.append(r)
    return horserace_global(sub)


def horas_a(end_date: str) -> float | None:
    if not end_date:
        return None
    try:
        s = end_date
        if "T" not in s and len(s) == 10:
            s = s + "T23:59:59"
        if not s.endswith("Z") and "+" not in s[10:]:
            s = s + "+00:00"
        else:
            s = s.replace("Z", "+00:00")
        fin = datetime.fromisoformat(s)
        ahora = datetime.now(timezone.utc)
        return (fin - ahora).total_seconds() / 3600
    except Exception:
        return None


def pendientes_por_horizonte() -> dict:
    """Cuenta predicciones operables aún no resueltas, por horizonte temporal."""
    archivos = sorted(glob.glob(str(DIR_SHADOW / "predictions_*.csv")))
    pendientes_ids = set()
    if RESULTS_PATH.exists():
        with open(RESULTS_PATH, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                pendientes_ids.add((r.get("prediction_timestamp", ""),
                                     r.get("strategy", ""),
                                     r.get("market_id", "")))

    buckets = {"<24h": 0, "1-7d": 0, "7-14d": 0, "vencidas_sin_resolver": 0}
    for arch in archivos:
        with open(arch, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("decision", "SKIP") == "SKIP":
                    continue
                clave = (row.get("timestamp_utc", ""),
                         row.get("strategy", ""),
                         row.get("market_id", ""))
                if clave in pendientes_ids:
                    continue
                h = horas_a(row.get("end_date", ""))
                if h is None:
                    continue
                if h < 0:
                    buckets["vencidas_sin_resolver"] += 1
                elif h < 24:
                    buckets["<24h"] += 1
                elif h < 168:
                    buckets["1-7d"] += 1
                else:
                    buckets["7-14d"] += 1
    return buckets


def formato_eur(x: float) -> str:
    signo = "+" if x >= 0 else ""
    return f"{signo}{x:.2f}€"


def construir_digest() -> str:
    ahora = datetime.now(timezone.utc)

    predicciones_24h = cargar_predicciones_de_ultimo_dia()
    operables_24h = [p for p in predicciones_24h
                     if p.get("decision", "SKIP") != "SKIP"]

    resultados_todos = cargar_resultados_acumulados()
    hr_global = horserace_global(resultados_todos)
    hr_dia = horserace_ultimo_dia(resultados_todos)
    buckets = pendientes_por_horizonte()

    lineas = []
    lineas.append("📊 Polymarket Shadow Trader")
    lineas.append(f"Resumen diario · {ahora.strftime('%Y-%m-%d %H:%M UTC')}")
    lineas.append("")
    lineas.append("── ÚLTIMAS 24 HORAS ──")
    lineas.append(f"Predicciones emitidas: {len(predicciones_24h)}")
    lineas.append(f"  · operables: {len(operables_24h)}")
    lineas.append(f"  · SKIP (sin edge): {len(predicciones_24h) - len(operables_24h)}")
    n_resueltas_dia = sum(d["n"] for d in hr_dia.values())
    lineas.append(f"Resoluciones nuevas: {n_resueltas_dia}")
    lineas.append("")

    if hr_global:
        lineas.append("── HORSERACE GLOBAL (P&L acumulado) ──")
        ranking = sorted(hr_global.items(), key=lambda kv: kv[1]["pnl"],
                         reverse=True)
        for i, (s, d) in enumerate(ranking, 1):
            wr = d["aciertos"] / d["n"] * 100 if d["n"] else 0
            emoji = EMOJI.get(i, "  ")
            lineas.append(f"{emoji} {s[:22]:<22} {formato_eur(d['pnl']):>9}"
                          f" n={d['n']:>3} wr={wr:4.0f}%")
        lineas.append("")
    else:
        lineas.append("── HORSERACE GLOBAL ──")
        lineas.append("(aún no hay resoluciones)")
        lineas.append("")

    if hr_dia:
        lineas.append("── NUEVAS RESOLUCIONES (24h) ──")
        for s, d in sorted(hr_dia.items(), key=lambda kv: kv[1]["pnl"],
                           reverse=True):
            wr = d["aciertos"] / d["n"] * 100 if d["n"] else 0
            lineas.append(f"{s[:22]:<22} {d['aciertos']}/{d['n']:<3} "
                          f"{formato_eur(d['pnl']):>9} wr={wr:.0f}%")
        lineas.append("")

    lineas.append("── PENDIENTES DE RESOLVER ──")
    total_pend = sum(buckets.values())
    lineas.append(f"Total operables: {total_pend}")
    lineas.append(f"  · <24h: {buckets['<24h']}")
    lineas.append(f"  · 1-7 días: {buckets['1-7d']}")
    lineas.append(f"  · 7-14 días: {buckets['7-14d']}")
    if buckets["vencidas_sin_resolver"]:
        lineas.append(f"  · ⚠ vencidas sin resolver: "
                      f"{buckets['vencidas_sin_resolver']}")
    lineas.append("")
    lineas.append("(Sin recomendaciones operativas. "
                  "Decisión al final de las 3 semanas.)")

    return "\n".join(lineas)


def enviar_telegram(texto: str) -> bool:
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("(TELEGRAM_TOKEN o TELEGRAM_CHAT_ID no configurados, "
              "no se envía mensaje)")
        return False
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": texto,
        "disable_web_page_preview": True,
    }
    try:
        r = requests.post(url, json=payload, timeout=TIMEOUT)
        r.raise_for_status()
        print("Mensaje enviado a Telegram.")
        return True
    except Exception as e:
        print(f"Error enviando Telegram: {type(e).__name__}: {e}")
        return False


def main():
    digest = construir_digest()
    print("=" * 50)
    print(digest)
    print("=" * 50)
    enviar_telegram(digest)


if __name__ == "__main__":
    main()
