"""Pruebas de cosechar al abrir v2 reactiva sobre flujos sintéticos (sin datos reales, sin red)."""
import collections
import gzip
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analisis_5m_cosechar_apertura_v2 as V2  # noqa: E402

F = 1_791_671_700_000                 # cierre (ms) del mercado sintético
FIN_ISO = "2026-10-10 22:35:00+00:00"
TY, TN, MK = "tokY", "tokN", "m1"
T0 = F - 299_000                      # primer instante dentro de los 15 s de entrada


def k_lines(extra_mkt=None):
    return [f"k,{T0 - 500},{TY},BTC,5min,{MK},{FIN_ISO},YES", f"k,{T0 - 500},{TN},BTC,5min,{MK},{FIN_ISO},NO"]


def q(t, tk, bid, ask, bsz=10.0, asz=20.0):
    return f"q,{t - 20},{tk},{bid},{ask},{bsz},{asz},{t}"


def tr(t_ex, t_rx, tk, p, side="SELL", sz=50.0):
    return f"t,{t_ex},{tk},{p},{side},{sz},{t_rx},"


def fixture(tmp_path, lines, name="m5.csv.gz"):
    f = tmp_path / name
    with gzip.open(f, "wt") as fh:
        fh.write("tipo,t_ms,id,c1,c2,c3,c4,c5\n" + "\n".join(lines) + "\n")
    return f


def flujo_basico(extra=()):
    """YES cotiza 0,48 (cola 0) y se rellena en T0+300 (recepción T0+330); NO cotiza 0,48 por debajo del bid (solo si cruza)."""
    L = k_lines()
    L += [q(T0, TY, 0.47, 0.49), q(T0 + 5, TN, 0.50, 0.52)]
    L += [tr(T0 + 300, T0 + 330, TY, 0.47)]                           # rellena YES: t_det = T0+330
    L += list(extra)
    L += [q(F - 100_000, TY, 0.60, 0.61), q(F - 100_000, TN, 0.38, 0.39)]
    return L


def filas_de(tmp_path, lines, res="YES", control=True):
    f = fixture(tmp_path, lines)
    st = V2.correr_flujo(f)
    filas, cov = V2.construir_filas("2026-10-10", st, {MK: res}, control=control)
    return {r["pol"]: r for r in filas}, st, cov


# ------------------------------------------------------------------ piezas puras
def test_clasificar():
    n = lambda y, nn: {"YES": y, "NO": nn}                             # noqa: E731
    assert V2.clasificar(n(5, 5), 0, 0) == "par_maker"
    assert V2.clasificar(n(3, 3), 0, 0) == "par_parcial"
    assert V2.clasificar(n(5, 0), 0, 0) == "suelta"
    assert V2.clasificar(n(5, 5), 5, 0) == "completado_tomador"
    assert V2.clasificar(n(5, 3), 3, 0) == "completado_parcial"
    assert V2.clasificar(n(0, 0), 0, 5) == "salida"
    assert V2.clasificar(n(2, 0), 0, 3) == "salida_parcial"
    assert V2.clasificar(n(1, 0), 2, 3) == "mixto"


def test_precio_skew():
    assert V2.precio_skew(0.48, 2, "YES", +1) == 0.48                  # favorecido: precio de v1
    assert V2.precio_skew(0.48, 2, "NO", +1) == 0.46                   # el otro: k ticks más bajo
    assert V2.precio_skew(0.48, 1, "YES", -1) == 0.47
    assert V2.precio_skew(0.48, 1, "NO", 0) == 0.48                    # sin señal: simétrico
    assert V2.precio_skew(0.02, 2, "YES", -1) == 0.01                  # nunca <= 0


def test_señal_binance_por_recepcion():
    d = collections.deque([(0, 100.0), (4000, 100.0), (6000, 100.0), (7000, 100.02)])   # ref = tick (0) <= 7000−5000=2000
    assert V2.señal_binance(d, 7000) == 1                              # +2 bps
    d = collections.deque([(0, 100.0), (7000, 100.001)])                # +0,1 bp < umbral
    assert V2.señal_binance(d, 7000) == 0
    d = collections.deque([(0, 100.0), (7000, 99.98)])
    assert V2.señal_binance(d, 7000) == -1
    d = collections.deque([(5500, 100.0), (7000, 101.0)])               # sin tick <= t−5 s: sin dato
    assert V2.señal_binance(d, 7000) == 0
    d = collections.deque([(0, 100.0), (9000, 101.0)])                  # referencia 2 s+ vieja respecto a t−5 s: sin dato
    assert V2.señal_binance(d, 9000) == 0


EVY = [(1000, 1030, 0.48, 5.0)]
VAR = {v[0]: v for v in V2.variantes(control=True)}


def snap(bidY=0.47, askY=0.49, bidN=0.49, askN=0.50, bszY=10.0, aszN=20.0, aszY=20.0, bszN=10.0):
    return {"YES": (bidY, askY, bszY, aszY), "NO": (bidN, askN, bszN, aszN)}


def test_r1_completa_y_contabilidad():
    x = V2.evaluar_variante(VAR["_R1_U1.00"], {"YES": EVY, "NO": []}, (1030, "YES"), snap(), "YES")
    assert x["modo_final"] == "completado_tomador" and x["tN"] == 5.0
    fee = 0.07 * 0.5 * 0.5
    assert x["coste"] == pytest.approx(5 * 0.48 + 5 * 0.50)
    assert x["fees"] == pytest.approx(5 * fee)
    assert x["pnl"] == pytest.approx(5 - 4.9 - 5 * fee)
    # mismo caso, gana el otro lado: pago 5 por NO
    y = V2.evaluar_variante(VAR["_R1_U1.00"], {"YES": EVY, "NO": []}, (1030, "YES"), snap(), "NO")
    assert y["pnl"] == pytest.approx(5 - 4.9 - 5 * fee)


def test_r1_umbral_no_cumplido_queda_suelta():
    x = V2.evaluar_variante(VAR["_R1_U1.00"], {"YES": EVY, "NO": []}, (1030, "YES"), snap(askN=0.53), "NO")
    assert x["modo_final"] == "suelta" and x["motivo"] == "U_no_cumplida" and x["tN"] == 0
    assert x["pnl"] == pytest.approx(0 - 5 * 0.48)                      # pierde la pata suelta


@pytest.mark.parametrize("sn,mot", [(snap(bidN=0.51, askN=0.50), "libro_cruzado"), (snap(aszN=0.0), "sin_liquidez"),
                                     (None, "sin_dato"), ({"YES": snap()["YES"], "NO": None}, "sin_dato")])
def test_r1_sin_dato_no_opera(sn, mot):
    x = V2.evaluar_variante(VAR["_R1_U1.05"], {"YES": EVY, "NO": []}, (1030, "YES"), sn, "YES")
    assert x["tN"] == 0 and x["motivo"] == mot and x["modo_final"] == "suelta"


def test_r1_liquidez_parcial():
    x = V2.evaluar_variante(VAR["_R1_U1.05"], {"YES": EVY, "NO": []}, (1030, "YES"), snap(aszN=2.0), "YES")
    assert x["tN"] == 2.0 and x["modo_final"] == "completado_parcial"


def test_r2_salida_y_fee():
    x = V2.evaluar_variante(VAR["_R2_X0.03"], {"YES": EVY, "NO": []}, (1030, "YES"), snap(bidY=0.46), "YES")
    assert x["modo_final"] == "salida" and x["sY"] == 5.0
    fee = 0.07 * 0.46 * 0.54
    assert x["pnl"] == pytest.approx(5 * 0.46 - 5 * 0.48 - 5 * fee)
    y = V2.evaluar_variante(VAR["_R2_X0.03"], {"YES": EVY, "NO": []}, (1030, "YES"), snap(bidY=0.44), "NO")
    assert y["modo_final"] == "suelta" and y["motivo"] == "X_no_cumplida"
    z = V2.evaluar_variante(VAR["_R2_X0.03"], {"YES": EVY, "NO": []}, (1030, "YES"), snap(bidY=0.45), "NO")
    assert z["modo_final"] == "salida"                                  # frontera bid == precio − X


def test_r3_cae_a_salida():
    sn = snap(askN=0.60, bidY=0.47)
    x = V2.evaluar_variante(VAR["_R3_U1.00_X0.03"], {"YES": EVY, "NO": []}, (1030, "YES"), sn, "NO")
    assert x["modo_final"] == "salida" and x["motivo"] == "U_no_cumplida|salida"
    y = V2.evaluar_variante(VAR["_R3_U1.00_X0.03"], {"YES": EVY, "NO": []}, (1030, "YES"), snap(), "YES")
    assert y["modo_final"] == "completado_tomador" and y["sY"] == 0      # R1 primero


def test_cancelacion_ventana_65ms():
    dentro = [(1030 + 65, 1100, 0.48, 5.0)]
    fuera = [(1030 + 66, 1100, 0.48, 5.0)]
    a = V2.evaluar_variante(VAR["_R1_U1.00"], {"YES": EVY, "NO": dentro}, (1030, "YES"), snap(), "YES")
    assert a["modo_final"] == "par_maker" and a["qN"] == 5.0
    b = V2.evaluar_variante(VAR["_R1_U1.00"], {"YES": EVY, "NO": fuera}, (1030, "YES"), snap(), "YES")
    assert b["qN"] == 0 and b["modo_final"] == "completado_tomador"      # el relleno tardío del maker no existe y se completa
    c = V2.evaluar_variante(VAR["_CTRL"], {"YES": EVY, "NO": fuera}, (1030, "YES"), snap(), "YES")
    assert c["qN"] == 5.0 and c["modo_final"] == "par_maker"             # el control no cancela: v1


def test_rellenos_conocidos_solo_hasta_t_act():
    tarde = [(1090, 1030 + V2.L_TOMADOR_MS + 1, 0.48, 5.0)]             # relleno de la otra pata recibido DESPUÉS de t_act
    x = V2.evaluar_variante(VAR["_R1_U1.05"], {"YES": EVY, "NO": tarde}, (1030, "YES"), snap(), "YES")
    assert x["tN"] == 5.0 and x["qN"] == 5.0                            # no se conocía a t_act: compra y queda doble (ledger completo)
    assert x["modo_final"] == "completado_parcial" and x["completo"] == 1 and x["qY"] == 5.0
    assert x["coste"] == pytest.approx(5 * 0.48 + 5 * 0.48 + 5 * 0.50)


def test_ctrl_equivale_a_base():
    for ev in ({"YES": EVY, "NO": []}, {"YES": EVY, "NO": [(1050, 1060, 0.48, 3.0)]}):
        b = V2.evaluar_variante(VAR[""], ev, (1030, "YES"), snap(), "YES")
        c = V2.evaluar_variante(VAR["_CTRL"], ev, (1030, "YES"), snap(), "YES")
        for k in ("qY", "qN", "coste", "pnl", "rebate", "completo", "modo_final"):
            assert b[k] == c[k]


# ------------------------------------------------------------------ flujo completo
def test_flujo_r1_y_sin_lookahead(tmp_path):
    t_det = T0 + 330
    L = [q(t_det + 100, TN, 0.49, 0.50, asz=20.0),                      # libro válido antes de t_act
         q(t_det + V2.L_TOMADOR_MS, TN, 0.49, 0.51, asz=20.0),          # recepción == t_act: SÍ cuenta
         q(t_det + V2.L_TOMADOR_MS + 1, TN, 0.30, 0.31, asz=20.0)]      # posterior: NO debe usarse
    filas, st, cov = filas_de(tmp_path, flujo_basico(L))
    r = filas["A0_P96_FINAL_R1_U1.05"]
    assert r["modo_final"] == "completado_tomador"
    assert float(r["coste"]) == pytest.approx(5 * 0.48 + 5 * 0.51)      # ask 0,51 de t_act, no 0,31 de t_act+1
    assert filas["A0_P96_FINAL"]["modo_final"] == "suelta"
    assert filas["A0_P96_FINAL_CTRL"]["pnl"] == filas["A0_P96_FINAL"]["pnl"]
    assert cov["incoherencias_eventos"] == 0 and cov["sin_foto"] == 0 and cov["mercados_con_rellenos"] == 1


def test_flujo_libro_cruzado_no_opera(tmp_path):
    t_det = T0 + 330
    filas, _st, _cov = filas_de(tmp_path, flujo_basico([q(t_det + 150, TN, 0.52, 0.50)]))
    r = filas["A0_P96_FINAL_R1_U1.05"]
    assert r["modo_final"] == "suelta" and r["motivo"] == "libro_cruzado"


def test_flujo_sin_foto_al_acabar_el_archivo(tmp_path):
    L = k_lines() + [q(T0, TY, 0.47, 0.49), q(T0 + 5, TN, 0.50, 0.52), tr(T0 + 300, T0 + 330, TY, 0.47)]
    filas, _st, cov = filas_de(tmp_path, L)
    assert cov["sin_foto"] >= 1
    r = filas["A0_P96_FINAL_R1_U1.05"]
    assert r["modo_final"] == "suelta" and r["motivo"] == "sin_dato"


def test_flujo_pata_otra_rellena_en_ventana_de_cancelacion(tmp_path):
    # NO (0,48 < bid 0,50: solo cruza): relleno con t_ex = t_det+60 -> entra; t_ex = t_det+200 -> sería de v1 pero R1 ya canceló
    t_det = T0 + 330
    L = [tr(t_det + 60, t_det + 70, TN, 0.47)]
    filas, _st, _c = filas_de(tmp_path, flujo_basico(L))
    assert filas["A0_P96_FINAL_R1_U1.05"]["modo_final"] == "par_maker"
    L2 = [tr(t_det + 200, t_det + 210, TN, 0.47)]
    filas2, _st, _c = filas_de(tmp_path, flujo_basico(L2))
    assert filas2["A0_P96_FINAL"]["modo_final"] == "par_maker"           # v1: la pata sigue viva y se rellena
    assert filas2["A0_P96_FINAL_CTRL"]["modo_final"] == "par_maker"
    assert filas2["A0_P96_FINAL_R1_U0.00"]["modo_final"] == "suelta"     # ablación: cancelar sola cambia el resultado


def test_flujo_sin_desenlace_se_cuenta(tmp_path):
    f = fixture(tmp_path, flujo_basico())
    st = V2.correr_flujo(f)
    filas, cov = V2.construir_filas("2026-10-10", st, {}, control=False)
    assert filas == [] and cov["sin_desenlace"] == 1


def test_skew_baja_la_otra_pata(tmp_path):
    # Binance sube >1 bp en 5 s antes de cotizar -> YES a 0,48, NO a 0,47 (k=1) / 0,46 (k=2)
    bx = [f"x,{T0 - 6000},BTCUSDT,100000.0,1,0,{T0 - 6000},{T0 - 6000}", f"x,{T0 - 1},BTCUSDT,100020.0,1,0,{T0 - 1},{T0 - 1}"]
    L = k_lines() + bx + [q(T0, TY, 0.47, 0.49), q(T0 + 5, TN, 0.50, 0.52)]
    f = fixture(tmp_path, L)
    st = V2.correr_flujo(f)
    precios = {m: [s[0] for tk in (TY, TN) for s in st["est"][(m, tk)].segs] for m in
               ("A0_P96_FINAL", "A0_P96_FINAL_S1k1", "A0_P96_FINAL_S1k2")}
    assert precios["A0_P96_FINAL"] == [0.48, 0.48]
    assert precios["A0_P96_FINAL_S1k1"] == [0.48, 0.47]
    assert precios["A0_P96_FINAL_S1k2"] == [0.48, 0.46]


def test_corte_max_mercados_y_lineas(tmp_path):
    # un segundo mercado posterior provoca el corte tras 1 mercado cerrado; las líneas leídas excluyen la que corta
    L = flujo_basico()
    F2 = F + 300_000
    L += [f"k,{F},tokY2,BTC,5min,m2,2026-10-10 22:40:00+00:00,YES", f"k,{F},tokN2,BTC,5min,m2,2026-10-10 22:40:00+00:00,NO",
          q(F + 10, "tokY2", 0.47, 0.49)]
    f = fixture(tmp_path, L)
    st = V2.correr_flujo(f, max_mercados=1)
    assert st["st"]["t_stop"] == F + 10 and st["st"]["lineas"] == len(L) + 1 - 1   # cabecera incluida, línea de corte no
    assert V2.mercados_cerrados(st) == {MK}
    assert F2 > F


def test_politicas_unicas_y_nombres():
    p = [x[0] for x in V2.politicas(control=True)]
    assert len(p) == len(set(p))
    assert "A_BN_P96_CABEZA_R3_U1.05_X0.10" in p and "A0_P96_FINAL_S1k2" in p and "A0_P96_FINAL_CTRL" in p
    assert not any("S1k" in x and "_R" in x for x in p)


def _flujo_dos_tramos(tmp_path, bn_compat):
    """Tramo 1 (hora H) con un tick Binance muy distinto; tramo 2 (una hora ANTES, como en los registros concatenados)."""
    from datetime import datetime, timezone
    Fb = F - 3_600_000
    iso = datetime.fromtimestamp(Fb / 1000, timezone.utc).strftime("%Y-%m-%d %H:%M:%S+00:00")
    T0b = Fb - 299_000
    L = k_lines() + [f"x,{T0 - 10_000},BTCUSDT,99000.0,1,0,{T0 - 10_000},{T0 - 10_000}", q(T0, TY, 0.47, 0.49)]
    L += [f"k,{T0b - 500},tokYb,BTC,5min,m2,{iso},YES", f"k,{T0b - 500},tokNb,BTC,5min,m2,{iso},NO",
          f"x,{T0b - 3000},BTCUSDT,100000.0,1,0,{T0b - 3000},{T0b - 3000}", q(T0b, "tokYb", 0.47, 0.49), q(T0b + 5, "tokNb", 0.50, 0.52),
          f"x,{T0b + 1000},BTCUSDT,100000.0,1,0,{T0b + 1000},{T0b + 1000}", q(T0b + 2000, "tokYb", 0.47, 0.49)]
    st = V2.correr_flujo(fixture(tmp_path, L), bn_compat=bn_compat)
    return st, Fb


def test_salto_de_tramo_reinicia_ventana_binance(tmp_path):
    st, Fb = _flujo_dos_tramos(tmp_path, bn_compat=False)
    seg = st["est"][("A_BN_P96_FINAL", "tokYb")].segs[-1]
    assert st["st"]["saltos_tiempo"] == 1
    assert seg[3] == Fb - V2.T_FIN_S * 1000                           # la defensa no se dispara con un tick de otro tramo
    st2, Fb2 = _flujo_dos_tramos(tmp_path, bn_compat=True)
    seg2 = st2["est"][("A_BN_P96_FINAL", "tokYb")].segs[-1]
    assert seg2[3] < Fb2 - V2.T_FIN_S * 1000                          # v1: compara con un tick de hace una hora y cancela


def test_salto_de_tramo_descarta_fotos_pendientes(tmp_path):
    t_det = T0 + 330
    L = flujo_basico()[:-2] + [q(t_det - 3_600_000, TN, 0.49, 0.50)]  # el siguiente tramo empieza antes de t_det + L
    filas, st, cov = filas_de(tmp_path, L)
    assert st["st"]["saltos_tiempo"] == 1 and cov["sin_foto"] >= 1
    assert filas["A0_P96_FINAL_R1_U1.05"]["motivo"] == "sin_dato"
