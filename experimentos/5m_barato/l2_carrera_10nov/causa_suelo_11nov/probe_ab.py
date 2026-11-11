import httpx, time, random, numpy as np
c4 = httpx.Client(transport=httpx.HTTPTransport(http2=True, local_address='0.0.0.0'))
c6 = httpx.Client(transport=httpx.HTTPTransport(http2=True, local_address='::'))
for c in (c4, c6): c.get('https://clob.polymarket.com/time')
a = {4: [], 6: []}
for i in range(300):
    for k, c in random.sample([(4, c4), (6, c6)], 2):
        t = time.perf_counter(); c.get('https://clob.polymarket.com/time'); a[k].append((time.perf_counter() - t) * 1000)
        time.sleep(0.1)
    time.sleep(0.2)
for k in (4, 6):
    x = np.array(a[k]); print('IPv%d' % k, 'n', len(x), 'p10/p50/p90', np.percentile(x, [10, 50, 90]).round(1), 'min', x.min().round(1))
d = np.array(a[6]) - np.array(a[4]); print('dif v6-v4 mediana pareada', np.median(d).round(2), 'IC90 bootstrap', np.percentile([np.median(np.random.choice(d, len(d))) for _ in range(2000)], [5, 95]).round(2))
