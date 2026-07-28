#!/usr/bin/env python3
"""
smart_exit_logger.py — PASO 1 de Smart Exit (shadow puro, NO toca dinero real).

Cada minuto (cron) registra el precio de mercado ACTUAL de cada posición live
OPEN, para construir OFFLINE el dataset con el que calibrar si vender antes de
resolución recupera EV — cortar perdedoras ("vender cuando la cinta confirma
que vamos a palmar, recuperar al menos algo") o blindar ganadoras.

READ-ONLY sobre dinero: solo LEE trades.csv y consulta precios PÚBLICOS
(gamma-api, sin clave). NUNCA escribe trades.csv ni envía órdenes al CLOB.
Única salida: append a data/live/smart_exit_prices.csv.

Aproximación paso 1: usa el mid (outcomePrices) como precio de salida. El paso 2
lo refinará con el bid real del CLOB (vender cruza el spread → algo peor) y con
el fee (venta = taker → paga fee; maker = 0, ver fee de protocolo verificado
10-Jul). Ver memorias idea_smart_exit + project_state_2026-07-10.
"""
import csv
import json
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = Path(__file__).resolve().parent
TRADES = BASE / "data" / "live" / "trades.csv"
OUT = BASE / "data" / "live" / "smart_exit_prices.csv"
GAMMA = "https://gamma-api.polymarket.com/markets/{}"
TIMEOUT = 10

CAMPOS = ["ts_utc", "market_id", "strategy", "direction", "entry_price",
          "stake_eur", "precio_lado", "precio_yes", "precio_no",
          "seg_desde_entrada", "seg_hasta_fin", "valor_salida_eur",
          "pnl_salida_eur", "mkt_closed"]


def parse_dt(s):
    if not s:
        return None
    s = s.replace("Z", "").split("+")[0][:19]
    try:
        return datetime.fromisoformat(s).replace(tzinfo=timezone.utc)
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


def fetch(mid):
    for i in range(3):
        try:
            r = requests.get(GAMMA.format(mid), timeout=TIMEOUT)
            if r.status_code == 429:
                time.sleep(2 ** i)
                continue
            if r.status_code == 404:
                return None
            r.raise_for_status()
            d = r.json()
            if isinstance(d, list) and d:
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
    """28-Jul (fix bug real, ver feedback_capturas_sin_conectar_riesgo_
    olvido_28jul / analisis_touch_vs_win_smartexit_28jul.py): antes el
    ÚNICO tick con mkt_closed=1 dependía de re-consultar gamma-api MIENTRAS
    el trade seguía en trades.csv con status=OPEN -- pero shadow_resolve.py
    cierra el trade (status->CLOSED) normalmente ANTES de que la propia API
    de Polymarket marque el mercado como closed/resolved/archived, así que
    el bucle de arriba (filtra status=='OPEN') dejaba de mirar ese
    market_id justo antes de que mkt_closed pudiera llegar a ser True.
    Confirmado con datos reales: 63/87 mercados de FAVORITO_CONFIRMADO sin
    NINGÚN tick de cierre.

    Fix: en vez de perseguir el flag de la API (no fiable, llega tarde),
    usar el resultado YA AUTORITATIVO que trades.csv registra al cerrar
    (`exit_price`, `pnl_neto_eur`, `close_timestamp`) -- no hace falta
    ninguna llamada de red. Genera UN tick sintético de cierre por
    market_id CLOSED que todavía no tenga uno (dedup vía
    _market_ids_con_cierre_logueado), así que una sola corrida de este
    fix hace backfill retroactivo de TODO el histórico ya cerrado, no solo
    de los cierres futuros."""
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
        except (ValueError, TypeError):
            continue
        dir_ = t.get("direction", "")
        if dir_ == "BUY_YES":
            pyes, pno = exit_price, round(1.0 - exit_price, 4)
        else:
            pyes, pno = round(1.0 - exit_price, 4), exit_price
        t0 = parse_dt(t.get("timestamp_utc"))
        tc = parse_dt(t.get("close_timestamp"))
        te = parse_dt(t.get("end_date"))
        shares = stake / entry if entry > 0 else 0.0
        valor_salida = shares * exit_price
        filas.append({
            "ts_utc": (tc or datetime.now(timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "market_id": mid,
            "strategy": t.get("strategy", ""),
            "direction": dir_,
            "entry_price": entry,
            "stake_eur": stake,
            "precio_lado": round(exit_price, 4),
            "precio_yes": round(pyes, 4),
            "precio_no": round(pno, 4),
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
        pyes, pno = op
        dir_ = t.get("direction", "")
        p_lado = pyes if dir_ == "BUY_YES" else pno
        try:
            entry = float(t.get("entry_price") or 0)
        except (ValueError, TypeError):
            entry = 0.0
        try:
            stake = float(t.get("stake_eur") or 0)
        except (ValueError, TypeError):
            stake = 0.0
        shares = stake / entry if entry > 0 else 0.0
        valor_salida = shares * p_lado          # vender ahora al mid (aprox paso 1)
        pnl_salida = valor_salida - stake
        t0 = parse_dt(t.get("timestamp_utc"))
        te = parse_dt(t.get("end_date"))
        mkt_closed = bool(mkt.get("closed") or mkt.get("resolved")
                          or mkt.get("archived") or not mkt.get("active", True))
        filas.append({
            "ts_utc": ahora.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "market_id": t["market_id"],
            "strategy": t.get("strategy", ""),
            "direction": dir_,
            "entry_price": entry,
            "stake_eur": stake,
            "precio_lado": round(p_lado, 4),
            "precio_yes": round(pyes, 4),
            "precio_no": round(pno, 4),
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
