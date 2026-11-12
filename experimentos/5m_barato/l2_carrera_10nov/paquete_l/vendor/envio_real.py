"""envio_real.py -- EXTRACTO VERBATIM de sonda1/sonda1.py (sha256 origen en VENDOR_HASHES.json; lineas 75-75, 270-271, 274-281, 708-708, 711-727, 730-731, 734-868). NO editar: regenerar con regenerar_vendor.py.
Dependencias: `vendor_main` (la inyecta pl_core.cargar_vendor en sys.modules con el hash verificado; este modulo NO toca sys.path), re, threading, time, datetime. Solo lo usa pl_sender_real.py con --real + confirmacion."""
import re, sys, os, threading, time
from datetime import datetime, timezone
import vendor_main as V


NO_EXISTE = "NO_EXISTE"             # estado que devuelve estado_seguro ante un 404 EXPLÍCITO (distinto de ilegible)


def log(msg):
    print(f"{datetime.now(timezone.utc).isoformat(timespec='milliseconds')} {msg}", flush=True)


class ErrCrudo(str):
    """Error crudo de una lectura (texto para el CSV) que conserva el status_code HTTP: el 404 se decide por el código, nunca por subcadena."""
    status_code = None

    def __new__(cls, txt, status_code=None):
        o = super().__new__(cls, txt)
        o.status_code = status_code
        return o


PRECARGA_TIMEOUT_S, PRECARGA_MARGEN_MIN_S = 4.0, 10.0


def _con_timeout(fn, seg):
    """Ejecuta fn en un hilo daemon; si no acaba en seg lanza TimeoutError (fail-closed para la precarga)."""
    res = {}

    def run():
        try:
            res["v"] = fn()
        except BaseException as e:                      # se re-lanza en el hilo llamante
            res["e"] = e
    t = threading.Thread(target=run, daemon=True)
    t.start()
    t.join(seg)
    if t.is_alive():
        raise TimeoutError(f"CLOB sin respuesta en {seg} s")
    if "e" in res:
        raise res["e"]
    return res.get("v")


def _ahora():
    return time.monotonic()                              # reloj inyectable para tests


class EnvioReal:
    """SOLO wallet dedicada. Sin code-review: no usar sin decisión de la sesión principal + Javi."""
    real = True

    def __init__(self):
        self.M = V
        self.cli = V.cliente_dedicado()                 # fail-closed si comparte credenciales con producción
        self.wallet = getattr(getattr(self.cli, "builder", None), "funder", None)   # wallet de depósito (sin leer .env)
        self._cache_lock = threading.Lock()             # por instancia (la caché también lo es); no reentrante

    _CACHE_MAX = 16

    def _cache_set(self, tok, clave, valor):
        with self._cache_lock:
            c = self.__dict__.setdefault("_cache", {})
            e = c.setdefault(tok, {})
            e[clave] = valor
            e["ts"] = _ahora()                            # monotónico: TTL robusto a saltos de reloj
            while len(c) > self._CACHE_MAX:             # acotada: se descarta el token más antiguo
                c.pop(next(iter(c)))

    _CACHE_TTL_S = 300.0

    def _cache_get(self, tok, clave):
        with self._cache_lock:
            c = self.__dict__.get("_cache", {})
            e = c.get(tok)
            if e is not None and _ahora() - e.get("ts", 0) > self._CACHE_TTL_S:
                c.pop(tok, None)                        # caducada: se vuelve a pedir al CLOB
                return None
            return (e or {}).get(clave)

    def tick(self, tok):
        v = self._cache_get(tok, "tick")
        if v is None:                                   # sin precarga (o falló): una llamada ahora; si falla, propaga (regla de transitorios)
            v = str(self.cli.get_tick_size(tok))
            self._cache_set(tok, "tick", v)
        return v

    def _neg_risk(self, tok):
        v = self._cache_get(tok, "neg")
        if v is None:
            v = bool(self.cli.get_neg_risk(tok))
            self._cache_set(tok, "neg", v)
        return v

    def precargar(self, tok):
        """Precarga tick-size y neg-risk (constantes por mercado) en la caché. NUNCA propaga ni toca contadores/kill: devuelve False si
        falla (se reintenta en t0 por el camino normal)."""
        try:
            _con_timeout(lambda: (self.tick(tok), self._neg_risk(tok)), PRECARGA_TIMEOUT_S)
            return True
        except Exception as e:
            log(f"precarga fallida ({type(e).__name__}): se reintenta en t0")
            return False

    def poner(self, tok, precio, size, clave, neg_risk=None):
        from py_clob_client_v2 import OrderArgsV2, PartialCreateOrderOptions
        nr = self._neg_risk(tok)                        # el MISMO neg_risk para firmar y para el hash (como medir_cancelacion_delay)
        if neg_risk is not None and bool(neg_risk) != nr:
            raise RuntimeError(f"neg_risk del mercado (gamma {bool(neg_risk)}) != cliente ({nr}): no firmo")
        signed = self.cli.create_order(OrderArgsV2(token_id=tok, price=precio, size=size, side="BUY"),
                                       PartialCreateOrderOptions(neg_risk=nr))
        oid = self.M.hash_orden(signed, nr)             # hash EIP-712 local, calculado ANTES del POST
        return oid, signed

    def enviar(self, signed):
        from py_clob_client_v2 import OrderType
        return self.cli.post_order(signed, OrderType.GTC, post_only=True)

    def estado(self, oid):
        od = self.cli.get_order(oid)
        if od is None:                                  # medido (H47, n=38): una orden aún sin indexar/inexistente devuelve HTTP 200 con cuerpo null, NO 404
            return None, NO_EXISTE
        if isinstance(od, dict) and re.search(r"not found|no order|does not exist", str(od.get("error") or od.get("errorMsg") or ""), re.I):
            return None, NO_EXISTE                      # dict con 'error' NO verificado contra el CLOB real: DISEÑO.md §10
        if not (isinstance(od, dict) and od.get("size_matched") not in (None, "") and str(od.get("status") or "").strip()):
            return None, None                           # ilegible != 0 relleno
        return float(od["size_matched"]), str(od["status"]).strip().upper()

    def cancelar(self, oid):
        from py_clob_client_v2 import OrderPayload
        resp = self.cli.cancel_order(OrderPayload(orderID=oid))
        return isinstance(resp, dict) and oid.lower() in [str(x).lower() for x in (resp.get("canceled") or [])]

    def saldo(self):
        return V.saldo_onchain(self.wallet) if self.wallet else None

    def abiertas(self, tok):
        """ids de las órdenes ABIERTAS del cliente en el token (None si ilegible o si no se puede garantizar la lista COMPLETA). Filtra por
        asset_id y pide TODAS las páginas (`only_first_page=False`: el cliente itera next_cursor hasta END_CURSOR; leído del código de
        py_clob_client_v2, NO verificado contra el CLOB real, DISEÑO.md §11). Un cliente sin ese parámetro (TypeError), una excepción a mitad de
        paginación o una respuesta que no es lista de dicts => None => verificar_inexistente NO descarta la orden."""
        from py_clob_client_v2 import OpenOrderParams
        try:
            res = self.cli.get_open_orders(OpenOrderParams(asset_id=tok), only_first_page=False)
            if not isinstance(res, list) or not all(isinstance(o, dict) for o in res):
                return None
            return [str(o.get("id") or "") for o in res]
        except Exception as e:
            log(f"get_open_orders falló ({type(e).__name__}): {str(e)[:120]}")
            return None

    # --- lecturas CRUDAS (solo --paquete-pruebas): devuelven (respuesta|None, error|None); nunca lanzan ---
    def get_order_crudo(self, oid):
        try:
            return self.cli.get_order(oid), None
        except Exception as e:
            return None, ErrCrudo(f"{type(e).__name__}: status={getattr(e, 'status_code', None)} {getattr(e, 'error_msg', e)}"[:300],
                                  getattr(e, "status_code", None))

    def cancelar_crudo(self, oid):
        from py_clob_client_v2 import OrderPayload
        try:
            return self.cli.cancel_order(OrderPayload(orderID=oid)), None
        except Exception as e:
            return None, f"{type(e).__name__}: status={getattr(e, 'status_code', None)} {getattr(e, 'error_msg', e)}"[:300]

    def abiertas_paginas(self, tok):
        """(ids, nº de páginas) de las abiertas del token iterando next_cursor a mano (el cliente no expone el nº de páginas). Usa _l2_headers/_get
        del cliente (privados; NO verificado contra el CLOB real, DISEÑO.md §15): cualquier fallo => (None, None) y se registra vacío."""
        try:
            from py_clob_client_v2.constants import END_CURSOR, INITIAL_CURSOR
            from py_clob_client_v2.endpoints import ORDERS
            headers = self.cli._l2_headers("GET", ORDERS)
            cur, ids, n = INITIAL_CURSOR, [], 0
            while cur != END_CURSOR and n < 20:
                r = self.cli._get(f"{self.cli.host}{ORDERS}", headers=headers, params={"asset_id": tok, "next_cursor": cur})
                n += 1
                cur = r["next_cursor"]
                ids += [str(o.get("id") or "") for o in r["data"]]
            return ids, n
        except Exception as e:
            log(f"abiertas_paginas falló ({type(e).__name__}): {str(e)[:120]}")
            return None, None
