#!/usr/bin/env python3
"""m15_ms_cache.py -- caché compacta del registro ms (maker_ms_*.csv.gz) para la MISIÓN DEFINITIVA 15m (06-Oct).
Una sola lectura de las filas q/t/x de los tokens 15m -> arrays numpy en datalogs/m15_ms_cache/ (fuera de git; borrar al
cerrar la misión: se regenera con este script). Formatos verificados en libro_estado_ws.py (no de memoria):
  q,t_exchange,token,best_bid,best_ask,size_bid,size_ask,t_recepcion   (cada cambio de precio O tamaño del top)
  t,t_exchange,token,precio,side(TOMADOR, auditado 99,86 % vs on-chain),size,t_recepcion,
  x,T(Binance),símbolo,precio,cantidad,m,E,t_recepcion                 (aggTrade; usar T y recepción, nunca E)
  k,...,token,activo,marco,market_id,fin_iso,lado
Uso: (ulimit -v 4000000; python3 m15_ms_cache.py)  ->  q.npz, t.npz, x.npz, tokens.json
Lectura: from m15_ms_cache import cargar; C = cargar()  (dict de arrays + C["tokens"] lista de (token, activo, mid, fin, lado))
"""
import io
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

DL = Path("/root/polymarket-research-datalogs")
OUT = DL / "m15_ms_cache"
FILES = lambda: sorted(DL.glob("maker_ms_2026-10-0[56]_*.csv.gz"))
SIM = {"BTCUSDT": 0, "ETHUSDT": 1, "SOLUSDT": 2, "XRPUSDT": 3, "DOGEUSDT": 4, "BNBUSDT": 5}
MON = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]


def _grep(f, pref):
    p = subprocess.run(f"zcat {f} 2>/dev/null | grep -a '^{pref},'", shell=True, capture_output=True)
    return p.stdout


def _tuberia(f, pref):
    """stdout de zcat|grep como fichero (lectura por trozos: el registro de un día no cabe en memoria de golpe)."""
    return subprocess.Popen(f"zcat {f} 2>/dev/null | grep -a '^{pref},'", shell=True, stdout=subprocess.PIPE)


def construir():
    OUT.mkdir(exist_ok=True)
    toks = {}
    for f in FILES():
        for ln in _grep(f, "k").decode().splitlines():
            r = ln.split(",")
            if len(r) >= 8 and r[4] == "15min":
                toks[r[2]] = (r[3], r[5], int(datetime.fromisoformat(r[6]).timestamp()), r[7])
    lista = sorted(toks)
    idx = {t: i for i, t in enumerate(lista)}
    (OUT / "tokens.json").write_text(json.dumps([[t, *toks[t]] for t in lista]))
    print(f"tokens 15m: {len(lista)}", flush=True)
    partes = {"q": [], "t": [], "x": []}
    for f in FILES():
        print(f"  {f.name}", flush=True)
        for pref, names in (("q", ["k", "te", "tok", "bb", "ba", "bs", "as", "tr"]),
                            ("t", ["k", "te", "tok", "p", "side", "sz", "tr", "z"]),
                            ("x", ["k", "T", "sym", "p", "qty", "m", "E", "tr"])):
            proc = _tuberia(f, pref)
            try:
                lector = pd.read_csv(proc.stdout, header=None, names=names, chunksize=2_000_000, dtype=str,
                                     on_bad_lines="skip", engine="c")
            except pd.errors.EmptyDataError:
                continue
            for ch in lector:
                num = lambda c, dt: pd.to_numeric(ch[c], errors="coerce").to_numpy(dtype=dt, na_value=np.nan) \
                    if dt is np.float32 else pd.to_numeric(ch[c], errors="coerce").fillna(-1).to_numpy(dtype=dt)
                if pref == "x":
                    ch = ch[ch["sym"].isin(SIM)]
                    if ch.empty:
                        continue
                    d = {"T": num("T", np.int64), "tr": num("tr", np.int64), "s": ch["sym"].map(SIM).to_numpy(np.int8),
                         "p": pd.to_numeric(ch["p"], errors="coerce").to_numpy(np.float64),
                         "qty": num("qty", np.float32), "m": num("m", np.int8)}
                else:
                    ch = ch[ch["tok"].isin(idx)]
                    if ch.empty:
                        continue
                    d = {"te": num("te", np.int64), "tr": num("tr", np.int64), "tok": ch["tok"].map(idx).to_numpy(np.int16)}
                    if pref == "q":
                        for c, k in (("bb", "bb"), ("ba", "ba"), ("bs", "bs"), ("as", "as_")):
                            d[k] = num(c, np.float32)               # NaN = lado vacío ("None")
                    else:
                        d.update(p=num("p", np.float32), side=(ch["side"] == "BUY").to_numpy(np.int8), sz=num("sz", np.float32))
                partes[pref].append(d)
                del ch
            proc.wait()
    for pref, ps in partes.items():
        d = {k: np.concatenate([x[k] for x in ps]) for k in ps[0]}
        partes[pref] = None
        orden = np.lexsort((d["T"], d["s"])) if pref == "x" else np.lexsort((d["tr"], d["te"], d["tok"]))
        d = {k: v[orden] for k, v in d.items()}
        np.savez(OUT / f"{pref}.npz", **d)
        print(f"  {pref}: {len(orden)} filas", flush=True)
        del d, orden


def cargar():
    C = {"tokens": json.loads((OUT / "tokens.json").read_text())}
    for pref in ("q", "t", "x"):
        with np.load(OUT / f"{pref}.npz") as z:
            C[pref] = {k: z[k] for k in z.files}
    return C


if __name__ == "__main__":
    construir()
    sys.exit(0)
