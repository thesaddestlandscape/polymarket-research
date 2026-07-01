"""
sync_obsidian.py — Genera/actualiza notas de estrategias e hipótesis en el
vault de Obsidian (`second-brain`, repo separado) a partir de
strategy_params.json + hipotesis_custom.json + results.csv.

Diseño (2026-07-01, a petición de Javi: "conecta todo, quiero ver las
conexiones que se generan"):
- Notas de ESTRATEGIA como hubs (09_estrategias/): una por cada
  agregación que tiene sentido propio (top-level, asset, duración —
  deduplicadas cuando son idénticas, ej. ORDER_FLOW_5M solo tiene
  duración 5min → no se genera nota "#5min" redundante con la de arriba).
  Las combinaciones asset+duración exactas (ej. ETH#15min) solo se
  generan si las referencia una hipótesis o superan n≥40 (live-relevante).
- Notas de HIPÓTESIS (10_hipotesis/): una por cada entrada de
  hipotesis_custom.json, evaluada contra results.csv en el momento del
  sync, enlazando a su(s) estrategia(s) objetivo.
- Sin enlaces hipótesis↔hipótesis ni estrategia↔estrategia salvo que haya
  una razón real — el grafo se organiza en racimos (estrategia = centro,
  hipótesis = radios), no como telaraña.
- Estas dos carpetas son generadas: no editar a mano, se sobrescriben
  en cada sync.

No toca nada del pipeline fast/slow — corre por su cron propio
(ver crontab, 1x/día), separado del trading en vivo.
"""
import csv
import json
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

DIR_SHADOW = Path("data/shadow")
RESULTS_PATH = DIR_SHADOW / "results.csv"
PARAMS_PATH = DIR_SHADOW / "strategy_params.json"
HIPOTESIS_PATH = DIR_SHADOW / "hipotesis_custom.json"

VAULT_DIR = Path("/root/second-brain")
DIR_ESTRATEGIAS = VAULT_DIR / "09_estrategias"
DIR_HIPOTESIS = VAULT_DIR / "10_hipotesis"

N_MIN_NOTA = 15          # por debajo de esto, no genera nota de estrategia
N_MIN_ASSET_DURACION = 40  # combinación exacta asset#duración solo si supera esto (o la referencia una hipótesis)

DURACIONES_CONOCIDAS = {"5min", "15min", "60min", "240min", "daily", "atexpiry", "reach"}


def slug(key: str) -> str:
    return key.replace("#", "_")


def cargar_json(path, default):
    if not Path(path).exists():
        return default
    try:
        return json.load(open(path, encoding="utf-8"))
    except Exception:
        return default


def cargar_results():
    if not RESULTS_PATH.exists():
        return []
    with open(RESULTS_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def ic(w, n):
    return ((w + 1) / (n + 2) - 0.5) * min(1.0, n / 20) if n else 0.0


def elegir_notas_estrategia(params: dict, hipotesis: list) -> set:
    """Decide qué keys de strategy_params.json merecen nota propia, deduplicando
    combinaciones asset/duración idénticas cuando la estrategia solo tiene una
    duración posible."""
    top_keys = [k for k in params if "#" not in k]
    duraciones_por_top = defaultdict(set)
    for k in params:
        if "#" not in k:
            continue
        parts = k.split("#")
        base = parts[0]
        for p in parts[1:]:
            if p in DURACIONES_CONOCIDAS:
                duraciones_por_top[base].add(p)

    elegidas = set(top_keys)  # los hubs de estrategia siempre van
    for k, d in params.items():
        if "#" not in k or k in top_keys:
            continue
        n = d.get("n", 0)
        base = k.split("#")[0]
        multi_duracion = len(duraciones_por_top.get(base, set())) > 1
        parts = k.split("#")[1:]
        es_asset_duracion = len(parts) == 2

        if not multi_duracion:
            # única duración posible: solo la key de nivel "asset" (1 '#') es útil,
            # el resto son idénticas al top-level o al nivel asset
            if len(parts) == 1 and parts[0] not in DURACIONES_CONOCIDAS and n >= N_MIN_NOTA:
                elegidas.add(k)
            continue

        if not es_asset_duracion:
            # nivel asset-solo o duración-solo, con múltiples duraciones reales: útil
            if n >= N_MIN_NOTA:
                elegidas.add(k)
        else:
            # asset+duración exacto: solo si es relevante (n alto o referenciado)
            if n >= N_MIN_ASSET_DURACION:
                elegidas.add(k)

    # asegurar que cualquier key referenciada directamente por una hipótesis exista
    for h in hipotesis:
        target = resolver_target(h.get("filtro", {}), params)
        if target:
            elegidas.add(target)

    return elegidas


def resolver_target(filtro: dict, params: dict):
    prefix = filtro.get("strategy_prefix")
    if not prefix:
        return None
    par = filtro.get("par")
    duracion = filtro.get("subtype_contains") if filtro.get("subtype_contains") in DURACIONES_CONOCIDAS else None
    candidatos = []
    if par and duracion:
        candidatos.append(f"{prefix}#{par}#{duracion}")
    if par:
        candidatos.append(f"{prefix}#{par}")
    if duracion:
        candidatos.append(f"{prefix}#{duracion}")
    candidatos.append(prefix)
    for c in candidatos:
        if c in params:
            return c
    return None


def evaluar_hipotesis(h: dict, rows: list):
    filtro = h.get("filtro", {})
    sub = rows
    if filtro.get("strategy_prefix"):
        sub = [r for r in sub if r["strategy"].startswith(filtro["strategy_prefix"])]
    if filtro.get("subtype_contains"):
        sub = [r for r in sub if filtro["subtype_contains"] in r.get("subtype", "")]
    if filtro.get("decision"):
        sub = [r for r in sub if r.get("decision") == filtro["decision"]]
    if filtro.get("par"):
        par = filtro["par"]
        sub = [r for r in sub if par in r.get("subtype", "").upper().split("#")]
    if filtro.get("par_excluir"):
        excl = set(filtro["par_excluir"])
        sub = [r for r in sub if not (excl & set(r.get("subtype", "").upper().split("#")))]
    if filtro.get("hora_utc") is not None:
        h_val = str(filtro["hora_utc"]).zfill(2)
        sub = [r for r in sub if r.get("prediction_timestamp", "")[11:13] == h_val]
    if filtro.get("hora_utc_desde") is not None:
        sub = [r for r in sub if r.get("prediction_timestamp", "")[11:13].isdigit()
               and int(r["prediction_timestamp"][11:13]) >= filtro["hora_utc_desde"]]
    if filtro.get("hora_utc_hasta") is not None:
        sub = [r for r in sub if r.get("prediction_timestamp", "")[11:13].isdigit()
               and int(r["prediction_timestamp"][11:13]) <= filtro["hora_utc_hasta"]]
    if filtro.get("feature"):
        feat = filtro["feature"]
        lo, hi = filtro.get("feature_lo"), filtro.get("feature_hi")

        def _match(r):
            try:
                v = json.loads(r.get("features", "{}")).get(feat)
                v = float(v)
            except (TypeError, ValueError, json.JSONDecodeError):
                return False
            if lo is not None and v < lo:
                return False
            if hi is not None and v >= hi:
                return False
            return True
        sub = [r for r in sub if _match(r)]

    n_h = len(sub)
    if n_h == 0:
        return {"n": 0, "ic": 0.0, "pnl": 0.0, "veredicto": "SIN DATOS"}
    wins = sum(int(r.get("acierto", 0)) for r in sub)
    ic_v = round(ic(wins, n_h), 4)
    pnl_h = round(sum(float(r.get("pnl_neto", 0) or 0) for r in sub), 2)
    umbral_n = h.get("umbral_n", 20)
    ic_min = h.get("umbral_ic_min")
    ic_max = h.get("umbral_ic_max")
    if n_h < umbral_n:
        veredicto = f"EN SEGUIMIENTO (n={n_h}/{umbral_n})"
    elif ic_min and ic_v >= ic_min:
        veredicto = "CONFIRMADA (positiva)"
    elif ic_max is not None and ic_v <= ic_max:
        veredicto = "CONFIRMADA (negativa/filtro)"
    else:
        veredicto = "UMBRAL n CUMPLIDO, IC no confirma"
    return {"n": n_h, "ic": ic_v, "pnl": pnl_h, "veredicto": veredicto}


def escribir_nota_estrategia(key: str, entry: dict, hip_por_target: dict, ts: str):
    lines = [
        f"# Estrategia: {key}",
        "",
        "_Nota generada automáticamente por `sync_obsidian.py` — no editar a mano, "
        "se sobrescribe en cada sync. Fuente: `strategy_params.json` + `results.csv` "
        "del repo `polymarket-research`._",
        "",
        f"## Estado (sync {ts})",
        f"- n = {entry.get('n', 0)}, IC = {entry.get('ic_bayes', 0):+.3f}, "
        f"PNL = {entry.get('pnl_total', 0):+.2f}€, activa: "
        f"{'sí' if entry.get('activa', True) else 'NO'}",
        f"- Motivo: {entry.get('motivo', '')}",
        f"- Kelly: apuesta_kelly={entry.get('apuesta_kelly', 0):.2f}€",
    ]
    if "n_BUY_YES" in entry or "n_BUY_NO" in entry:
        lines.append(
            f"- Por dirección: BUY_YES n={entry.get('n_BUY_YES', 0)} "
            f"IC={entry.get('ic_BUY_YES', 0):+.3f} | "
            f"BUY_NO n={entry.get('n_BUY_NO', 0)} IC={entry.get('ic_BUY_NO', 0):+.3f}"
        )
    calib = entry.get("calibracion_prob")
    if calib:
        lines += [
            "",
            "## Calibración Platt activa",
            f"- p' = Φ({calib['a']:+.2f} + {calib['b']:.2f}·Φ⁻¹(p)) — "
            f"validado con walk-forward (n_oos={calib.get('n_oos_validado', '?')}, "
            f"mejora media={calib.get('mejora_media_oos', '?')})",
            "- Ver [[2026-07-01-recalibracion-platt-prob-yes-modelo]]",
        ]
    filtros = entry.get("filtros_causales", [])
    patrones = entry.get("patrones_ganadores", [])
    if filtros:
        lines += ["", "## Filtros causales (skip)"]
        for f in filtros:
            lines.append(
                f"- `{f.get('feature')}` {f.get('condicion')} {f.get('umbral')} → "
                f"IC_malo={f.get('ic_malo', 0):+.3f} (n={f.get('n_malo', 0)})"
            )
    if patrones:
        lines += ["", "## Patrones ganadores (boost)"]
        for p in patrones:
            lines.append(
                f"- `{p.get('feature')}` {p.get('condicion')} {p.get('umbral')} → "
                f"IC_patron={p.get('ic_patron', 0):+.3f} (n={p.get('n_patron', 0)}), "
                f"kelly_boost=+{p.get('kelly_boost', 0):.2f}€"
            )
    hips = hip_por_target.get(key, [])
    if hips:
        lines += ["", "## Hipótesis relacionadas"]
        for hid in hips:
            lines.append(f"- [[{slug(hid)}]]")
    lines.append("")
    return "\n".join(lines)


def escribir_nota_hipotesis(h: dict, resultado: dict, target: str, ts: str):
    lines = [
        f"# Hipótesis: {h['id']}",
        "",
        "_Nota generada automáticamente por `sync_obsidian.py` — no editar a mano. "
        "Fuente: `hipotesis_custom.json` + `results.csv` del repo `polymarket-research`._",
        "",
        f"## {h.get('nombre', '')}",
        h.get("descripcion", ""),
        "",
        f"## Estado actual (sync {ts})",
        f"- n = {resultado['n']} (umbral: {h.get('umbral_n', '?')})",
        f"- IC = {resultado['ic']:+.3f} "
        f"(umbral_min={h.get('umbral_ic_min')}, umbral_max={h.get('umbral_ic_max')})",
        f"- PNL = {resultado['pnl']:+.2f}€",
        f"- **Veredicto**: {resultado['veredicto']}",
        "",
        "## Acción si se confirma",
        h.get("accion", ""),
    ]
    if target:
        lines += ["", "## Estrategia relacionada", f"- [[{slug(target)}]]"]
    lines.append("")
    return "\n".join(lines)


def main():
    params_raw = cargar_json(PARAMS_PATH, {})
    params = params_raw.get("estrategias", params_raw)
    hipotesis = cargar_json(HIPOTESIS_PATH, {}).get("hipotesis", [])
    rows = cargar_results()
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")

    # Evaluar hipótesis y resolver su target una vez
    hip_evaluadas = []
    hip_por_target = defaultdict(list)
    for h in hipotesis:
        resultado = evaluar_hipotesis(h, rows)
        target = resolver_target(h.get("filtro", {}), params)
        hip_evaluadas.append((h, resultado, target))
        if target:
            hip_por_target[target].append(h["id"])

    claves_estrategia = elegir_notas_estrategia(params, hipotesis)

    DIR_ESTRATEGIAS.mkdir(parents=True, exist_ok=True)
    DIR_HIPOTESIS.mkdir(parents=True, exist_ok=True)

    for k in claves_estrategia:
        entry = params.get(k, {})
        contenido = escribir_nota_estrategia(k, entry, hip_por_target, ts)
        (DIR_ESTRATEGIAS / f"{slug(k)}.md").write_text(contenido, encoding="utf-8")

    for h, resultado, target in hip_evaluadas:
        contenido = escribir_nota_hipotesis(h, resultado, target, ts)
        (DIR_HIPOTESIS / f"{slug(h['id'])}.md").write_text(contenido, encoding="utf-8")

    print(f"  {len(claves_estrategia)} notas de estrategia, {len(hip_evaluadas)} notas de hipótesis escritas.")

    # git add/commit/push solo si hay cambios reales
    subprocess.run(["git", "pull", "--rebase", "--autostash"], cwd=VAULT_DIR, check=False)
    subprocess.run(["git", "add", "09_estrategias", "10_hipotesis"], cwd=VAULT_DIR, check=True)
    diff = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=VAULT_DIR)
    if diff.returncode == 0:
        print("  Sin cambios respecto al último sync.")
        return
    subprocess.run(
        ["git", "commit", "-m", f"sync: estrategias e hipótesis ({ts})"],
        cwd=VAULT_DIR, check=True,
    )
    subprocess.run(["git", "push"], cwd=VAULT_DIR, check=True)
    print("  Cambios commiteados y pusheados al vault.")


if __name__ == "__main__":
    main()
