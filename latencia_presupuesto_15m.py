#!/usr/bin/env python3
"""latencia_presupuesto_15m.py -- MISIÓN DEFINITIVA 15m (Javi 07-Oct), puntos 3-4: LATENCY BUDGET por etapa, PASIVO
(no envía ninguna orden). Cadena: market event -> receive -> parse -> detect -> decide -> construct -> sign -> send ->
exchange -> match -> fill. Este script mide las etapas que se pueden medir sin órdenes reales:
  A. event -> receive: registro ms (libro_estado_ws hijo). Filas q (top del libro, cada cambio de precio) y t
     (operaciones): hora del EXCHANGE vs hora de RECEPCIÓN; x (aggTrade Binance): T (operación) -> E (evento Binance)
     -> recepción. Por moneda#marco y por hora UTC (congestión). Reloj local: chrony (offset/RMS en la cabecera).
  B. parse: json.loads (y orjson si existe) de mensajes price_change de tamaño real (reconstruidos del registro).
  C. construct + sign: py-clob-client create_order() LOCAL (sin POST), en frío y en caliente.
  D. red hasta el CLOB: conexión nueva (DNS, TCP, TLS, TTFB) y conexión persistente (keep-alive), GET /time y GET /book;
     POP de Cloudflare (cf-ray).
Lo que NO se puede medir sin órdenes reales (send -> exchange -> match -> fill, retraso del tomador por tipo de orden)
queda para medir_latencia_ordenes_15m.py (requiere OK de Javi + /code-review).
Uso: (ulimit -v 3000000; nice -n 10 python3 latencia_presupuesto_15m.py [--fichero maker_ms_...csv.gz] [--max-filas N])
"""
import argparse
import collections
import glob
import gzip
import json
import os
import statistics
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
DATALOGS = Path("/root/polymarket-research-datalogs")
CLOB = "https://clob.polymarket.com"


def pct(v):
    v = np.asarray(v, dtype=float)
    v = v[~np.isnan(v)]
    if len(v) == 0:
        return "n=0"
    p = np.percentile(v, [50, 90, 95, 99])
    return f"n={len(v):>9} P50 {p[0]:7.1f}  P90 {p[1]:7.1f}  P95 {p[2]:7.1f}  P99 {p[3]:7.1f}  máx {v.max():8.1f}"


def etapa_a(fichero, max_filas):
    print(f"\n=== A. EVENTO -> RECEPCIÓN (ms) — {Path(fichero).name} ===")
    meta = {}
    q = collections.defaultdict(list)
    t = collections.defaultdict(list)
    xT, xE = collections.defaultdict(list), collections.defaultdict(list)
    qh = collections.defaultdict(list)
    n = 0
    with gzip.open(fichero, "rt", encoding="utf-8", errors="replace") as f:
        try:
            for ln in f:
                n += 1
                if max_filas and n > max_filas:
                    break
                c = ln.rstrip("\n").split(",")
                tp = c[0]
                try:
                    if tp == "k":
                        meta[c[2]] = (c[3], c[4])
                    elif tp == "q":
                        tex, rec = int(c[1]), int(c[7])
                        clave = "#".join(meta.get(c[2], ("?", "?")))
                        q[clave].append(rec - tex)
                        if clave.endswith("15min"):
                            qh[datetime.fromtimestamp(tex / 1000, timezone.utc).hour].append(rec - tex)
                    elif tp == "t":
                        clave = "#".join(meta.get(c[2], ("?", "?")))
                        t[clave].append(int(c[6]) - int(c[1]))
                    elif tp == "x":
                        s = c[2]
                        xT[s].append(int(c[6]) - int(c[1]))      # E - T dentro de Binance
                        xE[s].append(int(c[7]) - int(c[6]))      # recepción - E (red + nuestro socket)
                except (ValueError, IndexError):
                    continue
        except (EOFError, OSError):
            print("   (gzip truncado al final: se usa lo leído)")
    print(f"filas leídas {n:,}")
    print("Polymarket TOP del libro (q): recepción − hora del exchange")
    for k in sorted(q):
        if k.endswith("15min") or k.endswith("5min"):
            print(f"   {k:14} {pct(q[k])}")
    print("Polymarket OPERACIONES (t): recepción − hora del exchange")
    for k in sorted(t):
        if k.endswith("15min"):
            print(f"   {k:14} {pct(t[k])}")
    print("15m (q) por hora UTC (congestión): P50 / P99")
    print("   " + " ".join(f"{h:02d}:{np.percentile(v, 50):.0f}/{np.percentile(v, 99):.0f}" for h, v in sorted(qh.items()) if len(v) > 100))
    print("Binance aggTrade: E − T (interno Binance) | recepción − E (red + socket)")
    for s in sorted(xT):
        print(f"   {s:9} E−T  {pct(xT[s])}")
        print(f"   {'':9} rec−E {pct(xE[s])}")


def etapa_b():
    print("\n=== B. PARSE (µs por mensaje) ===")
    msg = {"event_type": "price_change", "market": "0x" + "ab" * 32, "timestamp": str(int(time.time() * 1000)),
           "price_changes": [{"asset_id": str(10 ** 76 + i), "price": "0.53", "size": "120.5", "side": "BUY",
                              "hash": "0x" + "cd" * 20, "best_bid": "0.52", "best_ask": "0.54"} for i in range(2)]}
    for nombre, cuerpo in (("price_change 2 cambios", json.dumps(msg)),
                           ("price_change 20 cambios", json.dumps({**msg, "price_changes": msg["price_changes"] * 10})),
                           ("book 30 niveles", json.dumps({"event_type": "book", "asset_id": "1" * 77,
                                                           "bids": [{"price": f"0.{i:02d}", "size": "100"} for i in range(30)],
                                                           "asks": [{"price": f"0.{99 - i:02d}", "size": "100"} for i in range(30)]}))):
        for lib in ("json", "orjson"):
            try:
                mod = __import__(lib)
            except ImportError:
                print(f"   {nombre:26} {lib:7} no instalado")
                continue
            N = 20000
            t0 = time.perf_counter()
            for _ in range(N):
                mod.loads(cuerpo)
            dt = (time.perf_counter() - t0) / N * 1e6
            print(f"   {nombre:26} {lib:7} {dt:7.1f} µs  ({len(cuerpo)} bytes)")


def etapa_c():
    print("\n=== C. CONSTRUCT + SIGN (ms), create_order LOCAL, sin POST ===")
    try:
        import live_trade as lt
        cli = lt._get_clob_client()
    except Exception as e:
        print(f"   no se pudo crear el cliente: {type(e).__name__}: {e}")
        return
    from py_clob_client_v2 import OrderArgsV2 as OrderArgs
    tok = None
    try:
        r = requests.get("https://gamma-api.polymarket.com/markets", params={"closed": "false", "limit": 50,
                         "order": "volume24hr", "ascending": "false"}, timeout=10).json()
        for m in r:
            ids = json.loads(m.get("clobTokenIds") or "[]")
            if ids and m.get("enableOrderBook"):
                tok = ids[0]
                break
    except Exception as e:
        print(f"   gamma falló: {e}")
    if not tok:
        print("   sin token de prueba")
        return
    tiempos = []
    for i in range(25):
        a = OrderArgs(token_id=tok, price=0.01, size=5.0, side="BUY")
        t0 = time.perf_counter()
        cli.create_order(a)
        tiempos.append((time.perf_counter() - t0) * 1000)
    print(f"   1ª (frío: tick/neg_risk/fee por red + firma) {tiempos[0]:.1f} ms")
    print(f"   caliente (cachés llenas, solo construir+firmar) {pct(tiempos[1:])}")


def etapa_d():
    print("\n=== D. RED HASTA EL CLOB (ms) ===")
    fmt = "%{time_namelookup} %{time_connect} %{time_appconnect} %{time_starttransfer} %{time_total}"
    filas = []
    for _ in range(20):
        try:
            o = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", fmt, f"{CLOB}/time"], capture_output=True,
                               text=True, timeout=10).stdout.split()
            filas.append([float(x) * 1000 for x in o])
        except Exception:
            pass
        time.sleep(0.2)
    if filas:
        A = np.array(filas)
        dns, tcp, tls, ttfb = A[:, 0], A[:, 1] - A[:, 0], A[:, 2] - A[:, 1], A[:, 3] - A[:, 2]
        print("   conexión NUEVA (curl):")
        for nom, v in (("DNS", dns), ("TCP connect", tcp), ("TLS", tls), ("TTFB (servidor + 1 RTT)", ttfb),
                       ("total", A[:, 4])):
            print(f"      {nom:26} {pct(v)}")
    s = requests.Session()
    s.get(f"{CLOB}/time", timeout=5)
    for ruta in ("/time", "/book?token_id="):
        if ruta.startswith("/book"):
            try:
                r = requests.get("https://gamma-api.polymarket.com/markets", params={"closed": "false", "limit": 5,
                                 "order": "volume24hr", "ascending": "false"}, timeout=10).json()
                ruta += json.loads(r[0]["clobTokenIds"])[0]
            except Exception:
                continue
        v, ray = [], None
        for _ in range(100):
            t0 = time.perf_counter()
            rr = s.get(f"{CLOB}{ruta}", timeout=5)
            v.append((time.perf_counter() - t0) * 1000)
            ray = rr.headers.get("cf-ray", ray)
            time.sleep(0.05)
        print(f"   keep-alive GET {ruta[:12]:12} {pct(v)}   (cf-ray {ray})")
    try:
        p = subprocess.run(["ping", "-c", "10", "-q", "clob.polymarket.com"], capture_output=True, text=True, timeout=20)
        print("   ICMP " + p.stdout.strip().splitlines()[-1])
    except Exception as e:
        print(f"   ping falló: {e}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichero", default=None)
    ap.add_argument("--max-filas", type=int, default=0)
    ap.add_argument("--etapas", default="ABCD")
    a = ap.parse_args()
    print(f"latencia_presupuesto_15m — {datetime.now(timezone.utc).isoformat(timespec='seconds')}")
    try:
        print(subprocess.run(["chronyc", "tracking"], capture_output=True, text=True).stdout.splitlines()[4:6])
    except Exception:
        pass
    if "A" in a.etapas:
        f = a.fichero or max(glob.glob(str(DATALOGS / "maker_ms_2026-*.csv.gz")), key=os.path.getsize)
        etapa_a(f, a.max_filas)
    if "B" in a.etapas:
        etapa_b()
    if "C" in a.etapas:
        etapa_c()
    if "D" in a.etapas:
        etapa_d()


if __name__ == "__main__":
    main()
