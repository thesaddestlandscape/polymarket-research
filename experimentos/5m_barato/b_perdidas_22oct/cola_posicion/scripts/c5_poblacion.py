#!/usr/bin/env python3
"""c5_poblacion.py DIA... -- PREREG_COLA (sha a72007c5...). Posicion de cada relleno maker (ETH/SOL/XRP 5m, oc_D de cola_vs_cruce) dentro de su rafaga (tx) entre makers del
MISMO nivel (precio equivalente largo-c, libro unificado) ordenados por (bloque, li), y unidades primeras-5-acc por (maker, mercado, c) con banda pc (0,10;0,30], T (60;300] como P1.
Salida: datos/pop_rows_D.csv.gz (filas de banda con posicion) y datos/pop_units_D.csv.gz (unidades con posicion de su 1a fila + pnl/coste/gana)."""
import sys, os, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); SRC = os.path.join(AQ, '..', '..', 'cola_vs_cruce', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_COLA.md'), 'rb').read()).hexdigest().startswith('a72007c5deecc5e7')
EX = '0xe111180000d2663c0091e4f400237545b87b996b'; US = '0x659a40ff9920febc5a66836213040924343d297f'
def dia(d):
    T = pd.read_csv(os.path.join(SRC, f'tok_{d}.csv'), dtype={'mid': str, 'token': str}); comp = {}
    for mid, g in T.groupby('mid'):
        if len(g) == 2: a, b = g.tok_i.values; comp[a] = b; comp[b] = a
    F = pd.read_csv(os.path.join(SRC, f'oc_{d}.csv.gz'), dtype={'tx': str, 'maker': str, 'taker': str})
    F = F[(F.taker != EX) & F.tok_i.isin(comp.keys())].copy()
    buy = F.side.values == 0
    F['sh'] = np.where(buy, F.ta, F.ma); usd = np.where(buy, F.ma, F.ta); F = F[F.sh > 0].copy(); buy = F.side.values == 0; usd = np.where(buy, F.ma, F.ta)
    pr = usd / F.sh.values
    F['c'] = np.where(buy, F.tok_i.values, F.tok_i.map(comp).values).astype(int); F['pc'] = np.where(buy, pr, 1 - pr); F['pcm'] = np.rint(F.pc * 1000).astype(int)
    ti = T.set_index('tok_i')
    for k in ('act', 'mid', 'fin', 'lado', 'des'): F[k] = F.c.map(ti[k])
    F['T'] = F.fin - F.ts
    F = F.sort_values(['tx', 'c', 'pcm', 'bloque', 'li'], ascending=[True, True, False, True, True]).reset_index(drop=True)
    # posicion dentro de la rafaga (grupo tx,c): niveles por precio desc, dentro del nivel por li
    g_lv = F.groupby(['tx', 'c', 'pcm'], sort=False)
    F['n_same'] = g_lv.sh.transform('size'); F['rank_same'] = g_lv.cumcount()
    F['sh_in_lv_before'] = g_lv.sh.cumsum() - F.sh
    lv = F.groupby(['tx', 'c', 'pcm'], sort=False).agg(lv_sh=('sh', 'sum')).reset_index()
    lv['sh_better'] = lv.groupby(['tx', 'c'], sort=False).lv_sh.cumsum() - lv.lv_sh
    F = F.merge(lv[['tx', 'c', 'pcm', 'sh_better', 'lv_sh']], on=['tx', 'c', 'pcm'], how='left')
    F['sh_total_tx'] = F.groupby(['tx', 'c']).sh.transform('sum')
    F['sh_beyond'] = F.sh_total_tx - F.sh_better - F.lv_sh
    F['sh_ahead_same'] = F.sh_in_lv_before
    F['q'] = np.where(F.n_same >= 2, F.rank_same / (F.n_same - 1).clip(lower=1), np.nan)
    F['pos1'] = np.where(F.n_same == 1, 'SOLO', np.where(F.rank_same == 0, 'FRENTE', np.where(F.rank_same == F.n_same - 1, 'ATRAS', 'CENTRO')))
    F['dia'] = d
    banda = F[(F.pc > 0.10 + 1e-9) & (F.pc <= 0.30 + 1e-9) & (F['T'] > 60) & (F['T'] <= 300)]
    banda[['maker', 'c', 'act', 'mid', 'fin', 'bloque', 'li', 'tx', 'pc', 'sh', 'n_same', 'rank_same', 'q', 'pos1', 'sh_ahead_same', 'sh_better', 'sh_beyond', 'T', 'dia']].to_csv(os.path.join(D, f'pop_rows_{d}.csv.gz'), index=False)
    # unidades como P1: primeras 5 acc por (maker, c) en orden (bloque, li)
    G = F.sort_values(['maker', 'c', 'bloque', 'li']).reset_index(drop=True)
    G['cum'] = G.groupby(['maker', 'c']).sh.cumsum(); prev = G.cum - G.sh
    G['use'] = np.clip(5 - prev, 0, None).clip(upper=G.sh); G = G[G.use > 0].copy()
    G['coste'] = G.use * G.pc; G['gana'] = (G.des == G.lado).astype(float); G.loc[G.des.isna(), 'gana'] = np.nan
    G['pnl'] = G.use * G.gana - G.coste
    g = G.groupby(['maker', 'c'], sort=False)
    U = g.first()[['act', 'mid', 'fin', 'lado', 'des', 'pc', 'T', 'bloque', 'ts', 'tx', 'n_same', 'rank_same', 'q', 'pos1', 'sh_ahead_same', 'sh_better', 'sh_beyond']].copy()
    U['coste'] = g.coste.sum(); U['pnl'] = g.pnl.sum(min_count=1); U['acc'] = g.use.sum(); U['gana'] = g.gana.first()
    U = U.reset_index(); U['es_b'] = (U.maker == US).astype(int)
    U = U[(U.pc > 0.10 + 1e-9) & (U.pc <= 0.30 + 1e-9) & (U['T'] > 60) & (U['T'] <= 300)]; U['dia'] = d
    U.to_csv(os.path.join(D, f'pop_units_{d}.csv.gz'), index=False)
    print(d, 'filas', len(F), 'banda', len(banda), 'unidades', len(U), 'B', int(U.es_b.sum()), 'sin desenlace', int(U.gana.isna().sum()), U.pos1.value_counts().to_dict(), flush=True)
for d in sys.argv[1:]: dia(d)
