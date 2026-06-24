"""
shadow_resolve.py — resolución de predicciones contra resultados reales.

Recorre todas las predicciones registradas que tengan decision != SKIP
y aún no se hayan resuelto. Para cada una:
  - Consulta el estado actual del mercado en Polymarket.
  - Si el mercado se ha cerrado/resuelto, determina el outcome ganador.
  - Calcula si la predicción acertó, el P&L bruto y el P&L con slippage.

Salidas:
  - data/shadow/results.csv         — historial acumulativo de resoluciones
  - data/shadow/strategy_accuracy.csv — IC y stats por estrategia (para auto-calibración)

Ejecutado tras shadow_predict.py en el mismo workflow.
"""

import csv
import glob
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path

import requests


def _infer_subtype(pred: dict) -> str:
    """Infiere subtype de la columna razon cuando no está disponible en el CSV."""
    s = pred.get("subtype", "")
    if s:
        return s
    razon = pred.get("razon", "") or ""
    # "updown_gbm BTC 15min ..."  →  BTC#15min
    m = re.search(r'updown_gbm\s+(\w+)\s+(\w+)', razon)
    if m:
        return f"{m.group(1)}#{m.group(2)}"
    # "price_target_gbm BTC atexpiry ..."  →  BTC#atexpiry
    m = re.search(r'price_target_gbm\s+(\w+)\s+(\w+)', razon)
    if m:
        return f"{m.group(1)}#{m.group(2)}"
    # "weekly_between BTC ..." / "weekly_price BTC ..."  →  BTC
    m = re.search(r'weekly_(?:between|price)\s+(\w+)', razon)
    if m:
        return m.group(1)
    # "price_momentum ..." / "smart_flow_1h ..."  → asset si aparece
    m = re.search(r'(?:price_momentum|smart_flow_1h)\s+.*?(BTC|ETH|SOL|XRP|DOGE|BNB)', razon)
    if m:
        return m.group(1)
    return ""

TIMEOUT = 30
SLIPPAGE = 0.02
APUESTA_SIMULADA = 0.90  # consistente con el bot anterior (3% de 30€)

DIR_SHADOW = Path("data/shadow")
DIR_SHADOW.mkdir(parents=True, exist_ok=True)
RESULTS_PATH = DIR_SHADOW / "results.csv"
ACCURACY_PATH = DIR_SHADOW / "strategy_accuracy.csv"


def _normalizar_pred(row: dict) -> dict:
    """
    El header del CSV puede tener solo 13 columnas (formato antiguo).
    En ese caso subtype, apuesta y features van al key None como lista.
    Los extraemos para que el resto del código los encuentre con sus nombres.
    """
    extra = row.pop(None, None)
    if isinstance(extra, list):
        campos = ["subtype", "apuesta", "features"]
        for i, campo in enumerate(campos):
            if i < len(extra) and extra[i] and not row.get(campo):
                row[campo] = extra[i]
    return row


def cargar_predicciones_pendientes() -> list:
    """Carga todas las predicciones que tengan decision != SKIP."""
    archivos = sorted(glob.glob(str(DIR_SHADOW / "predictions_*.csv")))
    pendientes = []
    for arch in archivos:
        with open(arch, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("decision", "SKIP") in ("BUY_YES", "BUY_NO"):
                    pendientes.append(_normalizar_pred(row))
    return pendientes


def cargar_ya_resueltas() -> set:
    """
    Devuelve set de (strategy, market_id) ya resueltos.
    Sin timestamp: cada (strategy, market_id) se resuelve UNA sola vez aunque
    se haya predicho en varios días distintos (evita duplicar el IC).
    """
    if not RESULTS_PATH.exists():
        return set()
    ya = set()
    with open(RESULTS_PATH, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ya.add((row.get("strategy", ""),
                    row.get("market_id", "")))
    return ya


def estado_mercado(market_id: str) -> dict | None:
    """Consulta el estado actual del mercado en Polymarket."""
    url = "https://gamma-api.polymarket.com/markets"
    try:
        r = requests.get(url, params={"id": market_id}, timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json()
        if isinstance(data, list) and data:
            return data[0]
        if isinstance(data, dict):
            return data
    except Exception as e:
        print(f"  Error consultando {market_id}: {type(e).__name__}: {e}")
    return None


def parse_outcome_prices(raw):
    if raw is None or raw == "":
        return None
    if isinstance(raw, list):
        return raw
    if isinstance(raw, str):
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return None
    return None


def evaluar(pred: dict, mercado: dict) -> dict | None:
    """
    Señal primaria: outcomePrices — si alguno llega a 1.0 el mercado está
    resuelto, independientemente de los flags closed/archived/resolved.
    Esto evita falsos negativos cuando la API actualiza los precios antes
    de cambiar el campo closed (comportamiento habitual en Polymarket).
    """
    if not mercado:
        return None

    # --- Señal primaria: outcomePrices ---
    precios = parse_outcome_prices(mercado.get("outcomePrices"))
    if not precios or len(precios) < 2:
        return None
    try:
        py_final = float(precios[0])
        pn_final = float(precios[1])
    except (ValueError, TypeError):
        return None

    if abs(py_final - 1.0) < 0.01:
        outcome_real = "YES"
    elif abs(pn_final - 1.0) < 0.01:
        outcome_real = "NO"
    else:
        # Precios no liquidados — comprobar flags de estado
        is_closed = (
            mercado.get("closed")
            or mercado.get("archived")
            or mercado.get("resolved")
            or not mercado.get("active", True)
        )
        if not is_closed:
            return None  # mercado genuinamente abierto
        return None  # cerrado pero oracle pendiente — reintentar

    decision = pred.get("decision", "")
    acierto = (decision == "BUY_YES" and outcome_real == "YES") or \
              (decision == "BUY_NO" and outcome_real == "NO")

    # P&L simulado.
    try:
        precio_entrada = float(pred.get("precio_yes_mercado", 0.5))
    except (ValueError, TypeError):
        precio_entrada = 0.5
    if decision == "BUY_NO":
        precio_entrada = 1 - precio_entrada

    # Apuesta: usa la registrada en la predicción (Kelly dinámico), o la base si no existe
    try:
        apuesta = float(pred.get("apuesta") or APUESTA_SIMULADA)
        if apuesta <= 0:
            apuesta = APUESTA_SIMULADA
    except (ValueError, TypeError):
        apuesta = APUESTA_SIMULADA

    if acierto:
        payout    = apuesta / max(0.01, precio_entrada)
        pnl_bruto = payout - apuesta
        pnl_neto  = pnl_bruto - SLIPPAGE * apuesta
    else:
        pnl_bruto = -apuesta
        pnl_neto  = -apuesta - SLIPPAGE * apuesta

    return {
        "outcome_real": outcome_real,
        "acierto": 1 if acierto else 0,
        "precio_entrada": precio_entrada,
        "pnl_bruto": pnl_bruto,
        "pnl_neto": pnl_neto,
    }


def actualizar_strategy_accuracy(nuevos: list, ts: str):
    """
    Actualiza data/shadow/strategy_accuracy.csv con las nuevas resoluciones.

    Por cada estrategia calcula métricas acumuladas:
    - n_total: predicciones resueltas
    - n_aciertos: cuántas acertaron
    - hit_rate: tasa de acierto real
    - edge_medio: edge_direccional medio al entrar
    - pnl_total: P&L neto acumulado
    - IC (Information Coefficient): correlación entre señal y outcome
      IC = hit_rate - 0.5  (simplificado para mercados binarios 50/50)
      Cuando tengamos suficientes datos usaremos correlación de Pearson
      entre prob_yes_modelo y outcome_real (YES=1, NO=0).
    - IC_pearson: correlación Pearson entre prob_yes_modelo y outcome_real
      (más preciso que hit_rate-0.5, requiere prob_yes_modelo poblado)
    """
    # Cargar stats existentes
    stats = {}
    if ACCURACY_PATH.exists():
        with open(ACCURACY_PATH, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                s = row["strategy"]
                stats[s] = {
                    "n_total": int(row.get("n_total", 0)),
                    "n_aciertos": int(row.get("n_aciertos", 0)),
                    "pnl_total": float(row.get("pnl_total", 0)),
                    "sum_edge": float(row.get("sum_edge", 0)),
                    # Para IC de Pearson: acumulamos suma de productos
                    "sum_prob": float(row.get("sum_prob", 0)),
                    "sum_outcome": float(row.get("sum_outcome", 0)),
                    "sum_prob2": float(row.get("sum_prob2", 0)),
                    "sum_outcome2": float(row.get("sum_outcome2", 0)),
                    "sum_prob_outcome": float(row.get("sum_prob_outcome", 0)),
                }

    # Incorporar nuevas resoluciones
    for r in nuevos:
        s = r["strategy"]
        if s not in stats:
            stats[s] = {
                "n_total": 0, "n_aciertos": 0, "pnl_total": 0.0,
                "sum_edge": 0.0, "sum_prob": 0.0, "sum_outcome": 0.0,
                "sum_prob2": 0.0, "sum_outcome2": 0.0, "sum_prob_outcome": 0.0,
            }
        d = stats[s]
        d["n_total"] += 1
        d["n_aciertos"] += int(r["acierto"])
        d["pnl_total"] += float(r["pnl_neto"])
        try:
            d["sum_edge"] += float(r.get("edge_direccional", 0) or 0)
        except (ValueError, TypeError):
            pass
        # Para IC Pearson: prob_yes_modelo vs outcome (YES=1, NO=0)
        try:
            prob = float(r.get("prob_yes_modelo", "") or "")
            outcome = 1.0 if r["outcome_real"] == "YES" else 0.0
            d["sum_prob"] += prob
            d["sum_outcome"] += outcome
            d["sum_prob2"] += prob * prob
            d["sum_outcome2"] += outcome * outcome
            d["sum_prob_outcome"] += prob * outcome
        except (ValueError, TypeError):
            pass

    # Calcular métricas derivadas y guardar
    columnas = [
        "timestamp_utc", "strategy",
        "n_total", "n_aciertos", "hit_rate",
        "edge_medio", "pnl_total", "pnl_medio",
        "IC_simple", "IC_pearson",
        # acumuladores internos (para poder añadir filas futuras)
        "sum_edge", "sum_prob", "sum_outcome",
        "sum_prob2", "sum_outcome2", "sum_prob_outcome",
    ]
    filas = []
    for s, d in sorted(stats.items()):
        n = d["n_total"]
        hit_rate = d["n_aciertos"] / n if n else 0.0
        ic_simple = round(hit_rate - 0.5, 4)  # IC simplificado binario
        # IC Pearson si tenemos datos de prob_yes_modelo
        ic_pearson = 0.0
        try:
            sp = d["sum_prob"]
            so = d["sum_outcome"]
            sp2 = d["sum_prob2"]
            so2 = d["sum_outcome2"]
            spo = d["sum_prob_outcome"]
            num = n * spo - sp * so
            den = math.sqrt(max(0, (n * sp2 - sp**2) * (n * so2 - so**2)))
            ic_pearson = round(num / den, 4) if den > 1e-10 else 0.0
        except (ZeroDivisionError, ValueError):
            pass

        filas.append({
            "timestamp_utc": ts,
            "strategy": s,
            "n_total": n,
            "n_aciertos": d["n_aciertos"],
            "hit_rate": round(hit_rate, 4),
            "edge_medio": round(d["sum_edge"] / n, 4) if n else 0.0,
            "pnl_total": round(d["pnl_total"], 4),
            "pnl_medio": round(d["pnl_total"] / n, 4) if n else 0.0,
            "IC_simple": ic_simple,
            "IC_pearson": ic_pearson,
            "sum_edge": round(d["sum_edge"], 6),
            "sum_prob": round(d["sum_prob"], 6),
            "sum_outcome": round(d["sum_outcome"], 6),
            "sum_prob2": round(d["sum_prob2"], 6),
            "sum_outcome2": round(d["sum_outcome2"], 6),
            "sum_prob_outcome": round(d["sum_prob_outcome"], 6),
        })

    with open(ACCURACY_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        w.writeheader()
        for fila in filas:
            w.writerow(fila)

    print(f"  IC por estrategia (IC_simple = hit_rate - 0.5):")
    for fila in filas:
        if fila["n_total"] > 0:
            bar = "+" * max(0, int(fila["IC_simple"] * 20))
            print(f"    {fila['strategy']:30s}  n={fila['n_total']:>4}  "
                  f"hit={fila['hit_rate']:.3f}  IC={fila['IC_simple']:+.3f}  "
                  f"pnl={fila['pnl_total']:+.2f}  {bar}")


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Shadow resolve ===")

    pendientes = cargar_predicciones_pendientes()
    ya_resueltas = cargar_ya_resueltas()

    nuevos_resultados = []
    consultados_ids = set()
    cache_mercados = {}
    debug_no_resueltos = 0  # log primeros mercados sin resolver para diagnóstico

    ahora = datetime.now(timezone.utc)

    for pred in pendientes:
        clave = (pred.get("strategy", ""),
                 pred.get("market_id", ""))
        if clave in ya_resueltas:
            continue

        # Saltar mercados cuyo end_date es más de 2h en el futuro — imposible que resuelvan
        end_str = pred.get("end_date", "")
        if end_str:
            try:
                end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
                if end_dt.tzinfo is None:
                    end_dt = end_dt.replace(tzinfo=timezone.utc)
                if (end_dt - ahora).total_seconds() > 7200:
                    continue
            except Exception:
                pass

        mid = pred.get("market_id", "")
        if mid not in cache_mercados:
            cache_mercados[mid] = estado_mercado(mid)
            consultados_ids.add(mid)
        mercado = cache_mercados[mid]
        res = evaluar(pred, mercado)
        if res is None:
            if mercado and debug_no_resueltos < 3:
                precios = mercado.get("outcomePrices", "?")
                print(f"  [debug] market {mid}: closed={mercado.get('closed')} "
                      f"archived={mercado.get('archived')} "
                      f"resolved={mercado.get('resolved')} "
                      f"active={mercado.get('active')} "
                      f"outcomePrices={str(precios)[:40]}")
                debug_no_resueltos += 1
            continue

        # Marcar como resuelta en memoria para evitar duplicados dentro del mismo run
        ya_resueltas.add(clave)

        nuevos_resultados.append({
            "resolution_timestamp": ts,
            "prediction_timestamp": pred.get("timestamp_utc", ""),
            "strategy": pred.get("strategy", ""),
            "subtype": _infer_subtype(pred),
            "market_id": mid,
            "question": pred.get("question", ""),
            "end_date": pred.get("end_date", ""),
            "decision": pred.get("decision", ""),
            "precio_yes_mercado": pred.get("precio_yes_mercado", ""),
            "prob_yes_modelo": pred.get("prob_yes_modelo", ""),
            "edge_neto": pred.get("edge_neto", ""),
            "edge_direccional": pred.get("edge_direccional", ""),
            "outcome_real": res["outcome_real"],
            "acierto": res["acierto"],
            "pnl_bruto": f"{res['pnl_bruto']:.4f}",
            "pnl_neto": f"{res['pnl_neto']:.4f}",
            "features": pred.get("features", ""),
        })

    print(f"  Predicciones pendientes consultadas: {len(consultados_ids)} mercados")
    print(f"  Resoluciones nuevas: {len(nuevos_resultados)}")

    if not nuevos_resultados:
        print(f"[{ts}] === Fin shadow resolve (nada nuevo) ===")
        return

    nuevo_archivo = not RESULTS_PATH.exists()
    columnas = list(nuevos_resultados[0].keys())
    with open(RESULTS_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        if nuevo_archivo:
            w.writeheader()
        for r in nuevos_resultados:
            w.writerow(r)

    # Resumen rápido por estrategia
    resumen = {}
    for r in nuevos_resultados:
        s = r["strategy"]
        resumen.setdefault(s, {"n": 0, "aciertos": 0, "pnl": 0.0})
        resumen[s]["n"] += 1
        resumen[s]["aciertos"] += r["acierto"]
        resumen[s]["pnl"] += float(r["pnl_neto"])
    print("  Resumen de nuevas resoluciones por estrategia:")
    for s, d in resumen.items():
        tasa = d["aciertos"] / d["n"] * 100 if d["n"] else 0
        print(f"    {s:30s}  n={d['n']:>4}  acierto={tasa:5.1f}%  "
              f"pnl_neto={d['pnl']:+.2f}€")

    actualizar_strategy_accuracy(nuevos_resultados, ts)

    print(f"[{ts}] === Fin shadow resolve ===")


if __name__ == "__main__":
    main()
