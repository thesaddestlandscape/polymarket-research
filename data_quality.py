"""
data_quality.py — Guardián centralizado de calidad de datos.

Cinco capas de defensa:
  L1 validar_precio()        — bloquea datos malos al escribir en CSV
  L2 verificar_series()      — detecta gaps y datos stale en la serie temporal
  L3 validar_features_gbm()  — bloquea predicciones con features imposibles
  L4 validar_cross_source()  — consenso multi-fuente: Binance/Kraken/Coinbase/CoinGecko
  L5 generar_reporte()       — snapshot completo → data_quality.json visible en estado_actual.md

Fuentes de datos y rol en el sistema:
  Binance   — klines 1min + taker flow (PRIMARY: sigma_h, drift, order flow)
  Kraken    — klines 1min fallback (PRIMARY: cuando Binance no responde)
  Coinbase  — spot price (SETTLEMENT: Polymarket resuelve BTC/ETH a precio Coinbase)
  CoinGecko — spot price (SLOW: cada 23min, menor calidad, solo para gap filling)
  Polymarket — precios YES/NO + liquidez (MARKET: lo que apostamos)

Importado por: fetch_binance_klines, capture_markets, shadow_predict, shadow_resumen.
Ejecutable standalone para diagnóstico: python3 data_quality.py
"""
import csv
import json
import concurrent.futures
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

try:
    import requests as _requests
    _HAS_REQUESTS = True
except ImportError:
    _HAS_REQUESTS = False

# ─── Constantes de validación (fuente única de verdad) ───────────────────────

PRICE_RANGES: dict[str, tuple[float, float]] = {
    "BTC":   (20_000,  500_000),
    "ETH":   (200,      30_000),
    "SOL":   (2,         5_000),
    "XRP":   (0.02,        100),
    "DOGE":  (0.001,        20),
    "BNB":   (20,       10_000),
    "ADA":   (0.01,         50),
    "LINK":  (0.5,         500),
    "AVAX":  (1,         2_000),
    "DOT":   (0.1,         500),
    "LTC":   (5,         5_000),
}

SIGMA_H_MAX      = 0.05   # vol horaria >5%/h → precio corrupto en CSV
DRIFT_MAX        = 10.0   # drift >1000%/h → imposible en mercado spot
MAX_SPIKE_PCT    = 0.10   # salto >10% en 1 minuto → dato inválido
MAX_GAP_MIN      = 10     # sin datos >10 min → sigma_h y drift no fiables
STALE_WARN_MIN   = 5      # último precio >5 min → alerta leve

ASSETS_GBM = ["BTC", "ETH", "SOL", "XRP"]

# Umbral de divergencia entre fuentes: >0.5% en condiciones normales es una anomalía
# (Medición histórica: Binance vs Coinbase ≈ 0.15% de divergencia normal)
CROSS_SOURCE_WARN_PCT  = 0.005   # 0.5%  → alerta, revisar
CROSS_SOURCE_BLOCK_PCT = 0.020   # 2.0%  → precio infiable, no apostar ese activo
FETCH_TIMEOUT          = 6       # segundos por fuente en cross-source check

# Settlement reference: Polymarket resuelve BTC/ETH al precio Coinbase
# Si Coinbase y Binance divergen >0.5% → usar Coinbase como spot en las predicciones
SETTLEMENT_ASSETS = {"BTC", "ETH"}   # los que Polymarket resuelve contra Coinbase

DIR_SHADOW = Path("data/shadow")
DQ_PATH    = DIR_SHADOW / "data_quality.json"
DQ_LOG     = DIR_SHADOW / "dq_events.jsonl"   # log de rechazos (append-only)

# ─── L4: Fetchers multi-fuente ───────────────────────────────────────────────

def fetch_coinbase_spot(assets: Optional[list] = None,
                         timeout: int = FETCH_TIMEOUT) -> dict[str, float]:
    """
    Obtiene precios spot de Coinbase Advanced Trade API (pública, sin auth).
    Coinbase es la fuente de settlement de Polymarket para BTC y ETH.
    """
    if not _HAS_REQUESTS:
        return {}
    if assets is None:
        assets = ASSETS_GBM

    def _fetch_one(sym):
        try:
            r = _requests.get(
                f"https://api.coinbase.com/v2/prices/{sym}-USD/spot",
                timeout=timeout,
            )
            r.raise_for_status()
            price = float(r.json()["data"]["amount"])
            ok, _ = validar_precio(sym, price)
            return (sym, price) if ok else (sym, None)
        except Exception:
            return (sym, None)

    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(assets)) as ex:
        for sym, price in ex.map(_fetch_one, assets):
            if price is not None:
                results[sym] = price
    return results


def fetch_kraken_spot(assets: Optional[list] = None,
                       timeout: int = FETCH_TIMEOUT) -> dict[str, float]:
    """Obtiene precios spot de Kraken (sin auth)."""
    if not _HAS_REQUESTS:
        return {}
    PAIRS = {"BTC":"XBTUSD","ETH":"ETHUSD","SOL":"SOLUSD","XRP":"XRPUSD","DOGE":"DOGEUSD","BNB":"BNBUSD"}
    if assets is None:
        assets = ASSETS_GBM

    def _fetch_one(sym):
        pair = PAIRS.get(sym)
        if not pair:
            return (sym, None)
        try:
            r = _requests.get(
                f"https://api.kraken.com/0/public/Ticker?pair={pair}",
                timeout=timeout,
            )
            body = r.json()
            if body.get("error"):
                return (sym, None)
            result = body.get("result", {})
            key = next((k for k in result if k != "last"), None)
            if not key:
                return (sym, None)
            price = float(result[key]["c"][0])
            ok, _ = validar_precio(sym, price)
            return (sym, price) if ok else (sym, None)
        except Exception:
            return (sym, None)

    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(assets)) as ex:
        for sym, price in ex.map(_fetch_one, assets):
            if price is not None:
                results[sym] = price
    return results


# ─── L4: Validación cross-source ─────────────────────────────────────────────

def validar_cross_source(
    sources: dict[str, dict[str, float]],
    assets: Optional[list] = None,
) -> dict:
    """
    Compara precios entre múltiples fuentes para detectar anomalías.

    Args:
        sources: {'binance': {BTC: 60000, ETH: 1580, ...},
                  'coinbase': {BTC: 60120, ETH: 1576, ...},
                  'kraken':   {...}, ...}
        assets:  lista de activos a validar

    Returns:
        dict con:
          'consenso':  {sym: precio_mediana}   ← usar para predicciones
          'alertas':   [{sym, fuentes, max_div, accion}]
          'bloqueados': [sym]                  ← divergencia >2%
    """
    if assets is None:
        assets = ASSETS_GBM

    consenso: dict[str, float] = {}
    alertas: list[dict] = []
    bloqueados: list[str] = []

    for sym in assets:
        precios_por_fuente = {
            nombre: prices[sym]
            for nombre, prices in sources.items()
            if prices.get(sym) is not None
        }
        if not precios_por_fuente:
            continue

        vals = list(precios_por_fuente.values())
        if len(vals) == 1:
            consenso[sym] = vals[0]
            continue

        # Mediana como precio de consenso (robusto a un outlier)
        sorted_vals = sorted(vals)
        n = len(sorted_vals)
        mediana = sorted_vals[n // 2] if n % 2 else (sorted_vals[n//2-1] + sorted_vals[n//2]) / 2

        max_div = (max(vals) - min(vals)) / min(vals)
        outlier = max(precios_por_fuente, key=lambda k: abs(precios_por_fuente[k] - mediana))

        if max_div >= CROSS_SOURCE_BLOCK_PCT:
            bloqueados.append(sym)
            alertas.append({
                "sym": sym, "max_div_pct": round(max_div * 100, 3),
                "fuentes": precios_por_fuente, "consenso": mediana,
                "accion": "BLOQUEADO",
            })
            _log_evento(sym, precios_por_fuente.get(outlier, 0),
                        f"cross_source_block {outlier}={precios_por_fuente.get(outlier):.4f} vs mediana={mediana:.4f} ({max_div*100:.2f}%)")
        elif max_div >= CROSS_SOURCE_WARN_PCT:
            alertas.append({
                "sym": sym, "max_div_pct": round(max_div * 100, 3),
                "fuentes": precios_por_fuente, "consenso": mediana,
                "accion": "ALERTA",
            })
            _log_evento(sym, precios_por_fuente.get(outlier, 0),
                        f"cross_source_warn {outlier}={precios_por_fuente.get(outlier):.4f} vs mediana={mediana:.4f} ({max_div*100:.2f}%)")

        consenso[sym] = mediana

    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "fuentes_activas": list(sources.keys()),
        "consenso": consenso,
        "alertas": alertas,
        "bloqueados": bloqueados,
    }


def obtener_consensus_spot(
    binance_prices: Optional[dict] = None,
    assets: Optional[list] = None,
    timeout: int = FETCH_TIMEOUT,
) -> dict:
    """
    Obtiene precio de consenso multi-fuente. Llamado desde fetch_binance_klines.
    Prioriza Coinbase para activos de settlement (BTC, ETH).

    Retorna:
      'precios':   {sym: float}  — precio a usar en predicciones
      'cross':     resultado de validar_cross_source
      'fuente_preferida': {sym: 'binance'|'coinbase'|'kraken'|'consenso'}
    """
    if assets is None:
        assets = ASSETS_GBM

    # Fetch Coinbase y Kraken en paralelo (Binance ya fue fetcheado por el caller)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as ex:
        f_cb = ex.submit(fetch_coinbase_spot, assets, timeout)
        f_kr = ex.submit(fetch_kraken_spot, assets, timeout)
        coinbase = f_cb.result()
        kraken   = f_kr.result()

    sources: dict[str, dict] = {}
    if binance_prices:
        sources["binance"] = {k: v for k, v in binance_prices.items() if k in assets}
    if coinbase:
        sources["coinbase"] = coinbase
    if kraken:
        sources["kraken"] = kraken

    cross = validar_cross_source(sources, assets)

    # Para settlement assets (BTC, ETH): usar Coinbase si está disponible y no bloqueado
    precios: dict[str, float] = {}
    fuente_elegida: dict[str, str] = {}
    for sym in assets:
        if sym in cross["bloqueados"]:
            continue   # no usar precio infiable
        if sym in SETTLEMENT_ASSETS and sym in coinbase:
            precios[sym] = coinbase[sym]
            fuente_elegida[sym] = "coinbase"
        elif cross["consenso"].get(sym):
            precios[sym] = cross["consenso"][sym]
            fuente_elegida[sym] = "consenso"
        elif binance_prices and sym in binance_prices:
            precios[sym] = binance_prices[sym]
            fuente_elegida[sym] = "binance"

    return {
        "precios": precios,
        "cross": cross,
        "fuente_elegida": fuente_elegida,
    }

# ─── L1: Validación en punto de escritura ────────────────────────────────────

def validar_precio(sym: str, price: float,
                   last_price: Optional[float] = None) -> tuple[bool, str]:
    """
    Valida un precio antes de escribirlo al CSV.
    Retorna (True, "OK") o (False, motivo_legible).
    Registra automáticamente rechazos en dq_events.jsonl.
    """
    try:
        price = float(price)
    except (TypeError, ValueError):
        return False, "no_es_numero"

    lo, hi = PRICE_RANGES.get(sym.upper(), (0, 1e18))
    if not (lo <= price <= hi):
        motivo = f"rango [{price:.6g}] esperado [{lo}, {hi}]"
        _log_evento(sym, price, motivo)
        return False, motivo

    if last_price is not None and last_price > 0:
        jump = abs(price / last_price - 1)
        if jump > MAX_SPIKE_PCT:
            motivo = f"spike {last_price:.6g}→{price:.6g} ({jump*100:.1f}%)"
            _log_evento(sym, price, motivo)
            return False, motivo

    return True, "OK"


def leer_ultimo_precio(sym: str, prices_path: Path) -> Optional[float]:
    """Lee el último precio válido de un símbolo desde el CSV del día."""
    if not prices_path.exists():
        return None
    last: Optional[float] = None
    try:
        with open(prices_path, "r", newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if row.get("asset", "").strip().upper() == sym.upper():
                    try:
                        last = float(row["price_usd"])
                    except (ValueError, TypeError):
                        pass
    except Exception:
        pass
    return last


def _log_evento(sym: str, value: float, reason: str) -> None:
    try:
        DIR_SHADOW.mkdir(parents=True, exist_ok=True)
        evento = {
            "ts":     datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "sym":    sym.upper(),
            "value":  round(float(value), 8),
            "reason": reason,
        }
        with open(DQ_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(evento, ensure_ascii=False) + "\n")
    except Exception:
        pass


# ─── L2: Validación de series temporales ─────────────────────────────────────

def verificar_series(precios_data: list,
                      assets: Optional[list] = None,
                      ahora: Optional[datetime] = None) -> dict:
    """
    Analiza la continuidad temporal de precios para cada asset.
    Retorna dict[sym] con: estado (OK/DEGRADED/CRITICAL), gaps, age_seconds, alertas.
    """
    if assets is None:
        assets = ASSETS_GBM
    if ahora is None:
        ahora = datetime.now(timezone.utc)

    resultado: dict = {}
    for sym in assets:
        puntos = sorted([
            (ts, prices[sym])
            for ts, prices in precios_data
            if sym in prices
        ])

        if not puntos:
            resultado[sym] = {
                "estado": "CRITICAL", "n": 0, "age_seconds": None,
                "ultimo_precio": None,
                "gaps": [{"inicio": "N/A", "fin": "N/A", "duracion_min": 9999}],
                "alertas": ["SIN_DATOS_EN_CSV"],
            }
            continue

        last_ts, last_price = puntos[-1]
        age_s = (ahora - last_ts).total_seconds()

        # Detectar gaps internos (>MAX_GAP_MIN entre dos puntos consecutivos)
        gaps = []
        for i in range(1, len(puntos)):
            delta_min = (puntos[i][0] - puntos[i-1][0]).total_seconds() / 60
            if delta_min > MAX_GAP_MIN:
                gaps.append({
                    "inicio":      puntos[i-1][0].isoformat()[:19],
                    "fin":         puntos[i][0].isoformat()[:19],
                    "duracion_min": round(delta_min, 1),
                })

        alertas: list[str] = []
        estado = "OK"

        # Dato stale
        if age_s > MAX_GAP_MIN * 60:
            alertas.append(f"stale {age_s/60:.0f}min sin actualizar")
            estado = "CRITICAL"
        elif age_s > STALE_WARN_MIN * 60:
            alertas.append(f"precio viejo ({age_s/60:.1f}min)")
            estado = "DEGRADED"

        # Gap histórico en la última ventana
        if gaps:
            worst = max(gaps, key=lambda g: g["duracion_min"])
            alertas.append(f"gap {worst['duracion_min']:.0f}min ({worst['inicio'][11:16]})")
            if worst["duracion_min"] > MAX_GAP_MIN * 3:
                if estado != "CRITICAL":
                    estado = "DEGRADED"

        resultado[sym] = {
            "estado":        estado,
            "n":             len(puntos),
            "age_seconds":   round(age_s, 1),
            "ultimo_precio": last_price,
            "gaps":          gaps,
            "alertas":       alertas,
        }

    return resultado


# ─── L3: Validación de features del modelo ───────────────────────────────────

def validar_features_gbm(sigma_h: Optional[float],
                          drift_60: Optional[float] = None,
                          drift_15: Optional[float] = None) -> tuple[bool, str]:
    """
    Valida features antes de computar p_up en s_updown_gbm.
    (True, "OK") o (False, motivo) — si False la predicción se descarta.
    """
    if sigma_h is None or sigma_h <= 0:
        return False, "sigma_h=None_o_cero"
    if sigma_h > SIGMA_H_MAX:
        return False, f"sigma_h={sigma_h:.5f} > {SIGMA_H_MAX} (corrupcion_de_precios)"
    if drift_60 is not None and abs(drift_60) > DRIFT_MAX:
        return False, f"drift_60={drift_60:.2f} > {DRIFT_MAX} (imposible)"
    if drift_15 is not None and abs(drift_15) > DRIFT_MAX:
        return False, f"drift_15={drift_15:.2f} > {DRIFT_MAX} (imposible)"
    return True, "OK"


# ─── L4: Reporte de calidad ───────────────────────────────────────────────────

def _contar_rechazos(ventana_min: int = 60) -> dict:
    """Cuenta eventos de rechazo en dq_events.jsonl en los últimos ventana_min minutos."""
    conteo: dict = {"rango": 0, "spike": 0, "total": 0, "por_sym": {}}
    if not DQ_LOG.exists():
        return conteo
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=ventana_min)
    try:
        with open(DQ_LOG, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    ev = json.loads(line)
                    ts = datetime.fromisoformat(ev["ts"])
                    if ts < cutoff:
                        continue
                    conteo["total"] += 1
                    r = ev.get("reason", "")
                    if "rango" in r:
                        conteo["rango"] += 1
                    if "spike" in r:
                        conteo["spike"] += 1
                    sym = ev.get("sym", "?")
                    conteo["por_sym"][sym] = conteo["por_sym"].get(sym, 0) + 1
                except Exception:
                    pass
    except Exception:
        pass
    return conteo


def generar_reporte(precios_data: list,
                     assets: Optional[list] = None,
                     cross_result: Optional[dict] = None) -> dict:
    """
    Genera snapshot completo de calidad de datos.
    Escribe data/shadow/data_quality.json y lo retorna.

    Args:
        precios_data: output de cargar_precios_intraday()
        assets:       lista de activos a analizar
        cross_result: output previo de validar_cross_source() si está disponible
                      (evita re-fetch de fuentes externas)
    """
    if assets is None:
        assets = ASSETS_GBM

    series   = verificar_series(precios_data, assets)
    rechazos = _contar_rechazos(60)

    estado_global = "OK"
    alertas_globales: list[str] = []

    for sym, info in series.items():
        if info["estado"] == "CRITICAL":
            estado_global = "CRITICAL"
        elif info["estado"] == "DEGRADED" and estado_global == "OK":
            estado_global = "DEGRADED"
        alertas_globales.extend([f"{sym}:{a}" for a in info["alertas"]])

    if rechazos["total"] > 5 and estado_global == "OK":
        estado_global = "DEGRADED"
    if rechazos["total"] > 0:
        alertas_globales.append(
            f"rechazos_1h:{rechazos['total']} (rango={rechazos['rango']}, spike={rechazos['spike']})"
        )

    # Integrar resultado cross-source si fue pasado
    if cross_result:
        if cross_result.get("bloqueados"):
            if estado_global != "CRITICAL":
                estado_global = "CRITICAL"
            for sym in cross_result["bloqueados"]:
                alertas_globales.append(f"{sym}:cross_source_BLOQUEADO")
        for alerta in cross_result.get("alertas", []):
            if alerta.get("accion") == "ALERTA":
                alertas_globales.append(
                    f"{alerta['sym']}:divergencia_{alerta['max_div_pct']:.2f}%"
                )
                if estado_global == "OK":
                    estado_global = "DEGRADED"

    reporte = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "estado_global": estado_global,
        "alertas":       alertas_globales,
        "rechazos_1h":   rechazos,
        "assets":        series,
        "cross_source":  cross_result or {},
    }

    try:
        DIR_SHADOW.mkdir(parents=True, exist_ok=True)
        with open(DQ_PATH, "w", encoding="utf-8") as f:
            json.dump(reporte, f, indent=2, ensure_ascii=False, default=str)
    except Exception as e:
        print(f"  [DQ] Error escribiendo reporte: {e}")

    return reporte


def leer_estado_calidad() -> dict:
    """Lee el último reporte de calidad generado (lectura rápida para otros módulos)."""
    if not DQ_PATH.exists():
        return {"estado_global": "DESCONOCIDO", "alertas": [], "assets": {}}
    try:
        with open(DQ_PATH, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"estado_global": "ERROR_LECTURA", "alertas": [], "assets": {}}


def simbolo_bloqueado(sym: str) -> bool:
    """True si el asset está en estado CRITICAL y las predicciones deben omitirse."""
    dq = leer_estado_calidad()
    info = dq.get("assets", {}).get(sym.upper(), {})
    return info.get("estado") == "CRITICAL"


# ─── Diagnóstico standalone ──────────────────────────────────────────────────

if __name__ == "__main__":
    print("Cargando datos de precios locales...")
    try:
        from shadow_predict import cargar_precios_intraday
        data = cargar_precios_intraday()
        print(f"  {len(data)} registros en CSV")
    except Exception as e:
        print(f"  [ERROR] No se pudieron cargar precios: {e}")
        data = []

    # Fetch Binance en paralelo para cross-source
    print("Consultando fuentes externas (Binance + Coinbase + Kraken)...")
    binance_now: dict = {}
    if _HAS_REQUESTS:
        def _fetch_bn(sym):
            try:
                r = _requests.get(
                    f"https://api.binance.com/api/v3/ticker/price?symbol={sym}USDT",
                    timeout=FETCH_TIMEOUT,
                )
                return sym, float(r.json()["price"])
            except Exception:
                return sym, None
        with concurrent.futures.ThreadPoolExecutor() as ex:
            for sym, p in ex.map(_fetch_bn, ASSETS_GBM):
                if p:
                    binance_now[sym] = p

    consensus = obtener_consensus_spot(binance_now, ASSETS_GBM)
    cross = consensus["cross"]
    reporte = generar_reporte(data, cross_result=cross)

    iconos = {"OK": "✅", "DEGRADED": "⚠️", "CRITICAL": "🚨", "DESCONOCIDO": "❓"}
    print(f"\n{'═'*60}")
    print(f" CALIDAD DE DATOS: {iconos.get(reporte['estado_global'], '?')} {reporte['estado_global']}")
    print(f" {reporte['timestamp_utc']}")
    print(f"{'═'*60}")

    # Series temporales
    print("\n── Series temporales ──────────────────────────────────────")
    for sym, info in reporte["assets"].items():
        ic = iconos.get(info["estado"], "?")
        age_str = (f"{info['age_seconds']/60:.1f}min"
                   if info["age_seconds"] is not None else "N/A")
        px_str  = (f"${info['ultimo_precio']:,.4f}"
                   if info["ultimo_precio"] else "N/A")
        gaps_s  = f"  [{len(info['gaps'])} gap(s)]" if info["gaps"] else ""
        print(f"  {ic} {sym:6s}: {px_str:>16}  ({age_str} ago)  n={info['n']}{gaps_s}")
        for a in info["alertas"]:
            print(f"       └─ ⚠ {a}")

    # Cross-source
    print("\n── Cross-source: Binance / Coinbase / Kraken ──────────────")
    print(f"  Fuentes activas: {cross.get('fuentes_activas', [])}")
    print(f"  {'Asset':6} {'Consenso':>18}  {'Fuente pred':>14}  {'Div%':>7}")
    for sym in ASSETS_GBM:
        px_c = cross.get("consenso", {}).get(sym)
        fe   = consensus.get("fuente_elegida", {}).get(sym, "—")
        blk  = " 🚨BLOQUEADO" if sym in cross.get("bloqueados", []) else ""
        div_str = ""
        for a in cross.get("alertas", []):
            if a["sym"] == sym:
                div_str = f"{a['max_div_pct']:.3f}%"
        px_str = f"${px_c:>16,.4f}" if px_c else "          N/A"
        print(f"  {sym:6} {px_str}  {fe:>14}  {div_str:>7}{blk}")

    if cross.get("alertas"):
        print("\n  Divergencias:")
        for a in cross["alertas"]:
            icon = "🚨" if a["accion"] == "BLOQUEADO" else "⚠️"
            fs = "  ".join([f"{k}=${v:,.2f}" for k, v in a["fuentes"].items()])
            print(f"    {icon} {a['sym']}: {fs}  div={a['max_div_pct']}%")

    # Rechazos
    r = reporte["rechazos_1h"]
    if r["total"] > 0:
        print(f"\n── Rechazos última hora ──────────────────────────────────")
        print(f"  Total: {r['total']}  (rango={r['rango']}  spike={r['spike']})")
        if r.get("por_sym"):
            print(f"  Por asset: {r['por_sym']}")

    if reporte["alertas"]:
        print(f"\n── Alertas activas ({len(reporte['alertas'])}) ──────────────────────────────")
        for a in reporte["alertas"]:
            print(f"    ⚠ {a}")
    else:
        print("\n  Sin alertas. Pipeline completamente limpio ✅")
