#!/usr/bin/env python3
"""
analisis_ic_fillable.py — Punto 2 de la lista Shannon (17-Jul, ver
project_checkpoint_sesion_17jul.md): IC Bayesiano condicionado al canal
REALMENTE ejecutable, por tupla EXACTA strategy#subtype#decision.

Motivo: Kelly (live_stake.py, vía _ic_n_para_subtype en live_trade.py) usa
ic_BUY_YES/ic_BUY_NO de strategy_params.json, calculado sobre TODAS las
resoluciones shadow -- un canal que casi nunca coincide con lo que de
verdad se puede ejecutar. El propio CLAUDE.md lo documenta: "la conversión
medida ronda el 8% y las señales vetadas por profundidad aciertan MÁS que
las ejecutadas (selección adversa)". Este análisis recalcula el MISMO
ic_bayes/ic_efectivo (fórmula exacta de shadow_postmortem.py:
ic_bayes=(aciertos+1)/(n+2)-0.5, confianza=min(1,n/20)) pero solo sobre
el subconjunto fillable, para comparar contra el IC que Kelly usa hoy:

  - tuplas ya en pares_permitidos_live: cruza trades.csv real (CLOSED, sin
    maker_pilot) contra results.csv -- verdad de terreno, no un proxy.
  - cualquier tupla (via CLI): libro_snapshots.csv con
    motivo=candidato_evaluacion + ratio_vs_stake>=5x, mismo proxy que
    vigia_causal_vs_fillable.py.

Diferencia con causal_fillability_real.json (vigia_causal_vs_fillable.py):
esa vigía colapsa por "activo" (pool 15min+60min+5min juntos) porque su
objetivo es cruzar patrones causales. Aquí se necesita el subtype EXACTO
(BTC#15min, no solo BTC) porque así es como Kelly indexa el IC en
strategy_params.json -- pool por marco temporal distorsionaría la
comparación.

Reutiliza RATIO_MIN/N_MIN_CAPA de vigia_causal_vs_fillable.py (mismos
umbrales, sin redefinir constantes por duplicado).

Uso:
  python3 analisis_ic_fillable.py                        # las 9 tuplas live
  python3 analisis_ic_fillable.py <strategy> <subtype> <decision>  # cualquier tupla (usa proxy candidato_evaluacion)

Solo lectura -- NO es cron, NO escribe nada, NO toca dinero ni pares_permitidos_live.
"""
import csv
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from vigia_causal_vs_fillable import RATIO_MIN, N_MIN_CAPA, _perm_pvalue  # noqa: E402

RESULTS = REPO / "data" / "shadow" / "results.csv"
LIBRO = REPO / "data" / "live" / "libro_snapshots.csv"
TRADES = REPO / "data" / "live" / "trades.csv"
CONFIG_LIVE = REPO / "data" / "live" / "config_live.json"
STRATEGY_PARAMS = REPO / "data" / "shadow" / "strategy_params.json"


def ic_bayes(aciertos: int, n: int):
    """Misma fórmula que shadow_postmortem.py: Bayes Beta(1,1) implícito +
    confianza saturando en n=20 (ic_efectivo es lo que consume Kelly)."""
    if n == 0:
        return None, None, None
    ic = (aciertos + 1) / (n + 2) - 0.5
    confianza = min(1.0, n / 20)
    return round(ic, 4), round(confianza, 4), round(ic * confianza, 4)


def _resultado_idx(strategy: str, subtype: str, decision: str) -> dict:
    idx = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["strategy"] == strategy and r["subtype"] == subtype and r["decision"] == decision:
                idx[r["market_id"]] = r
    return idx


def shadow_rows(strategy: str, subtype: str, decision: str) -> list:
    return [r for r in _resultado_idx(strategy, subtype, decision).values()
            if r.get("acierto") in ("0", "1")]


def fillable_rows(strategy: str, subtype: str, decision: str, idx: dict) -> list:
    """Proxy candidato_evaluacion + ratio_vs_stake>=RATIO_MIN, cruzado contra
    el resultado real (mismo mercado) -- igual que cargar_fillable() de
    vigia_causal_vs_fillable.py pero sin colapsar el subtype a activo."""
    if not LIBRO.exists():
        return []
    rows = []
    with open(LIBRO, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("motivo") != "candidato_evaluacion" or r.get("strategy") != strategy
                    or r.get("subtype") != subtype or r.get("direction") != decision):
                continue
            try:
                ratio = float(r.get("ratio_vs_stake") or 0)
            except ValueError:
                ratio = 0
            if ratio < RATIO_MIN:
                continue
            row = idx.get(r["market_id"])
            if row and row.get("acierto") in ("0", "1"):
                rows.append(row)
    return rows


def ejecutado_rows(strategy: str, subtype: str, decision: str, idx: dict) -> list:
    """Verdad de terreno: trades.csv real, CLOSED, sin maker_pilot (mismo
    criterio que cargar_ejecutado_real() de vigia_causal_vs_fillable.py) --
    el acierto/pnl se toma de results.csv (idx), no de trades.csv, para usar
    la misma fuente/metodología que el resto del sistema."""
    if not TRADES.exists():
        return []
    rows = []
    with open(TRADES, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy") == strategy and r.get("subtype") == subtype
                    and r.get("direction") == decision and r.get("status") == "CLOSED"
                    and "maker_pilot=1" not in (r.get("notas") or "")):
                row = idx.get(r.get("market_id"))
                if row and row.get("acierto") in ("0", "1"):
                    rows.append(row)
    return rows


def resumen(rows: list) -> dict:
    n = len(rows)
    if n == 0:
        return {"n": 0}
    aciertos = sum(1 for r in rows if r["acierto"] == "1")
    ic, confianza, ic_efectivo = ic_bayes(aciertos, n)
    pnl = sum(float(r.get("pnl_neto", 0) or 0) for r in rows)
    return {"n": n, "hit_pct": round(100 * aciertos / n, 1), "ic_bayes": ic,
            "confianza": confianza, "ic_efectivo": ic_efectivo,
            "pnl_medio": round(pnl / n, 4)}


def evaluar(strategy: str, subtype: str, decision: str, usar_ejecutado: bool) -> dict:
    """Para tuplas live devuelve las 3 capas (shadow completo, proxy
    candidato_evaluacion, ejecutado real) -- el proxy tiene mucho más n que
    trades.csv real (32-151 vs 0-4 por tupla, 17-Jul) y sirve de puente
    mientras n real crece; para candidatas (CLI) solo shadow+proxy."""
    idx = _resultado_idx(strategy, subtype, decision)
    sh = resumen(list(idx.values()))
    pr = resumen(fillable_rows(strategy, subtype, decision, idx))
    out = {"shadow": sh, "proxy": pr}
    if usar_ejecutado:
        out["ejecutado"] = resumen(ejecutado_rows(strategy, subtype, decision, idx))
    return out


def _p_shuffle_divergencia(strategy: str, subtype: str, decision: str) -> float:
    """Test de permutación (feedback_shuffle_antes_de_bloquear: gap+mayoría
    no es prueba) sobre pnl_neto fillable vs el resto del universo shadow --
    mismo método que vigia_causal_vs_fillable._perm_pvalue. Solo se llama
    para divergencias ya detectadas (evita 2000 shuffles por tupla sana)."""
    idx = _resultado_idx(strategy, subtype, decision)
    fill = fillable_rows(strategy, subtype, decision, idx)
    fill_ids = {id(r) for r in fill}
    resto = [r for r in idx.values() if r.get("acierto") in ("0", "1") and id(r) not in fill_ids]
    if len(fill) < 5 or len(resto) < 5:
        return 1.0
    return _perm_pvalue([float(r["pnl_neto"]) for r in fill], [float(r["pnl_neto"]) for r in resto])


def _ic_kelly_actual(params: dict, strategy: str, subtype: str, decision: str):
    """El IC que Kelly usaría HOY vía live_trade.py::_ic_n_para_subtype --
    misma jerarquía de claves (subtype exacto > activo > decision > estrategia),
    solo lectura, no reimplementa el fallback de patrones causales (irrelevante
    para esta comparación de referencia)."""
    activo = subtype.split("#", 1)[0] if "#" in subtype else subtype
    for k in (f"{strategy}#{subtype}", f"{strategy}#{activo}", strategy):
        p = params.get(k)
        if not p:
            continue
        campo_ic, campo_n = (("ic_BUY_NO", "n_BUY_NO") if decision == "BUY_NO"
                              else ("ic_BUY_YES", "n_BUY_YES"))
        if p.get(campo_ic) is not None and p.get(campo_n, 0) >= 40:
            return p[campo_ic], p[campo_n], k
        return p.get("ic_bayes"), p.get("n"), k
    return None, None, None


def _fmt(d: dict) -> str:
    if d.get("n", 0) == 0:
        return f"{'n=0':>28s}"
    if d["n"] < N_MIN_CAPA:
        return f"n={d['n']:<4d} (⚠ n<{N_MIN_CAPA}, no concluye){' '*4}"
    return f"n={d['n']:<4d} hit={d['hit_pct']:5.1f}% ic_efectivo={d['ic_efectivo']:+.4f}"


def main():
    params = json.loads(STRATEGY_PARAMS.read_text()).get("estrategias", {})

    if len(sys.argv) >= 4:
        tuplas = [(sys.argv[1], sys.argv[2], sys.argv[3], False)]
    else:
        config = json.loads(CONFIG_LIVE.read_text())
        tuplas = []
        for t in config.get("pares_permitidos_live", []):
            strategy, resto = t.split("#", 1)
            subtype, decision = resto.rsplit("#", 1)
            tuplas.append((strategy, subtype, decision, True))

    print(f"{'tupla':46s} {'IC Kelly hoy (shadow)':32s} {'PROXY fillable':30s} {'EJECUTADO real':30s}")
    print("-" * 142)
    divergencias = []
    for strategy, subtype, decision, usar_ejecutado in tuplas:
        tup = f"{strategy}#{subtype}#{decision}"
        r = evaluar(strategy, subtype, decision, usar_ejecutado)
        ic_kelly, n_kelly, clave = _ic_kelly_actual(params, strategy, subtype, decision)
        kelly_str = f"{ic_kelly:+.4f} (n={n_kelly})" if ic_kelly is not None else "sin dato"
        ejec_str = _fmt(r["ejecutado"]) if "ejecutado" in r else "  (solo candidata)"
        print(f"{tup:46s} {kelly_str:32s} {_fmt(r['proxy']):30s} {ejec_str:30s}")

        sh, pr = r["shadow"], r["proxy"]
        if sh.get("n", 0) >= N_MIN_CAPA and pr.get("n", 0) >= N_MIN_CAPA:
            gap = pr["ic_efectivo"] - sh["ic_efectivo"]
            if (pr["ic_efectivo"] < 0 <= sh["ic_efectivo"]) or abs(gap) >= 0.10:
                divergencias.append((tup, sh, pr, gap))

    if divergencias:
        print("\n⚠️  Divergencias candidatas shadow vs PROXY fillable (ambas capas n>=15, gap>=0.10 o cruce de signo)"
              " -- con test de permutación (feedback_shuffle_antes_de_bloquear, no concluir sin esto):")
        for tup, sh, pr, gap in divergencias:
            strategy, resto = tup.split("#", 1)
            subtype, decision = resto.rsplit("#", 1)
            p = _p_shuffle_divergencia(strategy, subtype, decision)
            veredicto = "🔴 REAL (p<0.10)" if p < 0.10 else "gris, no concluye (p>=0.10)"
            print(f"  {tup}: shadow ic_efectivo={sh['ic_efectivo']:+.4f} (n={sh['n']}) "
                  f"vs proxy fillable ic_efectivo={pr['ic_efectivo']:+.4f} (n={pr['n']})  "
                  f"gap={gap:+.4f}  p_shuffle={p:.4f} -> {veredicto}")
    else:
        print("\nSin divergencias con n>=15 en ambas capas (shadow vs proxy fillable).")
    print("\nColumna EJECUTADO real: trades.csv de verdad -- casi todas las tuplas tienen n<15 "
          "todavía (promociones recientes), no concluye por sí sola pero es la referencia a vigilar "
          "según crezca. La columna PROXY (candidato_evaluacion+ratio>=5x) es la aproximación con más "
          "dato disponible HOY -- ver vigia_causal_vs_fillable.py para el razonamiento de por qué es fiable.")


if __name__ == "__main__":
    main()
