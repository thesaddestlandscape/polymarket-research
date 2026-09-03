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

import sports_live_guard as _guard
import sports_live_stake as _stake
import sports_wallet_mirror_gate_bucket as _gate  # 27-Ago: segundo guardián,
# independiente de pares_permitidos_live -- ver docstring del módulo
from sports_wallet_mirror_clv import clv_tupla_sports  # 03-Sep: tercer
# guardián -- petición explícita Javi al promocionar CS#FADE[0.60,0.65)/
# LoL#FADE[0.70,0.75)/Dota#SEGUIR[0.47,0.52): mismo veto CLV que cripto
# (live_trade.py::_clv_tupla), construido 27-Ago pero nunca conectado a
# ninguna decisión hasta hoy.

CLV_VETO_MIN_N = 20  # mismo umbral que cripto (live_trade.py::CLV_VETO_MIN_N)

REPO = Path(__file__).resolve().parent

# 27-Ago: conexión explícita a la infraestructura live de sports
# (sports_live_guard.py/sports_live_stake.py/sports_live_trade.py,
# construida el mismo día).
#
# 31-Ago: DRY_RUN=False -- aprobación explícita de Javi en sesión,
# primera promoción real de sports. Whitelist restringida a
# LoL#SEGUIR#0.45:0.50 en config_live_sports.json (checklist completo:
# n=69, BH-FDR, split-half, g_kelly positivo, sin concentración,
# fill-ability real 82.1% -- ver nota de promoción en el propio config).
# CUALQUIER otra tupla sigue fail-closed (whitelist vacía para ellas +
# gate_bucket_veredicto vivo como segundo guardián, ver comentario más
# abajo). Import de sports_live_trade.ejecutar_orden_token() se hace
# DENTRO de la rama DRY_RUN=False (import perezoso).
DRY_RUN = False
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
    "gate_veredicto", "stake_sim_eur", "circuit_breaker_bloquea", "decision_dry_run",
    "gate_bucket_veredicto",  # 27-Ago noche, añadida al final a propósito --
    # el CSV ya tenía ~10k filas escritas con el header viejo; una columna
    # nueva en medio habría desalineado todas las filas futuras bajo
    # DictReader (ver commit del mismo día). Al final, las filas viejas
    # simplemente quedan con este campo vacío bajo el header nuevo.
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


_END_DATE_CACHE: dict = {}  # 27-Ago: mismo request que _tokens_para_condition,
# cacheado aparte -- alimenta analisis_diario_salud_sistema.py (chequeo de
# trades OPEN atascados tras el cierre del mercado), que sin esto no podía
# vigilar sports (end_date siempre vacío en trades.csv).


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
            _END_DATE_CACHE[condition_id] = m.get("endDate", "")
            break
    except Exception:
        tokens = None
    _TOKEN_CACHE[condition_id] = tokens
    return tokens


def _end_date_para_condition(condition_id: str) -> str:
    """Requiere que _tokens_para_condition() ya se haya llamado para este
    condition_id (mismo request, sin llamada de red extra) -- fail-open a
    "" si no está cacheado todavía (nunca bloquea el registro del trade
    por esto)."""
    return _END_DATE_CACHE.get(condition_id, "")


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

                # 27-Ago: evaluación de la infraestructura live (fail-closed
                # por diseño -- switch OFF y whitelist vacía hoy, así que
                # esto siempre da "no se ejecuta" mientras Javi no decida lo
                # contrario). Requiere mejor_ask real para evaluar el
                # micro-bucket -- sin libro consultado con éxito, no se
                # puede decidir nada (fail-closed, no "permitir por defecto").
                #
                # 27-Ago noche: DOS guardianes independientes, mismo patrón
                # que WALLET_MIRROR cripto (wallet_mirror_executor_dryrun.py)
                # -- (1) whitelist estática pares_permitidos_live (editada a
                # mano por Javi, categoria#tipo#lo:hi), (2) gate VIVO
                # (sports_wallet_mirror_gate_bucket.evaluar(), regenerado a
                # diario) que puede vetar automáticamente un bucket ya
                # aprobado si empieza a sangrar dinero real (kill switch),
                # sin que nadie tenga que tocar la whitelist a mano.
                gate_veredicto = "sin_libro"
                gate_bucket_veredicto = None
                gate_bucket_resultado = None
                stake_sim = 0.0
                cb_bloquea = False
                decision_dry_run = "NO_dispara"
                if isinstance(mejor_ask, (int, float)):
                    ok_operar, motivo_guard = _guard.puede_operar_live(categoria, info["tipo"], precio=mejor_ask)
                    gate_veredicto = motivo_guard if not ok_operar else "permitido"
                    if ok_operar:
                        gate_bucket_resultado = _gate.evaluar(categoria, info["tipo"], mejor_ask)
                        gate_bucket_veredicto = gate_bucket_resultado["veredicto"]
                        if gate_bucket_veredicto != "bueno_confirmado":
                            ok_operar = False
                            gate_veredicto = f"gate_bucket={gate_bucket_veredicto}"
                    if ok_operar:
                        # Veto CLV (03-Sep, mismo patrón que live_trade.py::
                        # _clv_tupla en cripto): tupla#dirección con CLV medio
                        # < 0 sostenido pierde contra la línea de cierre --
                        # guardia adicional sobre el gate de micro-bucket, no
                        # sustituto. Sin datos suficientes (n<20) no veta
                        # (fail-open por n insuficiente, mismo criterio que
                        # el resto del proyecto -- un veto que nunca ha visto
                        # datos no debe bloquear nada).
                        clv_medio, n_clv = clv_tupla_sports(categoria, info["tipo"])
                        if n_clv >= CLV_VETO_MIN_N and clv_medio < 0:
                            ok_operar = False
                            gate_veredicto = f"veto_clv(clv={clv_medio:+.4f},n={n_clv})"
                            _log(f"  ⛔ Veto CLV: {categoria}#{info['tipo']} clv_medio={clv_medio:+.4f} "
                                 f"(n={n_clv}) < 0 — no se ejecuta")
                    if ok_operar:
                        cb_bloquea = _stake.bloquear_por_circuit_breaker(lambda m: _log(f"circuit breaker: {m}"))
                        if not cb_bloquea:
                            edge_frac = abs(info["edge_pp"]) / 100.0
                            # 27-Ago noche (/code-review, hallazgo real): direction= debe ser
                            # el índice del outcome que se compraría (mirror_idx, "0"/"1" --
                            # lo que de verdad se guarda luego en trades.csv), NUNCA info["tipo"]
                            # (SEGUIR/FADE) -- con ese valor la penalización de inventario
                            # direccional nunca podía activarse (comparaba "SEGUIR"/"FADE"
                            # contra "0"/"1", cero coincidencias posibles).
                            stake_info = _stake.calcular_stake(edge_frac, categoria, info["tipo"], direction=str(mirror_idx))
                            stake_sim = stake_info["stake_eur"]
                            if stake_info["viable"]:
                                decision_dry_run = "DISPARARIA"
                                if not DRY_RUN:
                                    import sports_live_trade as _trade
                                    tokens_orden = _tokens_para_condition(condition_id)
                                    if tokens_orden is None:
                                        _log(f"  ⚠️ no se pudo resolver token_id para {condition_id}, no se ejecuta")
                                    else:
                                        # 03-Sep (fix real, mismo hallazgo y mismo
                                        # patrón que _ejecutar_orden_polymarket en
                                        # cripto, ver commit de la misma fecha:
                                        # racha WALLET_MIRROR#BTC/ETH#15min real
                                        # -6,55€ por validar el gate contra UN solo
                                        # snapshot de precio antes de firmar).
                                        # `mejor_ask`/`gate_bucket_resultado` de
                                        # arriba pueden ser de varios cientos de ms
                                        # atrás (websocket→guard→circuit
                                        # breaker→stake→resolución de token, todo
                                        # antes de llegar aquí) -- en un mercado
                                        # moviéndose rápido eso no protege nada.
                                        # Se exige reconfirmar bueno_confirmado en
                                        # N lecturas FRESCAS consecutivas
                                        # (re-consultando el libro cada vez, nunca
                                        # reusando el mismo snapshot) lo más pegado
                                        # posible a la construcción de la orden
                                        # real. Código de seguridad live -- no
                                        # minimizar.
                                        _n_rechequeos = _guard._cargar_config().get(
                                            "riesgo", {}).get("n_rechequeos_gate_bucket", 2)
                                        _ask_confirmado = None
                                        _gate_confirmado = gate_bucket_resultado
                                        resultado = None  # sin esto, un rechequeo abortado
                                        # reutilizaría el `resultado` de una iteración
                                        # ANTERIOR del bucle exterior (websocket) y
                                        # `if resultado.get("ok"):` de abajo registraría
                                        # un trade fantasma o reventaría con AttributeError
                                        # si nunca hubo un trade previo -- fail-closed.
                                        for _intento in range(1, _n_rechequeos + 1):
                                            if _intento > 1:
                                                # /code-review 03-Sep, hallazgo real: esta
                                                # coroutine (_correr_una_conexion) es la que
                                                # también mantiene vivo el ping/recv del
                                                # websocket -- time.sleep() bloqueante aquí
                                                # congela TODO el event loop (ping no sale,
                                                # ningún otro mensaje se procesa) durante la
                                                # pausa. await asyncio.sleep() cede el control.
                                                await asyncio.sleep(0.25)
                                            # /code-review 03-Sep, segundo hallazgo real:
                                            # _fillability_mirror() hace un requests.get()
                                            # bloqueante (timeout=10s) -- llamarlo a pelo aquí
                                            # añade 1-2 bloqueos más del event loop por señal
                                            # disparada (encima del que ya existe en la línea
                                            # ~299 de este mismo flujo), justo en el momento de
                                            # ejecutar dinero real. to_thread() lo saca del loop
                                            # sin tocar la función síncrona compartida.
                                            _fill_fresh = await asyncio.to_thread(
                                                _fillability_mirror, condition_id, mirror_idx, precio_ref)
                                            _ask_fresh = _fill_fresh.get("mejor_ask")
                                            if not isinstance(_ask_fresh, (int, float)):
                                                _log(f"  ⛔ Re-chequeo gate {_intento}/{_n_rechequeos}: "
                                                     f"sin datos de libro frescos -- no se ejecuta (fail-closed)")
                                                _ask_confirmado = None
                                                break
                                            _gate_fresh = _gate.evaluar(categoria, info["tipo"], float(_ask_fresh))
                                            if _gate_fresh["veredicto"] != "bueno_confirmado":
                                                _log(f"  ⛔ Re-chequeo gate {_intento}/{_n_rechequeos}: "
                                                     f"ask_fresco={_ask_fresh:.4f} veredicto={_gate_fresh['veredicto']} "
                                                     f"(precio en movimiento, no bueno_confirmado) -- no se ejecuta")
                                                _ask_confirmado = None
                                                break
                                            _ask_confirmado = float(_ask_fresh)
                                            _gate_confirmado = _gate_fresh
                                        if _ask_confirmado is None:
                                            gate_veredicto = "rechequeo_abortado"
                                        else:
                                            mejor_ask = _ask_confirmado
                                            # Propuesta #3 Arquetipo A aplicada a sports
                                            # (01-Sep, aprobación explícita Javi): techo
                                            # de precio seguro derivado de la zona EXACTA
                                            # que confirmó bueno_confirmado (grid o fino),
                                            # nunca del edge (sports no tiene edge_dir en
                                            # unidades de precio como cripto). Recalculado
                                            # con el ask/veredicto del rechequeo, no el
                                            # snapshot viejo de antes de reconfirmar.
                                            techo_precio = _gate.techo_confirmado(
                                                categoria, info["tipo"], mejor_ask, _gate_confirmado)
                                            resultado = _trade.ejecutar_orden_token(
                                                tokens_orden[mirror_idx], mejor_ask, stake_sim,
                                                market_id_log=condition_id, techo_precio=techo_precio)
                                            _log(f"  {'EJECUTADO' if resultado.get('ok') else 'ERROR'}: {resultado}")
                                        if resultado is not None and resultado.get("ok"):
                                            # 27-Ago noche: sin esto, un trade real se enviaba
                                            # pero NUNCA se registraba -- bankroll_actual()/
                                            # circuit breakers habrían quedado ciegos a él para
                                            # siempre (hallazgo real, corregido antes del primer
                                            # trade real, ver vigia_sports_micro_bucket_kill_
                                            # switch_wallet_mirror.py y sports_resolve.py).
                                            _trade.registrar_trade({
                                                "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                                                "market_id": condition_id,
                                                "question": payload.get("slug", ""),
                                                "end_date": _end_date_para_condition(condition_id),
                                                "categoria": categoria, "tipo": info["tipo"],
                                                "direction": str(mirror_idx),
                                                "stake_eur": stake_sim,
                                                "entry_price": resultado.get("entry_price", mejor_ask),
                                                "edge_neto": edge_frac,
                                                "status": "OPEN",
                                                "close_timestamp": "", "exit_price": "",
                                                "outcome_real": "", "fee_eur": resultado.get("fee_eur", 0.0),
                                                "pnl_bruto_eur": "", "pnl_neto_eur": "",
                                                "slip_real": resultado.get("slip_real", ""),
                                                "notas": f"wallet_mirror wallet={wallet}",
                                            })

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
                    "gate_veredicto": gate_veredicto,
                    "gate_bucket_veredicto": gate_bucket_veredicto or "",
                    "stake_sim_eur": stake_sim,
                    "circuit_breaker_bloquea": int(cb_bloquea),
                    "decision_dry_run": decision_dry_run,
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
