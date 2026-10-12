#!/usr/bin/env python3
"""vigia_5m_barato_v2_forward.py -- HIPÓTESIS 5M_CHEAP_V2_ALL_SIGNALS, CONGELADA el 2026-10-12T16:00:00Z (misión «5m barato»,
prompt definitivo de Javi 12-Oct, paso 4). SOLO OBSERVACIÓN: lee los eventos que ya escribe cada día el vigía congelado
v4 (vigia_5m_barato_forward.py, eventos_D.csv con TODOS los eventos B1_5m, re-armes incluidos) y evalúa la variante V2.

Origen: descubierta el 12-Oct al revisar el OOS de v4 (06-11 Oct): contando los re-armes, 51 señales / 24 ejecutables /
75 % de acierto. Esa muestra es de DESCUBRIMIENTO: aquí solo cuentan señales con t_deteccion >= CONGELADO.

REGLA V2 (congelada; cambiarla = V3 + nuevo periodo):
  - Señal = cualquier evento B1_5m de v4 (misma regla de señal: margen_neto >= 0,05, ventanas, re-armado tras 2 s sin
    señal, libro cruzado descartado), no solo el primero de cada (cierre, moneda).
  - Ejecución = la de v4 a L = 215 ms (precio y acciones de la columna L215 del evento; UNKNOWN no cuenta).
  - Exposición: como mucho MAX_EVENTOS_POR_MERCADO (3) ejecuciones por mercado 5m (se toman en orden temporal; el resto
    no se ejecuta) y riesgo por mercado <= MAX_RIESGO_MERCADO_EUR (6 €, = 3 x stake 2 €).
  - Unidad de independencia = CIERRE (todas las monedas y eventos de un mismo cierre comparten régimen): IC por cierre y
    por día; PnL por mercado = suma de sus ejecuciones.
Gates (mismo listón que v4): n_mercados_ejecutados >= 40, >= 10 días, EV €/€ >= 0,10, IC90 por día > 0, positivo sin el
mejor día, sin la mejor operación y sin BTC. Comparación obligatoria contra v4 (primera señal) en el MISMO periodo.
Uso: python3 vigia_5m_barato_v2_forward.py [--telegram]   (cron diario después del informe de v4)
"""
import argparse
import collections
import csv
import hashlib
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import vigia_5m_barato_forward as V  # noqa: E402  (solo lectura: pnl_de, SALIDA)

CONFIG_V2 = {"nombre": "5M_CHEAP_V2_ALL_SIGNALS", "congelado_utc": "2026-10-12T16:00:00+00:00", "latencia": "L215",
             "max_eventos_por_mercado": 3, "max_riesgo_mercado_eur": 6.0, "base": "vigia_5m_barato_forward v4",
             "gates": {"n_mercados": 40, "dias": 10, "ev_min": 0.10}}
HASH = hashlib.sha256(json.dumps(CONFIG_V2, sort_keys=True).encode()).hexdigest()[:16]
OUT = V.SALIDA / "v2_informe.json"


def _ic90(grupos, n=4000):
    g = [v for v in grupos.values() if v]
    if len(g) < 3:
        return None
    rng, med = random.Random(11), []
    for _ in range(n):
        s = [x for _ in g for x in rng.choice(g)]
        med.append(sum(s) / len(s))
    med.sort()
    return [round(med[int(0.05 * n)], 3), round(med[int(0.95 * n)], 3)]


def evaluar(evs, des, max_por_mercado, max_riesgo):
    """Aplica el tope por mercado en orden temporal. Devuelve lista de mercados ejecutados con su PnL y riesgo."""
    por_mercado = collections.defaultdict(list)
    for e in sorted(evs, key=lambda e: int(e["t_deteccion"])):
        por_mercado[e["market_compra"]].append(e)
    merc = []
    for mid, lst in por_mercado.items():
        pnl = rie = 0.0
        k = 0
        for e in lst:
            r = V.pnl_de(e, des, "L215")
            if r is None or r[1] <= 0:
                continue
            if k >= max_por_mercado or rie + r[1] > max_riesgo + 1e-9:
                break
            pnl, rie, k = pnl + r[0], rie + r[1], k + 1
        if k:
            e0 = lst[0]
            merc.append({"market": mid, "moneda": e0["moneda"], "cierre": e0["cierre"], "ejecuciones": k, "pnl": pnl,
                         "riesgo": rie, "dia": datetime.fromtimestamp(int(e0["t_deteccion"]) / 1000, timezone.utc).date().isoformat()})
    return merc


def resumen(merc):
    if not merc:
        return {"n_mercados": 0}
    pnl, rie = sum(m["pnl"] for m in merc), sum(m["riesgo"] for m in merc)
    por_dia, por_cierre = collections.defaultdict(list), collections.defaultdict(list)
    for m in merc:
        por_dia[m["dia"]].append(m["pnl"] / m["riesgo"])
        por_cierre[m["cierre"]].append(m["pnl"] / m["riesgo"])
    dia_pnl = collections.defaultdict(float)
    for m in merc:
        dia_pnl[m["dia"]] += m["pnl"]
    mejor_dia = max(dia_pnl, key=dia_pnl.get)
    top = max(merc, key=lambda m: m["pnl"])
    sin = lambda f: [m for m in merc if f(m)]  # noqa: E731
    ev = lambda L: round(sum(m["pnl"] for m in L) / sum(m["riesgo"] for m in L), 3) if L else None  # noqa: E731
    return {"n_mercados": len(merc), "ejecuciones": sum(m["ejecuciones"] for m in merc), "dias": len(por_dia),
            "cierres": len(por_cierre), "pnl_eur": round(pnl, 2), "riesgo_eur": round(rie, 2), "ev": round(pnl / rie, 3),
            "acierto_mercado": round(sum(1 for m in merc if m["pnl"] > 0) / len(merc), 3),
            "ic90_dia": _ic90(por_dia), "ic90_cierre": _ic90(por_cierre),
            "ev_sin_mejor_dia": ev(sin(lambda m: m["dia"] != mejor_dia)), "ev_sin_mejor_op": ev(sin(lambda m: m is not top)),
            "ev_sin_btc": ev(sin(lambda m: m["moneda"] != "BTC")),
            "pct_pnl_mejor_dia": round(dia_pnl[mejor_dia] / pnl, 2) if pnl > 0 else None}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--telegram", action="store_true")
    ap.add_argument("--desde", default=None, help="solo diagnóstico: otra fecha de inicio (NO cambia la evaluación oficial)")
    a = ap.parse_args()
    from analisis_maker_cancelacion_binance import desenlaces
    desde = a.desde or CONFIG_V2["congelado_utc"]
    cong = int(datetime.fromisoformat(desde).timestamp() * 1000)
    E = []
    for f in sorted(V.SALIDA.glob("eventos_*.csv")):
        E += [e for e in csv.DictReader(open(f)) if e["regla"] == "B1_5m" and int(e["t_deteccion"]) >= cong]
    des = desenlaces({e["market_compra"] for e in E}) if E else {}
    v2 = resumen(evaluar(E, des, CONFIG_V2["max_eventos_por_mercado"], CONFIG_V2["max_riesgo_mercado_eur"]))
    v1 = resumen(evaluar([e for e in E if e["es_primero"] == "1"], des, 1, 2.0 + 1e9))
    g = CONFIG_V2["gates"]
    gates = {"n_mercados>=40": v2.get("n_mercados", 0) >= g["n_mercados"], "dias>=10": v2.get("dias", 0) >= g["dias"],
             "EV>=0,10": (v2.get("ev") or -9) >= g["ev_min"], "IC90_dia>0": bool(v2.get("ic90_dia")) and v2["ic90_dia"][0] > 0,
             "sin_mejor_dia>0": (v2.get("ev_sin_mejor_dia") or -9) > 0, "sin_mejor_op>0": (v2.get("ev_sin_mejor_op") or -9) > 0,
             "sin_BTC>0": (v2.get("ev_sin_btc") or -9) > 0}
    estado = "OOS_VALIDATED" if all(gates.values()) else ("FORWARD_PENDING" if v2.get("n_mercados", 0) < g["n_mercados"] else "TESTING")
    rep = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "config": CONFIG_V2, "hash": HASH,
           "desde": desde, "v2": v2, "v1_mismo_periodo": v1, "gates": gates, "estado": estado}
    if not a.desde:
        OUT.write_text(json.dumps(rep, indent=1, ensure_ascii=False), encoding="utf-8")
    f = lambda d: (f"mercados {d.get('n_mercados', 0)} (ejec. {d.get('ejecuciones', 0)}), {d.get('dias', 0)} días, "  # noqa: E731
                   f"PnL {d.get('pnl_eur', 0):+.2f}€, EV {d.get('ev')}, IC90 día {d.get('ic90_dia')}, sin mejor día "
                   f"{d.get('ev_sin_mejor_dia')}, sin mejor op {d.get('ev_sin_mejor_op')}, sin BTC {d.get('ev_sin_btc')}")
    msg = (f"🧪 5M_CHEAP_V2_ALL_SIGNALS (congelada {CONFIG_V2['congelado_utc'][:16]}Z, hash {HASH}; forward desde {desde[:16]}Z)\n"
           f"V2: {f(v2)}\nv4 mismo periodo: {f(v1)}\n"
           f"gates: {' '.join(k + ('✅' if v else '❌') for k, v in gates.items())}\nESTADO: {estado}. Nada a dinero sin "
           f"gates + /code-review + OK Javi.")
    print(msg)
    if a.telegram and not a.desde:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
