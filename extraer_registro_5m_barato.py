#!/usr/bin/env python3
"""extraer_registro_5m_barato.py -- 08-Oct (Javi: "no podemos retenerlo solo hasta el 10 de octubre, hay que retenerlo
mucho más tiempo"). Conserva, más allá de la retención de 4 días del registro ms (maker_ms_*.csv.gz, ~1-1,4 GB/día),
SOLO las filas que lee vigia_5m_barato_forward.py, para poder reprocesar cualquier día OOS del vigía congelado.

Garantía de equivalencia: un fichero de salida por fichero de entrada, MISMO nombre, MISMO orden de filas y MISMO mtime
(el vigía ordena por mtime y construye el mapa k en streaming). Se guarda un SUPERCONJUNTO de lo que el vigía usa:
  k y x: todas. l: todas las de tokens 5m/15m. q y t: tokens 15m o 5m que cierran con un 15m, en su último tramo de
  5 min (+5 s), con la misma hora de recepción que usa el vigía; filas ilegibles o de token sin k en el fichero: se
  guardan (el vigía decide). h y b: fuera (el vigía no las lee).
Única diferencia esperable en la salida del vigía: la incidencia de calidad "fichero_truncado" (la copia ya no está
truncada); se anota en el manifiesto del archivo.
Salida: /mnt/HC_Volume_106538179/registro_5m_barato/maker_ms_D_<pid>.csv.gz + manifiesto.json. Retención RETENCION_DIAS.
Reprocesar desde el archivo: vigia_5m_barato_desde_archivo.py --dia D (no toca el fichero congelado del vigía).
Uso: python3 extraer_registro_5m_barato.py [--dia D] [--forzar]. Cron diario 03:50 UTC (día anterior completo).
"""
import argparse
import gzip
import json
import os
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from archivo_volumen import guarda, retencion

DL = Path("/root/polymarket-research-datalogs")
# En el VOLUMEN /dev/sdb (el disco raíz está al 92 %; el volumen aloja también .git y backups: la guarda protege su
# espacio libre).
OUT = Path("/mnt/HC_Volume_106538179/registro_5m_barato")
RETENCION_DIAS = 60


def _cierre(iso):
    return int(datetime.fromisoformat(iso).timestamp())


def extraer_fichero(src, dst):
    mapa = {}                                   # token -> (marco, cierre) desde las k del propio fichero
    with gzip.open(src, "rt", errors="replace") as fi:
        try:
            for ln in fi:
                if ln.startswith("k,"):
                    c = ln.rstrip("\n").split(",")
                    try:
                        mapa[c[2]] = (c[4], _cierre(c[6]))
                    except (IndexError, ValueError):
                        pass
        except (EOFError, OSError):
            pass
    n_in = n_out = 0
    truncado = False
    tmp = dst.with_name(dst.name + ".tmp")
    with gzip.open(src, "rt", errors="replace") as fi, gzip.open(tmp, "wt", compresslevel=6) as fo:
        try:
            for ln in fi:
                n_in += 1
                tp = ln[:2]
                if tp in ("k,", "x,"):
                    fo.write(ln)
                    n_out += 1
                    continue
                if tp not in ("q,", "t,", "l,", "L,"):     # L (14-Oct): libro ask completo de los pares BTC
                    continue
                c = ln.rstrip("\n").split(",")
                m = mapa.get(c[2]) if len(c) > 2 else None
                if m is None:
                    fo.write(ln)                      # sin k en este fichero: decide el vigía
                    n_out += 1
                    continue
                marco, cie = m
                if marco not in ("5min", "15min"):
                    continue
                if tp in ("l,", "L,"):
                    fo.write(ln)
                    n_out += 1
                    continue
                if marco == "5min" and cie % 900:
                    continue
                try:
                    k = 7 if tp == "q," else 6
                    tr = int(c[k]) if len(c) > k and c[k] else int(c[1])
                except (ValueError, IndexError):
                    fo.write(ln)                      # ilegible: el vigía la cuenta en calidad
                    n_out += 1
                    continue
                if (cie - 300) * 1000 - 5000 <= tr <= cie * 1000:
                    fo.write(ln)
                    n_out += 1
        except (EOFError, OSError):
            truncado = True
    st = src.stat()
    os.utime(tmp, (st.st_atime, st.st_mtime))
    tmp.rename(dst)
    return {"filas_in": n_in, "filas_out": n_out, "origen_truncado": truncado, "mb": round(dst.stat().st_size / 1e6, 1)}


def extraer(dia, forzar=False):
    OUT.mkdir(exist_ok=True)
    man_f = OUT / "manifiesto.json"
    man = json.loads(man_f.read_text()) if man_f.exists() else {}
    fuentes = sorted(DL.glob(f"maker_ms_{dia}_*.csv.gz"))
    if not fuentes:
        print(f"{dia}: sin ficheros maker_ms (¿ya rotados?)")
        return
    t0 = time.time()
    for src in fuentes:
        dst = OUT / src.name
        if dst.exists() and not forzar and src.name in man and man[src.name].get("mtime_origen") == src.stat().st_mtime:
            continue
        r = extraer_fichero(src, dst)
        r.update({"dia": dia, "mtime_origen": src.stat().st_mtime, "extraido_utc": datetime.now(timezone.utc).isoformat()})
        man[src.name] = r
        print(f"{src.name}: {r['filas_in']:,} -> {r['filas_out']:,} filas ({r['mb']} MB, truncado={r['origen_truncado']})")
    tmp = man_f.with_name("manifiesto.json.tmp")
    tmp.write_text(json.dumps(man, indent=1))
    tmp.rename(man_f)
    print(f"{dia}: {len(fuentes)} ficheros en {time.time() - t0:.0f} s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dia", default=None)
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()
    dia = a.dia or (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    extraer(dia, a.forzar)
    retencion("registro_5m_barato", RETENCION_DIAS)
    guarda()                    # 09-Oct: guarda ÚNICA para todos los archivos 60 d del volumen (5m + 15m)


if __name__ == "__main__":
    main()
