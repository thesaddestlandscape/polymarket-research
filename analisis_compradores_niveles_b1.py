#!/usr/bin/env python3
"""analisis_compradores_niveles_b1.py -- B2 nueva misión (06-Oct, Javi: "¿quién gana de verdad con los niveles baratos
de B1?"). Reglas fijadas ANTES de mirar resultados:
  UNIVERSO: todas las compras (operaciones del WS del CLOB, lado BUY) en los tokens A (15m) y B (5m) de los episodios del
    escáner ms, a precio <= ask barato del episodio en esa pata.
  VENTANA PRINCIPAL: [t0, fin del episodio + 250 ms] por hora de RECEPCIÓN. Robustez: [t0, t0+X] con X en 10..500 ms
    (se reportan todas; ninguna se elige por PnL).
  IDENTIDAD: orden tomadora on-chain (fila M: maker = dueño de la orden tomadora) del mismo token, lado compra, tamaño
    total ±1 %, bloque en [t_exchange - 0,5 s, t_exchange + 4 s]; solo emparejamientos ÚNICOS (cobertura informada).
  PnL: a resolución con desenlace oficial: acciones x (pago - precio) - comisión de tomador 0,07·p·(1-p) por acción.
    Ventas (fuera de B1): acciones x (precio - pago) - comisión si tomadora. PnL B1 separado del resto de la wallet.
Uso: --episodios <csv> [--min-ventanas 2]
"""
import argparse
import collections
import csv
import glob
import gzip
import statistics as st
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

DL = "/root/polymarket-research-datalogs"
EX = "0xe111180000d2663c0091e4f400237545b87b996b"
ROBUSTEZ = [10, 25, 50, 100, 250, 500]
VENTANA_GRANDE = "BTC_1791270000"


def fee(p):
    return 0.07 * p * (1 - p)


def ps(r):
    ma, ta = float(r["maker_amt"] or 0), float(r["taker_amt"] or 0)
    if not ma or not ta:
        return None, None
    return (ma / ta, ta) if r["side"] == "0" else (ta / ma, ma)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodios", required=True)
    a = ap.parse_args()
    E = list(csv.DictReader(open(a.episodios, encoding="utf-8")))
    mids = {e["mid_l"] for e in E} | {e["mid_c"] for e in E}
    t_lo = min(int(e["t0r"]) for e in E) - 5000
    t_hi = max(int(e["t0r"]) + int(e["vida_recv_ms"]) for e in E) + 10_000
    meta, tok = {}, {}
    trades = collections.defaultdict(list)
    for f in sorted(glob.glob(f"{DL}/maker_ms_*.csv.gz"), key=lambda f: Path(f).stat().st_mtime):
        try:
            for ln in gzip.open(f, "rt"):
                c = ln.rstrip("\n").split(",")
                if c[0] == "k":
                    meta[c[2]] = (c[3], c[4], c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
                    if c[5] in mids:
                        tok[(c[5], c[7])] = c[2]
                elif c[0] == "t" and (meta.get(c[2]) or (None,) * 3)[2] in mids:
                    rv = int(c[6]) if len(c) > 6 and c[6] else int(c[1])
                    if t_lo <= rv <= t_hi:
                        trades[c[2]].append((rv, int(c[1]), float(c[3]), c[4], float(c[5])))
        except (EOFError, OSError):
            pass
    # on-chain: órdenes tomadoras (M) en esos tokens + toda la actividad de las wallets que aparezcan
    toks = set(tok.values())
    M = collections.defaultdict(list)
    todas = []
    for f in sorted(glob.glob(f"{DL}/onchain_fills_*.csv.gz")):
        try:
            for r in csv.DictReader(gzip.open(f, "rt")):
                todas.append(r) if r["token_id"] in meta else None
                if r["tipo"] == "M" and r["token_id"] in toks:
                    M[r["token_id"]].append(r)
        except (EOFError, OSError):
            pass
    des = desenlaces({m[2] for m in meta.values()})

    def pago(token):
        m = meta.get(token)
        if not m or m[2] not in des:
            return None
        return 1.0 if des[m[2]] == m[4] else 0.0

    # ---- compras B1
    compras, sin_wallet = [], 0
    for e in E:
        t0, fin = int(e["t0r"]), int(e["t0r"]) + int(e["vida_recv_ms"])
        ventana = f"{e['moneda']}_{e['cierre']}"
        for pata, mid, lado_p, precio in (("A", e["mid_l"], e["pata_A"], float(e["askA"])),
                                          ("B", e["mid_c"], e["pata_B"], float(e["askB"]))):
            tk = tok.get((mid, "YES" if lado_p.startswith("Up") else "NO"))
            if not tk:
                continue
            for rv, te, p, side, sz in trades[tk]:
                if side != "BUY" or p > precio + 1e-9 or not (t0 <= rv <= fin + 500):
                    continue
                cand = [r for r in M[tk] if r["side"] == "0" and te - 500 <= float(r["ts_est"]) * 1000 <= te + 4000
                        and abs(ps(r)[1] - sz) <= max(0.01 * sz, 0.011)]
                w = cand[0]["maker"].lower() if len(cand) == 1 else None
                if w is None:
                    sin_wallet += 1
                pg = pago(tk)
                if pg is None:
                    continue
                compras.append({"wallet": w, "ventana": ventana, "episodio": (ventana, t0), "pata": pata, "precio": p,
                                "shares": sz, "dt_ms": rv - t0, "principal": rv <= fin + 250,
                                "pnl": sz * (pg - p - fee(p)), "riesgo": sz * (p + fee(p)), "neto_ep": float(e["neto0"]),
                                "dia": datetime.fromtimestamp(t0 / 1000, timezone.utc).date().isoformat()})
    P = [c for c in compras if c["principal"]]
    print(f"compras B1 (ventana principal): {len(P)} en {len({c['episodio'] for c in P})} episodios, "
          f"{len({c['ventana'] for c in P})} ventanas | con wallet identificada {sum(c['wallet'] is not None for c in P)} "
          f"({sum(c['wallet'] is not None for c in P) / max(1, len(P)):.0%})")
    tot = sum(c["pnl"] for c in P)
    rk = sum(c["riesgo"] for c in P)
    print(f"  TODAS las compras B1: PnL {tot:+.2f} $ sobre {rk:.0f} $ arriesgados ({tot / rk:+.1%}) | por pata: "
          + " ".join(f"{p_}: {sum(c['pnl'] for c in P if c['pata'] == p_):+.1f} $ (n={sum(c['pata'] == p_ for c in P)})" for p_ in "AB"))
    sin_g = [c for c in P if c["ventana"] != VENTANA_GRANDE]
    print(f"  sin la ventana BTC 07:00: PnL {sum(c['pnl'] for c in sin_g):+.2f} $ sobre {sum(c['riesgo'] for c in sin_g):.0f} $ "
          f"({sum(c['pnl'] for c in sin_g) / max(1, sum(c['riesgo'] for c in sin_g)):+.1%}) | ventanas: "
          + ", ".join(f"{v}: {sum(c['pnl'] for c in P if c['ventana'] == v):+.1f}" for v in sorted({c['ventana'] for c in P})))
    print("  robustez por ventana fija tras t0 (todas las compras, PnL / arriesgado):")
    for X in ROBUSTEZ:
        s = [c for c in compras if 0 <= c["dt_ms"] <= X]
        if s:
            print(f"     +{X:3} ms: n={len(s):4} PnL {sum(c['pnl'] for c in s):+8.2f} $ ({sum(c['pnl'] for c in s) / sum(c['riesgo'] for c in s):+.1%})")
    # ---- precio o selección: por descuento del episodio y por orden de llegada
    print("  por tamaño del arbitraje del episodio (neto/acción del par en t0):")
    for lo, hi in ((0, .01), (.01, .02), (.02, .03), (.03, .05), (.05, .10), (.10, 9)):
        s = [c for c in P if lo <= c["neto_ep"] < hi]
        if s:
            print(f"     [{lo:.2f},{hi:.2f}): n={len(s):4} P(gana)={sum(c['pnl'] > 0 for c in s) / len(s):.0%} "
                  f"PnL {sum(c['pnl'] for c in s):+.2f} $ ({sum(c['pnl'] for c in s) / sum(c['riesgo'] for c in s):+.1%}) "
                  f"ventanas {len({c['ventana'] for c in s})}")
    orden = collections.defaultdict(list)
    for ep in {c["episodio"] for c in P}:
        cs = sorted((c for c in P if c["episodio"] == ep), key=lambda c: c["dt_ms"])
        for i, c in enumerate(cs):
            orden["1º" if i == 0 else "2º-3º" if i < 3 else "4º+"].append(c)
    print("  por orden de llegada en el episodio: " + " | ".join(
        f"{k}: n={len(v)} {sum(c['pnl'] for c in v) / sum(c['riesgo'] for c in v):+.1%}" for k, v in sorted(orden.items())))
    # ---- por wallet
    porw = collections.defaultdict(list)
    for c in P:
        if c["wallet"]:
            porw[c["wallet"]].append(c)
    # actividad fuera de B1 de esas wallets (resolución oficial, compras y ventas)
    ids_b1 = set()
    fuera = collections.defaultdict(lambda: [0.0, 0.0, 0])
    for r in todas:
        w = r["maker"].lower()
        if w not in porw:
            continue
        tomadora = r["tipo"] == "M"
        maker = r["tipo"] == "F" and r["taker"].lower() not in (EX, "")
        if not (tomadora or maker):
            continue
        p, sh = ps(r)
        pg = pago(r["token_id"])
        if p is None or pg is None:
            continue
        f_ = fee(p) * sh if tomadora else 0.0
        v = sh * (pg - p) if r["side"] == "0" else sh * (p - pg)
        fuera[w][0] += v - f_
        fuera[w][1] += sh * p
        fuera[w][2] += 1
    print(f"\n  wallets compradoras identificadas: {len(porw)}; con compras en >=2 ventanas: "
          f"{sum(1 for v in porw.values() if len({c['ventana'] for c in v}) >= 2)}; en >=3: "
          f"{sum(1 for v in porw.values() if len({c['ventana'] for c in v}) >= 3)}")
    filas = []
    for w, cs in porw.items():
        pv = collections.defaultdict(float)
        for c in cs:
            pv[c["ventana"]] += c["pnl"]
        pnl = sum(c["pnl"] for c in cs)
        rk = sum(c["riesgo"] for c in cs)
        mejor = max(pv.values(), key=abs) if pv else 0
        ambas = {(c["episodio"], c["pata"]) for c in cs}
        n_ambas = sum(1 for ep in {c["episodio"] for c in cs} if (ep, "A") in ambas and (ep, "B") in ambas)
        filas.append((w, len(cs), len(pv), pnl, pnl / rk if rk else 0, pnl - mejor,
                      sum(v for k, v in pv.items() if k != VENTANA_GRANDE), n_ambas, fuera[w][0], fuera[w][2],
                      len({c["dia"] for c in cs})))
    filas.sort(key=lambda x: -x[3])
    print("  wallet       compras ventanas  PnL_B1  ROI_B1  sin_mejor_ventana  sin_BTC07  episodios_ambas_patas  PnL_wallet_total(n)  días")
    for x in filas[:12] + [("...",)] + filas[-5:]:
        if x[0] == "...":
            print("  ...")
            continue
        print(f"  {x[0][:10]} {x[1]:7} {x[2]:8} {x[3]:+7.2f} {x[4]:+7.1%} {x[5]:+12.2f} {x[6]:+10.2f} {x[7]:8} "
              f"{x[8]:+12.2f} ({x[9]}) {x[10]}")
    # walk-forward: wallets con PnL_B1 > 0 el día 1 -> su PnL B1 el día 2
    dias = sorted({c["dia"] for c in P})
    if len(dias) >= 2:
        d1, d2 = dias[0], dias[1]
        buenas = {w for w, cs in porw.items() if sum(c["pnl"] for c in cs if c["dia"] == d1) > 0}
        s2 = [c for c in P if c["dia"] == d2 and c["wallet"] in buenas]
        r2 = [c for c in P if c["dia"] == d2 and c["wallet"] not in buenas]
        print(f"\n  WALK-FORWARD: wallets ganadoras en B1 el {d1} ({len(buenas)}) -> el {d2}: n={len(s2)} "
              f"PnL {sum(c['pnl'] for c in s2):+.2f} $ ({sum(c['pnl'] for c in s2) / max(1e-9, sum(c['riesgo'] for c in s2)):+.1%}) "
              f"vs resto n={len(r2)} ({sum(c['pnl'] for c in r2) / max(1e-9, sum(c['riesgo'] for c in r2)):+.1%})")


if __name__ == "__main__":
    main()
