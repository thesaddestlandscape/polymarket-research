#!/usr/bin/env python3
"""fetch_hyperliquid_perps.py -- Hyperliquid como fuente para el modelo PERPS (05-Oct, Javi: "usar Hyperliquid para wallets
expertas, funding y liquidaciones"). API pública y gratuita (https://api.hyperliquid.xyz/info), solo lectura.

Por qué: de los 88 perps de Polymarket, 38 existen igual en el núcleo de Hyperliquid y casi todo el resto (acciones, oro,
plata, índices) en sus mercados HIP-3 (dex xyz/flx/km/hyna). Hyperliquid tiene 10-100x el interés abierto (es donde se forma
el precio), un leaderboard público (~47 k wallets, PnL/ROI/volumen por ventana) y posiciones públicas por wallet -- justo lo
que Polymarket Perps raciona (429). Cubre los pendientes #1 (precio de referencia), #2/#5 (wallets expertas por categoría),
#4 (funding) y #6 (precios de liquidación) de project_perps_pendientes_25sep.

Modos:
  ctx         (cron */5): funding, OI, mark, oráculo, mid, prima y volumen 24 h de cada instrumento (núcleo + HIP-3)
              -> datalogs hl_ctx_YYYY-MM-DD.csv.gz. Comparar con perps_tickers_*.csv (Polymarket) para el diferencial
              de funding entre venues (05-Oct, una foto: ±10..59 % anual en el mismo instrumento).
  posiciones  (cron horario): leaderboard (caché diaria data/shadow/hl_leaderboard_top.json) -> wallets "expertas" =
              PnL > 0 en semana Y mes, cuenta >= 25 k$, top N por PnL mensual; sus posiciones abiertas (núcleo + HIP-3):
              tamaño con signo, entrada, valor, PnL latente, apalancamiento, PRECIO DE LIQUIDACIÓN
              -> datalogs hl_posiciones_YYYY-MM-DD.csv.gz.
Cada ejecución escribe un miembro gzip COMPLETO (nunca truncado). Retención en scripts/comprimir_data_historica.sh.
Límite de la API: 1.200 de peso/min por IP; clearinghouseState pesa 2 -> se espacian las consultas.
"""
import gzip
import io
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
INFO = "https://api.hyperliquid.xyz/info"
LEADERBOARD = "https://stats-data.hyperliquid.xyz/Mainnet/leaderboard"
DEXES = [None, "xyz", "flx", "km", "hyna"]          # núcleo + HIP-3 que cubren acciones/commodities de Polymarket Perps
DATALOGS = Path("/root/polymarket-research-datalogs")
CACHE_LB = REPO / "data/shadow/hl_leaderboard_top.json"
N_EXPERTAS = 300
CUENTA_MIN = 25000.0
PAUSA_S = 0.12                                       # ~500 consultas/min de peso 2 = ~1.000 de peso: bajo el límite
SES = requests.Session()


def info(payload, intentos=3):
    for i in range(intentos):
        try:
            r = SES.post(INFO, json=payload, timeout=30)
            if r.status_code == 429:
                time.sleep(10 * (i + 1))
                continue
            r.raise_for_status()
            return r.json()
        except Exception as e:
            if i == intentos - 1:
                raise
            print(f"  reintento {payload.get('type')}: {type(e).__name__}: {e}", flush=True)
            time.sleep(2 * (i + 1))


def escribir(nombre, cabecera, filas):
    if not filas:
        return
    dia = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    ruta = DATALOGS / f"{nombre}_{dia}.csv.gz"
    buf = io.BytesIO()
    with gzip.GzipFile(fileobj=buf, mode="wb", compresslevel=6) as g:
        if not ruta.exists():
            g.write((cabecera + "\n").encode())
        g.write(("\n".join(",".join(str(x) for x in f) for f in filas) + "\n").encode())
    with open(ruta, "ab") as f:
        f.write(buf.getvalue())


def modo_ctx():
    ts = int(time.time())
    filas = []
    for dex in DEXES:
        p = {"type": "metaAndAssetCtxs"}
        if dex:
            p["dex"] = dex
        try:
            meta, ctx = info(p)
        except Exception as e:
            print(f"  ctx {dex}: {type(e).__name__}: {e}", flush=True)
            continue
        for u, c in zip(meta["universe"], ctx):
            filas.append((ts, dex or "", u["name"], c.get("funding"), c.get("openInterest"), c.get("markPx"),
                          c.get("oraclePx"), c.get("midPx"), c.get("premium"), c.get("dayNtlVlm")))
        time.sleep(PAUSA_S)
    escribir("hl_ctx", "ts,dex,coin,funding_h,open_interest,mark,oracle,mid,premium,vol24h_usd", filas)
    print(f"{datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ} ctx: {len(filas)} instrumentos", flush=True)


def expertas():
    hoy = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    try:
        c = json.loads(CACHE_LB.read_text())
        if c.get("dia") == hoy:
            return c["wallets"]
    except Exception:
        pass
    rows = SES.get(LEADERBOARD, timeout=60).json()["leaderboardRows"]
    cand = []
    for r in rows:
        w = dict(r.get("windowPerformances") or [])
        try:
            sem, mes, cuenta = float(w["week"]["pnl"]), float(w["month"]["pnl"]), float(r["accountValue"])
        except (KeyError, TypeError, ValueError):
            continue
        if sem > 0 and mes > 0 and cuenta >= CUENTA_MIN:
            cand.append((mes, r["ethAddress"], sem, cuenta, float(w.get("allTime", {}).get("pnl") or 0)))
    cand.sort(reverse=True)
    sel = [{"wallet": a, "pnl_mes": m, "pnl_semana": s, "cuenta": c, "pnl_total": t} for m, a, s, c, t in cand[:N_EXPERTAS]]
    CACHE_LB.write_text(json.dumps({"dia": hoy, "n_leaderboard": len(rows), "n_candidatas": len(cand), "wallets": sel}))
    return sel


def modo_posiciones():
    ts = int(time.time())
    sel = expertas()
    filas, n_err = [], 0
    for e in sel:
        for dex in DEXES:
            p = {"type": "clearinghouseState", "user": e["wallet"]}
            if dex:
                p["dex"] = dex
            try:
                st = info(p)
            except Exception:
                n_err += 1
                continue
            for ap in st.get("assetPositions") or []:
                q = ap.get("position") or {}
                lev = (q.get("leverage") or {}).get("value")
                filas.append((ts, e["wallet"], dex or "", q.get("coin"), q.get("szi"), q.get("entryPx"),
                              q.get("positionValue"), q.get("unrealizedPnl"), lev, q.get("liquidationPx")))
            time.sleep(PAUSA_S)
    escribir("hl_posiciones", "ts,wallet,dex,coin,size,entry,valor_usd,pnl_latente,apalancamiento,precio_liquidacion", filas)
    print(f"{datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ} posiciones: {len(sel)} wallets, {len(filas)} posiciones, "
          f"{n_err} errores", flush=True)


if __name__ == "__main__":
    modo = sys.argv[1] if len(sys.argv) > 1 else "ctx"
    {"ctx": modo_ctx, "posiciones": modo_posiciones}[modo]()
