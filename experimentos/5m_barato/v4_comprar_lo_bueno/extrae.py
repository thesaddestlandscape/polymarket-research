#!/usr/bin/env python3
"""Extrae, para las 58 señales V4 OOS (B1_5m es_primero, t_deteccion >= 06-Oct 12:00Z), las filas q/t de su token 5m (lado s)
y 15m (lado s), los x de Binance de su moneda, y los fills on-chain del token 5m s, a ficheros pequeños en OUT.
Solo lectura sobre archivo en el volumen. Lanzar: nice -n 19 ionice -c3 python3 extrae.py OUT [dia ...]
Streaming por zcat|grep -F (RAM mínima)."""
import csv, glob, gzip, json, subprocess, sys, os, collections
from datetime import datetime, timezone
D = '/root/polymarket-research-datalogs/'
VOL = '/mnt/HC_Volume_106538179/'
OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
cong = int(datetime.fromisoformat('2026-10-06T12:00:00+00:00').timestamp() * 1000)
E = []
for f in sorted(glob.glob(D + 'vigia_5m_barato/eventos_*.csv')):
    E += list(csv.DictReader(open(f)))
prim = [e for e in E if e['regla'] == 'B1_5m' and e['es_primero'] == '1' and int(e['t_deteccion']) >= cong]
bydia = collections.defaultdict(list)
for e in prim:
    bydia[datetime.fromtimestamp(int(e['t_deteccion']) / 1000, timezone.utc).date().isoformat()].append(e)
dias = sys.argv[2:] or sorted(bydia)
SIM = {'BTC': 'BTCUSDT', 'ETH': 'ETHUSDT', 'SOL': 'SOLUSDT', 'XRP': 'XRPUSDT', 'DOGE': 'DOGEUSDT', 'BNB': 'BNBUSDT'}


def sh(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, executable='/bin/bash').stdout


for dia in dias:
    if dia not in bydia:
        continue
    Ed = bydia[dia]
    f5 = f'{VOL}m5_registro/m5_registro_{dia}.csv.gz'
    f15 = f'{VOL}m15_registro/m15_registro_{dia}.csv.gz'
    ko = f'{OUT}/k_{dia}.txt'
    if not os.path.exists(ko):
        open(ko, 'w').write(sh(f"zcat {f5} | grep '^k,'"))
    km = {}
    for ln in open(ko):
        c = ln.rstrip('\n').split(',')
        if len(c) >= 8:
            km[(c[5], c[7])] = (c[2], c[3], c[4], c[6])
    # 15m tokens pueden no estar en k de m5? (si lo están: ok)
    toks = {}
    for i, e in enumerate(Ed):
        lado = 'YES' if e['lado'] == 'Up' else 'NO'
        a = km.get((e['market_compra'], lado)); b = km.get((e['market_otro'], lado))
        toks[e['event_id']] = (a[0] if a else None, b[0] if b else None)
    allt = sorted({t for v in toks.values() for t in v if t})
    tf = f'{OUT}/tok_{dia}.txt'
    open(tf, 'w').write('\n'.join(allt) + '\n')
    mons = sorted({SIM[e['moneda']] for e in Ed})
    # q,t del 5m
    o5 = f'{OUT}/qt5_{dia}.txt'
    if not os.path.exists(o5):
        open(o5, 'w').write(sh(f"zcat {f5} | grep -F -f {tf} | grep -v '^k,'"))
    o15 = f'{OUT}/qt15_{dia}.txt'
    if not os.path.exists(o15):
        open(o15, 'w').write(sh(f"zcat {f15} | grep -F -f {tf} | grep -v '^k,'"))
    ox = f'{OUT}/x_{dia}.txt'
    if not os.path.exists(ox):
        pat = '|'.join(f'^x,[0-9]*,{m},' for m in mons)
        open(ox, 'w').write(sh(f"zcat {f5} | grep -E '{pat}'"))
    oc = f'{OUT}/oc_{dia}.txt'
    if not os.path.exists(oc):
        fo = f'{VOL}m5_onchain/m5_onchain_{dia}.csv.gz'
        open(oc, 'w').write(sh(f"zcat {fo} | grep -F -f {tf}"))
    json.dump(toks, open(f'{OUT}/toks_{dia}.json', 'w'))
    print(dia, len(Ed), 'tokens', len(allt), 'lineas qt5', sum(1 for _ in open(o5)), 'qt15', sum(1 for _ in open(o15)), 'oc', sum(1 for _ in open(oc)), flush=True)
