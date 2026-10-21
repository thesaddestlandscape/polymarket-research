#!/usr/bin/env python3
import csv, glob, sys, collections
import numpy as np
O = '/tmp/claude-0/-root-polymarket-research/46569fb1-feea-4c5a-8d2d-299a326f3bc5/scratchpad/h61/out/'
TRAMOS = {'DISC': [f'2026-10-{d:02d}' for d in range(6, 13)], 'VAL': [f'2026-10-{d:02d}' for d in range(13, 19)], 'OOS': ['2026-10-19', '2026-10-20']}
rng = np.random.default_rng(7)
def ic_dias(pd_, cd):  # pnl y coste por dia -> IC90 del EV pond por bootstrap de dias
    ds = sorted(cd); 
    if len(ds) < 2: return (np.nan, np.nan)
    P = np.array([pd_[d] for d in ds]); Cc = np.array([cd[d] for d in ds]); bs = []
    for _ in range(3000):
        i = rng.integers(0, len(ds), len(ds)); s = Cc[i].sum()
        if s > 0: bs.append(P[i].sum() / s)
    return tuple(np.percentile(bs, [5, 95])) if bs else (np.nan, np.nan)
def sin2(pd_, cd):
    ds = sorted(pd_, key=lambda d: -pd_[d])[2:]; c = sum(cd[d] for d in ds)
    return sum(pd_[d] for d in ds) / c if c > 0 else np.nan
F = collections.defaultdict(list)
dias = set()
for f in sorted(glob.glob(O + 'fills_*.csv')):
    for r in csv.DictReader(open(f)):
        if float(r['lleno']) <= 0: continue
        F[(r['brazo'], r['rep'], r['modo'], r['W'], r['X'])].append(r); dias.add(r['dia'])
mode = sys.argv[1] if len(sys.argv) > 1 else 'fills'
if mode == 'fills':
    for tramo, ds in TRAMOS.items():
        print(f'== {tramo} {ds[0]}..{ds[-1]} (dias con fichero: {len(set(ds) & set(x.split("_")[-1][:10] for x in glob.glob(O+"fills_*.csv")))})')
        for brazo in 'AB':
            for rep in ('150', '1500'):
                base = [r for r in F[(brazo, rep, 'none', '0', '0.0')] if r['dia'] in ds]
                nb = len(base); pb = sum(float(r['pnl']) for r in base); cb = sum(float(r['coste']) for r in base)
                print(f' {brazo} r{rep} v1: n={nb} EVpond={pb/cb if cb else float("nan"):+.3f} PnL={pb:+.2f}')
                for k, rows in sorted(F.items()):
                    if k[0] != brazo or k[1] != rep or k[2] == 'none': continue
                    rr = [r for r in rows if r['dia'] in ds]
                    n = len(rr); p = sum(float(r['pnl']) for r in rr); c = sum(float(r['coste']) for r in rr)
                    pd_ = collections.Counter(); cd = collections.Counter()
                    for r in rr: pd_[r['dia']] += float(r['pnl']); cd[r['dia']] += float(r['coste'])
                    lo, hi = ic_dias(pd_, cd)
                    print(f'   {k[2]:6s} W{k[3]:>4s} X{k[4]:>3s}: n={n:2d} ret={n/max(nb,1):.2f} EVpond={p/c if c else float("nan"):+.3f} PnL={p:+6.2f} dPnL={p-pb:+6.2f} sin2={sin2(pd_,cd):+.3f} IC90d=({lo:+.2f};{hi:+.2f})')
else:
    P = []
    for f in sorted(glob.glob(O + 'prints_*.csv')):
        P += list(csv.DictReader(open(f)))
    print('prints', len(P))
    for tramo, ds in list(TRAMOS.items()) + [('VAL+OOS', TRAMOS['VAL'] + TRAMOS['OOS'])]:
        for brazo in 'AB':
            rr = [r for r in P if r['dia'] in ds and r['brazo'] == brazo]
            # unidad: primer print por (cierre) y todos los prints (1 accion cada uno)
            for W in ('r500', 'r1000', 'r3000'):
                for X in (0.0, 0.5, 1.0, 2.0, 3.0):
                    for unidad in ('todos', 'primero'):
                        g = {'contra': collections.defaultdict(lambda: [0.0, 0.0, 0]), 'resto': collections.defaultdict(lambda: [0.0, 0.0, 0])}
                        vistos = set()
                        for r in rr:
                            if unidad == 'primero':
                                if r['cierre'] in vistos: continue
                                vistos.add(r['cierre'])
                            v = r[W]; grp = 'contra' if (v != '' and float(v) < -X) else 'resto'
                            p = float(r['p']); pnl = int(r['gana']) - p + 0.2 * 0.07 * p * (1 - p)
                            a = g[grp][r['dia']]; a[0] += pnl; a[1] += p; a[2] += 1
                        def ev(d): 
                            c = sum(x[1] for x in d.values()); return (sum(x[0] for x in d.values()) / c if c else np.nan), sum(x[2] for x in d.values()), len(d)
                        ec, nc, dc = ev(g['contra']); er, nr, dr = ev(g['resto'])
                        # IC90 dias de la diferencia
                        ds2 = sorted(set(g['contra']) & set(g['resto'])); bs = []
                        if len(ds2) >= 2:
                            for _ in range(2000):
                                i = rng.integers(0, len(ds2), len(ds2)); s = [ds2[j] for j in i]
                                cc = sum(g['contra'][d][1] for d in s); cr = sum(g['resto'][d][1] for d in s)
                                if cc > 0 and cr > 0: bs.append(sum(g['contra'][d][0] for d in s)/cc - sum(g['resto'][d][0] for d in s)/cr)
                        lo, hi = (np.percentile(bs, [5, 95]) if bs else (np.nan, np.nan))
                        print(f'{tramo:7s} {brazo} {W:5s} X{X:3.1f} {unidad:7s}: contra n={nc:5d} ({dc}d) EV={ec:+.3f} | resto n={nr:5d} EV={er:+.3f} | frac_contra={nc/max(nc+nr,1):.2f} | dif IC90d=({lo:+.3f};{hi:+.3f})')
