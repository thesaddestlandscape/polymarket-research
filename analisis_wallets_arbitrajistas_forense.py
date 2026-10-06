#!/usr/bin/env python3
"""analisis_wallets_arbitrajistas_forense.py -- B2 paso 1 (06-Oct, Javi: "reverse engineering forense de los wallets que
capturan la ventana que nosotros no alcanzamos"). REGLA: separar lo OBSERVADO de lo COMPATIBLE.

Fuentes y qué demuestra cada una:
  on-chain (onchain_fills_*.csv.gz): identidad EXACTA de maker y tomador de cada relleno, lado de la orden, importes,
    comisión; hora = bloque (~1,5 s, ts_est). En un casado: filas maker=X,taker=W (W tomador consumiendo la orden de X)
    y una fila resumen maker=W,taker=EXCHANGE (la orden tomadora de W). Fila maker=W,taker!=EXCHANGE = orden EN REPOSO de
    W llenada (W fue MAKER).
  registro ms (maker_ms_*.csv.gz): mapa token -> moneda/marco/mercado/cierre/lado (k); operaciones del WS del CLOB
    con hora del EXCHANGE en ms (t: precio, lado, tamaño); top del libro en cada cambio (q).
  EMPAREJAMIENTO on-chain <-> operación ms: mismo token, |precio| <= 0,005, tamaño ±1 %, |hora bloque - hora exchange|
    <= 4 s; único candidato -> el relleno de W hereda la hora del exchange en ms (OBSERVADO si el emparejamiento es
    único; si hay varios candidatos se descarta).
Salida: fichas por wallet + pickle con el detalle para los pasos siguientes.
Uso: --wallets 0x..,0x.. [--out pickle]
"""
import argparse
import bisect
import collections
import csv
import glob
import gzip
import pickle
from datetime import datetime
from pathlib import Path

DL = "/root/polymarket-research-datalogs"
EX = "0xe111180000d2663c0091e4f400237545b87b996b"


def precio_y_shares(r):
    ma, ta = float(r["maker_amt"] or 0), float(r["taker_amt"] or 0)
    if not ma or not ta:
        return None, None
    if r["side"] == "0":          # la orden de la fila COMPRA: paga USDC (maker_amt), recibe tokens (taker_amt)
        return ma / ta, ta
    return ta / ma, ma            # VENDE tokens (maker_amt) por USDC (taker_amt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--wallets", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    W = [w.lower() for w in a.wallets.split(",")]
    # ---- on-chain: filas de las wallets + filas de sus contrapartes en los mismos tx
    rel = []
    for f in sorted(glob.glob(f"{DL}/onchain_fills_*.csv.gz")):
        try:
            for r in csv.DictReader(gzip.open(f, "rt")):
                if r["maker"].lower() in W or r["taker"].lower() in W:
                    rel.append(r)
        except (EOFError, OSError):
            pass
    toks = {r["token_id"] for r in rel}
    ventanas = collections.defaultdict(list)      # token -> instantes (ms) de sus rellenos
    for r in rel:
        ventanas[r["token_id"]].append(float(r["ts_est"]) * 1000)
    for k in ventanas:
        ventanas[k].sort()

    def cerca(tok, t, margen):
        v = ventanas.get(tok)
        if not v:
            return False
        i = bisect.bisect_left(v, t - margen)
        return i < len(v) and v[i] <= t + margen

    # ---- registro ms
    meta, trades, libro = {}, collections.defaultdict(list), collections.defaultdict(list)
    for f in sorted(glob.glob(f"{DL}/maker_ms_*.csv.gz"), key=lambda f: Path(f).stat().st_mtime):
        try:
            for ln in gzip.open(f, "rt"):
                c = ln.rstrip("\n").split(",")
                if c[0] == "k":
                    meta[c[2]] = (c[3], c[4], c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
                elif c[0] == "t" and c[2] in toks:
                    te = int(c[1])
                    if cerca(c[2], te, 6000):
                        trades[c[2]].append((te, float(c[3]), c[4], float(c[5]), int(c[6]) if len(c) > 6 and c[6] else None))
                elif c[0] == "q" and c[2] in toks:
                    te = int(c[1])
                    if cerca(c[2], te, 8000):
                        f_ = lambda x: None if x in ("", "None") else float(x)
                        libro[c[2]].append((te, f_(c[3]), f_(c[4]), f_(c[5]) or 0.0, f_(c[6]) or 0.0))
        except (EOFError, OSError):
            pass
    for d in (trades, libro):
        for k in d:
            d[k].sort(key=lambda x: x[0])
    # ---- emparejar cada relleno on-chain con su operación ms
    emp = {}
    usados = set()
    for r in rel:
        p, sh = precio_y_shares(r)
        if p is None:
            continue
        tb = float(r["ts_est"]) * 1000
        cand = [x for x in trades.get(r["token_id"], []) if abs(x[0] - tb) <= 4000 and abs(x[1] - p) <= 0.005
                and abs(x[3] - sh) <= max(0.01 * sh, 0.011)]
        key = (r["tx"], r["log_index"])
        if len(cand) == 1 and (r["token_id"], cand[0][0], cand[0][3]) not in usados:
            emp[key] = cand[0]
            usados.add((r["token_id"], cand[0][0], cand[0][3]))
    pickle.dump({"rel": rel, "meta": meta, "trades": dict(trades), "libro": dict(libro), "emp": emp, "W": W},
                open(a.out, "wb"))
    # ---- fichas
    for w in W:
        mk = [r for r in rel if r["maker"].lower() == w and r["taker"].lower() != EX]
        tk = [r for r in rel if r["maker"].lower() == w and r["taker"].lower() == EX]
        todas = mk + tk
        en_reg = [r for r in todas if r["token_id"] in meta]
        marcos = collections.Counter(meta[r["token_id"]][1] for r in en_reg)
        monedas = collections.Counter(meta[r["token_id"]][0] for r in en_reg)
        # contrapartes
        contra = collections.Counter()
        for r in rel:
            if r["taker"].lower() == w:
                contra[r["maker"].lower()] += 1
            elif r["maker"].lower() == w and r["taker"].lower() != EX:
                contra[r["taker"].lower()] += 1
        # ¿compra los dos lados del mismo mercado? ¿y pares 5m/15m del mismo cierre?
        por_merc = collections.defaultdict(set)
        por_cierre = collections.defaultdict(set)
        for r in en_reg:
            mo, ma_, mid, cie, lado = meta[r["token_id"]]
            por_merc[mid].add(lado)
            por_cierre[(mo, cie)].add((ma_, lado))
        ambos = sum(1 for v in por_merc.values() if len(v) == 2)
        anidados = sum(1 for v in por_cierre.values() if any(x[0] == "5min" for x in v) and any(x[0] == "15min" for x in v))
        det = mk + [r for r in rel if r["taker"].lower() == w]     # filas por relleno individual (las emparejables)
        n_emp = sum(1 for r in det if (r["tx"], r["log_index"]) in emp)
        print(f"\n=== {w} ===")
        print(f"  rellenos: MAKER {len(mk)} | TOMADOR {len(tk)} | en mercados cripto del registro {len(en_reg)}/{len(todas)} "
              f"| rellenos individuales {len(det)}, con hora ms emparejada {n_emp}")
        print(f"  marcos {dict(marcos)} | monedas {dict(monedas.most_common(6))}")
        print(f"  mercados con compra de AMBOS lados (YES y NO) {ambos}/{len(por_merc)} | cierres con 5m y 15m a la vez "
              f"{anidados}/{len(por_cierre)}")
        print(f"  contrapartes principales: {contra.most_common(4)}")
        ps = [precio_y_shares(r)[0] for r in todas if precio_y_shares(r)[0] is not None]
        if ps:
            ps.sort()
            print(f"  precio de compra P10/P50/P90: {ps[len(ps) // 10]:.3f} {ps[len(ps) // 2]:.3f} {ps[int(len(ps) * .9)]:.3f}")


if __name__ == "__main__":
    main()
