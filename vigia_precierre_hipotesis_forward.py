#!/usr/bin/env python3
"""vigia_precierre_hipotesis_forward.py -- seguimiento FORWARD de las hipótesis congeladas el 30-Sep sobre el
observador multi-instante (precierre_multioffset_fase0.csv). Aviso diario por Telegram (cron 07:28).

Salieron de mirar ~200 celdas con 6 días (25-30 Sep): por eso NO valen por lo visto antes del corte; solo cuenta lo
que ocurra después de CORTE, con las reglas tal como quedaron escritas aquí (no se retocan).
Todas: ask REAL con profundidad >= 5x de 1,05 €, comisión real 7 % x (1 - precio), desenlace oficial, una entrada
por mercado (el primer instante que cumple).

  H1 SOLITARIO 5m  : 5 min, T-120..T-45, z en [1, 1,8) y NINGUNA otra moneda con z>=1 en el mismo lado en ese
                     instante -> comprar el lado CONTRARIO a su ask real (columna ask_contrario; ask 0,03-0,60).
                     Antes del corte, con el ask contrario ESTIMADO (1 - bid): +0,147, n=429.
  H2 Z3 5m         : 5 min, T-120..T-45, z >= 3 y ask del lado TWAP en [0,30, 0,80) -> comprar el lado TWAP.
                     Antes: +0,142 (n=61).
  H3 Z CRECE 15m   : 15 min, a T-60, z >= 1, ask [0,65, 0,95) y z mayor que en T-90 (mismo lado). Antes: +0,074 (n=80).
  H4 TWAP 15m      : 15 min, T-90..T-45, z >= 1, ask [0,65, 0,95). Antes: +0,038 (n=607, 6/6 días).
  H5 TWAP 15m noche: H4 solo entre las 18 y las 24 UTC. Antes: +0,078 (n=146).
  H6 TWAP 4h       : 4 h, T-600..T-45, z >= 1, ask [0,65, 0,95). Sin datos previos (mercado añadido el 30-Sep).

Confirmada = n>=40, >=10 días, IC90 por días > 0. Para dinero real además EV >= +0,10 por € (regla del proyecto),
checklist de 6 categorías, /code-review y OK de Javi. Salida: data/shadow/precierre_hipotesis_forward.json.
"""
import collections
import csv
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import analisis_precierre_rejilla_ask_real as A  # noqa: E402

CORTE = "2026-09-30T13:30"
OUT = REPO / "data" / "shadow" / "precierre_hipotesis_forward.json"
FEE = 0.07


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main() -> int:
    filas = []
    with open(A.SRC, encoding="utf-8", errors="replace", newline="") as f:
        for r in csv.DictReader(f):
            z = _f(r.get("z"))
            if z is None or not r.get("direccion"):
                continue
            filas.append(dict(m=r["marco"], off=int(float(r["offset_s"])), ts=r["ts_utc"], dia=r["ts_utc"][:10], slug=r["slug"],
                              z=abs(z), dir=r["direccion"], a=_f(r.get("ask")), rt=_f(r.get("ratio_vs_stake")) or 0.0,
                              ac=_f(r.get("ask_contrario")), rc=_f(r.get("ratio_contrario")) or 0.0,
                              hora=int(r["ts_utc"][11:13]), fin=r["slug"].rsplit("-", 1)[-1]))
    gan = A.desenlaces(x["slug"] for x in filas)
    inst = collections.defaultdict(list)                 # (marco, offset, fin de ventana) -> filas de todas las monedas
    por_mk = collections.defaultdict(dict)
    for x in filas:
        inst[(x["m"], x["off"], x["fin"])].append(x)
        por_mk[x["slug"]][x["off"]] = x
    for x in filas:
        x["acuerdo"] = sum(1 for y in inst[(x["m"], x["off"], x["fin"])] if y is not x and y["dir"] == x["dir"] and y["z"] >= 1)

    def ok_twap(x, lo, hi):
        return x["a"] is not None and lo <= x["a"] < hi and x["rt"] >= 5

    def h3(x):
        p = por_mk[x["slug"]].get(-90)
        return x["z"] >= 1 and ok_twap(x, 0.65, 0.95) and p is not None and p["dir"] == x["dir"] and x["z"] > p["z"]
    H = [
        ("H1 SOLITARIO 5m (contrario)", "5m", (-120, -90, -60, -45), True,
         lambda x: 1 <= x["z"] < 1.8 and x["acuerdo"] == 0 and x["ac"] is not None and 0.03 <= x["ac"] < 0.60 and x["rc"] >= 5),
        ("H2 Z3 5m", "5m", (-120, -90, -60, -45), False, lambda x: x["z"] >= 3 and ok_twap(x, 0.30, 0.80)),
        ("H3 Z CRECE 15m", "15m", (-60,), False, h3),
        ("H4 TWAP 15m", "15m", (-90, -60, -45), False, lambda x: x["z"] >= 1 and ok_twap(x, 0.65, 0.95)),
        ("H5 TWAP 15m 18-24 UTC", "15m", (-90, -60, -45), False, lambda x: x["z"] >= 1 and ok_twap(x, 0.65, 0.95) and x["hora"] >= 18),
        ("H6 TWAP 4h", "4h", (-600, -300, -180, -120, -90, -60, -45), False, lambda x: x["z"] >= 1 and ok_twap(x, 0.65, 0.95)),
    ]
    res, lineas = {}, [f"🧊 Hipótesis congeladas del precierre (corte {CORTE}Z; solo cuenta el forward)"]
    for nombre, marco, offs, contrario, regla in H:
        bloque = {}
        for etiqueta, dentro in (("antes", lambda x: x["ts"] < CORTE), ("forward", lambda x: x["ts"] >= CORTE)):
            vistos, pd = set(), collections.defaultdict(list)
            for x in sorted(filas, key=lambda y: y["off"]):
                if x["m"] != marco or x["off"] not in offs or x["slug"] in vistos or x["slug"] not in gan or not dentro(x):
                    continue
                if not regla(x):
                    continue
                vistos.add(x["slug"])
                acierta_twap = gan[x["slug"]] == x["dir"]
                precio, gana = (x["ac"], not acierta_twap) if contrario else (x["a"], acierta_twap)
                pd[x["dia"]].append((1 if gana else 0) / precio - 1 - FEE * (1 - precio))
            v = [y for d in pd.values() for y in d]
            ic = A.ic90(pd)
            bloque[etiqueta] = {"n": len(v), "dias": len(pd), "ev": round(sum(v) / len(v), 4) if v else None,
                                "ic90": [round(ic[0], 4), round(ic[1], 4)] if ic else None,
                                "dias_positivos": sum(1 for d in pd.values() if sum(d) > 0)}
        fw = bloque["forward"]
        conf = bool(fw["n"] >= 40 and fw["dias"] >= 10 and fw["ic90"] and fw["ic90"][0] > 0)
        bloque["confirmada"] = conf
        bloque["ev_minimo_dinero_real"] = bool(conf and fw["ev"] >= 0.10)
        res[nombre] = bloque
        if fw["n"]:
            txt = f"n={fw['n']} días={fw['dias']} EV {fw['ev']:+.3f}" + (f" IC90 {fw['ic90']}" if fw["ic90"] else "") + f" ({fw['dias_positivos']}/{fw['dias']} días +)"
        else:
            txt = "sin casos todavía"
        lineas.append(f"{'✅' if conf else '·'} {nombre}: {txt}" + (" — CONFIRMADA" + ("" if bloque["ev_minimo_dinero_real"] else " (EV < +0,10: no llega al mínimo para dinero real)") if conf else ""))
    lineas.append("Confirmada = n≥40, ≥10 días, IC90>0. Nada opera sin checklist + /code-review + OK de Javi.")
    tmp = OUT.with_name(OUT.name + f".tmp{os.getpid()}")
    tmp.write_text(json.dumps({"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "corte": CORTE,
                               "hipotesis": res}, indent=1, ensure_ascii=False), encoding="utf-8")
    tmp.replace(OUT)
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
