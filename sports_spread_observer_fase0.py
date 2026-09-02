#!/usr/bin/env python3
"""
sports_spread_observer_fase0.py — FASE 0, solo observación, sin dinero real.

Origen (02-Sep, petición explícita Javi): un bot externo real (0x1cba55...,
verificado en polymarket.com/@..., de 500$ en agosto a 46k$) hace maker de
dos lados sobre el universo de tenis (cuadro principal + clasificatorios +
challengers ITF) capturando spread + rewards de liquidez de Polymarket
(`rewardsMinSize`/`rewardsMaxSpread`), sin ninguna ventaja direccional
(win-rate ~50%).

02-Sep, misma noche, corrección de alcance (Javi: "¿por qué lo haces solo
sobre tenis?"): el mecanismo (rewards de liquidez + spread) NO es
específico de tenis, existe en TODAS las categorías de sports de
Polymarket -- tenis es solo donde vive ESE bot concreto porque tiene
volumen enorme de partidos de bajo perfil con libros vacíos. Restringir
el observador a tenis dejaba fuera exactamente el mismo hueco potencial en
CS/LoL/Dota/UFC/cricket/fútbol de ligas menores. Generalizado a TODO
sports reutilizando `clasificar()` de `sports_wallet_edge_tracker.py`
(misma taxonomía ya validada por el resto del stack de sports, 25+
categorías + fallback Soccer-<liga> por slug).

Verificado en vivo el mismo día: `tag_slug=sports` (umbrella de gamma-api)
da 2.100 eventos abiertos (CS 358, MLB 50, LoL 42, Dota 19, NBA 18, UFC 18,
Cricket 14, WNBA 11...) pero SUBCLASIFICA tenis (solo 7 vía `clasificar()`,
porque títulos tipo "Australian Open Women's: X vs Y" no llevan
"ATP/WTA/ITF/tennis" literal) -- tenis vive mayormente FUERA de la etiqueta
"sports" en gamma-api. Por eso se combinan 2 fuentes (`tag_slug=sports` +
`tag_slug=tennis`, deduplicadas por market_id) en vez de fiarse de una sola.

Bloqueado HOY por bankroll (10,65$ reales compartidos entre los 3 modelos,
ver [[idea_lp_farming_rewards_polymarket_22jul]] P21 -- ni cubre una sola
cotización de un solo mercado con `rewardsMinSize` real). Este observador
NO opera nada -- solo acumula el dataset (spread real, rewards params) por
partido 24/7, para que el día que el bankroll de sports lo permita, la
decisión de pilotar se tome con semanas de datos reales, no con la foto de
un solo día.

Qué mide, cada ciclo (poll cada 240s -- ahora 2 fuentes paginadas en vez de
1, sigue siendo barato en CPU/red, pero sin necesidad de más frecuencia:
los spreads de partidos de bajo perfil no cambian en segundos como cripto):
  - Todos los eventos abiertos de `tag_slug=sports` + `tag_slug=tennis`
    (paginado, gamma-api, deduplicados por market_id).
  - Por cada mercado NO cerrado con libro real (bestBid/bestAsk presentes):
    spread absoluto, rewardsMinSize, rewardsMaxSpread, volumeNum,
    categoría vía `clasificar()` (UFC/NBA/MLB/CS/LoL/Tennis/Soccer-<liga>/
    etc, CLAUDE.md pt.17) con fallback propio ("vs" en el título = partido
    real head-to-head aunque el regex compartido no lo reconozca; sin "vs"
    = props/futuros, otro tipo de mercado).
  - Un mercado con `rewardsMaxSpread>0` y spread real DENTRO de esa banda
    ya sería "cotizable ahora mismo con rewards" -- se marca en
    `elegible_rewards_hoy` para no tener que recalcularlo después a mano.

100% observacional. No coloca, no cancela, no importa nada de live_trade.py
ni de sports_live_trade.py.
"""
import asyncio
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
DIR_SHADOW = REPO / "data" / "shadow"
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

from sports_wallet_edge_tracker import clasificar  # noqa: E402

GAMMA = "https://gamma-api.polymarket.com"
TIMEOUT = 20
POLL_S = 240
TAG_SLUGS = ["sports", "tennis"]  # "sports" = umbrella (CS/LoL/Dota/NBA/UFC/
# Cricket/etc); "tennis" dedicado porque el umbrella subclasifica tenis
# (verificado 02-Sep, ver docstring). Ampliar aquí si una auditoría futura
# encuentra otra categoría con el mismo hueco (mismo patrón que
# vigia_sports_categoria_sin_clasificar.py -- vigilar "otro_partido_sin_categoria").

CSV_COLS = [
    "timestamp_utc", "event_title", "market_id", "condition_id", "question",
    "categoria", "fuente_tag", "closed", "active", "best_bid", "best_ask",
    "spread", "rewards_min_size", "rewards_max_spread", "volume_num",
    "elegible_rewards_hoy",
]


def _log(msg: str, *extra) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    linea = f"[{ts}] {msg}"
    if extra:
        linea += " " + " ".join(str(e) for e in extra)
    print(linea, flush=True)


def _categoria(event_title: str, event_slug: str, question: str) -> str:
    """Primero la taxonomía compartida (`clasificar()`, ya validada por el
    resto del stack de sports). Si no reconoce el título (hueco real, ver
    docstring del módulo), heurística propia: "vs" en el título = partido
    real head-to-head (maker de dos lados tiene sentido aunque no sepamos
    el deporte exacto) vs prop/futuro (otro tipo de mercado, no aplica)."""
    cat = clasificar(event_title, event_slug) or clasificar(question, event_slug)
    if cat:
        return cat
    t = f"{event_title} {question}".lower()
    if " vs " in t or " vs. " in t:
        if "doubles" in t:
            return "partido_dobles_sin_categoria"
        if "qualification" in t or "qualifying" in t or "clasificat" in t:
            return "partido_clasificatorio_sin_categoria"
        return "partido_sin_categoria_regex"
    return "props_futuros"


def fetch_eventos_sports() -> list:
    """Combina TAG_SLUGS, deduplicado por market_id (un mismo evento puede
    aparecer bajo varios tags). Tolera que gamma-api devuelva un objeto de
    error (dict) en vez de una lista al superar su offset máximo interno
    -- corta esa fuente y sigue con las demás, en vez de reventar."""
    vistos_market_id = set()
    filas = []
    for slug in TAG_SLUGS:
        offset = 0
        while True:
            try:
                r = requests.get(f"{GAMMA}/events", timeout=TIMEOUT, params={
                    "tag_slug": slug, "closed": "false", "limit": 100, "offset": offset})
                r.raise_for_status()
                batch = r.json()
            except Exception as e:
                _log(f"⚠ fetch tag={slug} offset={offset} falló: {type(e).__name__}: {e}")
                break
            if not isinstance(batch, list) or (batch and not isinstance(batch[0], dict)):
                break  # gamma-api devolvió un error/objeto al pasar su offset máximo
            for ev in batch:
                for mk in ev.get("markets", []):
                    mid = mk.get("id", "")
                    if not mid or mid in vistos_market_id:
                        continue
                    vistos_market_id.add(mid)
                    filas.append((ev, mk, slug))
            if len(batch) < 100:
                break
            offset += 100
    return filas


def ciclo() -> int:
    filas_raw = fetch_eventos_sports()
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    path = DIR_SHADOW / f"sports_spread_fase0_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.csv"
    nuevo = not path.exists()
    n_filas = 0
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLS)
        if nuevo:
            w.writeheader()
        for ev, mk, fuente_tag in filas_raw:
            if mk.get("closed"):
                continue
            bid = mk.get("bestBid")
            ask = mk.get("bestAsk")
            if bid is None and ask is None:
                continue
            try:
                bid_f = float(bid) if bid is not None else None
                ask_f = float(ask) if ask is not None else None
            except (TypeError, ValueError):
                continue
            spread = round(ask_f - bid_f, 4) if (bid_f is not None and ask_f is not None) else None
            rewards_min = mk.get("rewardsMinSize") or 0
            rewards_max_spread = mk.get("rewardsMaxSpread") or 0
            elegible = bool(
                rewards_max_spread and spread is not None
                and spread * 100 <= float(rewards_max_spread)
            )
            event_title = ev.get("title", "")
            w.writerow({
                "timestamp_utc": ts,
                "event_title": event_title,
                "market_id": mk.get("id", ""),
                "condition_id": mk.get("conditionId", ""),
                "question": mk.get("question", ""),
                "categoria": _categoria(event_title, ev.get("slug", ""), mk.get("question", "")),
                "fuente_tag": fuente_tag,
                "closed": mk.get("closed", False),
                "active": mk.get("active", False),
                "best_bid": bid_f,
                "best_ask": ask_f,
                "spread": spread,
                "rewards_min_size": rewards_min,
                "rewards_max_spread": rewards_max_spread,
                "volume_num": mk.get("volumeNum", 0),
                "elegible_rewards_hoy": elegible,
            })
            n_filas += 1
    return n_filas


async def main_async(poll_s: int = POLL_S) -> None:
    _log(f"sports_spread_observer_fase0 arrancando (poll {poll_s}s, tags={TAG_SLUGS})")
    while True:
        try:
            n = ciclo()
            _log(f"ciclo OK — {n} filas escritas")
        except Exception as e:
            _log(f"🚨 error en ciclo: {type(e).__name__}: {e}")
        await asyncio.sleep(poll_s)


def main() -> int:
    asyncio.run(main_async())
    return 0


if __name__ == "__main__":
    sys.exit(main())
