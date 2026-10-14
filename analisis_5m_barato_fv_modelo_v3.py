#!/usr/bin/env python3
"""5m barato 4/4b — FV v3: modelar el ERROR del mid del 5m (BTC), no el precio desde cero (14-Oct).

v1/v2 no batían al mid: un modelo global no puede pesar el mid distinto según el tiempo restante y el boosting
desde cero sobreajusta (muchas filas correlacionadas por mercado). v3 parte del mid y solo aprende una corrección:
  - recal_mid_T     : control — logística por tramo de T solo sobre logit(mid5) (¿recalibrar el mid ya mejora?)
  - corr_logit_T    : logística por tramo de T con logit(mid5) + rasgos v1/v2, fuerte regularización (C=0.05)
  - corr_boost_res  : boosting poco profundo sobre el residuo y − mid5 (depth 2, hoja ≥500), p = clip(mid5 + corr)
Filas ponderadas 1/filas del mercado (cada mercado pesa igual, como la métrica por mercado).
Disciplina: selección SOLO en DESC (entrena 05-08, valida 09). OOS 10-13 ya se miró con v1 y v2: este es el 3er
vistazo al mismo OOS -> un "bate" aquí NO basta; el juicio que cuenta es el forward desde 14-Oct.
Reutiliza las cachés y la matriz de analisis_5m_barato_fv_modelo_v2.py (no recalcula rasgos).
Uso: nice -n 19 /usr/bin/python3 analisis_5m_barato_fv_modelo_v3.py
"""
import sys
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analisis_5m_barato_fv_modelo_v2 as V2  # noqa: E402

TRAMOS = ((10, 60), (60, 150), (150, 301))
EPS = 1e-4


def pesos(mk):
    c = Counter(mk)
    return np.array([1.0 / c[m] for m in mk])


def tramo(T):
    out = np.full(len(T), -1)
    for i, (lo, hi) in enumerate(TRAMOS):
        out[(T >= lo) & (T < hi)] = i
    return out


class PorTramo:
    def __init__(self, cols, C):
        self.cols, self.C, self.m = cols, C, {}

    def fit(self, X, y, w):
        from sklearn.linear_model import LogisticRegression
        tr = tramo(X[:, 3])
        Z = X[:, self.cols]
        self.mu, self.sd = np.nanmean(Z, 0), np.nanstd(Z, 0) + 1e-9
        Z = np.nan_to_num((Z - self.mu) / self.sd, nan=0.0)
        for i in range(len(TRAMOS)):
            s = tr == i
            self.m[i] = LogisticRegression(C=self.C, max_iter=3000).fit(Z[s], y[s], sample_weight=w[s] * s.sum() / w[s].sum())
        return self

    def predict(self, X, mid):
        tr = tramo(X[:, 3])
        Z = np.nan_to_num((X[:, self.cols] - self.mu) / self.sd, nan=0.0)
        p = mid.copy()
        for i, mdl in self.m.items():
            s = tr == i
            if s.any():
                p[s] = mdl.predict_proba(Z[s])[:, 1]
        return p


class BoostResiduo:
    def fit(self, X, y, w, mid):
        from sklearn.ensemble import HistGradientBoostingRegressor
        self.m = HistGradientBoostingRegressor(max_depth=2, learning_rate=0.03, max_iter=150, min_samples_leaf=500,
                                               l2_regularization=5.0, random_state=1)
        self.m.fit(X, y - mid, sample_weight=w)
        return self

    def predict(self, X, mid):
        return np.clip(mid + self.m.predict(X), EPS, 1 - EPS)


def ajustar(nom, X, y, w, mid):
    todas = list(range(X.shape[1]))
    if nom == "recal_mid_T":
        return PorTramo([0], C=1.0).fit(X, y, w)
    if nom == "corr_logit_T":
        return PorTramo([c for c in todas if c != 3], C=0.05).fit(X, y, w)
    return BoostResiduo().fit(X, y, w, mid)


def main():
    dias = V2.DIAS
    desc_tr, desc_va, desc, oos = dias[:4], dias[4:5], dias[:5], dias[5:]
    Xtr, ytr, mktr, midtr = V2.matriz(desc_tr)
    Xva, yva, mkva, midva = V2.matriz(desc_va)
    ok = lambda X, mid: np.isfinite(mid) & (mid > 0) & (mid < 1) & np.isfinite(X[:, 3])
    L = ["FV v3 BTC 5m — corrección del ERROR del mid (selección DESC 05-08/09; OOS 10-13 = 3er vistazo, decide el forward)"]
    s_tr, s_va = ok(Xtr, midtr), ok(Xva, midva)
    b_mid = V2.metricas(midva[s_va], yva[s_va], [m for m, k in zip(mkva, s_va) if k])[2]
    L.append(f"  validación 09-Oct: mid5 Brier/mercado {b_mid:.5f}")
    mejor, mejor_b = None, 9.0
    for nom in ("recal_mid_T", "corr_logit_T", "corr_boost_res"):
        mk_tr = [m for m, k in zip(mktr, s_tr) if k]
        mdl = ajustar(nom, Xtr[s_tr], ytr[s_tr], pesos(mk_tr), midtr[s_tr])
        p = mdl.predict(Xva[s_va], midva[s_va])
        b = V2.metricas(p, yva[s_va], [m for m, k in zip(mkva, s_va) if k])[2]
        L.append(f"  validación 09-Oct: {nom:15s} Brier/mercado {b:.5f} ({'MEJOR' if b < b_mid else 'peor'} que mid, Δ {b - b_mid:+.5f})")
        if b < mejor_b:
            mejor, mejor_b = nom, b
    if mejor_b >= b_mid:
        L.append("  NINGUNA candidata bate al mid en validación DESC -> no se juzga en OOS (se conserva el OOS)")
        txt = "\n".join(L)
        print(txt)
        (V2.OUT / "fv3_modelo_informe.txt").write_text(txt + "\n")
        return
    L.append(f"  ELEGIDO (solo con DESC): {mejor}")
    Xd, yd, mkd, midd = V2.matriz(desc)
    Xo, yo, mko, mido = V2.matriz(oos)
    sd_, so = ok(Xd, midd), ok(Xo, mido)
    Xd, yd, midd, mkd = Xd[sd_], yd[sd_], midd[sd_], [m for m, k in zip(mkd, sd_) if k]
    Xo, yo, mido, mko = Xo[so], yo[so], mido[so], [m for m, k in zip(mko, so) if k]
    po = ajustar(mejor, Xd, yd, pesos(mkd), midd).predict(Xo, mido)
    for nom, p in (("mid del 5m", mido), (f"MODELO {mejor}", po)):
        b, l_, bm, lm, nm = V2.metricas(p, yo, mko)
        L.append(f"  OOS {nom:22s} Brier {b:.5f} logloss {l_:.5f} | por mercado Brier {bm:.5f} logloss {lm:.5f} (n={nm})")
    u = {}
    for pm, p5, yy, mm in zip(po, mido, yo, mko):
        s = u.setdefault(mm, [0.0, 0.0, 0])
        s[0] += (pm - yy) ** 2
        s[1] += (p5 - yy) ** 2
        s[2] += 1
    dif = np.array([(v[0] - v[1]) / v[2] for v in u.values()])
    rng = np.random.default_rng(4)
    bs = [rng.choice(dif, len(dif)).mean() for _ in range(3000)]
    L.append(f"  OOS Δ Brier (modelo − mid5) por mercado: {dif.mean():+.5f} IC90 ({np.quantile(bs, .05):+.5f}, "
             f"{np.quantile(bs, .95):+.5f}) -> {'BATE AL MID (3er vistazo: confirmar en forward)' if np.quantile(bs, .95) < 0 else 'NO bate al mid con IC90'}")
    tr = tramo(Xo[:, 3])
    for i, (lo, hi) in enumerate(TRAMOS):
        m = tr == i
        sub = [x for x, k in zip(mko, m) if k]
        b0, b1 = V2.metricas(mido[m], yo[m], sub)[0], V2.metricas(po[m], yo[m], sub)[0]
        L.append(f"  OOS T[{lo},{hi}) Brier mid5 {b0:.5f} vs modelo {b1:.5f} ({'MEJOR' if b1 < b0 else 'peor'})")
    # ¿dónde decide el maker? tramos baratos del lado comprado: mid en [0,10-0,40) o (0,60-0,90]
    bar = ((mido >= 0.10) & (mido < 0.40)) | ((mido > 0.60) & (mido <= 0.90))
    sub = [x for x, k in zip(mko, bar) if k]
    if bar.sum():
        b0, b1 = V2.metricas(mido[bar], yo[bar], sub)[0], V2.metricas(po[bar], yo[bar], sub)[0]
        L.append(f"  OOS banda maker (mid 0,10-0,40 o 0,60-0,90, n filas {int(bar.sum())}): Brier mid5 {b0:.5f} vs modelo {b1:.5f}")
    txt = "\n".join(L)
    print(txt)
    (V2.OUT / "fv3_modelo_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
