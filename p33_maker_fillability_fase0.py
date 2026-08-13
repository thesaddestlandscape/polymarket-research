#!/usr/bin/env python3
"""
p33_maker_fillability_fase0.py -- FASE 0 (SOLO OBSERVACIÓN) del hallazgo
P33 (idea_p33_arbitraje_umbrales_precio_monotonia_12ago, corregido
13-Ago en idea_p33_refutado_fee_y_spread_real_13ago / idea_p33_maker_
fillability_fase0_13ago): mercados "Will X reach/dip to $Y by [fecha]"
tienen una relación de monotonía matemática estricta entre umbrales del
mismo evento -- cuando se viola, hay arbitraje sin modelo. Como TAKER
(cruzando el spread) el fee real (7%, feeType=crypto_fees_v2, igual que
los mercados Up/Down) mata el edge en 21/23 pares persistentes medidos
ayer. Pero estos mercados son takerOnly=True -- el MAKER no paga fee.
La pregunta que este observador responde, nunca medida: ¿se podría
llenar de verdad una orden maker que mejora el libro sin exponerse a
riesgo de pata suelta (legging)?

Mecanismo (no requiere websocket -- estos mercados son "reach $X by
diciembre 2026", se mueven en horas/días, no en segundos, a diferencia
de los Up/Down 5/15/60min):
  1. Descubre una vez al día (cache en data/shadow/p33_pares_universo.json)
     los pares (evento, dirección, umbral_bajo, umbral_alto) con
     violación de monotonía HOY, leyendo data/markets/HOY.csv (ya lo
     mantiene capture_markets.py, sin llamada de red nueva para eso --
     mismo patrón que fetch_libro_ambos_lados.py) + resuelve
     clobTokenIds de cada pata vía gamma-api.
  2. Cada POLL_INTERVAL_S, para cada par activo, consulta el libro real
     de AMBAS patas (YES del umbral bajo, NO del umbral alto) vía
     lt._fetch_book_publico (solo lectura, misma función pública que ya
     usa el resto del proyecto -- NUNCA se llama nada que ordene).
  3. Calcula el precio maker hipotético de cada pata (mejor_bid + 1
     tick, la mejora mínima que aún es maker) y lo compara contra el
     precio maker hipotético calculado en el ciclo ANTERIOR: si el
     best_ask de esa pata ha caído hasta tocar o cruzar el precio
     hipotético de antes, es la señal proxy de que una orden resting
     ahí se habría llenado (alguien vendió al nivel que ofrecíamos).
  4. Persiste cada ciclo en data/shadow/p33_maker_fillability_fase0.csv
     -- both legs, spread, precio maker hipotético, y si hubo "cruce"
     desde el ciclo anterior en cada pata por separado (para medir el
     riesgo de pata suelta: ¿se llenan las dos patas juntas o una sí y
     la otra no?).

NO coloca, cancela ni modifica ninguna orden real, no llama a ninguna
función de ejecución de live_trade.py, no toca pares_permitidos_live ni
candidatos_evaluacion_live -- puramente observacional.

Se fusiona en observadores_fase0.py (screen "observadores").
"""
import csv
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

import live_trade as lt  # solo lectura: _fetch_book_publico -- NUNCA se llama nada que ordene

REPO = Path(__file__).resolve().parent
DIR_MARKETS = REPO / "data" / "markets"
DIR_SHADOW = REPO / "data" / "shadow"
UNIVERSO_JSON = DIR_SHADOW / "p33_pares_universo.json"
OUT = DIR_SHADOW / "p33_maker_fillability_fase0.csv"

PAT = re.compile(r"\b(reach|dip to)\s*\$([\d,]+\.?\d*)", re.IGNORECASE)
POLL_INTERVAL_S = 300  # 5min -- mercados que se mueven en horas/días, no hace falta más rápido
REDESCUBRIR_CADA_S = 24 * 3600

COLUMNS = [
    "timestamp_utc", "event_title", "direccion", "umbral_bajo", "umbral_alto",
    "bid_yes_bajo", "ask_yes_bajo", "bid_no_alto", "ask_no_alto",
    "maker_hipotetico_bajo", "maker_hipotetico_alto",
    "cruce_pata_bajo", "cruce_pata_alto", "cruce_ambas_patas",
]

_log = print  # sobrescrito por observadores_fase0.py con el logger dedicado


def _archivo_hoy() -> Path:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return DIR_MARKETS / f"{fecha}.csv"


def _parsear_umbral(pregunta: str):
    m = PAT.search(pregunta)
    if not m:
        return None, None
    return m.group(1).lower(), float(m.group(2).replace(",", ""))


def _extraer_fecha_evento(pregunta: str) -> str:
    m = re.search(r"by\s+([A-Za-z]+\s+\d{1,2},?\s*\d{4}|\d{4}-\d{2}-\d{2})", pregunta)
    return m.group(1) if m else "sin_fecha"


def _resolver_token_ids(condition_id: str) -> list | None:
    try:
        r = requests.get("https://gamma-api.polymarket.com/markets",
                          params={"condition_ids": condition_id}, timeout=15)
        data = r.json()
        if not data:
            return None
        raw = data[0].get("clobTokenIds")
        return json.loads(raw) if isinstance(raw, str) else raw
    except Exception as e:
        _log(f"error resolviendo tokens de {condition_id}: {e}")
        return None


def _descubrir_pares() -> list:
    """Lee data/markets/HOY.csv (solo columnas necesarias, filtrado por
    texto antes de cargar a memoria -- ese fichero pesa cientos de MB),
    detecta violaciones de monotonía vigentes hoy, resuelve tokens."""
    path = _archivo_hoy()
    cols = ["market_id", "condition_id", "question", "liquidity", "price_yes",
            "event_id", "event_title"]
    chunks = []
    for chunk in pd.read_csv(path, usecols=cols, chunksize=200_000, on_bad_lines="skip"):
        mask = chunk["question"].str.contains(r"(reach|dip to)\s*\$", case=False,
                                                regex=True, na=False)
        if mask.any():
            chunks.append(chunk[mask])
    if not chunks:
        return []
    df = pd.concat(chunks, ignore_index=True).drop_duplicates("market_id", keep="last")
    df["direccion"], df["umbral"] = zip(*df["question"].map(_parsear_umbral))
    df = df.dropna(subset=["direccion", "umbral"])
    df["fecha_evento"] = df["question"].map(_extraer_fecha_evento)

    pares = []
    for (event_id, direccion, fecha_evento), grupo in df.groupby(
            ["event_id", "direccion", "fecha_evento"]):
        grupo = grupo.sort_values("umbral")
        filas = grupo.to_dict("records")
        for i in range(len(filas) - 1):
            a, b = filas[i], filas[i + 1]
            if direccion == "reach":
                viola = b["price_yes"] > a["price_yes"]
            else:
                viola = b["price_yes"] < a["price_yes"]
            if not viola:
                continue
            tokens_a = _resolver_token_ids(a["condition_id"])
            tokens_b = _resolver_token_ids(b["condition_id"])
            if not tokens_a or not tokens_b or len(tokens_a) < 2 or len(tokens_b) < 2:
                continue
            pares.append({
                "event_title": a["event_title"], "direccion": direccion,
                "umbral_bajo": a["umbral"], "umbral_alto": b["umbral"],
                "token_yes_bajo": tokens_a[0],  # [YES, NO] -- confirmado orden gamma-api
                "token_no_alto": tokens_b[1],
            })
    return pares


def _cargar_o_descubrir_pares() -> list:
    if UNIVERSO_JSON.exists():
        try:
            data = json.loads(UNIVERSO_JSON.read_text())
            edad_s = time.time() - data.get("_generado_ts", 0)
            if edad_s < REDESCUBRIR_CADA_S:
                return data["pares"]
        except Exception:
            pass
    pares = _descubrir_pares()
    UNIVERSO_JSON.write_text(json.dumps(
        {"_generado_ts": time.time(), "pares": pares}, indent=1, ensure_ascii=False))
    _log(f"universo redescubierto: {len(pares)} pares con violación de monotonía hoy")
    return pares


def _mejor_bid_ask(token_id: str):
    book = lt._fetch_book_publico(token_id)
    if book is None:
        return None, None
    bids = book.get("bids") or []
    asks = book.get("asks") or []
    if not bids or not asks:
        return None, None
    mejor_bid = max(float(b["price"]) for b in bids)
    mejor_ask = min(float(a["price"]) for a in asks)
    return mejor_bid, mejor_ask


def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    nuevo = not OUT.exists()
    pares = _cargar_o_descubrir_pares()
    _log(f"arrancado -- {len(pares)} pares en seguimiento, poll cada {POLL_INTERVAL_S}s")
    ultimo_maker = {}  # (event_title, umbral_bajo, umbral_alto) -> (hipotetico_bajo, hipotetico_alto)
    ultimo_redescubrimiento = time.time()

    with open(OUT, "a", newline="") as fh:
        writer = csv.writer(fh)
        if nuevo:
            writer.writerow(COLUMNS)
        fh.flush()

        while True:
            try:
                if time.time() - ultimo_redescubrimiento > REDESCUBRIR_CADA_S:
                    pares = _cargar_o_descubrir_pares()
                    ultimo_redescubrimiento = time.time()

                for par in pares:
                    clave = (par["event_title"], par["umbral_bajo"], par["umbral_alto"])
                    bid_yes, ask_yes = _mejor_bid_ask(par["token_yes_bajo"])
                    bid_no, ask_no = _mejor_bid_ask(par["token_no_alto"])
                    if None in (bid_yes, ask_yes, bid_no, ask_no):
                        continue

                    tick = 0.001
                    maker_bajo = round(bid_yes + tick, 4)
                    maker_alto = round(bid_no + tick, 4)

                    prev = ultimo_maker.get(clave)
                    cruce_bajo = cruce_alto = False
                    if prev:
                        prev_bajo, prev_alto = prev
                        cruce_bajo = ask_yes <= prev_bajo
                        cruce_alto = ask_no <= prev_alto
                    ultimo_maker[clave] = (maker_bajo, maker_alto)

                    writer.writerow([
                        datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        par["event_title"], par["direccion"],
                        par["umbral_bajo"], par["umbral_alto"],
                        bid_yes, ask_yes, bid_no, ask_no,
                        maker_bajo, maker_alto,
                        cruce_bajo, cruce_alto, cruce_bajo and cruce_alto,
                    ])
                fh.flush()
            except Exception as e:
                _log(f"error en ciclo principal: {e}")

            time.sleep(POLL_INTERVAL_S)


if __name__ == "__main__":
    main()
