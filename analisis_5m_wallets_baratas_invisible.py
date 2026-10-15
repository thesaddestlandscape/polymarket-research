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
import gzip
import random
import sys
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


def grupos():
    r = pd.read_csv(OUT / "baratas_wallets.csv", index_col=0)
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
            pass

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
    if cache.exists():
        return pd.read_csv(cache)
    filas, tok = fills_dia(d, persist)
    if not filas:
        return None
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
    df.to_csv(cache, index=False, compression="gzip")
    return df


def ev(x):
    return float((x.acc * x.gana).sum() / x.usdc.sum() - 1) if len(x) and x.usdc.sum() > 0 else float("nan")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", default=",".join(DIAS))
    a = ap.parse_args()
    persist = grupos()
    partes = []
    for d in a.dias.split(","):
        r = dia(d, persist)
        if r is not None:
            partes.append(r)
            print(f"  {d}: {len(r)} rellenos", flush=True)
    df = pd.concat(partes, ignore_index=True)
    lines = ["FASE 2 (lo invisible) — rellenos MAKER de compra a <= 0,20 en BTC 5m; contexto a hora de bloque − 2 s",
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
    (OUT / "invisible_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
