#!/usr/bin/env python3
"""analisis_flujo_tomador_vs_justo.py -- ¿quién paga de más y cuándo? El lado MAKER de cada ejecución (30-Sep, Javi:
"sabiendo lo que hacen las takers que ganan, sus ventajas y nuestras limitaciones, dame alfa").

Idea: las tomadoras que ganan lo hacen comprando con valor (justo - precio >= 0,10) justo tras un movimiento de
Binance, y en esa carrera un tomador lento no entra (taker delay de 150 ms + nuestros ~250 ms). Pero cada ejecución
tiene dos lados: si el flujo tomador que NO viene de un movimiento de Binance paga por encima del justo, el dinero
está en ser la contraparte de ESE flujo y retirarse cuando Binance se mueve.

Para cada ejecución con tomador identificable (transacción con >=3 filas en el firehose; el tomador es la fila cuyo
tamaño iguala la suma del resto) en up/down 5/15 min:
  lado y precio efectivos del tomador (VENDER X a p = comprar el contrario a 1-p),
  bin  = movimiento de Binance en los 1 s previos a favor del tomador (bps),
  val  = justo - precio pagado, con justo = Phi(z) del subyacente (mid Binance vs apertura, sigma 300 s),
  resultado del MAKER por acción = precio - pago del lado del tomador (sin comisión: el maker no paga).
Tablas ponderadas por acciones y por dólares del maker, con el resultado por día. Solo lectura.
Uso: analisis_flujo_tomador_vs_justo.py 2026-09-27 2026-09-28 2026-09-29
"""
import bisect
import csv
import gzip
import math
import statistics as st
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent
DATALOGS = Path("/root/polymarket-research-datalogs")


def ab(p):
    return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")


def ruta(d, pre, dia):
    for c in (d / f"{pre}_{dia}.csv", d / f"{pre}_{dia}.csv.gz"):
        if c.exists():
            return c


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()


def phi(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def main() -> int:
    dias = sys.argv[1:] or ["2026-09-27", "2026-09-28", "2026-09-29"]
    F = []
    for dia in dias:
        out = {}
        with ab(ruta(REPO / "data/shadow", "resolution_sniper_obs", dia)) as f:
            for r in csv.DictReader(f):
                if r.get("outcome_real") in ("Up", "Down"):
                    out[r["slug"]] = r["outcome_real"]
        B = defaultdict(lambda: ([], []))
        with ab(ruta(DATALOGS, "binance_bookticker", dia)) as f:
            for r in csv.DictReader(f):
                try:
                    B[r["activo"]][0].append(int(r["ts_recepcion_ms"]) / 1000)
                    B[r["activo"]][1].append(float(r["mid"]))
                except (ValueError, TypeError):
                    pass

        def mid(a, t, tol=20):
            bt, bm = B[a]
            i = bisect.bisect_right(bt, t) - 1
            return bm[i] if i >= 0 and t - bt[i] < tol else None
        sig = {}

        def sigma(a, t):
            k = (a, int(t) // 60)
            if k not in sig:
                xs = [x for x in (mid(a, t - 300 + 5 * j) for j in range(61)) if x]
                rs = [math.log(y / x) for x, y in zip(xs, xs[1:])]
                sig[k] = (st.pstdev(rs) / math.sqrt(5)) if len(rs) >= 30 else None
            return sig[k]

        def cerrar(tx):
            if len(tx) < 3:
                return
            sizes = [x[3] for x in tx]
            i = max(range(len(tx)), key=lambda k: sizes[k])
            resto_sz = sum(sizes) - sizes[i]
            if resto_sz <= 0 or abs(sizes[i] - resto_sz) / resto_sz >= 0.02:
                return
            slug, outcome, side, size, p, t, act, marco = tx[i]
            lado, q = (outcome, p) if side == "BUY" else ("Down" if outcome == "Up" else "Up", 1 - p)
            if not 0.02 <= q <= 0.98:
                return
            try:
                ini = int(slug.rsplit("-", 1)[1])
            except ValueError:
                return
            resto = ini + (300 if marco == "5min" else 900) - t
            if resto <= 0:
                return
            sg = 1 if lado == "Up" else -1
            m0, m1, mo = mid(act, t), mid(act, t - 1), mid(act, ini, tol=60)
            binm = (m0 / m1 - 1) * 1e4 * sg if m0 and m1 else None
            s1 = sigma(act, t)
            val = None
            if m0 and mo and s1:
                val = phi(sg * math.log(m0 / mo) / (s1 * math.sqrt(resto))) - q
            gana = 1 if out[slug] == lado else 0
            F.append((dia, act, marco, q, size, resto, binm, val, gana, side))
        tx, h_prev, n = [], None, 0
        with ab(ruta(DATALOGS, "polymarket_activity", dia)) as f:
            for r in csv.DictReader(f):
                if r.get("categoria_updown_tracked") != "1" or r.get("marco") not in ("5min", "15min") \
                        or r["market_slug"] not in out or r["outcome"] not in ("Up", "Down"):
                    continue
                try:
                    p, t, s = float(r["price"]), ts(r["timestamp_utc"]), float(r["size"])
                except (ValueError, TypeError):
                    continue
                if not 0 < p < 1 or s <= 0:
                    continue
                h = r["transaction_hash"]
                if h != h_prev:
                    cerrar(tx)
                    tx, h_prev = [], h
                tx.append((r["market_slug"], r["outcome"], r["side"], s, p, t, r["activo"], r["marco"]))
                n += 1
            cerrar(tx)
        print(f"{dia}: {n} filas up/down, {sum(1 for x in F if x[0] == dia)} ejecuciones con tomador identificado", flush=True)

    # resultado del maker: por acción = q - gana ; capital del maker por acción = 1 - q
    def tabla(titulo, clave, orden=None, filtro=lambda x: True):
        g = defaultdict(list)
        for x in F:
            if filtro(x):
                g[clave(x)].append(x)
        tot_acc = sum(x[4] for v in g.values() for x in v)
        print(f"\n== {titulo} ==\n{'tramo':24s} {'%acciones':>9s} {'ejec':>7s} {'precio_tom':>10s} {'gana_tom':>8s} {'maker c/acción':>14s} {'maker % s/capital':>17s}  por día (c/acción)")
        for k in (orden or sorted(g)):
            v = g.get(k)
            if not v:
                continue
            acc = sum(x[4] for x in v)
            pm = sum((x[3] - x[8]) * x[4] for x in v)
            cap = sum((1 - x[3]) * x[4] for x in v)
            pd = []
            for d in dias:
                vd = [x for x in v if x[0] == d]
                ad = sum(x[4] for x in vd)
                pd.append(f"{sum((x[3] - x[8]) * x[4] for x in vd) / ad * 100:+.2f}" if ad else "-")
            print(f"{str(k):24s} {acc / tot_acc * 100:9.1f} {len(v):7d} {sum(x[3] * x[4] for x in v) / acc:10.3f} {sum(x[8] * x[4] for x in v) / acc:8.3f} "
                  f"{pm / acc * 100:+14.2f} {pm / cap * 100:+17.2f}  {' '.join(pd)}")

    def tr(v, cortes):
        if v is None:
            return "sin dato"
        for c in cortes:
            if v < c:
                return f"< {c}"
        return f">= {cortes[-1]}"
    O = lambda cs: [f"< {c}" for c in cs] + [f">= {cs[-1]}", "sin dato"]
    cb, cv, cq, cr = (-2, -0.5, 0.5, 2), (-0.20, -0.10, -0.05, -0.02, 0.02, 0.05, 0.10, 0.20), (0.1, 0.3, 0.5, 0.7, 0.9), (15, 30, 60, 120, 240)
    print(f"\nTOTAL ejecuciones: {len(F)}; acciones {sum(x[4] for x in F):,.0f}; resultado maker {sum((x[3] - x[8]) * x[4] for x in F):,.0f} $")
    tabla("Binance 1 s previo a favor del tomador (bps)", lambda x: tr(x[6], cb), O(cb))
    tabla("valor del tomador: justo - precio pagado", lambda x: tr(x[7], cv), O(cv))
    calmo = lambda x: x[6] is not None and abs(x[6]) < 0.5
    tabla("valor del tomador, SOLO con Binance quieto (|1 s| < 0,5 bps)", lambda x: tr(x[7], cv), O(cv), calmo)
    tabla("precio pagado por el tomador, Binance quieto", lambda x: tr(x[3], cq), O(cq), calmo)
    tabla("segundos restantes, Binance quieto", lambda x: tr(x[5], cr), O(cr), calmo)
    paga_de_mas = lambda x: calmo(x) and x[7] is not None and x[7] < -0.05
    tabla("FLUJO QUE PAGA DE MÁS (Binance quieto y valor < -0,05): por marco", lambda x: x[2], None, paga_de_mas)
    tabla("... por moneda", lambda x: x[1], None, paga_de_mas)
    tabla("... por precio pagado", lambda x: tr(x[3], cq), O(cq), paga_de_mas)
    tabla("... por segundos restantes", lambda x: tr(x[5], cr), O(cr), paga_de_mas)
    tabla("... por tamaño de la ejecución (acciones)", lambda x: tr(x[4], (10, 50, 200, 1000)), O((10, 50, 200, 1000)), paga_de_mas)
    tabla("... compra directa o venta del contrario", lambda x: x[9], None, paga_de_mas)
    v = [x for x in F if paga_de_mas(x)]
    if v:
        nd = len(dias)
        print(f"\nvolumen diario de ese flujo: {sum(x[4] for x in v) / nd:,.0f} acciones/día, {sum(x[4] * x[3] for x in v) / nd:,.0f} $/día, "
              f"capital maker {sum(x[4] * (1 - x[3]) for x in v) / nd:,.0f} $/día, resultado maker {sum((x[3] - x[8]) * x[4] for x in v) / nd:,.0f} $/día")
    return 0


if __name__ == "__main__":
    sys.exit(main())
