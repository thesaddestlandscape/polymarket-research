#!/usr/bin/env python3
"""s6_analisis.py -- analisis preregistrado (PREREGISTRO_COSECHAR_ABRIR.md): seleccion en DESC 05-14, juicio unico en OOS 15-21, por moneda, regimen BASE.
Uso: s6_analisis.py [--solo-desc]   (--solo-desc imprime solo DESC y la politica elegida; el OOS no se calcula hasta ejecutar sin flag)
Lee DL/m5_cosechar_abrir/sim_<MONEDA>_<DIA>.csv.gz. Salida: ../datos/s6_informe.txt y s6_resultados.json."""
import sys, os, glob, json, numpy as np, pandas as pd
OUT = '/root/polymarket-research-datalogs/m5_cosechar_abrir'
HERE = os.path.dirname(os.path.abspath(__file__)); DAT = os.path.join(HERE, '..', 'datos')
COINS = ('BTC', 'ETH', 'SOL', 'XRP')
DESC = [f'2026-10-{d:02d}' for d in range(5, 15)]; OOS = [f'2026-10-{d:02d}' for d in range(15, 22)]
POL6 = [f'P{p}_{d}' for p in (96, 98) for d in ('A0', 'A_BN', 'B_15')]
rng = np.random.default_rng(20261022)
LOG = []
def L(s=''):
    print(s, flush=True); LOG.append(s)
def cargar():
    fs = sorted(glob.glob(f'{OUT}/sim_*_2026-10-*.csv.gz'))
    df = pd.concat([pd.read_csv(f) for f in fs], ignore_index=True)
    df['tot_pnl'] = df.pnl + df.reemb
    df['pares'] = np.minimum(df.qY, df.qN)
    df['pnl_pares'] = df.pares * (1 - df.bY - df.bN)
    df['ambos'] = (df.qY > 0) & (df.qN > 0)
    df['con_fill'] = (df.qY + df.qN) > 0
    return df
def ev(d, reemb=True):
    c = d.cost.sum()
    return (d.pnl.sum() + (d.reemb.sum() if reemb else 0)) / c if c > 0 else np.nan
def boot_days(d, n=3000, reemb=True):
    days = sorted(d.dia.unique()); S = {x: g for x, g in d.groupby('dia')}
    num = np.array([S[x].pnl.sum() + (S[x].reemb.sum() if reemb else 0) for x in days]); den = np.array([S[x].cost.sum() for x in days])
    r = []
    for _ in range(n):
        i = rng.integers(0, len(days), len(days)); dd = den[i].sum()
        if dd > 0: r.append(num[i].sum() / dd)
    return (np.percentile(r, 5), np.percentile(r, 95)) if r else (np.nan, np.nan)
def boot_cierres(d, n=2000, reemb=True):
    g = d.groupby('fin').agg(num=('pnl', 'sum'), rb=('reemb', 'sum'), den=('cost', 'sum'))
    num = (g.num + (g.rb if reemb else 0)).values; den = g.den.values; r = []
    for _ in range(n):
        i = rng.integers(0, len(g), len(g)); dd = den[i].sum()
        if dd > 0: r.append(num[i].sum() / dd)
    return (np.percentile(r, 5), np.percentile(r, 95)) if r else (np.nan, np.nan)
def sin2(d):
    s = d.groupby('dia').tot_pnl.sum().sort_values(ascending=False); k = d[~d.dia.isin(s.index[:2])]
    return ev(k)
def dias_pos(d):
    g = d.groupby('dia').apply(lambda x: (x.tot_pnl.sum()) / max(x.cost.sum(), 1e-9) if x.cost.sum() > 0 else np.nan)
    return int((g > 0).sum()), int(g.notna().sum())
def perm_p(d, n=1000):
    """H0: relleno sin informacion sobre el desenlace. Permuta 'des' dentro de (dia, moneda). p unilateral EV>=obs (incl. reembolso)."""
    obs = ev(d); win_y = (d.des == 'YES').values; qY = d.qY.values; qN = d.qN.values; cost = d.cost.sum(); rb = d.reemb.sum()
    grp = d.groupby(['dia', 'coin']).indices; cnt = 1
    for _ in range(n):
        wy = win_y.copy()
        for ix in grp.values(): wy[ix] = rng.permutation(win_y[ix])
        win = np.where(wy, qY, qN).sum()
        if (win - cost + rb) / cost >= obs: cnt += 1
    return cnt / (n + 1)
def fila(d, nombre):
    lo, hi = boot_days(d); a, b = dias_pos(d)
    return (f'{nombre:28s} merc {len(d):5d} con_fill {int(d.con_fill.sum()):5d} | EV/€ {ev(d):+.4f} (sin reemb {ev(d, False):+.4f}) IC90 días ({lo:+.4f},{hi:+.4f}) {a}/{b} días+ | '
            f'$ {d.tot_pnl.sum():+.1f} coste {d.cost.sum():.0f} | pares completos {100 * d.ambos.sum() / max(1, d.con_fill.sum()):.0f}% de mercados con relleno')
def seleccionar(D, coin):
    best = None; tabla = []
    for p in POL6:
        d = D[(D.coin == coin) & (D.pol == p + '_BASE')]
        if d.con_fill.sum() < 100: continue
        lo, hi = boot_days(d); tabla.append((p, ev(d), lo, hi, int(d.con_fill.sum())))
        if best is None or lo > best[1]: best = (p, lo)
    return (best[0] if best else None), tabla
def main():
    solo_desc = '--solo-desc' in sys.argv
    df = cargar()
    L(f'COSECHAR AL ABRIR v3 — días en sim: {sorted(df.dia.unique())}')
    cov = [json.load(open(f)) for f in sorted(glob.glob(f'{OUT}/cobertura_*_2026-10-*.json'))]
    cv = pd.DataFrame(cov); L('\nCOBERTURA (esperados / procesados / sin_par / sin_datos / sin_desenlace) por moneda:')
    L(cv.groupby('coin')[['esperados', 'procesados', 'sin_par', 'sin_datos', 'sin_desenlace']].sum().to_string())
    L('días por moneda: ' + str({c: sorted(cv[cv.coin == c].dia.unique())[:1] + ['..'] + sorted(cv[cv.coin == c].dia.unique())[-1:] for c in COINS}) + f' (n días {cv.groupby("coin").dia.nunique().to_dict()})')
    res = {}; elegida = {}
    L('\n=========== DESCUBRIMIENTO 05-14 (BASE) ===========')
    DD = df[df.dia.isin(DESC)]
    for c in COINS:
        p, tabla = seleccionar(DD, c); elegida[c] = p
        L(f'\n-- {c}: elegida en DESC = {p}')
        for t in tabla: L(f'   {t[0]:10s} EV/€ {t[1]:+.4f} IC90 días ({t[2]:+.4f},{t[3]:+.4f}) con_fill {t[4]}')
        for reg in ('OPT', 'BASE', 'CONS'):
            for pol in ([p + '_' + reg] if p else []) + ['JOIN_A0_' + reg]:
                d = DD[(DD.coin == c) & (DD.pol == pol)]
                if len(d): L('   ' + fila(d, pol))
        for pol in ('CTL60_P96_A0_BASE', 'CTL120_P96_A0_BASE'):
            d = DD[(DD.coin == c) & (DD.pol == pol)]
            if len(d): L('   ' + fila(d, pol))
    if solo_desc:
        json.dump(elegida, open(os.path.join(DAT, 's6_elegidas_desc.json'), 'w')); open(os.path.join(DAT, 's6_informe_desc.txt'), 'w').write('\n'.join(LOG)); return
    L('\n=========== OOS 15-21 (juicio único, política elegida en DESC) ===========')
    DO = df[df.dia.isin(OOS)]; pasan = {}
    for c in COINS:
        p = elegida[c]
        if p is None: L(f'\n-- {c}: sin política elegible'); pasan[c] = False; continue
        L(f'\n-- {c}: política {p}')
        for reg in ('OPT', 'BASE', 'CONS'):
            d = DO[(DO.coin == c) & (DO.pol == p + '_' + reg)]; L('   ' + fila(d, p + '_' + reg))
        d = DO[(DO.coin == c) & (DO.pol == p + '_BASE')]
        lo_c, hi_c = boot_cierres(d); s2 = sin2(d); pp = perm_p(d); a, b = dias_pos(d)
        L(f'   BASE: IC90 cierres ({lo_c:+.4f},{hi_c:+.4f}) | sin 2 mejores días {s2:+.4f} | p_perm {pp:.4f} | días+ {a}/{b}')
        # placebo temporal (mismos días/mercados)
        dif = []
        ctl = DO[(DO.coin == c) & (DO.pol == 'CTL120_P96_A0_BASE')]
        if len(ctl):
            days = sorted(d.dia.unique()); r = []
            for _ in range(2000):
                i = rng.integers(0, len(days), len(days)); xs = [days[k] for k in i]
                a1 = pd.concat([d[d.dia == x] for x in xs]); a2 = pd.concat([ctl[ctl.dia == x] for x in xs]); r.append(ev(a1) - ev(a2))
            L(f'   EV(pol) - EV(CTL120) = {ev(d) - ev(ctl):+.4f} IC90 días ({np.nanpercentile(r, 5):+.4f},{np.nanpercentile(r, 95):+.4f})  [CTL120 EV {ev(ctl):+.4f}; CTL60 {ev(DO[(DO.coin == c) & (DO.pol == "CTL60_P96_A0_BASE")]):+.4f}]')
            dif_lo = np.nanpercentile(r, 5)
        else: dif_lo = np.nan
        # seleccion adversa
        L('   SELECCIÓN ADVERSA / PATA SUELTA (BASE):')
        cf = d[d.con_fill]; su = cf[~cf.ambos]; am = cf[cf.ambos]
        pnl_p = cf.pnl_pares.sum(); resid = cf.pnl.sum() - pnl_p
        L(f'     mercados con relleno {len(cf)}: ambos lados {len(am)} ({100 * len(am) / max(1, len(cf)):.0f}%), sueltos {len(su)}; PnL pares {pnl_p:+.1f} $, PnL residuo (sueltas+excedente) {resid:+.1f} $ -> residuo/pares = {-resid / pnl_p * 100 if pnl_p > 0 else float("nan"):.0f}% del margen de pares se pierde; reembolso {cf.reemb.sum():+.1f} $')
        for lado, q, b_ in (('YES', 'qY', 'bY'), ('NO', 'qN', 'bN')):
            op = d[d['op' + lado[0]]] if False else d
            fil = d[d[q] > 0]; nof = d[(d[q] == 0) & (d['op' + lado[0]])]
            if len(fil): L(f'     pata {lado}: rellena n={len(fil)} acierto {100 * (fil.des == lado).mean():.1f}% (b medio {fil[b_].mean():.3f}) | no rellena (cotizada) n={len(nof)} acierto {100 * (nof.des == lado).mean():.1f}%')
        ok = (ev(d) > 0 and lo_c > 0 and boot_days(d)[0] > 0 and a >= 5 and s2 > 0 and pp < 0.0125 and d.con_fill.sum() >= 200 and dif_lo > 0)
        pasan[c] = bool(ok); L(f'   GATES (sin fidelidad): {"PASA" if ok else "NO PASA"}')
        res[c] = dict(politica=p, ev_base=ev(d), ic_dias=boot_days(d), ic_cierres=(lo_c, hi_c), sin2=s2, p_perm=pp, dias_pos=(a, b), pasa=bool(ok))
    L('\n=========== AGREGADO ALTS (ETH+SOL+XRP) OOS, cada moneda con su política, BASE ===========')
    A = pd.concat([DO[(DO.coin == c) & (DO.pol == elegida[c] + '_BASE')] for c in ('ETH', 'SOL', 'XRP') if elegida[c]])
    if len(A):
        L('   ' + fila(A, 'ALTS'));  lo, hi = boot_cierres(A); L(f'   IC90 cierres ({lo:+.4f},{hi:+.4f}) sin 2 mejores días {sin2(A):+.4f}')
    json.dump(dict(elegidas=elegida, pasan=pasan, res=res), open(os.path.join(DAT, 's6_resultados.json'), 'w'), default=str)
    open(os.path.join(DAT, 's6_informe.txt'), 'w').write('\n'.join(LOG))
if __name__ == '__main__': main()
