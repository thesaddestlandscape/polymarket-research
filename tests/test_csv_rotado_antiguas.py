import csv, gzip, sys, tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import csv_rotado as R


def _mk(d, dias_filas):
    p = Path(d) / "x.csv"
    now = datetime.now(timezone.utc)
    with open(p, "w", newline="") as f:
        w = csv.writer(f); w.writerow(["timestamp_utc", "a", "acierto"])
        for i, (dias, ac) in enumerate(dias_filas):
            w.writerow([(now - timedelta(days=dias)).strftime("%Y-%m-%dT%H:%M:%S.000+00:00"), f"v{i}", ac])
    return p


def _todo(p):
    with R.abrir(p) as f:
        return list(csv.reader(f))


def test_prefijo_resuelto_y_orden():
    with tempfile.TemporaryDirectory() as d:
        R.DIR_PARTES = Path(d) / "partes"
        p = _mk(d, [(9, "1"), (8, "0"), (5, "1"), (2, "1"), (1, ""), (0.1, "")])
        antes = _todo(p)
        assert R.rotar_antiguas(p) == 3
        assert len(_todo(p)) == len(antes) and _todo(p) == antes     # mismas lineas, mismo orden
        assert sum(1 for _ in open(p)) == 4                          # cabecera + 3 vivas


def test_pendiente_viejo_bloquea_hasta_muerta():
    with tempfile.TemporaryDirectory() as d:
        R.DIR_PARTES = Path(d) / "partes"
        p = _mk(d, [(9, "1"), (6, ""), (5, "1"), (1, "1")])           # pendiente a 6 d (<10 d muertas): corta ahi
        assert R.rotar_antiguas(p) == 1
        assert [r[1] for r in _todo(p)[1:]] == ["v0", "v1", "v2", "v3"]
        p2 = _mk(d, [(12, ""), (5, "1"), (1, "1")])                   # muerta (>10 d): se mueve
        assert R.rotar_antiguas(p2) == 2


def test_nada_que_rotar_y_idempotente():
    with tempfile.TemporaryDirectory() as d:
        R.DIR_PARTES = Path(d) / "partes"
        p = _mk(d, [(1, "1"), (0.5, "")])
        assert R.rotar_antiguas(p) == 0
        p = _mk(d, [(9, "1"), (1, "1")])
        assert R.rotar_antiguas(p) == 1 and R.rotar_antiguas(p) == 0
