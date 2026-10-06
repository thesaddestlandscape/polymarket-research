#!/usr/bin/env python3
"""auditoria_15m_datos.py -- MISIÓN DEFINITIVA 15m, punto 10 (06-Oct): ¿son fiables los datos antes de concluir nada?
Referencia = on-chain (fetch_polymarket_fills_onchain.py: OrdersMatched = una fila por ORDEN TOMADORA con su wallet, lado
0=BUY/1=SELL, token e importes; OrderFilled = cada relleno de maker). Solo mercados 15m cripto (mapa token del registro ms,
filas k). Ventana = solape real de las fuentes.
  0a. firehose (polymarket_activity, RTDS) vs on-chain, emparejado por (tx, wallet tomadora): cobertura en ambos sentidos,
      error de precio, de tamaño, de lado y de outcome↔token, y retraso de recepción frente al bloque.
  0b. operaciones del registro ms (filas t de maker_ms) vs on-chain, emparejado por (token, precio, tamaño, ±4 s):
      cobertura y si el campo `side` es el lado del TOMADOR.
  0c. registro ms: huecos (minutos sin ninguna fila q de 15m) y libros cruzados.
Uso: (ulimit -v 3000000; python3 auditoria_15m_datos.py)    Solo lectura.
"""
import bisect
import collections
import csv
import gzip
import subprocess
from datetime import datetime
from pathlib import Path

DL = Path("/root/polymarket-research-datalogs")
DIAS = ("2026-10-05", "2026-10-06")
csv.field_size_limit(10 ** 7)


def zlines(f, patron):
    p = subprocess.Popen(f"zcat {f} 2>/dev/null | grep -a -E '{patron}'", shell=True, stdout=subprocess.PIPE, text=True)
    for ln in p.stdout:
        yield ln.rstrip("\n")


def mapa_tokens():
    tok = {}
    for f in sorted(DL.glob("maker_ms_2026-10-0[56]_*.csv.gz")):
        for ln in zlines(f, "^k,"):
            r = ln.split(",")
            if len(r) >= 8 and r[4] == "15min":
                tok[r[2]] = (r[3], r[5], r[6], r[7])        # activo, market_id, fin_iso, lado
    return tok


def leer_onchain(tok):
    M, F = [], []
    for d in DIAS:
        f = DL / f"onchain_fills_{d}.csv.gz"
        with gzip.open(f, "rt") as fh:
            for r in csv.DictReader(fh):
                if r["token_id"] not in tok:
                    continue
                ma, ta = float(r["maker_amt"]), float(r["taker_amt"])
                side = int(r["side"])
                # orden con side BUY: entrega USDC (maker_amt) y recibe acciones (taker_amt); SELL al revés
                px, sz = (ma / ta, ta) if side == 0 else (ta / ma, ma)
                rec = (float(r["ts_est"]), r["tx"].lower(), r["maker"].lower(), side, r["token_id"], px, sz)
                (M if r["tipo"] == "M" else F).append(rec)
    return M, F


def leer_firehose(t0, t1, mercados_slug):
    out = []
    for d in DIAS:
        f = DL / f"polymarket_activity_{d}.csv"
        with open(f, encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                if r["marco"] != "15min":
                    continue
                try:
                    ts = datetime.fromisoformat(r["timestamp_utc"]).timestamp()
                except ValueError:
                    continue
                if not (t0 <= ts <= t1):
                    continue
                out.append((ts, r["transaction_hash"].lower(), r["wallet"].lower(), r["side"], r["outcome"],
                            float(r["price"]), float(r["size"] or 0), r["activo"], r["market_slug"]))
    return out


def pct(x, q):
    x = sorted(x)
    return x[min(len(x) - 1, int(q * len(x)))] if x else float("nan")


def main():
    tok = mapa_tokens()
    print(f"tokens 15m en el registro ms: {len(tok)}")
    M, F = leer_onchain(tok)
    t0, t1 = min(x[0] for x in M), max(x[0] for x in M)
    print(f"on-chain 15m: {len(M)} órdenes tomadoras (M), {len(F)} rellenos de maker (F), "
          f"{datetime.utcfromtimestamp(t0)} → {datetime.utcfromtimestamp(t1)} UTC")
    # slug -> (activo, fin) para validar outcome <-> token
    lado_tok = {k: v[3] for k, v in tok.items()}
    fin_tok = {k: (v[0], v[2]) for k, v in tok.items()}
    FH = leer_firehose(t0 + 60, t1 - 60, None)
    print(f"firehose 15m en la ventana: {len(FH)} filas")
    # ---- 0a
    Mi = collections.defaultdict(list)
    for x in M:
        if t0 + 60 <= x[0] <= t1 - 60:
            Mi[(x[1], x[2])].append(x)
    nM = sum(len(v) for v in Mi.values())
    usados, dpx, dsz, dts, lado_ok, out_ok, n_emp = set(), [], [], [], 0, 0, 0
    for r in FH:
        c = Mi.get((r[1], r[2]))
        if not c:
            continue
        # misma tx y wallet: el que más se parezca en precio
        o = min(c, key=lambda m: abs(m[5] - r[5]) + abs(m[6] - r[6]) / max(1, r[6]))
        n_emp += 1
        usados.add(id(o))
        dpx.append(r[5] - o[5])
        dsz.append((r[6] - o[6]) / o[6] if o[6] else 0)
        dts.append(r[0] - o[0])
        lado_ok += (r[3] == "BUY") == (o[3] == 0)
        lt = lado_tok[o[4]]
        out_ok += (r[4] in ("Up", "Yes")) == (lt in ("YES", "Up", "Yes"))
    print("\n0a FIREHOSE vs ON-CHAIN (15m, emparejado por tx + wallet tomadora)")
    print(f"  on-chain M en ventana {nM} | con fila de firehose {len(usados)} ({len(usados) / nM:.1%})")
    print(f"  firehose filas {len(FH)} | con orden on-chain {n_emp} ({n_emp / max(1, len(FH)):.1%})")
    if n_emp:
        print(f"  precio firehose − on-chain: p50 {pct(dpx, .5):+.4f} p05 {pct(dpx, .05):+.4f} p95 {pct(dpx, .95):+.4f} "
              f"| |Δ|>0,005 en {sum(abs(x) > 0.005 for x in dpx) / n_emp:.2%}")
        print(f"  tamaño relativo: p50 {pct(dsz, .5):+.3f} p05 {pct(dsz, .05):+.3f} p95 {pct(dsz, .95):+.3f} "
              f"| |Δ|>5 % en {sum(abs(x) > 0.05 for x in dsz) / n_emp:.2%}")
        print(f"  lado coincide {lado_ok / n_emp:.2%} | outcome↔token coincide {out_ok / n_emp:.2%}")
        print(f"  recepción firehose − bloque (s): p05 {pct(dts, .05):+.2f} p50 {pct(dts, .5):+.2f} p95 {pct(dts, .95):+.2f}"
              f" (bloque ±1,5 s)")
    # cobertura por tamaño y por moneda
    falt = [x for v in Mi.values() for x in v if id(x) not in usados]
    for lo, hi in ((0, 10), (10, 100), (100, 1e12)):
        a = [x for v in Mi.values() for x in v if lo <= x[5] * x[6] < hi]
        b = [x for x in a if id(x) in usados]
        print(f"  cobertura on-chain con nocional [{lo},{hi}) $: {len(b)}/{len(a)} = {len(b) / max(1, len(a)):.1%}")
    porm = collections.Counter(tok[x[4]][0] for v in Mi.values() for x in v)
    porm_ok = collections.Counter(tok[x[4]][0] for v in Mi.values() for x in v if id(x) in usados)
    print("  cobertura por moneda: " + " ".join(f"{m}:{porm_ok[m] / porm[m]:.0%}" for m in sorted(porm)))
    # ---- 0b
    T = collections.defaultdict(list)
    files = sorted(DL.glob("maker_ms_2026-10-0[56]_*.csv.gz"))
    nT = 0
    for f in files:
        for ln in zlines(f, "^t,"):
            r = ln.split(",")
            if len(r) < 6 or r[2] not in tok:
                continue
            try:
                T[r[2]].append((int(r[1]) / 1000, float(r[3]), r[4], float(r[5])))
                nT += 1
            except ValueError:
                continue
    for k in T:
        T[k].sort()
    tr0 = min(v[0][0] for v in T.values())
    tr1 = max(v[-1][0] for v in T.values())
    Mw = [x for x in M if max(t0, tr0) + 60 <= x[0] <= min(t1, tr1) - 60]
    emp, side_ok, dt = 0, 0, []
    for x in Mw:
        L = T.get(x[4], [])
        i = bisect.bisect_left(L, (x[0] - 4,))
        best = None
        while i < len(L) and L[i][0] <= x[0] + 4:
            c = L[i]
            if abs(c[1] - x[5]) < 0.0051 and abs(c[3] - x[6]) <= max(0.02, 0.02 * x[6]):
                if best is None or abs(c[0] - x[0]) < abs(best[0] - x[0]):
                    best = c
            i += 1
        if best:
            emp += 1
            side_ok += (best[2] == "BUY") == (x[3] == 0)
            dt.append(best[0] - x[0])
    print("\n0b REGISTRO ms (filas t) vs ON-CHAIN (15m, token + precio + tamaño ±2 %, ±4 s)")
    print(f"  filas t 15m: {nT} | on-chain M en solape: {len(Mw)} | emparejadas {emp} ({emp / max(1, len(Mw)):.1%})")
    if emp:
        print(f"  `side` del registro = lado del TOMADOR en {side_ok / emp:.2%} | hora exchange − bloque (s): "
              f"p05 {pct(dt, .05):+.2f} p50 {pct(dt, .5):+.2f} p95 {pct(dt, .95):+.2f}")
    # ---- 0c
    print("\n0c REGISTRO ms: huecos y libros cruzados (filas q de tokens 15m)")
    mins, cruz, nq = set(), 0, 0
    for f in files:
        for ln in zlines(f, "^q,"):
            r = ln.split(",")
            if len(r) < 8 or r[2] not in tok:
                continue
            nq += 1
            mins.add(int(r[1]) // 60000)
            try:
                if r[3] not in ("None", "") and r[4] not in ("None", "") and float(r[3]) > float(r[4]):
                    cruz += 1
            except ValueError:
                pass
    m0, m1 = min(mins), max(mins)
    huecos, ini = [], None
    for m in range(m0, m1 + 1):
        if m not in mins and ini is None:
            ini = m
        elif m in mins and ini is not None:
            huecos.append((ini, m - ini))
            ini = None
    print(f"  filas q 15m {nq} | {datetime.utcfromtimestamp(m0 * 60)} → {datetime.utcfromtimestamp(m1 * 60)} | "
          f"minutos sin datos {sum(h[1] for h in huecos)} de {m1 - m0 + 1}")
    for h in huecos:
        if h[1] >= 2:
            print(f"    hueco {datetime.utcfromtimestamp(h[0] * 60)} durante {h[1]} min")
    print(f"  libro cruzado (bid > ask) en {cruz} filas ({cruz / max(1, nq):.3%})")


if __name__ == "__main__":
    main()
