#!/usr/bin/env python3
"""
analisis_perps_categorizacion_universo.py -- 14-Sep, petición explícita
Javi: "tiene que haber una manera de identificar grandes jugadas, estudia
todas las categorías posibles de las wallets, de los bots, de todo el
universo Perps... las ballenas, las wallets informadas, los insiders,
las wallets de nicho saben todo, ahí es donde hay que estar y recopilar
datos."

Usa la taxonomía OFICIAL de la API (`/v1/info/instruments::category`,
cacheada en polymarket_perps_instruments.json) en vez de inventar una:
`index` (3), `commodity` (4 -- oro/plata/petróleo), `crypto` (40, majors
Y memecoins MEZCLADOS, la API no los separa), `equity` (36). Sub-divide
`crypto` en `crypto_memecoin`/`crypto_major` a mano (lista curada, ver
MEMECOINS abajo) porque es justo la distinción que pide Javi y la API no
la da.

Para cada wallet de la watchlist (`polymarket_perps_wallet_fills_*.csv`,
todo el histórico acumulado desde 09-Sep), calcula:
  - Especialización: % de notional por categoría -- ¿wallet generalista
    o especialista de nicho (ballena de un solo instrumento)?
  - "Grandes jugadas": operaciones individuales con notional (price×qty)
    por encima del percentil 95 de TODA la actividad observada en su
    categoría -- estas son las jugadas que de verdad importan vigilar,
    no el ruido de miles de fills pequeños de bots de market-making.
  - Liquidaciones propias (columna `liquidation`): cuántas veces a esta
    wallet la liquidaron -- señal de riesgo mal gestionado, NO de
    insider (un insider no se deja liquidar).
  - Ratio taker/maker: alta agresividad (taker) sugiere convicción de
    timing; alta pasividad (maker) sugiere proveer liquidez, no apostar
    dirección.

LIMITACIÓN ESTRUCTURAL (Fail Loud, verificada antes de prometer nada):
la API pública (`/v1/info/position-fills?address=&instrument_id=`) exige
conocer la wallet DE ANTEMANO -- no existe endpoint público de "todas las
trades recientes de este instrumento, cualquier wallet" (firehose), a
diferencia de Polymarket predicciones (RTDS websocket). Esto significa
que NO podemos descubrir insiders/wallets de nicho que no aparezcan ya
en el leaderboard (day/week/all, top50) -- la watchlist de
fetch_polymarket_perps_wallet_fills.py (TOP_WALLETS=30) es today el techo
real de cobertura, no una limitación de este script. Si aparece un
endpoint de trades globales en el futuro, este es el punto a extender.

Solo lectura -- no toca dinero real (Perps no tiene ejecución todavía).
Salida: data/shadow/perps_categorizacion_universo.json.
"""
import csv
import glob
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parent
FILLS_GLOB = str(REPO / "data/shadow/polymarket_perps_wallet_fills_*.csv")
INSTRUMENTS = REPO / "data/shadow/polymarket_perps_instruments.json"
OUT = REPO / "data/shadow/perps_categorizacion_universo.json"

# Curada a mano -- la API mete memecoins dentro de 'crypto' sin distinguir.
# Ampliar aquí si polymarket_perps_market_*.csv muestra símbolos nuevos con
# pinta de memecoin (nombre de meme, no un proyecto real conocido).
MEMECOINS = {"FARTCOIN-USD", "CASHCAT-USD", "KPEPE-USD", "KSHIB-USD", "PUMP-USD", "USELESS-USD"}

PERCENTIL_GRANDE = 0.95


def _cargar_categoria_por_symbol() -> dict[str, str]:
    try:
        instrumentos = json.loads(INSTRUMENTS.read_text(encoding="utf-8"))
    except Exception:
        return {}
    out = {}
    for i in instrumentos:
        sym = i.get("symbol", "")
        cat = i.get("category", "otros")
        if cat == "crypto" and sym in MEMECOINS:
            cat = "crypto_memecoin"
        elif cat == "crypto":
            cat = "crypto_major"
        out[sym] = cat
    return out


def _cargar_fills() -> list[dict]:
    filas = []
    for fn in sorted(glob.glob(FILLS_GLOB)):
        with open(fn, encoding="utf-8") as f:
            filas.extend(csv.DictReader(f))
    return filas


def main() -> int:
    cat_por_symbol = _cargar_categoria_por_symbol()
    filas = _cargar_fills()
    print(f"[perps_categorizacion] {len(filas)} fills cargados, {len(cat_por_symbol)} símbolos categorizados")

    notional_por_categoria: dict = defaultdict(list)  # categoria -> [notional, ...] (para percentil)
    por_wallet: dict = defaultdict(lambda: {
        "notional_por_categoria": defaultdict(float),
        "n_por_categoria": defaultdict(int),
        "n_liquidaciones": 0,
        "n_taker": 0,
        "n_total": 0,
        "grandes_jugadas": [],
    })

    for r in filas:
        try:
            price = float(r.get("price") or 0)
            qty = float(r.get("quantity") or 0)
        except (TypeError, ValueError):
            continue
        notional = abs(price * qty)
        if notional <= 0:
            continue
        sym = r.get("symbol", "")
        cat = cat_por_symbol.get(sym, "otros")
        addr = r.get("address", "")
        w = por_wallet[addr]
        w["notional_por_categoria"][cat] += notional
        w["n_por_categoria"][cat] += 1
        w["n_total"] += 1
        if r.get("liquidation") in ("True", "1", "true"):
            w["n_liquidaciones"] += 1
        if r.get("taker") in ("True", "1", "true"):
            w["n_taker"] += 1
        notional_por_categoria[cat].append(notional)
        w.setdefault("_fills_crudos", []).append((notional, cat, sym, r.get("fill_timestamp_utc", ""), r.get("pnl", "")))

    # Percentil 95 de notional POR CATEGORÍA (una jugada "grande" en
    # equity no es la misma cifra que una grande en un commodity de bajo
    # volumen -- nunca un umbral absoluto global).
    p95_por_cat = {}
    for cat, vals in notional_por_categoria.items():
        vals_sorted = sorted(vals)
        p95_por_cat[cat] = vals_sorted[int(len(vals_sorted) * PERCENTIL_GRANDE)] if vals_sorted else 0.0

    resultado = {"generado_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 "p95_notional_por_categoria": {k: round(v, 2) for k, v in p95_por_cat.items()},
                 "wallets": {}}

    for addr, w in por_wallet.items():
        n_total = w["n_total"]
        if n_total == 0:
            continue
        notional_total = sum(w["notional_por_categoria"].values())
        cat_dominante = max(w["notional_por_categoria"], key=w["notional_por_categoria"].get)
        pct_dominante = round(100 * w["notional_por_categoria"][cat_dominante] / notional_total, 1) if notional_total else 0.0

        grandes = [(notional, cat, sym, ts, pnl) for notional, cat, sym, ts, pnl in w["_fills_crudos"]
                   if notional >= p95_por_cat.get(cat, float("inf"))]
        grandes.sort(key=lambda x: -x[0])

        resultado["wallets"][addr] = {
            "n_total_fills": n_total,
            "notional_total": round(notional_total, 2),
            "categoria_dominante": cat_dominante,
            "pct_notional_dominante": pct_dominante,
            "es_especialista_nicho": pct_dominante >= 70.0,
            "n_liquidaciones_propias": w["n_liquidaciones"],
            "pct_taker": round(100 * w["n_taker"] / n_total, 1),
            "n_grandes_jugadas": len(grandes),
            "grandes_jugadas_top5": [
                {"notional": round(nt, 2), "categoria": cat, "symbol": sym, "ts": ts, "pnl": pnl}
                for nt, cat, sym, ts, pnl in grandes[:5]
            ],
        }

    n_especialistas = sum(1 for v in resultado["wallets"].values() if v["es_especialista_nicho"])
    print(f"[perps_categorizacion] {len(resultado['wallets'])} wallets categorizadas, "
          f"{n_especialistas} especialistas de nicho (>=70% notional en 1 categoría)")
    for addr, v in sorted(resultado["wallets"].items(), key=lambda x: -x[1]["notional_total"])[:15]:
        marca = " ⭐ NICHO" if v["es_especialista_nicho"] else ""
        print(f"  {addr[:12]} notional={v['notional_total']:.0f} dominante={v['categoria_dominante']}"
              f"({v['pct_notional_dominante']}%) grandes_jugadas={v['n_grandes_jugadas']}"
              f" liquidaciones={v['n_liquidaciones_propias']}{marca}")

    OUT.write_text(json.dumps(resultado, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[perps_categorizacion] -> {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
