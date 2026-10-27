#!/usr/bin/env python3
"""E-RE-BR-01: descomposicion economica de B (SPREAD/SEL/COND), P(fill) por unidad, rebate. Solo lectura.
Uso: python3 -I e01_descomp.py  (lee DL fijo; escribe nada salvo stdout)."""
import csv, gzip, json, random, collections, glob

DL = '/root/polymarket-research-datalogs'
pp = {}
for l in open(DL + '/experimento_h47_B_ledger.jsonl'):
    if '"puja_post"' not in l:
        continue
    try:
        d = json.loads(l)
    except Exception:
        continue
    if d.get('tipo') != 'puja_post':
        continue
    lb = d.get('libro') or {}
    bids, asks = lb.get('bids') or [], lb.get('asks') or []
    if not bids or not asks:
        continue
    bb = max(b[0] for b in bids); ba = min(a[0] for a in asks)
    if ba <= bb:
        continue
    pp[d['oid']] = dict(slug=d['slug'], lado=d['lado'], precio=float(d['precio']), bb=bb, ba=ba,
                        mid=(bb + ba) / 2, t=float(d['t_dec']), n=d.get('n_orden'))
rows = []
for f in sorted(glob.glob(DL + '/etiquetado_pasivo_B/etiquetado_B_2026-10-2*.csv.gz')):
    for r in csv.DictReader(gzip.open(f, 'rt')):
        if r['unidad'] != 'orden' or r['resuelto'] != '1' or r['gana_lado'] == '':
            continue
        o = pp.get(r['id'])
        if o is None:
            continue
        rows.append(dict(o, id=r['id'], dia=r['dia'], coin=r['coin'], acc=float(r['acc']),
                         al=float(r['acc_llena'] or 0), g=float(r['gana_lado']), mk=r['mercado']))
print('ordenes con libro+desenlace', len(rows), 'de puja_post', len(pp))
# --- Q1 P(fill)
po = sum(1 for r in rows if r['al'] > 0) / len(rows)
puj = collections.defaultdict(list)
for r in rows:
    puj[(r['mk'], r['lado'])].append(r)
pf_p = sum(1 for v in puj.values() if any(x['al'] > 0 for x in v)) / len(puj)
mk = collections.defaultdict(list)
for r in rows:
    mk[r['mk']].append(r)
pf_m = sum(1 for v in mk.values() if any(x['al'] > 0 for x in v)) / len(mk)
print('Q1 P(fill) orden %.4f  puja %.4f (n=%d pujas)  mercado %.4f (n=%d)  ordenes/puja %.1f' %
      (po, pf_p, len(puj), pf_m, len(mk), len(rows) / len(puj)))
for dia in sorted({r['dia'] for r in rows}):
    pd = [v for v in puj.values() if v[0]['dia'] == dia]
    print('   dia', dia, 'pujas', len(pd), 'P(fill puja) %.3f' % (sum(1 for v in pd if any(x['al'] > 0 for x in v)) / len(pd)))

# --- Q2 descomposicion
def cierre(s):
    return s.rsplit('-', 1)[1]

fills = [r for r in rows if r['al'] > 0]
first = {k: min(v, key=lambda x: x['t']) for k, v in puj.items()}

def comp(F, P):
    # F: fills; P: dict puja->first order (todas las pujas armadas)
    cost = sum(r['al'] * r['precio'] for r in F)
    if cost == 0:
        return None
    ev = sum(r['al'] * (r['g'] - r['precio']) for r in F) / cost
    spread = sum(r['al'] * (r['mid'] - r['precio']) for r in F) / cost
    # U no condicionado por puja: gana - m0, peso nominal armado (acc*precio 1a orden)
    w = sum(p['acc'] * p['mid'] for p in P.values())
    U = sum(p['acc'] * (p['g'] - p['mid']) for p in P.values()) / w if w else float('nan')
    # SEL aplicado a los fills: (gana_puja_media_no_cond - m0) ~ usamos U escalado a las p de fills: U * sum(al*m0)/cost
    m0 = {k: P[k]['mid'] for k in P}
    sel = U * sum(r['al'] * m0[(r['mk'], r['lado'])] for r in F) / cost
    cond = ev - spread - sel
    mf_pp = sum(r['al'] * (r['g'] - r['precio']) for r in F) / sum(r['al'] for r in F)
    return dict(ev=ev, spread=spread, U=U, sel=sel, cond=cond, mf_pp=mf_pp, cost=cost, n=len(F))

base = comp(fills, first)
print('Q2 base', {k: round(v, 4) for k, v in base.items()})
# bootstrap por cierre
cl = collections.defaultdict(lambda: ([], {}))
for r in fills:
    cl[cierre(r['mk'])][0].append(r)
for k, p in first.items():
    cl[cierre(k[0])][1][k] = p
keys = list(cl)
random.seed(20261026)
B = collections.defaultdict(list)
for _ in range(2000):
    F, P = [], {}
    for c in random.choices(keys, k=len(keys)):
        F += cl[c][0]
        for kk, vv in cl[c][1].items():
            P[(kk, len(P))] = vv
        # duplicate pujas allowed via unique key
    # remap fills to unique keys: use m0 from own puja (mid of first order)
    cost = sum(r['al'] * r['precio'] for r in F)
    if cost == 0:
        continue
    ev = sum(r['al'] * (r['g'] - r['precio']) for r in F) / cost
    sp = sum(r['al'] * (r['mid'] - r['precio']) for r in F) / cost
    w = sum(p['acc'] * p['mid'] for p in P.values())
    U = sum(p['acc'] * (p['g'] - p['mid']) for p in P.values()) / w
    sel = U * sum(r['al'] * first[(r['mk'], r['lado'])]['mid'] for r in F) / cost
    for nm, v in (('ev', ev), ('spread', sp), ('U', U), ('sel', sel), ('cond', ev - sp - sel)):
        B[nm].append(v)
for nm in ('ev', 'spread', 'U', 'sel', 'cond'):
    s = sorted(B[nm]); print('   IC90 %-6s (%.4f, %.4f)' % (nm, s[int(.05 * len(s))], s[int(.95 * len(s))]))
print('   cierres', len(keys))
for dia in sorted({r['dia'] for r in rows}):
    Fd = [r for r in fills if r['dia'] == dia]; Pd = {k: v for k, v in first.items() if v['dia'] == dia}
    c = comp(Fd, Pd)
    if c: print('   dia', dia, {k: round(v, 3) for k, v in c.items()})
for coin in sorted({r['coin'] for r in rows}):
    Fd = [r for r in fills if r['coin'] == coin]; Pd = {k: v for k, v in first.items() if v['coin'] == coin}
    c = comp(Fd, Pd)
    if c: print('   coin', coin, {k: round(v, 3) for k, v in c.items()})
# nivel de armado
lv = collections.Counter(round((r['bb'] - r['precio']) * 100) for r in rows)
print('nivel (c bajo mejor bid) ordenes', sorted(lv.items())[:8])
lvf = collections.defaultdict(lambda: [0, 0, 0.0, 0.0])
for r in rows:
    k = round((r['bb'] - r['precio']) * 100); x = lvf[k]
    x[0] += 1; x[1] += r['al'] > 0
    if r['al'] > 0:
        x[2] += r['al'] * (r['g'] - r['precio']); x[3] += r['al'] * r['precio']
for k in sorted(lvf):
    x = lvf[k]
    if x[0] >= 30: print('   nivel %dc: ordenes %d P(fill) %.3f EV_f %s coste %.1f' % (k, x[0], x[1] / x[0], ('%.3f' % (x[2] / x[3])) if x[3] else 'na', x[3]))
# Q3 posiciones
pos = [r for r in csv.DictReader(open('/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/posiciones.csv')) if r['tanda_B']]
c = sum(float(r['coste']) for r in pos); p = sum(float(r['pnl_realizado'] or 0) for r in pos)
print('Q3 posiciones B n=%d coste %.2f pnl %.2f EV %.4f | ordenes coste %.2f EV %.4f' % (len(pos), c, p, p / c, base['cost'], base['ev']))
d = collections.defaultdict(float)
for r in pos: d[r['fecha_primer_fill_utc'][:10]] += float(r['coste'])
print('Q4 coste relleno por dia', {k: round(v, 1) for k, v in sorted(d.items())})
pm = sum(r['al'] * r['precio'] for r in fills) / sum(r['al'] for r in fills)
print('Q4 p media rellenos %.3f rebate por EUR si cobra 0,2*0,07*(1-p) = %.4f' % (pm, 0.2 * 0.07 * (1 - pm)))
