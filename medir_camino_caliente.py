#!/usr/bin/env python3
"""medir_camino_caliente.py — F1 del ejecutor dedicado (Javi 15-Oct: objetivo 175 ms). ⚠️ HERRAMIENTA MANUAL que puede
ENVIAR ÓRDENES REALES, solo con la WALLET DEDICADA (cliente_dedicado de medir_cancelacion_delay: fail-closed si comparte
credenciales con el live). Nunca en cron/screen/watchdog.

Mide el camino caliente de ejecutor_rapido (orden PREFIRMADA + conexión HTTP/2 caliente + libro WS propio) con órdenes
que no deberían casar, frente a la línea base del 07-Oct (GTC 68-81 ms, cancelación 60-70, FOK no marketable 213-216):
  GTC : post_only BUY ~5 acc a 0,01 (tamaño ÚNICO por orden: así su aparición en el WS es inequívoca) -> acuse del POST
        y aparición del nivel en el WS (recepción); cancelación por id -> acuse y desaparición. Cada orden se FIRMA
        `edad` s antes de enviarse (0,5 / 10 / 60 / 120): ¿acepta el servidor una orden prefirmada hace minutos?
  FOK : BUY 105 acc a 0,01 (1,05 $) -> acuse (incluye el retraso del tomador).
Riesgo residual (asumido): una venta que barra hasta 0,01 durante los ~0,8 s en reposo rellenaría la GTC (5 acc a 0,01 =
0,05 $) o, en el retraso, la FOK (1,05 $ por acciones a 0,01). Mitigado: solo un 15m BTC con 500-890 s al cierre, ambos
tokens con mejor bid >= 0,10 y mejor ask >= 0,12, comprobado justo ANTES de cada POST con el libro WS fresco de ESE token.
Cualquier relleno detectado (respuesta, cancelación o estado) -> PARA. try/finally: barre por hash TODAS las órdenes
firmadas y enviadas (también las de respuesta ambigua) y al final cancela las de ESTE mercado de la wallet dedicada.
Uso: python3 medir_camino_caliente.py --gtc 8 --fok 8 [--confirmo-dinero-real]   (sin la marca: firma y simula, no envía)
"""
import argparse
import sys
import time
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import ejecutor_rapido as er  # noqa: E402
from medir_cancelacion_delay import cliente_dedicado, mercados_btc, hash_orden  # noqa: E402

LEDGER = Path("/root/polymarket-research-datalogs/medir_camino_caliente_ledger.jsonl")
MAX_N = 20
EDADES_S = (0.5, 10, 60, 120)
BID_MIN, ASK_MIN = 0.10, 0.12


def lleno(res):
    """True si la respuesta indica cualquier relleno, o si no se puede interpretar (tratar como relleno: parar)."""
    if not isinstance(res, dict):
        return True
    if "error" in res and len(res) == 1:
        return False                                  # error de red/servidor: ambiguo, se barre por hash
    try:
        return (float(res.get("makingAmount") or 0) > 0 or float(res.get("takingAmount") or 0) > 0
                or str(res.get("status", "")).lower() in ("matched", "delayed") or bool(res.get("tradeIDs")))
    except (TypeError, ValueError):
        return True


def pct(xs):
    xs = sorted(x for x in xs if x is not None)
    if not xs:
        return "n=0"
    return f"n={len(xs)} p50 {xs[len(xs) // 2]:.1f} p90 {xs[int(len(xs) * 0.9)]:.1f} min {xs[0]:.1f} ms"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gtc", type=int, default=8)
    ap.add_argument("--fok", type=int, default=8)
    ap.add_argument("--confirmo-dinero-real", action="store_true")
    a = ap.parse_args()
    if a.gtc > MAX_N or a.fok > MAX_N:
        sys.exit(f"máximo {MAX_N} por tipo")
    real = a.confirmo_dinero_real
    c = cliente_dedicado()
    t_lim = time.time() + 960                          # espera como mucho un ciclo de 15m a que abra uno
    ms = []
    while time.time() < t_lim:
        ms = [m for m in mercados_btc(500, 890) if "15m" in m[0]]
        if ms:
            break
        time.sleep(10)
    if not ms:
        sys.exit("no hay 15m BTC con 500-890 s al cierre tras 16 min de espera")
    slug, fin, toks, neg = ms[0]
    tok = toks[0]
    tick = str(c.get_tick_size(tok))
    print(f"mercado {slug} cierre en {fin - time.time():.0f} s, tick {tick}, neg_risk {neg}, REAL={real}")

    apar = {}                                          # delta exacto de tamaño en 0,01 -> [t_recv, ...]

    def al_nivel(tk, lado, p, s_nuevo, s_viejo, t_recv):
        if tk == tok and lado == "bids" and abs(p - 0.01) < 1e-9:
            apar.setdefault(round(s_nuevo - s_viejo, 4), []).append(t_recv)

    def primera(d, desde):
        return next((t for t in apar.get(d, []) if t >= desde), None)

    lib = er.Libro(toks, al_nivel=al_nivel).iniciar()
    t_esp = time.time() + 10
    while time.time() < t_esp and not all(lib.fresco(t) for t in toks):
        time.sleep(0.1)

    def apto():
        for t in toks:
            top = lib.top.get(t)
            if not lib.fresco(t) or not top or top[1] is None or top[3] is None:
                return False, f"libro no apto {t[:8]} top={top}"
            if top[1] < BID_MIN or top[3] < ASK_MIN:
                return False, f"precios fuera de banda segura {t[:8]} bid={top[1]} ask={top[3]}"
        if fin - time.time() < 120:
            return False, "menos de 120 s al cierre"
        return True, "ok"

    riesgo = er.Riesgo([apto], cada_s=0.2, max_edad_s=0.5)
    env = er.Enviador(c, LEDGER, riesgo, dry_run=not real)
    arm = er.Armero(c, tick, neg)
    enviados = []                                      # (hash, tipo) de TODO lo enviado (barrido final)
    futuros = []
    res_gtc, res_can, ws_alta, ws_baja, res_fok, edades = [], [], [], [], [], {}
    parar = None
    try:
        time.sleep(1.0)                                # latido HTTP + primera foto de riesgo
        for i in range(a.gtc):
            edad = EDADES_S[i % len(EDADES_S)]
            tam = round(5.0 + 0.01 * (i + 1), 2)       # tamaño único por orden
            signed = arm._firmar((tok, 0.01, tam, "BUY"))
            h = hash_orden(signed, neg)
            time.sleep(edad)
            ok, motivo = apto()                        # re-chequeo JUSTO antes del POST (además del de Enviador)
            if not ok:
                parar = motivo
                break
            enviados.append((h, "GTC"))
            t_ev = er.ahora_ms()
            fut = env.enviar(f"gtc#{h}", signed, "GTC", t_ev, meta={"edad_firma_s": edad, "tam": tam}, post_only=True)
            if fut is None:
                parar = "Enviador vetó (riesgo o idempotencia)"
                break
            futuros.append(fut)
            r = fut.result(timeout=15)
            res = r["res"]
            if isinstance(res, dict) and "abortada" in res:
                parar = f"abortada por riesgo justo antes del POST: {res['abortada']}"
                break
            if lleno(res):
                parar = f"GTC con relleno o respuesta no interpretable: {res}"
                break
            oid = res.get("orderID") if isinstance(res, dict) else None
            edades.setdefault(edad, []).append(bool(oid) if real else None)
            res_gtc.append(r["ms_post"])
            if not real:
                continue
            if oid and oid.lower() != h.lower():
                print(f"aviso: orderID {oid} != hash local {h}")
            time.sleep(0.8)
            if not oid:
                print(f"GTC edad {edad} s RECHAZADA o ambigua: {res}")   # se barre por hash al final
                time.sleep(0.3)
                continue
            ta = primera(tam, t_ev)
            if ta is not None:
                ws_alta.append(ta - t_ev)
            t_c = er.ahora_ms()
            cr = env.cancelar(oid)
            res_can.append(cr["ms_cancel"])
            cres = cr["res"] if isinstance(cr["res"], dict) else {}
            if oid.lower() not in [x.lower() for x in (cres.get("canceled") or [])]:
                parar = f"la cancelación no confirma {oid}: {cres} (¿rellenada?)"
                break
            time.sleep(0.8)
            tb = primera(-tam, t_c)
            if tb is not None:
                ws_baja.append(tb - t_c)
            time.sleep(0.3)
        for i in range(a.fok if parar is None else 0):
            tam = round(105.0 + 0.01 * (i + 1), 2)
            signed = arm._firmar((tok, 0.01, tam, "BUY"))
            h = hash_orden(signed, neg)
            time.sleep(0.5)
            ok, motivo = apto()
            if not ok:
                parar = motivo
                break
            enviados.append((h, "FOK"))
            fut = env.enviar(f"fok#{h}", signed, "FOK", er.ahora_ms(), meta={"tam": tam})
            if fut is None:
                parar = "Enviador vetó (riesgo o idempotencia)"
                break
            futuros.append(fut)
            r = fut.result(timeout=15)
            if isinstance(r["res"], dict) and "abortada" in r["res"]:
                parar = f"abortada por riesgo justo antes del POST: {r['res']['abortada']}"
                break
            if lleno(r["res"]):
                parar = f"FOK con relleno o respuesta no interpretable: {r['res']}"
                break
            res_fok.append(r["ms_post"])
            time.sleep(0.5)
    finally:
        for f in futuros:                              # que ningún POST siga en vuelo al barrer
            try:
                f.result(timeout=20)
            except Exception:
                pass
        if real:
            for h, tipo in enviados:                   # barrido por hash: también las de respuesta ambigua
                try:
                    o = c.get_order(h)
                    st = str((o or {}).get("status", "")).upper() if isinstance(o, dict) else ""
                    if st in ("LIVE", "OPEN"):
                        env.cancelar(h, meta={"barrido": True})
                    elif st and st not in ("CANCELED", "CANCELLED", "UNMATCHED", ""):
                        print(f"⚠️ orden {h} ({tipo}) en estado {st}: revisar posición en la wallet dedicada")
                except Exception as e:
                    print("barrido", h, type(e).__name__, e)
            try:                                       # red de seguridad: SOLO la wallet dedicada y SOLO este token
                from py_clob_client_v2.clob_types import OrderMarketCancelParams
                print("cancelación por token (wallet dedicada):", c.cancel_market_orders(OrderMarketCancelParams(asset_id=tok)))
            except Exception as e:
                print("cancelación por token falló:", type(e).__name__, e)
        lib.parar()
        env.vaciar_ledger()
    if parar:
        print("⛔ PARADA:", parar)
    print("RESULTADO (camino caliente; línea base 07-Oct: GTC 68-81, cancelación 60-70, FOK no marketable 213-216 ms)")
    print("  GTC acuse POST    :", pct(res_gtc))
    print("  GTC aparece en WS :", pct(ws_alta), "(envío -> recepción del nivel 0,01 con nuestro tamaño)")
    print("  cancelación acuse :", pct(res_can))
    print("  cancelación en WS :", pct(ws_baja))
    print("  FOK no marketable :", pct(res_fok))
    print("  aceptación por edad de firma:", {e: f"{sum(1 for x in v if x)}/{len(v)}" for e, v in sorted(edades.items())})


if __name__ == "__main__":
    main()
