"""Pruebas de coloc_modelo.py con datos SINTÉTICOS (no toca datos reales ni producción).
Ejecutar:  python3 -m pytest -q experimentos/5m_barato/colocacion_17oct/test_coloc_modelo.py
Cubren: primera decisión por unidad, política (mejor k, theta, NaN), IC90 por grupos, cadena completa sobre cachés sintéticas con meta válida,
ausencia de fuga (theta y predicciones OOS no dependen de las etiquetas OOS), idempotencia (misma semilla -> mismo informe) y cobertura baja -> BLOCKED."""
import json
import sys
from pathlib import Path

import numpy as np
import pandas as pd

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import coloc_dataset as C  # noqa: E402
import coloc_modelo as M  # noqa: E402


def dp_sintetico(dia, semilla, n_mkt=500, dec_por_unidad=6, ruido_etq=False):
    rng = np.random.default_rng(semilla)
    filas = []
    X = []
    for im in range(n_mkt):
        fin = 1_700_000_000 + im * 300
        for coin in range(6):
            for lado in (0, 1):
                nd = dec_por_unidad
                for j in range(nd):
                    filas.append((f"m{im}c{coin}", lado, coin, fin, 1_000 * (fin - 250) + 1500 * j, 0))
    n = len(filas)
    mkt = np.array([f[0] for f in filas], dtype="U12")
    d = {"mkt": mkt, "lado_yes": np.array([f[1] for f in filas], np.int8), "coin": np.array([f[2] for f in filas], np.int8),
         "fin_s": np.array([f[3] for f in filas], np.int64), "tq": np.array([f[4] for f in filas], np.int64),
         "tramo": np.zeros(n, np.int16), "completo": np.ones(n, np.int8)}
    Xm = rng.normal(size=(n, C.NF)).astype(np.float32)
    Xm[rng.random(Xm.shape) < 0.05] = np.nan
    sig = np.nan_to_num(Xm[:, C.FI["imb"]])
    d["X"] = Xm
    p = 0.2 + 0.0 * sig
    # el resultado del mercado depende del par (mkt, lado): constante por unidad
    clave = pd.factorize(pd.Series(mkt) + "|" + pd.Series(d["lado_yes"]).astype(str))[0]
    gana_u = rng.random(clave.max() + 1) < 0.2
    d["win"] = gana_u[clave].astype(np.int8)
    for k in C.KS:
        av = np.ones(n, np.int8)
        pr = 1.0 / (1.0 + np.exp(-(sig * 1.5 - 0.5 * k)))          # P(relleno) depende del rasgo imb
        lleno = np.where(rng.random(n) < pr, 5.0, 0.0).astype(np.float32)
        d[f"av{k}"] = av
        d[f"lleno{k}"] = lleno
        d[f"coste{k}"] = (lleno * (0.2 - 0.01 * k)).astype(np.float32)
        d[f"reb{k}"] = (lleno * 0.2 * 0.07 * 0.2 * 0.8).astype(np.float32)
        d[f"tf{k}"] = np.full(n, np.nan, np.float32)
        d[f"nord{k}"] = np.ones(n, np.int16)
        d[f"p0{k}"] = np.full(n, 200 - 10 * k, np.int16)
        d[f"known{k}"] = np.full(n, 1, np.int8)
    return d


def escribe_cache(out, dia, d, cobertura=1.0):
    ruta = out / f"dp_{dia}.npz"
    C.guardar_npz(ruta, d)
    meta = {"dia": dia, "decisiones": int(len(d["mkt"])), "cobertura_des": cobertura, "sha_npz": C.S.sha_fichero(ruta),
            "script_sha": C.sha_codigo(), "params_hash": C.params_hash()}
    (out / f"meta_{dia}.json").write_text(json.dumps(meta))


def monta(tmp_path, dias_desc, dias_oos, cobertura=1.0, semilla=0, permuta_oos=False):
    out = tmp_path
    for i, dia in enumerate(dias_desc + dias_oos):
        d = dp_sintetico(dia, semilla * 100 + i, n_mkt=70)
        if permuta_oos and dia in dias_oos:
            r = np.random.default_rng(99)
            for k in C.KS:                     # se barajan las ETIQUETAS (lleno/coste/win) de OOS, no los rasgos
                o = r.permutation(len(d["mkt"]))
                d[f"lleno{k}"], d[f"coste{k}"] = d[f"lleno{k}"][o], d[f"coste{k}"][o]
            d["win"] = d["win"][r.permutation(len(d["win"]))]
        escribe_cache(out, dia, d, cobertura)
    return out


def test_primeras_por_unidad():
    unit = np.array([0, 0, 0, 1, 1, 2])
    cand = np.array([False, True, True, True, True, False])
    assert M.primeras_por_unidad(unit, cand).tolist() == [1, 3]


def test_politica_mejor_k_y_theta_y_nan():
    unit = np.array([0, 0, 1, 1, 2])
    P = np.array([[0.0, 0.1, np.nan], [0.0, 0.0, 0.5], [np.nan, np.nan, np.nan], [0.2, 0.01, 0.0], [0.0, 0.0, 0.0]])
    E = {"unit": unit}
    f, k = M.politica(E, P, 0.05)
    assert f.tolist() == [0, 3] and k.tolist() == [1, 0]        # unidad 0: primera con >0,05 es la fila 0 (k=1); unidad 1: fila 3 (NaN fila 2 no cuenta)
    f2, _ = M.politica(E, P, 0.3)
    assert f2.tolist() == [1]


def test_ic90_boot_y_dif():
    p = np.array([1.0, 1.0, 1.0, 1.0])
    c = np.array([2.0, 2.0, 2.0, 2.0])
    lo, hi = M.ic90_boot(p, c, np.array([0, 0, 1, 1]))
    assert abs(lo - 0.5) < 1e-9 and abs(hi - 0.5) < 1e-9
    lo, hi = M.ic90_dif(p, c, p * 0.5, c, np.array([0, 1, 2, 3]))
    assert lo > 0
    assert np.isnan(M.ic90_boot(p, c, np.zeros(4))[0])          # un solo grupo: sin IC


def test_cadena_completa_idempotente_y_sin_fuga(tmp_path):
    desc = [f"2026-10-0{d}" for d in (5, 6, 7)]
    oos = ["2026-10-14", "2026-10-15"]
    out1 = monta(tmp_path / "a" if (tmp_path / "a").mkdir() is None else tmp_path / "a", desc, oos, semilla=1)
    args = ["--out", str(out1), "--desc", ",".join(desc), "--oos", ",".join(oos), "--configs", "A_ridge,A_hgb", "--nrep", "5"]
    assert M.main(args) == 0
    j1 = json.loads((out1 / "informe_modelo.json").read_text())
    assert set(j1["configs"]) == {"A_ridge", "A_hgb"}
    assert "ALL" in j1["configs"]["A_hgb"]["oos"]
    # idempotencia: segunda ejecución idéntica
    assert M.main(args) == 0
    j2 = json.loads((out1 / "informe_modelo.json").read_text())
    assert j1["configs"]["A_hgb"]["theta"] == j2["configs"]["A_hgb"]["theta"]
    assert j1["configs"]["A_hgb"]["oos"]["ALL"]["modelo"]["pnl"] == j2["configs"]["A_hgb"]["oos"]["ALL"]["modelo"]["pnl"]
    # sin fuga: mismas características OOS, etiquetas OOS barajadas -> theta idéntico (theta sale de DESC) y mismas unidades elegidas por el modelo
    (tmp_path / "b").mkdir()
    out2 = monta(tmp_path / "b", desc, oos, semilla=1, permuta_oos=True)
    args2 = ["--out", str(out2), "--desc", ",".join(desc), "--oos", ",".join(oos), "--configs", "A_hgb", "--nrep", "5"]
    assert M.main(args2) == 0
    j3 = json.loads((out2 / "informe_modelo.json").read_text())
    assert j1["configs"]["A_hgb"]["theta"] == j3["configs"]["A_hgb"]["theta"]
    assert j1["configs"]["A_hgb"]["oos"]["ALL"]["modelo"]["n_unid"] == j3["configs"]["A_hgb"]["oos"]["ALL"]["modelo"]["n_unid"]


def test_cobertura_baja_bloquea(tmp_path):
    desc = ["2026-10-05", "2026-10-06"]
    oos = ["2026-10-14"]
    monta(tmp_path, desc, oos, cobertura=0.5)
    assert M.main(["--out", str(tmp_path), "--desc", ",".join(desc), "--oos", ",".join(oos), "--configs", "A_ridge", "--nrep", "2"]) == 3


def test_placebo_fuente_causal():
    unit = np.array([0, 0, 0, 0])
    tq = np.array([0, 10_000, 31_000, 62_000])
    src = M.placebo_desplazado({"unit": unit, "tq": tq}, None, 0.0)
    assert src.tolist() == [-1, -1, 0 + 1 - 1, 2] or src.tolist() == [-1, -1, 0, 2]
    assert all(s < i for i, s in enumerate(src) if s >= 0)      # nunca usa una fila futura
