#!/usr/bin/env python3
"""replay_train.py DIA [--sin-ws] -- PRUEBA DE REPRODUCCION del nucleo del dry-run contra el motor v3 en un dia TRAIN (26-Oct..09-Nov; HOLD >=10-Nov prohibido). SOLO LECTURA, 0 ordenes.
Carga el dia con el PREAMBULO del propio passT_cxb_v3.py (exec de su texto hasta '# ===== PASO 4-6': mismos datos, mismo sello v3, mismo E/D/K/FE; nada copiado) y compara con out_v3/CX_v3dd_<D>.pkl:
  MODO A (exactitud de la maquina): features del motor (FE[k]) inyectadas + relleno del motor (E.run_segment) -> la maquina incremental debe reproducir EXACTAMENTE n_seg/n_canc/n_fill/pnl y cada relleno (k, L, seg, t_dec, tf, q, canc)
         de G0, GEO1, CXB60, CXB100, CXB150. Tolerancia: 0 diferencias (pnl a 1e-9).
  MODO B (ruta VIVA): features calculadas por TokenFeats desde los buffers RX (filas q/t del npz ms2 como las daria el tailer en vivo: ex, rx, bid, ask, szb, sza) + relleno con MiniDay (cinta = prints WS, sello ex - C_PRINT - 1)
         en vez de cinta on-chain+firma exacta. Se REPORTA la diferencia respecto del motor (n_fill, pnl, EV, tasa de coincidencia de rellenos); es la cota de lo que cambia al pasar de on-chain a WS en vivo.
Uso de memoria: ~3,5 GB (el preambulo del motor); lanzar con nice 19 ionice -c3, ulimit -v 3700000 y fuera de 06-09Z."""
import os, sys, json, time, gc
import numpy as np, pandas as pd
ARGV0 = list(sys.argv); T0 = time.time(); HERE = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, HERE)
D_ = sys.argv[1]; assert D_ <= '2026-11-09', 'HOLD >= 10-Nov no se usa'
OUTD = HERE + 'out_replay/'; os.makedirs(OUTD, exist_ok=True)
import cxb60_core as C
MOTOR = C.HERE + 'passT_cxb_v3.py'; src = open(MOTOR).read(); pre = src[:src.index('# ======================= PASO 4-6')]
os.environ['PASST_OUT'] = OUTD + 'motor_scratch/'; sys.argv = [MOTOR, 'v3', 'dd', D_]
ns = {'__file__': MOTOR, '__name__': 'motor_preambulo'}; exec(compile(pre, MOTOR, 'exec'), ns)
E, D, K, FE, ks, G = ns['E'], ns['D'], ns['K'], ns['FE'], ns['ks'], ns['G']
SUB = None
if '--ks-sel' in ARGV0:                                   # subconjunto COIN:H0-H1 (hora UTC, fin en (H0,H1]); el motor ya esta cargado: solo reduce los mercados de la comparacion (no toca el motor)
    c_, hh = ARGV0[ARGV0.index('--ks-sel') + 1].split(':'); h0_, h1_ = map(int, hh.split('-')); d0_ = int(pd.Timestamp(D_, tz='UTC').timestamp()); SUB = (c_.upper(), h0_, h1_)
    ks = [k for k in ks if str(D.act[k]).upper() == c_.upper() and d0_ + h0_ * 3600 < int(D.fin[k]) <= d0_ + h1_ * 3600]
print('preambulo motor', round(time.time() - T0, 1), 's, mercados', len(ks), 'subconjunto', SUB, flush=True)
GOLD_DIR = os.environ.get('CXB60_GOLD_DIR') or (C.HERE + 'out_v3/'); gold = pd.read_pickle(GOLD_DIR + f'CX_v3dd_{D_}.pkl'); print('gold:', GOLD_DIR, flush=True); VARS = ['G0', 'GEO1', 'CXB60', 'CXB100', 'CXB150']
GR = gold['R'][gold['R']['var'].isin(VARS)]; GA = gold['A'][gold['A']['var'].isin(VARS)]
if SUB: GR = GR[GR['k'].isin(set(ks))]                                  # subconjunto: solo se comparan los rellenos de esos mercados (la tabla agregada A no es filtrable por k)
SPECS = [C.VSpec('G0', 'G0'), C.VSpec('GEO1', 'GEO1'), C.VSpec('CXB60', 'CXB', l=60), C.VSpec('CXB100', 'CXB', l=100), C.VSpec('CXB150', 'CXB', l=150)]

# ---- buffers vivos desde el npz ms2 (mismos campos que las filas q/t del registro ms)
z = np.load('/root/polymarket-research-datalogs/sa_ms2/' + f'ms2_{D_}.npz', allow_pickle=True); t0 = int(z['t0']); qk = z['q_k']; oq = np.lexsort((np.arange(len(qk)), z['q_t_rx'].astype(np.int64), qk))
qk_s = qk[oq]; qb = np.searchsorted(qk_s, np.arange(len(z['tokens']) + 1)); del qk_s; QX = z['q_t_ex'][oq]; QR = z['q_t_rx'][oq]      # int32 relativos a t0 (memoria)
QV = [z[f'q_v{j}'][oq] for j in range(4)]; QOK = QR >= 0; del qk
tk = z['t_k']; ot = np.lexsort((np.arange(len(tk)), z['t_t_rx'].astype(np.int64), tk)); tk_s = tk[ot]; tb = np.searchsorted(tk_s, np.arange(len(z['tokens']) + 1))
TX = z['t_t_ex'][ot]; TR = z['t_t_rx'][ot]; TP = z['t_pr'][ot]; TS = z['t_sd'][ot]; TZ = z['t_sz'][ot]; TOK = list(z['tokens']); del oq, ot; z = None


def mkbuf(k):
    """TokBuf con arrays numpy (sin listas de Python: 18 M filas/dia no caben); misma estructura que rellena el tailer en vivo."""
    b = C.TokBuf(); a, e = qb[k], qb[k + 1]; m = QOK[a:e]
    b.qrx = QR[a:e][m].astype(np.int64) + t0; b.qex = QX[a:e][m].astype(np.int64) + t0; b.qbid = QV[0][a:e][m].astype(np.float64); b.qask = QV[1][a:e][m].astype(np.float64); b.qszb = QV[2][a:e][m].astype(np.float64); b.qsza = QV[3][a:e][m].astype(np.float64)
    a, e = tb[k], tb[k + 1]; m = TR[a:e] >= 0
    b.trx = TR[a:e][m].astype(np.int64) + t0; b.tex = TX[a:e][m].astype(np.int64) + t0; b.tp = TP[a:e][m].astype(np.float64); b.tbuy = TS[a:e][m].astype(np.float64); b.tsz = TZ[a:e][m].astype(np.float64); return b


class Inj(C.TokenFeats):
    def __init__(self, tok, fin, arr, buf):
        super().__init__(tok, fin, buf, None, None); self.arr = arr

    def extend(self, t_known):
        m1 = int(min(self.n, max(0, (t_known - self.g[0]) // C.GRID + 1))) if t_known >= self.g[0] else 0
        if m1 <= self.m: return
        a = self.arr; s = slice(self.m, m1); self._apply(self.g[s], a[0][s], a[1][s], a[2][s], a[3][s], a[4][s]); self.m = m1


def agregar(recs, k_of, gana_of, k):
    pass


def correr(modo):
    get = lambda kk: mkbuf(kk) if kk is not None else C.TokBuf()      # sin cache: un buffer por mercado (la cache de todo el dia agota la memoria)
    R = []; A = {}; feat_cmp = dict(ticks=0, can_igual=0)
    for ik, k in enumerate(ks):
        if ik % 100 == 99: gc.collect(); print('  mercado', ik + 1, 'de', len(ks), 'RSS', int(int(open('/proc/self/statm').read().split()[1]) * os.sysconf('SC_PAGE_SIZE') / 1048576), 'MB', flush=True)
        tok = D.toks[k]; fin = int(D.fin[k]); kc = D.comp(k); coin = D.act[k]; lado = D.lado[k]; gana = G.capt_outcome(E, k); mk = dict(tok=tok, mid=D.mid[k], lado=lado, coin=coin, fin=fin)
        mc = dict(tok=D.toks[kc], mid=D.mid[kc], lado=D.lado[kc], coin=coin, fin=fin) if kc is not None else dict(tok='sin_comp', mid=D.mid[k], lado='NO' if lado == 'YES' else 'YES', coin=coin, fin=fin)
        buf = get(k); bcomp = get(kc); f15 = int(np.ceil(fin / 900.0) * 900); k15 = D.t15.get((coin, f15, lado)); b15buf = get(k15) if k15 is not None else None
        g, bid, ask, b15, vol, hora = FE[k]; b300 = E.quotes(k, g - 300)[0]
        if modo == 'A':
            F0 = Inj(tok, fin, (bid, ask, b300, b15, vol), buf); fill = lambda t_, L, ta, te, rem, k=k: E.run_segment(k, L, ta, te, rem, 'BASE')
        else:
            F0 = C.TokenFeats(tok, fin, buf, bcomp, b15buf); bufs = {tok: (buf, bcomp)}
            fill = C.make_live_fill(lambda t_: bufs[t_], lambda t_, mk=mk, mc=mc: [mk, mc])
        mkt = C.Market.__new__(C.Market); mkt.tok, mkt.fin, mkt.coin = tok, fin, coin; mkt.F = F0; key = int(k)
        mkt.M = [C.VMachine(sp, F0, L, key) for L in C.LEVELS for sp in SPECS]; mkt.closed = False
        for rec in mkt.advance(10 ** 18, fill):
            q = rec['q']; ag = A.setdefault((rec['var'], coin, rec['L']), [0, 0, 0, 0.0, 0.0]); ag[0] += 1; ag[1] += rec['canc']
            if q > 1e-9:
                pnl = C.pnl_of(q, rec['L'], gana); ag[2] += 1; ag[3] += q * rec['L']; ag[4] += pnl
                R.append((rec['var'], k, rec['L'], rec['seg'], rec['t_dec_rx'], rec['tf'], q, rec['canc'], pnl, coin))
        if modo == 'B':
            F0.extend(10 ** 18)
            for L in C.LEVELS:
                can_m = (G.gate_vec('G', L, b15, vol, hora) & np.isfinite(ask) & (ask > L + C.EPS)); can_l = F0.code[L] == 0; feat_cmp['ticks'] += len(can_m); feat_cmp['can_igual'] += int((can_m == can_l).sum())
    return R, A, feat_cmp


def comparar(R, A, nombre):
    Rd = pd.DataFrame(R, columns=['var', 'k', 'L', 'seg', 't_dec', 'tf', 'q', 'canc', 'pnl', 'act'])
    g = GR.rename(columns={'t_dec': 't_dec', 'tf': 'tf'})[['var', 'k', 'L', 'seg', 't_dec', 'tf', 'q', 'canc', 'pnl']]
    m = Rd.merge(g, on=['var', 'k', 'L', 'seg'], how='outer', suffixes=('_r', '_g'), indicator=True)
    both = m[m._merge == 'both']; exact = ((both.t_dec_r == both.t_dec_g) & (both.tf_r == both.tf_g) & (abs(both.q_r - both.q_g) < 1e-9) & (both.canc_r == both.canc_g) & (abs(both.pnl_r - both.pnl_g) < 1e-9)).sum()
    ne = both[~((both.t_dec_r == both.t_dec_g) & (both.tf_r == both.tf_g) & (abs(both.q_r - both.q_g) < 1e-9) & (both.canc_r == both.canc_g) & (abs(both.pnl_r - both.pnl_g) < 1e-9))]
    if len(ne): print('FILAS NO IDENTICAS (replay _r vs motor _g):'); print(ne.drop(columns=['_merge']).to_string(index=False))
    print(f'\n=== MODO {nombre}: rellenos replay {len(Rd)} vs motor {len(g)}; coinciden (var,k,L,seg) {len(both)}, identicos {int(exact)}, solo replay {(m._merge == "left_only").sum()}, solo motor {(m._merge == "right_only").sum()}')
    rows = []
    for v in (VARS if not SUB else []):
        a = [(c, L, *x) for (vv, c, L), x in A.items() if vv == v]; ga = GA[GA['var'] == v]
        rows.append(dict(var=v, seg_r=sum(x[2] for x in a), seg_m=int(ga.n_seg.sum()), canc_r=sum(x[3] for x in a), canc_m=int(ga.n_canc.sum()), fill_r=sum(x[4] for x in a), fill_m=int(ga.n_fill.sum()),
                         pnl_r=round(sum(x[6] for x in a), 3), pnl_m=round(float(ga.pnl.sum()), 3), ev_r=round(sum(x[6] for x in a) / max(sum(x[5] for x in a), 1e-9), 4), ev_m=round(float(ga.pnl.sum() / max(ga.cost.sum(), 1e-9)), 4)))
    T = pd.DataFrame(rows, columns=['var', 'seg_r', 'seg_m', 'canc_r', 'canc_m', 'fill_r', 'fill_m', 'pnl_r', 'pnl_m', 'ev_r', 'ev_m']); print(T.to_string(index=False)); return T, dict(identicos=int(exact), replay=len(Rd), motor=len(g), solo_replay=int((m._merge == 'left_only').sum()), solo_motor=int((m._merge == 'right_only').sum()))


if __name__ == '__main__':
    res = {}
    modos = ['A'] + ([] if '--sin-ws' in ARGV0 else ['B'])
    for modo in modos:
        t = time.time(); R, A, fc = correr(modo); T, st = comparar(R, A, modo); print('  tiempo', round(time.time() - t, 1), 's', ('features: ticks %d, can igual al motor %.4f' % (fc['ticks'], fc['can_igual'] / max(fc['ticks'], 1))) if modo == 'B' else '')
        res[modo] = dict(tabla=T.to_dict('records'), rellenos=st, features=fc)
        if modo == 'A':
            ok = ((T.seg_r == T.seg_m).all() and (T.canc_r == T.canc_m).all() and (T.fill_r == T.fill_m).all() and (abs(T.pnl_r - T.pnl_m) < 1e-6).all() if not SUB else True) and st['identicos'] == st['motor'] == st['replay'] and st['solo_replay'] == 0 and st['solo_motor'] == 0; print('MODO A EXACTO:', bool(ok)); res['A']['exacto'] = bool(ok)
    json.dump(dict(dia=D_, **res), open(OUTD + f'replay_{D_}.json', 'w'), indent=1, default=str); print('listo', round(time.time() - T0, 1), 's')
