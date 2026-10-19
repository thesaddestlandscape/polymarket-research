import pickle, random
from collections import defaultdict
D = pickle.load(open("U.pkl", "rb")); U, POP = D["U"], D["POP"]
ins = [f"2026-10-{x:02d}" for x in range(6, 17)]
pd_ = defaultdict(lambda: [0.0, 0.0]); r5 = defaultdict(lambda: [0.0, 0.0]); r8 = defaultdict(lambda: [0.0, 0.0])
for (d, m, l), (c, p) in POP.items(): pd_[d][0] += c; pd_[d][1] += p
for (o, k, d, m, l), (c, p) in U.items():
    if (o, k) == (5000.0, 50.0): r5[d][0] += c; r5[d][1] += p
    if (o, k) == (8000.0, 50.0): r8[d][0] += c; r8[d][1] += p
def fit(dd, R):
    x = [pd_[d][1]/pd_[d][0] for d in dd]; y = [R[d][1]/R[d][0] for d in dd]
    mx, my = sum(x)/len(x), sum(y)/len(y); sxx = sum((a-mx)**2 for a in x)
    if sxx == 0: return None
    b = sum((a-mx)*(c-my) for a, c in zip(x, y))/sxx; return my - b*mx, b
random.seed(5)
for lab, R in (("R5K", r5), ("R8K", r8)):
    a0, b = fit(ins, R); bs = []
    for _ in range(4000):
        s = [random.choice(ins) for _ in ins]; f = fit(s, R)
        if f: bs.append(f)
    ia = sorted(v[0] for v in bs); ib = sorted(v[1] for v in bs); n = len(bs)
    print(lab, f"intercepto {a0:+.3f} IC90 dias ({ia[int(.05*n)]:+.3f},{ia[int(.95*n)]:+.3f})  pendiente {b:.2f} ({ib[int(.05*n)]:.2f},{ib[int(.95*n)]:.2f})")
