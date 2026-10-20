#!/usr/bin/env python3
"""Tests de H23-MAKER-V1 (regla + shadow), sin red. Desde este directorio: python3 -m pytest -q test_h23.py"""
import gzip, json, math, os, random, sys, tempfile
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pytest
import h23_regla as R
import h23_shadow as S

C = 1_800_000_000
U5, D5, U15, D15 = "u5", "d5", "u15", "d15"


def ms(T):
    return int((C - T) * 1000)


class Banco:
    """Par BTC 5m/15m sintetico con lado Up (ref15 > ref5). Salida en memoria."""
    def __init__(self, emitidos=None, records=None, lado=True):
        self.rows = []
        self.n = S.Nucleo(self.rows.append, emitidos, records)
        self.p = self.n.nuevo_par(C, {"id": "m5", "up": U5, "down": D5}, {"id": "m15", "up": U15, "down": D15}, ms(350))
        self.libros(320)
        if lado:
            self.n.fijar_lado(self.p, 100.0, 99.9, ms(298))

    def libros(self, T, b5=((0.30, 100.0), (0.29, 50.0)), a5=((0.33, 50.0),), b15=((0.45, 80.0),), a15=((0.47, 80.0),)):
        t = ms(T)
        self.n.on_book(U5, t, [{"price": str(p), "size": str(s)} for p, s in b5], [{"price": str(p), "size": str(s)} for p, s in a5])
        self.n.on_book(D5, t, [{"price": "0.66", "size": "10"}], [{"price": "0.70", "size": "10"}])
        self.n.on_book(U15, t, [{"price": str(p), "size": str(s)} for p, s in b15], [{"price": str(p), "size": str(s)} for p, s in a15])
        self.n.on_book(D15, t, [{"price": "0.50", "size": "10"}], [{"price": "0.54", "size": "10"}])

    def pc(self, T, tk, side, price, size):
        self.n.vivo(self.p, ms(T))
        self.n.on_price_change(ms(T), [{"asset_id": tk, "side": side, "price": str(price), "size": str(size)}])

    def venta(self, T, pc, acc):
        """Un tomador VENDE el token s (U5) a pc: el maker adquiere s a pc."""
        self.n.vivo(self.p, ms(T))
        self.n.on_trade(U5, ms(T), {"price": str(pc), "size": str(acc), "side": "SELL"})

    def tipo(self, t, **kw):
        return [r for r in self.rows if r["tipo"] == t and all(r.get(k) == v for k, v in kw.items())]


# ------------------------------------------------------------------ regla
def test_p_limite_igual_que_v4_congelada():
    sys.path.insert(0, "/root/polymarket-research")
    import vigia_5m_barato_forward as V
    random.seed(1)
    for _ in range(300):
        b = round(random.uniform(0.05, 0.95), 4)
        if abs(b * 100 - round(b * 100)) < 1e-6:
            continue                                   # solo en frontera de rejilla el +1e-9 difiere a proposito
        assert R.p_limite(b, 0.05) == V.p_limite(b), b


def test_querer_casos_limite():
    q = R.querer
    assert q(0.30, 0.33, 0.45, 0.47, 0.05) == 0.30
    assert q(0.30, 0.33, 0.45, 0.44, 0.05) is None            # 15m cruzado
    assert q(0.34, 0.33, 0.45, 0.47, 0.05) is None            # 5m cruzado
    assert q(0.30, 0.30, 0.45, 0.47, 0.05) is None            # bid == ask: no es post-only valido (cand < ask)
    assert q(0.40, 0.42, 0.45, 0.47, 0.05) is None            # cand 0,40 > p_limite(0,45)=0,38
    assert q(0.40, 0.42, 0.45, 0.47, 0.02) == 0.40            # brazo B (0,02): p_limite 0,41
    assert q(0.30, 0.60, 0.45, 0.47, 0.05) is None            # margen de mercado 0,45-0,60-.. < -0,05
    assert q(None, 0.33, 0.45, 0.47, 0.05) is None and q(0.3, 0.33, float("nan"), 0.47, 0.05) is None
    assert q(0.0, 0.01, 0.45, 0.47, 0.05) is None             # cand < 0,01


def test_acciones_y_pnl():
    assert R.acciones(0.50) == 5.0 and R.acciones(0.20) == 10.0 and R.acciones(0.35) == 5.72
    pn = R.pnl_relleno(10, 0.30, True)                          # gana: 10*(1-0,30) + rebate
    assert pn == pytest.approx(7.0 + 0.2 * 0.07 * 0.3 * 0.7 * 10)
    assert R.pnl_relleno(10, 0.30, False) == pytest.approx(-3.0 + 0.2 * 0.07 * 0.3 * 0.7 * 10)


# ------------------------------------------------------------------ shadow
def esc_resumen(b, arm="A", var="join"):
    b.n.cerrar_par("m5", ms(-0.5))
    return b.tipo("relleno_resumen", arm=arm, var=var)[0]["esc"]


def test_puja_join_y_ventana_de_ref():
    b = Banco(lado=False)
    b.libros(250)
    assert not b.tipo("puesto")                                # sin lado (ref5 no ha llegado): no cotiza
    b.n.fijar_lado(b.p, 100.0, 99.9, ms(249))
    pu = b.tipo("puesto", arm="A", var="join")
    assert len(pu) == 1 and pu[0]["precio"] == 0.30 and pu[0]["depth"] == 100.0 and pu[0]["lado"] == "Up"
    assert len(b.tipo("puesto", arm="B", var="join")) == 1 and len(b.tipo("puesto", var="nc")) == 2


def test_gap_menor_de_1bp_descarta_el_par():
    b = Banco(lado=False)
    b.n.fijar_lado(b.p, 100.0, 99.9995, ms(298))              # 0,5 bp
    b.libros(250)
    assert not b.tipo("puesto") and b.tipo("par")[0]["descartado"] == "gap<min"


def test_relleno_respeta_cola_y_latencia():
    b = Banco()
    b.libros(250)                                               # puja a T=250 con 100 acc delante (depth)
    t0 = ms(250)
    b.venta(250 - 0.050, 0.30, 100)                            # a +50 ms: aun no esta la orden (alta 79)
    b.venta(250 - 0.100, 0.30, 100)                            # a +100 ms: consume lo de delante (cons) / 50 de base / nada de opt
    b.venta(250 - 0.300, 0.30, 4)
    r = esc_resumen(b)
    NEED = R.acciones(0.30)                                    # 6,67 acc
    assert r["opt|c"]["acc"] == pytest.approx(NEED)            # opt: nada delante -> el print de +100 ms la completa
    assert r["base|c"]["acc"] == pytest.approx(NEED)           # base: 50 delante, el print de 100 deja 50 -> la completa
    assert r["cons|c"]["acc"] == pytest.approx(4.0)            # cons: 100 delante, el de 100 las consume, luego solo llegan 4
    assert r["opt|k"]["acc"] == pytest.approx(4.0)             # latencia 254 ms: el print de +100 ms no cuenta, el de +300 ms si


def test_print_que_atraviesa_el_nivel_barre():
    b = Banco()
    b.libros(250)
    b.venta(249.5, 0.29, 1)                                     # precio < nuestro nivel: barrido completo (prioridad de precio)
    r = esc_resumen(b)
    assert all(r[e]["acc"] == pytest.approx(R.acciones(0.30)) for e in ("opt|c", "base|c", "cons|c"))


def cancel_por_desplome(b):
    """bid15 cae de 0,45 a 0,36: p_limite(0,36)=0,29 < 0,30 -> cota_cae; la cancelacion llega a +60 ms."""
    b.libros(250)
    b.n.vivo(b.p, ms(240))
    b.n.on_price_change(ms(240), [{"asset_id": U15, "side": "BUY", "price": "0.45", "size": "0"},     # un solo mensaje del feed
                                  {"asset_id": U15, "side": "BUY", "price": "0.36", "size": "80"}])
    return b


def test_cancela_por_cota_y_las_ventas_tras_la_cancelacion_no_cuentan():
    b = cancel_por_desplome(Banco())
    ca = b.tipo("cancela", arm="A", var="join")
    assert len(ca) == 1 and ca[0]["causa"] == "cota_cae" and ca[0]["precio"] == 0.30 and ca[0]["eff"]["c"] == ms(240) + 60
    b.venta(240 - 0.030, 0.30, 100)                            # +30 ms de la decision de cancelar: aun vivia -> cuenta (central)
    b.venta(240 - 0.200, 0.30, 100)                            # +200 ms: ya cancelada (60) y tambien (150) -> no cuenta
    r = esc_resumen(b)
    assert r["opt|c"]["acc"] == pytest.approx(R.acciones(0.30))
    nc = b.tipo("relleno_resumen", arm="A", var="nc")[0]["esc"]   # el control SIN cancelar si se rellena con el print tardio
    assert nc["opt|c"]["acc"] == pytest.approx(R.acciones(0.30))
    assert r["opt|c"]["acc"] == pytest.approx(R.acciones(0.30)) and r["opt|c"]["n"] == 1


def test_causa_desplome_del_bid_propio_y_reposicion():
    b = Banco()
    b.libros(250)
    b.pc(245, U5, "BUY", 0.30, 0)                              # se va el nivel 0,30 -> el mejor bid pasa a 0,29
    ca = b.tipo("cancela", arm="A", var="join")
    assert ca and ca[0]["causa"] == "bid5_baja"
    pu = b.tipo("puesto", arm="A", var="join")
    assert [x["precio"] for x in pu] == [0.30, 0.29]            # reposicion al nuevo mejor bid (join)


def test_nc_control_no_cancela_nunca():
    b = cancel_por_desplome(Banco())
    b.pc(230, U5, "BUY", 0.30, 0)
    assert not b.tipo("cancela", var="nc") and len(b.tipo("puesto", var="nc")) == 2     # un solo segmento por brazo


def test_fin_cancela_en_t_fin_exacto_y_no_cotiza_despues():
    b = Banco()
    b.libros(250)
    b.pc(9, U5, "BUY", 0.29, 10)                                # T=9 s: ya pasado C-10 s
    ca = b.tipo("cancela", arm="A", var="join")
    assert ca and ca[0]["causa"] == "fin" and ca[0]["r"] == b.p.t_fin
    assert len(b.tipo("puesto", arm="A", var="join")) == 1


def test_gap_cancela_y_marca_incompleto():
    b = Banco()
    b.libros(250)
    b.n.on_gap(b.p, ms(200), "ConnectionClosed")
    assert b.tipo("cancela", arm="A", var="join")[0]["causa"] == "gap"
    b.n.cerrar_par("m5", ms(-0.5))
    assert b.tipo("mercado_fin")[0]["completo"] is False


def test_sin_vista_por_libro_viejo_cancela_pero_pong_lo_mantiene():
    b = Banco()
    b.libros(250)
    b.n.tick(ms(250) + 2900); assert not b.tipo("cancela")
    b.n.vivo(b.p, ms(250) + 2900)                               # PONG: conexion viva, libro quieto valido
    b.n.tick(ms(250) + 5000); assert not b.tipo("cancela")
    b.n.tick(ms(250) + 9000)                                    # 4 s sin nada, ni PONG: fail-closed
    assert b.tipo("cancela", arm="A", var="join")[0]["causa"] == "sin_libro"


def test_markouts_y_missing():
    b = Banco()
    b.libros(250)
    b.venta(249.5, 0.29, 3)                                     # 1er relleno a T=249,5
    b.pc(244, U5, "BUY", 0.29, 40)
    b.n.tick(ms(244))
    mk = b.tipo("markout", arm="A", var="join", esc="opt|c", h=5)
    assert mk and mk[0]["motivo"] is None and mk[0]["bid"] is not None
    b.n.cerrar_par("m5", ms(-0.5))
    h120 = b.tipo("markout", arm="A", var="join", esc="opt|c", h=120)
    assert h120 and h120[0]["bid"] is None and h120[0]["motivo"] in ("sin_libro_al_vencer", "post_cierre", "sin_libro")   # missing != 0


def test_desenlace_pnl_y_missing():
    b = Banco()
    b.libros(250)
    b.venta(249.5, 0.29, 100)
    b.n.cerrar_par("m5", ms(-0.5))
    assert b.n.on_desenlace("m5", "YES", ms(-30))
    d = b.tipo("desenlace")[0]
    assert d["gana_s"] is True and d["pnl"]["A|join|opt|c"] == pytest.approx(R.pnl_relleno(R.acciones(0.30), 0.30, True), abs=1e-4)
    b2 = Banco(); b2.libros(250); b2.venta(249.5, 0.29, 100); b2.n.cerrar_par("m5", ms(-0.5))
    b2.n.on_desenlace("m5", None, ms(-30), motivo="sin_resolver_6h")
    assert b2.tipo("desenlace")[0]["pnl"]["A|join|opt|c"] is None       # sin desenlace = missing, no 0


def test_reinicio_idempotente_y_log_tolerante():
    b = Banco(); b.libros(250); b.venta(249.5, 0.29, 100); b.n.cerrar_par("m5", ms(-0.5)); b.n.on_desenlace("m5", "NO", ms(-30))
    n0 = len(b.rows)
    with tempfile.TemporaryDirectory() as d:
        dia = S._dia(ms(250))
        with open(os.path.join(d, f"h23_shadow_{dia}.jsonl.gz"), "wb") as f:
            f.write(gzip.compress(("\n".join(json.dumps(r) for r in b.rows) + "\n").encode()))
            f.write(gzip.compress(b'{"k":"x","tipo":"latido"}\n')[:-6])     # miembro final truncado (crash a mitad)
        em, rec = S.restaurar(d, C)
    assert "fin|m5" in em and rec["m5"]["des_emitido"] and rec["m5"]["ganador"] == "NO"
    b2 = Banco(emitidos=set(em), records=rec)
    b2.libros(250); b2.venta(249.5, 0.29, 100); b2.n.cerrar_par("m5", ms(-0.5)); b2.n.on_desenlace("m5", "NO", ms(-30))
    assert not b2.tipo("puesto") and not b2.tipo("desenlace") and not b2.tipo("mercado_fin")   # nada duplicado


def test_tope_de_cotizaciones_por_mercado():
    b = Banco(); b.libros(250)
    for i in range(40):                                         # el bid baila entre 0,30 y 0,29
        b.pc(240 - i * 0.2, U5, "BUY", 0.30, 0 if i % 2 == 0 else 100)
    assert len(b.tipo("puesto", arm="A", var="join")) <= R.CONFIG["max_cotiz_por_mercado"] and b.p.motivos["tope_cotiz"] > 0


# ------------------------------------------------------------------ mutaciones: los tests deben DETECTARLAS
def _detecta(mutacion, prueba):
    mutacion()
    try:
        prueba()
    except (AssertionError, KeyError, IndexError, TypeError):
        return True
    return False


def test_mutacion_sin_condicion_de_cota_se_detecta(monkeypatch):
    monkeypatch.setattr(R, "p_limite", lambda b, u: 0.99)
    with pytest.raises((AssertionError, IndexError, KeyError)):
        test_cancela_por_cota_y_las_ventas_tras_la_cancelacion_no_cuentan()


def test_mutacion_cancelar_nunca_se_detecta(monkeypatch):
    monkeypatch.setattr(S.Nucleo, "_cancelar", lambda self, p, tr, seg, t, causa: None)
    with pytest.raises((AssertionError, IndexError, KeyError)):
        test_cancela_por_cota_y_las_ventas_tras_la_cancelacion_no_cuentan()


def test_mutacion_latencia_de_alta_cero_se_detecta(monkeypatch):
    monkeypatch.setitem(S.LAT, "c", (0, 60))
    with pytest.raises(AssertionError):
        test_relleno_respeta_cola_y_latencia()


def test_mutacion_cola_ignorada_se_detecta(monkeypatch):
    monkeypatch.setitem(R.CONFIG["colas"], "cons", 0.0)
    with pytest.raises(AssertionError):
        test_relleno_respeta_cola_y_latencia()


def test_mutacion_rebate_cero_se_detecta(monkeypatch):
    monkeypatch.setitem(R.CONFIG, "rebate", 0.0)
    with pytest.raises(AssertionError):
        test_acciones_y_pnl()


def test_join_r_espera_1500ms_tras_cancelar_y_join_no():
    b = Banco(); b.libros(250)
    b.pc(245, U5, "BUY", 0.30, 0)                               # desplome del nivel: cancela y el nuevo bid es 0,29
    assert [x["precio"] for x in b.tipo("puesto", arm="A", var="join")] == [0.30, 0.29]
    assert [x["precio"] for x in b.tipo("puesto", arm="A", var="join_r")] == [0.30]       # bloqueada 1,5 s
    b.pc(245 - 1.0, U5, "BUY", 0.29, 51)                        # +1,0 s: sigue bloqueada
    assert len(b.tipo("puesto", arm="A", var="join_r")) == 1
    b.pc(245 - 1.6, U5, "BUY", 0.29, 52)                        # +1,6 s: ya puede
    assert [x["precio"] for x in b.tipo("puesto", arm="A", var="join_r")] == [0.30, 0.29]
    assert b.p.motivos["repost_espera"] >= 1
