#!/usr/bin/env python3
"""
Extensión de analisis_timing_wallets_smart.py (14-Jul, sesión siguiente):
timing EXACTO de las apuestas GANADORAS de wallets 'smart', desagregado por
activo (BTC/ETH/SOL/XRP/...) y marco temporal (5/15/60min), no solo 15min
agregado. Motivación: el agregado ya mostró que el edge real está en la
zona 8-15min restantes — ¿es uniforme por activo/marco, o hay una
combinación con un patrón más afinado?

Reutiliza el mismo pipeline que analisis_timing_wallets_smart.py (fetch_activity,
fetch_mercados_paralelo/parse_outcome_prices) pero cachea a disco (JSON) para
no repetir llamadas a la API si hace falta iterar el análisis.

Puramente análisis/shadow — no toca live_trade.py/config_live.json.
Uso: python3 analisis_timing_wallets_por_activo.py [--n-wallets 25] [--max-events 500] [--no-cache]
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

from wallet_pnl_diario import fetch_activity
from shadow_resolve import fetch_mercados_paralelo, parse_outcome_prices

DIR = Path(__file__).parent
SMART_WALLETS = DIR / "data/shadow/smart_money_wallets.json"
COND_MAP = Path("/tmp/cond_market_map.csv")
CACHE = Path("/tmp/wallets_timing_cache.json")

PATRON_VENTANA = re.compile(r"(\d{1,2}):(\d{2})(AM|PM)-(\d{1,2}):(\d{2})(AM|PM) ET")
PATRON_HORA_UNICA = re.compile(r"(\d{1,2})(AM|PM) ET")
ACTIVOS = {
    "bitcoin": "BTC", "ethereum": "ETH", "solana": "SOL", "xrp": "XRP",
    "dogecoin": "DOGE", "bnb": "BNB",
}


def parse_dt(s: str) -> datetime:
    dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def duracion_ventana_min(title: str) -> int | None:
    m = PATRON_VENTANA.search(title or "")
    if m:
        h1, m1, ap1, h2, m2, ap2 = m.groups()
        t1 = int(h1) % 12 + (12 if ap1 == "PM" else 0)
        t2 = int(h2) % 12 + (12 if ap2 == "PM" else 0)
        dur = (t2 * 60 + int(m2)) - (t1 * 60 + int(m1))
        if dur < 0:
            dur += 24 * 60
        return dur
    if PATRON_HORA_UNICA.search(title or ""):
        return 60  # "Bitcoin Up or Down - July 14, 1PM ET" = ventana horaria
    return None


def extraer_activo(title: str) -> str | None:
    t = (title or "").lower()
    for k, v in ACTIVOS.items():
        if k in t:
            return v
    return None


def cargar_top_wallets_smart(n: int) -> list[str]:
    data = json.loads(SMART_WALLETS.read_text())
    smart = [(k, v) for k, v in data.items()
             if v.get("clasificacion") == "smart" and (v.get("n") or 0) > 0]
    smart.sort(key=lambda kv: -(kv[1].get("pnl_total") or 0))
    return [k for k, _ in smart[:n]]


def cargar_cond_market_map() -> dict:
    mapa = {}
    with open(COND_MAP, newline="", encoding="utf-8") as f:
        for line in f:
            parts = line.rstrip("\n").split(",")
            if len(parts) == 2 and parts[0] and parts[1] and parts[0] != "market_id":
                mapa[parts[1]] = parts[0]
    return mapa


def recolectar(n_wallets: int, max_events: int) -> list[dict]:
    wallets = cargar_top_wallets_smart(n_wallets)
    print(f"Wallets smart seleccionadas: {len(wallets)}")
    cond_to_market = cargar_cond_market_map()
    print(f"Mapeo condition_id->market_id: {len(cond_to_market)} entradas")

    trades_up_down = []
    for i, w in enumerate(wallets):
        evs = fetch_activity(w, max_events=max_events)
        n_t = 0
        for e in evs:
            if e.get("type") != "TRADE" or e.get("side") != "BUY":
                continue
            title = e.get("title", "")
            if "up or down" not in title.lower():
                continue
            dur = duracion_ventana_min(title)
            activo = extraer_activo(title)
            if dur is None or activo is None:
                continue
            trades_up_down.append({
                "wallet": w,
                "conditionId": e.get("conditionId", ""),
                "timestamp": e["timestamp"],
                "price": e.get("price"),
                "outcomeIndex": e.get("outcomeIndex"),
                "dur_min": dur,
                "activo": activo,
            })
            n_t += 1
        print(f"  [{i+1}/{len(wallets)}] {w[:12]}...: {n_t} trades Up/Down de {len(evs)} eventos")

    print(f"\nTotal trades Up/Down recolectados: {len(trades_up_down)}")

    market_ids_necesarios = set()
    for t in trades_up_down:
        mid = cond_to_market.get(t["conditionId"])
        if mid:
            t["market_id"] = mid
            market_ids_necesarios.add(mid)

    print(f"Mercados únicos a resolver: {len(market_ids_necesarios)}")
    print("Consultando resolución oficial (gamma-api, throttled 3 workers)...")
    resueltos = fetch_mercados_paralelo(list(market_ids_necesarios), workers=3)
    n_ok = sum(1 for v in resueltos.values() if v)
    print(f"Mercados con respuesta: {n_ok}/{len(market_ids_necesarios)}")

    resultados = []
    for t in trades_up_down:
        mid = t.get("market_id")
        if not mid or mid not in resueltos or not resueltos[mid]:
            continue
        mercado = resueltos[mid]
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
        end_str = mercado.get("endDate", "")
        if not end_str:
            continue
        try:
            end_dt = parse_dt(end_str)
            t_dt = datetime.fromtimestamp(t["timestamp"], tz=timezone.utc)
            restante_min = (end_dt - t_dt).total_seconds() / 60
            precio = float(t["price"])
        except Exception:
            continue
        if not (-2 <= restante_min <= t["dur_min"] + 2):
            continue
        compro_yes = (t["outcomeIndex"] == 0)
        acierto = (compro_yes and outcome_real == "YES") or (not compro_yes and outcome_real == "NO")
        resultados.append({
            "wallet": t["wallet"], "activo": t["activo"], "dur_min": t["dur_min"],
            "restante_min": round(restante_min, 2), "precio": precio,
            "acierto": acierto,
        })
    return resultados


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n-wallets", type=int, default=25)
    ap.add_argument("--max-events", type=int, default=500)
    ap.add_argument("--no-cache", action="store_true")
    args = ap.parse_args()

    if not args.no_cache and CACHE.exists():
        print(f"Usando cache: {CACHE} (--no-cache para refrescar)")
        resultados = json.loads(CACHE.read_text())
    else:
        resultados = recolectar(args.n_wallets, args.max_events)
        CACHE.write_text(json.dumps(resultados))
        print(f"Cacheado en {CACHE}")

    print(f"\nTotal trades con resolución+timing válidos: {len(resultados)}")

    # Desagregación por (activo, marco temporal)
    grupos = defaultdict(list)
    for r in resultados:
        grupos[(r["activo"], r["dur_min"])].append(r)

    print("\n=== Por activo x marco temporal (n>=15 para reportar) ===")
    print("    (n_wallets = wallets distintas detrás del bucket; top1% = cuota del PnL")
    print("     positivo que aporta la wallet más concentrada, para detectar si el edge")
    print("     es de 1 cuenta o de verdad está repartido — mismo error que SOL#5min)")
    for (activo, dur), rs in sorted(grupos.items(), key=lambda kv: -len(kv[1])):
        n = len(rs)
        if n < 15:
            continue
        hit = sum(1 for r in rs if r["acierto"]) / n * 100
        precio_medio = sum(r["precio"] for r in rs) / n
        pnl_por_fila = [(1 - r["precio"] if r["acierto"] else -r["precio"]) for r in rs]
        ev = sum(pnl_por_fila) / n
        pnl_total = sum(pnl_por_fila)
        n_wallets = len({r["wallet"] for r in rs})
        pnl_por_wallet = Counter()
        for r, p in zip(rs, pnl_por_fila):
            pnl_por_wallet[r["wallet"]] += p
        top1_pnl = pnl_por_wallet.most_common(1)[0][1] if pnl_por_wallet else 0
        top1_pct = (top1_pnl / pnl_total * 100) if pnl_total > 0 else float("nan")
        print(f"  {activo:<5} {dur:>4}min: n={n:>4} hit={hit:>5.1f}% precio_medio={precio_medio:.3f} "
              f"EV/1USD={ev:+.3f} pnl_total={pnl_total:+7.2f} n_wallets={n_wallets:>2} top1={top1_pct:>5.0f}%")

    # Timing de solo las GANADORAS, por (activo, marco)
    print("\n=== Timing EXACTO de apuestas GANADORAS, por activo x marco (n>=15) ===")
    ganadoras = defaultdict(list)
    for r in resultados:
        if r["acierto"]:
            ganadoras[(r["activo"], r["dur_min"])].append(r["restante_min"])

    for (activo, dur), restantes in sorted(ganadoras.items(), key=lambda kv: -len(kv[1])):
        n = len(restantes)
        if n < 15:
            continue
        restantes_sorted = sorted(restantes)
        mediana = restantes_sorted[n // 2]
        p25 = restantes_sorted[n // 4]
        p75 = restantes_sorted[3 * n // 4]
        print(f"  {activo:<5} {dur:>4}min: n_ganadoras={n:>4} mediana_restante={mediana:>5.1f}min "
              f"p25={p25:>5.1f} p75={p75:>5.1f}")


if __name__ == "__main__":
    sys.exit(main() or 0)
