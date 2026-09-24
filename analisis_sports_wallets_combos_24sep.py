#!/usr/bin/env python3
"""analisis_sports_wallets_combos_24sep.py -- ¿hay wallets de sports expertas en
COMBOS (varias piernas en mercados distintos del MISMO evento) cuyo edge
PERSISTE fuera de muestra? (24-Sep, petición Javi: "tenemos que seguir a las
wallets expertas en combos, hay pasta ahí").

Combo = (wallet, event_slug) con compras BUY en >=2 condition_id distintos.
PnL del combo = sum(shares * 1{outcome_index == ganador}) - coste, sin fee (se
reporta aparte el ROI; fee sports 0,05*p*(1-p)/share es de 2º orden aquí).

Rigor:
- Walk-forward: wallets elegidas SOLO con combos cuyo primer trade cae antes de
  CORTE (n>=N_SEL combos, ROI>0); se miden en combos POSTERIORES al corte.
  Base de comparación: TODOS los combos posteriores de wallets con >=N_SEL
  combos previos (mismo filtro de actividad, sin mirar su ROI).
- Unidad = combo (wallet,evento); CI90 bootstrap por DÍAS del combo; cuota de
  la wallet top en el grupo seleccionado.
Streaming (agregación por wallet,evento,cid,outcome_index): ~1 GB con 21 días.
Solo lectura; salida data/sports/wallets_combos_24sep.json.
"""
import csv
import glob
import gzip
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
from sports_wallet_mirror_sniper import _outcomes_por_lote  # noqa: E402

DIR = REPO / "data/sports"
OUT = DIR / "wallets_combos_24sep.json"
CACHE_OUTCOMES = DIR / "combos_outcomes_cache.json"  # gitignorado; solo mercados ya cerrados
N_SEL = 5
FRAC_CORTE = 0.6


def cargar():
    """agg[(wallet, evento)][(cid, idx)] = [shares, coste, ts_min]"""
    agg = defaultdict(dict)
    cat_ev = {}
    for path in sorted(glob.glob(str(DIR / "activity_ws_*.csv*"))):
        op = gzip.open if path.endswith(".gz") else open
        with op(path, "rt", newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                if (r.get("side") or "").upper() != "BUY":
                    continue
                ev, cid, w = r.get("event_slug"), r.get("condition_id"), (r.get("wallet") or "").lower()
                if not ev or not cid or not w:
                    continue
                try:
                    p, sz, idx = float(r["price"]), float(r["size"]), int(r["outcome_index"])
                except (TypeError, ValueError, KeyError):
                    continue
                if not (0 < p < 1) or sz <= 0:
                    continue
                k = (sys.intern(w), sys.intern(ev))
                leg = (sys.intern(cid), idx)
                v = agg[k].get(leg)
                ts = r.get("timestamp_utc", "")
                if v is None:
                    agg[k][leg] = [sz, sz * p, ts]
                else:
                    v[0] += sz; v[1] += sz * p
                    if ts < v[2]:
                        v[2] = ts
                cat_ev.setdefault(ev, r.get("categoria", ""))
        print(f"  leído {Path(path).name}: {len(agg)} (wallet,evento)", flush=True)
    combos = {k: legs for k, legs in agg.items() if len({c for c, _ in legs}) >= 2}
    return combos, cat_ev


def outcomes_conocidos() -> dict:
    out = {}
    with open(DIR / "wallet_mirror_sniper_dry_run.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r.get("outcome_real_index") not in (None, ""):
                out[r["condition_id"]] = int(r["outcome_real_index"])
    return out


def main():
    t0 = time.time()
    combos, cat_ev = cargar()
    print(f"combos (>=2 mercados del mismo evento): {len(combos)}  [{time.time()-t0:.0f}s]", flush=True)
    res = outcomes_conocidos()
    if CACHE_OUTCOMES.exists():
        res.update({k: int(v) for k, v in json.loads(CACHE_OUTCOMES.read_text()).items()})
    faltan = sorted({c for legs in combos.values() for c, _ in legs} - set(res))
    print(f"cids en combos: resueltos por dry-run {len(res)}, a consultar {len(faltan)}", flush=True)
    for i in range(0, len(faltan), 20):
        r = _outcomes_por_lote(faltan[i:i + 20])
        if r:
            res.update(r)
        time.sleep(0.25)
        if i % 4000 == 0:
            print(f"  gamma {i}/{len(faltan)}", flush=True)

    CACHE_OUTCOMES.write_text(json.dumps(res))
    filas = []  # un combo resuelto (todas sus piernas resueltas)
    for (w, ev), legs in combos.items():
        if any(c not in res for c, _ in legs):
            continue
        coste = sum(v[1] for v in legs.values())
        fee = sum(0.05 * (v[1] / v[0]) * (1 - v[1] / v[0]) * v[0] for v in legs.values())
        pago = sum(v[0] for (c, idx), v in legs.items() if res[c] == idx) - fee
        ts = min(v[2] for v in legs.values())
        filas.append({"w": w, "ev": ev, "cat": cat_ev.get(ev, ""), "ts": ts, "dia": ts[:10],
                      "coste": coste, "pnl": pago - coste, "piernas": len(legs)})
    print(f"combos resueltos: {len(filas)}", flush=True)
    filas.sort(key=lambda x: x["ts"])
    dias = sorted({f["dia"] for f in filas})
    corte = dias[int(len(dias) * FRAC_CORTE)]
    antes = [f for f in filas if f["dia"] < corte]
    despues = [f for f in filas if f["dia"] >= corte]

    por_w = defaultdict(list)
    for f in antes:
        por_w[f["w"]].append(f)
    activas = {w for w, fs in por_w.items() if len(fs) >= N_SEL}
    elegidas = {w for w in activas
                if sum(f["pnl"] for f in por_w[w]) / max(1e-9, sum(f["coste"] for f in por_w[w])) > 0}

    def resumen(fs, seed):
        if not fs:
            return {"n": 0}
        roi = sum(f["pnl"] for f in fs) / sum(f["coste"] for f in fs)
        por_dia = defaultdict(lambda: [0.0, 0.0])
        for f in fs:
            por_dia[f["dia"]][0] += f["pnl"]; por_dia[f["dia"]][1] += f["coste"]
        d = list(por_dia.values())
        rng = np.random.default_rng(seed)
        bs = []
        for _ in range(2000):
            idx = rng.integers(0, len(d), len(d))
            p = sum(d[i][0] for i in idx); c = sum(d[i][1] for i in idx)
            bs.append(p / c if c else 0)
        top = max(defaultdict(int, {f["w"]: 0 for f in fs}).keys(),
                  key=lambda w: sum(1 for f in fs if f["w"] == w))
        return {"n_combos": len(fs), "n_dias": len(d), "n_wallets": len({f["w"] for f in fs}),
                "top_wallet_pct": round(sum(1 for f in fs if f["w"] == top) / len(fs), 3),
                "roi": round(roi, 4), "ci90_roi_dia": [round(float(np.percentile(bs, 5)), 4),
                                                        round(float(np.percentile(bs, 95)), 4)],
                "win_rate": round(sum(f["pnl"] > 0 for f in fs) / len(fs), 3),
                "coste_total_usd": round(sum(f["coste"] for f in fs), 0)}

    def roi(fs):
        c = sum(f["coste"] for f in fs)
        return sum(f["pnl"] for f in fs) / c if c else 0.0

    def ci_lo_wallet(fs, seed):
        rng = np.random.default_rng(seed)
        p = np.array([f["pnl"] for f in fs]); c = np.array([f["coste"] for f in fs])
        bs = [p[i].sum() / c[i].sum() for i in (rng.integers(0, len(fs), len(fs)) for _ in range(300))]
        return float(np.percentile(bs, 5))

    reglas = {
        "R2_n20_roi5": {w for w in activas if len(por_w[w]) >= 20 and roi(por_w[w]) >= 0.05},
    }
    reglas["R3_n20_roi5_ci"] = {w for w in reglas["R2_n20_roi5"] if ci_lo_wallet(por_w[w], hash(w) & 0xFFFF) > 0}
    por_wc = defaultdict(list)
    for f in antes:
        por_wc[(f["w"], f["cat"])].append(f)
    expertos_cat = {k for k, fs in por_wc.items() if len(fs) >= 10 and roi(fs) >= 0.10}

    sel = [f for f in despues if f["w"] in elegidas]
    base = [f for f in despues if f["w"] in activas]
    out = {"corte": corte, "dias": [dias[0], dias[-1]], "n_combos_resueltos": len(filas),
           "wallets_activas_pre": len(activas), "wallets_elegidas_pre": len(elegidas),
           "forward_elegidas": resumen(sel, 1), "forward_base_activas": resumen(base, 2),
           "por_categoria_elegidas": {},
           "reglas_estrictas": {k: {"n_wallets_pre": len(v), "forward": resumen([f for f in despues if f["w"] in v], 10 + i)}
                                for i, (k, v) in enumerate(reglas.items())}}
    out["reglas_estrictas"]["R4_experto_wallet_x_categoria_n10_roi10"] = {
        "n_pares_pre": len(expertos_cat),
        "forward": resumen([f for f in despues if (f["w"], f["cat"]) in expertos_cat], 20)}
    cats = defaultdict(list)
    for f in sel:
        cats[f["cat"]].append(f)
    for c, fs in sorted(cats.items(), key=lambda x: -len(x[1])):
        if len(fs) >= 30:
            out["por_categoria_elegidas"][c] = resumen(fs, 3)
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
