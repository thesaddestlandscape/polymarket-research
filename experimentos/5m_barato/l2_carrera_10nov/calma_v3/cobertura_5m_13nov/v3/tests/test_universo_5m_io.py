"""universo_5m_io: formato, escritura multi-miembro, lectura tolerante (truncado, conflictos, cambio de dia), pausa 429, retencion."""
import csv, datetime as dt, gzip, json, os, time
import pytest
from pathlib import Path
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


def test_retencion_solo_datos_propios_y_nunca_estado(d):
    U.escribir([fila(mid="1")], d)
    viejos = ["new_market_universo_2020-01-01.csv.gz", "adelanto_2020-01-01.csv"]
    intactos = ["vigia_frescura_estado.json", "gamma_pausa.json", ".gamma_turno.lock", "otro_fichero.csv", "adelanto_2020-01-01.txt"]
    for n in viejos + intactos:
        (d / n).write_bytes(b"x")
        os.utime(d / n, (1, 1))
    U.retencion(d)
    assert not any((d / n).exists() for n in viejos) and all((d / n).exists() for n in intactos) and U.fichero(U.dia_utc(), d).exists()


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


def test_marcos_con_duracion_y_24h():
    assert set(U.RE_SLUG.pattern.split("(")[2].split(")")[0].split("|")) <= set(U.DUR_S)          # todo marco aceptado tiene duracion
    f = U.parsear_nuevo(ev(slug="btc-updown-24h-1794686700"), 1)
    assert f["cierre_ts"] == 1794686700 + 86400
    assert U.parsear_nuevo(ev(slug="btc-updown-3h-1794686700"), 1) is None


def test_fila_con_t_recv_o_t_evento_corruptos_no_mata_la_lectura(d):
    U.escribir([fila(mid="1")], d)
    p = U.fichero(U.dia_utc(), d)
    mala = fila(mid="2", slug="eth-updown-5m-1794687000")
    mala["t_recv_ms"] = "no-es-un-numero"
    mala2 = fila(mid="3", slug="sol-updown-5m-1794687000")
    mala2["t_evento_ms"] = "xx"
    import gzip as _gz, io as _io
    buf = _io.StringIO(newline="")
    w = csv.DictWriter(buf, fieldnames=U.COLS)
    w.writeheader(); w.writerows([mala, mala2])
    with open(p, "ab") as f:
        f.write(_gz.compress(buf.getvalue().encode()))
    mk, st = U.leer(directorio=d)
    assert set(mk) == {"1"} and st["invalidas"] == 2 and isinstance(mk["1"]["_t_recv"], int)


def test_miembros_es_lineal(d):
    def t(n):
        U.escribir([fila(mid=str(i), slug=f"btc-updown-5m-{1794686700 + 300 * i}") for i in range(n)], d / f"x{n}")   # un miembro grande
        raw = b"".join(__import__("gzip").compress(b"a,b\n1,2\n" * 20) for _ in range(n))
        t0 = time.perf_counter()
        datos, ok = U._miembros(raw)
        return time.perf_counter() - t0, ok, len(datos)
    t1, ok1, n1 = t(1000)
    t4, ok4, n4 = t(4000)
    assert ok1 and ok4 and n4 == 4 * n1
    assert t4 < max(8 * t1, 0.5) and t4 < 3.0                                  # O(n), no O(n^2) (x16 si fuera cuadratico)


def test_pausa_compartida_persistente_entre_procesos_y_solo_se_alarga(d):
    ahora = dt.datetime(2026, 11, 13, 19, 46, tzinfo=dt.timezone.utc)
    h = U.marcar_429(ahora, d)
    assert h == dt.datetime(2026, 11, 13, 20, 2, tzinfo=dt.timezone.utc).timestamp()
    import subprocess, sys, textwrap
    r = subprocess.run([sys.executable, "-c", textwrap.dedent("""
        import sys; sys.path.insert(0, %r); import universo_5m_io as U
        print(U.pausa_activa(%r, %r))""" % (str(Path(U.__file__).parent), h - 100, str(d)))], capture_output=True, text=True)
    assert float(r.stdout) == h
    assert U.marcar_429(dt.datetime(2026, 11, 13, 19, 10, tzinfo=dt.timezone.utc), d) == h          # una pausa mas corta no acorta la existente
    assert U.pausa_activa(h + 1, d) == 0.0                                                          # vencida
    (d / "gamma_pausa.json").write_text("{corrupto")
    assert U.pausa_activa(h - 100, d) == 0.0
    (d / "gamma_pausa.json").write_text(json.dumps({"hasta": time.time() + 10**7}))
    assert U.pausa_activa(time.time(), d) == 0.0                                                    # estado absurdo: se ignora


def test_turnos_de_gamma_compartidos_espaciados_entre_hilos_y_failopen(d):
    base = 1000.0
    assert U.esperar_turno(0.5, d, ahora=base) == 0.0
    assert U.esperar_turno(0.5, d, ahora=base) == pytest.approx(0.5)
    assert U.esperar_turno(0.5, d, ahora=base) == pytest.approx(1.0)
    import threading
    res = []
    def w():
        res.append(U.esperar_turno(0.1, d, ahora=5000.0))
    ts = [threading.Thread(target=w) for _ in range(12)]
    [t.start() for t in ts]; [t.join() for t in ts]
    r = sorted(res)
    assert all(b - a == pytest.approx(0.1, abs=1e-6) for a, b in zip(r, r[1:])) and r[0] == 0.0     # 12 llamantes: 0,1 s exactos entre turnos
    bad = d / "esto_es_un_fichero"
    bad.write_text("x")
    assert U.esperar_turno(0.5, bad) == 0.0 and U.marcar_429(dt.datetime(2026, 11, 13, 10, 0, tzinfo=dt.timezone.utc), bad) > 0   # fail-open
