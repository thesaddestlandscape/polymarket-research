"""Adaptador Data API v2 -> forma v1 (camelCase, listas planas). v1 retirada 24-Oct-2026.
Uso: data_api.get("trades", {"user": w, "limit": 100}) devuelve lo mismo que el v1 /trades.
Fail-closed: cualquier error HTTP/forma inesperada lanza excepción (nunca lista vacía)."""
import re
import requests

BASE = "https://data-api.polymarket.com"
_ALIAS = {"token_id": "asset", "opposite_token_id": "oppositeAsset",
          # /v2/positions: nombres distintos a v1 (verificado 01-Nov)
          "current_size": "size", "total_pnl": "cashPnl", "total_cost_usdc": "initialValue",
          "total_size": "totalBought", "current_price": "curPrice", "avg_price": "avgPrice",
          # /v2/leaderboard
          "user_id": "proxyWallet", "user_name": "userName", "volume": "vol", "x_username": "xUsername"}
_RUTAS = {"trades", "activity", "positions", "value", "oi", "holders", "live-volume", "leaderboard"}


def _camel(k: str) -> str:
    if k in _ALIAS:
        return _ALIAS[k]
    return re.sub(r"_([a-z0-9])", lambda m: m.group(1).upper(), k)


def _conv(x):
    if isinstance(x, dict):
        return {_camel(k): _conv(v) for k, v in x.items()}
    if isinstance(x, list):
        return [_conv(v) for v in x]
    return x


def get(ruta: str, params: dict | None = None, timeout: float = 15, paginas: int = 1):
    """ruta sin prefijo ('trades', 'activity', 'positions', 'leaderboard'...).
    `market` -> `condition`; `offset` no existe en v2 (>0 se pagina por cursor)."""
    if ruta not in _RUTAS:
        raise ValueError(f"ruta no migrada: {ruta}")
    p = dict(params or {})
    if "market" in p:
        p["condition"] = p.pop("market")
    # v1 `redeemable=true|false` -> v2 `status`; el OPEN de v2 incluye redimibles: filtrar en cliente
    if ruta == "trades":
        p.setdefault("taker_only", "true")   # v1 devolvía solo tomadoras; v2 por defecto mezcla maker (verificado 01-Nov: 15 vs 77)
    red = p.pop("redeemable", None) if ruta == "positions" else None
    if red is not None:
        red = str(red).lower() == "true"
        p["status"] = "REDEEMABLE" if red else "OPEN"
    off = int(p.pop("offset", 0) or 0)
    lim = min(int(p.get("limit", 100)), 1000)   # v2: limit 0..1000
    p["limit"] = lim
    if ruta == "positions":
        paginas = max(paginas, 10)   # el filtro de cliente puede vaciar páginas: seguir hasta agotar
    out, cursor, saltar = [], None, off
    for _ in range(max(paginas, 1) + (off // max(lim, 1) + 1 if off else 0)):
        q = dict(p, **({"cursor": cursor} if cursor else {}))
        r = requests.get(f"{BASE}/v2/{ruta}", params=q, timeout=timeout)
        r.raise_for_status()
        j = r.json()
        if not isinstance(j, dict) or "data" not in j:
            raise ValueError(f"forma v2 inesperada en {ruta}")
        d = j["data"]
        if d is None and ruta == "value":
            raise ValueError("value: data null (fail-closed)")
        rows = d if isinstance(d, list) else ([] if d is None else [d])
        if saltar >= len(rows) and saltar:
            saltar -= len(rows)
        else:
            out.extend(rows[saltar:]); saltar = 0
        cursor = (j.get("pagination") or {}).get("next_cursor")
        if not cursor or (not saltar and len(out) >= lim * max(paginas, 1)):
            break
    else:
        if saltar:
            raise ValueError(f"{ruta}: offset {off} no alcanzado (paginas insuficientes)")
    if saltar:
        raise ValueError(f"{ruta}: offset {off} más allá del final de la paginación")
    if ruta == "positions":
        # v1 aplicaba sizeThreshold=1 por defecto; v2 no
        umbral = float(p.get("sizeThreshold", 1))
        out = [x for x in out if (x.get("current_size") or 0) >= umbral]
        if red is not None:
            out = [x for x in out if bool(x.get("redeemable")) == red]
    return _conv(out)


class _Resp:
    """Compat con requests.Response para scripts que hacen r.json()/r.status_code."""
    status_code = 200
    def __init__(self, data): self._d = data
    def json(self): return self._d
    def raise_for_status(self): pass
    @property
    def text(self): return __import__("json").dumps(self._d)


def resp(ruta: str, params: dict | None = None, timeout: float = 15, headers=None):
    """Sustituto directo de requests.get(f"{DATA_API}/{ruta}", params=..., timeout=...)."""
    return _Resp(get(ruta, params, timeout))
