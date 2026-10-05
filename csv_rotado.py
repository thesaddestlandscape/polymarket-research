"""csv_rotado.py — rotación sin pérdida de CSV append-only que se leen enteros.

05-Oct (disco al 91 %): data/shadow/dispersed_bot_executor_dryrun.csv pesaba
1,2 GB (5,97 M filas desde el 25-Ago, ~30 MB/día) y sus lectores diarios
(analisis_bot_wallets_gate_bucket_25ago.py, vigia_dispersed_bot_progreso_diario.py)
necesitan TODO el histórico. Cada rotación mueve el fichero vivo a una parte
.csv.gz fuera de git y el escritor (que abre en modo "a" en cada escritura y
pone cabecera si el fichero no existe) crea uno nuevo solo. Los lectores usan
abrir(): partes en orden + fichero vivo con UNA sola cabecera, es decir, las
mismas líneas en el mismo orden que el fichero único de antes.

Uso: python3 csv_rotado.py rotar <ruta.csv>   (cron diario, comprimir_data_historica.sh)
"""
import gzip
import hashlib
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

DIR_PARTES = Path("/root/polymarket-research-datalogs/csv_rotados")
ESPERA_ESCRITOR_S = 10  # un escritor con el fd ya abierto termina su escritura en ms


def _dir_partes(path: Path) -> Path:
    return DIR_PARTES / Path(path).stem


def _fuentes(path: Path) -> list:
    """Partes .csv.gz (orden = orden de rotación) + rotación a medias + fichero vivo."""
    path = Path(path)
    d = _dir_partes(path)
    partes = sorted(d.glob(f"{path.stem}_*.csv.gz")) if d.exists() else []
    con_parte = {p.name[len(path.stem) + 1:-len(".csv.gz")] for p in partes}
    rotando = [r for r in (sorted(d.glob(f"{path.stem}_*.csv.rotando")) if d.exists() else [])
               if r.name[len(path.stem) + 1:-len(".csv.rotando")] not in con_parte]
    vivo = [path] if path.exists() else []
    return partes + rotando + vivo


class _Lector:
    def __init__(self, fuentes):
        self._fuentes = fuentes
        self._f = None
        self._gen = self._lineas()

    def _abrir(self, p: Path):
        if p.name.endswith(".gz"):
            return gzip.open(p, "rt", encoding="utf-8")
        return open(p, encoding="utf-8")

    def _lineas(self):
        cabecera = None
        for p in self._fuentes:
            self._f = self._abrir(p)
            try:
                primera = self._f.readline()
                if cabecera is None:
                    cabecera = primera
                    yield primera
                elif primera and primera != cabecera:
                    yield primera  # fichero creado sin cabecera (carrera con el escritor)
                yield from self._f
            finally:
                self._f.close()
                self._f = None

    def readline(self):
        return next(self._gen, "")

    def __iter__(self):
        return self._gen

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self._gen.close()
        return False


def abrir(path):
    """Como open(path, encoding="utf-8") para leer: readline(), iterable, context manager."""
    return _Lector(_fuentes(Path(path)))


def _sha_texto(p: Path, comprimido: bool) -> str:
    h = hashlib.sha256()
    with (gzip.open(p, "rb") if comprimido else open(p, "rb")) as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def _comprimir_rotando(rot: Path, stem: str) -> None:
    ts = rot.name[len(stem) + 1:-len(".csv.rotando")]
    final = rot.with_name(f"{stem}_{ts}.csv.gz")
    tmp = final.with_name(final.name + ".tmp")
    with open(rot, "rb") as fi, gzip.open(tmp, "wb", compresslevel=6) as fo:
        for bloque in iter(lambda: fi.read(1 << 20), b""):
            fo.write(bloque)
    if _sha_texto(tmp, True) != _sha_texto(rot, False):
        tmp.unlink(missing_ok=True)
        raise RuntimeError(f"verificación fallida, se conserva {rot}")
    os.replace(tmp, final)
    rot.unlink()
    print(f"OK: {rot.name} -> {final}")


def rotar(path) -> None:
    path = Path(path).resolve()
    d = _dir_partes(path)
    d.mkdir(parents=True, exist_ok=True)
    # una rotación anterior que murió a medias se termina primero
    for rot in sorted(d.glob(f"{path.stem}_*.csv.rotando")):
        _comprimir_rotando(rot, path.stem)
    if not path.exists() or path.stat().st_size == 0:
        print(f"SKIP (no existe o vacío): {path}")
        return
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rot = d / f"{path.stem}_{ts}.csv.rotando"
    os.rename(path, rot)  # mismo filesystem: atómico; nunca pasa por data/ (auto-commit)
    time.sleep(ESPERA_ESCRITOR_S)
    _comprimir_rotando(rot, path.stem)


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != "rotar":
        sys.exit("uso: csv_rotado.py rotar <ruta.csv>")
    rotar(sys.argv[2])
