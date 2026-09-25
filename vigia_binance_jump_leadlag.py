#!/usr/bin/env python3
"""vigia_binance_jump_leadlag.py -- resumen DIARIO por Telegram del observador A3b (Binance manda).
25-Sep, Javi: "mándame datos diarios por Telegram, léelos cada día en el protocolo y vamos decidiendo".
Cron 07:55 UTC. Solo lectura del CSV de datalogs + cache de outcomes; escribe
data/shadow/vigia_binance_jump_leadlag.json. No decide nada: 'DECIDIR' solo indica que una celda
cruzó n>=40 con >=3 días (mismo listón que el resto del proyecto); la promoción exige checklist + OK Javi.
"""
import json
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import analisis_binance_jump_leadlag as A

OUT = REPO / "data" / "shadow" / "vigia_binance_jump_leadlag.json"
N_DECISION, DIAS_DECISION = 40, 3


def main() -> int:
    try:
        n_ev, n_res, celdas = A.calcular()
    except OSError:
        print("sin CSV del observador todavía")
        return 0
    ahora = datetime.now(timezone.utc)
    lim = (ahora - timedelta(hours=24)).isoformat()
    import csv
    ev24, coin24, latencias = set(), Counter(), []
    porev = {}                                    # (ts,activo,marco,mid) -> {offset: (ask, bid)}
    for r in csv.DictReader(open(A.CSV, encoding="utf-8")):
        if not r["error"]:
            try:
                porev.setdefault((r["ts_evento"], r["activo"], r["marco"], r["market_id"]), {})[float(r["offset_s"])] = (
                    float(r["ask"]), float(r["bid"]))
            except (TypeError, ValueError):
                pass
        if r["ts_evento"] >= lim and not r["error"]:
            k = (r["ts_evento"], r["activo"], r["market_id"])
            if k not in ev24:
                ev24.add(k); coin24[r["activo"]] += 1
            if r["offset_s"] in ("0.0",):
                try:
                    latencias.append(float(r["lat_libro_ms"]))
                except ValueError:
                    pass
    lineas = [f"⚡ A3b Binance manda -- resumen diario ({ahora:%Y-%m-%d})",
              f"eventos 24h (evento×mercado): {len(ev24)} ({', '.join(f'{a}={n}' for a, n in coin24.most_common())}); "
              f"total acumulado {n_ev} ({n_res} con resultado); lat. libro mediana "
              f"{sorted(latencias)[len(latencias)//2] if latencias else '-'} ms"]
    # Medida DIRECTA de si el libro sigue a Binance: cuánto se mueve el ask del token del lado del salto
    # entre la lectura a t0 (~0,06 s tras la detección) y +0,3/+1/+4 s. Si ya subió a +0,3 s, el libro
    # reaccionó antes de que pudiéramos entrar (no hay ventana desde esta máquina).
    repre = {}
    for marco in ("5m", "15m"):
        fila = {}
        for off in (0.3, 1.0, 4.0):
            v = [o[off][0] - o[0.0][0] for k, o in porev.items() if k[2] == marco and 0.0 in o and off in o]
            fila[off] = (round(sum(v) / len(v) * 100, 2), len(v)) if len(v) >= 5 else None
        repre[marco] = fila
        if any(fila.values()):
            lineas.append(f"· reprecio del ask tras el salto ({marco}): " + " | ".join(
                f"+{o}s {x[0]:+.1f}c (n={x[1]})" for o, x in fila.items() if x))
    salida = {"actualizado_utc": ahora.isoformat(timespec="seconds"), "eventos_total": n_ev, "con_resultado": n_res,
              "eventos_24h": len(ev24), "reprecio_ask_c": {m: {str(o): x for o, x in f.items()} for m, f in repre.items()}, "celdas": {"|".join(map(str, k)): v for k, v in celdas.items()}}
    decidir = []
    for marco in ("5m", "15m"):
        for e in A.ENTRADAS:
            c = celdas.get(("TODAS", marco, e))
            if not c:
                continue
            ev = "-" if c["ev"] is None else f"{c['ev']:+.2f}"
            lo = "-" if c["ic90_lo"] is None else f"{c['ic90_lo']:+.2f}"
            lineas.append(f"· TODAS {marco} entrada +{e}s: n={c['n']} descontado {c['descontado_c']:+.1f}c "
                          f"markout {c['markout_c']:+.1f}c | resultado n={c['n_res']} EV/€={ev} IC90días_lo={lo} días={c['dias']}")
            if c["n_res"] >= N_DECISION and c["dias"] >= DIAS_DECISION:
                decidir.append((marco, e, c))
    coins = sorted({k[0] for k in celdas if k[0] != "TODAS"})
    for act in coins:
        c = celdas.get((act, "5m", 0.6))
        if c and c["n"] >= 5:
            ev = "-" if c["ev"] is None else f"{c['ev']:+.2f}"
            lineas.append(f"   {act} 5m +0,6s: n={c['n']} markout {c['markout_c']:+.1f}c EV/€={ev} (n_res={c['n_res']})")
    lineas.append("✅ DECIDIR: " + ", ".join(f"{m} +{e}s EV={c['ev']:+.2f} lo={c['ic90_lo']:+.2f}" for m, e, c in decidir)
                  if decidir else f"acumulando: ninguna celda TODAS con n_res>={N_DECISION} y >={DIAS_DECISION} días")
    OUT.write_text(json.dumps(salida, indent=1, ensure_ascii=False), encoding="utf-8")
    print("\n".join(lineas))
    try:
        from shadow_digest import enviar_telegram
        enviar_telegram("\n".join(lineas))
    except Exception as e:
        print(f"(Telegram falló: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
