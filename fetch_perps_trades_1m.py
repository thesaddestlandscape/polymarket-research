#!/usr/bin/env python3
"""fetch_perps_trades_1m.py -- serie de precios DENSA de Polymarket Perps (25-Sep, pendiente 1 de
project_perps_pendientes_25sep). Pagina hacia atrás /v1/info/trades?instrument_id= (público, 100/página,
cursor) y agrega a velas de 1 min (open,high,low,close,vol,n) -> data/shadow/perps_precios_1m/<id>.csv
(gitignored). Reanudable: estado perps_precios_1m_state.json {id: {newest_ms, oldest_ms, backfill_done}}.
Cada ejecución: (a) avanza lo NUEVO hasta el newest guardado, (b) continúa el backfill hacia atrás hasta
DESDE_MS o el presupuesto de tiempo (--max-min, def. 12). Solo lectura, ≤1,6 req/s, backoff en 429.
Instrumentos: los que más fills tienen en perps_fills_full + commodities/memecoins (categoría del
universo). Uso: python3 fetch_perps_trades_1m.py [--max-min N]"""
import csv, glob, json, sys, time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import requests

REPO = Path(__file__).resolve().parent
DIR = REPO / "data/shadow/perps_precios_1m"
STATE = REPO / "data/shadow/perps_precios_1m_state.json"
URL = "https://api.perpetuals.polymarket.com/v1/info/trades"
DESDE_MS = int(datetime(2026, 8, 24, tzinfo=timezone.utc).timestamp() * 1000)
N_TOP = 24
COLS = ["ts_min", "open", "high", "low", "close", "vol", "n"]


def instrumentos():
    c = Counter()
    for f in glob.glob(str(REPO / "data/shadow/perps_fills_full/*.csv")):
        for r in csv.DictReader(open(f, encoding="utf-8")):
            c[r["instrument_id"]] += 1
    ids = [i for i, _ in c.most_common(N_TOP)]
    try:
        for x in json.loads((REPO / "data/shadow/polymarket_perps_instruments.json").read_text()):
            if x.get("category") in ("commodity", "crypto_memecoin") and str(x["instrument_id"]) not in ids:
                ids.append(str(x["instrument_id"]))
    except Exception:
        pass
    return ids


def leer(i):
    p = DIR / f"{i}.csv"
    d = {}
    if p.exists():
        for r in csv.DictReader(open(p, encoding="utf-8")):
            d[int(r["ts_min"])] = [float(r["open"]), float(r["high"]), float(r["low"]), float(r["close"]), float(r["vol"]), int(r["n"])]
    return d


def guardar(i, d):
    DIR.mkdir(parents=True, exist_ok=True)
    tmp = DIR / f"{i}.csv.tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(COLS)
        for k in sorted(d):
            w.writerow([k] + d[k])
    tmp.replace(DIR / f"{i}.csv")


def pagina(i, cursor):
    for esp in (1, 2, 5, 15, 30):
        try:
            r = requests.get(URL, params={"instrument_id": i, **({"cursor": cursor} if cursor else {})}, timeout=30)
            if r.status_code == 429:
                time.sleep(esp * 2); continue
            r.raise_for_status()
            return r.json()
        except requests.RequestException:
            time.sleep(esp)
    return None


def agregar(d, trades):
    tmp = defaultdict(list)
    for t in trades:
        tmp[int(t["timestamp"]) // 60000 * 60000].append((int(t["timestamp"]), float(t["price"]), float(t["quantity"])))
    for m, L in tmp.items():
        L.sort(); ps = [p for _, p, _ in L]
        new = [ps[0], max(ps), min(ps), ps[-1], sum(q for *_, q in L), len(L)]
        if m in d:   # fusiona con lo ya guardado (misma vela vista en dos pasadas)
            o = d[m]; new = [o[0] if o[5] >= len(L) else new[0], max(o[1], new[1]), min(o[2], new[2]), new[3] if len(L) >= 1 else o[3], max(o[4], new[4]), max(o[5], new[5])]
        d[m] = new


def klines_1h():
    """Respaldo: /v1/info/statistics devuelve solo las ultimas 24 velas horarias por instrumento; se acumulan
    aqui (perps_klines_1h/<id>.csv, dedupe por hora) para cubrir huecos de la serie de 1 min."""
    try:
        j = requests.get(URL.replace("trades", "statistics"), timeout=30).json()
    except Exception:
        return
    D2 = REPO / "data/shadow/perps_klines_1h"; D2.mkdir(parents=True, exist_ok=True)
    for x in j:
        p = D2 / f"{x['instrument_id']}.csv"
        have = set()
        if p.exists():
            have = {r["t"] for r in csv.DictReader(open(p, encoding="utf-8"))}
        nuevas = [k for k in x.get("klines", []) if str(k[0]) not in have]
        if nuevas:
            nuevo = not p.exists()
            with open(p, "a", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                if nuevo:
                    w.writerow(["t", "open", "high", "low", "close", "vol", "n"])
                for k in nuevas:
                    w.writerow(k[:7])


def main():
    """Sin backfill: /v1/info/trades NO se puede paginar (medido 25-Sep: solo las ultimas 100 operaciones,
    `more`=True sin cursor; 100 operaciones = ~75 min en el instrumento 31). La serie densa se construye HACIA
    ADELANTE con este cron (cada 10 min). Historia previa: solo la dispersa de los propios fills."""
    st = json.loads(STATE.read_text()) if STATE.exists() else {}
    for i in instrumentos():
        j = pagina(i, None)
        if not j or not j.get("data"):
            continue
        tr = j["data"]; d = leer(i); s = st.setdefault(i, {"newest_ms": 0, "huecos": 0})
        ts = [int(t["timestamp"]) for t in tr]
        if s["newest_ms"] and min(ts) > s["newest_ms"] + 1000:
            s["huecos"] += 1              # la pagina no llega hasta lo ya guardado: hueco (mercado muy activo)
        agregar(d, tr); s["newest_ms"] = max(s["newest_ms"], max(ts))
        guardar(i, d); time.sleep(0.5)
    STATE.write_text(json.dumps(st))
    klines_1h()


if __name__ == "__main__":
    main()
