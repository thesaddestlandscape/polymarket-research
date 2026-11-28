#!/usr/bin/env python3
"""diagnostico_latencia_p1b_28nov.py RUN_DIR [RUN_DIR ...] [--q-file F] [--out J]

TAREA 0 (28-Nov): separa, para cada run de paquete_l/P1b (ledger.jsonl + cancel_evid/*.jsonl), TRES componentes de latencia que el informe_final mezcla:
  (1) HTTP: t_ack - t_send del POST (alta) y del DELETE (baja), medido en el propio proceso (reloj monotono local). Por moneda.
  (2) SELLO DE EVENTO DEL EXCHANGE vs ACK HTTP: ts_ex(PLACEMENT|CANCELLATION del canal de usuario) - t_ack. En condiciones normales (13-Nov B2/B3/B5) es ~ -25 ms (el sello cae ANTES del ack).
      Positivo = el exchange publica el evento DESPUES de haber contestado por HTTP (lag de publicacion del canal de usuario; la POST ya devuelve status 'live'): NO es red ni reloj nuestros.
  (3) RECEPCION: t_recv - ts_ex (WS de usuario). Estable (~17-19 ms) => ni la red de vuelta ni el lector local se retrasan.
Opcional --q-file (lineas `t_ms,token` de filas q del registro ms, ver comando en la nota): correlacion Spearman entre el ack HTTP y la tasa de eventos del libro del token en el segundo previo al envio (carga del mercado).
Opcional --d-file (lineas `t_ms,token,precio,tamano,rx` de filas `d` del libro5_ms: lado B, nivel 0.01; comando en la nota): TESTIGO INDEPENDIENTE del efecto real en el libro. Nuestra orden (5 acc a 0,01) se ve como un salto de +5,00 (alta) / -5,00 (baja) en el tamano del nivel;
su sello del canal de MERCADO (t_ms) da la hora a la que el exchange cambio el libro, sin pasar por el canal de usuario. Se publica por moneda: alta_mercado_ex_menos_envio, cancel_mercado_ex_menos_envio, y la diferencia con el sello del canal de usuario. Atribucion por salto exacto: en libros muy activos (BTC) puede haber coincidencias falsas (se declara).
SOLO LEE ficheros. 0 red, 0 ordenes, no importa paquete_l ni ejecutor alguno. No sustituye a analiza_p1b.py (que no se toca: sus pins/hashes valen para P1b)."""
import argparse
import bisect
import collections
import glob
import json
import statistics as st
import sys


def cuantil(x, p):
    x = sorted(x)
    return None if not x else x[min(len(x) - 1, int(p * len(x)))]


def resumen(x):
    return None if not x else dict(n=len(x), p10=cuantil(x, .1), p50=cuantil(x, .5), p90=cuantil(x, .9))


def rangos(v):
    o = sorted(range(len(v)), key=lambda k: v[k]); r = [0] * len(v)
    for j, k in enumerate(o):
        r[k] = j
    return r


def spearman(a, b):
    if len(a) < 5 or len(a) != len(b):
        return None
    return round(st.correlation(rangos(a), rangos(b)), 3)


def leer_run(d):
    """-> (intenciones{oid:coin,tok}, posts{oid:fila}, cancels{oid:fila intento 1 ok}, eventos{(tipo,oid):fila}). Filas corruptas se cuentan, no se ignoran en silencio."""
    I, P, C, E, corruptas = {}, {}, {}, {}, 0
    for l in open(d + "/ledger.jsonl"):
        try:
            r = json.loads(l)
        except ValueError:
            corruptas += 1; continue
        k = r.get("k")
        if k == "intencion":
            I[r["oid_local"]] = r
        elif k == "post" and r.get("t_send_ns") and r.get("t_ack_ns") and r.get("clase") == "ok":
            P[r["oid_local"]] = r
        elif k == "cancel" and r.get("ok") and r.get("intento") == 1 and r.get("t_ack_ns"):
            C[r["oid"]] = r
    for f in sorted(glob.glob(d + "/cancel_evid/*.jsonl")):
        for l in open(f):
            try:
                r = json.loads(l)
            except ValueError:
                corruptas += 1; continue
            if r.get("k") == "user_order" and r.get("mine") and r.get("tipo") in ("PLACEMENT", "CANCELLATION"):
                E[(r["tipo"], r["oid"])] = r
    return I, P, C, E, corruptas


def salto(a, t0, t1, delta, tol=0.006):
    """Primer cambio de tamano del nivel (lista [(t_ms, size, rx)] ordenada) con |delta_size - delta| < tol en [t0, t1]. -> fila o None."""
    for i in range(1, len(a)):
        if t0 <= a[i][0] <= t1 and abs((a[i][1] - a[i - 1][1]) - delta) < tol:
            return a[i]
    return None


def lee_d(path):
    rows = collections.defaultdict(list)
    for l in open(path):
        t, tok, _p, sz, rx = l.strip().split(",")
        rows[tok].append((int(t), float(sz), int(rx)))
    for v in rows.values():
        v.sort()
    return rows


def analiza(d, q_file=None, d_file=None):
    I, P, C, E, corruptas = leer_run(d)
    g = collections.defaultdict(lambda: collections.defaultdict(list))
    ev = None
    if q_file:
        ev = collections.defaultdict(list)
        for l in open(q_file):
            t, tok = l.strip().split(",", 1); ev[tok].append(int(t))
        for v in ev.values():
            v.sort()
    acks, tasas = [], []
    dm = lee_d(d_file) if d_file else None
    for oid, p in P.items():
        i = I.get(oid)
        if not i:
            continue
        c = i["coin"]; ts = p["t_send_ns"] / 1e6; ta = p["t_ack_ns"] / 1e6
        for k in ("TODAS", c):
            g[k]["post_http_ms"].append(ta - ts)
        pl = E.get(("PLACEMENT", oid))
        if pl:
            for k in ("TODAS", c):
                g[k]["place_ex_menos_ack_ms"].append(pl["ts_ex_ms"] - ta)
                g[k]["place_recv_menos_ex_ms"].append(pl["t_recv_ms"] - pl["ts_ex_ms"])
        cx = C.get(oid)
        if cx:
            for k in ("TODAS", c):
                g[k]["delete_http_ms"].append((cx["t_ack_ns"] - cx["t_send_ns"]) / 1e6)
            ca = E.get(("CANCELLATION", oid))
            if ca:
                for k in ("TODAS", c):
                    g[k]["cancel_ex_menos_ack_ms"].append(ca["ts_ex_ms"] - cx["t_ack_ns"] / 1e6)
                    g[k]["cancel_ex_menos_envio_ms"].append(ca["ts_ex_ms"] - cx["t_send_ns"] / 1e6)
        if dm is not None:
            pm = salto(dm.get(i["tok"], []), ts - 20, ts + 3500, 5.0)
            if pm:
                for k in ("TODAS", c):
                    g[k]["alta_mercado_ex_menos_envio_ms"].append(pm[0] - ts)
                    g[k]["alta_mercado_ex_menos_ack_ms"].append(pm[0] - ta)
                    if pl: g[k]["alta_mercado_ex_menos_usuario_ex_ms"].append(pm[0] - pl["ts_ex_ms"])
            cx2 = C.get(oid)
            cm = salto(dm.get(i["tok"], []), cx2["t_send_ns"] / 1e6 - 20, cx2["t_send_ns"] / 1e6 + 3500, -5.0) if cx2 else None
            if cm:
                ca2 = E.get(("CANCELLATION", oid))
                for k in ("TODAS", c):
                    g[k]["cancel_mercado_ex_menos_envio_ms"].append(cm[0] - cx2["t_send_ns"] / 1e6)
                    g[k]["cancel_mercado_ex_menos_ack_ms"].append(cm[0] - cx2["t_ack_ns"] / 1e6)
                    if ca2: g[k]["cancel_mercado_ex_menos_usuario_ex_ms"].append(cm[0] - ca2["ts_ex_ms"])
        if ev is not None and i.get("tok") in ev:
            a = ev[i["tok"]]; t = int(ts)
            acks.append(ta - ts); tasas.append(bisect.bisect_right(a, t) - bisect.bisect_left(a, t - 1000))
    out = dict(run=d, filas_corruptas=corruptas, n_posts=len(P), por_moneda={})
    for k, m in g.items():
        out["por_moneda"][k] = {n: resumen(v) for n, v in m.items()}
        # fraccion de eventos publicados DESPUES del ack HTTP (lag de publicacion; normal = 0)
        for n in ("place_ex_menos_ack_ms", "cancel_ex_menos_ack_ms"):
            v = m.get(n)
            if v:
                out["por_moneda"][k][n.replace("_ms", "_frac_pos")] = dict(n=len(v), frac_gt0=round(sum(1 for x in v if x > 0) / len(v), 3), frac_gt100=round(sum(1 for x in v if x > 100) / len(v), 3))
    if ev is not None:
        out["spearman_ack_vs_tasa_q_1s"] = dict(n=len(acks), rho=spearman(acks, tasas))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("runs", nargs="+"); ap.add_argument("--q-file"); ap.add_argument("--d-file"); ap.add_argument("--out")
    ns = ap.parse_args(argv)
    res = [analiza(d, ns.q_file, ns.d_file) for d in ns.runs]
    txt = json.dumps(res, indent=1, sort_keys=True)
    if ns.out:
        open(ns.out, "w").write(txt)
    for r in res:
        print("==", r["run"], "posts", r["n_posts"], "corruptas", r["filas_corruptas"])
        for k in ("TODAS", "BTC", "ETH", "SOL", "XRP"):
            m = r["por_moneda"].get(k)
            if m:
                print(k, {n: (None if v is None else ("%s/%s/%s" % (v.get("p10"), v.get("p50"), v.get("p90")) if "p50" in v else v)) for n, v in m.items()})
        if "spearman_ack_vs_tasa_q_1s" in r:
            print("spearman ack~tasa", r["spearman_ack_vs_tasa_q_1s"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
