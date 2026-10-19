#!/usr/bin/env python3
"""H43 auditoria (19-Oct). Cifras finales con UNA definicion: K cosechable (50 acc de fills T in (60,270] tras cruzar 5000),
unidades COMPLETAS, dia = dia de CIERRE (fin UTC), EV ponderado por EUR (USDC), IC90 por cierre y por dia, sin 2 mejores dias,
sin top-20. Tambien por dia de FICHERO y posicional, para la tabla de discrepancias. Ligero (bandas).
Uso: python3 -I a7_cierre_final.py OUTJSON"""
import datetime, json, os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1]
sys.argv = [sys.argv[0], "/dev/null", "2026-10-06"]
g = {}
exec(open(os.path.join(HERE, "a4_definicion_k_y_regimen.py")).read().split('res = {"definiciones"')[0], g)
DIAS = ["2026-10-%02d" % i for i in range(5, 19)]
COS, POS = {}, {}
for d in DIAS:
    try:
        rows = g["leer"](d)
    except Exception as e:
        print("sin banda", d, e); continue
    for k, u in g["unid_cosechable"](rows).items(): COS[(d,) + k] = dict(u, fichero=d)
    for k, u in g["unid_posicional"](rows).items(): POS[(d,) + k] = dict(u, fichero=d)
def cierre(u): return datetime.datetime.fromtimestamp(u["fin"], datetime.timezone.utc).strftime("%Y-%m-%d")
def cifras(us, clave_dia):
    us = list(us)
    if not us: return None
    c = sum(u["c"] for u in us); p = sum(u["p"] for u in us)
    dia = defaultdict(lambda: [0.0, 0.0]); cie = defaultdict(lambda: [0.0, 0.0])
    for u in us:
        dia[clave_dia(u)][0] += u["c"]; dia[clave_dia(u)][1] += u["p"]
        cie[u["fin"]][0] += u["c"]; cie[u["fin"]][1] += u["p"]
    def ic(gr, B=4000):
        gg = list(gr.values())
        if len(gg) < 3: return None
        r = random.Random(11); bs = []
        for _ in range(B):
            m = [r.choice(gg) for _ in gg]; cc = sum(x[0] for x in m); bs.append(sum(x[1] for x in m) / cc if cc else 0.0)
        bs.sort(); return [round(bs[int(B * .05)], 3), round(bs[int(B * .95) - 1], 3)]
    mej = sorted(dia, key=lambda d: dia[d][1], reverse=True)[:2]
    rest = [v for d, v in dia.items() if d not in mej]
    top = sorted(us, key=lambda u: u["p"], reverse=True)[20:]
    tc = sum(u["c"] for u in top)
    return {"n": len(us), "dias": len(dia), "cierres": len(cie), "coste_usdc": round(c, 2), "pnl_usdc": round(p, 2),
            "EV_ponderado": round(p / c, 4), "IC90_cierre": ic(cie), "IC90_dias": ic(dia),
            "EV_sin_2_mejores_dias": round(sum(v[1] for v in rest) / sum(v[0] for v in rest), 4) if rest and sum(v[0] for v in rest) else None,
            "EV_sin_top20_unidades": round(sum(u["p"] for u in top) / tc, 4) if tc else None,
            "dias_positivos": sum(1 for v in dia.values() if v[1] > 0),
            "por_dia": {d: round(v[1] / v[0], 3) for d, v in sorted(dia.items())}}
res = {}
for nom, U in (("cosechable_completas", [u for u in COS.values() if u["completa"]]),
               ("cosechable_todas", list(COS.values())),
               ("posicional_todas", list(POS.values()))):
    for lab, clave in (("dia_cierre", cierre), ("dia_fichero", lambda u: u["fichero"])):
        for per, lo, hi in (("in_06_16", "2026-10-06", "2026-10-16"), ("fw_17", "2026-10-17", "2026-10-17")):
            sub = [u for u in U if lo <= clave(u) <= hi]
            res[f"{nom}|{lab}|{per}"] = cifras(sub, clave)
json.dump(res, open(OUT, "w"), indent=1, ensure_ascii=False)
for k, v in res.items():
    if v: print(k, {x: v[x] for x in ("n", "dias", "coste_usdc", "EV_ponderado", "IC90_cierre", "IC90_dias", "EV_sin_2_mejores_dias", "EV_sin_top20_unidades", "dias_positivos")})
    else: print(k, None)
