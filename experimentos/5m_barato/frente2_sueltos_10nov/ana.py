#!/usr/bin/env python3
"""FRENTE 2 sueltos: analisis (EXPLORATORIO, dias quemados). Lee out/F_*.pkl de ext.py. EV ponderado por EUR (sum pnl / sum coste).
IC90 bootstrap POR DIA (2000). TRAIN = 26-31 Oct (6 d), HOLD = 01-04 + 07-08 Nov (6 d). Umbrales elegidos SOLO en TRAIN.
Salida tomadora: precio = bid a decision+250 ms (red 68 + taker delay 145), fee tomador 0,07*b*(1-b) por accion; profundidad L1:
si bsz < q el resto se vende a bid-0,01 (pesimista). Delta(salida) = q*(b_neto - gana) (el rebate de entrada no cambia)."""
import glob, sys, numpy as np, pandas as pd
H = '/root/polymarket-research/experimentos/5m_barato/frente2_sueltos_10nov/'
F = pd.concat([pd.read_pickle(f) for f in sorted(glob.glob(H + 'out/F_*.pkl'))], ignore_index=True)
F = F[F.R0 >= 0].copy()
TR = {'2026-10-26', '2026-10-27', '2026-10-28', '2026-10-29', '2026-10-30', '2026-10-31'}
F['per'] = np.where(F.dia.isin(TR), 'TRAIN', 'HOLD'); F['suelto'] = F.R0 == 0
F['Tdec'] = F.fin - F.t_dec / 1000.0; F['hora'] = (F.tf // 3600000) % 24; F['cola_ms'] = F.tf - (F.t_dec + 68)
F['mid_p1000'] = (F.bid_p1000 + F.ask_p1000) / 2; F['mid_p5000'] = (F.bid_p5000 + F.ask_p5000) / 2; F['mid_p30000'] = (F.bid_p30000 + F.ask_p30000) / 2
F['mid_m300'] = (F.bid_m300 + F.ask_m300) / 2; F['spread_dec'] = F.ask_dec - F.bid_dec; F['g15'] = F.b15_dec - F.L
RNG = np.random.default_rng(12345); DAYS = sorted(F.dia.unique())
def fee(b): return 0.07 * b * (1 - b)
def bnet(b, s, q):   # ingreso neto por accion vendiendo q al bid b con tamano visible s (resto a b-0,01)
    b = np.asarray(b, float); s = np.nan_to_num(np.asarray(s, float), nan=0.0); q = np.asarray(q, float)
    b2 = np.maximum(b - 0.01, 0.0); f1 = np.minimum(s, q) / q
    return f1 * (b - fee(b)) + (1 - f1) * (b2 - fee(b2))
def ev(df): c = df.cost.sum(); return df.pnl.sum() / c if c > 0 else np.nan
def boot_days(df, val, den, B=2000):
    g = df.groupby('dia').agg(v=(val, 'sum'), c=(den, 'sum')); dd = g.index.values; v = g.v.values; c = g.c.values
    if len(dd) == 0: return (np.nan, np.nan)
    ix = RNG.integers(0, len(dd), (B, len(dd))); r = v[ix].sum(1) / c[ix].sum(1); return tuple(np.percentile(r, [5, 95]))
def sin2(df, val, den):   # quitando los 2 mejores dias (por val)
    g = df.groupby('dia').agg(v=(val, 'sum'), c=(den, 'sum')).sort_values('v')
    g = g.iloc[:-2] if len(g) > 2 else g; return g.v.sum() / g.c.sum() if g.c.sum() > 0 else np.nan
def line(nm, df, val='pnl', den='cost'):
    if len(df) == 0: return f'{nm:34s} n=0'
    lo, hi = boot_days(df, val, den); g = df.groupby('dia')[val].sum()
    return f'{nm:34s} n={len(df):5d} EUR={df[den].sum():7.1f} pnl={df[val].sum():+7.1f} EV={df[val].sum()/df[den].sum():+.3f} IC90d=({lo:+.3f},{hi:+.3f}) sin2={sin2(df, val, den):+.3f} dias-={int((g<0).sum())}/{len(g)}'
out = []
P = lambda s='': out.append(s)
P('== 0. Reproduccion (12 d, 26-Oct..04-Nov + 07-08 Nov, G0 S_sim etiquetado R0)')
P(line('TODO', F)); P(line('rafaga R0=1', F[~F.suelto])); P(line('suelto R0=0', F[F.suelto]))
for per in ('TRAIN', 'HOLD'): P(line(f'suelto {per}', F[F.suelto & (F.per == per)]))
SU = F[F.suelto].copy()
P(); P('== 1. De donde viene la perdida de los SUELTOS (EV ponderado por EUR, IC90 por dia)')
def cut(nm, col, bins=None, labels=None, df=SU):
    P(f'-- {nm}')
    x = df[col] if bins is None else pd.cut(df[col], bins, labels=labels, right=False)
    for v, g in df.groupby(x, observed=True): P(line(f'  {v}', g))
cut('L (precio del bid)', 'L'); cut('moneda', 'act'); cut('lado', 'lado'); cut('tipo de relleno', 'ftype')
cut('T restante en relleno (s)', 'T', [0, 120, 200, 400]); cut('hora UTC', 'hora', [0, 6, 12, 18, 24])
cut('tiempo en cola (ms)', 'cola_ms', [-1e9, 1000, 5000, 30000, 1e9], ['<1s', '1-5s', '5-30s', '>30s'])
cut('bidL ex ante (bid-L a t_dec-300)', 'bidL', [-1, 0.02, 0.06, 0.08, 1])
cut('dir. 1h previa alineada (bps)', 'bn_pre1h', [-1e9, -10, 0, 10, 1e9]); cut('Binance en ventana alineado (bps)', 'bn_inwin', [-1e9, -5, 0, 5, 1e9])
cut('orden tomadora: acciones', 'shtx', [0, 20, 100, 1e9]); cut('makers rellenados por la tx', 'nmk', [0, 2, 3, 1e9])
cut('dia', 'dia')
SU['mk1'] = SU.mid_p1000 - SU.L; SU['mk5'] = SU.mid_p5000 - SU.L; SU['mk30'] = SU.mid_p30000 - SU.L
cut('markout mid(+1s)-L', 'mk1', [-1, -0.03, -0.01, 0.0, 0.01, 1]); cut('markout mid(+5s)-L', 'mk5', [-1, -0.03, -0.01, 0.0, 0.01, 1]); cut('markout mid(+30s)-L', 'mk30', [-1, -0.03, -0.01, 0.0, 0.01, 1])
P('-- calibracion tras el relleno (sueltos): acierto vs mid/bid')
for c in ('mid_m300', 'bid_p250', 'mid_p1000', 'mid_p5000', 'mid_p30000'):
    m = SU[c].notna(); P(f'  {c:11s} n={int(m.sum())} acierto={SU.gana[m].mean():.4f} media={SU[c][m].mean():.4f} acierto-precio={SU.gana[m].mean()-SU[c][m].mean():+.4f}')
P(f'  L medio={SU.L.mean():.4f}  acierto={SU.gana.mean():.4f}')

P(); P('== 2. SALIDA tras el relleno (sueltos). Delta = q*(b_neto - gana) sobre los rellenos que disparan; EV_total = (pnl + Delta)/coste')
def apply_exit(df, trig, bcol, scol):
    d = np.where(trig, df.q * (bnet(df[bcol], df[scol], df.q) - df.gana), 0.0); d = np.nan_to_num(d, nan=0.0)
    return d
def rep_exit(nm, df, trig, bcol, scol, placebo=True):
    df = df.copy(); trig = np.asarray(trig, bool) & df[bcol].notna().values
    df['d'] = apply_exit(df, trig, bcol, scol); df['pnl2'] = df.pnl + df.d
    lo, hi = boot_days(df, 'd', 'cost'); g = df.groupby('dia').d.sum()
    s = f'{nm:30s} cob={trig.mean():.3f} n_trig={int(trig.sum()):4d} dPnL={df.d.sum():+7.2f} d/EUR={df.d.sum()/df.cost.sum():+.4f} IC90d=({lo:+.4f},{hi:+.4f}) sin2={sin2(df, "d", "cost"):+.4f} dias+={int((g>0).sum())}/{len(g)} EVtot={df.pnl2.sum()/df.cost.sum():+.3f}'
    if placebo and trig.sum() > 0:   # placebo: misma cobertura por dia, rellenos al azar
        obs = df.d.sum(); null = []
        for _ in range(500):
            tp = np.zeros(len(df), bool)
            for dd, idx in df.groupby('dia').indices.items():
                kk = int(trig[idx].sum())
                if kk: tp[RNG.choice(idx, kk, replace=False)] = True
            tp &= df[bcol].notna().values; null.append(apply_exit(df, tp, bcol, scol).sum())
        null = np.array(null); s += f' | placebo media={null.mean():+.2f} p(>=obs)={(null >= obs).mean():.3f}'
    return s, df.d.sum()
for per in ('TRAIN', 'HOLD', 'TODO'):
    D_ = SU if per == 'TODO' else SU[SU.per == per]
    P(f'-- {per} (n={len(D_)}, EV base {ev(D_):+.3f})')
    P('  ' + rep_exit('E0 vender ya (tf+250)', D_, np.ones(len(D_), bool), 'bid_p250', 'bsz_p250', placebo=False)[0])
    for th in (0.0, 0.01, 0.02, 0.03, 0.05):
        P('  ' + rep_exit(f'E1 bid(+1s)<=L-{th:.2f}', D_, (D_.bid_p1000 <= D_.L - th + 1e-9).values, 'bid_p1250', 'bsz_p1250')[0])
    for th in (0.0, 0.02, 0.05):
        P('  ' + rep_exit(f'E1b bid(+5s)<=L-{th:.2f}', D_, (D_.bid_p5000 <= D_.L - th + 1e-9).values, 'bid_p5250', 'bsz_p5250')[0])
    for th in (0.01, 0.02, 0.05):
        P('  ' + rep_exit(f'INV bid(+1s)>L-{th:.2f}', D_, (D_.bid_p1000 > D_.L - th + 1e-9).values, 'bid_p1250', 'bsz_p1250', placebo=False)[0])
    for s_ in (2, 3, 5):
        for wn in ('30', 'E'):
            P('  ' + rep_exit(f'E2 stop L-0,{s_:02d} W={wn}', D_, D_[f'stop{s_}_{wn}_t'].notna().values, f'stop{s_}_{wn}_b', f'stop{s_}_{wn}_s')[0])
    for th in (1, 2, 3, 5):
        P('  ' + rep_exit(f'E4 Binance(+1s)<=-{th}bps', D_, (D_.bn_p1 <= -th).values, 'bid_p1250', 'bsz_p1250')[0])
    for x in (0.02, 0.05):
        P('  ' + rep_exit(f'E3 A30 bid(T-30)<={x:.2f}', D_, (D_.bid_T30 <= x + 1e-9).values, 'bid_T30', 'bsz_T30')[0])
    for th in (0.01, 0.03):
        P('  ' + rep_exit(f'E5 mid(+1s)<=midpre-{th:.2f}', D_, ((D_.bid_p1000 + D_.ask_p1000) / 2 <= D_.mid_m300 - th + 1e-9).values, 'bid_p1250', 'bsz_p1250')[0])
P(f'  (factibilidad) nocional de la venta q*b < 1 $ en {(SU.q * SU.bid_p250 < 1).mean():.3f} de los sueltos; bsz<q a +250 ms en {(SU.bsz_p250 < SU.q).mean():.3f}')

P(); P('== 3. EVITAR (rasgos ex ante a t_dec-300; quitar el segmento quita sus rellenos). dPnL = -sum pnl de los quitados; split suelto/rafaga')
def rep_av(nm, df, mask):
    mask = np.asarray(mask, bool); df = df.copy(); df['d'] = np.where(mask, -df.pnl, 0.0)
    lo, hi = boot_days(df, 'd', 'cost'); g = df.groupby('dia').d.sum(); kept = df[~mask]
    ds = df.d[df.suelto].sum(); dr = df.d[~df.suelto].sum()
    return f'{nm:30s} quita={mask.mean():.3f} dPnL={df.d.sum():+7.2f} (suelto {ds:+.1f} raf {dr:+.1f}) IC90d dPnL/EUR=({lo:+.4f},{hi:+.4f}) dias+={int((g>0).sum())}/{len(g)} EV_rest={ev(kept):+.3f} EVsuelto_rest={ev(kept[kept.suelto]):+.3f} sin2_rest={sin2(kept, "pnl", "cost") if len(kept) else np.nan:+.3f}'
for per in ('TRAIN', 'HOLD', 'TODO'):
    D_ = F if per == 'TODO' else F[F.per == per]
    P(f'-- {per} (n={len(D_)}; EV {ev(D_):+.3f}; suelto {ev(D_[D_.suelto]):+.3f})')
    for g_ in (0.02, 0.04, 0.06, 0.08): P('  ' + rep_av(f'A1 GEO bidL<{g_:.2f}', D_, (D_.bidL < g_ - 1e-6).values | D_.bidL.isna().values))
    P('  ' + rep_av('A2 lado NO', D_, (D_.lado == 'NO').values))
    P('  ' + rep_av('A3 dir1h alineada<=0', D_, (D_.bn_pre1h <= 0).values)); P('  ' + rep_av('A3i dir1h alineada>0', D_, (D_.bn_pre1h > 0).values))
    for t_ in (90, 120, 150): P('  ' + rep_av(f'A4 Tdec<{t_}', D_, (D_.Tdec < t_).values))
    for g_ in (-0.02, 0.0, 0.02): P('  ' + rep_av(f'A5 b15-L<{g_:+.2f}', D_, (D_.g15 < g_ - 1e-6).values))
    for s_ in (0.02, 0.04): P('  ' + rep_av(f'A6 spread_dec>={s_:.2f}', D_, (D_.spread_dec >= s_ - 1e-6).values))
    P('  ' + rep_av('A7 salto adverso 3s (ja3)', D_, D_.ja3.fillna(False).values.astype(bool)))
    P('  ' + rep_av('A7b |r3|>=3', D_, (D_.r3.abs() >= 3).values))
    for co in ('ETH', 'SOL', 'XRP'): P('  ' + rep_av(f'A8 no {co}', D_, (D_.act == co).values))
    for L_ in (0.10, 0.13, 0.16, 0.19): P('  ' + rep_av(f'A9 no L={L_:.2f}', D_, (D_.L.round(2) == L_).values))
open(H + 'out/ana.txt', 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
