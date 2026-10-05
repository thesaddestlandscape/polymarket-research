"""predicciones_archivos.py — acceso a data/shadow/predictions_YYYY-MM-DD.csv[.gz].

05-Oct (disco al 91 %): los predictions_*.csv (~0,68 GB/día) se guardaban sin
comprimir 12 días (~8,3 GB) porque shadow_resolve.py/shadow_postmortem.py los
leen con ventana de 12 días. scripts/comprimir_data_historica.sh los comprime
ahora a partir del 4º día (con `touch -r`, el .gz conserva el mtime del CSV)
y los lectores multi-día pasan por aquí:

- listar(): un fichero por día, ordenado por fecha; si coexisten X.csv y
  X.csv.gz (ventana de segundos mientras se comprime) gana el .csv.
- abrir(): texto UTF-8, plano o gzip.
- stat_logico(): st_size = tamaño SIN comprimir (trailer ISIZE del gzip,
  exacto por debajo de 4 GiB) y el mtime del fichero. Para un CSV comprimido
  con el script da la MISMA firma que tenía el CSV, así que las cachés por
  fichero de resolve/postmortem (validadas por tamaño+mtime) siguen valiendo
  y no se re-parsea nada al comprimir.
- nombre_logico(): nombre sin ".gz", para nombrar cachés por día.
"""
import gzip
import os
import struct
from pathlib import Path
from types import SimpleNamespace

_SUF_GZ = ".gz"


def nombre_logico(path) -> str:
    n = Path(path).name
    return n[:-len(_SUF_GZ)] if n.endswith(_SUF_GZ) else n


def listar(dir_shadow) -> list:
    """predictions_*.csv y predictions_*.csv.gz, uno por día, ordenados por nombre lógico."""
    por_dia = {}
    for p in Path(dir_shadow).glob("predictions_*.csv.gz"):
        por_dia[nombre_logico(p)] = p
    for p in Path(dir_shadow).glob("predictions_*.csv"):
        por_dia[p.name] = p  # el plano gana si coexisten
    return [por_dia[k] for k in sorted(por_dia)]


def ruta_dia(dir_shadow, fecha: str):
    """Ruta del día `fecha` (YYYY-MM-DD), plana o .gz; None si no existe ninguna."""
    plano = Path(dir_shadow) / f"predictions_{fecha}.csv"
    if plano.exists():
        return plano
    gz = plano.with_name(plano.name + _SUF_GZ)
    return gz if gz.exists() else None


def abrir(path):
    path = Path(path)
    if path.name.endswith(_SUF_GZ):
        return gzip.open(path, "rt", encoding="utf-8")
    return open(path, encoding="utf-8")


def stat_logico(path):
    """Como os.stat() (st_size, st_mtime, st_mtime_ns); st_size sin comprimir para .gz."""
    path = Path(path)
    st = os.stat(path)
    if not path.name.endswith(_SUF_GZ):
        return st
    with open(path, "rb") as f:
        f.seek(-4, os.SEEK_END)
        isize = struct.unpack("<I", f.read(4))[0]
    return SimpleNamespace(st_size=isize, st_mtime=st.st_mtime, st_mtime_ns=st.st_mtime_ns)
