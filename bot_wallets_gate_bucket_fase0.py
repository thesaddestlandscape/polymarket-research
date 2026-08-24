#!/usr/bin/env python3
"""
bot_wallets_gate_bucket_fase0.py -- P-GALLINA FASE 0, 25-Ago (petición
explícita Javi: "constrúyelo ahora, FASE 0, solo lectura").

Continuación de la Candidata 11 (gallina de los huevos de oro,
idea_gallina_huevos_oro_candidatas_25ago): el cruce retroactivo
(wallet_edge_score_por_activo_marco.json + ballenas_timing_history.csv,
desagregado por arquetipo×activo×marco×micro-bucket) encontró 58 celdas
con n>=100 y g_kelly>0 -- pero eso mide EDGE, no FILL-ABILITY (el precio
histórico de la wallet no es una consulta de libro real, mismo error ya
cazado y corregido en Wallet Mirror el 10-Ago,
project_p24_wallet_mirror_refutado_ask_real_10ago). Este observador
cierra ese hueco EXACTAMENTE como wallet_mirror_executor_dryrun.py
(P24 FASE1) lo hizo para Wallet Mirror: cuando detecta a una de las bot
wallets (bot_wallets_universo_25ago.json) operar en tiempo real vía el
firehose de trades (polyactivity), consulta el libro PÚBLICO real en ese
instante y registra la profundidad -- sin eso, cualquier veredicto de
fill-ability sobre estas celdas sería inventado.

Reusa (import directo, sin duplicar) `_archivos_activity()` (lee el
firehose ya escrito por fetch_polymarket_activity_ws.py) y
`_fillability_mirror()` (consulta pública de libro, mismo criterio de
stake de referencia) de wallet_mirror_tracker.py -- mismo patrón de
detección que ya usa wallet_mirror_sniper.py.

NO coloca, cancela ni modifica ninguna orden real -- puramente
observacional. NO usa la clasificación de arquetipo persistida (no
existe todavía como fichero propio) -- clasifica sobre la marcha con la
MISMA lógica que analisis_bot_arquetipos_25ago.py (marco dominante +
restante_min mediana), recalculada una vez al arrancar desde
ballenas_timing_history.csv.
"""
import csv
import json
import math
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from wallet_mirror_tracker import _archivos_activity, _fillability_mirror  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "bot_wallets_gate_bucket_fase0.csv"
VISTOS_PATH = DIR_SHADOW / "bot_wallets_gate_bucket_fase0_vistos.json"
BOTS_PATH = DIR_SHADOW / "bot_wallets_universo_25ago.json"
HIST = DIR_SHADOW / "ballenas_timing_history.csv"

POLL_S = 15
STEP_BUCKET = 0.05
UMBRAL_SNIPER_MIN = 5.0

COLUMNS = [
    "timestamp_utc", "trade_timestamp", "wallet", "arquetipo", "activo", "marco",
    "bucket_precio", "condition_id", "market_slug", "lado_wallet", "precio_wallet",
    "usd_trade", "ratio_vs_stake_deteccion", "mejor_ask_deteccion", "profundidad_eur_deteccion",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _bucket(p: float) -> float:
    return round(math.floor(p / STEP_BUCKET + 1e-9) * STEP_BUCKET, 4)


def clasificar_arquetipos(wallets: set) -> dict:
    """MISMA lógica que analisis_bot_arquetipos_25ago.py::clasificar_wallets()
    -- recalculada aquí en vez de importada porque ese script es de un solo
    disparo (main() con prints), no un módulo de librería reutilizable."""
    por_wallet = defaultdict(lambda: defaultdict(list))
    with open(HIST, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            w = r.get("wallet", "").lower()
            if w not in wallets:
                continue
            try:
                rm = float(r["restante_min"])
            except (TypeError, ValueError):
                continue
            por_wallet[w][r.get("marco", "?")].append(rm)

    out = {}
    for w, marcos in por_wallet.items():
        marco_dom = max(marcos, key=lambda m: len(marcos[m]))
        mediana = sorted(marcos[marco_dom])[len(marcos[marco_dom]) // 2]
        if marco_dom == "weekly":
            out[w] = "WEEKLY_TEMPRANO" if mediana > 500 else "WEEKLY_TARDIO"
        else:
            out[w] = "SNIPER" if mediana <= UMBRAL_SNIPER_MIN else "DISPERSO"
    return out


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-50000:]), encoding="utf-8")


def _guardar(filas: list) -> None:
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        for fila in filas:
            w.writerow([fila.get(c, "") for c in COLUMNS])


def _seed_vistos_sin_consultar(wallets: set) -> set:
    """25-Ago (fix real, encontrado en el propio despliegue -- el primer
    arranque se quedó procesando ~2 días de backlog del firehose CON una
    consulta de red (_fillability_mirror -> gamma-api) POR CADA evento
    histórico, la inmensa mayoría mercados ya cerrados donde la consulta
    tarda en fallar en vez de fallar rápido -- podía tardar horas y quemar
    CPU/red para nada, mismo patrón de incidente que el fetch_polymarket_
    activity_ws.py del 22-Ago). Al arrancar, se marcan como "vistos" todos
    los matches YA existentes en el firehose SIN consultar profundidad --
    solo se mide profundidad real para eventos que lleguen A PARTIR de
    ahora, que es lo único que tiene sentido medir (el propósito es
    fill-ability EN EL INSTANTE DE DETECCIÓN, no reconstruir el pasado)."""
    vistos = _vistos_cargar()
    nuevos = 0
    for path in _archivos_activity():
        with open(path, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                if (row.get("side") or "").strip().upper() != "BUY":
                    continue
                w = (row.get("wallet") or "").lower()
                if w not in wallets:
                    continue
                dedup_key = f"{w}|{row.get('market_slug','')}"
                if dedup_key not in vistos:
                    vistos.add(dedup_key)
                    nuevos += 1
    _log(f"backlog existente marcado como visto sin consultar profundidad: {nuevos} matches")
    return vistos


def _procesar_fila(row: dict, wallets: set, arquetipos: dict, vistos: set) -> dict | None:
    if (row.get("side") or "").strip().upper() != "BUY":
        return None
    w = (row.get("wallet") or "").lower()
    if w not in wallets:
        return None
    dedup_key = f"{w}|{row.get('market_slug','')}"
    if dedup_key in vistos:
        return None
    vistos.add(dedup_key)
    try:
        precio = float(row.get("price") or 0)
    except (TypeError, ValueError):
        return None
    if not (0.0 < precio < 1.0):
        return None
    lado = row.get("outcome", "")  # "Up"/"Down"
    fill = _fillability_mirror(row.get("market_slug", ""), lado, row.get("price", ""))
    try:
        usd_trade = float(row.get("usd_value") or 0)
    except (TypeError, ValueError):
        usd_trade = 0.0
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "trade_timestamp": row.get("timestamp_utc", ""),
        "wallet": w, "arquetipo": arquetipos.get(w, "?"),
        "activo": row.get("activo", ""), "marco": row.get("marco", ""),
        "bucket_precio": f"{_bucket(precio):.2f}",
        "condition_id": row.get("condition_id", ""),
        "market_slug": row.get("market_slug", ""),
        "lado_wallet": lado, "precio_wallet": row.get("price", ""),
        "usd_trade": usd_trade,
        "ratio_vs_stake_deteccion": fill.get("ratio_vs_stake", "") if fill.get("ok") else "",
        "mejor_ask_deteccion": fill.get("mejor_ask", "") if fill.get("ok") else "",
        "profundidad_eur_deteccion": fill.get("profundidad_eur", "") if fill.get("ok") else "",
    }


def main() -> None:
    bots = json.loads(BOTS_PATH.read_text(encoding="utf-8"))
    wallets = set(bots.keys())
    arquetipos = clasificar_arquetipos(wallets)
    _log(f"bot_wallets_gate_bucket_fase0 arrancado -- {len(wallets)} bot wallets, "
         f"{len(arquetipos)} clasificadas por arquetipo")

    vistos = _seed_vistos_sin_consultar(wallets)
    _vistos_guardar(vistos)

    # 25-Ago (2º fix real, encontrado en el propio despliegue): sin esto,
    # cada ciclo releía los ~2 días completos del firehose (~1GB/día, ~2.6M
    # filas/día) desde el principio solo para encontrar las pocas filas
    # NUEVAS añadidas desde el ciclo anterior -- a este volumen, un ciclo
    # podía tardar minutos, nunca alcanzaría tiempo real. Mismo patrón que
    # _ChainlinkTail._loop (resolution_sniper_observer.py): trackear
    # posición de lectura (bytes) por fichero, seek() en vez de releer.
    posiciones: dict[Path, int] = {}
    cabeceras: dict[Path, list[str]] = {}
    while True:
        try:
            filas = []
            for path in _archivos_activity():
                if path not in posiciones:
                    with open(path, encoding="utf-8") as f:
                        cabeceras[path] = next(csv.reader([f.readline()]))
                        posiciones[path] = f.tell()
                with open(path, encoding="utf-8") as f:
                    f.seek(posiciones[path])
                    nuevas = f.readlines()
                    posiciones[path] = f.tell()
                if not nuevas:
                    continue
                header = cabeceras[path]
                for linea in csv.reader(nuevas):
                    if len(linea) != len(header):
                        continue  # fila truncada por escritura concurrente -- se recoge en el siguiente ciclo
                    row = dict(zip(header, linea))
                    fila = _procesar_fila(row, wallets, arquetipos, vistos)
                    if fila is not None:
                        filas.append(fila)
                        _log(f"[{fila['arquetipo']}] {fila['activo']}#{fila['marco']}"
                             f"[{fila['bucket_precio']}) wallet={fila['wallet'][:10]}.. "
                             f"ratio_deteccion={fila['ratio_vs_stake_deteccion']}")
            if filas:
                _guardar(filas)
                _vistos_guardar(vistos)
        except Exception as e:
            _log(f"🚨 error en ciclo: {type(e).__name__}: {e}")
        time.sleep(POLL_S)


if __name__ == "__main__":
    main()
