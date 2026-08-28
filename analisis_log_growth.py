#!/usr/bin/env python3
"""
analisis_log_growth.py — Gate de crecimiento logarítmico (Kelly) por tupla
strategy#subtype#decision, complementario al gate de IC/n existente.

Motivo (17-Jul): el IC/EV por $ puede ser positivo mientras el crecimiento
compuesto es negativo -- "payout inverso" (hit-rate alto, pérdidas grandes
y poco frecuentes se comen el compounding). Ya confirmado contra el caso
conocido: FAVORITO_CONFIRMADO#{BTC,SOL,ETH}#15min#BUY_NO tienen EV/$
positivo pero g(f=10%) negativo en los 3 -- exactamente la trampa que el
IC no ve.

Fórmula: la fracción de retorno de una apuesta binaria NO depende del
tamaño de la apuesta (se cancela), así que se deriva directo de
precio_entrada + acierto (ver shadow_resolve.py:271-283, misma
convención SLIPPAGE):
  gana: r = (1-p)/p - SLIPPAGE      pierde: r = -1 - SLIPPAGE
Growth a una fracción de bankroll de referencia F (max_pct_bankroll del
config, no el tamaño real -- así todas las tuplas son comparables aunque
el stake esté pineado):
  g = mean(ln(1 + F*r_i))  sobre resoluciones shadow (results.csv)

Uso: ejecutar a mano al evaluar una candidata para pares_permitidos_live,
junto al gate estándar (IC>=0.08, n>=40). NO es cron, NO toca dinero,
NO escribe nada -- solo lee results.csv/config_live.json.
"""
import csv
import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import gate_bucket_propio as _gbp  # noqa: E402 -- 15-Ago, ver nota en gate()

RESULTS = REPO / "data" / "shadow" / "results.csv"
CONFIG_LIVE = REPO / "data" / "live" / "config_live.json"
SLIPPAGE = 0.02  # misma constante que shadow_resolve.py:64
N_MIN = 15       # regla del proyecto: ninguna conclusión con n<15


# Vocabulario alterno de decisión: WALLET_MIRROR/RESOLUTION_SNIPER_NAIVE (y
# cualquier estrategia futura sobre mercados Up/Down) usan "BUY_Down" en vez
# de "BUY_NO" (CLAUDE.md pt.19 -- mismo vocabulario distinto que ya rompió
# _grupos_desde_config() el 19-Ago). 28-Ago (/code-review, hallazgo real):
# _retorno() solo comprobaba "BUY_NO" -- una tupla BUY_Down calculaba g_kelly
# como si fuera BUY_YES (signo invertido, sin flip de precio). Inerte hoy
# (ninguna de las 2 estrategias escribe en results.csv todavía), pero
# cargar_tuplas_live() de analisis_gate_bucket_propio_fillable_03ago.py ya
# incluye sus 20 tuplas live/candidato genéricamente -- el día que empiecen a
# resolver en results.csv esto habría escrito g_kelly con signo equivocado
# sin ningún aviso.
_DECISIONES_NO = {"BUY_NO", "BUY_Down"}


def _retorno(row: dict) -> float:
    p = float(row["precio_yes_mercado"])
    p = min(0.99, max(0.01, p))
    if row["decision"] in _DECISIONES_NO:
        p = 1 - p
    if row["acierto"] == "1":
        return (1 - p) / p - SLIPPAGE
    return -1 - SLIPPAGE


def gate(strategy: str, subtype: str, decision: str, f: float = 0.10) -> dict:
    filas = [
        r for r in csv.DictReader(open(RESULTS, encoding="utf-8"))
        if r["strategy"] == strategy and r["subtype"] == subtype
        and r["decision"] == decision and r.get("acierto") in ("0", "1")
    ]
    # 15-Ago (/code-review, tras el fix del estado absorbente de
    # gate_bucket_propio en shadow_predict.py): si esta tupla YA está en
    # pares_permitidos_live, results.csv ahora también trae filas de zonas
    # de precio no confirmadas (antes suprimidas del todo) -- sin filtrarlas
    # aquí, este gate de payout inverso (el que detectó el sangrado real de
    # 28-Jul, CLAUDE.md pt.14) mezclaría esas zonas nunca-ejecutables con la
    # zona que sí opera dinero real, pudiendo enmascarar un payout inverso
    # de verdad o disparar uno falso. pares_live=set() si config_live.json
    # no se pudo leer -- filtrar_filas_zona_confirmada no filtra nada en ese
    # caso (mismo criterio que antes de este fix, ver cargar_pares_live_
    # fail_closed para el porqué es aceptable aquí: un config ilegible ya
    # deja el propio live_trade.py fail-closed sin operar).
    pares_live, pares_live_ok = _gbp.cargar_pares_live_fail_closed()
    if not pares_live_ok:
        print("[analisis_log_growth] \u26a0\ufe0f config_live.json ilegible -- filtro de zona confirmada NO se aplica este ciclo")
    filas = _gbp.filtrar_filas_zona_confirmada(filas, pares_live)
    n = len(filas)
    if n == 0:
        return {"n": 0}
    rs = [_retorno(r) for r in filas]
    hit = 100 * sum(1 for r in filas if r["acierto"] == "1") / n
    ev = sum(rs) / n
    g = sum(math.log(1 + f * x) for x in rs) / n
    return {"n": n, "hit_pct": hit, "ev_por_dolar": ev, "growth": g,
            "pasa": n >= N_MIN and g > 0}


def main():
    f = 0.10
    if len(sys.argv) >= 4:
        tuplas = [tuple(sys.argv[1:4])]
    else:
        config = json.loads(CONFIG_LIVE.read_text())
        f = config.get("riesgo", {}).get("max_pct_bankroll_por_trade", 0.10)
        # subtype ya contiene un "#" propio (BTC#15min) -- partir estrategia
        # por el primero y decision por el último, no split() plano.
        tuplas = []
        for t in config.get("pares_permitidos_live", []):
            strategy, resto = t.split("#", 1)
            subtype, decision = resto.rsplit("#", 1)
            tuplas.append((strategy, subtype, decision))

    print(f"{'tupla':60s} {'n':>5s} {'hit%':>6s} {'EV/$':>7s} {f'g(f={f:.0%})':>10s}  gate")
    for strategy, subtype, decision in tuplas:
        r = gate(strategy, subtype, decision, f)
        tup = f"{strategy}#{subtype}#{decision}"
        if r["n"] == 0:
            print(f"{tup:60s}   n=0  -- sin resoluciones shadow con esta clave exacta")
            continue
        flag = "PASA" if r["pasa"] else ("NO -- payout inverso" if r["n"] >= N_MIN else "NO -- n<15, sin concluir")
        print(f"{tup:60s} {r['n']:5d} {r['hit_pct']:5.1f}% {r['ev_por_dolar']:+7.3f} "
              f"{r['growth']:+10.5f}  {flag}")


if __name__ == "__main__":
    main()
