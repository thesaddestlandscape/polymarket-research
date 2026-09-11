#!/usr/bin/env python3
"""
analisis_kalshi_hourly_leadlag_25ago.py -- ángulo #3 de
idea_kalshi_leadlag_refutado_primera_pasada_24ago (petición Javi 25-Ago,
"adelante con Kalshi"): en vez del mid-price de un mercado direccional
(KXBTC15M, ya probado), deriva un PRECIO implícito de BTC de la escalera
completa de strikes horaria (KXBTCD, ~100 strikes/hora) -- el strike
donde yes_bid cruza 0.5 (interpolado linealmente entre los dos strikes
más cercanos) es la mediana implícita de la distribución de precio del
mercado en ese instante. Se compara el RETORNO de ese precio implícito
contra el RETORNO de Chainlink, mismos lags -10s..+30s que el ángulo
original.

Solo lectura. No promociona nada por sí solo.
"""
from pathlib import Path

import numpy as np
import pandas as pd

from analisis_kalshi_leadlag_binance_24ago import (
    DIR_PRICES, LAGS_S, RESAMPLE_S, cargar_chainlink, resamplear_retornos, shuffle_p,
)


def cargar_kalshi_hourly_implicito(dias: int) -> pd.Series:
    import glob
    archivos = sorted(glob.glob(str(DIR_PRICES / "kalshi_btchourly_*.csv")))[-dias:]
    dfs = []
    for f in archivos:
        df = pd.read_csv(f, usecols=["timestamp_utc", "event_ticker", "floor_strike", "yes_bid"])
        dfs.append(df)
    df = pd.concat(dfs, ignore_index=True)
    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True, errors="coerce")
    df = df.dropna(subset=["timestamp_utc", "floor_strike", "yes_bid"])
    # redondea a la rejilla de captura (cada ~3s) para agrupar snapshots de
    # la MISMA pasada de la escalera -- distintos strikes de un mismo evento
    # se escriben en el mismo segundo/los mismos pocos segundos
    df["ts_bucket"] = df["timestamp_utc"].dt.floor(f"{RESAMPLE_S}s")

    # 25-Ago (fix de rendimiento -- el groupby con Python-level loop/mode()
    # sobre ~4.7M filas tardaba >280s sin terminar): se queda con el evento
    # de MÁS VOLUMEN por (ts_bucket) de forma vectorizada (sin loop Python),
    # y dentro de eso usa numpy puro (sort_values + searchsorted vectorizado
    # por grupo vía groupby.apply, pero solo sobre el subconjunto ya
    # reducido a 1 evento por bucket -- muchos menos grupos).
    vol_por_ts_evt = df.groupby(["ts_bucket", "event_ticker"])["yes_bid"].transform("size")
    df = df.assign(_vol=vol_por_ts_evt)
    idx_max = df.groupby("ts_bucket")["_vol"].idxmax()
    evt_dominante = df.loc[idx_max, ["ts_bucket", "event_ticker"]].set_index("ts_bucket")["event_ticker"]
    df = df.merge(evt_dominante.rename("evt_dom"), on="ts_bucket")
    df = df[df["event_ticker"] == df["evt_dom"]]

    def _cruce(g):
        g = g.sort_values("floor_strike")
        strikes = g["floor_strike"].to_numpy()
        bids = g["yes_bid"].to_numpy()
        if len(strikes) < 3:
            return np.nan
        idx = np.searchsorted(-bids, -0.5)
        if idx <= 0 or idx >= len(bids):
            return np.nan
        b1, b0 = bids[idx - 1], bids[idx]
        s1, s0 = strikes[idx - 1], strikes[idx]
        if b1 == b0:
            return np.nan
        frac = (b1 - 0.5) / (b1 - b0)
        return s1 + frac * (s0 - s1)

    precios = df.groupby("ts_bucket").apply(_cruce, include_groups=False)
    precios = precios.dropna()
    precios.index.name = "ts"
    return precios


def main():
    dias = 6
    print(f"Cargando {dias} días de kalshi_btchourly (precio implícito) + chainlink BTC...")
    kal_precio = cargar_kalshi_hourly_implicito(dias)
    chl = cargar_chainlink(dias)
    print(f"kalshi precio implícito: {len(kal_precio)} puntos ({kal_precio.index.min()} -> {kal_precio.index.max()})")
    print(f"chainlink: {len(chl)} filas")

    inicio = max(kal_precio.index.min(), chl.index.min())
    fin = min(kal_precio.index.max(), chl.index.max())
    rejilla = pd.date_range(inicio, fin, freq=f"{RESAMPLE_S}s", tz="UTC")
    print(f"rejilla común 1s: {len(rejilla)} puntos ({inicio} -> {fin})")

    kal_ret = resamplear_retornos(kal_precio, rejilla)
    chl_ret = resamplear_retornos(chl["price_usd"], rejilla)
    print(f"kalshi_ret no-nulos: {kal_ret.notna().sum()}, chainlink_ret no-nulos: {chl_ret.notna().sum()}")

    print("\nlag_s | n | corr(kalshi_implicito_ret[t], chainlink_ret[t+lag]) | shuffle_p")
    resultados = []
    for lag in LAGS_S:
        chl_shift = chl_ret.shift(-lag)
        df = pd.DataFrame({"k": kal_ret, "c": chl_shift}).dropna()
        df = df[(df["k"] != 0) | (df["c"] != 0)]
        n = len(df)
        if n < 50:
            print(f"{lag:+4d}s | n={n} insuficiente, salto")
            continue
        r = np.corrcoef(df["k"], df["c"])[0, 1]
        if np.isnan(r):
            continue
        p = shuffle_p(df["k"].values, df["c"].values, r) if n < 20000 else shuffle_p(
            df["k"].sample(20000, random_state=1).values, df["c"].sample(20000, random_state=1).values, r)
        resultados.append((lag, n, r, p))
        marca = " <-- " if p < 0.05 else ""
        print(f"{lag:+4d}s | n={n:6d} | r={r:+.4f} | p_shuffle={p:.4f}{marca}")

    if resultados:
        mejor = max(resultados, key=lambda x: abs(x[2]))
        print(f"\nMáxima |correlación|: lag={mejor[0]:+d}s r={mejor[2]:+.4f} n={mejor[1]} p={mejor[3]:.4f}")
        sig_pos = [x for x in resultados if x[0] > 0 and x[3] < 0.05]
        print(f"Lags POSITIVOS significativos (Kalshi lidera): {len(sig_pos)} de {sum(1 for x in resultados if x[0]>0)}")
        for x in sig_pos:
            print(f"  {x[0]:+d}s r={x[2]:+.4f} n={x[1]} p={x[3]:.4f}")


if __name__ == "__main__":
    main()
