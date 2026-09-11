#!/usr/bin/env python3
"""
analisis_bot_wallets_universo_25ago.py -- amplía el universo de bot
wallets de 8 (top por volumen) a TODAS las que cumplen el heurístico de
bot dentro del conjunto con edge confirmado (petición Javi 25-Ago: "no
cojas solo las 8, coge las 50 wallets de bots que operen en crypto que
cumplan los criterios").

Heurístico de bot: trades/día > 20 (imposible para un humano de forma
sostenida) Y horas activas >= 20/24 (actividad 24/7, no un horario
humano). Aplicado sobre las 248 wallets con edge YA confirmado
(sig_bhfdr + g_kelly>0 + edge_pp>0 en wallet_edge_score_por_activo_marco.json)
-- no sobre el universo entero de wallets (eso incluiría wallets sin
edge validado, no accionable).

Solo lectura. No promociona nada por sí solo.
"""
import csv
import json
from collections import defaultdict
from datetime import datetime

WEDGE = json.load(open("data/shadow/wallet_edge_score_por_activo_marco.json"))


def wallets_con_edge_confirmado():
    sig = [v for v in WEDGE.values() if v.get("sig_bhfdr") and v.get("g_kelly", 0) > 0 and v.get("edge_pp", 0) > 0]
    wallets = {v["wallet"] for v in sig}
    print(f"combos con edge confirmado: {len(sig)} | wallets únicas: {len(wallets)}")
    return wallets


def cargar_historial(wallets: set):
    por_wallet = defaultdict(list)
    with open("data/shadow/ballenas_timing_history.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            w = r.get("wallet", "").lower()
            if w in wallets:
                por_wallet[w].append(r)
    return por_wallet


def es_bot(rows) -> dict | None:
    ts = []
    for r in rows:
        try:
            ts.append(datetime.fromisoformat(r["ts_trade"].replace("Z", "+00:00")))
        except (KeyError, ValueError):
            pass
    if len(ts) < 30:
        return None
    ts.sort()
    dias = max((ts[-1] - ts[0]).total_seconds() / 86400, 0.5)
    trades_dia = len(ts) / dias
    horas_activas = len({t.hour for t in ts})
    if trades_dia > 20 and horas_activas >= 20:
        return {"n": len(ts), "dias": round(dias, 1), "trades_dia": round(trades_dia, 1),
                "horas_activas": horas_activas}
    return None


def main():
    wallets = wallets_con_edge_confirmado()
    historial = cargar_historial(wallets)
    print(f"wallets con >=1 fila de historial: {len(historial)}")

    bots = {}
    for w, rows in historial.items():
        perfil = es_bot(rows)
        if perfil:
            bots[w] = perfil

    print(f"\nBOT WALLETS (trades/día>20, horas_activas>=20/24) dentro del universo con edge confirmado: {len(bots)}")
    for w, p in sorted(bots.items(), key=lambda kv: -kv[1]["trades_dia"]):
        print(f"  {w} n={p['n']} dias={p['dias']} trades_dia={p['trades_dia']} horas_activas={p['horas_activas']}")

    with open("data/shadow/bot_wallets_universo_25ago.json", "w", encoding="utf-8") as f:
        json.dump(bots, f, indent=1)
    print(f"\nGuardado en data/shadow/bot_wallets_universo_25ago.json")


if __name__ == "__main__":
    main()
