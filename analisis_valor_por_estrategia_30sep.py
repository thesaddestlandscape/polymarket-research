#!/usr/bin/env python3
"""analisis_valor_por_estrategia_30sep.py -- ¿las variables que separan a las tomadoras ganadoras
(valor frente al subyacente y lado a favor del subyacente) separan también las señales buenas y
malas de CADA una de nuestras estrategias? (Javi 30-Sep: "¿afecta a todas nuestras estrategias?")

Por señal con ASK REAL (ask_real_por_senal.csv, 21 días, el mismo que usa el 4º veto):
  z      = signo_del_lado * ln(S_t / S_apertura) / (sigma_1s * sqrt(segundos restantes))
           S = precio spot (data/prices, ~1 por minuto), sigma de los 30 min previos
  valor  = Phi(z) - ask real del lado comprado
Se reporta EV por € al ask real (fee 7 % sobre la ganancia, igual que ask_real_por_senal.py) por
estrategia x marco, para: todas las señales; lado A FAVOR (z>=0,5) / EN CONTRA (z<=-0,5) del
subyacente; y tramos de valor. Marca de tiempo de la señal = prediction_timestamp (puede ir
decenas de segundos por detrás de la decisión real: ruido, no mirada al futuro).
Solo lectura. Salida: data/shadow/valor_por_estrategia.json
"""
import bisect, csv, glob, gzip, json, math, random, statistics as st, sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
REPO = Path(__file__).resolve().parent
FEE = 0.07; DUR = {"5min": 300, "15min": 900, "60min": 3600}
def ts(s): return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
def phi(x): return 0.5 * (1 + math.erf(x / math.sqrt(2)))
def main():
    S = {}
    with open(REPO / "data/shadow/ask_real_por_senal.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["ask"] and r["acierto"] in ("0", "1"):
                S[(r["strategy"], r["market_id"], r["decision"])] = [r["prediction_timestamp"], float(r["ask"]), int(r["acierto"]), None, None]
    print("señales con ask real:", len(S), flush=True)
    with open(REPO / "data/shadow/results.csv", encoding="utf-8") as f:
        rd = csv.reader(f); h = next(rd); ix = {c: h.index(c) for c in ("strategy", "market_id", "decision", "subtype", "end_date")}
        for row in rd:
            k = (row[ix["strategy"]], row[ix["market_id"]], row[ix["decision"]])
            v = S.get(k)
            if v is not None and v[3] is None: v[3], v[4] = row[ix["subtype"]], row[ix["end_date"]]
    PX = defaultdict(lambda: ([], []))
    for p in sorted(glob.glob(str(REPO / "data/prices/2026-09-*.csv*"))):
        if "chainlink" in p or "polybolt" in p or "kalshi" in p: continue
        f = gzip.open(p, "rt", encoding="utf-8") if p.endswith(".gz") else open(p, encoding="utf-8")
        with f:
            for r in csv.DictReader(f):
                try: PX[r["asset"]][0].append(ts(r["timestamp_utc"])); PX[r["asset"]][1].append(float(r["price_usd"]))
                except (ValueError, TypeError, KeyError): pass
    def px(a, t, tol=150):
        pt, pv = PX[a]; i = bisect.bisect_right(pt, t) - 1
        return pv[i] if i >= 0 and t - pt[i] <= tol else None
    sig = {}
    def sigma(a, t):
        k = (a, int(t) // 300)
        if k not in sig:
            xs = [px(a, t - 1800 + 60 * j) for j in range(31)]; xs = [x for x in xs if x]
            rs = [math.log(y / x) for x, y in zip(xs, xs[1:])]
            sig[k] = st.pstdev(rs) / math.sqrt(60) if len(rs) >= 15 else None
        return sig[k]
    G = defaultdict(lambda: defaultdict(lambda: defaultdict(list))); usadas = 0
    for (strat, mid_, dec), (pt, ask, ac, sub, end) in S.items():
        if not sub or not end or "#" not in sub or not 0.03 <= ask < 0.97: continue
        act, marco = sub.split("#")[:2]
        if marco not in DUR: continue
        try: t, fin = ts(pt), ts(end)
        except ValueError: continue
        resto = fin - t
        if resto < 5 or resto > DUR[marco] + 120: continue
        s_t, s_0, sg1 = px(act, t), px(act, fin - DUR[marco]), sigma(act, t)
        if not (s_t and s_0 and sg1): continue
        z = (1 if dec == "BUY_YES" else -1) * math.log(s_t / s_0) / (sg1 * math.sqrt(resto)); val = phi(z) - ask
        pnl = (1 - ask) / ask * (1 - FEE) if ac else -1.0
        usadas += 1; d = pt[:10]
        cortes = ["todas", "lado A FAVOR (z>=0,5)" if z >= 0.5 else "lado EN CONTRA (z<=-0,5)" if z <= -0.5 else "lado neutro",
                  "valor < -0,10" if val < -0.10 else "valor -0,10..0,03" if val < 0.03 else "valor 0,03..0,10" if val < 0.10 else "valor >= 0,10"]
        for c in cortes: G[(strat, marco)][c][d].append((pnl, ac, ask))
    print("señales usadas:", usadas)
    def res(vd):
        x = [y for v in vd.values() for y in v]
        if len(x) < 40: return None
        ks = list(vd); rng = random.Random(4); ms = []
        for _ in range(600):
            s = [y[0] for k in (rng.choice(ks) for _ in ks) for y in vd[k]]; ms.append(sum(s) / len(s))
        ms.sort()
        return dict(n=len(x), dias=len(ks), ask=round(sum(y[2] for y in x) / len(x), 3), hit=round(sum(y[1] for y in x) / len(x) * 100, 1),
                    ev=round(sum(y[0] for y in x) / len(x), 4), ic=[round(ms[30], 3), round(ms[570], 3)])
    orden = ["todas", "lado A FAVOR (z>=0,5)", "lado neutro", "lado EN CONTRA (z<=-0,5)", "valor >= 0,10", "valor 0,03..0,10", "valor -0,10..0,03", "valor < -0,10"]
    salida = {}
    for (strat, marco), cs in sorted(G.items(), key=lambda kv: -sum(len(v) for v in kv[1]["todas"].values())):
        base = res(cs["todas"])
        if not base or base["n"] < 300: continue
        print(f"\n{strat} {marco}")
        salida[f"{strat}#{marco}"] = {}
        for c in orden:
            r = res(cs.get(c, {}))
            if not r: continue
            salida[f"{strat}#{marco}"][c] = r
            marca = " ✅" if r["ic"][0] > 0 else " ❌" if r["ic"][1] < 0 else ""
            print(f"   {c:26s} n={r['n']:6d} días={r['dias']:2d} ask {r['ask']:.3f} hit {r['hit']:5.1f}% EV/€ {r['ev']:+.4f} IC90 ({r['ic'][0]:+.3f},{r['ic'][1]:+.3f}){marca}")
    (REPO / "data/shadow/valor_por_estrategia.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    return 0
if __name__ == "__main__": sys.exit(main())
