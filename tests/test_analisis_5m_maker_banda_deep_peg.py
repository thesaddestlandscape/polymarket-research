"""Pruebas de H35 DEEP_PEG / H37 salida / H38 markout sobre flujos sintéticos: sin datos reales, sin red, sin órdenes."""
import argparse
import gzip
import json
import sys
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analisis_5m_maker_banda_deep_peg as D  # noqa: E402
import analisis_5m_maker_banda_simulador as S  # noqa: E402

FIN = 1_791_936_300_000
FIN_ISO = "2026-10-14 00:05:00+00:00"
TY, TN, MK = "tokY", "tokN", "m1"
T0 = FIN - 299_000                        # T = 299 s


def k_lines(coin="BTC", mkt=MK, ty=TY, tn=TN):
    return [f"k,{T0 - 500},{ty},{coin},5min,{mkt},{FIN_ISO},YES", f"k,{T0 - 500},{tn},{coin},5min,{mkt},{FIN_ISO},NO"]


def q(t, tk, bid, ask, bsz=10.0, asz=20.0, lag=20):
    return f"q,{t - lag},{tk},{bid},{ask},{bsz},{asz},{t}\n"


def tr(t_ex, tk, p, side="SELL", sz=50.0, lag=20):
    return f"t,{t_ex},{tk},{p},{side},{sz},{t_ex + lag},\n"


def lrow(t, tk, niv, lag=5):
    """Fila l de ASK del token: niv = [(precio, tamaño)] (hasta 3)."""
    cols = [str(x) for ps in niv for x in ps] + [""] * (6 - 2 * len(niv))
    return f"l,{t - lag},{tk},{','.join(cols)},{t}\n"


def srt(lines):
    """Ordena las filas sintéticas por hora de recepción (el registro de un tramo es cronológico)."""
    def key(ln):
        c = ln.split(",")
        return int(c[7]) if c[0] == "q" else int(c[6]) if c[0] == "t" else int(c[9]) if c[0] == "l" else 0
    return sorted(lines, key=key)


def ka(t0, t1, paso=5000):
    return [q(t, TN, 0.50, 0.52) for t in range(t0, t1, paso)]


def fichero(tmp_path, lines, name="m5.csv.gz"):
    f = tmp_path / name
    with gzip.open(f, "wt") as fh:
        fh.write("tipo,t_ms,id,c1,c2,c3,c4,c5\n")
        for ln in lines:
            fh.write(ln if ln.endswith("\n") else ln + "\n")
    return f


def motores(ks=(1,), colas=("CONS",), bn=False, placebos=False, **kw):
    return D.construir_motores(ks, colas, bn=bn, placebos=placebos, **kw)


def ladders(*lineas):
    lad = D.Ladders()
    for ln in lineas:
        lad.add(ln)
    return lad


def correr(tmp_path, lines, engines=None, lad=None, ext=None, nombre="m5.csv.gz", deltas=D.DELTAS):
    f = fichero(tmp_path, k_lines() + list(lines), nombre)
    return D.procesar_registro(f, ext or S.Externas(), lad or D.Ladders(), engines or motores(), 0, deltas=deltas)


def unidad(mo, nombre, tk=TY):
    for p in mo.pos_ant:
        if p.e.nombre == nombre and p.tk == tk:
            return p
    return None


def fila(mo, nombre, tk=TY):
    for r in mo.filas_deep("2026-10-14"):
        if r["motor"] == nombre and r["lado"] == ("YES" if tk == TY else "NO"):
            return r
    return None


DK1 = "DEEP_k1|C0|CONS|5"
DK1O = "DEEP_k1|C0|OPT|5"


def trazas(tmp_path, lines, engines=None, lad=None, ext=None, nombre="t.csv.gz"):
    """-> (lista de pujas [(motor, token, t_rx, precio, qty)], motor)"""
    f = fichero(tmp_path, k_lines() + list(lines), nombre)
    mo = D.procesar_registro(f, ext or S.Externas(), lad or D.Ladders(), engines or motores(), 0, traza=True)
    return mo.traza, mo


# ---------------------------------------------------------------- escalones por niveles (espejo YES-bid = NO-ask a 1−p)
def test_ladders_nivel_listado_vacio_entre_niveles_y_desconocido():
    lad = ladders(lrow(1000, TN, [(0.75, 10.0), (0.77, 3.0), (0.80, 9.0)]))
    assert lad.nivel(TN, 750, 1500) == (10.0, True)
    assert lad.nivel(TN, 770, 1500) == (3.0, True)
    assert lad.nivel(TN, 760, 1500) == (0.0, True)           # entre niveles listados: vacío CONOCIDO
    assert lad.nivel(TN, 700, 1500) == (0.0, True)           # por debajo del mejor
    assert lad.nivel(TN, 850, 1500) == (None, False)         # más profundo que el 3º nivel: desconocido
    assert lad.nivel(TN, 750, 900) == (None, False)          # antes de la primera fila
    assert lad.nivel("otro", 750, 1500) == (None, False)


def test_ladders_menos_de_tres_niveles_implica_vacio_mas_arriba_y_filas_desordenadas_se_ordenan():
    lad = ladders(lrow(2000, TN, [(0.75, 10.0), (0.77, 3.0)]), lrow(1000, TN, [(0.75, 99.0)]))   # llegan desordenadas
    assert lad.nivel(TN, 900, 2500) == (0.0, True)           # libro de 2 niveles: más profundo = vacío
    assert lad.nivel(TN, 750, 1500) == (99.0, True)          # la fila anterior a t=1500
    assert lad.nivel(TN, 750, 2500) == (10.0, True)


def test_ladders_fila_L_libro_completo_manda_si_es_la_mas_reciente_y_cubre_niveles_profundos():
    lad = ladders(lrow(1000, TN, [(0.75, 10.0), (0.76, 7.0), (0.77, 3.0)]),
                  "L,1990,%s,0.75:10.0;0.76:7.0;0.77:3.0;0.9:55.0;0.95:1.0,2000\n" % TN)
    assert lad.nivel(TN, 900, 2500) == (55.0, True)          # nivel profundo conocido por L
    assert lad.nivel(TN, 880, 2500) == (0.0, True)           # L completo: ausente = vacío
    assert lad.nivel(TN, 760, 1500) == (7.0, True)           # antes de L usa l


# ---------------------------------------------------------------- precio de la puja, banda, nunca mejorar el top
def test_deep_puja_en_top_menos_k_ticks_y_nunca_mejora_el_top(tmp_path):
    tz, mo = trazas(tmp_path, [q(T0, TY, 0.25, 0.30)], motores(ks=(1, 2)))
    precios = {n: p for n, _, _, p, _ in tz}
    assert precios["DEEP_k1|C0|CONS|5"] == 240 and precios["DEEP_k2|C0|CONS|5"] == 230
    assert all(p < 250 for p in precios.values())
    assert all(qty == 5.0 for *_, qty in tz)


def test_banda_del_top_es_mayor_que_011_y_hasta_030(tmp_path):
    for bid, esperado in ((0.11, False), (0.12, True), (0.30, True), (0.31, False)):
        tz, _ = trazas(tmp_path, [q(T0, TY, bid, bid + 0.05)], motores(ks=(2,)), nombre=f"b{bid}.csv.gz")
        assert bool(tz) is esperado, bid
    # k=2 con top 0,12 -> 0,10 (permitido); JOIN con top 0,11 sí cotiza (banda base 0,10 < bid) y DEEP no
    tz, _ = trazas(tmp_path, [q(T0, TY, 0.12, 0.20)], motores(ks=(2,)), nombre="k2.csv.gz")
    assert tz[0][3] == 100
    E = D.construir_motores((1,), ("CONS",), bn=False, placebos=True)
    tz, _ = trazas(tmp_path, [q(T0, TY, 0.11, 0.20)], E, nombre="j.csv.gz")
    assert [n for n, *_ in tz] == ["JOIN|C0|CONS|5", "IMPROVE|C0|CONS|5"] or [n for n, *_ in tz] == ["JOIN|C0|CONS|5"]


def test_bid_subcentavo_baja_al_centavo_inferior_sin_mejorar(tmp_path):
    mo = D.DeepMotor(motores(ks=(1, 2)), S.Externas(), D.Ladders())
    assert mo._objetivo(255, 1) == 250 and mo._objetivo(255, 2) == 240
    assert mo._objetivo(250, 1) == 240 and mo._objetivo(110, 2) == 90 - 0 or mo._objetivo(110, 2) is None
    assert mo._objetivo(120, 2) == 100 and mo._objetivo(110, 1) == 100


# ---------------------------------------------------------------- repegado
def test_repega_cuando_cambia_el_top_cancelacion_y_alta_nueva(tmp_path):
    L = [q(T0, TY, 0.25, 0.30), q(T0 + 1000, TY, 0.27, 0.30), q(T0 + 2000, TY, 0.27, 0.30, bsz=11.0)]
    tz, mo = trazas(tmp_path, L)
    assert [(p) for _, _, _, p, _ in tz] == [240, 260]       # sin tercer alta: mismo top
    assert tz[1][2] == T0 + 1000
    p = unidad(mo, DK1)
    assert p.norders == 2
    segs = sorted(p.segs, key=lambda g: g.dec)
    assert segs[0].ceff == T0 + 1000 + S.LAT_CANCEL_MS        # la vieja sigue expuesta hasta la cancelación efectiva (+60)
    assert segs[1].act == T0 + 1000 + S.LAT_POST_MS           # alta nueva +68


def test_cambio_de_top_durante_el_bloqueo_en_vuelo_se_atiende_con_la_siguiente_foto(tmp_path):
    L = [q(T0, TY, 0.25, 0.30), q(T0 + 30, TY, 0.27, 0.30), q(T0 + 200, TY, 0.27, 0.30, bsz=12.0)]
    tz, _ = trazas(tmp_path, L)
    assert [(p, t) for _, _, t, p, _ in tz] == [(240, T0), (260, T0 + 200)]   # a T0+30 la orden estaba en vuelo (lock 68 ms)


def test_la_orden_vieja_rellena_hasta_su_cancelacion_efectiva_pero_no_despues(tmp_path):
    L = [q(T0, TY, 0.25, 0.30), q(T0 + 1000, TY, 0.27, 0.30),
         tr(T0 + 1030, TY, 0.23, "SELL", 50.0)]               # recibido a T0+1050 < ceff T0+1060: aún rellena a 0,24
    mo = correr(tmp_path, L)
    assert unidad(mo, DK1).lleno == pytest.approx(5.0)
    assert unidad(mo, DK1).coste == pytest.approx(5 * 0.24)
    L = [q(T0, TY, 0.25, 0.30), q(T0 + 1000, TY, 0.27, 0.30), tr(T0 + 1090, TY, 0.20, "SELL", 50.0)]   # recibido a T0+1110: la vieja ya no
    mo = correr(tmp_path, L, nombre="b.csv.gz")
    p = unidad(mo, DK1)
    assert p.lleno == pytest.approx(5.0) and p.coste == pytest.approx(5 * 0.26)    # rellena la nueva (0,26 > 0,20: la barrida la atraviesa)


def test_deep_fijo_no_repega_ni_se_cancela_al_moverse_el_top(tmp_path):
    E = D.construir_motores((1,), ("CONS",), bn=False, placebos=True)
    L = [q(T0, TY, 0.25, 0.30), q(T0 + 1000, TY, 0.27, 0.30), q(T0 + 2000, TY, 0.35, 0.40)]
    tz, mo = trazas(tmp_path, L, E)
    fijo = [(p, t) for n, _, t, p, _ in tz if n.startswith("DEEPFIJO")]
    assert fijo == [(240, T0)]
    deep = [p for n, _, _, p, _ in tz if n == DK1]
    assert deep == [240, 260]
    assert unidad(mo, "DEEPFIJO_k1|C0|CONS|5").ncap == 0


def test_parada_a_t_60s_no_rellena_despues(tmp_path):
    t_fin = FIN - 59_000                                      # T = 59 s (después de la parada efectiva a T=60 s + 60 ms)
    L = [q(T0, TY, 0.25, 0.30), q(FIN - 120_000, TY, 0.25, 0.30, bsz=10.5), tr(t_fin, TY, 0.20, "SELL", 50.0)]
    assert unidad(correr(tmp_path, L), DK1).lleno == 0.0


# ---------------------------------------------------------------- relleno conservador y cola
def test_barrida_por_debajo_rellena_completo_aun_con_cola_desconocida_cons(tmp_path):
    L = [q(T0, TY, 0.25, 0.30), tr(T0 + 200, TY, 0.23, "SELL", 1.0)]
    p = unidad(correr(tmp_path, L), DK1)
    assert p.lleno == pytest.approx(5.0)


def test_cola_desconocida_cons_no_rellena_al_igualar_pero_opt_cola_cero_si(tmp_path):
    E = motores(colas=("CONS", "OPT"))
    L = [q(T0, TY, 0.25, 0.30), tr(T0 + 200, TY, 0.24, "SELL", 4.0)]
    mo = correr(tmp_path, L, E)
    assert unidad(mo, DK1).lleno == 0.0
    assert unidad(mo, DK1O).lleno == pytest.approx(4.0)
    assert fila(mo, DK1)["cola_desc"] == 1 and fila(mo, DK1)["cola_con"] == 0
    assert mo.st["cola_desconocida|" + DK1] == 1


def test_cola_conocida_por_el_espejo_del_contrario_solo_se_rellena_al_superarla(tmp_path):
    lad = ladders(lrow(T0 - 10, TN, [(0.75, 10.0), (0.76, 7.0), (0.77, 3.0)]))     # YES bid 0,24 = NO ask 0,76: cola 7
    L = [q(T0, TY, 0.25, 0.30),
         tr(T0 + 200, TY, 0.24, "SELL", 4.0),               # vol 4 < 7
         tr(T0 + 300, TY, 0.24, "SELL", 4.0)]               # vol 8 -> 1 por encima de la cola
    mo = correr(tmp_path, L, lad=lad)
    p = unidad(mo, DK1)
    assert p.lleno == pytest.approx(1.0)
    assert fila(mo, DK1)["cola_con"] == 1 and fila(mo, DK1)["cola_desc"] == 0


def test_escalon_vacio_conocido_cola_cero_y_compra_del_contrario_por_acunacion(tmp_path):
    lad = ladders(lrow(T0 - 10, TN, [(0.75, 10.0), (0.77, 3.0), (0.80, 9.0)]))     # 0,76 ausente: vacío conocido
    L = [q(T0, TY, 0.25, 0.30), tr(T0 + 200, TN, 0.76, "BUY", 3.0)]                 # BUY de NO a 0,76 = SELL YES a 0,24
    p = unidad(correr(tmp_path, L, lad=lad), DK1)
    assert p.lleno == pytest.approx(3.0)


def test_la_cola_se_lee_a_la_hora_del_alta_no_de_la_decision(tmp_path):
    lad = ladders(lrow(T0 - 10, TN, [(0.75, 10.0), (0.76, 7.0)]), lrow(T0 + 40, TN, [(0.75, 10.0), (0.76, 20.0)]))   # entran 13 antes de que lleguemos
    L = [q(T0, TY, 0.25, 0.30), tr(T0 + 300, TY, 0.24, "SELL", 15.0)]               # 15 < 20: no rellena (con cola 7 sí)
    assert unidad(correr(tmp_path, L, lad=lad), DK1).lleno == 0.0


def test_cola_opt_adelanta_por_cancelaciones_no_explicadas(tmp_path):
    E = motores(colas=("CONS", "OPT"))
    lad = ladders(lrow(T0 - 10, TN, [(0.75, 10.0), (0.76, 10.0)]), lrow(T0 + 500, TN, [(0.75, 10.0), (0.76, 4.0)]))   # se cancelan 6 (sin operaciones)
    L = [q(T0, TY, 0.25, 0.30), q(T0 + 600, TY, 0.25, 0.30, bsz=10.5), tr(T0 + 900, TY, 0.24, "SELL", 5.0)]
    mo = correr(tmp_path, L, E, lad)
    assert unidad(mo, DK1).lleno == 0.0                      # CONS: cola 10 -> 5 < 10
    assert unidad(mo, DK1O).lleno > 0.0                      # OPT: cola 10, adelanta 6*(10/10) = 6 -> cola 4 -> 1 por encima


# ---------------------------------------------------------------- brazo secundario Binance
def ext_con(ticks, coin="BTC"):
    e = S.Externas()
    t = np.array([x[0] for x in ticks], dtype=np.int64)
    p = np.array([x[1] for x in ticks], dtype=np.float64)
    e.x[coin] = (t, p)
    return e


def test_brazo_bn_solo_cotiza_con_binance_en_contra_y_cancela_si_deja_de_cumplirse(tmp_path):
    E = D.construir_motores((1,), ("CONS",), bn=True, bn_w=(1000,), bn_bps=3.0, placebos=False)
    nombre_bn = [e.nombre for e in E if e.fam == "DEEPBN"][0]
    # Binance cae 5 bps entre T0-1000 y T0 (en contra del YES); luego queda plano
    ext = ext_con([(T0 - 1500, 100000.0), (T0 - 900, 100000.0), (T0 - 10, 99950.0), (T0 + 5000, 99950.0), (T0 + 9000, 99950.0)])
    L = [q(T0, TY, 0.25, 0.30), q(T0 + 5000, TY, 0.26, 0.30), q(T0 + 12000, TY, 0.26, 0.30)] + ka(T0 - 500, T0 + 20000)
    tz, mo = trazas(tmp_path, L, E, ext=ext)
    bn = [(t, p) for n, _, t, p, _ in tz if n == nombre_bn]
    assert bn == [(T0, 240)]                                  # cotiza en la primera decisión; a T0+5000 el movimiento ya no está en la ventana
    assert unidad(mo, nombre_bn).ncap == 1                     # y se cancela por condición
    # el DEEP normal sí repega
    assert [p for n, _, _, p, _ in tz if n == DK1] == [240, 250]


def test_brazo_bn_lado_no_exige_subida_y_sin_datos_no_cotiza(tmp_path):
    E = D.construir_motores((1,), ("CONS",), bn=True, bn_w=(1000,), bn_bps=3.0, placebos=False)
    nombre_bn = [e.nombre for e in E if e.fam == "DEEPBN"][0]
    sube = ext_con([(T0 - 1500, 100000.0), (T0 - 10, 100050.0)])
    L = [q(T0, TY, 0.25, 0.30), q(T0, TN, 0.25, 0.30)] + ka(T0 - 500, T0 + 3000)
    tz, _ = trazas(tmp_path, L, E, ext=sube)
    assert {(tk) for n, tk, *_ in tz if n == nombre_bn} == {TN}                # sube: amenaza al NO, no al YES
    tz, _ = trazas(tmp_path, L, E, ext=S.Externas(), nombre="sd.csv.gz")                 # sin datos de Binance: no cotiza (a prueba de fallos)
    assert [n for n, *_ in tz if n == nombre_bn] == []


def test_brazo_bn_no_mira_el_futuro(tmp_path):
    E = D.construir_motores((1,), ("CONS",), bn=True, bn_w=(1000,), bn_bps=3.0, placebos=False)
    nombre_bn = [e.nombre for e in E if e.fam == "DEEPBN"][0]
    ext = ext_con([(T0 - 1500, 100000.0), (T0 + 50, 99900.0)])                    # el movimiento llega 50 ms DESPUÉS de la decisión
    L = [q(T0, TY, 0.25, 0.30)] + ka(T0 - 500, T0 + 3000)
    tz, _ = trazas(tmp_path, L, E, ext=ext)
    assert [n for n, *_ in tz if n == nombre_bn] == []


# ---------------------------------------------------------------- H38 markout
def test_markout_a_5_30_120_s_por_recepcion_y_missing_pasado_el_cierre(tmp_path):
    L = [q(T0, TY, 0.25, 0.30), tr(T0 + 200, TY, 0.23, "SELL", 50.0),               # relleno de 5 a 0,24 en T0+200 (recepción +20)
         q(T0 + 3000, TY, 0.30, 0.32), q(T0 + 10_000, TY, 0.40, 0.44)]               # mid 0,31 a +5 s? la foto vigente a T+5s es la de T0+3000
    L += [q(T0 + 31_000, TY, 0.50, 0.52), q(T0 + 125_000, TY, 0.60, 0.62)] + ka(T0, T0 + 140_000, 4000)
    mo = correr(tmp_path, srt(L))
    r = fila(mo, DK1)
    assert r["lleno"] == pytest.approx(5.0) and r["nfills"] == 1
    # relleno a t = T0+220 (recepción del print); +5 s = T0+5220 -> foto vigente: la de T0+3000 (mid 0,31); +30 s -> T0+10_000 (mid 0,42)
    assert r["mo5_n"] == 1 and r["mo5_pnl"] == pytest.approx(5 * (0.31 - 0.24))
    assert r["mo30_n"] == 1 and r["mo30_pnl"] == pytest.approx(5 * (0.42 - 0.24))
    assert r["mo120_n"] == 1 and r["mo120_pnl"] == pytest.approx(5 * (0.51 - 0.24))
    assert r["mo5_cost"] == pytest.approx(5 * 0.24)


def test_markout_pasado_el_cierre_es_missing_no_cero(tmp_path):
    t = FIN - 100_000                                                                  # relleno a T = 100 s: +120 s cae tras el cierre
    L = [q(T0, TY, 0.25, 0.30), q(t - 10_000, TY, 0.25, 0.30, bsz=10.5), tr(t, TY, 0.23, "SELL", 50.0), q(t + 10_000, TY, 0.40, 0.44)]
    L += ka(T0, FIN, 4000) + [q(FIN - 5000, TY, 0.60, 0.62)]
    r = fila(correr(tmp_path, srt(L)), DK1)
    assert r["lleno"] == pytest.approx(5.0)
    assert r["mo120_n"] == 0 and r["mo120_miss"] == 1 and r["mo120_cost"] == 0.0
    assert r["mo5_n"] == 1


# ---------------------------------------------------------------- H37 salida maker
def _fill_y(extra, motor_args=None):
    return [q(T0, TY, 0.25, 0.30), tr(T0 + 200, TY, 0.23, "SELL", 50.0)] + extra      # relleno 5 @0,24 en T0+220


def test_salida_se_llena_si_un_comprador_barre_el_ask_a_entrada_mas_delta(tmp_path):
    # tras el relleno el top cae: bid 0,22 ask 0,26. Salida 0,25 < ask -> mejora el ask, cola 0. BUY de YES a 0,25 de 5 en T0+3000.
    L = _fill_y([q(T0 + 250, TY, 0.22, 0.26), tr(T0 + 3000, TY, 0.25, "BUY", 5.0)])
    mo = correr(tmp_path, L)
    r = fila(mo, DK1)
    assert r["x10_n"] == 1 and r["x10_fq"] == pytest.approx(5.0)
    assert r["x10_pnl"] == pytest.approx(5 * 0.01)
    assert r["x10_cost"] == pytest.approx(5 * 0.24)
    assert r["x20_n"] == 1 and r["x20_fq"] == 0.0                                       # δ=0,02 (0,26 = ask): cola por delante, sin volumen
    assert r["x10_capm"] < r["capm"]                                                    # recicla capital: menos $·min inmovilizados


def test_salida_expira_a_los_10_s_y_se_mantiene_a_resolucion(tmp_path):
    L = _fill_y([q(T0 + 250, TY, 0.22, 0.26), tr(T0 + 12_000, TY, 0.25, "BUY", 5.0)])   # llega tras la ventana de 10 s
    r = fila(correr(tmp_path, L), DK1)
    assert r["x10_n"] == 1 and r["x10_fq"] == 0.0


def test_salida_que_cruzaria_el_bid_no_se_pone(tmp_path):
    L = _fill_y([q(T0 + 250, TY, 0.26, 0.28)])                                          # bid 0,26 >= 0,25: ejecutaría como tomador
    mo = correr(tmp_path, L)
    r = fila(mo, DK1)
    assert r["x10_n"] == 0 and mo.st["salida_cruza_o_fuera"] >= 1


def test_salida_al_ask_del_libro_necesita_superar_la_cola_del_nivel(tmp_path):
    L = _fill_y([q(T0 + 250, TY, 0.22, 0.25, bsz=10.0, asz=8.0), tr(T0 + 3000, TY, 0.25, "BUY", 5.0), tr(T0 + 3500, TY, 0.25, "BUY", 5.0)])
    r = fila(correr(tmp_path, L), DK1)
    assert r["x10_fq"] == pytest.approx(2.0)                                            # cola 8: 10 de volumen -> 2 por encima


def test_salida_desconocida_cons_no_rellena_en_el_nivel_y_opt_si(tmp_path):
    E = motores(colas=("CONS", "OPT"))
    L = _fill_y([q(T0 + 250, TY, 0.22, 0.24), tr(T0 + 3000, TY, 0.25, "BUY", 5.0)])      # ask 0,24 < 0,25: nivel 0,25 más profundo, sin fila l
    mo = correr(tmp_path, L, E)
    assert fila(mo, DK1)["x10_fq"] == 0.0 and fila(mo, DK1O)["x10_fq"] == pytest.approx(5.0)


# ---------------------------------------------------------------- regresión: JOIN/IMPROVE idénticos a la versión base
def test_join_e_improve_reproducen_el_simulador_base(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=10.0), tr(T0 + 200, TY, 0.20, "SELL", 4.0), tr(T0 + 300, TY, 0.20, "SELL", 8.0),
         q(T0 + 2000, TY, 0.22, 0.27, bsz=5.0), q(T0 + 2500, TY, 0.22, 0.27, bsz=3.0), tr(T0 + 3000, TY, 0.21, "SELL", 2.0),
         q(T0 + 4000, TY, 0.35, 0.40), q(T0 + 6000, TY, 0.18, 0.23, bsz=7.0), tr(T0 + 7000, TN, 0.82, "BUY", 20.0)] + ka(T0, T0 + 9000, 4000)
    f = fichero(tmp_path, k_lines() + L, "r.csv.gz")
    base = S.procesar_registro(f, S.Externas(), S.construir_motores(("JOIN", "IMPROVE"), ("CONS", "OPT"), (), {"C0"}, placebo=False), 0)
    nuevo = D.procesar_registro(f, S.Externas(), D.Ladders(), D.construir_motores((), ("CONS", "OPT"), bn=False, placebos=True), 0)
    comp = ("JOIN|C0|CONS|5", "JOIN|C0|OPT|5", "IMPROVE|C0|CONS|5")
    A = {(p.e.nombre, p.tk): (p.lleno, p.coste, p.norders, p.ncap, round(p.reb, 9)) for p in base.pos_ant if p.e.nombre in comp}
    B = {(p.e.nombre, p.tk): (p.lleno, p.coste, p.norders, p.ncap, round(p.reb, 9)) for p in nuevo.pos_ant if p.e.nombre in comp}
    assert A and A == B


# ---------------------------------------------------------------- orquestación: caché durable, idempotencia, coberturas
def test_correr_dia_cache_valida_unicidad_y_corrupcion(tmp_path, monkeypatch):
    vol = tmp_path / "vol"
    (vol / "m5_registro").mkdir(parents=True)
    dia = "2026-10-14"
    f = vol / "m5_registro" / f"m5_registro_{dia}.csv.gz"
    L = [q(T0, TY, 0.25, 0.30), tr(T0 + 200, TY, 0.23, "SELL", 50.0)] + ka(T0, T0 + 30_000, 4000)
    with gzip.open(f, "wt") as fh:
        fh.write("tipo\n")
        for ln in k_lines() + L:
            fh.write(ln if ln.endswith("\n") else ln + "\n")
    monkeypatch.setattr(S, "VOL", vol)
    out = tmp_path / "out"
    out.mkdir()
    eng = motores(ks=(1,), colas=("CONS", "OPT"))
    args = argparse.Namespace(monedas="", recorte_min=0, max_lineas=0, max_lineas_ext=0, dirs_l=str(tmp_path / "nada"), deltas_t=D.DELTAS)
    logs = []
    des = lambda mids: {m: "YES" for m in mids}      # noqa: E731
    est, filas, *_ = D.correr_dia(dia, eng, out, args, logs.append, des_fn=des)
    assert est["estado"] == "COMPLETO" and est["cobertura_des"] == 1.0
    ph = D.params_hash(eng, D.DELTAS)
    assert D.cache_valida(out, dia, ph)["filas"] == len(filas)
    assert D.cache_valida(out, dia, "otro") is None                                    # parámetros distintos: se recalcula
    est2, filas2, *_ = D.correr_dia(dia, eng, out, args, logs.append, des_fn=des)       # reanudar = mismo resultado, sin duplicar
    assert [r["lleno"] for r in filas2] == [r["lleno"] for r in filas]
    import pandas as pd
    U = D.cargar_unidades([dia], out)
    assert not U.duplicated(["dia", "motor", "mkt", "lado", "tramo"]).any()
    assert U.pnl.sum() == pytest.approx(sum((r["lleno"] - r["coste"]) for r in filas))  # una sola vez el pago de resolución
    with gzip.open(out / f"unidades_{dia}.csv.gz", "ab") as fh:                        # corrupción
        fh.write(b"basura")
    assert D.cache_valida(out, dia, ph) is None
    assert pd is not None


def test_cobertura_baja_no_cachea(tmp_path, monkeypatch):
    vol = tmp_path / "vol"
    (vol / "m5_registro").mkdir(parents=True)
    dia = "2026-10-14"
    with gzip.open(vol / "m5_registro" / f"m5_registro_{dia}.csv.gz", "wt") as fh:
        for ln in k_lines() + [q(T0, TY, 0.25, 0.30), tr(T0 + 200, TY, 0.23, "SELL", 50.0)] + ka(T0, T0 + 30_000, 4000):
            fh.write(ln if ln.endswith("\n") else ln + "\n")
    monkeypatch.setattr(S, "VOL", vol)
    out = tmp_path / "o"
    out.mkdir()
    args = argparse.Namespace(monedas="", recorte_min=0, max_lineas=0, max_lineas_ext=0, dirs_l=str(tmp_path / "x"), deltas_t=D.DELTAS)
    est, *_ = D.correr_dia(dia, motores(), out, args, lambda *_: None, des_fn=lambda mids: {})
    assert est["estado"] == "COBERTURA_DES_BAJA" and not (out / f"unidades_{dia}.csv").exists() and not (out / f"unidades_{dia}.csv.gz").exists()


def test_filtro_de_monedas_ignora_las_demas(tmp_path):
    f = fichero(tmp_path, k_lines("ETH") + [q(T0, TY, 0.25, 0.30)], "e.csv.gz")
    mo = D.procesar_registro(f, S.Externas(), D.Ladders(), motores(), 0, monedas={"BTC"})
    assert not mo.pos_ant and not mo.meta


# ---------------------------------------------------------------- estadística
def _df(rows):
    import pandas as pd
    return pd.DataFrame(rows, columns=["dia", "mkt", "pnl", "coste", "fin_s", "rebate"])


def test_ic90_cierre_agrupa_monedas_del_mismo_cierre_y_ev_sin_top5():
    rows = [("d1", f"m{i}", 1.0 if i < 6 else -0.5, 1.0, 100 + i // 2, 0.0) for i in range(12)]
    F = _df(rows)
    lo, hi = D.ic90_cierre(F)
    assert lo == lo and hi == hi and lo <= F.pnl.sum() / F.coste.sum() <= hi
    assert D.ev_sin_top_mercados(F, 5) == pytest.approx((1.0 - 0.5 * 6) / 7)


def test_gates_exigen_todo():
    F = _df([(f"d{i % 6}", f"m{i}", 0.3, 1.0, 1000 + i, 0.0) for i in range(60)])
    F["lleno"] = 5.0
    for h in D.MARK_S:
        F[f"mo{h}_pnl"], F[f"mo{h}_cost"], F[f"mo{h}_n"], F[f"mo{h}_miss"] = 0.1, 1.0, 1, 0
    m = D.met(F, 6)
    g = D.gates(m, 6)
    assert all(g.values()), g
    F2 = F.copy()
    F2["mo30_pnl"] = -0.1
    assert D.gates(D.met(F2, 6), 6)["markout30>0"] is False
    assert D.gates(D.met(F, 6), 3)["días+>=4/6"] is False                                # con menos de 6 días de OOS no se da por cumplido


def test_equivalencia_en_flujo_consistente(tmp_path):
    L = []
    for t in range(T0, T0 + 200_000, 1000):
        L.append(q(t, TY, 0.25, 0.30, bsz=10.0))
        L.append(lrow(t + 5, TN, [(0.75, 10.0), (0.76, 7.0), (0.77, 3.0)]))
    f = fichero(tmp_path, k_lines() + L, "eq.csv.gz")
    res, txt = D.equivalencia([f])
    assert res["quieto_n"] > 10 and res["quieto_precio_ok"] == res["quieto_n"] and res["quieto_tam_ok"] == res["quieto_n"]
    assert "100.00%" in txt


def test_manifiesto_y_humo_via_main_no_escriben_cache(tmp_path, monkeypatch, capsys):
    vol = tmp_path / "vol"
    (vol / "m5_registro").mkdir(parents=True)
    dia = "2026-10-14"
    with gzip.open(vol / "m5_registro" / f"m5_registro_{dia}.csv.gz", "wt") as fh:
        for ln in k_lines() + [q(T0, TY, 0.25, 0.30), tr(T0 + 200, TY, 0.23, "SELL", 50.0)] + ka(T0, T0 + 30_000, 4000):
            fh.write(ln if ln.endswith("\n") else ln + "\n")
    monkeypatch.setattr(S, "VOL", vol)
    out = tmp_path / "o"
    cache = tmp_path / "cache.json"
    cache.write_text(json.dumps({}))
    monkeypatch.setattr(S, "desenlaces_oficiales", lambda mids: {m: "YES" for m in mids})
    rc = D.main(["--dias", dia, "--out", str(out), "--recorte-min", "1", "--sin-bn", "--dirs-l", str(tmp_path / "nada")])
    assert rc == 0
    man = json.loads((out / "run_manifest.json").read_text())
    assert man["estado"] == "HUMO" and man["dias"][dia]["estado"] == "HUMO_NO_CACHEADO"
    assert not list(out.glob("unidades_*"))
    assert "HUMO" in capsys.readouterr().out


def _dia_sintetico(vol, dia, fill=True):
    (vol / "m5_registro").mkdir(parents=True, exist_ok=True)
    L = [q(T0, TY, 0.25, 0.30), tr(T0 + 200, TY, 0.23 if fill else 0.27, "SELL", 50.0),
         q(T0 + 250, TY, 0.22, 0.26), tr(T0 + 3000, TY, 0.25, "BUY", 5.0)]
    L = srt(L + ka(FIN - 300_500, FIN + 500, 4000))
    with gzip.open(vol / "m5_registro" / f"m5_registro_{dia}.csv.gz", "wt") as fh:
        for ln in k_lines() + L:
            fh.write(ln if ln.endswith("\n") else ln + "\n")


def test_informe_completo_sobre_cachés_sintéticas_recorre_todas_las_secciones(tmp_path, monkeypatch):
    vol = tmp_path / "vol"
    out = tmp_path / "out"
    out.mkdir()
    dias = ["2026-10-05", "2026-10-06", "2026-10-14", "2026-10-15"]
    monkeypatch.setattr(S, "VOL", vol)
    monkeypatch.setattr(D, "MIN_FILL_COIN", 1)
    monkeypatch.setattr(D, "MIN_FILL_ALL", 1)
    eng = D.construir_motores((1, 2), ("CONS", "OPT"), bn=False, placebos=True)
    args = argparse.Namespace(monedas="", recorte_min=0, max_lineas=0, max_lineas_ext=0, dirs_l=str(tmp_path / "x"), deltas_t=D.DELTAS)
    for d in dias:
        _dia_sintetico(vol, d)
        est, *_ = D.correr_dia(d, eng, out, args, lambda *_: None, des_fn=lambda mids: {m: "YES" for m in mids})
        assert est["estado"] == "COMPLETO"
    txt, res = D.informe(out, dias)
    for sec in ("== 0. COLA", "== 1. ELECCIÓN DE k EN DESC", "== 2. OOS", "placebo DEEP_FIJO", "placebo JOIN", "placebo IMPROVE", "H37 salida maker",
                "== 4. TODOS LOS MOTORES", "== 5. H38 MARKOUT"):
        assert sec in txt, sec
    assert res["seleccion_desc"]["BTC"]["k"] in (1, 2)
    assert "DEEP_k" in txt and "gates:" in txt
    # la elección usa SOLO DESC: cambiar el OOS no cambia el k elegido
    sel1 = res["seleccion_desc"]["BTC"]["motor"]
    txt2, res2 = D.informe(out, ["2026-10-05", "2026-10-06", "2026-10-14"])
    assert res2["seleccion_desc"]["BTC"]["motor"] == sel1


def test_dias_excluidos_11_13_no_son_ni_desc_ni_oos(tmp_path, monkeypatch):
    vol = tmp_path / "vol"
    out = tmp_path / "out"
    out.mkdir()
    monkeypatch.setattr(S, "VOL", vol)
    eng = D.construir_motores((1,), ("CONS",), bn=False, placebos=False)
    args = argparse.Namespace(monedas="", recorte_min=0, max_lineas=0, max_lineas_ext=0, dirs_l=str(tmp_path / "x"), deltas_t=D.DELTAS)
    _dia_sintetico(vol, "2026-10-12")
    D.correr_dia("2026-10-12", eng, out, args, lambda *_: None, des_fn=lambda mids: {m: "YES" for m in mids})
    txt, res = D.informe(out, ["2026-10-12"])
    assert "DESC=[]" in txt and "OOS (>= 2026-10-14)=[]" in txt and "excluidos del hallazgo (descriptivo, no cuentan)=['2026-10-12']" in txt
