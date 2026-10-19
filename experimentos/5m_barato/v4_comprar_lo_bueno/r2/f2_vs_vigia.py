#!/usr/bin/env python3
"""(2) Latencia NUESTRA (F2, WS propio en vivo) vs registro del vigía V4 para los MISMOS eventos B1_5m (16-18 Oct).
Solo lectura. Une por (moneda, cierre, n). Reloj: recepción local en ambos (mismo host, mismo reloj)."""
import json, csv, glob, collections, statistics as st
D = '/root/polymarket-research-datalogs/'
F2 = {}
REL = collections.defaultdict(dict)
for f in sorted(glob.glob(D + 'f2_5m_barato/f2_2026-10-1[6-9].jsonl')):
    for l in open(f):
        d = json.loads(l)
        if d['tipo'] == 'v4_evento': F2[(d['moneda'], d['cierre'], d['n'])] = d
        elif d['tipo'] == 'v4_relleno': REL[(d['moneda'], d['cierre'], d['n'])][d['L']] = d
V = {}
for f in sorted(glob.glob(D + 'vigia_5m_barato/eventos_2026-10-1[6-9].csv')):
    for e in csv.DictReader(open(f)):
        if e['regla'] != 'B1_5m': continue
        n = int(e['event_id'].rsplit('_', 1)[1])
        V[(e['moneda'], int(e['cierre']), n)] = e
def pct(x):
    x = sorted(x); n = len(x)
    if not n: return 'n=0'
    q = lambda p: x[min(n - 1, int(p * n))]
    return f'n={n} P10/25/50/75/90={q(.1):.1f}/{q(.25):.1f}/{q(.5):.1f}/{q(.75):.1f}/{q(.9):.1f} min={x[0]:.1f} max={x[-1]:.1f}'
print('F2 v4_evento:', len(F2), '| vigía B1_5m 16-19:', len(V))
comunes = sorted(set(F2) & set(V)); sf2 = sorted(set(F2) - set(V)); sv = sorted(set(V) - set(F2))
print('comunes', len(comunes), '| solo F2', len(sf2), '| solo vigía', len(sv))
dd, dec, firma = [], [], []
cl = collections.Counter()
for k in comunes:
    f, v = F2[k], V[k]
    dd.append(f['t_deteccion'] - int(v['t_deteccion']))
    dec.append(f.get('ms_evento_a_decision') or 0); firma.append(f.get('ms_tomar_firma') or 0)
    r = REL[k].get(215)
    cl[(v['L215_clase'][:1], r['clase'] if r else None)] += 1
print('t_det F2 - t_det vigía (ms):', pct(dd))
print('F2 evento->decisión (ms):', pct(dec)); print('F2 tomar+firma (ms):', pct(firma))
print('clase L215 vigía x F2:', dict(cl))
for k in comunes:
    f, v = F2[k], V[k]
    print(' ', k, 'dt', f['t_deteccion'] - int(v['t_deteccion']), 'ask', f['ask5_t0'], v['ask_compra_t0'], 'bid15', f['bid15_t0'], v['bid_otro_t0'], 'disp', f.get('disparador'), 'vig', v['L215_clase'][:1], 'F2', (REL[k].get(215) or {}).get('clase'))
for k in sf2: print(' solo F2', k, F2[k]['t_deteccion'], F2[k]['ask5_t0'], F2[k]['bid15_t0'], F2[k]['margen_neto'])
for k in sv: print(' solo vigía', k, V[k]['t_deteccion'], V[k]['ask_compra_t0'], V[k]['bid_otro_t0'], V[k]['margen_neto'])
