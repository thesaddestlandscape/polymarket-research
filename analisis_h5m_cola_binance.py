#!/usr/bin/env python3
"""analisis_h5m_cola_binance.py -- H5M v2 (Javi 14-Oct, opción 1): ¿se salva la política SEGUIR de
analisis_h5m_cola_simulada.py (maker en el mejor bid de la banda 0,10-0,30 a T 60-300 s, 5m, al final de la cola:
−0,050 €/€ IC90 (−0,082,−0,020) en 09-13 Oct) si se APARTA cuando Binance se mueve en contra?
Diagnóstico del v1: las órdenes llenas del todo (barridos que atraviesan el nivel) pierden; las parciales ganan.

REGLA FIJADA ANTES DE MIRAR (14-Oct ~06:50Z):
  - Binance = aggTrade de la moneda en el registro ms (fila x), reloj de RECEPCIÓN (c[7]; trampa: E mezcla relojes).
  - movimiento = (p_ahora − p_hace W) / p_hace W en bps, W = 1000 ms (primer aggTrade de la ventana).
  - En contra = baja si compramos YES (Up), sube si compramos NO (Down).
  - Si movimiento en contra >= U bps: cancelar la cotización (efectiva a recepción + LAT_CANCEL_MS, nos pueden llenar
    mientras tanto) y no recotizar durante BLOQ_MS = 2000 ms.
  - U en {1, 2, 3} bps -> SEGUIR_BN1/2/3 (3 celdas; la PRINCIPAL es U = 2). Todo lo demás idéntico a SEGUIR.
Prueba justa (trampa 07-Oct del simulador con "cancelar si X salta"): se informa la FRECUENCIA de la señal, P(relleno)
frente a SEGUIR, y en los rellenos de SEGUIR el EV de los que tuvieron señal en contra en el segundo previo frente a
los que no (si no discrimina ahí, una mejora de la política sería solo operar menos).
Uso: nice -n 19 ionice -c3 python3 analisis_h5m_cola_binance.py --desde 2026-10-09 --hasta 2026-10-13 [--max-lineas N]
Salida: datalogs/h5m_cola_sim/v2_unidades_D.csv.gz + v2_informe.txt
"""
import argparse
import bisect
import csv
import gzip
import sys
from array import array
from collections import deque
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_h5m_cola_simulada import (LAT_CANCEL_MS, OUT, P_HI, P_LO, SH, T_MAX, T_MIN, Orden,  # noqa: E402
                                        ic_dias)
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402
from archivo_volumen import VOL  # noqa: E402

W_MS = 1000
BLOQ_MS = 2000
UMBRALES = {"SEGUIR": None, "SEGUIR_BN1": 1.0, "SEGUIR_BN2": 2.0, "SEGUIR_BN3": 3.0}
PRINCIPAL = "SEGUIR_BN2"


class OrdenT(Orden):
    __slots__ = ("t_rel",)

    def __init__(self, pol, tok, t_fin):
        super().__init__(pol, tok, t_fin)
        self.t_rel = None

    def consumir(self, t_ex, pe, sz):
        antes = self.lleno
        super().consumir(t_ex, pe, sz)
        if self.t_rel is None and self.lleno > antes + 1e-9:
            self.t_rel = t_ex


def simular_dia(d, max_lineas=None):
    f = VOL / "m5_registro" / f"m5_registro_{d}.csv.gz"
    if not f.exists():
        return None, None
    meta, por_mkt, ordenes, bloq = {}, {}, {}, {}
    vivas = {}                                 # moneda -> set((pol, tok)) con política BN y cotización viva
    bn = {}                                    # moneda -> deque[(t_rx, p)] últimos W_MS
    hist = {}                                  # moneda -> (array t_rx, array p) del día (diagnóstico)
    n_senal = {p: 0 for p in UMBRALES if UMBRALES[p]}
    n = 0
    with gzip.open(f, "rt", errors="replace") as fh:
        try:
            for ln in fh:
                n += 1
                if max_lineas and n > max_lineas:
                    break
                tp = ln[:2]
                if tp == "ti":
                    continue
                c = ln.rstrip("\n").split(",")
                if tp == "x,":
                    try:
                        mon, p, t_rx = c[2][:-4], float(c[3]), int(c[7])
                    except (ValueError, IndexError):
                        continue
                    h = hist.setdefault(mon, (array("q"), array("d")))
                    h[0].append(t_rx)
                    h[1].append(p)
                    dq = bn.setdefault(mon, deque())
                    if dq and t_rx < dq[-1][0] - W_MS:
                        dq.clear()                              # salto atrás en el tiempo (cambio de fichero)
                    dq.append((t_rx, p))
                    while dq and dq[0][0] < t_rx - W_MS:
                        dq.popleft()
                    mov = (p - dq[0][1]) / dq[0][1] * 1e4
                    if abs(mov) < 1.0:
                        continue
                    for clave in list(vivas.get(mon, ())):
                        pol, tk = clave
                        o = ordenes.get(clave)
                        if o is None or not o.viva:
                            vivas[mon].discard(clave)
                            continue
                        contra = -mov if meta[tk][3] == "YES" else mov
                        if contra >= UMBRALES[pol]:
                            o.cancelar(t_rx)
                            bloq[clave] = t_rx + BLOQ_MS
                            vivas[mon].discard(clave)
                            n_senal[pol] += 1
                    continue
                if tp == "k,":
                    if len(c) >= 8 and c[4] == "5min":
                        fin = int(datetime.fromisoformat(c[6]).timestamp() * 1000)
                        meta[c[2]] = (c[3], c[5], fin, c[7])
                        por_mkt.setdefault(c[5], {})[c[7]] = c[2]
                    continue
                tk = c[2]
                m = meta.get(tk)
                if m is None:
                    continue
                if tp == "q,":
                    try:
                        bid, ask, bsz = float(c[3]), float(c[4]), float(c[5])
                        t_rx = int(c[7])
                    except (ValueError, IndexError):
                        continue
                    T = (m[2] - t_rx) / 1000.0
                    if not (T_MIN < T <= T_MAX):
                        continue
                    b = round(bid, 2)
                    ok = P_LO < b <= P_HI and b < ask - 1e-9
                    for pol, u in UMBRALES.items():
                        clave = (pol, tk)
                        o = ordenes.get(clave)
                        if o is not None and o.lleno >= SH - 1e-9:
                            continue
                        if o is not None and o.viva:
                            if ok and abs(o.segs[-1][0] - b) < 1e-9:
                                continue
                            o.cancelar(t_rx)
                        if ok and t_rx >= bloq.get(clave, 0):
                            if o is None:
                                o = ordenes[clave] = OrdenT(pol, tk, m[2] - T_MIN * 1000)
                            o.cotizar(b, bsz, t_rx)
                            if u:
                                vivas.setdefault(m[0], set()).add(clave)
                elif tp == "t,":
                    try:
                        p, side, sz = float(c[3]), c[4], float(c[5])
                        t_ex = int(c[1])
                    except (ValueError, IndexError):
                        continue
                    if side == "SELL":
                        objetivo, pe = tk, p
                    elif side == "BUY":
                        objetivo, pe = por_mkt.get(m[1], {}).get("NO" if m[3] == "YES" else "YES"), round(1.0 - p, 4)
                        if objetivo is None:
                            continue
                    else:
                        continue
                    for pol in UMBRALES:
                        o = ordenes.get((pol, objetivo))
                        if o is not None:
                            o.consumir(t_ex, pe, sz)
        except (EOFError, OSError) as e:
            print(f"  {d}: fichero truncado ({type(e).__name__}) tras {n} líneas", file=sys.stderr)

    # los ficheros del día (uno por PID de observadores) no van necesariamente en orden de tiempo: ordenar el histórico
    for mon, (tt, pp) in list(hist.items()):
        ta, pa = np.frombuffer(tt, dtype=np.int64), np.frombuffer(pp, dtype=np.float64)
        o_ = np.argsort(ta, kind="stable")
        hist[mon] = (ta[o_].tolist(), pa[o_])

    def contra_previo(mon, lado, t):
        """Máximo movimiento en contra (bps) entre p(t - W) y cualquier p en [t - W, t] (reloj de recepción)."""
        h = hist.get(mon)
        if h is None:
            return float("nan")
        i0, i1 = bisect.bisect_left(h[0], t - W_MS), bisect.bisect_right(h[0], t)
        if i1 - i0 < 1:
            return 0.0
        p0 = float(h[1][max(0, i0 - 1)])
        tramo = h[1][i0:i1]
        if lado == "YES":
            return (p0 - float(tramo.min())) / p0 * 1e4
        return (float(tramo.max()) - p0) / p0 * 1e4

    des = desenlaces({meta[o.tok][1] for o in ordenes.values()})
    filas = []
    for o in ordenes.values():
        act, mkt, fin, lado = meta[o.tok]
        r = des.get(mkt)
        ll, co = o.lleno, o.coste
        filas.append({"dia": d, "pol": o.pol, "mkt": mkt, "act": act, "lado": lado,
                      "precio": round(co / ll if ll > 0 else o.segs[0][0], 4), "n_cotiz": len(o.segs),
                      "lleno": round(ll, 4), "des": r or "", "coste": round(co, 6),
                      "pnl": round((ll if r == lado else 0.0) - co, 6) if r else "",
                      "contra_prev_bps": round(contra_previo(act, lado, o.t_rel), 3) if o.t_rel else ""})
    return filas, n_senal


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--desde", default="2026-10-09")
    ap.add_argument("--hasta")
    ap.add_argument("--max-lineas", type=int, default=None)
    a = ap.parse_args()
    OUT.mkdir(exist_ok=True)
    d0 = date.fromisoformat(a.desde)
    d1 = date.fromisoformat(a.hasta) if a.hasta else datetime.now(timezone.utc).date() - timedelta(days=1)
    filas, senales = [], {}
    d = d0
    while d <= d1:
        ds = d.isoformat()
        cache = OUT / f"v2_unidades_{ds}.csv.gz"
        if cache.exists() and not a.max_lineas:
            with gzip.open(cache, "rt") as fh:
                filas += list(csv.DictReader(fh))
        else:
            fs, ns = simular_dia(ds, a.max_lineas)
            if fs is not None:
                cob = np.mean([bool(x["des"]) for x in fs]) if fs else 0.0
                print(f"{ds}: {len(fs)} órdenes, cobertura {cob:.1%}, cancelaciones por señal {ns}", flush=True)
                senales[ds] = ns
                if not a.max_lineas and cob >= 0.99:
                    with gzip.open(cache, "wt") as fh:
                        w = csv.DictWriter(fh, fieldnames=list(fs[0].keys()))
                        w.writeheader()
                        w.writerows(fs)
                filas += fs
        d += timedelta(days=1)
    lin = [f"H5M v2 cola + apartarse por Binance (W={W_MS} ms, bloqueo {BLOQ_MS} ms, cancel +{LAT_CANCEL_MS} ms, "
           f"principal {PRINCIPAL}, sin reembolso)"]
    base_llenas = None
    for pol in UMBRALES:
        F = [x for x in filas if x["pol"] == pol and x["des"]]
        R = [x for x in F if float(x["lleno"]) > 0]
        dias = sorted({x["dia"] for x in F})
        ev_d = []
        for ds in dias:
            Rd = [float(x["pnl"]) / float(x["coste"]) for x in R if x["dia"] == ds]
            ev_d.append(np.mean(Rd) if Rd else float("nan"))
        evs = [float(x["pnl"]) / float(x["coste"]) for x in R]
        lo, hi = ic_dias([e for e in ev_d if e == e])
        sinbtc = [float(x["pnl"]) / float(x["coste"]) for x in R if x["act"] != "BTC"]
        pnl = sum(float(x["pnl"]) for x in R)
        if pol == "SEGUIR":
            base_llenas = len(R)
        lin.append(f"\n{pol}{' (PRINCIPAL)' if pol == PRINCIPAL else ''}: órdenes {len(F)} | rellenas {len(R)} "
                   f"({len(R) / max(1, len(F)):.0%}; vs SEGUIR {len(R) / max(1, base_llenas):.0%}) | EV/€ {np.mean(evs):+.4f} "
                   f"IC90 días ({lo:+.4f},{hi:+.4f}) | sin BTC {np.mean(sinbtc):+.4f} | PnL {pnl:+.2f} $ | días + "
                   f"{sum(e > 0 for e in ev_d)}/{len(ev_d)}")
        lin.append("    por día: " + " ".join(f"{ds[5:]} {e:+.3f}" for ds, e in zip(dias, ev_d)))
        if pol == "SEGUIR":
            for u in (1.0, 2.0, 3.0):
                con = [float(x["pnl"]) / float(x["coste"]) for x in R if x["contra_prev_bps"] != ""
                       and float(x["contra_prev_bps"]) >= u]
                sin = [float(x["pnl"]) / float(x["coste"]) for x in R if x["contra_prev_bps"] != ""
                       and float(x["contra_prev_bps"]) < u]
                lin.append(f"    prueba justa U={u:g}: rellenos con señal en contra en el 1 s previo n={len(con)} "
                           f"({len(con) / max(1, len(R)):.0%}) EV {np.mean(con) if con else float('nan'):+.4f} | sin señal "
                           f"n={len(sin)} EV {np.mean(sin) if sin else float('nan'):+.4f}")
    if senales:
        lin.append(f"\ncancelaciones por señal por día: {senales}")
    txt = "\n".join(lin)
    print(txt)
    if not a.max_lineas:
        (OUT / "v2_informe.txt").write_text(txt + "\n")


if __name__ == "__main__":
    main()
