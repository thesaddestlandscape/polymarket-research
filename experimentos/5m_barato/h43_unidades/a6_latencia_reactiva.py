#!/usr/bin/env python3
"""A6 H43 (20-Oct): ¿cuanto de la POBLACION R5K es capturable por una orden que REACCIONA al cruce de 5000 detectado en vivo?
Reproduce con DetectorR5K la banda en vivo (libro5: T con hora de RECEPCION) y, por unidad (mkt, lado), cosecha las K=50 acc
cosechables (T in (60,270]) solo de los fills RECIBIDOS >= t_cruce + L (L = latencia deteccion->orden en reposo: feed ~44 ms +
decision + alta GTC ~70-85 ms; L=0 es la poblacion original, el fill que cruza incluido). Cola OPTIMISTA (primeros de la cola).
Solo lectura, sin red (desenlaces desde caches), sin ordenes. Uso: a6_latencia_reactiva.py OUT.json --desde ISO --hasta ISO
  --tg ... --b ... --k ... [--gamma-cache f.json]"""
import argparse, json, os, sys
from collections import defaultdict
from datetime import datetime
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "a6_detector_vivo"))
from detector_r5k import DetectorR5K, OFFSET, K, T_MIN, T_COS_MAX                      # noqa: E402
from r5k_io import tokens_btc5, eventos_libro5, desenlaces_cache                      # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("out"); ap.add_argument("--desde", required=True); ap.add_argument("--hasta", required=True)
ap.add_argument("--tg", nargs="+", required=True); ap.add_argument("--b", nargs="*", default=[]); ap.add_argument("--k", nargs="+", required=True)
ap.add_argument("--gamma-cache"); a = ap.parse_args()
d0 = datetime.fromisoformat(a.desde.replace("Z", "+00:00")).timestamp(); d1 = datetime.fromisoformat(a.hasta.replace("Z", "+00:00")).timestamp()
tok = {t: v for t, v in tokens_btc5(a.k).items() if d0 <= v[2] <= d1}
mk = {v[0] for v in tok.values()}; cierre = {v[0]: v[2] for v in tok.values()}
det = DetectorR5K(tok, max_edad_s=10 ** 9)
ult = None
for e in eventos_libro5(a.tg, a.b, tok):
    if e[0] == "T":
        _, recv, _t, tk, pr, side, sz = e
        if not (d0 - 400 <= recv / 1000.0 <= d1 + 10): continue
        det.on_trade(tk, recv, pr, side, sz); ult = recv
    elif e[0] == "G":
        if e[3] == "baja": continue
        if e[3] == "arranque" and ult is not None: det.on_gap(None, ult)
        det.on_gap(e[2], e[1]); ult = e[1]
    else:
        det.on_snapshot(e[2], e[1]); ult = e[1]
des = desenlaces_cache()
if a.gamma_cache and os.path.exists(a.gamma_cache): des.update(json.load(open(a.gamma_cache)))
comp = {m: det.completo(m, cierre[m]) for m in mk}
por = defaultdict(list)                                    # (mkt, lado) -> filas (recv_ms, acc, coste, T, pc) en orden de llegada
for ts, m, l, acc, coste, T, pc, recv in det.filas: por[(m, l)].append((recv, acc, coste, T, pc))
def unidad(lst, g, lado, L):
    cum, t_cruce, need, take = 0.0, None, K, []
    for recv, acc, coste, T, pc in lst:
        new = cum + acc
        if t_cruce is None:
            if new < OFFSET: cum = new; continue
            t_cruce = recv; cand = min(new - OFFSET, acc)
        else: cand = acc
        if recv < t_cruce + L or not (T_MIN < T <= T_COS_MAX): continue
        th = min(cand, need)
        if th <= 0: continue
        take.append((pc, th)); need -= th
        if need <= 1e-9: break
    if not take: return None
    c = sum(t * p for p, t in take); p = sum(t * ((1.0 if g == lado else 0.0) - pc) for pc, t in take)
    return {"c": c, "p": p, "acc": K - need, "completa": need <= 1e-9}
res = {"ventana": [a.desde, a.hasta], "mercados": len(mk), "mercados_cobertura_completa": sum(comp.values()),
       "unidades_con_cruce_detectado": len(det.estado), "sin_desenlace": 0, "por_L_ms": {}}
for L in (0, 100, 250, 500, 1000, 2000, 5000):
    for etq, filt in (("todas", lambda m: True), ("cobertura_completa", lambda m: comp.get(m, False))):
        us, sd, cierres = [], 0, defaultdict(lambda: [0.0, 0.0])
        for (m, lado), lst in por.items():
            if not filt(m): continue
            g = des.get(m)
            if g is None: sd += 1; continue
            u = unidad(lst, g, lado, L)
            if u: us.append(u); cierres[cierre[m]][0] += u["c"]; cierres[cierre[m]][1] += u["p"]
        cp = [u for u in us if u["completa"]]
        def ev(x): c = sum(u["c"] for u in x); p = sum(u["p"] for u in x); return {"n": len(x), "coste": round(c, 2), "ev": round(p / c, 4) if c else None}
        res["por_L_ms"].setdefault(str(L), {})[etq] = {"completas": ev(cp), "todas_incl_parciales": ev(us),
            "acc_media_cosechada": round(sum(u["acc"] for u in us) / len(us), 2) if us else None, "frac_completas": round(len(cp) / len(us), 3) if us else None}
        res["sin_desenlace"] = max(res["sin_desenlace"], sd)
json.dump(res, open(a.out, "w"), indent=1, ensure_ascii=False)
for L, v in res["por_L_ms"].items(): print(L, json.dumps(v["cobertura_completa"]), flush=True)
