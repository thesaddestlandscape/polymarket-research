"""vendor_main.py -- GENERADO por regenerar_vendor.py (NO editar a mano: cambia el sha y el paquete se niega a cargarlo). MINIMO que necesita vendor/envio_real.py.
  hash_orden                                       VERBATIM de sonda1/vendor_main.py        (segmento y sha en VENDOR_HASHES.json)
  _clob_redondeo_parcheado, _parchear_redondeo_clob  VERBATIM (texto) de live_trade.py        (codigo de seguridad live; el modulo live_trade NUNCA se importa)
  cliente_dedicado, saldo_onchain                  escritos para el paquete (abajo): sin live_trade, sin polygon_rpc, sin REPO ni variables de entorno; los .env de produccion se abren SOLO para comparar y negarse (hallazgo 8).
"""
import dataclasses, json, os, stat, sys, time

ENV_DEDICADA = "/root/.secrets/experimento_pares.env"        # ruta FIJA: no sale del entorno ni de argumentos de linea de comandos
WALLET_DEDICADA = "0x659a40FF9920fEBc5a66836213040924343d297F"
ENVS_PRODUCCION = ("/root/polymarket-research/data/live/.env", "/root/polymarket-research/.env")     # SOLO comparacion (hallazgo 8); el 1o obligatorio
CLOB = "https://clob.polymarket.com"
PUSD = "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB"          # colateral (de sonda1/vendor_main.py)
RPCS = ("https://polygon-bor-rpc.publicnode.com", "https://polygon.drpc.org", "https://1rpc.io/matic")     # grupo 'latest' de polygon_rpc (12-Nov); lista FIJA, no se lee ningun JSON
RPC_MIN_VALIDAS = 2                                          # v7 (hallazgo 9): respuestas validas MINIMAS para dar un saldo (se toma el minimo); con menos => None


def hash_orden(signed, neg_risk=False):
    """orderID = hash EIP-712 de la orden V2 (sin la firma). La fase 0 verifica que coincide con el del servidor."""
    from py_clob_client_v2.config import get_contract_config
    from py_clob_client_v2.order_utils.exchange_order_builder_v2 import ExchangeOrderBuilderV2
    from py_clob_client_v2.order_utils.model.order_data_v2 import OrderV2
    cfg = get_contract_config(137)
    ex = cfg.neg_risk_exchange_v2 if neg_risk else cfg.exchange_v2
    b = ExchangeOrderBuilderV2(ex, 137, None)
    campos = {k: v for k, v in dataclasses.asdict(signed).items() if k != "signature"}
    return b.build_order_hash(b.build_order_typed_data(OrderV2(**campos)))


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


def cliente_dedicado(ruta=ENV_DEDICADA, wallet_esperada=WALLET_DEDICADA, _clob=None, _prod=ENVS_PRODUCCION):
    """Cliente CLOB V2 de la wallet DEDICADA (POLY_1271, funder = wallet de deposito). Fail-closed (sys.exit) si: la ruta (tras resolver symlinks) es una de produccion; el fichero no es regular o es legible por
    grupo/otros; faltan credenciales; la wallet de deposito NO es EXACTAMENTE la autorizada; o CUALQUIERA de POLY_PRIVATE_KEY / POLY_API_KEY / POLY_DEPOSIT_WALLET coincide con las de produccion.
    DECISION (2o /code-review, hallazgo 8; restaura la guarda de la Sonda1): los .env de produccion (`_prod`) se ABREN SOLO para COMPARAR y negarse a arrancar; sus valores jamas se usan ni se guardan ni se escriben. `data/live/.env` es
    OBLIGATORIO y legible (si no se puede comprobar => no arranco, como la Sonda1); el `.env` principal se compara ademas si existe. No importa live_trade: la unica clave que entra en el cliente es la de `ruta`.
    (`ruta`/`wallet_esperada`/`_clob`/`_prod` existen para los tests; el paquete llama sin argumentos.)"""
    from dotenv import dotenv_values
    ruta = str(ruta); norm = lambda x: str(x or "").strip().lower().removeprefix("0x")
    real = os.path.realpath(ruta); prod_reales = [os.path.realpath(p) for p in _prod]
    if real in prod_reales or os.path.basename(real) == ".env" or "data/live" in real:
        sys.exit(f"{ruta} (-> {real}) es/parece la credencial de produccion: no arranco")
    try:
        st = os.stat(real)
    except OSError as e:
        sys.exit(f"{ruta}: no se puede leer ({type(e).__name__}): no arranco")
    if not stat.S_ISREG(st.st_mode) or st.st_mode & 0o077:
        sys.exit(f"{ruta}: debe ser un fichero regular con permisos 600 (modo {oct(st.st_mode & 0o7777)}): no arranco")
    c = dotenv_values(real)
    faltan = [k for k in ("POLY_PRIVATE_KEY", "POLY_DEPOSIT_WALLET", "POLY_API_KEY", "POLY_API_SECRET", "POLY_API_PASSPHRASE") if not c.get(k)]
    if faltan:
        sys.exit(f"{ruta}: faltan {faltan}")
    if norm(c["POLY_DEPOSIT_WALLET"]) != norm(wallet_esperada):
        sys.exit("la wallet de deposito del fichero NO es la wallet dedicada autorizada: no arranco")
    for i, pp in enumerate(_prod):                                  # el primero es OBLIGATORIO; los demas solo si existen
        if i > 0 and not os.path.exists(pp):
            continue
        live = dotenv_values(pp) if os.path.exists(pp) else {}
        if not live.get("POLY_DEPOSIT_WALLET") or not live.get("POLY_API_KEY") or not live.get("POLY_PRIVATE_KEY"):
            sys.exit(f"no se puede comprobar que la wallet dedicada no sea la de produccion ({pp} ilegible o incompleto): no arranco")
        if any(norm(c[k]) == norm(live[k]) for k in ("POLY_DEPOSIT_WALLET", "POLY_API_KEY", "POLY_PRIVATE_KEY")):
            sys.exit(f"{ruta} comparte credenciales con {pp}: no arranco")
    _parchear_redondeo_clob()
    if _clob is None:
        from py_clob_client_v2 import ClobClient
        _clob = ClobClient
    from py_clob_client_v2 import ApiCreds
    from py_clob_client_v2.constants import POLYGON
    pk = c["POLY_PRIVATE_KEY"] if c["POLY_PRIVATE_KEY"].lower().startswith("0x") else "0x" + c["POLY_PRIVATE_KEY"]
    return _clob(CLOB, key=pk, chain_id=POLYGON,
                 creds=ApiCreds(api_key=c["POLY_API_KEY"], api_secret=c["POLY_API_SECRET"], api_passphrase=c["POLY_API_PASSPHRASE"]),
                 signature_type=3, funder=c["POLY_DEPOSIT_WALLET"])


def saldo_onchain(wallet, _post=None):
    """pUSD on-chain de la wallet de deposito (balanceOf, eth_call 'latest') por RPC publico. Las ordenes abiertas NO lo reducen (solo el casado). v7 (5o /code-review, hallazgo 9): exige SIEMPRE >= RPC_MIN_VALIDAS (2) respuestas validas de RPC distintos de la lista fija
    y devuelve el MINIMO (un nodo atrasado devolveria un saldo MAS ALTO y ocultaria un relleno: el minimo es el lado conservador). Con UNA sola respuesta valida (o ninguna) => None (ilegible: quien llama no envia / bloquea): una lectura sin contrastar no vale.
    Por que NO `polygon_rpc.llamar` (regla del repo: Polygon solo via polygon_rpc.py): se detiene en la PRIMERA respuesta valida (justo lo que se prohibe aqui), importa `requests` y relee un JSON fuera del paquete, incompatible con `python -I` + vendor con hash;
    RPCS replica su grupo 'latest' (un test lo compara con `polygon_rpc._POR_DEFECTO`)."""
    w = str(wallet or "").lower()
    if not (w.startswith("0x") and len(w) == 42):
        return None
    try:
        int(w[2:], 16)
    except ValueError:
        return None
    if _post is None:
        import requests
        _post = lambda url, js: requests.post(url, json=js, timeout=(2, 3)).json()
    js = {"jsonrpc": "2.0", "id": 1, "method": "eth_call", "params": [{"to": PUSD, "data": "0x70a08231" + w[2:].rjust(64, "0")}, "latest"]}
    vals, t_fin = [], time.monotonic() + 6.0
    for url in RPCS:
        if time.monotonic() > t_fin:
            break
        try:
            res = _post(url, js).get("result")
            if isinstance(res, str) and res.startswith("0x") and 3 <= len(res) <= 66:
                vals.append(int(res, 16) / 1e6)
        except Exception:
            continue
        if len(vals) >= RPC_MIN_VALIDAS:
            break
    return min(vals) if len(vals) >= RPC_MIN_VALIDAS else None
