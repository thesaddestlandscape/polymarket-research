#!/usr/bin/env python3
"""
tennis_spread_observer_fase0.py — FASE 0, solo observación, sin dinero real.

Origen (02-Sep, petición explícita Javi): un bot externo real (0x1cba55...,
verificado en polymarket.com/@..., de 500$ en agosto a 46k$) hace maker de
dos lados sobre TODO el universo de tenis (cuadro principal + clasificatorios
+ challengers ITF) capturando spread + rewards de liquidez de Polymarket
(`rewardsMinSize`/`rewardsMaxSpread`), sin ninguna ventaja direccional
(win-rate ~50%). Verificado en vivo el mismo día vía gamma-api que el
mecanismo es real: challengers ITF con bestBid=None/bestAsk=0.01-0.02
(spread brutal, permanente) y `rewardsMinSize` de 20 a 1000 shares según
el mercado.

Bloqueado HOY por bankroll (10,65$ reales compartidos entre los 3 modelos,
ver [[idea_lp_farming_rewards_polymarket_22jul]] P21 -- ni cubre una sola
cotización de un solo challenger). Este observador NO opera nada -- solo
acumula el dataset (spread real, profundidad, rewards params) por partido
de tenis 24/7, para que el día que el bankroll de sports lo permita, la
decisión de pilotar se tome con semanas de datos reales, no con la
foto de un solo día.

Qué mide, cada ciclo (poll cada 180s -- los spreads de challengers no
cambian en segundos como cripto, no hace falta más frecuencia y ahorra
CPU/red en un VPS ya sobresuscrito):
  - Todos los eventos abiertos tag_slug=tennis (paginado, gamma-api).
  - Por cada mercado NO cerrado con libro real (bestBid/bestAsk presentes):
    spread absoluto, rewardsMinSize, rewardsMaxSpread, volumeNum,
    categoría aproximada por texto (Challenger/ITF/Qualification/Grand Slam/
    Doubles/otro) -- desagregación exigida por CLAUDE.md pt.17, igual que
    cripto por activo.
  - Un mercado con `rewardsMaxSpread>0` y spread real DENTRO de esa banda
    ya sería "cotizable ahora mismo con rewards" -- se marca en
    `elegible_rewards_hoy` para no tener que recalcularlo después a mano.

100% observacional. No coloca, no cancela, no importa nada de live_trade.py
ni de sports_live_trade.py.
"""
import asyncio
import csv
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

GAMMA = "https://gamma-api.polymarket.com"
TIMEOUT = 20
POLL_S = 180

CSV_COLS = [
    "timestamp_utc", "event_title", "market_id", "condition_id", "question",
    "categoria", "closed", "active", "best_bid", "best_ask", "spread",
    "rewards_min_size", "rewards_max_spread", "volume_num",
    "elegible_rewards_hoy",
]


def _log(msg: str, *extra) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    linea = f"[{ts}] {msg}"
    if extra:
        linea += " " + " ".join(str(e) for e in extra)
    print(linea, flush=True)


_GRAND_SLAMS = ("us open", "australian open", "roland garros", "wimbledon")


def _categoria(event_title: str, question: str) -> str:
    """02-Sep, corregido tras auditar 4510 filas reales: los challengers/ITF
    NO llevan la palabra "challenger"/"itf" en el título -- se identifican
    por nombre de ciudad + torneo (ej. "Geneva Open: X vs Y", igual que las
    ciudades citadas por Javi: Manacor/Porto/Plovdiv/Como/Zhangjiagang).
    El patrón real es "¿tiene ' vs ' un partido cabeza a cabeza?" -- eso
    distingue partido real (maker de dos lados tiene sentido) de
    futuros/props (ranking, retirada, awards -- otro tipo de mercado)."""
    t = f"{event_title} {question}".lower()
    es_partido = " vs " in t or " vs. " in t
    if "doubles" in t:
        return "doubles"
    if not es_partido:
        return "props_futuros"
    if "qualification" in t or "qualifying" in t or "clasificat" in t:
        return "qualifier"
    if any(gs in t for gs in _GRAND_SLAMS):
        return "grand_slam_main_draw"
    return "challenger_itf_tour"


def fetch_eventos_tenis() -> list:
    eventos, offset = [], 0
    while True:
        r = requests.get(f"{GAMMA}/events", timeout=TIMEOUT, params={
            "tag_slug": "tennis", "closed": "false", "limit": 100, "offset": offset})
        r.raise_for_status()
        batch = r.json()
        eventos += batch
        if len(batch) < 100:
            return eventos
        offset += 100


def ciclo() -> int:
    eventos = fetch_eventos_tenis()
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    path = DIR_SHADOW / f"tennis_spread_fase0_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.csv"
    nuevo = not path.exists()
    n_filas = 0
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CSV_COLS)
        if nuevo:
            w.writeheader()
        for ev in eventos:
            event_title = ev.get("title", "")
            for mk in ev.get("markets", []):
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
                w.writerow({
                    "timestamp_utc": ts,
                    "event_title": event_title,
                    "market_id": mk.get("id", ""),
                    "condition_id": mk.get("conditionId", ""),
                    "question": mk.get("question", ""),
                    "categoria": _categoria(event_title, mk.get("question", "")),
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
    _log(f"tennis_spread_observer_fase0 arrancando (poll {poll_s}s)")
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
