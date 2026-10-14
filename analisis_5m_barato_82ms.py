#!/usr/bin/env python3
"""analisis_5m_barato_82ms.py -- MISIÓN «misterio de los 82 ms» (Javi 14-Oct). SOLO LECTURA.

Pista: el ask barato del 5m lo compra un tomador ~82 ms (hora del exchange) después de que la q que lo publica tenga
su hora del exchange, cuando un tomador tiene un retraso propio de ~145-150 ms (medido 07-Oct con órdenes reales:
GTC post-only 68 ms vs FOK no marketable 213 ms). Esta herramienta:
 A. CRONOLOGÍA por evento de señal v4 (eventos B1_5m del vigía, re-armes incluidos): hora exchange y recepción de la q
    barata (t_q_ex, t_q_rx), primera COMPRA tomadora del token a <= ese ask (t_tr_ex, t_tr_rx), dt en reloj del
    exchange (t_tr_ex - t_q_ex) y en reloj de RECEPCIÓN (t_tr_rx - t_q_rx, mismo reloj local: inmune al sello de lote),
    transacción y bloque on-chain del tomador (fila taker==exchange, token, precio <= ask + 1c, bloque en [t_tr_ex/1000-1,
    +6] s, la más cercana) y su wallet.
 B. PLACEBO / CONTROL: TODAS las bajadas del mejor ask (nuevo precio < anterior) de los 5m que cierran con un 15m, en sus
    últimos 300 s, ambos lados. SOLO el lado s implicado por las referencias TWAP60 (como v4, |gap| >= 1 bp). Para cada una: ¿hay compra tomadora a <= ese ask con dt_ex en [0, 150] ms? ("rápida": una
    orden que ya estaba en vuelo), margen respecto al 15m del mismo lado (bid15 - ask - fee) en ese instante, Binance
    orientado al lado en [-500, 0] y [-2000, 0] ms (recepción) y si el bid15 cambió en los 500 ms previos.
    H1 (flujo genérico) predice P(rápida) igual con y sin margen; H2/H3 predicen P(rápida) mayor con margen >= 0,05 y
    un precursor (Binance / 15m) más frecuente en las rápidas.
Uso: nice -n 19 ionice -c3 python3 analisis_5m_barato_82ms.py --desde 2026-10-05 --hasta 2026-10-13
Salida: datalogs/m5barato_mision/82ms_cronologia.csv, 82ms_bajadas_D.csv.gz, 82ms_informe.txt
"""
import argparse
from array import array
import bisect
import csv
import glob
import gzip
import statistics as st
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from archivo_volumen import VOL  # noqa: E402

OUT = Path("/root/polymarket-research-datalogs/m5barato_mision")
EV4 = Path("/root/polymarket-research-datalogs/vigia_5m_barato")
EXCH = "0xe111180000d2663c0091e4f400237545b87b996b"
RAPIDA_MS = 150


def fee(p):
    return 0.07 * p * (1 - p)


class Cols:
    """Filas de n campos en columnas array (memoria compacta); Q[i] devuelve la tupla. None se guarda como NaN."""
    def __init__(self, tipos):
        self.c = [array(tp) for tp in tipos]

    def append(self, fila):
        for col, v in zip(self.c, fila):
            col.append(float("nan") if v is None else v)

    def __len__(self):
        return len(self.c[0])

    def __getitem__(self, i):
        return tuple(None if (isinstance(v, float) and v != v) else v for v in (col[i] for col in self.c))

    def ordenar(self):
        import numpy as np
        o = np.argsort(np.frombuffer(self.c[0], dtype=np.int64), kind="stable")
        self.c = [array(col.typecode, [col[int(i)] for i in o]) for col in self.c]


def cargar(dia):
    meta = {}
    q = defaultdict(lambda: Cols("qqddd"))
    t = defaultdict(lambda: Cols("qqdqd"))      # (t_ex, t_rx, precio, BUY=1/SELL=0, tamaño)
    bn = defaultdict(lambda: Cols("qd"))
    for pref in ("m15", "m5"):
        f = VOL / f"{pref}_registro" / f"{pref}_registro_{dia}.csv.gz"
        if not f.exists():
            return None
        with gzip.open(f, "rt", errors="replace") as fh:
            try:
                for ln in fh:
                    tp = ln[:2]
                    if tp == "k,":
                        c = ln.rstrip("\n").split(",")
                        if len(c) >= 8 and c[4] in ("5min", "15min"):
                            meta[c[2]] = (c[3], c[4], c[5], int(datetime.fromisoformat(c[6]).timestamp()), c[7])
                        continue
                    if tp == "x,":
                        if pref == "m5":
                            c = ln.split(",")
                            try:
                                tr = int(c[7])
                                if (tr // 1000) % 900 < 588 and (tr // 1000) % 900 != 0:
                                    continue
                                bn[c[2][:-4]].append((tr, float(c[3])))
                            except (ValueError, IndexError):
                                pass
                        continue
                    if tp not in ("q,", "t,"):
                        continue
                    c = ln.rstrip("\n").split(",")
                    m = meta.get(c[2])
                    if not m or m[3] % 900:
                        continue
                    try:
                        if tp == "q,":
                            tr = int(c[7])
                            if (m[3] - 305) * 1000 <= tr <= m[3] * 1000:
                                q[c[2]].append((tr, int(c[1]), None if c[3] in ("", "None") else float(c[3]),
                                                None if c[4] in ("", "None") else float(c[4]), float(c[6] or 0)))
                        elif m[1] == "5min":
                            te = int(c[1])
                            if (m[3] - 305) * 1000 <= te <= m[3] * 1000 + 2000:
                                t[c[2]].append((te, int(c[6]), float(c[3]), 1 if c[4] == "BUY" else 0, float(c[5])))
                    except (ValueError, IndexError):
                        continue
            except (EOFError, OSError):
                pass
    for d in (q, t, bn):
        for k in d:
            d[k].ordenar()
    return meta, q, t, bn


def onchain(dia, peticiones):
    """peticiones: (clave, token, precio, t_tr_ex_s) -> clave -> (wallet, tx, bloque_ts, precio, acc)."""
    f = VOL / "m5_onchain" / f"m5_onchain_{dia}.csv.gz"
    if not f.exists() or not peticiones:
        return {}
    por = defaultdict(list)
    for p in peticiones:
        por[p[1]].append(p)
    mejor = {}
    with gzip.open(f, "rt", errors="replace") as fh:
        r = csv.reader(fh)
        ix = {k: i for i, k in enumerate(next(r))}
        for row in r:
            tok = row[ix["token_id"]]
            if tok not in por or row[ix["tipo"]] != "F" or row[ix["taker"]] != EXCH or row[ix["side"]] != "0":
                continue
            try:
                ts = float(row[ix["ts_est"]])
                usdc, acc = float(row[ix["maker_amt"]]), float(row[ix["taker_amt"]])
                pr = usdc / acc
            except (ValueError, ZeroDivisionError):
                continue
            for k, _, p, tex in por[tok]:
                if pr <= p + 0.0101 and tex - 1.0 <= ts <= tex + 6.0:
                    d = abs(ts - tex - 1.5)
                    if k not in mejor or d < mejor[k][0]:
                        mejor[k] = (d, row[ix["maker"]].lower(), row[ix["tx"]], ts, round(pr, 4), round(acc, 3))
    return {k: v[1:] for k, v in mejor.items()}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-05")
    ap.add_argument("--hasta", default="2026-10-13")
    ap.add_argument("--rehacer", action="store_true", help="recalcula el placebo aunque exista el fichero del día")
    a = ap.parse_args()
    E = []
    for f in sorted(EV4.glob("eventos_*.csv")):
        E += [e for e in csv.DictReader(open(f)) if e["regla"] == "B1_5m"]
    crono = []
    d, d1 = date.fromisoformat(a.desde), date.fromisoformat(a.hasta)
    while d <= d1:
        dia = d.isoformat()
        d += timedelta(days=1)
        r = cargar(dia)
        if r is None:
            continue
        meta, q, t, bn = r
        import vigia_5m_barato_forward as V4
        tw = V4.twap_refs([(date.fromisoformat(dia) - timedelta(days=1)).isoformat(), dia])
        def lado_s(mo, cie):
            r15, r5 = tw.get(mo, {}).get(cie - 900), tw.get(mo, {}).get(cie - 300)
            if r15 is None or r5 is None or abs((r5 / r15 - 1) * 1e4) < 1.0:
                return None
            return "YES" if r15 > r5 else "NO"
        # índices: (activo, cierre, marco, lado) -> token
        tok = {(m[0], m[3], m[1], m[4]): k for k, m in meta.items()}
        qts = {k: v.c[0] for k, v in q.items()}
        bts = {k: v.c[0] for k, v in bn.items()}
        def bid15_en(mo, cie, lado, tt):
            k = tok.get((mo, cie, "15min", lado))
            Q = q.get(k, [])
            i = bisect.bisect_right(qts[k], tt) - 1 if Q else -1
            return (Q[i][2], Q, i) if i >= 0 else (None, Q, -1)
        def binance(mo, lado, tt, w):
            B = bn.get(mo, [])
            if not B:
                return None
            ts = bts[mo]
            i, j = bisect.bisect_right(ts, tt) - 1, bisect.bisect_right(ts, tt - w) - 1
            if i < 0 or j < 0:
                return None
            return round((B[i][1] / B[j][1] - 1) * 1e4 * (1 if lado == "YES" else -1), 3)
        # ---------- B: todas las bajadas del ask ----------
        if (OUT / f"82ms_bajadas_{dia}.csv.gz").exists() and not a.rehacer:
            filas_b = None                            # placebo del día ya calculado
        else:
            filas_b = []
        for k, Q in (q.items() if filas_b is not None else []):
            m = meta[k]
            if m[1] != "5min" or lado_s(m[0], m[3]) != m[4]:
                continue                                  # solo el lado s implicado por las referencias (como v4)
            T = t.get(k, [])
            Tex = T.c[0] if len(T) else []
            prev = None
            for (rx, ex, b, ask, asz) in Q:
                if ask is None:
                    prev = None
                    continue
                if prev is not None and ask < prev - 1e-9 and (m[3] - 300) * 1000 <= rx:
                    j = bisect.bisect_right(Tex, ex)
                    dt = None
                    while j < len(T) and T[j][0] <= ex + 1000:
                        if T[j][3] == 1 and T[j][2] <= ask + 1e-9:
                            dt = T[j][0] - ex
                            break
                        j += 1
                    b15, Q15, i15 = bid15_en(m[0], m[3], m[4], rx)
                    mg = None if b15 is None else round(b15 - ask - fee(ask), 4)
                    cambio15 = None
                    if i15 >= 0:
                        jj = i15
                        while jj > 0 and Q15[jj - 1][2] == Q15[i15][2]:
                            jj -= 1
                        cambio15 = rx - Q15[jj][0] <= 500
                    filas_b.append({"dia": dia, "moneda": m[0], "lado": m[4], "t_q_rx": rx, "t_q_ex": ex, "ask": ask,
                                    "ask_sz": asz, "dt_compra_ex": dt, "rapida": dt is not None and dt <= RAPIDA_MS,
                                    "margen15": mg, "bid15_cambio_500ms": cambio15, "bin500": binance(m[0], m[4], rx, 500),
                                    "bin2000": binance(m[0], m[4], rx, 2000), "resto_s": round(m[3] - rx / 1000, 1)})
                prev = ask
        if filas_b is not None:
          with gzip.open(OUT / f"82ms_bajadas_{dia}.csv.gz", "wt") as fh:
            if filas_b:
                w = csv.DictWriter(fh, fieldnames=list(filas_b[0]))
                w.writeheader()
                w.writerows(filas_b)
        # ---------- A: cronología de los eventos de señal ----------
        pet = []
        for e in E:
            if datetime.fromtimestamp(int(e["t_deteccion"]) / 1000, timezone.utc).date().isoformat() != dia:
                continue
            lado = "YES" if e["lado"] == "Up" else "NO"
            k = tok.get((e["moneda"], int(e["cierre"]), "5min", lado))
            Q, T = q.get(k, []), t.get(k, [])
            t0 = int(e["t_deteccion"])
            i = bisect.bisect_right(qts.get(k, []), t0) - 1
            fila = {"event_id": e["event_id"], "dia": dia, "moneda": e["moneda"], "lado": e["lado"], "mercado5": e["market_compra"],
                    "mercado15": e["market_otro"], "t0_rx": t0, "ask0": e["ask_compra_t0"], "bid15_0": e["bid_otro_t0"],
                    "p_limite": e["p_limite"], "clase_L215": e["L215_clase"]}
            if i < 0:
                fila["motivo"] = "sin q del 5m en el registro"
                crono.append(fila)
                continue
            q0 = Q[i]
            # primera aparición del precio barato: retroceder mientras el ask siga igual
            ii = i
            while ii > 0 and Q[ii - 1][3] == q0[3]:
                ii -= 1
            fila.update({"t_q_rx": Q[ii][0], "t_q_ex": Q[ii][1], "feed_ms": Q[ii][0] - Q[ii][1], "ask_nivel": q0[3], "ask_sz": q0[4],
                         "q_creo_senal_rx": q0[0], "q_creo_senal_ex": q0[1]})
            p = float(e["p_limite"])
            cons = next((x for x in T if x[0] > Q[ii][1] and x[3] == 1 and x[2] <= p + 1e-9), None)
            if cons:
                fila.update({"t_tr_ex": cons[0], "t_tr_rx": cons[1], "precio_tr": cons[2], "acc_tr": cons[4],
                             "dt_ex_ms": cons[0] - Q[ii][1], "dt_rx_ms": cons[1] - Q[ii][0], "dt_vs_deteccion_rx_ms": cons[1] - t0})
                pet.append((len(crono), k, cons[2], cons[0] / 1000))
            else:
                fila["motivo"] = "sin compra tomadora <= p_limite en el registro"
            crono.append(fila)
        for kk, (w, tx, ts, pr, acc) in onchain(dia, pet).items():
            crono[kk].update({"tomador": w, "tx": tx, "bloque_ts": ts, "precio_onchain": pr, "acc_onchain": acc,
                              "bloque_menos_tr_ex_ms": round(ts * 1000 - crono[kk]["t_tr_ex"])})
        print(f"{dia}: bajadas de ask {len(filas_b) if filas_b is not None else 'caché'}, eventos de señal "
              f"{sum(1 for c in crono if c['dia'] == dia)}", flush=True)
    campos = list(dict.fromkeys(k for f in crono for k in f))
    with open(OUT / "82ms_cronologia.csv", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos)
        w.writeheader()
        w.writerows(crono)
    # ---------- informe ----------
    L = ["MISTERIO DE LOS 82 ms"]
    C = [c for c in crono if c.get("dt_ex_ms") is not None]
    def q_(v, p):
        v = sorted(v)
        return v[min(len(v) - 1, int(p * len(v)))] if v else None
    for k in ("feed_ms", "dt_ex_ms", "dt_rx_ms", "bloque_menos_tr_ex_ms"):
        v = [float(c[k]) for c in C if c.get(k) is not None]
        L.append(f"  {k:24s} n={len(v):3d} P10/P25/P50/P75/P90 {[q_(v, p) for p in (.1, .25, .5, .75, .9)]}")
    v = [float(c["dt_ex_ms"]) for c in C]
    L.append(f"  eventos de señal con compra: {len(C)}/{len(crono)}; dt_ex <= 150 ms: {sum(1 for x in v if x <= 150)}; "
             f"dt_rx <= 150 ms: {sum(1 for c in C if float(c['dt_rx_ms']) <= 150)}; con wallet on-chain: {sum(1 for c in C if c.get('tomador'))}")
    # placebo agregado en streaming desde los ficheros diarios (sin cargar 1 M+ filas en memoria)
    grupos = {"margen15 < 0": lambda mg, ch: mg is not None and mg < 0,
              "margen15 [0, 0,05)": lambda mg, ch: mg is not None and 0 <= mg < 0.05,
              "margen15 >= 0,05 (señal)": lambda mg, ch: mg is not None and mg >= 0.05,
              "  señal y bid15 cambió en 500 ms": lambda mg, ch: mg is not None and mg >= 0.05 and ch,
              "  señal y bid15 quieto": lambda mg, ch: mg is not None and mg >= 0.05 and not ch,
              "sin margen calculable": lambda mg, ch: mg is None}
    acc = {g: [0, 0, 0, 0, 0] for g in grupos}           # n, rápidas, bin500 válidos, bin500>=0,5, bid15 cambió
    por_dia = defaultdict(lambda: [0, 0, 0, 0])          # señal: n, rápidas | sin margen<0: n, rápidas
    for f in sorted(OUT.glob("82ms_bajadas_*.csv.gz")):
        dd = f.name[13:23]
        if not (a.desde <= dd <= a.hasta):
            continue
        with gzip.open(f, "rt") as fh:
            for r in csv.DictReader(fh):
                mg = float(r["margen15"]) if r["margen15"] not in ("", "None") else None
                ch = r["bid15_cambio_500ms"] == "True"
                rp = r["rapida"] == "True"
                b5 = float(r["bin500"]) if r["bin500"] not in ("", "None") else None
                for g, cond in grupos.items():
                    if cond(mg, ch):
                        x = acc[g]
                        x[0] += 1
                        x[1] += rp
                        if b5 is not None:
                            x[2] += 1
                            x[3] += b5 >= 0.5
                        x[4] += ch
                if mg is not None and mg >= 0.05:
                    por_dia[dd][0] += 1
                    por_dia[dd][1] += rp
                elif mg is not None and mg < 0:
                    por_dia[dd][2] += 1
                    por_dia[dd][3] += rp
    tot = sum(acc[g][0] for g in ("margen15 < 0", "margen15 [0, 0,05)", "margen15 >= 0,05 (señal)", "sin margen calculable"))
    L.append(f"\nPLACEBO: {tot} bajadas del mejor ask (5m pares, lado s, últimos 300 s). P(compra tomadora <= ask en <= {RAPIDA_MS} ms):")
    for g, x in acc.items():
        if x[0]:
            L.append(f"  {g:38s} n={x[0]:7d} rápidas {x[1]:6d} = {x[1] / x[0]:6.2%} | Binance 500 ms a favor >=0,5 bp "
                     f"{x[3] / max(1, x[2]):.1%} | bid15 cambió 500 ms {x[4] / x[0]:.1%}")
    L.append("  por día (señal: rápidas/n | margen<0: rápidas/n): " + " ".join(
        f"{d[5:]} {v[1]}/{v[0]} | {v[3]}/{v[2]};" for d, v in sorted(por_dia.items())))
    txt = "\n".join(L)
    print(txt)
    (OUT / "82ms_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
