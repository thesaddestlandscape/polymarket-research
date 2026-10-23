#!/usr/bin/env python3
"""POST-HOC (declarado): ¿llega B a su gate de 500 pujas con el capital que le queda? y drawdown con correlación por cierre.
Plantilla temporal = secuencia real de rellenos de B (posiciones_snapshot.csv) en bucle; resultados sintéticos con EV e y correlación dentro del cierre
(mezcla: con prob RHO todas las posiciones del cierre comparten un único sorteo; RHO calibrado a la concordancia observada 0,774).
Reglas de capital = las de H47/supervisor: suelo de tanda = saldo − 5; se toma un relleno si caja − coste >= suelo; tanda agotada si caja − suelo < 1,5
y nada abierto; rotación solo si caja >= 17 (ROTACION_SALDO_DURO 12 + 5); opcional «asegurar» (caja >= suelo + 6 -> suelo = caja − 5).
Uso: nice -n 19 python3 ruina.py"""
import json
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import analisis_tandas as A  # noqa: E402

CONC_OBS = 0.774
SALDO0 = 17.116677          # saldo_base de la tanda 24 (ledger, 2026-10-22T14:38:56Z)
PUJAS_HECHAS = 305          # mercados con intencion_post en el ledger a las 14:47Z
FILL_POR_PUJA = 175 / 299   # posiciones liquidadas / pujas hasta el corte del snapshot (aprox.; ver INFORME)
NSIM = 4000


def rho_calibrado(P):
    p = np.mean([q["precio"] for q in P])
    ind = p * p + (1 - p) * (1 - p)
    return max(0.0, (CONC_OBS - ind) / (1 - ind))


def generador(P, e, rho, rng):
    """Devuelve una función slot_index -> (win) con correlación por cierre, regenerada por vuelta."""
    por_cierre = defaultdict(list)
    for i, p in enumerate(P):
        por_cierre[p["fin"]].append(i)

    def vuelta():
        w = np.zeros(len(P), dtype=bool)
        for idx in por_cierre.values():
            if len(idx) > 1 and rng.random() < rho:
                pm = np.mean([P[i]["precio"] for i in idx]) * (1 + e)
                x = rng.random() < pm
                for i in idx:
                    w[i] = x
            else:
                for i in idx:
                    w[i] = rng.random() < P[i]["precio"] * (1 + e)
        return w
    return vuelta


def correr(P, e, rho, rng, asegurar=True, objetivo_pos=None, max_pos=4000):
    gen = generador(P, e, rho, rng)
    n = len(P)
    span = P[-1]["tf"] - P[0]["tf"] + 3600
    caja, suelo = SALDO0, SALDO0 - 5.0
    abiertas = []               # (tk, payout)
    k, tomadas, pnl = 0, 0, 0.0
    w = None
    while tomadas < max_pos:
        if k % n == 0:
            w = gen()
        i_slot = k % n
        p = P[i_slot]
        off = (k // n) * span
        t = p["tf"] + off
        k += 1
        quedan = []
        for tk, pay in abiertas:
            if tk <= t:
                caja += pay
            else:
                quedan.append((tk, pay))
        abiertas = quedan
        if asegurar and not abiertas and caja >= suelo + 6.0:
            suelo = caja - 5.0
        if caja - suelo < 1.5 and not abiertas:
            if caja >= 17.0:
                suelo = caja - 5.0
            else:
                break
        if caja - p["coste"] >= suelo:
            caja -= p["coste"]
            pay = p["acc"] if w[i_slot] else 0.0
            abiertas.append((p["tk"] + off, pay))
            pnl += pay - p["coste"]
            tomadas += 1
            if objetivo_pos and tomadas >= objetivo_pos:
                return tomadas, True, caja + sum(x[1] for x in abiertas)
    return tomadas, False, caja


def dd_corr(P, e, rho, rng, nsim=NSIM, w_regla=None):
    gen = generador(P, e, rho, rng)
    out = []
    for _ in range(nsim):
        w = gen()
        Q = [dict(p, win=bool(x), pnl=(p["acc"] if x else 0.0) - p["coste"]) for p, x in zip(P, w)]
        out.append(A.curva(Q, w_regla or [1.0] * len(Q))[0])
    v = np.array(out)
    return dict(mediana=round(float(np.median(v)), 2), p90=round(float(np.percentile(v, 90)), 2))


def main():
    rng = np.random.default_rng(A.SEED + 7)
    P = A.cargar()
    rho = rho_calibrado(P)
    faltan_pos = int(round((500 - PUJAS_HECHAS) * FILL_POR_PUJA))
    out = dict(rho=round(rho, 3), saldo0=SALDO0, pujas_hechas=PUJAS_HECHAS, fill_por_puja=round(FILL_POR_PUJA, 3), faltan_posiciones=faltan_pos)
    for aseg in (True, False):
        for e in (-0.10, 0.0, 0.10, 0.20):
            r = [correr(P, e, rho, rng, asegurar=aseg, objetivo_pos=faltan_pos) for _ in range(NSIM)]
            pos = np.array([x[0] for x in r])
            out[f"llega500_e{e:+.2f}_asegurar{int(aseg)}"] = dict(p_llega=round(float(np.mean([x[1] for x in r])), 3),
                                                                  pos_mediana_antes_de_parar=float(np.median(pos)),
                                                                  pujas_medianas_totales=round(PUJAS_HECHAS + float(np.median(pos)) / FILL_POR_PUJA))
    # variante «una por cierre» (solo el primer relleno de cada cierre: menos posiciones por puja)
    keep = A.una_por_cierre(P)
    Pk = [p for p, x in zip(P, keep) if x > 0]
    fpp = FILL_POR_PUJA * len(Pk) / len(P)
    fal = int(round((500 - PUJAS_HECHAS) * fpp))
    for e in (0.0, 0.10):
        r = [correr(Pk, e, 0.0, rng, asegurar=True, objetivo_pos=fal) for _ in range(NSIM)]
        out[f"R3_llega500_e{e:+.2f}"] = dict(p_llega=round(float(np.mean([x[1] for x in r])), 3), faltan_posiciones=fal)
    out["dd_corr"] = {f"e{e:+.3f}": dd_corr(P, e, rho, rng) for e in (0.0, -0.012, 0.10)}
    out["dd_corr_R3"] = dd_corr(P, 0.0, rho, rng, w_regla=keep)
    (AQUI / "ruina_resultados.json").write_text(json.dumps(out, indent=1, ensure_ascii=False))
    print(json.dumps(out, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
