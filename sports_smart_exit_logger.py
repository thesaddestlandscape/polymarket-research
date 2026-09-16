#!/usr/bin/env python3
"""
sports_smart_exit_logger.py — PASO 1 de Smart Exit para sports (shadow
puro, NO toca dinero real). Port directo de smart_exit_logger.py
(cripto, ya validado con meses de datos) -- petición explícita Javi,
16-Sep: "diseñar la venta de posiciones si vemos que vamos a palmar,
como hemos hecho en cripto. La idea es ganar pasta por encima del
precio de entrada y no perder nada".

Cada ciclo (cron) registra el precio de mercado ACTUAL de cada posición
real OPEN de sports (data/sports/trades.csv), para construir OFFLINE el
dataset con el que calibrar TP/SL -- exactamente el mismo propósito que
el logger de cripto, que tardó semanas en acumular suficiente n para
calibrar con rigor (analisis_smart_exit.py). Sports no tiene ese
histórico todavía -- este logger es el punto de partida.

READ-ONLY sobre dinero: solo LEE trades.csv y consulta precios PÚBLICOS
(gamma-api, sin clave). NUNCA escribe trades.csv ni envía órdenes al
CLOB. Única salida: append a data/sports/smart_exit_prices.csv.

Diferencias reales con el logger de cripto (no una copia ciega):
- trades.csv de sports usa columnas distintas: `categoria`/`tipo` (no
  `strategy`/`subtype`), `direction` es el ÍNDICE del outcome elegido
  (0/1), no "BUY_YES"/"BUY_NO" -- outcomePrices[direction] es el precio
  del lado que se compró.
- `timestamp_utc` de sports ya viene con offset explícito
  (`+00:00`), no `Z` -- fromisoformat lo parsea directo, sin el
  recorte que hace parse_dt() en cripto.
- Sin fee aplicado aquí (igual que cripto paso 1): precio_lado es el
  mid crudo (outcomePrices), la calibración posterior (equivalente a
  analisis_smart_exit.py) es quien aplica HAIRCUT_VENTA + fee real
  (5% sports, no 7%).
"""
import csv
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = Path(__file__).resolve().parent
TRADES = BASE / "data" / "sports" / "trades.csv"
OUT = BASE / "data" / "sports" / "smart_exit_prices.csv"
GAMMA = "https://gamma-api.polymarket.com/markets"
TIMEOUT = 10

CAMPOS = ["ts_utc", "market_id", "categoria", "tipo", "direction", "entry_price",
          "stake_eur", "precio_lado", "precio_outcome0", "precio_outcome1",
          "seg_desde_entrada", "seg_hasta_fin", "valor_salida_eur",
          "pnl_salida_eur", "mkt_closed"]


def parse_dt(s):
    if not s:
        return None
    try:
        dt = datetime.fromisoformat(s)
        return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None


def outcome_prices(mkt):
    raw = mkt.get("outcomePrices")
    if isinstance(raw, str):
        try:
            raw = json.loads(raw)
        except Exception:
            return None
    if isinstance(raw, list) and len(raw) >= 2:
        try:
            return float(raw[0]), float(raw[1])
        except (ValueError, TypeError):
            return None
    return None


def fetch(cid):
    """16-Sep (hallazgo real, cripto usa el ID numérico interno de
    Polymarket en `market_id` -- el endpoint singular /markets/{id}
    funciona ahí; sports guarda el CONDITION_ID hexadecimal en esa
    columna, mismo valor que ya usa outcome_por_condition_id() en
    sports_wallet_mirror_sniper.py -- hace falta el endpoint plural con
    `condition_ids`, sin filtro closed (a diferencia de esa función,
    aquí también interesan los mercados AÚN ABIERTOS)."""
    for i in range(3):
        try:
            r = requests.get(GAMMA, timeout=TIMEOUT, params={"condition_ids": cid})
            if r.status_code == 429:
                time.sleep(2 ** i)
                continue
            r.raise_for_status()
            d = r.json()
            if isinstance(d, list) and d:
                for m in d:
                    if (m.get("conditionId") or m.get("condition_id")) == cid:
                        return m
                return d[0]
            if isinstance(d, dict):
                return d
        except Exception:
            if i == 2:
                return None
    return None


def _market_ids_con_cierre_logueado() -> set:
    if not OUT.exists():
        return set()
    ids = set()
    with open(OUT, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("mkt_closed") == "1" and r.get("market_id"):
                ids.add(r["market_id"])
    return ids


def _filas_cierre_desde_trades(cerradas: list, ya_logueados: set) -> list:
    """Mismo fix que cripto (28-Jul, feedback_capturas_sin_conectar_
    riesgo_olvido_28jul): un tick sintético de cierre por market_id
    CLOSED, usando el resultado ya autoritativo de trades.csv
    (exit_price/pnl_neto_eur/close_timestamp) -- no depende de que la
    API marque el mercado como closed a tiempo."""
    filas = []
    for t in cerradas:
        mid = t.get("market_id")
        if not mid or mid in ya_logueados:
            continue
        try:
            entry = float(t.get("entry_price") or 0)
            exit_price = float(t.get("exit_price") or "")
            stake = float(t.get("stake_eur") or 0)
            pnl = float(t.get("pnl_neto_eur") or 0)
            direction = int(t.get("direction", ""))
        except (ValueError, TypeError):
            continue
        if exit_price == 1.0:
            p0, p1 = (1.0, 0.0) if direction == 0 else (0.0, 1.0)
        elif exit_price == 0.0:
            p0, p1 = (0.0, 1.0) if direction == 0 else (1.0, 0.0)
        else:
            continue
        t0 = parse_dt(t.get("timestamp_utc"))
        tc = parse_dt(t.get("close_timestamp"))
        te = parse_dt(t.get("end_date"))
        shares = stake / entry if entry > 0 else 0.0
        valor_salida = shares * exit_price
        filas.append({
            "ts_utc": (tc or datetime.now(timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "market_id": mid,
            "categoria": t.get("categoria", ""),
            "tipo": t.get("tipo", ""),
            "direction": direction,
            "entry_price": entry,
            "stake_eur": stake,
            "precio_lado": round(exit_price, 4),
            "precio_outcome0": round(p0, 4),
            "precio_outcome1": round(p1, 4),
            "seg_desde_entrada": round((tc - t0).total_seconds()) if (tc and t0) else "",
            "seg_hasta_fin": round((te - tc).total_seconds()) if (tc and te) else "",
            "valor_salida_eur": round(valor_salida, 4),
            "pnl_salida_eur": round(pnl, 4),
            "mkt_closed": 1,
        })
        ya_logueados.add(mid)
    return filas


def main():
    if not TRADES.exists():
        return
    with open(TRADES, encoding="utf-8") as f:
        todas = list(csv.DictReader(f))
    abiertas = [r for r in todas if r.get("status") == "OPEN" and r.get("market_id")]
    cerradas = [r for r in todas if r.get("status") == "CLOSED" and r.get("market_id")]

    filas_cierre = _filas_cierre_desde_trades(cerradas, _market_ids_con_cierre_logueado())

    if not abiertas and not filas_cierre:
        return

    ahora = datetime.now(timezone.utc)
    filas = list(filas_cierre)
    for t in abiertas:
        mkt = fetch(t["market_id"])
        if not mkt:
            continue
        op = outcome_prices(mkt)
        if not op:
            continue
        p0, p1 = op
        try:
            direction = int(t.get("direction", ""))
        except (ValueError, TypeError):
            continue
        p_lado = p0 if direction == 0 else p1
        try:
            entry = float(t.get("entry_price") or 0)
        except (ValueError, TypeError):
            entry = 0.0
        try:
            stake = float(t.get("stake_eur") or 0)
        except (ValueError, TypeError):
            stake = 0.0
        shares = stake / entry if entry > 0 else 0.0
        valor_salida = shares * p_lado
        pnl_salida = valor_salida - stake
        t0 = parse_dt(t.get("timestamp_utc"))
        te = parse_dt(t.get("end_date"))
        mkt_closed = bool(mkt.get("closed") or mkt.get("resolved")
                          or mkt.get("archived") or not mkt.get("active", True))
        filas.append({
            "ts_utc": ahora.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "market_id": t["market_id"],
            "categoria": t.get("categoria", ""),
            "tipo": t.get("tipo", ""),
            "direction": direction,
            "entry_price": entry,
            "stake_eur": stake,
            "precio_lado": round(p_lado, 4),
            "precio_outcome0": round(p0, 4),
            "precio_outcome1": round(p1, 4),
            "seg_desde_entrada": round((ahora - t0).total_seconds()) if t0 else "",
            "seg_hasta_fin": round((te - ahora).total_seconds()) if te else "",
            "valor_salida_eur": round(valor_salida, 4),
            "pnl_salida_eur": round(pnl_salida, 4),
            "mkt_closed": int(mkt_closed),
        })

    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)


if __name__ == "__main__":
    main()
