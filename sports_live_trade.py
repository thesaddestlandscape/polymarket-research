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


def ejecutar_orden_token(token_id: str, precio: float, stake_eur: float,
                          market_id_log: str = "") -> dict:
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
    reusando la mecánica CLOB de bajo nivel de live_trade.py."""
    entry_price = precio
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
                order_args = MarketOrderArgsV2(token_id=token_id, amount=amt, side="BUY", price=precio)
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
        filled_price = float(resp.get("price", precio))
        fee = float(resp.get("feeRateBps", 0)) / 10000 * stake_eur
        slip_real = round(filled_price - precio, 4)

        log(f"  ✅ Orden ejecutada: token={token_id} market={market_id_log or '?'} "
            f"stake={stake_eur:.2f}€ precio={filled_price:.4f} slip={slip_real:+.4f} order_id={order_id}")
        enviar_telegram(
            f"⚽ SPORTS\n"
            f"🎯 *Orden live ejecutada*\n"
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
