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

Petición explícita Javi (06-Ago, ampliada tras la v1 con proxy de spread):
"profundiza en todas las wallets y todas las monedas [...] este barrido
lo tienes que repetir todos los días [...] identificar oportunidades y
deficiencias de las ballenas para explotar nosotros lo que ellas no
hacen".

v2 (06-Ago, mismo día): sustituye el proxy de "sell - buy más cercano en
tiempo" de la v1 por RECONSTRUCCIÓN REAL de posición -- la API de
actividad de Polymarket da `asset` (id único del TOKEN del outcome
concreto, ej. "ETH Down 4:50-4:55am") y `outcomeIndex`/`outcome`, así que
se puede trackear (wallet, asset) con FIFO real: cada BUY apila lotes con
su precio, cada SELL consume lotes en orden FIFO y realiza PnL real
(precio_venta - precio_compra_del_lote) × cantidad -- ya no es un proxy,
es el PnL realizado real de cada round-trip.

Universo de wallets: `data/shadow/ballenas_diario.csv` (mantenido por
wallet_pnl_diario.py, cron diario) -- últimos 5 días, sell_n>=15 (bajado
de 20 en v1 para ampliar cobertura, petición "todas las wallets") y
pnl_neto agregado > 0.

Persiste histórico diario en data/shadow/ballenas_buysell_historico.csv
(una fila por (fecha, activo, marco), append) para poder ver si el
patrón (ej. dominancia de BTC) es persistente o una racha puntual --
cron diario, ver crontab.

Solo lectura -- no toca dinero ni config. Salida:
data/shadow/ballenas_buysell_activo_marco.json (foto del día)
data/shadow/ballenas_buysell_historico.csv (serie temporal, append)
"""
import csv
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
HISTORICO = REPO / "data/shadow/ballenas_buysell_historico.csv"
DATA_API = "https://data-api.polymarket.com"

DIAS_VENTANA = 5
SELL_N_MIN = 15
MAX_WALLETS = 50
MAX_EVENTOS_POR_WALLET = 2000

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


def reconstruir_roundtrips(eventos: list):
    """FIFO real por (activo,marco,asset). Devuelve lista de round-trips
    (activo, marco, asset, cantidad, precio_compra, precio_venta,
    pnl_realizado, gap_s, ts_venta)."""
    por_asset = defaultdict(list)  # asset -> [(ts,side,price,size,activo,marco)]
    for ev in eventos:
        if ev.get("type") != "TRADE":
            continue
        q = ev.get("title") or ev.get("slug") or ""
        activo = identificar_activo(q)
        marco = parse_marco(q)
        if activo is None or marco is None:
            continue
        asset = ev.get("asset")
        side = ev.get("side")
        price = ev.get("price")
        size = ev.get("size")
        ts = ev.get("timestamp")
        if asset is None or side not in ("BUY", "SELL") or price is None or ts is None:
            continue
        por_asset[asset].append((int(ts), side, float(price), float(size or 0), activo, marco))

    roundtrips = []
    for asset, trades in por_asset.items():
        trades.sort(key=lambda t: t[0])
        lotes = []  # FIFO: [(ts, precio, cantidad_restante)]
        activo = marco = None
        for ts, side, price, size, a, m in trades:
            activo, marco = a, m
            if side == "BUY":
                lotes.append([ts, price, size])
            else:  # SELL -- consume lotes FIFO
                restante = size
                while restante > 1e-9 and lotes:
                    lote = lotes[0]
                    usar = min(restante, lote[2])
                    pnl = (price - lote[1]) * usar
                    roundtrips.append({
                        "activo": activo, "marco": marco, "asset": asset,
                        "cantidad": usar, "precio_compra": lote[1], "precio_venta": price,
                        "pnl_realizado": pnl, "gap_s": ts - lote[0], "ts_venta": ts,
                    })
                    lote[2] -= usar
                    restante -= usar
                    if lote[2] <= 1e-9:
                        lotes.pop(0)
                # restante>0 sin lotes = venta sin compra previa en la ventana
                # capturada (posición abierta antes del rango de /activity
                # pedido) -- se ignora, no se puede calcular PnL real sin la
                # compra original.
    return roundtrips


def main() -> int:
    candidatos = cargar_wallets_candidatas()
    print(f"[analisis_ballenas_buysell] {len(candidatos)} wallets candidatas "
          f"(sell_n>={SELL_N_MIN}, pnl {DIAS_VENTANA}d>0)")

    agregado = defaultdict(lambda: {
        "wallets": set(), "n_roundtrips": 0, "pnl_total": 0.0, "wins": 0,
        "gaps_s": [], "volumen_usd": 0.0,
    })
    detalle_wallets = {}

    for i, (wallet, info) in enumerate(candidatos):
        print(f"[{i+1}/{len(candidatos)}] {info['nombre']} ({wallet[:10]}...) "
              f"pnl_{DIAS_VENTANA}d={info['pnl']:.0f}", flush=True)
        eventos = fetch_activity(wallet)
        rts = reconstruir_roundtrips(eventos)
        por_clave_wallet = defaultdict(lambda: {"n": 0, "pnl": 0.0, "wins": 0, "vol": 0.0})
        for rt in rts:
            clave = f"{rt['activo']}#{rt['marco']}min"
            por_clave_wallet[clave]["n"] += 1
            por_clave_wallet[clave]["pnl"] += rt["pnl_realizado"]
            por_clave_wallet[clave]["wins"] += 1 if rt["pnl_realizado"] > 0 else 0
            por_clave_wallet[clave]["vol"] += rt["cantidad"] * rt["precio_venta"]

            agregado[clave]["wallets"].add(wallet)
            agregado[clave]["n_roundtrips"] += 1
            agregado[clave]["pnl_total"] += rt["pnl_realizado"]
            agregado[clave]["wins"] += 1 if rt["pnl_realizado"] > 0 else 0
            agregado[clave]["gaps_s"].append(rt["gap_s"])
            agregado[clave]["volumen_usd"] += rt["cantidad"] * rt["precio_venta"]

        detalle_wallets[wallet] = {
            "nombre": info["nombre"], "pnl_ventana_diaria": info["pnl"],
            "por_activo_marco": {
                k: {"n_roundtrips": v["n"], "pnl_realizado": round(v["pnl"], 2),
                    "hit_rate": round(v["wins"] / v["n"], 3) if v["n"] else None,
                    "volumen_usd": round(v["vol"], 1)}
                for k, v in por_clave_wallet.items()
            },
        }
        time.sleep(0.3)

    resumen = {}
    for clave, v in sorted(agregado.items(), key=lambda kv: -kv[1]["n_roundtrips"]):
        gaps = sorted(v["gaps_s"])
        resumen[clave] = {
            "n_wallets_distintas": len(v["wallets"]),
            "n_roundtrips": v["n_roundtrips"],
            "pnl_total_realizado": round(v["pnl_total"], 2),
            "pnl_por_roundtrip": round(v["pnl_total"] / v["n_roundtrips"], 4) if v["n_roundtrips"] else None,
            "hit_rate": round(v["wins"] / v["n_roundtrips"], 3) if v["n_roundtrips"] else None,
            "volumen_usd": round(v["volumen_usd"], 1),
            "gap_mediana_s": gaps[len(gaps)//2] if gaps else None,
            "gap_p25_s": gaps[len(gaps)//4] if gaps else None,
            "gap_p75_s": gaps[3*len(gaps)//4] if gaps else None,
        }

    hoy_iso = datetime.now(timezone.utc).date().isoformat()
    salida = {
        "generado_utc": datetime.now(timezone.utc).isoformat(),
        "n_wallets_analizadas": len(candidatos),
        "resumen_por_activo_marco": resumen,
        "detalle_wallets": detalle_wallets,
    }
    OUT.write_text(json.dumps(salida, indent=2, ensure_ascii=False))

    nuevo_hist = not HISTORICO.exists()
    with open(HISTORICO, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if nuevo_hist:
            w.writerow(["fecha", "activo_marco", "n_wallets", "n_roundtrips",
                        "pnl_total", "pnl_por_roundtrip", "hit_rate", "volumen_usd",
                        "gap_mediana_s"])
        for clave, r in resumen.items():
            w.writerow([hoy_iso, clave, r["n_wallets_distintas"], r["n_roundtrips"],
                        r["pnl_total_realizado"], r["pnl_por_roundtrip"], r["hit_rate"],
                        r["volumen_usd"], r["gap_mediana_s"]])

    print(f"\n[analisis_ballenas_buysell] guardado en {OUT} + histórico en {HISTORICO}")
    print("\n=== RESUMEN POR (ACTIVO, MARCO) -- PnL REALIZADO REAL (FIFO) ===")
    for clave, r in resumen.items():
        print(f"{clave:10s} wallets={r['n_wallets_distintas']:3d} roundtrips={r['n_roundtrips']:5d} "
              f"pnl_total=${r['pnl_total_realizado']:10,.1f} pnl/rt={r['pnl_por_roundtrip']} "
              f"hit={r['hit_rate']} vol=${r['volumen_usd']:12,.0f} gap_mediana={r['gap_mediana_s']}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
