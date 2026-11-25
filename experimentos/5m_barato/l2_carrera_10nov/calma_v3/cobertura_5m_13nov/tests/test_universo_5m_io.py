"""universo_5m_io: formato, escritura multi-miembro, lectura tolerante (truncado, conflictos, cambio de dia), pausa 429, retencion."""
import csv, datetime as dt, gzip, os, time
import pytest
import universo_5m_io as U


@pytest.fixture
def d(tmp_path):
    return tmp_path / "u5"


def ev(slug="btc-updown-5m-1794686700", mid="1", outs=("Up", "Down"), toks=("11", "22"), cid=None):
    return {"id": mid, "market": cid or "0xc" + mid, "slug": slug, "question": "q", "assets_ids": list(toks), "outcomes": list(outs),
            "timestamp": "1700000000000"}


def fila(t=None, **k):
    return U.parsear_nuevo(ev(**k), int((t or time.time()) * 1000))


def test_parseo_mapea_por_etiqueta_no_por_posicion():
    f = U.parsear_nuevo(ev(outs=("Down", "Up"), toks=("33", "44")), 1700000000500)
    assert (f["token_up"], f["token_down"], f["activo"], f["marco"], f["cierre_ts"]) == ("44", "33", "BTC", "5m", 1794687000)


@pytest.mark.parametrize("e", [ev(slug="polyv2-btc-updown-5m-1"), ev(slug="hype-updown-5m-1794686700"), ev(slug="btc-above-100k"),
                               ev(toks=("1", "1")), ev(toks=("1",)), ev(outs=("Yes", "No")), ev(mid=""), ev(toks=("a", "b")),
                               ev(cid="dead"), {"slug": "btc-updown-5m-1", "assets_ids": "xx", "outcomes": "yy", "id": "1"}])
def test_parseo_fail_closed(e):
    assert U.parsear_nuevo(e, 1) is None


def test_escribir_leer_multiples_miembros(d):
    U.escribir([fila(mid="1")], d)
    U.escribir([fila(mid="2", slug="eth-updown-5m-1794687000"), fila(mid="3", slug="sol-updown-5m-1794687000")], d)
    mk, st = U.leer(directorio=d)
    assert set(mk) == {"1", "2", "3"} and st["ficheros"] == 1 and st["filas"] == 3 and st["conflictos"] == 0


def test_lectura_sin_directorio_o_fichero_no_falla(d):
    assert U.leer(directorio=d) == ({}, {"ficheros": 0, "filas": 0, "invalidas": 0, "conflictos": 0, "truncados": 0})


def test_fichero_truncado_se_lee_lo_legible(d):
    U.escribir([fila(mid="1")], d)
    U.escribir([fila(mid="2", slug="eth-updown-5m-1794687000")], d)
    p = U.fichero(U.dia_utc(), d)
    b = p.read_bytes()
    p.write_bytes(b[:-7])                                   # ultimo miembro cortado
    mk, st = U.leer(directorio=d)
    assert "1" in mk and st["truncados"] == 1


def test_basura_al_final_y_fichero_vacio(d):
    U.escribir([fila(mid="1")], d)
    p = U.fichero(U.dia_utc(), d)
    p.write_bytes(p.read_bytes() + b"\x1f\x8b\x08basura")
    mk, st = U.leer(directorio=d)
    assert "1" in mk
    p.write_bytes(b"")
    mk, st = U.leer(directorio=d)
    assert mk == {}


def test_conflicto_de_tokens_excluye_el_mercado(d):
    U.escribir([fila(mid="1", toks=("11", "22"))], d)
    U.escribir([fila(mid="1", toks=("11", "99")), fila(mid="2", slug="eth-updown-5m-1794687000")], d)
    mk, st = U.leer(directorio=d)
    assert "1" not in mk and "2" in mk and st["conflictos"] == 1


def test_duplicado_identico_es_inocuo(d):
    U.escribir([fila(mid="1")], d)
    U.escribir([fila(mid="1")], d)
    mk, st = U.leer(directorio=d)
    assert set(mk) == {"1"} and st["conflictos"] == 0


def test_cambio_de_dia_lee_hoy_y_ayer_no_anteayer(d):
    ahora = dt.datetime(2026, 11, 14, 0, 1, tzinfo=dt.timezone.utc).timestamp()
    U.escribir([fila(t=ahora - 3600, mid="ayer", slug="btc-updown-5m-1794700000")], d)           # 23:01 del 13
    U.escribir([fila(t=ahora - 86400 * 2, mid="viejo", slug="btc-updown-5m-1794600000")], d)     # dia 12
    U.escribir([fila(t=ahora + 30, mid="hoy", slug="btc-updown-5m-1794700300")], d)
    mk, _ = U.leer(ahora, d)
    assert set(mk) == {"ayer", "hoy"}


def test_leer_usa_cache_y_ve_lo_nuevo(d):
    U.escribir([fila(mid="1")], d)
    assert set(U.leer(directorio=d)[0]) == {"1"}
    U.escribir([fila(mid="2", slug="eth-updown-5m-1794687000")], d)
    assert set(U.leer(directorio=d)[0]) == {"1", "2"}


def test_pausa_429():
    D = lambda h, m: dt.datetime(2026, 11, 13, h, m, 30, tzinfo=dt.timezone.utc)
    assert U.pausa_tras_429(D(19, 46)) == dt.datetime(2026, 11, 13, 20, 2, tzinfo=dt.timezone.utc).timestamp()
    assert U.pausa_tras_429(D(23, 40)) == dt.datetime(2026, 11, 14, 0, 2, tzinfo=dt.timezone.utc).timestamp()
    assert U.pausa_tras_429(D(23, 59)) == dt.datetime(2026, 11, 14, 0, 2, tzinfo=dt.timezone.utc).timestamp()
    assert U.pausa_tras_429(D(10, 39)) == D(10, 39).timestamp() + 120


def test_retencion(d):
    U.escribir([fila(mid="1")], d)
    old = d / "new_market_universo_2020-01-01.csv.gz"
    old.write_bytes(b"x")
    os.utime(old, (1, 1))
    U.retencion(d)
    assert not old.exists() and U.fichero(U.dia_utc(), d).exists()


def test_subdirectorio_no_coincide_con_globs_de_datalogs():
    """Ningun glob de datalogs/<prefijo>_*.csv* del repo ve el subdirectorio universo_5m/ (no recursivo)."""
    assert U.UNIV_DIR.name == "universo_5m" and U.UNIV_DIR.parent.name == "polymarket-research-datalogs"


def test_miembro_roto_en_medio_no_pierde_lo_escrito_despues(d):
    U.escribir([fila(mid="1")], d)
    p = U.fichero(U.dia_utc(), d)
    p.write_bytes(p.read_bytes() + b"\x1f\x8b\x08\x00corrupto a medias")          # escritura interrumpida
    U.escribir([fila(mid="2", slug="eth-updown-5m-1794687000")], d)
    U.escribir([fila(mid="3", slug="sol-updown-5m-1794687000")], d)
    mk, st = U.leer(directorio=d)
    assert set(mk) == {"1", "2", "3"} and st["truncados"] == 1


def test_miembro_cortado_al_final_y_gzip_de_un_solo_byte(d):
    U.escribir([fila(mid="1")], d)
    U.escribir([fila(mid="2", slug="eth-updown-5m-1794687000")], d)
    p = U.fichero(U.dia_utc(), d)
    p.write_bytes(p.read_bytes()[:-3])
    assert set(U.leer(directorio=d)[0]) == {"1"}
    p.write_bytes(b"\x1f")
    assert U.leer(directorio=d)[0] == {}
