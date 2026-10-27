#!/usr/bin/env python3
"""analisis_f5.py -- métricas del ensayo F5 desde el LEDGER (solo lectura, sin red, idempotente). PREREG: ESPECIFICACION.md §3.
Unidad = puja (slug, lado) con al menos una intención de POST. Desenlace OFICIAL = dict slug -> 'YES'|'NO' (lado ganador) aportado por quien llama (gamma closed=true);
sin desenlace = FALTA (se cuenta y se excluye de EV/acierto, nunca se trata como 0). Duplicados de puja_fin (reinicio) -> se queda la ÚLTIMA por (slug, lado).
EV ponderado por € = Σpnl/Σcoste (pnl de maker sin fee; rebate NO incluido, se reporta aparte si se observa). Bootstrap por CIERRE (slug), semilla fija."""
import json
import random
import sys
from pathlib import Path

SEMILLA = 20261024


def leer_ledger(path):
    """Eventos válidos; las líneas ilegibles se CUENTAN (ilegibles), no se ignoran en silencio."""
    ev, mal = [], 0
    for ln in Path(path).read_text().splitlines():
        if not ln.strip():
            continue
        try:
            e = json.loads(ln)
        except ValueError:
            mal += 1
            continue
        if isinstance(e, dict):
            ev.append(e)
        else:
            mal += 1
    return ev, mal


def unidades(eventos, real=True):
    """{(slug, lado): puja_fin} con la última puja_fin de cada unidad; solo de ese modo (real/seco)."""
    out = {}
    for e in eventos:
        if e.get("tipo") == "puja_fin" and not e.get("interrumpida") and bool(e.get("real")) == bool(real) and e.get("slug") and e.get("lado"):   # parcial de salida != cierre
            out[(e["slug"], e["lado"])] = e
    return out


def posicion(pf, ganador):
    """(acc, coste, pnl) de una puja_fin; None si no hay relleno. Relleno = Σ acc de `rellenos` (precio propio de cada relleno)."""
    acc = sum(float(r["acc"]) for r in pf.get("rellenos", []))
    if acc <= 1e-9:
        return None
    coste = sum(float(r["acc"]) * float(r["precio"]) for r in pf["rellenos"])
    pnl = (acc if pf["lado"] == ganador else 0.0) - coste
    return acc, coste, pnl


def _ic(vals, f, rng, B=2000):
    """IC90 bootstrap de f(sub-muestra de clusters). vals = lista de clusters (cada uno lista de tuplas)."""
    if len(vals) < 2:
        return None
    r = []
    for _ in range(B):
        m = [vals[rng.randrange(len(vals))] for _ in vals]
        v = f([x for c in m for x in c])
        if v is not None:
            r.append(v)
    if not r:
        return None
    r.sort()
    return [round(r[int(.05 * (len(r) - 1))], 4), round(r[int(.95 * (len(r) - 1))], 4)]


def metricas(eventos, desenlaces, real=True):
    U = unidades(eventos, real)
    rng = random.Random(SEMILLA)
    n = {"pujas": len(U), "rellenas": 0, "no_rellenas": 0, "sin_desenlace": 0}
    por_cierre = {}                      # slug -> [(rellena, acierto, coste, pnl, mk5*coste, mk30*coste, tiene_mk5, tiene_mk30)]
    tasa = {"pujas": len(U), "rellenas": 0}
    for (slug, lado), pf in U.items():
        pos = posicion(pf, desenlaces.get(slug, "?"))
        rellena = any(float(r["acc"]) > 1e-9 for r in pf.get("rellenos", []))
        tasa["rellenas"] += rellena
        g = desenlaces.get(slug)
        if g not in ("YES", "NO"):
            n["sin_desenlace"] += 1
            continue
        pos = posicion(pf, g)
        acierto = 1.0 if lado == g else 0.0
        if rellena:
            n["rellenas"] += 1
            acc, coste, pnl = pos
            m5 = [r.get("markout_5s") for r in pf["rellenos"]]
            m30 = [r.get("markout_30s") for r in pf["rellenos"]]
            w = [float(r["acc"]) * float(r["precio"]) for r in pf["rellenos"]]
            mk5 = sum(a * b for a, b in zip(m5, w) if a is not None)
            mk30 = sum(a * b for a, b in zip(m30, w) if a is not None)
            c5 = sum(b for a, b in zip(m5, w) if a is not None)
            c30 = sum(b for a, b in zip(m30, w) if a is not None)
            por_cierre.setdefault(slug, []).append((1, acierto, coste, pnl, mk5, mk30, c5, c30))
        else:
            n["no_rellenas"] += 1
            por_cierre.setdefault(slug, []).append((0, acierto, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
    cl = list(por_cierre.values())
    flat = [x for c in cl for x in c]

    def ev(t):
        s = sum(x[2] for x in t if x[0])
        return sum(x[3] for x in t if x[0]) / s if s > 0 else None

    def gap(t):
        a = [x[1] for x in t if x[0]]
        b = [x[1] for x in t if not x[0]]
        return (sum(a) / len(a) - sum(b) / len(b)) if a and b else None

    def mk(i, j):
        def f(t):
            s = sum(x[j] for x in t if x[0])
            return sum(x[i] for x in t if x[0]) / s if s > 0 else None
        return f

    ac_r = [x[1] for x in flat if x[0]]
    ac_n = [x[1] for x in flat if not x[0]]
    out = {"n": n, "cierres": len(cl), "tasa_relleno": round(tasa["rellenas"] / tasa["pujas"], 4) if tasa["pujas"] else None,
           "coste_total": round(sum(x[2] for x in flat), 4), "pnl_total": round(sum(x[3] for x in flat), 4),
           "ev_ponderado_eur": None if ev(flat) is None else round(ev(flat), 4), "ev_ic90_cierres": _ic(cl, ev, rng),
           "acierto_rellenas": round(sum(ac_r) / len(ac_r), 4) if ac_r else None, "acierto_no_rellenas": round(sum(ac_n) / len(ac_n), 4) if ac_n else None,
           "gap_as": None if gap(flat) is None else round(gap(flat), 4), "gap_ic90_cierres": _ic(cl, gap, rng),
           "markout_5s_pond": None if mk(4, 6)(flat) is None else round(mk(4, 6)(flat), 4),
           "markout_30s_pond": None if mk(5, 7)(flat) is None else round(mk(5, 7)(flat), 4)}
    return out


if __name__ == "__main__":
    # uso: analisis_f5.py LEDGER DESENLACES.json   (DESENLACES = {slug: 'YES'|'NO'}, de gamma closed=true; cobertura se imprime)
    ev, mal = leer_ledger(sys.argv[1])
    des = json.loads(Path(sys.argv[2]).read_text())
    r = metricas(ev, des)
    r["lineas_ilegibles"] = mal
    print(json.dumps(r, indent=1))
