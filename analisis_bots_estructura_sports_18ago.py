#!/usr/bin/env python3
"""analisis_bots_estructura_sports_18ago.py — minar la ESTRUCTURA de los
bots que dominan volumen en sports/esports (firehose completo, no solo
whale-tier significativo), petición explícita Javi 18-Ago: "los bots
tienen estructura y procedimientos que nos pueden servir a nosotros para
minar pasta... aquí hemos venido a hacer dinero a toda costa."

No es un gate de promoción -- es minería de patrones operativos (¿a qué
precio entran? ¿cuántas categorías tocan? ¿compran y venden ambos lados?
¿qué tan concentrados en el tiempo?) para robar la mecánica, igual que ya
se hizo en weather (day-1: 2 bots comprando favorito ~0.80 y manteniendo,
resolution farmers entrando a 0.999, 1 market-maker 87% SELL en 102
ciudades).

Streaming, sin materializar filas (mismo patrón de
weather_wallet_edge_tracker.py tras el incidente de OOM de hoy) -- solo
acumuladores por wallet.
"""
import csv
import glob
import gzip
from collections import defaultdict

DATALOGS = "/root/polymarket-research-datalogs"


def _stat():
    return {"n": 0, "usd": 0.0, "n_buy": 0, "n_sell": 0, "cats": set(),
            "cids": set(), "precios": [], "dias": set()}


def main():
    files = sorted(glob.glob(f"{DATALOGS}/polymarket_activity_*.csv*"))
    print(f"{len(files)} ficheros firehose")
    por_wallet = defaultdict(_stat)
    n_filas = 0
    n_sports = 0
    for path in files:
        opener = gzip.open if path.endswith(".gz") else open
        with opener(path, "rt") as f:
            for r in csv.DictReader(f):
                n_filas += 1
                if r.get("activo"):
                    continue  # fila de cripto, no de sports/esports
                title = r.get("title", "")
                if not title:
                    continue
                n_sports += 1
                w = (r.get("wallet") or "").lower()
                if not w:
                    continue
                try:
                    price = float(r["price"])
                    usd = float(r.get("usd_value") or 0)
                except (ValueError, KeyError):
                    continue
                d = por_wallet[w]
                d["n"] += 1
                d["usd"] += usd
                side = (r.get("side") or "").strip().upper()
                if side == "BUY":
                    d["n_buy"] += 1
                elif side == "SELL":
                    d["n_sell"] += 1
                d["cats"].add(title[:40])
                d["cids"].add(r.get("condition_id", ""))
                if len(d["precios"]) < 500:
                    d["precios"].append(price)
                ts = r.get("timestamp_utc", "")
                if ts:
                    d["dias"].add(ts[:10])
    print(f"{n_filas} filas totales, {n_sports} filas sports/esports, {len(por_wallet)} wallets únicas")

    filas = []
    for w, d in por_wallet.items():
        if d["n"] < 20:
            continue
        precios = sorted(d["precios"])
        n = len(precios)
        p_mediana = precios[n // 2] if n else 0
        p_alta = sum(1 for p in precios if p >= 0.90) / n if n else 0
        p_baja = sum(1 for p in precios if p <= 0.10) if n else 0
        n_dias = len(d["dias"])
        filas.append({
            "wallet": w, "n": d["n"], "usd": d["usd"],
            "n_mercados": len(d["cids"]), "n_titulos_distintos": len(d["cats"]),
            "pct_buy": d["n_buy"] / d["n"] if d["n"] else 0,
            "pct_sell": d["n_sell"] / d["n"] if d["n"] else 0,
            "precio_mediano": p_mediana, "pct_precio_alto_090": p_alta,
            "n_precio_bajo_010": p_baja, "n_dias_activo": n_dias,
            "trades_por_dia_activo": d["n"] / n_dias if n_dias else 0,
        })

    print("\n=== TOP 25 por VOLUMEN USD (posibles bots grandes) ===")
    for f in sorted(filas, key=lambda x: -x["usd"])[:25]:
        print(f"  {f['wallet'][:16]} usd={f['usd']:>10,.0f} n={f['n']:>5} mercados={f['n_mercados']:>4} "
              f"buy={f['pct_buy']*100:.0f}% sell={f['pct_sell']*100:.0f}% "
              f"p_med={f['precio_mediano']:.3f} p>=0.90={f['pct_precio_alto_090']*100:.0f}% "
              f"dias_act={f['n_dias_activo']} t/dia={f['trades_por_dia_activo']:.1f}")

    print("\n=== TOP 25 por FRECUENCIA (trades/día activo) — bots de alta cadencia ===")
    for f in sorted([x for x in filas if x["n_dias_activo"] >= 3], key=lambda x: -x["trades_por_dia_activo"])[:25]:
        print(f"  {f['wallet'][:16]} t/dia={f['trades_por_dia_activo']:>7.1f} n={f['n']:>5} usd={f['usd']:>10,.0f} "
              f"mercados={f['n_mercados']:>4} buy={f['pct_buy']*100:.0f}% sell={f['pct_sell']*100:.0f}% "
              f"p_med={f['precio_mediano']:.3f}")

    print("\n=== TOP 20 por AMPLITUD (nº mercados distintos tocados) — generalistas/MM ===")
    for f in sorted(filas, key=lambda x: -x["n_mercados"])[:20]:
        print(f"  {f['wallet'][:16]} mercados={f['n_mercados']:>5} n={f['n']:>5} usd={f['usd']:>10,.0f} "
              f"buy={f['pct_buy']*100:.0f}% sell={f['pct_sell']*100:.0f}% p_med={f['precio_mediano']:.3f}")

    print("\n=== 'Resolution farmers' — precio mediano >=0.97, n>=20 ===")
    for f in sorted([x for x in filas if x["precio_mediano"] >= 0.97], key=lambda x: -x["n"])[:20]:
        print(f"  {f['wallet'][:16]} p_med={f['precio_mediano']:.3f} n={f['n']:>5} usd={f['usd']:>10,.0f} "
              f"mercados={f['n_mercados']}")

    print("\n=== Market-makers (dos lados, SELL>=30%) ===")
    for f in sorted([x for x in filas if x["pct_sell"] >= 0.30], key=lambda x: -x["n"])[:20]:
        print(f"  {f['wallet'][:16]} sell={f['pct_sell']*100:.0f}% n={f['n']:>5} usd={f['usd']:>10,.0f} "
              f"mercados={f['n_mercados']}")


if __name__ == "__main__":
    main()
