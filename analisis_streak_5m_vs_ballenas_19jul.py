"""Cruce causal: STREAK_MOM_5M / STREAK_FADE_5M (ambas desactivadas, IC
negativo en las dos direcciones -- ver CLAUDE.md punto 1 de la sesión
19-Jul) contra el flujo REAL de ballenas en cada mercado.

Intento 1 (descartado): usar ballenas_timing_history.csv ya acumulado --
0 intersección con los market_id de estas señales. Causa: ballenas_observer.py
solo captura mercados que están ACTIVOS en el momento de su poll horario;
un mercado de 5min casi nunca coincide con esa cadencia (cubierto en firme
solo desde el ejecutor de baja latencia ballenas_5m, 18-Jul, posterior a
estas señales de 08-16 Jul). No hay atajo: hay que re-pedir /trades.

Intento 2 (este script): re-pide /trades por mercado (mismo endpoint y
mismo patrón que analisis_ballenas_dosis_respuesta_16jul.py), pero SIN
re-pedir la resolución -- ya la tenemos en results.csv (columna acierto).
Corte causal estricto: solo trades con ts < prediction_timestamp de
nuestra señal, dentro de la banda de precio calibrada [banda_lo,banda_hi)
para activo#5m en ballenas_timing_state.json (evita la fuga temporal de
idea_cruce_ballenas_hipotesis_muertas_19jul). Exige >=3 trades previos en
banda para fijar una mayoría.

No escribe nada en data/ ni toca ningún proceso live.
Uso: python3 analisis_streak_5m_vs_ballenas_19jul.py
"""
import csv
import json
import random
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

from smart_money_tracker import trades_de_mercado

DIR = Path(__file__).parent
RESULTS = DIR / "data/shadow/results.csv"
STATE = DIR / "data/shadow/ballenas_timing_state.json"

ESTRATEGIAS = {"STREAK_MOM_5M", "STREAK_FADE_5M"}
MIN_TRADES_PREVIOS = 3
MUESTRA_MAX = 350  # tope de re-fetch, mismo espíritu que MUESTRA_MAX_POR_COMBO=250 del script hermano


def parse_ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def cargar_bandas_5m():
    estado = json.loads(STATE.read_text())
    bandas = {}
    for activo in ("SOL", "ETH", "XRP"):
        e = estado.get(f"{activo}#5m", {})
        if e.get("significativo"):
            bandas[activo] = (e["banda_lo"], e["banda_hi"])
    return bandas


def cargar_señales():
    filas = []
    with open(RESULTS, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["strategy"] not in ESTRATEGIAS:
                continue
            activo = row["subtype"].split("#")[0]
            if activo not in ("SOL", "ETH", "XRP"):
                continue
            try:
                pred_ts = parse_ts(row["prediction_timestamp"])
            except ValueError:
                continue
            filas.append({
                "strategy": row["strategy"], "activo": activo,
                "market_id": row["market_id"], "condition_id": row.get("condition_id", ""),
                "pred_ts": pred_ts, "decision": row["decision"], "acierto": int(row["acierto"]),
            })
    return filas


def cargar_condition_ids(market_ids, fecha_lo, fecha_hi):
    mapa = {}
    pendientes = set(market_ids)
    for archivo in sorted((DIR / "data/markets").glob("*.csv")):
        if not (fecha_lo <= archivo.stem <= fecha_hi):
            continue
        with open(archivo, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                mid = row.get("market_id", "")
                if mid in pendientes:
                    cid = row.get("condition_id", "")
                    if cid:
                        mapa[mid] = cid
                        pendientes.discard(mid)
        if not pendientes:
            break
    return mapa


def main():
    bandas = cargar_bandas_5m()
    print(f"Bandas 5m significativas: {bandas}", flush=True)

    señales = cargar_señales()
    print(f"Señales STREAK_MOM_5M + STREAK_FADE_5M (SOL/ETH/XRP): {len(señales)}", flush=True)

    if len(señales) > MUESTRA_MAX:
        random.seed(19)
        random.shuffle(señales)
        señales = señales[:MUESTRA_MAX]
        print(f"Muestreado a {MUESTRA_MAX} (tope de re-fetch)", flush=True)

    fechas = sorted(s["pred_ts"].strftime("%Y-%m-%d") for s in señales)
    market_ids = {s["market_id"] for s in señales}
    mapa_mid_cid = cargar_condition_ids(market_ids, fechas[0], fechas[-1])
    print(f"Mapa market_id->condition_id: {len(mapa_mid_cid)}/{len(market_ids)}", flush=True)

    resultado = []
    sin_cid = sin_previos = 0
    t0 = time.time()
    for i, s in enumerate(señales):
        cid = mapa_mid_cid.get(s["market_id"])
        if cid is None:
            sin_cid += 1
            continue
        lo, hi = bandas[s["activo"]]
        trades = trades_de_mercado(cid)
        previos = []
        for t in trades:
            if (t.get("side") or "").strip().upper() != "BUY":
                continue
            ts_str = t.get("timestamp")
            try:
                # timestamp de la API viene en epoch segundos (mismo parseo que ballenas_observer.py)
                ts_trade = datetime.fromtimestamp(float(ts_str), tz=timezone.utc)
            except (TypeError, ValueError, OSError):
                continue
            if ts_trade >= s["pred_ts"]:
                continue
            precio_t = t.get("price")
            outcome_t = (t.get("outcome") or "").strip().lower()
            if precio_t is None or outcome_t not in ("up", "down", "yes", "no"):
                continue
            try:
                precio_t = float(precio_t)
            except (ValueError, TypeError):
                continue
            if not (lo <= precio_t < hi):
                continue
            previos.append(outcome_t in ("up", "yes"))
        if len(previos) < MIN_TRADES_PREVIOS:
            sin_previos += 1
            continue
        n_yes = sum(previos)
        mayoria_yes = n_yes >= (len(previos) - n_yes)
        ballena_decision = "BUY_YES" if mayoria_yes else "BUY_NO"
        coincide = int(s["decision"] == ballena_decision)
        resultado.append((s["strategy"], s["activo"], s["decision"], s["acierto"], coincide, len(previos)))
        if (i + 1) % 50 == 0:
            print(f"  {i+1}/{len(señales)} procesados ({time.time()-t0:.0f}s)...", flush=True)

    print(f"\nDescartadas: sin_cid={sin_cid} sin>={MIN_TRADES_PREVIOS}_previos_en_banda={sin_previos}")
    print(f"Filas con dato causal completo: {len(resultado)}")
    if not resultado:
        print("Sin datos suficientes para concluir nada -- salir.")
        return

    def reportar(nombre, filas):
        n = len(filas)
        print(f"\n--- {nombre} (n={n}) ---")
        if n < 15:
            print("  n<15, no concluye (mínimo del proyecto).")
            return
        for etiqueta, val in (("coincide con mayoría ballena", 1), ("contradice mayoría ballena", 0)):
            sub = [f for f in filas if f[4] == val]
            if not sub:
                print(f"  {etiqueta}: n=0")
                continue
            hit = sum(f[3] for f in sub) / len(sub)
            print(f"  {etiqueta}: n={len(sub):>3}  hit={hit*100:5.1f}%")

    reportar("TODAS (STREAK_MOM_5M + STREAK_FADE_5M)", resultado)
    for estr in ESTRATEGIAS:
        reportar(estr, [f for f in resultado if f[0] == estr])
    for activo in ("SOL", "ETH", "XRP"):
        reportar(f"activo={activo}", [f for f in resultado if f[1] == activo])


if __name__ == "__main__":
    sys.exit(main() or 0)
