import json, csv, glob, sys, collections, random, statistics as st
from datetime import datetime, timezone
S = sys.argv[1]
D = '/root/polymarket-research-datalogs/'
O = json.load(open(f'{S}/cron2_out.json')); des = json.load(open(D + 'maker_ms_desenlaces_cache.json'))
EV = {}
for f in sorted(glob.glob(D + 'vigia_5m_barato/eventos_*.csv')):
    for e in csv.DictReader(open(f)): EV[e['event_id']] = e
def fee(p): return 0.07 * p * (1 - p)
rng = random.Random(4)
for r in O:
    r['hueco'] = (r.get('gap_prev_q5_ms') or 0) > 60000 or (r.get('gap_prev_q15_ms') or 0) > 60000
    r['ej'] = r['acc215'] > 0
    e = EV[r['event_id']]; p = float(e['ask_compra_t0']); acc = max(5.0, 2.0 / p)
    r['paper'] = acc * ((1.0 if r['gana'] else 0) - p - fee(p)); r['paper_c'] = acc * (p + fee(p))
    if r['ej']:
        r['pnl'] = r['acc215'] * ((1.0 if r['gana'] else 0) - r['p215'] - fee(r['p215'])); r['c'] = r['acc215'] * (r['p215'] + fee(r['p215']))
    r['day'] = datetime.fromtimestamp(r['cierre'], timezone.utc).date().isoformat()
def boot(rows, key, n=5000):
    g = collections.defaultdict(list)
    for r in rows: g[key(r)].append(r)
    ks = list(g); m = []
    for _ in range(n):
        s = [rng.choice(ks) for _ in ks]; c = sum(r['c'] for k in s for r in g[k])
        if c > 0: m.append(sum(r['pnl'] for k in s for r in g[k]) / c)
    m.sort(); return round(m[int(.05 * len(m))], 3), round(m[int(.95 * len(m))], 3)
for nom, S1 in (('58 señales', O), ('53 sin huecos de feed', [r for r in O if not r['hueco']])):
    ex = [r for r in S1 if r['ej']]; nx = [r for r in S1 if not r['ej'] and r['cls215'] != 'UNKNOWN']
    pnl = sum(r['pnl'] for r in ex); c = sum(r['c'] for r in ex)
    byd = collections.defaultdict(float)
    for r in ex: byd[r['day']] += r['pnl']
    best = max(byd, key=byd.get); exb = [r for r in ex if r['day'] != best]
    bestop = max(ex, key=lambda r: r['pnl'])
    print(f'== {nom}: ejecutables {len(ex)} (ganan {sum(r["gana"] for r in ex)}), no ejec {len(nx)} (ganan {sum(r["gana"] for r in nx)})')
    print(f'   L215 PnL {pnl:.2f} coste {c:.2f} EV {pnl/c:+.3f} IC90 días {boot(ex, lambda r: r["day"])} IC90 cierre {boot(ex, lambda r: (r["day"], r["cierre"]))} | sin mejor día ({best}) {sum(r["pnl"] for r in exb)/sum(r["c"] for r in exb):+.3f} | sin mejor op {(pnl-bestop["pnl"])/(c-bestop["c"]):+.3f}')
    pp = sum(r['paper'] for r in S1); pc = sum(r['paper_c'] for r in S1)
    print(f'   PAPEL (comprar todas al ask_t0, sin latencia, 5 acc mín): PnL {pp:.2f} coste {pc:.2f} EV {pp/pc:+.3f}; ejecutables capturan {sum(r["paper"] for r in ex):.2f} de papel (a ask_t0) y su PnL real a L215 {pnl:.2f}; no ejecutables papel {sum(r["paper"] for r in nx):.2f}')
    print(f'   papel de las ganadoras: {sum(r["paper"] for r in S1 if r["gana"]):.2f}; capturado a L215: {sum(r["pnl"] for r in ex if r["gana"]):.2f} ({sum(r["pnl"] for r in ex if r["gana"])/sum(r["paper"] for r in S1 if r["gana"]):.2%})')
