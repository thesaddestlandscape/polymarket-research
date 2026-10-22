#!/usr/bin/env python3
"""h23_pares_lector.py -- lector del REGISTRO PROPIO DE PARES de h23_shadow_v3r.py (--registro-dir) con la MISMA interfaz que simlib.grupos/kmap del replay h23_sim_v3.py.

Formato (h23_pares_<COIN>_<YYYY-MM-DD>.csv.gz, miembros gzip anadidos; el dia es el de la hora de RECEPCION de la fila; un par que cruza medianoche tiene filas en 2 ficheros):
  P,<C>,<mkt5>,<mkt15>,<tok5u>,<tok5d>,<tok15u>,<tok15d>,<COIN>,<t_open_rel>   alta del par (C = cierre en epoch s; t_open_rel = ms respecto a C*1000)
  q,<C>,<slot>,<recv_rel>,<ev_rel>,<bid>,<ask>,<bsz>,<asz>,<src>             top del libro del token `slot` (0=5m Up, 1=5m Down, 2=15m Up, 3=15m Down) tras un mensaje;
                                                                              se escribe SOLO si el top (precio o tamano) cambia, mas SIEMPRE en snapshots del servidor
                                                                              (src=b), y una foto de estado a C-310 s (src=s). recv_abs = C*1000+recv_rel; ev_abs = recv_abs+ev_rel
  t,<C>,<slot>,<recv_rel>,<ev_rel>,<precio>,<BUY|SELL>,<tamano>               last_trade_price del token
  g,<C>,<grp>,<recv_rel>,<motivo>                                             la conexion del grupo `grp` cayo (los libros de SUS tokens quedan fuera hasta el siguiente snapshot)
  c,<C>,<grp>,<recv_rel>                                                      conexion establecida y suscrita
A diferencia de maker_ms: las caidas SE MARCAN (g), tras reconectar hay snapshot (q src=b) y el estado a la apertura de ventana esta fijado (src=s).
Salida de `grupos`: (C, {token: simlib.Q}, {token: simlib.T}) con rx = recepcion en ms (mismo reloj que el registro maker_ms), como simlib.grupos.
"""
import glob
import gzip
import os
import sys
import zlib
from datetime import datetime, timedelta, timezone

import numpy as np

REGISTRO_DEFECTO = "/mnt/HC_Volume_106538179/h23_pares"
SLOTS = ("5u", "5d", "15u", "15d")


def lineas(path):
    """Lectura tolerante de miembros gzip anadidos (el ultimo puede estar truncado)."""
    try:
        data = open(path, "rb").read()
    except OSError:
        return
    while data:
        d = zlib.decompressobj(31)
        try:
            txt = d.decompress(data)
        except zlib.error:
            return
        ls = txt.decode(errors="replace").splitlines()
        if not d.eof and ls:
            ls = ls[:-1]                 # miembro truncado por un corte brusco: la ultima linea puede estar a medias
        yield from ls
        data = d.unused_data
        if not d.eof:
            return


def _dia_de_cierre(C):
    """Dia del vigia (controles_D): cierres D 00:15 .. D+1 00:00 -> D."""
    return datetime.fromtimestamp(C - 1, timezone.utc).strftime("%Y-%m-%d")


def cargar(coin, dia, dirn=REGISTRO_DEFECTO):
    """-> (pares, filas): pares[C] = dict(mkt5, mkt15, toks=[4], huecos=[(grp, recv_abs, motivo)], conex=[(grp, recv_abs)], q=[...], t=[...]) para los cierres del dia `dia`.
    Lee los ficheros de dia-1, dia y dia+1 (un par cruza medianoche)."""
    d0 = datetime.strptime(dia, "%Y-%m-%d").date()
    pares = {}
    for dd in (d0 - timedelta(days=1), d0, d0 + timedelta(days=1)):
        f = os.path.join(dirn, f"h23_pares_{coin}_{dd.isoformat()}.csv.gz")
        if not os.path.exists(f):
            continue
        for ln in lineas(f):
            c = ln.split(",")
            if not c or len(c) < 4:
                continue
            try:
                C = int(c[1])
            except ValueError:
                continue
            if _dia_de_cierre(C) != dia:
                continue
            k = c[0]
            if k == "P":
                if len(c) >= 10 and C not in pares:
                    pares[C] = dict(mkt5=c[2], mkt15=c[3], toks=c[4:8], huecos=[], conex=[], q=[], t=[])
                continue
            p = pares.get(C)
            if p is None:
                continue
            base = C * 1000
            try:
                if k == "q":
                    rx = base + int(c[3])
                    p["q"].append((int(c[2]), rx, rx + int(c[4]), c[5], c[6], c[7], c[8], c[9] if len(c) > 9 else ""))
                elif k == "t":
                    rx = base + int(c[3])
                    p["t"].append((int(c[2]), rx, rx + int(c[4]), float(c[5]), 1.0 if c[6] == "BUY" else 0.0, float(c[7])))
                elif k == "g":
                    p["huecos"].append((int(c[2]), base + int(c[3]), c[4] if len(c) > 4 else ""))
                elif k == "c":
                    p["conex"].append((int(c[2]), base + int(c[3])))
            except (ValueError, IndexError):
                continue
    return pares


def _nan(x):
    return np.nan if x in ("", "None") else float(x)


def kmap(pares):
    """Equivalente a h23_sim_v3.kmap: (marco, C, lado) -> (token, mercado)."""
    km = {}
    for C, p in pares.items():
        t5u, t5d, t15u, t15d = p["toks"]
        km[("5min", C, "YES")] = (t5u, p["mkt5"])
        km[("5min", C, "NO")] = (t5d, p["mkt5"])
        km[("15min", C, "YES")] = (t15u, p["mkt15"])
        km[("15min", C, "NO")] = (t15d, p["mkt15"])
    return km


def grupos(pares, simlib):
    """Itera (C, {token: Q}, {token: T}) ordenado por C, con las clases de simlib (mismo orden (rx, ex) y mismos tipos que el replay del registro)."""
    for C in sorted(pares):
        p = pares[C]
        q = {tk: [] for tk in p["toks"]}
        t = {tk: [] for tk in p["toks"]}
        for slot, rx, ex, bid, ask, bsz, asz, src in p["q"]:
            q[p["toks"][slot]].append((rx, ex, _nan(bid), _nan(ask), _nan(bsz) if bsz else 0.0, _nan(asz) if asz else 0.0))
        for slot, rx, ex, px, buy, sz in p["t"]:
            t[p["toks"][slot]].append((rx, ex, px, buy, sz))
        yield C, {k: simlib.Q(v) for k, v in q.items()}, {k: simlib.T(v) for k, v in t.items()}


def huecos_en_ventana(p, C, lo_s=298.5, hi_s=10.0):
    """Huecos (grp, recv, motivo) cuyo instante cae dentro de la ventana de cotizacion [C-298,5 s, C-10 s] o en los 5 s previos (el hueco arrastra el estado)."""
    lo, hi = (C - lo_s) * 1000 - 5000, (C - hi_s) * 1000
    return [h for h in p["huecos"] if lo <= h[1] <= hi]
