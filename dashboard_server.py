#!/usr/bin/env python3
"""
dashboard_server.py — Dashboard visual del bot Polymarket
Lanzar:  screen -dmS dash python3 dashboard_server.py
Acceso:  http://<VPS_IP>:8888  (pide usuario/contraseña — ver data/live/.env)
         o SSH tunnel: ssh -L 8888:localhost:8888 root@<VPS_IP> → http://localhost:8888

Auth: HTTP Basic, credenciales en data/live/.env (DASHBOARD_USER/DASHBOARD_PASS,
gitignored). Añadido 2026-07-01 — antes exponía bankroll/trades/IC en la IP
pública del VPS sin ningún control de acceso.
"""
import base64, csv, hmac, json, sys, time, threading, socket
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from pathlib import Path
from datetime import datetime, timezone, timedelta
from collections import defaultdict

STATIC_DIR = Path(__file__).parent / "static"

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / "data" / "live" / ".env")
except Exception:
    pass
import os
DASHBOARD_USER = os.environ.get("DASHBOARD_USER", "")
DASHBOARD_PASS = os.environ.get("DASHBOARD_PASS", "")
if not DASHBOARD_USER or not DASHBOARD_PASS:
    print("[dashboard] ⚠️  DASHBOARD_USER/DASHBOARD_PASS no configurados en data/live/.env "
          "— el dashboard queda SIN AUTENTICACIÓN en la IP pública.")

REPO             = Path(__file__).parent
RESULTS_CSV      = REPO / "data/shadow/results.csv"
STRATEGY_PARAMS  = REPO / "data/shadow/strategy_params.json"
PRICES_DIR       = REPO / "data/prices"
LIVE_TRADES_CSV  = REPO / "data/live/trades.csv"
LIVE_BALANCE_HISTORY_CSV = REPO / "data/live/balance_history.csv"
LIVE_SWITCH_PATH = REPO / "data/live/LIVE_MODE_ON"
LIVE_BANKROLL_INICIAL = 25.44  # depósito real 2026-06-29
BANKROLL_INICIAL = 20.0
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8888

try:
    # Fuente de verdad real: shadow_predict.py::ORDER_FLOW_BLACKLIST_HOURS.
    # Antes hardcodeado aquí como {7, 11, 18}, desactualizado frente al valor
    # real {2, 7, 9, 10, 11, 22} — el gráfico "mejor hora" marcaba mal las
    # horas bloqueadas. Import directo en vez de duplicar la constante.
    from shadow_predict import ORDER_FLOW_BLACKLIST_HOURS as BLACKLIST_HOURS
except Exception:
    BLACKLIST_HOURS = {2, 7, 9, 10, 11, 22}  # UTC — fallback si el import falla

try:
    # Balance REAL on-chain (verdad de suelo), cacheado por live_balance.py.
    from live_balance import cargar_balance_real
except Exception:
    cargar_balance_real = lambda **_: None  # fail-closed: sin módulo → sin real

# ─── Cache ───────────────────────────────────────────────────────────────────
_cache_lock = threading.Lock()
_cache_data  = None
_cache_ts    = 0.0
CACHE_TTL    = 1.0   # segundos — recalcula máximo 1×/s

# ─── Utilidades ──────────────────────────────────────────────────────────────

def _ts(s):
    try:
        s = str(s).replace("Z", "+00:00")
        if len(s) == 10:
            s += "T00:00:00+00:00"
        if "+" not in s[10:] and s[-1] != "Z":
            s += "+00:00"
        return int(datetime.fromisoformat(s).timestamp())
    except Exception:
        return 0

def _ic(wins, n):
    if n == 0:
        return 0.0
    return ((wins + 1) / (n + 2) - 0.5) * min(1.0, n / 20)

def _strat_key(r):
    s = r.get("strategy", "")
    sub = r.get("subtype", "")
    return f"{s}#{sub}" if sub else s

def _pnl(r):
    try:
        return float(r.get("pnl_neto", 0) or 0)
    except Exception:
        return 0.0

def _win(r):
    try:
        return int(r.get("acierto", 0) or 0)
    except Exception:
        return 0

# Simulación FIEL: el bankroll compuesto (+1900%) es una ficción — compone Kelly
# sobre tamaño que en live no se puede colocar. Este PnL usa STAKE FIJO (sin
# compounding) y descuenta el slippage estimado del modelo. Sigue SIN modelar
# fill-ability (conversión ~8%, selección adversa) → cota superior, no cobrable.
STAKE_FIJO_SIM = 1.0
SLIP_SIM = 0.02  # = shadow_predict.SLIPPAGE_ESTIMADO (clamp [0.005, 0.02])

def _pnl_realista(r):
    """PnL de una resolución a stake fijo 1$ con slippage real. None si no aplica."""
    dec = r.get("decision", "")
    if dec not in ("BUY_YES", "BUY_NO"):
        return None
    try:
        p_yes = float(r.get("precio_yes_mercado"))
        ac = int(r.get("acierto", 0) or 0)
    except Exception:
        return None
    p_dir = p_yes if dec == "BUY_YES" else (1.0 - p_yes)
    if not (0.01 < p_dir < 0.99):
        return None
    p_exec = min(p_dir + SLIP_SIM, 0.98)  # compra adversa: cuesta más
    return STAKE_FIJO_SIM * (1.0 / p_exec - 1.0) if ac == 1 else -STAKE_FIJO_SIM

# ─── Carga de datos ──────────────────────────────────────────────────────────

def load_results():
    if not RESULTS_CSV.exists():
        return []
    rows = list(csv.DictReader(open(RESULTS_CSV, encoding="utf-8")))
    rows.sort(key=lambda r: r.get("resolution_timestamp", ""))
    return rows

def load_prices():
    """Precios BTC/ETH/SOL de los últimos 7 días.
    Maneja dos formatos:
      - Viejo: timestamp_utc,BTC,ETH,SOL,XRP,DOGE,BNB,...  (una fila = todos los activos)
      - Nuevo: timestamp_utc,asset,price_usd,...            (una fila = un activo)
      - Mixto: archivo nuevo con filas viejas añadidas por el fast loop
    """
    assets = ("BTC", "ETH", "SOL")
    prices = {a: [] for a in assets}
    seen   = {a: set() for a in assets}

    for pf in sorted(PRICES_DIR.glob("*.csv"))[-7:]:
        try:
            with open(pf, encoding="utf-8") as fh:
                header = fh.readline().strip().split(",")

            old_multi = "BTC" in header   # timestamp_utc,BTC,ETH,SOL,...
            new_single = "asset" in header  # timestamp_utc,asset,price_usd,...

            if not old_multi and not new_single:
                continue

            with open(pf, encoding="utf-8") as fh:
                next(fh)  # skip header
                for line in fh:
                    parts = line.strip().split(",")
                    if len(parts) < 3:
                        continue
                    ts = _ts(parts[0])
                    if not ts:
                        continue

                    if old_multi:
                        # Columnas fijas: BTC=1, ETH=2, SOL=3
                        for i, a in enumerate(assets, start=1):
                            if i < len(parts) and parts[i] and ts not in seen[a]:
                                try:
                                    prices[a].append({"time": ts, "value": round(float(parts[i]), 2)})
                                    seen[a].add(ts)
                                except Exception:
                                    pass
                    else:
                        # Formato nuevo: parts[1]=asset, parts[2]=price_usd
                        asset_col = parts[1].strip() if len(parts) > 1 else ""
                        if asset_col in assets:
                            # Fila nueva (asset = "BTC", "ETH", "SOL")
                            try:
                                val = float(parts[2])
                                if ts not in seen[asset_col]:
                                    prices[asset_col].append({"time": ts, "value": round(val, 2)})
                                    seen[asset_col].add(ts)
                            except Exception:
                                pass
                        else:
                            # Fila vieja mezclada (parts[1] es el precio BTC)
                            for i, a in enumerate(assets, start=1):
                                if i < len(parts) and parts[i] and ts not in seen[a]:
                                    try:
                                        prices[a].append({"time": ts, "value": round(float(parts[i]), 2)})
                                        seen[a].add(ts)
                                    except Exception:
                                        pass
        except Exception:
            pass

    for a in assets:
        prices[a].sort(key=lambda x: x["time"])
        if len(prices[a]) > 600:
            step = len(prices[a]) // 600
            prices[a] = prices[a][::step]
    return prices

def load_activas():
    try:
        sp = json.load(open(STRATEGY_PARAMS, encoding="utf-8"))
        return {k: v.get("activa", True) for k, v in sp.get("estrategias", {}).items()}
    except Exception:
        return {}

def load_live_trades():
    if not LIVE_TRADES_CSV.exists():
        return []
    try:
        return list(csv.DictReader(open(LIVE_TRADES_CSV, encoding="utf-8")))
    except Exception:
        return []

def load_balance_history():
    """Serie granular del balance real on-chain (cron live_balance.py, ~15min).
    A diferencia de real_daily (un punto por día, reconstruido del PnL diario),
    esto es el snapshot real tal cual se capturó — más fiel para ver movimiento
    intradía, no solo el cierre de cada día."""
    if not LIVE_BALANCE_HISTORY_CSV.exists():
        return []
    try:
        rows = list(csv.DictReader(open(LIVE_BALANCE_HISTORY_CSV, encoding="utf-8")))
    except Exception:
        return []
    seen = {}
    for r in rows:
        ts = _ts(r.get("ts", ""))
        try:
            total = float(r.get("total") or 0)
        except (ValueError, TypeError):
            continue
        if not ts or not total:
            continue
        seen[ts] = round(total, 4)  # dedup por segundo, igual que el resto de charts
    return [{"time": t, "value": v} for t, v in sorted(seen.items())]

def compute_live_data():
    trades = load_live_trades()
    switch_on = LIVE_SWITCH_PATH.exists()
    closed = [t for t in trades if t.get("status") == "CLOSED"]
    # Orden cronológico por cierre — trades.csv está ordenado por apertura,
    # pero equity/daily se construyen sobre el momento en que se realiza el PnL
    closed.sort(key=lambda t: t.get("close_timestamp") or t.get("timestamp_utc") or "")
    pnl_total = sum(float(t.get("pnl_neto_eur") or 0) for t in closed)

    # PnL hoy en día Madrid sobre close_timestamp — mismo criterio que
    # live_stake.pnl_live_hoy() (el freno diario); antes usaba día UTC sobre
    # timestamp de apertura y no cuadraba con lo que reporta el circuit breaker
    try:
        from zoneinfo import ZoneInfo
        madrid_hoy = datetime.now(ZoneInfo("Europe/Madrid")).replace(
            hour=0, minute=0, second=0, microsecond=0)
        ts_ini_hoy = madrid_hoy.astimezone(timezone.utc).isoformat(timespec="seconds")
    except Exception:
        ts_ini_hoy = datetime.now(timezone.utc).strftime("%Y-%m-%dT00:00:00")
    ts_ini_7d = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat(timespec="seconds")

    def _cierre(t):
        return t.get("close_timestamp") or t.get("timestamp_utc") or ""
    pnl_hoy = sum(float(t.get("pnl_neto_eur") or 0) for t in closed if _cierre(t) >= ts_ini_hoy)
    pnl_7d  = sum(float(t.get("pnl_neto_eur") or 0) for t in closed if _cierre(t) >= ts_ini_7d)

    open_trades = [t for t in trades if t.get("status") == "OPEN"]
    wins = sum(1 for t in closed if float(t.get("pnl_neto_eur") or 0) > 0)
    fees_total = sum(float(t.get("fee_eur") or 0) for t in closed)
    fees_sin_confirmar = sum(1 for t in closed if "fee_confirmado=1" not in (t.get("notas") or ""))
    recent = sorted(trades, key=lambda t: t.get("timestamp_utc",""), reverse=True)[:10]

    # ── Equity curve (mismo formato que la shadow: {time, value}) ────────────
    bankroll = LIVE_BANKROLL_INICIAL
    seen = {}
    for t in closed:
        ts = _ts(_cierre(t))
        if not ts:
            continue
        bankroll += float(t.get("pnl_neto_eur") or 0)
        seen[ts] = round(bankroll, 4)   # dedup por segundo — LW exige tiempos crecientes
    equity = [{"time": ts, "value": v} for ts, v in sorted(seen.items())]
    if equity:
        equity = [{"time": equity[0]["time"] - 1, "value": LIVE_BANKROLL_INICIAL}] + equity

    # ── PnL diario ────────────────────────────────────────────────────────────
    daily = defaultdict(lambda: {"pnl": 0.0, "n": 0, "wins": 0})
    for t in closed:
        d = _cierre(t)[:10]
        if d:
            pnl = float(t.get("pnl_neto_eur") or 0)
            daily[d]["pnl"]  += pnl
            daily[d]["n"]    += 1
            daily[d]["wins"] += 1 if pnl > 0 else 0
    daily_pnl = sorted([
        {"time": d, "value": round(v["pnl"], 4), "n": v["n"],
         "wr": round(v["wins"] / v["n"] * 100, 1) if v["n"] else 0,
         "color": "#26a69a" if v["pnl"] >= 0 else "#ef5350"}
        for d, v in daily.items()
    ], key=lambda x: x["time"])

    # ── Por tupla estrategia#subtype dirección ────────────────────────────────
    strat = defaultdict(lambda: {"n": 0, "wins": 0, "pnl": 0.0})
    for t in closed:
        k = f"{t.get('strategy','?')}#{t.get('subtype','?')} {t.get('direction','')}"
        pnl = float(t.get("pnl_neto_eur") or 0)
        strat[k]["n"]    += 1
        strat[k]["wins"] += 1 if pnl > 0 else 0
        strat[k]["pnl"]  += pnl
    by_strategy = sorted([
        {"name": k, "n": d["n"],
         "ic": round(_ic(d["wins"], d["n"]), 4),
         "wr": round(d["wins"] / d["n"] * 100, 1) if d["n"] else 0,
         "pnl": round(d["pnl"], 2),
         "avg": round(d["pnl"] / d["n"], 4)}
        for k, d in strat.items() if d["n"] >= 3
    ], key=lambda x: x["pnl"], reverse=True)

    # ── Balance REAL on-chain (verdad de suelo) ───────────────────────────────
    # trades.csv da PnL de PLAN (precio previsto, fee=0); nunca cuadra con el
    # wallet. Anclamos a lo que Polymarket dice de verdad. Fail-closed: si el
    # cache falta o está rancio (>1h), real_* = None y el front muestra "n/d".
    real = cargar_balance_real(max_edad_s=3600)
    if real and not real.get("_rancio"):
        real_total   = real.get("total")
        real_pnl     = real.get("pnl_real")
        real_ts      = real.get("ts")
        real_deposito = real.get("deposito_inicial")
        real_hoy     = real.get("pnl_hoy_real")
        real_7d      = real.get("pnl_7d_real")
        real_daily   = real.get("daily_real") or []
        real_stale   = False
        # tracking error de ejecución: modelo(trades.csv) − real. >0 = optimista.
        tracking_error = round(pnl_total - real_pnl, 2) if real_pnl is not None else None
    else:
        real_total = real_pnl = real_ts = tracking_error = None
        real_deposito = real_hoy = real_7d = None
        real_daily = []
        real_stale = bool(real and real.get("_rancio"))

    # % de beneficio sobre el depósito inicial — pedido explícito 09-Jul: no
    # solo el $ absoluto, también el % relativo al depósito (por día y total).
    real_pct_total = (round(real_pnl / real_deposito * 100, 2)
                       if real_pnl is not None and real_deposito else None)
    real_pct_hoy = (round(real_hoy / real_deposito * 100, 2)
                     if real_hoy is not None and real_deposito else None)
    real_pct_7d = (round(real_7d / real_deposito * 100, 2)
                    if real_7d is not None and real_deposito else None)
    if real_daily and real_deposito:
        for d in real_daily:
            d["pct"] = round(d.get("pnl", 0) / real_deposito * 100, 2)

    # Histórico del capital real, DESDE EL LANZAMIENTO del bot (pedido 09-Jul):
    # backbone diario reconstruido de real_daily (cubre desde el primer día
    # real de trading, 07-01 — 06-29/06-30 fueron depósito y un intento con
    # error, sin actividad on-chain) + detalle fino donde ya hay snapshots de
    # 15min (live_balance.py, cron desde 07-07). Ambas fuentes en unix
    # seconds (_ts) para poder concatenarlas en una sola serie LightweightCharts.
    real_history_fine = load_balance_history()
    if real_daily and real_deposito:
        corte = real_history_fine[0]["time"] if real_history_fine else None
        acc = real_deposito
        t0 = _ts(real_daily[0]["date"])
        backbone = [{"time": t0 - 1, "value": round(real_deposito, 4)}] if t0 else []
        for d in real_daily:
            acc += d.get("pnl", 0)
            t = _ts(d["date"])
            if not t or (corte is not None and t >= corte):
                continue
            backbone.append({"time": t, "value": round(acc, 4)})
        real_history = backbone + real_history_fine
    else:
        real_history = real_history_fine

    return {
        "switch": switch_on,
        "bankroll": round(LIVE_BANKROLL_INICIAL + pnl_total, 2),
        "bankroll_inicial": LIVE_BANKROLL_INICIAL,
        "real_total": real_total,
        "real_pnl": real_pnl,
        "real_ts": real_ts,
        "real_deposito": real_deposito,
        "real_hoy": real_hoy,
        "real_7d": real_7d,
        "real_daily": real_daily,
        "real_history": real_history,
        "real_pct_total": real_pct_total,
        "real_pct_hoy": real_pct_hoy,
        "real_pct_7d": real_pct_7d,
        "real_stale": real_stale,
        "tracking_error": tracking_error,
        "pnl_total": round(pnl_total, 2),
        "pnl_hoy": round(pnl_hoy, 2),
        "pnl_7d": round(pnl_7d, 2),
        "n_total": len(trades),
        "n_open": len(open_trades),
        "n_closed": len(closed),
        "fees_total": round(fees_total, 4),
        "fees_sin_confirmar": fees_sin_confirmar,
        "win_rate": round(wins / len(closed) * 100, 1) if closed else 0,
        "recent_trades": recent,
        "equity_curve": equity,
        "daily_pnl": daily_pnl,
        "by_strategy": by_strategy,
    }

# ─── Procesamiento ───────────────────────────────────────────────────────────

def compute_data():
    rows    = load_results()
    prices  = load_prices()
    activas = load_activas()
    now     = datetime.now(timezone.utc)

    # ── Equity curve ──────────────────────────────────────────────────────────
    bankroll = BANKROLL_INICIAL
    equity_raw = []
    for r in rows:
        ts = _ts(r.get("resolution_timestamp", ""))
        if not ts:
            continue
        bankroll += _pnl(r)
        equity_raw.append({"time": ts, "value": round(bankroll, 4)})
    # LightweightCharts exige timestamps estrictamente crecientes — deduplicar por segundo
    seen = {}
    for p in equity_raw:
        seen[p["time"]] = p["value"]  # si hay duplicado, gana el último (más actualizado)
    equity = [{"time": t, "value": v} for t, v in sorted(seen.items())]
    if equity:
        equity = [{"time": equity[0]["time"] - 1, "value": BANKROLL_INICIAL}] + equity

    # ── PnL diario ────────────────────────────────────────────────────────────
    daily = defaultdict(lambda: {"pnl": 0.0, "n": 0, "wins": 0})
    for r in rows:
        d = r.get("resolution_timestamp", "")[:10]
        if d:
            daily[d]["pnl"]  += _pnl(r)
            daily[d]["n"]    += 1
            daily[d]["wins"] += _win(r)

    daily_pnl = sorted([
        {"time": d,
         "value": round(v["pnl"], 4),
         "n": v["n"],
         "wr": round(v["wins"] / v["n"] * 100, 1) if v["n"] else 0,
         "color": "#26a69a" if v["pnl"] >= 0 else "#ef5350"}
        for d, v in daily.items()
    ], key=lambda x: x["time"])

    # ── Por hora UTC ──────────────────────────────────────────────────────────
    hourly = defaultdict(lambda: {"n": 0, "wins": 0, "pnl": 0.0})
    for r in rows:
        ts_str = r.get("resolution_timestamp", "")
        if not ts_str:
            continue
        try:
            h = datetime.fromisoformat(ts_str.replace("Z", "+00:00")).hour
            hourly[h]["n"]    += 1
            hourly[h]["wins"] += _win(r)
            hourly[h]["pnl"]  += _pnl(r)
        except Exception:
            pass

    by_hour = []
    for h in range(24):
        d  = hourly[h]
        n  = d["n"]
        ic = round(_ic(d["wins"], n), 4)
        by_hour.append({
            "hour": h,
            "n": n,
            "ic": ic,
            "pnl": round(d["pnl"], 2),
            "wr": round(d["wins"] / n * 100, 1) if n else 0,
            "blacklisted": h in BLACKLIST_HOURS,
        })

    # ── Por estrategia ────────────────────────────────────────────────────────
    strat = defaultdict(lambda: {"n": 0, "wins": 0, "pnl": 0.0})
    for r in rows:
        k = _strat_key(r)
        strat[k]["n"]    += 1
        strat[k]["wins"] += _win(r)
        strat[k]["pnl"]  += _pnl(r)

    by_strategy = sorted([
        {
            "name":   k,
            "n":      d["n"],
            "ic":     round(_ic(d["wins"], d["n"]), 4),
            "pnl":    round(d["pnl"], 2),
            "wr":     round(d["wins"] / d["n"] * 100, 1) if d["n"] else 0,
            "activa": activas.get(k, True),
        }
        for k, d in strat.items() if d["n"] >= 5
    ], key=lambda x: x["pnl"], reverse=True)

    # ── Por activo ────────────────────────────────────────────────────────────
    asset_map = defaultdict(lambda: {"n": 0, "wins": 0, "pnl": 0.0})
    for r in rows:
        sub = r.get("subtype", "")
        if not sub:
            continue
        asset = sub.split("#")[0]
        if any(x in asset for x in ("min", "daily", "sniper", "atexpiry", "reach")):
            continue
        asset_map[asset]["n"]    += 1
        asset_map[asset]["wins"] += _win(r)
        asset_map[asset]["pnl"]  += _pnl(r)

    by_asset = sorted([
        {"asset": a,
         "n": d["n"],
         "ic": round(_ic(d["wins"], d["n"]), 4),
         "pnl": round(d["pnl"], 2),
         "wr": round(d["wins"] / d["n"] * 100, 1) if d["n"] else 0}
        for a, d in asset_map.items()
    ], key=lambda x: x["pnl"], reverse=True)

    # ── Rolling IC por estrategia principal ───────────────────────────────────
    WINDOW = 20
    rolling_ic = {}
    for k, d in strat.items():
        if d["n"] < WINDOW:
            continue
        k_rows = [r for r in rows if _strat_key(r) == k]
        pts = []
        step = max(1, len(k_rows) // 80)
        for i in range(WINDOW, len(k_rows) + 1, step):
            chunk = k_rows[max(0, i - WINDOW):i]
            wins  = sum(_win(r) for r in chunk)
            ic    = _ic(wins, len(chunk))
            ts    = _ts(k_rows[i - 1].get("resolution_timestamp", ""))
            if ts:
                pts.append({"time": ts, "value": round(ic, 4)})
        if pts:
            rolling_ic[k] = pts

    # ── Ventanas del bot (Madrid CEST = UTC+2) ────────────────────────────────
    # Ventana → rango UTC (h0:m0 → h1:m1)
    VENTANAS = [
        ("08:30–09:30",  6, 30,  7, 30),
        ("10:30–11:30",  8, 30,  9, 30),
        ("16:30–17:30", 14, 30, 15, 30),
        ("18:30–19:30", 16, 30, 17, 30),
        ("20:30–21:30", 18, 30, 19, 30),
    ]
    ventanas_perf = []
    for label, h0, m0, h1, m1 in VENTANAS:
        start_min = h0 * 60 + m0
        end_min   = h1 * 60 + m1
        vrows = []
        for r in rows:
            ts_str = r.get("resolution_timestamp", "")
            if not ts_str:
                continue
            try:
                dt   = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                mins = dt.hour * 60 + dt.minute
                if start_min <= mins <= end_min:
                    vrows.append(r)
            except Exception:
                pass
        n    = len(vrows)
        wins = sum(_win(r) for r in vrows)
        pnl  = sum(_pnl(r) for r in vrows)
        ventanas_perf.append({
            "label": label,
            "n": n,
            "ic": round(_ic(wins, n), 4),
            "pnl": round(pnl, 2),
            "wr": round(wins / n * 100, 1) if n else 0,
        })

    # ── Rentabilidad por apuesta ──────────────────────────────────────────────
    all_pnls  = [_pnl(r) for r in rows]
    wins_pnl  = [p for p in all_pnls if p > 0]
    loss_pnl  = [p for p in all_pnls if p < 0]
    BUCKETS = [
        ("< −1$",        None, -1.0),
        ("−1$ a −0.5$",  -1.0, -0.5),
        ("−0.5$ a 0$",   -0.5,  0.0),
        ("0$ a +0.5$",    0.0,  0.5),
        ("+0.5$ a +1$",   0.5,  1.0),
        ("> +1$",          1.0, None),
    ]
    dist = []
    for label_b, lo, hi in BUCKETS:
        cnt = sum(1 for p in all_pnls
                  if (lo is None or p >= lo) and (hi is None or p < hi))
        dist.append({"label": label_b, "n": cnt,
                     "pct": round(cnt / len(all_pnls) * 100, 1) if all_pnls else 0,
                     "pos": (hi is None or hi > 0) and (lo is None or lo >= 0)})

    per_bet_strat = sorted([
        {"name": k,
         "avg": round(d["pnl"] / d["n"], 4),
         "n": d["n"],
         "pnl": round(d["pnl"], 2),
         "activa": activas.get(k, True)}
        for k, d in strat.items() if d["n"] >= 10
    ], key=lambda x: x["avg"], reverse=True)

    per_bet = {
        "avg_total": round(sum(all_pnls) / len(all_pnls), 4) if all_pnls else 0,
        "avg_win":   round(sum(wins_pnl) / len(wins_pnl), 4) if wins_pnl else 0,
        "avg_loss":  round(sum(loss_pnl) / len(loss_pnl), 4) if loss_pnl else 0,
        "ratio":     round(abs(sum(wins_pnl) / len(wins_pnl)) / abs(sum(loss_pnl) / len(loss_pnl)), 3) if wins_pnl and loss_pnl else 0,
        "dist":      dist,
        "by_strategy": per_bet_strat,
    }

    # ── Stats globales ────────────────────────────────────────────────────────
    pnl_total  = sum(_pnl(r) for r in rows)
    wins_total = sum(_win(r) for r in rows)
    n_total    = len(rows)
    hoy        = now.strftime("%Y-%m-%d")
    rows_hoy   = [r for r in rows if r.get("resolution_timestamp", "").startswith(hoy)]
    rows_7d    = [r for r in rows if r.get("resolution_timestamp", "") >= (now - timedelta(days=7)).strftime("%Y-%m-%d")]
    rows_30d   = [r for r in rows if r.get("resolution_timestamp", "") >= (now - timedelta(days=30)).strftime("%Y-%m-%d")]

    # Trade markers para BTC (gana/pierde en precios)
    btc_markers = []
    for r in rows:
        if "BTC" not in r.get("subtype", ""):
            continue
        ts = _ts(r.get("resolution_timestamp", ""))
        if not ts:
            continue
        won = _win(r) == 1
        btc_markers.append({
            "time": ts,
            "position": "aboveBar" if won else "belowBar",
            "color": "#26a69a" if won else "#ef5350",
            "shape": "arrowDown" if won else "arrowUp",
            "size": 0.6,
        })

    return {
        "stats": {
            "bankroll":  round(BANKROLL_INICIAL + pnl_total, 2),
            "pnl_total": round(pnl_total, 2),
            "pnl_hoy":   round(sum(_pnl(r) for r in rows_hoy), 2),
            "pnl_7d":    round(sum(_pnl(r) for r in rows_7d), 2),
            "pnl_30d":   round(sum(_pnl(r) for r in rows_30d), 2),
            "win_rate":  round(wins_total / n_total * 100, 1) if n_total else 0,
            "n_ops":     n_total,
            "n_hoy":     len(rows_hoy),
            "updated":   now.strftime("%H:%M:%S UTC"),
            # PnL fiel (stake fijo + slippage, sin compounding ni fill-ability)
            "pnl_realista": round(sum(v for v in (_pnl_realista(r) for r in rows) if v is not None), 2),
        },
        "equity_curve":  equity,
        "daily_pnl":     daily_pnl,
        "by_hour":       by_hour,
        "by_strategy":   by_strategy,
        "by_asset":      by_asset,
        "rolling_ic":    rolling_ic,
        "prices":        prices,
        "btc_markers":   btc_markers,
        "ventanas_perf": ventanas_perf,
        "per_bet":       per_bet,
        "live":          compute_live_data(),
    }

def get_data():
    global _cache_data, _cache_ts
    with _cache_lock:
        if time.monotonic() - _cache_ts < CACHE_TTL and _cache_data is not None:
            return _cache_data
        try:
            _cache_data = compute_data()
        except Exception as e:
            if _cache_data is not None:
                return _cache_data   # sirve el último bueno si falla
            raise
        _cache_ts = time.monotonic()
        return _cache_data

# ─── HTML ────────────────────────────────────────────────────────────────────

HTML = r"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Polymarket Bot Dashboard</title>
<script src="/lc.js"></script>
<style>
:root {
  --bg:       #131722;
  --card:     #1e2230;
  --border:   #2a2e39;
  --text:     #d1d4dc;
  --muted:    #787b86;
  --green:    #26a69a;
  --red:      #ef5350;
  --yellow:   #f0c832;
  --blue:     #2962ff;
  --purple:   #9c27b0;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: var(--bg); color: var(--text); font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 13px; }
header { display: flex; align-items: center; justify-content: space-between; padding: 12px 20px; background: var(--card); border-bottom: 1px solid var(--border); }
header h1 { font-size: 16px; font-weight: 600; letter-spacing: .5px; color: #fff; }
#update-badge { font-size: 11px; color: var(--muted); }
.stats-row { display: grid; grid-template-columns: repeat(6, 1fr); gap: 1px; background: var(--border); border-bottom: 1px solid var(--border); }
.stat-card { background: var(--card); padding: 12px 16px; }
.stat-card .label { font-size: 10px; color: var(--muted); text-transform: uppercase; letter-spacing: .5px; margin-bottom: 4px; }
.stat-card .value { font-size: 22px; font-weight: 700; }
.pos { color: var(--green); }
.neg { color: var(--red); }
.neu { color: var(--text); }
.tabs { display: flex; gap: 4px; padding: 10px 16px; background: var(--card); border-bottom: 1px solid var(--border); }
.tab { padding: 5px 14px; border-radius: 4px; cursor: pointer; font-size: 12px; color: var(--muted); border: 1px solid transparent; transition: all .15s; }
.tab.active { background: #2962ff22; border-color: var(--blue); color: var(--blue); }
.tab:hover:not(.active) { color: var(--text); border-color: var(--border); }
.grid { display: grid; gap: 1px; background: var(--border); }
.grid-2 { grid-template-columns: 1fr 1fr; }
.grid-3 { grid-template-columns: 2fr 1fr 1fr; }
.panel { background: var(--card); padding: 14px; }
.panel-title { font-size: 11px; color: var(--muted); text-transform: uppercase; letter-spacing: .5px; margin-bottom: 10px; }
.chart-host { width: 100%; }

/* ── Barra horizontal ── */
.bar-row { display: flex; align-items: center; gap: 8px; margin-bottom: 5px; font-size: 11px; }
.bar-label { width: 140px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; color: var(--text); flex-shrink: 0; }
.bar-label.inactive { color: var(--muted); text-decoration: line-through; }
.bar-track { flex: 1; height: 14px; background: #ffffff0a; border-radius: 2px; position: relative; overflow: hidden; }
.bar-fill { height: 100%; border-radius: 2px; transition: width .3s; }
.bar-val { width: 56px; text-align: right; flex-shrink: 0; }
.bar-n { width: 36px; text-align: right; color: var(--muted); flex-shrink: 0; }

/* ── Barras de hora ── */
.hour-grid { display: grid; grid-template-columns: repeat(24, 1fr); gap: 2px; height: 90px; align-items: end; margin-top: 8px; }
.hour-bar-wrap { display: flex; flex-direction: column; align-items: center; gap: 2px; }
.hour-bar { width: 100%; border-radius: 2px 2px 0 0; min-height: 2px; }
.hour-label { font-size: 8px; color: var(--muted); }
.hour-bl { opacity: .35; outline: 1px solid var(--red); }

/* ── Ventanas ── */
.ventanas-grid { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
.ventana-card { background: #ffffff06; border-radius: 4px; padding: 10px; border: 1px solid var(--border); }
.ventana-card.pos-card { border-color: #26a69a44; }
.ventana-card.neg-card { border-color: #ef535044; }
.ventana-time { font-size: 11px; font-weight: 600; margin-bottom: 6px; color: var(--text); }
.ventana-ic { font-size: 18px; font-weight: 700; margin-bottom: 2px; }
.ventana-sub { font-size: 10px; color: var(--muted); }

/* ── Rolling ── */
#legend { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 6px; font-size: 11px; }
.legend-item { display: flex; align-items: center; gap: 5px; cursor: pointer; }
.legend-dot { width: 8px; height: 8px; border-radius: 50%; }

/* ── Tabla ── */
.mini-table { width: 100%; border-collapse: collapse; font-size: 11px; }
.mini-table th { color: var(--muted); text-align: left; padding: 4px 6px; border-bottom: 1px solid var(--border); font-weight: 500; }
.mini-table td { padding: 4px 6px; border-bottom: 1px solid #ffffff08; }
.mini-table tr:hover td { background: #ffffff05; }

footer { text-align: center; padding: 10px; font-size: 10px; color: var(--muted); border-top: 1px solid var(--border); }
</style>
</head>
<body>
<header>
  <h1>🤖 Polymarket Bot — Dashboard</h1>
  <span id="update-badge">Cargando…</span>
</header>

<!-- LIVE TRADING — preámbulo -->
<div id="live-section" style="background:#0d1f1a;border:1px solid #26a69a55;border-radius:8px;margin:8px 8px 0;padding:12px 16px">
  <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">
    <div id="live-switch-badge" style="font-size:12px;font-weight:700;padding:3px 10px;border-radius:20px">…</div>
    <span style="font-size:13px;font-weight:600;color:#e0e0e0">LIVE TRADING — Polymarket</span>
    <span style="font-size:11px;color:#26a69a;margin-left:4px">💵 dinero real · todas las cifras del wallet on-chain</span>
    <span id="live-real-freshness" style="font-size:10px;color:var(--muted);margin-left:auto">balance on-chain: —</span>
  </div>
  <div style="display:grid;grid-template-columns:repeat(10,1fr);gap:8px;margin-bottom:6px">
    <div style="background:#ffffff08;border-radius:6px;padding:8px;text-align:center">
      <div style="font-size:9px;color:var(--muted)">💰 Depósito inicial</div>
      <div id="live-deposito" style="font-size:20px;font-weight:700">—</div>
      <div style="font-size:9px;color:var(--muted)">2026-06-29</div>
    </div>
    <div style="background:#ffffff08;border-radius:6px;padding:8px;text-align:center">
      <div style="font-size:9px;color:var(--muted)">🏦 Dinero actual</div>
      <div id="live-bankroll" style="font-size:20px;font-weight:700">—</div>
      <div style="font-size:9px;color:var(--muted)">balance wallet</div>
    </div>
    <div style="background:#ffffff08;border-radius:6px;padding:8px;text-align:center">
      <div style="font-size:9px;color:var(--muted)">📈 PNL real total</div>
      <div id="live-pnl" style="font-size:20px;font-weight:700">—</div>
      <div style="font-size:9px;color:var(--muted)">desde el depósito</div>
    </div>
    <div style="background:#ffffff08;border-radius:6px;padding:8px;text-align:center" title="PNL real total dividido entre el depósito inicial">
      <div style="font-size:9px;color:var(--muted)">📊 % total</div>
      <div id="live-pct-total" style="font-size:20px;font-weight:700">—</div>
      <div style="font-size:9px;color:var(--muted)">sobre depósito</div>
    </div>
    <div style="background:#ffffff08;border-radius:6px;padding:8px;text-align:center">
      <div style="font-size:9px;color:var(--muted)">🎯 PNL hoy</div>
      <div id="live-pnl-hoy" style="font-size:20px;font-weight:700">—</div>
      <div style="font-size:9px;color:var(--muted)">real · día UTC</div>
    </div>
    <div style="background:#ffffff08;border-radius:6px;padding:8px;text-align:center" title="PNL de hoy dividido entre el depósito inicial">
      <div style="font-size:9px;color:var(--muted)">📊 % hoy</div>
      <div id="live-pct-hoy" style="font-size:20px;font-weight:700">—</div>
      <div style="font-size:9px;color:var(--muted)">sobre depósito</div>
    </div>
    <div style="background:#ffffff08;border-radius:6px;padding:8px;text-align:center">
      <div style="font-size:9px;color:var(--muted)">📅 Últimos 7 días</div>
      <div id="live-pnl-7d" style="font-size:20px;font-weight:700">—</div>
      <div style="font-size:9px;color:var(--muted)">real</div>
    </div>
    <div style="background:#ffffff08;border-radius:6px;padding:8px;text-align:center">
      <div style="font-size:9px;color:var(--muted)">✅ Win rate</div>
      <div id="live-wr" style="font-size:20px;font-weight:700">—</div>
      <div style="font-size:9px;color:var(--muted)">trades cerrados</div>
    </div>
    <div style="background:#ffffff08;border-radius:6px;padding:8px;text-align:center">
      <div style="font-size:9px;color:var(--muted)">🎲 Trades</div>
      <div id="live-trades-count" style="font-size:20px;font-weight:700">—</div>
      <div style="font-size:9px;color:var(--muted)">total · abiertas</div>
    </div>
    <div style="background:#ffffff08;border-radius:6px;padding:8px;text-align:center" title="Fee real de Polymarket cobrado en cada compra (nunca al canjear); contabilizado desde el fix del 08-Jul">
      <div style="font-size:9px;color:var(--muted)">💸 Fees pagados</div>
      <div id="live-fees-total" style="font-size:20px;font-weight:700">—</div>
      <div style="font-size:9px;color:var(--muted)">real · acumulado</div>
    </div>
  </div>
  <div id="live-modelo-nota" style="font-size:10px;color:var(--muted);margin-bottom:10px">&nbsp;</div>

  <!-- Charts live — mismo escritorio que el modelo simulado -->
  <div style="display:grid;grid-template-columns:2fr 1fr;gap:8px;margin-bottom:10px">
    <div style="background:#ffffff05;border-radius:6px;padding:10px">
      <div class="panel-title">📈 Evolución del capital real — desde el lanzamiento (diario + snapshot ~15min recientes, on-chain)</div>
      <div class="chart-host" id="live-equity-chart" style="height:180px"></div>
    </div>
    <div style="background:#ffffff05;border-radius:6px;padding:10px">
      <div class="panel-title">📊 PnL real por día — on-chain (redenciones − compras)</div>
      <div class="chart-host" id="live-daily-chart" style="height:180px"></div>
    </div>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-bottom:10px">
    <div style="background:#ffffff05;border-radius:6px;padding:10px">
      <div class="panel-title">🧠 Ventaja por estrategia live (tuplas cerradas, n≥3)</div>
      <div id="live-strat-bars"><span style="color:var(--muted);font-size:11px">Sin datos aún</span></div>
    </div>
    <div style="background:#ffffff05;border-radius:6px;padding:10px">
      <div class="panel-title">💶 Ganancia neta media por trade y estrategia — live</div>
      <div id="live-perbet-bars"><span style="color:var(--muted);font-size:11px">Sin datos aún</span></div>
    </div>
  </div>

  <table class="mini-table" id="live-trades-table">
    <thead><tr>
      <th>Hora</th><th>Estrategia</th><th>Mercado</th><th>Dir.</th>
      <th>Stake</th><th>Precio</th><th>Fee</th><th>Estado</th><th>PNL neto</th>
    </tr></thead>
    <tbody id="live-trades-body"><tr><td colspan="9" style="color:var(--muted);text-align:center">Sin trades aún</td></tr></tbody>
  </table>
</div>

<!-- Separador: a partir de aquí TODO es simulación, no dinero real -->
<div style="margin:14px 8px 4px;padding:8px 14px;background:#3a2a0d;border:1px solid #d1932655;border-radius:8px;display:flex;align-items:center;gap:10px">
  <span style="font-size:12px;font-weight:700;color:#e0a53a">🧪 MODELO SIMULADO</span>
  <span style="font-size:11px;color:var(--muted)">shadow sin fricciones — <b>no es dinero real</b>. No descuenta fill-ability (conversión medida ~8%) ni slippage; es una cota superior, no lo cobrable en live.</span>
</div>

<!-- Stats row (simulado) -->
<div class="stats-row">
  <div class="stat-card"><div class="label">🧪 Capital simulado</div><div class="value neu" id="s-bankroll">—</div></div>
  <div class="stat-card"><div class="label">📈 Beneficio simulado <span style="opacity:.6">compuesto</span></div><div class="value" id="s-pnl">—</div></div>
  <div class="stat-card" title="Stake fijo 1$ + slippage real 0.02, sin compounding. NO modela fill-ability (~8% conversión) → sigue siendo cota superior."><div class="label">🧮 PnL fiel <span style="opacity:.6">stake fijo</span></div><div class="value" id="s-pnl-real">—</div></div>
  <div class="stat-card"><div class="label">🎯 Simulado hoy</div><div class="value" id="s-pnl-hoy">—</div></div>
  <div class="stat-card"><div class="label">📅 Últimos 7 días (sim)</div><div class="value" id="s-pnl-7d">—</div></div>
  <div class="stat-card"><div class="label">✅ Apuestas acertadas</div><div class="value neu" id="s-wr">—</div></div>
  <div class="stat-card"><div class="label">🎲 Apuestas (hoy)</div><div class="value neu" id="s-ops">—</div></div>
</div>

<!-- Tabs -->
<div class="tabs">
  <div class="tab active" data-period="1">Hoy</div>
  <div class="tab" data-period="7">7 días</div>
  <div class="tab" data-period="30">30 días</div>
  <div class="tab" data-period="0">Todo</div>
</div>

<!-- Row 1: Equity + PnL diario -->
<div class="grid grid-2" style="grid-template-columns:2fr 1fr">
  <div class="panel">
    <div class="panel-title">📈 Evolución del capital — cada punto es una apuesta resuelta</div>
    <div class="chart-host" id="equity-chart" style="height:200px"></div>
  </div>
  <div class="panel">
    <div class="panel-title">📊 Ganancia / Pérdida por día</div>
    <div class="chart-host" id="daily-chart" style="height:200px"></div>
  </div>
</div>

<!-- Row 2: BTC price + Rolling IC -->
<div class="grid grid-2">
  <div class="panel">
    <div class="panel-title">💹 Precio de las criptos — los marcadores ▲▼ son apuestas ganadas/perdidas en BTC</div>
    <div class="chart-host" id="price-chart" style="height:180px"></div>
  </div>
  <div class="panel">
    <div class="panel-title">📡 Tendencia de precisión — media de las últimas 20 apuestas por estrategia</div>
    <div id="legend"></div>
    <div class="chart-host" id="rolling-chart" style="height:155px"></div>
  </div>
</div>

<!-- Row 3: Hora UTC + Ventanas -->
<div class="grid grid-2">
  <div class="panel">
    <div class="panel-title">🕐 Mejor hora para apostar — verde = rentable, 🚫 = hora bloqueada por el bot</div>
    <div class="hour-grid" id="hour-bars"></div>
    <div style="display:flex;justify-content:space-between;margin-top:4px;font-size:9px;color:var(--muted)">
      <span>medianoche</span><span>06h</span><span>mediodía</span><span>18h</span><span>23h</span>
    </div>
  </div>
  <div class="panel">
    <div class="panel-title">⏰ Horarios de operación — Madrid (todas las estrategias)</div>
    <div class="ventanas-grid" id="ventanas"></div>
  </div>
</div>

<!-- Row 4: Por estrategia + Por activo -->
<div class="grid grid-2">
  <div class="panel">
    <div class="panel-title">🧠 Ventaja por estrategia — qué tan por encima del 50% acierta cada una</div>
    <div id="strat-bars"></div>
  </div>
  <div class="panel">
    <div class="panel-title">🪙 Ventaja por moneda</div>
    <div id="asset-bars"></div>
    <div class="panel-title" style="margin-top:16px">📋 Tabla completa de estrategias</div>
    <table class="mini-table">
      <thead><tr><th>Estrategia</th><th>Apuestas</th><th>Aciertos</th><th>Ventaja</th><th>Beneficio</th></tr></thead>
      <tbody id="strat-table"></tbody>
    </table>
  </div>
</div>

<!-- Row 5: Rentabilidad por apuesta -->
<div class="grid" style="grid-template-columns:1fr 1fr 1fr;background:var(--border);gap:1px;border-top:1px solid var(--border)">

  <!-- Mini stats -->
  <div class="panel">
    <div class="panel-title">💶 ¿Cuánto gana el bot por apuesta? — resumen</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:4px">
      <div style="background:#ffffff08;border-radius:6px;padding:12px;text-align:center">
        <div style="font-size:10px;color:var(--muted);margin-bottom:4px">Valor esperado por apuesta</div>
        <div id="pb-avg" style="font-size:26px;font-weight:700">—</div>
        <div style="font-size:10px;color:var(--muted)">en promedio, cada apuesta genera este importe neto</div>
      </div>
      <div style="background:#ffffff08;border-radius:6px;padding:12px;text-align:center">
        <div style="font-size:10px;color:var(--muted);margin-bottom:4px">Ratio ganancia / pérdida</div>
        <div id="pb-ratio" style="font-size:26px;font-weight:700">—</div>
        <div style="font-size:10px;color:var(--muted)">cuando gana, gana esta proporción vs cuando pierde</div>
      </div>
      <div style="background:#26a69a18;border:1px solid #26a69a44;border-radius:6px;padding:12px;text-align:center">
        <div style="font-size:10px;color:var(--muted);margin-bottom:4px">✅ Media cuando acierta</div>
        <div id="pb-win" style="font-size:22px;font-weight:700;color:var(--green)">—</div>
      </div>
      <div style="background:#ef535018;border:1px solid #ef535044;border-radius:6px;padding:12px;text-align:center">
        <div style="font-size:10px;color:var(--muted);margin-bottom:4px">❌ Media cuando falla</div>
        <div id="pb-loss" style="font-size:22px;font-weight:700;color:var(--red)">—</div>
      </div>
    </div>
  </div>

  <!-- Distribución -->
  <div class="panel">
    <div class="panel-title">📊 Distribución de resultados por apuesta</div>
    <div id="pb-dist" style="margin-top:8px"></div>
  </div>

  <!-- Por estrategia -->
  <div class="panel">
    <div class="panel-title">🏆 Ganancia neta media por apuesta y estrategia</div>
    <div id="pb-strat"></div>
  </div>

</div>

<footer>Se actualiza automáticamente cada 60 segundos · "Ventaja" = qué tan por encima del 50% acierta el modelo · Verde = ganando, Rojo = perdiendo</footer>

<script>
// ─── Estado ──────────────────────────────────────────────────────────────────
let DATA       = null;
let PERIOD     = 1;   // días; 0 = todo
const COLORS   = ["#2962ff","#26a69a","#f0c832","#9c27b0","#ff6d00","#00bcd4","#e91e63"];

// ─── Instancias de charts LW ─────────────────────────────────────────────────
let eqChart, eqArea, dailyChart, dailySeries, priceChart, btcLine, ethLine, solLine,
    rollingChart, rollingSeries = {},
    liveEqChart, liveEqArea, liveDailyChart, liveDailySeries;

function makeLWChart(id, opts = {}) {
  const el = document.getElementById(id);
  return LightweightCharts.createChart(el, {
    width:  el.offsetWidth,
    height: el.offsetHeight,
    layout: { background: { color: "transparent" }, textColor: "#787b86" },
    grid:   { vertLines: { color: "#2a2e39" }, horzLines: { color: "#2a2e39" } },
    crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
    rightPriceScale: { borderColor: "#2a2e39" },
    timeScale: { borderColor: "#2a2e39", timeVisible: true, secondsVisible: false },
    ...opts,
  });
}

function initCharts() {
  // Equity
  eqChart = makeLWChart("equity-chart");
  eqArea = eqChart.addAreaSeries({
    lineColor: "#26a69a", topColor: "#26a69a44", bottomColor: "#26a69a00",
    lineWidth: 2, priceFormat: { type: "price", precision: 2, minMove: 0.01 },
    title: "$",
  });

  // Daily PnL histogram
  dailyChart = makeLWChart("daily-chart", { timeScale: { visible: true } });
  dailySeries = dailyChart.addHistogramSeries({
    color: "#26a69a", priceFormat: { type: "price", precision: 2, minMove: 0.01 },
  });

  // Prices
  priceChart = makeLWChart("price-chart");
  btcLine = priceChart.addLineSeries({ color: "#f0c832", lineWidth: 1.5, title: "BTC", priceScaleId: "btc" });
  ethLine = priceChart.addLineSeries({ color: "#2962ff", lineWidth: 1.5, title: "ETH", priceScaleId: "eth" });
  solLine = priceChart.addLineSeries({ color: "#26a69a", lineWidth: 1.5, title: "SOL", priceScaleId: "sol" });
  priceChart.priceScale("eth").applyOptions({ visible: false });
  priceChart.priceScale("sol").applyOptions({ visible: false });

  // Rolling IC
  rollingChart = makeLWChart("rolling-chart", {
    rightPriceScale: { borderColor: "#2a2e39" },
    timeScale: { timeVisible: true, secondsVisible: false },
  });
  // Baseline at 0
  rollingChart.addLineSeries({ color: "#2a2e3988", lineWidth: 1, lineStyle: 2, priceScaleId: "right" })
    .setData([]);

  // Live equity — mismo estilo que la equity shadow
  liveEqChart = makeLWChart("live-equity-chart");
  liveEqArea = liveEqChart.addAreaSeries({
    lineColor: "#26a69a", topColor: "#26a69a44", bottomColor: "#26a69a00",
    lineWidth: 2, priceFormat: { type: "price", precision: 2, minMove: 0.01 },
    title: "$",
  });

  // Live daily PnL histogram
  liveDailyChart = makeLWChart("live-daily-chart", { timeScale: { visible: true } });
  liveDailySeries = liveDailyChart.addHistogramSeries({
    color: "#26a69a", priceFormat: { type: "price", precision: 2, minMove: 0.01 },
  });

  // Responsive
  window.addEventListener("resize", () => {
    for (const [id, chart] of [
      ["equity-chart", eqChart], ["daily-chart", dailyChart],
      ["price-chart", priceChart], ["rolling-chart", rollingChart],
      ["live-equity-chart", liveEqChart], ["live-daily-chart", liveDailyChart]
    ]) {
      const el = document.getElementById(id);
      if (el) chart.applyOptions({ width: el.offsetWidth });
    }
  });
}

// ─── Filtrar por período ──────────────────────────────────────────────────────
function filterByPeriod(arr, period) {
  if (!period) return arr;
  const cutoff = Date.now() / 1000 - period * 86400;
  return arr.filter(pt => pt.time >= cutoff);
}

function filterDailyByPeriod(arr, period) {
  if (!period) return arr;
  const now = new Date();
  const cutoff = new Date(now - period * 86400000).toISOString().slice(0, 10);
  return arr.filter(pt => pt.time >= cutoff);
}

// ─── Render Live ─────────────────────────────────────────────────────────────
function renderLive(live) {
  if (!live) return;
  const fmtPnl = v => {
    const cls = v > 0 ? "pos" : v < 0 ? "neg" : "neu";
    return `<span class="${cls}">${v > 0 ? "+" : ""}${v.toFixed(2)}$</span>`;
  };
  const fmtPct = v => {
    const cls = v > 0 ? "pos" : v < 0 ? "neg" : "neu";
    return `<span class="${cls}">${v > 0 ? "+" : ""}${v.toFixed(2)}%</span>`;
  };
  // Switch badge
  const badge = document.getElementById("live-switch-badge");
  if (live.switch) {
    badge.textContent = "🟢 LIVE ON";
    badge.style.background = "#26a69a33";
    badge.style.color = "#26a69a";
    badge.style.border = "1px solid #26a69a66";
  } else {
    badge.textContent = "⚫ LIVE OFF";
    badge.style.background = "#ffffff11";
    badge.style.color = "#888";
    badge.style.border = "1px solid #ffffff22";
  }
  // TODAS las cifras de dinero son REALES (wallet on-chain). Fail-closed: si el
  // dato real no está fresco, mostramos "n/d" en vez de la cifra de plan.
  const nd = `<span class="neu">n/d</span>`;
  const fmtOr = (v) => (v != null ? fmtPnl(v) : nd);
  // Depósito inicial (constante conocida, viene del snapshot real)
  document.getElementById("live-deposito").textContent =
    live.real_deposito != null ? `${live.real_deposito.toFixed(2)}$` : "25.44$";
  // Dinero actual = balance real del wallet
  document.getElementById("live-bankroll").textContent =
    live.real_total != null ? `${live.real_total.toFixed(2)}$` : "n/d";
  // PNL real total / hoy / 7 días — todo del wallet on-chain
  document.getElementById("live-pnl").innerHTML     = fmtOr(live.real_pnl);
  document.getElementById("live-pnl-hoy").innerHTML = fmtOr(live.real_hoy);
  document.getElementById("live-pnl-7d").innerHTML  = fmtOr(live.real_7d);
  // % de beneficio sobre el depósito inicial (no sobre el balance del día)
  document.getElementById("live-pct-total").innerHTML =
    live.real_pct_total != null ? fmtPct(live.real_pct_total) : nd;
  document.getElementById("live-pct-hoy").innerHTML =
    live.real_pct_hoy != null ? fmtPct(live.real_pct_hoy) : nd;
  // Win rate y trades (trades ejecutados reales, de trades.csv)
  document.getElementById("live-wr").textContent = live.n_closed ? `${live.win_rate}%` : "—";
  document.getElementById("live-trades-count").textContent =
    `${(live.n_closed || 0) + (live.n_open || 0)} · ${live.n_open || 0} ab.`;
  const feesEl = document.getElementById("live-fees-total");
  if (feesEl) {
    const ft = live.fees_total || 0;
    const sinConf = live.fees_sin_confirmar || 0;
    feesEl.innerHTML = `${ft.toFixed(2)}$${sinConf > 0 ? ` <span style="font-size:9px;color:var(--muted)" title="${sinConf} trade(s) sin fee confirmado on-chain">⚠${sinConf}</span>` : ""}`;
  }
  // Nota discreta con la estimación del modelo (plan) y su desvío vs real.
  const notaEl = document.getElementById("live-modelo-nota");
  if (notaEl) {
    if (live.tracking_error != null) {
      const cls = Math.abs(live.tracking_error) < 0.5 ? "neu" : "neg";
      notaEl.innerHTML = `ℹ️ Referencia — estimación del modelo (trades.csv, precio de plan): PNL total ${live.pnl_total > 0 ? "+" : ""}${live.pnl_total.toFixed(2)}$ · desvío vs real <span class="${cls}">Δ ${live.tracking_error > 0 ? "+" : ""}${live.tracking_error.toFixed(2)}$</span> (el modelo no descuenta slippage/liquidación; vale el real).`;
    } else { notaEl.innerHTML = "&nbsp;"; }
  }
  const freshEl = document.getElementById("live-real-freshness");
  if (freshEl) {
    if (live.real_ts) freshEl.textContent = `balance on-chain: ${live.real_ts.replace("T", " ").slice(0, 16)}Z`;
    else if (live.real_stale) freshEl.textContent = "balance on-chain: ⚠️ rancio (>1h)";
    else freshEl.textContent = "balance on-chain: n/d";
  }

  // Chart de capital real: live.real_history ya viene fusionado desde el backend
  // (backbone diario desde el lanzamiento + snapshot ~15min reciente donde hay
  // dato fino). Fallback solo si el backend no pudo construirlo por lo que sea.
  const dep = live.real_deposito != null ? live.real_deposito : 25.44;
  if (live.real_history && live.real_history.length) {
    if (liveEqArea) {
      liveEqArea.setData(live.real_history);
      liveEqChart.timeScale().fitContent();
    }
  } else if (live.real_daily && live.real_daily.length) {
    let acc = dep;
    const eqReal = live.real_daily.map(d => { acc += d.pnl; return { time: d.date, value: +acc.toFixed(2) }; });
    // punto de arranque = depósito el día previo al primer trade
    eqReal.unshift({ time: live.real_daily[0].date, value: dep });
    if (liveEqArea) {
      liveEqArea.setData(eqReal);
      liveEqChart.timeScale().fitContent();
    }
  }
  // Barras diarias — SIEMPRE desde real_daily (independiente de si el
  // histórico granular está disponible arriba, es "el diario" que se pidió
  // mantener además del histórico completo).
  if (live.real_daily && live.real_daily.length && liveDailySeries) {
    liveDailySeries.setData(live.real_daily.map(d => ({
      time: d.date, value: +d.pnl.toFixed(2),
      color: d.pnl >= 0 ? "#26a69a" : "#ef5350",
    })));
    liveDailyChart.timeScale().fitContent();
  }

  // Barras por estrategia live (ventaja) + $/trade — mismas funciones que shadow
  if (live.by_strategy?.length) {
    renderBars("live-strat-bars", live.by_strategy, d => simpleName(d.name), d => d.ic,
      () => true, d => `${d.ic >= 0 ? "+" : ""}${(d.ic*100).toFixed(1)}%`, d => `${d.n} tr.`);
    const sortedAvg = [...live.by_strategy].sort((a, b) => b.avg - a.avg);
    renderBars("live-perbet-bars", sortedAvg, d => simpleName(d.name), d => d.avg,
      () => true, d => `${d.avg >= 0 ? "+" : ""}${d.avg.toFixed(3)}$`, d => `${d.n} tr.`);
  }
  // Tabla trades
  const tbody = document.getElementById("live-trades-body");
  if (!live.recent_trades || live.recent_trades.length === 0) {
    tbody.innerHTML = '<tr><td colspan="9" style="color:var(--muted);text-align:center">Sin trades aún</td></tr>';
    return;
  }
  tbody.innerHTML = live.recent_trades.map(t => {
    const pnl = t.pnl_neto_eur ? parseFloat(t.pnl_neto_eur) : null;
    const pnlBruto = t.pnl_bruto_eur ? parseFloat(t.pnl_bruto_eur) : null;
    const feeConfirmado = (t.notas || "").includes("fee_confirmado=1");
    const tooltipPnl = pnlBruto !== null
      ? `bruto ${pnlBruto>=0?"+":""}${pnlBruto.toFixed(2)}$ − fee ${parseFloat(t.fee_eur||0).toFixed(4)}$ = neto`
      : "";
    const pnlHtml = pnl !== null && t.status === "CLOSED"
      ? `<span class="${pnl>0?"pos":"neg"}" title="${tooltipPnl}">${pnl>0?"+":""}${pnl.toFixed(2)}$</span>`
      : "—";
    const feeVal = t.fee_eur ? parseFloat(t.fee_eur) : 0;
    const feeHtml = t.status === "CLOSED"
      ? `<span style="color:var(--muted)" title="${feeConfirmado ? "confirmado on-chain" : "sin confirmar, puede quedar bajo lo real"}">${feeVal.toFixed(3)}$${feeConfirmado ? "" : "⚠"}</span>`
      : "—";
    const hora = (t.timestamp_utc || "").slice(11, 16);
    const q = (t.question || "").slice(0, 45);
    const statusColor = t.status === "OPEN" ? "#f5a623" : t.status === "CLOSED" ? "#26a69a" : "#888";
    return `<tr>
      <td>${hora}</td>
      <td>${t.strategy}#${t.subtype}</td>
      <td title="${t.question}">${q}…</td>
      <td><b>${t.direction}</b></td>
      <td>${parseFloat(t.stake_eur||0).toFixed(2)}$</td>
      <td>${parseFloat(t.entry_price||0).toFixed(3)}</td>
      <td>${feeHtml}</td>
      <td style="color:${statusColor}">${t.status}</td>
      <td>${pnlHtml}</td>
    </tr>`;
  }).join("");
}

// ─── Render ───────────────────────────────────────────────────────────────────
function renderAll() {
  if (!DATA) return;
  const { stats, equity_curve, daily_pnl, by_hour, by_strategy,
          by_asset, rolling_ic, prices, btc_markers, ventanas_perf, live } = DATA;
  renderLive(live);

  // Stats
  const fmt = (v, prefix="") => {
    const cls = v > 0 ? "pos" : v < 0 ? "neg" : "neu";
    return `<span class="${cls}">${prefix}${v > 0 ? "+" : ""}${v.toFixed(2)}$</span>`;
  };
  document.getElementById("s-bankroll").innerHTML = `${stats.bankroll.toFixed(2)}$`;
  document.getElementById("s-pnl").innerHTML      = fmt(stats.pnl_total);
  if (stats.pnl_realista != null)
    document.getElementById("s-pnl-real").innerHTML = fmt(stats.pnl_realista);
  document.getElementById("s-pnl-hoy").innerHTML  = fmt(stats.pnl_hoy);
  document.getElementById("s-pnl-7d").innerHTML   = fmt(stats.pnl_7d);
  document.getElementById("s-wr").textContent     = `${stats.win_rate}%`;
  document.getElementById("s-ops").textContent    = `${stats.n_ops} (${stats.n_hoy})`;
  document.getElementById("update-badge").textContent = `Actualizado: ${stats.updated} · refresco automático cada 60s`;

  // Equity curve
  const eqData = filterByPeriod(equity_curve, PERIOD);
  if (eqData.length) {
    // Rebase al inicio del período
    const base = eqData[0].value;
    eqArea.setData(PERIOD ? eqData.map(p => ({...p, value: p.value - base + 20})) : eqData);
    eqChart.timeScale().fitContent();
  }

  // Daily PnL
  const dpData = filterDailyByPeriod(daily_pnl, PERIOD);
  dailySeries.setData(dpData);
  dailyChart.timeScale().fitContent();

  // Prices (últimos N días)
  const pDays = PERIOD || 7;
  const pCutoff = Date.now() / 1000 - pDays * 86400;
  if (prices.BTC?.length) btcLine.setData(prices.BTC.filter(p => p.time >= pCutoff));
  if (prices.ETH?.length) ethLine.setData(prices.ETH.filter(p => p.time >= pCutoff));
  if (prices.SOL?.length) solLine.setData(prices.SOL.filter(p => p.time >= pCutoff));
  // BTC markers
  if (btc_markers?.length) btcLine.setMarkers(btc_markers.filter(m => m.time >= pCutoff).slice(-200));
  priceChart.timeScale().fitContent();

  // Rolling IC — nombres legibles en la leyenda
  const legEl = document.getElementById("legend");
  legEl.innerHTML = "";
  let ci = 0;
  // Elimina series antiguas
  for (const k in rollingSeries) { try { rollingChart.removeSeries(rollingSeries[k]); } catch(e){} }
  rollingSeries = {};
  for (const [k, pts] of Object.entries(rolling_ic).slice(0, 6)) {
    const color = COLORS[ci++ % COLORS.length];
    const series = rollingChart.addLineSeries({ color, lineWidth: 1.5, title: k });
    const filtered = filterByPeriod(pts, PERIOD);
    if (filtered.length) series.setData(filtered);
    rollingSeries[k] = series;
    legEl.innerHTML += `<div class="legend-item"><div class="legend-dot" style="background:${color}"></div><span>${simpleName(k)}</span></div>`;
  }
  rollingChart.timeScale().fitContent();

  // Barras de hora
  const hourEl = document.getElementById("hour-bars");
  const maxAbsIC = Math.max(...by_hour.map(h => Math.abs(h.ic)), 0.01);
  hourEl.innerHTML = by_hour.map(h => {
    const pct  = Math.abs(h.ic) / maxAbsIC * 100;
    const color = h.blacklisted ? "#ef535077"
                : h.ic > 0 ? `#26a69a${Math.round(40 + pct * 0.6).toString(16)}` : "#ef535077";
    const bl    = h.blacklisted ? " hour-bl" : "";
    const tip   = `${h.hour}:00h UTC${h.blacklisted?" — BLOQUEADA":""} | Ventaja: ${h.ic>=0?"+":""}${(h.ic*100).toFixed(1)}% | Apuestas: ${h.n} | Aciertos: ${h.wr}% | Beneficio: ${h.pnl>=0?"+":""}${h.pnl}$`;
    return `<div class="hour-bar-wrap${bl}" title="${tip}">
      <div class="hour-bar" style="height:${Math.max(4, pct * 0.9)}px;background:${color}"></div>
      <div class="hour-label">${String(h.hour).padStart(2,"0")}</div>
    </div>`;
  }).join("");

  // Ventanas
  const ventEl = document.getElementById("ventanas");
  ventEl.innerHTML = ventanas_perf.map(v => {
    const cls = v.ic > 0 ? "pos-card" : v.ic < 0 ? "neg-card" : "";
    const icColor = v.ic > 0 ? "var(--green)" : v.ic < 0 ? "var(--red)" : "var(--text)";
    return `<div class="ventana-card ${cls}">
      <div class="ventana-time">${v.label}</div>
      <div class="ventana-ic" style="color:${icColor}">${v.ic > 0 ? "+" : ""}${(v.ic*100).toFixed(1)}%</div>
      <div class="ventana-sub">${v.wr}% aciertos · ${v.n} apuestas · ${v.pnl >= 0 ? "+" : ""}${v.pnl}$</div>
    </div>`;
  }).join("");

  // Barras estrategia
  renderBars("strat-bars", by_strategy, d => simpleName(d.name), d => d.ic, d => d.activa,
    d => `${d.ic >= 0 ? "+" : ""}${(d.ic*100).toFixed(1)}%`, d => `${d.n} ap.`);

  // Barras activo
  renderBars("asset-bars", by_asset, d => d.asset, d => d.ic, () => true,
    d => `${d.ic >= 0 ? "+" : ""}${(d.ic*100).toFixed(1)}%`, d => `${d.n} ap.`);

  // Tabla de estrategias
  const tblBody = document.getElementById("strat-table");
  tblBody.innerHTML = by_strategy.slice(0, 30).map(s => {
    const icColor = s.ic > 0 ? "var(--green)" : s.ic < 0 ? "var(--red)" : "var(--text)";
    const pColor  = s.pnl > 0 ? "var(--green)" : s.pnl < 0 ? "var(--red)" : "var(--text)";
    const rowStyle = s.activa ? "" : "style='opacity:.5'";
    return `<tr ${rowStyle}>
      <td title="${s.name}">${s.activa ? "✅" : "🚫"} ${simpleName(s.name)}</td>
      <td>${s.n}</td>
      <td>${s.wr}%</td>
      <td style="color:${icColor}">${s.ic >= 0 ? "+" : ""}${(s.ic*100).toFixed(1)}%</td>
      <td style="color:${pColor}">${s.pnl >= 0 ? "+" : ""}${s.pnl}$</td>
    </tr>`;
  }).join("");

  renderPerBet(DATA.per_bet);
}

function renderBars(elId, data, labelFn, icFn, activaFn, valFn, nFn) {
  const el = document.getElementById(elId);
  const maxIC = Math.max(...data.map(d => Math.abs(icFn(d))), 0.001);
  el.innerHTML = data.slice(0, 18).map(d => {
    const ic     = icFn(d);
    const pct    = Math.abs(ic) / maxIC * 100;
    const color  = ic > 0 ? "var(--green)" : "var(--red)";
    const activa = activaFn(d);
    return `<div class="bar-row">
      <div class="bar-label ${activa ? "" : "inactive"}" title="${labelFn(d)}">${labelFn(d)}</div>
      <div class="bar-track">
        <div class="bar-fill" style="width:${pct}%;background:${color}${ic < 0 ? "88" : ""}"></div>
      </div>
      <div class="bar-val" style="color:${color}">${valFn(d)}</div>
      <div class="bar-n">${nFn(d)}</div>
    </div>`;
  }).join("");
}

function renderPerBet(per_bet) {
  if (!per_bet) return;
  const { avg_total, avg_win, avg_loss, ratio, dist, by_strategy } = per_bet;

  // Stats
  const avgEl = document.getElementById("pb-avg");
  avgEl.textContent = `${avg_total >= 0 ? "+" : ""}${avg_total.toFixed(4)}$`;
  avgEl.style.color = avg_total >= 0 ? "var(--green)" : "var(--red)";

  document.getElementById("pb-ratio").textContent = `${ratio.toFixed(2)}x`;
  document.getElementById("pb-win").textContent   = `+${avg_win.toFixed(3)}$`;
  document.getElementById("pb-loss").textContent  = `${avg_loss.toFixed(3)}$`;

  // Distribución
  const distEl = document.getElementById("pb-dist");
  const maxPct = Math.max(...dist.map(d => d.pct), 1);
  distEl.innerHTML = dist.map(d => {
    const color = d.pos ? "var(--green)" : "var(--red)";
    const opacity = d.pos ? "" : "88";
    return `<div class="bar-row" style="margin-bottom:7px">
      <div class="bar-label" style="width:110px;font-size:11px">${d.label}</div>
      <div class="bar-track">
        <div class="bar-fill" style="width:${d.pct/maxPct*100}%;background:${color}${opacity}"></div>
      </div>
      <div class="bar-val" style="color:${color};width:44px">${d.pct}%</div>
      <div class="bar-n">${d.n} ap.</div>
    </div>`;
  }).join("");

  // Por estrategia (avg $/apuesta)
  const stratEl = document.getElementById("pb-strat");
  const maxAvg = Math.max(...by_strategy.map(d => Math.abs(d.avg)), 0.01);
  stratEl.innerHTML = by_strategy.slice(0, 16).map(d => {
    const color  = d.avg >= 0 ? "var(--green)" : "var(--red)";
    const pct    = Math.abs(d.avg) / maxAvg * 100;
    const label  = simpleName(d.name);
    const opacity = d.activa ? "" : "88";
    return `<div class="bar-row">
      <div class="bar-label ${d.activa ? "" : "inactive"}" title="${d.name}" style="width:150px">${label}</div>
      <div class="bar-track">
        <div class="bar-fill" style="width:${pct}%;background:${color}${opacity}"></div>
      </div>
      <div class="bar-val" style="color:${color};width:64px">${d.avg >= 0 ? "+" : ""}${d.avg.toFixed(4)}$</div>
      <div class="bar-n">${d.n} ap.</div>
    </div>`;
  }).join("");
}

// ─── Tabs ────────────────────────────────────────────────────────────────────
document.querySelectorAll(".tab").forEach(tab => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
    tab.classList.add("active");
    PERIOD = parseInt(tab.dataset.period);
    renderAll();
  });
});

// ─── Nombres legibles para estrategias ───────────────────────────────────────
function simpleName(k) {
  return k
    .replace("ORDER_FLOW_5M#", "Flujo órdenes · ")
    .replace("UPDOWN_GBM_15M_TARDIO#", "Tendencia tardía 15m · ")
    .replace("UPDOWN_GBM#", "Tendencia · ")
    .replace("UPDOWN_OU_5M#", "Reversión · ")
    .replace("SMART_FLOW_1H#", "Flujo inteligente · ")
    .replace("WEEKLY_PRICE#", "Precio semanal · ")
    .replace("PRICE_TARGET_GBM#", "Precio objetivo · ")
    .replace("RESOLUTION_SNIPER#", "Sniper · ")
    .replace("ORDER_FLOW_5M", "Flujo de órdenes")
    .replace("UPDOWN_GBM", "Tendencia GBM")
    .replace("WEEKLY_PRICE", "Precio semanal")
    .replace("#5min", " 5min")
    .replace("#15min", " 15min")
    .replace("#60min", " 1 hora")
    .replace("#240min", " 4 horas")
    .replace("#daily", " diario")
    .replace("#atexpiry", " al vencer")
    .replace("#reach", " alcance")
    .replace("#sniper", " sniper");
}

// ─── Boot ────────────────────────────────────────────────────────────────────
let _lastUpdated = "";
async function fetchData() {
  try {
    const r = await fetch("/api/data");
    const d = await r.json();
    const newTs = d?.stats?.updated || "";
    if (newTs !== _lastUpdated) {
      DATA = d;
      _lastUpdated = newTs;
      renderAll();
    }
    document.getElementById("update-badge").textContent = newTs ? `🟢 ${newTs}` : "";
  } catch(e) {
    document.getElementById("update-badge").textContent = "⚠️ sin conexión";
  }
}
initCharts();
fetchData();
setInterval(fetchData, 1_000);
</script>
</body>
</html>"""

# ─── Servidor HTTP ────────────────────────────────────────────────────────────

_LC_JS = (STATIC_DIR / "lc.js").read_bytes() if (STATIC_DIR / "lc.js").exists() else b""

class Handler(BaseHTTPRequestHandler):
    def _autenticado(self) -> bool:
        if not DASHBOARD_USER or not DASHBOARD_PASS:
            return True  # sin credenciales configuradas → no bloquear (fallback)
        header = self.headers.get("Authorization", "")
        if not header.startswith("Basic "):
            return False
        try:
            decoded = base64.b64decode(header[6:]).decode("utf-8")
            user, _, pw = decoded.partition(":")
        except Exception:
            return False
        # Comparación en tiempo constante para evitar timing attacks
        return hmac.compare_digest(user, DASHBOARD_USER) and hmac.compare_digest(pw, DASHBOARD_PASS)

    def _pedir_auth(self):
        self.send_response(401)
        self.send_header("WWW-Authenticate", 'Basic realm="Polymarket Dashboard"')
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Autenticacion requerida")

    def do_GET(self):
        if not self._autenticado():
            self._pedir_auth()
            return
        if self.path == "/api/data":
            body = json.dumps(get_data()).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", len(body))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(body)
        elif self.path in ("/", "/index.html"):
            body = HTML.encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", len(body))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/lc.js":
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript")
            self.send_header("Content-Length", len(_LC_JS))
            self.send_header("Cache-Control", "public, max-age=86400")
            self.end_headers()
            self.wfile.write(_LC_JS)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, fmt, *args):
        ts = datetime.now(timezone.utc).strftime("%H:%M:%S")
        print(f"[{ts}] {fmt % args}", flush=True)

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True
    address_family  = socket.AF_INET6   # AF_INET6 soporta dual-stack IPv4+IPv6

if __name__ == "__main__":
    srv = ThreadedHTTPServer(("::", PORT), Handler)
    print(f"Dashboard → http://0.0.0.0:{PORT}  (IPv4+IPv6)", flush=True)
    print(f"Acceso directo: http://<VPS_IP>:{PORT}", flush=True)
    print(f"SSH tunnel:     ssh -L {PORT}:localhost:{PORT} root@<VPS_IP>", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass
