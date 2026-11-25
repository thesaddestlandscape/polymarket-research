"""
capture_markets.py — v9. Añade captura de mercados Up/Down 5m por slug dinámico.

Mejoras vs v8:
- fetch_updown_5m_activos(): construye slugs {asset}-updown-5m-{ts} para la ventana
  de 5m actual y las 2 siguientes, consulta Gamma API por event slug directamente.
- Los mercados Up/Down 5M con precio válido y end_date futuro se añaden al CSV normal.
- Bucle interno de 10 capturas con sleep 60s
"""
import csv, io, json, os, re, tempfile, time
from datetime import datetime, timedelta, timezone
from pathlib import Path
import requests

from data_quality import validar_precio, fetch_coinbase_spot, validar_cross_source

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

# --- 13-Nov (cobertura 5m a +24 h + fix 429) ------------------------------------------------------------------
# data/markets/<dia>.csv NO CAMBIA (solo lo lee _universo_activo -> 4 consumidores que consultan gamma/CLOB por cada mercado: un
# horizonte largo ahi provocaria rafagas). El ADELANTO de updown-5m (de la 4a ventana hasta CAPTURE_5M_HORIZONTE_MIN; 0 = apagado,
# defecto; 1440 = 24 h) va SIEMPRE a UNIVERSO_5M_DIR (datalogs/universo_5m/, fuera de git, nadie lo glob-lee):
#   - adelanto_<dia>.csv: MISMO esquema que data/markets (auditoria);
#   - new_market_universo_<dia>.csv.gz: filas CON TOKENS (formato universo_5m_io), compartido con el listener new_market_universo.
#     Es el punto de commit y la fuente de "ya hecho": el adelanto salta los slugs que ya estan en ese fichero (hoy+ayer), vengan
#     del listener o de una captura anterior; asi si cae uno, el otro cubre, y un reinicio a mitad de ciclo no deja huecos.
# Captura incremental: nearest-first, lotes de LOTE_SLUGS por moneda (events?slug=a&slug=b...), <= MAX_LOTES_CICLO por ciclo.
# 429 de gamma: se aborta la rafaga al primer 429 (sin reintento inmediato) y se PAUSA toda llamada a gamma hasta xx+1:02 si el
# 429 llega en xx:40-xx:59 (ventana observada xx:46..xx+1:01), o 120 s en otro caso. La pausa persiste en ESTADO_PATH
# (capture_markets se relanza cada ~13 min por run_slow).
try:
    import universo_5m_io as U            # solo el adelanto lo necesita; si falta, el adelanto queda apagado y lo demas no cambia
except Exception as _e:                   # pragma: no cover
    U = None
    print(f"  Aviso: universo_5m_io no disponible ({type(_e).__name__}); adelanto 5m apagado", flush=True)


def _env_int(nombre, defecto):
    try:
        return int(os.environ.get(nombre, defecto))
    except (TypeError, ValueError):
        return defecto


HORIZONTE_5M_MIN = _env_int("CAPTURE_5M_HORIZONTE_MIN", 0) if U is not None else 0
LOTE_SLUGS = 12
MAX_LOTES_CICLO = _env_int("CAPTURE_5M_MAX_LOTES_CICLO", 40)
GAMMA_INTERVALO_MIN_S = 0.55           # < 2 GET/s en la ruta nueva
ESTADO_PATH = Path(os.environ.get("CAPTURE_ESTADO_PATH", "/root/polymarket-research-datalogs/capture_5m_estado.json"))
INEXISTENTE_REINTENTO_S = 300
RE_SLUG_5M = re.compile(r"^([a-z]+)-updown-5m-(\d+)$")
_GAMMA_URL_EVENTS = "https://gamma-api.polymarket.com/events"
_ESTADO = {"cargado": False, "pausa_hasta": 0.0, "inexistente": {}}
_RAFAGA = {"abortada": False, "ultimo_get": 0.0}
_GET = {"fn": None}                     # inyectable en tests (sin red)


class _Gamma429(Exception):
    pass


def _gamma_get(url, params, throttle=False):
    """GET a gamma con deteccion de 429 (-> _Gamma429, sin reintento). throttle: separa llamadas >= GAMMA_INTERVALO_MIN_S."""
    if _RAFAGA["abortada"]:
        raise _Gamma429("rafaga ya abortada")
    if throttle:
        espera = GAMMA_INTERVALO_MIN_S - (time.monotonic() - _RAFAGA["ultimo_get"])
        if espera > 0:
            time.sleep(espera)
    _RAFAGA["ultimo_get"] = time.monotonic()
    fn = _GET["fn"] or (lambda u, p: requests.get(u, params=p, headers=HEADERS_HTTP, timeout=TIMEOUT))
    r = fn(url, params)
    if r.status_code == 429:
        _marcar_429()
        raise _Gamma429("HTTP 429")
    r.raise_for_status()
    return r.json()


def _pausa_tras_429(ahora_dt):
    """xx+1:02 si el 429 llega en xx:40-xx:59; 120 s en otro caso (misma regla que universo_5m_io.pausa_tras_429)."""
    if ahora_dt.minute >= 40:
        return (ahora_dt.replace(minute=2, second=0, microsecond=0) + timedelta(hours=1)).timestamp()
    return (ahora_dt + timedelta(seconds=120)).timestamp()


def _marcar_429():
    if not _RAFAGA["abortada"]:
        _RAFAGA["abortada"] = True
        _cargar_estado()
        _ESTADO["pausa_hasta"] = _pausa_tras_429(datetime.now(timezone.utc))
        _guardar_estado()
        print(f"  [429] gamma: rafaga abortada; sin llamadas a gamma hasta "
              f"{datetime.fromtimestamp(_ESTADO['pausa_hasta'], timezone.utc).strftime('%H:%M:%S')}Z", flush=True)


def gamma_en_pausa():
    _cargar_estado()
    return time.time() < _ESTADO["pausa_hasta"]


def _cargar_estado():
    if _ESTADO["cargado"]:
        return
    _ESTADO["cargado"] = True
    try:
        d = json.loads(ESTADO_PATH.read_text())
        p = float(d.get("pausa_hasta", 0.0))
        # defensa ante reloj/estado absurdo: una pausa nunca excede 70 min desde ahora (xx:40 -> xx+1:02 son <= 22 min)
        _ESTADO["pausa_hasta"] = p if p <= time.time() + 4200 else 0.0
    except (OSError, ValueError, TypeError, AttributeError):
        pass                              # sin estado / corrupto: sin pausa (el 1er 429 la recrea)


def _guardar_estado():
    """Atomico: tmp en el mismo directorio + fsync + replace."""
    try:
        ESTADO_PATH.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=str(ESTADO_PATH.parent), prefix=ESTADO_PATH.name + ".tmp")
        with os.fdopen(fd, "w") as f:
            json.dump({"pausa_hasta": _ESTADO["pausa_hasta"]}, f)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, ESTADO_PATH)
    except OSError as e:
        print(f"  Aviso: no se pudo guardar el estado ({e})", flush=True)


COINGECKO_IDS = {
    "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana",
    "XRP": "ripple", "DOGE": "dogecoin", "BNB": "binancecoin",
    "ADA": "cardano", "LINK": "chainlink", "AVAX": "avalanche-2",
    "DOT": "polkadot", "MATIC": "matic-network", "LTC": "litecoin",
}
SPOT_SYMBOLS = list(COINGECKO_IDS.keys())

# PRICE_RANGES importado de data_quality (fuente única de verdad)

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
            lote = _gamma_get(url, params)
        except _Gamma429:
            print(f"  429 gamma slug={slug} offset={offset}: lista de tag incompleta (rafaga abortada)")
            break
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
        if _RAFAGA["abortada"]:
            break
        for asset in UPDOWN_ASSETS:
            event_slug = f"{asset}-{prefix}-{ts}"
            try:
                datos = _gamma_get(url, {"slug": event_slug})
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
            except _Gamma429:
                break                      # rafaga abortada: ninguna llamada mas en este ciclo
            except Exception:
                pass  # slug no existe aún para ventanas futuras

    if encontrados:
        print(f"  Up/Down {prefix}: {encontrados} mercados activos")
    return mercados


def fetch_todos_updown() -> list:
    """Captura mercados Up/Down de todos los horizontes configurados."""
    mercados = []
    for horizonte in UPDOWN_HORIZONTES:
        if _RAFAGA["abortada"]:
            break
        mercados += fetch_updown_por_horizonte(horizonte)
    return mercados


def _mercados_de_evento(ev):
    """Mismas anotaciones/filtros que fetch_updown_por_horizonte para los mercados de un evento."""
    ev_id, ev_title, ev_slug = ev.get("id", ""), ev.get("title", ""), ev.get("slug", "")
    ev_vol24 = ev.get("volume24hr", "")
    tags = "|".join([t.get("label", "") for t in (ev.get("tags") or []) if isinstance(t, dict) and t.get("label")])
    out = []
    for m in ev.get("markets") or []:
        end_date = (m.get("endDate") or "")[:19]
        if es_expirado(end_date):
            continue
        precios = parse_outcome_prices(m.get("outcomePrices"))
        py = precios[0] if precios and len(precios) >= 1 else ""
        try:
            if not py or float(py) <= 0:
                continue
        except (TypeError, ValueError):
            continue
        m["_event_id"], m["_event_title"], m["_event_slug"] = ev_id, ev_title, ev_slug
        m["_event_volume24hr"], m["_event_tags"] = ev_vol24, tags
        out.append(m)
    return out


def fetch_updown_5m_adelanto(ahora_ts=None, horizonte_min=None, ya_vistos=(), conocidos=None):
    """Mercados updown-5m por delante de fetch_updown_por_horizonte (que cubre siguiente..+2), hasta horizonte_min.
    conocidos: slugs ya presentes en el fichero de tokens (hoy+ayer); por defecto se leen de universo_5m_io.
    Incremental, nearest-first, lotes de LOTE_SLUGS slugs por moneda, <= MAX_LOTES_CICLO lotes por ciclo. Lote fallido (red/5xx/JSON):
    no se da por hecho, se imprime y se reintenta en el ciclo siguiente; 429: aborta la rafaga.
    Devuelve (mercados, filas_tokens, contadores): el llamador escribe PRIMERO adelanto_<dia>.csv y DESPUES filas_tokens (commit)."""
    horizonte_min = HORIZONTE_5M_MIN if horizonte_min is None else horizonte_min
    cont = {"esperados": 0, "pendientes": 0, "lotes": 0, "lotes_fallidos": 0, "recibidos": 0, "inexistentes": 0,
            "abortado_429": False, "tokens_invalidos": 0}
    if horizonte_min <= 0 or _RAFAGA["abortada"]:
        return [], [], cont
    _cargar_estado()
    ahora_ts = int(ahora_ts if ahora_ts is not None else time.time())
    if ahora_ts < _ESTADO["pausa_hasta"]:
        return [], [], cont
    if conocidos is None:
        mk, _st = U.leer(ahora_ts)
        conocidos = {r["slug"] for r in mk.values()}
    siguiente = ((ahora_ts // 300) + 1) * 300
    primero = siguiente + 3 * 300                               # las 3 primeras ya las cubre fetch_updown_por_horizonte
    wins = list(range(primero, ahora_ts + horizonte_min * 60 + 1, 300))
    _ESTADO["inexistente"] = {k: v for k, v in _ESTADO["inexistente"].items() if v > ahora_ts}
    pend = {}
    for a in UPDOWN_ASSETS:
        pend[a] = [t for t in wins if f"{a}-updown-5m-{t}" not in conocidos and (a, t) not in ya_vistos
                   and _ESTADO["inexistente"].get((a, t), 0) <= ahora_ts]
        cont["esperados"] += len(wins)
        cont["pendientes"] += len(pend[a])
    lotes = []
    for a in UPDOWN_ASSETS:
        for i in range(0, len(pend[a]), LOTE_SLUGS):
            lotes.append((pend[a][i], a, pend[a][i:i + LOTE_SLUGS]))
    lotes.sort(key=lambda x: (x[0], x[1]))
    mercados, filas_tok = [], []
    fallos_seguidos = 0
    for _, a, tss in lotes[:MAX_LOTES_CICLO]:
        slugs = [f"{a}-updown-5m-{t}" for t in tss]
        cont["lotes"] += 1
        try:
            datos = _gamma_get(_GAMMA_URL_EVENTS, [("slug", s) for s in slugs], throttle=True)
            if not isinstance(datos, list):
                raise ValueError(f"respuesta no lista: {type(datos).__name__}")
        except _Gamma429:
            cont["abortado_429"] = True
            break
        except Exception as e:
            cont["lotes_fallidos"] += 1
            fallos_seguidos += 1
            print(f"  Error gamma lote {a} {tss[0]}..{tss[-1]}: {type(e).__name__}: {e} (se reintenta en el ciclo siguiente)", flush=True)
            if fallos_seguidos >= 3:
                print("  3 lotes seguidos fallidos: se corta el adelanto de este ciclo", flush=True)
                break
            continue
        fallos_seguidos = 0
        t_recv = int(time.time() * 1000)
        por_slug = {ev.get("slug"): ev for ev in datos if isinstance(ev, dict)}
        for t, s in zip(tss, slugs):
            ev = por_slug.get(s)
            if ev is None:
                cont["inexistentes"] += 1
                _ESTADO["inexistente"][(a, t)] = ahora_ts + INEXISTENTE_REINTENTO_S
                continue
            ft = U.filas_de_evento_gamma(ev, t_recv, fuente="capture")
            if not ft:                                           # sin tokens/outcomes validos todavia: NO se da por hecho
                cont["tokens_invalidos"] += 1
                continue
            mercados += _mercados_de_evento(ev)
            filas_tok += ft
            cont["recibidos"] += 1
    return mercados, filas_tok, cont


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


def guardar_mercados(mercados, ts, archivo=None):
    """Una SOLA escritura (O_APPEND) del bloque entero: un kill a mitad no deja lineas partidas ni bloques parciales
    visibles para los lectores incrementales de _universo_activo (que cortan en el ultimo '\\n')."""
    fecha   = ts[:10]
    archivo = archivo or (DIR_MARKETS / f"{fecha}.csv")
    archivar_si_obsoleto(archivo, CABECERA_MARKETS)
    nuevo = not archivo.exists()
    buf = io.StringIO(newline="")
    w = csv.writer(buf)
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
    if mercados or nuevo:
        archivo.parent.mkdir(parents=True, exist_ok=True)
        with open(archivo, "ab") as f:
            f.write(buf.getvalue().encode("utf-8"))


def guardar_precios(precios, ts):
    fecha   = ts[:10]
    archivo = DIR_PRICES / f"{fecha}.csv"
    nuevo   = not archivo.exists()

    # L1: validar rango para cada precio de CoinGecko
    precios_validos: dict[str, float] = {}
    rechazados: list[str] = []
    for sym in SPOT_SYMBOLS:
        v = precios.get(sym)
        if v is None:
            continue
        ok, motivo = validar_precio(sym, v)
        if ok:
            precios_validos[sym] = float(v)
        else:
            rechazados.append(f"{sym}({motivo})")
    if rechazados:
        print(f"  [DQ L1] CoinGecko rechazados: {', '.join(rechazados)}")

    fuentes: dict[str, str] = {sym: "coingecko" for sym in precios_validos}

    # L4: cross-source — comparar CoinGecko con Coinbase para assets principales
    assets_check = [s for s in ["BTC", "ETH", "SOL", "XRP"] if s in precios_validos]
    if assets_check:
        try:
            coinbase = fetch_coinbase_spot(assets_check, timeout=5)
            cg_subset = {s: precios_validos[s] for s in assets_check}
            cross = validar_cross_source(
                {"coingecko": cg_subset, "coinbase": coinbase}, assets_check
            )
            for a in cross.get("alertas", []):
                icon = "🚨" if a["accion"] == "BLOQUEADO" else "⚠️"
                print(f"  [DQ L4] {icon} CoinGecko {a['sym']} div={a['max_div_pct']:.2f}%")
            # Si Coinbase está disponible y CoinGecko diverge >2%, usar Coinbase
            for sym in cross.get("bloqueados", []):
                if sym in coinbase:
                    precios_validos[sym] = coinbase[sym]
                    fuentes[sym] = "coinbase"
                    print(f"  [DQ L4] {sym}: usando Coinbase en lugar de CoinGecko (bloqueado)")
        except Exception as _e:
            pass   # cross-source es best-effort; no bloquea el guardado

    # El fichero puede haber sido creado ya por fetch_binance_klines.py con
    # columna "source" (o no) — igualar el esquema real del fichero en vez de
    # asumirlo, para no mezclar filas de 5 y 6 campos en el mismo CSV (eso
    # deja algunas filas con source=None para siempre, indistinguibles del
    # exchange real que las originó).
    tiene_col_source = True
    if not nuevo:
        with open(archivo, encoding="utf-8") as pf:
            tiene_col_source = "source" in (pf.readline().strip().split(","))

    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow(["timestamp_utc", "asset", "price_usd", "change_1h_pct", "change_24h_pct", "source"])
        for sym, price in precios_validos.items():
            fila = [ts, sym, price, "", ""]
            if tiene_col_source:
                fila.append(fuentes.get(sym, "coingecko"))
            w.writerow(fila)


def una_captura():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    n_mkt, n_px = 0, 0
    try:
        precios = fetch_coingecko_prices()
        n_px = sum(1 for v in precios.values() if v is not None)
        guardar_precios(precios, ts)
    except Exception as e:
        print(f"  ERROR precios: {type(e).__name__}: {e}")
    _RAFAGA["abortada"] = False
    if gamma_en_pausa():
        _RAFAGA["abortada"] = True          # sin llamadas a gamma hasta el fin de la pausa (429 previo)
        print(f"  gamma en pausa tras 429 hasta "
              f"{datetime.fromtimestamp(_ESTADO['pausa_hasta'], timezone.utc).strftime('%H:%M:%S')}Z: ciclo sin gamma")
        return n_mkt, n_px
    try:
        eventos   = fetch_todos_eventos_crypto()
        mercados  = extraer_mercados_de_eventos(eventos)
        mercados += fetch_todos_updown()
        n_mkt     = len(mercados)
        guardar_mercados(mercados, ts)
        print(f"  Eventos únicos: {len(eventos)} → mercados totales: {n_mkt}")
    except Exception as e:
        print(f"  ERROR polymarket: {type(e).__name__}: {e}")
        mercados, eventos = [], []
    if HORIZONTE_5M_MIN > 0 and not _RAFAGA["abortada"]:
        try:
            U.retencion()
            adel, filas_tok, c = fetch_updown_5m_adelanto()
            if filas_tok:
                dia = ts[:10]
                guardar_mercados(adel, ts, archivo=U.UNIV_DIR / f"adelanto_{dia}.csv")   # 1) auditoria (mismo esquema que data/markets)
                U.escribir(filas_tok)                                                   # 2) commit: tokens (fuente de "ya hecho")
            print(f"  Adelanto 5m ({HORIZONTE_5M_MIN} min): esperados {c['esperados']}, pendientes {c['pendientes']}, "
                  f"lotes {c['lotes']} (fallidos {c['lotes_fallidos']}), eventos recibidos {c['recibidos']}, "
                  f"aun inexistentes {c['inexistentes']}, sin tokens validos {c['tokens_invalidos']}, filas escritas {len(filas_tok)}"
                  + (", 429: rafaga abortada" if c["abortado_429"] else ""))
        except Exception as e:
            print(f"  ERROR adelanto 5m: {type(e).__name__}: {e}")
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
