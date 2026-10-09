#!/usr/bin/env python3
"""extraer_registro_15m.py -- MISIÓN DEFINITIVA 15m (07-Oct): conserva más allá de la retención de 4 días del registro ms
(maker_ms_*.csv.gz, ~1 GB/día) SOLO lo que necesita la misión 15m, para acumular días fuera de muestra:
  k (mapa token -> activo/marco/mercado/cierre/lado), q y t de los tokens 15min, x (aggTrade Binance).
  (Las filas h NO se guardan: el hijo de libro_estado_ws solo escribe t,bb,ba,bs,as -- nivel 1 muestreado, redundante
  con q; la profundidad multinivel nunca se ha registrado en disco, ver libro_l2_15m_fase0.py.)
Formatos: ver libro_estado_ws.py / m15_ms_cache.py. Salida: VOLUMEN /mnt/HC_Volume_106538179/m15_registro/ (09-Oct, Javi:
60 días como el 5m; datalogs/m15_registro es un enlace simbólico ahí). Retención y guarda de espacio: archivo_volumen.py. Un día ya extraído no se rehace salvo --forzar.
Cron diario 03:45 UTC (día anterior completo, antes de que rote). Uso: python3 extraer_registro_15m.py [--dia D] [--forzar]
09-Oct (MISIÓN 5M, Javi): --marco 5min -> lo mismo para los tokens 5m en m5_registro/m5_registro_D.csv.gz (cron 04:00).
"""
import argparse
import gzip
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from archivo_volumen import VOL, guarda, retencion

DL = Path("/root/polymarket-research-datalogs")
MARCO, PREF = "15min", "m15"
OUT = VOL / "m15_registro"


def extraer(dia, forzar=False):
    OUT.mkdir(exist_ok=True)
    dst = OUT / f"{PREF}_registro_{dia}.csv.gz"
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
                            if len(c) > 4 and c[4] == MARCO:
                                m15.add(c[2])
                            fo.write(ln)
                except (EOFError, OSError):
                    pass
            with gzip.open(f, "rt", errors="replace") as fi:
                try:
                    for ln in fi:
                        n_in += 1
                        tp = ln[:2]
                        if tp == "x," or ((tp == "q," or tp == "t,") and ln.split(",", 3)[2] in m15):
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
    ap.add_argument("--marco", choices=("15min", "5min"), default="15min")
    a = ap.parse_args()
    global MARCO, PREF, OUT
    MARCO, PREF = a.marco, {"15min": "m15", "5min": "m5"}[a.marco]
    OUT = VOL / f"{PREF}_registro"
    dia = a.dia or (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d")
    extraer(dia, a.forzar)
    retencion(f"{PREF}_registro")
    guarda()


if __name__ == "__main__":
    main()
