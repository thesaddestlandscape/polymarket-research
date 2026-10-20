import glob, json, random, collections
import numpy as np, pandas as pd
O = '/mnt/HC_Volume_106538179/datalogs_analisis_caches/v4_captura_maker/'
fs = sorted(glob.glob(O + 'm1_2026-*.csv'))
M = pd.concat([pd.read_csv(f) for f in fs]); M = M[M.gana.notna()]
print('dias', sorted(M.dia.unique()), 'filas', len(M), '| missing desenlace excluidos:', 0)
dl = [json.load(open(f)) for f in sorted(glob.glob(O + 'm1_delta_*.json'))]
print('DELTA rx(trade) - rx(bid5 cae por debajo de p) [ms] por dia (n, p10, p50, p90, %libro_antes, %>60ms, %>150ms):')
for d in dl: print('  ', d['dia'], d['n'], d['p10'], d['p50'], d['p90'], d['frac_libro_antes'], d['frac_gt60'], d['frac_gt150'])
def st(g):
    if not len(g): return 'n=0'
    pdd = g.groupby('dia').agg(p=('pnl', 'sum'), c=('coste', 'sum'))
    ds = list(pdd.index); random.seed(1); bs = []
    for _ in range(2000):
        s = [random.choice(ds) for _ in ds]; bs.append(pdd.loc[s, 'p'].sum() / pdd.loc[s, 'c'].sum())
    top = pdd.p.sort_values(ascending=False).index[:2]; r2 = pdd.drop(top)
    s2 = r2.p.sum() / r2.c.sum() if len(r2) else float('nan')
    return (f'n={len(g):3d} dias={len(ds):2d}(+{(pdd.p>0).sum()}) PnL={g.pnl.sum():+7.2f} coste={g.coste.sum():6.2f} EVpond={g.pnl.sum()/g.coste.sum():+.3f} '
            f'IC90d=({np.percentile(bs,5):+.2f},{np.percentile(bs,95):+.2f}) sin2={s2:+.3f} acierto={g.gana.mean():.2f} vs precio={(g.coste.sum()/g.lleno.sum()):.2f}')
print('\n=== H23 con reloj de relleno ADELANTADO S ms (S=0 reproduce h23 alta79/cancel60) ===')
for brazo in ('A', 'B'):
    for var in ('join', 'join_r', 'nc'):
        for cola in ('base', 'cons', 'opt'):
            for S in sorted(M.S.unique()):
                g = M[(M.brazo == brazo) & (M['var'] == var) & (M.cola == cola) & (M.S == S)]
                if var == 'nc' and cola != 'base': continue
                print(f'{brazo} {var:6s} {cola:4s} S={S:3d} | {st(g)}')
print('\n=== V3 en el MAKER: retorno Binance orientado a s en los 5 s / 1 s previos al relleno (rx). Primario join base ===')
for brazo in ('A', 'B'):
    for S in (0, 100):
        g = M[(M.brazo == brazo) & (M['var'] == 'join') & (M.cola == 'base') & (M.S == S)]
        for nom, m in (('bret5>=-1', g.bret5 >= -1), ('bret5<-1', g.bret5 < -1), ('bret1>=0', g.bret1 >= 0), ('bret1<0', g.bret1 < 0)):
            print(f'{brazo} S={S:3d} {nom:10s} | {st(g[m])}')
print('\n=== Bucket de precio 0,05 (A y B join base S=0) ===')
for brazo in ('A', 'B'):
    g = M[(M.brazo == brazo) & (M['var'] == 'join') & (M.cola == 'base') & (M.S == 0)].copy()
    g['bk'] = (np.floor(g.pm / 0.05) * 0.05).round(2)
    for bk, gg in g.groupby('bk'): print(f'{brazo} [{bk:.2f},{bk+0.05:.2f}) | {st(gg)}')
