#!/usr/bin/env python3
"""r3_regla.py -- NUCLEO PURO (sin red, sin disco) del brazo SHADOW en tiempo real de R2/R3 sobre la politica de B (H47-B maker, ETH/SOL/XRP 5m).

DRY-RUN PURO: no importa nada de produccion, no crea cliente CLOB, no firma, no envia ni cancela nada; solo transforma mensajes publicos del WS de mercado en
decisiones virtuales ("cotizaria / no cotizaria"), rellenos simulados y filas de log. Regla congelada: reglas_congeladas.json v2 (HASH.txt) del directorio padre.

POLITICAS (traders virtuales independientes por mercado):
  BASE  gemelo de B tal cual (H35 DEEP_PEG: top en banda (0,11-0,30], objetivo = top - k ticks, k ETH 2 / SOL 1 / XRP 1, repega, para a T=60). Sin regla.
  R2    B + R2_NIVEL15: cotiza solo si bid15(mismo lado, 15m que contiene al 5m) - objetivo <= 0,03 (en MILESIMAS enteras: <= 30). Sin dato / libro 15m cruzado
        / WS viejo => NO cotiza (fail-closed). Si la regla pasa a falso con una puja viva, se cancela (igual que B cuando el objetivo desaparece).
  R3    R2 AND acciones casadas en el mercado 5m en los 30 s previos (WS last_trade_price de ambos tokens) >= 26 AND hora UTC >= 4. Ventana incompleta => no cotiza.
ESCENARIOS de relleno (puja_cola explicita; el orden de prioridad real es desconocido => cota conservadora / cota optimista):
  cons_x  = gemelo CONS de B (sim_uno): operaciones del CLOB con hora del EXCHANGE; cola delante = tamano del nivel al entrar.  (PRIMARIO)
  cons_r  = igual, pero con la hora de RECEPCION (sensibilidad al reloj del exchange).
  opt_x   = cola delante = 0 (cota optimista), hora del exchange.
Semantica de relleno (identica a experimento_maker_h47.sim_uno): una operacion TOMADORA por debajo de nuestro precio llena entera; a nuestro precio solo llena lo que
supera la cola; consumen el bid del token las ventas tomadoras del token y las compras tomadoras del contrario (acunacion, precio equivalente 1-p); solo
operaciones con hora >= envio + 70 ms y <= cancelacion + 60 ms. Un relleno (aunque parcial) CIERRA la puja. Lectura del relleno cada POLL_S (0,5 s) como en B;
cancelacion -> 1,5 s de asentado antes de volver a pujar. No hay cap de 5 pujas vivas ni presupuesto (el brazo cotiza en TODOS los mercados de las 3 monedas).
Comisiones: maker 0 (rebate 20 % NO se suma: conservador). EV se mide por EUR (sum pnl / sum coste) en el vigia.

Todas las funciones de decision de B se REPLICAN aqui (mils, en_banda, objetivo_h35, en_rejilla, tamano_orden) porque importar el modulo de B arrastra el harness con
dinero; test_r3_shadow.py::test_gemelo_identico_a_b las compara con experimento_maker_h47 en una rejilla densa (si B cambia, ese test falla)."""
import math
from collections import deque
from datetime import datetime, timezone

VERSION = 1
K_POR_MONEDA = {"eth": 2, "sol": 1, "xrp": 1}
T_INI, T_STOP = 298.0, 60.0
LAT_POST_S, LAT_CANCEL_S = 0.07, 0.06
ASENTAR_S = 1.5
MIN_ENTRE_ACCIONES_S = 0.1
POLL_S = 0.5
REQUOTE_INVALIDO_S = 2.0
WS_MAX_S = 5.0
SIZE_BASE, SIZE_MIN, SIZE_MAX, MIN_NOCIONAL = 5, 5, 10, 1.0
# --- regla congelada (reglas_congeladas.json v2)
R2_MAX_MILS = 30                  # bid15 - objetivo <= 0,03
VOL30_MIN = 26.0                  # acciones casadas en 30 s
HORA_MIN = 4                      # hora UTC >= 4
VENTANA_VOL_S = 30.0
POLITICAS = ("BASE", "R2", "R3")
ESCENARIOS = {"cons_x": ("x", False), "cons_r": ("r", False), "opt_x": ("x", True)}   # clave -> (reloj, cola_cero)
ESC_PRIMARIO = "cons_x"
MUESTREO_S = 5.0


# ------------------------------------------------------------------ reglas puras (copia de experimento_maker_h47; ver test_gemelo_identico_a_b)
def mils(p):
    return int(round(float(p) * 1000))


def en_banda(bid, ask):
    try:
        b, a = mils(bid), mils(ask)
    except (TypeError, ValueError):
        return False
    return 0 < a and b < a and 110 < b <= 300


def objetivo_h35(bid, ask, k):
    b, a = mils(bid), mils(ask)
    o = b - k * 10 if b % 10 == 0 else (b // 10 - (k - 1)) * 10
    return round(o / 1000.0, 3) if (100 <= o <= 300 and o < b and o < a) else None


def en_rejilla(p):
    return abs(p * 100 - round(p * 100)) <= 1e-6


def tamano_orden(precio, size_base=SIZE_BASE, min_nocional=MIN_NOCIONAL):
    if size_base < SIZE_MIN or size_base > SIZE_MAX or precio <= 0:
        return None
    s = float(size_base)
    if min_nocional > 0 and s * precio < min_nocional - 1e-9:
        s = float(math.ceil(min_nocional / precio - 1e-9))
    if s > SIZE_MAX or s < SIZE_MIN:
        return None
    return s


def regla(pol, f):
    """(ok, motivo). f = rasgos (ver Mercado.rasgos). Cualquier dato ausente => False (fail-closed). BASE siempre True."""
    if pol == "BASE":
        return True, None
    if not f.get("fresco"):
        return False, "ws_viejo"
    if f.get("b15m") is None:
        return False, "sin_b15"
    if f.get("cruzado15"):
        return False, "b15_cruzado"
    if f["b15m"] - f["objm"] > R2_MAX_MILS:
        return False, "r2_nivel15"
    if pol == "R2":
        return True, None
    if f.get("vol30") is None:
        return False, "vol30_sin_ventana"
    if f["vol30"] < VOL30_MIN:
        return False, "r3_vol30"
    if f["hora"] < HORA_MIN:
        return False, "r3_hora"
    return True, None


def _r(x, n=4):
    return None if x is None else round(x, n)


# ------------------------------------------------------------------ libro L2 (formato del WS de mercado del CLOB; mismo parseo que X.Libro de B)
class Libro:
    def __init__(self, toks):
        self.L = {t: {"bids": {}, "asks": {}} for t in toks}
        self.snap = set()                       # tokens con snapshot desde la ultima (re)conexion
        self.trades = {t: [] for t in toks}     # (recepcion_s, hora_exchange_s, precio, tamano, lado_TOMADOR)
        self.trades_r = {t: [] for t in toks}
        self.tick_cambiado = False
        self.ult_cambio = {}                    # token -> recepcion del ultimo cambio aplicado

    def reset_snap(self):
        self.snap.clear()

    def aplicar(self, m, t_r):
        """Aplica UN mensaje (dict). Devuelve True si cambio el libro o llego una operacion."""
        et = m.get("event_type")
        tk = m.get("asset_id")
        if et == "tick_size_change" and tk in self.L:
            self.tick_cambiado = True
            return False
        if et == "last_trade_price" and tk in self.L:
            try:
                t_x = float(m["timestamp"]) / 1000.0 if m.get("timestamp") not in (None, "") else t_r
                self.trades[tk].append((t_r, t_x, float(m["price"]), float(m.get("size") or 0), str(m.get("side") or "").upper()))
                self.trades_r[tk].append(t_r)
                return True
            except (KeyError, TypeError, ValueError):
                return False
        if "price_changes" in m:
            hecho = False
            for pc in m["price_changes"]:
                L = self.L.get(pc.get("asset_id"))
                if L is None:
                    continue
                try:
                    p, s = float(pc["price"]), float(pc.get("size") or 0)
                except (KeyError, TypeError, ValueError):
                    continue
                lado = "bids" if pc.get("side") == "BUY" else "asks"
                if s <= 0:
                    L[lado].pop(p, None)
                else:
                    L[lado][p] = s
                self.ult_cambio[pc.get("asset_id")] = t_r
                hecho = True
            return hecho
        if tk in self.L and ("bids" in m or "asks" in m):
            self.L[tk] = {"bids": {float(x["price"]): float(x["size"]) for x in (m.get("bids") or [])},
                          "asks": {float(x["price"]): float(x["size"]) for x in (m.get("asks") or [])}}
            self.snap.add(tk)
            self.ult_cambio[tk] = t_r
            return True
        return False

    def top(self, tk):
        L = self.L[tk]
        b = max(((p, s) for p, s in L["bids"].items() if s > 0), default=None)
        a = min(((p, s) for p, s in L["asks"].items() if s > 0), default=None)
        return b, a

    def nivel(self, tk, precio):
        return float(self.L[tk]["bids"].get(precio, 0.0) or 0.0)

    def indice_trades(self, tk, t_r):
        import bisect
        return bisect.bisect_left(self.trades_r[tk], t_r)

    def trades_desde(self, tk, i):
        return self.trades[tk][i:]


def sim_orden(lib, par, o, f_prev, reloj):
    """Relleno CONS de UNA puja (port de experimento_maker_h47.sim_uno; reloj 'x' = hora del exchange como B, 'r' = recepcion). -> acciones llenadas (monotono)."""
    t_can = o.get("t_cancel")
    q = float(o["precio"])
    f = f_prev
    idx = o.setdefault("i_sim", {})
    o.setdefault("vol_sim", 0.0)
    for tk, lado_tomador in ((o["tok"], "SELL"), (par[o["tok"]], "BUY")):
        if tk not in idx:
            idx[tk] = lib.indice_trades(tk, o["t_post"] - 1.0)
        nuevos = lib.trades_desde(tk, idx[tk])
        idx[tk] += len(nuevos)
        for tr, tx, p, sz, sd in nuevos:
            t = tx if reloj == "x" else tr
            if sd != lado_tomador or t < o["t_post"] + LAT_POST_S:
                continue
            if t_can is not None and t > t_can + LAT_CANCEL_S:
                continue
            pe = p if tk == o["tok"] else round(1.0 - p, 2)
            if f >= o["size"] - 1e-9:
                break
            if pe < q - 1e-9:
                f = float(o["size"])
                o.setdefault("t1", tr)
            elif abs(pe - q) < 1e-9:
                o["vol_sim"] += sz
                nf = min(float(o["size"]), max(f, o["vol_sim"] - float(o["cola"] or 0.0)))
                if nf > f + 1e-12 and f <= 0:
                    o.setdefault("t1", tr)
                f = nf
    return f


# ------------------------------------------------------------------ un mercado 5m + su 15m
class Mercado:
    def __init__(self, coin, ini, mk5, mk15, t_ms_ahora):
        self.coin, self.ini, self.fin = coin, ini, ini + 300
        self.slug = mk5["slug"]
        self.id5, self.id15 = str(mk5["id"]), str(mk15["id"])
        self.k = K_POR_MONEDA[coin]
        self.up, self.dn, self.u15, self.d15 = mk5["up"], mk5["down"], mk15["up"], mk15["down"]
        self.par = {self.up: self.dn, self.dn: self.up}
        self.lado = {self.up: "YES", self.dn: "NO"}
        self.t15 = {self.up: self.u15, self.dn: self.d15}
        self.lib = Libro([self.up, self.dn, self.u15, self.d15])
        self.t_conexion = None          # recepcion del primer mensaje con libro (ventana de vol30 valida 30 s despues)
        self.ult_msg = 0.0
        self.vol = deque()              # (recepcion_s, tamano) de last_trade_price de los 2 tokens 5m
        self.n_msgs = 0
        self.reconex = 0
        self.huecos = 0
        self.parar_motivo = None
        self.arranque_tarde = (t_ms_ahora / 1000.0) > (self.ini - 20) + 25.0      # se empezo a vigilar > 25 s tras lo previsto
        self.traders = [Trader(p, e) for p in POLITICAS for e in ESCENARIOS]
        self.ult_smp = 0.0
        self.n_smp = 0
        self.cerrado = False
        self.t_fin_emitido = False
        self.n_dec = 0
        self._memo = {}
        self._memo_now = None

    # -- entrada de mensajes
    def on_msg(self, m, t_r):
        self.n_msgs += 1
        self.ult_msg = t_r
        self._memo = {}                 # el estado cambia con cada mensaje: se invalida la cache de rasgos
        if self.lib.aplicar(m, t_r):
            if self.t_conexion is None and self.lib.snap:
                self.t_conexion = t_r
            if m.get("event_type") == "last_trade_price" and m.get("asset_id") in (self.up, self.dn):
                try:
                    self.vol.append((t_r, float(m.get("size") or 0)))
                except (TypeError, ValueError):
                    pass

    def vivo(self, t_r):
        """Algun mensaje (PONG incluido) -> conexion viva."""
        self.ult_msg = t_r

    def reconectado(self, t_r):
        self.reconex += 1
        self.lib.reset_snap()
        self.huecos += 1
        # tras una reconexion el libro puede haberse perdido cambios: B pararia (ws_viejo > 5 s); aqui se registra el hueco y se para solo si fue largo
        self.t_conexion = None

    def fresco(self, now):
        return self.ult_msg > 0 and now - self.ult_msg <= WS_MAX_S

    # -- consultas
    def top(self, tk):
        return self.lib.top(tk)

    def libro_valido(self, tk):
        if tk not in self.lib.snap:
            return False
        b, a = self.top(tk)
        return b is not None and a is not None and b[0] < a[0] and en_rejilla(b[0])

    def elegir_cara(self):
        if self.lib.tick_cambiado:
            return None
        for tk in (self.up, self.dn):
            if tk not in self.lib.snap:
                continue
            b, a = self.top(tk)
            if b is not None and a is not None and en_rejilla(b[0]) and en_banda(b[0], a[0]):
                return tk
        return None

    def vol30(self, now):
        """Acciones casadas en el 5m en (max(now-30, apertura), now] por recepcion; None si el libro se conecto despues del inicio de la ventana."""
        while self.vol and self.vol[0][0] < now - 60.0:
            self.vol.popleft()
        # la ventana empieza en max(now-30, apertura): antes de abrir no hay operaciones (hecho, no dato ausente); debe haber libro conectado ANTES de ese inicio
        ini_v = max(now - VENTANA_VOL_S, float(self.ini))
        if self.t_conexion is None or self.t_conexion > ini_v:
            return None
        return sum(s for t, s in self.vol if ini_v < t <= now)

    def rasgos(self, tk, obj, now):
        """Rasgos de la decision para el token `tk` y el objetivo `obj` (precio). Todo lo que usan las reglas + el contexto que se loguea."""
        b, a = self.top(tk)
        t15 = self.t15[tk]
        b15 = a15 = None
        cruz = False
        if t15 in self.lib.snap:
            bb15, aa15 = self.top(t15)
            b15 = bb15[0] if bb15 else None
            a15 = aa15[0] if aa15 else None
            cruz = b15 is not None and a15 is not None and b15 >= a15 - 1e-9
        objm = mils(obj) if obj is not None else None
        b15m = mils(b15) if b15 is not None else None
        hora = datetime.fromtimestamp(now, timezone.utc).hour
        return {"fresco": self.fresco(now), "bb": b[0] if b else None, "ba": a[0] if a else None, "obj": obj, "objm": objm, "b15": b15, "a15": a15,
                "b15m": b15m, "cruzado15": cruz, "lvl15m": (b15m - objm) if (b15m is not None and objm is not None) else None,
                "vol30": self.vol30(now), "hora": hora, "T": round(self.fin - now, 2)}

    def flags(self, tk, obj, now):
        """Rasgos + flags de R2/R3. Cache por (token, objetivo, now): dentro de un tick el estado no cambia (un solo hilo asyncio) y 9 traders piden lo mismo."""
        if self._memo_now != now:
            self._memo, self._memo_now = {}, now
        k = (tk, obj)
        f = self._memo.get(k)
        if f is None:
            f = self.rasgos(tk, obj, now)
            f["r2"], f["m2"] = regla("R2", f)
            f["r3"], f["m3"] = regla("R3", f)
            self._memo[k] = f
        return f


def _fl(f):
    """Subconjunto compacto de rasgos para las filas."""
    if f is None:
        return None
    return {k: (_r(v, 3) if isinstance(v, float) else v) for k, v in f.items() if k in ("bb", "ba", "obj", "b15", "a15", "lvl15m", "vol30", "hora", "T", "r2", "r3", "m2", "m3")}


# ------------------------------------------------------------------ trader virtual
class Trader:
    def __init__(self, pol, esc):
        self.pol, self.esc = pol, esc
        self.reloj, self.cola_cero = ESCENARIOS[esc]
        self.tok = None
        self.orden = None
        self.pend = []                  # canceladas sin asentar
        self.llenas = 0.0
        self.coste = 0.0
        self.cerrado = False
        self.parado = False
        self.t_accion = 0.0
        self.fuera_desde = None
        self.ult_poll = 0.0
        self.n_post = 0
        self.motivo_prev = "__ini__"
        self.fin_puja = None
        self.fills = 0

    # -- helpers de log
    def _dec(self, m, now, emit, accion, tok, f, motivo=None, extra=None):
        m.n_dec += 1
        row = {"k": f"dec|{m.slug}|{self.pol}|{self.esc}|{m.n_dec}", "tipo": "dec", "r": int(now * 1000), "slug": m.slug, "coin": m.coin, "pol": self.pol,
               "esc": self.esc, "acc": accion, "lado": m.lado.get(tok) if tok else None, "motivo": motivo}
        row.update(_fl(f) or {})
        if extra:
            row.update(extra)
        emit(row)

    def _cancelar(self, m, now, emit, motivo, f=None):
        o = self.orden
        if o is None:
            return
        o["t_cancel"] = now
        o["motivo_cancel"] = motivo
        self.pend.append(o)
        self.orden = None
        self.t_accion = now
        self._dec(m, now, emit, "cancela", o["tok"], f, motivo, {"precio": o["precio"], "n_orden": o["n"]})

    def _liquidar(self, m, o, now, emit):
        f = o["f"]
        if f > 1e-9:
            self.llenas += f
            self.coste += f * o["precio"]
            self.cerrado = True
            self.fin_puja = self.fin_puja or "relleno"
            self.fills += 1
            t1 = o.get("t1") or o.get("t_det") or now
            emit({"k": f"fill|{m.slug}|{self.pol}|{self.esc}|{o['n']}", "tipo": "fill", "r": int(now * 1000), "slug": m.slug, "coin": m.coin, "pol": self.pol,
                  "esc": self.esc, "lado": m.lado[o["tok"]], "precio": o["precio"], "size": o["size"], "acc": round(f, 4), "n_orden": o["n"], "t1": int(t1 * 1000),
                  "T1": round(m.fin - t1, 2), "t_post": int(o["t_post"] * 1000), "T_post": round(m.fin - o["t_post"], 2), "cola": o["cola"],
                  "feat_post": _fl(o.get("feat_post")), "feat_det": _fl(o.get("feat_det")), "motivo_cancel": o.get("motivo_cancel")})

    # -- ciclo (10 Hz, como el LOOP_S=0,1 de B)
    def paso(self, m, now, emit):
        T = m.fin - now
        poll = (now - self.ult_poll) >= POLL_S
        if poll:
            self.ult_poll = now
        vivos = ([self.orden] if self.orden else []) + list(self.pend)
        for o in vivos:
            o["f"] = sim_orden(m.lib, m.par, o, o["f"], self.reloj)
            if poll and o["f"] > 1e-9 and o.get("t_det") is None:
                o["t_det"] = now
                o["feat_det"] = m.flags(o["tok"], o["precio"], now)
        for o in list(self.pend):
            if now - o["t_cancel"] >= ASENTAR_S:
                self._liquidar(m, o, now, emit)
                self.pend.remove(o)
        if self.orden is not None and poll and self.orden["f"] > 1e-9:
            self.cerrado = True
            self.fin_puja = self.fin_puja or "relleno"
            self._cancelar(m, now, emit, "relleno", self.orden.get("feat_det"))
        motivo_parada = m.parar_motivo or ("t_stop" if T <= T_STOP else None)
        if not self.parado and motivo_parada:
            self.parado = True
            self.fin_puja = self.fin_puja or motivo_parada
            if self.orden is not None:
                self._cancelar(m, now, emit, motivo_parada)
        if self.parado or self.cerrado or T > T_INI:
            return
        self._decidir(m, T, now, emit)

    def _decidir(self, m, T, now, emit):
        tok = self.tok or m.elegir_cara()
        if tok is None:
            return
        b, a = m.top(tok)
        valido = m.libro_valido(tok) and m.fresco(now)
        obj_base = objetivo_h35(b[0], a[0], m.k) if valido and en_banda(b[0], a[0]) else None
        f = None
        ok, motivo = False, "sin_objetivo"
        if obj_base is not None:
            f = m.flags(tok, obj_base, now)
            ok, motivo = regla(self.pol, f)
        obj = obj_base if ok else None
        o = self.orden
        if o is not None:
            if not valido:
                self.fuera_desde = self.fuera_desde or now
                if now - self.fuera_desde >= REQUOTE_INVALIDO_S:
                    self._cancelar(m, now, emit, "libro_invalido", f)
                    self.fuera_desde = None
                return
            self.fuera_desde = None
            if now - self.t_accion < MIN_ENTRE_ACCIONES_S:
                return
            if obj is None or abs(obj - o["precio"]) > 1e-9:
                self._cancelar(m, now, emit, "repega" if obj is not None else f"cancela_{motivo}", f)
            return
        if obj is None:
            if motivo != self.motivo_prev:
                self.motivo_prev = motivo
                self._dec(m, now, emit, "no_cotiza", tok, f, motivo)
            return
        if any(x["tok"] == tok for x in self.pend):
            return
        if now - self.t_accion < MIN_ENTRE_ACCIONES_S or T <= T_STOP + 2:
            return
        size = tamano_orden(obj)
        if size is None:
            if self.motivo_prev != "tamano":
                self.motivo_prev = "tamano"
                self._dec(m, now, emit, "no_cotiza", tok, f, "tamano")
            return
        cola = 0.0 if self.cola_cero else m.lib.nivel(tok, obj)
        self.n_post += 1
        self.tok = self.tok or tok
        self.orden = {"tok": tok, "precio": obj, "size": size, "t_post": now, "cola": cola, "f": 0.0, "n": self.n_post, "feat_post": f, "t_det": None}
        self.t_accion = now
        self.motivo_prev = "cotiza"
        self._dec(m, now, emit, "post", tok, f, None, {"precio": obj, "size": size, "cola": cola, "n_orden": self.n_post})

    def asentado(self):
        return self.orden is None and not self.pend


# ------------------------------------------------------------------ nucleo
class Nucleo:
    """Logica pura. `salida` = callable(row). `emitidos` = claves ya escritas (estado = el propio log: un reinicio no duplica)."""

    def __init__(self, salida, emitidos=None, prueba=None):
        self.salida = salida
        self.emitidos = emitidos if emitidos is not None else set()
        self.prueba = prueba
        self.mercados = {}
        self.stats = {}

    def emit(self, row):
        k = row["k"]
        if k in self.emitidos:
            self.stats["duplicado_evitado"] = self.stats.get("duplicado_evitado", 0) + 1
            return False
        self.emitidos.add(k)
        row["v"] = VERSION
        if self.prueba is not None:
            row["prueba"] = self.prueba
        self.salida(row)
        return True

    def nuevo(self, coin, ini, mk5, mk15, t_ms):
        m = Mercado(coin, ini, mk5, mk15, t_ms)
        self.mercados[m.slug] = m
        self.emit({"k": f"mkt|{m.slug}", "tipo": "mkt", "r": t_ms, "slug": m.slug, "coin": coin, "ini": ini, "fin": m.fin, "id5": m.id5, "id15": m.id15,
                   "tok5": [m.up, m.dn], "tok15": [m.u15, m.d15], "k_ticks": m.k, "arranque_tarde": m.arranque_tarde})
        return m

    def tick(self, now):
        for m in list(self.mercados.values()):
            if m.cerrado:
                continue
            T = m.fin - now
            if not m.parar_motivo and m.lib.tick_cambiado:
                m.parar_motivo = "tick_cambiado"             # como B: el tick deja de ser 0,01 => se sale
            if not m.parar_motivo and m.t_conexion is not None and not m.fresco(now) and T <= T_INI:
                m.parar_motivo = "ws_viejo"
                m.huecos += 1
            for tr in m.traders:
                try:
                    tr.paso(m, now, self.emit)
                except Exception as e:                       # una excepcion no mata el proceso: se registra y ese trader se para
                    tr.parado = True
                    self.stats["error_trader"] = self.stats.get("error_trader", 0) + 1
                    self.emit({"k": f"error|{m.slug}|{tr.pol}|{tr.esc}", "tipo": "error", "r": int(now * 1000), "m": f"{type(e).__name__}: {str(e)[:100]}"})
            self._muestreo(m, now)
            if T <= T_STOP + 0.0 and all(tr.asentado() for tr in m.traders):
                self.cerrar(m, now)
            elif T < -30:                                    # red de seguridad: nunca queda un mercado abierto para siempre
                self.cerrar(m, now, "timeout")

    def _muestreo(self, m, now):
        T = m.fin - now
        if T > T_INI or T <= T_STOP or now - m.ult_smp < MUESTREO_S:
            return
        tk = m.elegir_cara()
        if tk is None or not m.libro_valido(tk):
            return
        b, a = m.top(tk)
        obj = objetivo_h35(b[0], a[0], m.k)
        if obj is None:
            return
        m.ult_smp = now
        m.n_smp += 1
        f = m.flags(tk, obj, now)
        row = {"k": f"smp|{m.slug}|{int(now // MUESTREO_S)}", "tipo": "smp", "r": int(now * 1000), "slug": m.slug, "coin": m.coin, "lado": m.lado[tk]}
        row.update(_fl(f))
        self.emit(row)

    def cerrar(self, m, now, motivo=None):
        if m.cerrado:
            return
        m.cerrado = True
        for tr in m.traders:
            self.emit({"k": f"fin_t|{m.slug}|{tr.pol}|{tr.esc}", "tipo": "fin_t", "r": int(now * 1000), "slug": m.slug, "coin": m.coin, "pol": tr.pol, "esc": tr.esc,
                       "n_post": tr.n_post, "acc": round(tr.llenas, 4), "coste": round(tr.coste, 4), "fin_puja": tr.fin_puja,
                       "lado": m.lado.get(tr.tok) if tr.tok else None})
        completo = (not m.arranque_tarde) and m.huecos == 0 and m.parar_motivo is None and motivo is None
        self.emit({"k": f"mkt_fin|{m.slug}", "tipo": "mkt_fin", "r": int(now * 1000), "slug": m.slug, "coin": m.coin, "cierre": m.fin, "completo": completo,
                   "arranque_tarde": m.arranque_tarde, "huecos": m.huecos, "reconex": m.reconex, "n_msgs": m.n_msgs, "n_smp": m.n_smp, "n_dec": m.n_dec,
                   "parada": m.parar_motivo or motivo})

    def podar(self, now):
        for s in [s for s, m in self.mercados.items() if m.cerrado and now > m.fin + 120]:
            del self.mercados[s]
