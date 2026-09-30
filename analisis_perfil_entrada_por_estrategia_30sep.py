#!/usr/bin/env python3
"""analisis_perfil_entrada_por_estrategia_30sep.py -- ¿entramos ANTES, DURANTE o DESPUÉS del
movimiento de precio? Perfil del precio negociado alrededor de cada entrada (firehose de trades),
por estrategia, y comparado con las tomadoras que ganan (que entran con el precio subiendo
5,7 c en los 5 s previos y aún +1 c en los 1-2 s siguientes).

Por entrada (lado L, instante t, precio de entrada p): mediana del precio negociado de L en
ventanas [-30,-10] [-10,-5] [-5,-2] [-2,-0,5] antes y [+0,5,+2] [+2,+5] [+5,+15] [+15,+60]
después, menos p. "Antes" negativo = el precio venía subiendo hacia nuestra entrada;
"después" positivo = siguió a favor. Fuentes con marca de tiempo en ms:
 wallet_mirror_executor_dryrun.csv (ask_decision) y dispersed_bot_executor_dryrun.csv
 (mejor_ask_deteccion), más el universo de tomadoras persistentes como referencia.
Solo lectura. Uso: python3 analisis_perfil_entrada_por_estrategia_30sep.py 2026-09-29
"""
import bisect, csv, gzip, json, statistics as st, sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
REPO = Path(__file__).resolve().parent; DATALOGS = Path("/root/polymarket-research-datalogs")
VENT = [(-30, -10), (-10, -5), (-5, -2), (-2, -0.5), (0.5, 2), (2, 5), (5, 15), (15, 60)]
def ab(p): return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")
def ts(s): return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
def main():
    dia = sys.argv[1] if len(sys.argv) > 1 else "2026-09-29"
    out = {}
    for c in (REPO / f"data/shadow/resolution_sniper_obs_{dia}.csv",):
        with ab(c) as f:
            for r in csv.DictReader(f):
                if r.get("outcome_real") in ("Up", "Down"): out[r["slug"]] = r["outcome_real"]
    try: U = set(json.loads((REPO / "data/shadow/tomadores_persistentes_universo.json").read_text())["wallets"])
    except Exception: U = set()
    P = defaultdict(list); ev = defaultdict(list); visto = set()
    pa = DATALOGS / f"polymarket_activity_{dia}.csv"; pa = pa if pa.exists() else Path(str(pa) + ".gz")
    with ab(pa) as f:
        for r in csv.DictReader(f):
            if r["market_slug"] not in out or r["outcome"] not in ("Up", "Down"): continue
            try: p, t = float(r["price"]), ts(r["timestamp_utc"])
            except (ValueError, TypeError): continue
            if not 0 < p < 1: continue
            P[r["market_slug"]].append((t, p if r["outcome"] == "Up" else 1 - p))
            w = r["wallet"].lower()
            if w in U and r["side"] == "BUY" and (w, r["market_slug"]) not in visto:
                visto.add((w, r["market_slug"]))
                ev[f"REFERENCIA tomadoras persistentes#{r['marco']}"].append((r["market_slug"], t, r["outcome"], p))
    for s in P: P[s].sort()
    T = {s: [x[0] for x in v] for s, v in P.items()}
    with open(REPO / "data/shadow/wallet_mirror_executor_dryrun.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r["timestamp_utc"].startswith(dia) or r["market_slug"] not in out or r["sigue_fillable_en_decision"] != "1": continue
            try: ev[f"WALLET_MIRROR {r['tipo']}#{r['marco']}"].append((r["market_slug"], ts(r["timestamp_utc"]), r["mirror_lado"], float(r["ask_decision"])))
            except (ValueError, TypeError): continue
    with open(REPO / "data/shadow/dispersed_bot_executor_dryrun.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if not r["timestamp_utc"].startswith(dia) or r["market_slug"] not in out or r["sigue_fillable"] not in ("1", "True"): continue
            try: ev[f"{r['arquetipo']}#{r['marco']}"].append((r["market_slug"], ts(r["timestamp_utc"]), r["lado_wallet"], float(r["mejor_ask_deteccion"])))
            except (ValueError, TypeError): continue
    print(f"{dia} | céntimos respecto al precio de entrada (mediana del precio negociado en cada ventana, en segundos)")
    print(f"{'estrategia':42s} {'n':>6s} {'hit':>5s} {'entrada':>7s} | " + " ".join(f"[{a:+g},{b:+g}]".rjust(11) for a, b in VENT) + " | EV/€")
    for k in sorted(ev, key=lambda k: (not k.startswith("REF"), k)):
        for nombre, lo, hi in (("todo", 0.05, 0.95), ("0,60-0,85", 0.60, 0.85), ("0,40-0,60", 0.40, 0.60), ("0,05-0,40", 0.05, 0.40)):
            E = [e for e in ev[k] if lo <= e[3] < hi and e[2] in ("Up", "Down")]
            if len(E) < 100: continue
            cols = []
            for a, b in VENT:
                d = []
                for s, t, o, p in E:
                    i = bisect.bisect_left(T[s], t + a); j = bisect.bisect_right(T[s], t + b)
                    if j > i:
                        x = st.median(u for _, u in P[s][i:j]); d.append((x if o == "Up" else 1 - x) - p)
                cols.append(f"{st.mean(d) * 100:+.2f}".rjust(11) if len(d) >= 50 else "-".rjust(11))
            hit = st.mean(1 if e[2] == out[e[0]] else 0 for e in E); pm = st.mean(e[3] for e in E)
            evv = st.mean((1 if e[2] == out[e[0]] else 0) / e[3] - 1 - 0.07 * (1 - e[3]) for e in E)
            print(f"{(k + ' ' + nombre)[:42]:42s} {len(E):6d} {hit:5.0%} {pm:7.3f} | " + " ".join(cols) + f" | {evv:+.3f}")
    return 0
if __name__ == "__main__": sys.exit(main())
