# Concentración y bootstrap por mercado (cluster) de las unidades PRIMARIAS completas, por día. Solo lectura de CSV propios.
import gzip, csv, random, sys
random.seed(7)
res = {}
for D in ['10', '12', '14']:
    rows = []
    with gzip.open(f'unidades_2026-10-{D}_PRIMARIA.csv.gz', 'rt') as f:
        for r in csv.DictReader(f):
            if r['estado'] == 'COMPLETA':
                rows.append((r['mkt'], r['s'], float(r['pnl']), float(r['coste'])))
    P = sum(r[2] for r in rows); C = sum(r[3] for r in rows)
    srt = sorted(rows, key=lambda r: -r[2])
    def ev(lst):
        c = sum(r[3] for r in lst); return sum(r[2] for r in lst) / c if c > 0 else float('nan')
    # bootstrap por mercado (clusters), 2000 reps
    mk = {}
    for r in rows: mk.setdefault(r[0], []).append(r)
    keys = list(mk.keys())
    bs = []
    for _ in range(2000):
        samp = [x for k in random.choices(keys, k=len(keys)) for x in mk[k]]
        bs.append(ev(samp))
    bs.sort()
    lo, hi = bs[int(0.05 * len(bs))], bs[int(0.95 * len(bs))]
    n_mk = len(keys)
    # lados de un mismo mercado
    both = sum(1 for k in keys if len(mk[k]) == 2)
    print(f"2026-10-{D}: n={len(rows)} mercados={n_mk} (ambos lados en {both}) coste={C:.1f} pnl={P:.2f} EV={P/C:+.4f} "
          f"IC90 cluster-mercado=({lo:+.3f},{hi:+.3f}) | sin top1 {ev(srt[1:]):+.4f} | sin top2 {ev(srt[2:]):+.4f} | "
          f"sin top20 {ev(srt[20:]):+.4f} | top1 pnl {srt[0][2]:.2f} ({srt[0][0]} {srt[0][1]}) top5 pnl share {sum(r[2] for r in srt[:5])/P:+.2f}")
    # pnl por lado
    for s in ('YES', 'NO'):
        sub = [r for r in rows if r[1] == s]
        if sub: print(f"   lado {s}: n={len(sub)} EV={ev(sub):+.4f} coste={sum(r[3] for r in sub):.1f}")
    res[D] = (len(rows), C, P)
tot = [sum(res[d][i] for d in res) for i in range(3)]
print("3 dias: n=%d coste=%.1f pnl=%.2f EV=%+.4f" % (tot[0], tot[1], tot[2], tot[2] / tot[1]))
