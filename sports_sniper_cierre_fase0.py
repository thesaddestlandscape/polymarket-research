#!/usr/bin/env python3
"""sports_sniper_cierre_fase0.py -- FASE 0 (solo lectura, NUNCA orden real), 29-Sep.

Ronda 1 #6 de las 30 propuestas 28-Sep: "Sniper fin de partido sports —
partido terminado, mercado abierto hasta UMA, ganador a 0,97-0,99. Riesgos:
capital bloqueado, disputas." Paso 1 pedido: firehose + tiempo fin→resolución
y precio en el hueco.

Mide, para cada mercado de deportes cuyo end_date YA pasó pero sigue
`closed=false` (evento terminado, resultado casi seguro pero UMA todavía
no ha asentado):
  - precio actual del lado ganador (ask real, no solo mid) -- el "hueco"
    de rentabilidad si se compra ahora y se espera a la resolución.
  - `expected_settlement_time`/`settlement_time_basis` de
    GET /v2/resolutions (campo NUEVO, 28-Sep -- ver idea_settlement_
    estimates_v2_resolutions_29sep en memoria) -- estimación de CUÁNTO
    tiempo va a estar bloqueado el capital, algo que antes no se podía
    saber sin adivinar.
  - tiempo REAL hasta que el mercado desaparece de `closed=false` (se
    recalcula cada corrida sobre los mismos market_id ya vistos -- el
    dato de verdad para contrastar contra la estimación de la API).

Clasificación de deporte reutiliza sports_wallet_edge_tracker.clasificar()
(misma fuente de verdad que el resto del proyecto de sports, NUNCA una
lista nueva) -- NO se usa el tag_slug=sports de gamma-api porque está
devolviendo resultados mezclados con cripto/weather (verificado 29-Sep).

Solo lectura -- nunca coloca, cancela ni modifica ninguna orden real.

Cron sugerido: cada 10min (no es latencia-crítico, el fenómeno dura
horas/días).
"""
import csv
import json
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from sports_wallet_edge_tracker import clasificar  # noqa: E402

GAMMA = "https://gamma-api.polymarket.com"
DATA_API = "https://data-api.polymarket.com"
CLOB_BOOK = "https://clob.polymarket.com/book"

VENTANA_PASADO_H = 96      # solo mercados terminados en las últimas 96h (más allá, ya lo cubre el resolver aparte)
PRECIO_GANADOR_MIN = 0.90  # "ganador casi seguro" -- mismo umbral cualitativo que describe la propuesta

OUT = REPO / "data" / "shadow" / "sports_sniper_cierre_fase0.csv"
CAMPOS = ["timestamp_utc", "condition_id", "event_slug", "question", "categoria",
          "end_date", "horas_desde_fin", "precio_ganador_actual", "ask_real_ganador",
          "resolutions_status", "was_disputed", "extended_review",
          "expected_settlement_time", "settlement_time_basis",
          "primera_vez_visto_utc", "resuelto_en_esta_corrida"]

_SESSION = requests.Session()
_VISTOS_PATH = REPO / "data" / "shadow" / "sports_sniper_cierre_fase0_vistos.json"


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _cargar_vistos() -> dict:
    try:
        return json.loads(_VISTOS_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def _guardar_vistos(d: dict) -> None:
    _VISTOS_PATH.write_text(json.dumps(d), encoding="utf-8")


def _mercados_terminados_no_cerrados() -> list:
    ahora = datetime.now(timezone.utc)
    corte_atras = ahora - timedelta(hours=VENTANA_PASADO_H)
    mercados = []
    offset = 0
    while offset < 1000:
        try:
            r = _SESSION.get(f"{GAMMA}/markets", params={
                "closed": "false", "limit": 100, "offset": offset,
                "order": "endDate", "ascending": "false",
                "end_date_max": ahora.strftime("%Y-%m-%dT%H:%M:%SZ"),
            }, timeout=15)
            r.raise_for_status()
            lote = r.json()
        except Exception as e:
            _log(f"error listando mercados (offset={offset}): {e}")
            break
        if not lote:
            break
        parada = False
        for m in lote:
            ed_raw = m.get("endDate")
            if not ed_raw:
                continue
            try:
                ed = datetime.fromisoformat(ed_raw.replace("Z", "+00:00"))
            except Exception:
                continue
            if ed < corte_atras:
                parada = True
                break
            mercados.append((m, ed))
        offset += 100
        if parada:
            break
    return mercados


def _resolutions(condition_id: str) -> dict | None:
    try:
        r = _SESSION.get(f"{DATA_API}/v2/resolutions", params={"condition": condition_id}, timeout=8)
        r.raise_for_status()
        data = r.json()
        rows = data.get("data") or []
        return rows[0] if rows else None
    except Exception:
        return None


def _mejor_ask(token_id: str) -> float | None:
    try:
        r = _SESSION.get(CLOB_BOOK, params={"token_id": token_id}, timeout=8)
        r.raise_for_status()
        asks = r.json().get("asks") or []
        if not asks:
            return None
        return min(float(a["price"]) for a in asks)
    except Exception:
        return None


def _guardar_fila(fila: dict) -> None:
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        w.writerow(fila)


def main() -> None:
    _log("sports_sniper_cierre_fase0 arrancado (solo lectura, sin órdenes reales)")
    vistos = _cargar_vistos()
    mercados = _mercados_terminados_no_cerrados()
    _log(f"{len(mercados)} mercados con end_date pasado (últimas {VENTANA_PASADO_H}h) y closed=false")

    cids_actuales = set()
    n_sports = 0
    for m, ed in mercados:
        question = m.get("question", "")
        event_slug = m.get("groupItemTitle") or m.get("slug", "")
        cat = clasificar(question, event_slug)
        if cat is None:
            continue
        n_sports += 1
        cid = m.get("conditionId", "")
        if not cid:
            continue
        cids_actuales.add(cid)

        try:
            prices = json.loads(m.get("outcomePrices") or "[]")
        except Exception:
            prices = []
        if not prices or max(float(p) for p in prices) < PRECIO_GANADOR_MIN:
            continue

        idx_ganador = max(range(len(prices)), key=lambda i: float(prices[i]))
        try:
            tokens = json.loads(m.get("clobTokenIds") or "[]")
            token_ganador = tokens[idx_ganador] if idx_ganador < len(tokens) else None
        except Exception:
            token_ganador = None
        ask_real = _mejor_ask(token_ganador) if token_ganador else None

        res = _resolutions(cid) or {}
        ahora = datetime.now(timezone.utc)

        primera_vez = vistos.get(cid)
        if primera_vez is None:
            primera_vez = ahora.isoformat(timespec="seconds")
            vistos[cid] = primera_vez

        fila = {
            "timestamp_utc": ahora.isoformat(timespec="seconds"),
            "condition_id": cid, "event_slug": event_slug, "question": question,
            "categoria": cat, "end_date": ed.isoformat(),
            "horas_desde_fin": round((ahora - ed).total_seconds() / 3600, 2),
            "precio_ganador_actual": float(prices[idx_ganador]),
            "ask_real_ganador": ask_real if ask_real is not None else "",
            "resolutions_status": res.get("status", ""),
            "was_disputed": res.get("was_disputed", ""),
            "extended_review": res.get("extended_review", ""),
            "expected_settlement_time": res.get("expected_settlement_time", ""),
            "settlement_time_basis": res.get("settlement_time_basis", ""),
            "primera_vez_visto_utc": primera_vez, "resuelto_en_esta_corrida": False,
        }
        _guardar_fila(fila)

    # cualquier condition_id que estaba en `vistos` pero YA NO aparece en la
    # lista de "terminados y closed=false" se ha resuelto (o cerrado) entre
    # esta corrida y la anterior -- registrar el momento real de desaparición
    resueltos_ahora = [cid for cid in vistos if cid not in cids_actuales]
    for cid in resueltos_ahora:
        fila = {c: "" for c in CAMPOS}
        fila.update({
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "condition_id": cid, "primera_vez_visto_utc": vistos[cid],
            "resuelto_en_esta_corrida": True,
        })
        _guardar_fila(fila)
        vistos.pop(cid, None)

    _guardar_vistos(vistos)
    _log(f"{n_sports} mercados de deportes en la ventana, "
         f"{len(resueltos_ahora)} desaparecidos (resueltos) desde la última corrida")


if __name__ == "__main__":
    main()
