import pickle, math, random
from collections import defaultdict
D = pickle.load(open("U.pkl", "rb")); U, POP = D["U"], D["POP"]
OFFS = (500.0, 1000.0, 2000.0, 3000.0, 5000.0, 8000.0); KS = (5.0, 50.0, 200.0, 1e12)
CELLS = [(o, k) for o in OFFS for k in KS]
days = sorted({k[2] for k in U})
cd = defaultdict(lambda: [0.0, 0.0, 0])  # (cell,dia)
for (o, k, d, m, l), (c, p) in U.items():
    x = cd[((o, k), d)]; x[0] += c; x[1] += p; x[2] += 1
pd_ = defaultdict(lambda: [0.0, 0.0, 0])
for (d, m, l), (c, p) in POP.items():
    x = pd_[d]; x[0] += c; x[1] += p; x[2] += 1
def ev(c, p): return p / c if c > 0 else float("nan")
print("dia      POP_BTC_banda(n)      R5K 5000/K50 (n)   exceso   5000/Kinf   8000/K50")
for d in days:
    P = pd_[d]; R = cd[((5000.0, 50.0), d)]; I = cd[((5000.0, 1e12), d)]; E = cd[((8000.0, 50.0), d)]
    print(f"{d} {ev(P[0],P[1]):+.3f}({P[2]:4d})  {ev(R[0],R[1]):+.3f}({R[2]:3d})  {ev(R[0],R[1])-ev(P[0],P[1]):+.3f}  {ev(I[0],I[1]):+.3f}  {ev(E[0],E[1]):+.3f}({E[2]})")
# correlacion diaria R5K vs poblacion 06-16
ds = [d for d in days if "2026-10-06" <= d <= "2026-10-16"]
a = [ev(*pd_[d][:2]) for d in ds]; b = [ev(*cd[((5000.0, 50.0), d)][:2]) for d in ds]
ma, mb = sum(a)/len(a), sum(b)/len(b)
r = sum((x-ma)*(y-mb) for x, y in zip(a, b)) / math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))
print("corr diaria pob vs R5K 06-16:", round(r, 3))
# --- walk-forward del PROCEDIMIENTO de seleccion
def agg(cell, dd):
    c = sum(cd[(cell, d)][0] for d in dd); p = sum(cd[(cell, d)][1] for d in dd); n = sum(cd[(cell, d)][2] for d in dd)
    return c, p, n
def pick(dd, rule):
    best = None
    for cell in CELLS:
        c, p, n = agg(cell, dd)
        if c <= 0: continue
        e = p / c
        s = e if rule == "maxEV_n30d" and n >= 30*len(dd) else (e*math.sqrt(n) if rule == "tstat" else None)
        if rule == "maxEV_n30d" and n < 30*len(dd): continue
        if s is None: continue
        if best is None or s > best[0]: best = (s, cell)
    return best[1]
full = [d for d in days if "2026-10-06" <= d <= "2026-10-16"]
for rule in ("maxEV_n30d", "tstat"):
    for scheme in ("adelante", "atras", "LODO"):
        tot = [0.0, 0.0, 0]; fixed = [0.0, 0.0, 0]; out = []
        tests = full[3:] if scheme == "adelante" else (full[:-3] if scheme == "atras" else full)
        for t in tests:
            if scheme == "adelante": tr = [d for d in full if d < t]
            elif scheme == "atras": tr = [d for d in full if d > t]
            else: tr = [d for d in full if d != t]
            cell = pick(tr, rule); c, p, n = cd[(cell, t)]
            tot[0] += c; tot[1] += p; tot[2] += n
            f = cd[((5000.0, 50.0), t)]; fixed[0] += f[0]; fixed[1] += f[1]
            out.append(f"{t[5:]}:{int(cell[0])}/{cell[1]:g}:{ev(c,p):+.2f}")
        print(f"{rule:10s} {scheme:8s} OOS-de-la-seleccion EV {ev(tot[0],tot[1]):+.3f} n={tot[2]} | R5K fija mismos dias {ev(fixed[0],fixed[1]):+.3f} | " + " ".join(out))
# celdas elegidas con 06-16 aplicadas a 05, 17, 18
for rule in ("maxEV_n30d", "tstat"):
    cell = pick(full, rule)
    print(rule, "elige con 06-16:", cell, " 05:", "%+.3f" % ev(*cd[(cell,"2026-10-05")][:2]), " 17:", "%+.3f" % ev(*cd[(cell,"2026-10-17")][:2]), " 18:", "%+.3f" % ev(*cd[(cell,"2026-10-18")][:2]))
# placebo de dosis-respuesta: exceso de cada celda sobre poblacion, por dia, signo
print("dias con exceso R5K(5000/K50) > poblacion:", sum(1 for d in days if ev(*cd[((5000.0,50.0),d)][:2]) > ev(*pd_[d][:2])), "/", len(days))
# IC por cierre para 5000/K50 en 05+17+18 juntos (fuera del descubrimiento)
fin = defaultdict(lambda: [0.0, 0.0])
for (o, k, d, m, l), (c, p) in U.items():
    if (o, k) == (5000.0, 50.0) and d in ("2026-10-05", "2026-10-17", "2026-10-18"):
        x = fin[m]; x[0] += c; x[1] += p
ks = list(fin); random.seed(1); bs = []
for _ in range(2000):
    s = [fin[random.choice(ks)] for _ in ks]; bs.append(sum(x[1] for x in s)/sum(x[0] for x in s))
bs.sort(); C = sum(x[0] for x in fin.values()); Pp = sum(x[1] for x in fin.values())
print(f"R5K fuera de descubrimiento (05 parcial+17+18): n_merc={len(ks)} coste {C:.0f} EV {Pp/C:+.3f} IC90 cierre ({bs[100]:+.3f},{bs[1900]:+.3f})")
