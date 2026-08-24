#!/usr/bin/env python3
"""
analisis_kalshi_leadlag_binance_24ago.py — 24-Ago, petición explícita Javi
("tienes que arrancar el análisis, ya tenemos datos suficientes").

Hallazgo externo que motiva esto (SynthData, ver CLAUDE.md screen "chainlink"
19-Ago): Kalshi lidera a Binance spot en la ventana 0-10s tras un movimiento,
correlación creciente 0.036->0.173 en 2026. `fetch_kalshi_btc.py` lleva
capturando desde el 19-Ago (6 días, KXBTC15M cada 2s) sin que nadie lo
analizara todavía -- este script es la primera pasada.

Metodología: el mercado KXBTC15M es un mercado DIRECCIONAL (arriba/abajo en
la ventana de 15min actual), no un precio de BTC -- su mid-price (yes_bid+
yes_ask)/2 es la probabilidad implícita de que BTC suba. Se compara el
RETORNO de esa probabilidad implícita contra el RETORNO del precio Chainlink
(fuente de resolución oficial de Polymarket) en la MISMA ventana, desplazado
lag segundos -- si Kalshi lidera, la correlación debe ser mayor en lag>0
(el movimiento de Kalshi de HOY predice el movimiento de Chainlink de
DENTRO de `lag` segundos) que en lag=0 o lag<0.

Sin scipy disponible en el venv -- correlación de Pearson manual con numpy
(np.corrcoef), sin p-valor paramétrico; se complementa con shuffle test
(mismo criterio que gate_bucket_propio.py) para significancia.

Uso: python3 analisis_kalshi_leadlag_binance_24ago.py [--dias N]
"""
import argparse
import glob
from pathlib import Path

import numpy as np
import pandas as pd

DIR_PRICES = Path(__file__).parent / "data" / "prices"
LAGS_S = list(range(-10, 31, 1))  # -10s..+30s, positivo = kalshi lidera
RESAMPLE_S = 1  # rejilla común de 1s
N_SHUFFLES = 500


def cargar_kalshi(dias: int) -> pd.DataFrame:
    archivos = sorted(glob.glob(str(DIR_PRICES / "kalshi_btc15m_*.csv")))[-dias:]
    dfs = []
    for f in archivos:
        df = pd.read_csv(f, usecols=["timestamp_utc", "ticker", "yes_bid", "yes_ask"])
        dfs.append(df)
    df = pd.concat(dfs, ignore_index=True)
    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True, errors="coerce")
    df = df.dropna(subset=["timestamp_utc"])
    df["mid"] = (df["yes_bid"] + df["yes_ask"]) / 2.0
    # cuando el mercado rota (nuevo ticker), el "salto" de mid no es movimiento
    # real de probabilidad -- se descarta el primer tick de cada ticker nuevo
    df = df.sort_values("timestamp_utc")
    df["ticker_prev"] = df["ticker"].shift(1)
    df["rotacion"] = df["ticker"] != df["ticker_prev"]
    return df[["timestamp_utc", "mid", "rotacion"]].set_index("timestamp_utc")


def cargar_chainlink(dias: int) -> pd.DataFrame:
    archivos = sorted(glob.glob(str(DIR_PRICES / "chainlink_*.csv")))[-dias:]
    dfs = []
    for f in archivos:
        df = pd.read_csv(f, usecols=["timestamp_utc", "asset", "price_usd"])
        dfs.append(df[df["asset"] == "BTC"])
    df = pd.concat(dfs, ignore_index=True)
    df["timestamp_utc"] = pd.to_datetime(df["timestamp_utc"], utc=True, errors="coerce")
    df = df.dropna(subset=["timestamp_utc"]).sort_values("timestamp_utc")
    return df[["timestamp_utc", "price_usd"]].set_index("timestamp_utc")


def resamplear_retornos(serie: pd.Series, rejilla: pd.DatetimeIndex) -> pd.Series:
    """Forward-fill sobre rejilla común de 1s, log-retorno por paso.
    24-Ago (bug real cazado en el primer run): mid=0 antes del primer tick
    real (huecos de arranque) da log(0)=-inf -> toda la matriz de
    correlación sale NaN. Filtrar valores no positivos ANTES del ffill."""
    s = serie[~serie.index.duplicated(keep="last")]
    s = s[s > 0]
    s = s.reindex(s.index.union(rejilla)).ffill().reindex(rejilla)
    s = s[s > 0]
    ret = np.log(s).diff()
    return ret.replace([np.inf, -np.inf], np.nan)


def shuffle_p(x: np.ndarray, y: np.ndarray, r_obs: float, n: int = N_SHUFFLES) -> float:
    rng = np.random.default_rng(42)
    count = 0
    for _ in range(n):
        yp = rng.permutation(y)
        r = np.corrcoef(x, yp)[0, 1]
        if abs(r) >= abs(r_obs):
            count += 1
    return count / n


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=6)
    args = ap.parse_args()

    print(f"Cargando {args.dias} días de kalshi_btc15m + chainlink BTC...")
    kal = cargar_kalshi(args.dias)
    chl = cargar_chainlink(args.dias)
    print(f"kalshi: {len(kal)} filas ({kal.index.min()} -> {kal.index.max()})")
    print(f"chainlink: {len(chl)} filas ({chl.index.min()} -> {chl.index.max()})")

    inicio = max(kal.index.min(), chl.index.min())
    fin = min(kal.index.max(), chl.index.max())
    rejilla = pd.date_range(inicio, fin, freq=f"{RESAMPLE_S}s", tz="UTC")
    print(f"rejilla común 1s: {len(rejilla)} puntos ({inicio} -> {fin})")

    kal_mid = kal["mid"]
    kal_ret = resamplear_retornos(kal_mid, rejilla)

    # marcar como NaN los retornos que cruzan una rotación de mercado (ruido,
    # no movimiento real de probabilidad direccional)
    rot_ts = set(kal.index[kal["rotacion"]].floor(f"{RESAMPLE_S}s"))
    for ts in rot_ts:
        ventana = pd.date_range(ts, ts + pd.Timedelta(seconds=2), freq=f"{RESAMPLE_S}s", tz="UTC")
        kal_ret.loc[kal_ret.index.isin(ventana)] = np.nan

    chl_px = chl["price_usd"]
    chl_ret = resamplear_retornos(chl_px, rejilla)

    print(f"\nkalshi_ret no-nulos: {kal_ret.notna().sum()}, chainlink_ret no-nulos: {chl_ret.notna().sum()}")
    print("\nlag_s | n | corr(kalshi_ret[t], chainlink_ret[t+lag]) | shuffle_p")
    resultados = []
    for lag in LAGS_S:
        chl_shift = chl_ret.shift(-lag)  # chainlink en t+lag alineado a t
        df = pd.DataFrame({"k": kal_ret, "c": chl_shift}).dropna()
        # descartar retornos cero-cero (ambos mercados sin tick nuevo, infla corr espuria)
        df = df[(df["k"] != 0) | (df["c"] != 0)]
        n = len(df)
        if n < 50:
            print(f"{lag:+4d}s | n={n} insuficiente, salto")
            continue
        r = np.corrcoef(df["k"], df["c"])[0, 1]
        p = shuffle_p(df["k"].values, df["c"].values, r) if n < 20000 else shuffle_p(
            df["k"].sample(20000, random_state=1).values, df["c"].sample(20000, random_state=1).values, r)
        resultados.append((lag, n, r, p))
        marca = " <-- " if p < 0.05 else ""
        print(f"{lag:+4d}s | n={n:6d} | r={r:+.4f} | p_shuffle={p:.4f}{marca}")

    if resultados:
        mejor = max(resultados, key=lambda x: abs(x[2]))
        print(f"\nMáxima |correlación|: lag={mejor[0]:+d}s r={mejor[2]:+.4f} n={mejor[1]} p={mejor[3]:.4f}")
        print("Lag positivo = movimiento de Kalshi PRECEDE al de Chainlink (Kalshi lidera).")
        print("Lag negativo = Chainlink precede a Kalshi (Kalshi va por detrás).")


if __name__ == "__main__":
    main()
