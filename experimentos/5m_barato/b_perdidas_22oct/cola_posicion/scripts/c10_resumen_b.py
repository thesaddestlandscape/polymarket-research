#!/usr/bin/env python3
"""c10_resumen_b.py -- PREREG_COLA (sha a72007c5...). Une b_barridos (on-chain), b_l2 (libro) y b_clase (clase cola/cruce de cola_vs_cruce, solo lectura) por orden de B
y resume, por moneda / nivel / tamano / clase, la cola delante al postear, lo consumido/cancelado, el tiempo hasta el relleno y la presencia de otros en el nivel antes de la rafaga.
Salida datos/b_cola.csv, datos/resumen_b.txt"""
import os, hashlib, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); CV = os.path.join(AQ, '..', '..', 'cola_vs_cruce', 'datos')
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_COLA.md'), 'rb').read()).hexdigest().startswith('a72007c5deecc5e7')
pd.set_option('display.width', 220)
B = pd.read_csv(os.path.join(D, 'b_barridos.csv')); B = B[B.es_primera == 1]
L = pd.read_csv(os.path.join(D, 'b_l2.csv'))
C = pd.read_csv(os.path.join(CV, 'b_clase.csv'), dtype={'tx': str})
X = B.merge(L.drop(columns=['coin', 'pc', 'acc', 'ts_chain', 'sh_ahead_same', 'sh_after_same', 'n_same', 'rank_same', 'n_better', 'sh_better']), on='oid', how='left')
X = X.merge(C[['tx', 'cl_h1_0.005', 'pnl', 'coste', 'gana', 'T']].drop_duplicates('tx'), on='tx', how='left')
X['A0'] = X.A0_book.fillna(X.A0_ledger)
X['A0_fuente'] = np.where(X.A0_book.notna(), 'book', 'ledger')
X['avance_trade'] = X.F_prev; X['cancel_ahead'] = X.A0_book - X.F_prev - X.sh_ahead_same
X['exceso'] = (X.F_prev + X.sh_ahead_same - X.A0_book).clip(lower=0)
bsz = X['size']
X['otros_m1000'] = X.S_m1000 - bsz; X['otros_m300'] = X.S_m300 - bsz; X['otros_m100'] = X.S_m100 - bsz
X['dia'] = pd.to_datetime(X.ts_chain, unit='s').dt.strftime('%Y-%m-%d'); X['espera_s'] = X.vida_ms / 1000
X.to_csv(os.path.join(D, 'b_cola.csv'), index=False)
out = []
def P(*a): out.append(' '.join(str(x) for x in a))
q = lambda s: np.nanpercentile(s, [10, 25, 50, 75, 90]).round(1).tolist()
P(f'B: {len(X)} ordenes con relleno; L2 disponible {int((X.l2=="ok").sum())}; llegada localizada en L2 {int(X.A0_book.notna().sum())}; rafaga localizada (print) {int(X.t_print.notna().sum())}')
P(f'  (sin mapa de tokens/L2 22-Oct >14:40Z: {int((X.l2=="sin_mapa_tokens").sum())}; sin print: {int(((X.l2=="ok")&X.t_print.isna()).sum())}; sin llegada: {int(((X.l2=="ok")&X.A0_book.isna()).sum())})')
P('\n1) COLA DELANTE AL POSTEAR (acciones del mismo nivel, libro unificado): A0 =', 'L2 justo antes de verse la orden (cuando se localiza), si no ledger')
P(f'   A0 cuantiles 10/25/50/75/90: {q(X.A0)}   P(A0=0)={ (X.A0<=0.5).mean():.1%}  P(A0<=10)={(X.A0<=10).mean():.1%}  (n={X.A0.notna().sum()})')
P(f'   ledger vs L2: cola del ledger (muestreada ~100 ms antes) cuantiles {q(X.A0_ledger)}; |A0_ledger-A0_book|<=1 acc: {( (X.A0_ledger-X.A0_book).abs()<=1).mean():.1%} (n={X.A0_book.notna().sum()})')
P(f'   latencia envio->visible en L2 (t_arr - t_call0): cuantiles {q(X.arr_lat_ms)} ms')
P('\n2) AL RELLENARSE')
P(f'   acciones por delante en la MISMA rafaga (mismo nivel): P(0)={(X.sh_ahead_same<=1e-9).mean():.1%}; cuantiles {q(X.sh_ahead_same)}; solo makers en el nivel (SOLO) {(X.n_same==1).mean():.1%}')
P(f'   acciones por delante en la rafaga con mejor precio: P(>0)={(X.sh_better>0).mean():.1%}; rafaga continua mas abajo (sh_worse>0) {(X.sh_worse>0).mean():.1%}')
P(f'   prints consumidos en el nivel durante la vida (F_prev) cuantiles {q(X.F_prev)}; P(F_prev>0)={(X.F_prev>0).mean():.1%} (n={X.F_prev.notna().sum()})')
Z = X[X.A0_book.notna() & X.t_print.notna()]
P(f'   A0 -> fill: de A0={Z.A0.sum():.0f} acc delante en total (n={len(Z)}): salieron por prints previos {Z.F_prev.sum():.0f} ({Z.F_prev.sum()/Z.A0.sum():.1%}), por la propia rafaga {Z.sh_ahead_same.sum():.0f} ({Z.sh_ahead_same.sum()/Z.A0.sum():.1%}), por CANCELACION/no explicado {Z.cancel_ahead.sum():.0f} ({Z.cancel_ahead.sum()/Z.A0.sum():.1%})')
P(f'   «llegaron despues y se rellenaron antes» (cota inferior: F_prev + sh_ahead - A0 > 0.5): {(Z.exceso>0.5).sum()} de {len(Z)} ordenes; acciones {Z.exceso.sum():.1f}')
P(f'   espera llegada->rafaga (s) cuantiles: {q(X.espera_s)}; T restante al rellenarse: {q(X["T_y"] if "T_y" in X else X["T"])}')
P(f'   OTROS en el nivel (talla - nuestra orden) a -1 s / -300 ms / -100 ms antes del print: medianas {np.nanmedian(X.otros_m1000):.1f} / {np.nanmedian(X.otros_m300):.1f} / {np.nanmedian(X.otros_m100):.1f}; P(sin otros<=0.5) {(X.otros_m1000<=0.5).mean():.1%} / {(X.otros_m300<=0.5).mean():.1%} / {(X.otros_m100<=0.5).mean():.1%} (n={X.otros_m100.notna().sum()})')
P('\n3) POR MONEDA')
g = X.groupby('coin').agg(n=('oid', 'size'), A0_med=('A0', 'median'), A0_0=('A0', lambda s: (s <= 0.5).mean()), n_same1=('n_same', lambda s: (s == 1).mean()), ahead0=('sh_ahead_same', lambda s: (s <= 1e-9).mean()), esp_med=('espera_s', 'median'), pc_med=('pc', 'median'))
P(g.round(2).to_string())
P('\n4) POR NIVEL DE PRECIO (pc)')
X['nivel'] = pd.cut(X.pc, [0.0, 0.15, 0.20, 0.25, 0.31])
g = X.groupby('nivel', observed=True).agg(n=('oid', 'size'), A0_med=('A0', 'median'), A0_0=('A0', lambda s: (s <= 0.5).mean()), solo=('n_same', lambda s: (s == 1).mean()), esp_med=('espera_s', 'median'))
P(g.round(2).to_string())
P('\n5) POR TAMANO DE LA ORDEN')
X['tam'] = pd.cut(X['size'], [0, 4.99, 5.01, 7.5, 11])
g = X.groupby('tam', observed=True).agg(n=('oid', 'size'), A0_med=('A0', 'median'), solo=('n_same', lambda s: (s == 1).mean()), ahead_med=('sh_ahead_same', 'median'), esp_med=('espera_s', 'median'))
P(g.round(2).to_string())
P('\n6) POR CLASE DE RELLENO (cola_vs_cruce: C1 barrido misma tx / C2 se sigue casando por debajo / C3 cola), solo posiciones con desenlace')
g = X.groupby('cl_h1_0.005', observed=True).agg(n=('oid', 'size'), A0_med=('A0', 'median'), A0_0=('A0', lambda s: (s <= 0.5).mean()), solo=('n_same', lambda s: (s == 1).mean()), ahead0=('sh_ahead_same', lambda s: (s <= 1e-9).mean()), esp_med=('espera_s', 'median'), otros100=('otros_m100', 'median'))
P(g.round(2).to_string())
P('\n7) POR DIA'); P(X.groupby('dia').agg(n=('oid', 'size'), A0_med=('A0', 'median'), solo=('n_same', lambda s: (s == 1).mean())).round(2).to_string())
open(os.path.join(D, 'resumen_b.txt'), 'w').write('\n'.join(out) + '\n'); print('\n'.join(out))
