#!/usr/bin/env python3
"""analisis_15m_mineria_mes.py -- minería de alpha del 15m como activo autónomo sobre el dataset del MES
(analisis_15m_dataset_mes.py -> datalogs/m15mes/m15mes_D.csv). 06-Oct, ronda 2 de la misión "15m como activo autónomo".
Gemelo de analisis_15m_mineria.py (ronda 1, registro ms ~20 h), corregido por su lección: un único corte de 20 h quedó
dominado por la dirección del día -> aquí varios días enteros de prueba, IC por días y controles por permutación.

PROTOCOLO (fijado ANTES de mirar resultados; cambiarlo = ronda nueva):
  - DESCUBRIMIENTO = días 16-Sep..28-Sep; EMBARGO = 29-Sep (fuera); PRUEBA = 30-Sep..05-Oct (6 días enteros).
  - Unidad = foto del libro (~45 s por mercado). Señal con signo (+ = comprar YES, - = comprar NO).
  - Umbral = percentil 90 de |señal| en DESCUBRIMIENTO (señales binarias: 0,5); en PRUEBA se aplica tal cual.
  - Una operación como máximo por (mercado, minuto del contrato): la primera foto que supera el umbral.
  - Dos cotas de ejecución SIEMPRE: OPT = ask de la propia foto (latencia 0); PES = ask de la foto SIGUIENTE (~45 s).
    PnL a resolución oficial por € arriesgado, comisión 0,07·p·(1-p); stake fijo (no hay tamaños en las fotos).
    Ida y vuelta: vender al bid de la foto >= t+60 s / >= t+300 s (comisión de tomador en ambas patas).
  - Control negativo: señal PERMUTADA dentro de (día, minuto del contrato, tramo de mid de 0,10) -> conserva la mezcla
    YES/NO y el NIVEL de precio (sin el tramo, el control caía en longshots y regalaba p; visto en la prueba de humo con
    4 permutaciones, antes de la pasada real), rompe la relación señal->mercado. 200 permutaciones. p por hipótesis y p FAMILIAR por
    max-statistic sobre el estadístico estandarizado (EV - media control)/sd control de todas las hipótesis.
  - Dejar una moneda fuera (LOMO): para cada moneda c, umbral calculado en DESCUBRIMIENTO SIN c; se exige EV>0 en
    descubrimiento sin c y se mide la PRUEBA SOLO en c. Se reporta en cuántas monedas se cumple y el EV agregado.
  - SUPERVIVIENTE DEL MES = (a) EV_PES > 0 en descubrimiento y en prueba; (b) EV_OPT > 0 en prueba; (c) p familiar
    (max-stat) < 0,10 con la cota PES (calib.*: señal constante, no permutable -> solo cuenta (d)); (d) IC90 por días (bootstrap de los 6 días) > 0 con PES; (e) EV_PES > 0 sin los
    2 mejores días; (f) LOMO positivo en >= 4 de 6 monedas; (g) ninguna moneda > 60 % del PnL positivo.
  - CRUCE con la ronda 1 ms (+215 ms exacto): solo cuenta una señal que sobreviva aquí Y cuyo equivalente de mecanismo
    en informes/m15_mineria_ms_ronda1_06oct.txt sea > 0 en su PRUEBA y > p95 de su control.
Uso: (ulimit -v 3000000; python3 analisis_15m_mineria_mes.py [--dir datalogs/m15mes] [--perms 200])
"""
import argparse
import glob
import math
import re
from pathlib import Path

import numpy as np
import pandas as pd

FEE = 0.07
DESC = ("2026-09-16", "2026-09-28")
EMBARGO = "2026-09-29"
PRUEBA = ("2026-09-30", "2026-10-05")
RONDA1 = Path(__file__).resolve().parent / "informes" / "m15_mineria_ms_ronda1_06oct.txt"

# mecanismo del mes -> hipótesis equivalentes de la ronda 1 ms (ventanas distintas: el mes tiene fotos de ~45 s)
EQUIV_MS = {
    "flujo.compras_yes_10s": ["flujo.compras_yes_1s", "flujo.compras_yes_5s"],
    "flujo.reversion_10s": ["flujo.reversion_1s", "flujo.reversion_5s"],
    "flujo.compras_yes_60s": ["flujo.compras_yes_30s"], "flujo.reversion_60s": ["flujo.reversion_30s"],
    "flujo.compras_yes_300s": ["flujo.compras_yes_30s"], "flujo.reversion_300s": ["flujo.reversion_30s"],
    "flujo.intensidad_x_dir": ["flujo.intensidad_x_dir"],
    "precio.impulso_45s": ["precio.impulso_5s"], "precio.reversion_45s": ["precio.reversion_5s"],
    "precio.impulso_90s": ["precio.impulso_5s"], "precio.reversion_90s": ["precio.reversion_5s"],
    "fv.misp": ["fv.misp"], "fv.misp_ejecutable": ["fv.misp_ejecutable"], "fv.z": ["fv.z"], "fv.z_inv": ["fv.z_inv"],
    "fv.dist_ref": ["fv.dist_ref"], "fv.valor_ask": ["fv.misp_ejecutable"],
    "chainlink.impulso_30s": ["chainlink.impulso_30s"], "chainlink.reversion_30s": ["chainlink.reversion_30s"],
    "chainlink.impulso_60s": ["chainlink.impulso_30s"], "chainlink.reversion_60s": ["chainlink.reversion_30s"],
    "chainlink.impulso_300s": ["chainlink.impulso_30s"], "chainlink.reversion_300s": ["chainlink.reversion_30s"],
    "chainlink.adelanto_vs_libro": ["chainlink.adelanto_vs_libro"],
    "m5.impulso": ["m5.impulso_5s"], "m5.adelanto": ["m5.adelanto_5s"],
    "expira.fv_tarde": ["expira.fv_tarde"], "expira.impulso_tarde": ["expira.impulso_tarde"],
    "expira.reversion_temprana": ["expira.reversion_temprana"],
    "regimen.fv_vol_alta": ["regimen.fv_vol_alta"], "regimen.fv_vol_baja": ["regimen.fv_vol_baja"],
    "secuencia.cl_mueve_libro_quieto": ["secuencia.cl_mueve_libro_quieto"],
    "micro.suma_asks_baja": ["micro.suma_asks_baja"],
}


def fee(p):
    return FEE * p * (1 - p)


def cargar(d):
    fs = sorted(glob.glob(str(Path(d) / "m15mes_*.csv")))
    df = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
    df = df[(df["bid_y"] <= df["ask_y"]) & (df["bid_n"] <= df["ask_n"])]          # guarda de libro cruzado
    df = df.sort_values(["market", "t"]).reset_index(drop=True)
    w = (df["desenlace"] == "YES").astype(float).values
    df["win_yes"] = w
    for cota, (cy, cn) in {"opt": ("ask_y", "ask_n"), "pes": ("ask_y_sig", "ask_n_sig")}.items():
        aY, aN = df[cy], df[cn]
        okY, okN = (aY > 0) & (aY < 1), (aN > 0) & (aN < 1)
        # por € arriesgado: pnl / (ask + fee) con stake fijo -> se acumula pnl y riesgo por separado
        df[f"p_{cota}_Y"] = np.where(okY, w - aY - fee(aY), np.nan) / np.where(okY, aY, np.nan)
        df[f"r_{cota}_Y"] = np.where(okY, (aY + fee(aY)) / aY, np.nan)
        df[f"p_{cota}_N"] = np.where(okN, (1 - w) - aN - fee(aN), np.nan) / np.where(okN, aN, np.nan)
        df[f"r_{cota}_N"] = np.where(okN, (aN + fee(aN)) / aN, np.nan)
        for H in (60, 300):
            bY, bN = df[f"bid_y_{H}"], df[f"bid_n_{H}"]
            df[f"p_{cota}_rt{H}_Y"] = np.where(okY, bY - aY - fee(aY) - fee(bY), np.nan) / np.where(okY, aY, np.nan)
            df[f"p_{cota}_rt{H}_N"] = np.where(okN, bN - aN - fee(aN) - fee(bN), np.nan) / np.where(okN, aN, np.nan)
    df["min_contrato"] = (df["t_desde_inicio_s"] // 60).astype(int)
    df["clave"] = df["market"].astype(np.int64) * 100 + df["min_contrato"]
    return df


def hipotesis(df):
    """Señales con signo (+ = comprar YES). Mismos mecanismos que la ronda 1 donde el dataset lo permite."""
    H = {}
    g = lambda c: df[c].astype(float)
    for w in (10, 60, 300):
        H[f"flujo.compras_yes_{w}s"] = g(f"flujo_{w}s")
        H[f"flujo.reversion_{w}s"] = -g(f"flujo_{w}s")
    H["flujo.intensidad_x_dir"] = g("ntr_60s") * np.sign(g("vel1").fillna(0))
    H["flujo.desequilibrio_rel_60s"] = g("flujo_60s") / (g("flujo_60s").abs() + 50)
    H["precio.impulso_45s"], H["precio.reversion_45s"] = g("vel1"), -g("vel1")
    H["precio.impulso_90s"], H["precio.reversion_90s"] = g("vel2"), -g("vel2")
    H["precio.aceleracion"] = g("vel1") - (g("vel2") - g("vel1"))
    H["fv.misp"] = g("fv_yes") - g("mid")
    H["fv.misp_ejecutable"] = g("misp_yes") - g("misp_no")
    vy, vn = g("misp_yes"), g("misp_no")
    H["fv.valor_ask"] = np.where(vy >= vn, vy, -vn)                     # Φ(z) - ask del lado con más valor
    H["fv.valor_ask"] = pd.Series(H["fv.valor_ask"], index=df.index).where(np.maximum(vy, vn) > 0)
    H["fv.z"], H["fv.z_inv"] = g("z"), -g("z")
    H["fv.dist_ref"] = g("dist_ref_bps")
    for w in (30, 60, 300):
        H[f"chainlink.impulso_{w}s"] = g(f"cl_ret_{w}s_bps")
        H[f"chainlink.reversion_{w}s"] = -g(f"cl_ret_{w}s_bps")
    H["chainlink.adelanto_vs_libro"] = g("cl_ret_60s_bps") * 1e-4 * 50 - g("vel1")
    H["m5.impulso"] = g("m5_vel")
    H["m5.adelanto"] = g("m5_vel") - g("vel1")
    H["m5.nivel_vs_15"] = g("m5_mid") - g("mid")
    for lo in np.arange(0.0, 1.0, 0.1):
        m = (g("mid") >= lo) & (g("mid") < lo + 0.1)
        H[f"calib.compra_yes_{lo:.1f}"] = pd.Series(1.0, index=df.index).where(m)
        H[f"calib.compra_no_{lo:.1f}"] = pd.Series(-1.0, index=df.index).where(m)
    late, early = g("t_hasta_cierre_s") < 120, g("t_desde_inicio_s") < 180
    H["expira.fv_tarde"] = (g("fv_yes") - g("mid")).where(late)
    H["expira.impulso_tarde"] = g("vel1").where(late)
    H["expira.reversion_temprana"] = (-g("vel1")).where(early)
    H["expira.z_tarde"] = g("z").where(late)
    alta = g("sigma_bps_s") > g("sigma_bps_s").median()
    H["regimen.fv_vol_alta"] = (g("fv_yes") - g("mid")).where(alta)
    H["regimen.fv_vol_baja"] = (g("fv_yes") - g("mid")).where(~alta)
    H["secuencia.cl_mueve_libro_quieto"] = g("cl_ret_60s_bps").where(g("vel1") == 0)
    H["secuencia.flujo_contra_precio"] = g("flujo_60s").where(np.sign(g("flujo_60s")) != np.sign(g("vel1")))
    H["micro.suma_asks_baja"] = -(g("suma_asks") - 1) * np.sign(g("mid") - 0.5 + 1e-9)
    H["micro.spread_ancho_reversion"] = (-g("vel1")).where(g("spread_y") >= 0.03)
    return {k: pd.Series(v, index=df.index).astype(float) for k, v in H.items()}


class Evaluador:
    """Evaluación vectorizada: primera foto por (mercado, minuto) entre las que disparan; agregados por día y moneda."""

    def __init__(self, df):
        self.clave = df["clave"].values
        self.dia_idx, self.dias = pd.factorize(df["dia"])
        self.mon_idx, self.monedas = pd.factorize(df["moneda"])
        self.market = df["market"].values
        self.cols = {}
        for k in ("p_opt", "r_opt", "p_pes", "r_pes", "p_opt_rt60", "p_pes_rt60", "p_opt_rt300", "p_pes_rt300"):
            for lado in ("Y", "N"):
                c = f"{k}_{lado}" if not k.startswith("r_") else f"{k}_{lado}"
                self.cols[(k, lado)] = df[c].values if c in df else None

    def primeras(self, idx):
        if len(idx) == 0:
            return idx
        _, first = np.unique(self.clave[idx], return_index=True)   # idx ya ordenado por (market, t)
        return idx[np.sort(first)]

    def ev(self, s, thr, mask, cota="pes", tgt=""):
        """-> (ev, n, idx_usados, pnl_por_op, riesgo_por_op) para la cota/objetivo."""
        sv = s
        idx = np.flatnonzero(mask & ~np.isnan(sv) & (np.abs(sv) >= thr))
        idx = self.primeras(idx)
        if len(idx) == 0:
            return np.nan, 0, idx, None, None
        yes = sv[idx] > 0
        k = f"p_{cota}{'_' + tgt if tgt else ''}"
        p = np.where(yes, self.cols[(k, "Y")][idx], self.cols[(k, "N")][idx])
        r = np.where(yes, self.cols[(f"r_{cota}", "Y")][idx], self.cols[(f"r_{cota}", "N")][idx])
        ok = ~np.isnan(p) & ~np.isnan(r)
        if not ok.any():
            return np.nan, 0, idx[:0], None, None
        return p[ok].sum() / r[ok].sum(), int(ok.sum()), idx[ok], p[ok], r[ok]


def ic_dias(ev_obj, idx, p, r, rng, B=2000):
    di = ev_obj.dia_idx[idx]
    u = np.unique(di)
    P = np.array([p[di == d].sum() for d in u])
    R = np.array([r[di == d].sum() for d in u])
    evd = P / R
    bs = []
    for _ in range(B):
        k = rng.integers(0, len(u), len(u))
        bs.append(P[k].sum() / R[k].sum())
    orden = np.argsort(-P)
    sin2 = (P.sum() - P[orden[:2]].sum()) / (R.sum() - R[orden[:2]].sum()) if len(u) > 2 else np.nan
    return np.percentile(bs, 5), np.percentile(bs, 95), int((evd > 0).sum()), len(u), sin2


def leer_ronda1():
    out = {}
    if not RONDA1.exists():
        return out
    for ln in RONDA1.read_text().splitlines():
        m = re.match(r"^(\S+)\s+([+-][\d.]+)\s+(\d+)\s+\|\s+([+-][\d.]+)\s+(\d+)\s+(\d+)\s+([+-][\d.]+)\s+([+-][\d.]+)\s+\|"
                     r"\s+([+-][\d.]+)\s+([+-][\d.]+)", ln)
        if m:
            out[m.group(1)] = {"desc": float(m.group(2)), "prueba": float(m.group(4)), "n": int(m.group(5)),
                               "c95": float(m.group(10))}
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default="/root/polymarket-research-datalogs/m15mes")
    ap.add_argument("--perms", type=int, default=200)
    a = ap.parse_args()
    df = cargar(a.dir)
    dia = df["dia"].values
    desc = (dia >= DESC[0]) & (dia <= DESC[1])
    prueba = (dia >= PRUEBA[0]) & (dia <= PRUEBA[1])
    E = Evaluador(df)
    rng = np.random.default_rng(7)
    print(f"filas {len(df)} | mercados {df['market'].nunique()} | DESC {DESC[0]}..{DESC[1]} ({desc.sum()} fotos) | "
          f"embargo {EMBARGO} | PRUEBA {PRUEBA[0]}..{PRUEBA[1]} ({prueba.sum()} fotos)")
    # dirección de cada día de prueba (artefacto de la ronda 1)
    dd = df[prueba].drop_duplicates("market").groupby("dia")["win_yes"].mean()
    print("fracción de mercados que cierran YES por día de PRUEBA: " + " ".join(f"{k[5:]}:{v:.2f}" for k, v in dd.items()))
    for lado, s in (("YES", 1.0), ("NO", -1.0)):
        sv = np.full(len(df), s)
        e_o = E.ev(sv, 0.5, prueba, "opt")[0]
        e_p = E.ev(sv, 0.5, prueba, "pes")[0]
        print(f"línea base comprar SIEMPRE {lado} (1 por mercado-minuto) en PRUEBA: OPT {e_o:+.3f}  PES {e_p:+.3f}")

    H = hipotesis(df)
    # grupos de permutación: (día, minuto del contrato, es_nan)
    # el tramo de precio entra en el grupo: si no, la señal permutada cae en longshots (-50 %/€) y el control regala p
    tramo = np.clip((df["mid"].values * 10).astype(int), 0, 9).astype(str)
    gid = pd.factorize(df["dia"] + "_" + df["min_contrato"].astype(str) + "_" + tramo)[0].astype(np.int64)
    filas = []
    for nombre, s in H.items():
        sv = s.values
        sd = np.abs(sv[desc & ~np.isnan(sv)])
        if len(sd) < 500 or sd.max() == 0:
            continue
        thr = 0.5 if len(np.unique(sd[:5000])) <= 2 else np.quantile(sd, 0.9)
        rd = {c: E.ev(sv, thr, desc, c) for c in ("opt", "pes")}
        rp = {c: E.ev(sv, thr, prueba, c) for c in ("opt", "pes")}
        if rp["pes"][1] < 30:
            continue
        rt = {f"{c}_rt{H_}": E.ev(sv, thr, prueba, c, f"rt{H_}")[0] for c in ("opt", "pes") for H_ in (60, 300)}
        # LOMO
        lomo_ok, lomo_p, lomo_r, lomo_m = 0, 0.0, 0.0, {}
        for mi, mon in enumerate(E.monedas):
            esta = E.mon_idx == mi
            sdm = np.abs(sv[desc & ~esta & ~np.isnan(sv)])
            thm = 0.5 if len(np.unique(sdm[:5000])) <= 2 else np.quantile(sdm, 0.9)
            e_d = E.ev(sv, thm, desc & ~esta, "pes")[0]
            e_t, n_t, _, pp, rr = E.ev(sv, thm, prueba & esta, "pes")
            if n_t:
                lomo_p += pp.sum(); lomo_r += rr.sum()
                lomo_m[mon] = e_t
                lomo_ok += int(e_d > 0 and e_t > 0)
        # por moneda (prueba, PES) y concentración
        _, _, idx, pp, rr = rp["pes"]
        pm = {mon: pp[E.mon_idx[idx] == mi].sum() for mi, mon in enumerate(E.monedas)}
        pos = sum(v for v in pm.values() if v > 0)
        conc = max(pm.values()) / pos if pos > 0 else np.nan
        lo, hi, dpos, nd, sin2 = ic_dias(E, idx, pp, rr, rng)
        filas.append(dict(h=nombre, thr=thr, sv=sv, d_opt=rd["opt"][0], d_pes=rd["pes"][0], n_d=rd["pes"][1],
                          p_opt=rp["opt"][0], p_pes=rp["pes"][0], n_p=rp["pes"][1],
                          merc=len(np.unique(E.market[idx])), **rt, lo=lo, hi=hi, dpos=dpos, nd=nd, sin2=sin2,
                          lomo_ok=lomo_ok, lomo_ev=lomo_p / lomo_r if lomo_r else np.nan, lomo_m=lomo_m, conc=conc,
                          pm={k: pp[E.mon_idx[idx] == i].sum() / rr[E.mon_idx[idx] == i].sum()
                              for i, k in enumerate(E.monedas) if (E.mon_idx[idx] == i).any()}))
    print(f"\nhipótesis evaluadas: {len(filas)} | permutaciones {a.perms} (vectorizadas, dentro de día x minuto del contrato)")
    # permutaciones: matriz [perm, hip] de EV_PES en prueba
    M = np.full((a.perms, len(filas)), np.nan)
    for b in range(a.perms):
        rk = rng.random(len(df))
        for j, f in enumerate(filas):
            sv = f["sv"]
            # nan se quedan en su sitio: permutar solo valores no-nan dentro del grupo
            if "g2" not in f:
                f["g2"] = gid * 2 + ~np.isnan(sv)
                f["o_base"] = np.argsort(f["g2"], kind="stable")
            o_base = f["o_base"]
            o_perm = np.lexsort((rk, f["g2"]))
            sp = np.empty_like(sv)
            sp[o_base] = sv[o_perm]
            M[b, j] = E.ev(sp, f["thr"], prueba, "pes")[0]
        if (b + 1) % 50 == 0:
            print(f"   permutación {b + 1}/{a.perms}", flush=True)
    mu, sd = np.nanmean(M, 0), np.nanstd(M, 0)
    sd[sd == 0] = np.nan
    Z = (M - mu) / sd
    maxZ = np.nanmax(Z, 1)
    for j, f in enumerate(filas):
        f["c_mu"], f["c95"] = mu[j], np.nanpercentile(M[:, j], 95)
        f["p_ind"] = (np.sum(M[:, j] >= f["p_pes"]) + 1) / (a.perms + 1)
        zj = (f["p_pes"] - mu[j]) / sd[j] if sd[j] == sd[j] else np.nan
        f["p_fam"] = (np.sum(maxZ >= zj) + 1) / (a.perms + 1) if zj == zj else np.nan
    r1 = leer_ronda1()
    for f in filas:
        f["sobrevive_mes"] = bool(f["d_pes"] > 0 and f["p_pes"] > 0 and f["p_opt"] > 0 and (f["p_fam"] < 0.10 or f["p_fam"] != f["p_fam"])
                                  and f["lo"] > 0 and f["sin2"] > 0 and f["lomo_ok"] >= 4 and f["conc"] <= 0.60)
        eq = [r1[k] for k in EQUIV_MS.get(f["h"], [f["h"]] if f["h"] in r1 else []) if k in r1]
        f["ms"] = eq
        f["ms_ok"] = bool(eq) and any(e["prueba"] > 0 and e["prueba"] > e["c95"] for e in eq)
    filas.sort(key=lambda f: -(f["p_pes"] if f["p_pes"] == f["p_pes"] else -9))
    print(f"\n{'hipótesis':34} {'DESC opt':>8} {'pes':>7} {'n':>5} | {'PRUEBA opt':>10} {'pes':>7} {'n':>5} {'merc':>5} | "
          f"{'IC90 días (pes)':>17} {'d+':>4} {'sin2':>7} | {'ctl μ':>6} {'p95':>6} {'p_ind':>6} {'p_fam':>6} | "
          f"{'LOMO':>4} {'evL':>6} {'conc':>5} | rt60 opt/pes  rt300 opt/pes | ms ronda1 (prueba/c95)")
    for f in filas:
        ms = " ".join(f"{e['prueba']:+.3f}/{e['c95']:+.3f}" for e in f["ms"]) or "-"
        print(f"{f['h']:34} {f['d_opt']:+8.3f} {f['d_pes']:+7.3f} {f['n_d']:5} | {f['p_opt']:+10.3f} {f['p_pes']:+7.3f} "
              f"{f['n_p']:5} {f['merc']:5} | ({f['lo']:+.3f},{f['hi']:+.3f}) {f['dpos']}/{f['nd']} {f['sin2']:+7.3f} | "
              f"{f['c_mu']:+6.3f} {f['c95']:+6.3f} {f['p_ind']:6.3f} {f['p_fam']:6.3f} | {f['lomo_ok']:>4} "
              f"{f['lomo_ev']:+6.3f} {f['conc']:5.2f} | {f['opt_rt60']:+.3f}/{f['pes_rt60']:+.3f} "
              f"{f['opt_rt300']:+.3f}/{f['pes_rt300']:+.3f} | {ms}")
    esperado = 0.10 * len(filas)
    nfam = sum(f["p_fam"] < 0.10 for f in filas)
    nind = sum(f["p_ind"] < 0.05 for f in filas)
    print(f"\np_ind<0,05: {nind} de {len(filas)} (azar ~{0.05 * len(filas):.1f}) | p_fam<0,10: {nfam}")
    sob = [f for f in filas if f["sobrevive_mes"]]
    print(f"SUPERVIVIENTES DEL MES (criterios a-g): {len(sob)}")
    for f in sob:
        print(f"   {f['h']}: PES desc {f['d_pes']:+.3f} prueba {f['p_pes']:+.3f} (n={f['n_p']}, {f['merc']} mercados) "
              f"OPT {f['p_opt']:+.3f} IC90 ({f['lo']:+.3f},{f['hi']:+.3f}) LOMO {f['lomo_ok']}/6 | por moneda "
              + " ".join(f"{k}:{v:+.2f}" for k, v in sorted(f["pm"].items()))
              + f" | ronda1 ms {'CONFIRMA' if f['ms_ok'] else 'NO confirma' if f['ms'] else 'sin equivalente'}")
    cruce = [f for f in sob if f["ms_ok"]]
    print(f"SUPERVIVIENTES MES + RONDA 1 ms (+215 ms): {len(cruce)} -> " + (", ".join(f["h"] for f in cruce) or "ninguna"))
    # cerca del listón: positivas en ambas cotas y en desc, para el informe
    cerca = [f for f in filas if not f["sobrevive_mes"] and f["d_pes"] > 0 and f["p_pes"] > 0 and f["p_opt"] > 0]
    print(f"\nPositivas DESC y PRUEBA en ambas cotas pero que NO pasan el resto: {len(cerca)}")
    for f in cerca:
        fallos = [n for n, c in (("p_fam", f["p_fam"] < 0.10), ("IC90", f["lo"] > 0), ("sin2", f["sin2"] > 0),
                                 ("LOMO", f["lomo_ok"] >= 4), ("conc", f["conc"] <= 0.60)) if not c]
        print(f"   {f['h']}: PES {f['p_pes']:+.3f} n={f['n_p']} falla {','.join(fallos)}")

    # modelo combinado: entrenado SOLO en descubrimiento, objetivo = pnl/€ PESIMISTA
    try:
        from sklearn.ensemble import HistGradientBoostingRegressor
        excl = {"dia", "moneda", "market", "cierre", "t", "desenlace", "win_yes", "min_contrato", "clave",
                "ask_y_sig", "ask_n_sig", "seg_hasta_sig", "bid_y_60", "bid_n_60", "bid_y_300", "bid_n_300"}
        feats = [c for c in df.columns if c not in excl and not c.startswith(("p_", "r_"))]
        X = df[feats].astype(float)
        for lado, sg in (("Y", 1.0), ("N", -1.0)):
            y = df[f"p_pes_{lado}"] / df[f"r_pes_{lado}"]
            m = desc & y.notna().values
            mdl = HistGradientBoostingRegressor(max_iter=200, learning_rate=0.05, max_leaf_nodes=15,
                                                min_samples_leaf=300, random_state=0)
            mdl.fit(X[m], y[m])
            pr = mdl.predict(X)
            thr = np.quantile(pr[desc], 0.9)
            sv = np.where(pr >= thr, sg, np.nan)
            eo, _, _, _, _ = E.ev(sv, 0.5, prueba, "opt")
            ep, n, idx, pp, rr = E.ev(sv, 0.5, prueba, "pes")
            lo, hi, dpos, nd, sin2 = ic_dias(E, idx, pp, rr, rng) if n else (np.nan,) * 5
            pmn = {k: pp[E.mon_idx[idx] == i].sum() / rr[E.mon_idx[idx] == i].sum()
                   for i, k in enumerate(E.monedas) if n and (E.mon_idx[idx] == i).any()}
            print(f"\nMODELO GBM (solo DESC, objetivo PES) comprar {'YES' if lado == 'Y' else 'NO'} en su decil superior: "
                  f"PRUEBA OPT {eo:+.3f} PES {ep:+.3f} n={n} IC90 días ({lo:+.3f},{hi:+.3f}) {dpos}/{nd} sin2 {sin2:+.3f} | "
                  + " ".join(f"{k}:{v:+.2f}" for k, v in sorted(pmn.items())))
    except Exception as e:  # noqa: BLE001
        print(f"modelo: {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
