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

--casa N (Javi 15-Oct, "tendrás que utilizar la otra vía": sin VPS, medir el CASADO real): FOK BUY 7 acc (tamaño poco habitual, para reconocer nuestro casado) MARKETABLE del
FAVORITO casi decidido de un BTC 5m/15m (ask en [0,97, 0,99], mejor bid del otro lado <= 0,03) a T-280..-55 o T-35..-15
(nunca alrededor de T-45, el disparo de PRECIERRE; además PRECIERRE live solo compra con ask < 0,80/0,85: no competimos
por el mismo nivel), límite = mejor ask (nunca por
encima: no barre niveles) y re-chequeo del libro WS de ESE token justo antes del POST. Mide envío -> recepción del print
de NUESTRO trade (grupo de prints que suma 7 en <= 50 ms) en el WS = cota superior del casado (+~31 ms de feed). Coste: ~7 $
por orden que se recuperan al resolver si el favorito gana (+0,07-0,21 $); si se da la vuelta, −~7 $. Tope 3 casadas en 24 h
ENTRE ejecuciones (ledger; el saldo queda retenido hasta redimir; peor caso 3 × ~7 $), una sola instancia (cerrojo) y
ningún otro script de la wallet dedicada vivo; PARADA ante respuesta ambigua.
"""
import argparse
import json
import os
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


def _otro_proceso_wallet_dedicada():
    """¿Corre otro script que usa la wallet dedicada (experimento de pares, medición de cancelación)? Lee /proc (sin
    pgrep -f, que se encuentra a sí mismo)."""
    import os
    excl, p = set(), os.getpid()                       # este proceso y TODOS sus ancestros (timeout, bash -c, cron...)
    while p > 1 and p not in excl:
        excl.add(p)
        try:
            p = int(open(f"/proc/{p}/stat").read().rsplit(")", 1)[1].split()[1])
        except (OSError, ValueError, IndexError):
            break
    for pid in os.listdir("/proc"):
        if not pid.isdigit() or int(pid) in excl:
            continue
        try:
            argv = open(f"/proc/{pid}/cmdline", "rb").read().split(b"\0")
        except OSError:
            continue
        exe = os.path.basename(argv[0].decode(errors="replace")) if argv and argv[0] else ""
        cmd = b" ".join(argv).decode(errors="replace")
        # solo un INTÉRPRETE de Python ejecutando el script (no shells/envoltorios cuya línea lo menciona)
        if exe.startswith("python") and any(x in cmd for x in ("experimento_pares_cola_15m", "medir_cancelacion_delay",
                                                       "medir_latencia_ordenes_15m", "medir_camino_caliente")):
            return cmd[:120]
    return None


def _saldo_dedicada(c):
    from py_clob_client_v2.clob_types import AssetType, BalanceAllowanceParams
    try:
        pr = BalanceAllowanceParams(asset_type=AssetType.COLLATERAL)
        try:
            c.update_balance_allowance(pr)              # fuerza recálculo (el saldo del servidor va cacheado)
        except Exception:
            pass
        b = c.get_balance_allowance(pr)
        return float(b["balance"]) / 1e6
    except Exception:
        return None                                     # fail-closed: sin saldo legible no se envía


def _live_abierto_en(fin):
    """¿Tiene el LIVE (PRECIERRE/NAIVE u otro) una posición OPEN en un mercado que cierra a `fin`? Lee la cola de
    trades.csv; ante error -> True (no competir con el live por el mismo nivel)."""
    import csv
    from collections import deque
    from datetime import datetime, timezone
    try:
        with open(REPO / "data/live/trades.csv", encoding="utf-8") as f:
            filas = deque(csv.DictReader(f), maxlen=300)   # solo la cola (trampa: list(DictReader) entero)
        for r in filas:
            if r.get("status") == "CLOSED" or not str(r.get("subtype", "")).startswith("BTC"):
                continue                                   # OPEN, ERROR ("revisar manualmente"), STUB... de BTC
            try:
                e = datetime.fromisoformat(r["end_date"].replace("Z", "+00:00")).astimezone(timezone.utc).timestamp()
            except (KeyError, ValueError, AttributeError):
                continue
            if abs(e - fin) < 2:
                print(f"  live con fila {r.get('status')} {r.get('strategy')} {r.get('subtype')} en este cierre")
                return True
        return False
    except Exception as e:
        print(f"  no se pudo leer trades.csv ({type(e).__name__}: {e}): no compito")
        return True


def _cerrojo_unico():
    """Una sola instancia de medición real a la vez (--casa o --gtc/--fok) (dos terminales duplicarían el tope). El cerrojo vive lo que el proceso."""
    import fcntl
    f = open("/root/polymarket-research-datalogs/medir_camino_caliente_casa.lock", "w")
    try:
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        sys.exit("⛔ ya hay otra instancia de medir_camino_caliente --casa: no arranco")
    return f


def _resolver_estado(c, h, res, t_max_s=6.0):
    """CONSERVADOR (7ª /code-review): 'muerta' SOLO si la respuesta dice explícitamente que la FOK no pudo llenarse;
    'casada' si la respuesta o get_order muestran relleno; TODO lo demás 'ambigua' (cuenta para el tope y PARA). El
    saldo nunca rebaja un caso a muerta (puede no estar liquidado/cacheado)."""
    if isinstance(res, dict):                           # 1º evidencia de relleno (gana a cualquier texto)
        try:
            if (str(res.get("status", "")).lower() == "matched" or float(res.get("takingAmount") or 0) > 0
                    or float(res.get("makingAmount") or 0) > 0 or res.get("tradeIDs")):
                return "casada", res
        except (TypeError, ValueError):
            return "ambigua", res
    rechazo_fok = (isinstance(res, dict) and set(res) == {"error"} and "status_code=400" in str(res["error"])
                   and "couldn't be fully filled" in str(res["error"]))
    if rechazo_fok:                                     # 2º mensaje EXACTO del CLOB como excepción, y confirmado:
        try:
            o = c.get_order(h)                          # FOK muerta -> None (14-Oct); si aparece con relleno, casó
        except Exception as e:
            o = f"{type(e).__name__}: {e}"
        try:
            if o is None:
                return "muerta", o                      # FOK muerta: el servidor no la guarda (14-Oct)
            if isinstance(o, dict) and float(o.get("size_matched") or 0) > 0:
                return "casada", o
            if (isinstance(o, dict) and "size_matched" in o and float(o.get("size_matched") or 0) == 0
                    and str(o.get("status", "")).upper() in ("CANCELED", "CANCELLED")):
                return "muerta", o
        except (TypeError, ValueError):
            pass
        return "ambigua", o                             # cualquier otra forma: no se presume muerte
    if isinstance(res, dict) and res.get("orderID") and str(res["orderID"]).lower() != str(h).lower():
        h = res["orderID"]
    t_fin, o = time.time() + t_max_s, None
    while time.time() < t_fin:
        try:
            o = c.get_order(h)
        except Exception as e:
            o = f"{type(e).__name__}: {e}"
        if isinstance(o, dict):
            try:
                if float(o.get("size_matched") or 0) > 0:
                    return "casada", o
            except (TypeError, ValueError):
                return "ambigua", o
        time.sleep(0.3)
    return "ambigua", o


TAM_CASA = 7.0              # tamaño poco habitual: identifica NUESTRO casado (prints que suman 7 en <= 50 ms)
TOPE_CASADAS_24H = 3       # tope ENTRE ejecuciones (el saldo queda retenido hasta redimir)
# 15-Oct (Javi: "lanza FOK más baratas", "máximo arriesgar 5 euros en total"): modo --barata = 6 acciones del lado NO
# favorito con ask en [0,17, 0,20] (1,02-1,20 $ por orden, el mínimo del CLOB es 5 acc y 1 $). Tope DURO de coste
# acumulado de las órdenes baratas: 5 USDC (< 5 €), contando toda intención salvo las que murieron/rechazadas.
TAM_BARATA = 6.0
BANDA_BARATA = (0.17, 0.20)
TOPE_COSTE_BARATA_USDC = 5.0
MODO = "favorito"


def _coste_barata_ledger():
    """USDC comprometidos por órdenes --barata (TODO el ledger, sin ventana: el tope de Javi es total)."""
    intenciones, cerradas = [], {}
    try:
        with open(LEDGER) as f:
            for ln in f:
                try:
                    e = json.loads(ln)
                except ValueError:
                    continue
                if e.get("modo") != "barata":
                    continue
                if e.get("fase") == "intencion_casa":
                    intenciones.append((e.get("hash"), float(e.get("ask") or 0) * float(e.get("tam") or 0)))
                elif e.get("fase") == "casa":
                    cerradas.setdefault(e.get("hash"), []).append(e.get("estado"))
    except FileNotFoundError:
        pass
    total = 0.0
    for h, coste in intenciones:
        est = cerradas.get(h, [])
        if est and est[0] in ("muerta", "rechazada"):
            est.pop(0)
            continue                                    # no casó: no consumió presupuesto
        total += coste
    return total


def _casadas_ledger_24h():
    """Cuenta para el tope: 'casa' casada/ambigua, y TODA intención sin su 'casa' (el proceso murió tras el POST:
    pudo casar). Ventana 24 h."""
    casas, intenciones = [], []                       # por FILA (no por hash: un hash repetido/None no resta)
    try:
        with open(LEDGER) as f:
            for ln in f:
                try:
                    e = json.loads(ln)
                except ValueError:
                    continue
                if e.get("fase") == "intencion_casa":
                    intenciones.append((e.get("hash"), int(e.get("t") or 0)))
                elif e.get("fase") == "casa":
                    casas.append((e.get("hash"), e.get("estado"), int(e.get("t_envio_ms") or 0)))
    except FileNotFoundError:
        pass
    ahora = er.ahora_ms()
    n = sum(1 for _h, est, t in casas if est in ("casada", "ambigua") and ahora - t < 86_400_000)
    con_casa = [h for h, _e, _t in casas]
    for h, t in intenciones:                            # cada intención sin su 'casa' (emparejadas 1 a 1)
        if h in con_casa:
            con_casa.remove(h)
        elif ahora - t < 86_400_000:
            n += 1
    return n


MS_MIN_FISICO = 120        # nada nuestro puede casar antes: ida ~28 ms + retraso del tomador ~144 ms


def _grupo_nuestro(prints, tk, ask, t0, t_hasta):
    """Subconjuntos de prints de NUESTRO token a precio <= ask (cualquier lado; si casara por acuñación y el feed lo
    imprimiera en el otro token, queda 'ninguna': la medida se pierde, no se falsea) dentro de 50 ms, desde t0 + MS_MIN_FISICO, cuya suma es EXACTAMENTE TAM_CASA. Solo se
    atribuye si hay UNO (o todos empiezan en el mismo print); si hay varios candidatos distintos -> ambigua, no cuenta.
    -> (t_primer_print | None, detalle)."""
    from itertools import combinations
    cands = []
    for (k, t, m) in prints:
        try:
            pr, sz = float(m.get("price")), float(m.get("size"))
        except (TypeError, ValueError):
            continue
        if t < t0 + MS_MIN_FISICO or t > t_hasta or sz > TAM_CASA + 1e-6:
            continue                                    # el casado no puede llegar después del acuse + margen
        if k == tk and pr <= ask + 1e-9:
            cands.append((t, sz, True, pr))
    cands.sort()
    inicios = set()
    hallado = None
    for i in range(len(cands)):
        ventana = [x for x in cands[i:] if x[0] - cands[i][0] <= 50][:11]
        resto = ventana[1:]
        for r in range(0, len(resto) + 1):              # solo subconjuntos que INCLUYEN ventana[0]: <= 2^10 por i
            for sub in combinations(resto, r):
                if abs(ventana[0][1] + sum(x[1] for x in sub) - TAM_CASA) < 1e-6:
                    inicios.add(ventana[0][0])
                    hallado = hallado or [ventana[0], *sub]
    if len(inicios) == 1:
        return min(inicios), {"atribucion": "unica", "grupo": hallado}
    return None, {"atribucion": "ninguna" if not inicios else f"ambigua ({len(inicios)} grupos)", "cands": cands[:8]}


def _desenlace(c, h, res, prints, tk, ask, t0, ack, saldo_antes, espera_s=2.0):
    """Tras el POST de --casa: (estado, orden, t_print, grupo, saldo_despues). Las pruebas (prints únicos del WS, saldo)
    solo pueden SUBIR la alerta a 'ambigua', nunca rebajarla. Probado en tests/test_medir_camino_caliente.py."""
    estado, orden = _resolver_estado(c, h, res)
    time.sleep(espera_s)                                # liquidación on-chain (~1,5 s) y llegada de prints del WS
    t_print, grupo = _grupo_nuestro(list(prints), tk, ask, t0, t0 + ack + 400)   # de ESTA orden
    if estado != "casada" and grupo.get("atribucion") == "unica":
        estado = "ambigua"                              # el WS muestra nuestras 7 acciones: no se presume muerte
    saldo_despues = _saldo_dedicada(c)
    if estado in ("muerta", "rechazada"):
        if saldo_antes is None or saldo_despues is None:
            estado = "ambigua"                          # sin poder comprobar el saldo no se presume muerte
        elif saldo_antes - saldo_despues >= 0.5 * TAM_CASA * ask:
            estado = "ambigua"
    if estado == "casada" and isinstance(orden, dict) and orden.get("size_matched") is not None:
        try:
            if abs(float(orden.get("size_matched") or 0) - TAM_CASA) > 1e-6:
                estado = "ambigua"                      # tamaño imposible para una FOK: anomalía -> cuenta y PARA
                t_print, grupo = None, {**grupo, "atribucion": f"size_matched {orden.get('size_matched')} != {TAM_CASA}"}
        except (TypeError, ValueError):
            estado, t_print = "ambigua", None
    return estado, orden, t_print, grupo, saldo_despues


def casadas(c, n, real):
    from py_clob_client_v2 import PartialCreateOrderOptions, OrderArgs, OrderType
    _lk = _cerrojo_unico()  # noqa: F841 (mantener vivo el cerrojo)
    hechas, por_marco = [], {"5m": 0, "15m": 0}
    t_lim = time.time() + 3600
    saltados = set()
    while len([h for h in hechas if h.get("enviada")]) < n and time.time() < t_lim:
        if real and MODO == "barata" and _coste_barata_ledger() + TAM_CASA * BANDA_BARATA[1] > TOPE_COSTE_BARATA_USDC + 1e-9:
            print(f"⛔ tope de coste de las órdenes baratas: {_coste_barata_ledger():.2f} USDC ya comprometidos "
                  f"(máx {TOPE_COSTE_BARATA_USDC}): PARO")
            break
        if real and MODO == "favorito" and _casadas_ledger_24h() >= TOPE_CASADAS_24H:
            print(f"⛔ ya hay {TOPE_CASADAS_24H} casadas/ambiguas en 24 h en el ledger: tope entre ejecuciones (redimir antes)")
            break
        ms = [m for m in mercados_btc(60, 300) if m[0] not in saltados]
        if not ms:
            time.sleep(10)
            continue
        # alterna 5m/15m: el marco con menos medidas primero (cada 15m cierra a la vez que un 5m)
        ms.sort(key=lambda m: por_marco["15m" if "15m" in m[0] else "5m"])
        slug, fin, toks, neg = ms[0]
        marco = "15m" if "15m" in slug else "5m"
        prints = []
        saltados.add(slug)                              # un intento por mercado, pase lo que pase (sin bucles)

        def al_trade(tk, t_recv, msg, _p=prints):       # lista ligada a ESTA iteración
            _p.append((tk, t_recv, msg))
        try:                                            # precarga de TODO lo que create_order pediría por red
            for tk in toks:                             # calienta la caché del cliente: create_order no irá por red
                c.get_tick_size(tk)
            negs = {bool(c.get_neg_risk(tk)) for tk in toks}
            if negs != {bool(neg)}:
                print(f"{slug}: neg_risk de gamma ({neg}) != CLOB ({negs}): salto mercado (fail-closed)")
                continue
        except Exception as e:
            print(f"{slug}: precarga falló ({type(e).__name__}: {e}); salto mercado")
            time.sleep(5)
            continue
        if real:                                        # todo lo lento, ANTES de la ventana de disparo
            libre = _saldo_dedicada(c)
            if libre is None or libre < TAM_CASA + 1.5:
                print(f"⛔ saldo de la wallet dedicada no apto ({libre}): PARO")
                break
            otro_p = _otro_proceso_wallet_dedicada()
            if otro_p:
                print(f"⛔ otro proceso usa la wallet dedicada ({otro_p}): PARO")
                break
        lib = er.Libro(toks, al_trade=al_trade).iniciar()
        disparo = None

        def apto(tk, otro):
            """(ok, ask) con TODAS las condiciones; se evalúa al elegir Y justo antes del POST."""
            T = fin - time.time()
            if not (15 <= T <= 35 or 55 <= T <= 280) or not (lib.fresco(tk) and lib.fresco(otro)):
                return False, None
            t1, t2 = lib.top.get(tk), lib.top.get(otro)
            if not t1 or not t2 or t1[3] is None or t1[4] is None:
                return False, None
            ask, ask_sz, bid_otro = t1[3], t1[4], t2[1]
            if abs(round(ask * 100) - ask * 100) > 1e-6:
                return False, None                      # solo asks en rejilla de 0,01: 7 × ask con 2 decimales (el
                                                        # CLOB rechaza importes de compra con más; 0,975 no)
            if MODO == "barata":
                ok = BANDA_BARATA[0] <= ask <= BANDA_BARATA[1] and ask_sz >= TAM_CASA
            else:
                ok = 0.97 <= ask <= 0.99 and ask_sz >= TAM_CASA and (bid_otro is None or bid_otro <= 0.03)
            return ok, ask
        live_ok, saldo_antes = None, None
        try:
            while time.time() < fin - 15 and not disparo:
                T_ = fin - time.time()
                if T_ > 280 or 35 < T_ < 55:            # fuera de ventana: antes de T-280, o el disparo de PRECIERRE (T-45)
                    time.sleep(0.2)
                    continue
                if live_ok is None:                     # tras T-45 (PRECIERRE ya disparó): ¿el live opera este cierre?
                    live_ok = not (real and _live_abierto_en(fin))
                    saldo_antes = _saldo_dedicada(c) if real else None
                if not live_ok:
                    print(f"{slug}: el live tiene posición en este cierre: no compito, salto")
                    break
                for i, tk in enumerate(toks):
                    ok, ask = apto(tk, toks[1 - i])
                    if not ok:
                        continue
                    if real and _live_abierto_en(fin):  # re-chequeo del live JUSTO antes de firmar (~ms de disco)
                        live_ok = False
                        break
                    try:                                # tick 0,01 SIEMPRE: el ask ya está en rejilla de 0,01, que es
                                                        # válida con tick 0,01 o 0,001, y 0,01 nunca es "menor" que el
                                                        # mínimo cacheado por el cliente (no lanza)
                        signed = c.create_order(OrderArgs(token_id=tk, price=ask, size=TAM_CASA, side="BUY"),
                                                PartialCreateOrderOptions(tick_size="0.01", neg_risk=neg))
                        h = hash_orden(signed, neg)
                    except Exception as e:
                        print(f"{slug}: firma falló ({type(e).__name__}: {e}): salto mercado")
                        live_ok = False                 # un intento de firma por mercado (sin bucles de E/S)
                        break
                    disparo = (tk, toks[1 - i], ask, h, signed)
                    break
                if live_ok is False:
                    print(f"{slug}: salto mercado (live presente en este cierre o firma fallida)")
                    break
                time.sleep(0.05)
            if not disparo:
                tops = {t[:6]: lib.top.get(t) and lib.top.get(t)[1:4] for t in toks}
                print(f"{slug}: sin favorito apto en T-280..-55 / -35..-15 (fresco {[lib.fresco(t) for t in toks]}, "
                      f"bid/bid_sz/ask {tops})", flush=True)
                continue
            tk, otro, ask, h, signed = disparo
            if not real:
                print(f"[seco] dispararía {slug} ask={ask}")
                hechas.append({"seco": True, "enviada": True})
                continue
            otro_p = _otro_proceso_wallet_dedicada()     # ~ms: justo antes del POST
            if otro_p:
                print(f"⛔ otro proceso usa la wallet dedicada ({otro_p}): PARO")
                break
            if MODO == "barata" and _coste_barata_ledger() + TAM_CASA * ask > TOPE_COSTE_BARATA_USDC + 1e-9:
                print("⛔ esta orden superaría el tope de 5 USDC: PARO")
                break
            ok, ask2 = apto(tk, otro)                   # RE-CHEQUEO COMPLETO justo antes del POST
            if not ok or ask2 != ask:
                print(f"{slug}: condiciones cambiaron antes del POST (ask {ask}->{ask2}): no envío")
                continue
            with open(LEDGER, "a") as f:
                f.write("\n" + json.dumps({"fase": "intencion_casa", "slug": slug, "tok": tk, "ask": ask, "hash": h,
                                           "t": er.ahora_ms(), "modo": MODO, "tam": TAM_CASA}) + "\n")   # "\n" previo: una línea truncada
                                                                            # anterior no se traga esta intención
                f.flush()
                os.fsync(f.fileno())                    # la intención sobrevive a un corte tras el POST
            T = fin - time.time()
            t0, t0n = er.ahora_ms(), time.time_ns()
            try:
                res = c.post_order(signed, OrderType.FOK)
            except Exception as e:
                res = {"error": f"{type(e).__name__}: {e}"}
            ack = (time.time_ns() - t0n) / 1e6
            estado, orden, t_print, grupo, saldo_despues = _desenlace(c, h, res, prints, tk, ask, t0, ack, saldo_antes)
            reg = {"fase": "casa", "modo": MODO, "slug": slug, "marco": marco, "hash": h, "ask": ask, "T": round(T, 2),
                   "ms_ack": round(ack, 1), "estado": estado, "grupo_prints": grupo,
                   "ms_envio_a_primer_print": (t_print - t0) if t_print is not None else None,
                   "t_envio_ms": t0, "res": res, "saldo_antes": saldo_antes, "saldo_despues": saldo_despues}
            reg["estado_orden"] = orden
            with open(LEDGER, "a") as f:
                f.write("\n" + json.dumps(reg, default=str) + "\n")
            print(f"{slug} T={T:.1f} ask={ask} {estado}: ack {ack:.1f} ms, envío->1er print {reg['ms_envio_a_primer_print']} ms "
                  f"({grupo.get('atribucion')})")
            reg["enviada"] = True
            hechas.append(reg)
            por_marco[marco] += 1
            if estado == "ambigua":
                print("⛔ respuesta ambigua: PARO y reviso la wallet dedicada", reg.get("estado_orden"))
                break
        finally:
            lib.parar()
    v = sorted(x["ms_envio_a_primer_print"] for x in hechas if x.get("estado") == "casada"
               and x.get("ms_envio_a_primer_print") is not None)
    print(f"CASADAS: n={len(v)} envío->1er print {v} | acks {sorted(x['ms_ack'] for x in hechas if 'ms_ack' in x)}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--gtc", type=int, default=8)
    ap.add_argument("--fok", type=int, default=8)
    ap.add_argument("--confirmo-dinero-real", action="store_true")
    ap.add_argument("--casa", type=int, default=0)
    ap.add_argument("--barata", action="store_true", help="--casa con 6 acc del lado no favorito a 0,17-0,20 (tope 5 USDC)")
    a = ap.parse_args()
    if a.casa:
        if a.casa > 3:
            sys.exit("--casa máximo 3 (el saldo queda retenido hasta redimir)")
        global MODO, TAM_CASA
        if a.barata:
            MODO, TAM_CASA = "barata", TAM_BARATA
        casadas(cliente_dedicado(), a.casa, a.confirmo_dinero_real)
        return
    if a.gtc > MAX_N or a.fok > MAX_N:
        sys.exit(f"máximo {MAX_N} por tipo")
    real = a.confirmo_dinero_real
    if real:
        _lk = _cerrojo_unico()  # noqa: F841 (mismo cerrojo que --casa: un solo proceso de medición a la vez)
        otro_p = _otro_proceso_wallet_dedicada()
        if otro_p:
            sys.exit(f"⛔ otro proceso usa la wallet dedicada ({otro_p}): no arranco")
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
                if real and "status_code=400" not in str(res):
                    parar = f"GTC con respuesta ambigua (sin orderID ni 400): {res}"   # pudo quedar en el libro
                    break
                print(f"GTC edad {edad} s RECHAZADA: {res}")   # se barre por hash al final
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
            try:                                        # cancelada, pero ¿se rellenó EN PARTE antes?
                o = c.get_order(oid)
                if isinstance(o, dict) and float(o.get("size_matched") or 0) > 0:
                    parar = f"GTC {oid} rellenada en parte ({o.get('size_matched')}) antes de cancelar"
                    break
            except Exception as e:
                parar = f"no se pudo comprobar relleno parcial de {oid}: {type(e).__name__}: {e}"
                break
            time.sleep(0.8)
            tb = primera(-tam, t_c)
            if tb is not None:
                ws_baja.append(tb - t_c)
            time.sleep(0.3)
        for i in range(a.fok if parar is None else 0):
            tam = float(105 + i + 1)                   # entero: importe 1,06..1,13 $ con 2 decimales (el CLOB rechaza más)
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
            txt = str(r["res"]).lower()
            if real and not ("couldn't be fully filled" in txt and "status_code=400" in txt):
                parar = f"FOK sin la muerte explícita del CLOB (posible relleno o red): {str(r['res'])[:200]}"
                break
            if "invalid" in txt or "status_code=400" in txt and "fully" not in txt:
                parar = f"FOK rechazada al validar (no mide el retraso): {str(r['res'])[:200]}"
                break
            res_fok.append(r["ms_post"])
            print(f"FOK {tam}: {r['ms_post']} ms -> {str(r['res'])[:120]}")
            time.sleep(0.5)
    finally:
        for f in futuros:                              # que ningún POST siga en vuelo al barrer (sin tope: el
            try:                                       # cliente HTTP tiene su propio timeout)
                f.result()
            except Exception:
                pass
        if real:
            for h, tipo in enviados:                   # barrido por hash: también las de respuesta ambigua
                try:
                    o = c.get_order(h)
                    st = str((o or {}).get("status", "")).upper() if isinstance(o, dict) else ""
                    if st in ("LIVE", "OPEN"):
                        cr = env.cancelar(h, meta={"barrido": True})
                        o2 = c.get_order(h)
                        if isinstance(o2, dict) and str(o2.get("status", "")).upper() in ("LIVE", "OPEN"):
                            print(f"🚨🚨 ORDEN {h} SIGUE VIVA tras cancelar ({cr.get('res')}): CANCELAR A MANO en la wallet dedicada")
                    if isinstance(o, dict) and float(o.get("size_matched") or 0) > 0:
                        print(f"⚠️ orden {h} ({tipo}) con size_matched={o.get('size_matched')}: hay posición en la wallet dedicada")
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
