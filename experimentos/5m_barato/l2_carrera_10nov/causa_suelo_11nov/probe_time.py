#!/usr/bin/env python3
"""Sondeo SOLO LECTURA: GET /time (CLOB) y /api/v3/time (Binance) sobre UNA conexion keep-alive.
Guarda t_send/t_first_byte/t_done (ns, reloj local UTC) y el sello del servidor. Uso: probe_time.py host path n intervalo_s salida.json"""
import sys, time, ssl, json, http.client, random
host, path, n, iv, out = sys.argv[1], sys.argv[2], int(sys.argv[3]), float(sys.argv[4]), sys.argv[5]
ctx = ssl.create_default_context()
t0 = time.time_ns(); c = http.client.HTTPSConnection(host, timeout=10, context=ctx); c.connect(); t1 = time.time_ns()
rows = []
for i in range(n):
    ts = time.time_ns()
    c.putrequest('GET', path, skip_accept_encoding=True); c.putheader('User-Agent', 'probe-ro/1'); c.putheader('Accept', '*/*'); c.endheaders()
    r = c.getresponse(); tf = time.time_ns(); body = r.read(); td = time.time_ns()
    rows.append(dict(ts=ts, tf=tf, td=td, status=r.status, body=body.decode()[:200], date=r.getheader('date'), cf=r.getheader('cf-ray')))
    time.sleep(iv * (0.5 + random.random()))        # fase aleatoria respecto al segundo del servidor
json.dump(dict(host=host, path=path, connect_ms=(t1 - t0) / 1e6, rows=rows), open(out, 'w'))
print(host, 'n', len(rows), 'connect_ms', (t1 - t0) / 1e6)
