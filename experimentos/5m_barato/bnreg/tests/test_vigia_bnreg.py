"""Tests del parche del vigia de silencio (dev_main/vigia_loggers_silenciosos.py::_bnreg_avisos): latido, centinela, huecos de la ultima hora, integridad de ayer, latch por episodio."""
import importlib.util
import json
import time
from pathlib import Path

BN = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("vls", BN / "dev_main" / "vigia_loggers_silenciosos.py")
vls = importlib.util.module_from_spec(spec)
spec.loader.exec_module(vls)


def estado(d, ts_ms, est="activo", lock=True, **extra):
    (d / "binance_registro_estado.json").write_text(json.dumps(dict(ts=ts_ms, estado=est, lock=lock, ultimo_recv_ms=ts_ms, **extra)))


def huecos(d, ahora, eventos, dia=None):
    dia = dia or time.strftime("%Y-%m-%d", time.gmtime(ahora))
    f = d / f"binance_huecos_{dia}.csv"
    nuevo = not f.exists()
    with open(f, "a") as fh:
        if nuevo:
            fh.write("evento,t_ms,conn_id,pid,motivo\n")
        for ev, seg_atras in eventos:
            fh.write(f"{ev},{int((ahora - seg_atras) * 1000)},1,99,x\n")


def test_sin_centinela_ni_huecos_no_avisa(tmp_path):
    estado(tmp_path, 1)
    a, v = vls._bnreg_avisos(time.time(), tmp_path, tmp_path / "latch.json")
    assert a == [] and v == []


def test_latido_parado_avisa_una_vez_y_avisa_recuperacion(tmp_path):
    (tmp_path / "BNREG_HABILITADO").touch()
    lt = tmp_path / "latch.json"
    ahora = time.time()
    estado(tmp_path, int((ahora - 300) * 1000))
    a, v = vls._bnreg_avisos(ahora, tmp_path, lt)
    assert len(a) == 1 and "latido de bnreg parado" in a[0]
    a, v = vls._bnreg_avisos(ahora + 60, tmp_path, lt)
    assert a == [] and v == []
    estado(tmp_path, int((ahora + 120) * 1000))
    a, v = vls._bnreg_avisos(ahora + 121, tmp_path, lt)
    assert a == [] and len(v) == 1 and "recuperado" in v[0]


def test_con_centinela_pero_sin_lock_escritor_fallando_o_sin_datos(tmp_path):
    (tmp_path / "BNREG_HABILITADO").touch()
    ahora = time.time()
    estado(tmp_path, int(ahora * 1000), "espera_lock", False)
    a, _ = vls._bnreg_avisos(ahora, tmp_path, tmp_path / "l1.json")
    assert len(a) == 1 and "sin ser el escritor" in a[0]
    estado(tmp_path, int(ahora * 1000), "activo", True, escritor_fallando=True, escritor_errores=3, cola=500)
    a, _ = vls._bnreg_avisos(ahora, tmp_path, tmp_path / "l2.json")
    assert len(a) == 1 and "escritor de bnreg FALLA" in a[0]
    (tmp_path / "binance_registro_estado.json").write_text(json.dumps(dict(ts=int(ahora * 1000), estado="reconectando", lock=True, ultimo_recv_ms=int((ahora - 400) * 1000))))
    a, _ = vls._bnreg_avisos(ahora, tmp_path, tmp_path / "l3.json")
    assert len(a) == 1 and "sin recibir datos de Binance" in a[0]


def test_sin_fichero_de_latido_avisa(tmp_path):
    (tmp_path / "BNREG_HABILITADO").touch()
    a, _ = vls._bnreg_avisos(time.time(), tmp_path, tmp_path / "l.json")
    assert len(a) == 1 and "sin latido legible" in a[0]


def test_huecos_largos_avisan_una_vez_firma_estable(tmp_path):
    ahora = time.time()
    huecos(tmp_path, ahora, [("caida", 1800), ("conexion", 1790),            # 10 s: NO (no supera 10)
                             ("parada", 1200), ("conexion", 1100),           # 100 s: SI
                             ("cola_llena", 600)])                           # perdida: SI
    lt = tmp_path / "latch.json"
    a, _ = vls._bnreg_avisos(ahora, tmp_path, lt)
    textos = " | ".join(a)
    assert len(a) == 2 and "parada -> reconectado tras 100 s" in textos and "cola_llena" in textos, a
    # misma hora, mas tarde: la duracion NO cambia la firma -> sin spam
    a, _ = vls._bnreg_avisos(ahora + 600, tmp_path, lt)
    assert a == []
    # un hueco antiguo (fuera de la ultima hora) no avisa
    tmp2 = tmp_path / "x"
    tmp2.mkdir()
    huecos(tmp2, ahora, [("caida", 7200), ("conexion", 7000)])
    a, _ = vls._bnreg_avisos(ahora, tmp2, tmp2 / "l.json")
    assert a == []


def test_hueco_abierto_avisa_y_no_se_repite_aunque_crezca(tmp_path):
    ahora = time.time()
    huecos(tmp_path, ahora, [("hijo_cede", 300)])
    lt = tmp_path / "latch.json"
    a, _ = vls._bnreg_avisos(ahora, tmp_path, lt)
    assert len(a) == 1 and "ABIERTO" in a[0]
    a, _ = vls._bnreg_avisos(ahora + 900, tmp_path, lt)
    assert a == []


def test_integridad_de_ayer_falta_con_centinela_ayer(tmp_path):
    ahora = time.time()
    ayer = time.strftime("%Y-%m-%d", time.gmtime(ahora - 86400))
    huecos(tmp_path, ahora - 86400, [("lock_tomado", 100)], dia=ayer)
    lt = tmp_path / "l.json"
    a, _ = vls._bnreg_avisos(ahora, tmp_path, lt)
    assert any(f"falta binance_integridad_{ayer}.csv" in x for x in a), a
    a, _ = vls._bnreg_avisos(ahora + 60, tmp_path, lt)                       # una vez al dia
    assert not any("falta binance_integridad" in x for x in a)
    # sin evidencia de centinela ayer: no avisa
    t2 = tmp_path / "y"
    t2.mkdir()
    a, _ = vls._bnreg_avisos(ahora, t2, t2 / "l.json")
    assert not any("falta binance_integridad" in x for x in a)
    # centinela visto por el propio vigia ayer (latch)
    t3 = tmp_path / "z"
    t3.mkdir()
    (t3 / "l.json").write_text(json.dumps({"dias_centinela": [ayer]}))
    a, _ = vls._bnreg_avisos(ahora, t3, t3 / "l.json")
    assert any("falta binance_integridad" in x for x in a)


def test_integridad_de_ayer_con_faltantes_avisa_una_vez_al_dia(tmp_path):
    ahora = time.time()
    ayer = time.strftime("%Y-%m-%d", time.gmtime(ahora - 86400))
    (tmp_path / f"binance_integridad_{ayer}.csv").write_text("min_utc,sym,conn_id,n_x,a_min,a_max,distintos,dup,fuera_orden,faltantes\n"
                                                              "2026-11-08T10:00,BTCUSDT,1,10,1,20,10,0,0,10\n2026-11-08T10:01,ETHUSDT,1,10,1,10,10,0,0,0\n")
    lt = tmp_path / "l.json"
    a, _ = vls._bnreg_avisos(ahora, tmp_path, lt)
    assert len(a) == 1 and "10 aggTradeId faltantes" in a[0]
    a, _ = vls._bnreg_avisos(ahora + 10, tmp_path, lt)
    assert a == []
