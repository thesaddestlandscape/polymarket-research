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
from datetime import datetime, timezone
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
ORDEN_EN_CURSO_PATH = DIR_LIVE / "orden_en_curso.json"


def _marcar_orden_en_curso(market_id: str, direction: str):
    """Marca que hay una orden real en vuelo hacia el CLOB. watchdog_fast.sh
    la comprueba antes de matar la screen 'fast' para no interrumpir un
    envío ya hecho al exchange justo antes de registrarlo en trades.csv."""
    try:
        ORDEN_EN_CURSO_PATH.write_text(json.dumps({
            "market_id": market_id, "direction": direction,
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }), encoding="utf-8")
    except Exception:
        pass


def _limpiar_orden_en_curso():
    try:
        ORDEN_EN_CURSO_PATH.unlink(missing_ok=True)
    except Exception:
        pass

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
    """Set de todos los market_id que ya tienen trade OPEN o CLOSED (cada
    market_id es una ventana concreta e irrepetible, nunca reaparece en un
    día distinto, así que no hace falta ni conviene acotar por fecha).
    Antes se filtraba comparando una fecha Madrid (UTC+offset) contra
    timestamp_utc crudo (UTC) — durante 23:00-24:00 UTC (=01:00-02:00 Madrid,
    justo la ventana de prueba activa) la fecha Madrid ya era "mañana" y
    ningún trade de esa ventana entraba en `vistos`, permitiendo re-operar
    el mismo mercado varias veces con dinero real."""
    if not TRADES_CSV.exists():
        return set()
    vistos = set()
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            vistos.add(row.get("market_id", ""))
    return vistos


def _posiciones_abiertas_misma_direccion(direction: str) -> int:
    """Nº de trades con status OPEN ahora mismo en la misma dirección.

    Límite de correlación (2026-07-03): BTC/ETH/SOL/XRP se mueven casi al
    unísono intradía, así que N posiciones misma-dirección abiertas a la vez
    son en la práctica UNA apuesta con stake ×N, no N apuestas — el cluster
    shadow de 2026-07-02 01h UTC perdió -24.4€ en 17 BUY_NO simultáneos
    multi-par cuando todo subió a la vez. La penalización de inventario de
    live_stake reduce el stake pero no acota el nº de posiciones; este techo
    duro sí. Código de seguridad live — no minimizar."""
    if not TRADES_CSV.exists():
        return 0
    n = 0
    with open(TRADES_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            # OPEN y STUB cuentan como posición viva — mismo criterio que
            # live_stake.py (stakes_desplegados_ventana_actual e
            # inventario_direccional_hoy); solo OPEN dejaba colarse trades
            # STUB por el techo.
            if (row.get("status") in ("OPEN", "STUB")
                    and row.get("direction") == direction):
                n += 1
    return n


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
    evaluar condiciones de patrones_ganadores/filtros_causales. Estricto en
    los 4 casos (ver comentario en shadow_predict.py: coincide con el límite
    "malo" de _evaluar_bucket, antes abs_lt/lt colaban el umbral de más)."""
    try:
        v, u = float(feat_val), float(umbral)
        if cond == "abs_gt": return abs(v) > u
        if cond == "abs_lt": return abs(v) < u
        if cond == "gt":     return v > u
        if cond == "lt":     return v < u
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

    # No alcanza min_n+min_ic por la vía normal — probar patrón causal confirmado.
    # Veto previo: si el subtype EXACTO ya tiene evidencia direccional propia
    # NEGATIVA (o agregada negativa si no hay direccional), ningún patrón de una
    # clave más genérica puede rehabilitarlo para live — un patrón de
    # UPDOWN_GBM#15min (aprendido sobre todo en ETH/XRP) validó en vivo un
    # SOL#15min BUY_NO cuyo ic_BUY_NO propio era -0.025 (trade real perdido
    # 2026-07-02 19:26 UTC, -2.00€). El patrón sigue valiendo para subtypes
    # sin historial propio o con historial propio ≥0 pero insuficiente.
    # Código de seguridad live — no minimizar.
    if features:
        p_exacto = params.get(claves[0], {})
        ic_propio = p_exacto.get(f"ic_{decision}") if decision else None
        if ic_propio is None:
            ic_propio = p_exacto.get("ic_bayes")
        if ic_propio is not None and float(ic_propio) < 0:
            return ic_normal, n_normal

        mejor_patron = None
        for k in claves:
            for patron in params.get(k, {}).get("patrones_ganadores", []):
                if patron.get("direccion") not in (None, decision):
                    continue
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


_clob_redondeo_parcheado = False


def _parchear_redondeo_clob():
    """Sustituye los helpers de redondeo de py_clob_client_v2 por versiones
    exactas basadas en Decimal. Los originales operan en float puro
    (floor(x * 10**n) / 10**n), y para ciertas combinaciones stake/precio el
    residuo binario deja maker/taker amounts con más decimales de los que el
    CLOB admite → rechazo "invalid amounts" (2 señales reales perdidas:
    2026-06-30 y 2026-07-02 19:22 UTC). Esta es la causa raíz; el reintento
    con stake±0.01€ de _ejecutar_orden_polymarket se mantiene como red de
    seguridad. Se parchean tanto helpers como builder (importa por nombre).

    Causa raíz principal encontrada 2026-07-03: los mercados cripto up/down
    usan tick 0.001 (precios de 3 decimales, ej. 0.485), y para ese tick la
    librería redondea el taker amount a 5 decimales (RoundConfig(amount=5)),
    pero el CLOB solo admite 4 en market orders ("taker amount a max of 4
    decimals") → la orden falla exactamente cuando el 5º decimal del cociente
    maker/precio no es cero, de ahí la intermitencia. Se sustituye también
    get_market_order_amounts por una versión que respeta los límites reales
    del CLOB para market orders: maker (USDC) ≤2 decimales, taker (shares) ≤4.
    Código de seguridad live — no minimizar."""
    global _clob_redondeo_parcheado
    if _clob_redondeo_parcheado:
        return
    from decimal import Decimal, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_UP
    from py_clob_client_v2.order_builder import builder as _b, helpers as _h
    from py_clob_client_v2.order_utils import Side as _Side

    def _q(sig_digits: int) -> Decimal:
        return Decimal(1).scaleb(-sig_digits)

    def round_down(x: float, sig_digits: int) -> float:
        return float(Decimal(str(x)).quantize(_q(sig_digits), rounding=ROUND_FLOOR))

    def round_up(x: float, sig_digits: int) -> float:
        return float(Decimal(str(x)).quantize(_q(sig_digits), rounding=ROUND_CEILING))

    def round_normal(x: float, sig_digits: int) -> float:
        return float(Decimal(str(x)).quantize(_q(sig_digits), rounding=ROUND_HALF_UP))

    def to_token_decimals(x: float) -> int:
        return int((Decimal(str(x)) * 10**6).quantize(Decimal(1), rounding=ROUND_HALF_UP))

    for mod in (_h, _b):
        mod.round_down = round_down
        mod.round_up = round_up
        mod.round_normal = round_normal
        mod.to_token_decimals = to_token_decimals

    MAX_DEC_TAKER_MARKET = 4  # límite del CLOB para market orders, no depende del tick

    def get_market_order_amounts(self, side, amount, price, round_config):
        if isinstance(side, _Side):
            side = _b.BUY if side == _Side.BUY else _b.SELL
        raw_price = round_down(price, round_config.price)
        max_dec = min(round_config.amount, MAX_DEC_TAKER_MARKET)
        if side == _b.BUY:
            # maker = USDC gastado (≤2 dec), taker = shares recibidas (≤4 dec).
            # Shares hacia abajo: nunca pedir más de lo que el dinero compra.
            raw_maker = round_down(amount, round_config.size)
            raw_taker = round_down(raw_maker / raw_price, max_dec)
            return _Side.BUY, to_token_decimals(raw_maker), to_token_decimals(raw_taker)
        elif side == _b.SELL:
            raw_maker = round_down(amount, round_config.size)
            raw_taker = round_down(raw_maker * raw_price, max_dec)
            return _Side.SELL, to_token_decimals(raw_maker), to_token_decimals(raw_taker)
        raise ValueError(f"order_args.side must be '{_b.BUY}' or '{_b.SELL}'")

    _b.OrderBuilder.get_market_order_amounts = get_market_order_amounts
    _clob_redondeo_parcheado = True


def _get_clob_client():
    """Crea cliente CLOB V2 autenticado desde .env."""
    from dotenv import load_dotenv
    from py_clob_client_v2 import ClobClient, ApiCreds
    from py_clob_client_v2.constants import POLYGON
    _parchear_redondeo_clob()
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
    """Devuelve (yes_token_id, no_token_id) desde Gamma API.

    Valida el orden real contra `outcomes` en vez de asumir ciegamente
    clobTokenIds[0]=YES/UP — si algún mercado trajera el orden invertido,
    asumirlo a ciegas compraría el token contrario con dinero real sin
    ningún aviso. Si `outcomes` no trae las etiquetas esperadas, falla
    fuerte (se captura arriba en _ejecutar_orden_polymarket) en vez de
    arriesgar una dirección adivinada."""
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

    raw_outcomes = data.get("outcomes", [])
    outcomes = json.loads(raw_outcomes) if isinstance(raw_outcomes, str) else raw_outcomes
    if len(outcomes) < 2:
        raise ValueError(f"outcomes incompleto para market {market_id}: {outcomes}")

    AFIRMATIVOS = {"yes", "up"}
    NEGATIVOS   = {"no", "down"}
    o0 = str(outcomes[0]).strip().lower()
    o1 = str(outcomes[1]).strip().lower()
    if o0 in AFIRMATIVOS and o1 in NEGATIVOS:
        return tokens[0], tokens[1]
    if o0 in NEGATIVOS and o1 in AFIRMATIVOS:
        return tokens[1], tokens[0]
    raise ValueError(
        f"outcomes inesperados para market {market_id}: {outcomes} — "
        f"no se puede mapear YES/NO con seguridad"
    )


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


REQUOTE_EDGE_MIN  = 0.02   # mismo listón que EDGE_MINIMO de shadow_predict
REQUOTE_PRECIO_MAX = 0.95  # nunca pagar más de esto por el token, pase lo que pase
MIN_ORDEN_CLOB_USD = 1.00  # el CLOB rechaza marketable BUY < $1 ("min size: 1")
REQUOTE_DIVERGENCIA_MAX = 0.10  # |ask - plan| máx; más allá el modelo está desfasado


def _decidir_requote(edge_dir: float, precio_plan: float,
                     mejor_ask: float | None) -> tuple[float, float, bool, str]:
    """Re-cotización en el momento de ejecutar (fix 2026-07-03).

    Antes la orden FOK salía al precio de la PREDICCIÓN (minutos de
    antigüedad): si el mercado había mejorado, el FOK moría ("couldn't be
    fully filled", 3 kills seguidos 2026-07-02 19:25) y perdíamos la entrada
    buena; si había empeorado, nos llenaban igual — selección adversa pura:
    solo ejecutábamos cuando el libro venía en contra.

    Con el mejor ask actual del libro:
      - deterioro = mejor_ask - precio_plan (>0 → pagamos más que al señalar)
      - el edge restante se recorta por el deterioro; la mejora NO infla el
        edge estimado (conservador)
      - si el edge restante < REQUOTE_EDGE_MIN → no operar (la señal caducó)
      - si sigue vivo → ejecutar al precio REAL del libro (el FOK casa)

    Devuelve (precio_final, edge_restante, operar, motivo).
    Sin libro (mejor_ask None) se mantiene el comportamiento anterior:
    precio de la predicción, edge tal cual. Código de seguridad live — no
    minimizar."""
    if mejor_ask is None:
        return precio_plan, edge_dir, True, "sin libro — precio de predicción"
    if mejor_ask > REQUOTE_PRECIO_MAX:
        return mejor_ask, 0.0, False, (
            f"mejor_ask={mejor_ask:.4f} > tope {REQUOTE_PRECIO_MAX}")
    deterioro = round(mejor_ask - precio_plan, 4)
    # Divergencia extrema plan↔libro = el mercado sabe algo que el snapshot
    # del modelo no vio (spot movido tras la señal). Un ask MUY por debajo
    # del plan no es regalo: 2026-07-03 08:49 XRP#15min BUY_YES señal a
    # 0.475 (modelo 0.62), libro a 0.12, fill 0.04 → resolvió NO, -1.63€.
    # El mercado a 11min del cierre tenía razón. El lado deterioro>0 ya lo
    # corta el chequeo de edge; este guard corta el lado "mejora" que antes
    # se celebraba. Código de seguridad live — no minimizar.
    if abs(deterioro) > REQUOTE_DIVERGENCIA_MAX:
        return mejor_ask, 0.0, False, (
            f"divergencia plan↔libro {deterioro:+.4f} > {REQUOTE_DIVERGENCIA_MAX} "
            f"(plan {precio_plan:.4f}, ask {mejor_ask:.4f}) — modelo desfasado, no operar")
    edge_ahora = round(edge_dir - max(0.0, deterioro), 4)
    if edge_ahora < REQUOTE_EDGE_MIN:
        return mejor_ask, edge_ahora, False, (
            f"edge evaporado: {edge_dir:+.4f} → {edge_ahora:+.4f} "
            f"(ask {precio_plan:.4f}→{mejor_ask:.4f}) < {REQUOTE_EDGE_MIN}")
    if deterioro > 0:
        motivo = f"deterioro {deterioro:+.4f} pero edge vivo ({edge_ahora:+.4f})"
    elif deterioro < 0:
        motivo = f"precio mejoró {deterioro:+.4f} — antes el FOK moría aquí"
    else:
        motivo = "precio sin cambios"
    return mejor_ask, edge_ahora, True, motivo


def _ejecutar_orden_polymarket(market_id: str, direction: str,
                               stake_eur: float, entry_price: float,
                               edge_dir: float | None = None) -> dict:
    """Ejecuta orden real en Polymarket via CLOB API.

    edge_dir: edge neto A FAVOR de nuestra dirección (edge_neto de la
    predicción con el signo ya resuelto: +edge para BUY_YES, -edge para
    BUY_NO). Si se pasa, se re-cotiza contra el libro actual antes de
    ejecutar (ver _decidir_requote)."""
    try:
        from py_clob_client_v2 import MarketOrderArgsV2, OrderType
        yes_token, no_token = _get_token_ids(market_id)
        if direction == "BUY_YES":
            token_id = yes_token
            precio   = entry_price
        else:  # BUY_NO
            token_id = no_token
            precio   = round(1.0 - entry_price, 6)
        precio_plan = precio   # precio del token en el momento de la señal

        client = _get_clob_client()

        depth = _consultar_profundidad_libro(client, token_id, precio, stake_eur)
        if depth.get("ok"):
            log(f"  📊 Libro {market_id}/{direction}: mejor_ask={depth['mejor_ask']} "
                f"profundidad≈{depth['profundidad_eur']:.2f}€ "
                f"({depth['n_niveles']} niveles, ratio={depth['ratio_vs_stake']}x stake)")
        else:
            log(f"  📊 Libro {market_id}/{direction}: error consultando profundidad — {depth.get('error')}")

        # Veto por profundidad: 2026-07-03 XRP/SOL#15min ejecutaron contra
        # libros con profundidad 0.00€ (ratio=0.0x, ask oscilando 0.52↔0.75
        # en segundos) y el slippage real (+0.04/+0.085) se comió el edge:
        # -3.19€. El re-quote solo mira el mejor ask de UN snapshot — en un
        # libro vacío ese snapshot es ruido. Fail-closed: si la consulta del
        # libro falla tampoco se ejecuta (sin libro no hay re-quote fiable).
        # Código de seguridad live — no minimizar.
        min_ratio = _cargar_config().get("riesgo", {}).get("min_profundidad_ratio_libro", 5.0)
        if not depth.get("ok"):
            log(f"  ⛔ Sin datos de libro — no se ejecuta (fail-closed)")
            return {
                "ok": False, "no_fill": True, "libro_sin_datos": True,
                "order_id": None, "entry_price": entry_price,
                "fee_eur": 0.0, "error": f"profundidad no consultable: {depth.get('error')}",
            }
        ratio = depth.get("ratio_vs_stake")
        if ratio is None or ratio < min_ratio:
            log(f"  ⛔ Libro sin profundidad: ratio={ratio}x < {min_ratio}x stake — no se ejecuta")
            return {
                "ok": False, "no_fill": True, "libro_vacio": True,
                "order_id": None, "entry_price": entry_price,
                "fee_eur": 0.0, "error": f"profundidad insuficiente: ratio={ratio}x < {min_ratio}x",
            }

        # Re-cotización con el libro actual (solo si el caller pasó edge_dir)
        if edge_dir is not None:
            mejor_ask = depth.get("mejor_ask") if depth.get("ok") else None
            mejor_ask = float(mejor_ask) if mejor_ask is not None else None
            precio, edge_vivo, operar, motivo_rq = _decidir_requote(
                edge_dir, precio_plan, mejor_ask)
            log(f"  🔁 Re-quote: {motivo_rq}")
            if not operar:
                return {
                    "ok": False, "no_fill": True, "edge_evaporado": True,
                    "order_id": None, "entry_price": entry_price,
                    "fee_eur": 0.0, "error": f"requote: {motivo_rq}",
                }

        _marcar_orden_en_curso(market_id, direction)
        try:
            # py_clob_client_v2 calcula makerAmount/takerAmount dividiendo
            # amount/price en float puro y redondeando después — para ciertas
            # combinaciones concretas el resultado conserva más decimales de
            # los que el tick del mercado permite y el CLOB rechaza la orden
            # con "invalid amounts" (confirmado en real 2026-07-01, stake=0€
            # perdido = ningún dinero en riesgo, solo la señal). Es un bug de
            # precisión de coma flotante en la librería (order_builder/
            # builder.py::get_market_order_amounts, no en nuestro código), no
            # reproducible de forma determinista sin acceso al validador del
            # CLOB. Mitigación: un reintento con el stake desplazado 1
            # céntimo cambia el resultado de la división y en la práctica
            # evita la misma colisión — ningún intento previo llega a
            # ejecutarse de verdad (el rechazo es previo al match), así que
            # reintentar no puede duplicar la operación.
            _max_stake = _cargar_config().get("riesgo", {}).get("max_stake_eur", 2.00)
            intentos_stake = [stake_eur, round(stake_eur - 0.01, 2)]
            _mas = round(stake_eur + 0.01, 2)
            if _mas <= _max_stake:
                intentos_stake.append(_mas)
            # El CLOB exige ≥$1 en órdenes marketable BUY ("min size: 1") —
            # 2026-07-03: 2 señales rechazadas con stake 0.94/0.98€. El suelo
            # min_stake_eur=1.05 del config debería impedir llegar aquí con
            # menos; este filtro es la red fail-closed si alguna ruta lo salta.
            intentos_stake = [a for a in intentos_stake if a >= MIN_ORDEN_CLOB_USD]
            if not intentos_stake:
                log(f"  ⛔ Stake {stake_eur:.2f}€ < mínimo CLOB ${MIN_ORDEN_CLOB_USD:.2f} — no se ejecuta")
                return {
                    "ok": False, "no_fill": True, "stake_bajo_minimo": True,
                    "order_id": None, "entry_price": entry_price,
                    "fee_eur": 0.0,
                    "error": f"stake {stake_eur:.2f} < mínimo CLOB {MIN_ORDEN_CLOB_USD}",
                }
            resp = None
            for intento, amt in enumerate(intentos_stake):
                if amt <= 0:
                    continue
                order_args = MarketOrderArgsV2(
                    token_id=token_id,
                    amount=amt,
                    side="BUY",
                    price=precio,
                )
                try:
                    signed_order = client.create_market_order(order_args)
                    resp = client.post_order(signed_order, OrderType.FOK)
                    stake_eur = amt
                    if intento > 0:
                        log(f"  ⚠️  Orden aceptada en reintento {intento} con stake={amt:.2f}€ "
                            f"(precisión decimal, ver comentario en código)")
                    break
                except Exception as e_intento:
                    if "invalid amounts" not in str(e_intento) or intento == len(intentos_stake) - 1:
                        raise
                    log(f"  ⚠️  'invalid amounts' con stake={amt:.2f}€, reintentando con otro monto...")
            if resp is None:
                raise RuntimeError("no se pudo construir una orden con amounts válidos")
        finally:
            _limpiar_orden_en_curso()

        order_id = resp.get("orderID") or resp.get("id") or str(resp)
        filled_price = float(resp.get("price", precio))
        fee = float(resp.get("feeRateBps", 0)) / 10000 * stake_eur

        # Slippage real señal→fill (en el token comprado). Se acumula en
        # `notas` para calibrar SLIPPAGE_ESTIMADO (hoy constante 0.02) con
        # datos reales cuando haya n≥30 fills.
        slip_real = round(filled_price - precio_plan, 4)

        log(f"  ✅ Orden ejecutada: {direction} market={market_id} "
            f"stake={stake_eur:.2f}€ precio={filled_price:.4f} "
            f"slip={slip_real:+.4f} order_id={order_id}")
        return {
            "ok":          True,
            "order_id":    order_id,
            "entry_price": filled_price,
            "fee_eur":     fee,
            "slip_real":   slip_real,
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
    min_n_overrides   = riesgo.get("min_n_overrides", {})
    min_ic_asimetrico = riesgo.get("min_ic_asimetrico", {})
    # Whitelist por tupla exacta STRATEGY#SUBTYPE#DIRECTION. Antes eran dos
    # listas independientes (estrategias × subtypes) y el producto cartesiano
    # dejaba pasar combinaciones nunca aprobadas: UPDOWN_GBM#SOL#15min
    # (02-Jul, -2.00€ real) y UPDOWN_GBM#BTC#15min (03-Jul, -2.00€ real).
    # Fail-closed: lista vacía o ausente → no se opera nada. Código de
    # seguridad live — no minimizar.
    pares_ok = set(config.get("pares_permitidos_live", []))
    if not pares_ok:
        log("  ⚠️ pares_permitidos_live vacío o ausente en config — no se opera (fail-closed)")
    ya_operados  = _ya_operados_hoy()
    bkr          = bankroll_actual()

    log(f"  Predicciones hoy: {len(predicciones)} | Bankroll: {bkr:.2f}€ | Ya operados hoy: {len(ya_operados)}")

    ejecutados = 0
    for pred in predicciones:
        strategy = pred.get("strategy", "")
        subtype  = pred.get("subtype", "")
        mid      = pred.get("market_id", "")
        dec      = pred.get("decision", "")

        # Filtros de elegibilidad — tupla exacta aprobada para live
        if f"{strategy}#{subtype}#{dec}" not in pares_ok:
            continue
        if mid in ya_operados:
            continue

        # Mercado ya cerrado → no operar (evita "invalid order version" de la API).
        # Fail-closed: end_date vacío o sin parsear NO debe dejar pasar el
        # trade sin validar — código de seguridad live, no se minimiza (ver
        # CLAUDE.md). No observado en producción (0/117 predicciones de hoy
        # con end_date vacío) pero es el comportamiento correcto si pasa.
        end_str = pred.get("end_date", "")
        try:
            if not end_str:
                continue
            end_dt = datetime.fromisoformat(end_str.replace("Z", "+00:00"))
            if end_dt.tzinfo is None:
                end_dt = end_dt.replace(tzinfo=timezone.utc)
            if end_dt <= datetime.now(timezone.utc):
                continue
        except Exception:
            continue

        # IC mínimo confirmado en histórico (n_hist siempre corresponde a la
        # muestra real detrás de ic_hist, direccional o agregada), umbral global.
        # Barra asimétrica: strategy#decision con evidencia estructural de que
        # esa dirección rinde peor (ver H-CUSTOM-GBM-BUYYES-GLOBAL-MALO,
        # confirmada 2026-07-01, n=507 IC=-0.076) exige un min_ic más alto que
        # el global, en vez del mismo umbral para las dos direcciones.
        min_ic_efectivo = min_ic_asimetrico.get(f"{strategy}#{dec}", min_ic)
        try:
            feats_pred = json.loads(pred.get("features", "{}") or "{}")
        except Exception:
            feats_pred = {}
        ic_hist, n_hist = _ic_n_para_subtype(strategy, subtype, params, decision=dec,
                                              min_n=min_n, min_ic=min_ic_efectivo, features=feats_pred)
        pasa = not (ic_hist < min_ic_efectivo or n_hist < min_n)

        # Override puntual por strategy#subtype#decision (config_live.json):
        # solo mira el n/ic direccional de ESA clave exacta, nunca una clave
        # más amplia de la jerarquía de fallback — antes el min_n rebajado se
        # colaba dentro de _ic_n_para_subtype y podía validar la señal contra
        # el ic_bayes/n agregado de toda la estrategia (una muestra mucho más
        # amplia y potencialmente más débil que la que motivó el override).
        override_key = f"{strategy}#{subtype}#{dec}"
        if not pasa and override_key in min_n_overrides:
            min_n_override = min_n_overrides[override_key]
            exact_key = f"{strategy}#{subtype}" if subtype else strategy
            p_exact = params.get(exact_key, {})
            campo_ic = f"ic_{dec}"
            campo_n  = f"n_{dec}"
            ic_exacto = p_exact.get(campo_ic)
            n_exacto  = p_exact.get(campo_n, 0)
            if ic_exacto is not None and n_exacto >= min_n_override and float(ic_exacto) >= min_ic_efectivo:
                ic_hist, n_hist = float(ic_exacto), n_exacto
                pasa = True
                if n_hist >= min_n:
                    _avisar_override_superado(override_key, n_hist, min_n)
        if not pasa:
            continue

        # IC del modelo para esta señal concreta
        try:
            prob_y = float(pred.get("prob_yes_modelo", 0.5))
            precio = float(pred.get("precio_yes_mercado", 0.5))
            edge   = float(pred.get("edge_neto", 0))
        except ValueError:
            continue

        # Stake (con penalización de inventario direccional)
        # Techo de correlación direccional: los pares cripto se mueven casi
        # al unísono — más de N posiciones abiertas en la misma dirección es
        # una sola apuesta con stake multiplicado (ver
        # _posiciones_abiertas_misma_direccion).
        max_misma_dir = riesgo.get("max_posiciones_abiertas_misma_direccion", 2)
        abiertas_dir = _posiciones_abiertas_misma_direccion(dec)
        if abiertas_dir >= max_misma_dir:
            log(f"  SKIP {strategy}#{subtype} {dec}: ya hay {abiertas_dir} "
                f"posiciones abiertas {dec} (techo correlación = {max_misma_dir})")
            continue

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
            # Solo log, no Telegram: la señal rechazada no se registra, así
            # que se re-evalúa (y se re-rechazaría) cada ciclo ~20s mientras
            # la predicción siga viva — un Telegram aquí es un mensaje por
            # ciclo. Misma clase de spam que la notificación pre-ejecución
            # eliminada 2026-07-03.
            log(f"  ⛔ EVALUADOR RECHAZA — no se ejecuta")
            continue

        # 3+4. Ejecutar y notificar DESPUÉS con el resultado real.
        # Antes el Telegram "señal detectada" salía antes de ejecutar: una
        # señal con no_fill (FOK kill, o edge evaporado en re-quote) no se
        # registra y se reintenta cada ciclo (~20s) mientras la predicción
        # siga viva → un mensaje por ciclo (ocurrió 2026-07-02 19:25, 3
        # mensajes en 90s; el re-quote lo habría amplificado). Los reintentos
        # silenciosos quedan en live.log; Telegram solo recibe fills y
        # errores reales, una vez, porque ambos se registran en trades.csv y
        # el mercado entra en ya_operados.
        # edge_dir = edge_neto con el signo resuelto hacia
        # nuestra dirección (shadow_predict: en>=min → BUY_YES, -en>=min →
        # BUY_NO), para que _decidir_requote pueda recortar por deterioro.
        edge_dir = edge if dec == "BUY_YES" else -edge
        resultado = _ejecutar_orden_polymarket(mid, dec, stake, entry_p,
                                               edge_dir=edge_dir)

        # FOK kill o edge evaporado en re-quote = no registrar ni contar;
        # la señal puede reintentarse en ciclos siguientes si sigue viva.
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
            "notas":           (f"slip_real={resultado['slip_real']:+.4f}"
                                if resultado.get("ok") and "slip_real" in resultado
                                else resultado.get("error", "")),
        }
        _registrar_trade(trade)
        ya_operados.add(mid)
        ejecutados += 1

        if resultado["ok"]:
            enviar_telegram(
                f"🎯 *Orden live ejecutada*\n"
                f"Estrategia: {strategy}#{subtype}\n"
                f"Dirección: {dec}\n"
                f"Precio fill: {resultado['entry_price']:.4f} "
                f"(slip {resultado.get('slip_real', 0):+.4f})\n"
                f"Stake: {stake:.2f}€  |  IC: {ic_hist:+.3f}\n"
                f"Bankroll: {bankroll_actual():.2f}€"
            )
        else:
            enviar_telegram(
                f"❌ *Orden live ERROR*\n"
                f"{strategy}#{subtype} {dec}\n"
                f"{resultado.get('error', '')[:200]}"
            )

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
