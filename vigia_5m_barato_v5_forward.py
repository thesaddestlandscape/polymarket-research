#!/usr/bin/env python3
"""vigia_5m_barato_v5_forward.py -- HIPÓTESIS 5M_CHEAP_V5_ORIGEN15M, CONGELADA el 2026-10-14T08:45:00Z (misión «origen 15m»,
prompt de Javi 14-Oct). SOLO OBSERVACIÓN / DRY-RUN: nunca firma ni envía nada.

ORIGEN (descubrimiento, NO evidencia): analisis_5m_barato_competencia.py sobre 05-13 Oct (79 eventos B1_5m de v4): cuando la
señal la crea un cambio del bid del 15m (el 15m trae información nueva que el 5m aún no ha absorbido) acierta 39/44 y EV
hipotético al ask de la señal +2,04 por cierre; cuando la crea el 5m (bajó el ask del 5m mientras el bid del 15m estaba quieto
= 15m rancio, el diagnóstico del 12-Oct) 22/33 y las que quedan ejecutables valen poco. Todo 05-13 Oct es DESCUBRIMIENTO.

DEFINICIÓN CONGELADA (sobre columnas que el vigía v4 ya escribe en cada evento, hash 77a75859ae5cf22e, NO modificado):
  origen_15m  <=>  o_edad_bid_ms < c_edad_ask_ms   (en t0 = recepción de la q que creó la señal)
  o_edad_bid_ms = ms desde el último cambio de PRECIO del mejor bid del 15m del lado s; c_edad_ask_ms = ms desde el último
  cambio de (precio, tamaño) del mejor ask del 5m del lado s (definiciones de vigia_5m_barato_forward.rasgos_libro).
  Coincide con la definición simétrica (edades por precio, competencia) en 75/79 eventos de descubrimiento.
VARIANTES (dos, fijadas aquí):
  V5a = primer evento B1_5m de cada (cierre, moneda) de v4 Y origen_15m (subconjunto EMPAREJADO de v4: mismos eventos).
  V5b = primer evento B1_5m con origen_15m de cada (cierre, moneda) (los re-armes cuentan hasta el primero que cumple);
        una ejecución por mercado.
  Universo declarado ANTES del forward: TODAS las monedas y, por decisión de Javi 14-Oct ("si de momento solo podemos operar
  en BTC no hay problema"), también el subuniverso BTC (V5a_BTC, V5b_BTC) evaluado aparte (en él G7 no aplica por diseño).
EJECUCIÓN: la de v4 (libro real del 5m a t0+L, niveles 1-3 hasta p_limite, stake 2 €, comisión 0,07·p·(1-p), desenlace
  oficial). Latencia PRINCIPAL L355 (llegada al casado P50 medida 14-Oct: pre-envío + ~34 ida + 150 taker delay); estrés
  L475 (P90); comparativa L215 (la de v4). Las columnas L355/L475 salen del laboratorio lab_5m_barato_replay.py (misma
  maquinaria de v4 sobre el archivo del registro) en datalogs/m5barato_mision/lab_lat/.
MÉTRICAS Y GATES: idénticos a v4 (vigia_5m_barato_forward.resumen; G1 ejecutables>=40, G2 días>=10, G3 EV/€>=0,10,
  G4 IC90 por días>0, G5 EV sin mejor día>0, G6 PnL sin top 5 %>0, G7 EV sin BTC>0, G8 sin UNKNOWN, G9 latencia real
  (=L355 medida), G10 solo forward >= FORWARD_DESDE). Se añade (documentado, no sustituye): G11 PnL sin las 3 mejores
  operaciones > 0.
REFUTACIÓN: con >= 40 ejecutables forward a L355, EV/€ <= 0 o IC90 por días por debajo de 0 => refutada. ABANDONO: si a
  los 30 días forward hay < 15 ejecutables (no hay capacidad).
Uso: python3 vigia_5m_barato_v5_forward.py [--telegram] [--descubrimiento]   (--descubrimiento: evalúa 05-13 Oct, solo
  diagnóstico, nunca cuenta para gates)
"""
import argparse
import csv
import hashlib
import json
import sys
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import vigia_5m_barato_forward as V  # noqa: E402  (solo lectura: resumen, pnl_de, fee)

LAB = Path("/root/polymarket-research-datalogs/m5barato_mision/lab_lat")
OUT = Path("/root/polymarket-research-datalogs/m5barato_mision/v5_informe.json")
CONFIG_V5 = {"nombre": "5M_CHEAP_V5_ORIGEN15M", "congelado_utc": "2026-10-14T08:45:00+00:00",
             "forward_desde_utc": "2026-10-14T09:00:00+00:00", "base": "vigia_5m_barato_forward v4 77a75859ae5cf22e",
             "origen": "o_edad_bid_ms < c_edad_ask_ms", "latencia_principal": "L355", "estres": "L475", "comparativa": "L215",
             "variantes": ["V5a", "V5b"], "universos": ["TODAS", "BTC"], "gates": "v4 G1-G10 + G11 sin top3"}


def hash_v5():
    h = hashlib.sha256(json.dumps(CONFIG_V5, sort_keys=True).encode())
    h.update(Path(__file__).read_bytes())
    return h.hexdigest()[:16]


def origen_15m(e):
    try:
        return float(e["o_edad_bid_ms"]) < float(e["c_edad_ask_ms"])
    except (TypeError, ValueError, KeyError):
        return False                                 # sin dato -> no (fail-closed)


def seleccionar(E, variante):
    b1 = sorted((e for e in E if e["regla"] == "B1_5m"), key=lambda e: int(e["t_deteccion"]))
    if variante == "V5a":
        return [e for e in b1 if e["es_primero"] == "1" and origen_15m(e)]
    vistos, out = set(), []
    for e in b1:
        k = (e["cierre"], e["moneda"])
        if k not in vistos and origen_15m(e):
            vistos.add(k)
            out.append(e)
    return out


def gates(r, sin_top3, universo):
    ic = (r.get("ic_dias") or {}).get("ic90")
    return {"G1_n>=40": r.get("ejecutables", 0) >= 40, "G2_dias>=10": r.get("dias", 0) >= 10,
            "G3_EV>=0,10": (r.get("ev_por_eur") or -9) >= 0.10, "G4_IC90_diario>0": bool(ic and ic[0] > 0),
            "G5_sin_mejor_dia>0": (r.get("ev_sin_mejor_dia") or -9) > 0, "G6_sin_top5%>0": (r.get("pnl_sin_top5pct") or -9) > 0,
            "G7_sin_BTC>0": "n/a (universo BTC)" if universo == "BTC" else (r.get("ev_sin_btc") or -9) > 0,
            "G8_reconstruccion": r.get("unknown", 1) == 0, "G9_latencia_real": True, "G10_forward": True,
            "G11_sin_top3>0": sin_top3 > 0}


def evaluar(E, des, variante, universo, lat):
    sel = seleccionar(E, variante)
    if universo == "BTC":
        sel = [e for e in sel if e["moneda"] == "BTC"]
    r = V.resumen(sel, des, lat, f"{variante} {universo} {lat}")
    pn = sorted((p[0] for p in (V.pnl_de(e, des, lat) for e in sel) if p and p[1] > 0), reverse=True)
    sin3 = round(sum(pn[3:]), 3) if pn else 0.0
    r["pnl_sin_top3"] = sin3
    return r, gates(r, sin3, universo)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--telegram", action="store_true")
    ap.add_argument("--descubrimiento", action="store_true")
    a = ap.parse_args()
    from analisis_maker_cancelacion_binance import desenlaces
    E = []
    for f in sorted(LAB.glob("eventos_*.csv")):
        E += list(csv.DictReader(open(f)))
    corte = int(datetime.fromisoformat(CONFIG_V5["forward_desde_utc"]).timestamp() * 1000)
    E = [e for e in E if (int(e["t_deteccion"]) < corte) == a.descubrimiento]
    tag = "DESCUBRIMIENTO 05-13 Oct (NO cuenta para gates)" if a.descubrimiento else f"FORWARD desde {CONFIG_V5['forward_desde_utc']}"
    lin = [f"🧪 {CONFIG_V5['nombre']} (hash {hash_v5()}; congelada {CONFIG_V5['congelado_utc']}) — {tag}"]
    res = {"hash": hash_v5(), "config": CONFIG_V5, "modo": tag, "resultados": {}}
    if not E:
        lin.append("sin eventos en el periodo")
    else:
        des = desenlaces({e["market_compra"] for e in E})
        v4p = [e for e in E if e["regla"] == "B1_5m" and e["es_primero"] == "1"]
        for lat in ("L215", "L355", "L475"):
            r = V.resumen(v4p, des, lat, f"v4 {lat}")
            lin.append(f"v4 (referencia emparejada) {lat}: señales {r['senales']} ejec {r['ejecutables']} PnL {r.get('pnl_neto')} "
                       f"EV/€ {r.get('ev_por_eur')} sin BTC {r.get('ev_sin_btc')} sin mejor día {r.get('ev_sin_mejor_dia')}")
            res["resultados"][f"v4_{lat}"] = r
        for var in ("V5a", "V5b"):
            for uni in ("TODAS", "BTC"):
                for lat in ("L215", "L355", "L475"):
                    r, g = evaluar(E, des, var, uni, lat)
                    res["resultados"][f"{var}_{uni}_{lat}"] = {"r": r, "gates": g}
                    lin.append(f"{var} {uni:5s} {lat}: señales {r['senales']} ejec {r['ejecutables']} PnL {r.get('pnl_neto')} "
                               f"EV/€ {r.get('ev_por_eur')} IC90 días {(r.get('ic_dias') or {}).get('ic90')} sin mejor día "
                               f"{r.get('ev_sin_mejor_dia')} sin top3 {r.get('pnl_sin_top3')} acierto {r.get('acierto')}"
                               + (f" | gates {sum(1 for v in g.values() if v is True)}/{len(g)}" if lat == "L355" else ""))
        lin.append("Nada pasa a dinero sin gates + /code-review + OK Javi.")
    txt = "\n".join(lin)
    print(txt)
    if not a.descubrimiento:
        OUT.write_text(json.dumps(res, indent=1, default=str))
        if a.telegram:
            from shadow_digest import enviar_telegram
            enviar_telegram(txt)


if __name__ == "__main__":
    main()
