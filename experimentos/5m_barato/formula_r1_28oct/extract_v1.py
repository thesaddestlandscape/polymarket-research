#!/usr/bin/env python3
# FORMULA_R1_B extract: estados por unidad x instante (reloj de RECEPCION). uso: extract.py DIA [--maxlines N] [--out DIR]
import sys, os, gzip, csv, json, math, subprocess, datetime
import numpy as np
from array import array
D0 = '/root/polymarket-research/experimentos/5m_barato/'
UN = D0 + 'alpha_miner_b_27oct/units/u_%s.csv.gz'
R5 = '/mnt/HC_Volume_106538179/m5_registro/m5_registro_%s.csv.gz'
R15 = '/mnt/HC_Volume_106538179/m15_registro/m15_registro_%s.csv.gz'
G = json.load(open('/root/polymarket-research-datalogs/maker_ms_desenlaces_cache.json'))
SYM = {'BTC': 'BTCUSDT', 'ETH': 'ETHUSDT', 'SOL': 'SOLUSDT', 'XRP': 'XRPUSDT', 'DOGE': 'DOGEUSDT', 'BNB': 'BNBUSDT'}
SYMV = set(SYM.values())
LT = 250.0; E = 1e-9; NAN = float('nan')
AWK5 = r'''BEGIN{FS=","; while((getline l < MKF)>0) mk[l]=1}
$1=="k"{ if($5=="5min" && (("m" $6) in mk) && ($8=="YES"||$8=="NO")){ids["t" $3]=1; print}; next}
$1=="q"{ if(("t" $3) in ids) print; next}
$1=="x"{ if($3 ~ /^(BTC|ETH|SOL|XRP|DOGE|BNB)USDT$/){b=int($8/100); if(b!=lb[$3]){lb[$3]=b; print}}; next}'''
AWK15 = r'''BEGIN{FS=","}
$1=="k"{ if($5=="15min" && ($8=="YES"||$8=="NO")){ids["t" $3]=1; print}; next}
$1=="q"{ kk="t" $3; if(kk in ids){ b=int($8/250); if((kk in lb) && b!=lb[kk]) print last[kk]; lb[kk]=b; last[kk]=$0 }; next}
END{ for(kk in last) print last[kk] }'''
HDR = ['dia','coin','mercado','lado','label','cls','jw','extra','tau','dtf','p0','sh','cost','win','A_b','A_a','A_bs','A_as','A_age','B_b','B_a','B_bs','B_as','B_age','X_b','X_bs','X_age','C_b','C_a','C_age','C0_b','C0_a','C0_age','S_now','S_1','S_5','refB','sig60']
def num(s):
    s = s.strip()
    if s == '' or s == 'None' or s == 'nan': return NAN
    return float(s)
class Tok:
    __slots__ = ('q', 'lo', 'hi', 'qa')
    def __init__(s, lo, hi): s.q = array('d'); s.lo = lo; s.hi = hi; s.qa = None
def prep(t):
    a = np.frombuffer(t.q, dtype=float).reshape(-1, 5) if len(t.q) else np.zeros((0, 5))
    o = np.argsort(a[:, 0], kind='stable'); t.qa = a[o]
def stream(path, prog, mkf=None, maxlines=0):
    head = ' | head -n %d' % maxlines if maxlines else ''
    va = '-v MKF=%s' % mkf if mkf else ''
    cmd = "nice -n 19 ionice -c3 zcat %s%s | awk -F, %s '%s'" % (path, head, va, prog)
    return subprocess.Popen(['bash', '-c', cmd], stdout=subprocess.PIPE, text=True, bufsize=1 << 20)
def ql(t, tm):
    if t is None or t.qa is None or len(t.qa) == 0: return (NAN,) * 5
    i = int(np.searchsorted(t.qa[:, 0], tm, side='right')) - 1
    if i < 0: return (NAN,) * 5
    r = t.qa[i]; return (r[1], r[2], r[3], r[4], tm - r[0])
def main(day, maxlines=0, outdir=None):
    outdir = outdir or (D0 + 'formula_r1_28oct/out')
    units = []
    with gzip.open(UN % day, 'rt') as f:
        for r in csv.DictReader(f):
            if r['P_sh'] and float(r['P_sh']) >= 5 - 1e-9 and r['P_t1'] not in ('', 'None') and G.get(str(r['mercado'])) in ('YES', 'NO'):
                units.append(r)
    mk = sorted(set(r['mercado'] for r in units))
    mkf = outdir + '/mk_%s.txt' % day
    open(mkf, 'w').write(''.join('m%s\n' % m for m in mk))
    toks = {}; byk = {}; BNt = {}; BNp = {}
    p = stream(R5 % day, AWK5, mkf, maxlines)
    for ln in p.stdout:
        ty = ln[0]
        if ty == 'q':
            c0 = ln.split(',', 3); t = toks.get(c0[2])
            if t is None: continue
            c = ln.rstrip('\n').split(',')
            rv = c[7].strip(); tm = float(rv) if rv else float(c[1])
            if t.lo <= tm <= t.hi:
                bb = num(c[3]); ba = num(c[4])
                if bb == bb and ba == ba and bb > ba + E: continue
                t.q.extend((tm, bb, ba, num(c[5]), num(c[6])))
        elif ty == 'x':
            c = ln.rstrip('\n').split(',')
            if c[2] in SYMV:
                BNt.setdefault(c[2], array('d')).append(float(c[7])); BNp.setdefault(c[2], array('d')).append(float(c[3]))
        elif ty == 'k':
            c = ln.rstrip('\n').split(',')
            if c[2] in toks: continue
            cie = datetime.datetime.fromisoformat(c[6]).timestamp() * 1000
            toks[c[2]] = Tok(cie - 330000, cie + 10000); byk[(c[5], c[7])] = c[2]
    p.wait()
    toks15 = {}; k15 = {}
    p = stream(R15 % day, AWK15, None, maxlines)
    for ln in p.stdout:
        ty = ln[0]
        if ty == 'q':
            c0 = ln.split(',', 3); t = toks15.get(c0[2])
            if t is None: continue
            c = ln.rstrip('\n').split(',')
            rv = c[7].strip(); tm = float(rv) if rv else float(c[1])
            if t.lo <= tm <= t.hi:
                bb = num(c[3]); ba = num(c[4])
                if bb == bb and ba == ba and bb > ba + E: continue
                t.q.extend((tm, bb, ba, num(c[5]), num(c[6])))
        elif ty == 'k':
            c = ln.rstrip('\n').split(',')
            if c[2] in toks15: continue
            ts = datetime.datetime.fromisoformat(c[6]).timestamp()
            toks15[c[2]] = Tok(ts * 1000 - 940000, ts * 1000 + 10000); k15[(c[3], int(round(ts)), c[7])] = c[2]
    p.wait()
    for t in toks.values(): prep(t)
    for t in toks15.values(): prep(t)
    BN = {}
    for s in BNt:
        a = np.frombuffer(BNt[s], dtype=float); b = np.frombuffer(BNp[s], dtype=float); o = np.argsort(a, kind='stable'); BN[s] = (a[o], b[o])
    def bpr(sym, tm):
        if sym not in BN: return NAN
        bt, bp = BN[sym]; i = int(np.searchsorted(bt, tm, side='right')) - 1
        return NAN if i < 0 or tm - bt[i] > 60000 else bp[i]
    def brv(sym, tm):
        if sym not in BN: return NAN
        bt, bp = BN[sym]; g = tm - np.arange(61, -1, -1) * 1000.0
        idx = np.searchsorted(bt, g, side='right') - 1
        if idx.min() < 0 or tm - bt[idx[-1]] > 60000: return NAN
        pr = bp[idx]; s = np.diff(np.log(pr)).std(); return s if s > 0 else NAN
    def bref(sym, t0):
        if sym not in BN: return NAN
        bt, bp = BN[sym]; i0 = int(np.searchsorted(bt, t0 - 62000, side='left')); i1 = int(np.searchsorted(bt, t0 - 3000, side='right'))
        return float(bp[i0:i1].mean()) if i1 - i0 >= 5 else NAN
    rows = []
    for r in units:
        m = r['mercado']; side = r['lado']; oth = 'NO' if side == 'YES' else 'YES'; coin = r['coin']
        A = toks.get(byk.get((m, side))); Bt = toks.get(byk.get((m, oth)))
        if A is None or Bt is None or A.qa is None or len(A.qa) == 0 or len(Bt.qa) == 0: continue
        cie = float(r['cierre']); T = cie * 1000; sh = float(r['P_sh']); cost = float(r['P_cost']); p0 = cost / sh; t1 = float(r['P_t1'])
        win = 1.0 if G[str(m)] == side else 0.0
        T15 = math.ceil(cie / 900.0) * 900.0; extra = T15 - cie; jw = 3 - int(round(extra / 300.0)); t0 = T - 300000
        C = toks15.get(k15.get((coin, int(round(T15)), side)))
        sym = SYM[coin]; rb = bref(sym, t0)
        inst = [('n1', t1 - 250, 'N'), ('n0', t1 - 100, 'N'), ('e1', t1 + 250, 'E'), ('e2', t1 + 2000, 'E'), ('e3', t1 + 10000, 'E'), ('e4', t1 + 30000, 'E'),
                ('l1', T - 90000, 'L'), ('l2', T - 60000, 'L'), ('l3', T - 45000, 'L'), ('l4', T - 30000, 'L'), ('l5', T - 20000, 'L'), ('l6', T - 10000, 'L')]
        for lab, td, cl in inst:
            if cl != 'N' and not (td >= t1 + 250 - 1e-9 and td + LT <= T - 2000): continue
            a = ql(A, td); b = ql(Bt, td); c = ql(C, td); c0 = ql(C, t0) if jw >= 2 else (NAN,) * 5
            x = ql(A, td + LT) if cl != 'N' else (NAN,) * 5
            rows.append([day, coin, m, side, lab, cl, jw, extra, (T - td) / 1000.0, (td - t1) / 1000.0, p0, sh, cost, win,
                         a[0], a[1], a[2], a[3], a[4], b[0], b[1], b[2], b[3], b[4], x[0], x[2], x[4], c[0], c[1], c[4], c0[0], c0[1], c0[4],
                         bpr(sym, td), bpr(sym, td - 1000), bpr(sym, td - 5000), rb, brv(sym, td)])
    tmp = outdir + '/f_%s.csv.gz.tmp' % day
    with gzip.open(tmp, 'wt', newline='') as f:
        w = csv.writer(f); w.writerow(HDR)
        for r in rows: w.writerow(r)
    os.replace(tmp, outdir + '/f_%s.csv.gz' % day)
    print(day, 'unidades', len(units), 'filas', len(rows), 'tok5', len(toks), 'tok15', len(toks15), 'bn', len(BN), flush=True)
if __name__ == '__main__':
    a = sys.argv
    ml = int(a[a.index('--maxlines') + 1]) if '--maxlines' in a else 0
    od = a[a.index('--out') + 1] if '--out' in a else None
    main(a[1], ml, od)
