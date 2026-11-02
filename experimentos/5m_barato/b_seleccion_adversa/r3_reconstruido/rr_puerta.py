#!/usr/bin/env python3
"""rr_puerta.py -- PUERTA de validacion de la reconstruccion contra el brazo VIVO en el solape 26-Oct 00:00..21:18Z.
CRITERIOS FIJADOS ANTES DE EJECUTAR LA REPLICA (ver PUERTA_CRITERIOS.txt):
  Universo U: mercados con ini del 26-Oct, mkt_fin del vivo con completo=true, cobertura reconstruida 'ok', cierre <= ultimo mkt_fin del vivo.
  Emparejado de fills: misma (slug, pol, esc) y mismo lado y |precio_vivo - precio_rec| <= 0,01.
  C1  para esc en {cons_x, cons_r} (agrupando BASE+R2+R3): recall = emparejados/fills_vivo >= 0,90  Y  precision = emparejados/fills_rec >= 0,90.
  C2  para esc en {cons_x, cons_r} (agrupando las 3 politicas, EV = sum pnl / sum coste con el desenlace oficial): mismo signo del EV agregado vivo vs rec.
  PASA = C1 y C2 en ambos escenarios. Informativos (no deciden): opt_x, por politica, razon fills_rec/fills_vivo, motivos de divergencia.
Uso: .venv/bin/python -I rr_puerta.py"""
import gzip
import json
import sys
from collections import defaultdict
from pathlib import Path

VIVO = Path("/root/polymarket-research-datalogs/r3_shadow")
REC = Path("/root/polymarket-research-datalogs/r3_reconstruido/puerta")
D = "2026-10-26"


def leer(p, tipos):
    out = []
    for ln in gzip.open(p, "rt"):
        if not any(f'"tipo":"{t}"' in ln for t in tipos):
            continue
        try:
            r = json.loads(ln)
        except ValueError:
            continue
        if r.get("tipo") in tipos:
            out.append(r)
    return out


def main():
    cob = json.loads((REC / f"cobertura_{D}.json").read_text())
    vf = leer(VIVO / f"r3_shadow_{D}.jsonl.gz", ("fill", "mkt_fin"))
    rf = leer(REC / f"r3_reconstruido_{D}.jsonl.gz", ("fill", "mkt_fin"))
    des = {r["slug"]: r["ganador"] for r in leer(VIVO / f"r3_desenlaces_{D}.jsonl.gz", ("des",))}
    mf_v = {r["slug"]: r for r in vf if r["tipo"] == "mkt_fin"}
    mf_r = {r["slug"]: r for r in rf if r["tipo"] == "mkt_fin"}
    ult = max(r["cierre"] for r in mf_v.values())
    U = {s for s, r in mf_v.items() if r.get("completo") and cob.get(s) == "ok" and r["cierre"] <= ult and s in mf_r and mf_r[s].get("completo")}
    print(f"universo: vivo mkt_fin={len(mf_v)} completo={sum(1 for r in mf_v.values() if r.get('completo'))} cob_ok={sum(1 for s in mf_v if cob.get(s)=='ok')} rec={len(mf_r)} U={len(U)}")
    FV = {(r["slug"], r["pol"], r["esc"]): r for r in vf if r["tipo"] == "fill" and r["slug"] in U}
    FR = {(r["slug"], r["pol"], r["esc"]): r for r in rf if r["tipo"] == "fill" and r["slug"] in U}
    print(f"fills vivo={len(FV)} rec={len(FR)}  (claves unicas por slug,pol,esc: un relleno cierra la puja)")
    res = {}
    for esc in ("cons_x", "cons_r", "opt_x"):
        for pols in (("BASE", "R2", "R3"), ("BASE",), ("R2",), ("R3",)):
            kv = {k: v for k, v in FV.items() if k[2] == esc and k[1] in pols}
            kr = {k: v for k, v in FR.items() if k[2] == esc and k[1] in pols}
            m = [k for k in kv if k in kr and kv[k]["lado"] == kr[k]["lado"] and abs(kv[k]["precio"] - kr[k]["precio"]) <= 0.01]

            def ev(F):
                p = c = 0.0
                n = 0
                for (s, pol, e), r in F.items():
                    if e != esc or pol not in pols or des.get(s) is None:
                        continue
                    cs = r["acc"] * r["precio"]
                    p += r["acc"] * (1.0 if r["lado"] == des[s] else 0.0) - cs
                    c += cs
                    n += 1
                return (p / c if c > 0 else None), n, p, c
            evv, evr = ev(FV), ev(FR)
            rec = len(m) / len(kv) if kv else None
            pre = len(m) / len(kr) if kr else None
            res[(esc, "+".join(pols))] = (len(kv), len(kr), len(m), rec, pre, evv, evr)
            f = lambda x: "NA" if x is None else f"{x:.3f}"
            print(f"{esc:7s} {'+'.join(pols):12s} vivo={len(kv):4d} rec={len(kr):4d} emp={len(m):4d} recall={f(rec)} prec={f(pre)}  EV_vivo={f(evv[0])}(n={evv[1]}) EV_rec={f(evr[0])}(n={evr[1]})")
    ok = True
    for esc in ("cons_x", "cons_r"):
        nv, nr, nm, rec, pre, evv, evr = res[(esc, "BASE+R2+R3")]
        c1 = rec is not None and pre is not None and rec >= 0.90 and pre >= 0.90
        c2 = evv[0] is not None and evr[0] is not None and (evv[0] > 0) == (evr[0] > 0)
        print(f"PUERTA {esc}: C1(recall>=0,90 y prec>=0,90)={'OK' if c1 else 'FALLA'}  C2(signo EV)={'OK' if c2 else 'FALLA'}")
        ok = ok and c1 and c2
    print("PUERTA:", "PASA" if ok else "NO PASA")
    return 0 if ok else 3


if __name__ == "__main__":
    sys.exit(main())
