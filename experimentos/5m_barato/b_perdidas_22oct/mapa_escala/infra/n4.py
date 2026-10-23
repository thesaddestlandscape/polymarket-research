#!/usr/bin/env python3
"""n4.py - nicho de MINERIA N4 (5m pc en [0.01,0.10)) segun PREREG_TESTS_ADENDA_N4.md (sha256 7d7929dd...). Rejilla fija 1.485 celdas.
Subcomandos: backfill (descriptivo 06..22-Oct, NO gatea) | eval [--telegram] (forward 24-Oct..02-Nov). Las celdas diarias forward las escribe tp1.dia() via celdas()."""
import sys, os, math, argparse, json, datetime as dt
import numpy as np, pandas as pd
import infra_lib as L, tp1 as P
SHA_ADENDA = '7d7929dd922b365c1d91e2fcabb55c694099934365342db87430853beeaaf55b'
COINS = ['BTC', 'ETH', 'SOL', 'XRP', 'DOGE', 'BNB']
CSETS = {**{c: [c] for c in COINS}, 'ALT3': ['ETH', 'SOL', 'XRP'], 'ETHSOL': ['ETH', 'SOL'], 'ALL': COINS}
BSETS = {**{f'{0.01 * (i + 1):.2f}-{0.01 * (i + 2):.2f}': [i] for i in range(9)}, 'L0.01-0.05': [0, 1, 2, 3], 'H0.05-0.10': [4, 5, 6, 7, 8]}
TSETS = {'60-120': [0], '120-180': [1], '180-240': [2], '240-300': [3], 'TODO': [0, 1, 2, 3]}
LSETS = {'YES': ['YES'], 'NO': ['NO'], 'AMBOS': ['YES', 'NO']}
MIN_CIERRES = 100; GATE_EV = 0.02; COB_MIN = 0.995
REF = ('ETHSOL', 'H0.05-0.10', 'TODO', 'AMBOS')
def celdas(X):
    """X = fills 5m ya clasificados (tp1.clasifica). -> agregado por (coin,b,tt,lc,mid,maker) con fin."""
    S = X[(X.pc >= 0.01) & (X.pc < 0.10) & (X['T'] >= 60) & (X['T'] < 300)].copy()
    S['b'] = np.minimum(np.floor((S.pc.values - 0.01) / 0.01 + 1e-9).astype(int), 8); S['tt'] = np.digitize(S['T'].values, [60, 120, 180, 240, 300]) - 1
    return S.groupby(['coin', 'b', 'tt', 'lc', 'mid', 'maker'], sort=False).agg(coste=('coste', 'sum'), acc=('acc', 'sum'), reb=('reb', 'sum'), nf=('coste', 'size'), fin=('fin', 'first')).reset_index()
def backfill_dia(d):
    tok = json.load(open(L.ROOT / 'mapa_escala/tokens.json')); tk = {t: v for t, v in tok.items() if v[1] == '5min'}
    X, nrow, ndup = P.calcula_marco(d, '5min', tk); return celdas(P.clasifica(X)) if len(X) else pd.DataFrame(), nrow, ndup
def carga(d, des, backfill=False):
    f = (L.TP1 / 'n4_backfill' if backfill else P.dirs()) / f'celdas_n4_{d}.csv.gz'
    if not f.exists(): return None
    C = pd.read_csv(f, dtype={'mid': str, 'maker': str, 'lc': str, 'coin': str}); C['des'] = C.mid.map(des); ok = C.des.notna()
    C['pnl'] = np.where(ok, C.acc * (C.lc == C.des).astype(float) - C.coste, 0.0); C['dia'] = d
    cob = C.coste[ok].sum() / C.coste.sum() if C.coste.sum() > 0 else np.nan
    return C[ok].drop(columns=['des']), float(cob)
def normal_sf(z): return 0.5 * math.erfc(z / math.sqrt(2))
def bh(p):
    p = np.asarray(p); n = len(p); o = np.argsort(p); q = np.empty(n); r = p[o] * n / (np.arange(n) + 1); q[o] = np.minimum(np.minimum.accumulate(r[::-1])[::-1], 1); return q
def minera(C, dias_, mitad_corte, forward=True):
    """C: filas (dia,coin,b,tt,lc,mid,maker,fin,coste,acc,reb,pnl) de los dias validos. -> DataFrame de celdas."""
    G = C.groupby(['dia', 'coin', 'b', 'tt', 'lc', 'fin'], observed=True)[['pnl', 'coste', 'reb']].sum().reset_index()
    di = {d: i for i, d in enumerate(dias_)}; G['di'] = G.dia.map(di).values; fu, fi = np.unique(G.fin.values, return_inverse=True); NF = len(fu); K = len(dias_) * NF
    key = G.di.values * NF + fi; pnl, cos, reb = G.pnl.values, G.coste.values, G.reb.values
    mc = {k: G.coin.isin(v).values for k, v in CSETS.items()}; mb = {k: G.b.isin(v).values for k, v in BSETS.items()}; mt = {k: G.tt.isin(v).values for k, v in TSETS.items()}; ml = {k: G.lc.isin(v).values for k, v in LSETS.items()}
    dmask = np.array([d <= mitad_corte for d in dias_]); rows = []
    for cs in CSETS:
        for bs in BSETS:
            m1 = mc[cs] & mb[bs]
            for ts in TSETS:
                m2 = m1 & mt[ts]
                for ls in LSETS:
                    m = m2 & ml[ls]
                    if not m.any(): continue
                    P_ = np.bincount(key[m], weights=pnl[m], minlength=K); C_ = np.bincount(key[m], weights=cos[m], minlength=K); R_ = np.bincount(key[m], weights=reb[m], minlength=K)
                    pd_ = P_.reshape(len(dias_), NF).sum(1); cd_ = C_.reshape(len(dias_), NF).sum(1); fc = np.flatnonzero(C_ > 0)
                    if len(fc) == 0: continue
                    ev = P_.sum() / C_.sum(); se = math.sqrt(np.sum((P_[fc] - ev * C_[fc]) ** 2)) / C_.sum(); p = normal_sf(ev / se) if se > 0 else (0.0 if ev > 0 else 1.0)
                    pf = np.sort(P_[fc])[::-1]; top5 = np.argsort(-P_[fc])[:5]; kp = np.ones(len(fc), bool); kp[top5] = False
                    ev5 = P_[fc][kp].sum() / C_[fc][kp].sum() if C_[fc][kp].sum() > 0 else np.nan
                    o2 = np.argsort(-pd_)[:2]; k2 = np.ones(len(dias_), bool); k2[o2] = False; ev2d = pd_[k2].sum() / cd_[k2].sum() if cd_[k2].sum() > 0 else np.nan
                    h1 = dmask; h2 = ~dmask
                    rows.append(dict(coin=cs, bucket=bs, T=ts, lado=ls, cierres=len(fc), dias_con_coste=int((cd_ > 0).sum()), coste=float(C_.sum()), vol_dia=float(C_.sum() / len(dias_)), pnl=float(P_.sum()), ev=float(ev),
                                     ev_reb=float((P_.sum() + R_.sum()) / C_.sum()), se=se, p=p, dias_pos=int((pd_ > 0).sum()), ev_sin5=float(ev5), ev_sin2dias=float(ev2d),
                                     ev_h1=float(pd_[h1].sum() / cd_[h1].sum()) if cd_[h1].sum() > 0 else np.nan, ev_h2=float(pd_[h2].sum() / cd_[h2].sum()) if cd_[h2].sum() > 0 else np.nan))
    R = pd.DataFrame(rows); T_ = R.cierres >= MIN_CIERRES; R['testeable'] = T_
    R['q_bh'] = np.nan; R['p_bonf'] = np.nan
    if T_.sum():
        R.loc[T_, 'q_bh'] = bh(R.loc[T_, 'p'].values); R.loc[T_, 'p_bonf'] = np.minimum(R.loc[T_, 'p'].values * T_.sum(), 1)
    R['m_testeables'] = int(T_.sum()); return R
def refina(R, C, B=1000, seed=20261024):
    """Para candidatos (cumplen 1,3,4 y testeables): IC90 por cierre (bootstrap) y concentracion del top-1 wallet. Anade columnas."""
    cand = R.testeable & (R.ev >= GATE_EV) & (R.dias_pos >= 7) & (R.ev_sin5 > 0)
    R['ic_lo_cierre'] = np.nan; R['ic_hi_cierre'] = np.nan; R['top1_wallet'] = np.nan
    for i in R.index[cand]:
        r = R.loc[i]; S = C[C.coin.isin(CSETS[r.coin]) & C.b.isin(BSETS[r.bucket]) & C.tt.isin(TSETS[r['T']]) & C.lc.isin(LSETS[r.lado])]
        g = S.groupby('fin')[['pnl', 'coste']].sum(); p, c = g.pnl.values, g.coste.values; n = len(p); rng = np.random.default_rng(seed)
        cnt = rng.multinomial(n, np.ones(n) / n, size=B).astype(np.float64); ev = (cnt @ p) / (cnt @ c); R.loc[i, 'ic_lo_cierre'] = np.quantile(ev, .05); R.loc[i, 'ic_hi_cierre'] = np.quantile(ev, .95)
        mk = S.groupby('maker').coste.sum(); R.loc[i, 'top1_wallet'] = mk.max() / mk.sum()
    return R
def cruza(R):
    return (R.testeable & (R.ev >= GATE_EV) & (R.ic_lo_cierre > 0) & (R.dias_pos >= 7) & (R.ev_sin5 > 0) & (R.q_bh < 0.10) & (R.top1_wallet <= 0.30) & (R.ev_sin2dias > 0) & (R.ev_h1 > 0) & (R.ev_h2 > 0)).fillna(False)
def texto(R, titulo, n_dias, extra=''):
    L_ = [titulo + f'  [adenda N4 sha {SHA_ADENDA[:12]}; EXPLORATORY; EV/EUR pond. sin rebate]', f'dias validos {n_dias}; celdas con coste {len(R)}, testeables (>= {MIN_CIERRES} cierres) {int(R.testeable.sum())}; ' + extra]
    cols = ['coin', 'bucket', 'T', 'lado', 'cierres', 'vol_dia', 'ev', 'ev_reb', 'dias_pos', 'ev_sin5', 'ev_sin2dias', 'ev_h1', 'ev_h2', 'p', 'q_bh', 'ic_lo_cierre', 'top1_wallet']
    top = R[R.testeable].sort_values('ev', ascending=False).head(15)
    L_.append('TOP 15 testeables por EV (informativo):'); L_.append(top[cols].round(4).to_string(index=False))
    ref = R[(R.coin == REF[0]) & (R.bucket == REF[1]) & (R['T'] == REF[2]) & (R.lado == REF[3])]
    L_.append('CELDA DE REFERENCIA ETHSOL 0.05-0.10 TODO AMBOS:'); L_.append(ref[cols].round(4).to_string(index=False) if len(ref) else 'sin datos')
    if 'ic_lo_cierre' in R: L_.append(f"celdas que CRUZAN el gate completo: {int(cruza(R).sum())}")
    return '\n'.join(L_)
def cmd_backfill():
    out = L.TP1 / 'n4_backfill'; out.mkdir(parents=True, exist_ok=True); des = L.read_json(L.ROOT / 'mapa_escala/des.json', {}); des.update(L.read_json(L.TP1 / 'des.json', {}))
    dd = L.dias('2026-10-06', '2026-10-22'); frames = []; dias_ok = []; meta = {}
    for d in dd:
        f = out / f'celdas_n4_{d}.csv.gz'
        if not f.exists():
            if not P.onchain('5min', d).exists(): continue
            C, nrow, ndup = backfill_dia(d)
            if len(C) == 0: continue
            C.to_csv(str(f) + '.tmp', index=False, compression='gzip'); os.replace(str(f) + '.tmp', f); L.log(f'n4 backfill {d}: {len(C)} celdas ({nrow} fills, {ndup} dup)')
        r = carga(d, des, backfill=True)
        if r is None: continue
        C, cob = r; meta[d] = cob
        if d == '2026-10-22' and cob < COB_MIN: continue           # 22-Oct: solo si esta completo
        if cob >= COB_MIN: frames.append(C); dias_ok.append(d)
    C = pd.concat(frames, ignore_index=True); R = minera(C, dias_ok, '2026-10-13', forward=False); R = refina(R, C)
    R.to_csv(out / 'n4_backfill_celdas.csv', index=False)
    txt = texto(R, 'N4 BACKFILL DESCRIPTIVO (NO forward, NO gatea)', len(dias_ok), f'dias {dias_ok[0]}..{dias_ok[-1]} (cobertura desenlace por dia: min {min(meta[d] for d in dias_ok):.4f}); h1 = 06..13, h2 = resto')
    (out / 'n4_backfill_informe.txt').write_text(txt + '\n'); L.INFORMES.mkdir(parents=True, exist_ok=True); (L.INFORMES / 'n4_backfill_informe.txt').write_text(txt + '\n'); print(txt)
def cmd_eval(telegram=False):
    hoy = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d'); des = L.read_json(L.TP1 / 'des.json', {}); W = L.dias(L.FWD0, L.FWD1); frames = []; ok = []; estados = {}
    for d in W:
        mf = L.read_json(P.dirs() / f'tp1_{d}.json'); r = carga(d, des) if mf else None
        if r is None: estados[d] = 'AUSENTE' if d < hoy else 'FUTURO'; continue
        C, cob = r; v = mf['estado'] == 'COMPLETE' and cob >= COB_MIN; estados[d] = 'VALIDO' if v else f"INVALIDO({mf['estado']},cob={cob:.3f})"
        if v: frames.append(C); ok.append(d)
    L.TP1.mkdir(parents=True, exist_ok=True)
    if not ok:
        txt = f'N4 informe {hoy}: 0 dias validos aun. Estados: {estados}'
    else:
        C = pd.concat(frames, ignore_index=True); R = minera(C, ok, W[4]); R = refina(R, C); R.to_csv(L.TP1 / 'n4_celdas_ultimo.csv', index=False)
        final = len(ok) >= P.NDIAS; X_ = cruza(R) if final else pd.Series(False, index=R.index)
        txt = texto(R, f'N4 FORWARD informe {hoy}', len(ok), f"{'FINAL' if final else 'ACUMULANDO ' + str(len(ok)) + '/10 (condiciones solo informativas)'}; estados {estados}")
        if final: txt += f"\nVEREDICTO: {'CRUZA el gate (celdas: ' + str(int(X_.sum())) + ')' if X_.any() else 'NO cruza (ninguna celda cumple todo)'}"
        if telegram and final and X_.any():
            latch = L.read_json(L.TP1 / 'n4_telegram_latch.json', {})
            for _, r in R[X_].iterrows():
                k = f"{r.coin}|{r.bucket}|{r['T']}|{r.lado}"
                if k not in latch and L.telegram(f"MAPA-ESCALA N4 (5m 0.00-0.10) CRUZA el gate (EXPLORATORY): {k} EV {r.ev:+.3f}, IC90 cierre lo {r.ic_lo_cierre:+.3f}, dias+ {r.dias_pos}/10, sin5 {r.ev_sin5:+.3f}, q_BH {r.q_bh:.3f}, top1 wallet {r.top1_wallet:.0%}, {r.cierres} cierres. Ver datalogs/mapa_tp1_informes/n4_informe_ultimo.txt"): latch[k] = L.now()
            L.atomic_json(L.TP1 / 'n4_telegram_latch.json', latch)
    L.INFORMES.mkdir(parents=True, exist_ok=True); [(b / f'n4_informe_{hoy}.txt').write_text(txt + '\n') or (b / 'n4_informe_ultimo.txt').write_text(txt + '\n') for b in (L.TP1, L.INFORMES)]; print(txt)
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('cmd', choices=['backfill', 'eval']); ap.add_argument('--telegram', action='store_true'); a = ap.parse_args()
    cmd_backfill() if a.cmd == 'backfill' else cmd_eval(a.telegram)
