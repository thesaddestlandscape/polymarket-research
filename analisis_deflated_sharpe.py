#!/usr/bin/env python3
"""Read-only: corrección por tests múltiples (propuesta #23, backlog
quant-desk 13-jul, inspirado en Deflated Sharpe Ratio / Probability of
Backtest Overfitting, Bailey & Lopez de Prado). Afina la propuesta #6 (ya
cubierta por analisis_gate_riguroso.py, Wilson+shuffle sobre UNA hipótesis):
esto corrige el umbral de significancia por CUÁNTAS hipótesis se han
probado en total. Con 191 claves en strategy_params.json + 53 hipótesis en
hipotesis_custom.json, la probabilidad de que ALGUNA parezca buena por puro
azar sube con cada intento — ningún gate del proyecto corregía por eso.

Adaptación al dominio (no hay retornos continuos, hay win-rate binario):
en vez de Sharpe ratio, se usa el z-score del hit-rate contra 0.5 (mismo
espíritu, misma matemática de fondo — ambos son "cuántas desviaciones
típicas por encima del azar"). Bajo la hipótesis nula (sin ventaja
genuina), el MÁXIMO z-score esperado entre N intentos independientes NO es
1.645 (percentil 95 de un solo test) sino que crece con sqrt(2*ln(N))
(resultado clásico de valores extremos para el máximo de N gaussianas
i.i.d.). Comparar cada bucket contra ESE umbral corregido, no contra el de
un solo test, es la versión mínima viable de DSR/PBO para este proyecto.

N usado: nº de claves en strategy_params.json (cada una es, en la práctica,
un bucket sobre el que se ha mirado el IC al menos una vez) — conservador
(más alto que solo las tuplas whitelisted/candidatas), da el umbral más
exigente posible con datos reales del propio proyecto, no un número
inventado.

No toca ningún gate real ni config — solo una capa de lectura adicional,
igual que analisis_gate_riguroso.py (Wilson+shuffle) el 10-Jul.
"""
import json
import math

PARAMS = "data/shadow/strategy_params.json"
CUSTOM_HIP = "data/shadow/hipotesis_custom.json"
CONFIG_LIVE = "data/live/config_live.json"


def n_trials_estimado():
    """Nº de 'intentos' ya realizados en el proyecto: cada clave de
    strategy_params.json es un bucket con su propio IC calculado, más las
    hipótesis custom (búsquedas explícitas de patrón)."""
    n_buckets = len(json.load(open(PARAMS))["estrategias"])
    try:
        n_hip = len(json.load(open(CUSTOM_HIP))["hipotesis"])
    except (FileNotFoundError, KeyError):
        n_hip = 0
    return n_buckets + n_hip, n_buckets, n_hip


def z_max_esperado_bajo_null(n_trials: int) -> float:
    """E[max de N normales estándar i.i.d.] — aproximación clásica de
    valores extremos (Bailey & Lopez de Prado 2014, ec. 6alente para el
    caso normal). Con N=1 debe devolver ~0 (sin corrección)."""
    if n_trials <= 1:
        return 0.0
    ln_n = math.log(n_trials)
    termino_principal = math.sqrt(2 * ln_n)
    correccion = (math.log(math.log(n_trials)) + math.log(4 * math.pi)) / (2 * termino_principal) if n_trials > math.e else 0.0
    return termino_principal - correccion


def z_score_hit_rate(aciertos: int, n: int) -> float:
    """z-score del hit-rate observado contra la nula p=0.5 (aproximación
    normal al binomial, válida para n>=~20 como los que maneja este
    proyecto)."""
    if n == 0:
        return 0.0
    phat = aciertos / n
    se = math.sqrt(0.25 / n)
    return (phat - 0.5) / se


def evaluar_tuplas(nombres_y_datos, n_trials_total):
    z_umbral = z_max_esperado_bajo_null(n_trials_total)
    print(f"N intentos estimado: {n_trials_total} -> z máximo esperado bajo la nula (sin ventaja real): {z_umbral:.3f}")
    print(f"(el umbral de un solo test al 95% sería z=1.645 — {z_umbral/1.645:.1f}x más exigente con N={n_trials_total})\n")
    print(f"{'tupla':<50} {'n':>5} {'hit%':>6} {'z':>7} {'veredicto'}")
    print("-" * 100)
    for nombre, n, ic in nombres_y_datos:
        if n == 0:
            continue
        aciertos = round((ic + 0.5) * (n + 2) - 1)  # invierte ic_bayes=(aciertos+1)/(n+2)-0.5
        hit = aciertos / n
        z = z_score_hit_rate(aciertos, n)
        veredicto = "SOBREVIVE la corrección" if z > z_umbral else "no distinguible del mejor de N azares"
        print(f"{nombre:<50} {n:>5} {hit*100:>5.1f}% {z:>7.2f}  {veredicto}")


def main():
    n_total, n_buckets, n_hip = n_trials_estimado()
    print(f"strategy_params.json: {n_buckets} claves | hipotesis_custom.json: {n_hip} hipótesis\n")

    cfg = json.load(open(CONFIG_LIVE))
    tuplas_interes = list(cfg.get("pares_permitidos_live", [])) + list(cfg.get("candidatos_evaluacion_live", []))
    params = json.load(open(PARAMS))["estrategias"]

    filas = []
    for t in tuplas_interes:
        strat, par, tf, dec = t.split("#")
        clave = f"{strat}#{par}#{tf}"
        v = params.get(clave, {})
        campo_ic = f"ic_{dec}"
        campo_n = f"n_{dec}"
        ic = v.get(campo_ic)
        n = v.get(campo_n, 0)
        if ic is None:
            # fallback al agregado de la clave si no hay desglose direccional
            ic = v.get("ic_bayes")
            n = v.get("n", 0)
        if ic is None:
            continue
        filas.append((t, n, ic))

    evaluar_tuplas(filas, n_total)


if __name__ == "__main__":
    main()
