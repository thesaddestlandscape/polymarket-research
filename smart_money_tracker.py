"""
smart_money_tracker.py — Rastrea wallets reales que operan en nuestros mismos
mercados (BTC/ETH/SOL/XRP Up-or-Down 5/15/60min) y mide su historial de PNL
verificado contra la API pública de Polymarket. Genera una señal de "consenso
de smart money" por activo como feature observacional para shadow_predict.py.

Origen (2026-07-01): Javi propuso estudiar los bots que mejor funcionan en
nuestros mercados. Un repo/artículo sobre "el mejor bot" no sirve — si de
verdad gana dinero, nadie lo publica (razonamiento verificado ya dos veces
esta semana con wallets citadas en artículos que no aguantaban el cruce con
data-api.polymarket.com). La alternativa que sí funciona: mirar los datos
reales de quién opera en estos mercados y verificar su track record
directamente, no creer narrativas de terceros. Conecta con P12 del roadmap
(CLAUDE.md: "Smart money wallets + trade size feature") — esta es la versión
ligera y ya en marcha, sin esperar la descarga de 36GB de Jon-Becker.

Metodología:
1. Toma mercados recientes (últimas ~30h) de BTC/ETH/SOL/XRP Up-or-Down
   5/15/60min desde data/markets/*.csv.
2. Para cada mercado, pide los trades reales vía data-api.polymarket.com/trades.
3. Agrega por wallet: nº de operaciones, dirección, activos tocados.
4. Para wallets con actividad suficiente (>=5 trades en la muestra), pide su
   historial de posiciones y calcula PNL/win-rate REAL, filtrado solo a
   posiciones "Up or Down" (mismo universo que operamos nosotros).
5. Persiste todo en data/shadow/smart_money_wallets.json (se acumula, no se
   sobrescribe del todo — cachea wallets ya evaluadas <6h para no re-pedir
   de más). Calcula consenso direccional reciente de las wallets "smart"
   (win_rate>0.55, n>=10, pnl>0) por activo → smart_money_consensus.json.

Solo observacional: shadow_predict.py añade el consenso como feature, no
cambia ninguna decisión todavía. Corre por su propio cron (no toca fast/slow).
"""
import csv
import json
import random
import re
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

DIR_MARKETS = Path("data/markets")
DIR_SHADOW = Path("data/shadow")
WALLETS_PATH = DIR_SHADOW / "smart_money_wallets.json"
CONSENSUS_PATH = DIR_SHADOW / "smart_money_consensus.json"

DATA_API = "https://data-api.polymarket.com"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; polymarket-research/1.0)",
    "Accept": "application/json",
}
TIMEOUT = 20
SLEEP_ENTRE_LLAMADAS = 0.2

ACTIVOS = ("BTC", "ETH", "SOL", "XRP")
# Duración real por tag de evento (más fiable que el slug: 5min/15min/4h usan
# slug "activo-updown-Xm-..." pero 60min ("hourly") usa un slug sin duración
# fija, ej. "bitcoin-up-or-down-july-2-2026-7am-et" — solo el tag lo distingue.
TAG_A_DURACION = {"5M": "5m", "15M": "15m", "1H": "60m", "4H": "240m"}
# WEEKLY_PRICE (mercados de rango/umbral de precio, tag "Weekly", pregunta
# "Will the price of X be above/below/between $A and $B on <fecha>?") usan
# el nombre completo del activo en vez del ticker — ni en tags ni en la
# pregunta aparece "BTC"/"ETH" literal.
NOMBRE_A_TICKER = {"bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL", "xrp": "XRP"}
_RE_WEEKLY_TITLE = re.compile(r"the price of .* be (above|below|less than|greater than|between)", re.I)

VENTANA_MERCADOS_HORAS = 30      # cuántas horas hacia atrás muestrear mercados
MAX_MERCADOS_MUESTRA = 150       # tope de mercados a consultar por ciclo
MAX_TRADES_POR_MERCADO = 100
MIN_TRADES_PARA_CANDIDATO = 5    # nº mínimo de trades en la muestra para mirar su PNL
MAX_CANDIDATOS_POR_CICLO = 300   # tope de llamadas a /positions por ciclo, por si acaso
REFRESH_POSICIONES_HORAS = 6     # no re-pedir /positions si se evaluó hace menos de esto
MIN_N_SMART = 10
MIN_WINRATE_SMART = 0.55


def _cargar_json(path, default):
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return default


def _get(url, params=None):
    try:
        r = requests.get(url, params=params, headers=HEADERS, timeout=TIMEOUT)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        print(f"  [warn] {url}: {e}")
        return None


def mercados_recientes() -> dict:
    """Devuelve {condition_id: {question, slug, activo, duracion}} de mercados
    de nuestro universo vistos en las últimas VENTANA_MERCADOS_HORAS."""
    corte = datetime.now(timezone.utc) - timedelta(hours=VENTANA_MERCADOS_HORAS)
    vistos = {}
    archivos = sorted(DIR_MARKETS.glob("*.csv"))[-2:]  # hoy + ayer, por si cruza medianoche
    for archivo in archivos:
        try:
            with open(archivo, encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    tags = (row.get("event_tags") or "").split("|")
                    question = row.get("question") or ""
                    duracion = next((TAG_A_DURACION[t] for t in tags if t in TAG_A_DURACION), None)
                    activo = None
                    if duracion is not None:
                        if "Up or Down" not in question:
                            continue
                        activo = next((a for a in ACTIVOS if a in [t.upper() for t in tags]
                                       or a.lower() in question.lower()), None)
                    elif "Up or Down" not in question and (
                        "weekly" in [t.lower() for t in tags] or "week" in question.lower()
                    ):
                        # WEEKLY_PRICE: mismo universo que shadow_predict.py::s_weekly_price
                        # (pregunta "the price of <nombre completo> be above/below/between..."),
                        # nombre completo del activo, no ticker.
                        duracion = "weekly"
                        activo = next((tk for nombre, tk in NOMBRE_A_TICKER.items()
                                       if nombre in question.lower()), None)
                    if duracion is None or not activo:
                        continue
                    ts = row.get("timestamp_utc", "")
                    try:
                        ts_dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                    except Exception:
                        continue
                    if ts_dt < corte:
                        continue
                    cid = row.get("condition_id", "")
                    if not cid or cid in vistos:
                        continue
                    vistos[cid] = {
                        "question": question,
                        "slug": row.get("slug", ""),
                        "activo": activo,
                        "duracion": duracion,
                    }
        except Exception as e:
            print(f"  [warn] leyendo {archivo}: {e}")
    return vistos


def trades_de_mercado(condition_id: str) -> list:
    data = _get(f"{DATA_API}/trades", {"market": condition_id, "limit": MAX_TRADES_POR_MERCADO})
    time.sleep(SLEEP_ENTRE_LLAMADAS)
    return data or []


def _resumen_posiciones(data: list, filtro_titulo) -> dict:
    pos = [p for p in data if filtro_titulo(p.get("title") or "")]
    n = len(pos)
    if n == 0:
        return {"n": 0}
    wins = sum(1 for p in pos if (p.get("cashPnl") or 0) > 0)
    pnl_total = sum(float(p.get("cashPnl") or 0) for p in pos)
    tam_medio = sum(float(p.get("initialValue") or 0) for p in pos) / n
    return {
        "n": n,
        "win_rate": round(wins / n, 4),
        "pnl_total": round(pnl_total, 2),
        "tamano_medio_usd": round(tam_medio, 2),
    }


def posiciones_updown(wallet: str) -> dict:
    """PNL/win-rate real de una wallet, filtrado a posiciones 'Up or Down'."""
    data = _get(f"{DATA_API}/positions", {"user": wallet, "limit": 500}) or []
    time.sleep(SLEEP_ENTRE_LLAMADAS)
    return _resumen_posiciones(data, lambda t: "Up or Down" in t)


def posiciones_weekly(wallet: str) -> dict:
    """PNL/win-rate real de una wallet, filtrado a posiciones WEEKLY_PRICE
    (rango/umbral de precio, título tipo 'the price of X be above/below/
    between...'). Track record separado del de Up-or-Down: son apuestas de
    naturaleza distinta (umbral de precio vs. dirección), mezclarlas
    diluiría ambas señales."""
    data = _get(f"{DATA_API}/positions", {"user": wallet, "limit": 500}) or []
    time.sleep(SLEEP_ENTRE_LLAMADAS)
    return _resumen_posiciones(data, lambda t: bool(_RE_WEEKLY_TITLE.search(t)))


def main():
    print(f"[smart_money_tracker] {datetime.now(timezone.utc).isoformat(timespec='seconds')}")
    mercados = mercados_recientes()
    print(f"  Mercados en universo (últimas {VENTANA_MERCADOS_HORAS}h): {len(mercados)}")
    condition_ids = list(mercados.keys())
    random.shuffle(condition_ids)
    condition_ids = condition_ids[:MAX_MERCADOS_MUESTRA]

    actividad_wallet = defaultdict(lambda: {
        "n": 0,
        "activos": defaultdict(lambda: {"up": 0, "down": 0}),
        "duraciones": defaultdict(int),
    })
    for cid in condition_ids:
        info = mercados[cid]
        for t in trades_de_mercado(cid):
            w = t.get("proxyWallet")
            if not w:
                continue
            actividad_wallet[w]["n"] += 1
            actividad_wallet[w]["duraciones"][info["duracion"]] += 1
            # /trades usa "up"/"down" o "yes"/"no" según el mercado (mismo
            # patrón ya visto en capture_trades.py) — antes solo reconocía
            # "up" literal, así que un mercado con "yes"/"no" clasificaba
            # todo como "down", sesgando el consenso hacia negativo.
            lado = "up" if (t.get("outcome") or "").strip().lower() in ("up", "yes") else "down"
            actividad_wallet[w]["activos"][info["activo"]][lado] += 1

    print(f"  Wallets distintas vistas: {len(actividad_wallet)}")
    duraciones_totales = defaultdict(int)
    for d in actividad_wallet.values():
        for dur, n in d["duraciones"].items():
            duraciones_totales[dur] += n
    print(f"  Trades por duración en la muestra: {dict(duraciones_totales)}")
    candidatos = {w: d for w, d in actividad_wallet.items() if d["n"] >= MIN_TRADES_PARA_CANDIDATO}
    print(f"  Candidatas con >= {MIN_TRADES_PARA_CANDIDATO} trades en la muestra: {len(candidatos)}")
    if len(candidatos) > MAX_CANDIDATOS_POR_CICLO:
        claves = random.sample(list(candidatos.keys()), MAX_CANDIDATOS_POR_CICLO)
        candidatos = {k: candidatos[k] for k in claves}
        print(f"  Recortado a {MAX_CANDIDATOS_POR_CICLO} candidatas al azar (tope de llamadas por ciclo)")

    wallets_db = _cargar_json(WALLETS_PATH, {})
    ahora = datetime.now(timezone.utc)
    consultadas = 0
    consultadas_weekly = 0
    for w, act in candidatos.items():
        prev = wallets_db.get(w, {})
        ultima = prev.get("ultima_actualizacion")
        fresca = False
        if ultima:
            try:
                fresca = (ahora - datetime.fromisoformat(ultima)) < timedelta(hours=REFRESH_POSICIONES_HORAS)
            except Exception:
                fresca = False
        if fresca:
            stats = {k: prev[k] for k in ("n", "win_rate", "pnl_total", "tamano_medio_usd") if k in prev}
            weekly_stats = prev.get("weekly")
        else:
            stats = posiciones_updown(w)
            consultadas += 1
            # Track record WEEKLY_PRICE aparte — solo se pide si la wallet
            # tuvo actividad reciente en mercados semanales (evita duplicar
            # llamadas a /positions para wallets que solo operan Up-or-Down).
            weekly_stats = None
            if act["duraciones"].get("weekly", 0) > 0:
                weekly_stats = posiciones_weekly(w)
                consultadas_weekly += 1
        clasificacion = "smart" if (
            stats.get("n", 0) >= MIN_N_SMART
            and stats.get("win_rate", 0) >= MIN_WINRATE_SMART
            and stats.get("pnl_total", 0) > 0
        ) else "normal"
        wallets_db[w] = {
            **stats,
            "clasificacion": clasificacion,
            "trades_muestra_reciente": act["n"],
            "activos_muestra_reciente": {k: v for k, v in act["activos"].items()},
            "duraciones_muestra_reciente": dict(act["duraciones"]),
            "primera_vez_visto": prev.get("primera_vez_visto", ahora.isoformat(timespec="seconds")),
            "ultima_actualizacion": ahora.isoformat(timespec="seconds") if not fresca else ultima,
        }
        if weekly_stats is not None:
            wallets_db[w]["weekly"] = weekly_stats
    print(f"  Posiciones consultadas de verdad (resto cacheado <{REFRESH_POSICIONES_HORAS}h): "
          f"{consultadas} (+{consultadas_weekly} weekly)")
    WALLETS_PATH.write_text(json.dumps(wallets_db, indent=2, ensure_ascii=False), encoding="utf-8")

    # Consenso direccional de las wallets "smart" en la muestra reciente, por activo
    consenso = defaultdict(lambda: {"up": 0, "down": 0, "n_wallets_smart": 0})
    for w, act in candidatos.items():
        if wallets_db.get(w, {}).get("clasificacion") != "smart":
            continue
        for activo, dirs in act["activos"].items():
            consenso[activo]["up"] += dirs["up"]
            consenso[activo]["down"] += dirs["down"]
            consenso[activo]["n_wallets_smart"] += 1

    consenso_final = {}
    for activo, d in consenso.items():
        total = d["up"] + d["down"]
        if total == 0:
            continue
        consenso_final[activo] = {
            "smart_money_consensus": round((d["up"] - d["down"]) / total, 4),
            "n_trades_smart": total,
            "n_wallets_smart": d["n_wallets_smart"],
        }
    consenso_final["_actualizado"] = ahora.isoformat(timespec="seconds")
    CONSENSUS_PATH.write_text(json.dumps(consenso_final, indent=2, ensure_ascii=False), encoding="utf-8")

    n_smart = sum(1 for v in wallets_db.values() if v.get("clasificacion") == "smart")
    print(f"  Wallets 'smart' acumuladas en base de datos: {n_smart} / {len(wallets_db)} totales")
    print(f"  Consenso por activo: {consenso_final}")


if __name__ == "__main__":
    main()
