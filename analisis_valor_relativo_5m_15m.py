#!/usr/bin/env python3
"""analisis_valor_relativo_5m_15m.py -- usar el mercado de 5 min (eficiente) como precio justo del de 15 min (30-Sep).

El último tramo de 5 min de cada ventana de 15 min cierra en el MISMO instante y con el MISMO precio de cierre; solo
cambia la referencia de apertura. Si ref15 < ref5, "sube en 5 min" IMPLICA "sube en 15 min" (cierre > ref5 > ref15),
así que P(Up15) >= P(Up5): si el ask de Up en 15 min está por debajo del bid de Up en 5 min, el de 15 min está barato
respecto a un mercado que sabemos eficiente. Simétrico con Down si ref15 > ref5. No es el arbitraje anidado (comprar
las dos patas, refutado): aquí se compra UNA pata, la barata, y se lleva a resolución.

Datos: libro_ambos_lados (fotos de ambos lados, ~1-2 min, 10-30 Sep), referencias de apertura y desenlace de
resolution_sniper_obs. Solo pares con referencias separadas >= GAP_MIN bps (con gaps menores el orden de las
referencias no es fiable). Comisión real 7 % x (1-precio). Una entrada por mercado de 15 min (la primera que cumple).
Solo lectura. Uso: analisis_valor_relativo_5m_15m.py
"""
import bisect
import collections
import csv
import glob
import gzip
import random
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")
FEE, GAP_MIN, DT_MAX = 0.07, 2.0, 20.0


def ab(p):
    return gzip.open(p, "rt", encoding="utf-8", newline="") if str(p).endswith(".gz") else open(p, encoding="utf-8", newline="")


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def main() -> int:
    random.seed(8)
    res = []            # (dia, margen, pnl, ok, ask, tipo)
    stats = collections.Counter()
    for f in sorted(glob.glob(str(DATALOGS / "libro_ambos_lados_*.csv*"))):
        dia = f.split("libro_ambos_lados_")[1][:10]
        obs = None
        for cand in (REPO / f"data/shadow/resolution_sniper_obs_{dia}.csv", REPO / f"data/shadow/resolution_sniper_obs_{dia}.csv.gz"):
            if cand.exists():
                obs = cand
        if obs is None:
            continue
        info = {}                                  # market_id -> (activo, marco, ts_end, ref, outcome)
        with ab(obs) as fh:
            for r in csv.DictReader(fh):
                if r.get("outcome_real") in ("Up", "Down") and r.get("chainlink_ref_open"):
                    try:
                        info[r["market_id"]] = (r["activo"], r["marco"], int(float(r["ts_end"])), float(r["chainlink_ref_open"]), r["outcome_real"])
                    except ValueError:
                        pass
        por_fin = collections.defaultdict(dict)    # (activo, ts_end) -> {marco: market_id}
        for mid, (act, marco, fin, ref, out) in info.items():
            por_fin[(act, fin)][marco.replace("min", "m")] = mid
        fotos = collections.defaultdict(list)      # market_id -> [(t, ask_yes, ask_no, bid_yes, bid_no)]
        with ab(f) as fh:
            for r in csv.DictReader(fh):
                if r["market_id"] not in info:
                    continue
                try:
                    fotos[r["market_id"]].append((ts(r["timestamp_utc"]), float(r["ask_yes"]), float(r["ask_no"]), float(r["bid_yes"]), float(r["bid_no"])))
                except (ValueError, TypeError):
                    continue
        for (act, fin), d in por_fin.items():
            if "5m" not in d or "15m" not in d:
                continue
            m5, m15 = d["5m"], d["15m"]
            r5, r15 = info[m5][3], info[m15][3]
            gap = (r5 / r15 - 1) * 1e4
            stats["pares"] += 1
            if abs(gap) < GAP_MIN:
                stats["gap_pequeño"] += 1
                continue
            lado = "Up" if gap > 0 else "Down"           # ref15 < ref5: Up5 => Up15 ; ref15 > ref5: Down5 => Down15
            o5, o15 = info[m5][4], info[m15][4]
            stats["implicación_medible"] += 1
            if o5 == lado and o15 != lado:
                stats["implicación_ROTA"] += 1
            f5 = sorted(fotos.get(m5, []))
            t5 = [x[0] for x in f5]
            hecho = False
            for t, ay, an, by, bn in sorted(fotos.get(m15, [])):
                if hecho or not fin - 290 <= t <= fin - 15 or not f5:
                    continue
                i = min(range(max(0, bisect.bisect_left(t5, t) - 1), min(len(f5), bisect.bisect_left(t5, t) + 1)), key=lambda k: abs(t5[k] - t))
                if abs(t5[i] - t) > DT_MAX:
                    continue
                ask15 = ay if lado == "Up" else an
                bid5 = f5[i][3] if lado == "Up" else f5[i][4]
                if not 0.05 <= ask15 < 0.97 or bid5 <= 0:
                    continue
                stats["fotos_comparables"] += 1
                margen = bid5 - ask15
                if margen >= 0.02:
                    ok = 1 if o15 == lado else 0
                    res.append((dia, margen, ok / ask15 - 1 - FEE * (1 - ask15), ok, ask15, abs(gap), fin - t))
                    hecho = True
    print(dict(stats))
    if stats["implicación_medible"]:
        print(f"la implicación se rompe en {stats['implicación_ROTA']} de {stats['implicación_medible']} pares "
              f"({stats['implicación_ROTA'] / stats['implicación_medible']:.2%}): mide lo fiable que es el orden de las referencias")

    def rep(nombre, v):
        if len(v) < 15:
            print(f"{nombre:34s} n={len(v)}")
            return
        pd = collections.defaultdict(list)
        for x in v:
            pd[x[0]].append(x[2])
        ks, bs = [k for k in pd], []
        for _ in range(1000):
            s = [y for k in random.choices(ks, k=len(ks)) for y in pd[k]]
            bs.append(sum(s) / len(s))
        bs.sort()
        print(f"{nombre:34s} n={len(v):4d} ({len(v) / len(pd):.1f}/día, {len(pd)} días) acierto={sum(x[3] for x in v) / len(v):.3f} ask15={sum(x[4] for x in v) / len(v):.3f} "
              f"margen={sum(x[1] for x in v) / len(v):.3f} EV={sum(x[2] for x in v) / len(v):+.4f} IC90=({bs[50]:+.3f},{bs[949]:+.3f}) días+={sum(1 for z in pd.values() if sum(z) > 0)}/{len(pd)}")
    print("\ncomprar la pata barata del de 15 min cuando bid(5m) - ask(15m) >= margen:")
    for m in (0.02, 0.03, 0.05, 0.08, 0.12):
        rep(f"  margen >= {m:.2f}", [x for x in res if x[1] >= m])
    for lo, hi in ((0.05, 0.4), (0.4, 0.6), (0.6, 0.8), (0.8, 0.97)):
        rep(f"  margen>=0.03, ask15 [{lo},{hi})", [x for x in res if x[1] >= 0.03 and lo <= x[4] < hi])
    for g in (2, 5, 10):
        rep(f"  margen>=0.03, gap refs >= {g} bps", [x for x in res if x[1] >= 0.03 and x[5] >= g])
    for lo, hi in ((15, 60), (60, 150), (150, 291)):
        rep(f"  margen>=0.03, resto [{lo},{hi}) s", [x for x in res if x[1] >= 0.03 and lo <= x[6] < hi])
    return 0


if __name__ == "__main__":
    sys.exit(main())
