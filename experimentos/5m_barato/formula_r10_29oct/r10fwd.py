#!/usr/bin/env python3
"""r10fwd: evaluacion FORWARD (solo dias > fecha de congelado D) de la regla R10 (BTC, INVERSION HGB, bid15 CORREGIDO clave +900). Sustituye a r9fwd.py (DEPRECADO).
Uso: nice -n 19 ionice -c3 python3 r10fwd.py 2026-10-30 [dia ...]   (fuera de 06-09Z; requiere m5/m15_registro del dia y desenlaces en cache)
     python3 r10fwd.py --check DIA     reproduccion de un dia ya incluido en el entrenamiento, en fwd_check/ (compara con hz_BTC.npz; no cuenta para el juez)
     python3 r10fwd.py --status        solo comprueba que el modelo congelado existe y cuadra con HASHES_R10.txt (ligero, no construye nada)
Requiere HASHES_R10.txt (escrito tras r10_train.py) con lineas '<sha256>  <fichero>' y una linea 'FECHA_CONGELADO YYYY-MM-DD'. Si falta algo: sale con codigo 2 y mensaje (fail-loud).
Idempotente: cada dia -> fwd/res_BTC_<dia>.json; el resumen se recalcula con todos los dias guardados. Solo lectura sobre datos vivos."""
import sys, os, json, pickle, hashlib, glob, re
R10 = '/root/polymarket-research/experimentos/5m_barato/formula_r10_29oct/'
def die(msg): print('R10FWD BLOQUEADO:', msg, file=sys.stderr, flush=True); sys.exit(2)
def congelado():
    """Devuelve (D, sha_modelo) validando HASHES_R10.txt y el pkl. Fail-loud."""
    hp = R10 + 'HASHES_R10.txt'; mp = R10 + 'frozen_R10_hgb_BTC.pkl'
    if not os.path.exists(hp): die('no existe HASHES_R10.txt (modelo R10 aun no congelado: esperar a run_r10.sh/r10_train.py)')
    if not os.path.exists(mp): die('no existe frozen_R10_hgb_BTC.pkl')
    txt = open(hp).read(); m = re.search(r'FECHA_CONGELADO\s+(\d{4}-\d{2}-\d{2})', txt)
    if not m: die('HASHES_R10.txt sin linea FECHA_CONGELADO YYYY-MM-DD')
    sha = hashlib.sha256(open(mp, 'rb').read()).hexdigest(); h = re.search(r'([0-9a-f]{64})\s+\*?frozen_R10_hgb_BTC\.pkl', txt)
    if not h: die('HASHES_R10.txt sin sha256 de frozen_R10_hgb_BTC.pkl')
    if h.group(1) != sha: die('sha del modelo %s != HASHES_R10 %s' % (sha, h.group(1)))
    return m.group(1), sha
if '--status' in sys.argv: D0, S0 = congelado(); print('OK modelo R10 sha', S0, 'congelado', D0, '-> forward limpio dias >', D0); sys.exit(0)
D0, SHA = congelado()  # antes de importar nada pesado
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/formula_r8_28oct')
import r8lib; from r8lib import *
import r5
sys.path.insert(0, E4 + 'formula_r7_28oct'); import r7_15m
FW = R10 + 'fwd/'; N = 10.0
SRC = open(R10 + 'r10_build.py').read()
def dedupe(sel, di, u, t):
    keep = np.zeros(len(sel), bool); lk = None; lt = -1e18
    for i in np.flatnonzero(sel):
        k = (di[i], u[i])
        if k != lk or t[i] - lt >= 10300.0: keep[i] = True; lk = k; lt = t[i]
    return keep
def build(day, coin='BTC'):
    ext = FW + 'ext_%s/' % coin; os.makedirs(ext + 'tmp/', exist_ok=True); os.makedirs(FW + 'k15/', exist_ok=True)
    r5.EXT = ext; r5.TMP = ext + 'tmp/'; r5.ext(day)
    r7_15m.OUT = FW + 'k15/'; r7_15m.run(day)
    r8lib.EXTD[coin] = ext; out = FW + 'hz_%s_%s.npz' % (coin, day)
    if not os.path.exists(out):
        src = SRC.replace("coin = sys.argv[1]; G = json.load(open(r4.I.CACHE)); days = days_incl()", "coin = %r; G = json.load(open(r4.I.CACHE)); days = [%r]" % (coin, day))
        src = src.replace("BASE.replace('formula_r8_28oct', 'formula_r7_28oct') + 'k15/k_%s.npz' % d", "%r + 'k_%%s.npz' %% d" % (FW + 'k15/')).replace("R10 + 'hz_%s.npz' % coin", repr(out))
        assert repr(out) in src and 'days = [' in src and "(float(D.cie[u]) - 300.0) // 900 * 900 + 900" in src, 'sustitucion de r10_build fallida'
        exec(compile(src, 'r10_build_fwd', 'exec'), dict(globals()))
    D = Day(day, coin); G = json.load(open(r4.I.CACHE)); cov = float(np.mean([G.get(str(m)) in ('YES', 'NO') for m in D.mks])) if D.n else 0.0
    return np.load(out, allow_pickle=True), cov, D.n
def evaluate(day, coin='BTC'):
    fo = FW + 'res_%s_%s.json' % (coin, day)
    if os.path.exists(fo): return json.load(open(fo))
    Z, cov, ntok = build(day, coin); F_ = Z['F'].astype(float); di = Z['di']; u = Z['u']; t = Z['t']; y = Z['y']; tg = Z['tg']; fl = Z['fl']
    M = pickle.load(open(R10 + 'frozen_R10_hgb_BTC.pkl', 'rb')); p = M['hgb'].predict_proba(F_)[:, 1]
    lg = np.log(np.clip(p, 1e-6, 1 - 1e-6) / (1 - np.clip(p, 1e-6, 1 - 1e-6))).reshape(-1, 1); sc = M['platt'].predict_proba(lg)[:, 1]; sel = np.isfinite(tg[:, 2]) & (sc <= M['thr'])
    k = dedupe(sel, di, u, t); f = fl[:, 2] & k
    r = dict(day=day, coin=coin, cobertura_desenlace=cov, tokens=int(ntok), filas=int(len(di)), ordenes=int(k.sum()), rellenos=int(f.sum()), num=float((N * (y - tg[:, 2]))[f].sum()), den=float((N * tg[:, 2])[f].sum()),
             frac_sel=float(sel.mean()) if len(sel) else 0.0, hash_modelo=SHA)
    json.dump(r, open(fo, 'w')); return r
def resumen():
    rs = [json.load(open(f)) for f in sorted(glob.glob(FW + 'res_BTC_*.json'))]; rs = [r for r in rs if r['day'] > D0 and r['den'] > 0 and r['cobertura_desenlace'] >= 0.99 and r.get('hash_modelo') == SHA]
    if not rs: print('BTC sin dias validos posteriores a', D0); return
    e = np.array([r['num'] / r['den'] for r in rs]); m, lo, hi = r4.tci(e) if len(e) > 2 else (e.mean(), np.nan, np.nan); s2 = float(np.sort(e)[:-2].mean()) if len(e) > 3 else float('nan')
    nf = sum(r['rellenos'] for r in rs); ev = sum(r['num'] for r in rs) / sum(r['den'] for r in rs)
    ok = len(e) >= 10 and nf >= 40 and ev >= 0.05 and lo > 0 and s2 > 0 and (e > 0).mean() >= 0.8
    print('BTC R10 forward %d dias (>%s) rellenos %d: EVw %+.3f dia %+.3f IC90 [%+.3f,%+.3f] +%d/%d sin2 %+.3f %.0f E/dia -> %s  (faltan comparadores SIEMPRE/ALEATORIO/ALTO y top-dia<=30%%: evaluar aparte)' % (len(e), D0, nf, ev, m, lo, hi, (e > 0).sum(), len(e), s2, np.mean([r['den'] for r in rs]), 'CUMPLE GATE parcial' if ok else ('EN CURSO (<10 dias o n<40)' if len(e) < 10 or nf < 40 else 'NO CUMPLE')))
if __name__ == '__main__':
    CHK = len(sys.argv) > 1 and sys.argv[1] == '--check'
    if CHK: FW = R10 + 'fwd_check/'; sys.argv.pop(1)
    os.makedirs(FW, exist_ok=True)
    for d in sys.argv[1:]:
        assert CHK or d > D0, 'solo dias posteriores al congelado (%s)' % D0
        try: print(evaluate(d), flush=True)
        except Exception as ex: print(d, 'ERROR', repr(ex), flush=True)
    resumen()
