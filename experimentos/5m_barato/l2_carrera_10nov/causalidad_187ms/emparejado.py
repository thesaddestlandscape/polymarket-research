#!/usr/bin/env python3
"""Emparejado INDEPENDIENTE print<->consumo L1 (solo lectura). DIA.
Unidad: (token, tx) de la cinta on-chain (tape, maker BUY = consumo del BID del token) con print t_ev (EXCHANGE, libro5_tx) y recv (RX).
Firma de consumo en filas q (sa_ms2, reloj EXCHANGE): exacta = bid==p antes y (bid==p y szb baja exactamente S) o (bid<p y szb previo==S).
Ventana SIMETRICA [t_ev-W, t_ev+W] EX; placebo = misma busqueda con t_ev +/-20 s (mismo token).
Compara con la regla vieja (primera transicion bid>p -> bid<=p en [recv-400, recv] por RX)."""
import sys, json, glob, numpy as np, pandas as pd
d = sys.argv[1]; OUT = sys.argv[2]
W = 1500; TOLP = 0.0049; TOLS = 0.015; SH = (20000, -20000)
PB = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/precursores_barrido/out/'
z = np.load(f'/root/polymarket-research-datalogs/sa_ms2/ms2_{d}.npz', allow_pickle=True)
toks = list(z['tokens']); tokidx = {t: i for i, t in enumerate(toks)}; t0 = int(z['t0'])
qk = z['q_k']; qb = np.searchsorted(qk, np.arange(len(toks) + 1)); del qk
EX = z['q_t_ex']; RXa = z['q_t_rx']   # int32 relativos a t0
B = z['q_v0']; A = z['q_v1']; Z = z['q_v2']
tape = pd.read_pickle(PB + f'tape_{d}.pkl'); tape = tape[(tape.src == 'tx_ws') & (tape.side == 0)]
tape = tape.assign(k=tape.token_id.map(tokidx)); tape = tape[tape.k.notna()]; tape['k'] = tape.k.astype(int)
tape['p'] = tape.price.round(3)
txs = set(tape.tx.unique()); TEV = {}
for dd in [(pd.Timestamp(d) + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in (-1, 0, 1)]:
    for f in sorted(glob.glob(f'/mnt/HC_Volume_106538179/libro5_tx/libro5_tx_{dd}_*.csv.gz')):
        for ch in pd.read_csv(f, header=None, names=['t_ev', 'token', 'tx', 'recv'], usecols=['t_ev', 'tx', 'recv'], dtype={'tx': str}, chunksize=500000):
            ch = ch[ch.tx.isin(txs)]
            for tx, te, rc in zip(ch.tx.values, ch.t_ev.values, ch.recv.values):
                o = TEV.get(tx)
                if o is None or te < o[0]: TEV[tx] = (int(te), int(rc))
lv = tape.groupby(['k', 'tx', 'p']).agg(S=('sh', 'sum'), nmk=('maker', 'nunique')).reset_index()
ev = lv.groupby(['k', 'tx']).agg(npr=('p', 'size'), pmin=('p', 'min'), pmax=('p', 'max'), S=('S', 'sum'), nmk=('nmk', 'sum')).reset_index()
ev['tev'] = ev.tx.map(lambda x: TEV.get(x, (t0 - 1, t0 - 1))[0] - t0); ev['rcv'] = ev.tx.map(lambda x: TEV.get(x, (t0 - 1, t0 - 1))[1] - t0)
n_ev_total = len(ev); ev = ev[ev.tev >= 0].reset_index(drop=True)
def sig_rows(a, b, i0, i1, p, S, npr, pmin):
    """indices (absolutos) de filas firma en [i0,i1) (i>a). exacta / laxa / salto multinivel."""
    i0 = max(i0, a + 1)
    if i1 <= i0: return np.array([], int), np.array([], int)
    bp = B[i0 - 1:i1 - 1]; bc = B[i0:i1]; zp = Z[i0 - 1:i1 - 1]; zc = Z[i0:i1]
    if npr == 1:
        atp = np.abs(bp - p) < TOLP
        dec = atp & (np.abs(bc - p) < TOLP) & (np.abs((zp - zc) - S) <= TOLS)
        clr = atp & (bc < p - TOLP) & (np.abs(zp - S) <= TOLS)
        exact = dec | clr
        loose = atp & ((bc < p - TOLP) | ((np.abs(bc - p) < TOLP) & (zc < zp - TOLS)))
    else:   # barrido: una sola fila que salta de bid>=pmax a bid<=pmin
        exact = (bp >= p - TOLP) & (bc <= pmin + TOLP)
        loose = (bp >= p - TOLP) & (bc < p - TOLP)
    return np.where(exact)[0] + i0, np.where(loose)[0] + i0
rows = []; HE = {s: [] for s in ('real',) + SH}; HL = {s: [] for s in ('real',) + SH}
for r in ev.itertuples():
    k = r.k; a, b = qb[k], qb[k + 1]
    if b - a < 3: continue
    p = r.pmax; e = EX[a:b]
    res = {}
    for s in ('real',) + SH:
        tq = r.tev + (0 if s == 'real' else s)
        i0 = a + np.searchsorted(e, tq - W, 'left'); i1 = a + np.searchsorted(e, tq + W, 'right')
        ex_, lo_ = sig_rows(a, b, i0, i1, p, r.S, r.npr, r.pmin)
        HE[s].append(tq - EX[ex_]); HL[s].append(tq - EX[lo_]); res[s] = (ex_, lo_)
    ex_, lo_ = res['real']
    # regla vieja (diag/passT causal): primera transicion bid>pmin -> bid<=pmin en [rcv-400, rcv] por RX (filas ordenadas por rx dentro del token)
    rx = RXa[a:b]; o = np.argsort(rx, kind='stable'); rxs = rx[o]
    j0 = np.searchsorted(rxs, r.rcv - 400, 'left'); j1 = np.searchsorted(rxs, r.rcv, 'right'); old = -1
    if j1 > j0 and j0 > 0:
        v = B[a + o[j0 - 1:j1]]; lo = v <= r.pmin + TOLP; w = np.where(lo[1:] & ~lo[:-1])[0]
        if len(w): old = a + o[j0 + w[0]]
    near = -1
    if len(ex_): near = ex_[np.argmin(np.abs(r.tev - EX[ex_]))]
    crossed = bool(near >= 0 and np.isfinite(A[near]) and A[near] > 0 and B[near] >= A[near] - 1e-6)
    rows.append((d, k, r.tx, r.npr, r.pmin, r.pmax, r.S, r.nmk, r.tev, r.rcv, len(ex_), len(lo_),
                 int(r.tev - EX[near]) if near >= 0 else None, int(r.rcv - RXa[near]) if near >= 0 else None, int(RXa[near] - EX[near]) if near >= 0 else None,
                 int(r.tev - EX[old]) if old >= 0 else None, int(r.rcv - RXa[old]) if old >= 0 else None,
                 bool(old >= 0 and near >= 0 and old == near), bool(old >= 0 and old in set(ex_.tolist())), bool(old >= 0 and old in set(lo_.tolist())), crossed,
                 int((r.tev - EX[ex_] > 0).sum()), int((r.tev - EX[ex_] <= 0).sum())))
R = pd.DataFrame(rows, columns=['dia', 'k', 'tx', 'npr', 'pmin', 'pmax', 'S', 'nmk', 'tev', 'rcv', 'n_exact', 'n_loose', 'd_ex_near', 'd_rx_near', 'lag_q_near',
                                'd_ex_old', 'd_rx_old', 'old_is_near', 'old_in_exact', 'old_in_loose', 'crossed_near', 'n_ex_before', 'n_ex_after'])
R.to_pickle(OUT + f'/EMP_{d}.pkl')
def hist(L):
    x = np.concatenate([np.asarray(v, np.int64) for v in L]) if L else np.array([], np.int64)
    return np.histogram(x, bins=np.arange(-W, W + 1, 10))[0].tolist()
json.dump(dict(dia=d, n_ev_total=n_ev_total, n_ev_tev=len(ev), n_proc=len(R), W=W, bins10=list(range(-W, W, 10)),
               H_exact={str(s): hist(HE[s]) for s in HE}, H_loose={str(s): hist(HL[s]) for s in HL}), open(OUT + f'/HIST_{d}.json', 'w'))
print(d, 'ev', n_ev_total, 'con_tev', len(ev), 'proc', len(R), 'exact>=1', int((R.n_exact > 0).sum()), 'exact==1', int((R.n_exact == 1).sum()), 'old', int(R.d_ex_old.notna().sum()), flush=True)
