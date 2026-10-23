#!/usr/bin/env python3
"""diseccion.py WALLET [WALLET...] -- conducta fina en alts 5m (fills_alts.csv.gz): T de los rellenos, precio por fase, tamano,
maker/tomador, inventario (max|I|, final), reequilibrado (P(siguiente relleno reduce |I|) vs base), retraso entre patas,
rango en cola (li entre makers del mismo token+precio en la misma tx) frente a azar."""
import os, sys, numpy as np, pandas as pd
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'datos')
F = pd.read_csv(os.path.join(D, 'fills_alts.csv.gz'))
F['T'] = F.fin - F.ts
out = []
def P(*a): out.append(' '.join(str(x) for x in a))
for w in sys.argv[1:]:
    x = F[F.wallet == w].sort_values(['mid', 'ts', 'li'])
    if not len(x): P(w, 'sin filas'); continue
    P(f'\n######## {w}  rellenos {len(x)}  mercados {x.mid.nunique()}  dias {x.dia.nunique()}')
    P('rol (por USD):', (x.groupby('rol').cost_ef.sum() / x.cost_ef.sum()).round(3).to_dict(), '| side (0 compra,1 venta) filas:', x.side.value_counts().to_dict())
    P('T restante del relleno (s) cuantiles 0/10/25/50/75/90/100:', np.round(x['T'].quantile([0, .1, .25, .5, .75, .9, 1]).values, 0).tolist())
    x['fase'] = pd.cut(x['T'], [-1, 60, 120, 180, 240, 301], labels=['0-60', '60-120', '120-180', '180-240', '240-300'])
    px_ef = np.where(x.side == 0, x.px, 1 - x.px)
    x['px_ef'] = px_ef
    P('precio efectivo pagado por fase (mediana) y % USD:', x.groupby('fase', observed=False).agg(px=('px_ef', 'median'), usd=('cost_ef', 'sum')).assign(usd=lambda z: (z.usd / z.usd.sum()).round(3)).round(3).to_dict('index'))
    P('acc por relleno cuantiles 10/50/90:', np.round(x.acc.quantile([.1, .5, .9]).values, 2).tolist(), '| px_ef bandas:', pd.cut(x.px_ef, [0, .1, .3, .5, .7, .9, 1]).value_counts(normalize=True).sort_index().round(3).to_dict())
    # inventario por mercado
    res = []; red = []; base = []; lag = []
    for mid, z in x.groupby('mid'):
        s = np.where(z.lado_ef == 'YES', 1.0, -1.0) * z.acc.values
        I = np.cumsum(s); tot = z.acc.sum()
        res.append((np.abs(I).max(), abs(I[-1]), tot, len(z)))
        for i in range(1, len(s)):
            if I[i - 1] != 0:
                red.append(int(np.sign(s[i]) != np.sign(I[i - 1])))
        # retraso primera pata -> primera del contrario
        ly = z[z.lado_ef == 'YES'].ts; ln = z[z.lado_ef == 'NO'].ts
        if len(ly) and len(ln): lag.append(abs(ly.iloc[0] - ln.iloc[0]))
    r = np.array(res)
    P(f'inventario: max|I| mediana {np.median(r[:,0]):.1f} acc (p90 {np.percentile(r[:,0],90):.1f}); final |I|/acc total mediana {np.median(r[:,1]/r[:,2]):.2f}; rellenos/mercado mediana {np.median(r[:,3]):.0f}')
    lado_share = (x.lado_ef == 'YES').mean()
    P(f'reequilibrado: P(siguiente relleno reduce |I|) = {np.mean(red):.3f} (n={len(red)}) frente a azar ~0,5 (YES {lado_share:.2f})')
    if lag: P(f'retraso entre la 1a pata de cada lado (s): mediana {np.median(lag):.1f} p25 {np.percentile(lag,25):.1f} p75 {np.percentile(lag,75):.1f} (n={len(lag)}, mismo bloque {np.mean(np.array(lag)==0):.2f})')
    # cola: tx con >=2 makers en el mismo token y precio
    m = x[x.rol == 'M'][['tx', 'li', 'px', 'mid', 'lado']]
    allm = F[(F.rol == 'M') & F.tx.isin(m.tx)][['tx', 'li', 'px', 'mid', 'lado', 'wallet']]
    rk = []
    for (tx, mid, lado, px), g in allm.groupby(['tx', 'mid', 'lado', 'px']):
        if len(g) < 2 or w not in set(g.wallet): continue
        g = g.sort_values('li'); pos = list(g.wallet).index(w)
        rk.append(pos / (len(g) - 1))
    if rk: P(f'rango en cola dentro del nivel (0=primero,1=ultimo): media {np.mean(rk):.2f} (azar 0,50), primero {np.mean(np.array(rk)==0):.2f}, n niveles {len(rk)}')
    # PnL por fase de entrada del par: coste par por mercado vs T del primer relleno
    P('por moneda: rellenos', x.act.value_counts().to_dict())
txt = '\n'.join(out); print(txt); open(os.path.join(D, 'diseccion.txt'), 'a').write(txt + '\n')
