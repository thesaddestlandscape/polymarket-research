#!/usr/bin/env python3
"""esc_v3b.py DIA -- esc_dec2_v3 (Calma-T1 con sello passT_v3) con tres cambios, TODO lo demas ejecutado desde el fuente dev de esc_dec2.py:
 (1) cinta tape2 (todas las horas, src tx_ws|bloque) en vez de tape (solo horas sanas); (2) exclusion de mercados por VENTANAS (engine_copy.sane) segun MODE:
   hora   = horas con <95 % tx_ws (regla vieja; debe reproducir recalc_13nov/out/dec2v3_*)
   hole60 = huecos libro5_tx +-60 s (sin reconstruccion)
   rec    = sello reconstruido para fills sin t_ev (tx fuera de libro5_tx): firma exacta (token,precio,tamano) en libro5_ms (q) en +-3 s de bloque-2,25 s; solo se excluyen
            +-5 s alrededor de eventos NO recuperados (firma ausente/ambigua)
 (3) validacion de la reconstruccion en eventos CON t_ev (rama sig verdadera) -> meta.
Env: MODE, HF_OUT. Solo lectura; 0 ordenes."""
import sys, os, json
HF = os.path.dirname(os.path.abspath(__file__)) + '/'; L2 = os.path.dirname(os.path.dirname(os.path.dirname(HF.rstrip('/')))) + '/'
DEV = '/root/polymarket-research-dev/misiones/5m_barato/sonda1/p2/A3_guarda/ret_cinta_corregida/descomp/esc_dec2.py'
sys.path.insert(0, HF); import engine_copy; sys.modules['engine'] = engine_copy
src = open(DEV).read(); d = sys.argv[1]; MODE = os.environ['MODE']; OUTD = os.environ['HF_OUT']; os.makedirs(OUTD, exist_ok=True)
A = "H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = H + 'out/'"; assert src.count(A) == 1
src = src.replace(A, "H = os.path.dirname(os.path.abspath(__file__)) + '/'; OUT = os.environ['HF_OUT'].rstrip('/') + '/'")
B = "TAGF = 'dec2' if XS == 0 else f'dec3s{XS}'"; assert src.count(B) == 1
src = src.replace(B, "TAGF = (MODE + '_dec2v3') if XS == 0 else f'{MODE}_dec3v3s{XS}'")
C = "tape = pd.read_pickle(PB + f'tape_{d}.pkl'); bad = {tuple(x) for x in json.load(open(PB + f'bad_{d}.json'))['bad']}"; assert src.count(C) == 1
src = src.replace(C, """tape = pd.read_pickle(HFD + f'out/tape2_{d}.pkl'); META = json.load(open(HFD + f'out/meta2_{d}.json')); _d0 = int(pd.Timestamp(d, tz='UTC').timestamp() * 1000)
if MODE == 'hora': bad = [(_d0 + h * 3600000, _d0 + (h + 1) * 3600000) for dd_, h in META['bad_hours']]
elif MODE == 'hole60': bad = [(a - 60000, b + 60000) for a, b in META['holes']]
else: bad = []   # rec: se rellena tras el sello
""")
i0 = src.index('# --- cinta re-sincronizada (identica a pol_day.py / esc_ret.py)'); i1 = src.index('NMK = {}'); assert 0 < i0 < i1
NEW = '''# --- cinta con SELLO v3 + reconstruccion (huecos_fix)
import stamp_v3 as ST, glob, gc, collections
TXD = '/mnt/HC_Volume_106538179/libro5_tx/'; fr = []
for dd_ in [(pd.Timestamp(d) + pd.Timedelta(days=i)).strftime('%Y-%m-%d') for i in (-1, 0, 1)]:
    for f_ in sorted(glob.glob(TXD + f'libro5_tx_{dd_}_*.csv.gz')):
        try: fr.append(pd.read_csv(f_, header=None, names=['t_ev', 'token', 'tx', 'recv'], dtype={'token': str, 'tx': str}, on_bad_lines='skip'))
        except Exception as e_: print('err', f_, e_)
TEV = pd.concat(fr, ignore_index=True).groupby('tx').t_ev.min() if fr else pd.Series(dtype='int64'); del fr
tp = tape.assign(k=tape.token_id.map(D.tokidx)); tp = tp[tp.k.notna()].copy(); tp['k'] = tp.k.astype(int); tp['pr3'] = tp.price.round(3)
ev = tp.groupby(['k', 'tx']).agg(t=('t_ws_ms', 'min'), pmin=('price', 'min'), pmax=('pr3', 'max'), S=('sh', 'sum'), npr=('pr3', 'nunique'), nmk=('maker', 'nunique'), tse=('ts_est', 'min')).reset_index(); tp = tp.drop(columns=['pr3'])
tev_ = ev.tx.map(TEV).values; tev_abs = np.where(np.isfinite(tev_), np.nan_to_num(tev_, nan=-1.0), -1.0).astype(np.int64)
tm, RAMA, ROW, DEX, C_EPOCA, NEX = ST.stamp_events(D.qt, D.v0, D.v2, D.qb, ev.k.values, tev_abs, ev.pmax.values, ev.pmin.values, ev.S.values, ev.npr.values)
sinev = RAMA == 'sinev'
# reconstruccion de t_ev SIN libro5_tx: busca el print en las filas T (WS trades) de libro5_ms (D.tt/D.tsz) del token k o su complemento, tamano = S (+-0,011) en +-3 s de bloque-2,25 s;
# si hay un unico instante candidato, tev_rec = ese instante; luego el sello es EL MISMO ST.stamp_events (misma definicion v3, mismas ramas).
n_ = len(ev); tsyn = (ev.tse.values * 1000 - 2250).astype(np.int64); tev_rec = np.full(n_, -1, np.int64); nc_rec = np.zeros(n_, np.int32)
for i in range(n_):
    k = int(ev.k.values[i]); S_ = float(ev.S.values[i]); c_ = set()
    for kk in (k, D.comp(k)):
        if kk is None: continue
        a, b = int(D.tb[kk]), int(D.tb[kk + 1])
        if b <= a: continue
        t_ = D.tt[a:b]; i0_ = np.searchsorted(t_, tsyn[i] - 3000, 'left'); i1_ = np.searchsorted(t_, tsyn[i] + 3000, 'right')
        if i1_ > i0_:
            m_ = np.abs(D.tsz[a + i0_:a + i1_].astype(float) - S_) < 0.011
            c_.update(int(x) for x in t_[i0_:i1_][m_])
    nc_rec[i] = len(c_)
    if len(c_) == 1: tev_rec[i] = next(iter(c_))
tm_r, RAMA_r, _, _, _, _ = ST.stamp_events(D.qt, D.v0, D.v2, D.qb, ev.k.values, tev_rec, ev.pmax.values, ev.pmin.values, ev.S.values, ev.npr.values)
kn = ~sinev; sg = (RAMA == 'sig')
VAL = dict(n_con_tev=int(kn.sum()), tev_recuperado=int((kn & (tev_rec >= 0)).sum()), tev_igual=int((kn & (tev_rec == tev_abs)).sum()), tev_distinto=int((kn & (tev_rec >= 0) & (tev_rec != tev_abs)).sum()),
           cand0=int((kn & (nc_rec == 0)).sum()), cand_multi=int((kn & (nc_rec >= 2)).sum()), tm_igual=int((kn & (tev_rec >= 0) & (tm_r == tm)).sum()),
           tm_dif_abs_p50=float(np.median(np.abs((tm_r - tm)[kn & (tev_rec >= 0)]))) if (kn & (tev_rec >= 0)).any() else None, tm_dif_abs_p99=float(np.percentile(np.abs((tm_r - tm)[kn & (tev_rec >= 0)]), 99)) if (kn & (tev_rec >= 0)).any() else None,
           rama_igual=int((kn & (tev_rec >= 0) & (RAMA_r == RAMA)).sum()))
recok = sinev & (tev_rec >= 0)
if MODE == 'rec':
    tm = np.where(recok, tm_r, tm); RAMA = np.where(recok, np.char.add('rec_', RAMA_r.astype(str)), RAMA)
    unrec = sinev & ~recok; E.bad = [(int(t_) - 5000, int(t_) + 5000) for t_ in ev.t.values[unrec]]
tm = np.where(RAMA == 'sinev', ev.t.values - 63, tm)
META_OUT = dict(ramas={str(k_): int(v_) for k_, v_ in collections.Counter(RAMA).items()}, n_sinev=int(sinev.sum()), n_sinev_recuperado=int(recok.sum()), n_ev=int(n_), VAL=VAL, MODE=MODE, n_ventanas_excl=len(E.bad))
print('ramas', META_OUT, flush=True); json.dump(META_OUT, open(OUT + f'{TAGF}_meta_{d}.json', 'w'))
ev['tm'] = tm - XS; tp = tp.merge(ev[['k', 'tx', 'tm']], on=['k', 'tx'], how='left'); tp['t_ws_ms'] = tp.tm.astype(np.int64)
E.tape = G.Tape('chain', D, tp.drop(columns=['k', 'tm'])); del tp, tape; gc.collect()
'''
src = src[:i0] + NEW + src[i1:]
src = src.replace("PB = P2 + 'precursores_barrido/out/'", "PB = P2 + 'precursores_barrido/out/'; HFD = %r" % HF, 1)
sys.argv = [DEV, d]
exec(compile(src, DEV, 'exec'), {'__file__': DEV, '__name__': '__main__', 'MODE': MODE})
