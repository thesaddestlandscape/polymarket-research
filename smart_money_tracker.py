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
import statistics as st
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

from wallet_pnl_diario import fetch_activity

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

# Clasificación "smart" v2 (2026-07-02): el criterio original basado en
# /positions resultó estar INVERTIDO para wallets de alta frecuencia — el
# endpoint solo retiene posiciones sin redimir, y como las ganadoras se
# redimen (cash) y las perdedoras valen 0 (no hay nada que redimir), lo que
# queda listado es el residuo perdedor. Verificado 2026-07-02: la wallet
# "wowitsamazing" figuraba aquí con pnl=-478k/wr=0.002 y en el leaderboard
# oficial (que capturamos a diario en data/wallets/) es +$10k/mes. El
# leaderboard es ahora la fuente autoritativa de "smart"; win_rate/pnl de
# /positions se conservan solo como dato informativo, no como criterio.
DIR_WALLETS = Path("data/wallets")
MIN_PNL_LEADERBOARD_SMART = 1000.0  # USD/mes en leaderboard oficial

# Consenso ponderado por tamaño (P16, CLAUDE.md — cerrado 12-Jul en
# analisis_p16_redencion_corregido.py: el eje de TAMAÑO de apuesta relativo
# a la mediana propia de cada wallet sobreviva y se refuerza tras corregir
# el sesgo de redención (17.8→20.8pp de gap ≥2x vs ≤0.5x); el eje de
# novedad de activo se evaporó y NO se usa aquí). Cada trade de una wallet
# "smart" pesa según su tamaño relativo a la mediana histórica de apuesta
# de ESA wallet (vía /activity), no 1 voto por trade. CAP_RATIO evita que
# una única apuesta enorme de una wallet normalmente pequeña domine el
# consenso (mismo motivo por el que existía el voto plano).
MAX_EVENTOS_MEDIANA = 500
REFRESH_MEDIANA_HORAS = 24
CAP_RATIO = 5.0


def _mediana_apuesta_wallet(wallet: str) -> float | None:
    eventos = fetch_activity(wallet, max_events=MAX_EVENTOS_MEDIANA)
    buys = [float(e.get("usdcSize", 0) or 0) for e in eventos
            if e.get("type") == "TRADE" and e.get("side") == "BUY" and float(e.get("usdcSize", 0) or 0) > 0]
    if not buys:
        return None
    return st.median(buys)


def _leaderboard_pnl() -> dict:
    """{address_lower: pnl_mes} del leaderboard oficial más reciente en disco."""
    # Cada fichero diario acumula capturas horarias del top-~75 → pocas
    # addresses únicas por día. Se fusionan los últimos 3 días para ampliar
    # cobertura (una wallet que estuvo en el top el lunes sigue verificada
    # el miércoles a efectos de clasificación).
    archivos = sorted(DIR_WALLETS.glob("leaderboard_*.csv"))[-3:]
    out: dict[str, float] = {}
    for archivo in archivos:
        try:
            with open(archivo, encoding="utf-8") as f:
                for row in csv.DictReader(f):
                    a = (row.get("address") or "").lower()
                    try:
                        p = float(row.get("pnl") or "")
                    except ValueError:
                        continue
                    if a and (a not in out or p > out[a]):
                        out[a] = p
        except Exception as e:
            print(f"  [warn] leyendo {archivo.name}: {e}")
    return out


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
                    if duracion is not None and "Up or Down" not in question:
                        continue
                    elif duracion is None and "Up or Down" not in question and (
                        "weekly" in [t.lower() for t in tags] or "week" in question.lower()
                    ):
                        # WEEKLY_PRICE: mismo universo que shadow_predict.py::s_weekly_price
                        # (pregunta "the price of <nombre completo> be above/below/between..."),
                        # nombre completo del activo, no ticker.
                        duracion = "weekly"
                    # Detección de activo por NOMBRE COMPLETO en la pregunta
                    # (bitcoin/ethereum/solana/xrp), NUNCA por ticker/tag —
                    # Polymarket etiqueta estos mercados con el nombre
                    # completo ("Bitcoin", no "BTC"). BUG REAL encontrado
                    # 15-Jul (Javi notó que BTC nunca salía en el consenso):
                    # la rama Up-or-Down comprobaba ticker en tags/pregunta
                    # y solo "funcionaba" para ETH/SOL por coincidencia
                    # (ticker=substring del nombre: "eth" en "ethereum",
                    # "sol" en "solana") y XRP (ticker=nombre) — "btc" NO es
                    # substring de "bitcoin", así que TODO mercado de
                    # Bitcoin Up-or-Down quedaba silenciosamente fuera desde
                    # que este tracker existe. La rama weekly ya usaba
                    # NOMBRE_A_TICKER (correcto) — unificadas ambas ramas.
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
        "activos_usd": defaultdict(lambda: {"up": [], "down": []}),
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
            usd = float(t.get("size", 0) or 0) * float(t.get("price", 0) or 0)
            actividad_wallet[w]["activos_usd"][info["activo"]][lado].append(usd)

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
    lb_pnl = _leaderboard_pnl()
    print(f"  Leaderboard oficial cargado: {len(lb_pnl)} wallets con PNL verificado")
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
        # v2: "smart" solo si el leaderboard oficial lo verifica (ver nota en
        # MIN_PNL_LEADERBOARD_SMART — el criterio viejo por /positions estaba
        # invertido para wallets que redimen rápido).
        pnl_lb = lb_pnl.get(w.lower())
        if pnl_lb is not None and pnl_lb >= MIN_PNL_LEADERBOARD_SMART:
            clasificacion = "smart"
        elif (stats.get("n", 0) >= MIN_N_SMART
              and stats.get("win_rate", 0) >= MIN_WINRATE_SMART
              and stats.get("pnl_total", 0) > 0):
            # criterio viejo: se degrada a candidato (no entra en el consenso)
            clasificacion = "candidato_posiciones"
        else:
            clasificacion = "normal"

        # Mediana de apuesta propia (P16) — solo se pide para wallets "smart"
        # (las únicas que cuentan en el consenso), cacheada aparte con su
        # propia cadencia porque el tamaño típico cambia más despacio que el
        # win-rate de /positions.
        mediana_apuesta = prev.get("mediana_apuesta_usd")
        mediana_actualizada = prev.get("mediana_actualizada")
        mediana_fresca = False
        if mediana_actualizada:
            try:
                mediana_fresca = (ahora - datetime.fromisoformat(mediana_actualizada)) < timedelta(hours=REFRESH_MEDIANA_HORAS)
            except Exception:
                mediana_fresca = False
        if clasificacion == "smart" and not mediana_fresca:
            mediana_apuesta = _mediana_apuesta_wallet(w)
            mediana_actualizada = ahora.isoformat(timespec="seconds")

        wallets_db[w] = {
            **stats,
            "clasificacion": clasificacion,
            **({"pnl_leaderboard_mes": round(pnl_lb, 2)} if pnl_lb is not None else {}),
            "trades_muestra_reciente": act["n"],
            "activos_muestra_reciente": {k: v for k, v in act["activos"].items()},
            "duraciones_muestra_reciente": dict(act["duraciones"]),
            "primera_vez_visto": prev.get("primera_vez_visto", ahora.isoformat(timespec="seconds")),
            "ultima_actualizacion": ahora.isoformat(timespec="seconds") if not fresca else ultima,
            **({"mediana_apuesta_usd": round(mediana_apuesta, 2)} if mediana_apuesta else {}),
            **({"mediana_actualizada": mediana_actualizada} if mediana_actualizada else {}),
        }
        if weekly_stats is not None:
            wallets_db[w]["weekly"] = weekly_stats
    print(f"  Posiciones consultadas de verdad (resto cacheado <{REFRESH_POSICIONES_HORAS}h): "
          f"{consultadas} (+{consultadas_weekly} weekly)")
    WALLETS_PATH.write_text(json.dumps(wallets_db, indent=2, ensure_ascii=False), encoding="utf-8")

    # Consenso direccional de las wallets "smart" en la muestra reciente, por activo
    consenso = defaultdict(lambda: {"up": 0, "down": 0, "n_wallets_smart": 0})
    # Consenso ponderado por tamaño (P16): cada trade pesa usd/mediana_propia,
    # tope CAP_RATIO. Wallets sin mediana cacheada aún (primera vez "smart"
    # o /activity vacío) caen al peso plano 1.0 por trade, igual que el
    # consenso sin ponderar, hasta que se compute su baseline.
    consenso_pond = defaultdict(lambda: {"up": 0.0, "down": 0.0, "n_wallets_smart": 0})
    for w, act in candidatos.items():
        info_w = wallets_db.get(w, {})
        if info_w.get("clasificacion") != "smart":
            continue
        mediana = info_w.get("mediana_apuesta_usd")
        for activo, dirs in act["activos"].items():
            consenso[activo]["up"] += dirs["up"]
            consenso[activo]["down"] += dirs["down"]
            consenso[activo]["n_wallets_smart"] += 1
        for activo, usd_dirs in act["activos_usd"].items():
            n_lado = 0
            for lado in ("up", "down"):
                for usd in usd_dirs[lado]:
                    peso = min(usd / mediana, CAP_RATIO) if mediana else 1.0
                    consenso_pond[activo][lado] += peso
                    n_lado += 1
            if n_lado:
                consenso_pond[activo]["n_wallets_smart"] += 1

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
        dp = consenso_pond.get(activo)
        total_p = (dp["up"] + dp["down"]) if dp else 0
        if dp and total_p > 0:
            consenso_final[activo]["smart_money_consensus_ponderado"] = round((dp["up"] - dp["down"]) / total_p, 4)
            consenso_final[activo]["n_wallets_smart_ponderado"] = dp["n_wallets_smart"]
    consenso_final["_actualizado"] = ahora.isoformat(timespec="seconds")
    CONSENSUS_PATH.write_text(json.dumps(consenso_final, indent=2, ensure_ascii=False), encoding="utf-8")

    n_smart = sum(1 for v in wallets_db.values() if v.get("clasificacion") == "smart")
    print(f"  Wallets 'smart' acumuladas en base de datos: {n_smart} / {len(wallets_db)} totales")
    print(f"  Consenso por activo: {consenso_final}")


if __name__ == "__main__":
    main()
