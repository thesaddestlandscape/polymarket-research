#!/usr/bin/env python3
"""
ladder_arb_weather_fase0.py — FASE 0, solo observación: vigila la suma
bid/ask de cada "escalera" de temperatura (mercados de weather de
Polymarket, gamma-api pública) buscando arbitraje libre real.

Origen (27-Ago, idea_ronda2_propuestas_profundas_27ago, sección 1):
los mercados de temperatura NO son ventanas anidadas (como cripto) sino
una escalera de strikes MUTUAMENTE EXCLUYENTES Y EXHAUSTIVOS para el
mismo día/ciudad (ej. "23c-or-below, 24c, 25c, ..., 33c-or-higher").
Como exactamente uno gana, la suma de precios YES de TODA la escalera
debería ser ~1 (menos fees) en todo momento -- mismo principio que
nested_arb_scanner.py en cripto, aplicado aquí a otra estructura.
Verificado en vivo 27-Ago sobre Munich (11 strikes): suma bestAsk=1.10,
suma bestBid=0.972 -- spread 12.8pp, SIN arb libre ese día concreto. La
memoria pide un scanner que vigile esto periódicamente por si el spread
se estrecha (menos competencia de MM que cripto, según hallazgo #7 de
la ronda 1) -- este script es ESO, nunca construido hasta hoy (01-Sep,
CLAUDE.md pt.21b propuesta #8).

⚠️ NO toca el repo /root/polymarket-weather (CLAUDE.md: sistema
independiente, no mezclar) -- esto lee ÚNICAMENTE la API pública de
Polymarket (gamma-api), igual que nested_arb_scanner.py o
box_builder_fase0.py ya hacen para cripto. No requiere ninguna wallet ni
lógica interna del bot de weather.

Descubrimiento: `gamma-api.polymarket.com/public-search?q=highest
temperature&events_status=active` (paginado) -- devuelve eventos con su
lista de `markets` (cada uno YA trae bestBid/bestAsk, sin llamada extra
al CLOB). Verificado en vivo: 156 resultados totales (decenas de
ciudades × varios días), cada evento con 11 mercados (strikes) en los
casos comprobados.

Solo observación, cero ejecución, cero dinero. Cron cada 15min (los
mercados de temperatura se mueven mucho más lento que cripto -- no hace
falta cadencia de segundos).

Salida: data/shadow/ladder_arb_weather_fase0.csv
"""

import csv
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
DIR_SHADOW = REPO / "data" / "shadow"

SEARCH_URL = "https://gamma-api.polymarket.com/public-search"
QUERY = "highest temperature"
LIMIT_POR_PAGINA = 50
MAX_PAGINAS = 6  # techo de seguridad -- 156 resultados vistos hoy, cabe en 4 páginas de 50
TIMEOUT_S = 15

OUT = DIR_SHADOW / "ladder_arb_weather_fase0.csv"
COLUMNS = [
    "timestamp_utc", "evento_titulo", "evento_slug", "neg_risk_market_id",
    "n_strikes", "n_sin_ask", "n_sin_bid", "suma_bestask", "suma_bestbid", "spread_pp",
    "arb_comprar_libre", "arb_vender_libre",
]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _descubrir_eventos() -> list:
    """Todos los eventos activos de escalera de temperatura, paginado."""
    eventos = []
    offset = 0
    for _ in range(MAX_PAGINAS):
        try:
            r = requests.get(SEARCH_URL, params={
                "q": QUERY, "events_status": "active",
                "limit_per_type": LIMIT_POR_PAGINA, "offset": offset,
            }, timeout=TIMEOUT_S)
            r.raise_for_status()
            data = r.json()
        except Exception as e:
            _log(f"WARN: fallo consultando public-search (offset={offset}): {type(e).__name__}: {e}")
            break
        lote = data.get("events", [])
        eventos.extend(lote)
        if not data.get("pagination", {}).get("hasMore") or not lote:
            break
        offset += LIMIT_POR_PAGINA
    return eventos


def _procesar_evento(ev: dict) -> dict | None:
    markets = ev.get("markets") or []
    if len(markets) < 2:
        return None  # no es una escalera de verdad (ej. 1 solo mercado binario)
    asks, bids = [], []
    n_sin_ask = n_sin_bid = 0
    neg_risk_ids = set()
    for m in markets:
        try:
            ba = float(m.get("bestAsk"))
        except (TypeError, ValueError):
            ba = None
        try:
            bb = float(m.get("bestBid"))
        except (TypeError, ValueError):
            bb = None
        # Strike sin bid = nadie compra ahí (bid efectivo 0, no descarta el
        # evento -- normal en strikes muy improbables). Strike sin ask = nadie
        # vende ahí -- se trata como 1.0 (no comprable barato), así que un
        # hueco de liquidez real NUNCA produce un falso "arb_comprar_libre".
        asks.append(ba if ba is not None else 1.0)
        bids.append(bb if bb is not None else 0.0)
        if ba is None:
            n_sin_ask += 1
        if bb is None:
            n_sin_bid += 1
        nrid = m.get("negRiskMarketID")
        if nrid:
            neg_risk_ids.add(nrid)
    suma_ask = round(sum(asks), 4)
    suma_bid = round(sum(bids), 4)
    return {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "evento_titulo": ev.get("title", ""),
        "evento_slug": ev.get("slug", ""),
        "neg_risk_market_id": next(iter(neg_risk_ids), "") if len(neg_risk_ids) == 1 else "MULTIPLE",
        "n_strikes": len(markets),
        "n_sin_ask": n_sin_ask,
        "n_sin_bid": n_sin_bid,
        "suma_bestask": suma_ask,
        "suma_bestbid": suma_bid,
        "spread_pp": round((suma_ask - suma_bid) * 100, 2),
        # arb_comprar_libre: comprar TODA la escalera (garantiza $1) cuesta
        # menos de $1 -- arb real, comprando al ask. Exige ask real en TODOS
        # los strikes (n_sin_ask==0) -- si falta uno, no se puede ejecutar
        # de verdad aunque la suma con el 1.0 de relleno dé <1.
        "arb_comprar_libre": int(suma_ask < 1.0 and n_sin_ask == 0),
        # arb_vender_libre: vender TODA la escalera (garantiza pagar $1 al
        # resolver) da MÁS de $1 de ingreso -- arb real, vendiendo al bid.
        # Exige bid real en TODOS los strikes (n_sin_bid==0).
        "arb_vender_libre": int(suma_bid > 1.0 and n_sin_bid == 0),
    }


def _guardar(filas: list) -> None:
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)


def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    t0 = time.time()
    eventos = _descubrir_eventos()
    filas = []
    for ev in eventos:
        fila = _procesar_evento(ev)
        if fila:
            filas.append(fila)
    _guardar(filas)
    arbs = [f for f in filas if f["arb_comprar_libre"] or f["arb_vender_libre"]]
    _log(f"{len(eventos)} eventos descubiertos, {len(filas)} escaleras procesadas, "
         f"{len(arbs)} con arb libre AHORA MISMO ({time.time()-t0:.1f}s)")
    if arbs:
        for a in arbs:
            _log(f"  🚨 ARB: {a['evento_titulo']} ask_sum={a['suma_bestask']} bid_sum={a['suma_bestbid']}")


if __name__ == "__main__":
    main()
