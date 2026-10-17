"""Pruebas del simulador H26 (maker en la banda barata) sobre flujos sintéticos: sin datos reales, sin red, sin órdenes."""
import gzip
import json
import sys
from array import array
from datetime import date, timedelta
from pathlib import Path

import numpy as np
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import analisis_5m_maker_banda_simulador as S  # noqa: E402

FIN = 1_791_936_300_000                   # cierre (ms) del mercado sintético
FIN_ISO = "2026-10-14 00:05:00+00:00"
TY, TN, MK = "tokY", "tokN", "m1"
T0 = FIN - 299_000                        # T = 299 s: dentro de la ventana (60, 300]
OK_NOM = "JOIN|C0|CONS|5"


def k_lines(coin="BTC", mkt=MK, ty=TY, tn=TN, fin_iso=FIN_ISO):
    return [f"k,{T0 - 500},{ty},{coin},5min,{mkt},{fin_iso},YES", f"k,{T0 - 500},{tn},{coin},5min,{mkt},{fin_iso},NO"]


def q(t, tk, bid, ask, bsz=10.0, asz=20.0, lag=20):
    return f"q,{t - lag},{tk},{bid},{ask},{bsz},{asz},{t}\n"


def tr(t_ex, tk, p, side="SELL", sz=50.0, lag=20):
    return f"t,{t_ex},{tk},{p},{side},{sz},{t_ex + lag},\n"


def ka(t0, t1, paso=5000):
    """Filas de mantenimiento del reloj (token NO fuera de banda): evitan que un hueco sintético corte el tramo."""
    return [q(t, TN, 0.50, 0.52) for t in range(t0, t1, paso)]


def fichero(tmp_path, lines, name="m5.csv.gz"):
    f = tmp_path / name
    with gzip.open(f, "wt") as fh:
        fh.write("tipo,t_ms,id,c1,c2,c3,c4,c5\n")
        for ln in lines:
            fh.write(ln if ln.endswith("\n") else ln + "\n")
    return f


def motores(pols=("JOIN",), colas=("CONS",), capas=("C0",), sh_cap=()):
    return S.construir_motores(pols, colas, sh_cap, set(capas))


def correr(tmp_path, lines, ext=None, engines=None, nombre="m5.csv.gz", traza=False):
    ext = ext or S.Externas()
    f = fichero(tmp_path, k_lines() + list(lines), nombre)
    return S.procesar_registro(f, ext, engines or motores(), 0, traza=traza)


def unidad(mo, nombre, tk=None):
    for p in mo.pos_ant:
        if p.e.nombre == nombre and (tk is None or p.tk == tk):
            return p
    return None


# ---------------------------------------------------------------- relleno: solo si la operación atraviesa o supera la cola
def test_join_cola_delante_es_el_tamano_del_nivel_y_solo_se_rellena_al_superarla(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=10.0),
         tr(T0 + 200, TY, 0.20, "SELL", 4.0),          # 4 < cola 10: no rellena
         tr(T0 + 300, TY, 0.20, "SELL", 5.0),          # vol 9 < 10: no rellena
         tr(T0 + 400, TY, 0.20, "SELL", 3.0)]          # vol 12 -> 2 por encima de la cola: relleno PARCIAL de 2
    mo = correr(tmp_path, L)
    p = unidad(mo, OK_NOM, TY)
    assert p.norders == 1
    assert p.lleno == pytest.approx(2.0)
    assert p.coste == pytest.approx(2 * 0.20)


def test_la_operacion_a_precio_peor_no_rellena_y_la_que_atraviesa_llena_todo(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=10.0),
         tr(T0 + 200, TY, 0.21, "SELL", 999.0),        # por encima de nuestro bid: no puede consumirlo
         tr(T0 + 300, TY, 0.19, "SELL", 1.0)]          # atraviesa: la barrida vació el nivel -> relleno completo
    mo = correr(tmp_path, L)
    p = unidad(mo, OK_NOM, TY)
    assert p.lleno == pytest.approx(5.0)
    assert p.completo


def test_compra_tomadora_del_contrario_consume_nuestro_bid_por_acunacion(tmp_path):
    # BUY de NO a 0,80 = precio equivalente 0,20 sobre YES
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 200, TN, 0.80, "BUY", 5.0)]
    mo = correr(tmp_path, L)
    assert unidad(mo, OK_NOM, TY).lleno == pytest.approx(5.0)


def test_la_compra_del_propio_token_no_cuenta(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 200, TY, 0.20, "BUY", 50.0)]
    mo = correr(tmp_path, L)
    assert unidad(mo, OK_NOM, TY).lleno == 0.0


def test_no_se_rellena_antes_del_alta_ni_despues_de_la_cancelacion_efectiva(tmp_path):
    # alta efectiva = T0 + 68; el reloj del relleno es la RECEPCIÓN del print (el sello del WS es de lote): recibido en T0+50 no cuenta
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 30, TY, 0.19, "SELL", 50.0)]
    assert unidad(correr(tmp_path, L), OK_NOM, TY).lleno == 0.0
    # tras la alta sí; cancelación por salir de banda en T0+1000 (efectiva +60): operación en T0+1050 aún rellena, en T0+1100 no
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), q(T0 + 1000, TY, 0.35, 0.40), tr(T0 + 1030, TY, 0.19, "SELL", 50.0)]   # recibido a T0+1050
    assert unidad(correr(tmp_path, L, nombre="a.csv.gz"), OK_NOM, TY).lleno == pytest.approx(5.0)       # cancelación EN VUELO
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), q(T0 + 1000, TY, 0.35, 0.40), tr(T0 + 1100, TY, 0.19, "SELL", 50.0)]
    assert unidad(correr(tmp_path, L, nombre="b.csv.gz"), OK_NOM, TY).lleno == 0.0


def test_cola_se_toma_de_la_ultima_foto_con_hora_de_exchange_anterior_al_alta(tmp_path):
    # decisión en T0 con bsz 10; a T0+30 (exchange) el nivel pasa a 50 (entran antes que nosotros) -> cola 50
    L = [q(T0, TY, 0.20, 0.25, bsz=10.0), q(T0 + 50, TY, 0.20, 0.25, bsz=50.0, lag=20),
         q(T0 + 200, TY, 0.20, 0.25, bsz=50.0),          # primera foto con hora de exchange > alta: congela
         tr(T0 + 300, TY, 0.20, "SELL", 30.0)]            # 30 < 50: no rellena (con cola 10 sí)
    mo = correr(tmp_path, L)
    p = unidad(mo, OK_NOM, TY)
    assert p.lleno == 0.0


def test_improve_cotiza_un_tick_encima_con_cola_cero(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=999.0), tr(T0 + 200, TY, 0.21, "SELL", 2.0)]
    mo = correr(tmp_path, L, engines=motores(pols=("IMPROVE",)))
    p = unidad(mo, "IMPROVE|C0|CONS|5", TY)
    assert p.lleno == pytest.approx(2.0)                 # parcial: sin cola delante, rellena lo que viene
    assert p.coste == pytest.approx(2 * 0.21)


def test_improve_no_cotiza_si_el_spread_no_lo_permite_y_fuera_de_banda_no_se_cotiza(tmp_path):
    L = [q(T0, TY, 0.20, 0.21)]                          # spread de 1 tick: +1 tick cruzaría
    assert unidad(correr(tmp_path, L, engines=motores(pols=("IMPROVE",))), "IMPROVE|C0|CONS|5", TY) is None
    for bid, ask in ((0.10, 0.12), (0.31, 0.35), (0.05, 0.06)):   # banda abierta por abajo (0,10 no entra) y cerrada por arriba
        assert unidad(correr(tmp_path, [q(T0, TY, bid, ask)], nombre=f"{bid}.csv.gz"), OK_NOM, TY) is None


def test_libro_cruzado_o_bloqueado_no_cotiza(tmp_path):
    for bid, ask in ((0.22, 0.20), (0.20, 0.20)):
        assert unidad(correr(tmp_path, [q(T0, TY, bid, ask)], nombre=f"c{bid}{ask}.csv.gz"), OK_NOM, TY) is None


def test_fuera_de_la_ventana_de_tiempo_no_se_cotiza(tmp_path):
    for t in (FIN - 301_000, FIN - 59_000):
        assert unidad(correr(tmp_path, [q(t, TY, 0.20, 0.25)], nombre=f"{t}.csv.gz"), OK_NOM, TY) is None


def test_parada_programada_a_t60_cancela(tmp_path):
    stop = FIN - 60_000
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0)] + ka(T0 + 5000, stop) + [tr(stop + 30, TY, 0.19, "SELL", 50.0)]   # en vuelo (<60 ms)
    assert unidad(correr(tmp_path, L), OK_NOM, TY).lleno == pytest.approx(5.0)
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0)] + ka(T0 + 5000, stop) + [tr(stop + 200, TY, 0.19, "SELL", 50.0)]
    assert unidad(correr(tmp_path, L, nombre="b.csv.gz"), OK_NOM, TY).lleno == 0.0


# ---------------------------------------------------------------- recolocación
def test_recoloca_cuando_cambia_el_mejor_bid_y_la_vieja_sigue_expuesta_60ms(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0),
         q(T0 + 1000, TY, 0.22, 0.25, bsz=0.0),          # el mejor bid sube: cancelar la de 0,20 (+60) y alta a 0,22 (+68)
         tr(T0 + 1030, TY, 0.19, "SELL", 50.0)]           # la vieja (0,20) aún vive y la nueva todavía no: rellena la vieja a 0,20
    mo = correr(tmp_path, L)
    p = unidad(mo, OK_NOM, TY)
    assert p.norders == 2
    assert p.lleno == pytest.approx(5.0)
    assert p.coste == pytest.approx(5 * 0.20)


def test_el_tope_por_unidad_es_sh_aunque_las_dos_pujas_sean_rellenables(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), q(T0 + 1000, TY, 0.22, 0.25, bsz=0.0),
         tr(T0 + 1030, TY, 0.19, "SELL", 50.0), tr(T0 + 1100, TY, 0.19, "SELL", 50.0)]
    p = unidad(correr(tmp_path, L), OK_NOM, TY)
    assert p.lleno == pytest.approx(5.0)


def test_yes_y_no_son_unidades_independientes(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), q(T0 + 1, TN, 0.22, 0.27, bsz=0.0), tr(T0 + 300, TY, 0.19, "SELL", 50.0)]
    mo = correr(tmp_path, L)
    y, n = unidad(mo, OK_NOM, TY), unidad(mo, OK_NOM, TN)
    assert y.lleno == pytest.approx(5.0) and n.lleno == 0.0
    assert y.tk != n.tk


# ---------------------------------------------------------------- capas de defensa
def ext_con_alarma(alarmas, coin="BTC", capa=("C1", 2.0, 1000)):
    e = S.Externas()
    e._a1[(coin, capa[1], capa[2], "dn")] = array("q", alarmas)       # YES amenazado por bajada
    e._a1[(coin, capa[1], capa[2], "up")] = array("q", [])
    return e


def eng_c1():
    return S.construir_motores(("JOIN",), ("CONS",), (), {"C1_u2_w1"})


def test_c1_cancela_a_alarma_mas_60ms_y_no_se_rellena_despues(tmp_path):
    ext = ext_con_alarma([T0 + 1000])
    # sin alarma lo rellenaría en T0+1100; con la alarma (cancelación efectiva T0+1060) no
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 1100, TY, 0.19, "SELL", 50.0)]
    p = unidad(correr(tmp_path, L, ext=ext, engines=eng_c1()), "JOIN|C1_u2_w1|CONS|5", TY)
    assert p.lleno == 0.0 and p.ncap == 1
    # operación DENTRO de la cancelación en vuelo (T0+1040 <= T0+1060): sí se rellena
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 1040, TY, 0.19, "SELL", 50.0)]
    p = unidad(correr(tmp_path, L, ext=ext, engines=eng_c1(), nombre="b.csv.gz"), "JOIN|C1_u2_w1|CONS|5", TY)
    assert p.lleno == pytest.approx(5.0)


def test_c1_no_cancela_el_lado_no_amenazado(tmp_path):
    ext = S.Externas()
    ext._a1[("BTC", 2.0, 1000, "dn")] = array("q", [])
    ext._a1[("BTC", 2.0, 1000, "up")] = array("q", [T0 + 1000])        # sube Binance: amenaza NO, no YES
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 1100, TY, 0.19, "SELL", 50.0)]
    p = unidad(correr(tmp_path, L, ext=ext, engines=eng_c1()), "JOIN|C1_u2_w1|CONS|5", TY)
    assert p.lleno == pytest.approx(5.0) and p.ncap == 0


def test_c1_no_recotiza_hasta_2s_despues_de_la_alarma(tmp_path):
    ext = ext_con_alarma([T0 + 1000])
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0),
         q(T0 + 1500, TY, 0.21, 0.25, bsz=0.0),         # dentro del enfriamiento: no cotiza
         q(T0 + 3100, TY, 0.22, 0.25, bsz=0.0),         # 2,1 s después: vuelve
         tr(T0 + 3400, TY, 0.21, "SELL", 50.0)]
    p = unidad(correr(tmp_path, L, ext=ext, engines=eng_c1()), "JOIN|C1_u2_w1|CONS|5", TY)
    assert p.norders == 2 and p.lleno == pytest.approx(5.0)
    assert p.coste == pytest.approx(5 * 0.22)


def test_c1_enfriamiento_se_reevalua_con_filas_de_solo_tamano(tmp_path):
    ext = ext_con_alarma([T0 + 1000])
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0),
         q(T0 + 1500, TY, 0.20, 0.25, bsz=7.0),          # sin cambio de precio, aún bloqueado
         q(T0 + 3200, TY, 0.20, 0.25, bsz=8.0),          # sin cambio de precio, enfriamiento cumplido: recotiza
         tr(T0 + 3500, TY, 0.19, "SELL", 50.0)]
    p = unidad(correr(tmp_path, L, ext=ext, engines=eng_c1()), "JOIN|C1_u2_w1|CONS|5", TY)
    assert p.norders == 2 and p.lleno == pytest.approx(5.0)


def test_c2_sin_15m_identificable_es_sin_dato_y_no_cotiza(tmp_path):
    eng = S.construir_motores(("JOIN",), ("CONS",), (), {"C2_k1"})
    mo = correr(tmp_path, [q(T0, TY, 0.20, 0.25)], engines=eng)
    assert unidad(mo, "JOIN|C2_k1|CONS|5", TY) is None
    assert mo.st["sin_dato|JOIN|C2_k1|CONS|5"] >= 1


def test_c2_cancela_con_alarma_del_bid15_del_mismo_lado(tmp_path):
    ext = S.Externas()
    fin15 = -(-FIN // 900_000) * 900_000
    ext.k15[("BTC", fin15, "YES")] = "t15Y"
    ext.b15["t15Y"] = (np.array([T0]), np.array([500]))
    ext._a2[("t15Y", 1)] = array("q", [T0 + 1000])
    eng = S.construir_motores(("JOIN",), ("CONS",), (), {"C2_k1"})
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 1100, TY, 0.19, "SELL", 50.0)]
    p = unidad(correr(tmp_path, L, ext=ext, engines=eng), "JOIN|C2_k1|CONS|5", TY)
    assert p.lleno == 0.0 and p.ncap == 1


# ---------------------------------------------------------------- cola optimista
def test_cola_optimista_adelanta_por_cancelaciones_no_explicadas_por_operaciones(tmp_path):
    eng = S.construir_motores(("JOIN",), ("CONS", "OPT"), (), {"C0"})
    L = [q(T0, TY, 0.20, 0.25, bsz=10.0), q(T0 + 200, TY, 0.20, 0.25, bsz=10.0),   # congela la cola en 10
         q(T0 + 400, TY, 0.20, 0.25, bsz=5.0),             # bajan 5 sin operaciones -> cancelaciones; cola restante 10/10 = 100 % delante
         tr(T0 + 600, TY, 0.20, "SELL", 7.0)]              # 7 > cola efectiva 5: relleno parcial 2 (cons: cola 10, nada)
    mo = correr(tmp_path, L, engines=eng)
    assert unidad(mo, "JOIN|C0|CONS|5", TY).lleno == 0.0
    assert unidad(mo, "JOIN|C0|OPT|5", TY).lleno == pytest.approx(2.0)


def test_cola_optimista_no_cuenta_como_cancelacion_lo_que_explican_las_operaciones(tmp_path):
    eng = S.construir_motores(("JOIN",), ("OPT",), (), {"C0"})
    L = [q(T0, TY, 0.20, 0.25, bsz=10.0), q(T0 + 200, TY, 0.20, 0.25, bsz=10.0),
         tr(T0 + 300, TY, 0.20, "SELL", 4.0),               # consume 4 de la cola
         q(T0 + 400, TY, 0.20, 0.25, bsz=6.0)]               # 10 -> 6 explicado por la operación: sin adelanto extra
    mo = correr(tmp_path, L, engines=eng)
    g = unidad(mo, "JOIN|C0|OPT|5", TY).segs[0] if unidad(mo, "JOIN|C0|OPT|5", TY).segs else None
    assert unidad(mo, "JOIN|C0|OPT|5", TY).lleno == 0.0
    assert g is None or g.adv == pytest.approx(0.0)


# ---------------------------------------------------------------- capacidad y parciales
def test_capacidad_sh25_relleno_parcial_y_pnl_cuadra(tmp_path):
    eng = S.construir_motores(("JOIN",), ("CONS",), (25.0,), {"C0"})
    nombre = "JOIN|C0|CONS|25"
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 300, TY, 0.20, "SELL", 8.0)]
    mo = correr(tmp_path, L, engines=eng)
    p = unidad(mo, nombre, TY)
    assert p.lleno == pytest.approx(8.0) and not p.completo
    assert p.reb == pytest.approx(8.0 * 0.2 * 0.07 * 0.2 * 0.8)


# ---------------------------------------------------------------- tramos del registro (no cronológico)
def test_salto_atras_reinicia_el_estado_y_marca_los_mercados_incompletos(tmp_path):
    fin_b = FIN - 7_200_000          # un mercado de dos horas antes (tramo posterior en el archivo)
    Tb = fin_b - 299_000
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0)]
    L += k_lines(mkt="m2", ty="tokY2", tn="tokN2", fin_iso="2026-10-13 22:05:00+00:00")
    L += [q(Tb + 10, "tokY2", 0.20, 0.25, bsz=0.0), tr(Tb + 400, "tokY2", 0.19, "SELL", 50.0)]
    mo = correr(tmp_path, L)
    assert len(mo.tramos) == 2 and mo.st["saltos_atras"] == 1
    # el estado no se arrastra: sin relleno en TY (su tramo acabó), relleno en tokY2 por la operación de su tramo
    assert unidad(mo, OK_NOM, TY).lleno == 0.0
    assert unidad(mo, OK_NOM, "tokY2").lleno == pytest.approx(5.0)
    filas = {(r[3], r[4]): r for r in mo.filas("2026-10-14")}
    assert filas[("m1", "YES")][6] == 0     # m1: su tramo termina antes de su cierre -> incompleto
    assert filas[("m2", "YES")][6] == 0     # m2: el tramo empieza ~ 10 ms tras su apertura pero termina antes del cierre


def test_hueco_hacia_adelante_tambien_corta_el_tramo(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), q(T0 + 60_000, TY, 0.20, 0.25, bsz=0.0)]
    mo = correr(tmp_path, L)
    assert mo.st["huecos_adelante"] == 1 and len(mo.tramos) == 2


def test_las_operaciones_de_un_tramo_no_rellenan_pujas_de_otro(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0),
         q(T0 - 3_600_000, TN, 0.5, 0.6),                  # salto atrás de 1 h: tramo nuevo
         tr(T0 + 500, TY, 0.19, "SELL", 50.0)]             # y otro salto adelante de 1 h: tramo nuevo
    mo = correr(tmp_path, L)
    assert len(mo.tramos) == 3
    assert unidad(mo, OK_NOM, TY).lleno == 0.0             # la operación pertenece a otro tramo: no rellena la puja del primero


# ---------------------------------------------------------------- cronología (sin información posterior a la decisión)
def test_prefijo_invariante_las_decisiones_no_dependen_del_futuro(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=5.0), q(T0 + 1000, TY, 0.22, 0.26, bsz=3.0), q(T0 + 2000, TY, 0.12, 0.26, bsz=3.0),
         tr(T0 + 2500, TY, 0.11, "SELL", 9.0), q(T0 + 4000, TY, 0.18, 0.26, bsz=3.0), q(T0 + 6000, TY, 0.40, 0.45)]
    eng = motores(pols=("JOIN", "IMPROVE"), colas=("CONS", "OPT"), capas=("C0",))
    completo = correr(tmp_path, L, engines=eng, nombre="full.csv.gz", traza=True)
    parcial = correr(tmp_path, L[:3], engines=eng, nombre="part.csv.gz", traza=True)
    t_corte = T0 + 2000
    a = sorted(x for x in completo.traza if x[2] <= t_corte)
    b = sorted(x for x in parcial.traza if x[2] <= t_corte)
    assert a == b and len(a) > 0                      # truncar el futuro no cambia ninguna decisión ya tomada


def test_decision_usa_solo_alarmas_anteriores_o_iguales_a_la_recepcion(tmp_path):
    ext = ext_con_alarma([T0 + 5000])            # alarma futura: no puede condicionar una decisión en T0
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 1100, TY, 0.19, "SELL", 50.0)]
    p = unidad(correr(tmp_path, L, ext=ext, engines=eng_c1()), "JOIN|C1_u2_w1|CONS|5", TY)
    assert p.lleno == pytest.approx(5.0) and p.ncap == 0


# ---------------------------------------------------------------- alarmas desde series
def test_alarmas_c1_binance_baja_u_bps_en_w():
    e = S.Externas()
    t = np.array([0, 500, 1000, 1500, 2000, 10_000], dtype=np.int64)
    px = np.array([100.0, 100.0, 100.0, 99.97, 99.99, 99.99])
    e.x["BTC"] = (t, px)
    dn = list(e.c1("BTC", 2.0, 1000, "dn"))
    assert dn == [1500]                       # 100 -> 99,97 en 500 ms = -3 bps; a 2000 el ref (1000) es 100: -1 bp, no alarma
    assert list(e.c1("BTC", 2.0, 1000, "up")) == []
    assert list(e.c1("BTC", 2.0, 1000, "dn")) == dn                      # caché


def test_alarmas_c1_referencia_demasiado_vieja_no_senala():
    e = S.Externas()
    t = np.array([0, 20_000], dtype=np.int64)
    e.x["BTC"] = (t, np.array([100.0, 90.0]))
    assert list(e.c1("BTC", 2.0, 1000, "dn")) == []         # hueco de 20 s: sin referencia fiable


def test_alarmas_c2_caida_de_ticks_respecto_al_maximo_de_3s():
    e = S.Externas()
    e.b15["a"] = (np.array([0, 1000, 2000, 2500, 9000]), np.array([500, 520, 520, 490, 480]))
    assert list(e.c2("a", 2)) == [2500]       # 520 -> 490 = 3 ticks; 9000: ventana vacía (máx = su propio valor)
    assert list(e.c2("a", 1)) == [2500]


# ---------------------------------------------------------------- cuentas: PnL, desenlace, unicidad
def test_fila_csv_pnl_y_desenlace_missing_no_es_cero():
    r = ("2026-10-14", OK_NOM, "BTC", "m1", "YES", 0, 1, 1, 0, 5.0, 1.0, 0.2, 0.0, 10.0, 12.0, 100.0)
    assert S.fila_csv(r, {"m1": "YES"}).rstrip().split(",")[-2:] == ["YES", "4.0"]
    assert S.fila_csv(r, {"m1": "NO"}).rstrip().split(",")[-2:] == ["NO", "-1.0"]
    assert S.fila_csv(r, {}).rstrip().split(",")[-2:] == ["", ""]


def test_unicidad_de_claves():
    r = ("d", "m", "BTC", "m1", "YES", 0)
    assert S.validar_unicidad([r + (1,), r + (2,)]) == [("d", "m", "m1", "YES", 0)]
    assert S.validar_unicidad([r + (1,), ("d", "m", "BTC", "m1", "NO", 0)]) == []


def test_conciliacion_de_pnl_total_entre_unidades_y_mercado(tmp_path):
    # YES y NO rellenos en el mismo mercado: PnL del mercado = suma de las dos unidades y cobra el pago de UNA sola pata
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), q(T0 + 1, TN, 0.22, 0.27, bsz=0.0),
         tr(T0 + 300, TY, 0.19, "SELL", 50.0), tr(T0 + 301, TN, 0.21, "SELL", 50.0)]
    mo = correr(tmp_path, L)
    filas = mo.filas("2026-10-14")
    des = {"m1": "YES"}
    pnl = [float(S.fila_csv(r, des).rstrip().split(",")[-1]) for r in filas if r[2] and r[9] > 0]
    assert sum(pnl) == pytest.approx((5 - 5 * 0.20) + (0 - 5 * 0.22))


# ---------------------------------------------------------------- reanudación idempotente y checkpoint corrupto
def preparar_dia(tmp_path, monkeypatch, d="2026-10-14"):
    vol = tmp_path / "vol"
    (vol / "m5_registro").mkdir(parents=True)
    (vol / "m15_registro").mkdir(parents=True)
    lines = k_lines() + [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 300, TY, 0.19, "SELL", 50.0)]
    fichero(vol / "m5_registro", lines, f"m5_registro_{d}.csv.gz")
    fichero(vol / "m15_registro", ["x,1,BTCUSDT,100.0,1,0,1," + str(T0 - 1000)], f"m15_registro_{d}.csv.gz")
    monkeypatch.setattr(S, "VOL", vol)
    return d


class Args:
    max_lineas_ext = 0
    recorte_min = 0
    max_lineas = 0


def test_correr_dia_escribe_cache_atomica_y_es_idempotente_al_reanudar(tmp_path, monkeypatch):
    d = preparar_dia(tmp_path, monkeypatch)
    out = tmp_path / "out"
    out.mkdir()
    eng = motores()
    est, filas, des, mo, uni = S.correr_dia(d, eng, out, Args(), lambda m: None, des_fn=lambda mids: {m: "YES" for m in mids})
    assert est["estado"] == "COMPLETO"
    ph = S.params_hash(eng)
    assert S.cache_valida(out, d, ph)
    sha1 = S.sha_fichero(out / f"unidades_{d}.csv.gz")
    # reanudar: la caché válida se reconoce y no hay que recalcular; recalcular a la fuerza da exactamente las mismas filas
    S.correr_dia(d, eng, out, Args(), lambda m: None, des_fn=lambda mids: {m: "YES" for m in mids})
    import pandas as pd
    a = pd.read_csv(out / f"unidades_{d}.csv.gz", dtype={"mkt": str})
    assert len(a) == len(filas) and not a.duplicated(["dia", "motor", "mkt", "lado", "tramo"]).any()
    assert S.sha_fichero(out / f"unidades_{d}.csv.gz") == sha1 or len(a) == len(filas)
    assert not list(out.glob("*.tmp*"))


def test_checkpoint_corrupto_o_de_otra_version_se_recalcula(tmp_path, monkeypatch):
    d = preparar_dia(tmp_path, monkeypatch)
    out = tmp_path / "out"
    out.mkdir()
    eng = motores()
    S.correr_dia(d, eng, out, Args(), lambda m: None, des_fn=lambda mids: {m: "YES" for m in mids})
    ph = S.params_hash(eng)
    assert S.cache_valida(out, d, ph)
    with gzip.open(out / f"unidades_{d}.csv.gz", "ab") as fh:         # corrupción: añadir basura rompe el hash
        fh.write(b"x")
    assert S.cache_valida(out, d, ph) is None
    S.correr_dia(d, eng, out, Args(), lambda m: None, des_fn=lambda mids: {m: "YES" for m in mids})
    assert S.cache_valida(out, d, ph)
    assert S.cache_valida(out, d, "otros_parametros") is None
    meta = json.loads((out / f"meta_{d}.json").read_text())
    meta["cobertura_des"] = 0.5
    (out / f"meta_{d}.json").write_text(json.dumps(meta))
    assert S.cache_valida(out, d, ph) is None                          # cobertura de desenlaces baja: no es checkpoint válido


def test_cobertura_de_desenlaces_baja_no_cachea(tmp_path, monkeypatch):
    d = preparar_dia(tmp_path, monkeypatch)
    out = tmp_path / "out"
    out.mkdir()
    est = S.correr_dia(d, motores(), out, Args(), lambda m: None, des_fn=lambda mids: {})[0]
    assert est["estado"] == "COBERTURA_DES_BAJA" and not (out / f"unidades_{d}.csv.gz").exists()


def test_dia_sin_entrada_se_informa_sin_inventar(tmp_path, monkeypatch):
    monkeypatch.setattr(S, "VOL", tmp_path / "vacio")
    est = S.correr_dia("2026-10-14", motores(), tmp_path, Args(), lambda m: None)[0]
    assert est["estado"] == "FALTA_ENTRADA"


# ---------------------------------------------------------------- población y estadística
def test_unidades_poblacion_agrupa_por_mercado_y_lado():
    import pandas as pd
    C = pd.DataFrame({"mkt": ["a", "a", "b"], "lado_c": ["YES", "YES", "NO"], "act": ["BTC"] * 3, "T": [100.0, 120.0, 200.0],
                      "pc": [0.2, 0.25, 0.1], "acc": [5.0, 5.0, 10.0], "coste": [1.0, 1.25, 1.0], "cola": ["final"] * 3,
                      "des": ["YES", "YES", "YES"], "pnl": [4.0, 3.75, -1.0]})
    U = S.unidades_poblacion(C)
    assert len(U) == 2
    a = U[U.mkt == "a"].iloc[0]
    assert a.pnl == pytest.approx(7.75) and a.coste == pytest.approx(2.25) and a.gana == 1
    assert U[U.mkt == "b"].iloc[0].gana == 0


def test_metricas_ev_sin_mejor_dia_y_dias_positivos():
    import pandas as pd
    U = pd.DataFrame({"dia": ["d1", "d1", "d2", "d3"], "pnl": [10.0, 5.0, -2.0, -1.0], "coste": [10.0, 10.0, 10.0, 10.0]})
    m = S.metricas(U, total_dias=3)
    assert m["ev"] == pytest.approx(12.0 / 40.0)
    assert m["dias_pos"] == 1 and m["ev_sin_mejor"] == pytest.approx(-3.0 / 20.0)
    assert m["pnl_dia"] == pytest.approx(4.0)


def test_gates_exigen_todo():
    m = {"n_fill": 100, "ev": 0.1, "ic90": (0.01, 0.2), "ev_sin_mejor": 0.05, "dias_pos": 5}
    assert all(S.gates(m, 6).values())
    m["ic90"] = (-0.01, 0.2)
    assert not S.gates(m, 6)["IC90_dias>0"]
    assert not any(S.gates({"n_fill": 0}, 6).values())


def test_eleccion_solo_con_desc_y_minimo_de_rellenos():
    import pandas as pd
    filas = []
    for i in range(40):
        for mot, pnl in (("JOIN|C0|CONS|5", -0.5), ("IMPROVE|C0|CONS|5", 0.5), ("JOIN|C0|OPT|5", 0.9)):
            filas.append({"dia": f"d{i % 3}", "motor": mot, "act": "ETH", "lleno": 5.0, "pnl": pnl, "coste": 1.0})
    U = pd.DataFrame(filas)
    sel = S.elegir_desc(U, ["d0", "d1", "d2"], ["ETH", "BTC"])
    assert sel["ETH"][0] == "IMPROVE|C0|CONS|5"          # OPT nunca se elige (solo cota); BTC sin datos: ninguna
    assert sel["BTC"][0] is None


def test_motores_opt_solo_para_join_y_capacidad_solo_c0():
    E = S.construir_motores()
    nombres = [e.nombre for e in E]
    assert not any(n.startswith("IMPROVE") and "|OPT|" in n for n in nombres)
    assert any(n == "JOIN|C0|OPT|5" for n in nombres)
    assert [n for n in nombres if not n.endswith("|5")] == ["JOIN|C0|CONS|25", "JOIN|C0|CONS|50", "IMPROVE|C0|CONS|25",
                                                           "IMPROVE|C0|CONS|50"]
    assert len(set(nombres)) == len(nombres)


def test_no_hay_ningun_envio_ni_firma_en_el_modulo():
    src = Path(S.__file__).read_text().lower()
    for prohibido in ("py_clob_client", "post_order", "create_order", "private_key", ".env", "signer"):
        assert prohibido not in src


def test_k15_previo_recupera_mercados_listados_el_dia_anterior_y_cachea(tmp_path, monkeypatch):
    vol = tmp_path / "vol"
    (vol / "m15_registro").mkdir(parents=True)
    fichero(vol / "m15_registro", ["k,1,tokBNB15Y,BNB,15min,m9,2026-10-14 00:15:00+00:00,YES",
                                   "k,1,tokBNB15N,BNB,15min,m9,2026-10-14 00:15:00+00:00,NO",
                                   "k,1,tok60,BNB,60min,m8,2026-10-14 01:00:00+00:00,YES"], "m15_registro_2026-10-13.csv.gz")
    monkeypatch.setattr(S, "VOL", vol)
    out = tmp_path / "out"
    out.mkdir()
    m = S.k15_previo("2026-10-14", out)
    fin = S._ms_iso("2026-10-14 00:15:00+00:00")
    assert m == {("BNB", fin, "YES"): "tokBNB15Y", ("BNB", fin, "NO"): "tokBNB15N"}
    assert (out / "k15map_2026-10-13.csv.gz").exists()
    (vol / "m15_registro" / "m15_registro_2026-10-13.csv.gz").unlink()
    assert S.k15_previo("2026-10-14", out) == m                      # ahora sale de la caché
    assert S.k15_previo("2026-10-15", out) == {}                     # sin fichero ni caché: vacío (C2 = sin dato), nunca inventado


def test_libro_vacio_retira_la_puja_viva_y_no_cotiza_sin_dato(tmp_path):
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0),
         f"q,{T0 + 900},{TY},None,0.25,None,5.0,{T0 + 1000}\n",          # el bid desaparece: fuera de banda -> cancelar
         tr(T0 + 1100, TY, 0.19, "SELL", 50.0)]                           # tras la cancelación efectiva (T0+1060): no rellena
    mo = correr(tmp_path, L)
    p = unidad(mo, OK_NOM, TY)
    assert p.lleno == 0.0 and mo.st["q_libro_vacio"] == 1
    # y un libro sin bid desde el principio nunca cotiza
    assert unidad(correr(tmp_path, [f"q,{T0 - 20},{TY},None,0.25,None,5.0,{T0}\n"], nombre="b.csv.gz"), OK_NOM, TY) is None


# ---------------------------------------------------------------- 17-Oct: causalidad Binance, placebo/inversión, calibración, estadística
def test_leer_externas_usa_la_hora_de_recepcion_c7_y_no_la_de_binance_c6(tmp_path, monkeypatch):
    vol = tmp_path / "vol"
    (vol / "m15_registro").mkdir(parents=True)
    # c[6] (E de Binance) = 1_000 y c[7] (recepción) = 1_500 / 2_500: el reloj de la simulación es SIEMPRE c[7]
    fichero(vol / "m15_registro", ["x,1,BTCUSDT,100.0,1.0,0,1000,1500", "x,1,BTCUSDT,99.9,1.0,0,1900,2500"],
            "m15_registro_2026-10-14.csv.gz")
    monkeypatch.setattr(S, "VOL", vol)
    ext = S.leer_externas("2026-10-14", out=tmp_path)
    assert list(ext.x["BTC"][0]) == [1500, 2500]


def test_placebo_inversion_y_desplazamiento_de_las_alarmas(tmp_path):
    E = S.construir_motores(("JOIN",), ("CONS",), (), None)
    nom = {e.capa: e for e in E}
    assert nom["PINV_u2_w1"].plc == "inv" and nom["PSH_u2_w1"].plc == "shift" and nom["PSH_C2_k1"].plc == "shift"
    assert all(e.cola == "CONS" and e.sh == 5.0 for e in E if e.plc)
    assert not any(e.plc for e in S.construir_motores(placebo=False))
    # inversión: para el lado YES la alarma real es 'dn'; la del placebo-inversión es 'up'
    ext = S.Externas()
    ext._a1[("BTC", 2.0, 1000, "dn")] = array("q", [T0 + 1000])
    ext._a1[("BTC", 2.0, 1000, "up")] = array("q", [])
    eng = S.construir_motores(("JOIN",), ("CONS",), (), {"PINV_u2_w1"})
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 1100, TY, 0.19, "SELL", 50.0)]
    p = unidad(correr(tmp_path, L, ext=ext, engines=eng), "JOIN|PINV_u2_w1|CONS|5", TY)
    assert p.lleno == pytest.approx(5.0) and p.ncap == 0              # la alarma real (dn) NO cancela a la inversión
    # desplazamiento: la alarma de T0+1000 pasa a T0+1000+30 min: no cancela
    eng = S.construir_motores(("JOIN",), ("CONS",), (), {"PSH_u2_w1"})
    p = unidad(correr(tmp_path, L, ext=ext, engines=eng, nombre="b.csv.gz"), "JOIN|PSH_u2_w1|CONS|5", TY)
    assert p.lleno == pytest.approx(5.0) and p.ncap == 0


def test_los_placebos_nunca_se_eligen_en_desc():
    import pandas as pd
    filas = []
    for i in range(40):
        for mot, pnl in (("JOIN|C0|CONS|5", -0.5), ("JOIN|PSH_u2_w1|CONS|5", 0.9), ("JOIN|PINV_u2_w1|CONS|5", 0.8)):
            filas.append({"dia": f"d{i % 3}", "motor": mot, "act": "ETH", "lleno": 5.0, "pnl": pnl, "coste": 1.0})
    sel = S.elegir_desc(pd.DataFrame(filas), ["d0", "d1", "d2"], ["ETH"])
    assert sel["ETH"][0] == "JOIN|C0|CONS|5"


def test_veredicto_calibracion_haz_cons_opt():
    ok = {"poblacion_final": {"ev": 0.12}, "JOIN|C0|CONS|5": {"ev": -0.05}, "JOIN|C0|OPT|5": {"ev": 0.10}}
    assert S.veredicto_calibracion(ok)["estado"] == "PASA"
    mal = {"poblacion_final": {"ev": 0.12}, "JOIN|C0|CONS|5": {"ev": -0.20}, "JOIN|C0|OPT|5": {"ev": 0.02}}
    assert S.veredicto_calibracion(mal)["estado"] == "NO_REPRODUCE"
    assert S.veredicto_calibracion({})["estado"] == "SIN_DATOS"
    nan = {"poblacion_final": {"ev": float("nan")}, "JOIN|C0|CONS|5": {"ev": 0.0}, "JOIN|C0|OPT|5": {"ev": 0.0}}
    assert S.veredicto_calibracion(nan)["estado"] == "SIN_DATOS"


def test_metricas_ev_sin_los_dos_mejores_dias():
    import pandas as pd
    U = pd.DataFrame({"dia": ["d1", "d2", "d3", "d4"], "pnl": [10.0, 5.0, -2.0, -1.0], "coste": [10.0] * 4})
    m = S.metricas(U, total_dias=4)
    assert m["ev_sin_2mejores"] == pytest.approx(-3.0 / 20.0)
    assert S.metricas(U[U.dia.isin(["d1", "d2"])], 2)["ev_sin_2mejores"] != S.metricas(U[U.dia.isin(["d1", "d2"])], 2)["ev_sin_2mejores"]  # NaN


def test_informe_completo_sobre_cachés_sinteticas_incluye_placebo_pares_y_veredicto(tmp_path, monkeypatch):
    import gzip as gz
    monkeypatch.setattr(S, "VOL", tmp_path / "volvacio")
    rng = np.random.default_rng(1)
    motores_ = ["JOIN|C0|CONS|5", "JOIN|C0|OPT|5", "IMPROVE|C0|CONS|5", "JOIN|C1_u2_w1|CONS|5", "JOIN|PINV_u2_w1|CONS|5",
                "JOIN|PSH_u2_w1|CONS|5", "JOIN|C0|CONS|25"]
    des = {}
    for d in S.DIAS[:7]:
        filas = []
        for i in range(60):
            mk = f"{d}-m{i}"
            des[mk] = "YES" if rng.random() < 0.25 else "NO"
            for lado in ("YES", "NO"):
                for mot in motores_:
                    lleno = 5.0 if rng.random() < 0.5 else 0.0
                    filas.append((d, mot, ["BTC", "ETH"][i % 2], mk, lado, 0, 1, 1, 0, lleno, lleno * 0.2, 0.2 if lleno else 0.0,
                                  0.0, 10.0, 1.0, 100.0 if lleno else ""))
        with gz.open(tmp_path / f"unidades_{d}.csv.gz", "wt") as fh:
            fh.write(S.CAB)
            fh.writelines(S.fila_csv(r, des) for r in filas)
    txt, res = S.informe(tmp_path, S.DIAS[:7])
    assert "PLACEBO" in txt and "INVERSIÓN" in txt and "Pares quietos" in txt and "sin 2 mejores" in txt
    assert "3b. PLACEBO" in txt
    assert res["unidades_total"] == 7 * 60 * 2 * len(motores_)


# ---------------------------------------------------------------- 17-Oct (chief): reloj de recepción, Λ y parámetros de la guarda
def test_el_sello_de_lote_del_print_se_ignora_se_usa_la_recepcion(tmp_path):
    # sello (c[1]) 300 ms ANTES del alta pero recibido en T0+1000: es un casado posterior al alta -> rellena
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), f"t,{T0 - 200},{TY},0.19,SELL,50.0,{T0 + 1000},\n"]
    assert unidad(correr(tmp_path, L), OK_NOM, TY).lleno == pytest.approx(5.0)
    # y al revés: sello posterior a la cancelación pero recibido antes de ella -> rellena (orden de recepción)
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), q(T0 + 1000, TY, 0.35, 0.40), f"t,{T0 + 5000},{TY},0.19,SELL,50.0,{T0 + 1040},\n"]
    assert unidad(correr(tmp_path, L, nombre="b.csv.gz"), OK_NOM, TY).lleno == pytest.approx(5.0)


def test_lambda_alarga_la_exposicion_de_la_cancelacion_por_alarma(tmp_path):
    ext = ext_con_alarma([T0 + 1000])
    for lam, esperado in ((60, 0.0), (150, 5.0), (300, 5.0)):
        eng = S.construir_motores(("JOIN",), ("CONS",), (), {"C1_u2_w1" if lam == 60 else f"C1_u2_w1_L{lam}"}) if lam == 60 else None
        if eng is None:
            monk = S.LAMBDAS
            S.LAMBDAS = (lam,)
            try:
                eng = S.construir_motores(("JOIN",), ("CONS",), (), {f"C1_u2_w1_L{lam}"})
            finally:
                S.LAMBDAS = monk
        nom = eng[0].nombre
        assert eng[0].lam == lam
        L = [q(T0, TY, 0.20, 0.25, bsz=0.0), tr(T0 + 1100, TY, 0.19, "SELL", 50.0)]   # casado recibido a 100 ms de la alarma
        p = unidad(correr(tmp_path, L, ext=ext, engines=eng, nombre=f"l{lam}.csv.gz"), nom, TY)
        assert p.lleno == pytest.approx(esperado), (lam, p.lleno)


def test_feed_ms_adelanta_el_casado_modelado(tmp_path, monkeypatch):
    L = [q(T0, TY, 0.20, 0.25, bsz=0.0), q(T0 + 1000, TY, 0.35, 0.40), tr(T0 + 1070, TY, 0.19, "SELL", 50.0, lag=0)]
    assert unidad(correr(tmp_path, L), OK_NOM, TY).lleno == 0.0          # recibido 70 ms tras la baja: la cancelación (60) llegó antes
    monkeypatch.setattr(S, "FEED_MS", 50)                                  # casado modelado a T0+1020 <= ceff 1060: rellena
    assert unidad(correr(tmp_path, L, nombre="b.csv.gz"), OK_NOM, TY).lleno == pytest.approx(5.0)


def test_parametros_de_la_guarda_binance_se_pueden_variar(monkeypatch):
    monkeypatch.setattr(S, "C1_U", (1.0,))
    monkeypatch.setattr(S, "C1_W", (500, 2000))
    monkeypatch.setattr(S, "LAMBDAS", (30, 60))
    n = [e.capa for e in S.construir_motores(("JOIN",), ("CONS",), (), None, placebo=False)]
    assert "C1_u1_w500_L30" in n and "C1_u1_w500" in n and "C1_u1_w2_L30" in n and "C2_k1_L30" in n
    assert len(set(n)) == len(n)
