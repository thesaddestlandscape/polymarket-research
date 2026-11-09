"""Tests de las correcciones del /code-review (09-Nov): senales, escritor que falla, gzip truncado, mensajes basura, backoff/sin_datos, cesion del hijo, choom -200, traspaso (funciones de bash),
vigia (huecos). Mismo esquema que test_bnreg.py: scratch + servidor WS falso, nada toca produccion."""
import csv
import glob
import gzip
import importlib.util
import json
import os
import re
import signal
import subprocess
import sys
import time
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from test_bnreg import (BN, PY, REPO, esperar, estado, filas, lanzar_bnreg, lanzar_hijo, lock_libre, parar, srv)  # noqa: E402,F401


def huecos(d):
    out = []
    for f in sorted(glob.glob(str(Path(d) / "binance_huecos_*.csv"))):
        out += [r for r in csv.DictReader(open(f)) if r["evento"] != "evento"]
    return out


def cargar_modulo(nombre, ruta, **env):
    for k, v in env.items():
        os.environ[k] = v
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ------------------------------------------------------------ 1. senales
@pytest.mark.parametrize("sg", [signal.SIGHUP, signal.SIGTERM, signal.SIGINT])
def test_senal_cierre_limpio(tmp_path, srv, sg):
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
    time.sleep(2.5)
    t0 = time.time()
    p.send_signal(sg)
    rc = p.wait(10)
    dt = time.time() - t0
    assert rc == 0, f"codigo de salida {rc} con {sg.name}"
    assert dt < 4, f"cierre tardo {dt:.1f}s"
    f = glob.glob(str(tmp_path / "maker_ms_*.csv.gz"))[0]
    lineas = gzip.open(f, "rt").read().splitlines()          # sin EOFError: gzip cerrado
    assert lineas[0].startswith("tipo,") and len(lineas) > 50
    assert estado(tmp_path)["estado"] == "parado" and estado(tmp_path)["lock"] is False
    ev = [h["evento"] for h in huecos(tmp_path)]
    assert "parada" in ev
    assert glob.glob(str(tmp_path / "binance_integridad_*.csv")), "sin integridad del minuto en curso"
    assert lock_libre(tmp_path)
    print(f"{sg.name}: salida {rc} en {dt:.2f} s, {len(lineas)} lineas, marca parada, integridad volcada")


def test_senal_durante_backoff_no_espera_el_sueno(tmp_path, srv):
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
        srv.stop()                                                 # servidor caido: bnreg entra en backoff creciente
        time.sleep(9)                                              # backoff 1+2+4... -> durmiendo ya
        t0 = time.time()
        p.send_signal(signal.SIGHUP)
        p.wait(10)
        dt = time.time() - t0
        print(f"SIGHUP durante backoff: salio en {dt:.2f} s")
        assert dt < 3
    finally:
        parar(p)


# ------------------------------------------------------------ 2. escritor que falla
def test_escritor_no_pierde_lineas_si_falla(tmp_path, monkeypatch):
    bn = cargar_modulo("bn_w", BN / "binance_registro_ms.py", LIBRO_WS_REGISTRO_DIR=str(tmp_path))
    real_open = gzip.open
    estado_fallo = {"abrir_falla": 0, "escribir_tras": None}

    class Envoltura:
        def __init__(self, f):
            self.f, self.n = f, 0

        def write(self, x):
            if estado_fallo["escribir_tras"] is not None and self.n >= estado_fallo["escribir_tras"]:
                raise OSError("disco lleno (simulado)")
            self.n += 1
            return self.f.write(x)

        def flush(self):
            return self.f.flush()

        def close(self):
            return self.f.close()

    def abrir(*a, **k):
        if estado_fallo["abrir_falla"] > 0:
            estado_fallo["abrir_falla"] -= 1
            raise OSError("no se puede abrir (simulado)")
        return Envoltura(real_open(*a, **k))

    monkeypatch.setattr(bn.gzip, "open", abrir)
    estado_fallo["abrir_falla"] = 3                               # 1) el fichero no se puede abrir 3 veces seguidas
    esc = bn.Escritor()
    enviadas = [f"x,{i},BTCUSDT,1,1,0,{i},{i}\n" for i in range(300)]
    for l in enviadas[:50]:
        esc.put(l)
    assert esperar(lambda: esc.fallando, 3), "el escritor no declara fallo"
    assert esc.q.qsize() > 0 or esc.errores > 0
    est = bn.Estado()
    est.escritor = esc
    assert esperar(lambda: not esc.fallando, 10), "no se recupera"
    for l in enviadas[50:150]:
        esc.put(l)
    time.sleep(0.5)
    estado_fallo["escribir_tras"] = 40                            # 2) a mitad de fichero la escritura falla: el fichero se descarta y se retoma en otro
    for l in enviadas[150:]:
        esc.put(l)
    assert esperar(lambda: esc.fallando, 5)
    estado_fallo["escribir_tras"] = None
    assert esperar(lambda: not esc.fallando and esc.q.qsize() == 0, 10)
    esc.parar()
    lin = []
    for f in sorted(glob.glob(str(tmp_path / "maker_ms_*.csv.gz"))):
        lin += [l for l in real_open(f, "rt").read().splitlines(True) if l.startswith("x,")]
    assert sorted(lin) == sorted(enviadas), f"{len(lin)} escritas de {len(enviadas)}: hay perdida o duplicado"
    ev = [h["evento"] for h in huecos(tmp_path)]
    assert "escritor_fallo" in ev and "escritor_recuperado" in ev
    ficheros = sorted(Path(f).name for f in glob.glob(str(tmp_path / "maker_ms_*.csv.gz")))
    assert len(ficheros) == 2, ficheros      # fichero 1 (descartado a mitad de escritura) + fichero 2 (retoma)
    print(f"escritor: {len(lin)}/{len(enviadas)} lineas, ficheros {ficheros}, errores={esc.errores}, marcas={sorted(set(ev))}")


def test_latido_muestra_escritor_fallando_y_cola(tmp_path):
    bn = cargar_modulo("bn_l", BN / "binance_registro_ms.py", LIBRO_WS_REGISTRO_DIR=str(tmp_path))
    class E:                       # escritor falso
        q = type("Q", (), {"qsize": staticmethod(lambda: 1234)})()
        descartes, filas, fallando, errores = 7, 9, True, 4
    bn.ST.escritor = E()
    bn.ST.escribir()
    d = json.loads((tmp_path / "binance_registro_estado.json").read_text())
    assert d["escritor_fallando"] is True and d["cola"] == 1234 and d["descartes"] == 7 and d["escritor_errores"] == 4 and "ignorados" in d and "oom_adj" in d


# ------------------------------------------------------------ 3. gzip truncado
def test_no_se_anade_tras_fragmento_truncado(tmp_path):
    from falso_binance import FalsoBinance
    dia = time.strftime("%Y-%m-%d", time.gmtime())
    pid = os.getpid()
    bn = cargar_modulo("bn_t", BN / "binance_registro_ms.py", LIBRO_WS_REGISTRO_DIR=str(tmp_path))
    assert bn.PID == pid
    trunc = tmp_path / f"maker_ms_{dia}_{pid}.csv.gz"
    with gzip.open(trunc, "wt") as fh:                             # fichero previo: se corta a medias (SIGKILL)
        fh.write("tipo,t_ms,id,c1,c2,c3,c4,c5\n" + "".join(f"x,{i},BTCUSDT,1,1,0,{i},{i}\n" for i in range(2000)))
    datos = trunc.read_bytes()
    trunc.write_bytes(datos[: len(datos) // 2])
    antes = trunc.read_bytes()
    esc = bn.Escritor()
    for i in range(100):
        esc.put(f"x,{i},ETHUSDT,1,1,0,{i},{i}\n")
    time.sleep(1.5)
    esc.parar()
    assert trunc.read_bytes() == antes, "se modifico el fragmento truncado"
    nuevo = tmp_path / f"maker_ms_{dia}_{pid}1.csv.gz"
    assert nuevo.exists() and nuevo.name == esc.ruta.name
    # glob de los lectores (maker_ms_<dia>_*.csv.gz) ve ambos; el nuevo se lee entero con pandas (names=8 como m15_ms_cache) y con gzip
    assert len(glob.glob(str(tmp_path / f"maker_ms_{dia}_*.csv.gz"))) == 2
    import pandas as pd
    df = pd.read_csv(nuevo, header=0, names=["k", "T", "sym", "p", "qty", "m", "E", "tr"], dtype=str)
    assert len(df) == 100 and (df["sym"] == "ETHUSDT").all()
    # el truncado sigue siendo legible hasta donde llega con el lector tolerante (EOFError al final, como hoy)
    n = 0
    try:
        with gzip.open(trunc, "rt") as fh:
            for _ in fh:
                n += 1
    except EOFError:
        pass
    assert 0 < n < 2001
    # el nombre cuadra con el regex del vigia de silencio (un solo logger por familia)
    vls = cargar_modulo("vls_n", BN / "dev_main" / "vigia_loggers_silenciosos.py")
    assert vls._SUFIJO_PROCESO.sub("", nuevo.name) == vls._SUFIJO_PROCESO.sub("", trunc.name)
    print(f"fragmento truncado intacto ({n} filas legibles), nuevo fichero {nuevo.name} leido por pandas (100 filas)")


def test_sigkill_y_reinicio_usa_fichero_distinto(tmp_path, srv):
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url, "a")
    assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
    time.sleep(6)
    p.send_signal(signal.SIGKILL)
    p.wait()
    f1 = set(glob.glob(str(tmp_path / "maker_ms_*.csv.gz")))
    tam = {f: Path(f).stat().st_size for f in f1}
    p2 = lanzar_bnreg(tmp_path, srv.url, "b")
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo" and estado(tmp_path).get("pid") == p2.pid, 10)
        time.sleep(3)
        f2 = set(glob.glob(str(tmp_path / "maker_ms_*.csv.gz")))
        assert len(f2) == 2 and all(Path(f).stat().st_size == tam[f] for f in f1), "el fichero previo se modifico"
        ev = [h for h in huecos(tmp_path) if h["evento"] == "caida_proceso"]
        assert len(ev) == 1 and "pid_previo" in ev[0]["motivo"], "falta la marca caida_proceso con el ultimo latido"
    finally:
        parar(p2)


# ------------------------------------------------------------ 7. mensajes basura
def test_mensajes_no_json_no_cierran_la_conexion(tmp_path, srv):
    srv.basura = True
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
        time.sleep(7)
        assert srv.conexiones == 1, f"se reconecto por mensajes basura ({srv.conexiones} conexiones)"
        assert esperar(lambda: estado(tmp_path).get("ignorados", 0) > 20, 6)
        print("ignorados en el latido:", estado(tmp_path)["ignorados"], "; conexiones:", srv.conexiones)
    finally:
        parar(p)
    x = [l for l in filas(tmp_path) if l.startswith("x,")]
    assert len(x) > 100 and all(l.count(",") == 7 for l in x)


# ------------------------------------------------------------ 8. backoff y sin_datos
def test_sin_datos_solo_cuenta_tiempo_conectado(tmp_path, srv):
    """Servidor caido (conexion rechazada) >> umbral: NO sale; recupera al volver; backoff vuelve a 1 s tras mensajes."""
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url, extra={"BNREG_SIN_DATOS_S": "5"})
    port = srv.port
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
        srv.stop()
        time.sleep(14)                                             # >2x el umbral de 5 s, todo en backoff/conexion rechazada
        assert p.poll() is None, "salio por tiempo de backoff"
        assert estado(tmp_path)["estado"] == "reconectando"
        srv.start(port)
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 40), "no recupero"
        n0 = srv.conexiones
        time.sleep(1)
        t0 = time.time()
        srv.drop()                                                 # tras mensajes sanos el backoff vale 1 s
        assert esperar(lambda: srv.conexiones > n0, 5)
        dt = time.time() - t0
        print(f"reconexion tras caida con backoff reiniciado: {dt:.2f} s")
        assert dt < 2.5
    finally:
        parar(p)


def test_sin_datos_sale_tras_120s_conectado_sin_mensajes(tmp_path, srv):
    """Conectado pero mudo (umbral reducido a 12 s en la prueba): sale con codigo 2, con marca y estado."""
    (tmp_path / "BNREG_HABILITADO").touch()
    srv.silencio = True
    p = lanzar_bnreg(tmp_path, srv.url, extra={"BNREG_SIN_DATOS_S": "12"})
    t0 = time.time()
    rc = p.wait(60)
    dt = time.time() - t0
    print(f"salida por sin datos conectado: codigo {rc} tras {dt:.1f} s (umbral de prueba 12 s)")
    assert rc == 2
    ev = [h["evento"] for h in huecos(tmp_path)]
    assert "salida_sin_datos" in ev and estado(tmp_path)["estado"] == "salida"


def test_reconexion_log_consistente(tmp_path, srv):
    (tmp_path / "BNREG_HABILITADO").touch()
    p = lanzar_bnreg(tmp_path, srv.url)
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo", 8)
        time.sleep(1)
        srv.drop()
        assert esperar(lambda: srv.conexiones >= 2, 6)
        time.sleep(1)
    finally:
        parar(p)
    log = (tmp_path / "bnreg.stdout").read_text()
    m = re.search(r"reconecta en (\d+) s", log)
    assert m and m.group(1) == "1"
    ev = [h["evento"] for h in huecos(tmp_path)]
    assert ev.count("conexion") == 2 and "caida" in ev


# ------------------------------------------------------------ 5. cesion del hijo
def test_hijo_cede_el_lock_cuando_bnreg_vuelve(tmp_path, srv):
    (tmp_path / "BNREG_HABILITADO").touch()
    sal = tmp_path / "hijo_x.csv"
    p = lanzar_bnreg(tmp_path, srv.url, "bn1")
    h = None
    p2 = None
    try:
        assert esperar(lambda: estado(tmp_path).get("lock"), 8)
        h = lanzar_hijo(tmp_path, srv.url, sal, cede_s=4)
        time.sleep(1)
        p.send_signal(signal.SIGKILL)
        p.wait()
        assert esperar(lambda: sal.exists() and sal.stat().st_size > 0, 10), "el hijo no asumio"
        # bnreg vuelve: con el hijo cubriendo -> espera_lock; el hijo cede tras >=4 s (histeresis de prueba) y bnreg pasa a escribir
        p2 = lanzar_bnreg(tmp_path, srv.url, "bn2")
        t_espera = esperar(lambda: estado(tmp_path).get("estado") == "espera_lock" and time.time(), 8)
        assert t_espera, "bnreg no anuncia espera_lock"
        assert time.time() - t_espera < 3 and not [e for e in huecos(tmp_path) if e["evento"] == "hijo_cede"], "cedio antes de la histeresis"
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo" and estado(tmp_path).get("lock") and estado(tmp_path).get("pid") == p2.pid, 20), "bnreg no recupero el lock"
        t_cede = time.time() - t_espera
        print(f"bnreg anuncio espera_lock -> bnreg dueno del lock: {t_cede:.1f} s (histeresis de prueba 4 s)")
        assert t_cede >= 3.5
        n = sal.stat().st_size
        time.sleep(3)
        assert sal.stat().st_size == n, "el hijo sigue escribiendo tras ceder"
        ev = [e["evento"] for e in huecos(tmp_path)]
        assert ev.count("hijo_asume") == 1 and ev.count("hijo_cede") == 1 and ev.count("hijo_conexion") == 1, ev
        # una sola vez por episodio: el hijo no vuelve a competir mientras bnreg escribe
        time.sleep(12)
        assert ev.count("hijo_cede") == 1 and [e["evento"] for e in huecos(tmp_path)].count("hijo_asume") == 1
        assert estado(tmp_path)["pid"] == p2.pid and estado(tmp_path)["lock"]
        # sin hueco en la union: el solape lo vigila el test T4; aqui se mide que no hubo doble escritor (x repetidas por (T,sym,p,q,m) entre ficheros)
        propios = [l.split(",")[1:6] for l in filas(tmp_path) if l.startswith("x,")]
        del_hijo = [l.split(",")[1:6] for l in open(sal) if l.startswith("x,")]
        t_ult_hijo = max(int(l[0]) for l in del_hijo)
        sol = [l for l in propios if int(l[0]) <= t_ult_hijo]
        print(f"x de bnreg con T <= ultimo T del hijo (solape): {len(sol)}")
        assert len(sol) <= 3
    finally:
        parar(p)
        if p2:
            parar(p2)
        if h:
            parar(h)


# ------------------------------------------------------------ 9. choom -200
def test_choom_menos_200_aplicado(tmp_path, srv):
    """Ejecuta la linea REAL de SCREEN_RESTART["bnreg"] (con ulimit y choom) en un sandbox y lee oom_score_adj del proceso."""
    src = (BN / "dev_main" / "pipeline_watchdog.py").read_text()
    m = re.search(r'^\s*"bnreg": f"(.*)",\s*$', src, re.M)
    assert m, "no hay SCREEN_RESTART['bnreg']"
    cmd = m.group(1).replace("{REPO}", str(tmp_path / "repo"))
    assert "choom -n -200 -- " in cmd and "ulimit -v 2000000" in cmd
    (tmp_path / "repo" / "logs").mkdir(parents=True)
    os.symlink(REPO / ".venv", tmp_path / "repo" / ".venv")
    (tmp_path / "repo" / "binance_registro_ms.py").write_bytes((BN / "binance_registro_ms.py").read_bytes())
    dl = tmp_path / "dl"
    dl.mkdir()
    (dl / "BNREG_HABILITADO").touch()
    env = dict(os.environ, LIBRO_WS_REGISTRO_DIR=str(dl), BINANCE_WS_URL=srv.url)
    p = subprocess.Popen(["bash", "-c", cmd], env=env)
    try:
        assert esperar(lambda: estado(dl).get("estado") == "activo", 10), (tmp_path / "repo/logs/binance_registro_ms.log").read_text()[-800:]
        pid = estado(dl)["pid"]
        adj = int(Path(f"/proc/{pid}/oom_score_adj").read_text())
        lim = [l for l in Path(f"/proc/{pid}/limits").read_text().splitlines() if l.startswith("Max address space")][0]
        print(f"pid {pid}: oom_score_adj={adj}; latido oom_adj={estado(dl)['oom_adj']}; {lim}")
        assert adj == -200 and estado(dl)["oom_adj"] == -200
        assert "2048000000" in lim.replace(",", "") or "2000000" in lim
        time.sleep(3)
        assert estado(dl)["filas_total"] > 0, "bajo ulimit -v no escribe"
    finally:
        try:
            os.kill(estado(dl)["pid"], signal.SIGTERM)
        except Exception:
            pass
        p.wait(10)


# ------------------------------------------------------------ 4. traspaso: funciones de bash
def _bash_funcs():
    t = (BN / "traspaso_bnreg_once.sh").read_text()
    a = t.index("bn_estado_ok()")
    b = t.index("restaurar()")
    return t[a:b]


def _bash(dl, cuerpo):
    script = f'PY={PY}\nDL={dl}\n' + _bash_funcs() + cuerpo
    return subprocess.run(["bash", "-c", script], capture_output=True, text=True)


def test_traspaso_duenyo_del_lock(tmp_path, srv):
    (tmp_path / "BNREG_HABILITADO").touch()
    # sin nadie: no es duenyo
    assert _bash(tmp_path, "bn_es_duenyo").returncode != 0
    p = lanzar_bnreg(tmp_path, srv.url)
    try:
        assert esperar(lambda: estado(tmp_path).get("estado") == "activo" and estado(tmp_path).get("lock"), 8)
        assert _bash(tmp_path, "bn_estado_ok activo 15 && bn_es_duenyo").returncode == 0, "bnreg activo con lock debe ser duenyo"
        assert _bash(tmp_path, "oom_de_bnreg").stdout.strip() == str(int(Path(f'/proc/{p.pid}/oom_score_adj').read_text()))
    finally:
        parar(p)
    # bnreg muerto pero el lock lo tiene el hijo: NO es duenyo (el texto del lock no es de bnreg vivo)
    sal = tmp_path / "hx.csv"
    (tmp_path / "BNREG_HABILITADO").touch()
    h = lanzar_hijo(tmp_path, srv.url, sal)
    try:
        assert esperar(lambda: sal.exists() and sal.stat().st_size > 0, 12), "el hijo no tomo el lock"
        assert _bash(tmp_path, "bn_es_duenyo").returncode != 0, "con el hijo como escritor, bn_es_duenyo debe fallar"
    finally:
        parar(h)


def test_traspaso_modo_plan_no_modifica_nada(tmp_path):
    repo, dl = tmp_path / "repo", tmp_path / "dl"
    repo.mkdir()
    dl.mkdir()
    env = dict(os.environ, REPO=str(repo), DL=str(dl), STAGING=str(BN / "dev_main"), PY=PY)
    r = subprocess.run(["bash", str(BN / "traspaso_bnreg_once.sh")], capture_output=True, text=True, env=env)
    assert r.returncode == 1
    assert "FALLA binance_registro_ms.py presente en main" in r.stdout and "Modo plan: no se hace ningun cambio" in r.stdout
    assert sorted(p.name for p in dl.iterdir()) == ["traspaso_bnreg"], "el modo plan toco el directorio de datos"
    assert not list(repo.iterdir())
    print(r.stdout.strip().splitlines()[-2])


def test_traspaso_orden_de_pasos_en_el_texto():
    t = (BN / "traspaso_bnreg_once.sh").read_text()
    pos = [t.index(m) for m in ("== P4 parar observadores", "== P5 habilitar bnreg", "== P6 arrancar observadores")]
    assert pos == sorted(pos)
    assert "20 s" in t and 'die "bnreg no es el dueno del lock en 20 s"' in t and "restaurar()" in t
    assert t.count("verify_deploy.py --restart observadores") >= 2          # P6 y la restauracion
