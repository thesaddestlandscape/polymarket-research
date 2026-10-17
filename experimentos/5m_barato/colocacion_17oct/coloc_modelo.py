#!/usr/bin/env python3
"""H43 MODELO DE COLOCACION -- entrenamiento, política y evaluación OOS (SOLO LECTURA sobre los dp_D.npz de coloc_dataset.py).

ESPECIFICACION FIJADA ANTES DE MIRAR OOS (17-Oct; cambiarla = versión nueva + OOS nuevo):
 Días     DESC = 05-10 Oct (entrenamiento, elección de umbral por validación cruzada dejando un día fuera), OOS = 14, 15, 16 Oct (juicio único).
          11-13 Oct NO se usan (días del hallazgo de H35). Unidad = (día, mercado, lado, tramo) con mercado completo y desenlace oficial.
 Etiqueta por decisión t_q y profundidad k en {0,1,2} (0 = unirse al top / JOIN; 1,2 = ticks por debajo / DEEP): r = pnl / (5 · precio inicial)
          (pnl con desenlace oficial, 0 si no se rellena; sin rebate; el rebate 0,2·0,07·p(1−p)/acción va aparte y se reporta con y sin).
 Modelos  PRIMARIO = grupo de rasgos A (libro+flujo+Binance+moneda/lado) con HistGradientBoosting poco profundo (depth 3, 80 iter, lr 0,05,
          min_samples_leaf 400, l2 10). SECUNDARIOS declarados: A+Ridge(alpha 300), B (= A + rasgos 15m) +HGB, C (= A + profundidad espejo l) +HGB.
          Un modelo por k. Peso de muestra = 1/(nº de decisiones de su unidad) (cada unidad pesa igual).
 Política "colocar solo si E[r] predicho > theta": en cada unidad, en orden cronológico, se coloca en la PRIMERA decisión en que el mejor
          k disponible (argmax del predicho) supera theta; una orden por unidad; después sigue la vida/repegado de H35. theta numérico UNICO
          (no por moneda), fijado en DESC sobre predicciones fuera de muestra (un día fuera): el cuantil que maximiza EV/€ ponderado por € con
          >= 25 % de las unidades de la línea base colocadas.
 LINEA BASE = colocar SIEMPRE en la primera decisión de la unidad con k fijo (k=0 JOIN, k=1, k=2; coinciden con los motores JOIN/DEEP de H35),
          con rebate (REB = 0,2·0,07 por acción·p(1−p), confirmado en gamma feeSchedule rebateRate 0,2 takerOnly para 5m el 17-Oct) y sin él.
          La comparación principal es contra el MEJOR k de la línea base de cada moneda elegido SOLO en DESC.
 Métricas EV/€ PONDERADO POR € (Σpnl/Σcoste de las pujas rellenas), IC90 por días y por CIERRE (las 6 monedas de un cierre = una apuesta),
          sin los 5 mejores cierres, placebo (rasgos desplazados 30 s), inversión (colocar donde el modelo dice peor, mismo nº), permutación
          dentro del cierre (mismos nº de unidades al azar) y dentro de la unidad (decisión al azar de la misma unidad).
 GATE (por moneda): EV(modelo) − EV(línea base) >= +0,05 €/€ con IC90 por días > 0 (y por cierre > 0), n_rellenas >= 40, placebo e inversión peores.
"""
import argparse
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import coloc_dataset as C  # noqa: E402

S = C.S
OUT = C.OUT
DESC = [f"2026-10-{d:02d}" for d in range(5, 11)]
OOS = ["2026-10-14", "2026-10-15", "2026-10-16"]
KS = C.KS
SEED = 43
THETA_MIN_FRAC = 0.25
REB = S.REB
GRUPOS = {
    "A": C.F_BOOK + C.F_FLOW + C.F_BN + C.F_CAT,
    "B": C.F_BOOK + C.F_FLOW + C.F_BN + C.F_15 + C.F_CAT,
    "C": C.F_BOOK + C.F_FLOW + C.F_BN + C.F_LAD + C.F_CAT,
}
HGB = dict(max_depth=3, max_iter=80, learning_rate=0.05, min_samples_leaf=400, l2_regularization=10.0, random_state=SEED)
RIDGE_ALPHA = 300.0
CONFIGS = {"A_hgb": ("A", "hgb"), "A_ridge": ("A", "ridge"), "B_hgb": ("B", "hgb"), "C_hgb": ("C", "hgb")}
PRIMARIO = "A_hgb"
SUB = 3                                    # entrenamiento: 1 de cada 3 decisiones de cada unidad (muy correlacionadas)


# ---------------------------------------------------------------- carga
def cargar(dias, out=OUT, log=print):
    partes, resumen = [], {}
    for d in dias:
        m = C.cache_valida(out, d)
        if m is None:
            log(f"{d}: sin caché válida de dp (se omite)")
            continue
        z = np.load(out / f"dp_{d}.npz", allow_pickle=False)
        n = len(z["mkt"])
        dd = {k: z[k] for k in z.files}
        dd["dia"] = np.full(n, d)
        partes.append(dd)
        resumen[d] = {"decisiones": n, "cobertura_des": m.get("cobertura_des")}
    if not partes:
        return None, resumen
    D = {k: np.concatenate([p[k] for p in partes]) for k in partes[0]}
    return D, resumen


def preparar(D):
    """Filtra a mercados completos con desenlace oficial, crea unidad, etiquetas por k y orden (unidad, tq). -> DataFrame de índices + arrays."""
    ok = (D["completo"] == 1) & (D["win"] >= 0)
    n0, n1 = len(ok), int(ok.sum())
    idx = np.flatnonzero(ok)
    E = {k: v[idx] for k, v in D.items()}
    key = pd.Series(E["dia"]) + "|" + pd.Series(E["mkt"]).astype(str) + "|" + pd.Series(E["lado_yes"]).astype(str) + "|" + pd.Series(E["tramo"]).astype(str)
    E["unit"] = pd.factorize(key)[0]
    # una unidad (dia, mkt, lado) con varios tramos completos: se conserva el de menor tramo (contado)
    k2 = pd.Series(E["dia"]) + "|" + pd.Series(E["mkt"]).astype(str) + "|" + pd.Series(E["lado_yes"]).astype(str)
    tr_min = pd.Series(E["tramo"]).groupby(k2.values).transform("min").values
    dup = E["tramo"] != tr_min
    ndup = int(dup.sum())
    if ndup:
        keep = ~dup
        E = {k: (v[keep] if hasattr(v, "__len__") and len(v) == len(keep) else v) for k, v in E.items()}
    o = np.lexsort((E["tq"], E["unit"]))
    E = {k: (v[o] if hasattr(v, "__len__") and len(v) == len(o) else v) for k, v in E.items()}
    for k in KS:
        p0 = E[f"p0{k}"].astype(float) / 1000.0
        av = E[f"av{k}"] == 1
        nom = np.where(av, 5.0 * p0, np.nan)
        pnl = E[f"lleno{k}"].astype(float) * E["win"] - E[f"coste{k}"].astype(float)
        E[f"pnl{k}"] = np.where(av, pnl, np.nan)
        E[f"nom{k}"] = nom
        E[f"y{k}"] = pnl / nom
        E[f"rebk{k}"] = E[f"reb{k}"].astype(float)
    E["cierre"] = E["fin_s"]
    info = {"decisiones_total": n0, "tras_filtro_completo_desenlace": n1, "descartadas_tramos_duplicados": ndup}
    return E, info


def pesos(E):
    cnt = np.bincount(E["unit"])
    return 1.0 / cnt[E["unit"]]


# ---------------------------------------------------------------- modelos
def _imput(X, med):
    X = X.copy()
    m = np.isnan(X)
    if m.any():
        X[m] = np.take(med, np.where(m)[1])
    return X


class Mod:
    def __init__(self, tipo):
        self.tipo = tipo

    def fit(self, X, y, w):
        if self.tipo == "hgb":
            from sklearn.ensemble import HistGradientBoostingRegressor
            self.m = HistGradientBoostingRegressor(**HGB)
            self.m.fit(X, y, sample_weight=w)
        else:
            from sklearn.linear_model import Ridge
            self.med = np.nanmedian(X, axis=0)
            self.med = np.where(np.isnan(self.med), 0.0, self.med)
            Xi = _imput(X, self.med)
            self.mu, self.sd = Xi.mean(0), Xi.std(0) + 1e-9
            self.m = Ridge(alpha=RIDGE_ALPHA)
            self.m.fit((Xi - self.mu) / self.sd, y, sample_weight=w)
        return self

    def predict(self, X):
        if self.tipo == "hgb":
            return self.m.predict(X)
        return self.m.predict((_imput(X, self.med) - self.mu) / self.sd)


def columnas(E, grupo):
    ix = [C.FI[n] for n in GRUPOS[grupo]]
    return E["X"][:, ix]


def entrenar_predecir(Etr, Ete, cfg, log=print):
    """Un modelo por k (solo filas con la orden disponible). -> matriz (n_te, 3) de E[r] predicho (NaN si no disponible)."""
    grupo, tipo = CONFIGS[cfg]
    w = pesos(Etr)
    Xtr_all, Xte = columnas(Etr, grupo), columnas(Ete, grupo)
    P = np.full((len(Xte), len(KS)), np.nan)
    sub = (np.arange(len(Xtr_all)) % SUB) == 0
    for j, k in enumerate(KS):
        m = sub & (Etr[f"av{k}"] == 1) & np.isfinite(Etr[f"y{k}"])
        if m.sum() < 500:
            continue
        mod = Mod(tipo).fit(Xtr_all[m], Etr[f"y{k}"][m], w[m])
        av = Ete[f"av{k}"] == 1
        P[av, j] = mod.predict(Xte[av])
    return P


def subconj(E, mask):
    return {k: (v[mask] if hasattr(v, "__len__") and not isinstance(v, str) and len(v) == len(mask) else v) for k, v in E.items()}


# ---------------------------------------------------------------- política y estadística
def primeras_por_unidad(unit, cand):
    """Índice de la primera fila True de cada unidad (E ordenado por unit, tq)."""
    s = pd.Series(cand.astype(int)).groupby(unit).cumsum().values
    return np.flatnonzero(cand & (s == 1))


def politica(E, P, theta):
    """-> (filas elegidas, k elegido). Mejor k disponible por decisión; primera que supera theta."""
    Pn = np.where(np.isnan(P), -np.inf, P)
    kb = Pn.argmax(1)
    best = Pn.max(1)
    cand = best > theta
    f = primeras_por_unidad(E["unit"], cand)
    return f, kb[f]


def linea_base(E, k):
    return primeras_por_unidad(E["unit"], E[f"av{k}"] == 1)


def sel_valores(E, rows, ks):
    """pnl, coste, rebate, lleno por orden elegida (k por fila)."""
    ks = np.asarray(ks)
    pnl = np.zeros(len(rows))
    cos = np.zeros(len(rows))
    reb = np.zeros(len(rows))
    fil = np.zeros(len(rows), bool)
    for k in KS:
        m = ks == k
        if m.any():
            r = rows[m]
            pnl[m] = E[f"pnl{k}"][r]
            cos[m] = E[f"coste{k}"][r]
            reb[m] = E[f"rebk{k}"][r]
            fil[m] = E[f"lleno{k}"][r] > 0
    return pnl, cos, reb, fil


def ic90_boot(v_p, v_c, grp, B=2000, seed=SEED):
    """IC90 de Σp/Σc remuestreando grupos (días o cierres). -> (lo, hi)."""
    g = pd.DataFrame({"p": v_p, "c": v_c, "g": grp}).groupby("g").sum()
    if len(g) < 2:
        return (float("nan"), float("nan"))
    p, c = g.p.values, g.c.values
    rng = np.random.default_rng(seed)
    ix = rng.integers(0, len(g), size=(B, len(g)))
    den = c[ix].sum(1)
    ev = np.where(den > 0, p[ix].sum(1) / np.where(den > 0, den, 1), np.nan)
    return (float(np.nanquantile(ev, .05)), float(np.nanquantile(ev, .95)))


def ic90_dif(pm, cm, pb, cb, grp, B=2000, seed=SEED):
    """IC90 de EV_modelo − EV_base remuestreando grupos (pareado)."""
    g = pd.DataFrame({"pm": pm, "cm": cm, "pb": pb, "cb": cb, "g": grp}).groupby("g").sum()
    if len(g) < 2:
        return (float("nan"), float("nan"))
    rng = np.random.default_rng(seed)
    ix = rng.integers(0, len(g), size=(B, len(g)))
    a, b, c_, d = (g[x].values[ix].sum(1) for x in ("pm", "cm", "pb", "cb"))
    ok = (b > 0) & (d > 0)
    dif = np.where(ok, a / np.where(b > 0, b, 1) - c_ / np.where(d > 0, d, 1), np.nan)
    return (float(np.nanquantile(dif, .05)), float(np.nanquantile(dif, .95)))


def resumen_sel(E, rows, ks, con_rebate=False):
    pnl, cos, reb, fil = sel_valores(E, rows, ks)
    num = pnl + (reb if con_rebate else 0.0)
    r = {"n_unid": int(len(rows)), "n_fill": int(fil.sum()), "coste": float(cos.sum()), "pnl": float(pnl.sum()), "rebate": float(reb.sum())}
    r["ev"] = float(pnl.sum() / cos.sum()) if cos.sum() > 0 else float("nan")
    r["ev_reb"] = float((pnl.sum() + reb.sum()) / cos.sum()) if cos.sum() > 0 else float("nan")
    dias, cier = E["dia"][rows], E["cierre"][rows]
    r["ic90_dias"] = ic90_boot(num, cos, dias)
    r["ic90_cierre"] = ic90_boot(num, cos, cier)
    gc = pd.DataFrame({"p": num, "c": cos, "g": cier}).groupby("g").sum()
    top = gc.p.nlargest(5).index
    rest = gc.drop(index=top)
    r["ev_sin_top5_cierres"] = float(rest.p.sum() / rest.c.sum()) if rest.c.sum() > 0 else float("nan")
    gd = pd.DataFrame({"p": num, "c": cos, "g": dias}).groupby("g").sum()
    r["dias_pos"] = int((gd.p > 0).sum())
    r["n_dias"] = int(len(gd))
    r["ev_dias"] = {k: float(v.p / v.c) if v.c > 0 else float("nan") for k, v in gd.iterrows()}
    return r


def comparar(E, rows_m, k_m, rows_b, k_b, con_rebate=True):
    """Diferencia pareada EV_modelo − EV_base con IC90 por días y cierres (cada uno con sus propias filas)."""
    pm, cm, rm, _ = sel_valores(E, rows_m, k_m)
    pb, cb, rb, _ = sel_valores(E, rows_b, k_b)
    num_m, num_b = pm + (rm if con_rebate else 0), pb + (rb if con_rebate else 0)
    evm = num_m.sum() / cm.sum() if cm.sum() > 0 else float("nan")
    evb = num_b.sum() / cb.sum() if cb.sum() > 0 else float("nan")
    gm = pd.DataFrame({"pm": num_m, "cm": cm, "d": E["dia"][rows_m], "c": E["cierre"][rows_m]})
    gb = pd.DataFrame({"pb": num_b, "cb": cb, "d": E["dia"][rows_b], "c": E["cierre"][rows_b]})
    out = {"ev_modelo": float(evm), "ev_base": float(evb), "dif": float(evm - evb)}
    for nom, col in (("dias", "d"), ("cierre", "c")):
        a = gm.groupby(col)[["pm", "cm"]].sum()
        b = gb.groupby(col)[["pb", "cb"]].sum()
        j = a.join(b, how="outer").fillna(0.0)
        out[f"ic90_dif_{nom}"] = ic90_dif(j.pm.values, j.cm.values, j.pb.values, j.cb.values, np.arange(len(j)))
    return out


# ---------------------------------------------------------------- elección de theta en DESC (un día fuera)
def oof_desc(E, cfg, log=print):
    P = np.full((len(E["unit"]), len(KS)), np.nan)
    dias = sorted(set(E["dia"].tolist()))
    for d in dias:
        te = E["dia"] == d
        tr = ~te
        Etr, Ete = subconj(E, tr), subconj(E, te)
        P[te] = entrenar_predecir(Etr, Ete, cfg, log)
        log(f"  OOF {cfg}: día {d} fuera ({te.sum()} decisiones)")
    return P


def elegir_theta(E, P, log=print):
    base_n = max(len(linea_base(E, k)) for k in KS)
    finite = P[np.isfinite(P)]
    if not len(finite):
        return None, []
    cuant = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95]
    cand = []
    for q in cuant:
        th = float(np.quantile(finite, q))
        f, kk = politica(E, P, th)
        if len(f) < THETA_MIN_FRAC * base_n:
            cand.append((q, th, len(f), float("nan")))
            continue
        pnl, cos, _, _ = sel_valores(E, f, kk)
        ev = pnl.sum() / cos.sum() if cos.sum() > 0 else float("nan")
        cand.append((q, th, len(f), float(ev)))
    ok = [c for c in cand if c[3] == c[3]]
    if not ok:
        return None, cand
    best = max(ok, key=lambda c: c[3])
    return best[1], cand


# ---------------------------------------------------------------- placebos
def placebo_desplazado(E, P_fn_rows, theta, lag_ms=30000):
    """Política con las predicciones de la decisión de la MISMA unidad ~30 s antes (último t <= tq - lag); sin ella no se coloca."""
    unit, tq = E["unit"], E["tq"]
    n = len(unit)
    src = np.full(n, -1, dtype=np.int64)
    ini = np.r_[0, np.flatnonzero(np.diff(unit)) + 1, n]
    for a, b in zip(ini[:-1], ini[1:]):
        t = tq[a:b]
        j = np.searchsorted(t, t - lag_ms, side="right") - 1
        src[a:b] = np.where(j >= 0, a + j, -1)
    return src


def politica_con_fuente(E, P, theta, src):
    Pf = np.where((src >= 0)[:, None], P[np.maximum(src, 0)], np.nan)
    return politica(E, Pf, theta)


def perm_cierre_y_unidad(E, rows_m, k_m, k_base, n_rep=500, seed=SEED):
    """Nulos: (a) mismas cantidades de unidades por cierre elegidas al azar entre las unidades de ese cierre con la línea base (k fijo del
    modelo por orden); (b) la misma unidad con una decisión al azar entre las disponibles. -> (ev_a [n_rep], ev_b [n_rep])."""
    rng = np.random.default_rng(seed)
    unit, cier = E["unit"], E["cierre"]
    # (a) universo: primera decisión disponible de cada unidad con k=k_base
    fb = linea_base(E, k_base)
    cb = cier[fb]
    pnl_b, cos_b, _, _ = sel_valores(E, fb, np.full(len(fb), k_base))
    grp = pd.Series(np.arange(len(fb))).groupby(cb).apply(lambda s: s.values).to_dict()
    cm = pd.Series(cier[rows_m]).value_counts().to_dict()
    evs_a = np.empty(n_rep)
    for r in range(n_rep):
        p = c = 0.0
        for g, n in cm.items():
            ii = grp.get(g)
            if ii is None:
                continue
            take = rng.choice(ii, size=min(n, len(ii)), replace=False)
            p += pnl_b[take].sum()
            c += cos_b[take].sum()
        evs_a[r] = p / c if c > 0 else np.nan
    # (b) misma unidad, decisión al azar con orden disponible
    ini = {}
    n = len(unit)
    bounds = np.r_[0, np.flatnonzero(np.diff(unit)) + 1, n]
    for a, b in zip(bounds[:-1], bounds[1:]):
        ini[unit[a]] = (a, b)
    evs_b = np.empty(n_rep)
    us = unit[rows_m]
    for r in range(n_rep):
        p = c = 0.0
        for u, k in zip(us, k_m):
            a, b = ini[u]
            av = np.flatnonzero(E[f"av{k}"][a:b] == 1)
            if not len(av):
                continue
            i = a + av[rng.integers(0, len(av))]
            p += E[f"pnl{k}"][i]
            c += E[f"coste{k}"][i]
        evs_b[r] = p / c if c > 0 else np.nan
    return evs_a, evs_b


# ---------------------------------------------------------------- informe
def _nm(x):
    x = np.asarray(x, float)
    return float(np.nanmean(x)) if np.isfinite(x).any() else float("nan")


def diagnostico(Ed, Eo, log):
    """Qué es predecible (descriptivo, grupo A, entrenado en DESC, medido en OOS): AUC de P(relleno) y correlación del predicho con r entre las rellenas."""
    from sklearn.ensemble import HistGradientBoostingClassifier
    from sklearn.metrics import roc_auc_score
    ix = [C.FI[n] for n in GRUPOS["A"]]
    w = pesos(Ed)
    sub = (np.arange(len(w)) % SUB) == 0
    res = {}
    for k in KS:
        mtr = sub & (Ed[f"av{k}"] == 1)
        mte = Eo[f"av{k}"] == 1
        if mtr.sum() < 500 or mte.sum() < 100:
            continue
        ytr = (Ed[f"lleno{k}"][mtr] > 0).astype(int)
        yte = (Eo[f"lleno{k}"][mte] > 0).astype(int)
        clf = HistGradientBoostingClassifier(max_depth=3, max_iter=80, learning_rate=0.05, min_samples_leaf=400, l2_regularization=10.0, random_state=SEED)
        clf.fit(Ed["X"][mtr][:, ix], ytr, sample_weight=w[mtr])
        pr = clf.predict_proba(Eo["X"][mte][:, ix])[:, 1]
        auc = float(roc_auc_score(yte, pr)) if 0 < yte.sum() < len(yte) else float("nan")
        res[k] = {"auc_relleno_oos": auc, "tasa_relleno_oos": float(yte.mean())}
        log(f"  diagnóstico k={k}: AUC OOS de P(relleno) {auc:.3f} (tasa de relleno {yte.mean():.3f}; n decisiones {int(mte.sum())})")
    return res


def fmt_r(r):
    if not r or not r.get("n_unid"):
        return "sin órdenes"
    return (f"unid {r['n_unid']:5d} rell {r['n_fill']:5d} | EV/€ {r['ev']:+.4f} (con rebate {r['ev_reb']:+.4f}) | IC90 días ({r['ic90_dias'][0]:+.3f},{r['ic90_dias'][1]:+.3f}) "
            f"cierres ({r['ic90_cierre'][0]:+.3f},{r['ic90_cierre'][1]:+.3f}) | sin top5 cierres {r['ev_sin_top5_cierres']:+.4f} | días+ {r['dias_pos']}/{r['n_dias']} | PnL {r['pnl']:+.2f} $ coste {r['coste']:.1f} $")


def mejor_k_base_desc(E_desc, mask_coin):
    """Mejor k de la línea base (EV/€ con rebate, ponderado por €) elegido SOLO en DESC y para la moneda."""
    best = None
    for k in KS:
        f = linea_base(E_desc, k)
        f = f[mask_coin[f]]
        pnl, cos, reb, _ = sel_valores(E_desc, f, np.full(len(f), k))
        if cos.sum() <= 0:
            continue
        ev = (pnl.sum() + reb.sum()) / cos.sum()
        if best is None or ev > best[1]:
            best = (k, float(ev))
    return best


def bloque(E, P, theta, Eref, etiqueta, dias, primario, nrep, log):
    """Evalúa la política (P, theta) y la línea base sobre E, por moneda y ALL. La línea base usa el mejor k de cada moneda elegido en Eref
    (DESC). -> dict por scope."""
    monedas = C.MONEDAS
    res = {}
    fm_all, km_all = politica(E, P, theta)
    # inversión: colocar donde el modelo predice PEOR, con el mismo nº de unidades que el modelo (búsqueda del umbral por cuantiles)
    Pn = np.where(np.isnan(P), np.inf, P)
    best_low = Pn.min(1)
    cand_low = np.isfinite(best_low)
    mejor = None
    for q in np.linspace(0.01, 0.95, 60):
        thr_inv = np.quantile(best_low[cand_low], q)
        fi_all = primeras_por_unidad(E["unit"], cand_low & (best_low < thr_inv))
        dist = abs(len(fi_all) - len(fm_all))
        if mejor is None or dist < mejor[0]:
            mejor = (dist, fi_all)
    fi_all = mejor[1]
    ki_all = Pn.argmin(1)[fi_all]
    src = placebo_desplazado(E, None, theta)
    fp_all, kp_all = politica_con_fuente(E, P, theta, src)
    for scope in ("ALL",) + tuple(monedas):
        mo_ = np.ones(len(E["unit"]), bool) if scope == "ALL" else (E["coin"] == C.COIN_IDX[scope])
        md_ = np.ones(len(Eref["unit"]), bool) if scope == "ALL" else (Eref["coin"] == C.COIN_IDX[scope])
        kb = mejor_k_base_desc(Eref, md_)
        if kb is None:
            continue
        k0 = kb[0]
        fb = linea_base(E, k0)
        fb = fb[mo_[fb]]
        sel = mo_[fm_all]
        fm, km = fm_all[sel], km_all[sel]
        fi, ki = fi_all[mo_[fi_all]], ki_all[mo_[fi_all]]
        fp, kp = fp_all[mo_[fp_all]], kp_all[mo_[fp_all]]
        rb = resumen_sel(E, fb, np.full(len(fb), k0))
        rm = resumen_sel(E, fm, km)
        cmp_ = comparar(E, fm, km, fb, np.full(len(fb), k0), con_rebate=True)
        cmp_sin = comparar(E, fm, km, fb, np.full(len(fb), k0), con_rebate=False)
        ri, rp = resumen_sel(E, fi, ki), resumen_sel(E, fp, kp)
        if primario and len(fm):
            ea, eb = perm_cierre_y_unidad(E, fm, km, k0, nrep)
        else:
            ea, eb = np.array([np.nan]), np.array([np.nan])
        pa = float(np.nanmean(ea >= rm["ev"])) if rm["ev"] == rm["ev"] and np.isfinite(ea).any() else float("nan")
        pb = float(np.nanmean(eb >= rm["ev"])) if rm["ev"] == rm["ev"] and np.isfinite(eb).any() else float("nan")
        gate = {
            "n_fill>=40": rm["n_fill"] >= 40,
            "dif>=+0,05": cmp_["dif"] >= 0.05,
            "IC90 dif días>0": cmp_["ic90_dif_dias"][0] > 0,
            "IC90 dif cierre>0": cmp_["ic90_dif_cierre"][0] > 0,
            "placebo peor": (rp["ev"] if rp["n_unid"] else -9) < rm["ev"],
            "inversión peor": (ri["ev"] if ri["n_unid"] else -9) < rm["ev"],
        }
        res[scope] = {"k_base": k0, "ev_desc_base": kb[1], "base": rb, "modelo": rm, "cmp": cmp_, "cmp_sin_rebate": cmp_sin, "inversion": ri,
                      "placebo30": rp, "perm_cierre": {"media": _nm(ea), "p": pa}, "perm_unidad": {"media": _nm(eb), "p": pb},
                      "gate": gate, "pasa": all(gate.values()), "ks_elegidos": {int(a_): int(b_) for a_, b_ in zip(*np.unique(km, return_counts=True))}}
        log(f"\n [{scope}] {etiqueta} {','.join(dias)} | línea base: siempre k={k0} (elegido en DESC, EV DESC con rebate {kb[1]:+.3f})")
        log("   base   : " + fmt_r(rb))
        log("   modelo : " + fmt_r(rm) + f" | k elegidos {res[scope]['ks_elegidos']}")
        log(f"   dif modelo−base (con rebate): {cmp_['dif']:+.4f} IC90 días ({cmp_['ic90_dif_dias'][0]:+.3f},{cmp_['ic90_dif_dias'][1]:+.3f}) "
            f"cierres ({cmp_['ic90_dif_cierre'][0]:+.3f},{cmp_['ic90_dif_cierre'][1]:+.3f}) | sin rebate {cmp_sin['dif']:+.4f}")
        log("   inversión: " + fmt_r(ri))
        log("   placebo 30 s: " + fmt_r(rp))
        if primario:
            log(f"   permutación en el cierre: EV medio {_nm(ea):+.4f} (p={pa:.3f}) | en la unidad: {_nm(eb):+.4f} (p={pb:.3f})")
        log("   gate: " + " ".join(f"{k}{'OK' if v else 'NO'}" for k, v in gate.items()) + f" -> {'PASA' if res[scope]['pasa'] else 'NO PASA'}")
    return res


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--desc", default=",".join(DESC))
    ap.add_argument("--oos", default=",".join(OOS))
    ap.add_argument("--configs", default=",".join(CONFIGS))
    ap.add_argument("--nrep", type=int, default=300)
    ap.add_argument("--informe", default="informe_modelo.txt")
    a = ap.parse_args(argv)
    out = Path(a.out)
    L = []

    def log(x):
        print(x, flush=True)
        L.append(x)

    t0 = time.time()
    d_desc = [d for d in a.desc.split(",") if d]
    d_oos = [d for d in a.oos.split(",") if d]
    D1, r1 = cargar(d_desc, out, log)
    D2, r2 = cargar(d_oos, out, log)
    if D1 is None or D2 is None:
        log("BLOCKED: faltan días con caché válida (DESC u OOS)")
        return 3
    Ed, i1 = preparar(D1)
    Eo, i2 = preparar(D2)
    del D1, D2
    log(f"H43 modelo de colocación | DESC {sorted(r1)} OOS {sorted(r2)} | {i1} {i2}")
    log(f"rasgos: {len(C.FEATS)} | grupos { {g: len(v) for g, v in GRUPOS.items()} } | primario {PRIMARIO}")
    res = {"desc": r1, "oos": r2, "info": [i1, i2], "configs": {}}
    for cfg in a.configs.split(","):
        if cfg not in CONFIGS:
            continue
        log(f"\n===== configuración {cfg} {CONFIGS[cfg]} =====")
        Pd = oof_desc(Ed, cfg, log)
        theta, cand = elegir_theta(Ed, Pd, log)
        log("  theta (DESC, fuera de muestra): " + "; ".join(f"q{q:.2f}: θ={th:+.3f} n={n} EV={ev:+.3f}" for q, th, n, ev in cand))
        if theta is None:
            log("  sin theta válido: configuración descartada")
            continue
        log(f"  theta elegido {theta:+.4f}")
        Po = entrenar_predecir(Ed, Eo, cfg, log)
        cres = {"theta": theta, "theta_candidatos": cand}
        log(f"\n--- {cfg}: OOS (juicio único) ---")
        cres["oos"] = bloque(Eo, Po, theta, Ed, "OOS", d_oos, cfg == PRIMARIO, a.nrep, log)
        log(f"\n--- {cfg}: DESC fuera de muestra (un día fuera; theta elegido sobre estos mismos datos: OPTIMISTA, descriptivo) ---")
        cres["desc_oof"] = bloque(Ed, Pd, theta, Ed, "DESC-OOF", d_desc, False, a.nrep, log)
        if cfg == PRIMARIO:
            cres["diagnostico"] = diagnostico(Ed, Eo, log)
        res["configs"][cfg] = cres
    log(f"\nsegundos {time.time() - t0:.0f}")
    (out / a.informe).write_text("\n".join(L) + "\n")
    (out / a.informe.replace(".txt", ".json")).write_text(json.dumps(res, indent=1, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
