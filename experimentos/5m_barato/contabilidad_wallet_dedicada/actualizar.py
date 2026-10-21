#!/usr/bin/env python3
"""Contabilidad completa de la wallet DEDICADA de experimentos (0x659a...297F) -- SOLO LECTURA.

Sin claves, sin .env, sin firmar ni enviar nada. Rerunnable e idempotente: cada ejecucion reconstruye todo desde
fuentes append-only (logs on-chain y data-api) y reescribe las salidas de forma atomica (tmp + rename).

FUENTES (cada cifra sale de una):
  1. ON-CHAIN, verdad del efectivo: eth_getLogs de Transfer(pUSD 0xC011...2DFB) con la wallet como origen o destino,
     DESDE EL BLOQUE 0 hasta la cabeza (una sola consulta por sentido, vía polygon_rpc.py, grupo 'archivo'). El saldo
     se compara con balanceOf en EL MISMO bloque. Clave unica de movimiento: (tx_hash, log_index).
  2. data-api.polymarket.com /activity (TRADE, REDEEM, y cualquier otro tipo): mercado, lado, precio, tamano, comision.
     Se cruza con (1) por tx_hash. Es la fuente de la ATRIBUCION de cada movimiento a mercado/posicion.
  3. gamma-api /markets?condition_ids=..&closed=true: desenlace OFICIAL (outcomePrices exactamente 1/0, closed=true).
     Mercado cerrado sin desenlace limpio = 'pendiente' (nunca se cuenta como realizado ni como cero).
  4. data-api /positions: valoracion (curPrice) de posiciones abiertas, aparte del PnL realizado.
  5. Ledgers del experimento (DL=/root/polymarket-research-datalogs): ventanas de tandas de H47-B (suelo_reiniciado),
     ventana de H47-A, y tx_hash de las ordenes reales de F1 (medir_camino_caliente_ledger.jsonl). Solo para ATRIBUIR.

SALIDAS (en este directorio): movimientos.csv, posiciones.csv, resumen_por_experimento.md, estado_dashboard.json,
  INFORME.md, run_manifest.json, actualizar.log, estado/ (cache: logs pUSD, actividad, bloques, desenlaces).

Uso:  nice -n 19 ionice -c3 python3 actualizar.py [--sin-red] [--sin-informe]
  --sin-red: no consulta RPC/API, recompone desde la cache de estado/ (para pruebas y reproduccion).
"""
import argparse
import csv
import datetime as dt
import hashlib
import json
import os
import sys
import time
from collections import defaultdict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
sys.path.insert(0, str(RAIZ))

WALLET = "0x659a40FF9920fEBc5a66836213040924343d297F"
PUSD = "0xC011a7E12a19f7B1f670d46F03B03f3342E82DFB"
TOPIC_TRANSFER = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
DL = Path("/root/polymarket-research-datalogs")
EST = AQUI / "estado"
DATA_API = "https://data-api.polymarket.com"
GAMMA = "https://gamma-api.polymarket.com"
PAUSA_S = 0.35            # throttle entre llamadas a RPC/API (la API da 429 con muchas consultas)
SCHEMA_VERSION = 1
LOG = AQUI / "actualizar.log"

# ---------------------------------------------------------------- utilidades


def ahora():
    return dt.datetime.now(dt.UTC)


def iso(ts):
    return dt.datetime.fromtimestamp(ts, dt.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def log(msg):
    linea = f"{ahora().strftime('%Y-%m-%dT%H:%M:%SZ')} {msg}"
    print(linea, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(linea + "\n")


def escribir_atomico(ruta: Path, contenido: str):
    tmp = ruta.with_name(ruta.name + f".tmp{os.getpid()}")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(contenido)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, ruta)


def escribir_csv(ruta: Path, cols, filas):
    import io
    b = io.StringIO()
    w = csv.writer(b, lineterminator="\n")
    w.writerow(cols)
    for r in filas:
        w.writerow([r.get(c, "") for c in cols])
    escribir_atomico(ruta, b.getvalue())


def sha256_fichero(p: Path):
    if not p.exists():
        return None
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()[:16]


def cargar_json(p: Path, defecto):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return defecto


def eur(x, nd=4):
    return None if x is None else round(x, nd)


# ---------------------------------------------------------------- red (solo GET / eth_getLogs / eth_call)


def http_get(url, params=None, intentos=5):
    import requests
    espera = 2.0
    ultimo = None
    for _ in range(intentos):
        time.sleep(PAUSA_S)
        try:
            r = requests.get(url, params=params, timeout=30)
            if r.status_code == 429:
                ultimo = RuntimeError("HTTP 429")
                time.sleep(espera)
                espera *= 2
                continue
            r.raise_for_status()
            return r.json()
        except Exception as e:  # noqa: BLE001
            ultimo = e
            time.sleep(espera)
            espera *= 2
    raise RuntimeError(f"GET {url} fallo tras {intentos} intentos: {ultimo}")


def rpc(metodo, params, grupo="archivo"):
    from polygon_rpc import llamar
    time.sleep(PAUSA_S)
    try:
        return llamar(metodo, params, grupo=grupo, intentos=2, plazo_total_s=90, log=None)
    except Exception:
        if grupo == "archivo":     # respaldo: el grupo 'latest' (sirve para bloques recientes)
            return llamar(metodo, params, grupo="latest", intentos=2, plazo_total_s=90, log=None)
        raise


def topic_wallet():
    return "0x" + "0" * 24 + WALLET[2:].lower()


def descargar_logs_pusd():
    """Devuelve (lista de logs, bloque_cabeza, desde_bloque, metodo). Falla en voz alta si la consulta es parcial."""
    head = int(rpc("eth_blockNumber", [], grupo="latest"), 16)
    tw = topic_wallet()
    logs, metodo, desde = [], "completo_desde_bloque_0", 0
    try:
        for tp in ([TOPIC_TRANSFER, None, tw], [TOPIC_TRANSFER, tw, None]):
            logs += rpc("eth_getLogs", [{"fromBlock": "0x0", "toBlock": hex(head), "address": PUSD, "topics": tp}])
    except Exception as e:  # noqa: BLE001
        # Respaldo: trozos de 2 M de bloques desde el 90 M (la wallet no existia antes: primer movimiento 95,2 M).
        log(f"getLogs completo fallo ({type(e).__name__}: {str(e)[:120]}); troceo de 2M bloques desde 90M")
        logs, metodo, desde = [], "troceado_2M_desde_bloque_90000000", 90_000_000
        for ini in range(desde, head + 1, 2_000_000):
            fin = min(ini + 1_999_999, head)
            for tp in ([TOPIC_TRANSFER, None, tw], [TOPIC_TRANSFER, tw, None]):
                logs += rpc("eth_getLogs", [{"fromBlock": hex(ini), "toBlock": hex(fin), "address": PUSD, "topics": tp}])
    return logs, head, desde, metodo


def timestamps_bloques(bloques):
    cache = cargar_json(EST / "bloques.json", {})
    for b in sorted(bloques):
        if str(b) not in cache:
            blk = rpc("eth_getBlockByNumber", [hex(b), False])
            cache[str(b)] = int(blk["timestamp"], 16)
    escribir_atomico(EST / "bloques.json", json.dumps(cache, sort_keys=True))
    return {int(k): v for k, v in cache.items()}


def saldo_pusd_en(bloque):
    sel = "0x70a08231" + "0" * 24 + WALLET[2:].lower()
    res = rpc("eth_call", [{"to": PUSD, "data": sel}, hex(bloque)])
    return int(res, 16)


def descargar_actividad():
    """Todas las filas de /activity en ventanas diarias (evita el tope de offset). Dedup por clave estable."""
    vistas = {}
    ahora_s = int(time.time())
    # ventana de partida: 2026-10-01 (la wallet recibio su primer pUSD el 09-Oct); se amplia hacia atras si hay filas en el borde
    ini = int(dt.datetime(2026, 10, 1, tzinfo=dt.UTC).timestamp())
    t = ini
    while t <= ahora_s:
        fin = min(t + 86400 - 1, ahora_s + 3600)
        off = 0
        while True:
            pag = http_get(f"{DATA_API}/activity", {"user": WALLET, "limit": 500, "offset": off, "start": t, "end": fin,
                                                    "sortDirection": "ASC"})
            for x in pag:
                k = (x["transactionHash"], x.get("type"), x.get("asset") or x.get("conditionId"), x["timestamp"],
                     x.get("size"), x.get("side"))
                vistas[k] = x
            if len(pag) < 500:
                break
            off += 500
            if off >= 3000:
                raise RuntimeError("activity: >3000 filas en un dia, ventana demasiado grande (COBERTURA INCOMPLETA)")
        t += 86400
    return list(vistas.values())


def descargar_posiciones():
    out, off = [], 0
    while True:
        pag = http_get(f"{DATA_API}/positions", {"user": WALLET, "sizeThreshold": 0, "limit": 500, "offset": off})
        out += pag
        if len(pag) < 500:
            break
        off += 500
    return out


def valor_data_api():
    d = http_get(f"{DATA_API}/value", {"user": WALLET})
    return d[0]["value"] if d else None


def resolver_desenlaces(condition_ids):
    """cache inmutable para mercados cerrados con desenlace limpio; los demas se reconsultan siempre."""
    cache = cargar_json(EST / "desenlaces.json", {})
    for c in sorted(condition_ids):
        if c in cache and cache[c].get("estado") == "resuelto":
            continue
        d = http_get(f"{GAMMA}/markets", {"condition_ids": c, "closed": "true"})
        if not d:
            d = http_get(f"{GAMMA}/markets", {"condition_ids": c})
        if not d:
            cache[c] = {"estado": "desconocido", "consultado": iso(time.time())}
            continue
        m = d[0]
        try:
            precios = [float(p) for p in json.loads(m.get("outcomePrices") or "[]")]
        except Exception:  # noqa: BLE001
            precios = []
        limpio = m.get("closed") is True and precios and all(p in (0.0, 1.0) for p in precios) and abs(sum(precios) - 1) < 1e-9
        cache[c] = {"estado": "resuelto" if limpio else ("cerrado_sin_desenlace" if m.get("closed") else "abierto"),
                    "outcomePrices": precios, "slug": m.get("slug"), "endDate": m.get("endDate"),
                    "umaResolutionStatus": m.get("umaResolutionStatus"), "consultado": iso(time.time())}
    escribir_atomico(EST / "desenlaces.json", json.dumps(cache, sort_keys=True))
    return cache


def receta_deposito(txh, sin_red=False):
    """Para entradas sin actividad: origen de la entrada (mint desde 0x0 tras wrap de USDC.e, etc.). Cache por tx."""
    cache = cargar_json(EST / "recibos.json", {})
    if txh not in cache and sin_red:
        return {}
    if txh not in cache:
        r = rpc("eth_getTransactionReceipt", [txh])
        usdce = "0x2791bca1f2de4661ed88a30c99a7a9449aa84174"
        wrap = any(l["address"].lower() == usdce and l["topics"][0] == TOPIC_TRANSFER for l in r["logs"])
        cache[txh] = {"from_tx": r["from"], "to_tx": r["to"], "con_transferencia_usdc_e": wrap}
        escribir_atomico(EST / "recibos.json", json.dumps(cache, sort_keys=True))
    return cache[txh]


# ---------------------------------------------------------------- ledgers (atribucion)


def leer_jsonl(p: Path):
    out = []
    if not p.exists():
        return out
    for linea in p.read_text(encoding="utf-8", errors="replace").splitlines():
        linea = linea.strip()
        if not linea.startswith("{"):
            continue
        try:
            out.append(json.loads(linea))
        except Exception:  # noqa: BLE001
            pass
    return out


def ts_iso_a_epoch(s):
    return dt.datetime.fromisoformat(s).timestamp()


def ventanas_experimentos():
    """H47-B: tandas desde saldo_inicial + cada suelo_reiniciado (motivo 'tanda N'); H47-A: primer/ultimo evento real."""
    b = [d for d in leer_jsonl(DL / "experimento_h47_B_ledger.jsonl") if d.get("real") is True]
    a = [d for d in leer_jsonl(DL / "experimento_h47_A_ledger.jsonl") if d.get("real") is True]
    inicios = []
    for d in b:
        if d["tipo"] == "saldo_inicial" and not inicios:
            inicios.append((1, ts_iso_a_epoch(d["ts"]), "saldo_inicial"))
        if d["tipo"] == "suelo_reiniciado":
            inicios.append((d["n_reinicio"] + 1, ts_iso_a_epoch(d["ts"]), d.get("motivo", "")[:60]))
    tandas = []
    for i, (n, t0, mot) in enumerate(inicios):
        t1 = inicios[i + 1][1] if i + 1 < len(inicios) else None
        tandas.append({"tanda": n, "inicio": t0, "fin": t1, "origen": mot})
    ventana_a = None
    if a:
        ts = [ts_iso_a_epoch(d["ts"]) for d in a]
        ventana_a = {"inicio": min(ts), "fin": (tandas[0]["inicio"] if tandas else max(ts))}
    return tandas, ventana_a, b


def hashes_f1():
    """tx_hash de las ordenes REALES de medir_camino_caliente (F1, 15-Oct) desde su ledger."""
    hs = set()
    for d in leer_jsonl(DL / "medir_camino_caliente_ledger.jsonl"):
        res = d.get("res") or {}
        for h in res.get("transactionsHashes") or []:
            hs.add(h.lower())
    return hs


def atribuir(ts, txh, f1, tandas, ventana_a):
    if txh.lower() in f1:
        return "F1 medir_camino_caliente (15-Oct)", None, "ledger medir_camino_caliente: tx_hash de orden real"
    for t in tandas:
        if ts >= t["inicio"] and (t["fin"] is None or ts < t["fin"]):
            return "H47-B", t["tanda"], "ledger H47-B: ventana de tanda (suelo_reiniciado) por hora del fill"
    if ventana_a and ventana_a["inicio"] <= ts < ventana_a["fin"]:
        return "H47-A", None, "ledger H47-A: ventana de ejecucion real"
    return "NO ATRIBUIDO", None, "fuera de toda ventana de ledger / sin tx_hash en ledger"


# ---------------------------------------------------------------- nucleo


anomalias_info = []   # condiciones resueltas por inferencia desde REDEEM (gamma aun sin desenlace)


def construir(logs, head, desde_bloque, metodo, saldo_chain, ts_bloque, actividad, posiciones, desenl, valor_api, sin_red):
    wl = WALLET.lower()
    # 1) movimientos on-chain, clave (tx, logIndex), orden cronologico
    mov = {}
    for l in logs:
        if l.get("removed"):
            continue
        k = (l["transactionHash"].lower(), int(l["logIndex"], 16))
        f = "0x" + l["topics"][1][-40:]
        t = "0x" + l["topics"][2][-40:]
        v = int(l["data"], 16)
        signo = (1 if t == wl else 0) - (1 if f == wl else 0)
        if signo == 0:      # transferencia wallet->wallet o ajena: no mueve el saldo; se registra por si acaso
            continue
        mov[k] = {"tx": k[0], "log_index": k[1], "bloque": int(l["blockNumber"], 16), "micro": signo * v,
                  "contraparte": t if signo < 0 else f}
    orden = sorted(mov, key=lambda k: (mov[k]["bloque"], k[1]))
    duplicados = len(logs) - len(mov)

    # 2) actividad por tx
    act_tx = defaultdict(list)
    for x in actividad:
        act_tx[x["transactionHash"].lower()].append(x)

    f1 = hashes_f1()
    tandas, ventana_a, _ = ventanas_experimentos()

    # 3) fills (filas TRADE de actividad) con desenlace
    def pago_token(cond, idx):
        d = desenl.get(cond)
        if not d or d.get("estado") != "resuelto":
            return None
        try:
            return d["outcomePrices"][idx]
        except Exception:  # noqa: BLE001
            return None

    precio_pos = {p["asset"]: p for p in posiciones}
    # Respaldo ante retraso de gamma: si ya hay un REDEEM en la cadena para esa condicion, el mercado esta resuelto;
    # el token ganador es el unico que tenemos si sus acciones coinciden con las redimidas (marcado como inferido).
    redimido = defaultdict(float)
    for x in actividad:
        if x.get("type") == "REDEEM":
            redimido[x["conditionId"]] += x["size"]
    tokens_cond = defaultdict(lambda: defaultdict(float))
    for x in actividad:
        if x.get("type") == "TRADE" and x["side"] == "BUY":
            tokens_cond[x["conditionId"]][x["outcomeIndex"]] += x["size"]
    inferidos = set()

    def pago_inferido(cond, idx):
        if cond in redimido and abs(tokens_cond[cond].get(idx, 0) - redimido[cond]) < 1e-6 and len(tokens_cond[cond]) == 1:
            inferidos.add(cond)
            return 1.0
        return None
    fills = []
    for x in sorted(actividad, key=lambda r: (r["timestamp"], r["transactionHash"])):
        if x.get("type") != "TRADE":
            continue
        ts = x["timestamp"]
        exp, tanda, fuente = atribuir(ts, x["transactionHash"], f1, tandas, ventana_a)
        bruto = round(x["size"] * x["price"], 6)
        com = round(x["usdcSize"] - bruto, 6)
        com = com if com > 5e-4 else 0.0
        es_f1 = x["transactionHash"].lower() in f1
        rol = "tomador (FOK, ledger F1)" if es_f1 else ("tomador (inferido: paga comision)" if com > 0 else "maker (inferido: sin comision)")
        pago = pago_token(x["conditionId"], x["outcomeIndex"]) if x["side"] == "BUY" else None
        if pago is None and x["side"] == "BUY":
            pago = pago_inferido(x["conditionId"], x["outcomeIndex"])
        fila = {"tx": x["transactionHash"].lower(), "ts": ts, "slug": x["slug"], "condition_id": x["conditionId"],
                "asset": x["asset"], "outcome": x["outcome"], "outcome_index": x["outcomeIndex"], "side": x["side"],
                "precio": x["price"], "size": x["size"], "coste": x["usdcSize"], "comision": com, "rol": rol,
                "experimento": exp, "tanda": tanda, "fuente_atribucion": fuente}
        if x["side"] != "BUY":
            fila["estado"] = "NO_MODELADO_SELL"
        elif pago is not None:
            fila["estado"] = "liquidada_ganada" if pago == 1.0 else "liquidada_perdida"
            fila["payout"] = x["size"] * pago
            fila["pnl"] = round(fila["payout"] - x["usdcSize"], 6)
        else:
            d = desenl.get(x["conditionId"], {})
            p = precio_pos.get(x["asset"])
            mtm = None if p is None else p.get("curPrice")
            fila["estado"] = "abierta" if d.get("estado") in ("abierto", None) else "pendiente_desenlace"
            fila["mtm_precio"] = mtm
            fila["valor_mtm"] = None if mtm is None else round(x["size"] * mtm, 6)
            fila["pnl_no_realizado"] = None if mtm is None else round(fila["valor_mtm"] - x["usdcSize"], 6)
        fills.append(fila)

    # redenciones: atribuir por conditionId a la fill ganadora
    fills_por_cond = defaultdict(list)
    for fl in fills:
        fills_por_cond[fl["condition_id"]].append(fl)

    # 4) tabla de movimientos con saldo acumulado
    filas, saldo, anomalias = [], 0, []
    tx_vistos_act = set()
    for k in orden:
        m = mov[k]
        bl = ts_bloque.get(m["bloque"])
        acts = act_tx.get(m["tx"], [])
        tipo, slug, exp, tanda, fuente, nota = "", "", "", "", "", ""
        outcome = side = precio = size = com = rol = ""
        if acts:
            tx_vistos_act.add(m["tx"])
            a0 = acts[0]
            tipo = {"TRADE": "COMPRA" if a0.get("side") == "BUY" else "VENTA", "REDEEM": "REDENCION"}.get(a0["type"], a0["type"])
            slug = a0["slug"]
            if a0["type"] == "TRADE":
                fl = next((f for f in fills if f["tx"] == m["tx"]), None)
                exp, tanda, fuente = fl["experimento"], fl["tanda"], fl["fuente_atribucion"]
                outcome, side, precio, size, com, rol = fl["outcome"], fl["side"], fl["precio"], fl["size"], fl["comision"], fl["rol"]
                if abs(abs(m["micro"]) / 1e6 - a0["usdcSize"]) > 1e-6:
                    anomalias.append(f"importe on-chain {abs(m['micro'])/1e6} != actividad {a0['usdcSize']} en {m['tx'][:12]}")
            else:  # REDEEM
                fl_c = fills_por_cond.get(a0["conditionId"], [])
                gan = [f for f in fl_c if f["estado"] == "liquidada_ganada"] or fl_c
                exps = {(f["experimento"], f["tanda"]) for f in gan}
                if len(exps) == 1:
                    exp, tanda = next(iter(exps))
                    fuente = "cruce por conditionId con la fill ganadora"
                elif exps:
                    exp, fuente, nota = "MIXTO", "conditionId con fills de varias tandas", "redencion repartida"
                else:
                    exp, fuente = "NO ATRIBUIDO", "redencion sin fill conocida"
                size = a0["size"]
                outcome = a0.get("outcome", "")
        else:
            if m["micro"] > 0:
                rec = receta_deposito(m["tx"], sin_red)
                tipo = "DEPOSITO" if rec.get("con_transferencia_usdc_e") else "ENTRADA_SIN_ACTIVIDAD"
                nota = ("mint de pUSD tras wrap de USDC.e (tx de %s)" % rec.get("from_tx", "?")) if tipo == "DEPOSITO" else "entrada sin fila de actividad ni wrap de USDC.e"
                exp, fuente = "CAPITAL (no es experimento)", "on-chain: sin actividad de mercado"
            else:
                tipo, nota = "SALIDA_SIN_ACTIVIDAD", "salida sin fila de actividad (retirada u otro)"
                exp, fuente = "NO ATRIBUIDO", "sin actividad"
        saldo += m["micro"]
        filas.append({"fecha_utc": iso(bl) if bl else "", "ts": bl, "bloque": m["bloque"], "tx": m["tx"], "log_index": m["log_index"],
                      "tipo": tipo, "importe_pusd": m["micro"] / 1e6, "saldo_acumulado": saldo / 1e6, "mercado": slug,
                      "outcome": outcome, "side": side, "precio": precio, "size": size, "comision_est": com, "rol": rol,
                      "experimento": exp, "tanda_B": tanda, "fuente_atribucion": fuente, "nota": nota})

    act_sin_chain = [x for x in actividad if x["transactionHash"].lower() not in {m["tx"] for m in mov.values()}]
    if inferidos:
        anomalias_info.extend(sorted(inferidos))
    return filas, saldo, fills, tandas, ventana_a, anomalias, duplicados, act_sin_chain


def agregar(fills, filtro=None):
    sel = [f for f in fills if (filtro is None or filtro(f)) and f["side"] == "BUY"]
    liq = [f for f in sel if f["estado"].startswith("liquidada")]
    abi = [f for f in sel if not f["estado"].startswith("liquidada")]
    pos = {(f["condition_id"], f["asset"]) for f in sel}
    pos_liq = {(f["condition_id"], f["asset"]) for f in liq}
    coste_liq = sum(f["coste"] for f in liq)
    pnl_liq = sum(f["pnl"] for f in liq)
    # por posicion (mercado-lado): el "relleno" economico
    por_pos = defaultdict(float)
    for f in liq:
        por_pos[(f["condition_id"], f["asset"])] += f["pnl"]
    top2 = sum(sorted(por_pos.values(), reverse=True)[:2])
    return {"pnl_realizado_sin_2_mejores_posiciones": round(pnl_liq - top2, 6) if len(por_pos) > 2 else None,
            "n_filas": len(sel), "n_posiciones": len(pos), "n_posiciones_liquidadas": len(pos_liq),
            "n_filas_liquidadas": len(liq), "n_filas_abiertas_o_pendientes": len(abi),
            "ganadoras_posiciones": sum(1 for v in por_pos.values() if v > 0),
            "perdedoras_posiciones": sum(1 for v in por_pos.values() if v <= 0),
            "acciones": round(sum(f["size"] for f in sel), 6), "coste_total": round(sum(f["coste"] for f in sel), 6),
            "coste_liquidado": round(coste_liq, 6), "payout_liquidado": round(sum(f["payout"] for f in liq), 6),
            "pnl_realizado": round(pnl_liq, 6), "comisiones": round(sum(f["comision"] for f in sel), 6),
            "coste_abierto_pendiente": round(sum(f["coste"] for f in abi), 6),
            "valor_mtm_abierto": round(sum(f.get("valor_mtm") or 0 for f in abi), 6),
            "pnl_no_realizado_mtm": round(sum(f.get("pnl_no_realizado") or 0 for f in abi), 6),
            "mtm_faltante": sum(1 for f in abi if f.get("valor_mtm") is None),
            "ev_ponderado_por_euro": None if coste_liq == 0 else round(pnl_liq / coste_liq, 6),
            "euro_por_fila": None if not liq else round(pnl_liq / len(liq), 6),
            "euro_por_posicion": None if not pos_liq else round(pnl_liq / len(pos_liq), 6)}


def conciliar_ledger_B(fills):
    """Acciones por slug: ledger H47-B vs actividad on-chain (ventana B). Ledger por slug = puja_fin.llenas_detectadas;
    si el mercado no tiene puja_fin (ejecucion parada antes de cerrarlo) se usa relleno_tardio (trae slug) y, en su
    defecto, un gemelo_relleno emparejado por hora (+-5 s), precio y acciones con un fill on-chain aun no explicado."""
    led = defaultdict(float)
    tard = defaultdict(float)
    gem = []
    for d in leer_jsonl(DL / "experimento_h47_B_ledger.jsonl"):
        if d.get("real") is not True:
            continue
        if d["tipo"] == "puja_fin":
            led[d["slug"]] += d.get("llenas_detectadas", 0) or 0
        elif d["tipo"] == "relleno_tardio":
            tard[d["slug"]] += d["acc"]
        elif d["tipo"] == "gemelo_relleno":
            gem.append((ts_iso_a_epoch(d["ts"]), d["precio"], d["acc_total"]))
    for slug, v in tard.items():
        if slug not in led:
            led[slug] = v
    chain = defaultdict(float)
    for f in fills:
        if f["experimento"] == "H47-B":
            chain[f["slug"]] += f["size"]
    usados = set()
    for s_ in sorted(set(chain) - set(led)):
        for f in fills:
            if f["experimento"] != "H47-B" or f["slug"] != s_:
                continue
            for k, (t, pr, acc) in enumerate(gem):
                if k not in usados and abs(t - f["ts"]) <= 5 and abs(pr - f["precio"]) < 1e-9 and abs(acc - f["size"]) < 1e-6:
                    usados.add(k)
                    led[s_] += acc
                    break
    difs = []
    for s_ in sorted(set(led) | set(chain)):
        if abs(led.get(s_, 0) - chain.get(s_, 0)) > 1e-6:
            difs.append({"slug": s_, "ledger": led.get(s_), "onchain": chain.get(s_)})
    return {"mercados_con_fill_en_ledger": sum(1 for v in led.values() if v > 0), "mercados_con_fill_onchain": len(chain),
            "discrepancias": difs, "acciones_ledger": round(sum(led.values()), 6), "acciones_onchain": round(sum(chain.values()), 6)}


def fin_mercado(slug):
    try:
        marco = slug.split("-")[2]
        dur = {"5m": 300, "15m": 900}.get(marco)
        return int(slug.rsplit("-", 1)[1]) + dur if dur else None
    except Exception:  # noqa: BLE001
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-red", action="store_true")
    ap.add_argument("--sin-informe", action="store_true")
    args = ap.parse_args()
    EST.mkdir(exist_ok=True)
    t_ini = ahora()
    log(f"inicio actualizar.py sin_red={args.sin_red}")
    errores = []

    if not args.sin_red:
        logs, head, desde, metodo = descargar_logs_pusd()
        # cache append-only de logs (clave tx+logIndex); lo nuevo se anade, lo existente se valida igual
        previos = {(l["transactionHash"], l["logIndex"]): l for l in cargar_json(EST / "pusd_logs.json", [])}
        for l in logs:
            previos[(l["transactionHash"], l["logIndex"])] = l
        logs_todos = list(previos.values())
        ts_bloque = timestamps_bloques({int(l["blockNumber"], 16) for l in logs_todos})
        saldo_chain = saldo_pusd_en(head)
        ts_head = int(rpc("eth_getBlockByNumber", [hex(head), False], grupo="latest")["timestamp"], 16)
        actividad_bruta = descargar_actividad()
        # foto coherente: solo actividad hasta la hora del bloque cabeza (lo posterior aun no esta en la cadena consultada)
        actividad = [a for a in actividad_bruta if a["timestamp"] <= ts_head]
        if len(actividad) != len(actividad_bruta):
            log(f"aviso: {len(actividad_bruta) - len(actividad)} filas de actividad posteriores al bloque {head} descartadas (se recogen en la proxima ejecucion)")
        posiciones = descargar_posiciones()
        valor_api = valor_data_api()
        conds = {x["conditionId"] for x in actividad if x.get("type") == "TRADE"}
        desenl = resolver_desenlaces(conds)
        escribir_atomico(EST / "pusd_logs.json", json.dumps(logs_todos, sort_keys=True))
        escribir_atomico(EST / "actividad.json", json.dumps(actividad, sort_keys=True))
        escribir_atomico(EST / "posiciones.json", json.dumps(posiciones, sort_keys=True))
        escribir_atomico(EST / "cuadre_cadena.json", json.dumps({"head": head, "saldo_micro": saldo_chain, "ts_head": ts_head,
                                                                 "valor_api": valor_api, "desde": desde, "metodo": metodo}))
    else:
        logs_todos = cargar_json(EST / "pusd_logs.json", [])
        actividad = cargar_json(EST / "actividad.json", [])
        posiciones = cargar_json(EST / "posiciones.json", [])
        desenl = cargar_json(EST / "desenlaces.json", {})
        c = cargar_json(EST / "cuadre_cadena.json", {})
        head, saldo_chain, ts_head, valor_api = c["head"], c["saldo_micro"], c["ts_head"], c.get("valor_api")
        desde, metodo = c.get("desde", 0), c.get("metodo", "cache")
        ts_bloque = {int(k): v for k, v in cargar_json(EST / "bloques.json", {}).items()}

    filas, saldo_mov, fills, tandas, ventana_a, anomalias, dup, act_sin_chain = construir(
        logs_todos, head, desde, metodo, saldo_chain, ts_bloque, actividad, posiciones, desenl, valor_api, args.sin_red)

    # ------------------------------------------------------------ cuadre
    depositos = sum(f["importe_pusd"] for f in filas if f["tipo"] in ("DEPOSITO", "ENTRADA_SIN_ACTIVIDAD"))
    retiradas = -sum(f["importe_pusd"] for f in filas if f["tipo"] == "SALIDA_SIN_ACTIVIDAD")
    capital_neto = depositos - retiradas
    compras = -sum(f["importe_pusd"] for f in filas if f["tipo"] == "COMPRA")
    redenciones = sum(f["importe_pusd"] for f in filas if f["tipo"] == "REDENCION")
    ventas = sum(f["importe_pusd"] for f in filas if f["tipo"] == "VENTA")
    otros = sum(f["importe_pusd"] for f in filas if f["tipo"] not in ("DEPOSITO", "ENTRADA_SIN_ACTIVIDAD", "SALIDA_SIN_ACTIVIDAD", "COMPRA", "REDENCION", "VENTA"))
    saldo_chain_f = saldo_chain / 1e6
    dif = saldo_mov / 1e6 - saldo_chain_f

    tot = agregar(fills)
    ganadoras_sin_redimir = [f for f in fills if f["estado"] == "liquidada_ganada"]
    redim_conds = {a["conditionId"] for a in actividad if a.get("type") == "REDEEM"}
    por_cobrar = round(sum(f["payout"] for f in ganadoras_sin_redimir if f["condition_id"] not in redim_conds), 6)
    valor_pos = tot["valor_mtm_abierto"] + por_cobrar
    pnl_cash_total = saldo_chain_f - capital_neto + valor_pos          # identidad de efectivo
    pnl_fills_total = tot["pnl_realizado"] + tot["pnl_no_realizado_mtm"]  # suma por fills
    # redenciones ganadoras = payout de las ganadoras ya redimidas
    payout_redimido = sum(f["payout"] for f in ganadoras_sin_redimir if f["condition_id"] in redim_conds)
    comprobaciones = [
        {"nombre": "saldo_movimientos_vs_balanceOf_mismo_bloque", "ok": abs(dif) < 1e-6, "diferencia_pusd": round(dif, 6)},
        {"nombre": "identidad_efectivo_vs_suma_por_fills(PnL)", "ok": abs(pnl_cash_total - pnl_fills_total) < 1e-4 and tot["mtm_faltante"] == 0,
         "diferencia_pusd": round(pnl_cash_total - pnl_fills_total, 6)},
        {"nombre": "redenciones_onchain_vs_payout_ganadoras_redimidas", "ok": abs(redenciones - payout_redimido) < 1e-6,
         "diferencia_pusd": round(redenciones - payout_redimido, 6)},
        {"nombre": "importes_onchain_vs_actividad_por_tx", "ok": not anomalias, "anomalias": anomalias},
        {"nombre": "actividad_sin_transferencia_onchain", "ok": not act_sin_chain, "n": len(act_sin_chain)},
        {"nombre": "valoracion_abiertas_vs_data_api_value(informativo)", "ok": valor_api is None or abs(valor_api - valor_pos) < 0.5,
         "diferencia_pusd": None if valor_api is None else round(valor_api - valor_pos, 6)},
        {"nombre": "sin_ventas_ni_otros_tipos_no_modelados", "ok": ventas == 0 and otros == 0 and not any(f["estado"] == "NO_MODELADO_SELL" for f in fills)},
        {"nombre": "fills_sin_atribuir", "ok": all(f["experimento"] != "NO ATRIBUIDO" for f in fills),
         "n": sum(1 for f in fills if f["experimento"] == "NO ATRIBUIDO")},
    ]
    cuadra = comprobaciones[0]["ok"] and comprobaciones[1]["ok"]
    motivo = "" if cuadra else "; ".join(f"{c['nombre']}: dif {c.get('diferencia_pusd')}" for c in comprobaciones[:2] if not c["ok"])
    if abs(dif) < 1e-6 and not comprobaciones[1]["ok"]:
        motivo = "el efectivo on-chain cuadra, pero la suma por fills no reproduce el PnL de efectivo (ver comprobaciones)"

    # ------------------------------------------------------------ agregados por experimento y tanda
    exps = sorted({f["experimento"] for f in fills})
    por_exp = []
    for e in exps:
        a = agregar(fills, lambda f, e=e: f["experimento"] == e)
        a["experimento"] = e
        por_exp.append(a)
    # H47-A: sin fills; mostrarlo explicitamente
    if "H47-A" not in exps and ventana_a:
        a = agregar([], None)
        a["experimento"] = "H47-A"
        a["nota"] = f"sin fills en actividad on-chain entre {iso(ventana_a['inicio'])} y {iso(ventana_a['fin'])}"
        por_exp.append(a)
    por_tanda = []
    for t in tandas:
        a = agregar(fills, lambda f, n=t["tanda"]: f["experimento"] == "H47-B" and f["tanda"] == n)
        a.update({"tanda": t["tanda"], "inicio_utc": iso(t["inicio"]), "fin_utc": iso(t["fin"]) if t["fin"] else None,
                  "origen": t["origen"]})
        por_tanda.append(a)

    # ------------------------------------------------------------ posiciones.csv
    pos_filas = []
    grp = defaultdict(list)
    for f in fills:
        grp[(f["condition_id"], f["asset"], f["experimento"], f["tanda"])].append(f)
    for (c, asset, e, tnd), fs in sorted(grp.items(), key=lambda kv: kv[1][0]["ts"]):
        buys = [f for f in fs if f["side"] == "BUY"]
        sz = sum(f["size"] for f in buys)
        cost = sum(f["coste"] for f in buys)
        est = fs[0]["estado"] if len({f["estado"] for f in fs}) == 1 else "mixto"
        pnl = sum(f.get("pnl", 0) for f in buys) if est.startswith("liquidada") else None
        mtm = sum(f.get("valor_mtm") or 0 for f in buys) if not est.startswith("liquidada") else None
        pos_filas.append({"fecha_primer_fill_utc": iso(fs[0]["ts"]), "mercado": fs[0]["slug"], "condition_id": c, "outcome": fs[0]["outcome"],
                          "experimento": e, "tanda_B": tnd, "n_filas": len(fs), "acciones": round(sz, 6), "coste": round(cost, 6),
                          "precio_medio": round(cost / sz, 6) if sz else "", "comision": round(sum(f["comision"] for f in buys), 6),
                          "estado": est, "payout": round(sum(f.get("payout", 0) for f in buys), 6) if est.startswith("liquidada") else "",
                          "pnl_realizado": round(pnl, 6) if pnl is not None else "", "valor_mtm": round(mtm, 6) if mtm is not None else "",
                          "rol": fs[0]["rol"], "fin_mercado_utc": iso(fin_mercado(fs[0]["slug"])) if fin_mercado(fs[0]["slug"]) else ""})

    # ------------------------------------------------------------ serie diaria
    dias = []
    if filas:
        d0 = dt.datetime.fromtimestamp(filas[0]["ts"], dt.UTC).date()
        d1 = ahora().date()
        liq_dia = defaultdict(float)
        for f in fills:
            if f["estado"].startswith("liquidada"):
                fm = fin_mercado(f["slug"]) or f["ts"]
                liq_dia[dt.datetime.fromtimestamp(fm, dt.UTC).date()] += f["pnl"]
        d = d0
        acum_pnl = 0.0
        while d <= d1:
            fin_dia = dt.datetime(d.year, d.month, d.day, 23, 59, 59, tzinfo=dt.UTC).timestamp()
            s = [r for r in filas if r["ts"] <= fin_dia]
            saldo_d = s[-1]["saldo_acumulado"] if s else 0.0
            dep_d = sum(r["importe_pusd"] for r in s if r["tipo"] in ("DEPOSITO", "ENTRADA_SIN_ACTIVIDAD"))
            acum_pnl += liq_dia.get(d, 0.0)
            dias.append({"fecha": d.isoformat(), "saldo_cierre_pusd": round(saldo_d, 6), "depositos_acum": round(dep_d, 6),
                         "pnl_liquidado_dia": round(liq_dia.get(d, 0.0), 6), "pnl_liquidado_acum": round(acum_pnl, 6),
                         "n_movimientos": sum(1 for r in filas if dt.datetime.fromtimestamp(r["ts"], dt.UTC).date() == d)})
            d += dt.timedelta(days=1)

    conc = conciliar_ledger_B(fills)
    abiertas = [f for f in fills if f["side"] == "BUY" and not f["estado"].startswith("liquidada")]
    detalle_abiertas = [{"mercado": f["slug"], "outcome": f["outcome"], "acciones": f["size"], "coste": f["coste"], "mtm_precio": f.get("mtm_precio"),
                         "valor_mtm": f.get("valor_mtm"), "estado": f["estado"], "experimento": f["experimento"], "tanda_B": f["tanda"]} for f in abiertas]

    cobertura = {"onchain": {"metodo": metodo, "desde_bloque": desde, "hasta_bloque": head, "transferencias_pusd_wallet": len(filas),
                             "duplicados_descartados": dup, "primer_movimiento_utc": filas[0]["fecha_utc"] if filas else None,
                             "ultimo_movimiento_utc": filas[-1]["fecha_utc"] if filas else None},
                 "desenlaces_inferidos_de_redeem": len(anomalias_info),
                 "actividad_data_api": {"filas": len(actividad), "tipos": sorted({a.get("type") for a in actividad}),
                                        "ventana": "ventanas diarias desde 2026-10-01 (wallet sin movimientos antes del 09-Oct segun on-chain)"},
                 "desenlaces_gamma": {"mercados": len(desenl), "resueltos": sum(1 for d in desenl.values() if d.get("estado") == "resuelto"),
                                      "otros": {e: sum(1 for d in desenl.values() if d.get("estado") == e) for e in sorted({d.get("estado") for d in desenl.values()} - {"resuelto"})}},
                 "rewards_y_rebates": "ninguna entrada de pUSD distinta de depositos y redenciones observada; si Polymarket paga rebates/rewards de maker fuera de esta wallet o con retraso NO es verificable aqui",
                 "conciliacion_ledger_B": {k: conc[k] for k in ("mercados_con_fill_en_ledger", "mercados_con_fill_onchain", "acciones_ledger", "acciones_onchain")} | {"n_discrepancias": len(conc["discrepancias"])}}

    estado = {
        "schema_version": SCHEMA_VERSION, "generado_utc": ahora().strftime("%Y-%m-%dT%H:%M:%SZ"), "wallet": WALLET,
        "saldo": {"pusd_onchain": round(saldo_chain_f, 6), "bloque": head, "ts_utc": iso(ts_head),
                  "suma_movimientos": round(saldo_mov / 1e6, 6)},
        "capital": {"depositos": round(depositos, 6), "retiradas": round(retiradas, 6), "depositado_neto": round(capital_neto, 6)},
        "pnl": {"realizado_total": tot["pnl_realizado"], "no_realizado_mtm": tot["pnl_no_realizado_mtm"],
                "total_efectivo_mas_posiciones": round(pnl_cash_total, 6), "saldo_menos_capital_neto": round(saldo_chain_f - capital_neto, 6),
                "ganadoras_por_redimir_pusd": por_cobrar, "comisiones_pagadas": tot["comisiones"],
                "n_filas_fill": tot["n_filas"], "n_posiciones": tot["n_posiciones"],
                "euro_por_fila_liquidada": tot["euro_por_fila"], "euro_por_posicion_liquidada": tot["euro_por_posicion"],
                "ev_ponderado_por_euro": tot["ev_ponderado_por_euro"]},
        "por_experimento": por_exp, "tandas_B": por_tanda,
        "posiciones_abiertas": {"n_filas": len(abiertas), "coste": tot["coste_abierto_pendiente"], "valor_mtm": tot["valor_mtm_abierto"],
                                "valor_data_api_value": valor_api, "detalle": detalle_abiertas},
        "cuadre": {"ok": bool(cuadra), "diferencia_pusd": round(dif, 6), "motivo": motivo, "tolerancia_pusd": 1e-6,
                   "comprobaciones": comprobaciones},
        "cobertura": cobertura,
        "ultimos_movimientos": [{k: r[k] for k in ("fecha_utc", "tipo", "importe_pusd", "saldo_acumulado", "mercado", "experimento", "tanda_B", "tx")}
                                for r in filas[-50:][::-1]],
        "serie_diaria": dias,
        "no_atribuido": {"fills": sum(1 for f in fills if f["experimento"] == "NO ATRIBUIDO"),
                         "movimientos_no_atribuidos": sum(1 for r in filas if r["experimento"] == "NO ATRIBUIDO")},
    }

    # ------------------------------------------------------------ escritura
    cols = ["fecha_utc", "bloque", "tx", "log_index", "tipo", "importe_pusd", "saldo_acumulado", "mercado", "outcome", "side", "precio",
            "size", "comision_est", "rol", "experimento", "tanda_B", "fuente_atribucion", "nota"]
    escribir_csv(AQUI / "movimientos.csv", cols, filas)
    escribir_csv(AQUI / "posiciones.csv", list(pos_filas[0].keys()) if pos_filas else ["vacio"], pos_filas)
    escribir_atomico(AQUI / "estado_dashboard.json", json.dumps(estado, indent=1, ensure_ascii=False))
    escribir_atomico(AQUI / "resumen_por_experimento.md", md_resumen(estado, conc, fills))
    if not args.sin_informe:
        escribir_atomico(AQUI / "INFORME.md", md_informe(estado, conc))
    manifest = {"job": "contabilidad_wallet_dedicada", "codigo_sha256": sha256_fichero(Path(__file__)), "wallet": WALLET,
                "inicio": t_ini.strftime("%Y-%m-%dT%H:%M:%SZ"), "fin": ahora().strftime("%Y-%m-%dT%H:%M:%SZ"),
                "sin_red": args.sin_red, "cobertura": cobertura, "cuadre_ok": bool(cuadra), "estado": "COMPLETE" if cuadra else "PARTIAL",
                "entradas_sha256": {n: sha256_fichero(EST / n) for n in ("pusd_logs.json", "actividad.json", "desenlaces.json")},
                "reproducir": "nice -n 19 ionice -c3 python3 " + str(Path(__file__)), "errores": errores}
    escribir_atomico(AQUI / "run_manifest.json", json.dumps(manifest, indent=1))
    log(f"fin: movimientos={len(filas)} fills={len(fills)} cuadre_ok={cuadra} dif={dif} pnl_realizado={tot['pnl_realizado']}")
    return 0 if cuadra else 2


# ---------------------------------------------------------------- informes


def fmt(x, nd=2):
    return "n/d" if x is None else f"{x:+.{nd}f}"


def md_resumen(e, conc, fills):
    L = [f"# Resumen por experimento -- wallet dedicada {e['wallet']}", "",
         f"Generado {e['generado_utc']} por actualizar.py. Fuente: pUSD on-chain (hasta bloque {e['saldo']['bloque']}) + data-api + gamma + ledgers. Cifras en pUSD (~ USD).", "",
         f"Saldo on-chain {e['saldo']['pusd_onchain']:.6f} ({e['saldo']['ts_utc']}); capital depositado neto {e['capital']['depositado_neto']:.2f}; "
         f"cuadre {'OK' if e['cuadre']['ok'] else 'NO CUADRA'} (dif {e['cuadre']['diferencia_pusd']}).", "",
         "## PnL por experimento (PnL realizado = mercados con desenlace oficial: payout - coste incl. comision; abiertas aparte, nunca en el realizado)", "",
         "| experimento | filas | posiciones (liq.) | ganadoras/perdedoras | coste liq. | payout liq. | PnL realizado | PnL sin 2 mejores pos. | EV pond. por EUR | EUR/fila | comisiones | abiertas/pend.: coste | MTM abierto |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for a in e["por_experimento"]:
        L.append(f"| {a['experimento']} | {a['n_filas']} | {a['n_posiciones']} ({a['n_posiciones_liquidadas']}) | {a['ganadoras_posiciones']}/{a['perdedoras_posiciones']} | "
                 f"{a['coste_liquidado']:.2f} | {a['payout_liquidado']:.2f} | {fmt(a['pnl_realizado'])} | {fmt(a['pnl_realizado_sin_2_mejores_posiciones'])} | {fmt(a['ev_ponderado_por_euro'],3)} | {fmt(a['euro_por_fila'],3)} | "
                 f"{a['comisiones']:.4f} | {a['coste_abierto_pendiente']:.2f} | {a['valor_mtm_abierto']:.2f} |")
    L += ["", "PnL realizado sin las 2 mejores posiciones = trampa 'PnL concentrado en 1-2 episodios' (CLAUDE.md raiz): una muestra de pocos aciertos baratos domina el total.", "", "## H47-B por tanda (la tanda de cada fill sale de su hora frente a los suelo_reiniciado del ledger; el PnL de una posicion se imputa a la tanda en que se rellenó)", "",
          "| tanda | inicio UTC | fin UTC | filas | pos. liq. | gan/perd | coste liq. | PnL realizado | EV pond./EUR | EUR/fila | abiertas coste | MTM |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for a in e["tandas_B"]:
        L.append(f"| {a['tanda']} | {a['inicio_utc']} | {a['fin_utc'] or 'abierta'} | {a['n_filas']} | {a['n_posiciones_liquidadas']} | {a['ganadoras_posiciones']}/{a['perdedoras_posiciones']} | "
                 f"{a['coste_liquidado']:.2f} | {fmt(a['pnl_realizado'])} | {fmt(a['ev_ponderado_por_euro'],3)} | {fmt(a['euro_por_fila'],3)} | {a['coste_abierto_pendiente']:.2f} | {a['valor_mtm_abierto']:.2f} |")
    L += ["", "## Cuadre", ""]
    for c in e["cuadre"]["comprobaciones"]:
        L.append(f"- {'OK ' if c['ok'] else 'FALLA'} {c['nombre']}: " + json.dumps({k: v for k, v in c.items() if k not in ('nombre', 'ok')}, ensure_ascii=False))
    L += ["", "## Conciliacion ledger H47-B vs on-chain (acciones por mercado)", "",
          f"Mercados con fill: ledger {conc['mercados_con_fill_en_ledger']}, on-chain {conc['mercados_con_fill_onchain']}; acciones ledger {conc['acciones_ledger']} vs on-chain {conc['acciones_onchain']}; discrepancias {len(conc['discrepancias'])}."]
    for d in conc["discrepancias"][:30]:
        L.append(f"- {d['slug']}: ledger {d['ledger']} vs on-chain {d['onchain']}")
    L += ["", "## Limites", "",
          "- Atribucion a tanda por hora del fill (la actividad on-chain no lleva el oid); H47-A y F1 por ventana/tx_hash de ledger.",
          "- Rol maker/tomador INFERIDO por la comision (maker no paga); F1 tomador por ledger.",
          f"- {e['cobertura']['rewards_y_rebates']}.",
          "- Posiciones abiertas valoradas al curPrice de data-api (precio medio del mercado, no realizable): fuera del PnL realizado."]
    return "\n".join(L) + "\n"


def md_informe(e, conc):
    p, c, s = e["pnl"], e["capital"], e["saldo"]
    ex = {a["experimento"]: a for a in e["por_experimento"]}
    def lin(n):
        a = ex.get(n)
        return f"{n}: PnL realizado {fmt(a['pnl_realizado'])} (filas {a['n_filas']}, EV pond. {fmt(a['ev_ponderado_por_euro'],3)}/EUR)" if a else f"{n}: sin fills"
    L = [f"# INFORME contabilidad wallet dedicada ({e['wallet'][:10]}...) -- generado {e['generado_utc']}", "",
         f"Saldo on-chain {s['pusd_onchain']:.4f} pUSD (bloque {s['bloque']}, {s['ts_utc']}); depositado neto {c['depositado_neto']:.2f}; saldo - capital = {fmt(p['saldo_menos_capital_neto'])}.",
         f"PnL realizado total {fmt(p['realizado_total'])} (n={p['n_filas_fill']} filas, {p['n_posiciones']} posiciones); no realizado MTM {fmt(p['no_realizado_mtm'])}; ganadoras por redimir {p['ganadoras_por_redimir_pusd']:.2f}; comisiones {p['comisiones_pagadas']:.4f}.",
         "Por experimento: " + " | ".join(lin(n) for n in ("F1 medir_camino_caliente (15-Oct)", "H47-A", "H47-B")) + ". Tandas B en resumen_por_experimento.md.",
         f"CUADRE: {'CIERRA' if e['cuadre']['ok'] else 'NO CIERRA'} (dif {e['cuadre']['diferencia_pusd']} pUSD; {e['cuadre']['motivo'] or 'sin motivo pendiente'}). Detalle en estado_dashboard.json::cuadre.comprobaciones.",
         f"Fuente/cobertura: pUSD Transfer (eth_getLogs, {e['cobertura']['onchain']['metodo']}, bloque {e['cobertura']['onchain']['desde_bloque']}..{s['bloque']}, {e['cobertura']['onchain']['transferencias_pusd_wallet']} movimientos) + data-api /activity ({e['cobertura']['actividad_data_api']['filas']} filas) + gamma (desenlaces {e['cobertura']['desenlaces_gamma']['resueltos']}/{e['cobertura']['desenlaces_gamma']['mercados']}).",
         f"Conciliacion ledger H47-B vs on-chain: {conc['acciones_ledger']} vs {conc['acciones_onchain']} acciones, {len(conc['discrepancias'])} discrepancias. No atribuido: {e['no_atribuido']['fills']} fills.",
         "Sin sesgo de supervivencia: cada fill se resuelve con desenlace oficial (gamma); sin desenlace = abierta/pendiente (aparte, valorada a curPrice).",
         "Rewards/rebates: ninguna entrada distinta de deposito/redencion; no verificable si se pagan fuera o con retraso.",
         "", "Reproducir: `nice -n 19 ionice -c3 ulimit -v 2500000; python3 experimentos/5m_barato/contabilidad_wallet_dedicada/actualizar.py` (idempotente; `--sin-red` recompone de la cache estado/).",
         "", "## Esquema estado_dashboard.json (schema_version 1, escritura atomica tmp+rename)",
         "- saldo{pusd_onchain,bloque,ts_utc,suma_movimientos}; capital{depositos,retiradas,depositado_neto}",
         "- pnl{realizado_total,no_realizado_mtm,total_efectivo_mas_posiciones,saldo_menos_capital_neto,ganadoras_por_redimir_pusd,comisiones_pagadas,n_filas_fill,n_posiciones,euro_por_fila_liquidada,euro_por_posicion_liquidada,ev_ponderado_por_euro}",
         "- por_experimento[] y tandas_B[]: n_filas,n_posiciones,n_posiciones_liquidadas,ganadoras_posiciones,perdedoras_posiciones,acciones,coste_total,coste_liquidado,payout_liquidado,pnl_realizado,comisiones,coste_abierto_pendiente,valor_mtm_abierto,pnl_no_realizado_mtm,ev_ponderado_por_euro,euro_por_fila,euro_por_posicion (+experimento | tanda,inicio_utc,fin_utc)",
         "- posiciones_abiertas{n_filas,coste,valor_mtm,valor_data_api_value,detalle[]}; cuadre{ok,diferencia_pusd,motivo,tolerancia_pusd,comprobaciones[]}",
         "- cobertura{onchain,actividad_data_api,desenlaces_gamma,rewards_y_rebates,conciliacion_ledger_B}; ultimos_movimientos[50]; serie_diaria[{fecha,saldo_cierre_pusd,depositos_acum,pnl_liquidado_dia,pnl_liquidado_acum,n_movimientos}]; no_atribuido{}",
         "- Valores desconocidos = null (nunca 0). Campos nuevos solo se anaden; un cambio incompatible sube schema_version."]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    sys.exit(main())
