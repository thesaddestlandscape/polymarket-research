#!/usr/bin/env python3
"""polygon_rpc.py -- UN solo punto para hablar JSON-RPC con Polygon, con failover entre RPCs públicos (12-Oct).

Por qué: el 09-Oct 08:10 publicnode empezó a rechazar eth_getLogs de archivo ("personal token") y
fetch_polymarket_fills_onchain.py estuvo 3,5 días sin datos on-chain sin que nadie se enterase (Javi: "no podemos
permitir que esto pase de nuevo"). Un nodo gratuito puede cambiar de política cuando quiera: lo que se garantiza es
(1) varios a los que saltar y (2) saber en cuanto uno falla (vigia_polygon_rpc.py, cada hora).

La LISTA vive en polygon_rpc_lista.json y se relee en cada llamada: este .py lo importan (vía live_balance) los
ejecutores con dinero real, así que cambiar de proveedor NO debe tocar código (el watchdog reiniciaría 12 screens).
Mantener este fichero estable; /code-review antes de editarlo.

Uso: from polygon_rpc import llamar ;  llamar("eth_call", [...], grupo="latest", plazo_total_s=10)
"""
import json
import sys
import threading
import time
from pathlib import Path

import requests

LISTA = Path(__file__).resolve().parent / "polygon_rpc_lista.json"
_ARCHIVO_DEF = ["https://polygon.drpc.org", "https://1rpc.io/matic", "https://gateway.tenderly.co/public/polygon",
                "https://rpc-mainnet.matic.quiknode.pro", "https://polygon-bor-rpc.publicnode.com"]
_POR_DEFECTO = {"latest": ["https://polygon-bor-rpc.publicnode.com", "https://polygon.drpc.org", "https://1rpc.io/matic"],
                "archivo": _ARCHIVO_DEF}   # /code-review 12-Oct: publicnode el ÚLTIMO para archivo (pide token)
_HTTP_POLITICA = (401, 402, 403)
_TEXTO_POLITICA = ("archive requests", "personal token", "api key", "unauthorized", "forbidden")
_TEXTO_LIMITE = ("rate limit", "too many requests", "exceeded")
_CACHE = {"mtime": None, "datos": None, "error": None}
_TLS = threading.local()


class RechazoPolitica(RuntimeError):
    """El RPC rechaza por política (token, auth): no se reintenta en ese RPC."""


class LimiteTemporal(RuntimeError):
    """429 / cuota: se reintenta con espera (no es un cambio de política)."""


def _leer_lista():
    """JSON cacheado por mtime. Error -> None y queda en _CACHE['error'] (lo reporta el vigía; aviso por stderr)."""
    try:
        mt = LISTA.stat().st_mtime
        if _CACHE["mtime"] != mt:
            _CACHE.update(mtime=mt, datos=json.loads(LISTA.read_text(encoding="utf-8")), error=None)
        return _CACHE["datos"]
    except Exception as e:
        if _CACHE["error"] != str(e):
            print(f"[polygon_rpc] ⚠️ {LISTA.name} ilegible ({type(e).__name__}: {e}): uso la lista por defecto",
                  file=sys.stderr, flush=True)
        _CACHE.update(mtime=None, datos=None, error=str(e))
        return None


def error_lista():
    _leer_lista()
    return _CACHE["error"]


def rpcs(grupo="latest"):
    """Lista vigente del grupo; si el JSON falta, está roto o el grupo viene vacío: la lista por defecto (y aviso)."""
    d = _leer_lista()
    if d is not None:
        lst = [u for u in d.get(grupo, []) if isinstance(u, str) and u.startswith("https://")]
        if lst:
            return lst
        if _CACHE["error"] is None:
            _CACHE["error"] = f"grupo '{grupo}' vacío o sin URLs https"
    return list(_POR_DEFECTO.get(grupo, _POR_DEFECTO["latest"]))


def todos():
    vistos = []
    for g in ("latest", "archivo"):
        for u in rpcs(g):
            if u not in vistos:
                vistos.append(u)
    return vistos


def _sesion():
    # una Session POR HILO (/code-review 12-Oct): reutiliza TLS sin compartir el pool entre hilos
    if not hasattr(_TLS, "s"):
        _TLS.s = requests.Session()
    return _TLS.s


def _post(url, metodo, params, timeout):
    r = _sesion().post(url, json={"jsonrpc": "2.0", "id": 1, "method": metodo, "params": params}, timeout=timeout)
    if r.status_code in _HTTP_POLITICA:
        raise RechazoPolitica(f"HTTP {r.status_code}")
    if r.status_code == 429:
        raise LimiteTemporal("HTTP 429")
    r.raise_for_status()
    j = r.json()
    if "error" in j:
        err = str(j["error"]).lower()
        if any(k in err for k in _TEXTO_POLITICA):
            raise RechazoPolitica(str(j["error"]))
        if any(k in err for k in _TEXTO_LIMITE):
            raise LimiteTemporal(str(j["error"]))
        raise RuntimeError(j["error"])
    return j["result"]


def llamar(metodo, params, grupo="latest", intentos=3, timeout=(5, 30), plazo_total_s=None, validar=None,
           lista=None, log=print):
    """Prueba cada RPC del grupo en orden. En cada uno hasta `intentos` reintentos, salvo RechazoPolitica (salta al
    siguiente). `validar(resultado) -> bool`: un resultado no válido (p. ej. "0x" de un nodo podado) pasa al
    siguiente RPC. `plazo_total_s`: no se empieza un intento nuevo pasado ese plazo (el que está en vuelo lo acota
    su timeout, así que el peor caso es plazo + un timeout). Lanza la última excepción si no hay respuesta válida."""
    t0, ultimo = time.monotonic(), None
    for url in (lista or rpcs(grupo)):
        for i in range(intentos):
            if plazo_total_s is not None and time.monotonic() - t0 >= plazo_total_s:
                raise ultimo or TimeoutError(f"plazo total {plazo_total_s}s agotado")
            try:
                res = _post(url, metodo, params, timeout)
                if validar is not None and not validar(res):
                    ultimo = RuntimeError(f"resultado no válido de {url}: {str(res)[:60]}")
                    break
                return res
            except RechazoPolitica as e:
                ultimo = e
                break
            except Exception as e:
                ultimo = e
                if i < intentos - 1:
                    if log:
                        log(f"  reintento {metodo} ({url}): {type(e).__name__}: {str(e)[:150]}")
                    time.sleep(min(2 * (i + 1), 5))
    raise ultimo or RuntimeError("sin RPCs configurados")


def hex_valido(res) -> bool:
    return isinstance(res, str) and res.startswith("0x") and len(res) > 2
