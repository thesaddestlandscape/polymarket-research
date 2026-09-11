"""sports_live_trade.py — Ejecución real de órdenes en Polymarket para
sports. Reutiliza las piezas de bajo nivel del CLOB de live_trade.py
(cripto) VÍA IMPORT (mismo repo, misma wallet, un único punto de verdad
para bugs ya cazados: redondeo decimal, resolución de token YES/NO,
consulta de profundidad) -- no se copian ni reimplementan.

⚠️ Lo que NO se reutiliza de live_trade.py: `_ejecutar_orden_polymarket`
en sí NO se importa -- esa función tiene acoplado veto_ballenas/CLV/
requote específicos del modelo de decisión de cripto (parsea `subtype`
asumiendo convención ACTIVO#marco, aplica _evaluar_veto_ballenas, etc.)
que no aplican ni son seguros de invocar sobre tuplas de sports. Se
escribe una función de ejecución propia, simple (firma+envía, sin esos
guardias específicos de cripto -- los guardias de sports viven en el
CALLER: sports_live_guard.py + sports_live_stake.py), mismo patrón que
ya se usó para adaptar esto a weather (weather_live_trade.py).

Ledger PROPIO (data/sports/trades.csv) -- nunca el de cripto.
"""

import fcntl
import json
from datetime import datetime, timezone
from pathlib import Path

import live_trade as _crypto_lt  # mismo repo -- SOLO se usan sus piezas de bajo nivel, agnósticas de mercado
from shadow_digest import enviar_telegram  # bot="sports" (27-Ago), ver SPORTS_TELEGRAM_TOKEN ahí

DIR_SPORTS_LIVE = Path("data/sports")
DIR_SPORTS_LIVE.mkdir(parents=True, exist_ok=True)
TRADES_CSV = DIR_SPORTS_LIVE / "trades.csv"
TRADES_LOCK_PATH = DIR_SPORTS_LIVE / ".trades_lock"
ORDEN_EN_CURSO_PATH = DIR_SPORTS_LIVE / "orden_en_curso.json"

MIN_ORDEN_CLOB_USD = 1.00  # el CLOB rechaza marketable BUY < $1 ("min size: 1"), mismo exchange que cripto
SPORTS_PRECIO_MAX = 0.95  # mismo tope duro que REQUOTE_PRECIO_MAX en live_trade.py -- nunca pagar más, pase lo que pase

TRADES_COLS = [
    "timestamp_utc", "market_id", "question", "end_date", "categoria",
    "tipo", "direction", "stake_eur", "entry_price", "edge_neto",
    "status", "close_timestamp", "exit_price", "outcome_real",
    "fee_eur", "pnl_bruto_eur", "pnl_neto_eur", "slip_real", "notas",
]


def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def get_token_ids(market_id: str) -> tuple[str, str, str | None]:
    """(yes_token_id, no_token_id, condition_id) -- reusa live_trade.py,
    pieza agnóstica de mercado, no toca datos/decisión de cripto."""
    return _crypto_lt._get_token_ids(market_id)


def consultar_profundidad_libro(token_id: str, precio_entrada: float, stake_eur: float) -> dict:
    """Solo lectura -- reusa live_trade.py::_consultar_profundidad_libro
    (client=None => endpoint público /book, solo lectura, agnóstico)."""
    return _crypto_lt._consultar_profundidad_libro(None, token_id, precio_entrada, stake_eur)


def _marcar_orden_en_curso(market_id: str, direction: str) -> None:
    try:
        ORDEN_EN_CURSO_PATH.write_text(json.dumps({
            "market_id": market_id, "direction": direction,
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }), encoding="utf-8")
    except Exception as e:
        log(f"  ⚠️ fallo al escribir orden_en_curso.json ({market_id}): {e}")


def _limpiar_orden_en_curso() -> None:
    try:
        ORDEN_EN_CURSO_PATH.unlink(missing_ok=True)
    except Exception as e:
        log(f"  ⚠️ fallo al borrar orden_en_curso.json: {e}")


# 01-Sep: _verificar_fill_real se trasladó a live_trade.py (código
# compartido) -- _ejecutar_orden_polymarket (el motor de cripto) tenía
# exactamente el mismo hueco que este comentario documentaba solo para
# sports, así que ahora vive en un único punto de verdad. Alias local
# para no tocar las ~2 llamadas de abajo.
_verificar_fill_real = _crypto_lt._verificar_fill_real


def ejecutar_orden_token(token_id: str, precio: float, stake_eur: float,
                          market_id_log: str = "", techo_precio: float | None = None) -> dict:
    """Ejecuta orden real FOK (fill-or-kill) en Polymarket para un
    token_id YA RESUELTO por el caller. `precio` es el precio del LADO
    DEL TOKEN que se compra (no siempre el lado YES -- el caller resuelve
    SEGUIR/FADE -> qué token_id y qué precio antes de llamar aquí).

    Deliberadamente NO recibe market_id/condition_id + resuelve tokens
    internamente (a diferencia de live_trade.py/weather_live_trade.py):
    en sports, el caller natural (sports_wallet_mirror_sniper.py) ya
    tiene el token_id correcto vía `_tokens_para_condition()` (resuelto
    desde condition_id, no desde el market_id numérico de Gamma que
    espera `gamma-api/markets/{market_id}`) -- pasar condition_id donde
    se espera market_id habría sido un bug real de identificador
    equivocado. Si algún día hace falta un camino que solo tenga
    market_id, añadir una función de resolución explícita, no reusar
    ésta a ciegas.

    Simplificado respecto a live_trade.py (cripto): sin veto_ballenas,
    sin requote contra edge_dir, sin veto CLV -- esos guardias no
    aplican al modelo de decisión de sports (Wallet Mirror) o viven en
    el CALLER (sports_live_guard.py + sports_live_stake.py +
    verificar_circuit_breaker). Esta función solo firma y envía,
    reusando la mecánica CLOB de bajo nivel de live_trade.py.

    `techo_precio` (propuesta #3 Arquetipo A aplicada a sports, 01-Sep,
    aprobación explícita Javi): el FOK se enviaba con price=precio exacto
    -- una limit-buy a ese precio solo puede casar contra ventas EN ese
    nivel, nunca contra niveles peores, aunque `wallet_mirror_sniper_
    dry_run.csv` confirme profundidad agregada de sobra (mediana
    ratio_vs_stake_mirror=499,8x) unos niveles más arriba. El caller pasa
    aquí el límite superior de la zona de precio YA confirmada rentable
    (`sports_wallet_mirror_gate_bucket.techo_confirmado()`) -- nunca se
    ensancha más allá de esa zona, y nunca por encima de `precio` si el
    caller no pasa nada (comportamiento anterior exacto, fail-closed por
    falta de dato)."""
    entry_price = precio
    precio_limite_fok = precio
    if techo_precio is not None and techo_precio > precio:
        # code-review 01-Sep (hallazgo real, 2 rondas): el primer intento
        # (min(max(techo_precio,precio), SPORTS_PRECIO_MAX)) seguía pudiendo
        # dar un resultado < precio en el caso extremo de que `precio` YA
        # superara SPORTS_PRECIO_MAX (sports no tiene el veto previo que sí
        # tiene cripto sobre mejor_ask>REQUOTE_PRECIO_MAX) -- eso enviaría
        # un límite peor que el ask actual, garantizando que el FOK muera,
        # peor que el comportamiento anterior (price=precio exacto). Fix
        # definitivo: solo ensanchar si el candidato resultante es >= precio
        # de verdad; si no, se queda en `precio` sin cambios -- nunca puede
        # producir un precio peor que antes, en NINGÚN caso, sin necesitar
        # ningún veto adicional. No disparable con la whitelist de hoy
        # (todo hi<=0.50), pero blindado igual por ser código de dinero real.
        candidato = min(max(techo_precio, precio), SPORTS_PRECIO_MAX)
        if candidato >= precio:
            precio_limite_fok = candidato
            log(f"  📈 Límite FOK ensanchado {precio:.4f}→{precio_limite_fok:.4f} "
                f"(techo de zona confirmada) -- deja al CLOB barrer niveles peores sin matar la orden")
    try:
        client = _crypto_lt._get_clob_client()
        from py_clob_client_v2 import MarketOrderArgsV2, OrderType

        if stake_eur < MIN_ORDEN_CLOB_USD:
            log(f"  ⛔ Stake {stake_eur:.2f}€ < mínimo CLOB ${MIN_ORDEN_CLOB_USD:.2f} -- no se ejecuta")
            return {"ok": False, "no_fill": True, "stake_bajo_minimo": True,
                    "order_id": None, "entry_price": entry_price, "fee_eur": 0.0,
                    "error": f"stake {stake_eur:.2f} < mínimo CLOB"}

        _lock_f = open(TRADES_LOCK_PATH, "w")
        fcntl.flock(_lock_f, fcntl.LOCK_EX)
        try:
            _marcar_orden_en_curso(market_id_log or token_id, "BUY")
            # Reintento con stake desplazado +-0.01€ -- mismo bug de
            # precisión decimal de la librería que ya se cazó en cripto/
            # weather (_parchear_redondeo_clob ya debería evitarlo casi
            # siempre, esto es red de seguridad adicional).
            intentos_stake = [round(stake_eur, 2), round(stake_eur - 0.01, 2), round(stake_eur + 0.01, 2)]
            intentos_stake = [a for a in intentos_stake if a >= MIN_ORDEN_CLOB_USD]
            resp = None
            for intento, amt in enumerate(intentos_stake):
                if amt <= 0:
                    continue
                order_args = MarketOrderArgsV2(token_id=token_id, amount=amt, side="BUY", price=precio_limite_fok)
                try:
                    signed_order = client.create_market_order(order_args)
                    resp = client.post_order(signed_order, OrderType.FOK)
                    stake_eur = amt
                    if intento > 0:
                        log(f"  ⚠️ orden aceptada en reintento {intento} con stake={amt:.2f}€")
                    break
                except Exception as e_intento:
                    if "invalid amounts" not in str(e_intento) or intento == len(intentos_stake) - 1:
                        raise
                    log(f"  ⚠️ 'invalid amounts' con stake={amt:.2f}€, reintentando...")
            if resp is None:
                raise RuntimeError("no se pudo construir una orden con amounts válidos")
        finally:
            _limpiar_orden_en_curso()
            fcntl.flock(_lock_f, fcntl.LOCK_UN)
            _lock_f.close()

        order_id = resp.get("orderID") or resp.get("id") or str(resp)

        # 31-Ago (hallazgo real, ver _verificar_fill_real): NUNCA confiar
        # en resp.get("price"/"feeRateBps") a secas -- pueden venir con el
        # valor SOLICITADO (fallback silencioso) si la orden no llegó a
        # casar. Verificar contra el histórico real de fills antes de
        # devolver ok=True.
        ts_envio = datetime.now(timezone.utc).timestamp()
        trade_real = _verificar_fill_real(client, market_id_log or "", order_id, ts_envio)
        if trade_real is None:
            log(f"  ⛔ orden aceptada (order_id={order_id}) pero SIN evidencia de fill real "
                f"tras el poll -- fail-closed, no se registra como ejecutada")
            enviar_telegram(
                f"⚽ SPORTS\n⚠️ *Orden aceptada pero sin fill confirmado* (posible fantasma)\n"
                f"market={market_id_log or token_id}\norder_id={order_id}\n"
                f"NO se ha registrado ningún trade -- revisar manualmente.",
                bot="sports",
            )
            return {"ok": False, "no_fill": True, "sin_fill_confirmado": True,
                    "order_id": order_id, "entry_price": entry_price, "fee_eur": 0.0,
                    "error": "orden aceptada por la API pero sin evidencia de fill real en get_trades()"}

        # fallback usa precio_limite_fok (precio real solicitado), no
        # `precio` (mejor_ask pre-ensanche) -- mismo fix que en cripto.
        filled_price = float(trade_real.get("price", precio_limite_fok))
        fee_rate_bps = trade_real.get("fee_rate_bps") or 0
        fee = float(fee_rate_bps) / 10000 * stake_eur if fee_rate_bps else 0.0
        slip_real = round(filled_price - precio, 4)

        log(f"  ✅ Orden ejecutada y VERIFICADA: token={token_id} market={market_id_log or '?'} "
            f"stake={stake_eur:.2f}€ precio={filled_price:.4f} slip={slip_real:+.4f} order_id={order_id}")
        enviar_telegram(
            f"⚽ SPORTS\n"
            f"🎯 *Orden live ejecutada (verificada contra get_trades)*\n"
            f"market={market_id_log or token_id}\n"
            f"stake={stake_eur:.2f}€ precio={filled_price:.4f} slip={slip_real:+.4f}\n"
            f"order_id={order_id}",
            bot="sports",
        )
        return {"ok": True, "order_id": order_id, "entry_price": filled_price,
                "fee_eur": fee, "slip_real": slip_real, "error": ""}
    except Exception as e:
        err_str = str(e)
        if "couldn't be fully filled" in err_str or "FOK" in err_str:
            log(f"  ⚠️ FOK kill (sin liquidez a ese precio) -- no fill: {e}")
            return {"ok": False, "no_fill": True, "order_id": None,
                    "entry_price": entry_price, "fee_eur": 0.0, "error": err_str}
        log(f"  ❌ error ejecutando orden: {e}")
        enviar_telegram(
            f"⚽ SPORTS\n❌ *Orden live ERROR*\nmarket={market_id_log or token_id}\n{err_str}",
            bot="sports",
        )
        return {"ok": False, "no_fill": False, "order_id": None,
                "entry_price": entry_price, "fee_eur": 0.0, "error": err_str}


def registrar_trade(row: dict) -> None:
    """Append a data/sports/trades.csv -- ledger PROPIO, nunca el de
    cripto. flock protege el append de un entrelazado entre procesos."""
    import csv
    with open(TRADES_LOCK_PATH, "w") as lock_f:
        fcntl.flock(lock_f, fcntl.LOCK_EX)
        try:
            nuevo = not TRADES_CSV.exists()
            with open(TRADES_CSV, "a", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=TRADES_COLS, extrasaction="ignore")
                if nuevo:
                    w.writeheader()
                w.writerow({col: row.get(col, "") for col in TRADES_COLS})
        finally:
            fcntl.flock(lock_f, fcntl.LOCK_UN)
