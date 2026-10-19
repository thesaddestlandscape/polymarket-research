#!/usr/bin/env python3
"""r5k_io.py -- lectores de solo lectura para A6 (libro5 T/G/B, mapa de tokens k, banda on-chain de pass1, desenlaces).
Sin escritura en producción. Los extractos TG/B se generan fuera (grep sobre libro5, ver LEEME_A6.txt)."""
import csv
import glob
import gzip
import json
import os
import sys
from datetime import datetime, timezone

DES_CACHES = ("/root/polymarket-research/experimentos/5m_barato/h43_auditoria_datos/des_cache_descubrimiento.json",
              "/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json")


def tokens_btc5(kfiles):
    """token -> (mkt, lado, cierre_epoch_s) de las filas k (k,t_ms,token,act,marco,mkt,fin_iso,lado) BTC 5min."""
    out = {}
    for f in kfiles:
        with open(f, errors="replace") as fh:
            for ln in fh:
                c = ln.rstrip("\n").split(",")
                if len(c) >= 8 and c[3] == "BTC" and c[4] == "5min" and c[2] not in out:
                    try:
                        fin = datetime.fromisoformat(c[6]).timestamp()
                    except ValueError:
                        continue
                    out[c[2]] = (c[5], c[7], fin)
    return out


def eventos_libro5(tg_files, b_files, tokens):
    """Itera (seq-ordenado por fichero) eventos de libro5 de los tokens BTC 5m: ('T', recv_ms, t_ev_ms, token, precio, side,
    size) | ('G', recv_ms, token|None, motivo) | ('B', recv_ms, token). Los ficheros se dan en orden cronológico; un
    fichero = un proceso; dentro, el orden es seq (NUNCA t_ms: sello de lote)."""
    for tg in tg_files:
        base = os.path.basename(tg).replace(".TG.gz", "")
        bf = [b for b in b_files if os.path.basename(b).replace(".B.gz", "") == base]
        ev = []
        with gzip.open(tg, "rt", errors="replace") as fh:
            for ln in fh:
                c = ln.rstrip("\n").split(",")
                try:
                    if c[0] == "T":
                        if c[2] in tokens:
                            ev.append((int(c[7]), ("T", int(c[6]), int(c[1]), c[2], float(c[3]), c[4], float(c[5]))))
                    elif c[0] == "G":
                        tk = None if c[2] == "*" else c[2]
                        if tk is None or tk in tokens:
                            ev.append((int(c[7]), ("G", int(c[6]), tk, c[3])))
                except (IndexError, ValueError):
                    continue          # última línea cortada
        for b in bf:
            with gzip.open(b, "rt", errors="replace") as fh:
                for ln in fh:
                    c = ln.rstrip("\n").split(",")
                    try:
                        if len(c) >= 5 and c[2] in tokens:
                            ev.append((int(c[4]), ("B", int(c[3]), c[2])))
                    except ValueError:
                        continue
        ev.sort(key=lambda x: x[0])
        for _s, e in ev:
            yield e


def banda_cadena(band_files):
    """Filas de banda on-chain de pass1 (solo BTC): dict con ts(est), tx, li, mkt, lado, pc, acc, coste, T."""
    rows = []
    for f in band_files:
        with gzip.open(f, "rt") as fh:
            rd = csv.reader(fh)
            h = next(rd)
            ix = {k: i for i, k in enumerate(h)}
            for c in rd:
                if c[ix["act"]] != "BTC":
                    continue
                rows.append({"ts": float(c[ix["ts"]]), "tx": c[ix["tx"]], "li": int(float(c[ix["li"]])), "mkt": c[ix["mkt"]],
                             "lado": c[ix["lado_c"]], "pc": float(c[ix["pc"]]), "acc": float(c[ix["acc"]]),
                             "coste": float(c[ix["coste"]]), "T": float(c[ix["T"]])})
    return rows


def desenlaces_cache():
    des = {}
    for f in DES_CACHES:
        if os.path.exists(f):
            des.update(json.load(open(f)))
    return des


EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"


def tomadores_cadena(onchain_gz, tokens):
    """Eventos a nivel de ORDEN TOMADORA desde las filas F del exchange (taker == EXCH: la fila resume lo que casó el
    tomador en esa orden). Devuelve [(ts_est, tx, li, token, 'BUY'|'SELL', acciones, usdc)] de los tokens dados.
    side=1 (vende): acciones=maker_amt, usdc=taker_amt; side=0 (compra): usdc=maker_amt, acciones=taker_amt."""
    out = []
    with gzip.open(onchain_gz, "rt", errors="replace") as fh:
        rd = csv.reader(fh)
        next(rd)
        for c in rd:
            if c[0] != "F" or c[7] != EXCH or c[9] not in tokens:
                continue
            try:
                ma, ta = float(c[10]), float(c[11])
                side = int(c[8])
                out.append((float(c[2]), c[3], int(c[4]), c[9], "SELL" if side == 1 else "BUY",
                            ma if side == 1 else ta, ta if side == 1 else ma))
            except ValueError:
                continue
    return out


def banda_cadena_cruda(onchain_gz, tokens, lo=0.10, hi=0.30, t_min=60.0, t_max=300.0):
    """Mismas filas de banda que pass1.py (maker-level) calculadas directamente de las filas F del exchange, sin inventario
    ni historial de precios. tokens: token -> (mkt, lado, cierre_s). Fila maker = F con taker != EXCH.
    Maker VENDE (side=1): acc=maker_amt, usdc=taker_amt, lado_c=opuesto, pc=1-usdc/acc. Maker COMPRA (side=0): acc=taker_amt,
    usdc=maker_amt, lado_c=lado, pc=usdc/acc. coste = acc*pc; T = cierre - ts_est."""
    rows = []
    opp = {"YES": "NO", "NO": "YES"}
    with gzip.open(onchain_gz, "rt", errors="replace") as fh:
        rd = csv.reader(fh)
        next(rd)
        for c in rd:
            if c[0] != "F" or c[7] == EXCH:
                continue
            t = tokens.get(c[9])
            if t is None:
                continue
            try:
                side, ma, ta, ts = int(c[8]), float(c[10]), float(c[11]), float(c[2])
            except ValueError:
                continue
            venta = side == 1
            acc, usdc = (ma, ta) if venta else (ta, ma)
            if acc <= 0:
                continue
            mkt, lado, cierre = t
            lado_c = opp[lado] if venta else lado
            pc = 1 - usdc / acc if venta else usdc / acc
            coste = acc - usdc if venta else usdc
            T = cierre - ts
            if not (lo < pc <= hi and t_min < T <= t_max and coste > 0):
                continue
            rows.append({"ts": ts, "tx": c[3], "li": int(c[4]), "mkt": mkt, "lado": lado_c, "pc": round(pc, 4), "acc": acc,
                         "coste": round(coste, 5), "T": round(T, 1)})
    return rows


def desenlaces_gamma(mids, cache_path):
    """Desenlace oficial de los mercados que faltan en las cachés, por gamma-api pública (closed=true; resolución cuando
    outcomePrices >= 0,999). Caché PROPIA (no toca las de producción). Ausente = missing, nunca inventado."""
    import requests
    try:
        c = json.load(open(cache_path))
    except Exception:
        c = {}
    pend = sorted(m for m in set(mids) if m not in c)
    ses = requests.Session()
    for k in range(0, len(pend), 40):
        try:
            for m in ses.get("https://gamma-api.polymarket.com/markets", timeout=20,
                             params=[("id", x) for x in pend[k:k + 40]] + [("closed", "true"), ("limit", "40")]).json() or []:
                pr = m.get("outcomePrices")
                pr = json.loads(pr) if isinstance(pr, str) else pr
                if pr and float(pr[0]) >= 0.999:
                    c[str(m["id"])] = "YES"
                elif pr and float(pr[1]) >= 0.999:
                    c[str(m["id"])] = "NO"
        except Exception as e:
            print(f"  desenlaces_gamma lote {k // 40}: {type(e).__name__}", file=sys.stderr)
    if pend:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        json.dump(c, open(cache_path, "w"))
    return c
