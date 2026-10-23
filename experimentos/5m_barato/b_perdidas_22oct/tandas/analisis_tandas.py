#!/usr/bin/env python3
"""Análisis de pérdidas de B (H47-B real) a nivel cartera/tanda. Reglas fijadas en PREREG.md (sha256 en PREREG.sha256).
Solo lectura: entrada posiciones_snapshot.csv (copia de contabilidad_wallet_dedicada/posiciones.csv), salida resultados.json + stdout.
Uso: nice -n 19 ionice -c3 python3 analisis_tandas.py [--perm 2000] [--sims 2000]"""
import csv
import json
import random
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
SNAP = AQUI / "posiciones_snapshot.csv"
NPERM = int(sys.argv[sys.argv.index("--perm") + 1]) if "--perm" in sys.argv else 2000
NSIM = int(sys.argv[sys.argv.index("--sims") + 1]) if "--sims" in sys.argv else 2000
SEED = 20261022


def ep(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc).timestamp()


def cargar():
    out = []
    with open(SNAP) as f:
        for r in csv.DictReader(f):
            if r["experimento"] != "H47-B" or not r["estado"].startswith("liquidada"):
                continue
            acc = float(r["acciones"])
            out.append(dict(tf=ep(r["fecha_primer_fill_utc"]), fin=ep(r["fin_mercado_utc"]), tanda=int(r["tanda_B"]),
                            coin=r["mercado"].split("-")[0], outcome=r["outcome"], acc=acc, coste=float(r["coste"]),
                            pnl=float(r["pnl_realizado"]), win=r["estado"] == "liquidada_ganada", precio=float(r["coste"]) / acc,
                            mercado=r["mercado"]))
    out.sort(key=lambda p: (p["tf"], p["mercado"]))
    for p in out:
        p["tk"] = p["fin"] + 60
        p["hora"] = datetime.fromtimestamp(p["tf"], timezone.utc).hour
        p["dia"] = datetime.fromtimestamp(p["tf"], timezone.utc).strftime("%Y-%m-%d")
    return out


ATR = ("acc", "coste", "pnl", "win", "precio", "coin", "outcome", "mercado")


# ------------------------------------------------------------------ reglas (devuelven factor por posición: 0 = no se toma, 1 = se toma, otro = escala)
def r0(P):
    return [1.0] * len(P)


def racha(k, pausa=3600):
    def f(P):
        tom, pausa_hasta, reset = [], -1e18, -1e18
        out = []
        for p in P:
            t = p["tf"]
            if t < pausa_hasta:
                out.append(0.0)
                continue
            known = sorted((q for q in tom if reset < q["tk"] <= t), key=lambda q: q["tk"])
            if len(known) >= k and not any(q["win"] for q in known[-k:]):
                fin = known[-1]["tk"] + pausa
                reset = max(fin, known[-1]["tk"])
                if t < fin:
                    pausa_hasta = fin
                    out.append(0.0)
                    continue
            out.append(1.0)
            tom.append(p)
        return out
    return f


def tope_conc(C):
    def f(P):
        tom, out = [], []
        for p in P:
            t = p["tf"]
            abierto = sum(q["coste"] for q in tom if q["tf"] <= t < q["tk"])
            if abierto + p["coste"] > C + 1e-9:
                out.append(0.0)
            else:
                out.append(1.0)
                tom.append(p)
        return out
    return f


def una_por_cierre(P):
    vistos, out = set(), []
    for p in P:
        if p["fin"] in vistos:
            out.append(0.0)
        else:
            vistos.add(p["fin"])
            out.append(1.0)
    return out


def stop_diario(L):
    def f(P):
        tom, parado, out = [], set(), []
        for p in P:
            t, d = p["tf"], p["dia"]
            if d in parado:
                out.append(0.0)
                continue
            pnl_d = sum(q["pnl"] for q in tom if q["tk"] <= t and datetime.fromtimestamp(q["tk"], timezone.utc).strftime("%Y-%m-%d") == d)
            if pnl_d <= -L:
                parado.add(d)
                out.append(0.0)
                continue
            out.append(1.0)
            tom.append(p)
        return out
    return f


def tandas_seguidas(P):
    orden = sorted({p["tanda"] for p in P})
    ini = {T: min(p["tf"] for p in P if p["tanda"] == T) for T in orden}
    tomadas, saltar, racha_neg = {}, set(), 0
    for T in orden:
        t0 = ini[T]
        # resultado conocido (solo posiciones ya resueltas al inicio de T) de las tandas anteriores aún no evaluadas
        if racha_neg >= 2:
            saltar.add(T)
            racha_neg = 0
            continue
        tomadas[T] = True
        # evaluar T al inicio de la siguiente: se hace en el bucle siguiente con conocimiento parcial
        idx = orden.index(T)
        if idx + 1 < len(orden):
            t_sig = ini[orden[idx + 1]]
            res = sum(p["pnl"] for p in P if p["tanda"] == T and p["tk"] <= t_sig)
            racha_neg = racha_neg + 1 if res < 0 else 0
    return [0.0 if p["tanda"] in saltar else 1.0 for p in P]


def wf(clave, nmin=15):
    def f(P):
        out = []
        for p in P:
            t = p["tf"]
            g = [q for q in P if q["tk"] <= t and clave(q) == clave(p)]
            c = sum(q["coste"] for q in g)
            out.append(0.0 if len(g) >= nmin and c > 0 and sum(q["pnl"] for q in g) / c < 0 else 1.0)
        return out
    return f


def tam_min(P):
    return [5.0 / p["acc"] for p in P]


REGLAS = {
    "R0_ACTUAL": r0,
    "R1a_RACHA5": racha(5), "R1b_RACHA8": racha(8),
    "R2a_CONC2": tope_conc(2.0), "R2b_CONC3": tope_conc(3.0),
    "R3_UNA_POR_CIERRE": una_por_cierre,
    "R4a_STOPDIA5": stop_diario(5.0), "R4b_STOPDIA10": stop_diario(10.0),
    "R5_TANDAS_SEGUIDAS": tandas_seguidas,
    "R6a_WF_MONEDA": wf(lambda q: q["coin"]), "R6b_WF_HORA4": wf(lambda q: q["hora"] // 4),
    "R7_TAM_MIN5": tam_min,
}


# ------------------------------------------------------------------ métricas
def curva(P, w):
    ev = sorted(((p["tk"], p["pnl"] * x) for p, x in zip(P, w) if x > 0), key=lambda z: z[0])
    cum, pico, dd = 0.0, 0.0, 0.0
    for _, v in ev:
        cum += v
        pico = max(pico, cum)
        dd = max(dd, pico - cum)
    peor24 = 0.0
    ts = [e[0] for e in ev]
    vs = np.cumsum([0.0] + [e[1] for e in ev])
    j = 0
    for i in range(len(ev)):
        while ts[i] - ts[j] > 86400:
            j += 1
        peor24 = min(peor24, vs[i + 1] - vs[j])
    return dd, peor24


def metricas(P, w):
    pnl = sum(p["pnl"] * x for p, x in zip(P, w))
    coste = sum(p["coste"] * x for p, x in zip(P, w))
    dd, p24 = curva(P, w)
    return dict(n=sum(1 for x in w if x > 0), pnl=round(pnl, 3), coste=round(coste, 2), ev=round(pnl / coste, 4) if coste else None,
                dd=round(dd, 2), peor24h=round(p24, 2))


def delta_por_tanda(P, w):
    d = defaultdict(float)
    for p, x in zip(P, w):
        d[p["tanda"]] += p["pnl"] * (x - 1.0)
    return d


def boot_tandas(d, tandas, rng, B=10000):
    v = np.array([d.get(T, 0.0) for T in tandas])
    idx = rng.integers(0, len(v), size=(B, len(v)))
    s = v[idx].sum(axis=1)
    return float(np.percentile(s, 5)), float(np.percentile(s, 95))


def permutar(P, rng):
    perm = rng.permutation(len(P))
    Q = []
    for i, p in enumerate(P):
        q = dict(p)
        src = P[perm[i]]
        for a in ATR:
            q[a] = src[a]
        Q.append(q)
    return Q


def permutar_cierres(P, rng):
    """POST-HOC (no en PREREG): mantiene la correlación dentro de un cierre y rompe el orden temporal entre cierres.
    Los grupos (mismo fin_mercado) se permutan entre grupos del MISMO tamaño; dentro del grupo, atributos en el mismo orden."""
    grupos = defaultdict(list)
    for i, p in enumerate(P):
        grupos[p["fin"]].append(i)
    por_tam = defaultdict(list)
    for fin, idx in grupos.items():
        por_tam[len(idx)].append(idx)
    Q = [dict(p) for p in P]
    for tam, lista in por_tam.items():
        orden = rng.permutation(len(lista))
        for dst, src_k in zip(lista, orden):
            src = lista[src_k]
            for a_i, b_i in zip(dst, src):
                for a in ATR:
                    Q[a_i][a] = P[b_i][a]
    return Q


def sintetico(P, e, rng):
    Q = []
    for p in P:
        q = dict(p)
        prob = min(0.999, p["precio"] * (1 + e))
        q["win"] = bool(rng.random() < prob)
        q["pnl"] = (p["acc"] if q["win"] else 0.0) - p["coste"]
        Q.append(q)
    return Q


# ------------------------------------------------------------------ perfil por tanda
def perfil(P):
    por = defaultdict(list)
    for p in P:
        por[p["tanda"]].append(p)
    filas = []
    for T in sorted(por):
        g = por[T]
        c = sum(p["coste"] for p in g)
        pnl = sum(p["pnl"] for p in g)
        acc = sum(p["acc"] for p in g)
        conc_max = 0.0
        for p in g:
            conc_max = max(conc_max, sum(q["coste"] for q in g if q["tf"] <= p["tf"] < q["tk"]))
        cierres = defaultdict(int)
        for p in g:
            cierres[p["fin"]] += 1
        monedas = defaultdict(int)
        for p in g:
            monedas[p["coin"]] += 1
        gan = [p["pnl"] for p in g if p["win"]]
        filas.append(dict(tanda=T, n=len(g), coste=round(c, 2), pnl=round(pnl, 2), ganadoras=len(gan), precio_medio=round(c / acc, 3),
                          primer_relleno_gana=g[0]["win"], conc_max=round(conc_max, 2), max_pos_mismo_cierre=max(cierres.values()),
                          frac_pos_en_cierre_compartido=round(sum(v for v in cierres.values() if v > 1) / len(g), 2),
                          monedas=dict(monedas), horas=sorted({p["hora"] for p in g}), duracion_min=round((g[-1]["tk"] - g[0]["tf"]) / 60),
                          mayor_ganancia_share=round(max(gan) / sum(gan), 2) if gan else None, dia=g[0]["dia"]))
    return filas


def resumen_grupo(filas, P, cond):
    Ts = {f["tanda"] for f in filas if cond(f)}
    g = [p for p in P if p["tanda"] in Ts]
    c = sum(p["coste"] for p in g)
    acc = sum(p["acc"] for p in g)
    mon = defaultdict(lambda: [0, 0.0, 0.0])
    for p in g:
        mon[p["coin"]][0] += 1
        mon[p["coin"]][1] += p["coste"]
    hb = defaultdict(int)
    for p in g:
        hb[p["hora"] // 4 * 4] += 1
    fl = [f for f in filas if f["tanda"] in Ts]
    return dict(n_tandas=len(Ts), n_pos=len(g), pos_por_tanda=round(len(g) / max(1, len(Ts)), 1), coste=round(c, 2),
                pnl=round(sum(p["pnl"] for p in g), 2), acierto=round(sum(p["win"] for p in g) / len(g), 3), precio_medio=round(c / acc, 3),
                acierto_esperado_precio=round(sum(p["precio"] for p in g) / len(g), 3),
                primer_relleno_gana=f"{sum(f['primer_relleno_gana'] for f in fl)}/{len(fl)}",
                conc_max_media=round(float(np.mean([f["conc_max"] for f in fl])), 2),
                frac_pos_cierre_compartido=round(float(np.mean([f["frac_pos_en_cierre_compartido"] for f in fl])), 2),
                monedas={k: v[0] for k, v in sorted(mon.items())}, bloques_hora4={k: hb[k] for k in sorted(hb)},
                duracion_min_mediana=float(np.median([f["duracion_min"] for f in fl])))


def racimo_cierre(P, rng, nperm=2000):
    """Concordancia de resultado entre posiciones del MISMO cierre (fin_mercado) frente a permutación de resultados entre posiciones."""
    def estad(wins):
        por = defaultdict(list)
        for p, w in zip(P, wins):
            por[p["fin"]].append(w)
        pares = conc = 0
        todos_pierden = grupos = 0
        for v in por.values():
            if len(v) < 2:
                continue
            grupos += 1
            todos_pierden += not any(v)
            for i in range(len(v)):
                for j in range(i + 1, len(v)):
                    pares += 1
                    conc += v[i] == v[j]
        return pares, conc, grupos, todos_pierden
    w0 = [p["win"] for p in P]
    pares, conc, grupos, tp = estad(w0)
    ge = 0
    sims = []
    for _ in range(nperm):
        w = list(rng.permutation(w0))
        _, c2, _, tp2 = estad(w)
        sims.append(tp2)
        ge += c2 >= conc
    # misma dirección (outcome) dentro del cierre
    por = defaultdict(list)
    for p in P:
        por[p["fin"]].append(p)
    misma = opuesta = 0
    for v in por.values():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                if v[i]["outcome"] == v[j]["outcome"]:
                    misma += 1
                else:
                    opuesta += 1
    return dict(cierres_con_2omas=grupos, pares=pares, concordancia=round(conc / pares, 3) if pares else None, p_perm=round(ge / nperm, 4),
                cierres_todos_pierden=tp, esperado_perm=round(float(np.mean(sims)), 2), pares_mismo_outcome=misma, pares_outcome_opuesto=opuesta,
                pos_en_cierre_compartido=sum(len(v) for v in por.values() if len(v) > 1), n_pos=len(P))


# ------------------------------------------------------------------ proceso de tandas simulado
def sim_tandas(P, e, rng, n_tandas=4000, presupuesto=5.0, margen=1.5, asegurar=6.0, max_pos=300):
    """Reproduce la mecánica de B: presupuesto 5 $; una posición se toma si (5 + PnL conocido − coste abierto) >= su coste; la tanda acaba
    cuando no queda margen (< margen) y no hay abiertas (agotada) o cuando el PnL conocido >= asegurar. Huecos temporales = secuencia real de B en bucle."""
    n = len(P)
    span = P[-1]["tf"] - P[0]["tf"] + 3600
    res = []
    k = 0
    vuelta = 0
    for _ in range(n_tandas):
        tom = []
        cerr, abiertas_prev = 0.0, []
        while True:
            p = P[k % n]
            off = (k // n) * span
            t = p["tf"] + off
            k += 1
            abiertas = [q for q in tom if q["tk"] > t]
            for q in [q for q in abiertas_prev if q["tk"] <= t]:
                cerr += q["pnl"]
            pnl_c = cerr
            abiertas_prev = abiertas
            abierto = sum(q["coste"] for q in abiertas)
            if pnl_c >= asegurar or len(tom) >= max_pos:
                break
            disp = presupuesto + pnl_c - abierto
            if disp < margen and not abiertas:
                break
            if disp >= p["coste"]:
                prob = min(0.999, p["precio"] * (1 + e))
                w = rng.random() < prob
                nq = dict(tk=p["tk"] + off, coste=p["coste"], pnl=(p["acc"] if w else 0.0) - p["coste"])
                tom.append(nq)
                abiertas_prev.append(nq)
        res.append(sum(q["pnl"] for q in tom))
        vuelta += len(tom)
    r = np.array(res)
    return dict(e=e, frac_perdedoras=round(float((r < 0).mean()), 3), media=round(float(r.mean()), 3), mediana=round(float(np.median(r)), 2),
                media_perdedora=round(float(r[r < 0].mean()), 2), media_ganadora=round(float(r[r > 0].mean()), 2) if (r > 0).any() else None,
                frac_le_menos4=round(float((r <= -4).mean()), 3), pos_por_tanda=round(vuelta / n_tandas, 1))


def main():
    rng = np.random.default_rng(SEED)
    random.seed(SEED)
    P = cargar()
    tandas = sorted({p["tanda"] for p in P})
    out = {"n_pos": len(P), "tandas": len(tandas), "periodo": [P[0]["dia"], P[-1]["dia"]]}
    # 1. perfil
    filas = perfil(P)
    out["perfil_tandas"] = filas
    out["perdedoras"] = resumen_grupo(filas, P, lambda f: f["pnl"] < 0)
    out["ganadoras"] = resumen_grupo(filas, P, lambda f: f["pnl"] >= 0)
    out["racimo_cierre"] = racimo_cierre(P, rng)
    # autocorrelación lag-1 del resultado por cierre (PnL/coste del cierre) entre cierres consecutivos, placebo por permutación de cierres
    cier = defaultdict(lambda: [0.0, 0.0])
    for p in P:
        cier[p["fin"]][0] += p["pnl"]
        cier[p["fin"]][1] += p["coste"]
    serie = np.array([cier[k][0] / cier[k][1] for k in sorted(cier)])
    def ac1(x):
        return float(np.corrcoef(x[:-1], x[1:])[0, 1])
    a0 = ac1(serie)
    sims = np.array([ac1(rng.permutation(serie)) for _ in range(5000)])
    gan_c = (serie > 0).astype(float)
    out["autocorr_cierres"] = dict(n_cierres=len(serie), ac1_ev=round(a0, 3), p_perm=round(float((sims >= a0).mean()), 4),
                                   ac1_gana=round(ac1(gan_c), 3), p_perm_gana=round(float(np.mean([ac1(rng.permutation(gan_c)) >= ac1(gan_c) for _ in range(5000)])), 4))
    # pago
    gan = [p for p in P if p["win"]]
    out["pago"] = dict(acierto=round(len(gan) / len(P), 3), precio_medio_pond=round(sum(p["coste"] for p in P) / sum(p["acc"] for p in P), 3),
                       ganancia_media=round(float(np.mean([p["pnl"] for p in gan])), 2),
                       perdida_media=round(float(np.mean([p["pnl"] for p in P if not p["win"]])), 2),
                       ev_pond=round(sum(p["pnl"] for p in P) / sum(p["coste"] for p in P), 4), pnl=round(sum(p["pnl"] for p in P), 2),
                       pnl_sin_2_mejores=round(sum(sorted(p["pnl"] for p in P)[:-2]), 2))
    por_dia = defaultdict(lambda: [0.0, 0.0, 0])
    for p in P:
        por_dia[p["dia"]][0] += p["pnl"]
        por_dia[p["dia"]][1] += p["coste"]
        por_dia[p["dia"]][2] += 1
    out["por_dia"] = {d: dict(pnl=round(v[0], 2), coste=round(v[1], 2), ev=round(v[0] / v[1], 3), n=v[2]) for d, v in sorted(por_dia.items())}
    # 2. reglas
    mitad1 = {T for T in tandas if T <= 12}
    base = metricas(P, r0(P))
    res = {}
    for nom, f in REGLAS.items():
        w = f(P)
        m = metricas(P, w)
        d = delta_por_tanda(P, w)
        m["delta"] = round(m["pnl"] - base["pnl"], 3)
        m["coste_retenido"] = round(m["coste"] / base["coste"], 3)
        m["ic90_delta_tandas"] = [round(x, 2) for x in boot_tandas(d, tandas, rng)]
        m["delta_mitad1"] = round(sum(v for T, v in d.items() if T in mitad1), 2)
        m["delta_mitad2"] = round(sum(v for T, v in d.items() if T not in mitad1), 2)
        m["dd_cambio"] = round(m["dd"] - base["dd"], 2)
        dd_dia = defaultdict(float)
        for p, x in zip(P, w):
            dd_dia[p["dia"]] += p["pnl"] * (x - 1.0)
        m["delta_por_dia"] = {k: round(v, 2) for k, v in sorted(dd_dia.items())}
        m["pnl_quitado_por_tanda"] = {T: round(-v, 2) for T, v in sorted(d.items()) if abs(v) > 1e-9}
        res[nom] = m
    # placebo de secuencia
    for nom, f in REGLAS.items():
        if nom == "R0_ACTUAL":
            continue
        ge = 0
        dds = []
        for _ in range(NPERM):
            Q = permutar(P, rng)
            w = f(Q)
            dq = sum(q["pnl"] * (x - 1) for q, x in zip(Q, w))
            ge += dq >= res[nom]["delta"] - 1e-9
        res[nom]["p_placebo"] = round(ge / NPERM, 4)
        ge2 = 0
        for _ in range(NPERM):
            Q = permutar_cierres(P, rng)
            w = f(Q)
            ge2 += sum(q["pnl"] * (x - 1) for q, x in zip(Q, w)) >= res[nom]["delta"] - 1e-9
        res[nom]["p_placebo_cierres_posthoc"] = round(ge2 / NPERM, 4)
        res[nom]["p_bonf11"] = round(min(1.0, 11 * ge / NPERM), 4)
    # falso disparo con edge sintético
    for nom, f in REGLAS.items():
        if nom == "R0_ACTUAL":
            continue
        res[nom]["sint"] = {}
        for e in (0.10, 0.0, -0.10):
            ds, disp, frac, pnl0 = [], 0, [], []
            for _ in range(NSIM // 4):
                Q = sintetico(P, e, rng)
                w = f(Q)
                dq = sum(q["pnl"] * (x - 1) for q, x in zip(Q, w))
                ds.append(dq)
                pnl0.append(sum(q["pnl"] for q in Q))
                disp += any(x < 1 for x in w)
                cq = sum(q["coste"] for q in Q)
                frac.append(1 - sum(q["coste"] * x for q, x in zip(Q, w)) / cq)
            res[nom]["sint"][f"{e:+.2f}"] = dict(delta_medio=round(float(np.mean(ds)), 2), delta_p5_p95=[round(float(np.percentile(ds, 5)), 2),
                                                 round(float(np.percentile(ds, 95)), 2)], p_dispara=round(disp / len(ds), 3),
                                                 frac_coste_quitado=round(float(np.mean(frac)), 3), pnl_esperado_sin_regla=round(float(np.mean(pnl0)), 2))
    out["reglas"] = res
    # 3. drawdown irreducible
    dd_obs = base["dd"]
    dd = {}
    for e in (0.0, out["pago"]["ev_pond"], 0.10):
        v = [curva(Q, [1.0] * len(Q))[0] for Q in (sintetico(P, e, rng) for _ in range(NSIM))]
        dd[f"iid_e{e:+.3f}"] = dict(mediana=round(float(np.median(v)), 2), p90=round(float(np.percentile(v, 90)), 2),
                                    p_ge_obs=round(float(np.mean(np.array(v) >= dd_obs)), 3))
    v = [curva(Q, [1.0] * len(Q))[0] for Q in (permutar(P, rng) for _ in range(NSIM))]
    dd["permutacion_orden"] = dict(mediana=round(float(np.median(v)), 2), p90=round(float(np.percentile(v, 90)), 2),
                                   p_ge_obs=round(float(np.mean(np.array(v) >= dd_obs)), 3))
    w3 = una_por_cierre(P)
    v = [curva(Q, w3)[0] for Q in (sintetico(P, 0.0, rng) for _ in range(NSIM))]
    dd["iid_e0_R3"] = dict(mediana=round(float(np.median(v)), 2), p90=round(float(np.percentile(v, 90)), 2))
    out["drawdown"] = dict(observado=dd_obs, **dd)
    out["sim_tandas"] = [sim_tandas(P, e, rng) for e in (0.0, out["pago"]["ev_pond"], 0.10)]
    out["sim_tandas_sin_asegurar"] = sim_tandas(P, 0.0, rng, asegurar=1e9)
    (AQUI / "resultados.json").write_text(json.dumps(out, indent=1, ensure_ascii=False, default=str))
    print(json.dumps({k: v for k, v in out.items() if k != "perfil_tandas"}, indent=1, ensure_ascii=False, default=str))


if __name__ == "__main__":
    main()
