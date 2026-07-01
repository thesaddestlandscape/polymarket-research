"""
live_trade.py — Motor de ejecución live. Se añade al fast loop tras shadow_predict.

Flujo por ciclo:
  1. live_guard: ¿puede operar ahora? (switch + ventana)
  2. Leer predicciones del ciclo actual (predictions_HOY.csv)
  3. Filtrar señales que pasan el umbral IC mínimo y son de estrategias permitidas
  4. Evitar duplicados: no operar en el mismo mercado dos veces
  5. Calcular stake con live_stake.py
  6. Ejecutar orden real en Polymarket via CLOB API (py-clob-client)
  7. Registrar en data/live/trades.csv
  8. Log completo en logs/live.log
"""

import csv
import json
import os
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path

from live_guard import puede_operar_live, estado_live, switch_activo
from live_stake import calcular_stake, bankroll_actual, verificar_circuit_breaker, pnl_live_hoy, stakes_desplegados_ventana_actual
from shadow_digest import enviar_telegram

DIR_LIVE    = Path("data/live")
DIR_SHADOW  = Path("data/shadow")
TRADES_CSV  = DIR_LIVE  / "trades.csv"
PARAMS_PATH = DIR_SHADOW / "strategy_params.json"
LOG_PATH    = Path("logs/live.log")
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

TRADES_COLS = [
    "timestamp_utc", "market_id", "question", "end_date",
    "strategy", "subtype", "direction", "stake_eur",
    "entry_price", "ic_modelo", "edge_neto",
    "conviction_score", "kelly_recomendado",
    "status", "close_timestamp", "exit_price",
    "outcome_real", "fee_eur", "pnl_bruto_eur", "pnl_neto_eur", "notas",
]


def log(msg: str):
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    line = f"[{ts}] {msg}"
    print(line)
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def _cargar_params() -> dict:
    if not PARAMS_PATH.exists():
        return {}
    with open(PARAMS_PATH, encoding="utf-8") as f:
        return json.load(f).get("estrategias", {})


def _cargar_config() -> dict:
    p = DIR_LIVE / "config_live.json"
    if not p.exists():
        return {}
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def _ya_operados_hoy() -> set:
    """Set de market_id que ya tienen trade OPEN o CLOSED hoy."""
    if not TRADES_CSV.exists():
        return set()
    config = _cargar_config()
    offset = config.get("utc_offset_verano", 2)
    hoy    = (datetime.now(timezone.utc) + timedelta(hours=offset)).strftime("%Y-%m-%d")
    vistos = set()
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if (row.get("timestamp_utc") or "")[:10] == hoy:
                vistos.add(row.get("market_id", ""))
    return vistos


def _cargar_predicciones_hoy() -> list:
    """Carga las predicciones de hoy con decision BUY_YES o BUY_NO."""
    hoy  = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    path = DIR_SHADOW / f"predictions_{hoy}.csv"
    if not path.exists():
        return []
    rows = []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("decision") in ("BUY_YES", "BUY_NO"):
                rows.append(row)
    return rows


def _feature_match(feat_val, cond, umbral):
    """Idéntico a shadow_predict.py::_feature_match — mismo criterio para
    evaluar condiciones de patrones_ganadores/filtros_causales."""
    try:
        v, u = float(feat_val), float(umbral)
        if cond == "abs_gt": return abs(v) > u
        if cond == "abs_lt": return abs(v) <= u
        if cond == "gt":     return v > u
        if cond == "lt":     return v <= u
    except (TypeError, ValueError):
        pass
    return False


def _ic_n_para_subtype(strategy: str, subtype: str, params: dict,
                       decision: str = "", min_n: int = 40, min_ic: float = 0.08,
                       features: dict | None = None) -> tuple[float, int]:
    """IC Bayesiano efectivo del subtype + n de la muestra que lo respalda.
    Usa ic_BUY_NO/ic_BUY_YES (direccional) solo si su propio n_BUY_NO/n_BUY_YES
    ya cumple min_n; si no, cae al ic_bayes/n agregados. Así el n devuelto
    siempre corresponde a la muestra real detrás del IC usado (antes se
    comparaba min_n contra el n agregado aunque se usara un IC direccional
    de muestra mucho menor).

    2026-07-01: si el resultado normal (direccional o agregado) NO alcanza
    min_n Y min_ic a la vez — exactamente los mismos umbrales que ya
    aplicaba el caller después de llamar a esta función — se comprueba si
    esta predicción concreta cumple la condición de un patrón causal ya
    confirmado (patrones_ganadores con su propio n_patron>=min_n e
    ic_patron>=min_ic). Si es así, se devuelve el IC/n de ese patrón.

    Es puramente aditivo respecto al caso ACEPTADO: cualquier combinación
    que antes pasaba el filtro (ic>=min_ic y n>=min_n) sigue devolviendo
    exactamente el mismo (ic, n) y se acepta igual — se comprueba esa
    condición antes de mirar ningún patrón. Solo cambia el resultado en
    combinaciones que HOY se rechazan (ej. ORDER_FLOW_5M: n direccional de
    sobra pero IC diluido por debajo de 0.08 en el agregado, mientras que su
    patrón delta_ratio confirmado si tiene ic_patron>=0.08)."""
    claves = []
    if "#" in subtype:
        a, d = subtype.split("#", 1)
        claves = [f"{strategy}#{subtype}", f"{strategy}#{a}", f"{strategy}#{d}", strategy]
    elif subtype:
        claves = [f"{strategy}#{subtype}", strategy]
    else:
        claves = [strategy]

    ic_normal, n_normal, clave_usada = None, None, None
    for k in claves:
        if k in params:
            p = params[k]
            if decision == "BUY_NO" and p.get("ic_BUY_NO") is not None:
                n_dir = p.get("n_BUY_NO", 0)
                if n_dir >= min_n:
                    ic_normal, n_normal, clave_usada = float(p["ic_BUY_NO"]), n_dir, k
                    break
            elif decision == "BUY_YES" and p.get("ic_BUY_YES") is not None:
                n_dir = p.get("n_BUY_YES", 0)
                if n_dir >= min_n:
                    ic_normal, n_normal, clave_usada = float(p["ic_BUY_YES"]), n_dir, k
                    break
            ic_normal, n_normal, clave_usada = float(p.get("ic_bayes", 0)), p.get("n", 0), k
            break

    if clave_usada is None:
        return 0.0, 0
    if n_normal >= min_n and ic_normal >= min_ic:
        return ic_normal, n_normal

    # No alcanza min_n+min_ic por la vía normal — probar patrón causal confirmado
    if features:
        mejor_patron = None
        for k in claves:
            for patron in params.get(k, {}).get("patrones_ganadores", []):
                n_patron = patron.get("n_patron", 0)
                if n_patron < min_n:
                    continue
                ic_patron = float(patron.get("ic_patron", 0))
                if ic_patron < min_ic:
                    continue
                fv = features.get(patron.get("feature"))
                if fv is None:
                    continue
                if not _feature_match(fv, patron.get("condicion", ""), patron.get("umbral", 999)):
                    continue
                if mejor_patron is None or ic_patron > mejor_patron[0]:
                    mejor_patron = (ic_patron, n_patron)
        if mejor_patron:
            return mejor_patron

    return ic_normal, n_normal


def _get_clob_client():
    """Crea cliente CLOB V2 autenticado desde .env."""
    from dotenv import load_dotenv
    from py_clob_client_v2 import ClobClient, ApiCreds
    from py_clob_client_v2.constants import POLYGON
    load_dotenv(DIR_LIVE / ".env")
    key = os.getenv("POLY_PRIVATE_KEY")
    creds = ApiCreds(
        api_key=os.getenv("POLY_API_KEY"),
        api_secret=os.getenv("POLY_API_SECRET"),
        api_passphrase=os.getenv("POLY_API_PASSPHRASE"),
    )
    deposit_wallet = os.getenv("POLY_DEPOSIT_WALLET")
    return ClobClient(
        "https://clob.polymarket.com",
        key=key,
        chain_id=POLYGON,
        creds=creds,
        signature_type=3,       # POLY_1271 — deposit wallet flow
        funder=deposit_wallet,
    )


def _get_token_ids(market_id: str) -> tuple[str, str]:
    """Devuelve (yes_token_id, no_token_id) desde Gamma API."""
    resp = requests.get(
        f"https://gamma-api.polymarket.com/markets/{market_id}",
        timeout=10
    )
    resp.raise_for_status()
    data = resp.json()
    raw = data.get("clobTokenIds", [])
    tokens = json.loads(raw) if isinstance(raw, str) else raw
    if len(tokens) < 2:
        raise ValueError(f"clobTokenIds incompleto para market {market_id}: {tokens}")
    return tokens[0], tokens[1]


def _consultar_profundidad_libro(client, token_id: str, precio_entrada: float,
                                 stake_eur: float) -> dict:
    """
    Observación pura (no cambia ninguna decisión): consulta el order book
    real de Polymarket para el token que vamos a comprar y mide cuánta
    profundidad hay en el lado ask cerca del precio de entrada. Se loguea
    junto a cada orden para poder cruzar después si los kills de FOK
    ("sin liquidez a ese precio") correlacionan con libros finos.
    """
    try:
        book = client.get_order_book(token_id)
        asks = (book.get("asks") if isinstance(book, dict) else getattr(book, "asks", None)) or []
        techo = precio_entrada * 1.05  # banda razonable sobre el precio objetivo
        profundidad_eur = 0.0
        mejor_ask = None
        for lvl in asks:
            p = float(lvl.get("price") if isinstance(lvl, dict) else lvl.price)
            s = float(lvl.get("size") if isinstance(lvl, dict) else lvl.size)
            if mejor_ask is None or p < mejor_ask:
                mejor_ask = p
            if p <= techo:
                profundidad_eur += p * s
        ratio = (profundidad_eur / stake_eur) if stake_eur > 0 else None
        return {
            "ok": True,
            "mejor_ask": mejor_ask,
            "profundidad_eur": round(profundidad_eur, 2),
            "n_niveles": len(asks),
            "ratio_vs_stake": round(ratio, 1) if ratio is not None else None,
        }
    except Exception as e:
        return {"ok": False, "error": str(e)}


def _ejecutar_orden_polymarket(market_id: str, direction: str,
                               stake_eur: float, entry_price: float) -> dict:
    """Ejecuta orden real en Polymarket via CLOB API."""
    try:
        from py_clob_client_v2 import MarketOrderArgsV2, OrderType
        yes_token, no_token = _get_token_ids(market_id)
        if direction == "BUY_YES":
            token_id = yes_token
            precio   = entry_price
        else:  # BUY_NO
            token_id = no_token
            precio   = round(1.0 - entry_price, 6)

        client = _get_clob_client()

        # Observación de profundidad del libro — no afecta a la ejecución,
        # solo se loguea para poder correlacionar con kills de FOK más tarde.
        depth = _consultar_profundidad_libro(client, token_id, precio, stake_eur)
        if depth.get("ok"):
            log(f"  📊 Libro {market_id}/{direction}: mejor_ask={depth['mejor_ask']} "
                f"profundidad≈{depth['profundidad_eur']:.2f}€ "
                f"({depth['n_niveles']} niveles, ratio={depth['ratio_vs_stake']}x stake)")
        else:
            log(f"  📊 Libro {market_id}/{direction}: error consultando profundidad — {depth.get('error')}")

        order_args = MarketOrderArgsV2(
            token_id=token_id,
            amount=stake_eur,
            side="BUY",
            price=precio,
        )
        signed_order = client.create_market_order(order_args)
        resp = client.post_order(signed_order, OrderType.FOK)

        order_id = resp.get("orderID") or resp.get("id") or str(resp)
        filled_price = float(resp.get("price", precio))
        fee = float(resp.get("feeRateBps", 0)) / 10000 * stake_eur

        log(f"  ✅ Orden ejecutada: {direction} market={market_id} "
            f"stake={stake_eur:.2f}€ precio={filled_price:.4f} order_id={order_id}")
        return {
            "ok":          True,
            "order_id":    order_id,
            "entry_price": filled_price,
            "fee_eur":     fee,
            "error":       "",
        }
    except Exception as e:
        err_str = str(e)
        if "couldn't be fully filled" in err_str or "FOK" in err_str:
            log(f"  ⚠️  FOK kill (sin liquidez a ese precio) — no fill: {e}")
            return {
                "ok":       False,
                "no_fill":  True,
                "order_id": None,
                "entry_price": entry_price,
                "fee_eur":  0.0,
                "error":    err_str,
            }
        log(f"  ❌ Error ejecutando orden: {e}")
        return {
            "ok":          False,
            "no_fill":     False,
            "order_id":    None,
            "entry_price": entry_price,
            "fee_eur":     0.0,
            "error":       err_str,
        }


def _evaluar_pre_trade(pred: dict, decision: str) -> tuple[bool, str]:
    """
    Evaluador independiente pre-trade (generator/evaluator split — Loop Engineering).
    Actúa como skeptic: asume que la señal está mal hasta que se demuestre lo contrario.
    Rechaza si ≥2 señales independientes contradicen la predicción.
    Las señales individuales son ruidosas; se necesita consenso para rechazar.
    """
    flags = []

    try:
        feats = json.loads(pred.get("features", "{}") or "{}")
    except Exception:
        feats = {}

    # 1. Predicción vieja (>5 min) — el mercado pudo moverse desde que se generó
    try:
        pred_ts = datetime.fromisoformat(
            pred.get("timestamp_utc", "").replace("Z", "+00:00"))
        if pred_ts.tzinfo is None:
            pred_ts = pred_ts.replace(tzinfo=timezone.utc)
        age_min = (datetime.now(timezone.utc) - pred_ts).total_seconds() / 60
        if age_min > 5:
            flags.append(f"pred_vieja={age_min:.0f}min>5")
    except Exception:
        pass

    # 2. Edge en el momento de ejecutar demasiado pequeño (más estricto que el modelo)
    try:
        edge = float(pred.get("edge_neto", 0))
    except (ValueError, TypeError):
        edge = 0.0
    if abs(edge) < 0.025:
        flags.append(f"edge={edge:.4f}<0.025")

    # 3. Funding rate de perps contradice la dirección
    fr = feats.get("funding_rate_8h")  # % por 8h
    if fr is not None:
        if decision == "BUY_YES" and fr > 0.05:
            flags.append(f"funding={fr:+.3f}%/8h longs_sobrecargados vs BUY_YES")
        elif decision == "BUY_NO" and fr < -0.02:
            flags.append(f"funding={fr:+.3f}%/8h shorts_sobrecargados vs BUY_NO")

    # 4. Drift interno de Polymarket (poly_drift_5obs) contradice fuertemente
    poly_d = feats.get("poly_drift_5obs")
    if poly_d is not None and abs(poly_d) > 1.5:
        if decision == "BUY_YES" and poly_d < -1.5:
            flags.append(f"poly_drift={poly_d:+.2f}% vende_YES vs BUY_YES")
        elif decision == "BUY_NO" and poly_d > 1.5:
            flags.append(f"poly_drift={poly_d:+.2f}% compra_YES vs BUY_NO")

    if len(flags) >= 2:
        return False, f"{len(flags)} señales contrarias: " + " | ".join(flags)
    flag_str = f"({flags[0]})" if flags else "sin flags"
    return True, f"PASS {flag_str}"


def _registrar_trade(row: dict):
    nuevo = not TRADES_CSV.exists()
    with open(TRADES_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=TRADES_COLS)
        if nuevo:
            w.writeheader()
        w.writerow({col: row.get(col, "") for col in TRADES_COLS})


OVERRIDES_NOTIF_PATH = DIR_LIVE / "overrides_notificados.json"


def _avisar_override_superado(key: str, n_real: int, min_n_global: int):
    """Telegram una sola vez cuando el n direccional real de una key con
    min_n_overrides alcanza el umbral global — a partir de ahí el override
    ya no hace falta y se puede quitar de config_live.json."""
    try:
        notificados = json.loads(OVERRIDES_NOTIF_PATH.read_text()) if OVERRIDES_NOTIF_PATH.exists() else {}
    except Exception:
        notificados = {}
    if notificados.get(key):
        return
    enviar_telegram(
        f"✅ *Override de min_n ya no hace falta*\n"
        f"{key}\n"
        f"n real = {n_real} ≥ min_n_para_live ({min_n_global})\n"
        f"Puedes quitar la entrada de `min_n_overrides` en config_live.json."
    )
    log(f"  ℹ️  Override {key} superó min_n global ({n_real}≥{min_n_global}) — avisado por Telegram")
    notificados[key] = {"n_real": n_real, "ts": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    OVERRIDES_NOTIF_PATH.write_text(json.dumps(notificados, indent=2))


def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    log(f"=== live_trade ciclo {ts} ===")

    # 1. Guardián: ¿podemos operar ahora?
    puede, motivo = puede_operar_live()
    est = estado_live()
    log(f"  Switch: {'ON' if est['switch'] else 'OFF'} | "
        f"Ventana: {'SÍ' if est['en_ventana'] else 'NO'} ({motivo}) | "
        f"Hora Madrid: {est['hora_madrid']} ({est['dia']})")

    if not puede:
        log(f"  → Fuera de operación. Motivo: {motivo}")
        return

    # 2. Circuit breaker — verificar límites de pérdida antes de operar
    disparado, motivo_cb = verificar_circuit_breaker()
    desp  = stakes_desplegados_ventana_actual()
    pnl_d = pnl_live_hoy()
    log(f"  Circuit breaker: desplegado_ventana={desp:.2f}€  pnl_día={pnl_d:+.2f}€  → {'🛑 DISPARADO' if disparado else '✅ OK'}")

    if disparado:
        log(f"  🛑 CIRCUIT BREAKER: {motivo_cb}")
        enviar_telegram(
            f"🛑 *CIRCUIT BREAKER DISPARADO*\n"
            f"{motivo_cb}\n"
            f"Bankroll actual: {bankroll_actual():.2f}€\n"
            f"PNL hoy: {pnl_live_hoy():+.2f}€\n"
            f"Bot parado. Usa `/live_switch.sh on` para reactivar."
        )
        return

    # 3. Cargar predicciones y parámetros
    predicciones = _cargar_predicciones_hoy()
    params       = _cargar_params()
    config       = _cargar_config()
    riesgo       = config.get("riesgo", {})
    min_ic       = riesgo.get("min_ic_para_live", 0.08)
    min_n        = riesgo.get("min_n_para_live", 40)
    min_n_overrides = riesgo.get("min_n_overrides", {})
    estrategias_ok = config.get("estrategias_permitidas_live", [])
    subtypes_ok    = config.get("subtypes_permitidos_live", [])
    ya_operados  = _ya_operados_hoy()
    bkr          = bankroll_actual()

    log(f"  Predicciones hoy: {len(predicciones)} | Bankroll: {bkr:.2f}€ | Ya operados hoy: {len(ya_operados)}")

    ejecutados = 0
    for pred in predicciones:
        strategy = pred.get("strategy", "")
        subtype  = pred.get("subtype", "")
        mid      = pred.get("market_id", "")
        dec      = pred.get("decision", "")

        # Filtros de elegibilidad
        if strategy not in estrategias_ok:
            continue
        if subtypes_ok and subtype not in subtypes_ok:
            continue
        if mid in ya_operados:
            continue

        # Mercado ya cerrado → no operar (evita "invalid order version" de la API)
        try:
            end_str = pred.get("end_date", "")
            if end_str:
                end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
                if end_dt.tzinfo is None:
                    end_dt = end_dt.replace(tzinfo=timezone.utc)
                if end_dt <= datetime.now(timezone.utc):
                    continue
        except Exception:
            pass

        # IC mínimo confirmado en histórico (n_hist siempre corresponde a la
        # muestra real detrás de ic_hist, direccional o agregada). min_n_efectivo
        # permite un override puntual por strategy#subtype#decision (config_live.json)
        # cuando el n direccional está muy cerca del umbral global.
        override_key = f"{strategy}#{subtype}#{dec}"
        min_n_efectivo = min_n_overrides.get(override_key, min_n)
        try:
            feats_pred = json.loads(pred.get("features", "{}") or "{}")
        except Exception:
            feats_pred = {}
        ic_hist, n_hist = _ic_n_para_subtype(strategy, subtype, params, decision=dec,
                                              min_n=min_n_efectivo, min_ic=min_ic, features=feats_pred)
        if override_key in min_n_overrides and n_hist >= min_n:
            _avisar_override_superado(override_key, n_hist, min_n)
        if ic_hist < min_ic or n_hist < min_n_efectivo:
            continue

        # IC del modelo para esta señal concreta
        try:
            prob_y = float(pred.get("prob_yes_modelo", 0.5))
            precio = float(pred.get("precio_yes_mercado", 0.5))
            edge   = float(pred.get("edge_neto", 0))
        except ValueError:
            continue

        # Stake (con penalización de inventario direccional)
        stake_info = calcular_stake(ic_hist, strategy, subtype, direction=dec)
        if not stake_info["viable"]:
            log(f"  SKIP {strategy}#{subtype}: stake no viable — {stake_info['motivo']}")
            continue

        stake    = stake_info["stake_eur"]
        entry_p  = precio

        log(f"  SEÑAL → {strategy}#{subtype} {dec} "
            f"precio={entry_p:.4f} IC_hist={ic_hist:+.3f} n={n_hist} "
            f"stake={stake:.2f}€")
        log(f"         {stake_info['motivo']}")

        # Evaluador pre-trade independiente (generator/evaluator split)
        eval_ok, eval_motivo = _evaluar_pre_trade(pred, dec)
        log(f"  Evaluador: {eval_motivo}")
        if not eval_ok:
            log(f"  ⛔ EVALUADOR RECHAZA — no se ejecuta")
            enviar_telegram(
                f"⛔ *Señal rechazada por evaluador*\n"
                f"{strategy}#{subtype} {dec}\n"
                f"{eval_motivo}"
            )
            continue

        # 3. Notificar señal antes de ejecutar
        enviar_telegram(
            f"🎯 *Señal live detectada*\n"
            f"Estrategia: {strategy}#{subtype}\n"
            f"Dirección: {dec}\n"
            f"Precio entrada: {entry_p:.4f}\n"
            f"Stake: {stake:.2f}€  |  IC: {ic_hist:+.3f}\n"
            f"Bankroll: {bankroll_actual():.2f}€"
        )

        # 4. Ejecutar
        resultado = _ejecutar_orden_polymarket(mid, dec, stake, entry_p)

        # FOK kill = sin liquidez, no registrar ni contar
        if resultado.get("no_fill"):
            continue

        # 5. Registrar
        ts_now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        trade = {
            "timestamp_utc":   ts_now,
            "market_id":       mid,
            "question":        pred.get("question", ""),
            "end_date":        pred.get("end_date", ""),
            "strategy":        strategy,
            "subtype":         subtype,
            "direction":       dec,
            "stake_eur":       stake if resultado["ok"] else 0.0,
            "entry_price":     resultado["entry_price"],
            "ic_modelo":       round(prob_y, 4),
            "edge_neto":       round(edge, 4),
            "conviction_score": round(ic_hist, 4),
            "kelly_recomendado": stake,
            "status":          "OPEN" if resultado["ok"] else "ERROR",
            "close_timestamp": "",
            "exit_price":      "",
            "outcome_real":    "",
            "fee_eur":         resultado.get("fee_eur", 0),
            "pnl_bruto_eur":   "",
            "pnl_neto_eur":    "",
            "notas":           resultado.get("error", ""),
        }
        _registrar_trade(trade)
        ya_operados.add(mid)
        ejecutados += 1

        # No más de 3 operaciones por ciclo (espacio entre señales)
        if ejecutados >= 3:
            log(f"  Límite de 3 operaciones por ciclo alcanzado.")
            break

    log(f"  Operaciones ejecutadas este ciclo: {ejecutados}")

    # Resumen de ventana si hubo actividad
    if ejecutados > 0:
        bkr_final = bankroll_actual()
        pnl_d     = pnl_live_hoy()
        enviar_telegram(
            f"📊 *Ciclo live completado*\n"
            f"Operaciones este ciclo: {ejecutados}\n"
            f"PNL hoy: {pnl_d:+.2f}€\n"
            f"Bankroll actual: {bkr_final:.2f}€"
        )

    log(f"=== Fin live_trade ===")


if __name__ == "__main__":
    main()
