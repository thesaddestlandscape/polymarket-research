#!/usr/bin/env python3
"""extraer_onchain_15m.py -- MISIÓN 15M v2 (07-Oct): conserva 60 días (09-Oct, antes 30; en el VOLUMEN /dev/sdb) de los rellenos ON-CHAIN de los mercados 15m.
onchain_fills_YYYY-MM-DD.csv.gz (fetch_polymarket_fills_onchain.py, ~3,9 M filas/día, retención 4 d) trae cada relleno con
MAKER y TOMADOR explícitos, lado, token, importes y comisión: la única fuente sin contaminar para flujo tomador, identidad
de quien captura y comisión realmente cobrada. Aquí se guardan solo las filas de tokens 15m (mapa k de
datalogs/m15_registro/m15_registro_D.csv.gz y de los días vecinos). Salida datalogs/m15_onchain/m15_onchain_D.csv.gz.
Cron 03:55 UTC (tras extraer_registro_15m 03:45). Uso: python3 extraer_onchain_15m.py [--dia D] [--forzar]
09-Oct (MISIÓN 5M, Javi): --marco 5min -> rellenos de tokens 5m en m5_onchain/m5_onchain_D.csv.gz (el mapa k sale
del mismo m15_registro, que guarda las filas k de TODOS los marcos). Cron 04:10.
"""
import argparse
import gzip
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

from archivo_volumen import VOL, guarda, retencion

DL = Path("/root/polymarket-research-datalogs")
REG = VOL / "m15_registro"
OUT = VOL / "m15_onchain"       # datalogs/m15_onchain es un enlace simbólico aquí
MARCO, PREF = "15min", "m15"


def tokens_15m(dia):
    d = date.fromisoformat(dia)
    toks = set()
    for k in (-1, 0, 1):
        f = REG / f"m15_registro_{(d + timedelta(days=k)).isoformat()}.csv.gz"
        if not f.exists():
            continue
        with gzip.open(f, "rt", errors="replace") as fh:
            try:
                for ln in fh:
                    if ln.startswith("k,"):
                        c = ln.split(",")
                        if len(c) > 4 and c[4] == MARCO:
                            toks.add(c[2])
            except (EOFError, OSError):
                pass
    return toks


def extraer(dia, forzar=False):
    OUT.mkdir(exist_ok=True)
    dst = OUT / f"{PREF}_onchain_{dia}.csv.gz"
    if dst.exists() and not forzar:
        print(f"{dia}: ya existe")
        return
    src = DL / f"onchain_fills_{dia}.csv.gz"
    if not src.exists():
        print(f"{dia}: sin {src.name} (¿rotado?)")
        return
    toks = tokens_15m(dia)
    if not toks:
        print(f"{dia}: sin mapa de tokens {MARCO} (falta m15_registro): NO se extrae (fail-closed)")
        return
    t0, n_in, n_out = time.time(), 0, 0
    tmp = dst.with_suffix(".tmp")
    with gzip.open(src, "rt", errors="replace") as fi, gzip.open(tmp, "wt", compresslevel=6) as fo:
        cab = fi.readline()
        fo.write(cab)
        i_tok = cab.rstrip("\n").split(",").index("token_id")
        try:
            for ln in fi:
                n_in += 1
                c = ln.split(",", i_tok + 2)
                if len(c) > i_tok and c[i_tok] in toks:
                    fo.write(ln)
                    n_out += 1
        except (EOFError, OSError):
            pass
    tmp.rename(dst)
    print(f"{dia}: {len(toks)} tokens {MARCO}, {n_in:,} filas -> {n_out:,} ({dst.stat().st_size / 1e6:.0f} MB) en {time.time() - t0:.0f} s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dia", default=None)
    ap.add_argument("--forzar", action="store_true")
    ap.add_argument("--marco", choices=("15min", "5min"), default="15min")
    a = ap.parse_args()
    global MARCO, PREF, OUT
    MARCO, PREF = a.marco, {"15min": "m15", "5min": "m5"}[a.marco]
    OUT = VOL / f"{PREF}_onchain"
    extraer(a.dia or (datetime.now(timezone.utc) - timedelta(days=1)).strftime("%Y-%m-%d"), a.forzar)
    retencion(f"{PREF}_onchain")
    guarda()


if __name__ == "__main__":
    main()
