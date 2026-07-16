#!/usr/bin/env python3
"""Read-only: trayectoria de la varianza de pnl por trade, cada 10 N, para
las tuplas EN LIVE (dinero real, trades.csv) y las CANDIDATAS en evaluación
(shadow, results.csv, `candidatos_evaluacion_live` con n_shadow>=30).

Origen (16-Jul, petición Javi tras el análisis de la racha real 09-16Jul):
la varianza por trade es grande (std~1.2-1.9€ frente a medias de +-0.2€), así
que una racha de días negativos puede caer dentro de la varianza normal o
señalar una ruptura real. Este script muestra CÓMO evoluciona esa varianza a
medida que se acumulan datos (N=10,20,30...), en vez de solo el snapshot
actual, para distinguir "siempre fue así de ruidoso" de "se ha vuelto más
ruidoso/ha cambiado de signo recientemente".

LIVE: trayectoria completa (n pequeño, cabe entera).
CANDIDATAS: al ser 82 tuplas con n_shadow>=30, se resume en split-half
(misma disciplina que ic_rolling.py) en vez de volcar cada checkpoint de 10.

No toca dinero ni config. Correr desde la raíz del repo:
  python3 varianza_evolutiva.py            # live + resumen candidatas
  python3 varianza_evolutiva.py --full X   # trayectoria completa de una tupla
                                            # (live o candidata), X="STRATEGY#SUBTYPE#DIR"
"""
import csv
import json
import statistics as st
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data/shadow/results.csv"
TRADES = REPO / "data/live/trades.csv"
CONFIG_LIVE = REPO / "data/live/config_live.json"
OUT_LIVE = REPO / "data/shadow/varianza_evolutiva_live.csv"
OUT_CAND = REPO / "data/shadow/varianza_evolutiva_candidatas.csv"

PASO = 10
N_MIN_CANDIDATA = 30


def _tuplas(campo):
    try:
        cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
        pares = cfg.get(campo, [])
        out = []
        for p in pares:
            partes = p.split("#")
            if len(partes) == 4:
                strategy, activo, dur, direccion = partes
                out.append((strategy, f"{activo}#{dur}", direccion))
        return out
    except Exception:
        return []


def _pnls_reales(strategy, subtype, direccion):
    filas = []
    with open(TRADES, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy") == strategy and r.get("subtype") == subtype
                    and r.get("direction") == direccion and r.get("status") == "CLOSED"):
                try:
                    filas.append((r.get("close_timestamp") or r.get("timestamp_utc", ""),
                                  float(r.get("pnl_neto_eur") or 0)))
                except ValueError:
                    continue
    filas.sort(key=lambda x: x[0])
    return [p for _, p in filas]


def _pnls_shadow(strategy, subtype, direccion):
    filas = []
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy") == strategy and r.get("subtype") == subtype
                    and r.get("decision") == direccion and r.get("pnl_neto") not in ("", None)):
                filas.append((r.get("resolution_timestamp", ""), float(r["pnl_neto"])))
    filas.sort(key=lambda x: x[0])
    return [p for _, p in filas]


def trayectoria(pnls, paso=PASO):
    """Varianza/media/hit acumulados (ventana expansiva) en cada checkpoint
    de `paso` observaciones nuevas."""
    out = []
    for n in range(paso, len(pnls) + 1, paso):
        sub = pnls[:n]
        var = st.variance(sub)
        mean = st.mean(sub)
        hit = sum(1 for p in sub if p > 0) / n * 100
        out.append((n, mean, var, var ** 0.5, hit))
    return out


def split_half(pnls, n_min=N_MIN_CANDIDATA // 2):
    n = len(pnls)
    mid = n // 2
    primera, segunda = pnls[:mid], pnls[mid:]
    if len(primera) < n_min or len(segunda) < n_min:
        return None
    v1, v2 = st.variance(primera), st.variance(segunda)
    m1, m2 = st.mean(primera), st.mean(segunda)
    return {
        "n": n, "n1": len(primera), "var1": v1, "mean1": m1,
        "n2": len(segunda), "var2": v2, "mean2": m2,
        "delta_var": v2 - v1, "delta_mean": m2 - m1,
    }


def imprimir_trayectoria_live():
    print("=" * 100)
    print("LIVE (dinero real, trades.csv) — varianza acumulada cada 10 N")
    print("=" * 100)
    filas_csv = []
    for strategy, subtype, direccion in _tuplas("pares_permitidos_live"):
        pnls = _pnls_reales(strategy, subtype, direccion)
        clave = f"{strategy}#{subtype}#{direccion}"
        if len(pnls) < PASO:
            print(f"{clave}: n={len(pnls)} < {PASO}, sin checkpoints todavia")
            continue
        print(f"\n{clave}  (n total real = {len(pnls)})")
        print(f"  {'N':>4} {'media':>8} {'var':>8} {'std':>8} {'hit%':>6}")
        for n, mean, var, sd, hit in trayectoria(pnls):
            print(f"  {n:4d} {mean:8.4f} {var:8.4f} {sd:8.4f} {hit:6.1f}")
            filas_csv.append([clave, n, round(mean, 4), round(var, 4), round(sd, 4), round(hit, 1)])
    with open(OUT_LIVE, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["par", "n", "media", "var", "std", "hit_pct"])
        w.writerows(filas_csv)
    print(f"\n(volcado completo en {OUT_LIVE.relative_to(REPO)})")


def imprimir_resumen_candidatas():
    print("\n" + "=" * 100)
    print(f"CANDIDATAS (shadow, results.csv, n_shadow>={N_MIN_CANDIDATA}) — split-half de varianza")
    print("=" * 100)
    resultados = []
    for strategy, subtype, direccion in _tuplas("candidatos_evaluacion_live"):
        pnls = _pnls_shadow(strategy, subtype, direccion)
        if len(pnls) < N_MIN_CANDIDATA:
            continue
        sh = split_half(pnls)
        if sh is None:
            continue
        clave = f"{strategy}#{subtype}#{direccion}"
        resultados.append((clave, sh))

    resultados.sort(key=lambda kv: -abs(kv[1]["delta_var"]))
    print(f"{'clave':<55} {'n':>5} {'var1':>7} {'var2':>7} {'d_var':>7} {'mean1':>7} {'mean2':>7} {'d_mean':>7}")
    filas_csv = [["par", "n", "var1", "var2", "delta_var", "mean1", "mean2", "delta_mean"]]
    for clave, sh in resultados:
        print(f"{clave:<55} {sh['n']:5d} {sh['var1']:7.3f} {sh['var2']:7.3f} {sh['delta_var']:+7.3f} "
              f"{sh['mean1']:7.3f} {sh['mean2']:7.3f} {sh['delta_mean']:+7.3f}")
        filas_csv.append([clave, sh["n"], round(sh["var1"], 4), round(sh["var2"], 4),
                           round(sh["delta_var"], 4), round(sh["mean1"], 4), round(sh["mean2"], 4),
                           round(sh["delta_mean"], 4)])
    with open(OUT_CAND, "w", newline="", encoding="utf-8") as f:
        csv.writer(f).writerows(filas_csv)
    print(f"\n{len(resultados)} candidatas con n>={N_MIN_CANDIDATA}. Volcado completo en {OUT_CAND.relative_to(REPO)}")
    print("delta_var = var(2a mitad) - var(1a mitad): positivo = se ha vuelto MAS ruidosa recientemente.")


def main():
    if len(sys.argv) >= 3 and sys.argv[1] == "--full":
        clave = sys.argv[2]
        strategy, subtype, direccion = clave.split("#", 1)[0], None, None
        partes = clave.split("#")
        strategy, activo, dur, direccion = partes[0], partes[1], partes[2], partes[3]
        subtype = f"{activo}#{dur}"
        pnls = _pnls_reales(strategy, subtype, direccion)
        origen = "REAL (trades.csv)"
        if not pnls:
            pnls = _pnls_shadow(strategy, subtype, direccion)
            origen = "SHADOW (results.csv)"
        print(f"{clave} — {origen}, n={len(pnls)}")
        print(f"{'N':>4} {'media':>8} {'var':>8} {'std':>8} {'hit%':>6}")
        for n, mean, var, sd, hit in trayectoria(pnls):
            print(f"{n:4d} {mean:8.4f} {var:8.4f} {sd:8.4f} {hit:6.1f}")
        return 0

    imprimir_trayectoria_live()
    imprimir_resumen_candidatas()
    return 0


if __name__ == "__main__":
    sys.exit(main())
