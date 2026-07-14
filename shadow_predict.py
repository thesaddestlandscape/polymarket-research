"""
shadow_predict.py — v8. Cuatro estrategias activas:
  1. PRICE_MOMENTUM — tendencia exponencial del precio YES en historial de mercados
  2. SMART_FLOW_1H  — flujo de compras recientes (ultimo 1h, wallets humanas)
  3. UPDOWN_GBM     — mercados Up/Down via modelo Black-Scholes digital (daily/hourly/slot)
  4. WEEKLY_PRICE   — mercados de rango de precio semanal (BTC/ETH/SOL entre $X-$Y)
"""
import csv, glob, io, json, math, os, pickle, re, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
import requests

from data_quality import (
    SIGMA_H_MAX, DRIFT_MAX, ASSETS_GBM,
    validar_features_gbm, simbolo_bloqueado, generar_reporte, obtener_consensus_spot,
)

_HAS_PANDAS: bool | None = None   # None = not yet checked; True/False after first use
_pd = None                         # populated lazily on first cache miss

def _check_pandas():
    global _HAS_PANDAS, _pd
    if _HAS_PANDAS is None:
        try:
            import pandas as _pd_mod  # noqa: PLC0415
            _pd = _pd_mod
            _HAS_PANDAS = True
        except ImportError:
            _HAS_PANDAS = False
    return _HAS_PANDAS

TIMEOUT = 30
HORIZONTE_MIN_HORAS = 0.05    # 3 min: cubre mercados Up/Down 5m
HORIZONTE_MAX_HORAS = 365 * 24  # 1 anno
EDGE_MINIMO = 0.02
SLIPPAGE_ESTIMADO = 0.02          # fallback; ver _slippage_estimado_dinamico()
SLIPPAGE_MIN_N = 30               # fills live con slip_real necesarios para recalibrar
SLIPPAGE_FLOOR = 0.005            # nunca asumir slippage mejor que esto
SLIPPAGE_VENTANA = 60             # últimos N fills (el régimen post-requote domina)
MIN_LIQUIDEZ = 500

DIR_DATA    = Path("data")
DIR_SHADOW  = DIR_DATA / "shadow"
DIR_LIVE    = DIR_DATA / "live"


def _slippage_estimado_dinamico() -> float:
    """
    Recalibra SLIPPAGE_ESTIMADO con el slippage real de los fills live
    (live_trade guarda `slip_real=±X` en notas desde 2026-07-03). Gate n≥30;
    mediana sobre los últimos SLIPPAGE_VENTANA fills (robusta a los outliers
    pre-veto-profundidad +0.085/+0.04) con clamp [SLIPPAGE_FLOOR, 0.02].
    Cualquier problema → fallback a la constante 0.02 (fail-safe).
    """
    try:
        slips = []
        with open(DIR_DATA / "live" / "trades.csv", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                m = re.search(r"slip_real=([+-]?[\d.]+)", row.get("notas", "") or "")
                if m:
                    slips.append(float(m.group(1)))
        slips = slips[-SLIPPAGE_VENTANA:]
        if len(slips) < SLIPPAGE_MIN_N:
            return SLIPPAGE_ESTIMADO
        mediana = sorted(slips)[len(slips) // 2]
        return round(min(max(mediana, SLIPPAGE_FLOOR), SLIPPAGE_ESTIMADO), 4)
    except Exception:
        return SLIPPAGE_ESTIMADO

_FUNDING_CACHE: dict = {}          # {activo: rate} — en memoria, TTL gestionado por mtime
_FUNDING_CACHE_FILE = DIR_DATA / "funding_rates_cache.json"
_FUNDING_SYMBOLS = {"BTC": "BTCUSDT", "ETH": "ETHUSDT", "SOL": "SOLUSDT", "XRP": "XRPUSDT"}
FUNDING_TTL_S = 1800               # 30 min — las rates cambian cada 8h


def _fetch_funding_rates() -> dict:
    """
    Funding rates actuales de perps Binance para BTC/ETH/SOL/XRP.
    Devuelve {activo: last_funding_rate_8h} como decimal (ej: 0.0001 = 0.01%/8h).
    Usa caché en disco con TTL=30min para no penalizar el fast loop.
    """
    global _FUNDING_CACHE
    # Comprobar caché en disco
    if _FUNDING_CACHE_FILE.exists():
        age_s = (datetime.now(timezone.utc).timestamp()
                 - _FUNDING_CACHE_FILE.stat().st_mtime)
        if age_s < FUNDING_TTL_S:
            if not _FUNDING_CACHE:
                try:
                    _FUNDING_CACHE = json.loads(_FUNDING_CACHE_FILE.read_text())
                except Exception:
                    pass
            if _FUNDING_CACHE:
                return _FUNDING_CACHE

    rates = {}
    for activo, sym in _FUNDING_SYMBOLS.items():
        try:
            resp = requests.get(
                "https://fapi.binance.com/fapi/v1/premiumIndex",
                params={"symbol": sym},
                timeout=5,
            )
            if resp.status_code == 200:
                rates[activo] = float(resp.json().get("lastFundingRate", 0))
        except Exception:
            pass

    if rates:
        _FUNDING_CACHE = rates
        try:
            _FUNDING_CACHE_FILE.write_text(json.dumps(rates))
        except Exception:
            pass
    return rates


def _cargar_params_dinamicos() -> dict:
    """Lee strategy_params.json generado por postmortem. Devuelve {} si no existe."""
    path = DIR_SHADOW / "strategy_params.json"
    if not path.exists():
        return {}
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        return data.get("estrategias", {})
    except Exception:
        return {}

def _cargar_meta_params() -> dict:
    """Lee la sección 'meta' de strategy_params.json — parámetros auto-aplicados por hypothesis_tracker."""
    path = DIR_SHADOW / "strategy_params.json"
    if not path.exists():
        return {}
    try:
        return json.load(open(path, encoding="utf-8")).get("meta", {})
    except Exception:
        return {}
DIR_MARKETS = DIR_DATA / "markets"
DIR_TRADES  = DIR_DATA / "trades"
DIR_BINANCE = DIR_DATA / "binance"
DIR_SHADOW.mkdir(parents=True, exist_ok=True)

def _norm_cdf(x):
    if x < -8.0: return 0.0
    if x >  8.0: return 1.0
    sign = 1.0 if x >= 0 else -1.0
    x = abs(x)
    t = 1.0 / (1.0 + 0.2316419 * x)
    d = 0.3989422820 * math.exp(-0.5 * x * x)
    p = d * t * (0.3193815302
        + t * (-0.3565637813
        + t * (1.7814779372
        + t * (-1.8212559978
        + t * 1.3302744929))))
    return 1.0 - p if sign > 0 else p

def _norm_ppf(p, lo=-8.0, hi=8.0, it=60):
    """Inversa de _norm_cdf por bisección — usada por la recalibración Platt (calibracion_prob)."""
    if p <= 1e-9: return -8.0
    if p >= 1 - 1e-9: return 8.0
    for _ in range(it):
        mid = (lo + hi) / 2
        if _norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2

# Features observacionales de calendario astronómico (2026-07-01) — inspirado en
# Fornero, "La doctrina de la astrología financiera" (43 Jornadas SADAF, 2023):
# el paper es escéptico de la astrología en sí, pero documenta 2 efectos empíricos
# replicados en revistas peer-review, con mecanismo NO místico (sesgo de humor /
# creencia supersticiosa de inversores retail, más fuerte en mercados dominados
# por minoristas — igual que Polymarket): fase lunar (Dichev & Janes 2003 y otros,
# ~5-10%/año) y Mercurio retrógrado (Qi/Wang/Zhang 2022, Kou & Ma 2022, -3% a -31%
# anualizado). Solo observacional, no cambia ninguna decisión — necesitamos meses
# de calendario (no solo más operaciones) para tener suficientes ciclos lunares y
# ventanas de retrogradación distintas. Ver H-CUSTOM-MOON-PHASE y
# H-CUSTOM-MERCURY-RETROGRADO en hipotesis_custom.json.
_MOON_SYNODIC_DIAS = 29.530588853
_MOON_REF_NUEVA = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)

def _moon_phase(dt):
    """0.0=luna nueva, 0.5=luna llena, ciclo continuo 0-1."""
    dias = (dt - _MOON_REF_NUEVA).total_seconds() / 86400.0
    return round((dias % _MOON_SYNODIC_DIAS) / _MOON_SYNODIC_DIAS, 4)

# Ventanas de Mercurio retrógrado (fechas públicas, actualizar cada año — ver
# almanac.com o astro-seek.com). 2026 confirmadas:
MERCURIO_RETROGRADO_VENTANAS = [
    (datetime(2026, 2, 26, tzinfo=timezone.utc), datetime(2026, 3, 20, tzinfo=timezone.utc)),
    (datetime(2026, 6, 29, tzinfo=timezone.utc), datetime(2026, 7, 23, tzinfo=timezone.utc)),
    (datetime(2026, 10, 24, tzinfo=timezone.utc), datetime(2026, 11, 13, tzinfo=timezone.utc)),
]

def _mercurio_retrogrado(dt):
    return any(lo <= dt <= hi for lo, hi in MERCURIO_RETROGRADO_VENTANAS)


# Pre-FOMC announcement drift (Lucca & Moench, JF/NY Fed, SSRN 1923197,
# artículo pasado por Javi 11-Jul): gran parte de la prima de equities se
# concentra en las ~24h ANTES del anuncio programado del FOMC (14:00 ET del
# 2º día de reunión). Cripto correlaciona con equities en macro → feature
# observacional de calendario, mismo patrón que moon_phase/mercury: solo
# loguea, NO toca ninguna decisión. n acumula lento (8 reuniones/año) — el
# pipeline causal decidirá con n suficiente si BUY_YES pre-FOMC rinde
# distinto. Fechas confirmadas federalreserve.gov 11-Jul-2026; 14:00 ET =
# 18:00 UTC en horario de verano, 19:00 UTC en invierno (Oct salida DST 01-Nov).
FOMC_ANUNCIOS_UTC = [
    datetime(2026, 7, 29, 18, 0, tzinfo=timezone.utc),
    datetime(2026, 9, 16, 18, 0, tzinfo=timezone.utc),
    datetime(2026, 10, 28, 18, 0, tzinfo=timezone.utc),
    datetime(2026, 12, 9, 19, 0, tzinfo=timezone.utc),
]

def _horas_hasta_fomc(dt):
    """Horas hasta el próximo anuncio FOMC (float, redondeado a 0.1h).
    None si no hay anuncio futuro en el calendario (fail-soft: recordar
    ampliar FOMC_ANUNCIOS_UTC con el calendario 2027 en diciembre)."""
    futuros = [f for f in FOMC_ANUNCIOS_UTC if f > dt]
    if not futuros:
        return None
    return round((min(futuros) - dt).total_seconds() / 3600.0, 1)

ACTIVOS_REF = {
    "BTC":  ("bitcoin",  "btc"),
    "ETH":  ("ethereum", "eth"),
    "SOL":  ("solana",   "sol"),
    "XRP":  ("xrp",      "ripple"),
    "DOGE": ("dogecoin", "doge", "dogo"),
    "BNB":  ("bnb",      "binance coin"),
    "MSTR": ("microstrategy", "mstr"),
}

BINANCE_SYMBOLS = {
    "BTC":  "BTCUSDT",
    "ETH":  "ETHUSDT",
    "SOL":  "SOLUSDT",
    "XRP":  "XRPUSDT",
    "DOGE": "DOGEUSDT",
    "BNB":  "BNBUSDT",
}

def identificar_activo(question):
    q = (question or "").lower()
    best, best_len = None, 0
    for tk, kws in ACTIVOS_REF.items():
        for kw in kws:
            if kw in q and len(kw) > best_len:
                best, best_len = tk, len(kw)
    return best

def horas_a_vencimiento(end_date_str):
    if not end_date_str:
        return None
    try:
        s = end_date_str
        if "T" not in s and len(s) == 10:
            s = s + "T23:59:59"
        if not s.endswith("Z") and "+" not in s[10:]:
            s = s + "+00:00"
        else:
            s = s.replace("Z", "+00:00")
        return (datetime.fromisoformat(s) - datetime.now(timezone.utc)).total_seconds() / 3600
    except Exception:
        return None

def _cache_path(nombre: str) -> Path:
    return DIR_DATA / "shadow" / f"_cache_{nombre}.pkl"


def _cache_valida(cache_file: Path, fuentes: list = None, ttl_s: int = 90) -> bool:
    """True si el cache existe y no ha expirado el TTL temporal.
    No compara mtimes de fuentes — el slow loop actualiza los CSV cada ~23min
    pero los datos son válidos para el fast loop durante ttl_s segundos."""
    if not cache_file.exists():
        return False
    cache_mtime = cache_file.stat().st_mtime
    ahora = datetime.now(timezone.utc).timestamp()
    return (ahora - cache_mtime) <= ttl_s


def cargar_mercados_recientes():
    """
    Devuelve la snapshot más reciente de cada mercado activo.
    Lee solo la cola de today's CSV (los archivos de mercado crecen hasta 700MB/día).
    Se cubre con ayer solo si hoy tiene < 200 filas (arranque a medianoche).
    TTL cache 90s: necesitamos datos frescos para price_yes actual.
    """
    fecha_hoy  = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    fecha_ayer = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")

    cache_file = _cache_path("mercados_recientes")
    if _cache_valida(cache_file, ttl_s=90):
        with open(cache_file, "rb") as f:
            return pickle.load(f)

    # Leer solo los últimos ~100MB de hoy (contiene las últimas 100-110 capturas ≈ 4h de datos)
    # Suficiente para obtener el snapshot más reciente de todos los mercados activos.
    BYTES_COLA = 100 * 1024 * 1024
    archivos_a_leer = [DIR_MARKETS / f"{fecha_hoy}.csv"]

    por_id: dict = {}

    for arch in archivos_a_leer:
        if not arch.exists():
            continue
        fsize = arch.stat().st_size
        skip  = max(0, fsize - BYTES_COLA)
        try:
            with open(arch, "rb") as fb:
                header = fb.readline().decode("utf-8", errors="replace").strip()
                fieldnames = [h.strip() for h in header.split(",")]
                if skip > 0:
                    fb.seek(skip)
                    fb.readline()
                content = fb.read()
        except Exception as e:
            print(f"  Error leyendo {arch.name}: {e}")
            continue

        if _check_pandas():
            try:
                df = _pd.read_csv(
                    io.BytesIO(content), names=fieldnames,
                    on_bad_lines="skip", dtype=str, engine="c",
                )
                df = df[df["market_id"].notna() & (df["market_id"] != "")]
                # Último snapshot por market_id (el CSV está en orden cronológico)
                df = df.groupby("market_id", as_index=False).last()
                resultado = df.to_dict("records")
                # Si el archivo empieza hoy y tiene poca data, añadir de ayer
                if len(resultado) < 200:
                    archivos_a_leer.append(DIR_MARKETS / f"{fecha_ayer}.csv")
                else:
                    for row in resultado:
                        mid = row.get("market_id", "")
                        if mid and (mid not in por_id or row.get("timestamp_utc","") > por_id[mid].get("timestamp_utc","")):
                            por_id[mid] = row
                    continue  # pandas path done
            except Exception:
                pass  # fallback below

        # Fallback: csv.DictReader
        try:
            for row in csv.DictReader(io.StringIO(content.decode("utf-8", errors="replace")), fieldnames=fieldnames):
                mid = row.get("market_id", "")
                if not mid:
                    continue
                ts = row.get("timestamp_utc", "")
                if mid not in por_id or ts > por_id[mid].get("timestamp_utc", ""):
                    por_id[mid] = row
        except Exception as e:
            print(f"  Error parseando {arch.name}: {e}")

    resultado = list(por_id.values())
    # Si muy pocos resultados (arranque en frío), también leer ayer
    if len(resultado) < 200:
        arch_ayer = DIR_MARKETS / f"{fecha_ayer}.csv"
        if arch_ayer.exists():
            fsize = arch_ayer.stat().st_size
            skip  = max(0, fsize - BYTES_COLA)
            try:
                with open(arch_ayer, "rb") as fb:
                    header = fb.readline().decode("utf-8", errors="replace").strip()
                    fieldnames = [h.strip() for h in header.split(",")]
                    if skip > 0:
                        fb.seek(skip); fb.readline()
                    content = fb.read()
                for row in csv.DictReader(io.StringIO(content.decode("utf-8", errors="replace")), fieldnames=fieldnames):
                    mid = row.get("market_id", "")
                    if not mid:
                        continue
                    ts = row.get("timestamp_utc", "")
                    if mid not in por_id or ts > por_id[mid].get("timestamp_utc", ""):
                        por_id[mid] = row
            except Exception:
                pass
            resultado = list(por_id.values())

    with open(cache_file, "wb") as f:
        pickle.dump(resultado, f)
    return resultado


def _leer_historial_archivo(arch: Path, corte: datetime, bytes_cola: int) -> dict:
    """
    Lee solo los últimos `bytes_cola` de un CSV de mercados y filtra a ts >= corte.
    Usa pandas si disponible (2× más rápido); fallback a csv.DictReader.
    """
    resultado: dict = {}
    fsize = arch.stat().st_size
    skip  = max(0, fsize - bytes_cola)
    try:
        with open(arch, "rb") as fb:
            header = fb.readline().decode("utf-8", errors="replace").strip()
            if skip > 0:
                fb.seek(skip)
                fb.readline()  # descartar línea parcial
            content = fb.read()
    except Exception as e:
        print(f"  Error leyendo {arch.name}: {e}")
        return resultado

    if _check_pandas():
        try:
            df = _pd.read_csv(
                io.BytesIO(content),
                names=header.split(","),
                usecols=["timestamp_utc", "market_id", "price_yes"],
                on_bad_lines="skip",
                dtype=str,
                engine="c",
            )
            df["ts"] = _pd.to_datetime(df["timestamp_utc"], utc=True, errors="coerce")
            df = df[df["ts"] >= _pd.Timestamp(corte)]
            df["py"] = _pd.to_numeric(df["price_yes"], errors="coerce")
            df = df.dropna(subset=["ts", "market_id", "py"])
            ts_list = df["ts"].dt.to_pydatetime()  # tz-aware Python datetime objects
            for mid, ts, py in zip(df["market_id"].values, ts_list, df["py"].values):
                resultado.setdefault(mid, []).append((ts, float(py)))
            return resultado
        except Exception:
            pass  # fallback to csv below

    # Fallback: csv.DictReader
    fieldnames = [h.strip() for h in header.split(",")]
    try:
        for row in csv.DictReader(io.StringIO(content.decode("utf-8", errors="replace")), fieldnames=fieldnames):
            try:
                ts = datetime.fromisoformat(row["timestamp_utc"].replace("Z", "+00:00"))
            except Exception:
                continue
            if ts < corte:
                continue
            mid = row.get("market_id", "")
            py  = row.get("price_yes", "")
            if not mid or not py:
                continue
            try:
                resultado.setdefault(mid, []).append((ts, float(py)))
            except ValueError:
                pass
    except Exception as e:
        print(f"  Error parseando {arch.name}: {e}")
    return resultado


def cargar_historial_mercados():
    ahora = datetime.now(timezone.utc)
    corte = ahora - timedelta(hours=6)

    cache_file = _cache_path("historial_mercados")
    if _cache_valida(cache_file, ttl_s=300):  # 5min TTL: el historial solo cambia con slow loop
        with open(cache_file, "rb") as f:
            return pickle.load(f)

    # Solo hoy + ayer. No incluir ayer si hoy ya tiene ≥6.5h de datos.
    # Cada archivo solo se lee por la cola: ~180MB = ~6h de capturas de mercados.
    BYTES_COLA = 180 * 1024 * 1024
    h_hoy = ahora.hour + ahora.minute / 60
    candidatos = [ahora.strftime("%Y-%m-%d")]
    if h_hoy < 6.5:  # antes de 06:30 UTC: hoy tiene < 6.5h de datos → incluir ayer
        candidatos.append((ahora - timedelta(days=1)).strftime("%Y-%m-%d"))
    archivos = [DIR_MARKETS / f"{d}.csv" for d in candidatos if (DIR_MARKETS / f"{d}.csv").exists()]

    from concurrent.futures import ThreadPoolExecutor
    historial: dict = {}
    with ThreadPoolExecutor(max_workers=len(archivos) or 1) as ex:
        futuros = [ex.submit(_leer_historial_archivo, arch, corte, BYTES_COLA) for arch in archivos]
        for fut in futuros:
            for mid, pts in fut.result().items():
                historial.setdefault(mid, []).extend(pts)

    for mid in historial:
        historial[mid].sort(key=lambda x: x[0])

    with open(cache_file, "wb") as f:
        pickle.dump(historial, f)
    return historial

def cargar_trades_recientes():
    """
    Carga BUY trades de la última 1h desde el CSV de trades.
    Indexa por condition_id (market_id siempre vacío en la data-api de Polymarket).
    """
    corte      = datetime.now(timezone.utc) - timedelta(hours=1)
    fecha_hoy  = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    fecha_ayer = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    archivos   = []
    for fname in [DIR_TRADES / f"{fecha_hoy}.csv", DIR_TRADES / f"{fecha_ayer}.csv"]:
        if Path(fname).exists():
            archivos.append(fname)
    if not archivos:
        return {}
    por_market = {}
    for arch in archivos:
        try:
            with open(arch, encoding="utf-8") as fh:
                for row in csv.DictReader(fh):
                    ts_str = row.get("timestamp_utc", "")
                    try:
                        dt = datetime.fromisoformat(ts_str[:19] + "+00:00")
                    except Exception:
                        continue
                    if dt < corte:
                        continue
                    side = (row.get("side") or "").upper()
                    if side != "BUY":
                        continue
                    # market_id está siempre vacío en data-api → usar condition_id
                    cid    = (row.get("condition_id") or "").strip()
                    wallet = (row.get("wallet") or "").lower()
                    outcome = (row.get("outcome") or "").upper()
                    if not wallet or not cid:
                        continue
                    if outcome == "YES":
                        action = "BUY_YES"
                    elif outcome == "NO":
                        action = "BUY_NO"
                    else:
                        continue
                    por_market.setdefault(cid, {}).setdefault(wallet, []).append(action)
        except Exception as e:
            print(f"  Error leyendo trades {arch}: {e}")
    return por_market

UPDOWN_ASSETS_LOWER = ["btc", "eth", "sol", "xrp", "doge", "bnb"]

def _fetch_slot(slug: str, ahora_iso: str) -> list:
    """Descarga un slot concreto de Polymarket. Llamado en paralelo."""
    url = "https://gamma-api.polymarket.com/events"
    mercados = []
    try:
        r = requests.get(url, params={"slug": slug}, timeout=5)
        if r.status_code != 200:
            return []
        events = r.json() if isinstance(r.json(), list) else []
        for ev in events:
            for m in (ev.get("markets") or []):
                precios_raw = m.get("outcomePrices")
                try:
                    pr = json.loads(precios_raw) if isinstance(precios_raw, str) else precios_raw
                    py = float(pr[0]) if pr else None
                except Exception:
                    py = None
                if py is None or not (0.01 < py < 0.99):
                    continue
                mercados.append({
                    "market_id":    m.get("id", ""),
                    "condition_id": m.get("conditionId", ""),
                    "question":     m.get("question", ""),
                    "slug":         m.get("slug", ""),
                    "end_date":     (m.get("endDate") or "")[:19],
                    "liquidity":    m.get("liquidity", ""),
                    "spread":       m.get("spread", ""),
                    "price_yes":    py,
                    "event_tags":   "|".join(t.get("slug","") for t in (ev.get("tags") or [])),
                    "timestamp_utc": ahora_iso,
                })
    except Exception:
        pass
    return mercados


def fetch_slots_directos(horizonte_min=5, ventanas_adelante=2):
    """
    Consulta Polymarket por slots activos/próximos de 5min y 15min en paralelo.
    Todas las combinaciones (asset × ventana) se lanzan simultáneamente.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed
    ahora = datetime.now(timezone.utc)
    ahora_iso = ahora.isoformat(timespec="seconds")
    intervalo_s = horizonte_min * 60
    ts_base = (int(ahora.timestamp()) // intervalo_s) * intervalo_s
    prefix = f"updown-{horizonte_min}m"

    slugs = [
        f"{asset}-{prefix}-{ts_base + delta * intervalo_s}"
        for delta in range(ventanas_adelante + 1)
        for asset in UPDOWN_ASSETS_LOWER
    ]

    mercados = []
    with ThreadPoolExecutor(max_workers=len(slugs)) as executor:
        futuros = {executor.submit(_fetch_slot, slug, ahora_iso): slug for slug in slugs}
        for futuro in as_completed(futuros):
            try:
                mercados.extend(futuro.result())
            except Exception:
                pass
    return mercados


def _smart_flow_activa() -> bool:
    """Comprueba si SMART_FLOW_1H está activa en strategy_params.json."""
    try:
        path = DIR_SHADOW / "strategy_params.json"
        if not path.exists():
            return True
        with open(path, encoding="utf-8") as f:
            params = json.load(f).get("estrategias", {})
        return params.get("SMART_FLOW_1H", {}).get("activa", True)
    except Exception:
        return True


def construir_contexto():
    print("Construyendo contexto...")
    ctx = {}
    ctx["historial_mercados"] = cargar_historial_mercados()
    print(f"  Historial precios YES cargado para {len(ctx['historial_mercados'])} mercados")

    # Trades solo si SMART_FLOW_1H está activa — ahorra 5-6s cuando está desactivada
    if _smart_flow_activa():
        trades = cargar_trades_recientes()
    else:
        trades = {}
    ctx["trades_1h"] = trades
    n_mkt     = len(trades)
    n_wallets = sum(len(v) for v in trades.values())
    print(f"  SMART_FLOW_1H: {n_mkt} mercados, {n_wallets} wallet-acciones en ultima 1h")

    # Precios intraday para UPDOWN_GBM + generar reporte de calidad
    precios_data = cargar_precios_intraday()
    ctx["precios_intraday"] = precios_data
    try:
        # L4: reusa el cache de cross-source (refrescado por fetch_binance_klines.py
        # cada ciclo, TTL 5min) para que simbolo_bloqueado() sepa de divergencias
        # Binance/Coinbase/Kraken. Antes generar_reporte() se llamaba sin
        # cross_result → el bloqueo L4 nunca llegaba al gate real (dead code).
        try:
            cross_result = obtener_consensus_spot(assets=ASSETS_GBM).get("cross", {})
        except Exception as _cross_err:
            print(f"  [DQ] Cross-source no disponible: {_cross_err}")
            cross_result = None
        dq = generar_reporte(precios_data, cross_result=cross_result)
        if dq["estado_global"] != "OK":
            print(f"  [DQ] Estado: {dq['estado_global']} — {dq['alertas']}")
    except Exception as _dq_err:
        print(f"  [DQ] Error generando reporte: {_dq_err}")

    # Spot más reciente + klines raw para ORDER_FLOW_5M
    spot_prices = {}
    klines_raw  = {}
    for _, prices in precios_data[-5:]:
        spot_prices.update(prices)
    try:
        fecha_hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        kf = DIR_BINANCE / f"klines_{fecha_hoy}.json"
        if kf.exists():
            with open(kf, encoding="utf-8") as f:
                kd = json.load(f)
            for sym, klines in kd.items():
                if isinstance(klines, list) and klines:
                    spot_prices[sym] = float(klines[-1][4])
                    klines_raw[sym]  = klines   # todas las velas, con flow si está disponible
            # VWAP de sesión (dict {activo: vwap}) — clave "vwap" del mismo JSON.
            # El bucle de arriba la ignora (no es lista). Feature dist_vwap_pct.
            _vw = kd.get("vwap")
            if isinstance(_vw, dict):
                ctx["vwap_sesion"] = _vw
            # Régimen de volumen (10-Jul, propuesta #5): clave "volumen_regimen"
            # del mismo JSON, mismo patrón que vwap arriba.
            _vr = kd.get("volumen_regimen")
            if isinstance(_vr, dict):
                ctx["volumen_regimen"] = _vr
    except Exception:
        pass
    ctx["spot_prices"] = spot_prices
    ctx["klines_raw"]  = klines_raw
    has_flow = any(len(v[0]) >= 7 for v in klines_raw.values() if v)
    print(f"  UPDOWN_GBM: {len(precios_data)} pts intraday | spot={{{', '.join(f'{k}={v:.4g}' for k, v in list(spot_prices.items())[:4])}}}")
    print(f"  ORDER_FLOW: klines de {len(klines_raw)} activos | flow_real={'sí' if has_flow else 'no (Kraken fallback)'}")

    # Funding rates perps Binance — feature de régimen (crowded longs/shorts)
    funding = _fetch_funding_rates()
    ctx["funding_rates"] = funding
    if funding:
        fr_str = "  ".join(f"{k}={v*100:+.4f}%" for k, v in funding.items())
        print(f"  Funding rates (8h): {fr_str}")
    else:
        print("  Funding rates: sin datos (API inaccesible)")

    return ctx

def s_price_momentum(market, ctx):
    mid = market.get("market_id", "")
    obs = ctx["historial_mercados"].get(mid, [])
    if len(obs) < 5:
        return None
    try:
        liq = float(market.get("liquidity") or 0)
    except (ValueError, TypeError):
        liq = 0.0
    if liq < MIN_LIQUIDEZ:
        return None
    try:
        spread = float(market.get("spread") or 0)
    except (ValueError, TypeError):
        spread = 0.0
    if spread > 0.08:
        return None
    HALF_LIFE_H = 3.0
    ahora      = datetime.now(timezone.utc)
    suma_pesos = 0.0
    suma_pond  = 0.0
    for ts, price in obs:
        horas = (ahora - ts).total_seconds() / 3600
        w     = 0.5 ** (horas / HALF_LIFE_H)
        suma_pesos += w
        suma_pond  += w * price
    if suma_pesos == 0:
        return None
    weighted_avg = suma_pond / suma_pesos
    last_price   = obs[-1][1]
    drift        = last_price - weighted_avg
    if abs(drift) < 0.015:
        return None
    steps = [obs[i+1][1] - obs[i][1] for i in range(len(obs) - 1)]
    if not steps:
        return None
    if drift > 0:
        consistent = sum(1 for s in steps if s > 0)
    else:
        consistent = sum(1 for s in steps if s < 0)
    consistency = consistent / len(steps)
    if consistency < 0.60:
        return None
    py       = market.get("_precio_yes", last_price)
    prob_yes = max(0.05, min(0.95, py + drift * 0.4))
    return {
        "prob_yes": prob_yes,
        "razon": (f"price_momentum drift={drift:+.4f} "
                  f"consistency={consistency:.0%} obs={len(obs)} spread={spread:.3f}"),
        "subtype": identificar_activo(market.get("question", "")) or "",
    }

def s_smart_flow_1h(market, ctx):
    import json as _json, glob as _glob
    if _parse_updown_tipo(market.get("question", ""))[0] is not None:
        return None
    # Lookup por condition_id (market_id siempre vacío en data-api)
    cid    = market.get("condition_id", "")
    trades = ctx.get("trades_1h", {}).get(cid, {})
    top_wallets = ctx.get("top_wallets", set())
    w_stats     = ctx.get("wallet_stats", {})
    if not trades:
        return None
    yes_wallets = set()
    no_wallets  = set()
    for wallet, actions in trades.items():
        n_yes = sum(1 for a in actions if a == "BUY_YES")
        n_no  = sum(1 for a in actions if a == "BUY_NO")
        if n_yes > n_no:
            yes_wallets.add(wallet)
        elif n_no > n_yes:
            no_wallets.add(wallet)
    n_yes  = len(yes_wallets)
    n_no   = len(no_wallets)
    total  = n_yes + n_no
    if total == 0:
        return None
    dominant  = "YES" if n_yes >= n_no else "NO"
    dom_count = n_yes if dominant == "YES" else n_no
    dom_set   = yes_wallets if dominant == "YES" else no_wallets
    if dom_count < 3:
        return None
    imbalance = dom_count / total
    if imbalance < 0.70:
        return None
    n_top = sum(1 for w in dom_set if w in top_wallets and
                w_stats.get(w, {}).get("hit_rate", 0) >= 0.60)
    py         = market.get("_precio_yes", 0.5)
    base_boost = min(0.10, dom_count * 0.03)
    top_boost  = min(0.15, n_top * 0.05)
    if dominant == "YES":
        prob_yes = max(0.05, min(0.95, py + base_boost + top_boost))
        razon    = f"smart_flow_1h {dom_count}w->YES imb={imbalance:.0%} top={n_top}"
    else:
        prob_yes = max(0.05, min(0.95, py - base_boost - top_boost))
        razon    = f"smart_flow_1h {dom_count}w->NO imb={imbalance:.0%} top={n_top}"
    return {
        "prob_yes": prob_yes,
        "razon": razon,
        "subtype": identificar_activo(market.get("question", "")) or "",
    }

def s_binance_updown(market, ctx):
    question = market.get("question", "")
    q_lower = question.lower()
    if "up or down" not in q_lower and "arriba o abajo" not in q_lower:
        return None
    try:
        liq = float(market.get("liquidity") or 0)
    except (ValueError, TypeError):
        liq = 0.0
    if liq <= 100:
        return None
    py_str = market.get("price_yes", "")
    if not py_str:
        return None
    activo = identificar_activo(question)
    if not activo or activo not in BINANCE_SYMBOLS:
        return None
    klines = None
    for delta in (0, 1):
        fecha = (datetime.now(timezone.utc) - timedelta(days=delta)).strftime("%Y-%m-%d")
        path  = DIR_BINANCE / f"klines_{fecha}.json"
        if path.exists():
            try:
                with open(path, encoding="utf-8") as f:
                    data = json.load(f)
                klines = data.get(activo)
                if klines:
                    break
            except Exception:
                pass
    if not klines or len(klines) < 6:
        return None
    klines = klines[-20:]
    try:
        closes = [float(k[4]) for k in klines]
    except (IndexError, ValueError, TypeError):
        return None
    if len(closes) < 6:
        return None
    log_returns = []
    for i in range(1, len(closes)):
        if closes[i - 1] <= 0:
            continue
        log_returns.append(math.log(closes[i] / closes[i - 1]))
    if len(log_returns) < 5:
        return None
    mean_r = sum(log_returns) / len(log_returns)
    var_r  = sum((r - mean_r) ** 2 for r in log_returns) / len(log_returns)
    vol    = math.sqrt(var_r)
    if vol == 0:
        return None
    momentum = (closes[-1] - closes[-5]) / closes[-5]
    z    = momentum / (vol * math.sqrt(5)) * 0.35
    p_up = _norm_cdf(z)
    py = market.get("_precio_yes", 0.5)
    eb = p_up - py
    if abs(eb) <= EDGE_MINIMO + SLIPPAGE_ESTIMADO:
        return None
    prob_yes = max(0.05, min(0.95, p_up))
    return {
        "prob_yes": prob_yes,
        "razon": f"binance_updown {activo} mom={momentum:+.4f} vol={vol:.5f} p_up={p_up:.3f}",
    }


import re as _re
SPOT_PRECIOS = {}

def _cargar_spot():
    if SPOT_PRECIOS:
        return SPOT_PRECIOS
    archivos = sorted(glob.glob(str(DIR_DATA / "prices" / "*.csv")))
    if not archivos:
        return {}
    try:
        with open(archivos[-1], encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        if not rows:
            return {}
        if "asset" in rows[0]:
            # Formato largo (una fila por activo: timestamp,asset,price_usd,...).
            # El parser anterior asumía el formato ancho legacy y devolvía
            # {'price_usd': <último precio>} — .get(activo) era None SIEMPRE,
            # matando en silencio toda estrategia dependiente de spot
            # (WEEKLY_PRICE, RESOLUTION_SNIPER, LATE_WINDOW_5MIN, OU).
            # Detectado 2026-07-02.
            # Prioridad por fuente: coingecko solo como fallback. capture_prices
            # intercala filas coingecko (~cada 72s) con las de consenso (~27s);
            # sin este filtro ~20% de las lecturas usaban el precio coingecko
            # (diff hasta 0.13% vs consenso y potencialmente rancio por 429).
            # Detectado 2026-07-05.
            fallback = {}
            for r in rows:  # la última aparición de cada activo gana
                try:
                    activo = (r.get("asset") or "").upper()
                    precio = float(r["price_usd"])
                except (KeyError, ValueError, TypeError):
                    continue
                if (r.get("source") or "") == "coingecko":
                    fallback[activo] = precio
                else:
                    SPOT_PRECIOS[activo] = precio
            for k, v in fallback.items():
                SPOT_PRECIOS.setdefault(k, v)
            SPOT_PRECIOS.pop("", None)
        else:
            # Formato ancho legacy: última fila, una columna por activo
            for k, v in rows[-1].items():
                if k == "timestamp_utc":
                    continue
                try:
                    SPOT_PRECIOS[k] = float(v)
                except (ValueError, TypeError):
                    pass
    except Exception:
        pass
    return SPOT_PRECIOS

def s_weekly_price(market, ctx):
    import re as _re2
    tags = (market.get("event_tags") or "").lower()
    question = market.get("question", "")
    q = question.lower()
    if "weekly" not in tags and "week" not in q:
        return None
    activo = identificar_activo(question)
    if not activo:
        return None
    spot = _cargar_spot().get(activo)
    if not spot or spot <= 0:
        return None
    py = market.get("_precio_yes", 0.5)

    # Formato: between X and Y
    m = _re2.search(r"between[^0-9]*([0-9,]+(?:\.[0-9]+)?)[^0-9]+([0-9,]+(?:\.[0-9]+)?)", q)
    if m:
        lo = float(m.group(1).replace(",", ""))
        hi = float(m.group(2).replace(",", ""))
        if lo > hi:
            lo, hi = hi, lo
        in_range = lo <= spot <= hi
        if in_range:
            prob_yes = min(0.88, py + 0.15)
        else:
            dist = min(abs(spot - lo), abs(spot - hi))
            pct_dist = dist / spot
            prob_yes = max(0.06, py - 0.20) if pct_dist > 0.20 else max(0.10, py - 0.10)
        T_h = round(market.get("_horas", 0), 4)
        pct_d = round(min(abs(spot-lo), abs(spot-hi))/spot*100, 4) if not in_range else 0.0
        return {
            "prob_yes": max(0.05, min(0.95, prob_yes)),
            "razon": f"weekly_between {activo} spot={spot:.0f} [{lo:.0f},{hi:.0f}] in={in_range}",
            "subtype": activo,
            "features": {"spot": round(spot,2), "in_range": int(in_range), "pct_dist": pct_d, "T_h": T_h},
        }

    # Formato: above/below X
    rm = _re2.search(r"([0-9]{4,}(?:\.[0-9]+)?)", question.replace(",","").replace("$",""))
    if not rm:
        return None
    precio_obj = float(rm.group(1))
    is_above = any(w in q for w in ["above","over","exceed","higher","reach"])
    is_below = any(w in q for w in ["below","under","dip","lower"])
    if not is_above and not is_below:
        return None
    ratio = precio_obj / spot
    if is_above:
        prob_yes = min(0.90, py + 0.12) if ratio < 1.0 else max(0.08, py - 0.10)
    else:
        prob_yes = min(0.90, py + 0.12) if ratio > 1.0 else max(0.08, py - 0.10)
    return {
        "prob_yes": max(0.05, min(0.95, prob_yes)),
        "razon": f"weekly_price {activo} spot={spot:.0f} obj={precio_obj:.0f} ratio={ratio:.3f}",
        "subtype": activo,
        "features": {"spot": round(spot,2), "ratio": round(ratio,4), "is_above": int(is_above), "T_h": round(market.get("_horas",0),4)},
    }


# ─────────────────────────────────────────────────────────────────────────────
# UPDOWN_GBM — Black-Scholes digital para mercados Up/Down
# ─────────────────────────────────────────────────────────────────────────────

def cargar_precios_intraday():
    """Carga prices CSV (hoy y ayer) → lista ordenada de (ts_utc, {sym: float})."""
    SYMS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
    fecha_hoy  = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    fecha_ayer = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    rows = []
    for fecha in [fecha_ayer, fecha_hoy]:
        path = DIR_DATA / "prices" / f"{fecha}.csv"
        if not path.exists():
            continue
        try:
            with open(path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                fieldnames = reader.fieldnames or []
                new_fmt = "asset" in fieldnames
                old_in_new = new_fmt and "BTC" not in fieldnames
                # Si new_fmt: header tiene "asset","price_usd"
                #   - filas limpias:  asset=BTC/ETH/…, price_usd=precio
                #   - filas mixtas:   asset=precio_BTC, price_usd=precio_ETH, …
                #     (escritas por capture_markets con formato viejo en fichero nuevo)
                OLD_IN_NEW_COLS = {  # col_nueva → símbolo
                    "asset": "BTC", "price_usd": "ETH",
                    "change_1h_pct": "SOL", "change_24h_pct": "XRP",
                }
                buf: dict = {}
                buf_ts = None
                def _emit(ts, d):
                    if d and ts: rows.append((ts, dict(d)))
                for row in reader:
                    try:
                        ts = datetime.fromisoformat(
                            row["timestamp_utc"].replace("Z", "+00:00"))
                        if ts.tzinfo is None:
                            ts = ts.replace(tzinfo=timezone.utc)
                    except Exception:
                        continue
                    if new_fmt:
                        asset = row.get("asset", "").strip().upper()
                        if asset in SYMS:
                            # fila limpia formato nuevo — asset conocido
                            try:
                                v = float(row.get("price_usd", ""))
                            except (ValueError, TypeError):
                                continue
                            if ts != buf_ts:
                                _emit(buf_ts, buf); buf, buf_ts = {}, ts
                            buf[asset] = v
                        else:
                            # Distinguir fila vieja (asset=número BTC) de fila nueva
                            # con asset desconocido (LTC, ADA, AVAX…).
                            # BUG CRÍTICO: tratar LTC/ADA como fila vieja mapeaba
                            # price_usd→ETH, provocando ETH=41 y sigma_h=36.
                            try:
                                float(asset)   # si convierte → es precio numérico → fila vieja
                                is_old = True
                            except ValueError:
                                is_old = False  # texto → asset desconocido → IGNORAR
                            if not is_old:
                                continue
                            # fila vieja dentro de fichero nuevo: cada col = un sym
                            prices = {}
                            for col, sym in OLD_IN_NEW_COLS.items():
                                try:
                                    prices[sym] = float(row.get(col, ""))
                                except (ValueError, TypeError):
                                    pass
                            if prices:
                                if ts != buf_ts:
                                    _emit(buf_ts, buf); buf, buf_ts = {}, ts
                                buf.update(prices)
                    else:
                        prices = {}
                        for sym in SYMS:
                            v = row.get(sym, "")
                            if v:
                                try:
                                    prices[sym] = float(v)
                                except ValueError:
                                    pass
                        if prices:
                            rows.append((ts, prices))
                if new_fmt:
                    _emit(buf_ts, buf)
        except Exception as e:
            print(f"  Error precios_intraday {fecha}: {e}")
    rows.sort(key=lambda x: x[0])

    # Deduplicar (ts, sym): si el union-merge de git añadió filas duplicadas,
    # conservar solo la primera aparición de cada (timestamp, asset).
    seen: set = set()
    deduped = []
    for ts, prices in rows:
        ts_key = ts.isoformat()
        clean = {}
        for sym, price in prices.items():
            k = (ts_key, sym)
            if k not in seen:
                seen.add(k)
                clean[sym] = price
        if clean:
            deduped.append((ts, clean))
    return deduped


def _subset_precios_recientes(sym, precios_data, n_min):
    """(ts, precio) de sym en los últimos n_min minutos, con fallback a los
    últimos 60 puntos si hay menos de 5 — lógica compartida por
    _estimar_vol_h y _n_obs_vol_h (antes duplicada en las dos, riesgo de
    que divergieran si se editaba una sin la otra)."""
    ahora = datetime.now(timezone.utc)
    corte = ahora - timedelta(minutes=n_min)
    subset = [(ts, p[sym]) for ts, p in precios_data if sym in p and ts >= corte]
    if len(subset) < 5:
        subset = [(ts, p[sym]) for ts, p in precios_data if sym in p][-60:]
    return subset


def _n_obs_vol_h(sym, precios_data, n_min=120):
    """Nº de log-retornos que usaría _estimar_vol_h para este sym/ventana —
    para exponer barato cuántas observaciones respaldan sigma_h (propuesta
    #2, backlog quant-desk 13-jul: distinguir sigma_h bien estimado de
    sigma_h con pocas klines detrás). Ver _estimar_vol_h."""
    subset = _subset_precios_recientes(sym, precios_data, n_min)
    if len(subset) < 2:
        return 0
    prices = [p for _, p in subset]
    return sum(1 for i in range(1, len(prices))
               if prices[i - 1] > 0 and prices[i] > 0)


def _estimar_vol_h(sym, precios_data, n_min=120):
    """Vol por hora a partir de las últimas n_min de precios spot. None si insuficiente."""
    subset = _subset_precios_recientes(sym, precios_data, n_min)
    if len(subset) < 2:
        return None
    prices = [p for _, p in subset]
    log_r = [math.log(prices[i] / prices[i-1])
             for i in range(1, len(prices))
             if prices[i-1] > 0 and prices[i] > 0]
    if len(log_r) < 2:
        return None
    var = sum(r * r for r in log_r) / len(log_r)
    # Duración media entre puntos (minutos)
    durs = [(subset[i][0] - subset[i-1][0]).total_seconds() / 60
            for i in range(1, len(subset))]
    avg_dur = sum(durs) / len(durs)
    if avg_dur <= 0:
        return None
    return math.sqrt(var / avg_dur * 60)  # vol por hora


def _estimar_vol_h_ewma(sym, precios_data, n_min=120, half_life_min=10):
    """Como _estimar_vol_h pero pondera cada retorno al cuadrado por
    decaimiento exponencial (más peso a lo reciente) en vez de ventana
    plana — propuesta #11 backlog quant-desk 13-jul. Backtest
    (analisis_ewma_vol.py, n=4210/activo sobre 21 días de precios reales,
    lookback 20min/forward 15min igual que GBM_LATE_15M) contra el sigma_h
    REALIZADO en los 15min siguientes: mejora modesta pero consistente en
    las 4 monedas frente al flat actual (MAE -0.3% a -3%, corr +0.006 a
    +0.037; half_life=10min mejor que 5min salvo XRP). El mismo backtest
    REFUTA el efecto apalancamiento tipo Heston en cripto (drift reciente
    vs vol futura: corr +0.003 a +0.112, cerca de cero y de signo
    equivocado si hubiera efecto — no construir nada que lo asuma). Solo
    LOGUEA (sigma_h_ewma10 en _s_gbm_late) — sigma_h sigue siendo
    _estimar_vol_h, esta función NO alimenta la decisión ni el stake de
    GBM_LATE_15M (estrategia en vivo); el pipeline causal decide con datos
    forward reales si alguna vez merece sustituirla."""
    subset = _subset_precios_recientes(sym, precios_data, n_min)
    if len(subset) < 2:
        return None
    log_r = [(subset[i][0], math.log(subset[i][1] / subset[i-1][1]))
             for i in range(1, len(subset))
             if subset[i-1][1] > 0 and subset[i][1] > 0]
    if len(log_r) < 2:
        return None
    ahora = datetime.now(timezone.utc)
    decay = math.log(2) / half_life_min
    pesos = [math.exp(-decay * (ahora - t).total_seconds() / 60) for t, _ in log_r]
    peso_total = sum(pesos)
    if peso_total <= 0:
        return None
    var = sum(w * r * r for w, (_, r) in zip(pesos, log_r)) / peso_total
    durs = [(subset[i][0] - subset[i-1][0]).total_seconds() / 60
            for i in range(1, len(subset))]
    avg_dur = sum(durs) / len(durs)
    if avg_dur <= 0:
        return None
    return math.sqrt(var / avg_dur * 60)


def _precio_en(activo, ref_time, precios_data, tol_min=10):
    """Precio más cercano a ref_time (tolerancia ±tol_min minutos). None si no hay."""
    best_p, best_d = None, None
    for ts, prices in precios_data:
        if activo not in prices:
            continue
        d = abs((ts - ref_time).total_seconds())
        if best_d is None or d < best_d:
            best_d, best_p = d, prices[activo]
    if best_d is not None and best_d <= tol_min * 60:
        return best_p
    return None


def _calcular_retest_pct(activo, window_start, now_utc, ref, spot, precios_data):
    """% de retroceso desde el máximo alejamiento (en la dirección del
    movimiento final) antes del instante actual — ver
    analisis_retest_gbm_late.py (13-Jul, idea_retest_gbm_late_15m_13jul):
    hallazgo con permutación+BH-FDR+split temporal de que retest_pct==0
    (nunca retrocedió, recorrido monótono) acierta MÁS en GBM_LATE_15M#SOL#
    BUY_YES (n=528 gap=-0.182 p=0.0000, estable en ambas mitades del
    periodo) que retest_pct>0. Signo CONTRARIO al break-and-retest de ORB
    que inspiró la idea. Solo LOGUEA — no toca prob_yes/edge/decision;
    cualquier uso como filtro en el par live requiere aprobación explícita
    + /code-review (CLAUDE.md, código que toca dinero real)."""
    if not ref or ref <= 0 or not spot or spot <= 0:
        return None
    camino = [(ts, p[activo]) for ts, p in precios_data
              if activo in p and window_start <= ts <= now_utc]
    if len(camino) < 4:
        return None
    signo_final = 1 if spot > ref else -1
    excursion_max = 0.0
    for _, p in camino:
        dev = (p - ref) / ref * signo_final
        if dev > excursion_max:
            excursion_max = dev
    if excursion_max <= 1e-9:
        return None
    dev_final = (spot - ref) / ref * signo_final
    return round(max(0.0, (excursion_max - dev_final) / excursion_max), 4)


def _calcular_drift_h(sym, precios_data, n_min):
    """
    Drift observado en las últimas n_min, expresado como fracción por hora.
    Usa precios_intraday (datos cada ~60s) para cubrir ventanas largas.
    """
    ahora = datetime.now(timezone.utc)
    corte = ahora - timedelta(minutes=n_min)
    subset = [(ts, p[sym]) for ts, p in precios_data if sym in p and ts >= corte]
    if len(subset) < 5:
        return None
    ref_p, now_p = subset[0][1], subset[-1][1]
    if ref_p <= 0:
        return None
    return (now_p / ref_p - 1) / (n_min / 60)  # fracción por hora


def _drift_e_ibs_ventana(sym, precios_data, n_min):
    """Momentum reciente MUY corto (10-Jul, libro Shannon 'multiple timeframes'
    aplicado a nuestra escala): probado que la alineación con tendencia a 60min
    NO aporta nada (EV+0.32 igual con o sin ella, n=1635) porque a esa distancia
    la señal ya está diluida/es ruido para una apuesta de 15min — pero a ~20min
    (≈1.3x nuestra propia ventana) SÍ hay señal real: alineado 65% hit EV+0.34
    vs no-alineado 59% hit EV+0.27 (n=1133/508). Devuelve (drift_pct_crudo,
    ibs) — ibs es la posición dentro del rango [min,max] de la ventana (0=en
    el mínimo, 1=en el máximo), mismo concepto que ibs_15 de UPDOWN_GBM
    (klines) pero aquí sobre precios_intraday para no depender de klines_raw.
    Confirmado el 10-Jul también con estructura de swing: entrar EN un
    extremo fresco a favor de la apuesta (ibs≈1 para BUY_YES, ibs≈0 para
    BUY_NO) da 70% hit EV+0.42 (n=398); entrar contra el extremo fresco
    (ibs≈0 para BUY_YES) cae a 19% hit EV-0.27 (n=16, fino, vigilar).
    Puro logging — no cambia decisión, alimenta el bucket causal existente."""
    ahora = datetime.now(timezone.utc)
    corte = ahora - timedelta(minutes=n_min)
    subset = [p[sym] for ts, p in precios_data if sym in p and ts >= corte]
    if len(subset) < 5:
        return None, None
    ref_p, now_p = subset[0], subset[-1]
    if ref_p <= 0:
        return None, None
    drift_pct = (now_p / ref_p - 1) * 100
    lo, hi = min(subset), max(subset)
    ibs = (now_p - lo) / (hi - lo) if (hi - lo) > 1e-9 else 0.5
    return round(drift_pct, 4), round(ibs, 4)


def _dist_ancla_estructural_pct(sym, precios_data, horas_lookback=3):
    """VWAP anclada a un punto estructural (10-Jul, propuesta #4 libro Shannon
    "Anchored VWAP"): en vez de anclar a las 00:00 UTC fija (dist_vwap_pct
    existente, solo UPDOWN_GBM) — arbitrario para un activo 24/7 sin apertura
    de sesión real — ancla al extremo (máx o mín) de las últimas
    `horas_lookback`. Aproximación DELIBERADA y documentada, no la Anchored
    VWAP completa de Shannon: (a) es media SIN ponderar por volumen —
    precios_intraday (data/prices/*.csv) no tiene volumen, solo
    data/binance/klines lo tiene y con ~25min de profundidad, insuficiente
    para un ancla de horas; volumen-ponderar exigiría una llamada nueva a la
    API dedicada (mismo patrón que fetch_session_vwap) que hoy NO se añade
    para no revertir el ahorro de latencia del mismo día (ver
    project_hallazgo_latencia_10jul); (b) el "extremo de la ventana" es una
    detección de swing ingenua (no un detector de pivotes real) — en un
    mercado en tendencia fuerte, el extremo tiende a coincidir con el inicio
    de la ventana, casi indistinguible de una media de lookback fijo. SIN
    VALIDAR con datos históricos (no se puede: la feature no existía antes de
    hoy, no hay forma de reconstruir retroactivamente qué habría dicho en
    trades pasados). Puro logging — el pipeline causal decide con n futuro."""
    ahora = datetime.now(timezone.utc)
    corte = ahora - timedelta(hours=horas_lookback)
    serie = [(ts, p[sym]) for ts, p in precios_data if sym in p and ts >= corte]
    if len(serie) < 10:
        return None
    valores = [v for _, v in serie]
    idx_max = valores.index(max(valores))
    idx_min = valores.index(min(valores))
    # ancla = el extremo MÁS RECIENTE de los dos (más probable que sea el
    # swing point relevante "ahora" que el más antiguo de la ventana)
    idx_ancla = idx_max if idx_max > idx_min else idx_min
    desde_ancla = valores[idx_ancla:]
    if len(desde_ancla) < 2:
        return None
    media_ancla = sum(desde_ancla) / len(desde_ancla)
    if media_ancla <= 0:
        return None
    spot = valores[-1]
    return round((spot - media_ancla) / media_ancla * 100, 4)


def _calcular_delta_ratio_macro(sym, klines_raw):
    """
    Delta ratio acumulado sobre todas las klines disponibles con taker_buy_vol.
    Señal macro de presión compradora/vendedora en el exchange.
    """
    klines = klines_raw.get(sym, [])
    if not klines or len(klines[0]) < 7:
        return None
    tb = sum(float(k[6]) for k in klines)
    tv = sum(float(k[5]) for k in klines)
    ts_vol = tv - tb
    denom = tb + ts_vol
    if denom <= 0:
        return None
    return (tb - ts_vol) / denom


# Fracción del drift observado que se incorpora al GBM.
# DRIFT_DAMPING por ventana — backfill 90d × 6 pares (125k predicciones GBM).
# El momentum de Binance aporta más en ventanas cortas (5/15min) que en largas.
# dd óptimo por ventana: 5min=0.30, 15min=0.20, 60min=0.05, 240min=0.10.
DRIFT_DAMPING = {
    5:   0.30,
    15:  0.20,
    60:  0.05,
    240: 0.10,
}
DRIFT_DAMPING_DEFAULT = 0.10  # daily y ventanas no catalogadas

# Filtro régimen — solo activo en ventanas ≥60min y solo para BUY_NO alcista.
# Backfill 90d: 60min drift>+0.7 BUY_NO IC=−0.004; 240min IC=−0.050 → mala señal.
# drift<−0.7 BUY_YES en 60min IC=+0.169 → buena señal, no filtrar.
# En 5/15min ambas señales son buenas → sin filtro.
REGIME_BUY_NO_THRESHOLD = 0.7  # %/h, solo para ventanas ≥60min

# Filtro BUY_YES #15min — solo operar cuando drift_60min ∈ [0, +0.25%)
# Análisis original n=81 (2026-06-26): [0,0.5) IC=+0.208. NO se sostuvo en forward:
# 27-Jun→05-Jul [0,0.25) IC=-0.018 n=195 | [0.25,0.5) IC=-0.071 n=82 (peor tramo).
# 2026-07-05: HI 0.5→0.25 — recorta la zona peor; el resto sigue en tracking
# (H-CUSTOM-BUYYES-15MIN-POSTFILTRO). Ninguna zona drift es positiva forward.
DRIFT_60_BUY_YES_15M_LO = 0.0   # %/h — mínimo (drift plano o ligeramente alcista)
DRIFT_60_BUY_YES_15M_HI = 0.25  # %/h — máximo (2026-07-05, antes 0.5: IC=-0.071 en [0.25,0.5))
# BUY_YES #15min SOLO TARDÍO (2026-07-06): el sesgo retail "Up" infla el YES al
# principio de la ventana y se disuelve cerca del cierre. Medido en results.csv:
# BUY_YES 15min con T_h>=0.2 (entrada temprana) IC=-0.062 n=404 PNL=-46.2€ vs
# T_h<0.2 (tardía, <=12min restantes) IC=+0.123 n=51. El mismo signo que voltea
# GBM_LATE_15M BUY_YES (+0.119 n=672). Bloquear temprano NO pierde la señal: el
# fast loop re-evalúa cada ~20s y la predicción se dispara sola al entrar el
# mercado en zona tardía (si la señal sigue viva) → entrada tardía deliberada.
# BUY_NO no se toca (temprana break-even con bolsillos positivos: zona moneda
# IC=+0.162). Forward gate hacia live: H-CUSTOM-BUYYES15-SOLO-TARDIO.
BUY_YES_15M_TH_MAX = 0.2        # T_h máximo para permitir BUY_YES #15min

# Filtro ETH#15min BUY_NO — skip si el mercado ya da >55% al YES (NO longshot).
# Análisis 2026-07-02 últ.60 shadow: py_mkt~0.5 → wr 0.67 PNL=+29.3€ (n=49);
# py_mkt 0.6-0.8 → wr 0.33→0 PNL=-5.75€ (n=9). Comprar NO contra favorito no paga.
PY_MKT_MAX_BUY_NO_ETH15 = 0.55

KELLY_COMPUESTO_BOOST = 1.5
KELLY_COMPUESTO_MAX   = 2.00


def _aplicar_kelly_compuesto(rows: list) -> list:
    """
    rows: listas [ts, nombre, mid, q, end, horas, py, prob_y, eb, en, ed,
                  dec(11), razon(12), subtype(13), apuesta(14), features(15)]
    Si UPDOWN_GBM y ORDER_FLOW_5M coinciden → boost apuesta 1.5×.
    Si divergen → ambas SKIP (señal ambigua).
    """
    gbm = next((r for r in rows if r[1] == "UPDOWN_GBM"    and r[11] != "SKIP"), None)
    of  = next((r for r in rows if r[1] == "ORDER_FLOW_5M"  and r[11] != "SKIP"), None)
    if not gbm or not of:
        return rows
    if gbm[11] == of[11]:
        for r in rows:
            if r[1] in ("UPDOWN_GBM", "ORDER_FLOW_5M") and r[11] != "SKIP":
                r[14] = f"{min(float(r[14]) * KELLY_COMPUESTO_BOOST, KELLY_COMPUESTO_MAX):.2f}"
                r[12] += " [+compuesto]"
    else:
        for r in rows:
            if r[1] in ("UPDOWN_GBM", "ORDER_FLOW_5M"):
                r[11] = "SKIP"
    return rows


# ── Conexiones detectadas 13-Jul (sesión de auditoría estrategia↔problema),
# implementadas en shadow como features observacionales — nunca tocan
# dec/apuesta. El pipeline causal (postmortem→FEATURE_RULES) las descubrirá
# solo si hace falta un filtro/boost, con n suficiente, igual que el resto
# de features del sistema. Ver idea_awesome_quant_hallazgos_13jul y
# project_auditoria_estrategia_problema_13jul (memoria nativa Claude).
GBM_LATE_FAMILIA = {"GBM_LATE_15M", "GBM_LATE_15M_TARDIO", "GBM_LATE_15M_ESPACIO_ATR"}

# Wang Transform (Yang, Y. 2026, "Pricing Prediction Markets" — calibrado
# sobre 291,309 contratos reales, 6 plataformas): p_mercado =
# Phi(Phi^-1(p_real) + lambda), lambda_hat=0.183 global (p<1e-15). Formaliza
# el mismo sesgo favorito-longshot que FAVORITO_CONFIRMADO ya explota
# ad-hoc. Se usa el lambda GLOBAL (no el jerárquico por volumen/plazo — su
# dependencia de "días a vencimiento" no tiene análogo directo en mercados
# de minutos, ver caveat en la nota de origen) hasta que haya n suficiente
# para recalibrar sobre nuestra propia escala.
WANG_LAMBDA = 0.183


def _inyectar_features_cruzadas(rows: list) -> list:
    """
    rows: mismo formato que _aplicar_kelly_compuesto (índices: 1=strategy,
    6=precio_yes, 7=prob_yes_modelo, 11=decision, 15=features_json).

    Dos conexiones detectadas al auditar el sistema (13-Jul), medidas aquí
    por primera vez para que dejen de vivir solo en el análisis retrospectivo:

    1. Wang Transform sobre FAVORITO_CONFIRMADO: p_implicito = probabilidad
       "justa" que implica el precio de mercado tras deshacer el sesgo
       lambda. wang_gap = cuánto se aleja nuestro prob_yes_modelo de esa
       corrección — si FAVORITO_CONFIRMADO ya captura el mismo sesgo,
       wang_gap debería ser pequeño; si no, es una corrección potencialmente
       complementaria (a estudiar, no aplicada).
    2. Confirmación cruzada FAVORITO_CONFIRMADO -> familia GBM_LATE_15M:
       mecanismo distinto (convicción de favorito vs continuación GBM) sobre
       el MISMO market_id — favorito_confirma_coincide=1 si están de
       acuerdo en dirección. Candidata a alimentar `boost_ic_coincidencia_tuplas`
       (P8) el día que FAVORITO_CONFIRMADO entre en pares_permitidos_live;
       hoy solo se mide.
    """
    favorito_row = next((r for r in rows if r[1] == "FAVORITO_CONFIRMADO" and r[11] != "SKIP"), None)
    for r in rows:
        try:
            feats = json.loads(r[15]) if r[15] else {}
        except Exception:
            feats = {}
        cambiado = False

        if r[1] == "FAVORITO_CONFIRMADO" and r[11] != "SKIP":
            try:
                wang_p_implicito = _norm_cdf(_norm_ppf(float(r[6])) - WANG_LAMBDA)
                feats["wang_p_implicito"] = round(wang_p_implicito, 4)
                feats["wang_gap"] = round(float(r[7]) - wang_p_implicito, 4)
                cambiado = True
            except (TypeError, ValueError, ZeroDivisionError):
                pass

        if r[1] in GBM_LATE_FAMILIA and r[11] != "SKIP":
            if favorito_row is not None:
                feats["favorito_confirma_decision"] = favorito_row[11]
                feats["favorito_confirma_coincide"] = 1 if favorito_row[11] == r[11] else 0
            else:
                feats["favorito_confirma_decision"] = None
                feats["favorito_confirma_coincide"] = None
            cambiado = True

        if cambiado:
            r[15] = json.dumps(feats, separators=(",", ":"))
    return rows


def _gbm_p_up(spot, ref, sigma_h, T_h, mu_h=0.0):
    """
    P(S_T > ref | S_t=spot) via Black-Scholes digital.
    mu_h: drift estimado por hora (fracción). Default 0 = riesgo neutro.
    Con drift: d2 = (log(spot/ref) + mu_h * T_h) / (sigma_h * sqrt(T_h))
    """
    if sigma_h <= 0 or T_h <= 0 or ref <= 0 or spot <= 0:
        return None
    sigma_T = sigma_h * math.sqrt(T_h)
    if sigma_T < 1e-9:
        return 1.0 if spot > ref else (0.0 if spot < ref else 0.5)
    d2 = (math.log(spot / ref) + mu_h * T_h) / sigma_T
    return _norm_cdf(d2)


def _parse_updown_tipo(question):
    """
    Clasifica el mercado Up/Down y devuelve (tipo, ventana_min).
    tipo: 'daily' | 'slot' | 'hourly' | None
    ventana_min: minutos de la ventana (None para daily)
    """
    q = question.lower()
    if "up or down" not in q:
        return None, None

    # Daily: "Bitcoin Up or Down on June 24?"
    if re.search(r'up or down on \w+ \d+\??$', q.strip()):
        return 'daily', None

    # Slot con rango explícito: "1:15am-1:20am et" (5min, 15min, etc.)
    m = re.search(r'(\d+):(\d+)(am|pm)-(\d+):(\d+)(am|pm)', q)
    if m:
        def to_min(h, mn, mer):
            h = int(h) % 12 + (12 if mer == 'pm' else 0)
            return h * 60 + int(mn)
        t1 = to_min(m.group(1), m.group(2), m.group(3))
        t2 = to_min(m.group(4), m.group(5), m.group(6))
        diff = (t2 - t1) % (24 * 60)
        return ('slot', diff) if diff > 0 else (None, None)

    # Hourly: "June 24, 9am et" (sin rango de minutos)
    if re.search(r',\s*\d+\s*(am|pm)\s+et', q):
        return 'hourly', 60

    return None, None


def s_updown_gbm(market, ctx):
    """
    Black-Scholes digital para mercados Up/Down.
    Calcula P(S_T > S_ref | spot, sigma, T) y compara con price_yes del mercado.
    Cubre: daily ($42k liq), hourly (1h), slots de 5/15min.
    """
    question = market.get("question", "")
    if "up or down" not in question.lower():
        return None

    activo = identificar_activo(question)
    if not activo or activo not in BINANCE_SYMBOLS:
        return None

    try:
        liq = float(market.get("liquidity") or 0)
    except (ValueError, TypeError):
        liq = 0.0
    if liq < 2000:
        return None

    try:
        spread = float(market.get("spread") or 0)
    except (ValueError, TypeError):
        spread = 0.0
    if spread > 0.05:
        return None

    tipo, ventana_min = _parse_updown_tipo(question)
    if tipo is None:
        return None

    T_h = market.get("_horas")
    if T_h is None or T_h <= 2 / 60:  # mínimo 2 minutos
        return None

    precios_data = ctx.get("precios_intraday", [])
    if not precios_data:
        return None

    # L2: bloquear si data_quality marca este símbolo como CRITICAL
    if simbolo_bloqueado(activo):
        return None

    # Meta auto-params: blacklist de horas aplicada automáticamente por hypothesis_tracker
    meta = ctx.get("meta_params", {})
    gbm_auto_blacklist = set(meta.get("gbm_blacklist_hours_auto", []))
    if gbm_auto_blacklist:
        hora_actual = datetime.now(timezone.utc).hour
        if hora_actual in gbm_auto_blacklist:
            return None

    # Spot actual: klines > precios_intraday
    spot = ctx.get("spot_prices", {}).get(activo)
    if not spot:
        recientes = [(ts, p[activo]) for ts, p in precios_data if activo in p]
        if not recientes:
            return None
        spot = recientes[-1][1]

    # end_date
    try:
        end_str = market.get("end_date", "").replace("Z", "+00:00")
        end_dt = datetime.fromisoformat(end_str)
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None

    # Tiempo de referencia y ventana de vol según tipo
    if tipo == 'daily':
        ref_time = end_dt.replace(hour=0, minute=0, second=0, microsecond=0)
        vol_win  = min(240, max(60, int(T_h * 20)))
        tol_min  = 15
    elif tipo == 'hourly':
        ref_time = end_dt - timedelta(hours=1)
        vol_win  = 120
        tol_min  = 8
    else:  # slot
        ref_time = end_dt - timedelta(minutes=ventana_min)
        vol_win  = min(60, max(15, ventana_min * 4))
        tol_min  = max(2, ventana_min // 2)

    ref = _precio_en(activo, ref_time, precios_data, tol_min)
    if ref is None:
        return None

    sigma_h = _estimar_vol_h(activo, precios_data, n_min=vol_win)
    if not sigma_h or sigma_h <= 0:
        return None

    # sigma_ewma_delta_pct (12-Jul, propuesta #6 lista puntos ciegos): mismo
    # feature ya validado en _s_gbm_late (efecto real pero de SIGNO distinto
    # por activo: ETH/BTC mejoran cuando la vol acelera, XRP empeora) —
    # extendido aquí porque UPDOWN_GBM tiene mucho más volumen (ya desagregada
    # por activo en FEATURE_RULES) y validará el feature 3-4x más rápido.
    # Solo logueo, no cambia p_up/decisión.
    _sigma_h_ewma10 = _estimar_vol_h_ewma(activo, precios_data, n_min=vol_win, half_life_min=10)
    _sigma_ewma_delta_pct = (
        round((_sigma_h_ewma10 - sigma_h) / sigma_h * 100, 3)
        if _sigma_h_ewma10 is not None and sigma_h > 0 else None
    )

    pct = (spot / ref - 1) * 100

    # Drift macro: tendencia de las últimas 1h y 15min desde precios_intraday.
    # Se incorpora al GBM (amortiguado) para que el modelo sea consciente del régimen.
    drift_15 = _calcular_drift_h(activo, precios_data, 15)
    drift_60 = _calcular_drift_h(activo, precios_data, 60)
    delta_macro = _calcular_delta_ratio_macro(activo, ctx.get("klines_raw", {}))

    # L3: validar features via data_quality (fuente única de verdad para umbrales)
    feat_ok, feat_motivo = validar_features_gbm(sigma_h, drift_60, drift_15)
    if not feat_ok:
        if "drift" not in feat_motivo:
            return None   # sigma_h corrupta → descartar predicción completamente
        # drift imposible → ignorar el drift pero continuar con predicción
        if drift_60 is not None and abs(drift_60) > DRIFT_MAX:
            drift_60 = None
        if drift_15 is not None and abs(drift_15) > DRIFT_MAX:
            drift_15 = None

    # mu_h: drift por hora amortiguado según ventana temporal.
    # dd óptimo varía: más en corto (momentum 5min) que en largo (ruido 60min+).
    _dd = DRIFT_DAMPING.get(ventana_min, DRIFT_DAMPING_DEFAULT)
    mu_h = (drift_60 or 0.0) * _dd

    p_up = _gbm_p_up(spot, ref, sigma_h, T_h, mu_h=mu_h)
    if p_up is None:
        return None

    # Filtro mean-reversion 5min: sin datos suficientes para decidir, conservar.
    if tipo == 'slot' and ventana_min == 5 and abs(pct) > 0.05:
        return None

    # Filtro régimen — solo en ventanas ≥60min y solo para BUY_NO alcista fuerte.
    # Backfill 90d: 60min drift>+0.7 BUY_NO IC=−0.004; 240min IC=−0.050.
    # No filtrar BUY_YES (drift<−0.7 BUY_YES 60min IC=+0.169 — mean-reversion buena).
    if tipo in ('slot', 'hourly') and ventana_min and ventana_min >= 60 and drift_60 is not None:
        drift_pct = drift_60 * 100
        py_mkt = market.get("_precio_yes", 0.5)
        if drift_pct > REGIME_BUY_NO_THRESHOLD and p_up < py_mkt:
            return None  # 60min+ alcista + BUY_NO → señal mala históricamente

    # Filtro BUY_YES #15min: solo cuando drift_60min ∈ [0, +0.5%)
    # Lógica: confirma dirección (alcista moderado) sin estar ya priceado (alcista fuerte).
    # IC fuera del rango ≈ 0 (n=59, PNL=−7.94€ total) vs IC=+0.208 dentro (n=22).
    # Si drift_60 es None (sin histórico 60min), bloquear BUY_YES — sin datos no apostar.
    if tipo == 'slot' and ventana_min == 15 and p_up > market.get("_precio_yes", 0.5):
        # Solo tardío (2026-07-06): temprana IC=-0.062 n=404 vs tardía +0.123 n=51.
        # El skip deja el mercado sin predecir → el loop lo re-evalúa y la señal
        # entra sola al cruzar T_h<0.2 (ver nota en BUY_YES_15M_TH_MAX).
        if T_h >= BUY_YES_15M_TH_MAX:
            return None  # BUY_YES #15min temprano → esperar zona tardía
        if drift_60 is None:
            return None  # BUY_YES #15min sin histórico 60min → no apostar
        drift_60_pct = drift_60 * 100
        if not (DRIFT_60_BUY_YES_15M_LO <= drift_60_pct < DRIFT_60_BUY_YES_15M_HI):
            return None  # BUY_YES #15min fuera del sweet spot drift_60min

    # Filtro ETH#15min BUY_NO — no comprar NO cuando el mercado da >55% al YES.
    if (tipo == 'slot' and ventana_min == 15 and activo == 'ETH'
            and p_up < market.get("_precio_yes", 0.5)
            and market.get("_precio_yes", 0.5) > PY_MKT_MAX_BUY_NO_ETH15):
        return None

    # Filtro BTC#15min — solo operar cuando drift_15min ≥ +0.3%/h (momentum claro)
    # Análisis n=36 BTC#15min con feature: drift≥0.3 → IC=+0.152 n=13 (77%);
    # drift<0.3 → IC=−0.100 n=23 (39%). La señal GBM necesita dirección clara.
    # Zona muerta [-0.3,+0.3]: mercado consolidando → GBM incapaz de predecir.
    # Zona -1…-0.3: señal negativa activa (mercado bajando suavemente) → también mala.
    # Implementado 2026-06-27 con n=36, revisable con n≥60.
    if tipo == 'slot' and ventana_min == 15 and activo == 'BTC' and drift_15 is not None:
        if drift_15 * 100 < 0.3:
            return None  # BTC#15min sin momentum positivo claro → no apostar

    # Filtro GBM#15min — zona muerta drift_15min∈[-0.3,+0.3]%/h (todos los pares)
    # H-CUSTOM-DRIFT15-ZONA-MUERTA confirmada 2026-07-01: IC=-0.037 n=52 en la zona
    # muerta (mercado sin dirección clara, GBM no puede predecir), vs IC=+0.100 n=28
    # con drift>0.3 (momentum) y edge de reversión aparte con drift<-1 (boost Kelly).
    # Para BTC ya queda cubierto por el filtro de momentum de arriba (más estricto).
    if tipo == 'slot' and ventana_min == 15 and drift_15 is not None:
        if abs(drift_15 * 100) < 0.3:
            return None  # GBM#15min en zona muerta → sin dirección clara, no apostar

    if tipo == 'daily':
        slot_type = 'daily'
    elif tipo == 'hourly':
        slot_type = '60min'
    else:
        slot_type = f'{ventana_min}min'
    subtype = f"{activo}#{slot_type}"
    razon = (
        f"updown_gbm {activo} {slot_type} "
        f"ref={ref:.4g} spot={spot:.4g} ({pct:+.2f}%) "
        f"sigma_h={sigma_h:.4f} T={T_h:.2f}h p_up={p_up:.3f} mu_h={mu_h:+.4f}"
    )

    # H-CUSTOM-CROSS-WINDOW-SPREAD: diferencia de precio_yes contra la ventana
    # relacionada del mismo activo (15min vs 60min). Solo observación — no
    # afecta a p_up ni a la decisión, solo se registra como feature.
    precios_ventanas = ctx.get("precios_ventanas_hoy", {})
    _py_propio = market.get("_precio_yes", 0.5)
    cross_window_spread = None
    if ventana_min == 15:
        _rel = precios_ventanas.get((activo, 60))
        if _rel is not None:
            cross_window_spread = round(_py_propio - _rel, 4)
    elif tipo == 'hourly':
        _rel = precios_ventanas.get((activo, 15))
        if _rel is not None:
            cross_window_spread = round(_py_propio - _rel, 4)

    features = {
        "pct_spot_vs_ref": round(pct, 4),
        "sigma_h":         round(sigma_h, 6),
        "T_h":             round(T_h, 4),
        "hora_utc":        datetime.now(timezone.utc).hour,
    }
    if _sigma_ewma_delta_pct is not None:
        features["sigma_ewma_delta_pct"] = _sigma_ewma_delta_pct
    if drift_15 is not None:
        features["drift_15min"] = round(drift_15 * 100, 4)   # %/hora
    if drift_60 is not None:
        features["drift_60min"] = round(drift_60 * 100, 4)   # %/hora
    if delta_macro is not None:
        features["delta_ratio_macro"] = round(delta_macro, 4)
    if cross_window_spread is not None:
        features["cross_window_spread"] = cross_window_spread
    # IBS-15: posición del precio dentro del rango high/low de las últimas 15 velas 1min.
    # IBS>0.7 = precio cerca del máximo (sobrecompra → señal BUY_NO).
    # IBS<0.3 = precio cerca del mínimo (sobreventa → señal BUY_YES).
    klines_sym = ctx.get("klines_raw", {}).get(activo, [])
    if len(klines_sym) >= 15:
        k15 = klines_sym[-15:]
        h15 = max(float(k[2]) for k in k15)
        l15 = min(float(k[3]) for k in k15)
        c15 = float(k15[-1][4])
        if (h15 - l15) > 1e-8:
            features["ibs_15"] = round((c15 - l15) / (h15 - l15), 4)
    # dist_vwap_pct (aprobada 05-Jul, impl 07-Jul): distancia % del spot a la VWAP
    # de sesión UTC (ancla 00:00), ponderada por volumen. Única feature GBM que usa
    # volumen. Shadow-only: se loguea, el postmortem decide si filtra/boostea.
    # Fail-closed: sin VWAP (fetch falló o Kraken fallback) → no se añade.
    _vwap = ctx.get("vwap_sesion", {}).get(activo)
    if _vwap and spot and _vwap > 0:
        features["dist_vwap_pct"] = round((spot - _vwap) / _vwap * 100, 4)
    # poly_drift_5obs: drift del precio YES DENTRO de Polymarket en últimas 5 obs (~5min).
    # Negativo → el mercado interno está vendiendo YES (demanda NO). Positivo → demanda YES.
    # Si poly_drift y nuestra predicción coinciden → señal reforzada (cross-confirmation).
    mid_market = market.get("id")
    hist_mkt = ctx.get("historial_mercados", {}).get(mid_market, [])
    if len(hist_mkt) >= 5:
        prices_hist = [p for _, p in hist_mkt[-5:]]
        if prices_hist[0] > 1e-6:
            poly_drift = (prices_hist[-1] - prices_hist[0]) / prices_hist[0] * 100
            features["poly_drift_5obs"] = round(poly_drift, 4)
    # funding_rate_8h: última tasa de financiación del perp Binance (decimal/8h).
    fr = ctx.get("funding_rates", {}).get(activo)
    if fr is not None:
        features["funding_rate_8h"] = round(fr * 100, 5)
    # logit_edge (Shaw & Dalen 2025 — BS-P): edge en espacio logit.
    # logit(p_modelo) - logit(p_mercado) es más estable que la diferencia en probabilidad
    # cerca de los extremos (p→0 o p→1) y captura el edge multiplicativo real.
    py_mkt_le    = market.get("_precio_yes", 0.5)
    p_up_clipped = max(0.02, min(0.98, p_up))
    py_clipped   = max(0.02, min(0.98, py_mkt_le))
    logit_edge   = math.log(p_up_clipped / (1 - p_up_clipped)) - math.log(py_clipped / (1 - py_clipped))
    features["logit_edge"] = round(logit_edge, 4)
    # sigma_b (belief volatility): volatilidad del logit(price_yes) en Polymarket.
    # Mide cuánto oscila la creencia del mercado — alta sigma_b = señal poco fiable.
    # Shaw & Dalen 2025: σ_b es el factor de riesgo análogo a implied vol en opciones.
    if len(hist_mkt) >= 4:
        logit_prices = []
        for _, p_hist in hist_mkt[-10:]:
            if 0.01 < p_hist < 0.99:
                logit_prices.append(math.log(p_hist / (1 - p_hist)))
        if len(logit_prices) >= 3:
            diffs = [abs(logit_prices[i] - logit_prices[i-1]) for i in range(1, len(logit_prices))]
            sigma_b = (sum(d**2 for d in diffs) / len(diffs)) ** 0.5
            features["sigma_b"] = round(sigma_b, 4)
    features.update(_libro_calidad(market))
    return {
        "prob_yes": max(0.05, min(0.95, p_up)),
        "razon":   razon,
        "subtype": subtype,
        "features": features,
    }


# ─────────────────────────────────────────────────────────────────────────────
# PRICE_TARGET_GBM — mercados de precio objetivo via Black-Scholes digital/barrera
# ─────────────────────────────────────────────────────────────────────────────

def _parse_price_target(question):
    """
    Extrae (tipo, direction, K) de preguntas de precio objetivo.
      tipo:      'atexpiry' | 'reach'
      direction: 'above' | 'below'  (solo para atexpiry)
      K:         precio objetivo (float)

    Soporta: "$76,000", "$150k", "$3,000", "$1.5m"
    """
    q = question.lower().replace(",", "")

    def parse_k(s):
        s = s.strip()
        mul = 1
        if s.endswith("b"): s = s[:-1]; mul = 1_000_000_000
        elif s.endswith("m"): s = s[:-1]; mul = 1_000_000
        elif s.endswith("k"): s = s[:-1]; mul = 1_000
        try:
            return float(s) * mul
        except ValueError:
            return None

    m = re.search(r'\$([0-9]+(?:\.[0-9]+)?[bBmMkK]?)', q)
    if not m:
        return None, None, None
    K = parse_k(m.group(1))
    if not K or K <= 0:
        return None, None, None

    if re.search(r'\b(hit|reach|exceed|get to|touch)\b', q):
        return 'reach', None, K
    elif re.search(r'\babove\b|\bover\b', q):
        return 'atexpiry', 'above', K
    elif re.search(r'\bbelow\b|\bunder\b', q):
        return 'atexpiry', 'below', K

    return None, None, None


def s_price_target_gbm(market, ctx):
    """
    GBM digital/barrera para mercados de precio objetivo sobre activos cripto.

    atexpiry above K: P(S_T > K)   = N( log(S/K) / σ√T )
    atexpiry below K: P(S_T < K)   = N(-log(S/K) / σ√T )
    reach    K:       P(toca K)     = 2·N(-|log(S/K)| / σ√T )  [reflexión BM]

    Solo activos con precio spot disponible (BTC/ETH/SOL/XRP/DOGE/BNB).
    Ventana de tiempo: 1h – 30 días (más allá el modelo GBM pierde fiabilidad).
    """
    question = market.get("question", "")

    activo = identificar_activo(question)
    if not activo or activo not in BINANCE_SYMBOLS:
        return None
    if simbolo_bloqueado(activo):
        return None

    try:
        liq = float(market.get("liquidity") or 0)
    except (ValueError, TypeError):
        liq = 0.0
    if liq < 2000:
        return None

    try:
        spread = float(market.get("spread") or 0)
    except (ValueError, TypeError):
        spread = 0.0
    if spread > 0.08:
        return None

    tipo, direction, K = _parse_price_target(question)
    if tipo is None:
        return None

    T_h = market.get("_horas")
    if T_h is None or not (1 <= T_h <= 720):   # 1h … 30 días
        return None

    precios_data = ctx.get("precios_intraday", [])
    spot = ctx.get("spot_prices", {}).get(activo)
    if not spot:
        recientes = [(ts, p[activo]) for ts, p in precios_data if activo in p]
        if not recientes:
            return None
        spot = recientes[-1][1]

    # K fuera de rango imposible (evita FDV, market cap, etc.)
    if not (spot / 50 < K < spot * 50):
        return None

    # Vol: ventana proporcional a T (2h para slots intraday, hasta 12h para multi-día)
    # El CSV de precios tiene ~12h de historia a resolución 60s
    vol_win = min(720, max(30, int(T_h * 5)))
    sigma_h = _estimar_vol_h(activo, precios_data, n_min=vol_win)
    if not sigma_h or sigma_h <= 0 or sigma_h > SIGMA_H_MAX:
        return None

    sigma_T = sigma_h * math.sqrt(T_h)
    if sigma_T < 1e-9:
        return None

    log_ratio = math.log(spot / K)   # > 0 si spot > K, < 0 si spot < K

    if tipo == 'atexpiry':
        p_yes = _norm_cdf(log_ratio / sigma_T if direction == 'above'
                          else -log_ratio / sigma_T)
        subtype = f"{activo}#atexpiry"
    else:  # reach / barrier
        p_yes = min(0.99, 2 * _norm_cdf(-abs(log_ratio) / sigma_T))
        subtype = f"{activo}#reach"

    pct_vs_K = (spot / K - 1) * 100
    razon = (
        f"price_target_gbm {activo} {tipo} "
        f"K={K:.5g} spot={spot:.5g} ({pct_vs_K:+.1f}%vsK) "
        f"sigma_h={sigma_h:.4f} T={T_h:.1f}h p_yes={p_yes:.3f}"
    )
    return {
        "prob_yes": max(0.05, min(0.95, p_yes)),
        "razon": razon,
        "subtype": subtype,
        "features": {"pct_vs_K": round(pct_vs_K, 4), "sigma_h": round(sigma_h, 6),
                     "T_h": round(T_h, 4), "log_ratio": round(log_ratio, 6)},
    }


# ─────────────────────────────────────────────────────────────────────────────
# ORDER_FLOW_5M — Cumulative delta en exchanges reales para slots Up/Down 5min
# ─────────────────────────────────────────────────────────────────────────────

# Horas UTC blacklisteadas para ORDER_FLOW_5M.
# RECALIBRADO 2026-07-07 (aprobado Javi, shadow-only — OF fuera de whitelist live).
# El blacklist estaba PARCIALMENTE INVERTIDO: se calibró sobre IC mixto de direcciones,
# pero OF dejó de generar BUY_YES el 2026-06-26 → solo BUY_NO desde entonces. Split por
# dirección (BUY_NO = lo único que OF opera hoy) sobre BTC+SOL, n=387 (scan_blacklist_hours.py):
#   h2  n=10 hit30% edge-0.076  → MALA, mantener
#   h7  n=11 hit45% edge-0.007  → neutra, mantener por cautela
#   h9  n=7  hit86% edge+0.147  → prometedora, n<15 → mantener hasta n≥15
#   h10 n=16 hit69% edge+0.081  → BUENA, DESBLOQUEADA (el -0.028 previo era el BUY_YES h10 28% arrastrando)
#   h11 n=27 hit67% edge+0.060  → BUENA, DESBLOQUEADA (n≥15; revalidar forward, umbral previo pedía n≥40)
#   h22 n=7  hit71% edge+0.083  → prometedora, n<15 → mantener hasta n≥15
# Antes: {2, 7, 9, 10, 11, 22}. Después: {2, 7, 9, 22}. (18h/20h ya se quitaron antes.)
ORDER_FLOW_BLACKLIST_HOURS = {2, 7, 9, 22}

# Pares con IC negativo en sweet spot [0.38-0.46] (conf=1.00, n≥80) — HISTÓRICO,
# ver reapertura abajo: ETH n=112 IC=-0.026 | XRP n=119 IC=-0.004 | DOGE n=83 IC=-0.006
# | BNB n=63 IC=+0.038 (nota original: "backfill 90d negativo, mantener hasta n≥150").
#
# REABIERTOS 11-Jul (aprobado Javi, shadow puro — OF_5M no está en pares_permitidos_live,
# cero riesgo real): el 93% del histórico de estos 4 pares (n=1465/1574 del total
# ORDER_FLOW_5M) viene de una ráfaga de 48h (24-25jun) — la MISMA ventana que calibró
# DELTA_MIN/MAX y ORDER_FLOW_BLACKLIST_HOURS. Verificado con results.csv: 0 predicciones
# de ETH/XRP/DOGE/BNB desde el 26-jun — nunca se re-testaron bajo los filtros actuales
# (más estrictos que cuando se bloquearon). BNB ya superaba su propio umbral de reapertura
# (n≥150, real n=191) sin que nadie lo revisara — mismo patrón de estado absorbente que
# UPDOWN_OU_5M a nivel de estrategia. Acumulan desde cero bajo delta band + horas + el
# nuevo total_vol_5m (FEATURE_RULES, shadow_postmortem.py) — decisión de reactivar cada
# uno como par vivo con n≥40 propio, igual que cualquier otra hipótesis.
#
# BTC: n=291, IC=0.000 (p_shuffle=0.51, no bate control aleatorio zero-intelligence,
# analisis_zero_intelligence_of.py 11-Jul, DATO FRESCO no de la ráfaga) — bloqueado
# 11-Jul (aprobado Javi), se queda fuera. SOL sigue siendo el único confirmado
# (IC+0.060, p_shuffle=0.038, sí bate el control).
ORDER_FLOW_PAIR_BLACKLIST = {'BTC'}


def s_order_flow_5m(market, ctx):
    """
    Explota el lag entre el flujo de órdenes en exchanges (Binance) y el
    reajuste del mercado de predicción de Polymarket.

    Si hay presión compradora neta fuerte en los últimos 5 minutos de klines
    Y el precio YES en Polymarket sigue en torno a 0.50 (no ha reaccionado),
    existe una ventana de arbitraje: el exchange ya 'sabe' la dirección,
    Polymarket todavía no.

    Delta real (Binance): taker_buy_vol - taker_sell_vol por minuto.
    Delta estimado (Kraken fallback): close-location en el rango H-L.
    """
    question = market.get("question", "")

    # Filtro horario: horas con edge sistemáticamente negativo
    hora_utc = datetime.now(timezone.utc).hour
    if hora_utc in ORDER_FLOW_BLACKLIST_HOURS:
        return None

    # Solo slots 5min Up/Down
    tipo, ventana_min = _parse_updown_tipo(question)
    if tipo != 'slot' or ventana_min != 5:
        return None

    activo = identificar_activo(question)
    if not activo or activo not in BINANCE_SYMBOLS:
        return None
    if activo in ORDER_FLOW_PAIR_BLACKLIST:
        return None
    if simbolo_bloqueado(activo):
        return None

    klines = ctx.get("klines_raw", {}).get(activo, [])
    if len(klines) < 5:
        return None

    last_5 = klines[-5:]
    cum_delta = 0.0
    total_vol = 0.0
    has_real_flow = all(len(k) >= 7 for k in last_5)

    for k in last_5:
        try:
            vol = float(k[5])
        except (ValueError, TypeError, IndexError):
            return None
        total_vol += vol

        if len(k) >= 7:
            # Binance: taker_buy_base_asset_volume en columna 6 (guardada como col 7 original)
            try:
                taker_buy = float(k[6])
            except (ValueError, TypeError):
                taker_buy = vol / 2
            cum_delta += 2 * taker_buy - vol
        else:
            # Kraken fallback: close location como proxy de presión compradora
            try:
                h, l, c = float(k[2]), float(k[3]), float(k[4])
                bull_frac = (c - l) / (h - l) if h > l else 0.5
            except (ValueError, TypeError, ZeroDivisionError):
                bull_frac = 0.5
            cum_delta += (2 * bull_frac - 1) * vol

    if total_vol <= 0:
        return None

    # Delta normalizado: fracción del volumen total que fue presión neta
    delta_ratio = cum_delta / total_vol  # rango [-1, +1]

    # Umbral mínimo y máximo de desequilibrio.
    # Datos (n=518): zona [0.38-0.46] IC=+0.03→+0.125 ✅
    #               zona [0.46-0.65] IC=-0.079 ❌ (señal "fuerte" ya priceada → reversión)
    #               zona [0.65+]     IC=+0.032 ✅ (momentum extremo, pocas ops)
    DELTA_MIN = 0.38
    DELTA_MAX = 0.46  # añadido 2026-06-25: elimina zona muerta que destruía -6.75€
    if abs(delta_ratio) < DELTA_MIN or abs(delta_ratio) > DELTA_MAX:
        return None

    # Solo operar en dirección BUY_NO (delta negativo — presión vendedora).
    # Análisis n=271 BTC+SOL: BUY_NO IC=+0.092 PNL=+8.64€ vs BUY_YES IC=-0.038 PNL=-4.10€.
    # Razón: presión compradora ya visible → priceada; presión vendedora silenciosa → lag mayor.
    if delta_ratio > 0:
        return None

    # Timing: esperar a que el slot lleve ≥1.5min abierto.
    # Datos: slot 0-1min → IC=-0.035 (-15.28€). Slot 2-3min → IC=+0.045.
    # Los klines del primer minuto son del slot ANTERIOR → señal de ruido.
    h_restantes = market.get("_horas", 0) * 60  # minutos restantes
    minutos_vividos = 5 - h_restantes  # cuánto lleva abierto el slot de 5min
    if minutos_vividos < 1.5:
        return None

    # El mercado de Polymarket no debe haber reaccionado ya
    # Si YES está en 0.40-0.60 → lag explotable; si ya se movió → tarde
    py = market.get("_precio_yes", 0.5)
    LAG_MAX = 0.12
    if abs(py - 0.5) > LAG_MAX:
        return None

    # Conversión delta → probabilidad
    # delta=0.20 → prob=0.60 ; delta=0.50 → prob=0.75 ; delta=1.0 → prob=1.0 (capped)
    p_yes = 0.5 + delta_ratio * 0.5
    p_yes = max(0.10, min(0.90, p_yes))

    flow_src = "binance_real" if has_real_flow else "kraken_est"
    razon = (
        f"order_flow_5m {activo} "
        f"delta={delta_ratio:+.3f} vol5m={total_vol:.3f} "
        f"py_mkt={py:.3f} [{flow_src}]"
    )
    return {
        "prob_yes": p_yes,
        "razon":   razon,
        "subtype": f"{activo}#5min",
        "features": {
            "delta_ratio":  round(delta_ratio, 4),
            "total_vol_5m": round(total_vol, 4),
            "has_real_flow": int(has_real_flow),
            "hora_utc": hora_utc,
            "es_ntm_5min": _es_ntm_5min(market),
            **_libro_calidad(market),
        },
    }


def s_resolution_sniper(market, ctx):
    """
    Sniper de vencimiento: mercados NO Up/Down en su última 1.5h.
    Usa GBM real (no heurísticas) para calcular prob cuando la incertidumbre ya es mínima.
    Solo dispara si edge > 0.08 y |prob - 0.5| > 0.30 (alta certeza).
    """
    import re as _re
    h   = market.get("_horas", 999)
    if not (0.05 < h < 1.5):
        return None
    q   = market.get("question", "")
    ql  = q.lower()
    if "up or down" in ql:          # ya cubierto por UPDOWN_GBM
        return None
    activo = identificar_activo(q)
    if not activo:
        return None
    spot = _cargar_spot().get(activo)
    if not spot or spot <= 0:
        return None

    py_mkt = market.get("_precio_yes", 0.5)
    precios = ctx.get("precios_intraday", [])
    sigma_h = _estimar_vol_h(activo, precios, n_min=60) or 0.015
    T_h     = max(h, 0.05)
    prob_yes = None
    detalle  = ""

    # ── Bracket "between X and Y" ──────────────────────────────────────────
    m = _re.search(r"between[^0-9]*([0-9,]+(?:\.[0-9]+)?)[^0-9]+([0-9,]+(?:\.[0-9]+)?)", ql)
    if m:
        lo = float(m.group(1).replace(",", ""))
        hi = float(m.group(2).replace(",", ""))
        if lo > hi: lo, hi = hi, lo
        if lo <= spot <= hi:
            d_lo = math.log(spot / lo) / (sigma_h * math.sqrt(T_h))
            d_hi = math.log(hi / spot) / (sigma_h * math.sqrt(T_h))
            prob_yes = max(0.50, min(0.97, _norm_cdf(d_lo) + _norm_cdf(d_hi) - 1.0))
        else:
            dist = min(abs(spot - lo), abs(spot - hi))
            d    = dist / (spot * sigma_h * math.sqrt(T_h))
            prob_yes = max(0.03, 1.0 - _norm_cdf(abs(d)))
        detalle = f"bracket [{lo:.0f},{hi:.0f}] spot={spot:.0f}"

    # ── Precio objetivo "above/below $X" ───────────────────────────────────
    else:
        m2 = _re.search(r"\$([0-9,]+(?:\.[0-9]+)?)", q)
        if not m2:
            return None
        target   = float(m2.group(1).replace(",", ""))
        is_above = any(w in ql for w in ("above", "over", "reach", "exceed", "higher"))
        p_up = _gbm_p_up(spot, target, sigma_h, T_h)
        if p_up is None:
            return None
        prob_yes = p_up if is_above else (1.0 - p_up)
        detalle  = f"target={target:.0f} spot={spot:.0f} {'above' if is_above else 'below'}"

    edge = abs(prob_yes - py_mkt)
    if edge < 0.08 or abs(prob_yes - 0.5) < 0.30:
        return None

    return {
        "prob_yes": max(0.05, min(0.95, prob_yes)),
        "razon":    f"resolution_sniper {activo} {detalle} T={T_h:.2f}h σ={sigma_h:.4f}",
        "subtype":  f"{activo}#sniper",
    }


THETA_OU = 30.0  # calibrar con Jon-Becker cuando n≥200

LATE_WINDOW_DRIFT_MIN = 0.003   # 0.3 %/h mínimo en ventana para señal late-window
LATE_WINDOW_ENTRY_LO  = 160     # segundos desde inicio ventana: entrada mínima
LATE_WINDOW_ENTRY_HI  = 270     # segundos desde inicio ventana: entrada máxima


def s_late_window_5min(market: dict, ctx: dict):
    """
    Late-window arbitraje BTC 5min — inspirado en VyvanseWithMarijuana (36.5% ROI).

    Lógica: a T+160-270s dentro de una ventana de 5min, si BTC ya se ha movido
    > 0.3% desde el inicio de la ventana, Polymarket a menudo no ha actualizado
    precio aún → edge estructural en la dirección del movimiento.

    Sólo BTC (el par con mayor correlación y menor latencia en Polymarket).
    En shadow mode hasta n≥30 con IC>+0.05.
    """
    question = market.get("question", "")
    if "up or down" not in question.lower():
        return None
    tipo, ventana_min = _parse_updown_tipo(question)
    if tipo != "slot" or ventana_min != 5:
        return None
    activo = identificar_activo(question)
    if activo != "BTC":
        return None

    # Determinar posición temporal dentro de la ventana
    try:
        end_dt = datetime.fromisoformat(
            market.get("end_date", "").replace("Z", "+00:00"))
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None

    now_utc = datetime.now(timezone.utc)
    window_start = end_dt - timedelta(minutes=5)
    elapsed_s = (now_utc - window_start).total_seconds()

    if not (LATE_WINDOW_ENTRY_LO <= elapsed_s <= LATE_WINDOW_ENTRY_HI):
        return None  # fuera de la zona de entrada late-window

    # Drift BTC desde inicio de ventana usando klines intraday
    precios_data = ctx.get("precios_intraday", [])
    spot = _cargar_spot().get("BTC")
    if not spot or spot <= 0:
        return None

    ref = _precio_en("BTC", window_start, precios_data, tol_min=3)
    if ref is None or ref <= 0:
        return None

    drift_ventana = (spot / ref - 1)  # fracción, ej: +0.004 = +0.4%

    if abs(drift_ventana) < LATE_WINDOW_DRIFT_MIN:
        return None  # movimiento insuficiente

    # La señal sigue la dirección del drift (momentum intra-ventana)
    # BUY_YES si BTC subió, BUY_NO si BTC bajó
    p_up = 0.70 if drift_ventana > 0 else 0.30

    drift_15 = _calcular_drift_h("BTC", precios_data, 15)
    drift_60 = _calcular_drift_h("BTC", precios_data, 60)

    return {
        "prob_yes": p_up,
        "razon":    (f"late_window_5min BTC drift_ventana={drift_ventana*100:+.3f}% "
                     f"elapsed={elapsed_s:.0f}s p_up={p_up:.2f}"),
        "subtype":  "BTC#5min",
        "features": {
            "drift_ventana_pct":  round(drift_ventana * 100, 4),
            "elapsed_s":          round(elapsed_s, 1),
            "drift_15min":        round(drift_15 * 100, 4) if drift_15 is not None else None,
            "drift_60min":        round(drift_60 * 100, 4) if drift_60 is not None else None,
            "es_ntm_5min":        _es_ntm_5min(market),
        },
    }


GBM_LATE_15M_REST_MIN_LO = 3.0    # min restantes mínimos (suelo operables = 3min)
GBM_LATE_15M_REST_MIN_HI = 12.0   # min restantes máximos (salta los 3 primeros min)
GBM_LATE_15M_TARDIO_REST_MIN_HI = 10.5  # variante "entra más tarde" (reimplementada 09-Jul,
# la primera vez se perdió sin commitear — ver idea_gbm_late_tardio_08jul). Bucketing 08-Jul
# (n=645+71+24+16+5) sugería un sweet spot en [9,10.5)min IC+0.199, no una mejora monótona al
# alargar la espera ([5,7) cae a IC+0.056) — esta variante estrecha la ventana [3,12]->[3,10.5]
# para medir forward si ese sweet spot aguanta con n propio, no si "más tarde siempre es mejor".
GBM_LATE_60M_REST_MIN_LO = 5.0    # 60min: suelo más alto — libros finos al final
GBM_LATE_60M_REST_MIN_HI = 20.0   # 60min: último tercio de la ventana (T_h<0.33)
GBM_LATE_15M_PARES = {"BTC", "ETH", "SOL", "XRP"}
# 5min (14-Jul, sesión siguiente): rest_lo/rest_hi calibrados al timing real
# de wallet-timing analysis (analisis_timing_wallets_por_activo.py) — restante
# mediana 2.9-3.3min, p25 1.8-2.0min, p75 4.3-4.4min en BTC/ETH/SOL (las 3
# monedas que pasaron z-test + reparto de wallets, ver s_gbm_late_5min).
GBM_LATE_5M_REST_MIN_LO = 1.0
GBM_LATE_5M_REST_MIN_HI = 4.5
GBM_LATE_5M_PARES = {"BTC", "ETH", "SOL"}  # XRP excluido: z=+1.58 no concluyente (14-Jul)
# Banda de precio_yes_mercado donde el z-test confirmó edge real y repartido
# (no 1-2 wallets) en BTC#15min y en 5min BTC/ETH/SOL — favorito moderado/
# fuerte ya formado, no un longshot barato (esa banda <0.05 SÍ resultó ser
# 1-2 wallets, descartada). Usada por s_gbm_late_15min_py_confirmado y
# s_gbm_late_5min.
GBM_LATE_PY_CONFIRMADO_LO = 0.5
GBM_LATE_PY_CONFIRMADO_HI = 0.9
# Estrategias shadow-puras que deben SEGUIR generando predicciones aunque el
# postmortem las desactive por IC negativo con n pequeño. Sin esto caen en un
# estado ABSORBENTE: desactivada (n=8, 1 win → ic_bayes=-0.30 < umbral) → no
# genera → n nunca crece → sigue desactivada para siempre, matando el propósito
# del shadow (aprender). El gate real de dinero es la whitelist por tupla de
# live_trade (pares_permitidos_live); estas NO están ahí, así que forzar su
# generación no toca dinero real. GBM_LATE_60M = clon de entrada tardía 60min,
# necesita acumular n para medir si el edge tardío (probado en 15min, IC=+0.279)
# transfiere a ventanas 60min más profundas. (2026-07-06)
ACUMULAR_SHADOW_AUNQUE_DESACTIVADA = {"GBM_LATE_60M", "GBM_LATE_15M_TARDIO", "GBM_LATE_15M_ESPACIO_ATR",
                                      "STREAK_MOM_5M"}  # 2026-07-10: -0.052 IC n=306, no cruza umbral auto pero sin edge; desactivada manualmente en strategy_params.json (motivo "DESACTIVADA MANUALMENTE"), sigue midiendo sin ruido de atención
# Photo finish (2026-07-05): entrar con el precio pegado al strike es moneda
# al aire cobrada como favorito. |drift_ventana|<0.02% → IC=-0.145 n=181
# (win 35%), estable en ambas mitades temporales (-0.163/-0.127) y monótono
# con la distancia; buffer [0.02,0.05) ya es positivo en los 4 pares.
# Tracking forward: H-CUSTOM-LATE15-PHOTO-FINISH.
# 2026-07-11 (propuesta #5 backlog quant-desk, aprobado Javi): subido
# 0.02->0.03. barrido_vecinos.py con franja MARGINAL (analisis_drift_vent_
# por_par.py) mostró que la franja 0.02-0.03 es consistentemente mala en
# los 3 pares/direcciones con n suficiente: BTC n=100 hit=38.0% edge=-0.036,
# ETH#BUY_YES n=30 hit=36.7% edge=-0.017, SOL#BUY_YES n=19 hit=26.3%
# edge=-0.048 — las tres coinciden en recortarla, 0.03 es el único valor
# soportado por ETH y SOL (las 2 tuplas live) A LA VEZ. NO se sube más allá
# (a 0.05, donde BTC/ETH siguen mejorando) porque la franja 0.03-0.05 es
# BUENA específicamente para SOL (n=52 hit=65.4% edge=+0.023) — un umbral
# único más alto le cortaría a SOL una franja que rinde. Ver también
# ic_rolling.py (propuesta #5, gap pareado por activo: 0 divergencias en
# 117 claves — confirma que el efecto no es artefacto de composición).
# TODO (idea anotada, NO implementada — propuesta #5b, revisar con más n):
# separar este umbral por par en vez de un valor único (0.03 SOL / 0.05
# ETH+BTC parecen los óptimos individuales) — hoy las franjas marginales
# más finas por par (ej. SOL n=19 en la banda decisiva) están justo en el
# límite n>=15 del proyecto, demasiado ajustado para fiarse de un ajuste
# por par todavía. Revisar analisis_drift_vent_por_par.py cuando cada par
# tenga más resoluciones.
GBM_LATE_DRIFT_VENT_MIN_PCT = 0.03  # % — distancia mínima |spot vs ref ventana| (antes 0.02)

# Propuesta #1 (artículo breakout trading, 09-Jul): el "espacio" debería
# escalar con volatilidad propia del activo (ATR-multiplier), no ser un %
# fijo igual para BTC que para XRP. `d` ya se calcula en _s_gbm_late como
# log(spot/ref)/(sigma_h*sqrt(T_restante)) — es exactamente ese espacio
# estandarizado, solo que hoy no se usa como filtro. Analizado 09-Jul sobre
# GBM_LATE_15M (n=2462, feature d_gbm ya logueada): relación MONÓTONA fuerte,
# no un pico — hit 61.4%(n=2462)→64.5%(n=2010,|d|≥0.1)→69.4%(n=546,|d|≥0.4)
# →80.6%(n=62,|d|≥0.8). k=0.3 elegido como punto de partida con volumen
# comparable al filtro pct actual (n=841, hit 66.9%, edge+0.060) — no el
# óptimo del barrido (sería sobreajustar al mismo dataset que lo sugiere).
# Variante SEPARADA (mismo patrón que TARDIO/60M): dedup por (strategy,
# market_id) exige nombre propio, acumula IC desde cero. NO está en
# pares_permitidos_live — imposible que toque dinero real sin decisión
# explícita con n≥40.
GBM_LATE_ESPACIO_K = 0.3


def s_gbm_late_15min(market, ctx):
    """
    GBM de entrada tardía en ventanas 15min — estrategia propia (2026-07-02).

    Evidencia doble: (a) nuestras entradas tardías accidentales en GBM#15min
    (T_h<0.2) dan IC=+0.279 n=61 vs IC=-0.024 la entrada temprana; (b) el
    estudio de ballenas verificadas contra el leaderboard oficial muestra que
    los 3 mayores ganadores de estos mercados compran el lado que ya va
    ganando a mitad/final de ventana (zhangfan151 compra a 0.88 en la 2ª
    mitad, +$8.7k/mes). Mecanismo: con poco tiempo restante la varianza
    residual cae y el movimiento ya hecho domina el outcome, pero el precio
    de Polymarket se queda rezagado cerca de 50/50.

    Estrategia SEPARADA de UPDOWN_GBM a propósito: (1) el dedup por
    (strategy, market_id) impediría una segunda pasada bajo el mismo nombre;
    (2) acumula su propio IC desde cero; (3) no está en
    estrategias_permitidas_live → imposible que toque dinero real hasta
    decisión explícita.
    """
    return _s_gbm_late(market, ctx, ventana_min=15,
                       rest_lo=GBM_LATE_15M_REST_MIN_LO,
                       rest_hi=GBM_LATE_15M_REST_MIN_HI)


def s_gbm_late_60min(market, ctx):
    """
    GBM de entrada tardía en ventanas 60min (2026-07-03) — clona la mecánica
    de GBM_LATE_15M donde ya está validada (CLV +0.107, calibración
    infraconfiada en colas): entra solo en el último tercio (5-20 min
    restantes), cuando el movimiento hecho domina el outcome y el precio se
    rezaga. H-60MIN acumula IC≈+0.059 (BTC/ETH n=32) con entrada temprana —
    hipótesis: la tardía lo mejora igual que en 15min. Shadow puro: no está
    en pares_permitidos_live (whitelist fail-closed por tupla).
    """
    return _s_gbm_late(market, ctx, ventana_min=60,
                       rest_lo=GBM_LATE_60M_REST_MIN_LO,
                       rest_hi=GBM_LATE_60M_REST_MIN_HI)


def s_gbm_late_15min_tardio(market, ctx):
    """
    Variante de GBM_LATE_15M que espera más antes de entrar — REST_MIN_HI
    10.5 en vez de 12.0, estrechando la ventana de entrada a [3,10.5] min
    restantes (vs [3,12] de la estrategia real). Reimplementada 09-Jul: la
    primera versión (08-Jul) se perdió sin commitear (nunca llegó a git,
    dejó de generar predicciones desde las 15:20 UTC del 08-Jul sin que
    nadie lo notara). Pregunta: el bucketing retrospectivo de 08-Jul mostró
    un sweet spot en restante_min∈[9,10.5) (IC+0.199, n=71) mejor que la
    zona dominante [10.5,12) (IC+0.129, n=645) — pero [5,7) cae a IC+0.056,
    o sea NO es "cuanto más tarde mejor" sino un óptimo con tradeoff
    (mejor lectura del drift vs. libro que se adelgaza cerca del cierre).
    Esta estrategia mide forward, con n propio, si ese sweet spot aguanta.

    Estrategia SEPARADA de GBM_LATE_15M a propósito (mismo patrón que
    GBM_LATE_60M): dedup por (strategy, market_id) exige nombre propio;
    acumula su propio IC desde cero. NO está en pares_permitidos_live →
    imposible que toque dinero real hasta decisión explícita con n≥40.
    """
    return _s_gbm_late(market, ctx, ventana_min=15,
                       rest_lo=GBM_LATE_15M_REST_MIN_LO,
                       rest_hi=GBM_LATE_15M_TARDIO_REST_MIN_HI)


def s_gbm_late_15min_espacio_atr(market, ctx):
    """
    Variante de GBM_LATE_15M con el "espacio" (distancia mínima al ancla)
    escalado por volatilidad propia del activo en vez de un % fijo — ver
    GBM_LATE_ESPACIO_K arriba para el análisis que motiva k=0.3. Mide
    forward si sustituir GBM_LATE_DRIFT_VENT_MIN_PCT por |d|>=k mejora el
    edge sin perder demasiado volumen, con n propio (n=0 al arrancar).
    """
    return _s_gbm_late(market, ctx, ventana_min=15,
                       rest_lo=GBM_LATE_15M_REST_MIN_LO,
                       rest_hi=GBM_LATE_15M_REST_MIN_HI,
                       espacio_k=GBM_LATE_ESPACIO_K)


def s_gbm_late_15min_py_confirmado(market, ctx):
    """
    Variante de GBM_LATE_15M restringida a BTC y a la banda de precio donde
    el análisis de timing de wallets 'smart' (14-Jul, sesión siguiente,
    analisis_timing_wallets_por_activo.py) confirmó edge real CON
    significancia: precio_yes_mercado ya en [0.5,0.9) (favorito
    moderado/fuerte ya formado) en el momento de la señal.

    z-test contra el precio implicado (H0: mercado eficiente, gana con
    prob=precio): banda [0.50,0.70) z=+2.63 n=188, banda [0.70,0.90)
    z=+2.27 n=61 — ambas con reparto amplio entre wallets (16/10 distintas,
    ninguna aporta más del 32%/24% del PnL). Solo BTC: fue la ÚNICA moneda
    que pasó las dos barras (significancia Y reparto, no 1-2 cuentas) en
    15min — ETH/SOL/XRP en la misma banda mostraron señales igual de
    "espectaculares" (z hasta 3.2) pero resultaron ser 77-95% el PnL de UNA
    sola wallet, descartadas. BTC#60min banda barata también descartada
    por el mismo motivo (top1=78%).

    Estrategia SEPARADA de GBM_LATE_15M a propósito (dedup por
    (strategy, market_id) exige nombre propio; acumula su propio IC desde
    cero). NO está en pares_permitidos_live — shadow puro hasta n≥40
    propio y decisión explícita de Javi. Ver memoria
    idea_timing_wallets_smart_vs_sistema_14jul.
    """
    activo = identificar_activo(market.get("question", ""))
    if activo != "BTC":
        return None
    py = market.get("_precio_yes")
    if py is None or not (GBM_LATE_PY_CONFIRMADO_LO <= py < GBM_LATE_PY_CONFIRMADO_HI):
        return None
    return _s_gbm_late(market, ctx, ventana_min=15,
                       rest_lo=GBM_LATE_15M_REST_MIN_LO,
                       rest_hi=GBM_LATE_15M_REST_MIN_HI)


def s_gbm_late_5min(market, ctx):
    """
    GBM de entrada tardía en ventanas de 5min (14-Jul, sesión siguiente) —
    NUNCA antes probado a esta escala (_s_gbm_late ya operaba a 15/60min
    desde 03-Jul; las hipótesis de 5min previas, H-5MIN-REVERSIÓN y
    H-OU-5MIN, probaban REVERSIÓN —apostar CONTRA el movimiento reciente—
    y están refutadas/desactivadas; esto es CONFIRMACIÓN, mecanismo
    opuesto, nunca antes probado).

    Motivado por wallet-timing analysis (analisis_timing_wallets_por_activo.py):
    banda de precio_yes_mercado [0.5,0.9) en mercados Up/Down de 5min
    muestra z-test fortísimo contra el precio implicado y REPARTIDO entre
    muchas wallets (no 1-2 cuentas, a diferencia de la banda barata <0.05
    que sí resultó ser eso): BTC z=+14.25 n=2961 32 wallets top1=12%,
    ETH z=+5.77 n=657 19 wallets top1=30%, SOL z=+6.81 n=532 16 wallets
    top1=30% — 3 monedas confirman el mismo patrón (pasa el criterio de
    confirmación cruzada del proyecto). XRP EXCLUIDO (z=+1.58, no
    concluyente, n menor).

    rest_lo/rest_hi calibrados al timing real de las wallets (restante
    mediana 2.9-3.3min, p25 1.8-2.0min, p75 4.3-4.4min en las 3 monedas).

    Estrategia SEPARADA (dedup exige nombre propio). NO está en
    pares_permitidos_live — shadow puro hasta n≥40 propio y decisión
    explícita de Javi. Ver memoria idea_timing_wallets_smart_vs_sistema_14jul.
    """
    activo = identificar_activo(market.get("question", ""))
    if activo not in GBM_LATE_5M_PARES:
        return None
    py = market.get("_precio_yes")
    if py is None or not (GBM_LATE_PY_CONFIRMADO_LO <= py < GBM_LATE_PY_CONFIRMADO_HI):
        return None
    return _s_gbm_late(market, ctx, ventana_min=5,
                       rest_lo=GBM_LATE_5M_REST_MIN_LO,
                       rest_hi=GBM_LATE_5M_REST_MIN_HI)


def _s_gbm_late(market, ctx, ventana_min, rest_lo, rest_hi, espacio_k=None):
    question = market.get("question", "")
    if "up or down" not in question.lower():
        return None
    tipo, vent = _parse_updown_tipo(question)
    # 15min llega como slot con rango explícito; 60min como hourly (o slot de 60)
    if vent != ventana_min or tipo not in ("slot", "hourly"):
        return None
    activo = identificar_activo(question)
    if activo not in GBM_LATE_15M_PARES:
        return None

    try:
        end_dt = datetime.fromisoformat(
            market.get("end_date", "").replace("Z", "+00:00"))
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None

    now_utc = datetime.now(timezone.utc)
    restante_min = (end_dt - now_utc).total_seconds() / 60.0
    if not (rest_lo <= restante_min <= rest_hi):
        return None

    precios_data = ctx.get("precios_intraday", [])
    spot = _cargar_spot().get(activo)
    if not spot or spot <= 0:
        return None

    window_start = end_dt - timedelta(minutes=ventana_min)
    ref = _precio_en(activo, window_start, precios_data, tol_min=3)
    if ref is None or ref <= 0:
        return None

    sigma_h = _estimar_vol_h(activo, precios_data, n_min=20) or 0.02
    T_rem_h = restante_min / 60.0
    # P(cierre > apertura de ventana) con lo ya movido como ventaja:
    # d = ln(spot/ref) / (sigma * sqrt(T_restante))
    import math
    denom = sigma_h * math.sqrt(max(T_rem_h, 1e-6))
    if denom <= 0:
        return None
    d = math.log(spot / ref) / denom
    p_up = _norm_cdf(d)

    drift_ventana = spot / ref - 1
    # Photo finish: sin distancia real al strike no hay señal, solo ruido 50/50.
    # espacio_k (propuesta #1, 09-Jul): variante que sustituye el % fijo por
    # el espacio ya estandarizado por volatilidad (|d|), en vez de apilar
    # ambos filtros sobre la misma variante.
    if espacio_k is not None:
        if abs(d) < espacio_k:
            return None
    elif abs(drift_ventana * 100) < GBM_LATE_DRIFT_VENT_MIN_PCT:
        return None
    py = market.get("_precio_yes")
    if py is None:
        return None

    edge = p_up - py
    # Mismo listón que el resto: EDGE_MINIMO lo aplica main() sobre edge_neto;
    # aquí solo se exige señal direccional mínima para no emitir ruido 50/50.
    if abs(edge) < 0.03:
        return None

    # Anchura de mercado (09-Jul, análisis con precios reales 05-09jul, n=802):
    # media del retorno concurrente (mismo tramo de ventana, sin fuga — solo
    # hasta "ahora") de los otros 3 majors de GBM_LATE_15M. Señal real y NO
    # redundante con drift_ventana_pct propio (correlación 0.26): decil bajo
    # IC=-0.146 hit=35% vs decil alto IC=+0.29 hit~75-80%, monótono. Puro
    # logging — no cambia edge ni decisión, alimenta el bucket causal existente
    # (postmortem IC_bucket) y H-CUSTOM-GBMLATE-ANCHURA-MERCADO.
    spot_map = _cargar_spot()
    otros_rets = []
    for otro in GBM_LATE_15M_PARES:
        if otro == activo:
            continue
        spot_otro = spot_map.get(otro)
        ref_otro = _precio_en(otro, window_start, precios_data, tol_min=3)
        if not spot_otro or spot_otro <= 0 or not ref_otro or ref_otro <= 0:
            continue
        otros_rets.append(spot_otro / ref_otro - 1)
    mercado_anchura_pct = (round(sum(otros_rets) / len(otros_rets) * 100, 4)
                           if len(otros_rets) == len(GBM_LATE_15M_PARES) - 1 else None)

    # drift_20min_pct / ibs_20min (10-Jul, ver _drift_e_ibs_ventana): momentum
    # muy reciente, distinto de drift_ventana_pct (que mide desde la apertura
    # de ESTA ventana de {ventana_min}min, no una ventana fija de 20min).
    drift_20min_pct, ibs_20min = _drift_e_ibs_ventana(activo, precios_data, 20)
    dist_ancla_estructural_pct = _dist_ancla_estructural_pct(activo, precios_data, horas_lookback=3)
    volumen_regimen = ctx.get("volumen_regimen", {}).get(activo)

    # dist_vwap_pct (11-Jul, paper Zarattini/Aziz "VWAP the Holy Grail"): ya
    # existía en UPDOWN_GBM desde 07-Jul pero nunca se extendió aquí. Chequeo
    # manual sobre UPDOWN_GBM (ver FEATURE_RULES en shadow_postmortem.py):
    # BUY_NO a-favor-de-tendencia (spot<VWAP) ic+0.038 n=78 vs contra-tendencia
    # (spot>=VWAP) ic-0.105 n=36 — puro logging, no cambia edge ni decisión.
    _vwap_sesion = ctx.get("vwap_sesion", {}).get(activo)
    dist_vwap_pct = (round((spot - _vwap_sesion) / _vwap_sesion * 100, 4)
                      if _vwap_sesion and spot and _vwap_sesion > 0 else None)

    # SE aproximado de d_gbm (propuesta #2, backlog quant-desk 13-jul, Part
    # II del artículo de simulación cuantitativa): la varianza del estimador
    # es máxima justo en p=0.5, donde opera GBM_LATE. sigma_h tiene un error
    # de estimación relativo ~1/sqrt(2N) (N=nº de log-retornos usados, delta
    # method sobre la varianza muestral); como d=C/sigma_h, se propaga a
    # SE(d)≈|d|/sqrt(2N). Solo LOGUEA — no cambia edge/decisión, mismo
    # patrón que libro_spread/es_ntm_5min: el pipeline causal decide si
    # hace falta filtrar señales con sigma_h mal estimado.
    n_obs_vol = _n_obs_vol_h(activo, precios_data, n_min=20)
    se_d_gbm_aprox = round(abs(d) / math.sqrt(2 * n_obs_vol), 4) if n_obs_vol >= 2 else None

    # sigma_h EWMA half_life=10min, solo logueo (propuesta #11, ver
    # _estimar_vol_h_ewma) — n_min=20 igual que sigma_h real de esta función.
    sigma_h_ewma10 = _estimar_vol_h_ewma(activo, precios_data, n_min=20, half_life_min=10)
    # Aceleración de volatilidad = EWMA reciente vs ventana plana, en % relativo
    # (12-Jul, petición Javi "modelo más rápido" + sugerencia de desagregar por
    # activo): verificado con forward n=66-86/activo que el SIGNO de este efecto
    # NO es uniforme — ETH +16pp / BTC +10.5pp cuando la vol acelera (ewma>flat),
    # XRP -11.7pp (signo OPUESTO), SOL sin efecto. Mezclado en agregado esto se
    # diluye a un +3.5pp que parece débil — desagregado por activo es mucho más
    # fuerte en 3 de los 4. Solo LOGUEA aquí; entra en FEATURE_RULES abajo para
    # que el pipeline causal descubra el umbral/signo correcto POR ACTIVO solo.
    sigma_ewma_delta_pct = (
        round((sigma_h_ewma10 - sigma_h) / sigma_h * 100, 3)
        if sigma_h_ewma10 is not None and sigma_h > 0 else None
    )

    # retest_pct (13-Jul, ver analisis_retest_gbm_late.py / _calcular_retest_pct):
    # solo logueo, no cambia edge ni decisión — ver docstring del helper.
    retest_pct = _calcular_retest_pct(activo, window_start, now_utc, ref, spot, precios_data)

    return {
        "prob_yes": round(p_up, 4),
        "razon":    (f"gbm_late_{ventana_min}min {activo} drift_vent={drift_ventana*100:+.3f}% "
                     f"rest={restante_min:.1f}min d={d:+.2f} p_up={p_up:.2f} py={py:.2f}"),
        "subtype":  f"{activo}#{ventana_min}min",
        "features": {
            "drift_ventana_pct":   round(drift_ventana * 100, 4),
            "restante_min":        round(restante_min, 2),
            "T_h":                 round(T_rem_h, 4),
            "sigma_h":             round(sigma_h, 5),
            "d_gbm":               round(d, 3),
            "py_entrada":          round(py, 3),
            "hora_utc":            now_utc.hour,
            "mercado_anchura_pct": mercado_anchura_pct,
            "drift_20min_pct":     drift_20min_pct,
            "ibs_20min":           ibs_20min,
            "dist_ancla_estructural_pct": dist_ancla_estructural_pct,
            "volumen_regimen":     volumen_regimen,
            "n_obs_vol_h":         n_obs_vol,
            "se_d_gbm_aprox":      se_d_gbm_aprox,
            "sigma_h_ewma10":      round(sigma_h_ewma10, 5) if sigma_h_ewma10 is not None else None,
            "sigma_ewma_delta_pct": sigma_ewma_delta_pct,
            "dist_vwap_pct":       dist_vwap_pct,
            "retest_pct":          retest_pct,
            **_libro_calidad(market),
        },
    }


def s_updown_ou_5m(market, ctx):
    """
    OU (Ornstein-Uhlenbeck) para slots de 5min — hipótesis mean-reversion.
    Corre en PARALELO con UPDOWN_GBM para acumular evidencia.
    No reemplaza GBM hasta que IC_OU > IC_GBM con n≥200.
    Fórmula: p_up = 0.5 - pct_spot_vs_ref * THETA_OU
    """
    question = market.get("question", "")
    if "up or down" not in question.lower():
        return None
    tipo, ventana_min = _parse_updown_tipo(question)
    if tipo != "slot" or ventana_min != 5:
        return None

    activo = identificar_activo(question)
    if not activo:
        return None

    precios_data = ctx.get("precios_intraday", [])
    spot = _cargar_spot().get(activo)
    if not spot or spot <= 0:
        return None

    try:
        end_dt = datetime.fromisoformat(
            market.get("end_date","").replace("Z","+00:00"))
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
    except Exception:
        return None

    ref_time = end_dt - timedelta(minutes=5)
    tol_min  = 3
    ref = _precio_en(activo, ref_time, precios_data, tol_min)
    if ref is None or ref <= 0:
        return None

    pct = (spot / ref - 1)
    if abs(pct) < 0.0001:   # sin señal cuando spot≈ref
        return None

    sigma_h = _estimar_vol_h(activo, precios_data, n_min=20) or 0.02

    # Filtro de fuerza de señal: solo disparar si |pct| ≥ 0.8 desviaciones típicas.
    # Datos (n=21): todas las señales actuales tienen 0.24-0.50σ → ruido puro.
    # Una señal de mean-reversion necesita al menos 0.8σ para ser estadísticamente
    # distinguible de una fluctuación aleatoria.
    T_h_slot = max(market.get("_horas", 0.083), 0.05)
    sigma_T = sigma_h * math.sqrt(T_h_slot)  # desviación típica total del slot
    signal_strength = abs(pct) / sigma_T if sigma_T > 0 else 0
    OU_SIGNAL_MIN = 0.5  # σ mínimas. 0.8σ = demasiado estricto (0 señales). Calibrar con Jon-Becker.
    if signal_strength < OU_SIGNAL_MIN:
        return None

    p_up = max(0.05, min(0.95, 0.5 - pct * THETA_OU))
    drift_15 = _calcular_drift_h(activo, precios_data, 15)
    drift_60 = _calcular_drift_h(activo, precios_data, 60)
    delta_macro = _calcular_delta_ratio_macro(activo, ctx.get("klines_raw", {}))

    features = {
        "pct_spot_vs_ref": round(pct * 100, 4),
        "sigma_h":          round(sigma_h, 6),
        "theta_ou":         THETA_OU,
        "es_ntm_5min":      _es_ntm_5min(market),
    }
    if drift_15 is not None: features["drift_15min"] = round(drift_15 * 100, 4)
    if drift_60 is not None: features["drift_60min"] = round(drift_60 * 100, 4)
    if delta_macro is not None: features["delta_ratio_macro"] = round(delta_macro, 4)

    return {
        "prob_yes": p_up,
        "razon":   f"ou_5m {activo} pct={pct*100:+.3f}% θ={THETA_OU} p_up={p_up:.3f}",
        "subtype": f"{activo}#5min",
        "features": features,
    }


# ── STRUCT_NO_15M — factor estructural "sobreprecio del YES" (model-free) ──────
# Hallazgo 2026-07-05: en los cripto Up/Down 15min, el NO gana sistemáticamente
# por encima de su precio implícito CUANDO es el favorito leve (precio_yes<0.50).
# No es simétrico (respaldar el YES-favorito da EV negativo) → es el sesgo
# conductual "el retail compra Up" aislado del GBM. Backtest mercados únicos
# BTC+ETH+SOL BUY_NO py∈[0.47,0.50): n=459 P(NO)=55.6% EV_neto(fee 2%)=+0.066.
# Modelo: P(YES)=0.43 (P(NO)≈0.57) en la zona coinflip. Calibrado a la sub-banda
# de disparo real py∈[0.47,0.50), donde el empírico es P(NO)=0.556 (n=459). Con el
# gate de main() (slippage 0.02 + edge_min 0.02) este prob_yes hace que dispare
# BUY_NO exactamente en [0.47,0.50) —el tramo de mayor EV— sin riesgo de misfire a
# BUY_YES (imposible en la banda). El prob_yes solo fija el umbral de decisión: el
# PnL/IC se miden con resultados reales en shadow_resolve, no con este valor.
# Shadow puro: NO está en pares_permitidos_live → jamás opera en vivo. XRP excluido
# (P(NO)=0.51, sin edge), BNB/DOGE fuera (n minúsculo).
STRUCT_NO_15M_PARES = {"BTC", "ETH", "SOL"}
STRUCT_NO_PY_LO = 0.44   # banda coinflip observada (fires ~[0.47,0.50), resto SKIP)
STRUCT_NO_PY_HI = 0.50
STRUCT_NO_PROB_YES = 0.43  # P(YES) justo ≈ 1 - P(NO)(0.556) en la sub-banda de disparo

def _libro_calidad(market: dict) -> dict:
    """spread/liquidez del libro en el momento de la señal (item 7 checklist
    08-Jul, idea del playbook KOL Layer 1: "libro limpio" antes de entrar).
    Campos ya presentes en el market dict (capture_markets), sin llamada extra.
    Solo LOGUEA — el pipeline causal existente (postmortem -> IC_bucket ->
    filtro_causal, N_BUCKET_MIN=15) decide solo si hace falta un umbral; no se
    hardcodea ninguno aquí para no perder N en shadow con estrategias que aún
    no están live (STREAK_*/STRUCT_NO_15M fuera de whitelist hoy)."""
    try:
        spread = float(market.get("spread") or 0)
    except (ValueError, TypeError):
        spread = None
    try:
        liquidez = float(market.get("liquidity") or 0)
    except (ValueError, TypeError):
        liquidez = None
    return {"libro_spread": spread, "libro_liquidez": liquidez}


def _es_ntm_5min(market: dict, ancho: float = 0.05) -> int:
    """Flag near-the-money (propuesta #14, 13-jul, paper Dai/Jia/Yu
    "Settlement Manipulation in Prediction Markets"): precio YES a menos de
    `ancho` de 0.50 al momento de la señal. Hallazgo del paper: en el
    contrato de 5min, ciclos NTM (cerca de 50%) se voltean 65% de las veces
    con manipulación de push en los últimos ~10s (vs 41% normal); en 15min
    el patrón casi desaparece. Solo LOGUEA — mismo patrón que
    _libro_calidad: el pipeline causal decide si hace falta filtrar, no se
    hardcodea ningún veto aquí."""
    py = market.get("_precio_yes")
    if py is None:
        return 0
    return int(abs(py - 0.5) <= ancho)


def s_struct_no_15m(market, ctx):
    question = market.get("question", "")
    if "up or down" not in question.lower():
        return None
    tipo, vent = _parse_updown_tipo(question)
    if tipo != "slot" or vent != 15:
        return None
    activo = identificar_activo(question)
    if activo not in STRUCT_NO_15M_PARES:
        return None
    py = market.get("_precio_yes")
    if py is None or not (STRUCT_NO_PY_LO <= py < STRUCT_NO_PY_HI):
        return None

    restante_min = None
    try:
        end_dt = datetime.fromisoformat(market.get("end_date", "").replace("Z", "+00:00"))
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
        restante_min = round((end_dt - datetime.now(timezone.utc)).total_seconds() / 60.0, 2)
    except Exception:
        pass

    return {
        "prob_yes": STRUCT_NO_PROB_YES,
        "razon":    f"struct_no_15m {activo} py={py:.3f} (favorito-NO leve, model-free)",
        "subtype":  f"{activo}#15min",
        "features": {
            "py_entrada":   round(py, 3),
            "restante_min": restante_min,
            "hora_utc":     datetime.now(timezone.utc).hour,
            **_libro_calidad(market),
        },
    }


# ── FAVORITO_CONFIRMADO — model-free, replica el patrón de las wallets ──────────
# ganadoras estudiadas 2026-07-10 (project_estudio_bots_ganadores_10jul): 0x20d2309c
# (+447€, 97% TAKER, paga el mismo fee que nosotros) y BoneOhio (+527€, compra y
# mantiene igual que nosotros) NO tienen ventaja de estructura de fee — su edge es
# comprar el lado que el MERCADO ya confirma como favorito (precio_yes mediana 0.63
# y 0.67 respectivamente, 58%/62% de sus entradas en zona >=0.55), sin sesgo
# direccional (46-56% Up en todas las wallets estudiadas). El timing NO separa
# ganadores de perdedores (0x20d2309c entra al 58.7% de ventana restante, la
# perdedora sixx7 casi igual, 58.3%) — la señal es puramente el NIVEL DE PRECIO.
#
# Model-free a propósito (mismo patrón que STRUCT_NO_15M): no hay estimación de
# drift/sigma detrás, solo la hipótesis "el mercado seguirá confirmando lo que ya
# empezó a confirmar" (momentum de consenso), la hipótesis contraria a nuestras
# estrategias GBM que buscan entrar ANTES de que el precio lo refleje (backtest
# 10-Jul: nuestro edge real vive en precio_yes∈[0.45,0.53), EV+0.308 n=955 —
# filtrar por precio>=0.55 ahí DESTRUYE el 95% de ese EV, ver
# idea_4_propuestas_09jul_resueltas). Por eso esta es una estrategia SEPARADA, no
# un filtro sobre GBM_LATE: mide si el momentum-de-consenso tiene edge PROPIO,
# independiente del edge de anticipación que ya capturamos en otro sitio.
#
# El nudge de prob_yes es un valor de partida (no calibrado) solo para que la
# señal cruce EDGE_MINIMO y genere volumen medible — el veredicto real lo da
# ic_bayes del bucket en shadow_postmortem con n>=40, no este número.
# Shadow puro: NO está en pares_permitidos_live → jamás opera en vivo.
FAVORITO_CONFIRMADO_PARES = {"BTC", "ETH", "SOL", "XRP"}
FAVORITO_CONFIRMADO_UMBRAL = 0.55  # nivel de precio que "confirma" favorito
FAVORITO_CONFIRMADO_UMBRAL_BAJO = round(1.0 - FAVORITO_CONFIRMADO_UMBRAL, 4)  # 0.45 exacto —
# NO derivar como "1.0 - FAVORITO_CONFIRMADO_UMBRAL" inline en la comparación: sin el
# round(), da 0.44999999999999996 (float) y excluye py=0.45 exacto del lado NO, justo
# el valor más probable de aparecer (Polymarket cotiza en incrementos limpios). Cazado
# por test unitario antes de desplegar.
FAVORITO_CONFIRMADO_NUDGE = 0.06   # empuje de la hipótesis, sin calibrar


def s_favorito_confirmado(market, ctx):
    question = market.get("question", "")
    if "up or down" not in question.lower():
        return None
    tipo, vent = _parse_updown_tipo(question)
    if tipo not in ("slot", "hourly"):
        return None
    activo = identificar_activo(question)
    if activo not in FAVORITO_CONFIRMADO_PARES:
        return None
    py = market.get("_precio_yes")
    if py is None:
        return None

    if py >= FAVORITO_CONFIRMADO_UMBRAL:
        prob_yes = min(0.97, py + FAVORITO_CONFIRMADO_NUDGE)
        lado = "YES"
    elif py <= FAVORITO_CONFIRMADO_UMBRAL_BAJO:
        prob_yes = max(0.03, py - FAVORITO_CONFIRMADO_NUDGE)
        lado = "NO"
    else:
        return None  # zona coinflip — no es la hipótesis que medimos aquí

    restante_min = None
    try:
        end_dt = datetime.fromisoformat(market.get("end_date", "").replace("Z", "+00:00"))
        if end_dt.tzinfo is None:
            end_dt = end_dt.replace(tzinfo=timezone.utc)
        restante_min = round((end_dt - datetime.now(timezone.utc)).total_seconds() / 60.0, 2)
    except Exception:
        pass

    return {
        "prob_yes": prob_yes,
        "razon":    f"favorito_confirmado {activo} py={py:.3f} lado={lado} (momentum-consenso, model-free)",
        "subtype":  f"{activo}#{vent}min" if vent else activo,
        "features": {
            "py_entrada":   round(py, 3),
            "restante_min": restante_min,
            "hora_utc":     datetime.now(timezone.utc).hour,
            **_libro_calidad(market),
        },
    }


# ── STREAK — momentum (5min) / reversión (15min) en la SECUENCIA de resoluciones ──
# Hallazgo 2026-07-05: nadie miraba la secuencia de ventanas (todas las estrategias
# las tratan como independientes). El signo se INVIERTE por escala:
#   5min  → MOMENTUM:  tras ≥3 resoluciones iguales, continúa (n=189 58% EV+0.15).
#   15min → REVERSIÓN: tras ≥4 resoluciones iguales, revierte (n=68 71% EV+0.28;
#           en el slice de entrada temprana py~0.50: 80% EV+0.53).
# Mecanismo: en 5min el flujo persiste (momentum); en 15min el retail persigue la
# racha, sobre-extiende y revierte. Entrada AL ABRIR la ventana (py∈[0.47,0.53]): el
# timing es crítico (si el precio ya derivó, el edge muere). BTC excluido (flojo en
# ambas). Shadow puro: no en pares_permitidos_live → jamás opera en vivo.
_STREAK_SEQ = None

def _cargar_outcomes_recientes():
    """Lee results.csv → {(activo, ventana_min): [(end_dt, outcome), ...] ordenado}.
    Un outcome por ventana (mayoría). Cache por proceso (predict corre fresco c/ciclo)."""
    global _STREAK_SEQ
    if _STREAK_SEQ is not None:
        return _STREAK_SEQ
    acc = {}
    try:
        with open(DIR_SHADOW / "results.csv", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                sub = r.get("subtype") or ""
                if "#" not in sub:
                    continue
                activo, resto = sub.split("#", 1)
                if activo not in ("BTC", "ETH", "SOL", "XRP"):
                    continue
                vent = 5 if resto == "5min" else (15 if resto == "15min" else None)
                if vent is None:
                    continue
                out = r.get("outcome_real")
                if out not in ("YES", "NO"):
                    continue
                try:
                    edt = datetime.fromisoformat((r.get("end_date") or "").replace("Z", "+00:00"))
                    if edt.tzinfo is None:
                        edt = edt.replace(tzinfo=timezone.utc)
                except Exception:
                    continue
                acc.setdefault((activo, vent), {}).setdefault(edt, []).append(out)
    except FileNotFoundError:
        _STREAK_SEQ = {}
        return _STREAK_SEQ
    seqs = {}
    for key, d in acc.items():
        seqs[key] = [(edt, ("YES" if o.count("YES") >= o.count("NO") else "NO"))
                     for edt, o in ((e, d[e]) for e in sorted(d))]
    # Cobertura 5min desde klines (fix 08-Jul): results.csv solo tiene ventanas
    # 5min cuando alguna estrategia predijo (4-14/día, nunca adyacentes) →
    # STREAK_MOM_5M no disparaba jamás. fetch_binance_klines mantiene
    # outcomes_5m_klines.json (rolling 48h, convención validada 98.6% n=738
    # contra outcome oficial). El outcome oficial de results.csv gana en conflicto.
    try:
        kl = json.loads((DIR_SHADOW / "outcomes_5m_klines.json").read_text())
    except Exception:
        kl = {}
    for activo, outs in kl.items():
        if activo not in ("BTC", "ETH", "SOL", "XRP") or not isinstance(outs, dict):
            continue
        d5 = dict(seqs.get((activo, 5), []))
        for iso, out in outs.items():
            if out not in ("YES", "NO"):
                continue
            try:
                edt = datetime.fromisoformat(iso)
                if edt.tzinfo is None:
                    edt = edt.replace(tzinfo=timezone.utc)
            except ValueError:
                continue
            d5.setdefault(edt, out)
        seqs[(activo, 5)] = sorted(d5.items())
    _STREAK_SEQ = seqs
    return _STREAK_SEQ

def _racha_actual(activo, ventana_min, current_end_dt):
    """Racha de resoluciones consecutivas de ventanas ANTERIORES a la actual.
    Exige que la última resuelta sea adyacente (una ventana antes) para no usar
    rachas obsoletas. Devuelve (longitud, direccion) o (0, None)."""
    seq = _cargar_outcomes_recientes().get((activo, ventana_min))
    if not seq:
        return 0, None
    gap = ventana_min * 60
    tol = max(30, gap * 0.05)
    prev = [(edt, o) for edt, o in seq if edt < current_end_dt]
    if not prev:
        return 0, None
    prev.sort()
    if abs((current_end_dt - prev[-1][0]).total_seconds() - gap) > tol:
        return 0, None  # última resuelta no es adyacente → racha obsoleta
    k = 1
    d = prev[-1][1]
    for i in range(len(prev) - 1, 0, -1):
        if abs((prev[i][0] - prev[i - 1][0]).total_seconds() - gap) > tol:
            break
        if prev[i - 1][1] == d:
            k += 1
        else:
            break
    return k, d

STREAK_MOM_5M_PARES = {"SOL", "ETH", "XRP"}    # BTC excluido (flojo, EV≈0)
STREAK_FADE_15M_PARES = {"ETH", "SOL", "XRP"}  # BTC excluido (flojo, EV≈0)
STREAK_PY_LO = 0.47   # entrada temprana / coinflip: fuera de esta banda el edge muere
STREAK_PY_HI = 0.53

def _streak_end_dt(market):
    try:
        edt = datetime.fromisoformat(market.get("end_date", "").replace("Z", "+00:00"))
        return edt.replace(tzinfo=timezone.utc) if edt.tzinfo is None else edt
    except Exception:
        return None

def s_streak_mom_5m(market, ctx):
    q = market.get("question", "")
    if "up or down" not in q.lower():
        return None
    tipo, vent = _parse_updown_tipo(q)
    if tipo != "slot" or vent != 5:
        return None
    activo = identificar_activo(q)
    if activo not in STREAK_MOM_5M_PARES:
        return None
    py = market.get("_precio_yes")
    if py is None or not (STREAK_PY_LO <= py <= STREAK_PY_HI):
        return None
    edt = _streak_end_dt(market)
    if edt is None:
        return None
    k, d = _racha_actual(activo, 5, edt)
    if k < 3 or d is None:
        return None
    # momentum: SEGUIR la racha. prob_yes = P(continuación)≈0.58 empírico
    prob_yes = 0.58 if d == "YES" else 0.42
    return {
        "prob_yes": prob_yes,
        "razon":    f"streak_mom_5m {activo} racha={k}x{d} py={py:.3f} (momentum)",
        "subtype":  f"{activo}#5min",
        "features": {
            "streak_len":    k,
            "streak_dir_up": 1 if d == "YES" else 0,
            "py_entrada":    round(py, 3),
            "hora_utc":      datetime.now(timezone.utc).hour,
            "es_ntm_5min":   _es_ntm_5min(market),
            **_libro_calidad(market),
        },
    }

STREAK_FADE_5M_PARES = {"SOL", "ETH", "XRP"}  # mismo universo que STREAK_MOM_5M

def s_streak_fade_5m(market, ctx):
    """
    Espejo invertido de STREAK_MOM_5M (11-Jul, bloque B backlog ítem 1 —
    Javi: "1 y 2 no tienen otra visión que les haga candidatos a
    estrategia"). STREAK_MOM_5M (sigue la racha, k>=3, mismos 3 pares)
    lleva IC_bayes=-0.0548 n=308 (desactivada 10-Jul). Un IC negativo en
    una apuesta direccional es matemáticamente evidencia a favor de la
    apuesta OPUESTA: invertir cada decisión histórica (BUY_YES<->BUY_NO)
    da IC_bayes=+0.0548 n=308 (BUY_YES original -0.0685 n=144 -> fade
    +0.0685; BUY_NO original -0.0422 n=164 -> fade +0.0422). No cruza
    todavía el gate live (IC>=0.08 n>=40) y es la MISMA muestra que ya
    generó el hallazgo (no es validación forward independiente) — por eso
    nace como estrategia separada, mide su propio n desde cero con precio
    de entrada real del lado contrario (distinto slippage/edge_neto que
    negar directamente el histórico de MOM). Mismo patrón que
    STREAK_FADE_15M (reversión probada ahí, IC+0.117) pero a 5min.
    NO está en pares_permitidos_live — shadow puro, cero riesgo real.
    """
    q = market.get("question", "")
    if "up or down" not in q.lower():
        return None
    tipo, vent = _parse_updown_tipo(q)
    if tipo != "slot" or vent != 5:
        return None
    activo = identificar_activo(q)
    if activo not in STREAK_FADE_5M_PARES:
        return None
    py = market.get("_precio_yes")
    if py is None or not (STREAK_PY_LO <= py <= STREAK_PY_HI):
        return None
    edt = _streak_end_dt(market)
    if edt is None:
        return None
    k, d = _racha_actual(activo, 5, edt)
    if k < 3 or d is None:
        return None
    # reversión: FADEAR la racha (espejo de streak_mom_5m, que la sigue)
    prob_yes = 0.42 if d == "YES" else 0.58
    return {
        "prob_yes": prob_yes,
        "razon":    f"streak_fade_5m {activo} racha={k}x{d} py={py:.3f} (reversión, espejo de MOM)",
        "subtype":  f"{activo}#5min",
        "features": {
            "streak_len":    k,
            "streak_dir_up": 1 if d == "YES" else 0,
            "py_entrada":    round(py, 3),
            "hora_utc":      datetime.now(timezone.utc).hour,
            "es_ntm_5min":   _es_ntm_5min(market),
            **_libro_calidad(market),
        },
    }


# Items 11/12 del checklist 08-Jul (idea_streak_fade_15m, artículo Spicy
# mean-reversion): régimen (¿la reversión funciona mejor en choppy que en
# tendencia?) y combustible (¿la racha con más volumen revierte más fuerte,
# más atrapados forzados a salir?). Solo LOGUEAN — mismo patrón que
# _libro_calidad: el pipeline causal (postmortem IC_bucket, N_BUCKET_MIN=15)
# descubre el corte cuando haya n suficiente, no se hardcodea ningún umbral.

def _regimen_ma_toques(activo, ctx, n_velas=15, periodo_ma=5):
    """Nº de cruces del precio sobre su propia media móvil en las últimas
    n_velas velas de 1min -- proxy barato de régimen: cerca de 0 = tendencia
    persistente (malo para reversión); muchos toques = choppy/lateral
    (bueno para reversión, hipótesis del artículo Spicy)."""
    klines = ctx.get("klines_raw", {}).get(activo, [])
    if len(klines) < n_velas + periodo_ma:
        return None
    try:
        closes = [float(k[4]) for k in klines[-(n_velas + periodo_ma):]]
    except (ValueError, TypeError, IndexError):
        return None
    toques = 0
    for i in range(periodo_ma, len(closes)):
        ma = sum(closes[i - periodo_ma:i]) / periodo_ma
        if (closes[i - 1] - ma) * (closes[i] - ma) < 0:
            toques += 1
    return toques


def _volumen_racha(activo, ctx, n_velas=15):
    """Volumen acumulado (klines 1min) en los minutos previos a la señal --
    proxy de 'combustible': racha con más volumen = más posiciones atrapadas
    que se ven forzadas a salir, reversión más fuerte."""
    klines = ctx.get("klines_raw", {}).get(activo, [])
    if len(klines) < n_velas:
        return None
    try:
        total = sum(float(k[5]) for k in klines[-n_velas:])
    except (ValueError, TypeError, IndexError):
        return None
    return round(total, 4)


def s_streak_fade_15m(market, ctx):
    q = market.get("question", "")
    if "up or down" not in q.lower():
        return None
    tipo, vent = _parse_updown_tipo(q)
    if tipo != "slot" or vent != 15:
        return None
    activo = identificar_activo(q)
    if activo not in STREAK_FADE_15M_PARES:
        return None
    py = market.get("_precio_yes")
    if py is None or not (STREAK_PY_LO <= py <= STREAK_PY_HI):
        return None
    edt = _streak_end_dt(market)
    if edt is None:
        return None
    k, d = _racha_actual(activo, 15, edt)
    if k < 4 or d is None:
        return None
    # reversión: FADEAR la racha. racha UP → esperamos DOWN → prob_yes bajo, y viceversa
    prob_yes = 0.30 if d == "YES" else 0.70
    return {
        "prob_yes": prob_yes,
        "razon":    f"streak_fade_15m {activo} racha={k}x{d} py={py:.3f} (reversión)",
        "subtype":  f"{activo}#15min",
        "features": {
            "streak_len":    k,
            "streak_dir_up": 1 if d == "YES" else 0,
            "py_entrada":    round(py, 3),
            "hora_utc":      datetime.now(timezone.utc).hour,
            "regimen_ma_toques": _regimen_ma_toques(activo, ctx),
            "volumen_racha":     _volumen_racha(activo, ctx),
            # 13-Jul (retomando idea_racha_correlacion... no, ver
            # project_volumen_racha_signo_contrario_13jul): volumen_racha
            # (15min) salió con signo CONTRARIO a la hipótesis de origen
            # (Spicy: volumen en el EXTREMO del spike, no acumulado en
            # toda la racha). No se puede reconstruir retroactivo -- el
            # caché de klines solo guarda ~25 velas por ciclo, sin
            # histórico minuto-a-minuto del pasado. Se loguea AHORA una
            # ventana corta (3min, más fiel a "el extremo") en paralelo a
            # la de 15min, puramente observacional, para comparar signo
            # cuando acumule n. No sustituye volumen_racha, no toca dec.
            "volumen_racha_corto": _volumen_racha(activo, ctx, n_velas=3),
            **_libro_calidad(market),
        },
    }


# ── LEADLAG_BTC_XRP_15M — order flow propio de BTC -> outcome de XRP misma ventana ──
# Hallazgo 2026-07-09 (fills reales Jon-Becker, luego validado contra la API real
# de Polymarket con timestamps reales): el momentum temprano del propio mercado
# BTC#15min (primeros ~3min de vida de la ventana) correlaciona con el outcome de
# XRP en la MISMA ventana de 15min. No es "spot BTC lidera precio" (esa premisa ya
# se refutó, ver idea_lead_lag_refutado) — es order flow/posicionamiento propio de
# Polymarket. BTC->XRP fue el ÚNICO par que sobrevivió el control split-half
# cronológico (z=2.4-2.8 en ambas mitades, n~400/mitad); BTC->ETH/SOL NO son
# estables (se desinflan a la mitad más reciente) y NO se implementan aquí.
# prob_yes fijo por signo (no escalado por magnitud: sin calibración forward
# todavía) — el pipeline causal existente (postmortem IC_bucket, N_BUCKET_MIN=15)
# descubrirá si hace falta un umbral de magnitud sobre btc_momentum, igual que
# con libro_spread/liquidez en STRUCT_NO/STREAK. Shadow puro: NO está en
# pares_permitidos_live → jamás opera en vivo. Ver idea_leadlag_btc_xrp_revive_parcial.
LEADLAG_STATE_PATH = DIR_SHADOW / "leadlag_btc_state.json"
LEADLAG_MIN_MUESTRAS = 3
LEADLAG_VENTANA_MIN = 3.0  # minutos desde apertura de la ventana BTC a muestrear


def _actualizar_leadlag_btc_state(operables):
    """Acumula precio_yes de BTC#15min en los primeros minutos de cada ventana,
    para que s_leadlag_btc_xrp lea el momentum temprano al evaluar XRP de la
    MISMA ventana. Solo logging -- nunca lanza, nunca bloquea el ciclo."""
    try:
        estado = json.loads(LEADLAG_STATE_PATH.read_text()) if LEADLAG_STATE_PATH.exists() else {}
    except Exception:
        estado = {}
    ahora = datetime.now(timezone.utc)
    tocado = False
    for m in operables:
        q = m.get("question", "")
        if "up or down" not in q.lower():
            continue
        tipo, vent = _parse_updown_tipo(q)
        if tipo != "slot" or vent != 15 or identificar_activo(q) != "BTC":
            continue
        end_date = m.get("end_date", "")
        if not end_date:
            continue
        try:
            end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
            if end_dt.tzinfo is None:
                end_dt = end_dt.replace(tzinfo=timezone.utc)
        except Exception:
            continue
        restante_min = (end_dt - ahora).total_seconds() / 60.0
        elapsed_min = 15.0 - restante_min
        if not (0 <= elapsed_min <= LEADLAG_VENTANA_MIN):
            continue
        estado.setdefault(end_date, []).append({"t": ahora.timestamp(), "py": m["_precio_yes"]})
        tocado = True
    if tocado:
        corte = ahora.timestamp() - 7200  # poda: ventanas de las últimas 2h
        estado = {k: v for k, v in estado.items() if v and v[-1]["t"] >= corte}
        try:
            LEADLAG_STATE_PATH.write_text(json.dumps(estado))
        except Exception:
            pass


def s_leadlag_btc_xrp(market, ctx):
    q = market.get("question", "")
    if "up or down" not in q.lower():
        return None
    tipo, vent = _parse_updown_tipo(q)
    if tipo != "slot" or vent != 15 or identificar_activo(q) != "XRP":
        return None
    end_date = market.get("end_date", "")
    if not end_date:
        return None
    try:
        estado = json.loads(LEADLAG_STATE_PATH.read_text()) if LEADLAG_STATE_PATH.exists() else {}
    except Exception:
        return None
    muestras = estado.get(end_date)
    if not muestras or len(muestras) < LEADLAG_MIN_MUESTRAS:
        return None
    precios = [x["py"] for x in muestras]
    btc_momentum = precios[-1] - precios[0]
    prob_yes = 0.53 if btc_momentum > 0 else (0.47 if btc_momentum < 0 else 0.50)
    return {
        "prob_yes": prob_yes,
        "razon":    f"leadlag_btc_xrp btc_momentum={btc_momentum:+.4f} n_muestras={len(precios)}",
        "subtype":  "XRP#15min",
        "features": {
            "btc_momentum":   round(btc_momentum, 5),
            "n_muestras_btc": len(precios),
            "py_entrada":     round(market.get("_precio_yes", 0), 3),
            "hora_utc":       datetime.now(timezone.utc).hour,
            **_libro_calidad(market),
        },
    }


ESTRATEGIAS = [
    ("WEEKLY_PRICE",        s_weekly_price),
    ("PRICE_MOMENTUM",      s_price_momentum),
    ("SMART_FLOW_1H",       s_smart_flow_1h),
    ("UPDOWN_GBM",          s_updown_gbm),
    ("UPDOWN_OU_5M",        s_updown_ou_5m),
    ("PRICE_TARGET_GBM",    s_price_target_gbm),
    ("ORDER_FLOW_5M",       s_order_flow_5m),
    ("RESOLUTION_SNIPER",   s_resolution_sniper),
    ("LATE_WINDOW_5MIN",    s_late_window_5min),
    ("GBM_LATE_15M",        s_gbm_late_15min),
    ("GBM_LATE_15M_TARDIO", s_gbm_late_15min_tardio),
    ("GBM_LATE_15M_ESPACIO_ATR", s_gbm_late_15min_espacio_atr),
    ("GBM_LATE_15M_PYCONFIRMADO", s_gbm_late_15min_py_confirmado),
    ("GBM_LATE_5M",         s_gbm_late_5min),
    ("GBM_LATE_60M",        s_gbm_late_60min),
    ("STRUCT_NO_15M",       s_struct_no_15m),
    ("FAVORITO_CONFIRMADO", s_favorito_confirmado),
    ("STREAK_MOM_5M",       s_streak_mom_5m),
    ("STREAK_FADE_5M",      s_streak_fade_5m),
    ("STREAK_FADE_15M",     s_streak_fade_15m),
    ("LEADLAG_BTC_XRP_15M", s_leadlag_btc_xrp),
    # ("BINANCE_UPDOWN", s_binance_updown),  # retirada — IC -0.50
]

# ── Boost horario de stake: UNA fuente de verdad (P15, colapsado 2026-07-10) ──
# Antes convivían dos multiplicadores horarios sobre `apuesta` que se apilaban:
# (a) set 24H hardcoded ×1.1 y (b) meta.hora_boost_factor. Ahora se aplican una
# sola vez aquí, con prioridad al dato aprendido (H-KELLY-HORA). h18 quitada del
# fallback (dud: EV +0.066 dentro de un set que promedia +0.38 en GBM_LATE_15M;
# coincide con analisis_hora_boost n=1996, h18=-0.011). El bucket causal sobre
# hora_utc (causal_boost) sigue siendo una capa ADITIVA separada — al des-pinear
# max_stake, decidir si excluir hora del causal para tener literalmente 1 fuente.
HORA_BOOST_15M_BUYYES = frozenset({5, 6, 7, 15, 16, 17, 19})


def _hora_stake_factor(dec: str, subtype: str, meta: dict) -> float:
    """Multiplicador de stake por hora, aplicado UNA sola vez. meta.hora_boost_factor
    (dato aprendido) manda si define la hora actual; si no, fallback estático ×1.1
    para BUY_YES#15min en las horas históricamente buenas."""
    if dec not in ("BUY_YES", "BUY_NO"):
        return 1.0
    h = datetime.now(timezone.utc).hour
    meta_map = (meta or {}).get("hora_boost_factor", {}) or {}
    if str(h) in meta_map:
        try:
            return float(meta_map[str(h)])
        except (TypeError, ValueError):
            return 1.0
    if dec == "BUY_YES" and subtype.endswith("15min") and h in HORA_BOOST_15M_BUYYES:
        return 1.1
    return 1.0


def main():
    global SLIPPAGE_ESTIMADO
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Shadow predict v8 ===")
    slip_din = _slippage_estimado_dinamico()
    if slip_din != SLIPPAGE_ESTIMADO:
        print(f"  SLIPPAGE_ESTIMADO recalibrado con slip_real live: 0.02 → {slip_din}")
        SLIPPAGE_ESTIMADO = slip_din
    mercados = cargar_mercados_recientes()
    print(f"  Mercados snapshot reciente: {len(mercados)}")

    # Enriquecer con slots frescos obtenidos directamente de la API
    # Garantiza cobertura de slots 5min/15min independientemente del slow loop
    ids_conocidos = {m.get("market_id", "") for m in mercados}
    frescos_5m  = fetch_slots_directos(horizonte_min=5,  ventanas_adelante=2)
    frescos_15m = fetch_slots_directos(horizonte_min=15, ventanas_adelante=1)
    nuevos_frescos = [m for m in frescos_5m + frescos_15m
                      if m.get("market_id", "") not in ids_conocidos and m.get("market_id", "")]
    if nuevos_frescos:
        mercados = mercados + nuevos_frescos
        print(f"  + {len(nuevos_frescos)} slots frescos (5/15min) de API directa")

    operables = []
    for m in mercados:
        h = horas_a_vencimiento(m.get("end_date", ""))
        if h is None or h > HORIZONTE_MAX_HORAS:
            continue
        if h < HORIZONTE_MIN_HORAS:
            # Zona late-window: mercados Up-or-Down a 30s-3min de expirar.
            # El suelo general de 3min dejaba a LATE_WINDOW_5MIN sin un solo
            # mercado elegible (su zona de entrada 160-270s de una ventana de
            # 5min deja 30-140s restantes) — 0 predicciones desde su creación,
            # detectado 2026-07-02. Estos mercados pasan marcados y SOLO los
            # evalúa LATE_WINDOW_5MIN (ver check _solo_late en el bucle).
            if h < 0.008 or "up or down" not in (m.get("question") or "").lower():
                continue
            m["_solo_late"] = True
        try:
            py = float(m.get("price_yes", ""))
        except (ValueError, TypeError):
            continue
        if not (0.01 < py < 0.99):
            continue
        m["_horas"]      = h
        m["_precio_yes"] = py
        try:
            m["_spread"] = float(m.get("spread", "") or 0)
        except (ValueError, TypeError):
            m["_spread"] = 0.0
        operables.append(m)
    print(f"  Mercados operables ({HORIZONTE_MIN_HORAS}-{HORIZONTE_MAX_HORAS}h): {len(operables)}")
    if not operables:
        print("  Nada que predecir.")
        return
    try:
        _actualizar_leadlag_btc_state(operables)
    except Exception as e:
        print(f"  Aviso leadlag_btc_state: {e}")

    # Lookup precio_yes por (activo, ventana) — feature de spread entre
    # ventanas relacionadas del mismo activo (H-CUSTOM-CROSS-WINDOW-SPREAD).
    # Solo observación: no cambia ninguna decisión de predicción existente.
    _precios_ventanas_acc = {}
    for _m in operables:
        _tipo_m, _ventana_m = _parse_updown_tipo(_m.get("question", ""))
        if _tipo_m is None:
            continue
        _activo_m = identificar_activo(_m.get("question", ""))
        if not _activo_m:
            continue
        _clave = _ventana_m if _tipo_m == 'slot' else (60 if _tipo_m == 'hourly' else 'daily')
        _precios_ventanas_acc.setdefault((_activo_m, _clave), []).append(_m["_precio_yes"])
    precios_ventanas_hoy = {k: sum(v) / len(v) for k, v in _precios_ventanas_acc.items()}
    _moon_phase_hoy = _moon_phase(datetime.now(timezone.utc))
    _mercury_retro_hoy = _mercurio_retrogrado(datetime.now(timezone.utc))
    _horas_hasta_fomc_hoy = _horas_hasta_fomc(datetime.now(timezone.utc))
    try:
        _smart_money_consenso = json.loads(
            (DIR_SHADOW / "smart_money_consensus.json").read_text(encoding="utf-8")
        )
    except Exception:
        _smart_money_consenso = {}

    # Fail-safe (12-Jul, aprobado Javi, code-review sobre FEATURE_RULES de
    # GBM_LATE_15M): un filtro_causal recién descubierto (aprender_patrones_
    # causales, shadow_postmortem.py) NUNCA debe poder saltar en silencio
    # una señal de un par que YA está en pares_permitidos_live (dinero
    # real) — se trata como "candidato", igual que cualquier otra promoción
    # de whitelist, y no se auto-aplica sin revisión humana explícita.
    # _pares_live_hoy=None (lectura falló: JSON corrupto, fichero ausente,
    # etc.) es el estado MÁS seguro posible: _es_par_live_protegido()
    # entonces asume "no puedo confirmar que NO sea live" y NO aplica el
    # filtro — el error inverso (asumir "no es live" y dejar que el filtro
    # salte una señal real) es exactamente el fallo que este guardia existe
    # para prevenir, así que nunca se toma ese camino.
    try:
        _pares_live_hoy = set(
            json.loads((DIR_LIVE / "config_live.json").read_text(encoding="utf-8"))
            .get("pares_permitidos_live", [])
        )
    except Exception:
        _pares_live_hoy = None

    def _es_par_live_protegido(nombre_estr: str, sub: str, direccion: str) -> bool:
        if _pares_live_hoy is None:
            return True
        return f"{nombre_estr}#{sub}#{direccion}" in _pares_live_hoy

    ctx = construir_contexto()
    ctx["precios_ventanas_hoy"] = precios_ventanas_hoy
    params_din = _cargar_params_dinamicos()
    meta_params = _cargar_meta_params()
    ctx["meta_params"] = meta_params
    if params_din:
        activas = {k for k, v in params_din.items() if not v.get("activa", True)}
        print(f"  Params dinámicos cargados: {len(params_din)} estrategias, desactivadas: {activas or 'ninguna'}")
    if meta_params:
        auto_hours = meta_params.get("gbm_blacklist_hours_auto", [])
        hora_boost = meta_params.get("hora_boost_factor", {})
        if auto_hours:
            print(f"  Meta auto-params: GBM_BLACKLIST_HOURS_AUTO={set(auto_hours)}")
        if hora_boost:
            print(f"  Meta auto-params: HORA_BOOST={hora_boost}")
    fecha   = ts[:10]
    archivo = DIR_SHADOW / f"predictions_{fecha}.csv"
    nuevo   = not archivo.exists()
    ya_predichos = set()
    if not nuevo:
        try:
            with open(archivo, encoding="utf-8") as f_exist:
                for row in csv.DictReader(f_exist):
                    ya_predichos.add((row.get("strategy", ""), row.get("market_id", "")))
        except Exception as e:
            print(f"  Aviso leyendo predicciones existentes: {e}")
    print(f"  Pares (strategy,market_id) ya predichos hoy: {len(ya_predichos)}")
    total, ops, skipped_dup, skipped_extremo = 0, 0, 0, 0
    contador = {nombre: {"aplica": 0, "operable": 0} for nombre, _ in ESTRATEGIAS}
    # Conexión "correlación de ventana" (13-Jul, idea_racha_correlacion_ventana):
    # (end_date, dirección) -> {activos que ya dispararon GBM_LATE_15M/familia
    # esta ventana}. Se rellena según se procesan los mercados de este ciclo
    # (orden de llegada real, no retrospectivo) — puramente observacional.
    _ventana_activos_gbmlate = {}
    with open(archivo, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo:
            w.writerow([
                "timestamp_utc", "strategy", "market_id", "question", "end_date",
                "horas_a_vencimiento", "precio_yes_mercado", "prob_yes_modelo",
                "edge_bruto", "edge_neto", "edge_direccional", "decision", "razon", "subtype",
                "apuesta", "features",
            ])
        for m in operables:
            market_rows = []  # buffer para Kelly compuesto
            py  = m["_precio_yes"]
            mid = m.get("market_id", "")
            for nombre, func in ESTRATEGIAS:
                if m.get("_solo_late") and nombre != "LATE_WINDOW_5MIN":
                    continue
                if (nombre, mid) in ya_predichos:
                    skipped_dup += 1
                    continue
                try:
                    pred = func(m, ctx)
                except Exception as e:
                    print(f"  Exc {nombre}/{mid}: {type(e).__name__}: {e}")
                    continue
                if pred is None:
                    continue
                # Edge mínimo y activa: lookup de más específico a más general
                subtype = pred.get("subtype", "")
                if "#" in subtype:
                    a_part, d_part = subtype.split("#", 1)
                    lookup_keys = [
                        f"{nombre}#{subtype}",   # UPDOWN_GBM#BTC#15min
                        f"{nombre}#{a_part}",    # UPDOWN_GBM#BTC
                        f"{nombre}#{d_part}",    # UPDOWN_GBM#15min
                        nombre,
                    ]
                elif subtype:
                    lookup_keys = [f"{nombre}#{subtype}", nombre]
                else:
                    lookup_keys = [nombre]
                sp = next((params_din[k] for k in lookup_keys if k in params_din), {})
                # Si CUALQUIER clave de la jerarquía está desactivada → saltar
                # (evita que BTC#240min quede activo cuando #240min está desactivado).
                # Excepción: estrategias shadow-puras en ACUMULAR_SHADOW_AUNQUE_DESACTIVADA
                # siguen generando para romper el estado absorbente (nunca en whitelist live).
                # Direction-aware (auditoría 15-Jul, mismo fix que live_trade.py::_tupla_activa):
                # 'activa' por nivel es el IC MIXTO (BUY_YES+BUY_NO); sin esto, un BUY_NO
                # shadow hundido podía apagar la GENERACIÓN de un BUY_YES sano — más grave
                # que el veto de live_trade.py, porque ni siquiera llega una fila que vetar.
                # Si existe el campo direction-aware activa_{decision} se usa ese; si no
                # (dato pre-deploy u otra dirección sin volumen), cae al 'activa' mixto.
                _dec_gate = pred.get("decision", "")
                _campo_dir_gate = f"activa_{_dec_gate}" if _dec_gate else None
                def _nivel_bloqueado(k, _cd=_campo_dir_gate):
                    e = params_din.get(k, {})
                    if _cd and _cd in e:
                        return not e[_cd]
                    return not e.get("activa", True)
                if (any(_nivel_bloqueado(k) for k in lookup_keys if k in params_din)
                        and nombre not in ACUMULAR_SHADOW_AUNQUE_DESACTIVADA):
                    continue
                edge_min = sp.get("edge_minimo") or EDGE_MINIMO
                # Apuesta Kelly: escala con IC confirmado, mínimo 0.50€ si activa
                apuesta = sp.get("apuesta_kelly", 0.50) or 0.50
                # Aprendizaje causal: filtros (evitar) + patrones ganadores (amplificar)
                pred_features = pred.get("features", {}) or {}
                # Calendario astronómico observacional (moon_phase, mercury_retrogrado) —
                # no afecta ninguna decisión, solo se acumula para análisis futuro
                pred_features["moon_phase"] = _moon_phase_hoy
                pred_features["mercury_retrogrado"] = 1 if _mercury_retro_hoy else 0
                pred_features["horas_hasta_fomc"] = _horas_hasta_fomc_hoy
                _activo_pred = subtype.split("#", 1)[0].upper() if subtype else ""
                _consenso_activo = _smart_money_consenso.get(_activo_pred)
                if _consenso_activo:
                    pred_features["smart_money_consensus"] = _consenso_activo.get("smart_money_consensus")
                    pred_features["smart_money_n_wallets"] = _consenso_activo.get("n_wallets_smart")
                    # P16 (12-Jul): consenso ponderado por tamaño de apuesta relativo a
                    # la mediana propia de cada wallet — observacional, NO sustituye al
                    # plano hasta n≥40 forward (ver CLAUDE.md P16 y smart_money_tracker.py)
                    if "smart_money_consensus_ponderado" in _consenso_activo:
                        pred_features["smart_money_consensus_ponderado"] = _consenso_activo.get("smart_money_consensus_ponderado")
                        pred_features["smart_money_n_wallets_ponderado"] = _consenso_activo.get("n_wallets_smart_ponderado")
                pred["features"] = pred_features

                def _feature_match(feat_val, cond, umbral):
                    # Estricto en los 4 casos: coincide con el límite "malo" tal
                    # como lo define _evaluar_bucket() en shadow_postmortem.py
                    # (malo siempre estricto, bueno siempre inclusive). Antes
                    # "abs_lt"/"lt" usaban <= y colaban el valor umbral —que
                    # _evaluar_bucket había clasificado como "bueno"— dentro de
                    # filtros_causales, descartando operaciones rentables reales
                    # (ej. hora_utc=11 en BTC#15min, confirmado en producción).
                    try:
                        v, u = float(feat_val), float(umbral)
                        if cond == "abs_gt":  return abs(v) > u
                        if cond == "abs_lt":  return abs(v) < u
                        if cond == "gt":      return v > u
                        if cond == "lt":      return v < u
                    except (TypeError, ValueError):
                        pass
                    return False

                contador[nombre]["aplica"] += 1
                prob_y_raw = pred["prob_yes"]
                prob_y = prob_y_raw
                # Recalibración Platt (a,b) aprendida por postmortem sobre el histórico
                # agregado de la estrategia — solo se activa cuando el holdout OOS confirma
                # mejora significativa (walk-forward 2026-07-01: prob_yes_modelo crudo
                # estaba sobreconfiado, ver calibracion_prob en strategy_params.json).
                # Se persiste prob_y_raw (no el calibrado) en la columna
                # prob_yes_modelo: postmortem reentrena (a,b) leyendo esa misma
                # columna asumiendo que es la probabilidad cruda del modelo —
                # si se guardara ya calibrada, cada reentreno calibraría sobre
                # su propia calibración anterior en vez de sobre la señal
                # original (deriva compuesta, detectado 2026-07-01).
                calib = params_din.get(nombre, {}).get("calibracion_prob")
                if calib:
                    prob_y = _norm_cdf(calib["a"] + calib["b"] * _norm_ppf(prob_y_raw))
                eb = prob_y - py
                en = eb - SLIPPAGE_ESTIMADO if eb > 0 else eb + SLIPPAGE_ESTIMADO
                precio_extremo = (en >= edge_min and py < 0.10) or (-en >= edge_min and py > 0.90)
                if precio_extremo:
                    skipped_extremo += 1
                if en >= edge_min and not precio_extremo:
                    dec = "BUY_YES"
                elif -en >= edge_min and not precio_extremo:
                    dec = "BUY_NO"
                else:
                    dec = "SKIP"
                # PRICE_TARGET#atexpiry BUY_YES: IC=-0.267 (n=16) — el modelo GBM
                # sobreestima P(precio_above_K) consistentemente; BUY_NO es la única
                # dirección con IC positivo (+0.059). Filtro estructural por dirección.
                if (nombre == "PRICE_TARGET_GBM" and "atexpiry" in subtype
                        and dec == "BUY_YES"):
                    dec = "SKIP"

                # WEEKLY_PRICE BUY_YES con in_range=1 (13-Jul, H-CUSTOM-WEEKLY-
                # INRANGE-BUYYES confirmada con n=35, IC=-0.257 < umbral -0.10):
                # acertar que el spot YA está dentro del rango estrecho al
                # vencimiento es intrínsecamente poco probable y el mercado
                # sobrevalora el "sí" en ese caso. Shadow-only (WEEKLY_PRICE no
                # está en pares_permitidos_live), sin riesgo de dinero real.
                if nombre == "WEEKLY_PRICE" and dec == "BUY_YES":
                    if pred_features.get("in_range") == 1:
                        dec = "SKIP"

                # GBM_LATE_15M#ETH#15min BUY_YES: promoción manual explícita
                # (13-Jul, aprobado Javi) del filtro_causal descubierto por
                # postmortem sobre par live-protegido (ver _es_par_live_protegido
                # abajo, que por diseño NUNCA lo aplica solo). sigma_ewma_delta_pct
                # < 4.947 → IC=-0.157 n=33 (malo) vs IC=+0.239 n=21 (bueno).
                # Verificado antes de promocionar: permutación 20k shuffles
                # p=0.0026; estable en split temporal (primera mitad 35.7%/76.9%
                # hit, segunda mitad 31.6%/75.0% hit — mismo gap en ambas mitades);
                # patrón coherente cross-asset en los 4 pares (BTC/SOL/XRP/ETH,
                # mismo signo: sigma bajo→peor, sigma alto→mejor) y ya aplicado
                # automáticamente en BTC (umbral 6.604) porque BTC no está en
                # pares_permitidos_live. Mecanismo: GBM_LATE_15M apuesta a
                # continuación direccional — con volatilidad plana/cayendo el
                # precio tiende a no moverse y la apuesta falla más.
                # Caveat: feature nuevo, solo ~30h de historia (desde 12-Jul
                # 07:50 UTC) — no hay validación out-of-time de varios días.
                # Revisar de nuevo con más n/días; no ampliar a otros pares sin
                # repetir esta misma verificación.
                if nombre == "GBM_LATE_15M" and subtype == "ETH#15min" and dec == "BUY_YES":
                    _sigma_eth = pred_features.get("sigma_ewma_delta_pct")
                    if _sigma_eth is not None:
                        try:
                            if float(_sigma_eth) < 4.947:
                                dec = "SKIP"
                        except (TypeError, ValueError):
                            pass

                # 1. Filtros causales — direccionales (BUY_YES/BUY_NO), se
                # evalúan aquí (ya se conoce `dec`) para exigir que el filtro
                # coincida con la dirección real. Antes se evaluaban sin
                # conocer la dirección, mezclando el aprendizaje de BUY_YES y
                # BUY_NO en el mismo bucket causal.
                if dec in ("BUY_YES", "BUY_NO"):
                    skip_causal = False
                    filtro_matched = None
                    for lk in lookup_keys:
                        for f in params_din.get(lk, {}).get("filtros_causales", []):
                            if f.get("direccion") not in (None, dec):
                                continue
                            fv = pred_features.get(f.get("feature"))
                            if fv is not None and _feature_match(fv, f.get("condicion",""), f.get("umbral",999)):
                                skip_causal = True
                                filtro_matched = (lk, f)
                                break
                        if skip_causal:
                            break
                    if skip_causal:
                        if _es_par_live_protegido(nombre, subtype, dec):
                            # Ver nota fail-safe arriba (_es_par_live_protegido):
                            # este par YA es dinero real hoy — un filtro recién
                            # descubierto no lo salta solo, requiere promoción
                            # explícita. Se loguea fuerte para que no pase
                            # desapercibido (vigia_filtro_gbmlate.py también lo
                            # detecta vía strategy_params.json).
                            print(f"  ⚠️ filtro_causal matcheó en PAR LIVE "
                                  f"{nombre}#{subtype}#{dec} pero se IGNORA "
                                  f"(fail-safe, requiere promoción manual): "
                                  f"{filtro_matched}")
                        else:
                            dec = "SKIP"

                # 2. Patrones ganadores — direccionales, y se toma el de mayor
                # ic_patron entre los que matchean (no se suman): sumar boosts
                # de features/niveles de jerarquía solapados (ej. mismo
                # subconjunto de filas contado dos veces bajo
                # "UPDOWN_GBM#SOL#15min" y el agregado "UPDOWN_GBM#15min")
                # inflaba el stake muy por encima de lo que la evidencia real
                # sostiene (confirmado 2026-07-01, dos patrones con n_patron
                # e ic_patron idénticos sumándose como si fueran señales
                # independientes). Guardado en variable aparte para que
                # sobreviva al override del Kelly por dirección de abajo.
                causal_boost = 0.0
                if dec in ("BUY_YES", "BUY_NO"):
                    # Fail-safe (13-Jul): mismo criterio que ya existe para
                    # filtros_causales (ver _es_par_live_protegido arriba) —
                    # un patron_ganador recién descubierto por postmortem
                    # tampoco puede subir el stake en un par YA live sin
                    # promoción manual explícita. Antes esta rama no tenía
                    # ningún guardia (asimetría real: el filtro que SALTA una
                    # señal live sí lo tenía desde el episodio GBM_LATE_15M
                    # de FEATURE_RULES, el que SUBE el stake no). Impacto real
                    # detectado al auditar: cero hasta hoy porque max_stake_eur
                    # está pineado por debajo de donde llegaría el boost, pero
                    # es el mismo tipo de gap que P15 (boosts horarios sin
                    # gatear) — se cierra ahora que no cuesta nada, no cuando
                    # ya esté despineado.
                    _par_protegido_boost = _es_par_live_protegido(nombre, subtype, dec)
                    mejor_ic_patron = None
                    _bloqueados_boost = []
                    for lk in lookup_keys:
                        for g in params_din.get(lk, {}).get("patrones_ganadores", []):
                            if g.get("direccion") not in (None, dec):
                                continue
                            fv = pred_features.get(g.get("feature"))
                            if fv is not None and _feature_match(fv, g.get("condicion",""), g.get("umbral",999)):
                                if _par_protegido_boost:
                                    _bloqueados_boost.append(
                                        f"{lk}:{g.get('feature')} {g.get('condicion')} "
                                        f"{g.get('umbral')} kelly_boost={g.get('kelly_boost')}")
                                    continue
                                ic_g = float(g.get("ic_patron", 0))
                                if mejor_ic_patron is None or ic_g > mejor_ic_patron:
                                    mejor_ic_patron = ic_g
                                    causal_boost = float(g.get("kelly_boost", 0))
                    # Un solo aviso consolidado por predicción (no uno por cada
                    # patron_ganador que matchea) — evita inundar logs/fast.log
                    # cuando varios niveles de jerarquía matchean a la vez.
                    if _bloqueados_boost:
                        print(f"  ⚠️ patron_ganador matcheó en PAR LIVE "
                              f"{nombre}#{subtype}#{dec} pero se IGNORA "
                              f"(fail-safe, requiere promoción manual): "
                              f"{'; '.join(_bloqueados_boost)}")
                    if causal_boost > 0:
                        apuesta = min(2.00, apuesta + causal_boost)

                # Kelly por dirección: usar el IC específico como base, luego sumar
                # el boost causal encima (no reemplazarlo). Evita overstakear BUY_YES.
                if dec in ("BUY_YES", "BUY_NO"):
                    dir_stake = sp.get(f"apuesta_kelly_{dec}")
                    if dir_stake is not None:
                        apuesta = max(0.50, min(2.00, float(dir_stake) + causal_boost))
                # Boost horario de stake — UNA sola fuente de verdad (P15, 10-Jul):
                # antes el set 24H hardcoded ×1.1 (abajo, ya eliminado) y
                # meta.hora_boost_factor se aplicaban por separado y se apilaban
                # multiplicativamente. Ahora un único factor, meta con prioridad.
                apuesta = min(2.00, apuesta * _hora_stake_factor(dec, subtype, meta_params))
                # Longshot bias (Jon-Becker, 2026-06-27): mercados con py_mkt<0.20 tienen
                # win_rate<precio_implícito para compradores de YES (EV negativo en longshots).
                # BUY_NO en estos mercados tiene edge estructural adicional → boost ×1.1.
                if dec == "BUY_NO" and py < 0.20:
                    apuesta = min(2.00, apuesta * 1.1)
                # YES/NO flow interno Polymarket (poly_drift_5obs, 2026-06-27):
                # Si el precio YES en Polymarket lleva bajando (poly_drift<0) y predecimos
                # BUY_NO → señal interna confirma la nuestra → boost ×1.1.
                # Si el precio lleva subiendo y predecimos BUY_YES → boost ×1.1.
                # Si hay divergencia → reducir apuesta ×0.85 (mercado interno dice otra cosa).
                poly_d = pred.get("features", {}).get("poly_drift_5obs") if isinstance(pred.get("features"), dict) else None
                if poly_d is not None and abs(poly_d) > 0.5:  # solo si hay movimiento real (>0.5%)
                    if (dec == "BUY_NO" and poly_d < 0) or (dec == "BUY_YES" and poly_d > 0):
                        apuesta = min(2.00, apuesta * 1.1)   # confluencia: poly + nuestro signal
                    elif (dec == "BUY_NO" and poly_d > 1.5) or (dec == "BUY_YES" and poly_d < -1.5):
                        apuesta = max(0.50, apuesta * 0.85)  # divergencia fuerte → cautela
                # H-CUSTOM-ETH15-REVERSION (confirmada 2026-07-01, IC=+0.155 n=27):
                # ETH#15min con drift_15min<-1%/h (caída fuerte reciente) tiene mean-reversion
                # → BUY_YES contra la caída. A diferencia de BTC (momentum, filtro arriba),
                # ETH reacciona por reversión. Boost ×1.1.
                drift_15_val = pred_features.get("drift_15min")
                if (dec == "BUY_YES" and subtype == "ETH#15min" and drift_15_val is not None
                        and float(drift_15_val) < -1.0):
                    apuesta = min(2.00, apuesta * 1.1)
                ed = en if dec != "BUY_NO" else -en
                if dec != "SKIP":
                    ops += 1
                    ya_predichos.add((nombre, mid))
                # Conexión "correlación de ventana" (ver init de
                # _ventana_activos_gbmlate arriba): cuántos OTROS activos ya
                # dispararon la misma dirección en esta ventana antes que yo,
                # este ciclo. idea_racha_correlacion_ventana ya tenía evidencia
                # fuerte (n=238, dependencia de cola 3-5x) de que pares
                # correlacionados en la misma ventana explican los disparos
                # del freno=4 mejor que "régimen de mercado" (refutado hoy en
                # analisis_regimen_sesion.py) — esto lo mide en vivo, trade a
                # trade, en vez de solo retrospectivo.
                if nombre in GBM_LATE_FAMILIA and dec in ("BUY_YES", "BUY_NO"):
                    _activo_actual = subtype.split("#", 1)[0] if "#" in subtype else ""
                    _vkey = (m.get("end_date", ""), dec)
                    _previos = _ventana_activos_gbmlate.setdefault(_vkey, set())
                    pred_features["ventana_activos_previos_mismo_signo"] = len(_previos - {_activo_actual})
                    _previos.add(_activo_actual)
                features_json = json.dumps(pred.get("features", {}), separators=(",", ":"))
                market_rows.append([
                    ts, nombre, mid,
                    m.get("question", ""), m.get("end_date", ""),
                    f"{m['_horas']:.2f}", f"{py:.4f}", f"{prob_y_raw:.4f}",
                    f"{eb:.4f}", f"{en:.4f}", f"{ed:.4f}", dec,
                    pred.get("razon", ""), subtype,
                    f"{apuesta:.2f}", features_json,
                ])

            # Kelly compuesto: boost si UPDOWN_GBM y ORDER_FLOW_5M coinciden
            market_rows = _aplicar_kelly_compuesto(market_rows)
            # Wang Transform (FAVORITO_CONFIRMADO) + confirmación cruzada
            # FAVORITO_CONFIRMADO<->familia GBM_LATE_15M — solo observacional
            market_rows = _inyectar_features_cruzadas(market_rows)

            for row in market_rows:
                if row[11] != "SKIP":
                    contador[row[1]]["operable"] += 1
                w.writerow(row)
                total += 1

    print(f"  Predicciones registradas: {total} (operables: {ops}, dup saltados: {skipped_dup}, extremo filtrado: {skipped_extremo})")
    print("  Desglose por estrategia (aplica / operable):")
    for nombre, c in contador.items():
        print(f"    {nombre:20s}  {c['aplica']:>4} / {c['operable']:>4}")
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] === Fin ===")

if __name__ == "__main__":
    main()

