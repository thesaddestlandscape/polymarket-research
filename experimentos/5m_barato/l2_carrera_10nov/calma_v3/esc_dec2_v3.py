#!/usr/bin/env python3
"""esc_dec2_v3.py DIA -- F (12-Nov): Calma-T1 (esc_dec2.py del forward, dev SIN EDITAR) RECALCULADO con el sello de cinta passT_v3 (stamp_v3: firma exacta de la fila de consumo + hash de tx a libro5_tx) en lugar de la regla vieja
(1a transicion bid>pmin->=<pmin en 400 ms previos / t-63, el artefacto del 187 ms). TODO lo demas es identico: mismo motor engine.DayEng (legacy, reloj EX), mismas variantes, mismo codigo de variantes (se EJECUTA el fuente de esc_dec2.py con SOLO tres
sustituciones de texto: directorio de salida, etiqueta, y el bloque de re-sincronizacion de la cinta). Variable EXTRA_SHIFT_MS igual que el original (100 -> etiqueta dec3v3s100).
sello_print del resultado: v3 (stamp_v3) | motor: engine.DayEng legacy SIN dedupe (el dedupe de engine_v3 es otro cambio; con el sello v3 el print va ANTES de su fila y el doble conteo es neutro).
Solo lectura de datos; 0 ordenes; escribe CALMA_V3_OUT/<tag>_<D>.pkl. Lanzar con guard_rss.py (RSS) y fuera de 06-09Z."""
import sys, os
L2 = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/'; DEV = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/esc_dec2.py'
src = open(DEV).read(); d = sys.argv[1]; OUTD = os.environ.get('CALMA_V3_OUT', os.path.dirname(os.path.abspath(__file__)) + '/out/'); os.makedirs(OUTD, exist_ok=True)
A = "H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'"; assert src.count(A) == 1
src = src.replace(A, "H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = os.environ['CALMA_V3_OUT'].rstrip('/') + '/'")
B = "TAGF = 'dec2' if XS == 0 else f'dec3s{XS}'"; assert src.count(B) == 1
src = src.replace(B, "TAGF = 'dec2v3' if XS == 0 else f'dec3v3s{XS}'")
i0 = src.index('# --- cinta re-sincronizada (identica a pol_day.py / esc_ret.py)'); i1 = src.index('NMK = {}'); assert 0 < i0 < i1
NEW = '''# --- cinta con SELLO v3 (stamp_v3), igual que el preambulo de passT_cxb_v3.py (STAMP=v3)
sys.path.insert(0, %r); import stamp_v3 as ST, glob, gc
TXD = '/mnt/HC_Volume_106538179/libro5_tx/'; fr = []
for dd_ in [(pd.Timestamp(d) + pd.Timedelta(days=i)).strftime('%%Y-%%m-%%d') for i in (-1, 0, 1)]:
    for f_ in sorted(glob.glob(TXD + f'libro5_tx_{dd_}_*.csv.gz')): fr.append(pd.read_csv(f_, header=None, names=['t_ev', 'token', 'tx', 'recv'], dtype={'token': str, 'tx': str}))
TEV = pd.concat(fr, ignore_index=True).groupby('tx').t_ev.min() if fr else pd.Series(dtype='int64'); del fr
tp = tape.assign(k=tape.token_id.map(D.tokidx)); tp = tp[tp.k.notna()].copy(); tp['k'] = tp.k.astype(int); tp['pr3'] = tp.price.round(3)
ev = tp.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), pmin=('price', 'min'), pmax=('pr3', 'max'), S=('sh', 'sum'), npr=('pr3', 'nunique'), nmk=('maker', 'nunique')).reset_index(); tp = tp.drop(columns=['pr3'])
tev_ = ev.tx.map(TEV).values; tev_abs = np.where(np.isfinite(tev_), np.nan_to_num(tev_, nan=-1.0), -1.0).astype(np.int64)
tm, RAMA, ROW, DEX, C_EPOCA, NEX = ST.stamp_events(D.qt, D.v0, D.v2, D.qb, ev.k.values, tev_abs, ev.pmax.values, ev.pmin.values, ev.S.values, ev.npr.values)
sinev = RAMA == 'sinev'; tm = np.where(sinev, ev.t.values - 63, tm); import collections; print('ramas sello v3', dict(collections.Counter(RAMA)), 'c_epoca', C_EPOCA, flush=True)
ev['tm'] = tm - XS; tp = tp.merge(ev[['k', 'tx', 'tm']], on=['k', 'tx'], how='left'); tp['t_ws_ms'] = tp.tm.astype(np.int64)
E.tape = G.Tape('chain', D, tp.drop(columns=['k', 'tm'])); del tp, tape; gc.collect()
''' % L2
src = src[:i0] + NEW + src[i1:]
sys.argv = [DEV, d]; os.environ['CALMA_V3_OUT'] = OUTD
exec(compile(src, DEV, 'exec'), {'__file__': DEV, '__name__': '__main__'})
