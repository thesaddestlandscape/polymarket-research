#!/usr/bin/env python3
"""
analisis_gate_bucket_kelly_24ago.py — gate de CRECIMIENTO LOGARÍTMICO
(Kelly, g(f)) por MICRO-BUCKET de precio, mismo rigor exacto que
gate_bucket_propio.py (Wilson/bootstrap+shuffle+split-half+BH-FDR por
familia+moneda) pero sobre g(f) en vez de pnl_neto.

Motivo (petición explícita Javi, 24-Ago, "necesitamos más mecanismos para
eliminar el payout inverso... no hay más margen para cagadas"): hueco real
encontrado al auditar el sistema -- `gate_bucket_propio.py` confirma
buckets por PnL LINEAL medio (EV por trade), y `analisis_log_growth.py`
(vigia_log_growth) mide g(f) pero SOLO agregado por tupla completa. NINGÚN
mecanismo existente comprueba g(f) por micro-bucket. Esto importa porque
un bucket puede tener pnl_medio>0 (EV lineal positivo) y aun así g(f)<0
-- payout inverso real: hit-rate alto con pérdidas grandes y poco
frecuentes que se comen el compounding, exactamente el patrón que ya
tumbó FAVORITO_CONFIRMADO#{BTC,SOL,ETH}#15min#BUY_NO en 17-Jul (ver
CLAUDE.md). Si el payout inverso vive concentrado en una franja de precio
(zona "ya confirmada", py alto) dentro de una tupla que en otras franjas
SÍ crece, pausar la tupla ENTERA (lo único que se hacía hasta hoy) tira
también la parte buena -- el micro-bucket es más quirúrgico, mismo
principio que ya demostró gate_bucket_propio con el PnL lineal.

Fórmula de retorno: IDÉNTICA a analisis_log_growth.py (misma convención
SLIPPAGE, mismo clamp) -- la fracción de retorno de una apuesta binaria no
depende del stake real, así todas las tuplas/buckets son comparables:
  gana: r = (1-p)/p - SLIPPAGE      pierde: r = -1 - SLIPPAGE
  g_i = ln(1 + f * r_i),  f = max_pct_bankroll_por_trade (config_live.json)

Reutiliza (import directo, sin duplicar lógica) de
analisis_gate_bucket_propio_28jul.py: cargar_tuplas_live(), bucket(),
shuffle_test(), bh_fdr_signif(), las constantes TWAP y _marco_de_subtype
-- el bucketing (grid 0.05 sobre precio_yes_mercado RAW, sin flipar
BUY_NO) y el filtro TWAP tienen que ser EXACTAMENTE los mismos que
gate_bucket_propio.json para que ambos gates hablen de la MISMA celda.

⚠️ FASE 0 -- SOLO OBSERVACIONAL. Este script y su JSON de salida
(data/shadow/gate_bucket_kelly.json) NO están conectados a
gate_bucket_propio.evaluar() ni a ningún ejecutor todavía -- tocar el
motor de decisión compartido por estrategias live exige diseño cuidadoso
+ /code-review antes de commitear (CLAUDE.md, "código compartido"), no un
parche apresurado. El propósito de esta primera pasada es MEDIR dónde
vive el payout inverso a resolución de micro-bucket con datos reales,
antes de decidir cómo conectarlo.

Uso:
  python3 analisis_gate_bucket_kelly_24ago.py            # todas las tuplas (live+candidatos)
  python3 analisis_gate_bucket_kelly_24ago.py --live-only # solo pares_permitidos_live
"""
import csv
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_gate_bucket_propio_28jul import (  # noqa: E402
    bucket, shuffle_test, bh_fdr_signif, cargar_tuplas_live,
    _marco_de_subtype, FECHA_CAMBIO_TWAP, MARCOS_TWAP_AFECTADOS,
    FECHA_CAMBIO_TWAP_5MIN_60S, N_MIN, P_MAX,
)
from kelly_precio_gate import _familia  # noqa: E402
from datetime import datetime  # noqa: E402

RESULTS = REPO / "data/shadow/results.csv"
CONFIG_LIVE = REPO / "data/live/config_live.json"
OUT = REPO / "data/shadow/gate_bucket_kelly.json"
SLIPPAGE = 0.02  # misma constante que analisis_log_growth.py/shadow_resolve.py


def _retorno(py: float, decision: str, acierto: str) -> float:
    p = min(0.99, max(0.01, py))
    if decision == "BUY_NO":
        p = 1 - p
    if acierto == "1":
        return (1 - p) / p - SLIPPAGE
    return -1 - SLIPPAGE


def cargar_filas_g(tuplas, f: float):
    """(ts, py_bucket_key, g) por tupla -- misma exclusión TWAP EXACTA que
    analisis_gate_bucket_propio_28jul.py::cargar_filas(), pero devuelve g
    (crecimiento logarítmico de esa fila a la fracción f) en vez de
    pnl_neto. El bucket se calcula sobre precio_yes_mercado RAW (igual que
    el gate de PnL) para que las celdas coincidan 1:1 entre ambos JSON."""
    claves = {(s, sub, d): t for s, sub, d, t, _ in tuplas}
    marco_por_tupla = {t: _marco_de_subtype(sub) for _, sub, _, t, _ in tuplas}
    out = defaultdict(list)
    n_excluidas = 0
    with open(RESULTS, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row.get("acierto") not in ("0", "1"):
                continue
            clave = (row["strategy"], row["subtype"], row["decision"])
            t = claves.get(clave)
            if t is None:
                continue
            marco_t = marco_por_tupla.get(t)
            if marco_t in MARCOS_TWAP_AFECTADOS:
                try:
                    ts_dt = datetime.fromisoformat(row.get("prediction_timestamp", ""))
                except Exception:
                    continue
                corte = FECHA_CAMBIO_TWAP_5MIN_60S if marco_t == "5min" else FECHA_CAMBIO_TWAP
                if ts_dt < corte:
                    n_excluidas += 1
                    continue
            try:
                py = float(row["precio_yes_mercado"])
            except Exception:
                continue
            r = _retorno(py, row["decision"], row["acierto"])
            g = math.log(1 + f * r)
            out[t].append((row.get("prediction_timestamp", ""), py, g))
    if n_excluidas:
        print(f"[cargar_filas_g] {n_excluidas} filas pre-TWAP excluidas en marcos afectados")
    return out


def main():
    live_only = "--live-only" in sys.argv
    with open(CONFIG_LIVE, encoding="utf-8") as fh:
        f = json.load(fh).get("riesgo", {}).get("max_pct_bankroll_por_trade", 0.10)

    tuplas = cargar_tuplas_live()
    if live_only:
        tuplas = [t for t in tuplas if t[4]]
    filas_por_tupla = cargar_filas_g(tuplas, f)
    n_live = sum(1 for *_, es_live in tuplas if es_live)
    print(f"Tuplas a evaluar: {len(tuplas)} ({n_live} live, {len(tuplas) - n_live} candidatos), f={f:.0%}")

    pendientes = []
    resultado = {}
    for i, (strategy, subtype, decision, tupla_str, es_live) in enumerate(tuplas):
        if i % 25 == 0:
            print(f"  ... {i}/{len(tuplas)} tuplas procesadas (pasada 1/2)", flush=True)
        filas = filas_por_tupla.get(tupla_str, [])
        if len(filas) < N_MIN:
            resultado[tupla_str] = {}
            continue

        por_bucket = defaultdict(list)
        for ts, py, g in filas:
            por_bucket[bucket(py)].append((ts, g))

        tabla = {}
        for b in sorted(por_bucket):
            dentro = por_bucket[b]
            fuera = [(ts, g) for bb, fs in por_bucket.items() if bb != b for ts, g in fs]
            n_d = len(dentro)
            g_d = [g for _, g in dentro]
            g_f = [g for _, g in fuera]
            media_d = sum(g_d) / n_d

            entrada = {"n": n_d, "g_medio": round(media_d, 6),
                       "diff_vs_resto": round(media_d - (sum(g_f) / len(g_f)), 6) if g_f else None,
                       "shuffle_p": None, "split_half_diff": None,
                       "ci90_bootstrap_absoluto": None, "veredicto": "sin_concluir"}
            tabla[f"{b:.2f}"] = entrada

            if n_d >= N_MIN and g_f:
                diff, p_valor = shuffle_test(g_d, g_f)
                entrada["shuffle_p"] = round(p_valor, 4)
                g_d_arr = np.asarray(g_d, dtype=np.float64)
                rng = np.random.default_rng(42)
                boots = g_d_arr[rng.integers(0, n_d, size=(2000, n_d))].mean(axis=1)
                boots.sort()
                ci_lo90 = float(boots[int(0.05 * len(boots))])
                ci_hi90 = float(boots[int(0.95 * len(boots))])
                entrada["ci90_bootstrap_absoluto"] = [round(ci_lo90, 6), round(ci_hi90, 6)]
                dentro_sorted = sorted(dentro, key=lambda x: x[0])
                mid = n_d // 2
                m1, m2 = dentro_sorted[:mid], dentro_sorted[mid:]
                if len(m1) >= 5 and len(m2) >= 5:
                    d1 = sum(g for _, g in m1) / len(m1) - sum(g_f) / len(g_f)
                    d2 = sum(g for _, g in m2) / len(m2) - sum(g_f) / len(g_f)
                    entrada["split_half_diff"] = [round(d1, 6), round(d2, 6)]
                    consistente = (d1 < 0 and d2 < 0) or (d1 > 0 and d2 > 0)
                    if consistente:
                        pendientes.append({"tupla_str": tupla_str, "bucket": f"{b:.2f}", "entrada": entrada,
                                            "p": p_valor, "diff": diff, "es_live": es_live})
        resultado[tupla_str] = tabla

    por_familia_moneda = defaultdict(list)
    for idx, p in enumerate(pendientes):
        partes = p["tupla_str"].split("#")
        strategy = partes[0]
        activo = partes[1] if len(partes) > 1 else "?"
        clave = (_familia(strategy), activo)
        por_familia_moneda[clave].append(idx)

    sobreviven = set()
    for (familia, activo), indices in por_familia_moneda.items():
        p_valores_grupo = [pendientes[i]["p"] for i in indices]
        sobreviven_grupo = bh_fdr_signif(p_valores_grupo, q=P_MAX)
        sobreviven |= {indices[j] for j in sobreviven_grupo}
        print(f"  familia={familia} activo={activo}: {len(indices)} tests candidatos, "
              f"{len(sobreviven_grupo)} sobreviven BH-FDR q={P_MAX}")

    print(f"\nTests candidatos: {len(pendientes)} | sobreviven BH-FDR (por familia+moneda): {len(sobreviven)}")

    veredictos_nuevos = []
    payout_inverso_encontrado = []
    for idx, p in enumerate(pendientes):
        if idx not in sobreviven:
            continue
        ci = p["entrada"]["ci90_bootstrap_absoluto"]
        if p["diff"] < 0:
            veredicto = "malo_confirmado"
        elif p["entrada"]["g_medio"] >= 0 and ci is not None and ci[0] > 0:
            veredicto = "bueno_confirmado"
        else:
            continue
        p["entrada"]["veredicto"] = veredicto
        marca = "🔴" if veredicto == "malo_confirmado" else "🟢"
        etiqueta = "LIVE" if p["es_live"] else "candidato"
        b = p["bucket"]
        linea = (f"{marca} [{etiqueta}] {p['tupla_str']} [{b},{float(b)+0.05:.2f}) "
                 f"n={p['entrada']['n']} g_medio={p['entrada']['g_medio']:+.5f} "
                 f"p={p['p']:.4f} {veredicto}")
        veredictos_nuevos.append(linea)
        if veredicto == "malo_confirmado" and p["es_live"]:
            payout_inverso_encontrado.append(linea)

    print(f"\n{len(veredictos_nuevos)} bucket(s) con veredicto final tras BH-FDR:")
    for linea in veredictos_nuevos:
        print(f"  {linea}")

    if payout_inverso_encontrado:
        print(f"\n🚨 {len(payout_inverso_encontrado)} bucket(s) LIVE con payout inverso CONFIRMADO "
              f"por micro-bucket (g(f) significativamente negativo, no solo pnl):")
        for linea in payout_inverso_encontrado:
            print(f"  {linea}")

    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(resultado, fh, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
