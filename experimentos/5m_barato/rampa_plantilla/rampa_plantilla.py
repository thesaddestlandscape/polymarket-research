#!/usr/bin/env python3
"""rampa_plantilla.py -- PLANTILLA reutilizable de rampa de stake por subestrategia (diseno + simulacion, NO envia nada).
Entrada: un spec JSON (ver spec_h55.json) y una tabla de entradas historicas (dia, cierre, precio, gana, profundidad nivel 1).
Salida: tabla_rampa_<tag>.json/.txt con, por peldano: stake, capital inmovilizado, EUR/dia, EUR/ano con IC90 por dias (EV empirico)
y por escenario de EV, dias minimos, P(pasar el gate), P(kill en falso) con K1 (media acumulada) y K2 (perdidas con ask alto),
presupuesto de perdida (P95 del drawdown maximo en 30 dias) y la trayectoria con reinversion de ganancias.
Modelo de capacidad: acciones(S) = min(max(5, S/ask), profundidad nivel 1); si profundidad < 5 acciones no hay orden.
EV por EUR constante con el tamano (SUPUESTO: sin impacto mas alla del nivel 1; hay que medirlo en cada peldano con el gemelo).
Para otra subestrategia: otro spec + otra funcion cargar_*(); el resto no cambia.
Uso: python3 rampa_plantilla.py spec_h55.json [--tag h55]   (nice 19; solo numpy/pandas)"""
import argparse, glob, json, math, sys
from pathlib import Path
import numpy as np
import pandas as pd

FEAT = "/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/"
fee = lambda p: 0.07 * p * (1 - p)


def cargar_descubrimiento_h55():
    """Entradas H55 (F3) del descubrimiento 06-18 Oct (feat_D.csv.gz de sim_dia3): 1 por cierre, ejecutables a +215 ms."""
    F = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(FEAT + "feat_*.csv.gz"))], ignore_index=True).drop_duplicates(["cierre", "t"]).sort_values(["cierre", "t"])
    d = F[(F.ask5 >= .5) & (F.ask5 <= .95) & (F.m >= -.05)].groupby("cierre").head(1)
    out = pd.DataFrame({"dia": d.dia, "cierre": d.cierre, "ask": d.ask_e215, "gana": d.gana.astype(bool), "prof": d.asz5, "ejec": d.acc_e215 > 0})
    return out[out.ejec].reset_index(drop=True), len(d)


def retorno(df):
    p = df.ask.values
    return np.where(df.gana.values, 1 - p - fee(p), -(p + fee(p))) / (p + fee(p))     # por EUR


def acciones(df, S):
    a = np.maximum(5.0, S / df.ask.values)
    a = np.minimum(a, df.prof.values)
    return np.where(a >= 5.0, a, 0.0)


def anual_por_peldano(df, S, ndias_fuente, rng, nb=4000):
    """EUR/ano al stake S con el EV empirico de las entradas (bootstrap por DIAS, incluidos los dias sin entrada)."""
    a = acciones(df, S); p = df.ask.values
    coste = a * (p + fee(p)); pnl = a * (np.where(df.gana.values, 1.0, 0.0) - p - fee(p))
    dias = sorted(df.dia.unique()); idx = {d: i for i, d in enumerate(dias)}
    PC = np.zeros((ndias_fuente, 2))
    for k, d in enumerate(df.dia.values): PC[idx[d]] += (pnl[k], coste[k])
    est = lambda M: (M[:, 0].mean() * 365, M[:, 1].mean())
    ix = rng.integers(0, ndias_fuente, (nb, ndias_fuente))
    b = np.array([PC[i].mean(0) for i in ix]) * np.array([365, 1])
    return {"pnl_ano": est(PC)[0], "pnl_ano_ic90": tuple(np.percentile(b[:, 0], [5, 95])), "coste_dia": est(PC)[1],
            "fill_frac": float((a > 0).mean()), "acc_media": float(a[a > 0].mean()) if (a > 0).any() else 0.0}


def simular(df, ev_t, lam, dias, spec, rng, sims):
    """Monte Carlo de un peldano: entradas ~ Poisson(lam)/dia con retornos por EUR remuestreados y desplazados al EV objetivo
    (SUPUESTO: conserva la varianza). -> P(K1 falso), P(K2 falso), P(gate), P(K1 o K2), drawdown P95 (en unidades de stake)."""
    r0 = retorno(df); perd_alto = (~df.gana.values) & (df.ask.values >= spec["kill"]["K2_perdidas_ask_ge"])
    delta = r0.mean() - ev_t; g = spec["paso_peldano"]; k = spec["kill"]
    K1 = K2 = G = KK = 0; dd = []
    for _ in range(sims):
        n_d = rng.poisson(lam, dias); n = n_d.sum()
        if n == 0: continue
        ix = rng.integers(0, len(r0), n); r = r0[ix] - delta; pa = perd_alto[ix]
        dia_e = np.repeat(np.arange(dias), n_d)
        cm = np.cumsum(r) / np.arange(1, n + 1)
        k1 = bool(((np.arange(1, n + 1) >= k["K1_n"]) & (cm < k["K1_ev_lt"])).any())
        dl = dia_e[pa]; k2 = bool(len(dl) >= k["K2_perdidas"] and (dl[k["K2_perdidas"] - 1:] - dl[:len(dl) - k["K2_perdidas"] + 1] < k["K2_ventana_dias"]).any())
        K1 += k1; K2 += k2; KK += (k1 or k2)
        pd_ = np.bincount(dia_e, weights=r, minlength=dias); top2 = np.argsort(-pd_)[:2]
        sin2 = np.delete(pd_, top2).sum() / max(1, n - np.isin(dia_e, top2).sum())
        cond = (n >= g["n_min"]) and (np.unique(dia_e).size >= g["dias_min"]) and r.mean() >= g["ev_pond_min"] \
            and (r.mean() - 1.645 * r.std(ddof=1) / math.sqrt(n) > 0) and sin2 > 0
        G += cond
        c = np.cumsum(r[dia_e < min(dias, 30)]); dd.append(float((np.maximum.accumulate(np.r_[0, c]) - np.r_[0, c]).max()) if len(c) else 0.0)
    return {"P_K1_falso": K1 / sims, "P_K2_falso": K2 / sims, "P_kill_cualquiera": KK / sims, "P_gate": G / sims, "dd30_P95_en_stakes": float(np.percentile(dd, 95))}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("spec"); ap.add_argument("--tag", default="h55"); a = ap.parse_args()
    spec = json.load(open(a.spec)); rng = np.random.default_rng(spec["semilla"]); sims = spec["sims"]
    df, disparos = cargar_descubrimiento_h55(); nd = spec["dias_fuente"]
    r = retorno(df); ev_emp = float(np.average(r, weights=(df.ask + fee(df.ask)))); lam = len(df) / nd
    # IC90 del EV empirico por cierre
    bs = [np.average(r[i], weights=(df.ask + fee(df.ask)).values[i]) for i in rng.integers(0, len(df), (4000, len(df)))]
    ic = tuple(np.percentile(bs, [5, 95]))
    ev = {k: (ev_emp if k.startswith("A_") else 0.28 * ev_emp if k.startswith("C_") else v) for k, v in spec["ev_escenarios"].items()}
    L = [f"RAMPA {spec['nombre']} -- DISENO/EXPLORATORY (no autoriza dinero)",
         f"fuente: {spec['fuente']} n={len(df)} ejecutables de {disparos} disparos, {nd} dias; entradas/dia={lam:.2f}; EV pond empirico {ev_emp:+.3f} IC90 cierre ({ic[0]:+.3f},{ic[1]:+.3f}); precio medio {df.ask.mean():.3f}; acierto {df.gana.mean():.2f}",
         f"profundidad nivel 1 en la decision (proxy): P10/P50/P90 acciones = {np.percentile(df.prof,[10,50,90]).round(0).tolist()} ; ask>=0,90: {(df.ask>=.9).mean():.2f} de las entradas",
         "Escenarios de EV por EUR: " + ", ".join(f"{k}={v:+.3f}" for k, v in ev.items()), ""]
    filas = []
    for S in spec["peldanos_eur"]:
        an = anual_por_peldano(df, S, nd, rng)
        # entradas/dia efectivas = lam * fill_frac ; capital inmovilizado = coste maximo de UNA entrada (5m, una a la vez por cierre)
        cap = float((acciones(df, S) * (df.ask + fee(df.ask))).max())
        row = {"stake_eur": S, "capital_inmovilizado_eur": round(cap, 2), "fill_frac": round(an["fill_frac"], 2), "coste_dia_eur": round(an["coste_dia"], 2),
               "eur_ano_EV_empirico": round(an["pnl_ano"]), "eur_ano_IC90_dias": [round(x) for x in an["pnl_ano_ic90"]],
               "eur_ano_por_escenario": {k: round(an["coste_dia"] * v * 365) for k, v in ev.items()},
               "dias_min": max(spec["paso_peldano"]["dias_min"], math.ceil(spec["paso_peldano"]["n_min"] / max(1e-9, lam * an["fill_frac"])))}
        filas.append(row)
    sim = {}
    for ek, evv in ev.items():
        sim[ek] = {str(h): simular(df, evv, lam, h, spec, rng, sims) for h in spec["horizontes_dias"]}
    # trayectoria con reinversion (esperada, determinista) por escenario
    tray = {}
    ru = spec["reinversion"]
    for ek, evv in ev.items():
        B, peld, t, hist = ru["capital_inicial_eur"], 0, 0, []
        for dia in range(1, 366):
            S_perm = spec["peldanos_eur"][peld]
            S = max(min(S_perm, ru["f_max_bankroll_por_entrada"] * B), 0.0)
            B += (anual_por_peldano_cache(df, S, nd) * evv) if S > 0 else 0.0
            t += 1
            # solo se sube si el EV de ESE escenario superaria el gate (ev_pond_min); si no, la rampa se queda en el peldano
            if t >= filas[peld]["dias_min"] and evv >= spec["paso_peldano"]["ev_pond_min"] and peld < len(spec["peldanos_eur"]) - 1 and S >= S_perm * 0.999:
                peld += 1; t = 0
            if dia in (30, 90, 180, 365): hist.append((dia, round(B, 1), round(S, 1)))
        tray[ek] = hist
    # stake necesario para el objetivo con cada EV
    obj = spec["objetivo_anual_eur"]; need = {}
    for ek, evv in ev.items():
        mejor = None
        for S in [2, 5, 10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000, 25000]:
            an = anual_por_peldano(df, S, nd, rng, nb=200)
            if an["coste_dia"] * evv * 365 >= obj: mejor = S; break
        techo = max(an2 for an2 in [anual_por_peldano(df, S, nd, rng, nb=200)["coste_dia"] * evv * 365 for S in (25000,)])
        need[ek] = {"stake_para_200k": mejor, "eur_ano_en_techo_profundidad_nivel1": round(techo)}
    out = {"spec": spec, "n": len(df), "lam": lam, "ev": ev, "ev_emp": ev_emp, "ic90": ic, "peldanos": filas, "simulacion": sim, "trayectoria_reinversion": tray, "stake_para_objetivo": need}
    Path(f"tabla_rampa_{a.tag}.json").write_text(json.dumps(out, indent=1, default=float))
    L.append("PELDANOS (EV constante por EUR con el tamano; techo = profundidad nivel 1 del libro en la decision)")
    for f in filas:
        L.append(f"  S={f['stake_eur']:>5} EUR | capital inmovilizado {f['capital_inmovilizado_eur']:>7} | fill {f['fill_frac']:.2f} | coste/dia {f['coste_dia_eur']:>7} | EUR/ano EV emp {f['eur_ano_EV_empirico']:>7} IC90 dias {f['eur_ano_IC90_dias']} | por escenario {f['eur_ano_por_escenario']} | dias min {f['dias_min']}")
    L.append(""); L.append("MONTE CARLO por escenario de EV y horizonte (dias): P(K1 falso), P(K2 falso), P(kill cualquiera), P(pasar gate), drawdown P95 30 d en stakes")
    for ek, d in sim.items():
        for h, s in d.items():
            L.append(f"  {ek:26s} {h:>3} d: K1 {s['P_K1_falso']:.2f} K2 {s['P_K2_falso']:.2f} kill {s['P_kill_cualquiera']:.2f} gate {s['P_gate']:.2f} dd95 {s['dd30_P95_en_stakes']:.1f}")
    L.append(""); L.append("TRAYECTORIA con reinversion (dia, bankroll EUR, stake EUR) desde capital inicial %.1f: " % ru["capital_inicial_eur"])
    for ek, h in tray.items(): L.append(f"  {ek:26s} {h}")
    L.append(""); L.append("STAKE NECESARIO para %d EUR/ano (limite: profundidad nivel 1 en la decision): " % obj + json.dumps(need))
    Path(f"tabla_rampa_{a.tag}.txt").write_text("\n".join(L) + "\n"); print("\n".join(L))


_cache = {}
def anual_por_peldano_cache(df, S, nd):
    """EUR/dia de COSTE esperado a stake S (para la trayectoria)."""
    k = round(S, 2)
    if k not in _cache:
        a = acciones(df, S); _cache[k] = float((a * (df.ask.values + fee(df.ask.values))).sum() / nd)
    return _cache[k]


if __name__ == "__main__":
    main()
