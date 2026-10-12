#!/usr/bin/env python3
"""polygon_rpc.py -- UN solo punto para hablar JSON-RPC con Polygon, con failover entre RPCs públicos (12-Oct).

Por qué: el 09-Oct 08:10 publicnode empezó a responder "Archive requests require a personal token" a eth_getLogs y
fetch_polymarket_fills_onchain.py estuvo 3,5 días sin datos on-chain sin que nadie se enterase (Javi: "no podemos
permitir que esto pase de nuevo"). Los nodos gratuitos cambian de política sin avisar: no se puede garantizar que
uno no rechace; sí que (1) haya varios a los que saltar y (2) se sepa en cuanto uno empieza a fallar
(vigia_polygon_rpc.py, cada hora, prueba TODOS con las tres llamadas que usa el sistema).

Uso: from polygon_rpc import llamar, RPCS ;  llamar("eth_blockNumber", [])
Lista probada el 12-Oct con eth_getLogs de archivo (bloque de 3,5 días atrás): publicnode NO (pide token);
drpc, 1rpc, tenderly y quiknode SÍ. Orden = preferencia; publicnode se mantiene primero para las llamadas
"latest" (rápido y sin límite), y para archivo se salta al siguiente en cuanto pide token.
"""
import time

import requests

RPCS = [
    "https://polygon-bor-rpc.publicnode.com",
    "https://polygon.drpc.org",
    "https://1rpc.io/matic",
    "https://gateway.tenderly.co/public/polygon",
    "https://rpc-mainnet.matic.quiknode.pro",
]
_SESION = requests.Session()


def _es_rechazo_politica(e) -> bool:
    t = str(e).lower()
    return any(k in t for k in ("archive requests", "personal token", "api key", "unauthorized", "forbidden",
                                "rate limit", "too many requests", "429", "401", "403"))


def llamar(metodo, params, intentos=3, timeout=60, rpcs=None, log=print):
    """Prueba cada RPC en orden; en cada uno hasta `intentos` reintentos, salvo rechazo de política (token, auth,
    límite), que salta al siguiente de inmediato. Lanza la última excepción si fallan todos."""
    ultimo = None
    for url in (rpcs or RPCS):
        for i in range(intentos):
            try:
                r = _SESION.post(url, json={"jsonrpc": "2.0", "id": 1, "method": metodo, "params": params},
                                 timeout=timeout)
                if r.status_code in (401, 403, 429):
                    raise RuntimeError(f"HTTP {r.status_code}")
                j = r.json()
                if "error" in j:
                    raise RuntimeError(j["error"])
                return j["result"]
            except Exception as e:
                ultimo = e
                if _es_rechazo_politica(e):
                    break
                if i < intentos - 1:
                    if log:
                        log(f"  reintento {metodo} ({url}): {type(e).__name__}: {str(e)[:150]}")
                    time.sleep(2 * (i + 1))
    raise ultimo
