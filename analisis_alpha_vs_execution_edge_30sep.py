#!/usr/bin/env python3
"""analisis_alpha_vs_execution_edge_30sep.py -- descomposición del PnL REAL (data/live/trades.csv)
en alpha direccional y execution edge (idea de polybot, prioridad Javi 29-Sep; Stage 0).

Por acción comprada del lado operado (precios en perspectiva del token comprado):
    alpha      = desenlace (1/0) - mid_en_decisión        -> ¿acertamos la dirección frente al mercado?
    execution  = mid_en_decisión - precio_pagado          -> ¿cuánto nos cuesta entrar? (taker: <0)
    bruto      = alpha + execution = desenlace - precio_pagado
    neto       = bruto - fee
Todo multiplicado por acciones = stake / precio_pagado.

MID en decisión, dos fuentes (siempre ANTERIOR a la orden, nunca posterior: look-ahead):
  1. `libro`: /root/polymarket-research-datalogs/libro_ambos_lados_*.csv(.gz) (bid y ask reales de
     ambos lados, desde 10-Sep): último snapshot <= hora de la orden, con su antigüedad.
  2. `api`: CLOB /prices-history (mid por minuto, funciona en mercados cerrados): último punto
     <= hora de la orden. Hasta ~60 s de antigüedad: en mercados de 5 min el precio se mueve, y
     si la estrategia entra a favor del movimiento el mid previo queda por DEBAJO del mid real
     -> infla alpha y hunde execution. Por eso se reporta la antigüedad y el contraste entre
     fuentes en los trades donde hay las dos.

Solo lectura de datos de producción. Caché de la API fuera de git. Salida:
data/shadow/alpha_vs_execution_edge.json + tabla por pantalla.
Uso: python3 analisis_alpha_vs_execution_edge_30sep.py [--sin-api]
"""
import bisect
import csv
import glob
import gzip
import json
import random
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
TRADES = REPO / "data" / "live" / "trades.csv"
DATALOGS = Path("/root/polymarket-research-datalogs")
CACHE = DATALOGS / "analisis_persistente_30sep" / "alpha_exec_api_cache.json"
OUT = REPO / "data" / "shadow" / "alpha_vs_execution_edge.json"
GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
EDAD_MAX_LIBRO_S = 30      # snapshot de libro más viejo que esto no vale como mid en decisión
EDAD_MAX_API_S = 90
N_MIN = 15                 # CLAUDE.md: ninguna conclusión con n<15


def _ts(s: str) -> float:
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def cargar_trades() -> list:
    out = []
    with open(TRADES, encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["status"] != "CLOSED":
                continue
            try:
                entry, stake = float(r["entry_price"]), float(r["stake_eur"])
                bruto, neto = float(r["pnl_bruto_eur"]), float(r["pnl_neto_eur"])
                fee = float(r["fee_eur"] or 0)
            except (ValueError, TypeError):
                continue
            if not (0 < entry < 1) or stake <= 0:
                continue
            r["_t"], r["_entry"], r["_stake"] = _ts(r["timestamp_utc"]), entry, stake
            r["_bruto"], r["_neto"], r["_fee"] = bruto, neto, fee
            r["_gana"] = 1 if bruto > 0 else 0
            out.append(r)
    return out


def mids_api(trades: list, usar_red: bool) -> dict:
    """market_id -> {'tokens': [yes, no], 'hist': {t_orden: [[t, p_yes], ...]}} (cacheado)."""
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    try:
        cache = json.loads(CACHE.read_text())
    except Exception:
        cache = {}
    if not usar_red:
        return cache
    ses = requests.Session()
    nuevos = 0
    for r in trades:
        mid, clave_t = r["market_id"], str(int(r["_t"]))
        ent = cache.setdefault(mid, {"tokens": None, "hist": {}})
        try:
            if ent["tokens"] is None:
                m = ses.get(f"{GAMMA}/markets/{mid}", timeout=15).json()
                ent["tokens"] = json.loads(m.get("clobTokenIds") or "[]")
                time.sleep(0.12)
            if clave_t not in ent["hist"] and ent["tokens"]:
                h = ses.get(f"{CLOB}/prices-history", params={
                    "market": ent["tokens"][0], "startTs": int(r["_t"]) - 900,
                    "endTs": int(r["_t"]) + 5, "fidelity": 1}, timeout=15).json()
                ent["hist"][clave_t] = [[p["t"], p["p"]] for p in h.get("history", [])]
                nuevos += 1
                time.sleep(0.12)
        except Exception as e:
            print(f"  (api {mid}: {type(e).__name__})", flush=True)
            time.sleep(1)
        if nuevos and nuevos % 100 == 0:
            CACHE.write_text(json.dumps(cache))
            print(f"  api: {nuevos} históricos nuevos", flush=True)
    CACHE.write_text(json.dumps(cache))
    return cache


def mids_libro(trades: list) -> dict:
    """market_id -> ([ts...], [mid_yes...]) desde libro_ambos_lados, solo mercados operados."""
    objetivo = {r["market_id"] for r in trades}
    serie = defaultdict(list)
    for p in sorted(glob.glob(str(DATALOGS / "libro_ambos_lados_*.csv*"))):
        ab = gzip.open(p, "rt", encoding="utf-8") if p.endswith(".gz") else open(p, encoding="utf-8")
        with ab as f:
            for row in csv.DictReader(f):
                if row.get("market_id") not in objetivo:
                    continue
                try:
                    by, ay = float(row["bid_yes"]), float(row["ask_yes"])
                except (ValueError, TypeError, KeyError):
                    continue
                if not (0 < by <= ay < 1):
                    continue
                serie[row["market_id"]].append((_ts(row["timestamp_utc"]), (by + ay) / 2, ay - by))
    out = {}
    for mid, v in serie.items():
        v.sort()
        out[mid] = ([t for t, _, _ in v], [m for _, m, _ in v], [s for _, _, s in v])
    return out


def descomponer(trades: list, api: dict, libro: dict) -> list:
    filas = []
    for r in trades:
        es_yes = r["direction"].upper().endswith(("YES", "UP"))
        mid_yes, fuente, edad, spread = None, None, None, None
        lb = libro.get(r["market_id"])
        if lb:
            i = bisect.bisect_right(lb[0], r["_t"]) - 1
            if i >= 0 and r["_t"] - lb[0][i] <= EDAD_MAX_LIBRO_S:
                mid_yes, fuente, edad, spread = lb[1][i], "libro", r["_t"] - lb[0][i], lb[2][i]
        mid_api = None
        h = (api.get(r["market_id"]) or {}).get("hist", {}).get(str(int(r["_t"])))
        if h:
            prev = [(t, p) for t, p in h if t <= r["_t"]]
            if prev and r["_t"] - prev[-1][0] <= EDAD_MAX_API_S:
                mid_api = prev[-1][1]
                if mid_yes is None:
                    mid_yes, fuente, edad = mid_api, "api", r["_t"] - prev[-1][0]
        if mid_yes is None:
            continue
        mid = mid_yes if es_yes else 1 - mid_yes
        acc = r["_stake"] / r["_entry"]
        alpha = (r["_gana"] - mid) * acc
        ejec = (mid - r["_entry"]) * acc
        sub = r["subtype"].split("#")
        filas.append({
            "ts": r["timestamp_utc"], "strategy": r["strategy"], "direction": r["direction"],
            "activo": sub[0] if sub else "", "marco": sub[1] if len(sub) > 1 else "",
            "entry": r["_entry"], "mid": round(mid, 4), "fuente": fuente, "edad_s": round(edad, 1),
            "spread": spread, "stake": r["_stake"], "alpha": alpha, "ejec": ejec, "fee": r["_fee"],
            "bruto_real": r["_bruto"], "neto_real": r["_neto"], "gana": r["_gana"],
            "mid_api_lado": None if mid_api is None else (mid_api if es_yes else 1 - mid_api),
        })
    return filas


def _ic90(vals: list, fechas: list) -> list:
    """IC90 bootstrap por DÍAS de la suma/stake (en % del stake no: en € por trade)."""
    dias = defaultdict(list)
    for v, d in zip(vals, fechas):
        dias[d].append(v)
    claves = list(dias)
    if len(claves) < 5:
        return None
    rng = random.Random(42)
    medias = []
    for _ in range(2000):
        m = [x for k in (rng.choice(claves) for _ in claves) for x in dias[k]]
        medias.append(sum(m) / len(m))
    medias.sort()
    return [round(medias[100], 4), round(medias[1900], 4)]


def resumir(filas: list) -> dict:
    n = len(filas)
    stake = sum(f["stake"] for f in filas)
    a, e, fee = sum(f["alpha"] for f in filas), sum(f["ejec"] for f in filas), sum(f["fee"] for f in filas)
    fechas = [f["ts"][:10] for f in filas]
    return {
        "n": n, "stake": round(stake, 2), "hit_pct": round(sum(f["gana"] for f in filas) / n * 100, 1),
        "entry_medio": round(sum(f["entry"] for f in filas) / n, 3),
        "mid_medio": round(sum(f["mid"] for f in filas) / n, 3),
        "alpha_eur": round(a, 2), "ejec_eur": round(e, 2), "fee_eur": round(fee, 2),
        "neto_eur": round(a + e - fee, 2),
        "alpha_pct_stake": round(a / stake * 100, 2), "ejec_pct_stake": round(e / stake * 100, 2),
        "fee_pct_stake": round(fee / stake * 100, 2),
        "ic90_alpha_por_trade": _ic90([f["alpha"] for f in filas], fechas),
        "ic90_ejec_por_trade": _ic90([f["ejec"] for f in filas], fechas),
        "dias": len(set(fechas)),
        "fuente_libro_pct": round(sum(f["fuente"] == "libro" for f in filas) / n * 100),
    }


def _tabla(titulo: str, grupos: dict, minimo: int = N_MIN) -> None:
    print(f"\n== {titulo} (n>={minimo}) ==")
    print(f"{'grupo':58s} {'n':>4s} {'hit%':>5s} {'entry':>6s} {'mid':>6s} {'alpha€':>8s} {'ejec€':>8s} {'fee€':>7s} "
          f"{'neto€':>8s} {'alpha%':>7s} {'ejec%':>7s}  IC90 alpha/trade      IC90 ejec/trade")
    for k, v in sorted(grupos.items(), key=lambda kv: -kv[1]["n"]):
        if v["n"] < minimo:
            continue
        print(f"{k[:58]:58s} {v['n']:4d} {v['hit_pct']:5.1f} {v['entry_medio']:6.3f} {v['mid_medio']:6.3f} "
              f"{v['alpha_eur']:8.2f} {v['ejec_eur']:8.2f} {v['fee_eur']:7.2f} {v['neto_eur']:8.2f} "
              f"{v['alpha_pct_stake']:7.2f} {v['ejec_pct_stake']:7.2f}  {str(v['ic90_alpha_por_trade']):20s} "
              f"{v['ic90_ejec_por_trade']}")


def main() -> int:
    trades = cargar_trades()
    print(f"trades reales CLOSED válidos: {len(trades)}")
    libro = mids_libro(trades)
    print(f"mercados con libro de ambos lados: {len(libro)}")
    api = mids_api(trades, usar_red="--sin-api" not in sys.argv)
    filas = descomponer(trades, api, libro)
    print(f"trades con mid en decisión: {len(filas)} (libro {sum(f['fuente'] == 'libro' for f in filas)}, "
          f"api {sum(f['fuente'] == 'api' for f in filas)}) | sin mid: {len(trades) - len(filas)}")
    err = [abs((f["alpha"] + f["ejec"]) - f["bruto_real"]) for f in filas]
    print(f"cuadre alpha+ejec vs pnl_bruto real: error medio {sum(err) / len(err):.4f} €, máx {max(err):.3f} €, "
          f">0,05 € en {sum(x > 0.05 for x in err)} trades")
    ambos = [f for f in filas if f["fuente"] == "libro" and f["mid_api_lado"] is not None]
    if ambos:
        d = sorted(f["mid"] - f["mid_api_lado"] for f in ambos)
        print(f"contraste de fuentes (n={len(ambos)}): mid_libro - mid_api  media {sum(d) / len(d):+.4f}  "
              f"mediana {d[len(d) // 2]:+.4f}  p5 {d[len(d) // 20]:+.3f}  p95 {d[-len(d) // 20]:+.3f}")

    def agrupar(clave):
        g = defaultdict(list)
        for f in filas:
            g[clave(f)].append(f)
        return {k: resumir(v) for k, v in g.items()}

    total = resumir(filas)
    por_familia = agrupar(lambda f: f"{f['strategy']}#{f['direction']}")
    por_tupla = agrupar(lambda f: f"{f['strategy']}#{f['activo']}#{f['marco']}#{f['direction']}")
    por_bucket = agrupar(lambda f: f"{f['strategy']}#{f['direction']}#[{int(f['entry'] * 10) / 10:.1f},{int(f['entry'] * 10) / 10 + 0.1:.1f})")
    por_fuente = agrupar(lambda f: f["fuente"])
    por_mes = agrupar(lambda f: f["ts"][:7])
    _tabla("TOTAL", {"TOTAL": total}, 1)
    _tabla("por fuente del mid", por_fuente, 1)
    _tabla("por mes", por_mes, 1)
    _tabla("por estrategia#dirección", por_familia)
    _tabla("por estrategia#activo#marco#dirección", por_tupla)
    _tabla("por estrategia#dirección#bucket de precio de entrada (0,10)", por_bucket)
    OUT.write_text(json.dumps({
        "generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "nota": "alpha=(desenlace-mid)*acciones; ejec=(mid-entry)*acciones; mid ANTERIOR a la orden "
                "(libro <=30 s, api <=90 s). n<15 no concluye.",
        "total": total, "por_fuente": por_fuente, "por_mes": por_mes, "por_familia": por_familia,
        "por_tupla": por_tupla, "por_bucket": por_bucket,
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
