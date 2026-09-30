#!/usr/bin/env python3
"""analisis_pares_maker_sim_30sep.py -- versión MAKER de "comprar ambos lados" (Javi 30-Sep).

Las wallets sistemáticas ganadoras de up/down 5/15 min compran Up y Down del mismo mercado con
coste conjunto 0,92-0,98 (project_como_ganan_las_wallets_ganadoras_30sep). Como tomador ingenuo
no es replicable (analisis_pares_ambos_lados_sim_30sep.py, negativo en todo). Aquí se simula
con órdenes PASIVAS usando todos los trades reales del firehose (polymarket_activity_*.csv).

Regla de fill CONSERVADORA (sin suponer posición en la cola): una compra pasiva de Up a precio b
se da por ejecutada solo si después se imprime un trade con precio-Up ESTRICTAMENTE menor que b
(precio-Up = price si outcome=Up, 1-price si outcome=Down: en Polymarket comprar Down a q casa
con comprar Up a 1-q). Con prioridad precio-tiempo, un trade por debajo de nuestro bid no puede
ocurrir sin habernos llenado antes. Análogo para Down. Un trade AL precio del bid no cuenta.

Sin mirar al futuro: los bids se fijan con el mid del último snapshot de libro_ambos_lados
(~5 s) y solo se comparan con trades POSTERIORES a ese snapshot. Maker no paga fee (takerOnly).
1 acción por lado y mercado. Variantes:
  estatico  d      : al abrir (primer snapshot válido) bid Up = mid-d y bid Down = (1-mid)-d, fijos.
  sigue     d, g   : los dos bids siguen al mid (mid-d) en cada snapshot hasta el primer fill a p1;
                     entonces el otro lado queda fijo a 1-p1-g (coste del par = 1-g).
Todas cancelan lo no ejecutado CANCELA_S antes del cierre; una pata sola va a resolución.
Entrenamiento = primeros días, validación = últimos. Solo lectura.
"""
import bisect
import csv
import glob
import gzip
import random
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
MARCOS = {"5min": 300, "15min": 900}
ABRE_MIN_RESTO = {"5min": 200, "15min": 600}     # solo se entra si aún queda esto al primer snapshot
CANCELA_S = {"5min": 20, "15min": 45}
EPS = 1e-9
VARIANTES = ([("estatico", d, None) for d in (0.01, 0.02, 0.03, 0.05, 0.08)]
             + [("sigue", d, g) for d in (0.01, 0.02, 0.03) for g in (0.02, 0.04, 0.06)])


def abrir(p):
    return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")


def ruta(prefijo, dia):
    for c in (DATALOGS / f"{prefijo}_{dia}.csv", DATALOGS / f"{prefijo}_{dia}.csv.gz"):
        if c.exists():
            return c
    return None


def ts(s):
    return datetime.fromisoformat(s).timestamp()


def desenlaces():
    out = {}
    for p in glob.glob(str(REPO / "data/shadow/resolution_sniper_obs_2026-09-*.csv*")):
        with abrir(p) as f:
            for r in csv.DictReader(f):
                if r.get("outcome_real") in ("Up", "Down"):
                    out[r["condition_id"]] = r["outcome_real"]
    return out


def simular(var, snaps, prints_t, prints_up, gan, t_fin, marco):
    """snaps [(t, mid_up)] ordenados; prints: tiempos y precio-Up. -> (pnl, tipo, precio_1ª) | None."""
    nombre, d, g = var
    t_cancel = t_fin - CANCELA_S[marco]
    if not snaps or t_fin - snaps[0][0] < ABRE_MIN_RESTO[marco]:
        return None
    bu = bd = None          # bids vigentes (precio Up del bid de Up; precio Down del bid de Down)
    pu = pd = None          # precios ejecutados
    i = bisect.bisect_right(prints_t, snaps[0][0])
    k = 0
    n_s = len(snaps)
    while k < n_s and snaps[k][0] < t_cancel:
        t_s, mid = snaps[k]
        t_sig = min(snaps[k + 1][0] if k + 1 < n_s else t_cancel, t_cancel)
        if nombre == "estatico":
            if k == 0:
                bu, bd = mid - d, (1 - mid) - d
        else:
            if pu is None and pd is None:
                bu, bd = mid - d, (1 - mid) - d
        if bu is not None and (bu <= 0.01 or bd <= 0.01):
            return None if (pu is None and pd is None and k == 0) else None
        while i < len(prints_t) and prints_t[i] < t_sig:
            x = prints_up[i]
            if pu is None and bu is not None and x < bu - EPS:
                pu = bu
                if nombre == "sigue" and pd is None:
                    bd = 1 - pu - g
            if pd is None and bd is not None and (1 - x) < bd - EPS:
                pd = bd
                if nombre == "sigue" and pu is None:
                    bu = 1 - pd - g
            i += 1
            if pu is not None and pd is not None:
                return 1 - pu - pd, "par", None
        k += 1
    if pu is not None and pd is not None:
        return 1 - pu - pd, "par", None
    if pu is not None:
        return (1.0 if gan == "Up" else 0.0) - pu, "suelta", pu
    if pd is not None:
        return (1.0 if gan == "Down" else 0.0) - pd, "suelta", pd
    return 0.0, "nada", None


def main():
    dias = sys.argv[1:] or [f"2026-09-{d:02d}" for d in range(21, 30)]
    out = desenlaces()
    res = defaultdict(lambda: defaultdict(list))      # (marco, var) -> dia -> [(pnl, tipo, activo, p1)]
    for dia in dias:
        p_act, p_lib = ruta("polymarket_activity", dia), ruta("libro_ambos_lados", dia)
        if not (p_act and p_lib):
            print(dia, "faltan ficheros", flush=True)
            continue
        snaps, meta = defaultdict(list), {}
        with abrir(p_lib) as f:
            for r in csv.DictReader(f):
                if r["marco"] not in MARCOS or r["condition_id"] not in out:
                    continue
                try:
                    b, a = float(r["bid_yes"]), float(r["ask_yes"])
                    t = ts(r["timestamp_utc"])
                    fin = ts(r["end_date"])
                except (ValueError, TypeError):
                    continue
                if 0 < b <= a < 1 and a - b <= 0.06:
                    snaps[r["condition_id"]].append((t, (a + b) / 2))
                    meta[r["condition_id"]] = (r["marco"], r["activo"], fin)
        prints = defaultdict(list)
        with abrir(p_act) as f:
            for r in csv.DictReader(f):
                cid = r["condition_id"]
                if cid not in meta:
                    continue
                try:
                    p = float(r["price"])
                    t = ts(r["timestamp_utc"])
                except (ValueError, TypeError):
                    continue
                if not (0 < p < 1) or r["outcome"] not in ("Up", "Down"):
                    continue
                prints[cid].append((t, p if r["outcome"] == "Up" else 1 - p))
        n = 0
        for cid, s in snaps.items():
            pr = prints.get(cid)
            if not pr:
                continue
            s.sort()
            pr.sort()
            pt, pu = [x[0] for x in pr], [x[1] for x in pr]
            marco, activo, fin = meta[cid]
            for var in VARIANTES:
                r = simular(var, s, pt, pu, out[cid], fin, marco)
                if r:
                    res[(marco, var)][dia].append((r[0], r[1], activo, r[2]))
            n += 1
        print(dia, n, "mercados simulados", flush=True)

    dias_ok = sorted({d for v in res.values() for d in v})
    corte = dias_ok[len(dias_ok) * 5 // 9] if len(dias_ok) >= 4 else dias_ok[-1]
    print(f"\ndías {dias_ok[0]}..{dias_ok[-1]} ({len(dias_ok)}) | entrenamiento < {corte} <= validación")

    def resumen(vd):
        x = [t for d in vd.values() for t in d]
        if len(x) < 40:
            return None
        n = len(x)
        media = sum(t[0] for t in x) / n
        par = sum(t[1] == "par" for t in x) / n
        su = [t for t in x if t[1] == "suelta"]
        ks = list(vd)
        rng = random.Random(11)
        bs = []
        for _ in range(1000):
            s = [t[0] for k in (rng.choice(ks) for _ in ks) for t in vd[k]]
            bs.append(sum(s) / len(s))
        bs.sort()
        dias_pos = sum(1 for d in vd.values() if sum(t[0] for t in d) > 0)
        return (n, media, par, len(su) / n, (sum(t[0] for t in su) / len(su)) if su else 0.0,
                (bs[50], bs[950]), f"{dias_pos}/{len(vd)}")

    def fmt(r):
        return (f"{r[0]:6d} {r[1] * 100:+6.2f}c par {r[2]:4.0%} suelta {r[3]:4.0%} ({r[4] * 100:+6.1f}c) "
                f"IC90 ({r[5][0] * 100:+.2f},{r[5][1] * 100:+.2f})c días+ {r[6]}") if r else "(n<40)"

    for marco in MARCOS:
        print(f"\n== {marco}: céntimos por mercado cotizado, 1 acción por lado, sin fee (maker) ==")
        for var in VARIANTES:
            v = res[(marco, var)]
            a = resumen({d: t for d, t in v.items() if d < corte})
            b = resumen({d: t for d, t in v.items() if d >= corte})
            etiqueta = f"{var[0]} d={var[1]}" + (f" g={var[2]}" if var[2] is not None else "")
            print(f"{etiqueta:22s} ENTR {fmt(a)}\n{'':22s} VALI {fmt(b)}")
    for marco in MARCOS:
        cand = [((resumen({d: t for d, t in res[(marco, var)].items() if d < corte}) or (0, -9))[1], var) for var in VARIANTES]
        mejor = max(cand)[1]
        print(f"\n{marco}: mejor variante en ENTRENAMIENTO = {mejor} -> VALIDACIÓN por activo:")
        por = defaultdict(list)
        for d, t in res[(marco, mejor)].items():
            if d >= corte:
                for pnl, tipo, a, _ in t:
                    por[a].append((pnl, tipo))
        for a, v in sorted(por.items()):
            print(f"   {a}: n={len(v)} media {sum(x[0] for x in v) / len(v) * 100:+.2f}c  par {sum(x[1] == 'par' for x in v) / len(v):.0%}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
