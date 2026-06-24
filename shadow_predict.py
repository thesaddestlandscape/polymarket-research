"""
shadow_predict.py — v7. Tres estrategias activas:
  1. PRICE_MOMENTUM — tendencia exponencial del precio YES (mejora de MICROSTRUCTURE_MOMENTUM)
  2. SMART_FLOW_1H  — flujo de compras recientes (ultimo 1h, wallets distintas, no BOT)
  3. BINANCE_UPDOWN — mercados Up/Down con senal de klines Binance (reserva futura)
"""
import csv, glob, json, math, os, sys
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

def cargar_mercados_recientes():
    fecha_hoy  = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    fecha_ayer = (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    archivos   = [DIR_MARKETS / f"{fecha_hoy}.csv", DIR_MARKETS / f"{fecha_ayer}.csv"]
    por_id = {}
    for arch in archivos:
        if not arch.exists():
            continue
        with open(arch, encoding="utf-8") as f:
            for row in csv.DictReader(f):
                mid = row.get("market_id")
                if not mid:
                    continue
                ts = row.get("timestamp_utc", "")
                if mid not in por_id or ts > por_id[mid]["timestamp_utc"]:
                    por_id[mid] = row
    return list(por_id.values())

def cargar_historial_mercados():
    corte    = datetime.now(timezone.utc) - timedelta(hours=6)
    historial = {}
    archivos  = sorted(glob.glob(str(DIR_MARKETS / "*.csv")))[-3:]
    for arch in archivos:
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
    return historial

def cargar_trades_recientes():
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
                    side    = (row.get("side") or "").upper()
                    if side != "BUY":
                        continue
                    wtype   = (row.get("wallet_type") or "").upper()
                    if wtype == "BOT":
                        continue
                    wallet  = (row.get("wallet") or "").lower()
                    mid     = (row.get("market_id") or "").strip()
                    outcome = (row.get("outcome") or "").upper()
                    if not wallet or not mid:
                        continue
                    if outcome == "YES":
                        action = "BUY_YES"
                    elif outcome == "NO":
                        action = "BUY_NO"
                    else:
                        continue
                    por_market.setdefault(mid, {}).setdefault(wallet, []).append(action)
        except Exception as e:
            print(f"  Error leyendo trades {arch}: {e}")
    return por_market

def construir_contexto():
    print("Construyendo contexto...")
    ctx = {}
    ctx["historial_mercados"] = cargar_historial_mercados()
    print(f"  Historial precios YES cargado para {len(ctx['historial_mercados'])} mercados")
    trades = cargar_trades_recientes()
    ctx["trades_1h"] = trades
    n_mkt     = len(trades)
    n_wallets = sum(len(v) for v in trades.values())
    print(f"  SMART_FLOW_1H: {n_mkt} mercados, {n_wallets} wallet-acciones en ultima 1h")
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
    }

def s_smart_flow_1h(market, ctx):
    import json as _json, glob as _glob
    mid         = market.get("market_id", "")
    trades      = ctx.get("trades_1h", {}).get(mid, {})
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
    return {"prob_yes": prob_yes, "razon": razon}

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
        return {
            "prob_yes": max(0.05, min(0.95, prob_yes)),
            "razon": f"weekly_between {activo} spot={spot:.0f} [{lo:.0f},{hi:.0f}] in={in_range}",
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
    }


ESTRATEGIAS = [
    ("WEEKLY_PRICE", s_weekly_price),
    ("PRICE_MOMENTUM",  s_price_momentum),
    ("SMART_FLOW_1H",   s_smart_flow_1h),
    # ("BINANCE_UPDOWN",  s_binance_updown),  # desactivado — IC -0.50
]

def main():
    ts = datetime.now(timezone.utc).isoformat(timespec="seconds")
    print(f"[{ts}] === Shadow predict v7 ===")
    mercados = cargar_mercados_recientes()
    print(f"  Mercados snapshot reciente: {len(mercados)}")
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
                "edge_bruto", "edge_neto", "edge_direccional", "decision", "razon",
            ])
        for m in operables:
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
                contador[nombre]["aplica"] += 1
                prob_y = pred["prob_yes"]
                eb = prob_y - py
                en = eb - SLIPPAGE_ESTIMADO if eb > 0 else eb + SLIPPAGE_ESTIMADO
                precio_extremo = (en >= EDGE_MINIMO and py < 0.10) or (-en >= EDGE_MINIMO and py > 0.90)
                if precio_extremo:
                    skipped_extremo += 1
                if en >= EDGE_MINIMO and not precio_extremo:
                    dec = "BUY_YES"
                elif -en >= EDGE_MINIMO and not precio_extremo:
                    dec = "BUY_NO"
                else:
                    dec = "SKIP"
                ed = en if dec != "BUY_NO" else -en
                if dec != "SKIP":
                    ops += 1
                    contador[nombre]["operable"] += 1
                    ya_predichos.add((nombre, mid))
                w.writerow([
                    ts, nombre, mid,
                    m.get("question", ""), m.get("end_date", ""),
                    f"{m['_horas']:.2f}", f"{py:.4f}", f"{prob_y:.4f}",
                    f"{eb:.4f}", f"{en:.4f}", f"{ed:.4f}", dec,
                    pred.get("razon", ""),
                ])
                total += 1
    print(f"  Predicciones registradas: {total} (operables: {ops}, dup saltados: {skipped_dup}, extremo filtrado: {skipped_extremo})")
    print("  Desglose por estrategia (aplica / operable):")
    for nombre, c in contador.items():
        print(f"    {nombre:20s}  {c['aplica']:>4} / {c['operable']:>4}")
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] === Fin ===")

if __name__ == "__main__":
    main()

