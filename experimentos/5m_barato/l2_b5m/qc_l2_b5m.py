#!/usr/bin/env python3
"""qc_l2_b5m.py -- control de calidad SOLO LECTURA del feed L2 5m (libro5_ms) para medir la carrera cancelacion-vs-tomador.
No es un logger: libro5 (libro_estado_ws._Libro5) ya graba B (libro completo), d (price_change por nivel, tamano absoluto),
T (last_trade_price) y G (huecos) de todos los tokens 5m, con t_ms (exchange, sello de LOTE) y recepcion (c[6]) y seq.
Mide por DIA: ficheros truncados, filas por tipo, huecos G por motivo, seq no monotona, libros cruzados (bid>=ask tras un d),
tokens con B y cobertura del tx (libro5_tx) sobre los T. Reloj: ordenar por seq/recepcion, NUNCA por t_ms.
Uso: nice -n 19 ionice -c3 python3 -I qc_l2_b5m.py 2026-11-09 [--dir DIR_LIBRO5] [--tx DIR_TX] [--max-lineas N]
"""
import argparse, csv, glob, gzip, io, json, os, sys, zlib
from collections import Counter

LIBRO5 = "/mnt/HC_Volume_106538179/libro5_ms"
TXDIR = "/mnt/HC_Volume_106538179/libro5_tx"


def _lineas(path, max_lineas=None):
    """Genera lineas de un gzip tolerando el truncado final; devuelve (iterador, estado) donde estado['truncado']."""
    estado = {"truncado": False}

    def it():
        n = 0
        try:
            with gzip.open(path, "rt", errors="replace") as f:
                for ln in f:
                    yield ln
                    n += 1
                    if max_lineas and n >= max_lineas:
                        return
        except (EOFError, zlib.error, OSError):
            estado["truncado"] = True
    return it(), estado


def _niveles(txt):
    out = {}
    for kv in txt.split(";"):
        if ":" in kv:
            p, s = kv.split(":", 1)
            try:
                out[float(p)] = float(s)
            except ValueError:
                pass
    return out


def qc_fichero(path, max_lineas=None):
    tipos, gm = Counter(), Counter()
    seq_mal = cruzados = filas_t = 0
    ult_seq = None
    libros = {}                       # token -> [bids{}, asks{}]  (estado por seq; se pierde tras G del token)
    tokens_b, ts_T = set(), []
    it, est = _lineas(path, max_lineas)
    for ln in it:
        c = ln.rstrip("\n").split(",")
        if len(c) < 8 or c[0] == "tipo":
            continue
        t = c[0]
        tipos[t] += 1
        try:
            seq = int(c[7])
        except ValueError:
            continue
        if ult_seq is not None and seq <= ult_seq and not c[0] == "G":
            seq_mal += 1
        ult_seq = seq
        if t == "B":
            libros[c[2]] = [_niveles(c[3]), _niveles(c[4])]
            tokens_b.add(c[2])
        elif t == "d" and c[2] in libros:
            lado = libros[c[2]][0 if c[3] == "B" else 1]
            try:
                p, s = float(c[4]), float(c[5])
            except ValueError:
                continue
            if s <= 0:
                lado.pop(p, None)
            else:
                lado[p] = s
            b, a = libros[c[2]]
            if b and a and max(b) >= min(a):
                cruzados += 1
        elif t == "T":
            filas_t += 1
            ts_T.append((c[2], int(c[1])))
        elif t == "G":
            gm[c[3]] += 1
            if c[2] == "*":
                libros.clear()
            else:
                libros.pop(c[2], None)
    return {"fichero": os.path.basename(path), "truncado": est["truncado"], "filas": dict(tipos), "huecos_G": dict(gm),
            "seq_no_monotona": seq_mal, "libros_cruzados_tras_d": cruzados, "tokens_con_B": len(tokens_b)}, ts_T


def cobertura_tx(tx_files, ts_T):
    """Fraccion de T con una fila de libro5_tx (token igual y |t_ev - t_T| <= 5 ms); t_ev es el sello de lote del exchange."""
    pares = {}
    for f in tx_files:
        op = gzip.open if f.endswith(".gz") else open
        try:
            with op(f, "rt") as fh:
                for r in csv.reader(fh):
                    if len(r) >= 3 and r[0].isdigit():
                        pares.setdefault(r[1], []).append(int(r[0]))
        except (EOFError, OSError, zlib.error):
            pass
    if not ts_T:
        return None
    ok = 0
    for tok, t in ts_T:
        if any(abs(t - x) <= 5 for x in pares.get(tok, ())):
            ok += 1
    return {"T": len(ts_T), "con_tx": ok, "frac": round(ok / len(ts_T), 4)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dia")
    ap.add_argument("--dir", default=LIBRO5)
    ap.add_argument("--tx", default=TXDIR)
    ap.add_argument("--max-lineas", type=int, default=None)
    a = ap.parse_args()
    ficheros = sorted(glob.glob(os.path.join(a.dir, f"libro5_ms_{a.dia}_*.csv.gz")))
    if not ficheros:
        print(json.dumps({"dia": a.dia, "error": "sin ficheros libro5 (MISSING, no es 0)"}))
        return 1
    res, todos_T = [], []
    for f in ficheros:
        r, ts = qc_fichero(f, a.max_lineas)
        res.append(r)
        todos_T += ts
    tx_files = sorted(glob.glob(os.path.join(a.tx, f"libro5_tx_{a.dia}_*.csv*")))
    out = {"dia": a.dia, "ficheros": res, "tx": cobertura_tx(tx_files, todos_T) if tx_files else "MISSING"}
    print(json.dumps(out, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
