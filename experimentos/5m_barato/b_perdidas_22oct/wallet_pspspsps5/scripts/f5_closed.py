#!/usr/bin/env python3
"""f5: baja /closed-positions (data-api publica) de pspspsps5 hasta 2026-09-01; guarda closed.csv.gz"""
import requests, time, pandas as pd, sys
W = "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5"; s = requests.Session(); rows = []; off = 0; stop = 1788220800  # 2026-09-01
while True:
    for k in range(4):
        r = s.get("https://data-api.polymarket.com/closed-positions", params=dict(user=W, limit=50, offset=off, sortBy="TIMESTAMP", sortDirection="DESC"), timeout=30)
        if r.status_code == 200: break
        time.sleep(2 * (k + 1))
    else:
        print("fallo", off, r.status_code); break
    j = r.json()
    if not j: break
    rows += j; off += 50
    if j[-1]["timestamp"] < stop: break
    time.sleep(0.05)
df = pd.DataFrame(rows)[["conditionId", "asset", "avgPrice", "totalBought", "realizedPnl", "slug", "outcome", "timestamp", "endDate"]]
df.to_csv("/root/polymarket-research-datalogs/wallet_pspspsps5/closed.csv.gz", index=False, compression="gzip")
print(len(df), df.timestamp.min(), df.timestamp.max())
