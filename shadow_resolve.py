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
import time
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
    """
    Consulta el estado actual del mercado en Polymarket. Reintenta en 429.

    Usa el endpoint por path (/markets/{id}), NO por query param (?id=X):
    verificado 2026-07-01 que ?id=X aplica un filtro implícito closed=false
    y por tanto NUNCA devuelve un mercado ya cerrado — exactamente el caso
    que evaluar() necesita para confirmar la resolución final. Esto dejaba
    predicciones sin resolver indefinidamente en cuanto el mercado cerraba
    de verdad (875 pares strategy/market_id >6h pasado su end_date sin
    resolver en el momento de detectarlo), con riesgo directo de dejar
    trades live en status=OPEN para siempre.
    """
    url = f"https://gamma-api.polymarket.com/markets/{market_id}"
    for intento in range(3):
        try:
            r = requests.get(url, timeout=TIMEOUT)
            if r.status_code == 429:
                time.sleep(2 ** intento)  # backoff: 1s, 2s, 4s
                continue
            if r.status_code == 404:
                return None
            r.raise_for_status()
            data = r.json()
            if isinstance(data, list) and data:
                return data[0]
            if isinstance(data, dict):
                return data
            return None
        except Exception as e:
            if intento == 2:
                print(f"  Error consultando {market_id}: {type(e).__name__}: {e}")
    return None


def fetch_mercados_paralelo(market_ids: list, workers: int = 3) -> dict:
    """
    Descarga el estado de múltiples mercados en paralelo con throttle.
    Máximo 3 workers simultáneos para no saturar la API de Polymarket.
    """
    import threading
    from concurrent.futures import ThreadPoolExecutor, as_completed
    _sem = threading.Semaphore(workers)

    def _fetch_con_sem(mid):
        with _sem:
            time.sleep(0.1)  # 100ms entre requests → ~30 req/s máximo
            return estado_mercado(mid)

    resultados = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futuros = {executor.submit(_fetch_con_sem, mid): mid for mid in market_ids}
        for futuro in as_completed(futuros):
            mid = futuros[futuro]
            try:
                resultados[mid] = futuro.result()
            except Exception:
                resultados[mid] = None
    return resultados


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


def evaluar(pred: dict, mercado: dict, ahora: datetime | None = None) -> dict | None:
    """
    Señal primaria: outcomePrices — si alguno llega a 1.0 el mercado está
    resuelto, independientemente de los flags closed/archived/resolved.
    Esto evita falsos negativos cuando la API actualiza los precios antes
    de cambiar el campo closed (comportamiento habitual en Polymarket).

    Salvaguarda: en ventanas cortas (15-60min) el precio puede tocar ~0.99
    por pura volatilidad intraciclo y revertir antes del cierre real. Para
    aceptar la resolución por precio exigimos ADEMÁS que el mercado ya haya
    pasado su end_date o que la API confirme closed/resolved — si no,
    reintentamos en el siguiente ciclo en vez de cerrar en falso.
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
        return None  # precios no liquidados — reintentar en el siguiente ciclo

    # Confirmar que el mercado realmente cerró antes de aceptar el precio como definitivo
    is_closed = (
        mercado.get("closed")
        or mercado.get("archived")
        or mercado.get("resolved")
        or not mercado.get("active", True)
    )
    if not is_closed:
        # Prioriza el endDate fresco del mercado (recién descargado en esta
        # misma función) sobre el cacheado en la predicción — si la predicción
        # se hizo sin endDate (mercado aún sin ese campo poblado en su
        # momento), el cacheado queda vacío para siempre y la resolución por
        # precio nunca se acepta (trade live queda OPEN indefinidamente).
        end_str = mercado.get("endDate") or pred.get("end_date", "")
        end_pasado = False
        if end_str:
            try:
                end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
                if end_dt.tzinfo is None:
                    end_dt = end_dt.replace(tzinfo=timezone.utc)
                end_pasado = (ahora or datetime.now(timezone.utc)) >= end_dt
            except Exception:
                pass
        if not end_pasado:
            return None  # precio cerca de certeza pero ventana aún no ha cerrado — reintentar

    decision = pred.get("decision", "")
    acierto = (decision == "BUY_YES" and outcome_real == "YES") or \
              (decision == "BUY_NO" and outcome_real == "NO")

    # P&L simulado.
    try:
        precio_entrada = float(pred.get("precio_yes_mercado", 0.5))
    except (ValueError, TypeError):
        precio_entrada = 0.5
    # Piso Y techo: precio_yes_mercado es una probabilidad, [0,1]. Un valor
    # corrupto por encima de 1 (dato upstream dañado) haría que un WIN real
    # se contabilizara como pérdida más abajo (payout = apuesta/precio_entrada
    # sale por debajo de la apuesta) — mismo patrón que ya se corrigió para
    # el caso "hacia 0", pero por el lado no cubierto.
    precio_entrada = min(0.99, max(0.01, precio_entrada))
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


def _brier(pred: dict, res: dict) -> str:
    """Brier score = (prob_modelo - outcome)². Proper scoring rule: se minimiza con la prob real."""
    try:
        p = float(pred.get("prob_yes_modelo", 0.5) or 0.5)
        o = float(res["acierto"])  # 1 si acertó YES, 0 si no
        # Para BUY_NO: el acierto es cuando outcome=NO (acierto=1 pero outcome_real=NO)
        # prob_yes_modelo < 0.5 para BUY_NO, outcome_real puede ser YES o NO
        outcome_yes = 1.0 if res["outcome_real"] == "YES" else 0.0
        return f"{(p - outcome_yes) ** 2:.4f}"
    except Exception:
        return ""


def _clv(pred: dict, res: dict) -> str:
    """
    Closing Line Value: mide si nuestra predicción tenía edge respecto al mercado.
    CLV = outcome_real - precio_entrada (para BUY_YES)
        = precio_entrada - outcome_real  (para BUY_NO)
    Positivo = compramos barato (el mercado estaba equivocado a nuestro favor).
    Promedio de CLV > 0 con n suficiente = edge real, no suerte.
    """
    try:
        precio = float(pred.get("precio_yes_mercado", 0.5) or 0.5)
        outcome_yes = 1.0 if res["outcome_real"] == "YES" else 0.0
        dec = pred.get("decision", "")
        if dec == "BUY_YES":
            return f"{outcome_yes - precio:.4f}"
        elif dec == "BUY_NO":
            return f"{precio - outcome_yes:.4f}"
        return ""
    except Exception:
        return ""


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Shadow resolve ===")

    pendientes = cargar_predicciones_pendientes()
    ya_resueltas = cargar_ya_resueltas()

    nuevos_resultados = []
    debug_no_resueltos = 0
    ahora = datetime.now(timezone.utc)

    # Filtrar predicciones que vale la pena consultar
    candidatas = []
    for pred in pendientes:
        if pred.get("decision", "") == "SKIP":
            continue  # SKIP no necesitan resolución
        clave = (pred.get("strategy", ""), pred.get("market_id", ""))
        if clave in ya_resueltas:
            continue
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
        candidatas.append(pred)

    # Obtener IDs únicos y descargar en paralelo (throttled)
    mids_unicos = list({p.get("market_id", "") for p in candidatas if p.get("market_id")})
    print(f"  Descargando {len(mids_unicos)} mercados en paralelo (workers=3, throttled)...")
    cache_mercados = fetch_mercados_paralelo(mids_unicos, workers=3)
    consultados_ids = set(mids_unicos)

    for pred in candidatas:
        clave = (pred.get("strategy", ""), pred.get("market_id", ""))
        if clave in ya_resueltas:
            continue
        mid = pred.get("market_id", "")
        mercado = cache_mercados.get(mid)
        res = evaluar(pred, mercado, ahora=ahora)
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
            "brier_score": _brier(pred, res),
            "clv": _clv(pred, res),
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

    # Cerrar trades live que hayan resuelto
    _cerrar_trades_live(nuevos_resultados, ts)


def _notificar_cierre_live(trade: dict, pnl_neto: float, acierto_dir: bool):
    """Envía notificación Telegram cuando un trade live se resuelve."""
    import os
    tok = os.environ.get("TELEGRAM_TOKEN", "")
    cid = os.environ.get("TELEGRAM_CHAT_ID", "")
    if not tok or not cid:
        return

    # Calcular bankroll actualizado y P&L del día leyendo trades.csv completo
    try:
        from live_stake import bankroll_actual, pnl_live_hoy, CAPITAL_OPERATIVO_INICIAL
        bkr   = bankroll_actual()
        pnl_d = pnl_live_hoy()
        bkr_ini = CAPITAL_OPERATIVO_INICIAL
        pnl_total = bkr - bkr_ini
    except Exception:
        bkr = pnl_d = pnl_total = 0.0

    signo   = "✅ WIN" if acierto_dir else "❌ LOSS"
    pnl_str = f"{pnl_neto:+.2f}€"
    q       = trade.get("question", "")[:55]
    entry_p = float(trade.get("entry_price") or 0)
    dir_    = trade.get("direction", "")
    sub     = trade.get("subtype", "")

    # Racha: contar wins/losses en trades.csv para el día
    try:
        trades_hoy = []
        LIVE_CSV = Path("data/live/trades.csv")
        hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        for row in csv.DictReader(open(LIVE_CSV, encoding="utf-8")):
            if row.get("status") == "CLOSED" and row.get("close_timestamp", "").startswith(hoy):
                trades_hoy.append(row)
        n_hoy  = len(trades_hoy)
        w_hoy  = sum(1 for r in trades_hoy if float(r.get("pnl_neto_eur", 0) or 0) > 0)
        racha  = f"{w_hoy}W/{n_hoy-w_hoy}L hoy"
    except Exception:
        racha = ""

    bkr_color = "📈" if bkr >= bkr_ini else "📉"
    msg = (
        f"{'🏆' if acierto_dir else '💸'} *TRADE LIVE — {signo}*\n"
        f"\n"
        f"Mercado: _{q}_\n"
        f"Dir: {dir_}  |  Entrada: {entry_p:.3f}  |  Sub: {sub}\n"
        f"P&L trade: *{pnl_str}*\n"
        f"\n"
        f"{bkr_color} Bankroll real: *{bkr:.2f}€*  ({pnl_total:+.2f}€ total)\n"
        f"Hoy: {pnl_d:+.2f}€  |  {racha}"
    )
    try:
        requests.post(
            f"https://api.telegram.org/bot{tok}/sendMessage",
            json={"chat_id": cid, "text": msg, "parse_mode": "Markdown"},
            timeout=10,
        )
        print(f"  [telegram] Resultado live enviado.")
    except Exception as e:
        print(f"  [telegram] Error notificando cierre live: {e}")


def _cerrar_trades_live(nuevos_resultados: list, ts: str):
    """Actualiza data/live/trades.csv: cierra trades OPEN cuyo mercado ya resolvió."""
    LIVE_CSV = Path("data/live/trades.csv")
    if not LIVE_CSV.exists():
        return

    # Índice de outcomes por market_id
    outcomes = {}
    for r in nuevos_resultados:
        outcomes[str(r["market_id"])] = {
            "outcome_real": r["outcome_real"],
            "acierto":      int(r["acierto"]),
        }

    trades = list(csv.DictReader(open(LIVE_CSV, encoding="utf-8")))
    modificado = False
    cierres = []

    for t in trades:
        if t.get("status") != "OPEN":
            continue
        mid = str(t.get("market_id", ""))
        if mid not in outcomes:
            continue

        outcome = outcomes[mid]["outcome_real"]
        acierto = outcomes[mid]["acierto"]
        direction = t.get("direction", "")
        acierto_dir = (direction == "BUY_YES" and outcome == "YES") or \
                      (direction == "BUY_NO"  and outcome == "NO")

        try:
            stake      = float(t.get("stake_eur") or 0)
            # Techo además de piso: mismo motivo que en evaluar() — un
            # entry_price corrupto >1 convertiría un WIN real en pérdida
            # via pnl_bruto = stake*(1/entry_p - 1) negativo.
            entry_p    = min(0.99, max(0.01, float(t.get("entry_price") or 0.5)))
            fee        = float(t.get("fee_eur") or 0)
        except ValueError:
            continue

        if acierto_dir and entry_p > 0:
            pnl_bruto = stake * (1.0 / entry_p - 1.0)
        else:
            pnl_bruto = -stake
        pnl_neto = pnl_bruto - fee

        t["status"]          = "CLOSED"
        t["close_timestamp"] = ts
        t["exit_price"]      = "1.0" if acierto_dir else "0.0"
        t["outcome_real"]    = outcome
        t["pnl_bruto_eur"]   = f"{pnl_bruto:.4f}"
        t["pnl_neto_eur"]    = f"{pnl_neto:.4f}"
        modificado = True
        cierres.append((t, pnl_neto, acierto_dir))
        signo = "✅" if acierto_dir else "❌"
        print(f"  {signo} Trade live cerrado: {t['strategy']}#{t['subtype']} "
              f"{direction} market={mid} PNL={pnl_neto:+.4f}€")

    if modificado:
        cols = list(trades[0].keys())
        with open(LIVE_CSV, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=cols)
            w.writeheader()
            w.writerows(trades)
        # Notificar cada cierre por Telegram
        for t, pnl_neto, acierto_dir in cierres:
            _notificar_cierre_live(t, pnl_neto, acierto_dir)

    actualizar_strategy_accuracy(nuevos_resultados, ts)

    print(f"[{ts}] === Fin shadow resolve ===")


if __name__ == "__main__":
    main()
