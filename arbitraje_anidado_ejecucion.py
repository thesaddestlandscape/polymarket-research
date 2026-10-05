#!/usr/bin/env python3
"""arbitraje_anidado_ejecucion.py -- camino de ejecución del arbitraje anidado de 2 patas (05-Oct, Javi: "mandar las dos
patas en un solo envío por lotes" + "disparar solo cuando la oportunidad se confirma una segunda vez y con la firma ya
precalentada"). La DETECCIÓN sigue siendo la de arbitraje_anidado_dryrun_fase0.py; aquí solo vive cómo se dispara.

Por qué (analisis_arbitraje_anidado_dryrun.py, 67 oportunidades 02-05 Oct, desenlace oficial 100 %, 0 garantías rotas):
  - L=150 ms es inalcanzable para un tomador (taker delay oficial 150 ms en cripto). Medido 05-Oct 17Z con órdenes
    reales imposibles de llenar: firma 5 ms (caché caliente; 172 ms la primera vez por token) y POST 226 ms mediana
    (p95 702) -> evento->casado ~215-250 ms. POST /orders con las 2 patas: 254 ms mediana (vs ~450 en serie).
  - 1ª detección: +136 $ a 150 ms pero +12 $ a 400 ms (−19 sin el mejor día): la pata vieja la retira un maker
    protegido por el retraso. 2ª detección: positiva y casi insensible a la latencia (n pequeño: EXPLORATORIO; la cifra
    vigente la da `analisis_arbitraje_anidado_dryrun.py --reconfirmada`, que replica ESTA política y ESTAS guardas).
  - Las dos patas en UNA petición (POST /orders) se casan en el mismo ciclo del motor; dos POST seguidos dejarían la
    segunda ~226 ms detrás y la simulación (ambas patas en t+L) dejaría de ser cierta. NO es atómico: cada FOK casa o
    muere por separado -> la pata suelta se trata abajo.

Piezas:
  Precalentador  -- al conocer los tokens de un par, cachea tick_size/neg_risk y hace una firma de descarte: el disparo
                    firma en ~5 ms sin consultas de red. La caché caduca a los TICK_TTL_S y un precio fuera de la
                    rejilla cacheada veta y recalienta (el tick cambia por debajo de 0,04 / encima de 0,96).
  Reconfirmador  -- la 2ª detección de la misma oportunidad (par, moneda, cierre, pata A) a RECONF_MIN_MS..RECONF_MAX_MS
                    de la 1ª es candidata; solo cuenta como disparada si pasa las guardas (marcar()). Más allá de
                    RECONF_MAX_MS la detección pasa a ser la nueva 1ª. Tras un reinicio relee el ledger (idempotencia).
  veto_basico()  -- guardas puras de la oportunidad (neto, shares en rejilla, nocional, cierre): las comparte el análisis.
  disparar()     -- guardas fail-closed -> anota la INTENCIÓN en el ledger -> firma 2 BUY FOK con límite = ask detectado
                    -> un solo post_orders -> verifica cada pata contra get_trades (_verificar_pata: si/no/desconocido; la
                    respuesta del CLOB no es fiable). Una sola pata casada o estado incierto => kill-switch + alerta.
                    DRY_RUN (por defecto) firma pero NO envía.

NO hay envío real sin: pase de casos límite + /code-review + OK de Javi (CLAUDE.md). LIVE solo si existe
data/live/arbitraje_anidado_LIVE, y el kill-switch data/live/arbitraje_anidado_kill.json lo para siempre.

Uso de prueba (latencia del lote, sin riesgo): python3 arbitraje_anidado_ejecucion.py --probar-lote
  -> 2 órdenes FOK a 0,02 (imposibles de llenar) en un solo POST sobre las dos patas de un par vivo BTC 5m>15m.
"""
import json
import os
import statistics
import sys
import threading
import time
from decimal import Decimal
from pathlib import Path

REPO = Path(__file__).resolve().parent
FICHERO_LIVE = REPO / "data/live/arbitraje_anidado_LIVE"
KILL = REPO / "data/live/arbitraje_anidado_kill.json"
LEDGER = REPO / "data/live/arbitraje_anidado_disparos.jsonl"

FEE = 0.07
RECONF_MIN_MS = 500           # la 2ª detección debe llegar al menos 0,5 s después de la 1ª
RECONF_MAX_MS = 30_000        # y no más tarde de 30 s (si no, pasa a ser una 1ª detección nueva)
NETO_MIN_DISPARO = 0.01       # margen por share tras fees en el disparo (la detección usa 0,0005)
MIN_SHARES = 5.0              # min_order_size del CLOB
MIN_NOCIONAL_USD = 1.0        # mínimo de $1 por orden
MAX_SHARES = 200.0
FIN_MARGEN_S = 5              # no disparar a <5 s del cierre (rechazos "trading is disabled")
TICK_TTL_S = 60               # caducidad de tick_size/neg_risk cacheados (refresco en segundo plano a TTL/2)
USO_S = 20 * 60               # un token pedido en los últimos 20 min se mantiene caliente
LEDGER_RELECTURA_S = 6 * 3600


def fee(p):
    return FEE * p * (1 - p)


def _log(msg):
    print(f"[{time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())}Z] [arb_ejec] {msg}", flush=True)


def es_live():
    return FICHERO_LIVE.exists()


def kill_activo():
    """Fail-closed: un kill ilegible cuenta como activo."""
    if not KILL.exists():
        return False
    try:
        return bool(json.loads(KILL.read_text()).get("activo", True))
    except Exception:
        return True


def activar_kill(motivo):
    try:
        KILL.write_text(json.dumps({"activo": True, "motivo": motivo,
                                    "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}))
    except Exception as e:
        _log(f"🚨 no se pudo escribir el kill ({motivo}): {type(e).__name__}: {e}")
    _log(f"🚨 KILL activado: {motivo}")
    try:
        import live_trade as lt
        lt.enviar_telegram(f"🚨 ARBITRAJE ANIDADO: kill activado -- {motivo}. Revisar posición a mano.")
    except Exception:
        pass


def _dec(x):
    return Decimal(str(x))


def shares_en_rejilla(shares, ask_a, ask_b):
    """Mayor nº ENTERO de shares <= shares (y <= MAX_SHARES) con el que ask·shares tenga como mucho 2 decimales en las
    DOS patas (el CLOB rechaza más de 2 decimales de USDC: "invalid amounts"). Mismo tamaño en ambas = garantía exacta.
    -> 0.0 si no hay ninguno >= MIN_SHARES."""
    try:
        sh = int(min(float(shares), MAX_SHARES))
        a, b = _dec(ask_a), _dec(ask_b)
    except Exception:
        return 0.0
    cent = Decimal("0.01")
    while sh >= MIN_SHARES:
        if (a * sh) % cent == 0 and (b * sh) % cent == 0:
            return float(sh)
        sh -= 1
    return 0.0


def veto_basico(ask_a, ask_b, shares, resto_s):
    """Guardas puras de la oportunidad (sin estado): -> (motivo o None, shares en rejilla). Las usa también el análisis."""
    try:
        if not (0 < ask_a < 1 and 0 < ask_b < 1):
            return "precio_fuera_rango", 0.0
        if 1 - ask_a - ask_b - fee(ask_a) - fee(ask_b) < NETO_MIN_DISPARO:
            return "neto<min", 0.0
        if resto_s < FIN_MARGEN_S:
            return "cierre_cerca", 0.0
        sh = shares_en_rejilla(shares, ask_a, ask_b)
        if sh < MIN_SHARES:
            return "shares", 0.0
        if sh * min(ask_a, ask_b) < MIN_NOCIONAL_USD:
            return "nocional<1$", 0.0
        return None, sh
    except Exception as e:
        return f"error_guardas:{type(e).__name__}", 0.0


class Precalentador:
    """Cachea tick_size/neg_risk por token (TTL) y deja la firma caliente. Hilo propio: nunca bloquea la detección."""

    def __init__(self, client, refresco=True):
        self.client = client
        self.opciones = {}            # token -> (PartialCreateOrderOptions, epoch)
        self.en_uso = {}              # token -> último epoch en que se pidió
        self._lock = threading.Lock()
        self._pend = set()
        if refresco:
            threading.Thread(target=self._refrescar, daemon=True, name="arb_precal").start()

    def _refrescar(self):
        """Recalienta ANTES de caducar los tokens pedidos en los últimos USO_S: el disparo no debe encontrar la caché
        vieja (un par de 5m vive 300 s y el TTL es 60 s)."""
        while True:
            time.sleep(TICK_TTL_S / 4)
            try:
                ahora = time.time()
                with self._lock:
                    viejos = [t for t, u in self.en_uso.items() if ahora - u <= USO_S
                              and (t not in self.opciones or ahora - self.opciones[t][1] > TICK_TTL_S / 2)
                              and t not in self._pend]
                    for t in [t for t, u in self.en_uso.items() if ahora - u > USO_S]:
                        self.en_uso.pop(t, None)
                    self._pend.update(viejos)
                if viejos:
                    self._calentar(viejos)
            except Exception as e:
                _log(f"refresco: {type(e).__name__}: {e}")

    def pedir(self, tokens):
        nuevos = []
        ahora = time.time()
        with self._lock:
            for t in tokens:
                if t:
                    self.en_uso[t] = ahora
                o = self.opciones.get(t)
                if t and (o is None or ahora - o[1] > TICK_TTL_S) and t not in self._pend:
                    self._pend.add(t)
                    nuevos.append(t)
        if nuevos:
            threading.Thread(target=self._calentar, args=(nuevos,), daemon=True).start()

    def invalidar(self, token):
        with self._lock:
            self.opciones.pop(token, None)
        self.pedir([token])

    def _calentar(self, tokens):
        from py_clob_client_v2 import OrderArgsV2, PartialCreateOrderOptions
        for t in tokens:
            try:
                op = PartialCreateOrderOptions(tick_size=self.client.get_tick_size(t),
                                               neg_risk=self.client.get_neg_risk(t))
                self.client.create_order(OrderArgsV2(token_id=t, price=0.5, size=MIN_SHARES * 2, side="BUY"), op)
                with self._lock:
                    self.opciones[t] = (op, time.time())
            except Exception as e:
                _log(f"precalentar {t[:10]}…: {type(e).__name__}: {e}")
            finally:
                with self._lock:
                    self._pend.discard(t)

    def opcion_valida(self, token, precio):
        """Opciones cacheadas si están vigentes Y el precio cae exacto en su rejilla de tick; si no, None (y recalienta)."""
        with self._lock:
            o = self.opciones.get(token)
            self.en_uso[token] = time.time()
        if o is None or time.time() - o[1] > TICK_TTL_S:
            self.pedir([token])
            return None
        try:
            if _dec(precio) % _dec(o[0].tick_size) != 0:
                self.invalidar(token)
                return None
        except Exception:
            return None
        return o[0]


class Reconfirmador:
    """Candidata = 2ª detección a RECONF_MIN_MS..RECONF_MAX_MS de la 1ª. Solo marcar() la consume (tras pasar las
    guardas): un veto no quema la oportunidad. Persistente vía ledger para no disparar dos veces tras un reinicio."""

    def __init__(self, releer_ledger=True):
        self.primera = {}             # clave -> ts_ms de la 1ª detección
        self.disparadas = {}          # clave -> ts_ms del disparo
        if releer_ledger:
            self._releer()

    def _releer(self):
        if not LEDGER.exists():
            return
        lim = (time.time() - LEDGER_RELECTURA_S) * 1000
        try:
            with open(LEDGER, encoding="utf-8") as f:
                for l in f:
                    try:
                        r = json.loads(l)
                    except Exception:
                        continue
                    if r.get("fase") in ("intencion", "resultado") and r.get("ts_ms", 0) >= lim:
                        self.disparadas[tuple(r["clave"])] = r["ts_ms"]
        except Exception as e:
            _log(f"🚨 releer ledger: {type(e).__name__}: {e}")
            raise                       # fail-closed: sin saber qué se disparó, no arrancar

    def candidata(self, clave, ts_ms):
        if clave in self.disparadas:
            return False
        t1 = self.primera.get(clave)
        if t1 is None or ts_ms - t1 > RECONF_MAX_MS:
            self.primera[clave] = ts_ms
            return False
        return ts_ms - t1 >= RECONF_MIN_MS

    def marcar(self, clave, ts_ms):
        self.disparadas[clave] = ts_ms

    def purgar(self, ts_ms):
        for d in (self.primera, self.disparadas):
            for k in [k for k, t in d.items() if ts_ms - t > 3_600_000]:
                d.pop(k, None)


def _anotar(reg):
    """Ledger append-only. Devuelve False si no se pudo escribir (el caller no envía sin ledger)."""
    try:
        with open(LEDGER, "a", encoding="utf-8") as f:
            f.write(json.dumps(reg, default=str) + "\n")
            f.flush()
        return True
    except Exception as e:
        _log(f"🚨 ledger: {type(e).__name__}: {e}")
        return False


def _ids_lote(resp):
    """-> [orderID pata A, orderID pata B] (None si esa pata vino con error). Formato inesperado -> excepción."""
    if not isinstance(resp, list) or len(resp) != 2:
        raise ValueError(f"respuesta de post_orders inesperada: {str(resp)[:200]}")
    out = []
    for it in resp:
        if not isinstance(it, dict):
            raise ValueError(f"elemento inesperado: {str(it)[:120]}")
        out.append(None if it.get("errorMsg") else (it.get("orderID") or it.get("id")))
    return out


def _verificar_pata(client, condition_id, order_id, ts_envio, intentos=3):
    """-> "si" / "no" / "desconocido". Mismo criterio de casado que live_trade._verificar_fill_real (verificado contra
    la wallet real: maker_address == nuestra wallet, trader_side TAKER, taker_order_id == orden), pero distinguiendo
    "no casó" (al menos una consulta respondió y no aparece) de "no se pudo verificar" (todas fallaron): esa función
    devuelve None en ambos casos y aquí eso escondería una pata suelta."""
    from py_clob_client_v2.clob_types import TradeParams
    if not order_id:
        return "no"                                       # la pata vino con errorMsg: el CLOB la rechazó/mató
    wallet = (os.getenv("POLY_DEPOSIT_WALLET") or "").lower()
    if not condition_id or not wallet:
        return "desconocido"
    alguna_ok = False
    for i in range(intentos):
        try:
            trades = client.get_trades(TradeParams(market=condition_id, after=int(ts_envio) - 5))
            alguna_ok = True
        except Exception as e:
            _log(f"verificar pata {order_id[:10]}… intento {i + 1}: {type(e).__name__}: {e}")
            trades = []
        for t in trades or []:
            if (str(t.get("maker_address", "")).lower() == wallet and t.get("trader_side") == "TAKER"
                    and t.get("taker_order_id") == order_id):
                return "si"
        if i < intentos - 1:
            time.sleep(1.5)
    return "no" if alguna_ok else "desconocido"


def disparar(client, precal, reconf, clave, tok_a, cond_a, ask_a, tok_b, cond_b, ask_b, shares, resto_s):
    """Guardas -> intención al ledger -> firma 2 patas -> UN post_orders (solo LIVE) -> verificación de cada pata."""
    from py_clob_client_v2 import OrderArgsV2, OrderType, PostOrdersV2Args
    ts_ms = int(time.time() * 1000)
    reg = {"ts_ms": ts_ms, "clave": list(clave), "ask_A": ask_a, "ask_B": ask_b, "shares_det": shares, "live": False}
    veto, sh = veto_basico(ask_a, ask_b, shares, resto_s)
    if not veto and (not tok_a or not tok_b or tok_a == tok_b or not cond_a or not cond_b):
        veto = "tokens"
    if not veto and kill_activo():
        veto = "kill"
    op_a = op_b = None
    if not veto:
        op_a, op_b = precal.opcion_valida(tok_a, ask_a), precal.opcion_valida(tok_b, ask_b)
        if op_a is None or op_b is None:
            veto = "firma_fria_o_tick"
    if veto:
        reg.update(fase="veto", veto=veto)
        _anotar(reg)
        return reg
    reg["shares"] = sh
    try:
        import live_trade as lt
        lt._parchear_redondeo_clob()                      # redondeo Decimal exacto (idempotente)
        t0 = time.perf_counter()
        oa = client.create_order(OrderArgsV2(token_id=tok_a, price=ask_a, size=sh, side="BUY"), op_a)
        ob = client.create_order(OrderArgsV2(token_id=tok_b, price=ask_b, size=sh, side="BUY"), op_b)
        reg["firma_ms"] = round((time.perf_counter() - t0) * 1000, 1)
    except Exception as e:
        reg.update(fase="veto", veto=f"firma:{type(e).__name__}:{str(e)[:80]}")
        _anotar(reg)
        return reg
    if not es_live():
        reg.update(fase="resultado", resultado="dry_run")
        reconf.marcar(clave, ts_ms)
        _anotar(reg)
        return reg
    # --- LIVE ---
    reg["live"] = True
    if not _anotar(dict(reg, fase="intencion")):
        reg.update(fase="veto", veto="ledger_no_escribible")
        return reg
    reconf.marcar(clave, ts_ms)                           # desde aquí, la oportunidad está consumida pase lo que pase
    t1 = time.perf_counter()
    try:
        resp = client.post_orders([PostOrdersV2Args(order=oa, orderType=OrderType.FOK),
                                   PostOrdersV2Args(order=ob, orderType=OrderType.FOK)])
        ts_envio = time.time()
        reg["post_ms"] = round((time.perf_counter() - t1) * 1000, 1)
        reg["resp"] = str(resp)[:400]
        id_a, id_b = _ids_lote(resp)
    except Exception as e:
        reg.update(fase="resultado", resultado=f"incierto:{type(e).__name__}: {str(e)[:200]}")
        _anotar(reg)
        activar_kill(f"estado incierto tras post_orders {clave}: {type(e).__name__}")
        return reg
    fa, fb = _verificar_pata(client, cond_a, id_a, ts_envio), _verificar_pata(client, cond_b, id_b, ts_envio)
    reg["fill_A"], reg["fill_B"] = fa, fb
    if "desconocido" in (fa, fb):
        reg["resultado"] = "incierto_verificacion"
    elif fa == "si" and fb == "si":
        reg["resultado"] = "ambas"
    elif fa == "no" and fb == "no":
        reg["resultado"] = "ninguna"
    else:
        reg["resultado"] = "pata_suelta_A" if fa == "si" else "pata_suelta_B"
    reg["fase"] = "resultado"
    _anotar(reg)
    if reg["resultado"] not in ("ambas", "ninguna"):
        activar_kill(f"{reg['resultado']} en {clave} ({sh} shares, A={fa}, B={fb}): posible posición sin cubrir")
    return reg


def probar_lote(n=6):
    """Latencia de POST /orders con 2 órdenes FOK a 0,02 (imposibles de llenar). Comprueba ANTES DE CADA LOTE que los
    dos mercados (5m y 15m) siguen a >= 60 s del cierre y que el ask de ambas patas está muy por encima de 0,02."""
    import live_trade as lt
    from py_clob_client_v2 import OrderArgsV2, OrderType, PostOrdersV2Args
    from resolution_sniper_observer import mercado_slot, token_ids
    ahora = time.time()
    ini15, ini5 = int(ahora // 900) * 900, int(ahora // 300) * 300
    fin5, fin15 = ini5 + 300, ini15 + 900
    if min(fin5, fin15) - ahora < 60 + n * 1.5:
        print("demasiado cerca del cierre del 5m o del 15m; reintentar en 1-2 min")
        return
    _, m15 = mercado_slot("BTC", "15m", ini15)
    _, m5 = mercado_slot("BTC", "5m", ini5)
    if not m15 or not m5:
        print("sin mercados vivos")
        return
    (y15, _), (_, n5) = token_ids(m15), token_ids(m5)
    if not y15 or not n5:
        print("ABORTADO: tokens no validados contra outcomes")
        return
    client = lt._get_clob_client()
    if client is None:
        print("ABORTADO: sin cliente CLOB")
        return
    precal = Precalentador(client, refresco=False)
    t0 = time.perf_counter()
    precal._calentar([y15, n5])
    print(f"precalentado (tick_size+neg_risk+firma de descarte) de 2 tokens: {(time.perf_counter() - t0) * 1000:.0f} ms")
    if y15 not in precal.opciones or n5 not in precal.opciones:
        print("ABORTADO: el precalentado falló (ver log arriba)")
        return
    firmas, lotes = [], []
    for i in range(n):
        if min(fin5, fin15) - time.time() < 60:
            print("ABORTADO: un mercado entra en su último minuto")
            break
        for t in (y15, n5):
            d = lt._consultar_profundidad_libro(None, t, 0.50, 1.05)
            if not isinstance(d.get("mejor_ask"), (int, float)) or d["mejor_ask"] <= 0.10:
                print(f"ABORTADO: ask {d.get('mejor_ask')} demasiado cerca de 0,02 en {t[:10]}…")
                return
        tf = time.perf_counter()
        oa = client.create_order(OrderArgsV2(token_id=y15, price=0.02, size=MIN_SHARES * 10, side="BUY"), precal.opciones[y15][0])
        ob = client.create_order(OrderArgsV2(token_id=n5, price=0.02, size=MIN_SHARES * 10, side="BUY"), precal.opciones[n5][0])
        firmas.append((time.perf_counter() - tf) * 1000)
        tp = time.perf_counter()
        try:
            r = client.post_orders([PostOrdersV2Args(order=oa, orderType=OrderType.FOK),
                                    PostOrdersV2Args(order=ob, orderType=OrderType.FOK)])
            est = str(r)[:160]
        except Exception as e:
            est = f"{type(e).__name__}: {str(e)[:120]}"
        lotes.append((time.perf_counter() - tp) * 1000)
        print(f"  lote {i + 1}: firma 2 patas {firmas[-1]:5.1f} ms  POST /orders {lotes[-1]:7.1f} ms -> {est}")
        time.sleep(0.4)
    if lotes:
        print(f"firma 2 patas mediana {statistics.median(firmas):.1f} ms | POST /orders (2 FOK) mediana "
              f"{statistics.median(lotes):.1f} ms, máx {max(lotes):.1f} ms")


if __name__ == "__main__":
    if "--probar-lote" in sys.argv:
        probar_lote()
    else:
        print(__doc__)
