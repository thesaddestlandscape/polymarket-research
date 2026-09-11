"""
fetch_binance_klines.py — Fetches 1-min OHLCV klines for crypto assets.

Primary source: Binance public API.
Fallback source: Kraken public REST API (usado cuando Binance falla, p.ej.
HTTP 451 desde runners de CI en datacenters bloqueados por Binance).

Saves to data/binance/klines_YYYY-MM-DD.json as:
{
  "timestamp_utc": "...",
  "BTC": [[open_time_ms, open, high, low, close, volume], ...],
  "ETH": [...],
  ...
}
open_time_ms is Unix milliseconds (consistent with Binance format).

If all sources are unreachable, prints a warning and exits 0.
"""
import csv, json, os, sys, time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import requests

from data_quality import validar_precio, obtener_consensus_spot, DQ_LOG

DIR_PRICES = Path("data") / "prices"
DIR_PRICES.mkdir(parents=True, exist_ok=True)

SPOT_SYMBOLS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]

TIMEOUT = 15
LIMIT   = 25  # number of 1-min candles

# Kraken pair names (XBT = BTC on Kraken)
KRAKEN_PAIRS = {
    "BTC":  "XBTUSD",
    "ETH":  "ETHUSD",
    "SOL":  "SOLUSD",
    "XRP":  "XRPUSD",
    "DOGE": "DOGEUSD",
    "BNB":  "BNBUSD",
}

# Binance symbol names (fallback)
BINANCE_SYMBOLS = {
    "BTC":  "BTCUSDT",
    "ETH":  "ETHUSDT",
    "SOL":  "SOLUSDT",
    "XRP":  "XRPUSDT",
    "DOGE": "DOGEUSDT",
    "BNB":  "BNBUSDT",
}

DIR_BINANCE = Path("data") / "binance"
DIR_BINANCE.mkdir(parents=True, exist_ok=True)

OUTCOMES_5M_PATH = Path("data") / "shadow" / "outcomes_5m_klines.json"
OUTCOMES_5M_RETENCION_H = 48
OUTCOMES_5M_ASSETS = ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB")  # 13-Ago: DOGE/BNB añadidos —
# klines ya se fetchean para los 6 (SPOT_SYMBOLS/KRAKEN_PAIRS), pero esta lista se quedó
# clavada a 4 desde el origen (08-Jul) y dejaba STREAK_MOM_5M/STREAK_FADE_5M#DOGE en estado
# absorbente permanente: _cargar_outcomes_recientes() solo tiene ventanas 5min adyacentes vía
# este store (results.csv por sí solo nunca tiene ventanas consecutivas), así que sin DOGE aquí
# _racha_actual() nunca podía calcular racha y k=0 siempre. Mismo bug ya corregido para 60min en
# _cargar_outcomes_recientes (28-Jul), pendiente en este punto de entrada. Ver
# vigia_candidatas_estancadas.py / candidatas_estancadas.json::candidatos_nunca_genero.


def actualizar_outcomes_5m(data: dict) -> None:
    """Deriva outcomes de ventanas 5min COMPLETAS del snapshot de klines y los
    persiste en OUTCOMES_5M_PATH (rolling 48h, idempotente: una ventana ya
    escrita no se re-escribe aunque un recompute posterior discrepe, p.ej. por
    alternancia Binance↔Kraken).

    Motivo (08-Jul): results.csv solo cubre ventanas 5min cuando alguna
    estrategia predijo (4-14/día, nunca adyacentes) → STREAK_MOM_5M no
    disparaba jamás. shadow_predict._cargar_outcomes_recientes mergea este
    store (el outcome oficial de results.csv gana en conflicto).
    Convención YES=Up si close(última vela) > open(primera vela), validada
    98.6% (n=738, 48h) contra outcome_real oficial en ventanas 15min.
    Cualquier excepción se loguea y NO rompe el fetch.
    """
    try:
        try:
            store = json.loads(OUTCOMES_5M_PATH.read_text())
            if not isinstance(store, dict):
                store = {}
        except Exception:
            store = {}
        paso = 300_000  # 5 min en ms
        ahora_ms = int(time.time() * 1000)
        lim_ms = ahora_ms - OUTCOMES_5M_RETENCION_H * 3_600_000
        cambiado = False
        for asset in OUTCOMES_5M_ASSETS:
            velas = data.get(asset)
            if not (velas and isinstance(velas, list)):
                continue
            por_ts = {}
            for v in velas:
                try:
                    por_ts[int(v[0])] = v
                except (ValueError, TypeError, IndexError):
                    continue
            if not por_ts:
                continue
            outs = store.setdefault(asset, {})
            t_start = -(-min(por_ts) // paso) * paso  # ceil-align a frontera 5min
            while t_start + paso <= ahora_ms:  # solo ventanas cuya última vela ya cerró
                first = por_ts.get(t_start)
                last = por_ts.get(t_start + paso - 60_000)
                if first is None or last is None:
                    t_start += paso
                    continue
                iso = datetime.fromtimestamp((t_start + paso) / 1000,
                                             tz=timezone.utc).isoformat()
                if iso not in outs:
                    try:
                        outs[iso] = "YES" if float(last[4]) > float(first[1]) else "NO"
                        cambiado = True
                    except (ValueError, TypeError, IndexError):
                        pass
                t_start += paso
            for k in list(outs):
                try:
                    if datetime.fromisoformat(k).timestamp() * 1000 < lim_ms:
                        del outs[k]
                        cambiado = True
                except ValueError:
                    del outs[k]
                    cambiado = True
        if cambiado:
            tmp = OUTCOMES_5M_PATH.with_suffix(".json.tmp")
            tmp.write_text(json.dumps(store, separators=(",", ":")))
            os.replace(tmp, OUTCOMES_5M_PATH)
    except Exception as e:
        print(f"  [WARN] actualizar_outcomes_5m falló (no bloquea fetch): {e}")


def fetch_kraken(asset: str) -> list | None:
    """Fetch last LIMIT 1-min candles from Kraken. Returns [[open_time_ms, o, h, l, c, v], ...]."""
    pair = KRAKEN_PAIRS.get(asset)
    if not pair:
        return None
    try:
        # Kraken OHLC: since = now - LIMIT minutes
        since = int(time.time()) - LIMIT * 60
        r = requests.get(
            "https://api.kraken.com/0/public/OHLC",
            params={"pair": pair, "interval": 1, "since": since},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        body = r.json()
        if body.get("error"):
            print(f"  [WARN] Kraken error for {asset}: {body['error']}", file=sys.stderr)
            return None
        result = body.get("result", {})
        # Kraken returns the pair key (sometimes with X/Z prefix). Take first non-"last" key.
        candle_key = next((k for k in result if k != "last"), None)
        if not candle_key:
            return None
        candles = result[candle_key][-LIMIT:]  # take last LIMIT candles
        # Kraken format: [time_sec, open, high, low, close, vwap, volume, count]
        # Convert to Binance-compatible: [open_time_ms, open, high, low, close, volume]
        return [[c[0] * 1000, c[1], c[2], c[3], c[4], c[6]] for c in candles]
    except Exception as e:
        print(f"  [WARN] Kraken error for {asset}: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def fetch_binance(asset: str, with_flow: bool = False) -> list | None:
    """Fetch last LIMIT 1-min klines from Binance.
    with_flow=True → devuelve 7 columnas: [time_ms, o, h, l, c, vol, taker_buy_vol]
    with_flow=False → 6 columnas compatibles con Kraken.
    """
    symbol = BINANCE_SYMBOLS.get(asset)
    if not symbol:
        return None
    try:
        r = requests.get(
            "https://api.binance.com/api/v3/klines",
            params={"symbol": symbol, "interval": "1m", "limit": LIMIT},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        raw = r.json()
        if with_flow:
            # col 9: taker_buy_base_asset_volume
            return [[k[0], k[1], k[2], k[3], k[4], k[5], k[9]] for k in raw]
        return [[k[0], k[1], k[2], k[3], k[4], k[5]] for k in raw]
    except Exception as e:
        print(f"  [WARN] Binance error for {asset}: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def fetch_session_vwap(asset: str) -> float | None:
    """VWAP de la sesión UTC (ancla 00:00) desde klines 1min Binance, ponderada
    por volumen. Feature dist_vwap_pct (shadow-only). Fetch aparte porque el
    principal solo trae LIMIT=25 velas; aquí startTime=00:00 UTC hoy, limit=1500
    (día completo = 1440 velas < 1500 → una sola llamada cubre la sesión).
    Solo Binance: Kraken devuelve semántica de volumen distinta → fail-closed
    (sin VWAP la feature no se añade y la predicción sigue igual)."""
    symbol = BINANCE_SYMBOLS.get(asset)
    if not symbol:
        return None
    try:
        now = datetime.now(timezone.utc)
        inicio_ms = int(now.replace(hour=0, minute=0, second=0,
                                    microsecond=0).timestamp() * 1000)
        r = requests.get(
            "https://api.binance.com/api/v3/klines",
            params={"symbol": symbol, "interval": "1m",
                    "startTime": inicio_ms, "limit": 1500},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        num = den = 0.0
        for k in r.json():
            # típico = (high+low+close)/3, peso = volumen base (col 5)
            typ = (float(k[2]) + float(k[3]) + float(k[4])) / 3.0
            v = float(k[5])
            num += typ * v
            den += v
        if den <= 0:
            return None
        return round(num / den, 6)
    except Exception as e:
        print(f"  [WARN] session VWAP {asset}: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def fetch_volume_regimen(asset: str, horas_lookback: int = 3, minutos_ventana: int = 20) -> float | None:
    """Ratio de volumen reciente vs línea base (10-Jul, propuesta #5 libro
    Shannon "multiple timeframes"): volumen de los últimos `minutos_ventana`
    (misma ventana que drift_20min_pct/ibs_20min) dividido entre el volumen
    medio por bloque equivalente en las últimas `horas_lookback` horas.
    >1 = actividad reciente elevada vs el propio histórico corto del activo;
    <1 = diminuida. Llamada dedicada (mismo patrón que fetch_session_vwap) —
    NO reusa el snapshot de 25 velas del fetch principal (insuficiente
    profundidad para una línea base de horas). Fail-closed: cualquier fallo
    devuelve None y la feature no se añade (no rompe nada aguas abajo)."""
    symbol = BINANCE_SYMBOLS.get(asset)
    if not symbol:
        return None
    try:
        now = datetime.now(timezone.utc)
        inicio_ms = int((now.timestamp() - horas_lookback * 3600) * 1000)
        r = requests.get(
            "https://api.binance.com/api/v3/klines",
            params={"symbol": symbol, "interval": "1m",
                    "startTime": inicio_ms, "limit": 1000},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        velas = r.json()
        if len(velas) < minutos_ventana * 2:
            return None  # histórico insuficiente para una línea base fiable
        vol_reciente = sum(float(k[5]) for k in velas[-minutos_ventana:])
        vol_total = sum(float(k[5]) for k in velas)
        n_bloques = len(velas) / minutos_ventana
        vol_base_por_bloque = vol_total / n_bloques if n_bloques > 0 else 0
        if vol_base_por_bloque <= 0:
            return None
        return round(vol_reciente / vol_base_por_bloque, 4)
    except Exception as e:
        print(f"  [WARN] volume regimen {asset}: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def fetch_volume_patron(asset: str, minutos_ventana: int = 20, n_bloques: int = 4) -> dict | None:
    """Forma del volumen reciente, no solo su nivel (12-Ago, pendiente
    project_pendiente_detectar_spikes_volumen_12ago -- petición Javi: el
    ratio simple de fetch_volume_regimen no separó señal en agregado sobre
    GBM_LATE_15M#BUY_YES, hipótesis de que mezcla patrones cualitativamente
    distintos -- creciente sostenido vs plano vs spike puntual -- que un
    solo número no distingue). Reparte `minutos_ventana` en `n_bloques`
    bloques iguales y calcula:
      - pendiente_norm: pendiente de regresión lineal de los bloques (0..
        n_bloques-1) normalizada por su media -- positivo=creciente,
        negativo=decreciente, cerca de 0=plano.
      - spike_ratio: volumen del bloque máximo / mediana de los demás --
        alto = un solo bloque domina (actividad climática puntual).

    Prototipo verificado 12-Ago (analisis_taxonomia_volumen_12ago.py, n=318
    post-TWAP GBM_LATE_15M#BUY_YES): agrupando creciente+plano vs
    decreciente+spike, hit=79.1% vs 70.0% (gap 9.1pp, p_shuffle=0.072 --
    prometedor, NO confirmado todavía, dejar crecer n). Se loguean los 2
    valores CRUDOS (no la clasificación categórica ya decidida) para que
    el pipeline causal (FEATURE_RULES, shadow_postmortem.py) descubra el
    umbral real con más datos, mismo criterio que el resto del proyecto
    (sigma_ewma_delta_pct, volumen_regimen) -- no precocinar la respuesta.

    Llamada dedicada (no reusa fetch_volume_regimen, que solo cubre 4
    activos) -- cubre los 6 activos de GBM_LATE_15M. Fail-closed: None en
    cualquier fallo, la feature simplemente no se loguea ese ciclo."""
    symbol = BINANCE_SYMBOLS.get(asset)
    if not symbol:
        return None
    try:
        now = datetime.now(timezone.utc)
        inicio_ms = int((now.timestamp() - minutos_ventana * 60) * 1000)
        r = requests.get(
            "https://api.binance.com/api/v3/klines",
            params={"symbol": symbol, "interval": "1m",
                    "startTime": inicio_ms, "limit": minutos_ventana + 2},
            timeout=TIMEOUT,
        )
        r.raise_for_status()
        velas = r.json()
        if len(velas) < minutos_ventana - 2:
            return None
        vols = [float(k[5]) for k in velas[-minutos_ventana:]]
        if len(vols) < minutos_ventana:
            return None
        min_por_bloque = minutos_ventana // n_bloques
        bloques = [sum(vols[i:i + min_por_bloque]) for i in range(0, minutos_ventana, min_por_bloque)]
        bloques = bloques[:n_bloques]
        if len(bloques) != n_bloques or any(b <= 0 for b in bloques):
            return None

        import numpy as np
        x = np.arange(n_bloques)
        y = np.array(bloques, dtype=np.float64)
        media = y.mean()
        pendiente = np.polyfit(x, y, 1)[0]
        pendiente_norm = pendiente / media if media > 0 else 0.0

        idx_max = int(np.argmax(y))
        otros = np.delete(y, idx_max)
        mediana_otros = float(np.median(otros)) if len(otros) else 0.0
        spike_ratio = (y[idx_max] / mediana_otros) if mediana_otros > 0 else 10.0

        return {"pendiente_norm": round(float(pendiente_norm), 4),
                "spike_ratio": round(float(spike_ratio), 4)}
    except Exception as e:
        print(f"  [WARN] volume patron {asset}: {type(e).__name__}: {e}", file=sys.stderr)
        return None


def _log_evento_fuente(sym: str, fuente_prev: str, fuente_nueva: str, salto_pct: float) -> None:
    """Deja constancia en dq_events.jsonl (mismo log que L1) de un cambio de
    fuente de precio para un activo, con el salto de precio asociado — antes
    no había ninguna forma de auditar retroactivamente cuándo pasaba esto."""
    try:
        DQ_LOG.parent.mkdir(parents=True, exist_ok=True)
        evento = {
            "ts": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "sym": sym.upper(),
            "value": round(salto_pct, 4),
            "reason": f"cambio_fuente {fuente_prev}->{fuente_nueva}",
        }
        with open(DQ_LOG, "a", encoding="utf-8") as f:
            f.write(json.dumps(evento, ensure_ascii=False) + "\n")
    except Exception:
        pass


def main():
    now_utc = datetime.now(timezone.utc)
    ts_str  = now_utc.isoformat(timespec="seconds")
    fecha   = now_utc.strftime("%Y-%m-%d")
    print(f"[{ts_str}] Fetching 1-min klines (Binance primary, Kraken fallback)...")

    data = {"timestamp_utc": ts_str}
    any_success = False
    fuente_por_symbol: dict[str, str] = {}

    def _fetch_asset(asset):
        klines = fetch_binance(asset, with_flow=True)
        source = "Binance+flow"
        if klines is None:
            klines = fetch_kraken(asset)
            source = "Kraken"
        return asset, klines, source

    with ThreadPoolExecutor(max_workers=len(KRAKEN_PAIRS)) as ex:
        for asset, klines, source in ex.map(_fetch_asset, list(KRAKEN_PAIRS)):
            if klines is not None:
                data[asset] = klines
                any_success = True
                fuente_por_symbol[asset] = "kraken" if source == "Kraken" else "binance"
                has_flow = len(klines[0]) >= 7 if klines else False
                print(f"  {asset}: {len(klines)} klines OK [{source}{'  ✓flow' if has_flow else ''}]")
            else:
                print(f"  {asset}: SKIP (both sources failed)")

    if not any_success:
        print("[WARN] No klines fetched — all sources unreachable. Exiting 0.")
        sys.exit(0)

    # VWAP de sesión (ancla 00:00 UTC) para dist_vwap_pct — solo activos GBM.
    # Se añade al mismo JSON; shadow_predict lo lee. Fail-closed: si algún fetch
    # falla, ese activo no entra y su feature no se loguea (no rompe nada).
    vwaps = {}
    for _asset in ("BTC", "ETH", "SOL", "XRP"):
        _v = fetch_session_vwap(_asset)
        if _v is not None:
            vwaps[_asset] = _v
    if vwaps:
        data["vwap"] = vwaps
        print(f"  VWAP sesión: {{{', '.join(f'{k}={v:.4g}' for k, v in vwaps.items())}}}")

    # Régimen de volumen (10-Jul, propuesta #5) — mismo patrón fail-closed
    # que vwaps arriba. Llamada dedicada, no reusa el snapshot principal.
    vol_regimen = {}
    for _asset in ("BTC", "ETH", "SOL", "XRP"):
        _vr = fetch_volume_regimen(_asset)
        if _vr is not None:
            vol_regimen[_asset] = _vr
    if vol_regimen:
        data["volumen_regimen"] = vol_regimen
        print(f"  Volumen régimen: {{{', '.join(f'{k}={v:.2f}x' for k, v in vol_regimen.items())}}}")

    # Forma del volumen (12-Ago) — mismo patrón fail-closed, 6 activos
    # (GBM_LATE_15M cubre los 6, a diferencia de volumen_regimen arriba
    # que solo cubre 4).
    vol_patron = {}
    for _asset in ("BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"):
        _vp = fetch_volume_patron(_asset)
        if _vp is not None:
            vol_patron[_asset] = _vp
    if vol_patron:
        data["volumen_patron"] = vol_patron
        _resumen_vp = ", ".join(
            f"{k}=pend{v['pendiente_norm']:+.2f}/spike{v['spike_ratio']:.1f}x"
            for k, v in vol_patron.items()
        )
        print(f"  Volumen patrón: {{{_resumen_vp}}}")

    out_path = DIR_BINANCE / f"klines_{fecha}.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, separators=(",", ":"))
    print(f"  Saved -> {out_path}")

    actualizar_outcomes_5m(data)

    # Escribir spot price (close de última vela) en prices CSV cada 60s
    # Solo si el archivo ya existe (capture_markets lo crea con el header completo)
    # Kraken/Binance reemplaza la dependencia de CoinGecko free tier para los 6 activos principales
    prices_path = DIR_PRICES / f"{fecha}.csv"
    tiene_col_source = False
    if not prices_path.exists():
        # Crear el archivo con header si no existe (no depender de capture_markets).
        # Incluye "source" (binance/kraken/consenso) desde el primer momento —
        # antes no había forma de saber retroactivamente qué fila venía de qué
        # exchange, y el fallback Binance↔Kraken alterna varias veces al día
        # (desfase típico 0.1-1% entre exchanges, suficiente para invertir el
        # signo de un drift_15min/60min si cae justo en el cambio de fuente).
        with open(prices_path, "w", newline="", encoding="utf-8") as pf:
            csv.writer(pf).writerow(["timestamp_utc", "asset", "price_usd", "change_1h_pct", "change_24h_pct", "source"])
        tiene_col_source = True
    else:
        with open(prices_path, encoding="utf-8") as pf:
            tiene_col_source = "source" in (pf.readline().strip().split(","))

    # Leer último precio Y fuente de cada asset en una sola pasada (para
    # detección de spikes en L1 y de cambios de fuente en la misma línea).
    last_prices: dict[str, float | None] = {}
    last_sources: dict[str, str | None] = {}
    try:
        with open(prices_path, encoding="utf-8") as pf:
            for row in csv.DictReader(pf):
                sym = (row.get("asset") or "").strip().upper()
                if sym not in SPOT_SYMBOLS:
                    continue
                try:
                    last_prices[sym] = float(row["price_usd"])
                except (KeyError, ValueError, TypeError):
                    continue
                last_sources[sym] = row.get("source") or None
    except Exception:
        pass

    # L1: extraer y validar precios desde klines
    binance_prices: dict[str, float] = {}
    for sym in SPOT_SYMBOLS:
        klines_sym = data.get(sym)
        if not (klines_sym and isinstance(klines_sym, list)):
            continue
        try:
            price = float(klines_sym[-1][4])
        except (IndexError, ValueError, TypeError):
            continue
        ok, motivo = validar_precio(sym, price, last_prices.get(sym))
        if not ok:
            print(f"  [DQ L1] {sym} RECHAZADO ({motivo})")
            continue
        binance_prices[sym] = price

    # L4: cross-source consensus (Binance vs Coinbase vs Kraken)
    # TTL 5min: solo hace peticiones externas cuando el cache está stale.
    # Coinbase = settlement reference para BTC/ETH en Polymarket.
    assets_gbm  = ["BTC", "ETH", "SOL", "XRP"]
    binance_gbm = {k: v for k, v in binance_prices.items() if k in assets_gbm}
    if binance_gbm:
        try:
            consensus = obtener_consensus_spot(binance_gbm, assets_gbm, timeout=4)
            cross     = consensus.get("cross", {})
            cached    = consensus.get("cached", False)
            if not cached and cross.get("alertas"):
                for a in cross["alertas"]:
                    icon = "🚨" if a["accion"] == "BLOQUEADO" else "⚠️"
                    print(f"  [DQ L4] {icon} {a['sym']} div={a['max_div_pct']:.2f}% ({'cache' if cached else 'fresco'})")
            for sym, px_consenso in consensus.get("precios", {}).items():
                if sym in binance_prices:
                    binance_prices[sym] = px_consenso
                    fuente_por_symbol[sym] = "consenso"
        except Exception as _cs_err:
            print(f"  [DQ L4] Cross-source error (no bloqueante): {_cs_err}")

    if binance_prices:
        with open(prices_path, "a", newline="", encoding="utf-8") as pf:
            w = csv.writer(pf)
            for sym, price in binance_prices.items():
                fuente = fuente_por_symbol.get(sym, "")
                # Cambio de fuente respecto a la fila anterior de este activo
                # (ej. Binance→Kraken por un fallo puntual): el desfase típico
                # entre exchanges (0.1-1%) puede leerse como movimiento real.
                # Solo se deja constancia en dq_events.jsonl (no bloqueante) —
                # antes no había ninguna forma de saber que esto pasaba.
                fuente_prev = last_sources.get(sym)
                if fuente and fuente_prev and fuente_prev not in (fuente, "consenso") and fuente != "consenso":
                    prev_p = last_prices.get(sym)
                    salto = abs(price / prev_p - 1) * 100 if prev_p else 0.0
                    print(f"  [DQ] {sym} cambio de fuente {fuente_prev}→{fuente} (salto {salto:.3f}%)")
                    _log_evento_fuente(sym, fuente_prev, fuente, salto)
                fila = [ts_str, sym, price, "", ""]
                if tiene_col_source:
                    fila.append(fuente)
                w.writerow(fila)
        btc = binance_prices.get('BTC','?')
        eth = binance_prices.get('ETH','?')
        sol = binance_prices.get('SOL','?')
        print(f"  Spot → prices/{fecha}.csv  BTC={btc} ETH={eth} SOL={sol}")

    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] Done.")


if __name__ == "__main__":
    main()
