#!/usr/bin/env python3
"""
precierre_sondeo_corte_exchange.py -- 21-Sep, aprobado por Javi ("2 - ok, procede").

Objetivo: medir con datos REALES en que instante, respecto al cierre nominal
`T` de un mercado Up/Down 5min, el exchange de Polymarket deja de ACEPTAR
ordenes. El dry-run del ejecutor pre-cierre (resolution_sniper_precierre_
executor.py) firma pero NUNCA envia, asi que no puede medirlo; el flag
`accepting_orders` de gamma (freezeestado) se mantiene True hasta ~T+1,5s y
no refleja lo que acepta el motor de emparejamiento (la unica prueba real,
03-Sep, aterrizo en T exacto por 2s de latencia propia del pipeline generico).

Diseno SIN RIESGO DE FILL:
  * orden LIMITE BUY, precio 0.01, 5 shares (minimo del CLOB) = 0.05 USDC max
  * `post_only=True`: el exchange rechaza cualquier orden que cruzaria el
    libro, asi que NUNCA puede ejecutarse contra una contraparte
  * se pone sobre el token de MAYOR mejor-ask (el lado "ganador"), cuyo ask
    esta muy por encima de 0.01 -- doble garantia de que queda en reposo
  * se CANCELA inmediatamente si es aceptada; al final se barren restos
  * la firma se hace ANTES del instante objetivo: en el instante solo se
    llama a post_order, asi que la latencia medida es red + exchange, no
    nuestro pipeline
Cada fila registra el instante de envio y de respuesta relativos a T
(reloj sincronizado con NTP, offset ~0,2ms), la latencia del POST y el
error literal del exchange (p.ej. 503 "trading is disabled").

Uso:
  python3 precierre_sondeo_corte_exchange.py            # DRY: todo salvo el POST
  python3 precierre_sondeo_corte_exchange.py --real     # envia de verdad
Parada de emergencia: crear data/shadow/SONDEO_STOP.
Salida: data/shadow/precierre_sondeo_corte_exchange.csv
"""
import argparse
import csv
import sys
import threading
import time
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import live_trade as lt  # noqa: E402
from resolution_sniper_observer import mercado_slot, token_ids  # noqa: E402

DUR_S = 300
MARCO_TAG = "5m"
PRECIO = 0.01
SIZE = 5.0                      # min_order_size real del CLOB (17-Sep)
MAX_ORDENES = 40                # tope duro de ordenes enviadas por ejecucion
OFFSETS_DEFECTO = [-3.0, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0]
ACTIVOS_DEFECTO = ("BTC", "ETH")
STOP = REPO / "data" / "shadow" / "SONDEO_STOP"
OUT = REPO / "data" / "shadow" / "precierre_sondeo_corte_exchange.csv"
CAMPOS = ["timestamp_utc", "modo", "ts_end", "activo", "ronda", "offset_objetivo_s",
          "t_envio_rel_s", "t_resp_rel_s", "latencia_post_ms", "aceptada", "error",
          "order_id", "cancelada", "cancel_ms", "lado_token", "best_ask_token"]
_lock = threading.Lock()


def _log(msg: str) -> None:
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


def _append(row: dict) -> None:
    with _lock:
        nuevo = not OUT.exists()
        with open(OUT, "a", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=CAMPOS)
            if nuevo:
                w.writeheader()
            w.writerow({k: row.get(k, "") for k in CAMPOS})


def _mejor_ask(token: str):
    book = lt._fetch_book_publico(token)
    if not book:
        return None
    mejor = None
    for lvl in book.get("asks") or []:
        try:
            p = float(lvl.get("price"))
        except (TypeError, ValueError, AttributeError):
            continue
        if mejor is None or p < mejor:
            mejor = p
    return mejor


def _esperar_hasta(t_epoch: float) -> None:
    while True:
        falta = t_epoch - time.time()
        if falta <= 0:
            return
        time.sleep(0.05 if falta > 0.2 else 0.0005)


def _sondear(client, real: bool, ts_end: int, activo: str, ronda: int, offset: float,
             token: str, lado: str, best_ask, signed) -> None:
    from py_clob_client_v2.clob_types import OrderType, OrderPayload
    fila = {"timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "modo": "real" if real else "dry", "ts_end": ts_end, "activo": activo,
            "ronda": ronda, "offset_objetivo_s": offset, "lado_token": lado,
            "best_ask_token": best_ask}
    _esperar_hasta(ts_end + offset)
    if not real:
        fila.update({"t_envio_rel_s": round(time.time() - ts_end, 4), "aceptada": "dry"})
        _append(fila)
        return
    t0 = time.time()
    order_id, error, aceptada = "", "", False
    try:
        resp = client.post_order(signed, OrderType.GTC, post_only=True)
        t1 = time.time()
        order_id = (resp.get("orderID") or resp.get("id") or "") if isinstance(resp, dict) else ""
        aceptada = bool(order_id) and (resp.get("success", True) if isinstance(resp, dict) else True)
        if not aceptada:
            error = str(resp)[:300]
    except Exception as e:
        t1 = time.time()
        error = f"{type(e).__name__}: {e}"[:300]
    fila.update({"t_envio_rel_s": round(t0 - ts_end, 4), "t_resp_rel_s": round(t1 - ts_end, 4),
                 "latencia_post_ms": round((t1 - t0) * 1000, 1), "aceptada": int(aceptada),
                 "error": error, "order_id": order_id})
    if order_id:
        c0 = time.time()
        try:
            client.cancel_order(OrderPayload(orderID=order_id))
            fila["cancelada"] = 1
        except Exception as e:
            fila["cancelada"] = 0
            fila["error"] = (fila["error"] + f" | cancel_fallo:{e}")[:300]
        fila["cancel_ms"] = round((time.time() - c0) * 1000, 1)
    _append(fila)
    _log(f"{activo} off={offset:+.1f}s envio={fila['t_envio_rel_s']:+.3f}s resp={fila['t_resp_rel_s']:+.3f}s "
         f"lat={fila['latencia_post_ms']}ms aceptada={fila['aceptada']} {error[:80]}")


def _barrer_restos(client, tokens: set) -> int:
    """Cancela cualquier orden abierta nuestra en los tokens sondeados."""
    from py_clob_client_v2.clob_types import OpenOrderParams, OrderPayload
    n = 0
    for t in tokens:
        try:
            for o in client.get_open_orders(OpenOrderParams(asset_id=t)) or []:
                oid = o.get("id") or o.get("orderID")
                if oid:
                    client.cancel_order(OrderPayload(orderID=oid))
                    n += 1
        except Exception as e:
            _log(f"aviso: barrido de restos fallo en {t[:10]}...: {e}")
    return n


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--real", action="store_true", help="envia ordenes de verdad (sin esto: DRY)")
    ap.add_argument("--reps", type=int, default=2, help="ventanas por offset")
    ap.add_argument("--offsets", type=float, nargs="*", default=OFFSETS_DEFECTO)
    ap.add_argument("--activos", nargs="*", default=list(ACTIVOS_DEFECTO))
    a = ap.parse_args()

    if STOP.exists():
        _log("SONDEO_STOP presente -- no arranca"); return 1
    client = lt._get_clob_client()
    from py_clob_client_v2.clob_types import OrderArgsV2
    plan = [o for _ in range(a.reps) for o in a.offsets]
    _log(f"modo={'REAL' if a.real else 'DRY'} ventanas={len(plan)} activos={a.activos} "
         f"max_ordenes={MAX_ORDENES} (orden BUY {SIZE}@{PRECIO} post_only GTC, cancela al aceptar)")
    enviadas, tokens_usados = 0, set()
    try:
        for ronda, offset in enumerate(plan):
            if STOP.exists():
                _log("SONDEO_STOP detectado -- parada limpia"); break
            if enviadas + len(a.activos) > MAX_ORDENES and a.real:
                _log("tope de ordenes alcanzado -- fin"); break
            now = time.time()
            ts_end = (int(now) // DUR_S + 1) * DUR_S
            if ts_end - now < 30:
                ts_end += DUR_S
            _esperar_hasta(ts_end - 20)
            preparados = []
            for activo in a.activos:
                try:
                    _slug, mkt = mercado_slot(activo, MARCO_TAG, ts_end - DUR_S)
                    ty, tn = token_ids(mkt) if mkt else (None, None)
                    if not ty or not tn:
                        _log(f"{activo}: mercado no resuelto -- se salta"); continue
                    ay, an = _mejor_ask(ty), _mejor_ask(tn)
                    if ay is None or an is None:
                        # sin ambos asks no se sabe cual es el lado ganador: NO adivinar
                        _log(f"{activo}: libro sin ask legible (yes={ay} no={an}) -- se salta"); continue
                    # token con MAYOR ask (lado ganador): 0.01 queda muy por debajo
                    if ay >= an:
                        token, lado, best = ty, "yes", ay
                    else:
                        token, lado, best = tn, "no", an
                    signed = client.create_order(OrderArgsV2(token_id=token, price=PRECIO, size=SIZE, side="BUY"))
                    preparados.append((activo, token, lado, best, signed))
                    tokens_usados.add(token)
                except Exception as e:
                    _log(f"{activo}: preparacion fallo ({type(e).__name__}: {e}) -- se salta")
            if not preparados:
                continue
            hilos = [threading.Thread(target=_sondear, args=(client, a.real, ts_end, act, ronda, offset,
                                                              tok, lado, best, sg), daemon=True)
                     for act, tok, lado, best, sg in preparados]
            for h in hilos:
                h.start()
            for h in hilos:
                h.join(timeout=60)
            enviadas += len(preparados)
            _log(f"ronda {ronda + 1}/{len(plan)} offset={offset:+.1f}s hecha ({enviadas} ordenes acumuladas)")
    finally:
        if a.real:
            _log(f"barrido final de restos: {_barrer_restos(client, tokens_usados)} ordenes canceladas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
