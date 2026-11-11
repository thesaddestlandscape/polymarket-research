import json, sys, numpy as np
def rtts(rows): return np.array([(r['tf'] - r['ts']) / 1e6 for r in rows])
def clob(f, frac=0.5):
    d = json.load(open(f)); r = [x for x in d['rows'] if x['status'] == 200]
    rt = rtts(r); rtd = np.array([(x['td'] - x['ts']) / 1e6 for x in r])
    S = np.array([int(x['body']) for x in r], float)
    m = np.array([(x['ts'] + x['tf']) / 2e9 for x in r])     # reloj local, s epoch, punto medio ts..primer byte
    out = dict(n=len(r), rtt_min=float(rt.min()), rtt_p50=float(np.median(rt)), rtt_p90=float(np.percentile(rt, 90)), rtt_max=float(rt.max()), connect_ms=d['connect_ms'])
    # filtrar el 'frac' de menor RTT
    k = rt <= np.quantile(rt, frac); Sk, mk = S[k], m[k]
    th = np.arange(-1.0, 1.0, 0.001)                 # offset servidor-local (s), paso 1 ms
    mis = np.array([(np.floor(mk + t) != Sk).sum() for t in th])
    best = mis.min(); reg = th[mis == best]
    # region contigua mas larga con el minimo
    out['n_filtrado'] = int(k.sum()); out['mismatch_min'] = int(best)
    out['theta_ms_min'] = float(reg.min() * 1000); out['theta_ms_max'] = float(reg.max() * 1000); out['theta_ms_centro'] = float(np.median(reg) * 1000)
    # intersecion de intervalos
    out['L_ms'] = float(np.max(Sk - mk) * 1000); out['U_ms'] = float(np.min(Sk + 1 - mk) * 1000)
    return out
def bn(f):
    d = json.load(open(f)); r = [x for x in d['rows'] if x['status'] == 200]
    rt = rtts(r)
    sv = np.array([json.loads(x['body'])['serverTime'] for x in r], float)
    m = np.array([(x['ts'] + x['tf']) / 2e6 for x in r])      # ms
    off = sv - m
    i = np.argsort(rt)[:max(5, len(r) // 5)]
    return dict(n=len(r), rtt_min=float(rt.min()), rtt_p50=float(np.median(rt)), off_all_p50=float(np.median(off)), off_all_sd=float(off.std()),
                off_minrtt_p50=float(np.median(off[i])), off_minrtt_min=float(off[i].min()), off_minrtt_max=float(off[i].max()), off_at_minrtt=float(off[np.argmin(rt)]), connect_ms=d['connect_ms'])
if __name__ == '__main__':
    print('CLOB', clob(sys.argv[1]))
    if len(sys.argv) > 2: print('BN', bn(sys.argv[2]))
