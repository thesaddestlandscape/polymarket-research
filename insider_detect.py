"""
insider_detect.py — detecta señales de actividad insider en mercados Polymarket.

Un movimiento brusco de precio (>8% en <2.5h) es la huella de una entrada de capital
con información privilegiada. Este script filtra las alertas del día y clasifica los
mercados candidatos según el tipo de pregunta:
  - ESPECIFICO: pregunta concreta no relacionada con precio cripto genérico → umbral 8%
  - CRIPTO:     pregunta de precio cripto genérica → umbral más alto (12%)

Shadow_predict.py usa este archivo para la estrategia INSIDER_FOLLOW.

Salida: data/wallets/insiders_YYYY-MM-DD.csv
"""
import csv
from datetime import datetime, timezone
from pathlib import Path

DIR_ALERTS  = Path("data/alerts")
DIR_WALLETS = Path("data/wallets")
DIR_WALLETS.mkdir(parents=True, exist_ok=True)

UMBRAL_ESPECIFICO = 8.0   # % mínimo para mercados específicos
UMBRAL_CRIPTO     = 12.0  # % mínimo para mercados genéricos de precio cripto

CRYPTO_GENERIC_KW = [
    "above", "below", "hit", "reach", "exceed", "over", "under",
    "btc", "eth", "sol", "bitcoin", "ethereum", "solana",
    "$", "usd", "price", "xrp", "doge", "bnb",
]


def es_mercado_generico(question: str) -> bool:
    q = question.lower()
    return sum(1 for kw in CRYPTO_GENERIC_KW if kw in q) >= 3


def cargar_alertas_hoy() -> list:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    archivo = DIR_ALERTS / f"alerts_{fecha}.csv"
    if not archivo.exists():
        return []
    with open(archivo, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def detectar_insiders(alertas: list) -> list:
    # Deduplicar por market_id: quedarse con la alerta de mayor cambio
    por_mercado = {}
    for a in alertas:
        mid = a.get("market_id", "")
        if not mid:
            continue
        try:
            cambio = float(a.get("cambio_pct", 0))
        except (ValueError, TypeError):
            continue
        if mid not in por_mercado or cambio > float(por_mercado[mid].get("cambio_pct", 0)):
            por_mercado[mid] = a

    insiders = []
    for mid, a in por_mercado.items():
        try:
            cambio_pct = float(a.get("cambio_pct", 0))
        except (ValueError, TypeError):
            continue

        question = a.get("question", "")
        generico = es_mercado_generico(question)
        umbral = UMBRAL_CRIPTO if generico else UMBRAL_ESPECIFICO

        if cambio_pct < umbral:
            continue

        insiders.append({
            "market_id": mid,
            "question": question,
            "end_date": a.get("end_date", ""),
            "direccion": a.get("direccion", ""),
            "cambio_pct": round(cambio_pct, 1),
            "py_actual": a.get("py_actual", ""),
            "liquidez": a.get("liquidez", ""),
            "ts_ref": a.get("ts_ref", ""),
            "ts_actual": a.get("ts_actual", ""),
            "tipo": "ESPECIFICO" if not generico else "CRIPTO",
            "confianza": "ALTA" if cambio_pct >= 12 else "MEDIA",
        })

    insiders.sort(key=lambda x: x["cambio_pct"], reverse=True)
    return insiders


def guardar_insiders(insiders: list, ts: str) -> Path:
    fecha = ts[:10]
    archivo = DIR_WALLETS / f"insiders_{fecha}.csv"
    columnas = [
        "timestamp_utc", "market_id", "question", "end_date",
        "direccion", "cambio_pct", "py_actual", "liquidez",
        "ts_ref", "ts_actual", "tipo", "confianza",
    ]
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=columnas)
        w.writeheader()
        for ins in insiders:
            ins["timestamp_utc"] = ts
            w.writerow(ins)
    return archivo


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Insider detect ===")

    alertas = cargar_alertas_hoy()
    print(f"  Alertas cargadas hoy: {len(alertas)}")

    insiders = detectar_insiders(alertas)
    print(f"  Señales insider detectadas: {len(insiders)}")

    if insiders:
        for ins in insiders[:5]:
            print(f"    {ins['confianza']:5s} {ins['tipo']:10s} "
                  f"{ins['direccion']:5s} {ins['cambio_pct']:5.1f}%  "
                  f"{ins['question'][:60]}")
        archivo = guardar_insiders(insiders, ts)
        print(f"  Guardado: {archivo}")
    else:
        print(f"  Sin señales insider hoy (umbral específico={UMBRAL_ESPECIFICO}%, cripto={UMBRAL_CRIPTO}%).")

    print(f"[{ts}] === Fin insider detect ===")


if __name__ == "__main__":
    main()
