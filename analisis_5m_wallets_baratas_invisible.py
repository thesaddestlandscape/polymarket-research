#!/usr/bin/env python3
"""analisis_5m_wallets_baratas_invisible.py — FASE 2 (lo INVISIBLE) del estudio de wallets que compran barato en BTC 5m
(Javi 15-Oct: "entender tanto lo visible como lo invisible para utilizarlo a nuestro favor"). SOLO LECTURA.

Grupos: PERSIST = top 20 wallets persistentes por PnL TEST (datalogs/m5barato_mision/baratas_wallets.csv, fase 1);
MOMONEY = @mo-money 0x32ed2e54…; CONTROL = muestra (1 de cada 5) del resto de compras MAKER baratas en los mismos días.
Unidad = relleno maker de COMPRA a precio <= 0,20 en BTC 5m (OrderFilled: fila del dueño `maker`, taker != exchange).
Contexto en t_ctx = hora de BLOQUE − 2 s (la hora on-chain es la del bloque, ~1,5 s de resolución; sin look-ahead) desde
el registro ms (m5_registro_D: q = top por recepción; x = Binance; m15_registro_D: bid del 15m):
  edad_top_s  = segundos que el MEJOR BID del token lleva >= al precio del relleno (¿estaba la orden colocada antes?)
  spread, mid, bsz (tamaño del mejor bid), T (s al cierre)
  bn5_bps     = retorno de Binance en [t_ctx − 5 s, t_ctx] en la DIRECCIÓN del lado comprado (+ = a favor)
  d15         = cambio del bid del 15m del mismo lado en [t_ctx − 1 s, t_ctx] (solo 5m que cierran con un 15m)
Resultado: acierto y EV/€ (maker sin comisión) por grupo y por tramos de cada rasgo -> ¿qué rellenos BUSCAN o EVITAN?
Salida: datalogs/m5barato_mision/invisible_fills_D.csv.gz (caché) + invisible_informe.txt
Uso: nice -n 19 ionice -c3 python3 analisis_5m_wallets_baratas_invisible.py [--dias ...]
"""
import argparse
import bisect
import collections
import csv
import gzip
import hashlib
import json
import os
import random
import sys
import time
from array import array
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_5m_barato_quien_gana import mapas, EXCH  # noqa: E402
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
DIAS = [f"2026-10-{d:02d}" for d in range(5, 15)]
MOMONEY = "0x32ed2e546b187ca15e2841edc82b22c713cf8ec3"
P_MAX = 0.20
CTX_MS = 2000

IN_DIR = OUT                                        # entradas de la fase 1 (baratas_wallets.csv): fijas aunque se cambie --out
TRUNCADOS = set()                                   # días cuyo m5_registro de origen estaba truncado (no se cachean)


def escribir_atomico(ruta, texto):
    """Escritura atómica (tmp + fsync + os.replace): un kill nunca deja el fichero final a medias."""
    ruta = Path(ruta)
    tmp = ruta.with_name(ruta.name + ".tmp")
    with open(tmp, "w") as fh:
        fh.write(texto)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, ruta)


def leer_cache(cache):
    """DataFrame de la caché o None. Se lee ENTERA (el CRC del gz detecta truncados); si falla o no tiene filas se borra
    y se recalcula (una caché vacía no cuenta como válida)."""
    if not cache.exists():
        return None
    try:
        df = pd.read_csv(cache)
    except (EOFError, OSError, UnicodeDecodeError, ValueError, csv.Error, pd.errors.ParserError) as e:   # EmptyDataError es ValueError
        print(f"  {cache.name}: caché corrupta ({type(e).__name__}) -> se borra y se recalcula", file=sys.stderr, flush=True)
        cache.unlink()
        return None
    if not len(df):
        print(f"  {cache.name}: caché sin filas -> se borra y se recalcula", file=sys.stderr, flush=True)
        cache.unlink()
        return None
    return df


def escribir_cache(cache, df):
    """Caché atómica (gz a <cache>.tmp + os.replace)."""
    tmp = cache.with_name(cache.name + ".tmp")
    df.to_csv(tmp, index=False, compression="gzip")
    with open(tmp, "rb") as fh:
        os.fsync(fh.fileno())
    os.replace(tmp, cache)


def grupos():
    r = pd.read_csv(IN_DIR / "baratas_wallets.csv", index_col=0)
    persist = set(r.sort_values("pnl_t", ascending=False).head(20).index.str.lower())
    return persist


def fills_dia(d, persist):
    tok = {t: v for t, v in mapas(d)["5min"].items() if v[0] == "BTC"}   # token -> (activo, mercado, cierre, lado)
    rnd = random.Random(f"control#{d}")
    filas = []
    with gzip.open(VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz", "rt") as fh:
        for x in pd.read_csv(fh, chunksize=300_000, dtype={"token_id": str, "maker": str, "taker": str},
                             usecols=["tipo", "ts_est", "maker", "taker", "side", "token_id", "maker_amt", "taker_amt"]):
            x = x[(x.tipo == "F") & (x.side == 0) & x.token_id.isin(tok.keys()) & (x.taker.str.lower() != EXCH)]
            if not len(x):
                continue
            usdc, acc = x.maker_amt.astype(float), x.taker_amt.astype(float)
            pr = usdc / acc.where(acc > 0)
            x = x.assign(p=pr, usdc=usdc, acc=acc)
            x = x[(x.p > 0) & (x.p <= P_MAX)]
            for r in x.itertuples(index=False):
                w = r.maker.lower()
                g = "PERSIST" if w in persist else "MOMONEY" if w == MOMONEY else None
                if g is None:
                    if rnd.random() >= 0.2:
                        continue
                    g = "CONTROL"
                a, mkt, cie, lado = tok[r.token_id]
                filas.append((g, w, r.token_id, str(mkt), int(cie), lado, int(float(r.ts_est) * 1000), float(r.p),
                              float(r.usdc), float(r.acc)))
    return filas, tok


def series(d, tokens):
    """Mejor bid/ask por token 5m (q), Binance (x) y bid 15m BTC por (cierre_ms, lado)."""
    q = {}
    bn_t, bn_p = array("q"), array("d")
    with gzip.open(VOL / "m5_registro" / f"m5_registro_{d}.csv.gz", "rt", errors="replace") as fh:
        try:
            for ln in fh:
                tp = ln[:2]
                if tp == "x,":
                    c = ln.split(",")
                    if c[2] == "BTCUSDT":
                        try:
                            bn_t.append(int(c[7]))
                            bn_p.append(float(c[3]))
                        except (ValueError, IndexError):
                            pass
                    continue
                if tp != "q,":
                    continue
                c = ln.rstrip("\n").split(",")
                if c[2] not in tokens or c[3] in ("", "None") or c[4] in ("", "None"):
                    continue
                try:
                    s = q.setdefault(c[2], (array("q"), array("d"), array("d"), array("d")))
                    s[0].append(int(c[7]))
                    s[1].append(float(c[3]))
                    s[2].append(float(c[4]))
                    s[3].append(float(c[5]) if c[5] not in ("", "None") else 0.0)
                except (ValueError, IndexError):
                    continue
        except (EOFError, OSError):
            TRUNCADOS.add(d)

    def ordenar(cols):
        o = sorted(range(len(cols[0])), key=cols[0].__getitem__)
        return tuple(array(c.typecode, (c[i] for i in o)) for c in cols)
    q = {k: ordenar(v) for k, v in q.items()}
    bn = ordenar((bn_t, bn_p))
    s15 = {}
    meta15 = {}
    f15 = VOL / "m15_registro" / f"m15_registro_{d}.csv.gz"
    if f15.exists():
        with gzip.open(f15, "rt", errors="replace") as fh:
            try:
                for ln in fh:
                    tp = ln[:2]
                    if tp == "k,":
                        c = ln.rstrip("\n").split(",")
                        if len(c) >= 8 and c[3] == "BTC" and c[4] == "15min":
                            meta15[c[2]] = (int(datetime.fromisoformat(c[6]).timestamp()), c[7])
                        continue
                    if tp != "q,":
                        continue
                    c = ln.rstrip("\n").split(",")
                    m = meta15.get(c[2])
                    if not m or c[3] in ("", "None"):
                        continue
                    try:
                        s = s15.setdefault(m, (array("q"), array("d")))
                        s[0].append(int(c[7]))
                        s[1].append(float(c[3]))
                    except (ValueError, IndexError):
                        continue
            except (EOFError, OSError):
                pass
    s15 = {k: ordenar(v) for k, v in s15.items()}
    return q, bn, s15


def en(serie, t):
    i = bisect.bisect_right(serie[0], t) - 1
    return i


def dia(d, persist):
    cache = OUT / f"invisible_fills_{d}.csv.gz"
    c_ = leer_cache(cache)
    if c_ is not None:
        return c_
    if not (VOL / "m5_onchain" / f"m5_onchain_{d}.csv.gz").exists() or \
            not (VOL / "m5_registro" / f"m5_registro_{d}.csv.gz").exists():
        return None                                  # AUSENTE: falta el on-chain o el registro del día
    filas, tok = fills_dia(d, persist)
    if not filas:
        print(f"  {d}: dia_sin_filas (on-chain presente, 0 rellenos maker baratos): no se cachea", flush=True)
        return pd.DataFrame()
    q, bn, s15 = series(d, {f[2] for f in filas})
    des = desenlaces({f[3] for f in filas})
    out = []
    for g, w, tk, mkt, cie, lado, t_b, p, usdc, acc in filas:
        r = des.get(mkt)
        if r not in ("YES", "NO") or tk not in q:
            continue
        t = t_b - CTX_MS
        s = q[tk]
        i = en(s, t)
        if i < 0:
            continue
        bid, ask, bsz = s[1][i], s[2][i], s[3][i]
        k = i                                           # edad: desde cuándo el mejor bid es >= p sin interrupción
        while k >= 0 and s[1][k] >= p - 1e-9:
            k -= 1
        edad = (t - s[0][k + 1]) / 1000.0 if k + 1 <= i and s[1][i] >= p - 1e-9 else 0.0
        j, j5 = en(bn, t), en(bn, t - 5000)
        bn5 = (bn[1][j] / bn[1][j5] - 1) * 1e4 if j >= 0 and j5 >= 0 else float("nan")
        bn5 = bn5 if lado == "YES" else -bn5           # en la dirección del lado comprado
        d15 = float("nan")
        if cie % 900 == 0 and (cie, lado) in s15:
            s_ = s15[(cie, lado)]
            a1, a0 = en(s_, t), en(s_, t - 1000)
            if a1 >= 0 and a0 >= 0:
                d15 = s_[1][a1] - s_[1][a0]
        out.append({"dia": d, "grupo": g, "wallet": w, "mkt": mkt, "lado": lado, "p": p, "usdc": usdc, "acc": acc,
                    "gana": int(r == lado), "T": (cie * 1000 - t_b) / 1000.0, "edad_top_s": round(edad, 2),
                    "spread": round(ask - bid, 4), "mid": round((ask + bid) / 2, 4), "bsz": bsz,
                    "bn5_bps": round(bn5, 3), "d15": d15})
    df = pd.DataFrame(out)
    if not len(df):
        print(f"  {d}: dia_sin_filas (rellenos sin desenlace/serie): no se cachea", flush=True)
    elif d in TRUNCADOS:
        print(f"  {d}: origen truncado: resultado parcial, no se cachea", flush=True)
    else:
        OUT.mkdir(parents=True, exist_ok=True)
        escribir_cache(cache, df)
    return df


def ev(x):
    return float((x.acc * x.gana).sum() / x.usdc.sum() - 1) if len(x) and x.usdc.sum() > 0 else float("nan")


def main():
    global OUT
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default=",".join(DIAS))
    ap.add_argument("--out", default=str(OUT), help="directorio de cachés/informe/manifiesto (por defecto el real)")
    a = ap.parse_args()
    OUT = Path(a.out)
    OUT.mkdir(parents=True, exist_ok=True)
    pedidos = a.dias.split(",")
    man = {"job": "analisis_5m_wallets_baratas_invisible", "script": Path(__file__).name,
           "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "args": vars(a), "dias_pedidos": pedidos, "dias_ok": [], "dias_ausentes": [], "dias_sin_filas": [],
           "dias_truncados": [], "dias_fallidos": {}, "inicio_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           "fin_utc": None, "estado": "RUNNING"}
    man_f = OUT / "manifiesto_invisible.json"
    escribir_atomico(man_f, json.dumps(man, indent=1))
    persist = grupos()
    partes = []
    for d in pedidos:
        try:
            r = dia(d, persist)
        except Exception as e:                       # un día roto no tumba el resto ni deja el manifiesto en RUNNING
            man["dias_fallidos"][d] = f"{type(e).__name__}: {e}"
            print(f"  {d}: FALLIDO {man['dias_fallidos'][d]}", file=sys.stderr, flush=True)
            escribir_atomico(man_f, json.dumps(man, indent=1))
            continue
        if r is None:
            man["dias_ausentes"].append(d)
            print(f"  {d}: AUSENTE (sin m5_onchain o m5_registro)", flush=True)
        elif not len(r):
            man["dias_sin_filas"].append(d)
        else:
            partes.append(r)
            man["dias_ok"].append(d)
            if d in TRUNCADOS:
                man["dias_truncados"].append(d)
            print(f"  {d}: {len(r)} rellenos", flush=True)
        escribir_atomico(man_f, json.dumps(man, indent=1))   # resumen parcial tras cada día
    completo = len(man["dias_ok"]) == len(pedidos) and not man["dias_truncados"] and not man["dias_fallidos"]
    cobertura = (f"COBERTURA: {len(man['dias_ok'])}/{len(pedidos)} días con filas | ausentes: "
                 f"{man['dias_ausentes'] or 'ninguno'} | sin filas: {man['dias_sin_filas'] or 'ninguno'} | origen truncado: "
                 f"{man['dias_truncados'] or 'ninguno'} | fallidos: {list(man['dias_fallidos']) or 'ninguno'} | "
                 f"VEREDICTO {'COMPLETE' if completo else 'PARTIAL'}")
    df = pd.concat(partes, ignore_index=True) if partes else pd.DataFrame(columns=["grupo"])
    lines = [cobertura, "FASE 2 (lo invisible) — rellenos MAKER de compra a <= 0,20 en BTC 5m; contexto a hora de bloque − 2 s",
             f"Grupos: PERSIST = top 20 persistentes (fase 1); MOMONEY; CONTROL = 1/5 del resto. Días {DIAS[0]}..{DIAS[-1]}"]
    for g, x in df.groupby("grupo"):
        lines.append(f"\n== {g}: rellenos {len(x)} wallets {x.wallet.nunique()} | EV/€ {ev(x):+.3f} | acierto {x.gana.mean():.3f}"
                     f" vs precio pond {x.usdc.sum() / x.acc.sum():.3f}")
        lines.append(f"   medianas: precio {x.p.median():.3f} T {x['T'].median():.0f} s | edad_top {x.edad_top_s.median():.1f} s"
                     f" | spread {x.spread.median():.3f} | bsz {x.bsz.median():.0f} | bn5 {x.bn5_bps.median():+.2f} bps"
                     f" | d15 {x.d15.median():+.3f} (n {x.d15.notna().sum()})")
        for col, cortes in (("edad_top_s", (0, 1, 5, 30, 1e9)), ("bn5_bps", (-1e9, -2, -0.5, 0.5, 2, 1e9)),
                            ("T", (0, 60, 120, 180, 240, 301)), ("spread", (0, 0.015, 0.035, 1))):
            partes_ = []
            for lo, hi in zip(cortes[:-1], cortes[1:]):
                y = x[(x[col] >= lo) & (x[col] < hi)]
                if len(y) >= 30:
                    partes_.append(f"[{lo:g},{hi:g}) n{len(y)} EV{ev(y):+.2f} frac{len(y) / len(x):.0%}")
            lines.append(f"   {col:10s}: " + " | ".join(partes_))
    txt = "\n".join(lines)
    print(txt)
    escribir_atomico(OUT / "invisible_informe.txt", txt + "\n")
    man["estado"] = "COMPLETE" if completo else "PARTIAL"
    man["fin_utc"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    escribir_atomico(man_f, json.dumps(man, indent=1))


if __name__ == "__main__":
    main()
