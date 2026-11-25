#!/usr/bin/env python3
"""Construye (solo lectura, red publica) un universo realista para medir el hijo: 5m (tokens de new_market_universo, <=2 h) + 15m y 60m
vigentes del CSV de hoy (solo su COLA, 8 MB) con tokens por gamma /markets/{id}. Salida: JSON {toks, claves, meta}. Uso: construir_universo.py <dir_universo_5m> <salida.json>"""
import csv, io, json, os, sys, time, requests
from datetime import datetime, timezone
sys.path.insert(0, "/root/polymarket-research"); sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "stage"))
import universo_5m_io as U
from shadow_predict import _parse_updown_tipo, identificar_activo
ahora = time.time()
toks, claves, meta = [], {}, {}
mk, st = U.leer(ahora, sys.argv[1])
n5 = 0
for mid, r in mk.items():
    if r["marco"] != "5m" or r["_cierre"] <= ahora or r["_cierre"] - 300 > ahora + 7200:
        continue
    a = r["activo"].upper(); edt = datetime.fromtimestamp(r["_cierre"], timezone.utc).isoformat()
    for t, lado in ((r["token_up"], "YES"), (r["token_down"], "NO")):
        toks.append(t); claves[t] = f"{a}#5min"; meta[t] = (a, "5min", mid, edt, lado)
    n5 += 1
f = "/root/polymarket-research/data/markets/%s.csv" % datetime.now(timezone.utc).strftime("%Y-%m-%d")
sz = os.path.getsize(f)
with open(f, "rb") as fh:
    fh.seek(max(0, sz - 8 * 1024 * 1024)); fh.readline(); cola = fh.read().decode("utf-8", "replace")
cab = open(f).readline()
vig = {}
for r in csv.DictReader(io.StringIO(cab + cola)):
    try:
        tipo, vent = _parse_updown_tipo(r["question"])
        a = identificar_activo(r["question"])
        edt = datetime.fromisoformat(r["end_date"]).replace(tzinfo=timezone.utc)
    except Exception:
        continue
    if tipo in ("slot", "hourly") and vent in (15, 60) and a in {"BTC", "ETH", "SOL", "XRP", "DOGE", "BNB"} and edt.timestamp() > ahora:
        vig[r["market_id"]] = (a, f"{vent}min", edt)
n15 = n60 = 0
for mid, (a, marco, edt) in vig.items():
    try:
        j = requests.get("https://gamma-api.polymarket.com/markets/" + mid, timeout=10).json()
        t = json.loads(j["clobTokenIds"]); o = json.loads(j["outcomes"]); d = dict(zip(o, t))
        up, dn = d["Up"], d["Down"]
    except Exception:
        continue
    for tk, lado in ((up, "YES"), (dn, "NO")):
        toks.append(tk); claves[tk] = f"{a}#{marco}"; meta[tk] = (a, marco, mid, edt.isoformat(), lado)
    n15 += marco == "15min"; n60 += marco == "60min"
    time.sleep(0.3)
json.dump({"toks": toks, "claves": claves, "meta": meta}, open(sys.argv[2], "w"))
print(json.dumps({"mercados_5m": n5, "mercados_15m": n15, "mercados_60m": n60, "tokens": len(toks)}))
