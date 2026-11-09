"""Tests T1, T2, T4 de la FASE 1 (captura Binance independiente). Todo en un scratch (tmp_path) y contra un servidor WS falso: NO toca datalogs de produccion ni abre sockets externos.
Uso: nice -n 19 .venv/bin/python -m pytest -q experimentos/5m_barato/bnreg/tests/test_bnreg.py
T3 (sombra contra el hijo vivo, red real) es el script t3_sombra.py; T5 es solo post-despliegue (ver el traspaso)."""
import csv
import glob
import gzip
import importlib.util
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

AQUI = Path(__file__).resolve().parent
BN = AQUI.parent
REPO = BN.parent.parent.parent
PY = sys.executable
sys.path.insert(0, str(AQUI))
from falso_binance import FalsoBinance  # noqa: E402


@pytest.fixture
def srv():
    s = FalsoBinance()
    s.url = s.start()
    yield s
    try:
        s.stop()
    except Exception:
        pass


def lanzar_bnreg(dir_, url, nombre="bnreg", extra=None):
    env = dict(os.environ, LIBRO_WS_REGISTRO_DIR=str(dir_), BINANCE_WS_URL=url, **(extra or {}))
    log = open(Path(dir_) / f"{nombre}.stdout", "ab")
    return subprocess.Popen([PY, "-u", str(BN / "binance_registro_ms.py")], env=env, stdout=log, stderr=subprocess.STDOUT, cwd=str(REPO))


def lanzar_hijo(dir_, url, salida, nombre="hijo", cede_s=None):
    env = dict(os.environ, LIBRO_WS_REGISTRO_DIR=str(dir_), BINANCE_WS_URL=url, SALIDA_HIJO=str(salida))
    if cede_s is not None:
        env["BNREG_CEDE_S"] = str(cede_s)
    log = open(Path(dir_) / f"{nombre}.stdout", "ab")
    return subprocess.Popen([PY, "-u", str(AQUI / "hijo_reserva_driver.py")], env=env, stdout=log, stderr=subprocess.STDOUT, cwd=str(REPO))


def estado(dir_):
    try:
        return json.loads((Path(dir_) / "binance_registro_estado.json").read_text())
    except Exception:
        return {}


def esperar(cond, t=15.0, paso=0.05):
    t0 = time.time()
    while time.time() - t0 < t:
        v = cond()
        if v:
            return v
        time.sleep(paso)
    return None


def lock_libre(dir_):
    import fcntl
    fd = os.open(str(Path(dir_) / ".binance_registro.lock"), os.O_CREAT | os.O_RDWR)
    try:
        fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return True
    except OSError:
        return False
    finally:
        os.close(fd)


def filas(dir_, patron="maker_ms_*.csv.gz"):
    """Todas las lineas de los gz del dir, tolerando el final truncado."""
    out = []
    for f in sorted(glob.glob(str(Path(dir_) / patron))):
        try:
            with gzip.open(f, "rt", encoding="utf-8") as fh:
                for ln in fh:
                    out.append(ln)
        except (EOFError, OSError):
            pass
    return out


def parar(p, sig=signal.SIGTERM):
    if p.poll() is None:
        p.send_signal(sig)
        try:
            p.wait(10)
        except subprocess.TimeoutExpired:
            p.kill()
            p.wait()


# ---------------------------------------------------------------- T1
def test_t1_ocioso_sin_centinela(tmp_path, srv):
    p = lanzar_bnreg(tmp_path, srv.url)
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "ocioso", 8), "no llega a ocioso"
        time.sleep(2)
        assert srv.conexiones == 0, "conectado sin centinela"
        assert not glob.glob(str(tmp_path / "maker_ms_*")), "creo fichero maker_ms sin centinela"
        assert lock_libre(tmp_path), "lock tomado sin centinela"
        assert estado(tmp_path)["lock"] is False
    finally:
        parar(p)


def test_t1_un_solo_escritor_y_killswitch(tmp_path, srv):
    cent = tmp_path / "BNREG_HABILITADO"
    cent.touch()
    p1 = lanzar_bnreg(tmp_path, srv.url, "bnreg1")
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo" and estado(tmp_path).get("lock"), 8), "no activo con lock"
        # segundo proceso: no puede tomar el lock -> espera_lock, sin conexion ni fichero propio
        p2 = lanzar_bnreg(tmp_path, srv.url, "bnreg2")
        try:
            time.sleep(3)
            assert srv.conexiones == 1, f"el segundo bnreg conecto (conexiones={srv.conexiones})"
            assert len(glob.glob(str(tmp_path / "maker_ms_*.csv.gz"))) == 1, "dos ficheros de escritor"
            assert p2.poll() is None
        finally:
            parar(p2)
        # kill-switch: borrar el centinela -> cierra, suelta el lock y queda ocioso en <=3 s
        t0 = time.time()
        cent.unlink()
        assert esperar(lambda: lock_libre(tmp_path), 5), "lock no liberado tras borrar el centinela"
        dt = time.time() - t0
        assert dt <= 3.0, f"kill-switch tardo {dt:.1f}s"
        assert esperar(lambda: estado(tmp_path).get("estado") == "ocioso", 5)
        assert p1.poll() is None, "el proceso debe seguir vivo (ocioso), no morir"
        # fichero cerrado limpio (legible sin EOFError)
        f = glob.glob(str(tmp_path / "maker_ms_*.csv.gz"))[0]
        n = sum(1 for _ in gzip.open(f, "rt"))
        assert n > 50
        # se puede rehabilitar sin reiniciar
        cent.touch()
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
    finally:
        parar(p1)


def test_t1_hijo_en_reserva_y_relevo(tmp_path, srv):
    """Con bnreg activo el hijo NO conecta ni escribe; si bnreg muere (SIGKILL), el hijo asume en <=5 s; el kill-switch tambien."""
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    sal = tmp_path / "hijo_x.csv"
    h = None
    try:
        assert esperar(lambda: estado(tmp_path).get("lock"), 8)
        h = lanzar_hijo(tmp_path, srv.url, sal)
        time.sleep(7)                                           # >1 ciclo de reintento (5 s)
        assert srv.conexiones == 1, f"el hijo conecto con bnreg vivo (conexiones={srv.conexiones})"
        assert not sal.exists() or sal.stat().st_size == 0, "el hijo escribio con bnreg vivo"
        assert "RESERVA" in (tmp_path / "hijo.stdout").read_text()
        # bnreg muere de golpe
        t0 = time.time()
        p.send_signal(signal.SIGKILL)
        p.wait()
        assert esperar(lambda: srv.conexiones >= 2 and sal.exists() and sal.stat().st_size > 0, 8), "el hijo no asumio"
        dt = time.time() - t0
        print(f"relevo bnreg SIGKILL -> hijo escribiendo: {dt:.2f} s")
        assert dt <= 5.6, f"relevo tardo {dt:.2f}s (>5 s + conexion)"
        assert "ASUME" in (tmp_path / "hijo.stdout").read_text()
    finally:
        parar(p)
        if h:
            parar(h)


def test_t1_relevo_por_killswitch(tmp_path, srv):
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    sal = tmp_path / "hijo_x.csv"
    h = None
    try:
        assert esperar(lambda: estado(tmp_path).get("lock"), 8)
        h = lanzar_hijo(tmp_path, srv.url, sal)
        time.sleep(1)
        t0 = time.time()
        (tmp_path / "BNREG_HABILITADO").unlink()
        assert esperar(lambda: sal.exists() and sal.stat().st_size > 0, 10), "el hijo no asumio tras el kill-switch"
        dt = time.time() - t0
        print(f"relevo kill-switch -> hijo escribiendo: {dt:.2f} s")
        assert dt <= 6.0
        # ... y bnreg no vuelve a escribir mientras el hijo tiene el lock (aunque se vuelva a habilitar)
        (tmp_path / "BNREG_HABILITADO").touch()
        time.sleep(3)
        assert estado(tmp_path)["estado"] == "espera_lock" and estado(tmp_path)["lock"] is False
    finally:
        parar(p)
        if h:
            parar(h)


# ---------------------------------------------------------------- T2
def _produce(tmp_path, srv, segundos=8):
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
        time.sleep(segundos)
    finally:
        parar(p)                                              # SIGTERM -> cierre limpio
    return glob.glob(str(tmp_path / "maker_ms_*.csv.gz"))[0]


def test_t2_formato_y_lectores(tmp_path, srv):
    f = _produce(tmp_path, srv)
    lineas = gzip.open(f, "rt", encoding="utf-8").read().splitlines()
    assert lineas[0] == "tipo,t_ms,id,c1,c2,c3,c4,c5"
    x = [l for l in lineas[1:] if l.startswith("x,")]
    b = [l for l in lineas[1:] if l.startswith("b,")]
    assert len(x) > 100 and len(b) > 100 and len(x) + len(b) == len(lineas) - 1
    assert all(l.count(",") == 7 for l in lineas[1:]), "fila con != 8 campos"
    assert all(l.endswith(",") for l in b), "la fila b termina en coma (c5 vacio)"
    # --- pandas con names= como m15_ms_cache.py (x: 8 nombres) y q-like de 8
    import numpy as np
    import pandas as pd
    import io
    df = pd.read_csv(io.StringIO("\n".join(x)), header=None, names=["k", "T", "sym", "p", "qty", "m", "E", "tr"], dtype=str, on_bad_lines="skip", engine="c")
    assert len(df) == len(x) and df["tr"].notna().all() and df["sym"].isin(["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT", "BNBUSDT"]).all()
    assert (pd.to_numeric(df["tr"]).to_numpy(np.int64) >= pd.to_numeric(df["T"]).to_numpy(np.int64)).all(), "recepcion < T"
    # --- analisis_maker_cancelacion_binance.leer (mismos nombres, parche de DATALOGS)
    spec = importlib.util.spec_from_file_location("amcb", REPO / "analisis_maker_cancelacion_binance.py")
    amcb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(amcb)
    amcb.DATALOGS = tmp_path
    dia = time.strftime("%Y-%m-%d", time.gmtime())
    meta, libro, trades, binance = amcb.leer([dia])
    assert sum(len(v[0]) for v in binance.values()) > 0, "leer() no ve filas b"
    # --- parseo de x como vigia_5m_barato_forward.procesar (copia de la linea; el vigia congelado no se importa)
    binance_v = {}
    ilegibles = 0
    for ln in x:
        c = ln.split(",")
        try:
            binance_v.setdefault(c[2], []).append((int(c[7]), float(c[3]), float(c[4])))
        except (ValueError, IndexError):
            ilegibles += 1
    assert ilegibles == 0 and sum(len(v) for v in binance_v.values()) == len(x)
    # --- extraer_registro_5m_barato.extraer_fichero conserva todas las x
    spec = importlib.util.spec_from_file_location("erc", REPO / "extraer_registro_5m_barato.py")
    erc = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(erc)
    dst = tmp_path / "salida_extraida.csv.gz"
    erc.extraer_fichero(Path(f), dst)
    assert sum(1 for l in gzip.open(dst, "rt") if l.startswith("x,")) == len(x)
    print(f"T2: {len(x)} x + {len(b)} b, todas con 8 campos; pandas/leer/vigia/extraer OK")


def test_t2_x_exactos_frente_a_lo_enviado_e_integridad(tmp_path, srv):
    """Cada aggTrade enviado aparece EXACTAMENTE una vez con T,sym,p,q,m identicos; integridad sin faltantes; con un salto de ids forzado la integridad lo cuenta."""
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
        time.sleep(3)
        srv.saltar_ids = 7
        time.sleep(4)
    finally:
        parar(p)
        time.sleep(0.5)
    rec = [l.split(",") for l in filas(tmp_path) if l.startswith("x,")]
    obtenido = sorted((int(c[1]), c[2], c[3], c[4], int(c[5])) for c in rec)
    enviado = sorted(srv.enviados)
    # el servidor puede haber enviado algo en vuelo al cerrar: comparar el recibido contra el enviado (subconjunto) y que no haya duplicados
    assert len(set(obtenido)) == len(obtenido), "duplicados en el fichero"
    assert set(obtenido) <= set(enviado), "x en el fichero que el servidor no envio"
    assert len(obtenido) >= len(enviado) - 3, f"faltan {len(enviado) - len(obtenido)} x"
    integ = list(csv.DictReader(open(glob.glob(str(tmp_path / "binance_integridad_*.csv"))[0])))
    assert integ, "sin filas de integridad"
    falt = sum(int(r["faltantes"]) for r in integ if r["sym"] == "BTCUSDT")
    falt_otros = sum(int(r["faltantes"]) for r in integ if r["sym"] != "BTCUSDT")
    assert falt == 7 and falt_otros == 0, f"faltantes BTC={falt} otros={falt_otros} (esperado 7 y 0)"
    assert sum(int(r["dup"]) for r in integ) == 0
    h = open(glob.glob(str(tmp_path / "binance_huecos_*.csv"))[0]).read()
    assert "arranque" in h and "lock_tomado" in h and "parada" in h
    print(f"T2b: enviados {len(enviado)}, recibidos {len(obtenido)}, faltantes BTC detectados {falt}")


def test_t2_reconexion_marca_hueco_y_ids_continuos(tmp_path, srv):
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
        time.sleep(2)
        srv.drop()                                              # el servidor cierra: bnreg debe reconectar
        assert esperar(lambda: srv.conexiones >= 2, 8), "no reconecto"
        time.sleep(3)
    finally:
        parar(p)
    h = open(glob.glob(str(tmp_path / "binance_huecos_*.csv"))[0]).read()
    assert "caida" in h and h.count("conexion,") == 2, h      # `conexion` marca cada conexion exitosa (cierra el episodio de hueco)
    rec = [l.split(",") for l in filas(tmp_path) if l.startswith("x,")]
    rec_ms = sorted(int(c[7]) for c in rec)
    gap = max(b - a for a, b in zip(rec_ms, rec_ms[1:]))
    print(f"T2c: mayor hueco union en reconexion: {gap} ms")
    assert gap < 4000


def test_t2_silencio_union_reconecta(tmp_path, srv):
    """El servidor calla (conexion viva sin mensajes): a los ~10 s bnreg cierra y reconecta (marca `silencio`)."""
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
        time.sleep(1)
        srv.silencio = True
        t0 = time.time()
        assert esperar(lambda: srv.conexiones >= 2, 20), "no reconecto tras silencio"
        dt = time.time() - t0
        srv.silencio = False
        print(f"T2d: reconexion tras silencio de la union: {dt:.1f} s")
        assert 9.0 <= dt <= 13.0
        time.sleep(1.5)
    finally:
        parar(p)
    assert "silencio_union_10s" in open(glob.glob(str(tmp_path / "binance_huecos_*.csv"))[0]).read()


def test_t2_constantes_identicas_al_hijo():
    """_SIMB_BN y la URL por defecto de bnreg == las de libro_estado_ws de MAIN (un test, no un import)."""
    spec = importlib.util.spec_from_file_location("bn", BN / "binance_registro_ms.py")
    bn = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bn)
    env = dict(os.environ)
    env.pop("BINANCE_WS_URL", None)
    r = subprocess.run([PY, "-c", "import sys;sys.path.insert(0,sys.argv[1]);import libro_estado_ws as m;print(m._SIMB_BN);print(m.BINANCE_WS)", str(REPO)], capture_output=True, text=True, env=env, cwd=str(REPO))
    simb, url = r.stdout.strip().splitlines()[-2:]
    assert simb == str(tuple(bn._SIMB_BN)) and url == bn.BINANCE_WS_DEFECTO
    r = subprocess.run([PY, "-c", "import sys;sys.path.insert(0,sys.argv[1]);import libro_estado_ws as m;print(m._SIMB_BN);print(m.BINANCE_WS)", str(BN / "dev_main")], capture_output=True, text=True, env=env, cwd=str(REPO))
    simb2, url2 = r.stdout.strip().splitlines()[-2:]
    assert simb2 == simb and url2 == url, "el parche cambio simbolos/URL por defecto"


# ---------------------------------------------------------------- T4
def test_t4_reinicio_observadores_no_deja_hueco(tmp_path, srv):
    """Escenario real: bnreg escribe; el 'observadores' (hijo) se mata y relanza -> la union de x NO tiene hueco >1 s (en prod el hueco era 46-148 s)."""
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    sal = tmp_path / "hijo_x.csv"
    try:
        assert esperar(lambda: estado(tmp_path).get("lock"), 8)
        h = lanzar_hijo(tmp_path, srv.url, sal, "hijo1")
        time.sleep(3)
        h.send_signal(signal.SIGKILL)                           # 'OOM-kill' del hijo
        h.wait()
        time.sleep(2)
        h2 = lanzar_hijo(tmp_path, srv.url, sal, "hijo2")       # watchdog relanza observadores
        time.sleep(6)
        parar(h2)
        assert srv.conexiones == 1, "alguien mas conecto"
    finally:
        parar(p)
    rec_ms = sorted(int(l.split(",")[7]) for l in filas(tmp_path) if l.startswith("x,"))
    gap = max(b - a for a, b in zip(rec_ms, rec_ms[1:]))
    print(f"T4a: hueco maximo de la union durante el reinicio simulado de observadores: {gap} ms (n={len(rec_ms)})")
    assert gap < 1000
    assert not sal.exists() or sal.stat().st_size == 0


def test_t4_bnreg_cae_y_el_hijo_cubre(tmp_path, srv):
    """Peor caso: cae bnreg (SIGKILL). Union de x de ambos ficheros: hueco maximo <=10,6 s = cola sin volcar de bnreg (<=5 s de gz) + relevo del hijo (<=5 s) + conexion."""
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    sal = tmp_path / "hijo_x.csv"
    h = None
    try:
        assert esperar(lambda: estado(tmp_path).get("lock"), 8)
        h = lanzar_hijo(tmp_path, srv.url, sal)
        time.sleep(8)                                           # >5 s: el gz de bnreg ya tiene volcados; lo NO volcado al SIGKILL se pierde (<=5 s, igual que el hijo viejo)
        p.send_signal(signal.SIGKILL)
        p.wait()
        assert esperar(lambda: sal.exists() and sal.stat().st_size > 2000, 10), "el hijo no cubrio"
        time.sleep(3)
    finally:
        parar(p)
        if h:
            parar(h)
    rec = [int(l.split(",")[7]) for l in filas(tmp_path) if l.startswith("x,")]
    rec += [int(l.split(",")[7]) for l in open(sal) if l.startswith("x,")]
    rec.sort()
    gap = max(b - a for a, b in zip(rec, rec[1:]))
    print(f"T4b: hueco maximo de la union con bnreg caido y el hijo cubriendo: {gap} ms (n={len(rec)})")
    assert gap <= 10600
