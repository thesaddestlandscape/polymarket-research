#!/usr/bin/env python3
"""medir_cancelacion_delay.py -- (OK explícito de Javi 14-Oct) ¿se puede CANCELAR una orden tomadora mientras está retenida
en el taker delay (~145 ms medidos el 07-Oct)? Si sí, la vía "órdenes armadas" de 5m barato pone nuestra ejecución a
~150 ms efectivos (la orden ya está en vuelo; decidimos tarde y cancelamos lo que no conviene).
⚠️ HERRAMIENTA MANUAL que puede ENVIAR ÓRDENES REALES. Nunca en cron/screen/watchdog. /code-review medium antes de usarla.
Usa SOLO la WALLET DEDICADA de experimentos (/root/.secrets/experimento_pares.env), nunca la del live (guarda fail-closed).

El ID de una orden es su hash EIP-712, que calculamos ANTES de enviarla -> la cancelación se manda en paralelo al POST,
sin esperar su respuesta (el POST de una FOK no responde hasta después del retraso).
FASES (cada intento deja INTENCIÓN en el ledger antes de enviar: datalogs/medir_cancelacion_delay_ledger.jsonl):
  0  (coste 0)  GTC post_only BUY 5 acc a 0,01 (no puede casar): ¿orderID devuelto == hash calculado?; después se cancela.
  1  (coste 0)  FOK BUY 5 acc a 0,01 (no casa) + cancelación concurrente por hash a +CANCEL_TRAS_MS del inicio del POST,
                alternando defer_exec False/True: ¿qué responden el POST y el DELETE con la orden retenida?
  2  (riesgo acotado) FOK BUY 5 acc MARKETABLE del FAVORITO de un mercado BTC 5m/15m casi decidido (ask en [0,97, 0,99],
                mejor bid del otro lado <= 0,03, entre 20 y 90 s al cierre; re-chequeo del libro justo antes de enviar) +
                cancelación concurrente. Si la cancelación funciona no compra nada; si falla compra 5 acc que casi seguro
                ganan (~+0,09 $); solo si el mercado se da la vuelta se pierden ~4,9 $ por relleno. Tope MAX_N[2] intentos y
                PARADA al 2º relleno.
Uso: python3 medir_cancelacion_delay.py --fase 0 --n 3 [--confirmo-dinero-real]   (sin la marca: ensayo en seco: firma y
     calcula hashes pero NO envía nada)
"""
import argparse
import dataclasses
import json
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
ENV_DEDICADA = Path("/root/.secrets/experimento_pares.env")
LEDGER = Path("/root/polymarket-research-datalogs/medir_cancelacion_delay_ledger.jsonl")
GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
SIZE = 5.0
CANCEL_TRAS_MS = 10            # el POST tarda ~35 ms de ida: la cancelación (también ~35 ms) llega dentro del retraso
MAX_N = {0: 5, 1: 10, 2: 5}
MAX_RELLENOS_F2 = 2


def log(ev):
    ev["ts"] = datetime.now(timezone.utc).isoformat(timespec="milliseconds")
    with open(LEDGER, "a") as f:
        f.write(json.dumps(ev, default=str) + "\n")


def cliente_dedicado():
    """Copia de experimento_pares_cola_15m.cliente_dedicado (dev 44eba08867, 25 /code-review): POLY_1271, funder = wallet
    de depósito; fail-closed si alguna credencial coincide con la de producción."""
    from dotenv import dotenv_values
    from py_clob_client_v2 import ClobClient, ApiCreds
    from py_clob_client_v2.constants import POLYGON
    import live_trade as lt
    lt._parchear_redondeo_clob()
    c = dotenv_values(ENV_DEDICADA)
    faltan = [k for k in ("POLY_PRIVATE_KEY", "POLY_DEPOSIT_WALLET", "POLY_API_KEY", "POLY_API_SECRET",
                          "POLY_API_PASSPHRASE") if not c.get(k)]
    if faltan:
        sys.exit(f"{ENV_DEDICADA}: faltan {faltan}")
    live = dotenv_values(REPO / "data" / "live" / ".env")
    if not live.get("POLY_DEPOSIT_WALLET") or not live.get("POLY_API_KEY") or not live.get("POLY_PRIVATE_KEY"):
        sys.exit("no se puede comprobar que la wallet dedicada no sea la de producción: no arranco")
    norm = lambda x: str(x or "").strip().lower().removeprefix("0x")
    if any(norm(c[k]) == norm(live[k]) for k in ("POLY_DEPOSIT_WALLET", "POLY_API_KEY", "POLY_PRIVATE_KEY")):
        sys.exit("experimento_pares.env comparte credenciales con data/live/.env: no arranco")
    pk = c["POLY_PRIVATE_KEY"] if c["POLY_PRIVATE_KEY"].lower().startswith("0x") else "0x" + c["POLY_PRIVATE_KEY"]
    return ClobClient(CLOB, key=pk, chain_id=POLYGON,
                      creds=ApiCreds(api_key=c["POLY_API_KEY"], api_secret=c["POLY_API_SECRET"],
                                     api_passphrase=c["POLY_API_PASSPHRASE"]),
                      signature_type=3, funder=c["POLY_DEPOSIT_WALLET"])


def hash_orden(signed, neg_risk=False):
    """orderID = hash EIP-712 de la orden V2 (sin la firma). La fase 0 verifica que coincide con el del servidor."""
    from py_clob_client_v2.config import get_contract_config
    from py_clob_client_v2.order_utils.exchange_order_builder_v2 import ExchangeOrderBuilderV2
    from py_clob_client_v2.order_utils.model.order_data_v2 import OrderV2
    cfg = get_contract_config(137)
    ex = cfg.neg_risk_exchange_v2 if neg_risk else cfg.exchange_v2
    b = ExchangeOrderBuilderV2(ex, 137, None)
    campos = {k: v for k, v in dataclasses.asdict(signed).items() if k != "signature"}
    return b.build_order_hash(b.build_order_typed_data(OrderV2(**campos)))


def libro(tok):
    r = requests.get(f"{CLOB}/book", params={"token_id": tok}, timeout=5).json()
    bids = sorted(((float(x["price"]), float(x["size"])) for x in r.get("bids", [])), reverse=True)
    asks = sorted((float(x["price"]), float(x["size"])) for x in r.get("asks", []))
    return bids, asks


def mercados_btc(cierre_min_s, cierre_max_s):
    """Mercados BTC up/down 5m y 15m abiertos que cierran dentro de [min, max] s -> [(slug, fin, toks, neg_risk)]."""
    out = []
    ahora = time.time()
    for marco, paso in (("5m", 300), ("15m", 900)):
        base = int(ahora // paso) * paso
        for k in (0, 1):
            ini = base + k * paso
            slug = f"btc-updown-{marco}-{ini}"
            try:
                ev = requests.get(f"{GAMMA}/events", params={"slug": slug}, timeout=5).json()
            except Exception:
                continue
            if not ev:
                continue
            for m in ev[0].get("markets", []):
                fin = ini + paso
                if (not (cierre_min_s <= fin - ahora <= cierre_max_s) or m.get("closed")
                        or m.get("acceptingOrders") is False or m.get("active") is False):
                    continue
                toks = json.loads(m["clobTokenIds"]) if isinstance(m["clobTokenIds"], str) else m["clobTokenIds"]
                out.append((slug, fin, toks, bool(m.get("negRisk"))))
    return out


def intento(cli, OrderType, OrderPayload, signed, h, tipo, defer, real):
    """POST y cancelación concurrentes (la cancelación solo en FOK). -> dict con respuestas y tiempos."""
    res = {"hash": h, "tipo": tipo, "defer_exec": defer}
    if not real:
        res["ensayo_seco"] = True
        return res
    t0 = time.perf_counter()

    def post():
        try:
            res["post_resp"] = cli.post_order(signed, OrderType.FOK if tipo == "FOK" else OrderType.GTC,
                                              post_only=(tipo == "GTC"), defer_exec=defer)
        except Exception as e:
            res["post_resp"] = f"{type(e).__name__}: {e}"[:400]
        res["post_ms"] = round((time.perf_counter() - t0) * 1000, 1)

    def cancel():
        """Primera cancelación a +CANCEL_TRAS_MS; si el servidor aún no conoce la orden (no la cancela), reintenta cada
        30 ms mientras el POST siga en vuelo (máx. 6). Se registran todas las respuestas."""
        time.sleep(CANCEL_TRAS_MS / 1000)
        res["cancel_resps"] = []
        for k in range(6):
            t1 = time.perf_counter()
            try:
                cr = cli.cancel_order(OrderPayload(orderID=h))
            except Exception as e:
                cr = f"{type(e).__name__}: {e}"[:300]
            res["cancel_resps"].append({"inicio_ms": round((t1 - t0) * 1000, 1),
                                        "ms": round((time.perf_counter() - t1) * 1000, 1), "resp": cr})
            if h.lower() in str(cr).lower().split("not_canceled")[0] or "post_resp" in res:
                break                                   # cancelada, o el POST ya volvió (ya no hay nada que cancelar)
            time.sleep(0.03)
        res["cancel_resp"] = res["cancel_resps"][-1]["resp"] if res["cancel_resps"] else None

    hp = threading.Thread(target=post)
    hp.start()
    if tipo == "FOK":
        hc = threading.Thread(target=cancel)
        hc.start()
        hc.join(10)
    hp.join(10)
    if hp.is_alive() or (tipo == "FOK" and hc.is_alive()):
        res["ambiguo"] = "hilo POST/DELETE sin terminar a los 10 s"
    try:
        res["estado_final"] = cli.get_order(h)
    except Exception as e:
        res["estado_final"] = f"{type(e).__name__}: {e}"[:200]
    return res


def relleno(res):
    """True si el POST o el estado final dicen que la orden casó (algo). Ante duda -> True (cuenta para la PARADA)."""
    if res.get("ambiguo") or "post_resp" not in res or not isinstance(res.get("post_resp"), dict) \
            and "couldn't be fully filled" not in str(res.get("post_resp")).lower():
        return True                                     # excepción/timeout/sin respuesta: puede haber casado
    s = (str(res.get("post_resp")) + " " + str(res.get("estado_final"))).lower()
    if "'status': 'matched'" in s or '"status": "matched"' in s:
        return True
    if "size_matched" in s and "'size_matched': '0'" not in s and "'size_matched': 0" not in s:
        return True
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase", type=int, required=True, choices=(0, 1, 2))
    ap.add_argument("--n", type=int, default=3)
    ap.add_argument("--confirmo-dinero-real", action="store_true")
    a = ap.parse_args()
    if a.n > MAX_N[a.fase]:
        sys.exit(f"--n > {MAX_N[a.fase]} para la fase {a.fase}")
    real = a.confirmo_dinero_real
    from py_clob_client_v2 import OrderArgsV2, OrderType, OrderPayload, PartialCreateOrderOptions
    if a.fase == 2 and real:
        ok_hash = False
        if LEDGER.exists():
            for ln in LEDGER.read_text().splitlines():
                try:
                    ev = json.loads(ln)
                except ValueError:
                    continue
                if ev.get("tipo") == "F0_resultado" and ev.get("id_coincide") == "True":
                    ok_hash = True
        if not ok_hash:
            sys.exit("fase 2 bloqueada: la fase 0 no ha confirmado en el ledger que el hash calculado == orderID del servidor")
    cli = cliente_dedicado()
    print(f"{'REAL' if real else 'ENSAYO EN SECO'} | fase {a.fase} | n {a.n} | wallet DEDICADA")
    rellenos = 0
    i = 0
    intentos_busqueda = 0
    while i < a.n and intentos_busqueda < 30:
        if a.fase in (0, 1):
            elegido = None
            for slug, fin, toks, nr in mercados_btc(150, 900):
                for tk in toks:
                    try:
                        _, asks = libro(tk)
                    except Exception:
                        continue
                    if asks and asks[0][0] >= 0.05:          # un BUY a 0,01 no puede casar contra este libro
                        elegido = (slug, fin, tk)
                        break
                if elegido:
                    break
            if not elegido:
                sys.exit("sin token BTC con ask >= 0,05 y >= 150 s al cierre")
            slug, fin, tok = elegido
            precio = 0.01
            tipo = "GTC" if a.fase == 0 else "FOK"
            size = SIZE if a.fase == 0 else 105.0             # FOK: 1,05 $ de nominal (como la T2 del 07-Oct)
            defer = (a.fase == 1 and i % 2 == 1)
        else:
            intentos_busqueda += 1
            cand = []
            for slug, fin, toks, nr in mercados_btc(20, 90):
                try:
                    (b0, a0), (b1, a1) = libro(toks[0]), libro(toks[1])
                except Exception as e:
                    print(f"  libro ilegible ({type(e).__name__}); salto")
                    continue
                for (tk, otro, asks, bids_otro) in ((toks[0], toks[1], a0, b1), (toks[1], toks[0], a1, b0)):
                    if asks and 0.97 <= asks[0][0] <= 0.99 and (not bids_otro or bids_otro[0][0] <= 0.03):
                        cand.append((slug, fin, tk, otro))
            if not cand:
                print(f"  sin favorito casi decidido (ask 0,97-0,99, 20-90 s al cierre); espero 20 s")
                time.sleep(20)
                continue
            slug, fin, tok, otro = cand[0]
            tipo, defer, size = "FOK", False, SIZE
            try:                                                    # re-chequeo JUSTO antes de enviar (fail-closed)
                _, asks = libro(tok)
                bids_otro, _ = libro(otro)
            except Exception:
                print("  libro ilegible en el re-chequeo; no se envía")
                continue
            if (not asks or not (0.97 <= asks[0][0] <= 0.99) or not (20 <= fin - time.time() <= 90)
                    or (bids_otro and bids_otro[0][0] > 0.03)):
                print("  el libro cambió antes de enviar; no se envía")
                continue
            precio = asks[0][0]
            if round(precio, 2) != precio:
                print(f"  precio {precio} con tick < 0,01 (el CLOB rechazaría el importe); no se envía")
                continue
        nr = bool(cli.get_neg_risk(tok))                        # el MISMO neg_risk para firmar y para el hash
        signed = cli.create_order(OrderArgsV2(token_id=tok, price=precio, size=size, side="BUY"),
                                  PartialCreateOrderOptions(neg_risk=nr))
        if not dataclasses.is_dataclass(signed) or "salt" not in dataclasses.asdict(signed) or not hasattr(signed, "timestamp"):
            sys.exit("la orden firmada no es V2: el hash calculado no sería válido; no se envía")
        h = hash_orden(signed, nr)
        log({"tipo": f"F{a.fase}_intencion", "slug": slug, "tok": tok, "precio": precio, "size": size, "hash": h,
             "orden": tipo, "defer_exec": defer, "real": real})
        r = intento(cli, OrderType, OrderPayload, signed, h, tipo, defer, real)
        r.update({"slug": slug, "precio": precio})
        if a.fase == 0 and real:
            r["id_coincide"] = h.lower() in str(r.get("post_resp")).lower()
            try:
                r["cancel_resp"] = cli.cancel_order(OrderPayload(orderID=h))
            except Exception as e:
                r["cancel_resp"] = f"{type(e).__name__}: {e}"[:300]
        log({"tipo": f"F{a.fase}_resultado", **{k: str(v)[:600] for k, v in r.items()}})
        print(f"  intento {i}: " + json.dumps({k: str(v)[:200] for k, v in r.items()}, ensure_ascii=False))
        i += 1
        if a.fase == 2 and real and relleno(r):
            rellenos += 1
            print(f"  ⚠ relleno {rellenos}: la cancelación NO llegó a tiempo")
            if rellenos >= MAX_RELLENOS_F2:
                print("  PARADA: 2 rellenos")
                break
        time.sleep(2)
    print("fin")


if __name__ == "__main__":
    main()
