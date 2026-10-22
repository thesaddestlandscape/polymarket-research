"""Carga sim_*.npz y evalua politicas de puja tipo B sobre la cinta. Unidad = mercado (una puja, 5 acc). EV ponderado por EUR."""
import numpy as np, pandas as pd, glob
TKV = 295 - 5 * np.arange(47)
def load(dirn, days=None):
    D = []
    for f in sorted(glob.glob(dirn + '/sim_*.npz')):
        d = f[-14:-4]
        if days and d not in days: continue
        z = np.load(f, allow_pickle=True); D.append({k: z[k] for k in z.files})
    out = {}
    for k in D[0]:
        if k == 'TK': continue
        out[k] = np.concatenate([x[k] for x in D])
    return out
def price(q, delta): return np.floor(q * 100 + 1e-7) / 100 - 0.01 * np.asarray(delta)
def run(D, delta=1, tstart=300, tstop=60, gate=None, mode='cons', pmin=0.10, pmax=0.30, sel=None):
    """Devuelve DataFrame por mercado: quoted, filled, p, k, win, dia, act. gate: M x K bool (True = se puede cotizar). sel: mascara de mercados."""
    q = D['q']; p = price(q, delta)
    steps = (TKV <= tstart) & (TKV > tstop)
    valid = D['ok'] & (p >= pmin - 1e-9) & (p <= pmax + 1e-9) & steps[None, :]
    if gate is not None: valid &= gate
    if sel is not None: valid &= sel[:, None]
    mp = D['minpc']
    fillm = valid & ((mp < p - 1e-9) if mode == 'cons' else (mp <= p + 1e-9))
    kf = fillm.argmax(1); filled = fillm.any(1); quoted = valid.any(1)
    pf = np.where(filled, p[np.arange(len(p)), kf], np.nan)
    first_q = valid.argmax(1); pq = np.where(quoted, p[np.arange(len(p)), first_q], np.nan)
    return pd.DataFrame(dict(dia=D['dia'], act=D['act'], quoted=quoted, filled=filled, p=pf, pq=pq, k=np.where(filled, kf, -1), win=D['win'].astype(bool), fin=D['fin'], mkt=D['mkt']))
def unit_ev(R, shares=5, rebate=False):
    """Por mercado rellenado: c = 5p, pnl = 5(win - p) (+ rebate maker 20% de la comision 0,07 p(1-p) si rebate)."""
    r = R[R.filled].copy(); r['c'] = shares * r.p; r['p_'] = shares * (r.win.astype(float) - r.p)
    if rebate: r['p_'] += shares * 0.2 * 0.07 * r.p * (1 - r.p)
    return r.rename(columns={'p_': 'p'}) if False else r.assign(pnl=r.p_).drop(columns=['p_'])
def evtab(R, rebate=False, **kw):
    from sa_common import day_boot
    f = R[R.filled]
    if not len(f): return dict(ev=np.nan, lo=np.nan, hi=np.nan, ev_sin2=np.nan, dias=0, dpos=0, n=0, eur=0.0)
    c = 5 * f.p.values; pn = 5 * (f.win.values.astype(float) - f.p.values)
    if rebate: pn = pn + 5 * 0.2 * 0.07 * f.p.values * (1 - f.p.values)
    return day_boot(pd.DataFrame(dict(dia=f.dia.values, p=pn, c=c)), **kw)
def adv(R):
    f = R[R.filled]; u = R[R.quoted & ~R.filled]
    return dict(quoted=int(R.quoted.sum()), fill=int(len(f)), fr=len(f) / max(R.quoted.sum(), 1), win_f=f.win.mean() if len(f) else np.nan, p_f=f.p.mean() if len(f) else np.nan,
                win_u=u.win.mean() if len(u) else np.nan, pq_u=u.pq.mean() if len(u) else np.nan)
def run_static(D, p, tstart=300, tstop=60, mode='cons', gap=0.01, gate0=None):
    """Puja ESTATICA a precio fijo p (no persigue): colocada en el 1er paso con q valido y q-p >= gap, mantenida hasta tstop; relleno si minpc<p."""
    q = D['q']; steps = (TKV <= tstart) & (TKV > tstop)
    okk = D['ok'] & steps[None, :]
    place = okk & ((q - p) >= gap - 1e-9)
    if gate0 is not None: place &= gate0
    kp = place.argmax(1); quoted = place.any(1)
    after = np.arange(q.shape[1])[None, :] >= kp[:, None]
    mp = D['minpc']; fillm = after & quoted[:, None] & steps[None, :] & ((mp < p - 1e-9) if mode == 'cons' else (mp <= p + 1e-9))
    filled = fillm.any(1); kf = fillm.argmax(1)
    pf = np.where(filled, p, np.nan)
    return pd.DataFrame(dict(dia=D['dia'], act=D['act'], quoted=quoted, filled=filled, p=pf, pq=np.where(quoted, p, np.nan), k=np.where(filled, kf, -1), win=D['win'].astype(bool), fin=D['fin'], mkt=D['mkt']))
def dB(D): return np.where(D['act'] == 'ETH', 2, 1)[:, None]      # delta tipo B: ETH k=2, SOL/XRP k=1 (sobre la ultima operacion, no sobre el bid top)
def sub(D, m):
    return {k: v[m] for k, v in D.items()}
