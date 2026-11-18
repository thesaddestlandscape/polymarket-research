#!/usr/bin/env python3
"""s3 (18-Nov, MECANISMO): consistencia L2 en libro5_ms: estado = B (snapshot) + d (price_change, size = NUEVO total del nivel); compara el estado predicho con el siguiente B del token (bids <=0,35).
Uso: s3 FICHERO NLINEAS"""
import sys, gzip, json, collections
f, N = sys.argv[1], int(sys.argv[2]); S = {}; res = collections.Counter(); dif = []; dts = []
def parse(s):
    return {round(float(a), 4): float(b) for a, b in (x.split(':') for x in s.split(';') if x)} if s else {}
with gzip.open(f, 'rt') as fh:
    next(fh)
    for i, l in enumerate(fh):
        if i >= N: break
        p = l.rstrip('\n').split(',')
        t = p[0]
        if t == 'B':
            tk = p[2]; bids = {k: v for k, v in parse(p[3]).items() if k <= 0.35}
            if tk in S and S[tk]['n'] > 0:
                pr = S[tk]['b']; keys = set(pr) | set(bids); ok = sum(1 for k in keys if abs(pr.get(k, 0) - bids.get(k, 0)) < 0.011)
                res['B_comparados'] += 1; res['niveles'] += len(keys); res['niveles_ok'] += ok; res['B_identicos'] += int(ok == len(keys))
                dts.append((int(p[1]) - S[tk]['t']) / 1000)
            S[tk] = {'b': bids, 'n': 0, 't': int(p[1])}
        elif t == 'd':
            tk = p[2]
            if tk not in S or p[3] != 'B': continue
            px = round(float(p[4]), 4)
            if px > 0.35: continue
            if float(p[5]) <= 0: S[tk]['b'].pop(px, None)
            else: S[tk]['b'][px] = float(p[5])
            S[tk]['n'] += 1
res['frac_niveles_ok'] = round(res['niveles_ok'] / max(1, res['niveles']), 4); res['frac_B_identicos'] = round(res['B_identicos'] / max(1, res['B_comparados']), 4)
res['dt_entre_B_s_p50'] = sorted(dts)[len(dts) // 2] if dts else None
print(json.dumps(res))
