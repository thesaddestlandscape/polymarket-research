"""escritura_atomica.py -- reescritura ATÓMICA de CSV (23-Sep).

Incidente que lo motiva (23-Sep 06:01:52 UTC): `wallet_mirror_tracker.resolver_pendientes()`
reescribía `wallet_mirror_executor_dryrun.csv` con `open(OUT, "w")` (trunca y escribe en el
sitio). Un OOM-kill a mitad de la escritura dejó el fichero cortado tras las filas del 07-Sep:
se perdieron 15 días (08-Sep..23-Sep 06:01) de la evidencia que alimenta el gate de
WALLET_MIRROR. Sin git ni backup de ese CSV -> irrecuperable.

Con este helper el fichero nunca queda a medias: se escribe a un temporal en el MISMO
directorio, fsync, y `os.replace` (atómico en POSIX). Si el proceso muere antes del replace,
el original sigue intacto; si muere después, ya está el nuevo completo.
Los escritores concurrentes deben seguir usando el mismo flock que ya usaban (el replace se
hace dentro de ese lock); los que abren en modo "a" por cada escritura ven el fichero nuevo.
"""
import csv
import os
from pathlib import Path


def _limpiar_tmp_huerfanos(ruta: Path) -> None:
    """Un proceso muerto por SIGKILL/OOM no llega a borrar su temporal (el finally no corre):
    se eliminan los temporales de PIDs que ya no existen (pueden pesar cientos de MB)."""
    for t in ruta.parent.glob(f"{ruta.name}.tmp*"):
        try:
            pid = int(t.name.rsplit(".tmp", 1)[1])
            os.kill(pid, 0)          # sigue vivo -> no tocar
        except ProcessLookupError:
            try:
                t.unlink()
            except OSError:
                pass
        except (ValueError, PermissionError, OSError):
            continue


def escribir_csv_atomico(ruta, fieldnames, filas) -> None:
    ruta = Path(ruta)
    _limpiar_tmp_huerfanos(ruta)
    tmp = ruta.with_name(f"{ruta.name}.tmp{os.getpid()}")
    try:
        with open(tmp, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(filas)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, ruta)
    finally:
        if tmp.exists():
            tmp.unlink()
    try:   # persistir también la entrada de directorio (best effort)
        fd = os.open(ruta.parent, os.O_RDONLY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
    except OSError:
        pass
