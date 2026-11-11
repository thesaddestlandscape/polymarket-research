import httpx, time, json, random, numpy as np, sys
fam = sys.argv[1] if len(sys.argv) > 1 else 'any'
kw = {}
if fam == '4': kw['transport'] = httpx.HTTPTransport(http2=True, local_address='0.0.0.0')
elif fam == '6': kw['transport'] = httpx.HTTPTransport(http2=True, local_address='::')
else: kw['http2'] = True
c = httpx.Client(**kw)
c.get('https://clob.polymarket.com/time')
a = []
for i in range(150):
    t = time.perf_counter(); r = c.get('https://clob.polymarket.com/time', headers={'User-Agent': 'probe-ro/1'}); a.append((time.perf_counter() - t) * 1000)
    time.sleep(0.15 + 0.3 * random.random())
a = np.array(a); print(fam, r.http_version, 'n', len(a), 'p10/p50/p90 ms', np.percentile(a, [10, 50, 90]).round(1), 'min', a.min().round(1))
