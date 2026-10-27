#!/usr/bin/env python3
"""v3_B.py -- VERIFICACION INDEPENDIENTE: rellenos REALES de B. Ledger (movimientos/posiciones) + m5_onchain CRUDO (tx + maker==wallet dedicada) + f_D 09-18 propios."""
import sys, json, gzip, numpy as np, pandas as pd
sys.path.insert(0, '/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/verificacion')
import vlib
from vlib import *
rng = np.random.default_rng(777)
C = '/root/polymarket-research/experimentos/5m_barato/contabilidad_wallet_dedicada/'
M = pd.read_csv(C + 'movimientos.csv'); Pz = pd.read_csv(C + 'posiciones.csv')
B = M[(M.tipo == 'COMPRA') & (M.experimento == 'H47-B')].copy()
B['coste'] = -B.importe_pusd; B['coin'] = B.mercado.str.split('-').str[0].str.upper()
print('compras B', len(B), 'tx unicos', B.tx.nunique(), B.fecha_utc.min(), B.fecha_utc.max(), 'monedas', B.coin.value_counts().to_dict())
print('precio*size vs coste: max |dif|', float((B.precio * B['size'] - B.coste).abs().max()), '| rol:', B.rol.value_counts().to_dict())
txs = set(B.tx); rows = []
for d in sorted(set(B.fecha_utc.str[:10])):
    f = '/mnt/HC_Volume_106538179/m5_onchain/m5_onchain_%s.csv.gz' % d
    try:
        for ch in pd.read_csv(f, usecols=['tipo', 'tx', 'log_index', 'ts_est', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt'], dtype={'token_id': str}, chunksize=300000):
            ch = ch[ch.tx.isin(txs) & (ch.maker.str.lower() == US) & (ch.tipo == 'F')]
            if len(ch): rows.append(ch.assign(arch=d))
    except FileNotFoundError:
        print('FALTA', f)
X = pd.concat(rows); X['taker'] = X.taker.str.lower()
print('filas on-chain F maker==wallet dedicada', len(X), 'tx', X.tx.nunique(), 'dup (tx,li)', int(X.duplicated(['tx', 'log_index']).sum()))
g = X.groupby('tx').taker.nunique(); print('tx con >1 taker distinto', int((g > 1).sum()), '| tx con >1 fila US', int((X.groupby('tx').size() > 1).sum()))
# precio/tam on-chain vs ledger
v = X.side.values == 1; X['sh'] = np.where(v, X.maker_amt, X.taker_amt); usd = np.where(v, X.taker_amt, X.maker_amt); X['usd'] = usd
Xt = X.groupby('tx').agg(taker=('taker', 'first'), sh=('sh', 'sum'), usd=('usd', 'sum'), nf=('sh', 'size'), side=('side', 'first')).reset_index()
J = B.merge(Xt, on='tx', how='left'); print('compras con taker on-chain', J.taker.notna().sum(), '/', len(J))
mm = J.taker.notna(); print('desajuste size ledger vs chain >0.01:', int((np.abs(J['size'][mm] - J.sh[mm]) > 0.01).sum()), '| coste >0.02:', int((np.abs(J.coste[mm] - J.usd[mm]) > 0.02).sum()))
print('faltan:', J[~mm][['fecha_utc', 'mercado']].head(20).to_string())
# desenlace oficial por posicion (ledger) + contraste con precierre cache (slug->Up/Down) + clob
Pz2 = Pz[Pz.experimento.str.contains('H47-B', na=False)][['mercado', 'outcome', 'estado', 'payout', 'coste', 'pnl_realizado']]
J = J.merge(Pz2.rename(columns={'coste': 'coste_pos'}), on=['mercado', 'outcome'], how='left')
PRE = json.load(open('/root/polymarket-research-datalogs/precierre_desenlaces_cache.json'))
J['ganador_pre'] = J.mercado.map(PRE)
J['gana_led'] = J.estado.map({'liquidada_ganada': 1, 'liquidada_perdida': 0})
J['gana_pre'] = np.where(J.ganador_pre.isna(), np.nan, (J.ganador_pre == J.outcome).astype(float))
cc = J.gana_led.notna() & J.gana_pre.notna()
print('desenlace: ledger vs precierre_cache: comparables', int(cc.sum()), 'discrepan', int((J.gana_led[cc] != J.gana_pre[cc]).sum()), '| sin desenlace ledger', int(J.gana_led.isna().sum()), '| sin pre-cache', int(J.gana_pre.isna().sum()))
J['gana'] = J.gana_led.fillna(J.gana_pre)
J['pnl'] = J['size'] * J.gana - J.coste
J['pnl_aut'] = J.pnl_realizado * J.coste / J.coste_pos
print('PNL total fills (mio) por desenlace:', round(J.pnl.sum(), 4), '| autor (alloc. posicion):', round(J.pnl_aut.sum(), 4), '| n', len(J))
J = J[J.pnl.notna() & J.taker.notna()].copy()
J['cierre'] = J.mercado.str.extract(r'(\d+)$')[0]
print('n fills usables', len(J), 'cierres', J.cierre.nunique(), 'coste', round(J.coste.sum(), 2), 'EV_total', round(J.pnl.sum() / J.coste.sum(), 4), 'pnl', round(J.pnl.sum(), 3))
print('por moneda:', J.groupby('coin').apply(lambda g: pd.Series({'n': len(g), 'EV': g.pnl.sum() / g.coste.sum()})).round(3).to_dict('index'))
# --- conjuntos
S = pd.read_pickle(V + 'sets_codes.pkl'); codes = S['codes']; vlib._codes.update(codes); SAw = set(k for k, v in codes.items() if v in S['SA'])
acc = []
for d in pd.date_range('2026-10-09', '2026-10-18').strftime('%Y-%m-%d'):
    Xd, ok = load_day(d); Xd = Xd[ok]; res = Xd.gana.values >= 0; Xd = Xd[res & (Xd.tk.values != vlib._codes.get(US, -9))]
    pm = pnl_m(Xd); fee = FEE * Xd.sh.values * Xd.pc.values * (1 - Xd.pc.values)
    acc.append(pd.DataFrame({'tk': Xd.tk.values, 'p': -pm - fee, 'pg': -pm, 'c': Xd.sh.values * (1 - Xd.pc.values)}))
Aq = pd.concat(acc).groupby('tk').agg(p=('p', 'sum'), pg=('pg', 'sum'), c=('c', 'sum'), n=('p', 'size'))
inv_ = {v: k for k, v in vlib._codes.items()}
inf_net = set(inv_[t] for t in Aq[(Aq.n >= 100) & (Aq.c >= 200) & (Aq.p / Aq.c >= .02)].index)
inf_gro = set(inv_[t] for t in Aq[(Aq.n >= 100) & (Aq.c >= 200) & (Aq.pg / Aq.c >= .02)].index)
print('informados 09-18 neto', len(inf_net), 'bruto', len(inf_gro), 'S_A (prereg, mis sets)', len(SAw))
c = J.coste.values; p = J.pnl.values; cl = pd.factorize(J.cierre)[0]; ncl = cl.max() + 1; tkx = J.taker.values
def exc(f): return p[~f].sum() / c[~f].sum() - p.sum() / c.sum()
def run(nm, st, Bp=5000):
    f = J.taker.isin(st).values; obs = exc(f)
    Pt = np.bincount(cl, p, ncl); Ct = np.bincount(cl, c, ncl); Pr = np.bincount(cl, p * ~f, ncl); Cr = np.bincount(cl, c * ~f, ncl)
    w = rng.multinomial(ncl, np.ones(ncl) / ncl, size=3000).astype(float); e = (w @ Pr) / (w @ Cr) - (w @ Pt) / (w @ Ct)
    perm_f = np.array([exc(rng.permutation(f)) for _ in range(Bp)])
    # permutacion a nivel TOMADOR: reetiquetar k tomadores distintos al azar entre los tomadores presentes en B
    ut = np.unique(tkx); k = len(np.unique(tkx[f])); pt = np.array([exc(np.isin(tkx, rng.choice(ut, k, replace=False))) for _ in range(Bp)])
    # permutacion a nivel TOMADOR restringida al pool de los takers activos 09-18 (n>=100,c>=200) sin criterio de ROI
    pool = set(inv_[t] for t in Aq[(Aq.n >= 100) & (Aq.c >= 200)].index) & set(ut); pool = np.array(sorted(pool))
    pp = np.array([exc(np.isin(tkx, rng.choice(pool, min(k, len(pool)), replace=False))) for _ in range(Bp)])
    fi = np.where(f)[0]; loss = np.sort(p[fi])
    r = dict(n_flag_fills=int(f.sum()), n_flag_cierres=int(len(set(J.cierre[f]))), n_flag_takers=k, frac_eur=float(c[f].sum() / c.sum()), pnl_flag=float(p[f].sum()), pnl_no=float(p[~f].sum()),
             EV_flag=float(p[f].sum() / c[f].sum()) if f.any() else None, EV_no=float(p[~f].sum() / c[~f].sum()), EXCESO=float(obs), IC90_cierre=[float(np.percentile(e, 5)), float(np.percentile(e, 95))],
             p_perm_fill=float((1 + (perm_f >= obs).sum()) / (Bp + 1)), p_perm_taker_pool_B=float((1 + (pt >= obs).sum()) / (Bp + 1)), p_perm_taker_pool_activos=float((1 + (pp >= obs).sum()) / (Bp + 1)), n_pool=int(len(pool)),
             peores5_flag=[round(float(x), 2) for x in loss[:5]])
    # EXCESO sin el cierre banderado mas perdedor y sin los 3 mas perdedores
    pc_ = pd.DataFrame({'cl': J.cierre.values[f], 'p': p[f]}).groupby('cl').p.sum().sort_values()
    for kk in (1, 3):
        drop = set(pc_.index[:kk]); f2 = f & ~J.cierre.isin(drop).values; m = ~J.cierre.isin(drop).values
        r['EXC_sin_%d_peores_cierres_banderados' % kk] = float(p[m & ~f2].sum() / c[m & ~f2].sum() - p[m].sum() / c[m].sum())
    # por unidad de posicion (mercado, outcome)
    U = J.assign(f=f).groupby(['mercado', 'outcome']).agg(p=('pnl', 'sum'), c=('coste', 'sum'), f=('f', 'max')).reset_index()
    r['unidades_posicion'] = int(len(U)); r['EXC_unidad_posicion'] = float(U.p[U.f == 0].sum() / U.c[U.f == 0].sum() - U.p.sum() / U.c.sum())
    r['EV_pond_euro_vs_media_unidad'] = dict(pond=float(U.p.sum() / U.c.sum()), media=float((U.p / U.c).mean()))
    print(nm, json.dumps(r, default=float)); return r
OUT = {'S_A': run('S_A_prereg(mis sets)', SAw), 'inf_net_09_18': run('informados 09-18 neto>=2%', inf_net), 'inf_bruto_09_18': run('informados 09-18 bruto>=2%', inf_gro)}
J[['fecha_utc', 'mercado', 'outcome', 'coste', 'pnl', 'taker', 'gana']].to_csv('/mnt/HC_Volume_106538179/agentes_datos/as_tomador/verif/B_fills_mio.csv', index=False)
# concentracion de los banderados por tomador/dia
f = J.taker.isin(inf_net).values; print(J[f].groupby('taker').agg(n=('pnl', 'size'), pnl=('pnl', 'sum'), c=('coste', 'sum')).sort_values('pnl').head(8).round(2))
print(J[f].assign(dia=J.fecha_utc.str[:10][f]).groupby('dia').agg(n=('pnl', 'size'), pnl=('pnl', 'sum')).round(2).T)
print(J.assign(dia=J.fecha_utc.str[:10]).groupby('dia').agg(n=('pnl', 'size'), pnl=('pnl', 'sum'), c=('coste', 'sum')).round(2).T)
json.dump(OUT, open('/root/polymarket-research/experimentos/5m_barato/b_perdidas_22oct/as_tomador/verificacion/v3_resultados.json', 'w'), indent=1, default=float)
