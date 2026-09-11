#!/usr/bin/env python3
"""
analisis_kalshi_leadlag_movimientos_grandes_25ago.py -- ángulo #2 de
idea_kalshi_leadlag_refutado_primera_pasada_24ago (petición Javi 25-Ago,
"adelante con Kalshi"): la pasada agregada del 24-Ago mezclaba
micro-movimientos sin información con los pocos momentos donde llega
información real nueva -- aquí se repite el MISMO cruce (reusa toda la
carga de datos de analisis_kalshi_leadlag_binance_24ago.py sin duplicar)
pero condicionado a |retorno_chainlink| > percentil90 en cada punto de
la rejilla, para ver si el lead-lag aparece solo en movimientos grandes.

Solo lectura. No promociona nada por sí solo.
"""
import numpy as np
import pandas as pd

from analisis_kalshi_leadlag_binance_24ago import (
    DIR_PRICES, LAGS_S, RESAMPLE_S, cargar_kalshi, cargar_chainlink,
    resamplear_retornos, shuffle_p,
)


def main():
    dias = 6
    print(f"Cargando {dias} días de kalshi_btc15m + chainlink BTC...")
    kal = cargar_kalshi(dias)
    chl = cargar_chainlink(dias)

    inicio = max(kal.index.min(), chl.index.min())
    fin = min(kal.index.max(), chl.index.max())
    rejilla = pd.date_range(inicio, fin, freq=f"{RESAMPLE_S}s", tz="UTC")

    kal_ret = resamplear_retornos(kal["mid"], rejilla)
    rot_ts = set(kal.index[kal["rotacion"]].floor(f"{RESAMPLE_S}s"))
    for ts in rot_ts:
        ventana = pd.date_range(ts, ts + pd.Timedelta(seconds=2), freq=f"{RESAMPLE_S}s", tz="UTC")
        kal_ret.loc[kal_ret.index.isin(ventana)] = np.nan

    chl_ret = resamplear_retornos(chl["price_usd"], rejilla)

    umbral = chl_ret.abs().quantile(0.90)
    print(f"Umbral percentil90 |retorno chainlink| = {umbral:.6f} "
          f"({(chl_ret.abs() > umbral).sum()} puntos de {chl_ret.notna().sum()} no-nulos)")

    print("\n=== SOLO movimientos GRANDES de Chainlink (|ret|>p90 en el punto t+lag) ===")
    print("lag_s | n | corr | p_shuffle")
    resultados = []
    for lag in LAGS_S:
        chl_shift = chl_ret.shift(-lag)
        df = pd.DataFrame({"k": kal_ret, "c": chl_shift}).dropna()
        df = df[df["c"].abs() > umbral]  # condicional al movimiento grande en el chainlink desplazado
        n = len(df)
        if n < 50:
            print(f"{lag:+4d}s | n={n} insuficiente, salto")
            continue
        r = np.corrcoef(df["k"], df["c"])[0, 1]
        if np.isnan(r):
            print(f"{lag:+4d}s | n={n} | r=NaN (varianza cero), salto")
            continue
        p = shuffle_p(df["k"].values, df["c"].values, r) if n < 20000 else shuffle_p(
            df["k"].sample(20000, random_state=1).values, df["c"].sample(20000, random_state=1).values, r)
        resultados.append((lag, n, r, p))
        marca = " <-- " if p < 0.05 else ""
        print(f"{lag:+4d}s | n={n:6d} | r={r:+.4f} | p_shuffle={p:.4f}{marca}")

    if resultados:
        mejor = max(resultados, key=lambda x: abs(x[2]))
        print(f"\nMáxima |correlación|: lag={mejor[0]:+d}s r={mejor[2]:+.4f} n={mejor[1]} p={mejor[3]:.4f}")
        print("Lag positivo = Kalshi PRECEDE a Chainlink (Kalshi lidera).")
        print("Lag negativo = Chainlink precede a Kalshi.")
        sig_pos = [x for x in resultados if x[0] > 0 and x[3] < 0.05]
        print(f"\nLags POSITIVOS significativos (Kalshi lidera): {len(sig_pos)} de {sum(1 for x in resultados if x[0]>0)}")
        for x in sig_pos:
            print(f"  {x[0]:+d}s r={x[2]:+.4f} n={x[1]} p={x[3]:.4f}")


if __name__ == "__main__":
    main()
