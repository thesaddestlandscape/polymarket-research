#!/usr/bin/env python3
"""detector_r5k.py -- A6 (misión 5m barato, H43 R5K): detector EN VIVO del «volumen adquirido por makers» en la banda.

Núcleo puro (stdlib, sin red, sin disco): se alimenta con los `last_trade_price` del WS de mercado del CLOB (hora de
RECEPCIÓN local en ms, nunca el timestamp del mensaje) y reproduce, con el MISMO criterio que pass1.py (on-chain), las filas
«relleno de maker en banda»: cum_banda(s) = acciones ADQUIRIDAS por makers del lado s con precio equivalente pc en
(BANDA_LO, BANDA_HI] y T = cierre - recepción en (T_MIN, T_MAX].

Normalización (idéntica a pass1.py::procesar_tx, lado del TOMADOR que da el WS en `side`):
  tomador COMPRA token X a p  -> el maker VENDIÓ X a p  -> adquirió el lado contrario de X a pc = 1 - p   (venta en pass1)
  tomador VENDE  token X a p  -> el maker COMPRÓ X a p  -> adquirió X a pc = p                            (compra en pass1)
  coste = acc * pc (USDC)

Enchufable: `DetectorR5K.al_trade(token, t_recv_ms, msg)` tiene la firma de `ejecutor_rapido.Libro(al_trade=...)`.
Huecos de feed (`on_gap` / `on_snapshot`): el WS no reenvía operaciones perdidas; un mercado con un hueco dentro de su
ventana (cierre-300, cierre-60) se marca `completo=False` y su cum es COTA INFERIOR (nunca se presenta como exacto).
Ningún método envía órdenes ni toca disco. Uso offline: r5k_replay.py. Tests: test_detector_r5k.py.
"""
import threading
from collections import defaultdict
from functools import wraps

BANDA_LO, BANDA_HI = 0.10, 0.30
T_MIN, T_MAX = 60.0, 300.0
OFFSET, K, T_COS_MAX = 5000.0, 50.0, 270.0   # congelados en H43 R5K (REGISTRO_HIPOTESIS), no se retocan
OPUESTO = {"YES": "NO", "NO": "YES"}


def normalizar(lado_token, side, precio, size):
    """(lado_c, pc, acc, coste) del maker según el lado del TOMADOR, o None si el evento no es interpretable."""
    if size is None or size <= 0 or precio is None or not (0.0 < precio < 1.0):
        return None
    if side == "BUY":                       # tomador compra X -> el maker vendió X -> adquiere el opuesto a 1-p
        lado_c, pc = OPUESTO[lado_token], round(1.0 - precio, 4)
    elif side == "SELL":                    # tomador vende X -> el maker compró X a p
        lado_c, pc = lado_token, round(precio, 4)
    else:
        return None
    return lado_c, pc, size, size * pc


def _con_cerrojo(f):
    @wraps(f)
    def g(self, *a, **k):
        with self._lock:
            return f(self, *a, **k)
    return g


class DetectorR5K:
    def __init__(self, tokens=None, banda=(BANDA_LO, BANDA_HI), t_min=T_MIN, t_max=T_MAX, offset=OFFSET, k=K,
                 t_cos_max=T_COS_MAX, guardar_filas=True, max_edad_s=1800):
        """tokens: dict token -> (mkt, lado 'YES'|'NO', cierre_epoch_s) SOLO de los mercados BTC 5m a vigilar."""
        self.tok = dict(tokens or {})
        self.lo, self.hi, self.t_min, self.t_max = banda[0], banda[1], t_min, t_max
        self.offset, self.k, self.t_cos_max = offset, k, t_cos_max
        self.guardar = guardar_filas
        self.max_edad_s = max_edad_s
        self.cum = defaultdict(float)          # (mkt, lado_c) -> acciones en banda acumuladas (T in (t_min, t_max])
        self.estado = {}                       # (mkt, lado_c) -> dict de la cosecha
        self.filas = []                        # filas de banda en el formato común con pass1 (ts_s, mkt, lado_c, acc, coste, T, pc, recv_ms)
        self.cruces = []                       # eventos de cruce de offset
        self.huecos = defaultdict(list)        # mkt -> [(t_ini_ms, t_fin_ms|None)]
        self._abierto = {}                     # token -> t_ini_ms de hueco abierto (hasta el siguiente snapshot)
        self.stats = defaultdict(int)
        self._lock = threading.RLock()         # varios Libro (uno por mercado) alimentan el mismo detector desde hilos distintos

    # -- alta/baja de mercados --------------------------------------------------------------------------------
    @_con_cerrojo
    def alta(self, token, mkt, lado, cierre_s):
        self.tok[token] = (str(mkt), lado, float(cierre_s))

    @_con_cerrojo
    def podar(self, ahora_s):
        """Quita tokens/estado de mercados cerrados hace > max_edad_s (memoria acotada en vivo)."""
        viejos = {t for t, (_m, _l, c) in self.tok.items() if c < ahora_s - self.max_edad_s}
        if not viejos:
            return 0
        mk = {self.tok[t][0] for t in viejos}
        for t in viejos:
            self.tok.pop(t, None)
            self._abierto.pop(t, None)
        for key in [x for x in self.cum if x[0] in mk]:
            self.cum.pop(key, None)
            self.estado.pop(key, None)
        for m in mk:
            self.huecos.pop(m, None)
        return len(viejos)

    # -- huecos ----------------------------------------------------------------------------------------------------
    @_con_cerrojo
    def on_gap(self, token, t_ms):
        """Pérdida potencial de operaciones. token=None -> toda la conexión (todos los tokens conocidos).
        El hueco de cada token se cierra con SU siguiente snapshot (on_snapshot): el servidor manda el libro al suscribir."""
        for tk in ([token] if token is not None else list(self.tok)):
            if tk not in self._abierto:
                self._abierto[tk] = t_ms
        self.stats["huecos"] += 1

    @_con_cerrojo
    def on_snapshot(self, token, t_ms):
        """Llegó un libro completo (B) del token: cierra su hueco abierto, si lo hay."""
        ini = self._abierto.pop(token, None)
        if ini is not None and token in self.tok:
            self.huecos[self.tok[token][0]].append((ini, t_ms))

    @_con_cerrojo
    def completo(self, mkt, cierre_s, hasta_ms=None):
        """True si ningún hueco (ni abierto) solapa la ventana de banda [cierre-t_max, cierre-t_min] hasta `hasta_ms`."""
        a, b = (cierre_s - self.t_max) * 1000.0, (cierre_s - self.t_min) * 1000.0
        if hasta_ms is not None:
            b = min(b, hasta_ms)
        for ini, fin in self.huecos.get(mkt, ()):
            if ini <= b and (fin is None or fin >= a):
                return False
        for tk, ini in self._abierto.items():
            if tk in self.tok and self.tok[tk][0] == mkt and ini <= b:
                return False
        return True

    @_con_cerrojo
    def en_hueco(self, mkt, t_ms):
        """True si t_ms cae dentro de un hueco conocido (cerrado o abierto) de algún token del mercado."""
        for ini, fin in self.huecos.get(mkt, ()):
            if ini <= t_ms and (fin is None or t_ms <= fin):
                return True
        for tk, ini in self._abierto.items():
            if tk in self.tok and self.tok[tk][0] == mkt and ini <= t_ms:
                return True
        return False

    # -- operaciones -------------------------------------------------------------------------------------------------
    def al_trade(self, token, t_recv_ms, msg):
        """Firma de ejecutor_rapido.Libro(al_trade=...). msg = dict del WS (price, size, side como cadenas)."""
        try:
            return self.on_trade(token, t_recv_ms, float(msg["price"]), msg.get("side"), float(msg.get("size") or 0))
        except (KeyError, TypeError, ValueError):
            self.stats["trade_ilegible"] += 1
            return []

    @_con_cerrojo
    def on_trade(self, token, t_recv_ms, precio, side, size):
        """Devuelve la lista de eventos generados (vacía casi siempre). Evento 'cruce' al alcanzar `offset`."""
        info = self.tok.get(token)
        if info is None:
            self.stats["token_fuera"] += 1
            return []
        mkt, lado_tk, cierre = info
        n = normalizar(lado_tk, side, precio, size)
        if n is None:
            self.stats["no_interpretable"] += 1
            return []
        lado_c, pc, acc, coste = n
        T = cierre - t_recv_ms / 1000.0
        if not (self.lo < pc <= self.hi) or not (self.t_min < T <= self.t_max):
            self.stats["fuera_banda"] += 1
            return []
        self.stats["en_banda"] += 1
        key = (mkt, lado_c)
        if self.guardar:
            self.filas.append((t_recv_ms / 1000.0, mkt, lado_c, acc, coste, T, pc, t_recv_ms))
        eventos = []
        c0 = self.cum[key]
        self.cum[key] = c0 + acc
        st = self.estado.get(key)
        if st is None and c0 + acc >= self.offset:             # cruce (criterio de unid_cosechable: new >= OFF)
            cand = min(c0 + acc - self.offset, acc)
            st = self.estado[key] = {"t_cruce_ms": t_recv_ms, "T_cruce": T, "cum": c0 + acc, "need": self.k,
                                     "take": [], "completo_al_cruce": self.completo(mkt, cierre, t_recv_ms)}
            ev = {"evento": "cruce", "mkt": mkt, "lado": lado_c, "t_recv_ms": t_recv_ms, "T": round(T, 3),
                  "cum": c0 + acc, "completo": st["completo_al_cruce"], "cierre": cierre}
            self.cruces.append(ev)
            if not self.guardar and len(self.cruces) > 2000:
                del self.cruces[:1000]                       # en vivo: memoria acotada
            eventos.append(ev)
        elif st is not None:
            cand = acc
        else:
            return eventos
        # cosecha: las K acciones SIGUIENTES con T <= t_cos_max (precio del maker, población con cola optimista)
        if st["need"] > 1e-9 and T <= self.t_cos_max:
            th = min(cand, st["need"])
            if th > 0:
                st["take"].append((pc, th, t_recv_ms))
                st["need"] -= th
                if st["need"] <= 1e-9:
                    eventos.append({"evento": "cosecha_completa", "mkt": self._mk(key), "lado": lado_c, "t_recv_ms": t_recv_ms,
                                    "precio_medio": sum(p * t for p, t, _ in st["take"]) / self.k})
        return eventos

    @staticmethod
    def _mk(key):
        return key[0]

    @_con_cerrojo
    def unidades(self):
        """Unidad por (mkt, lado_c) con las K acciones cosechadas: {'take': [(pc, acc, recv_ms)], 'completa': bool}."""
        out = {}
        for key, st in self.estado.items():
            if st["take"]:
                out[key] = {"take": list(st["take"]), "completa": st["need"] <= 1e-9, "t_cruce_ms": st["t_cruce_ms"],
                            "completo_al_cruce": st["completo_al_cruce"]}
        return out
