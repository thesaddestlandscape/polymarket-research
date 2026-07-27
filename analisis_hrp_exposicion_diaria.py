#!/usr/bin/env python3
"""Vigía/análisis read-only (27-Jul, P28 punto 5 -- ver idea_propuesta_hrp_portfolio_23jul):
HRP (Hierarchical Risk Parity, Lopez de Prado) sobre las tuplas live, con
puerta de madurez (>=14 dias de historial Y >=100 trades resueltos en
results.csv, ambas condiciones). Sin puerta, la tupla mas nueva (menos
varianza APARENTE por poco n) se lleva la mayoria del peso -- ya visto:
BALLENAS_TARDIAS#BTC#15min con solo 4 dias se llevaba 86.3%.

Objetivo (paso 3 de la propuesta 23-Jul, el unico seguro de dar sin tocar
dinero): loguear que exposicion agregada REAL tiene cada tupla (trades.csv,
stakes de los ultimos N dias) frente al techo que le asignaria HRP, SIN
aplicar ningun limite -- observacional puro, mismo patron que todo vigia_*
del proyecto. Decision de convertir esto en un techo real de
live_stake.py sigue siendo 100% de Javi, con /code-review antes.

Metodologia (identica a la usada 23-Jul, ahora persistida como script
reproducible en vez de calculo efimero):
  1. pnl_neto diario por tupla (results.csv, agrupado por
     strategy#subtype#decision, sumado por resolution_timestamp[:10]).
  2. Matriz de correlacion de esas series diarias (dias sin trade en una
     tupla = 0, no NaN -- mismo criterio que el calculo original).
  3. Distancia d = sqrt(0.5*(1-corr)), linkage jerarquico (single),
     cuasi-diagonalizacion por orden de la dendrograma, biseccion
     recursiva por varianza inversa de cluster (HRP estandar).
  4. Exposicion real reciente (trades.csv, ultimos EXPOSICION_DIAS dias,
     suma de stake_eur por tupla) vs peso_HRP * presupuesto_total
     (bankroll actual, data/live/balance_real.json).

Solo lectura sobre results.csv/trades.csv/balance_real.json. No escribe en
config_live.json ni toca ninguna decision. Salida: JSON en
data/shadow/hrp_exposicion_diaria.json + resumen por stdout.
"""
import csv
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram

REPO = Path(__file__).resolve().parent
RESULTS = REPO / "data/shadow/results.csv"
TRADES = REPO / "data/live/trades.csv"
CONFIG_LIVE = REPO / "data/live/config_live.json"
BALANCE = REPO / "data/live/balance_real.json"
OUT = REPO / "data/shadow/hrp_exposicion_diaria.json"

MADUREZ_DIAS_MIN = 14
MADUREZ_N_MIN = 100
EXPOSICION_DIAS = 7  # ventana reciente para "exposicion agregada actual"


def _tuplas_live():
    cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
    return cfg.get("pares_permitidos_live", [])


def _clave(tupla_str):
    """'STRATEGY#SUBTYPE#DIRECTION' (3 campos) -- subtype ya trae activo#marco."""
    partes = tupla_str.split("#")
    strategy = partes[0]
    direction = partes[-1]
    subtype = "#".join(partes[1:-1])
    return strategy, subtype, direction


def cargar_pnl_diario(tuplas):
    """Devuelve {tupla: {fecha: pnl_dia}} + {tupla: n_total} + {tupla: fecha_primera}."""
    idx = {}
    for t in tuplas:
        strategy, subtype, direction = _clave(t)
        idx[(strategy, subtype, direction)] = t
    series = {t: defaultdict(float) for t in tuplas}
    conteos = {t: 0 for t in tuplas}
    primeras = {}
    with open(RESULTS, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            k = (r.get("strategy"), r.get("subtype"), r.get("decision"))
            t = idx.get(k)
            if t is None:
                continue
            ts = r.get("resolution_timestamp") or r.get("prediction_timestamp")
            if not ts:
                continue
            fecha = ts[:10]
            pnl = float(r.get("pnl_neto") or 0)
            series[t][fecha] += pnl
            conteos[t] += 1
            if t not in primeras or fecha < primeras[t]:
                primeras[t] = fecha
    return series, conteos, primeras


def dias_historial(fecha_primera):
    if not fecha_primera:
        return 0
    d0 = datetime.strptime(fecha_primera, "%Y-%m-%d")
    return (datetime.now(timezone.utc).replace(tzinfo=None) - d0).days


def matriz_correlacion(series, tuplas_maduras):
    fechas = sorted(set().union(*[series[t].keys() for t in tuplas_maduras]))
    M = np.array([[series[t].get(f, 0.0) for f in fechas] for t in tuplas_maduras])
    corr = np.corrcoef(M)
    corr = np.nan_to_num(corr, nan=0.0)
    return corr


def hrp_pesos(corr, tuplas_maduras, varianzas):
    """HRP estandar: distancia -> linkage -> cuasi-diagonalizacion (orden de
    hojas del dendrograma) -> biseccion recursiva por varianza inversa."""
    n = len(tuplas_maduras)
    if n == 1:
        return {tuplas_maduras[0]: 1.0}
    dist = np.sqrt(np.clip(0.5 * (1 - corr), 0, None))
    condensed = []
    for i in range(n):
        for j in range(i + 1, n):
            condensed.append(dist[i, j])
    Z = linkage(condensed, method="single")
    orden = dendrogram(Z, no_plot=True)["leaves"]

    def biseccion(indices):
        if len(indices) == 1:
            return {indices[0]: 1.0}
        mid = len(indices) // 2
        izq, der = indices[:mid], indices[mid:]
        var_izq = sum(varianzas[i] for i in izq)
        var_der = sum(varianzas[i] for i in der)
        alpha = 1 - var_izq / (var_izq + var_der) if (var_izq + var_der) > 0 else 0.5
        pesos = {}
        pesos.update({k: v * alpha for k, v in biseccion(izq).items()})
        pesos.update({k: v * (1 - alpha) for k, v in biseccion(der).items()})
        return pesos

    pesos_idx = biseccion(orden)
    return {tuplas_maduras[i]: w for i, w in pesos_idx.items()}


def exposicion_reciente(tuplas):
    corte = (datetime.now(timezone.utc).date().toordinal() - EXPOSICION_DIAS)
    exp = {t: 0.0 for t in tuplas}
    idx = {}
    for t in tuplas:
        strategy, subtype, direction = _clave(t)
        idx[(strategy, subtype, direction)] = t
    if not TRADES.exists():
        return exp
    with open(TRADES, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            k = (r.get("strategy"), r.get("subtype"), r.get("direction"))
            t = idx.get(k)
            if t is None:
                continue
            ts = r.get("timestamp_utc")
            if not ts:
                continue
            fecha = datetime.fromisoformat(ts.replace("Z", "+00:00")).date()
            if fecha.toordinal() < corte:
                continue
            try:
                exp[t] += float(r.get("stake_eur") or 0)
            except ValueError:
                pass
    return exp


def main():
    tuplas = _tuplas_live()
    series, conteos, primeras = cargar_pnl_diario(tuplas)

    maduras, inmaduras = [], []
    for t in tuplas:
        dh = dias_historial(primeras.get(t))
        if dh >= MADUREZ_DIAS_MIN and conteos[t] >= MADUREZ_N_MIN:
            maduras.append(t)
        else:
            inmaduras.append((t, dh, conteos[t]))

    resultado = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tuplas_maduras": [],
        "tuplas_inmaduras": [{"tupla": t, "dias_historial": dh, "n": n} for t, dh, n in inmaduras],
    }

    print(f"Maduras ({len(maduras)}/{len(tuplas)}): {maduras}")
    for t, dh, n in inmaduras:
        print(f"  INMADURA {t}: dias={dh} n={n} (necesita >={MADUREZ_DIAS_MIN}d y >={MADUREZ_N_MIN} trades) -- Kelly normal, sin techo HRP")

    if len(maduras) >= 2:
        corr = matriz_correlacion(series, maduras)
        varianzas = []
        for t in maduras:
            vals = list(series[t].values())
            varianzas.append(float(np.var(vals)) if len(vals) > 1 else 1e-9)
        pesos = hrp_pesos(corr, maduras, varianzas)
        exp = exposicion_reciente(tuplas)
        presupuesto_total = sum(exp.get(t, 0.0) for t in maduras) or 1.0

        print(f"\nPesos HRP ({len(maduras)} tuplas maduras) vs exposicion real (ultimos {EXPOSICION_DIAS}d):")
        for t in sorted(pesos, key=lambda k: -pesos[k]):
            share_real = exp.get(t, 0.0) / presupuesto_total if presupuesto_total else 0
            excede = share_real > pesos[t] * 1.5  # umbral de aviso: 50% por encima del techo HRP
            marca = " <-- excede techo HRP x1.5" if excede else ""
            print(f"  {t}: peso_HRP={pesos[t]:.1%}  exposicion_reciente_eur={exp.get(t,0):.2f} ({share_real:.1%} del total){marca}")
            resultado["tuplas_maduras"].append({
                "tupla": t, "peso_hrp": round(pesos[t], 4),
                "exposicion_reciente_eur": round(exp.get(t, 0.0), 2),
                "share_exposicion_reciente": round(share_real, 4),
                "excede_techo_hrp_x1_5": excede,
            })
    else:
        print("\nMenos de 2 tuplas maduras -- no se puede calcular HRP todavia.")

    OUT.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
