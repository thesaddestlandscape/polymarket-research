"""
capture_markets.py — v9. Añade captura de mercados Up/Down 5m por slug dinámico.

Mejoras vs v8:
- fetch_updown_5m_activos(): construye slugs {asset}-updown-5m-{ts} para la ventana
  de 5m actual y las 2 siguientes, consulta Gamma API por event slug directamente.
- Los mercados Up/Down 5M con precio válido y end_date futuro se añaden al CSV normal.
- Bucle interno de 10 capturas con sleep 60s
"""
import csv, json, time
from datetime import datetime, timezone
from pathlib import Path
import requests

TIMEOUT = 30
N_CAPTURAS_POR_WORKFLOW = 10
SLEEP_ENTRE_CAPTURAS_SEG = 60

TAG_SLUGS = [
    "crypto",
    "bitcoin",
    "ethereum",
    "solana",
    "crypto-prices",
]

UPDOWN_ASSETS = ["btc", "eth", "sol", "xrp", "doge", "bnb"]

# Horizontes de mercados Up/Down con sus intervalos en segundos
# slug_prefix: prefijo del slug en Polymarket
# intervalo_s: duración en segundos de cada ventana
# ventanas_adelante: cuántas ventanas futuras capturar además de la actual
UPDOWN_HORIZONTES = [
    {"slug_prefix": "updown-5m",  "intervalo_s": 300,    "ventanas": 3},
    {"slug_prefix": "updown-15m", "intervalo_s": 900,    "ventanas": 3},
    {"slug_prefix": "updown-1h",  "intervalo_s": 3600,   "ventanas": 2},
    {"slug_prefix": "updown-4h",  "intervalo_s": 14400,  "ventanas": 2},
    {"slug_prefix": "updown-24h", "intervalo_s": 86400,  "ventanas": 2},
]

COINGECKO_IDS = {
    "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana",
    "XRP": "ripple", "DOGE": "dogecoin", "BNB": "binancecoin",
    "ADA": "cardano", "LINK": "chainlink", "AVAX": "avalanche-2",
    "DOT": "polkadot", "MATIC": "matic-network", "LTC": "litecoin",
}
SPOT_SYMBOLS = list(COINGECKO_IDS.keys())

DIR_MARKETS = Path("data/markets")
DIR_PRICES  = Path("data/prices")
DIR_MARKETS.mkdir(parents=True, exist_ok=True)
DIR_PRICES.mkdir(parents=True, exist_ok=True)

CABECERA_MARKETS = [
    "timestamp_utc","market_id","condition_id","question","slug","end_date",
    "volume","volume_24hr","liquidity","price_yes","price_no","outcomes",
    "best_bid","best_ask","spread","last_trade_price",
    "one_day_price_change","one_hour_price_change",
    "event_id","event_title","event_slug","event_tags","event_volume_24hr",
]

HEADERS_HTTP = {
    "User-Agent": "Mozilla/5.0 (compatible; polymarket-research/9.0)",
    "Accept": "application/json",
}


def parse_outcome_prices(raw):
    if raw is None: return None
    if isinstance(raw, list): return raw
    if isinstance(raw, str):
        try: return json.loads(raw)
        except json.JSONDecodeError: return None
    return None


def es_expirado(end_date_str):
    if not end_date_str:
        return False
    try:
        s = end_date_str
        if not s.endswith("Z") and "+" not in s[10:]:
            s += "+00:00"
        else:
            s = s.replace("Z", "+00:00")
        return datetime.fromisoformat(s) < datetime.now(timezone.utc)
    except Exception:
        return False


def archivar_si_obsoleto(archivo, cabecera_esperada):
    if not archivo.exists():
        return
    try:
        with open(archivo, encoding="utf-8") as f:
            primera = f.readline().strip()
        if primera != ",".join(cabecera_esperada):
            destino = archivo.with_suffix(".old.csv")
            archivo.rename(destino)
            print(f"  Archivado {archivo.name} → {destino.name} (cabecera obsoleta)")
    except Exception as e:
        print(f"  Error verificando cabecera de {archivo}: {e}")


def fetch_events_por_slug(slug):
    url = "https://gamma-api.polymarket.com/events"
    offset, todos = 0, []
    while True:
        params = {
            "tag_slug": slug,
            "active": "true",
            "closed": "false",
            "related_tags": "true",
            "limit": 200,
            "offset": offset,
        }
        try:
            r = requests.get(url, params=params, headers=HEADERS_HTTP, timeout=TIMEOUT)
            r.raise_for_status()
            lote = r.json()
        except Exception as e:
            print(f"  Error gamma slug={slug} offset={offset}: {type(e).__name__}: {e}")
            break
        if not lote:
            break
        todos.extend(lote)
        if len(lote) < 200:
            break
        offset += 200
        if offset > 10000:
            break
    return todos


def fetch_updown_por_horizonte(horizonte: dict) -> list:
    """
    Fetch mercados Up/Down para un horizonte dado (5m, 15m, 1h, 4h, 24h).
    Construye slugs {asset}-{slug_prefix}-{ts} para las próximas N ventanas.
    """
    ahora_ts   = int(time.time())
    intervalo  = horizonte["intervalo_s"]
    prefix     = horizonte["slug_prefix"]
    n_ventanas = horizonte["ventanas"]

    siguiente = ((ahora_ts // intervalo) + 1) * intervalo
    ventanas  = [siguiente + i * intervalo for i in range(n_ventanas)]

    url      = "https://gamma-api.polymarket.com/events"
    mercados = []
    encontrados = 0

    for ts in ventanas:
        for asset in UPDOWN_ASSETS:
            event_slug = f"{asset}-{prefix}-{ts}"
            try:
                r = requests.get(
                    url,
                    params={"slug": event_slug},
                    headers=HEADERS_HTTP,
                    timeout=TIMEOUT,
                )
                r.raise_for_status()
                datos = r.json()
                if not datos:
                    continue
                ev = datos[0] if isinstance(datos, list) else datos
                ev_id    = ev.get("id", "")
                ev_title = ev.get("title", "")
                ev_slug  = ev.get("slug", "")
                ev_vol24 = ev.get("volume24hr", "")
                tags = "|".join([
                    t.get("label", "")
                    for t in (ev.get("tags") or [])
                    if isinstance(t, dict) and t.get("label")
                ])
                for m in ev.get("markets") or []:
                    end_date = (m.get("endDate") or "")[:19]
                    if es_expirado(end_date):
                        continue
                    precios = parse_outcome_prices(m.get("outcomePrices"))
                    py = precios[0] if precios and len(precios) >= 1 else ""
                    if not py or float(py) <= 0:
                        continue
                    m["_event_id"]         = ev_id
                    m["_event_title"]      = ev_title
                    m["_event_slug"]       = ev_slug
                    m["_event_volume24hr"] = ev_vol24
                    m["_event_tags"]       = tags
                    mercados.append(m)
                    encontrados += 1
            except Exception:
                pass  # slug no existe aún para ventanas futuras

    if encontrados:
        print(f"  Up/Down {prefix}: {encontrados} mercados activos")
    return mercados


def fetch_todos_updown() -> list:
    """Captura mercados Up/Down de todos los horizontes configurados."""
    mercados = []
    for horizonte in UPDOWN_HORIZONTES:
        mercados += fetch_updown_por_horizonte(horizonte)
    return mercados


def fetch_todos_eventos_crypto():
    eventos_por_id = {}
    for slug in TAG_SLUGS:
        lote = fetch_events_por_slug(slug)
        print(f"  slug={slug}: {len(lote)} eventos")
        for ev in lote:
            eid = ev.get("id", "")
            if eid and eid not in eventos_por_id:
                eventos_por_id[eid] = ev
    return list(eventos_por_id.values())


def extraer_mercados_de_eventos(eventos):
    mercados = []
    for ev in eventos:
        ev_id    = ev.get("id", "")
        ev_title = ev.get("title", "")
        ev_slug  = ev.get("slug", "")
        ev_vol24 = ev.get("volume24hr", "")
        tags = "|".join([
            t.get("label", "")
            for t in (ev.get("tags") or [])
            if isinstance(t, dict) and t.get("label")
        ])
        for m in ev.get("markets") or []:
            if m.get("closed") or m.get("archived") or m.get("active") is False:
                continue
            end_date = (m.get("endDate") or "")[:19]
            if es_expirado(end_date):
                continue
            precios = parse_outcome_prices(m.get("outcomePrices"))
            py = precios[0] if precios and len(precios) >= 1 else ""
            if not py or float(py) <= 0:
                continue
            m["_event_id"]         = ev_id
            m["_event_title"]      = ev_title
            m["_event_slug"]       = ev_slug
            m["_event_volume24hr"] = ev_vol24
            m["_event_tags"]       = tags
            mercados.append(m)
    return mercados


def fetch_coingecko_prices():
    ids = ",".join(COINGECKO_IDS.values())
    url = "https://api.coingecko.com/api/v3/simple/price"
    try:
        r = requests.get(url, params={"ids": ids, "vs_currencies": "usd"}, timeout=TIMEOUT)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        print(f"  CoinGecko: {type(e).__name__}: {e}")
        return {s: None for s in SPOT_SYMBOLS}
    return {
        sym: data.get(cg_id, {}).get("usd")
        for sym, cg_id in COINGECKO_IDS.items()
    }


def guardar_mercados(mercados, ts):
    fecha   = ts[:10]
    archivo = DIR_MARKETS / f"{fecha}.csv"
    archivar_si_obsoleto(archivo, CABECERA_MARKETS)
    nuevo = not archivo.exists()
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(CABECERA_MARKETS)
        for m in mercados:
            precios  = parse_outcome_prices(m.get("outcomePrices"))
            py = precios[0] if precios and len(precios) >= 1 else ""
            pn = precios[1] if precios and len(precios) >= 2 else ""
            outcomes = m.get("outcomes", "")
            if isinstance(outcomes, list):
                outcomes = json.dumps(outcomes)
            w.writerow([
                ts,
                m.get("id", ""),
                m.get("conditionId", ""),
                m.get("question", ""),
                m.get("slug", ""),
                (m.get("endDate") or "")[:19],
                m.get("volume", ""),
                m.get("volume24hr", ""),
                m.get("liquidity", ""),
                py, pn, outcomes,
                m.get("bestBid", ""),
                m.get("bestAsk", ""),
                m.get("spread", ""),
                m.get("lastTradePrice", ""),
                m.get("oneDayPriceChange", ""),
                m.get("oneHourPriceChange", ""),
                m.get("_event_id", ""),
                m.get("_event_title", ""),
                m.get("_event_slug", ""),
                m.get("_event_tags", ""),
                m.get("_event_volume24hr", ""),
            ])


def guardar_precios(precios, ts):
    fecha   = ts[:10]
    archivo = DIR_PRICES / f"{fecha}.csv"
    nuevo   = not archivo.exists()
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            # Formato nuevo: una fila por asset
            w.writerow(["timestamp_utc", "asset", "price_usd", "change_1h_pct", "change_24h_pct"])
            for sym in SPOT_SYMBOLS:
                v = precios.get(sym)
                if v is not None:
                    w.writerow([ts, sym, v, "", ""])
        else:
            # Detectar formato del archivo existente
            try:
                with open(archivo, "r", newline="", encoding="utf-8") as rf:
                    header = next(csv.reader(rf), [])
            except Exception:
                header = []
            if "asset" in header:
                # Formato nuevo: una fila por asset
                for sym in SPOT_SYMBOLS:
                    v = precios.get(sym)
                    if v is not None:
                        w.writerow([ts, sym, v, "", ""])
            else:
                # Formato viejo: una fila con todos los assets
                w.writerow([ts] + [precios.get(s, "") for s in SPOT_SYMBOLS])


def una_captura():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    n_mkt, n_px = 0, 0
    try:
        precios = fetch_coingecko_prices()
        n_px = sum(1 for v in precios.values() if v is not None)
        guardar_precios(precios, ts)
    except Exception as e:
        print(f"  ERROR precios: {type(e).__name__}: {e}")
    try:
        eventos   = fetch_todos_eventos_crypto()
        mercados  = extraer_mercados_de_eventos(eventos)
        mercados += fetch_todos_updown()
        n_mkt     = len(mercados)
        guardar_mercados(mercados, ts)
        print(f"  Eventos únicos: {len(eventos)} → mercados totales: {n_mkt}")
    except Exception as e:
        print(f"  ERROR polymarket: {type(e).__name__}: {e}")
    return n_mkt, n_px


def main():
    ts_i = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts_i}] === Bucle de {N_CAPTURAS_POR_WORKFLOW} capturas (v9) ===")
    for i in range(N_CAPTURAS_POR_WORKFLOW):
        print(f"\n--- Captura {i+1}/{N_CAPTURAS_POR_WORKFLOW} ---")
        n_mkt, n_px = una_captura()
        print(f"  Resumen: {n_mkt} mercados, {n_px}/{len(SPOT_SYMBOLS)} precios spot")
        if i < N_CAPTURAS_POR_WORKFLOW - 1:
            time.sleep(SLEEP_ENTRE_CAPTURAS_SEG)
    print(f"\n[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] === Fin ===")


if __name__ == "__main__":
    main()
