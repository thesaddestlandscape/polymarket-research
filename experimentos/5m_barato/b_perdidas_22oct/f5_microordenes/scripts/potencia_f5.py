#!/usr/bin/env python3
"""Potencia y ruina del ensayo F5 (BTC 5m banda 0,05-0,30, wallet dedicada). Solo cálculo, sin red. Semilla fija.
Modelo: cada FILL cuesta ~size*p (min nocional 1 $ -> ceil(1/p) acc, tope 10), gana (1-p)/p por € con prob q=p*(1+ev) (maker: sin fee, sin rebate),
p ~ U(0,10;0,30). Las posiciones se resuelven por orden (sin solape; el solape por cierre solo AUMENTA la varianza)."""
import json, math, random, sys
SEED = 20261024
def sorteo(rng):
    p = rng.choice([x/100 for x in range(10, 31)])
    s = min(max(5, math.ceil(1.0/p - 1e-9)), 10)
    return p, s, s*p
def resolver(rng, ev, p, s, c):
    return s*(1-p) if rng.random() < min(1.0, p*(1+ev)) else -c
def fill(rng, ev):
    p, s, c = sorteo(rng); return resolver(rng, ev, p, s, c), c
def tanda(rng, ev, n_pujas, fill_rate, presup):
    """Una tanda con suelo: no se envía si perdidas_acumuladas + coste_del_fill > presup (peor caso). Devuelve (pnl, fills, pujas, parada_por_suelo)."""
    pnl = 0.0; fills = 0
    for pujas in range(1, n_pujas + 1):
        if rng.random() > fill_rate: continue
        p, s, c = sorteo(rng)
        if -pnl + c > presup + 1e-9: return pnl, fills, pujas, True
        pnl += resolver(rng, ev, p, s, c); fills += 1
    return pnl, fills, n_pujas, False
def main():
    rng = random.Random(SEED); R = 4000; out = {}
    for ev in (-0.15, -0.06, 0.0, 0.058):
        for presup in (5.0, 10.0):
            for n in (100, 150, 300):
                ruinas = 0; F = []; P = []
                for _ in range(R):
                    pnl, f, pu, r = tanda(rng, ev, n, 0.57, presup); ruinas += r; F.append(f); P.append(pnl)
                F.sort(); P.sort()
                out[f"ev{ev}_presup{presup}_N{n}"] = {"P_suelo_antes_de_N": round(ruinas/R, 3), "fills_mediana": F[R//2], "fills_p10": F[R//10], "fills_p90": F[9*R//10],
                    "pnl_p10": round(P[R//10], 2), "pnl_med": round(P[R//2], 2), "pnl_p90": round(P[9*R//10], 2)}
    # sd de un fill en $ y por €
    xs = []; cs = []
    for _ in range(200000):
        d, c = fill(rng, 0.0); xs.append(d); cs.append(c)
    m = sum(xs)/len(xs); sd = (sum((x-m)**2 for x in xs)/len(xs))**.5
    out["sd_fill_usd_ev0"] = round(sd, 3); out["coste_medio_fill"] = round(sum(cs)/len(cs), 3); out["sd_por_eur"] = round(sd/(sum(cs)/len(cs)), 3)
    # MDE de EV ponderado por € con n fills (80% pot., alfa 5% una cola): (1,645+0,842)*sd_eur/sqrt(n)
    out["mde_ev_por_eur"] = {str(n): round((1.645+0.842)*out["sd_por_eur"]/math.sqrt(n), 3) for n in (50, 100, 200, 1000, 10000, 30000)}
    out["n_fills_para_detectar"] = {str(d): math.ceil(((1.645+0.842)*out["sd_por_eur"]/d)**2) for d in (0.02, 0.05, 0.10)}
    # markout 5 s y 30 s: sd medidos en el ledger real de B (n=177): 0,331 y 0,926 por €
    out["n_fills_markout"] = {k: {str(d): math.ceil(((1.645+0.842)*sd/d)**2) for d in (0.02, 0.05)} for k, sd in (("5s", 0.331), ("30s", 0.926))}
    # AS propio: diferencia de acierto rellenas-no rellenas; MDE con n1 rellenas, n2 no rellenas, aciertos 0,18/0,45 (vpv BTC pes)
    def mde_gap(n1, n2, p1=0.18, p2=0.40):
        se = math.sqrt(p1*(1-p1)/n1 + p2*(1-p2)/n2); return round((1.645+0.842)*se, 3)
    out["mde_gap_acierto_pp"] = {f"{n1}/{n2}": mde_gap(n1, n2) for n1, n2 in ((40, 20), (60, 40), (85, 65), (100, 100))}
    # tasa de relleno: IC95 normal con n pujas
    out["se_tasa_relleno"] = {str(n): round(math.sqrt(.57*.43/n), 3) for n in (60, 100, 150, 300)}
    json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "/dev/stdout", "w"), indent=1)
if __name__ == "__main__":
    main()
