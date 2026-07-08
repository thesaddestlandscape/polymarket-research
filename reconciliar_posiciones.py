"""
reconciliar_posiciones.py — Guardia de reconciliación POSICIÓN A POSICIÓN
(complementa reconciliar.py, que solo mira el balance agregado).

Item 9 del checklist 08-Jul: FOK cubre el 99% de los casos (todo-o-nada →
"unfilled"="sin posición"), pero queda el residuo de timeout-tras-fill o
mismatch de parsing. Esta guardia lo cacha comparando lo que el CLOB dice
que tenemos (data-api/positions, público, sin clave) contra lo que
trades.csv cree.

Dos anomalías, ambas fail-loud (avisan, no actúan):
  A) POSICION_FANTASMA — el CLOB tiene valor real (currentValue>UMBRAL_DUST)
     en un mercado que no aparece en NINGUNA fila de trades.csv. Puede ser
     un fill que no se registró.
  B) CANJE_ATASCADO — trades.csv marca CLOSED hace >UMBRAL_CANJE_MIN minutos
     pero el CLOB sigue mostrando valor en esa posición (el canje on-chain
     no ha aterrizado). Normal unos minutos (ver sesión 08-Jul, lag de
     Polymarket); solo alerta si se pasa del umbral.
  C) TRADE_OPEN_HUERFANO — trades.csv marca OPEN con end_date ya pasado hace
     >UMBRAL_OPEN_MIN minutos y el CLOB no muestra ninguna posición viva
     para ese mercado — el resolver pudo saltárselo.

Determinista y read-only: no toca órdenes, config ni frenos. Escribe solo su
historial (data/live/reconciliacion_posiciones.csv) y avisa por Telegram,
una vez por anomalía (data/live/posiciones_notificadas.json evita repetir
el mismo aviso cada ciclo; se limpia sola cuando la anomalía se resuelve).

Cron sugerido: cada hora, en :20 (no coincide con live_balance :00/:15/:30/:45
ni con reconciliar 05:50).
"""
import csv
import glob
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = Path(__file__).parent
DIR_LIVE = BASE / "data" / "live"
TRADES_PATH = DIR_LIVE / "trades.csv"
HIST_PATH = DIR_LIVE / "reconciliacion_posiciones.csv"
NOTIF_PATH = DIR_LIVE / "posiciones_notificadas.json"
MARKETS_GLOB = str(BASE / "data" / "markets" / "*.csv")
DATA_API = "https://data-api.polymarket.com"

UMBRAL_DUST = 0.05        # $ por debajo de esto se ignora (redondeo/residuo sin valor)
UMBRAL_CANJE_MIN = 90     # minutos tras CLOSED antes de alertar canje atascado
UMBRAL_OPEN_MIN = 60      # minutos tras end_date antes de alertar OPEN huérfano

from dotenv import load_dotenv
load_dotenv(DIR_LIVE / ".env")
from shadow_digest import enviar_telegram  # noqa: E402


def cargar_wallet() -> str | None:
    import os
    return os.getenv("POLY_DEPOSIT_WALLET")


def fetch_posiciones(wallet: str) -> list:
    r = requests.get(f"{DATA_API}/positions", params={"user": wallet}, timeout=20)
    r.raise_for_status()
    return r.json() or []


def mapear_condition_a_market(condition_ids: set) -> dict:
    """condition_id -> market_id vía grep dirigido (los CSV de markets pesan
    cientos de MB/día, no parsear entero). csv.reader real (no split(",")
    ingenuo: question lleva comas dentro de comillas)."""
    if not condition_ids:
        return {}
    ids_file = "/tmp/_reconciliar_cids.txt"
    Path(ids_file).write_text("\n".join(sorted(condition_ids)))
    try:
        out = subprocess.run(
            ["grep", "-h", "-F", "-f", ids_file] + sorted(glob.glob(MARKETS_GLOB)),
            capture_output=True, text=True, timeout=120,
        ).stdout
    finally:
        Path(ids_file).unlink(missing_ok=True)

    mapa = {}
    for parts in csv.reader(out.splitlines()):
        if len(parts) < 3:
            continue
        cid = parts[2]
        if cid in condition_ids and cid not in mapa:
            mapa[cid] = parts[1]  # market_id
    return mapa


def cargar_trades() -> list[dict]:
    if not TRADES_PATH.exists():
        return []
    with open(TRADES_PATH, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def cargar_notificadas() -> dict:
    try:
        return json.loads(NOTIF_PATH.read_text()) if NOTIF_PATH.exists() else {}
    except Exception:
        return {}


def guardar_notificadas(d: dict):
    NOTIF_PATH.write_text(json.dumps(d, indent=2))


def guardar_historial(filas: list[dict]):
    campos = ["ts", "tipo", "market_id", "detalle"]
    nuevo = not HIST_PATH.exists()
    with open(HIST_PATH, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos)
        if nuevo:
            w.writeheader()
        w.writerows(filas)


def main() -> int:
    ahora = datetime.now(timezone.utc)
    wallet = cargar_wallet()
    if not wallet:
        print("[reconciliar_posiciones] POLY_DEPOSIT_WALLET no encontrado — abortando.")
        return 1

    try:
        posiciones = fetch_posiciones(wallet)
    except Exception as e:
        print(f"[reconciliar_posiciones] fetch_posiciones falló: {e} — sin dato hoy, no alarmar en falso.")
        return 1

    posiciones_valor = [p for p in posiciones if float(p.get("currentValue") or 0) > UMBRAL_DUST]
    condition_ids = {p["conditionId"] for p in posiciones_valor if p.get("conditionId")}
    mapa_cid_mid = mapear_condition_a_market(condition_ids)

    trades = cargar_trades()
    trades_por_mid = {}
    for r in trades:
        trades_por_mid.setdefault(r.get("market_id", ""), []).append(r)

    anomalias = []

    # A) POSICION_FANTASMA + B) CANJE_ATASCADO
    for p in posiciones_valor:
        cid = p.get("conditionId", "")
        mid = mapa_cid_mid.get(cid)
        valor = float(p.get("currentValue") or 0)
        filas_mid = trades_por_mid.get(mid, []) if mid else []

        if not filas_mid:
            anomalias.append({
                "tipo": "POSICION_FANTASMA",
                "market_id": mid or f"cid:{cid[:12]}…",
                "detalle": f"{p.get('title','?')} valor=${valor:.2f} sin fila en trades.csv",
            })
            continue

        # última fila conocida de ese mercado (puede haber solo una en la práctica)
        fila = sorted(filas_mid, key=lambda r: r.get("timestamp_utc", ""))[-1]
        if fila.get("status") == "CLOSED":
            try:
                cierre = datetime.fromisoformat(fila["close_timestamp"].replace("Z", "+00:00"))
                if cierre.tzinfo is None:
                    cierre = cierre.replace(tzinfo=timezone.utc)
                edad_min = (ahora - cierre).total_seconds() / 60.0
            except Exception:
                edad_min = None
            if edad_min is not None and edad_min > UMBRAL_CANJE_MIN:
                anomalias.append({
                    "tipo": "CANJE_ATASCADO",
                    "market_id": mid,
                    "detalle": f"{p.get('title','?')} CLOSED hace {edad_min:.0f}min, "
                               f"CLOB aún muestra valor=${valor:.2f}",
                })

    # C) TRADE_OPEN_HUERFANO — OPEN con end_date pasado, sin posición real con valor
    mids_con_valor = {mapa_cid_mid.get(p.get("conditionId", "")) for p in posiciones_valor}
    for r in trades:
        if r.get("status") != "OPEN":
            continue
        try:
            end_dt = datetime.fromisoformat(r["end_date"].replace("Z", "+00:00"))
            if end_dt.tzinfo is None:
                end_dt = end_dt.replace(tzinfo=timezone.utc)
            edad_min = (ahora - end_dt).total_seconds() / 60.0
        except Exception:
            continue
        if edad_min > UMBRAL_OPEN_MIN and r.get("market_id") not in mids_con_valor:
            anomalias.append({
                "tipo": "TRADE_OPEN_HUERFANO",
                "market_id": r.get("market_id"),
                "detalle": f"{r.get('question','?')} OPEN desde hace {edad_min:.0f}min tras "
                           f"end_date, sin posición real en el CLOB — ¿el resolver lo saltó?",
            })

    # Persistir historial (append, cada corrida)
    filas_hist = [{"ts": ahora.isoformat(timespec="seconds"), "tipo": a["tipo"],
                    "market_id": a["market_id"], "detalle": a["detalle"]} for a in anomalias]
    if filas_hist:
        guardar_historial(filas_hist)

    print(f"[reconciliar_posiciones] {ahora.isoformat(timespec='seconds')} "
          f"posiciones_con_valor={len(posiciones_valor)} anomalias={len(anomalias)}")
    for a in anomalias:
        print(f"  ⚠️ {a['tipo']} {a['market_id']}: {a['detalle']}")

    # Telegram solo para anomalías nuevas (evita spam en cada corrida horaria)
    notificadas = cargar_notificadas()
    claves_activas = set()
    nuevas = []
    for a in anomalias:
        clave = f"{a['tipo']}:{a['market_id']}"
        claves_activas.add(clave)
        if clave not in notificadas:
            nuevas.append(a)
            notificadas[clave] = {"detalle": a["detalle"], "ts": ahora.isoformat(timespec="seconds")}

    # limpiar las que ya no aparecen (se resolvieron solas)
    for clave in list(notificadas):
        if clave not in claves_activas:
            del notificadas[clave]
    guardar_notificadas(notificadas)

    if nuevas:
        cuerpo = "\n".join(f"• *{a['tipo']}* {a['market_id']}: {a['detalle']}" for a in nuevas)
        enviar_telegram(
            "🔎 *RECONCILIACIÓN posiciones* (nuevo)\n" + cuerpo +
            "\n\nRevisar trades.csv vs data-api/positions manualmente antes de actuar."
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
