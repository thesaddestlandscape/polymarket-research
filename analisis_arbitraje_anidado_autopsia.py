#!/usr/bin/env python3
"""analisis_arbitraje_anidado_autopsia.py -- autopsia del arbitraje anidado de 2 patas (06-Oct, Javi: "encontrar la
causa raíz del fracaso del arbitraje anidado"; solo diagnóstico, nada de soluciones).

Fuentes:
  1) arbitraje_anidado_dryrun_*.csv(.gz) (02-Oct en adelante): oportunidad detectada (asks, tamaños, EDAD de cada
     cotización, neto) y, por latencia fija 150..1000 ms, si una FOK simultánea al precio detectado habría llenado
     ambas / solo_A / solo_B / ninguna.
  2) maker_ms_*.csv.gz (desde 05-Oct ~15:40Z): top del libro de cada token en cada cambio de precio o tamaño
     (filas q, hora del exchange y de recepción) y TODAS las operaciones (filas t). Con eso, para cada pata:
     SUPERVIVENCIA = ms desde la detección hasta que el nivel detectado deja de servir (ask sube por encima del
     precio detectado, o queda < shares a ese precio), y CAUSA de la desaparición:
        consumida  = hubo operaciones a ese precio en la ventana (otro tomador se la llevó)
        cancelada  = el tamaño cayó / el nivel desapareció SIN operaciones (el maker retiró la cotización)
        sobrevive  = sigue viva a +2 s.
Unidad = oportunidad única (par, moneda, cierre, pata A), primera detección (como el análisis oficial).
Clases (a la latencia L): TRUE_ARB (ambas llenas), PARTIAL (solo una), FAILED (ninguna), INVALID (sin desenlace
oficial, tamaño < 5 shares o datos incoherentes). LATE_LEG no existe con FOK simultáneas (no hay relleno tardío);
se informa en su lugar si la pata que faltaba podía COMPLETARSE al top de t+L con neto aún >0 (neto_top_L).
DIRECTIONAL = el PnL de las PARTIAL (pata suelta valorada con desenlace oficial): se reporta SIEMPRE aparte.
IDEAL = las dos patas al precio detectado en el instante de detección (pago garantizado >= 1).
Uso: python3 analisis_arbitraje_anidado_autopsia.py [--lat 250]
"""
import argparse
import bisect
import collections
import csv
import glob
import gzip
import statistics as st
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from analisis_maker_cancelacion_binance import desenlaces  # noqa: E402

DL = "/root/polymarket-research-datalogs"
LATS_CSV = [150, 200, 250, 300, 400, 600, 1000]
CURVA_MS = [25, 50, 75, 100, 150, 200, 250, 300, 400, 500, 1000]
HORIZ_MS = 2000


def fee(p):
    return 0.07 * p * (1 - p)


def cargar_oportunidades():
    filas = []
    for f in sorted(glob.glob(f"{DL}/arbitraje_anidado_dryrun_*.csv*")):
        op = gzip.open if f.endswith(".gz") else open
        with op(f, "rt") as fh:
            filas += list(csv.DictReader(fh))
    vistas, ops = set(), []
    for r in sorted(filas, key=lambda r: int(r["ts_ms"])):
        k = (r["par"], r["activo"], r["fin"], r["pata_A"])
        if k in vistas:
            continue
        vistas.add(k)
        ops.append(r)
    return ops


def pago(pata, r, des):
    lado, cual = pata.split("_")
    res = des.get(r["market_" + cual])
    if res is None:
        return None
    return 1.0 if (res == "YES") == (lado == "Up") else 0.0


def cargar_ms(mercados):
    """{(market_id, lado YES/NO): {'q': ([t_recv], [(ask, asz)]), 't': [(t, precio)]}} solo para esos mercados."""
    tok2 = {}
    q = collections.defaultdict(lambda: ([], []))
    t = collections.defaultdict(list)
    for f in sorted(glob.glob(f"{DL}/maker_ms_*.csv.gz")):
        try:
            with gzip.open(f, "rt") as fh:
                for ln in fh:
                    c = ln.rstrip("\n").split(",")
                    tp = c[0]
                    if tp == "k":
                        if c[5] in mercados:
                            tok2[c[2]] = (c[5], c[7])
                    elif tp == "q":
                        k = tok2.get(c[2])
                        if k:
                            a = q[k]
                            a[0].append(int(c[7]) if len(c) > 7 and c[7] else int(c[1]))
                            ask = None if c[4] in ("", "None") else float(c[4])
                            asz = 0.0 if c[6] in ("", "None") else float(c[6])
                            a[1].append((ask, asz))
                    elif tp == "t":
                        k = tok2.get(c[2])
                        if k:
                            t[k].append((int(c[6]) if len(c) > 6 and c[6] else int(c[1]), float(c[3])))
        except (EOFError, OSError):
            pass
    for k, (ts, vs) in q.items():
        o = sorted(range(len(ts)), key=ts.__getitem__)
        q[k] = ([ts[i] for i in o], [vs[i] for i in o])
    for k in t:
        t[k].sort()
    return q, t


def supervivencia(qk, tk, t0, precio, shares):
    """(ms hasta que el nivel deja de servir o None si sobrevive HORIZ_MS, causa, cubierto)."""
    ts, vs = qk
    i = bisect.bisect_right(ts, t0) - 1
    if i < 0 or t0 - ts[i] > 30_000:
        return None, "sin_dato", False
    for j in range(i, len(ts)):
        if ts[j] > t0 + HORIZ_MS:
            break
        ask, asz = vs[j]
        if j > i and (ask is None or ask > precio + 1e-9 or (abs(ask - precio) < 1e-9 and asz < shares)):
            dt = ts[j] - t0
            tr = [x for x in tk if t0 - 50 <= x[0] <= ts[j] + 50 and x[1] >= precio - 1e-9]
            return dt, ("consumida" if tr else "cancelada"), True
    return None, "sobrevive", True


def resumen_clase(nombre, xs):
    if not xs:
        print(f"  {nombre:12} n=0")
        return
    pn = [x for x in xs]
    acum, pico, dd = 0.0, 0.0, 0.0
    for v in pn:
        acum += v
        pico = max(pico, acum)
        dd = max(dd, pico - acum)
    print(f"  {nombre:12} n={len(pn):3}  PnL {sum(pn):+8.2f} $  expectancy {st.mean(pn):+7.3f} $  "
          f"gana {sum(v > 0 for v in pn) / len(pn):4.0%}  DD máx {dd:6.2f} $")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lat", type=int, default=250)
    a = ap.parse_args()
    ops = cargar_oportunidades()
    des = desenlaces({r[k] for r in ops for k in ("market_largo", "market_corto")})
    L = str(a.lat)
    print(f"oportunidades únicas: {len(ops)} ({ops[0]['ts_ms'] and ''}días {sorted({__import__('datetime').datetime.utcfromtimestamp(int(r['ts_ms']) / 1000).date().isoformat() for r in ops})})")

    # ---------- 1-2. clasificación y PnL por clase (fuente 1), a la latencia pedida ----------
    clases = collections.defaultdict(list)
    ideal, real, invalid = [], [], collections.Counter()
    capital = []
    for r in ops:
        sh = float(r["shares"])
        aA, aB = float(r["ask_A"]), float(r["ask_B"])
        pA, pB = pago(r["pata_A"], r, des), pago(r["pata_B"], r, des)
        if pA is None or pB is None:
            invalid["sin_desenlace"] += 1
            continue
        if sh < 5:
            invalid["shares<5"] += 1
            continue
        if f"fill_{L}" not in r or not r[f"fill_{L}"]:
            invalid[f"sin_latencia_{L}_en_csv"] += 1
            continue
        if pA + pB < 1:
            invalid["garantia_rota"] += 1
        coste_A, coste_B = aA + fee(aA), aB + fee(aB)
        v_ideal = sh * (pA + pB - coste_A - coste_B)
        f_ = r[f"fill_{L}"]
        if f_ == "ambas":
            v = v_ideal
        elif f_ == "solo_A":
            v = sh * (pA - coste_A)
        elif f_ == "solo_B":
            v = sh * (pB - coste_B)
        else:
            v = 0.0
        clase = {"ambas": "TRUE_ARB", "solo_A": "PARTIAL", "solo_B": "PARTIAL", "ninguna": "FAILED"}[f_]
        clases[clase].append(v)
        ideal.append(v_ideal)
        real.append(v)
        capital.append(sh * (coste_A + coste_B))
    print(f"\n== 1-2. Clasificación a {L} ms (fuente: dry-run, FOK simultáneas al precio detectado) ==")
    print(f"  INVALID: {dict(invalid)}")
    for c in ("TRUE_ARB", "PARTIAL", "FAILED"):
        resumen_clase(c, clases[c])
    print(f"  DIRECTIONAL (= PnL de las PARTIAL, pata suelta con desenlace oficial): {sum(clases['PARTIAL']):+.2f} $")
    print(f"  capital comprometido por oportunidad: mediana {st.median(capital):.1f} $, máx {max(capital):.1f} $")
    tot_ideal = sum(ideal)
    print(f"  IDEAL (ambas al precio detectado, instante 0): {tot_ideal:+.2f} $ en {len(ideal)} ops "
          f"(media {st.mean(ideal):+.3f} $) | REAL a {L} ms: {sum(real):+.2f} $ | EXECUTION GAP {tot_ideal - sum(real):+.2f} $")
    if tot_ideal > 0:
        print(f"  alpha que queda solo con TRUE_ARB: {sum(clases['TRUE_ARB']):+.2f} $ = "
              f"{sum(clases['TRUE_ARB']) / tot_ideal:.0%} del ideal; se pierde el {1 - sum(clases['TRUE_ARB']) / tot_ideal:.0%}")

    # ---------- 5 (versión discreta). curva por latencia (fuente 1) ----------
    print("\n== 5a. Curva de viabilidad (fuente: dry-run, 7 latencias) ==")
    for lat in LATS_CSV:
        k = f"fill_{lat}"
        vs = [r for r in ops if r.get(k) and float(r["shares"]) >= 5 and pago(r["pata_A"], r, des) is not None
              and pago(r["pata_B"], r, des) is not None]
        if not vs:
            continue
        amb = [r for r in vs if r[k] == "ambas"]
        cond = [float(r["shares"]) * (pago(r["pata_A"], r, des) + pago(r["pata_B"], r, des) - float(r["ask_A"])
                - fee(float(r["ask_A"])) - float(r["ask_B"]) - fee(float(r["ask_B"]))) for r in amb]
        print(f"  {lat:5} ms  n={len(vs):3}  P(ambas)={len(amb) / len(vs):5.1%}  E[neto | ambas]="
              f"{(st.mean(cond) if cond else 0):+7.3f} $  E[neto TRUE-ARB incondicional]={sum(cond) / len(vs):+7.3f} $")

    # ---------- 3-5. microestructura ms (fuente 2) ----------
    mercados = {r[k] for r in ops for k in ("market_largo", "market_corto")}
    q, t = cargar_ms(mercados)
    surv = []
    for r in ops:
        sh = float(r["shares"])
        if sh < 5:
            continue
        t0 = int(r["ts_ms"])
        fila = {"r": r}
        for pata, ask in (("A", float(r["ask_A"])), ("B", float(r["ask_B"]))):
            lado, cual = r[f"pata_{pata}"].split("_")
            k = (r["market_" + cual], "YES" if lado == "Up" else "NO")
            if k not in q:
                fila[pata] = (None, "sin_dato", False)
                continue
            fila[pata] = supervivencia(q[k], t.get(k, []), t0, ask, sh)
        if fila["A"][2] and fila["B"][2]:
            surv.append(fila)
    print(f"\n== 3-4. Supervivencia de cada pata en ms (fuente: registro ms; cubiertas {len(surv)} de {len(ops)} ops) ==")
    if surv:
        for pata in ("A", "B"):
            d = [f[pata][0] for f in surv if f[pata][0] is not None]
            c = collections.Counter(f[pata][1] for f in surv)
            qs = sorted(d)
            pr = (lambda p: qs[min(len(qs) - 1, int(len(qs) * p))]) if qs else (lambda p: None)
            print(f"  pata {pata}: muere en {len(d)}/{len(surv)} (<{HORIZ_MS} ms) | P50 {pr(.5)} P75 {pr(.75)} P90 {pr(.9)} "
                  f"P95 {pr(.95)} P99 {pr(.99)} máx {qs[-1] if qs else None} ms | causas {dict(c)}")
        dmin = []
        for f in surv:
            a_, b_ = f["A"][0], f["B"][0]
            dmin.append(min(x for x in (a_, b_, 10 ** 9) if x is not None))
        print("  edad al detectar (ms) — pata A mediana "
              f"{st.median(int(f['r']['edad_A_ms']) for f in surv)}, pata B mediana {st.median(int(f['r']['edad_B_ms']) for f in surv)}")
        quien = collections.Counter()
        for f in surv:
            a_, b_ = f["A"][0], f["B"][0]
            if a_ is None and b_ is None:
                quien["ninguna muere"] += 1
            else:
                prim = "A" if (b_ is None or (a_ is not None and a_ <= b_)) else "B"
                ea, eb = int(f["r"]["edad_A_ms"]), int(f["r"]["edad_B_ms"])
                vieja = "A" if ea > eb else "B"
                quien[f"muere primero la {'VIEJA' if prim == vieja else 'NUEVA'} ({f[prim][1]})"] += 1
        print(f"  ¿qué pata muere primero? {dict(quien)}")
        print("\n== 5b. Curva continua (fuente: registro ms) P(ambas vivas en t0+L) ==")
        for Lm in CURVA_MS:
            ok = [f for f in surv if all((f[p][0] is None or f[p][0] > Lm) for p in ("A", "B"))]
            v = []
            for f in ok:
                r = f["r"]
                pA, pB = pago(r["pata_A"], r, des), pago(r["pata_B"], r, des)
                if pA is None or pB is None:
                    continue
                v.append(float(r["shares"]) * (pA + pB - float(r["ask_A"]) - fee(float(r["ask_A"])) - float(r["ask_B"])
                                                - fee(float(r["ask_B"]))))
            print(f"  {Lm:5} ms  P(ambas)={len(ok) / len(surv):5.1%}  E[neto|ambas]={(st.mean(v) if v else 0):+7.3f} $  "
                  f"E[TRUE-ARB incond.]={sum(v) / len(surv):+7.3f} $")
    neto = sorted(float(r["neto"]) for r in ops)
    print(f"\n== Tamaño del edge detectado: neto por share P50 {neto[len(neto) // 2]:.4f}  P90 {neto[int(len(neto) * .9)]:.4f} "
          f"máx {neto[-1]:.4f} | beneficio ideal por op P50 {st.median(float(r['beneficio_usd']) for r in ops):.2f} $ ==")


if __name__ == "__main__":
    main()
