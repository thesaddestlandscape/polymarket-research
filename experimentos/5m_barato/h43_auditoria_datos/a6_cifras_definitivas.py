#!/usr/bin/env python3
"""H43 auditoria (19-Oct). CIFRAS con UNA definicion: K cosechable (50 primeras acc de fills T in (60,270] tras cruzar 5000 acc
de banda), unidades COMPLETAS, dia = dia de CIERRE, EV ponderado por EUR, IC90 por cierre (cluster) y por dia, sin 2 mejores dias,
sin top-20 unidades. NOTA 19-Oct: esta version agrupa por DIA DE FICHERO (no de cierre); para dia de cierre ver a7. Ligero (bandas).
Uso: python3 -I a6_cifras_definitivas.py OUTJSON D..."""
import csv, gzip, json, os, random, sys, datetime
from collections import defaultdict
sys.argv_saved = list(sys.argv)
import importlib.util
spec = importlib.util.spec_from_file_location("a4", os.path.join(os.path.dirname(os.path.abspath(__file__)), "a4_definicion_k_y_regimen.py"))
src = open(spec.origin).read().split('res = {"definiciones"')[0]
g = {"__name__": "a4lib"}
sys.argv = [sys.argv_saved[0], "/dev/null"] + sys.argv_saved[2:3]
exec(src, g)
OUT = sys.argv_saved[1]; DIAS = sys.argv_saved[2:]
def cifras(U):
    us = list(U.values())
    if not us: return None
    c = sum(u["c"] for u in us); p = sum(u["p"] for u in us)
    dia = defaultdict(lambda: [0.0, 0.0]); cie = defaultdict(lambda: [0.0, 0.0])
    for k, u in U.items():
        dia[k[0]][0] += u["c"]; dia[k[0]][1] += u["p"]; cie[u["fin"]][0] += u["c"]; cie[u["fin"]][1] += u["p"]
    def ic(gr, B=4000, seed=11):
        gg = list(gr.values())
        if len(gg) < 3: return None
        r = random.Random(seed); bs = []
        for _ in range(B):
            m = [r.choice(gg) for _ in gg]; cc = sum(x[0] for x in m); bs.append(sum(x[1] for x in m) / cc if cc else 0.0)
        bs.sort(); return [round(bs[int(B * .05)], 3), round(bs[int(B * .95) - 1], 3)]
    mej = sorted(dia, key=lambda d: dia[d][1], reverse=True)[:2]
    rest = [v for d, v in dia.items() if d not in mej]
    top = sorted(us, key=lambda u: u["p"], reverse=True)[20:]
    return {"n": len(us), "dias": len(dia), "cierres": len(cie), "coste_eur": round(c, 2), "pnl_eur": round(p, 2),
            "EV_ponderado": round(p / c, 4), "EV_media_unidad": round(sum(u["p"] / u["c"] for u in us if u["c"]) / len(us), 4),
            "IC90_cierre": ic(cie), "IC90_dias": ic(dia),
            "EV_sin_2_mejores_dias": round(sum(v[1] for v in rest) / sum(v[0] for v in rest), 4) if rest else None,
            "EV_sin_top20_unidades": round(sum(u["p"] for u in top) / sum(u["c"] for u in top), 4) if top else None,
            "dias_positivos": sum(1 for v in dia.values() if v[1] > 0), "por_dia_EV": {d: round(v[1] / v[0], 3) for d, v in sorted(dia.items())}}
COS, POS = {}, {}
for d in DIAS:
    rows = g["leer"](d)
    for k, u in g["unid_cosechable"](rows).items(): COS[(d,) + k] = dict(u, dia=d)
    for k, u in g["unid_posicional"](rows).items(): POS[(d,) + k] = dict(u, dia=d)
def f_in(U): return {k: v for k, v in U.items() if "2026-10-06" <= k[0] <= "2026-10-16"}
def f_fw(U): return {k: v for k, v in U.items() if k[0] >= "2026-10-17"}
def f_fw_mismo_cierre(U): return {k: v for k, v in U.items() if k[0] == "2026-10-17"}
res = {}
for nom, U in (("cosechable_completas", {k: v for k, v in COS.items() if v["completa"]}),
               ("cosechable_todas", COS), ("posicional_vigia", POS)):
    res[nom] = {"in_06_16": cifras(f_in(U)), "fw_17": cifras(f_fw_mismo_cierre(U)), "fw_17_mas_18_si_hay": cifras(f_fw(U))}
json.dump(res, open(OUT, "w"), indent=1, ensure_ascii=False)
for nom in res:
    for per in ("in_06_16", "fw_17"):
        r = res[nom][per]
        print(nom, per, {k: r[k] for k in ("n", "dias", "coste_eur", "EV_ponderado", "IC90_cierre", "IC90_dias", "EV_sin_2_mejores_dias", "EV_sin_top20_unidades", "dias_positivos")} if r else None)
