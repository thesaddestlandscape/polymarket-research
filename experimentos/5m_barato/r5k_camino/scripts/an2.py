import pickle, random
from collections import defaultdict
D = pickle.load(open("U.pkl", "rb")); U, POP = D["U"], D["POP"]
pd_ = defaultdict(lambda: [0.0, 0.0])
for (d, m, l), (c, p) in POP.items(): pd_[d][0] += c; pd_[d][1] += p
ins = [f"2026-10-{x:02d}" for x in range(6, 17)]; out = ["2026-10-05", "2026-10-17", "2026-10-18"]
def cellday(cell, d):
    c = p = 0.0; n = 0
    for (o, k, dd, m, l), (cc, pp) in U.items():
        if (o, k) == cell and dd == d: c += cc; p += pp; n += 1
    return c, p, n
r5 = {d: cellday((5000.0, 50.0), d) for d in ins + out}
x = [pd_[d][1]/pd_[d][0] for d in ins]; y = [r5[d][1]/r5[d][0] for d in ins]
mx, my = sum(x)/len(x), sum(y)/len(y)
b = sum((a-mx)*(c-my) for a, c in zip(x, y))/sum((a-mx)**2 for a in x); a0 = my - b*mx
print(f"R5K_dia = {a0:+.3f} + {b:.2f} * pob_dia  (06-16, 11 dias)")
for d in out:
    pr = a0 + b*pd_[d][1]/pd_[d][0]; print(d, "pob", round(pd_[d][1]/pd_[d][0], 3), "R5K predicho por regimen", round(pr, 3), "observado", round(r5[d][1]/r5[d][0], 3), "n", r5[d][2])
def pooled(cell, dd, seed=3):
    fin = defaultdict(lambda: [0.0, 0.0])
    for (o, k, d, m, l), (c, p) in U.items():
        if (o, k) == cell and d in dd: fin[m][0] += c; fin[m][1] += p
    ks = list(fin); random.seed(seed); bs = []
    for _ in range(2000):
        s = [fin[random.choice(ks)] for _ in ks]; bs.append(sum(v[1] for v in s)/sum(v[0] for v in s))
    bs.sort(); C = sum(v[0] for v in fin.values()); P = sum(v[1] for v in fin.values())
    return len(ks), C, P/C, bs[100], bs[1900]
for cell in ((5000.0, 50.0), (5000.0, 1e12), (8000.0, 50.0), (8000.0, 1e12), (3000.0, 50.0)):
    for lab, dd in (("IN", ins), ("OUT", out)):
        n, C, e, lo, hi = pooled(cell, dd); print(cell, lab, f"cierres {n} coste {C:.0f} EV {e:+.3f} IC90 cierre ({lo:+.3f},{hi:+.3f})")
