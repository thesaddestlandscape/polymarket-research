#!/usr/bin/env python3
"""
sports_wallet_mirror_sniper.py — Wallet Mirror de sports/esports EN
TIEMPO REAL, DRY_RUN puro (18-Ago, mismo patrón que
weather_wallet_mirror_sniper.py, construido el mismo día).

Requiere sports_activity_ws.py corriendo (firehose propio, sin el filtro
whale-tier del fichero compartido de cripto). Abre su PROPIA conexión
independiente (mismo patrón que wallet_mirror_sniper.py de cripto: no
depender de la latencia/rotación del fichero de captura general).

3 hallazgos ya verificados con datos reales el mismo día en weather,
aplicables aquí sin re-verificar desde cero (mismo mecanismo RTDS,
mismo formato binario condition_id -- confirmado también en sports:
0 condition_ids con >2 outcomes distintos en 86k filas revisadas):
1. Mercados binarios por condition_id -- fade = outcome_index contrario
   en el MISMO condition_id, sin ambigüedad.
2. Dedup por (wallet,condition_id) -- solo reacciona al primer BUY.
3. Profundidad de libro real desde el PRIMER despliegue (no esperar a
   descubrir selección adversa semanas después, como pasó en cripto).

Separación estricta: solo lee data/sports/ (nunca data/shadow/data/live
de cripto), prefijo sports_.

⚠️ Solo observación -- NO coloca ninguna orden real.
Salida: data/sports/wallet_mirror_sniper_dry_run.csv

Corre en screen propia:
  screen -dmS sports-mirror bash -c "cd /root/polymarket-research && .venv/bin/python sports_wallet_mirror_sniper.py >> logs/sports_wallet_mirror_sniper.log 2>&1"

Resolución periódica (cron, no en el loop en vivo):
  .venv/bin/python sports_wallet_mirror_sniper.py --resolver
"""
import argparse
import asyncio
import csv
import fcntl
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests
import websockets

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from sports_wallet_edge_tracker import clasificar  # noqa: E402

DIR_SPORTS = REPO / "data" / "sports"
EDGE_JSON = DIR_SPORTS / "wallet_edge_score_por_categoria.json"
OUT = DIR_SPORTS / "wallet_mirror_sniper_dry_run.csv"
OUT_LOCK = DIR_SPORTS / "wallet_mirror_sniper_dry_run.lock"
VISTOS_PATH = DIR_SPORTS / "wallet_mirror_sniper_vistos.json"

GAMMA_API = "https://gamma-api.polymarket.com"
CLOB_BOOK_URL = "https://clob.polymarket.com/book"  # público, sin auth
STAKE_REF_EUR = 1.05
WS_URL = "wss://ws-live-data.polymarket.com"
PING_INTERVAL_S = 5
RECONNECT_ESPERA_S = 5
RECV_TIMEOUT_S = 30

REFRESCO_WALLETS_S = 1800
MAX_CIDS_POR_CICLO = 60

# 19-Ago: hallazgo real sobre las primeras 177 señales resueltas (petición
# Javi, "por qué palmamos si las wallets minan pasta") -- mirrorear TODO
# diluye el edge real de las wallets con su propio ruido. Dos filtros
# candidatos verificados con datos reales (SEGUIR, n=144):
#   - Tamaño de apuesta de la wallet (usd_wallet>=8.4€, corte por tercios):
#     p_shuffle=0.0002, hit 32.6%→64.3% bajo/alto.
#   - Precio de entrada del mirror (mejor_ask_mirror>=0.5): MÁS FUERTE,
#     p_shuffle=0.0000, hit 31.1%→78.6%, robusto en split-half cronológico
#     (ambas mitades). Cruzado: precio domina, tamaño no aporta información
#     extra una vez se tiene precio (corr(usd_wallet,precio_mirror)=0.256,
#     filtrar por ambos da PEOR PnL que solo por precio -- no combinar).
# FADE muestra el mismo patrón direccional pero con n=1-7 por bucket,
# insuficiente para fijar umbral propio -- se deja SIN clasificar (columna
# vacía) hasta que acumule n suficiente. NO cambia qué se detecta/loguea
# (se sigue capturando TODO, DRY_RUN puro) -- solo etiqueta cada señal para
# poder filtrar en análisis futuros sin tener que rehacer el cruce.
UMBRAL_PRECIO_SEGUIR = 0.5

COLUMNS = [
    "timestamp_utc", "trade_timestamp", "wallet", "tipo", "edge_pp_validado",
    "n_validado", "categoria", "condition_id", "market_slug",
    "outcome_index_wallet", "precio_wallet", "usd_wallet",
    "mirror_outcome_index", "transaction_hash", "outcome_real_index",
    "acierto", "resolved_ts", "lag_deteccion_s",
    "libro_ok", "mejor_ask_mirror", "profundidad_eur_mirror", "ratio_vs_stake_mirror",
    "cumple_filtro_precio",
]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def cargar_wallets_validadas() -> dict:
    if not EDGE_JSON.exists():
        return {}
    d = json.loads(EDGE_JSON.read_text(encoding="utf-8"))
    out = {}
    for w in d.get("wallets_validadas", []):
        tipo = "SEGUIR" if w["edge_pp"] > 0 else "FADE"
        out[(w["wallet"].lower(), w["categoria"])] = {
            "tipo": tipo, "edge_pp": w["edge_pp"], "n": w["n"],
        }
    return out


_TOKEN_CACHE: dict = {}


def _tokens_para_condition(condition_id: str):
    if condition_id in _TOKEN_CACHE:
        return _TOKEN_CACHE[condition_id]
    tokens = None
    try:
        r = requests.get(f"{GAMMA_API}/markets", timeout=10,
                          params={"condition_ids": condition_id})
        r.raise_for_status()
        for m in r.json():
            mcid = m.get("conditionId") or m.get("condition_id")
            if mcid != condition_id:
                continue
            raw = m.get("clobTokenIds")
            ids = json.loads(raw) if isinstance(raw, str) else raw
            if ids and len(ids) == 2:
                tokens = [str(ids[0]), str(ids[1])]
            break
    except Exception:
        tokens = None
    _TOKEN_CACHE[condition_id] = tokens
    return tokens


def _consultar_profundidad_libro(token_id: str, precio_entrada: float, stake_eur: float) -> dict:
    try:
        r = requests.get(CLOB_BOOK_URL, params={"token_id": token_id}, timeout=10)
        r.raise_for_status()
        book = r.json()
    except Exception:
        return {"ok": False, "error": "sin respuesta del libro"}
    if book is None:
        return {"ok": False, "error": "sin respuesta del libro"}
    asks = (book.get("asks") if isinstance(book, dict) else None) or []
    techo = precio_entrada * 1.05
    profundidad_eur = 0.0
    mejor_ask = None
    try:
        for lvl in asks:
            p = float(lvl.get("price")); s = float(lvl.get("size"))
            if mejor_ask is None or p < mejor_ask:
                mejor_ask = p
            if p <= techo:
                profundidad_eur += p * s
    except (TypeError, ValueError, AttributeError):
        return {"ok": False, "error": "libro con formato inesperado"}
    ratio = (profundidad_eur / stake_eur) if stake_eur > 0 else None
    return {"ok": True, "mejor_ask": mejor_ask, "profundidad_eur": round(profundidad_eur, 2),
            "ratio_vs_stake": round(ratio, 2) if ratio is not None else None}


def _fillability_mirror(condition_id: str, mirror_outcome_index: int, precio_referencia: float) -> dict:
    tokens = _tokens_para_condition(condition_id)
    if not tokens or mirror_outcome_index not in (0, 1):
        return {"ok": False, "error": "sin token_id"}
    return _consultar_profundidad_libro(tokens[mirror_outcome_index], precio_referencia, STAKE_REF_EUR)


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(list(vistos)[-50000:]), encoding="utf-8")


def _escribir_fila(fila: dict) -> None:
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
        _log(f"Conectado, {len(wallets)} combos (wallet,categoria) validados cargados")
        ping_task = asyncio.create_task(_mantener_ping(ws))
        n_total = n_matches = 0
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
                if (payload.get("side") or "").upper() != "BUY":
                    continue
                n_total += 1
                title = payload.get("title", "")
                categoria = clasificar(title, payload.get("eventSlug", ""))
                if categoria is None:
                    continue
                wallet = (payload.get("proxyWallet") or "").lower()
                condition_id = payload.get("conditionId", "")
                dedup_key = f"{wallet}|{condition_id}"
                if dedup_key in vistos:
                    continue
                info = wallets.get((wallet, categoria))
                if info is None:
                    continue
                vistos.add(dedup_key)
                try:
                    outcome_idx = int(payload.get("outcomeIndex"))
                except (TypeError, ValueError):
                    continue
                mirror_idx = outcome_idx if info["tipo"] == "SEGUIR" else 1 - outcome_idx
                try:
                    price = float(payload.get("price", 0) or 0)
                    size = float(payload.get("size", 0) or 0)
                except (TypeError, ValueError):
                    price = size = 0.0
                ws_ts = payload.get("timestamp")
                lag_s = None
                if ws_ts:
                    try:
                        lag_s = round(time.time() - float(ws_ts), 2)
                    except (TypeError, ValueError):
                        lag_s = None
                precio_ref = price if info["tipo"] == "SEGUIR" else round(1.0 - price, 6)
                fill = _fillability_mirror(condition_id, mirror_idx, precio_ref)
                mejor_ask = fill.get("mejor_ask")
                if info["tipo"] == "SEGUIR" and isinstance(mejor_ask, (int, float)):
                    cumple_filtro_precio = int(mejor_ask >= UMBRAL_PRECIO_SEGUIR)
                else:
                    cumple_filtro_precio = ""  # FADE: n insuficiente para fijar umbral propio (ver nota arriba)
                fila = {
                    "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
                    "trade_timestamp": ws_ts,
                    "wallet": wallet, "tipo": info["tipo"],
                    "edge_pp_validado": info["edge_pp"], "n_validado": info["n"],
                    "categoria": categoria,
                    "condition_id": condition_id, "market_slug": payload.get("slug", ""),
                    "outcome_index_wallet": outcome_idx, "precio_wallet": price,
                    "usd_wallet": round(price * size, 4),
                    "mirror_outcome_index": mirror_idx,
                    "transaction_hash": payload.get("transactionHash", ""),
                    "outcome_real_index": "", "acierto": "", "resolved_ts": "",
                    "lag_deteccion_s": lag_s,
                    "libro_ok": int(fill.get("ok", False)),
                    "mejor_ask_mirror": fill.get("mejor_ask", ""),
                    "profundidad_eur_mirror": fill.get("profundidad_eur", ""),
                    "ratio_vs_stake_mirror": fill.get("ratio_vs_stake", ""),
                    "cumple_filtro_precio": cumple_filtro_precio,
                }
                _escribir_fila(fila)
                n_matches += 1
                _log(f"MATCH #{n_matches}: {wallet[:14]} {categoria} {info['tipo']} "
                     f"edge={info['edge_pp']:+.1f}pp outcome_wallet={outcome_idx} "
                     f"mirror={mirror_idx} lag={lag_s}s libro_ok={fill.get('ok')} "
                     f"ratio_vs_stake={fill.get('ratio_vs_stake')}")
                if n_matches % 20 == 0:
                    _vistos_guardar(vistos)
                if n_total % 5000 == 0:
                    _log(f"{n_total} trades BUY vistos, {n_matches} matches con wallets validadas")
        finally:
            ping_task.cancel()
    return vistos


def outcome_por_condition_id(cid: str):
    try:
        r = requests.get(f"{GAMMA_API}/markets", timeout=15,
                          params={"condition_ids": cid, "closed": "true"})
        r.raise_for_status()
        data = r.json()
    except Exception:
        return None
    for m in data:
        mcid = m.get("conditionId") or m.get("condition_id")
        if mcid != cid or not m.get("closed"):
            continue
        try:
            precios = json.loads(m["outcomePrices"]) if isinstance(m.get("outcomePrices"), str) else m.get("outcomePrices")
            precios = [float(p) for p in precios]
        except Exception:
            continue
        for idx, p in enumerate(precios):
            if abs(p - 1.0) < 0.01:
                return idx
    return None


def resolver_pendientes() -> int:
    if not OUT.exists():
        return 0
    with open(OUT, newline="", encoding="utf-8") as f:
        filas = list(csv.DictReader(f))
    cids_pendientes = sorted({r["condition_id"] for r in filas
                               if not r.get("outcome_real_index") and r.get("condition_id")})
    outcomes = {}
    for cid in cids_pendientes[:MAX_CIDS_POR_CICLO]:
        idx = outcome_por_condition_id(cid)
        if idx is not None:
            outcomes[cid] = idx
        time.sleep(0.3)
    if not outcomes:
        return 0
    lock_f = open(OUT_LOCK, "w")
    try:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        with open(OUT, newline="", encoding="utf-8") as f:
            filas = list(csv.DictReader(f))
        resueltas = 0
        for r in filas:
            if r.get("outcome_real_index"):
                continue
            idx = outcomes.get(r.get("condition_id"))
            if idx is None:
                continue
            r["outcome_real_index"] = str(idx)
            r["acierto"] = "1" if str(idx) == str(r.get("mirror_outcome_index")) else "0"
            r["resolved_ts"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
            resueltas += 1
        if resueltas:
            with open(OUT, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=COLUMNS)
                w.writeheader()
                w.writerows(filas)
        return resueltas
    finally:
        fcntl.flock(lock_f, fcntl.LOCK_UN)
        lock_f.close()


async def main_ws() -> None:
    wallets = cargar_wallets_validadas()
    _log(f"wallets validadas: {len(wallets)} combos (SEGUIR="
         f"{sum(1 for v in wallets.values() if v['tipo']=='SEGUIR')}, "
         f"FADE={sum(1 for v in wallets.values() if v['tipo']=='FADE')})")
    vistos = _vistos_cargar()
    ultimo_refresco = time.time()
    while True:
        try:
            vistos = await _correr_una_conexion(wallets, vistos)
        except (websockets.exceptions.ConnectionClosed, OSError, asyncio.TimeoutError) as e:
            _log(f"Conexión perdida ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        except Exception as e:
            _log(f"Error inesperado ({type(e).__name__}: {e}) — reintentando en {RECONNECT_ESPERA_S}s")
        _vistos_guardar(vistos)
        if time.time() - ultimo_refresco >= REFRESCO_WALLETS_S:
            wallets = cargar_wallets_validadas()
            ultimo_refresco = time.time()
            _log(f"wallets validadas refrescadas: {len(wallets)} combos")
        await asyncio.sleep(RECONNECT_ESPERA_S)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--resolver", action="store_true")
    args = ap.parse_args()
    if args.resolver:
        n = resolver_pendientes()
        _log(f"resueltas este ciclo: {n}")
        if OUT.exists():
            with open(OUT, newline="", encoding="utf-8") as f:
                filas = [r for r in csv.DictReader(f) if r.get("outcome_real_index")]
            if filas:
                n_tot = len(filas)
                aciertos = sum(1 for r in filas if r["acierto"] == "1")
                n_seguir = sum(1 for r in filas if r["tipo"] == "SEGUIR")
                _log(f"acumulado resuelto: n={n_tot} hit={aciertos/n_tot*100:.1f}% "
                     f"(SEGUIR n={n_seguir}, FADE n={n_tot - n_seguir})")
        return 0
    asyncio.run(main_ws())
    return 0


if __name__ == "__main__":
    sys.exit(main())
