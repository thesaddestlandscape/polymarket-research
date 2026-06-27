"""
data_quality.py — Guardián centralizado de calidad de datos.

Cuatro capas de defensa:
  L1 validar_precio()      — bloquea datos malos al escribir en CSV
  L2 verificar_series()    — detecta gaps y datos stale en la serie temporal
  L3 validar_features_gbm()— bloquea predicciones con features imposibles
  L4 generar_reporte()     — snapshot del estado → data_quality.json

Importado por: fetch_binance_klines, capture_markets, shadow_predict, shadow_resumen.
Ejecutable standalone para diagnóstico: python3 data_quality.py
"""
import csv
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Optional

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

DIR_SHADOW = Path("data/shadow")
DQ_PATH    = DIR_SHADOW / "data_quality.json"
DQ_LOG     = DIR_SHADOW / "dq_events.jsonl"   # log de rechazos (append-only)

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
                     assets: Optional[list] = None) -> dict:
    """
    Genera snapshot completo de calidad de datos.
    Escribe data/shadow/data_quality.json y lo retorna.
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

    reporte = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "estado_global": estado_global,
        "alertas":       alertas_globales,
        "rechazos_1h":   rechazos,
        "assets":        series,
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
    print("Cargando datos de precios...")
    try:
        from shadow_predict import cargar_precios_intraday
        data = cargar_precios_intraday()
        print(f"  {len(data)} registros")
    except Exception as e:
        print(f"  [ERROR] No se pudieron cargar precios: {e}")
        data = []

    reporte = generar_reporte(data)

    iconos = {"OK": "✅", "DEGRADED": "⚠️", "CRITICAL": "🚨", "DESCONOCIDO": "❓"}
    print(f"\n{'═'*55}")
    print(f" CALIDAD DE DATOS: {iconos.get(reporte['estado_global'], '?')} {reporte['estado_global']}")
    print(f" {reporte['timestamp_utc']}")
    print(f"{'═'*55}")

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

    r = reporte["rechazos_1h"]
    if r["total"] > 0:
        print(f"\n  Rechazos última hora: {r['total']}  "
              f"(rango={r['rango']}  spike={r['spike']})")
        if r.get("por_sym"):
            print(f"  Por asset: {r['por_sym']}")

    if reporte["alertas"]:
        print("\n  Alertas activas:")
        for a in reporte["alertas"]:
            print(f"    ⚠ {a}")
    else:
        print("\n  Sin alertas. Pipeline limpio.")
