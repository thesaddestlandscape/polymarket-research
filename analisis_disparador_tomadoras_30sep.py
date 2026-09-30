#!/usr/bin/env python3
"""analisis_disparador_tomadoras_30sep.py -- ¿qué dispara a las tomadoras que ganan?

Para cada compra (lado L, instante de recepción t del trade en el firehose) se mide el movimiento
de Binance (mid de bookTicker, ~100 ms) en ventanas antes y después de t, con signo a favor del
lado comprado (Up = subida, Down = bajada), en puntos básicos. Si compran tras un movimiento de
Binance, el retorno con signo se concentra en las ventanas previas.
Grupos: tomadoras persistentes (universo), resto de wallets (control, 1 de cada 40 compras) y
nuestras entradas (Wallet Mirror y bots, instante de decisión del dry-run).
OJO: t es la hora de RECEPCIÓN del trade (el trade real ocurrió ~0,1-0,8 s antes).
Solo lectura. Uso: python3 analisis_disparador_tomadoras_30sep.py 2026-09-29
"""
import bisect, csv, gzip, json, statistics as st, sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
REPO = Path(__file__).resolve().parent; DATALOGS = Path("/root/polymarket-research-datalogs")
VENT = [(-10, -5), (-5, -3), (-3, -2), (-2, -1.5), (-1.5, -1), (-1, -0.5), (-0.5, 0), (0, 0.5), (0.5, 1), (1, 2), (2, 5)]
def ab(p): return gzip.open(p, "rt", encoding="utf-8") if str(p).endswith(".gz") else open(p, encoding="utf-8")
def ts(s): return datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()
def main():
    dia = sys.argv[1] if len(sys.argv) > 1 else "2026-09-29"
    B = defaultdict(lambda: ([], []))
    p = DATALOGS / f"binance_bookticker_{dia}.csv"; p = p if p.exists() else Path(str(p) + ".gz")
    with ab(p) as f:
        for r in csv.DictReader(f):
            try: B[r["activo"]][0].append(int(r["ts_recepcion_ms"]) / 1000); B[r["activo"]][1].append(float(r["mid"]))
            except (ValueError, TypeError): pass
    def mid(a, t):
        bt, bm = B[a]; i = bisect.bisect_right(bt, t) - 1
        return bm[i] if i >= 0 and t - bt[i] < 30 else None
    cob = {a: (len(v[0]), (v[0][-1] - v[0][0]) / 3600 if v[0] else 0) for a, v in B.items()}
    print("bookTicker:", {a: f"{n} puntos en {h:.1f} h" for a, (n, h) in cob.items()})
    U = set(json.loads((REPO / "data/shadow/tomadores_persistentes_universo.json").read_text())["wallets"])
    ev = defaultdict(list); visto = set(); k = 0
    pa = DATALOGS / f"polymarket_activity_{dia}.csv"; pa = pa if pa.exists() else Path(str(pa) + ".gz")
    with ab(pa) as f:
        for r in csv.DictReader(f):
            if r.get("categoria_updown_tracked") != "1" or r.get("marco") not in ("5min", "15min") or r["side"] != "BUY" or r["outcome"] not in ("Up", "Down"): continue
            w = r["wallet"].lower(); c = (w, r["market_slug"])
            if c in visto: continue
            visto.add(c)
            try: pr, t = float(r["price"]), ts(r["timestamp_utc"])
            except (ValueError, TypeError): continue
            if w in U: ev["tomadoras persistentes"].append((r["activo"], t, r["outcome"], pr))
            else:
                k += 1
                if k % 40 == 0: ev["resto de wallets (control)"].append((r["activo"], t, r["outcome"], pr))
    with open(REPO / "data/shadow/wallet_mirror_executor_dryrun.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["timestamp_utc"].startswith(dia) and r["marco"] in ("5min", "15min") and r["sigue_fillable_en_decision"] == "1":
                try: ev["NUESTRO Wallet Mirror (decisión)"].append((r["activo"], ts(r["timestamp_utc"]), r["mirror_lado"], float(r["ask_decision"])))
                except (ValueError, TypeError): pass
    with open(REPO / "data/shadow/dispersed_bot_executor_dryrun.csv", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["timestamp_utc"].startswith(dia) and r["marco"] in ("5min", "15min") and r["sigue_fillable"] in ("1", "True") and r["arquetipo"] in ("SNIPER", "DISPERSO"):
                try: ev[f"NUESTRO {r['arquetipo']} (detección)"].append((r["activo"], ts(r["timestamp_utc"]), r["lado_wallet"], float(r["mejor_ask_deteccion"])))
                except (ValueError, TypeError): pass
    print(f"\n{dia}: retorno de Binance CON SIGNO a favor del lado comprado, en puntos básicos, por ventana (s respecto a la recepción del trade)")
    print(f"{'grupo / precio':46s} {'n':>6s} | " + " ".join(f"[{a:g},{b:g}]".rjust(10) for a, b in VENT) + " | acum[-5,0]  %mov>2bps[-3,0]")
    for g in sorted(ev, key=lambda x: (x.startswith("NUESTRO"), x)):
        for nombre, lo, hi in (("todo", 0.05, 0.95), ("0,60-0,85", 0.60, 0.85), ("0,40-0,60", 0.40, 0.60), ("0,05-0,40", 0.05, 0.40)):
            E = [e for e in ev[g] if lo <= e[3] < hi and e[2] in ("Up", "Down")]
            if len(E) < 200: continue
            cols = []
            for a, b in VENT:
                d = []
                for act, t, o, _ in E:
                    m0, m1 = mid(act, t + a), mid(act, t + b)
                    if m0 and m1: d.append((m1 / m0 - 1) * 1e4 * (1 if o == "Up" else -1))
                cols.append(f"{st.mean(d):+.2f}".rjust(10) if len(d) >= 100 else "-".rjust(10))
            ac, mv = [], 0
            for act, t, o, _ in E:
                m0, m1, m3 = mid(act, t - 5), mid(act, t), mid(act, t - 3)
                if m0 and m1 and m3:
                    ac.append((m1 / m0 - 1) * 1e4 * (1 if o == "Up" else -1))
                    if (m1 / m3 - 1) * 1e4 * (1 if o == "Up" else -1) > 2: mv += 1
            print(f"{(g + ' ' + nombre)[:46]:46s} {len(E):6d} | " + " ".join(cols) + (f" | {st.mean(ac):+9.2f}  {mv / len(ac):14.0%}" if ac else ""))
    return 0
if __name__ == "__main__": sys.exit(main())
