#!/usr/bin/env python3
"""f9: baja /activity (TRADE y REDEEM) de pspspsps5 en ventanas de 3 h, 2026-09-22..2026-10-07, sin sesgo de supervivencia (REDEEM incluye perdedoras con usdc 0). Guarda actividad.csv.gz"""
import requests, time, datetime as dt, pandas as pd
W = "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5"; s = requests.Session(); rows = []
t = int(dt.datetime(2026, 9, 22, tzinfo=dt.timezone.utc).timestamp()); tend = int(dt.datetime(2026, 10, 7, tzinfo=dt.timezone.utc).timestamp())
def get(ty, a, b):
    out = []; off = 0
    while True:
        for k in range(5):
            r = s.get("https://data-api.polymarket.com/activity", params=dict(user=W, limit=500, offset=off, start=a, end=b, type=ty, sortBy="TIMESTAMP", sortDirection="ASC"), timeout=30)
            if r.status_code == 200: break
            time.sleep(2 * (k + 1))
        else:
            print("fallo", ty, a, off, r.status_code, flush=True); return out
        j = r.json(); out += j; off += len(j)
        if len(j) < 500: break
        if off >= 3000: print("AVISO tope offset", ty, a, flush=True); break
        time.sleep(0.05)
    return out
while t < tend:
    for ty in ("TRADE", "REDEEM"):
        rows += get(ty, t, t + 10800)
    t += 10800
df = pd.DataFrame(rows)[["timestamp", "conditionId", "type", "size", "usdcSize", "price", "side", "slug", "outcome", "transactionHash"]]
df.to_csv("/root/polymarket-research-datalogs/wallet_pspspsps5/actividad.csv.gz", index=False, compression="gzip")
print(len(df), df.type.value_counts().to_dict())
