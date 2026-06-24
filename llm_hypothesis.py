"""
llm_hypothesis.py — Meta-learner: LLM analiza resultados y propone nuevas hipótesis.

Corre UNA VEZ AL DÍA (no en el fast loop). Lee los datos acumulados del sistema
y usa Claude para identificar patrones que el postmortem no captura y proponer
nuevas FEATURE_RULES o ajustes de estrategia para revisión humana.

Requiere: ANTHROPIC_API_KEY en el entorno.
Salida: data/shadow/hipotesis_YYYY-MM-DD.md (commiteado en git, visible en GitHub)

Uso:
    ANTHROPIC_API_KEY=sk-ant-... .venv/bin/python llm_hypothesis.py
"""
import csv
import json
import os
import sys
import glob
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: pip install anthropic")
    sys.exit(1)

DIR_SHADOW = Path("data/shadow")
OUTPUT_DIR = DIR_SHADOW

MODEL   = "claude-sonnet-4-6"
MAX_TOKENS = 2048


# ─── Cargar datos ────────────────────────────────────────────────────────────

def cargar_resultados() -> list:
    path = DIR_SHADOW / "results.csv"
    if not path.exists():
        return []
    return list(csv.DictReader(open(path, encoding="utf-8")))


def cargar_params() -> dict:
    path = DIR_SHADOW / "strategy_params.json"
    if not path.exists():
        return {}
    return json.load(open(path, encoding="utf-8"))


def cargar_performance() -> list:
    path = DIR_SHADOW / "performance.csv"
    if not path.exists():
        return []
    return list(csv.DictReader(open(path, encoding="utf-8")))


def cargar_hipotesis_anteriores() -> list:
    """Lee hipótesis previas para que el LLM no las repita."""
    archivos = sorted(glob.glob(str(DIR_SHADOW / "hipotesis_*.md")))
    anteriores = []
    for arch in archivos[-3:]:  # últimas 3
        try:
            txt = open(arch, encoding="utf-8").read()
            # Extraer solo los títulos de hipótesis para no saturar el contexto
            for line in txt.split("\n"):
                if line.startswith("### Hipótesis") or line.startswith("## Hipótesis"):
                    anteriores.append(line.strip())
        except Exception:
            pass
    return anteriores


# ─── Construir resumen compacto para el LLM ──────────────────────────────────

def construir_resumen(resultados: list, params: dict, performance: list) -> str:
    """
    Construye un resumen compacto y estructurado de los datos para el prompt.
    No mandamos los CSVs completos — solo lo esencial.
    """
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # 1. Resultados por subtipo
    by_sub = defaultdict(lambda: {"n": 0, "win": 0, "pnl": 0.0, "features": []})
    for r in resultados:
        sub = r.get("subtype", "")
        k = r["strategy"] + ("#" + sub if sub else "")
        by_sub[k]["n"]   += 1
        by_sub[k]["win"] += int(r.get("acierto", 0))
        by_sub[k]["pnl"] += float(r.get("pnl_neto", 0))
        # Features de las últimas 30 resoluciones (con datos estructurados)
        feat_raw = r.get("features", "")
        if feat_raw and feat_raw != "{}":
            try:
                feat = json.loads(feat_raw) if isinstance(feat_raw, str) else feat_raw
                acierto = int(r.get("acierto", 0))
                by_sub[k]["features"].append({**feat, "win": acierto})
            except Exception:
                pass

    lines = [f"# Resumen del sistema — {hoy}"]
    lines.append("\n## Resultados por estrategia/subtipo\n")
    lines.append("| Subtipo | n | Win% | IC_ef | PNL |")
    lines.append("|---|---|---|---|---|")
    for k, d in sorted(by_sub.items(), key=lambda x: x[1]["pnl"], reverse=True):
        n = d["n"]
        wr = d["win"] / n if n else 0
        ic = ((d["win"] + 1) / (n + 2) - 0.5) * min(1.0, n / 20)
        lines.append(f"| {k} | {n} | {wr*100:.1f}% | {ic:+.3f} | {d['pnl']:+.2f}€ |")

    # 2. Filtros y patrones ya descubiertos
    lines.append("\n## Filtros causales activos (ya implementados)\n")
    encontrado = False
    for k, v in params.get("estrategias", {}).items():
        for f in v.get("filtros_causales", []):
            lines.append(f"- {k}: |{f['feature']}| > {f['umbral']}  "
                         f"→ IC_malo={f['ic_malo']:+.3f} (n={f['n_malo']}), "
                         f"IC_bueno={f['ic_bueno']:+.3f}")
            encontrado = True
        for g in v.get("patrones_ganadores", []):
            lines.append(f"- PATRON {k}: {g['condicion']} {g['feature']} {g['umbral']}  "
                         f"→ IC={g['ic_patron']:+.3f} boost=+{g['kelly_boost']}€")
            encontrado = True
    if not encontrado:
        lines.append("- (ninguno todavía)")

    # 3. Features estructuradas de últimas resoluciones (muestra por subtipo)
    lines.append("\n## Features estructuradas por subtipo (últimas resoluciones con datos)")
    for k, d in by_sub.items():
        feats = d["features"][-20:]  # últimas 20
        if not feats:
            continue
        wins   = [f for f in feats if f.get("win") == 1]
        losses = [f for f in feats if f.get("win") == 0]
        lines.append(f"\n### {k} ({len(feats)} obs con features)")

        # Promedios de features por win/loss
        all_feat_keys = set()
        for f in feats:
            all_feat_keys.update(k2 for k2 in f if k2 != "win")

        for fk in sorted(all_feat_keys):
            w_vals = [float(f[fk]) for f in wins  if fk in f]
            l_vals = [float(f[fk]) for f in losses if fk in f]
            if w_vals or l_vals:
                w_avg = sum(w_vals) / len(w_vals) if w_vals else None
                l_avg = sum(l_vals) / len(l_vals) if l_vals else None
                w_str = f"{w_avg:+.4f}" if w_avg is not None else "N/A"
                l_str = f"{l_avg:+.4f}" if l_avg is not None else "N/A"
                abs_diff = abs((w_avg or 0) - (l_avg or 0))
                lines.append(f"  - {fk}: WIN_avg={w_str} | LOSS_avg={l_str} | diff={abs_diff:.4f}")

    # 4. Kelly actual
    lines.append("\n## Kelly actual por subtipo")
    for k, v in sorted(params.get("estrategias", {}).items(),
                        key=lambda x: x[1].get("apuesta_kelly", 0), reverse=True)[:8]:
        lines.append(f"- {k}: IC={v['ic_bayes']:+.4f} n={v['n']} "
                     f"kelly={v.get('apuesta_kelly', 0):.2f}€ activa={v['activa']}")

    return "\n".join(lines)


# ─── Prompt ──────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """Eres un investigador cuantitativo analizando un bot de predicción en Polymarket.
El sistema opera mercados cripto binarios (YES/NO) a corto plazo, principalmente slots de 5 y 15 minutos.

CONTEXTO DEL SISTEMA:
- UPDOWN_GBM: modelo Black-Scholes digital. Feature clave: pct_spot_vs_ref (% que se ha movido el spot desde el precio de referencia del slot). También guarda sigma_h (volatilidad estimada) y T_h (tiempo restante en horas).
- ORDER_FLOW_5M: cumulative delta de Binance (taker_buy - taker_sell) en últimas 5 velas. Feature: delta_ratio (rango -1 a +1) y has_real_flow (1=Binance real, 0=estimado Kraken).
- SMART_FLOW_1H: flujo de wallets en Polymarket. Sin features estructuradas aún.
- WEEKLY_PRICE y PRICE_TARGET_GBM: mercados multi-día, pocas resoluciones.

ARQUITECTURA DE APRENDIZAJE (ya implementada):
El sistema tiene FEATURE_RULES que le indican qué features analizar por estrategia.
Cuando una feature en un rango tiene IC < -0.12 con n≥8 → genera filtro automático (skip).
Cuando IC > +0.12 con n≥8 → genera patrón ganador (kelly_boost).
Lo que TÚ puedes aportar: proponer nuevas features o rangos que el sistema no está analizando.

TU TAREA:
Analiza los datos y propón 2-4 hipótesis concretas y accionables. Para cada una:
1. Qué feature analizar y en qué estrategia
2. Qué condición probar (abs_gt, lt, gt, abs_lt)
3. El razonamiento económico de por qué podría separar wins de losses
4. Evidencia en los datos que te lleva a esa hipótesis (diferencias en promedios de features entre WIN y LOSS)

FORMATO DE SALIDA — responde ÚNICAMENTE con este formato markdown:

### Hipótesis 1: [título breve]
**Feature**: nombre_feature
**Estrategia**: UPDOWN_GBM#5min (o la que sea)
**Condición a probar**: abs_gt 0.003 (o la que corresponda)
**Razonamiento**: [2-3 líneas explicando la lógica económica]
**Evidencia**: [qué ves en los datos que te lleva a esto]
**Prioridad**: Alta / Media / Baja

(repite para cada hipótesis)

### Resumen
[1-2 líneas sobre el patrón más importante que ves en los datos]

IMPORTANTE: Solo propón hipótesis donde veas diferencia real entre WIN_avg y LOSS_avg en los datos. No inventes patrones que no estén en los números."""


def construir_prompt(resumen: str, hipotesis_anteriores: list) -> str:
    prev = ""
    if hipotesis_anteriores:
        prev = "\n## Hipótesis ya propuestas (NO repetir)\n" + "\n".join(f"- {h}" for h in hipotesis_anteriores) + "\n"

    return f"""{prev}
## Datos actuales del sistema

{resumen}

---
Analiza los datos anteriores y propón hipótesis nuevas siguiendo exactamente el formato indicado."""


# ─── Llamada al LLM ─────────────────────────────────────────────────────────

def llamar_llm(prompt: str) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        return "ERROR: ANTHROPIC_API_KEY no configurada. Ejecuta: export ANTHROPIC_API_KEY=sk-ant-..."

    client = anthropic.Anthropic(api_key=api_key)
    mensaje = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )
    return mensaje.content[0].text


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    ts = datetime.now(timezone.utc)
    hoy = ts.strftime("%Y-%m-%d")
    hora = ts.strftime("%H:%M UTC")

    print(f"[{ts.isoformat(timespec='seconds')}] === LLM Hypothesis Generator ===")

    resultados  = cargar_resultados()
    params      = cargar_params()
    performance = cargar_performance()
    anteriores  = cargar_hipotesis_anteriores()

    if len(resultados) < 20:
        print("  Insuficientes datos (<20 resoluciones). Saltando.")
        return

    print(f"  Datos: {len(resultados)} resoluciones, {len(params.get('estrategias', {}))} subtypes en params")
    print(f"  Hipótesis anteriores a evitar: {len(anteriores)}")

    resumen = construir_resumen(resultados, params, performance)
    prompt  = construir_prompt(resumen, anteriores)

    print(f"  Llamando a Claude ({MODEL})...")
    respuesta = llamar_llm(prompt)

    if respuesta.startswith("ERROR"):
        print(f"  {respuesta}")
        return

    # Guardar output
    output_path = OUTPUT_DIR / f"hipotesis_{hoy}.md"
    cabecera = f"# Hipótesis LLM — {hoy} {hora}\n\n"
    cabecera += f"*Generado automáticamente por {MODEL} sobre {len(resultados)} resoluciones*\n\n---\n\n"
    output_path.write_text(cabecera + respuesta, encoding="utf-8")

    print(f"  Guardado: {output_path}")
    print(f"\n{'='*60}")
    print(respuesta)
    print(f"{'='*60}")
    print(f"\n[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] === Fin ===")


if __name__ == "__main__":
    main()
