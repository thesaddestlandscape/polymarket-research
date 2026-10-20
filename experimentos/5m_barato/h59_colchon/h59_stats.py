"""h59_stats.py -- estadistica del forward H59 (sin E/S salvo lectura). EV PONDERADO POR EUR (sum pnl / sum coste), IC90 por dias y por
cierre (bootstrap, semilla fija), sin 2 mejores dias, sin top 5 % de operaciones, diferencia emparejada/incremental, gate y kill.
Una operacion = {dia, cierre, pnl, coste, precio, gana}. Desenlace ausente => la operacion NO entra (se cuenta como pendiente)."""
import math
import numpy as np

NBOOT, SEED = 4000, 20261020
GATE = {"n": 40, "dias_con_operacion": 10, "ev_pond": 0.10, "ic90_dias_inf": 0.0, "sin_2_mejores_dias": 0.0, "sin_top5pct": 0.0}
KILL = {"ev_pond_lt": -0.15, "n_ev": 25, "incremental_ev_lt": -0.15, "n_incremental": 10, "ic90_cierre_sup_lt0_n": 20}


def boot_ratio(grupos, q=5, nboot=NBOOT, seed=SEED):
    """IC (q, 100-q) % de sum pnl / sum coste remuestreando GRUPOS (dias o cierres). None si <3 grupos (no se inventa un IC)."""
    g = np.array(grupos, dtype=float)
    if len(g) < 3:
        return None
    rng = np.random.default_rng(seed)
    ix = rng.integers(0, len(g), (nboot, len(g)))
    r = g[ix, 0].sum(1) / np.maximum(g[ix, 1].sum(1), 1e-12)
    return tuple(float(x) for x in np.percentile(r, [q, 100 - q]).round(4))


def por_dia(ops):
    d = {}
    for o in ops:
        a = d.setdefault(o["dia"], [0.0, 0.0])
        a[0] += o["pnl"]
        a[1] += o["coste"]
    return d


def resumen(ops, nombre):
    out = {"brazo": nombre, "n": len(ops)}
    if not ops:
        return out
    pn, co = sum(o["pnl"] for o in ops), sum(o["coste"] for o in ops)
    pd_ = por_dia(ops)
    top2 = sorted(pd_, key=lambda k: -pd_[k][0])[:2]
    resto = [v for k, v in pd_.items() if k not in top2]
    r_i = np.array([o["pnl"] / o["coste"] for o in ops])
    nt = max(1, math.ceil(0.05 * len(ops)))
    sin_top = sorted(ops, key=lambda o: -o["pnl"])[nt:]
    cst = sum(o["coste"] for o in sin_top)
    out.update({
        "dias_con_operacion": len(pd_), "coste_eur": round(co, 2), "pnl_eur": round(pn, 2), "ev_pond_por_eur": round(pn / co, 4),
        "ev_medio_por_unidad": round(float(r_i.mean()), 4),
        "ic90_por_dias": boot_ratio(list(pd_.values())),
        "ic90_por_cierre": boot_ratio([(o["pnl"], o["coste"]) for o in ops]),
        "ev_sin_2_mejores_dias": (round(sum(v[0] for v in resto) / sum(v[1] for v in resto), 4)
                                  if len(pd_) >= 3 and sum(v[1] for v in resto) > 0 else None),
        "ev_sin_top5pct": round(sum(o["pnl"] for o in sin_top) / cst, 4) if cst > 0 else None, "n_top5pct_quitadas": nt,
        "dias_positivos": sum(1 for v in pd_.values() if v[0] > 0), "acierto": round(float(np.mean([o["gana"] for o in ops])), 3),
        "g_log_f10": round(float(np.mean(np.log1p(0.10 * r_i))), 5),
        "precio_medio": round(float(np.mean([o["precio"] for o in ops])), 4), "peor": round(min(o["pnl"] for o in ops), 3),
        "pct_pnl_mejor_dia": (round(max(v[0] for v in pd_.values()) / pn, 3) if pn > 0 else None),
    })
    return out


def dif_emparejada(A, B, nombre):
    """EV_pond(A) - EV_pond(B) sobre la UNION de cierres; IC90 remuestreando cierres."""
    da, db = {o["cierre"]: o for o in A}, {o["cierre"]: o for o in B}
    cs = sorted(set(da) | set(db))
    if len(cs) < 3:
        return {"comparacion": nombre, "n_cierres": len(cs), "dif": None}
    M = np.array([[da[c]["pnl"] if c in da else 0, da[c]["coste"] if c in da else 0, db[c]["pnl"] if c in db else 0,
                   db[c]["coste"] if c in db else 0] for c in cs], dtype=float)
    est = lambda m: m[:, 0].sum() / max(m[:, 1].sum(), 1e-12) - m[:, 2].sum() / max(m[:, 3].sum(), 1e-12)
    rng = np.random.default_rng(SEED + 1)
    ix = rng.integers(0, len(cs), (NBOOT, len(cs)))
    b = [est(M[i]) for i in ix]
    return {"comparacion": nombre, "n_cierres": len(cs), "dif": round(float(est(M)), 4),
            "ic90_por_cierre": tuple(float(x) for x in np.percentile(b, [5, 95]).round(4)),
            "pnl_dif_eur": round(float(M[:, 0].sum() - M[:, 2].sum()), 2)}


def veredicto(r, incr):
    """Gate/kill PREREGISTRADOS de H59 (k = 0,02). r = resumen del brazo principal; incr = resumen de las operaciones INCREMENTALES
    (llenas con k=0,02 y NO llenas con k=0 en el mismo cierre)."""
    n = r.get("n", 0)
    ic_d = r.get("ic90_por_dias")
    ic_c = r.get("ic90_por_cierre")
    cond = {
        "n>=40": n >= GATE["n"],
        "dias_con_operacion>=10": r.get("dias_con_operacion", 0) >= GATE["dias_con_operacion"],
        "ev_pond>=+0,10": bool(n) and r["ev_pond_por_eur"] >= GATE["ev_pond"],
        "ic90_dias_inf>0": bool(n) and ic_d is not None and ic_d[0] > GATE["ic90_dias_inf"],
        "sin_2_mejores_dias>0": bool(n) and r.get("ev_sin_2_mejores_dias") is not None and r["ev_sin_2_mejores_dias"] > 0,
        "sin_top5pct>0": bool(n) and r.get("ev_sin_top5pct") is not None and r["ev_sin_top5pct"] > 0,
    }
    kill = bool(n) and (
        (n >= KILL["n_ev"] and r["ev_pond_por_eur"] < KILL["ev_pond_lt"])
        or (n >= KILL["ic90_cierre_sup_lt0_n"] and ic_c is not None and ic_c[1] < 0)
        or (incr.get("n", 0) >= KILL["n_incremental"] and incr["ev_pond_por_eur"] < KILL["incremental_ev_lt"]))
    v = "KILLED_REJECTED" if kill else ("GATE_SUPERADO_pasa_a_revision" if all(cond.values()) else "PENDIENTE")
    return {"veredicto": v, "kill_disparado": kill, "condiciones_gate": cond}
