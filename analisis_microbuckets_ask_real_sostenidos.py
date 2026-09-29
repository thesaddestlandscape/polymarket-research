#!/usr/bin/env python3
"""analisis_microbuckets_ask_real_sostenidos.py -- micro-buckets de precio por
tupla (strategy#activo#marco#decision) con edge REAL SOSTENIDO al ASK REAL
(29-Sep, petición Javi: "no de shadow, necesitamos reales" + "hay
micro-buckets en gbm que dan positivo y llevan días sostenidos").

Fuente: ask_real_por_senal.csv (ask del token propio en el primer libro
POSTERIOR a la señal, libro_book_ws; sin profundidad -> cota optimista de
fill) unido a results.csv (activo/marco/acierto) con las mismas funciones
que ask_real_por_senal.py (cargar_senales, pnl con fee 7 %, bucket de
gate_bucket_propio). NUNCA precio_yes_mercado de la señal.

Gate "sostenido" (todos a la vez, fail-closed):
  n_ask >= 40, EV/EUR >= +0.10, IC90 bootstrap por DIAS con lo > 0,
  >= 60 % de días positivos con >= 8 días, ambas mitades cronológicas
  (por día) con EV > 0, y BH-FDR q=0.10 sobre p de bootstrap por días
  (corrige haber mirado cientos de buckets).
No promueve nada: es la lista de CANDIDATAS con evidencia real; promoción =
checklist de 6 categorías + /code-review + OK Javi. Salida:
data/shadow/microbuckets_ask_real_sostenidos.json. Solo lectura.

Uso: python3 analisis_microbuckets_ask_real_sostenidos.py [--familia GBM]
"""
import argparse
import csv
import json
import random
import statistics as st
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

import ask_real_por_senal as ARS  # noqa: E402
from gate_bucket_propio import bucket  # noqa: E402

CSV_ASK = REPO / "data/shadow/ask_real_por_senal.csv"
CONFIG_LIVE = REPO / "data/live/config_live.json"
OUT = REPO / "data/shadow/microbuckets_ask_real_sostenidos.json"

N_MIN, EV_MIN, DIAS_MIN, FRAC_POS, Q_BH = 40, 0.10, 8, 0.60, 0.10


def _bootstrap(por_dia: dict, it=2000):
    ds = list(por_dia.values())
    rng = random.Random(7)
    m = []
    for _ in range(it):
        s = [v for _ in ds for v in rng.choice(ds)]
        m.append(sum(s) / len(s))
    m.sort()
    p_le0 = sum(1 for x in m if x <= 0) / it
    return m[int(0.05 * it)], m[int(0.95 * it) - 1], p_le0


def cargar_unidades(dias: int):
    desde = (datetime.now(timezone.utc) - timedelta(days=dias)).strftime("%Y-%m-%d")
    sen = ARS.cargar_senales(desde)
    idx = {(s["st"], s["mid"], s["dec"]): s for s in sen}
    U = []
    with open(CSV_ASK, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            if not r["ask"]:
                continue
            s = idx.get((r["strategy"], r["market_id"], r["decision"]))
            if not s:
                continue
            ask = float(r["ask"])
            if not 0.02 <= ask <= 0.98:
                continue
            dia = datetime.fromtimestamp(s["t"], timezone.utc).date().isoformat()
            U.append({"tupla": f"{s['st']}#{s['act']}#{s['marco']}#{s['dec']}",
                      "bucket": f"{bucket(s['py']):.2f}", "dia": dia, "pnl": ARS.pnl(ask, s["ac"]),
                      "ask": ask})
    return U


def _anadir_fill_libro_real(cands):
    """% de mercados con profundidad >=5x stake (libro real de live, libro_snapshots.csv, colapsado por
    market_id = max ratio) en el MISMO (tupla, bucket). ask_real no mide profundidad -> esta es la
    corrección de fill-ability; arquetipo A tiene 6-36 %."""
    want = {(c["tupla"], c["bucket"]) for c in cands}
    mx = defaultdict(float)
    try:
        with open(REPO / "data/live/libro_snapshots.csv", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f):
                try:
                    pp, ra = float(r["precio_plan"]), float(r["ratio_vs_stake"])
                except (ValueError, KeyError):
                    continue
                py = pp if r["direction"] == "BUY_YES" else 1 - pp
                t = f"{r['strategy']}#{r['subtype']}#{r['direction']}"
                b = f"{bucket(py):.2f}"
                if (t, b) in want:
                    k = (t, b, r["market_id"])
                    mx[k] = max(mx[k], ra)
    except OSError:
        pass
    agg = defaultdict(list)
    for (t, b, _), ra in mx.items():
        agg[(t, b)].append(ra)
    for c in cands:
        v = agg.get((c["tupla"], c["bucket"]), [])
        c["fill_libro_real"] = round(sum(r >= 5 for r in v) / len(v), 3) if len(v) >= 15 else None
        c["n_mercados_libro"] = len(v)


def evaluar(dias=21, familia=None):
    U = cargar_unidades(dias)
    if familia:
        U = [u for u in U if u["tupla"].startswith(familia) or f"#{familia}" in u["tupla"]]
    live = set(json.loads(CONFIG_LIVE.read_text(encoding="utf-8")).get("pares_permitidos_live", []))
    G = defaultdict(list)
    for u in U:
        G[(u["tupla"], u["bucket"])].append(u)
    cand = []
    for (tupla, b), xs in G.items():
        if len(xs) < N_MIN:
            continue
        por_dia = defaultdict(list)
        for u in xs:
            por_dia[u["dia"]].append(u["pnl"])
        dias_ord = sorted(por_dia)
        if len(dias_ord) < DIAS_MIN:
            continue
        ev = st.mean(u["pnl"] for u in xs)
        lo, hi, p = _bootstrap(por_dia)
        pos = sum(1 for d in dias_ord if sum(por_dia[d]) > 0)
        mid = len(dias_ord) // 2
        m1 = [v for d in dias_ord[:mid] for v in por_dia[d]]
        m2 = [v for d in dias_ord[mid:] for v in por_dia[d]]
        cand.append({"tupla": tupla, "bucket": b, "n": len(xs), "ev_eur": round(ev, 4),
                     "ic90_dias": [round(lo, 4), round(hi, 4)], "dias": len(dias_ord), "dias_pos": pos,
                     "ev_mitad1": round(st.mean(m1), 4) if m1 else None,
                     "ev_mitad2": round(st.mean(m2), 4) if m2 else None,
                     "ask_medio": round(st.mean(u["ask"] for u in xs), 3), "p_boot": p,
                     "live": tupla in live})
    # BH-FDR sobre p de bootstrap (una cola, mitad positiva)
    cand.sort(key=lambda c: c["p_boot"])
    m = len(cand)
    corte = -1
    for i, c in enumerate(cand, 1):
        if c["p_boot"] <= Q_BH * i / m:
            corte = i
    for i, c in enumerate(cand, 1):
        c["bh_ok"] = i <= corte
        c["base_sin_bh"] = bool(c["ev_eur"] >= EV_MIN and c["ic90_dias"][0] > 0
                                and c["dias_pos"] >= FRAC_POS * c["dias"]
                                and (c["ev_mitad1"] or -1) > 0 and (c["ev_mitad2"] or -1) > 0)
        c["sostenido"] = bool(c["base_sin_bh"] and c["bh_ok"])
    _anadir_fill_libro_real([c for c in cand if c["base_sin_bh"]])
    cand.sort(key=lambda c: -c["ev_eur"])
    return {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "dias": dias,
            "criterio": {"n_min": N_MIN, "ev_min": EV_MIN, "dias_min": DIAS_MIN, "frac_dias_pos": FRAC_POS,
                         "bh_q": Q_BH, "fuente": "ask_real_por_senal.csv (ask real, fee 7%)"},
            "n_buckets_testeados": m, "candidatas": cand}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--familia", default=None)
    ap.add_argument("--dias", type=int, default=21)
    a = ap.parse_args()
    r = evaluar(a.dias, a.familia)
    if not a.familia:
        OUT.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"buckets testeados (n>={N_MIN}, >={DIAS_MIN} dias): {r['n_buckets_testeados']}")
    for c in r["candidatas"]:
        if c["ev_eur"] < 0.05:
            continue
        print(f"{'✅' if c['sostenido'] else ('◐' if c['base_sin_bh'] else ' ')} {c['tupla']:50s}[{c['bucket']}] n={c['n']:4d} EV={c['ev_eur']:+.3f} "
              f"IC90d[{c['ic90_dias'][0]:+.2f},{c['ic90_dias'][1]:+.2f}] dias={c['dias']} pos={c['dias_pos']} "
              f"mitades[{c['ev_mitad1']:+.2f},{c['ev_mitad2']:+.2f}] bh={c['bh_ok']} {'LIVE' if c['live'] else ''}")


if __name__ == "__main__":
    main()
