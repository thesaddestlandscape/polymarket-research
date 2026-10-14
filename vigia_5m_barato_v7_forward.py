"""vigia_5m_barato_v7_forward.py -- HIPÓTESIS 5M_CHEAP_V7_DISPARO15M_BTC, CONGELADA el 2026-10-14 (vía 3, OK Javi: congelar y
forward como V5/V6). SOLO OBSERVACIÓN / DRY-RUN: nunca firma ni envía nada.

REGLA (= analisis_5m_barato_disparo15m.py, cuyo contenido queda HASHEADO aquí; si cambia, este vigía no corre):
  pares 5m/15m que cierran a la vez, lado s por referencias TWAP60 oficiales (|gap| >= 1 bp); DISPARO en cada operación del
  15m (token s o contrario) recibida en t (como mucho 1 cada 100 ms por par), ventana (C-300)s+1,5s..C-10s; FOK de compra
  del 5m lado s con límite p* = p_limite(bid15_s(t) + DELTA); casa a t+L si ask5_s(t+L) <= p* (nivel 1, como mucho su
  tamaño, objetivo max(5, 2 €/ask)); una ejecución por mercado. PRINCIPAL: BTC, DELTA 0, L355. Diagnóstico: DELTA 0,02/0,04,
  L223, otras monedas.
MECANISMO: la subida del bid15 que crea la señal va precedida de operaciones en el 15m (81 % en 300 ms vs 9,7 % placebo, 9
  días); disparar en ellas adelanta a quien reacciona al cambio del bid15.
ORIGEN (DESCUBRIMIENTO 05-13 Oct, no cuenta): BTC DELTA 0 L355 n=18, 8 días (8/8 positivos), EV +1,99/€ IC90 días
  (0,86, 4,05), sin top3 +23,7 €, sin 05-Oct +1,12 (n=17). 12 celdas (3 DELTA x 2 L x 2 universos) todas positivas.
GATES (forward, días >= FORWARD_DESDE): G1 ejecutables >= 40, G2 >= 10 días, G3 EV/€ >= 0,10, G4 IC90 por días > 0,
  G5 EV sin mejor día > 0, G6 PnL sin top3 > 0, G7 L223 (referencia) EV > 0. REFUTACIÓN: con >= 40 ejecutables, EV <= 0 o
  IC90 por días < 0. ABANDONO: < 15 ejecutables a los 30 días forward.
Uso: python3 vigia_5m_barato_v7_forward.py [--telegram] [--descubrimiento]
"""
import argparse
import csv
import gzip
import hashlib
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
D = Path("/root/polymarket-research-datalogs/m5barato_mision")
REGLA = REPO / "analisis_5m_barato_disparo15m.py"
SHA_REGLA = "c42f2c1f14ea72e4202389b9790e14b6477a418ee21a00959df4b8e937d2f1cd"   # sha256 de analisis_5m_barato_disparo15m.py congelado 14-Oct
CONFIG_V6 = {"nombre": "5M_CHEAP_V7_DISPARO15M_BTC", "congelado_utc": "2026-10-14T12:55:00+00:00",
             "forward_desde": "2026-10-14", "universo": "BTC", "delta": 0.0, "lat_principal": 355,
             "lat_estres": 223, "lat_ref": 223, "gates": "G1-G7 docstring"}
OUT = D / "v7_informe.json"
RNG = random.Random(6)


def hash_v7():
    h = hashlib.sha256(json.dumps(CONFIG_V6, sort_keys=True).encode())
    h.update(Path(__file__).read_bytes())
    return h.hexdigest()[:16]


def cargar(desde, hasta=None):
    filas = []
    for f in sorted(D.glob("disparo15m_2026-*.csv.gz")):
        dia = f.name[11:21]
        if dia < desde or (hasta and dia > hasta):
            continue
        with gzip.open(f, "rt") as fh:
            for r in csv.DictReader(fh):
                if (r["moneda"] != CONFIG_V6["universo"] or r.get("pnl") in (None, "")
                        or abs(float(r["delta"]) - CONFIG_V6["delta"]) > 1e-9):
                    continue
                filas.append({"dia": dia, "L": int(r["L"]), "pnl": float(r["pnl"]), "coste": float(r["coste"]),
                              "gana": r["gana"] == "True"})
    return filas


def met(R):
    if not R:
        return {"n": 0}
    pdd = defaultdict(lambda: [0.0, 0.0])
    for r in R:
        pdd[r["dia"]][0] += r["pnl"]
        pdd[r["dia"]][1] += r["coste"]
    ks = list(pdd)
    ic = None
    if len(ks) >= 3:
        m = sorted(sum(pdd[k][0] for k in s) / sum(pdd[k][1] for k in s) for s in ([RNG.choice(ks) for _ in ks] for _ in range(3000)))
        ic = (round(m[150], 3), round(m[2850], 3))
    md = max(pdd, key=lambda k: pdd[k][0])
    pn = sorted((r["pnl"] for r in R), reverse=True)
    sin_md = [(v[0], v[1]) for k, v in pdd.items() if k != md]
    return {"n": len(R), "dias": len(ks), "pnl": round(sum(pn), 2), "ev": round(sum(pn) / sum(r["coste"] for r in R), 4),
            "acierto": round(sum(r["gana"] for r in R) / len(R), 3), "ic90_dias": ic,
            "ev_sin_mejor_dia": round(sum(x[0] for x in sin_md) / sum(x[1] for x in sin_md), 4) if sin_md and sum(x[1] for x in sin_md) else None,
            "pnl_sin_top3": round(sum(pn[3:]), 2)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--telegram", action="store_true")
    ap.add_argument("--descubrimiento", action="store_true")
    a = ap.parse_args()
    sha = hashlib.sha256(REGLA.read_bytes()).hexdigest()
    if sha != SHA_REGLA:
        msg = f"🚨 V7_DISPARO15M_BTC: la regla (analisis_5m_barato_disparo15m.py) CAMBIÓ (sha {sha[:12]}): no corro"
        print(msg)
        if a.telegram:
            from shadow_digest import enviar_telegram
            enviar_telegram(msg)
        sys.exit(2)
    if a.descubrimiento:
        F, tag = cargar("2026-10-05", "2026-10-13"), "DESCUBRIMIENTO 05-13 Oct (no cuenta)"
    else:
        F, tag = cargar(CONFIG_V6["forward_desde"]), f"FORWARD desde {CONFIG_V6['forward_desde']}"
    res = {"hash": hash_v7(), "sha_regla": sha[:16], "modo": tag}
    lin = [f"🧪 {CONFIG_V6['nombre']} (hash {hash_v7()}, regla {sha[:12]}) — {tag}"]
    for L in dict.fromkeys((CONFIG_V6["lat_principal"], CONFIG_V6["lat_estres"], CONFIG_V6["lat_ref"])):
        r = met([x for x in F if x["L"] == L])
        res[f"L{L}"] = r
        lin.append(f"  L{L}: " + (f"n {r['n']} días {r['dias']} PnL {r['pnl']:+.2f} € EV/€ {r['ev']:+.3f} IC90 días {r['ic90_dias']} "
                                   f"sin mejor día {r['ev_sin_mejor_dia']} sin top3 {r['pnl_sin_top3']:+.2f} acierto {r['acierto']:.0%}"
                                   if r["n"] else "sin ejecuciones todavía"))
    p, e = res[f"L{CONFIG_V6['lat_principal']}"], res[f"L{CONFIG_V6['lat_estres']}"]
    if p.get("n"):
        g = {"G1_n>=40": p["n"] >= 40, "G2_dias>=10": p["dias"] >= 10, "G3_EV>=0,10": p["ev"] >= 0.10,
             "G4_IC90_dias>0": bool(p["ic90_dias"] and p["ic90_dias"][0] > 0), "G5_sin_mejor_dia>0": (p["ev_sin_mejor_dia"] or -9) > 0,
             "G6_sin_top3>0": p["pnl_sin_top3"] > 0, "G7_L223>0": (e.get("ev") or -9) > 0}
        res["gates"] = g
        lin.append("  gates: " + " ".join(f"{k}{'✅' if v else '❌'}" for k, v in g.items()))
    lin.append("Nada pasa a dinero sin gates + /code-review + OK Javi.")
    txt = "\n".join(lin)
    print(txt)
    if not a.descubrimiento:
        OUT.write_text(json.dumps(res, indent=1, default=str))
        if a.telegram:
            from shadow_digest import enviar_telegram
            enviar_telegram(txt)


if __name__ == "__main__":
    main()
