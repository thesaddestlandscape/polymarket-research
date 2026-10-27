#!/usr/bin/env python3
"""Presupuesto de pérdida necesario para llegar a N pujas sin tocar el suelo (misma tanda() que potencia_f5.py)."""
import json, random, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import potencia_f5 as P
rng = random.Random(P.SEED + 1); R = 3000; out = {}
for ev in (-0.06, 0.0):
    for n in (60, 100, 150):
        for pres in (5, 8, 10, 12, 15):
            r = 0; fl = []
            for _ in range(R):
                pnl, f, pu, par = P.tanda(rng, ev, n, 0.57, float(pres)); r += par; fl.append(f)
            fl.sort(); out[f"ev{ev}_N{n}_presup{pres}"] = {"P_suelo": round(r/R, 3), "fills_p10_med_p90": [fl[R//10], fl[R//2], fl[9*R//10]]}
json.dump(out, open(sys.argv[1], "w"), indent=1)
