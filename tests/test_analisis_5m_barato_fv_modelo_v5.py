"""Pruebas de FV v5 (H34) con registros sintéticos: sin datos reales, sin red. Cubre reproducibilidad del modelo, regresión
de rasgos contra v4, ausencia de look-ahead, gz truncados, orden no cronológico, idempotencia/reanudación, cobertura,
manifiesto, economía del tomador (fee, precios frontera, profundidad, primera entrada cronológica, límite), curva monótona,
guarda de cancelación fail-closed, bloqueo por franja/RAM y juicio sin reentrenar."""
import gzip
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analisis_5m_barato_fv_modelo_v4 as F4  # noqa: E402
import analisis_5m_barato_fv_modelo_v5 as F5  # noqa: E402
import vigia_5m_barato_forward as V  # noqa: E402
from comision_cripto import pnl_por_euro  # noqa: E402

REF = {"BTC": 80000.0, "ETH": 2400.0}


def epoch(dia):
    return int(datetime.fromisoformat(dia + "T00:00:00+00:00").timestamp())


def iso(c):
    return datetime.fromtimestamp(c, timezone.utc).strftime("%Y-%m-%d %H:%M:%S+00:00")


def gen_dia(raiz, dia, n5=6, coins=("BTC",), seed=1, barajar=False, truncar=None, h0=1):
    """Registro sintético de un día: n5 mercados 5m consecutivos desde la hora h0 y sus 15m. Binance cada 200 ms con saltos
    de 3 bps, 5m cada 400 ms (tick 0,01), 15m cada 1 s. Marcas de recepción únicas (sin empates)."""
    rng = np.random.default_rng(seed)
    d0 = epoch(dia)
    cierres = [d0 + h0 * 3600 + 300 * (i + 1) for i in range(n5)]
    c15s = sorted({c + (-c) % 900 for c in cierres})
    k5, k15, q5, q15, xs = [], [], [], [], []
    mids = {}
    for ci, coin in enumerate(coins):
        px = REF[coin]
        t0, t1 = (min(cierres) - 1000) * 1000, max(c15s) * 1000
        for t in range(t0, t1 + 1, 200):
            if rng.random() < 0.01:
                px *= 1 + 3e-4 * (1 if rng.random() < 0.5 else -1)
            px *= 1 + rng.normal(0, 2e-5)
            xs.append(f"x,{t + 30 + ci},{F5.V.SIM[coin]},{px:.4f},0.01,0,{t + 30 + ci},{t + 55 + ci}")
        for i, c in enumerate(cierres):
            mid5 = f"{5000 + 100 * ci + i}"
            mids[(coin, c)] = mid5
            k5.append(f"k,1,t5y_{coin}_{c},{coin},5min,{mid5},{iso(c)},YES")
            k5.append(f"k,1,t5n_{coin}_{c},{coin},5min,{mid5},{iso(c)},NO")
            m = 0.5
            for t in range((c - 305) * 1000, c * 1000 + 1, 400):
                m = float(np.clip(m + rng.choice([-0.01, 0.0, 0.0, 0.01]), 0.1, 0.9))
                b, a = round(m - 0.01, 2), round(m + 0.01, 2)
                q5.append(f"q,{t + 5 + ci},t5y_{coin}_{c},{b},{a},{rng.integers(5, 60)},{rng.integers(5, 60)},{t + 25 + ci}")
        for c15 in c15s:
            k15.append(f"k,1,t15y_{coin}_{c15},{coin},15min,{9000 + 100 * ci + c15 % 977},{iso(c15)},YES")
            m = 0.5
            for t in range((c15 - 905) * 1000, c15 * 1000 + 1, 1000):
                m = float(np.clip(m + rng.choice([-0.01, 0.0, 0.0, 0.0, 0.01]), 0.1, 0.9))
                q15.append(f"q,{t + 7 + ci},t15y_{coin}_{c15},{round(m - 0.01, 2)},{round(m + 0.01, 2)},20,20,{t + 31 + ci}")

    def escribir(pref, ks, cuerpo):
        d = raiz / f"{pref}_registro"
        d.mkdir(parents=True, exist_ok=True)
        cuerpo = list(cuerpo)
        if barajar:
            n = len(cuerpo) // 3
            cuerpo = cuerpo[2 * n:] + cuerpo[:n] + cuerpo[n:2 * n]
        f = d / f"{pref}_registro_{dia}.csv.gz"
        with gzip.open(f, "wt") as fh:
            fh.write("tipo,t_ms,id,c1,c2,c3,c4,c5\n" + "\n".join(ks + cuerpo) + "\n")
        if truncar and pref == "m5":
            raw = f.read_bytes()
            f.write_bytes(raw[:int(len(raw) * truncar)])

    escribir("m15", k15, q15)
    escribir("m5", k5, q5 + xs)
    return {"d0": d0, "cierres": cierres, "mids": mids}


@pytest.fixture
def entorno(tmp_path, monkeypatch):
    reg = tmp_path / "vol"
    out = tmp_path / "out"
    monkeypatch.setattr(F5, "VOL", reg)
    monkeypatch.setattr(F4, "VOL", reg)
    monkeypatch.setattr(F4, "OUT", out / "v4")

    def refs(dias):
        return {c: {} for c in REF}

    estado = {"refs": {}}

    def twap(dias):
        return estado["refs"]

    monkeypatch.setattr(V, "twap_refs", twap)
    des = lambda mids: {m: ("YES" if int(m) % 2 == 0 else "NO") for m in mids}  # noqa: E731
    monkeypatch.setattr(F5, "desenlaces", des)
    monkeypatch.setattr(F4, "desenlaces", des)

    def preparar(dia, **kw):
        info = gen_dia(reg, dia, **kw)
        coins = kw.get("coins", ("BTC",))
        for coin in coins:
            estado["refs"].setdefault(coin, {})
            for c in info["cierres"]:
                estado["refs"][coin][c - 300] = REF[coin] * (1 + 1e-4 * ((c // 300) % 5 - 2))
        return info

    return {"reg": reg, "out": out, "preparar": preparar}


# ---------------------------------------------------------------------------------------------------------------- v4
def test_regresion_rasgos_contra_v4(entorno):
    """Las filas BTC del dataset v5 son idénticas (cadena a cadena) a las del dataset v4 en todas las columnas de v4."""
    entorno["preparar"]("2026-10-10", coins=("BTC", "ETH"))
    c5, m5 = F5.construir_dia("2026-10-10", ("BTC", "ETH"), entorno["out"])
    c4 = F4.dataset_dia("2026-10-10")
    with gzip.open(c4, "rt") as fh:
        l4 = fh.read().splitlines()
    with gzip.open(c5, "rt") as fh:
        l5 = fh.read().splitlines()
    assert l5[0].split(",") == F5.COLS and l4[0].split(",") == F4.COLS
    n4 = len(F4.COLS)
    btc = [ln for ln in l5[1:] if ln.split(",")[len(F4.COLS)] == "BTC" or ln.split(",")[n4 + 0] == "BTC"]
    assert len(btc) == len(l4) - 1 > 1000
    for a, b in zip(l4[1:], btc):
        assert a == ",".join(b.split(",")[:n4])
    assert m5["cobertura"]["ETH"]["filas"] > 1000 and m5["cobertura"]["BTC"]["filas"] == len(btc)


def test_extras_coherentes(entorno):
    entorno["preparar"]("2026-10-10")
    import pandas as pd
    c, m = F5.construir_dia("2026-10-10", ("BTC",), entorno["out"])
    df = pd.read_csv(c)
    ctx = F5.contexto_dia("2026-10-10", ("BTC",))
    r = df[df["m5_355"].notna() & df["m5_70"].notna()].iloc[7]
    L5, L15, r5, mkt = F5.mercado_de(ctx, "BTC", int(r["cierre"]))
    assert F4._top(L5, int(r["t"]) + 355)[0] == pytest.approx(r["m5_355"])
    assert F4._top(L5, int(r["t"]) + 70)[0] == pytest.approx(r["m5_70"])
    assert (r["ask5_lat"] + r["bid5_lat"]) / 2 == pytest.approx(r["m5_355"])
    assert F4._top(L5, int(r["t"]) + 355)[4] == pytest.approx(r["asz_lat"])
    assert r["moneda"] == "BTC"


def test_sin_look_ahead(entorno):
    """Los rasgos en t no cambian si se estropea todo lo recibido DESPUÉS de t."""
    entorno["preparar"]("2026-10-10", n5=2)
    ctxA = F5.contexto_dia("2026-10-10", ("BTC",))
    cie = int(sorted(c for (_, c) in ctxA["por"] if _ == "BTC")[0])
    cie5 = [c for (co, c), v in ctxA["por"].items() if "5min" in v][0]
    t = (cie5 - 150) * 1000
    # versión B: cualquier fila con recepción > t se sustituye por basura
    for pref in ("m15", "m5"):
        f = entorno["reg"] / f"{pref}_registro" / f"{pref}_registro_2026-10-10.csv.gz"
        with gzip.open(f, "rt") as fh:
            lines = fh.read().splitlines()
        nuevo = []
        for ln in lines:
            c = ln.split(",")
            if c[0] in ("q", "x") and int(c[7]) > t:
                if c[0] == "q":
                    c[3], c[4] = "0.97", "0.98"
                else:
                    c[3] = "123456.0"
                ln = ",".join(c)
            nuevo.append(ln)
        with gzip.open(f, "wt") as fh:
            fh.write("\n".join(nuevo) + "\n")
    ctxB = F5.contexto_dia("2026-10-10", ("BTC",))
    for ctx in (ctxA, ctxB):
        pass
    mkA, mkB = F5.mercado_de(ctxA, "BTC", cie5), F5.mercado_de(ctxB, "BTC", cie5)
    ra = F5.rasgos_punto(*ctxA["bx"]["BTC"], mkA[0], mkA[1], mkA[2], cie5, t)
    rb = F5.rasgos_punto(*ctxB["bx"]["BTC"], mkB[0], mkB[1], mkB[2], cie5, t)
    assert ra is not None and ra == rb
    # y sí cambian si se mira DESPUÉS
    rc = F5.rasgos_punto(*ctxB["bx"]["BTC"], mkB[0], mkB[1], mkB[2], cie5, t + 100_000)
    assert rc is None or rc != F5.rasgos_punto(*ctxA["bx"]["BTC"], mkA[0], mkA[1], mkA[2], cie5, t + 100_000)


def test_gz_truncado_no_se_silencia(entorno):
    entorno["preparar"]("2026-10-10", truncar=0.6)
    r = F5.leer_registro("2026-10-10", ("BTC",))
    assert r[3]["truncado"] is True and "m5" in r[3]["archivos"] and r[3]["archivos"]["m5"]["lineas_leidas"] > 0
    c, m = F5.construir_dia("2026-10-10", ("BTC",), entorno["out"])
    assert m["truncado"] is True and m["estado"] == "PARTIAL" and m["archivos_truncados"]
    info = []
    assert F5.cargar(["2026-10-10"], entorno["out"], ("BTC",), info=info) is None       # excluido por defecto
    assert info[0]["excluido"] == "gz truncado"
    df = F5.cargar(["2026-10-10"], entorno["out"], ("BTC",), incluir_truncados=True)
    assert df is not None


def test_tramos_no_cronologicos_dan_el_mismo_dataset(entorno, tmp_path):
    entorno["preparar"]("2026-10-10", barajar=False)
    c1, _ = F5.construir_dia("2026-10-10", ("BTC",), entorno["out"] / "a")
    entorno["preparar"]("2026-10-10", barajar=True)
    c2, _ = F5.construir_dia("2026-10-10", ("BTC",), entorno["out"] / "b")
    a = gzip.open(c1, "rt").read().splitlines()
    b = gzip.open(c2, "rt").read().splitlines()
    assert sorted(a) == sorted(b) and len(a) > 1000


def test_idempotencia_y_reanudacion(entorno):
    entorno["preparar"]("2026-10-10")
    c, m = F5.construir_dia("2026-10-10", ("BTC",), entorno["out"])
    mt = c.stat().st_mtime_ns
    sha = m["sha256"]
    c2, m2 = F5.construir_dia("2026-10-10", ("BTC",), entorno["out"])          # reanudar: caché, no recalcula
    assert c2.stat().st_mtime_ns == mt and m2["sha256"] == sha
    c3, m3 = F5.construir_dia("2026-10-10", ("BTC",), entorno["out"], rehacer=True)   # recalcular: mismos bytes lógicos
    assert gzip.open(c3, "rt").read() == gzip.open(c, "rt").read()
    # un .tmp huérfano (caída a mitad) no se confunde con caché válida
    (entorno["out"] / "fv5_dataset_2026-10-11.csv.gz.tmp").write_bytes(b"basura")
    entorno["preparar"]("2026-10-11")
    c4, m4 = F5.construir_dia("2026-10-11", ("BTC",), entorno["out"])
    assert m4["filas"] > 0 and gzip.open(c4, "rt").read().count("\n") == m4["filas"] + 1


def test_cobertura_ausentes_y_manifiesto(entorno):
    entorno["preparar"]("2026-10-10")
    rc = F5.main(["dataset", "--dias", "2026-10-10,2026-10-09", "--monedas", "BTC", "--out", str(entorno["out"]), "--sin-guardas"])
    assert rc == 0
    man = json.loads(next((entorno["out"] / "fv5_runs").glob("*/run_manifest.json")).read_text())
    assert man["estado"] == "PARTIAL"                      # 09 ausente: nunca COMPLETE
    assert man["dias_ausentes"] == ["2026-10-09"]
    assert man["dias_parciales"] == ["2026-10-10"]         # 6 mercados de 288: cobertura baja se declara
    assert man["script_sha256"] and man["entradas"]["m5_2026-10-10"]["bytes"] > 0 and man["fin_utc"]
    m = json.loads((entorno["out"] / "fv5_dataset_2026-10-10.meta.json").read_text())
    assert m["cobertura"]["BTC"]["mercados_con_filas"] == 6 and m["monedas_cobertura_baja"] == ["BTC"]


def test_desenlace_ausente_se_cuenta_no_se_inventa(entorno, monkeypatch):
    entorno["preparar"]("2026-10-10")
    monkeypatch.setattr(F5, "desenlaces", lambda mids: {m: "YES" for m in sorted(mids)[:3]})
    c, m = F5.construir_dia("2026-10-10", ("BTC",), entorno["out"])
    assert m["cobertura"]["BTC"]["sin_desenlace"] == 3 and m["cobertura"]["BTC"]["mercados_con_filas"] == 3


# ---------------------------------------------------------------------------------------------------------- modelo
def df_sintetico(n=12000, seed=0):
    import pandas as pd
    r = np.random.default_rng(seed)
    d = pd.DataFrame({c: r.normal(size=n) for c in F5.RASGOS_BASE})
    d["coin_id"] = r.integers(0, 6, n)
    d["moneda"] = np.where(d["coin_id"] == 0, "BTC", "ETH")
    d["dy"] = 0.3 * d["rb500"] + 0.1 * d["T"] + r.normal(0, 0.1, n)
    return d


@pytest.mark.parametrize("ambito,nombre", [("pool", "hgb_d3_l500_i150_pool"), ("btc", "hgb_d3_l500_i150_btc")])
def test_modelo_reproducible_al_bit(ambito, nombre):
    import pickle
    cfg = next(c for n, a, c in F5.CANDIDATOS if n == nombre)
    d = df_sintetico()
    m1, m2 = F5.ajustar(d, nombre, ambito, cfg), F5.ajustar(d, nombre, ambito, cfg)
    assert pickle.dumps(m1, protocol=4) == pickle.dumps(m2, protocol=4)
    p1, p2 = F5.predecir(m1, d), F5.predecir(m2, d)
    assert p1.tobytes() == p2.tobytes()
    est = m1["est"]
    assert est.early_stopping is False and est.random_state == F5.SEED and est.n_iter_ == cfg["max_iter"]
    # el modelo aprende señal real (no es un cero constante)
    assert F5.r2(d[d["moneda"] == "BTC" if ambito == "btc" else slice(None)]["dy"].to_numpy(),
                 F5.predecir(m1, d[d["moneda"] == "BTC"] if ambito == "btc" else d)) > 0.3


def _entrenar_fixture(entorno, out, monedas=("BTC", "ETH")):
    return F5.entrenar(out, monedas, ["2026-10-10"], ["2026-10-11"])


def test_entrenar_hash_estable_y_juicio_no_reentrena(entorno, monkeypatch):
    monkeypatch.setattr(F5, "CANDIDATOS", [c for c in F5.CANDIDATOS if c[0] in ("ridge_btc", "hgb_d3_l500_i150_pool")])
    monkeypatch.setattr(F5, "GRID_STRIDE", 1)
    for d, s in (("2026-10-10", 1), ("2026-10-11", 2), ("2026-10-13", 3)):
        entorno["preparar"](d, coins=("BTC", "ETH"), seed=s, n5=6)
    ra, ma = _entrenar_fixture(entorno, entorno["out"])
    rb, mb = _entrenar_fixture(entorno, entorno["out"])                      # misma carpeta: debe reproducir byte a byte
    assert ra == rb and mb["reproducido_byte_a_byte"] is True and ma["hash"] == mb["hash"]
    assert ma["cumple_protocolo"] is False and ma["tomador_apto"] in (True, False)
    mdl = F5.FVModelo.cargar(ma["hash"], entorno["out"])
    assert mdl.hash == ma["hash"]
    # integridad: un byte cambiado se detecta
    pk = ra / "modelo.pkl"
    raw = pk.read_bytes()
    pk.write_bytes(raw[:-1] + bytes([raw[-1] ^ 1]))
    with pytest.raises(ValueError):
        F5.FVModelo.cargar(ma["hash"], entorno["out"])
    pk.write_bytes(raw)
    # juzgar: no se puede usar días del DESC; en OOS no reentrena (el hash del modelo no cambia) y trae COBERTURA
    with pytest.raises(ValueError):
        F5.juzgar(mdl, entorno["out"], ["2026-10-10"], ("BTC", "ETH"))
    lineas, res = F5.juzgar(mdl, entorno["out"], ["2026-10-13"], ("BTC", "ETH"))
    assert lineas[0].startswith("COBERTURA:") and "VEREDICTO PARTIAL" in lineas[0]      # 6 de 288 mercados
    assert F5.FVModelo.cargar(ma["hash"], entorno["out"]).meta["hash"] == ma["hash"]
    # señal: fv_en coincide con el predictor aplicado al dataset
    import pandas as pd
    df = F5.cargar(["2026-10-13"], entorno["out"], ("BTC", "ETH"))
    dh = mdl.dhat(df)
    sub = df[(df["moneda"] == "ETH") & (df["tipo"] == "evento15")].head(5)
    ctx = F5.contexto_dia("2026-10-13", ("ETH",))
    for _, r in sub.iterrows():
        s = F5.fv_en(ctx, mdl, "ETH", int(r["cierre"]), [int(r["t"])])
        assert s["dhat"][0] == pytest.approx(dh[r.name], abs=1e-12)
        assert s["fv_up"][0] == pytest.approx(min(max(r["mid5"] + dh[r.name], 0.01), 0.99), abs=1e-12)
    # exportar señal y lectura asof
    rutas = F5.exportar_senal(mdl, entorno["out"], ["2026-10-13"], ("BTC", "ETH"))
    se = F5.SenalFV(rutas[0])
    r0 = df[df["moneda"] == "BTC"].iloc[10]
    fv, edad = se.en(r0["mercado"], int(r0["t"]) + 400)
    assert 0 <= edad <= 400 and 0.01 <= fv <= 0.99
    assert se.en(r0["mercado"], int(r0["t"]) - 10**9)[1] is None


# ------------------------------------------------------------------------------------------------------ tomador
def df_econ(filas):
    import pandas as pd
    base = dict(dia="2026-10-14", moneda="BTC", mercado=1, cierre=1000, t=0, tipo="evento", T=100.0, bn500=0.0, mid5=0.5,
                bid5=0.49, ask5=0.51, ask5_lat=0.51, bid5_lat=0.49, asz_lat=100.0, bsz_lat=100.0, y=1)
    return pd.DataFrame([dict(base, **f) for f in filas])


def test_econ_primera_entrada_cronologica_fee_y_lados():
    # fila 0 (más tardía en tiempo) aparece antes en el DataFrame que la 1: debe elegirse la de menor t
    d = df_econ([dict(t=9000, ask5_lat=0.40), dict(t=2000, ask5_lat=0.45), dict(t=500, tipo="grid", ask5_lat=0.30)])
    o = F5.econ_tomador(d, np.full(3, 0.20), 0.05)
    assert len(o) == 1 and o.iloc[0]["t"] == 2000 and o.iloc[0]["lado"] == "Up"        # grid fuera, cronológica
    assert o.iloc[0]["pnl"] == pytest.approx(pnl_por_euro(0.45, 1))
    og = F5.econ_tomador(d, np.full(3, 0.20), 0.05, solo_eventos=False)
    assert og.iloc[0]["t"] == 500
    # Down: precio = 1 - bid_lat, profundidad = bsz_lat, gana si y==0
    d2 = df_econ([dict(y=0, bid5_lat=0.60, bid5=0.60, bsz_lat=7.0, ask5_lat=0.62, ask5=0.62)])
    o2 = F5.econ_tomador(d2, np.full(1, -0.30), 0.05)
    assert len(o2) == 1 and o2.iloc[0]["lado"] == "Down" and o2.iloc[0]["ask"] == pytest.approx(0.40)
    assert o2.iloc[0]["depth_val"] == pytest.approx(7.0 * 0.40) and o2.iloc[0]["pnl"] == pytest.approx(pnl_por_euro(0.40, 1))
    # pierde: -1 exacto
    d3 = df_econ([dict(y=0, ask5_lat=0.45)])
    assert F5.econ_tomador(d3, np.full(1, 0.20), 0.05).iloc[0]["pnl"] == pytest.approx(-1.0)


def test_econ_precios_frontera_y_nan():
    d = df_econ([dict(mercado=1, ask5_lat=1.0), dict(mercado=2, ask5_lat=0.0), dict(mercado=3, ask5_lat=np.nan),
                 dict(mercado=4, ask5_lat=0.93), dict(mercado=5, ask5_lat=0.50)])
    o = F5.econ_tomador(d, np.full(5, 0.60), 0.05)     # fv = 1.0 -> clip 0.99
    assert sorted(o["mercado"].tolist()) == [4, 5]      # ask>=1, ask<=0 y NaN excluidos
    # margen exacto en el borde: f - ask == M entra
    d4 = df_econ([dict(ask5_lat=0.45)])
    assert len(F5.econ_tomador(d4, np.full(1, 0.0), 0.05)) == 0                       # fv=0.5: 0.05 de margen
    assert len(F5.econ_tomador(d4, np.full(1, 0.0), 0.04)) == 1


def test_econ_limite_ask_t0_y_profundidad():
    d = df_econ([dict(mercado=1, ask5=0.50, ask5_lat=0.45), dict(mercado=2, ask5=0.45, ask5_lat=0.50)])
    assert len(F5.econ_tomador(d, np.full(2, 0.20), 0.05)) == 2
    ol = F5.econ_tomador(d, np.full(2, 0.20), 0.05, limite_t0=True)
    assert ol["mercado"].tolist() == [1] and ol.iloc[0]["dask"] == pytest.approx(-0.05)


def test_curva_monotona():
    assert F5.evaluar_curva({0.02: (100, 0.0), 0.03: (90, 0.02), 0.05: (60, 0.05), 0.08: (35, 0.09)}) == (True, 0.08)
    assert F5.evaluar_curva({0.02: (100, -0.1), 0.03: (90, -0.12), 0.05: (60, 0.02), 0.08: (35, -0.14)}) == (False, 0.08)  # pico aislado
    assert F5.evaluar_curva({0.02: (100, 0.0), 0.03: (90, 0.02), 0.05: (60, 0.05), 0.08: (10, -0.9)}) == (True, 0.05)    # n<30 no cuenta
    assert F5.evaluar_curva({0.02: (10, 0.1), 0.03: (90, 0.02)}) == (False, 0.03)                                          # 1 punto: no monótona


def test_guardia_cancelar_fail_closed():
    fv = np.array([0.52, 0.40, np.nan, 0.62])
    c = F5.cancelar_guardia(fv, "Up", 0.48, 0.03)
    assert c.tolist() == [False, True, True, False]         # NaN -> cancelar (0,52-0,48=0,04 >= g)
    cd = F5.cancelar_guardia(fv, "Down", 0.48, 0.03)         # FV_down = 1 - fv = 0.48, 0.60, nan, 0.38
    assert cd.tolist() == [True, False, True, True]


def test_auc_y_guarda_diag_con_senal_perfecta():
    import pandas as pd
    r = np.random.default_rng(0)
    n = 600
    m0 = r.uniform(0.3, 0.7, n)
    fut = m0 + r.normal(0, 0.03, n)
    ev = pd.DataFrame({"dia": "2026-10-14", "moneda": "BTC", "mid5": m0, "bid5": m0 - 0.01, "ask5": m0 + 0.01, "m5_3000": fut,
                       "rb500": np.zeros(n)})
    g = F5.guarda_diag(ev, fut - m0)           # Δ̂ = Δ real: AUC ~ 1
    assert g["BTC"]["auc_fv"] > 0.95
    g0 = F5.guarda_diag(ev, np.zeros(n))       # sin información: AUC ~ 0,5 (solo el semi-spread, constante)
    assert abs(g0["BTC"]["auc_fv"] - 0.5) < 0.1


def test_bloqueo_franja_y_ram(monkeypatch):
    assert F5.bloqueo(ahora=datetime(2026, 10, 16, 7, 0, tzinfo=timezone.utc)) is not None
    monkeypatch.setattr(F5, "mem_disponible_mb", lambda: 1000)
    assert "MemAvailable" in F5.bloqueo(ahora=datetime(2026, 10, 16, 12, 0, tzinfo=timezone.utc))
    monkeypatch.setattr(F5, "mem_disponible_mb", lambda: 5000)
    assert F5.bloqueo(ahora=datetime(2026, 10, 16, 12, 0, tzinfo=timezone.utc)) is None
    assert F5.bloqueo(ahora=datetime(2026, 10, 16, 7, 0, tzinfo=timezone.utc), sin_guardas=True) is None


def test_no_hay_ruta_de_envio_ni_secretos():
    src = Path(F5.__file__).read_text()
    for prohibido in ("dotenv", "data/live", "post_order", "create_order", "py_clob_client", "private_key", "ClobClient"):
        assert prohibido not in src
