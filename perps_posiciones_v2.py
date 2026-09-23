#!/usr/bin/env python3
"""perps_posiciones_v2.py -- (23-Sep, Perps) POSICIONES correctas desde el historial completo
(perps_fills_full/, ver fetch_polymarket_perps_fills_full.py). Sustituye al segmentador de
perps_rastreador_posiciones.py, que (medido 23-Sep) solo observaba 12/210 cierres y no
segmentaba las 2.323 inversiones de signo dentro de un solo fill.

## Semántica (datos reales, ver docstring del fetcher)
`previous_size` = tamaño CON SIGNO de la posición antes del fill (+ largo, - corto);
`side` = dirección del fill (long suma, short resta). Tras el fill: after = prev ± qty.
  - Abre posición: prev == 0  -> nueva posición.
  - Cierra: after == 0.
  - Inversión: prev y after de signo contrario -> el fill se PARTE: |prev| cierra la
    posición vigente y el residual abre la contraria. pnl y fee del fill se reparten
    proporcionalmente (el pnl realizado corresponde a la parte que reduce).
Integridad: la cadena prev_{i+1} == after_i debe cumplirse por (wallet, instrumento);
se mide y se reporta (`cadena_rota`), NO se asume.

## Salida por posición
address, instrument_id, lado, ts_apertura, ts_cierre, n_fills, notional_abre (Σ precio×qty de
los fills que suman), pnl_bruto (Σ pnl), fees, pnl_neto, ret_neto (pnl_neto/notional_abre),
cerrada (bool), liquidada (bool). NO incluye funding (no está en la API pública de fills:
limitación, no fingida).
"""
import csv
import glob
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent
DIR_FULL = REPO / "data/shadow/perps_fills_full"
EPS = 1e-9


def _f(x, d=0.0):
    try:
        return float(x)
    except (TypeError, ValueError):
        return d


def cargar_fills(direcciones=None) -> dict:
    """(address, instrument_id) -> lista de fills ordenados, dedup por trade_id.
    Cada fill: dict(ts, side, price, qty, prev, pnl, fee, liq)."""
    grupos = defaultdict(list)
    vistos = set()
    archivos = sorted(glob.glob(str(DIR_FULL / "*.csv")))
    for arch in archivos:
        if direcciones and Path(arch).stem not in direcciones:
            continue
        with open(arch, encoding="utf-8") as f:
            for r in csv.DictReader(f):
                tid = r.get("trade_id", "")
                if tid in vistos:
                    continue
                vistos.add(tid)
                try:
                    ts = int(r["ts_ms"])
                except (KeyError, ValueError):
                    continue
                grupos[(r["address"], r["instrument_id"])].append({
                    "ts": ts, "side": r.get("side", ""), "price": _f(r.get("price")),
                    "qty": _f(r.get("quantity")), "prev": _f(r.get("previous_size")),
                    "pnl": _f(r.get("pnl")), "fee": _f(r.get("fee")),
                    "liq": str(r.get("liquidation", "")).lower() == "true",
                    "oid": r.get("order_id") or ""})
    for k in list(grupos):
        grupos[k] = _ordenar_por_cadena(_agrupar_ordenes(grupos[k]))
    return grupos


def _agrupar_ordenes(fills: list) -> list:
    """`previous_size` es el tamano ANTES DE LA ORDEN (medido 23-Sep): todos los fills de una
    orden lo comparten. Se agrupa por order_id (respaldo: (ts, side, prev)) sumando qty/pnl/fee,
    precio = vwap; la cadena prev_{i+1}==after_i solo tiene sentido a nivel de orden."""
    ord_, orden_llegada = {}, []
    for f in fills:
        k = f["oid"] or (f["ts"], f["side"], f["prev"])
        o = ord_.get(k)
        if o is None:
            ord_[k] = o = {"ts": f["ts"], "side": f["side"], "prev": f["prev"], "qty": 0.0, "notion": 0.0,
                           "pnl": 0.0, "fee": 0.0, "liq": False}
        o["qty"] += f["qty"]; o["notion"] += f["price"] * f["qty"]
        o["pnl"] += f["pnl"]; o["fee"] += f["fee"]; o["liq"] = o["liq"] or f["liq"]
        o["ts"] = min(o["ts"], f["ts"])
    out = []
    for o in ord_.values():
        o["price"] = o["notion"] / o["qty"] if o["qty"] > 0 else 0.0
        out.append(o)
    return out


def _after(f: dict) -> float:
    return f["prev"] + (f["qty"] if f["side"] == "long" else -f["qty"])


def _ordenar_por_cadena(fills: list) -> list:
    """Orden por ts; dentro de un mismo ts_ms (varios fills el mismo milisegundo, el
    orden que devuelve la API no es fiable) se reordena siguiendo la cadena
    prev_{i+1} == after_i cuando es posible."""
    fills.sort(key=lambda x: x["ts"])
    out, i, n = [], 0, len(fills)
    while i < n:
        j = i
        while j < n and fills[j]["ts"] == fills[i]["ts"]:
            j += 1
        grupo = fills[i:j]
        if len(grupo) > 1:
            resto, cadena = list(grupo), []
            # candidatos de inicio: el que no es sucesor de ningun otro del grupo
            afters = [_after(g) for g in resto]
            def _es_sucesor(g):
                return any(abs(g["prev"] - a) <= 1e-6 * max(1.0, abs(a)) for a in afters if a is not None)
            inicio = [g for g in resto if not _es_sucesor(g)] or resto[:1]
            cur = inicio[0]
            resto.remove(cur); cadena.append(cur)
            while resto:
                a = _after(cur)
                sig = next((g for g in resto if abs(g["prev"] - a) <= 1e-6 * max(1.0, abs(a))), None)
                if sig is None:
                    break
                resto.remove(sig); cadena.append(sig); cur = sig
            grupo = cadena + resto
        out.extend(grupo)
        i = j
    return out


def _nueva(ts: int, lado: str) -> dict:
    return {"lado": lado, "ts_apertura": ts, "ts_cierre": ts, "n_fills": 0, "notional_abre": 0.0,
            "pnl_bruto": 0.0, "fees": 0.0, "cerrada": False, "liq": False}


def segmentar(fills: list) -> tuple:
    """fills ordenados de un (address, instrumento) -> (posiciones, n_cadena_rota).
    Una posicion 'cerrada' tiene el cierre (after==0 o inversion) OBSERVADO; la ultima puede
    seguir abierta. Historial que empieza con posicion ya abierta se ignora hasta su cierre."""
    pos, cur, rota, esperado = [], None, 0, None
    for f in fills:
        prev, qty = f["prev"], f["qty"]
        if esperado is not None and abs(prev - esperado) > 1e-6 * max(1.0, abs(esperado)):
            rota += 1
        signed = qty if f["side"] == "long" else -qty
        after = prev + signed
        esperado = after

        def _sumar(frac, abre_notional):
            cur["n_fills"] += 1
            cur["ts_cierre"] = f["ts"]
            cur["fees"] += f["fee"] * frac
            if abre_notional:
                cur["notional_abre"] += f["price"] * qty * frac
            if f["liq"]:
                cur["liq"] = True

        if abs(prev) <= EPS:                          # abre
            if cur is not None:
                pos.append(cur)                        # anterior sin cierre observado (hueco de datos)
            cur = _nueva(f["ts"], "long" if signed > 0 else "short")
            _sumar(1.0, True)
        elif prev * signed > 0:                        # suma en la misma direccion
            if cur is not None:
                _sumar(1.0, True)
        else:                                          # reduce / cierra / invierte
            cierra = min(abs(signed), abs(prev))
            frac = cierra / abs(signed)
            if cur is not None:
                _sumar(frac, False)
                cur["pnl_bruto"] += f["pnl"]           # pnl realizado = parte que reduce
            if abs(after) <= EPS:
                if cur is not None:
                    cur["cerrada"] = True
                    pos.append(cur)
                cur = None
            elif prev * after < 0:                     # inversion: cierra la vieja, abre la contraria
                if cur is not None:
                    cur["cerrada"] = True
                    pos.append(cur)
                cur = _nueva(f["ts"], "long" if after > 0 else "short")
                _sumar(1.0 - frac, True)
    if cur is not None:
        pos.append(cur)
    for p in pos:
        p["pnl_neto"] = p["pnl_bruto"] - p["fees"]
        p["ret_neto"] = p["pnl_neto"] / p["notional_abre"] if p["notional_abre"] > 0 else 0.0
    return pos, rota
