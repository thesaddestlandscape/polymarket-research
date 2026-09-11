"""
price_alerts.py — detecta movimientos bruscos en precio YES de mercados.

Compara el precio YES actual con el de hace ~2h en los datos capturados.
Si el cambio supera el umbral, genera una alerta. Esto indica que alguien
grande ha entrado en el mercado — señal que SMART_FLOW no captura sin trades.

Salida: data/alerts/alerts_YYYY-MM-DD.csv (acumulativo del día)
"""
import csv
import glob
from datetime import datetime, timezone, timedelta
from pathlib import Path

DIR_MARKETS = Path("data/markets")
DIR_ALERTS  = Path("data/alerts")
DIR_ALERTS.mkdir(parents=True, exist_ok=True)

UMBRAL_CAMBIO   = 0.05   # 5% de movimiento mínimo para generar alerta
VENTANA_HORAS   = 2.5    # ventana de comparación
MIN_LIQUIDEZ    = 1000   # ignorar mercados con liquidez < $1000


def cargar_historial_reciente() -> dict:
    corte = datetime.now(timezone.utc) - timedelta(hours=VENTANA_HORAS * 2)
    historial = {}
    archivos = sorted(glob.glob(str(DIR_MARKETS / "*.csv")))[-3:]
    for arch in archivos:
        try:
            with open(arch, encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    ts_str = row.get("timestamp_utc", "")
                    try:
                        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                    except Exception:
                        continue
                    if ts < corte:
                        continue
                    mid = row.get("market_id", "")
                    py_str = row.get("price_yes", "")
                    if not mid or not py_str:
                        continue
                    try:
                        py = float(py_str)
                        liq = float(row.get("liquidity", 0) or 0)
                    except (ValueError, TypeError):
                        continue
                    historial.setdefault(mid, []).append((
                        ts, py,
                        row.get("question", ""),
                        row.get("end_date", ""),
                        liq,
                    ))
        except Exception as e:
            print(f"  Error leyendo {arch}: {e}")

    for mid in historial:
        historial[mid].sort(key=lambda x: x[0])
    return historial


def detectar_alertas(historial: dict) -> list:
    ahora = datetime.now(timezone.utc)
    corte_ref = ahora - timedelta(hours=VENTANA_HORAS)
    alertas = []

    for mid, obs in historial.items():
        if len(obs) < 2:
            continue
        ts_actual, py_actual, question, end_date, liq = obs[-1]
        if liq < MIN_LIQUIDEZ:
            continue
        if not (0.02 < py_actual < 0.98):
            continue
        refs = [(ts, py) for ts, py, *_ in obs if ts <= corte_ref]
        if not refs:
            continue
        ts_ref, py_ref = refs[0]
        cambio = py_actual - py_ref
        cambio_abs = abs(cambio)
        if cambio_abs < UMBRAL_CAMBIO:
            continue
        direccion = "SUBE" if cambio > 0 else "BAJA"
        minutos_transcurridos = int((ts_actual - ts_ref).total_seconds() / 60)
        alertas.append({
            "market_id": mid,
            "question": question,
            "end_date": end_date[:19] if end_date else "",
            "direccion": direccion,
            "py_ref": round(py_ref, 4),
            "py_actual": round(py_actual, 4),
            "cambio_abs": round(cambio_abs, 4),
            "cambio_pct": round(cambio_abs * 100, 1),
            "minutos": minutos_transcurridos,
            "liquidez": round(liq, 0),
            "ts_ref": ts_ref.isoformat(timespec="seconds"),
            "ts_actual": ts_actual.isoformat(timespec="seconds"),
        })

    alertas.sort(key=lambda x: x["cambio_abs"], reverse=True)
    return alertas


def guardar_alertas(alertas: list, ts: str) -> Path:
    fecha = ts[:10]
    archivo = DIR_ALERTS / f"alerts_{fecha}.csv"
    nuevo = not archivo.exists()
    columnas = [
        "timestamp_utc", "market_id", "question", "end_date",
        "direccion", "py_ref", "py_actual", "cambio_abs", "cambio_pct",
        "minutos", "liquidez", "ts_ref", "ts_actual",
    ]
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        if nuevo:
            w.writeheader()
        for a in alertas:
            a["timestamp_utc"] = ts
            w.writerow(a)
    return archivo


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Price alerts ===")

    historial = cargar_historial_reciente()
    print(f"  Mercados con historial reciente: {len(historial)}")

    alertas = detectar_alertas(historial)
    print(f"  Alertas detectadas (cambio ≥{UMBRAL_CAMBIO*100:.0f}%): {len(alertas)}")

    if alertas:
        print(f"  TOP alertas:")
        for a in alertas[:8]:
            print(f"    {a['direccion']:5s} {a['cambio_pct']:4.1f}% "
                  f"({a['py_ref']:.2f}→{a['py_actual']:.2f}) "
                  f"en {a['minutos']}min  liq=${a['liquidez']:,.0f}  "
                  f"{a['question'][:55]}")
        archivo = guardar_alertas(alertas, ts)
        print(f"  Guardado: {archivo}")
    else:
        print(f"  Sin movimientos bruscos en esta ventana.")

    print(f"[{ts}] === Fin price alerts ===")


if __name__ == "__main__":
    main()
