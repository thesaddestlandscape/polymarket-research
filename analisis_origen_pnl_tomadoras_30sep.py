#!/usr/bin/env python3
"""analisis_origen_pnl_tomadoras_30sep.py -- ¿de dónde sale el dinero de las tomadoras persistentes?
(Javi 30-Sep: "encuentra la respuesta": el 81 % de sus compras no sigue a un movimiento de Binance.)

Para CADA compra de las wallets del universo (no solo la primera; ponderado por dólares) en up/down
5/15 min se calculan, con datos anteriores al trade:
  bin   : movimiento de Binance en los 3 s previos a favor del lado comprado (bps)
  mom   : cambio del precio de ese lado en Polymarket en los ~5 s previos (c): precio - mediana de trades [-7,-3] s
  z     : ventaja del lado comprado según el subyacente = signo * ln(S_t/S_apertura) / (sigma_1s * sqrt(resto))
          (S = mid de Binance; sigma de los últimos 300 s). z>0: compran el lado que va ganando.
  valor : probabilidad justa Phi(z) menos precio pagado (¿compran barato respecto al justo?).
  precio, segundos restantes, tamaño, nº de compra en ese mercado.
y el resultado bruto de la compra a resolución ($) y su fee estimado de tomador.
Salida: reparto del volumen y del PnL por tramos de cada variable y por una clasificación
excluyente del motivo de la compra. Solo lectura.
Uso: python3 analisis_origen_pnl_tomadoras_30sep.py 2026-09-28 2026-09-29
"""
import bisect, csv, gzip, json, math, statistics as st, sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
REPO = Path(__file__).resolve().parent; DATALOGS = Path("/root/polymarket-research-datalogs")
def ab(p): return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")
def ruta(d, pre, dia):
    for c in (d / f"{pre}_{dia}.csv", d / f"{pre}_{dia}.csv.gz"):
        if c.exists(): return c
def ts(s): return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
def phi(x): return 0.5 * (1 + math.erf(x / math.sqrt(2)))
def main():
    dias = sys.argv[1:] or ["2026-09-28", "2026-09-29"]
    U = set(json.loads((REPO / "data/shadow/tomadores_persistentes_universo.json").read_text())["wallets"])
    F = []
    for dia in dias:
        out = {}
        with ab(ruta(REPO / "data/shadow", "resolution_sniper_obs", dia)) as f:
            for r in csv.DictReader(f):
                if r.get("outcome_real") in ("Up", "Down"): out[r["slug"]] = r["outcome_real"]
        B = defaultdict(lambda: ([], []))
        with ab(ruta(DATALOGS, "binance_bookticker", dia)) as f:
            for r in csv.DictReader(f):
                try: B[r["activo"]][0].append(int(r["ts_recepcion_ms"]) / 1000); B[r["activo"]][1].append(float(r["mid"]))
                except (ValueError, TypeError): pass
        def mid(a, t, tol=20):
            bt, bm = B[a]; i = bisect.bisect_right(bt, t) - 1
            return bm[i] if i >= 0 and t - bt[i] < tol else None
        sig = {}
        def sigma(a, t):
            k = (a, int(t) // 60)
            if k not in sig:
                xs = [mid(a, t - 300 + 5 * j) for j in range(61)]; xs = [x for x in xs if x]
                rs = [math.log(y / x) for x, y in zip(xs, xs[1:])]
                sig[k] = (st.pstdev(rs) / math.sqrt(5)) if len(rs) >= 30 else None     # por segundo
            return sig[k]
        P = defaultdict(list); compras = []; nth = defaultdict(int)
        with ab(ruta(DATALOGS, "polymarket_activity", dia)) as f:
            for r in csv.DictReader(f):
                if r.get("categoria_updown_tracked") != "1" or r.get("marco") not in ("5min", "15min") or r["market_slug"] not in out or r["outcome"] not in ("Up", "Down"): continue
                try: p, t, s = float(r["price"]), ts(r["timestamp_utc"]), float(r["size"])
                except (ValueError, TypeError): continue
                if not 0 < p < 1 or s <= 0: continue
                P[r["market_slug"]].append((t, p if r["outcome"] == "Up" else 1 - p))
                w = r["wallet"].lower()
                if w in U and r["side"] == "BUY":
                    nth[(w, r["market_slug"])] += 1
                    compras.append((r["market_slug"], t, r["outcome"], p, s, r["activo"], r["marco"], nth[(w, r["market_slug"])], w))
        T = {}
        for sl in P: P[sl].sort(); T[sl] = [x[0] for x in P[sl]]
        for slug, t, o, p, s, act, marco, n, w in compras:
            dur = 300 if marco == "5min" else 900
            try: ini = int(slug.rsplit("-", 1)[1])
            except ValueError: continue
            resto = ini + dur - t
            sg = 1 if o == "Up" else -1
            m0, m3, mo = mid(act, t), mid(act, t - 3), mid(act, ini, tol=60)
            binm = (m0 / m3 - 1) * 1e4 * sg if m0 and m3 else None
            a, b = bisect.bisect_left(T[slug], t - 7), bisect.bisect_right(T[slug], t - 3)
            mom = None
            if b > a:
                x = st.median(u for _, u in P[slug][a:b]); mom = (p - (x if o == "Up" else 1 - x)) * 100
            z = val = None
            sg1 = sigma(act, t)
            if m0 and mo and sg1 and resto > 1:
                z = sg * math.log(m0 / mo) / (sg1 * math.sqrt(resto)); val = phi(z) - p
            gana = 1 if out[slug] == o else 0
            F.append(dict(usd=s * p, pnl=s * (gana - p), fee=0.07 * p * (1 - p) * s, p=p, resto=resto, marco=marco, act=act, n=n, bin=binm, mom=mom, z=z, val=val, gana=gana, dia=dia, w=w))
        print(dia, "compras del universo:", len(compras), flush=True)
    V = sum(x["usd"] for x in F); PN = sum(x["pnl"] for x in F); FE = sum(x["fee"] for x in F)
    print(f"\nTOTAL: {len(F)} compras, {V:,.0f} $ | bruto {PN:,.0f} $ ({PN / V * 100:+.2f}% del vol) | fee estimado si todo fuese tomador {FE:,.0f} $ ({FE / V * 100:.2f}%)")
    def tabla(titulo, clave, orden=None):
        g = defaultdict(list)
        for x in F: g[clave(x)].append(x)
        print(f"\n== {titulo} ==\n{'tramo':26s} {'%vol':>6s} {'precio':>6s} {'hit':>6s} {'bruto $':>9s} {'%bruto/vol':>10s} {'neto tras fee %':>15s} {'%del PnL':>8s}  días+")
        for k in (orden or sorted(g)):
            v = g.get(k)
            if not v: continue
            vol = sum(x["usd"] for x in v); pn = sum(x["pnl"] for x in v); fe = sum(x["fee"] for x in v)
            dp = [sum(x["pnl"] - x["fee"] for x in v if x["dia"] == d) for d in dias]
            print(f"{str(k):26s} {vol / V * 100:6.1f} {sum(x['p'] * x['usd'] for x in v) / vol:6.3f} {sum(x['gana'] * x['usd'] for x in v) / vol:6.1%} {pn:9.0f} {pn / vol * 100:+10.2f} {(pn - fe) / vol * 100:+15.2f} {pn / PN * 100:8.0f}  {sum(1 for y in dp if y > 0)}/{len(dias)}")
    def tr(v, cortes, fmt):
        if v is None: return "sin dato"
        for c in cortes:
            if v < c: return fmt.format(c)
        return f">= {cortes[-1]}"
    tabla("precio pagado", lambda x: tr(x["p"], (0.2, 0.4, 0.6, 0.8, 0.9), "< {}"), ["< 0.2", "< 0.4", "< 0.6", "< 0.8", "< 0.9", ">= 0.9"])
    tabla("segundos restantes", lambda x: tr(x["resto"], (15, 30, 60, 120, 240), "< {}"), ["< 15", "< 30", "< 60", "< 120", "< 240", ">= 240"])
    tabla("marco", lambda x: x["marco"])
    tabla("moneda", lambda x: x["act"])
    tabla("z del lado comprado (subyacente)", lambda x: tr(x["z"], (-1, 0, 0.5, 1, 2, 3), "< {}"), ["< -1", "< 0", "< 0.5", "< 1", "< 2", "< 3", ">= 3", "sin dato"])
    tabla("valor: Phi(z) - precio", lambda x: tr(x["val"], (-0.10, -0.03, 0.03, 0.10), "< {}"), ["< -0.1", "< -0.03", "< 0.03", "< 0.1", ">= 0.1", "sin dato"])
    tabla("Binance 3 s previos a favor (bps)", lambda x: tr(x["bin"], (-2, -0.5, 0.5, 2), "< {}"), ["< -2", "< -0.5", "< 0.5", "< 2", ">= 2", "sin dato"])
    tabla("momentum Polymarket 5 s previos (c)", lambda x: tr(x["mom"], (-2, -0.5, 0.5, 2, 5), "< {}"), ["< -2", "< -0.5", "< 0.5", "< 2", "< 5", ">= 5", "sin dato"])
    tabla("nº de compra en el mercado", lambda x: "1ª" if x["n"] == 1 else "2ª-5ª" if x["n"] <= 5 else "6ª-20ª" if x["n"] <= 20 else ">20ª", ["1ª", "2ª-5ª", "6ª-20ª", ">20ª"])
    def motivo(x):
        if x["resto"] < 30 and x["p"] >= 0.8: return "1 cierre: favorito >=0,80 con <30 s"
        if x["bin"] is not None and x["bin"] >= 2: return "2 sigue a Binance (>=2 bps/3 s)"
        if x["mom"] is not None and x["mom"] >= 2: return "3 sigue al precio de Polymarket (>=2c/5 s)"
        if x["z"] is not None and x["z"] >= 1 and x["p"] >= 0.6: return "4 favorito del subyacente (z>=1)"
        if x["z"] is not None and x["z"] < 0: return "5 contra el subyacente (z<0)"
        return "6 resto"
    tabla("MOTIVO (clasificación excluyente, en este orden)", motivo)
    # concentración: ¿cuántas wallets hacen el PnL?
    pw = defaultdict(float)
    for x in F: pw[x["w"]] += x["pnl"] - x["fee"]
    o = sorted(pw.values(), reverse=True); tot = sum(o)
    print(f"\nconcentración del neto: {len(o)} wallets; top 5 = {sum(o[:5]):,.0f} $ de {tot:,.0f} $; con neto>0: {sum(1 for v in o if v > 0)}")
    return 0
if __name__ == "__main__": sys.exit(main())
