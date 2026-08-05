#!/usr/bin/env python3
"""
wallet_mirror_sniper.py — Wallet Mirror en TIEMPO REAL (P24, petición
explícita Javi 30-Jul: "quiero que lo instrumentes, porque ya sabes
cuales son los objetivos y misiones de este proyecto").

wallet_mirror_tracker.py (29-Jul) ya construyó TODA la lógica de negocio
(cargar_wallets_validadas, _opuesto, _fillability_mirror -- consulta real
del libro CLOB) pero corre como cron cada 10min sobre un CSV que ya se
escribió solo: la fila que usa para "fill-ability" es el libro en el
INSTANTE DE DETECCIÓN, que puede ir hasta 10 minutos por detrás del
trade real de la wallet -- su propio docstring lo admite ("mismo desfase
que ya acepta P22", nunca cuantificado). Ese desfase es exactamente lo
que hace inútil medir fill-ability de verdad: a los 10 minutos cualquier
oportunidad de precio ya se movió.

Este script CIERRA ese hueco: conexión WebSocket PROPIA al mismo feed
RTDS (wss://ws-live-data.polymarket.com, topic activity/trades -- mismo
endpoint gratis que fetch_polymarket_activity_ws.py, sin auth) y, en
cuanto llega un trade BUY de una wallet validada, consulta el libro
CLOB en el mismo segundo (no en el próximo ciclo de cron) -- reutiliza
TODA la lógica de wallet_mirror_tracker.py (import directo, cero
duplicación) salvo la fuente del evento (WS en vivo, no CSV rezagado) y
el dedup (fichero propio, para no competir por el mismo estado que el
cron de 10min).

Nueva columna clave: `lag_deteccion_s` (segundos entre el timestamp del
trade real de la wallet y el instante en que ESTE proceso lo procesó) --
permite comparar empíricamente la fill-ability medida aquí (lag~1-3s)
contra la del cron de 10min (lag~0-600s) antes de proponer nada con
dinero real.

⚠️ Solo observación -- NO coloca ni cancela ninguna orden real, igual que
wallet_mirror_tracker.py. Cualquier paso hacia dinero real (P24 FASE 1)
requiere medir aquí que la fill-ability en tiempo real es sustancialmente
mejor que la ya medida (arquetipo A vs B, ver project_dos_patrones_
edge_bandera_21jul) + revisión + aprobación explícita, mismo patrón en
dos fases que todos los ejecutores de este proyecto.

Salida: data/shadow/wallet_mirror_sniper_dry_run.csv (mismas columnas que
wallet_mirror_dry_run.csv + lag_deteccion_s). Resolución de outcome vía
el mismo mecanismo que wallet_mirror_tracker.py (--resolver).

Corre en screen propia:
  screen -dmS walletmirror bash -c "cd /root/polymarket-research && .venv/bin/python wallet_mirror_sniper.py >> logs/wallet_mirror_sniper.log 2>&1"
"""
import asyncio
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from wallet_mirror_tracker import (  # noqa: E402
    cargar_wallets_validadas, _opuesto, _fillability_mirror, resolver_pendientes,
)
from fetch_polymarket_activity_ws import _parse_updown  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "wallet_mirror_sniper_dry_run.csv"
VISTOS_PATH = DIR_SHADOW / "wallet_mirror_sniper_vistos.json"  # propio -- no compartir
# estado con wallet_mirror_tracker.py (cron 10min), evita una carrera de
# escritura sobre el mismo fichero desde dos procesos independientes.

WS_URL = "wss://ws-live-data.polymarket.com"
PING_INTERVAL_S = 5
RECONNECT_ESPERA_S = 5
RECV_TIMEOUT_S = 30  # mismo fix que fetch_polymarket_activity_ws.py/chainlink --
# sin esto, una conexión muerta en silencio bloquea el bucle para siempre.

REFRESCO_WALLETS_S = 1800  # wallet_edge_score_por_activo_marco.json lo
# regenera wallet_edge_tracker.py cada hora (cron) -- 30min de margen.

COLUMNS = ["timestamp_utc", "trade_timestamp", "wallet", "tipo", "edge_pp_validado",
           "n_validado", "activo", "marco", "condition_id", "market_slug",
           "lado_wallet", "precio_wallet", "mirror_lado", "transaction_hash",
           "outcome_real", "acierto", "resolved_ts",
           "ratio_vs_stake_deteccion", "mejor_ask_deteccion",
           "usd_trade", "size_mediana_wallet", "ratio_vs_mediana_propia",
           "es_jugada_grande", "lag_deteccion_s"]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    lista = list(vistos)[-50000:]
    VISTOS_PATH.write_text(json.dumps(lista), encoding="utf-8")


def _guardar_fila(fila: dict) -> None:
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)


async def _mantener_ping(ws):
    try:
        while True:
            await asyncio.sleep(PING_INTERVAL_S)
            await ws.send("PING")
    except (asyncio.CancelledError, websockets.exceptions.ConnectionClosed):
        pass


async def _correr_una_conexion(wallets: dict, vistos: set) -> set:
    async with websockets.connect(WS_URL, open_timeout=10, close_timeout=5) as ws:
        sub = {"action": "subscribe", "subscriptions": [{"topic": "activity", "type": "trades"}]}
        await ws.send(json.dumps(sub))
        _log(f"Conectado, suscrito a activity/trades -- {len(wallets)} wallets validadas en watch")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        n_trades = n_matches = 0
        try:
            while True:
                raw = await asyncio.wait_for(ws.recv(), timeout=RECV_TIMEOUT_S)
                if not raw:
                    continue
                try:
                    msg = json.loads(raw)
                except (json.JSONDecodeError, TypeError):
                    continue
                payload = msg.get("payload")
                if not isinstance(payload, dict) or "proxyWallet" not in payload:
                    continue
                n_trades += 1
                if (payload.get("side") or "").strip().upper() != "BUY":
                    continue
                w = (payload.get("proxyWallet") or "").lower()
                event_slug = payload.get("eventSlug", "")
                activo, marco = _parse_updown(event_slug, payload.get("title", ""))
                if activo is None:
                    continue
                clave = (w, activo, marco)
                info = wallets.get(clave)
                if info is None:
                    continue

                market_slug = payload.get("slug", "")
                dedup_key = f"{w}|{market_slug}"
                if dedup_key in vistos:
                    continue
                vistos.add(dedup_key)

                ahora = datetime.now(timezone.utc)
                ws_ts = payload.get("timestamp")
                try:
                    # payload["timestamp"] llega en SEGUNDOS (verificado en vivo:
                    # 1785415671 ~ epoch actual -- fetch_polymarket_activity_ws.py
                    # lo guarda crudo sin convertir, mismo formato aquí; la
                    # primera versión de este script asumía milisegundos por
                    # error, dando lags de ~1785 millones de segundos).
                    lag_s = round(ahora.timestamp() - float(ws_ts), 2) if ws_ts else None
                except (TypeError, ValueError):
                    lag_s = None

                lado_wallet = payload.get("outcome", "")
                mirror_lado = lado_wallet if info["tipo"] == "SEGUIR" else _opuesto(lado_wallet)
                precio = payload.get("price", "")
                fill = _fillability_mirror(market_slug, mirror_lado, precio)

                try:
                    price_f = float(precio)
                    size_f = float(payload.get("size", 0) or 0)
                    usd_trade = round(price_f * size_f, 4)
                except (TypeError, ValueError):
                    usd_trade = 0.0
                size_mediana = info.get("size_mediana")
                ratio_size = round(usd_trade / size_mediana, 2) if size_mediana and usd_trade > 0 else None

                fila = {
                    "timestamp_utc": ahora.isoformat(timespec="seconds"),
                    "trade_timestamp": datetime.fromtimestamp(float(ws_ts), timezone.utc).isoformat(timespec="milliseconds") if ws_ts else "",
                    "wallet": w, "tipo": info["tipo"], "edge_pp_validado": info["edge_pp"],
                    "n_validado": info["n"], "activo": activo, "marco": marco,
                    "condition_id": payload.get("conditionId", ""), "market_slug": market_slug,
                    "lado_wallet": lado_wallet, "precio_wallet": precio, "mirror_lado": mirror_lado,
                    "transaction_hash": payload.get("transactionHash", ""),
                    "outcome_real": "", "acierto": "", "resolved_ts": "",
                    "ratio_vs_stake_deteccion": fill.get("ratio_vs_stake", "") if fill.get("ok") else "",
                    "mejor_ask_deteccion": fill.get("mejor_ask", "") if fill.get("ok") else "",
                    "usd_trade": usd_trade if usd_trade > 0 else "",
                    "size_mediana_wallet": size_mediana if size_mediana else "",
                    "ratio_vs_mediana_propia": ratio_size if ratio_size is not None else "",
                    "es_jugada_grande": int(ratio_size >= 2.0) if ratio_size is not None else "",
                    "lag_deteccion_s": lag_s if lag_s is not None else "",
                }
                _guardar_fila(fila)
                n_matches += 1
                _log(f"🎯 MATCH {activo}#{marco} wallet={w[:10]}... {info['tipo']} "
                     f"lado_wallet={lado_wallet} mirror={mirror_lado} lag={lag_s}s "
                     f"fill_ok={fill.get('ok')} ratio_vs_stake={fill.get('ratio_vs_stake')}")
                if n_matches % 20 == 0:
                    _vistos_guardar(vistos)
                if n_trades % 5000 == 0:
                    _log(f"{n_trades} trades vistos, {n_matches} matches con wallets validadas")
        finally:
            ping_task.cancel()
    return vistos


async def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    wallets = cargar_wallets_validadas()
    ultimo_refresco = datetime.now(timezone.utc).timestamp()
    vistos = _vistos_cargar()
    _log(f"wallet_mirror_sniper arrancado -- {len(wallets)} wallets validadas (sig_bhfdr, n>=30)")
    while True:
        try:
            ahora_ts = datetime.now(timezone.utc).timestamp()
            if ahora_ts - ultimo_refresco > REFRESCO_WALLETS_S:
                wallets = cargar_wallets_validadas()
                ultimo_refresco = ahora_ts
                _log(f"wallets validadas refrescadas -- {len(wallets)} activas")
            vistos = await _correr_una_conexion(wallets, vistos)
        except (websockets.exceptions.ConnectionClosed, OSError, asyncio.TimeoutError) as e:
            _log(f"Conexión perdida ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        except Exception as e:
            _log(f"Error inesperado ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        _vistos_guardar(vistos)
        await asyncio.sleep(RECONNECT_ESPERA_S)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--resolver":
        # reusa el resolvedor de wallet_mirror_tracker.py pero apuntado a
        # nuestro propio CSV -- import perezoso para no cargar websockets
        # en el camino de resolución (invocado por cron, no por el screen).
        import wallet_mirror_tracker as wmt
        wmt.OUT = OUT
        wmt.OUT_LOCK = DIR_SHADOW / "wallet_mirror_sniper_dry_run.csv.lock"
        wmt.COLUMNS = COLUMNS
        n = resolver_pendientes()
        print(f"Resueltas: {n}")
    else:
        asyncio.run(main())
