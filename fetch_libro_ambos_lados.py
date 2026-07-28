#!/usr/bin/env python3
"""
fetch_libro_ambos_lados.py — Captura periódica del libro de AMBOS lados
(YES y NO) para nuestro universo de mercados Up/Down (5/15/60min,
BTC/ETH/SOL/XRP/DOGE/BNB). Solo lectura.

Origen (28-Jul, backlog Moon Dev — Box Builder / Corridor Collector /
Spread-Harvest Maker, Stage 3/4): los 3 comparten el mismo bloqueo —
`libro_snapshots.csv` (live_trade.py) solo registra el lado que
NOSOTROS compramos, nunca el lado opuesto, así que no se puede calcular
"¿el libro está ancho?" (ask_YES+ask_NO) con los datos que ya
teníamos, en ningún timeframe.

Deliberadamente NO se toca `live_trade.py` para esto -- es código que
decide dinero real, CLAUDE.md exige `/code-review` antes de CUALQUIER
cambio ahí sin excepción (antecedente real 18-Jul: un refactor
"seguro" de 6 líneas rompió el 100% de las compras live). En su lugar,
este script IMPORTA sus funciones de solo lectura ya existentes
(`_get_token_ids`, `_fetch_book_publico`) sin modificarlas -- mismo
patrón ya usado por `ballenas_executor_5min.py`/`ballenas_executor_
btc15m.py` (`import live_trade as lt`).

Descubre el universo activo leyendo `data/markets/HOY.csv` (ya lo
mantiene `capture_markets.py`, sin llamada de red nueva para eso) y
resuelve tokens/libro vía Gamma+CLOB públicos (sin auth, sin construir
ClobClient).

Salida: data/shadow/libro_ambos_lados_YYYY-MM-DD.csv, columnas
incluyen ask_yes, ask_no, ask_sum (la métrica "libro ancho" que
Box Builder/Spread-Harvest necesitan: ask_sum>=X ~ MMs ausentes).

Corre en screen propio (mismo patrón que chainlink/liqs):
  screen -dmS libroambos bash -c "cd /root/polymarket-research && .venv/bin/python fetch_libro_ambos_lados.py >> logs/libro_ambos_lados.log 2>&1"
"""

import csv
import time
from datetime import datetime, timezone
from pathlib import Path

import live_trade as lt  # solo lectura: _get_token_ids, _fetch_book_publico -- NUNCA se llama nada que ordene
# _parse_updown_tipo/identificar_activo (solo lectura, funciones puras sobre
# texto) en vez de parsear el slug -- descubierto en vivo (28-Jul): los
# mercados 'hourly' (60min) NO tienen slug updown-1h resoluble (confirmado
# contra la API real, 0 resultados) -- se identifican por el TEXTO de la
# pregunta ("June 24, 9am ET", sin rango de minutos), exactamente lo que
# ya hace shadow_predict.py. Reinventar esto contra el slug se habría
# quedado ciego a todo el universo 60min silenciosamente.
from shadow_predict import _parse_updown_tipo, identificar_activo

REPO = Path(__file__).resolve().parent
DIR_MARKETS = REPO / "data" / "markets"
DIR_SHADOW = REPO / "data" / "shadow"

ACTIVOS = {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"}
MARCOS_TRACKEADOS = {5, 15, 60}  # minutos -- nuestro universo real de trading
INTERVALO_ESCANEO_S = 45

COLUMNS = [
    "timestamp_utc", "market_id", "condition_id", "activo", "marco",
    "end_date", "restante_s", "ask_yes", "ask_no", "ask_sum",
    "bid_yes", "bid_no",
]


def _log(msg: str) -> None:
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] {msg}", flush=True)


def _archivo_hoy() -> Path:
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return DIR_SHADOW / f"libro_ambos_lados_{fecha}.csv"


def _universo_activo() -> dict:
    """{market_id: (activo, marco_str, condition_id, end_date)} desde el CSV
    de hoy de capture_markets.py, solo mercados Up/Down aún no vencidos.
    Clasificación por TEXTO de la pregunta (_parse_updown_tipo/
    identificar_activo, mismas funciones que usa shadow_predict.py) -- no
    por slug, ver nota arriba sobre por qué el slug no sirve para 60min."""
    archivo = DIR_MARKETS / f"{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.csv"
    if not archivo.exists():
        return {}
    ahora = datetime.now(timezone.utc)
    universo = {}
    with open(archivo, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            question = r.get("question") or ""
            tipo, vent = _parse_updown_tipo(question)
            if tipo not in ("slot", "hourly") or vent not in MARCOS_TRACKEADOS:
                continue
            activo = identificar_activo(question)
            if activo not in ACTIVOS:
                continue
            end_date = r.get("end_date") or ""
            try:
                edt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
                if edt.tzinfo is None:
                    edt = edt.replace(tzinfo=timezone.utc)
            except Exception:
                continue
            if edt <= ahora:
                continue
            universo[r.get("market_id", "")] = (activo, f"{vent}min", r.get("condition_id", ""), edt)
    return universo


def _mejor_ask(book: dict | None) -> float | None:
    if not book:
        return None
    asks = book.get("asks") or []
    mejor = None
    for lvl in asks:
        try:
            p = float(lvl.get("price"))
        except (TypeError, ValueError, AttributeError):
            continue
        if mejor is None or p < mejor:
            mejor = p
    return mejor


def _mejor_bid(book: dict | None) -> float | None:
    if not book:
        return None
    bids = book.get("bids") or []
    mejor = None
    for lvl in bids:
        try:
            p = float(lvl.get("price"))
        except (TypeError, ValueError, AttributeError):
            continue
        if mejor is None or p > mejor:
            mejor = p
    return mejor


def _capturar_mercado(mid: str, activo: str, marco: str, condition_id: str, edt) -> dict | None:
    try:
        yes_token, no_token, cid_real = lt._get_token_ids(mid)
    except Exception:
        return None
    book_yes = lt._fetch_book_publico(yes_token)
    book_no = lt._fetch_book_publico(no_token)
    ask_yes = _mejor_ask(book_yes)
    ask_no = _mejor_ask(book_no)
    ask_sum = round(ask_yes + ask_no, 4) if (ask_yes is not None and ask_no is not None) else None
    ahora = datetime.now(timezone.utc)
    return {
        "timestamp_utc": ahora.isoformat(timespec="seconds"),
        "market_id": mid,
        "condition_id": cid_real or condition_id,
        "activo": activo,
        "marco": marco,
        "end_date": edt.isoformat(timespec="seconds"),
        "restante_s": round((edt - ahora).total_seconds(), 1),
        "ask_yes": ask_yes if ask_yes is not None else "",
        "ask_no": ask_no if ask_no is not None else "",
        "ask_sum": ask_sum if ask_sum is not None else "",
        "bid_yes": _mejor_bid(book_yes) or "",
        "bid_no": _mejor_bid(book_no) or "",
    }


def _guardar(filas: list) -> None:
    if not filas:
        return
    archivo = _archivo_hoy()
    nuevo = not archivo.exists()
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)


def main() -> None:
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    _log(f"fetch_libro_ambos_lados arrancado — escaneo cada {INTERVALO_ESCANEO_S}s")
    while True:
        t0 = time.time()
        try:
            universo = _universo_activo()
            filas = []
            for mid, (activo, marco, cid, edt) in universo.items():
                fila = _capturar_mercado(mid, activo, marco, cid, edt)
                if fila:
                    filas.append(fila)
            _guardar(filas)
            if filas:
                anchos = [f for f in filas if isinstance(f["ask_sum"], float) and f["ask_sum"] >= 1.10]
                _log(f"escaneados {len(universo)} mercados, {len(filas)} con libro leído, "
                     f"{len(anchos)} con ask_sum>=1.10 (libro ancho)")
        except Exception as e:
            _log(f"Error en ciclo de escaneo: {type(e).__name__}: {e}")
        dormir = INTERVALO_ESCANEO_S - (time.time() - t0)
        if dormir > 0:
            time.sleep(dormir)


if __name__ == "__main__":
    main()
