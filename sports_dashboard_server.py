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
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8890

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
</style></head><body>
<h1>🏟️ Sports/Esports — inteligencia de wallets (fase: descubrimiento, sin ejecución todavía)</h1>
<div class="aviso">Fase actual: solo detección de wallets con edge validado por categoría/deporte/liga
(ballenas ≥$1000, shuffle test + BH-FDR, mismo rigor que cripto). Todavía NO hay ejecutor/tracker en
tiempo real ni PnL de trading (ni shadow) — eso es el siguiente paso.</div>
<div class="stats" id="stats"></div>
<h2>Por categoría</h2>
<table><thead><tr><th>Categoría</th><th>trades whale</th><th>wallets validadas</th>
<th>buenas</th><th>malas</th><th>mejor edge_pp</th></tr></thead><tbody id="tbody-cat"></tbody></table>
<h2>Top wallets informadas (mayor edge)</h2>
<table><thead><tr><th>Wallet</th><th>Categoría</th><th>n</th><th>hit%</th><th>edge_pp</th></tr></thead>
<tbody id="tbody-top"></tbody></table>
<h2>Peores wallets (candidatas a fade)</h2>
<table><thead><tr><th>Wallet</th><th>Categoría</th><th>n</th><th>hit%</th><th>edge_pp</th></tr></thead>
<tbody id="tbody-worst"></tbody></table>
<script>
async function refresh(){
  const r = await fetch('/api/data'); const d = await r.json();
  if(d.sin_datos){
    document.getElementById('stats').innerHTML = '<div class="stat"><div class="v">Sin datos todavía</div></div>';
    return;
  }
  document.getElementById('stats').innerHTML = `
    <div class="stat"><div class="v">${d.n_trades_whale_clasificados}</div><div class="l">trades whale (${d.ventana_dias}d)</div></div>
    <div class="stat"><div class="v">${d.n_trades_resueltos}</div><div class="l">con outcome resuelto</div></div>
    <div class="stat"><div class="v">${d.n_wallets_especialistas}</div><div class="l">wallets especialistas (&ge;80%% 1 categoría)</div></div>
    <div class="stat"><div class="v">${d.n_combos_validados}</div><div class="l">(wallet,categoría) con edge validado BH-FDR</div></div>
  `;
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
refresh(); setInterval(refresh, 10000);
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
