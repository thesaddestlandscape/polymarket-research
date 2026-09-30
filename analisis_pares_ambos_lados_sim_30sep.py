#!/usr/bin/env python3
"""analisis_pares_ambos_lados_sim_30sep.py -- ¿se puede replicar como TOMADOR lo que hacen las
wallets sistemáticas ganadoras (comprar Up y Down del mismo mercado con coste conjunto <1)?

Hallazgo 30-Sep (analisis_ganadores_alpha_vs_ejecucion_30sep.py): las wallets con PnL positivo
3/3 días y >=500 mercados ganan sobre todo comprando AMBOS lados a un coste medio del par de
0,92-0,98 (0x3048: 0,956, 843 mercados, 22,9k$ en 3 días solo de pares).

Simulación honesta con el ASK REAL de libro_ambos_lados (snapshots ~5 s), 1 acción por mercado,
fee tomador 0,07·p·(1-p) por acción, sin mirar al futuro:
  1ª pata : cuando el ask del lado más barato <= X y quedan >= R_MIN s, se compra ese lado.
  2ª pata : si después el ask del otro lado <= C - precio_1ª, se compra (par cerrado, paga 1).
  si no   : la 1ª pata se queda hasta la resolución (riesgo direccional).
Rejilla X x C; se elige en ENTRENAMIENTO (primeros días) y se valida en los días posteriores.
Solo lectura.  Uso: python3 analisis_pares_ambos_lados_sim_30sep.py
"""
import csv, glob, gzip, random, sys
from collections import defaultdict
from pathlib import Path
REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
FEE = 0.07
R_MIN = {"5min": 60, "15min": 120}
XS = (0.30, 0.35, 0.40, 0.45, 0.48)
CS = (0.90, 0.94, 0.97)

def abrir(p):
    return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")

def desenlaces():
    out = {}
    for p in glob.glob(str(REPO / "data/shadow/resolution_sniper_obs_2026-09-*.csv*")):
        with abrir(p) as f:
            for r in csv.DictReader(f):
                if r.get("outcome_real") in ("Up", "Down"):
                    out[r["condition_id"]] = r["outcome_real"]
    return out

def fee(p): return FEE * p * (1 - p)

def simular(snaps, gan, X, C, rmin):
    """snaps: [(restante_s, ask_up, ask_dn)] en orden temporal. -> (pnl, tipo) o None si no entra."""
    lado = p1 = None
    for rest, au, ad in snaps:
        if lado is None:
            if rest < rmin: break
            if min(au, ad) <= X:
                lado, p1 = ("Up", au) if au <= ad else ("Down", ad)
        else:
            otro = ad if lado == "Up" else au
            if otro <= C - p1:
                return 1 - p1 - otro - fee(p1) - fee(otro), "par"
    if lado is None: return None
    return (1.0 if lado == gan else 0.0) - p1 - fee(p1), "suelta"

def main():
    out = desenlaces()
    res = defaultdict(lambda: defaultdict(list))   # (marco,X,C) -> dia -> [(pnl,tipo,activo)]
    ficheros = sorted(glob.glob(str(DATALOGS / "libro_ambos_lados_2026-09-*.csv*")))
    for p in ficheros:
        dia = Path(p).name.split("_")[-1][:10]
        merc = defaultdict(list); meta = {}
        with abrir(p) as f:
            for r in csv.DictReader(f):
                if r["marco"] not in R_MIN or r["condition_id"] not in out: continue
                try: au, ad, rest = float(r["ask_yes"]), float(r["ask_no"]), float(r["restante_s"])
                except (ValueError, TypeError): continue
                if not (0 < au < 1 and 0 < ad < 1): continue
                merc[r["condition_id"]].append((rest, au, ad)); meta[r["condition_id"]] = (r["marco"], r["activo"])
        for cid, s in merc.items():
            s.sort(key=lambda x: -x[0]); marco, activo = meta[cid]
            for X in XS:
                for C in CS:
                    r = simular(s, out[cid], X, C, R_MIN[marco])
                    if r: res[(marco, X, C)][dia].append((r[0], r[1], activo))
        print(dia, len(merc), "mercados", flush=True)
    dias = sorted({d for v in res.values() for d in v}); corte = dias[len(dias) * 6 // 10]
    print(f"\ndías: {dias[0]}..{dias[-1]} ({len(dias)}) | entrenamiento < {corte} <= validación")
    def resumen(v_dias):
        x = [t for d in v_dias.values() for t in d]
        if len(x) < 40: return None
        m = sum(t[0] for t in x) / len(x); par = sum(t[1] == "par" for t in x) / len(x)
        ks = list(v_dias); rng = random.Random(7); bs = []
        for _ in range(1000):
            s = [t[0] for k in (rng.choice(ks) for _ in ks) for t in v_dias[k]]; bs.append(sum(s) / len(s))
        bs.sort()
        su = [t[0] for t in x if t[1] == "suelta"]
        return len(x), m, par, (bs[50], bs[950]), (sum(su) / len(su) if su else 0)
    for marco in R_MIN:
        print(f"\n== {marco}: € por mercado operado (1 acción), fee incluido ==")
        print(f"{'X':>5s} {'C':>5s} | ENTRENAMIENTO n   media   %par  IC90            suelta | VALIDACIÓN n   media   %par  IC90            suelta")
        for X in XS:
            for C in CS:
                v = res[(marco, X, C)]
                a = resumen({d: t for d, t in v.items() if d < corte}); b = resumen({d: t for d, t in v.items() if d >= corte})
                f = lambda r: f"{r[0]:6d} {r[1]:+.4f} {r[2]:5.0%}  ({r[3][0]:+.3f},{r[3][1]:+.3f}) {r[4]:+.3f}" if r else "   (n<40)"
                print(f"{X:5.2f} {C:5.2f} | {f(a)} | {f(b)}")
    # desglose por activo de la mejor celda de entrenamiento por marco
    for marco in R_MIN:
        mejores = sorted(((resumen({d: t for d, t in res[(marco, X, C)].items() if d < corte}) or (0, -9))[1], X, C) for X in XS for C in CS)
        _, X, C = mejores[-1]
        print(f"\n{marco}: mejor celda en entrenamiento X={X} C={C} -> en VALIDACIÓN por activo:")
        por = defaultdict(list)
        for d, t in res[(marco, X, C)].items():
            if d >= corte:
                for pnl, tipo, a in t: por[a].append(pnl)
        for a, v in sorted(por.items()): print(f"   {a}: n={len(v)} media {sum(v)/len(v):+.4f}")
    return 0
if __name__ == "__main__": sys.exit(main())
