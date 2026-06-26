"""
shadow_predict.py — v8. Cuatro estrategias activas:
  1. PRICE_MOMENTUM — tendencia exponencial del precio YES en historial de mercados
  2. SMART_FLOW_1H  — flujo de compras recientes (ultimo 1h, wallets humanas)
  3. UPDOWN_GBM     — mercados Up/Down via modelo Black-Scholes digital (daily/hourly/slot)
  4. WEEKLY_PRICE   — mercados de rango de precio semanal (BTC/ETH/SOL entre $X-$Y)
"""
import csv, glob, json, math, os, pickle, re, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
import requests

TIMEOUT = 30
HORIZONTE_MIN_HORAS = 0.05    # 3 min: cubre mercados Up/Down 5m
HORIZONTE_MAX_HORAS = 365 * 24  # 1 anno
EDGE_MINIMO = 0.02
SLIPPAGE_ESTIMADO = 0.02
MIN_LIQUIDEZ = 500

DIR_DATA    = Path("data")
DIR_SHADOW  = DIR_DATA / "shadow"

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
    fecha_hoy  = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    fecha_ayer = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    archivos   = [DIR_MARKETS / f"{fecha_hoy}.csv", DIR_MARKETS / f"{fecha_ayer}.csv"]
    fuentes    = [str(a) for a in archivos if Path(a).exists()]

    cache_file = _cache_path("mercados_recientes")
    if _cache_valida(cache_file, fuentes):
        with open(cache_file, "rb") as f:
            return pickle.load(f)

    por_id = {}
    for arch in archivos:
        if not Path(arch).exists():
            continue
        with open(arch, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                mid = row.get("market_id")
                if not mid:
                    continue
                ts = row.get("timestamp_utc", "")
                if mid not in por_id or ts > por_id[mid]["timestamp_utc"]:
                    por_id[mid] = row
    resultado = list(por_id.values())
    with open(cache_file, "wb") as f:
        pickle.dump(resultado, f)
    return resultado


def cargar_historial_mercados():
    corte    = datetime.now(timezone.utc) - timedelta(hours=6)
    archivos = sorted(glob.glob(str(DIR_MARKETS / "*.csv")))[-3:]
    fuentes  = [a for a in archivos if Path(a).exists()]

    cache_file = _cache_path("historial_mercados")
    if _cache_valida(cache_file, fuentes, ttl_s=90):  # 90s: el historial cambia más rápido
        with open(cache_file, "rb") as f:
            return pickle.load(f)

    historial = {}
    for arch in fuentes:
        try:
            with open(arch, encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    try:
                        ts = datetime.fromisoformat(
                            row["timestamp_utc"].replace("Z", "+00:00"))
                    except Exception:
                        continue
                    if ts < corte:
                        continue
                    mid = row.get("market_id", "")
                    py  = row.get("price_yes", "")
                    if not mid or not py:
                        continue
                    try:
                        py_f = float(py)
                    except ValueError:
                        continue
                    historial.setdefault(mid, []).append((ts, py_f))
        except Exception as e:
            print(f"  Error leyendo {arch}: {e}")
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

    # Precios intraday para UPDOWN_GBM
    precios_data = cargar_precios_intraday()
    ctx["precios_intraday"] = precios_data

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
    except Exception:
        pass
    ctx["spot_prices"] = spot_prices
    ctx["klines_raw"]  = klines_raw
    has_flow = any(len(v[0]) >= 7 for v in klines_raw.values() if v)
    print(f"  UPDOWN_GBM: {len(precios_data)} pts intraday | spot={{{', '.join(f'{k}={v:.4g}' for k, v in list(spot_prices.items())[:4])}}}")
    print(f"  ORDER_FLOW: klines de {len(klines_raw)} activos | flow_real={'sí' if has_flow else 'no (Kraken fallback)'}")
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
        last = rows[-1]
        for k, v in last.items():
            if k == "timestamp_utc":
                continue
            try:
                SPOT_PRECIOS[k] = float(v)
            except (ValueError, TypeError):
                pass
    except Exception:
        pass
    return SPOT_PRECIOS

def _extraer_precio_objetivo(question):
    q = question.replace(",", "").replace("$", "")
    m = _re.search(r'\b(\d+(?:\.\d+)?)[kK]\b', q)
    if m:
        return float(m.group(1)) * 1000
    m = _re.search(r'\b(\d{4,}(?:\.\d+)?)\b', q)
    if m:
        return float(m.group(1))
    return None

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
                            # fila limpia formato nuevo
                            try:
                                v = float(row.get("price_usd", ""))
                            except (ValueError, TypeError):
                                continue
                            if ts != buf_ts:
                                _emit(buf_ts, buf); buf, buf_ts = {}, ts
                            buf[asset] = v
                        else:
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
    return rows


def _estimar_vol_h(sym, precios_data, n_min=120):
    """Vol por hora a partir de las últimas n_min de precios spot. None si insuficiente."""
    ahora = datetime.now(timezone.utc)
    corte = ahora - timedelta(minutes=n_min)
    subset = [(ts, p[sym]) for ts, p in precios_data if sym in p and ts >= corte]
    if len(subset) < 5:
        subset = [(ts, p[sym]) for ts, p in precios_data if sym in p][-60:]
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

    pct = (spot / ref - 1) * 100

    # Drift macro: tendencia de las últimas 1h y 15min desde precios_intraday.
    # Se incorpora al GBM (amortiguado) para que el modelo sea consciente del régimen.
    drift_15 = _calcular_drift_h(activo, precios_data, 15)
    drift_60 = _calcular_drift_h(activo, precios_data, 60)
    delta_macro = _calcular_delta_ratio_macro(activo, ctx.get("klines_raw", {}))

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
    features = {
        "pct_spot_vs_ref": round(pct, 4),
        "sigma_h":         round(sigma_h, 6),
        "T_h":             round(T_h, 4),
    }
    if drift_15 is not None:
        features["drift_15min"] = round(drift_15 * 100, 4)   # %/hora
    if drift_60 is not None:
        features["drift_60min"] = round(drift_60 * 100, 4)   # %/hora
    if delta_macro is not None:
        features["delta_ratio_macro"] = round(delta_macro, 4)
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
    if not sigma_h or sigma_h <= 0:
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

# Horas UTC con edge negativo confirmado en ORDER_FLOW_5M (n≥20, IC≤-0.05)
ORDER_FLOW_BLACKLIST_HOURS = {2, 7, 9, 10, 11, 22}
# 02h IC=-0.081 n=29 PNL=-2.77€ | 07h IC=-0.067 n=28 PNL=-2.23€ | 09h IC=-0.067 n=28 PNL=-2.24€
# 10h IC=-0.190 n=27 PNL=-6.18€ (peor hora) | 11h IC=-0.086 n=56 | 22h IC=-0.115 n=37 PNL=-4.87€
# 18:xx UTC (20:xx Madrid): IC=-0.178 n=16 PNL=-4.15€ — cierre primera mitad
# 22:xx UTC era el blacklist original (IC=-0.115); con n=30 actual IC=+0.031 → desbloqueado

# Pares con IC negativo en sweet spot [0.38-0.46] (conf=1.00, n≥80):
# ETH: n=112, IC=-0.026 | XRP: n=119, IC=-0.004 (-6.13€ el 2026-06-25) | DOGE: n=83, IC=-0.006
# BNB: n=63, IC=+0.038 shadow — backfill 90d negativo, mantener bloqueado hasta n≥150
ORDER_FLOW_PAIR_BLACKLIST = {'ETH', 'BNB', 'XRP', 'DOGE'}


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


ESTRATEGIAS = [
    ("WEEKLY_PRICE",        s_weekly_price),
    ("PRICE_MOMENTUM",      s_price_momentum),
    ("SMART_FLOW_1H",       s_smart_flow_1h),
    ("UPDOWN_GBM",          s_updown_gbm),
    ("UPDOWN_OU_5M",        s_updown_ou_5m),
    ("PRICE_TARGET_GBM",    s_price_target_gbm),
    ("ORDER_FLOW_5M",       s_order_flow_5m),
    ("RESOLUTION_SNIPER",   s_resolution_sniper),
    # ("BINANCE_UPDOWN", s_binance_updown),  # retirada — IC -0.50
]

def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Shadow predict v8 ===")
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
        if h is None or not (HORIZONTE_MIN_HORAS <= h <= HORIZONTE_MAX_HORAS):
            continue
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
    ctx = construir_contexto()
    params_din = _cargar_params_dinamicos()
    if params_din:
        activas = {k for k, v in params_din.items() if not v.get("activa", True)}
        print(f"  Params dinámicos cargados: {len(params_din)} estrategias, desactivadas: {activas or 'ninguna'}")
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
                # (evita que BTC#240min quede activo cuando #240min está desactivado)
                if any(not params_din.get(k, {}).get("activa", True) for k in lookup_keys if k in params_din):
                    continue
                edge_min = sp.get("edge_minimo") or EDGE_MINIMO
                # Apuesta Kelly: escala con IC confirmado, mínimo 0.50€ si activa
                apuesta = sp.get("apuesta_kelly", 0.50) or 0.50
                # Aprendizaje causal: filtros (evitar) + patrones ganadores (amplificar)
                pred_features = pred.get("features", {}) or {}

                def _feature_match(feat_val, cond, umbral):
                    try:
                        v, u = float(feat_val), float(umbral)
                        if cond == "abs_gt":  return abs(v) > u
                        if cond == "abs_lt":  return abs(v) <= u
                        if cond == "gt":      return v > u
                        if cond == "lt":      return v <= u
                    except (TypeError, ValueError):
                        pass
                    return False

                # 1. Filtros causales — si matchean, skip
                skip_causal = False
                for lk in lookup_keys:
                    for f in params_din.get(lk, {}).get("filtros_causales", []):
                        fv = pred_features.get(f.get("feature"))
                        if fv is not None and _feature_match(fv, f.get("condicion",""), f.get("umbral",999)):
                            skip_causal = True
                            break
                    if skip_causal:
                        break
                if skip_causal:
                    continue

                # 2. Patrones ganadores — si matchean, boost a la apuesta
                for lk in lookup_keys:
                    for g in params_din.get(lk, {}).get("patrones_ganadores", []):
                        fv = pred_features.get(g.get("feature"))
                        if fv is not None and _feature_match(fv, g.get("condicion",""), g.get("umbral",999)):
                            boost = float(g.get("kelly_boost", 0))
                            apuesta = min(2.00, apuesta + boost)
                contador[nombre]["aplica"] += 1
                prob_y = pred["prob_yes"]
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
                ed = en if dec != "BUY_NO" else -en
                if dec != "SKIP":
                    ops += 1
                    ya_predichos.add((nombre, mid))
                features_json = json.dumps(pred.get("features", {}), separators=(",", ":"))
                market_rows.append([
                    ts, nombre, mid,
                    m.get("question", ""), m.get("end_date", ""),
                    f"{m['_horas']:.2f}", f"{py:.4f}", f"{prob_y:.4f}",
                    f"{eb:.4f}", f"{en:.4f}", f"{ed:.4f}", dec,
                    pred.get("razon", ""), subtype,
                    f"{apuesta:.2f}", features_json,
                ])

            # Kelly compuesto: boost si UPDOWN_GBM y ORDER_FLOW_5M coinciden
            market_rows = _aplicar_kelly_compuesto(market_rows)

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

