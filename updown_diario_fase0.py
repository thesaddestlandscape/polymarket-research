#!/usr/bin/env python3
"""updown_diario_fase0.py -- FASE 0, SOLO OBSERVACIÓN: mercados "X Up or Down on <fecha>" (ronda 1 #5).

Regla de resolución (gamma, verificada 30-Sep): Up si el cierre de la vela de 1 min de Binance
X/USDT de las 12:00 ET de hoy es mayor que el de la vela de las 12:00 ET de ayer. La referencia
se conoce exacta desde el día anterior y el subyacente es Binance spot (sin oráculo intermedio).
Volumen por mercado (8-29 Sep, 87 mercados BTC/ETH/SOL/XRP): mediana 22k $, media 64k $.
Retrospectivo con precio MEDIO por minuto: n por tramo demasiado pequeño para concluir.

Qué captura (cron cada minuto; solo actúa en las 2 h previas al cierre y 3 min después):
spot de Binance, referencia, volatilidad de 1 min, z = ln(S/ref)/(sigma*sqrt(min restantes)),
probabilidad justa Phi(z) y el libro REAL de ambos lados (mejor bid/ask y USD hasta ask+1c).
Salida: data/shadow/updown_diario_fase0_v2.csv (≈500 filas/día; v1 congelado hasta 18-Nov). Sin órdenes.
CAMBIO DE PLATAFORMA (mercado del 19-Nov-2026 en adelante): slug "{coin}-updown-1d-{cierre-24h}" y regla
TWAP60 Chainlink de las 12:00 ET de hoy >= el de ayer (empate = Up). Para esa regla ref y proyección salen
de la MISMA fuente: PolyBolt canal twap60 (data/prices/polybolt_*.csv, event_ts_ms del segundo exacto);
sigma sigue siendo la de 1 min de Binance (aprox.). Columna `regla` separa ambos regímenes.
Gate para pensar en ejecutor: n>=40 mercados, >=10 días, EV al ask real >= +0,10 con IC90 por
días >0 en una celda definida ANTES de mirar (p. ej. valor = Phi(z) - ask >= 0,10 a T-10 min).
"""
import csv
import json
import math
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
OUT = REPO / "data" / "shadow" / "updown_diario_fase0_v2.csv"
PRICES = REPO / "data" / "prices"
REF_CACHE = REPO / "data" / "shadow" / "updown_diario_ref_twap_cache.json"
COIN = {"bitcoin": "btc", "ethereum": "eth", "solana": "sol", "xrp": "xrp", "dogecoin": "doge", "bnb": "bnb"}
GAMMA = "https://gamma-api.polymarket.com"
CLOB_BOOK = "https://clob.polymarket.com/book"
BINANCE = "https://api.binance.com/api/v3"
ACTIVOS = {"bitcoin": "BTCUSDT", "ethereum": "ETHUSDT", "solana": "SOLUSDT", "xrp": "XRPUSDT",
           "dogecoin": "DOGEUSDT", "bnb": "BNBUSDT"}
MESES = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
         "october", "november", "december"]
VENTANA_ANTES_MIN, VENTANA_DESPUES_MIN = 120, 3
COLS = ["ts_utc", "activo", "slug", "market_id", "min_restantes", "spot", "ref", "sigma_1m", "z", "prob_justa_up",
        "ask_up", "bid_up", "usd_ask_up", "ask_down", "bid_down", "usd_ask_down", "lat_ms", "error",
        "regla", "spot_edad_s"]
_S = requests.Session()


def _phi(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def _libro(token: str):
    r = _S.get(CLOB_BOOK, params={"token_id": token}, timeout=6)
    r.raise_for_status()
    j = r.json()
    asks = sorted((float(a["price"]), float(a["size"])) for a in (j.get("asks") or []))
    bids = sorted(((float(b["price"]), float(b["size"])) for b in (j.get("bids") or [])), reverse=True)
    ask = asks[0][0] if asks else None
    usd = round(sum(p * s for p, s in asks if p <= ask + 0.01), 2) if asks else 0.0
    return ask, (bids[0][0] if bids else None), usd


def _mercado(nombre: str, dia: datetime):
    """Mercado diario con cierre a las 12:00 ET de `dia`; exige endDate EXACTO (un slug sin año trae el de 2025)."""
    from zoneinfo import ZoneInfo
    fin = int(datetime(dia.year, dia.month, dia.day, 12, tzinfo=ZoneInfo("America/New_York")).timestamp())
    for slug in (f"{COIN[nombre]}-updown-1d-{fin - 86400}",                                   # desde 19-Nov-2026
                 f"{nombre}-up-or-down-on-{MESES[dia.month - 1]}-{dia.day}-{dia.year}"):    # hasta 18-Nov-2026
        r = _S.get(f"{GAMMA}/markets", params={"slug": slug}, timeout=10)
        if r.status_code != 200:
            raise RuntimeError(f"gamma HTTP {r.status_code}")
        j = r.json()
        if isinstance(j, list) and j and int(datetime.fromisoformat(j[0]["endDate"].replace("Z", "+00:00")).timestamp()) == fin:
            return slug, j[0]
    return slug, None


def _twap_en(activo: str, seg: int):
    """twap60 oficial (PolyBolt/Chainlink) del segundo exacto `seg`; caché por (activo, seg). None si falta."""
    try:
        cache = json.loads(REF_CACHE.read_text())
    except (OSError, ValueError):
        cache = {}
    k = f"{activo}|{seg}"
    if k in cache:
        return cache[k]
    p = PRICES / f"polybolt_{datetime.fromtimestamp(seg, timezone.utc):%Y-%m-%d}.csv"
    v, objetivo, pref = None, str(seg * 1000), f",{activo},twap60,"
    if not p.exists() and p.with_suffix(".csv.gz").exists():
        p = p.with_suffix(".csv.gz")
    if p.exists():
        import gzip
        with (gzip.open(p, "rt", encoding="utf-8") if p.suffix == ".gz" else open(p, encoding="utf-8")) as f:
            for ln in f:
                if pref in ln:
                    c = ln.rstrip("\n").split(",")
                    if c[4] == objetivo and c[6] == "chainlink":
                        v = float(c[3]); break
    if v is not None:
        cache[k] = v
        tmp = REF_CACHE.with_suffix(".tmp")
        tmp.write_text(json.dumps(dict(list(cache.items())[-200:])))
        tmp.replace(REF_CACHE)
    return v


def _twap_ultimo(activo: str, ahora: datetime):
    """Último twap60 del fichero de hoy (lee solo la cola) -> (valor, edad_s) o (None, None)."""
    p = PRICES / f"polybolt_{ahora:%Y-%m-%d}.csv"
    if not p.exists():
        return None, None
    with open(p, "rb") as f:
        f.seek(0, 2); f.seek(max(0, f.tell() - 60000))
        cola = f.read().decode("utf-8", "replace").splitlines()[1:]
    for ln in reversed(cola):
        c = ln.split(",")
        if len(c) >= 7 and c[1] == activo and c[2] == "twap60" and c[6] == "chainlink":
            return float(c[3]), round(ahora.timestamp() - int(c[4]) / 1000, 1)
    return None, None


def _kline_cierre(simbolo: str, apertura_utc: datetime):
    j = _S.get(f"{BINANCE}/klines", params={"symbol": simbolo, "interval": "1m", "limit": 1,
                                             "startTime": int(apertura_utc.timestamp() * 1000)}, timeout=8).json()
    return float(j[0][4]) if j and int(j[0][0]) == int(apertura_utc.timestamp() * 1000) else None


def _sigma_1m(simbolo: str):
    j = _S.get(f"{BINANCE}/klines", params={"symbol": simbolo, "interval": "1m", "limit": 121}, timeout=8).json()
    c = [float(x[4]) for x in j]
    r = [math.log(b / a) for a, b in zip(c, c[1:])]
    if len(r) < 60:
        return None, (c[-1] if c else None)
    m = sum(r) / len(r)
    return math.sqrt(sum((x - m) ** 2 for x in r) / len(r)), c[-1]


def main() -> int:
    ahora = datetime.now(timezone.utc)
    forzar = "--forzar" in sys.argv
    filas = []
    for nombre, simbolo in ACTIVOS.items():
        fila = {"ts_utc": ahora.isoformat(timespec="seconds"), "activo": simbolo[:-4], "error": ""}
        try:
            slug, m = None, None
            for d in (ahora, ahora + timedelta(days=1)):          # el de hoy; si ya cerró, el de mañana
                slug, m = _mercado(nombre, d)
                if m and datetime.fromisoformat(m["endDate"].replace("Z", "+00:00")) + timedelta(minutes=VENTANA_DESPUES_MIN) > ahora:
                    break
                m = None
            if m is None:
                continue
            fin = datetime.fromisoformat(m["endDate"].replace("Z", "+00:00"))
            resto = (fin - ahora).total_seconds() / 60
            if not forzar and not (-VENTANA_DESPUES_MIN <= resto <= VENTANA_ANTES_MIN):
                continue
            t0 = time.time()
            outs, toks = json.loads(m["outcomes"]), json.loads(m["clobTokenIds"])
            i_up = outs.index("Up")
            regla = "twap60_chainlink" if "TWAP" in (m.get("description") or "") else "binance_1m"
            sigma, spot = _sigma_1m(simbolo)
            edad = ""
            if regla == "twap60_chainlink":     # ref y proyección de la MISMA fuente (PolyBolt twap60)
                ref = _twap_en(simbolo[:-4], int((fin - timedelta(days=1)).timestamp()))
                spot, edad = _twap_ultimo(simbolo[:-4], ahora)
                if edad is not None and edad > 30:
                    spot = None                  # fail-closed: twap60 rancio -> sin z
            else:
                ref = _kline_cierre(simbolo, fin - timedelta(days=1))
            ask_u, bid_u, usd_u = _libro(toks[i_up])
            ask_d, bid_d, usd_d = _libro(toks[1 - i_up])
            z = p = ""
            if ref and spot and sigma and resto + 1 > 0.05:
                z = math.log(spot / ref) / (sigma * math.sqrt(max(resto + (1 if regla == "binance_1m" else 0.5), 0.05)))   # binance: la vela decisiva cierra 1 min después; twap60: media del último minuto ≈ +0,5
                p = round(_phi(z), 4)
                z = round(z, 3)
            fila.update({"slug": slug, "market_id": m.get("id", ""), "min_restantes": round(resto, 2), "spot": spot,
                         "ref": ref if ref is not None else "", "sigma_1m": f"{sigma:.6f}" if sigma else "", "z": z,
                         "prob_justa_up": p, "ask_up": ask_u if ask_u is not None else "",
                         "bid_up": bid_u if bid_u is not None else "", "usd_ask_up": usd_u,
                         "ask_down": ask_d if ask_d is not None else "", "bid_down": bid_d if bid_d is not None else "",
                         "usd_ask_down": usd_d, "lat_ms": round((time.time() - t0) * 1000),
                         "regla": regla, "spot_edad_s": edad if edad is not None else ""})
        except Exception as e:
            fila["error"] = f"{type(e).__name__}: {e}"[:120]
        filas.append(fila)
    if not filas:
        return 0
    if "--no-escribir" in sys.argv:
        for f in filas:
            print({k: f.get(k, "") for k in COLS})
        return 0
    nuevo = not OUT.exists()
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow({k: fila.get(k, "") for k in COLS})
    return 0


if __name__ == "__main__":
    sys.exit(main())
