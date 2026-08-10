#!/usr/bin/env python3
"""analisis_zonas_validadas_externas_post_twap_10ago.py — regenera
data/shadow/zonas_validadas_externas.json, la semilla externa de
gate_bucket_propio.py::_ZONAS_VALIDADAS_EXTERNAMENTE, usando SOLO datos
post-TWAP (07-Ago en adelante) de ballenas_timing_history.csv.

Origen (10-Ago, petición explícita Javi tras el diagnóstico de por qué
BALLENAS_TARDIAS#ETH#5min y FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC
#15min llevaban desde el 09-Ago con el override de emergencia puesto):
la semilla externa original (05-Ago) se retiró el 09-Ago porque se basaba
en `ballenas_timing_history.csv` PRE-TWAP -- pero el fichero sigue
creciendo cada día con datos NUEVOS, post-TWAP, y ya acumula miles de
observaciones por zona (n=2500-14700 según zona) -- mucho más rápido que
esperar a que las 2 tuplas acumulen su propio n en results.csv (que
habría tardado meses en el caso más ajustado, ver
project_stage0_redefinido_diagnostico_completo_10ago).

Rigor por zona (bucket 0.05, mismo step que gate_bucket_propio.py):
  1. n >= N_MIN (15, mínimo CLAUDE.md -- en la práctica todas las zonas
     activas tienen n en miles, muy por encima)
  2. Wilson90 lower bound del hit-rate > breakeven implícito por el
     precio medio real de la zona + fee 7% real (gross_win=(1-p)/p,
     NUNCA (1-p) -- fórmula exacta del proyecto)
  3. Concentración: ningún mercado (condition_id) puede superar el 30%
     de las observaciones de la zona (mismo umbral que analisis_franja_
     milimetrica_ballenas.py usa para huecos de cobertura) -- evita que
     un solo evento amplificado por muchas wallets infle el n
  4. Split-half cronológico: el signo de (wilson90lo - breakeven) debe
     repetirse en ambas mitades temporales del periodo post-TWAP

SOLO promueve a "bueno_confirmado" -- nunca "malo_confirmado" (la
semilla externa, por diseño de gate_bucket_propio.py, únicamente
PROMUEVE mientras el dato propio siga sin_concluir, nunca sustituye un
veredicto propio ya confirmado ni añade vetos nuevos).

Solo lectura de ballenas_timing_history.csv -- solo ESCRIBE
data/shadow/zonas_validadas_externas.json. No toca gate_bucket_propio.py
ni ningún override -- la conexión final (leer este JSON en vez del
diccionario hardcodeado) y la retirada del override son decisiones
separadas, explícitas, después de revisar este resultado.
"""
import csv
import json
import math
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
BALLENAS_HIST = REPO / "data/shadow/ballenas_timing_history.csv"
OUT = REPO / "data/shadow/zonas_validadas_externas.json"

FECHA_CAMBIO_TWAP = datetime(2026, 8, 7, tzinfo=timezone.utc)
STEP = 0.05
N_MIN = 15
FEE = 0.07
Z_90 = 1.645
TOP1_MAX_PCT = 30.0

# Tuplas objetivo: (tupla_str exacta, activo ballenas, marco ballenas --
# MARCO_BALLENAS_MAP: "5min"->"5m", "15min"->"15m"). 10-Ago: extendido de
# las 2 tuplas ya live a la FAMILIA COMPLETA (petición explícita Javi,
# "repite esto para el resto de la familia") -- BALLENAS_TARDIAS opera en
# 6 monedas (5 en 5min + BTC en 15min), FAVORITO_CONFIRMADO_15MIN_
# ALTACONVICCION en 6 monedas #15min. Solo ETH#5min y BTC#15min
# respectivamente estaban en pares_permitidos_live antes de hoy -- el
# resto son candidatas en candidatos_evaluacion_live, mismo mecanismo,
# mismo rigor, para ver si tienen la misma zona externa rescatable.
OBJETIVO = [
    ("BALLENAS_TARDIAS#BNB#5min#BUY_YES", "BNB", "5m"),
    ("BALLENAS_TARDIAS#BTC#15min#BUY_YES", "BTC", "15m"),
    ("BALLENAS_TARDIAS#DOGE#5min#BUY_YES", "DOGE", "5m"),
    ("BALLENAS_TARDIAS#ETH#5min#BUY_YES", "ETH", "5m"),
    ("BALLENAS_TARDIAS#SOL#5min#BUY_YES", "SOL", "5m"),
    ("BALLENAS_TARDIAS#XRP#5min#BUY_YES", "XRP", "5m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BNB#15min#BUY_YES", "BNB", "15m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#BTC#15min#BUY_YES", "BTC", "15m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#DOGE#15min#BUY_YES", "DOGE", "15m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#ETH#15min#BUY_YES", "ETH", "15m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#SOL#15min#BUY_YES", "SOL", "15m"),
    ("FAVORITO_CONFIRMADO_15MIN_ALTACONVICCION#XRP#15min#BUY_YES", "XRP", "15m"),
]


def bucket(p):
    return round(math.floor(p / STEP + 1e-9) * STEP, 4)


def wilson_lower(hits, n, z=Z_90):
    if n == 0:
        return 0.0
    p = hits / n
    denom = 1 + z * z / n
    centro = p + z * z / (2 * n)
    margen = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centro - margen) / denom


def breakeven(py_medio):
    gross_win = (1 - py_medio) / py_medio
    return 1 / (1 + gross_win * (1 - FEE))


def cargar(activo, marco, compro_yes="1"):
    """compro_yes filtra el LADO comprado -- 10-Ago, fix real cazado por
    /code-review: `precio` en ballenas_timing_history.csv es el precio SIN
    CONVERTIR del lado que compró esa wallet (ballenas_observer.py::precio
    = t["price"] crudo de la API). Un compro_yes=0 a precio=0.55 significa
    "pagó 0.55 por NO" (probabilidad YES implícita ~0.45), NO es el mismo
    bucket de precio que un compro_yes=1 a precio=0.55. Mezclar ambos
    lados sin convertir contaminaba el bucket con dos series de precio
    distintas. Las 2 tuplas OBJETIVO son BUY_YES -- exige compro_yes="1"
    (precio YES directo, comparable 1:1 con lo que paga nuestro
    ejecutador BUY_YES) por defecto."""
    por_bucket = defaultdict(list)
    with open(BALLENAS_HIST, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("activo") != activo or row.get("marco") != marco:
                continue
            if row.get("compro_yes") != compro_yes:
                continue
            try:
                p = float(row["precio"])
                ac = int(row["acierto"])
            except (TypeError, ValueError):
                continue
            try:
                ts = datetime.fromisoformat(row["ts_trade"])
                if ts.tzinfo is None:
                    ts = ts.replace(tzinfo=timezone.utc)
            except Exception:
                continue
            if ts < FECHA_CAMBIO_TWAP:
                continue
            b = bucket(p)
            por_bucket[b].append((ts, p, ac, row.get("condition_id", "")))
    return por_bucket


def evaluar_zona(filas):
    n = len(filas)
    if n < N_MIN:
        return None
    py_medio = sum(p for _, p, _, _ in filas) / n
    hits = sum(ac for _, _, ac, _ in filas)
    hit = hits / n
    wlo = wilson_lower(hits, n)
    be = breakeven(py_medio)

    from collections import Counter
    c_mkt = Counter(cid for _, _, _, cid in filas)
    top1_pct = (c_mkt.most_common(1)[0][1] / n * 100) if c_mkt else 100.0

    filas_ordenadas = sorted(filas, key=lambda x: x[0])
    mid = n // 2
    m1, m2 = filas_ordenadas[:mid], filas_ordenadas[mid:]
    if len(m1) < 5 or len(m2) < 5:
        split_ok = False
        wlo1 = wlo2 = None
    else:
        hits1 = sum(ac for _, _, ac, _ in m1)
        hits2 = sum(ac for _, _, ac, _ in m2)
        py1 = sum(p for _, p, _, _ in m1) / len(m1)
        py2 = sum(p for _, p, _, _ in m2) / len(m2)
        wlo1 = wilson_lower(hits1, len(m1))
        wlo2 = wilson_lower(hits2, len(m2))
        be1, be2 = breakeven(py1), breakeven(py2)
        split_ok = (wlo1 > be1) and (wlo2 > be2)

    return {
        "n": n, "py_medio": round(py_medio, 4), "hit": round(hit, 4),
        "wilson90lo": round(wlo, 4), "breakeven": round(be, 4),
        "margen_pp": round((wlo - be) * 100, 2),
        "n_mercados": len(c_mkt), "top1_pct": round(top1_pct, 1),
        "split_half_ok": split_ok,
        "pasa": bool(wlo > be and top1_pct <= TOP1_MAX_PCT and split_ok),
    }


def main():
    resultado = {}
    for tupla_str, activo, marco in OBJETIVO:
        direccion = tupla_str.rsplit("#", 1)[-1]
        compro_yes = "1" if direccion == "BUY_YES" else "0"
        por_bucket = cargar(activo, marco, compro_yes=compro_yes)
        zonas_confirmadas = []
        detalle = {}
        for b in sorted(por_bucket):
            info = evaluar_zona(por_bucket[b])
            if info is None:
                continue
            detalle[f"{b:.2f}"] = info
            if info["pasa"]:
                zonas_confirmadas.append([b, round(b + STEP, 2)])
        resultado[tupla_str] = {
            "zonas_bueno_confirmado": zonas_confirmadas,
            "detalle_por_bucket": detalle,
            "fuente": "ballenas_timing_history.csv post-07-Ago (TWAP-safe)",
            "regenerado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
        print(f"\n=== {tupla_str} ===")
        for b, hi in zonas_confirmadas:
            info = detalle[f"{b:.2f}"]
            print(f"  🟢 [{b:.2f},{hi:.2f}) n={info['n']} hit={info['hit']*100:.1f}% "
                  f"wilson90lo={info['wilson90lo']*100:.1f}% breakeven={info['breakeven']*100:.1f}% "
                  f"margen={info['margen_pp']:+.1f}pp mercados={info['n_mercados']} top1={info['top1_pct']:.1f}%")
        if not zonas_confirmadas:
            print("  (ninguna zona confirmada)")

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(resultado, f, indent=2, ensure_ascii=False)
    print(f"\nGuardado en {OUT}")


if __name__ == "__main__":
    main()
