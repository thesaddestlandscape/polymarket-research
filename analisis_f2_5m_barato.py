#!/usr/bin/env python3
"""analisis_f2_5m_barato.py — concilia el F2 en vivo (f2_5m_barato_dryrun.py, DRY-RUN) con los vigías offline del mismo día.
Solo lectura. Responde: (1) ¿detecta el camino caliente las MISMAS señales que la regla congelada sobre el registro ms?
(2) ¿con qué diferencia de hora? (3) ¿coincide el relleno simulado a +L (libro L2 propio) con el del vigía? (4) latencias
internas del camino caliente (evento -> decisión, tomar firma) y llegada real de ref5 frente al +1,5 s supuesto.
Fuentes: datalogs/f2_5m_barato/f2_D.jsonl; v4 = datalogs/vigia_5m_barato/eventos_D.csv (B1_5m, es_primero=1);
V7 = datalogs/m5barato_mision/disparo15m_D.csv.gz (las genera el cron 04:35 / 05:50 del día siguiente).
Uso: python3 analisis_f2_5m_barato.py --dia 2026-10-16 [--desde HH:MM] (por defecto cubre solo los cierres que F2 vio).
"""
import argparse
import csv
import gzip
import json
import statistics as st
from collections import Counter, defaultdict
from pathlib import Path

DL = Path("/root/polymarket-research-datalogs")


def pct(xs, q):
    xs = sorted(xs)
    return None if not xs else xs[min(len(xs) - 1, int(q * len(xs)))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dia", required=True)
    a = ap.parse_args()
    evs = [json.loads(ln) for ln in open(DL / "f2_5m_barato" / f"f2_{a.dia}.jsonl")]
    vistos = {(e["moneda"], e["cierre"]) for e in evs if e["tipo"] == "par_fin"}
    refs = [e for e in evs if e["tipo"] == "par_refs"]
    print(f"F2 {a.dia}: pares cerrados {len(vistos)}, con ref {len(refs)}, errores de par "
          f"{sum(e['tipo'] in ('par_error', 'par_sin_mercado', 'par_sin_ref') for e in evs)}")
    r = [e["ref5_retraso_ms"] for e in refs if e.get("ref5_retraso_ms") is not None]
    if r:
        print(f"  ref5 leída tras C-300: p50 {pct(r, .5)} ms, p90 {pct(r, .9)}, máx {max(r)} "
              f"(la regla offline la supone conocida a +1500; >1500 en {sum(x > 1500 for x in r)}/{len(r)})")
    mot = Counter()
    for e in evs:
        if e["tipo"] == "par_fin":
            mot.update(e.get("motivos", {}))
            if e.get("errores_ws"):
                mot["pares_con_errores_ws"] += 1
    print(f"  motivos/incidencias: {dict(mot)}")

    # ── v4 ──
    f2 = {(e["moneda"], e["cierre"]): e for e in evs if e["tipo"] == "v4_evento" and e["es_primero"]}
    rel = defaultdict(dict)
    for e in evs:
        if e["tipo"] == "v4_relleno" and e["n"] == 1:
            rel[(e["moneda"], e["cierre"])][e["L"]] = e
    off = {}
    p = DL / "vigia_5m_barato" / f"eventos_{a.dia}.csv"
    if p.exists():
        for x in csv.DictReader(open(p)):
            if x["regla"] == "B1_5m" and x["es_primero"] == "1":
                k = (x["moneda"], int(x["cierre"]))
                if k in vistos:
                    off[k] = x
    else:
        print(f"  ⚠️ falta {p} (el vigía v4 lo genera a las 04:35 del día siguiente)")
    ambos, solo_f2, solo_off = f2.keys() & off.keys(), f2.keys() - off.keys(), off.keys() - f2.keys()
    print(f"\nv4 primeros eventos (en cierres vistos por F2): F2 {len(f2)} | offline {len(off)} | ambos {len(ambos)} | "
          f"solo F2 {len(solo_f2)} | solo offline {len(solo_off)}")
    dt = [f2[k]["t_deteccion"] - int(off[k]["t_deteccion"]) for k in ambos]
    if dt:
        print(f"  t_deteccion F2 − offline: p50 {pct(dt, .5)} ms, p10 {pct(dt, .1)}, p90 {pct(dt, .9)}")
    acu = Counter()
    for k in ambos:
        o = off[k].get("L215_clase", "")
        l = rel[k].get(215, {}).get("clase")
        acu[(("llena" if o.startswith(("A_", "D_")) else "no"), ("llena" if l in ("llena", "parcial") else "no"))] += 1
    if acu:
        print(f"  relleno L215 (offline, F2): {dict(acu)}")
    for k in sorted(solo_f2 | solo_off):
        e = f2.get(k) or {}
        print(f"   {'solo F2' if k in solo_f2 else 'solo offline'} {k}: margen {e.get('margen_neto') or off[k]['margen_neto']}")
    lat = [e["ms_evento_a_decision"] for e in evs if e["tipo"] == "v4_evento" and "ms_evento_a_decision" in e]
    if lat:
        print(f"  camino caliente evento->decisión: p50 {pct(lat, .5)} ms p99 {pct(lat, .99)} máx {max(lat)}; "
              f"prefirmada disponible {sum(e['prefirmada'] for e in evs if e['tipo'] == 'v4_evento' and e['moneda'] == 'BTC')}"
              f"/{sum(1 for e in evs if e['tipo'] == 'v4_evento' and e['moneda'] == 'BTC')} (BTC)")

    led = []
    for f in sorted((DL / "f2_5m_barato").glob("f2_ledger_*.jsonl")):
        for ln in open(f):
            e = json.loads(ln)
            if e.get("fase") == "respuesta" and e.get("t_evento_ms") and \
                    str(e.get("cierre")) and (e.get("moneda"), e.get("cierre")) in vistos:
                led.append(e)
    for mo in sorted({e["moneda"] for e in led}):
        x = [e["ms_decision_a_envio"] for e in led if e["moneda"] == mo]
        print(f"  {mo} decisión->envío (cola del pool, dry-run): n {len(x)} p50 {pct(x, .5)} p90 {pct(x, .9)} máx {max(x)} ms;"
              f" prefirmada {sum(e.get('prefirmada', False) for e in led if e['moneda'] == mo)}/{len(x)}")

    # ── V7 ──
    f7 = {(e["mercado_5m"], e["delta"], e["L"]): e for e in evs if e["tipo"] == "v7_casa"}
    o7 = {}
    p7 = DL / "m5barato_mision" / f"disparo15m_{a.dia}.csv.gz"
    if p7.exists():
        for x in csv.DictReader(gzip.open(p7, "rt")):
            if (x["moneda"], int(x["cierre"])) in vistos:
                o7[(x["mercado"], float(x["delta"]), int(x["L"]))] = x
    else:
        print(f"  ⚠️ falta {p7}")
    a7 = f7.keys() & o7.keys()
    print(f"\nV7 casadas virtuales: F2 {len(f7)} | offline {len(o7)} | ambos {len(a7)} | solo F2 {len(f7.keys() - o7.keys())}"
          f" | solo offline {len(o7.keys() - f7.keys())}")
    d7 = [f7[k]["t"] - int(o7[k]["t"]) for k in a7]
    if d7:
        print(f"  t disparo F2 − offline: p50 {pct(d7, .5)} ms, p10 {pct(d7, .1)}, p90 {pct(d7, .9)}; "
              f"ask igual {sum(abs(f7[k]['ask'] - float(o7[k]['ask'])) < 1e-9 for k in a7)}/{len(a7)}")
    it = [e.get("intentos_previos", 0) for e in f7.values()]
    if it:
        print(f"  FOK que habría enviado antes de casar (por mercado/DELTA/L): p50 {pct(it, .5)}, máx {max(it)} "
              f"(coste real: límite de órdenes del CLOB)")


if __name__ == "__main__":
    main()
