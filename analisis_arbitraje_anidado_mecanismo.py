#!/usr/bin/env python3
"""analisis_arbitraje_anidado_mecanismo.py -- B1 nueva fase, paso 3 (06-Oct, Javi: "identificar el mecanismo que
destruye la oportunidad"; no inferir identidades sin evidencia).

Para cada episodio del escáner ms (CSV de analisis_arbitraje_anidado_ms_scanner.py) reconstruye, con el registro ms,
qué cierra el arbitraje y cómo, y une las operaciones del libro con los fills ON-CHAIN (maker y tomador explícitos):
  FIN del episodio: qué cambio deja neto < 0,0005 primero: sube el ask de A (15m), sube el de B (5m) o ambos.
  Para la pata que cierra: ¿hubo operaciones a ese precio entre t0 y el cierre? -> CONSUMIDA (con tamaño operado vs
  tamaño del nivel) / RETIRADA SIN OPERACIONES / REPRECIO ESTRUCTURAL (el nivel sigue pero la OTRA pata se movió).
  On-chain (onchain_fills_*.csv.gz, hora de bloque ~1,5 s): fills del token en [t0-3 s, t0+5 s] al precio del episodio
  -> wallets tomadoras y makers; ¿la misma wallet compra A y B en el mismo bloque/tx? (evidencia de arbitrajista).
Uso: --episodios <csv>
"""
import argparse
import bisect
import collections
import csv
import glob
import gzip
from datetime import datetime
from pathlib import Path

DL = "/root/polymarket-research-datalogs"
EXCHANGE = "0xe111180000d2663c0091e4f400237545b87b996b"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--episodios", required=True)
    a = ap.parse_args()
    E = list(csv.DictReader(open(a.episodios, encoding="utf-8")))
    mids = {e["mid_l"] for e in E} | {e["mid_c"] for e in E}
    tok = {}            # (mid, lado) -> token
    q = collections.defaultdict(list)
    t = collections.defaultdict(list)
    vent = [(int(e["t0r"]) - 3000, int(e["t0r"]) + 5000) for e in E]
    lo, hi = min(v[0] for v in vent), max(v[1] for v in vent)
    fich = sorted(glob.glob(f"{DL}/maker_ms_*.csv.gz"), key=lambda f: Path(f).stat().st_mtime)
    toks_set = set()
    for f in fich:
        try:
            for ln in gzip.open(f, "rt"):
                c = ln.rstrip("\n").split(",")
                if c[0] == "k" and c[5] in mids:
                    tok[(c[5], c[7])] = c[2]
                    toks_set.add(c[2])
                elif c[0] == "q" and c[2] in toks_set:
                    tr = int(c[7]) if len(c) > 7 and c[7] else int(c[1])
                    if lo <= tr <= hi:
                        q[c[2]].append((tr, None if c[4] in ("", "None") else float(c[4]),
                                        0.0 if c[6] in ("", "None") else float(c[6])))
                elif c[0] == "t" and c[2] in toks_set:
                    tr = int(c[6]) if len(c) > 6 and c[6] else int(c[1])
                    if lo <= tr <= hi:
                        t[c[2]].append((tr, float(c[3]), c[4], float(c[5])))
        except (EOFError, OSError):
            pass
    for d in (q, t):
        for k in d:
            d[k].sort(key=lambda x: x[0])   # un lado vacío del libro es None: ordenar solo por hora
    # on-chain
    oc = collections.defaultdict(list)
    for f in sorted(glob.glob(f"{DL}/onchain_fills_*.csv.gz")):
        try:
            for r in csv.DictReader(gzip.open(f, "rt")):
                if r["token_id"] in toks_set:
                    ts = float(r["ts_est"]) * 1000
                    if lo - 5000 <= ts <= hi + 5000:
                        oc[r["token_id"]].append(r)
        except (EOFError, OSError):
            pass

    fines = collections.Counter()
    modos = collections.Counter()
    tomadores = collections.Counter()
    makers = collections.Counter()
    ambos_misma = 0
    n_con_oc = 0
    filas = []
    for e in E:
        t0 = int(e["t0r"])
        lA = "YES" if e["pata_A"].startswith("Up") else "NO"
        lB = "YES" if e["pata_B"].startswith("Up") else "NO"
        A, B = tok.get((e["mid_l"], lA)), tok.get((e["mid_c"], lB))
        if not A or not B:
            fines["sin_token"] += 1
            continue
        pA, pB, sh = float(e["askA"]), float(e["askB"]), float(e["shares"])
        fin = t0 + int(e["vida_recv_ms"])
        # ¿qué pata cambió en el instante de fin?
        def cambio_en(tk, tt):
            for x in q[tk]:
                if abs(x[0] - tt) <= 2:
                    return x
            return None
        ca, cb = cambio_en(A, fin), cambio_en(B, fin)
        quien = "A" if ca and not cb else "B" if cb and not ca else "ambas" if ca and cb else "desconocido"
        fines[quien] += 1
        for pata, tk, precio in (("A", A, pA), ("B", B, pB)):
            if quien not in (pata, "ambas"):
                continue
            ops = [x for x in t[tk] if t0 <= x[0] <= fin + 50 and abs(x[1] - precio) < 1e-9]
            vol = sum(x[3] for x in ops)
            nivel = float(e["szA"] if pata == "A" else e["szB"])
            if ops and vol >= nivel * 0.9:
                modo = "CONSUMIDA_entera"
            elif ops:
                modo = "CONSUMIDA_parcial_y_retirada"
            else:
                modo = "RETIRADA_sin_operaciones"
            modos[(pata, modo)] += 1
        # on-chain: compradores del precio barato en A y B
        comp = {}
        for pata, tk, precio in (("A", A, pA), ("B", B, pB)):
            ws = set()
            for r in oc.get(tk, []):
                ts = float(r["ts_est"]) * 1000
                if not (t0 - 3000 <= ts <= t0 + 5000):
                    continue
                ma, ta = float(r["maker_amt"] or 0), float(r["taker_amt"] or 0)
                if not ma or not ta:
                    continue
                # side del fill de la orden MAKER: 0 = compra (paga USDC=maker_amt, recibe tokens), 1 = venta
                if r["side"] == "1":
                    p = ta / ma     # maker VENDE tokens (maker_amt) por USDC (taker_amt): r["taker"] = quien compró
                    if abs(p - precio) < 0.006 and r["taker"].lower() != EXCHANGE:
                        ws.add(r["taker"].lower())
                        tomadores[r["taker"].lower()] += 1
                        makers[r["maker"].lower()] += 1
            comp[pata] = ws
        if comp.get("A") or comp.get("B"):
            n_con_oc += 1
        if comp.get("A") and comp.get("B") and comp["A"] & comp["B"]:
            ambos_misma += 1
        filas.append(e)
    print(f"episodios {len(E)} | ¿qué pata cierra el arbitraje?: {dict(fines)}")
    print("modo de cierre por pata:")
    for k, v in sorted(modos.items()):
        print(f"   {k}: {v}")
    print(f"on-chain: episodios con compras al precio barato identificadas {n_con_oc}; con la MISMA wallet comprando "
          f"A y B: {ambos_misma}")
    print("  tomadores más frecuentes (compran el nivel barato):", tomadores.most_common(6))
    print("  makers más frecuentes (publicaron el nivel barato):", makers.most_common(6))


if __name__ == "__main__":
    main()
