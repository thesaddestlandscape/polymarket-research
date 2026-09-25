#!/usr/bin/env python3
"""analisis_perps_markout_entradas_25sep.py -- Perps: ¿las wallets rastreadas tienen edge COPIABLE en sus
ENTRADAS? (25-Sep, Javi: "dale a perps aquí"). Solo lectura de data/shadow/perps_fills_full/.

Por qué no usa posiciones (segmentador v2): medido 25-Sep, la cadena previous_size->after se cumple en
el 79 % de los pares de órdenes consecutivas (1,2 % con el signo invertido en maker, 19,7 % rotas): hay
variaciones de posición no explicadas por los fills devueltos (no es paginación: la API completa
coincide con el backfill salvo los fills posteriores al backfill; ni es "polvo" de redondeo). Las
ENTRADAS, en cambio, se identifican solo con datos de la propia orden (prev==0 o mismo signo que el lado)
y no dependen de la cadena.
Evento de entrada = primera orden de entrada de (wallet, instrumento, dirección) tras >=SEP_MIN min sin
entrada de esa clave (una posición grande trozeada = 1 evento). Seguidor: compra al precio de la
primera operación de CUALQUIER wallet en ese instrumento >= LAT_S s después (proxy de ask), marca a
H horas con la primera operación posterior a t+H (tolerancia TOL_MIN). Retorno neto = dir*(P_H/P_0-1)
menos 2*FEE_TAKER (entrada+salida taker). FUNDING NO incluido (no hay fuente pública; limitación).
Walk-forward: selección con eventos previos al corte (n>=N_MIN, retorno neto medio>0, t>=T_MIN), test
posterior; t por clúster (wallet,día); concentración top-1 y retorno sin la mejor wallet.
"""
import bisect
import collections
import csv
import glob
import json
import math
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR = REPO / "data/shadow/perps_fills_full"
STATE = REPO / "data/shadow/perps_fills_full_state.json"
SEP_MIN, LAT_S, TOL_MIN = 30, 60, 15
HORIZONTES_H = [1, 6, 24]
FEE_TAKER = 0.0004
N_MIN, T_MIN = 30, 2.0


def _t(x):
    n = len(x)
    if n < 2:
        return 0.0
    sd = statistics.pstdev(x)
    return (sum(x) / n) / (sd / math.sqrt(n)) if sd > 0 else 0.0


def cargar():
    hf = {a for a, v in json.loads(STATE.read_text()).items() if v.get("alta_frecuencia")}
    ordenes, serie = [], collections.defaultdict(list)
    vistos = set()
    for f in glob.glob(str(DIR / "*.csv")):
        a = Path(f).stem
        if a in hf:
            continue
        por = {}
        for r in csv.DictReader(open(f, encoding="utf-8")):
            if r["trade_id"] in vistos:
                continue
            vistos.add(r["trade_id"])
            ts, p, q = int(r["ts_ms"]), float(r["price"]), float(r["quantity"])
            serie[r["instrument_id"]].append((ts, p))
            k = (r["instrument_id"], r["order_id"])
            o = por.get(k)
            if o is None:
                por[k] = o = {"w": a, "ins": r["instrument_id"], "ts": ts, "side": r["side"], "prev": float(r["previous_size"]),
                              "qty": 0.0, "notion": 0.0, "liq": r["liquidation"] == "True"}
            o["qty"] += q; o["notion"] += p * q; o["ts"] = min(o["ts"], ts)
        for o in por.values():
            o["price"] = o["notion"] / o["qty"] if o["qty"] > 0 else 0.0
            ordenes.append(o)
    for k in serie:
        serie[k].sort()
    return ordenes, serie


def es_entrada(o):
    if o["liq"] or o["price"] <= 0:
        return False
    return o["prev"] == 0 or (o["prev"] > 0) == (o["side"] == "long")


def eventos(ordenes):
    por = collections.defaultdict(list)
    for o in ordenes:
        if es_entrada(o):
            por[(o["w"], o["ins"], o["side"])].append(o)
    ev = []
    for k, L in por.items():
        L.sort(key=lambda o: o["ts"]); ult = -1e18
        for o in L:
            if o["ts"] - ult >= SEP_MIN * 60_000:
                ev.append(o)
            ult = o["ts"]
    return ev


def precio_desde(serie, ins, t_ms, tol_ms):
    s = serie.get(ins)
    if not s:
        return None
    i = bisect.bisect_left(s, (t_ms, -1))
    return s[i][1] if i < len(s) and s[i][0] - t_ms <= tol_ms else None


def markouts(ev, serie):
    out = []
    for o in ev:
        p0 = precio_desde(serie, o["ins"], o["ts"] + LAT_S * 1000, 5 * 60_000)
        if not p0:
            continue
        d = 1 if o["side"] == "long" else -1
        fila = {"w": o["w"], "ins": o["ins"], "ts": o["ts"], "dia": datetime.fromtimestamp(o["ts"] / 1000, timezone.utc).strftime("%Y-%m-%d")}
        for h in HORIZONTES_H:
            ph = precio_desde(serie, o["ins"], o["ts"] + h * 3_600_000, TOL_MIN * 60_000)
            fila[f"r{h}"] = None if not ph else d * (ph / p0 - 1) - 2 * FEE_TAKER
        out.append(fila)
    return out


def resumen(rows, h, etiqueta):
    v = [r[f"r{h}"] for r in rows if r[f"r{h}"] is not None]
    if len(v) < 10:
        print(f"  {etiqueta} H={h}h n={len(v)} (insuficiente)")
        return
    cl = collections.defaultdict(list)
    for r in rows:
        if r[f"r{h}"] is not None:
            cl[(r["w"], r["dia"])].append(r[f"r{h}"])
    mc = [sum(x) / len(x) for x in cl.values()]
    bw = collections.defaultdict(float)
    for r in rows:
        if r[f"r{h}"] is not None:
            bw[r["w"]] += r[f"r{h}"]
    tot = sum(bw.values()); top = max(bw.values()) if bw else 0
    peor = max(bw, key=bw.get) if bw else None
    rest = [r[f"r{h}"] for r in rows if r[f"r{h}"] is not None and r["w"] != peor]
    print(f"  {etiqueta} H={h}h n={len(v)} eventos, {len(cl)} clústeres wallet-día, {len(bw)} wallets | ret neto medio={sum(v)/len(v)*100:+.3f}% "
          f"t_iid={_t(v):+.2f} t_cluster={_t(mc):+.2f} | top1 wallet={top/tot:.0%} sin ella={sum(rest)/max(len(rest),1)*100:+.3f}%" if tot > 0 else
          f"  {etiqueta} H={h}h n={len(v)} ret neto medio={sum(v)/len(v)*100:+.3f}% t_iid={_t(v):+.2f} t_cluster={_t(mc):+.2f}")


def main():
    ordenes, serie = cargar()
    ev = eventos(ordenes)
    rows = markouts(ev, serie)
    t0 = min(r["ts"] for r in rows); t1 = max(r["ts"] for r in rows)
    print(f"órdenes {len(ordenes)} | eventos de entrada independientes {len(ev)} | con precio de seguimiento {len(rows)} | "
          f"{datetime.fromtimestamp(t0/1000, timezone.utc):%Y-%m-%d} -> {datetime.fromtimestamp(t1/1000, timezone.utc):%Y-%m-%d} | wallets {len({r['w'] for r in rows})}")
    print("\nBASE (todas las entradas de todas las wallets, seguidor a +60 s):")
    for h in HORIZONTES_H:
        resumen(rows, h, "TODAS")
    dias = sorted({r["dia"] for r in rows})
    for i_corte in (len(dias) * 5 // 10, len(dias) * 7 // 10):
        corte = dias[i_corte]
        for h in HORIZONTES_H:
            tr = collections.defaultdict(list)
            for r in rows:
                if r["dia"] < corte and r[f"r{h}"] is not None:
                    tr[r["w"]].append(r[f"r{h}"])
            sel = {w for w, v in tr.items() if len(v) >= N_MIN and sum(v) > 0 and _t(v) >= T_MIN}
            print(f"\nWALK-FORWARD H={h}h corte={corte}: wallets con n>={N_MIN} en train: {sum(len(v)>=N_MIN for v in tr.values())}, seleccionadas: {len(sel)}")
            test = [r for r in rows if r["dia"] >= corte and r["w"] in sel]
            resumen(test, h, "test seleccionadas")
            todos = [r for r in rows if r["dia"] >= corte]
            resumen(todos, h, "test TODAS (placebo)")


if __name__ == "__main__":
    sys.exit(main())
