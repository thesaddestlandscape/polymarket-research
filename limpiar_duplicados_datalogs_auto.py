#!/usr/bin/env python3
"""limpiar_duplicados_datalogs_auto.py (04-Nov, Javi: "no podemos consumir espacio tan rápido"). mover_datalogs_a_sdb.sh deja X.csv en el volumen y luego
comprimir_data_historica crea X.csv.gz; el CSV plano quedaba duplicado para siempre (4,6 GB de polymarket_activity, 25-31 Oct). Borra de
/mnt/HC_Volume.../datalogs_auto el X.csv SOLO si el X.csv.gz del mismo nombre en datalogs (o su destino) existe, descomprime IDÉNTICO byte a byte y el CSV tiene >2 d.
Cron 03:50 UTC. Uso: [--dry-run]"""
import gzip
import os
import shutil
import sys
import time
from pathlib import Path

DA = Path("/mnt/HC_Volume_106538179/datalogs_auto")
RAIZ = Path("/root/polymarket-research-datalogs")


def identicos(gz, csv):
    with gzip.open(gz, "rb") as a, open(csv, "rb") as b:
        while True:
            x, y = a.read(1 << 20), b.read(1 << 20)
            if x != y:
                return False
            if not x:
                return True


def main():
    dry = "--dry-run" in sys.argv
    libre = 0
    for csv in sorted(DA.glob("*.csv")):
        if csv.is_symlink() or time.time() - csv.stat().st_mtime < 2 * 86400:
            continue
        gz = Path(os.path.realpath(RAIZ / (csv.name + ".gz")))
        if not gz.is_file() or gz == csv:
            continue
        try:
            if identicos(gz, csv):
                sz = csv.stat().st_size
                print(f"duplicado idéntico {csv.name} ({sz // 1048576} MB)" + (" [dry]" if dry else " borrado"))
                if not dry:
                    csv.unlink()
                libre += sz
            else:
                print(f"DIFERENTE, no se borra: {csv.name}")
        except OSError as e:
            print(f"error {csv.name}: {e}")
    print(f"liberado {libre / 1073741824:.2f} GB")


if __name__ == "__main__":
    main()
