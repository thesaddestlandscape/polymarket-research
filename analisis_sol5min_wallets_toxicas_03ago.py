#!/usr/bin/env python3
"""
analisis_sol5min_wallets_toxicas_03ago.py — investiga POR QUÉ SOL#5m tiene
dosis-respuesta INVERSA (a más concentración de ballenas, peor acierta:
51.4%->16.3%, hallazgo 03-Ago vía analisis_ballenas_dosis_respuesta_16jul.py
"SOL#5m,ETH#5m,BTC#5m,XRP#5m,DOGE#5m,BNB#5m"), justo lo contrario de BTC/
ETH#5m. Petición explícita Javi: investigar en los datos de wallets/
ballenas qué explica esto para SOL.

Hipótesis a probar: la concentración alta del bucket [0.9,1.0) para SOL
está dominada por unas pocas wallets con edge NEGATIVO conocido (ver
wallet_edge_score_por_activo_marco.json), no por consenso amplio genuino
-- reusa exactamente la misma muestra/banda que el script canónico
(import directo, no reimplementa la lógica de muestreo/banda), solo añade
el desglose por wallet que el original no guarda.

Solo lectura.
"""
import json
from collections import Counter

import analisis_ballenas_dosis_respuesta_16jul as dr
from shadow_resolve import fetch_mercados_paralelo, parse_outcome_prices
from smart_money_tracker import trades_de_mercado

COMBO = "SOL#5m"


def cargar_wallet_edge():
    try:
        d = json.load(open("data/shadow/wallet_edge_score_por_activo_marco.json"))
        return {(v["wallet"], v["activo"], v["marco"]): v for v in d.values()}
    except Exception:
        return {}


def main():
    dr.COMBOS = [COMBO]
    bandas = dr.cargar_bandas()
    if COMBO not in bandas:
        print(f"{COMBO} sin banda significativa")
        return
    lo, hi, rl, rh = bandas[COMBO]
    print(f"Banda SOL#5m: precio [{lo},{hi}) ventana [{rl},{rh}]min")

    seleccion = dr.muestrear_mercados({COMBO: bandas[COMBO]})
    cids = seleccion.get(COMBO, [])
    print(f"Muestra: {len(cids)} mercados")

    mapa_cid_mid = dr.mapear_condition_a_market()
    edge_db = cargar_wallet_edge()

    bucket_alto = []   # (cid, pct_mayoria, acierta, wallets_lado_mayoria, top1_share)
    bucket_bajo = []
    for i, cid in enumerate(cids):
        mid = mapa_cid_mid.get(cid)
        if mid is None:
            continue
        resueltos = fetch_mercados_paralelo([mid], workers=1)
        mercado = resueltos.get(mid)
        if not mercado:
            continue
        precios = parse_outcome_prices(mercado.get("outcomePrices"))
        if not precios or len(precios) < 2:
            continue
        try:
            py, pn = float(precios[0]), float(precios[1])
        except (ValueError, TypeError):
            continue
        if abs(py - 1.0) < 0.01:
            outcome_real = "YES"
        elif abs(pn - 1.0) < 0.01:
            outcome_real = "NO"
        else:
            continue

        trades = trades_de_mercado(cid)
        por_wallet_yes = Counter()
        por_wallet_no = Counter()
        for t in trades:
            if (t.get("side") or "").strip().upper() != "BUY":
                continue
            precio_t = t.get("price")
            outcome_t = (t.get("outcome") or "").strip().lower()
            wallet = (t.get("proxyWallet") or "").lower()
            if precio_t is None or outcome_t not in ("up", "down", "yes", "no") or not wallet:
                continue
            try:
                precio_t = float(precio_t)
            except (ValueError, TypeError):
                continue
            if not (lo <= precio_t < hi):
                continue
            if outcome_t in ("up", "yes"):
                por_wallet_yes[wallet] += 1
            else:
                por_wallet_no[wallet] += 1

        n_yes = sum(por_wallet_yes.values())
        n_no = sum(por_wallet_no.values())
        n = n_yes + n_no
        if n < dr.MIN_TRADES_MERCADO:
            continue
        pct_yes = n_yes / n
        lado_mayoria = "YES" if pct_yes >= 0.5 else "NO"
        pct_mayoria = max(pct_yes, 1 - pct_yes)
        acierta = int(lado_mayoria == outcome_real)
        wallets_mayoria = por_wallet_yes if lado_mayoria == "YES" else por_wallet_no
        top1 = max(wallets_mayoria.values()) / sum(wallets_mayoria.values()) if wallets_mayoria else 0

        fila = (cid, pct_mayoria, acierta, dict(wallets_mayoria), top1)
        if pct_mayoria >= 0.9:
            bucket_alto.append(fila)
        elif pct_mayoria < 0.6:
            bucket_bajo.append(fila)

        if (i + 1) % 30 == 0:
            print(f"  {i+1}/{len(cids)} procesados...")

    print(f"\n=== Bucket ALTO [0.9,1.0) -- el que sale mal (16.3% en el hallazgo original) ===")
    print(f"n={len(bucket_alto)}, accuracy={sum(f[2] for f in bucket_alto)/len(bucket_alto)*100:.1f}%" if bucket_alto else "sin datos")
    n_wallets_totales = Counter()
    for cid, pct, acierta, wallets, top1 in bucket_alto:
        n_wallets_totales.update(wallets.keys())
    print(f"top1_share medio (cuánto domina la wallet mayor dentro del lado mayoritario): "
          f"{sum(f[4] for f in bucket_alto)/len(bucket_alto)*100:.1f}%" if bucket_alto else "")
    print(f"wallets distintas involucradas: {len(n_wallets_totales)}")
    print("wallets que más aparecen en el bucket alto (posible dominancia):")
    for w, c in n_wallets_totales.most_common(10):
        edge = edge_db.get((w, "SOL", "5m"))
        edge_str = f"edge_pp={edge['edge_pp']:.1f} sig={edge['sig_bhfdr']}" if edge else "sin score"
        print(f"  {w[:14]}  apariciones={c}  {edge_str}")

    print(f"\n=== Bucket BAJO [0.5,0.6) -- referencia, cerca de coinflip real ===")
    print(f"n={len(bucket_bajo)}, accuracy={sum(f[2] for f in bucket_bajo)/len(bucket_bajo)*100:.1f}%" if bucket_bajo else "sin datos")


if __name__ == "__main__":
    main()
