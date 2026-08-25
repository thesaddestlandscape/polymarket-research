#!/usr/bin/env python3
"""
candidata2_weekly_temprano_espejo_fase0.py -- P-GALLINA Candidata 2, 25-Ago
(petición explícita Javi: "haz lo que sea mas eficaz, eficiente para sacar
pasta de esta estrategia").

Espejo del arquetipo WEEKLY_TEMPRANO (9 wallets, `analisis_bot_arquetipos_
25ago.py::clasificar_wallets`, el único arquetipo con g_kelly ponderado
positivo en agregado, ver idea_gallina_huevos_oro_candidatas_25ago). Sus
mercados "weekly" NO son Up/Down -- son la familia strike-ladder ("Will
Bitcoin reach $X, Aug24-30") que ya es nuestra propia estrategia
WEEKLY_PRICE (IC+0.286 shadow). Verificado 25-Ago: liquidez real
($13k-31k/mercado) muy distinta al libro vacío habitual del proyecto.

Por qué CRON DIARIO y no un observer en tiempo real (mismo patrón que
bot_wallets_gate_bucket_fase0.py, P-GALLINA Candidata 1): las entradas de
estos bots son RARAS a nivel de todo el mercado (51 trades weekly de TODO
Polymarket en un día completo, medido 25-Ago) y las posiciones se sostienen
DÍAS (no son sensibles a latencia de segundos) -- un observer 24/7 quemaría
CPU (ya limitada, 2 cores, ver incidente watchdog 25-Ago) por eventos que
tardarán días en aparecer. En vez de esperar pasivamente al firehose,
consulta directamente las posiciones ACTUALES de las 9 wallets vía Data API
(9 llamadas, barato) y diffea contra el snapshot de ayer -- detecta
posiciones NUEVAS en mercados todavía abiertos sin esperar el evento en
vivo. Para cada una: consulta el libro público real (misma función que usa
live_trade.py) para medir fill-ability REAL, no aproximada.

Solo lectura -- no coloca, cancela ni modifica ninguna orden real. FASE 0.
"""
import csv
import json
import sys
import time
from datetime import date, datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

from analisis_bot_arquetipos_25ago import clasificar_wallets  # noqa: E402
import live_trade as lt  # noqa: E402

DIR_SHADOW = REPO / "data" / "shadow"
OUT = DIR_SHADOW / "candidata2_weekly_temprano_espejo_fase0.csv"
VISTOS_PATH = DIR_SHADOW / "candidata2_weekly_temprano_espejo_fase0_vistos.json"

STAKE_REF_EUR = 1.05  # mismo suelo que min_stake_eur en config_live.json
TIMEOUT = 15

COLUMNS = [
    "timestamp_utc", "wallet", "market_slug", "title", "outcome", "asset",
    "end_date", "avg_price_wallet", "size_wallet", "usd_cost_wallet",
    "cur_price_gamma", "mejor_ask_deteccion", "profundidad_eur_deteccion",
    "ratio_vs_stake_deteccion",
]


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _wallets_weekly_temprano() -> set:
    arqs = clasificar_wallets()
    return {w for w, v in arqs.items() if v["arquetipo"] == "WEEKLY_TEMPRANO"}


def _posiciones_abiertas(wallet: str) -> list[dict]:
    """Posiciones con endDate en el futuro (todavía no resuelto). La API
    no expone un flag "abierto" fiable (redeemable=true aparece también en
    mercados ya resueltos) -- endDate es el filtro robusto."""
    try:
        r = requests.get("https://data-api.polymarket.com/positions",
                          params={"user": wallet, "limit": 500}, timeout=TIMEOUT)
        r.raise_for_status()
        pos = r.json()
    except Exception as e:
        _log(f"WARN /positions falló para {wallet[:10]}..: {type(e).__name__}: {e}")
        return []
    hoy = date.today()
    out = []
    for p in pos:
        ed = p.get("endDate")
        if not ed:
            continue
        try:
            ed_date = datetime.fromisoformat(ed.replace("Z", "+00:00")).date()
        except Exception:
            continue
        if ed_date >= hoy:
            out.append(p)
    return out


def _vistos_cargar() -> set:
    try:
        return set(json.loads(VISTOS_PATH.read_text(encoding="utf-8")))
    except Exception:
        return set()


def _vistos_guardar(vistos: set) -> None:
    VISTOS_PATH.write_text(json.dumps(sorted(vistos)), encoding="utf-8")


def _guardar(filas: list) -> None:
    if not filas:
        return
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(COLUMNS)
        for fila in filas:
            w.writerow([fila.get(c, "") for c in COLUMNS])


def main() -> int:
    wallets = _wallets_weekly_temprano()
    _log(f"arrancado -- {len(wallets)} wallets WEEKLY_TEMPRANO")
    vistos = _vistos_cargar()
    primera_vez = not VISTOS_PATH.exists()

    filas_nuevas = []
    for w in wallets:
        for p in _posiciones_abiertas(w):
            clave = f"{w}|{p.get('asset', '')}"
            if clave in vistos:
                continue
            vistos.add(clave)
            if primera_vez:
                # 25-Ago (mismo patrón que bot_wallets_gate_bucket_fase0.py:
                # el backlog de posiciones YA abiertas antes de hoy no tiene
                # sentido medirlo -- fill-ability es del INSTANTE de detección,
                # no reconstruible retroactivamente). Se marca como visto sin
                # consultar libro, solo detecciones desde MAÑANA cuentan.
                continue
            token_id = p.get("asset", "")
            precio_entrada = p.get("avgPrice")
            try:
                precio_ref = float(precio_entrada)
            except (TypeError, ValueError):
                precio_ref = 0.5
            fill = lt._consultar_profundidad_libro(None, token_id, precio_ref, STAKE_REF_EUR)
            fila = {
                "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "wallet": w,
                "market_slug": p.get("slug", ""),
                "title": p.get("title", ""),
                "outcome": p.get("outcome", ""),
                "asset": token_id,
                "end_date": p.get("endDate", ""),
                "avg_price_wallet": precio_entrada,
                "size_wallet": p.get("size"),
                "usd_cost_wallet": p.get("initialValue"),
                "cur_price_gamma": p.get("curPrice"),
                "mejor_ask_deteccion": fill.get("mejor_ask") if fill.get("ok") else "",
                "profundidad_eur_deteccion": fill.get("profundidad_eur") if fill.get("ok") else "",
                "ratio_vs_stake_deteccion": fill.get("ratio_vs_stake") if fill.get("ok") else "",
            }
            filas_nuevas.append(fila)
            _log(f"NUEVA posicion detectada: {w[:10]}.. {p.get('title','')[:60]} "
                 f"avg={precio_entrada} profundidad={fill.get('profundidad_eur') if fill.get('ok') else 'sin-datos'}")
            time.sleep(0.2)  # cortesía, evita ráfaga sobre el book público

    if primera_vez:
        _log(f"backlog inicial marcado como visto sin consultar libro: {len(vistos)} posiciones abiertas hoy")

    _guardar(filas_nuevas)
    _vistos_guardar(vistos)
    _log(f"fin -- {len(filas_nuevas)} posiciones nuevas registradas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
