#!/usr/bin/env python3
"""H43 auditoria (19-Oct, solo lectura, ligero). Sobre band_D de pass1.
(a) K POSICIONAL (vigia/recon: las 50 acc de la ventana [5000,5050) de posicion; los fills con T fuera de (60,270] consumen posicion)
(b) K COSECHABLE (registro literal y validador 17-Oct: las 50 primeras acc de fills con T en (60,270] tras cruzar 5000)
(c) controles de regimen por dia: volumen de banda, mercados que cruzan 5000, concentracion de makers (top-5 y top-1 wallet).
Uso: python3 -I a4_definicion_k_y_regimen.py OUTJSON D1 D2 ..."""
import csv, gzip, json, os, sys, datetime, random
from collections import defaultdict
DISC = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/scratch_17oct/vend/out"
VIGC = "/root/polymarket-research-datalogs/vigia_5m_barato_r5k"
OFF, K, TMIN, TMAX, HTMAX = 5000.0, 50.0, 60.0, 300.0, 270.0
DES = {}
for f in ("/root/polymarket-research/experimentos/5m_barato/h43_auditoria_datos/des_cache_descubrimiento.json",
          "/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json"):
    DES.update(json.load(open(f)))
OUT = sys.argv[1]; DIAS = sys.argv[2:]
def band(d):
    for f in (f"{DISC}/band_{d}.csv.gz", f"{VIGC}/{d}/out/band_{d}.csv.gz"):
        if os.path.exists(f): return f
def leer(d):
    rows = []
    with gzip.open(band(d), "rt") as fh:
        rd = csv.reader(fh); h = next(rd); ix = {k: i for i, k in enumerate(h)}
        for c in rd:
            if c[ix["act"]] != "BTC": continue
            rows.append((float(c[ix["ts"]]), int(float(c[ix["li"]])), c[ix["mkt"]], c[ix["lado_c"]], float(c[ix["acc"]]),
                         float(c[ix["coste"]]), float(c[ix["T"]]), float(c[ix["pc"]]), c[ix["maker"]]))
    return rows
def unid_posicional(rows):
    cum = defaultdict(float); U = {}
    for ts, li, mkt, lado, acc, coste, T, pc, mk in sorted(rows, key=lambda r: (r[2], r[3], r[0], r[1])):
        k = (mkt, lado); c0 = cum[k]; cum[k] = c0 + acc
        if acc <= 0 or not (TMIN < T <= HTMAX): continue
        lo, hi = max(c0 - OFF, 0.0), max(c0 + acc - OFF, 0.0)
        tk = max(min(K, hi) - min(K, lo), 0.0)
        if tk <= 0 or DES.get(mkt) is None: continue
        f = tk / acc; g = DES[mkt]
        u = U.setdefault(k, {"fin": round((ts + T) / 300) * 300, "c": 0.0, "p": 0.0, "acc": 0.0})
        u["c"] += coste * f; u["p"] += (acc * (g == lado) - coste) * f; u["acc"] += tk
    return U
def unid_cosechable(rows):
    seq = defaultdict(list)
    for r in sorted(rows, key=lambda r: (r[2], r[3], r[0], r[1])): seq[(r[2], r[3])].append(r)
    U = {}
    for k, lst in seq.items():
        mkt, lado = k
        if DES.get(mkt) is None: continue
        cum = 0.0; crossed = False; need = K; take = []
        for ts, li, _, _, acc, coste, T, pc, _ in lst:
            if not crossed:
                new = cum + acc
                if new >= OFF:
                    crossed = True; cand = min(new - OFF, acc)
                else:
                    cum = new; continue
            else:
                cand = acc
            if not (TMIN < T <= HTMAX): continue
            th = min(cand, need)
            if th <= 0: continue
            take.append((pc, th)); need -= th
            if need <= 1e-9: break
        if not take: continue
        g = DES[mkt]
        c = sum(t * p for p, t in take); pnl = sum(t * ((1.0 if g == lado else 0.0) - p) for p, t in take)
        U[k] = {"fin": round((lst[0][0] + lst[0][6]) / 300) * 300, "c": c, "p": pnl, "acc": K - need, "completa": need <= 1e-9}
    return U
def ev(U, f=lambda u: True):
    us = [u for u in U.values() if f(u)]; c = sum(u["c"] for u in us); p = sum(u["p"] for u in us)
    return {"n": len(us), "coste": round(c, 2), "ev": round(p / c, 4) if c else None}
def ic_cierre(U, B=2000, seed=11):
    g = defaultdict(lambda: [0.0, 0.0])
    for u in U.values(): g[u["fin"]][0] += u["c"]; g[u["fin"]][1] += u["p"]
    g = list(g.values())
    if len(g) < 3: return None
    r = random.Random(seed); bs = []
    for _ in range(B):
        m = [r.choice(g) for _ in g]; c = sum(x[0] for x in m); bs.append(sum(x[1] for x in m) / c if c else 0.0)
    bs.sort(); return [round(bs[int(B * .05)], 3), round(bs[int(B * .95) - 1], 3)]
res = {"definiciones": {}, "regimen": {}}
POS, COS, COSC = {}, {}, {}
for d in DIAS:
    rows = leer(d)
    up = unid_posicional(rows); uc = unid_cosechable(rows)
    for k, u in up.items(): POS[(d,) + k] = dict(u, dia=d)
    for k, u in uc.items(): COS[(d,) + k] = dict(u, dia=d)
    # regimen
    accs = defaultdict(float); mk_acc = defaultdict(float); mercados = defaultdict(float); cruza = 0
    tot = sum(r[4] for r in rows)
    for r in rows:
        mk_acc[r[8]] += r[4]; mercados[r[2]] += r[4]
    top = sorted(mk_acc.values(), reverse=True)
    cru = 0
    cum = defaultdict(float)
    for r in sorted(rows, key=lambda r: (r[2], r[3], r[0], r[1])):
        k = (r[2], r[3]); before = cum[k]; cum[k] += r[4]
        if before < OFF <= cum[k]: cru += 1
    res["regimen"][d] = {"filas_banda": len(rows), "acc_banda": round(tot, 1), "mercados": len(mercados),
                         "mercados_cruzan_5000": cru, "acc_medio_por_mercado": round(tot / max(len(mercados), 1), 1),
                         "makers_distintos": len(mk_acc), "top5_makers_share": round(sum(top[:5]) / tot, 3) if tot else None,
                         "top1_maker_share": round(top[0] / tot, 3) if tot else None}
    print(d, json.dumps(res["regimen"][d]), flush=True)
def bloque(U, pref):
    out = {}
    for name, f in [("todas", lambda u: True), ("completas", lambda u: u.get("completa", True) if "completa" in u else (u["acc"] >= K - 1e-6)),
                    ("incompletas", lambda u: not (u.get("completa", True) if "completa" in u else (u["acc"] >= K - 1e-6)))]:
        out[name] = ev(U, f)
    return out
res["definiciones"]["posicional_vigia"] = bloque(POS, "")
res["definiciones"]["cosechable_registro_validador"] = bloque(COS, "")
def por_periodo(U, lo, hi):
    return ev({k: v for k, v in U.items() if lo <= k[0] <= hi})
for nm, U in (("posicional_vigia", POS), ("cosechable_registro_validador", COS)):
    res.setdefault("periodos", {})[nm] = {
        "in_06_16_por_dia": {d: ev({k: v for k, v in U.items() if k[0] == d}) for d in DIAS if "2026-10-06" <= d <= "2026-10-16"},
        "in_06_16": por_periodo(U, "2026-10-06", "2026-10-16"),
        "fw_17": por_periodo(U, "2026-10-17", "2026-10-17"),
        "ic90_cierre_in_06_16": ic_cierre({k: v for k, v in U.items() if "2026-10-06" <= k[0] <= "2026-10-16"}),
        "ic90_cierre_fw_17": ic_cierre({k: v for k, v in U.items() if k[0] == "2026-10-17"}),
    }
json.dump(res, open(OUT, "w"), indent=1, ensure_ascii=False)
print(json.dumps(res["definiciones"], ensure_ascii=False))
print(json.dumps(res["periodos"], ensure_ascii=False)[:1500])
