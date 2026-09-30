#!/usr/bin/env python3
"""analisis_tomadores_persistencia_30sep.py -- ¿los TOMADORES agresivos que ganan son persistentes?

Javi 30-Sep: "tiene que haber takers sacando pasta". Medido 27-29 Sep: de 898 wallets sistemáticas
en up/down 5/15 min, las 243 agresivas (>=70 % del volumen por encima del mid) suman neto +0,14 %
del volumen; las pasivas -2,28 %. 39 agresivas ganan los 3 días netas de fee. Pero elegir por PnL
y medir en los mismos días es circular. Aquí: SELECCIÓN en días A (primeros) y MEDICIÓN en días B
(posteriores), sin solape:
  1. rendimiento propio de las seleccionadas en B (PnL bruto, fee estimado, neto, % que repite);
  2. EV de COPIARLAS nosotros en B al ask REAL en el instante de decisión (bot_wallets_gate_bucket_
     fase0.csv: primera detección por wallet x mercado, con latencia real y fee 7 %).
Solo lectura.
"""
import bisect, csv, json, random, sys
from collections import defaultdict
from pathlib import Path
import analisis_ganadores_alpha_vs_ejecucion_30sep as G

REPO = Path(__file__).resolve().parent

def perfilar(dias):
    out = G.cargar_desenlaces(dias); mids = G.cargar_mids(dias)
    W = defaultdict(lambda: dict(n=0, vol=0.0, agr=0.0, cl=0.0, pnl=defaultdict(float), fee=0.0, volm=0.0, merc=set(), pv=0.0))
    for d in dias:
        f = G._abrir(G.DATALOGS / f"polymarket_activity_{d}.csv")
        if f is None: continue
        with f:
            for r in csv.DictReader(f):
                if r.get("categoria_updown_tracked") != "1" or r.get("marco") not in G.MARCOS: continue
                g = out.get(r["market_slug"])
                if g is None or r["outcome"] not in ("Up", "Down"): continue
                try: s, p, t = float(r["size"]), float(r["price"]), G._ts(r["timestamp_utc"])
                except (ValueError, TypeError): continue
                if s <= 0 or not 0 < p < 1: continue
                a = W[r["wallet"].lower()]; sg = 1 if r["side"] == "BUY" else -1
                a["n"] += 1; v = s * p; a["vol"] += v; a["pv"] += p * v
                a["pnl"][d] += sg * s * ((1.0 if r["outcome"] == g else 0.0) - p); a["merc"].add(r["market_slug"])
                m = mids.get(r["condition_id"])
                if m:
                    i = bisect.bisect_right(m[0], t) - 1
                    if i >= 0 and t - m[0][i] <= 20:
                        mid = m[1][i] if r["outcome"] == "Up" else 1 - m[1][i]
                        a["volm"] += v; a["cl"] += v
                        if sg * (p - mid) > 0.004:
                            a["agr"] += v; a["fee"] += 0.07 * p * (1 - p) * s
        print("perfilado", d, flush=True)
    R = {}
    for w, a in W.items():
        if a["volm"] <= 0: continue
        pnl = sum(a["pnl"].values()); fee = a["fee"] / a["volm"] * a["vol"]
        R[w] = dict(n=a["n"], vol=a["vol"], pnl=pnl, fee=fee, neto=pnl - fee, agr=a["agr"] / a["cl"] * 100 if a["cl"] else 0,
                    merc=len(a["merc"]), precio=a["pv"] / a["vol"], dpos=sum(1 for v in a["pnl"].values() if v > 0), nd=len(a["pnl"]),
                    cob=a["volm"] / a["vol"])
    return R

def main():
    A = [f"2026-09-{d:02d}" for d in range(21, 27)]; B = ["2026-09-27", "2026-09-28", "2026-09-29"]
    RA = perfilar(A); RB = perfilar(B)
    base = {w: r for w, r in RA.items() if r["n"] >= 500 and r["merc"] >= 200 and r["cob"] >= 0.15}
    grupos = {
        "agresivas, neto>0 en A y >=5/6 días +": [w for w, r in base.items() if r["agr"] >= 70 and r["neto"] > 0 and r["dpos"] >= 5],
        "agresivas, neto>0 en A": [w for w, r in base.items() if r["agr"] >= 70 and r["neto"] > 0],
        "agresivas, todas": [w for w, r in base.items() if r["agr"] >= 70],
        "no agresivas, neto>0 en A": [w for w, r in base.items() if r["agr"] < 70 and r["neto"] > 0],
        "todas las sistemáticas": list(base),
    }
    print(f"\nSELECCIÓN en {A[0]}..{A[-1]} | MEDICIÓN en {B[0]}..{B[-1]} (sin solape)")
    for nombre, ws in grupos.items():
        a_vol = sum(RA[w]["vol"] for w in ws); a_neto = sum(RA[w]["neto"] for w in ws)
        enB = [w for w in ws if w in RB and RB[w]["n"] >= 100]
        if not enB: print(nombre, "sin datos en B"); continue
        v = sum(RB[w]["vol"] for w in enB); bruto = sum(RB[w]["pnl"] for w in enB); fee = sum(RB[w]["fee"] for w in enB)
        rep = sum(1 for w in enB if RB[w]["neto"] > 0)
        print(f"{nombre:40s} n={len(ws):4d} | en A neto {a_neto / a_vol * 100:+.2f}% | siguen activas en B {len(enB):4d} | en B: bruto {bruto / v * 100:+.2f}% fee {fee / v * 100:.2f}% "
              f"NETO {(bruto - fee) / v * 100:+.2f}% ({bruto - fee:+.0f} $) | repiten neto>0: {rep / len(enB):.0%}")
    # copiar en B a las seleccionadas en A, al ask real de decisión
    sel = set(grupos["agresivas, neto>0 en A y >=5/6 días +"]); sel2 = set(grupos["agresivas, neto>0 en A"])
    filas = defaultdict(list)
    with open(REPO / "data/shadow/bot_wallets_gate_bucket_fase0.csv") as f:
        for r in csv.DictReader(f):
            if r["timestamp_utc"][:10] not in B or r["acierto"] not in ("0", "1") or r["marco"] not in G.MARCOS: continue
            w = r["wallet"].lower()
            g = "A) agresivas neto>0 y >=5/6 días" if w in sel else "B) agresivas neto>0 (resto)" if w in sel2 else "C) resto de wallets rastreadas"
            try: a = float(r["mejor_ask_decision"])
            except (ValueError, TypeError): continue
            if not 0.05 <= a < 0.95 or r["sigue_fillable_decision"] not in ("1", "1.0"): continue
            ac = int(r["acierto"]); filas[g].append((r["timestamp_utc"][:10], ac / a - 1 - 0.07 * (1 - a), ac, a, w, r["marco"]))
    print("\nCOPIARLAS en B (primera detección por wallet x mercado, ask REAL en decisión, fillable, fee 7 %): EV por € apostado")
    for g, v in sorted(filas.items()):
        for marco in ("5min", "15min", None):
            x = [t for t in v if marco is None or t[5] == marco]
            if len(x) < 40: continue
            for lo, hi in ((0.05, 0.95), (0.60, 0.95), (0.70, 0.85)):
                y = [t for t in x if lo <= t[3] < hi]
                if len(y) < 40: continue
                print(f"  {g:36s} {marco or 'ambos':5s} ask[{lo:.2f},{hi:.2f}) n={len(y):5d} wallets={len(set(t[4] for t in y)):3d} hit {sum(t[2] for t in y) / len(y):.1%} "
                      f"ask medio {sum(t[3] for t in y) / len(y):.3f} EV {sum(t[1] for t in y) / len(y):+.4f}")
    json.dump({"seleccion_A": sorted(sel), "seleccion_A_laxa": sorted(sel2)}, open(REPO / "data/shadow/tomadores_seleccion_21_26sep.json", "w"), indent=1)
    return 0

if __name__ == "__main__": sys.exit(main())
