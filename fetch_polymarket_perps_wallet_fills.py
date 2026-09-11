#!/usr/bin/env python3
"""fetch_polymarket_perps_wallet_fills.py — FASE 1 de tracking de wallets en
Polymarket Perps: qué está haciendo CADA WALLET candidata ahora mismo (lado
long/short, precio, tamaño, si fue taker o maker, pnl realizado por fill,
si fue liquidación/ADL) -- petición explícita Javi 09-Sep: "tienes que
saber que estan haciendo en cada momento, como han construido su pnl".

⚠️ LIMITACIÓN REAL DE LA API, verificada 09-Sep antes de escribir esto (no
asumida) -- Fail Loud: el único endpoint público por wallet arbitraria es

  GET /v1/info/position-fills?address=&instrument_id=

y este SOLO devuelve los fills del CICLO DE POSICIÓN ABIERTO ACTUAL (desde
que la posición pasó de flat o cambió de dirección la última vez) -- NO el
historial completo de la wallet. El histórico completo (`/v1/account/fills`)
es AUTENTICADO, solo accesible para la propia cuenta -- no hay forma
pública de "descargar todo el pasado" de una wallet ajena de una vez.
Consecuencia operativa: NO podemos reconstruir retroactivamente cómo una
wallet construyó su PnL histórico completo -- solo podemos, desde HOY,
empezar a acumular su actividad hacia adelante, exactamente el mismo
patrón forward-only que ballenas_timing_history.csv / resolution_sniper_
observer.py / cualquier otro histórico de este proyecto que tampoco pudo
backfillear el pasado. Cuanto antes se despliegue este fetcher, antes
empieza a acumular ese historial propio -- de ahí la prioridad de
construirlo ya en vez de esperar más días de solo-leaderboard.

Diseño acotado a propósito (RAM/CPU limitados, ver
project_disco_ram_critico_09sep -- petición explícita Javi de no saturar):
  - Watchlist de wallets: NO todas las ~150+ ya vistas en el leaderboard,
    solo las que de verdad destacan -- top TOP_WALLETS por mejor pnl "all"
    entre las que tienen mejor_rank<=50 en window "all" o "week" (evita
    perseguir un día bueno aislado en "day").
  - Universo de instrumentos: NO los 67 de golpe -- top TOP_INSTRUMENTS por
    volumen real (statistics), así no se gastan requests en acciones
    ilíquidas.
  - Dedupe por timestamp: se recuerda el último timestamp de fill visto
    por (wallet, instrumento) y solo se procesan/guardan fills más nuevos
    -- evita reprocesar el histórico entero en cada corrida.
  - Circuit breaker manual: si hay 5 errores de red seguidos, aborta el
    resto de la corrida (no insistir contra una API caída/limitando).
  - Delay entre llamadas (evitar ráfaga, cortesía con el rate-limit no
    documentado del endpoint -- Request Weight: 10 según la doc).

Salidas:
  data/shadow/polymarket_perps_wallet_fills_YYYY-MM-DD.csv  (append, cada
      fill nuevo de cada wallet vigilada)
  data/shadow/polymarket_perps_wallet_fills_state.json      (último
      timestamp visto por wallet+instrumento, para el dedupe)

Cron sugerido: horario (los fills no necesitan cadencia de minutos para
construir un perfil de comportamiento, y así se acota el gasto de
requests -- ~30 wallets x ~12 instrumentos = 360 llamadas/hora máximo).
"""
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

API_BASE = "https://api.perpetuals.polymarket.com"
TIMEOUT = 20
DELAY_S = 0.15
MAX_ERRORES_SEGUIDOS = 5
MAX_PAGINAS_POR_PAR = 2  # tope 200 fills/par/corrida -- suficiente en cadencia horaria

TOP_WALLETS = 30
TOP_INSTRUMENTS = 12

RUTA_WALLETS_STATE = DIR_SHADOW / "polymarket_perps_wallets_state.json"
RUTA_FILLS_STATE = DIR_SHADOW / "polymarket_perps_wallet_fills_state.json"
RUTA_INSTRUMENTS_CACHE = DIR_SHADOW / "polymarket_perps_instruments.json"

CAMPOS = ["timestamp_utc", "fill_timestamp_utc", "address", "instrument_id", "symbol",
          "side", "price", "quantity", "taker", "fee", "previous_size",
          "previous_entry_price", "pnl", "liquidation", "adl", "trade_id"]


def _out_path(ahora: datetime) -> Path:
    return DIR_SHADOW / f"polymarket_perps_wallet_fills_{ahora.date().isoformat()}.csv"


def _elegir_watchlist() -> list[str]:
    if not RUTA_WALLETS_STATE.exists():
        return []
    try:
        state = json.loads(RUTA_WALLETS_STATE.read_text())
    except Exception:
        return []
    candidatas = []
    for addr, rec in state.items():
        mejor = rec.get("mejor_rank", {})
        if mejor.get("all", 9999) <= 50 or mejor.get("week", 9999) <= 30:
            try:
                pnl_all = float(rec.get("ultimo_pnl_all", 0) or 0)
            except (TypeError, ValueError):
                pnl_all = 0.0
            candidatas.append((pnl_all, addr))
    candidatas.sort(reverse=True)
    return [addr for _, addr in candidatas[:TOP_WALLETS]]


def _elegir_instrumentos() -> list[dict]:
    try:
        r = requests.get(f"{API_BASE}/v1/info/statistics", timeout=TIMEOUT)
        r.raise_for_status()
        stats = r.json()
    except Exception as e:
        print(f"  [WARN] statistics error: {type(e).__name__}: {e}", file=sys.stderr)
        stats = []

    simbolos = {}
    if RUTA_INSTRUMENTS_CACHE.exists():
        try:
            data = json.loads(RUTA_INSTRUMENTS_CACHE.read_text())
            simbolos = {d["instrument_id"]: d.get("symbol", "") for d in data}
        except Exception:
            pass

    def _vol(s):
        try:
            return float(s.get("volume", 0) or 0)
        except (TypeError, ValueError):
            return 0.0

    stats.sort(key=_vol, reverse=True)
    return [{"instrument_id": s["instrument_id"],
             "symbol": s.get("symbol", simbolos.get(s["instrument_id"], ""))}
            for s in stats[:TOP_INSTRUMENTS]]


def _cargar_fills_state() -> dict:
    if RUTA_FILLS_STATE.exists():
        try:
            return json.loads(RUTA_FILLS_STATE.read_text())
        except Exception:
            return {}
    return {}


def _guardar_fills_state(state: dict) -> None:
    tmp = RUTA_FILLS_STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1))
    tmp.replace(RUTA_FILLS_STATE)


def fetch_position_fills(address: str, instrument_id: int, cursor: str | None) -> tuple[dict | None, bool]:
    """Devuelve (data, es_error_real). 413 payload_too_large / 400 (cursor
    inválido a media paginación) son respuestas ESPERADAS del endpoint para
    ciclos de posición gigantes o carreras de paginación -- se tratan como
    "sin datos para este par", NO como fallo de red (no deben disparar el
    circuit breaker, ver docs: "Cycle older than that bound returns 413")."""
    params = {"address": address, "instrument_id": instrument_id}
    if cursor:
        params["cursor"] = cursor
    try:
        r = requests.get(f"{API_BASE}/v1/info/position-fills", params=params, timeout=TIMEOUT)
        if r.status_code in (413, 400):
            return None, False
        if r.status_code != 200:
            body = r.text[:120]
            print(f"  [WARN] {address[:10]}.. id={instrument_id} HTTP {r.status_code}: {body}", file=sys.stderr)
            return None, True
        return r.json(), False
    except Exception as e:
        print(f"  [WARN] {address[:10]}.. id={instrument_id} error: {type(e).__name__}: {e}", file=sys.stderr)
        return None, True


def main() -> int:
    ahora = datetime.now(timezone.utc)
    ahora_iso = ahora.isoformat(timespec="seconds")

    watchlist = _elegir_watchlist()
    instrumentos = _elegir_instrumentos()
    if not watchlist or not instrumentos:
        print(f"[{ahora_iso}] Watchlist ({len(watchlist)}) o instrumentos ({len(instrumentos)}) vacíos -- nada que hacer todavía.")
        return 0

    fills_state = _cargar_fills_state()
    path = _out_path(ahora)
    nuevo = not path.exists()

    filas_nuevas = []
    errores_seguidos = 0
    pares_ok = 0
    pares_con_datos = 0
    pares_413 = 0

    salir = False
    for address in watchlist:
        if salir:
            break
        for inst in instrumentos:
            iid = inst["instrument_id"]
            clave = f"{address}:{iid}"
            ultimo_ts_visto = fills_state.get(clave, {}).get("ultimo_ts", 0)

            cursor = None
            max_ts_esta_corrida = ultimo_ts_visto
            for _pagina in range(MAX_PAGINAS_POR_PAR):
                data, es_error_real = fetch_position_fills(address, iid, cursor)
                time.sleep(DELAY_S)

                if data is None:
                    if es_error_real:
                        errores_seguidos += 1
                        if errores_seguidos >= MAX_ERRORES_SEGUIDOS:
                            print(f"[{ahora_iso}] {errores_seguidos} errores de red seguidos -- abortando corrida.", file=sys.stderr)
                            salir = True
                    else:
                        errores_seguidos = 0  # 413/400 esperado, no cuenta como fallo de red
                        pares_413 += 1
                    break
                errores_seguidos = 0

                fills = data.get("data", [])
                if not fills:
                    break

                fills_nuevos_pagina = [f for f in fills if f.get("timestamp", 0) > ultimo_ts_visto]
                for f in fills_nuevos_pagina:
                    filas_nuevas.append({
                        "timestamp_utc": ahora_iso,
                        "fill_timestamp_utc": datetime.fromtimestamp(f["timestamp"] / 1000, tz=timezone.utc).isoformat(timespec="seconds"),
                        "address": address,
                        "instrument_id": iid,
                        "symbol": inst["symbol"],
                        "side": f.get("side", ""),
                        "price": f.get("price", ""),
                        "quantity": f.get("quantity", ""),
                        "taker": f.get("taker", ""),
                        "fee": f.get("fee", ""),
                        "previous_size": f.get("previous_size", ""),
                        "previous_entry_price": f.get("previous_entry_price", ""),
                        "pnl": f.get("pnl", ""),
                        "liquidation": f.get("liquidation", ""),
                        "adl": f.get("adl", ""),
                        "trade_id": f.get("trade_id", ""),
                    })
                    max_ts_esta_corrida = max(max_ts_esta_corrida, f["timestamp"])

                # si toda la página ya era conocida, no hace falta paginar más
                if len(fills_nuevos_pagina) < len(fills):
                    break
                if not data.get("more"):
                    break
                cursor = data.get("cursor")
                if not cursor:
                    break

            if salir:
                break

            pares_ok += 1
            if max_ts_esta_corrida > ultimo_ts_visto:
                fills_state[clave] = {"ultimo_ts": max_ts_esta_corrida, "actualizado": ahora_iso}
                pares_con_datos += 1

    if filas_nuevas:
        with open(path, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            if nuevo:
                w.writeheader()
            for fila in filas_nuevas:
                w.writerow(fila)

    _guardar_fills_state(fills_state)

    print(f"[{ahora_iso}] {len(watchlist)} wallets x {len(instrumentos)} instrumentos | "
          f"{pares_ok} pares consultados, {pares_con_datos} con fills nuevos, "
          f"{pares_413} con ciclo demasiado grande (413, esperado en whales) | "
          f"{len(filas_nuevas)} fills nuevos escritos en {path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
