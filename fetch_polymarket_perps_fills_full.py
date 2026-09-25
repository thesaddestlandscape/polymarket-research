#!/usr/bin/env python3
"""fetch_polymarket_perps_fills_full.py -- (23-Sep, Perps) HISTORIAL COMPLETO de fills por wallet.

## Por qué existe
Hasta el 23-Sep se creyó que el historial por wallet solo era accesible con auth
(`/v1/account/fills`, solo la cuenta propia) y que la API pública solo daba el ciclo
ABIERTO (`/v1/info/position-fills`). FALSO: `GET /v1/info/fills?address=` es PÚBLICO,
devuelve fills de la wallet en TODOS los instrumentos, más recientes primero,
paginado por cursor (100/página, `more`, `cursor` base64 {"ts","id"}), sin límite
de profundidad apreciable (verificado 23-Sep: 40 páginas/4000 fills seguidas sin 429).

NOTA de semántica (medida 23-Sep): `previous_size` es el tamaño ANTES DE LA ORDEN, no antes de
cada fill -- todos los fills de una misma orden (`order_id`) comparten previous_size. La unidad
de cadena es la ORDEN (perps_posiciones_v2.py agrupa por order_id).

Consecuencia (ver análisis 23-Sep): el rastreador de posiciones basado en
position-fills tenía solo 12/210 "posiciones cerradas" con el cierre realmente
observado (los fills de cierre desaparecían del ciclo abierto antes de la siguiente
captura horaria) y 2.323 inversiones de signo dentro de un solo fill que
`previous_size==0` no segmenta. Con el historial completo se puede reconstruir la
posición correctamente (segmentando por cruce de signo de previous_size + fill).

## Diseño (bajo consumo: VPS 4 cores cargado, ver CLAUDE.md)
- Un CSV por wallet en data/shadow/perps_fills_full/<address>.csv (gitignored, ver
  .gitignore) -- NO se toca la recogida actual (fetch_polymarket_perps_wallet_fills.py).
- Estado por wallet en data/shadow/perps_fills_full_state.json: newest_ts (ms),
  ids_en_newest_ts, back_cursor, back_done. Reanudable tras cualquier corte.
- Cada corrida: (1) fase incremental (desde lo más nuevo hasta lo ya visto), (2)
  continúa backfill desde back_cursor. Presupuesto de tiempo por corrida y de 429.
- Duplicados posibles si hay corte entre escribir filas y guardar estado: el lector
  DEBE deduplicar por trade_id (perps_fills_full_lector.cargar()).
Solo lectura de API pública, sin dinero.
"""
import csv
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
DIR_SHADOW = REPO / "data/shadow"
DIR_OUT = DIR_SHADOW / "perps_fills_full"
RUTA_STATE = DIR_SHADOW / "perps_fills_full_state.json"
API = "https://api.perpetuals.polymarket.com/v1/info/fills"
TIMEOUT = 20
DELAY_S = 0.7            # ~1,4 req/s: 40 paginas seguidas sin 429 (23-Sep)
PRESUPUESTO_S = 1500     # 25 min por corrida (cron cada 30 min mientras haya backfill)
MAX_429_SEGUIDOS = 4
# Tope de backfill por wallet (23-Sep): una wallet de alta frecuencia (0x0034: ~90 fills/min,
# >15.000 paginas de historia) no es copiable ni aporta posiciones de horas-dias; se marca
# `alta_frecuencia` y se queda con sus 40k fills mas recientes (los ultimos ~5h).
MAX_PAGINAS_BACKFILL = 400
CAMPOS = ["capturado_utc", "fill_timestamp_utc", "address", "instrument_id", "side", "price",
          "quantity", "taker", "fee", "previous_size", "previous_entry_price", "pnl",
          "liquidation", "adl", "trade_id", "order_id", "ts_ms"]


def _watchlist() -> list:
    """Union: watchlist de la recogida actual + wallets ya presentes en sus fills."""
    import glob
    direcciones = {}
    try:
        from fetch_polymarket_perps_wallet_fills import _elegir_watchlist
        for a in _elegir_watchlist():
            direcciones[a.lower()] = a
    except Exception as e:
        print(f"  [WARN] watchlist state: {type(e).__name__}: {e}", file=sys.stderr)
    for arch in glob.glob(str(DIR_SHADOW / "polymarket_perps_wallet_fills_*.csv")):
        try:
            with open(arch, encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    a = r.get("address", "")
                    if a:
                        direcciones.setdefault(a.lower(), a)
        except OSError:
            continue
    # 25-Sep: watchlist AMPLIADA (top-200 cuentas de los leaderboards por apariciones/PnL, 849 distintas vistas;
    # solo 41 tenian backfill) -> potencia para el consenso por categoria (project_perps_pendientes_25sep #2).
    try:
        import json as _json
        for a in _json.loads((DIR_SHADOW / "perps_watchlist_ampliada.json").read_text()):
            direcciones.setdefault(a.lower(), a)
    except Exception:
        pass
    return sorted(direcciones.values())


def _cargar_state() -> dict:
    if RUTA_STATE.exists():
        try:
            return json.loads(RUTA_STATE.read_text())
        except Exception:
            return {}
    return {}


def _guardar_state(state: dict) -> None:
    tmp = RUTA_STATE.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=1))
    tmp.replace(RUTA_STATE)


class Limite429(Exception):
    pass


def _pagina(address: str, cursor, contador_429: list) -> dict | None:
    params = {"address": address}
    if cursor:
        params["cursor"] = cursor
    for intento in range(3):
        try:
            r = requests.get(API, params=params, timeout=TIMEOUT)
        except requests.RequestException as e:
            print(f"  [WARN] {address[:10]} red: {type(e).__name__}", file=sys.stderr)
            time.sleep(5)
            continue
        if r.status_code == 429:
            contador_429[0] += 1
            if contador_429[0] >= MAX_429_SEGUIDOS:
                raise Limite429()
            time.sleep(min(60, float(r.headers.get("Retry-After") or 20)))
            continue
        if r.status_code != 200:
            print(f"  [WARN] {address[:10]} HTTP {r.status_code}: {r.text[:100]}", file=sys.stderr)
            return None
        contador_429[0] = 0
        try:
            return r.json()
        except ValueError:
            return None
    return None


def _fila(address: str, x: dict, ahora: str) -> dict:
    ts = int(x["timestamp"])
    return {
        "capturado_utc": ahora,
        "fill_timestamp_utc": datetime.fromtimestamp(ts / 1000, timezone.utc).isoformat(timespec="milliseconds"),
        "address": address, "instrument_id": x.get("instrument_id"), "side": x.get("side"),
        "price": x.get("price"), "quantity": x.get("quantity"), "taker": x.get("taker"),
        "fee": x.get("fee"), "previous_size": x.get("previous_size"),
        "previous_entry_price": x.get("previous_entry_price"), "pnl": x.get("pnl"),
        "liquidation": x.get("liquidation"), "adl": x.get("adl"),
        "trade_id": x.get("trade_id"), "order_id": x.get("order_id"), "ts_ms": ts,
    }


def _escribir(address: str, filas: list) -> None:
    if not filas:
        return
    DIR_OUT.mkdir(parents=True, exist_ok=True)
    ruta = DIR_OUT / f"{address}.csv"
    nuevo = not ruta.exists() or ruta.stat().st_size == 0
    with open(ruta, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        w.writerows(filas)


def procesar_wallet(address: str, st: dict, t_fin: float, c429: list) -> str:
    ahora = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rec = st.setdefault(address, {"newest_ts": None, "ids_en_newest_ts": [], "back_cursor": None,
                                   "back_done": False, "n": 0})
    estado_txt = ""

    # (1) FASE INCREMENTAL: solo si ya hay historial (newest_ts). Baja desde lo mas nuevo
    # hasta cruzar newest_ts. Si nunca hubo historial, la fase (2) hace todo.
    if rec["newest_ts"] is not None:
        cursor = None
        nuevos_total, primero = 0, True
        nuevo_newest = rec["newest_ts"]
        ids_newest = set(rec["ids_en_newest_ts"])
        while time.time() < t_fin:
            d = _pagina(address, cursor, c429)
            if d is None:
                break
            filas, cruzo = [], False
            for x in d.get("data", []):
                ts = int(x["timestamp"])
                tid = str(x.get("trade_id"))
                if ts < rec["newest_ts"] or (ts == rec["newest_ts"] and tid in set(rec["ids_en_newest_ts"])):
                    cruzo = True
                    continue
                filas.append(_fila(address, x, ahora))
                if ts > nuevo_newest:
                    nuevo_newest, ids_newest = ts, {tid}
                elif ts == nuevo_newest:
                    ids_newest.add(tid)
            _escribir(address, filas)
            nuevos_total += len(filas)
            if cruzo or not d.get("more"):
                break
            cursor = d.get("cursor")
            time.sleep(DELAY_S)
        rec["newest_ts"], rec["ids_en_newest_ts"] = nuevo_newest, sorted(ids_newest)
        rec["n"] += nuevos_total
        estado_txt += f"+{nuevos_total} nuevos "

    # (2) BACKFILL: desde back_cursor (o desde el principio si es la primera vez).
    if not rec["back_done"]:
        cursor = rec["back_cursor"]
        paginas, escritos = 0, 0
        while time.time() < t_fin:
            d = _pagina(address, cursor, c429)
            if d is None:
                break
            datos = d.get("data", [])
            filas = [_fila(address, x, ahora) for x in datos]
            _escribir(address, filas)
            escritos += len(filas)
            paginas += 1
            rec["paginas_backfill"] = rec.get("paginas_backfill", 0) + 1
            if rec["paginas_backfill"] >= MAX_PAGINAS_BACKFILL and d.get("more"):
                rec["back_done"], rec["back_cursor"], rec["alta_frecuencia"] = True, None, True
                break
            if rec["newest_ts"] is None and datos:   # primera pagina de la historia: fija el borde
                mx = max(int(x["timestamp"]) for x in datos)
                rec["newest_ts"] = mx
                rec["ids_en_newest_ts"] = sorted(str(x.get("trade_id")) for x in datos if int(x["timestamp"]) == mx)
            if not d.get("more") or not d.get("cursor"):
                rec["back_done"], rec["back_cursor"] = True, None
                break
            cursor = d["cursor"]
            rec["back_cursor"] = cursor
            _guardar_state(st)      # reanudable pagina a pagina
            time.sleep(DELAY_S)
        rec["n"] += escritos
        estado_txt += f"backfill +{escritos} en {paginas} pags {('TOPE alta_frecuencia' if rec.get('alta_frecuencia') else 'COMPLETO') if rec['back_done'] else '(sigue)'}"
    else:
        estado_txt += "backfill completo"
    return estado_txt


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--wallets", nargs="*", help="solo estas direcciones (prueba)")
    ap.add_argument("--presupuesto", type=int, default=PRESUPUESTO_S)
    a_ = ap.parse_args()
    t0 = time.time()
    t_fin = t0 + a_.presupuesto
    st = _cargar_state()
    c429 = [0]
    wl = a_.wallets or _watchlist()
    # Prioridad: primero las que aun no han terminado el backfill / nunca empezadas
    wl.sort(key=lambda a: (st.get(a, {}).get("back_done", False), a))
    print(f"[perps_fills_full] {len(wl)} wallets, presupuesto {a_.presupuesto}s")
    try:
        for a in wl:
            if time.time() >= t_fin:
                print("  presupuesto agotado -- el resto en la proxima corrida")
                break
            txt = procesar_wallet(a, st, t_fin, c429)
            _guardar_state(st)
            print(f"  {a[:10]}.. {txt} (total {st[a]['n']})")
    except Limite429:
        print("  ⚠️ 429 repetido -- se aborta la corrida (estado guardado, se reanuda)")
    finally:
        _guardar_state(st)
    hechos = sum(1 for a in wl if st.get(a, {}).get("back_done"))
    print(f"[perps_fills_full] backfill completo {hechos}/{len(wl)} wallets, {time.time()-t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
