#!/usr/bin/env python3
"""vigia_wallet_mirror_seleccion_ab.py -- ¿con qué vara hay que elegir las wallets de Wallet Mirror? (30-Sep, Javi)

Hoy Wallet Mirror valida cada wallet con TODO su histórico, al precio que pagó la wallet y sin comisión
(wallet_edge_tracker.py: acierto menos precio medio, n>=30, BH-FDR). Este vigía compara, día a día y SIEMPRE al
ask real que habríamos pagado nosotros (wallet_mirror_executor_dryrun.csv: ask en el instante de decisión, libro
con profundidad >=5x), esa selección contra una alternativa de VENTANA MÓVIL y NETA de comisión:

  A  = todas las señales de wallets validadas por histórico (lo que hoy se detecta y copia).
  B  = solo las claves wallet x moneda x marco que, en los 7 días ANTERIORES al día medido, dieron EV neto > 0
       copiándolas a NUESTRO ask, con n >= 15, datos en >= 3 días y >= 60 % de esos días en positivo.
  noB = el resto de A (validadas por histórico que no pasan la ventana móvil).

La selección de cada día usa solo días anteriores (walk-forward); los criterios de B quedaron FIJADOS el 30-Sep
antes de mirar ningún resultado y no se retocan. Comisión: 7 % x (1 - precio) por euro, gane o pierda.
Limitación: solo entran wallets que el método histórico ya valida (son las únicas que el dry-run registra); las
que ganan ahora y no están validadas se miden aparte en la familia TOMADORA (seleccion_tomadores_persistentes.py).
Hueco de datos 08-22 Sep (el dry-run no registró); los días sin 3 días previos con datos no se miden.

Solo observación: no cambia qué wallets opera nadie. Salida: data/shadow/wallet_mirror_seleccion_ab.json.
Cron diario 07:44 con --telegram.  Veredicto a favor de B = >=10 días medidos, EV(B) - EV(noB) con IC90 por días >0
y EV(B) >= +0,10 con IC90 >0.
"""
import csv
import json
import os
import random
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
SRC = REPO / "data" / "shadow" / "wallet_mirror_executor_dryrun.csv"
OUT = REPO / "data" / "shadow" / "wallet_mirror_seleccion_ab.json"
FEE = 0.07
VENTANA, N_MIN, DIAS_MIN, FRAC_DIAS_POS = 7, 15, 3, 0.60        # FIJADOS 30-Sep, no tocar
GATE_DIAS, GATE_EV = 10, 0.10


def _cargar() -> dict:
    """dia -> [(clave, marco, pnl)] con señales ejecutables y resueltas."""
    por_dia = defaultdict(list)
    with open(SRC, encoding="utf-8", errors="replace", newline="") as f:
        for r in csv.DictReader(f):
            if r.get("acierto") not in ("0", "1") or r.get("sigue_fillable_en_decision") != "1":
                continue
            try:
                a, ratio = float(r["ask_decision"]), float(r["ratio_decision"] or 0)
            except (ValueError, TypeError):
                continue
            if ratio < 5 or not 0.05 <= a < 0.95:
                continue
            pnl = int(r["acierto"]) / a - 1 - FEE * (1 - a)
            por_dia[r["timestamp_utc"][:10]].append(((r["wallet"], r["activo"], r["marco"]), r["marco"], pnl))
    return por_dia


def _ic90(por_dia: dict):
    ks = [k for k in por_dia if por_dia[k]]
    if len(ks) < 3:
        return None
    rng, ms = random.Random(7), []
    for _ in range(1000):
        s = [x for k in (rng.choice(ks) for _ in ks) for x in por_dia[k]]
        ms.append(sum(s) / len(s))
    ms.sort()
    return [round(ms[50], 4), round(ms[950], 4)]


def _ic90_dif(b: dict, nob: dict):
    ks = [k for k in b if b[k] and nob.get(k)]
    if len(ks) < 3:
        return None
    rng, ms = random.Random(9), []
    for _ in range(1000):
        sel = [rng.choice(ks) for _ in ks]
        xb = [x for k in sel for x in b[k]]
        xn = [x for k in sel for x in nob[k]]
        ms.append(sum(xb) / len(xb) - sum(xn) / len(xn))
    ms.sort()
    return [round(ms[50], 4), round(ms[950], 4)]


def _res(por_dia: dict) -> dict:
    x = [v for d in por_dia.values() for v in d]
    if not x:
        return {"n": 0}
    return {"n": len(x), "dias": sum(1 for d in por_dia.values() if d), "ev": round(sum(x) / len(x), 4), "ic90": _ic90(por_dia),
            "dias_positivos": sum(1 for d in por_dia.values() if d and sum(d) > 0)}


def main() -> int:
    por_dia = _cargar()
    hoy = datetime.now(timezone.utc).date().isoformat()
    dias = sorted(d for d in por_dia if d < hoy)                 # solo días cerrados
    grupos = {g: {m: defaultdict(list) for m in ("todos", "5min", "15min", "60min")} for g in ("A", "B", "noB")}
    detalle, n_claves_b = [], {}
    for d in dias:
        d0 = date.fromisoformat(d)
        prev = [(d0 - timedelta(days=k)).isoformat() for k in range(1, VENTANA + 1)]
        prev = [p for p in prev if p in por_dia]
        if len(prev) < DIAS_MIN:
            continue
        acc = defaultdict(lambda: defaultdict(list))
        for p in prev:
            for clave, _, pnl in por_dia[p]:
                acc[clave][p].append(pnl)
        sel = set()
        for clave, pd in acc.items():
            x = [v for dd in pd.values() for v in dd]
            if len(x) >= N_MIN and len(pd) >= DIAS_MIN and sum(x) > 0 and \
                    sum(1 for dd in pd.values() if sum(dd) > 0) >= FRAC_DIAS_POS * len(pd):
                sel.add(clave)
        n_claves_b[d] = len(sel)
        fila = {"dia": d, "claves_B": len(sel)}
        for clave, marco, pnl in por_dia[d]:
            g = "B" if clave in sel else "noB"
            for gg in ("A", g):
                grupos[gg]["todos"][d].append(pnl)
                if marco in grupos[gg]:
                    grupos[gg][marco][d].append(pnl)
        for g in ("A", "B", "noB"):
            x = grupos[g]["todos"].get(d, [])
            fila[g] = {"n": len(x), "ev": round(sum(x) / len(x), 4) if x else None}
        detalle.append(fila)
    res = {g: {m: _res(pd) for m, pd in gm.items()} for g, gm in grupos.items()}
    dif = _ic90_dif(grupos["B"]["todos"], grupos["noB"]["todos"])
    # tramo reciente (desde la reanudación del 23-Sep): lo que cuenta hacia adelante
    rec = {g: _res({d: v for d, v in grupos[g]["todos"].items() if d >= "2026-09-23"}) for g in grupos}
    b = res["B"]["todos"]
    veredicto = ("B CONFIRMADA" if b.get("n") and b["dias"] >= GATE_DIAS and b["ev"] >= GATE_EV and b["ic90"] and b["ic90"][0] > 0
                 and dif and dif[0] > 0 else
                 "B mejor que noB pero sin edge suficiente" if dif and dif[0] > 0 else "sin diferencia demostrada")
    salida = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
              "criterio_B": f"ventana {VENTANA} d, n>={N_MIN}, >={DIAS_MIN} días con datos, >={FRAC_DIAS_POS:.0%} días +, EV neto>0 (fijado 30-Sep)",
              "dias_medidos": len(detalle), "resumen": res, "desde_23sep": rec, "ic90_diferencia_B_menos_noB": dif,
              "veredicto": veredicto, "por_dia": detalle}
    tmp = OUT.with_name(OUT.name + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps(salida, indent=1, ensure_ascii=False), encoding="utf-8")
    tmp.replace(OUT)

    def _l(nombre, r):
        return (f"{nombre}: n={r['n']} días={r['dias']} EV {r['ev']:+.4f} por € IC90 {r['ic90']} ({r['dias_positivos']}/{r['dias']} días +)"
                if r.get("n") else f"{nombre}: sin datos")
    lineas = [f"🪞 Wallet Mirror, ¿con qué vara elegir wallets? ({len(detalle)} días medidos, al ask real, neto de comisión)",
              _l("A  todas las validadas por histórico", res["A"]["todos"]),
              _l("B  ventana móvil 7 d neta >0", b),
              _l("noB el resto", res["noB"]["todos"]),
              f"Diferencia B − noB, IC90 por días: {dif}",
              "Desde el 23-Sep → " + " | ".join(f"{g}: n={r.get('n', 0)} EV {r.get('ev', 0):+.4f}" for g, r in rec.items() if r.get("n")),
              "Por marco (B): " + " | ".join(f"{m} n={r['n']} EV {r['ev']:+.3f}" for m, r in res["B"].items() if m != "todos" and r.get("n")),
              f"Veredicto: {veredicto}. Solo observación; cambiar la selección real = checklist + /code-review + OK de Javi."]
    if detalle:
        u = detalle[-1]
        lineas.insert(5, f"Último día {u['dia']}: claves en B {u['claves_B']} | A {u['A']['ev']} (n={u['A']['n']}) | B {u['B']['ev']} (n={u['B']['n']}) | noB {u['noB']['ev']} (n={u['noB']['n']})")
    print("\n".join(lineas))
    if "--telegram" in sys.argv:
        try:
            from shadow_digest import enviar_telegram
            enviar_telegram("\n".join(lineas), bot="cripto")
        except Exception as e:
            print(f"(telegram falló: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
