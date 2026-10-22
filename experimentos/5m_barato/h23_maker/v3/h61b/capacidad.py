#!/usr/bin/env python3
"""capacidad.py -- HITO 3: capacidad y hueco hasta 200 k. Solo lectura de DL/h61b/rows_*_D.csv.gz (salida de h61b_sim). Por moneda x variante (v3 / C_reg / C_live) x brazo:
rellenos/dia, coste medio por relleno, EV ponderado por EUR (celda central cola base 79/60), PnL/dia y PnL anualizado (x365, sin IC propio: el IC viene del bootstrap por DIAS de EV x coste/dia),
rango opt..cons de cola y 79/60 vs 254/150, y por TAMANO (mult 1,2,5,10,20 x real) en modo 'primer' (un relleno cierra) y 'acum' (puede acumular): complecion = sum lleno / sum need en los cierres con relleno.
Comparacion siempre EMPAREJADA: solo dias en que la variante C tiene datos (el aggTrade 'live' solo existe desde 17-Oct). Unidades: pUSD tal como salen (no convertido a EUR).
Hueco: 200.000 - suma por moneda del mejor brazo (A o B, NO ambos: pujan en los mismos mercados) de la mejor variante medida; es una COTA SUPERIOR descriptiva sobre dias ya vistos (in-sample), no una prevision.
Uso: python3 -I capacidad.py [--desde D] [--hasta D] [--coins BTC,ETH,...]"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import h61b_stats as S

COINS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")


def cargar_coin(coin, desde, hasta, prefijo="rows"):
    rows, dias = [], []
    for d, f in S.dias_con_datos(coin, desde, hasta, prefijo=prefijo):
        try:
            rows += S.leer_dia(f); dias.append(d)
        except (OSError, EOFError):
            print("ilegible", f, file=sys.stderr)
    return rows, dias


def celda(rows, var, brazo, cola="base", lp=79, lc=60, mult=1, modo="primer", dias=None):
    sel = [r for r in rows if r["var"] == var and r["brazo"] == brazo and r["cola"] == cola and int(r["lp"]) == lp and int(r["lc"]) == lc and int(r["mult"]) == mult and r["modo"] == modo
           and (dias is None or r["dia"] in dias)]
    cot = {r["cierre"] for r in sel if int(r["n_seg"]) > 0}
    fills = [r for r in sel if float(r["lleno"]) > 0]
    con = [r for r in fills if r["gana"] != ""]
    pnl = sum(float(r["lleno"]) * int(r["gana"]) - float(r["coste"]) + float(r["rebate"]) for r in con)
    coste = sum(float(r["coste"]) for r in con)
    need = sum(float(r["need"]) for r in fills)
    lleno = sum(float(r["lleno"]) for r in fills)
    pos = [(r["dia"], float(r["lleno"]) * int(r["gana"]) - float(r["coste"]) + float(r["rebate"]), float(r["coste"])) for r in con]
    e = S.ev_dias(pos)
    return dict(n_cot=len(cot), n_fill=len(fills), n_missing=len(fills) - len(con), pnl=pnl, coste=coste, ev=(pnl / coste if coste > 0 else float("nan")), compl=(lleno / need if need > 0 else float("nan")),
                ic_lo=e.get("ic90_lo", float("nan")), ic_hi=e.get("ic90_hi", float("nan")), sin2=e.get("sin2", float("nan")), prof_med=(float(np.median([float(r["prof_join"]) for r in fills])) if fills else float("nan")),
                precio_med=(float(np.mean([float(r["precio"]) for r in fills])) if fills else float("nan")))


def tabla(coin, desde, hasta, prefijo="rows", brazos=("A", "B")):
    rows, dias = cargar_coin(coin, desde, hasta, prefijo)
    if not rows: return None
    dias_c = {v: sorted({r["dia"] for r in rows if r["var"] == v}) for v in ("v3", "C_reg", "C_live")}
    out = dict(coin=coin, dias_v3=dias_c["v3"], arms={})
    for var in ("C_reg", "C_live"):
        if not dias_c[var]: continue
        dd = set(dias_c[var]); nd = len(dd)
        for brazo in brazos:
            base = celda(rows, "v3", brazo, dias=dd); c = celda(rows, var, brazo, dias=dd)
            rango = {}
            for nom, v in (("v3", "v3"), (var, var)):
                vals = [celda(rows, v, brazo, cola=co, lp=lp, lc=lc, dias=dd) for co in ("opt", "base", "cons") for lp, lc in ((79, 60), (254, 150))]
                rango[nom] = [x["pnl"] / nd * 365 for x in vals]
            tam = {}
            for modo in ("primer", "acum"):
                for m in S.__dict__.get("MULTS", (1, 2, 5, 10, 20)):
                    x = celda(rows, var, brazo, mult=m, modo=modo, dias=dd); tam[f"{modo}x{m}"] = dict(n_fill=x["n_fill"], pnl_dia=x["pnl"] / nd, ev=x["ev"], compl=x["compl"], coste_dia=x["coste"] / nd)
            out["arms"][f"{brazo}/{var}"] = dict(dias=nd, v3=base, C=c, pnl_anual_v3=base["pnl"] / nd * 365, pnl_anual_C=c["pnl"] / nd * 365, rango_anual_cola_lat=rango, por_tamano=tam,
                                                  rellenos_dia_v3=base["n_fill"] / nd, rellenos_dia_C=c["n_fill"] / nd, coste_relleno_C=(c["coste"] / c["n_fill"] if c["n_fill"] else float("nan")))
    return out


def main():
    a = sys.argv[1:]
    desde = a[a.index("--desde") + 1] if "--desde" in a else "2026-10-06"
    hasta = a[a.index("--hasta") + 1] if "--hasta" in a else None
    coins = a[a.index("--coins") + 1].split(",") if "--coins" in a else COINS
    res = {}; f = lambda x: "n/e" if x != x else f"{x:+.2f}"
    best = {}
    for c in coins:
        t = tabla(c, desde, hasta, "rows_ext", ("U00", "U01", "U10")) if "--ext" in a else tabla(c, desde, hasta)
        if not t: print(c, "SIN DATOS"); continue
        res[c] = t
        print(f"== {c}: dias v3 {len(t['dias_v3'])} ({t['dias_v3'][0]}..{t['dias_v3'][-1]})")
        for k, v in t["arms"].items():
            C, V = v["C"], v["v3"]
            print(f" {k:10s} dias={v['dias']:2d} cotiz={C['n_cot']:3d} | v3: rell={V['n_fill']:2d} ({v['rellenos_dia_v3']:.2f}/d) EV={f(V['ev'])} PnL={V['pnl']:+.2f} anual={v['pnl_anual_v3']:+.0f} "
                  f"| C: rell={C['n_fill']:2d} ({v['rellenos_dia_C']:.2f}/d) miss={C['n_missing']} EV={f(C['ev'])} IC90d=({f(C['ic_lo'])},{f(C['ic_hi'])}) sin2={f(C['sin2'])} PnL={C['pnl']:+.2f} anual={v['pnl_anual_C']:+.0f} "
                  f"coste/rell={v['coste_relleno_C']:.2f} prof_join_med={C['prof_med']:.1f}")
            print("     rango anual C (opt/base/cons x 79-60/254-150):", [round(x) for x in v["rango_anual_cola_lat"][k.split('/')[1]]])
            print("     tamano:", {kk: (round(vv['pnl_dia'], 3), round(vv['ev'], 2) if vv['ev'] == vv['ev'] else None, round(vv['compl'], 2) if vv['compl'] == vv['compl'] else None) for kk, vv in v["por_tamano"].items()})
            if v["pnl_anual_C"] > best.get((c, "C"), (-1e18,))[0]: best[(c, "C")] = (v["pnl_anual_C"], k)
            if v["pnl_anual_v3"] > best.get((c, "v3"), (-1e18,))[0]: best[(c, "v3")] = (v["pnl_anual_v3"], k)
    for var in ("v3", "C"):
        tot = sum(max(0, b[0]) for (c, v), b in best.items() if v == var)
        print(f"SUMA mejor brazo por moneda ({var}): {tot:+.0f} pUSD/año ({tot / 200000 * 100:.2f} % de 200.000); hueco {200000 - tot:+.0f}  detalle {[(c, round(b[0]), b[1]) for (c, v), b in best.items() if v == var]}")
    out = os.environ.get("H61B_OUT", S.DL)
    json.dump(res, open(os.path.join(out, "capacidad_ext.json" if "--ext" in a else "capacidad.json"), "w"), indent=1, default=float)


if __name__ == "__main__":
    main()
