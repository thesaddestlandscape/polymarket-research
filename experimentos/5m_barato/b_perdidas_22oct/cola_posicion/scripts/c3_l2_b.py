#!/usr/bin/env python3
"""c3_l2_b.py -- PREREG_COLA (sha a72007c5...). Reconstruye el nivel (token c, precio pc) del libro L2 (libro5 extraido por cola_vs_cruce, lado bids; el libro es
unificado: incluye SELL del complemento) para cada ORDEN de B con relleno: tamano justo antes de verse nuestra orden (A0_book), contraste con la cola del ledger (A0_ledger),
instante de la rafaga (print WS que casa con la suma de acciones del mismo nivel de la tx), tamano antes de la rafaga (S_pre), consumo previo por prints y no explicado (cancelaciones).
Tiempos = RECEPCION del recorder (ms). Salida datos/b_l2.csv."""
import json, hashlib, gzip, os, numpy as np, pandas as pd
AQ = os.path.dirname(os.path.abspath(__file__)); D = os.path.join(AQ, '..', 'datos'); DL = '/root/polymarket-research-datalogs/cola_posicion/'
assert hashlib.sha256(open(os.path.join(AQ, '..', 'prereg', 'PREREG_COLA.md'), 'rb').read()).hexdigest().startswith('a72007c5deecc5e7')
TM = json.load(open('/root/polymarket-research-datalogs/cola_vs_cruce/tokens.json'))
O = {o['oid']: o for o in json.load(open(DL + 'ordenes_b.json'))}
TOK = {}
for l in open(DL + 'snap/ledger_B.jsonl'):
    d = json.loads(l)
    if d.get('tipo') == 'intencion_post': TOK[d['oid']] = d['tok']
Bq = pd.read_csv(os.path.join(D, 'b_barridos.csv')); Bq = Bq[Bq.es_primera == 1]
def mills(p): return int(round(float(p) * 1000))
def carga(act, mid, L, pc):
    """-> niveles [(r, size)] de (L, pc) y prints de consumo [(r, acc)] del nivel; 'G' (huecos) [r]"""
    lv = []; pr = []; gaps = []; key = f'{pc:.2f}'
    other = 'N' if L == 'Y' else 'Y'; pcm = mills(pc)
    with gzip.open(f'/root/polymarket-research-datalogs/cola_vs_cruce/mk/{act}_{mid}.gz', 'rt') as f:
        for ln in f:
            c = ln.rstrip('\n').split(',')
            ty = c[1]
            if ty == 'd':
                if c[0] == L and mills(c[3]) == pcm: lv.append((int(c[2]), float(c[4])))
            elif ty == 'B':
                if c[0] == L:
                    s = 0.0
                    for x in c[3].split(';'):
                        if x.startswith(key + ':'): s = float(x.split(':')[1]); break
                    lv.append((int(c[2]), s))
            elif ty == 'T':
                q = mills(c[4]); a = float(c[5]); r = int(c[2])
                if c[0] == L and c[3] == 'SELL' and q == pcm: pr.append((r, a))
                elif c[0] == other and c[3] == 'BUY' and 1000 - q == pcm: pr.append((r, a))
            elif ty == 'G' and c[0] == L: gaps.append(int(c[2]))
    return lv, pr, gaps
rows = []
for _, r in Bq.iterrows():
    o = O[r.oid]; t = TOK[r.oid]
    out = dict(oid=r.oid, coin=r.coin, pc=r.pc, size=o['size'], acc=r.acc, A0_ledger=o['cola'], tdec=o['t_dec'], tcall=o.get('t_call0'), tret=o.get('t_ret'), t_visto=o.get('t_visto'), ts_chain=r.ts_chain)
    if t not in TM: out['l2'] = 'sin_mapa_tokens'; rows.append(out); continue
    act, mid, lado, fin = TM[t]; L = 'Y' if lado == 'YES' else 'N'
    try: lv, pr, gaps = carga(act, mid, L, r.pc)
    except FileNotFoundError: out['l2'] = 'sin_fichero'; rows.append(out); continue
    out.update(mid=mid, fin=fin)
    if not lv: out['l2'] = 'nivel_sin_datos'; rows.append(out); continue
    tl = np.array([x[0] for x in lv]); sz = np.array([x[1] for x in lv])
    def S(tms):                                # tamano del nivel con recepcion <= tms
        i = np.searchsorted(tl, tms, 'right') - 1
        return sz[i] if i >= 0 else np.nan
    tc = int(o['t_call0'] * 1000)
    # llegada de nuestra orden: primer salto de +size (+-0,011) con recepcion en [t_call0, t_ret+500 ms]
    lo, hi = tc, int(o['t_ret'] * 1000) + 500
    arr = None
    for i in range(1, len(tl)):
        if lo <= tl[i] <= hi and abs((sz[i] - sz[i - 1]) - o['size']) < 0.011: arr = i; break
    if arr is None:                            # tolera que lleguen otras ordenes en el mismo ms: salto >= size
        for i in range(1, len(tl)):
            if lo <= tl[i] <= hi and (sz[i] - sz[i - 1]) >= o['size'] - 0.011 and (sz[i] - sz[i - 1]) <= o['size'] + 60: arr = i; out['arr_aprox'] = 1; break
    out['l2'] = 'ok'
    out['S_dec'] = S(int(o['t_dec'] * 1000))
    if arr is not None:
        out['t_arr'] = tl[arr]; out['A0_book'] = sz[arr - 1]; out['arr_lat_ms'] = tl[arr] - tc
    else: out['arr_nf'] = 1
    # rafaga: print de consumo del nivel cuya talla casa con la suma de acciones del mismo nivel en la tx, ventana respecto a la hora de bloque
    tot_same = r.sh_ahead_same + r.acc + r.sh_after_same
    # (en la tx de B puede haber filas parciales: se usa la suma del nivel)
    win = [(rr, a) for rr, a in pr if -5.5 <= rr / 1000 - r.ts_chain <= -0.2]
    tk_acc = None
    cand = [(0, abs((rr / 1000 - r.ts_chain) + 2.0), rr, a) for rr, a in win if abs(a - tot_same) <= max(0.03, 0.002 * tot_same)]
    out['print_exacto'] = int(bool(cand))
    if not cand:
        tkacc = Bq.loc[Bq.oid == r.oid, 'taker_acc'].iloc[0]
        cand = [(0, abs((rr / 1000 - r.ts_chain) + 2.0), rr, a) for rr, a in win if abs(a - tkacc) <= max(0.03, 0.002 * tkacc)]
        if cand: out['print_exacto'] = 2
    if not cand and win: cand = [(1, abs((rr / 1000 - r.ts_chain) + 2.0), rr, a) for rr, a in win]
    cand.sort(key=lambda x: (x[0], x[1]))
    if cand:
        m = cand[0][2]; out['t_print'] = m; out['print_acc'] = cand[0][3]
        # tamano antes de la rafaga: ultimo valor con recepcion < t_print - 0 ms que no sea ya la caida (la caida llega ~10 ms antes del print)
        j = np.searchsorted(tl, m, 'right') - 1
        # retrocede mientras el valor sea menor que el anterior en <=60 ms (caida de la rafaga)
        k = j
        while k > 0 and tl[k] > m - 60 and sz[k] < sz[k - 1] - 1e-9 and (sz[k - 1] - sz[k]) <= tot_same + 1e-6 and k > (arr or 0): k -= 1
        out['S_pre'] = sz[k]; out['t_pre'] = tl[k]
        for dt in (1000, 300, 100): out[f'S_m{dt}'] = S(m - dt)
        out['gap_en_vida'] = int(any((out.get('t_arr', tc)) <= g <= m for g in gaps))
        if arr is not None and out['t_arr'] > m: out['print_antes_llegada'] = 1
        elif arr is not None:
            ent = [(rr, a) for rr, a in pr if out['t_arr'] <= rr < m - 1]
            out['F_prev'] = sum(a for _, a in ent); out['n_prints_prev'] = len(ent)
            # tamano minimo del nivel entre llegada y rafaga, y maximo
            seg = sz[(tl >= out['t_arr']) & (tl <= m)]; out['S_min'] = seg.min(); out['S_max'] = seg.max(); out['vida_ms'] = m - out['t_arr']
            # caida no explicada en los 500 ms previos a la rafaga
            pre = sz[(tl >= m - 500) & (tl < m - 60)]
            out['S_500pre_max'] = pre.max() if len(pre) else np.nan
    else: out['sin_print'] = 1
    rows.append(out)
R = pd.DataFrame(rows).merge(Bq[['oid', 'sh_ahead_same', 'sh_after_same', 'n_same', 'rank_same', 'n_better', 'sh_better']], on='oid')
R.to_csv(os.path.join(D, 'b_l2.csv'), index=False)
print(R.l2.value_counts().to_dict(), '| arr encontrada', int(R.A0_book.notna().sum()), '| print', int(R.t_print.notna().sum()), '| S_pre', int(R.S_pre.notna().sum()))
