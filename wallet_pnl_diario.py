#!/usr/bin/env python3
"""
wallet_pnl_diario.py — Track diario de ballenas crypto (10-Jul, petición Javi:
"quiero que le pongas un track diario a todas estas wallets... y busques
todas las ballenas que operan en crypto y hagas lo mismo").

Complementa smart_money_tracker.py, no lo sustituye: ese usa /positions para
descubrir wallets activas en NUESTROS mercados y calcula un consenso
direccional (feature ya probada y refutada como boost/veto, sigue solo
observacional). Este script usa /activity (TRADE+REDEEM cash-flow real) —
el mismo método que /positions NO puede dar bien: /positions solo retiene el
residuo SIN REDIMIR para wallets de alta frecuencia, así que su pnl_total
queda roto (verificado 10-Jul: sixx7/neversmiling/manual-large muestran
win_rate=0.0-0.002 exacto en n=248-500, firma del bug ya documentado en
hipotesis_custom.json 02-Jul). /activity da el flujo de caja REAL: BUY=-usdc,
SELL=+usdc, REDEEM=+usdc — sin ese sesgo.

Universo: unión de WALLETS_SEED (9 wallets caracterizadas a fondo el 10-Jul,
ver project_estudio_bots_ganadores_10jul) + direcciones únicas del leaderboard
CRYPTO más reciente (data/wallets/leaderboard_YYYY-MM-DD.csv, ya capturado
por capture_wallets.py vía run_slow.sh, category=CRYPTO, top75 por PNL+VOL).//
No hace falta descubrir ballenas desde cero: el leaderboard YA es la fuente
oficial y verificada de "todas las ballenas que operan en crypto".

Salida: data/shadow/ballenas_diario.csv, una fila por wallet por día
(append, nunca sobrescribe) — permite ver persistencia/decaimiento del edge
a lo largo del tiempo, no solo una foto puntual (que puede coincidir con una
mala racha de una wallet genuinamente buena, como pasó hoy con neversmiling).

Cadencia recomendada: 1x/día (cron), pull pesado por wallet (paginado,
~90 wallets × hasta 3000 eventos c/u). NO toca dinero, solo lectura pública.
"""
import csv
import json
import re
import statistics as st
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import requests

DIR = Path(__file__).resolve().parent
DIR_WALLETS = DIR / "data" / "wallets"
OUT = DIR / "data" / "shadow" / "ballenas_diario.csv"
DATA_API = "https://data-api.polymarket.com"
TIMEOUT = 25
MAX_EVENTOS_POR_WALLET = 3000  # ~1 día a semanas según actividad; ver caveat en memoria
DUR_RE = re.compile(r'-updown-(\d+)m-(\d+)$')

# Las 9 wallets caracterizadas a fondo el 10-Jul (ver project_estudio_bots_
# ganadores_10jul.md) — se incluyen SIEMPRE aunque salgan del leaderboard del
# día, para no perder continuidad de la serie temporal de las ya estudiadas.
WALLETS_SEED = {
    "0x20d2309cd92b797ae7ca175ed828ed8a27fbe29d": "sin_nombre_20d2",
    "0xee55214ee3a9ee22a404663c76ca832577df7b04": "sixx7",
    "0x48ac40fc545cf327edd5365435c3a9f385614a7e": "BoneOhio",
    "0xfcdc071df7080c214196bb0b3b751e5417f9d8e3": "neversmiling",
    "0xe3eeb127d5763a6e4ad597f773f9d259c94d5176": "sin_nombre_e3ee",
    "0x0479be41c67b588ece5bdc8913beb2adb3ca8177": "cybermaxs",
    "0x3deac23f85896126e9fc8134247a643092087b7b": "EvanChance",
    "0x0d7dfb4f0299335c81991c8c011df5d7cebb15c0": "manual-large",
    "0xdc8923aa7d6b293af2974c521092d0026ac37ac3": "sin_nombre_dc89",
}

CAMPOS = [
    "fecha", "wallet", "nombre", "pnl_neto", "roi_sobre_comprado",
    "buy_usd", "sell_usd", "redeem_usd", "buy_n", "sell_n", "redeem_n",
    "pct_maker", "mercados_unicos", "span_h", "trades_por_mercado_mediana",
    "precio_buy_mediana", "pct_precio_lt010", "pct_precio_045_055",
    "pct_precio_gte070", "seg_ventana_restante_pct_mediana",
    "en_leaderboard_hoy", "pnl_leaderboard_rank",
]


def wallets_del_leaderboard_hoy() -> dict:
    """{address_lower: (username, rank_combined)} de la captura más reciente
    del leaderboard CRYPTO de hoy. Vacío si no hay fichero (fail-soft: el
    script sigue con solo WALLETS_SEED)."""
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    archivo = DIR_WALLETS / f"leaderboard_{fecha}.csv"
    if not archivo.exists():
        print(f"  [aviso] sin leaderboard de hoy ({archivo}) — solo WALLETS_SEED", file=sys.stderr)
        return {}
    rows = list(csv.DictReader(open(archivo, encoding="utf-8")))
    if not rows:
        return {}
    ultimo_ts = max(r["timestamp_utc"] for r in rows)
    out = {}
    for r in rows:
        if r["timestamp_utc"] != ultimo_ts:
            continue
        addr = (r.get("address") or "").lower()
        if addr:
            out[addr] = (r.get("username", ""), r.get("rank_combined", ""))
    return out


def fetch_activity(wallet: str, max_events: int = MAX_EVENTOS_POR_WALLET) -> list:
    evs = []
    offset = 0
    while len(evs) < max_events:
        try:
            r = requests.get(f"{DATA_API}/activity",
                             params={"user": wallet, "limit": 500, "offset": offset},
                             timeout=TIMEOUT)
            r.raise_for_status()
        except Exception as e:
            print(f"  [error] {wallet[:12]} offset={offset}: {e}", file=sys.stderr)
            break
        chunk = r.json()
        if not chunk:
            break
        evs.extend(chunk)
        if len(chunk) < 500:
            break
        offset += 500
        time.sleep(0.15)
    return evs


def analizar(wallet: str, nombre: str, eventos: list) -> dict | None:
    trades = [e for e in eventos if e.get("type") == "TRADE"]
    redeems = [e for e in eventos if e.get("type") == "REDEEM"]
    if not trades and not redeems:
        return None

    cash = buy_usd = sell_usd = redeem_usd = 0.0
    buy_n = sell_n = 0
    diffs_fee = []
    for t in trades:
        u = float(t.get("usdcSize", 0) or 0)
        p = float(t.get("price", 0) or 0)
        s = float(t.get("size", 0) or 0)
        if t.get("side") == "BUY":
            cash -= u; buy_usd += u; buy_n += 1
        else:
            cash += u; sell_usd += u; sell_n += 1
        nominal = p * s
        if nominal > 0:
            diffs_fee.append(abs(u - nominal) / nominal)
    for r in redeems:
        cash += float(r.get("usdcSize", 0) or 0)
        redeem_usd += float(r.get("usdcSize", 0) or 0)

    pct_maker = (sum(1 for d in diffs_fee if d < 0.001) / len(diffs_fee)) if diffs_fee else None

    buys = [t for t in trades if t.get("side") == "BUY"]
    precios = [t.get("price", 0) for t in buys]
    rem_pct = []
    for t in buys:
        m = DUR_RE.search(t.get("slug", "") or "")
        if not m:
            continue
        dur_min, start_ts = int(m.group(1)), int(m.group(2))
        remaining = start_ts + dur_min * 60 - t["timestamp"]
        rem_pct.append(remaining / (dur_min * 60))

    all_ts = [e["timestamp"] for e in eventos]
    span_h = (max(all_ts) - min(all_ts)) / 3600 if all_ts else 0

    mercados = Counter(t.get("conditionId") for t in trades)
    tpm = list(mercados.values())

    n_precios = len(precios) or 1
    return dict(
        wallet=wallet, nombre=nombre,
        pnl_neto=round(cash, 2),
        roi_sobre_comprado=round(cash / buy_usd, 4) if buy_usd else None,
        buy_usd=round(buy_usd, 1), sell_usd=round(sell_usd, 1),
        redeem_usd=round(redeem_usd, 1),
        buy_n=buy_n, sell_n=sell_n, redeem_n=len(redeems),
        pct_maker=round(pct_maker, 3) if pct_maker is not None else None,
        mercados_unicos=len(mercados), span_h=round(span_h, 1),
        trades_por_mercado_mediana=round(st.median(tpm), 1) if tpm else None,
        precio_buy_mediana=round(st.median(precios), 3) if precios else None,
        pct_precio_lt010=round(sum(1 for p in precios if p < 0.10) / n_precios, 3),
        pct_precio_045_055=round(sum(1 for p in precios if 0.45 <= p < 0.55) / n_precios, 3),
        pct_precio_gte070=round(sum(1 for p in precios if p >= 0.70) / n_precios, 3),
        seg_ventana_restante_pct_mediana=round(st.median(rem_pct), 3) if rem_pct else None,
    )


def main():
    fecha = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lb = wallets_del_leaderboard_hoy()
    universo = dict(WALLETS_SEED)
    for addr, (username, rank) in lb.items():
        universo.setdefault(addr, username or addr[:10])
    print(f"[{fecha}] universo total: {len(universo)} wallets "
          f"({len(WALLETS_SEED)} seed + {len(lb)} leaderboard hoy)")

    nuevo = not OUT.exists()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    filas = []
    for i, (wallet, nombre) in enumerate(universo.items(), 1):
        evs = fetch_activity(wallet)
        r = analizar(wallet, nombre, evs)
        if r is None:
            continue
        r["fecha"] = fecha
        r["en_leaderboard_hoy"] = int(wallet in lb)
        r["pnl_leaderboard_rank"] = lb.get(wallet, ("", ""))[1]
        filas.append(r)
        if i % 10 == 0:
            print(f"  {i}/{len(universo)} procesadas...", file=sys.stderr)
        time.sleep(0.2)

    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS)
        if nuevo:
            w.writeheader()
        for r in filas:
            w.writerow({k: r.get(k, "") for k in CAMPOS})

    ganadoras = sum(1 for r in filas if (r.get("pnl_neto") or 0) > 0)
    print(f"[{fecha}] {len(filas)} wallets analizadas — {ganadoras} con PnL neto positivo en la ventana muestreada")


if __name__ == "__main__":
    main()
