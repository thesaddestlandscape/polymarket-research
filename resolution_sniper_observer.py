#!/usr/bin/env python3
"""
resolution_sniper_observer.py — captura observacional del sniping de
resolución por latencia en TODAS las monedas que operamos en 5min y
15min (BTC/ETH/SOL/XRP/DOGE/BNB), no solo BTC.

Origen (2026-07-28, misma sesión que idea_wallet_0bba_resolution_sniper_
5min_btc_28jul): analizada la wallet real 0x0bbaee5747feafc2df73ada86b2b
de69a225d7bb vía data-api.polymarket.com/activity (680 mercados BTC#5min
cerrados, 75.0% hit, +6090 USDC) — el 98.3% de sus compras ocurren 1-3s
DESPUÉS del cierre nominal de la ventana (mediana 1s), comprando el lado
ya casi cierto antes de que el libro/AMM termine de converger a ~0.99.

Mecanismo: cuando una ventana Up/Down cierra, el resultado ya lo
determina el precio Chainlink (fuente de resolución OFICIAL,
`fetch_chainlink_prices.py`, screen `chainlink`) en el instante exacto
del cierre, pero el libro de Polymarket (ask_yes/ask_no) tarda unos
segundos en reflejarlo del todo — ventana de oportunidad.

Por qué un observador nuevo y no reusar datos ya capturados: la única
fuente con book de ambos lados (`fetch_libro_ambos_lados.py`,
`data/shadow/libro_ambos_lados_YYYY-MM-DD.csv`) escanea cada 45s
(INTERVALO_ESCANEO_S) — demasiado grueso para medir un fenómeno de 1-3
segundos. Este script solo despierta un hilo por (activo,marco) unos
segundos antes de cada cierre y muestrea el libro a alta frecuencia
(~1 lectura/segundo) durante T-2s..T+8s, cruzado con el precio Chainlink
en el mismo instante (leído de `data/prices/chainlink_YYYY-MM-DD.csv`,
que `fetch_chainlink_prices.py` ya escribe en near-tiempo-real, un
open+write+close por tick — no hace falta abrir un 2º websocket).

Diseño explícito por moneda (características reales, no "café para
todos" -- petición Javi 28-Jul "atendiendo a las características de
cada una"):
  - BTC/ETH/SOL/XRP: ya tenían cobertura Chainlink (SIMBOLOS en
    fetch_chainlink_prices.py). ask_sum medio (spread) 1.01-1.02 —
    libro más eficiente, mayor probabilidad de que el edge sobreviva
    al spread.
  - DOGE/BNB: NO tenían cobertura Chainlink hasta este mismo commit
    (añadidos a SIMBOLOS) -- requiere el restart de la screen
    `chainlink` para empezar a recibir sus ticks. ask_sum medio
    1.04-1.06 (bastante más ancho, medido en `libro_ambos_lados`) --
    la oportunidad, si existe, es más estrecha después de pagar spread;
    NO asumir que replica igual que BTC, es precisamente lo que este
    observador tiene que medir.
  - BTC#5min es el caso con evidencia más fuerte a favor (broken hoy:
    FAVORITO_CONFIRMADO#BTC#5min n=10 ic=-0.125 desactivada, mientras
    la wallet real saca 75% hit ahí) — prioridad de análisis cuando
    haya n suficiente.
  - ETH/SOL/XRP#5min: FAVORITO_CONFIRMADO YA funciona razonable ahí
    (ic +0.127/+0.135, activa) con el mecanismo normal (disparo
    temprano) — este observador mide si el sniper tardío MEJORA la
    fill-ability sobre lo que ya hay, no si "arregla algo roto".
  - 15min (las 6 monedas): FAVORITO_CONFIRMADO YA funciona bien en
    general (ic +0.11 a +0.21) — prioridad más baja, capturado igual
    para tener el dato cuando haga falta decidir.

Puramente observacional: NO ejecuta nada, NO toca dinero, NO se integra
con el pipeline de predicciones. Escribe su propio CSV, se resuelve con
el outcome oficial de Polymarket (mismo patrón que
favorito_ultimosegundo_5min.py/photo_finish_logger.py).

Corre en screen propia:
  screen -dmS ressniper bash -c "cd /root/polymarket-research && .venv/bin/python resolution_sniper_observer.py >> logs/resolution_sniper_observer.log 2>&1"
"""

import csv
import json
import threading
import time
from collections import deque
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO = Path(__file__).resolve().parent
DIR_SHADOW = REPO / "data" / "shadow"
DIR_PRICES = REPO / "data" / "prices"

GAMMA = "https://gamma-api.polymarket.com"
CLOB = "https://clob.polymarket.com"
TIMEOUT = 5

ASSETS = ["BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"]
TIMEFRAMES = {"5min": (300, "5m"), "15min": (900, "15m")}

# Offsets de muestreo relativos al cierre nominal (segundos, negativo =
# antes del cierre). Cubre el margen [-2, +8] con paso ~1s -- suficiente
# para ver la referencia justo antes y la convergencia del libro después,
# sin machacar el book endpoint (10 lecturas por mercado por marco).
OFFSETS_S = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 8]

DESPERTAR_ANTICIPO_S = 6   # el hilo despierta ANTES del primer offset (-2s)
RESOLVE_DELAY_S = 90       # mismo margen que el resto del proyecto (anti-parpadeo)

COLUMNS = [
    "timestamp_utc", "activo", "marco", "slug", "market_id", "condition_id",
    "ts_end", "offset_s", "chainlink_price", "chainlink_ref_open",
    "chainlink_direccion_implicita", "ask_yes", "ask_no", "bid_yes", "bid_no",
    "outcome_real", "acierto_direccion_implicita",
]


def _log(msg: str):
    print(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}", flush=True)


# ─────────────────────────────────────────────────────────────────────────
# Tail en memoria de data/prices/chainlink_YYYY-MM-DD.csv -- evita abrir un
# 2º websocket, reusa lo que fetch_chainlink_prices.py (screen `chainlink`)
# ya está escribiendo en near-tiempo-real (open+write+close por tick).
# ─────────────────────────────────────────────────────────────────────────
class _ChainlinkTail:
    def __init__(self, ventana_s: int = 1800):
        self._buf = {a: deque() for a in ASSETS}  # asset -> deque[(epoch, price)]
        self._ventana_s = ventana_s
        self._lock = threading.Lock()
        self._pos = 0
        self._archivo_actual = None

    def _archivo_hoy(self) -> Path:
        return DIR_PRICES / f"chainlink_{datetime.now(timezone.utc).strftime('%Y-%m-%d')}.csv"

    def _loop(self):
        while True:
            try:
                archivo = self._archivo_hoy()
                if archivo != self._archivo_actual:
                    self._archivo_actual = archivo
                    self._pos = 0
                if archivo.exists():
                    with open(archivo, encoding="utf-8") as f:
                        f.seek(self._pos)
                        nuevas = f.readlines()
                        self._pos = f.tell()
                    if nuevas:
                        ahora = time.time()
                        with self._lock:
                            for linea in nuevas:
                                partes = linea.rstrip("\n").split(",")
                                if len(partes) < 3 or partes[0] == "timestamp_utc":
                                    continue
                                asset = partes[1]
                                if asset not in self._buf:
                                    continue
                                try:
                                    ts = datetime.fromisoformat(partes[0]).timestamp()
                                    price = float(partes[2])
                                except (ValueError, IndexError):
                                    continue
                                dq = self._buf[asset]
                                dq.append((ts, price))
                                while dq and dq[0][0] < ahora - self._ventana_s:
                                    dq.popleft()
            except Exception as e:
                _log(f"[chainlink_tail] error: {e}")
            time.sleep(0.3)

    def arrancar(self):
        threading.Thread(target=self._loop, daemon=True).start()

    def precio_en(self, asset: str, epoch: float):
        """Precio más cercano a `epoch` dentro de la ventana bufferizada,
        o None si no hay dato suficientemente cerca (>5s de distancia)."""
        with self._lock:
            dq = list(self._buf.get(asset, ()))
        if not dq:
            return None
        mejor = min(dq, key=lambda t: abs(t[0] - epoch))
        if abs(mejor[0] - epoch) > 5.0:
            return None
        return mejor[1]

    def precio_ultimo(self, asset: str):
        with self._lock:
            dq = self._buf.get(asset)
            return dq[-1][1] if dq else None


_TAIL = _ChainlinkTail()


# ─────────────────────────────────────────────────────────────────────────
# Descubrimiento de mercado (mismo patrón que favorito_ultimosegundo_5min.py
# / ballenas_executor_btc15m.py) -- slug determinista, cacheado.
# ─────────────────────────────────────────────────────────────────────────
_CACHE_MKT = {}


def mercado_slot(asset: str, marco_tag: str, ts_start: int):
    slug = f"{asset.lower()}-updown-{marco_tag}-{ts_start}"
    if slug in _CACHE_MKT:
        return slug, _CACHE_MKT[slug]
    try:
        r = requests.get(f"{GAMMA}/events", params={"slug": slug}, timeout=TIMEOUT)
        if r.status_code != 200:
            return slug, None
        ev = r.json()
        if not ev or not ev[0].get("markets"):
            return slug, None
        mkt = ev[0]["markets"][0]
        _CACHE_MKT[slug] = mkt
        return slug, mkt
    except Exception:
        return slug, None


def token_ids(mkt: dict):
    """(token_yes, token_no) validado contra `outcomes` -- mismo motivo que
    live_trade._get_token_ids: clobTokenIds[0] NO siempre es YES/Up, asumirlo
    a ciegas mezclaría ask_yes/ask_no en el CSV sin ningún aviso."""
    try:
        tokens = json.loads(mkt.get("clobTokenIds") or "[]")
        outcomes = json.loads(mkt.get("outcomes") or "[]")
    except Exception:
        return None, None
    if len(tokens) < 2 or len(outcomes) < 2:
        return None, None
    AFIRMATIVOS = {"yes", "up"}
    NEGATIVOS = {"no", "down"}
    o0, o1 = str(outcomes[0]).strip().lower(), str(outcomes[1]).strip().lower()
    if o0 in AFIRMATIVOS and o1 in NEGATIVOS:
        return tokens[0], tokens[1]
    if o0 in NEGATIVOS and o1 in AFIRMATIVOS:
        return tokens[1], tokens[0]
    return None, None


def libro(token_yes: str, token_no: str):
    def _mejor(token_id, lado):
        try:
            r = requests.get(f"{CLOB}/book", params={"token_id": token_id}, timeout=TIMEOUT)
            if r.status_code != 200:
                return None, None
            b = r.json()
            asks = [float(a["price"]) for a in (b.get("asks") or [])]
            bids = [float(a["price"]) for a in (b.get("bids") or [])]
            return (min(asks) if asks else None), (max(bids) if bids else None)
        except Exception:
            return None, None
    ask_yes, bid_yes = _mejor(token_yes, "yes")
    ask_no, bid_no = _mejor(token_no, "no")
    return ask_yes, ask_no, bid_yes, bid_no


def outcome_oficial(market_id: str):
    try:
        r = requests.get(f"{GAMMA}/markets/{market_id}", timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        m = r.json()
        pr = m.get("outcomePrices")
        pr = json.loads(pr) if isinstance(pr, str) else pr
        if not pr or len(pr) < 2:
            return None
        if float(pr[0]) >= 0.999:
            return "Up"
        if float(pr[1]) >= 0.999:
            return "Down"
    except Exception:
        pass
    return None


# ─────────────────────────────────────────────────────────────────────────
def _csv_path(dt: datetime) -> Path:
    return DIR_SHADOW / f"resolution_sniper_obs_{dt.strftime('%Y-%m-%d')}.csv"


def guardar(filas: list):
    if not filas:
        return
    path = _csv_path(datetime.now(timezone.utc))
    nuevo = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        if nuevo:
            w.writeheader()
        for fila in filas:
            w.writerow(fila)


def resolver_pendientes():
    ahora = datetime.now(timezone.utc)
    for delta_dias in (0, 1):
        dt = datetime.fromtimestamp(ahora.timestamp() - delta_dias * 86400, timezone.utc)
        path = _csv_path(dt)
        if not path.exists():
            continue
        with open(path, encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        cambiado = False
        pendientes_por_mkt = {}
        for r in rows:
            if r["outcome_real"] or not r["market_id"]:
                continue
            pendientes_por_mkt.setdefault(r["market_id"], []).append(r)
        for market_id, filas in pendientes_por_mkt.items():
            try:
                ts_end = float(filas[0]["ts_end"])
            except (ValueError, IndexError):
                continue
            if ahora.timestamp() - ts_end < RESOLVE_DELAY_S:
                continue
            out = outcome_oficial(market_id)
            if not out:
                continue
            for r in filas:
                r["outcome_real"] = out
                dir_imp = r.get("chainlink_direccion_implicita")
                r["acierto_direccion_implicita"] = (
                    "1" if dir_imp and dir_imp == out else ("0" if dir_imp else "")
                )
                cambiado = True
        if cambiado:
            tmp = path.with_suffix(".tmp")
            with open(tmp, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=COLUMNS)
                w.writeheader()
                w.writerows(rows)
            tmp.replace(path)
            n_res = sum(1 for r in rows if r["outcome_real"])
            _log(f"resolver: {path.name} {n_res}/{len(rows)} resueltas")


def observar_ventana(asset: str, marco: str, dur_s: int, marco_tag: str, ts_end: int):
    ts_start = ts_end - dur_s
    slug, mkt = mercado_slot(asset, marco_tag, ts_start)
    if not mkt:
        return []
    market_id = mkt.get("id", "")
    condition_id = mkt.get("conditionId", "")
    token_yes, token_no = token_ids(mkt)
    ref_open = _TAIL.precio_en(asset, ts_start) or _TAIL.precio_en(asset, ts_start + 2)

    filas = []
    for offset in OFFSETS_S:
        objetivo = ts_end + offset
        espera = objetivo - time.time()
        if espera > 0:
            time.sleep(espera)
        precio = _TAIL.precio_ultimo(asset)
        ask_yes = ask_no = bid_yes = bid_no = ""
        if token_yes and token_no:
            ay, an, by, bn = libro(token_yes, token_no)
            ask_yes = ay if ay is not None else ""
            ask_no = an if an is not None else ""
            bid_yes = by if by is not None else ""
            bid_no = bn if bn is not None else ""
        direccion_implicita = ""
        if precio is not None and ref_open is not None and ref_open > 0:
            if precio > ref_open:
                direccion_implicita = "Up"
            elif precio < ref_open:
                direccion_implicita = "Down"
        filas.append({
            "timestamp_utc": datetime.now(timezone.utc).isoformat(timespec="milliseconds"),
            "activo": asset, "marco": marco, "slug": slug,
            "market_id": market_id, "condition_id": condition_id,
            "ts_end": ts_end, "offset_s": offset,
            "chainlink_price": precio if precio is not None else "",
            "chainlink_ref_open": ref_open if ref_open is not None else "",
            "chainlink_direccion_implicita": direccion_implicita,
            "ask_yes": ask_yes, "ask_no": ask_no, "bid_yes": bid_yes, "bid_no": bid_no,
            "outcome_real": "", "acierto_direccion_implicita": "",
        })
    return filas


def worker(asset: str, marco: str, dur_s: int, marco_tag: str):
    while True:
        now = time.time()
        ts_end = (int(now) // dur_s + 1) * dur_s
        despertar = ts_end - DESPERTAR_ANTICIPO_S
        resto = despertar - time.time()
        if resto > 0:
            time.sleep(resto)
        try:
            filas = observar_ventana(asset, marco, dur_s, marco_tag, ts_end)
            guardar(filas)
        except Exception as e:
            _log(f"[{asset}#{marco}] error en ventana ts_end={ts_end}: {e}")
        # evitar re-disparar la misma ventana si algo fue más lento de lo esperado
        resto2 = ts_end + max(OFFSETS_S) + 1 - time.time()
        if resto2 > 0:
            time.sleep(resto2)


def main():
    DIR_SHADOW.mkdir(parents=True, exist_ok=True)
    _TAIL.arrancar()
    time.sleep(2)  # dar tiempo a que el tail acumule algo de buffer inicial
    _log(f"resolution_sniper_observer arrancado — activos={ASSETS} marcos={list(TIMEFRAMES)} "
         f"offsets={OFFSETS_S}")

    hilos = []
    with ThreadPoolExecutor(max_workers=len(ASSETS) * len(TIMEFRAMES)) as ex:
        for asset in ASSETS:
            for marco, (dur_s, tag) in TIMEFRAMES.items():
                ex.submit(worker, asset, marco, dur_s, tag)
        # loop de resolución periódica en el hilo principal del pool
        while True:
            try:
                resolver_pendientes()
            except Exception as e:
                _log(f"resolver_pendientes error: {e}")
            time.sleep(30)


if __name__ == "__main__":
    main()
