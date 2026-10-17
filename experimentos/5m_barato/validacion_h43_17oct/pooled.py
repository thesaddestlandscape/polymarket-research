# Agregado de los 3 días (PRIMARIA, unidades completas) + tasa de acierto por día + bootstrap por mercado.
import gzip, csv, random
random.seed(11)
allr = []
for D in ['10', '12', '14']:
    rows = []
    with gzip.open(f'unidades_2026-10-{D}_PRIMARIA.csv.gz', 'rt') as f:
        for r in csv.DictReader(f):
            if r['estado'] == 'COMPLETA':
                rows.append((D, r['mkt'], r['s'], float(r['pnl']), float(r['coste'])))
    wins = sum(1 for r in rows if r[3] > 0)
    c = sum(r[4] for r in rows); p = sum(r[3] for r in rows)
    print(f"dia {D}: n={len(rows)} aciertos(pnl>0)={wins} ({wins/len(rows):.1%}) coste={c:.1f} pnl={p:.2f} EV={p/c:+.4f} precio_medio_ponderado={c/ (sum(1 for _ in rows) and 1):.0f}")
    allr += rows
def ev(l):
    c = sum(r[4] for r in l); return sum(r[3] for r in l) / c
srt = sorted(allr, key=lambda r: -r[3])
print('pooled n', len(allr), 'EV', round(ev(allr), 4), 'sin top2', round(ev(srt[2:]), 4), 'sin top20', round(ev(srt[20:]), 4), 'sin top2 dias (14,10)', round(ev([r for r in allr if r[0] == '12']), 4))
mk = {}
for r in allr: mk.setdefault((r[0], r[1]), []).append(r)
keys = list(mk)
bs = []
for _ in range(3000):
    smp = [x for k in random.choices(keys, k=len(keys)) for x in mk[k]]
    bs.append(ev(smp))
bs.sort(); print('IC90 pooled por mercado-cluster', round(bs[150], 3), round(bs[2850], 3))
# dia a dia: EV de cada día cuando se excluye el mejor día
