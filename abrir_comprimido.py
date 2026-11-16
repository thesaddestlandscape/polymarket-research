"""Abre .gz, .zst o texto plano con la misma llamada (16-Nov). Python 3.14: zstd viene en la stdlib (compression.zstd)."""
import gzip
from compression import zstd


def abrir(path, mode="rt", **kw):
    p = str(path)
    if p.endswith(".zst"):
        return zstd.open(p, mode, **kw)
    if p.endswith(".gz"):
        return gzip.open(p, mode, **kw)
    return open(p, mode, **kw)
