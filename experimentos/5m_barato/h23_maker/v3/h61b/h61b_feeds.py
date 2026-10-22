"""h61b_feeds.py -- cargadores del aggTrade de Binance por RECEPCION (ms). Dos fuentes:
  'reg'  = x_D del registro ms (extracto de maker_ms; el que uso el replay H61): x,T,SIMBOLO,precio,cantidad,m,E,RECEPCION
  'live' = multivenue_ms binance_spot (fetch propio, stream.binance.com aggTrade): bolsa,T,MONEDA,sello_ms,recepcion_ms,precio,cantidad,lado
Devuelven (rx int64 ordenado, p float) o None. Dedup exacto por (rx, p, q) para reinicios solapados."""
import glob
import gzip
import os
import subprocess
import numpy as np

CACHE = os.environ.get("H61B_X", "/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/")
MV = os.environ.get("H61B_MV", "/mnt/HC_Volume_106538179/multivenue_ms/")


def _ordenar(filas):
    if not filas:
        return None
    a = np.array(sorted(set(filas)), dtype=np.float64)   # (rx, p, q)
    a = a[np.argsort(a[:, 0], kind="stable")]
    return a[:, 0].astype(np.int64), a[:, 1], a[:, 2]


def parse_x(lines, simbolo="BTCUSDT"):
    filas = []
    for ln in lines:
        c = ln.rstrip("\n").split(",")
        if len(c) >= 8 and c[0] == "x" and c[2] == simbolo:
            try:
                filas.append((int(c[7]), float(c[3]), float(c[4])))
            except ValueError:
                pass
    return filas


def parse_mv(lines, moneda="BTC"):
    filas = []
    for ln in lines:
        c = ln.rstrip("\n").split(",")
        if len(c) >= 7 and c[0] == "binance_spot" and c[1] == "T" and c[2] == moneda:
            try:
                filas.append((int(c[4]), float(c[5]), float(c[6])))
            except ValueError:
                pass
    return filas


def cargar_reg(D, simbolo="BTCUSDT"):
    f = CACHE + f"x_{D}.csv.gz"
    if not os.path.exists(f):
        return None
    with gzip.open(f, "rt") as fh:
        return _ordenar(parse_x(fh, simbolo))


def ficheros_mv(D):
    return sorted(glob.glob(MV + f"multivenue_ms_{D}_binance_spot_*.csv.gz"))


def cargar_live(D, moneda="BTC"):
    """Solo las filas T de la moneda (grep por zcat: no se carga el fichero entero en Python). Varios ficheros/dia (reinicios) se unen y dedup."""
    fs = ficheros_mv(D)
    if not fs:
        return None
    filas = []
    for f in fs:
        p = subprocess.run(f"nice -n 19 zcat {f} | grep -a ',T,{moneda},'", shell=True, capture_output=True, text=True)
        filas += parse_mv(p.stdout.splitlines(), moneda)
    return _ordenar(filas)
