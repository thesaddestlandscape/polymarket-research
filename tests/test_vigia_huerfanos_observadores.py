import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import vigia_huerfanos_observadores as V


def _proc(root, pid, args, ppid):
    d = root / str(pid); d.mkdir()
    (d / "cmdline").write_bytes(b"\0".join(a.encode() for a in args) + b"\0")
    (d / "status").write_text(f"Name:\tx\nPPid:\t{ppid}\n")


def test_listar_filtra_ppid1_y_objetivo(tmp_path):
    _proc(tmp_path, 10, [".venv/bin/python", "observadores_fase0.py"], 1)                       # huerfano
    _proc(tmp_path, 11, ["/x/python", "-u", "/r/libro_estado_ws.py", "--hijo"], 1)              # hijo huerfano
    _proc(tmp_path, 12, [".venv/bin/python", "observadores_fase0.py"], 500)                     # vivo con padre
    _proc(tmp_path, 13, ["SCREEN", "-dmS", "observadores", "bash", "-c", "python observadores_fase0.py"], 1)
    _proc(tmp_path, 14, ["bash", "-c", "cd r && python observadores_fase0.py"], 1)              # envoltorio
    _proc(tmp_path, 15, ["python", "libro_estado_ws.py"], 1)                                    # standalone sin --hijo: no
    (tmp_path / "self").mkdir()
    assert [p for p, _ in V.listar_huerfanos(tmp_path)] == [10, 11]


def test_latch_un_aviso_por_episodio_y_recuperacion():
    e, a = V.decidir({}, [1], 1000.0); assert a is None and e["desde"] == 1000.0
    e, a = V.decidir(e, [1], 1500.0); assert a is None                 # 500 s < 600
    e, a = V.decidir(e, [1, 2], 1700.0); assert a == "avisar" and e["avisado"]
    e, a = V.decidir(e, [1], 9000.0); assert a is None                 # sin spam
    e, a = V.decidir(e, [], 9100.0); assert a == "recuperado" and e == {"desde": None, "avisado": False}
    e, a = V.decidir(e, [], 9200.0); assert a is None
    e, a = V.decidir(e, [3], 9300.0); assert a is None and e["desde"] == 9300.0   # nuevo episodio reinicia el reloj


def test_viva_actual_no_cuenta():
    # el proceso real (ppid = bash/screen) no es huerfano
    assert all(p != 0 for p, _ in V.listar_huerfanos())
