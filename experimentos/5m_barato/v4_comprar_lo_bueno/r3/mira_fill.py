import sys, os, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from simlib import *
D, C, t0, w = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
km = kmap(D); LS = lados(D); lado, m5 = LS[C]; sl = 'YES' if lado == 'Up' else 'NO'; ol = 'NO' if sl == 'YES' else 'YES'
k5, k5o, k15 = km[('5min', C, sl)][0], km[('5min', C, ol)][0], km[('15min', C, sl)][0]
import gzip
for ln in gzip.open(O + f'rows_{D}.csv.gz', 'rt'):
    c = ln.split(',')
    if int(c[0]) != -(-C // 900) * 900 and int(c[0]) != C: continue
    if c[1] == 't':
        rx = int(c[7]); ex = int(c[2])
        if abs(rx - t0) <= w and c[3] in (k5, k5o): print('T', 'S' if c[3] == k5 else 'O', 'ex', ex - t0, 'rx', rx - t0, c[4], c[5], c[6])
    elif c[1] == 'q':
        rx = int(c[8]) if c[8].strip() else int(c[2])
        if abs(rx - t0) <= w and c[3] == k5: print('Q S', 'ex', int(c[2]) - t0, 'rx', rx - t0, 'bid', c[4], 'ask', c[5], 'bsz', c[6], 'asz', c[7])
