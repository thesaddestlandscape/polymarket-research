"""h59_lectura.py -- COPIA LITERAL (20-Oct) de las funciones de lectura de ../h55_forward/m5b_anidado_dia.py (Col, i_en, twap_refs, leer),
sin la logica de H55/H53/maker. Se copia para que editar el vigia H55 no invalide la congelacion de H59 (su hash cubre este fichero).
Lee el registro ms crudo (solo lectura, BTC). Test de equivalencia con el original: test_h59.py::test_lectura_identica_a_h55."""
import argparse, bisect, collections, csv, glob, gzip, hashlib, json, os, sys, time
from array import array
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

DL = Path(os.environ.get("M5B_DL", "/root/polymarket-research-datalogs"))
PRICES = Path(os.environ.get("M5B_PRICES", "/root/polymarket-research/data/prices"))


class Col:
    """Serie de filas q de un token: columnas array (rx, ex, bid, ask, bsz, asz). None -> NaN."""
    __slots__ = ("rx", "ex", "c")
    def __init__(self):
        self.rx, self.ex, self.c = array("q"), array("q"), array("d")
    def add(self, rx, ex, b, a, bs, as_):
        self.rx.append(rx); self.ex.append(ex); self.c.extend((b, a, bs, as_))
    def np(self):
        rx, ex = np.frombuffer(self.rx, dtype=np.int64), np.frombuffer(self.ex, dtype=np.int64)
        c = np.frombuffer(self.c, dtype=np.float64).reshape(-1, 4) if len(self.rx) else np.zeros((0, 4))
        o = np.lexsort((ex, rx))                          # orden (rx, ex), estable
        return rx[o], c[o, 0], c[o, 1], c[o, 2], c[o, 3]


def i_en(rx, t):
    return np.searchsorted(rx, t, side="right") - 1


def twap_refs(dias):
    tw = collections.defaultdict(dict)
    for d in dias:
        for suf in (".csv", ".csv.gz"):
            f = PRICES / f"polybolt_{d}{suf}"
            if f.exists():
                with (gzip.open(f, "rt") if suf.endswith("gz") else open(f)) as fh:
                    for r in csv.DictReader(fh):
                        if r["canal"] == "twap60" and r.get("source", "chainlink") == "chainlink":
                            e = int(r["event_ts_ms"]) // 1000
                            if e % 300 == 0:
                                tw[r["asset"]][e] = float(r["value"])
    return tw


def leer(dia, ficheros, t_lo, t_hi, cal):
    meta, idx = {}, collections.defaultdict(dict)
    qs, ts = collections.defaultdict(Col), collections.defaultdict(list)
    ult_rx = {}
    num = lambda x: np.nan if x in ("", "None") else float(x)
    for f in ficheros:
        try:
            with gzip.open(f, "rt") as fh:
                for ln in fh:
                    tp = ln[:2]
                    if tp == "k,":
                        c = ln.rstrip("\n").split(",")
                        if len(c) > 7 and c[3] == "BTC" and c[4] in ("5min", "15min"):
                            cie = int(datetime.fromisoformat(c[6]).timestamp())
                            meta[c[2]] = (c[4], c[5], cie, c[7])
                            idx[cie][(c[4], c[7])] = c[2]
                        continue
                    if tp not in ("q,", "t,"):
                        continue
                    c = ln.split(",", 3)
                    m = meta.get(c[2]) if len(c) > 3 else None
                    if m is None or not (t_lo < m[2] <= t_hi) or (m[0] == "5min" and m[2] % 900):
                        continue
                    c = ln.rstrip("\n").split(",")
                    try:
                        if tp == "q,":
                            rx = int(c[7]) if len(c) > 7 and c[7] else int(c[1])
                            if not ((m[2] - 300) * 1000 - 5000 <= rx <= m[2] * 1000):
                                continue
                            b, a, bs, as_ = num(c[3]), num(c[4]), num(c[5]), num(c[6])
                            if (b == b and not 0 < b < 1) or (a == a and not 0 < a < 1):
                                cal["precio_imposible"] += 1; continue
                            if (bs == bs and bs < 0) or (as_ == as_ and as_ < 0):
                                cal["tamano_negativo"] += 1; continue
                            if b == b and a == a and b > a:
                                cal["libro_cruzado_bid>ask"] += 1
                            if c[2] in ult_rx and rx < ult_rx[c[2]]:
                                cal["recepcion_no_monotona"] += 1
                            ult_rx[c[2]] = max(rx, ult_rx.get(c[2], 0))
                            qs[c[2]].add(rx, int(c[1]), b, a, 0.0 if bs != bs else bs, 0.0 if as_ != as_ else as_)
                        elif m[0] == "5min":
                            rx = int(c[6]) if len(c) > 6 and c[6] else int(c[1])
                            if not ((m[2] - 300) * 1000 - 5000 <= rx <= m[2] * 1000):
                                continue
                            ts[c[2]].append((rx, int(c[1]), float(c[3]), 1.0 if c[4] == "BUY" else 0.0, float(c[5])))
                    except (ValueError, IndexError):
                        cal["fila_ilegible"] += 1
        except (EOFError, OSError):
            cal[f"fichero_truncado:{Path(f).name}"] += 1
    return meta, idx, qs, ts


