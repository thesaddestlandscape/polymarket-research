#!/usr/bin/env python3
"""Sondeo SOLO LECTURA: efecto del tiempo ocioso en la latencia de GET /time (CLOB) sobre conexion keep-alive (HTTP/1.1 via http.client)
y sobre conexion NUEVA. Para cada hueco: se espera, se envia 1 peticion en la persistente (tras 1 caliente de referencia) y 1 en conexion nueva."""
import time, ssl, json, http.client, sys
H = 'clob.polymarket.com'; ctx = ssl.create_default_context()
def req(c):
    ts = time.perf_counter(); c.putrequest('GET', '/time', skip_accept_encoding=True); c.putheader('User-Agent', 'probe-ro/1'); c.endheaders()
    r = c.getresponse(); tf = time.perf_counter(); r.read(); return (tf - ts) * 1000
def nueva():
    t0 = time.perf_counter(); c = http.client.HTTPSConnection(H, timeout=15, context=ctx); c.connect(); t1 = time.perf_counter(); l = req(c); c.close()
    return (t1 - t0) * 1000, l
gaps = [0.3, 0.3, 0.3, 2, 2, 2, 5, 5, 5, 10, 10, 10, 20, 20, 20, 40, 40, 40, 60, 60, 60, 90, 90, 90, 120, 120, 120, 180, 180, 240, 240, 300, 300]
pers = http.client.HTTPSConnection(H, timeout=15, context=ctx); pers.connect(); req(pers)
rows = []
for g in gaps:
    time.sleep(g)
    try: a = req(pers); err = None
    except Exception as e:
        err = type(e).__name__; pers = http.client.HTTPSConnection(H, timeout=15, context=ctx); pers.connect(); a = req(pers)
    cn, cl = nueva()
    rows.append(dict(gap=g, pers_ms=a, reconexion=err, nueva_connect_tls_ms=cn, nueva_first_ms=cl)); print(rows[-1], flush=True)
    req(pers) if g < 60 else None
json.dump(rows, open('idle_probe.json', 'w'))
