#!/usr/bin/env python3
"""tp1.py - TP1 forward pasivo del MAPA-ESCALA (PREREG_TESTS.md sha 4ec2741a...): repite s2->s6 (misma aritmetica que scripts/s2_celdas.py y
s4b_nichos.py/s5_estadisticos.py) sobre los dias nuevos 24-Oct..02-Nov para tres nichos CONGELADOS:
  N1 = 5m BTC [0.20,0.30) gate EV>=+0.02 | N2 = 15m ETH [0.70,0.99) gate EV>=+0.01 | N3 = 5m todas [0.90,0.99) gate EV>=+0.005
con T en (60, L] (5m: (60,300], 15m: (60,900]), EV ponderado por EUR (sum pnl / sum coste, SIN rebate), desenlace OFICIAL, rellenos MAKER on-chain.
Gate por nicho (TODOS): EV>=umbral, IC90 por dias (bootstrap 2000, seed 20261023) con limite inferior >0, >=7 de 10 dias positivos, EV sin los 5 mejores
cierres >0. Subcomandos: dia D | resolver | eval [--telegram]. Idempotente: celdas por dia atomicas; el resolutor solo anade desenlaces."""
import sys, json, argparse, os, datetime as dt, glob
import numpy as np, pandas as pd
from pathlib import Path
import infra_lib as L, tokmap as T
NICHOS = {
 'N1': dict(marco='5min', coins=['BTC'], bandas=[3], tb=(1, 2), gate=0.02, nombre='5m BTC [0.20,0.30)'),
 'N2': dict(marco='15min', coins=['ETH'], bandas=[6, 7], tb=(1, 3), gate=0.01, nombre='15m ETH [0.70,0.99)'),
 'N3': dict(marco='5min', coins=None, bandas=[7], tb=(1, 2), gate=0.005, nombre='5m todas [0.90,0.99)')}
EDG = np.array([0.01, 0.05, 0.10, 0.20, 0.30, 0.50, 0.70, 0.90, 0.99]); TEDG = np.array([-5, 60, 150, 300, 900, 3600])
NDIAS = 10; COB_MIN = 0.995; MIN_TOK = {'5min': 6500, '15min': 2200}   # tokens/dia observados 6.986-7.022 y 2.348-2.364 (18..21-Oct)
def dirs(): return L.TP1 / 'dia'
def onchain(marco, d): return L.VOL / f'{L.PREF[marco]}_onchain' / f'{L.PREF[marco]}_onchain_{d}.csv.gz'
# ---------------------------------------------------------------- dia
def calcula_marco(d, marco, tk):
    ids = set(tk); cols = ['tipo', 'ts_est', 'tx', 'log_index', 'maker', 'taker', 'side', 'token_id', 'maker_amt', 'taker_amt']
    parts = []; nrow = 0
    for x in pd.read_csv(onchain(marco, d), usecols=cols, dtype={'token_id': str, 'tx': str, 'maker': str, 'taker': str}, chunksize=300000):
        x = x[(x.tipo == 'F') & (x.taker != L.EXCH) & x.token_id.isin(ids)]
        if len(x) == 0: continue
        nrow += len(x); tkv = x.token_id.values
        coin = np.array([tk[t][0] for t in tkv]); mid = np.array([tk[t][2] for t in tkv]); fin = np.array([tk[t][3] for t in tkv], float); lado = np.array([tk[t][4] for t in tkv])
        venta = x.side.values == 1
        acc = np.where(venta, x.maker_amt.values, x.taker_amt.values).astype(float); usdc = np.where(venta, x.taker_amt.values, x.maker_amt.values).astype(float)
        lc = np.where(venta, np.where(lado == 'YES', 'NO', 'YES'), lado)
        with np.errstate(all='ignore'):
            pc = np.where(venta, 1 - usdc / acc, usdc / acc); coste = np.where(venta, acc - usdc, usdc)
        parts.append(pd.DataFrame(dict(tx=x.tx.values, li=x.log_index.values, coin=coin, mid=mid, fin=fin, T=fin - x.ts_est.astype(float).values, lc=lc, pc=pc, coste=coste, acc=acc, maker=x.maker.str.lower().values)))
    if not parts: return pd.DataFrame(), 0, 0
    X = pd.concat(parts, ignore_index=True); n0 = len(X); X = X.drop_duplicates(['tx', 'li']); ndup = n0 - len(X)
    return X, nrow, ndup
def clasifica(X):
    X = X[(X.acc > 0) & (X.coste > 0) & (X.pc >= 0.01) & (X.pc < 0.99) & (X['T'] >= -5)].copy()
    X['banda'] = np.digitize(X.pc.values, EDG) - 1; X['tb'] = np.digitize(X['T'].values, TEDG) - 1; X['reb'] = 0.014 * (1 - X.pc) * X.coste
    return X
def dia(d, forzar=False):
    import n4 as N4        # import tardio (n4 importa tp1)
    f = dirs() / f'celdas_{d}.csv.gz'; mf = dirs() / f'tp1_{d}.json'
    old = L.read_json(mf)
    if old and old.get('estado') == 'COMPLETE' and f.exists() and (dirs() / f'celdas_n4_{d}.csv.gz').exists() and not forzar:
        L.log(f'{d}: celdas ya COMPLETE (idempotente, sin recalcular)'); return old
    man = dict(dia=d, inicio=L.now(), estado='RUNNING', codigo=L.sha_code([__file__, Path(__file__).parent / 'tokmap.py']), fuentes={}, nichos={})
    marcos = ['5min', '15min']; faltan = [m for m in marcos if not onchain(m, d).exists()]
    if faltan:
        man.update(estado='BLOCKED', motivo=f'falta on-chain {faltan}'); L.atomic_json(mf, man); return man
    tks, info = T.tokens_dia(d, marcos); man['tokens_info'] = info
    ex = L.read_json(L.INFRA / 'runs' / f'extract_{d}.json', {}).get('marcos', {})
    res = []; valido = True; motivos = []
    for m in marcos:
        st = ex.get(m, {}).get('estado', 'sin_manifest_extraccion')
        man['fuentes'][m] = dict(bytes=onchain(m, d).stat().st_size, estado_extraccion=st, n_tokens=len(tks[m]))
        if not (st.startswith('COMPLETE') or st == 'sin_manifest_extraccion'): valido = False; motivos.append(f'extraccion {m}={st}')
        if st == 'sin_manifest_extraccion':       # extraido por el cron antiguo de las 04:10: comprobar plausibilidad por tamano
            import extrae_onchain_ext as E
            if E.estado_previo(m, d) != 'ok': valido = False; motivos.append(f'{m} on-chain truncado por tamano')
        if len(tks[m]) < MIN_TOK[m]: valido = False; motivos.append(f'mapa tokens {m}={len(tks[m])} incompleto')
        if not tks[m]: continue
        X, nrow, ndup = calcula_marco(d, m, tks[m])
        man['fuentes'][m].update(fills_maker=int(nrow), duplicados=int(ndup))
        if len(X) == 0: valido = False; motivos.append(f'{m} sin fills'); continue
        X = clasifica(X)
        if m == '5min': n4c = N4.celdas(X); n4tmp = dirs() / f'celdas_n4_{d}.csv.gz.tmp'; dirs().mkdir(parents=True, exist_ok=True); n4c.to_csv(n4tmp, index=False, compression='gzip'); os.replace(n4tmp, dirs() / f'celdas_n4_{d}.csv.gz')
        for k, n in NICHOS.items():
            if n['marco'] != m: continue
            S = X[X.banda.isin(n['bandas']) & X.tb.between(*n['tb'])]
            if n['coins']: S = S[S.coin.isin(n['coins'])]
            g = S.groupby(['coin', 'mid', 'lc', 'maker'], sort=False).agg(coste=('coste', 'sum'), acc=('acc', 'sum'), reb=('reb', 'sum'), nf=('coste', 'size'), fin=('fin', 'first')).reset_index()
            g.insert(0, 'nicho', k); res.append(g)
            man['nichos'][k] = dict(coste=float(S.coste.sum()), fills=int(len(S)), unidades=int(g[['mid', 'lc']].drop_duplicates().shape[0]), makers=int(g.maker.nunique()))
    C = pd.concat(res, ignore_index=True) if res else pd.DataFrame()
    dirs().mkdir(parents=True, exist_ok=True); tmp = f.with_name(f.name + '.tmp')
    C.to_csv(tmp, index=False, compression='gzip'); os.replace(tmp, f)
    man.update(estado='COMPLETE' if valido else 'PARTIAL', motivos=motivos, celdas=len(C), celdas_sha16=L.sha_file(f), fin=L.now()); L.atomic_json(mf, man)
    L.log(f"{d}: tp1 {man['estado']} {man['nichos']} {motivos}"); return man
# ---------------------------------------------------------------- resolvedor (solo lectura de la cache compartida; cache propia)
def resolver(dias_):
    import requests
    own = L.read_json(L.TP1 / 'des.json', {}); shared = L.read_json(L.ROOT / 'maker_ms_desenlaces_cache.json', {})
    mids = set()
    for d in dias_:
        f = dirs() / f'celdas_{d}.csv.gz'
        if f.exists(): mids |= set(pd.read_csv(f, usecols=['mid'], dtype={'mid': str}).mid)
    for m in mids:
        if m not in own and shared.get(m) in ('YES', 'NO'): own[m] = shared[m]
    pend = sorted(m for m in mids if m not in own); S = requests.Session(); nres = 0; err = 0
    for k in range(0, len(pend), 40):
        try:
            r = S.get('https://gamma-api.polymarket.com/markets', timeout=20, params=[('id', x) for x in pend[k:k + 40]] + [('closed', 'true'), ('limit', '40')]); r.raise_for_status()
            for m in r.json() or []:
                pr = m.get('outcomePrices'); pr = json.loads(pr) if isinstance(pr, str) else pr
                if pr and float(pr[0]) >= 0.999: own[str(m['id'])] = 'YES'; nres += 1
                elif pr and float(pr[1]) >= 0.999: own[str(m['id'])] = 'NO'; nres += 1
        except Exception as e: err += 1; L.log(f'resolver lote {k // 40}: {type(e).__name__}')
    L.atomic_json(L.TP1 / 'des.json', own)
    L.log(f'resolver: {len(mids)} mercados, {len(pend)} pendientes, {nres} resueltos ahora, {len(pend) - nres} sin desenlace, {err} errores gamma'); return own
# ---------------------------------------------------------------- estadistica
def boot_days(p, c, B=2000, seed=20261023):
    rng = np.random.default_rng(seed); n = len(p); idx = rng.integers(0, n, (B, n)); s = p[idx].sum(1); cc = c[idx].sum(1)
    ev = s / np.where(cc > 0, cc, np.nan); ev = ev[np.isfinite(ev)]; return float(np.quantile(ev, .05)), float(np.quantile(ev, .95))
def boot_fin(p, c, B=1000, seed=20261024):
    n = len(p)
    if n < 5: return (np.nan, np.nan)
    rng = np.random.default_rng(seed); cnt = rng.multinomial(n, np.ones(n) / n, size=B).astype(np.float64); s = cnt @ p; cc = cnt @ c
    ev = s / np.where(cc > 0, cc, np.nan); ev = ev[np.isfinite(ev)]; return float(np.quantile(ev, .05)), float(np.quantile(ev, .95))
def carga_dia(d, des):
    """-> {nicho: DataFrame(coin,mid,lc,maker,coste,acc,reb,nf,fin,pnl,con_des)} con pnl = acc*gana - coste."""
    C = pd.read_csv(dirs() / f'celdas_{d}.csv.gz', dtype={'mid': str, 'maker': str, 'lc': str}); C['des'] = C.mid.map(des); C['con_des'] = C.des.notna()
    C['pnl'] = np.where(C.con_des, C.acc * (C.lc == C.des).astype(float) - C.coste, 0.0)
    return {k: g for k, g in C.groupby('nicho')}
def evalua(des, hoy=None):
    hoy = hoy or dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d'); W = L.dias(L.FWD0, L.FWD1); out = {}
    for k, n in NICHOS.items():
        filas = []; fin_p = {}; mk = {}
        for d in W:
            mf = L.read_json(dirs() / f'tp1_{d}.json')
            if not mf or not (dirs() / f'celdas_{d}.csv.gz').exists(): filas.append(dict(dia=d, estado='AUSENTE' if d < hoy else 'FUTURO')); continue
            g = carga_dia(d, des).get(k)
            coste = float(g.coste.sum()) if g is not None else 0.0; cd = float(g[g.con_des].coste.sum()) if g is not None else 0.0
            cob = cd / coste if coste > 0 else np.nan
            ok = mf['estado'] == 'COMPLETE' and (coste > 0) and cob >= COB_MIN
            fila = dict(dia=d, estado='VALIDO' if ok else f"INVALIDO({mf['estado']},cob={cob:.3f})" if coste > 0 else 'INVALIDO(sin_coste)', coste=coste, cobertura=cob)
            if g is not None and ok:
                fila.update(pnl=float(g.pnl.sum()), reb=float(g.reb.sum()), unidades=int(g[['mid', 'lc']].drop_duplicates().shape[0]), makers=int(g.maker.nunique()))
                for fin, v in g.groupby('fin')[['pnl', 'coste']].sum().iterrows(): a = fin_p.setdefault((d, fin), [0, 0]); a[0] += v.pnl; a[1] += v.coste
                for m, v in g.groupby('maker').coste.sum().items(): mk[m] = mk.get(m, 0) + v
            filas.append(fila)
        V = [f for f in filas if f['estado'] == 'VALIDO']; r = dict(nicho=k, nombre=n['nombre'], gate_ev=n['gate'], dias=filas, n_validos=len(V))
        if V:
            p = np.array([f['pnl'] for f in V]); c = np.array([f['coste'] for f in V]); ev = p.sum() / c.sum()
            lo, hi = boot_days(p, c) if len(V) >= 2 else (np.nan, np.nan)
            fp = np.array([v[0] for v in fin_p.values()]); fc = np.array([v[1] for v in fin_p.values()]); o = np.argsort(-fp)[:5]; keep = np.ones(len(fp), bool); keep[o] = False
            ev5 = fp[keep].sum() / fc[keep].sum() if keep.sum() and fc[keep].sum() > 0 else np.nan
            flo, fhi = boot_fin(fp, fc); mt = sum(mk.values()); top1 = max(mk.values()) / mt if mt else np.nan
            r.update(ev=float(ev), ev_con_rebate=float((p.sum() + sum(f['reb'] for f in V)) / c.sum()), ic90_dias=[lo, hi], ic90_cierre=[flo, fhi], dias_pos=int((p > 0).sum()), ev_sin5=float(ev5), cierres=len(fp),
                     coste_total=float(c.sum()), top1_maker=float(top1), unidades=int(sum(f['unidades'] for f in V)))
            r['cond'] = dict(ev=bool(ev >= n['gate']), ic_lo=bool(lo > 0), pos7=bool((p > 0).sum() >= 7), sin5=bool(ev5 > 0))
        pendientes = [f['dia'] for f in filas if f['estado'] in ('FUTURO',)]
        if r['n_validos'] >= NDIAS: r['veredicto'] = 'PASA' if all(r['cond'].values()) else 'NO_PASA'
        elif not pendientes: r['veredicto'] = 'INCOMPLETO(<10 dias validos)'
        else: r['veredicto'] = f"ACUMULANDO {r['n_validos']}/{NDIAS}"
        out[k] = r
    return out
def informe(ev, hoy):
    L_ = [f'MAPA-ESCALA TP1 informe {hoy} (PREREG_TESTS sha 4ec2741a; ventana {L.FWD0}..{L.FWD1}; EV ponderado por EUR sin rebate; EXPLORATORY hasta 10 dias)']
    for k, r in ev.items():
        L_.append(f"\n[{k}] {r['nombre']}  gate EV>={r['gate_ev']}  dias validos {r['n_validos']}/{NDIAS}  -> {r['veredicto']}")
        if 'ev' in r:
            c = r['cond']; L_.append(f"  EV {r['ev']:+.4f} (IC90 dias {r['ic90_dias'][0]:+.4f},{r['ic90_dias'][1]:+.4f}; cierre {r['ic90_cierre'][0]:+.4f},{r['ic90_cierre'][1]:+.4f}) con rebate inferido {r['ev_con_rebate']:+.4f}; "
                     f"dias+ {r['dias_pos']}/{r['n_validos']}; EV sin 5 mejores cierres {r['ev_sin5']:+.4f}; cierres {r['cierres']}; unidades {r['unidades']}; coste {r['coste_total']:,.0f}; top1 maker {r['top1_maker']:.1%}")
            L_.append(f"  condiciones (informativas hasta 10 dias): EV>=gate {c['ev']} | IC90 dias lo>0 {c['ic_lo']} | >=7 dias+ {c['pos7']} | sin5 >0 {c['sin5']}")
        for f in r['dias']:
            if f['estado'] == 'VALIDO': L_.append(f"  {f['dia']}  EV {f['pnl'] / f['coste']:+.4f}  pnl {f['pnl']:+,.0f}  coste {f['coste']:,.0f}  unid {f['unidades']}  cob {f['cobertura']:.4f}")
            elif f['estado'] != 'FUTURO': L_.append(f"  {f['dia']}  {f['estado']}")
    return '\n'.join(L_)
def cmd_eval(telegram=False):
    hoy = dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d'); des = L.read_json(L.TP1 / 'des.json', {}); ev = evalua(des, hoy)
    txt = informe(ev, hoy); L.TP1.mkdir(parents=True, exist_ok=True)
    (L.TP1 / f'informe_{hoy}.txt').write_text(txt + '\n'); (L.TP1 / 'informe_ultimo.txt').write_text(txt + '\n'); L.atomic_json(L.TP1 / 'eval_ultimo.json', ev); print(txt)
    if telegram:                    # SOLO al cerrar el gate (veredicto definitivo), una vez por nicho
        latch = L.read_json(L.TP1 / 'telegram_latch.json', {})
        for k, r in ev.items():
            v = r['veredicto']
            if v in ('PASA', 'NO_PASA') or v.startswith('INCOMPLETO'):
                if latch.get(k) != v:
                    ok = L.telegram(f"MAPA-ESCALA TP1 {k} {r['nombre']}: {v} (EXPLORATORY; {r['n_validos']} dias validos). EV {r.get('ev', float('nan')):+.4f} gate {r['gate_ev']}, IC90 dias {r.get('ic90_dias')}, dias+ {r.get('dias_pos')}, sin5 {r.get('ev_sin5')}. Informe: datalogs/mapa_tp1/informe_ultimo.txt")
                    if ok: latch[k] = v
        L.atomic_json(L.TP1 / 'telegram_latch.json', latch)
    return ev
if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('cmd', choices=['dia', 'resolver', 'eval']); ap.add_argument('dias', nargs='*'); ap.add_argument('--forzar', action='store_true'); ap.add_argument('--telegram', action='store_true')
    a = ap.parse_args()
    if a.cmd == 'dia':
        for d in a.dias: dia(d, a.forzar)
    elif a.cmd == 'resolver': resolver(a.dias or [d for d in L.dias(L.FWD0, L.FWD1) if (dirs() / f'celdas_{d}.csv.gz').exists()])
    else: cmd_eval(a.telegram)
