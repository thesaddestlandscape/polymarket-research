#!/usr/bin/env python3
"""Diagrama de calibración (reliability diagram) — Parte 6 del artículo
bayesiano del 12-Jul: ¿el prob_yes_modelo que reporta cada estrategia
coincide con la frecuencia REAL observada, o solo suena convincente?

Complementa Brier/log_loss (métricas agregadas, un solo número) con la
forma del error: bins de confianza (distancia a 0.5, normalizada a la
dirección de la decisión) vs frecuencia real de acierto en cada bin.
Un gap sistemático en los bins de ALTA confianza es el patrón que ya nos
costó dinero esta sesión (FAVORITO_CONFIRMADO: 60% hit reportado, pnl
negativo en ejecución real — sobreconfianza, no falta de acierto).

Desagregado por (estrategia, activo) — nunca solo agregado, regla de la
sesión. n≥15 por bin (regla n-por-capa). Solo lectura, no toca dinero.
"""
import csv
import json
from collections import defaultdict
from pathlib import Path

RESULTS = Path("data/shadow/results.csv")
OUT = Path("data/shadow/calibracion_reliability.json")
N_MIN_BIN = 15
N_MIN_GRUPO = 30
BINS = [(0.5, 0.6), (0.6, 0.7), (0.7, 0.8), (0.8, 0.9), (0.9, 1.001)]


def confianza_normalizada(prob_yes_modelo, decision):
    """prob_yes_modelo siempre es P(YES) — para juzgar calibración de la
    decisión TOMADA hay que normalizar: BUY_YES usa p tal cual, BUY_NO usa
    1-p (su confianza real es en el NO, no en el YES)."""
    try:
        p = float(prob_yes_modelo)
    except (TypeError, ValueError):
        return None
    if decision == "BUY_YES":
        return p
    if decision == "BUY_NO":
        return 1 - p
    return None


def main():
    rows = list(csv.DictReader(open(RESULTS, encoding="utf-8")))
    grupos = defaultdict(list)
    for r in rows:
        strat = r.get("strategy", "")
        subtype = r.get("subtype", "") or ""
        activo = subtype.split("#")[0] if subtype else "SIN_ACTIVO"
        dec = r.get("decision", "")
        conf = confianza_normalizada(r.get("prob_yes_modelo"), dec)
        if conf is None:
            continue
        try:
            acierto = int(r.get("acierto"))
        except (TypeError, ValueError):
            continue
        grupos[(strat, activo)].append((conf, acierto))

    resultado = {}
    peores_gaps = []
    for (strat, activo), datos in sorted(grupos.items()):
        if len(datos) < N_MIN_GRUPO:
            continue
        filas_bin = []
        for lo, hi in BINS:
            sub = [(c, a) for c, a in datos if lo <= c < hi]
            if len(sub) < N_MIN_BIN:
                continue
            pred_media = sum(c for c, a in sub) / len(sub)
            realizado = sum(a for c, a in sub) / len(sub)
            gap = pred_media - realizado
            fila = {"bin": f"[{lo:.1f},{hi:.1f})", "n": len(sub),
                    "predicho": round(pred_media, 4), "realizado": round(realizado, 4),
                    "gap": round(gap, 4)}
            filas_bin.append(fila)
            if lo >= 0.7:  # solo bins de convicción alta interesan para "sobreconfianza"
                peores_gaps.append((strat, activo, fila["bin"], fila["n"], gap))
        if filas_bin:
            resultado[f"{strat}#{activo}"] = filas_bin

    OUT.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[calibracion] {len(resultado)} grupos (estrategia#activo) con n>={N_MIN_GRUPO}, guardado en {OUT}")
    print("\n=== Peores gaps en convicción ALTA (bins >=0.7, predicho-realizado) ===")
    peores_gaps.sort(key=lambda x: -abs(x[-1]))
    for strat, activo, b, n, gap in peores_gaps[:15]:
        marca = "🔴 SOBRECONFIANZA" if gap > 0.05 else ("🟡 infraconfianza" if gap < -0.05 else "ok")
        print(f"  {strat:28s} {activo:6s} {b:12s} n={n:4d} gap={gap:+.4f} {marca}")


if __name__ == "__main__":
    main()
