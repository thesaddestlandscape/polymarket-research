#!/usr/bin/env python3
"""vigia_5m_barato_v3_forward.py -- HIPÓTESIS 5M_CHEAP_V3_H3A (filtro de deterioro por Binance), CONGELADA el
2026-10-12T18:00:00Z (misión «5m barato», pasos 5.1/6 del prompt de Javi). SOLO OBSERVACIÓN, lee los eventos del vigía
congelado v4 (mismas señales y misma ejecución L215) y aplica UN filtro decidido en la muestra de DESCUBRIMIENTO 06-11 Oct:

  H3a: no se compra si el retorno de Binance en los 5 s previos a la señal (columna bin_ret_5s_bps del vigía, orientado
       al lado s: Up +, Down -) es < -1 bps (Binance moviéndose en CONTRA del lado comprado) o no hay dato (fail-closed).
  Mecanismo (autopsia 12-Oct): las perdedoras llegan con Binance en contra (mediana -2,2 bps vs 0), mucha actividad en
  Binance (32 vs 3 operaciones/s), el 5m de s cayendo y la cota del 15m RANCIA (bid de 147 ms vs 0): el 5m no está
  barato, el 15m está desfasado. Descubrimiento (NO evidencia): v4 L215 40 %→67 % acierto, EV +0,41→+1,23 (n 10→6);
  V2 L215 75 %→90 %, EV +1,28→+1,70, IC90 cierre (+0,55, +2,62) (n 24→20). Umbral elegido tras ver las medianas.

Dos variantes evaluadas por separado (registro de versiones independiente):
  V3a = v4 (primera señal por cierre-moneda) + H3a.   V3b = V2 (todas, tope 3 ejecuciones y 6 € por mercado) + H3a.
Gates como v4/V2. Unidad = cierre. Uso: python3 vigia_5m_barato_v3_forward.py [--telegram] [--desde ISO (diagnóstico)]
"""
import argparse
import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))
import vigia_5m_barato_forward as V  # noqa: E402
from vigia_5m_barato_v2_forward import evaluar, resumen  # noqa: E402

CONFIG_V3 = {"nombre": "5M_CHEAP_V3_H3A", "congelado_utc": "2026-10-12T18:00:00+00:00", "filtro": "bin_ret_5s_bps_orientado >= -1",
             "variantes": {"V3a": {"base": "v4 primera señal", "max_por_mercado": 1, "max_riesgo": 1e9},
                           "V3b": {"base": "V2 todas", "max_por_mercado": 3, "max_riesgo": 6.0}},
             "gates": {"n_mercados": 40, "dias": 10, "ev_min": 0.10}}
HASH = hashlib.sha256(json.dumps(CONFIG_V3, sort_keys=True).encode()).hexdigest()[:16]
OUT = V.SALIDA / "v3_informe.json"


def pasa_h3a(e):
    try:
        v = float(e["bin_ret_5s_bps"])
    except (TypeError, ValueError, KeyError):
        return False                                   # sin dato -> no se compra (fail-closed)
    if v != v:
        return False
    return (v if e["lado"] == "Up" else -v) >= -1.0


def gates(r):
    g = CONFIG_V3["gates"]
    return {"n_mercados>=40": r.get("n_mercados", 0) >= g["n_mercados"], "dias>=10": r.get("dias", 0) >= g["dias"],
            "EV>=0,10": (r.get("ev") or -9) >= g["ev_min"], "IC90_dia>0": bool(r.get("ic90_dia")) and r["ic90_dia"][0] > 0,
            "sin_mejor_dia>0": (r.get("ev_sin_mejor_dia") or -9) > 0, "sin_mejor_op>0": (r.get("ev_sin_mejor_op") or -9) > 0,
            "sin_BTC>0": (r.get("ev_sin_btc") or -9) > 0}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--telegram", action="store_true")
    ap.add_argument("--desde", default=None)
    a = ap.parse_args()
    from analisis_maker_cancelacion_binance import desenlaces
    desde = a.desde or CONFIG_V3["congelado_utc"]
    cong = int(datetime.fromisoformat(desde).timestamp() * 1000)
    E = []
    for f in sorted(V.SALIDA.glob("eventos_*.csv")):
        E += [e for e in csv.DictReader(open(f)) if e["regla"] == "B1_5m" and int(e["t_deteccion"]) >= cong]
    des = desenlaces({e["market_compra"] for e in E}) if E else {}
    rep = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "config": CONFIG_V3, "hash": HASH, "desde": desde}
    lineas = [f"🧪 5M_CHEAP_V3_H3A (filtro Binance 5 s ≥ −1 bps; congelada {CONFIG_V3['congelado_utc'][:16]}Z, hash {HASH}; desde {desde[:16]}Z)"]
    for nombre, cfg in CONFIG_V3["variantes"].items():
        base = [e for e in E if cfg["max_por_mercado"] > 1 or e["es_primero"] == "1"]
        r = resumen(evaluar([e for e in base if pasa_h3a(e)], des, cfg["max_por_mercado"], cfg["max_riesgo"]))
        r0 = resumen(evaluar(base, des, cfg["max_por_mercado"], cfg["max_riesgo"]))
        g = gates(r)
        est = "OOS_VALIDATED" if all(g.values()) else ("FORWARD_PENDING" if r.get("n_mercados", 0) < 40 else "TESTING")
        rep[nombre] = {"con_filtro": r, "sin_filtro_mismo_periodo": r0, "gates": g, "estado": est}
        lineas.append(f"{nombre} ({cfg['base']} + H3a): mercados {r.get('n_mercados', 0)}, {r.get('dias', 0)} días, PnL {r.get('pnl_eur', 0):+.2f}€, "
                      f"EV {r.get('ev')}, IC90 día {r.get('ic90_dia')}, sin mejor día {r.get('ev_sin_mejor_dia')}, sin BTC {r.get('ev_sin_btc')} "
                      f"| sin filtro: {r0.get('n_mercados', 0)} merc. EV {r0.get('ev')} | {est}")
    lineas.append("Nada a dinero sin gates + /code-review + OK Javi.")
    if not a.desde:
        OUT.write_text(json.dumps(rep, indent=1, ensure_ascii=False), encoding="utf-8")
    msg = "\n".join(lineas)
    print(msg)
    if a.telegram and not a.desde:
        from shadow_digest import enviar_telegram
        enviar_telegram(msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
