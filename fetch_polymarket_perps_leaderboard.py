#!/usr/bin/env python3
"""fetch_polymarket_perps_leaderboard.py — FASE 0 de tracking de wallets en
Polymarket Perps (producto nuevo, lanzado 03-Sep-2026, cuenta/API SEPARADA
del Polymarket de predicción que ya explotamos -- ver
project_investigacion_universo_perps_09sep).

Petición explícita Javi 09-Sep: "vamos a i trackeando esto... replicar todo
lo que funciona en nuestro modelo actual para Perps, pero solo operando
cuando operen las mejores wallets, las ballenas, las wallets expertas...
atendiendo a los limites de infraestructura que tenemos, hazlo para evitar
que saturemos Ram, memoria".

Diseño deliberadamente mínimo (mismo criterio "ir poco a poco" que ya usó
el proyecto en P29/dispersed_bot): CRON, no screen persistente -- proceso
corre unos segundos y termina, sin huella de RAM residente. Verificado en
vivo antes de escribir código (09-Sep, RAM 2.5GB libres / swap 7.4/10GB
usado -- margen ajustado, no abundante, por eso cron y no otro hilo más en
una screen ya cargada):

    GET https://api.perpetuals.polymarket.com/v1/info/leaderboard
        ?window=day|week|all&limit=50
    -> {"window","sort_by","timestamp","total","entries":[
         {"rank","account","pnl","notional","account_value"}, ...]}

Es PÚBLICO, sin auth, y con limit=50 el payload es ~4-5KB por ventana
(sin limit, "all" son 16878 cuentas -- innecesario, top 50 por ventana ya
es la cantera de candidatas a "ballena").

Esto es la FASE 0 (solo captura, igual que fetch_chainlink_prices.py o
fetch_binance_perp_cvd_oi.py al arrancar): acumula un historial de
snapshots del leaderboard y un contador de apariciones por wallet en el
top 50 "all" -- el mismo patrón que wallet_especialistas_state.json. NO
llama a /v1/info/position-fills todavía (eso exige (address, instrument_id)
por separado -- 50 wallets x 67 instrumentos sería carísimo sin antes
tener una watchlist reducida) -- esa es la FASE 1, a construir solo cuando
este historial ya tenga unos días y permita quedarse con las wallets
REALMENTE persistentes en el top (no ruido de un día bueno aislado),
exactamente el mismo criterio que ya evitó el incidente de HRP con
BALLENAS_TARDIAS#BTC#15min (varianza artificialmente baja por poca
historia, ver project_decisiones_payout_varianza_23jul).

Salidas:
  data/shadow/polymarket_perps_leaderboard_YYYY-MM-DD.csv  (append, histórico)
  data/shadow/polymarket_perps_wallets_state.json          (contador de
      apariciones en top50 "all"/"week"/"day" por wallet -- acotado de
      forma natural, nunca crece sin límite porque solo entran wallets
      que ya estuvieron en un top 50)

Cron sugerido: cada 15min (el leaderboard no cambia a nivel de segundos,
no hace falta más cadencia -- mismo espíritu que binance_perp_cvd_oi, que
usa 5min por ser una señal de minutos-horas).
"""
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

API_BASE = "https://api.perpetuals.polymarket.com"
TIMEOUT = 15
LIMIT = 50
WINDOWS = ["day", "week", "all"]

CAMPOS = ["timestamp_utc", "window", "rank", "account", "pnl", "notional", "account_value"]

RUTA_STATE = DIR_SHADOW / "polymarket_perps_wallets_state.json"


def _out_path(ahora: datetime) -> Path:
    return DIR_SHADOW / f"polymarket_perps_leaderboard_{ahora.date().isoformat()}.csv"


def fetch_leaderboard(window: str) -> list | None:
    try:
        r = requests.get(f"{API_BASE}/v1/info/leaderboard",
                          params={"window": window, "limit": LIMIT},
                          timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json()
        return data.get("entries", [])
    except Exception as e:
        print(f"  [WARN] leaderboard error window={window}: {type(e).__name__}: {e}", file=sys.stderr)
        return None


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


def _actualizar_state(state: dict, window: str, entries: list, ahora_iso: str) -> list:
    """Actualiza contador de apariciones por wallet en este top-N de esta
    ventana. Devuelve la lista de cuentas NUEVAS en el top (nunca vistas
    antes en ninguna ventana) para el log."""
    nuevas = []
    for e in entries:
        acc = e["account"]
        if acc not in state:
            state[acc] = {"primera_vez": ahora_iso, "veces_visto": {}, "mejor_rank": {}}
            nuevas.append(acc)
        rec = state[acc]
        rec["veces_visto"][window] = rec["veces_visto"].get(window, 0) + 1
        rank = e["rank"]
        if window not in rec["mejor_rank"] or rank < rec["mejor_rank"][window]:
            rec["mejor_rank"][window] = rank
        rec["ultimo_pnl_" + window] = e["pnl"]
        rec["ultima_vez"] = ahora_iso
    return nuevas


def main() -> int:
    ahora = datetime.now(timezone.utc)
    ahora_iso = ahora.isoformat(timespec="seconds")
    path = _out_path(ahora)
    nuevo = not path.exists()

    state = _cargar_state()
    filas = []
    nuevas_totales = []

    for window in WINDOWS:
        entries = fetch_leaderboard(window)
        if not entries:
            continue
        for e in entries:
            filas.append({
                "timestamp_utc": ahora_iso,
                "window": window,
                "rank": e["rank"],
                "account": e["account"],
                "pnl": e["pnl"],
                "notional": e["notional"],
                "account_value": e["account_value"],
            })
        nuevas_totales.extend(_actualizar_state(state, window, entries, ahora_iso))

    if not filas:
        print(f"[{ahora_iso}] Sin datos de ninguna ventana -- API perps no responde, nada que escribir.")
        return 0

    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)

    _guardar_state(state)

    print(f"[{ahora_iso}] {len(filas)} filas escritas en {path.name} | "
          f"{len(state)} wallets únicas vistas en top{LIMIT} acumulado | "
          f"{len(set(nuevas_totales))} nuevas esta corrida")
    return 0


if __name__ == "__main__":
    sys.exit(main())
