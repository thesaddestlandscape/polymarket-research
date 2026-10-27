#!/usr/bin/env python3
"""f4: valida on-chain vs data-api /activity de un dia UTC (solo lectura, publico). Uso: f4 YYYY-MM-DD"""
import sys, requests, datetime as dt, collections, re
W = "0xb0f85baa97990910a3e8ac2b4a58a322f01ecef5"
d = sys.argv[1]; t0 = int(dt.datetime.fromisoformat(d).replace(tzinfo=dt.timezone.utc).timestamp()); t1 = t0 + 86400
rows = []; off = 0; s = requests.Session()
while True:
    r = s.get("https://data-api.polymarket.com/activity", params=dict(user=W, limit=500, offset=off, start=t0, end=t1, type="TRADE", sortBy="TIMESTAMP", sortDirection="ASC"), timeout=30)
    if r.status_code != 200: print("status", r.status_code, r.text[:100], "offset", off); break
    j = r.json()
    if not j: break
    rows += j; off += len(j)
    if len(j) < 500 or off >= 3500: break
print(d, "trades", len(rows))
c = collections.Counter(); v = collections.Counter(); sd = collections.Counter()
for x in rows:
    m = re.match(r"(\w+)-updown-(\w+)-", x["slug"]) or re.match(r"(\w+)-", x["slug"]); k = (m.group(1), m.group(2) if m.lastindex > 1 else "?")
    c[k] += 1; v[k] += x["usdcSize"]; sd[x["side"]] += 1
print(dict(c)); print({k: round(x) for k, x in v.items()}, dict(sd))
