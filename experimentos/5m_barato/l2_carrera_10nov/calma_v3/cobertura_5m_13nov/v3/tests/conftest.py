import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "stage"))
sys.path.insert(0, "/root/polymarket-research")        # data_quality (import de capture_markets)


# ---- L1: sello del ensayo e2e. El P0 del despliegue real exige datalogs/traspaso_deltas_ws/e2e_ok.json (sha de los scripts, <24 h, 5 tests PASADOS): un skip
# (sin red/espacio) o un fallo NO sellan. Se escribe solo si TODOS los tests de test_e2e_real.py corrieron y pasaron.
import hashlib, json, os, time
_E2E = {}
_V3 = Path(__file__).resolve().parent.parent


# ---- L3: volumen de pruebas para los e2e. El hijo REAL de libro_estado_ws pausa libro5 con < 10 GB libres en su volumen (umbral del codigo desplegado: NO se toca), asi que los e2e necesitan un
# directorio con >= E2E_MIN_GB libres que NO sea el disco raiz. Si hay e2e seleccionados y E2E_DIR no existe o no llega, se monta un tmpfs (tests/e2e/vol_e2e.sh; tope 12 GB, no reserva RAM)
# y se desmonta al acabar (pytest_unconfigure). run_tests.sh monta/desmonta el suyo con trap y exporta E2E_DIR (entonces aqui no se hace nada). Un E2E_DIR explicito del usuario NO se
# sustituye: si no llega, los e2e FALLAN con 'E2E necesita >=10 GB libres en $E2E_DIR'.
import shutil, subprocess
E2E_MIN_GB = 10.5
_VOL = {"dir": None}


def pytest_collection_modifyitems(config, items):
    if not any("test_e2e_real.py" in i.nodeid for i in items):
        return
    d = os.environ.get("E2E_DIR")
    if d:
        return
    r = subprocess.run(["bash", str(_V3 / "tests/e2e/vol_e2e.sh"), "monta"], capture_output=True, text=True)
    if r.returncode == 0 and r.stdout.strip():
        _VOL["dir"] = r.stdout.strip(); os.environ["E2E_DIR"] = _VOL["dir"]


def pytest_unconfigure(config):
    if _VOL["dir"]:
        subprocess.run(["bash", str(_V3 / "tests/e2e/vol_e2e.sh"), "limpia", _VOL["dir"]], capture_output=True)
        os.environ.pop("E2E_DIR", None); _VOL["dir"] = None


def pytest_runtest_logreport(report):
    if "test_e2e_real.py" in report.nodeid and (report.when == "call" or (report.when == "setup" and report.outcome != "passed")):
        _E2E[report.nodeid] = report.outcome


def pytest_sessionfinish(session, exitstatus):
    esperados = [i.nodeid for i in session.items if "test_e2e_real.py" in i.nodeid]
    if not esperados or len(esperados) < 5 or any(_E2E.get(n) != "passed" for n in esperados):
        return
    fs = [_V3 / "deploy/deploy_deltas_libro_ws_once.sh", _V3 / "deploy/lib_espera_hijos.sh", _V3 / "deploy/p6_ciclo_aislado.py", _V3 / "deploy/clases_error.conf", _V3 / "delta_v3/sembrar_cache_tokens.py",
          _V3 / "delta_v3/libro_estado_ws.py", _V3 / "stage/capture_markets.py", _V3 / "stage/universo_5m_io.py"]       # = E2E_FILES del script (SEMBRAR_PY por defecto)
    h = hashlib.sha256(b"".join(f.read_bytes() for f in fs if f.exists())).hexdigest()[:32]
    d = Path(os.environ.get("E2E_STAMP_DIR", "/root/polymarket-research-datalogs/traspaso_deltas_ws")); d.mkdir(parents=True, exist_ok=True)
    (d / "e2e_ok.json").write_text(json.dumps({"sha": h, "ts": int(time.time()), "pasados": len(esperados)}))
