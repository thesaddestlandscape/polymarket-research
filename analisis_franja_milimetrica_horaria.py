#!/usr/bin/env python3
"""analisis_franja_milimetrica_horaria.py — Franja milimétrica de ballenas
CRUZADA CON HORA UTC (22-Jul, petición explícita Javi: "hay que instrumentar
por moneda y por franja horaria TODAS las bandas milimétricas que dan pasta
-- no solo la de más carne, sacar TODAS las que tienen carne").

Extiende analisis_franja_milimetrica_ballenas.py / ballenas_observer.py::
_calcular_estado_fino() con una dimensión más: (activo, marco, hora_utc,
banda_precio_fina=0.05) en vez de solo (activo, marco, banda). Reusa
_stats_banda de ballenas_observer.py (misma fórmula z-test, no reinventa).

RIGOR OBLIGATORIO (lección del mismo día, no opcional): el filtro de
concentración de mercado (>=N_MERCADOS_MIN mercados distintos, ningún
mercado >TOP1_MERCADO_MAX% del bucket) es el mismo que atrapó el hallazgo
falso de BTC#5min[0.55,0.60) esta sesión -- sin él, un solo mercado con
muchas wallets puede simular "edge" que en realidad es 1 evento.

Con 5 activos x 5 marcos x 24 horas x ~20 bandas = hasta 12.000 combos
posibles, la inmensa mayoría caerán por n insuficiente -- es exactamente
lo esperado (dividir por hora reparte el mismo histórico en 24 trozos).
Solo se reportan los que sobreviven con n real.

CORRECCIÓN 22-Jul (misma sesión, tras primera corrida): con ~500 combos x
hasta 18 bandas cada uno, esto son miles de tests estadísticos simultáneos.
Un filtro crudo z>=2.0 sin corregir por comparaciones múltiples deja pasar
ruido puro por volumen (a p~0.023 por test, con miles de tests se esperan
decenas de "significativos" falsos solo por azar). Se corrige con
Benjamini-Hochberg FDR -- MISMO método y mismo FDR=0.10 que ya usa
shadow_postmortem.py para el aprendizaje causal en producción (no se
inventa un criterio nuevo, se reutiliza vía `import shadow_postmortem as sp`,
mismo patrón que analisis_gate_riguroso.py). La familia de tests para BH-FDR
es TODA banda con n>=N_MIN_INFORMATIVO y filtro de mercado OK -- no solo las
que ya pasaban z>=2.0 (si se corrige solo sobre los ya-significativos el
control de falsos descubrimientos queda circular y no significa nada).

El p-valor no reutiliza `sp._shuffle_pvalue` tal cual: esa función simula
bajo null "coinflip 50/50" (correcto para el IC del proyecto, que compara
contra una base fija de 0.5). Aquí el null correcto es "el mercado es
eficiente" -- P(acierto)=precio_medio de la banda, que varía banda a banda
(una banda a precio 0.85 acierta ~85% SIN edge, eso no es señal). Se
implementa `_shuffle_pvalue_precio()` local con la misma técnica de
simulación (binomial bajo null, fracción de tiradas que igualan/superan lo
observado) parametrizada con el null correcto -- no un criterio nuevo,
la misma técnica bien parametrizada.

Solo lectura. No decide nada, no toca prob_yes ni ningún gate real.
"""
import csv
import json
from collections import defaultdict, Counter
from datetime import datetime
from pathlib import Path

import numpy as np

import shadow_postmortem as sp  # noqa: E402 -- reusa _benjamini_hochberg/SHUFFLE_FDR
from ballenas_observer import _stats_banda

REPO = Path(__file__).resolve().parent
BALLENAS_HIST = REPO / "data" / "shadow" / "ballenas_timing_history.csv"
OUT = REPO / "data" / "shadow" / "franja_milimetrica_horaria.json"

ACTIVOS = ("BTC", "ETH", "SOL", "XRP", "DOGE")
MARCOS = ("5m", "15m", "60m", "240m", "weekly")
STEP = 0.05
TECHO_SEGURIDAD_BANDA = 0.90  # misma razón que ballenas_observer.py: fee real se come el edge cerca de certeza

# Umbrales -- N_MIN algo más laxo que el n>=40 estándar del proyecto porque
# partir por hora reparte el mismo histórico en 24 trozos; cualquier cosa
# con n<40 se marca explícitamente "exploratorio" en el output, nunca se
# presenta como concluyente (mismo principio que CLAUDE.md: n<15 no concluye).
N_MIN_INFORMATIVO = 15
N_MIN_SOLIDO = 40
Z_MIN = 2.0  # ya no es el gate final -- solo pre-filtro para no simular sobre ruido evidente, ver BH-FDR abajo
TOP1_WALLET_MAX = 0.40
N_MERCADOS_MIN = 10
TOP1_MERCADO_MAX = 0.30
N_SHUFFLE = 5000


def _shuffle_pvalue_precio(n, hit, precio_medio, n_shuffle=N_SHUFFLE):
    """P(hits_simulados/n >= hit) bajo null 'mercado eficiente' (cada trial
    con probabilidad de acierto = precio_medio de la banda, no 0.5) -- misma
    técnica de simulación que sp._shuffle_pvalue, null distinto (ver
    docstring del módulo). Semilla determinista por (n,precio_medio) para
    reproducibilidad exacta entre corridas."""
    if n == 0 or not (0 < precio_medio < 1):
        return 1.0
    seed = (n * 1_000_003 + int(round(precio_medio * 1e6))) % (2**32)
    rng = np.random.default_rng(seed=seed)
    hits_sim = rng.binomial(n, precio_medio, size=n_shuffle)
    aciertos_real = round(hit * n)
    return float(np.mean(hits_sim >= aciertos_real))


def bucket(p):
    return round((p // STEP) * STEP, 3)


def cargar():
    """(activo,marco,hora_utc) -> banda -> {'filas':[...], 'mercados':Counter}."""
    out = defaultdict(lambda: defaultdict(lambda: {"filas": [], "mercados": Counter()}))
    with open(BALLENAS_HIST, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            activo, marco = row.get("activo"), row.get("marco")
            if activo not in ACTIVOS or marco not in MARCOS:
                continue
            try:
                p = float(row["precio"])
                acierto = int(row["acierto"])
                hora = datetime.fromisoformat(row["ts_trade"]).hour
            except (TypeError, ValueError, KeyError):
                continue
            b = bucket(p)
            if b > TECHO_SEGURIDAD_BANDA:
                continue  # ni se calcula -- zona de certeza, fee se come el edge
            clave = (activo, marco, hora)
            d = out[clave][b]
            d["filas"].append({"precio": p, "acierto": bool(acierto), "wallet": row["wallet"]})
            d["mercados"][row.get("condition_id", "")] += 1
    return out


def main():
    datos = cargar()
    print(f"Combos (activo,marco,hora) con datos: {len(datos)}")

    # Fase 1: construir la FAMILIA COMPLETA de tests -- toda banda con
    # n>=N_MIN_INFORMATIVO y filtro de mercado OK, sin pre-filtrar por z.
    # Pre-filtrar aquí por z>=2.0 antes de BH-FDR haría el control de falsos
    # descubrimientos circular (solo se puede corregir sobre TODOS los tests
    # realmente realizados, no sobre el subconjunto que ya parecía bueno).
    familia = []
    for (activo, marco, hora), bandas in datos.items():
        for b, d in bandas.items():
            filas = d["filas"]
            n = len(filas)
            if n < N_MIN_INFORMATIVO:
                continue
            s = _stats_banda(filas)
            if s is None:
                continue
            n_mercados = len(d["mercados"])
            top1_mercado = (d["mercados"].most_common(1)[0][1] / n) if d["mercados"] else 1.0
            # filtro de concentración de mercado -- OBLIGATORIO, ver docstring
            if n_mercados < N_MERCADOS_MIN or top1_mercado > TOP1_MERCADO_MAX:
                continue
            familia.append({
                "clave": f"{activo}#{marco}#h{hora:02d}",
                "banda_lo": b, "banda_hi": round(b + STEP, 3),
                "n": n, "hit": s["hit"], "precio_medio": s["precio_medio"],
                "edge_pp": round((s["hit"] - s["precio_medio"]) * 100, 2),
                "z": s["z"], "n_wallets": s["n_wallets"], "top1_wallet_share": s["top1_share"],
                "n_mercados": n_mercados, "top1_mercado_pct": round(top1_mercado * 100, 1),
                "solido_n40": n >= N_MIN_SOLIDO,
            })

    print(f"Familia completa de tests (n>=15 + filtro mercado OK): {len(familia)}")

    # Fase 2: p-valor por test (shuffle, null = mercado eficiente) + BH-FDR
    # global sobre la familia completa.
    for c in familia:
        c["p_valor"] = _shuffle_pvalue_precio(c["n"], c["hit"], c["precio_medio"])
    pvals = [c["p_valor"] for c in familia]
    sobrevive = sp._benjamini_hochberg(pvals, fdr=sp.SHUFFLE_FDR)
    for c, ok in zip(familia, sobrevive):
        c["sobrevive_fdr"] = ok

    n_pasa_z_crudo = sum(1 for c in familia if c["z"] >= Z_MIN and c["top1_wallet_share"] < TOP1_WALLET_MAX)
    n_sobrevive_fdr = sum(1 for c in familia if c["sobrevive_fdr"])
    print(f"Pasan z>=2.0 sin corregir (crudo, INFLADO por comparaciones múltiples): {n_pasa_z_crudo}")
    print(f"Sobreviven BH-FDR (fdr={sp.SHUFFLE_FDR}) sobre la familia completa: {n_sobrevive_fdr}  <- usar este número")

    # "Carne" real = sobrevive BH-FDR (no solo z>=2.0 crudo). Se conserva
    # top1_wallet_share<TOP1_WALLET_MAX como guardia adicional (BH-FDR
    # controla azar estadístico, no concentración en una sola wallet).
    resultado = {}
    total_bandas_carne = 0
    for c in familia:
        if not (c["sobrevive_fdr"] and c["top1_wallet_share"] < TOP1_WALLET_MAX):
            continue
        clave = c.pop("clave")
        resultado.setdefault(clave, []).append(c)
        total_bandas_carne += 1
    for cs in resultado.values():
        cs.sort(key=lambda c: -c["z"])

    print(f"\nCombos (activo,marco,hora) con al menos 1 banda 'con carne' (post BH-FDR): {len(resultado)}")
    print(f"Total de bandas con carne (todas, no solo la mejor por combo): {total_bandas_carne}")

    solidas = [(k, c) for k, cs in resultado.items() for c in cs if c["solido_n40"]]
    solidas.sort(key=lambda x: -x[1]["z"])
    print(f"\nDe esas, con n>=40 (sólidas, no solo exploratorias): {len(solidas)}")
    print(f"\n{'combo':22} {'banda':14} {'n':>6} {'hit':>7} {'edge_pp':>8} {'z':>7} {'p_valor':>9} {'mercados':>9} {'top1_mkt':>9}")
    for k, c in solidas[:60]:
        print(f"{k:22} [{c['banda_lo']:.2f},{c['banda_hi']:.2f}){'':2} {c['n']:6} {c['hit']*100:6.1f}% "
              f"{c['edge_pp']:+7.2f} {c['z']:7.2f} {c['p_valor']:9.4f} {c['n_mercados']:9} {c['top1_mercado_pct']:8.1f}%")

    OUT.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
