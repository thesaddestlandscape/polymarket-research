#!/usr/bin/env python3
"""Tests del shadow H23 v3 (sin red, sin disco de produccion). Desde este directorio: python3 -m pytest -q test_h23_shadow_v3.py
Incluye la EQUIVALENCIA con el replay (h23_sim_v3.segmentos/llenar): mismos segmentos y mismos rellenos con flujos aleatorios de libro+operaciones."""
import os, random, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..'))
import numpy as np
import pytest
import h23_regla_v3 as R
import h23_shadow_v3 as S
import h23_sim_v3 as V3

C = 1_800_000_000
U5, D5, U15, D15 = "u5", "d5", "u15", "d15"


def ms(T):
    return int(round((C - T) * 1000))


class Banco:
    """Par BTC 5m/15m sintetico (lado Up). Un 'estado' de libro se aplica con UNA llamada a on_price_change (un solo evaluar por evento, como una fila q del registro)."""
    def __init__(self):
        self.rows = []
        self.n = S.Nucleo(self.rows.append)
        self.p = self.n.nuevo_par(C, {"id": "m5", "up": U5, "down": D5}, {"id": "m15", "up": U15, "down": D15}, ms(350))
        self.cur = {}
        self.n.fijar_lado(self.p, 100.0, 99.9, ms(298.4))

    def libro(self, t_ms, b5, bs5, a5, b15, a15, as5=50.0):
        niv = {(U5, "BUY"): (b5, bs5), (U5, "SELL"): (a5, as5), (U15, "BUY"): (b15, 80.0), (U15, "SELL"): (a15, 80.0),
               (D5, "BUY"): (0.60, 10.0), (D5, "SELL"): (0.70, 10.0), (D15, "BUY"): (0.50, 10.0), (D15, "SELL"): (0.54, 10.0)}
        if not self.cur:                                                      # primer estado: snapshots `book` (dejan vivo cada libro); el ultimo completa la vista
            self.n.vivo(self.p, t_ms)
            for tk in (D5, D15, U15, U5):
                self.n.on_book(tk, t_ms, [{"price": str(niv[(tk, "BUY")][0]), "size": str(niv[(tk, "BUY")][1])}],
                               [{"price": str(niv[(tk, "SELL")][0]), "size": str(niv[(tk, "SELL")][1])}])
            self.cur = dict(niv)
            return
        ent = []
        for (tk, side), (px, sz) in niv.items():
            ant = self.cur.get((tk, side))
            if ant and ant[0] != px:
                ent.append({"asset_id": tk, "side": side, "price": str(ant[0]), "size": "0"})
            if not ant or ant != (px, sz):
                ent.append({"asset_id": tk, "side": side, "price": str(px), "size": str(sz)})
            self.cur[(tk, side)] = (px, sz)
        self.n.vivo(self.p, t_ms)
        if ent:
            self.n.on_price_change(t_ms, ent)
        else:
            self.n.evaluar(self.p, t_ms)                                      # estado repetido: equivale a un tick (el replay tambien evalua esa fila)

    def venta(self, t_ms, pc, acc):
        self.n.vivo(self.p, t_ms)
        self.n.on_trade(U5, t_ms, {"price": str(pc), "size": str(acc), "side": "SELL"})

    def tipo(self, t, **kw):
        return [r for r in self.rows if r["tipo"] == t and all(r.get(k) == v for k, v in kw.items())]


def test_variantes_y_config():
    assert S.VARIANTES == ("join", "join_150", "join_r", "nc")
    assert R.CONFIG["repost_min_ms"] == {"join": 0, "join_r": 1500, "join_150": 150, "nc": 0}
    assert S.CFG["repuja_ms"] == 150 and R.hash_config() == "3eeff503cf0a75c9"
    assert S.querible(0.09) is None and S.querible(0.10) == 0.10 and S.querible(0.60) == 0.60 and S.querible(0.61) is None and S.querible(None) is None


def test_repuja_150_vs_1500_hecho_a_mano():
    b = Banco()
    # T=250: bid 0,30 respaldado por el 15m 0,45 -> todos pujan 0,30 (A, umbral 0,05)
    b.libro(ms(250), 0.30, 100.0, 0.33, 0.45, 0.47)
    for v in ("join", "join_150", "join_r"):
        assert b.tipo("puesto", arm="A", var=v)[0]["precio"] == 0.30
    # T=240: el bid15 cae a 0,36 -> p_limite < 0,30 -> la condicion se rompe: cancelan en ese evento
    b.libro(ms(240), 0.30, 100.0, 0.33, 0.36, 0.38)
    for v in ("join", "join_150", "join_r"):
        assert b.tipo("cancela", arm="A", var=v)[0]["causa"] == "cota_cae"
    # T=239,9 (100 ms despues) vuelve la condicion: r0 re-puja ya; r150 todavia NO (bloqueado hasta +150); r1500 tampoco
    b.libro(ms(239.9), 0.30, 100.0, 0.33, 0.45, 0.47)
    assert len(b.tipo("puesto", arm="A", var="join")) == 2
    assert len(b.tipo("puesto", arm="A", var="join_150")) == 1 and len(b.tipo("puesto", arm="A", var="join_r")) == 1
    # T=239,8 (200 ms despues de la decision): r150 re-puja con t_dec = decision+150 EXACTO (no a +200) y estado del evento previo (bid15 0,45)
    b.libro(ms(239.8), 0.30, 100.0, 0.33, 0.45, 0.47)
    p150 = b.tipo("puesto", arm="A", var="join_150")
    assert len(p150) == 2 and p150[1]["r"] == ms(240) + 150 and p150[1]["repuja"] is True and p150[1]["precio"] == 0.30
    rp = b.tipo("repuja", arm="A", var="join_150")[0]
    assert rp["ms_desde_decision_cancel"] == 150 and rp["simulada"] is True and rp["lag_obs_ms"] == 50
    assert len(b.tipo("puesto", arm="A", var="join_r")) == 1                      # placebo: sigue bloqueado hasta +1500
    b.libro(ms(238.4), 0.30, 100.0, 0.33, 0.45, 0.47)                              # +1,6 s
    pr = b.tipo("puesto", arm="A", var="join_r")
    assert len(pr) == 2 and pr[1]["r"] == ms(240) + 1500


def test_universo_precio_y_T12_y_tamano_real():
    b = Banco()
    b.libro(ms(250), 0.08, 100.0, 0.10, 0.20, 0.22, as5=40.0)                      # 0,08 < 0,10: fuera del universo ejecutable -> nadie puja
    assert not b.tipo("puesto")
    b.libro(ms(240), 0.15, 100.0, 0.18, 0.30, 0.32)                                 # 0,15: need = ceil(1/0,15)=7 acc (no 2 EUR)
    assert b.tipo("puesto", arm="A", var="join")[0]["need"] == 7.0
    b2 = Banco()
    b2.libro(ms(11), 0.30, 100.0, 0.33, 0.45, 0.47)                                 # T=11 s <= 12: no se abre puja NUEVA
    assert not b2.tipo("puesto") and b2.p.motivos["sin_puja_nueva_T<=12"] > 0


def test_primer_relleno_cierra_la_puja_por_escenario():
    b = Banco()
    b.libro(ms(250), 0.30, 1.0, 0.33, 0.45, 0.47)                                   # sin nada delante
    b.venta(ms(250) + 100, 0.30, 2.0)                                                # relleno parcial (2 de 5 acc)
    b.venta(ms(250) + 200, 0.30, 10.0)                                               # NO debe sumar: la puja ya se cerro con el primero
    b.n.cerrar_par("m5", ms(-0.5))
    e = b.tipo("relleno_resumen", arm="A", var="join")[0]["esc"]
    assert e["opt|c"]["acc"] == pytest.approx(2.0) and e["opt|c"]["n"] == 1


def _flujo(rng, n_ev=40):
    """Flujo aleatorio de estados de libro (T de 295 a 20 s) y operaciones SELL sobre el 5m."""
    ts = sorted(set(int(ms(295) + x) for x in rng.integers(0, 270_000, n_ev)))
    evs = []
    for t in ts:
        b15 = float(rng.choice([0.30, 0.36, 0.40, 0.45, 0.50, 0.64]))
        b5 = float(rng.choice([0.12, 0.20, 0.30, 0.31, 0.33, 0.45, 0.62]))
        evs.append((t, b5, float(rng.integers(1, 300)), round(b5 + float(rng.choice([0.01, 0.02, 0.03])), 2), b15, round(b15 + 0.02, 2)))
    trs = sorted(set((int(ms(295) + x), float(rng.choice([0.12, 0.20, 0.29, 0.30, 0.31, 0.33, 0.45])), float(rng.integers(1, 30)))
                     for x in rng.integers(0, 275_000, 25)))
    t, *u = evs[-1]
    evs.append((ms(11.0),) + tuple(u))                                              # evento final a T=11 s: el replay solo materializa una re-puja pendiente si hay un evento posterior
    return evs, trs


@pytest.mark.parametrize("seed", range(40))
def test_equivalencia_con_el_replay_v3(seed, monkeypatch):
    monkeypatch.setitem(S.CFG, "max_cotiz_por_mercado", 10 ** 6)                 # el replay no tiene el tope de 20 cotizaciones/mercado del shadow
    rng = np.random.default_rng(seed)
    evs, trs = _flujo(rng)
    # ---- shadow: eventos de libro y operaciones intercalados por hora de recepcion
    b = Banco()
    cola = [(e[0], 0, e) for e in evs] + [(t[0], 1, t) for t in trs]
    cola.sort(key=lambda x: (x[0], x[1]))
    for t, k, x in cola:
        if k == 0:
            b.libro(t, *x[1:])
        else:
            b.venta(t, x[1], x[2])
    b.n.cerrar_par("m5", ms(-0.5))
    # ---- replay: mismas series
    inst = np.array([e[0] for e in evs], dtype=np.int64)
    ask5 = np.array([e[3] for e in evs]); bid5 = np.array([e[1] for e in evs]); bsz = np.array([e[2] for e in evs])
    bid15 = np.array([e[4] for e in evs]); ask15 = np.array([e[5] for e in evs])
    t_ini, t_fin = (C - 300) * 1000 + R.CONFIG["ref_conocible_ms"], (C - R.CONFIG["fin_margen_s"]) * 1000
    tpm = (C - R.CONFIG["t_min_ejec_s"]) * 1000
    m = (inst >= t_ini) & (inst < t_fin)
    inst, ask5, bid5, bsz, bid15, ask15 = inst[m], ask5[m], bid5[m], bsz[m], bid15[m], ask15[m]
    FIL = [(t[0], t[1], t[2]) for t in trs]
    FE = np.array([f[0] for f in FIL], dtype=np.int64)
    for var, rep in (("join", 0), ("join_150", 150), ("join_r", 1500)):
        for brazo, umbral in R.CONFIG["brazos"].items():
            want = [V3.querible(R.querer(b5, a5, bb, aa, umbral), True) for b5, a5, bb, aa in zip(bid5, ask5, bid15, ask15)]
            segs = V3.segmentos(inst, want, bsz, rep, tpm)
            rec = b.n.records["m5"]["res"]
            filas = sorted((r["n"], r["precio"], r["r"]) for r in b.tipo("puesto", arm=brazo, var=var))
            exp = sorted((i + 1, s[0], s[2]) for i, s in enumerate(segs))
            assert filas == exp, (var, brazo, filas, exp)
            if not segs:
                continue
            need = R.acciones_real(segs[0][0])
            for cola_n, frac in R.CONFIG["colas"].items():
                for lp, lc, tag in ((79, 60, "c"), (254, 150, "k")):
                    lleno, coste, t_rel, p_rel, nf = V3.llenar(segs, need, frac, lp, lc, FIL, FE, t_fin, True)
                    d = rec[f"{brazo}|{var}|{cola_n}|{tag}"]
                    assert d["acc"] == pytest.approx(round(lleno, 4), abs=1e-3), (var, brazo, cola_n, tag, d, lleno)
                    assert d["coste"] == pytest.approx(round(coste, 5), abs=1e-3)
                    assert d["n"] == nf


def test_nc_control_no_cancela_y_una_sola_puja():
    b = Banco()
    b.libro(ms(250), 0.30, 50.0, 0.33, 0.45, 0.47)
    b.libro(ms(240), 0.30, 50.0, 0.33, 0.36, 0.38)                                  # la condicion se rompe: el control NO cancela
    assert not b.tipo("cancela", var="nc") and len(b.tipo("puesto", var="nc", arm="A")) == 1


def test_restaurar_es_idempotente_y_no_repite_filas(tmp_path):
    out = S.Salida(str(tmp_path))
    nuc = S.Nucleo(out.put)
    nuc.emit({"k": "x|1", "tipo": "latido", "r": ms(100)})
    out.cerrar()
    em, rec = S.restaurar(str(tmp_path), C - 100)
    assert "x|1" in em
    nuc2 = S.Nucleo(lambda r: None, em, rec)
    assert nuc2.emit({"k": "x|1", "tipo": "latido", "r": ms(99)}) is False


def test_sin_ordenes_ni_claves_en_el_fuente():
    src = open(os.path.join(HERE, 'h23_shadow_v3.py')).read()
    for prohibido in ('py_clob_client', 'create_order', 'post_order', '.env', 'private_key', 'PRIVATE_KEY', 'signature'):
        assert prohibido not in src, prohibido
