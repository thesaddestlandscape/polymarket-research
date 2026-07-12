#!/usr/bin/env python3
"""¿Los patrones_ganadores (boosts de Kelly) que hoy están activos para los
pares REALMENTE en vivo (pares_permitidos_live) se sostienen en la ejecución
real, o solo existen en el shadow "de papel"?

Origen (12-Jul, pregunta directa de Javi): tras encontrar que
H-CUSTOM-GBMLATE-PYBAJO-LONGSHOT decía una cosa en shadow (IC-0.155,
"filtrar") y lo contrario en ejecutado real (+0.315€/trade, "no tocar"),
Javi preguntó si esto puede estar pasando en MÁS sitios. Respuesta: sí,
parcialmente — de los 4 patrones_ganadores activos hoy en GBM_LATE_15M
(BUY_YES, agregado+SOL+ETH), 2 de 4 CONTRADICEN la ejecución real:

  sigma_h>0.0152  (shadow IC+0.137) -> real: dentro=+0.040€/trade
                                       fuera=+0.346€/trade  CONTRADICE
  hora_utc<17.0   (shadow IC+0.122) -> real: dentro=+0.187€/trade
                                       fuera=+0.372€/trade  CONTRADICE
  hora_utc>6.0    (shadow IC+0.123) -> real: dentro=+0.291€/trade
                                       fuera=-0.116€/trade  consistente
  dist_vwap_pct<0.1365 -> n real=3 vs 2, insuficiente

Impacto HOY: cero (apuesta_kelly con boost es inerte mientras el stake
siga pineado a 1.05€, live_stake.calcular_stake lo ignora). Impacto SI se
despinea el stake sin este chequeo: sobre-apostar justo en los peores
buckets reales. Este script formaliza la comprobación para que sea
reproducible cada vez que se plantee des-pinear, en vez de un análisis
manual puntual.

Lee pares_permitidos_live dinámicamente (no hardcodea SOL/ETH). Solo
lectura, no toca dinero ni config.
"""
import csv
import glob
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

TRADES = REPO / "data/live/trades.csv"
CONFIG_LIVE = REPO / "data/live/config_live.json"
STRATEGY_PARAMS = REPO / "data/shadow/strategy_params.json"


def _tuplas_live():
    try:
        cfg = json.loads(CONFIG_LIVE.read_text(encoding="utf-8"))
        tuplas = []
        for p in cfg.get("pares_permitidos_live", []):
            partes = p.split("#")
            if len(partes) == 4:
                tuplas.append(tuple(partes))
        return tuplas
    except Exception:
        return []


def _pred_index(strategy):
    idx = {}
    for path in glob.glob(str(REPO / "data/shadow/predictions_*.csv")):
        try:
            with open(path, encoding="utf-8") as f:
                for r in csv.DictReader(f):
                    if r.get("strategy") == strategy:
                        idx[(r["market_id"], r["decision"])] = r
        except Exception:
            continue
    return idx


def _real_trades(strategy, subtype, direccion):
    filas = []
    with open(TRADES, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if (r.get("strategy") == strategy and r.get("subtype") == subtype
                    and r.get("direction") == direccion and r.get("status") == "CLOSED"
                    and "maker_pilot=1" not in (r.get("notas") or "")):
                try:
                    filas.append((r["market_id"], r["outcome_real"] == "YES",
                                  float(r["pnl_neto_eur"])))
                except (ValueError, KeyError):
                    continue
    return filas


def _eval(feats, feature, condicion, umbral):
    v = feats.get(feature)
    if v is None:
        return None
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None
    if condicion == "gt": return v > umbral
    if condicion == "lt": return v < umbral
    if condicion == "abs_gt": return abs(v) > umbral
    if condicion == "abs_lt": return abs(v) < umbral
    return None


def _stats(rows):
    n = len(rows)
    if n == 0:
        return None
    hit = sum(1 for _, ok, _ in rows if ok) / n
    pnl = sum(p for _, _, p in rows)
    return n, hit, pnl, pnl / n


def main():
    params = json.loads(STRATEGY_PARAMS.read_text())
    est = params.get("estrategias", params)
    tuplas = _tuplas_live()
    if not tuplas:
        print("Sin pares_permitidos_live legible, nada que auditar.")
        return

    print(f"Auditando {len(tuplas)} tupla(s) live contra ejecución real:\n")
    contradicciones = 0
    for strategy, activo, duracion, direccion in tuplas:
        subtype = f"{activo}#{duracion}"
        real = _real_trades(strategy, subtype, direccion)
        if len(real) < 10:
            print(f"{strategy}#{subtype}#{direccion}: n real={len(real)} insuficiente, se salta\n")
            continue
        pred_idx = _pred_index(strategy)
        real_con_feats = []
        for mid, ok, pnl in real:
            pred = pred_idx.get((mid, direccion))
            feats = {}
            if pred:
                try:
                    feats = json.loads(pred.get("features") or "{}")
                except Exception:
                    feats = {}
            real_con_feats.append((feats, ok, pnl))

        claves = {strategy, f"{strategy}#{subtype}", f"{strategy}#{activo}", f"{strategy}#{duracion}"}
        patrones = []
        for clave in claves:
            for p in (est.get(clave, {}) or {}).get("patrones_ganadores", []) or []:
                if p.get("direccion") == direccion:
                    patrones.append((clave, p))

        print(f"=== {strategy}#{subtype}#{direccion} (n real={len(real)}) ===")
        if not patrones:
            print("  sin patrones_ganadores activos para esta dirección\n")
            continue
        for clave, p in patrones:
            feature, cond, umbral = p["feature"], p["condicion"], p["umbral"]
            dentro = [(f, ok, pnl) for f, ok, pnl in real_con_feats if _eval(f, feature, cond, umbral) is True]
            fuera = [(f, ok, pnl) for f, ok, pnl in real_con_feats if _eval(f, feature, cond, umbral) is False]
            sd, sf = _stats(dentro), _stats(fuera)
            veredicto = "n insuficiente"
            if sd and sf:
                veredicto = "✅ consistente" if sd[3] >= sf[3] else "⚠️  CONTRADICE"
                if veredicto.startswith("⚠️"):
                    contradicciones += 1
            print(f"  [{clave}] {feature} {cond} {umbral} (shadow ic_patron={p['ic_patron']:+.3f} n={p['n_patron']})")
            print(f"    real DENTRO: {sd if sd else 'n=0'}  |  real FUERA: {sf if sf else 'n=0'}  -> {veredicto}")
        print()

    print(f"Total contradicciones encontradas: {contradicciones}")
    if contradicciones:
        print("⚠️  Estos patrones NO deben usarse para dimensionar Kelly sin más "
              "validación real, aunque hoy sean inertes (stake pineado).")


if __name__ == "__main__":
    main()
