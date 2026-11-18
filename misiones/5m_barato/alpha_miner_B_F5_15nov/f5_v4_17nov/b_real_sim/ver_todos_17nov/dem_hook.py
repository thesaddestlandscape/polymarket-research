#!/usr/bin/env python3
"""dem_hook.py (ver_todos_17nov, 17-Nov) -- CINTA DE DEMANDA TOMADORA RESIDUAL para el replay de B. SOLO LECTURA, 0 ordenes.
Mecanismo: cada tx matchOrders lleva la orden del TOMADOR (calldata: makerAmount/takerAmount -> limite y tamano total S_T). Si el tomador
vende nuestro token (side 1) o compra el complementario (side 0, via mint), su demanda alcanza las pujas de nuestro token hasta el precio
equivalente eq. Demanda residual SIN NOSOTROS = S_T - acciones casadas con makers AJENOS en ese tx. Si eq <= L y residual > 0, una puja nuestra
en L en la vida simulada habria recibido esa demanda -> se inyecta un print sintetico (t = sello v3 del tx, precio L, tamano residual) y el motor
engine_v4 aplica la cola en L como con cualquier print. Anti-circularidad: (r) solo tx que EXISTIRIAN sin nosotros (>=1 maker ajeno); (e) ademas
sin ninguna fila nuestra en el tx; (all) incluye tx solo-nuestros = CIRCULAR, solo cota diagnostica. Placebos: eventos desplazados +-30 s.
Pasada 1 (DEM_PASS=1): escribe out/needed_<d>.txt con los tx sin calldata y sale. Pasada 2: calcula."""
import os, sys, json, numpy as np, pandas as pd
EX = '0xe111180000d2663c0091e4f400237545b87b996b'; TOLP = 0.0049; FLOOR = 1e-3
HD = os.path.dirname(os.path.abspath(__file__)) + '/'
CACHES = ['/root/polymarket-research-datalogs/cola_posicion/calldata_b.jsonl', HD + 'calldata_extra.jsonl', HD + 'calldata_dem.jsonl']
SHIFT = 30000


def _parse_taker(inp):
    b = bytes.fromhex(inp[10:]); w = lambda i: int.from_bytes(b[i:i + 32], 'big'); s = w(32)
    f = [w(s + 32 * k) for k in range(12)]
    return dict(tok=str(f[3]), mA=f[4], tA=f[5], side=f[6], ts=f[8])


def construir(D, RAW, FM_ALL, evA, tm3, OWN, d, OUT):
    O = pd.read_csv('/root/polymarket-research-datalogs/calibracion_etiqueta/ordenes_b.csv', dtype={'tok': str}); O = O[O.dia == d]
    ks = {D.tokidx.get(str(t)) for t in O.tok} - {None}
    win = {}
    for r in O.itertuples():
        k = D.tokidx.get(str(r.tok))
        if k is None: continue
        fin = r.t_cancel_int if np.isfinite(r.t_cancel_int) else r.cie - 60
        win.setdefault(k, []).append((int(r.t_call0 * 1000) - SHIFT - 1000, int(max(fin, r.t_fuera if np.isfinite(r.t_fuera) else fin) * 1000) + SHIFT + 1000))
    raw = RAW.copy(); raw['taker'] = raw.taker.str.lower(); raw['maker'] = raw.maker.str.lower()
    S = raw[(raw.tipo == 'F') & (raw.taker == EX)].drop_duplicates('tx')[['tx', 'maker', 'token_id', 'side']]
    fm = FM_ALL.copy(); fm['own'] = fm.maker == OWN
    agg = fm.groupby('tx').agg(f_aj=('sh', lambda s: 0.0), n=('sh', 'size')).reset_index()
    f_aj = fm[~fm.own].groupby('tx').sh.sum(); f_own = fm[fm.own].groupby('tx').sh.sum(); n_aj = fm[~fm.own].groupby('tx').size()
    tmap = {}
    for (k, tx), t in zip(zip(evA.k.values, evA.tx.values), tm3):
        tmap.setdefault(tx, {})[int(k)] = int(t)
    ev = []
    for r in S.itertuples():
        kt = D.tokidx.get(str(r.token_id))
        if kt is None: continue
        ktar = kt if r.side == 1 else D.comp(kt)
        if ktar is None or ktar not in ks: continue
        tt = tmap.get(r.tx, {}); t = tt.get(ktar, min(tt.values()) if tt else None)
        if t is None: continue
        if not any(a <= t <= b for a, b in win[ktar]): continue
        ev.append(dict(tx=r.tx, k=int(ktar), t=int(t), side=int(r.side), tok=str(r.token_id), f_aj=float(f_aj.get(r.tx, 0.0)), f_own=float(f_own.get(r.tx, 0.0)), n_aj=int(n_aj.get(r.tx, 0))))
    ev = pd.DataFrame(ev)
    have = {}
    for c in CACHES:
        if os.path.exists(c):
            for l in open(c):
                j = json.loads(l); have[j['tx']] = j['input']
    falta = sorted(set(ev.tx) - set(have)) if len(ev) else []
    if os.environ.get('DEM_PASS') == '1':
        open(OUT + f'needed_{d}.txt', 'w').write('\n'.join(falta)); print('DEM pasada1', d, 'eventos', len(ev), 'faltan calldata', len(falta), flush=True); sys.exit(0)
    assert not falta or os.environ.get('DEM_ALLOW_MISSING') == '1', ('faltan calldata', len(falta))
    eq = []; sz = []; ok = []
    for r in ev.itertuples():
        inp = have.get(r.tx)
        if inp is None or not inp.startswith('0x3c2b4399'): eq.append(np.nan); sz.append(np.nan); ok.append('sin_calldata'); continue
        tk = _parse_taker(inp)
        if tk['tok'] != r.tok or tk['side'] != r.side: eq.append(np.nan); sz.append(np.nan); ok.append('discrepa'); continue
        if r.side == 1: eq.append(tk['tA'] / tk['mA']); sz.append(tk['mA'] / 1e6)
        else: eq.append(1 - tk['mA'] / tk['tA']); sz.append(tk['tA'] / 1e6)
        ok.append('ok')
    ev['eq'] = eq; ev['S_T'] = sz; ev['dec'] = ok; ev['resid'] = ev.S_T - ev.f_aj
    ev.to_pickle(OUT + f'DEMEV_{d}.pkl')
    print('DEM eventos', len(ev), ev.dec.value_counts().to_dict(), 'resid>0', int((ev.resid > FLOOR).sum()), flush=True)
    return {k: g.sort_values('t') for k, g in ev[ev.dec == 'ok'].groupby('k')}


D_TAKER = 150   # ms: retraso del tomador (FOK +145 ms medido 07-Oct; casado ~215 ms tras envio). Variante C150: un print hasta te+150 cuenta si el tomador ENTRO antes de nuestra cancelacion


def _cola(D, k, L, ta, te, size, cola, qupd3):
    """COLA: (1) si a la llegada hay puja > L, cola delante = 'cola' de B en t_dec (L2 propio, causal) en vez de INF; (2) las filas de libro en L del sa_ms real
    incluyen NUESTRA orden real: se resta nuestro tamano (solo replay de ordenes reales)."""
    bk = D.book(k, ta)
    if bk is None: return None, None
    bid, ask, bsz, x = bk
    if bid > L + 1e-6 and np.isfinite(cola): bk = (L, ask, float(cola), x)
    q = qupd3(k, L, ta, te); q = (q[0], q[1], np.clip(np.asarray(q[2], float) - size, 0, None), q[3] - size if len(q) > 3 else None)
    return bk, q


def variantes(DEM, D, k, L, ta, te, size, tape, qupd3, E4, cola=np.nan):
    out = {}; g = DEM.get(k)
    for v, te2, usa_cola, usa_dem in (('C150', te + D_TAKER, False, False), ('COLA', te, True, False), ('COLA_C150', te + D_TAKER, True, False), ('DEMr_COLA_C150', te + D_TAKER, True, True), ('DEMr_COLA', te, True, True), ('DEMr_COLA_p30', te, True, 30000), ('DEMr_COLA_m30', te, True, -30000)):
        pt2, pp2, ps2 = tape.get(k, L, ta, te2)
        if usa_dem and g is not None:
            sh_ = 0 if usa_dem is True else int(usa_dem); t2_ = g.t.values + sh_
            m = (g['eq'].values <= L + TOLP) & (g.resid.values > FLOOR) & (g.n_aj.values > 0) & (t2_ >= ta) & (t2_ <= te2)
            st = t2_[m].astype(np.int64); ss = g.resid.values[m].astype(float)
            T_ = np.concatenate([np.asarray(pt2, np.int64), st]); P_ = np.concatenate([np.asarray(pp2, float), np.full(len(st), L)]); Z_ = np.concatenate([np.asarray(ps2, float), ss]); o = np.argsort(T_, kind='stable')
            pt2, pp2, ps2 = T_[o], P_[o], Z_[o]
        if usa_cola: bk, q = _cola(D, k, L, ta, te2, size, cola, qupd3)
        else: bk, q = D.book(k, ta), qupd3(k, L, ta, te2)
        qq, tf, mot = E4.fill_segment_v4(bk, 0.0, q, (pt2, pp2, ps2), L, ta, te2, size, 'BASE', dedupe=True)
        out[f'{v}_f_q'] = float(qq); out[f'{v}_f_tf'] = int(tf) if E4.es_fill(qq) else -1
    pt, pp, ps = tape.get(k, L, ta, te)
    sel_base = None if g is None else ((g['eq'].values <= L + TOLP) & (g.resid.values > FLOOR))
    for v, mask_fn, sh in (('DEMr', lambda g: g.n_aj.values > 0, 0), ('DEMe', lambda g: (g.n_aj.values > 0) & (g.f_own.values <= 0), 0),
                           ('DEMall', lambda g: np.ones(len(g), bool), 0), ('DEMr_p30', lambda g: g.n_aj.values > 0, SHIFT), ('DEMr_m30', lambda g: g.n_aj.values > 0, -SHIFT)):
        if g is None: st = np.array([], np.int64); ss = np.array([])
        else:
            t2 = g.t.values + sh; m = sel_base & mask_fn(g) & (t2 >= ta) & (t2 <= te); st = t2[m].astype(np.int64); ss = g.resid.values[m].astype(float)
        if len(st) == 0:
            q, tf, mot = E4.fill_segment_v4(D.book(k, ta), 0.0, qupd3(k, L, ta, te), (pt, pp, ps), L, ta, te, size, 'BASE', dedupe=True)
        else:
            T_ = np.concatenate([np.asarray(pt, np.int64), st]); P_ = np.concatenate([np.asarray(pp, float), np.full(len(st), L)]); Z_ = np.concatenate([np.asarray(ps, float), ss])
            o = np.argsort(T_, kind='stable'); q, tf, mot = E4.fill_segment_v4(D.book(k, ta), 0.0, qupd3(k, L, ta, te), (T_[o], P_[o], Z_[o]), L, ta, te, size, 'BASE', dedupe=True)
        out[f'{v}_f_q'] = float(q); out[f'{v}_f_tf'] = int(tf) if E4.es_fill(q) else -1; out[f'{v}_nsint'] = int(len(st))
    return out
