#!/usr/bin/env python3
"""extraer_registro_15m.py -- MISIÓN DEFINITIVA 15m (07-Oct): conserva más allá de la retención de 4 días del registro ms
(maker_ms_*.csv.gz, ~1 GB/día) SOLO lo que necesita la misión 15m, para acumular días fuera de muestra:
  k (mapa token -> activo/marco/mercado/cierre/lado), q y t de los tokens 15min, x (aggTrade Binance) y h de los 15min
  (muestreo 100 ms: t,bb,ba,imb1,imb5,imb10,dask5,bid_size,ask_size -> profundidad/pendiente para §7/§9).
Formatos: ver libro_estado_ws.py / m15_ms_cache.py. Salida: datalogs/m15_registro/m15_registro_YYYY-MM-DD.csv.gz
(fuera de git; retención RETENCION_DIAS). Un día ya extraído no se rehace salvo --forzar.
Cron diario 03:45 UTC (día anterior completo, antes de que rote). Uso: python3 extraer_registro_15m.py [--dia D] [--forzar]
"""
import argparse
import gzip
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

DL = Path("/root/polymarket-research-datalogs")
OUT = DL / "m15_registro"
RETENCION_DIAS = 14


def extraer(dia, forzar=False):
    OUT.mkdir(exist_ok=True)
    dst = OUT / f"m15_registro_{dia}.csv.gz"
    if dst.exists() and not forzar:
        print(f"{dia}: ya existe ({dst.stat().st_size / 1e6:.0f} MB)")
        return
    fuentes = sorted(DL.glob(f"maker_ms_{dia}_*.csv.gz"))
    if not fuentes:
        print(f"{dia}: sin ficheros maker_ms (¿ya rotados?)")
        return
    tmp = dst.with_suffix(".tmp")
    n_in = n_out = 0
    t0 = time.time()
    with gzip.open(tmp, "wt", compresslevel=6) as fo:
        fo.write("tipo,t_ms,id,c1,c2,c3,c4,c5\n")
        for f in fuentes:
            m15 = set()
            # 1ª pasada: mapa k del fichero (los k se escriben al ver el token, antes o después de sus filas)
            with gzip.open(f, "rt", errors="replace") as fi:
                try:
                    for ln in fi:
                        if ln.startswith("k,"):
                            c = ln.split(",")
                            if len(c) > 4 and c[4] == "15min":
                                m15.add(c[2])
                            fo.write(ln)
                except (EOFError, OSError):
                    pass
            with gzip.open(f, "rt", errors="replace") as fi:
                try:
                    for ln in fi:
                        n_in += 1
                        tp = ln[:2]
                        if tp == "x," or ((tp in ("q,", "t,", "h,")) and ln.split(",", 3)[2] in m15):
                            fo.write(ln)
                            n_out += 1
                except (EOFError, OSError):
                    pass                                    # final de gzip truncado (corte de un arranque)
    tmp.rename(dst)
    print(f"{dia}: {len(fuentes)} ficheros, {n_in:,} filas -> {n_out:,} ({dst.stat().st_size / 1e6:.0f} MB) "
          f"en {time.time() - t0:.0f} s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dia", default=None)
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()
    dia = a.dia or (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    extraer(dia, a.forzar)
    lim = time.time() - RETENCION_DIAS * 86400
    for f in OUT.glob("m15_registro_*.csv.gz"):
        if f.stat().st_mtime < lim:
            f.unlink()
            print(f"retención: borrado {f.name}")


if __name__ == "__main__":
    main()
