#!/usr/bin/env python3
"""Test sintetico de palanca1_extraer.py (python3 -I test_palanca1_fixture.py <dir_tmp>). Comprueba: estado a t_sw+L por ORDEN DE RECEPCION, ask que se mueve, maker, idempotencia."""
import sys, gzip, json, subprocess, os, hashlib, time, csv
d = sys.argv[1]; os.makedirs(d, exist_ok=True)
C = int(time.mktime(time.strptime('2026-10-26 00:05:00', '%Y-%m-%d %H:%M:%S')) - time.timezone) * 1000
Y, N = 'TY', 'TN'; t0 = C - 200_000; sw = C - 190_000
rows = ['k,1,%s,BTC,5min,1,2026-10-26 00:05:00+00:00,YES' % Y, 'k,1,%s,BTC,5min,1,2026-10-26 00:05:00+00:00,NO' % N,
 'q,%d,%s,0.20,0.25,10.0,10.0,%d' % (t0, Y, t0), 'q,%d,%s,0.75,0.80,10.0,10.0,%d' % (t0, N, t0),
 'q,%d,%s,0.18,0.25,10.0,10.0,%d' % (sw, Y, sw),            # barrido de Y (bb .20 -> .18) en t_sw
 'q,%d,%s,0.75,0.82,10.0,10.0,%d' % (sw+50, N, sw+50),      # ask N se mueve .80->.82 a +50
 'q,%d,%s,0.77,0.85,7.0,6.0,%d' % (sw+300, N, sw+300),      # +300: ask .85 (afecta solo L=500)
 't,%d,%s,0.75,SELL,40.0,%d' % (sw+400, N, sw+400),         # SELL de N a .75: llena la puja maker de L=100/250 (bid .75, t0<=sw+250); NO la de L=500 (se coloca en sw+500, despues)
 'q,%d,%s,0.77,0.90,7.0,6.0,%d' % (sw+700, N, sw+700),      # disparador L=500; ask .90 no debe usarse
 'q,%d,%s,0.10,0.25,10.0,10.0,%d' % (C-100_000, Y, C-100_000),
 'q,%d,%s,0.80,0.90,10.0,10.0,%d' % (C-100_000, N, C-100_000),
 'q,%d,%s,0.10,0.25,10.0,10.0,%d' % (C-5_000, Y, C-5_000)]
src = os.path.join(d, 'reg.csv.gz'); 
with gzip.open(src, 'wt') as f: f.write('tipo\n' + '\n'.join(rows) + '\n')
json.dump({'1': 'NO'}, open(os.path.join(d, 'des.json'), 'w'))
here = os.path.dirname(os.path.abspath(__file__)); out = os.path.join(d, 'out.csv.gz'); h = []
for _ in range(2):
    subprocess.check_call(['python3', '-I', os.path.join(here, 'palanca1_extraer.py'), '--dia', '2026-10-26', '--src', src, '--des', os.path.join(d, 'des.json'), '--out', out, '--nplc', '8'])
    h.append(hashlib.sha256(open(out, 'rb').read()).hexdigest() if False else hashlib.sha256(gzip.open(out).read()).hexdigest())
assert h[0] == h[1], 'no idempotente'
ALL = list(csv.DictReader(gzip.open(out, 'rt'))); PL = [r for r in ALL if r['kind'] == 'placebo']
assert {r['lado_ev'] for r in PL} == {'YES', 'NO'}, ('placebos de ambos lados', {r['lado_ev'] for r in PL})
assert all(r['mk_fin'] for r in ALL)
R = {int(r['L']): r for r in ALL if r['kind'] == 'real'}
assert set(R) == {100, 250, 500}, R.keys()
assert float(R[100]['ask_L']) == 0.82 and float(R[250]['ask_L']) == 0.82, (R[100], R[250])
assert float(R[500]['ask_L']) == 0.85, R[500]          # el ask se movio: cuenta el precio nuevo, no el previo
assert float(R[100]['ask_prev']) == 0.80 and R[100]['lado_buy'] == 'NO' and R[100]['gana_buy'] == '1'
assert float(R[250]['bid_L']) == 0.75 and float(R[500]['bid_L']) == 0.77
assert R[100]['mk_pes'] == '1' and R[250]['mk_pes'] == '1' and R[500]['mk_pes'] == '0', (R[100]['mk_pes'], R[250]['mk_pes'], R[500]['mk_pes'])
assert len(R) == 3
print('FIXTURE OK (idempotente, estado por recepcion, ask movido, maker)')
