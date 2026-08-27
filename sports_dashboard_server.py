#!/usr/bin/env python3
"""
sports_dashboard_server.py — Dashboard visual de sports/esports
Lanzar:  screen -dmS dash-sports python3 sports_dashboard_server.py
Acceso:  http://<VPS_IP>:8890  (HTTP Basic Auth, mismas credenciales que
         el dashboard de cripto -- decisión explícita Javi 18-Ago)

SEPARACIÓN ESTRICTA de cripto (18-Ago): prefijo sports_, solo lee
data/sports/ (nunca data/shadow/ ni data/live/, esos son de cripto).
Fase actual: solo descubrimiento de wallets (sports_wallet_edge_tracker.py)
-- todavía no hay ejecutor/tracker en tiempo real, así que este dashboard
muestra el estado de la inteligencia de wallets por categoría, no un PnL
de trading (no existe ninguno todavía, ni siquiera shadow).
"""
import base64
import hmac
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
from socketserver import ThreadingMixIn

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / "data" / "live" / ".env")  # mismas credenciales que cripto
except Exception:
    pass

DASHBOARD_USER = os.environ.get("DASHBOARD_USER", "")
DASHBOARD_PASS = os.environ.get("DASHBOARD_PASS", "")
if not DASHBOARD_USER or not DASHBOARD_PASS:
    print("[dashboard-sports] ⚠️  DASHBOARD_USER/DASHBOARD_PASS no configurados "
          "— el dashboard queda SIN AUTENTICACIÓN en la IP pública.")

REPO = Path(__file__).parent
DIR_SPORTS = REPO / "data" / "sports"
EDGE_JSON = DIR_SPORTS / "wallet_edge_score_por_categoria.json"
MIRROR_CSV = DIR_SPORTS / "wallet_mirror_sniper_dry_run.csv"  # 18-Ago
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8890

# 27-Ago: mismo static/lc.js (LightweightCharts) que dashboard_server.py
# (cripto) -- fichero único en el repo, ambos dashboards lo sirven.
_STATIC_DIR = REPO / "static"
_LC_JS = (_STATIC_DIR / "lc.js").read_bytes() if (_STATIC_DIR / "lc.js").exists() else b""


def compute_mirror():
    """18-Ago: el dashboard llevaba desde su creación (mañana) sin
    reflejar el Wallet Mirror en tiempo real desplegado por la tarde --
    Javi lo detectó preguntando directamente. Lee wallet_mirror_sniper_
    dry_run.csv (matches detectados, fill-ability, resolución).
    18-Ago (2ª pasada, petición Javi): tabla de señales recientes con
    detalle completo, mismo espíritu que la tabla de "live trades" del
    dashboard de cripto -- trazabilidad real, no solo agregados."""
    if not MIRROR_CSV.exists():
        return {"n_matches": 0, "n_resueltos": 0, "senales_recientes": []}
    import csv as _csv
    filas = list(_csv.DictReader(open(MIRROR_CSV, encoding="utf-8")))
    n = len(filas)
    senales_recientes = list(reversed(filas))[:50]
    resueltas = [r for r in filas if r.get("acierto") in ("0", "1")]
    n_res = len(resueltas)
    aciertos = sum(1 for r in resueltas if r["acierto"] == "1")
    con_libro = [r for r in filas if r.get("libro_ok") == "1"]

    def _ratio(r):
        try:
            return float(r.get("ratio_vs_stake_mirror") or 0)
        except (TypeError, ValueError):
            return 0.0
    fillable = [r for r in con_libro if _ratio(r) > 0]
    por_cat_wallet = defaultdict(set)
    for r in filas:
        por_cat_wallet[r.get("categoria", "")].add(r.get("wallet", ""))
    concentracion = [{"categoria": c, "n_wallets_activas": len(ws)}
                      for c, ws in sorted(por_cat_wallet.items(), key=lambda kv: len(kv[1]))]
    return {
        "n_matches": n, "n_seguir": sum(1 for r in filas if r.get("tipo") == "SEGUIR"),
        "n_fade": sum(1 for r in filas if r.get("tipo") == "FADE"),
        "n_resueltos": n_res,
        "hit_pct": round(aciertos / n_res * 100, 1) if n_res else None,
        "pct_libro_consultado": round(len(con_libro) / n * 100, 1) if n else 0,
        "pct_fillable": round(len(fillable) / len(con_libro) * 100, 1) if con_libro else 0,
        "concentracion_baja": [c for c in concentracion if c["n_wallets_activas"] == 1][:10],
        "senales_recientes": senales_recientes,
    }

TRADES_LIVE_CSV = DIR_SPORTS / "trades.csv"
CONFIG_LIVE_SPORTS = DIR_SPORTS / "config_live_sports.json"
SWITCH_LIVE_SPORTS = DIR_SPORTS / "LIVE_MODE_ON"


def compute_live():
    """27-Ago: sección Live -- mismo espíritu que compute_live_data() del
    dashboard de cripto, pero sports todavía no tiene dinero real
    desplegado (config_live_sports.json::depositos=[] hoy), así que se
    limita a lo que hay: estado del switch/circuit-breaker/whitelist +
    trades reales (0 hoy, tabla lista para cuando empiecen) + cuántas
    señales del sniper YA habrían disparado si el switch estuviera ON
    (columna decision_dry_run, útil para ver el ritmo real antes de
    mandar dinero)."""
    try:
        import sports_live_guard as _g
        import sports_live_stake as _s
        estado = _g.estado_live()
        bkr = _s.bankroll_actual()
        cb_disparado, cb_motivo = _s.verificar_circuit_breaker()
        pnl_hoy = _s.pnl_hoy()
    except Exception as e:
        return {"error": str(e)}

    trades = []
    if TRADES_LIVE_CSV.exists():
        import csv as _csv
        trades = list(_csv.DictReader(open(TRADES_LIVE_CSV, encoding="utf-8")))
    closed = [t for t in trades if t.get("status") == "CLOSED"]
    open_trades = [t for t in trades if t.get("status") == "OPEN"]
    pnl_total = sum(float(t.get("pnl_neto_eur") or 0) for t in closed)

    n_dispararia = 0
    if MIRROR_CSV.exists():
        import csv as _csv
        for r in _csv.DictReader(open(MIRROR_CSV, encoding="utf-8")):
            if r.get("decision_dry_run") == "DISPARARIA":
                n_dispararia += 1

    # ── Capital inicial (para la equity curve) ──────────────────────────
    capital_inicial = 0.0
    try:
        cfg = _g._cargar_config()
        capital_inicial = sum(float(d.get("eur", 0)) for d in cfg.get("depositos", []))
    except Exception:
        pass

    # ── Equity curve: un punto por trade CERRADO, ordenado por cierre ──
    closed_ord = sorted(closed, key=lambda t: t.get("close_timestamp") or t.get("timestamp_utc") or "")

    def _epoch(ts):
        try:
            from datetime import datetime, timezone
            s = (ts or "").replace("Z", "+00:00")
            dt = datetime.fromisoformat(s)
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return int(dt.timestamp())
        except Exception:
            return None

    equity = []
    bankroll_run = capital_inicial
    seen_ts = {}
    for t in closed_ord:
        ts = _epoch(t.get("close_timestamp") or t.get("timestamp_utc"))
        if ts is None:
            continue
        bankroll_run += float(t.get("pnl_neto_eur") or 0)
        seen_ts[ts] = round(bankroll_run, 4)  # dedup por segundo, LW exige tiempos crecientes
    equity = [{"time": ts, "value": v} for ts, v in sorted(seen_ts.items())]
    if equity:
        equity = [{"time": equity[0]["time"] - 1, "value": round(capital_inicial, 4)}] + equity

    # ── PnL diario ───────────────────────────────────────────────────────
    daily = defaultdict(lambda: {"pnl": 0.0, "n": 0, "wins": 0})
    for t in closed:
        d = (t.get("close_timestamp") or t.get("timestamp_utc") or "")[:10]
        if not d:
            continue
        pnl = float(t.get("pnl_neto_eur") or 0)
        daily[d]["pnl"] += pnl
        daily[d]["n"] += 1
        daily[d]["wins"] += 1 if pnl > 0 else 0
    daily_pnl = sorted([
        {"time": d, "value": round(v["pnl"], 4), "n": v["n"],
         "wr": round(v["wins"] / v["n"] * 100, 1) if v["n"] else 0,
         "color": "#26a69a" if v["pnl"] >= 0 else "#ef5350"}
        for d, v in daily.items()
    ], key=lambda x: x["time"])

    # ── Por categoría#tipo ───────────────────────────────────────────────
    por_cat = defaultdict(lambda: {"n": 0, "wins": 0, "pnl": 0.0})
    for t in closed:
        k = f"{t.get('categoria','?')}#{t.get('tipo','?')} {t.get('direction','')}"
        pnl = float(t.get("pnl_neto_eur") or 0)
        por_cat[k]["n"] += 1
        por_cat[k]["wins"] += 1 if pnl > 0 else 0
        por_cat[k]["pnl"] += pnl
    by_categoria = sorted([
        {"name": k, "n": v["n"],
         "wr": round(v["wins"] / v["n"] * 100, 1) if v["n"] else 0,
         "pnl": round(v["pnl"], 4)}
        for k, v in por_cat.items()
    ], key=lambda x: -abs(x["pnl"]))

    return {
        "switch": estado["switch"],
        "pares_permitidos": estado["pares_permitidos"],
        "bankroll": round(bkr, 2),
        "capital_inicial": round(capital_inicial, 2),
        "pnl_hoy": round(pnl_hoy, 2),
        "pnl_total_cerrado": round(pnl_total, 2),
        "equity_curve": equity,
        "daily_pnl": daily_pnl,
        "by_categoria": by_categoria,
        "circuit_breaker_disparado": cb_disparado,
        "circuit_breaker_motivo": cb_motivo,
        "n_trades_reales": len(trades),
        "n_open": len(open_trades),
        "n_closed": len(closed),
        "n_señales_dispararia_hoy": n_dispararia,
        "trades_recientes": sorted(trades, key=lambda t: t.get("timestamp_utc", ""), reverse=True)[:20],
    }


_cache = {"ts": 0.0, "data": None}
_CACHE_TTL = 30.0


def compute_data():
    if not EDGE_JSON.exists():
        return {"sin_datos": True}
    d = json.loads(EDGE_JSON.read_text(encoding="utf-8"))
    wallets = d.get("wallets_validadas", [])

    por_cat = defaultdict(list)
    for w in wallets:
        por_cat[w["categoria"]].append(w)

    resumen_categorias = []
    for cat, ws in sorted(por_cat.items(), key=lambda kv: -len(kv[1])):
        buenas = [w for w in ws if w["edge_pp"] > 0]
        malas = [w for w in ws if w["edge_pp"] <= 0]
        resumen_categorias.append({
            "categoria": cat, "n_wallets": len(ws),
            "n_buenas": len(buenas), "n_malas": len(malas),
            "mejor_edge": round(max((w["edge_pp"] for w in ws), default=0), 2),
            "n_trades_categoria": d.get("por_categoria_n_trades", {}).get(cat, 0),
        })

    top_wallets = sorted(wallets, key=lambda w: -w["edge_pp"])[:25]
    peores_wallets = sorted(wallets, key=lambda w: w["edge_pp"])[:15]

    return {
        "sin_datos": False,
        "actualizado_utc": d.get("actualizado_utc"),
        "ventana_dias": d.get("ventana_dias"),
        "n_trades_whale_clasificados": d.get("n_trades_whale_clasificados"),
        "n_trades_resueltos": d.get("n_trades_resueltos"),
        "n_wallets_especialistas": d.get("n_wallets_especialistas"),
        "n_combos_validados": len(wallets),
        "resumen_categorias": resumen_categorias,
        "top_wallets": top_wallets,
        "peores_wallets": peores_wallets,
        "mirror": compute_mirror(),
        "live": compute_live(),
    }


def get_data():
    import time as _time
    ahora = _time.time()
    if _cache["data"] is None or ahora - _cache["ts"] > _CACHE_TTL:
        _cache["data"] = compute_data()
        _cache["ts"] = ahora
    return _cache["data"]


PAGE_HTML = """<!doctype html><html><head><meta charset="utf-8">
<title>Sports/Esports — wallet intelligence</title>
<style>
body{background:#0b0f14;color:#e6edf3;font-family:system-ui,sans-serif;margin:0;padding:20px}
h1{font-size:20px;font-weight:600}
h2{font-size:15px;font-weight:600;margin-top:28px;color:#8b949e}
.stats{display:flex;gap:24px;margin:16px 0;flex-wrap:wrap}
.stat{background:#161b22;padding:12px 20px;border-radius:8px}
.stat .v{font-size:22px;font-weight:700}
.stat .l{font-size:12px;color:#8b949e}
table{border-collapse:collapse;width:100%;font-size:13px;margin-top:8px}
th,td{padding:6px 10px;text-align:right;border-bottom:1px solid #21262d}
th:first-child,td:first-child{text-align:left}
th{color:#8b949e;font-weight:500}
.pos{color:#3fb950}.neg{color:#f85149}
.badge{background:#1f6feb;color:#fff;padding:1px 6px;border-radius:4px;font-size:11px;margin-left:6px}
.aviso{background:#3a2a00;border:1px solid #9e6a03;padding:10px 14px;border-radius:6px;color:#f0b429;margin-bottom:16px}
/* ── mismo lenguaje visual que dashboard_server.py (cripto) ── */
.panel{background:#161b22;border-radius:8px;padding:14px}
.panel-title{font-size:11px;color:#8b949e;text-transform:uppercase;letter-spacing:.5px;margin-bottom:10px}
.chart-host{width:100%}
.grid-2{display:grid;grid-template-columns:2fr 1fr;gap:8px;margin:12px 0}
.grid-2b{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0}
.bar-row{display:flex;align-items:center;gap:8px;margin-bottom:5px;font-size:11px}
.bar-label{width:160px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:#e6edf3;flex-shrink:0}
.bar-track{flex:1;height:14px;background:#ffffff0a;border-radius:2px;position:relative;overflow:hidden}
.bar-fill{height:100%;border-radius:2px;transition:width .3s}
.bar-val{width:64px;text-align:right;flex-shrink:0}
.bar-n{width:36px;text-align:right;color:#8b949e;flex-shrink:0}
</style></head><body>
<h1>🏟️ Sports/Esports — inteligencia de wallets + Wallet Mirror en tiempo real (DRY_RUN)</h1>
<div class="aviso">Descubrimiento: ballenas ≥$1000 + firehose completo, shuffle test + BH-FDR. Wallet Mirror
(18-Ago): sniper en tiempo real con profundidad de libro real, 100% DRY_RUN, sin dinero real.</div>
<div class="stats" id="stats"></div>
<h2>💰 Live — dinero real</h2>
<div id="aviso-live"></div>
<div class="stats" id="stats-live"></div>
<div class="grid-2">
  <div class="panel">
    <div class="panel-title">📈 Evolución del capital real — un punto por trade cerrado</div>
    <div class="chart-host" id="live-equity-chart" style="height:200px"></div>
  </div>
  <div class="panel">
    <div class="panel-title">📊 PnL real por día</div>
    <div class="chart-host" id="live-daily-chart" style="height:200px"></div>
  </div>
</div>
<div class="panel" style="margin-bottom:12px">
  <div class="panel-title">🏆 PnL total por categoría (SEGUIR/FADE, dinero real)</div>
  <div id="live-cat-bars"><span style="color:#8b949e;font-size:11px">Sin datos aún — cero trades reales todavía</span></div>
</div>
<table><thead><tr><th>Hora</th><th>Categoría</th><th>Tipo</th><th>Dirección</th>
<th>Stake</th><th>Entrada</th><th>Estado</th><th>PnL</th></tr></thead>
<tbody id="tbody-live-trades"></tbody></table>
<h2>🪞 Wallet Mirror — actividad en tiempo real</h2>
<div class="stats" id="stats-mirror"></div>
<div id="aviso-concentracion"></div>
<h2>Señales recientes (trazabilidad)</h2>
<table><thead><tr><th>Hora (UTC)</th><th>Wallet</th><th>Categoría</th><th>Tipo</th>
<th>Precio</th><th>Lag(s)</th><th>Libro</th><th>Ratio/stake</th><th>Acierto</th></tr></thead>
<tbody id="tbody-senales"></tbody></table>
<h2>Por categoría</h2>
<table><thead><tr><th>Categoría</th><th>trades whale</th><th>wallets validadas</th>
<th>buenas</th><th>malas</th><th>mejor edge_pp</th></tr></thead><tbody id="tbody-cat"></tbody></table>
<h2>Top wallets informadas (mayor edge)</h2>
<table><thead><tr><th>Wallet</th><th>Categoría</th><th>n</th><th>hit%</th><th>edge_pp</th></tr></thead>
<tbody id="tbody-top"></tbody></table>
<h2>Peores wallets (candidatas a fade)</h2>
<table><thead><tr><th>Wallet</th><th>Categoría</th><th>n</th><th>hit%</th><th>edge_pp</th></tr></thead>
<tbody id="tbody-worst"></tbody></table>
<script src="/lc.js"></script>
<script>
let liveEqChart, liveEqArea, liveDailyChart, liveDailySeries;
function makeLWChart(id){
  const el = document.getElementById(id);
  return LightweightCharts.createChart(el, {
    width: el.offsetWidth, height: el.offsetHeight,
    layout: { background: { color: "transparent" }, textColor: "#787b86" },
    grid: { vertLines: { color: "#2a2e39" }, horzLines: { color: "#2a2e39" } },
    crosshair: { mode: LightweightCharts.CrosshairMode.Normal },
    rightPriceScale: { borderColor: "#2a2e39" },
    timeScale: { borderColor: "#2a2e39", timeVisible: true, secondsVisible: false },
  });
}
function initCharts(){
  liveEqChart = makeLWChart("live-equity-chart");
  liveEqArea = liveEqChart.addAreaSeries({
    lineColor: "#26a69a", topColor: "#26a69a44", bottomColor: "#26a69a00",
    lineWidth: 2, priceFormat: { type: "price", precision: 2, minMove: 0.01 }, title: "€",
  });
  liveDailyChart = makeLWChart("live-daily-chart");
  liveDailySeries = liveDailyChart.addHistogramSeries({
    color: "#26a69a", priceFormat: { type: "price", precision: 2, minMove: 0.01 },
  });
  window.addEventListener("resize", () => {
    for (const [id, chart] of [["live-equity-chart", liveEqChart], ["live-daily-chart", liveDailyChart]]) {
      const el = document.getElementById(id);
      if (el) chart.applyOptions({ width: el.offsetWidth });
    }
  });
}
function renderBars(elId, data){
  const el = document.getElementById(elId);
  if(!data || !data.length){
    el.innerHTML = '<span style="color:#8b949e;font-size:11px">Sin datos aún — cero trades reales todavía</span>';
    return;
  }
  const maxAbs = Math.max(...data.map(d => Math.abs(d.pnl)), 0.01);
  el.innerHTML = data.slice(0, 20).map(d => {
    const pct = Math.abs(d.pnl) / maxAbs * 100;
    const color = d.pnl >= 0 ? "#26a69a" : "#ef5350";
    return `<div class="bar-row">
      <div class="bar-label" title="${d.name}">${d.name}</div>
      <div class="bar-track"><div class="bar-fill" style="width:${pct}%;background:${color}"></div></div>
      <div class="bar-val" style="color:${color}">${d.pnl>=0?'+':''}${d.pnl.toFixed(2)}€</div>
      <div class="bar-n">n=${d.n}</div>
    </div>`;
  }).join("");
}
function renderLiveCharts(live){
  if(!live) return;
  const eq = live.equity_curve || [];
  liveEqArea.setData(eq);
  if(eq.length) liveEqChart.timeScale().fitContent();
  const daily = live.daily_pnl || [];
  liveDailySeries.setData(daily.map(p => ({ time: p.time, value: p.value, color: p.color })));
  if(daily.length) liveDailyChart.timeScale().fitContent();
  renderBars('live-cat-bars', live.by_categoria);
}
async function refresh(){
  const r = await fetch('/api/data'); const d = await r.json();
  if(d.sin_datos){
    document.getElementById('stats').innerHTML = '<div class="stat"><div class="v">Sin datos todavía</div></div>';
    return;
  }
  renderLiveCharts(d.live);
  document.getElementById('stats').innerHTML = `
    <div class="stat"><div class="v">${d.n_trades_whale_clasificados}</div><div class="l">trades whale (${d.ventana_dias}d)</div></div>
    <div class="stat"><div class="v">${d.n_trades_resueltos}</div><div class="l">con outcome resuelto</div></div>
    <div class="stat"><div class="v">${d.n_wallets_especialistas}</div><div class="l">wallets especialistas (&ge;80%% 1 categoría)</div></div>
    <div class="stat"><div class="v">${d.n_combos_validados}</div><div class="l">(wallet,categoría) con edge validado BH-FDR</div></div>
  `;
  const l = d.live || {};
  const switchTxt = l.switch ? '<span class="pos">ON</span>' : '<span class="neg">OFF</span>';
  const cbTxt = l.circuit_breaker_disparado ? '<span class="neg">DISPARADO</span>' : '<span class="pos">OK</span>';
  document.getElementById('stats-live').innerHTML = `
    <div class="stat"><div class="v">${switchTxt}</div><div class="l">switch live</div></div>
    <div class="stat"><div class="v">${(l.pares_permitidos||[]).length}</div><div class="l">micro-buckets en whitelist</div></div>
    <div class="stat"><div class="v">${l.bankroll!=null?l.bankroll.toFixed(2)+'€':'—'}</div><div class="l">bankroll actual</div></div>
    <div class="stat"><div class="v" style="color:${(l.pnl_hoy||0)>=0?'#3fb950':'#f85149'}">${l.pnl_hoy!=null?(l.pnl_hoy>=0?'+':'')+l.pnl_hoy.toFixed(2)+'€':'—'}</div><div class="l">PnL hoy</div></div>
    <div class="stat"><div class="v">${cbTxt}</div><div class="l">circuit breaker</div></div>
    <div class="stat"><div class="v">${l.n_trades_reales||0}</div><div class="l">trades reales (${l.n_open||0} abiertos)</div></div>
    <div class="stat"><div class="v">${l.n_señales_dispararia_hoy||0}</div><div class="l">señales que YA dispararían si switch=ON</div></div>
  `;
  document.getElementById('aviso-live').innerHTML = (l.pares_permitidos||[]).length===0
    ? '<div class="aviso">⚠️ Whitelist vacía -- fail-closed, ninguna señal puede operar con dinero real todavía.</div>'
    : (l.circuit_breaker_disparado ? `<div class="aviso">🛑 Circuit breaker disparado: ${l.circuit_breaker_motivo}</div>` : '');
  document.getElementById('tbody-live-trades').innerHTML = (l.trades_recientes||[]).map(t => {
    const pnl = t.pnl_neto_eur ? parseFloat(t.pnl_neto_eur) : null;
    return `<tr><td>${(t.timestamp_utc||'').replace('T',' ').slice(0,16)}</td><td>${t.categoria||''}</td>
      <td>${t.tipo||''}</td><td>${t.direction||''}</td><td>${t.stake_eur||''}€</td>
      <td>${t.entry_price||''}</td><td>${t.status||''}</td>
      <td class="${pnl>=0?'pos':'neg'}">${pnl!=null?pnl.toFixed(2)+'€':'—'}</td></tr>`;
  }).join('') || '<tr><td colspan="8" style="text-align:center;color:#8b949e">Sin trades reales todavía</td></tr>';
  const m = d.mirror || {};
  document.getElementById('stats-mirror').innerHTML = `
    <div class="stat"><div class="v">${m.n_matches||0}</div><div class="l">señales detectadas (${m.n_seguir||0} SEGUIR / ${m.n_fade||0} FADE)</div></div>
    <div class="stat"><div class="v">${m.n_resueltos||0}</div><div class="l">resueltas</div></div>
    <div class="stat"><div class="v">${m.hit_pct!=null?m.hit_pct+'%':'—'}</div><div class="l">hit-rate DRY_RUN</div></div>
    <div class="stat"><div class="v">${m.pct_fillable||0}%</div><div class="l">con profundidad real (de ${m.pct_libro_consultado||0}% con libro consultado)</div></div>
  `;
  const conc = (m.concentracion_baja||[]);
  document.getElementById('aviso-concentracion').innerHTML = conc.length
    ? `<div class="aviso">⚠️ ${conc.length} categorías con actividad de UNA sola wallet (riesgo de concentración): ${conc.map(c=>c.categoria).join(', ')}</div>`
    : '';
  document.getElementById('tbody-senales').innerHTML = (m.senales_recientes||[]).map(s => {
    const acierto = s.acierto==='1' ? '<span class="pos">✔</span>' : (s.acierto==='0' ? '<span class="neg">✘</span>' : '—');
    const libro = s.libro_ok==='1' ? '✅' : '❌';
    const ratio = s.ratio_vs_stake_mirror ? parseFloat(s.ratio_vs_stake_mirror).toFixed(2) : '—';
    const tipoClass = s.tipo === 'SEGUIR' ? 'pos' : 'neg';
    return `<tr><td>${(s.timestamp_utc||'').replace('T',' ').slice(0,19)}</td>
      <td>${(s.wallet||'').slice(0,14)}</td><td>${s.categoria||''}</td>
      <td class="${tipoClass}">${s.tipo||''}</td><td>${s.precio_wallet||''}</td>
      <td>${s.lag_deteccion_s||''}</td><td>${libro}</td><td>${ratio}</td><td>${acierto}</td></tr>`;
  }).join('');
  document.getElementById('tbody-cat').innerHTML = d.resumen_categorias.map(c =>
    `<tr><td>${c.categoria}</td><td>${c.n_trades_categoria}</td><td>${c.n_wallets}</td>
     <td class="pos">${c.n_buenas}</td><td class="neg">${c.n_malas}</td>
     <td class="${c.mejor_edge>=0?'pos':'neg'}">${c.mejor_edge>=0?'+':''}${c.mejor_edge}</td></tr>`).join('');
  document.getElementById('tbody-top').innerHTML = d.top_wallets.map(w =>
    `<tr><td>${w.wallet.slice(0,14)}${w.especialista?'<span class="badge">ESP</span>':''}</td>
     <td>${w.categoria}</td><td>${w.n}</td><td>${(w.hit*100).toFixed(1)}%</td>
     <td class="pos">+${w.edge_pp.toFixed(2)}</td></tr>`).join('');
  document.getElementById('tbody-worst').innerHTML = d.peores_wallets.map(w =>
    `<tr><td>${w.wallet.slice(0,14)}${w.especialista?'<span class="badge">ESP</span>':''}</td>
     <td>${w.categoria}</td><td>${w.n}</td><td>${(w.hit*100).toFixed(1)}%</td>
     <td class="neg">${w.edge_pp.toFixed(2)}</td></tr>`).join('');
}
initCharts(); refresh(); setInterval(refresh, 10000);
</script></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def _auth_ok(self):
        if not DASHBOARD_USER or not DASHBOARD_PASS:
            return True
        auth = self.headers.get("Authorization", "")
        if not auth.startswith("Basic "):
            return False
        try:
            user, pwd = base64.b64decode(auth[6:]).decode().split(":", 1)
        except Exception:
            return False
        return hmac.compare_digest(user, DASHBOARD_USER) and hmac.compare_digest(pwd, DASHBOARD_PASS)

    def do_GET(self):
        if not self._auth_ok():
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="sports-dashboard"')
            self.end_headers()
            return
        if self.path == "/api/data":
            body = json.dumps(get_data()).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        elif self.path == "/lc.js":
            # mismo static/lc.js que dashboard_server.py (cripto) -- un
            # único fichero de librería, servido por los dos dashboards.
            if not _LC_JS:
                self.send_response(404)
                self.end_headers()
                return
            self.send_response(200)
            self.send_header("Content-Type", "application/javascript")
            self.send_header("Content-Length", str(len(_LC_JS)))
            self.end_headers()
            self.wfile.write(_LC_JS)
        else:
            body = PAGE_HTML.encode()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

    def log_message(self, fmt, *args):
        pass


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True


def main():
    print(f"[dashboard-sports] arrancando en :{PORT}")
    server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    server.serve_forever()


if __name__ == "__main__":
    main()
