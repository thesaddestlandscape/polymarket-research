#!/usr/bin/env python3
"""r9fwd: evaluacion FORWARD (dias >= 2026-10-28, unico OOS limpio) de las reglas congeladas E2 (BTC INVERSION HGB) y E5 (ETH T120-200 bajo m=3).
Uso: nice -n 19 ionice -c3 python3 r9fwd.py 2026-10-28 [2026-10-29 ...]   (fuera de 06-09Z; requiere m5/m15_registro del dia y desenlaces en cache)
Idempotente: cada dia se guarda en fwd/res_<coin>_<dia>.json; el resumen se recalcula con todos los dias guardados. No toca nada vivo."""
import sys, os, json, pickle, hashlib, glob; sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
import r8lib; from r8lib import *
import r5
sys.path.insert(0, E4 + 'formula_r7_28oct'); import r7_15m
R9 = E4 + 'formula_r9_28oct/'; FW = R9 + 'fwd/'; N = 10.0
HASH = {'frozen_E2_hgb_BTC.pkl': None, 'frozen_E5_logit_ETH.pkl': None}
for k in HASH: HASH[k] = hashlib.sha256(open(R9 + k, 'rb').read()).hexdigest()
SRC = open(BASE + 'r8h_build.py').read()
def dedupe(sel, di, u, t):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
def build(day, coin):
    ext = FW + 'ext_%s/' % coin; os.makedirs(ext + 'tmp/', exist_ok=True); os.makedirs(FW + 'k15/', exist_ok=True)
    r5.EXT = ext; r5.TMP = ext + 'tmp/'; awk0 = r5.AWK
    if coin == 'ETH': r5.AWK = awk0.replace('"BTC"', '"ETH"').replace('BTCUSDT', 'ETHUSDT')
    r5.ext(day); r5.AWK = awk0
    if coin == 'BTC': r7_15m.OUT = FW + 'k15/'; r7_15m.run(day)
    r8lib.EXTD[coin] = ext; out = FW + 'hz_%s_%s.npz' % (coin, day)
    if not os.path.exists(out):
        src = SRC.replace("coin = sys.argv[1]; G = json.load(open(r4.I.CACHE)); days = days_incl()", "coin = %r; G = json.load(open(r4.I.CACHE)); days = [%r]" % (coin, day))
        src = src.replace("BASE.replace('formula_r8_28oct', 'formula_r7_28oct') + 'k15/k_%s.npz' % d", "%r + 'k_%%s.npz' %% d" % (FW + 'k15/')).replace("BASE + 'hz_%s.npz' % coin", repr(out))
        assert repr(out) in src and 'days = [' in src; exec(compile(src, 'r8h_build_fwd', 'exec'), dict(globals()))
    D = Day(day, coin); G = json.load(open(r4.I.CACHE)); cov = float(np.mean([G.get(str(m)) in ('YES', 'NO') for m in D.mks])) if D.n else 0.0
    return np.load(out, allow_pickle=True), cov, D.n
def evaluate(day, coin):
    fo = FW + 'res_%s_%s.json' % (coin, day)
    if os.path.exists(fo): return json.load(open(fo))
    Z, cov, ntok = build(day, coin); F_ = Z['F'].astype(float); COLS = list(Z['cols']); di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; tg = Z['tg']; fl = Z['fl']
    if coin == 'BTC':
        M = pickle.load(open(R9 + 'frozen_E2_hgb_BTC.pkl', 'rb')); p = M['hgb'].predict_proba(F_)[:, 1]
        lg = np.log(np.clip(p, 1e-6, 1 - 1e-6) / (1 - np.clip(p, 1e-6, 1 - 1e-6))).reshape(-1, 1); sc = M['platt'].predict_proba(lg)[:, 1]; sel = np.isfinite(tg[:, 2]) & (sc <= M['thr'])
    else:
        M = pickle.load(open(R9 + 'frozen_E5_logit_ETH.pkl', 'rb')); C = M['cols']
        A = np.hstack([np.where(np.isnan(F_), 0.0, F_), np.isnan(F_[:, [C.index(c) for c in ('cbb', 'bid15', 'comp_acc5')]]).astype(float)])
        sc = M['logit'].decision_function(M['scaler'].transform(A)); tr = F_[:, C.index('trem')]; sel = np.isfinite(tg[:, 2]) & (sc <= M['thr']) & (tr >= 120) & (tr < 200)
    k = dedupe(sel, di, u, t); f = fl[:, 2] & k
    r = dict(day=day, coin=coin, cobertura_desenlace=cov, tokens=int(ntok), filas=int(len(di)), ordenes=int(k.sum()), rellenos=int(f.sum()), num=float((N * (y - tg[:, 2]))[f].sum()), den=float((N * tg[:, 2])[f].sum()),
             frac_sel=float(sel.mean()) if len(sel) else 0.0, hash_modelo=HASH['frozen_E2_hgb_BTC.pkl' if coin == 'BTC' else 'frozen_E5_logit_ETH.pkl'])
    json.dump(r, open(fo, 'w')); return r
def resumen():
    for coin in ('BTC', 'ETH'):
        rs = [json.load(open(f)) for f in sorted(glob.glob(FW + 'res_%s_*.json' % coin))]; rs = [r for r in rs if r['den'] > 0 and r['cobertura_desenlace'] >= 0.99]
        if not rs: print(coin, 'sin dias validos'); continue
        e = np.array([r['num'] / r['den'] for r in rs]); m, lo, hi = r4.tci(e) if len(e) > 2 else (e.mean(), np.nan, np.nan); s2 = float(np.sort(e)[:-2].mean()) if len(e) > 3 else float('nan')
        ok = len(e) >= 10 and sum(r['num'] for r in rs) / sum(r['den'] for r in rs) >= 0.05 and lo > 0 and s2 > 0 and (e > 0).mean() >= 0.8
        print('%s forward %d dias: EVw %+.3f dia %+.3f IC90 [%+.3f,%+.3f] +%d/%d sin2 %+.3f %.0f E/dia -> %s' % (coin, len(e), sum(r['num'] for r in rs) / sum(r['den'] for r in rs), m, lo, hi, (e > 0).sum(), len(e), s2, np.mean([r['den'] for r in rs]), 'CUMPLE GATE' if ok else ('EN CURSO (<10 dias)' if len(e) < 10 else 'NO CUMPLE')))
if __name__ == '__main__':
    CHK = sys.argv[1] == '--check'  # reproduccion de un dia ya incluido (p.ej. 2026-10-27) en fwd_check/, comparar con hz_*.npz
    if CHK: FW = R9 + 'fwd_check/'; sys.argv.pop(1)
    os.makedirs(FW, exist_ok=True)
    for d in sys.argv[1:]:
        assert CHK or d >= '2026-10-28', 'solo dias forward'
        for coin in ('BTC', 'ETH'):
            try: print(evaluate(d, coin), flush=True)
            except Exception as ex: print(d, coin, 'ERROR', repr(ex), flush=True)
    resumen()
