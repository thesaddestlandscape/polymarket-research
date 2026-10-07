#!/usr/bin/env python3
"""medir_latencia_ordenes_15m.py -- MISIÓN DEFINITIVA 15m §3-4 (07-Oct): la parte ACTIVA del presupuesto de latencia.
⚠️ HERRAMIENTA MANUAL que ENVÍA ÓRDENES REALES. Nunca en cron/screen/watchdog. Requiere OK de Javi + /code-review.

Por qué: según docs.polymarket.com (order lifecycle) el taker delay SOLO se aplica a órdenes MARKETABLE. La medición
del 05-Oct (FOK a 0,02, 226 ms) NO era marketable -> nunca incluyó el retraso: la latencia real de un tomador está
SIN MEDIR. Pruebas (sobre el 15m vivo de la moneda de --moneda, por defecto btc; con >=150 s al cierre y >=60 s desde la apertura):
  T1 RESTING  : GTC post_only BUY 5 acciones a 0,01 (no puede cruzar; sin taker delay) -> acuse del POST; luego
                cancel por orderID -> acuse del DELETE; get_order para confirmar estado.
  T2 FOK_NM   : FOK BUY 1,05 $ a 0,02 (no marketable; réplica del 05-Oct) -> acuse.
  T3 FAK_MKT  : FAK BUY 5 acciones al MEJOR ASK del lado barato (ask en [0,20, 0,45] -> 5 acciones >= 1 $ (mínimo del CLOB), <=2,25 $ + comisión por orden) -> acuse,
                estado devuelto (matched/delayed/...) y HORA DEL EXCHANGE del print en el WS de mercado (mismo token,
                mismo precio, tamaño 5, primer print >= envío) -> envío->casado = red + validación + taker delay + casado.
SEGURIDAD (fail-closed):
  - Presupuesto duro: T3 <= MAX_T3 órdenes y <= MAX_EUR_T3 $ de coste total; T1/T2 no pueden costar nada (si T1 se
    rellenara, sería comprar a 0,01: asimétrico a favor).
  - Solo cancela órdenes cuyo orderID ha creado ESTE proceso (nunca cancel_all ni por mercado: hay ejecutores live).
  - Ledger de INTENCIÓN antes de cada POST (datalogs/medir_latencia_ordenes_15m_ledger.jsonl) y barrido final que
    cancela cualquier T1 propio que siga vivo.
  - Aborta si no hay libro, si el ask del lado elegido sale de banda, si falta poco para el cierre o si el cliente falla.
  - No escribe en trades.csv ni en ningún ledger del sistema live. Las posiciones de T3 se dejan a resolución.
Uso: python3 medir_latencia_ordenes_15m.py --t1 20 --t2 20 --t3 10 --confirmo-dinero-real
     (sin --confirmo-dinero-real solo hace un ensayo en seco: elige mercado y lado, construye y firma, NO envía).
"""
import argparse
import asyncio
import json
import statistics
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
LEDGER = Path("/root/polymarket-research-datalogs/medir_latencia_ordenes_15m_ledger.jsonl")
CLOB = "https://clob.polymarket.com"
WS = "wss://ws-subscriptions-clob.polymarket.com/ws/market"
MAX_T3, MAX_EUR_T3 = 10, 20.0
BANDA_T3 = (0.20, 0.45)          # 5 acciones x 0,20 = 1 $: mínimo del CLOB para una compra marketable
SIZE = 5.0


def log(ev):
    ev["ts"] = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
    with open(LEDGER, "a") as f:
        f.write(json.dumps(ev) + "\n")


def libro(tok):
    r = requests.get(f"{CLOB}/book", params={"token_id": tok}, timeout=5).json()
    bids = sorted(((float(x["price"]), float(x["size"])) for x in r.get("bids", [])), reverse=True)
    asks = sorted((float(x["price"]), float(x["size"])) for x in r.get("asks", []))
    return bids, asks


def mercado(moneda):
    """15m vivo de `moneda` con margen: (slug, cierre, [(tok, outcome)])"""
    ahora = time.time()
    ini = int(ahora // 900 * 900)
    fin = ini + 900
    if ahora - ini < 60 or fin - ahora < 150:
        return None
    for a in (moneda,):
        r = requests.get("https://gamma-api.polymarket.com/markets", params={"slug": f"{a}-updown-15m-{ini}"},
                         timeout=10).json()
        if r:
            m = r[0]
            toks = json.loads(m["clobTokenIds"])
            outs = json.loads(m["outcomes"])
            return m["slug"], fin, list(zip(toks, outs))
    return None


class Prints:
    """WS de mercado en un hilo: guarda (t_exchange_ms, t_recepcion_ms, asset, price, size) de last_trade_price."""

    def __init__(self, toks):
        self.toks, self.p, self.ok, self.vivo, self.error = toks, [], threading.Event(), False, None
        threading.Thread(target=self._hilo, daemon=True).start()
        if not self.ok.wait(10):
            raise RuntimeError(f"WS de mercado no conectó en 10 s: {self.error}")

    def _hilo(self):
        try:
            asyncio.run(self._run())
        except Exception as e:                      # fallo visible: T3 consulta self.vivo antes de cada orden
            self.error = f"{type(e).__name__}: {e}"
        self.vivo = False

    async def _run(self):
        import websockets
        async with websockets.connect(WS, ping_interval=20, max_queue=None) as ws:
            await ws.send(json.dumps({"assets_ids": self.toks, "type": "market"}))
            self.vivo = True
            self.ok.set()
            t_ping = time.time()
            while True:
                if time.time() - t_ping >= 10:      # el canal de mercado exige PING de TEXTO cada 10 s (fix 05-Oct)
                    await ws.send("PING")
                    t_ping = time.time()
                try:
                    raw = await asyncio.wait_for(ws.recv(), timeout=1.0)
                except asyncio.TimeoutError:
                    continue
                rec = int(time.time() * 1000)
                if not raw or raw == "PONG" or raw[0] not in "[{":
                    continue
                d = json.loads(raw)
                for m in (d if isinstance(d, list) else [d]):
                    if m.get("event_type") == "last_trade_price":
                        self.p.append((int(m.get("timestamp", 0)), rec, m.get("asset_id"), float(m.get("price", 0)),
                                       float(m.get("size", 0)), str(m.get("side", "")).upper()))

    def buscar(self, tok, limite, t_envio_ms, lleno, espera_s=4.0):
        """Primer print TOMADOR-COMPRA del token a precio <= límite con hora del exchange >= envío + 20 ms (antes es
        físicamente imposible: la ida al origen ya son ~25 ms). Devuelve (t_ex, t_rec, n_prints, suma, ambiguo).
        ambiguo = los prints compatibles en la ventana suman MÁS que lo que nos llenaron (hay otro tomador): se excluye."""
        time.sleep(espera_s)
        cand = [x for x in self.p if x[2] == tok and x[5] == "BUY" and x[3] <= limite + 1e-9
                and t_envio_ms + 20 <= x[0] <= t_envio_ms + 3000]
        if not cand:
            return None
        cand.sort()
        suma = sum(x[4] for x in cand)
        ambiguo = lleno is None or suma > lleno + 1e-6
        return cand[0][0], cand[0][1], len(cand), round(suma, 4), ambiguo


def resumen(nombre, xs):
    if not xs:
        print(f"{nombre:28} n=0")
        return
    s = sorted(xs)
    q = lambda f: s[min(len(s) - 1, int(f * len(s)))]
    print(f"{nombre:28} n={len(s):3} P50 {statistics.median(s):7.1f}  P90 {q(0.9):7.1f}  P95 {q(0.95):7.1f}  "
          f"P99 {q(0.99):7.1f}  máx {s[-1]:7.1f} ms")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--t1", type=int, default=0)
    ap.add_argument("--t2", type=int, default=0)
    ap.add_argument("--t3", type=int, default=0)
    ap.add_argument("--confirmo-dinero-real", action="store_true")
    ap.add_argument("--moneda", default="btc", choices=("btc", "eth", "sol", "xrp", "doge", "bnb"))
    a = ap.parse_args()
    real = a.confirmo_dinero_real
    if a.t3 > MAX_T3:
        sys.exit(f"t3 > {MAX_T3}")
    mk = mercado(a.moneda)
    if not mk:
        sys.exit("sin 15m vivo con margen (>=60 s desde apertura y >=150 s al cierre): reintentar en unos minutos")
    slug, fin, toks = mk
    import live_trade as lt
    from py_clob_client_v2 import OrderArgsV2, MarketOrderArgsV2, OrderType, OrderPayload
    cli = lt._get_clob_client()
    if cli is None:
        sys.exit("sin cliente CLOB")
    libros = {t: libro(t) for t, _ in toks}
    print(f"{'REAL' if real else 'ENSAYO EN SECO'} | {slug} | cierra en {fin - time.time():.0f} s")
    for t, o in toks:
        b, s_ = libros[t]
        print(f"   {o:5} bid {b[0] if b else None} ask {s_[0] if s_ else None}")
    # calentar cachés (tick, neg_risk, fee) y la firma
    t0 = time.perf_counter()
    cli.create_order(OrderArgsV2(token_id=toks[0][0], price=0.01, size=SIZE, side="BUY"))
    print(f"   firma de calentamiento {(time.perf_counter() - t0) * 1000:.0f} ms")
    R = {"t1_post": [], "t1_cancel": [], "t2_post": [], "t3_post": [], "t3_casado": [], "t3_recep": [], "firma": []}
    mios, huerfanas = [], []
    t_inicio = time.time()
    try:
        # ---- T1 resting
        tok1 = max(toks, key=lambda x: (libros[x[0]][0][0][0] if libros[x[0]][0] else 0))[0]
        if libros[tok1][0] and libros[tok1][0][0][0] >= 0.03:
            for i in range(a.t1):
                if fin - time.time() < 120:
                    break
                b1, _ = libro(tok1)
                if not b1 or b1[0][0] < 0.03:              # libro fresco: 0,01 nunca puede ser el mejor bid
                    print("   T1: bid < 0,03 ahora, parada")
                    break
                tf = time.perf_counter()
                o = cli.create_order(OrderArgsV2(token_id=tok1, price=0.01, size=SIZE, side="BUY"))
                R["firma"].append((time.perf_counter() - tf) * 1000)
                if not real:
                    continue
                log({"tipo": "T1_intencion", "tok": tok1, "i": i})
                t0 = time.perf_counter()
                try:
                    resp = cli.post_order(o, OrderType.GTC, post_only=True)
                except Exception as e:
                    log({"tipo": "T1_error", "e": str(e)[:200]})
                    huerfanas.append(tok1)              # el POST pudo entrar: el barrido final busca por token/precio/tamaño
                    print(f"   T1 error {type(e).__name__}: {str(e)[:80]} -> sigo")
                    time.sleep(1)
                    continue
                R["t1_post"].append((time.perf_counter() - t0) * 1000)
                oid = (resp or {}).get("orderID") or (resp or {}).get("orderId")
                log({"tipo": "T1_post", "oid": oid, "resp": str(resp)[:200], "ms": R["t1_post"][-1]})
                if oid:
                    mios.append(oid)
                    t0 = time.perf_counter()
                    cr = cli.cancel_order(OrderPayload(orderID=oid))
                    R["t1_cancel"].append((time.perf_counter() - t0) * 1000)
                    log({"tipo": "T1_cancel", "oid": oid, "resp": str(cr)[:200], "ms": R["t1_cancel"][-1]})
                time.sleep(0.3)
        else:
            print("   T1 omitido: ningún lado con bid >= 0,03 (0,01 podría ser el mejor bid)")
        # ---- T2 FOK no marketable
        tok2 = toks[0][0]
        ask2 = libros[tok2][1][0][0] if libros[tok2][1] else None
        if ask2 is not None and ask2 >= 0.10:
            for i in range(a.t2):
                if fin - time.time() < 120:
                    break
                _, a2 = libro(tok2)
                if not a2 or a2[0][0] < 0.10:              # libro fresco: 0,02 nunca puede cruzar
                    print("   T2: ask < 0,10 ahora, parada")
                    break
                o = cli.create_market_order(MarketOrderArgsV2(token_id=tok2, amount=1.05, side="BUY", price=0.02))
                if not real:
                    continue
                log({"tipo": "T2_intencion", "tok": tok2, "i": i})
                t0 = time.perf_counter()
                try:
                    resp = cli.post_order(o, OrderType.FOK)
                except Exception as e:
                    resp = f"{type(e).__name__}: {e}"
                R["t2_post"].append((time.perf_counter() - t0) * 1000)
                log({"tipo": "T2_post", "resp": str(resp)[:200], "ms": R["t2_post"][-1]})
                time.sleep(0.3)
        else:
            print(f"   T2 omitido: ask {ask2} < 0,10")
        # ---- T3 FAK marketable
        if a.t3:
            pr = Prints([t for t, _ in toks]) if real else None
            gastado = 0.0
            for i in range(a.t3):
                if fin - time.time() < 120:
                    print("   T3: poco tiempo al cierre, parada")
                    break
                if real and not pr.vivo:
                    print(f"   T3: WS de prints caído ({pr.error}) -> parada (no se envía sin poder medir)")
                    break
                cand = []
                for t, o_ in toks:
                    _, asks = libro(t)
                    if asks and BANDA_T3[0] <= asks[0][0] <= BANDA_T3[1] and asks[0][1] >= SIZE:
                        cand.append((asks[0][0], t, o_))
                if not cand:
                    print("   T3: ningún lado con ask en banda y >=5 acciones; espera 5 s")
                    time.sleep(5)
                    continue
                ask, tok3, out3 = min(cand)
                coste = ask * SIZE + 0.07 * ask * (1 - ask) * SIZE    # comisión real del tomador
                if ask * SIZE < 1.0:
                    print(f"   T3: {ask} x 5 < 1 $ (mínimo del CLOB), se descarta")
                    time.sleep(5)
                    continue
                if gastado + coste > MAX_EUR_T3:
                    print("   T3: presupuesto agotado")
                    break
                o = cli.create_order(OrderArgsV2(token_id=tok3, price=ask, size=SIZE, side="BUY"))
                if not real:
                    print(f"   [seco] T3 {out3} ask {ask} coste {coste:.2f}")
                    continue
                log({"tipo": "T3_intencion", "tok": tok3, "ask": ask, "i": i})
                t_env = int(time.time() * 1000)
                t0 = time.perf_counter()
                try:
                    resp = cli.post_order(o, OrderType.FAK)
                except Exception as e:
                    resp = f"{type(e).__name__}: {e}"
                R["t3_post"].append((time.perf_counter() - t0) * 1000)
                gastado += coste
                log({"tipo": "T3_post", "resp": str(resp)[:300], "ms": R["t3_post"][-1], "t_envio_ms": t_env})
                lleno = None
                if isinstance(resp, dict):
                    try:
                        lleno = float(resp.get("takingAmount") or 0) or None   # acciones recibidas (BUY)
                    except (TypeError, ValueError):
                        lleno = None
                hit = pr.buscar(tok3, ask, t_env, lleno)
                if hit and not hit[4]:
                    R["t3_casado"].append(hit[0] - t_env)
                    R["t3_recep"].append(hit[1] - t_env)
                log({"tipo": "T3_print", "hit": hit, "lleno": lleno, "status": (resp or {}).get("status") if isinstance(resp, dict) else None})
                print(f"   T3 {i + 1}: {out3} ask {ask} POST {R['t3_post'][-1]:.0f} ms | print exchange "
                      f"{(hit[0] - t_env) if hit else 'no visto'} ms{' (AMBIGUO, excluido)' if hit and hit[4] else ''} "
                      f"| lleno {lleno} | resp {str(resp)[:90]}")
                time.sleep(1.0)
    finally:
        # barrido: cancelar cualquier orden propia que siga viva (solo IDs creados aquí)
        for oid in mios:
            try:
                st = cli.get_order(oid)
                if isinstance(st, dict) and str(st.get("status", "")).lower() in ("live", "open"):
                    cli.cancel_order(OrderPayload(orderID=oid))
                    log({"tipo": "barrido_cancel", "oid": oid})
            except Exception as e:
                log({"tipo": "barrido_error", "oid": oid, "e": str(e)[:200]})
        if huerfanas:
            from py_clob_client_v2 import OpenOrderParams
            for tok in set(huerfanas):
                try:
                    for od in cli.get_open_orders(OpenOrderParams(asset_id=tok)) or []:
                        if (abs(float(od.get("price", 0)) - 0.01) < 1e-9 and abs(float(od.get("original_size", 0)) - SIZE) < 1e-6
                                and od.get("side") == "BUY" and float(od.get("created_at", 0)) >= t_inicio - 5):
                            cli.cancel_order(OrderPayload(orderID=od["id"]))
                            log({"tipo": "barrido_huerfana", "oid": od["id"]})
                except Exception as e:
                    log({"tipo": "barrido_huerfana_error", "tok": tok, "e": str(e)[:200]})
                    print(f"   ⚠ revisar a mano órdenes abiertas en {tok[:12]}…: {e}")
    print()
    for k, v in R.items():
        resumen(k, v)
    print("\nNOTAS: t3_casado = hora del EXCHANGE del print − nuestro envío (red ida + validación + taker delay + casado; "
          "reloj chrony ±0,2 ms, reloj del exchange sin verificar); t3_post = respuesta del POST.")


if __name__ == "__main__":
    main()
