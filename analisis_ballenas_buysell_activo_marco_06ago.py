#!/usr/bin/env python3
"""
analisis_ballenas_buysell_activo_marco_06ago.py — Estudio de ballenas/wallets
expertas que ganan dinero COMPRANDO Y VENDIENDO posiciones (no solo
manteniendo hasta resolución), desagregado por (activo, marco temporal),
restringido a NUESTRO universo de mercados (Up/Down BTC/ETH/SOL/XRP/DOGE/BNB
en slots 5/15/60min -- mismo ACTIVOS_REF/_parse_updown_tipo que
shadow_predict.py, duplicado aquí en vez de importar el módulo completo
para evitar su cadena de imports pesada -- websockets, ballenas_firehose_
cache -- en un script de análisis puntual, solo lectura).

Petición explícita Javi (06-Ago): "estudiar ballenas con mucho pnl sacado
de hacer eso [comprar y vender] y wallets expertas, solo centrándote en el
mercado cripto que operamos nosotros [...] no mires una, mira todas las
que hacen eso [...] desagregado y granulado al máximo [por marco temporal
y moneda]".

Universo de wallets: `data/shadow/ballenas_diario.csv` (ya lo mantiene
wallet_pnl_diario.py, cron diario) -- últimos 5 días, sell_n>=20 (actividad
de venta real, no solo hold-to-redeem) y pnl_neto agregado > 0. Para cada
wallet: `/activity` real (misma API que wallet_pnl_diario.py) para
clasificar cada trade por (activo, marco) y detectar pares BUY+SELL en el
MISMO mercado por la MISMA wallet -- mide el gap temporal entre el buy y el
sell más cercano (spread capture casi simultáneo vs salida direccional con
más margen) y el "spread" implícito (precio_venta - precio_compra si es la
misma dirección, o 1-(p_buy+p_sell) si son direcciones opuestas -- patrón
de maker de dos lados).

Solo lectura -- no toca dinero ni config. Salida:
data/shadow/ballenas_buysell_activo_marco.json
"""
import json
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
sys.path.insert(0, str(REPO))

DIARIO = REPO / "data/shadow/ballenas_diario.csv"
OUT = REPO / "data/shadow/ballenas_buysell_activo_marco.json"
DATA_API = "https://data-api.polymarket.com"

DIAS_VENTANA = 5
SELL_N_MIN = 20
MAX_WALLETS = 30
MAX_EVENTOS_POR_WALLET = 1500

ACTIVOS_REF = {
    "BTC":  ("bitcoin",  "btc"),
    "ETH":  ("ethereum", "eth"),
    "SOL":  ("solana",   "sol"),
    "XRP":  ("xrp",      "ripple"),
    "DOGE": ("dogecoin", "doge", "dogo"),
    "BNB":  ("bnb",      "binance coin"),
}


def identificar_activo(question: str):
    q = (question or "").lower()
    best, best_len = None, 0
    for tk, kws in ACTIVOS_REF.items():
        for kw in kws:
            if kw in q and len(kw) > best_len:
                best, best_len = tk, len(kw)
    return best


def parse_marco(question: str):
    """Devuelve minutos de ventana (5/15/60) o None si no es un slot
    Up/Down de los que operamos. Mismo regex que
    shadow_predict.py::_parse_updown_tipo, versión reducida (solo 'slot')."""
    q = (question or "").lower()
    if "up or down" not in q:
        return None
    import re
    m = re.search(r'(\d+):(\d+)(am|pm)-(\d+):(\d+)(am|pm)', q)
    if not m:
        return None
    def to_min(h, mn, mer):
        h = int(h) % 12 + (12 if mer == 'pm' else 0)
        return h * 60 + int(mn)
    t1 = to_min(m.group(1), m.group(2), m.group(3))
    t2 = to_min(m.group(4), m.group(5), m.group(6))
    diff = (t2 - t1) % (24 * 60)
    return diff if diff in (5, 15, 60) else None


def cargar_wallets_candidatas():
    hoy = datetime.now(timezone.utc).date()
    desde = (hoy - timedelta(days=DIAS_VENTANA)).isoformat()
    agg = defaultdict(lambda: {"pnl": 0.0, "sell_n": 0, "buy_n": 0, "nombre": ""})
    import csv
    with open(DIARIO, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row["fecha"] < desde:
                continue
            w = row["wallet"]
            agg[w]["pnl"] += float(row["pnl_neto"] or 0)
            agg[w]["sell_n"] += int(row["sell_n"] or 0)
            agg[w]["buy_n"] += int(row["buy_n"] or 0)
            agg[w]["nombre"] = row["nombre"]
    candidatos = [(w, v) for w, v in agg.items() if v["sell_n"] >= SELL_N_MIN and v["pnl"] > 0]
    candidatos.sort(key=lambda x: -x[1]["pnl"])
    return candidatos[:MAX_WALLETS]


def fetch_activity(wallet: str, max_events: int = MAX_EVENTOS_POR_WALLET) -> list:
    eventos = []
    offset = 0
    while offset < max_events:
        try:
            r = requests.get(f"{DATA_API}/activity",
                              params={"user": wallet, "limit": 500, "offset": offset},
                              timeout=15)
            r.raise_for_status()
            d = r.json()
        except Exception as e:
            print(f"  [warn] fetch_activity({wallet[:10]}) offset={offset}: {e}")
            break
        if not d:
            break
        eventos.extend(d)
        offset += 500
        if len(d) < 500:
            break
    return eventos


def procesar_wallet(wallet: str, nombre: str, eventos: list):
    """Filtra a TRADE en nuestro universo (activo+marco), agrupa por
    (activo, marco, conditionId) y busca el par buy/sell más cercano en el
    tiempo dentro del mismo mercado."""
    por_mercado = defaultdict(list)  # (activo,marco,conditionId) -> [(ts,side,price,size)]
    for ev in eventos:
        if ev.get("type") != "TRADE":
            continue
        q = ev.get("title") or ev.get("slug") or ""
        activo = identificar_activo(q)
        marco = parse_marco(q)
        if activo is None or marco is None:
            continue
        cid = ev.get("conditionId")
        side = ev.get("side")
        price = ev.get("price")
        size = ev.get("size")
        ts = ev.get("timestamp")
        if cid is None or side not in ("BUY", "SELL") or price is None or ts is None:
            continue
        por_mercado[(activo, marco, cid)].append((int(ts), side, float(price), float(size or 0)))

    resultado = defaultdict(lambda: {
        "n_mercados_con_buy_y_sell": 0, "n_pares": 0, "gaps_s": [], "spreads": [],
        "volumen_usd": 0.0,
    })
    for (activo, marco, cid), trades in por_mercado.items():
        trades.sort(key=lambda t: t[0])
        buys = [t for t in trades if t[1] == "BUY"]
        sells = [t for t in trades if t[1] == "SELL"]
        if not buys or not sells:
            continue
        clave = (activo, marco)
        resultado[clave]["n_mercados_con_buy_y_sell"] += 1
        # empareja cada sell con el buy más cercano en el tiempo (antes o
        # después, ambos son informativos: casi-simultáneo = maker de dos
        # lados, con gap = entra y sale de una posición direccional)
        for s_ts, _, s_price, s_size in sells:
            mejor = min(buys, key=lambda b: abs(b[0] - s_ts))
            gap = abs(mejor[0] - s_ts)
            resultado[clave]["gaps_s"].append(gap)
            resultado[clave]["n_pares"] += 1
            resultado[clave]["volumen_usd"] += s_price * s_size
            # spread implícito: si BUY y SELL son la misma dirección de
            # apuesta (imposible distinguir aquí sin el outcome exacto),
            # mejor proxy simple: diferencia de precio absoluta entre el
            # buy emparejado y este sell -- alto = venta con margen,
            # bajo/negativo = venta a pérdida o cobertura del lado opuesto
            resultado[clave]["spreads"].append(s_price - mejor[2])
    return resultado


def main() -> int:
    candidatos = cargar_wallets_candidatas()
    print(f"[analisis_ballenas_buysell] {len(candidatos)} wallets candidatas "
          f"(sell_n>={SELL_N_MIN}, pnl {DIAS_VENTANA}d>0)")

    agregado = defaultdict(lambda: {
        "wallets": set(), "n_mercados_con_buy_y_sell": 0, "n_pares": 0,
        "gaps_s": [], "spreads": [], "volumen_usd": 0.0,
    })
    detalle_wallets = {}

    for i, (wallet, info) in enumerate(candidatos):
        print(f"[{i+1}/{len(candidatos)}] {info['nombre']} ({wallet[:10]}...) "
              f"pnl_{DIAS_VENTANA}d={info['pnl']:.0f}...", flush=True)
        eventos = fetch_activity(wallet)
        res = procesar_wallet(wallet, info["nombre"], eventos)
        detalle_wallets[wallet] = {
            "nombre": info["nombre"], "pnl_ventana": info["pnl"],
            "por_activo_marco": {
                f"{a}#{m}min": {
                    "n_mercados": v["n_mercados_con_buy_y_sell"],
                    "n_pares": v["n_pares"],
                    "gap_mediana_s": sorted(v["gaps_s"])[len(v["gaps_s"])//2] if v["gaps_s"] else None,
                    "volumen_usd": round(v["volumen_usd"], 1),
                } for (a, m), v in res.items()
            },
        }
        for (a, m), v in res.items():
            clave = f"{a}#{m}min"
            agregado[clave]["wallets"].add(wallet)
            agregado[clave]["n_mercados_con_buy_y_sell"] += v["n_mercados_con_buy_y_sell"]
            agregado[clave]["n_pares"] += v["n_pares"]
            agregado[clave]["gaps_s"].extend(v["gaps_s"])
            agregado[clave]["spreads"].extend(v["spreads"])
            agregado[clave]["volumen_usd"] += v["volumen_usd"]
        time.sleep(0.3)  # cortesía con la API pública

    resumen = {}
    for clave, v in sorted(agregado.items(), key=lambda kv: -kv[1]["volumen_usd"]):
        gaps = sorted(v["gaps_s"])
        spreads = sorted(v["spreads"])
        resumen[clave] = {
            "n_wallets_distintas": len(v["wallets"]),
            "n_mercados_con_buy_y_sell": v["n_mercados_con_buy_y_sell"],
            "n_pares_buy_sell": v["n_pares"],
            "volumen_usd": round(v["volumen_usd"], 1),
            "gap_mediana_s": gaps[len(gaps)//2] if gaps else None,
            "gap_p25_s": gaps[len(gaps)//4] if gaps else None,
            "gap_p75_s": gaps[3*len(gaps)//4] if gaps else None,
            "spread_medio": round(sum(spreads)/len(spreads), 4) if spreads else None,
        }

    salida = {
        "generado_utc": datetime.now(timezone.utc).isoformat(),
        "n_wallets_analizadas": len(candidatos),
        "resumen_por_activo_marco": resumen,
        "detalle_wallets": detalle_wallets,
    }
    OUT.write_text(json.dumps(salida, indent=2, ensure_ascii=False))
    print(f"\n[analisis_ballenas_buysell] guardado en {OUT}")
    print("\n=== RESUMEN POR (ACTIVO, MARCO) ===")
    for clave, r in resumen.items():
        print(f"{clave:10s} wallets={r['n_wallets_distintas']:3d} "
              f"mercados={r['n_mercados_con_buy_y_sell']:5d} pares={r['n_pares_buy_sell']:5d} "
              f"vol=${r['volumen_usd']:12,.0f} gap_mediana={r['gap_mediana_s']}s "
              f"spread_medio={r['spread_medio']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
