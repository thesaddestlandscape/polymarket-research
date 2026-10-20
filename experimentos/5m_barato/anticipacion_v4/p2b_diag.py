"""Diagnostico (post hoc, NO regla): EV de la entrada simulada A/C/D dentro y fuera de los cierres que operan los rivales; y
rasgos causales de la entrada (T, ask5, tamano nivel 1, gap) para ver QUE cierres eligen. Exploratorio, sin correccion."""
import glob, numpy as np, pandas as pd
O = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_comprar_lo_bueno/r3_out/'
F = pd.concat([pd.read_csv(f) for f in sorted(glob.glob(O + 'feat_*.csv.gz'))], ignore_index=True).drop_duplicates(['cierre', 't']).sort_values(['cierre', 't'])
F['gana'] = F.gana.astype(bool); F['dm'] = F.db15_1s - F.da5_1s
A = pd.read_csv(O + 'p1_fills.csv.gz'); A = A[(A.placebo == 0)]
riv = A.groupby('cierre').agg(first_ex=('ex', 'min'), ws=('w', lambda s: ','.join(sorted(set(x[:2] for x in s)))), usd=('usd', 'sum'), nf=('p', 'size'))
fee = lambda p: 0.07 * p * (1 - p)
def primera(mask):
    d = F[mask].groupby('cierre').head(1).copy()
    d['ejec'] = d.acc_e215 > 0; d['p'] = d.ask_e215
    d['coste'] = np.where(d.ejec, d.acc_e215 * (d.p + fee(d.p)), 0.0); d['pnl'] = np.where(d.ejec, d.acc_e215 * (d.gana.astype(float) - d.p - fee(d.p)), 0.0)
    d = d.join(riv, on='cierre'); d['riv'] = d.first_ex.notna(); d['T'] = d.cierre - d.t / 1000
    return d
def ev(x): return (x.pnl.sum() / x.coste.sum()) if x.coste.sum() > 0 else np.nan
for nom, mk in (('A', (F.m >= -0.05) & (F.dm >= 0.01)), ('C', (F.m >= -0.05) & (F.dm >= 0.01) & ((F.m - F.dm) < -0.05)), ('D', (F.m >= 0) & (F.dm >= 0.01)), ('V4', F.sen.astype(bool))):
    d = primera(mk); e = d[d.ejec]
    print(f'\n{nom}: disparos {len(d)} ejec {len(e)} | cierres con rival {int(d.riv.sum())} ({100*d.riv.mean():.0f} %)')
    for lab, x in (('rival opero el cierre', e[e.riv]), ('rival NO opero', e[~e.riv])):
        print(f'   {lab:24s} n={len(x):3d} coste={x.coste.sum():6.1f} EV={ev(x):+.3f} acierto={x.gana.mean() if len(x) else np.nan:.2f} dias={x.dia.nunique()}')
    x = d[d.riv & d.ejec]
    if len(x): print('   nuestro t - 1a compra rival (ms, ex rival-150 como envio): P10/50/90', np.percentile(x.t - (x.first_ex - 150), [10, 50, 90]).round(0), '| nuestro ask5 P50', x.ask5.median(), '| T P50', round(x['T'].median()))
    # por banda de ask (exploratorio)
    e = e.assign(banda=pd.cut(e.ask5, [0, .15, .3, .5, .7, 1])); t_ = e.groupby('banda', observed=True).apply(lambda g: pd.Series(dict(n=len(g), EV=round(ev(g), 3), acierto=round(g.gana.mean(), 2))))
    print('   por ask5:', t_.to_dict('index'))
    e = e.assign(tb=pd.cut(e['T'], [0, 60, 120, 200, 300])); t_ = e.groupby('tb', observed=True).apply(lambda g: pd.Series(dict(n=len(g), EV=round(ev(g), 3))))
    print('   por T:', t_.to_dict('index'))
