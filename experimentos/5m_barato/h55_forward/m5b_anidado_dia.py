"""m5b_anidado_dia.py -- Extraccion DIARIA (solo lectura, BTC) de las entradas H55 / H53 / V4(replica nivel 1) / maker H23 por cierre.
Lee el registro ms crudo del dia (DL/maker_ms_D*.csv.gz, ficheros con nombre D y D+1, como el vigia V4), filtra BTC, reconstruye
por cierre C (multiplo de 900, C en (D 00:00, D+1 00:00]) los libros 5m/15m por HORA DE RECEPCION y aplica las reglas de
m5b_anidado_regla (la unica copia de la decision). NO firma, NO envia, NO escribe fuera de DL/vigia_5m_barato_anidado/.
Salida: entradas_D.csv.gz (1 fila por cierre; clave unica = cierre), entradas_D.meta.json, calidad_D.csv. Idempotente: se reemplaza
el fichero completo de forma atomica; nunca se anexa.
Uso: nice -n 19 ionice -c3 python3 -I m5b_anidado_dia.py --dia YYYY-MM-DD [--forzar]   (ulimit -v 3000000)
"""
import argparse, bisect, collections, csv, glob, gzip, hashlib, json, os, sys, time
from array import array
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import m5b_anidado_regla as R  # noqa: E402

DL = Path(os.environ.get("M5B_DL", "/root/polymarket-research-datalogs"))
PRICES = Path(os.environ.get("M5B_PRICES", "/root/polymarket-research/data/prices"))
SALIDA = Path(os.environ.get("M5B_SALIDA", str(DL / "vigia_5m_barato_anidado")))
CAMPOS = ["dia", "cierre", "lado", "m5", "n_inst", "ref15", "ref5", "gap_bps"]
for _r in ("v4", "h53", "h55"):
    CAMPOS += [f"{_r}_t", f"{_r}_m", f"{_r}_ask5", f"{_r}_bid15", f"{_r}_lim", f"{_r}_ask_llegada", f"{_r}_asz_llegada",
               f"{_r}_edad_llegada_ms", f"{_r}_acc", f"{_r}_precio"]
CAMPOS += ["mk_lleno", "mk_coste", "mk_t_rel", "mk_p_rel", "mk_n_cotiz", "mk_n_fill"]


def hash_codigo():
    h = hashlib.sha256()
    for f in sorted(AQUI.glob("m5b_anidado_*.py")):
        h.update(f.name.encode() + f.read_bytes())
    return h.hexdigest()[:16]


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


def evaluar_cierre(C, lado, m5id, tok, qs, ts, cal):
    """-> dict de la fila (CAMPOS) o None. tok = {(marco, 'YES'/'NO'): token}. Sin look-ahead: estado = ultima fila con rx <= t."""
    sl = "YES" if lado == "Up" else "NO"
    ol = "NO" if sl == "YES" else "YES"
    k5, k15, k5o = tok.get(("5min", sl)), tok.get(("15min", sl)), tok.get(("5min", ol))
    if not (k5 and k15) or k5 not in qs or k15 not in qs:
        cal["cierre_sin_libro"] += 1
        return None
    r5, b5, a5, bs5, as5 = qs[k5].np()
    r15, b15, a15, _, _ = qs[k15].np()
    t_ini, t_fin = (C - 300) * 1000 + R.REF_CONOCIBLE_MS, (C - R.FIN_MARGEN_S) * 1000
    inst = np.unique(np.concatenate([r5, r15]))
    inst = inst[(inst >= t_ini) & (inst < t_fin)]
    if not len(inst):
        cal["cierre_sin_instantes"] += 1
        return None
    i5, i15 = i_en(r5, inst), i_en(r15, inst)
    ok = (i5 >= 0) & (i15 >= 0)
    inst, i5, i15 = inst[ok], i5[ok], i15[ok]
    ask5, bid5, bsz5, asz5 = a5[i5], b5[i5], bs5[i5], as5[i5]
    bid15, ask15 = b15[i15], a15[i15]
    row = {"n_inst": len(inst)}
    for regla in ("v4", "h53", "h55"):
        s = R.senal(regla.upper(), ask5, bid15, bid5, ask15)
        if not s.any():
            continue
        k = int(np.argmax(s))
        t0, a0, bb = int(inst[k]), float(ask5[k]), float(bid15[k])
        lim = R.limite_orden(regla.upper(), a0, bb)
        acc_obj = R.acciones_objetivo(a0)
        te = t0 + R.LAT_TOMADOR_MS
        j = int(i_en(r5, te))
        al = float(a5[j]) if j >= 0 else float("nan")
        az = float(as5[j]) if j >= 0 else 0.0
        acc, pr = R.llegada_tomador(al, az, lim, acc_obj)
        row.update({f"{regla}_t": t0, f"{regla}_m": round(float(R.margen(bb, a0)), 6), f"{regla}_ask5": a0, f"{regla}_bid15": bb,
                    f"{regla}_lim": lim, f"{regla}_ask_llegada": al, f"{regla}_asz_llegada": az,
                    f"{regla}_edad_llegada_ms": (te - int(r5[j])) if j >= 0 else "", f"{regla}_acc": round(acc, 4),
                    f"{regla}_precio": pr})
    # maker H23: relleno por operaciones TOMADORAS del 5m (ventas del token s a p o compras del contrario a 1-p)
    fills = []
    for tk_, es_s in ((k5, True), (k5o, False)):
        for rx_, ex_, p_, buy, sz in ts.get(tk_, []) if tk_ else []:
            if (buy == 0.0) if es_s else (buy == 1.0):
                fills.append((int(rx_), round(p_ if es_s else 1 - p_, 4), float(sz)))
    fills.sort()
    mk = R.maker_join(inst, ask5, bid5, bid15, ask15, bsz5, fills, t_fin)
    row.update({"mk_lleno": mk["lleno"], "mk_coste": mk["coste"], "mk_t_rel": mk["t_rel"] if mk["t_rel"] is not None else "",
                "mk_p_rel": mk["p_rel"] if mk["p_rel"] is not None else "", "mk_n_cotiz": mk["n_cotiz"], "mk_n_fill": mk["n_fill"]})
    return row


def procesar_dia(dia, forzar=False, ahora=None):
    SALIDA.mkdir(parents=True, exist_ok=True)
    d = date.fromisoformat(dia)
    t_lo = int(datetime(d.year, d.month, d.day, tzinfo=timezone.utc).timestamp())
    t_hi = t_lo + 86400
    ahora = time.time() if ahora is None else ahora
    completo = ahora >= t_hi + 600
    fo, fm = SALIDA / f"entradas_{dia}.csv.gz", SALIDA / f"entradas_{dia}.meta.json"
    hc = hash_codigo()
    if fo.exists() and fm.exists() and not forzar:
        m0 = json.loads(fm.read_text())
        if m0.get("completo") and m0.get("hash_codigo") == hc:
            print(f"{dia}: ya procesado COMPLETO (hash {hc}); nada que hacer"); return m0
    fich = sorted((f for f in glob.glob(str(DL / "maker_ms_*.csv.gz"))
                   if Path(f).name[9:19] in (dia, (d + timedelta(days=1)).isoformat())), key=lambda f: Path(f).stat().st_mtime)
    cal = collections.Counter()
    t0 = time.time()
    meta, idx, qs, ts = leer(dia, fich, t_lo, t_hi, cal)
    tw = twap_refs([(d - timedelta(days=1)).isoformat(), dia])
    filas, esperados = [], 0
    for C in sorted(idx):
        if C % 900:
            continue
        esperados += 1
        tok = idx[C]
        if not all(x in tok for x in (("5min", "YES"), ("5min", "NO"), ("15min", "YES"), ("15min", "NO"))):
            cal["par_incompleto"] += 1; continue
        r15, r5 = tw.get("BTC", {}).get(C - 900), tw.get("BTC", {}).get(C - 300)
        if r15 is None or r5 is None:
            cal["par_sin_ref"] += 1; continue
        gap = (r5 / r15 - 1) * 1e4
        if abs(gap) < R.GAP_MIN_BPS:
            cal["par_gap<min"] += 1; continue
        lado = "Up" if r15 > r5 else "Down"
        m5id = meta[tok[("5min", "YES")]][1]
        row = evaluar_cierre(C, lado, m5id, tok, qs, ts, cal)
        if row is None:
            continue
        row.update({"dia": dia, "cierre": C, "lado": lado, "m5": m5id, "ref15": r15, "ref5": r5, "gap_bps": round(gap, 3)})
        filas.append(row)
    cierres = [r["cierre"] for r in filas]
    assert len(cierres) == len(set(cierres)), "clave cierre duplicada"
    tmp = Path(str(fo) + ".tmp")
    with gzip.open(tmp, "wt", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=CAMPOS, restval="")
        w.writeheader(); w.writerows(filas)
    os.replace(tmp, fo)
    meta_out = {"dia": dia, "completo": bool(completo), "generado_utc": datetime.now(timezone.utc).isoformat(), "hash_codigo": hc,
                "ficheros_ms": [Path(f).name for f in fich], "cierres_esperados": 96, "cierres_en_registro": esperados,
                "cierres_con_fila": len(filas), "ultimo_cierre": max(cierres) if cierres else None, "segundos": round(time.time() - t0, 1),
                "calidad": dict(cal), "regla_version": R.VERSION}
    fm.write_text(json.dumps(meta_out, indent=1))
    with open(SALIDA / f"calidad_{dia}.csv", "w", newline="") as fh:
        w = csv.writer(fh); w.writerow(["dia", "incidencia", "n"])
        for k, v in sorted(cal.items()): w.writerow([dia, k, v])
    print(f"{dia}: cierres {len(filas)}/{esperados} (esperados 96) completo={completo} h55 {sum(1 for r in filas if r.get('h55_t') not in (None, ''))} "
          f"h53 {sum(1 for r in filas if r.get('h53_t') not in (None, ''))} v4 {sum(1 for r in filas if r.get('v4_t') not in (None, ''))} calidad {dict(cal)}")
    return meta_out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--dia", required=True)
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()
    procesar_dia(a.dia, a.forzar)
