#!/usr/bin/env python3
"""FRENTE 2 / motor passT + IW (10-Nov, alpha-miner). EXPLORATORIO sobre dias QUEMADOS, DEV, 0 ordenes, sin tocar passT.py ni engine.py.
passT.py es un SCRIPT (no importable: ejecuta el dia entero y escribe RT_/SEGT_), asi que se IMPORTA por AST: se verifica su sha256 y se ejecuta
SIN CAMBIOS (a) todo su preludio (carga del motor engine, cinta resincronizada, FE, Binance XS, JUMP, y las funciones run_var/ftype/bnr/first_after),
(b) las sentencias de rasgo/armado de su bucle principal: preambulo por token (g,tq,b300,r3,...) y por nivel Gm, base, bloque `with` (bl, geo6, nj3..).
La decision de armado de GEO6 es por tanto la LITERAL de passT (geo6 = isfinite(b300) & (bl >= 0.06-1e-6), bl = bid(t-300)-L).
Solo se anade el rasgo IW (Binance desde la apertura del 5m, recepcion, solo ticks <= t_dec-300, signado a favor del lado) y se llama al MISMO run_var.
Variantes: G0, GEO6, IW5, GEO6IW5, IWINV5, GEO6IWINV5, PIW5_s / PGEO6IW5_s (placebo: iw5 de OTRO mercado del dia, misma moneda y lado, mismo tiempo desde la apertura).
Uso: nice -n 19 ionice -c3 python3 -I passT_iw.py DIA -> out/MI_<D>.pkl (idempotente)."""
import sys, os, ast, json, hashlib, time
T0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__)) + '/'
PASST = '/root/polymarket-research/experimentos/5m_barato/q11/toxicidad_thru1/passT.py'
PASST_SHA = 'a8b9d7a0158fd0b0cf47582c499d6c1cc870269310c8ef4481482733d1c64038'
d = sys.argv[1]
if d >= '2026-11-09': raise SystemExit('solo dias quemados 26-Oct..08-Nov')
OUTF = HERE + f'out/MI_{d}.pkl'
src = open(PASST).read()
assert hashlib.sha256(src.encode()).hexdigest() == PASST_SHA, 'passT.py cambio: sha distinto del registrado'
import numpy as np, pandas as pd
tree = ast.parse(src, PASST)
i_f = next(i for i, n in enumerate(tree.body) if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) and n.targets[0].id == 'FILLS')
PRE = tree.body[:i_f]; LOOP = tree.body[i_f + 2]
assert isinstance(LOOP, ast.For) and LOOP.target.id == 'k', ast.dump(LOOP)[:80]
KPRE = [n for n in LOOP.body if not isinstance(n, ast.For)]; LL = next(n for n in LOOP.body if isinstance(n, ast.For))
def tg(n): return n.targets[0].id if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name) else None
LSEL = [n for n in LL.body if tg(n) in ('Gm', 'base') or isinstance(n, ast.With)]
assert [tg(n) for n in LSEL] == ['Gm', 'base', None], [tg(n) for n in LSEL]
assert 'geo6 = np.isfinite(b300) & (bl >= 0.06 - 1e-6)' in src
# ejecutar el preludio de passT (sin cambios) con __file__ y argv propios; OUT de passT = carpeta inexistente de aqui (no escribe nada en el preludio)
ns = {'__name__': 'passT_prelude', '__file__': HERE + '_ref/passT.py'}
sys.argv = [PASST, d]
exec(compile(ast.Module(body=PRE, type_ignores=[]), PASST, 'exec'), ns)
G = ns['G']; E = ns['E']; D = ns['D']; XS = ns['XS']; run_var = ns['run_var']; ftype = ns['ftype']; ks = ns['ks']
def run_stmts(nodes):
    for n in nodes: exec(compile(ast.Module(body=[n], type_ignores=[]), PASST, 'exec'), ns)
def iw_feat(coin, op, tq, sgn):
    """Binance recepcion: retorno (bps) entre el ultimo tick <= op y el ultimo tick <= tq, signado a favor del lado. Frescura 15 s en ambos. tq<op o sin dato -> NaN (se arma)."""
    n = len(tq); A_ = XS.get(coin)
    if A_ is None: return np.full(n, np.nan), np.full(n, -1, np.int64)
    t, p = A_; ia = int(np.searchsorted(t, op, side='right')) - 1; ib = np.searchsorted(t, tq, side='right') - 1
    ok = (tq >= op) & (ia >= 0) & (ib >= 0)
    if ia < 0: return np.full(n, np.nan), np.full(n, -1, np.int64)
    ibc = np.maximum(ib, 0); ok &= (t[ia] >= op - 15000) & (t[ibc] >= tq - 15000)
    r = np.where(ok, sgn * (p[ibc] / p[ia] - 1) * 1e4, np.nan); return r, np.where(ok, t[ibc], -1)
SEEDS = range(1, 31); VAR = ['G0', 'GEO6', 'IW5', 'GEO6IW5', 'IWINV5', 'GEO6IWINV5'] + [f'PIW5_{s}' for s in SEEDS] + [f'PGEO6IW5_{s}' for s in SEEDS]
FILLS = []; AUD = dict(n_iw=0, viol_iw=0, n_b300=0, viol_b300=0, nan_iw=0, n_el=0, trunc_n=0, trunc_bad=0)
rs_t = np.random.default_rng(20261110)
# placebo con el MISMO perfil temporal: iw5 de OTRO mercado del dia (misma moneda y lado, mismo indice de rejilla = mismo tiempo desde la apertura); rejilla = E.grid, igual que passT
IWM = {}
for k_ in ks:
    gg = E.grid(k_); op_ = (int(D.fin[k_]) - 300) * 1000; IWM[k_] = iw_feat(D.act[k_], op_, gg - 300, 1.0 if D.lado[k_] == 'YES' else -1.0)[0] <= -5
PART = {}
for k_ in ks: PART[k_] = [k2 for k2 in ks if k2 != k_ and D.act[k2] == D.act[k_] and D.lado[k2] == D.lado[k_] and len(IWM[k2]) == len(IWM[k_])]
for k in ks:
    ns['k'] = k; run_stmts(KPRE)   # g,bid,ask,... fin,gana,coin,lado,sgn, tq,b300,b3300, r3,dbid3, J,jadv,ja3, a_,b_,qt,v0 (literal de passT)
    g = ns['g']; fin = ns['fin']; gana = ns['gana']; coin = ns['coin']; lado = ns['lado']; sgn = ns['sgn']; tq = ns['tq']; b300 = ns['b300']
    op = (int(fin) - 300) * 1000; iwr, tbu = iw_feat(coin, op, tq, sgn); iw5 = iwr <= -5; iwinv = iwr >= 5   # NaN -> False -> se arma
    # ---- auditoria de causalidad (rasgos solo con datos <= tq < t_dec)
    v = tbu >= 0; AUD['n_iw'] += int(v.sum()); AUD['viol_iw'] += int((tbu[v] > tq[v]).sum()); AUD['nan_iw'] += int(np.isnan(iwr).sum()); AUD['n_el'] += len(tq)
    a_q, b_q = D.qb[k], D.qb[k + 1]; qtt = D.qt[a_q:b_q]
    if b_q > a_q:
        jq = np.searchsorted(qtt, tq, side='right') - 1; okq = jq >= 0; AUD['n_b300'] += int(okq.sum()); AUD['viol_b300'] += int((qtt[np.where(okq, jq, 0)][okq] > tq[okq]).sum())
    if XS.get(coin) is not None and len(tq) > 6:   # test de truncamiento: iw recalculado con la serie Binance cortada en tq debe dar lo mismo
        t_, p_ = XS[coin]
        for ii in rs_t.integers(0, len(tq), 6):
            cut = int(np.searchsorted(t_, tq[ii], side='right')); sv = XS[coin]; XS[coin] = (t_[:cut], p_[:cut])
            r2, _ = iw_feat(coin, op, tq[ii:ii + 1], sgn); XS[coin] = sv; AUD['trunc_n'] += 1
            if not (np.isnan(r2[0]) and np.isnan(iwr[ii])) and not (r2[0] == iwr[ii]): AUD['trunc_bad'] += 1
    for L in G.LEVELS:
        ns['L'] = L; run_stmts(LSEL); Gm = ns['Gm']; base = ns['base']; geo6 = ns['geo6']
        rng = np.random.default_rng(k * 131 + int(L * 100) + 777)
        specs = {'G0': base, 'GEO6': base & geo6, 'IW5': base & ~iw5, 'GEO6IW5': base & geo6 & ~iw5, 'IWINV5': base & ~iwinv, 'GEO6IWINV5': base & geo6 & ~iwinv}
        for s in SEEDS:
            pr = np.random.default_rng(k * 977 + s * 13 + 5); ip = IWM[PART[k][int(pr.integers(0, len(PART[k])))]] if PART[k] else iw5
            specs[f'PIW5_{s}'] = base & ~ip; specs[f'PGEO6IW5_{s}'] = base & geo6 & ~ip
        for name in VAR:
            for (si, t, t_arr, t_end, q, tf, canc) in run_var(k, L, g, specs[name], Gm, fin, None):
                if q > 1e-9:
                    ig = int(np.searchsorted(g, t)); FILLS.append((name, d, coin, lado, fin, k, L, q, tf, (fin * 1000 - tf) / 1000.0, gana, si, t, ftype(k, L, tf), canc, float(iwr[ig]), float(b300[ig] - L)))
R = pd.DataFrame(FILLS, columns=['var', 'dia', 'act', 'lado', 'fin', 'k', 'L', 'q', 'tf', 'T', 'gana', 'seg', 't_dec', 'ftype', 'canc', 'iw_bps', 'bidL'])
R['cost'] = R.q * R.L; R['pnl'] = R.q * (R.gana - R.L) + R.q * 0.2 * 0.07 * R.L * (1 - R.L)   # misma formula que passT
R.attrs['aud'] = AUD; R.to_pickle(OUTF + '.tmp'); os.replace(OUTF + '.tmp', OUTF)
json.dump({'dia': d, 'passT_sha': PASST_SHA, 'aud': AUD, 'n_fills': {v: int(len(x)) for v, x in R.groupby('var', sort=False) if not v.startswith('P')}, 'seg': round(time.time() - T0, 1)}, open(HERE + f'out/MI_{d}.json', 'w'))
print('ok', d, {v: (len(x), round(float(x.pnl.sum()), 1)) for v, x in R.groupby('var', sort=False) if not v.startswith('P')}, 'AUD', AUD, round(time.time() - T0, 1), 's', flush=True)
